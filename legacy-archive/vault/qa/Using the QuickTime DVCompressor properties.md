---
title: Using the QuickTime DVCompressor properties
apple_id: DTS10003743
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2005-10-04'
source_url: https://developer.apple.com/library/archive/qa/qa1438/_index.html
archived_at: '2026-07-18T02:30:44.235254Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1438

# Using the QuickTime DVCompressor properties

## Q:  Can the `kQTPropertyClass_DVCompressor` properties only be used with a DV codec or do they also work with the DV export component?Additionally, what do the `kDVCompressorPropertyID_ProgressiveScan` and `kDVCompressorPropertyID_AspectRatio16x9` properties actually set?

A: The `kQTPropertyClass_DVCompressor` properties ( `kDVCompressorPropertyID_ProgressiveScan` and `kDVCompressorPropertyID_AspectRatio16x9` ) are supported by both the DV25 and DV50 compressor components as well as the DV export component.

These properties are supported via `QTGetComponentPropertyInfo`, `QTGetComponentProperty` and `QTSetComponentProperty` APIs. They are also part of the serialized DV compressor settings stored and restored with `ImageCodecGetSettings` and `ImageCodecSetSettings`.

These DVCompressor class properties cause the corresponding flags to be set for the encoded DV frames; Frames marked as progressive-scan when `kDVCompressorPropertyID_ProgressiveScan` is set, and frames marked as having a 16:9 picture aspect ratio when `kDVCompressorPropertyID_AspectRatio16x9` is set.

When used with the compressor components, these DVCompressor properties will also add the appropriate Field/Frame Information (`'fiel'`), Clean Aperture (`'clap'`) and Pixel Aspect Ratio (`'pasp'`) Image Description Extensions to describe the content.

