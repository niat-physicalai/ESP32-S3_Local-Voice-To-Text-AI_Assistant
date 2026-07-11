from flask import Flask, request
from faster_whisper import WhisperModel
from ollama import chat
import re



app = Flask(__name__)

print("Loading Whisper...")

whisper = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("Ready")

GPIO_COMMANDS = {
    "LED1 UP",
    "LED1 DOWN",
    "LED2 UP",
    "LED2 DOWN"
}

conversation = [
    {
        "role": "system",
        "content":
        "You are a voice assistant running on an ESP32. "
        "Keep answers short, under 100 words. "
        "Remember information provided by the user."
    }
]

def normalize(text):

    text = text.upper()

    text = text.replace(".", "")
    text = text.replace(",", "")

    text = text.replace("LED 1", "LED1")
    text = text.replace("LED 2", "LED2")

    text = text.replace("ON", "UP")
    text = text.replace("OFF", "DOWN")

    text = text.replace("-0", " UP")
    text = text.replace(" 0", " UP")

    text = text.replace("-1", " DOWN")
    text = text.replace(" 1", " DOWN")
    
    text = text.replace("LED ONE", "LED1")
    text = text.replace("LED TWO", "LED2")

    text = text.replace("TURN ON", "UP")
    text = text.replace("TURN OFF", "DOWN")

    text = text.replace("SWITCH ON", "UP")
    text = text.replace("SWITCH OFF", "DOWN")

    text = " ".join(text.split())

    return text.strip()

@app.route("/ping")
def ping():
    return {"status":"ok"}

@app.route("/transcribe_raw", methods=["POST"])
def transcribe_raw():

    with open("received.wav", "wb") as f:
        f.write(request.data)

    segments, info = whisper.transcribe(
        "received.wav",
        language="en"
    )

    text = " ".join(
        seg.text for seg in segments
    ).strip()

    command = normalize(text)

    # print("USER:", text)
    # print("RAW:", text)
    # print("NORMALIZED:", command)
    print("=" * 50)
    print("RAW:", repr(text))
    print("NORMALIZED:", repr(command))
    print("=" * 50)

    if (
        ("LED" in command)
        and
        (
            "ON" in command
            or "UP" in command
        )
    ):
        return {
            "success": True,
            "type": "gpio",
            "command": "LED1 UP"
        }

    if (
        ("LED" in command)
        and
        (
            "OFF" in command
            or "DOWN" in command
        )
    ):
        return {
            "success": True,
            "type": "gpio",
            "command": "LED1 DOWN"
        }

    conversation.append(
        {
            "role": "user",
            "content": text
        }
    )

    if len(conversation) > 20:
        conversation.pop(0)

#    response = chat(
#        model="qwen2.5:1.5b",
#        messages=[
#            {
#                "role": "user",
#                "content": text
#            }
#        ]
#    )


    response = chat(
        model="qwen2.5:1.5b",
        messages=conversation
    )

    answer = response["message"]["content"][:500]

    conversation.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    if len(conversation) > 20:
        conversation.pop(0)

    return {
        "success": True,
        "type": "answer",
        "question": text,
        "answer": answer
    }

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )