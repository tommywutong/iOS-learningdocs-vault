---
title: Standard Audio - The CodecSpecificSettingsArray and MagicCookie properties
apple_id: DTS10004118
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2009-09-16'
source_url: https://developer.apple.com/library/archive/qa/qa1390/_index.html
archived_at: '2026-07-18T02:30:29.634249Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1390

# Standard Audio - The CodecSpecificSettingsArray and MagicCookie properties

## Q:  I want to use the StdAudio dialog to configure an AudioConverter but I'm not sure what to do with the `kQTSCAudioPropertyID_CodecSpecificSettingsArray` property. What is the corresponding Core Audio Audio Converter property and is this property required?

A: Depending on format selected in the Standard Compression Dialog (see Figure 1), two properties may be available and required to correctly configure a Core Audio AudioConverter and output file (if one is being created) to store the converted audio data.

__Figure 1__  Standard Audio Compression Component Dialog.

!

The first is the __Codec Specific Settings Array__ and the second is the __Magic Cookie__. These two properties are represented by different constants when used with QuickTime and Core Audio APIs however, there is no difference in the property values they represent.

__Table 1__

| Standard Audio (QuickTimeComponents.h) | Audio Converter (AudioConverter.h) |
| kQTSCAudioPropertyID_CodecSpecificSettingsArray | kAudioConverterPropertySettings |

Some (but not all) audio codecs publish settings as a `CFDictionaryRef` describing various parameters that are only specific to the codec being configured.

Additionally, every subconverter used by an Audio Converter can potentially have a `CFDictionaryRef` of settings. For example, when performing a sample rate conversion from PCM to PCM there will be a dictionary exposed by a rate converter subconverter. The Audio Converter used in such a conversion operation will conglomerate the various `CFDictionaryRef`'s exposed by its subconverters in the `CFArrayRef` returned as the `CodecSpecificSettingsArray` property.

When working with Standard Audio, this property is retrieved and set by calling the `QTGetComponentProperty` / `QTSetComponentProperty` API pair using the `kQTSCAudioPropertyID_CodecSpecificSettingsArray` property ID.

When configuring an audio converter, the codec specific settings array retrieved from StdAudio is set by calling `AudioConverterSetProperty` using the `kAudioConverterPropertySettings` property ID.

Applications wishing to provide a custom user interface for audio codecs supporting this property may parse the returned `CFArrayRef` using the Audio Codec Property Settings keys available in `AudioCodec.h`.

When individual values in this array are modified, a client must call `QTSetComponentProperty` and pass in the entire array.

__Table 2__

| Standard Audio (QuickTimeComponents.h) | Audio Converter (AudioConverter.h) |
| kQTSCAudioPropertyID_MagicCookie | kAudioConverterCompressionMagicCookie |

Some (but not all) audio codecs provide a variable sized "blob" of untyped (`void *`) configuration data. This "out of band" data is required to process the stream of encoded audio correctly. This data is considered private to the codec.

When working with Standard Audio this property is retrieved and set by calling the `QTGetComponentProperty` / `QTSetComponentProperty` API pair using the `kQTSCAudioPropertyID_MagicCookie` property ID. You need to allocate a buffer to hold this data, therefore before calling `QTGetComponentProperty` to retrieve the magic cookie a call to `QTGetComponentPropertyInfo` is required to get the size, allocate a buffer of the specified size then call `QTGetComponentProperty` passing in the newly allocated buffer (see Listing 1).

When configuring an audio converter the magic cookie retrieved from StdAudio is set by calling `AudioConverterSetProperty` using the `kAudioConverterCompressionMagicCookie` property ID.

The rules for using the above two properties to configure a Core Audio `AudioConverter` are straight forward:

- When querying StdAudio, applications should always ask for both the `CodecSpecificSettingsArray` and the `MagicCookie`.
- When configuring a Core Audio `AudioConverter`, the `CodecSpecificSettingsArray` should be preferred if both properties are available.
- If the `CodecSpecificSettingsArray` is NOT available use the `MagicCookie` if available.

