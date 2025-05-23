# English AI Tutor (Command Line Version)

A simple command-line based AI tutor to practice English conversation.
This is the initial version focusing on text-based interaction.

## How to Run

1.  Ensure you have Python 3.x installed on your system.
2.  Clone this repository or download the `english_tutor_cli.py` file.
    To download directly, go to the `english_tutor_cli.py` file in this repository and click the "Raw" button, then save the page.
3.  Open your terminal or command prompt.
4.  Navigate to the directory where `english_tutor_cli.py` is saved.
5.  Run the script using the following command:
    ```bash
    python3 english_tutor_cli.py
    ```
6.  Follow the on-screen prompts to interact with the AI tutor. Type `quit`, `exit`, or `bye` to end the session.

## Current Features (v0.1.0)

*   User inputs questions or statements in English via the command line.
*   A rule-based AI provides responses in English based on predefined patterns.
*   Basic conversation flow for simple interactions.

## Future Ideas

*   Integrate actual speech-to-text (ASR) for voice input.
*   Integrate actual text-to-speech (TTS) for voice output.
*   Expand the AI's knowledge base and conversational rules.
*   Explore more advanced NLP techniques for better understanding.
*   Consider porting to other platforms (e.g., Web, Mobile App).

## Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check [issues page](https://github.com/jinv2/english-ai-tutor-cli/issues) if you want to contribute.
---

## Web-Based Voice Tester (Client-Side TTS, Simulated ASR)

This repository also includes a web-based tool for testing voice interaction concepts.
It allows uploading an audio file (ASR is simulated) and features client-side Text-to-Speech for AI responses.

*   **Access the Web Tester:** [Link to be added after GitHub Pages setup for this file]
*   **File:** `web_tester_client_tts.html`

**Note:** The Automatic Speech Recognition (ASR) from the uploaded audio file is **simulated** in this web version. The Text-to-Speech (TTS) for AI responses is handled directly by your browser.

---

## Web-Based Voice Tester (Client-Side TTS, Simulated ASR)

This repository also includes a web-based tool for testing voice interaction concepts, primarily demonstrating client-side Text-to-Speech (TTS) capabilities of your browser.

*   **Access the Web Tester:** [https://jinv2.github.io/english-ai-tutor-cli/web_tester_client_tts.html](https://jinv2.github.io/english-ai-tutor-cli/web_tester_client_tts.html)
*   **File in this repository:** `web_tester_client_tts.html`

**How it works:**
1.  Upload an English audio file (the content of the audio is not actually processed for transcription).
2.  The page will show a **simulated** transcription of the audio.
3.  It will then generate a **simulated** AI text response.
4.  This AI text response will be automatically spoken aloud using your browser's built-in Text-to-Speech engine.
5.  You can select different available voices (if your browser provides options) and click "Speak AI Response" to hear it again.

**Note:**
*   The Automatic Speech Recognition (ASR) from the uploaded audio file is **purely simulated** in this web version. It does not actually convert your speech to text.
*   The Text-to-Speech (TTS) for AI responses is handled directly by your web browser via the Web Speech API. Voice quality and availability depend on your browser and operating system.
