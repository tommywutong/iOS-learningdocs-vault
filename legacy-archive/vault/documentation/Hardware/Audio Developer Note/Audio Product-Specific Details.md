---
title: Audio Developer Note
apple_id: TP40003505
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-04-28'
source_url: https://developer.apple.com/library/archive/documentation/Hardware/Conceptual/HWTech_Audio/Articles/Audio_implementation.html
archived_at: '2026-07-15T07:40:46.070023Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Audio Developer Note](Introduction%20to%20Audio%20Developer%20Note.md)


[Next](Document%20Revision%20History.md)[Previous](Audio%20Concepts.md)

# Audio Product-Specific Details

This article highlights details of the audio system implementation specific to particular Mac computers. Unless otherwise specified in this article, audio support on a Mac computer adheres to the information in [Audio Concepts](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvomk7gezdambtgmytcnrx).

This section provides Audio-specific information for Mac Pro computers introduced beginning August 2006. Refer to the specific Mac Pro developer note for additional information.

The Mac Pro computers with Quad-Core Intel Xeon 5400 Series microprocessors were introduced in January 2008. The Mac Pro has a built-in audio system providing the developer with a set of hardware resources that can be used to record or play audio.

The Mac Pro computer includes four audio output ports that can be used to play audio: a mono internal speaker, headphone output on the front panel, line output on the rear panel, and S/PDIF optical digital output on the rear panel.

The internal mono speaker is automatically selected for audio output if no external device is detected at the front panel headphone port. If an external device is plugged into the front panel headphones port, the internal speaker automatically mutes and the audio stream is shifted to the external device. Both left and right stereo audio content is mixed to mono and played through the speaker. The internal speaker supports bit depths of 16, 20, or 24 bits per sample and sample rates of 44.1 kHz, 48 kHz, or 96 kHz.

The headphone output is automatically selected for audio output if an external device is plugged into the front panel headphones port.  The headphone output supports a stereo data stream at bit depths of 16, 20, and 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz.  The headphone output gain can be adjusted between 0.0 dB to -64 dB, below -64 dB the pin is set to mute where the output is essentially the noise floor or < -90 dB.

During playback of a 1 kHz, full-scale (unless otherwise specified) sine wave (44.1 kHz input sample rate, 24-bit sample depth, 150 Ω load, no weighting) the headphones output has the following nominal specifications:

- Jack type: 1/8” stereo-mini
- Maximum output voltage: 1.4 VRMS
- Output impedance: < 24 Ω
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N) at -3 dBFS output: ~1.0V rms: < -75 dB (0.02%)
- Channel separation: > 50 dB

The line output can be selected in Audio MIDI Setup or Sound Preferences as the audio output device for audio output. The line output supports a stereo data stream at bit depths of 16, 20, and 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. The line output gain can be adjusted between 0.0 dB to -64 dB, below -64 dB the pin is set to Mute where the output is essentially the noise floor or < -90 dB.

During playback of a 1 kHz, full-scale (unless otherwise specified) sine wave (44.1 kHz input sample rate, 24-bit sample depth, 100 kΩ load, no weighting) the line output has the following nominal specifications:

- Jack type: 1/8” stereo-mini
- Maximum output voltage: 1.6 VRMS
- Output impedance: < 24 Ω
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N) at -3dBFS output: ~1.13V rms: < -85 dB (0.006%)
- Channel separation: > 90 dB

The S/PDIF optical digital output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.100 kHz, 48.000 kHz or 96.000 kHz in PCM format. In addition, the S/PDIF optical digital output supports a stereo data stream at 16 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz in AC-3 encoded audio format.

During playback of a 1 kHz, full-scale sine wave (S/PDIF output format, 44.1 kHz output sample rate, 24-bit sample depth, unless otherwise specified) the digital audio output has the following nominal specifications:

- Jack type: TOSLINK friction-lock type F-05
- Digital audio signal-to-noise ratio (SNR): > 130 dB
- Digital audio total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The S/PDIF optical output channel status conforms to IEC 60958-3 consumer mode digital audio.

For a description of the TOSLINK friction-lock type F-05 jack, refer to [7.5 mm Optical Digital Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvonk7gezdambtgmytcnrx).

The Mac Pro includes two audio input ports that can be used for recording. The rear panel of the computer includes a S/PDIF (Toslink) digital input connector and a 1/8” stereo mini-jack.

The line input operates independently from all other audio input ports and is always available. The line input supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the line input is presented as a stereo data stream. The line input gain can be adjusted from -16 dB to +30 dB.

During input of a 1 kHz, full-scale 2 VRMS sine wave (44.1 kHz input sample rate, 24-bit sample depth, 0.0 dB input gain, no weighting) the audio line input has the following nominal specifications:

- Jack type: 1/8” stereo-mini
- Maximum input voltage: 2 VRMS (+8.24 dBu)
- Minimum voltage input for full scale output: 63 mVRMS (-21.8 dBu) at input gain = +30 dB
- Input impedance: > 20 kΩ
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N) at -3 dBFS input: ~1.414V rms: < -85 dB (0.006%)
- Channel separation: > 80 dB

Based on playback of a 1 kHz, -1 dBFS 24-bit sine wave playback, 24-bit 44.1 kHz output sample rate (unless otherwise specified below) the digital audio input and output have the following electrical characteristics (nominal specifications):

- Jack type: TOSLINK friction-lock type F-05
- FSI – input sample rates: 44.1 kHz, 48 kHz, or 96 kHz
- Bits per sample: 16, 20, or 24 bits
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

For a description of the TOSLINK friction-lock type F-05 jack, refer to [7.5 mm Optical Digital Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvonk7gezdambtgmytcnrx).

The quad-core Mac Pro was introduced in August 2006 and the 8-core Mac Pro was introduced in April 2007 as a configure-to-order-option. The Mac Pro has a built-in audio system providing the developer with a set of hardware resources that can be used to record or play audio.

The Mac Pro includes two audio input ports that can be used for recording. The rear panel of the computer includes a S/PDIF (Toslink) digital input connector and a 1/8” stereo mini-jack.

The line input operates independently from all other audio input ports and is always available. The line input supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the line input is presented as a stereo data stream. The line input gain can be adjusted from -16 dB to +20 dB.

During input of a 1 kHz, full-scale 2 VRMS sine wave (44.1 kHz input sample rate, 24-bit sample depth, 0.0 dB input gain, no weighting) the audio line input has the following nominal specifications:

- Jack type: 1/8” stereo-mini
- Maximum input voltage: 2 VRMS (+8.24 dBu)
- Minimum voltage input for full scale output: 63 mVRMS (-21.8 dBu) at input gain = +30 dB
- Input impedance: > 20 kΩ
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N) at -3dBFS input: ~1.414V rms: < -85 dB (0.006%)
- Channel separation: > 80 dB

Based on playback of a 1 kHz, -1 dBFS 24-bit sine wave playback, 24-bit 44.1 kHz output sample rate (unless otherwise specified below) the digital audio input and output have the following electrical characteristics (nominal specifications):

- Jack type: TOSLINK friction-lock type F-05
- FSI – input sample rates: 44.1 kHz, 48 kHz, or 96 kHz
- Bits per sample: 16-bit or 24-bit
- Signal-to-noise ratio (SNR): > 130 dB
- Total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

For a description of the TOSLINK friction-lock type F-05 jack, refer to [7.5 mm Optical Digital Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvonk7gezdambtgmytcnrx).

The Mac Pro computer includes four audio output ports that can be used to play audio: a mono internal speaker, headphone output on the front panel, line output on the rear panel, and S/PDIF optical digital output on the rear panel.

The internal mono speaker is automatically selected for audio output if no external device is detected at the front panel headphone port. If an external device is plugged into the front panel headphones port, the internal speaker automatically mutes and the audio stream is shifted to the external device. Both left and right stereo audio content is mixed to mono and played through the speaker. The internal speaker supports bit depths of 16, 20, or 24 bits per sample and sample rates of 44.1 kHz, 48 kHz, or 96 kHz.

The headphone output is automatically selected for audio output if an external device is plugged into the front panel headphones port.  The headphone output supports a stereo data stream at bit depths of 16, 20, and 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz.  The headphone output gain can be adjusted between 0.0 dB to -64 dB, below -64 dB the pin is set to mute where the output is essentially the noise floor or < -90 dB.

During playback of a 1 kHz, full-scale (unless otherwise specified) sine wave (44.1 kHz input sample rate, 24-bit sample depth, 300 Ω load, no weighting) the headphones output has the following nominal specifications:

- Jack type: 1/8” stereo-mini
- Maximum output voltage: 1.4 VRMS
- Output impedance: < 24 Ω
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N) at 3 dBFS output: ~1.0V rms: < -75 dB (0.02%)
- Channel separation: > 50 dB

The line output must be selected in Audio MIDI Setup as the audio output device for audio output. The line output supports a stereo data stream at bit depths of 16, 20, and 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. The line output gain can be adjusted between 0.0 dB to -64 dB, below -64 dB the pin is set to Mute where the output is essentially the noise floor or < -90 dB.

During playback of a 1 kHz, full-scale (unless otherwise specified) sine wave (44.1 kHz input sample rate, 24-bit sample depth, 100 kΩ load, no weighting) the line output has the following nominal specifications:

- Jack type: 1/8” stereo-mini
- Maximum output voltage: 1.6 VRMS
- Output impedance: < 24 Ω
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N) at -3dBFS output: ~1.13V rms: < -85 dB (0.006%)
- Channel separation: > 90 dB

The S/PDIF optical digital output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.100 kHz, 48.000 kHz or 96.000 kHz in PCM format. In addition, the S/PDIF optical digital output supports a stereo data stream at 16 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz in AC-3 encoded audio format.

During playback of a 1 kHz, full-scale sine wave (S/PDIF output format, 44.1 kHz output sample rate, 24-bit sample depth, unless otherwise specified) the digital audio output has the following nominal specifications:

- Jack type: TOSLINK friction-lock type F-05
- Digital audio signal-to-noise ratio (SNR): > 130 dB
- Digital audio total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The S/PDIF optical output channel status conforms to IEC 60958-3 consumer mode digital audio.

For a description of the TOSLINK friction-lock type F-05 jack, refer to [7.5 mm Optical Digital Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvonk7gezdambtgmytcnrx).

This section provides audio-specific information for Xserve servers.

The Xserve with Quad-Core Intel Xeon 5400 Series microprocessors, introduced in January 2008, does not support an audio subsystem.

The Xserve announced in August 2006, based on the dual-core Intel Xeon processor, does not support an audio subsystem.

This section provides audio-specific information for iMac computers.

The iMac computers announced in April 2008, incorporating the Intel Core 2 Duo microprocessor, include a built-in audio system providing the developer with a set of hardware resources that can be used to record or play audio.

This section contains the description and specifications of the iMac audio system. Details for the 20-inch iMac and the 24-inch iMac are the same except where specified otherwise.

The iMac includes two audio input ports that can be used for recording: an internal mic and a combination line (analog) input and optical digital input port.

The internal microphone operates independently from all other audio input ports and is always available. The internal microphone supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the microphone is presented as a stereo data stream with the same data appearing on both the left and right channels. The microphone gain can be adjusted from -16 dB to +30 dB.

The analog line input operates independently from all other audio input ports and is always available. The line input supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the line input is presented as a stereo data stream. The line input gain can be adjusted from -16 dB to +30 dB.

During input of a 1 kHz, 1 VRMS (-3 dBFS) sine wave (44.1 kHz input sample rate, 24-bit sample depth, 0.0 dB input gain, no weighting) the audio line input has the following nominal specifications:

- Jack type: 3.5 mm (1/8”) stereo
- Maximum input voltage: 3 VRMS (+11.8 dBu)
- Minimum voltage input for full scale output: 63 mVRMS (-21.5 dBu) at input gain = +30 dB
- Input impedance: > 20 kΩ
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -85 dB (0.006%)
- Channel separation: > 85 dB

The digital audio input has the following electrical characteristics (nominal specifications), based on input of a 1 kHz sine wave at 0 dBFS input level, 24-bit sample depth, and 44.1 kHz sample rate (unless otherwise specified below):

- FSI – input sample rates: 44.1 kHz, 48 kHz, or 96 kHz
- Bits per sample: 16, 20, or 24
- Signal-to-noise ratio (SNR): > 130 dB
- Total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The iMac computers include two audio output ports that can be used to play audio: one internal port for the built-in speakers and one external port supporting both analog headphone output and S/PDIF optical digital output through a 3.5 mm (1/8”) electrical/optical combination (combo) jack. For details, see [3.5 mm (1/8) Combination Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvonc7gezdambtgmytcnrx).

The internal speakers are automatically selected for audio output if no external device is detected at both the line/headphone output port and the S/PDIF optical digital output port. The internal speakers support a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz.

The headphone output is automatically selected for audio output if no external S/PDIF optical digital output device is detected. The headphone output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. The headphone output volume can be adjusted from 0.0 dB to -64 dB.

During playback of a 1 kHz sine wave at -3 dBFS voltage level, 24-bit sample depth, 44.1 kHz output sample rate, 100 kΩ load (unless otherwise specified) the audio output has the following nominal specifications:

- Jack type: 3.5 mm (1/8”) stereo combo
- Maximum output voltage: 2 VRMS (+8.2 dBu)
- Output impedance: <24 Ω
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.007%)
- Channel separation: > 85 dB

The S/PDIF optical digital output is automatically selected when an S/PDIF optical digital output device is detected on the external combo audio port. The S/PDIF optical digital output supports PCM and AC-3 audio formats with the following stereo data stream characteristics:

- PCM: 16, 20, or 24 bits per sample at sample rates of 44.1 kHz, 48 kHz, or 96 kHz
- AC-3: 16 bits per sample at sample rates of 44.1 kHz, 48 kHz, 88.2 kHz, 96 kHz, 176.4 kHz, or 192 kHz

The S/PDIF optical output channel status conforms to IEC 60958-3 consumer mode digital audio.

During playback of a 1 kHz sine wave (S/PDIF output format at 0 dBFS output level, 44.1 kHz sample rate, 24-bit sample depth, unless otherwise specified) the digital audio output has the following nominal specifications:

- Jack type: 3.5 mm (1/8”) stereo combo
- Digital audio signal-to-noise ratio (SNR): > 130 dB
- Digital audio total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The iMac computers announced in August 2007, incorporating the Intel Core 2 Duo microprocessor, include a built-in audio system providing the developer with a set of hardware resources that can be used to record or play audio.

This section contains the description and specifications of the iMac audio system. Details for the 20-inch iMac and the 24-inch iMac are the same except where specified otherwise.

The iMac includes two audio input ports that can be used for recording: an internal mic and a combination line (analog) input and optical digital input port.

The internal microphone operates independently from all other audio input ports and is always available. The internal microphone supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the microphone is presented as a stereo data stream with the same data appearing on both the left and right channels. The microphone gain can be adjusted from -16 dB to +30 dB.

The analog line input operates independently from all other audio input ports and is always available. The line input supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the line input is presented as a stereo data stream. The line input gain can be adjusted from -16 dB to +30 dB.

During input of a 1 kHz, 1 VRMS (-3 dBFS) sine wave (44.1 kHz input sample rate, 24-bit sample depth, 0.0 dB input gain, no weighting) the audio line input has the following nominal specifications:

- Jack type: 3.5 mm (1/8”) stereo
- Maximum input voltage: 3 VRMS (+11.8 dBu)
- Minimum voltage input for full scale output: 63 mVRMS (-21.5 dBu) at input gain = +30 dB
- Input impedance: > 20 kΩ
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -85 dB (0.006%)
- Channel separation: > 85 dB

The digital audio input has the following electrical characteristics (nominal specifications), based on input of a 1 kHz sine wave at 0 dBFS input level, 24-bit sample depth, and 44.1 kHz sample rate (unless otherwise specified below):

- FSI – input sample rates: 44.1 kHz, 48 kHz, or 96 kHz
- Bits per sample: 16, 20, or 24
- Signal-to-noise ratio (SNR): > 130 dB
- Total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The iMac computers include two audio output ports that can be used to play audio: one internal port for the built-in speakers and one external port supporting both analog headphone output and S/PDIF optical digital output through a 3.5 mm (1/8”) electrical/optical combination (combo) jack. For details, see [3.5 mm (1/8) Combination Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvonc7gezdambtgmytcnrx).

The internal speakers are automatically selected for audio output if no external device is detected at both the line/headphone output port and the S/PDIF optical digital output port. The internal speakers support a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz.

The headphone output is automatically selected for audio output if no external S/PDIF optical digital output device is detected. The headphone output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. The headphone output volume can be adjusted from 0.0 dB to -64 dB.

During playback of a 1 kHz sine wave at -3 dBFS voltage level, 24-bit sample depth, 44.1 kHz output sample rate, 100 kΩ load (unless otherwise specified) the audio output has the following nominal specifications:

- Jack type: 3.5 mm (1/8”) stereo combo
- Maximum output voltage: 1.6 VRMS (+6.3 dBu)
- Output impedance: < 24 Ω
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: > 85 dB

The S/PDIF optical digital output is automatically selected when an S/PDIF optical digital output device is detected on the external combo audio port. The S/PDIF optical digital output supports PCM and AC-3 audio formats with the following stereo data stream characteristics:

- PCM: 16, 20, or 24 bits per sample at sample rates of 44.1 kHz, 48 kHz, or 96 kHz
- AC-3: 16 bits per sample at sample rates of 44.1 kHz, 48 kHz, 88.2 kHz, 96 kHz, 176.4 kHz, or 192 kHz

The S/PDIF optical output channel status conforms to IEC 60958-3 consumer mode digital audio.

During playback of a 1 kHz sine wave (S/PDIF output format at 0 dBFS output level, 44.1 kHz sample rate, 24-bit sample depth, unless otherwise specified) the digital audio output has the following nominal specifications:

- Jack type: 3.5 mm (1/8”) stereo combo
- Digital audio signal-to-noise ratio (SNR): > 130 dB
- Digital audio total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The iMac with SuperDrive computers announced in September 2006, incorporating the Intel Core 2 Duo microprocessor, include a built-in audio system providing the developer with a set of hardware resources that can be used to record or play audio.

For information on the 17-inch and 20-inch iMac audio system, refer to [17-inch and 20-inch iMac Audio System](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzyfvjvom27gezdambtgmytcnrx). For information on the 24-inch iMac audio system, refer to [24-inch iMac Audio System](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzyfvjvonc7gezdambtgmytcnrx)

This section contains the description and specifications of the 17-inch and 20-inch iMac audio system.

The 17-inch and 20-inch iMac includes two audio input ports that can be used for recording: an internal mic and a combination line input and optical digital input port.

The internal microphone operates independently from all other audio input ports and is always available. The internal microphone supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the microphone is presented as a stereo data stream with the same data appearing on both the left and right channels. The microphone gain can be adjusted from 0.0 dB to +22.5 dB.

The line input operates independently from all other audio input ports and is always available. The line input supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the line input is presented as a stereo data stream. The line input gain can be adjusted from 0.0 dB to +22.5 dB.

During input of a 1 kHz, full-scale 1 VRMS sine wave (44.1 kHz input sample rate, 24-bit sample depth, 0.0 dB input gain, no weighting) the audio line input has the following nominal specifications:

- Jack type: 3.5 mm (1/8”) stereo
- Maximum input voltage: 1 VRMS (+2.22 dBu)
- Minimum voltage input for full scale output: 75 mVRMS (-20.28 dBu) at input gain = +22.5 dB
- Input impedance: > 20 kΩ
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: > 80 dB

Based on playback of a 1 kHz, -1 dBFS 24-bit sine wave playback, 24-bit 44.1 kHz output sample rate (unless otherwise specified below) the digital audio input and output have the following electrical characteristics (nominal specifications):

- FSI – input sample rates: 44.1 kHz, 48 kHz, or 96 kHz
- Bits per sample: 16-bit or 24-bit
- Signal-to-noise ratio (SNR): > 130 dB
- Total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The 17-inch and 20-inch iMac computer includes two audio output ports that can be used to play audio: internal speakers and a combined headphone output and S/PDIF optical digital output port.

The internal speakers are automatically selected for audio output if no external device is detected at both the line/headphone output port and the S/PDIF optical digital output port. The internal speakers support a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz.

The headphone output is automatically selected for audio output if no external S/PDIF optical digital output device is detected. The headphone output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. The headphone output volume can be adjusted from 0.0 dB to -95.25 dB.

During playback of a 1 kHz, full-scale sine wave (44.1 kHz output sample rate, 24-bit sample depth, 100 kΩ load, unless otherwise specified) the audio output has the following nominal specifications:

- Jack type: 3.5 mm (1/8”) stereo
- Maximum output voltage: 1 VRMS (+2.22 dBu)
- Output impedance: < 24 Ω
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: > 75 dB

The S/PDIF optical digital output is automatically selected when a S/PDIF optical digital output external device is detected. The S/PDIF optical digital output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz or 96 kHz in PCM format. In addition, the S/PDIF optical digital output supports a stereo data stream at 16 bits per sample and at sample rates of 44.1 kHz, 48 kHz, 88.2 kHz, 96 kHz, 176.4 kHz, or 192 kHz in AC-3 encoded audio format.

During playback of a 1 kHz, full-scale sine wave (S/PDIF output format, 44.1 kHz output sample rate, 24-bit sample depth, unless otherwise specified) the digital audio output has the following nominal specifications:

- Jack type: 3.5 mm (1/8”) optical
- Digital audio signal-to-noise ratio (SNR): > 130 dB
- Digital audio total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The S/PDIF optical output channel status conforms to IEC 60958-3 consumer mode digital audio.

The audio output connector on the 17-inch and 20-inch iMac is a 3.5 mm (1/8”) electrical/optical combination (combo) jack. For details, see [3.5 mm (1/8) Combination Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvonc7gezdambtgmytcnrx).

This section contains the description and specifications of the 24-inch iMac audio system.

The 24-inch iMac includes two audio input ports that can be used for recording: an internal mic and a combination line input and optical digital input port.

The internal microphone operates independently from all other audio input ports and is always available. The internal microphone supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the microphone is presented as a stereo data stream with the same data appearing on both the left and right channels. The microphone gain can be adjusted from -16 dB to +30 dB.

The analog line input operates independently from all other audio input ports and is always available. The analog line input supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the line input is presented as a stereo data stream. The line input gain can be adjusted from -16 dB to +30 dB.

During input of a 1 kHz, -3 dBFS 24-bit sine wave at 44.1 kHz sample rate, the audio line input has the following nominal specifications:

- Jack type: 3.5 mm (1/8”) stereo combo
- Maximum input voltage: 2 VRMS (+8.24 dBu)
- Minimum voltage input for full scale output: 63 mVRMS (-21.8 dBu) at input gain = +30 dB
- Input impedance: > 20 kΩ
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): <-50 dB (0.006%)
- Channel separation: > 90 dB

Based on playback of a 1 kHz, 0 dBFS 24-bit sine wave sample rate (unless otherwise specified below) the digital audio input and output have the following electrical characteristics (nominal specifications):

- FSI – input sample rates: 44.1 kHz, 48 kHz, or 96 kHz
- Bits per sample: 16-bit, 20-bit, or 24-bit
- Signal-to-noise ratio (SNR): > 130 dB
- Total harmonic distortion + noise (THD+N): <-130 dB (0.00003%)

The 24-inch iMac computer includes two audio output ports that can be used to play audio: internal speakers and a combined headphone output and S/PDIF optical digital output port.

The internal speakers are automatically selected for audio output if no external device is detected at both the line/headphone output port and the S/PDIF optical digital output port. The internal speakers support a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz.

The headphone output is automatically selected for audio output if no external S/PDIF optical digital output device is detected. The headphone output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. The headphone output volume can be adjusted from 0.0 dB to -64 dB.

During playback of a 1 kHz, -3 dBFS 24-bit sine wave at 44.1 kHz sample rate, 100 kΩ load, unless otherwise specified) the audio output has the following nominal specifications:

- Jack type: 3.5 mm (1/8”) stereo combo
- Maximum output voltage: 1.6 VRMS (+6.3 dBu)
- Output impedance: < 24 Ω
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): >95 dB
- Total harmonic distortion + noise (THD+N): < -85 dB (0.006%)
- Channel separation: >95 dB

The S/PDIF optical digital output is automatically selected when a S/PDIF optical digital output external device is connected to the 3.5 mm (1/8”) stereo combinational output jack. The S/PDIF optical digital output also supports AC-3 encoded data.

During playback of a 1 kHz, 0 dBFS 24-bit sine wave (S/PDIF output format, 44.1 kHz output sample rate, 24-bit sample rate, unless otherwise specified) the digital audio output has the following nominal specifications:

- Jack type: 3.5 mm (1/8”) stereo combo
- Bits per sample: 16-bit, 20-bit, or 24-bit
- Output sample rates: 44.1 kHz, 48 kHz, or 96 kHz
- Digital audio signal-to-noise ratio (SNR): > 130 dB
- Digital audio total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The S/PDIF optical output channel status conforms to IEC 60958-3 consumer mode digital audio.

The audio output connector on the 24-inch iMac is a 3.5 mm (1/8”) electrical/optical combination (combo) jack. For details, see [3.5 mm (1/8) Combination Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvonc7gezdambtgmytcnrx).

The iMac with Combo drive computer announced in September 2006, incorporating the Intel Core 2 Duo microprocessor, includes a built-in audio system providing the developer with a set of hardware resources that can be used to record or play audio.

The iMac includes two audio input ports that can be used for recording: an internal mic and a combination line input and optical digital input port.

The internal microphone operates independently from all other audio input ports and is always available. The internal microphone supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the microphone is presented as a stereo data stream with the same data appearing on both the left and right channels. The microphone gain can be adjusted from 0.0 dB to +22.5 dB.

The line input operates independently from all other audio input ports and is always available. The line input supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the line input is presented as a stereo data stream. The line input gain can be adjusted from 0.0 dB to +22.5 dB.

During input of a 1 kHz, full-scale 1 VRMS sine wave (44.1 kHz input sample rate, 24-bit sample depth, 0.0 dB input gain, no weighting) the audio line input has the following nominal specifications:

- Jack type: 3.5 mm stereo
- Maximum input voltage: 1 VRMS (+2.22 dBu)
- Minimum voltage input for full scale output: 75 mVRMS (-20.28 dBu) at input gain = +22.5 dB
- Input impedance: > 20 kΩ
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: > 80 dB

Based on playback of a 1 kHz, -1 dBFS 24-bit sine wave playback, 24-bit 44.1 kHz output sample rate (unless otherwise specified below) the digital audio input and output have the following electrical characteristics (nominal specifications):

- FSI – input sample rates: 44.1 kHz, 48 kHz, or 96 kHz
- Bits per sample: 16-bit or 24-bit
- Signal-to-noise ratio (SNR): > 130 dB
- Total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The iMac computer includes two audio output ports that can be used to play audio: internal speakers and a combined headphone output and S/PDIF optical digital output port.

The internal speakers are automatically selected for audio output if no external device is detected at both the line/headphone output port and the S/PDIF optical digital output port. The internal speakers support a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz.

The headphone output is automatically selected for audio output if no external S/PDIF optical digital output device is detected. The headphone output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. The headphone output volume can be adjusted from 0.0 dB to -95.25 dB.

During playback of a 1 kHz, full-scale sine wave (44.1 kHz output sample rate, 24-bit sample depth, 100 kΩ load, unless otherwise specified) the audio output has the following nominal specifications:

- Jack type: 3.5 mm stereo
- Maximum output voltage: 1 VRMS (+2.22 dBu)
- Output impedance: < 24 Ω
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: > 75 dB

The S/PDIF optical digital output is automatically selected when a S/PDIF optical digital output external device is detected. The S/PDIF optical digital output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz or 96 kHz in PCM format. In addition, the S/PDIF optical digital output supports a stereo data stream at 16 bits per sample and at sample rates of 44.1 kHz, 48 kHz, 88.2 kHz, 96 kHz, 176.4 kHz, or 192 kHz in AC-3 encoded audio format.

During playback of a 1 kHz, full-scale sine wave (S/PDIF output format, 44.1 kHz output sample rate, 24-bit sample depth, unless otherwise specified) the digital audio output has the following nominal specifications:

- Jack type: 3.5 mm optical
- Digital audio signal-to-noise ratio (SNR): > 130 dB
- Digital audio total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The S/PDIF optical output channel status conforms to IEC 60958-3 consumer mode digital audio.

The audio output connector on the iMac is a 3.5 mm electrical/optical combination (combo) jack. For details, see [3.5 mm (1/8) Combination Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvonc7gezdambtgmytcnrx).

The 17-inch iMac for education computer announced in July 2006, incorporating the Intel Core Duo microprocessor, includes a built-in audio system providing the developer with a set of hardware resources that can be used to record or play audio.

The 17-inch iMac for education includes two audio input ports that can be used for recording: an internal mic and a combination line input and optical digital input port.

The internal microphone operates independently from all other audio input ports and is always available. The internal microphone supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the microphone is presented as a stereo data stream with the same data appearing on both the left and right channels. The microphone gain can be adjusted from 0.0 dB to +22.5 dB.

The line input operates independently from all other audio input ports and is always available. The line input supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the line input is presented as a stereo data stream. The line input gain can be adjusted from 0.0 dB to +22.5 dB.

During input of a 1 kHz, full-scale 1 VRMS sine wave (44.1 kHz input sample rate, 24-bit sample depth, 0.0 dB input gain, no weighting) the audio line input has the following nominal specifications:

- Jack type: 3.5 mm stereo
- Maximum input voltage: 1 VRMS (+2.22 dBu)
- Minimum voltage input for full scale output: 75 mVRMS (-20.28 dBu) at input gain = +22.5 dB
- Input impedance: > 20 kΩ
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: > 80 dB

Based on playback of a 1 kHz, -1 dBFS 24-bit sine wave playback, 24-bit 44.1 kHz output sample rate (unless otherwise specified below) the digital audio input and output have the following electrical characteristics (nominal specifications):

- FSI – input sample rates: 44.1 kHz, 48 kHz, or 96 kHz
- Bits per sample: 16-bit or 24-bit
- Signal-to-noise ratio (SNR): > 130 dB
- Total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The 17-inch iMac for education computer includes two audio output ports that can be used to play audio: internal speakers and a combined headphone output and S/PDIF optical digital output port.

The internal speakers are automatically selected for audio output if no external device is detected at both the line/headphone output port and the S/PDIF optical digital output port. The internal speakers support a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz.

The headphone output is automatically selected for audio output if no external S/PDIF optical digital output device is detected. The headphone output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. The headphone output volume can be adjusted from 0.0 dB to -95.25 dB.

During playback of a 1 kHz, full-scale sine wave (44.1 kHz output sample rate, 24-bit sample depth, 100 kΩ load, unless otherwise specified) the audio output has the following nominal specifications:

- Jack type: 3.5 mm stereo
- Maximum output voltage: 1 VRMS (+2.22 dBu)
- Output impedance: < 24 Ω
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: > 75 dB

The S/PDIF optical digital output is automatically selected when a S/PDIF optical digital output external device is detected. The S/PDIF optical digital output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz or 96 kHz in PCM format. In addition, the S/PDIF optical digital output supports a stereo data stream at 16 bits per sample and at sample rates of 44.1 kHz, 48 kHz, 88.2 kHz, 96 kHz, 176.4 kHz, or 192 kHz in AC-3 encoded audio format.

During playback of a 1 kHz, full-scale sine wave (S/PDIF output format, 44.1 kHz output sample rate, 24-bit sample depth, unless otherwise specified) the digital audio output has the following nominal specifications:

- Jack type: 3.5 mm optical
- Digital audio signal-to-noise ratio (SNR): > 130 dB
- Digital audio total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The S/PDIF optical output channel status conforms to IEC 60958-3 consumer mode digital audio.

The audio output connector on the 17-inch iMac for education is a 3.5 mm electrical/optical combination jack. For details, see [3.5 mm (1/8) Combination Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvonc7gezdambtgmytcnrx).

The iMac computers announced in January 2006, incorporating the Intel Core Duo microprocessor, include a built-in audio system providing the developer with a set of hardware resources that can be used to record or play audio.

The iMac computer includes two audio input ports that can be used for recording.

The internal microphone operates independently from all other audio input ports and is always available. The internal microphone supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the microphone is presented as a stereo data stream with the same data appearing on both the left and right channels. The microphone gain can be adjusted from 0.0 dB to +22.5 dB.

The line input operates independently from all other audio input ports and is always available. The line input supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the line input is presented as a stereo data stream. The line input gain can be adjusted from 0.0 dB to +22.5 dB.

During input of a 1 kHz, full-scale 1 VRMS sine wave (44.1 kHz input sample rate, 24-bit sample depth, 0.0 dB input gain, no weighting) the audio line input has the following nominal specifications:

- Jack type: 3.5 mm stereo
- Maximum input voltage: 1 VRMS (+2.22 dBu)
- Minimum voltage input for full scale output: 75 mVRMS (-20.28 dBu) at input gain = +22.5 dB
- Input impedance: > 20 kΩ
- Frequency response: 20Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: > 80 dB

The iMac computer includes three audio output ports that can be used to play audio.

The internal speakers are automatically selected for audio output if no external device is detected at either the line/headphone output port or the S/PDIF optical digital output port. The internal speakers support a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz.

The line/headphone output is automatically selected for audio output if no external device is detected at the S/PDIF optical digital output port. The line/headphone output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. The line/headphone output volume can be adjusted from 0.0 dB to -95.25 dB.

During playback of a 1 kHz, full-scale sine wave (44.1 kHz output sample rate, 24-bit sample depth, 100 kΩ load, unless otherwise specified) the audio line output has the following nominal specifications:

- Jack type: 3.5 mm stereo
- Maximum output voltage: 1 VRMS (+2.22 dBu)
- Output impedance: < 24 Ω
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: > 75 dB

The S/PDIF optical digital output is automatically selected when a S/PDIF optical digital output external device is detected. The S/PDIF optical digital output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz or 96 kHz in PCM format. In addition, the S/PDIF optical digital output supports a stereo data stream at 16 bits per sample and at sample rates of 44.1 kHz, 48 kHz, 88.2 kHz, 96 kHz, 176.4 kHz, or 192 kHz in AC-3 encoded audio format.

During playback of a 1 kHz, full-scale sine wave (S/PDIF output format, 44.1 kHz output sample rate, 24-bit sample depth, unless otherwise specified) the digital audio output has the following nominal specifications:

- Jack type: 3.5 mm optical
- Digital audio signal-to-noise ratio (SNR): > 130 dB
- Digital audio total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The S/PDIF optical output channel status conforms to IEC 60958-3 consumer mode digital audio.

The audio output connector on the iMac is a 3.5 mm electrical/optical combination (combo) jack. For details, see [3.5 mm (1/8) Combination Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvonc7gezdambtgmytcnrx).

The iMac G5 audio system supports analog recording and both digital and analog playback.

The iMac G5 audio system features a combination output jack that supports both analog headphones output and optical digital output connectivity. Since a single connector is provided to support both headphone output and optical digital output connectivity, support of the headphones output and optical digital output is mutually exclusive. Audio output port selection is automatic. When no device is inserted into the output jack, the internal speakers are selected. When an optical cable is connected to the output jack, optical digital output is selected. When an analog device is connected to the output jack, the headphones output is selected. It is not possible to simultaneous select or use more than one output at a time. Encoded audio, such as AC-3, can be streamed only to the optical digital audio output. A mute control for the current active output port can be accessed in the Output section of the Sound pane in the System Preferences.

