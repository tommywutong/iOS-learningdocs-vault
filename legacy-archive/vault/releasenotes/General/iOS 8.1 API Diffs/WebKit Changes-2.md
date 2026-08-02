---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/WebKit.html
archived_at: '2026-07-18T02:56:18.166441Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# WebKit Changes

## WebKit

Modified WKBackForwardList.backItem

|  | Declaration |
| --- | --- |
| From | ``` var backItem: WKBackForwardListItem! { get } ``` |
| To | ``` var backItem: WKBackForwardListItem? { get } ``` |

Modified WKBackForwardList.backList

|  | Declaration |
| --- | --- |
| From | ``` var backList: [AnyObject]! { get } ``` |
| To | ``` var backList: [AnyObject] { get } ``` |

Modified WKBackForwardList.currentItem

|  | Declaration |
| --- | --- |
| From | ``` var currentItem: WKBackForwardListItem! { get } ``` |
| To | ``` var currentItem: WKBackForwardListItem? { get } ``` |

Modified WKBackForwardList.forwardItem

|  | Declaration |
| --- | --- |
| From | ``` var forwardItem: WKBackForwardListItem! { get } ``` |
| To | ``` var forwardItem: WKBackForwardListItem? { get } ``` |

Modified WKBackForwardList.forwardList

|  | Declaration |
| --- | --- |
| From | ``` var forwardList: [AnyObject]! { get } ``` |
| To | ``` var forwardList: [AnyObject] { get } ``` |

Modified WKBackForwardList.itemAtIndex(Int) -> WKBackForwardListItem?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func itemAtIndex(_ index: Int) -> WKBackForwardListItem! ``` | iOS 8.0 |
| To | ``` func itemAtIndex(_ index: Int) -> WKBackForwardListItem? ``` | iOS 8.1 |

Modified WKBackForwardListItem.URL

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var URL: NSURL! { get } ``` |
| To | ``` @NSCopying var URL: NSURL { get } ``` |

Modified WKBackForwardListItem.initialURL

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var initialURL: NSURL! { get } ``` |
| To | ``` @NSCopying var initialURL: NSURL { get } ``` |

Modified WKBackForwardListItem.title

|  | Declaration |
| --- | --- |
| From | ``` var title: String! { get } ``` |
| To | ``` var title: String? { get } ``` |

Modified WKFrameInfo.request

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var request: NSURLRequest! { get } ``` |
| To | ``` @NSCopying var request: NSURLRequest { get } ``` |

Modified WKNavigationAction.request

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var request: NSURLRequest! { get } ``` |
| To | ``` @NSCopying var request: NSURLRequest { get } ``` |

Modified WKNavigationAction.sourceFrame

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var sourceFrame: WKFrameInfo! { get } ``` |
| To | ``` @NSCopying var sourceFrame: WKFrameInfo? { get } ``` |

Modified WKNavigationAction.targetFrame

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var targetFrame: WKFrameInfo! { get } ``` |
| To | ``` @NSCopying var targetFrame: WKFrameInfo? { get } ``` |

Modified WKNavigationDelegate.webView(WKWebView, decidePolicyForNavigationAction: WKNavigationAction, decisionHandler:(WKNavigationActionPolicy) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: WKWebView!, decidePolicyForNavigationAction navigationAction: WKNavigationAction!, decisionHandler decisionHandler: ((WKNavigationActionPolicy) -> Void)!) ``` | iOS 8.0 |
| To | ``` optional func webView(_ webView: WKWebView, decidePolicyForNavigationAction navigationAction: WKNavigationAction, decisionHandler decisionHandler: (WKNavigationActionPolicy) -> Void) ``` | iOS 8.1 |

