---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/WebKit.html
archived_at: '2026-07-18T02:52:45.030557Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# WebKit Changes

## WebKit

Removed WKNavigation.errorRemoved WKNavigation.initialRequestRemoved WKNavigation.requestRemoved WKNavigation.responseRemoved WebDragDestinationAction.valueRemoved WebDragSourceAction.valueAdded NSObject.downloadWindowForAuthenticationSheet(WebDownload!) -> NSWindow!Added NSObject.finalizeForWebScript()Added NSObject.invokeDefaultMethodWithArguments([AnyObject]!) -> AnyObject!Added NSObject.invokeUndefinedMethodFromWebScript(String!, withArguments:[AnyObject]!) -> AnyObject!Added NSObject.isKeyExcludedFromWebScript(UnsafePointer<Int8>) -> Bool [class]Added NSObject.isSelectorExcludedFromWebScript(Selector) -> Bool [class]Added NSObject.objectForWebScriptAdded NSObject.undoManagerForWebView(WebView!) -> NSUndoManager!Added NSObject.webFrameAdded NSObject.webPlugInContainerLoadRequest(NSURLRequest!, inFrame: String!)Added NSObject.webPlugInContainerSelectionColorAdded NSObject.webPlugInContainerShowStatus(String!)Added NSObject.webPlugInDestroy()Added NSObject.webPlugInInitialize()Added NSObject.webPlugInMainResourceDidFailWithError(NSError!)Added NSObject.webPlugInMainResourceDidFinishLoading()Added NSObject.webPlugInMainResourceDidReceiveData(NSData!)Added NSObject.webPlugInMainResourceDidReceiveResponse(NSURLResponse!)Added NSObject.webPlugInSetIsSelected(Bool)Added NSObject.webPlugInStart()Added NSObject.webPlugInStop()Added NSObject.webScriptNameForKey(UnsafePointer<Int8>) -> String! [class]Added NSObject.webScriptNameForSelector(Selector) -> String! [class]Added NSObject.webView(WebView!, contextMenuItemsForElement:[NSObject: AnyObject]!, defaultMenuItems:[AnyObject]!) -> [AnyObject]!Added NSObject.webView(WebView!, createWebViewModalDialogWithRequest: NSURLRequest!) -> WebView!Added NSObject.webView(WebView!, createWebViewWithRequest: NSURLRequest!) -> WebView!Added NSObject.webView(WebView!, decidePolicyForMIMEType: String!, request: NSURLRequest!, frame: WebFrame!, decisionListener: WebPolicyDecisionListener!)Added NSObject.webView(WebView!, decidePolicyForNavigationAction:[NSObject: AnyObject]!, request: NSURLRequest!, frame: WebFrame!, decisionListener: WebPolicyDecisionListener!)Added NSObject.webView(WebView!, decidePolicyForNewWindowAction:[NSObject: AnyObject]!, request: NSURLRequest!, newFrameName: String!, decisionListener: WebPolicyDecisionListener!)Added NSObject.webView(WebView!, didCancelClientRedirectForFrame: WebFrame!)Added NSObject.webView(WebView!, didChangeLocationWithinPageForFrame: WebFrame!)Added NSObject.webView(WebView!, didClearWindowObject: WebScriptObject!, forFrame: WebFrame!)Added NSObject.webView(WebView!, didCommitLoadForFrame: WebFrame!)Added NSObject.webView(WebView!, didCreateJavaScriptContext: JSContext!, forFrame: WebFrame!)Added NSObject.webView(WebView!, didFailLoadWithError: NSError!, forFrame: WebFrame!)Added NSObject.webView(WebView!, didFailProvisionalLoadWithError: NSError!, forFrame: WebFrame!)Added NSObject.webView(WebView!, didFinishLoadForFrame: WebFrame!)Added NSObject.webView(WebView!, didReceiveIcon: NSImage!, forFrame: WebFrame!)Added NSObject.webView(WebView!, didReceiveServerRedirectForProvisionalLoadForFrame: WebFrame!)Added NSObject.webView(WebView!, didReceiveTitle: String!, forFrame: WebFrame!)Added NSObject.webView(WebView!, didStartProvisionalLoadForFrame: WebFrame!)Added NSObject.webView(WebView!, doCommandBySelector: Selector) -> BoolAdded NSObject.webView(WebView!, dragDestinationActionMaskForDraggingInfo: NSDraggingInfo!) -> IntAdded NSObject.webView(WebView!, dragSourceActionMaskForPoint: NSPoint) -> IntAdded NSObject.webView(WebView!, drawFooterInRect: NSRect)Added NSObject.webView(WebView!, drawHeaderInRect: NSRect)Added NSObject.webView(WebView!, identifierForInitialRequest: NSURLRequest!, fromDataSource: WebDataSource!) -> AnyObject!Added NSObject.webView(WebView!, makeFirstResponder: NSResponder!)Added NSObject.webView(WebView!, mouseDidMoveOverElement:[NSObject: AnyObject]!, modifierFlags: Int)Added NSObject.webView(WebView!, plugInFailedWithError: NSError!, dataSource: WebDataSource!)Added NSObject.webView(WebView!, printFrameView: WebFrameView!)Added NSObject.webView(WebView!, resource: AnyObject!, didCancelAuthenticationChallenge: NSURLAuthenticationChallenge!, fromDataSource: WebDataSource!)Added NSObject.webView(WebView!, resource: AnyObject!, didFailLoadingWithError: NSError!, fromDataSource: WebDataSource!)Added NSObject.webView(WebView!, resource: AnyObject!, didFinishLoadingFromDataSource: WebDataSource!)Added NSObject.webView(WebView!, resource: AnyObject!, didReceiveAuthenticationChallenge: NSURLAuthenticationChallenge!, fromDataSource: WebDataSource!)Added NSObject.webView(WebView!, resource: AnyObject!, didReceiveContentLength: Int, fromDataSource: WebDataSource!)Added NSObject.webView(WebView!, resource: AnyObject!, didReceiveResponse: NSURLResponse!, fromDataSource: WebDataSource!)Added NSObject.webView(WebView!, resource: AnyObject!, willSendRequest: NSURLRequest!, redirectResponse: NSURLResponse!, fromDataSource: WebDataSource!) -> NSURLRequest!Added NSObject.webView(WebView!, runBeforeUnloadConfirmPanelWithMessage: String!, initiatedByFrame: WebFrame!) -> BoolAdded NSObject.webView(WebView!, runJavaScriptAlertPanelWithMessage: String!, initiatedByFrame: WebFrame!)Added NSObject.webView(WebView!, runJavaScriptConfirmPanelWithMessage: String!, initiatedByFrame: WebFrame!) -> BoolAdded NSObject.webView(WebView!, runJavaScriptTextInputPanelWithPrompt: String!, defaultText: String!, initiatedByFrame: WebFrame!) -> String!Added NSObject.webView(WebView!, runOpenPanelForFileButtonWithResultListener: WebOpenPanelResultListener!)Added NSObject.webView(WebView!, runOpenPanelForFileButtonWithResultListener: WebOpenPanelResultListener!, allowMultipleFiles: Bool)Added NSObject.webView(WebView!, setFrame: NSRect)Added NSObject.webView(WebView!, setResizable: Bool)Added NSObject.webView(WebView!, setStatusBarVisible: Bool)Added NSObject.webView(WebView!, setStatusText: String!)Added NSObject.webView(WebView!, setToolbarsVisible: Bool)Added NSObject.webView(WebView!, shouldApplyStyle: DOMCSSStyleDeclaration!, toElementsInDOMRange: DOMRange!) -> BoolAdded NSObject.webView(WebView!, shouldBeginEditingInDOMRange: DOMRange!) -> BoolAdded NSObject.webView(WebView!, shouldChangeSelectedDOMRange: DOMRange!, toDOMRange: DOMRange!, affinity: NSSelectionAffinity, stillSelecting: Bool) -> BoolAdded NSObject.webView(WebView!, shouldChangeTypingStyle: DOMCSSStyleDeclaration!, toStyle: DOMCSSStyleDeclaration!) -> BoolAdded NSObject.webView(WebView!, shouldDeleteDOMRange: DOMRange!) -> BoolAdded NSObject.webView(WebView!, shouldEndEditingInDOMRange: DOMRange!) -> BoolAdded NSObject.webView(WebView!, shouldInsertNode: DOMNode!, replacingDOMRange: DOMRange!, givenAction: WebViewInsertAction) -> BoolAdded NSObject.webView(WebView!, shouldInsertText: String!, replacingDOMRange: DOMRange!, givenAction: WebViewInsertAction) -> BoolAdded NSObject.webView(WebView!, shouldPerformAction: Selector, fromSender: AnyObject!) -> BoolAdded NSObject.webView(WebView!, unableToImplementPolicyWithError: NSError!, frame: WebFrame!)Added NSObject.webView(WebView!, validateUserInterfaceItem: NSValidatedUserInterfaceItem!, defaultValidation: Bool) -> BoolAdded NSObject.webView(WebView!, willCloseFrame: WebFrame!)Added NSObject.webView(WebView!, willPerformClientRedirectToURL: NSURL!, delay: NSTimeInterval, fireDate: NSDate!, forFrame: WebFrame!)Added NSObject.webView(WebView!, willPerformDragDestinationAction: WebDragDestinationAction, forDraggingInfo: NSDraggingInfo!)Added NSObject.webView(WebView!, willPerformDragSourceAction: WebDragSourceAction, fromPoint: NSPoint, withPasteboard: NSPasteboard!)Added NSObject.webViewAreToolbarsVisible(WebView!) -> BoolAdded NSObject.webViewClose(WebView!)Added NSObject.webViewDidBeginEditing(NSNotification!)Added NSObject.webViewDidChange(NSNotification!)Added NSObject.webViewDidChangeSelection(NSNotification!)Added NSObject.webViewDidChangeTypingStyle(NSNotification!)Added NSObject.webViewDidEndEditing(NSNotification!)Added NSObject.webViewFirstResponder(WebView!) -> NSResponder!Added NSObject.webViewFocus(WebView!)Added NSObject.webViewFooterHeight(WebView!) -> FloatAdded NSObject.webViewFrame(WebView!) -> NSRectAdded NSObject.webViewHeaderHeight(WebView!) -> FloatAdded NSObject.webViewIsResizable(WebView!) -> BoolAdded NSObject.webViewIsStatusBarVisible(WebView!) -> BoolAdded NSObject.webViewRunModal(WebView!)Added NSObject.webViewShow(WebView!)Added NSObject.webViewStatusText(WebView!) -> String!Added NSObject.webViewUnfocus(WebView!)Added WebDragDestinationAction.init(rawValue: UInt)Added WebDragSourceAction.init(rawValue: UInt)Modified DOMAbstractView

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMAttr

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMAttr.style

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMBlob

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMCDATASection

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSCharsetRule

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSFontFaceRule

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSImportRule

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSMediaRule

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSMediaRule.insertRule(String!, index: UInt32) -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMCSSPageRule

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSPrimitiveValue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSPrimitiveValue.setFloatValue(UInt16, floatValue: Float)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMCSSPrimitiveValue.setStringValue(UInt16, stringValue: String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMCSSRule

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSRuleList

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.azimuth() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.background() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.backgroundAttachment() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.backgroundColor() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.backgroundImage() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.backgroundPosition() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.backgroundRepeat() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.border() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.borderBottom() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.borderBottomColor() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.borderBottomStyle() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.borderBottomWidth() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.borderCollapse() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.borderColor() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.borderLeft() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.borderLeftColor() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.borderLeftStyle() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.borderLeftWidth() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.borderRight() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.borderRightColor() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.borderRightStyle() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.borderRightWidth() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.borderSpacing() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.borderStyle() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.borderTop() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.borderTopColor() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.borderTopStyle() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.borderTopWidth() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.borderWidth() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.bottom() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.captionSide() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.clear() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.clip() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.color() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.content() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.counterIncrement() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.counterReset() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.cssFloat() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.cue() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.cueAfter() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.cueBefore() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.cursor() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.direction() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.display() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.elevation() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.emptyCells() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.font() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.fontFamily() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.fontSize() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.fontSizeAdjust() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.fontStretch() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.fontStyle() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.fontVariant() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.fontWeight() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.height() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.isPropertyImplicit(String!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMCSSStyleDeclaration.left() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.letterSpacing() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.lineHeight() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.listStyle() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.listStyleImage() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.listStylePosition() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.listStyleType() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.margin() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.marginBottom() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.marginLeft() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.marginRight() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.marginTop() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.markerOffset() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.marks() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.maxHeight() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.maxWidth() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.minHeight() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.minWidth() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.orphans() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.outline() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.outlineColor() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.outlineStyle() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.outlineWidth() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.overflow() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.padding() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.paddingBottom() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.paddingLeft() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.paddingRight() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.paddingTop() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.page() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.pageBreakAfter() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.pageBreakBefore() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.pageBreakInside() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.pause() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.pauseAfter() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.pauseBefore() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.pitch() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.pitchRange() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.playDuring() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.position() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.quotes() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.richness() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.right() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setAzimuth(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBackground(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBackgroundAttachment(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBackgroundColor(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBackgroundImage(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBackgroundPosition(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBackgroundRepeat(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBorder(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBorderBottom(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBorderBottomColor(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBorderBottomStyle(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBorderBottomWidth(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBorderCollapse(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBorderColor(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBorderLeft(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBorderLeftColor(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBorderLeftStyle(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBorderLeftWidth(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBorderRight(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBorderRightColor(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBorderRightStyle(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBorderRightWidth(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBorderSpacing(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBorderStyle(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBorderTop(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBorderTopColor(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBorderTopStyle(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBorderTopWidth(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBorderWidth(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setBottom(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setCaptionSide(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setClear(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setClip(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setColor(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setContent(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setCounterIncrement(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setCounterReset(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setCssFloat(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setCue(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setCueAfter(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setCueBefore(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setCursor(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setDirection(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setDisplay(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setElevation(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setEmptyCells(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setFont(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setFontFamily(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setFontSize(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setFontSizeAdjust(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setFontStretch(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setFontStyle(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setFontVariant(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setFontWeight(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setHeight(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setLeft(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setLetterSpacing(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setLineHeight(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setListStyle(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setListStyleImage(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setListStylePosition(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setListStyleType(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setMargin(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setMarginBottom(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setMarginLeft(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setMarginRight(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setMarginTop(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setMarkerOffset(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setMarks(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setMaxHeight(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setMaxWidth(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setMinHeight(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setMinWidth(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setOrphans(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setOutline(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setOutlineColor(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setOutlineStyle(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setOutlineWidth(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setOverflow(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setPadding(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setPaddingBottom(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setPaddingLeft(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setPaddingRight(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setPaddingTop(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setPage(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setPageBreakAfter(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setPageBreakBefore(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setPageBreakInside(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setPause(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setPauseAfter(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setPauseBefore(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setPitch(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setPitchRange(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setPlayDuring(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setPosition(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setProperty(String!, value: String!, priority: String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMCSSStyleDeclaration.setQuotes(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setRichness(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setRight(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setSize(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setSpeak(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setSpeakHeader(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setSpeakNumeral(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setSpeakPunctuation(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setSpeechRate(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setStress(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setTableLayout(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setTextAlign(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setTextDecoration(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setTextIndent(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setTextShadow(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setTextTransform(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setTop(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setUnicodeBidi(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setVerticalAlign(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setVisibility(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setVoiceFamily(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setVolume(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setWhiteSpace(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setWidows(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setWidth(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setWordSpacing(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.setZIndex(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.size() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.speak() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.speakHeader() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.speakNumeral() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.speakPunctuation() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.speechRate() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.stress() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.tableLayout() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.textAlign() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.textDecoration() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.textIndent() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.textShadow() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.textTransform() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.top() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.unicodeBidi() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.verticalAlign() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.visibility() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.voiceFamily() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.volume() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.whiteSpace() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.widows() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.width() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.wordSpacing() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleDeclaration.zIndex() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleRule

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleSheet

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSStyleSheet.addRule(String!, style: String!, index: UInt32) -> Int32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMCSSStyleSheet.insertRule(String!, index: UInt32) -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMCSSStyleSheet.removeRule(UInt32)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMCSSStyleSheet.rules

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMCSSUnknownRule

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSValue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCSSValueList

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCharacterData

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCharacterData.deleteData(UInt32, length: UInt32)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMCharacterData.insertData(UInt32, data: String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMCharacterData.replaceData(UInt32, length: UInt32, data: String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMCharacterData.substringData(UInt32, length: UInt32) -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMComment

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMCounter

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMDocument

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMDocument.activeElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMDocument.adoptNode(DOMNode!) -> DOMNode!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.characterSet

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.charset

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.createAttributeNS(String!, qualifiedName: String!) -> DOMAttr!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.createCSSStyleDeclaration() -> DOMCSSStyleDeclaration!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.createElementNS(String!, qualifiedName: String!) -> DOMElement!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.createExpression(String!, resolver: DOMXPathNSResolver!) -> DOMXPathExpression!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.createNSResolver(DOMNode!) -> DOMXPathNSResolver!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.createNodeIterator(DOMNode!, whatToShow: UInt32, filter: DOMNodeFilter!, expandEntityReferences: Bool) -> DOMNodeIterator!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.createProcessingInstruction(String!, data: String!) -> DOMProcessingInstruction!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.createTreeWalker(DOMNode!, whatToShow: UInt32, filter: DOMNodeFilter!, expandEntityReferences: Bool) -> DOMTreeWalker!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.defaultCharset

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.documentURI

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.elementFromPoint(Int32, y: Int32) -> DOMElement!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.evaluate(String!, contextNode: DOMNode!, resolver: DOMXPathNSResolver!, type: UInt16, inResult: DOMXPathResult!) -> DOMXPathResult!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.execCommand(String!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.execCommand(String!, userInterface: Bool) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.execCommand(String!, userInterface: Bool, value: String!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.getComputedStyle(DOMElement!, pseudoElement: String!) -> DOMCSSStyleDeclaration!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.getElementsByClassName(String!) -> DOMNodeList!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMDocument.getElementsByTagNameNS(String!, localName: String!) -> DOMNodeList!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.getMatchedCSSRules(DOMElement!, pseudoElement: String!) -> DOMCSSRuleList!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.getMatchedCSSRules(DOMElement!, pseudoElement: String!, authorOnly: Bool) -> DOMCSSRuleList!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.getOverrideStyle(DOMElement!, pseudoElement: String!) -> DOMCSSStyleDeclaration!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.hasFocus() -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMDocument.importNode(DOMNode!, deep: Bool) -> DOMNode!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.inputEncoding

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.lastModified

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMDocument.preferredStylesheetSet

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.queryCommandEnabled(String!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.queryCommandIndeterm(String!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.queryCommandState(String!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.queryCommandSupported(String!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.queryCommandValue(String!) -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.querySelector(String!) -> DOMElement!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMDocument.querySelectorAll(String!) -> DOMNodeList!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMDocument.readyState

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.selectedStylesheetSet

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.webkitCancelFullScreen()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMDocument.xmlEncoding

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.xmlStandalone

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocument.xmlVersion

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMDocumentFragment

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMDocumentType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMElement.blur()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMElement.childElementCount

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMElement.clientLeft

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMElement.clientTop

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMElement.firstElementChild

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMElement.focus()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMElement.getAttributeNS(String!, localName: String!) -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMElement.getAttributeNodeNS(String!, localName: String!) -> DOMAttr!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMElement.getElementsByClassName(String!) -> DOMNodeList!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMElement.getElementsByTagNameNS(String!, localName: String!) -> DOMNodeList!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMElement.hasAttributeNS(String!, localName: String!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMElement.image() -> NSImage!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMElement.innerText

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMElement.lastElementChild

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMElement.nextElementSibling

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMElement.previousElementSibling

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMElement.querySelector(String!) -> DOMElement!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMElement.querySelectorAll(String!) -> DOMNodeList!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMElement.removeAttributeNS(String!, localName: String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMElement.scrollByLines(Int32)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMElement.scrollByPages(Int32)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMElement.scrollIntoView(Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMElement.scrollIntoViewIfNeeded(Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMElement.setAttribute(String!, value: String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMElement.setAttributeNS(String!, qualifiedName: String!, value: String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMElement.webkitRequestFullScreen(UInt16)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMEntity

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMEntityReference

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMEvent

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMEvent.cancelBubble

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMEvent.initEvent(String!, canBubbleArg: Bool, cancelableArg: Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMEvent.returnValue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMEvent.srcElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMEventExceptionCode [struct]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMEventListener

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMEventTarget

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMEventTarget.addEventListener(String!, listener: DOMEventListener!, useCapture: Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMEventTarget.removeEventListener(String!, listener: DOMEventListener!, useCapture: Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMExceptionCode [struct]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMFile

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMFileList

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMHTMLAnchorElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLAnchorElement.absoluteLinkURL

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var absoluteLinkURL: NSURL! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var absoluteLinkURL: NSURL! { get } ``` | OS X 10.5 |

Modified DOMHTMLAnchorElement.hashName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLAnchorElement.host

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLAnchorElement.hostname

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLAnchorElement.pathname

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLAnchorElement.port

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLAnchorElement.protocol

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLAnchorElement.search

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLAnchorElement.text

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLAppletElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLAreaElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLAreaElement.absoluteLinkURL

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var absoluteLinkURL: NSURL! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var absoluteLinkURL: NSURL! { get } ``` | OS X 10.5 |

Modified DOMHTMLAreaElement.hashName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLAreaElement.host

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLAreaElement.hostname

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLAreaElement.pathname

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLAreaElement.port

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLAreaElement.protocol

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLAreaElement.search

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLBRElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLBaseElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLBaseFontElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLBodyElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLButtonElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLButtonElement.autofocus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMHTMLButtonElement.click()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLButtonElement.willValidate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMHTMLCollection

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLCollection.tags(String!) -> DOMNodeList!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMHTMLDListElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLDirectoryElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLDivElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLDocument

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLDocument.alinkColor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLDocument.bgColor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLDocument.captureEvents()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLDocument.clear()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMHTMLDocument.compatMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMHTMLDocument.createDocumentFragmentWithMarkupString(String!, baseURL: NSURL!) -> DOMDocumentFragment!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLDocument.createDocumentFragmentWithText(String!) -> DOMDocumentFragment!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLDocument.designMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLDocument.dir

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLDocument.embeds

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLDocument.fgColor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLDocument.height

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLDocument.linkColor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLDocument.plugins

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLDocument.releaseEvents()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLDocument.scripts

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLDocument.vlinkColor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLDocument.width

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLElement.accessKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified DOMHTMLElement.click()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified DOMHTMLElement.titleDisplayString

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLEmbedElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLFieldSetElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLFontElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLFormElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLFormElement.encoding

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLFrameElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLFrameElement.contentWindow

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLFrameElement.height

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLFrameElement.location

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLFrameElement.width

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLFrameSetElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLHRElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLHeadElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLHeadingElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLHtmlElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLIFrameElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLIFrameElement.contentWindow

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMHTMLImageElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLImageElement.absoluteImageURL

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var absoluteImageURL: NSURL! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var absoluteImageURL: NSURL! { get } ``` | OS X 10.5 |

Modified DOMHTMLImageElement.altDisplayString

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLImageElement.complete

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLImageElement.lowsrc

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLImageElement.naturalHeight

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLImageElement.naturalWidth

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLImageElement.x

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLImageElement.y

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLInputElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLInputElement.absoluteImageURL

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var absoluteImageURL: NSURL! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var absoluteImageURL: NSURL! { get } ``` | OS X 10.5 |

Modified DOMHTMLInputElement.altDisplayString

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLInputElement.autofocus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMHTMLInputElement.files

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMHTMLInputElement.indeterminate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLInputElement.multiple

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMHTMLInputElement.selectionEnd

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLInputElement.selectionStart

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLInputElement.setSelectionRange(Int32, end: Int32)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLInputElement.willValidate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMHTMLLIElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLLabelElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLLegendElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLLinkElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLLinkElement.absoluteLinkURL

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var absoluteLinkURL: NSURL! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var absoluteLinkURL: NSURL! { get } ``` | OS X 10.5 |

Modified DOMHTMLLinkElement.sheet

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLMapElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLMarqueeElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLMenuElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLMetaElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLModElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLOListElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLObjectElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLObjectElement.absoluteImageURL

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var absoluteImageURL: NSURL! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var absoluteImageURL: NSURL! { get } ``` | OS X 10.5 |

Modified DOMHTMLOptGroupElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLOptionElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLOptionsCollection

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLOptionsCollection.add(DOMHTMLOptionElement!, index: UInt32)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLOptionsCollection.remove(UInt32)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMHTMLOptionsCollection.selectedIndex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLParagraphElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLParamElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLPreElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLPreElement.wrap

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLQuoteElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLScriptElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLSelectElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLSelectElement.add(DOMHTMLElement!, before: DOMHTMLElement!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLSelectElement.autofocus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMHTMLSelectElement.item(UInt32) -> DOMNode!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMHTMLSelectElement.namedItem(String!) -> DOMNode!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMHTMLSelectElement.willValidate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMHTMLStyleElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLStyleElement.sheet

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLTableCaptionElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLTableCellElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLTableColElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLTableElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLTableRowElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLTableSectionElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLTextAreaElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLTextAreaElement.autofocus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMHTMLTextAreaElement.selectionEnd

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLTextAreaElement.selectionStart

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLTextAreaElement.setSelectionRange(Int32, end: Int32)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMHTMLTextAreaElement.willValidate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMHTMLTitleElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMHTMLUListElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMImplementation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMImplementation.createCSSStyleSheet(String!, media: String!) -> DOMCSSStyleSheet!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMImplementation.createDocument(String!, qualifiedName: String!, doctype: DOMDocumentType!) -> DOMDocument!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMImplementation.createDocumentType(String!, publicId: String!, systemId: String!) -> DOMDocumentType!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMImplementation.createHTMLDocument(String!) -> DOMHTMLDocument!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMImplementation.hasFeature(String!, version: String!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMKeyboardEvent

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMKeyboardEvent.altGraphKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMKeyboardEvent.initKeyboardEvent(String!, canBubble: Bool, cancelable: Bool, view: DOMAbstractView!, keyIdentifier: String!, location: UInt32, ctrlKey: Bool, altKey: Bool, shiftKey: Bool, metaKey: Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified DOMKeyboardEvent.initKeyboardEvent(String!, canBubble: Bool, cancelable: Bool, view: DOMAbstractView!, keyIdentifier: String!, location: UInt32, ctrlKey: Bool, altKey: Bool, shiftKey: Bool, metaKey: Bool, altGraphKey: Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified DOMKeyboardEvent.location

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified DOMMediaList

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMMouseEvent

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMMouseEvent.fromElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMMouseEvent.initMouseEvent(String!, canBubble: Bool, cancelable: Bool, view: DOMAbstractView!, detail: Int32, screenX: Int32, screenY: Int32, clientX: Int32, clientY: Int32, ctrlKey: Bool, altKey: Bool, shiftKey: Bool, metaKey: Bool, button: UInt16, relatedTarget: DOMEventTarget!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMMouseEvent.offsetX

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMMouseEvent.offsetY

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMMouseEvent.toElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMMouseEvent.x

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMMouseEvent.y

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMMutationEvent

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMMutationEvent.initMutationEvent(String!, canBubble: Bool, cancelable: Bool, relatedNode: DOMNode!, prevValue: String!, newValue: String!, attrName: String!, attrChange: UInt16)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMNamedNodeMap

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMNamedNodeMap.getNamedItemNS(String!, localName: String!) -> DOMNode!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMNamedNodeMap.removeNamedItemNS(String!, localName: String!) -> DOMNode!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMNode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMNode.baseURI

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMNode.boundingBox() -> NSRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMNode.compareDocumentPosition(DOMNode!) -> UInt16

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMNode.contains(DOMNode!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMNode.insertBefore(DOMNode!, refChild: DOMNode!) -> DOMNode!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMNode.isContentEditable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMNode.isDefaultNamespace(String!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMNode.isEqualNode(DOMNode!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMNode.isSameNode(DOMNode!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMNode.isSupported(String!, version: String!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMNode.lineBoxRects() -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMNode.lookupNamespaceURI(String!) -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMNode.lookupPrefix(String!) -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMNode.parentElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMNode.replaceChild(DOMNode!, oldChild: DOMNode!) -> DOMNode!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMNode.textContent

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMNodeFilter

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMNodeIterator

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMNodeIterator.pointerBeforeReferenceNode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMNodeIterator.referenceNode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMNodeList

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMNotation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMObject

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMObject.sheet

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMOverflowEvent

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMProcessingInstruction

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMProcessingInstruction.sheet

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMProgressEvent

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMRGBColor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMRGBColor.color

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var color: NSColor! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var color: NSColor! { get } ``` | OS X 10.5 |

Modified DOMRange

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMRange.compareBoundaryPoints(UInt16, sourceRange: DOMRange!) -> Int16

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMRange.compareNode(DOMNode!) -> Int16

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMRange.comparePoint(DOMNode!, offset: Int32) -> Int16

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMRange.createContextualFragment(String!) -> DOMDocumentFragment!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMRange.intersectsNode(DOMNode!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMRange.isPointInRange(DOMNode!, offset: Int32) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMRange.setEnd(DOMNode!, offset: Int32)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMRange.setStart(DOMNode!, offset: Int32)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMRange.text

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMRangeExceptionCode [struct]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMStyleSheet

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMStyleSheetList

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMText

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMText.replaceWholeText(String!) -> DOMText!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMText.wholeText

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified DOMTreeWalker

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMUIEvent

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMUIEvent.charCode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMUIEvent.initUIEvent(String!, canBubble: Bool, cancelable: Bool, view: DOMAbstractView!, detail: Int32)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMUIEvent.keyCode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMUIEvent.pageX

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMUIEvent.pageY

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMUIEvent.which

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMWheelEvent

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMWheelEvent.initWheelEvent(Int32, wheelDeltaY: Int32, view: DOMAbstractView!, screenX: Int32, screenY: Int32, clientX: Int32, clientY: Int32, ctrlKey: Bool, altKey: Bool, shiftKey: Bool, metaKey: Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMWheelEvent.wheelDeltaX

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMWheelEvent.wheelDeltaY

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMXPathExceptionCode [struct]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DOMXPathExpression

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMXPathExpression.evaluate(DOMNode!, type: UInt16, inResult: DOMXPathResult!) -> DOMXPathResult!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMXPathNSResolver

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DOMXPathResult

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

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

|  | Declaration |
| --- | --- |
| From | ``` func itemAtIndex(_ index: Int) -> WKBackForwardListItem! ``` |
| To | ``` func itemAtIndex(_ index: Int) -> WKBackForwardListItem? ``` |

Modified WKBackForwardListItem.URL

|  | Declaration |
| --- | --- |
| From | ``` var URL: NSURL! { get } ``` |
| To | ``` @NSCopying var URL: NSURL { get } ``` |

Modified WKBackForwardListItem.initialURL

|  | Declaration |
| --- | --- |
| From | ``` var initialURL: NSURL! { get } ``` |
| To | ``` @NSCopying var initialURL: NSURL { get } ``` |

Modified WKBackForwardListItem.title

|  | Declaration |
| --- | --- |
| From | ``` var title: String! { get } ``` |
| To | ``` var title: String? { get } ``` |

Modified WKFrameInfo.request

|  | Declaration |
| --- | --- |
| From | ``` var request: NSURLRequest! { get } ``` |
| To | ``` @NSCopying var request: NSURLRequest { get } ``` |

Modified WKNavigationAction.request

|  | Declaration |
| --- | --- |
| From | ``` var request: NSURLRequest! { get } ``` |
| To | ``` @NSCopying var request: NSURLRequest { get } ``` |

Modified WKNavigationAction.sourceFrame

|  | Declaration |
| --- | --- |
| From | ``` var sourceFrame: WKFrameInfo! { get } ``` |
| To | ``` @NSCopying var sourceFrame: WKFrameInfo? { get } ``` |

Modified WKNavigationAction.targetFrame

|  | Declaration |
| --- | --- |
| From | ``` var targetFrame: WKFrameInfo! { get } ``` |
| To | ``` @NSCopying var targetFrame: WKFrameInfo? { get } ``` |

Modified WKNavigationDelegate.webView(WKWebView, decidePolicyForNavigationAction: WKNavigationAction, decisionHandler:(WKNavigationActionPolicy) -> Void)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: WKWebView!, decidePolicyForNavigationAction navigationAction: WKNavigationAction!, decisionHandler decisionHandler: ((WKNavigationActionPolicy) -> Void)!) ``` | -- |
| To | ``` optional func webView(_ webView: WKWebView, decidePolicyForNavigationAction navigationAction: WKNavigationAction, decisionHandler decisionHandler: (WKNavigationActionPolicy) -> Void) ``` | yes |

Modified WKNavigationDelegate.webView(WKWebView, decidePolicyForNavigationResponse: WKNavigationResponse, decisionHandler:(WKNavigationResponsePolicy) -> Void)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: WKWebView!, decidePolicyForNavigationResponse navigationResponse: WKNavigationResponse!, decisionHandler decisionHandler: ((WKNavigationResponsePolicy) -> Void)!) ``` | -- |
| To | ``` optional func webView(_ webView: WKWebView, decidePolicyForNavigationResponse navigationResponse: WKNavigationResponse, decisionHandler decisionHandler: (WKNavigationResponsePolicy) -> Void) ``` | yes |

Modified WKNavigationDelegate.webView(WKWebView, didCommitNavigation: WKNavigation!)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: WKWebView!, didCommitNavigation navigation: WKNavigation!) ``` | -- |
| To | ``` optional func webView(_ webView: WKWebView, didCommitNavigation navigation: WKNavigation!) ``` | yes |

Modified WKNavigationDelegate.webView(WKWebView, didFailNavigation: WKNavigation!, withError: NSError)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: WKWebView!, didFailNavigation navigation: WKNavigation!, withError error: NSError!) ``` | -- |
| To | ``` optional func webView(_ webView: WKWebView, didFailNavigation navigation: WKNavigation!, withError error: NSError) ``` | yes |

Modified WKNavigationDelegate.webView(WKWebView, didFailProvisionalNavigation: WKNavigation!, withError: NSError)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: WKWebView!, didFailProvisionalNavigation navigation: WKNavigation!, withError error: NSError!) ``` | -- |
| To | ``` optional func webView(_ webView: WKWebView, didFailProvisionalNavigation navigation: WKNavigation!, withError error: NSError) ``` | yes |

Modified WKNavigationDelegate.webView(WKWebView, didFinishNavigation: WKNavigation!)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: WKWebView!, didFinishNavigation navigation: WKNavigation!) ``` | -- |
| To | ``` optional func webView(_ webView: WKWebView, didFinishNavigation navigation: WKNavigation!) ``` | yes |

Modified WKNavigationDelegate.webView(WKWebView, didReceiveAuthenticationChallenge: NSURLAuthenticationChallenge, completionHandler:(NSURLSessionAuthChallengeDisposition, NSURLCredential!) -> Void)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: WKWebView!, didReceiveAuthenticationChallenge challenge: NSURLAuthenticationChallenge!, completionHandler completionHandler: ((NSURLSessionAuthChallengeDisposition, NSURLCredential!) -> Void)!) ``` | -- |
| To | ``` optional func webView(_ webView: WKWebView, didReceiveAuthenticationChallenge challenge: NSURLAuthenticationChallenge, completionHandler completionHandler: (NSURLSessionAuthChallengeDisposition, NSURLCredential!) -> Void) ``` | yes |

Modified WKNavigationDelegate.webView(WKWebView, didReceiveServerRedirectForProvisionalNavigation: WKNavigation!)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: WKWebView!, didReceiveServerRedirectForProvisionalNavigation navigation: WKNavigation!) ``` | -- |
| To | ``` optional func webView(_ webView: WKWebView, didReceiveServerRedirectForProvisionalNavigation navigation: WKNavigation!) ``` | yes |

Modified WKNavigationDelegate.webView(WKWebView, didStartProvisionalNavigation: WKNavigation!)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: WKWebView!, didStartProvisionalNavigation navigation: WKNavigation!) ``` | -- |
| To | ``` optional func webView(_ webView: WKWebView, didStartProvisionalNavigation navigation: WKNavigation!) ``` | yes |

Modified WKNavigationResponse.response

|  | Declaration |
| --- | --- |
| From | ``` var response: NSURLResponse! { get } ``` |
| To | ``` @NSCopying var response: NSURLResponse { get } ``` |

Modified WKScriptMessage.body

|  | Declaration |
| --- | --- |
| From | ``` var body: AnyObject! { get } ``` |
| To | ``` @NSCopying var body: AnyObject { get } ``` |

Modified WKScriptMessage.frameInfo

|  | Declaration |
| --- | --- |
| From | ``` var frameInfo: WKFrameInfo! { get } ``` |
| To | ``` @NSCopying var frameInfo: WKFrameInfo { get } ``` |

Modified WKScriptMessage.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified WKScriptMessage.webView

|  | Declaration |
| --- | --- |
| From | ``` var webView: WKWebView! { get } ``` |
| To | ``` weak var webView: WKWebView? { get } ``` |

Modified WKScriptMessageHandler.userContentController(WKUserContentController, didReceiveScriptMessage: WKScriptMessage)

|  | Declaration |
| --- | --- |
| From | ``` func userContentController(_ userContentController: WKUserContentController!, didReceiveScriptMessage message: WKScriptMessage!) ``` |
| To | ``` func userContentController(_ userContentController: WKUserContentController, didReceiveScriptMessage message: WKScriptMessage) ``` |

Modified WKUIDelegate.webView(WKWebView, createWebViewWithConfiguration: WKWebViewConfiguration, forNavigationAction: WKNavigationAction, windowFeatures: WKWindowFeatures) -> WKWebView?

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: WKWebView!, createWebViewWithConfiguration configuration: WKWebViewConfiguration!, forNavigationAction navigationAction: WKNavigationAction!, windowFeatures windowFeatures: WKWindowFeatures!) -> WKWebView! ``` | -- |
| To | ``` optional func webView(_ webView: WKWebView, createWebViewWithConfiguration configuration: WKWebViewConfiguration, forNavigationAction navigationAction: WKNavigationAction, windowFeatures windowFeatures: WKWindowFeatures) -> WKWebView? ``` | yes |

Modified WKUIDelegate.webView(WKWebView, runJavaScriptAlertPanelWithMessage: String, initiatedByFrame: WKFrameInfo, completionHandler:() -> Void)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: WKWebView!, runJavaScriptAlertPanelWithMessage message: String!, initiatedByFrame frame: WKFrameInfo!, completionHandler completionHandler: (() -> Void)!) ``` | -- |
| To | ``` optional func webView(_ webView: WKWebView, runJavaScriptAlertPanelWithMessage message: String, initiatedByFrame frame: WKFrameInfo, completionHandler completionHandler: () -> Void) ``` | yes |

Modified WKUIDelegate.webView(WKWebView, runJavaScriptConfirmPanelWithMessage: String, initiatedByFrame: WKFrameInfo, completionHandler:(Bool) -> Void)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: WKWebView!, runJavaScriptConfirmPanelWithMessage message: String!, initiatedByFrame frame: WKFrameInfo!, completionHandler completionHandler: ((Bool) -> Void)!) ``` | -- |
| To | ``` optional func webView(_ webView: WKWebView, runJavaScriptConfirmPanelWithMessage message: String, initiatedByFrame frame: WKFrameInfo, completionHandler completionHandler: (Bool) -> Void) ``` | yes |

Modified WKUIDelegate.webView(WKWebView, runJavaScriptTextInputPanelWithPrompt: String, defaultText: String?, initiatedByFrame: WKFrameInfo, completionHandler:(String!) -> Void)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: WKWebView!, runJavaScriptTextInputPanelWithPrompt prompt: String!, defaultText defaultText: String!, initiatedByFrame frame: WKFrameInfo!, completionHandler completionHandler: ((String!) -> Void)!) ``` | -- |
| To | ``` optional func webView(_ webView: WKWebView, runJavaScriptTextInputPanelWithPrompt prompt: String, defaultText defaultText: String?, initiatedByFrame frame: WKFrameInfo, completionHandler completionHandler: (String!) -> Void) ``` | yes |

Modified WKUserContentController.addScriptMessageHandler(WKScriptMessageHandler, name: String)

|  | Declaration |
| --- | --- |
| From | ``` func addScriptMessageHandler(_ scriptMessageHandler: WKScriptMessageHandler!, name name: String!) ``` |
| To | ``` func addScriptMessageHandler(_ scriptMessageHandler: WKScriptMessageHandler, name name: String) ``` |

Modified WKUserContentController.addUserScript(WKUserScript)

|  | Declaration |
| --- | --- |
| From | ``` func addUserScript(_ userScript: WKUserScript!) ``` |
| To | ``` func addUserScript(_ userScript: WKUserScript) ``` |

Modified WKUserContentController.removeScriptMessageHandlerForName(String)

|  | Declaration |
| --- | --- |
| From | ``` func removeScriptMessageHandlerForName(_ name: String!) ``` |
| To | ``` func removeScriptMessageHandlerForName(_ name: String) ``` |

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

|  | Declaration |
| --- | --- |
| From | ``` init(source source: String!, injectionTime injectionTime: WKUserScriptInjectionTime, forMainFrameOnly forMainFrameOnly: Bool) ``` |
| To | ``` init(source source: String, injectionTime injectionTime: WKUserScriptInjectionTime, forMainFrameOnly forMainFrameOnly: Bool) ``` |

Modified WKWebView.UIDelegate

|  | Declaration |
| --- | --- |
| From | ``` var UIDelegate: WKUIDelegate! ``` |
| To | ``` weak var UIDelegate: WKUIDelegate? ``` |

Modified WKWebView.URL

|  | Declaration |
| --- | --- |
| From | ``` var URL: NSURL! { get } ``` |
| To | ``` @NSCopying var URL: NSURL? { get } ``` |

Modified WKWebView.backForwardList

|  | Declaration |
| --- | --- |
| From | ``` var backForwardList: WKBackForwardList! { get } ``` |
| To | ``` var backForwardList: WKBackForwardList { get } ``` |

Modified WKWebView.configuration

|  | Declaration |
| --- | --- |
| From | ``` var configuration: WKWebViewConfiguration! { get } ``` |
| To | ``` @NSCopying var configuration: WKWebViewConfiguration { get } ``` |

Modified WKWebView.evaluateJavaScript(String, completionHandler:((AnyObject!, NSError!) -> Void)?)

|  | Declaration |
| --- | --- |
| From | ``` func evaluateJavaScript(_ javaScriptString: String!, completionHandler completionHandler: ((AnyObject!, NSError!) -> Void)!) ``` |
| To | ``` func evaluateJavaScript(_ javaScriptString: String, completionHandler completionHandler: ((AnyObject!, NSError!) -> Void)?) ``` |

Modified WKWebView.init(frame: CGRect, configuration: WKWebViewConfiguration)

|  | Declaration |
| --- | --- |
| From | ``` init(frame frame: CGRect, configuration configuration: WKWebViewConfiguration!) ``` |
| To | ``` init(frame frame: CGRect, configuration configuration: WKWebViewConfiguration) ``` |

Modified WKWebView.goBack() -> WKNavigation?

|  | Declaration |
| --- | --- |
| From | ``` func goBack() -> WKNavigation! ``` |
| To | ``` func goBack() -> WKNavigation? ``` |

Modified WKWebView.goBack(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func goBack(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func goBack(_ sender: AnyObject?) ``` |

Modified WKWebView.goForward() -> WKNavigation?

|  | Declaration |
| --- | --- |
| From | ``` func goForward() -> WKNavigation! ``` |
| To | ``` func goForward() -> WKNavigation? ``` |

Modified WKWebView.goForward(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func goForward(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func goForward(_ sender: AnyObject?) ``` |

Modified WKWebView.goToBackForwardListItem(WKBackForwardListItem) -> WKNavigation?

|  | Declaration |
| --- | --- |
| From | ``` func goToBackForwardListItem(_ item: WKBackForwardListItem!) -> WKNavigation! ``` |
| To | ``` func goToBackForwardListItem(_ item: WKBackForwardListItem) -> WKNavigation? ``` |

Modified WKWebView.loadHTMLString(String, baseURL: NSURL?) -> WKNavigation?

|  | Declaration |
| --- | --- |
| From | ``` func loadHTMLString(_ string: String!, baseURL baseURL: NSURL!) -> WKNavigation! ``` |
| To | ``` func loadHTMLString(_ string: String, baseURL baseURL: NSURL?) -> WKNavigation? ``` |

Modified WKWebView.loadRequest(NSURLRequest) -> WKNavigation?

|  | Declaration |
| --- | --- |
| From | ``` func loadRequest(_ request: NSURLRequest!) -> WKNavigation! ``` |
| To | ``` func loadRequest(_ request: NSURLRequest) -> WKNavigation? ``` |

Modified WKWebView.navigationDelegate

|  | Declaration |
| --- | --- |
| From | ``` var navigationDelegate: WKNavigationDelegate! ``` |
| To | ``` weak var navigationDelegate: WKNavigationDelegate? ``` |

Modified WKWebView.reload() -> WKNavigation?

|  | Declaration |
| --- | --- |
| From | ``` func reload() -> WKNavigation! ``` |
| To | ``` func reload() -> WKNavigation? ``` |

Modified WKWebView.reload(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func reload(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func reload(_ sender: AnyObject?) ``` |

Modified WKWebView.reloadFromOrigin() -> WKNavigation?

|  | Declaration |
| --- | --- |
| From | ``` func reloadFromOrigin() -> WKNavigation! ``` |
| To | ``` func reloadFromOrigin() -> WKNavigation? ``` |

Modified WKWebView.reloadFromOrigin(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func reloadFromOrigin(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func reloadFromOrigin(_ sender: AnyObject?) ``` |

Modified WKWebView.stopLoading(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func stopLoading(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func stopLoading(_ sender: AnyObject?) ``` |

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

Modified WebArchive.data

|  | Declaration |
| --- | --- |
| From | ``` var data: NSData! { get } ``` |
| To | ``` @NSCopying var data: NSData! { get } ``` |

Modified WebArchive.init(data: NSData!)

|  | Declaration |
| --- | --- |
| From | ``` init(data data: NSData!) ``` |
| To | ``` init!(data data: NSData!) ``` |

Modified WebArchive.init(mainResource: WebResource!, subresources:[AnyObject]!, subframeArchives:[AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(mainResource mainResource: WebResource!, subresources subresources: [AnyObject]!, subframeArchives subframeArchives: [AnyObject]!) ``` |
| To | ``` init!(mainResource mainResource: WebResource!, subresources subresources: [AnyObject]!, subframeArchives subframeArchives: [AnyObject]!) ``` |

Modified WebDataSource.data

|  | Declaration |
| --- | --- |
| From | ``` var data: NSData! { get } ``` |
| To | ``` @NSCopying var data: NSData! { get } ``` |

Modified WebDataSource.init(request: NSURLRequest!)

|  | Declaration |
| --- | --- |
| From | ``` init(request request: NSURLRequest!) ``` |
| To | ``` init!(request request: NSURLRequest!) ``` |

Modified WebDragDestinationAction [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct WebDragDestinationAction : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var None: WebDragDestinationAction { get }     static var DHTML: WebDragDestinationAction { get }     static var Edit: WebDragDestinationAction { get }     static var Load: WebDragDestinationAction { get }     static var Any: WebDragDestinationAction { get } } ``` | RawOptionSet |
| To | ``` struct WebDragDestinationAction : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: WebDragDestinationAction { get }     static var DHTML: WebDragDestinationAction { get }     static var Edit: WebDragDestinationAction { get }     static var Load: WebDragDestinationAction { get }     static var Any: WebDragDestinationAction { get } } ``` | RawOptionSetType |

Modified WebDragDestinationAction.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified WebDragSourceAction [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct WebDragSourceAction : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var None: WebDragSourceAction { get }     static var DHTML: WebDragSourceAction { get }     static var Image: WebDragSourceAction { get }     static var Link: WebDragSourceAction { get }     static var Selection: WebDragSourceAction { get }     static var Any: WebDragSourceAction { get } } ``` | RawOptionSet |
| To | ``` struct WebDragSourceAction : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: WebDragSourceAction { get }     static var DHTML: WebDragSourceAction { get }     static var Image: WebDragSourceAction { get }     static var Link: WebDragSourceAction { get }     static var Selection: WebDragSourceAction { get }     static var Any: WebDragSourceAction { get } } ``` | RawOptionSetType |

Modified WebDragSourceAction.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified WebFrame.dataSource

|  | Declaration |
| --- | --- |
| From | ``` var dataSource: WebDataSource! { get } ``` |
| To | ``` var dataSource: WebDataSource? { get } ``` |

Modified WebFrame.globalContext

|  | Declaration |
| --- | --- |
| From | ``` var globalContext: JSGlobalContext! { get } ``` |
| To | ``` var globalContext: JSGlobalContextRef { get } ``` |

Modified WebFrame.init(name: String!, webFrameView: WebFrameView!, webView: WebView!)

|  | Declaration |
| --- | --- |
| From | ``` init(name name: String!, webFrameView view: WebFrameView!, webView webView: WebView!) ``` |
| To | ``` init!(name name: String!, webFrameView view: WebFrameView!, webView webView: WebView!) ``` |

Modified WebHistoryItem.init(URLString: String!, title: String!, lastVisitedTimeInterval: NSTimeInterval)

|  | Declaration |
| --- | --- |
| From | ``` init(URLString URLString: String!, title title: String!, lastVisitedTimeInterval time: NSTimeInterval) ``` |
| To | ``` init!(URLString URLString: String!, title title: String!, lastVisitedTimeInterval time: NSTimeInterval) ``` |

Modified WebOpenPanelResultListener.chooseFilenames([AnyObject]!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified WebPlugInViewFactory.plugInViewWithArguments([NSObject: AnyObject]!) -> NSView! [class]

|  | Declaration |
| --- | --- |
| From | ``` class func plugInViewWithArguments(_ arguments: [NSObject : AnyObject]!) -> NSView! ``` |
| To | ``` static func plugInViewWithArguments(_ arguments: [NSObject : AnyObject]!) -> NSView! ``` |

Modified WebPreferences.init(identifier: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(identifier anIdentifier: String!) ``` |
| To | ``` init!(identifier anIdentifier: String!) ``` |

Modified WebResource.data

|  | Declaration |
| --- | --- |
| From | ``` var data: NSData! { get } ``` |
| To | ``` @NSCopying var data: NSData! { get } ``` |

Modified WebResource.init(data: NSData!, URL: NSURL!, MIMEType: String!, textEncodingName: String!, frameName: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(data data: NSData!, URL URL: NSURL!, MIMEType MIMEType: String!, textEncodingName textEncodingName: String!, frameName frameName: String!) ``` |
| To | ``` init!(data data: NSData!, URL URL: NSURL!, MIMEType MIMEType: String!, textEncodingName textEncodingName: String!, frameName frameName: String!) ``` |

Modified WebScriptObject

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified WebScriptObject.JSObject() -> JSObjectRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSObject() -> Unmanaged<JSObject>! ``` | OS X 10.10 |
| To | ``` func JSObject() -> JSObjectRef ``` | OS X 10.5 |

Modified WebUndefined

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified WebView.UIDelegate

|  | Declaration |
| --- | --- |
| From | ``` var UIDelegate: AnyObject! ``` |
| To | ``` unowned(unsafe) var UIDelegate: AnyObject! ``` |

Modified WebView.alignCenter(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func alignCenter(_ sender: AnyObject!) ``` |
| To | ``` func alignCenter(_ sender: AnyObject?) ``` |

Modified WebView.alignJustified(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func alignJustified(_ sender: AnyObject!) ``` |
| To | ``` func alignJustified(_ sender: AnyObject?) ``` |

Modified WebView.alignLeft(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func alignLeft(_ sender: AnyObject!) ``` |
| To | ``` func alignLeft(_ sender: AnyObject?) ``` |

Modified WebView.alignRight(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func alignRight(_ sender: AnyObject!) ``` |
| To | ``` func alignRight(_ sender: AnyObject?) ``` |

Modified WebView.changeAttributes(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func changeAttributes(_ sender: AnyObject!) ``` |
| To | ``` func changeAttributes(_ sender: AnyObject?) ``` |

Modified WebView.changeColor(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func changeColor(_ sender: AnyObject!) ``` |
| To | ``` func changeColor(_ sender: AnyObject?) ``` |

Modified WebView.changeDocumentBackgroundColor(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func changeDocumentBackgroundColor(_ sender: AnyObject!) ``` |
| To | ``` func changeDocumentBackgroundColor(_ sender: AnyObject?) ``` |

Modified WebView.changeFont(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func changeFont(_ sender: AnyObject!) ``` |
| To | ``` func changeFont(_ sender: AnyObject?) ``` |

Modified WebView.checkSpelling(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func checkSpelling(_ sender: AnyObject!) ``` |
| To | ``` func checkSpelling(_ sender: AnyObject?) ``` |

Modified WebView.copy(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func copy(_ sender: AnyObject!) ``` |
| To | ``` func copy(_ sender: AnyObject?) ``` |

Modified WebView.copyFont(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func copyFont(_ sender: AnyObject!) ``` |
| To | ``` func copyFont(_ sender: AnyObject?) ``` |

Modified WebView.cut(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func cut(_ sender: AnyObject!) ``` |
| To | ``` func cut(_ sender: AnyObject?) ``` |

Modified WebView.delete(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func delete(_ sender: AnyObject!) ``` |
| To | ``` func delete(_ sender: AnyObject?) ``` |

Modified WebView.downloadDelegate

|  | Declaration |
| --- | --- |
| From | ``` var downloadDelegate: AnyObject! ``` |
| To | ``` unowned(unsafe) var downloadDelegate: AnyObject! ``` |

Modified WebView.init(frame: NSRect, frameName: String!, groupName: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(frame frame: NSRect, frameName frameName: String!, groupName groupName: String!) ``` |
| To | ``` init!(frame frame: NSRect, frameName frameName: String!, groupName groupName: String!) ``` |

Modified WebView.frameLoadDelegate

|  | Declaration |
| --- | --- |
| From | ``` var frameLoadDelegate: AnyObject! ``` |
| To | ``` unowned(unsafe) var frameLoadDelegate: AnyObject! ``` |

Modified WebView.goBack(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func goBack(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func goBack(_ sender: AnyObject?) ``` |

Modified WebView.goForward(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func goForward(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func goForward(_ sender: AnyObject?) ``` |

Modified WebView.makeTextLarger(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func makeTextLarger(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func makeTextLarger(_ sender: AnyObject?) ``` |

Modified WebView.makeTextSmaller(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func makeTextSmaller(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func makeTextSmaller(_ sender: AnyObject?) ``` |

Modified WebView.makeTextStandardSize(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func makeTextStandardSize(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func makeTextStandardSize(_ sender: AnyObject?) ``` |

Modified WebView.moveToBeginningOfSentence(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func moveToBeginningOfSentence(_ sender: AnyObject!) ``` |
| To | ``` func moveToBeginningOfSentence(_ sender: AnyObject?) ``` |

Modified WebView.moveToBeginningOfSentenceAndModifySelection(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func moveToBeginningOfSentenceAndModifySelection(_ sender: AnyObject!) ``` |
| To | ``` func moveToBeginningOfSentenceAndModifySelection(_ sender: AnyObject?) ``` |

Modified WebView.moveToEndOfSentence(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func moveToEndOfSentence(_ sender: AnyObject!) ``` |
| To | ``` func moveToEndOfSentence(_ sender: AnyObject?) ``` |

Modified WebView.moveToEndOfSentenceAndModifySelection(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func moveToEndOfSentenceAndModifySelection(_ sender: AnyObject!) ``` |
| To | ``` func moveToEndOfSentenceAndModifySelection(_ sender: AnyObject?) ``` |

Modified WebView.overWrite(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func overWrite(_ sender: AnyObject!) ``` |
| To | ``` func overWrite(_ sender: AnyObject?) ``` |

Modified WebView.paste(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func paste(_ sender: AnyObject!) ``` |
| To | ``` func paste(_ sender: AnyObject?) ``` |

Modified WebView.pasteAsPlainText(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func pasteAsPlainText(_ sender: AnyObject!) ``` |
| To | ``` func pasteAsPlainText(_ sender: AnyObject?) ``` |

Modified WebView.pasteAsRichText(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func pasteAsRichText(_ sender: AnyObject!) ``` |
| To | ``` func pasteAsRichText(_ sender: AnyObject?) ``` |

Modified WebView.pasteFont(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func pasteFont(_ sender: AnyObject!) ``` |
| To | ``` func pasteFont(_ sender: AnyObject?) ``` |

Modified WebView.performFindPanelAction(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func performFindPanelAction(_ sender: AnyObject!) ``` |
| To | ``` func performFindPanelAction(_ sender: AnyObject?) ``` |

Modified WebView.policyDelegate

|  | Declaration |
| --- | --- |
| From | ``` var policyDelegate: AnyObject! ``` |
| To | ``` unowned(unsafe) var policyDelegate: AnyObject! ``` |

Modified WebView.reload(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func reload(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func reload(_ sender: AnyObject?) ``` |

Modified WebView.reloadFromOrigin(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func reloadFromOrigin(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func reloadFromOrigin(_ sender: AnyObject?) ``` |

Modified WebView.resourceLoadDelegate

|  | Declaration |
| --- | --- |
| From | ``` var resourceLoadDelegate: AnyObject! ``` |
| To | ``` unowned(unsafe) var resourceLoadDelegate: AnyObject! ``` |

Modified WebView.selectSentence(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func selectSentence(_ sender: AnyObject!) ``` |
| To | ``` func selectSentence(_ sender: AnyObject?) ``` |

Modified WebView.showGuessPanel(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func showGuessPanel(_ sender: AnyObject!) ``` |
| To | ``` func showGuessPanel(_ sender: AnyObject?) ``` |

Modified WebView.startSpeaking(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func startSpeaking(_ sender: AnyObject!) ``` |
| To | ``` func startSpeaking(_ sender: AnyObject?) ``` |

Modified WebView.stopLoading(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func stopLoading(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func stopLoading(_ sender: AnyObject?) ``` |

Modified WebView.stopSpeaking(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func stopSpeaking(_ sender: AnyObject!) ``` |
| To | ``` func stopSpeaking(_ sender: AnyObject?) ``` |

Modified WebView.takeStringURLFrom(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func takeStringURLFrom(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func takeStringURLFrom(_ sender: AnyObject?) ``` |

Modified WebView.toggleContinuousSpellChecking(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func toggleContinuousSpellChecking(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func toggleContinuousSpellChecking(_ sender: AnyObject?) ``` |

Modified WebView.toggleSmartInsertDelete(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func toggleSmartInsertDelete(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func toggleSmartInsertDelete(_ sender: AnyObject?) ``` |

Modified DOMEventException

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DOMEventException: NSString! ``` | OS X 10.10 |
| To | ``` let DOMEventException: String ``` | OS X 10.4 |

Modified DOMException

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DOMException: NSString! ``` | OS X 10.10 |
| To | ``` let DOMException: String ``` | OS X 10.4 |

Modified DOMRangeException

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DOMRangeException: NSString! ``` | OS X 10.10 |
| To | ``` let DOMRangeException: String ``` | OS X 10.4 |

Modified DOMXPathException

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DOMXPathException: NSString! ``` | OS X 10.10 |
| To | ``` let DOMXPathException: String ``` | OS X 10.4 |

Modified WKErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let WKErrorDomain: NSString! ``` |
| To | ``` let WKErrorDomain: String ``` |

Modified WebActionButtonKey

|  | Declaration |
| --- | --- |
| From | ``` var WebActionButtonKey: NSString! ``` |
| To | ``` let WebActionButtonKey: String ``` |

Modified WebActionElementKey

|  | Declaration |
| --- | --- |
| From | ``` var WebActionElementKey: NSString! ``` |
| To | ``` let WebActionElementKey: String ``` |

Modified WebActionModifierFlagsKey

|  | Declaration |
| --- | --- |
| From | ``` var WebActionModifierFlagsKey: NSString! ``` |
| To | ``` let WebActionModifierFlagsKey: String ``` |

Modified WebActionNavigationTypeKey

|  | Declaration |
| --- | --- |
| From | ``` var WebActionNavigationTypeKey: NSString! ``` |
| To | ``` let WebActionNavigationTypeKey: String ``` |

Modified WebActionOriginalURLKey

|  | Declaration |
| --- | --- |
| From | ``` var WebActionOriginalURLKey: NSString! ``` |
| To | ``` let WebActionOriginalURLKey: String ``` |

Modified WebArchivePboardType

|  | Declaration |
| --- | --- |
| From | ``` var WebArchivePboardType: NSString! ``` |
| To | ``` let WebArchivePboardType: String ``` |

Modified WebElementDOMNodeKey

|  | Declaration |
| --- | --- |
| From | ``` var WebElementDOMNodeKey: NSString! ``` |
| To | ``` let WebElementDOMNodeKey: String ``` |

Modified WebElementFrameKey

|  | Declaration |
| --- | --- |
| From | ``` var WebElementFrameKey: NSString! ``` |
| To | ``` let WebElementFrameKey: String ``` |

Modified WebElementImageAltStringKey

|  | Declaration |
| --- | --- |
| From | ``` var WebElementImageAltStringKey: NSString! ``` |
| To | ``` let WebElementImageAltStringKey: String ``` |

Modified WebElementImageKey

|  | Declaration |
| --- | --- |
| From | ``` var WebElementImageKey: NSString! ``` |
| To | ``` let WebElementImageKey: String ``` |

Modified WebElementImageRectKey

|  | Declaration |
| --- | --- |
| From | ``` var WebElementImageRectKey: NSString! ``` |
| To | ``` let WebElementImageRectKey: String ``` |

Modified WebElementImageURLKey

|  | Declaration |
| --- | --- |
| From | ``` var WebElementImageURLKey: NSString! ``` |
| To | ``` let WebElementImageURLKey: String ``` |

Modified WebElementIsSelectedKey

|  | Declaration |
| --- | --- |
| From | ``` var WebElementIsSelectedKey: NSString! ``` |
| To | ``` let WebElementIsSelectedKey: String ``` |

Modified WebElementLinkLabelKey

|  | Declaration |
| --- | --- |
| From | ``` var WebElementLinkLabelKey: NSString! ``` |
| To | ``` let WebElementLinkLabelKey: String ``` |

Modified WebElementLinkTargetFrameKey

|  | Declaration |
| --- | --- |
| From | ``` var WebElementLinkTargetFrameKey: NSString! ``` |
| To | ``` let WebElementLinkTargetFrameKey: String ``` |

Modified WebElementLinkTitleKey

|  | Declaration |
| --- | --- |
| From | ``` var WebElementLinkTitleKey: NSString! ``` |
| To | ``` let WebElementLinkTitleKey: String ``` |

Modified WebElementLinkURLKey

|  | Declaration |
| --- | --- |
| From | ``` var WebElementLinkURLKey: NSString! ``` |
| To | ``` let WebElementLinkURLKey: String ``` |

Modified WebHistoryAllItemsRemovedNotification

|  | Declaration |
| --- | --- |
| From | ``` var WebHistoryAllItemsRemovedNotification: NSString! ``` |
| To | ``` let WebHistoryAllItemsRemovedNotification: String ``` |

Modified WebHistoryItemChangedNotification

|  | Declaration |
| --- | --- |
| From | ``` var WebHistoryItemChangedNotification: NSString! ``` |
| To | ``` let WebHistoryItemChangedNotification: String ``` |

Modified WebHistoryItemsAddedNotification

|  | Declaration |
| --- | --- |
| From | ``` var WebHistoryItemsAddedNotification: NSString! ``` |
| To | ``` let WebHistoryItemsAddedNotification: String ``` |

Modified WebHistoryItemsKey

|  | Declaration |
| --- | --- |
| From | ``` var WebHistoryItemsKey: NSString! ``` |
| To | ``` let WebHistoryItemsKey: String ``` |

Modified WebHistoryItemsRemovedNotification

|  | Declaration |
| --- | --- |
| From | ``` var WebHistoryItemsRemovedNotification: NSString! ``` |
| To | ``` let WebHistoryItemsRemovedNotification: String ``` |

Modified WebHistoryLoadedNotification

|  | Declaration |
| --- | --- |
| From | ``` var WebHistoryLoadedNotification: NSString! ``` |
| To | ``` let WebHistoryLoadedNotification: String ``` |

Modified WebHistorySavedNotification

|  | Declaration |
| --- | --- |
| From | ``` var WebHistorySavedNotification: NSString! ``` |
| To | ``` let WebHistorySavedNotification: String ``` |

Modified WebKitErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` var WebKitErrorDomain: NSString! ``` |
| To | ``` let WebKitErrorDomain: String ``` |

Modified WebKitErrorMIMETypeKey

|  | Declaration |
| --- | --- |
| From | ``` let WebKitErrorMIMETypeKey: NSString! ``` |
| To | ``` let WebKitErrorMIMETypeKey: String ``` |

Modified WebKitErrorPlugInNameKey

|  | Declaration |
| --- | --- |
| From | ``` let WebKitErrorPlugInNameKey: NSString! ``` |
| To | ``` let WebKitErrorPlugInNameKey: String ``` |

Modified WebKitErrorPlugInPageURLStringKey

|  | Declaration |
| --- | --- |
| From | ``` let WebKitErrorPlugInPageURLStringKey: NSString! ``` |
| To | ``` let WebKitErrorPlugInPageURLStringKey: String ``` |

Modified WebPlugInAttributesKey

|  | Declaration |
| --- | --- |
| From | ``` var WebPlugInAttributesKey: NSString! ``` |
| To | ``` let WebPlugInAttributesKey: String ``` |

Modified WebPlugInBaseURLKey

|  | Declaration |
| --- | --- |
| From | ``` var WebPlugInBaseURLKey: NSString! ``` |
| To | ``` let WebPlugInBaseURLKey: String ``` |

Modified WebPlugInContainerKey

|  | Declaration |
| --- | --- |
| From | ``` var WebPlugInContainerKey: NSString! ``` |
| To | ``` let WebPlugInContainerKey: String ``` |

Modified WebPlugInContainingElementKey

|  | Declaration |
| --- | --- |
| From | ``` var WebPlugInContainingElementKey: NSString! ``` |
| To | ``` let WebPlugInContainingElementKey: String ``` |

Modified WebPlugInShouldLoadMainResourceKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var WebPlugInShouldLoadMainResourceKey: NSString! ``` | OS X 10.10 |
| To | ``` let WebPlugInShouldLoadMainResourceKey: String ``` | OS X 10.6 |

Modified WebPreferencesChangedNotification

|  | Declaration |
| --- | --- |
| From | ``` var WebPreferencesChangedNotification: NSString! ``` |
| To | ``` let WebPreferencesChangedNotification: String ``` |

Modified WebViewDidBeginEditingNotification

|  | Declaration |
| --- | --- |
| From | ``` let WebViewDidBeginEditingNotification: NSString! ``` |
| To | ``` let WebViewDidBeginEditingNotification: String ``` |

Modified WebViewDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let WebViewDidChangeNotification: NSString! ``` |
| To | ``` let WebViewDidChangeNotification: String ``` |

Modified WebViewDidChangeSelectionNotification

|  | Declaration |
| --- | --- |
| From | ``` let WebViewDidChangeSelectionNotification: NSString! ``` |
| To | ``` let WebViewDidChangeSelectionNotification: String ``` |

Modified WebViewDidChangeTypingStyleNotification

|  | Declaration |
| --- | --- |
| From | ``` let WebViewDidChangeTypingStyleNotification: NSString! ``` |
| To | ``` let WebViewDidChangeTypingStyleNotification: String ``` |

Modified WebViewDidEndEditingNotification

|  | Declaration |
| --- | --- |
| From | ``` let WebViewDidEndEditingNotification: NSString! ``` |
| To | ``` let WebViewDidEndEditingNotification: String ``` |

Modified WebViewProgressEstimateChangedNotification

|  | Declaration |
| --- | --- |
| From | ``` var WebViewProgressEstimateChangedNotification: NSString! ``` |
| To | ``` let WebViewProgressEstimateChangedNotification: String ``` |

Modified WebViewProgressFinishedNotification

|  | Declaration |
| --- | --- |
| From | ``` var WebViewProgressFinishedNotification: NSString! ``` |
| To | ``` let WebViewProgressFinishedNotification: String ``` |

Modified WebViewProgressStartedNotification

|  | Declaration |
| --- | --- |
| From | ``` var WebViewProgressStartedNotification: NSString! ``` |
| To | ``` let WebViewProgressStartedNotification: String ``` |

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