Digital playback features Sony/Philips Digital Interface (S/PDIF) when an optical cable is connected to the audio output jack. The optical digital output supports both PCM and AC-3 formats. Optical digital output encoding conforms to IEC 60958-3. The IEC 60958-3 category code encoding for non-encoded (i.e. PCM) audio formats indicates an optical laser CD device. The IEC 60958-3 category code encoding for encoded ((i.e. AC-3) audio formats indicates an optical laser DVD device.

Under control of the system software, the audio circuitry digitally creates and records sounds. The iMac G5 can receive input from only one of two analog input sources: a built-in microphone and/or line input. Hardware input gain control is supported over a range of –4dB to +20dB. The input gain control can be accessed using the Audio MIDI Setup application included in the `Applications/Utilities` folder.

The audio circuitry and audio device drivers support audio data in multiple formats. Both digital and analog outputs support PCM audio at 16 and 24 bits with sample rates of 32.000 kHz, 44.1 kHz, 48 kHz, 64 kHz, 88.2 kHz, and 96 kHz. In addition, the optical digital output also supports AC-3 audio at 16 bits with sample rates of 32 kHz, 44.1 kHz, 48 kHz, 64 kHz, 88.2 kHz, and 96 kHz.

If audio data recorded on another computer at a sample rate not supported by the iMac G5 hardware is played on the iMac G5, Core Audio software (the Mac OS X audio API) transparently converts the data to the sample rate currently selected on the iMac G5. To maximize audio fidelity, the Core Audio samples are stored as 32-bit floating point values.

For more information about audio APIs in Mac OS X, visit the Apple audio technologies developer web page at

[http://developer.apple.com/audio/](https://developer.apple.com/audio/)

Digital audio data is transmitted from the iMac G5 using an optical cable, commonly referred to as a TOSLINK cable. The digital audio output format conforms to IEC 60874-17.

The audio output connector on the iMac G5 is a 3.5 mm electrical/optical combination (combo) jack. (For details, see [3.5 mm (1/8) Combination Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvonc7gezdambtgmytcnrx).)

For details on the S/PDIF digital output format and performance specifications, refer to the next section.

During playback of a 1 kHz, full-scale sine wave (S/PDIF output format, 44.1 kHz output sample rate, 24-bit sample depth, unless otherwise specified) the digital audio output has the following nominal specifications:

- Jack type: 3.5 mm analog/optical combo jack
- Output data formats: S/PDIF (IEC 60958-3), AC-3
- Output sample rates: 32 kHz, 44.1 kHz, 48 kHz, 64 kHz, 88.2 kHz, 96 kHz
- Bits per sample: 16 or 24 (S/PDIF),16 (AC-3)
- Frequency response: 20 Hz to 20 kHz, +/-0 dB
- Signal-to-noise ratio (SNR): > 130 dB
- Total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)
- Channel separation: > 130 dB

The iMac G5 has an electrical stereo audio line input jack on the back panel. See [3.5 mm (1/8) Stereo Electrical Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvoms7gezdambtgmytcnrx) for details.

The audio input is designed to accept audio signals with input levels ranging from 150 mVRMS (-14.3 dBu) to 3 VRMS (+11.8 dBu). The input gain should be set according to the input level so the input to the A/D converter in the codec is not clipped. Input gain control is supported over a range of –4 dB to +20 dB. The input gain control can be accessed using the Audio Midi Setup application included in the `Applications/Utilities` folder. The default input gain setting is 0dB, which will accommodate an input level of 2 VRMS (+8.2 dBu), which is the typical output level from CD players, DVD players and other consumer audio equipment. With an input gain setting of 20 dB, the minimum recommended input level is 150 mVRMS (-14.3 dBu), which will correspond to 3 dB below full-scale on the A/D converter in the codec.

During input of a 1 kHz, full-scale sine wave (44.1 kHz input sample rate, 24-bit sample depth, unless otherwise specified) the audio line input has the following nominal specifications:

- Jack type: 3.5 mm analog jack
- Input sample rates: 32 kHz, 44.1 kHz, 48 kHz, 64 kHz, 88.2 kHz, 96 kHz
- Bits per sample: 16 or 24
- Input impedance: > 20 kΩ
- Input gain range: -4 dB to +20 dB
- Typical input level (input gain = 0 dB): 2 VRMS (+8.2 dBu)
- Maximum input level (input gain = -4 dB): 3 VRMS (+11.8 dBu)
- Minimum input level to achieve full scale on A/D (input gain = 20 dB): 200 mVRMS (-11.8 dBu)
- Minimum recommended input level (input gain = 20dB): 150 mVRMS (-14.3 dBu)
- Frequency response: 20 Hz to 20 kHz, +/-0.5 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -85 dB (0.006%)
- Channel separation: > 85 dB

The iMac G5 has a stereo audio output jack on the back of the enclosure that is suitable for connecting amplified external speakers, audio equipment, or headphones.

The 
audio output connector on the iMac G5 is a 3.5 mm electrical/optical combination (combo) jack. For details, see [3.5 mm (1/8) Combination Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvonc7gezdambtgmytcnrx).

During playback of a 1 kHz, full-scale sine wave (44.1 kHz output sample rate, 24-bit sample depth, 100 kΩ load, unless otherwise specified) the audio line output has the following nominal specifications:

- Jack type: 3.5 mm analog/optical combo jack
- Output sample rates: 32 kHz, 44.1 kHz, 48 kHz, 64 kHz, 88.2 kHz, 96 kHz
- Bits per sample: 16 or 24
- Output impedance: < 50 Ω
- Output level: 1.75 VRMS (+7.1 dBu)
- Frequency response: 20 Hz to 20 kHz, +/-0.5 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -85 dB (0.006%)
- Channel separation: > 85 dB
- Output power (into 16 Ω headphones): 60 mW

This section provides audio-specific information for MacBook computers. Refer to the specific MacBook developer note for additional information.

The MacBook computer introduced in February 2008, incorporating the Intel Core 2 Duo processor on 45 nm process technology, includes a built-in audio system providing the developer with a set of hardware resources that can be used to record or play audio.

The MacBook computer includes two audio input ports that can be used for recording: an internal mic and a combination line input and optical digital input port.

The internal microphone operates independently from all other audio input ports and is always available. The internal microphone supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the microphone is presented as a stereo data stream with the same data appearing on both the left and right channels. The microphone gain can be adjusted from -16.0 dB to +30.0 dB.

The line input operates independently from all other audio input ports and is always available. The line input supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the line input is presented as a stereo data stream. The line input gain can be adjusted from -16.0 dB to +30.0 dB.

During input of a 1 kHz, full-scale 1VRMS sine wave (44.1 kHz input sample rate, 24-bit sample depth, 0.0 dB input gain, no weighting) the audio line input has the following nominal specifications:

- Jack Type: 3.5 mm stereo
- Maximum Input Voltage: 1.2 VRMS (+3.8 dBu)
- Minimum Voltage Input for Full Scale Output: 38 mVRMS (-26.2 dBu) at Input Gain = +30.0 dB
- Input Impedance: > 20 kΩ
- Frequency Response: 20 Hz – 20 kHz, +0.5 dB/-3 dB
- Signal-to-Noise Ratio (SNR): > 90 dB
- Total Harmonic Distortion + Noise (THD+N): < -80 dB (0.01%)
- Channel Separation: > 80 dB

Based on playback of a 1 kHz, -1 dBFS 24-bit sine wave playback, 24-bit 44.1 kHz output sample rate (unless otherwise specified below) the digital audio input and output have the following electrical characteristics (nominal specifications):

- Fsi – input sample rates: 44.1 kHz, 48 kHz, or 96 kHz
- bits per sample: 16-bit or 24-bit
- SNR: > 130 dB
- THD+N: < -130 dB (0.00003%)

The MacBook computer includes three audio output ports that can be used to play audio: internal speakers, combination line and headphone output, and S/PDIF optical digital output.

The internal speakers are automatically selected for audio output if no external device is detected at both the line/headphone output port and the S/PDIF optical digital output port. The internal speakers support a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz.

The line/headphone output is automatically selected for audio output if no external device is detected at the S/PDIF optical digital output port. The line/headphone output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. The line/headphone output volume can be adjusted from 0.0 dB to -64.0 dB.

During playback of a 1 kHz, full-scale sine wave (44.1 kHz output sample rate, 24-bit sample depth, 100 kΩ load, unless otherwise specified) the audio line output has the following nominal specifications:

- Jack Type: 3.5 mm Stereo
- Maximum Output Voltage: 1.2 VRMS (+3.8 dBu)
- Output Impedance: < 24 Ω
- Frequency Response: 20 Hz – 20 kHz, +0.5 dB/-3 dB
- Signal-to-Noise Ratio (SNR): > 90 dB
- Total Harmonic Distortion + Noise (THD+N): < -80 dB (0.01%)
- Channel Separation: > 80 dB

The S/PDIF optical digital output is automatically selected when a S/PDIF optical digital output external device is detected. The S/PDIF optical digital output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz or 96 kHz in PCM format. In addition, the S/PDIF optical digital output supports a stereo data stream at 16 bits per sample and at sample rates of 44.1 kHz, 48 kHz, 88.2 kHz, 96 kHz, 176.4 kHz, or 192 kHz in AC3 Encoded Audio format.

During playback of a 1KHz, full-scale sine wave (S/PDIF output format, 44.1 kHz output sample rate, 24-bit sample depth, unless otherwise specified) the digital audio output has the following nominal specifications:

- Jack Type: 3.5 mm Optical
- Digital Audio Signal-to-Noise Ratio (SNR): > 130 dB
- Digital Audio Total Harmonic Distortion + Noise (THD+N): < -130 dB (0.00003%)

The S/PDIF Optical Output channel status conforms to IEC60958-3 consumer mode digital audio.

The audio output connector on the MacBook is a 3.5 mm electrical/optical combination ("combo") jack. See [3.5 mm (1/8) Combination Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvonc7gezdambtgmytcnrx) for details.

The MacBook computer introduced in November 2007, incorporating the Intel Core 2 Duo, includes a built-in audio system providing the developer with a set of hardware resources that can be used to record or play audio.

The MacBook computer includes two audio input ports that can be used for recording: an internal mic and a combination line input and optical digital input port.

The internal microphone operates independently from all other audio input ports and is always available. The internal microphone supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the microphone is presented as a stereo data stream with the same data appearing on both the left and right channels. The microphone gain can be adjusted from -16.0 dB to +30.0 dB.

The line input operates independently from all other audio input ports and is always available. The line input supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the line input is presented as a stereo data stream. The line input gain can be adjusted from -16.0 dB to +30.0 dB.

During input of a 1 kHz, full-scale 1VRMS sine wave (44.1 kHz input sample rate, 24-bit sample depth, 0.0 dB input gain, no weighting) the audio line input has the following nominal specifications:

- Jack Type: 3.5 mm stereo
- Maximum Input Voltage: 1.2 VRMS (+3.8 dBu)
- Minimum Voltage Input for Full Scale Output: 38 mVRMS (-26.2 dBu) at Input Gain = +30.0 dB
- Input Impedance: > 20 kΩ
- Frequency Response: 20 Hz – 20 kHz, +0.5 dB/-3 dB
- Signal-to-Noise Ratio (SNR): > 90 dB
- Total Harmonic Distortion + Noise (THD+N): < -80 dB (0.01%)
- Channel Separation: > 80 dB

Based on playback of a 1 kHz, -1 dBFS 24-bit sine wave playback, 24-bit 44.1 kHz output sample rate (unless otherwise specified below) the digital audio input and output have the following electrical characteristics (nominal specifications):

- Fsi – input sample rates: 44.1 kHz, 48 kHz, or 96 kHz
- bits per sample: 16-bit or 24-bit
- SNR: > 130 dB
- THD+N: < -130 dB (0.00003%)

The MacBook computer includes three audio output ports that can be used to play audio: internal speakers, combination line and headphone output, and S/PDIF optical digital output.

The internal speakers are automatically selected for audio output if no external device is detected at both the line/headphone output port and the S/PDIF optical digital output port. The internal speakers support a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz.

The line/headphone output is automatically selected for audio output if no external device is detected at the S/PDIF optical digital output port. The line/headphone output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. The line/headphone output volume can be adjusted from 0.0 dB to -64.0 dB.

During playback of a 1 kHz, full-scale sine wave (44.1 kHz output sample rate, 24-bit sample depth, 100 kΩ load, unless otherwise specified) the audio line output has the following nominal specifications:

- Jack Type: 3.5 mm Stereo
- Maximum Output Voltage: 1.2 VRMS (+3.8 dBu)
- Output Impedance: < 24 Ω
- Frequency Response: 20 Hz – 20 kHz, +0.5 dB/-3 dB
- Signal-to-Noise Ratio (SNR): > 90 dB
- Total Harmonic Distortion + Noise (THD+N): < -80 dB (0.01%)
- Channel Separation: >80 dB

The S/PDIF optical digital output is automatically selected when a S/PDIF optical digital output external device is detected. The S/PDIF optical digital output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz or 96 kHz in PCM format. In addition, the S/PDIF optical digital output supports a stereo data stream at 16 bits per sample and at sample rates of 44.1 kHz, 48 kHz, 88.2 kHz, 96 kHz, 176.4 kHz, or 192 kHz in AC3 Encoded Audio format.

During playback of a 1KHz, full-scale sine wave (S/PDIF output format, 44.1 kHz output sample rate, 24-bit sample depth, unless otherwise specified) the digital audio output has the following nominal specifications:

- Jack Type: 3.5 mm Optical
- Digital Audio Signal-to-Noise Ratio (SNR): > 130 dB
- Digital Audio Total Harmonic Distortion + Noise (THD+N): < -130 dB (0.00003%)

The S/PDIF Optical Output channel status conforms to IEC60958-3 consumer mode digital audio.

The audio output connector on the MacBook is a 3.5 mm electrical/optical combination ("combo") jack. See [3.5 mm (1/8) Combination Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvonc7gezdambtgmytcnrx) for details.

The MacBook computer introduced in May 2007, incorporating the Intel Core 2 Duo, includes a built-in audio system providing the developer with a set of hardware resources that can be used to record or play audio.

The MacBook computer includes two audio input ports that can be used for recording: an internal mic and a combination line input and optical digital input port.

The internal microphone operates independently from all other audio input ports and is always available. The internal microphone supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the microphone is presented as a stereo data stream with the same data appearing on both the left and right channels. The microphone gain can be adjusted from 0.0 dB to +22.5 dB.

The line input operates independently from all other audio input ports and is always available. The line input supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the line input is presented as a stereo data stream. The line input gain can be adjusted from 0.0 dB to +22.5 dB.

During input of a 1 kHz, full-scale 1VRMS sine wave (44.1 kHz input sample rate, 24-bit sample depth, 0.0 dB input gain, no weighting) the audio line input has the following nominal specifications:

- Jack Type: 3.5 mm stereo
- Maximum Input Voltage: 1VRMS (+2.22 dBu)
- Minimum Voltage Input for Full Scale Output: 75 mV VRMS (-20.28 dBu) at Input Gain = +22.5 dB
- Input Impedance: > 20 kΩ
- Frequency Response: 20 Hz – 20 kHz, +0.5 dB/-3 dB
- Signal-to-Noise Ratio (SNR): > 90 dB
- Total Harmonic Distortion + Noise (THD+N): < -80 dB (0.01%)
- Channel Separation: > 80 dB

Based on playback of a 1 kHz, -1 dBFS 24-bit sine wave playback, 24-bit 44.1 kHz output sample rate (unless otherwise specified below) the digital audio input and output have the following electrical characteristics (nominal specifications):

- Fsi – input sample rates: 44.1 kHz, 48 kHz, or 96 kHz
- bits per sample: 16-bit or 24-bit
- SNR: > 130 dB
- THD+N: < -130 dB (0.00003%)

The MacBook computer includes three audio output ports that can be used to play audio: internal speakers, combination line and headphone output, and S/PDIF optical digital output.

The internal speakers are automatically selected for audio output if no external device is detected at both the line/headphone output port and the S/PDIF optical digital output port. The internal speakers support a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz.

The line/headphone output is automatically selected for audio output if no external device is detected at the S/PDIF optical digital output port. The line/headphone output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. The line/headphone output volume can be adjusted from 0.0 dB to -95.25 dB.

During playback of a 1 kHz, full-scale sine wave (44.1 kHz output sample rate, 24-bit sample depth, 100 kΩ load, unless otherwise specified) the audio line output has the following nominal specifications:

- Jack Type: 3.5 mm Stereo
- Maximum Output Voltage: 1VRMS (+2.22 dBu)
- Output Impedance: < 24 Ω
- Frequency Response: 20 Hz – 20 kHz, +0.5 dB/-3 dB
- Signal-to-Noise Ratio (SNR): > 90 dB
- Total Harmonic Distortion + Noise (THD+N): < -80 dB (0.01%)
- Channel Separation: > 75 dB

The S/PDIF optical digital output is automatically selected when a S/PDIF optical digital output external device is detected. The S/PDIF optical digital output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz or 96 kHz in PCM format. In addition, the S/PDIF optical digital output supports a stereo data stream at 16 bits per sample and at sample rates of 44.1 kHz, 48 kHz, 88.2 kHz, 96 kHz, 176.4 kHz, or 192 kHz in AC3 Encoded Audio format.

During playback of a 1KHz, full-scale sine wave (S/PDIF output format, 44.1 kHz output sample rate, 24-bit sample depth, unless otherwise specified) the digital audio output has the following nominal specifications:

- Jack Type: 3.5 mm Optical
- Digital Audio Signal-to-Noise Ratio (SNR): > 130 dB
- Digital Audio Total Harmonic Distortion + Noise (THD+N): < -130 dB (0.00003%)

The S/PDIF Optical Output channel status conforms to IEC60958-3 consumer mode digital audio.

The audio output connector on the MacBook is a 3.5 mm electrical/optical combination ("combo") jack. See [3.5 mm (1/8) Combination Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvonc7gezdambtgmytcnrx) for details.

The MacBook computers announced in November 2006, incorporating the Intel Core 2 Duo, include a built-in audio system providing the developer with a set of hardware resources that can be used to record or play audio.

The MacBook computer includes two audio input ports that can be used for recording: an internal mic and a combination line input and optical digital input port.

The internal microphone operates independently from all other audio input ports and is always available. The internal microphone supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the microphone is presented as a stereo data stream with the same data appearing on both the left and right channels. The microphone gain can be adjusted from 0.0 dB to +22.5 dB.

The line input operates independently from all other audio input ports and is always available. The line input supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the line input is presented as a stereo data stream. The line input gain can be adjusted from 0.0 dB to +22.5 dB.

During input of a 1 kHz, full-scale 1VRMS sine wave (44.1 kHz input sample rate, 24-bit sample depth, 0.0 dB input gain, no weighting) the audio line input has the following nominal specifications:

- Jack Type: 3.5 mm stereo
- Maximum Input Voltage: 1VRMS (+2.22 dBu)
- Minimum Voltage Input for Full Scale Output: 75 mV VRMS (-20.28 dBu) at Input Gain = +22.5 dB
- Input Impedance: > 20 kΩ
- Frequency Response: 20 Hz – 20 kHz, +0.5 dB/-3 dB
- Signal-to-Noise Ratio (SNR): > 90 dB
- Total Harmonic Distortion + Noise (THD+N): < -80 dB (0.01%)
- Channel Separation: > 80 dB

Based on playback of a 1 kHz, -1 dBFS 24-bit sine wave playback, 24-bit 44.1 kHz output sample rate (unless otherwise specified below) the digital audio input and output have the following electrical characteristics (nominal specifications):

- Fsi – input sample rates: 44.1 kHz, 48 kHz, or 96 kHz
- bits per sample: 16-bit or 24-bit
- SNR: > 130 dB
- THD+N: < -130 dB (0.00003%)

The MacBook computer includes three audio output ports that can be used to play audio: internal speakers, combination line and headphone output, and S/PDIF optical digital output.

The internal speakers are automatically selected for audio output if no external device is detected at both the line/headphone output port and the S/PDIF optical digital output port. The internal speakers support a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz.

The line/headphone output is automatically selected for audio output if no external device is detected at the S/PDIF optical digital output port. The line/headphone output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. The line/headphone output volume can be adjusted from 0.0 dB to -95.25 dB.

During playback of a 1 kHz, full-scale sine wave (44.1 kHz output sample rate, 24-bit sample depth, 100 kΩ load, unless otherwise specified) the audio line output has the following nominal specifications:

- Jack Type: 3.5 mm Stereo
- Maximum Output Voltage: 1VRMS (+2.22 dBu)
- Output Impedance: < 24 Ω
- Frequency Response: 20 Hz – 20 kHz, +0.5 dB/-3 dB
- Signal-to-Noise Ratio (SNR): > 90 dB
- Total Harmonic Distortion + Noise (THD+N): < -80 dB (0.01%)
- Channel Separation: > 75 dB

The S/PDIF optical digital output is automatically selected when a S/PDIF optical digital output external device is detected. The S/PDIF optical digital output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz or 96 kHz in PCM format. In addition, the S/PDIF optical digital output supports a stereo data stream at 16 bits per sample and at sample rates of 44.1 kHz, 48 kHz, 88.2 kHz, 96 kHz, 176.4 kHz, or 192 kHz in AC3 Encoded Audio format.

During playback of a 1KHz, full-scale sine wave (S/PDIF output format, 44.1 kHz output sample rate, 24-bit sample depth, unless otherwise specified) the digital audio output has the following nominal specifications:

- Jack Type: 3.5 mm Optical
- Digital Audio Signal-to-Noise Ratio (SNR): > 130 dB
- Digital Audio Total Harmonic Distortion + Noise (THD+N): < -130 dB (0.00003%)

The S/PDIF Optical Output channel status conforms to IEC60958-3 consumer mode digital audio.

The audio output connector on the MacBook is a 3.5 mm electrical/optical combination ("combo") jack. See [3.5 mm (1/8) Combination Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvonc7gezdambtgmytcnrx) for details.

The MacBook computers announced in May 2006, incorporating the Intel Core Duo, include a built-in audio system providing the developer with a set of hardware resources that can be used to record or play audio.

The MacBook computer includes two audio input ports that can be used for recording: an internal mic and a combination line input and optical digital input port.

The internal microphone operates independently from all other audio input ports and is always available. The internal microphone supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the microphone is presented as a stereo data stream with the same data appearing on both the left and right channels. The microphone gain can be adjusted from 0.0 dB to +22.5 dB.

The line input operates independently from all other audio input ports and is always available. The line input supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the line input is presented as a stereo data stream. The line input gain can be adjusted from 0.0 dB to +22.5 dB.

During input of a 1 kHz, full-scale 1 VRMS sine wave (44.1 kHz input sample rate, 24-bit sample depth, 0.0 dB input gain, no weighting) the audio line input has the following nominal specifications:

- Jack type: 3.5 mm stereo
- Maximum input voltage: 1 VRMS (+2.22 dBu)
- Minimum voltage input for full scale output: 75 mVRMS (-20.28 dBu) at input gain = +22.5 dB
- Input Impedance: > 20 kΩ
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: > 80 dB

Based on playback of a 1 kHz, -1 dBFS 24-bit sine wave playback, 24-bit 44.1 kHz output sample rate (unless otherwise specified below) the digital audio input and output have the following electrical characteristics (nominal specifications):

- FSI – input sample rates: 44.1 kHz, 48 kHz, or 96 kHz
- bits per sample: 16-bit or 24-bit
- Signal-to-noise ratio (SNR): > 130 dB
- Total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The MacBook computer includes three audio output ports that can be used to play audio: internal speakers, combination line and headphone output, and S/PDIF optical digital output.

The internal speakers are automatically selected for audio output if no external device is detected at either the line/headphone output port or the S/PDIF optical digital output port. The internal speakers support a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz.

The line/headphone output is automatically selected for audio output if no external device is detected at the S/PDIF optical digital output port. The line/headphone output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. The line/headphone output volume can be adjusted from 0.0 dB to -95.25 dB.

During playback of a 1 kHz, full-scale sine wave (44.1 kHz output sample rate, 24-bit sample depth, 100 kΩ load, unless otherwise specified) the audio line output has the following nominal specifications:

- Jack type: 3.5 mm stereo
- Maximum output voltage: 1 VRMS (+2.22 dBu)
- Output impedance: < 24 Ω
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: > 75 dB

The S/PDIF optical digital output is automatically selected when a S/PDIF optical digital output external device is detected. The S/PDIF optical digital output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz or 96 kHz in PCM format. In addition, the S/PDIF optical digital output supports a stereo data stream at 16 bits per sample and at sample rates of 44.1 kHz, 48 kHz, 88.2 kHz, 96 kHz, 176.4 kHz, or 192 kHz in AC-3 encoded audio format.

During playback of a 1 kHz, full-scale sine wave (S/PDIF output format, 44.1 kHz output sample rate, 24-bit sample depth, unless otherwise specified) the digital audio output has the following nominal specifications:

- Jack type: 3.5 mm optical
- Digital audio signal-to-noise ratio (SNR): > 130 dB
- Digital audio total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The S/PDIF optical output channel status conforms to IEC 60958-3 consumer mode digital audio.

The audio output connector on the MacBook is a 3.5 mm electrical/optical combination (combo) jack. For details, see [3.5 mm (1/8) Combination Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvonc7gezdambtgmytcnrx).

This section provides audio-specific information for MacBook Pro computers.

The 17-inch MacBook Pro computers introduced in February 2008, incorporating the Intel Core 2 Duo processor on 45 nm process technology, include a built-in audio system providing the developer with a set of hardware resources that can be used to record or play audio.

The 17-inch MacBook Pro computer includes two audio input ports that can be used for recording: an internal mic and a combination line input and optical digital input port.

The internal microphone operates independently from all other audio input ports and is always available. The internal microphone supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.100 kHz, 48.000 kHz, or 96.000 kHz. Audio recorded from the microphone is presented as a stereo data stream with the same data appearing on both the left and right channels. The microphone gain can be adjusted from -16.0 dB to +30.0 dB.

The line input operates independently from all other audio input ports and is always available. The line input supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.100 kHz, 48.000 kHz, or 96.000 kHz. Audio recorded from the line input is presented as a stereo data stream. The line input gain can be adjusted from -16.0 dB to +30.0 dB.

During input of a 1 kHz, full-scale 1VRMS sine wave (44.1 kHz input sample rate, 24-bit sample depth, 0.0 dB input gain, no weighting) the audio line input has the following nominal specifications:

- Jack type: 3.5 mm stereo
- Maximum input voltage: 2 VRMS (+8.2 dBu)
- Minimum voltage input for full scale output: 62 mVRMS (-21.93 dBu) at input gain = +30 dB
- Input impedance: > 13 kΩ
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -75 dB (0.02%)
- Channel separation: > 90 dB

Based on playback of a 1 kHz, -1 dBFS 24-bit sine wave playback, 24-bit 44.1 kHz output sample rate (unless otherwise specified below) the digital audio input and output have the following electrical characteristics (nominal specifications):

- FSI – input sample rates: 44.1 kHz, 48 kHz, or 96 kHz
- Bits per sample: 16-bit, 20-bit, or 24-bit
- Signal-to-noise ratio (SNR): > 130 dB
- Total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The 17-inch MacBook Pro computer includes the audio output ports that can be used to play audio: internal speakers, combination headphone output, and S/PDIF optical digital output.

The internal speakers are automatically selected for audio output if no external device is detected at either the line/headphone output port or the S/PDIF optical digital output port. The internal speakers support a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.100 kHz, 48.000 kHz, or 96.000 kHz.

The line/headphone output is automatically selected for audio output if no external device is detected at the S/PDIF optical digital output port. The line/headphone output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.100 kHz, 48.000 kHz, or 96.000 kHz. The line/headphone output volume can be adjusted from 0.0 dB to -95.25 dB.

During playback of a 1 kHz, full-scale sine wave (44.1 kHz output sample rate, 24-bit sample depth, 100 kΩ load, unless otherwise specified) the audio line output has the following nominal specifications:

- Jack type: 3.5 mm stereo
- Maximum output voltage: 2 VRMS (+8.24 dBu)
- Output impedance: < 24 Ω
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: > 75 dB

The S/PDIF optical digital output is automatically selected when a S/PDIF optical digital output external device is detected. The S/PDIF optical digital output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.100 kHz, 48.000 kHz or 96.000 kHz in PCM format. In addition, the S/PDIF optical digital output supports AC-3 encoded audio format.

During playback of a 1 kHz, full-scale sine wave (S/PDIF output format, 44.1 kHz output sample rate, 24-bit sample depth, unless otherwise specified) the digital audio output has the following nominal specifications:

- Jack type: 3.5 mm optical
- Digital audio signal-to-noise ratio (SNR): > 130 dB
- Digital audio total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The S/PDIF optical output channel status conforms to IEC 60958-3 consumer mode digital audio.

The audio output connector on the 17-inch MacBook Pro is a 3.5 mm electrical/optical combination (combo) jack. For details, see [3.5 mm (1/8) Combination Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvonc7gezdambtgmytcnrx).

The 15-inch MacBook Pro computers introduced in February 2008, incorporating the Intel Core 2 Duo processor on 45 nm process technology, include a built-in audio system providing the developer with a set of hardware resources that can be used to record or play audio.

The 15-inch MacBook Pro computer includes two audio input ports that can be used for recording: an internal mic and a combination line input and optical digital input port.

The internal microphone operates independently from all other audio input ports and is always available. The internal microphone supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the microphone is presented as a stereo data stream with the same data appearing on both the left and right channels. The microphone gain can be adjusted from -16.0 dB to +30.0 dB.

The line input operates independently from all other audio input ports and is always available. The line input supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the line input is presented as a stereo data stream. The line input gain can be adjusted from 0.0 dB to +30 dB.

During input of a 1 kHz, full-scale 1 VRMS sine wave (44.1 kHz input sample rate, 24-bit sample depth, 0.0 dB input gain, no weighting) the audio line input has the following nominal specifications:

- Jack type: 3.5 mm stereo
- Maximum input voltage: 1 VRMS (+2.22 dBu)
- Minimum voltage input for full scale output: 31 mVRMS (-27.95 dBu) at input gain = +30 dB
- Input impedance: > 20 kΩ
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -75 dB (0.02%)
- Channel separation: > 80 dB

Based on playback of a 1 kHz, -1 dBFS 24-bit sine wave playback, 24-bit 44.1 kHz output sample rate (unless otherwise specified below) the digital audio input and output have the following electrical characteristics (nominal specifications):

- FSI – input sample rates: 44.1 kHz, 48 kHz, or 96 kHz
- Bits per sample: 16-bit or 24-bit
- Signal-to-noise ratio (SNR): > 130 dB
- Total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The 15-inch MacBook Pro computer includes three audio output ports that can be used to play audio: internal speakers, combination line and headphone output, and S/PDIF optical digital output.

The internal speakers are automatically selected for audio output if no external device is detected at either the line/headphone output port or the S/PDIF optical digital output port. The internal speakers support a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz.

The line/headphone output is automatically selected for audio output if no external device is detected at the S/PDIF optical digital output port. The line/headphone output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. The line/headphone output volume can be adjusted from 0.0 dB to -95.25 dB.

During playback of a 1 kHz, full-scale sine wave (44.1 kHz output sample rate, 24-bit sample depth, 100 kΩ load, unless otherwise specified) the audio line output has the following nominal specifications:

- Jack type: 3.5 mm stereo
- Maximum output voltage: 2 VRMS (+8.24 dBu)
- Output impedance: < 24 Ω
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: > 75 dB

The S/PDIF optical digital output is automatically selected when a S/PDIF optical digital output external device is detected. The S/PDIF optical digital output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz or 96 kHz in PCM format. In addition, the S/PDIF optical digital output supports AC-3 encoded audio format.

During playback of a 1 kHz, full-scale sine wave (S/PDIF output format, 44.1 kHz output sample rate, 24-bit sample depth, unless otherwise specified) the digital audio output has the following nominal specifications:

- Jack type: 3.5 mm optical
- Digital audio signal-to-noise ratio (SNR): > 130 dB
- Digital audio total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The S/PDIF optical output channel status conforms to IEC 60958-3 consumer mode digital audio.

The audio output connector on the 15-inch MacBook Pro is a 3.5 mm electrical/optical combination (combo) jack. For details, see 3.5 mm (1/8) Combination Audio Jack.

The 17-inch MacBook Pro computers introduced in June 2007 and November 2007, incorporating the Intel Core 2 Duo, include a built-in audio system providing the developer with a set of hardware resources that can be used to record or play audio.

The 17-inch MacBook Pro computer includes two audio input ports that can be used for recording: an internal mic and a combination line input and optical digital input port.

The internal microphone operates independently from all other audio input ports and is always available. The internal microphone supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.100 kHz, 48.000 kHz, or 96.000 kHz. Audio recorded from the microphone is presented as a stereo data stream with the same data appearing on both the left and right channels. The microphone gain can be adjusted from 0.0 dB to +22.5 dB.

The line input operates independently from all other audio input ports and is always available. The line input supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.100 kHz, 48.000 kHz, or 96.000 kHz. Audio recorded from the line input is presented as a stereo data stream. The line input gain can be adjusted from 0.0 dB to +22.5 dB.

During input of a 1 kHz, full-scale 1VRMS sine wave (44.1 kHz input sample rate, 24-bit sample depth, 0.0 dB input gain, no weighting) the audio line input has the following nominal specifications:

- Jack type: 3.5 mm stereo
- Maximum input voltage: 2 VRMS (+8.2 dBu)
- Minimum voltage input for full scale output: 75 mVRMS (-20.28 dBu) at input gain = +22.5 dB
- Input impedance: > 20 kΩ
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: > 80 dB

Based on playback of a 1 kHz, -1 dBFS 24-bit sine wave playback, 24-bit 44.1 kHz output sample rate (unless otherwise specified below) the digital audio input and output have the following electrical characteristics (nominal specifications):

- FSI – input sample rates: 44.1 kHz, 48 kHz, or 96 kHz
- Bits per sample: 16-bit or 24-bit
- Signal-to-noise ratio (SNR): > 130 dB
- Total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The 17-inch MacBook Pro computer includes the audio output ports that can be used to play audio: internal speakers, combination headphone output, and S/PDIF optical digital output.

The internal speakers are automatically selected for audio output if no external device is detected at either the line/headphone output port or the S/PDIF optical digital output port. The internal speakers support a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.100 kHz, 48.000 kHz, or 96.000 kHz.

The line/headphone output is automatically selected for audio output if no external device is detected at the S/PDIF optical digital output port. The line/headphone output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.100 kHz, 48.000 kHz, or 96.000 kHz. The line/headphone output volume can be adjusted from 0.0 dB to -95.25 dB.

During playback of a 1 kHz, full-scale sine wave (44.1 kHz output sample rate, 24-bit sample depth, 100 kΩ load, unless otherwise specified) the audio line output has the following nominal specifications:

- Jack type: 3.5 mm stereo
- Maximum output voltage: 2 VRMS (+8.24 dBu)
- Output impedance: < 24 Ω
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: > 75 dB

The S/PDIF optical digital output is automatically selected when a S/PDIF optical digital output external device is detected. The S/PDIF optical digital output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.100 kHz, 48.000 kHz or 96.000 kHz in PCM format. In addition, the S/PDIF optical digital output supports AC-3 encoded audio format.

During playback of a 1 kHz, full-scale sine wave (S/PDIF output format, 44.1 kHz output sample rate, 24-bit sample depth, unless otherwise specified) the digital audio output has the following nominal specifications:

- Jack type: 3.5 mm optical
- Digital audio signal-to-noise ratio (SNR): > 130 dB
- Digital audio total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The S/PDIF optical output channel status conforms to IEC 60958-3 consumer mode digital audio.

The audio output connector on the 17-inch MacBook Pro is a 3.5 mm electrical/optical combination (combo) jack. For details, see [3.5 mm (1/8) Combination Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvonc7gezdambtgmytcnrx).

The 15-inch MacBook Pro computers introduced in June 2007 and November 2007, incorporating the Intel Core 2 Duo, include a built-in audio system providing the developer with a set of hardware resources that can be used to record or play audio.

The 15-inch MacBook Pro computer includes two audio input ports that can be used for recording: an internal mic and a combination line input and optical digital input port.

The internal microphone operates independently from all other audio input ports and is always available. The internal microphone supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the microphone is presented as a stereo data stream with the same data appearing on both the left and right channels. The microphone gain can be adjusted from 0.0 dB to +22.5 dB.

The line input operates independently from all other audio input ports and is always available. The line input supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the line input is presented as a stereo data stream. The line input gain can be adjusted from 0.0 dB to +22.5 dB.

During input of a 1 kHz, full-scale 1 VRMS sine wave (44.1 kHz input sample rate, 24-bit sample depth, 0.0 dB input gain, no weighting) the audio line input has the following nominal specifications:

- Jack type: 3.5 mm stereo
- Maximum input voltage: 1 VRMS (+2.22 dBu)
- Minimum voltage input for full scale output: 75 mVRMS (-20.28 dBu) at input gain = +22.5 dB
- Input impedance: > 20 kΩ
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: > 80 dB

Based on playback of a 1 kHz, -1 dBFS 24-bit sine wave playback, 24-bit 44.1 kHz output sample rate (unless otherwise specified below) the digital audio input and output have the following electrical characteristics (nominal specifications):

- FSI – input sample rates: 44.1 kHz, 48 kHz, or 96 kHz
- Bits per sample: 16-bit or 24-bit
- Signal-to-noise ratio (SNR): > 130 dB
- Total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The 15-inch MacBook Pro computer includes three audio output ports that can be used to play audio: internal speakers, combination line and headphone output, and S/PDIF optical digital output.

The internal speakers are automatically selected for audio output if no external device is detected at either the line/headphone output port or the S/PDIF optical digital output port. The internal speakers support a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz.

The line/headphone output is automatically selected for audio output if no external device is detected at the S/PDIF optical digital output port. The line/headphone output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. The line/headphone output volume can be adjusted from 0.0 dB to -95.25 dB.

During playback of a 1 kHz, full-scale sine wave (44.1 kHz output sample rate, 24-bit sample depth, 100 kΩ load, unless otherwise specified) the audio line output has the following nominal specifications:

- Jack type: 3.5 mm stereo
- Maximum output voltage: 2 VRMS (+8.24 dBu)
- Output impedance: < 24 Ω
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: > 75 dB

The S/PDIF optical digital output is automatically selected when a S/PDIF optical digital output external device is detected. The S/PDIF optical digital output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz or 96 kHz in PCM format. In addition, the S/PDIF optical digital output supports AC-3 encoded audio format.

During playback of a 1 kHz, full-scale sine wave (S/PDIF output format, 44.1 kHz output sample rate, 24-bit sample depth, unless otherwise specified) the digital audio output has the following nominal specifications:

- Jack type: 3.5 mm optical
- Digital audio signal-to-noise ratio (SNR): > 130 dB
- Digital audio total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The S/PDIF optical output channel status conforms to IEC 60958-3 consumer mode digital audio.

The audio output connector on the 15-inch MacBook Pro is a 3.5 mm electrical/optical combination (combo) jack. For details, see 3.5 mm (1/8) Combination Audio Jack.

The 17-inch MacBook Pro computer announced in October 2006, incorporating the Intel Core 2 Duo, includes a built-in audio system providing the developer with a set of hardware resources that can be used to record or play audio.

The 17-inch MacBook Pro computer includes two audio input ports that can be used for recording: an internal mic and a combination line input and optical digital input port.

The internal microphone operates independently from all other audio input ports and is always available. The internal microphone supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the microphone is presented as a stereo data stream with the same data appearing on both the left and right channels. The microphone gain can be adjusted from 0.0 dB to +22.5 dB.

The line input operates independently from all other audio input ports and is always available. The line input supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the line input is presented as a stereo data stream. The line input gain can be adjusted from 0.0 dB to +22.5 dB.

During input of a 1 kHz, full-scale 1VRMS sine wave (44.1 kHz input sample rate, 24-bit sample depth, 0.0 dB input gain, no weighting) the audio line input has the following nominal specifications:

- Jack type: 3.5 mm stereo
- Maximum input voltage: 2 VRMS (+8.2 dBu)
- Minimum voltage input for full scale output: 75 mVRMS (-20.28 dBu) at input gain = +22.5 dB
- Input impedance: > 20 kΩ
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: > 80 dB

Based on playback of a 1 kHz, -1 dBFS 24-bit sine wave playback, 24-bit 44.1 kHz output sample rate (unless otherwise specified below) the digital audio input and output have the following electrical characteristics (nominal specifications):

- FSI – input sample rates: 44.1 kHz, 48 kHz, or 96 kHz
- Bits per sample: 16-bit or 24-bit
- Signal-to-noise ratio (SNR): > 130 dB
- Total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The 17-inch MacBook Pro computer includes the audio output ports that can be used to play audio: internal speakers, combination headphone output, and S/PDIF optical digital output.

The internal speakers are automatically selected for audio output if no external device is detected at either the line/headphone output port or the S/PDIF optical digital output port. The internal speakers support a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz.

The line/headphone output is automatically selected for audio output if no external device is detected at the S/PDIF optical digital output port. The line/headphone output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. The line/headphone output volume can be adjusted from 0.0 dB to -95.25 dB.

During playback of a 1 kHz, full-scale sine wave (44.1 kHz output sample rate, 24-bit sample depth, 100 kΩ load, unless otherwise specified) the audio line output has the following nominal specifications:

- Jack type: 3.5 mm stereo
- Maximum output voltage: 1.45 VRMS (+5.45 dBu)
- Output impedance: < 24 Ω
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: >70 dB

The S/PDIF optical digital output is automatically selected when a S/PDIF optical digital output external device is detected. The S/PDIF optical digital output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz or 96 kHz in PCM format. In addition, the S/PDIF optical digital output supports AC-3 encoded audio format.

During playback of a 1 kHz, full-scale sine wave (S/PDIF output format, 44.1 kHz output sample rate, 24-bit sample depth, unless otherwise specified) the digital audio output has the following nominal specifications:

- Jack type: 3.5 mm optical
- Digital audio signal-to-noise ratio (SNR): > 130 dB
- Digital audio total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The S/PDIF optical output channel status conforms to IEC 60958-3 consumer mode digital audio.

The audio output connector on the 17-inch MacBook Pro is a 3.5 mm electrical/optical combination (combo) jack. For details, see [3.5 mm (1/8) Combination Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvonc7gezdambtgmytcnrx).

The 15-inch MacBook Pro computers announced in October 2006, incorporating the Intel Core 2 Duo, include a built-in audio system providing the developer with a set of hardware resources that can be used to record or play audio.

The 15-inch MacBook Pro computer includes two audio input ports that can be used for recording: an internal mic and a combination line input and optical digital input port.

The internal microphone operates independently from all other audio input ports and is always available. The internal microphone supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the microphone is presented as a stereo data stream with the same data appearing on both the left and right channels. The microphone gain can be adjusted from 0.0 dB to +22.5 dB.

The line input operates independently from all other audio input ports and is always available. The line input supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the line input is presented as a stereo data stream. The line input gain can be adjusted from 0.0 dB to +22.5 dB.

During input of a 1 kHz, full-scale 1 VRMS sine wave (44.1 kHz input sample rate, 24-bit sample depth, 0.0 dB input gain, no weighting) the audio line input has the following nominal specifications:

- Jack type: 3.5 mm stereo
- Maximum input voltage: 1 VRMS (+2.22 dBu)
- Minimum voltage input for full scale output: 75 mVRMS (-20.28 dBu) at input gain = +22.5 dB
- Input impedance: > 20 kΩ
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: > 80 dB

Based on playback of a 1 kHz, -1 dBFS 24-bit sine wave playback, 24-bit 44.1 kHz output sample rate (unless otherwise specified below) the digital audio input and output have the following electrical characteristics (nominal specifications):

- FSI – input sample rates: 44.1 kHz, 48 kHz, or 96 kHz
- Bits per sample: 16-bit or 24-bit
- Signal-to-noise ratio (SNR): > 130 dB
- Total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The 15-inch MacBook Pro computer includes three audio output ports that can be used to play audio: internal speakers, combination line and headphone output, and S/PDIF optical digital output.

The internal speakers are automatically selected for audio output if no external device is detected at either the line/headphone output port or the S/PDIF optical digital output port. The internal speakers support a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz.

The line/headphone output is automatically selected for audio output if no external device is detected at the S/PDIF optical digital output port. The line/headphone output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. The line/headphone output volume can be adjusted from 0.0 dB to -95.25 dB.

During playback of a 1 kHz, full-scale sine wave (44.1 kHz output sample rate, 24-bit sample depth, 100 kΩ load, unless otherwise specified) the audio line output has the following nominal specifications:

- Jack type: 3.5 mm stereo
- Maximum output voltage: 1 VRMS (+2.22 dBu)
- Output impedance: < 24 Ω
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: >70 dB

The S/PDIF optical digital output is automatically selected when a S/PDIF optical digital output external device is detected. The S/PDIF optical digital output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz or 96 kHz in PCM format. In addition, the S/PDIF optical digital output supports AC-3 encoded audio format.

During playback of a 1 kHz, full-scale sine wave (S/PDIF output format, 44.1 kHz output sample rate, 24-bit sample depth, unless otherwise specified) the digital audio output has the following nominal specifications:

- Jack type: 3.5 mm optical
- Digital audio signal-to-noise ratio (SNR): > 130 dB
- Digital audio total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The S/PDIF optical output channel status conforms to IEC 60958-3 consumer mode digital audio.

The audio output connector on the 15-inch MacBook Pro is a 3.5 mm electrical/optical combination (combo) jack. For details, see [3.5 mm (1/8) Combination Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvonc7gezdambtgmytcnrx).

The 17-inch MacBook Pro computers announced in April 2006, incorporating the Intel Core Duo microprocessor, include a built-in audio system providing the developer with a set of hardware resources that can be used to record or play audio.

The 17-inch MacBook Pro computer includes two audio input ports that can be used for recording: an internal mic and a combination line input and optical digital input port.

The internal microphone operates independently from all other audio input ports and is always available. The internal microphone supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the microphone is presented as a stereo data stream with the same data appearing on both the left and right channels. The microphone gain can be adjusted from 0.0 dB to +22.5 dB.

The line input operates independently from all other audio input ports and is always available. The line input supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the line input is presented as a stereo data stream. The line input gain can be adjusted from 0.0 dB to +22.5 dB.

During input of a 1 kHz, full-scale 1VRMS sine wave (44.1 kHz input sample rate, 24-bit sample depth, 0.0 dB input gain, no weighting) the audio line input has the following nominal specifications:

- Jack type: 3.5 mm stereo
- Maximum input voltage: 2 VRMS (+8.2 dBu)
- Minimum voltage input for full scale output: 75 mVRMS (-20.28 dBu) at input gain = +22.5 dB
- Input impedance: > 20 kΩ
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: > 80 dB

Based on playback of a 1 kHz, -1 dBFS 24-bit sine wave playback, 24-bit 44.1 kHz output sample rate (unless otherwise specified below) the digital audio input and output have the following electrical characteristics (nominal specifications):

- FSI – input sample rates: 44.1 kHz, 48 kHz, or 96 kHz
- Bits per sample: 16-bit or 24-bit
- Signal-to-noise ratio (SNR): > 130 dB
- Total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The 17-inch MacBook Pro computer includes the audio output ports that can be used to play audio: internal speakers, combination headphone output, and S/PDIF optical digital output.

The internal speakers are automatically selected for audio output if no external device is detected at either the line/headphone output port or the S/PDIF optical digital output port. The internal speakers support a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz.

The line/headphone output is automatically selected for audio output if no external device is detected at the S/PDIF optical digital output port. The line/headphone output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. The line/headphone output volume can be adjusted from 0.0 dB to -95.25 dB.

During playback of a 1 kHz, full-scale sine wave (44.1 kHz output sample rate, 24-bit sample depth, 100 kΩ load, unless otherwise specified) the audio line output has the following nominal specifications:

- Jack type: 3.5 mm stereo
- Maximum output voltage: 1.45 VRMS (+5.45 dBu)
- Output impedance: < 24 Ω
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: >70 dB

The S/PDIF optical digital output is automatically selected when a S/PDIF optical digital output external device is detected. The S/PDIF optical digital output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz or 96 kHz in PCM format. In addition, the S/PDIF optical digital output supports a stereo data stream at 16 bits per sample and at sample rates of 44.1 kHz, 48 kHz, 88.2 kHz, 96 kHz, 176.4 kHz, or 192 kHz in AC-3 encoded audio format.

During playback of a 1 kHz, full-scale sine wave (S/PDIF output format, 44.1 kHz output sample rate, 24-bit sample depth, unless otherwise specified) the digital audio output has the following nominal specifications:

- Jack type: 3.5 mm optical
- Digital audio signal-to-noise ratio (SNR): > 130 dB
- Digital audio total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The S/PDIF optical output channel status conforms to IEC 60958-3 consumer mode digital audio.

The audio output connector on the 17-inch MacBook Pro is a 3.5 mm electrical/optical combination (combo) jack. For details, see [3.5 mm (1/8) Combination Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvonc7gezdambtgmytcnrx).

The 15-inch MacBook Pro computers announced in January 2006, incorporating the Intel Core Duo microprocessor, include a built-in audio system providing the developer with a set of hardware resources that can be used to record or play audio.

The MacBook Pro computer includes two audio input ports that can be used for recording: an internal mic and a combination line input and optical digital input port.

The internal microphone operates independently from all other audio input ports and is always available. The internal microphone supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the microphone is presented as a stereo data stream with the same data appearing on both the left and right channels. The microphone gain can be adjusted from 0.0 dB to +22.5 dB.

The line input operates independently from all other audio input ports and is always available. The line input supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the line input is presented as a stereo data stream. The line input gain can be adjusted from 0.0 dB to +22.5 dB.

During input of a 1 kHz, full-scale 1 VRMS sine wave (44.1 kHz input sample rate, 24-bit sample depth, 0.0 dB input gain, no weighting) the audio line input has the following nominal specifications:

- Jack type: 3.5 mm stereo
- Maximum input voltage: 1 VRMS (+2.22 dBu)
- Minimum voltage input for full scale output: 75 mVRMS (-20.28 dBu) at input gain = +22.5 dB
- Input impedance: > 20 kΩ
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: > 80 dB

Based on playback of a 1 kHz, -1 dBFS 24-bit sine wave playback, 24-bit 44.1 kHz output sample rate (unless otherwise specified below) the digital audio input and output have the following electrical characteristics (nominal specifications):

- FSI – input sample rates: 44.1 kHz, 48 kHz, or 96 kHz
- Bits per sample: 16-bit or 24-bit
- Signal-to-noise ratio (SNR): > 130 dB
- Total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The MacBook Pro computer includes three audio output ports that can be used to play audio: internal speakers, combination line and headphone output, and S/PDIF optical digital output.

The internal speakers are automatically selected for audio output if no external device is detected at either the line/headphone output port or the S/PDIF optical digital output port. The internal speakers support a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz.

The line/headphone output is automatically selected for audio output if no external device is detected at the S/PDIF optical digital output port. The line/headphone output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. The line/headphone output volume can be adjusted from 0.0 dB to -95.25 dB.

During playback of a 1 kHz, full-scale sine wave (44.1 kHz output sample rate, 24-bit sample depth, 100 kΩ load, unless otherwise specified) the audio line output has the following nominal specifications:

- Jack type: 3.5 mm stereo
- Maximum output voltage: 1 VRMS (+2.22 dBu)
- Output impedance: < 24 Ω
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: >70 dB

The S/PDIF optical digital output is automatically selected when a S/PDIF optical digital output external device is detected. The S/PDIF optical digital output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz or 96 kHz in PCM format. In addition, the S/PDIF optical digital output supports a stereo data stream at 16 bits per sample and at sample rates of 44.1 kHz, 48 kHz, 88.2 kHz, 96 kHz, 176.4 kHz, or 192 kHz in AC-3 encoded audio format.

During playback of a 1 kHz, full-scale sine wave (S/PDIF output format, 44.1 kHz output sample rate, 24-bit sample depth, unless otherwise specified) the digital audio output has the following nominal specifications:

- Jack type: 3.5 mm optical
- Digital audio signal-to-noise ratio (SNR): > 130 dB
- Digital audio total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The S/PDIF optical output channel status conforms to IEC 60958-3 consumer mode digital audio.

The audio output connector on the MacBook Pro is a 3.5 mm electrical/optical combination (combo) jack. For details, see [3.5 mm (1/8) Combination Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvonc7gezdambtgmytcnrx).

This section provides Audio-specific information for MacBook Air computers. Refer to the specific MacBook Air developer note for additional information.

The MacBook Air computer introduced in January 2008, incorporating the Intel Core 2 Duo, includes a built-in audio system providing the developer with omni-directional microphone, mono speaker, and analog/headphone output.

The internal microphone operates independently from all other audio input ports and is always available. The internal microphone supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz or 48 kHz. Audio recorded from the microphone is presented as a stereo data stream with the same data appearing on both the left and right channels. The microphone gain can be adjusted from -16.0 dB to +30.0 dB.

The internal speaker is automatically selected for audio output if no external device is detected at the line/headphone output port. The internal speaker supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1kHz, 48 kHz, or 96 kHz.

The line/headphone output is automatically selected for audio output when a stereo plug is inserted into the jack. The line/headphone output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. The line/headphone output volume can be adjusted from 0.0 dB to -64.0 dB.

During playback of a 1 kHz, full-scale sine wave (44.1 kHz output sample rate, 24-bit sample depth, 100 kΩ load, unless otherwise specified) the audio line output has the following nominal specifications:

- Jack Type: 3.5 mm Stereo
- Maximum Output Voltage: 1.2 VRMS (+3.8 dBu)
- Output Impedance: < 24 Ω
- Frequency Response: 20 Hz – 20 kHz, +0.5 dB/-3 dB
- Signal-to-Noise Ratio (SNR): > 90 dB
- Total Harmonic Distortion + Noise (THD+N): < -80 dB (0.01%)
- Channel Separation: >80 dB

The audio output connector on the MacBook Air is a 3.5 mm stereo electrical audio jack. See [Optical Digital Audio Input/Output Specifications](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzyfvjvoms7gezdambtgmytcnrx) for details.

This section provides audio-specific information for Mac mini computers.

The Mac mini computers announced in February 2006, incorporating the Intel Core Duo microprocessor or Intel Core Solo microprocessor, include a built-in audio system providing the developer with a set of hardware resources that can be used to record or play audio.

The Mac mini computer has a combination line input and optical digital input port.

The line input operates independently from all other audio input ports and is always available. The line input supports recording at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. Audio recorded from the line input is presented as a stereo data stream. The line input gain can be adjusted from 0.0 dB to +22.5 dB.

During input of a 1 kHz, full-scale 1 VRMS sine wave (44.1 kHz input sample rate, 24-bit sample depth, 0.0 dB input gain, no weighting) the audio line input has the following nominal specifications:

- Jack type: 3.5 mm stereo
- Maximum input voltage: 1 VRMS (+2.22 dBu)
- Minimum voltage input for full scale output: 75 mVRMS (-20.28 dBu) at input gain = +22.5 dB
- Input impedance: > 20 kΩ
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: > 80 dB

Based on playback of a 1 kHz, -1 dBFS 24-bit sine wave playback, 24-bit 44.1 kHz output sample rate (unless otherwise specified below) the digital audio input and output have the following electrical characteristics (nominal specifications):

- FSI – input sample rates: 44.1 kHz, 48 kHz, or 96 kHz
- Bits per sample: 16-bit or 24-bit
- Signal-to-noise ratio (SNR): > 130 dB
- Total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The Mac mini computer includes three audio output ports that can be used to play audio: internal mono speaker, combination line and headphone output, and S/PDIF optical digital output.

The internal mono speaker is automatically selected for audio output if no external device is detected at either the line/headphone output port or the S/PDIF optical digital output port. The internal speaker supports a data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz.

The line/headphone output is automatically selected for audio output if no external device is detected at the S/PDIF optical digital output port. The line/headphone output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz. The line/headphone output volume can be adjusted from 0.0 dB to -95.25 dB.

During playback of a 1 kHz, full-scale sine wave (44.1 kHz output sample rate, 24-bit sample depth, 100 kΩ load, unless otherwise specified) the audio line output has the following nominal specifications:

- Jack type: 3.5 mm stereo
- Maximum output voltage: 1 VRMS (+2.22 dBu)
- Output impedance: < 24 Ω
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/-3 dB
- Signal-to-noise ratio (SNR): > 90 dB
- Total harmonic distortion + noise (THD+N): < -80 dB (0.01%)
- Channel separation: > 75 dB

The S/PDIF optical digital output is automatically selected when a S/PDIF optical digital output external device is detected. The S/PDIF optical digital output supports a stereo data stream at bit depths of 16, 20, or 24 bits per sample and at sample rates of 44.1 kHz, 48 kHz, or 96 kHz in PCM format. In addition, the S/PDIF optical digital output supports a stereo data stream at 16 bits per sample and at sample rates of 44.1 kHz, 48 kHz, 88.2 kHz, 96 kHz, 176.4 kHz, or 192 kHz in AC-3 encoded audio format.

During playback of a 1 kHz, full-scale sine wave (S/PDIF output format, 44.1 kHz output sample rate, 24-bit sample depth, unless otherwise specified) the digital audio output has the following nominal specifications:

- Jack type: 3.5 mm optical
- Digital audio signal-to-noise ratio (SNR): > 130 dB
- Digital audio Total harmonic distortion + noise (THD+N): < -130 dB (0.00003%)

The S/PDIF Optical Output channel status conforms to IEC 60958-3 consumer mode digital audio.

The audio output connector on the Mac mini is a 3.5 mm electrical/optical combination (combo) jack. See [3.5 mm (1/8) Combination Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvonc7gezdambtgmytcnrx) for details.

This section provides audio-specific information for Power Mac computers.

The Power Mac G5 computer supports a sound system with both digital and analog audio.

Under the control of the system software, the audio circuitry digitally creates and records sounds. The Power Mac G5 computer can receive input from either the analog input or the digital input. However, it can output simultaneously to digital and analog devices: the internal speaker, the headphone jack, the audio output jack, and the optical digital output connector.

By default, when components are plugged into the headphone jack or the rear line-out, the sound system mutes the internal speaker.

The headphones, rear line-out jack, and optical digital output are muted only when selected in System Preferences. Muting and sound options are set in the Output pane of Sound Preferences.

The analog and digital audio circuitries are not independent. Different audio streams cannot be played to the analog and digital circuitry. The selection of digital or analog output is performed through the Sound pane in System Preferences.

The audio circuitry and audio device drivers handle audio data in multiple formats. Both digital and analog audio circuitry handle audio input and output data at sample rates of 32 kHz, 44.1 kHz, 48 kHz, 64 kHz, 88.2 kHz, and 96 kHz at sample depths of 16 bits and 24 bits.

If audio data sampled from another computer at a lower rate is played as output on the Power Mac G5, Core Audio software (Mac OS X level audio API) transparently up-samples the data to the currently set sampling frequency prior to sending the audio data to the audio circuitry. To maximize audio fidelity, the Core Audio samples are stored as 32-bit floating point.

For more information about audio APIs in Mac OS X, visit the Apple [ADC Audio technology website](https://developer.apple.com/audio/).

Digital data is transmitted to and from the digital audio I/O using optical cables. The 7.5 mm digital optical TOSLINK input and output connectors are located on the back of the enclosure. For details, see [7.5 mm Optical Digital Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvonk7gezdambtgmytcnrx).

The digital I/O circuitry performs input clock recovery on an incoming data stream. To enable bit-accurate copies, select External Clock in the Clock Source pop-up menu in the Audio MIDI Setup application in `Applications/Utilities`.

Audio signals from the audio input jack are converted to digital data internally. All audio is handled digitally inside the computer, including audio data from the CD or DVD drive and from devices connected to the USB and FireWire ports. Audio data is converted to analog form for output to the internal speaker, the headphones, line output jacks, or external speakers.

For details on the optical digital input and output electrical specifications, refer to [Optical Digital Audio Input/Output Specifications](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzyfvjvoms7gezdambtgmytcnrx).

The Power Mac G5 computer also has the ability to lock its internal audio hardware to the incoming audio stream to synchronize the audio subsystem to an external device supplying the audio stream. This function allows audio and video to play in sync with the external audio or video device. The data format for signals transmitted over the optical cable is S/PDIF protocol IEC 60958-3.

Because no hardware sample rate converter is available to the Power Mac G5, Core Audio services provide the sample rate conversion.

When the Power Mac G5 computer is set to external clocking, the computer audio circuitry tracks and follows the outgoing digital sampling rate and lock the internal audio hardware to the sampling rate of the external device. The external clock must be stable enough to be locked onto, otherwise the digital circuit signals an error and the driver falls back to using the internal clock.

When the Power Mac G5 computer is set for internal clocking, the computer audio circuitry runs using the computer’s internal clock.

Based on playback of a 1 kHz, -1 dBFS 24-bit sine wave playback, 24-bit 44.1 kHz output sample rate (unless otherwise specified below) the digital audio input and output have the following electrical characteristics (nominal specifications):

- FSI input sample rates: 32 kHz to 96 kHz
- Bits per sample: 16-bit or 24-bit
- SNR: > 130 dB
- THD+N (external clock mode): < -130 dB (0.00003%)

The Power Mac G5 has a stereo audio line-in jack on the back panel. For details, see [3.5 mm (1/8) Stereo Electrical Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvoms7gezdambtgmytcnrx).

The audio inputs are designed to accept high-level audio signals: 2 VRMS (+8 .2 dBu), which is the standard output level from CD and DVD players. The output level of some consumer audio devices is lower, often 0.316 VRMS (–10 dBV). Audio recordings made on the Power Mac G5 with such low-level devices have more noise than those made with high-level devices. The user may obtain better results by connecting an amplifier between the low-level device and the computer’s audio input jack.

Based on a 1 kHz, 2 VRMS sine wave input, 24-bit 44.1 kHz input format, 0 dB input gain and no weighting, the line input has the following electrical characteristics:

- Maximum input voltage: 2 VRMS (+8.2 dBu)
- Input impedance: > 20 kΩ
- Bits per sample: 16-bit or 24-bit
- Channel separation: > 75 dB
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/–3.0 dB
- Total harmonic distortion + noise (THD+N): < –78 dB (no weighting)

The Power Mac G5 has a stereo output jack on the back of the enclosure. The audio output jack is suitable for connecting amplified external speakers or other high input impedance (> 1 kΩ) audio equipment. For details, see [3.5 mm (1/8) Stereo Electrical Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvoms7gezdambtgmytcnrx).

Based on a 1 kHz, -1 dBFS sine wave playback, 24-bit 44.1 kHz output format, -3 dB output level and 100 kΩ load no weighting (unless otherwise specified below), the line output has the following electrical characteristics (nominal specifications):

- Output voltage (full-scale output): 1.75 VRMS (+7.1 dBu)
- Output impedance: < 50 Ω
- Bits per sample: 16-bit or 24-bit
- Channel separation: > 65 dB
- THD+N (total harmonic distortion + noise): < –75 dB (0.02%)
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/–3.0 dB

The Power Mac G5 has a stereo headphone jack on the front of the enclosure. The headphone jack is a suitable for connecting a standard pair of headphones. When a plug is inserted into the headphone jack, the internal speaker is muted. For details, see [3.5 mm (1/8) Stereo Electrical Audio Jack](Audio%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsnzzfvjvoms7gezdambtgmytcnrx).

Based on a 1 kHz sine wave playback, 24-bit 44.1 kHz output format, -3 dB output level and 100 kΩ load no weighting (unless otherwise specified), the headphone output has the following electrical characteristics (nominal specifications):

- Output voltage (full-scale output): 1.75 VRMS, (+7.1 dBu)
- Output impedance: < 50 Ω
- Bits per sample: 16-bit or 24-bit
- Channel separation: > 60 dB
- Frequency response: 20 Hz to 20 kHz, +0.5 dB/–3.0 dB
- Total harmonic distortion + noise (THD+N ): < –75 dB (0.02%)

[Next](Document%20Revision%20History.md)[Previous](Audio%20Concepts.md)

