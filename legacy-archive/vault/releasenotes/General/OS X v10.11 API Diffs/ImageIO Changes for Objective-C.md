---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/ImageIO.html
archived_at: '2026-07-18T02:53:08.219675Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# ImageIO Changes for Objective-C

### ImageIO

#### CGImageDestination.h

Modified [CGImageDestinationAddImage()](https://developer.apple.com/documentation/imageio/1464962-cgimagedestinationaddimage)

|  | Declaration |
| --- | --- |
| From | ``` void CGImageDestinationAddImage (     CGImageDestinationRef idst,     CGImageRef image,     CFDictionaryRef properties ); ``` |
| To | ``` void CGImageDestinationAddImage (     CGImageDestinationRef _Nonnull idst,     CGImageRef _Nonnull image,     CFDictionaryRef _Nullable properties ); ``` |

Modified [CGImageDestinationAddImageAndMetadata()](https://developer.apple.com/documentation/imageio/1465429-cgimagedestinationaddimageandmet)

|  | Declaration |
| --- | --- |
| From | ``` void CGImageDestinationAddImageAndMetadata (     CGImageDestinationRef idst,     CGImageRef image,     CGImageMetadataRef metadata,     CFDictionaryRef options ); ``` |
| To | ``` void CGImageDestinationAddImageAndMetadata (     CGImageDestinationRef _Nonnull idst,     CGImageRef _Nonnull image,     CGImageMetadataRef _Nullable metadata,     CFDictionaryRef _Nullable options ); ``` |

Modified [CGImageDestinationAddImageFromSource()](https://developer.apple.com/documentation/imageio/1465143-cgimagedestinationaddimagefromso)

|  | Declaration |
| --- | --- |
| From | ``` void CGImageDestinationAddImageFromSource (     CGImageDestinationRef idst,     CGImageSourceRef isrc,     size_t index,     CFDictionaryRef properties ); ``` |
| To | ``` void CGImageDestinationAddImageFromSource (     CGImageDestinationRef _Nonnull idst,     CGImageSourceRef _Nonnull isrc,     size_t index,     CFDictionaryRef _Nullable properties ); ``` |

Modified [CGImageDestinationCopyImageSource()](https://developer.apple.com/documentation/imageio/1465189-cgimagedestinationcopyimagesourc)

|  | Declaration |
| --- | --- |
| From | ``` bool CGImageDestinationCopyImageSource (     CGImageDestinationRef idst,     CGImageSourceRef isrc,     CFDictionaryRef options,     CFErrorRef *err ); ``` |
| To | ``` bool CGImageDestinationCopyImageSource (     CGImageDestinationRef _Nonnull idst,     CGImageSourceRef _Nonnull isrc,     CFDictionaryRef _Nullable options,     CFErrorRef  _Nullable * _Nullable err ); ``` |

Modified [CGImageDestinationCopyTypeIdentifiers()](https://developer.apple.com/documentation/imageio/1465316-cgimagedestinationcopytypeidenti)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CGImageDestinationCopyTypeIdentifiers (     void ); ``` |
| To | ``` CFArrayRef _Nonnull CGImageDestinationCopyTypeIdentifiers (     void ); ``` |

Modified [CGImageDestinationCreateWithData()](https://developer.apple.com/documentation/imageio/1465133-cgimagedestinationcreatewithdata)

|  | Declaration |
| --- | --- |
| From | ``` CGImageDestinationRef CGImageDestinationCreateWithData (     CFMutableDataRef data,     CFStringRef type,     size_t count,     CFDictionaryRef options ); ``` |
| To | ``` CGImageDestinationRef _Nullable CGImageDestinationCreateWithData (     CFMutableDataRef _Nonnull data,     CFStringRef _Nonnull type,     size_t count,     CFDictionaryRef _Nullable options ); ``` |

Modified [CGImageDestinationCreateWithDataConsumer()](https://developer.apple.com/documentation/imageio/1465231-cgimagedestinationcreatewithdata)

|  | Declaration |
| --- | --- |
| From | ``` CGImageDestinationRef CGImageDestinationCreateWithDataConsumer (     CGDataConsumerRef consumer,     CFStringRef type,     size_t count,     CFDictionaryRef options ); ``` |
| To | ``` CGImageDestinationRef _Nullable CGImageDestinationCreateWithDataConsumer (     CGDataConsumerRef _Nonnull consumer,     CFStringRef _Nonnull type,     size_t count,     CFDictionaryRef _Nullable options ); ``` |

Modified [CGImageDestinationCreateWithURL()](https://developer.apple.com/documentation/imageio/1465361-cgimagedestinationcreatewithurl)

|  | Declaration |
| --- | --- |
| From | ``` CGImageDestinationRef CGImageDestinationCreateWithURL (     CFURLRef url,     CFStringRef type,     size_t count,     CFDictionaryRef options ); ``` |
| To | ``` CGImageDestinationRef _Nullable CGImageDestinationCreateWithURL (     CFURLRef _Nonnull url,     CFStringRef _Nonnull type,     size_t count,     CFDictionaryRef _Nullable options ); ``` |

Modified [CGImageDestinationFinalize()](https://developer.apple.com/documentation/imageio/1464968-cgimagedestinationfinalize)

|  | Declaration |
| --- | --- |
| From | ``` bool CGImageDestinationFinalize (     CGImageDestinationRef idst ); ``` |
| To | ``` bool CGImageDestinationFinalize (     CGImageDestinationRef _Nonnull idst ); ``` |

Modified [CGImageDestinationSetProperties()](https://developer.apple.com/documentation/imageio/1464919-cgimagedestinationsetproperties)

|  | Declaration |
| --- | --- |
| From | ``` void CGImageDestinationSetProperties (     CGImageDestinationRef idst,     CFDictionaryRef properties ); ``` |
| To | ``` void CGImageDestinationSetProperties (     CGImageDestinationRef _Nonnull idst,     CFDictionaryRef _Nullable properties ); ``` |

#### CGImageMetadata.h

Modified [CGImageMetadataCopyStringValueWithPath()](https://developer.apple.com/documentation/imageio/1465254-cgimagemetadatacopystringvaluewi)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CGImageMetadataCopyStringValueWithPath (     CGImageMetadataRef metadata,     CGImageMetadataTagRef parent,     CFStringRef path ); ``` |
| To | ``` CFStringRef _Nullable CGImageMetadataCopyStringValueWithPath (     CGImageMetadataRef _Nonnull metadata,     CGImageMetadataTagRef _Nullable parent,     CFStringRef _Nonnull path ); ``` |

Modified [CGImageMetadataCopyTagMatchingImageProperty()](https://developer.apple.com/documentation/imageio/1465081-cgimagemetadatacopytagmatchingim)

|  | Declaration |
| --- | --- |
| From | ``` CGImageMetadataTagRef CGImageMetadataCopyTagMatchingImageProperty (     CGImageMetadataRef metadata,     CFStringRef dictionaryName,     CFStringRef propertyName ); ``` |
| To | ``` CGImageMetadataTagRef _Nullable CGImageMetadataCopyTagMatchingImageProperty (     CGImageMetadataRef _Nonnull metadata,     CFStringRef _Nonnull dictionaryName,     CFStringRef _Nonnull propertyName ); ``` |

Modified [CGImageMetadataCopyTags()](https://developer.apple.com/documentation/imageio/1464944-cgimagemetadatacopytags)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CGImageMetadataCopyTags (     CGImageMetadataRef metadata ); ``` |
| To | ``` CFArrayRef _Nullable CGImageMetadataCopyTags (     CGImageMetadataRef _Nonnull metadata ); ``` |

Modified [CGImageMetadataCopyTagWithPath()](https://developer.apple.com/documentation/imageio/1465022-cgimagemetadatacopytagwithpath)

|  | Declaration |
| --- | --- |
| From | ``` CGImageMetadataTagRef CGImageMetadataCopyTagWithPath (     CGImageMetadataRef metadata,     CGImageMetadataTagRef parent,     CFStringRef path ); ``` |
| To | ``` CGImageMetadataTagRef _Nullable CGImageMetadataCopyTagWithPath (     CGImageMetadataRef _Nonnull metadata,     CGImageMetadataTagRef _Nullable parent,     CFStringRef _Nonnull path ); ``` |

Modified [CGImageMetadataCreateFromXMPData()](https://developer.apple.com/documentation/imageio/1465001-cgimagemetadatacreatefromxmpdata)

|  | Declaration |
| --- | --- |
| From | ``` CGImageMetadataRef CGImageMetadataCreateFromXMPData (     CFDataRef data ); ``` |
| To | ``` CGImageMetadataRef _Nullable CGImageMetadataCreateFromXMPData (     CFDataRef _Nonnull data ); ``` |

Modified [CGImageMetadataCreateMutable()](https://developer.apple.com/documentation/imageio/1465356-cgimagemetadatacreatemutable)

|  | Declaration |
| --- | --- |
| From | ``` CGMutableImageMetadataRef CGImageMetadataCreateMutable (     void ); ``` |
| To | ``` CGMutableImageMetadataRef _Nonnull CGImageMetadataCreateMutable (     void ); ``` |

Modified [CGImageMetadataCreateMutableCopy()](https://developer.apple.com/documentation/imageio/1465213-cgimagemetadatacreatemutablecopy)

|  | Declaration |
| --- | --- |
| From | ``` CGMutableImageMetadataRef CGImageMetadataCreateMutableCopy (     CGImageMetadataRef metadata ); ``` |
| To | ``` CGMutableImageMetadataRef _Nullable CGImageMetadataCreateMutableCopy (     CGImageMetadataRef _Nonnull metadata ); ``` |

Modified [CGImageMetadataCreateXMPData()](https://developer.apple.com/documentation/imageio/1465217-cgimagemetadatacreatexmpdata)

|  | Declaration |
| --- | --- |
| From | ``` CFDataRef CGImageMetadataCreateXMPData (     CGImageMetadataRef metadata,     CFDictionaryRef options ); ``` |
| To | ``` CFDataRef _Nullable CGImageMetadataCreateXMPData (     CGImageMetadataRef _Nonnull metadata,     CFDictionaryRef _Nullable options ); ``` |

Modified [CGImageMetadataEnumerateTagsUsingBlock()](https://developer.apple.com/documentation/imageio/1465182-cgimagemetadataenumeratetagsusin)

|  | Declaration |
| --- | --- |
| From | ``` void CGImageMetadataEnumerateTagsUsingBlock (     CGImageMetadataRef metadata,     CFStringRef rootPath,     CFDictionaryRef options,     CGImageMetadataTagBlock block ); ``` |
| To | ``` void CGImageMetadataEnumerateTagsUsingBlock (     CGImageMetadataRef _Nonnull metadata,     CFStringRef _Nullable rootPath,     CFDictionaryRef _Nullable options,     CGImageMetadataTagBlock _Nonnull block ); ``` |

Modified [CGImageMetadataRegisterNamespaceForPrefix()](https://developer.apple.com/documentation/imageio/1465270-cgimagemetadataregisternamespace)

|  | Declaration |
| --- | --- |
| From | ``` bool CGImageMetadataRegisterNamespaceForPrefix (     CGMutableImageMetadataRef metadata,     CFStringRef xmlns,     CFStringRef prefix,     CFErrorRef *err ); ``` |
| To | ``` bool CGImageMetadataRegisterNamespaceForPrefix (     CGMutableImageMetadataRef _Nonnull metadata,     CFStringRef _Nonnull xmlns,     CFStringRef _Nonnull prefix,     CFErrorRef  _Nullable * _Nullable err ); ``` |

Modified [CGImageMetadataRemoveTagWithPath()](https://developer.apple.com/documentation/imageio/1465138-cgimagemetadataremovetagwithpath)

|  | Declaration |
| --- | --- |
| From | ``` bool CGImageMetadataRemoveTagWithPath (     CGMutableImageMetadataRef metadata,     CGImageMetadataTagRef parent,     CFStringRef path ); ``` |
| To | ``` bool CGImageMetadataRemoveTagWithPath (     CGMutableImageMetadataRef _Nonnull metadata,     CGImageMetadataTagRef _Nullable parent,     CFStringRef _Nonnull path ); ``` |

Modified [CGImageMetadataSetTagWithPath()](https://developer.apple.com/documentation/imageio/1465409-cgimagemetadatasettagwithpath)

|  | Declaration |
| --- | --- |
| From | ``` bool CGImageMetadataSetTagWithPath (     CGMutableImageMetadataRef metadata,     CGImageMetadataTagRef parent,     CFStringRef path,     CGImageMetadataTagRef tag ); ``` |
| To | ``` bool CGImageMetadataSetTagWithPath (     CGMutableImageMetadataRef _Nonnull metadata,     CGImageMetadataTagRef _Nullable parent,     CFStringRef _Nonnull path,     CGImageMetadataTagRef _Nonnull tag ); ``` |

Modified [CGImageMetadataSetValueMatchingImageProperty()](https://developer.apple.com/documentation/imageio/1464974-cgimagemetadatasetvaluematchingi)

|  | Declaration |
| --- | --- |
| From | ``` bool CGImageMetadataSetValueMatchingImageProperty (     CGMutableImageMetadataRef metadata,     CFStringRef dictionaryName,     CFStringRef propertyName,     CFTypeRef value ); ``` |
| To | ``` bool CGImageMetadataSetValueMatchingImageProperty (     CGMutableImageMetadataRef _Nonnull metadata,     CFStringRef _Nonnull dictionaryName,     CFStringRef _Nonnull propertyName,     CFTypeRef _Nonnull value ); ``` |

Modified [CGImageMetadataSetValueWithPath()](https://developer.apple.com/documentation/imageio/1465265-cgimagemetadatasetvaluewithpath)

|  | Declaration |
| --- | --- |
| From | ``` bool CGImageMetadataSetValueWithPath (     CGMutableImageMetadataRef metadata,     CGImageMetadataTagRef parent,     CFStringRef path,     CFTypeRef value ); ``` |
| To | ``` bool CGImageMetadataSetValueWithPath (     CGMutableImageMetadataRef _Nonnull metadata,     CGImageMetadataTagRef _Nullable parent,     CFStringRef _Nonnull path,     CFTypeRef _Nonnull value ); ``` |

Modified [CGImageMetadataTagCopyName()](https://developer.apple.com/documentation/imageio/1465092-cgimagemetadatatagcopyname)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CGImageMetadataTagCopyName (     CGImageMetadataTagRef tag ); ``` |
| To | ``` CFStringRef _Nullable CGImageMetadataTagCopyName (     CGImageMetadataTagRef _Nonnull tag ); ``` |

Modified [CGImageMetadataTagCopyNamespace()](https://developer.apple.com/documentation/imageio/1465160-cgimagemetadatatagcopynamespace)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CGImageMetadataTagCopyNamespace (     CGImageMetadataTagRef tag ); ``` |
| To | ``` CFStringRef _Nullable CGImageMetadataTagCopyNamespace (     CGImageMetadataTagRef _Nonnull tag ); ``` |

Modified [CGImageMetadataTagCopyPrefix()](https://developer.apple.com/documentation/imageio/1465378-cgimagemetadatatagcopyprefix)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CGImageMetadataTagCopyPrefix (     CGImageMetadataTagRef tag ); ``` |
| To | ``` CFStringRef _Nullable CGImageMetadataTagCopyPrefix (     CGImageMetadataTagRef _Nonnull tag ); ``` |

Modified [CGImageMetadataTagCopyQualifiers()](https://developer.apple.com/documentation/imageio/1465094-cgimagemetadatatagcopyqualifiers)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CGImageMetadataTagCopyQualifiers (     CGImageMetadataTagRef tag ); ``` |
| To | ``` CFArrayRef _Nullable CGImageMetadataTagCopyQualifiers (     CGImageMetadataTagRef _Nonnull tag ); ``` |

Modified [CGImageMetadataTagCopyValue()](https://developer.apple.com/documentation/imageio/1464942-cgimagemetadatatagcopyvalue)

|  | Declaration |
| --- | --- |
| From | ``` CFTypeRef CGImageMetadataTagCopyValue (     CGImageMetadataTagRef tag ); ``` |
| To | ``` CFTypeRef _Nullable CGImageMetadataTagCopyValue (     CGImageMetadataTagRef _Nonnull tag ); ``` |

Modified [CGImageMetadataTagCreate()](https://developer.apple.com/documentation/imageio/1465060-cgimagemetadatatagcreate)

|  | Declaration |
| --- | --- |
| From | ``` CGImageMetadataTagRef CGImageMetadataTagCreate (     CFStringRef xmlns,     CFStringRef prefix,     CFStringRef name,     CGImageMetadataType type,     CFTypeRef value ); ``` |
| To | ``` CGImageMetadataTagRef _Nullable CGImageMetadataTagCreate (     CFStringRef _Nonnull xmlns,     CFStringRef _Nullable prefix,     CFStringRef _Nonnull name,     CGImageMetadataType type,     CFTypeRef _Nonnull value ); ``` |

Modified [CGImageMetadataTagGetType()](https://developer.apple.com/documentation/imageio/1465337-cgimagemetadatataggettype)

|  | Declaration |
| --- | --- |
| From | ``` CGImageMetadataType CGImageMetadataTagGetType (     CGImageMetadataTagRef tag ); ``` |
| To | ``` CGImageMetadataType CGImageMetadataTagGetType (     CGImageMetadataTagRef _Nonnull tag ); ``` |

#### CGImageProperties.h

Added #def IMAGEIO_PNG_ALL_FILTERSAdded [#def IMAGEIO_PNG_FILTER_AVG](https://developer.apple.com/documentation/imageio/imageio_png_filter_avg)Added [#def IMAGEIO_PNG_FILTER_NONE](https://developer.apple.com/documentation/imageio/imageio_png_filter_none)Added [#def IMAGEIO_PNG_FILTER_PAETH](https://developer.apple.com/documentation/imageio/imageio_png_filter_paeth)Added [#def IMAGEIO_PNG_FILTER_SUB](https://developer.apple.com/documentation/imageio/imageio_png_filter_sub)Added [#def IMAGEIO_PNG_FILTER_UP](https://developer.apple.com/documentation/imageio/imageio_png_filter_up)Added [#def IMAGEIO_PNG_NO_FILTERS](https://developer.apple.com/documentation/imageio/imageio_png_no_filters)Added [kCGImagePropertyExifSubsecTimeOriginal](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifsubsectimeoriginal)Added [kCGImagePropertyPNGCompressionFilter](https://developer.apple.com/documentation/imageio/kcgimagepropertypngcompressionfilter)Added [kCGImagePropertyTIFFTileLength](https://developer.apple.com/documentation/imageio/kcgimagepropertytifftilelength)Added [kCGImagePropertyTIFFTileWidth](https://developer.apple.com/documentation/imageio/kcgimagepropertytifftilewidth)

#### CGImageSource.h

Added [kCGImageSourceSubsampleFactor](https://developer.apple.com/documentation/imageio/kcgimagesourcesubsamplefactor)Modified [CGImageSourceCopyMetadataAtIndex()](https://developer.apple.com/documentation/imageio/1465476-cgimagesourcecopymetadataatindex)

|  | Declaration |
| --- | --- |
| From | ``` CGImageMetadataRef CGImageSourceCopyMetadataAtIndex (     CGImageSourceRef isrc,     size_t index,     CFDictionaryRef options ); ``` |
| To | ``` CGImageMetadataRef _Nullable CGImageSourceCopyMetadataAtIndex (     CGImageSourceRef _Nonnull isrc,     size_t index,     CFDictionaryRef _Nullable options ); ``` |

Modified [CGImageSourceCopyProperties()](https://developer.apple.com/documentation/imageio/1465443-cgimagesourcecopyproperties)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CGImageSourceCopyProperties (     CGImageSourceRef isrc,     CFDictionaryRef options ); ``` |
| To | ``` CFDictionaryRef _Nullable CGImageSourceCopyProperties (     CGImageSourceRef _Nonnull isrc,     CFDictionaryRef _Nullable options ); ``` |

Modified [CGImageSourceCopyPropertiesAtIndex()](https://developer.apple.com/documentation/imageio/1465363-cgimagesourcecopypropertiesatind)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CGImageSourceCopyPropertiesAtIndex (     CGImageSourceRef isrc,     size_t index,     CFDictionaryRef options ); ``` |
| To | ``` CFDictionaryRef _Nullable CGImageSourceCopyPropertiesAtIndex (     CGImageSourceRef _Nonnull isrc,     size_t index,     CFDictionaryRef _Nullable options ); ``` |

Modified [CGImageSourceCopyTypeIdentifiers()](https://developer.apple.com/documentation/imageio/1465383-cgimagesourcecopytypeidentifiers)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CGImageSourceCopyTypeIdentifiers (     void ); ``` |
| To | ``` CFArrayRef _Nonnull CGImageSourceCopyTypeIdentifiers (     void ); ``` |

Modified [CGImageSourceCreateImageAtIndex()](https://developer.apple.com/documentation/imageio/1465011-cgimagesourcecreateimageatindex)

|  | Declaration |
| --- | --- |
| From | ``` CGImageRef CGImageSourceCreateImageAtIndex (     CGImageSourceRef isrc,     size_t index,     CFDictionaryRef options ); ``` |
| To | ``` CGImageRef _Nullable CGImageSourceCreateImageAtIndex (     CGImageSourceRef _Nonnull isrc,     size_t index,     CFDictionaryRef _Nullable options ); ``` |

Modified [CGImageSourceCreateIncremental()](https://developer.apple.com/documentation/imageio/1465151-cgimagesourcecreateincremental)

|  | Declaration |
| --- | --- |
| From | ``` CGImageSourceRef CGImageSourceCreateIncremental (     CFDictionaryRef options ); ``` |
| To | ``` CGImageSourceRef _Nonnull CGImageSourceCreateIncremental (     CFDictionaryRef _Nullable options ); ``` |

Modified [CGImageSourceCreateThumbnailAtIndex()](https://developer.apple.com/documentation/imageio/1465099-cgimagesourcecreatethumbnailatin)

|  | Declaration |
| --- | --- |
| From | ``` CGImageRef CGImageSourceCreateThumbnailAtIndex (     CGImageSourceRef isrc,     size_t index,     CFDictionaryRef options ); ``` |
| To | ``` CGImageRef _Nullable CGImageSourceCreateThumbnailAtIndex (     CGImageSourceRef _Nonnull isrc,     size_t index,     CFDictionaryRef _Nullable options ); ``` |

Modified [CGImageSourceCreateWithData()](https://developer.apple.com/documentation/imageio/1465073-cgimagesourcecreatewithdata)

|  | Declaration |
| --- | --- |
| From | ``` CGImageSourceRef CGImageSourceCreateWithData (     CFDataRef data,     CFDictionaryRef options ); ``` |
| To | ``` CGImageSourceRef _Nullable CGImageSourceCreateWithData (     CFDataRef _Nonnull data,     CFDictionaryRef _Nullable options ); ``` |

Modified [CGImageSourceCreateWithDataProvider()](https://developer.apple.com/documentation/imageio/1465285-cgimagesourcecreatewithdataprovi)

|  | Declaration |
| --- | --- |
| From | ``` CGImageSourceRef CGImageSourceCreateWithDataProvider (     CGDataProviderRef provider,     CFDictionaryRef options ); ``` |
| To | ``` CGImageSourceRef _Nullable CGImageSourceCreateWithDataProvider (     CGDataProviderRef _Nonnull provider,     CFDictionaryRef _Nullable options ); ``` |

Modified [CGImageSourceCreateWithURL()](https://developer.apple.com/documentation/imageio/1465262-cgimagesourcecreatewithurl)

|  | Declaration |
| --- | --- |
| From | ``` CGImageSourceRef CGImageSourceCreateWithURL (     CFURLRef url,     CFDictionaryRef options ); ``` |
| To | ``` CGImageSourceRef _Nullable CGImageSourceCreateWithURL (     CFURLRef _Nonnull url,     CFDictionaryRef _Nullable options ); ``` |

Modified [CGImageSourceGetCount()](https://developer.apple.com/documentation/imageio/1465029-cgimagesourcegetcount)

|  | Declaration |
| --- | --- |
| From | ``` size_t CGImageSourceGetCount (     CGImageSourceRef isrc ); ``` |
| To | ``` size_t CGImageSourceGetCount (     CGImageSourceRef _Nonnull isrc ); ``` |

Modified [CGImageSourceGetStatus()](https://developer.apple.com/documentation/imageio/1465322-cgimagesourcegetstatus)

|  | Declaration |
| --- | --- |
| From | ``` CGImageSourceStatus CGImageSourceGetStatus (     CGImageSourceRef isrc ); ``` |
| To | ``` CGImageSourceStatus CGImageSourceGetStatus (     CGImageSourceRef _Nonnull isrc ); ``` |

Modified [CGImageSourceGetStatusAtIndex()](https://developer.apple.com/documentation/imageio/1465401-cgimagesourcegetstatusatindex)

|  | Declaration |
| --- | --- |
| From | ``` CGImageSourceStatus CGImageSourceGetStatusAtIndex (     CGImageSourceRef isrc,     size_t index ); ``` |
| To | ``` CGImageSourceStatus CGImageSourceGetStatusAtIndex (     CGImageSourceRef _Nonnull isrc,     size_t index ); ``` |

Modified [CGImageSourceGetType()](https://developer.apple.com/documentation/imageio/1465448-cgimagesourcegettype)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CGImageSourceGetType (     CGImageSourceRef isrc ); ``` |
| To | ``` CFStringRef _Nullable CGImageSourceGetType (     CGImageSourceRef _Nonnull isrc ); ``` |

Modified [CGImageSourceRemoveCacheAtIndex()](https://developer.apple.com/documentation/imageio/1465077-cgimagesourceremovecacheatindex)

|  | Declaration |
| --- | --- |
| From | ``` void CGImageSourceRemoveCacheAtIndex (     CGImageSourceRef isrc,     size_t index ); ``` |
| To | ``` void CGImageSourceRemoveCacheAtIndex (     CGImageSourceRef _Nonnull isrc,     size_t index ); ``` |

Modified [CGImageSourceUpdateData()](https://developer.apple.com/documentation/imageio/1465473-cgimagesourceupdatedata)

|  | Declaration |
| --- | --- |
| From | ``` void CGImageSourceUpdateData (     CGImageSourceRef isrc,     CFDataRef data,     bool final ); ``` |
| To | ``` void CGImageSourceUpdateData (     CGImageSourceRef _Nonnull isrc,     CFDataRef _Nonnull data,     bool final ); ``` |

Modified [CGImageSourceUpdateDataProvider()](https://developer.apple.com/documentation/imageio/1465175-cgimagesourceupdatedataprovider)

|  | Declaration |
| --- | --- |
| From | ``` void CGImageSourceUpdateDataProvider (     CGImageSourceRef isrc,     CGDataProviderRef provider,     bool final ); ``` |
| To | ``` void CGImageSourceUpdateDataProvider (     CGImageSourceRef _Nonnull isrc,     CGDataProviderRef _Nonnull provider,     bool final ); ``` |

#### ImageIOBase.h

Added #def IIO_BRIDGED_TYPE

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