To retrieve these properties from Image Descriptions without calling `GetImageDescriptionExtension` directly, use the [ICMImageDescriptionGetProperty](https://developer.apple.com/documentation/QuickTime/APIREF/icmimagedescriptiongetproperty.htm) API introduced in QuickTime 7.

[Dumpster version 7.0.1](https://developer.apple.com/quicktime/quicktimeintro/tools/index.html) will display several of these Image Description Extensions, including:

Field/Frame Information - `'fiel'`

Clean Aperture - `'clap'`

Pixel Aspect Ratio - `'pasp'`

Color parameters - `'colr'`

__Listing 1__  Setting DVCompressor properties on the DV Export Component.

```
// Set the ProgressiveScan and AspectRatio16x9 properties for the DV Export Component
//
// inProgressiveScan - if set to true, the compressed frames will be marked as
//                     progressive-scan. If set to false the frames will be marked as
//                     interlaced.
// inAspectRatio16x9 - if set to true, the compressor will use a 16:9 picture
//                     aspect ratio. If set to false, the compressor will use the
//                     default 4:3 picture aspect ratio.
OSStatus SetDVExportProperties(MovieExportComponent inDVExporter,
                               Boolean inProgressiveScan,
                               Boolean inAspectRatio16x9)
{
    OSStatus status;

    if (NULL == inDVExporter) return paramErr;

    // set the properties we want
    status = QTSetComponentProperty(inDVExporter, // DV export component instance
                                    kQTPropertyClass_DVCompressor,           // property class
                                    kDVCompressorPropertyID_ProgressiveScan, // property
                                    sizeof(inProgressiveScan),  // size
                                    &inProgressiveScan); // value
    if (status) goto bail;

    status = QTSetComponentProperty(inDVExporter, // DV export component instance
                                    kQTPropertyClass_DVCompressor,           // property class
                                    kDVCompressorPropertyID_AspectRatio16x9, // property
                                    sizeof(inAspectRatio16x9), // size
                                    &inAspectRatio16x9); // value

bail:
    return status;
}
```

The Image Compression Manager Session APIs allow attaching a serialized settings handle to the `ICMCompressionSessionOptions` object. This allows applications to use custom codec settings without the need to specifically open a compressor instance, configure it, use it throughout the compression operation and close it when done as was required by the older Compression Sequence API.

__Listing 2__  Setting DVCompressor properties for a ICM Compression Session.

```
// Configure the ProgressiveScan and AspectRatio16x9 properties for a DV compression session.
//
// inCompressionSessionOptions - a reference to a compression session options object
//                               created by calling ICMCompressionSessionOptionsCreate
// inCodecType - a DV25 or DV50 codec OSType, one of: kDVCNTSCCodecType
//                                                    kDVCPALCodecType
//                                                    kDVCProPALCodecType
//                                                    kDVCPro50NTSCCodecType
//                                                    kDVCPro50PALCodecType
// inProgressiveScan - if set to true, the compressed frames will be marked as
//                     progressive-scan. If set to false the frames will be marked as
//                     interlaced
// inAspectRatio16x9 - if set to true, the compressor will use a 16:9 picture
//                     aspect ratio. If set to false, the compressor will use the
//                     default 4:3 picture aspect ratio.
OSStatus ConfigureDVCodecCompressionSessionOptions(
                            ICMCompressionSessionOptionsRef inCompressionSessionOptions,
                            OSType inCodecType,
                            Boolean inProgressiveScan,
                            Boolean inAspectRatio16x9)
{

    OSStatus status;

    if (NULL == inCompressionSessionOptions || 0 == inCodecType ) return paramErr;

    ComponentInstance dvCodecInstance = 0;
    Handle hCodecSettings = NewHandle(0);

    status = OpenADefaultComponent(compressorComponentType, inCodecType, &dvCodecInstance);
    if (status) goto bail;

    // set the properties we want
    status = QTSetComponentProperty(dvCodecInstance, // DV codec component instance
                                    kQTPropertyClass_DVCompressor, // property class
                                    kDVCompressorPropertyID_ProgressiveScan, // property
                                    sizeof(inProgressiveScan),  // size
                                    &inProgressiveScan); // value
    if (status) goto bail;

    status = QTSetComponentProperty(dvCodecInstance, // DV codec component instance
                                    kQTPropertyClass_DVCompressor, // property class
                                    kDVCompressorPropertyID_AspectRatio16x9, // property
                                    sizeof(inAspectRatio16x9), // size
                                    &inAspectRatio16x9); // value

    // once we've set the codec properties, ask for the codec's specific settings
    status = ImageCodecGetSettings(dvCodecInstance, hCodecSettings);
    if (status) goto bail;

    // now set these codec specific settings on our compression session
    status = ICMCompressionSessionOptionsSetProperty(
        inCompressionSessionOptions, // compression session options object reference
        kQTPropertyClass_ICMCompressionSessionOptions,              // property class
        kICMCompressionSessionOptionsPropertyID_CompressorSettings, // property
        sizeof(hCodecSettings), // size
        &hCodecSettings); // codec settings

    if (status) goto bail;

bail:
    if (dvCodecInstance) CloseComponent(dvCodecInstance);
    DisposeHandle(hCodecSettings);

    return status;
}
```


__Listing 3__  Retrieving the Pixel Aspect Ratio Image Description Extension.

```
PixelAspectRatioImageDescriptionExtension pixelAspectRatio;
OSStatus status;
.
.
.
status = ICMImageDescriptionGetProperty(hSourceImageDescription, // image description
                                        kQTPropertyClass_ImageDescription, // class
                                        // 'pasp' image description extention property
                                        kICMImageDescriptionPropertyID_PixelAspectRatio,
                                        sizeof(pixelAspectRatio), // size
                                        &pixelAspectRatio,        // returned value
                                        NULL); // byte count
.
.
.

// Other Image Description Extentions are retrieved in a similar fashion, see
// ImageCompression.h for more details.
//
// Use kICMImageDescriptionPropertyID_FieldInfo to retrieve information about the number
// and order of fields, if available.
//
//     kICMImageDescriptionPropertyID_FieldInfo = 'fiel'
//         FieldInfoImageDescriptionExtension2
//
// Use kICMImageDescriptionPropertyID_CleanAperture to retrieve information describing
// the clean aperture. If not specified explicitly in the image description, a default
// clean aperture (full encoded width and height) will be returned.
//
//     kICMImageDescriptionPropertyID_CleanAperture = 'clap'
//         Native-endian CleanApertureImageDescriptionExtension
//
// Use kICMImageDescriptionPropertyID_PixelAspectRatio to retrieve information
// describing the pixel aspect ratio. If not specified explicitly in the image
// description, a square (1:1) pixel aspect ratio will be returned.
//
//    kICMImageDescriptionPropertyID_PixelAspectRatio = 'pasp'
//        Native-endian PixelAspectRatioImageDescriptionExtension
//
// Use kICMImageDescriptionPropertyID_NCLCColorInfo to retrieve color information if available, in the
// NCLCColorInfoImageDescriptionExtension format.
//
//    kICMImageDescriptionPropertyID_NCLCColorInfo = 'nclc'
//        Native-endian NCLCColorInfoImageDescriptionExtension
```


[QuickTime 7 Update Guide](https://developer.apple.com/documentation/QuickTime/Conceptual/QT7UpdateGuide/index.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-10-04 | Updated |
| 2005-07-05 | New document that describes the function of the DVCompressor class component properties. |

