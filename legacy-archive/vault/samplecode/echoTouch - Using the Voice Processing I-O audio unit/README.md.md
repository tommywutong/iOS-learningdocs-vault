---
title: echoTouch - Using the Voice Processing I/O audio unit
apple_id: TP40017575
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2016-11-29'
source_url: https://developer.apple.com/library/archive/samplecode/echoTouch/Listings/README_md.html
archived_at: '2026-07-18T03:29:08.447911Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [echoTouch - Using the Voice Processing I/O audio unit](echoTouch%20-%20Using%20the%20Voice%20Processing%20I-O%20audio%20unit.md)


[Next](Source-ViewController.h.md)[Previous](PublicUtility-CAMath.h.md)

# README.md

```
# echoTouch

echoTouch demonstrates using the Voice Processing I/O audio unit for handling audio input and output. The application tests local audio playback and simulated "far-talker" audio playback allowing you to record and listen back to the results. It also lets you to turn on/off the VPIO comparing the recorded results.

The Voice Processor I/O audio unit was discussed in the WWDC Session "Fundamentals of Digital Audio for Mac OS X and iPhone OS" which can be found here: < https://developer.apple.com/devcenter/download.action?path=/videos/wwdc_2010__sd/session_411__fundamentals_of_digital_audio_for_mac_os_x_and_iphone_os.mov >

## Main Files

ViewController.mm
- Source for the main sample implementation.

ViewController.h
- Header for main controller class.

echoTouchHelper.cpp
- Utility functions for setting up the I/O unit, AVAudioSession and loading data for the simulated input audio.

echoTouchHelper.h
- Headear for echoTouchHelper.cpp

echoTouchAppDelegate
- Standard App delegate files.

MeteringViews Folder
- Classes implementing the VU meters.

PublicUtility Folder
- AUOutputBuffer class
- CAStreamBasicDescription class

Audio Folder
- fx.caf : Sound Effects audio file.
- sampleVoiceXXXkHz.wav : Simulated far-talker audio files at various sample rates.

## Version History

Version 1.0 - Initial release.

## Requirements

### Build

Xcode 8.0, iOS 10 SDK

### Runtime

macOS 10.11.6 or greater
iOS 9.3 or greater

Copyright (C) 2016 Apple Inc. All rights reserved.
```

[Next](Source-ViewController.h.md)[Previous](PublicUtility-CAMath.h.md)

