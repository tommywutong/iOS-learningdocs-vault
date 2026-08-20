---
title: iOS 8.0 API Diffs
apple_id: TP40014455
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS80APIDiffs/headers/System.html
archived_at: '2026-07-18T02:56:02.160991Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.0 API Diffs](iOS%207.1%20to%20iOS%208.0%20API%20Differences.md)


# System Headers Changes

## System Headers

/usr/include/MacTypes.hRemoved StrLength()Added #def StrLengthModified [#def nil](https://developer.apple.com/documentation/objectivec/nil-2gl)

|  | Header |
| --- | --- |
| From | MacTypes.h |
| To | objc/objc.h |

/usr/include/dispatch/base.hAdded #def DISPATCH_ENUM_AVAILABLE_STARTINGAdded #def DISPATCH_RETURNS_RETAINED_BLOCKAdded #def DISPATCH_UNAVAILABLE/usr/include/dispatch/block.h (Added)Added [DISPATCH_BLOCK_ASSIGN_CURRENT](https://developer.apple.com/documentation/dispatch/dispatch_block_flags_t/dispatch_block_assign_current)Added [DISPATCH_BLOCK_BARRIER](https://developer.apple.com/documentation/dispatch/dispatch_block_flags_t/dispatch_block_barrier)Added [DISPATCH_BLOCK_DETACHED](https://developer.apple.com/documentation/dispatch/dispatch_block_flags_t/dispatch_block_detached)Added [DISPATCH_BLOCK_ENFORCE_QOS_CLASS](https://developer.apple.com/documentation/dispatch/dispatch_block_flags_t/dispatch_block_enforce_qos_class)Added [DISPATCH_BLOCK_INHERIT_QOS_CLASS](https://developer.apple.com/documentation/dispatch/dispatch_block_flags_t/dispatch_block_inherit_qos_class)Added [DISPATCH_BLOCK_NO_QOS_CLASS](https://developer.apple.com/documentation/dispatch/dispatch_block_flags_t/dispatch_block_no_qos_class)Added [dispatch_block_cancel()](https://developer.apple.com/documentation/dispatch/1431058-dispatch_block_cancel)Added [dispatch_block_create()](https://developer.apple.com/documentation/dispatch/1431050-dispatch_block_create)Added [dispatch_block_create_with_qos_class()](https://developer.apple.com/documentation/dispatch/1431068-dispatch_block_create_with_qos_c)Added [dispatch_block_flags_t](https://developer.apple.com/documentation/dispatch/dispatch_block_flags_t)Added [dispatch_block_notify()](https://developer.apple.com/documentation/dispatch/1431042-dispatch_block_notify)Added [dispatch_block_perform()](https://developer.apple.com/documentation/dispatch/1431048-dispatch_block_perform)Added [dispatch_block_testcancel()](https://developer.apple.com/documentation/dispatch/1431046-dispatch_block_testcancel)Added [dispatch_block_wait()](https://developer.apple.com/documentation/dispatch/1431064-dispatch_block_wait)/usr/include/dispatch/object.hAdded #def dispatch_cancelAdded #def dispatch_notifyAdded #def dispatch_testcancelAdded #def dispatch_waitModified [dispatch_block_t](https://developer.apple.com/documentation/dispatch/dispatch_block_t)

|  | Header |
| --- | --- |
| From | dispatch/queue.h |
| To | dispatch/object.h |

/usr/include/dispatch/queue.hRemoved #def dispatch_get_main_queueAdded [dispatch_get_main_queue()](https://developer.apple.com/documentation/dispatch/1452921-dispatch_get_main_queue)Added [dispatch_qos_class_t](https://developer.apple.com/documentation/dispatch/dispatch_qos_class_t)Added [dispatch_queue_attr_make_with_qos_class()](https://developer.apple.com/documentation/dispatch/1453028-dispatch_queue_attr_make_with_qo)Added [dispatch_queue_get_qos_class()](https://developer.apple.com/documentation/dispatch/1452829-dispatch_queue_get_qos_class)Modified [dispatch_block_t](https://developer.apple.com/documentation/dispatch/dispatch_block_t)

