---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/ImageIO.html
archived_at: '2026-07-18T02:56:26.290871Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# ImageIO Changes

## ImageIO

Modified CGImageDestinationAddImageFromSource(CGImageDestination!, CGImageSource!, Int, CFDictionary!)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageDestinationAddImageFromSource(_ idst: CGImageDestination!, _ isrc: CGImageSource!, _ index: UInt, _ properties: CFDictionary!) ``` |
| To | ``` func CGImageDestinationAddImageFromSource(_ idst: CGImageDestination!, _ isrc: CGImageSource!, _ index: Int, _ properties: CFDictionary!) ``` |

Modified CGImageDestinationCreateWithData(CFMutableData!, CFString!, Int, CFDictionary!) -> CGImageDestination!

|  | Declaration |
| --- | --- |
| From | ``` func CGImageDestinationCreateWithData(_ data: CFMutableData!, _ type: CFString!, _ count: UInt, _ options: CFDictionary!) -> CGImageDestination! ``` |
| To | ``` func CGImageDestinationCreateWithData(_ data: CFMutableData!, _ type: CFString!, _ count: Int, _ options: CFDictionary!) -> CGImageDestination! ``` |

Modified CGImageDestinationCreateWithDataConsumer(CGDataConsumer!, CFString!, Int, CFDictionary!) -> CGImageDestination!

|  | Declaration |
| --- | --- |
| From | ``` func CGImageDestinationCreateWithDataConsumer(_ consumer: CGDataConsumer!, _ type: CFString!, _ count: UInt, _ options: CFDictionary!) -> CGImageDestination! ``` |
| To | ``` func CGImageDestinationCreateWithDataConsumer(_ consumer: CGDataConsumer!, _ type: CFString!, _ count: Int, _ options: CFDictionary!) -> CGImageDestination! ``` |

Modified CGImageDestinationCreateWithURL(CFURL!, CFString!, Int, CFDictionary!) -> CGImageDestination!

|  | Declaration |
| --- | --- |
| From | ``` func CGImageDestinationCreateWithURL(_ url: CFURL!, _ type: CFString!, _ count: UInt, _ options: CFDictionary!) -> CGImageDestination! ``` |
| To | ``` func CGImageDestinationCreateWithURL(_ url: CFURL!, _ type: CFString!, _ count: Int, _ options: CFDictionary!) -> CGImageDestination! ``` |

Modified CGImageSourceCopyMetadataAtIndex(CGImageSource!, Int, CFDictionary!) -> CGImageMetadata!

|  | Declaration |
| --- | --- |
| From | ``` func CGImageSourceCopyMetadataAtIndex(_ isrc: CGImageSource!, _ index: UInt, _ options: CFDictionary!) -> CGImageMetadata! ``` |
| To | ``` func CGImageSourceCopyMetadataAtIndex(_ isrc: CGImageSource!, _ index: Int, _ options: CFDictionary!) -> CGImageMetadata! ``` |

Modified CGImageSourceCopyPropertiesAtIndex(CGImageSource!, Int, CFDictionary!) -> CFDictionary!

|  | Declaration |
| --- | --- |
| From | ``` func CGImageSourceCopyPropertiesAtIndex(_ isrc: CGImageSource!, _ index: UInt, _ options: CFDictionary!) -> CFDictionary! ``` |
| To | ``` func CGImageSourceCopyPropertiesAtIndex(_ isrc: CGImageSource!, _ index: Int, _ options: CFDictionary!) -> CFDictionary! ``` |

Modified CGImageSourceCreateImageAtIndex(CGImageSource!, Int, CFDictionary!) -> CGImage!

|  | Declaration |
| --- | --- |
| From | ``` func CGImageSourceCreateImageAtIndex(_ isrc: CGImageSource!, _ index: UInt, _ options: CFDictionary!) -> CGImage! ``` |
| To | ``` func CGImageSourceCreateImageAtIndex(_ isrc: CGImageSource!, _ index: Int, _ options: CFDictionary!) -> CGImage! ``` |

Modified CGImageSourceCreateThumbnailAtIndex(CGImageSource!, Int, CFDictionary!) -> CGImage!

|  | Declaration |
| --- | --- |
| From | ``` func CGImageSourceCreateThumbnailAtIndex(_ isrc: CGImageSource!, _ index: UInt, _ options: CFDictionary!) -> CGImage! ``` |
| To | ``` func CGImageSourceCreateThumbnailAtIndex(_ isrc: CGImageSource!, _ index: Int, _ options: CFDictionary!) -> CGImage! ``` |

Modified CGImageSourceGetCount(CGImageSource!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CGImageSourceGetCount(_ isrc: CGImageSource!) -> UInt ``` |
| To | ``` func CGImageSourceGetCount(_ isrc: CGImageSource!) -> Int ``` |

Modified CGImageSourceGetStatusAtIndex(CGImageSource!, Int) -> CGImageSourceStatus

|  | Declaration |
| --- | --- |
| From | ``` func CGImageSourceGetStatusAtIndex(_ isrc: CGImageSource!, _ index: UInt) -> CGImageSourceStatus ``` |
| To | ``` func CGImageSourceGetStatusAtIndex(_ isrc: CGImageSource!, _ index: Int) -> CGImageSourceStatus ``` |

Modified CGImageSourceRemoveCacheAtIndex(CGImageSource!, Int)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageSourceRemoveCacheAtIndex(_ isrc: CGImageSource!, _ index: UInt) ``` |
| To | ``` func CGImageSourceRemoveCacheAtIndex(_ isrc: CGImageSource!, _ index: Int) ``` |

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
