---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/SystemConfiguration.html
archived_at: '2026-07-18T02:56:28.356160Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# SystemConfiguration Changes

## SystemConfiguration

Added SCDynamicStoreContext.init()Added SCDynamicStoreContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Added SCNetworkConnectionContext.init()Added SCNetworkConnectionContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Added SCNetworkReachabilityContext.init()Added SCNetworkReachabilityContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Added SCPreferencesContext.init()Added SCPreferencesContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Added kSCNetworkConnectionBytesInAdded kSCNetworkConnectionBytesOutAdded kSCNetworkConnectionErrorsInAdded kSCNetworkConnectionErrorsOutAdded kSCNetworkConnectionPacketsInAdded kSCNetworkConnectionPacketsOutAdded kSCNetworkConnectionSelectionOptionOnDemandHostNameAdded kSCNetworkConnectionSelectionOptionOnDemandRetryModified SCDynamicStoreContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SCDynamicStoreContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> } ``` |
| To | ``` struct SCDynamicStoreContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |

Modified SCNetworkConnectionContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SCNetworkConnectionContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> } ``` |
| To | ``` struct SCNetworkConnectionContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |

Modified SCNetworkReachabilityContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SCNetworkReachabilityContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> } ``` |
| To | ``` struct SCNetworkReachabilityContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |

Modified SCPreferencesContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SCPreferencesContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> } ``` |
| To | ``` struct SCPreferencesContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |

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
