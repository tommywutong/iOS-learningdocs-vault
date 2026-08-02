---
title: Sound Manager Codec support in QuickTime 7
apple_id: DTS10003805
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2005-10-26'
source_url: https://developer.apple.com/library/archive/qa/qa1448/_index.html
archived_at: '2026-07-18T02:30:48.994939Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1448

# Sound Manager Codec support in QuickTime 7

## Q:  I have written a Sound Manager codec which supports compression and decompression of variable bitrate (VBR) sound for my particular sound format. After installing QuickTime 7, my codec no longer seems to work. What's going on?

A: QuickTime 7 is now based on Core Audio, allowing it to break free of the limitations of the Sound Manager, adding many new features and capabilities of which developers can take advantage.

For example, QuickTime 7 now supports high-resolution audio (audio sampled at sample rates higher than 64 kHz and up to 192 kHz and beyond) with up to 24 channels and support for surround sound. This is in stark contrast to the implementation of the Sound Manager, which only supports mono and stereo.

With Core Audio as its new audio foundation, QuickTime 7 makes use of the Audio Converter to play back movie audio instead of the old Sound Manager Sound Converter.  While the Audio Converter does have a compatibility layer that allows it to use the older Sound Converter, it does not handle VBR codecs, only constant bitrate (CBR) codecs. This means Sound Manager VBR codecs must be rewritten as Core Audio style Audio Codecs in order to work with QuickTime 7.

Core Audio provides excellent starter code for writing an Audio Codec -- there's a sample Audio Codec (an Apple IMA4 Format Encoder) implementation in the Core Audio SDK.

Also, as a convenience for developers who would like their codecs to work with earlier versions of QuickTime (prior to QuickTime 7) the Core Audio SDK contains a sample Audio Codec titled "SMAC".

The SMAC component example code demonstrates how to write a Sound Manager component that will interface to your new Audio Codec component. The codecs that you create (the new Audio Codec and its companion "smac" components) will then be seen by the system both as a Sound Manager codec (codec type: 'scom' and 'sdec') as well as an Audio Codec (codec type: 'aenc' and 'adec'). Applications that use the Sound Manager will then still be able to use your Audio Codec along with applications that interact with Core Audio directly.

__References__

- [Core Audio Website](https://developer.apple.com/audio/)
- Core Audio SDK, installed with the [XCode Tools](https://developer.apple.com/tools/xcode/index.html) at /Developer/Examples/CoreAudio, Audio Codec examples at /Developer/Examples/CoreAudio/AudioCodecs/
- Current updates for the Core Audio SDK (in addition to what is installed by the XCode Tools) can also be found on the [Development Kits](https://developer.apple.com/sdk/) page and in the [Downloads](https://developer.apple.com/audio/download/) section of the Core Audio Website

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-10-26 | New document that describes QuickTime 7 support for constant bitrate and variable bitrate Sound Manager codecs |

