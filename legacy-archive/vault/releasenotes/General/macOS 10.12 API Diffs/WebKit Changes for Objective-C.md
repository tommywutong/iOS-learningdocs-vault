---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/WebKit.html
archived_at: '2026-07-18T02:50:45.904438Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# WebKit Changes for Objective-C

### WebKit

#### WebDownload.h

Added #def WebDownload_h

#### WebEditingDelegate.h

Removed NSObject(WebEditingDelegate)Modified [-[WebEditingDelegate undoManagerForWebView:]](https://developer.apple.com/documentation/webkit/webeditingdelegate/1641945-undomanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebEditingDelegate webView:doCommandBySelector:]](https://developer.apple.com/documentation/webkit/webeditingdelegate/1641940-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebEditingDelegate webView:shouldApplyStyle:toElementsInDOMRange:]](https://developer.apple.com/documentation/webkit/webeditingdelegate/1641943-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebEditingDelegate webView:shouldBeginEditingInDOMRange:]](https://developer.apple.com/documentation/webkit/webeditingdelegate/1641942-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebEditingDelegate webView:shouldChangeSelectedDOMRange:toDOMRange:affinity:stillSelecting:]](https://developer.apple.com/documentation/webkit/webeditingdelegate/1641949-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebEditingDelegate webView:shouldChangeTypingStyle:toStyle:]](https://developer.apple.com/documentation/webkit/webeditingdelegate/1641944-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebEditingDelegate webView:shouldDeleteDOMRange:]](https://developer.apple.com/documentation/webkit/webeditingdelegate/1641948-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebEditingDelegate webView:shouldEndEditingInDOMRange:]](https://developer.apple.com/documentation/webkit/webeditingdelegate/1641936-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebEditingDelegate webView:shouldInsertNode:replacingDOMRange:givenAction:]](https://developer.apple.com/documentation/webkit/webeditingdelegate/1641975-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebEditingDelegate webView:shouldInsertText:replacingDOMRange:givenAction:]](https://developer.apple.com/documentation/webkit/webeditingdelegate/1641939-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebEditingDelegate webViewDidBeginEditing:]](https://developer.apple.com/documentation/webkit/webeditingdelegate/1641978-webviewdidbeginediting)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebEditingDelegate webViewDidChange:]](https://developer.apple.com/documentation/webkit/webeditingdelegate/1641915-webviewdidchange)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebEditingDelegate webViewDidChangeSelection:]](https://developer.apple.com/documentation/webkit/webeditingdelegate/1641954-webviewdidchangeselection)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebEditingDelegate webViewDidChangeTypingStyle:]](https://developer.apple.com/documentation/webkit/webeditingdelegate/1641918-webviewdidchangetypingstyle)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebEditingDelegate webViewDidEndEditing:]](https://developer.apple.com/documentation/webkit/webeditingdelegate/1641919-webviewdidendediting)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

#### WebView.h

Modified [WebView.editingDelegate](https://developer.apple.com/documentation/webkit/webview/1408349-editingdelegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) id editingDelegate ``` |
| To | ``` @property(nonatomic, assign) id<WebEditingDelegate> editingDelegate ``` |

#### WKOpenPanelParameters.h (Added)

Added [WKOpenPanelParameters](https://developer.apple.com/documentation/webkit/wkopenpanelparameters)Added [WKOpenPanelParameters.allowsMultipleSelection](https://developer.apple.com/documentation/webkit/wkopenpanelparameters/1639524-allowsmultipleselection)

#### WKPreferences.h

Modified [WKPreferences](https://developer.apple.com/documentation/webkit/wkpreferences)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSCoding |

#### WKProcessPool.h

Modified [WKProcessPool](https://developer.apple.com/documentation/webkit/wkprocesspool)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSCoding |

#### WKUIDelegate.h

Added [-[WKUIDelegate webView:runOpenPanelWithParameters:initiatedByFrame:completionHandler:]](https://developer.apple.com/documentation/webkit/wkuidelegate/1641952-webview)

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
| To | OS X 10.12 |

#### WKWebViewConfiguration.h

Added [WKWebViewConfiguration.mediaTypesRequiringUserActionForPlayback](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1851524-mediatypesrequiringuseractionfor)Added [WKWebViewConfiguration.userInterfaceDirectionPolicy](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1690322-userinterfacedirectionpolicy)Added [WKAudiovisualMediaTypeAll](https://developer.apple.com/documentation/webkit/wkaudiovisualmediatypes/wkaudiovisualmediatypeall)Added [WKAudiovisualMediaTypeAudio](https://developer.apple.com/documentation/webkit/wkaudiovisualmediatypes/wkaudiovisualmediatypeaudio)Added [WKAudiovisualMediaTypeNone](https://developer.apple.com/documentation/webkit/wkaudiovisualmediatypes/wkaudiovisualmediatypenone)Added [WKAudiovisualMediaTypes](https://developer.apple.com/documentation/webkit/wkaudiovisualmediatypes)Added [WKAudiovisualMediaTypeVideo](https://developer.apple.com/documentation/webkit/wkaudiovisualmediatypes/wkaudiovisualmediatypevideo)Added [WKUserInterfaceDirectionPolicy](https://developer.apple.com/documentation/webkit/wkuserinterfacedirectionpolicy)Added [WKUserInterfaceDirectionPolicyContent](https://developer.apple.com/documentation/webkit/wkuserinterfacedirectionpolicy/wkuserinterfacedirectionpolicycontent)Added [WKUserInterfaceDirectionPolicySystem](https://developer.apple.com/documentation/webkit/wkuserinterfacedirectionpolicy/wkuserinterfacedirectionpolicysystem)Modified [WKWebViewConfiguration](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration)

|  | Protocols |
| --- | --- |
| From | NSCopying |
| To | NSCoding, NSCopying |

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
