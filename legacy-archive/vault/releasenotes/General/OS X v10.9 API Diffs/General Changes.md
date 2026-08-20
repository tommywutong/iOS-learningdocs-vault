---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/General.html
archived_at: '2026-07-18T02:54:13.690117Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# General Changes

## General Headers

/usr/include/MacTypes.hModified [kVariableLengthArray](https://developer.apple.com/documentation/kernel/1645414-anonymous/kvariablelengtharray)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

/usr/include/dispatch/base.hAdded #def DISPATCH_ENUM/usr/include/dispatch/data.hAdded #def DISPATCH_DATA_DESTRUCTOR_MUNMAPAdded #def DISPATCH_DATA_DESTRUCTOR_TYPE_DECL/usr/include/dispatch/introspection.hAdded [dispatch_introspection_hook_queue_callout_begin()](https://developer.apple.com/documentation/dispatch/1452899-dispatch_introspection_hook_queu)Added [dispatch_introspection_hook_queue_callout_end()](https://developer.apple.com/documentation/dispatch/1453081-dispatch_introspection_hook_queu)Added [dispatch_introspection_hook_queue_create()](https://developer.apple.com/documentation/dispatch/1452858-dispatch_introspection_hook_queu)Added [dispatch_introspection_hook_queue_destroy()](https://developer.apple.com/documentation/dispatch/1452888-dispatch_introspection_hook_queu)Added [dispatch_introspection_hook_queue_item_dequeue()](https://developer.apple.com/documentation/dispatch/1453065-dispatch_introspection_hook_queu)Added [dispatch_introspection_hook_queue_item_enqueue()](https://developer.apple.com/documentation/dispatch/1452892-dispatch_introspection_hook_queu)/usr/include/dispatch/object.hModified [dispatch_debug()](https://developer.apple.com/documentation/dispatch/1496326-dispatch_debug)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [dispatch_debugv()](https://developer.apple.com/documentation/dispatch/1496308-dispatch_debugv)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

/usr/include/dispatch/queue.hAdded [#def DISPATCH_CURRENT_QUEUE_LABEL](https://developer.apple.com/documentation/dispatch/dispatch_current_queue_label)Modified [dispatch_get_current_queue()](https://developer.apple.com/documentation/dispatch/1493248-dispatch_get_current_queue)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

/usr/include/dispatch/source.hAdded [#def DISPATCH_MEMORYPRESSURE_CRITICAL](https://developer.apple.com/documentation/dispatch/dispatch_memorypressure_critical)Added [#def DISPATCH_MEMORYPRESSURE_NORMAL](https://developer.apple.com/documentation/dispatch/dispatch_memorypressure_normal)Added [#def DISPATCH_MEMORYPRESSURE_WARN](https://developer.apple.com/documentation/dispatch/dispatch_memorypressure_warn)Added #def DISPATCH_SOURCE_TYPE_DECLAdded [#def DISPATCH_SOURCE_TYPE_MEMORYPRESSURE](https://developer.apple.com/documentation/dispatch/dispatch_source_type_memorypressure)Added [#def DISPATCH_TIMER_STRICT](https://developer.apple.com/documentation/dispatch/dispatch_timer_strict)Added [dispatch_source_memorypressure_flags_t](https://developer.apple.com/documentation/dispatch/dispatch_source_memorypressure_flags_t)Added [dispatch_source_timer_flags_t](https://developer.apple.com/documentation/dispatch/dispatch_source_timer_flags_t)/usr/include/hfs/hfs_unistr.hAdded [ConstHFSUniStr255Param](https://developer.apple.com/documentation/kernel/consthfsunistr255param)Added [HFSUniStr255](https://developer.apple.com/documentation/kernel/hfsunistr255)/usr/include/launch.hAdded #def LAUNCH_JOBKEY_CFBUNDLEIDENTIFIERAdded #def LAUNCH_JOBKEY_DEFAULTSAdded #def LAUNCH_JOBKEY_PROCESSTYPEAdded #def LAUNCH_KEY_PROCESSTYPE_ADAPTIVEAdded #def LAUNCH_KEY_PROCESSTYPE_APPAdded #def LAUNCH_KEY_PROCESSTYPE_BACKGROUNDAdded #def LAUNCH_KEY_PROCESSTYPE_INTERACTIVEAdded #def LAUNCH_KEY_PROCESSTYPE_STANDARD/usr/include/notify_keys.hAdded #def kNotifyVFSUpdate/usr/include/objc/NSObjCRuntime.hModified #def NSINTEGER_DEFINED

|  | Header |
| --- | --- |
| From | Foundation/NSObjCRuntime.h |
| To | objc/NSObjCRuntime.h |

Modified [NSInteger](https://developer.apple.com/documentation/objectivec/nsinteger)

|  | Header |
| --- | --- |
| From | Foundation/NSObjCRuntime.h |
| To | objc/NSObjCRuntime.h |

Modified [#def NSIntegerMax](https://developer.apple.com/documentation/objectivec/nsintegermax)

|  | Header |
| --- | --- |
| From | Foundation/NSObjCRuntime.h |
| To | objc/NSObjCRuntime.h |

Modified [#def NSIntegerMin](https://developer.apple.com/documentation/objectivec/nsintegermin)

|  | Header |
| --- | --- |
| From | Foundation/NSObjCRuntime.h |
| To | objc/NSObjCRuntime.h |

Modified [NSUInteger](https://developer.apple.com/documentation/objectivec/nsuinteger)

|  | Header |
| --- | --- |
| From | Foundation/NSObjCRuntime.h |
| To | objc/NSObjCRuntime.h |

Modified [#def NSUIntegerMax](https://developer.apple.com/documentation/objectivec/nsuintegermax)

|  | Header |
| --- | --- |
| From | Foundation/NSObjCRuntime.h |
| To | objc/NSObjCRuntime.h |

/usr/include/objc/NSObject.hModified [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intf/NSObject)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/cl/NSObject)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject alloc]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/alloc)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject allocWithZone:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/allocWithZone:)

|  | Header | Declaration |
| --- | --- | --- |
| From | Foundation/NSObject.h | + (id)allocWithZone:(NSZone \*)zone |
| To | objc/NSObject.h | + (id)allocWithZone:(struct _NSZone \*)zone |

Modified [-[NSObject autorelease]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/autorelease)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject class]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/class)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject class]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/class)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject conformsToProtocol:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/conformsToProtocol:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject conformsToProtocol:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/conformsToProtocol:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject copy]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/copy)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject copyWithZone:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/copyWithZone:)

