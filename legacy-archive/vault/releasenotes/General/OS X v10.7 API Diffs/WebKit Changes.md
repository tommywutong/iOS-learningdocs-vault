---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/WebKit.html
archived_at: '2026-07-18T02:54:40.753668Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# WebKit Changes

## WebKit

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

DOMBlob.hAdded [DOMBlob](https://developer.apple.com/documentation/webkit/domblob)Added [DOMBlob.size](https://developer.apple.com/documentation/webkit/domblob/1528099-size)DOMCSSRule.hRemoved DOM_VARIABLES_RULEDOMDocument.hAdded -[DOMDocument AVAILABLE_IN_WEBKIT_VERSION_4_0] (no architecture available)Added [-[DOMDocument webkitCancelFullScreen]](https://developer.apple.com/documentation/webkit/domdocument/1494852-webkitcancelfullscreen)DOMElement.hAdded [-[DOMElement webkitRequestFullScreen:]](https://developer.apple.com/documentation/webkit/domelement/1476160-webkitrequestfullscreen)Added [DOM_ALLOW_KEYBOARD_INPUT](https://developer.apple.com/documentation/webkit/1476191-dom_keyboard_input_enumeration_l/dom_allow_keyboard_input)DOMFile.hAdded [DOMFile.name](https://developer.apple.com/documentation/webkit/domfile/1392551-name)Modified [DOMFile](https://developer.apple.com/documentation/webkit/domfile)

|  | Superclass |
| --- | --- |
| From | DOMObject |
| To | DOMBlob |

DOMProgressEvent.hModified [DOMProgressEvent.total](https://developer.apple.com/documentation/webkit/domprogressevent/1515420-total)

|  | Declaration |
| --- | --- |
| From | @property(readonly) unsigned total |
| To | @property(readonly) unsigned long long total |

Modified -[DOMProgressEvent initProgressEvent:canBubbleArg:cancelableArg:lengthComputableArg:loadedArg:totalArg:]

|  | Declaration |
| --- | --- |
| From | - (void)initProgressEvent:(NSString \*)typeArg canBubbleArg:(BOOL)canBubbleArg cancelableArg:(BOOL)cancelableArg lengthComputableArg:(BOOL)lengthComputableArg loadedArg:(unsigned)loadedArg totalArg:(unsigned)totalArg |
| To | - (void)initProgressEvent:(NSString \*)typeArg canBubbleArg:(BOOL)canBubbleArg cancelableArg:(BOOL)cancelableArg lengthComputableArg:(BOOL)lengthComputableArg loadedArg:(unsigned long long)loadedArg totalArg:(unsigned long long)totalArg |

Modified [DOMProgressEvent.loaded](https://developer.apple.com/documentation/webkit/domprogressevent/1515419-loaded)

|  | Declaration |
| --- | --- |
| From | @property(readonly) unsigned loaded |
| To | @property(readonly) unsigned long long loaded |

npapi.hRemoved NPPVpluginPrivateModeBoolRemoved #def adjustCursorEventRemoved #def getFocusEventRemoved int16Removed int32Removed #def loseFocusEventRemoved uint16 (no architecture available)Removed uint32 (no architecture available)Added NPEventTypeAdded NPEventType_AdjustCursorEventAdded NPEventType_ClippingChangedEventAdded NPEventType_GetFocusEventAdded NPEventType_LoseFocusEventAdded NPEventType_MenuCommandEventAdded NPEventType_ScrollingBeginsEventAdded NPEventType_ScrollingEndsEventAdded [NPFocusDirection](https://developer.apple.com/documentation/webkit/npfocusdirection)Added [NPFocusNext](https://developer.apple.com/documentation/webkit/npfocusdirection/npfocusnext)Added [NPFocusPrevious](https://developer.apple.com/documentation/webkit/npfocusdirection/npfocusprevious)Added NPImageExposeAdded [NPNToolkitType](https://developer.apple.com/documentation/webkit/npntoolkittype)Added [NPNVGtk12](https://developer.apple.com/documentation/webkit/npntoolkittype/npnvgtk12)Added [NPNVGtk2](https://developer.apple.com/documentation/webkit/npntoolkittype/npnvgtk2)Added NPNVSupportsWindowlessLocal (no architecture available)Added [NPPVpluginNativeAccessibleAtkPlugId](https://developer.apple.com/documentation/webkit/nppvariable/nppvpluginnativeaccessibleatkplugid)Added NPPVpluginWindowlessLocalBool (no architecture available)Added [NPP_ClearSiteData()](https://developer.apple.com/documentation/webkit/1444180-npp_clearsitedata)Added [NPP_GetSitesWithData()](https://developer.apple.com/documentation/webkit/1444006-npp_getsiteswithdata)Added [NPP_GotFocus()](https://developer.apple.com/documentation/webkit/1443779-npp_gotfocus)Added [NPP_LostFocus()](https://developer.apple.com/documentation/webkit/1443985-npp_lostfocus)Added [NPP_URLRedirectNotify()](https://developer.apple.com/documentation/webkit/1444065-npp_urlredirectnotify)Added [NPSize](https://developer.apple.com/documentation/webkit/npsize)Added #def NPVERS_HAS_ADVANCED_KEY_HANDLINGAdded #def NPVERS_HAS_CLEAR_SITE_DATAAdded #def NPVERS_HAS_URL_REDIRECT_HANDLINGAdded #def NP_CLEAR_ALLAdded #def NP_CLEAR_CACHEAdded #def NP_INFO_CompanyNameAdded #def NP_INFO_FileDescriptionAdded #def NP_INFO_FileExtentsAdded #def NP_INFO_FileOpenNameAdded #def NP_INFO_FileVersionAdded #def NP_INFO_InternalNameAdded #def NP_INFO_LegalCopyrightAdded #def NP_INFO_MIMETypeAdded #def NP_INFO_OriginalFilenameAdded #def NP_INFO_ProductNameAdded #def NP_INFO_ProductVersionAdded #def kNPEventHandledAdded #def kNPEventNotHandledAdded #def kNPEventStartIMEModified [NPP_WriteReady()](https://developer.apple.com/documentation/webkit/1443954-npp_writeready)

|  | Declaration |
| --- | --- |
| From | int32 NPP_WriteReady ( NPP instance, NPStream \*stream); |
| To | int32_t NPP_WriteReady ( NPP instance, NPStream \*stream); |

Modified [NPN_ScheduleTimer()](https://developer.apple.com/documentation/webkit/1443741-npn_scheduletimer)

|  | Declaration |
| --- | --- |
| From | uint32 NPN_ScheduleTimer ( NPP instance, uint32 interval, NPBool repeat, void (\*timerFunc)(NPP npp, uint32 timerID)); |
| To | uint32_t NPN_ScheduleTimer ( NPP instance, uint32_t interval, NPBool repeat, void (\*timerFunc)(NPP npp, uint32_t timerID)); |

Modified [NPN_PostURL()](https://developer.apple.com/documentation/webkit/1443998-npn_posturl)

|  | Declaration |
| --- | --- |
| From | NPError NPN_PostURL ( NPP instance, const char \*url, const char \*target, uint32 len, const char \*buf, NPBool file); |
| To | NPError NPN_PostURL ( NPP instance, const char \*url, const char \*target, uint32_t len, const char \*buf, NPBool file); |

Modified [NPP_NewStream()](https://developer.apple.com/documentation/webkit/1444052-npp_newstream)

|  | Declaration |
| --- | --- |
| From | NPError NPP_NewStream ( NPP instance, NPMIMEType type, NPStream \*stream, NPBool seekable, uint16 \*stype); |
| To | NPError NPP_NewStream ( NPP instance, NPMIMEType type, NPStream \*stream, NPBool seekable, uint16_t \*stype); |

Modified [NPP_New()](https://developer.apple.com/documentation/webkit/1444049-npp_new)

|  | Declaration |
| --- | --- |
| From | NPError NPP_New ( NPMIMEType pluginType, NPP instance, uint16 mode, int16 argc, char \*argn[], char \*argv[], NPSavedData \*saved); |
| To | NPError NPP_New ( NPMIMEType pluginType, NPP instance, uint16_t mode, int16_t argc, char \*argn[], char \*argv[], NPSavedData \*saved); |

Modified [NPP_HandleEvent()](https://developer.apple.com/documentation/webkit/1444082-npp_handleevent)

|  | Declaration |
| --- | --- |
| From | int16 NPP_HandleEvent ( NPP instance, void \*event); |
| To | int16_t NPP_HandleEvent ( NPP instance, void \*event); |

Modified [NPN_UnscheduleTimer()](https://developer.apple.com/documentation/webkit/1444192-npn_unscheduletimer)

|  | Declaration |
| --- | --- |
| From | void NPN_UnscheduleTimer ( NPP instance, uint32 timerID); |
| To | void NPN_UnscheduleTimer ( NPP instance, uint32_t timerID); |

Modified [NPEvent](https://developer.apple.com/documentation/webkit/npevent)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | 32-only | i386,ppc |
| To | Both | i386,x86_64 |

Modified [NPN_MemFlush()](https://developer.apple.com/documentation/webkit/1444042-npn_memflush)

|  | Declaration |
| --- | --- |
| From | uint32 NPN_MemFlush ( uint32 size); |
| To | uint32_t NPN_MemFlush ( uint32_t size); |

Modified [NPN_MemAlloc()](https://developer.apple.com/documentation/webkit/1443866-npn_memalloc)

|  | Declaration |
| --- | --- |
| From | void \* NPN_MemAlloc ( uint32 size); |
| To | void \* NPN_MemAlloc ( uint32_t size); |

Modified [NPN_GetValueForURL()](https://developer.apple.com/documentation/webkit/1443879-npn_getvalueforurl)

|  | Declaration |
| --- | --- |
| From | NPError NPN_GetValueForURL ( NPP instance, NPNURLVariable variable, const char \*url, char \*\*value, uint32 \*len); |
| To | NPError NPN_GetValueForURL ( NPP instance, NPNURLVariable variable, const char \*url, char \*\*value, uint32_t \*len); |

Modified [NPN_Write()](https://developer.apple.com/documentation/webkit/1443870-npn_write)

|  | Declaration |
| --- | --- |
| From | int32 NPN_Write ( NPP instance, NPStream \*stream, int32 len, void \*buffer); |
| To | int32_t NPN_Write ( NPP instance, NPStream \*stream, int32_t len, void \*buffer); |

Modified [NPP_Write()](https://developer.apple.com/documentation/webkit/1443809-npp_write)

|  | Declaration |
| --- | --- |
| From | int32 NPP_Write ( NPP instance, NPStream \*stream, int32 offset, int32 len, void \*buffer); |
| To | int32_t NPP_Write ( NPP instance, NPStream \*stream, int32_t offset, int32_t len, void \*buffer); |

Modified [NPN_PostURLNotify()](https://developer.apple.com/documentation/webkit/1443658-npn_posturlnotify)

|  | Declaration |
| --- | --- |
| From | NPError NPN_PostURLNotify ( NPP instance, const char \*url, const char \*target, uint32 len, const char \*buf, NPBool file, void \*notifyData); |
| To | NPError NPN_PostURLNotify ( NPP instance, const char \*url, const char \*target, uint32_t len, const char \*buf, NPBool file, void \*notifyData); |

Modified [NPN_SetValueForURL()](https://developer.apple.com/documentation/webkit/1444026-npn_setvalueforurl)

|  | Declaration |
| --- | --- |
| From | NPError NPN_SetValueForURL ( NPP instance, NPNURLVariable variable, const char \*url, const char \*value, uint32 len); |
| To | NPError NPN_SetValueForURL ( NPP instance, NPNURLVariable variable, const char \*url, const char \*value, uint32_t len); |

Modified [NPN_GetAuthenticationInfo()](https://developer.apple.com/documentation/webkit/1443864-npn_getauthenticationinfo)

|  | Declaration |
| --- | --- |
| From | NPError NPN_GetAuthenticationInfo ( NPP instance, const char \*protocol, const char \*host, int32 port, const char \*scheme, const char \*realm, char \*\*username, uint32 \*ulen, char \*\*password, uint32 \*plen); |
| To | NPError NPN_GetAuthenticationInfo ( NPP instance, const char \*protocol, const char \*host, int32_t port, const char \*scheme, const char \*realm, char \*\*username, uint32_t \*ulen, char \*\*password, uint32_t \*plen); |

npfunctions.hAdded [NPP_ClearSiteDataPtr](https://developer.apple.com/documentation/webkit/npp_clearsitedataptr)Added [NPP_GetSitesWithDataPtr](https://developer.apple.com/documentation/webkit/npp_getsiteswithdataptr)Added [NPP_GotFocusPtr](https://developer.apple.com/documentation/webkit/npp_gotfocusptr)Added [NPP_LostFocusPtr](https://developer.apple.com/documentation/webkit/npp_lostfocusptr)Added [NPP_URLRedirectNotifyPtr](https://developer.apple.com/documentation/webkit/npp_urlredirectnotifyptr)npruntime.hModified [NPN_ReleaseObject()](https://developer.apple.com/documentation/webkit/1409505-npn_releaseobject)

|  | Declaration |
| --- | --- |
| From | void NPN_ReleaseObject ( NPObject \*obj); |
| To | void NPN_ReleaseObject ( NPObject \*npobj); |

Modified [NPN_SetException()](https://developer.apple.com/documentation/webkit/1409451-npn_setexception)

|  | Declaration |
| --- | --- |
| From | void NPN_SetException ( NPObject \*obj, const NPUTF8 \*message); |
| To | void NPN_SetException ( NPObject \*npobj, const NPUTF8 \*message); |

Modified [NPN_RetainObject()](https://developer.apple.com/documentation/webkit/1409453-npn_retainobject)

|  | Declaration |
| --- | --- |
| From | NPObject \* NPN_RetainObject ( NPObject \*obj); |
| To | NPObject \* NPN_RetainObject ( NPObject \*npobj); |

nptypes.hAdded bool (no architecture available)Added #def boolAdded #def falseAdded [int16_t](https://developer.apple.com/documentation/kernel/int16_t) (no architecture available)Added [int32_t](https://developer.apple.com/documentation/kernel/int32_t) (no architecture available)Added [int64_t](https://developer.apple.com/documentation/kernel/int64_t) (no architecture available)Added #def trueAdded [uint16_t](https://developer.apple.com/documentation/kernel/uint16_t) (no architecture available)Added [uint32_t](https://developer.apple.com/documentation/kernel/uint32_t) (no architecture available)Added [uint64_t](https://developer.apple.com/documentation/kernel/uint64_t) (no architecture available)

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
