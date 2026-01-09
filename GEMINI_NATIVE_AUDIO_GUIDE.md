# Gemini 2.5 Native Audio Preview Integration Guide

## Overview
This document outlines the key learnings and configuration requirements for integrating the **Gemini 2.5 Flash Native Audio Preview** model (`gemini-2.5-flash-native-audio-preview-09-2025`) into an application using the Google GenAI Live API.

## Critical Constraints & Requirements

### 1. Native Audio vs. Text Modality
The native audio preview model is optimized for audio interactions but supports text. However, improper configuration in "Text Mode" can lead to connection failures.

*   **Error**: `Connection closed: received 1007 ... Cannot extract voices from a non-audio request`
*   **Cause**: This error occurs when the session is configured for TEXT modality, but the **Automatic Voice Activity Detection (VAD)** is left enabled (default behavior). The model expects an audio stream to perform VAD on, and fails when it receives only text messages.
*   **Fix**: You **must explicitly disable VAD** when initializing a text-only session.

### 2. Language Configuration
Unlike previous models, native audio models **do not support explicit language codes**.

*   **Constraint**: Setting `language_code` (e.g., "pt-BR", "es-ES") in `SpeechConfig` will cause errors or be ignored.
*   **Behavior**: The model automatically detects the language from the input audio or text context.
*   **Fix**: Remove `language_code` from your `SpeechConfig`.

### 3. Modality Exclusivity
*   **Constraint**: You can only set **one** response modality (`TEXT` or `AUDIO`) per session.
*   **Error**: Setting both results in a configuration error.

## Implementation Guide

### Correct Configuration for Text-Only Mode

When initializing a session where `response_modalities=["TEXT"]`:

```python
config = {
    "response_modalities": ["TEXT"],
    "realtime_input_config": {
        "automatic_activity_detection": {
            "disabled": True  # CRITICAL: Must be True for text-only sessions
        }
    }
}
```

### Correct Configuration for Audio Mode

When initializing a session where `response_modalities=["AUDIO"]`:

```python
speech_config = types.SpeechConfig(
    voice_config=types.VoiceConfig(
        prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name="Leda")
    )
    # DO NOT set language_code here
)

config = {
    "response_modalities": ["AUDIO"],
    "speech_config": speech_config,
    "input_audio_transcription": {},  # Enable if you want input transcripts
    "output_audio_transcription": {}  # Enable if you want output transcripts
}
# VAD is enabled by default, which is correct for Audio mode
```

## Troubleshooting Common Errors

| Error Code | Message | Cause | Solution |
|------------|---------|-------|----------|
| **1007** | `Cannot extract voices from a non-audio request` | VAD is enabled on a Text-only session. | Set `automatic_activity_detection.disabled = True`. |
| **1008** | `Policy violation` / `Model not found` | Using an unsupported model version or region. | Check model name and API version compatibility. |
| **Config** | `Invalid value for language_code` | Setting `language_code` for a Native Audio model. | Remove `language_code` from `SpeechConfig`. |

## Code Example (FastAPI / ADK)

```python
# app/main.py

# Create speech config (No language_code!)
speech_config = types.SpeechConfig(
    voice_config=types.VoiceConfig(
        prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name="Leda")
    )
)

# Configure based on modality
if is_audio:
    config = {
        "response_modalities": ["AUDIO"],
        "speech_config": speech_config,
        "input_audio_transcription": {},
        "output_audio_transcription": {}
    }
else:
    # TEXT MODE: Disable VAD to prevent errors
    config = {
        "response_modalities": ["TEXT"],
        "realtime_input_config": {
            "automatic_activity_detection": {"disabled": True}
        }
    }

run_config = RunConfig(**config)
```
