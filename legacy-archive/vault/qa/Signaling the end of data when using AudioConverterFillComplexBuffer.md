---
title: Signaling the end of data when using AudioConverterFillComplexBuffer
apple_id: DTS10002349
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2011-07-21'
source_url: https://developer.apple.com/library/archive/qa/qa1317/_index.html
archived_at: '2026-07-18T02:30:22.640362Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1317

# Signaling the end of data when using AudioConverterFillComplexBuffer

## Q:  When using AudioConverterFillComplexBuffer to convert data, what should I do when I am running out of data?

A: There will be three cases when you are running out of data:

1. End of stream - Inside your input procedure, you must set the total amount of packets read and the sizes of the data in the AudioBufferList to zero. The input procedure should also return noErr. This will signal the AudioConverter that you are out of data. More specifically, set `ioNumberDataPackets` and `ioBufferList->mDataByteSize` to zero in your input proc and return noErr. Where `ioNumberDataPackets` is the amount of data converted and `ioBufferList->mDataByteSize` is the size of the amount of data converted in each AudioBuffer within your input procedure callback. Your input procedure may be called a few more times; you should just keep returning zero and noErr.
2. Some data available from the input stream, but not enough to satisfy the input request - If data was being streamed in real time, there can be a situation where there is not enough data to be processed that meets the amount of data requested in your callback. In this case, you should return noErr and the amount of packets processed from your input callback. Your input callback will be called again for the remaining packets.
3. No data currently available - If there is no data currently available from the input stream, but data remains to be converted, set `ioNumberDataPackets` to zero and return an error (any non-zero value). The error will be propagated back to the caller. If any data was converted, that will also be returned to the caller.

You should also never try to guess exactly how much data to request from your callback to convert an entire data buffer in one call. Codecs are allowed to keep any amount of data buffered internally; therefore, you should request smaller amounts of data. The overhead of requesting a conversion is small compared to the conversion itself. Requesting very large buffers is also bad for cache. It causes every internal buffer to have to be large, or to have to be split up into smaller chunks.

See AudioConverter.h in AudioToolbox.framework for more details regarding the use of the AudioConverter.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-07-21 | Editorial |
| 2004-04-26 | Unspecified content revisions. |
| 2003-10-23 | New document that how to signal the end of data when using AudioConverterFillComplexBuffer to convert audio data. |