|  | Header |
| --- | --- |
| From | dispatch/queue.h |
| To | dispatch/object.h |

Modified [dispatch_get_global_queue()](https://developer.apple.com/documentation/dispatch/1452927-dispatch_get_global_queue)

|  | Declaration |
| --- | --- |
| From | ``` dispatch_queue_t dispatch_get_global_queue (	dispatch_queue_priority_t priority,	unsigned long flags); ``` |
| To | ``` dispatch_queue_t dispatch_get_global_queue (	long identifier,	unsigned long flags); ``` |

/usr/include/dispatch/source.hModified [dispatch_source_set_cancel_handler()](https://developer.apple.com/documentation/dispatch/1385648-dispatch_source_set_cancel_handl)

|  | Declaration |
| --- | --- |
| From | ``` void dispatch_source_set_cancel_handler (	dispatch_source_t source,	dispatch_block_t cancel_handler); ``` |
| To | ``` void dispatch_source_set_cancel_handler (	dispatch_source_t source,	dispatch_block_t handler); ``` |

Modified [dispatch_source_set_cancel_handler_f()](https://developer.apple.com/documentation/dispatch/1385592-dispatch_source_set_cancel_handl)

|  | Declaration |
| --- | --- |
| From | ``` void dispatch_source_set_cancel_handler_f (	dispatch_source_t source,	dispatch_function_t cancel_handler); ``` |
| To | ``` void dispatch_source_set_cancel_handler_f (	dispatch_source_t source,	dispatch_function_t handler); ``` |

Modified [dispatch_source_set_registration_handler()](https://developer.apple.com/documentation/dispatch/1385674-dispatch_source_set_registration)

|  | Declaration |
| --- | --- |
| From | ``` void dispatch_source_set_registration_handler (	dispatch_source_t source,	dispatch_block_t registration_handler); ``` |
| To | ``` void dispatch_source_set_registration_handler (	dispatch_source_t source,	dispatch_block_t handler); ``` |

Modified [dispatch_source_set_registration_handler_f()](https://developer.apple.com/documentation/dispatch/1385662-dispatch_source_set_registration)

|  | Declaration |
| --- | --- |
| From | ``` void dispatch_source_set_registration_handler_f (	dispatch_source_t source,	dispatch_function_t registration_handler); ``` |
| To | ``` void dispatch_source_set_registration_handler_f (	dispatch_source_t source,	dispatch_function_t handler); ``` |

/usr/include/launch.h (Removed)Removed [LAUNCH_DATA_ARRAY](https://developer.apple.com/documentation/xpc/launch_data_type_t/launch_data_array)Removed [LAUNCH_DATA_BOOL](https://developer.apple.com/documentation/xpc/launch_data_type_t/launch_data_bool)Removed [LAUNCH_DATA_DICTIONARY](https://developer.apple.com/documentation/xpc/launch_data_type_t/launch_data_dictionary)Removed [LAUNCH_DATA_ERRNO](https://developer.apple.com/documentation/xpc/launch_data_type_t/launch_data_errno)Removed [LAUNCH_DATA_FD](https://developer.apple.com/documentation/xpc/launch_data_type_t/launch_data_fd)Removed [LAUNCH_DATA_INTEGER](https://developer.apple.com/documentation/xpc/launch_data_type_t/launch_data_integer)Removed [LAUNCH_DATA_MACHPORT](https://developer.apple.com/documentation/xpc/launch_data_type_t/launch_data_machport)Removed [LAUNCH_DATA_OPAQUE](https://developer.apple.com/documentation/xpc/launch_data_type_t/launch_data_opaque)Removed [LAUNCH_DATA_REAL](https://developer.apple.com/documentation/xpc/launch_data_type_t/launch_data_real)Removed [LAUNCH_DATA_STRING](https://developer.apple.com/documentation/xpc/launch_data_type_t/launch_data_string)Removed #def LAUNCH_JOBINETDCOMPATIBILITY_WAITRemoved #def LAUNCH_JOBKEY_ABANDONPROCESSGROUPRemoved #def LAUNCH_JOBKEY_BONJOURFDSRemoved #def LAUNCH_JOBKEY_CAL_DAYRemoved #def LAUNCH_JOBKEY_CAL_HOURRemoved #def LAUNCH_JOBKEY_CAL_MINUTERemoved #def LAUNCH_JOBKEY_CAL_MONTHRemoved #def LAUNCH_JOBKEY_CAL_WEEKDAYRemoved #def LAUNCH_JOBKEY_CFBUNDLEIDENTIFIERRemoved #def LAUNCH_JOBKEY_DEBUGRemoved #def LAUNCH_JOBKEY_DEFAULTSRemoved #def LAUNCH_JOBKEY_DISABLEDRemoved #def LAUNCH_JOBKEY_DISABLED_MACHINETYPERemoved #def LAUNCH_JOBKEY_DISABLED_MODELNAMERemoved #def LAUNCH_JOBKEY_ENABLEGLOBBINGRemoved #def LAUNCH_JOBKEY_ENABLETRANSACTIONSRemoved #def LAUNCH_JOBKEY_ENVIRONMENTVARIABLESRemoved #def LAUNCH_JOBKEY_EXITTIMEOUTRemoved #def LAUNCH_JOBKEY_GROUPNAMERemoved #def LAUNCH_JOBKEY_HARDRESOURCELIMITSRemoved #def LAUNCH_JOBKEY_HOPEFULLYEXITSFIRSTRemoved #def LAUNCH_JOBKEY_HOPEFULLYEXITSLASTRemoved #def LAUNCH_JOBKEY_IGNOREPROCESSGROUPATSHUTDOWNRemoved #def LAUNCH_JOBKEY_INETDCOMPATIBILITYRemoved #def LAUNCH_JOBKEY_INITGROUPSRemoved #def LAUNCH_JOBKEY_KEEPALIVERemoved #def LAUNCH_JOBKEY_KEEPALIVE_AFTERINITIALDEMANDRemoved #def LAUNCH_JOBKEY_KEEPALIVE_CRASHEDRemoved #def LAUNCH_JOBKEY_KEEPALIVE_NETWORKSTATERemoved #def LAUNCH_JOBKEY_KEEPALIVE_OTHERJOBACTIVERemoved #def LAUNCH_JOBKEY_KEEPALIVE_OTHERJOBENABLEDRemoved #def LAUNCH_JOBKEY_KEEPALIVE_PATHSTATERemoved #def LAUNCH_JOBKEY_KEEPALIVE_SUCCESSFULEXITRemoved #def LAUNCH_JOBKEY_LABELRemoved #def LAUNCH_JOBKEY_LASTEXITSTATUSRemoved #def LAUNCH_JOBKEY_LAUNCHEVENTSRemoved #def LAUNCH_JOBKEY_LAUNCHONLYONCERemoved #def LAUNCH_JOBKEY_LIMITLOADFROMHARDWARERemoved #def LAUNCH_JOBKEY_LIMITLOADFROMHOSTSRemoved #def LAUNCH_JOBKEY_LIMITLOADTOHARDWARERemoved #def LAUNCH_JOBKEY_LIMITLOADTOHOSTSRemoved #def LAUNCH_JOBKEY_LIMITLOADTOSESSIONTYPERemoved #def LAUNCH_JOBKEY_LOWPRIORITYIORemoved #def LAUNCH_JOBKEY_MACHSERVICELOOKUPPOLICIESRemoved #def LAUNCH_JOBKEY_MACHSERVICESRemoved #def LAUNCH_JOBKEY_MACH_DRAINMESSAGESONCRASHRemoved #def LAUNCH_JOBKEY_MACH_HIDEUNTILCHECKINRemoved #def LAUNCH_JOBKEY_MACH_PINGEVENTUPDATESRemoved #def LAUNCH_JOBKEY_MACH_RESETATCLOSERemoved #def LAUNCH_JOBKEY_NICERemoved #def LAUNCH_JOBKEY_ONDEMANDRemoved #def LAUNCH_JOBKEY_PIDRemoved #def LAUNCH_JOBKEY_POLICIESRemoved #def LAUNCH_JOBKEY_PROCESSTYPERemoved #def LAUNCH_JOBKEY_PROGRAMRemoved #def LAUNCH_JOBKEY_PROGRAMARGUMENTSRemoved #def LAUNCH_JOBKEY_QUEUEDIRECTORIESRemoved #def LAUNCH_JOBKEY_RESOURCELIMIT_CORERemoved #def LAUNCH_JOBKEY_RESOURCELIMIT_CPURemoved #def LAUNCH_JOBKEY_RESOURCELIMIT_DATARemoved #def LAUNCH_JOBKEY_RESOURCELIMIT_FSIZERemoved #def LAUNCH_JOBKEY_RESOURCELIMIT_MEMLOCKRemoved #def LAUNCH_JOBKEY_RESOURCELIMIT_NOFILERemoved #def LAUNCH_JOBKEY_RESOURCELIMIT_NPROCRemoved #def LAUNCH_JOBKEY_RESOURCELIMIT_RSSRemoved #def LAUNCH_JOBKEY_RESOURCELIMIT_STACKRemoved #def LAUNCH_JOBKEY_ROOTDIRECTORYRemoved #def LAUNCH_JOBKEY_RUNATLOADRemoved #def LAUNCH_JOBKEY_SESSIONCREATERemoved #def LAUNCH_JOBKEY_SOCKETSRemoved #def LAUNCH_JOBKEY_SOFTRESOURCELIMITSRemoved #def LAUNCH_JOBKEY_STANDARDERRORPATHRemoved #def LAUNCH_JOBKEY_STANDARDINPATHRemoved #def LAUNCH_JOBKEY_STANDARDOUTPATHRemoved #def LAUNCH_JOBKEY_STARTCALENDARINTERVALRemoved #def LAUNCH_JOBKEY_STARTINTERVALRemoved #def LAUNCH_JOBKEY_STARTONMOUNTRemoved #def LAUNCH_JOBKEY_THROTTLEINTERVALRemoved #def LAUNCH_JOBKEY_TIMEOUTRemoved #def LAUNCH_JOBKEY_UMASKRemoved #def LAUNCH_JOBKEY_USERENVIRONMENTVARIABLESRemoved #def LAUNCH_JOBKEY_USERNAMERemoved #def LAUNCH_JOBKEY_WAITFORDEBUGGERRemoved #def LAUNCH_JOBKEY_WATCHPATHSRemoved #def LAUNCH_JOBKEY_WORKINGDIRECTORYRemoved #def LAUNCH_JOBPOLICY_DENYCREATINGOTHERJOBSRemoved #def LAUNCH_JOBSOCKETKEY_BONJOURRemoved #def LAUNCH_JOBSOCKETKEY_FAMILYRemoved #def LAUNCH_JOBSOCKETKEY_MULTICASTGROUPRemoved #def LAUNCH_JOBSOCKETKEY_NODENAMERemoved #def LAUNCH_JOBSOCKETKEY_PASSIVERemoved #def LAUNCH_JOBSOCKETKEY_PATHMODERemoved #def LAUNCH_JOBSOCKETKEY_PATHNAMERemoved #def LAUNCH_JOBSOCKETKEY_PROTOCOLRemoved #def LAUNCH_JOBSOCKETKEY_SECUREWITHKEYRemoved #def LAUNCH_JOBSOCKETKEY_SERVICENAMERemoved #def LAUNCH_JOBSOCKETKEY_TYPERemoved #def LAUNCH_KEY_CHECKINRemoved #def LAUNCH_KEY_GETJOBRemoved #def LAUNCH_KEY_GETJOBSRemoved #def LAUNCH_KEY_PROCESSTYPE_ADAPTIVERemoved #def LAUNCH_KEY_PROCESSTYPE_APPRemoved #def LAUNCH_KEY_PROCESSTYPE_BACKGROUNDRemoved #def LAUNCH_KEY_PROCESSTYPE_INTERACTIVERemoved #def LAUNCH_KEY_PROCESSTYPE_STANDARDRemoved #def LAUNCH_KEY_REMOVEJOBRemoved #def LAUNCH_KEY_STARTJOBRemoved #def LAUNCH_KEY_STOPJOBRemoved #def LAUNCH_KEY_SUBMITJOBRemoved [launch_data_alloc()](https://developer.apple.com/documentation/xpc/1505398-launch_data_alloc)Removed [launch_data_array_get_count()](https://developer.apple.com/documentation/xpc/1505515-launch_data_array_get_count)Removed [launch_data_array_get_index()](https://developer.apple.com/documentation/xpc/1505935-launch_data_array_get_index)Removed [launch_data_array_set_index()](https://developer.apple.com/documentation/xpc/1505624-launch_data_array_set_index)Removed [launch_data_copy()](https://developer.apple.com/documentation/xpc/1505864-launch_data_copy)Removed [launch_data_dict_get_count()](https://developer.apple.com/documentation/xpc/1505450-launch_data_dict_get_count)Removed [launch_data_dict_insert()](https://developer.apple.com/documentation/xpc/1505566-launch_data_dict_insert)Removed [launch_data_dict_iterate()](https://developer.apple.com/documentation/xpc/1505787-launch_data_dict_iterate)Removed [launch_data_dict_lookup()](https://developer.apple.com/documentation/xpc/1505396-launch_data_dict_lookup)Removed [launch_data_dict_remove()](https://developer.apple.com/documentation/xpc/1505490-launch_data_dict_remove)Removed [launch_data_free()](https://developer.apple.com/documentation/xpc/1505609-launch_data_free)Removed [launch_data_get_bool()](https://developer.apple.com/documentation/xpc/1505971-launch_data_get_bool)Removed [launch_data_get_errno()](https://developer.apple.com/documentation/xpc/1505553-launch_data_get_errno)Removed [launch_data_get_fd()](https://developer.apple.com/documentation/xpc/1505810-launch_data_get_fd)Removed [launch_data_get_integer()](https://developer.apple.com/documentation/xpc/1505651-launch_data_get_integer)Removed [launch_data_get_machport()](https://developer.apple.com/documentation/xpc/1505500-launch_data_get_machport)Removed [launch_data_get_opaque()](https://developer.apple.com/documentation/xpc/1505503-launch_data_get_opaque)Removed [launch_data_get_opaque_size()](https://developer.apple.com/documentation/xpc/1505665-launch_data_get_opaque_size)Removed [launch_data_get_real()](https://developer.apple.com/documentation/xpc/1505841-launch_data_get_real)Removed [launch_data_get_string()](https://developer.apple.com/documentation/xpc/1505866-launch_data_get_string)Removed [launch_data_get_type()](https://developer.apple.com/documentation/xpc/1505680-launch_data_get_type)Removed [launch_data_new_bool()](https://developer.apple.com/documentation/xpc/1505947-launch_data_new_bool)Removed [launch_data_new_fd()](https://developer.apple.com/documentation/xpc/1505647-launch_data_new_fd)Removed [launch_data_new_integer()](https://developer.apple.com/documentation/xpc/1505444-launch_data_new_integer)Removed [launch_data_new_machport()](https://developer.apple.com/documentation/xpc/1505641-launch_data_new_machport)Removed [launch_data_new_opaque()](https://developer.apple.com/documentation/xpc/1505806-launch_data_new_opaque)Removed [launch_data_new_real()](https://developer.apple.com/documentation/xpc/1505926-launch_data_new_real)Removed [launch_data_new_string()](https://developer.apple.com/documentation/xpc/1505574-launch_data_new_string)Removed [launch_data_set_bool()](https://developer.apple.com/documentation/xpc/1505509-launch_data_set_bool)Removed [launch_data_set_fd()](https://developer.apple.com/documentation/xpc/1505629-launch_data_set_fd)Removed [launch_data_set_integer()](https://developer.apple.com/documentation/xpc/1505961-launch_data_set_integer)Removed [launch_data_set_machport()](https://developer.apple.com/documentation/xpc/1505455-launch_data_set_machport)Removed [launch_data_set_opaque()](https://developer.apple.com/documentation/xpc/1505941-launch_data_set_opaque)Removed [launch_data_set_real()](https://developer.apple.com/documentation/xpc/1505361-launch_data_set_real)Removed [launch_data_set_string()](https://developer.apple.com/documentation/xpc/1505613-launch_data_set_string)Removed [launch_data_t](https://developer.apple.com/documentation/xpc/launch_data_t)Removed [launch_data_type_t](https://developer.apple.com/documentation/xpc/launch_data_type_t)Removed [launch_get_fd()](https://developer.apple.com/documentation/xpc/1505462-launch_get_fd)Removed [launch_msg()](https://developer.apple.com/documentation/xpc/1505402-launch_msg)/usr/include/notify.hAdded #def NOTIFY_TOKEN_INVALIDAdded [notify_is_valid_token()](https://developer.apple.com/documentation/darwinnotify/1433468-notify_is_valid_token)/usr/include/objc/NSObject.hRemoved [-[NSObject debugDescription]](https://developer.apple.com/documentation/objectivec/1418956-nsobject/1418703-debugdescription)Removed [-[NSObject description]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/description)Removed [-[NSObject hash]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/hash)Removed [-[NSObject superclass]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/superclass)Added [+[NSObject debugDescription]](https://developer.apple.com/documentation/objectivec/nsobject/1418711-debugdescription)Added [NSObject.debugDescription](https://developer.apple.com/documentation/objectivec/1418956-nsobject/1418703-debugdescription)Added [NSObject.description](https://developer.apple.com/documentation/objectivec/nsobjectprotocol/1418746-description)Added [+[NSObject hash]](https://developer.apple.com/documentation/objectivec/nsobject/1418561-hash)Added [NSObject.hash](https://developer.apple.com/documentation/objectivec/1418956-nsobject/1418859-hash)Added [NSObject.superclass](https://developer.apple.com/documentation/objectivec/1418956-nsobject/1418793-superclass)Modified [+[NSObject alloc]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/alloc)

|  | Declaration |
| --- | --- |
| From | ``` + (id)alloc ``` |
| To | ``` + (instancetype)alloc ``` |

Modified [+[NSObject allocWithZone:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/allocWithZone:)

|  | Declaration |
| --- | --- |
| From | ``` + (id)allocWithZone:(struct _NSZone *)zone ``` |
| To | ``` + (instancetype)allocWithZone:(struct _NSZone *)zone ``` |

Modified [-[NSObject autorelease]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/autorelease)

|  | Declaration |
| --- | --- |
| From | ``` - (id)autorelease ``` |
| To | ``` - (instancetype)autorelease ``` |

Modified [-[NSObject init]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)init ``` |
| To | ``` - (instancetype)init ``` |

Modified [+[NSObject new]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/new)

|  | Declaration |
| --- | --- |
| From | ``` + (id)new ``` |
| To | ``` + (instancetype)new ``` |

Modified [-[NSObject retain]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/retain)

|  | Declaration |
| --- | --- |
| From | ``` - (id)retain ``` |
| To | ``` - (instancetype)retain ``` |

Modified [-[NSObject self]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/self)

|  | Declaration |
| --- | --- |
| From | ``` - (id)self ``` |
| To | ``` - (instancetype)self ``` |

/usr/include/objc/objc.hModified [#def nil](https://developer.apple.com/documentation/objectivec/nil-2gl)

|  | Header |
| --- | --- |
| From | MacTypes.h |
| To | objc/objc.h |

/usr/include/objc/runtime.hAdded [object_isClass()](https://developer.apple.com/documentation/objectivec/1418659-object_isclass)

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
