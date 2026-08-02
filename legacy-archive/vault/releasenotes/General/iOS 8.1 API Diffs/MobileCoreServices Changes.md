---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/MobileCoreServices.html
archived_at: '2026-07-18T02:56:14.829452Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# MobileCoreServices Changes

## MobileCoreServices

Modified UTTypeConformsTo(CFString!, CFString!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UTTypeCopyDeclaration(CFString!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UTTypeCopyDeclaringBundleURL(CFString!) -> Unmanaged<CFURL>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UTTypeCopyDescription(CFString!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UTTypeCopyPreferredTagWithClass(CFString!, CFString!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UTTypeCreateAllIdentifiersForTag(CFString!, CFString!, CFString!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UTTypeCreatePreferredIdentifierForTag(CFString!, CFString!, CFString!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UTTypeEqual(CFString!, CFString!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTExportedTypeDeclarationsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTImportedTypeDeclarationsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTagClassFilenameExtension

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTagClassMIMEType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeAliasFile

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeAliasRecord

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeAppleICNS

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeAppleProtectedMPEG4Audio

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeApplication

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeApplicationBundle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeApplicationFile

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeArchive

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeAudio

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeAudiovisualContent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeBMP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeBundle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeCHeader

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeCPlusPlusHeader

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeCPlusPlusSource

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeCSource

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeCompositeContent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeConformsToKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeContact

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeContent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeData

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeDescriptionKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeDirectory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeDiskImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeFileURL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeFlatRTFD

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeFolder

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeFramework

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeGIF

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeHTML

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeICO

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeIconFileKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeIdentifierKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeInkText

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeItem

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeJPEG

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeJPEG2000

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeJavaSource

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeMP3

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeMPEG

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeMPEG4

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeMPEG4Audio

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeMessage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeMountPoint

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeMovie

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeObjectiveCPlusPlusSource

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeObjectiveCSource

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypePDF

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypePICT

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypePNG

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypePackage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypePlainText

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeQuickTimeImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeQuickTimeMovie

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeRTF

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeRTFD

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeReferenceURLKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeResolvable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeSourceCode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeSymLink

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeTIFF

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeTXNTextAndMultimediaData

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeTagSpecificationKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeText

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeURL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeUTF16ExternalPlainText

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeUTF16PlainText

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeUTF8PlainText

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeVCard

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeVersionKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeVideo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeVolume

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeWebArchive

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kUTTypeXML

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

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
