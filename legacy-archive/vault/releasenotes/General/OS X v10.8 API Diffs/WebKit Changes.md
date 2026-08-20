---
title: OS X v10.8 API Diffs
apple_id: TP40011748
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_8/WebKit.html
archived_at: '2026-07-18T02:54:06.988735Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.8 API Diffs](OS%20X%20v10.7%20to%20OS%20X%20v10.8%20API%20Differences.md)


# WebKit Changes

## WebKit

DOMCSSPrimitiveValue.hAdded [DOM_CSS_VH](https://developer.apple.com/documentation/webkit/1418446-dom_measurement_enumeration_lega/dom_css_vh)Added [DOM_CSS_VMIN](https://developer.apple.com/documentation/webkit/1418446-dom_measurement_enumeration_lega/dom_css_vmin)Added [DOM_CSS_VW](https://developer.apple.com/documentation/webkit/1418446-dom_measurement_enumeration_lega/dom_css_vw)DOMElement.hRemoved -[DOMElement contains:]DOMEvent.hAdded [DOM_NONE](https://developer.apple.com/documentation/webkit/1558620-dom_phase_enumeration_legacy/dom_none)DOMFile.hRemoved DOMFile.fileNameRemoved DOMFile.fileSizeDOMHTMLAnchorElement.hAdded DOMHTMLAnchorElement.AVAILABLE_WEBKIT_VERSION_1_3_AND_LATER_BUT_DEPRECATED_AFTER_WEBKIT_VERSION_5_1 (no architecture available)DOMHTMLAreaElement.hAdded DOMHTMLAreaElement.AVAILABLE_WEBKIT_VERSION_1_3_AND_LATER_BUT_DEPRECATED_AFTER_WEBKIT_VERSION_5_1 (no architecture available)DOMHTMLButtonElement.hAdded DOMHTMLButtonElement.AVAILABLE_WEBKIT_VERSION_1_3_AND_LATER_BUT_DEPRECATED_AFTER_WEBKIT_VERSION_5_1 (no architecture available)DOMHTMLElement.hAdded DOMHTMLElement.AVAILABLE_AFTER_WEBKIT_VERSION_5_1 (no architecture available)Added -[DOMHTMLElement AVAILABLE_AFTER_WEBKIT_VERSION_5_1] (no architecture available)Added [DOMHTMLElement.accessKey](https://developer.apple.com/documentation/webkit/domhtmlelement/1536534-accesskey)Added [-[DOMHTMLElement click]](https://developer.apple.com/documentation/webkit/domhtmlelement/1537554-click)DOMHTMLInputElement.hAdded DOMHTMLInputElement.AVAILABLE_WEBKIT_VERSION_1_3_AND_LATER_BUT_DEPRECATED_AFTER_WEBKIT_VERSION_5_1 (no architecture available)DOMHTMLIsIndexElement.hRemoved DOMHTMLIsIndexElementRemoved DOMHTMLIsIndexElement.formRemoved DOMHTMLIsIndexElement.promptDOMHTMLLabelElement.hAdded DOMHTMLLabelElement.AVAILABLE_WEBKIT_VERSION_1_3_AND_LATER_BUT_DEPRECATED_AFTER_WEBKIT_VERSION_5_1 (no architecture available)DOMHTMLLegendElement.hAdded DOMHTMLLegendElement.AVAILABLE_WEBKIT_VERSION_1_3_AND_LATER_BUT_DEPRECATED_AFTER_WEBKIT_VERSION_5_1 (no architecture available)DOMHTMLSelectElement.hModified DOMHTMLSelectElement.AVAILABLE_IN_WEBKIT_VERSION_4_0

|  | Declaration |
| --- | --- |
| From | @property(readonly) BOOL willValidate AVAILABLE_IN_WEBKIT_VERSION_4_0 |
| To | @property BOOL autofocus AVAILABLE_IN_WEBKIT_VERSION_4_0 |

DOMHTMLTextAreaElement.hAdded DOMHTMLTextAreaElement.AVAILABLE_WEBKIT_VERSION_1_3_AND_LATER_BUT_DEPRECATED_AFTER_WEBKIT_VERSION_5_1 (no architecture available)DOMNode.hAdded [-[DOMNode contains:]](https://developer.apple.com/documentation/webkit/domnode/1517986-contains)DOMProgressEvent.hRemoved -[DOMProgressEvent initProgressEvent:canBubbleArg:cancelableArg:lengthComputableArg:loadedArg:totalArg:]DOMUIEvent.hAdded DOMUIEvent.AVAILABLE_WEBKIT_VERSION_3_0_AND_LATER_BUT_DEPRECATED (no architecture available)WebKitErrors.hAdded [WebKitErrorBlockedPlugInVersion](https://developer.apple.com/documentation/webkit/webkiterrorblockedpluginversion)WebPreferences.hAdded [-[WebPreferences setSuppressesIncrementalRendering:]](https://developer.apple.com/documentation/webkit/webpreferences/1537563-suppressesincrementalrendering)Added [-[WebPreferences suppressesIncrementalRendering]](https://developer.apple.com/documentation/webkit/webpreferences/1537563-suppressesincrementalrendering)npapi.hAdded [NPNVcontentsScaleFactor](https://developer.apple.com/documentation/webkit/npnvariable/npnvcontentsscalefactor)Added [NPNVsupportsCompositingCoreAnimationPluginsBool](https://developer.apple.com/documentation/webkit/npnvariable/npnvsupportscompositingcoreanimationpluginsbool)Added [NPNVsupportsUpdatedCocoaTextInputBool](https://developer.apple.com/documentation/webkit/npnvariable/npnvsupportsupdatedcocoatextinputbool)Modified NPP_GetMIMEDescription()

|  | Declaration |
| --- | --- |
| From | char \* NPP_GetMIMEDescription ( void); |
| To | const char \* NPP_GetMIMEDescription ( void); |

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