Modified WKNavigationDelegate.webView(WKWebView, decidePolicyForNavigationResponse: WKNavigationResponse, decisionHandler:(WKNavigationResponsePolicy) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: WKWebView!, decidePolicyForNavigationResponse navigationResponse: WKNavigationResponse!, decisionHandler decisionHandler: ((WKNavigationResponsePolicy) -> Void)!) ``` | iOS 8.0 |
| To | ``` optional func webView(_ webView: WKWebView, decidePolicyForNavigationResponse navigationResponse: WKNavigationResponse, decisionHandler decisionHandler: (WKNavigationResponsePolicy) -> Void) ``` | iOS 8.1 |

Modified WKNavigationDelegate.webView(WKWebView, didCommitNavigation: WKNavigation!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: WKWebView!, didCommitNavigation navigation: WKNavigation!) ``` | iOS 8.0 |
| To | ``` optional func webView(_ webView: WKWebView, didCommitNavigation navigation: WKNavigation!) ``` | iOS 8.1 |

Modified WKNavigationDelegate.webView(WKWebView, didFailNavigation: WKNavigation!, withError: NSError)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: WKWebView!, didFailNavigation navigation: WKNavigation!, withError error: NSError!) ``` | iOS 8.0 |
| To | ``` optional func webView(_ webView: WKWebView, didFailNavigation navigation: WKNavigation!, withError error: NSError) ``` | iOS 8.1 |

Modified WKNavigationDelegate.webView(WKWebView, didFailProvisionalNavigation: WKNavigation!, withError: NSError)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: WKWebView!, didFailProvisionalNavigation navigation: WKNavigation!, withError error: NSError!) ``` | iOS 8.0 |
| To | ``` optional func webView(_ webView: WKWebView, didFailProvisionalNavigation navigation: WKNavigation!, withError error: NSError) ``` | iOS 8.1 |

Modified WKNavigationDelegate.webView(WKWebView, didFinishNavigation: WKNavigation!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: WKWebView!, didFinishNavigation navigation: WKNavigation!) ``` | iOS 8.0 |
| To | ``` optional func webView(_ webView: WKWebView, didFinishNavigation navigation: WKNavigation!) ``` | iOS 8.1 |

Modified WKNavigationDelegate.webView(WKWebView, didReceiveAuthenticationChallenge: NSURLAuthenticationChallenge, completionHandler:(NSURLSessionAuthChallengeDisposition, NSURLCredential!) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: WKWebView!, didReceiveAuthenticationChallenge challenge: NSURLAuthenticationChallenge!, completionHandler completionHandler: ((NSURLSessionAuthChallengeDisposition, NSURLCredential!) -> Void)!) ``` | iOS 8.0 |
| To | ``` optional func webView(_ webView: WKWebView, didReceiveAuthenticationChallenge challenge: NSURLAuthenticationChallenge, completionHandler completionHandler: (NSURLSessionAuthChallengeDisposition, NSURLCredential!) -> Void) ``` | iOS 8.1 |

Modified WKNavigationDelegate.webView(WKWebView, didReceiveServerRedirectForProvisionalNavigation: WKNavigation!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: WKWebView!, didReceiveServerRedirectForProvisionalNavigation navigation: WKNavigation!) ``` | iOS 8.0 |
| To | ``` optional func webView(_ webView: WKWebView, didReceiveServerRedirectForProvisionalNavigation navigation: WKNavigation!) ``` | iOS 8.1 |

Modified WKNavigationDelegate.webView(WKWebView, didStartProvisionalNavigation: WKNavigation!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: WKWebView!, didStartProvisionalNavigation navigation: WKNavigation!) ``` | iOS 8.0 |
| To | ``` optional func webView(_ webView: WKWebView, didStartProvisionalNavigation navigation: WKNavigation!) ``` | iOS 8.1 |

Modified WKNavigationResponse.response

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var response: NSURLResponse! { get } ``` |
| To | ``` @NSCopying var response: NSURLResponse { get } ``` |

Modified WKScriptMessage.body

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var body: AnyObject! { get } ``` |
| To | ``` @NSCopying var body: AnyObject { get } ``` |

