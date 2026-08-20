---
title: Mixer iPodEQ AUGraph Test
apple_id: DTS40009555
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2014-01-29'
source_url: https://developer.apple.com/library/archive/samplecode/iPhoneMixerEQGraphTest/Introduction/Intro.html
archived_at: '2026-07-18T03:29:41.601744Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# Mixer iPodEQ AUGraph Test

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2.2, 2014-01-29 Updated for iOS 7.0 SDK. Added SetProperty call setting output stream format for iPodAU. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnjvguwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | iOS 7.0 SDK |
| __Runtime Requirements:__ | iOS 7.0 or later |

Demonstrates how to build an Audio Unit Graph connecting a MultiChannel Mixer to the iPodEQ unit then to the RemoteIO unit.

Two input busses are created each with input volume controls. An overall mixer output volume control is also provided and each bus may be enabled or disabled. The iPodEQ may be enabled or disabled and a preset EQ curve may be chosen via a picker in the iPod Equalizer view. iPhoneMixerEQGraphTest uses 44.1kHz source and sets the hardware sample rate to 44.1kHz to avoid any extraneous sample rate conversions.

"Play Audio" simply calls AUGraphStart while "Stop Audio" calls AUGraphStop. Changing AU volume is performed via AudioUnitSetParameter. The iPodEQ unit presets are returned by using AudioUnitGetProperty asking for the kAudioUnitProperty_FactoryPresets CFArrayRef. A current preset is then selected calling AudioUnitSetProperty using the kAudioUnitProperty_PresentPreset property and passing in the appropriate AUPreset. Note that the AU Host owns the returned CFArray and should release it when done.

Audio data is provided from two stereo audio files. The audio data is AAC compressed and ExtAudioFile is used to convert this data to the Core Audio Canonical uncompressed LPCM client format for input to the multichannel mixer.

All the relevant audio code is in the file AUGraphController.mm

[Next](ReadMe.txt.md)

