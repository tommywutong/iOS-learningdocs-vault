---
title: API Changes in Snow Leopard
apple_id: TP40007673
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2008-06-09'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSX/SnowLeopard_API_ReleaseNote/WebKit.html
archived_at: '2026-07-18T02:58:45.902500Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [API Changes in Snow Leopard](API%20Changes%20in%20Snow%20Leopard.md)


[ADC Home](https://developer.apple.com/) >
[Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) >
Release Notes >
OS X >
[API Changes in Snow Leopard Developer Preview](API%20Changes%20in%20Snow%20Leopard.md) >

# WebKit Changes

## WebKit

DOMDocument.hAdded [DOMDocument.URL](https://developer.apple.com/documentation/webkit/domdocument/1494913-url)Added [DOMDocument.anchors](https://developer.apple.com/documentation/webkit/domdocument/1494855-anchors)Added [DOMDocument.applets](https://developer.apple.com/documentation/webkit/domdocument/1494970-applets)Added [DOMDocument.body](https://developer.apple.com/documentation/webkit/domdocument/1494850-body)Added [DOMDocument.cookie](https://developer.apple.com/documentation/webkit/domdocument/1494943-cookie)Added [DOMDocument.domain](https://developer.apple.com/documentation/webkit/domdocument/1494936-domain)Added [DOMDocument.forms](https://developer.apple.com/documentation/webkit/domdocument/1494929-forms)Added [-[DOMDocument getElementsByName:]](https://developer.apple.com/documentation/webkit/domdocument/1494897-getelementsbyname)Added [DOMDocument.images](https://developer.apple.com/documentation/webkit/domdocument/1494864-images)Added [DOMDocument.links](https://developer.apple.com/documentation/webkit/domdocument/1494895-links)Added [DOMDocument.referrer](https://developer.apple.com/documentation/webkit/domdocument/1494955-referrer)Added [DOMDocument.title](https://developer.apple.com/documentation/webkit/domdocument/1494946-title)DOMElement.hRemoved [-[DOMElement blur]](https://developer.apple.com/documentation/webkit/domelement/1476187-blur)Removed [-[DOMElement focus]](https://developer.apple.com/documentation/webkit/domelement/1476261-focus)DOMHTMLAnchorElement.hRemoved -[DOMHTMLAnchorElement blur]Removed -[DOMHTMLAnchorElement focus]Removed DOMHTMLAnchorElement.tabIndexDOMHTMLAreaElement.hRemoved DOMHTMLAreaElement.tabIndexDOMHTMLButtonElement.hRemoved DOMHTMLButtonElement.tabIndexDOMHTMLDocument.hRemoved DOMHTMLDocument.URLRemoved DOMHTMLDocument.anchorsRemoved DOMHTMLDocument.appletsRemoved DOMHTMLDocument.bodyRemoved DOMHTMLDocument.cookieRemoved DOMHTMLDocument.domainRemoved DOMHTMLDocument.formsRemoved -[DOMHTMLDocument getElementById:]Removed -[DOMHTMLDocument getElementsByName:]Removed DOMHTMLDocument.imagesRemoved DOMHTMLDocument.linksRemoved DOMHTMLDocument.referrerRemoved DOMHTMLDocument.titleDOMHTMLElement.hAdded -[DOMHTMLElement blur]Added -[DOMHTMLElement focus]Added [DOMHTMLElement.tabIndex](https://developer.apple.com/documentation/webkit/domhtmlelement/1537290-tabindex)DOMHTMLInputElement.hRemoved -[DOMHTMLInputElement blur]Removed -[DOMHTMLInputElement focus]Removed DOMHTMLInputElement.tabIndexDOMHTMLObjectElement.hRemoved DOMHTMLObjectElement.tabIndexDOMHTMLSelectElement.hRemoved -[DOMHTMLSelectElement blur]Removed -[DOMHTMLSelectElement focus]Removed DOMHTMLSelectElement.tabIndexDOMHTMLTextAreaElement.hRemoved -[DOMHTMLTextAreaElement blur]Removed -[DOMHTMLTextAreaElement focus]Removed DOMHTMLTextAreaElement.tabIndexDOMProgressEvent.hAdded [DOMProgressEvent](https://developer.apple.com/documentation/webkit/domprogressevent)Added -[DOMProgressEvent initProgressEvent:canBubbleArg:cancelableArg:lengthComputableArg:loadedArg:totalArg:]Added [DOMProgressEvent.lengthComputable](https://developer.apple.com/documentation/webkit/domprogressevent/1515418-lengthcomputable)Added [DOMProgressEvent.loaded](https://developer.apple.com/documentation/webkit/domprogressevent/1515419-loaded)Added [DOMProgressEvent.total](https://developer.apple.com/documentation/webkit/domprogressevent/1515420-total)HIWebView.hRemoved HIWebViewCreateWithClass()WebScriptObject.hModified [-[WebScriptObject callWebScriptMethod:withArguments:]](https://developer.apple.com/documentation/webkit/webscriptobject/1528556-callwebscriptmethod)

|  | Declaration |
| --- | --- |
| Old | - (id)callWebScriptMethod:(NSString \*)name withArguments:(NSArray \*)args |
| New | - (id)callWebScriptMethod:(NSString \*)name withArguments:(NSArray \*)arguments |

Modified [-[NSObject invokeDefaultMethodWithArguments:]](https://developer.apple.com/documentation/objectivec/nsobject/1528543-invokedefaultmethodwitharguments)

|  | Declaration |
| --- | --- |
| Old | - (id)invokeDefaultMethodWithArguments:(NSArray \*)args |
| New | - (id)invokeDefaultMethodWithArguments:(NSArray \*)arguments |

Modified [+[NSObject isSelectorExcludedFromWebScript:]](https://developer.apple.com/documentation/objectivec/nsobject/1528532-isselectorexcludedfromwebscript)

|  | Declaration |
| --- | --- |
| Old | + (BOOL)isSelectorExcludedFromWebScript:(SEL)aSelector |
| New | + (BOOL)isSelectorExcludedFromWebScript:(SEL)selector |

Modified [+[NSObject webScriptNameForSelector:]](https://developer.apple.com/documentation/objectivec/nsobject/1528539-webscriptnameforselector)

|  | Declaration |
| --- | --- |
| Old | + (NSString \*)webScriptNameForSelector:(SEL)aSelector |
| New | + (NSString \*)webScriptNameForSelector:(SEL)selector |

Modified [-[NSObject invokeUndefinedMethodFromWebScript:withArguments:]](https://developer.apple.com/documentation/objectivec/nsobject/1528562-invokeundefinedmethod)

|  | Declaration |
| --- | --- |
| Old | - (id)invokeUndefinedMethodFromWebScript:(NSString \*)name withArguments:(NSArray \*)args |
| New | - (id)invokeUndefinedMethodFromWebScript:(NSString \*)name withArguments:(NSArray \*)arguments |

npapi.hAdded [NPCocoaEvent](https://developer.apple.com/documentation/webkit/npcocoaevent)Added [NPCocoaEventDrawRect](https://developer.apple.com/documentation/webkit/npcocoaeventtype/npcocoaeventdrawrect)Added [NPCocoaEventFlagsChanged](https://developer.apple.com/documentation/webkit/npcocoaeventtype/npcocoaeventflagschanged)Added [NPCocoaEventFocusChanged](https://developer.apple.com/documentation/webkit/npcocoaeventtype/npcocoaeventfocuschanged)Added [NPCocoaEventKeyDown](https://developer.apple.com/documentation/webkit/npcocoaeventtype/npcocoaeventkeydown)Added [NPCocoaEventKeyUp](https://developer.apple.com/documentation/webkit/npcocoaeventtype/npcocoaeventkeyup)Added [NPCocoaEventMouseDown](https://developer.apple.com/documentation/webkit/npcocoaeventtype/npcocoaeventmousedown)Added [NPCocoaEventMouseDragged](https://developer.apple.com/documentation/webkit/npcocoaeventtype/npcocoaeventmousedragged)Added [NPCocoaEventMouseEntered](https://developer.apple.com/documentation/webkit/npcocoaeventtype/npcocoaeventmouseentered)Added [NPCocoaEventMouseExited](https://developer.apple.com/documentation/webkit/npcocoaeventtype/npcocoaeventmouseexited)Added [NPCocoaEventMouseMoved](https://developer.apple.com/documentation/webkit/npcocoaeventtype/npcocoaeventmousemoved)Added [NPCocoaEventMouseUp](https://developer.apple.com/documentation/webkit/npcocoaeventtype/npcocoaeventmouseup)Added [NPCocoaEventScrollWheel](https://developer.apple.com/documentation/webkit/npcocoaeventtype/npcocoaeventscrollwheel)Added [NPCocoaEventType](https://developer.apple.com/documentation/webkit/npcocoaeventtype)Added [NPCocoaEventWindowFocusChanged](https://developer.apple.com/documentation/webkit/npcocoaeventtype/npcocoaeventwindowfocuschanged)Added [NPEventModel](https://developer.apple.com/documentation/webkit/npeventmodel)Added NPEventModelCarbonAdded [NPEventModelCocoa](https://developer.apple.com/documentation/webkit/npeventmodel/npeventmodelcocoa)Added [NPMenu](https://developer.apple.com/documentation/webkit/npmenu)Added [NPNSMenu](https://developer.apple.com/documentation/webkit/npnsmenu)Added [NPNSString](https://developer.apple.com/documentation/webkit/npnsstring)Added [NPNSWindow](https://developer.apple.com/documentation/webkit/npnswindow)Added NPNVbrowserTextInputFuncsAdded NPNVsupportsCarbonBoolAdded [NPNVsupportsCocoaBool](https://developer.apple.com/documentation/webkit/npnvariable/npnvsupportscocoabool)Added [NPN_PluginThreadAsyncCall()](https://developer.apple.com/documentation/webkit/1444019-npn_pluginthreadasynccall)Added [NPN_PopUpContextMenu()](https://developer.apple.com/documentation/webkit/1443937-npn_popupcontextmenu)Added [NPN_ScheduleTimer()](https://developer.apple.com/documentation/webkit/1443741-npn_scheduletimer)Added [NPN_UnscheduleTimer()](https://developer.apple.com/documentation/webkit/1444192-npn_unscheduletimer)Added [NPPVpluginDrawingModel](https://developer.apple.com/documentation/webkit/nppvariable/nppvplugindrawingmodel)Added [NPPVpluginEventModel](https://developer.apple.com/documentation/webkit/nppvariable/nppvplugineventmodel)Added NPPVpluginTextInputFuncsAdded #def NPVERS_HAS_PLUGIN_THREAD_ASYNC_CALLAdded #def NPVERS_MACOSX_HAS_EVENT_MODELSAdded #def NP_NO_CARBONAdded #def NP_NO_QUICKDRAWModified uint16

|  | Architectures |
| --- | --- |
| Old | none? |
| New | x86_64 |

Modified uint32

|  | Architectures |
| --- | --- |
| Old | none? |
| New | x86_64 |

npfunctions.hAdded #def EXPORTED_CALLBACKAdded EXPORTED_CALLBACK() (no architecture available)Added EXPORTED_CALLBACK (no architecture available)Added [NPN_ConstructProcPtr](https://developer.apple.com/documentation/webkit/npn_constructprocptr)Added [NPN_PluginThreadAsyncCallProcPtr](https://developer.apple.com/documentation/webkit/npn_pluginthreadasynccallprocptr)Added [NPN_PopUpContextMenuProcPtr](https://developer.apple.com/documentation/webkit/npn_popupcontextmenuprocptr)Added [NPN_ScheduleTimerProcPtr](https://developer.apple.com/documentation/webkit/npn_scheduletimerprocptr)Added [NPN_UnscheduleTimerProcPtr](https://developer.apple.com/documentation/webkit/npn_unscheduletimerprocptr)npruntime.hAdded [NPN_Construct()](https://developer.apple.com/documentation/webkit/1409549-npn_construct)nptextinput.hAdded NPBrowserTextInputFuncsAdded NPN_MarkedTextAbandoned()Added NPN_MarkedTextAbandonedFuncAdded NPN_MarkedTextSelectionChanged()Added NPN_MarkedTextSelectionChangedFuncAdded NPP_AttributedSubstringFromRange()Added NPP_AttributedSubstringFromRangeFuncAdded NPP_CharacterIndexForPoint()Added NPP_CharacterIndexForPointFuncAdded NPP_DoCommandBySelector()Added NPP_DoCommandBySelectorFuncAdded NPP_FirstRectForCharacterRange()Added NPP_FirstRectForCharacterRangeFuncAdded NPP_HasMarkedText()Added NPP_HasMarkedTextFuncAdded NPP_InsertText()Added NPP_InsertTextFuncAdded NPP_MarkedRange()Added NPP_MarkedRangeFuncAdded NPP_SelectedRange()Added NPP_SelectedRangeFuncAdded NPP_SetMarkedText()Added NPP_SetMarkedTextFuncAdded NPP_UnmarkText()Added NPP_UnmarkTextFuncAdded NPP_ValidAttributesForMarkedText()Added NPP_ValidAttributesForMarkedTextFuncAdded NPPluginTextInputFuncs

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