|  | Header | Declaration |
| --- | --- | --- |
| From | Foundation/NSObject.h | + (id)copyWithZone:(NSZone \*)zone |
| To | objc/NSObject.h | + (id)copyWithZone:(struct _NSZone \*)zone |

Modified [-[NSObject dealloc]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/dealloc)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject debugDescription]](https://developer.apple.com/documentation/objectivec/1418956-nsobject/1418703-debugdescription)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject description]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/description)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject description]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/description)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject doesNotRecognizeSelector:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/doesNotRecognizeSelector:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject finalize]](https://developer.apple.com/documentation/objectivec/nsobject/1418513-finalize)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject forwardInvocation:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/forwardInvocation:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject forwardingTargetForSelector:]](https://developer.apple.com/documentation/objectivec/nsobject/1418855-forwardingtarget)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject hash]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/hash)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject init]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/init)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject initialize]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/initialize)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject instanceMethodForSelector:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/instanceMethodForSelector:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject instanceMethodSignatureForSelector:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/instanceMethodSignatureForSelector:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject instancesRespondToSelector:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/instancesRespondToSelector:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject isEqual:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/isEqual:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject isKindOfClass:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/isKindOfClass:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject isMemberOfClass:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/isMemberOfClass:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject isProxy]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/isProxy)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject isSubclassOfClass:]](https://developer.apple.com/documentation/objectivec/nsobject/1418669-issubclassofclass)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject load]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/load)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject methodForSelector:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/methodForSelector:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject methodSignatureForSelector:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/methodSignatureForSelector:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject mutableCopy]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/mutableCopy)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject mutableCopyWithZone:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/mutableCopyWithZone:)

|  | Header | Declaration |
| --- | --- | --- |
| From | Foundation/NSObject.h | + (id)mutableCopyWithZone:(NSZone \*)zone |
| To | objc/NSObject.h | + (id)mutableCopyWithZone:(struct _NSZone \*)zone |

Modified [+[NSObject new]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/new)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject performSelector:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/performSelector:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject performSelector:withObject:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/performSelector:withObject:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject performSelector:withObject:withObject:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/performSelector:withObject:withObject:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject release]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/release)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject resolveClassMethod:]](https://developer.apple.com/documentation/objectivec/nsobject/1418889-resolveclassmethod)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject resolveInstanceMethod:]](https://developer.apple.com/documentation/objectivec/nsobject/1418500-resolveinstancemethod)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject respondsToSelector:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/respondsToSelector:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject retain]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/retain)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject retainCount]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/retainCount)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject self]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/self)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject superclass]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/superclass)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject superclass]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/superclass)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject zone]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/zone)

|  | Header | Declaration |
| --- | --- | --- |
| From | Foundation/NSObject.h | - (NSZone \*)zone |
| To | objc/NSObject.h | - (struct _NSZone \*)zone |

/usr/include/objc/Protocol.hModified [-[Protocol conformsTo:]](https://developer.apple.com/documentation/objectivec/protocol/1444956-conformsto)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

Modified [-[Protocol name]](https://developer.apple.com/documentation/objectivec/protocol/1444960-name)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

/usr/include/objc/message.hModified [objc_msgSendv()](https://developer.apple.com/documentation/objectivec/1456718-objc_msgsendv)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

Modified [objc_msgSendv_fpret()](https://developer.apple.com/documentation/objectivec/1456714-objc_msgsendv_fpret)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

Modified [objc_msgSendv_stret()](https://developer.apple.com/documentation/objectivec/1456699-objc_msgsendv_stret)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

/usr/include/objc/objc-api.hAdded #def OBJC_ISA_AVAILABILITYAdded [#def OBJC_ROOT_CLASS](https://developer.apple.com/documentation/objectivec/objc_root_class)/usr/include/objc/objc-load.hModified [objc_loadModule()](https://developer.apple.com/documentation/objectivec/1393242-objc_loadmodule)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

Modified [objc_loadModules()](https://developer.apple.com/documentation/objectivec/1393246-objc_loadmodules)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

Modified [objc_unloadModules()](https://developer.apple.com/documentation/objectivec/1393244-objc_unloadmodules)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

/usr/include/objc/runtime.hModified [Cache](https://developer.apple.com/documentation/objectivec/cache)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

Modified [Module](https://developer.apple.com/documentation/objectivec/module)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

Modified [Symtab](https://developer.apple.com/documentation/objectivec/symtab)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

Modified [class_addMethods()](https://developer.apple.com/documentation/objectivec/1441602-class_addmethods)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

Modified [class_nextMethodList()](https://developer.apple.com/documentation/objectivec/1441592-class_nextmethodlist)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

Modified [class_poseAs()](https://developer.apple.com/documentation/objectivec/1441500-class_poseas)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

Modified [class_removeMethods()](https://developer.apple.com/documentation/objectivec/1441594-class_removemethods)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

Modified [method_getArgumentInfo()](https://developer.apple.com/documentation/objectivec/1441524-method_getargumentinfo)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

Modified [method_getSizeOfArguments()](https://developer.apple.com/documentation/objectivec/1441633-method_getsizeofarguments)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

Modified [objc_addClass()](https://developer.apple.com/documentation/objectivec/1441586-objc_addclass)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

Modified [objc_enumerationMutation()](https://developer.apple.com/documentation/objectivec/1418744-objc_enumerationmutation)

|  | Declaration |
| --- | --- |
| From | void objc_enumerationMutation ( id); |
| To | void objc_enumerationMutation ( id obj); |

Modified [objc_getClass()](https://developer.apple.com/documentation/objectivec/1418952-objc_getclass)

|  | Declaration |
| --- | --- |
| From | id objc_getClass ( const char \*name); |
| To | Class objc_getClass ( const char \*name); |

Modified [objc_getClasses()](https://developer.apple.com/documentation/objectivec/1441660-objc_getclasses)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

Modified [objc_getMetaClass()](https://developer.apple.com/documentation/objectivec/1418721-objc_getmetaclass)

|  | Declaration |
| --- | --- |
| From | id objc_getMetaClass ( const char \*name); |
| To | Class objc_getMetaClass ( const char \*name); |

Modified [objc_getOrigClass()](https://developer.apple.com/documentation/objectivec/1441475-objc_getorigclass)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

Modified [objc_getRequiredClass()](https://developer.apple.com/documentation/objectivec/1418661-objc_getrequiredclass)

|  | Declaration |
| --- | --- |
| From | id objc_getRequiredClass ( const char \*name); |
| To | Class objc_getRequiredClass ( const char \*name); |

Modified [objc_ivar_list](https://developer.apple.com/documentation/objectivec/objc_ivar_list)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

Modified [objc_lookUpClass()](https://developer.apple.com/documentation/objectivec/1418760-objc_lookupclass)

|  | Declaration |
| --- | --- |
| From | id objc_lookUpClass ( const char \*name); |
| To | Class objc_lookUpClass ( const char \*name); |

Modified [objc_method_list](https://developer.apple.com/documentation/objectivec/objc_method_list)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

Modified [objc_setClassHandler()](https://developer.apple.com/documentation/objectivec/1441676-objc_setclasshandler)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

Modified [objc_setMultithreaded()](https://developer.apple.com/documentation/objectivec/1441496-objc_setmultithreaded)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

Modified [object_realloc()](https://developer.apple.com/documentation/objectivec/1441573-object_realloc)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

Modified [object_reallocFromZone()](https://developer.apple.com/documentation/objectivec/1441685-object_reallocfromzone)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

/usr/include/xpc/activity.hAdded [XPC_ACTIVITY_ALLOW_BATTERY](https://developer.apple.com/documentation/xpc/xpc_activity_allow_battery)Added [XPC_ACTIVITY_CHECK_IN](https://developer.apple.com/documentation/xpc/xpc_activity_check_in)Added [XPC_ACTIVITY_DELAY](https://developer.apple.com/documentation/xpc/xpc_activity_delay)Added [XPC_ACTIVITY_GRACE_PERIOD](https://developer.apple.com/documentation/xpc/xpc_activity_grace_period)Added [XPC_ACTIVITY_INTERVAL](https://developer.apple.com/documentation/xpc/xpc_activity_interval)Added [XPC_ACTIVITY_INTERVAL_15_MIN](https://developer.apple.com/documentation/xpc/xpc_activity_interval_15_min)Added [XPC_ACTIVITY_INTERVAL_1_DAY](https://developer.apple.com/documentation/xpc/xpc_activity_interval_1_day)Added [XPC_ACTIVITY_INTERVAL_1_HOUR](https://developer.apple.com/documentation/xpc/xpc_activity_interval_1_hour)Added [XPC_ACTIVITY_INTERVAL_1_MIN](https://developer.apple.com/documentation/xpc/xpc_activity_interval_1_min)Added [XPC_ACTIVITY_INTERVAL_30_MIN](https://developer.apple.com/documentation/xpc/xpc_activity_interval_30_min)Added [XPC_ACTIVITY_INTERVAL_4_HOURS](https://developer.apple.com/documentation/xpc/xpc_activity_interval_4_hours)Added [XPC_ACTIVITY_INTERVAL_5_MIN](https://developer.apple.com/documentation/xpc/xpc_activity_interval_5_min)Added [XPC_ACTIVITY_INTERVAL_7_DAYS](https://developer.apple.com/documentation/xpc/xpc_activity_interval_7_days)Added [XPC_ACTIVITY_INTERVAL_8_HOURS](https://developer.apple.com/documentation/xpc/xpc_activity_interval_8_hours)Added [XPC_ACTIVITY_PRIORITY](https://developer.apple.com/documentation/xpc/xpc_activity_priority)Added [XPC_ACTIVITY_PRIORITY_MAINTENANCE](https://developer.apple.com/documentation/xpc/xpc_activity_priority_maintenance)Added [XPC_ACTIVITY_PRIORITY_UTILITY](https://developer.apple.com/documentation/xpc/xpc_activity_priority_utility)Added [XPC_ACTIVITY_REPEATING](https://developer.apple.com/documentation/xpc/xpc_activity_repeating)Added [XPC_ACTIVITY_REQUIRE_BATTERY_LEVEL](https://developer.apple.com/documentation/xpc/xpc_activity_require_battery_level)Added [XPC_ACTIVITY_REQUIRE_HDD_SPINNING](https://developer.apple.com/documentation/xpc/xpc_activity_require_hdd_spinning)Added [XPC_ACTIVITY_REQUIRE_SCREEN_SLEEP](https://developer.apple.com/documentation/xpc/xpc_activity_require_screen_sleep)Added [XPC_ACTIVITY_STATE_CHECK_IN](https://developer.apple.com/documentation/xpc/1495796-xpc_activity_state_t/xpc_activity_state_check_in)Added [XPC_ACTIVITY_STATE_CONTINUE](https://developer.apple.com/documentation/xpc/1495796-xpc_activity_state_t/xpc_activity_state_continue)Added [XPC_ACTIVITY_STATE_DEFER](https://developer.apple.com/documentation/xpc/xpc_activity_state_defer)Added [XPC_ACTIVITY_STATE_DONE](https://developer.apple.com/documentation/xpc/xpc_activity_state_done)Added [XPC_ACTIVITY_STATE_RUN](https://developer.apple.com/documentation/xpc/xpc_activity_state_run)Added [XPC_ACTIVITY_STATE_WAIT](https://developer.apple.com/documentation/xpc/1495796-xpc_activity_state_t/xpc_activity_state_wait)Added [#def XPC_TYPE_ACTIVITY](https://developer.apple.com/documentation/xpc/xpc_type_activity)Added [xpc_activity_copy_criteria()](https://developer.apple.com/documentation/xpc/1495802-xpc_activity_copy_criteria)Added [xpc_activity_get_state()](https://developer.apple.com/documentation/xpc/1495816-xpc_activity_get_state)Added [xpc_activity_handler_t](https://developer.apple.com/documentation/xpc/xpc_activity_handler_t)Added [xpc_activity_register()](https://developer.apple.com/documentation/xpc/1495824-xpc_activity_register)Added [xpc_activity_set_criteria()](https://developer.apple.com/documentation/xpc/1495813-xpc_activity_set_criteria)Added [xpc_activity_set_state()](https://developer.apple.com/documentation/xpc/1495820-xpc_activity_set_state)Added [xpc_activity_should_defer()](https://developer.apple.com/documentation/xpc/1495839-xpc_activity_should_defer)Added [xpc_activity_state_t](https://developer.apple.com/documentation/xpc/xpc_activity_state_t)Added [xpc_activity_t](https://developer.apple.com/documentation/xpc/xpc_activity_t)Added [xpc_activity_unregister()](https://developer.apple.com/documentation/xpc/1495809-xpc_activity_unregister)/usr/include/xpc/base.hAdded #def XPC_BRIDGEAdded #def XPC_BRIDGEREF_BEGINAdded #def XPC_BRIDGEREF_BEGIN_WITH_REFAdded #def XPC_BRIDGEREF_ENDAdded #def XPC_BRIDGEREF_MIDDLEAdded #def XPC_GIVES_REFERENCEAdded #def XPC_NONNULL10Added #def XPC_NONNULL11Added #def XPC_NONNULL8Added #def XPC_NONNULL9Added #def XPC_PROJECT_EXPORTAdded #def XPC_TRANSPARENT_UNIONAdded #def XPC_UNAVAILABLEAdded #def XPC_UNRETAINED

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
