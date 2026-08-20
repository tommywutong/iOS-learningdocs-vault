---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/frameworks/WebKit.html
archived_at: '2026-07-18T02:51:51.090319Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# WebKit Changes

## WebKit

WKNavigation.hRemoved WKNavigation.errorRemoved WKNavigation.initialRequestRemoved WKNavigation.requestRemoved WKNavigation.responseWKWebView.hModified [-[WKWebView goBack:]](https://developer.apple.com/documentation/webkit/wkwebview/1414975-goback)

|  | Declaration |
| --- | --- |
| From | ``` - (void)goBack:(id)sender ``` |
| To | ``` - (IBAction)goBack:(id)sender ``` |

Modified [-[WKWebView goForward:]](https://developer.apple.com/documentation/webkit/wkwebview/1414960-goforward)

|  | Declaration |
| --- | --- |
| From | ``` - (void)goForward:(id)sender ``` |
| To | ``` - (IBAction)goForward:(id)sender ``` |

Modified [-[WKWebView initWithFrame:configuration:]](https://developer.apple.com/documentation/webkit/wkwebview/1414998-initwithframe)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WKWebView reload:]](https://developer.apple.com/documentation/webkit/wkwebview/1414987-reload)

|  | Declaration |
| --- | --- |
| From | ``` - (void)reload:(id)sender ``` |
| To | ``` - (IBAction)reload:(id)sender ``` |

Modified [-[WKWebView reloadFromOrigin:]](https://developer.apple.com/documentation/webkit/wkwebview/1414989-reloadfromorigin)

|  | Declaration |
| --- | --- |
| From | ``` - (void)reloadFromOrigin:(id)sender ``` |
| To | ``` - (IBAction)reloadFromOrigin:(id)sender ``` |

Modified [-[WKWebView stopLoading:]](https://developer.apple.com/documentation/webkit/wkwebview/1415013-stoploading)

|  | Declaration |
| --- | --- |
| From | ``` - (void)stopLoading:(id)sender ``` |
| To | ``` - (IBAction)stopLoading:(id)sender ``` |

WebView.hModified [-[WebView goBack:]](https://developer.apple.com/documentation/webkit/webview/1408482-goback)

|  | Declaration |
| --- | --- |
| From | ``` - (void)goBack:(id)sender ``` |
| To | ``` - (IBAction)goBack:(id)sender ``` |

Modified [-[WebView goForward:]](https://developer.apple.com/documentation/webkit/webview/1408365-goforward)

|  | Declaration |
| --- | --- |
| From | ``` - (void)goForward:(id)sender ``` |
| To | ``` - (IBAction)goForward:(id)sender ``` |

Modified [-[WebView makeTextLarger:]](https://developer.apple.com/documentation/webkit/webview/1408492-maketextlarger)

|  | Declaration |
| --- | --- |
| From | ``` - (void)makeTextLarger:(id)sender ``` |
| To | ``` - (IBAction)makeTextLarger:(id)sender ``` |

Modified [-[WebView makeTextSmaller:]](https://developer.apple.com/documentation/webkit/webview/1408520-maketextsmaller)

|  | Declaration |
| --- | --- |
| From | ``` - (void)makeTextSmaller:(id)sender ``` |
| To | ``` - (IBAction)makeTextSmaller:(id)sender ``` |

Modified [-[WebView makeTextStandardSize:]](https://developer.apple.com/documentation/webkit/webview/1408504-maketextstandardsize)

|  | Declaration |
| --- | --- |
| From | ``` - (void)makeTextStandardSize:(id)sender ``` |
| To | ``` - (IBAction)makeTextStandardSize:(id)sender ``` |

Modified [-[WebView reload:]](https://developer.apple.com/documentation/webkit/webview/1408554-reload)

|  | Declaration |
| --- | --- |
| From | ``` - (void)reload:(id)sender ``` |
| To | ``` - (IBAction)reload:(id)sender ``` |

Modified [-[WebView reloadFromOrigin:]](https://developer.apple.com/documentation/webkit/webview/1408446-reloadfromorigin)

|  | Declaration |
| --- | --- |
| From | ``` - (void)reloadFromOrigin:(id)sender ``` |
| To | ``` - (IBAction)reloadFromOrigin:(id)sender ``` |

Modified [-[WebView stopLoading:]](https://developer.apple.com/documentation/webkit/webview/1408568-stoploading)

|  | Declaration |
| --- | --- |
| From | ``` - (void)stopLoading:(id)sender ``` |
| To | ``` - (IBAction)stopLoading:(id)sender ``` |

Modified [-[WebView takeStringURLFrom:]](https://developer.apple.com/documentation/webkit/webview/1408441-takestringurlfrom)

|  | Declaration |
| --- | --- |
| From | ``` - (void)takeStringURLFrom:(id)sender ``` |
| To | ``` - (IBAction)takeStringURLFrom:(id)sender ``` |

Modified [-[WebView toggleContinuousSpellChecking:]](https://developer.apple.com/documentation/webkit/webview/1408433-togglecontinuousspellchecking)

|  | Declaration |
| --- | --- |
| From | ``` - (void)toggleContinuousSpellChecking:(id)sender ``` |
| To | ``` - (IBAction)toggleContinuousSpellChecking:(id)sender ``` |

Modified [-[WebView toggleSmartInsertDelete:]](https://developer.apple.com/documentation/webkit/webview/1408333-togglesmartinsertdelete)

|  | Declaration |
| --- | --- |
| From | ``` - (void)toggleSmartInsertDelete:(id)sender ``` |
| To | ``` - (IBAction)toggleSmartInsertDelete:(id)sender ``` |

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
