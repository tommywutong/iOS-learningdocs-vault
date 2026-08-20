---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Objective-C/WebKit.html
archived_at: '2026-07-18T02:55:00.281959Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# WebKit Changes for Objective-C

### WebKit

#### WKPreferences.h

Modified [WKPreferences](https://developer.apple.com/documentation/webkit/wkpreferences)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSCoding |

#### WKPreviewActionItem.h (Added)

Added [WKPreviewActionItem](https://developer.apple.com/documentation/webkit/wkpreviewactionitem)Added [WKPreviewActionItem.identifier](https://developer.apple.com/documentation/webkit/wkpreviewactionitem/1649288-identifier)

#### WKPreviewActionItemIdentifiers.h (Added)

Added [WKPreviewActionItemIdentifierAddToReadingList](https://developer.apple.com/documentation/webkit/wkpreviewactionitemidentifieraddtoreadinglist)Added [WKPreviewActionItemIdentifierCopy](https://developer.apple.com/documentation/webkit/wkpreviewactionitemidentifiercopy)Added [WKPreviewActionItemIdentifierOpen](https://developer.apple.com/documentation/webkit/wkpreviewactionitemidentifieropen)Added [WKPreviewActionItemIdentifierShare](https://developer.apple.com/documentation/webkit/wkpreviewactionitemidentifiershare)

#### WKPreviewElementInfo.h (Added)

Added [WKPreviewElementInfo](https://developer.apple.com/documentation/webkit/wkpreviewelementinfo)Added [WKPreviewElementInfo.linkURL](https://developer.apple.com/documentation/webkit/wkpreviewelementinfo/2211611-linkurl)

#### WKProcessPool.h

Modified [WKProcessPool](https://developer.apple.com/documentation/webkit/wkprocesspool)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSCoding |

#### WKUIDelegate.h

Added [-[WKUIDelegate webView:commitPreviewingViewController:]](https://developer.apple.com/documentation/webkit/wkuidelegate/1648360-webview)Added [-[WKUIDelegate webView:previewingViewControllerForElement:defaultActions:]](https://developer.apple.com/documentation/webkit/wkuidelegate/1648361-webview)Added [-[WKUIDelegate webView:shouldPreviewElement:]](https://developer.apple.com/documentation/webkit/wkuidelegate/1648359-webview)

#### WKUserContentController.h

Modified [WKUserContentController](https://developer.apple.com/documentation/webkit/wkusercontentcontroller)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSCoding |

#### WKWebsiteDataStore.h

Modified [WKWebsiteDataStore](https://developer.apple.com/documentation/webkit/wkwebsitedatastore)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSCoding |

#### WKWebView.h

Added [-[WKWebView initWithCoder:]](https://developer.apple.com/documentation/webkit/wkwebview/1641916-init)Added [WKWebView.serverTrust](https://developer.apple.com/documentation/webkit/wkwebview/1791920-servertrust)Added WKWebView(WKDeprecated)Modified [WKWebView.certificateChain](https://developer.apple.com/documentation/webkit/wkwebview/1414958-certificatechain)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

#### WKWebViewConfiguration.h

Added [WKWebViewConfiguration.dataDetectorTypes](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1641937-datadetectortypes)Added [WKWebViewConfiguration.ignoresViewportScaleLimits](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/2274633-ignoresviewportscalelimits)Added [WKWebViewConfiguration.mediaTypesRequiringUserActionForPlayback](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1851524-mediatypesrequiringuseractionfor)Added [WKAudiovisualMediaTypeAll](https://developer.apple.com/documentation/webkit/wkaudiovisualmediatypes/wkaudiovisualmediatypeall)Added [WKAudiovisualMediaTypeAudio](https://developer.apple.com/documentation/webkit/wkaudiovisualmediatypes/wkaudiovisualmediatypeaudio)Added [WKAudiovisualMediaTypeNone](https://developer.apple.com/documentation/webkit/wkaudiovisualmediatypes/wkaudiovisualmediatypenone)Added [WKAudiovisualMediaTypes](https://developer.apple.com/documentation/webkit/wkaudiovisualmediatypes)Added [WKAudiovisualMediaTypeVideo](https://developer.apple.com/documentation/webkit/wkaudiovisualmediatypes/wkaudiovisualmediatypevideo)Added [WKDataDetectorTypeAddress](https://developer.apple.com/documentation/webkit/wkdatadetectortypes/1641968-address)Added [WKDataDetectorTypeAll](https://developer.apple.com/documentation/webkit/wkdatadetectortypes/1641938-all)Added [WKDataDetectorTypeCalendarEvent](https://developer.apple.com/documentation/webkit/wkdatadetectortypes/wkdatadetectortypecalendarevent)Added [WKDataDetectorTypeFlightNumber](https://developer.apple.com/documentation/webkit/wkdatadetectortypes/wkdatadetectortypeflightnumber)Added [WKDataDetectorTypeLink](https://developer.apple.com/documentation/webkit/wkdatadetectortypes/wkdatadetectortypelink)Added [WKDataDetectorTypeLookupSuggestion](https://developer.apple.com/documentation/webkit/wkdatadetectortypes/wkdatadetectortypelookupsuggestion)Added [WKDataDetectorTypeNone](https://developer.apple.com/documentation/webkit/wkdatadetectortypes/wkdatadetectortypenone)Added [WKDataDetectorTypePhoneNumber](https://developer.apple.com/documentation/webkit/wkdatadetectortypes/wkdatadetectortypephonenumber)Added [WKDataDetectorTypes](https://developer.apple.com/documentation/webkit/wkdatadetectortypes)Added [WKDataDetectorTypeSpotlightSuggestion](https://developer.apple.com/documentation/webkit/wkdatadetectortypes/wkdatadetectortypespotlightsuggestion)Added [WKDataDetectorTypeTrackingNumber](https://developer.apple.com/documentation/webkit/wkdatadetectortypes/wkdatadetectortypetrackingnumber)Modified [WKWebViewConfiguration](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration)

|  | Protocols |
| --- | --- |
| From | NSCopying |
| To | NSCoding, NSCopying |

Modified [WKWebViewConfiguration.requiresUserActionForMediaPlayback](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1614794-requiresuseractionformediaplayba)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

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
