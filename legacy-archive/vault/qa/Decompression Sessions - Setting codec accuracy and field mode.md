---
title: Decompression Sessions - Setting codec accuracy and field mode
apple_id: DTS10003837
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2006-01-12'
source_url: https://developer.apple.com/library/archive/qa/qa1460/_index.html
archived_at: '2026-07-18T02:30:52.571175Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1460

# Decompression Sessions - Setting codec accuracy and field mode

## Q:  When transitioning to Decompression Sessions how are codec accuracy and options such as deinterlacing set?

A: When transitioning to Decompression Sessions how are codec accuracy and options such as deinterlacing set?

The older Decompression Sequence APIs had a couple of specific APIs for setting these options. Codec accuracy for example could be set when first creating the sequence by calling `DecompressSequenceBeginS` or after the sequence was created by calling `SetDSequenceAccuracy`. Decompression Sequence flags such as `codecDSequenceDeinterlaceFields` on the other hand would need to be set separately by calling `SetDSequenceFlags`.

The __Decompression Session__ APIs now present a more unified approach for getting and setting options though the use of properties (this is a trend you can see throughout the entire modern QuickTime API).

When creating a Decompression Session, one of the parameters you pass to `ICMDecompressionSessionCreate` is a decompression session options reference (`ICMDecompressionSessionOptionsRef`). This reference is returned by `ICMDecompressionSessionOptionsCreate` and the values of specific properties of a decompression session options object are set by calling `ICMDecompressionSessionOptionsSetProperty`.

ImageCompression.h contains a list of enumerations for decompression session options (`kQTPropertyClass_ICMDecompressionSessionOptions`), for example `kICMDecompressionSessionOptionsPropertyID_FieldMode` for setting special field handling. Field mode options are `UInt32` values described by the typedef `ICMFieldMode`. These modes are then used with the `kICMDecompressionSessionOptionsPropertyID_FieldMode` property.


```
kICMFieldMode_BothFields - Both fields should be decompressed.  kICMFieldMode_TopFieldOnly - Only the top field should be decompressed, producing a half-height image.  kICMFieldMode_BottomFieldOnly - Only the bottom field should be decompressed, producing a                                 half-height image.  kICMFieldMode_DeinterlaceFields - Both fields should be decompressed, and then filtered to reduce                                   interlacing artifacts.
```

ImageCompression.h also contains a list of `CodecQ` values specifying decompression accuracy. These values are used with the `kICMDecompressionSessionOptionsPropertyID_Accuracy` property. If this property hasn't been set in the decompression session options object, the default session accuracy setting is `codecNormalQuality`.

__Listing 1__  Setting some Decompression Session options.

```
ICMDecompressionSessionOptionsRef sessionOptions = NULL; CodecQ codecAccuracy = codecHighQuality; ICMFieldMode fieldMode = kICMFieldMode_DeinterlaceFields;  ...  // create a decompression session options object err = ICMDecompressionSessionOptionsCreate(kCFAllocatorDefault, &sessionOptions); if (noErr == err) {      // set accuracy     ICMDecompressionSessionOptionsSetProperty(sessionOptions,                                               kQTPropertyClass_ICMDecompressionSessionOptions,                                               kICMDecompressionSessionOptionsPropertyID_Accuracy,                                               sizeof(CodecQ),                                               &codecAccuracy);     // set field mode     ICMDecompressionSessionOptionsSetProperty(sessionOptions,                                               kQTPropertyClass_ICMDecompressionSessionOptions,                                               kICMDecompressionSessionOptionsPropertyID_FieldMode,                                               sizeof(ICMFieldMode),                                               &fieldMode); }  ...  // create the decompression session passing in the options object err = ICMDecompressionSessionCreate(kCFAllocatorDefault, ..., sessionOptions, ...); if (err) goto bail;  ...  // the session will retain the options object so you can release it // you can also change options during the session by modifying the options object ICMDecompressionSessionOptionsRelease(sessionOptions);  ...
```


- [ICMDecompressionSessionOptionsSetProperty](https://developer.apple.com/documentation/QuickTime/APIREF/icmdecompressionsessionoptionssetproperty.htm)
- [Video Enhancements](https://developer.apple.com/documentation/QuickTime/Conceptual/QT7UpdateGuide/Chapter02/chapter_2_section_7.html#//apple_ref/doc/uid/TP40001163-CH313-BBCGDBDF)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-01-12 | New document that describes how to set codec accuracy and field mode options when creating a decompression sessions. |

