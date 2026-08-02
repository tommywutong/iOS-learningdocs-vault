---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/SystemConfiguration.html
archived_at: '2026-07-18T02:56:17.003785Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# SystemConfiguration Changes

## SystemConfiguration

Modified SCCopyLastError() -> Unmanaged<CFError>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SCError() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SCErrorString(Int32) -> UnsafePointer<Int8>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SCNetworkReachabilityCreateWithAddress(CFAllocator!, UnsafePointer<sockaddr>) -> Unmanaged<SCNetworkReachability>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SCNetworkReachabilityCreateWithAddressPair(CFAllocator!, UnsafePointer<sockaddr>, UnsafePointer<sockaddr>) -> Unmanaged<SCNetworkReachability>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SCNetworkReachabilityCreateWithName(CFAllocator!, UnsafePointer<Int8>) -> Unmanaged<SCNetworkReachability>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SCNetworkReachabilityGetFlags(SCNetworkReachability!, UnsafeMutablePointer<SCNetworkReachabilityFlags>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SCNetworkReachabilityGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SCNetworkReachabilityScheduleWithRunLoop(SCNetworkReachability!, CFRunLoop!, CFString!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SCNetworkReachabilitySetCallback(SCNetworkReachability!, SCNetworkReachabilityCallBack, UnsafeMutablePointer<SCNetworkReachabilityContext>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SCNetworkReachabilitySetDispatchQueue(SCNetworkReachability!, dispatch_queue_t!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified SCNetworkReachabilityUnscheduleFromRunLoop(SCNetworkReachability!, CFRunLoop!, CFString!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFErrorDomainSystemConfiguration

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

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
