---
title: 'AudioConverter: How do I know when I am done?'
apple_id: DTS10004400
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2007-08-23'
source_url: https://developer.apple.com/library/archive/qa/qa1532/_index.html
archived_at: '2026-07-18T02:32:15.050697Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1532

# AudioConverter: How do I know when I am done?

## Q:  How do I inform AudioConverter I am done processing data?

A: How do I inform AudioConverter I am done processing data?

By returning `noErr` and 0 packets of data, you are signaling to an Audio Converter object that you are out of data and at the logical end of the stream. Upon getting this message, the Audio Converter object will no longer call the input proc expecting to receive data. To get out of this state, you must call `AudioConverterReset`.

If you have no data to convert at this time but are not at the logical end of the stream, your input proc should return 0 packets of data along with any non-zero error code. This error will in turn be returned to you by `AudioConverterFillComplexBuffer`. The next time you call `AudioConverterFillComplexBuffer`, your input proc will get called again.

Audio Converter objects (of type AudioConverterRef) are built using the interfaces in the AudioConverter.h header file in the Audio Toolbox framework.

- [Audio Documentation](https://developer.apple.com/documentation/MusicAudio/index.html)
- [Audio and MIDI on Mac OS X](https://developer.apple.com/audio/pdf/coreaudio.pdf)
- [CoreAudio Mailing List](http://lists.apple.com/mailman/listinfo/coreaudio-api)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-08-23 | New document that describes how to correctly signal AudioConverter when a conversion is completed. |

