---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/WebKit.html
archived_at: '2026-07-18T02:57:11.894701Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# WebKit Changes for Swift

### WebKit

Modified [WKBackForwardList](https://developer.apple.com/documentation/webkit/wkbackforwardlist)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKBackForwardListItem](https://developer.apple.com/documentation/webkit/wkbackforwardlistitem)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKErrorCode [enum]](https://developer.apple.com/documentation/webkit/wkerrorcode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` enum WKErrorCode : Int {     case Unknown     case WebContentProcessTerminated     case WebViewInvalidated     case JavaScriptExceptionOccurred     case JavaScriptResultTypeIsUnsupported } extension WKErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension WKErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable |
| To | ``` enum WKErrorCode : Int {     case Unknown     case WebContentProcessTerminated     case WebViewInvalidated     case JavaScriptExceptionOccurred     case JavaScriptResultTypeIsUnsupported } extension WKErrorCode : _BridgedNSError { } extension WKErrorCode : _BridgedNSError { } ``` | -- |

Modified [WKFrameInfo](https://developer.apple.com/documentation/webkit/wkframeinfo)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [WKNavigation](https://developer.apple.com/documentation/webkit/wknavigation)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKNavigationAction](https://developer.apple.com/documentation/webkit/wknavigationaction)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKNavigationActionPolicy [enum]](https://developer.apple.com/documentation/webkit/wknavigationactionpolicy)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [WKNavigationResponse](https://developer.apple.com/documentation/webkit/wknavigationresponse)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKNavigationResponsePolicy [enum]](https://developer.apple.com/documentation/webkit/wknavigationresponsepolicy)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [WKNavigationType [enum]](https://developer.apple.com/documentation/webkit/wknavigationtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [WKPreferences](https://developer.apple.com/documentation/webkit/wkpreferences)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKProcessPool](https://developer.apple.com/documentation/webkit/wkprocesspool)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKScriptMessage](https://developer.apple.com/documentation/webkit/wkscriptmessage)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKSecurityOrigin](https://developer.apple.com/documentation/webkit/wksecurityorigin)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKSelectionGranularity [enum]](https://developer.apple.com/documentation/webkit/wkselectiongranularity)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [WKUserContentController](https://developer.apple.com/documentation/webkit/wkusercontentcontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKUserScript](https://developer.apple.com/documentation/webkit/wkuserscript)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [WKUserScriptInjectionTime [enum]](https://developer.apple.com/documentation/webkit/wkuserscriptinjectiontime)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [WKWebsiteDataRecord](https://developer.apple.com/documentation/webkit/wkwebsitedatarecord)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKWebsiteDataStore](https://developer.apple.com/documentation/webkit/wkwebsitedatastore)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKWebView](https://developer.apple.com/documentation/webkit/wkwebview)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKWebViewConfiguration](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [WKWindowFeatures](https://developer.apple.com/documentation/webkit/wkwindowfeatures)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

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