Modified WKScriptMessage.frameInfo

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var frameInfo: WKFrameInfo! { get } ``` |
| To | ``` @NSCopying var frameInfo: WKFrameInfo { get } ``` |

Modified WKScriptMessage.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified WKScriptMessage.webView

|  | Declaration |
| --- | --- |
| From | ``` weak var webView: WKWebView! { get } ``` |
| To | ``` weak var webView: WKWebView? { get } ``` |

Modified WKScriptMessageHandler.userContentController(WKUserContentController, didReceiveScriptMessage: WKScriptMessage)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func userContentController(_ userContentController: WKUserContentController!, didReceiveScriptMessage message: WKScriptMessage!) ``` | iOS 8.0 |
| To | ``` func userContentController(_ userContentController: WKUserContentController, didReceiveScriptMessage message: WKScriptMessage) ``` | iOS 8.1 |

Modified WKUIDelegate.webView(WKWebView, createWebViewWithConfiguration: WKWebViewConfiguration, forNavigationAction: WKNavigationAction, windowFeatures: WKWindowFeatures) -> WKWebView?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: WKWebView!, createWebViewWithConfiguration configuration: WKWebViewConfiguration!, forNavigationAction navigationAction: WKNavigationAction!, windowFeatures windowFeatures: WKWindowFeatures!) -> WKWebView! ``` | iOS 8.0 |
| To | ``` optional func webView(_ webView: WKWebView, createWebViewWithConfiguration configuration: WKWebViewConfiguration, forNavigationAction navigationAction: WKNavigationAction, windowFeatures windowFeatures: WKWindowFeatures) -> WKWebView? ``` | iOS 8.1 |

Modified WKUIDelegate.webView(WKWebView, runJavaScriptAlertPanelWithMessage: String, initiatedByFrame: WKFrameInfo, completionHandler:() -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: WKWebView!, runJavaScriptAlertPanelWithMessage message: String!, initiatedByFrame frame: WKFrameInfo!, completionHandler completionHandler: (() -> Void)!) ``` | iOS 8.0 |
| To | ``` optional func webView(_ webView: WKWebView, runJavaScriptAlertPanelWithMessage message: String, initiatedByFrame frame: WKFrameInfo, completionHandler completionHandler: () -> Void) ``` | iOS 8.1 |

Modified WKUIDelegate.webView(WKWebView, runJavaScriptConfirmPanelWithMessage: String, initiatedByFrame: WKFrameInfo, completionHandler:(Bool) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: WKWebView!, runJavaScriptConfirmPanelWithMessage message: String!, initiatedByFrame frame: WKFrameInfo!, completionHandler completionHandler: ((Bool) -> Void)!) ``` | iOS 8.0 |
| To | ``` optional func webView(_ webView: WKWebView, runJavaScriptConfirmPanelWithMessage message: String, initiatedByFrame frame: WKFrameInfo, completionHandler completionHandler: (Bool) -> Void) ``` | iOS 8.1 |

Modified WKUIDelegate.webView(WKWebView, runJavaScriptTextInputPanelWithPrompt: String, defaultText: String?, initiatedByFrame: WKFrameInfo, completionHandler:(String!) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: WKWebView!, runJavaScriptTextInputPanelWithPrompt prompt: String!, defaultText defaultText: String!, initiatedByFrame frame: WKFrameInfo!, completionHandler completionHandler: ((String!) -> Void)!) ``` | iOS 8.0 |
| To | ``` optional func webView(_ webView: WKWebView, runJavaScriptTextInputPanelWithPrompt prompt: String, defaultText defaultText: String?, initiatedByFrame frame: WKFrameInfo, completionHandler completionHandler: (String!) -> Void) ``` | iOS 8.1 |

