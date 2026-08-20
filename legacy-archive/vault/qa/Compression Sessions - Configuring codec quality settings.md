---
title: Compression Sessions - Configuring codec quality settings
apple_id: DTS10003796
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2005-10-17'
source_url: https://developer.apple.com/library/archive/qa/qa1444/_index.html
archived_at: '2026-07-18T02:30:48.861668Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1444

# Compression Sessions - Configuring codec quality settings

## Q:  When migrating from Compression Sequences to Compression Sessions how are the Codec Quality settings for Spatial and Temporal quality set for the Session? Can these be changed per frame?

A: When using `CompressSequenceBegin`, the appropriate `CodecQ` settings for spatial and temporal quality are passed into the API and can be changed for the Sequence by calling `SetCSequenceQuality`. Passing in 0 for `temporalQuality` prevents the compressor from applying any temporal compression to the sequence.

The setup for __Compression Sessions__ is a little different. You first create and configure a `ICMCompressionSessionOptions` object using the `ICMCompressionSessionOptionsCreate` API, then pass in this configuration to `ICMCompressionSessionCreate`.

Configuration of spatial quality for a Compression Session is done using the `kICMCompressionSessionOptionsPropertyID_Quality` property along with the `ICMCompressionSessionOptionsSetProperty` API.

Temporal compression can be enabled or disabled for a session by calling `ICMCompressionSessionOptionsSetAllowTemporalCompression` and passing in either `true` or `false`. See Listing 1.

If temporal compression is enabled, the `kICMCompressionSessionOptionsPropertyID_Quality` property is also used to set `temporalQuality`.

__Listing 1__  Configuring Session Options

```
CodecQ compressionQuality = codecNormalQuality;
Boolean allowTemporalCompression = true;
ICMCompressionSessionOptionsRef sessionOptions = NULL;
ICMCompressionSessionRef session = NULL;

...

// Create a compression session options token (ICMCompressionSessionOptionsRef).
err = ICMCompressionSessionOptionsCreate(kCFAllocatorDefault, &sessionOptions);
if(err || NULL == sessionOptions) goto bail;

// Set temporal compression on/off.
err = ICMCompressionSessionOptionsSetAllowTemporalCompression(sessionOptions,
                                                    allowTemporalCompression);
if (err) goto bail;

// Set the compression quality.
// kICMCompressionSessionOptionsPropertyID_Quality property is always used to
// set the spatialQuality; if temporal compression is enabled, it is also used
// to set temporalQuality.
// The default quality is codecNormalQuality.
err = ICMCompressionSessionOptionsSetProperty(sessionOptions,
                                kQTPropertyClass_ICMCompressionSessionOptions,
                                kICMCompressionSessionOptionsPropertyID_Quality,
                                sizeof(compressionQuality),
                                &compressionQuality );
if (err) goto bail;

...

err = ICMCompressionSessionCreate(kCFAllocatorDefault, ..., &session);
if (err) goto bail;

// Encode some frames
...

bail:
    // Both of these release calls are NULL safe, so we don't have to do an extra check.
    ICMCompressionSessionOptionsRelease(sessionOptions);
    ICMCompressionSessionRelease(session);
...
```


- [QT 7 Video Enhancements](https://developer.apple.com/documentation/QuickTime/Conceptual/QT7UpdateGuide/Chapter02/chapter_2_section_7.html)
- [ICMCompressionSessionOptionsSetAllowTemporalCompression](https://developer.apple.com/documentation/QuickTime/APIREF/icmcompressionsessionoptionssetallowtemporalcompression.htm)
- [ICMCompressionSessionOptionsSetAllowFrameReordering](https://developer.apple.com/documentation/QuickTime/APIREF/icmcompressionsessionoptionssetallowframereordering.htm)
- [ICMCompressionSessionOptionsSetAllowFrameTimeChanges](https://developer.apple.com/documentation/QuickTime/APIREF/icmcompressionsessionoptionssetallowframetimechanges.htm)
- [ICMCompressionSessionOptionsCreate](https://developer.apple.com/documentation/QuickTime/APIREF/icmcompressionsessionoptionscreate.htm)
- [ICMCompressionSessionOptionsSetProperty](https://developer.apple.com/documentation/QuickTime/APIREF/icmcompressionsessionoptionssetproperty.htm)
- [ICMCompressionSessionCreate](https://developer.apple.com/documentation/QuickTime/APIREF/icmcompressionsessioncreate.htm)
- [ICM Property IDs](https://developer.apple.com/documentation/QuickTime/APIREF/ICMPropertyIDs.htm)

See `ImageCompression.h` for additional property information.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-10-17 | New document that discusses how to set encoding quality for a Compression Sequence |

