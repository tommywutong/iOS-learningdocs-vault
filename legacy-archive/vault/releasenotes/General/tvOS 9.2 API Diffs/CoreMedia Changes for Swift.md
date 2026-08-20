---
title: tvOS 9.2 API Diffs
apple_id: TP40016673
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS92APIDiffs/Swift/CoreMedia.html
archived_at: '2026-07-18T02:58:05.533804Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 9.2 API Diffs](tvOS%209.1%20to%209.2%20API%20Differences.md)


# CoreMedia Changes for Swift

### CoreMedia

Removed kCMFormatDescriptionYCbCrMatrix_DCI_P3Removed kCMFormatDescriptionYCbCrMatrix_P3_D65Added [kCMBufferQueueTrigger_WhenDurationBecomesGreaterThanOrEqualToAndBufferCountBecomesGreaterThan](https://developer.apple.com/documentation/coremedia/kcmbufferqueuetrigger_whendurationbecomesgreaterthanorequaltoandbuffercountbecomesgreaterthan)Added [kCMMetadataKeySpace_HLSDateRange](https://developer.apple.com/documentation/coremedia/kcmmetadatakeyspace_hlsdaterange)Modified [CMBlockBuffer](https://developer.apple.com/documentation/coremedia/cmblockbufferref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CMBlockBufferRef | ``` typealias CMBlockBufferRef = CMBlockBuffer ``` |
| To | CMBlockBuffer | ``` class CMBlockBuffer { } ``` |

Modified [CMBufferQueue](https://developer.apple.com/documentation/coremedia/cmbufferqueueref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CMBufferQueueRef | ``` typealias CMBufferQueueRef = CMBufferQueue ``` |
| To | CMBufferQueue | ``` class CMBufferQueue { } ``` |

Modified [CMClock](https://developer.apple.com/documentation/coremedia/cmclock)

|  | Name | Declaration |
| --- | --- | --- |
| From | CMClockRef | ``` typealias CMClockRef = CMClock ``` |
| To | CMClock | ``` class CMClock { } ``` |

Modified [CMFormatDescription](https://developer.apple.com/documentation/coremedia/cmformatdescription)

|  | Name | Declaration |
| --- | --- | --- |
| From | CMFormatDescriptionRef | ``` typealias CMFormatDescriptionRef = CMFormatDescription ``` |
| To | CMFormatDescription | ``` class CMFormatDescription { } ``` |

Modified [CMMemoryPool](https://developer.apple.com/documentation/coremedia/cmmemorypoolref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CMMemoryPoolRef | ``` typealias CMMemoryPoolRef = CMMemoryPool ``` |
| To | CMMemoryPool | ``` class CMMemoryPool { } ``` |

Modified [CMSampleBuffer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer)

|  | Name | Declaration |
| --- | --- | --- |
| From | CMSampleBufferRef | ``` typealias CMSampleBufferRef = CMSampleBuffer ``` |
| To | CMSampleBuffer | ``` class CMSampleBuffer { } ``` |

Modified [CMSimpleQueue](https://developer.apple.com/documentation/coremedia/cmsimplequeue)

|  | Name | Declaration |
| --- | --- | --- |
| From | CMSimpleQueueRef | ``` typealias CMSimpleQueueRef = CMSimpleQueue ``` |
| To | CMSimpleQueue | ``` class CMSimpleQueue { } ``` |

Modified [CMTimebase](https://developer.apple.com/documentation/coremedia/cmtimebaseref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CMTimebaseRef | ``` typealias CMTimebaseRef = CMTimebase ``` |
| To | CMTimebase | ``` class CMTimebase { } ``` |

Modified [CMAttachmentBearer](https://developer.apple.com/documentation/coremedia/cmattachmentbearer)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMAttachmentBearerRef = CMAttachmentBearer ``` |
| To | ``` typealias CMAttachmentBearer = CFTypeRef ``` |

Modified [CMBuffer](https://developer.apple.com/documentation/coremedia/cmbufferref)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMBufferRef = CMBuffer ``` |
| To | ``` typealias CMBuffer = CFTypeRef ``` |

Modified [CMClosedCaptionFormatDescription](https://developer.apple.com/documentation/coremedia/cmclosedcaptionformatdescriptionref)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMClosedCaptionFormatDescriptionRef = CMClosedCaptionFormatDescription ``` |
| To | ``` typealias CMClosedCaptionFormatDescription = CMFormatDescriptionRef ``` |

Modified [CMTextFormatDescription](https://developer.apple.com/documentation/coremedia/cmtextformatdescription)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMTextFormatDescriptionRef = CMTextFormatDescription ``` |
| To | ``` typealias CMTextFormatDescription = CMFormatDescriptionRef ``` |

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