Modified WKUserContentController.addScriptMessageHandler(WKScriptMessageHandler, name: String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func addScriptMessageHandler(_ scriptMessageHandler: WKScriptMessageHandler!, name name: String!) ``` | iOS 8.0 |
| To | ``` func addScriptMessageHandler(_ scriptMessageHandler: WKScriptMessageHandler, name name: String) ``` | iOS 8.1 |

Modified WKUserContentController.addUserScript(WKUserScript)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func addUserScript(_ userScript: WKUserScript!) ``` | iOS 8.0 |
| To | ``` func addUserScript(_ userScript: WKUserScript) ``` | iOS 8.1 |

Modified WKUserContentController.removeScriptMessageHandlerForName(String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func removeScriptMessageHandlerForName(_ name: String!) ``` | iOS 8.0 |
| To | ``` func removeScriptMessageHandlerForName(_ name: String) ``` | iOS 8.1 |

Modified WKUserContentController.userScripts

|  | Declaration |
| --- | --- |
| From | ``` var userScripts: [AnyObject]! { get } ``` |
| To | ``` var userScripts: [AnyObject] { get } ``` |

Modified WKUserScript.source

|  | Declaration |
| --- | --- |
| From | ``` var source: String! { get } ``` |
| To | ``` var source: String { get } ``` |

Modified WKUserScript.init(source: String, injectionTime: WKUserScriptInjectionTime, forMainFrameOnly: Bool)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(source source: String!, injectionTime injectionTime: WKUserScriptInjectionTime, forMainFrameOnly forMainFrameOnly: Bool) ``` | iOS 8.0 |
| To | ``` init(source source: String, injectionTime injectionTime: WKUserScriptInjectionTime, forMainFrameOnly forMainFrameOnly: Bool) ``` | iOS 8.1 |

Modified WKWebView.UIDelegate

|  | Declaration |
| --- | --- |
| From | ``` weak var UIDelegate: WKUIDelegate! ``` |
| To | ``` weak var UIDelegate: WKUIDelegate? ``` |

Modified WKWebView.URL

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var URL: NSURL! { get } ``` |
| To | ``` @NSCopying var URL: NSURL? { get } ``` |

Modified WKWebView.backForwardList

|  | Declaration |
| --- | --- |
| From | ``` var backForwardList: WKBackForwardList! { get } ``` |
| To | ``` var backForwardList: WKBackForwardList { get } ``` |

Modified WKWebView.configuration

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var configuration: WKWebViewConfiguration! { get } ``` |
| To | ``` @NSCopying var configuration: WKWebViewConfiguration { get } ``` |

Modified WKWebView.evaluateJavaScript(String, completionHandler:((AnyObject!, NSError!) -> Void)?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func evaluateJavaScript(_ javaScriptString: String!, completionHandler completionHandler: ((AnyObject!, NSError!) -> Void)!) ``` | iOS 8.0 |
| To | ``` func evaluateJavaScript(_ javaScriptString: String, completionHandler completionHandler: ((AnyObject!, NSError!) -> Void)?) ``` | iOS 8.1 |

Modified WKWebView.init(frame: CGRect, configuration: WKWebViewConfiguration)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(frame frame: CGRect, configuration configuration: WKWebViewConfiguration!) ``` | iOS 8.0 |
| To | ``` init(frame frame: CGRect, configuration configuration: WKWebViewConfiguration) ``` | iOS 8.1 |

Modified WKWebView.goBack() -> WKNavigation?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func goBack() -> WKNavigation! ``` | iOS 8.0 |
| To | ``` func goBack() -> WKNavigation? ``` | iOS 8.1 |

Modified WKWebView.goForward() -> WKNavigation?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func goForward() -> WKNavigation! ``` | iOS 8.0 |
| To | ``` func goForward() -> WKNavigation? ``` | iOS 8.1 |

Modified WKWebView.goToBackForwardListItem(WKBackForwardListItem) -> WKNavigation?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func goToBackForwardListItem(_ item: WKBackForwardListItem!) -> WKNavigation! ``` | iOS 8.0 |
| To | ``` func goToBackForwardListItem(_ item: WKBackForwardListItem) -> WKNavigation? ``` | iOS 8.1 |

Modified WKWebView.loadHTMLString(String, baseURL: NSURL?) -> WKNavigation?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func loadHTMLString(_ string: String!, baseURL baseURL: NSURL!) -> WKNavigation! ``` | iOS 8.0 |
| To | ``` func loadHTMLString(_ string: String, baseURL baseURL: NSURL?) -> WKNavigation? ``` | iOS 8.1 |

Modified WKWebView.loadRequest(NSURLRequest) -> WKNavigation?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func loadRequest(_ request: NSURLRequest!) -> WKNavigation! ``` | iOS 8.0 |
| To | ``` func loadRequest(_ request: NSURLRequest) -> WKNavigation? ``` | iOS 8.1 |

Modified WKWebView.navigationDelegate

|  | Declaration |
| --- | --- |
| From | ``` weak var navigationDelegate: WKNavigationDelegate! ``` |
| To | ``` weak var navigationDelegate: WKNavigationDelegate? ``` |

Modified WKWebView.reload() -> WKNavigation?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func reload() -> WKNavigation! ``` | iOS 8.0 |
| To | ``` func reload() -> WKNavigation? ``` | iOS 8.1 |

Modified WKWebView.reloadFromOrigin() -> WKNavigation?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func reloadFromOrigin() -> WKNavigation! ``` | iOS 8.0 |
| To | ``` func reloadFromOrigin() -> WKNavigation? ``` | iOS 8.1 |

Modified WKWebView.scrollView

|  | Declaration |
| --- | --- |
| From | ``` var scrollView: UIScrollView! { get } ``` |
| To | ``` var scrollView: UIScrollView { get } ``` |

Modified WKWebView.title

|  | Declaration |
| --- | --- |
| From | ``` var title: String! { get } ``` |
| To | ``` var title: String? { get } ``` |

Modified WKWebViewConfiguration.preferences

|  | Declaration |
| --- | --- |
| From | ``` var preferences: WKPreferences! ``` |
| To | ``` var preferences: WKPreferences ``` |

Modified WKWebViewConfiguration.processPool

|  | Declaration |
| --- | --- |
| From | ``` var processPool: WKProcessPool! ``` |
| To | ``` var processPool: WKProcessPool ``` |

Modified WKWebViewConfiguration.userContentController

|  | Declaration |
| --- | --- |
| From | ``` var userContentController: WKUserContentController! ``` |
| To | ``` var userContentController: WKUserContentController ``` |

Modified WKWindowFeatures.allowsResizing

|  | Declaration |
| --- | --- |
| From | ``` var allowsResizing: NSNumber! { get } ``` |
| To | ``` var allowsResizing: NSNumber? { get } ``` |

Modified WKWindowFeatures.height

|  | Declaration |
| --- | --- |
| From | ``` var height: NSNumber! { get } ``` |
| To | ``` var height: NSNumber? { get } ``` |

Modified WKWindowFeatures.menuBarVisibility

|  | Declaration |
| --- | --- |
| From | ``` var menuBarVisibility: NSNumber! { get } ``` |
| To | ``` var menuBarVisibility: NSNumber? { get } ``` |

Modified WKWindowFeatures.statusBarVisibility

|  | Declaration |
| --- | --- |
| From | ``` var statusBarVisibility: NSNumber! { get } ``` |
| To | ``` var statusBarVisibility: NSNumber? { get } ``` |

Modified WKWindowFeatures.toolbarsVisibility

|  | Declaration |
| --- | --- |
| From | ``` var toolbarsVisibility: NSNumber! { get } ``` |
| To | ``` var toolbarsVisibility: NSNumber? { get } ``` |

Modified WKWindowFeatures.width

|  | Declaration |
| --- | --- |
| From | ``` var width: NSNumber! { get } ``` |
| To | ``` var width: NSNumber? { get } ``` |

Modified WKWindowFeatures.x

|  | Declaration |
| --- | --- |
| From | ``` var x: NSNumber! { get } ``` |
| To | ``` var x: NSNumber? { get } ``` |

Modified WKWindowFeatures.y

|  | Declaration |
| --- | --- |
| From | ``` var y: NSNumber! { get } ``` |
| To | ``` var y: NSNumber? { get } ``` |

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
