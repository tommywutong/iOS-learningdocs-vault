---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/WebKit.html
archived_at: '2026-07-18T02:54:22.324295Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# WebKit Changes

## WebKit

DOMCSSPrimitiveValue.hAdded [DOM_CSS_VMAX](https://developer.apple.com/documentation/webkit/dom_css_vmax)DOMCSSRule.hAdded [DOM_WEBKIT_REGION_RULE](https://developer.apple.com/documentation/webkit/1403866-dom_rule_enumeration_legacy/dom_webkit_region_rule)DOMCSSStyleDeclaration.hModified [-[DOMCSSStyleDeclaration getPropertyShorthand:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1580826-getpropertyshorthand)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

DOMElement.hAdded [DOMElement.className](https://developer.apple.com/documentation/webkit/domelement/1476224-classname)DOMHTMLButtonElement.hModified [DOMHTMLButtonElement.type](https://developer.apple.com/documentation/webkit/domhtmlbuttonelement/1532480-type)

|  | Declaration |
| --- | --- |
| From | @property(readonly, copy) NSString \*type |
| To | @property(copy) NSString \*type |

DOMHTMLElement.hRemoved DOMHTMLElement.classNameDOMHTMLInputElement.hModified [DOMHTMLInputElement.files](https://developer.apple.com/documentation/webkit/domhtmlinputelement/1501400-files)

|  | Declaration |
| --- | --- |
| From | @property(readonly, retain) DOMFileList \*files |
| To | @property(retain) DOMFileList \*files |

DOMWheelEvent.hRemoved DOMWheelEvent.altKeyRemoved DOMWheelEvent.clientXRemoved DOMWheelEvent.clientYRemoved DOMWheelEvent.ctrlKeyRemoved DOMWheelEvent.metaKeyRemoved DOMWheelEvent.offsetXRemoved DOMWheelEvent.offsetYRemoved DOMWheelEvent.screenXRemoved DOMWheelEvent.screenYRemoved DOMWheelEvent.shiftKeyRemoved DOMWheelEvent.xRemoved DOMWheelEvent.yAdded [DOM_DOM_DELTA_LINE](https://developer.apple.com/documentation/webkit/1420212-dom_delta_enumeration_legacy/dom_dom_delta_line)Added [DOM_DOM_DELTA_PAGE](https://developer.apple.com/documentation/webkit/1420212-dom_delta_enumeration_legacy/dom_dom_delta_page)Added [DOM_DOM_DELTA_PIXEL](https://developer.apple.com/documentation/webkit/1420212-dom_delta_enumeration_legacy/dom_dom_delta_pixel)Modified [DOMWheelEvent](https://developer.apple.com/documentation/webkit/domwheelevent)

|  | Superclass |
| --- | --- |
| From | DOMUIEvent |
| To | DOMMouseEvent |

WebFrame.hAdded [-[WebFrame javaScriptContext]](https://developer.apple.com/documentation/webkit/webframe/1494240-javascriptcontext)WebFrameLoadDelegate.hAdded -[NSObject webView:didCreateJavaScriptContext:forFrame:]WebJavaPlugIn.hRemoved -[NSObject webPlugInCallJava:isStatic:returnType:method:arguments:callingURL:exceptionDescription:]Removed -[NSObject webPlugInGetApplet]Removed NSObject(WebJavaPlugIn)Removed WebJNIReturnTypeRemoved WebJNIReturnTypeBooleanRemoved WebJNIReturnTypeByteRemoved WebJNIReturnTypeCharRemoved WebJNIReturnTypeDoubleRemoved WebJNIReturnTypeFloatRemoved WebJNIReturnTypeIntRemoved WebJNIReturnTypeInvalidRemoved WebJNIReturnTypeLongRemoved WebJNIReturnTypeObjectRemoved WebJNIReturnTypeShortRemoved WebJNIReturnTypeVoidWebPreferences.hAdded [WebPreferencesPrivate](https://developer.apple.com/documentation/webkit/webpreferencesprivate)WebScriptObject.hAdded [-[WebScriptObject JSValue]](https://developer.apple.com/documentation/webkit/webscriptobject/1528534-jsvalue)Added #def WebScriptObject_hWebView.hAdded [-[WebView overWrite:]](https://developer.apple.com/documentation/webkit/webview/1408506-overwrite)npapi.hAdded [NPNVsupportsAdvancedKeyHandling](https://developer.apple.com/documentation/webkit/npnvariable/npnvsupportsadvancedkeyhandling)

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
