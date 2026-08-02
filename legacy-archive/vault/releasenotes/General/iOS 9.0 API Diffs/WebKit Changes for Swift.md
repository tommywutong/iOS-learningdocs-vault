---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/WebKit.html
archived_at: '2026-07-18T02:57:04.084140Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# WebKit Changes for Swift

### WebKit

Added [WKErrorCode.JavaScriptResultTypeIsUnsupported](https://developer.apple.com/documentation/webkit/wkerror/code/javascriptresulttypeisunsupported)Added [WKFrameInfo.securityOrigin](https://developer.apple.com/documentation/webkit/wkframeinfo/1503089-securityorigin)Added [WKNavigationDelegate.webViewWebContentProcessDidTerminate(_: WKWebView)](https://developer.apple.com/documentation/webkit/wknavigationdelegate/1455639-webviewwebcontentprocessdidtermi)Added [WKSecurityOrigin](https://developer.apple.com/documentation/webkit/wksecurityorigin)Added [WKSecurityOrigin.host](https://developer.apple.com/documentation/webkit/wksecurityorigin/1536794-host)Added [WKSecurityOrigin.port](https://developer.apple.com/documentation/webkit/wksecurityorigin/1536403-port)Added [WKSecurityOrigin.protocol](https://developer.apple.com/documentation/webkit/wksecurityorigin/1537470-protocol)Added [WKUIDelegate.webViewDidClose(_: WKWebView)](https://developer.apple.com/documentation/webkit/wkuidelegate/1537390-webviewdidclose)Added [WKWebsiteDataRecord](https://developer.apple.com/documentation/webkit/wkwebsitedatarecord)Added [WKWebsiteDataRecord.dataTypes](https://developer.apple.com/documentation/webkit/wkwebsitedatarecord/1538007-datatypes)Added [WKWebsiteDataRecord.displayName](https://developer.apple.com/documentation/webkit/wkwebsitedatarecord/1537733-displayname)Added [WKWebsiteDataStore](https://developer.apple.com/documentation/webkit/wkwebsitedatastore)Added [WKWebsiteDataStore.allWebsiteDataTypes() -> Set<String> [class]](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/1532929-allwebsitedatatypes)Added [WKWebsiteDataStore.defaultDataStore() -> WKWebsiteDataStore [class]](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/1532937-default)Added [WKWebsiteDataStore.fetchDataRecordsOfTypes(_: Set<String>, completionHandler: ([WKWebsiteDataRecord]) -> Void)](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/1532932-fetchdatarecords)Added [WKWebsiteDataStore.nonPersistentDataStore() -> WKWebsiteDataStore [class]](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/1532934-nonpersistentdatastore)Added [WKWebsiteDataStore.persistent](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/1532928-ispersistent)Added [WKWebsiteDataStore.removeDataOfTypes(_: Set<String>, forDataRecords: [WKWebsiteDataRecord], completionHandler: () -> Void)](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/1532936-removedataoftypes)Added [WKWebsiteDataStore.removeDataOfTypes(_: Set<String>, modifiedSince: NSDate, completionHandler: () -> Void)](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/1532938-removedata)Added [WKWebView.allowsLinkPreview](https://developer.apple.com/documentation/webkit/wkwebview/1415000-allowslinkpreview)Added [WKWebView.certificateChain](https://developer.apple.com/documentation/webkit/wkwebview/1414958-certificatechain)Added [WKWebView.customUserAgent](https://developer.apple.com/documentation/webkit/wkwebview/1414950-customuseragent)Added [WKWebView.loadData(_: NSData, MIMEType: String, characterEncodingName: String, baseURL: NSURL) -> WKNavigation?](https://developer.apple.com/documentation/webkit/wkwebview/1415011-load)Added [WKWebView.loadFileURL(_: NSURL, allowingReadAccessToURL: NSURL) -> WKNavigation?](https://developer.apple.com/documentation/webkit/wkwebview/1414973-loadfileurl)Added [WKWebViewConfiguration.allowsAirPlayForMediaPlayback](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1395673-allowsairplayformediaplayback)Added [WKWebViewConfiguration.allowsPictureInPictureMediaPlayback](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1614792-allowspictureinpicturemediaplayb)Added [WKWebViewConfiguration.applicationNameForUserAgent](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1395665-applicationnameforuseragent)Added [WKWebViewConfiguration.requiresUserActionForMediaPlayback](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1614794-requiresuseractionformediaplayba)Added [WKWebViewConfiguration.websiteDataStore](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1395661-websitedatastore)Added [WKWebsiteDataTypeCookies](https://developer.apple.com/documentation/webkit/wkwebsitedatatypecookies)Added [WKWebsiteDataTypeDiskCache](https://developer.apple.com/documentation/webkit/wkwebsitedatatypediskcache)Added [WKWebsiteDataTypeIndexedDBDatabases](https://developer.apple.com/documentation/webkit/wkwebsitedatatypeindexeddbdatabases)Added [WKWebsiteDataTypeLocalStorage](https://developer.apple.com/documentation/webkit/wkwebsitedatatypelocalstorage)Added [WKWebsiteDataTypeMemoryCache](https://developer.apple.com/documentation/webkit/wkwebsitedatatypememorycache)Added [WKWebsiteDataTypeOfflineWebApplicationCache](https://developer.apple.com/documentation/webkit/wkwebsitedatatypeofflinewebapplicationcache)Added [WKWebsiteDataTypeSessionStorage](https://developer.apple.com/documentation/webkit/wkwebsitedatatypesessionstorage)Added [WKWebsiteDataTypeWebSQLDatabases](https://developer.apple.com/documentation/webkit/wkwebsitedatatypewebsqldatabases)Modified [WKBackForwardList](https://developer.apple.com/documentation/webkit/wkbackforwardlist)

|  | Declaration |
| --- | --- |
| From | ``` class WKBackForwardList : NSObject {     var currentItem: WKBackForwardListItem? { get }     var backItem: WKBackForwardListItem? { get }     var forwardItem: WKBackForwardListItem? { get }     func itemAtIndex(_ index: Int) -> WKBackForwardListItem?     var backList: [AnyObject] { get }     var forwardList: [AnyObject] { get } } ``` |
| To | ``` class WKBackForwardList : NSObject {     var currentItem: WKBackForwardListItem? { get }     var backItem: WKBackForwardListItem? { get }     var forwardItem: WKBackForwardListItem? { get }     func itemAtIndex(_ index: Int) -> WKBackForwardListItem?     var backList: [WKBackForwardListItem] { get }     var forwardList: [WKBackForwardListItem] { get } } ``` |

Modified [WKBackForwardList.backList](https://developer.apple.com/documentation/webkit/wkbackforwardlist/1516698-backlist)

|  | Declaration |
| --- | --- |
| From | ``` var backList: [AnyObject] { get } ``` |
| To | ``` var backList: [WKBackForwardListItem] { get } ``` |

Modified [WKBackForwardList.forwardList](https://developer.apple.com/documentation/webkit/wkbackforwardlist/1516701-forwardlist)

|  | Declaration |
| --- | --- |
| From | ``` var forwardList: [AnyObject] { get } ``` |
| To | ``` var forwardList: [WKBackForwardListItem] { get } ``` |

Modified [WKErrorCode [enum]](https://developer.apple.com/documentation/webkit/wkerrorcode)

|  | Declaration | Protocols | Raw Value Type |
| --- | --- | --- | --- |
| From | ``` enum WKErrorCode : Int {     case Unknown     case WebContentProcessTerminated     case WebViewInvalidated     case JavaScriptExceptionOccurred } ``` | Equatable, Hashable, RawRepresentable | -- |
| To | ``` enum WKErrorCode : Int {     case Unknown     case WebContentProcessTerminated     case WebViewInvalidated     case JavaScriptExceptionOccurred     case JavaScriptResultTypeIsUnsupported } extension WKErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension WKErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable | Int |

Modified [WKFrameInfo](https://developer.apple.com/documentation/webkit/wkframeinfo)

|  | Declaration |
| --- | --- |
| From | ``` class WKFrameInfo : NSObject, NSCopying {     var mainFrame: Bool { get }     @NSCopying var request: NSURLRequest { get } } ``` |
| To | ``` class WKFrameInfo : NSObject, NSCopying {     var mainFrame: Bool { get }     @NSCopying var request: NSURLRequest { get }     var securityOrigin: WKSecurityOrigin { get } } ``` |

Modified [WKNavigationAction](https://developer.apple.com/documentation/webkit/wknavigationaction)

|  | Declaration |
| --- | --- |
| From | ``` class WKNavigationAction : NSObject {     @NSCopying var sourceFrame: WKFrameInfo? { get }     @NSCopying var targetFrame: WKFrameInfo? { get }     var navigationType: WKNavigationType { get }     @NSCopying var request: NSURLRequest { get } } ``` |
| To | ``` class WKNavigationAction : NSObject {     @NSCopying var sourceFrame: WKFrameInfo { get }     @NSCopying var targetFrame: WKFrameInfo? { get }     var navigationType: WKNavigationType { get }     @NSCopying var request: NSURLRequest { get } } ``` |

Modified [WKNavigationAction.sourceFrame](https://developer.apple.com/documentation/webkit/wknavigationaction/1401926-sourceframe)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var sourceFrame: WKFrameInfo? { get } ``` |
| To | ``` @NSCopying var sourceFrame: WKFrameInfo { get } ``` |

Modified [WKNavigationActionPolicy [enum]](https://developer.apple.com/documentation/webkit/wknavigationactionpolicy)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [WKNavigationDelegate](https://developer.apple.com/documentation/webkit/wknavigationdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol WKNavigationDelegate : NSObjectProtocol {     optional func webView(_ webView: WKWebView, decidePolicyForNavigationAction navigationAction: WKNavigationAction, decisionHandler decisionHandler: (WKNavigationActionPolicy) -> Void)     optional func webView(_ webView: WKWebView, decidePolicyForNavigationResponse navigationResponse: WKNavigationResponse, decisionHandler decisionHandler: (WKNavigationResponsePolicy) -> Void)     optional func webView(_ webView: WKWebView, didStartProvisionalNavigation navigation: WKNavigation!)     optional func webView(_ webView: WKWebView, didReceiveServerRedirectForProvisionalNavigation navigation: WKNavigation!)     optional func webView(_ webView: WKWebView, didFailProvisionalNavigation navigation: WKNavigation!, withError error: NSError)     optional func webView(_ webView: WKWebView, didCommitNavigation navigation: WKNavigation!)     optional func webView(_ webView: WKWebView, didFinishNavigation navigation: WKNavigation!)     optional func webView(_ webView: WKWebView, didFailNavigation navigation: WKNavigation!, withError error: NSError)     optional func webView(_ webView: WKWebView, didReceiveAuthenticationChallenge challenge: NSURLAuthenticationChallenge, completionHandler completionHandler: (NSURLSessionAuthChallengeDisposition, NSURLCredential!) -> Void) } ``` |
| To | ``` protocol WKNavigationDelegate : NSObjectProtocol {     optional func webView(_ webView: WKWebView, decidePolicyForNavigationAction navigationAction: WKNavigationAction, decisionHandler decisionHandler: (WKNavigationActionPolicy) -> Void)     optional func webView(_ webView: WKWebView, decidePolicyForNavigationResponse navigationResponse: WKNavigationResponse, decisionHandler decisionHandler: (WKNavigationResponsePolicy) -> Void)     optional func webView(_ webView: WKWebView, didStartProvisionalNavigation navigation: WKNavigation!)     optional func webView(_ webView: WKWebView, didReceiveServerRedirectForProvisionalNavigation navigation: WKNavigation!)     optional func webView(_ webView: WKWebView, didFailProvisionalNavigation navigation: WKNavigation!, withError error: NSError)     optional func webView(_ webView: WKWebView, didCommitNavigation navigation: WKNavigation!)     optional func webView(_ webView: WKWebView, didFinishNavigation navigation: WKNavigation!)     optional func webView(_ webView: WKWebView, didFailNavigation navigation: WKNavigation!, withError error: NSError)     optional func webView(_ webView: WKWebView, didReceiveAuthenticationChallenge challenge: NSURLAuthenticationChallenge, completionHandler completionHandler: (NSURLSessionAuthChallengeDisposition, NSURLCredential?) -> Void)     optional func webViewWebContentProcessDidTerminate(_ webView: WKWebView) } ``` |

Modified [WKNavigationDelegate.webView(_: WKWebView, didReceiveAuthenticationChallenge: NSURLAuthenticationChallenge, completionHandler: (NSURLSessionAuthChallengeDisposition, NSURLCredential?) -> Void)](https://developer.apple.com/documentation/webkit/wknavigationdelegate/1455638-webview)

|  | Declaration |
| --- | --- |
| From | ``` optional func webView(_ webView: WKWebView, didReceiveAuthenticationChallenge challenge: NSURLAuthenticationChallenge, completionHandler completionHandler: (NSURLSessionAuthChallengeDisposition, NSURLCredential!) -> Void) ``` |
| To | ``` optional func webView(_ webView: WKWebView, didReceiveAuthenticationChallenge challenge: NSURLAuthenticationChallenge, completionHandler completionHandler: (NSURLSessionAuthChallengeDisposition, NSURLCredential?) -> Void) ``` |

Modified [WKNavigationResponsePolicy [enum]](https://developer.apple.com/documentation/webkit/wknavigationresponsepolicy)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [WKNavigationType [enum]](https://developer.apple.com/documentation/webkit/wknavigationtype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [WKSelectionGranularity [enum]](https://developer.apple.com/documentation/webkit/wkselectiongranularity)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [WKUIDelegate](https://developer.apple.com/documentation/webkit/wkuidelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol WKUIDelegate : NSObjectProtocol {     optional func webView(_ webView: WKWebView, createWebViewWithConfiguration configuration: WKWebViewConfiguration, forNavigationAction navigationAction: WKNavigationAction, windowFeatures windowFeatures: WKWindowFeatures) -> WKWebView?     optional func webView(_ webView: WKWebView, runJavaScriptAlertPanelWithMessage message: String, initiatedByFrame frame: WKFrameInfo, completionHandler completionHandler: () -> Void)     optional func webView(_ webView: WKWebView, runJavaScriptConfirmPanelWithMessage message: String, initiatedByFrame frame: WKFrameInfo, completionHandler completionHandler: (Bool) -> Void)     optional func webView(_ webView: WKWebView, runJavaScriptTextInputPanelWithPrompt prompt: String, defaultText defaultText: String?, initiatedByFrame frame: WKFrameInfo, completionHandler completionHandler: (String!) -> Void) } ``` |
| To | ``` protocol WKUIDelegate : NSObjectProtocol {     optional func webView(_ webView: WKWebView, createWebViewWithConfiguration configuration: WKWebViewConfiguration, forNavigationAction navigationAction: WKNavigationAction, windowFeatures windowFeatures: WKWindowFeatures) -> WKWebView?     optional func webViewDidClose(_ webView: WKWebView)     optional func webView(_ webView: WKWebView, runJavaScriptAlertPanelWithMessage message: String, initiatedByFrame frame: WKFrameInfo, completionHandler completionHandler: () -> Void)     optional func webView(_ webView: WKWebView, runJavaScriptConfirmPanelWithMessage message: String, initiatedByFrame frame: WKFrameInfo, completionHandler completionHandler: (Bool) -> Void)     optional func webView(_ webView: WKWebView, runJavaScriptTextInputPanelWithPrompt prompt: String, defaultText defaultText: String?, initiatedByFrame frame: WKFrameInfo, completionHandler completionHandler: (String?) -> Void) } ``` |

Modified [WKUIDelegate.webView(_: WKWebView, runJavaScriptTextInputPanelWithPrompt: String, defaultText: String?, initiatedByFrame: WKFrameInfo, completionHandler: (String?) -> Void)](https://developer.apple.com/documentation/webkit/wkuidelegate/1538086-webview)

|  | Declaration |
| --- | --- |
| From | ``` optional func webView(_ webView: WKWebView, runJavaScriptTextInputPanelWithPrompt prompt: String, defaultText defaultText: String?, initiatedByFrame frame: WKFrameInfo, completionHandler completionHandler: (String!) -> Void) ``` |
| To | ``` optional func webView(_ webView: WKWebView, runJavaScriptTextInputPanelWithPrompt prompt: String, defaultText defaultText: String?, initiatedByFrame frame: WKFrameInfo, completionHandler completionHandler: (String?) -> Void) ``` |

Modified [WKUserContentController](https://developer.apple.com/documentation/webkit/wkusercontentcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class WKUserContentController : NSObject {     var userScripts: [AnyObject] { get }     func addUserScript(_ userScript: WKUserScript)     func removeAllUserScripts()     func addScriptMessageHandler(_ scriptMessageHandler: WKScriptMessageHandler, name name: String)     func removeScriptMessageHandlerForName(_ name: String) } ``` |
| To | ``` class WKUserContentController : NSObject {     var userScripts: [WKUserScript] { get }     func addUserScript(_ userScript: WKUserScript)     func removeAllUserScripts()     func addScriptMessageHandler(_ scriptMessageHandler: WKScriptMessageHandler, name name: String)     func removeScriptMessageHandlerForName(_ name: String) } ``` |

Modified [WKUserContentController.userScripts](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/1538046-userscripts)

|  | Declaration |
| --- | --- |
| From | ``` var userScripts: [AnyObject] { get } ``` |
| To | ``` var userScripts: [WKUserScript] { get } ``` |

Modified [WKUserScriptInjectionTime [enum]](https://developer.apple.com/documentation/webkit/wkuserscriptinjectiontime)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [WKWebView](https://developer.apple.com/documentation/webkit/wkwebview)

|  | Declaration |
| --- | --- |
| From | ``` class WKWebView : UIView {     @NSCopying var configuration: WKWebViewConfiguration { get }     weak var navigationDelegate: WKNavigationDelegate?     weak var UIDelegate: WKUIDelegate?     var backForwardList: WKBackForwardList { get }     init(frame frame: CGRect, configuration configuration: WKWebViewConfiguration)     convenience init!(coder coder: NSCoder!)     func loadRequest(_ request: NSURLRequest) -> WKNavigation?     func loadHTMLString(_ string: String, baseURL baseURL: NSURL?) -> WKNavigation?     func goToBackForwardListItem(_ item: WKBackForwardListItem) -> WKNavigation?     var title: String? { get }     @NSCopying var URL: NSURL? { get }     var loading: Bool { get }     var estimatedProgress: Double { get }     var hasOnlySecureContent: Bool { get }     var canGoBack: Bool { get }     var canGoForward: Bool { get }     func goBack() -> WKNavigation?     func goForward() -> WKNavigation?     func reload() -> WKNavigation?     func reloadFromOrigin() -> WKNavigation?     func stopLoading()     func evaluateJavaScript(_ javaScriptString: String, completionHandler completionHandler: ((AnyObject!, NSError!) -> Void)?)     var allowsBackForwardNavigationGestures: Bool     var scrollView: UIScrollView { get } } ``` |
| To | ``` class WKWebView : UIView {     @NSCopying var configuration: WKWebViewConfiguration { get }     weak var navigationDelegate: WKNavigationDelegate?     weak var UIDelegate: WKUIDelegate?     var backForwardList: WKBackForwardList { get }     init(frame frame: CGRect, configuration configuration: WKWebViewConfiguration)     convenience init(coder coder: NSCoder)     func loadRequest(_ request: NSURLRequest) -> WKNavigation?     func loadFileURL(_ URL: NSURL, allowingReadAccessToURL readAccessURL: NSURL) -> WKNavigation?     func loadHTMLString(_ string: String, baseURL baseURL: NSURL?) -> WKNavigation?     func loadData(_ data: NSData, MIMEType MIMEType: String, characterEncodingName characterEncodingName: String, baseURL baseURL: NSURL) -> WKNavigation?     func goToBackForwardListItem(_ item: WKBackForwardListItem) -> WKNavigation?     var title: String? { get }     @NSCopying var URL: NSURL? { get }     var loading: Bool { get }     var estimatedProgress: Double { get }     var hasOnlySecureContent: Bool { get }     var certificateChain: [AnyObject] { get }     var canGoBack: Bool { get }     var canGoForward: Bool { get }     func goBack() -> WKNavigation?     func goForward() -> WKNavigation?     func reload() -> WKNavigation?     func reloadFromOrigin() -> WKNavigation?     func stopLoading()     func evaluateJavaScript(_ javaScriptString: String, completionHandler completionHandler: ((AnyObject?, NSError?) -> Void)?)     var allowsBackForwardNavigationGestures: Bool     var customUserAgent: String?     var allowsLinkPreview: Bool     var scrollView: UIScrollView { get } } ``` |

Modified [WKWebView.evaluateJavaScript(_: String, completionHandler: ((AnyObject?, NSError?) -> Void)?)](https://developer.apple.com/documentation/webkit/wkwebview/1415017-evaluatejavascript)

|  | Declaration |
| --- | --- |
| From | ``` func evaluateJavaScript(_ javaScriptString: String, completionHandler completionHandler: ((AnyObject!, NSError!) -> Void)?) ``` |
| To | ``` func evaluateJavaScript(_ javaScriptString: String, completionHandler completionHandler: ((AnyObject?, NSError?) -> Void)?) ``` |

Modified [WKWebViewConfiguration](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` class WKWebViewConfiguration : NSObject, NSCopying {     var processPool: WKProcessPool     var preferences: WKPreferences     var userContentController: WKUserContentController     var suppressesIncrementalRendering: Bool     var allowsInlineMediaPlayback: Bool     var mediaPlaybackRequiresUserAction: Bool     var mediaPlaybackAllowsAirPlay: Bool     var selectionGranularity: WKSelectionGranularity } ``` |
| To | ``` class WKWebViewConfiguration : NSObject, NSCopying {     var processPool: WKProcessPool     var preferences: WKPreferences     var userContentController: WKUserContentController     var websiteDataStore: WKWebsiteDataStore     var suppressesIncrementalRendering: Bool     var applicationNameForUserAgent: String?     var allowsAirPlayForMediaPlayback: Bool     var allowsInlineMediaPlayback: Bool     var requiresUserActionForMediaPlayback: Bool     var selectionGranularity: WKSelectionGranularity     var allowsPictureInPictureMediaPlayback: Bool } extension WKWebViewConfiguration {     var mediaPlaybackRequiresUserAction: Bool     var mediaPlaybackAllowsAirPlay: Bool } ``` |

Modified [WKWebViewConfiguration.mediaPlaybackAllowsAirPlay](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1614726-mediaplaybackallowsairplay)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [WKWebViewConfiguration.mediaPlaybackRequiresUserAction](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1614727-mediaplaybackrequiresuseraction)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

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
