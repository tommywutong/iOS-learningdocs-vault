---
title: macOS 10.12.1 API Diffs
apple_id: TP40017565
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12_1/Swift/SystemConfiguration.html
archived_at: '2026-07-18T02:51:47.823449Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12.1 API Diffs](macOS%2010.12%20to%20macOS%2010.12.1%20API%20Differences.md)


# SystemConfiguration Changes for Swift

### SystemConfiguration

Modified [SCDynamicStoreContext [struct]](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecontext)

|  | Declaration |
| --- | --- |
| From | ``` struct SCDynamicStoreContext {     var version: CFIndex     var info: UnsafeMutableRawPointer?     var retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?     var release: ((UnsafeRawPointer) -> Swift.Void)?     var copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer?, retain retain: (@escaping (UnsafeRawPointer) -> UnsafeRawPointer)?, release release: (@escaping (UnsafeRawPointer) -> Swift.Void)?, copyDescription copyDescription: (@escaping (UnsafeRawPointer) -> Unmanaged<CFString>)?) } ``` |
| To | ``` struct SCDynamicStoreContext {     var version: CFIndex     var info: UnsafeMutableRawPointer?     var retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?     var release: ((UnsafeRawPointer) -> Swift.Void)?     var copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer?, retain retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?, release release: ((UnsafeRawPointer) -> Swift.Void)?, copyDescription copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?) } ``` |

Modified [SCDynamicStoreContext.init(version: CFIndex, info: UnsafeMutableRawPointer?, retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?, release: ((UnsafeRawPointer) -> Swift.Void)?, copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?)](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecontext/1517217-init)

|  | Declaration |
| --- | --- |
| From | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer?, retain retain: (@escaping (UnsafeRawPointer) -> UnsafeRawPointer)?, release release: (@escaping (UnsafeRawPointer) -> Swift.Void)?, copyDescription copyDescription: (@escaping (UnsafeRawPointer) -> Unmanaged<CFString>)?) ``` |
| To | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer?, retain retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?, release release: ((UnsafeRawPointer) -> Swift.Void)?, copyDescription copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?) ``` |

Modified [SCNetworkConnectionContext [struct]](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectioncontext)

|  | Declaration |
| --- | --- |
| From | ``` struct SCNetworkConnectionContext {     var version: CFIndex     var info: UnsafeMutableRawPointer?     var retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?     var release: ((UnsafeRawPointer) -> Swift.Void)?     var copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer?, retain retain: (@escaping (UnsafeRawPointer) -> UnsafeRawPointer)?, release release: (@escaping (UnsafeRawPointer) -> Swift.Void)?, copyDescription copyDescription: (@escaping (UnsafeRawPointer) -> Unmanaged<CFString>)?) } ``` |
| To | ``` struct SCNetworkConnectionContext {     var version: CFIndex     var info: UnsafeMutableRawPointer?     var retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?     var release: ((UnsafeRawPointer) -> Swift.Void)?     var copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer?, retain retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?, release release: ((UnsafeRawPointer) -> Swift.Void)?, copyDescription copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?) } ``` |

Modified [SCNetworkConnectionContext.init(version: CFIndex, info: UnsafeMutableRawPointer?, retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?, release: ((UnsafeRawPointer) -> Swift.Void)?, copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?)](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectioncontext/1517275-init)

|  | Declaration |
| --- | --- |
| From | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer?, retain retain: (@escaping (UnsafeRawPointer) -> UnsafeRawPointer)?, release release: (@escaping (UnsafeRawPointer) -> Swift.Void)?, copyDescription copyDescription: (@escaping (UnsafeRawPointer) -> Unmanaged<CFString>)?) ``` |
| To | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer?, retain retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?, release release: ((UnsafeRawPointer) -> Swift.Void)?, copyDescription copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?) ``` |

Modified [SCNetworkReachabilityContext [struct]](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitycontext)

|  | Declaration |
| --- | --- |
| From | ``` struct SCNetworkReachabilityContext {     var version: CFIndex     var info: UnsafeMutableRawPointer?     var retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?     var release: ((UnsafeRawPointer) -> Swift.Void)?     var copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer?, retain retain: (@escaping (UnsafeRawPointer) -> UnsafeRawPointer)?, release release: (@escaping (UnsafeRawPointer) -> Swift.Void)?, copyDescription copyDescription: (@escaping (UnsafeRawPointer) -> Unmanaged<CFString>)?) } ``` |
| To | ``` struct SCNetworkReachabilityContext {     var version: CFIndex     var info: UnsafeMutableRawPointer?     var retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?     var release: ((UnsafeRawPointer) -> Swift.Void)?     var copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer?, retain retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?, release release: ((UnsafeRawPointer) -> Swift.Void)?, copyDescription copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?) } ``` |

Modified [SCNetworkReachabilityContext.init(version: CFIndex, info: UnsafeMutableRawPointer?, retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?, release: ((UnsafeRawPointer) -> Swift.Void)?, copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?)](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitycontext/1516770-init)

|  | Declaration |
| --- | --- |
| From | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer?, retain retain: (@escaping (UnsafeRawPointer) -> UnsafeRawPointer)?, release release: (@escaping (UnsafeRawPointer) -> Swift.Void)?, copyDescription copyDescription: (@escaping (UnsafeRawPointer) -> Unmanaged<CFString>)?) ``` |
| To | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer?, retain retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?, release release: ((UnsafeRawPointer) -> Swift.Void)?, copyDescription copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?) ``` |

Modified [SCPreferencesContext [struct]](https://developer.apple.com/documentation/systemconfiguration/scpreferencescontext)

|  | Declaration |
| --- | --- |
| From | ``` struct SCPreferencesContext {     var version: CFIndex     var info: UnsafeMutableRawPointer?     var retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?     var release: ((UnsafeRawPointer) -> Swift.Void)?     var copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer?, retain retain: (@escaping (UnsafeRawPointer) -> UnsafeRawPointer)?, release release: (@escaping (UnsafeRawPointer) -> Swift.Void)?, copyDescription copyDescription: (@escaping (UnsafeRawPointer) -> Unmanaged<CFString>)?) } ``` |
| To | ``` struct SCPreferencesContext {     var version: CFIndex     var info: UnsafeMutableRawPointer?     var retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?     var release: ((UnsafeRawPointer) -> Swift.Void)?     var copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer?, retain retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?, release release: ((UnsafeRawPointer) -> Swift.Void)?, copyDescription copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?) } ``` |

Modified [SCPreferencesContext.init(version: CFIndex, info: UnsafeMutableRawPointer?, retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?, release: ((UnsafeRawPointer) -> Swift.Void)?, copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?)](https://developer.apple.com/documentation/systemconfiguration/scpreferencescontext/1516727-init)

|  | Declaration |
| --- | --- |
| From | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer?, retain retain: (@escaping (UnsafeRawPointer) -> UnsafeRawPointer)?, release release: (@escaping (UnsafeRawPointer) -> Swift.Void)?, copyDescription copyDescription: (@escaping (UnsafeRawPointer) -> Unmanaged<CFString>)?) ``` |
| To | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer?, retain retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?, release release: ((UnsafeRawPointer) -> Swift.Void)?, copyDescription copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?) ``` |

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
