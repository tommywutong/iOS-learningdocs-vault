---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/CoreTelephony.html
archived_at: '2026-07-18T02:56:23.235230Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# CoreTelephony Changes

## CoreTelephony

Added CTError.init()Added CTError.init(domain: Int32, error: Int32)Modified CTCallCenter.currentCalls

|  | Declaration |
| --- | --- |
| From | ``` var currentCalls: NSSet! { get } ``` |
| To | ``` var currentCalls: Set<NSObject>! { get } ``` |

Modified CTError [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CTError {     var domain: Int32     var error: Int32 } ``` |
| To | ``` struct CTError {     var domain: Int32     var error: Int32     init()     init(domain domain: Int32, error error: Int32) } ``` |

Modified CTCallStateConnected

|  | Declaration |
| --- | --- |
| From | ``` let CTCallStateConnected: NSString! ``` |
| To | ``` let CTCallStateConnected: String ``` |

Modified CTCallStateDialing

|  | Declaration |
| --- | --- |
| From | ``` let CTCallStateDialing: NSString! ``` |
| To | ``` let CTCallStateDialing: String ``` |

Modified CTCallStateDisconnected

|  | Declaration |
| --- | --- |
| From | ``` let CTCallStateDisconnected: NSString! ``` |
| To | ``` let CTCallStateDisconnected: String ``` |

Modified CTCallStateIncoming

|  | Declaration |
| --- | --- |
| From | ``` let CTCallStateIncoming: NSString! ``` |
| To | ``` let CTCallStateIncoming: String ``` |

Modified CTRadioAccessTechnologyCDMA1x

|  | Declaration |
| --- | --- |
| From | ``` let CTRadioAccessTechnologyCDMA1x: NSString! ``` |
| To | ``` let CTRadioAccessTechnologyCDMA1x: String ``` |

Modified CTRadioAccessTechnologyCDMAEVDORev0

|  | Declaration |
| --- | --- |
| From | ``` let CTRadioAccessTechnologyCDMAEVDORev0: NSString! ``` |
| To | ``` let CTRadioAccessTechnologyCDMAEVDORev0: String ``` |

Modified CTRadioAccessTechnologyCDMAEVDORevA

|  | Declaration |
| --- | --- |
| From | ``` let CTRadioAccessTechnologyCDMAEVDORevA: NSString! ``` |
| To | ``` let CTRadioAccessTechnologyCDMAEVDORevA: String ``` |

Modified CTRadioAccessTechnologyCDMAEVDORevB

|  | Declaration |
| --- | --- |
| From | ``` let CTRadioAccessTechnologyCDMAEVDORevB: NSString! ``` |
| To | ``` let CTRadioAccessTechnologyCDMAEVDORevB: String ``` |

Modified CTRadioAccessTechnologyDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let CTRadioAccessTechnologyDidChangeNotification: NSString! ``` |
| To | ``` let CTRadioAccessTechnologyDidChangeNotification: String ``` |

Modified CTRadioAccessTechnologyEdge

|  | Declaration |
| --- | --- |
| From | ``` let CTRadioAccessTechnologyEdge: NSString! ``` |
| To | ``` let CTRadioAccessTechnologyEdge: String ``` |

Modified CTRadioAccessTechnologyGPRS

|  | Declaration |
| --- | --- |
| From | ``` let CTRadioAccessTechnologyGPRS: NSString! ``` |
| To | ``` let CTRadioAccessTechnologyGPRS: String ``` |

Modified CTRadioAccessTechnologyHSDPA

|  | Declaration |
| --- | --- |
| From | ``` let CTRadioAccessTechnologyHSDPA: NSString! ``` |
| To | ``` let CTRadioAccessTechnologyHSDPA: String ``` |

Modified CTRadioAccessTechnologyHSUPA

|  | Declaration |
| --- | --- |
| From | ``` let CTRadioAccessTechnologyHSUPA: NSString! ``` |
| To | ``` let CTRadioAccessTechnologyHSUPA: String ``` |

Modified CTRadioAccessTechnologyLTE

|  | Declaration |
| --- | --- |
| From | ``` let CTRadioAccessTechnologyLTE: NSString! ``` |
| To | ``` let CTRadioAccessTechnologyLTE: String ``` |

Modified CTRadioAccessTechnologyWCDMA

|  | Declaration |
| --- | --- |
| From | ``` let CTRadioAccessTechnologyWCDMA: NSString! ``` |
| To | ``` let CTRadioAccessTechnologyWCDMA: String ``` |

Modified CTRadioAccessTechnologyeHRPD

|  | Declaration |
| --- | --- |
| From | ``` let CTRadioAccessTechnologyeHRPD: NSString! ``` |
| To | ``` let CTRadioAccessTechnologyeHRPD: String ``` |

Modified CTSubscriberTokenRefreshed

|  | Declaration |
| --- | --- |
| From | ``` let CTSubscriberTokenRefreshed: NSString! ``` |
| To | ``` let CTSubscriberTokenRefreshed: String ``` |

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