__Listing 1__  Snippet for getting and setting properties discussed.

```
ComponentInstance ci = 0;
AudioConverterRef myAudioConverter = NULL;

CFArrayRef codecSpecificSettings = NULL;
UInt32 magicCookieSize = 0;
void * magicCookie = NULL;

UInt32 flags;

// open StdAudio (added in QuickTime 7.0)
err = OpenADefaultComponent(StandardCompressionType, StandardCompressionSubTypeAudio, &ci);
if (err) goto bail;

// set some configuration properties before bringing up the dialog
// such as input ASBD, input channel layout and so on
...

// show the dialog (this call blocks until the dialog is finished)
err = SCRequestImageSettings(ci);
if (err) goto bail;

// get the configuration properties specified in the dialog
...

// get the codec specific settings if available
if (noErr == QTGetComponentPropertyInfo(ci,
                                        kQTPropertyClass_SCAudio,
                                        kQTSCAudioPropertyID_CodecSpecificSettingsArray,
                                        NULL, NULL, &flags) && (flags &
                                        kComponentPropertyFlagCanGetNow)) {

    err = QTGetComponentProperty(ci, kQTPropertyClass_SCAudio,
                                     kQTSCAudioPropertyID_CodecSpecificSettingsArray,
                                     sizeof(CFArrayRef), &codecSpecificSettings, NULL);
    if (err) goto bail;
}

// get the magic cookie if available
if (noErr == QTGetComponentPropertyInfo(ci,
                                        kQTPropertyClass_SCAudio,
                                        kQTSCAudioPropertyID_MagicCookie,
                                        NULL, &magicCookieSize, NULL) &&
                                        magicCookieSize) {

    magicCookie = calloc(1, magicCookieSize);
    if (NULL == magicCookie) { err = memFullErr; goto bail; }

    err = QTGetComponentProperty(ci, kQTPropertyClass_SCAudio,
                                     kQTSCAudioPropertyID_MagicCookie,
                                     magicCookieSize, magicCookie, &magicCookieSize);
    if (err) goto bail;
}

// get more properties as appropriate
...

// once we have all the required properties close StdAudio
CloseComponent(ci); ci = 0;

 // create an AudioConverter
err = AudioConverterNew(&myInputASBD, &myOutputASBD, &myAudioConverter);
if (err) goto bail;

// set other Audio Converter properties such as channel layout and so on
...

// a codec that has CodecSpecificSettings may have a MagicCookie
// prefer the CodecSpecificSettingsArray if you have both
if (NULL != codecSpecificSettings) {

    err = AudioConverterSetProperty(myAudioConverter,
                                    kAudioConverterPropertySettings,
                                    sizeof(CFArray),
                                    codecSpecificSettings);
    if (err) goto bail;

    CFRelease(codecSpecificSettings);

} else if (NULL != magicCookie) {
    err = AudioConverterSetProperty(myAudioConverter,
                                    kAudioConverterCompressionMagicCookie,
                                    magicCookieSize,
                                    magicCookie);
    if (err) goto bail;

    // we may need the magic cookie later if we're going to write the data to a file
    // but make sure and remember to free it when we're done!
}

// continue with any other required setup
...

bail:

    if (codecSpecificSettings) CFRelease(codecSpecificSettings);
    if (magicCookie) free(magicCookie);
    if (ci) CloseComponent(ci);
    if (myAudioConverter) AudioConverterDispose(myAudioConverter);

    // clean up as required
    ...

return err;
```


- QuickTime 7.0 Audio Enhancements
- "QuickTime 7.1 Audio Enhancements and Changes"
- QTExtractAndConvertToMovieFile Sample Code
- QTExtractAndConvertToAIFF Sample Code
- [Technical Q&A QA1318, 'How to handle audio data with magic cookie information'](https://developer.apple.com/qa/qa2001/qa1318.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-09-16 | Editorial |
| 2006-11-16 | New document that discusses Core Audio AudioConverter configuration with StdAudio, specifically the CodecSpecificSettingsArray property. |

