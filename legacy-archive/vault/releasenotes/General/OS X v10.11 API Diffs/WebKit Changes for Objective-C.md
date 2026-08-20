---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/WebKit.html
archived_at: '2026-07-18T02:53:14.731373Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# WebKit Changes for Objective-C

### WebKit

#### DOMCSSRule.h

Added [DOM_KEYFRAME_RULE](https://developer.apple.com/documentation/webkit/dom_keyframe_rule)Added [DOM_KEYFRAMES_RULE](https://developer.apple.com/documentation/webkit/dom_keyframes_rule)Added [DOM_SUPPORTS_RULE](https://developer.apple.com/documentation/webkit/1403866-dom_rule_enumeration_legacy/dom_supports_rule)

#### DOMDocument.h

Modified [-[DOMDocument getElementsByClassName:]](https://developer.apple.com/documentation/webkit/domdocument/1494910-getelementsbyclassname)

|  | Declaration |
| --- | --- |
| From | ``` - (DOMNodeList *)getElementsByClassName:(NSString *)tagname ``` |
| To | ``` - (DOMNodeList *)getElementsByClassName:(NSString *)classNames ``` |

#### DOMElement.h

Added [DOMElement.innerHTML](https://developer.apple.com/documentation/webkit/domelement/1476181-innerhtml)Added [DOMElement.outerHTML](https://developer.apple.com/documentation/webkit/domelement/1476260-outerhtml)

#### DOMEventListener.h

Modified [-[DOMEventListener handleEvent:]](https://developer.apple.com/documentation/webkit/domeventlistener/1385523-handle)

|  | Declaration |
| --- | --- |
| From | ``` - (void)handleEvent:(DOMEvent *)evt ``` |
| To | ``` - (void)handleEvent:(DOMEvent *)event ``` |

#### DOMHTMLElement.h

Removed DOMHTMLElement.innerHTMLRemoved DOMHTMLElement.outerHTML

#### DOMMutationEvent.h

Added [-[DOMMutationEvent newValue]](https://developer.apple.com/documentation/webkit/dommutationevent/1393672-newvalue)Modified [DOMMutationEvent.newValue](https://developer.apple.com/documentation/webkit/dommutationevent/1393658-newvalue)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.5 |

#### DOMNotation.h (Removed)

Removed DOMNotationRemoved DOMNotation.publicIdRemoved DOMNotation.systemId

#### npapi.h

Added [NPN_HandleEvent()](https://developer.apple.com/documentation/webkit/1444134-npn_handleevent)Added [NPN_UnfocusInstance()](https://developer.apple.com/documentation/webkit/1443977-npn_unfocusinstance)Added [NPN_URLRedirectResponse()](https://developer.apple.com/documentation/webkit/1444093-npn_urlredirectresponse)Added [NPNVmuteAudioBool](https://developer.apple.com/documentation/webkit/npnvariable/npnvmuteaudiobool)Added [NPPVpluginIsPlayingAudio](https://developer.apple.com/documentation/webkit/nppvariable/nppvpluginisplayingaudio)

#### npfunctions.h

Added [NPN_HandleEventPtr](https://developer.apple.com/documentation/webkit/npn_handleeventptr)Added [NPN_UnfocusInstancePtr](https://developer.apple.com/documentation/webkit/npn_unfocusinstanceptr)Added [NPN_URLRedirectResponsePtr](https://developer.apple.com/documentation/webkit/npn_urlredirectresponseptr)

#### WebDownload.h

Removed NSObject(WebDownloadDelegate)Added [WebDownloadDelegate](https://developer.apple.com/documentation/webkit/webdownloaddelegate)Modified [-[WebDownloadDelegate downloadWindowForAuthenticationSheet:]](https://developer.apple.com/documentation/webkit/webdownloaddelegate/1537616-downloadwindowforauthentications)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

#### WebEditingDelegate.h

Removed NSObject(WebViewEditingDelegate)Added [WebEditingDelegate](https://developer.apple.com/documentation/webkit/webeditingdelegate)Added NSObject(WebEditingDelegate)

#### WebFrameLoadDelegate.h

Removed NSObject(WebFrameLoadDelegate)Added [WebFrameLoadDelegate](https://developer.apple.com/documentation/webkit/webframeloaddelegate)Modified [-[WebFrameLoadDelegate webView:didCancelClientRedirectForFrame:]](https://developer.apple.com/documentation/webkit/webframeloaddelegate/1501453-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebFrameLoadDelegate webView:didChangeLocationWithinPageForFrame:]](https://developer.apple.com/documentation/webkit/webframeloaddelegate/1501461-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebFrameLoadDelegate webView:didClearWindowObject:forFrame:]](https://developer.apple.com/documentation/webkit/webframeloaddelegate/1501445-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebFrameLoadDelegate webView:didCommitLoadForFrame:]](https://developer.apple.com/documentation/webkit/webframeloaddelegate/1501446-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebFrameLoadDelegate webView:didCreateJavaScriptContext:forFrame:]](https://developer.apple.com/documentation/webkit/webframeloaddelegate/1501462-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebFrameLoadDelegate webView:didFailLoadWithError:forFrame:]](https://developer.apple.com/documentation/webkit/webframeloaddelegate/1501443-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebFrameLoadDelegate webView:didFailProvisionalLoadWithError:forFrame:]](https://developer.apple.com/documentation/webkit/webframeloaddelegate/1501459-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebFrameLoadDelegate webView:didFinishLoadForFrame:]](https://developer.apple.com/documentation/webkit/webframeloaddelegate/1501444-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebFrameLoadDelegate webView:didReceiveIcon:forFrame:]](https://developer.apple.com/documentation/webkit/webframeloaddelegate/1501463-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebFrameLoadDelegate webView:didReceiveServerRedirectForProvisionalLoadForFrame:]](https://developer.apple.com/documentation/webkit/webframeloaddelegate/1501449-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebFrameLoadDelegate webView:didReceiveTitle:forFrame:]](https://developer.apple.com/documentation/webkit/webframeloaddelegate/1501450-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebFrameLoadDelegate webView:didStartProvisionalLoadForFrame:]](https://developer.apple.com/documentation/webkit/webframeloaddelegate/1501458-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebFrameLoadDelegate webView:willCloseFrame:]](https://developer.apple.com/documentation/webkit/webframeloaddelegate/1501455-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebFrameLoadDelegate webView:willPerformClientRedirectToURL:delay:fireDate:forFrame:]](https://developer.apple.com/documentation/webkit/webframeloaddelegate/1501451-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebFrameLoadDelegate webView:windowScriptObjectAvailable:]](https://developer.apple.com/documentation/webkit/webframeloaddelegate/1501448-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

#### WebPolicyDelegate.h

Removed NSObject(WebPolicyDelegate)Added [WebPolicyDelegate](https://developer.apple.com/documentation/webkit/webpolicydelegate)Modified [-[WebPolicyDelegate webView:decidePolicyForMIMEType:request:frame:decisionListener:]](https://developer.apple.com/documentation/webkit/webpolicydelegate/1537639-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebPolicyDelegate webView:decidePolicyForNavigationAction:request:frame:decisionListener:]](https://developer.apple.com/documentation/webkit/webpolicydelegate/1536273-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebPolicyDelegate webView:decidePolicyForNewWindowAction:request:newFrameName:decisionListener:]](https://developer.apple.com/documentation/webkit/webpolicydelegate/1536381-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebPolicyDelegate webView:unableToImplementPolicyWithError:frame:]](https://developer.apple.com/documentation/webkit/webpolicydelegate/1537683-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

#### WebPreferences.h

Added [WebPreferences.allowsAirPlayForMediaPlayback](https://developer.apple.com/documentation/webkit/webpreferences/1537474-allowsairplayformediaplayback)

#### WebResourceLoadDelegate.h

Removed NSObject(WebResourceLoadDelegate)Added [WebResourceLoadDelegate](https://developer.apple.com/documentation/webkit/webresourceloaddelegate)Modified [-[WebResourceLoadDelegate webView:identifierForInitialRequest:fromDataSource:]](https://developer.apple.com/documentation/webkit/webresourceloaddelegate/1536504-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebResourceLoadDelegate webView:plugInFailedWithError:dataSource:]](https://developer.apple.com/documentation/webkit/webresourceloaddelegate/1537028-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebResourceLoadDelegate webView:resource:didCancelAuthenticationChallenge:fromDataSource:]](https://developer.apple.com/documentation/webkit/webresourceloaddelegate/1537423-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebResourceLoadDelegate webView:resource:didFailLoadingWithError:fromDataSource:]](https://developer.apple.com/documentation/webkit/webresourceloaddelegate/1537843-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebResourceLoadDelegate webView:resource:didFinishLoadingFromDataSource:]](https://developer.apple.com/documentation/webkit/webresourceloaddelegate/1537418-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebResourceLoadDelegate webView:resource:didReceiveAuthenticationChallenge:fromDataSource:]](https://developer.apple.com/documentation/webkit/webresourceloaddelegate/1537599-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebResourceLoadDelegate webView:resource:didReceiveContentLength:fromDataSource:]](https://developer.apple.com/documentation/webkit/webresourceloaddelegate/1537519-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebResourceLoadDelegate webView:resource:didReceiveResponse:fromDataSource:]](https://developer.apple.com/documentation/webkit/webresourceloaddelegate/1536493-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebResourceLoadDelegate webView:resource:willSendRequest:redirectResponse:fromDataSource:]](https://developer.apple.com/documentation/webkit/webresourceloaddelegate/1537200-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

#### WebUIDelegate.h

Removed NSObject(WebUIDelegate)Added [WebUIDelegate](https://developer.apple.com/documentation/webkit/webuidelegate)Modified [-[WebUIDelegate webView:contextMenuItemsForElement:defaultMenuItems:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387728-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:createWebViewModalDialogWithRequest:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387789-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:createWebViewWithRequest:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387785-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:dragDestinationActionMaskForDraggingInfo:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387848-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:dragSourceActionMaskForPoint:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387830-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:drawFooterInRect:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387707-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:drawHeaderInRect:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387852-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:makeFirstResponder:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387824-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:mouseDidMoveOverElement:modifierFlags:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387779-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:printFrameView:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387787-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:runBeforeUnloadConfirmPanelWithMessage:initiatedByFrame:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387844-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:runJavaScriptAlertPanelWithMessage:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387807-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:runJavaScriptAlertPanelWithMessage:initiatedByFrame:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387846-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:runJavaScriptConfirmPanelWithMessage:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387864-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:runJavaScriptConfirmPanelWithMessage:initiatedByFrame:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387763-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:runJavaScriptTextInputPanelWithPrompt:defaultText:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387836-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:runJavaScriptTextInputPanelWithPrompt:defaultText:initiatedByFrame:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387732-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:runOpenPanelForFileButtonWithResultListener:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387793-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:runOpenPanelForFileButtonWithResultListener:allowMultipleFiles:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387756-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:setContentRect:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387805-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:setFrame:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387783-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:setResizable:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387758-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:setStatusBarVisible:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387826-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:setStatusText:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387717-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:setToolbarsVisible:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387742-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:shouldPerformAction:fromSender:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387701-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:validateUserInterfaceItem:defaultValidation:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387693-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:willPerformDragDestinationAction:forDraggingInfo:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387876-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webView:willPerformDragSourceAction:fromPoint:withPasteboard:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387842-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webViewAreToolbarsVisible:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387834-webviewaretoolbarsvisible)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webViewClose:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387777-webviewclose)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webViewContentRect:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387760-webviewcontentrect)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webViewFirstResponder:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387703-webviewfirstresponder)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webViewFocus:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387723-webviewfocus)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webViewFooterHeight:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387840-webviewfooterheight)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webViewFrame:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387746-webviewframe)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webViewHeaderHeight:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387820-webviewheaderheight)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webViewIsResizable:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387854-webviewisresizable)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webViewIsStatusBarVisible:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387801-webviewisstatusbarvisible)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webViewRunModal:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387815-webviewrunmodal)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webViewShow:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387822-webviewshow)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webViewStatusText:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387711-webviewstatustext)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[WebUIDelegate webViewUnfocus:]](https://developer.apple.com/documentation/webkit/webuidelegate/1387791-webviewunfocus)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

#### WebView.h

Modified [WebView.downloadDelegate](https://developer.apple.com/documentation/webkit/webview/1408536-downloaddelegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id downloadDelegate ``` |
| To | ``` @property(nonatomic, assign) id<WebDownloadDelegate> downloadDelegate ``` |

Modified [WebView.frameLoadDelegate](https://developer.apple.com/documentation/webkit/webview/1408540-frameloaddelegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id frameLoadDelegate ``` |
| To | ``` @property(nonatomic, assign) id<WebFrameLoadDelegate> frameLoadDelegate ``` |

Modified [WebView.policyDelegate](https://developer.apple.com/documentation/webkit/webview/1408391-policydelegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id policyDelegate ``` |
| To | ``` @property(nonatomic, assign) id<WebPolicyDelegate> policyDelegate ``` |

Modified [WebView.resourceLoadDelegate](https://developer.apple.com/documentation/webkit/webview/1408367-resourceloaddelegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id resourceLoadDelegate ``` |
| To | ``` @property(nonatomic, assign) id<WebResourceLoadDelegate> resourceLoadDelegate ``` |

Modified [WebView.UIDelegate](https://developer.apple.com/documentation/webkit/webview/1408544-uidelegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id UIDelegate ``` |
| To | ``` @property(nonatomic, assign) id<WebUIDelegate> UIDelegate ``` |

#### WKBackForwardList.h

Modified [WKBackForwardList.backItem](https://developer.apple.com/documentation/webkit/wkbackforwardlist/1516693-backitem)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, strong) WKBackForwardListItem *backItem ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) WKBackForwardListItem *backItem ``` |

Modified [WKBackForwardList.backList](https://developer.apple.com/documentation/webkit/wkbackforwardlist/1516698-backlist)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *backList ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSArray<WKBackForwardListItem *> *backList ``` |

Modified [WKBackForwardList.currentItem](https://developer.apple.com/documentation/webkit/wkbackforwardlist/1516703-currentitem)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, strong) WKBackForwardListItem *currentItem ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) WKBackForwardListItem *currentItem ``` |

Modified [WKBackForwardList.forwardItem](https://developer.apple.com/documentation/webkit/wkbackforwardlist/1516700-forwarditem)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, strong) WKBackForwardListItem *forwardItem ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) WKBackForwardListItem *forwardItem ``` |

Modified [WKBackForwardList.forwardList](https://developer.apple.com/documentation/webkit/wkbackforwardlist/1516701-forwardlist)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *forwardList ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSArray<WKBackForwardListItem *> *forwardList ``` |

Modified [-[WKBackForwardList itemAtIndex:]](https://developer.apple.com/documentation/webkit/wkbackforwardlist/1516694-item)

|  | Declaration |
| --- | --- |
| From | ``` - (WKBackForwardListItem *)itemAtIndex:(NSInteger)index ``` |
| To | ``` - (WKBackForwardListItem * _Nullable)itemAtIndex:(NSInteger)index ``` |

#### WKBackForwardListItem.h

Modified [WKBackForwardListItem.initialURL](https://developer.apple.com/documentation/webkit/wkbackforwardlistitem/1455507-initialurl)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSURL *initialURL ``` |
| To | ``` @property(readonly, copy, nonnull) NSURL *initialURL ``` |

Modified [WKBackForwardListItem.title](https://developer.apple.com/documentation/webkit/wkbackforwardlistitem/1455511-title)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *title ``` |
| To | ``` @property(readonly, copy, nullable) NSString *title ``` |

Modified [WKBackForwardListItem.URL](https://developer.apple.com/documentation/webkit/wkbackforwardlistitem/1455513-url)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSURL *URL ``` |
| To | ``` @property(readonly, copy, nonnull) NSURL *URL ``` |

#### WKError.h

Added [WKErrorJavaScriptResultTypeIsUnsupported](https://developer.apple.com/documentation/webkit/wkerrorcode/wkerrorjavascriptresulttypeisunsupported)

#### WKFrameInfo.h

Added [WKFrameInfo.securityOrigin](https://developer.apple.com/documentation/webkit/wkframeinfo/1503089-securityorigin)Modified [WKFrameInfo.request](https://developer.apple.com/documentation/webkit/wkframeinfo/1503091-request)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSURLRequest *request ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSURLRequest *request ``` |

#### WKNavigationAction.h

Modified [WKNavigationAction.request](https://developer.apple.com/documentation/webkit/wknavigationaction/1401910-request)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSURLRequest *request ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSURLRequest *request ``` |

Modified [WKNavigationAction.sourceFrame](https://developer.apple.com/documentation/webkit/wknavigationaction/1401926-sourceframe)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) WKFrameInfo *sourceFrame ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) WKFrameInfo *sourceFrame ``` |

Modified [WKNavigationAction.targetFrame](https://developer.apple.com/documentation/webkit/wknavigationaction/1401918-targetframe)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) WKFrameInfo *targetFrame ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) WKFrameInfo *targetFrame ``` |

#### WKNavigationDelegate.h

Added [-[WKNavigationDelegate webViewWebContentProcessDidTerminate:]](https://developer.apple.com/documentation/webkit/wknavigationdelegate/1455639-webviewwebcontentprocessdidtermi)Modified [-[WKNavigationDelegate webView:decidePolicyForNavigationAction:decisionHandler:]](https://developer.apple.com/documentation/webkit/wknavigationdelegate/1455641-webview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)webView:(WKWebView *)webView decidePolicyForNavigationAction:(WKNavigationAction *)navigationAction decisionHandler:(void (^)(WKNavigationActionPolicy))decisionHandler ``` |
| To | ``` - (void)webView:(WKWebView * _Nonnull)webView decidePolicyForNavigationAction:(WKNavigationAction * _Nonnull)navigationAction decisionHandler:(void (^ _Nonnull)(WKNavigationActionPolicy))decisionHandler ``` |

Modified [-[WKNavigationDelegate webView:decidePolicyForNavigationResponse:decisionHandler:]](https://developer.apple.com/documentation/webkit/wknavigationdelegate/1455643-webview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)webView:(WKWebView *)webView decidePolicyForNavigationResponse:(WKNavigationResponse *)navigationResponse decisionHandler:(void (^)(WKNavigationResponsePolicy))decisionHandler ``` |
| To | ``` - (void)webView:(WKWebView * _Nonnull)webView decidePolicyForNavigationResponse:(WKNavigationResponse * _Nonnull)navigationResponse decisionHandler:(void (^ _Nonnull)(WKNavigationResponsePolicy))decisionHandler ``` |

Modified [-[WKNavigationDelegate webView:didCommitNavigation:]](https://developer.apple.com/documentation/webkit/wknavigationdelegate/1455635-webview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)webView:(WKWebView *)webView didCommitNavigation:(WKNavigation *)navigation ``` |
| To | ``` - (void)webView:(WKWebView * _Nonnull)webView didCommitNavigation:(WKNavigation * _Null_unspecified)navigation ``` |

Modified [-[WKNavigationDelegate webView:didFailNavigation:withError:]](https://developer.apple.com/documentation/webkit/wknavigationdelegate/1455623-webview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)webView:(WKWebView *)webView didFailNavigation:(WKNavigation *)navigation withError:(NSError *)error ``` |
| To | ``` - (void)webView:(WKWebView * _Nonnull)webView didFailNavigation:(WKNavigation * _Null_unspecified)navigation withError:(NSError * _Nonnull)error ``` |

Modified [-[WKNavigationDelegate webView:didFailProvisionalNavigation:withError:]](https://developer.apple.com/documentation/webkit/wknavigationdelegate/1455637-webview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)webView:(WKWebView *)webView didFailProvisionalNavigation:(WKNavigation *)navigation withError:(NSError *)error ``` |
| To | ``` - (void)webView:(WKWebView * _Nonnull)webView didFailProvisionalNavigation:(WKNavigation * _Null_unspecified)navigation withError:(NSError * _Nonnull)error ``` |

Modified [-[WKNavigationDelegate webView:didFinishNavigation:]](https://developer.apple.com/documentation/webkit/wknavigationdelegate/1455629-webview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)webView:(WKWebView *)webView didFinishNavigation:(WKNavigation *)navigation ``` |
| To | ``` - (void)webView:(WKWebView * _Nonnull)webView didFinishNavigation:(WKNavigation * _Null_unspecified)navigation ``` |

Modified [-[WKNavigationDelegate webView:didReceiveAuthenticationChallenge:completionHandler:]](https://developer.apple.com/documentation/webkit/wknavigationdelegate/1455638-webview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)webView:(WKWebView *)webView didReceiveAuthenticationChallenge:(NSURLAuthenticationChallenge *)challenge completionHandler:(void (^)(NSURLSessionAuthChallengeDisposition disposition, NSURLCredential *credential))completionHandler ``` |
| To | ``` - (void)webView:(WKWebView * _Nonnull)webView didReceiveAuthenticationChallenge:(NSURLAuthenticationChallenge * _Nonnull)challenge completionHandler:(void (^ _Nonnull)(NSURLSessionAuthChallengeDisposition disposition, NSURLCredential * _Nullable credential))completionHandler ``` |

Modified [-[WKNavigationDelegate webView:didReceiveServerRedirectForProvisionalNavigation:]](https://developer.apple.com/documentation/webkit/wknavigationdelegate/1455627-webview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)webView:(WKWebView *)webView didReceiveServerRedirectForProvisionalNavigation:(WKNavigation *)navigation ``` |
| To | ``` - (void)webView:(WKWebView * _Nonnull)webView didReceiveServerRedirectForProvisionalNavigation:(WKNavigation * _Null_unspecified)navigation ``` |

Modified [-[WKNavigationDelegate webView:didStartProvisionalNavigation:]](https://developer.apple.com/documentation/webkit/wknavigationdelegate/1455621-webview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)webView:(WKWebView *)webView didStartProvisionalNavigation:(WKNavigation *)navigation ``` |
| To | ``` - (void)webView:(WKWebView * _Nonnull)webView didStartProvisionalNavigation:(WKNavigation * _Null_unspecified)navigation ``` |

#### WKNavigationResponse.h

Modified [WKNavigationResponse.response](https://developer.apple.com/documentation/webkit/wknavigationresponse/1459484-response)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSURLResponse *response ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSURLResponse *response ``` |

#### WKScriptMessage.h

Modified [WKScriptMessage.body](https://developer.apple.com/documentation/webkit/wkscriptmessage/1417901-body)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) id body ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) id body ``` |

Modified [WKScriptMessage.frameInfo](https://developer.apple.com/documentation/webkit/wkscriptmessage/1417906-frameinfo)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) WKFrameInfo *frameInfo ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) WKFrameInfo *frameInfo ``` |

Modified [WKScriptMessage.name](https://developer.apple.com/documentation/webkit/wkscriptmessage/1417908-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *name ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSString *name ``` |

Modified [WKScriptMessage.webView](https://developer.apple.com/documentation/webkit/wkscriptmessage/1417903-webview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, weak) WKWebView *webView ``` |
| To | ``` @property(nonatomic, readonly, weak, nullable) WKWebView *webView ``` |

#### WKScriptMessageHandler.h

Modified [-[WKScriptMessageHandler userContentController:didReceiveScriptMessage:]](https://developer.apple.com/documentation/webkit/wkscriptmessagehandler/1396222-usercontentcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (void)userContentController:(WKUserContentController *)userContentController didReceiveScriptMessage:(WKScriptMessage *)message ``` |
| To | ``` - (void)userContentController:(WKUserContentController * _Nonnull)userContentController didReceiveScriptMessage:(WKScriptMessage * _Nonnull)message ``` |

#### WKSecurityOrigin.h (Added)

Added [WKSecurityOrigin](https://developer.apple.com/documentation/webkit/wksecurityorigin)Added [WKSecurityOrigin.host](https://developer.apple.com/documentation/webkit/wksecurityorigin/1536794-host)Added [WKSecurityOrigin.port](https://developer.apple.com/documentation/webkit/wksecurityorigin/1536403-port)Added [WKSecurityOrigin.protocol](https://developer.apple.com/documentation/webkit/wksecurityorigin/1537470-protocol)

#### WKUIDelegate.h

Added [-[WKUIDelegate webViewDidClose:]](https://developer.apple.com/documentation/webkit/wkuidelegate/1537390-webviewdidclose)Modified [-[WKUIDelegate webView:createWebViewWithConfiguration:forNavigationAction:windowFeatures:]](https://developer.apple.com/documentation/webkit/wkuidelegate/1536907-webview)

|  | Declaration |
| --- | --- |
| From | ``` - (WKWebView *)webView:(WKWebView *)webView createWebViewWithConfiguration:(WKWebViewConfiguration *)configuration forNavigationAction:(WKNavigationAction *)navigationAction windowFeatures:(WKWindowFeatures *)windowFeatures ``` |
| To | ``` - (WKWebView * _Nullable)webView:(WKWebView * _Nonnull)webView createWebViewWithConfiguration:(WKWebViewConfiguration * _Nonnull)configuration forNavigationAction:(WKNavigationAction * _Nonnull)navigationAction windowFeatures:(WKWindowFeatures * _Nonnull)windowFeatures ``` |

Modified [-[WKUIDelegate webView:runJavaScriptAlertPanelWithMessage:initiatedByFrame:completionHandler:]](https://developer.apple.com/documentation/webkit/wkuidelegate/1537406-webview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)webView:(WKWebView *)webView runJavaScriptAlertPanelWithMessage:(NSString *)message initiatedByFrame:(WKFrameInfo *)frame completionHandler:(void (^)(void))completionHandler ``` |
| To | ``` - (void)webView:(WKWebView * _Nonnull)webView runJavaScriptAlertPanelWithMessage:(NSString * _Nonnull)message initiatedByFrame:(WKFrameInfo * _Nonnull)frame completionHandler:(void (^ _Nonnull)(void))completionHandler ``` |

Modified [-[WKUIDelegate webView:runJavaScriptConfirmPanelWithMessage:initiatedByFrame:completionHandler:]](https://developer.apple.com/documentation/webkit/wkuidelegate/1536489-webview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)webView:(WKWebView *)webView runJavaScriptConfirmPanelWithMessage:(NSString *)message initiatedByFrame:(WKFrameInfo *)frame completionHandler:(void (^)(BOOL result))completionHandler ``` |
| To | ``` - (void)webView:(WKWebView * _Nonnull)webView runJavaScriptConfirmPanelWithMessage:(NSString * _Nonnull)message initiatedByFrame:(WKFrameInfo * _Nonnull)frame completionHandler:(void (^ _Nonnull)(BOOL result))completionHandler ``` |

Modified [-[WKUIDelegate webView:runJavaScriptTextInputPanelWithPrompt:defaultText:initiatedByFrame:completionHandler:]](https://developer.apple.com/documentation/webkit/wkuidelegate/1538086-webview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)webView:(WKWebView *)webView runJavaScriptTextInputPanelWithPrompt:(NSString *)prompt defaultText:(NSString *)defaultText initiatedByFrame:(WKFrameInfo *)frame completionHandler:(void (^)(NSString *result))completionHandler ``` |
| To | ``` - (void)webView:(WKWebView * _Nonnull)webView runJavaScriptTextInputPanelWithPrompt:(NSString * _Nonnull)prompt defaultText:(NSString * _Nullable)defaultText initiatedByFrame:(WKFrameInfo * _Nonnull)frame completionHandler:(void (^ _Nonnull)(NSString * _Nullable result))completionHandler ``` |

#### WKUserContentController.h

Modified [-[WKUserContentController addScriptMessageHandler:name:]](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/1537172-addscriptmessagehandler)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addScriptMessageHandler:(id<WKScriptMessageHandler>)scriptMessageHandler name:(NSString *)name ``` |
| To | ``` - (void)addScriptMessageHandler:(id<WKScriptMessageHandler> _Nonnull)scriptMessageHandler name:(NSString * _Nonnull)name ``` |

Modified [-[WKUserContentController addUserScript:]](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/1537448-adduserscript)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addUserScript:(WKUserScript *)userScript ``` |
| To | ``` - (void)addUserScript:(WKUserScript * _Nonnull)userScript ``` |

Modified [-[WKUserContentController removeScriptMessageHandlerForName:]](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/1537532-removescriptmessagehandlerfornam)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeScriptMessageHandlerForName:(NSString *)name ``` |
| To | ``` - (void)removeScriptMessageHandlerForName:(NSString * _Nonnull)name ``` |

Modified [WKUserContentController.userScripts](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/1538046-userscripts)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *userScripts ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSArray<WKUserScript *> *userScripts ``` |

#### WKUserScript.h

Modified [-[WKUserScript initWithSource:injectionTime:forMainFrameOnly:]](https://developer.apple.com/documentation/webkit/wkuserscript/1537750-initwithsource)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithSource:(NSString *)source injectionTime:(WKUserScriptInjectionTime)injectionTime forMainFrameOnly:(BOOL)forMainFrameOnly ``` |
| To | ``` - (instancetype _Nonnull)initWithSource:(NSString * _Nonnull)source injectionTime:(WKUserScriptInjectionTime)injectionTime forMainFrameOnly:(BOOL)forMainFrameOnly ``` |

Modified [WKUserScript.source](https://developer.apple.com/documentation/webkit/wkuserscript/1537787-source)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *source ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSString *source ``` |

#### WKWebsiteDataRecord.h (Added)

Added [WKWebsiteDataRecord](https://developer.apple.com/documentation/webkit/wkwebsitedatarecord)Added [WKWebsiteDataRecord.dataTypes](https://developer.apple.com/documentation/webkit/wkwebsitedatarecord/1538007-datatypes)Added [WKWebsiteDataRecord.displayName](https://developer.apple.com/documentation/webkit/wkwebsitedatarecord/1537733-displayname)Added [WKWebsiteDataTypeCookies](https://developer.apple.com/documentation/webkit/wkwebsitedatatypecookies)Added [WKWebsiteDataTypeDiskCache](https://developer.apple.com/documentation/webkit/wkwebsitedatatypediskcache)Added [WKWebsiteDataTypeIndexedDBDatabases](https://developer.apple.com/documentation/webkit/wkwebsitedatatypeindexeddbdatabases)Added [WKWebsiteDataTypeLocalStorage](https://developer.apple.com/documentation/webkit/wkwebsitedatatypelocalstorage)Added [WKWebsiteDataTypeMemoryCache](https://developer.apple.com/documentation/webkit/wkwebsitedatatypememorycache)Added [WKWebsiteDataTypeOfflineWebApplicationCache](https://developer.apple.com/documentation/webkit/wkwebsitedatatypeofflinewebapplicationcache)Added [WKWebsiteDataTypeSessionStorage](https://developer.apple.com/documentation/webkit/wkwebsitedatatypesessionstorage)Added [WKWebsiteDataTypeWebSQLDatabases](https://developer.apple.com/documentation/webkit/wkwebsitedatatypewebsqldatabases)

#### WKWebsiteDataStore.h (Added)

Added [WKWebsiteDataStore](https://developer.apple.com/documentation/webkit/wkwebsitedatastore)Added [+[WKWebsiteDataStore allWebsiteDataTypes]](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/1532929-allwebsitedatatypes)Added [+[WKWebsiteDataStore defaultDataStore]](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/1532937-defaultdatastore)Added [-[WKWebsiteDataStore fetchDataRecordsOfTypes:completionHandler:]](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/1532932-fetchdatarecords)Added [+[WKWebsiteDataStore nonPersistentDataStore]](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/1532934-nonpersistentdatastore)Added [WKWebsiteDataStore.persistent](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/1532928-persistent)Added [-[WKWebsiteDataStore removeDataOfTypes:forDataRecords:completionHandler:]](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/1532936-removedataoftypes)Added [-[WKWebsiteDataStore removeDataOfTypes:modifiedSince:completionHandler:]](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/1532938-removedataoftypes)

#### WKWebView.h

Added [WKWebView.allowsLinkPreview](https://developer.apple.com/documentation/webkit/wkwebview/1415000-allowslinkpreview)Added [WKWebView.certificateChain](https://developer.apple.com/documentation/webkit/wkwebview/1414958-certificatechain)Added [WKWebView.customUserAgent](https://developer.apple.com/documentation/webkit/wkwebview/1414950-customuseragent)Added [-[WKWebView loadData:MIMEType:characterEncodingName:baseURL:]](https://developer.apple.com/documentation/webkit/wkwebview/1415011-loaddata)Added [-[WKWebView loadFileURL:allowingReadAccessToURL:]](https://developer.apple.com/documentation/webkit/wkwebview/1414973-loadfileurl)Modified [WKWebView.backForwardList](https://developer.apple.com/documentation/webkit/wkwebview/1414977-backforwardlist)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, strong) WKBackForwardList *backForwardList ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) WKBackForwardList *backForwardList ``` |

Modified [WKWebView.configuration](https://developer.apple.com/documentation/webkit/wkwebview/1414979-configuration)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) WKWebViewConfiguration *configuration ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) WKWebViewConfiguration *configuration ``` |

Modified [-[WKWebView evaluateJavaScript:completionHandler:]](https://developer.apple.com/documentation/webkit/wkwebview/1415017-evaluatejavascript)

|  | Declaration |
| --- | --- |
| From | ``` - (void)evaluateJavaScript:(NSString *)javaScriptString completionHandler:(void (^)(id, NSError *))completionHandler ``` |
| To | ``` - (void)evaluateJavaScript:(NSString * _Nonnull)javaScriptString completionHandler:(void (^ _Nullable)(id _Nullable, NSError * _Nullable error))completionHandler ``` |

Modified [-[WKWebView goBack]](https://developer.apple.com/documentation/webkit/wkwebview/1414952-goback)

|  | Declaration |
| --- | --- |
| From | ``` - (WKNavigation *)goBack ``` |
| To | ``` - (WKNavigation * _Nullable)goBack ``` |

Modified [-[WKWebView goBack:]](https://developer.apple.com/documentation/webkit/wkwebview/1414975-goback)

|  | Declaration |
| --- | --- |
| From | ``` - (IBAction)goBack:(id)sender ``` |
| To | ``` - (IBAction)goBack:(id _Nullable)sender ``` |

Modified [-[WKWebView goForward]](https://developer.apple.com/documentation/webkit/wkwebview/1414993-goforward)

|  | Declaration |
| --- | --- |
| From | ``` - (WKNavigation *)goForward ``` |
| To | ``` - (WKNavigation * _Nullable)goForward ``` |

Modified [-[WKWebView goForward:]](https://developer.apple.com/documentation/webkit/wkwebview/1414960-goforward)

|  | Declaration |
| --- | --- |
| From | ``` - (IBAction)goForward:(id)sender ``` |
| To | ``` - (IBAction)goForward:(id _Nullable)sender ``` |

Modified [-[WKWebView goToBackForwardListItem:]](https://developer.apple.com/documentation/webkit/wkwebview/1414991-go)

|  | Declaration |
| --- | --- |
| From | ``` - (WKNavigation *)goToBackForwardListItem:(WKBackForwardListItem *)item ``` |
| To | ``` - (WKNavigation * _Nullable)goToBackForwardListItem:(WKBackForwardListItem * _Nonnull)item ``` |

Modified [-[WKWebView initWithFrame:configuration:]](https://developer.apple.com/documentation/webkit/wkwebview/1414998-initwithframe)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithFrame:(CGRect)frame configuration:(WKWebViewConfiguration *)configuration ``` |
| To | ``` - (instancetype _Nonnull)initWithFrame:(CGRect)frame configuration:(WKWebViewConfiguration * _Nonnull)configuration ``` |

Modified [-[WKWebView loadHTMLString:baseURL:]](https://developer.apple.com/documentation/webkit/wkwebview/1415004-loadhtmlstring)

|  | Declaration |
| --- | --- |
| From | ``` - (WKNavigation *)loadHTMLString:(NSString *)string baseURL:(NSURL *)baseURL ``` |
| To | ``` - (WKNavigation * _Nullable)loadHTMLString:(NSString * _Nonnull)string baseURL:(NSURL * _Nullable)baseURL ``` |

Modified [-[WKWebView loadRequest:]](https://developer.apple.com/documentation/webkit/wkwebview/1414954-loadrequest)

|  | Declaration |
| --- | --- |
| From | ``` - (WKNavigation *)loadRequest:(NSURLRequest *)request ``` |
| To | ``` - (WKNavigation * _Nullable)loadRequest:(NSURLRequest * _Nonnull)request ``` |

Modified [WKWebView.navigationDelegate](https://developer.apple.com/documentation/webkit/wkwebview/1414971-navigationdelegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, weak) id<WKNavigationDelegate> navigationDelegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<WKNavigationDelegate> navigationDelegate ``` |

Modified [-[WKWebView reload]](https://developer.apple.com/documentation/webkit/wkwebview/1414969-reload)

|  | Declaration |
| --- | --- |
| From | ``` - (WKNavigation *)reload ``` |
| To | ``` - (WKNavigation * _Nullable)reload ``` |

Modified [-[WKWebView reload:]](https://developer.apple.com/documentation/webkit/wkwebview/1414987-reload)

|  | Declaration |
| --- | --- |
| From | ``` - (IBAction)reload:(id)sender ``` |
| To | ``` - (IBAction)reload:(id _Nullable)sender ``` |

Modified [-[WKWebView reloadFromOrigin]](https://developer.apple.com/documentation/webkit/wkwebview/1414956-reloadfromorigin)

|  | Declaration |
| --- | --- |
| From | ``` - (WKNavigation *)reloadFromOrigin ``` |
| To | ``` - (WKNavigation * _Nullable)reloadFromOrigin ``` |

Modified [-[WKWebView reloadFromOrigin:]](https://developer.apple.com/documentation/webkit/wkwebview/1414989-reloadfromorigin)

|  | Declaration |
| --- | --- |
| From | ``` - (IBAction)reloadFromOrigin:(id)sender ``` |
| To | ``` - (IBAction)reloadFromOrigin:(id _Nullable)sender ``` |

Modified [-[WKWebView stopLoading:]](https://developer.apple.com/documentation/webkit/wkwebview/1415013-stoploading)

|  | Declaration |
| --- | --- |
| From | ``` - (IBAction)stopLoading:(id)sender ``` |
| To | ``` - (IBAction)stopLoading:(id _Nullable)sender ``` |

Modified [WKWebView.title](https://developer.apple.com/documentation/webkit/wkwebview/1415015-title)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *title ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *title ``` |

Modified [WKWebView.UIDelegate](https://developer.apple.com/documentation/webkit/wkwebview/1415009-uidelegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, weak) id<WKUIDelegate> UIDelegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<WKUIDelegate> UIDelegate ``` |

Modified [WKWebView.URL](https://developer.apple.com/documentation/webkit/wkwebview/1415005-url)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSURL *URL ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSURL *URL ``` |

#### WKWebViewConfiguration.h

Added [WKWebViewConfiguration.allowsAirPlayForMediaPlayback](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1395673-allowsairplayformediaplayback)Added [WKWebViewConfiguration.applicationNameForUserAgent](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1395665-applicationnameforuseragent)Added [WKWebViewConfiguration.websiteDataStore](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1395661-websitedatastore)Added WKWebViewConfiguration(WKDeprecated)Modified [WKWebViewConfiguration.preferences](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1395666-preferences)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) WKPreferences *preferences ``` |
| To | ``` @property(nonatomic, strong, nonnull) WKPreferences *preferences ``` |

Modified [WKWebViewConfiguration.processPool](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1395659-processpool)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) WKProcessPool *processPool ``` |
| To | ``` @property(nonatomic, strong, nonnull) WKProcessPool *processPool ``` |

Modified [WKWebViewConfiguration.userContentController](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1395668-usercontentcontroller)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) WKUserContentController *userContentController ``` |
| To | ``` @property(nonatomic, strong, nonnull) WKUserContentController *userContentController ``` |

#### WKWindowFeatures.h

Modified [WKWindowFeatures.allowsResizing](https://developer.apple.com/documentation/webkit/wkwindowfeatures/1536871-allowsresizing)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSNumber *allowsResizing ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSNumber *allowsResizing ``` |

Modified [WKWindowFeatures.height](https://developer.apple.com/documentation/webkit/wkwindowfeatures/1536826-height)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSNumber *height ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSNumber *height ``` |

Modified [WKWindowFeatures.menuBarVisibility](https://developer.apple.com/documentation/webkit/wkwindowfeatures/1538001-menubarvisibility)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSNumber *menuBarVisibility ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSNumber *menuBarVisibility ``` |

Modified [WKWindowFeatures.statusBarVisibility](https://developer.apple.com/documentation/webkit/wkwindowfeatures/1536638-statusbarvisibility)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSNumber *statusBarVisibility ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSNumber *statusBarVisibility ``` |

Modified [WKWindowFeatures.toolbarsVisibility](https://developer.apple.com/documentation/webkit/wkwindowfeatures/1536218-toolbarsvisibility)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSNumber *toolbarsVisibility ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSNumber *toolbarsVisibility ``` |

Modified [WKWindowFeatures.width](https://developer.apple.com/documentation/webkit/wkwindowfeatures/1537562-width)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSNumber *width ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSNumber *width ``` |

Modified [WKWindowFeatures.x](https://developer.apple.com/documentation/webkit/wkwindowfeatures/1537705-x)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSNumber *x ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSNumber *x ``` |

Modified [WKWindowFeatures.y](https://developer.apple.com/documentation/webkit/wkwindowfeatures/1537052-y)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSNumber *y ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSNumber *y ``` |

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
