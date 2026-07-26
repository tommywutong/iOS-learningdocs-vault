---
title: Replacing UIWebView in your app
framework: WebKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/webkit/replacing-uiwebview-in-your-app
source_url: 'https://developer.apple.com/documentation/webkit/replacing-uiwebview-in-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/webkit/replacing-uiwebview-in-your-app.json'
content_hash: 'sha256:5822705e24efd1ed'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WebKit](../webkit.md) · [WebKit for AppKit and UIKit](webkit-for-appkit-and-uikit.md)

# Replacing UIWebView in your app

<sub>Article</sub>

Find a suitable alternative to handle your app’s web content.

## Overview

If your app is using [UIWebView](../uikit/uiwebview.md), you need to replace it with another Apple technology, because this class is now deprecated. Choose among several technologies, based on your app’s functionality and the degree of configurability you need. This article explores some alternatives and specifically the configuration and architectural changes of [WKWebView](wkwebview.md).

### Consider alternative technologies

Before beginning a migration away from [UIWebView](../uikit/uiwebview.md), consider whether it can be replaced with other tools. Apple has a variety of technologies that can replace a web view to accomplish similar functionality, and possibly a richer feature set with less code.

If you need an in-app web browser and don’t need deep customization of that experience, [SFSafariViewController](../safariservices/sfsafariviewcontroller.md) is a good choice. It handles all the features you’d need to implement in a basic browser and more.

If you need to authenticate your users, use [ASWebAuthenticationSession](../authenticationservices/aswebauthenticationsession.md).

If you need to display maps or map tiles, consider using [MKMapView](../mapkit/mkmapview.md).

### Update to WKWebView

If you need a high degree of configurability or are using web content in ways unrelated to browsing, use [WKWebView](wkwebview.md).

[WKWebView](wkwebview.md) isn’t a drop-in replacement for [UIWebView](../uikit/uiwebview.md). It has a different architecture that requires rethinking how you use web views, as well as code changes to implement its functionality. You may not be able to implement some features in [WKWebView](wkwebview.md).

### Implement delegates for functionality

[WKWebView](wkwebview.md) uses various delegates to implement functionality that’s similar to [UIWebViewDelegate](../uikit/uiwebviewdelegate.md). The table below shows the [UIWebViewDelegate](../uikit/uiwebviewdelegate.md) methods and their [WKWebView](wkwebview.md) equivalents in the [WKNavigationDelegate](wknavigationdelegate.md) column.

| `UIWebViewDelegate` | `WKNavigationDelegate` |
|---|---|
| [webViewDidStartLoad(_:)](<../uikit/uiwebviewdelegate/webviewdidstartload(__).md>) | [- webView:didStartProvisionalNavigation:](<wknavigationdelegate/webview(__didstartprovisionalnavigation_).md>) |
| [webViewDidFinishLoad(_:)](<../uikit/uiwebviewdelegate/webviewdidfinishload(__).md>) | [- webView:didFinishNavigation:](<wknavigationdelegate/webview(__didfinish_).md>) |
| [webView(_:didFailLoadWithError:)](<../uikit/uiwebviewdelegate/webview(__didfailloadwitherror_).md>) | [- webView:didFailProvisionalNavigation:withError:](<wknavigationdelegate/webview(__didfailprovisionalnavigation_witherror_).md>) or [- webView:didFailNavigation:withError:](<wknavigationdelegate/webview(__didfail_witherror_).md>) |
| [webView(_:shouldStartLoadWith:navigationType:)](<../uikit/uiwebviewdelegate/webview(__shouldstartloadwith_navigationtype_).md>) | [- webView:decidePolicyForNavigationAction:decisionHandler:](<wknavigationdelegate/webview(__decidepolicyfor_decisionhandler_)-2ni62.md>) or [- webView:decidePolicyForNavigationResponse:decisionHandler:](<wknavigationdelegate/webview(__decidepolicyfor_decisionhandler_)-19mn2.md>) |
| [connection(_:didReceive:)](<../foundation/nsurlconnectiondelegate/connection(__didreceive_).md>) | [- webView:didReceiveAuthenticationChallenge:completionHandler:](<wknavigationdelegate/webview(__didreceive_completionhandler_).md>) |

> [!note] Note
> The [- webView:decidePolicyForNavigationAction:decisionHandler:](<wknavigationdelegate/webview(__decidepolicyfor_decisionhandler_)-2ni62.md>) function doesn’t return a Boolean as its [UIWebView](../uikit/uiwebview.md) counterpart did; it uses the `decisionHandler` to return an [WKNavigationActionPolicyAllow](wknavigationactionpolicy/allow.md) or [WKNavigationActionPolicyCancel](wknavigationactionpolicy/cancel.md) value.

### Plan for architectural changes

One major architectural difference between [UIWebView](../uikit/uiwebview.md) and [WKWebView](wkwebview.md) is that the methods of [WKWebView](wkwebview.md) tend to be asynchronous, while the methods of [UIWebView](../uikit/uiwebview.md) were synchronous.

This difference requires code and architecture changes in your app. Another major change relates to creating single sign on (SSO) functionality. Cookie restrictions across the entire [WKWebView](wkwebview.md) landscape, mean SSO functionality in [WKWebView](wkwebview.md) isn’t supported for third-party cookies and clients should use a token-based authentication system like OAuth for SSO. Third-party cookies are cookies for a domain other than the domain for which the context was loaded. APIs in the [Authentication Services](../authenticationservices.md) framework are specifically built to do this.

## See Also

### Web views

- [Viewing Desktop or Mobile Web Content Using a Web View](viewing-desktop-or-mobile-web-content-using-a-web-view.md) — Implement a simple iPad web browser that can view either the desktop or mobile version of a website.
- [WKWebView](wkwebview.md) — An object that displays interactive web content, such as for an in-app browser.
- [WKUIDelegate](wkuidelegate.md) — The methods for presenting native user interface elements on behalf of a webpage.
