---
title: Compression Sessions - Temporal compression options
apple_id: DTS10003828
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2006-01-12'
source_url: https://developer.apple.com/library/archive/qa/qa1455/_index.html
archived_at: '2026-07-18T02:30:49.317325Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1455

# Compression Sessions - Temporal compression options

## Q:  The Compression Session API has a single quality property, but if temporal compression is enabled, how can the client influence the quality of key frames? Additionally, how does temporal compression interact with the keyframe interval and the frame reordering options?

A: __Temporal Compression and Quality__

The Compression Session APIs have a single compression quality property (`kICMCompressionSessionOptionsPropertyID_Quality`); Modern codecs aim to have consistent quality thereby avoiding jarring effects at keyframe intervals, therefore this single setting governs both the quality of key frames and difference frames produced during a compression operation.

If temporal compression is disabled (`kICMCompressionSessionOptionsPropertyID_AllowTemporalCompression` set to `false`), the quality property represents spatial quality.

If temporal compression is enabled, the quality setting represents a consistent quality setting between key frames and difference frames.

__Temporal Compression, Max Keyframe Interval and Frame Reordering__

If the `AllowTemporalCompression` property is __false__, only key frames will be generated -- every frame will be an __I__ frame. `MaxKeyFrameInterval` is __ignored__.

If `AllowTemporalCompression` is __true__ and `AllowFrameReordering` is __false__, key frames and difference frames will be generated but frames will be encoded in display order: __I__ and __P__ frames may be generated. `MaxKeyFrameInterval` will be __honored__.

If `AllowTemporalCompression` is __true__ and `AllowFrameReordering` is __true__, key frames and difference frames will be generated, and frames may be reordered by the compressor: __I__, __P__ and __B__ frames may be generated. `MaxKeyFrameInterval` will be __honored__.

Setting the `MaxKeyFrameInterval` to 1 (indicating that every frame must be a key frame) also has the effect of disabling temporal compression, since every frame must be a key frame.


```
kICMCompressionSessionOptionsPropertyID_Quality

This property specifies compression quality using a CodecQ value. This value is always used to set the
spatialQuality; if temporal compression is enabled, it is also used to set temporalQuality. The default
quality is codecNormalQuality.

CodecQ, Read/Write.


kICMCompressionSessionOptionsPropertyID_AllowTemporalCompression

This Boolean property enables temporal compression. By default, temporal compression is disabled.

IMPORTANT: If you want temporal compression (P frames and/or B frames) you must set this to true.

Boolean, Read/Write.


kICMCompressionSessionOptionsPropertyID_AllowFrameReordering

This property enables frame reordering. In order to encode B frames, a compressor must reorder frames,
which means that the order in which they will be emitted and stored (the decode order) is different from the
order in which they were presented to the compressor (the display order). By default, frame reordering is
disabled.

IMPORTANT: In order to encode using B frames, you must enable frame reordering.

Boolean, Read/Write.


kICMCompressionSessionOptionsPropertyID_MaxKeyFrameInterval

This property controls the maximum interval between key frames, also known as the key frame rate. Key frames,
also known as sync frames, reset inter-frame dependencies; decoding a key frame is sufficient to prepare a
decompressor for correctly decoding the difference frames that follow. Compressors are allowed to generate key
frames more frequently if this would result in more efficient compression.

The default key frame interval is 0, which indicates that the compressor should choose where to place all key
frames. A key frame interval of 1 indicates that every frame mus be a key frame, 2 indicates that at least
every other frame must be a key frame and so on.

SInt32, Read/Write.
```

- [Video Enhancements - QuickTime 7 Update Guide](https://developer.apple.com/documentation/QuickTime/Conceptual/QT7UpdateGuide/Chapter02/chapter_2_section_7.html)
- [Technical Q&A QA1444, 'Compression Sessions - Configuring codec quality settings'](https://developer.apple.com/qa/qa2005/qa1444.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-01-12 | New document that discusses the temporal compression option as it relates to quality and other compression session options. |

