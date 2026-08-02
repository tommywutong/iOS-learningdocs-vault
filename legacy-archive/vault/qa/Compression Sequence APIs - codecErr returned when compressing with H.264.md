---
title: Compression Sequence APIs - codecErr returned when compressing with H.264
apple_id: DTS10003917
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2006-11-15'
source_url: https://developer.apple.com/library/archive/qa/qa1470/_index.html
archived_at: '2026-07-18T02:30:57.111902Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1470

# Compression Sequence APIs - codecErr returned when compressing with H.264

## Q:  When using Compress Sequence and Standard Compression APIs to encode H.264 video, `SCCompressSequenceFrame` returns `codecErr` (-8960). I have no problems with other codecs such as MPEG-4. Why is H.264 failing?

A: This error is being returned from Standard Compression because the Image Compression Manager Sequence APIs such as `SCCompressSequenceFrame` do not support encoding with the H.264 codec.

The H.264 codec (introduced in QuickTime 7.0) can produce I-frames (independently decodable), P-frames (predicted from a previous I or P-frame) and B-frames (predicted from past and future I or P-frames). H.264 also supports multipass compression (a feature of the codec allowing it to analyzes source data multiple times before the actual encoding process begins).

While the pre-QuickTime 7.0 Image Compression Manager __Sequence__ APIs such as `CompressSequenceBegin`, `CompressSequenceFrame`, `SCCompressSequenceFrame` and so on support any codec producing I-frames or P-frames, they do not support features such as multibuffered compression, multipass compression, frame reordering, or a lookahead window all required by the H.264 codec.

To support H.264. developers must migrate to the new Image Compression Manager __Session__ APIs such as `ICMCompressionSessionCreate`, `ICMCompressionSessionEncodeFrame` and so on.

These new modern APIs support all the features required to compress and decompress H.264 while also supporting all the features required by pre-QuickTime 7.0 codecs.

- [QuickTime 7 Video Enhancements](https://developer.apple.com/documentation/QuickTime/Conceptual/QT7UpdateGuide/Chapter02/chapter_2_section_7.html)
- [Technical Q&A QA1456, 'Compression Sessions - Configuring options using the Standard Compression dialog'](https://developer.apple.com/qa/qa2005/qa1456.html)
- [Technical Q&A QA1444, 'Compression Sessions - Configuring codec quality settings'](https://developer.apple.com/qa/qa2005/qa1444.html)
- [Technical Q&A QA1450, 'Compression Sessions - Enabling multi-pass encoding'](https://developer.apple.com/qa/qa2005/qa1450.html)
- [Technical Q&A QA1455, 'Compression Sessions - Temporal compression options'](https://developer.apple.com/qa/qa2005/qa1455.html)
- [Technical Q&A QA1457, 'Compression Sessions - Multipass encoding and the pass mode flags'](https://developer.apple.com/qa/qa2005/qa1457.html)
- [CaptureAndCompressIPBMovie](https://developer.apple.com/samplecode/CaptureAndCompressIPBMovie/)
- [H.264](http://www.apple.com/quicktime/technologies/h264/)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-11-15 | New document that describes why ICM Compression Sequence APIs cannot be used to encode to H.264 |

