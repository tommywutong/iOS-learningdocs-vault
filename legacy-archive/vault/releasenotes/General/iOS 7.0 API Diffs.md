---
title: iOS 7.0 API Diffs
apple_id: TP40013203
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS70APIDiffs/index.html
archived_at: '2026-07-18T02:55:50.336103Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)


# iOS 6.1 to iOS 7.0 API Differences

## Added frameworks:

- GameController
- JavaScriptCore
- MediaAccessibility
- MultipeerConnectivity
- SafariServices
- SpriteKit

## General Headers

/usr/include/dispatch/data.hAdded #def DISPATCH_DATA_DESTRUCTOR_MUNMAPAdded #def DISPATCH_DATA_DESTRUCTOR_TYPE_DECL/usr/include/dispatch/introspection.hAdded [dispatch_introspection_hook_queue_callout_begin()](https://developer.apple.com/documentation/dispatch/1452899-dispatch_introspection_hook_queu)Added [dispatch_introspection_hook_queue_callout_end()](https://developer.apple.com/documentation/dispatch/1453081-dispatch_introspection_hook_queu)Added [dispatch_introspection_hook_queue_create()](https://developer.apple.com/documentation/dispatch/1452858-dispatch_introspection_hook_queu)Added [dispatch_introspection_hook_queue_destroy()](https://developer.apple.com/documentation/dispatch/1452888-dispatch_introspection_hook_queu)Added [dispatch_introspection_hook_queue_item_dequeue()](https://developer.apple.com/documentation/dispatch/1453065-dispatch_introspection_hook_queu)Added [dispatch_introspection_hook_queue_item_enqueue()](https://developer.apple.com/documentation/dispatch/1452892-dispatch_introspection_hook_queu)/usr/include/dispatch/queue.hAdded [#def DISPATCH_CURRENT_QUEUE_LABEL](https://developer.apple.com/documentation/dispatch/dispatch_current_queue_label)/usr/include/dispatch/source.hAdded [#def DISPATCH_MEMORYPRESSURE_CRITICAL](https://developer.apple.com/documentation/dispatch/dispatch_memorypressure_critical)Added [#def DISPATCH_MEMORYPRESSURE_NORMAL](https://developer.apple.com/documentation/dispatch/dispatch_memorypressure_normal)Added [#def DISPATCH_MEMORYPRESSURE_WARN](https://developer.apple.com/documentation/dispatch/dispatch_memorypressure_warn)Added #def DISPATCH_SOURCE_TYPE_DECLAdded [#def DISPATCH_SOURCE_TYPE_MEMORYPRESSURE](https://developer.apple.com/documentation/dispatch/dispatch_source_type_memorypressure)Added [#def DISPATCH_TIMER_STRICT](https://developer.apple.com/documentation/dispatch/dispatch_timer_strict)Added [dispatch_source_memorypressure_flags_t](https://developer.apple.com/documentation/dispatch/dispatch_source_memorypressure_flags_t)Added [dispatch_source_timer_flags_t](https://developer.apple.com/documentation/dispatch/dispatch_source_timer_flags_t)/usr/include/launch.hAdded #def LAUNCH_JOBKEY_CFBUNDLEIDENTIFIERAdded #def LAUNCH_JOBKEY_DEFAULTSAdded #def LAUNCH_JOBKEY_PROCESSTYPEAdded #def LAUNCH_KEY_PROCESSTYPE_ADAPTIVEAdded #def LAUNCH_KEY_PROCESSTYPE_APPAdded #def LAUNCH_KEY_PROCESSTYPE_BACKGROUNDAdded #def LAUNCH_KEY_PROCESSTYPE_INTERACTIVEAdded #def LAUNCH_KEY_PROCESSTYPE_STANDARD/usr/include/notify_keys.hAdded #def kNotifyVFSUpdate/usr/include/objc/NSObjCRuntime.hModified #def NSINTEGER_DEFINED

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

Modified [+[NSObject class]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/class)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject class]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/class)

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

/usr/include/objc/objc-api.hAdded #def OBJC_ARM64_UNAVAILABLEAdded #def OBJC_ISA_AVAILABILITYAdded [#def OBJC_ROOT_CLASS](https://developer.apple.com/documentation/objectivec/objc_root_class)/usr/include/objc/runtime.hModified [class_setSuperclass()](https://developer.apple.com/documentation/objectivec/1441536-class_setsuperclass)

|  | Deprecation |
| --- | --- |
| From | iOS 4.0 |
| To | iOS 2.0 |

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

Modified [objc_getMetaClass()](https://developer.apple.com/documentation/objectivec/1418721-objc_getmetaclass)

|  | Declaration |
| --- | --- |
| From | id objc_getMetaClass ( const char \*name); |
| To | Class objc_getMetaClass ( const char \*name); |

Modified [objc_getRequiredClass()](https://developer.apple.com/documentation/objectivec/1418661-objc_getrequiredclass)

|  | Declaration |
| --- | --- |
| From | id objc_getRequiredClass ( const char \*name); |
| To | Class objc_getRequiredClass ( const char \*name); |

Modified [objc_lookUpClass()](https://developer.apple.com/documentation/objectivec/1418760-objc_lookupclass)

|  | Declaration |
| --- | --- |
| From | id objc_lookUpClass ( const char \*name); |
| To | Class objc_lookUpClass ( const char \*name); |

## Accelerate

Alpha.hAdded [vImagePremultipliedAlphaBlendWithPermute_ARGB8888()](https://developer.apple.com/documentation/accelerate/1410688-vimagepremultipliedalphablendwit)Added [vImagePremultipliedAlphaBlendWithPermute_RGBA8888()](https://developer.apple.com/documentation/accelerate/1410721-vimagepremultipliedalphablendwit)Added [vImagePremultiplyData_ARGB16Q12()](https://developer.apple.com/documentation/accelerate/1410659-vimagepremultiplydata_argb16q12)Added [vImagePremultiplyData_RGBA16Q12()](https://developer.apple.com/documentation/accelerate/1410636-vimagepremultiplydata_rgba16q12)Added [vImageUnpremultiplyData_ARGB16Q12()](https://developer.apple.com/documentation/accelerate/1410730-vimageunpremultiplydata_argb16q1)Added [vImageUnpremultiplyData_RGBA16Q12()](https://developer.apple.com/documentation/accelerate/1410683-vimageunpremultiplydata_rgba16q1)Conversion.hAdded [kvImageConvert_DitherAtkinson](https://developer.apple.com/documentation/accelerate/kvimageconvert_ditheratkinson)Added [kvImageConvert_DitherFloydSteinberg](https://developer.apple.com/documentation/accelerate/kvimageconvert_ditherfloydsteinberg)Added [kvImageConvert_DitherNone](https://developer.apple.com/documentation/accelerate/1533233-dithering_methods/kvimageconvert_dithernone)Added [kvImageConvert_DitherOrdered](https://developer.apple.com/documentation/accelerate/1533233-dithering_methods/kvimageconvert_ditherordered)Added [kvImageConvert_DitherOrderedReproducible](https://developer.apple.com/documentation/accelerate/kvimageconvert_ditherorderedreproducible)Added [kvImageConvert_OrderedGaussianBlue](https://developer.apple.com/documentation/accelerate/kvimageconvert_orderedgaussianblue)Added [kvImageConvert_OrderedNoiseShapeMask](https://developer.apple.com/documentation/accelerate/1533233-dithering_methods/kvimageconvert_orderednoiseshapemask)Added [kvImageConvert_OrderedUniformBlue](https://developer.apple.com/documentation/accelerate/1533233-dithering_methods/kvimageconvert_ordereduniformblue)Added [vImageBufferFill_ARGB16S()](https://developer.apple.com/documentation/accelerate/1533219-vimagebufferfill_argb16s)Added [vImageBufferFill_ARGB16U()](https://developer.apple.com/documentation/accelerate/1533077-vimagebufferfill_argb16u)Added [vImageByteSwap_Planar16U()](https://developer.apple.com/documentation/accelerate/1533153-vimagebyteswap_planar16u)Added [vImageConvert_16Fto16U()](https://developer.apple.com/documentation/accelerate/1533203-vimageconvert_16fto16u)Added [vImageConvert_16Q12to16U()](https://developer.apple.com/documentation/accelerate/1533226-vimageconvert_16q12to16u)Added [vImageConvert_16Q12to8()](https://developer.apple.com/documentation/accelerate/1533295-vimageconvert_16q12to8)Added [vImageConvert_16Q12toF()](https://developer.apple.com/documentation/accelerate/1533114-vimageconvert_16q12tof)Added [vImageConvert_16Uto16F()](https://developer.apple.com/documentation/accelerate/1533082-vimageconvert_16uto16f)Added [vImageConvert_16Uto16Q12()](https://developer.apple.com/documentation/accelerate/1533100-vimageconvert_16uto16q12)Added [vImageConvert_8to16Q12()](https://developer.apple.com/documentation/accelerate/1533296-vimageconvert_8to16q12)Added [vImageConvert_ARGB16UToARGB8888()](https://developer.apple.com/documentation/accelerate/1533191-vimageconvert_argb16utoargb8888)Added [vImageConvert_ARGB16UtoPlanar16U()](https://developer.apple.com/documentation/accelerate/1533248-vimageconvert_argb16utoplanar16u)Added [vImageConvert_ARGB16UtoRGB16U()](https://developer.apple.com/documentation/accelerate/1533087-vimageconvert_argb16utorgb16u)Added [vImageConvert_ARGB8888ToARGB16U()](https://developer.apple.com/documentation/accelerate/1533031-vimageconvert_argb8888toargb16u)Added [vImageConvert_ARGB8888ToRGB16U()](https://developer.apple.com/documentation/accelerate/1533004-vimageconvert_argb8888torgb16u)Added [vImageConvert_ARGB8888toPlanar16Q12()](https://developer.apple.com/documentation/accelerate/1533126-vimageconvert_argb8888toplanar16)Added [vImageConvert_ARGB8888toPlanarF()](https://developer.apple.com/documentation/accelerate/1533036-vimageconvert_argb8888toplanarf)Added [vImageConvert_ARGBFFFFtoPlanar8()](https://developer.apple.com/documentation/accelerate/1533059-vimageconvert_argbfffftoplanar8)Added [vImageConvert_ARGBFFFFtoRGBFFF()](https://developer.apple.com/documentation/accelerate/1533142-vimageconvert_argbfffftorgbfff)Added [vImageConvert_BGRA16UtoRGB16U()](https://developer.apple.com/documentation/accelerate/1533183-vimageconvert_bgra16utorgb16u)Added #def vImageConvert_BGRA8888toPlanar8Added [vImageConvert_BGRA8888toRGB565()](https://developer.apple.com/documentation/accelerate/1533285-vimageconvert_bgra8888torgb565)Added #def vImageConvert_BGRAFFFFtoPlanarFAdded [vImageConvert_BGRAFFFFtoRGBFFF()](https://developer.apple.com/documentation/accelerate/1533214-vimageconvert_bgrafffftorgbfff)Added #def vImageConvert_BGRFFFtoBGRAFFFFAdded #def vImageConvert_BGRFFFtoRGBAFFFFAdded [vImageConvert_BGRX8888ToPlanar8()](https://developer.apple.com/documentation/accelerate/1533037-vimageconvert_bgrx8888toplanar8)Added [vImageConvert_BGRXFFFFToPlanarF()](https://developer.apple.com/documentation/accelerate/1533129-vimageconvert_bgrxfffftoplanarf)Added [vImageConvert_Fto16Q12()](https://developer.apple.com/documentation/accelerate/1533200-vimageconvert_fto16q12)Added [vImageConvert_Indexed1toPlanar8()](https://developer.apple.com/documentation/accelerate/1533038-vimageconvert_indexed1toplanar8)Added [vImageConvert_Indexed2toPlanar8()](https://developer.apple.com/documentation/accelerate/1533271-vimageconvert_indexed2toplanar8)Added [vImageConvert_Indexed4toPlanar8()](https://developer.apple.com/documentation/accelerate/1533028-vimageconvert_indexed4toplanar8)Added [vImageConvert_Planar16FtoPlanar8()](https://developer.apple.com/documentation/accelerate/1533139-vimageconvert_planar16ftoplanar8)Added [vImageConvert_Planar16Q12toARGB8888()](https://developer.apple.com/documentation/accelerate/1533180-vimageconvert_planar16q12toargb8)Added [vImageConvert_Planar16Q12toRGB888()](https://developer.apple.com/documentation/accelerate/1533184-vimageconvert_planar16q12torgb88)Added [vImageConvert_Planar16UtoARGB16U()](https://developer.apple.com/documentation/accelerate/1533093-vimageconvert_planar16utoargb16u)Added [vImageConvert_Planar16UtoRGB16U()](https://developer.apple.com/documentation/accelerate/1533025-vimageconvert_planar16utorgb16u)Added [vImageConvert_Planar1toPlanar8()](https://developer.apple.com/documentation/accelerate/1533136-vimageconvert_planar1toplanar8)Added [vImageConvert_Planar2toPlanar8()](https://developer.apple.com/documentation/accelerate/1533035-vimageconvert_planar2toplanar8)Added [vImageConvert_Planar4toPlanar8()](https://developer.apple.com/documentation/accelerate/1533091-vimageconvert_planar4toplanar8)Added [vImageConvert_Planar8toIndexed1()](https://developer.apple.com/documentation/accelerate/1533115-vimageconvert_planar8toindexed1)Added [vImageConvert_Planar8toIndexed2()](https://developer.apple.com/documentation/accelerate/1533017-vimageconvert_planar8toindexed2)Added [vImageConvert_Planar8toIndexed4()](https://developer.apple.com/documentation/accelerate/1533049-vimageconvert_planar8toindexed4)Added [vImageConvert_Planar8toPlanar1()](https://developer.apple.com/documentation/accelerate/1533024-vimageconvert_planar8toplanar1)Added [vImageConvert_Planar8toPlanar16F()](https://developer.apple.com/documentation/accelerate/1533064-vimageconvert_planar8toplanar16f)Added [vImageConvert_Planar8toPlanar2()](https://developer.apple.com/documentation/accelerate/1533166-vimageconvert_planar8toplanar2)Added [vImageConvert_Planar8toPlanar4()](https://developer.apple.com/documentation/accelerate/1533223-vimageconvert_planar8toplanar4)Added [vImageConvert_RGB16UToARGB8888()](https://developer.apple.com/documentation/accelerate/1533005-vimageconvert_rgb16utoargb8888)Added [vImageConvert_RGB16UtoARGB16U()](https://developer.apple.com/documentation/accelerate/1533272-vimageconvert_rgb16utoargb16u)Added [vImageConvert_RGB16UtoBGRA16U()](https://developer.apple.com/documentation/accelerate/1533033-vimageconvert_rgb16utobgra16u)Added [vImageConvert_RGB16UtoPlanar16U()](https://developer.apple.com/documentation/accelerate/1533021-vimageconvert_rgb16utoplanar16u)Added [vImageConvert_RGB16UtoRGBA16U()](https://developer.apple.com/documentation/accelerate/1533158-vimageconvert_rgb16utorgba16u)Added [vImageConvert_RGB565toBGRA8888()](https://developer.apple.com/documentation/accelerate/1533057-vimageconvert_rgb565tobgra8888)Added [vImageConvert_RGB565toRGBA8888()](https://developer.apple.com/documentation/accelerate/1533249-vimageconvert_rgb565torgba8888)Added [vImageConvert_RGB888toPlanar16Q12()](https://developer.apple.com/documentation/accelerate/1533023-vimageconvert_rgb888toplanar16q1)Added [vImageConvert_RGBA16UtoRGB16U()](https://developer.apple.com/documentation/accelerate/1533149-vimageconvert_rgba16utorgb16u)Added #def vImageConvert_RGBA8888toPlanar8Added [vImageConvert_RGBA8888toRGB565()](https://developer.apple.com/documentation/accelerate/1533162-vimageconvert_rgba8888torgb565)Added #def vImageConvert_RGBAFFFFtoPlanarFAdded [vImageConvert_RGBAFFFFtoRGBFFF()](https://developer.apple.com/documentation/accelerate/1533187-vimageconvert_rgbafffftorgbfff)Added [vImageConvert_RGBFFFtoARGBFFFF()](https://developer.apple.com/documentation/accelerate/1533175-vimageconvert_rgbffftoargbffff)Added [vImageConvert_RGBFFFtoBGRAFFFF()](https://developer.apple.com/documentation/accelerate/1533277-vimageconvert_rgbffftobgraffff)Added [vImageConvert_RGBFFFtoRGBAFFFF()](https://developer.apple.com/documentation/accelerate/1533050-vimageconvert_rgbffftorgbaffff)Added #def vImageConvert_RGBX8888ToPlanar8Added #def vImageConvert_RGBXFFFFToPlanarFAdded [vImageConvert_XRGB8888ToPlanar8()](https://developer.apple.com/documentation/accelerate/1533026-vimageconvert_xrgb8888toplanar8)Added [vImageConvert_XRGBFFFFToPlanarF()](https://developer.apple.com/documentation/accelerate/1533067-vimageconvert_xrgbfffftoplanarf)Added [vImageFlatten_ARGB16Q12()](https://developer.apple.com/documentation/accelerate/1533177-vimageflatten_argb16q12)Added [vImageFlatten_ARGB16U()](https://developer.apple.com/documentation/accelerate/1533278-vimageflatten_argb16u)Added [vImageFlatten_ARGB8888()](https://developer.apple.com/documentation/accelerate/1533236-vimageflatten_argb8888)Added [vImageFlatten_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1533071-vimageflatten_argbffff)Added #def vImageFlatten_BGRAFFFFToBGRFFFAdded [vImageFlatten_RGBA16Q12()](https://developer.apple.com/documentation/accelerate/1533112-vimageflatten_rgba16q12)Added [vImageFlatten_RGBA16U()](https://developer.apple.com/documentation/accelerate/1533048-vimageflatten_rgba16u)Added [vImageFlatten_RGBA8888()](https://developer.apple.com/documentation/accelerate/1532998-vimageflatten_rgba8888)Added [vImageFlatten_RGBAFFFF()](https://developer.apple.com/documentation/accelerate/1533221-vimageflatten_rgbaffff)Added #def vImageFlatten_RGBAFFFFToBGRFFFAdded [vImageOverwriteChannelsWithPixel_ARGB16U()](https://developer.apple.com/documentation/accelerate/1533053-vimageoverwritechannelswithpixel)Added [vImagePermuteChannelsWithMaskedInsert_ARGB8888()](https://developer.apple.com/documentation/accelerate/1533263-vimagepermutechannelswithmaskedi)Added [vImagePermuteChannelsWithMaskedInsert_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1533014-vimagepermutechannelswithmaskedi)Added [vImagePermuteChannels_ARGB16U()](https://developer.apple.com/documentation/accelerate/1533081-vimagepermutechannels_argb16u)Modified [vImageFlatten_ARGB8888ToRGB888()](https://developer.apple.com/documentation/accelerate/1533019-vimageflatten_argb8888torgb888)

|  | Declaration |
| --- | --- |
| From | vImage_Error vImageFlatten_ARGB8888ToRGB888 ( const vImage_Buffer \*, const vImage_Buffer \*, Pixel_8888, bool, vImage_Flags); |
| To | vImage_Error vImageFlatten_ARGB8888ToRGB888 ( const vImage_Buffer \*, const vImage_Buffer \*, const Pixel_8888, bool, vImage_Flags); |

Modified [vImageFlatten_ARGBFFFFToRGBFFF()](https://developer.apple.com/documentation/accelerate/1533210-vimageflatten_argbfffftorgbfff)

|  | Declaration |
| --- | --- |
| From | vImage_Error vImageFlatten_ARGBFFFFToRGBFFF ( const vImage_Buffer \*, const vImage_Buffer \*, Pixel_FFFF, bool, vImage_Flags); |
| To | vImage_Error vImageFlatten_ARGBFFFFToRGBFFF ( const vImage_Buffer \*, const vImage_Buffer \*, const Pixel_FFFF, bool, vImage_Flags); |

Modified [vImageFlatten_BGRA8888ToRGB888()](https://developer.apple.com/documentation/accelerate/1533119-vimageflatten_bgra8888torgb888)

|  | Declaration |
| --- | --- |
| From | vImage_Error vImageFlatten_BGRA8888ToRGB888 ( const vImage_Buffer \*, const vImage_Buffer \*, Pixel_8888, bool, vImage_Flags); |
| To | vImage_Error vImageFlatten_BGRA8888ToRGB888 ( const vImage_Buffer \*, const vImage_Buffer \*, const Pixel_8888, bool, vImage_Flags); |

Modified [vImageFlatten_BGRAFFFFToRGBFFF()](https://developer.apple.com/documentation/accelerate/1533156-vimageflatten_bgrafffftorgbfff)

|  | Declaration |
| --- | --- |
| From | vImage_Error vImageFlatten_BGRAFFFFToRGBFFF ( const vImage_Buffer \*, const vImage_Buffer \*, Pixel_FFFF, bool, vImage_Flags); |
| To | vImage_Error vImageFlatten_BGRAFFFFToRGBFFF ( const vImage_Buffer \*, const vImage_Buffer \*, const Pixel_FFFF, bool, vImage_Flags); |

Modified [vImageFlatten_RGBA8888ToRGB888()](https://developer.apple.com/documentation/accelerate/1533147-vimageflatten_rgba8888torgb888)

|  | Declaration |
| --- | --- |
| From | vImage_Error vImageFlatten_RGBA8888ToRGB888 ( const vImage_Buffer \*, const vImage_Buffer \*, Pixel_8888, bool, vImage_Flags); |
| To | vImage_Error vImageFlatten_RGBA8888ToRGB888 ( const vImage_Buffer \*, const vImage_Buffer \*, const Pixel_8888, bool, vImage_Flags); |

Modified [vImageFlatten_RGBAFFFFToRGBFFF()](https://developer.apple.com/documentation/accelerate/1533280-vimageflatten_rgbafffftorgbfff)

|  | Declaration |
| --- | --- |
| From | vImage_Error vImageFlatten_RGBAFFFFToRGBFFF ( const vImage_Buffer \*, const vImage_Buffer \*, Pixel_FFFF, bool, vImage_Flags); |
| To | vImage_Error vImageFlatten_RGBAFFFFToRGBFFF ( const vImage_Buffer \*, const vImage_Buffer \*, const Pixel_FFFF, bool, vImage_Flags); |

Geometry.hAdded [vImageAffineWarpCG_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509246-vimageaffinewarpcg_argb16s)Added [vImageAffineWarpCG_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509186-vimageaffinewarpcg_argb16u)Added [vImageAffineWarpD_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509282-vimageaffinewarpd_argb16s)Added [vImageAffineWarpD_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509292-vimageaffinewarpd_argb16u)Added [vImageAffineWarp_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509164-vimageaffinewarp_argb16s)Added [vImageAffineWarp_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509156-vimageaffinewarp_argb16u)Added [vImageGetResamplingFilterExtent()](https://developer.apple.com/documentation/accelerate/1509196-vimagegetresamplingfilterextent)Added [vImageHorizontalReflect_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509172-vimagehorizontalreflect_argb16s)Added [vImageHorizontalReflect_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509180-vimagehorizontalreflect_argb16u)Added [vImageHorizontalShearD_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509268-vimagehorizontalsheard_argb16s)Added [vImageHorizontalShearD_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509248-vimagehorizontalsheard_argb16u)Added [vImageHorizontalShear_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509194-vimagehorizontalshear_argb16s)Added [vImageHorizontalShear_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509274-vimagehorizontalshear_argb16u)Added [vImageRotate90_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509195-vimagerotate90_argb16s)Added [vImageRotate90_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509232-vimagerotate90_argb16u)Added [vImageRotate_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509206-vimagerotate_argb16s)Added [vImageRotate_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509235-vimagerotate_argb16u)Added [vImageScale_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509174-vimagescale_argb16s)Added [vImageScale_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509158-vimagescale_argb16u)Added [vImageVerticalReflect_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509267-vimageverticalreflect_argb16s)Added [vImageVerticalReflect_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509197-vimageverticalreflect_argb16u)Added [vImageVerticalShearD_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509278-vimageverticalsheard_argb16s)Added [vImageVerticalShearD_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509225-vimageverticalsheard_argb16u)Added [vImageVerticalShear_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509154-vimageverticalshear_argb16s)Added [vImageVerticalShear_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509227-vimageverticalshear_argb16u)Transform.hAdded [kvImageFullInterpolation](https://developer.apple.com/documentation/accelerate/kvimagefullinterpolation)Added [kvImageHalfInterpolation](https://developer.apple.com/documentation/accelerate/vimage_interpolationmethod/kvimagehalfinterpolation)Added [kvImageMDTableHint_16Q12](https://developer.apple.com/documentation/accelerate/kvimagemdtablehint_16q12)Added [kvImageMDTableHint_Float](https://developer.apple.com/documentation/accelerate/vimagemdtableusagehint/kvimagemdtablehint_float)Added [kvImageNoInterpolation](https://developer.apple.com/documentation/accelerate/kvimagenointerpolation)Added [vImageLookupTable_8to64U()](https://developer.apple.com/documentation/accelerate/1545860-vimagelookuptable_8to64u)Added [vImageLookupTable_Planar8toPlanar16()](https://developer.apple.com/documentation/accelerate/1545120-vimagelookuptable_planar8toplana)Added [vImageMDTableUsageHint](https://developer.apple.com/documentation/accelerate/vimagemdtableusagehint)Added [vImageMatrixMultiply_Planar16S()](https://developer.apple.com/documentation/accelerate/1545211-vimagematrixmultiply_planar16s)Added [vImageMultiDimensionalInterpolatedLookupTable_Planar16Q12()](https://developer.apple.com/documentation/accelerate/1546327-vimagemultidimensionalinterpolat)Added [vImageMultiDimensionalInterpolatedLookupTable_PlanarF()](https://developer.apple.com/documentation/accelerate/1546728-vimagemultidimensionalinterpolat)Added [vImageMultidimensionalTable_Create()](https://developer.apple.com/documentation/accelerate/1544435-vimagemultidimensionaltable_crea)Added [vImageMultidimensionalTable_Release()](https://developer.apple.com/documentation/accelerate/1546993-vimagemultidimensionaltable_rele)Added [vImageMultidimensionalTable_Retain()](https://developer.apple.com/documentation/accelerate/1545031-vimagemultidimensionaltable_reta)Added [vImagePiecewiseGamma_Planar16Q12()](https://developer.apple.com/documentation/accelerate/1545796-vimagepiecewisegamma_planar16q12)Added [vImagePiecewiseGamma_Planar16Q12toPlanar8()](https://developer.apple.com/documentation/accelerate/1544548-vimagepiecewisegamma_planar16q12)Added [vImagePiecewiseGamma_Planar8()](https://developer.apple.com/documentation/accelerate/1546371-vimagepiecewisegamma_planar8)Added [vImagePiecewiseGamma_Planar8toPlanar16Q12()](https://developer.apple.com/documentation/accelerate/1546537-vimagepiecewisegamma_planar8topl)Added [vImagePiecewiseGamma_Planar8toPlanarF()](https://developer.apple.com/documentation/accelerate/1544764-vimagepiecewisegamma_planar8topl)Added [vImagePiecewiseGamma_PlanarF()](https://developer.apple.com/documentation/accelerate/1544860-vimagepiecewisegamma_planarf)Added [vImagePiecewiseGamma_PlanarFtoPlanar8()](https://developer.apple.com/documentation/accelerate/1546645-vimagepiecewisegamma_planarftopl)Added [vImage_InterpolationMethod](https://developer.apple.com/documentation/accelerate/vimage_interpolationmethod)Added [vImage_MultidimensionalTable](https://developer.apple.com/documentation/accelerate/vimage_multidimensionaltable)cblas.hModified ATLU_DestroyThreadMemory()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

vDSP.hAdded [vDSP_DFT_DestroySetupD()](https://developer.apple.com/documentation/accelerate/1450367-vdsp_dft_destroysetupd)Added [vDSP_DFT_ExecuteD()](https://developer.apple.com/documentation/accelerate/1449812-vdsp_dft_executed)Added vDSP_DFT_SetupDAdded [vDSP_DFT_zop_CreateSetupD()](https://developer.apple.com/documentation/accelerate/1450730-vdsp_dft_zop_createsetupd)Added [vDSP_DFT_zrop_CreateSetupD()](https://developer.apple.com/documentation/accelerate/1449790-vdsp_dft_zrop_createsetupd)Added [vDSP_biquadm()](https://developer.apple.com/documentation/accelerate/1450603-vdsp_biquadm)Added [vDSP_biquadm_CopyState()](https://developer.apple.com/documentation/kernel/1579980-vdsp_biquadm_copystate)Added [vDSP_biquadm_CreateSetup()](https://developer.apple.com/documentation/kernel/1579945-vdsp_biquadm_createsetup)Added [vDSP_biquadm_DestroySetup()](https://developer.apple.com/documentation/kernel/1579970-vdsp_biquadm_destroysetup)Added [vDSP_biquadm_ResetState()](https://developer.apple.com/documentation/accelerate/1449898-vdsp_biquadm_resetstate)Added [vDSP_biquadm_Setup](https://developer.apple.com/documentation/kernel/vdsp_biquadm_setup)Added [vDSP_int24](https://developer.apple.com/documentation/accelerate/vdsp_int24)Added [vDSP_uint24](https://developer.apple.com/documentation/accelerate/vdsp_uint24)Added [vDSP_vaddi()](https://developer.apple.com/documentation/accelerate/1450179-vdsp_vaddi)Added [vDSP_vflt24()](https://developer.apple.com/documentation/accelerate/1450529-vdsp_vflt24)Added [vDSP_vfltsm24()](https://developer.apple.com/documentation/accelerate/1450177-vdsp_vfltsm24)Added [vDSP_vfltsmu24()](https://developer.apple.com/documentation/accelerate/1449841-vdsp_vfltsmu24)Added [vDSP_vfltu24()](https://developer.apple.com/documentation/accelerate/1450084-vdsp_vfltu24)Added [vDSP_vsmfix24()](https://developer.apple.com/documentation/accelerate/1449670-vdsp_vsmfix24)Added [vDSP_vsmfixu24()](https://developer.apple.com/documentation/kernel/1532178-vdsp_vsmfixu24)Added [vDSP_zvma()](https://developer.apple.com/documentation/accelerate/1449940-vdsp_zvma)Added [vDSP_zvmmaa()](https://developer.apple.com/documentation/accelerate/1450110-vdsp_zvmmaa)Modified [vDSP_biquad()](https://developer.apple.com/documentation/accelerate/1450838-vdsp_biquad)

|  | Declaration |
| --- | --- |
| From | void vDSP_biquad ( const struct vDSP_biquad_SetupStruct \*__vDSP_setup, float \*__vDSP_delay, const float \*__vDSP_X, vDSP_Stride __vDSP_IX, float \*__vDSP_Y, vDSP_Stride __vDSP_IY, vDSP_Length __vDSP_N); |
| To | void vDSP_biquad ( const struct vDSP_biquad_SetupStruct \*__vDSP_Setup, float \*__vDSP_Delay, const float \*__vDSP_X, vDSP_Stride __vDSP_IX, float \*__vDSP_Y, vDSP_Stride __vDSP_IY, vDSP_Length __vDSP_N); |

Modified [vDSP_biquadD()](https://developer.apple.com/documentation/accelerate/1450359-vdsp_biquadd)

|  | Declaration |
| --- | --- |
| From | void vDSP_biquadD ( const struct vDSP_biquad_SetupStructD \*__vDSP_setup, double \*__vDSP_delay, const double \*__vDSP_X, vDSP_Stride __vDSP_IX, double \*__vDSP_Y, vDSP_Stride __vDSP_IY, vDSP_Length __vDSP_N); |
| To | void vDSP_biquadD ( const struct vDSP_biquad_SetupStructD \*__vDSP_Setup, double \*__vDSP_Delay, const double \*__vDSP_X, vDSP_Stride __vDSP_IX, double \*__vDSP_Y, vDSP_Stride __vDSP_IY, vDSP_Length __vDSP_N); |

Modified [vDSP_biquad_CreateSetup()](https://developer.apple.com/documentation/accelerate/1450374-vdsp_biquad_createsetup)

|  | Declaration |
| --- | --- |
| From | vDSP_biquad_Setup vDSP_biquad_CreateSetup ( const double \*__vDSP_coeffs, vDSP_Length __vDSP_M); |
| To | vDSP_biquad_Setup vDSP_biquad_CreateSetup ( const double \*__vDSP_Coefficients, vDSP_Length __vDSP_M); |

Modified [vDSP_biquad_CreateSetupD()](https://developer.apple.com/documentation/accelerate/1450239-vdsp_biquad_createsetupd)

|  | Declaration |
| --- | --- |
| From | vDSP_biquad_SetupD vDSP_biquad_CreateSetupD ( const double \*__vDSP_coeffs, vDSP_Length __vDSP_M); |
| To | vDSP_biquad_SetupD vDSP_biquad_CreateSetupD ( const double \*__vDSP_Coefficients, vDSP_Length __vDSP_M); |

Modified [vDSP_blkman_window()](https://developer.apple.com/documentation/accelerate/1450190-vdsp_blkman_window)

|  | Declaration |
| --- | --- |
| From | void vDSP_blkman_window ( float \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_FLAG); |
| To | void vDSP_blkman_window ( float \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_Flag); |

Modified [vDSP_blkman_windowD()](https://developer.apple.com/documentation/accelerate/1450471-vdsp_blkman_windowd)

|  | Declaration |
| --- | --- |
| From | void vDSP_blkman_windowD ( double \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_FLAG); |
| To | void vDSP_blkman_windowD ( double \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_Flag); |

Modified [vDSP_conv()](https://developer.apple.com/documentation/kernel/1532184-vdsp_conv)

|  | Declaration |
| --- | --- |
| From | void vDSP_conv ( const float __vDSP_signal[], vDSP_Stride __vDSP_signalStride, const float __vDSP_filter[], vDSP_Stride __vDSP_strideFilter, float __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_lenResult, vDSP_Length __vDSP_lenFilter); |
| To | void vDSP_conv ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_F, vDSP_Stride __vDSP_IF, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_convD()](https://developer.apple.com/documentation/accelerate/1450637-vdsp_convd)

|  | Declaration |
| --- | --- |
| From | void vDSP_convD ( const double __vDSP_signal[], vDSP_Stride __vDSP_signalStride, const double __vDSP_filter[], vDSP_Stride __vDSP_strideFilter, double __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_lenResult, vDSP_Length __vDSP_lenFilter); |
| To | void vDSP_convD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_F, vDSP_Stride __vDSP_IF, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_create_fftsetup()](https://developer.apple.com/documentation/kernel/1580009-vdsp_create_fftsetup)

|  | Declaration |
| --- | --- |
| From | FFTSetup vDSP_create_fftsetup ( vDSP_Length __vDSP_log2n, FFTRadix __vDSP_radix); |
| To | FFTSetup vDSP_create_fftsetup ( vDSP_Length __vDSP_Log2n, FFTRadix __vDSP_Radix); |

Modified [vDSP_create_fftsetupD()](https://developer.apple.com/documentation/accelerate/1449974-vdsp_create_fftsetupd)

|  | Declaration |
| --- | --- |
| From | FFTSetupD vDSP_create_fftsetupD ( vDSP_Length __vDSP_log2n, FFTRadix __vDSP_radix); |
| To | FFTSetupD vDSP_create_fftsetupD ( vDSP_Length __vDSP_Log2n, FFTRadix __vDSP_Radix); |

Modified [vDSP_ctoz()](https://developer.apple.com/documentation/kernel/1579975-vdsp_ctoz)

|  | Declaration |
| --- | --- |
| From | void vDSP_ctoz ( const DSPComplex __vDSP_C[], vDSP_Stride __vDSP_strideC, DSPSplitComplex \*__vDSP_Z, vDSP_Stride __vDSP_strideZ, vDSP_Length __vDSP_size); |
| To | void vDSP_ctoz ( const DSPComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_Z, vDSP_Stride __vDSP_IZ, vDSP_Length __vDSP_N); |

Modified [vDSP_ctozD()](https://developer.apple.com/documentation/accelerate/1449970-vdsp_ctozd)

|  | Declaration |
| --- | --- |
| From | void vDSP_ctozD ( const DSPDoubleComplex __vDSP_C[], vDSP_Stride __vDSP_strideC, DSPDoubleSplitComplex \*__vDSP_Z, vDSP_Stride __vDSP_strideZ, vDSP_Length __vDSP_size); |
| To | void vDSP_ctozD ( const DSPDoubleComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_Z, vDSP_Stride __vDSP_IZ, vDSP_Length __vDSP_N); |

Modified [vDSP_deq22()](https://developer.apple.com/documentation/kernel/1532225-vdsp_deq22)

|  | Declaration |
| --- | --- |
| From | void vDSP_deq22 ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_deq22 ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_deq22D()](https://developer.apple.com/documentation/accelerate/1450534-vdsp_deq22d)

|  | Declaration |
| --- | --- |
| From | void vDSP_deq22D ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_deq22D ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_desamp()](https://developer.apple.com/documentation/accelerate/1449946-vdsp_desamp)

|  | Declaration |
| --- | --- |
| From | void vDSP_desamp ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |
| To | void vDSP_desamp ( const float \*__vDSP_A, vDSP_Stride __vDSP_I, const float \*__vDSP_F, float \*__vDSP_C, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_desampD()](https://developer.apple.com/documentation/accelerate/1450133-vdsp_desampd)

|  | Declaration |
| --- | --- |
| From | void vDSP_desampD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |
| To | void vDSP_desampD ( const double \*__vDSP_A, vDSP_Stride __vDSP_I, const double \*__vDSP_F, double \*__vDSP_C, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_distancesq()](https://developer.apple.com/documentation/accelerate/1450619-vdsp_distancesq)

|  | Declaration |
| --- | --- |
| From | void vDSP_distancesq ( const float __vDSP_input1[], vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, float \*__vDSP_result, vDSP_Length __vDSP_size); |
| To | void vDSP_distancesq ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_dotpr()](https://developer.apple.com/documentation/accelerate/1450313-vdsp_dotpr)

|  | Declaration |
| --- | --- |
| From | void vDSP_dotpr ( const float __vDSP_input1[], vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, float \*__vDSP_result, vDSP_Length __vDSP_size); |
| To | void vDSP_dotpr ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_dotprD()](https://developer.apple.com/documentation/accelerate/1450330-vdsp_dotprd)

|  | Declaration |
| --- | --- |
| From | void vDSP_dotprD ( const double __vDSP_input1[], vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, double \*__vDSP_result, vDSP_Length __vDSP_size); |
| To | void vDSP_dotprD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_f3x3()](https://developer.apple.com/documentation/accelerate/1450690-vdsp_f3x3)

|  | Declaration |
| --- | --- |
| From | void vDSP_f3x3 ( float \*__vDSP_signal, vDSP_Length __vDSP_rows, vDSP_Length __vDSP_cols, float \*__vDSP_filter, float \*__vDSP_result); |
| To | void vDSP_f3x3 ( const float \*__vDSP_A, vDSP_Length __vDSP_NR, vDSP_Length __vDSP_NC, const float \*__vDSP_F, float \*__vDSP_C); |

Modified [vDSP_f3x3D()](https://developer.apple.com/documentation/accelerate/1450651-vdsp_f3x3d)

|  | Declaration |
| --- | --- |
| From | void vDSP_f3x3D ( double \*__vDSP_signal, vDSP_Length __vDSP_rows, vDSP_Length __vDSP_cols, double \*__vDSP_filter, double \*__vDSP_result); |
| To | void vDSP_f3x3D ( const double \*__vDSP_A, vDSP_Length __vDSP_NR, vDSP_Length __vDSP_NC, const double \*__vDSP_F, double \*__vDSP_C); |

Modified [vDSP_f5x5()](https://developer.apple.com/documentation/accelerate/1450036-vdsp_f5x5)

|  | Declaration |
| --- | --- |
| From | void vDSP_f5x5 ( float \*__vDSP_signal, vDSP_Length __vDSP_rows, vDSP_Length __vDSP_cols, float \*__vDSP_filter, float \*__vDSP_result); |
| To | void vDSP_f5x5 ( const float \*__vDSP_A, vDSP_Length __vDSP_NR, vDSP_Length __vDSP_NC, const float \*__vDSP_F, float \*__vDSP_C); |

Modified [vDSP_f5x5D()](https://developer.apple.com/documentation/accelerate/1449839-vdsp_f5x5d)

|  | Declaration |
| --- | --- |
| From | void vDSP_f5x5D ( double \*__vDSP_signal, vDSP_Length __vDSP_rows, vDSP_Length __vDSP_cols, double \*__vDSP_filter, double \*__vDSP_result); |
| To | void vDSP_f5x5D ( const double \*__vDSP_A, vDSP_Length __vDSP_NR, vDSP_Length __vDSP_NC, const double \*__vDSP_F, double \*__vDSP_C); |

Modified [vDSP_fft2d_zip()](https://developer.apple.com/documentation/accelerate/1450430-vdsp_fft2d_zip)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zip ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_strideInRow, vDSP_Stride __vDSP_strideInCol, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_direction); |
| To | void vDSP_fft2d_zip ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft2d_zipD()](https://developer.apple.com/documentation/accelerate/1450508-vdsp_fft2d_zipd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zipD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_strideInRow, vDSP_Stride __vDSP_strideInCol, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_direction); |
| To | void vDSP_fft2d_zipD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft2d_zipt()](https://developer.apple.com/documentation/accelerate/1450777-vdsp_fft2d_zipt)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zipt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_strideInRow, vDSP_Stride __vDSP_strideInCol, DSPSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_direction); |
| To | void vDSP_fft2d_zipt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC1, vDSP_Stride __vDSP_IC0, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft2d_ziptD()](https://developer.apple.com/documentation/accelerate/1450202-vdsp_fft2d_ziptd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_ziptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_strideInRow, vDSP_Stride __vDSP_strideInCol, DSPDoubleSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_direction); |
| To | void vDSP_fft2d_ziptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft2d_zop()](https://developer.apple.com/documentation/accelerate/1450355-vdsp_fft2d_zop)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zop ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStrideInRow, vDSP_Stride __vDSP_signalStrideInCol, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResultInRow, vDSP_Stride __vDSP_strideResultInCol, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_flag); |
| To | void vDSP_fft2d_zop ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA0, vDSP_Stride __vDSP_IA1, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft2d_zopD()](https://developer.apple.com/documentation/accelerate/1449944-vdsp_fft2d_zopd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zopD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStrideInRow, vDSP_Stride __vDSP_signalStrideInCol, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResultInRow, vDSP_Stride __vDSP_strideResultInCol, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_flag); |
| To | void vDSP_fft2d_zopD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA0, vDSP_Stride __vDSP_IA1, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft2d_zopt()](https://developer.apple.com/documentation/accelerate/1450816-vdsp_fft2d_zopt)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zopt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStrideInRow, vDSP_Stride __vDSP_signalStrideInCol, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResultInRow, vDSP_Stride __vDSP_strideResultInCol, DSPSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_flag); |
| To | void vDSP_fft2d_zopt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA0, vDSP_Stride __vDSP_IA1, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft2d_zoptD()](https://developer.apple.com/documentation/accelerate/1449963-vdsp_fft2d_zoptd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zoptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStrideInRow, vDSP_Stride __vDSP_signalStrideInCol, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResultInRow, vDSP_Stride __vDSP_strideResultInCol, DSPDoubleSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_flag); |
| To | void vDSP_fft2d_zoptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA0, vDSP_Stride __vDSP_IA1, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft2d_zrip()](https://developer.apple.com/documentation/accelerate/1450116-vdsp_fft2d_zrip)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zrip ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_strideInRow, vDSP_Stride __vDSP_strideInCol, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_direction); |
| To | void vDSP_fft2d_zrip ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft2d_zripD()](https://developer.apple.com/documentation/accelerate/1450384-vdsp_fft2d_zripd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zripD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_strideInRow, vDSP_Stride __vDSP_strideInCol, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_flag); |
| To | void vDSP_fft2d_zripD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_flag); |

Modified [vDSP_fft2d_zript()](https://developer.apple.com/documentation/accelerate/1450144-vdsp_fft2d_zript)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zript ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_strideInRow, vDSP_Stride __vDSP_strideInCol, DSPSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_direction); |
| To | void vDSP_fft2d_zript ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft2d_zriptD()](https://developer.apple.com/documentation/accelerate/1450079-vdsp_fft2d_zriptd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zriptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_strideInRow, vDSP_Stride __vDSP_strideInCol, DSPDoubleSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_flag); |
| To | void vDSP_fft2d_zriptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_flag); |

Modified [vDSP_fft2d_zrop()](https://developer.apple.com/documentation/accelerate/1450361-vdsp_fft2d_zrop)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zrop ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStrideInRow, vDSP_Stride __vDSP_signalStrideInCol, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResultInRow, vDSP_Stride __vDSP_strideResultInCol, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_flag); |
| To | void vDSP_fft2d_zrop ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA0, vDSP_Stride __vDSP_IA1, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft2d_zropD()](https://developer.apple.com/documentation/accelerate/1450732-vdsp_fft2d_zropd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zropD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_Kr, vDSP_Stride __vDSP_Kc, DSPDoubleSplitComplex \*__vDSP_ioData2, vDSP_Stride __vDSP_Ir, vDSP_Stride __vDSP_Ic, vDSP_Length __vDSP_log2nc, vDSP_Length __vDSP_log2nr, FFTDirection __vDSP_flag); |
| To | void vDSP_fft2d_zropD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA0, vDSP_Stride __vDSP_IA1, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft2d_zropt()](https://developer.apple.com/documentation/accelerate/1450460-vdsp_fft2d_zropt)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zropt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStrideInRow, vDSP_Stride __vDSP_signalStrideInCol, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResultInRow, vDSP_Stride __vDSP_strideResultInCol, DSPSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_flag); |
| To | void vDSP_fft2d_zropt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA0, vDSP_Stride __vDSP_IA1, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft2d_zroptD()](https://developer.apple.com/documentation/accelerate/1450433-vdsp_fft2d_zroptd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zroptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_Kr, vDSP_Stride __vDSP_Kc, DSPDoubleSplitComplex \*__vDSP_ioData2, vDSP_Stride __vDSP_Ir, vDSP_Stride __vDSP_Ic, DSPDoubleSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2nc, vDSP_Length __vDSP_log2nr, FFTDirection __vDSP_flag); |
| To | void vDSP_fft2d_zroptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA0, vDSP_Stride __vDSP_IA1, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft3_zop()](https://developer.apple.com/documentation/accelerate/1450494-vdsp_fft3_zop)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft3_zop ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_flag); |
| To | void vDSP_fft3_zop ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft3_zopD()](https://developer.apple.com/documentation/accelerate/1450124-vdsp_fft3_zopd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft3_zopD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_K, DSPDoubleSplitComplex \*__vDSP_ioData2, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_flag); |
| To | void vDSP_fft3_zopD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft5_zop()](https://developer.apple.com/documentation/accelerate/1450044-vdsp_fft5_zop)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft5_zop ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_flag); |
| To | void vDSP_fft5_zop ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft5_zopD()](https://developer.apple.com/documentation/accelerate/1450738-vdsp_fft5_zopd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft5_zopD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_K, DSPDoubleSplitComplex \*__vDSP_ioData2, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_flag); |
| To | void vDSP_fft5_zopD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zip()](https://developer.apple.com/documentation/accelerate/1450224-vdsp_fft_zip)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zip ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_stride, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void vDSP_fft_zip ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zipD()](https://developer.apple.com/documentation/accelerate/1449916-vdsp_fft_zipd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zipD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_stride, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void vDSP_fft_zipD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zipt()](https://developer.apple.com/documentation/accelerate/1449879-vdsp_fft_zipt)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zipt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_stride, DSPSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void vDSP_fft_zipt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_ziptD()](https://developer.apple.com/documentation/accelerate/1450852-vdsp_fft_ziptd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_ziptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_stride, DSPDoubleSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void vDSP_fft_ziptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zop()](https://developer.apple.com/documentation/accelerate/1450581-vdsp_fft_zop)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zop ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void vDSP_fft_zop ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zopD()](https://developer.apple.com/documentation/accelerate/1450694-vdsp_fft_zopd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zopD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void vDSP_fft_zopD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zopt()](https://developer.apple.com/documentation/accelerate/1450812-vdsp_fft_zopt)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zopt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, DSPSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void vDSP_fft_zopt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zoptD()](https://developer.apple.com/documentation/accelerate/1450447-vdsp_fft_zoptd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zoptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, DSPDoubleSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void vDSP_fft_zoptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zrip()](https://developer.apple.com/documentation/kernel/1579997-vdsp_fft_zrip)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zrip ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_stride, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void vDSP_fft_zrip ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zripD()](https://developer.apple.com/documentation/accelerate/1450371-vdsp_fft_zripd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zripD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_stride, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_flag); |
| To | void vDSP_fft_zripD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zript()](https://developer.apple.com/documentation/accelerate/1450455-vdsp_fft_zript)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zript ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_stride, DSPSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void vDSP_fft_zript ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zriptD()](https://developer.apple.com/documentation/accelerate/1450486-vdsp_fft_zriptd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zriptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_stride, DSPDoubleSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_flag); |
| To | void vDSP_fft_zriptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zrop()](https://developer.apple.com/documentation/accelerate/1449994-vdsp_fft_zrop)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zrop ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void vDSP_fft_zrop ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zropD()](https://developer.apple.com/documentation/accelerate/1449666-vdsp_fft_zropd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zropD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_flag); |
| To | void vDSP_fft_zropD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zropt()](https://developer.apple.com/documentation/accelerate/1450404-vdsp_fft_zropt)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zropt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, DSPSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void vDSP_fft_zropt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zroptD()](https://developer.apple.com/documentation/accelerate/1450828-vdsp_fft_zroptd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zroptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, DSPDoubleSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_flag); |
| To | void vDSP_fft_zroptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zip()](https://developer.apple.com/documentation/accelerate/1450798-vdsp_fftm_zip)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zip ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zip ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IM, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zipD()](https://developer.apple.com/documentation/accelerate/1449959-vdsp_fftm_zipd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zipD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zipD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IM, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zipt()](https://developer.apple.com/documentation/accelerate/1449852-vdsp_fftm_zipt)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zipt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zipt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IM, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_ziptD()](https://developer.apple.com/documentation/accelerate/1450092-vdsp_fftm_ziptd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_ziptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPDoubleSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_ziptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IM, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zop()](https://developer.apple.com/documentation/accelerate/1450053-vdsp_fftm_zop)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zop ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Stride __vDSP_rfftStride, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zop ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Stride __vDSP_IMA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IMC, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zopD()](https://developer.apple.com/documentation/accelerate/1450439-vdsp_fftm_zopd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zopD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Stride __vDSP_rfftStride, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zopD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Stride __vDSP_IMA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IMC, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zopt()](https://developer.apple.com/documentation/accelerate/1449737-vdsp_fftm_zopt)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zopt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Stride __vDSP_rfftStride, DSPSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zopt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Stride __vDSP_IMA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IMC, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zoptD()](https://developer.apple.com/documentation/accelerate/1450596-vdsp_fftm_zoptd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zoptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Stride __vDSP_rfftStride, DSPDoubleSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zoptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Stride __vDSP_IMA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IMC, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zrip()](https://developer.apple.com/documentation/accelerate/1449883-vdsp_fftm_zrip)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zrip ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zrip ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IM, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zripD()](https://developer.apple.com/documentation/accelerate/1450075-vdsp_fftm_zripd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zripD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zripD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IM, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zript()](https://developer.apple.com/documentation/accelerate/1450050-vdsp_fftm_zript)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zript ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zript ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IM, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zriptD()](https://developer.apple.com/documentation/accelerate/1450514-vdsp_fftm_zriptd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zriptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPDoubleSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zriptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IM, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zrop()](https://developer.apple.com/documentation/accelerate/1450073-vdsp_fftm_zrop)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zrop ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Stride __vDSP_rfftStride, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zrop ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Stride __vDSP_IMA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IMC, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zropD()](https://developer.apple.com/documentation/accelerate/1449714-vdsp_fftm_zropd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zropD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Stride __vDSP_rfftStride, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zropD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Stride __vDSP_IMA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IMC, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zropt()](https://developer.apple.com/documentation/accelerate/1450659-vdsp_fftm_zropt)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zropt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Stride __vDSP_rfftStride, DSPSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zropt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Stride __vDSP_IMA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IMC, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zroptD()](https://developer.apple.com/documentation/accelerate/1450320-vdsp_fftm_zroptd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zroptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Stride __vDSP_rfftStride, DSPDoubleSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zroptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Stride __vDSP_IMA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IMC, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_hamm_window()](https://developer.apple.com/documentation/accelerate/1450040-vdsp_hamm_window)

|  | Declaration |
| --- | --- |
| From | void vDSP_hamm_window ( float \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_FLAG); |
| To | void vDSP_hamm_window ( float \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_Flag); |

Modified [vDSP_hamm_windowD()](https://developer.apple.com/documentation/accelerate/1450721-vdsp_hamm_windowd)

|  | Declaration |
| --- | --- |
| From | void vDSP_hamm_windowD ( double \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_FLAG); |
| To | void vDSP_hamm_windowD ( double \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_Flag); |

Modified [vDSP_hann_window()](https://developer.apple.com/documentation/accelerate/1450263-vdsp_hann_window)

|  | Declaration |
| --- | --- |
| From | void vDSP_hann_window ( float \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_FLAG); |
| To | void vDSP_hann_window ( float \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_Flag); |

Modified [vDSP_hann_windowD()](https://developer.apple.com/documentation/accelerate/1450048-vdsp_hann_windowd)

|  | Declaration |
| --- | --- |
| From | void vDSP_hann_windowD ( double \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_FLAG); |
| To | void vDSP_hann_windowD ( double \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_Flag); |

Modified [vDSP_imgfir()](https://developer.apple.com/documentation/accelerate/1449856-vdsp_imgfir)

|  | Declaration |
| --- | --- |
| From | void vDSP_imgfir ( float \*__vDSP_signal, vDSP_Length __vDSP_numRow, vDSP_Length __vDSP_numCol, float \*__vDSP_filter, float \*__vDSP_result, vDSP_Length __vDSP_fnumRow, vDSP_Length __vDSP_fnumCol); |
| To | void vDSP_imgfir ( const float \*__vDSP_A, vDSP_Length __vDSP_NR, vDSP_Length __vDSP_NC, const float \*__vDSP_F, float \*__vDSP_C, vDSP_Length __vDSP_P, vDSP_Length __vDSP_Q); |

Modified [vDSP_imgfirD()](https://developer.apple.com/documentation/accelerate/1449818-vdsp_imgfird)

|  | Declaration |
| --- | --- |
| From | void vDSP_imgfirD ( double \*__vDSP_signal, vDSP_Length __vDSP_numRow, vDSP_Length __vDSP_numCol, double \*__vDSP_filter, double \*__vDSP_result, vDSP_Length __vDSP_fnumRow, vDSP_Length __vDSP_fnumCol); |
| To | void vDSP_imgfirD ( const double \*__vDSP_A, vDSP_Length __vDSP_NR, vDSP_Length __vDSP_NC, const double \*__vDSP_F, double \*__vDSP_C, vDSP_Length __vDSP_P, vDSP_Length __vDSP_Q); |

Modified [vDSP_maxmgv()](https://developer.apple.com/documentation/kernel/1532187-vdsp_maxmgv)

|  | Declaration |
| --- | --- |
| From | void vDSP_maxmgv ( const float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_maxmgv ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_maxmgvD()](https://developer.apple.com/documentation/accelerate/1450633-vdsp_maxmgvd)

|  | Declaration |
| --- | --- |
| From | void vDSP_maxmgvD ( const double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_maxmgvD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_maxmgvi()](https://developer.apple.com/documentation/accelerate/1450576-vdsp_maxmgvi)

|  | Declaration |
| --- | --- |
| From | void vDSP_maxmgvi ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length \*__vDSP_IC, vDSP_Length __vDSP_N); |
| To | void vDSP_maxmgvi ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length \*__vDSP_I, vDSP_Length __vDSP_N); |

Modified [vDSP_maxmgviD()](https://developer.apple.com/documentation/accelerate/1450249-vdsp_maxmgvid)

|  | Declaration |
| --- | --- |
| From | void vDSP_maxmgviD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length \*__vDSP_IC, vDSP_Length __vDSP_N); |
| To | void vDSP_maxmgviD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length \*__vDSP_I, vDSP_Length __vDSP_N); |

Modified [vDSP_maxv()](https://developer.apple.com/documentation/kernel/1580003-vdsp_maxv)

|  | Declaration |
| --- | --- |
| From | void vDSP_maxv ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_maxv ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_maxvD()](https://developer.apple.com/documentation/accelerate/1449854-vdsp_maxvd)

|  | Declaration |
| --- | --- |
| From | void vDSP_maxvD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_maxvD ( const double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_maxvi()](https://developer.apple.com/documentation/accelerate/1450814-vdsp_maxvi)

|  | Declaration |
| --- | --- |
| From | void vDSP_maxvi ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length \*__vDSP_IC, vDSP_Length __vDSP_N); |
| To | void vDSP_maxvi ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length \*__vDSP_I, vDSP_Length __vDSP_N); |

Modified [vDSP_maxviD()](https://developer.apple.com/documentation/accelerate/1449682-vdsp_maxvid)

|  | Declaration |
| --- | --- |
| From | void vDSP_maxviD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length \*__vDSP_IC, vDSP_Length __vDSP_N); |
| To | void vDSP_maxviD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length \*__vDSP_I, vDSP_Length __vDSP_N); |

Modified [vDSP_meamgv()](https://developer.apple.com/documentation/accelerate/1449731-vdsp_meamgv)

|  | Declaration |
| --- | --- |
| From | void vDSP_meamgv ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_meamgv ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_meamgvD()](https://developer.apple.com/documentation/accelerate/1450214-vdsp_meamgvd)

|  | Declaration |
| --- | --- |
| From | void vDSP_meamgvD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_meamgvD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_meanv()](https://developer.apple.com/documentation/accelerate/1449980-vdsp_meanv)

|  | Declaration |
| --- | --- |
| From | void vDSP_meanv ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_meanv ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_meanvD()](https://developer.apple.com/documentation/accelerate/1449784-vdsp_meanvd)

|  | Declaration |
| --- | --- |
| From | void vDSP_meanvD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_meanvD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_measqv()](https://developer.apple.com/documentation/accelerate/1450014-vdsp_measqv)

|  | Declaration |
| --- | --- |
| From | void vDSP_measqv ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_measqv ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_measqvD()](https://developer.apple.com/documentation/accelerate/1450463-vdsp_measqvd)

|  | Declaration |
| --- | --- |
| From | void vDSP_measqvD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_measqvD ( const double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_minmgv()](https://developer.apple.com/documentation/accelerate/1449786-vdsp_minmgv)

|  | Declaration |
| --- | --- |
| From | void vDSP_minmgv ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_minmgv ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_minmgvD()](https://developer.apple.com/documentation/accelerate/1449830-vdsp_minmgvd)

|  | Declaration |
| --- | --- |
| From | void vDSP_minmgvD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_minmgvD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_minmgvi()](https://developer.apple.com/documentation/accelerate/1449814-vdsp_minmgvi)

|  | Declaration |
| --- | --- |
| From | void vDSP_minmgvi ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length \*__vDSP_IC, vDSP_Length __vDSP_N); |
| To | void vDSP_minmgvi ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length \*__vDSP_I, vDSP_Length __vDSP_N); |

Modified [vDSP_minmgviD()](https://developer.apple.com/documentation/accelerate/1450843-vdsp_minmgvid)

|  | Declaration |
| --- | --- |
| From | void vDSP_minmgviD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length \*__vDSP_IC, vDSP_Length __vDSP_N); |
| To | void vDSP_minmgviD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length \*__vDSP_I, vDSP_Length __vDSP_N); |

Modified [vDSP_minv()](https://developer.apple.com/documentation/accelerate/1450267-vdsp_minv)

|  | Declaration |
| --- | --- |
| From | void vDSP_minv ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_minv ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_minvD()](https://developer.apple.com/documentation/accelerate/1450663-vdsp_minvd)

|  | Declaration |
| --- | --- |
| From | void vDSP_minvD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_minvD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_minvi()](https://developer.apple.com/documentation/accelerate/1449875-vdsp_minvi)

|  | Declaration |
| --- | --- |
| From | void vDSP_minvi ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length \*__vDSP_IC, vDSP_Length __vDSP_N); |
| To | void vDSP_minvi ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length \*__vDSP_I, vDSP_Length __vDSP_N); |

Modified [vDSP_minviD()](https://developer.apple.com/documentation/accelerate/1450441-vdsp_minvid)

|  | Declaration |
| --- | --- |
| From | void vDSP_minviD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length \*__vDSP_IC, vDSP_Length __vDSP_N); |
| To | void vDSP_minviD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length \*__vDSP_I, vDSP_Length __vDSP_N); |

Modified [vDSP_mmov()](https://developer.apple.com/documentation/accelerate/1449950-vdsp_mmov)

|  | Declaration |
| --- | --- |
| From | void vDSP_mmov ( float \*__vDSP_A, float \*__vDSP_C, vDSP_Length __vDSP_NC, vDSP_Length __vDSP_NR, vDSP_Length __vDSP_TCA, vDSP_Length __vDSP_TCC); |
| To | void vDSP_mmov ( const float \*__vDSP_A, float \*__vDSP_C, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_TA, vDSP_Length __vDSP_TC); |

Modified [vDSP_mmovD()](https://developer.apple.com/documentation/accelerate/1449956-vdsp_mmovd)

|  | Declaration |
| --- | --- |
| From | void vDSP_mmovD ( double \*__vDSP_A, double \*__vDSP_C, vDSP_Length __vDSP_NC, vDSP_Length __vDSP_NR, vDSP_Length __vDSP_TCA, vDSP_Length __vDSP_TCC); |
| To | void vDSP_mmovD ( const double \*__vDSP_A, double \*__vDSP_C, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_TA, vDSP_Length __vDSP_TC); |

Modified [vDSP_mmul()](https://developer.apple.com/documentation/accelerate/1449984-vdsp_mmul)

|  | Declaration |
| --- | --- |
| From | void vDSP_mmul ( float \*__vDSP_a, vDSP_Stride __vDSP_aStride, float \*__vDSP_b, vDSP_Stride __vDSP_bStride, float \*__vDSP_c, vDSP_Stride __vDSP_cStride, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_mmul ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_mmulD()](https://developer.apple.com/documentation/accelerate/1450386-vdsp_mmuld)

|  | Declaration |
| --- | --- |
| From | void vDSP_mmulD ( double \*__vDSP_a, vDSP_Stride __vDSP_aStride, double \*__vDSP_b, vDSP_Stride __vDSP_bStride, double \*__vDSP_c, vDSP_Stride __vDSP_cStride, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_mmulD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_mtrans()](https://developer.apple.com/documentation/accelerate/1449988-vdsp_mtrans)

|  | Declaration |
| --- | --- |
| From | void vDSP_mtrans ( float \*__vDSP_a, vDSP_Stride __vDSP_aStride, float \*__vDSP_c, vDSP_Stride __vDSP_cStride, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_mtrans ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N); |

Modified [vDSP_mtransD()](https://developer.apple.com/documentation/accelerate/1450422-vdsp_mtransd)

|  | Declaration |
| --- | --- |
| From | void vDSP_mtransD ( double \*__vDSP_a, vDSP_Stride __vDSP_aStride, double \*__vDSP_c, vDSP_Stride __vDSP_cStride, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_mtransD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N); |

Modified [vDSP_mvessq()](https://developer.apple.com/documentation/accelerate/1449849-vdsp_mvessq)

|  | Declaration |
| --- | --- |
| From | void vDSP_mvessq ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_mvessq ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_mvessqD()](https://developer.apple.com/documentation/accelerate/1449753-vdsp_mvessqd)

|  | Declaration |
| --- | --- |
| From | void vDSP_mvessqD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_mvessqD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_nzcros()](https://developer.apple.com/documentation/accelerate/1450629-vdsp_nzcros)

|  | Declaration |
| --- | --- |
| From | void vDSP_nzcros ( float \*__vDSP_A, vDSP_Stride __vDSP_I, vDSP_Length __vDSP_B, vDSP_Length \*__vDSP_C, vDSP_Length \*__vDSP_D, vDSP_Length __vDSP_N); |
| To | void vDSP_nzcros ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Length __vDSP_B, vDSP_Length \*__vDSP_C, vDSP_Length \*__vDSP_D, vDSP_Length __vDSP_N); |

Modified [vDSP_nzcrosD()](https://developer.apple.com/documentation/accelerate/1450715-vdsp_nzcrosd)

|  | Declaration |
| --- | --- |
| From | void vDSP_nzcrosD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, vDSP_Length __vDSP_B, vDSP_Length \*__vDSP_C, vDSP_Length \*__vDSP_D, vDSP_Length __vDSP_N); |
| To | void vDSP_nzcrosD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Length __vDSP_B, vDSP_Length \*__vDSP_C, vDSP_Length \*__vDSP_D, vDSP_Length __vDSP_N); |

Modified [vDSP_polar()](https://developer.apple.com/documentation/accelerate/1450489-vdsp_polar)

|  | Declaration |
| --- | --- |
| From | void vDSP_polar ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_polar ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_polarD()](https://developer.apple.com/documentation/accelerate/1450540-vdsp_polard)

|  | Declaration |
| --- | --- |
| From | void vDSP_polarD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_polarD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_rect()](https://developer.apple.com/documentation/accelerate/1450416-vdsp_rect)

|  | Declaration |
| --- | --- |
| From | void vDSP_rect ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_rect ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_rectD()](https://developer.apple.com/documentation/accelerate/1450754-vdsp_rectd)

|  | Declaration |
| --- | --- |
| From | void vDSP_rectD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_rectD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_rmsqv()](https://developer.apple.com/documentation/accelerate/1450655-vdsp_rmsqv)

|  | Declaration |
| --- | --- |
| From | void vDSP_rmsqv ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_rmsqv ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_rmsqvD()](https://developer.apple.com/documentation/accelerate/1449917-vdsp_rmsqvd)

|  | Declaration |
| --- | --- |
| From | void vDSP_rmsqvD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_rmsqvD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_svdiv()](https://developer.apple.com/documentation/accelerate/1450412-vdsp_svdiv)

|  | Declaration |
| --- | --- |
| From | void vDSP_svdiv ( float \*__vDSP_A, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_svdiv ( const float \*__vDSP_A, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_svdivD()](https://developer.apple.com/documentation/accelerate/1450028-vdsp_svdivd)

|  | Declaration |
| --- | --- |
| From | void vDSP_svdivD ( double \*__vDSP_A, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_svdivD ( const double \*__vDSP_A, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_sve()](https://developer.apple.com/documentation/kernel/1579937-vdsp_sve)

|  | Declaration |
| --- | --- |
| From | void vDSP_sve ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_sve ( const float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_sveD()](https://developer.apple.com/documentation/accelerate/1450567-vdsp_sved)

|  | Declaration |
| --- | --- |
| From | void vDSP_sveD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_sveD ( const double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_sve_svesq()](https://developer.apple.com/documentation/kernel/1579989-vdsp_sve_svesq)

|  | Declaration |
| --- | --- |
| From | void vDSP_sve_svesq ( const float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_Sum, float \*__vDSP_SumOfSquares, vDSP_Length __vDSP_N); |
| To | void vDSP_sve_svesq ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_Sum, float \*__vDSP_SumOfSquares, vDSP_Length __vDSP_N); |

Modified [vDSP_sve_svesqD()](https://developer.apple.com/documentation/accelerate/1450682-vdsp_sve_svesqd)

|  | Declaration |
| --- | --- |
| From | void vDSP_sve_svesqD ( const double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_Sum, double \*__vDSP_SumOfSquares, vDSP_Length __vDSP_N); |
| To | void vDSP_sve_svesqD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_Sum, double \*__vDSP_SumOfSquares, vDSP_Length __vDSP_N); |

Modified [vDSP_svemg()](https://developer.apple.com/documentation/accelerate/1450055-vdsp_svemg)

|  | Declaration |
| --- | --- |
| From | void vDSP_svemg ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_svemg ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_svemgD()](https://developer.apple.com/documentation/accelerate/1450856-vdsp_svemgd)

|  | Declaration |
| --- | --- |
| From | void vDSP_svemgD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_svemgD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_svesq()](https://developer.apple.com/documentation/accelerate/1450392-vdsp_svesq)

|  | Declaration |
| --- | --- |
| From | void vDSP_svesq ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_svesq ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_svesqD()](https://developer.apple.com/documentation/accelerate/1450012-vdsp_svesqd)

|  | Declaration |
| --- | --- |
| From | void vDSP_svesqD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_svesqD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_svs()](https://developer.apple.com/documentation/kernel/1532174-vdsp_svs)

|  | Declaration |
| --- | --- |
| From | void vDSP_svs ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_svs ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_svsD()](https://developer.apple.com/documentation/accelerate/1450862-vdsp_svsd)

|  | Declaration |
| --- | --- |
| From | void vDSP_svsD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_svsD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_vaam()](https://developer.apple.com/documentation/accelerate/1450588-vdsp_vaam)

|  | Declaration |
| --- | --- |
| From | void vDSP_vaam ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, float \*__vDSP_D, vDSP_Stride __vDSP_L, float \*__vDSP_E, vDSP_Stride __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_vaam ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, vDSP_Stride __vDSP_IC, const float \*__vDSP_D, vDSP_Stride __vDSP_ID, float \*__vDSP_E, vDSP_Stride __vDSP_IE, vDSP_Length __vDSP_N); |

Modified [vDSP_vaamD()](https://developer.apple.com/documentation/accelerate/1450148-vdsp_vaamd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vaamD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, double \*__vDSP_D, vDSP_Stride __vDSP_L, double \*__vDSP_E, vDSP_Stride __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_vaamD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, vDSP_Stride __vDSP_IC, const double \*__vDSP_D, vDSP_Stride __vDSP_ID, double \*__vDSP_E, vDSP_Stride __vDSP_IE, vDSP_Length __vDSP_N); |

Modified [vDSP_vabs()](https://developer.apple.com/documentation/kernel/1532216-vdsp_vabs)

|  | Declaration |
| --- | --- |
| From | void vDSP_vabs ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vabs ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vabsD()](https://developer.apple.com/documentation/accelerate/1449982-vdsp_vabsd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vabsD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vabsD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vabsi()](https://developer.apple.com/documentation/accelerate/1449929-vdsp_vabsi)

|  | Declaration |
| --- | --- |
| From | void vDSP_vabsi ( int \*__vDSP_A, vDSP_Stride __vDSP_I, int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vabsi ( const int \*__vDSP_A, vDSP_Stride __vDSP_IA, int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vadd()](https://developer.apple.com/documentation/kernel/1532191-vdsp_vadd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vadd ( const float __vDSP_input1[], vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, float __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vadd ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vaddD()](https://developer.apple.com/documentation/accelerate/1449910-vdsp_vaddd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vaddD ( const double __vDSP_input1[], vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, double __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vaddD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vam()](https://developer.apple.com/documentation/accelerate/1450561-vdsp_vam)

|  | Declaration |
| --- | --- |
| From | void vDSP_vam ( const float __vDSP_input1[], vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, const float __vDSP_input3[], vDSP_Stride __vDSP_stride3, float __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vam ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, vDSP_Stride __vDSP_IC, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vamD()](https://developer.apple.com/documentation/accelerate/1450382-vdsp_vamd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vamD ( const double __vDSP_input1[], vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, const double __vDSP_input3[], vDSP_Stride __vDSP_stride3, double __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vamD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, vDSP_Stride __vDSP_IC, double \*__vDSP_D, vDSP_Stride __vDSP_IDD, vDSP_Length __vDSP_N); |

Modified [vDSP_vasbm()](https://developer.apple.com/documentation/accelerate/1450277-vdsp_vasbm)

|  | Declaration |
| --- | --- |
| From | void vDSP_vasbm ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, float \*__vDSP_D, vDSP_Stride __vDSP_L, float \*__vDSP_E, vDSP_Stride __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_vasbm ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, vDSP_Stride __vDSP_IC, const float \*__vDSP_D, vDSP_Stride __vDSP_ID, float \*__vDSP_E, vDSP_Stride __vDSP_IE, vDSP_Length __vDSP_N); |

Modified [vDSP_vasbmD()](https://developer.apple.com/documentation/accelerate/1449885-vdsp_vasbmd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vasbmD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, double \*__vDSP_D, vDSP_Stride __vDSP_L, double \*__vDSP_E, vDSP_Stride __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_vasbmD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, vDSP_Stride __vDSP_IC, const double \*__vDSP_D, vDSP_Stride __vDSP_ID, double \*__vDSP_E, vDSP_Stride __vDSP_IE, vDSP_Length __vDSP_N); |

Modified [vDSP_vasm()](https://developer.apple.com/documentation/accelerate/1449773-vdsp_vasm)

|  | Declaration |
| --- | --- |
| From | void vDSP_vasm ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vasm ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vasmD()](https://developer.apple.com/documentation/accelerate/1450146-vdsp_vasmd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vasmD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vasmD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vavlin()](https://developer.apple.com/documentation/accelerate/1449668-vdsp_vavlin)

|  | Declaration |
| --- | --- |
| From | void vDSP_vavlin ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vavlin ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vavlinD()](https://developer.apple.com/documentation/accelerate/1450158-vdsp_vavlind)

|  | Declaration |
| --- | --- |
| From | void vDSP_vavlinD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vavlinD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vclip()](https://developer.apple.com/documentation/accelerate/1450071-vdsp_vclip)

|  | Declaration |
| --- | --- |
| From | void vDSP_vclip ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vclip ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, const float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vclipD()](https://developer.apple.com/documentation/accelerate/1450285-vdsp_vclipd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vclipD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vclipD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, const double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vclipc()](https://developer.apple.com/documentation/accelerate/1450775-vdsp_vclipc)

|  | Declaration |
| --- | --- |
| From | void vDSP_vclipc ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N, vDSP_Length \*__vDSP_NLOW, vDSP_Length \*__vDSP_NHI); |
| To | void vDSP_vclipc ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, const float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N, vDSP_Length \*__vDSP_NLow, vDSP_Length \*__vDSP_NHigh); |

Modified [vDSP_vclipcD()](https://developer.apple.com/documentation/accelerate/1450162-vdsp_vclipcd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vclipcD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N, vDSP_Length \*__vDSP_NLOW, vDSP_Length \*__vDSP_NHI); |
| To | void vDSP_vclipcD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, const double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N, vDSP_Length \*__vDSP_NLow, vDSP_Length \*__vDSP_NHigh); |

Modified [vDSP_vclr()](https://developer.apple.com/documentation/accelerate/1450402-vdsp_vclr)

|  | Declaration |
| --- | --- |
| From | void vDSP_vclr ( float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vclr ( float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vclrD()](https://developer.apple.com/documentation/accelerate/1450639-vdsp_vclrd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vclrD ( double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vclrD ( double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vcmprs()](https://developer.apple.com/documentation/accelerate/1450286-vdsp_vcmprs)

|  | Declaration |
| --- | --- |
| From | void vDSP_vcmprs ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vcmprs ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vcmprsD()](https://developer.apple.com/documentation/accelerate/1449861-vdsp_vcmprsd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vcmprsD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vcmprsD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vdbcon()](https://developer.apple.com/documentation/accelerate/1450241-vdsp_vdbcon)

|  | Declaration |
| --- | --- |
| From | void vDSP_vdbcon ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N, unsigned int __vDSP_F); |
| To | void vDSP_vdbcon ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, unsigned int __vDSP_F); |

Modified [vDSP_vdbconD()](https://developer.apple.com/documentation/accelerate/1449896-vdsp_vdbcond)

|  | Declaration |
| --- | --- |
| From | void vDSP_vdbconD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N, unsigned int __vDSP_F); |
| To | void vDSP_vdbconD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, unsigned int __vDSP_F); |

Modified [vDSP_vdist()](https://developer.apple.com/documentation/accelerate/1450257-vdsp_vdist)

|  | Declaration |
| --- | --- |
| From | void vDSP_vdist ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vdist ( const float \*__vDSP_A, vDSP_Stride __vDSP_I, const float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |

Modified [vDSP_vdistD()](https://developer.apple.com/documentation/accelerate/1449966-vdsp_vdistd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vdistD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vdistD ( const double \*__vDSP_A, vDSP_Stride __vDSP_I, const double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |

Modified [vDSP_vdiv()](https://developer.apple.com/documentation/accelerate/1450243-vdsp_vdiv)

|  | Declaration |
| --- | --- |
| From | void vDSP_vdiv ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vdiv ( const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vdivD()](https://developer.apple.com/documentation/accelerate/1450126-vdsp_vdivd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vdivD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vdivD ( const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vdivi()](https://developer.apple.com/documentation/accelerate/1450839-vdsp_vdivi)

|  | Declaration |
| --- | --- |
| From | void vDSP_vdivi ( int \*__vDSP_A, vDSP_Stride __vDSP_I, int \*__vDSP_B, vDSP_Stride __vDSP_J, int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vdivi ( const int \*__vDSP_B, vDSP_Stride __vDSP_IB, const int \*__vDSP_A, vDSP_Stride __vDSP_IA, int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vdpsp()](https://developer.apple.com/documentation/accelerate/1450729-vdsp_vdpsp)

|  | Declaration |
| --- | --- |
| From | void vDSP_vdpsp ( double \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vdpsp ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_venvlp()](https://developer.apple.com/documentation/accelerate/1449964-vdsp_venvlp)

|  | Declaration |
| --- | --- |
| From | void vDSP_venvlp ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_venvlp ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, vDSP_Stride __vDSP_IC, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_venvlpD()](https://developer.apple.com/documentation/accelerate/1449687-vdsp_venvlpd)

|  | Declaration |
| --- | --- |
| From | void vDSP_venvlpD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_venvlpD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, vDSP_Stride __vDSP_IC, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_veqvi()](https://developer.apple.com/documentation/accelerate/1450585-vdsp_veqvi)

|  | Declaration |
| --- | --- |
| From | void vDSP_veqvi ( int \*__vDSP_A, vDSP_Stride __vDSP_I, int \*__vDSP_B, vDSP_Stride __vDSP_J, int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_veqvi ( const int \*__vDSP_A, vDSP_Stride __vDSP_IA, const int \*__vDSP_B, vDSP_Stride __vDSP_IB, int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfill()](https://developer.apple.com/documentation/kernel/1579967-vdsp_vfill)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfill ( float \*__vDSP_A, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfill ( const float \*__vDSP_A, float \*__vDSP_C, vDSP_Stride __vDSP_IA, vDSP_Length __vDSP_N); |

Modified [vDSP_vfillD()](https://developer.apple.com/documentation/accelerate/1450171-vdsp_vfilld)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfillD ( double \*__vDSP_A, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfillD ( const double \*__vDSP_A, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfilli()](https://developer.apple.com/documentation/accelerate/1450473-vdsp_vfilli)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfilli ( int \*__vDSP_A, int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfilli ( const int \*__vDSP_A, int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfix16()](https://developer.apple.com/documentation/accelerate/1449992-vdsp_vfix16)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfix16 ( float \*__vDSP_A, vDSP_Stride __vDSP_I, short \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfix16 ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, short \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfix16D()](https://developer.apple.com/documentation/accelerate/1450469-vdsp_vfix16d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfix16D ( double \*__vDSP_A, vDSP_Stride __vDSP_I, short \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfix16D ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, short \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfix32()](https://developer.apple.com/documentation/accelerate/1449976-vdsp_vfix32)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfix32 ( float \*__vDSP_A, vDSP_Stride __vDSP_I, int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfix32 ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfix32D()](https://developer.apple.com/documentation/accelerate/1450167-vdsp_vfix32d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfix32D ( double \*__vDSP_A, vDSP_Stride __vDSP_I, int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfix32D ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfix8()](https://developer.apple.com/documentation/accelerate/1450548-vdsp_vfix8)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfix8 ( float \*__vDSP_A, vDSP_Stride __vDSP_I, char \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfix8 ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, char \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfix8D()](https://developer.apple.com/documentation/accelerate/1450864-vdsp_vfix8d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfix8D ( double \*__vDSP_A, vDSP_Stride __vDSP_I, char \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfix8D ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, char \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixr16()](https://developer.apple.com/documentation/accelerate/1449925-vdsp_vfixr16)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixr16 ( float \*__vDSP_A, vDSP_Stride __vDSP_I, short \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixr16 ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, short \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixr16D()](https://developer.apple.com/documentation/accelerate/1450475-vdsp_vfixr16d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixr16D ( double \*__vDSP_A, vDSP_Stride __vDSP_I, short \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixr16D ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, short \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixr32()](https://developer.apple.com/documentation/accelerate/1450794-vdsp_vfixr32)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixr32 ( float \*__vDSP_A, vDSP_Stride __vDSP_I, int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixr32 ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixr32D()](https://developer.apple.com/documentation/accelerate/1450765-vdsp_vfixr32d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixr32D ( double \*__vDSP_A, vDSP_Stride __vDSP_I, int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixr32D ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixr8()](https://developer.apple.com/documentation/accelerate/1450408-vdsp_vfixr8)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixr8 ( float \*__vDSP_A, vDSP_Stride __vDSP_I, char \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixr8 ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, char \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixr8D()](https://developer.apple.com/documentation/accelerate/1449927-vdsp_vfixr8d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixr8D ( double \*__vDSP_A, vDSP_Stride __vDSP_I, char \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixr8D ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, char \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixru16()](https://developer.apple.com/documentation/accelerate/1450599-vdsp_vfixru16)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixru16 ( float \*__vDSP_A, vDSP_Stride __vDSP_I, unsigned short \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixru16 ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, unsigned short \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixru16D()](https://developer.apple.com/documentation/accelerate/1450082-vdsp_vfixru16d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixru16D ( double \*__vDSP_A, vDSP_Stride __vDSP_I, unsigned short \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixru16D ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, unsigned short \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixru32()](https://developer.apple.com/documentation/accelerate/1449735-vdsp_vfixru32)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixru32 ( float \*__vDSP_A, vDSP_Stride __vDSP_I, unsigned int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixru32 ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, unsigned int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixru32D()](https://developer.apple.com/documentation/accelerate/1450065-vdsp_vfixru32d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixru32D ( double \*__vDSP_A, vDSP_Stride __vDSP_I, unsigned int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixru32D ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, unsigned int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixru8()](https://developer.apple.com/documentation/accelerate/1449777-vdsp_vfixru8)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixru8 ( float \*__vDSP_A, vDSP_Stride __vDSP_I, unsigned char \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixru8 ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, unsigned char \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixru8D()](https://developer.apple.com/documentation/accelerate/1449847-vdsp_vfixru8d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixru8D ( double \*__vDSP_A, vDSP_Stride __vDSP_I, unsigned char \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixru8D ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, unsigned char \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixu16()](https://developer.apple.com/documentation/accelerate/1449834-vdsp_vfixu16)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixu16 ( float \*__vDSP_A, vDSP_Stride __vDSP_I, unsigned short \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixu16 ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, unsigned short \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixu16D()](https://developer.apple.com/documentation/accelerate/1449908-vdsp_vfixu16d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixu16D ( double \*__vDSP_A, vDSP_Stride __vDSP_I, unsigned short \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixu16D ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, unsigned short \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixu32()](https://developer.apple.com/documentation/accelerate/1450173-vdsp_vfixu32)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixu32 ( float \*__vDSP_A, vDSP_Stride __vDSP_I, unsigned int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixu32 ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, unsigned int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixu32D()](https://developer.apple.com/documentation/accelerate/1450846-vdsp_vfixu32d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixu32D ( double \*__vDSP_A, vDSP_Stride __vDSP_I, unsigned int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixu32D ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, unsigned int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixu8()](https://developer.apple.com/documentation/accelerate/1450800-vdsp_vfixu8)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixu8 ( float \*__vDSP_A, vDSP_Stride __vDSP_I, unsigned char \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixu8 ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, unsigned char \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixu8D()](https://developer.apple.com/documentation/accelerate/1450868-vdsp_vfixu8d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixu8D ( double \*__vDSP_A, vDSP_Stride __vDSP_I, unsigned char \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixu8D ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, unsigned char \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vflt16()](https://developer.apple.com/documentation/accelerate/1450096-vdsp_vflt16)

|  | Declaration |
| --- | --- |
| From | void vDSP_vflt16 ( short \*A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vflt16 ( const short \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vflt16D()](https://developer.apple.com/documentation/accelerate/1450208-vdsp_vflt16d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vflt16D ( short \*A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vflt16D ( const short \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vflt32()](https://developer.apple.com/documentation/kernel/1532181-vdsp_vflt32)

|  | Declaration |
| --- | --- |
| From | void vDSP_vflt32 ( int \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vflt32 ( const int \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vflt32D()](https://developer.apple.com/documentation/accelerate/1450342-vdsp_vflt32d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vflt32D ( int \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vflt32D ( const int \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vflt8()](https://developer.apple.com/documentation/accelerate/1450742-vdsp_vflt8)

|  | Declaration |
| --- | --- |
| From | void vDSP_vflt8 ( char \*A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vflt8 ( const char \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vflt8D()](https://developer.apple.com/documentation/accelerate/1449894-vdsp_vflt8d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vflt8D ( char \*A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vflt8D ( const char \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfltu16()](https://developer.apple.com/documentation/accelerate/1450118-vdsp_vfltu16)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfltu16 ( unsigned short \*A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfltu16 ( const unsigned short \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfltu16D()](https://developer.apple.com/documentation/accelerate/1450769-vdsp_vfltu16d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfltu16D ( unsigned short \*A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfltu16D ( const unsigned short \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfltu32()](https://developer.apple.com/documentation/accelerate/1450255-vdsp_vfltu32)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfltu32 ( unsigned int \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfltu32 ( const unsigned int \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfltu32D()](https://developer.apple.com/documentation/accelerate/1449794-vdsp_vfltu32d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfltu32D ( unsigned int \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfltu32D ( const unsigned int \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfltu8()](https://developer.apple.com/documentation/accelerate/1450549-vdsp_vfltu8)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfltu8 ( unsigned char \*A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfltu8 ( const unsigned char \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfltu8D()](https://developer.apple.com/documentation/accelerate/1450104-vdsp_vfltu8d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfltu8D ( unsigned char \*A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfltu8D ( const unsigned char \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfrac()](https://developer.apple.com/documentation/accelerate/1450336-vdsp_vfrac)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfrac ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfrac ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfracD()](https://developer.apple.com/documentation/accelerate/1449948-vdsp_vfracd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfracD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfracD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vgathr()](https://developer.apple.com/documentation/accelerate/1449749-vdsp_vgathr)

|  | Declaration |
| --- | --- |
| From | void vDSP_vgathr ( float \*__vDSP_A, vDSP_Length \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vgathr ( const float \*__vDSP_A, const vDSP_Length \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vgathrD()](https://developer.apple.com/documentation/accelerate/1449921-vdsp_vgathrd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vgathrD ( double \*__vDSP_A, vDSP_Length \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vgathrD ( const double \*__vDSP_A, const vDSP_Length \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vgathra()](https://developer.apple.com/documentation/accelerate/1450261-vdsp_vgathra)

|  | Declaration |
| --- | --- |
| From | void vDSP_vgathra ( float \*\*A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vgathra ( const float \*\*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vgathraD()](https://developer.apple.com/documentation/accelerate/1449865-vdsp_vgathrad)

|  | Declaration |
| --- | --- |
| From | void vDSP_vgathraD ( double \*\*A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vgathraD ( const double \*\*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vgen()](https://developer.apple.com/documentation/accelerate/1449703-vdsp_vgen)

|  | Declaration |
| --- | --- |
| From | void vDSP_vgen ( float \*__vDSP_A, float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vgen ( const float \*__vDSP_A, const float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vgenD()](https://developer.apple.com/documentation/accelerate/1450583-vdsp_vgend)

|  | Declaration |
| --- | --- |
| From | void vDSP_vgenD ( double \*__vDSP_A, double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vgenD ( const double \*__vDSP_A, const double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vgenp()](https://developer.apple.com/documentation/accelerate/1449771-vdsp_vgenp)

|  | Declaration |
| --- | --- |
| From | void vDSP_vgenp ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |
| To | void vDSP_vgenp ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |

Modified [vDSP_vgenpD()](https://developer.apple.com/documentation/accelerate/1450645-vdsp_vgenpd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vgenpD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |
| To | void vDSP_vgenpD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |

Modified [vDSP_viclip()](https://developer.apple.com/documentation/accelerate/1450512-vdsp_viclip)

|  | Declaration |
| --- | --- |
| From | void vDSP_viclip ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_viclip ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, const float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_viclipD()](https://developer.apple.com/documentation/accelerate/1450559-vdsp_viclipd)

|  | Declaration |
| --- | --- |
| From | void vDSP_viclipD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_viclipD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, const double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vindex()](https://developer.apple.com/documentation/accelerate/1449792-vdsp_vindex)

|  | Declaration |
| --- | --- |
| From | void vDSP_vindex ( float \*__vDSP_A, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vindex ( const float \*__vDSP_A, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vindexD()](https://developer.apple.com/documentation/accelerate/1449958-vdsp_vindexd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vindexD ( double \*__vDSP_A, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vindexD ( const double \*__vDSP_A, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vintb()](https://developer.apple.com/documentation/accelerate/1449705-vdsp_vintb)

|  | Declaration |
| --- | --- |
| From | void vDSP_vintb ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vintb ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vintbD()](https://developer.apple.com/documentation/accelerate/1449968-vdsp_vintbd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vintbD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vintbD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vlim()](https://developer.apple.com/documentation/accelerate/1450525-vdsp_vlim)

|  | Declaration |
| --- | --- |
| From | void vDSP_vlim ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vlim ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, const float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vlimD()](https://developer.apple.com/documentation/accelerate/1450709-vdsp_vlimd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vlimD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vlimD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, const double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vlint()](https://developer.apple.com/documentation/accelerate/1449775-vdsp_vlint)

|  | Declaration |
| --- | --- |
| From | void vDSP_vlint ( float \*__vDSP_A, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |
| To | void vDSP_vlint ( const float \*__vDSP_A, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |

Modified [vDSP_vlintD()](https://developer.apple.com/documentation/accelerate/1449733-vdsp_vlintd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vlintD ( double \*__vDSP_A, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |
| To | void vDSP_vlintD ( const double \*__vDSP_A, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |

Modified [vDSP_vma()](https://developer.apple.com/documentation/kernel/1532193-vdsp_vma)

|  | Declaration |
| --- | --- |
| From | void vDSP_vma ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vma ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, vDSP_Stride __vDSP_IC, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vmaD()](https://developer.apple.com/documentation/accelerate/1450825-vdsp_vmad)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmaD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vmaD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, vDSP_Stride __vDSP_IC, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vmax()](https://developer.apple.com/documentation/kernel/1579953-vdsp_vmax)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmax ( const float \*__vDSP_A, vDSP_Stride __vDSP_I, const float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vmax ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vmaxD()](https://developer.apple.com/documentation/accelerate/1449938-vdsp_vmaxd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmaxD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vmaxD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vmaxmg()](https://developer.apple.com/documentation/accelerate/1450295-vdsp_vmaxmg)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmaxmg ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vmaxmg ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vmaxmgD()](https://developer.apple.com/documentation/accelerate/1449767-vdsp_vmaxmgd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmaxmgD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vmaxmgD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vmin()](https://developer.apple.com/documentation/accelerate/1450216-vdsp_vmin)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmin ( const float \*__vDSP_A, vDSP_Stride __vDSP_I, const float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vmin ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vminD()](https://developer.apple.com/documentation/accelerate/1450601-vdsp_vmind)

|  | Declaration |
| --- | --- |
| From | void vDSP_vminD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vminD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vminmg()](https://developer.apple.com/documentation/accelerate/1450293-vdsp_vminmg)

|  | Declaration |
| --- | --- |
| From | void vDSP_vminmg ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vminmg ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vminmgD()](https://developer.apple.com/documentation/accelerate/1449680-vdsp_vminmgd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vminmgD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vminmgD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vmma()](https://developer.apple.com/documentation/accelerate/1450802-vdsp_vmma)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmma ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, float \*__vDSP_D, vDSP_Stride __vDSP_L, float \*__vDSP_E, vDSP_Stride __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_vmma ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, vDSP_Stride __vDSP_IC, const float \*__vDSP_D, vDSP_Stride __vDSP_ID, float \*__vDSP_E, vDSP_Stride __vDSP_IE, vDSP_Length __vDSP_N); |

Modified [vDSP_vmmaD()](https://developer.apple.com/documentation/accelerate/1450527-vdsp_vmmad)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmmaD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, double \*__vDSP_D, vDSP_Stride __vDSP_L, double \*__vDSP_E, vDSP_Stride __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_vmmaD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, vDSP_Stride __vDSP_IC, const double \*__vDSP_D, vDSP_Stride __vDSP_ID, double \*__vDSP_E, vDSP_Stride __vDSP_IE, vDSP_Length __vDSP_N); |

Modified [vDSP_vmmsb()](https://developer.apple.com/documentation/accelerate/1450613-vdsp_vmmsb)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmmsb ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, float \*__vDSP_D, vDSP_Stride __vDSP_L, float \*__vDSP_E, vDSP_Stride __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_vmmsb ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, vDSP_Stride __vDSP_IC, const float \*__vDSP_D, vDSP_Stride __vDSP_ID, float \*__vDSP_E, vDSP_Stride __vDSP_IE, vDSP_Length __vDSP_N); |

Modified [vDSP_vmmsbD()](https://developer.apple.com/documentation/accelerate/1450418-vdsp_vmmsbd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmmsbD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, double \*__vDSP_D, vDSP_Stride __vDSP_L, double \*__vDSP_E, vDSP_Stride __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_vmmsbD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, vDSP_Stride __vDSP_IC, const double \*__vDSP_D, vDSP_Stride __vDSP_ID, double \*__vDSP_E, vDSP_Stride __vDSP_IE, vDSP_Length __vDSP_N); |

Modified [vDSP_vmsa()](https://developer.apple.com/documentation/accelerate/1450590-vdsp_vmsa)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmsa ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vmsa ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vmsaD()](https://developer.apple.com/documentation/accelerate/1450698-vdsp_vmsad)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmsaD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vmsaD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vmsb()](https://developer.apple.com/documentation/accelerate/1450451-vdsp_vmsb)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmsb ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vmsb ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, vDSP_Stride __vDSP_IC, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vmsbD()](https://developer.apple.com/documentation/accelerate/1450609-vdsp_vmsbd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmsbD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vmsbD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, vDSP_Stride __vDSP_IC, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vmul()](https://developer.apple.com/documentation/accelerate/1450344-vdsp_vmul)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmul ( const float __vDSP_input1[], vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, float __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vmul ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vmulD()](https://developer.apple.com/documentation/accelerate/1450138-vdsp_vmuld)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmulD ( const double __vDSP_input1[], vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, double __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vmulD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vnabs()](https://developer.apple.com/documentation/accelerate/1450420-vdsp_vnabs)

|  | Declaration |
| --- | --- |
| From | void vDSP_vnabs ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vnabs ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vnabsD()](https://developer.apple.com/documentation/accelerate/1450259-vdsp_vnabsd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vnabsD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vnabsD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vneg()](https://developer.apple.com/documentation/accelerate/1450204-vdsp_vneg)

|  | Declaration |
| --- | --- |
| From | void vDSP_vneg ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vneg ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vnegD()](https://developer.apple.com/documentation/accelerate/1450346-vdsp_vnegd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vnegD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vnegD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vpoly()](https://developer.apple.com/documentation/accelerate/1450623-vdsp_vpoly)

|  | Declaration |
| --- | --- |
| From | void vDSP_vpoly ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_vpoly ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_vpolyD()](https://developer.apple.com/documentation/accelerate/1450503-vdsp_vpolyd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vpolyD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_vpolyD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_vpythg()](https://developer.apple.com/documentation/accelerate/1450824-vdsp_vpythg)

|  | Declaration |
| --- | --- |
| From | void vDSP_vpythg ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, float \*__vDSP_D, vDSP_Stride __vDSP_L, float \*__vDSP_E, vDSP_Stride __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_vpythg ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, vDSP_Stride __vDSP_IC, const float \*__vDSP_D, vDSP_Stride __vDSP_ID, float \*__vDSP_E, vDSP_Stride __vDSP_IE, vDSP_Length __vDSP_N); |

Modified [vDSP_vpythgD()](https://developer.apple.com/documentation/accelerate/1449766-vdsp_vpythgd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vpythgD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, double \*__vDSP_D, vDSP_Stride __vDSP_L, double \*__vDSP_E, vDSP_Stride __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_vpythgD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, vDSP_Stride __vDSP_IC, const double \*__vDSP_D, vDSP_Stride __vDSP_ID, double \*__vDSP_E, vDSP_Stride __vDSP_IE, vDSP_Length __vDSP_N); |

Modified [vDSP_vqint()](https://developer.apple.com/documentation/accelerate/1449942-vdsp_vqint)

|  | Declaration |
| --- | --- |
| From | void vDSP_vqint ( float \*__vDSP_A, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |
| To | void vDSP_vqint ( const float \*__vDSP_A, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |

Modified [vDSP_vqintD()](https://developer.apple.com/documentation/accelerate/1450491-vdsp_vqintd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vqintD ( double \*__vDSP_A, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |
| To | void vDSP_vqintD ( const double \*__vDSP_A, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |

Modified [vDSP_vramp()](https://developer.apple.com/documentation/accelerate/1450369-vdsp_vramp)

|  | Declaration |
| --- | --- |
| From | void vDSP_vramp ( float \*__vDSP_A, float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vramp ( const float \*__vDSP_A, const float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vrampD()](https://developer.apple.com/documentation/accelerate/1449999-vdsp_vrampd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vrampD ( double \*__vDSP_A, double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vrampD ( const double \*__vDSP_A, const double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vrsum()](https://developer.apple.com/documentation/accelerate/1450245-vdsp_vrsum)

|  | Declaration |
| --- | --- |
| From | void vDSP_vrsum ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_S, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vrsum ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_S, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vrsumD()](https://developer.apple.com/documentation/accelerate/1450713-vdsp_vrsumd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vrsumD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_S, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vrsumD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_S, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vrvrs()](https://developer.apple.com/documentation/accelerate/1450290-vdsp_vrvrs)

|  | Declaration |
| --- | --- |
| From | void vDSP_vrvrs ( float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vrvrs ( float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vrvrsD()](https://developer.apple.com/documentation/accelerate/1449825-vdsp_vrvrsd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vrvrsD ( double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vrvrsD ( double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsadd()](https://developer.apple.com/documentation/kernel/1579993-vdsp_vsadd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsadd ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vsadd ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsaddD()](https://developer.apple.com/documentation/accelerate/1450860-vdsp_vsaddd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsaddD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vsaddD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsaddi()](https://developer.apple.com/documentation/accelerate/1450088-vdsp_vsaddi)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsaddi ( int \*__vDSP_A, vDSP_Stride __vDSP_I, int \*__vDSP_B, int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vsaddi ( const int \*__vDSP_A, vDSP_Stride __vDSP_IA, const int \*__vDSP_B, int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsbm()](https://developer.apple.com/documentation/accelerate/1449914-vdsp_vsbm)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsbm ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vsbm ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, vDSP_Stride __vDSP_IC, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vsbmD()](https://developer.apple.com/documentation/accelerate/1450334-vdsp_vsbmd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsbmD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vsbmD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, vDSP_Stride __vDSP_IC, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vsbsbm()](https://developer.apple.com/documentation/accelerate/1449761-vdsp_vsbsbm)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsbsbm ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, float \*__vDSP_D, vDSP_Stride __vDSP_L, float \*__vDSP_E, vDSP_Stride __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_vsbsbm ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, vDSP_Stride __vDSP_IC, const float \*__vDSP_D, vDSP_Stride __vDSP_ID, float \*__vDSP_E, vDSP_Stride __vDSP_IE, vDSP_Length __vDSP_N); |

Modified [vDSP_vsbsbmD()](https://developer.apple.com/documentation/accelerate/1449707-vdsp_vsbsbmd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsbsbmD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, double \*__vDSP_D, vDSP_Stride __vDSP_L, double \*__vDSP_E, vDSP_Stride __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_vsbsbmD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, vDSP_Stride __vDSP_IC, const double \*__vDSP_D, vDSP_Stride __vDSP_ID, double \*__vDSP_E, vDSP_Stride __vDSP_IE, vDSP_Length __vDSP_N); |

Modified [vDSP_vsbsm()](https://developer.apple.com/documentation/accelerate/1450734-vdsp_vsbsm)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsbsm ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vsbsm ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vsbsmD()](https://developer.apple.com/documentation/accelerate/1450372-vdsp_vsbsmd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsbsmD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vsbsmD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vsdiv()](https://developer.apple.com/documentation/accelerate/1450680-vdsp_vsdiv)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsdiv ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vsdiv ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsdivD()](https://developer.apple.com/documentation/accelerate/1450212-vdsp_vsdivd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsdivD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vsdivD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsdivi()](https://developer.apple.com/documentation/accelerate/1449689-vdsp_vsdivi)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsdivi ( int \*__vDSP_A, vDSP_Stride __vDSP_I, int \*__vDSP_B, int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vsdivi ( const int \*__vDSP_A, vDSP_Stride __vDSP_IA, const int \*__vDSP_B, int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsimps()](https://developer.apple.com/documentation/accelerate/1450644-vdsp_vsimps)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsimps ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vsimps ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsimpsD()](https://developer.apple.com/documentation/accelerate/1450112-vdsp_vsimpsd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsimpsD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vsimpsD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsma()](https://developer.apple.com/documentation/accelerate/1450271-vdsp_vsma)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsma ( const float \*__vDSP_A, vDSP_Stride __vDSP_I, const float \*__vDSP_B, const float \*__vDSP_C, vDSP_Stride __vDSP_K, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vsma ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, const float \*__vDSP_C, vDSP_Stride __vDSP_IC, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vsmaD()](https://developer.apple.com/documentation/accelerate/1449759-vdsp_vsmad)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsmaD ( const double \*__vDSP_A, vDSP_Stride __vDSP_I, const double \*__vDSP_B, const double \*__vDSP_C, vDSP_Stride __vDSP_K, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vsmaD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, const double \*__vDSP_C, vDSP_Stride __vDSP_IC, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vsmsa()](https://developer.apple.com/documentation/accelerate/1450380-vdsp_vsmsa)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsmsa ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vsmsa ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, const float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vsmsaD()](https://developer.apple.com/documentation/accelerate/1450432-vdsp_vsmsad)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsmsaD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vsmsaD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, const double \*__vDSP_C, double \*__vDSP_ID, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |

Modified [vDSP_vsmsb()](https://developer.apple.com/documentation/accelerate/1450822-vdsp_vsmsb)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsmsb ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_K, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vsmsb ( const float \*__vDSP_A, vDSP_Stride __vDSP_I, const float \*__vDSP_B, const float \*__vDSP_C, vDSP_Stride __vDSP_K, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |

Modified [vDSP_vsmsbD()](https://developer.apple.com/documentation/accelerate/1450238-vdsp_vsmsbd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsmsbD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_K, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vsmsbD ( const double \*__vDSP_A, vDSP_Stride __vDSP_I, const double \*__vDSP_B, const double \*__vDSP_C, vDSP_Stride __vDSP_K, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |

Modified [vDSP_vsmsma()](https://developer.apple.com/documentation/accelerate/1450324-vdsp_vsmsma)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsmsma ( const float \*__vDSP_A, vDSP_Stride __vDSP_I, const float \*__vDSP_B, const float \*__vDSP_C, vDSP_Stride __vDSP_K, const float \*__vDSP_D, float \*__vDSP_E, vDSP_Stride __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_vsmsma ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, const float \*__vDSP_C, vDSP_Stride __vDSP_IC, const float \*__vDSP_D, float \*__vDSP_E, vDSP_Stride __vDSP_IE, vDSP_Length __vDSP_N); |

Modified [vDSP_vsmul()](https://developer.apple.com/documentation/kernel/1532223-vdsp_vsmul)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsmul ( const float __vDSP_input1[], vDSP_Stride __vDSP_stride1, const float \*__vDSP_input2, float __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vsmul ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsmulD()](https://developer.apple.com/documentation/accelerate/1449676-vdsp_vsmuld)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsmulD ( const double __vDSP_input1[], vDSP_Stride __vDSP_stride1, const double \*__vDSP_input2, double __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vsmulD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsort()](https://developer.apple.com/documentation/accelerate/1449747-vdsp_vsort)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsort ( float \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_OFLAG); |
| To | void vDSP_vsort ( float \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_Order); |

Modified [vDSP_vsortD()](https://developer.apple.com/documentation/accelerate/1450482-vdsp_vsortd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsortD ( double \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_OFLAG); |
| To | void vDSP_vsortD ( double \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_Order); |

Modified [vDSP_vsorti()](https://developer.apple.com/documentation/accelerate/1450736-vdsp_vsorti)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsorti ( float \*__vDSP_C, vDSP_Length \*__vDSP_IC, vDSP_Length \*__vDSP_List_addr, vDSP_Length __vDSP_N, int __vDSP_OFLAG); |
| To | void vDSP_vsorti ( const float \*__vDSP_C, vDSP_Length \*__vDSP_I, vDSP_Length \*__vDSP_Temporary, vDSP_Length __vDSP_N, int __vDSP_Order); |

Modified [vDSP_vsortiD()](https://developer.apple.com/documentation/accelerate/1450858-vdsp_vsortid)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsortiD ( double \*__vDSP_C, vDSP_Length \*__vDSP_IC, vDSP_Length \*__vDSP_List_addr, vDSP_Length __vDSP_N, int __vDSP_OFLAG); |
| To | void vDSP_vsortiD ( const double \*__vDSP_C, vDSP_Length \*__vDSP_I, vDSP_Length \*__vDSP_Temporary, vDSP_Length __vDSP_N, int __vDSP_Order); |

Modified [vDSP_vspdp()](https://developer.apple.com/documentation/accelerate/1450265-vdsp_vspdp)

|  | Declaration |
| --- | --- |
| From | void vDSP_vspdp ( float \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vspdp ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsq()](https://developer.apple.com/documentation/accelerate/1450611-vdsp_vsq)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsq ( const float __vDSP_input[], vDSP_Stride __vDSP_strideInput, float __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vsq ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsqD()](https://developer.apple.com/documentation/accelerate/1450841-vdsp_vsqd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsqD ( const double __vDSP_input[], vDSP_Stride __vDSP_strideInput, double __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vsqD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vssq()](https://developer.apple.com/documentation/accelerate/1450445-vdsp_vssq)

|  | Declaration |
| --- | --- |
| From | void vDSP_vssq ( const float __vDSP_input[], vDSP_Stride __vDSP_strideInput, float __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vssq ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vssqD()](https://developer.apple.com/documentation/accelerate/1450363-vdsp_vssqd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vssqD ( const double __vDSP_input[], vDSP_Stride __vDSP_strideInput, double __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vssqD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsub()](https://developer.apple.com/documentation/accelerate/1449900-vdsp_vsub)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsub ( const float __vDSP_input1[], vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, float __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vsub ( const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsubD()](https://developer.apple.com/documentation/accelerate/1449743-vdsp_vsubd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsubD ( const double __vDSP_input1[], vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, double __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vsubD ( const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vswap()](https://developer.apple.com/documentation/accelerate/1450661-vdsp_vswap)

|  | Declaration |
| --- | --- |
| From | void vDSP_vswap ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, vDSP_Length __vDSP_N); |
| To | void vDSP_vswap ( float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_B, vDSP_Stride __vDSP_IB, vDSP_Length __vDSP_N); |

Modified [vDSP_vswapD()](https://developer.apple.com/documentation/accelerate/1450555-vdsp_vswapd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vswapD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, vDSP_Length __vDSP_N); |
| To | void vDSP_vswapD ( double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_B, vDSP_Stride __vDSP_IB, vDSP_Length __vDSP_N); |

Modified [vDSP_vswsum()](https://developer.apple.com/documentation/accelerate/1449822-vdsp_vswsum)

|  | Declaration |
| --- | --- |
| From | void vDSP_vswsum ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_vswsum ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_vswsumD()](https://developer.apple.com/documentation/accelerate/1449693-vdsp_vswsumd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vswsumD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_vswsumD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_vtabi()](https://developer.apple.com/documentation/accelerate/1450762-vdsp_vtabi)

|  | Declaration |
| --- | --- |
| From | void vDSP_vtabi ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_S1, float \*__vDSP_S2, float \*__vDSP_C, vDSP_Length __vDSP_M, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vtabi ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_S1, const float \*__vDSP_S2, const float \*__vDSP_C, vDSP_Length __vDSP_M, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vtabiD()](https://developer.apple.com/documentation/accelerate/1449832-vdsp_vtabid)

|  | Declaration |
| --- | --- |
| From | void vDSP_vtabiD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_S1, double \*__vDSP_S2, double \*__vDSP_C, vDSP_Length __vDSP_M, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vtabiD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_S1, const double \*__vDSP_S2, const double \*__vDSP_C, vDSP_Length __vDSP_M, double \*__vDSP_ID, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |

Modified [vDSP_vthr()](https://developer.apple.com/documentation/accelerate/1450030-vdsp_vthr)

|  | Declaration |
| --- | --- |
| From | void vDSP_vthr ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vthr ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vthrD()](https://developer.apple.com/documentation/accelerate/1450834-vdsp_vthrd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vthrD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vthrD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vthres()](https://developer.apple.com/documentation/accelerate/1450597-vdsp_vthres)

|  | Declaration |
| --- | --- |
| From | void vDSP_vthres ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vthres ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vthresD()](https://developer.apple.com/documentation/accelerate/1450767-vdsp_vthresd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vthresD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vthresD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vthrsc()](https://developer.apple.com/documentation/accelerate/1450631-vdsp_vthrsc)

|  | Declaration |
| --- | --- |
| From | void vDSP_vthrsc ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vthrsc ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, const float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vthrscD()](https://developer.apple.com/documentation/accelerate/1450230-vdsp_vthrscd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vthrscD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vthrscD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, const double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vtmerg()](https://developer.apple.com/documentation/accelerate/1450140-vdsp_vtmerg)

|  | Declaration |
| --- | --- |
| From | void vDSP_vtmerg ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vtmerg ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vtmergD()](https://developer.apple.com/documentation/accelerate/1450175-vdsp_vtmergd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vtmergD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vtmergD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vtrapz()](https://developer.apple.com/documentation/accelerate/1450678-vdsp_vtrapz)

|  | Declaration |
| --- | --- |
| From | void vDSP_vtrapz ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vtrapz ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vtrapzD()](https://developer.apple.com/documentation/accelerate/1450810-vdsp_vtrapzd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vtrapzD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vtrapzD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_wiener()](https://developer.apple.com/documentation/accelerate/1450711-vdsp_wiener)

|  | Declaration |
| --- | --- |
| From | void vDSP_wiener ( vDSP_Length __vDSP_L, float \*__vDSP_A, float \*__vDSP_C, float \*__vDSP_F, float \*__vDSP_P, int __vDSP_IFLG, int \*__vDSP_IERR); |
| To | void vDSP_wiener ( vDSP_Length __vDSP_L, const float \*__vDSP_A, const float \*__vDSP_C, float \*__vDSP_F, float \*__vDSP_P, int __vDSP_Flag, int \*__vDSP_Error); |

Modified [vDSP_wienerD()](https://developer.apple.com/documentation/accelerate/1450592-vdsp_wienerd)

|  | Declaration |
| --- | --- |
| From | void vDSP_wienerD ( vDSP_Length __vDSP_L, double \*__vDSP_A, double \*__vDSP_C, double \*__vDSP_F, double \*__vDSP_P, int __vDSP_IFLG, int \*__vDSP_IERR); |
| To | void vDSP_wienerD ( vDSP_Length __vDSP_L, const double \*__vDSP_A, const double \*__vDSP_C, double \*__vDSP_F, double \*__vDSP_P, int __vDSP_Flag, int \*__vDSP_Error); |

Modified [vDSP_zaspec()](https://developer.apple.com/documentation/accelerate/1449691-vdsp_zaspec)

|  | Declaration |
| --- | --- |
| From | void vDSP_zaspec ( DSPSplitComplex \*__vDSP_A, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_zaspec ( const DSPSplitComplex \*__vDSP_A, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_zaspecD()](https://developer.apple.com/documentation/accelerate/1450746-vdsp_zaspecd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zaspecD ( DSPDoubleSplitComplex \*A, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_zaspecD ( const DSPDoubleSplitComplex \*__vDSP_A, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_zcoher()](https://developer.apple.com/documentation/accelerate/1450253-vdsp_zcoher)

|  | Declaration |
| --- | --- |
| From | void vDSP_zcoher ( float \*__vDSP_A, float \*__vDSP_B, DSPSplitComplex \*__vDSP_C, float \*__vDSP_D, vDSP_Length __vDSP_N); |
| To | void vDSP_zcoher ( const float \*__vDSP_A, const float \*__vDSP_B, const DSPSplitComplex \*__vDSP_C, float \*__vDSP_D, vDSP_Length __vDSP_N); |

Modified [vDSP_zcoherD()](https://developer.apple.com/documentation/accelerate/1450001-vdsp_zcoherd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zcoherD ( double \*__vDSP_A, double \*__vDSP_B, DSPDoubleSplitComplex \*__vDSP_C, double \*__vDSP_D, vDSP_Length __vDSP_N); |
| To | void vDSP_zcoherD ( const double \*__vDSP_A, const double \*__vDSP_B, const DSPDoubleSplitComplex \*__vDSP_C, double \*__vDSP_D, vDSP_Length __vDSP_N); |

Modified [vDSP_zconv()](https://developer.apple.com/documentation/accelerate/1450771-vdsp_zconv)

|  | Declaration |
| --- | --- |
| From | void vDSP_zconv ( DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPSplitComplex \*__vDSP_filter, vDSP_Stride __vDSP_strideFilter, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_lenResult, vDSP_Length __vDSP_lenFilter); |
| To | void vDSP_zconv ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_F, vDSP_Stride __vDSP_IF, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_zconvD()](https://developer.apple.com/documentation/accelerate/1450522-vdsp_zconvd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zconvD ( DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPDoubleSplitComplex \*__vDSP_filter, vDSP_Stride __vDSP_strideFilter, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_lenResult, vDSP_Length __vDSP_lenFilter); |
| To | void vDSP_zconvD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_F, vDSP_Stride __vDSP_IF, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_zcspec()](https://developer.apple.com/documentation/accelerate/1450283-vdsp_zcspec)

|  | Declaration |
| --- | --- |
| From | void vDSP_zcspec ( DSPSplitComplex \*__vDSP_A, DSPSplitComplex \*__vDSP_B, DSPSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_zcspec ( const DSPSplitComplex \*__vDSP_A, const DSPSplitComplex \*__vDSP_B, const DSPSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_zcspecD()](https://developer.apple.com/documentation/accelerate/1450164-vdsp_zcspecd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zcspecD ( DSPDoubleSplitComplex \*A, DSPDoubleSplitComplex \*__vDSP_B, DSPDoubleSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_zcspecD ( const DSPDoubleSplitComplex \*__vDSP_A, const DSPDoubleSplitComplex \*__vDSP_B, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_zdotpr()](https://developer.apple.com/documentation/accelerate/1450701-vdsp_zdotpr)

|  | Declaration |
| --- | --- |
| From | void vDSP_zdotpr ( DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPSplitComplex \*__vDSP_result, vDSP_Length __vDSP_size); |
| To | void vDSP_zdotpr ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_zdotprD()](https://developer.apple.com/documentation/accelerate/1450740-vdsp_zdotprd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zdotprD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPDoubleSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Length __vDSP_size); |
| To | void vDSP_zdotprD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_zidotpr()](https://developer.apple.com/documentation/accelerate/1450063-vdsp_zidotpr)

|  | Declaration |
| --- | --- |
| From | void vDSP_zidotpr ( DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPSplitComplex \*__vDSP_result, vDSP_Length __vDSP_size); |
| To | void vDSP_zidotpr ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_zidotprD()](https://developer.apple.com/documentation/accelerate/1450309-vdsp_zidotprd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zidotprD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPDoubleSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Length __vDSP_size); |
| To | void vDSP_zidotprD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_zmma()](https://developer.apple.com/documentation/accelerate/1450160-vdsp_zmma)

|  | Declaration |
| --- | --- |
| From | void vDSP_zmma ( DSPSplitComplex \*__vDSP_a, vDSP_Stride __vDSP_i, DSPSplitComplex \*__vDSP_b, vDSP_Stride __vDSP_j, DSPSplitComplex \*__vDSP_c, vDSP_Stride __vDSP_k, DSPSplitComplex \*__vDSP_d, vDSP_Stride __vDSP_l, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_zmma ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_zmmaD()](https://developer.apple.com/documentation/accelerate/1450365-vdsp_zmmad)

|  | Declaration |
| --- | --- |
| From | void vDSP_zmmaD ( DSPDoubleSplitComplex \*__vDSP_a, vDSP_Stride __vDSP_i, DSPDoubleSplitComplex \*__vDSP_b, vDSP_Stride __vDSP_j, DSPDoubleSplitComplex \*__vDSP_c, vDSP_Stride __vDSP_k, DSPDoubleSplitComplex \*__vDSP_d, vDSP_Stride __vDSP_l, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_zmmaD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_zmms()](https://developer.apple.com/documentation/accelerate/1450785-vdsp_zmms)

|  | Declaration |
| --- | --- |
| From | void vDSP_zmms ( DSPSplitComplex \*__vDSP_a, vDSP_Stride __vDSP_i, DSPSplitComplex \*__vDSP_b, vDSP_Stride __vDSP_j, DSPSplitComplex \*__vDSP_c, vDSP_Stride __vDSP_k, DSPSplitComplex \*__vDSP_d, vDSP_Stride __vDSP_l, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_zmms ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_zmmsD()](https://developer.apple.com/documentation/accelerate/1450311-vdsp_zmmsd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zmmsD ( DSPDoubleSplitComplex \*__vDSP_a, vDSP_Stride __vDSP_i, DSPDoubleSplitComplex \*__vDSP_b, vDSP_Stride __vDSP_j, DSPDoubleSplitComplex \*__vDSP_c, vDSP_Stride __vDSP_k, DSPDoubleSplitComplex \*__vDSP_d, vDSP_Stride __vDSP_l, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_zmmsD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_zmmul()](https://developer.apple.com/documentation/accelerate/1449712-vdsp_zmmul)

|  | Declaration |
| --- | --- |
| From | void vDSP_zmmul ( DSPSplitComplex \*__vDSP_a, vDSP_Stride __vDSP_i, DSPSplitComplex \*__vDSP_b, vDSP_Stride __vDSP_j, DSPSplitComplex \*__vDSP_c, vDSP_Stride __vDSP_k, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_zmmul ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_zmmulD()](https://developer.apple.com/documentation/accelerate/1450796-vdsp_zmmuld)

|  | Declaration |
| --- | --- |
| From | void vDSP_zmmulD ( DSPDoubleSplitComplex \*__vDSP_a, vDSP_Stride __vDSP_i, DSPDoubleSplitComplex \*__vDSP_b, vDSP_Stride __vDSP_j, DSPDoubleSplitComplex \*__vDSP_c, vDSP_Stride __vDSP_k, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_zmmulD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_zmsm()](https://developer.apple.com/documentation/accelerate/1450400-vdsp_zmsm)

|  | Declaration |
| --- | --- |
| From | void vDSP_zmsm ( DSPSplitComplex \*__vDSP_a, vDSP_Stride __vDSP_i, DSPSplitComplex \*__vDSP_b, vDSP_Stride __vDSP_j, DSPSplitComplex \*__vDSP_c, vDSP_Stride __vDSP_k, DSPSplitComplex \*__vDSP_d, vDSP_Stride __vDSP_l, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_zmsm ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_zmsmD()](https://developer.apple.com/documentation/accelerate/1450218-vdsp_zmsmd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zmsmD ( DSPDoubleSplitComplex \*__vDSP_a, vDSP_Stride __vDSP_i, DSPDoubleSplitComplex \*__vDSP_b, vDSP_Stride __vDSP_j, DSPDoubleSplitComplex \*__vDSP_c, vDSP_Stride __vDSP_k, DSPDoubleSplitComplex \*__vDSP_d, vDSP_Stride __vDSP_l, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_zmsmD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_zrdesamp()](https://developer.apple.com/documentation/accelerate/1449891-vdsp_zrdesamp)

|  | Declaration |
| --- | --- |
| From | void vDSP_zrdesamp ( DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, DSPSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |
| To | void vDSP_zrdesamp ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, const float \*__vDSP_F, const DSPSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_zrdesampD()](https://developer.apple.com/documentation/accelerate/1449934-vdsp_zrdesampd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zrdesampD ( DSPDoubleSplitComplex \*A, vDSP_Stride __vDSP_I, double \*__vDSP_B, DSPDoubleSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |
| To | void vDSP_zrdesampD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, const double \*__vDSP_F, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_zrdotpr()](https://developer.apple.com/documentation/accelerate/1450544-vdsp_zrdotpr)

|  | Declaration |
| --- | --- |
| From | void vDSP_zrdotpr ( DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, DSPSplitComplex \*__vDSP_result, vDSP_Length __vDSP_size); |
| To | void vDSP_zrdotpr ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_zrdotprD()](https://developer.apple.com/documentation/accelerate/1450394-vdsp_zrdotprd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zrdotprD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Length __vDSP_size); |
| To | void vDSP_zrdotprD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_zrvadd()](https://developer.apple.com/documentation/accelerate/1449990-vdsp_zrvadd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zrvadd ( DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_zrvadd ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zrvaddD()](https://developer.apple.com/documentation/accelerate/1450465-vdsp_zrvaddd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zrvaddD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_zrvaddD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zrvdiv()](https://developer.apple.com/documentation/accelerate/1450142-vdsp_zrvdiv)

|  | Declaration |
| --- | --- |
| From | void vDSP_zrvdiv ( DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zrvdiv ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zrvdivD()](https://developer.apple.com/documentation/accelerate/1450666-vdsp_zrvdivd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zrvdivD ( DSPDoubleSplitComplex \*A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zrvdivD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zrvmul()](https://developer.apple.com/documentation/accelerate/1450657-vdsp_zrvmul)

|  | Declaration |
| --- | --- |
| From | void vDSP_zrvmul ( DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_zrvmul ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zrvmulD()](https://developer.apple.com/documentation/accelerate/1449954-vdsp_zrvmuld)

|  | Declaration |
| --- | --- |
| From | void vDSP_zrvmulD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_zrvmulD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zrvsub()](https://developer.apple.com/documentation/accelerate/1449845-vdsp_zrvsub)

|  | Declaration |
| --- | --- |
| From | void vDSP_zrvsub ( DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_zrvsub ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zrvsubD()](https://developer.apple.com/documentation/accelerate/1450034-vdsp_zrvsubd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zrvsubD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_zrvsubD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_ztoc()](https://developer.apple.com/documentation/kernel/1579934-vdsp_ztoc)

|  | Declaration |
| --- | --- |
| From | void vDSP_ztoc ( const DSPSplitComplex \*__vDSP_Z, vDSP_Stride __vDSP_strideZ, DSPComplex __vDSP_C[], vDSP_Stride __vDSP_strideC, vDSP_Length __vDSP_size); |
| To | void vDSP_ztoc ( const DSPSplitComplex \*__vDSP_Z, vDSP_Stride __vDSP_IZ, DSPComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_ztocD()](https://developer.apple.com/documentation/accelerate/1450165-vdsp_ztocd)

|  | Declaration |
| --- | --- |
| From | void vDSP_ztocD ( const DSPDoubleSplitComplex \*__vDSP_Z, vDSP_Stride __vDSP_strideZ, DSPDoubleComplex __vDSP_C[], vDSP_Stride __vDSP_strideC, vDSP_Length __vDSP_size); |
| To | void vDSP_ztocD ( const DSPDoubleSplitComplex \*__vDSP_Z, vDSP_Stride __vDSP_IZ, DSPDoubleComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_ztrans()](https://developer.apple.com/documentation/accelerate/1450787-vdsp_ztrans)

|  | Declaration |
| --- | --- |
| From | void vDSP_ztrans ( float \*__vDSP_A, DSPSplitComplex \*__vDSP_B, DSPSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_ztrans ( const float \*__vDSP_A, const DSPSplitComplex \*__vDSP_B, const DSPSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_ztransD()](https://developer.apple.com/documentation/accelerate/1450357-vdsp_ztransd)

|  | Declaration |
| --- | --- |
| From | void vDSP_ztransD ( double \*__vDSP_A, DSPDoubleSplitComplex \*__vDSP_B, DSPDoubleSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_ztransD ( const double \*__vDSP_A, const DSPDoubleSplitComplex \*__vDSP_B, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_zvabs()](https://developer.apple.com/documentation/kernel/1579998-vdsp_zvabs)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvabs ( DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvabs ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvabsD()](https://developer.apple.com/documentation/accelerate/1450251-vdsp_zvabsd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvabsD ( DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvabsD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvadd()](https://developer.apple.com/documentation/accelerate/1450051-vdsp_zvadd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvadd ( DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_zvadd ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvaddD()](https://developer.apple.com/documentation/accelerate/1449906-vdsp_zvaddd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvaddD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPDoubleSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_zvaddD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvcma()](https://developer.apple.com/documentation/accelerate/1450200-vdsp_zvcma)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvcma ( const DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const DSPSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, const DSPSplitComplex \*__vDSP_input3, vDSP_Stride __vDSP_stride3, const DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_zvcma ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_zvcmaD()](https://developer.apple.com/documentation/accelerate/1450572-vdsp_zvcmad)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvcmaD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPDoubleSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_input3, vDSP_Stride __vDSP_stride3, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_zvcmaD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_zvcmul()](https://developer.apple.com/documentation/accelerate/1450717-vdsp_zvcmul)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvcmul ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_J, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvcmul ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvcmulD()](https://developer.apple.com/documentation/accelerate/1449764-vdsp_zvcmuld)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvcmulD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_J, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvcmulD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_iC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvconj()](https://developer.apple.com/documentation/accelerate/1450617-vdsp_zvconj)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvconj ( DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvconj ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvconjD()](https://developer.apple.com/documentation/accelerate/1450479-vdsp_zvconjd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvconjD ( DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvconjD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvdiv()](https://developer.apple.com/documentation/accelerate/1449769-vdsp_zvdiv)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvdiv ( DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_J, DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvdiv ( const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvdivD()](https://developer.apple.com/documentation/accelerate/1450594-vdsp_zvdivd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvdivD ( DSPDoubleSplitComplex \*A, vDSP_Stride __vDSP_I, DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_J, DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvdivD ( const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvfill()](https://developer.apple.com/documentation/accelerate/1450499-vdsp_zvfill)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvfill ( DSPSplitComplex \*__vDSP_A, DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvfill ( const DSPSplitComplex \*__vDSP_A, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvfillD()](https://developer.apple.com/documentation/accelerate/1450495-vdsp_zvfilld)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvfillD ( DSPDoubleSplitComplex \*__vDSP_A, DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvfillD ( const DSPDoubleSplitComplex \*__vDSP_A, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvmags()](https://developer.apple.com/documentation/accelerate/1450557-vdsp_zvmags)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvmags ( DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvmags ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvmagsD()](https://developer.apple.com/documentation/accelerate/1450026-vdsp_zvmagsd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvmagsD ( DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvmagsD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvmgsa()](https://developer.apple.com/documentation/accelerate/1450647-vdsp_zvmgsa)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvmgsa ( DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvmgsa ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvmgsaD()](https://developer.apple.com/documentation/accelerate/1450338-vdsp_zvmgsad)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvmgsaD ( DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvmgsaD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvmov()](https://developer.apple.com/documentation/kernel/1579979-vdsp_zvmov)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvmov ( DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvmov ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvmovD()](https://developer.apple.com/documentation/accelerate/1450484-vdsp_zvmovd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvmovD ( DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvmovD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvmul()](https://developer.apple.com/documentation/kernel/1579954-vdsp_zvmul)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvmul ( const DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const DSPSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, const DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size, int __vDSP_conjugate); |
| To | void vDSP_zvmul ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, int __vDSP_Conjugate); |

Modified [vDSP_zvmulD()](https://developer.apple.com/documentation/accelerate/1450390-vdsp_zvmuld)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvmulD ( const DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const DSPDoubleSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, const DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size, int __vDSP_conjugate); |
| To | void vDSP_zvmulD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, int __vDSP_Conjugate); |

Modified [vDSP_zvneg()](https://developer.apple.com/documentation/accelerate/1450326-vdsp_zvneg)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvneg ( DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvneg ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvnegD()](https://developer.apple.com/documentation/accelerate/1450351-vdsp_zvnegd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvnegD ( DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvnegD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvphas()](https://developer.apple.com/documentation/accelerate/1449904-vdsp_zvphas)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvphas ( DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvphas ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvphasD()](https://developer.apple.com/documentation/accelerate/1450132-vdsp_zvphasd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvphasD ( DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvphasD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvsma()](https://developer.apple.com/documentation/accelerate/1449902-vdsp_zvsma)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvsma ( DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, DSPSplitComplex \*__vDSP_B, DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, DSPSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_zvsma ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_zvsmaD()](https://developer.apple.com/documentation/accelerate/1450570-vdsp_zvsmad)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvsmaD ( DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, DSPDoubleSplitComplex \*__vDSP_B, DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, DSPDoubleSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_zvsmaD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_zvsub()](https://developer.apple.com/documentation/accelerate/1450818-vdsp_zvsub)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvsub ( DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_zvsub ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvsubD()](https://developer.apple.com/documentation/accelerate/1450642-vdsp_zvsubd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvsubD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPDoubleSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_zvsubD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvzsml()](https://developer.apple.com/documentation/accelerate/1450410-vdsp_zvzsml)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvzsml ( DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, DSPSplitComplex \*__vDSP_B, DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvzsml ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvzsmlD()](https://developer.apple.com/documentation/accelerate/1449727-vdsp_zvzsmld)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvzsmlD ( DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, DSPDoubleSplitComplex \*__vDSP_B, DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvzsmlD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

vForce.hModified [vvcopysign()](https://developer.apple.com/documentation/accelerate/1470348-vvcopysign)

|  | Declaration |
| --- | --- |
| From | void vvcopysign ( double \*, double \*, const double \*, const int \*); |
| To | void vvcopysign ( double \*, const double \*, const double \*, const int \*); |

Modified [vvfmod()](https://developer.apple.com/documentation/accelerate/1470379-vvfmod)

|  | Declaration |
| --- | --- |
| From | void vvfmod ( double \*, double \*, const double \*, const int \*); |
| To | void vvfmod ( double \*, const double \*, const double \*, const int \*); |

Modified [vvnextafter()](https://developer.apple.com/documentation/accelerate/1470487-vvnextafter)

|  | Declaration |
| --- | --- |
| From | void vvnextafter ( double \*, double \*, const double \*, const int \*); |
| To | void vvnextafter ( double \*, const double \*, const double \*, const int \*); |

Modified [vvremainder()](https://developer.apple.com/documentation/accelerate/1470456-vvremainder)

|  | Declaration |
| --- | --- |
| From | void vvremainder ( double \*, double \*, const double \*, const int \*); |
| To | void vvremainder ( double \*, const double \*, const double \*, const int \*); |

vImage_Types.hAdded Pixel_16SAdded Pixel_ARGB_16SAdded Pixel_ARGB_16UAdded #def VIMAGE_CHOICE_ENUMAdded #def VIMAGE_ENUM_AVAILABLE_STARTINGAdded #def VIMAGE_NON_NULLAdded #def VIMAGE_OPTIONS_ENUMAdded [kvImageColorSyncIsAbsent](https://developer.apple.com/documentation/accelerate/kvimagecolorsyncisabsent)Added [kvImageInternalError](https://developer.apple.com/documentation/accelerate/kvimageinternalerror)Added [kvImageInvalidImageFormat](https://developer.apple.com/documentation/accelerate/1578972-error_codes/kvimageinvalidimageformat)Added [kvImageInvalidRowBytes](https://developer.apple.com/documentation/accelerate/kvimageinvalidrowbytes)Added [kvImageNoAllocate](https://developer.apple.com/documentation/accelerate/1578976-processing_flags/kvimagenoallocate)Added [kvImageOutOfPlaceOperationRequired](https://developer.apple.com/documentation/accelerate/kvimageoutofplaceoperationrequired)Added [kvImagePrintDiagnosticsToConsole](https://developer.apple.com/documentation/accelerate/kvimageprintdiagnosticstoconsole)vImage_Utilities.hAdded [kvImageDecodeArray_16Q12Format](https://developer.apple.com/documentation/accelerate/kvimagedecodearray_16q12format)Added [vImageBuffer_GetSize()](https://developer.apple.com/documentation/accelerate/1399062-vimagebuffer_getsize)Added [vImageBuffer_Init()](https://developer.apple.com/documentation/accelerate/1399064-vimagebuffer_init)Added [vImageBuffer_InitWithCGImage()](https://developer.apple.com/documentation/accelerate/1399118-vimagebuffer_initwithcgimage)Added [vImageCGImageFormat_GetComponentCount()](https://developer.apple.com/documentation/accelerate/1399104-vimagecgimageformat_getcomponent)Added [vImageCGImageFormat_IsEqual()](https://developer.apple.com/documentation/accelerate/1399126-vimagecgimageformat_isequal)Added [vImageConvert_AnyToAny()](https://developer.apple.com/documentation/accelerate/1399134-vimageconvert_anytoany)Added [vImageConverterRef](https://developer.apple.com/documentation/accelerate/vimageconverterref)Added [vImageConverter_CreateWithCGImageFormat()](https://developer.apple.com/documentation/accelerate/1399114-vimageconverter_createwithcgimag)Added [vImageConverter_CreateWithColorSyncCodeFragment()](https://developer.apple.com/documentation/accelerate/1399082-vimageconverter_createwithcolors)Added [vImageConverter_MustOperateOutOfPlace()](https://developer.apple.com/documentation/accelerate/1399054-vimageconverter_mustoperateoutof)Added [vImageConverter_Release()](https://developer.apple.com/documentation/accelerate/1399068-vimageconverter_release)Added [vImageConverter_Retain()](https://developer.apple.com/documentation/accelerate/1399028-vimageconverter_retain)Added [vImageCreateCGImageFromBuffer()](https://developer.apple.com/documentation/accelerate/1399036-vimagecreatecgimagefrombuffer)Added [vImage_CGImageFormat](https://developer.apple.com/documentation/accelerate/vimage_cgimageformat)Added #def vImage_Utilities_hvecLibTypes.hAdded [vSInt64](https://developer.apple.com/documentation/kernel/vsint64)Added [vUInt64](https://developer.apple.com/documentation/kernel/vuint64)

## Accounts

ACAccount.hAdded [ACAccount.userFullName](https://developer.apple.com/documentation/accounts/acaccount/1616631-userfullname)ACAccountStore.hModified [ACFacebookAppIdKey](https://developer.apple.com/documentation/accounts/acfacebookappidkey)

|  | Header |
| --- | --- |
| From | Accounts/ACAccountStore.h |
| To | Accounts/ACAccountType.h |

Modified [ACFacebookAudienceEveryone](https://developer.apple.com/documentation/accounts/acfacebookaudienceeveryone)

|  | Header |
| --- | --- |
| From | Accounts/ACAccountStore.h |
| To | Accounts/ACAccountType.h |

Modified [ACFacebookAudienceFriends](https://developer.apple.com/documentation/accounts/acfacebookaudiencefriends)

|  | Header |
| --- | --- |
| From | Accounts/ACAccountStore.h |
| To | Accounts/ACAccountType.h |

Modified [ACFacebookAudienceKey](https://developer.apple.com/documentation/accounts/acfacebookaudiencekey)

|  | Header |
| --- | --- |
| From | Accounts/ACAccountStore.h |
| To | Accounts/ACAccountType.h |

Modified [ACFacebookAudienceOnlyMe](https://developer.apple.com/documentation/accounts/acfacebookaudienceonlyme)

|  | Header |
| --- | --- |
| From | Accounts/ACAccountStore.h |
| To | Accounts/ACAccountType.h |

Modified [ACFacebookPermissionsKey](https://developer.apple.com/documentation/accounts/acfacebookpermissionskey)

|  | Header |
| --- | --- |
| From | Accounts/ACAccountStore.h |
| To | Accounts/ACAccountType.h |

ACAccountType.hAdded [ACAccountTypeIdentifierTencentWeibo](https://developer.apple.com/documentation/accounts/acaccounttypeidentifiertencentweibo)Added [ACTencentWeiboAppIdKey](https://developer.apple.com/documentation/accounts/actencentweiboappidkey)Modified [ACFacebookAppIdKey](https://developer.apple.com/documentation/accounts/acfacebookappidkey)

|  | Header |
| --- | --- |
| From | Accounts/ACAccountStore.h |
| To | Accounts/ACAccountType.h |

Modified [ACFacebookAudienceEveryone](https://developer.apple.com/documentation/accounts/acfacebookaudienceeveryone)

|  | Header |
| --- | --- |
| From | Accounts/ACAccountStore.h |
| To | Accounts/ACAccountType.h |

Modified [ACFacebookAudienceFriends](https://developer.apple.com/documentation/accounts/acfacebookaudiencefriends)

|  | Header |
| --- | --- |
| From | Accounts/ACAccountStore.h |
| To | Accounts/ACAccountType.h |

Modified [ACFacebookAudienceKey](https://developer.apple.com/documentation/accounts/acfacebookaudiencekey)

|  | Header |
| --- | --- |
| From | Accounts/ACAccountStore.h |
| To | Accounts/ACAccountType.h |

Modified [ACFacebookAudienceOnlyMe](https://developer.apple.com/documentation/accounts/acfacebookaudienceonlyme)

|  | Header |
| --- | --- |
| From | Accounts/ACAccountStore.h |
| To | Accounts/ACAccountType.h |

Modified [ACFacebookPermissionsKey](https://developer.apple.com/documentation/accounts/acfacebookpermissionskey)

|  | Header |
| --- | --- |
| From | Accounts/ACAccountStore.h |
| To | Accounts/ACAccountType.h |

ACError.hAdded [ACErrorAccessDeniedByProtectionPolicy](https://developer.apple.com/documentation/accounts/acerroraccessdeniedbyprotectionpolicy)Added [ACErrorClientPermissionDenied](https://developer.apple.com/documentation/accounts/acerrorclientpermissiondenied)Added [ACErrorCredentialNotFound](https://developer.apple.com/documentation/accounts/acerrorcredentialnotfound)Added [ACErrorFetchCredentialFailed](https://developer.apple.com/documentation/accounts/acerrorcode/acerrorfetchcredentialfailed)Added [ACErrorInvalidClientBundleID](https://developer.apple.com/documentation/accounts/acerrorcode/acerrorinvalidclientbundleid)Added [ACErrorRemoveCredentialFailed](https://developer.apple.com/documentation/accounts/acerrorcode/acerrorremovecredentialfailed)Added [ACErrorStoreCredentialFailed](https://developer.apple.com/documentation/accounts/acerrorcode/acerrorstorecredentialfailed)Added [ACErrorUpdatingNonexistentAccount](https://developer.apple.com/documentation/accounts/acerrorupdatingnonexistentaccount)

## AddressBook

ABPerson.hAdded [ABPersonCopyCompositeNameDelimiterForRecord()](https://developer.apple.com/documentation/addressbook/1619765-abpersoncopycompositenamedelimit)Added [ABPersonGetCompositeNameFormatForRecord()](https://developer.apple.com/documentation/addressbook/1619802-abpersongetcompositenameformatfo)Modified [ABPersonGetCompositeNameFormat()](https://developer.apple.com/documentation/addressbook/1619750-abpersongetcompositenameformat)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

## AddressBookUI

No changes

## AdSupport

No changes

## AssetsLibrary

No changes

## AudioToolbox

AudioFile.hAdded [kAudioFilePropertyAudioTrackCount](https://developer.apple.com/documentation/audiotoolbox/kaudiofilepropertyaudiotrackcount)Added [kAudioFilePropertyUseAudioTrack](https://developer.apple.com/documentation/audiotoolbox/kaudiofilepropertyuseaudiotrack)AudioFileStream.hAdded [kAudioFileStreamProperty_InfoDictionary](https://developer.apple.com/documentation/audiotoolbox/1391506-audio_file_stream_properties/kaudiofilestreamproperty_infodictionary)AudioQueue.hAdded [kAudioQueueParam_Pitch](https://developer.apple.com/documentation/audiotoolbox/1552626-audio_queue_parameters/kaudioqueueparam_pitch)Added [kAudioQueueParam_PlayRate](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueparam_playrate)Added [kAudioQueueProperty_EnableTimePitch](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueproperty_enabletimepitch)Added [kAudioQueueProperty_TimePitchAlgorithm](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueproperty_timepitchalgorithm)Added [kAudioQueueProperty_TimePitchBypass](https://developer.apple.com/documentation/audiotoolbox/1552629-anonymous/kaudioqueueproperty_timepitchbypass)Added [kAudioQueueTimePitchAlgorithm_LowQualityZeroLatency](https://developer.apple.com/documentation/audiotoolbox/1618742-anonymous/kaudioqueuetimepitchalgorithm_lowqualityzerolatency)Added [kAudioQueueTimePitchAlgorithm_Spectral](https://developer.apple.com/documentation/audiotoolbox/1552630-anonymous/kaudioqueuetimepitchalgorithm_spectral)Added [kAudioQueueTimePitchAlgorithm_TimeDomain](https://developer.apple.com/documentation/audiotoolbox/kaudioqueuetimepitchalgorithm_timedomain)Added [kAudioQueueTimePitchAlgorithm_Varispeed](https://developer.apple.com/documentation/audiotoolbox/kaudioqueuetimepitchalgorithm_varispeed)AudioSession.hAdded [kAudioSessionRouteChangeReason_RouteConfigurationChange](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionroutechangereason_routeconfigurationchange)Modified [AudioSessionAddPropertyListener()](https://developer.apple.com/documentation/audiotoolbox/1618442-audiosessionaddpropertylistener)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [AudioSessionGetProperty()](https://developer.apple.com/documentation/audiotoolbox/1618433-audiosessiongetproperty)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [AudioSessionGetPropertySize()](https://developer.apple.com/documentation/audiotoolbox/1618437-audiosessiongetpropertysize)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [AudioSessionInitialize()](https://developer.apple.com/documentation/audiotoolbox/1618360-audiosessioninitialize)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [AudioSessionRemovePropertyListenerWithUserData()](https://developer.apple.com/documentation/audiotoolbox/1618396-audiosessionremovepropertylisten)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [AudioSessionSetActive()](https://developer.apple.com/documentation/audiotoolbox/1618421-audiosessionsetactive)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [AudioSessionSetActiveWithFlags()](https://developer.apple.com/documentation/audiotoolbox/1618356-audiosessionsetactivewithflags)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [AudioSessionSetProperty()](https://developer.apple.com/documentation/audiotoolbox/1618399-audiosessionsetproperty)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kAudioSessionInputRoute_BluetoothHFP](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioninputroute_bluetoothhfp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kAudioSessionInputRoute_BuiltInMic](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioninputroute_builtinmic)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kAudioSessionInputRoute_HeadsetMic](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioninputroute_headsetmic)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kAudioSessionInputRoute_LineIn](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioninputroute_linein)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kAudioSessionInputRoute_USBAudio](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioninputroute_usbaudio)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kAudioSessionOutputRoute_AirPlay](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_airplay)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kAudioSessionOutputRoute_BluetoothA2DP](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_bluetootha2dp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kAudioSessionOutputRoute_BluetoothHFP](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_bluetoothhfp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kAudioSessionOutputRoute_BuiltInReceiver](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_builtinreceiver)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kAudioSessionOutputRoute_BuiltInSpeaker](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_builtinspeaker)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kAudioSessionOutputRoute_HDMI](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_hdmi)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kAudioSessionOutputRoute_Headphones](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_headphones)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kAudioSessionOutputRoute_LineOut](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_lineout)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kAudioSessionOutputRoute_USBAudio](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_usbaudio)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kAudioSession_AudioRouteChangeKey_CurrentRouteDescription](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_audioroutechangekey_currentroutedescription)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kAudioSession_AudioRouteChangeKey_PreviousRouteDescription](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_audioroutechangekey_previousroutedescription)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kAudioSession_AudioRouteKey_Inputs](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_audioroutekey_inputs)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kAudioSession_AudioRouteKey_Outputs](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_audioroutekey_outputs)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kAudioSession_AudioRouteKey_Type](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_audioroutekey_type)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kAudioSession_InputSourceKey_Description](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_inputsourcekey_description)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kAudioSession_InputSourceKey_ID](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_inputsourcekey_id)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kAudioSession_OutputDestinationKey_Description](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_outputdestinationkey_description)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kAudioSession_OutputDestinationKey_ID](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_outputdestinationkey_id)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kAudioSession_RouteChangeKey_Reason](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_routechangekey_reason)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

AudioToolbox.hAdded [CopyInstrumentInfoFromSoundBank()](https://developer.apple.com/documentation/audiotoolbox/1475995-copyinstrumentinfofromsoundbank)Added [CopyNameFromSoundBank()](https://developer.apple.com/documentation/audiotoolbox/1475986-copynamefromsoundbank)Added [#def kInstrumentInfoKey_LSB](https://developer.apple.com/documentation/audiotoolbox/kinstrumentinfokey_lsb)Added [#def kInstrumentInfoKey_MSB](https://developer.apple.com/documentation/audiotoolbox/kinstrumentinfokey_msb)Added [#def kInstrumentInfoKey_Name](https://developer.apple.com/documentation/audiotoolbox/kinstrumentinfokey_name)Added [#def kInstrumentInfoKey_Program](https://developer.apple.com/documentation/audiotoolbox/kinstrumentinfokey_program)

## AudioUnit

AUComponent.hRemoved kAudioUnitSubType_DCFilterAdded [AudioComponentGetIcon()](https://developer.apple.com/documentation/audiotoolbox/1410443-audiocomponentgeticon)Added [AudioComponentGetLastActiveTime()](https://developer.apple.com/documentation/audiotoolbox/1619499-audiocomponentgetlastactivetime)Added [AudioOutputUnitGetHostIcon()](https://developer.apple.com/documentation/audiotoolbox/1619491-audiooutputunitgethosticon)Added [AudioOutputUnitPublish()](https://developer.apple.com/documentation/audiotoolbox/1619489-audiooutputunitpublish)Added [kAudioComponentErr_DuplicateDescription](https://developer.apple.com/documentation/audiotoolbox/1619490-anonymous/kaudiocomponenterr_duplicatedescription)Added [kAudioComponentErr_InitializationTimedOut](https://developer.apple.com/documentation/audiotoolbox/1619490-anonymous/kaudiocomponenterr_initializationtimedout)Added [kAudioComponentErr_InstanceInvalidated](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiocomponenterr_instanceinvalidated)Added [kAudioComponentErr_InvalidFormat](https://developer.apple.com/documentation/audiotoolbox/1619490-anonymous/kaudiocomponenterr_invalidformat)Added [kAudioComponentErr_NotPermitted](https://developer.apple.com/documentation/audiotoolbox/1619490-anonymous/kaudiocomponenterr_notpermitted)Added [kAudioComponentErr_TooManyInstances](https://developer.apple.com/documentation/audiotoolbox/1619490-anonymous/kaudiocomponenterr_toomanyinstances)Added [kAudioComponentErr_UnsupportedType](https://developer.apple.com/documentation/audiotoolbox/1619490-anonymous/kaudiocomponenterr_unsupportedtype)Added [kAudioComponentRegistrationsChangedNotification](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponentregistrationschangednotification)Added [kAudioUnitType_MIDIProcessor](https://developer.apple.com/documentation/audiotoolbox/1584142-audio_unit_types/kaudiounittype_midiprocessor)Added [kAudioUnitType_RemoteEffect](https://developer.apple.com/documentation/audiotoolbox/1619501-anonymous/kaudiounittype_remoteeffect)Added [kAudioUnitType_RemoteGenerator](https://developer.apple.com/documentation/audiotoolbox/1619501-anonymous/kaudiounittype_remotegenerator)Added [kAudioUnitType_RemoteInstrument](https://developer.apple.com/documentation/audiotoolbox/1619501-anonymous/kaudiounittype_remoteinstrument)Added [kAudioUnitType_RemoteMusicEffect](https://developer.apple.com/documentation/audiotoolbox/1619501-anonymous/kaudiounittype_remotemusiceffect)AudioComponent.hAdded [kAudioComponentFlag_SandboxSafe](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/kaudiocomponentflag_sandboxsafe)AudioUnitParameters.hRemoved kAUDCFilterParam_DecayTimeAdded [kRandomParam_BoundA](https://developer.apple.com/documentation/audiotoolbox/1389639-anonymous/krandomparam_bounda)Added [kRandomParam_BoundB](https://developer.apple.com/documentation/audiotoolbox/krandomparam_boundb)Added [kRandomParam_Curve](https://developer.apple.com/documentation/audiotoolbox/1389639-anonymous/krandomparam_curve)AudioUnitProperties.hAdded [AudioOutputUnitMIDICallbacks](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitmidicallbacks)Added [AudioUnitRemoteControlEvent](https://developer.apple.com/documentation/audiotoolbox/audiounitremotecontrolevent)Added [AudioUnitRemoteControlEventListener](https://developer.apple.com/documentation/audiotoolbox/audiounitremotecontroleventlistener)Added [HostCallback_GetTransportState2](https://developer.apple.com/documentation/audiotoolbox/hostcallback_gettransportstate2)Added [kAUNBandEQProperty_BiquadCoefficients](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqproperty_biquadcoefficients)Added [kAudioOutputUnitProperty_HostReceivesRemoteControlEvents](https://developer.apple.com/documentation/audiotoolbox/1621039-anonymous/kaudiooutputunitproperty_hostreceivesremotecontrolevents)Added [kAudioOutputUnitProperty_HostTransportState](https://developer.apple.com/documentation/audiotoolbox/1621039-anonymous/kaudiooutputunitproperty_hosttransportstate)Added [kAudioOutputUnitProperty_MIDICallbacks](https://developer.apple.com/documentation/audiotoolbox/kaudiooutputunitproperty_midicallbacks)Added [kAudioOutputUnitProperty_NodeComponentDescription](https://developer.apple.com/documentation/audiotoolbox/1621039-anonymous/kaudiooutputunitproperty_nodecomponentdescription)Added [kAudioOutputUnitProperty_RemoteControlToHost](https://developer.apple.com/documentation/audiotoolbox/1621039-anonymous/kaudiooutputunitproperty_remotecontroltohost)Added [#def kAudioUnitConfigurationInfo_ChannelConfigurations](https://developer.apple.com/documentation/audiotoolbox/kaudiounitconfigurationinfo_channelconfigurations)Added [#def kAudioUnitConfigurationInfo_HasCustomView](https://developer.apple.com/documentation/audiotoolbox/kaudiounitconfigurationinfo_hascustomview)Added [#def kAudioUnitConfigurationInfo_InitialInputs](https://developer.apple.com/documentation/audiotoolbox/kaudiounitconfigurationinfo_initialinputs)Added [#def kAudioUnitConfigurationInfo_InitialOutputs](https://developer.apple.com/documentation/audiotoolbox/kaudiounitconfigurationinfo_initialoutputs)Added [kAudioUnitProperty_FrequencyResponse](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_frequencyresponse)Added [kAudioUnitProperty_IsInterAppConnected](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_isinterappconnected)Added [kAudioUnitProperty_PeerURL](https://developer.apple.com/documentation/audiotoolbox/1621038-anonymous/kaudiounitproperty_peerurl)Added [kAudioUnitProperty_RemoteControlEventListener](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_remotecontroleventlistener)Added [kAudioUnitRemoteControlEvent_Rewind](https://developer.apple.com/documentation/audiotoolbox/audiounitremotecontrolevent/kaudiounitremotecontrolevent_rewind)Added [kAudioUnitRemoteControlEvent_TogglePlayPause](https://developer.apple.com/documentation/audiotoolbox/audiounitremotecontrolevent/toggleplaypause)Added [kAudioUnitRemoteControlEvent_ToggleRecord](https://developer.apple.com/documentation/audiotoolbox/audiounitremotecontrolevent/togglerecord)

## AVFoundation

AVAsset.hAdded [AVAsset.trackGroups](https://developer.apple.com/documentation/avfoundation/avasset/1390697-trackgroups)AVAssetExportSession.hAdded [AVAssetExportSession.audioTimePitchAlgorithm](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1385835-audiotimepitchalgorithm)Added [AVAssetExportSession.customVideoCompositor](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1388288-customvideocompositor)Added [AVAssetExportSession.metadataItemFilter](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1390226-metadataitemfilter)AVAssetImageGenerator.hAdded [AVAssetImageGenerator.customVideoCompositor](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/1386469-customvideocompositor)AVAssetReaderOutput.hAdded [AVAssetReaderAudioMixOutput.audioTimePitchAlgorithm](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/1388713-audiotimepitchalgorithm)Added [AVAssetReaderTrackOutput.audioTimePitchAlgorithm](https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput/1387851-audiotimepitchalgorithm)Added [AVAssetReaderVideoCompositionOutput.customVideoCompositor](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/1388310-customvideocompositor)AVAssetResourceLoader.hAdded [-[AVAssetResourceLoaderDelegate resourceLoader:didCancelLoadingRequest:]](https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate/1387722-resourceloader)Added [AVAssetResourceLoadingContentInformationRequest](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingcontentinformationrequest)Added [AVAssetResourceLoadingContentInformationRequest.byteRangeAccessSupported](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingcontentinformationrequest/1386054-isbyterangeaccesssupported)Added [AVAssetResourceLoadingContentInformationRequest.contentLength](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingcontentinformationrequest/1389390-contentlength)Added [AVAssetResourceLoadingContentInformationRequest.contentType](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingcontentinformationrequest/1388529-contenttype)Added [AVAssetResourceLoadingDataRequest](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest)Added [AVAssetResourceLoadingDataRequest.currentOffset](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest/1385945-currentoffset)Added [AVAssetResourceLoadingDataRequest.requestedLength](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest/1387720-requestedlength)Added [AVAssetResourceLoadingDataRequest.requestedOffset](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest/1388428-requestedoffset)Added [-[AVAssetResourceLoadingDataRequest respondWithData:]](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest/1390581-respondwithdata)Added [AVAssetResourceLoadingRequest.cancelled](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1389518-cancelled)Added [AVAssetResourceLoadingRequest.contentInformationRequest](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1390340-contentinformationrequest)Added [AVAssetResourceLoadingRequest.dataRequest](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1388779-datarequest)Added [-[AVAssetResourceLoadingRequest finishLoading]](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1388359-finishloading)Added [AVAssetResourceLoadingRequest.redirect](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1390854-redirect)Added [AVAssetResourceLoadingRequest.response](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1389034-response)Added AVAssetResourceLoadingRequest(AVAssetResourceLoader_ContentKeyRequestSupport)Added AVAssetResourceLoadingRequest(AVAssetResourceLoadingRequestDeprecated)Modified [-[AVAssetResourceLoadingRequest finishLoadingWithResponse:data:redirect:]](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1623677-finishloadingwithresponse)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [AVAssetResourceLoadingRequest.finished](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1389270-isfinished)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly) BOOL finished |
| To | @property(nonatomic, readonly, getter=isFinished) BOOL finished |

AVAssetTrack.hAdded [-[AVAssetTrack associatedTracksOfType:]](https://developer.apple.com/documentation/avfoundation/avassettrack/1389251-associatedtracksoftype)Added [AVAssetTrack.availableTrackAssociationTypes](https://developer.apple.com/documentation/avfoundation/avassettrack/1388065-availabletrackassociationtypes)Added [AVAssetTrack.minFrameDuration](https://developer.apple.com/documentation/avfoundation/avassettrack/1388608-minframeduration)Added AVAssetTrack(AVAssetTrackTrackAssociations)Added [AVTrackAssociationTypeAudioFallback](https://developer.apple.com/documentation/avfoundation/avtrackassociationtypeaudiofallback)Added [AVTrackAssociationTypeChapterList](https://developer.apple.com/documentation/avfoundation/avassettrack/associationtype/1385984-chapterlist)Added [AVTrackAssociationTypeForcedSubtitlesOnly](https://developer.apple.com/documentation/avfoundation/avassettrack/associationtype/1387329-forcedsubtitlesonly)Added [AVTrackAssociationTypeSelectionFollower](https://developer.apple.com/documentation/avfoundation/avtrackassociationtypeselectionfollower)Added [AVTrackAssociationTypeTimecode](https://developer.apple.com/documentation/avfoundation/avtrackassociationtypetimecode)AVAssetTrackGroup.hAdded [AVAssetTrackGroup](https://developer.apple.com/documentation/avfoundation/avassettrackgroup)Added [AVAssetTrackGroup.trackIDs](https://developer.apple.com/documentation/avfoundation/avassettrackgroup/1389024-trackids)AVAssetWriter.hAdded [-[AVAssetWriter addInputGroup:]](https://developer.apple.com/documentation/avfoundation/avassetwriter/1385643-add)Added [-[AVAssetWriter canAddInputGroup:]](https://developer.apple.com/documentation/avfoundation/avassetwriter/1386698-canaddinputgroup)Added [AVAssetWriter.inputGroups](https://developer.apple.com/documentation/avfoundation/avassetwriter/1388432-inputgroups)Added [AVAssetWriterInputGroup](https://developer.apple.com/documentation/avfoundation/avassetwriterinputgroup)Added [+[AVAssetWriterInputGroup assetWriterInputGroupWithInputs:defaultInput:]](https://developer.apple.com/documentation/avfoundation/avassetwriterinputgroup/1426655-assetwriterinputgroupwithinputs)Added [AVAssetWriterInputGroup.defaultInput](https://developer.apple.com/documentation/avfoundation/avassetwriterinputgroup/1389698-defaultinput)Added [-[AVAssetWriterInputGroup initWithInputs:defaultInput:]](https://developer.apple.com/documentation/avfoundation/avassetwriterinputgroup/1389502-init)Added [AVAssetWriterInputGroup.inputs](https://developer.apple.com/documentation/avfoundation/avassetwriterinputgroup/1388226-inputs)Added AVAssetWriter(AVAssetWriterInputGroups)AVAssetWriterInput.hAdded [-[AVAssetWriterInput addTrackAssociationWithTrackOfInput:type:]](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1388347-addtrackassociationwithtrackofin)Added [-[AVAssetWriterInput canAddTrackAssociationWithTrackOfInput:type:]](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1388292-canaddtrackassociation)Added [AVAssetWriterInput.extendedLanguageTag](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1390768-extendedlanguagetag)Added [AVAssetWriterInput.languageCode](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1388507-languagecode)Added [AVAssetWriterInput.marksOutputTrackAsEnabled](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1386764-marksoutputtrackasenabled)Added [AVAssetWriterInput.naturalSize](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1387437-naturalsize)Added [AVAssetWriterInput.preferredVolume](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1389949-preferredvolume)Added AVAssetWriterInput(AVAssetWriterInputLanguageProperties)Added AVAssetWriterInput(AVAssetWriterInputPropertiesForAudibleCharacteristic)Added AVAssetWriterInput(AVAssetWriterInputTrackAssociations)AVAudioMix.hAdded [AVAudioMixInputParameters.audioTimePitchAlgorithm](https://developer.apple.com/documentation/avfoundation/avaudiomixinputparameters/1387042-audiotimepitchalgorithm)Added [AVMutableAudioMixInputParameters.audioTimePitchAlgorithm](https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters/1388300-audiotimepitchalgorithm)AVAudioPlayer.hAdded [-[AVAudioPlayer initWithContentsOfURL:fileTypeHint:error:]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388349-initwithcontentsofurl)Added [-[AVAudioPlayer initWithData:fileTypeHint:error:]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388525-initwithdata)AVAudioProcessingSettings.hAdded [AVAudioTimePitchAlgorithmLowQualityZeroLatency](https://developer.apple.com/documentation/avfoundation/avaudiotimepitchalgorithmlowqualityzerolatency)Added [AVAudioTimePitchAlgorithmSpectral](https://developer.apple.com/documentation/avfoundation/avaudiotimepitchalgorithm/1388153-spectral)Added [AVAudioTimePitchAlgorithmTimeDomain](https://developer.apple.com/documentation/avfoundation/avaudiotimepitchalgorithm/1387220-timedomain)Added [AVAudioTimePitchAlgorithmVarispeed](https://developer.apple.com/documentation/avfoundation/avaudiotimepitchalgorithmvarispeed)AVAudioSession.hAdded [AVAudioSession.availableInputs](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616557-availableinputs)Added [AVAudioSession.maximumInputNumberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616454-maximuminputnumberofchannels)Added [AVAudioSession.maximumOutputNumberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616490-maximumoutputnumberofchannels)Added [AVAudioSession.preferredInput](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616536-preferredinput)Added [AVAudioSession.preferredInputNumberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616440-preferredinputnumberofchannels)Added [AVAudioSession.preferredOutputNumberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616448-preferredoutputnumberofchannels)Added [-[AVAudioSession requestRecordPermission:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616601-requestrecordpermission)Added [-[AVAudioSession setPreferredInput:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616491-setpreferredinput)Added [-[AVAudioSession setPreferredInputNumberOfChannels:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616483-setpreferredinputnumberofchannel)Added [-[AVAudioSession setPreferredOutputNumberOfChannels:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616481-setpreferredoutputnumberofchanne)Added [AVAudioSessionChannelDescription.channelLabel](https://developer.apple.com/documentation/avfoundation/avaudiosessionchanneldescription/1616565-channellabel)Added [AVAudioSessionDataSourceDescription.location](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616495-location)Added [AVAudioSessionDataSourceDescription.orientation](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616456-orientation)Added [AVAudioSessionDataSourceDescription.preferredPolarPattern](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616446-preferredpolarpattern)Added [AVAudioSessionDataSourceDescription.selectedPolarPattern](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616619-selectedpolarpattern)Added [-[AVAudioSessionDataSourceDescription setPreferredPolarPattern:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616516-setpreferredpolarpattern)Added [AVAudioSessionDataSourceDescription.supportedPolarPatterns](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616450-supportedpolarpatterns)Added [AVAudioSessionPortDescription.dataSources](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616570-datasources)Added [AVAudioSessionPortDescription.preferredDataSource](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616628-preferreddatasource)Added [AVAudioSessionPortDescription.selectedDataSource](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616538-selecteddatasource)Added [-[AVAudioSessionPortDescription setPreferredDataSource:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616554-setpreferreddatasource)Added [AVAudioSessionErrorCode](https://developer.apple.com/documentation/avfoundation/avaudiosessionerrorcode)Added [AVAudioSessionErrorCodeBadParam](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/badparam)Added [AVAudioSessionErrorCodeCannotInterruptOthers](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/cannotinterruptothers)Added [AVAudioSessionErrorCodeCannotStartPlaying](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/cannotstartplaying)Added [AVAudioSessionErrorCodeIncompatibleCategory](https://developer.apple.com/documentation/avfoundation/avaudiosessionerrorcode/avaudiosessionerrorcodeincompatiblecategory)Added [AVAudioSessionErrorCodeIsBusy](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/isbusy)Added [AVAudioSessionErrorCodeMediaServicesFailed](https://developer.apple.com/documentation/avfoundation/avaudiosessionerrorcode/avaudiosessionerrorcodemediaservicesfailed)Added [AVAudioSessionErrorCodeMissingEntitlement](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/missingentitlement)Added [AVAudioSessionErrorCodeNone](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/none)Added [AVAudioSessionErrorCodeSiriIsRecording](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/siriisrecording)Added [AVAudioSessionErrorCodeUnspecified](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/unspecified)Added [AVAudioSessionLocationLower](https://developer.apple.com/documentation/avfoundation/avaudiosessionlocationlower)Added [AVAudioSessionLocationUpper](https://developer.apple.com/documentation/avfoundation/avaudiosession/location/1616459-upper)Added [AVAudioSessionMediaServicesWereLostNotification](https://developer.apple.com/documentation/avfoundation/avaudiosessionmediaserviceswerelostnotification)Added [AVAudioSessionModeVideoChat](https://developer.apple.com/documentation/avfoundation/avaudiosessionmodevideochat)Added [AVAudioSessionOrientationBack](https://developer.apple.com/documentation/avfoundation/avaudiosession/location/1616585-orientationback)Added [AVAudioSessionOrientationBottom](https://developer.apple.com/documentation/avfoundation/avaudiosession/location/1616577-orientationbottom)Added [AVAudioSessionOrientationFront](https://developer.apple.com/documentation/avfoundation/avaudiosession/location/1616505-orientationfront)Added [AVAudioSessionOrientationTop](https://developer.apple.com/documentation/avfoundation/avaudiosessionorientationtop)Added [AVAudioSessionPolarPatternCardioid](https://developer.apple.com/documentation/avfoundation/avaudiosession/location/1616531-polarpatterncardioid)Added [AVAudioSessionPolarPatternOmnidirectional](https://developer.apple.com/documentation/avfoundation/avaudiosession/location/1616476-polarpatternomnidirectional)Added [AVAudioSessionPolarPatternSubcardioid](https://developer.apple.com/documentation/avfoundation/avaudiosession/location/1616587-polarpatternsubcardioid)Added [AVAudioSessionPortBluetoothLE](https://developer.apple.com/documentation/avfoundation/avaudiosession/port/1616624-bluetoothle)Added [AVAudioSessionRouteChangeReasonRouteConfigurationChange](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutechangereason/avaudiosessionroutechangereasonrouteconfigurationchange)Added [PermissionBlock](https://developer.apple.com/documentation/avfoundation/permissionblock)AVAudioSettings.hAdded [AVAudioBitRateStrategy_Constant](https://developer.apple.com/documentation/avfoundation/avaudiobitratestrategy_constant)Added [AVAudioBitRateStrategy_LongTermAverage](https://developer.apple.com/documentation/avfoundation/avaudiobitratestrategy_longtermaverage)Added [AVAudioBitRateStrategy_Variable](https://developer.apple.com/documentation/avfoundation/avaudiobitratestrategy_variable)Added [AVAudioBitRateStrategy_VariableConstrained](https://developer.apple.com/documentation/avfoundation/avaudiobitratestrategy_variableconstrained)Added [AVEncoderAudioQualityForVBRKey](https://developer.apple.com/documentation/avfoundation/avencoderaudioqualityforvbrkey)Added [AVEncoderBitRateStrategyKey](https://developer.apple.com/documentation/avfoundation/avencoderbitratestrategykey)Added [AVSampleRateConverterAlgorithmKey](https://developer.apple.com/documentation/avfoundation/avsamplerateconverteralgorithmkey)Added [AVSampleRateConverterAlgorithm_Mastering](https://developer.apple.com/documentation/avfoundation/avsamplerateconverteralgorithm_mastering)Added [AVSampleRateConverterAlgorithm_Normal](https://developer.apple.com/documentation/avfoundation/avsamplerateconverteralgorithm_normal)AVBase.hRemoved #def AVAILABLE_MAC_OS_X_VERSION_10_7_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_TBDAVCaptureDevice.hAdded [AVCaptureDevice.activeFormat](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1389221-activeformat)Added [AVCaptureDevice.activeVideoMaxFrameDuration](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1387816-activevideomaxframeduration)Added [AVCaptureDevice.activeVideoMinFrameDuration](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1389290-activevideominframeduration)Added [+[AVCaptureDevice authorizationStatusForMediaType:]](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624613-authorizationstatusformediatype)Added [AVCaptureDevice.autoFocusRangeRestriction](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624622-autofocusrangerestriction)Added [AVCaptureDevice.autoFocusRangeRestrictionSupported](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624570-isautofocusrangerestrictionsuppo)Added [-[AVCaptureDevice cancelVideoZoomRamp]](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624631-cancelvideozoomramp)Added [AVCaptureDevice.formats](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1388738-formats)Added [-[AVCaptureDevice rampToVideoZoomFactor:withRate:]](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624614-ramptovideozoomfactor)Added [AVCaptureDevice.rampingVideoZoom](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624588-rampingvideozoom)Added [+[AVCaptureDevice requestAccessForMediaType:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624584-requestaccess)Added [AVCaptureDevice.smoothAutoFocusEnabled](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624653-issmoothautofocusenabled)Added [AVCaptureDevice.smoothAutoFocusSupported](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624625-issmoothautofocussupported)Added [AVCaptureDevice.videoZoomFactor](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624611-videozoomfactor)Added [AVCaptureDeviceFormat](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format)Added [AVCaptureDeviceFormat.formatDescription](https://developer.apple.com/documentation/avfoundation/avcapturedeviceformat/1389445-formatdescription)Added [AVCaptureDeviceFormat.mediaType](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/1388503-mediatype)Added [AVCaptureDeviceFormat.videoBinned](https://developer.apple.com/documentation/avfoundation/avcapturedeviceformat/1624597-videobinned)Added [AVCaptureDeviceFormat.videoFieldOfView](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/1624569-videofieldofview)Added [AVCaptureDeviceFormat.videoMaxZoomFactor](https://developer.apple.com/documentation/avfoundation/avcapturedeviceformat/1624635-videomaxzoomfactor)Added [AVCaptureDeviceFormat.videoStabilizationSupported](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/1624634-isvideostabilizationsupported)Added [AVCaptureDeviceFormat.videoSupportedFrameRateRanges](https://developer.apple.com/documentation/avfoundation/avcapturedeviceformat/1387592-videosupportedframerateranges)Added [AVCaptureDeviceFormat.videoZoomFactorUpscaleThreshold](https://developer.apple.com/documentation/avfoundation/avcapturedeviceformat/1624638-videozoomfactorupscalethreshold)Added [AVFrameRateRange](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/avframeraterange)Added [AVFrameRateRange.maxFrameDuration](https://developer.apple.com/documentation/avfoundation/avframeraterange/1386786-maxframeduration)Added [AVFrameRateRange.maxFrameRate](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/avframeraterange/1386988-maxframerate)Added [AVFrameRateRange.minFrameDuration](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/avframeraterange/1388420-minframeduration)Added [AVFrameRateRange.minFrameRate](https://developer.apple.com/documentation/avfoundation/avframeraterange/1389132-minframerate)Added [AVAuthorizationStatus](https://developer.apple.com/documentation/avfoundation/avauthorizationstatus)Added [AVAuthorizationStatusAuthorized](https://developer.apple.com/documentation/avfoundation/avauthorizationstatus/avauthorizationstatusauthorized)Added [AVAuthorizationStatusDenied](https://developer.apple.com/documentation/avfoundation/avauthorizationstatus/denied)Added [AVAuthorizationStatusNotDetermined](https://developer.apple.com/documentation/avfoundation/avauthorizationstatus/notdetermined)Added [AVAuthorizationStatusRestricted](https://developer.apple.com/documentation/avfoundation/avauthorizationstatus/restricted)Added [AVCaptureAutoFocusRangeRestriction](https://developer.apple.com/documentation/avfoundation/avcaptureautofocusrangerestriction)Added [AVCaptureAutoFocusRangeRestrictionFar](https://developer.apple.com/documentation/avfoundation/avcapturedevice/autofocusrangerestriction/far)Added [AVCaptureAutoFocusRangeRestrictionNear](https://developer.apple.com/documentation/avfoundation/avcapturedevice/autofocusrangerestriction/near)Added [AVCaptureAutoFocusRangeRestrictionNone](https://developer.apple.com/documentation/avfoundation/avcapturedevice/autofocusrangerestriction/none)Added AVCaptureDevice(AVCaptureDeviceAuthorization)Added AVCaptureDevice(AVCaptureDeviceVideoZoom)AVCaptureInput.hAdded [AVCaptureInputPort.clock](https://developer.apple.com/documentation/avfoundation/avcaptureinput/port/1385908-clock)AVCaptureOutput.hRemoved [AVCaptureFileOutputDelegate](https://developer.apple.com/documentation/avfoundation/avcapturefileoutputdelegate)Added [-[AVCaptureAudioDataOutput recommendedAudioSettingsForAssetWriterWithOutputFileType:]](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutput/1616308-recommendedaudiosettingsforasset)Added [AVCaptureMetadataOutput.rectOfInterest](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/1616291-rectofinterest)Added [-[AVCaptureOutput metadataOutputRectOfInterestForRect:]](https://developer.apple.com/documentation/avfoundation/avcaptureoutput/1616304-metadataoutputrectconverted)Added [-[AVCaptureOutput rectForMetadataOutputRectOfInterest:]](https://developer.apple.com/documentation/avfoundation/avcaptureoutput/1616311-rectformetadataoutputrectofinter)Added [AVCaptureStillImageOutput.automaticallyEnablesStillImageStabilizationWhenAvailable](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616301-automaticallyenablesstillimagest)Added [AVCaptureStillImageOutput.stillImageStabilizationActive](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616297-isstillimagestabilizationactive)Added [AVCaptureStillImageOutput.stillImageStabilizationSupported](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616286-isstillimagestabilizationsupport)Added [-[AVCaptureVideoDataOutput recommendedVideoSettingsForAssetWriterWithOutputFileType:]](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1616290-recommendedvideosettingsforasset)AVCaptureSession.hRemoved [AVVideoFieldModeBoth](https://developer.apple.com/documentation/avfoundation/avvideofieldmode/avvideofieldmodeboth)Removed [AVVideoFieldModeBottomOnly](https://developer.apple.com/documentation/avfoundation/avvideofieldmode/avvideofieldmodebottomonly)Removed [AVVideoFieldModeDeinterlace](https://developer.apple.com/documentation/avfoundation/avvideofieldmode/avvideofieldmodedeinterlace)Removed [AVVideoFieldModeTopOnly](https://developer.apple.com/documentation/avfoundation/avvideofieldmode/avvideofieldmodetoponly)Added [AVCaptureSession.automaticallyConfiguresApplicationAudioSession](https://developer.apple.com/documentation/avfoundation/avcapturesession/1620477-automaticallyconfiguresapplicati)Added [AVCaptureSession.masterClock](https://developer.apple.com/documentation/avfoundation/avcapturesession/1388984-masterclock)Added [AVCaptureSession.usesApplicationAudioSession](https://developer.apple.com/documentation/avfoundation/avcapturesession/1620490-usesapplicationaudiosession)Added [AVCaptureSessionPresetInputPriority](https://developer.apple.com/documentation/avfoundation/avcapturesession/preset/1620473-inputpriority)Modified [AVCaptureConnection.supportsVideoMaxFrameDuration](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1389158-isvideomaxframedurationsupported)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [AVCaptureConnection.supportsVideoMinFrameDuration](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1386978-isvideominframedurationsupported)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [AVCaptureConnection.videoMaxFrameDuration](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1390246-videomaxframeduration)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [AVCaptureConnection.videoMinFrameDuration](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1388931-videominframeduration)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

AVCaptureVideoPreviewLayer.hAdded [-[AVCaptureVideoPreviewLayer metadataOutputRectOfInterestForRect:]](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/1623495-metadataoutputrectofinterestforr)Added [-[AVCaptureVideoPreviewLayer rectForMetadataOutputRectOfInterest:]](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/1623498-rectformetadataoutputrectofinter)AVError.hAdded [AVErrorApplicationIsNotAuthorizedToUseDevice](https://developer.apple.com/documentation/avfoundation/averror/code/applicationisnotauthorizedtousedevice)AVMediaFormat.hAdded [AVFileType3GPP2](https://developer.apple.com/documentation/avfoundation/avfiletype/1388141-mobile3gpp2)Added [AVFileTypeAC3](https://developer.apple.com/documentation/avfoundation/avfiletype/1390561-ac3)Added [AVFileTypeMPEGLayer3](https://developer.apple.com/documentation/avfoundation/avfiletype/1390512-mp3)Added [AVFileTypeSunAU](https://developer.apple.com/documentation/avfoundation/avfiletype/1386050-au)AVMediaSelectionGroup.hAdded [AVMediaSelectionOption.displayName](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1388485-displayname)Added [-[AVMediaSelectionOption displayNameWithLocale:]](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1388021-displaynamewithlocale)Added [AVMediaSelectionOption.extendedLanguageTag](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1387619-extendedlanguagetag)AVMetadataFormat.hAdded [AVMetadata3GPUserDataKeyAlbumAndTrack](https://developer.apple.com/documentation/avfoundation/avmetadata3gpuserdatakeyalbumandtrack)Added [AVMetadata3GPUserDataKeyCollection](https://developer.apple.com/documentation/avfoundation/avmetadata3gpuserdatakeycollection)Added [AVMetadata3GPUserDataKeyKeywordList](https://developer.apple.com/documentation/avfoundation/avmetadatakey/1390852-metadata3gpuserdatakeykeywordlis)Added [AVMetadata3GPUserDataKeyMediaClassification](https://developer.apple.com/documentation/avfoundation/avmetadatakey/1390882-metadata3gpuserdatakeymediaclass)Added [AVMetadata3GPUserDataKeyMediaRating](https://developer.apple.com/documentation/avfoundation/avmetadatakey/1385980-metadata3gpuserdatakeymediaratin)Added [AVMetadata3GPUserDataKeyThumbnail](https://developer.apple.com/documentation/avfoundation/avmetadata3gpuserdatakeythumbnail)Added [AVMetadata3GPUserDataKeyUserRating](https://developer.apple.com/documentation/avfoundation/avmetadata3gpuserdatakeyuserrating)Added [AVMetadataFormatISOUserData](https://developer.apple.com/documentation/avfoundation/avmetadataformat/1389879-isouserdata)Added [AVMetadataKeySpaceISOUserData](https://developer.apple.com/documentation/avfoundation/avmetadatakeyspaceisouserdata)AVMetadataItem.hAdded [+[AVMetadataItem metadataItemsFromArray:filteredByMetadataItemFilter:]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1390238-metadataitemsfromarray)Added [AVMetadataItemFilter](https://developer.apple.com/documentation/avfoundation/avmetadataitemfilter)Added [+[AVMetadataItemFilter metadataItemFilterForSharing]](https://developer.apple.com/documentation/avfoundation/avmetadataitemfilter/1387905-forsharing)AVMetadataObject.hAdded [AVMetadataMachineReadableCodeObject](https://developer.apple.com/documentation/avfoundation/avmetadatamachinereadablecodeobject)Added [AVMetadataMachineReadableCodeObject.corners](https://developer.apple.com/documentation/avfoundation/avmetadatamachinereadablecodeobject/1618815-corners)Added [AVMetadataMachineReadableCodeObject.stringValue](https://developer.apple.com/documentation/avfoundation/avmetadatamachinereadablecodeobject/1618800-stringvalue)Added [AVMetadataObjectTypeAztecCode](https://developer.apple.com/documentation/avfoundation/avmetadataobject/objecttype/1618809-aztec)Added [AVMetadataObjectTypeCode128Code](https://developer.apple.com/documentation/avfoundation/avmetadataobject/objecttype/1618817-code128)Added [AVMetadataObjectTypeCode39Code](https://developer.apple.com/documentation/avfoundation/avmetadataobject/objecttype/1618814-code39)Added [AVMetadataObjectTypeCode39Mod43Code](https://developer.apple.com/documentation/avfoundation/avmetadataobjecttypecode39mod43code)Added [AVMetadataObjectTypeCode93Code](https://developer.apple.com/documentation/avfoundation/avmetadataobject/objecttype/1618829-code93)Added [AVMetadataObjectTypeEAN13Code](https://developer.apple.com/documentation/avfoundation/avmetadataobjecttypeean13code)Added [AVMetadataObjectTypeEAN8Code](https://developer.apple.com/documentation/avfoundation/avmetadataobjecttypeean8code)Added [AVMetadataObjectTypePDF417Code](https://developer.apple.com/documentation/avfoundation/avmetadataobjecttypepdf417code)Added [AVMetadataObjectTypeQRCode](https://developer.apple.com/documentation/avfoundation/avmetadataobject/objecttype/1618819-qr)Added [AVMetadataObjectTypeUPCECode](https://developer.apple.com/documentation/avfoundation/avmetadataobjecttypeupcecode)AVOutputSettingsAssistant.hAdded [AVOutputSettingsAssistant](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant)Added [AVOutputSettingsAssistant.audioSettings](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1386233-audiosettings)Added [+[AVOutputSettingsAssistant availableOutputSettingsPresets]](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1388118-availableoutputsettingspresets)Added [AVOutputSettingsAssistant.outputFileType](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1390842-outputfiletype)Added [+[AVOutputSettingsAssistant outputSettingsAssistantWithPreset:]](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1387909-outputsettingsassistantwithprese)Added [AVOutputSettingsAssistant.sourceAudioFormat](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1390673-sourceaudioformat)Added [AVOutputSettingsAssistant.sourceVideoAverageFrameDuration](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1387414-sourcevideoaverageframeduration)Added [AVOutputSettingsAssistant.sourceVideoFormat](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1387885-sourcevideoformat)Added [AVOutputSettingsAssistant.sourceVideoMinFrameDuration](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1386812-sourcevideominframeduration)Added [AVOutputSettingsAssistant.videoSettings](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1386880-videosettings)Added AVOutputSettingsAssistant(AVOutputSettingsAssistant_SourceInformation)Added [AVOutputSettingsPreset1280x720](https://developer.apple.com/documentation/avfoundation/avoutputsettingspreset/1390506-preset1280x720)Added [AVOutputSettingsPreset1920x1080](https://developer.apple.com/documentation/avfoundation/avoutputsettingspreset1920x1080)Added [AVOutputSettingsPreset640x480](https://developer.apple.com/documentation/avfoundation/avoutputsettingspreset/1389392-preset640x480)Added [AVOutputSettingsPreset960x540](https://developer.apple.com/documentation/avfoundation/avoutputsettingspreset/1390817-preset960x540)AVPlayer.hAdded [AVPlayer.appliesMediaSelectionCriteriaAutomatically](https://developer.apple.com/documentation/avfoundation/avplayer/1387178-appliesmediaselectioncriteriaaut)Added [-[AVPlayer mediaSelectionCriteriaForMediaCharacteristic:]](https://developer.apple.com/documentation/avfoundation/avplayer/1387825-mediaselectioncriteriaformediach)Added [AVPlayer.muted](https://developer.apple.com/documentation/avfoundation/avplayer/1387544-ismuted)Added [-[AVPlayer setMediaSelectionCriteria:forMediaCharacteristic:]](https://developer.apple.com/documentation/avfoundation/avplayer/1390563-setmediaselectioncriteria)Added [AVPlayer.volume](https://developer.apple.com/documentation/avfoundation/avplayer/1390127-volume)Added AVPlayer(AVPlayerAudioDeviceSupport)Added AVPlayer(AVPlayerAutomaticMediaSelection)AVPlayerItem.hRemoved AVPlayerItem(AVPlayerItemPresentation)Added [AVPlayerItem.audioTimePitchAlgorithm](https://developer.apple.com/documentation/avfoundation/avplayeritem/1385855-audiotimepitchalgorithm)Added [AVPlayerItem.automaticallyLoadedAssetKeys](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388633-automaticallyloadedassetkeys)Added [AVPlayerItem.customVideoCompositor](https://developer.apple.com/documentation/avfoundation/avplayeritem/1390669-customvideocompositor)Added [-[AVPlayerItem initWithAsset:automaticallyLoadedAssetKeys:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1387529-initwithasset)Added [+[AVPlayerItem playerItemWithAsset:automaticallyLoadedAssetKeys:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1588088-playeritemwithasset)Added [-[AVPlayerItem selectMediaOptionAutomaticallyInMediaSelectionGroup:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388268-selectmediaoptionautomaticallyin)Added [AVPlayerItemAccessLogEvent.downloadOverdue](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1389213-downloadoverdue)Added [AVPlayerItemAccessLogEvent.mediaRequestsWWAN](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1388549-mediarequestswwan)Added [AVPlayerItemAccessLogEvent.observedBitrateStandardDeviation](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1386094-observedbitratestandarddeviation)Added [AVPlayerItemAccessLogEvent.observedMaxBitrate](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1386714-observedmaxbitrate)Added [AVPlayerItemAccessLogEvent.observedMinBitrate](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1390173-observedminbitrate)Added [AVPlayerItemAccessLogEvent.playbackType](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1387218-playbacktype)Added [AVPlayerItemAccessLogEvent.startupTime](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1389138-startuptime)Added [AVPlayerItemAccessLogEvent.switchBitrate](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1390645-switchbitrate)Added [AVPlayerItemAccessLogEvent.transferDuration](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1387370-transferduration)Added AVPlayerItem(AVPlayerItemAudioProcessing)Added AVPlayerItem(AVPlayerItemVisualPresentation)Modified [AVPlayerItemAccessLogEvent.numberOfSegmentsDownloaded](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1588090-numberofsegmentsdownloaded)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

AVPlayerItemOutput.hAdded [AVPlayerItemLegibleOutput](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput)Added [AVPlayerItemLegibleOutput.advanceIntervalForDelegateInvocation](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/1388098-advanceintervalfordelegateinvoca)Added [AVPlayerItemLegibleOutput.delegate](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/1387877-delegate)Added [AVPlayerItemLegibleOutput.delegateQueue](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/1386275-delegatequeue)Added [-[AVPlayerItemLegibleOutput initWithMediaSubtypesForNativeRepresentation:]](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/1390500-init)Added [-[AVPlayerItemLegibleOutput setDelegate:queue:]](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/1386204-setdelegate)Added [AVPlayerItemLegibleOutput.textStylingResolution](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/1385803-textstylingresolution)Added [AVPlayerItemLegibleOutputPushDelegate](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutputpushdelegate)Added [-[AVPlayerItemLegibleOutputPushDelegate legibleOutput:didOutputAttributedStrings:nativeSampleBuffers:forItemTime:]](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutputpushdelegate/1386790-legibleoutput)Added [AVPlayerItemOutputPushDelegate](https://developer.apple.com/documentation/avfoundation/avplayeritemoutputpushdelegate)Added [-[AVPlayerItemOutputPushDelegate outputSequenceWasFlushed:]](https://developer.apple.com/documentation/avfoundation/avplayeritemoutputpushdelegate/1390224-outputsequencewasflushed)Added AVPlayerItemLegibleOutput(AVPlayerItemLegibleOutput_NativeRepresentation)Added AVPlayerItemLegibleOutput(AVPlayerItemLegibleOutput_TextStylingResolution)Added [AVPlayerItemLegibleOutputTextStylingResolutionDefault](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutputtextstylingresolutiondefault)Added [AVPlayerItemLegibleOutputTextStylingResolutionSourceAndRulesOnly](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/textstylingresolution/1389666-sourceandrulesonly)AVPlayerItemTrack.hAdded [AVPlayerItemTrack.currentVideoFrameRate](https://developer.apple.com/documentation/avfoundation/avplayeritemtrack/1388956-currentvideoframerate)AVPlayerLayer.hAdded [AVPlayerLayer.videoRect](https://developer.apple.com/documentation/avfoundation/avplayerlayer/1385745-videorect)AVPlayerMediaSelectionCriteria.hAdded [AVPlayerMediaSelectionCriteria](https://developer.apple.com/documentation/avfoundation/avplayermediaselectioncriteria)Added [-[AVPlayerMediaSelectionCriteria initWithPreferredLanguages:preferredMediaCharacteristics:]](https://developer.apple.com/documentation/avfoundation/avplayermediaselectioncriteria/1387627-initwithpreferredlanguages)Added [AVPlayerMediaSelectionCriteria.preferredLanguages](https://developer.apple.com/documentation/avfoundation/avplayermediaselectioncriteria/1388559-preferredlanguages)Added [AVPlayerMediaSelectionCriteria.preferredMediaCharacteristics](https://developer.apple.com/documentation/avfoundation/avplayermediaselectioncriteria/1385734-preferredmediacharacteristics)AVSpeechSynthesis.hAdded [AVSpeechSynthesisVoice](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice)Added [+[AVSpeechSynthesisVoice currentLanguageCode]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619707-currentlanguagecode)Added [AVSpeechSynthesisVoice.language](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619698-language)Added [+[AVSpeechSynthesisVoice speechVoices]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619697-speechvoices)Added [+[AVSpeechSynthesisVoice voiceWithLanguage:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619699-init)Added [AVSpeechSynthesizer](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer)Added [-[AVSpeechSynthesizer continueSpeaking]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619704-continuespeaking)Added [AVSpeechSynthesizer.delegate](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619709-delegate)Added [-[AVSpeechSynthesizer pauseSpeakingAtBoundary:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619689-pausespeakingatboundary)Added [AVSpeechSynthesizer.paused](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619692-paused)Added [-[AVSpeechSynthesizer speakUtterance:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619686-speak)Added [AVSpeechSynthesizer.speaking](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619680-isspeaking)Added [-[AVSpeechSynthesizer stopSpeakingAtBoundary:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619676-stopspeakingatboundary)Added [AVSpeechSynthesizerDelegate](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate)Added [-[AVSpeechSynthesizerDelegate speechSynthesizer:didCancelSpeechUtterance:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619678-speechsynthesizer)Added [-[AVSpeechSynthesizerDelegate speechSynthesizer:didContinueSpeechUtterance:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619677-speechsynthesizer)Added [-[AVSpeechSynthesizerDelegate speechSynthesizer:didFinishSpeechUtterance:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619700-speechsynthesizer)Added [-[AVSpeechSynthesizerDelegate speechSynthesizer:didPauseSpeechUtterance:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619675-speechsynthesizer)Added [-[AVSpeechSynthesizerDelegate speechSynthesizer:didStartSpeechUtterance:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619701-speechsynthesizer)Added [-[AVSpeechSynthesizerDelegate speechSynthesizer:willSpeakRangeOfSpeechString:utterance:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619681-speechsynthesizer)Added [AVSpeechUtterance](https://developer.apple.com/documentation/avfoundation/avspeechutterance)Added [-[AVSpeechUtterance initWithString:]](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619684-init)Added [AVSpeechUtterance.pitchMultiplier](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619683-pitchmultiplier)Added [AVSpeechUtterance.postUtteranceDelay](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619694-postutterancedelay)Added [AVSpeechUtterance.preUtteranceDelay](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619679-preutterancedelay)Added [AVSpeechUtterance.rate](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619708-rate)Added [AVSpeechUtterance.speechString](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619702-speechstring)Added [+[AVSpeechUtterance speechUtteranceWithString:]](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619668-speechutterancewithstring)Added [AVSpeechUtterance.voice](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619710-voice)Added [AVSpeechUtterance.volume](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619687-volume)Added [AVSpeechBoundary](https://developer.apple.com/documentation/avfoundation/avspeechboundary)Added [AVSpeechBoundaryImmediate](https://developer.apple.com/documentation/avfoundation/avspeechboundary/avspeechboundaryimmediate)Added [AVSpeechBoundaryWord](https://developer.apple.com/documentation/avfoundation/avspeechboundary/avspeechboundaryword)Added [AVSpeechUtteranceDefaultSpeechRate](https://developer.apple.com/documentation/avfoundation/avspeechutterancedefaultspeechrate)Added [AVSpeechUtteranceMaximumSpeechRate](https://developer.apple.com/documentation/avfoundation/avspeechutterancemaximumspeechrate)Added [AVSpeechUtteranceMinimumSpeechRate](https://developer.apple.com/documentation/avfoundation/avspeechutteranceminimumspeechrate)AVVideoCompositing.hAdded [AVAsynchronousVideoCompositionRequest](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest)Added [AVAsynchronousVideoCompositionRequest.compositionTime](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/1386888-compositiontime)Added [-[AVAsynchronousVideoCompositionRequest finishCancelledRequest]](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/1386261-finishcancelledrequest)Added [-[AVAsynchronousVideoCompositionRequest finishWithComposedVideoFrame:]](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/1387450-finish)Added [-[AVAsynchronousVideoCompositionRequest finishWithError:]](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/1390797-finish)Added [AVAsynchronousVideoCompositionRequest.renderContext](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/1389112-rendercontext)Added [-[AVAsynchronousVideoCompositionRequest sourceFrameByTrackID:]](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/1390379-sourceframebytrackid)Added [AVAsynchronousVideoCompositionRequest.sourceTrackIDs](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/1388898-sourcetrackids)Added [AVAsynchronousVideoCompositionRequest.videoCompositionInstruction](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/1386672-videocompositioninstruction)Added [AVVideoCompositing](https://developer.apple.com/documentation/avfoundation/avvideocompositing)Added [-[AVVideoCompositing cancelAllPendingVideoCompositionRequests]](https://developer.apple.com/documentation/avfoundation/avvideocompositing/1390659-cancelallpendingvideocomposition)Added [-[AVVideoCompositing renderContextChanged:]](https://developer.apple.com/documentation/avfoundation/avvideocompositing/1390363-rendercontextchanged)Added [AVVideoCompositing.requiredPixelBufferAttributesForRenderContext](https://developer.apple.com/documentation/avfoundation/avvideocompositing/1386414-requiredpixelbufferattributesfor)Added [AVVideoCompositing.sourcePixelBufferAttributes](https://developer.apple.com/documentation/avfoundation/avvideocompositing/1388610-sourcepixelbufferattributes)Added [-[AVVideoCompositing startVideoCompositionRequest:]](https://developer.apple.com/documentation/avfoundation/avvideocompositing/1388894-startrequest)Added [AVVideoCompositionInstruction](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstructionprotocol)Added [AVVideoCompositionInstruction.containsTweening](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstructionprotocol/1389376-containstweening)Added [AVVideoCompositionInstruction.enablePostProcessing](https://developer.apple.com/documentation/avfoundation/1386654-avvideocompositioninstruction/1386216-enablepostprocessing)Added [AVVideoCompositionInstruction.passthroughTrackID](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstructionprotocol/1389919-passthroughtrackid)Added [AVVideoCompositionInstruction.requiredSourceTrackIDs](https://developer.apple.com/documentation/avfoundation/1386654-avvideocompositioninstruction/1388661-requiredsourcetrackids)Added [AVVideoCompositionInstruction.timeRange](https://developer.apple.com/documentation/avfoundation/1386654-avvideocompositioninstruction/1389873-timerange)Added [AVVideoCompositionRenderContext](https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext)Added [AVVideoCompositionRenderContext.edgeWidths](https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext/1387026-edgewidths)Added [AVVideoCompositionRenderContext.highQualityRendering](https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext/1388758-highqualityrendering)Added [-[AVVideoCompositionRenderContext newPixelBuffer]](https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext/1386802-newpixelbuffer)Added [AVVideoCompositionRenderContext.pixelAspectRatio](https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext/1389800-pixelaspectratio)Added [AVVideoCompositionRenderContext.renderScale](https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext/1387408-renderscale)Added [AVVideoCompositionRenderContext.renderTransform](https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext/1389831-rendertransform)Added [AVVideoCompositionRenderContext.size](https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext/1389718-size)Added [AVVideoCompositionRenderContext.videoComposition](https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext/1390647-videocomposition)Added [AVEdgeWidths](https://developer.apple.com/documentation/avfoundation/avedgewidths)Added [AVPixelAspectRatio](https://developer.apple.com/documentation/avfoundation/avpixelaspectratio)AVVideoComposition.hAdded [AVMutableVideoComposition.customVideoCompositorClass](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/1390649-customvideocompositorclass)Added [+[AVMutableVideoComposition videoCompositionWithPropertiesOfAsset:]](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/1388430-videocompositionwithpropertiesof)Added [-[AVMutableVideoCompositionLayerInstruction setCropRectangle:atTime:]](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/1387402-setcroprectangle)Added [-[AVMutableVideoCompositionLayerInstruction setCropRectangleRampFromStartCropRectangle:toEndCropRectangle:timeRange:]](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/1385677-setcroprectangleramp)Added [AVVideoComposition.customVideoCompositorClass](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1389622-customvideocompositorclass)Added [+[AVVideoCompositionCoreAnimationTool videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayers:inLayer:]](https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool/1389778-init)Added [AVVideoCompositionInstruction.passthroughTrackID](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction/1387657-passthroughtrackid)Added [AVVideoCompositionInstruction.requiredSourceTrackIDs](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction/1390913-requiredsourcetrackids)Added [-[AVVideoCompositionLayerInstruction getCropRectangleRampForTime:startCropRectangle:endCropRectangle:timeRange:]](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/1387998-getcroprectanglerampfortime)Modified [AVVideoCompositionInstruction](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSMutableCopying |
| To | AVVideoCompositionInstruction, NSCopying, NSMutableCopying, NSSecureCoding |

Modified [AVVideoCompositionLayerInstruction](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSMutableCopying |
| To | NSCopying, NSMutableCopying, NSSecureCoding |

Modified [-[AVVideoCompositionValidationHandling videoComposition:shouldContinueValidatingAfterFindingInvalidTimeRangeInInstruction:]](https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling/1390721-videocomposition)

|  | Declaration |
| --- | --- |
| From | - (BOOL)videoComposition:(AVVideoComposition \*)videoComposition shouldContinueValidatingAfterFindingInvalidTimeRangeInInstruction:(AVVideoCompositionInstruction \*)videoCompositionInstruction |
| To | - (BOOL)videoComposition:(AVVideoComposition \*)videoComposition shouldContinueValidatingAfterFindingInvalidTimeRangeInInstruction:(id<AVVideoCompositionInstruction>)videoCompositionInstruction |

Modified [-[AVVideoCompositionValidationHandling videoComposition:shouldContinueValidatingAfterFindingInvalidTrackIDInInstruction:layerInstruction:asset:]](https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling/1388452-videocomposition)

|  | Declaration |
| --- | --- |
| From | - (BOOL)videoComposition:(AVVideoComposition \*)videoComposition shouldContinueValidatingAfterFindingInvalidTrackIDInInstruction:(AVVideoCompositionInstruction \*)videoCompositionInstruction layerInstruction:(AVVideoCompositionLayerInstruction \*)layerInstruction asset:(AVAsset \*)asset |
| To | - (BOOL)videoComposition:(AVVideoComposition \*)videoComposition shouldContinueValidatingAfterFindingInvalidTrackIDInInstruction:(id<AVVideoCompositionInstruction>)videoCompositionInstruction layerInstruction:(AVVideoCompositionLayerInstruction \*)layerInstruction asset:(AVAsset \*)asset |

AVVideoSettings.hAdded [AVVideoAllowFrameReorderingKey](https://developer.apple.com/documentation/avfoundation/avvideoallowframereorderingkey)Added [AVVideoAverageNonDroppableFrameRateKey](https://developer.apple.com/documentation/avfoundation/avvideoaveragenondroppableframeratekey)Added [AVVideoExpectedSourceFrameRateKey](https://developer.apple.com/documentation/avfoundation/avvideoexpectedsourceframeratekey)Added [AVVideoH264EntropyModeCABAC](https://developer.apple.com/documentation/avfoundation/avvideoh264entropymodecabac)Added [AVVideoH264EntropyModeCAVLC](https://developer.apple.com/documentation/avfoundation/avvideoh264entropymodecavlc)Added [AVVideoH264EntropyModeKey](https://developer.apple.com/documentation/avfoundation/avvideoh264entropymodekey)Added [AVVideoMaxKeyFrameIntervalDurationKey](https://developer.apple.com/documentation/avfoundation/avvideomaxkeyframeintervaldurationkey)Added [AVVideoProfileLevelH264BaselineAutoLevel](https://developer.apple.com/documentation/avfoundation/avvideoprofilelevelh264baselineautolevel)Added [AVVideoProfileLevelH264HighAutoLevel](https://developer.apple.com/documentation/avfoundation/avvideoprofilelevelh264highautolevel)Added [AVVideoProfileLevelH264MainAutoLevel](https://developer.apple.com/documentation/avfoundation/avvideoprofilelevelh264mainautolevel)

## CFNetwork

CFHTTPMessage.hAdded kCFHTTPAuthenticationSchemeOAuth1Modified [CFHTTPMessageCopySerializedMessage()](https://developer.apple.com/documentation/cfnetwork/1387278-cfhttpmessagecopyserializedmessa)

|  | Declaration |
| --- | --- |
| From | CFDataRef CFHTTPMessageCopySerializedMessage ( CFHTTPMessageRef request); |
| To | CFDataRef CFHTTPMessageCopySerializedMessage ( CFHTTPMessageRef message); |

## CoreAudio

CoreAudioTypes.hAdded [kAudioChannelLayoutTag_AAC_7_1_C](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_aac_7_1_c)Added [kAudio_BadFilePathError](https://developer.apple.com/documentation/coreaudio/kaudio_badfilepatherror)Added [kAudio_FilePermissionError](https://developer.apple.com/documentation/coreaudio/1572099-anonymous/kaudio_filepermissionerror)Added [kAudio_TooManyFilesOpenError](https://developer.apple.com/documentation/coreaudio/1572099-anonymous/kaudio_toomanyfilesopenerror)

## CoreBluetooth

CBAdvertisementData.hAdded [CBAdvertisementDataIsConnectable](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdataisconnectable)Added [CBAdvertisementDataSolicitedServiceUUIDsKey](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdatasolicitedserviceuuidskey)CBCentral.hAdded CBCentral.identifierAdded [CBCentral.maximumUpdateValueLength](https://developer.apple.com/documentation/corebluetooth/cbcentral/1408800-maximumupdatevaluelength)Modified CBCentral.UUID

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

CBCentralManager.hAdded [-[CBCentralManager initWithDelegate:queue:options:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1519001-init)Added [-[CBCentralManager retrieveConnectedPeripheralsWithServices:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518924-retrieveconnectedperipheralswith)Added [-[CBCentralManager retrievePeripheralsWithIdentifiers:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1519127-retrieveperipheralswithidentifie)Added [-[CBCentralManagerDelegate centralManager:willRestoreState:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518819-centralmanager)Modified [CBCentralManager.delegate](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518944-delegate)

|  | Declaration |
| --- | --- |
| From | @property(assign, nonatomic) id<CBCentralManagerDelegate> delegate |
| To | @property(weak, nonatomic) id<CBCentralManagerDelegate> delegate |

Modified -[CBCentralManager retrieveConnectedPeripherals]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified -[CBCentralManager retrievePeripherals:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [CBCentralManagerScanOptionAllowDuplicatesKey](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerscanoptionallowduplicateskey)

|  | Header |
| --- | --- |
| From | CoreBluetooth/CBCentralManager.h |
| To | CoreBluetooth/CBCentralManagerConstants.h |

Modified [CBConnectPeripheralOptionNotifyOnConnectionKey](https://developer.apple.com/documentation/corebluetooth/cbconnectperipheraloptionnotifyonconnectionkey)

|  | Header |
| --- | --- |
| From | CoreBluetooth/CBCentralManager.h |
| To | CoreBluetooth/CBCentralManagerConstants.h |

Modified [CBConnectPeripheralOptionNotifyOnDisconnectionKey](https://developer.apple.com/documentation/corebluetooth/cbconnectperipheraloptionnotifyondisconnectionkey)

|  | Header |
| --- | --- |
| From | CoreBluetooth/CBCentralManager.h |
| To | CoreBluetooth/CBCentralManagerConstants.h |

Modified [CBConnectPeripheralOptionNotifyOnNotificationKey](https://developer.apple.com/documentation/corebluetooth/cbconnectperipheraloptionnotifyonnotificationkey)

|  | Header |
| --- | --- |
| From | CoreBluetooth/CBCentralManager.h |
| To | CoreBluetooth/CBCentralManagerConstants.h |

CBCentralManagerConstants.hAdded [CBCentralManagerOptionRestoreIdentifierKey](https://developer.apple.com/documentation/corebluetooth/cbcentralmanageroptionrestoreidentifierkey)Added [CBCentralManagerOptionShowPowerAlertKey](https://developer.apple.com/documentation/corebluetooth/cbcentralmanageroptionshowpoweralertkey)Added [CBCentralManagerRestoredStatePeripheralsKey](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerrestoredstateperipheralskey)Added [CBCentralManagerRestoredStateScanOptionsKey](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerrestoredstatescanoptionskey)Added [CBCentralManagerRestoredStateScanServicesKey](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerrestoredstatescanserviceskey)Added [CBCentralManagerScanOptionSolicitedServiceUUIDsKey](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerscanoptionsolicitedserviceuuidskey)Modified [CBCentralManagerScanOptionAllowDuplicatesKey](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerscanoptionallowduplicateskey)

|  | Header |
| --- | --- |
| From | CoreBluetooth/CBCentralManager.h |
| To | CoreBluetooth/CBCentralManagerConstants.h |

Modified [CBConnectPeripheralOptionNotifyOnConnectionKey](https://developer.apple.com/documentation/corebluetooth/cbconnectperipheraloptionnotifyonconnectionkey)

|  | Header |
| --- | --- |
| From | CoreBluetooth/CBCentralManager.h |
| To | CoreBluetooth/CBCentralManagerConstants.h |

Modified [CBConnectPeripheralOptionNotifyOnDisconnectionKey](https://developer.apple.com/documentation/corebluetooth/cbconnectperipheraloptionnotifyondisconnectionkey)

|  | Header |
| --- | --- |
| From | CoreBluetooth/CBCentralManager.h |
| To | CoreBluetooth/CBCentralManagerConstants.h |

Modified [CBConnectPeripheralOptionNotifyOnNotificationKey](https://developer.apple.com/documentation/corebluetooth/cbconnectperipheraloptionnotifyonnotificationkey)

|  | Header |
| --- | --- |
| From | CoreBluetooth/CBCentralManager.h |
| To | CoreBluetooth/CBCentralManagerConstants.h |

CBCharacteristic.hAdded [CBMutableCharacteristic.subscribedCentrals](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic/1518926-subscribedcentrals)Modified [CBCharacteristic.service](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/1518728-service)

|  | Declaration |
| --- | --- |
| From | @property(readonly, nonatomic) CBService \*service |
| To | @property(weak, readonly, nonatomic) CBService \*service |

CBDescriptor.hModified [CBDescriptor.characteristic](https://developer.apple.com/documentation/corebluetooth/cbdescriptor/1519035-characteristic)

|  | Declaration |
| --- | --- |
| From | @property(readonly, nonatomic) CBCharacteristic \*characteristic |
| To | @property(weak, readonly, nonatomic) CBCharacteristic \*characteristic |

CBPeripheral.hAdded CBPeripheral.identifierAdded [CBPeripheral.state](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1519113-state)Added [-[CBPeripheralDelegate peripheral:didModifyServices:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518865-peripheral)Added [CBPeripheralState](https://developer.apple.com/documentation/corebluetooth/cbperipheralstate)Added [CBPeripheralStateConnected](https://developer.apple.com/documentation/corebluetooth/cbperipheralstate/cbperipheralstateconnected)Added [CBPeripheralStateConnecting](https://developer.apple.com/documentation/corebluetooth/cbperipheralstate/cbperipheralstateconnecting)Added [CBPeripheralStateDisconnected](https://developer.apple.com/documentation/corebluetooth/cbperipheralstate/disconnected)Modified [CBPeripheral](https://developer.apple.com/documentation/corebluetooth/cbperipheral)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCopying |

Modified CBPeripheral.UUID

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [CBPeripheral.delegate](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518730-delegate)

|  | Declaration |
| --- | --- |
| From | @property(assign, nonatomic) id<CBPeripheralDelegate> delegate |
| To | @property(weak, nonatomic) id<CBPeripheralDelegate> delegate |

Modified CBPeripheral.isConnected

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[CBPeripheralDelegate peripheralDidInvalidateServices:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1805265-peripheraldidinvalidateservices)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

CBPeripheralManager.hAdded [+[CBPeripheralManager authorizationStatus]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1616317-authorizationstatus)Added [-[CBPeripheralManager initWithDelegate:queue:options:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393295-init)Added [-[CBPeripheralManagerDelegate peripheralManager:willRestoreState:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393317-peripheralmanager)Added [CBPeripheralManagerAuthorizationStatus](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerauthorizationstatus)Added [CBPeripheralManagerAuthorizationStatusAuthorized](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerauthorizationstatus/cbperipheralmanagerauthorizationstatusauthorized)Added [CBPeripheralManagerAuthorizationStatusDenied](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerauthorizationstatus/cbperipheralmanagerauthorizationstatusdenied)Added [CBPeripheralManagerAuthorizationStatusNotDetermined](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerauthorizationstatus/cbperipheralmanagerauthorizationstatusnotdetermined)Added [CBPeripheralManagerAuthorizationStatusRestricted](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerauthorizationstatus/restricted)Modified [CBPeripheralManager.delegate](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393313-delegate)

|  | Declaration |
| --- | --- |
| From | @property(assign, nonatomic) id<CBPeripheralManagerDelegate> delegate |
| To | @property(weak, nonatomic) id<CBPeripheralManagerDelegate> delegate |

CBPeripheralManagerConstants.hAdded [CBPeripheralManagerOptionRestoreIdentifierKey](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanageroptionrestoreidentifierkey)Added [CBPeripheralManagerOptionShowPowerAlertKey](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanageroptionshowpoweralertkey)Added [CBPeripheralManagerRestoredStateAdvertisementDataKey](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerrestoredstateadvertisementdatakey)Added [CBPeripheralManagerRestoredStateServicesKey](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerrestoredstateserviceskey)CBService.hModified [CBService.peripheral](https://developer.apple.com/documentation/corebluetooth/cbservice/1434334-peripheral)

|  | Declaration |
| --- | --- |
| From | @property(readonly, nonatomic) CBPeripheral \*peripheral |
| To | @property(weak, readonly, nonatomic) CBPeripheral \*peripheral |

CBUUID.hAdded [+[CBUUID UUIDWithNSUUID:]](https://developer.apple.com/documentation/corebluetooth/cbuuid/1518783-init)Modified CBUUIDAppearanceString

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified CBUUIDDeviceNameString

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified CBUUIDGenericAccessProfileString

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified CBUUIDGenericAttributeProfileString

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified CBUUIDPeripheralPreferredConnectionParametersString

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified CBUUIDPeripheralPrivacyFlagString

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified CBUUIDReconnectionAddressString

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified CBUUIDServiceChangedString

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

## CoreData

CoreDataDefines.hAdded [#def NSCoreDataVersionNumber10_7_4](https://developer.apple.com/documentation/coredata/nscoredataversionnumber10_7_4)Added [#def NSCoreDataVersionNumber10_8](https://developer.apple.com/documentation/coredata/nscoredataversionnumber10_8)Added [#def NSCoreDataVersionNumber10_8_2](https://developer.apple.com/documentation/coredata/nscoredataversionnumber10_8_2)Added [#def NSCoreDataVersionNumber_iPhoneOS_6_0](https://developer.apple.com/documentation/coredata/nscoredataversionnumber_iphoneos_6_0)NSPersistentStoreCoordinator.hAdded [+[NSPersistentStoreCoordinator removeUbiquitousContentAndPersistentStoreAtURL:options:error:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468923-removeubiquitouscontentandpersis)Added [NSPersistentStoreCoordinatorStoresWillChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1468800-nspersistentstorecoordinatorstor)Added [NSPersistentStoreRebuildFromUbiquitousContentOption](https://developer.apple.com/documentation/coredata/nspersistentstorerebuildfromubiquitouscontentoption)Added [NSPersistentStoreRemoveUbiquitousMetadataOption](https://developer.apple.com/documentation/coredata/nspersistentstoreremoveubiquitousmetadataoption)Added [NSPersistentStoreUbiquitousContainerIdentifierKey](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitouscontaineridentifierkey)Added [NSPersistentStoreUbiquitousPeerTokenOption](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitouspeertokenoption)Added [NSPersistentStoreUbiquitousTransitionType](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitoustransitiontype)Added [NSPersistentStoreUbiquitousTransitionTypeAccountAdded](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitoustransitiontype/accountadded)Added [NSPersistentStoreUbiquitousTransitionTypeAccountRemoved](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitoustransitiontype/accountremoved)Added [NSPersistentStoreUbiquitousTransitionTypeContentRemoved](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitoustransitiontype/contentremoved)Added [NSPersistentStoreUbiquitousTransitionTypeInitialImportCompleted](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitoustransitiontype/initialimportcompleted)Added [NSPersistentStoreUbiquitousTransitionTypeKey](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitoustransitiontypekey)

## CoreFoundation

CFAvailability.hModified #def CF_AVAILABLE_IOS

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_DEPRECATED_IOS

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM_AVAILABLE

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM_AVAILABLE_IOS

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM_AVAILABLE_MAC

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM_DEPRECATED

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM_DEPRECATED_IOS

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM_DEPRECATED_MAC

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_OPTIONS

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

CFBase.hAdded [CFAutorelease()](https://developer.apple.com/documentation/corefoundation/1521271-cfautorelease)Added [#def kCFCoreFoundationVersionNumber10_7_5](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_7_5)Added [#def kCFCoreFoundationVersionNumber10_8](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_8)Added [#def kCFCoreFoundationVersionNumber10_8_1](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_8_1)Added [#def kCFCoreFoundationVersionNumber10_8_2](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_8_2)Added [#def kCFCoreFoundationVersionNumber10_8_3](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_8_3)Added [#def kCFCoreFoundationVersionNumber10_8_4](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_8_4)Added [#def kCFCoreFoundationVersionNumber_iOS_6_0](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber_ios_6_0)Added [#def kCFCoreFoundationVersionNumber_iOS_6_1](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber_ios_6_1)Modified #def CF_AVAILABLE_IOS

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_DEPRECATED_IOS

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM_AVAILABLE

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM_AVAILABLE_IOS

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM_AVAILABLE_MAC

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM_DEPRECATED

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM_DEPRECATED_IOS

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM_DEPRECATED_MAC

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_OPTIONS

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

CFDate.hAdded #def CF_CALENDAR_DEPRECATEDAdded #def CF_CALENDAR_ENUM_DEPRECATEDCFFileSecurity.hAdded [CFFileSecurityClearOptions](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions)Modified [CFFileSecurityClearProperties()](https://developer.apple.com/documentation/corefoundation/1426500-cffilesecurityclearproperties)

|  | Declaration |
| --- | --- |
| From | Boolean CFFileSecurityClearProperties ( CFFileSecurityRef fileSec, CFOptionFlags clearPropertyMask); |
| To | Boolean CFFileSecurityClearProperties ( CFFileSecurityRef fileSec, CFFileSecurityClearOptions clearPropertyMask); |

CFPreferences.hModified [CFPreferencesCopyApplicationList()](https://developer.apple.com/documentation/corefoundation/1515523-cfpreferencescopyapplicationlist)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

CFRunLoop.hAdded [CFRunLoopTimerGetTolerance()](https://developer.apple.com/documentation/corefoundation/1543275-cfrunlooptimergettolerance)Added [CFRunLoopTimerSetTolerance()](https://developer.apple.com/documentation/corefoundation/1542980-cfrunlooptimersettolerance)CFStream.hAdded [CFReadStreamCopyDispatchQueue()](https://developer.apple.com/documentation/corefoundation/1539632-cfreadstreamcopydispatchqueue)Added [CFReadStreamSetDispatchQueue()](https://developer.apple.com/documentation/corefoundation/1539688-cfreadstreamsetdispatchqueue)Added [CFWriteStreamCopyDispatchQueue()](https://developer.apple.com/documentation/corefoundation/1539741-cfwritestreamcopydispatchqueue)Added [CFWriteStreamSetDispatchQueue()](https://developer.apple.com/documentation/corefoundation/1539656-cfwritestreamsetdispatchqueue)CFString.hModified [CFStringFold()](https://developer.apple.com/documentation/corefoundation/1542031-cfstringfold)

|  | Declaration |
| --- | --- |
| From | void CFStringFold ( CFMutableStringRef theString, CFOptionFlags theFlags, CFLocaleRef theLocale); |
| To | void CFStringFold ( CFMutableStringRef theString, CFStringCompareFlags theFlags, CFLocaleRef theLocale); |

CFURL.hAdded [CFURLIsFileReferenceURL()](https://developer.apple.com/documentation/corefoundation/1543161-cfurlisfilereferenceurl)Added [kCFURLUbiquitousItemDownloadingErrorKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemdownloadingerrorkey)Added [kCFURLUbiquitousItemDownloadingStatusCurrent](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemdownloadingstatuscurrent)Added [kCFURLUbiquitousItemDownloadingStatusDownloaded](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemdownloadingstatusdownloaded)Added [kCFURLUbiquitousItemDownloadingStatusKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemdownloadingstatuskey)Added [kCFURLUbiquitousItemDownloadingStatusNotDownloaded](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemdownloadingstatusnotdownloaded)Added [kCFURLUbiquitousItemUploadingErrorKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemuploadingerrorkey)Modified [CFURLCreateFromFSRef()](https://developer.apple.com/documentation/corefoundation/1584385-cfurlcreatefromfsref)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [CFURLGetFSRef()](https://developer.apple.com/documentation/corefoundation/1584387-cfurlgetfsref)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kCFURLBookmarkCreationPreferFileIDResolutionMask](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkcreationoptions/kcfurlbookmarkcreationpreferfileidresolutionmask)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kCFURLHFSPathStyle](https://developer.apple.com/documentation/corefoundation/cfurlpathstyle/kcfurlhfspathstyle)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kCFURLUbiquitousItemIsDownloadedKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemisdownloadedkey)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

CFURLAccess.hModified [CFURLCreateDataAndPropertiesFromResource()](https://developer.apple.com/documentation/corefoundation/1420742-cfurlcreatedataandpropertiesfrom)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [CFURLCreatePropertyFromResource()](https://developer.apple.com/documentation/corefoundation/1420715-cfurlcreatepropertyfromresource)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [CFURLDestroyResource()](https://developer.apple.com/documentation/corefoundation/1420709-cfurldestroyresource)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [CFURLWriteDataAndPropertiesToResource()](https://developer.apple.com/documentation/corefoundation/1420723-cfurlwritedataandpropertiestores)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kCFURLFileDirectoryContents](https://developer.apple.com/documentation/corefoundation/kcfurlfiledirectorycontents)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kCFURLFileExists](https://developer.apple.com/documentation/corefoundation/kcfurlfileexists)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kCFURLFileLastModificationTime](https://developer.apple.com/documentation/corefoundation/kcfurlfilelastmodificationtime)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kCFURLFileLength](https://developer.apple.com/documentation/corefoundation/kcfurlfilelength)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kCFURLFileOwnerID](https://developer.apple.com/documentation/corefoundation/kcfurlfileownerid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kCFURLFilePOSIXMode](https://developer.apple.com/documentation/corefoundation/kcfurlfileposixmode)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kCFURLHTTPStatusCode](https://developer.apple.com/documentation/corefoundation/kcfurlhttpstatuscode)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [kCFURLHTTPStatusLine](https://developer.apple.com/documentation/corefoundation/kcfurlhttpstatusline)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

## CoreGraphics

CGColorSpace.hAdded [CGColorSpaceCopyICCProfile()](https://developer.apple.com/documentation/coregraphics/1408889-cgcolorspacecopyiccprofile)CGContext.hModified [CGContextSelectFont()](https://developer.apple.com/documentation/coregraphics/cgcontext/1586511-selectfont)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [CGContextShowGlyphs()](https://developer.apple.com/documentation/coregraphics/1586500-cgcontextshowglyphs)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [CGContextShowGlyphsAtPoint()](https://developer.apple.com/documentation/coregraphics/cgcontext/1586502-showglyphsatpoint)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [CGContextShowGlyphsWithAdvances()](https://developer.apple.com/documentation/coregraphics/1586503-cgcontextshowglyphswithadvances)

|  | Deprecation | Declaration |
| --- | --- | --- |
| From | _none_ | void CGContextShowGlyphsWithAdvances ( CGContextRef c, const CGGlyph glyphs[], const CGSize advances[], size_t count); |
| To | iOS 7.0 | void CGContextShowGlyphsWithAdvances ( CGContextRef context, const CGGlyph glyphs[], const CGSize advances[], size_t count); |

Modified [CGContextShowText()](https://developer.apple.com/documentation/coregraphics/cgcontext/1586507-showtext)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [CGContextShowTextAtPoint()](https://developer.apple.com/documentation/coregraphics/1586505-cgcontextshowtextatpoint)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [CGTextEncoding](https://developer.apple.com/documentation/coregraphics/cgtextencoding)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

CGFont.hModified [CGGlyphMax](https://developer.apple.com/documentation/coregraphics/cgglyphdeprecatedenum/max)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [CGGlyphMin](https://developer.apple.com/documentation/coregraphics/cgglyphdeprecatedenum/min)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

CGGeometry.hAdded #def CGVECTOR_DEFINEDAdded [CGVector](https://developer.apple.com/documentation/coregraphics/cgvector)Added [CGVectorMake()](https://developer.apple.com/documentation/coregraphics/1454811-cgvectormake)CGPath.hAdded [CGPathAddRoundedRect()](https://developer.apple.com/documentation/coregraphics/1411124-cgpathaddroundedrect)Added [CGPathCreateWithRoundedRect()](https://developer.apple.com/documentation/coregraphics/cgpath/1411218-init)

## CoreImage

CIDetector.hAdded [CIDetectorEyeBlink](https://developer.apple.com/documentation/coreimage/cidetectoreyeblink)Added [CIDetectorSmile](https://developer.apple.com/documentation/coreimage/cidetectorsmile)CIFeature.hAdded [CIFaceFeature.bounds](https://developer.apple.com/documentation/coreimage/cifacefeature/1438068-bounds)Added [CIFaceFeature.faceAngle](https://developer.apple.com/documentation/coreimage/cifacefeature/1437689-faceangle)Added [CIFaceFeature.hasFaceAngle](https://developer.apple.com/documentation/coreimage/cifacefeature/1438165-hasfaceangle)Added [CIFaceFeature.hasSmile](https://developer.apple.com/documentation/coreimage/cifacefeature/1437882-hassmile)Added [CIFaceFeature.leftEyeClosed](https://developer.apple.com/documentation/coreimage/cifacefeature/1437630-lefteyeclosed)Added [CIFaceFeature.rightEyeClosed](https://developer.apple.com/documentation/coreimage/cifacefeature/1437615-righteyeclosed)CIFilter.hRemoved kCICategoryApplePrivateAdded CIFilter(CIFilterXMPSerialization)Added [kCIInputAngleKey](https://developer.apple.com/documentation/coreimage/kciinputanglekey)Added [kCIInputAspectRatioKey](https://developer.apple.com/documentation/coreimage/kciinputaspectratiokey)Added [kCIInputBrightnessKey](https://developer.apple.com/documentation/coreimage/kciinputbrightnesskey)Added [kCIInputCenterKey](https://developer.apple.com/documentation/coreimage/kciinputcenterkey)Added [kCIInputColorKey](https://developer.apple.com/documentation/coreimage/kciinputcolorkey)Added [kCIInputContrastKey](https://developer.apple.com/documentation/coreimage/kciinputcontrastkey)Added [kCIInputEVKey](https://developer.apple.com/documentation/coreimage/kciinputevkey)Added [kCIInputExtentKey](https://developer.apple.com/documentation/coreimage/kciinputextentkey)Added [kCIInputIntensityKey](https://developer.apple.com/documentation/coreimage/kciinputintensitykey)Added [kCIInputMaskImageKey](https://developer.apple.com/documentation/coreimage/kciinputmaskimagekey)Added [kCIInputRadiusKey](https://developer.apple.com/documentation/coreimage/kciinputradiuskey)Added [kCIInputSaturationKey](https://developer.apple.com/documentation/coreimage/kciinputsaturationkey)Added [kCIInputScaleKey](https://developer.apple.com/documentation/coreimage/kciinputscalekey)Added [kCIInputSharpnessKey](https://developer.apple.com/documentation/coreimage/kciinputsharpnesskey)Added [kCIInputTargetImageKey](https://developer.apple.com/documentation/coreimage/kciinputtargetimagekey)Added [kCIInputTimeKey](https://developer.apple.com/documentation/coreimage/kciinputtimekey)Added [kCIInputTransformKey](https://developer.apple.com/documentation/coreimage/kciinputtransformkey)Added [kCIInputWidthKey](https://developer.apple.com/documentation/coreimage/kciinputwidthkey)CIImage.hAdded [-[CIImage regionOfInterestForImage:inRect:]](https://developer.apple.com/documentation/coreimage/ciimage/1437994-regionofinterest)

## CoreLocation

CLBeaconRegion.hAdded [CLBeacon](https://developer.apple.com/documentation/corelocation/clbeacon)Added [CLBeacon.accuracy](https://developer.apple.com/documentation/corelocation/clbeacon/1621551-accuracy)Added [CLBeacon.major](https://developer.apple.com/documentation/corelocation/clbeacon/1621418-major)Added [CLBeacon.minor](https://developer.apple.com/documentation/corelocation/clbeacon/1621558-minor)Added [CLBeacon.proximity](https://developer.apple.com/documentation/corelocation/clbeacon/1621554-proximity)Added [CLBeacon.proximityUUID](https://developer.apple.com/documentation/corelocation/clbeacon/1621508-proximityuuid)Added [CLBeacon.rssi](https://developer.apple.com/documentation/corelocation/clbeacon/1621557-rssi)Added [CLBeaconRegion](https://developer.apple.com/documentation/corelocation/clbeaconregion)Added [-[CLBeaconRegion initWithProximityUUID:identifier:]](https://developer.apple.com/documentation/corelocation/clbeaconregion/1621534-initwithproximityuuid)Added [-[CLBeaconRegion initWithProximityUUID:major:identifier:]](https://developer.apple.com/documentation/corelocation/clbeaconregion/1621475-init)Added [-[CLBeaconRegion initWithProximityUUID:major:minor:identifier:]](https://developer.apple.com/documentation/corelocation/clbeaconregion/1621392-init)Added [CLBeaconRegion.major](https://developer.apple.com/documentation/corelocation/clbeaconregion/1621536-major)Added [CLBeaconRegion.minor](https://developer.apple.com/documentation/corelocation/clbeaconregion/1621414-minor)Added [CLBeaconRegion.notifyEntryStateOnDisplay](https://developer.apple.com/documentation/corelocation/clbeaconregion/1621552-notifyentrystateondisplay)Added [-[CLBeaconRegion peripheralDataWithMeasuredPower:]](https://developer.apple.com/documentation/corelocation/clbeaconregion/1621494-peripheraldatawithmeasuredpower)Added [CLBeaconRegion.proximityUUID](https://developer.apple.com/documentation/corelocation/clbeaconregion/1621556-proximityuuid)Added [CLBeaconMajorValue](https://developer.apple.com/documentation/corelocation/clbeaconmajorvalue)Added [CLBeaconMinorValue](https://developer.apple.com/documentation/corelocation/clbeaconminorvalue)CLCircularRegion.hAdded [CLCircularRegion](https://developer.apple.com/documentation/corelocation/clcircularregion)Added [CLCircularRegion.center](https://developer.apple.com/documentation/corelocation/clcircularregion/1423601-center)Added [-[CLCircularRegion containsCoordinate:]](https://developer.apple.com/documentation/corelocation/clcircularregion/1423697-containscoordinate)Added [-[CLCircularRegion initWithCenter:radius:identifier:]](https://developer.apple.com/documentation/corelocation/clcircularregion/1423761-initwithcenter)Added [CLCircularRegion.radius](https://developer.apple.com/documentation/corelocation/clcircularregion/1423734-radius)CLError.hAdded [kCLErrorRangingFailure](https://developer.apple.com/documentation/corelocation/clerror/kclerrorrangingfailure)Added [kCLErrorRangingUnavailable](https://developer.apple.com/documentation/corelocation/clerror/kclerrorrangingunavailable)CLHeading.hModified [CLHeading](https://developer.apple.com/documentation/corelocation/clheading)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

CLLocation.hModified [CLLocation](https://developer.apple.com/documentation/corelocation/cllocation)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

CLLocationManager.hAdded [+[CLLocationManager isMonitoringAvailableForClass:]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423654-ismonitoringavailable)Added [+[CLLocationManager isRangingAvailable]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620549-israngingavailable)Added [CLLocationManager.rangedRegions](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620552-rangedregions)Added [-[CLLocationManager requestStateForRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423804-requeststate)Added [-[CLLocationManager startRangingBeaconsInRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620554-startrangingbeacons)Added [-[CLLocationManager stopRangingBeaconsInRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620559-stoprangingbeaconsinregion)Modified [+[CLLocationManager regionMonitoringAvailable]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423564-regionmonitoringavailable)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

CLLocationManagerDelegate.hAdded [-[CLLocationManagerDelegate locationManager:didDetermineState:forRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423570-locationmanager)Added [-[CLLocationManagerDelegate locationManager:didRangeBeacons:inRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1621501-locationmanager)Added [-[CLLocationManagerDelegate locationManager:rangingBeaconsDidFailForRegion:withError:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1621483-locationmanager)CLPlacemark.hModified [CLPlacemark](https://developer.apple.com/documentation/corelocation/clplacemark)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

CLRegion.hAdded [CLRegion.notifyOnEntry](https://developer.apple.com/documentation/corelocation/clregion/1423566-notifyonentry)Added [CLRegion.notifyOnExit](https://developer.apple.com/documentation/corelocation/clregion/1423595-notifyonexit)Added [CLProximity](https://developer.apple.com/documentation/corelocation/clproximity)Added [CLProximityFar](https://developer.apple.com/documentation/corelocation/clproximity/far)Added [CLProximityImmediate](https://developer.apple.com/documentation/corelocation/clproximity/immediate)Added [CLProximityNear](https://developer.apple.com/documentation/corelocation/clproximity/clproximitynear)Added [CLProximityUnknown](https://developer.apple.com/documentation/corelocation/clproximity/clproximityunknown)Added [CLRegionState](https://developer.apple.com/documentation/corelocation/clregionstate)Added [CLRegionStateInside](https://developer.apple.com/documentation/corelocation/clregionstate/clregionstateinside)Added [CLRegionStateOutside](https://developer.apple.com/documentation/corelocation/clregionstate/outside)Added [CLRegionStateUnknown](https://developer.apple.com/documentation/corelocation/clregionstate/unknown)Modified [CLRegion](https://developer.apple.com/documentation/corelocation/clregion)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

Modified [CLRegion.center](https://developer.apple.com/documentation/corelocation/clregion/1423691-center)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[CLRegion containsCoordinate:]](https://developer.apple.com/documentation/corelocation/clregion/1423828-contains)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[CLRegion initCircularRegionWithCenter:radius:identifier:]](https://developer.apple.com/documentation/corelocation/clregion/1423681-init)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [CLRegion.radius](https://developer.apple.com/documentation/corelocation/clregion/1423730-radius)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

## CoreMedia

CMBase.hRemoved #def AVAILABLE_MAC_OS_X_VERSION_10_9_AND_LATERCMFormatDescription.hAdded [CMVideoFormatDescriptionCreateFromH264ParameterSets()](https://developer.apple.com/documentation/coremedia/1489818-cmvideoformatdescriptioncreatefr)Added [CMVideoFormatDescriptionGetH264ParameterSetAtIndex()](https://developer.apple.com/documentation/coremedia/1489529-cmvideoformatdescriptiongeth264p)Added [kCMFormatDescriptionError_ValueNotAvailable](https://developer.apple.com/documentation/coremedia/1564245-error_codes/kcmformatdescriptionerror_valuenotavailable)Added [kCMMPEG2VideoProfile_XF](https://developer.apple.com/documentation/coremedia/kcmmpeg2videoprofile_xf)CMSampleBuffer.hAdded [CMSampleBufferCopyPCMDataIntoAudioBufferList()](https://developer.apple.com/documentation/coremedia/1489200-cmsamplebuffercopypcmdataintoaud)Added [kCMSampleBufferAttachmentKey_DroppedFrameReasonInfo](https://developer.apple.com/documentation/coremedia/kcmsamplebufferattachmentkey_droppedframereasoninfo)Added [kCMSampleBufferDroppedFrameReasonInfo_CameraModeSwitch](https://developer.apple.com/documentation/coremedia/kcmsamplebufferdroppedframereasoninfo_cameramodeswitch)CMSync.hAdded [kCMTimebaseNotificationKey_EventTime](https://developer.apple.com/documentation/coremedia/kcmtimebasenotificationkey_eventtime)CMTextMarkup.hAdded [kCMTextMarkupAlignmentType_End](https://developer.apple.com/documentation/coremedia/kcmtextmarkupalignmenttype_end)Added [kCMTextMarkupAlignmentType_Left](https://developer.apple.com/documentation/coremedia/kcmtextmarkupalignmenttype_left)Added [kCMTextMarkupAlignmentType_Middle](https://developer.apple.com/documentation/coremedia/kcmtextmarkupalignmenttype_middle)Added [kCMTextMarkupAlignmentType_Right](https://developer.apple.com/documentation/coremedia/kcmtextmarkupalignmenttype_right)Added [kCMTextMarkupAlignmentType_Start](https://developer.apple.com/documentation/coremedia/kcmtextmarkupalignmenttype_start)Added [kCMTextMarkupAttribute_Alignment](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_alignment)Added [kCMTextMarkupAttribute_BaseFontSizePercentageRelativeToVideoHeight](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_basefontsizepercentagerelativetovideoheight)Added [kCMTextMarkupAttribute_CharacterBackgroundColorARGB](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_characterbackgroundcolorargb)Added [kCMTextMarkupAttribute_CharacterEdgeStyle](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_characteredgestyle)Added [kCMTextMarkupAttribute_GenericFontFamilyName](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_genericfontfamilyname)Added [kCMTextMarkupAttribute_OrthogonalLinePositionPercentageRelativeToWritingDirection](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_orthogonallinepositionpercentagerelativetowritingdirection)Added [kCMTextMarkupAttribute_TextPositionPercentageRelativeToWritingDirection](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_textpositionpercentagerelativetowritingdirection)Added [kCMTextMarkupAttribute_VerticalLayout](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_verticallayout)Added [kCMTextMarkupAttribute_WritingDirectionSizePercentage](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_writingdirectionsizepercentage)Added [kCMTextMarkupCharacterEdgeStyle_Depressed](https://developer.apple.com/documentation/coremedia/kcmtextmarkupcharacteredgestyle_depressed)Added [kCMTextMarkupCharacterEdgeStyle_DropShadow](https://developer.apple.com/documentation/coremedia/kcmtextmarkupcharacteredgestyle_dropshadow)Added [kCMTextMarkupCharacterEdgeStyle_None](https://developer.apple.com/documentation/coremedia/kcmtextmarkupcharacteredgestyle_none)Added [kCMTextMarkupCharacterEdgeStyle_Raised](https://developer.apple.com/documentation/coremedia/kcmtextmarkupcharacteredgestyle_raised)Added [kCMTextMarkupCharacterEdgeStyle_Uniform](https://developer.apple.com/documentation/coremedia/kcmtextmarkupcharacteredgestyle_uniform)Added [kCMTextMarkupGenericFontName_Casual](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_casual)Added [kCMTextMarkupGenericFontName_Cursive](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_cursive)Added [kCMTextMarkupGenericFontName_Default](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_default)Added [kCMTextMarkupGenericFontName_Fantasy](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_fantasy)Added [kCMTextMarkupGenericFontName_Monospace](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_monospace)Added [kCMTextMarkupGenericFontName_MonospaceSansSerif](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_monospacesansserif)Added [kCMTextMarkupGenericFontName_MonospaceSerif](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_monospaceserif)Added [kCMTextMarkupGenericFontName_ProportionalSansSerif](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_proportionalsansserif)Added [kCMTextMarkupGenericFontName_ProportionalSerif](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_proportionalserif)Added [kCMTextMarkupGenericFontName_SansSerif](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_sansserif)Added [kCMTextMarkupGenericFontName_Serif](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_serif)Added [kCMTextMarkupGenericFontName_SmallCapital](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_smallcapital)Added [kCMTextVerticalLayout_LeftToRight](https://developer.apple.com/documentation/coremedia/kcmtextverticallayout_lefttoright)Added [kCMTextVerticalLayout_RightToLeft](https://developer.apple.com/documentation/coremedia/kcmtextverticallayout_righttoleft)

## CoreMIDI

No changes

## CoreMotion

CMAttitude.hModified [CMAttitude](https://developer.apple.com/documentation/coremotion/cmattitude)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

CMAvailability.hAdded #def CM_EXTERNCMError.hAdded [CMErrorInvalidParameter](https://developer.apple.com/documentation/coremotion/cmerror/cmerrorinvalidparameter)Added [CMErrorMotionActivityNotAuthorized](https://developer.apple.com/documentation/coremotion/cmerror/cmerrormotionactivitynotauthorized)Added [CMErrorMotionActivityNotAvailable](https://developer.apple.com/documentation/coremotion/cmerrormotionactivitynotavailable)Added [CMErrorMotionActivityNotEntitled](https://developer.apple.com/documentation/coremotion/cmerror/cmerrormotionactivitynotentitled)Added [CMErrorUnknown](https://developer.apple.com/documentation/coremotion/cmerrorunknown)CMLogItem.hModified [CMLogItem](https://developer.apple.com/documentation/coremotion/cmlogitem)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

CMMotionActivity.hAdded [CMMotionActivity](https://developer.apple.com/documentation/coremotion/cmmotionactivity)Added [CMMotionActivity.automotive](https://developer.apple.com/documentation/coremotion/cmmotionactivity/1615437-automotive)Added [CMMotionActivity.confidence](https://developer.apple.com/documentation/coremotion/cmmotionactivity/1615433-confidence)Added [CMMotionActivity.running](https://developer.apple.com/documentation/coremotion/cmmotionactivity/1615441-running)Added [CMMotionActivity.startDate](https://developer.apple.com/documentation/coremotion/cmmotionactivity/1615453-startdate)Added [CMMotionActivity.stationary](https://developer.apple.com/documentation/coremotion/cmmotionactivity/1615430-stationary)Added [CMMotionActivity.unknown](https://developer.apple.com/documentation/coremotion/cmmotionactivity/1615439-unknown)Added [CMMotionActivity.walking](https://developer.apple.com/documentation/coremotion/cmmotionactivity/1615432-walking)Added [CMMotionActivityConfidence](https://developer.apple.com/documentation/coremotion/cmmotionactivityconfidence)Added [CMMotionActivityConfidenceHigh](https://developer.apple.com/documentation/coremotion/cmmotionactivityconfidence/high)Added [CMMotionActivityConfidenceLow](https://developer.apple.com/documentation/coremotion/cmmotionactivityconfidence/cmmotionactivityconfidencelow)Added [CMMotionActivityConfidenceMedium](https://developer.apple.com/documentation/coremotion/cmmotionactivityconfidence/cmmotionactivityconfidencemedium)CMMotionActivityManager.hAdded [CMMotionActivityManager](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager)Added [+[CMMotionActivityManager isActivityAvailable]](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/1616116-isactivityavailable)Added [-[CMMotionActivityManager queryActivityStartingFromDate:toDate:toQueue:withHandler:]](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/1615929-queryactivitystartingfromdate)Added [-[CMMotionActivityManager startActivityUpdatesToQueue:withHandler:]](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/1615945-startactivityupdatestoqueue)Added [-[CMMotionActivityManager stopActivityUpdates]](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/1616086-stopactivityupdates)Added [CMMotionActivityHandler](https://developer.apple.com/documentation/coremotion/cmmotionactivityhandler)Added [CMMotionActivityQueryHandler](https://developer.apple.com/documentation/coremotion/cmmotionactivityqueryhandler)CMStepCounter.hAdded [CMStepCounter](https://developer.apple.com/documentation/coremotion/cmstepcounter)Added [+[CMStepCounter isStepCountingAvailable]](https://developer.apple.com/documentation/coremotion/cmstepcounter/1616013-isstepcountingavailable)Added [-[CMStepCounter queryStepCountStartingFrom:to:toQueue:withHandler:]](https://developer.apple.com/documentation/coremotion/cmstepcounter/1616166-querystepcountstartingfrom)Added [-[CMStepCounter startStepCountingUpdatesToQueue:updateOn:withHandler:]](https://developer.apple.com/documentation/coremotion/cmstepcounter/1616151-startstepcountingupdates)Added [-[CMStepCounter stopStepCountingUpdates]](https://developer.apple.com/documentation/coremotion/cmstepcounter/1616157-stopstepcountingupdates)Added [CMStepQueryHandler](https://developer.apple.com/documentation/coremotion/cmstepqueryhandler)Added [CMStepUpdateHandler](https://developer.apple.com/documentation/coremotion/cmstepupdatehandler)

## CoreTelephony

CTSubscriber.hAdded [CTSubscriber](https://developer.apple.com/documentation/coretelephony/ctsubscriber)Added [CTSubscriber.carrierToken](https://developer.apple.com/documentation/coretelephony/ctsubscriber/1620318-carriertoken)Added [CTSubscriberTokenRefreshed](https://developer.apple.com/documentation/coretelephony/ctsubscribertokenrefreshed)CTSubscriberInfo.hAdded [CTSubscriberInfo](https://developer.apple.com/documentation/coretelephony/ctsubscriberinfo)Added [+[CTSubscriberInfo subscriber]](https://developer.apple.com/documentation/coretelephony/ctsubscriberinfo/1620278-subscriber)CTTelephonyNetworkInfo.hAdded [CTTelephonyNetworkInfo.currentRadioAccessTechnology](https://developer.apple.com/documentation/coretelephony/cttelephonynetworkinfo/1616895-currentradioaccesstechnology)Added [CTRadioAccessTechnologyCDMA1x](https://developer.apple.com/documentation/coretelephony/ctradioaccesstechnologycdma1x)Added [CTRadioAccessTechnologyCDMAEVDORev0](https://developer.apple.com/documentation/coretelephony/ctradioaccesstechnologycdmaevdorev0)Added [CTRadioAccessTechnologyCDMAEVDORevA](https://developer.apple.com/documentation/coretelephony/ctradioaccesstechnologycdmaevdoreva)Added [CTRadioAccessTechnologyCDMAEVDORevB](https://developer.apple.com/documentation/coretelephony/ctradioaccesstechnologycdmaevdorevb)Added [CTRadioAccessTechnologyDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1616908-ctradioaccesstechnologydidchange)Added [CTRadioAccessTechnologyEdge](https://developer.apple.com/documentation/coretelephony/ctradioaccesstechnologyedge)Added [CTRadioAccessTechnologyGPRS](https://developer.apple.com/documentation/coretelephony/ctradioaccesstechnologygprs)Added [CTRadioAccessTechnologyHSDPA](https://developer.apple.com/documentation/coretelephony/ctradioaccesstechnologyhsdpa)Added [CTRadioAccessTechnologyHSUPA](https://developer.apple.com/documentation/coretelephony/ctradioaccesstechnologyhsupa)Added [CTRadioAccessTechnologyLTE](https://developer.apple.com/documentation/coretelephony/ctradioaccesstechnologylte)Added [CTRadioAccessTechnologyWCDMA](https://developer.apple.com/documentation/coretelephony/ctradioaccesstechnologywcdma)Added [CTRadioAccessTechnologyeHRPD](https://developer.apple.com/documentation/coretelephony/ctradioaccesstechnologyehrpd)

## CoreText

CTDefines.hRemoved #def CT_AVAILABLE_BUT_DEPRECATEDRemoved #def CT_AVAILABLE_STARTINGRemoved #def CT_DEPRECATED_ENUMERATORAdded #def CT_DEPRECATED_MACCTFont.hAdded [#def ATSFONTREF_DEFINED](https://developer.apple.com/documentation/coretext/atsfontref_defined)Added [ATSFontRef](https://developer.apple.com/documentation/applicationservices/atsfontref)Added [kCTFontTableLtag](https://developer.apple.com/documentation/coretext/kctfonttableltag)CTFontDescriptor.hAdded [CTFontDescriptorCreateCopyWithFamily()](https://developer.apple.com/documentation/coretext/1510392-ctfontdescriptorcreatecopywithfa)Added [CTFontDescriptorCreateCopyWithSymbolicTraits()](https://developer.apple.com/documentation/coretext/1509171-ctfontdescriptorcreatecopywithsy)Added [kCTFontDownloadableAttribute](https://developer.apple.com/documentation/coretext/kctfontdownloadableattribute)Added [kCTFontDownloadedAttribute](https://developer.apple.com/documentation/coretext/kctfontdownloadedattribute)CTFontManager.hAdded [CTFontManagerCreateFontDescriptorFromData()](https://developer.apple.com/documentation/coretext/1499509-ctfontmanagercreatefontdescripto)Added [CTFontManagerCreateFontDescriptorsFromURL()](https://developer.apple.com/documentation/coretext/1499500-ctfontmanagercreatefontdescripto)Added [kCTFontManagerRegisteredFontsChangedNotification](https://developer.apple.com/documentation/coretext/kctfontmanagerregisteredfontschangednotification)CTFrame.hAdded [kCTFrameProgressionLeftToRight](https://developer.apple.com/documentation/coretext/ctframeprogression/kctframeprogressionlefttoright)CTStringAttributes.hAdded [kCTLanguageAttributeName](https://developer.apple.com/documentation/coretext/kctlanguageattributename)CoreText.hAdded [#def kCTVersionNumber10_9](https://developer.apple.com/documentation/coretext/kctversionnumber10_9)SFNTLayoutTypes.hAdded [LtagStringRange](https://developer.apple.com/documentation/coretext/ltagstringrange)Added [LtagTable](https://developer.apple.com/documentation/coretext/ltagtable)Added [kLTAGCurrentVersion](https://developer.apple.com/documentation/coretext/1446351-anonymous/kltagcurrentversion)Added [kLanguageTagType](https://developer.apple.com/documentation/coretext/klanguagetagtype)

## CoreVideo

No changes

## EventKit

EKEventStore.hModified [-[EKEventStore fetchRemindersMatchingPredicate:completion:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507500-fetchremindersmatchingpredicate)

|  | Declaration |
| --- | --- |
| From | - (id)fetchRemindersMatchingPredicate:(NSPredicate \*)predicate completion:(void (^)(NSArray \*))completion |
| To | - (id)fetchRemindersMatchingPredicate:(NSPredicate \*)predicate completion:(void (^)(NSArray \*reminders))completion |

## EventKitUI

EKCalendarChooser.hModified [EKCalendarChooser.delegate](https://developer.apple.com/documentation/eventkitui/ekcalendarchooser/1613949-delegate)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, assign) id<EKCalendarChooserDelegate> delegate |
| To | @property(nonatomic, weak) id<EKCalendarChooserDelegate> delegate |

EKEventEditViewController.hModified [EKEventEditViewController.editViewDelegate](https://developer.apple.com/documentation/eventkitui/ekeventeditviewcontroller/1613954-editviewdelegate)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, assign) id<EKEventEditViewDelegate> editViewDelegate |
| To | @property(nonatomic, weak) id<EKEventEditViewDelegate> editViewDelegate |

EKEventViewController.hModified [EKEventViewController.delegate](https://developer.apple.com/documentation/eventkitui/ekeventviewcontroller/1613939-delegate)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, assign) id<EKEventViewDelegate> delegate |
| To | @property(nonatomic, weak) id<EKEventViewDelegate> delegate |

## ExternalAccessory

No changes

## Foundation

FoundationErrors.hAdded [NSUbiquitousFileErrorMaximum](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nsubiquitousfileerrormaximum)Added [NSUbiquitousFileErrorMinimum](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nsubiquitousfileerrorminimum)Added [NSUbiquitousFileNotUploadedDueToQuotaError](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nsubiquitousfilenotuploadedduetoquotaerror)Added [NSUbiquitousFileUbiquityServerNotAvailable](https://developer.apple.com/documentation/foundation/nsubiquitousfileubiquityservernotavailable)Added [NSUbiquitousFileUnavailableError](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nsubiquitousfileunavailableerror)NSArray.hAdded [-[NSArray firstObject]](https://developer.apple.com/documentation/foundation/nsarray/1412852-firstobject)Added [-[NSArray init]](https://developer.apple.com/documentation/foundation/nsarray/1414315-init)Added [-[NSMutableArray init]](https://developer.apple.com/documentation/foundation/nsmutablearray/1407556-init)Modified [+[NSArray array]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/clm/NSArray/array)

|  | Declaration |
| --- | --- |
| From | + (id)array |
| To | + (instancetype)array |

Modified [+[NSArray arrayWithArray:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/clm/NSArray/arrayWithArray:)

|  | Declaration |
| --- | --- |
| From | + (id)arrayWithArray:(NSArray \*)array |
| To | + (instancetype)arrayWithArray:(NSArray \*)array |

Modified [+[NSArray arrayWithObject:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/clm/NSArray/arrayWithObject:)

|  | Declaration |
| --- | --- |
| From | + (id)arrayWithObject:(id)anObject |
| To | + (instancetype)arrayWithObject:(id)anObject |

Modified [+[NSArray arrayWithObjects:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/clm/NSArray/arrayWithObjects:)

|  | Declaration |
| --- | --- |
| From | + (id)arrayWithObjects:(id)firstObj, ... |
| To | + (instancetype)arrayWithObjects:(id)firstObj, ... |

Modified [+[NSArray arrayWithObjects:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/clm/NSArray/arrayWithObjects:count:)

|  | Declaration |
| --- | --- |
| From | + (id)arrayWithObjects:(const id [])objects count:(NSUInteger)cnt |
| To | + (instancetype)arrayWithObjects:(const id [])objects count:(NSUInteger)cnt |

Modified [-[NSArray initWithArray:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/initWithArray:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithArray:(NSArray \*)array |
| To | - (instancetype)initWithArray:(NSArray \*)array |

Modified [-[NSArray initWithArray:copyItems:]](https://developer.apple.com/documentation/foundation/nsarray/1408557-initwitharray)

|  | Declaration |
| --- | --- |
| From | - (id)initWithArray:(NSArray \*)array copyItems:(BOOL)flag |
| To | - (instancetype)initWithArray:(NSArray \*)array copyItems:(BOOL)flag |

Modified [-[NSArray initWithObjects:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/initWithObjects:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObjects:(id)firstObj, ... |
| To | - (instancetype)initWithObjects:(id)firstObj, ... |

Modified [-[NSArray initWithObjects:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/initWithObjects:count:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObjects:(const id [])objects count:(NSUInteger)cnt |
| To | - (instancetype)initWithObjects:(const id [])objects count:(NSUInteger)cnt |

Modified [+[NSMutableArray arrayWithCapacity:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/clm/NSMutableArray/arrayWithCapacity:)

|  | Declaration |
| --- | --- |
| From | + (id)arrayWithCapacity:(NSUInteger)numItems |
| To | + (instancetype)arrayWithCapacity:(NSUInteger)numItems |

Modified [-[NSMutableArray initWithCapacity:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/initWithCapacity:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithCapacity:(NSUInteger)numItems |
| To | - (instancetype)initWithCapacity:(NSUInteger)numItems |

NSBundle.hAdded [-[NSBundle appStoreReceiptURL]](https://developer.apple.com/documentation/foundation/nsbundle/1407276-appstorereceipturl)NSCalendar.hAdded [NSCalendarOptions](https://developer.apple.com/documentation/foundation/nscalendaroptions)Added [NSCalendarUnitCalendar](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunitcalendar)Added [NSCalendarUnitDay](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunitday)Added [NSCalendarUnitEra](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunitera)Added [NSCalendarUnitHour](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunithour)Added [NSCalendarUnitMinute](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunitminute)Added [NSCalendarUnitMonth](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunitmonth)Added [NSCalendarUnitQuarter](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunitquarter)Added [NSCalendarUnitSecond](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunitsecond)Added [NSCalendarUnitTimeZone](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunittimezone)Added [NSCalendarUnitWeekOfMonth](https://developer.apple.com/documentation/foundation/nscalendar/unit/1412656-weekofmonth)Added [NSCalendarUnitWeekOfYear](https://developer.apple.com/documentation/foundation/nscalendar/unit/1411748-weekofyear)Added [NSCalendarUnitWeekday](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunitweekday)Added [NSCalendarUnitWeekdayOrdinal](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunitweekdayordinal)Added [NSCalendarUnitYear](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunityear)Added [NSCalendarUnitYearForWeekOfYear](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunityearforweekofyear)Added [NSCalendarWrapComponents](https://developer.apple.com/documentation/foundation/nscalendar/options/1408451-wrapcomponents)Added [NSDateComponentUndefined](https://developer.apple.com/documentation/foundation/nsdatecomponentundefined)Added #def NS_CALENDAR_DEPRECATEDAdded #def NS_CALENDAR_DEPRECATED_MACAdded #def NS_CALENDAR_ENUM_DEPRECATEDModified [-[NSCalendar components:fromDate:]](https://developer.apple.com/documentation/foundation/nscalendar/1414841-components)

|  | Declaration |
| --- | --- |
| From | - (NSDateComponents \*)components:(NSUInteger)unitFlags fromDate:(NSDate \*)date |
| To | - (NSDateComponents \*)components:(NSCalendarUnit)unitFlags fromDate:(NSDate \*)date |

Modified [-[NSCalendar components:fromDate:toDate:options:]](https://developer.apple.com/documentation/foundation/nscalendar/1407925-components)

|  | Declaration |
| --- | --- |
| From | - (NSDateComponents \*)components:(NSUInteger)unitFlags fromDate:(NSDate \*)startingDate toDate:(NSDate \*)resultDate options:(NSUInteger)opts |
| To | - (NSDateComponents \*)components:(NSCalendarUnit)unitFlags fromDate:(NSDate \*)startingDate toDate:(NSDate \*)resultDate options:(NSCalendarOptions)opts |

Modified [-[NSCalendar dateByAddingComponents:toDate:options:]](https://developer.apple.com/documentation/foundation/nscalendar/1409577-date)

|  | Declaration |
| --- | --- |
| From | - (NSDate \*)dateByAddingComponents:(NSDateComponents \*)comps toDate:(NSDate \*)date options:(NSUInteger)opts |
| To | - (NSDate \*)dateByAddingComponents:(NSDateComponents \*)comps toDate:(NSDate \*)date options:(NSCalendarOptions)opts |

NSData.hAdded [-[NSData base64EncodedDataWithOptions:]](https://developer.apple.com/documentation/foundation/nsdata/1412739-base64encodeddatawithoptions)Added [-[NSData base64EncodedStringWithOptions:]](https://developer.apple.com/documentation/foundation/nsdata/1413546-base64encodedstringwithoptions)Added [-[NSData base64Encoding]](https://developer.apple.com/documentation/foundation/nsdata/1547242-base64encoding)Added [-[NSData enumerateByteRangesUsingBlock:]](https://developer.apple.com/documentation/foundation/nsdata/1408400-enumeratebyterangesusingblock)Added [-[NSData initWithBase64EncodedData:options:]](https://developer.apple.com/documentation/foundation/nsdata/1417833-init)Added [-[NSData initWithBase64EncodedString:options:]](https://developer.apple.com/documentation/foundation/nsdata/1410081-initwithbase64encodedstring)Added [-[NSData initWithBase64Encoding:]](https://developer.apple.com/documentation/foundation/nsdata/1547237-init)Added [-[NSData initWithBytesNoCopy:length:deallocator:]](https://developer.apple.com/documentation/foundation/nsdata/1417337-initwithbytesnocopy)Added NSData(NSDataBase64Encoding)Added [NSDataBase64DecodingIgnoreUnknownCharacters](https://developer.apple.com/documentation/foundation/nsdata/base64decodingoptions/1410087-ignoreunknowncharacters)Added [NSDataBase64DecodingOptions](https://developer.apple.com/documentation/foundation/nsdata/base64decodingoptions)Added [NSDataBase64Encoding64CharacterLineLength](https://developer.apple.com/documentation/foundation/nsdata/base64encodingoptions/1407872-linelength64characters)Added [NSDataBase64Encoding76CharacterLineLength](https://developer.apple.com/documentation/foundation/nsdata/base64encodingoptions/1413700-linelength76characters)Added [NSDataBase64EncodingEndLineWithCarriageReturn](https://developer.apple.com/documentation/foundation/nsdatabase64encodingoptions/nsdatabase64encodingendlinewithcarriagereturn)Added [NSDataBase64EncodingEndLineWithLineFeed](https://developer.apple.com/documentation/foundation/nsdatabase64encodingoptions/nsdatabase64encodingendlinewithlinefeed)Added [NSDataBase64EncodingOptions](https://developer.apple.com/documentation/foundation/nsdata/base64encodingoptions)NSDate.hModified [+[NSDate date]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/clm/NSDate/date)

|  | Declaration |
| --- | --- |
| From | + (id)date |
| To | + (instancetype)date |

Modified [+[NSDate dateWithTimeInterval:sinceDate:]](https://developer.apple.com/documentation/foundation/nsdate/1591578-datewithtimeinterval)

|  | Declaration |
| --- | --- |
| From | + (id)dateWithTimeInterval:(NSTimeInterval)ti sinceDate:(NSDate \*)date |
| To | + (instancetype)dateWithTimeInterval:(NSTimeInterval)secsToBeAdded sinceDate:(NSDate \*)date |

Modified [+[NSDate dateWithTimeIntervalSince1970:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/clm/NSDate/dateWithTimeIntervalSince1970:)

|  | Declaration |
| --- | --- |
| From | + (id)dateWithTimeIntervalSince1970:(NSTimeInterval)secs |
| To | + (instancetype)dateWithTimeIntervalSince1970:(NSTimeInterval)secs |

Modified [+[NSDate dateWithTimeIntervalSinceNow:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/clm/NSDate/dateWithTimeIntervalSinceNow:)

|  | Declaration |
| --- | --- |
| From | + (id)dateWithTimeIntervalSinceNow:(NSTimeInterval)secs |
| To | + (instancetype)dateWithTimeIntervalSinceNow:(NSTimeInterval)secs |

Modified [+[NSDate dateWithTimeIntervalSinceReferenceDate:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/clm/NSDate/dateWithTimeIntervalSinceReferenceDate:)

|  | Declaration |
| --- | --- |
| From | + (id)dateWithTimeIntervalSinceReferenceDate:(NSTimeInterval)secs |
| To | + (instancetype)dateWithTimeIntervalSinceReferenceDate:(NSTimeInterval)ti |

Modified [-[NSDate init]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/instm/NSDate/init)

|  | Declaration |
| --- | --- |
| From | - (id)init |
| To | - (instancetype)init |

Modified [-[NSDate initWithTimeInterval:sinceDate:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/instm/NSDate/initWithTimeInterval:sinceDate:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithTimeInterval:(NSTimeInterval)secsToBeAdded sinceDate:(NSDate \*)anotherDate |
| To | - (instancetype)initWithTimeInterval:(NSTimeInterval)secsToBeAdded sinceDate:(NSDate \*)date |

Modified [-[NSDate initWithTimeIntervalSince1970:]](https://developer.apple.com/documentation/foundation/nsdate/1416453-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithTimeIntervalSince1970:(NSTimeInterval)ti |
| To | - (instancetype)initWithTimeIntervalSince1970:(NSTimeInterval)secs |

Modified [-[NSDate initWithTimeIntervalSinceNow:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/instm/NSDate/initWithTimeIntervalSinceNow:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithTimeIntervalSinceNow:(NSTimeInterval)secs |
| To | - (instancetype)initWithTimeIntervalSinceNow:(NSTimeInterval)secs |

Modified [-[NSDate initWithTimeIntervalSinceReferenceDate:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/instm/NSDate/initWithTimeIntervalSinceReferenceDate:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithTimeIntervalSinceReferenceDate:(NSTimeInterval)secsToBeAdded |
| To | - (instancetype)initWithTimeIntervalSinceReferenceDate:(NSTimeInterval)ti |

NSDictionary.hAdded [-[NSDictionary init]](https://developer.apple.com/documentation/foundation/nsdictionary/1418147-init)Added [-[NSMutableDictionary init]](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1410577-init)Modified [+[NSDictionary dictionary]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/clm/NSDictionary/dictionary)

|  | Declaration |
| --- | --- |
| From | + (id)dictionary |
| To | + (instancetype)dictionary |

Modified [+[NSDictionary dictionaryWithDictionary:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/clm/NSDictionary/dictionaryWithDictionary:)

|  | Declaration |
| --- | --- |
| From | + (id)dictionaryWithDictionary:(NSDictionary \*)dict |
| To | + (instancetype)dictionaryWithDictionary:(NSDictionary \*)dict |

Modified [+[NSDictionary dictionaryWithObject:forKey:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/clm/NSDictionary/dictionaryWithObject:forKey:)

|  | Declaration |
| --- | --- |
| From | + (id)dictionaryWithObject:(id)object forKey:(id<NSCopying>)key |
| To | + (instancetype)dictionaryWithObject:(id)object forKey:(id<NSCopying>)key |

Modified [+[NSDictionary dictionaryWithObjects:forKeys:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/clm/NSDictionary/dictionaryWithObjects:forKeys:)

|  | Declaration |
| --- | --- |
| From | + (id)dictionaryWithObjects:(NSArray \*)objects forKeys:(NSArray \*)keys |
| To | + (instancetype)dictionaryWithObjects:(NSArray \*)objects forKeys:(NSArray \*)keys |

Modified [+[NSDictionary dictionaryWithObjects:forKeys:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/clm/NSDictionary/dictionaryWithObjects:forKeys:count:)

|  | Declaration |
| --- | --- |
| From | + (id)dictionaryWithObjects:(const id [])objects forKeys:(const id<NSCopying> [])keys count:(NSUInteger)cnt |
| To | + (instancetype)dictionaryWithObjects:(const id [])objects forKeys:(const id<NSCopying> [])keys count:(NSUInteger)cnt |

Modified [+[NSDictionary dictionaryWithObjectsAndKeys:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/clm/NSDictionary/dictionaryWithObjectsAndKeys:)

|  | Declaration |
| --- | --- |
| From | + (id)dictionaryWithObjectsAndKeys:(id)firstObject, ... |
| To | + (instancetype)dictionaryWithObjectsAndKeys:(id)firstObject, ... |

Modified [-[NSDictionary initWithDictionary:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/initWithDictionary:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithDictionary:(NSDictionary \*)otherDictionary |
| To | - (instancetype)initWithDictionary:(NSDictionary \*)otherDictionary |

Modified [-[NSDictionary initWithDictionary:copyItems:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/initWithDictionary:copyItems:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithDictionary:(NSDictionary \*)otherDictionary copyItems:(BOOL)flag |
| To | - (instancetype)initWithDictionary:(NSDictionary \*)otherDictionary copyItems:(BOOL)flag |

Modified [-[NSDictionary initWithObjects:forKeys:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/initWithObjects:forKeys:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObjects:(NSArray \*)objects forKeys:(NSArray \*)keys |
| To | - (instancetype)initWithObjects:(NSArray \*)objects forKeys:(NSArray \*)keys |

Modified [-[NSDictionary initWithObjects:forKeys:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/initWithObjects:forKeys:count:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObjects:(const id [])objects forKeys:(const id<NSCopying> [])keys count:(NSUInteger)cnt |
| To | - (instancetype)initWithObjects:(const id [])objects forKeys:(const id<NSCopying> [])keys count:(NSUInteger)cnt |

Modified [-[NSDictionary initWithObjectsAndKeys:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/initWithObjectsAndKeys:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObjectsAndKeys:(id)firstObject, ... |
| To | - (instancetype)initWithObjectsAndKeys:(id)firstObject, ... |

Modified [+[NSMutableDictionary dictionaryWithCapacity:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/clm/NSMutableDictionary/dictionaryWithCapacity:)

|  | Declaration |
| --- | --- |
| From | + (id)dictionaryWithCapacity:(NSUInteger)numItems |
| To | + (instancetype)dictionaryWithCapacity:(NSUInteger)numItems |

Modified [-[NSMutableDictionary initWithCapacity:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSMutableDictionary/initWithCapacity:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithCapacity:(NSUInteger)numItems |
| To | - (instancetype)initWithCapacity:(NSUInteger)numItems |

NSExpression.hAdded [-[NSExpression allowEvaluation]](https://developer.apple.com/documentation/foundation/nsexpression/1409244-allowevaluation)Added [+[NSExpression expressionForAnyKey]](https://developer.apple.com/documentation/foundation/nsexpression/1410198-expressionforanykey)Added [NSAnyKeyExpressionType](https://developer.apple.com/documentation/foundation/nsexpression/expressiontype/anykey)Modified [NSExpression](https://developer.apple.com/documentation/foundation/nsexpression)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSFileManager.hAdded [-[NSFileManager containerURLForSecurityApplicationGroupIdentifier:]](https://developer.apple.com/documentation/foundation/nsfilemanager/1412643-containerurlforsecurityapplicati)NSIndexPath.hAdded -[NSIndexPath init]Modified [+[NSIndexPath indexPathWithIndex:]](https://developer.apple.com/documentation/foundation/nsindexpath/1521019-indexpathwithindex)

|  | Declaration |
| --- | --- |
| From | + (id)indexPathWithIndex:(NSUInteger)index |
| To | + (instancetype)indexPathWithIndex:(NSUInteger)index |

Modified [+[NSIndexPath indexPathWithIndexes:length:]](https://developer.apple.com/documentation/foundation/nsindexpath/1521015-indexpathwithindexes)

|  | Declaration |
| --- | --- |
| From | + (id)indexPathWithIndexes:(const NSUInteger [])indexes length:(NSUInteger)length |
| To | + (instancetype)indexPathWithIndexes:(const NSUInteger [])indexes length:(NSUInteger)length |

Modified [-[NSIndexPath initWithIndex:]](https://developer.apple.com/documentation/foundation/nsindexpath/1416855-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithIndex:(NSUInteger)index |
| To | - (instancetype)initWithIndex:(NSUInteger)index |

Modified [-[NSIndexPath initWithIndexes:length:]](https://developer.apple.com/documentation/foundation/nsindexpath/1416906-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithIndexes:(const NSUInteger [])indexes length:(NSUInteger)length |
| To | - (instancetype)initWithIndexes:(const NSUInteger [])indexes length:(NSUInteger)length |

NSIndexSet.hModified [+[NSIndexSet indexSet]](https://developer.apple.com/documentation/foundation/nsindexset/1427281-indexset)

|  | Declaration |
| --- | --- |
| From | + (id)indexSet |
| To | + (instancetype)indexSet |

Modified [+[NSIndexSet indexSetWithIndex:]](https://developer.apple.com/documentation/foundation/nsindexset/1427254-indexsetwithindex)

|  | Declaration |
| --- | --- |
| From | + (id)indexSetWithIndex:(NSUInteger)value |
| To | + (instancetype)indexSetWithIndex:(NSUInteger)value |

Modified [+[NSIndexSet indexSetWithIndexesInRange:]](https://developer.apple.com/documentation/foundation/nsindexset/1427274-indexsetwithindexesinrange)

|  | Declaration |
| --- | --- |
| From | + (id)indexSetWithIndexesInRange:(NSRange)range |
| To | + (instancetype)indexSetWithIndexesInRange:(NSRange)range |

Modified [-[NSIndexSet init]](https://developer.apple.com/documentation/foundation/nsindexset/1807255-init)

|  | Declaration |
| --- | --- |
| From | - (id)init |
| To | - (instancetype)init |

Modified [-[NSIndexSet initWithIndex:]](https://developer.apple.com/documentation/foundation/nsindexset/1416501-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithIndex:(NSUInteger)value |
| To | - (instancetype)initWithIndex:(NSUInteger)value |

Modified [-[NSIndexSet initWithIndexSet:]](https://developer.apple.com/documentation/foundation/nsindexset/1415602-initwithindexset)

|  | Declaration |
| --- | --- |
| From | - (id)initWithIndexSet:(NSIndexSet \*)indexSet |
| To | - (instancetype)initWithIndexSet:(NSIndexSet \*)indexSet |

Modified [-[NSIndexSet initWithIndexesInRange:]](https://developer.apple.com/documentation/foundation/nsindexset/1414013-initwithindexesinrange)

|  | Declaration |
| --- | --- |
| From | - (id)initWithIndexesInRange:(NSRange)range |
| To | - (instancetype)initWithIndexesInRange:(NSRange)range |

NSKeyedArchiver.hAdded [-[NSKeyedArchiver setRequiresSecureCoding:]](https://developer.apple.com/documentation/foundation/nskeyedarchiver/1417084-requiressecurecoding)Added [-[NSKeyedUnarchiver setRequiresSecureCoding:]](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/1410824-requiressecurecoding)Added [NSKeyedArchiveRootObjectKey](https://developer.apple.com/documentation/foundation/nskeyedarchiverootobjectkey)NSLocale.hAdded -[NSLocale init]Added [+[NSLocale localeWithLocaleIdentifier:]](https://developer.apple.com/documentation/foundation/nslocale/1488627-localewithlocaleidentifier)Modified [-[NSLocale initWithLocaleIdentifier:]](https://developer.apple.com/documentation/foundation/nslocale/1414217-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithLocaleIdentifier:(NSString \*)string |
| To | - (instancetype)initWithLocaleIdentifier:(NSString \*)string |

NSMetadata.hAdded [-[NSMetadataQuery enumerateResultsUsingBlock:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1415856-enumerateresults)Added [-[NSMetadataQuery enumerateResultsWithOptions:usingBlock:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1415123-enumerateresults)Added [-[NSMetadataQuery operationQueue]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1410953-operationqueue)Added [-[NSMetadataQuery searchItems]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411307-searchitems)Added [-[NSMetadataQuery setOperationQueue:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1410953-operationqueue)Added [-[NSMetadataQuery setSearchItems:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411307-searchitems)Added [NSMetadataQueryUpdateAddedItemsKey](https://developer.apple.com/documentation/foundation/nsmetadataqueryupdateaddeditemskey)Added [NSMetadataQueryUpdateChangedItemsKey](https://developer.apple.com/documentation/foundation/nsmetadataqueryupdatechangeditemskey)Added [NSMetadataQueryUpdateRemovedItemsKey](https://developer.apple.com/documentation/foundation/nsmetadataqueryupdateremoveditemskey)Modified [NSMetadataItemDisplayNameKey](https://developer.apple.com/documentation/foundation/nsmetadataitemdisplaynamekey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemFSContentChangeDateKey](https://developer.apple.com/documentation/foundation/nsmetadataitemfscontentchangedatekey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemFSCreationDateKey](https://developer.apple.com/documentation/foundation/nsmetadataitemfscreationdatekey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemFSNameKey](https://developer.apple.com/documentation/foundation/nsmetadataitemfsnamekey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemFSSizeKey](https://developer.apple.com/documentation/foundation/nsmetadataitemfssizekey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemIsUbiquitousKey](https://developer.apple.com/documentation/foundation/nsmetadataitemisubiquitouskey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemPathKey](https://developer.apple.com/documentation/foundation/nsmetadataitempathkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemURLKey](https://developer.apple.com/documentation/foundation/nsmetadataitemurlkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataUbiquitousItemHasUnresolvedConflictsKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemhasunresolvedconflictskey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataUbiquitousItemIsDownloadedKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemisdownloadedkey)

|  | Header | Deprecation |
| --- | --- | --- |
| From | Foundation/NSMetadata.h | _none_ |
| To | Foundation/NSMetadataAttributes.h | iOS 7.0 |

Modified [NSMetadataUbiquitousItemIsDownloadingKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemisdownloadingkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataUbiquitousItemIsUploadedKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemisuploadedkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataUbiquitousItemIsUploadingKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemisuploadingkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataUbiquitousItemPercentDownloadedKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitempercentdownloadedkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataUbiquitousItemPercentUploadedKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitempercentuploadedkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

NSMetadataAttributes.hAdded [NSMetadataUbiquitousItemDownloadingErrorKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemdownloadingerrorkey)Added [NSMetadataUbiquitousItemDownloadingStatusCurrent](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemdownloadingstatuscurrent)Added [NSMetadataUbiquitousItemDownloadingStatusDownloaded](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemdownloadingstatusdownloaded)Added [NSMetadataUbiquitousItemDownloadingStatusKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemdownloadingstatuskey)Added [NSMetadataUbiquitousItemDownloadingStatusNotDownloaded](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemdownloadingstatusnotdownloaded)Added [NSMetadataUbiquitousItemUploadingErrorKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemuploadingerrorkey)Modified [NSMetadataItemDisplayNameKey](https://developer.apple.com/documentation/foundation/nsmetadataitemdisplaynamekey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemFSContentChangeDateKey](https://developer.apple.com/documentation/foundation/nsmetadataitemfscontentchangedatekey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemFSCreationDateKey](https://developer.apple.com/documentation/foundation/nsmetadataitemfscreationdatekey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemFSNameKey](https://developer.apple.com/documentation/foundation/nsmetadataitemfsnamekey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemFSSizeKey](https://developer.apple.com/documentation/foundation/nsmetadataitemfssizekey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemIsUbiquitousKey](https://developer.apple.com/documentation/foundation/nsmetadataitemisubiquitouskey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemPathKey](https://developer.apple.com/documentation/foundation/nsmetadataitempathkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemURLKey](https://developer.apple.com/documentation/foundation/nsmetadataitemurlkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataUbiquitousItemHasUnresolvedConflictsKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemhasunresolvedconflictskey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataUbiquitousItemIsDownloadedKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemisdownloadedkey)

|  | Header | Deprecation |
| --- | --- | --- |
| From | Foundation/NSMetadata.h | _none_ |
| To | Foundation/NSMetadataAttributes.h | iOS 7.0 |

Modified [NSMetadataUbiquitousItemIsDownloadingKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemisdownloadingkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataUbiquitousItemIsUploadedKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemisuploadedkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataUbiquitousItemIsUploadingKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemisuploadingkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataUbiquitousItemPercentDownloadedKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitempercentdownloadedkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataUbiquitousItemPercentUploadedKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitempercentuploadedkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

NSNetServices.hRemoved [-[NSNetService addresses]](https://developer.apple.com/documentation/foundation/netservice/1408528-addresses)Removed [-[NSNetService delegate]](https://developer.apple.com/documentation/foundation/netservice/1410296-delegate)Removed [-[NSNetService domain]](https://developer.apple.com/documentation/foundation/nsnetservice/1414495-domain)Removed [-[NSNetService hostName]](https://developer.apple.com/documentation/foundation/nsnetservice/1413300-hostname)Removed [-[NSNetService name]](https://developer.apple.com/documentation/foundation/nsnetservice/1409022-name)Removed [-[NSNetService port]](https://developer.apple.com/documentation/foundation/nsnetservice/1409816-port)Removed [-[NSNetService setDelegate:]](https://developer.apple.com/documentation/foundation/netservice/1410296-delegate)Removed [-[NSNetService type]](https://developer.apple.com/documentation/foundation/nsnetservice/1416595-type)Removed [-[NSNetServiceBrowser delegate]](https://developer.apple.com/documentation/foundation/netservicebrowser/1409380-delegate)Removed [-[NSNetServiceBrowser setDelegate:]](https://developer.apple.com/documentation/foundation/nsnetservicebrowser/1409380-delegate)Added [NSNetService.addresses](https://developer.apple.com/documentation/foundation/netservice/1408528-addresses)Added [NSNetService.delegate](https://developer.apple.com/documentation/foundation/nsnetservice/1410296-delegate)Added [NSNetService.domain](https://developer.apple.com/documentation/foundation/nsnetservice/1414495-domain)Added [NSNetService.hostName](https://developer.apple.com/documentation/foundation/netservice/1413300-hostname)Added [NSNetService.includesPeerToPeer](https://developer.apple.com/documentation/foundation/netservice/1414086-includespeertopeer)Added [NSNetService.name](https://developer.apple.com/documentation/foundation/nsnetservice/1409022-name)Added [NSNetService.port](https://developer.apple.com/documentation/foundation/netservice/1409816-port)Added [NSNetService.type](https://developer.apple.com/documentation/foundation/netservice/1416595-type)Added [NSNetServiceBrowser.delegate](https://developer.apple.com/documentation/foundation/nsnetservicebrowser/1409380-delegate)Added [NSNetServiceBrowser.includesPeerToPeer](https://developer.apple.com/documentation/foundation/nsnetservicebrowser/1413106-includespeertopeer)Added [-[NSNetServiceDelegate netService:didAcceptConnectionWithInputStream:outputStream:]](https://developer.apple.com/documentation/foundation/nsnetservicedelegate/1407489-netservice)Added [NSNetServiceListenForConnections](https://developer.apple.com/documentation/foundation/nsnetserviceoptions/nsnetservicelistenforconnections)NSNotification.hAdded [-[NSNotification init]](https://developer.apple.com/documentation/foundation/nsnotification/1412595-init)Added [-[NSNotification initWithName:object:userInfo:]](https://developer.apple.com/documentation/foundation/nsnotification/1415764-init)Added -[NSNotificationCenter init]Modified [+[NSNotification notificationWithName:object:]](https://developer.apple.com/documentation/foundation/nsnotification/1417440-notificationwithname)

|  | Declaration |
| --- | --- |
| From | + (id)notificationWithName:(NSString \*)aName object:(id)anObject |
| To | + (instancetype)notificationWithName:(NSString \*)aName object:(id)anObject |

Modified [+[NSNotification notificationWithName:object:userInfo:]](https://developer.apple.com/documentation/foundation/nsnotification/1574705-notificationwithname)

|  | Declaration |
| --- | --- |
| From | + (id)notificationWithName:(NSString \*)aName object:(id)anObject userInfo:(NSDictionary \*)aUserInfo |
| To | + (instancetype)notificationWithName:(NSString \*)aName object:(id)anObject userInfo:(NSDictionary \*)aUserInfo |

Modified [+[NSNotificationCenter defaultCenter]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationCenter/Description.html#//apple_ref/occ/clm/NSNotificationCenter/defaultCenter)

|  | Declaration |
| --- | --- |
| From | + (id)defaultCenter |
| To | + (instancetype)defaultCenter |

NSObjCRuntime.hAdded [#def NSFoundationVersionNumber10_8](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_8)Added [#def NSFoundationVersionNumber10_8_1](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_8_1)Added [#def NSFoundationVersionNumber10_8_2](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_8_2)Added [#def NSFoundationVersionNumber10_8_3](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_8_3)Added [#def NSFoundationVersionNumber10_8_4](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_8_4)Added [#def NSFoundationVersionNumber_iOS_6_0](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber_ios_6_0)Added [#def NSFoundationVersionNumber_iOS_6_1](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber_ios_6_1)Added #def NS_CLASS_DEPRECATEDAdded #def NS_CLASS_DEPRECATED_IOSAdded #def NS_CLASS_DEPRECATED_MACModified #def NSINTEGER_DEFINED

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

NSObject.hModified [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intf/NSObject)

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

Modified [+[NSObject class]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/class)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject class]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/class)

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

NSOrderedSet.hAdded [-[NSMutableOrderedSet init]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1410545-init)Added [-[NSOrderedSet init]](https://developer.apple.com/documentation/foundation/nsorderedset/1417735-init)Modified [-[NSMutableOrderedSet initWithCapacity:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1411583-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithCapacity:(NSUInteger)numItems |
| To | - (instancetype)initWithCapacity:(NSUInteger)numItems |

Modified [+[NSMutableOrderedSet orderedSetWithCapacity:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1543283-orderedsetwithcapacity)

|  | Declaration |
| --- | --- |
| From | + (id)orderedSetWithCapacity:(NSUInteger)numItems |
| To | + (instancetype)orderedSetWithCapacity:(NSUInteger)numItems |

Modified [-[NSOrderedSet initWithArray:]](https://developer.apple.com/documentation/foundation/nsorderedset/1408623-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithArray:(NSArray \*)array |
| To | - (instancetype)initWithArray:(NSArray \*)array |

Modified [-[NSOrderedSet initWithArray:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1418006-initwitharray)

|  | Declaration |
| --- | --- |
| From | - (id)initWithArray:(NSArray \*)set copyItems:(BOOL)flag |
| To | - (instancetype)initWithArray:(NSArray \*)set copyItems:(BOOL)flag |

Modified [-[NSOrderedSet initWithArray:range:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1409272-initwitharray)

|  | Declaration |
| --- | --- |
| From | - (id)initWithArray:(NSArray \*)set range:(NSRange)range copyItems:(BOOL)flag |
| To | - (instancetype)initWithArray:(NSArray \*)set range:(NSRange)range copyItems:(BOOL)flag |

Modified [-[NSOrderedSet initWithObject:]](https://developer.apple.com/documentation/foundation/nsorderedset/1413883-initwithobject)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObject:(id)object |
| To | - (instancetype)initWithObject:(id)object |

Modified [-[NSOrderedSet initWithObjects:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543287-initwithobjects)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObjects:(id)firstObj, ... |
| To | - (instancetype)initWithObjects:(id)firstObj, ... |

Modified [-[NSOrderedSet initWithObjects:count:]](https://developer.apple.com/documentation/foundation/nsorderedset/1411910-initwithobjects)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObjects:(const id [])objects count:(NSUInteger)cnt |
| To | - (instancetype)initWithObjects:(const id [])objects count:(NSUInteger)cnt |

Modified [-[NSOrderedSet initWithOrderedSet:]](https://developer.apple.com/documentation/foundation/nsorderedset/1412402-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithOrderedSet:(NSOrderedSet \*)set |
| To | - (instancetype)initWithOrderedSet:(NSOrderedSet \*)set |

Modified [-[NSOrderedSet initWithOrderedSet:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1411658-initwithorderedset)

|  | Declaration |
| --- | --- |
| From | - (id)initWithOrderedSet:(NSOrderedSet \*)set copyItems:(BOOL)flag |
| To | - (instancetype)initWithOrderedSet:(NSOrderedSet \*)set copyItems:(BOOL)flag |

Modified [-[NSOrderedSet initWithOrderedSet:range:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1417751-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithOrderedSet:(NSOrderedSet \*)set range:(NSRange)range copyItems:(BOOL)flag |
| To | - (instancetype)initWithOrderedSet:(NSOrderedSet \*)set range:(NSRange)range copyItems:(BOOL)flag |

Modified [-[NSOrderedSet initWithSet:]](https://developer.apple.com/documentation/foundation/nsorderedset/1416344-initwithset)

|  | Declaration |
| --- | --- |
| From | - (id)initWithSet:(NSSet \*)set |
| To | - (instancetype)initWithSet:(NSSet \*)set |

Modified [-[NSOrderedSet initWithSet:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1411246-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithSet:(NSSet \*)set copyItems:(BOOL)flag |
| To | - (instancetype)initWithSet:(NSSet \*)set copyItems:(BOOL)flag |

Modified [+[NSOrderedSet orderedSet]](https://developer.apple.com/documentation/foundation/nsorderedset/1543313-orderedset)

|  | Declaration |
| --- | --- |
| From | + (id)orderedSet |
| To | + (instancetype)orderedSet |

Modified [+[NSOrderedSet orderedSetWithArray:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543310-orderedsetwitharray)

|  | Declaration |
| --- | --- |
| From | + (id)orderedSetWithArray:(NSArray \*)array |
| To | + (instancetype)orderedSetWithArray:(NSArray \*)array |

Modified [+[NSOrderedSet orderedSetWithArray:range:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543321-orderedsetwitharray)

|  | Declaration |
| --- | --- |
| From | + (id)orderedSetWithArray:(NSArray \*)array range:(NSRange)range copyItems:(BOOL)flag |
| To | + (instancetype)orderedSetWithArray:(NSArray \*)array range:(NSRange)range copyItems:(BOOL)flag |

Modified [+[NSOrderedSet orderedSetWithObject:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543339-orderedsetwithobject)

|  | Declaration |
| --- | --- |
| From | + (id)orderedSetWithObject:(id)object |
| To | + (instancetype)orderedSetWithObject:(id)object |

Modified [+[NSOrderedSet orderedSetWithObjects:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543312-orderedsetwithobjects)

|  | Declaration |
| --- | --- |
| From | + (id)orderedSetWithObjects:(id)firstObj, ... |
| To | + (instancetype)orderedSetWithObjects:(id)firstObj, ... |

Modified [+[NSOrderedSet orderedSetWithObjects:count:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543334-init)

|  | Declaration |
| --- | --- |
| From | + (id)orderedSetWithObjects:(const id [])objects count:(NSUInteger)cnt |
| To | + (instancetype)orderedSetWithObjects:(const id [])objects count:(NSUInteger)cnt |

Modified [+[NSOrderedSet orderedSetWithOrderedSet:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543280-orderedsetwithorderedset)

|  | Declaration |
| --- | --- |
| From | + (id)orderedSetWithOrderedSet:(NSOrderedSet \*)set |
| To | + (instancetype)orderedSetWithOrderedSet:(NSOrderedSet \*)set |

Modified [+[NSOrderedSet orderedSetWithOrderedSet:range:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543292-orderedsetwithorderedset)

|  | Declaration |
| --- | --- |
| From | + (id)orderedSetWithOrderedSet:(NSOrderedSet \*)set range:(NSRange)range copyItems:(BOOL)flag |
| To | + (instancetype)orderedSetWithOrderedSet:(NSOrderedSet \*)set range:(NSRange)range copyItems:(BOOL)flag |

Modified [+[NSOrderedSet orderedSetWithSet:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543298-orderedsetwithset)

|  | Declaration |
| --- | --- |
| From | + (id)orderedSetWithSet:(NSSet \*)set |
| To | + (instancetype)orderedSetWithSet:(NSSet \*)set |

Modified [+[NSOrderedSet orderedSetWithSet:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543331-orderedsetwithset)

|  | Declaration |
| --- | --- |
| From | + (id)orderedSetWithSet:(NSSet \*)set copyItems:(BOOL)flag |
| To | + (instancetype)orderedSetWithSet:(NSSet \*)set copyItems:(BOOL)flag |

NSPredicate.hAdded [-[NSMutableOrderedSet filterUsingPredicate:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1408348-filterusingpredicate)Added [-[NSOrderedSet filteredOrderedSetUsingPredicate:]](https://developer.apple.com/documentation/foundation/nsorderedset/1415807-filtered)Added [-[NSPredicate allowEvaluation]](https://developer.apple.com/documentation/foundation/nspredicate/1416310-allowevaluation)Added NSMutableOrderedSet(NSPredicateSupport)Added NSOrderedSet(NSPredicateSupport)Modified [NSPredicate](https://developer.apple.com/documentation/foundation/nspredicate)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSProcessInfo.hAdded [-[NSProcessInfo beginActivityWithOptions:reason:]](https://developer.apple.com/documentation/foundation/nsprocessinfo/1415995-beginactivitywithoptions)Added [-[NSProcessInfo endActivity:]](https://developer.apple.com/documentation/foundation/processinfo/1411321-endactivity)Added [-[NSProcessInfo performActivityWithOptions:reason:usingBlock:]](https://developer.apple.com/documentation/foundation/processinfo/1418048-performactivity)Added [NSActivityAutomaticTerminationDisabled](https://developer.apple.com/documentation/foundation/nsactivityoptions/nsactivityautomaticterminationdisabled)Added [NSActivityBackground](https://developer.apple.com/documentation/foundation/nsactivityoptions/nsactivitybackground)Added [NSActivityIdleDisplaySleepDisabled](https://developer.apple.com/documentation/foundation/nsactivityoptions/nsactivityidledisplaysleepdisabled)Added [NSActivityIdleSystemSleepDisabled](https://developer.apple.com/documentation/foundation/nsactivityoptions/nsactivityidlesystemsleepdisabled)Added [NSActivityLatencyCritical](https://developer.apple.com/documentation/foundation/processinfo/activityoptions/1415541-latencycritical)Added [NSActivityOptions](https://developer.apple.com/documentation/foundation/processinfo/activityoptions)Added [NSActivitySuddenTerminationDisabled](https://developer.apple.com/documentation/foundation/nsactivityoptions/nsactivitysuddenterminationdisabled)Added [NSActivityUserInitiated](https://developer.apple.com/documentation/foundation/nsactivityoptions/nsactivityuserinitiated)Added [NSActivityUserInitiatedAllowingIdleSystemSleep](https://developer.apple.com/documentation/foundation/processinfo/activityoptions/1414902-userinitiatedallowingidlesystems)Added NSProcessInfo()NSProgress.hAdded [NSProgress](https://developer.apple.com/documentation/foundation/nsprogress)Added [-[NSProgress becomeCurrentWithPendingUnitCount:]](https://developer.apple.com/documentation/foundation/progress/1410103-becomecurrent)Added [-[NSProgress cancel]](https://developer.apple.com/documentation/foundation/nsprogress/1413832-cancel)Added [NSProgress.cancellable](https://developer.apple.com/documentation/foundation/nsprogress/1409348-cancellable)Added [NSProgress.cancellationHandler](https://developer.apple.com/documentation/foundation/nsprogress/1408913-cancellationhandler)Added [NSProgress.cancelled](https://developer.apple.com/documentation/foundation/progress/1414454-iscancelled)Added [NSProgress.completedUnitCount](https://developer.apple.com/documentation/foundation/nsprogress/1407934-completedunitcount)Added [+[NSProgress currentProgress]](https://developer.apple.com/documentation/foundation/nsprogress/1412499-currentprogress)Added [NSProgress.fractionCompleted](https://developer.apple.com/documentation/foundation/nsprogress/1408579-fractioncompleted)Added [NSProgress.indeterminate](https://developer.apple.com/documentation/foundation/progress/1412871-isindeterminate)Added [-[NSProgress initWithParent:userInfo:]](https://developer.apple.com/documentation/foundation/progress/1409133-init)Added [NSProgress.kind](https://developer.apple.com/documentation/foundation/progress/1416139-kind)Added [NSProgress.localizedAdditionalDescription](https://developer.apple.com/documentation/foundation/nsprogress/1412455-localizedadditionaldescription)Added [NSProgress.localizedDescription](https://developer.apple.com/documentation/foundation/nsprogress/1417251-localizeddescription)Added [NSProgress.pausable](https://developer.apple.com/documentation/foundation/progress/1417421-ispausable)Added [-[NSProgress pause]](https://developer.apple.com/documentation/foundation/nsprogress/1412377-pause)Added [NSProgress.paused](https://developer.apple.com/documentation/foundation/progress/1415495-ispaused)Added [NSProgress.pausingHandler](https://developer.apple.com/documentation/foundation/nsprogress/1412873-pausinghandler)Added [+[NSProgress progressWithTotalUnitCount:]](https://developer.apple.com/documentation/foundation/nsprogress/1415509-progresswithtotalunitcount)Added [-[NSProgress resignCurrent]](https://developer.apple.com/documentation/foundation/nsprogress/1407180-resigncurrent)Added [-[NSProgress setUserInfoObject:forKey:]](https://developer.apple.com/documentation/foundation/nsprogress/1407537-setuserinfoobject)Added [NSProgress.totalUnitCount](https://developer.apple.com/documentation/foundation/nsprogress/1410940-totalunitcount)Added [-[NSProgress userInfo]](https://developer.apple.com/documentation/foundation/progress/1413314-userinfo)Added [NSProgressEstimatedTimeRemainingKey](https://developer.apple.com/documentation/foundation/progressuserinfokey/1407371-estimatedtimeremainingkey)Added [NSProgressFileCompletedCountKey](https://developer.apple.com/documentation/foundation/nsprogressfilecompletedcountkey)Added [NSProgressFileOperationKindCopying](https://developer.apple.com/documentation/foundation/progress/fileoperationkind/1415785-copying)Added [NSProgressFileOperationKindDecompressingAfterDownloading](https://developer.apple.com/documentation/foundation/progress/fileoperationkind/1410985-decompressingafterdownloading)Added [NSProgressFileOperationKindDownloading](https://developer.apple.com/documentation/foundation/nsprogressfileoperationkinddownloading)Added [NSProgressFileOperationKindKey](https://developer.apple.com/documentation/foundation/progressuserinfokey/1408097-fileoperationkindkey)Added [NSProgressFileOperationKindReceiving](https://developer.apple.com/documentation/foundation/nsprogressfileoperationkindreceiving)Added [NSProgressFileTotalCountKey](https://developer.apple.com/documentation/foundation/nsprogressfiletotalcountkey)Added [NSProgressFileURLKey](https://developer.apple.com/documentation/foundation/progressuserinfokey/1408815-fileurlkey)Added [NSProgressKindFile](https://developer.apple.com/documentation/foundation/progresskind/1409141-file)Added [NSProgressPublishingHandler](https://developer.apple.com/documentation/foundation/nsprogresspublishinghandler)Added [NSProgressThroughputKey](https://developer.apple.com/documentation/foundation/nsprogressthroughputkey)Added [NSProgressUnpublishingHandler](https://developer.apple.com/documentation/foundation/progress/unpublishinghandler)NSScanner.hAdded [-[NSScanner scanUnsignedLongLong:]](https://developer.apple.com/documentation/foundation/scanner/1408559-scanunsignedlonglong)Modified [-[NSScanner scanCharactersFromSet:intoString:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/scanCharactersFromSet:intoString:)

|  | Declaration |
| --- | --- |
| From | - (BOOL)scanCharactersFromSet:(NSCharacterSet \*)set intoString:(NSString \*\*)value |
| To | - (BOOL)scanCharactersFromSet:(NSCharacterSet \*)set intoString:(NSString \*\*)result |

Modified [-[NSScanner scanDouble:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/scanDouble:)

|  | Declaration |
| --- | --- |
| From | - (BOOL)scanDouble:(double \*)value |
| To | - (BOOL)scanDouble:(double \*)result |

Modified [-[NSScanner scanFloat:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/scanFloat:)

|  | Declaration |
| --- | --- |
| From | - (BOOL)scanFloat:(float \*)value |
| To | - (BOOL)scanFloat:(float \*)result |

Modified [-[NSScanner scanHexInt:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/scanHexInt:)

|  | Declaration |
| --- | --- |
| From | - (BOOL)scanHexInt:(unsigned int \*)value |
| To | - (BOOL)scanHexInt:(unsigned int \*)result |

Modified [-[NSScanner scanInt:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/scanInt:)

|  | Declaration |
| --- | --- |
| From | - (BOOL)scanInt:(int \*)value |
| To | - (BOOL)scanInt:(int \*)result |

Modified [-[NSScanner scanInteger:]](https://developer.apple.com/documentation/foundation/nsscanner/1411082-scaninteger)

|  | Declaration |
| --- | --- |
| From | - (BOOL)scanInteger:(NSInteger \*)value |
| To | - (BOOL)scanInteger:(NSInteger \*)result |

Modified [-[NSScanner scanLongLong:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/scanLongLong:)

|  | Declaration |
| --- | --- |
| From | - (BOOL)scanLongLong:(long long \*)value |
| To | - (BOOL)scanLongLong:(long long \*)result |

Modified [-[NSScanner scanString:intoString:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/scanString:intoString:)

|  | Declaration |
| --- | --- |
| From | - (BOOL)scanString:(NSString \*)string intoString:(NSString \*\*)value |
| To | - (BOOL)scanString:(NSString \*)string intoString:(NSString \*\*)result |

Modified [-[NSScanner scanUpToCharactersFromSet:intoString:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/scanUpToCharactersFromSet:intoString:)

|  | Declaration |
| --- | --- |
| From | - (BOOL)scanUpToCharactersFromSet:(NSCharacterSet \*)set intoString:(NSString \*\*)value |
| To | - (BOOL)scanUpToCharactersFromSet:(NSCharacterSet \*)set intoString:(NSString \*\*)result |

Modified [-[NSScanner scanUpToString:intoString:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/scanUpToString:intoString:)

|  | Declaration |
| --- | --- |
| From | - (BOOL)scanUpToString:(NSString \*)string intoString:(NSString \*\*)value |
| To | - (BOOL)scanUpToString:(NSString \*)string intoString:(NSString \*\*)result |

NSSet.hAdded [-[NSMutableSet init]](https://developer.apple.com/documentation/foundation/nsmutableset/1414518-init)Added [-[NSSet init]](https://developer.apple.com/documentation/foundation/nsset/1409698-init)Modified [-[NSMutableSet initWithCapacity:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/initWithCapacity:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithCapacity:(NSUInteger)numItems |
| To | - (instancetype)initWithCapacity:(NSUInteger)numItems |

Modified [+[NSMutableSet setWithCapacity:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/clm/NSMutableSet/setWithCapacity:)

|  | Declaration |
| --- | --- |
| From | + (id)setWithCapacity:(NSUInteger)numItems |
| To | + (instancetype)setWithCapacity:(NSUInteger)numItems |

Modified [-[NSSet initWithArray:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/initWithArray:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithArray:(NSArray \*)array |
| To | - (instancetype)initWithArray:(NSArray \*)array |

Modified [-[NSSet initWithObjects:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/initWithObjects:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObjects:(id)firstObj, ... |
| To | - (instancetype)initWithObjects:(id)firstObj, ... |

Modified [-[NSSet initWithObjects:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/initWithObjects:count:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObjects:(const id [])objects count:(NSUInteger)cnt |
| To | - (instancetype)initWithObjects:(const id [])objects count:(NSUInteger)cnt |

Modified [-[NSSet initWithSet:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/initWithSet:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithSet:(NSSet \*)set |
| To | - (instancetype)initWithSet:(NSSet \*)set |

Modified [-[NSSet initWithSet:copyItems:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/initWithSet:copyItems:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithSet:(NSSet \*)set copyItems:(BOOL)flag |
| To | - (instancetype)initWithSet:(NSSet \*)set copyItems:(BOOL)flag |

Modified [+[NSSet set]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/clm/NSSet/set)

|  | Declaration |
| --- | --- |
| From | + (id)set |
| To | + (instancetype)set |

Modified [+[NSSet setWithArray:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/clm/NSSet/setWithArray:)

|  | Declaration |
| --- | --- |
| From | + (id)setWithArray:(NSArray \*)array |
| To | + (instancetype)setWithArray:(NSArray \*)array |

Modified [+[NSSet setWithObject:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/clm/NSSet/setWithObject:)

|  | Declaration |
| --- | --- |
| From | + (id)setWithObject:(id)object |
| To | + (instancetype)setWithObject:(id)object |

Modified [+[NSSet setWithObjects:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/clm/NSSet/setWithObjects:)

|  | Declaration |
| --- | --- |
| From | + (id)setWithObjects:(id)firstObj, ... |
| To | + (instancetype)setWithObjects:(id)firstObj, ... |

Modified [+[NSSet setWithObjects:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/clm/NSSet/setWithObjects:count:)

|  | Declaration |
| --- | --- |
| From | + (id)setWithObjects:(const id [])objects count:(NSUInteger)cnt |
| To | + (instancetype)setWithObjects:(const id [])objects count:(NSUInteger)cnt |

Modified [+[NSSet setWithSet:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/clm/NSSet/setWithSet:)

|  | Declaration |
| --- | --- |
| From | + (id)setWithSet:(NSSet \*)set |
| To | + (instancetype)setWithSet:(NSSet \*)set |

NSSortDescriptor.hAdded [-[NSMutableOrderedSet sortUsingDescriptors:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1410023-sort)Added [-[NSOrderedSet sortedArrayUsingDescriptors:]](https://developer.apple.com/documentation/foundation/nsorderedset/1409953-sortedarray)Added [-[NSSortDescriptor allowEvaluation]](https://developer.apple.com/documentation/foundation/nssortdescriptor/1412371-allowevaluation)Added NSMutableOrderedSet(NSKeyValueSorting)Added NSOrderedSet(NSKeyValueSorting)Modified [NSSortDescriptor](https://developer.apple.com/documentation/foundation/nssortdescriptor)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSString.hModified [-[NSString init]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/init)

|  | Declaration |
| --- | --- |
| From | - (id)init |
| To | - (instancetype)init |

Modified [-[NSString initWithBytes:length:encoding:]](https://developer.apple.com/documentation/foundation/nsstring/1407339-initwithbytes)

|  | Declaration |
| --- | --- |
| From | - (id)initWithBytes:(const void \*)bytes length:(NSUInteger)len encoding:(NSStringEncoding)encoding |
| To | - (instancetype)initWithBytes:(const void \*)bytes length:(NSUInteger)len encoding:(NSStringEncoding)encoding |

Modified [-[NSString initWithBytesNoCopy:length:encoding:freeWhenDone:]](https://developer.apple.com/documentation/foundation/nsstring/1413830-initwithbytesnocopy)

|  | Declaration |
| --- | --- |
| From | - (id)initWithBytesNoCopy:(void \*)bytes length:(NSUInteger)len encoding:(NSStringEncoding)encoding freeWhenDone:(BOOL)freeBuffer |
| To | - (instancetype)initWithBytesNoCopy:(void \*)bytes length:(NSUInteger)len encoding:(NSStringEncoding)encoding freeWhenDone:(BOOL)freeBuffer |

Modified [-[NSString initWithCString:encoding:]](https://developer.apple.com/documentation/foundation/nsstring/1411950-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithCString:(const char \*)nullTerminatedCString encoding:(NSStringEncoding)encoding |
| To | - (instancetype)initWithCString:(const char \*)nullTerminatedCString encoding:(NSStringEncoding)encoding |

Modified [-[NSString initWithCharacters:length:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/initWithCharacters:length:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithCharacters:(const unichar \*)characters length:(NSUInteger)length |
| To | - (instancetype)initWithCharacters:(const unichar \*)characters length:(NSUInteger)length |

Modified [-[NSString initWithCharactersNoCopy:length:freeWhenDone:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/initWithCharactersNoCopy:length:freeWhenDone:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithCharactersNoCopy:(unichar \*)characters length:(NSUInteger)length freeWhenDone:(BOOL)freeBuffer |
| To | - (instancetype)initWithCharactersNoCopy:(unichar \*)characters length:(NSUInteger)length freeWhenDone:(BOOL)freeBuffer |

Modified [-[NSString initWithContentsOfFile:encoding:error:]](https://developer.apple.com/documentation/foundation/nsstring/1412610-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithContentsOfFile:(NSString \*)path encoding:(NSStringEncoding)enc error:(NSError \*\*)error |
| To | - (instancetype)initWithContentsOfFile:(NSString \*)path encoding:(NSStringEncoding)enc error:(NSError \*\*)error |

Modified [-[NSString initWithContentsOfFile:usedEncoding:error:]](https://developer.apple.com/documentation/foundation/nsstring/1418227-initwithcontentsoffile)

|  | Declaration |
| --- | --- |
| From | - (id)initWithContentsOfFile:(NSString \*)path usedEncoding:(NSStringEncoding \*)enc error:(NSError \*\*)error |
| To | - (instancetype)initWithContentsOfFile:(NSString \*)path usedEncoding:(NSStringEncoding \*)enc error:(NSError \*\*)error |

Modified [-[NSString initWithContentsOfURL:encoding:error:]](https://developer.apple.com/documentation/foundation/nsstring/1414463-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithContentsOfURL:(NSURL \*)url encoding:(NSStringEncoding)enc error:(NSError \*\*)error |
| To | - (instancetype)initWithContentsOfURL:(NSURL \*)url encoding:(NSStringEncoding)enc error:(NSError \*\*)error |

Modified [-[NSString initWithContentsOfURL:usedEncoding:error:]](https://developer.apple.com/documentation/foundation/nsstring/1414472-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithContentsOfURL:(NSURL \*)url usedEncoding:(NSStringEncoding \*)enc error:(NSError \*\*)error |
| To | - (instancetype)initWithContentsOfURL:(NSURL \*)url usedEncoding:(NSStringEncoding \*)enc error:(NSError \*\*)error |

Modified [-[NSString initWithData:encoding:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/initWithData:encoding:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithData:(NSData \*)data encoding:(NSStringEncoding)encoding |
| To | - (instancetype)initWithData:(NSData \*)data encoding:(NSStringEncoding)encoding |

Modified [-[NSString initWithFormat:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/initWithFormat:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithFormat:(NSString \*)format, ... |
| To | - (instancetype)initWithFormat:(NSString \*)format, ... |

Modified [-[NSString initWithFormat:arguments:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/initWithFormat:arguments:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithFormat:(NSString \*)format arguments:(va_list)argList |
| To | - (instancetype)initWithFormat:(NSString \*)format arguments:(va_list)argList |

Modified [-[NSString initWithFormat:locale:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/initWithFormat:locale:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithFormat:(NSString \*)format locale:(id)locale, ... |
| To | - (instancetype)initWithFormat:(NSString \*)format locale:(id)locale, ... |

Modified [-[NSString initWithFormat:locale:arguments:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/initWithFormat:locale:arguments:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithFormat:(NSString \*)format locale:(id)locale arguments:(va_list)argList |
| To | - (instancetype)initWithFormat:(NSString \*)format locale:(id)locale arguments:(va_list)argList |

Modified [-[NSString initWithString:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/initWithString:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithString:(NSString \*)aString |
| To | - (instancetype)initWithString:(NSString \*)aString |

Modified [-[NSString initWithUTF8String:]](https://developer.apple.com/documentation/foundation/nsstring/1412128-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithUTF8String:(const char \*)nullTerminatedCString |
| To | - (instancetype)initWithUTF8String:(const char \*)nullTerminatedCString |

Modified [+[NSString localizedStringWithFormat:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/clm/NSString/localizedStringWithFormat:)

|  | Declaration |
| --- | --- |
| From | + (id)localizedStringWithFormat:(NSString \*)format, ... |
| To | + (instancetype)localizedStringWithFormat:(NSString \*)format, ... |

Modified [+[NSString string]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/clm/NSString/string)

|  | Declaration |
| --- | --- |
| From | + (id)string |
| To | + (instancetype)string |

Modified [+[NSString stringWithCString:encoding:]](https://developer.apple.com/documentation/foundation/nsstring/1497310-stringwithcstring)

|  | Declaration |
| --- | --- |
| From | + (id)stringWithCString:(const char \*)cString encoding:(NSStringEncoding)enc |
| To | + (instancetype)stringWithCString:(const char \*)cString encoding:(NSStringEncoding)enc |

Modified [+[NSString stringWithCharacters:length:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/clm/NSString/stringWithCharacters:length:)

|  | Declaration |
| --- | --- |
| From | + (id)stringWithCharacters:(const unichar \*)characters length:(NSUInteger)length |
| To | + (instancetype)stringWithCharacters:(const unichar \*)characters length:(NSUInteger)length |

Modified [+[NSString stringWithContentsOfFile:encoding:error:]](https://developer.apple.com/documentation/foundation/nsstring/1497327-stringwithcontentsoffile)

|  | Declaration |
| --- | --- |
| From | + (id)stringWithContentsOfFile:(NSString \*)path encoding:(NSStringEncoding)enc error:(NSError \*\*)error |
| To | + (instancetype)stringWithContentsOfFile:(NSString \*)path encoding:(NSStringEncoding)enc error:(NSError \*\*)error |

Modified [+[NSString stringWithContentsOfFile:usedEncoding:error:]](https://developer.apple.com/documentation/foundation/nsstring/1497254-stringwithcontentsoffile)

|  | Declaration |
| --- | --- |
| From | + (id)stringWithContentsOfFile:(NSString \*)path usedEncoding:(NSStringEncoding \*)enc error:(NSError \*\*)error |
| To | + (instancetype)stringWithContentsOfFile:(NSString \*)path usedEncoding:(NSStringEncoding \*)enc error:(NSError \*\*)error |

Modified [+[NSString stringWithContentsOfURL:encoding:error:]](https://developer.apple.com/documentation/foundation/nsstring/1497360-stringwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | + (id)stringWithContentsOfURL:(NSURL \*)url encoding:(NSStringEncoding)enc error:(NSError \*\*)error |
| To | + (instancetype)stringWithContentsOfURL:(NSURL \*)url encoding:(NSStringEncoding)enc error:(NSError \*\*)error |

Modified [+[NSString stringWithContentsOfURL:usedEncoding:error:]](https://developer.apple.com/documentation/foundation/nsstring/1497408-stringwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | + (id)stringWithContentsOfURL:(NSURL \*)url usedEncoding:(NSStringEncoding \*)enc error:(NSError \*\*)error |
| To | + (instancetype)stringWithContentsOfURL:(NSURL \*)url usedEncoding:(NSStringEncoding \*)enc error:(NSError \*\*)error |

Modified [+[NSString stringWithFormat:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/clm/NSString/stringWithFormat:)

|  | Declaration |
| --- | --- |
| From | + (id)stringWithFormat:(NSString \*)format, ... |
| To | + (instancetype)stringWithFormat:(NSString \*)format, ... |

Modified [+[NSString stringWithString:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/clm/NSString/stringWithString:)

|  | Declaration |
| --- | --- |
| From | + (id)stringWithString:(NSString \*)string |
| To | + (instancetype)stringWithString:(NSString \*)string |

Modified [+[NSString stringWithUTF8String:]](https://developer.apple.com/documentation/foundation/nsstring/1497379-stringwithutf8string)

|  | Declaration |
| --- | --- |
| From | + (id)stringWithUTF8String:(const char \*)nullTerminatedCString |
| To | + (instancetype)stringWithUTF8String:(const char \*)nullTerminatedCString |

NSTextCheckingResult.hAdded [NSTextCheckingResult.alternativeStrings](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1415454-alternativestrings)Added [+[NSTextCheckingResult correctionCheckingResultWithRange:replacementString:alternativeStrings:]](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1416640-correctioncheckingresult)NSTimer.hAdded [-[NSTimer setTolerance:]](https://developer.apple.com/documentation/foundation/nstimer/1415085-tolerance)Added [-[NSTimer tolerance]](https://developer.apple.com/documentation/foundation/nstimer/1415085-tolerance)NSURL.hAdded [+[NSCharacterSet URLFragmentAllowedCharacterSet]](https://developer.apple.com/documentation/foundation/nscharacterset/1412537-urlfragmentallowed)Added [+[NSCharacterSet URLHostAllowedCharacterSet]](https://developer.apple.com/documentation/foundation/nscharacterset/1416426-urlhostallowedcharacterset)Added [+[NSCharacterSet URLPasswordAllowedCharacterSet]](https://developer.apple.com/documentation/foundation/nscharacterset/1417313-urlpasswordallowed)Added [+[NSCharacterSet URLPathAllowedCharacterSet]](https://developer.apple.com/documentation/foundation/nscharacterset/1416804-urlpathallowed)Added [+[NSCharacterSet URLQueryAllowedCharacterSet]](https://developer.apple.com/documentation/foundation/nscharacterset/1416698-urlqueryallowed)Added [+[NSCharacterSet URLUserAllowedCharacterSet]](https://developer.apple.com/documentation/foundation/nscharacterset/1411851-urluserallowedcharacterset)Added [-[NSString stringByAddingPercentEncodingWithAllowedCharacters:]](https://developer.apple.com/documentation/foundation/nsstring/1411946-stringbyaddingpercentencodingwit)Added [-[NSString stringByRemovingPercentEncoding]](https://developer.apple.com/documentation/foundation/nsstring/1409569-removingpercentencoding)Added [-[NSURL fileSystemRepresentation]](https://developer.apple.com/documentation/foundation/nsurl/1412925-filesystemrepresentation)Added [+[NSURL fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:]](https://developer.apple.com/documentation/foundation/nsurl/1411492-fileurlwithfilesystemrepresentat)Added [-[NSURL getFileSystemRepresentation:maxLength:]](https://developer.apple.com/documentation/foundation/nsurl/1415117-getfilesystemrepresentation)Added [-[NSURL initFileURLWithFileSystemRepresentation:isDirectory:relativeToURL:]](https://developer.apple.com/documentation/foundation/nsurl/1411210-init)Added [-[NSURL removeAllCachedResourceValues]](https://developer.apple.com/documentation/foundation/nsurl/1417078-removeallcachedresourcevalues)Added [-[NSURL removeCachedResourceValueForKey:]](https://developer.apple.com/documentation/foundation/nsurl/1410758-removecachedresourcevalue)Added [-[NSURL setTemporaryResourceValue:forKey:]](https://developer.apple.com/documentation/foundation/nsurl/1411094-settemporaryresourcevalue)Added [NSURLComponents](https://developer.apple.com/documentation/foundation/nsurlcomponents)Added [-[NSURLComponents URL]](https://developer.apple.com/documentation/foundation/nsurlcomponents/1413469-url)Added [-[NSURLComponents URLRelativeToURL:]](https://developer.apple.com/documentation/foundation/nsurlcomponents/1408378-url)Added [+[NSURLComponents componentsWithString:]](https://developer.apple.com/documentation/foundation/nsurlcomponents/1572054-componentswithstring)Added [+[NSURLComponents componentsWithURL:resolvingAgainstBaseURL:]](https://developer.apple.com/documentation/foundation/nsurlcomponents/1572050-componentswithurl)Added [NSURLComponents.fragment](https://developer.apple.com/documentation/foundation/nsurlcomponents/1417638-fragment)Added [NSURLComponents.host](https://developer.apple.com/documentation/foundation/nsurlcomponents/1411178-host)Added [-[NSURLComponents init]](https://developer.apple.com/documentation/foundation/nsurlcomponents/1414141-init)Added [-[NSURLComponents initWithString:]](https://developer.apple.com/documentation/foundation/nsurlcomponents/1410784-initwithstring)Added [-[NSURLComponents initWithURL:resolvingAgainstBaseURL:]](https://developer.apple.com/documentation/foundation/nsurlcomponents/1416476-init)Added [NSURLComponents.password](https://developer.apple.com/documentation/foundation/nsurlcomponents/1415604-password)Added [NSURLComponents.path](https://developer.apple.com/documentation/foundation/nsurlcomponents/1409650-path)Added [NSURLComponents.percentEncodedFragment](https://developer.apple.com/documentation/foundation/nsurlcomponents/1418392-percentencodedfragment)Added [NSURLComponents.percentEncodedHost](https://developer.apple.com/documentation/foundation/nsurlcomponents/1418231-percentencodedhost)Added [NSURLComponents.percentEncodedPassword](https://developer.apple.com/documentation/foundation/nsurlcomponents/1410319-percentencodedpassword)Added [NSURLComponents.percentEncodedPath](https://developer.apple.com/documentation/foundation/nsurlcomponents/1408161-percentencodedpath)Added [NSURLComponents.percentEncodedQuery](https://developer.apple.com/documentation/foundation/nsurlcomponents/1410395-percentencodedquery)Added [NSURLComponents.percentEncodedUser](https://developer.apple.com/documentation/foundation/nsurlcomponents/1417767-percentencodeduser)Added [NSURLComponents.port](https://developer.apple.com/documentation/foundation/nsurlcomponents/1413451-port)Added [NSURLComponents.query](https://developer.apple.com/documentation/foundation/nsurlcomponents/1415452-query)Added [NSURLComponents.scheme](https://developer.apple.com/documentation/foundation/nsurlcomponents/1407517-scheme)Added [NSURLComponents.user](https://developer.apple.com/documentation/foundation/nsurlcomponents/1415026-user)Added NSCharacterSet(NSURLUtilities)Added [NSURLUbiquitousItemDownloadingErrorKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1415978-ubiquitousitemdownloadingerrorke)Added [NSURLUbiquitousItemDownloadingStatusCurrent](https://developer.apple.com/documentation/foundation/urlubiquitousitemdownloadingstatus/1412385-current)Added [NSURLUbiquitousItemDownloadingStatusDownloaded](https://developer.apple.com/documentation/foundation/nsurlubiquitousitemdownloadingstatusdownloaded)Added [NSURLUbiquitousItemDownloadingStatusKey](https://developer.apple.com/documentation/foundation/nsurlubiquitousitemdownloadingstatuskey)Added [NSURLUbiquitousItemDownloadingStatusNotDownloaded](https://developer.apple.com/documentation/foundation/urlubiquitousitemdownloadingstatus/1416947-notdownloaded)Added [NSURLUbiquitousItemUploadingErrorKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1417266-ubiquitousitemuploadingerrorkey)Modified [NSURLBookmarkCreationPreferFileIDResolution](https://developer.apple.com/documentation/foundation/nsurlbookmarkcreationoptions/nsurlbookmarkcreationpreferfileidresolution)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [NSURLUbiquitousItemIsDownloadedKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1572053-ubiquitousitemisdownloadedkey)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

NSURLAuthenticationChallenge.hModified [NSURLAuthenticationChallenge](https://developer.apple.com/documentation/foundation/nsurlauthenticationchallenge)

|  | Protocols |
| --- | --- |
| From | NSCoding |
| To | NSSecureCoding |

NSURLConnection.hModified [+[NSURLConnection sendAsynchronousRequest:queue:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlconnection/1418125-sendasynchronousrequest)

|  | Declaration |
| --- | --- |
| From | + (void)sendAsynchronousRequest:(NSURLRequest \*)request queue:(NSOperationQueue \*)queue completionHandler:(void (^)(NSURLResponse \*, NSData \*, NSError \*))handler |
| To | + (void)sendAsynchronousRequest:(NSURLRequest \*)request queue:(NSOperationQueue \*)queue completionHandler:(void (^)(NSURLResponse \*response, NSData \*data, NSError \*connectionError))handler |

NSURLCredential.hAdded [NSURLCredentialPersistenceSynchronizable](https://developer.apple.com/documentation/foundation/urlcredential/persistence/synchronizable)Modified [NSURLCredential](https://developer.apple.com/documentation/foundation/urlcredential)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSURLCredentialStorage.hAdded [-[NSURLCredentialStorage removeCredential:forProtectionSpace:options:]](https://developer.apple.com/documentation/foundation/urlcredentialstorage/1407695-remove)Added [NSURLCredentialStorageRemoveSynchronizableCredentials](https://developer.apple.com/documentation/foundation/nsurlcredentialstorageremovesynchronizablecredentials)NSURLError.hAdded [NSURLErrorBackgroundTaskCancelledReasonKey](https://developer.apple.com/documentation/foundation/nsurlerrorbackgroundtaskcancelledreasonkey)Added [NSURLErrorCancelledReasonBackgroundUpdatesDisabled](https://developer.apple.com/documentation/foundation/nsurlerrorcancelledreasonbackgroundupdatesdisabled)Added [NSURLErrorCancelledReasonUserForceQuitApplication](https://developer.apple.com/documentation/foundation/nsurlerrorcancelledreasonuserforcequitapplication)NSURLProtectionSpace.hModified [NSURLProtectionSpace](https://developer.apple.com/documentation/foundation/nsurlprotectionspace)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSURLRequest.hAdded [+[NSURLRequest supportsSecureCoding]](https://developer.apple.com/documentation/foundation/nsurlrequest/1416510-supportssecurecoding)Modified [NSURLRequest](https://developer.apple.com/documentation/foundation/nsurlrequest)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSMutableCopying |
| To | NSCopying, NSMutableCopying, NSSecureCoding |

NSURLResponse.hModified [NSURLResponse](https://developer.apple.com/documentation/foundation/nsurlresponse)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSURLSession.hAdded [NSURLSession](https://developer.apple.com/documentation/foundation/urlsession)Added [NSURLSession.configuration](https://developer.apple.com/documentation/foundation/nsurlsession/1411477-configuration)Added -[NSURLSession dataTaskWithHTTPGetRequest:]Added -[NSURLSession dataTaskWithHTTPGetRequest:completionHandler:]Added [-[NSURLSession dataTaskWithRequest:]](https://developer.apple.com/documentation/foundation/nsurlsession/1410592-datataskwithrequest)Added [-[NSURLSession dataTaskWithRequest:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsession/1407613-datataskwithrequest)Added [-[NSURLSession dataTaskWithURL:]](https://developer.apple.com/documentation/foundation/urlsession/1411554-datatask)Added [-[NSURLSession dataTaskWithURL:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsession/1410330-datataskwithurl)Added [NSURLSession.delegate](https://developer.apple.com/documentation/foundation/nsurlsession/1411530-delegate)Added [NSURLSession.delegateQueue](https://developer.apple.com/documentation/foundation/nsurlsession/1411571-delegatequeue)Added [-[NSURLSession downloadTaskWithRequest:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411481-downloadtaskwithrequest)Added [-[NSURLSession downloadTaskWithRequest:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411511-downloadtaskwithrequest)Added [-[NSURLSession downloadTaskWithResumeData:]](https://developer.apple.com/documentation/foundation/urlsession/1409226-downloadtask)Added [-[NSURLSession downloadTaskWithResumeData:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411598-downloadtaskwithresumedata)Added [-[NSURLSession downloadTaskWithURL:]](https://developer.apple.com/documentation/foundation/urlsession/1411482-downloadtask)Added [-[NSURLSession downloadTaskWithURL:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411608-downloadtaskwithurl)Added [-[NSURLSession finishTasksAndInvalidate]](https://developer.apple.com/documentation/foundation/urlsession/1407428-finishtasksandinvalidate)Added [-[NSURLSession flushWithCompletionHandler:]](https://developer.apple.com/documentation/foundation/urlsession/1411622-flush)Added [-[NSURLSession getTasksWithCompletionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411578-gettaskswithcompletionhandler)Added [-[NSURLSession invalidateAndCancel]](https://developer.apple.com/documentation/foundation/urlsession/1411538-invalidateandcancel)Added [-[NSURLSession resetWithCompletionHandler:]](https://developer.apple.com/documentation/foundation/urlsession/1411479-reset)Added [NSURLSession.sessionDescription](https://developer.apple.com/documentation/foundation/urlsession/1408277-sessiondescription)Added [+[NSURLSession sessionWithConfiguration:]](https://developer.apple.com/documentation/foundation/urlsession/1411474-init)Added [+[NSURLSession sessionWithConfiguration:delegate:delegateQueue:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411597-sessionwithconfiguration)Added [+[NSURLSession sharedSession]](https://developer.apple.com/documentation/foundation/urlsession/1409000-shared)Added [-[NSURLSession uploadTaskWithRequest:fromData:]](https://developer.apple.com/documentation/foundation/nsurlsession/1409763-uploadtaskwithrequest)Added [-[NSURLSession uploadTaskWithRequest:fromData:completionHandler:]](https://developer.apple.com/documentation/foundation/urlsession/1411518-uploadtask)Added [-[NSURLSession uploadTaskWithRequest:fromFile:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411550-uploadtaskwithrequest)Added [-[NSURLSession uploadTaskWithRequest:fromFile:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411638-uploadtaskwithrequest)Added [-[NSURLSession uploadTaskWithStreamedRequest:]](https://developer.apple.com/documentation/foundation/nsurlsession/1410934-uploadtaskwithstreamedrequest)Added [NSURLSessionConfiguration](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration)Added [NSURLSessionConfiguration.HTTPAdditionalHeaders](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1411532-httpadditionalheaders)Added [NSURLSessionConfiguration.HTTPCookieAcceptPolicy](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1408933-httpcookieacceptpolicy)Added [NSURLSessionConfiguration.HTTPCookieStorage](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1411599-httpcookiestorage)Added [NSURLSessionConfiguration.HTTPMaximumConnectionsPerHost](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1407597-httpmaximumconnectionsperhost)Added [NSURLSessionConfiguration.HTTPShouldSetCookies](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1411589-httpshouldsetcookies)Added [NSURLSessionConfiguration.HTTPShouldUsePipelining](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1411657-httpshouldusepipelining)Added [NSURLSessionConfiguration.TLSMaximumSupportedProtocol](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1409076-tlsmaximumsupportedprotocol)Added [NSURLSessionConfiguration.TLSMinimumSupportedProtocol](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1411526-tlsminimumsupportedprotocol)Added [NSURLSessionConfiguration.URLCache](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1410148-urlcache)Added [NSURLSessionConfiguration.URLCredentialStorage](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1410947-urlcredentialstorage)Added [NSURLSessionConfiguration.allowsCellularAccess](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1409406-allowscellularaccess)Added [+[NSURLSessionConfiguration backgroundSessionConfiguration:]](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1411521-backgroundsessionconfiguration)Added [NSURLSessionConfiguration.connectionProxyDictionary](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1411499-connectionproxydictionary)Added [+[NSURLSessionConfiguration defaultSessionConfiguration]](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1411560-defaultsessionconfiguration)Added [NSURLSessionConfiguration.discretionary](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1411552-isdiscretionary)Added [+[NSURLSessionConfiguration ephemeralSessionConfiguration]](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1410529-ephemeral)Added [NSURLSessionConfiguration.identifier](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1408987-identifier)Added [NSURLSessionConfiguration.networkServiceType](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1411606-networkservicetype)Added [NSURLSessionConfiguration.protocolClasses](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1411050-protocolclasses)Added [NSURLSessionConfiguration.requestCachePolicy](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1411655-requestcachepolicy)Added [NSURLSessionConfiguration.sessionSendsLaunchEvents](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1617174-sessionsendslaunchevents)Added [NSURLSessionConfiguration.timeoutIntervalForRequest](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1408259-timeoutintervalforrequest)Added [NSURLSessionConfiguration.timeoutIntervalForResource](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1408153-timeoutintervalforresource)Added [NSURLSessionDataDelegate](https://developer.apple.com/documentation/foundation/urlsessiondatadelegate)Added [-[NSURLSessionDataDelegate URLSession:dataTask:didBecomeDownloadTask:]](https://developer.apple.com/documentation/foundation/nsurlsessiondatadelegate/1409936-urlsession)Added [-[NSURLSessionDataDelegate URLSession:dataTask:didReceiveData:]](https://developer.apple.com/documentation/foundation/urlsessiondatadelegate/1411528-urlsession)Added [-[NSURLSessionDataDelegate URLSession:dataTask:didReceiveResponse:completionHandler:]](https://developer.apple.com/documentation/foundation/urlsessiondatadelegate/1410027-urlsession)Added [-[NSURLSessionDataDelegate URLSession:dataTask:willCacheResponse:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsessiondatadelegate/1411612-urlsession)Added [NSURLSessionDataTask](https://developer.apple.com/documentation/foundation/urlsessiondatatask)Added [NSURLSessionDelegate](https://developer.apple.com/documentation/foundation/nsurlsessiondelegate)Added [-[NSURLSessionDelegate URLSession:didBecomeInvalidWithError:]](https://developer.apple.com/documentation/foundation/nsurlsessiondelegate/1407776-urlsession)Added [-[NSURLSessionDelegate URLSession:didReceiveChallenge:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsessiondelegate/1409308-urlsession)Added [-[NSURLSessionDelegate URLSessionDidFinishEventsForBackgroundURLSession:]](https://developer.apple.com/documentation/foundation/nsurlsessiondelegate/1617185-urlsessiondidfinisheventsforback)Added [NSURLSessionDownloadDelegate](https://developer.apple.com/documentation/foundation/nsurlsessiondownloaddelegate)Added [-[NSURLSessionDownloadDelegate URLSession:downloadTask:didFinishDownloadingToURL:]](https://developer.apple.com/documentation/foundation/urlsessiondownloaddelegate/1411575-urlsession)Added [-[NSURLSessionDownloadDelegate URLSession:downloadTask:didResumeAtOffset:expectedTotalBytes:]](https://developer.apple.com/documentation/foundation/urlsessiondownloaddelegate/1408142-urlsession)Added [-[NSURLSessionDownloadDelegate URLSession:downloadTask:didWriteData:totalBytesWritten:totalBytesExpectedToWrite:]](https://developer.apple.com/documentation/foundation/nsurlsessiondownloaddelegate/1409408-urlsession)Added [NSURLSessionDownloadTask](https://developer.apple.com/documentation/foundation/nsurlsessiondownloadtask)Added [-[NSURLSessionDownloadTask cancelByProducingResumeData:]](https://developer.apple.com/documentation/foundation/nsurlsessiondownloadtask/1411634-cancelbyproducingresumedata)Added [NSURLSessionTask](https://developer.apple.com/documentation/foundation/nsurlsessiontask)Added [-[NSURLSessionTask cancel]](https://developer.apple.com/documentation/foundation/urlsessiontask/1411591-cancel)Added [NSURLSessionTask.countOfBytesExpectedToReceive](https://developer.apple.com/documentation/foundation/urlsessiontask/1410663-countofbytesexpectedtoreceive)Added [NSURLSessionTask.countOfBytesExpectedToSend](https://developer.apple.com/documentation/foundation/urlsessiontask/1411534-countofbytesexpectedtosend)Added [NSURLSessionTask.countOfBytesReceived](https://developer.apple.com/documentation/foundation/urlsessiontask/1411581-countofbytesreceived)Added [NSURLSessionTask.countOfBytesSent](https://developer.apple.com/documentation/foundation/nsurlsessiontask/1410444-countofbytessent)Added [NSURLSessionTask.currentRequest](https://developer.apple.com/documentation/foundation/nsurlsessiontask/1411649-currentrequest)Added [NSURLSessionTask.error](https://developer.apple.com/documentation/foundation/urlsessiontask/1408145-error)Added [NSURLSessionTask.originalRequest](https://developer.apple.com/documentation/foundation/urlsessiontask/1411572-originalrequest)Added [NSURLSessionTask.response](https://developer.apple.com/documentation/foundation/urlsessiontask/1410586-response)Added [-[NSURLSessionTask resume]](https://developer.apple.com/documentation/foundation/urlsessiontask/1411121-resume)Added [NSURLSessionTask.state](https://developer.apple.com/documentation/foundation/nsurlsessiontask/1409888-state)Added [-[NSURLSessionTask suspend]](https://developer.apple.com/documentation/foundation/nsurlsessiontask/1411565-suspend)Added [NSURLSessionTask.taskDescription](https://developer.apple.com/documentation/foundation/urlsessiontask/1409798-taskdescription)Added [NSURLSessionTask.taskIdentifier](https://developer.apple.com/documentation/foundation/urlsessiontask/1411231-taskidentifier)Added [NSURLSessionTaskDelegate](https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate)Added [-[NSURLSessionTaskDelegate URLSession:task:didCompleteWithError:]](https://developer.apple.com/documentation/foundation/nsurlsessiontaskdelegate/1411610-urlsession)Added [-[NSURLSessionTaskDelegate URLSession:task:didReceiveChallenge:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsessiontaskdelegate/1411595-urlsession)Added [-[NSURLSessionTaskDelegate URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:]](https://developer.apple.com/documentation/foundation/nsurlsessiontaskdelegate/1408299-urlsession)Added [-[NSURLSessionTaskDelegate URLSession:task:needNewBodyStream:]](https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/1410001-urlsession)Added [-[NSURLSessionTaskDelegate URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:]](https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/1411626-urlsession)Added [NSURLSessionUploadTask](https://developer.apple.com/documentation/foundation/nsurlsessionuploadtask)Added NSURLSession(NSURLSessionAsynchronousConvenience)Added NSURLSession(NSURLSessionDeprecated)Added [NSURLSessionAuthChallengeCancelAuthenticationChallenge](https://developer.apple.com/documentation/foundation/nsurlsessionauthchallengedisposition/nsurlsessionauthchallengecancelauthenticationchallenge)Added [NSURLSessionAuthChallengeDisposition](https://developer.apple.com/documentation/foundation/nsurlsessionauthchallengedisposition)Added [NSURLSessionAuthChallengePerformDefaultHandling](https://developer.apple.com/documentation/foundation/urlsession/authchallengedisposition/performdefaulthandling)Added [NSURLSessionAuthChallengeRejectProtectionSpace](https://developer.apple.com/documentation/foundation/nsurlsessionauthchallengedisposition/nsurlsessionauthchallengerejectprotectionspace)Added [NSURLSessionAuthChallengeUseCredential](https://developer.apple.com/documentation/foundation/urlsession/authchallengedisposition/usecredential)Added [NSURLSessionDownloadTaskResumeData](https://developer.apple.com/documentation/foundation/nsurlsessiondownloadtaskresumedata)Added [NSURLSessionResponseAllow](https://developer.apple.com/documentation/foundation/nsurlsessionresponsedisposition/nsurlsessionresponseallow)Added [NSURLSessionResponseBecomeDownload](https://developer.apple.com/documentation/foundation/nsurlsessionresponsedisposition/nsurlsessionresponsebecomedownload)Added [NSURLSessionResponseCancel](https://developer.apple.com/documentation/foundation/nsurlsessionresponsedisposition/nsurlsessionresponsecancel)Added [NSURLSessionResponseDisposition](https://developer.apple.com/documentation/foundation/urlsession/responsedisposition)Added [NSURLSessionTaskState](https://developer.apple.com/documentation/foundation/nsurlsessiontaskstate)Added [NSURLSessionTaskStateCanceling](https://developer.apple.com/documentation/foundation/nsurlsessiontaskstate/nsurlsessiontaskstatecanceling)Added [NSURLSessionTaskStateCompleted](https://developer.apple.com/documentation/foundation/urlsessiontask/state/completed)Added [NSURLSessionTaskStateRunning](https://developer.apple.com/documentation/foundation/urlsessiontask/state/running)Added [NSURLSessionTaskStateSuspended](https://developer.apple.com/documentation/foundation/nsurlsessiontaskstate/nsurlsessiontaskstatesuspended)Added [NSURLSessionTransferSizeUnknown](https://developer.apple.com/documentation/foundation/nsurlsessiontransfersizeunknown)NSUserDefaults.hAdded [-[NSUserDefaults initWithSuiteName:]](https://developer.apple.com/documentation/foundation/userdefaults/1409957-init)Modified [-[NSUserDefaults initWithUser:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/instm/NSUserDefaults/initWithUser:)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[NSUserDefaults persistentDomainNames]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/instm/NSUserDefaults/persistentDomainNames)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

## GameController

GCController.hAdded [GCController](https://developer.apple.com/documentation/gamecontroller/gccontroller)Added [GCController.attachedToDevice](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458868-attachedtodevice)Added [GCController.controllerPausedHandler](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458852-controllerpausedhandler)Added [+[GCController controllers]](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458871-controllers)Added [GCController.extendedGamepad](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458883-extendedgamepad)Added [GCController.gamepad](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458860-gamepad)Added [GCController.playerIndex](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458885-playerindex)Added [+[GCController startWirelessControllerDiscoveryWithCompletionHandler:]](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458879-startwirelesscontrollerdiscovery)Added [+[GCController stopWirelessControllerDiscovery]](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458854-stopwirelesscontrollerdiscovery)Added [GCController.vendorName](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458877-vendorname)Added [GCControllerDidConnectNotification](https://developer.apple.com/documentation/gamecontroller/gccontrollerdidconnectnotification)Added [GCControllerDidDisconnectNotification](https://developer.apple.com/documentation/gamecontroller/gccontrollerdiddisconnectnotification)Added [GCControllerPlayerIndexUnset](https://developer.apple.com/documentation/gamecontroller/gccontrollerplayerindex/indexunset)GCControllerAxisInput.hAdded [GCControllerAxisInput](https://developer.apple.com/documentation/gamecontroller/gccontrolleraxisinput)Added [GCControllerAxisInput.value](https://developer.apple.com/documentation/gamecontroller/gccontrolleraxisinput/1500224-value)Added [GCControllerAxisInput.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrolleraxisinput/1500221-valuechangedhandler)Added [GCControllerAxisValueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrolleraxisvaluechangedhandler)GCControllerButtonInput.hAdded [GCControllerButtonInput](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput)Added [GCControllerButtonInput.pressed](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/1522539-ispressed)Added [GCControllerButtonInput.value](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/1522580-value)Added [GCControllerButtonInput.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/1522491-valuechangedhandler)Added [GCControllerButtonValueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttonvaluechangedhandler)GCControllerDirectionPad.hAdded [GCControllerDirectionPad](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad)Added [GCControllerDirectionPad.down](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462920-down)Added [GCControllerDirectionPad.left](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462924-left)Added [GCControllerDirectionPad.right](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462922-right)Added [GCControllerDirectionPad.up](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462918-up)Added [GCControllerDirectionPad.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462914-valuechangedhandler)Added [GCControllerDirectionPad.xAxis](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462930-xaxis)Added [GCControllerDirectionPad.yAxis](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462926-yaxis)Added [GCControllerDirectionPadValueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpadvaluechangedhandler)GCControllerElement.hAdded [GCControllerElement](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement)Added [GCControllerElement.analog](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement/1522581-analog)Added [GCControllerElement.collection](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement/1522575-collection)GCExtendedGamepad.hAdded [GCExtendedGamepad](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad)Added [GCExtendedGamepad.buttonA](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522558-buttona)Added [GCExtendedGamepad.buttonB](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522396-buttonb)Added [GCExtendedGamepad.buttonX](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522567-buttonx)Added [GCExtendedGamepad.buttonY](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522473-buttony)Added [GCExtendedGamepad.controller](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522427-controller)Added [GCExtendedGamepad.dpad](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522422-dpad)Added [GCExtendedGamepad.leftShoulder](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522418-leftshoulder)Added [GCExtendedGamepad.leftThumbstick](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522564-leftthumbstick)Added [GCExtendedGamepad.leftTrigger](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522569-lefttrigger)Added [GCExtendedGamepad.rightShoulder](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522484-rightshoulder)Added [GCExtendedGamepad.rightThumbstick](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522437-rightthumbstick)Added [GCExtendedGamepad.rightTrigger](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522563-righttrigger)Added [-[GCExtendedGamepad saveSnapshot]](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522447-savesnapshot)Added [GCExtendedGamepad.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522464-valuechangedhandler)Added [GCExtendedGamepadValueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadvaluechangedhandler)GCExtendedGamepadSnapshot.hAdded [GCExtendedGamepadSnapshot](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshot)Added [-[GCExtendedGamepadSnapshot initWithController:snapshotData:]](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshot/1522527-init)Added [-[GCExtendedGamepadSnapshot initWithSnapshotData:]](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshot/1522554-initwithsnapshotdata)Added [GCExtendedGamepadSnapshot.snapshotData](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshot/1522478-snapshotdata)Added [GCExtendedGamepadSnapShotDataV100](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshotdatav100)Added [GCExtendedGamepadSnapShotDataV100FromNSData()](https://developer.apple.com/documentation/gamecontroller/1522439-gcextendedgamepadsnapshotdatav10)Added [NSDataFromGCExtendedGamepadSnapShotDataV100()](https://developer.apple.com/documentation/gamecontroller/1522471-nsdatafromgcextendedgamepadsnaps)GCGamepad.hAdded [GCGamepad](https://developer.apple.com/documentation/gamecontroller/gcgamepad)Added [GCGamepad.buttonA](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497427-buttona)Added [GCGamepad.buttonB](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497418-buttonb)Added [GCGamepad.buttonX](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497417-buttonx)Added [GCGamepad.buttonY](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497431-buttony)Added [GCGamepad.controller](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497428-controller)Added [GCGamepad.dpad](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497425-dpad)Added [GCGamepad.leftShoulder](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497423-leftshoulder)Added [GCGamepad.rightShoulder](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497429-rightshoulder)Added [-[GCGamepad saveSnapshot]](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497415-savesnapshot)Added [GCGamepad.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497421-valuechangedhandler)Added [GCGamepadValueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcgamepadvaluechangedhandler)GCGamepadSnapshot.hAdded [GCGamepadSnapshot](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshot)Added [-[GCGamepadSnapshot initWithController:snapshotData:]](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshot/1493915-init)Added [-[GCGamepadSnapshot initWithSnapshotData:]](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshot/1493933-init)Added [GCGamepadSnapshot.snapshotData](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshot/1493928-snapshotdata)Added [GCGamepadSnapShotDataV100](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshotdatav100)Added [GCGamepadSnapShotDataV100FromNSData()](https://developer.apple.com/documentation/gamecontroller/1493934-gcgamepadsnapshotdatav100fromnsd)Added [NSDataFromGCGamepadSnapShotDataV100()](https://developer.apple.com/documentation/gamecontroller/1493914-nsdatafromgcgamepadsnapshotdatav)GameController.h

## GameKit

GKAchievement.hAdded [-[GKAchievement initWithIdentifier:forPlayer:]](https://developer.apple.com/documentation/gamekit/gkachievement/1625009-initwithidentifier)Added [GKAchievement.playerID](https://developer.apple.com/documentation/gamekit/gkachievement/1625010-playerid)Modified [GKAchievement](https://developer.apple.com/documentation/gamekit/gkachievement)

|  | Protocols |
| --- | --- |
| From | NSCoding |
| To | NSCoding, NSSecureCoding |

Modified [GKAchievement.completed](https://developer.apple.com/documentation/gamekit/gkachievement/1521050-completed)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly, getter=isCompleted) BOOL completed |
| To | @property(readonly, getter=isCompleted, nonatomic) BOOL completed |

Modified [GKAchievement.hidden](https://developer.apple.com/documentation/gamekit/gkachievement/1521136-ishidden)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, assign, getter=isHidden, readonly) BOOL hidden |
| To | @property(assign, getter=isHidden, readonly, nonatomic) BOOL hidden |

Modified [GKAchievement.identifier](https://developer.apple.com/documentation/gamekit/gkachievement/1520631-identifier)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, retain) NSString \*identifier |
| To | @property(copy, nonatomic) NSString \*identifier |

Modified [GKAchievement.lastReportedDate](https://developer.apple.com/documentation/gamekit/gkachievement/1520993-lastreporteddate)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, retain, readonly) NSDate \*lastReportedDate |
| To | @property(copy, readonly, nonatomic) NSDate \*lastReportedDate |

Modified [GKAchievement.percentComplete](https://developer.apple.com/documentation/gamekit/gkachievement/1520939-percentcomplete)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, assign) double percentComplete |
| To | @property(assign, nonatomic) double percentComplete |

Modified [-[GKAchievement reportAchievementWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1521108-reportachievementwithcompletionh)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [GKAchievement.showsCompletionBanner](https://developer.apple.com/documentation/gamekit/gkachievement/1521058-showscompletionbanner)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, assign) BOOL showsCompletionBanner |
| To | @property(assign, nonatomic) BOOL showsCompletionBanner |

GKAchievementDescription.hAdded GKAchievementDescription(UI)Modified [GKAchievementDescription](https://developer.apple.com/documentation/gamekit/gkachievementdescription)

|  | Protocols |
| --- | --- |
| From | NSCoding |
| To | NSCoding, NSSecureCoding |

Modified [GKAchievementDescription.achievedDescription](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416598-achieveddescription)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, retain, readonly) NSString \*achievedDescription |
| To | @property(copy, readonly, nonatomic) NSString \*achievedDescription |

Modified [GKAchievementDescription.hidden](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416582-hidden)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, getter=isHidden, assign, readonly) BOOL hidden |
| To | @property(getter=isHidden, assign, readonly, nonatomic) BOOL hidden |

Modified [GKAchievementDescription.identifier](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416586-identifier)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, retain, readonly) NSString \*identifier |
| To | @property(copy, readonly, nonatomic) NSString \*identifier |

Modified [GKAchievementDescription.image](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416591-image)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [GKAchievementDescription.maximumPoints](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416589-maximumpoints)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, assign, readonly) NSInteger maximumPoints |
| To | @property(assign, readonly, nonatomic) NSInteger maximumPoints |

Modified [GKAchievementDescription.title](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416602-title)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, retain, readonly) NSString \*title |
| To | @property(copy, readonly, nonatomic) NSString \*title |

Modified [GKAchievementDescription.unachievedDescription](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416584-unachieveddescription)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, retain, readonly) NSString \*unachievedDescription |
| To | @property(copy, readonly, nonatomic) NSString \*unachievedDescription |

GKAchievementViewController.hModified [GKAchievementViewController](https://developer.apple.com/documentation/gamekit/gkachievementviewcontroller)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [GKAchievementViewControllerDelegate](https://developer.apple.com/documentation/gamekit/gkachievementviewcontrollerdelegate)

|  | Deprecation | Protocols |
| --- | --- | --- |
| From | _none_ | _none_ |
| To | iOS 7.0 | NSObject |

GKChallenge.hAdded [-[GKAchievement challengeComposeControllerWithPlayers:message:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1623556-challengecomposecontrollerwithpl)Added [+[GKAchievement reportAchievements:withEligibleChallenges:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1520558-reportachievements)Added [-[GKScore challengeComposeControllerWithPlayers:message:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkscore/1623555-challengecomposecontrollerwithpl)Added [+[GKScore reportScores:withEligibleChallenges:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkscore/1520627-reportscores)Added [GKChallengeComposeCompletionBlock](https://developer.apple.com/documentation/gamekit/gkchallengecomposecompletionblock)Modified [-[GKAchievement issueChallengeToPlayers:message:]](https://developer.apple.com/documentation/gamekit/gkachievement/1520984-issuechallenge)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [GKChallenge](https://developer.apple.com/documentation/gamekit/gkchallenge)

|  | Protocols |
| --- | --- |
| From | NSCoding |
| To | NSCoding, NSSecureCoding |

Modified [-[GKScore issueChallengeToPlayers:message:]](https://developer.apple.com/documentation/gamekit/gkscore/1520610-issuechallengetoplayers)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

GKChallengeEventHandler.hModified [GKChallengeEventHandler](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandler)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [+[GKChallengeEventHandler challengeEventHandler]](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandler/1563241-challengeeventhandler)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [GKChallengeEventHandler.delegate](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandler/1520556-delegate)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [GKChallengeEventHandlerDelegate](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

GKError.hAdded [GKErrorInvitationsDisabled](https://developer.apple.com/documentation/gamekit/gkerrorcode/gkerrorinvitationsdisabled)GKEventListener.hAdded [GKChallengeListener](https://developer.apple.com/documentation/gamekit/gkchallengelistener)Added [-[GKChallengeListener player:didCompleteChallenge:issuedByFriend:]](https://developer.apple.com/documentation/gamekit/gkchallengelistener/1494688-player)Added [-[GKChallengeListener player:didReceiveChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengelistener/1494691-player)Added [-[GKChallengeListener player:issuedChallengeWasCompleted:byFriend:]](https://developer.apple.com/documentation/gamekit/gkchallengelistener/1494686-player)Added [-[GKChallengeListener player:wantsToPlayChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengelistener/1494684-player)GKGameCenterViewController.hAdded [GKGameCenterViewController.leaderboardIdentifier](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/1520540-leaderboardidentifier)Modified [GKGameCenterViewController.leaderboardCategory](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/1520837-leaderboardcategory)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [GKGameCenterViewController.leaderboardTimeScope](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/1520464-leaderboardtimescope)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

GKLeaderboard.hAdded [GKLeaderboard.identifier](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503141-identifier)Added [-[GKLeaderboard loadImageWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503161-loadimagewithcompletionhandler)Added GKLeaderboard(UI)Modified [GKLeaderboard.category](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503154-category)

|  | Deprecation | Declaration |
| --- | --- | --- |
| From | _none_ | @property(nonatomic, retain) NSString \*category |
| To | iOS 7.0 | @property(copy, nonatomic) NSString \*category |

Modified [GKLeaderboard.localPlayerScore](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503151-localplayerscore)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly, retain) GKScore \*localPlayerScore |
| To | @property(readonly, retain, nonatomic) GKScore \*localPlayerScore |

Modified [GKLeaderboard.maxRange](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503136-maxrange)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly, assign) NSUInteger maxRange |
| To | @property(readonly, assign, nonatomic) NSUInteger maxRange |

Modified [GKLeaderboard.playerScope](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503165-playerscope)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, assign) GKLeaderboardPlayerScope playerScope |
| To | @property(assign, nonatomic) GKLeaderboardPlayerScope playerScope |

Modified [GKLeaderboard.range](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503144-range)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, assign) NSRange range |
| To | @property(assign, nonatomic) NSRange range |

Modified [GKLeaderboard.scores](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503159-scores)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly, retain) NSArray \*scores |
| To | @property(readonly, retain, nonatomic) NSArray \*scores |

Modified [+[GKLeaderboard setDefaultLeaderboard:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503123-setdefaultleaderboard)

|  | Deprecation | Declaration |
| --- | --- | --- |
| From | _none_ | + (void)setDefaultLeaderboard:(NSString \*)categoryID withCompletionHandler:(void (^)(NSError \*error))completionHandler |
| To | iOS 7.0 | + (void)setDefaultLeaderboard:(NSString \*)leaderboardIdentifier withCompletionHandler:(void (^)(NSError \*error))completionHandler |

Modified [GKLeaderboard.timeScope](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503130-timescope)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, assign) GKLeaderboardTimeScope timeScope |
| To | @property(assign, nonatomic) GKLeaderboardTimeScope timeScope |

Modified [GKLeaderboard.title](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503139-title)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly, retain) NSString \*title |
| To | @property(readonly, copy, nonatomic) NSString \*title |

GKLeaderboardSet.hAdded [GKLeaderboardSet](https://developer.apple.com/documentation/gamekit/gkleaderboardset)Added [GKLeaderboardSet.groupIdentifier](https://developer.apple.com/documentation/gamekit/gkleaderboardset/1451800-groupidentifier)Added [GKLeaderboardSet.identifier](https://developer.apple.com/documentation/gamekit/gkleaderboardset/1451802-identifier)Added [-[GKLeaderboardSet loadImageWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkleaderboardset/1451812-loadimage)Added [+[GKLeaderboardSet loadLeaderboardSetsWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkleaderboardset/1451798-loadleaderboardsetswithcompletio)Added [-[GKLeaderboardSet loadLeaderboardsWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkleaderboardset/1451810-loadleaderboardswithcompletionha)Added [GKLeaderboardSet.title](https://developer.apple.com/documentation/gamekit/gkleaderboardset/1451804-title)Added GKLeaderboardSet(UI)GKLeaderboardViewController.hModified [GKLeaderboardViewController](https://developer.apple.com/documentation/gamekit/gkleaderboardviewcontroller)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [GKLeaderboardViewControllerDelegate](https://developer.apple.com/documentation/gamekit/gkleaderboardviewcontrollerdelegate)

|  | Deprecation | Protocols |
| --- | --- | --- |
| From | _none_ | _none_ |
| To | iOS 7.0 | NSObject |

GKLocalPlayer.hAdded [-[GKLocalPlayer generateIdentityVerificationSignatureWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515407-generateidentityverificationsign)Added [-[GKLocalPlayer loadDefaultLeaderboardIdentifierWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515404-loaddefaultleaderboardidentifier)Added [-[GKLocalPlayer registerListener:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515393-registerlistener)Added [-[GKLocalPlayer setDefaultLeaderboardIdentifier:completionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515408-setdefaultleaderboardidentifier)Added [-[GKLocalPlayer unregisterAllListeners]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515388-unregisteralllisteners)Added [-[GKLocalPlayer unregisterListener:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515389-unregisterlistener)Added [GKLocalPlayerListener](https://developer.apple.com/documentation/gamekit/gklocalplayerlistener)Added GKLocalPlayer(GKLocalPlayerEvents)Modified [GKLocalPlayer.authenticated](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515402-isauthenticated)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly, getter=isAuthenticated) BOOL authenticated |
| To | @property(readonly, getter=isAuthenticated, nonatomic) BOOL authenticated |

Modified [-[GKLocalPlayer loadDefaultLeaderboardCategoryIDWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515398-loaddefaultleaderboardcategoryid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[GKLocalPlayer loadFriendsWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515391-loadfriendswithcompletionhandler)

|  | Declaration |
| --- | --- |
| From | - (void)loadFriendsWithCompletionHandler:(void (^)(NSArray \*friends, NSError \*error))completionHandler |
| To | - (void)loadFriendsWithCompletionHandler:(void (^)(NSArray \*friendIDs, NSError \*error))completionHandler |

Modified [-[GKLocalPlayer setDefaultLeaderboardCategoryID:completionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515385-setdefaultleaderboardcategoryid)

|  | Deprecation | Declaration |
| --- | --- | --- |
| From | _none_ | - (void)setDefaultLeaderboardCategoryID:(NSString \*)categoryID completionHandler:(void (^)(NSError \*error))completionHandler |
| To | iOS 7.0 | - (void)setDefaultLeaderboardCategoryID:(NSString \*)catogoryID completionHandler:(void (^)(NSError \*error))completionHandler |

Modified [GKLocalPlayer.underage](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515394-underage)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly, getter=isUnderage) BOOL underage |
| To | @property(readonly, getter=isUnderage, nonatomic) BOOL underage |

GKMatchmaker.hAdded [GKInviteEventListener](https://developer.apple.com/documentation/gamekit/gkinviteeventlistener)Added [-[GKInviteEventListener player:didAcceptInvite:]](https://developer.apple.com/documentation/gamekit/gkinviteeventlistener/1520672-player)Added [-[GKInviteEventListener player:didRequestMatchWithPlayers:]](https://developer.apple.com/documentation/gamekit/gkinviteeventlistener/1623695-player)Modified [GKInvite.hosted](https://developer.apple.com/documentation/gamekit/gkinvite/1520458-hosted)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly, getter=isHosted) BOOL hosted |
| To | @property(readonly, getter=isHosted, nonatomic) BOOL hosted |

Modified [GKInvite.inviter](https://developer.apple.com/documentation/gamekit/gkinvite/1520959-inviter)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly, retain) NSString \*inviter |
| To | @property(readonly, retain, nonatomic) NSString \*inviter |

Modified [GKInvite.playerAttributes](https://developer.apple.com/documentation/gamekit/gkinvite/1520917-playerattributes)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly) uint32_t playerAttributes |
| To | @property(readonly, nonatomic) uint32_t playerAttributes |

Modified [GKInvite.playerGroup](https://developer.apple.com/documentation/gamekit/gkinvite/1520563-playergroup)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly) NSUInteger playerGroup |
| To | @property(readonly, nonatomic) NSUInteger playerGroup |

Modified [GKMatchmaker.inviteHandler](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1521060-invitehandler)

|  | Deprecation | Declaration |
| --- | --- | --- |
| From | _none_ | @property(nonatomic, copy) void (^inviteHandler)(GKInvite \*acceptedInvite, NSArray \*playersToInvite) |
| To | iOS 7.0 | @property(nonatomic, copy) void (^inviteHandler)(GKInvite \*acceptedInvite, NSArray \*playerIDsToInvite) |

GKMatchmakerViewController.hModified [GKMatchmakerViewController.defaultInvitationMessage](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492409-defaultinvitationmessage)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

GKPeerPickerController.hModified [GKPeerPickerController](https://developer.apple.com/documentation/gamekit/gkpeerpickercontroller)

|  | Deprecation | Introduction |
| --- | --- | --- |
| From | _none_ | iOS 4.1 |
| To | iOS 7.0 | iOS 3.0 |

GKPlayer.hAdded GKPlayer(UI)Modified [GKPlayer.alias](https://developer.apple.com/documentation/gamekit/gkplayer/1520970-alias)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly, copy) NSString \*alias |
| To | @property(readonly, copy, nonatomic) NSString \*alias |

Modified [GKPlayer.displayName](https://developer.apple.com/documentation/gamekit/gkplayer/1520695-displayname)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly) NSString \*displayName |
| To | @property(readonly, nonatomic) NSString \*displayName |

Modified [GKPlayer.isFriend](https://developer.apple.com/documentation/gamekit/gkplayer/1520467-isfriend)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly) BOOL isFriend |
| To | @property(readonly, nonatomic) BOOL isFriend |

Modified [GKPlayer.playerID](https://developer.apple.com/documentation/gamekit/gkplayer/1521127-playerid)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly, retain) NSString \*playerID |
| To | @property(readonly, retain, nonatomic) NSString \*playerID |

GKPublicConstants.hModified [GKPeerConnectionState](https://developer.apple.com/documentation/gamekit/gkpeerconnectionstate)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [GKSendDataMode](https://developer.apple.com/documentation/gamekit/gksenddatamode)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [GKSessionMode](https://developer.apple.com/documentation/gamekit/gksessionmode)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [GKVoiceChatServiceError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

GKScore.hAdded [-[GKScore initWithLeaderboardIdentifier:]](https://developer.apple.com/documentation/gamekit/gkscore/1399240-initwithleaderboardidentifier)Added [-[GKScore initWithLeaderboardIdentifier:forPlayer:]](https://developer.apple.com/documentation/gamekit/gkscore/1620733-initwithleaderboardidentifier)Added [GKScore.leaderboardIdentifier](https://developer.apple.com/documentation/gamekit/gkscore/1399248-leaderboardidentifier)Modified [GKScore](https://developer.apple.com/documentation/gamekit/gkscore)

|  | Protocols |
| --- | --- |
| From | NSCoding |
| To | NSCoding, NSSecureCoding |

Modified [GKScore.category](https://developer.apple.com/documentation/gamekit/gkscore/1399225-category)

|  | Deprecation | Declaration |
| --- | --- | --- |
| From | _none_ | @property(nonatomic, retain) NSString \*category |
| To | iOS 7.0 | @property(copy, nonatomic) NSString \*category |

Modified [GKScore.date](https://developer.apple.com/documentation/gamekit/gkscore/1399234-date)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly, retain) NSDate \*date |
| To | @property(readonly, retain, nonatomic) NSDate \*date |

Modified [GKScore.formattedValue](https://developer.apple.com/documentation/gamekit/gkscore/1399221-formattedvalue)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly, retain) NSString \*formattedValue |
| To | @property(readonly, copy, nonatomic) NSString \*formattedValue |

Modified [-[GKScore initWithCategory:]](https://developer.apple.com/documentation/gamekit/gkscore/1399242-init)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [GKScore.playerID](https://developer.apple.com/documentation/gamekit/gkscore/1399232-playerid)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly, retain) NSString \*playerID |
| To | @property(readonly, retain, nonatomic) NSString \*playerID |

Modified [GKScore.rank](https://developer.apple.com/documentation/gamekit/gkscore/1399244-rank)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly, assign) NSInteger rank |
| To | @property(readonly, assign, nonatomic) NSInteger rank |

Modified [-[GKScore reportScoreWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkscore/1399223-report)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [GKScore.value](https://developer.apple.com/documentation/gamekit/gkscore/1399236-value)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, assign) int64_t value |
| To | @property(assign, nonatomic) int64_t value |

GKSession.hModified [GKSession](https://developer.apple.com/documentation/gamekit/gksession)

|  | Deprecation | Introduction |
| --- | --- | --- |
| From | _none_ | iOS 4.1 |
| To | iOS 7.0 | iOS 3.0 |

GKSessionError.hModified [GKSessionError](https://developer.apple.com/documentation/gamekit/gksessionerror)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

GKTurnBasedMatch.hAdded [GKTurnBasedEventListener](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener)Added [-[GKTurnBasedEventListener player:didRequestMatchWithPlayers:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1624268-player)Added [-[GKTurnBasedEventListener player:matchEnded:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1520554-player)Added [-[GKTurnBasedEventListener player:receivedExchangeCancellation:forMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1520649-player)Added [-[GKTurnBasedEventListener player:receivedExchangeReplies:forCompletedExchange:forMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1520827-player)Added [-[GKTurnBasedEventListener player:receivedExchangeRequest:forMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1521209-player)Added [-[GKTurnBasedEventListener player:receivedTurnEventForMatch:didBecomeActive:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1521017-player)Added [GKTurnBasedExchange](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange)Added [-[GKTurnBasedExchange cancelWithLocalizableMessageKey:arguments:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520779-cancel)Added [GKTurnBasedExchange.completionDate](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520994-completiondate)Added [GKTurnBasedExchange.data](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1521121-data)Added [GKTurnBasedExchange.exchangeID](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520666-exchangeid)Added [GKTurnBasedExchange.message](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520633-message)Added [GKTurnBasedExchange.recipients](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520849-recipients)Added [GKTurnBasedExchange.replies](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520516-replies)Added [-[GKTurnBasedExchange replyWithLocalizableMessageKey:arguments:data:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520478-reply)Added [GKTurnBasedExchange.sendDate](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1521131-senddate)Added [GKTurnBasedExchange.sender](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520936-sender)Added [GKTurnBasedExchange.status](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1521166-status)Added [GKTurnBasedExchange.timeoutDate](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1521105-timeoutdate)Added [GKTurnBasedExchangeReply](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangereply)Added [GKTurnBasedExchangeReply.data](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangereply/1520729-data)Added [GKTurnBasedExchangeReply.message](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangereply/1520896-message)Added [GKTurnBasedExchangeReply.recipient](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangereply/1521025-recipient)Added [GKTurnBasedMatch.activeExchanges](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520977-activeexchanges)Added [GKTurnBasedMatch.completedExchanges](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520918-completedexchanges)Added [-[GKTurnBasedMatch endMatchInTurnWithMatchData:scores:achievements:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521006-endmatchinturn)Added [GKTurnBasedMatch.exchangeDataMaximumSize](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521002-exchangedatamaximumsize)Added [GKTurnBasedMatch.exchangeMaxInitiatedExchangesPerPlayer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520965-exchangemaxinitiatedexchangesper)Added [GKTurnBasedMatch.exchanges](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521224-exchanges)Added [-[GKTurnBasedMatch saveMergedMatchData:withResolvedExchanges:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521154-savemergedmatchdata)Added [-[GKTurnBasedMatch sendExchangeToParticipants:data:localizableMessageKey:arguments:timeout:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520451-sendexchangetoparticipants)Added [-[GKTurnBasedMatch sendReminderToParticipants:localizableMessageKey:arguments:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520947-sendremindertoparticipants)Added [-[GKTurnBasedMatch setLocalizableMessageWithKey:arguments:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520510-setlocalizablemessagewithkey)Added [GKExchangeTimeoutDefault](https://developer.apple.com/documentation/gamekit/gkexchangetimeoutdefault)Added [GKExchangeTimeoutNone](https://developer.apple.com/documentation/gamekit/gkexchangetimeoutnone)Added [GKTurnBasedExchangeStatus](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus)Added [GKTurnBasedExchangeStatusActive](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus/active)Added [GKTurnBasedExchangeStatusCanceled](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus/gkturnbasedexchangestatuscanceled)Added [GKTurnBasedExchangeStatusComplete](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus/gkturnbasedexchangestatuscomplete)Added [GKTurnBasedExchangeStatusResolved](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus/gkturnbasedexchangestatusresolved)Added [GKTurnBasedExchangeStatusUnknown](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus/unknown)Modified [GKTurnBasedEventHandler](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandler)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [GKTurnBasedEventHandler.delegate](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandler/1521013-delegate)

|  | Deprecation | Declaration |
| --- | --- | --- |
| From | _none_ | @property(nonatomic, assign) NSObject<GKTurnBasedEventHandlerDelegate> \*delegate |
| To | iOS 7.0 | @property(assign, nonatomic) NSObject<GKTurnBasedEventHandlerDelegate> \*delegate |

Modified [+[GKTurnBasedEventHandler sharedTurnBasedEventHandler]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandler/1521211-sharedturnbasedeventhandler)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[GKTurnBasedEventHandlerDelegate handleInviteFromGameCenter:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/1520926-handleinvite)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[GKTurnBasedEventHandlerDelegate handleMatchEnded:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/1521053-handlematchended)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [-[GKTurnBasedEventHandlerDelegate handleTurnEventForMatch:didBecomeActive:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/1521103-handleturnevent)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [GKTurnBasedMatch.creationDate](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521168-creationdate)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly, retain) NSDate \*creationDate |
| To | @property(readonly, retain, nonatomic) NSDate \*creationDate |

Modified [GKTurnBasedMatch.currentParticipant](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520643-currentparticipant)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly, retain) GKTurnBasedParticipant \*currentParticipant |
| To | @property(readonly, retain, nonatomic) GKTurnBasedParticipant \*currentParticipant |

Modified [GKTurnBasedMatch.matchData](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520991-matchdata)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly, retain) NSData \*matchData |
| To | @property(readonly, retain, nonatomic) NSData \*matchData |

Modified [GKTurnBasedMatch.matchDataMaximumSize](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520731-matchdatamaximumsize)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly) NSUInteger matchDataMaximumSize |
| To | @property(readonly, nonatomic) NSUInteger matchDataMaximumSize |

Modified [GKTurnBasedMatch.matchID](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520625-matchid)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly, retain) NSString \*matchID |
| To | @property(readonly, retain, nonatomic) NSString \*matchID |

Modified [GKTurnBasedMatch.message](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520721-message)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readwrite, copy) NSString \*message |
| To | @property(readwrite, copy, nonatomic) NSString \*message |

Modified [GKTurnBasedMatch.participants](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520875-participants)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly, retain) NSArray \*participants |
| To | @property(readonly, retain, nonatomic) NSArray \*participants |

Modified [GKTurnBasedMatch.status](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520548-status)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly) GKTurnBasedMatchStatus status |
| To | @property(readonly, nonatomic) GKTurnBasedMatchStatus status |

Modified [GKTurnBasedParticipant.lastTurnDate](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1520941-lastturndate)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly, retain) NSDate \*lastTurnDate |
| To | @property(readonly, copy, nonatomic) NSDate \*lastTurnDate |

Modified [GKTurnBasedParticipant.matchOutcome](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1521110-matchoutcome)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, assign) GKTurnBasedMatchOutcome matchOutcome |
| To | @property(assign, nonatomic) GKTurnBasedMatchOutcome matchOutcome |

Modified [GKTurnBasedParticipant.playerID](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1520474-playerid)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly, retain) NSString \*playerID |
| To | @property(readonly, copy, nonatomic) NSString \*playerID |

Modified [GKTurnBasedParticipant.status](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1520514-status)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly) GKTurnBasedParticipantStatus status |
| To | @property(readonly, nonatomic) GKTurnBasedParticipantStatus status |

Modified [GKTurnBasedParticipant.timeoutDate](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1521187-timeoutdate)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly, retain) NSDate \*timeoutDate |
| To | @property(readonly, copy, nonatomic) NSDate \*timeoutDate |

GKTurnBasedMatchmakerViewController.hModified [GKTurnBasedMatchmakerViewControllerDelegate](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontrollerdelegate)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSObject |

GKVoiceChat.hModified [GKVoiceChat.active](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385697-active)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, assign, getter=isActive) BOOL active |
| To | @property(assign, getter=isActive, nonatomic) BOOL active |

Modified [GKVoiceChat.name](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385707-name)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly) NSString \*name |
| To | @property(readonly, copy, nonatomic) NSString \*name |

Modified [GKVoiceChat.playerIDs](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385721-playerids)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly) NSArray \*playerIDs |
| To | @property(readonly, nonatomic) NSArray \*playerIDs |

Modified [GKVoiceChat.playerStateUpdateHandler](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385705-playerstateupdatehandler)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, copy) void (^playerStateUpdateHandler)(NSString \*playerID, GKVoiceChatPlayerState state) |
| To | @property(copy, nonatomic) void (^playerStateUpdateHandler)(NSString \*playerID, GKVoiceChatPlayerState state) |

Modified [GKVoiceChat.volume](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385691-volume)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, assign) float volume |
| To | @property(assign, nonatomic) float volume |

GKVoiceChatService.hModified [GKVoiceChatService](https://developer.apple.com/documentation/gamekit/gkvoicechatservice)

|  | Deprecation | Introduction |
| --- | --- | --- |
| From | _none_ | iOS 4.1 |
| To | iOS 7.0 | iOS 3.0 |

## GLKit

GLKBaseEffect.hModified [GLKBaseEffect.label](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488835-label)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, retain) NSString \*label |
| To | @property(nonatomic, copy) NSString \*label |

Modified [GLKBaseEffect.textureOrder](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488830-textureorder)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, retain) NSArray \*textureOrder |
| To | @property(nonatomic, copy) NSArray \*textureOrder |

GLKEffectPropertyFog.hAdded [GLKFogMode](https://developer.apple.com/documentation/glkit/glkfogmode)GLKEffectPropertyTexture.hModified [GLKEffectPropertyTexture.envMode](https://developer.apple.com/documentation/glkit/glkeffectpropertytexture/1488986-envmode)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, assign) GLint envMode |
| To | @property(nonatomic, assign) GLKTextureEnvMode envMode |

GLKSkyboxEffect.hModified [GLKSkyboxEffect.label](https://developer.apple.com/documentation/glkit/glkskyboxeffect/1489038-label)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, retain) NSString \*label |
| To | @property(nonatomic, copy) NSString \*label |

GLKTextureLoader.hAdded [GLKTextureLoaderErrorIncompatibleFormatSRGB](https://developer.apple.com/documentation/glkit/glktextureloadererror/glktextureloadererrorincompatibleformatsrgb)Added [GLKTextureLoaderSRGB](https://developer.apple.com/documentation/glkit/glktextureloadersrgb)GLKView.hAdded [GLKViewDrawableColorFormatSRGBA8888](https://developer.apple.com/documentation/glkit/glkviewdrawablecolorformat/glkviewdrawablecolorformatsrgba8888)GLKitBase.h

## GSS

GSS.hgssapi.hAdded [#def kGSSICAppIdentifierACL](https://developer.apple.com/documentation/gss/kgssicappidentifieracl)Added [#def kGSSICKerberosCacheName](https://developer.apple.com/documentation/gss/kgssickerberoscachename)Added [#def kGSSICLKDCHostname](https://developer.apple.com/documentation/gss/kgssiclkdchostname)Modified [gss_aapl_change_password()](https://developer.apple.com/documentation/gss/1411903-gss_aapl_change_password)

|  | Header | Declaration |
| --- | --- | --- |
| From | GSS/gssapi.h | OM_uint32 gss_aapl_change_password ( const gss_name_t name, gss_const_OID mech, CFDictionaryRef attributes, CFErrorRef \*error); |
| To | GSS/gssapi_apple.h | OM_uint32 gss_aapl_change_password ( const gss_name_t, gss_const_OID, CFDictionaryRef, CFErrorRef \*); |

gssapi_apple.hAdded [GSSCreateCredentialFromUUID()](https://developer.apple.com/documentation/gss/1411915-gsscreatecredentialfromuuid)Added [GSSCreateName()](https://developer.apple.com/documentation/gss/1411907-gsscreatename)Added [GSSCredentialCopyName()](https://developer.apple.com/documentation/gss/1411911-gsscredentialcopyname)Added [GSSCredentialCopyUUID()](https://developer.apple.com/documentation/gss/1411905-gsscredentialcopyuuid)Added [GSSCredentialGetLifetime()](https://developer.apple.com/documentation/gss/1411899-gsscredentialgetlifetime)Added [GSSNameCreateDisplayString()](https://developer.apple.com/documentation/gss/1411901-gssnamecreatedisplaystring)Modified [gss_aapl_change_password()](https://developer.apple.com/documentation/gss/1411903-gss_aapl_change_password)

|  | Header | Declaration |
| --- | --- | --- |
| From | GSS/gssapi.h | OM_uint32 gss_aapl_change_password ( const gss_name_t name, gss_const_OID mech, CFDictionaryRef attributes, CFErrorRef \*error); |
| To | GSS/gssapi_apple.h | OM_uint32 gss_aapl_change_password ( const gss_name_t, gss_const_OID, CFDictionaryRef, CFErrorRef \*); |

gssapi_oid.hAdded #def GSS_C_CRED_HEIMBASEgssapi_protos.hAdded [gss_userok()](https://developer.apple.com/documentation/gss/1438440-gss_userok)

## iAd

ADBannerView.hModified [ADBannerView.delegate](https://developer.apple.com/documentation/iad/adbannerview/1614649-delegate)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, assign) id<ADBannerViewDelegate> delegate |
| To | @property(nonatomic, weak) id<ADBannerViewDelegate> delegate |

ADInterstitialAd.hAdded #def IAD_DEPRECATED_IOS_MSGModified [ADInterstitialAd.delegate](https://developer.apple.com/documentation/iad/adinterstitialad/1614647-delegate)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, assign) id<ADInterstitialAdDelegate> delegate |
| To | @property(nonatomic, weak) id<ADInterstitialAdDelegate> delegate |

Modified [-[ADInterstitialAd presentFromViewController:]](https://developer.apple.com/documentation/iad/adinterstitialad/1621985-presentfromviewcontroller)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

MPMoviePlayerController_iAdPreroll.hAdded [-[MPMoviePlayerController playPrerollAdWithCompletionHandler:]](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1614690-playprerollad)Added [+[MPMoviePlayerController preparePrerollAds]](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1614610-prepareprerollads)Added MPMoviePlayerController(iAdPreroll)UIViewControlleriAdAdditions.hAdded [UIViewController.canDisplayBannerAds](https://developer.apple.com/documentation/uikit/uiviewcontroller/1614606-candisplaybannerads)Added [UIViewController.displayingBannerAd](https://developer.apple.com/documentation/uikit/uiviewcontroller/1614640-isdisplayingbannerad)Added [UIViewController.interstitialPresentationPolicy](https://developer.apple.com/documentation/uikit/uiviewcontroller/1614670-interstitialpresentationpolicy)Added [UIViewController.originalContentView](https://developer.apple.com/documentation/uikit/uiviewcontroller/1614605-originalcontentview)Added [+[UIViewController prepareInterstitialAds]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1614624-prepareinterstitialads)Added [UIViewController.presentingFullScreenAd](https://developer.apple.com/documentation/uikit/uiviewcontroller/1614630-ispresentingfullscreenad)Added [-[UIViewController requestInterstitialAdPresentation]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1614631-requestinterstitialadpresentatio)Added [-[UIViewController shouldPresentInterstitialAd]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1614627-shouldpresentinterstitialad)Added [ADInterstitialPresentationPolicy](https://developer.apple.com/documentation/iad/adinterstitialpresentationpolicy)Added [ADInterstitialPresentationPolicyAutomatic](https://developer.apple.com/documentation/iad/adinterstitialpresentationpolicy/adinterstitialpresentationpolicyautomatic)Added [ADInterstitialPresentationPolicyManual](https://developer.apple.com/documentation/iad/adinterstitialpresentationpolicy/adinterstitialpresentationpolicymanual)Added [ADInterstitialPresentationPolicyNone](https://developer.apple.com/documentation/iad/adinterstitialpresentationpolicy/none)Added UIViewController(iAdAdditions)

## ImageIO

CGImageDestination.hAdded [CGImageDestinationAddImageAndMetadata()](https://developer.apple.com/documentation/imageio/1465429-cgimagedestinationaddimageandmet)Added [CGImageDestinationCopyImageSource()](https://developer.apple.com/documentation/imageio/1465189-cgimagedestinationcopyimagesourc)Added [kCGImageDestinationDateTime](https://developer.apple.com/documentation/imageio/kcgimagedestinationdatetime)Added [kCGImageDestinationMergeMetadata](https://developer.apple.com/documentation/imageio/kcgimagedestinationmergemetadata)Added [kCGImageDestinationMetadata](https://developer.apple.com/documentation/imageio/kcgimagedestinationmetadata)Added [kCGImageDestinationOrientation](https://developer.apple.com/documentation/imageio/kcgimagedestinationorientation)Added [kCGImageMetadataShouldExcludeXMP](https://developer.apple.com/documentation/imageio/kcgimagemetadatashouldexcludexmp)CGImageMetadata.hAdded [CGImageMetadataCopyStringValueWithPath()](https://developer.apple.com/documentation/imageio/1465254-cgimagemetadatacopystringvaluewi)Added [CGImageMetadataCopyTagMatchingImageProperty()](https://developer.apple.com/documentation/imageio/1465081-cgimagemetadatacopytagmatchingim)Added [CGImageMetadataCopyTagWithPath()](https://developer.apple.com/documentation/imageio/1465022-cgimagemetadatacopytagwithpath)Added [CGImageMetadataCopyTags()](https://developer.apple.com/documentation/imageio/1464944-cgimagemetadatacopytags)Added [CGImageMetadataCreateFromXMPData()](https://developer.apple.com/documentation/imageio/1465001-cgimagemetadatacreatefromxmpdata)Added [CGImageMetadataCreateMutable()](https://developer.apple.com/documentation/imageio/1465356-cgimagemetadatacreatemutable)Added [CGImageMetadataCreateMutableCopy()](https://developer.apple.com/documentation/imageio/1465213-cgimagemetadatacreatemutablecopy)Added [CGImageMetadataCreateXMPData()](https://developer.apple.com/documentation/imageio/1465217-cgimagemetadatacreatexmpdata)Added [CGImageMetadataEnumerateTagsUsingBlock()](https://developer.apple.com/documentation/imageio/1465182-cgimagemetadataenumeratetagsusin)Added [CGImageMetadataErrors](https://developer.apple.com/documentation/imageio/cgimagemetadataerrors)Added [CGImageMetadataGetTypeID()](https://developer.apple.com/documentation/imageio/1465148-cgimagemetadatagettypeid)Added [CGImageMetadataRef](https://developer.apple.com/documentation/imageio/cgimagemetadataref)Added [CGImageMetadataRegisterNamespaceForPrefix()](https://developer.apple.com/documentation/imageio/1465270-cgimagemetadataregisternamespace)Added [CGImageMetadataRemoveTagWithPath()](https://developer.apple.com/documentation/imageio/1465138-cgimagemetadataremovetagwithpath)Added [CGImageMetadataSetTagWithPath()](https://developer.apple.com/documentation/imageio/1465409-cgimagemetadatasettagwithpath)Added [CGImageMetadataSetValueMatchingImageProperty()](https://developer.apple.com/documentation/imageio/1464974-cgimagemetadatasetvaluematchingi)Added [CGImageMetadataSetValueWithPath()](https://developer.apple.com/documentation/imageio/1465265-cgimagemetadatasetvaluewithpath)Added [CGImageMetadataTagBlock](https://developer.apple.com/documentation/imageio/cgimagemetadatatagblock)Added [CGImageMetadataTagCopyName()](https://developer.apple.com/documentation/imageio/1465092-cgimagemetadatatagcopyname)Added [CGImageMetadataTagCopyNamespace()](https://developer.apple.com/documentation/imageio/1465160-cgimagemetadatatagcopynamespace)Added [CGImageMetadataTagCopyPrefix()](https://developer.apple.com/documentation/imageio/1465378-cgimagemetadatatagcopyprefix)Added [CGImageMetadataTagCopyQualifiers()](https://developer.apple.com/documentation/imageio/1465094-cgimagemetadatatagcopyqualifiers)Added [CGImageMetadataTagCopyValue()](https://developer.apple.com/documentation/imageio/1464942-cgimagemetadatatagcopyvalue)Added [CGImageMetadataTagCreate()](https://developer.apple.com/documentation/imageio/1465060-cgimagemetadatatagcreate)Added [CGImageMetadataTagGetType()](https://developer.apple.com/documentation/imageio/1465337-cgimagemetadatataggettype)Added [CGImageMetadataTagGetTypeID()](https://developer.apple.com/documentation/imageio/1465320-cgimagemetadatataggettypeid)Added [CGImageMetadataTagRef](https://developer.apple.com/documentation/imageio/cgimagemetadatatagref)Added [CGImageMetadataType](https://developer.apple.com/documentation/imageio/cgimagemetadatatype)Added [CGMutableImageMetadataRef](https://developer.apple.com/documentation/imageio/cgmutableimagemetadata)Added [kCFErrorDomainCGImageMetadata](https://developer.apple.com/documentation/imageio/kcferrordomaincgimagemetadata)Added [kCGImageMetadataEnumerateRecursively](https://developer.apple.com/documentation/imageio/kcgimagemetadataenumeraterecursively)Added [kCGImageMetadataErrorBadArgument](https://developer.apple.com/documentation/imageio/cgimagemetadataerrors/kcgimagemetadataerrorbadargument)Added [kCGImageMetadataErrorConflictingArguments](https://developer.apple.com/documentation/imageio/cgimagemetadataerrors/kcgimagemetadataerrorconflictingarguments)Added [kCGImageMetadataErrorPrefixConflict](https://developer.apple.com/documentation/imageio/cgimagemetadataerrors/prefixconflict)Added [kCGImageMetadataErrorUnknown](https://developer.apple.com/documentation/imageio/cgimagemetadataerrors/unknown)Added [kCGImageMetadataErrorUnsupportedFormat](https://developer.apple.com/documentation/imageio/cgimagemetadataerrors/unsupportedformat)Added [kCGImageMetadataNamespaceDublinCore](https://developer.apple.com/documentation/imageio/kcgimagemetadatanamespacedublincore)Added [kCGImageMetadataNamespaceExif](https://developer.apple.com/documentation/imageio/kcgimagemetadatanamespaceexif)Added [kCGImageMetadataNamespaceExifAux](https://developer.apple.com/documentation/imageio/kcgimagemetadatanamespaceexifaux)Added [kCGImageMetadataNamespaceExifEX](https://developer.apple.com/documentation/imageio/kcgimagemetadatanamespaceexifex)Added [kCGImageMetadataNamespaceIPTCCore](https://developer.apple.com/documentation/imageio/kcgimagemetadatanamespaceiptccore)Added [kCGImageMetadataNamespacePhotoshop](https://developer.apple.com/documentation/imageio/kcgimagemetadatanamespacephotoshop)Added [kCGImageMetadataNamespaceTIFF](https://developer.apple.com/documentation/imageio/kcgimagemetadatanamespacetiff)Added [kCGImageMetadataNamespaceXMPBasic](https://developer.apple.com/documentation/imageio/kcgimagemetadatanamespacexmpbasic)Added [kCGImageMetadataNamespaceXMPRights](https://developer.apple.com/documentation/imageio/kcgimagemetadatanamespacexmprights)Added [kCGImageMetadataPrefixDublinCore](https://developer.apple.com/documentation/imageio/kcgimagemetadataprefixdublincore)Added [kCGImageMetadataPrefixExif](https://developer.apple.com/documentation/imageio/kcgimagemetadataprefixexif)Added [kCGImageMetadataPrefixExifAux](https://developer.apple.com/documentation/imageio/kcgimagemetadataprefixexifaux)Added [kCGImageMetadataPrefixExifEX](https://developer.apple.com/documentation/imageio/kcgimagemetadataprefixexifex)Added [kCGImageMetadataPrefixIPTCCore](https://developer.apple.com/documentation/imageio/kcgimagemetadataprefixiptccore)Added [kCGImageMetadataPrefixPhotoshop](https://developer.apple.com/documentation/imageio/kcgimagemetadataprefixphotoshop)Added [kCGImageMetadataPrefixTIFF](https://developer.apple.com/documentation/imageio/kcgimagemetadataprefixtiff)Added [kCGImageMetadataPrefixXMPBasic](https://developer.apple.com/documentation/imageio/kcgimagemetadataprefixxmpbasic)Added [kCGImageMetadataPrefixXMPRights](https://developer.apple.com/documentation/imageio/kcgimagemetadataprefixxmprights)Added [kCGImageMetadataTypeAlternateArray](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/kcgimagemetadatatypealternatearray)Added [kCGImageMetadataTypeAlternateText](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/alternatetext)Added [kCGImageMetadataTypeArrayOrdered](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/arrayordered)Added [kCGImageMetadataTypeArrayUnordered](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/arrayunordered)Added [kCGImageMetadataTypeDefault](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/kcgimagemetadatatypedefault)Added [kCGImageMetadataTypeInvalid](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/invalid)Added [kCGImageMetadataTypeString](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/kcgimagemetadatatypestring)Added [kCGImageMetadataTypeStructure](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/structure)CGImageProperties.hAdded [kCGImagePropertyExifISOSpeed](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifisospeed)Added [kCGImagePropertyExifISOSpeedLatitudeyyy](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifisospeedlatitudeyyy)Added [kCGImagePropertyExifISOSpeedLatitudezzz](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifisospeedlatitudezzz)Added [kCGImagePropertyExifRecommendedExposureIndex](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifrecommendedexposureindex)Added [kCGImagePropertyExifSensitivityType](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifsensitivitytype)Added [kCGImagePropertyExifStandardOutputSensitivity](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifstandardoutputsensitivity)Added [kCGImagePropertyMakerAppleDictionary](https://developer.apple.com/documentation/imageio/kcgimagepropertymakerappledictionary)CGImageSource.hAdded [CGImageSourceCopyMetadataAtIndex()](https://developer.apple.com/documentation/imageio/1465476-cgimagesourcecopymetadataatindex)Added [CGImageSourceRemoveCacheAtIndex()](https://developer.apple.com/documentation/imageio/1465077-cgimagesourceremovecacheatindex)Added [kCGImageSourceShouldCacheImmediately](https://developer.apple.com/documentation/imageio/kcgimagesourceshouldcacheimmediately)

## IOKit

No changes

## JavaScriptCore

JSBase.hAdded [#def JSC_OBJC_API_ENABLED](https://developer.apple.com/documentation/javascriptcore/jsc_objc_api_enabled)Added [JSCheckScriptSyntax()](https://developer.apple.com/documentation/javascriptcore/1451547-jscheckscriptsyntax)Added [JSClassRef](https://developer.apple.com/documentation/javascriptcore/jsclassref)Added [JSContextGroupRef](https://developer.apple.com/documentation/javascriptcore/jscontextgroupref)Added [JSContextRef](https://developer.apple.com/documentation/javascriptcore/jscontextref)Added [JSEvaluateScript()](https://developer.apple.com/documentation/javascriptcore/1451589-jsevaluatescript)Added [JSGarbageCollect()](https://developer.apple.com/documentation/javascriptcore/1451393-jsgarbagecollect)Added [JSGlobalContextRef](https://developer.apple.com/documentation/javascriptcore/jsglobalcontextref)Added [JSObjectRef](https://developer.apple.com/documentation/javascriptcore/jsobjectref)Added [JSPropertyNameAccumulatorRef](https://developer.apple.com/documentation/javascriptcore/jspropertynameaccumulatorref)Added [JSPropertyNameArrayRef](https://developer.apple.com/documentation/javascriptcore/jspropertynamearrayref)Added [JSStringRef](https://developer.apple.com/documentation/javascriptcore/jsstringref)Added [JSValueRef](https://developer.apple.com/documentation/javascriptcore/jsvalueref)Added #def WTF_EXPORT_PRIVATEAdded #def WTF_PLATFORM_IOSJSContext.hAdded [JSContext](https://developer.apple.com/documentation/javascriptcore/jscontext)Added [-[JSContext JSGlobalContextRef]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451338-jsglobalcontextref)Added [+[JSContext contextWithJSGlobalContextRef:]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451491-init)Added [+[JSContext currentArguments]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451650-currentarguments)Added [+[JSContext currentContext]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451545-current)Added [+[JSContext currentThis]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451767-currentthis)Added [-[JSContext evaluateScript:]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451350-evaluatescript)Added [JSContext.exception](https://developer.apple.com/documentation/javascriptcore/jscontext/1451499-exception)Added [JSContext.exceptionHandler](https://developer.apple.com/documentation/javascriptcore/jscontext/1451731-exceptionhandler)Added [-[JSContext globalObject]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451436-globalobject)Added [-[JSContext init]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451742-init)Added [-[JSContext initWithVirtualMachine:]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451554-initwithvirtualmachine)Added [-[JSContext objectForKeyedSubscript:]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451771-objectforkeyedsubscript)Added [-[JSContext setObject:forKeyedSubscript:]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451416-setobject)Added [JSContext.virtualMachine](https://developer.apple.com/documentation/javascriptcore/jscontext/1451510-virtualmachine)Added JSContext(JSContextRefSupport)Added JSContext(SubscriptSupport)Added #def JSContext_hJSContextRef.hAdded [JSContextGetGlobalObject()](https://developer.apple.com/documentation/javascriptcore/1451440-jscontextgetglobalobject)Added [JSContextGetGroup()](https://developer.apple.com/documentation/javascriptcore/1451429-jscontextgetgroup)Added [JSContextGroupCreate()](https://developer.apple.com/documentation/javascriptcore/1451632-jscontextgroupcreate)Added [JSContextGroupRelease()](https://developer.apple.com/documentation/javascriptcore/1451520-jscontextgrouprelease)Added [JSContextGroupRetain()](https://developer.apple.com/documentation/javascriptcore/1451564-jscontextgroupretain)Added [JSGlobalContextCreate()](https://developer.apple.com/documentation/javascriptcore/1451585-jsglobalcontextcreate)Added [JSGlobalContextCreateInGroup()](https://developer.apple.com/documentation/javascriptcore/1451710-jsglobalcontextcreateingroup)Added [JSGlobalContextRelease()](https://developer.apple.com/documentation/javascriptcore/1451599-jsglobalcontextrelease)Added [JSGlobalContextRetain()](https://developer.apple.com/documentation/javascriptcore/1451719-jsglobalcontextretain)JSExport.hAdded [JSExport](https://developer.apple.com/documentation/javascriptcore/jsexport)Added #def JSExportAsJSManagedValue.hAdded [JSManagedValue](https://developer.apple.com/documentation/javascriptcore/jsmanagedvalue)Added [-[JSManagedValue initWithValue:]](https://developer.apple.com/documentation/javascriptcore/jsmanagedvalue/1451420-init)Added [+[JSManagedValue managedValueWithValue:]](https://developer.apple.com/documentation/javascriptcore/jsmanagedvalue/1501484-managedvaluewithvalue)Added [-[JSManagedValue value]](https://developer.apple.com/documentation/javascriptcore/jsmanagedvalue/1451448-value)Added #def JSManagedValue_hJSObjectRef.hAdded [JSClassAttributes](https://developer.apple.com/documentation/javascriptcore/jsclassattributes)Added [JSClassCreate()](https://developer.apple.com/documentation/javascriptcore/1451678-jsclasscreate)Added [JSClassDefinition](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition)Added [JSClassRelease()](https://developer.apple.com/documentation/javascriptcore/1451508-jsclassrelease)Added [JSClassRetain()](https://developer.apple.com/documentation/javascriptcore/1451344-jsclassretain)Added [JSObjectCallAsConstructor()](https://developer.apple.com/documentation/javascriptcore/1451445-jsobjectcallasconstructor)Added [JSObjectCallAsConstructorCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectcallasconstructorcallback)Added [JSObjectCallAsFunction()](https://developer.apple.com/documentation/javascriptcore/1451407-jsobjectcallasfunction)Added [JSObjectCallAsFunctionCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectcallasfunctioncallback)Added [JSObjectConvertToTypeCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectconverttotypecallback)Added [JSObjectCopyPropertyNames()](https://developer.apple.com/documentation/javascriptcore/1451560-jsobjectcopypropertynames)Added [JSObjectDeleteProperty()](https://developer.apple.com/documentation/javascriptcore/1451595-jsobjectdeleteproperty)Added [JSObjectDeletePropertyCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectdeletepropertycallback)Added [JSObjectFinalizeCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectfinalizecallback)Added [JSObjectGetPrivate()](https://developer.apple.com/documentation/javascriptcore/1451515-jsobjectgetprivate)Added [JSObjectGetProperty()](https://developer.apple.com/documentation/javascriptcore/1451619-jsobjectgetproperty)Added [JSObjectGetPropertyAtIndex()](https://developer.apple.com/documentation/javascriptcore/1451717-jsobjectgetpropertyatindex)Added [JSObjectGetPropertyCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectgetpropertycallback)Added [JSObjectGetPropertyNamesCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectgetpropertynamescallback)Added [JSObjectGetPrototype()](https://developer.apple.com/documentation/javascriptcore/1451342-jsobjectgetprototype)Added [JSObjectHasInstanceCallback](https://developer.apple.com/documentation/javascriptcore/jsobjecthasinstancecallback)Added [JSObjectHasProperty()](https://developer.apple.com/documentation/javascriptcore/1451558-jsobjecthasproperty)Added [JSObjectHasPropertyCallback](https://developer.apple.com/documentation/javascriptcore/jsobjecthaspropertycallback)Added [JSObjectInitializeCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectinitializecallback)Added [JSObjectIsConstructor()](https://developer.apple.com/documentation/javascriptcore/1451486-jsobjectisconstructor)Added [JSObjectIsFunction()](https://developer.apple.com/documentation/javascriptcore/1451769-jsobjectisfunction)Added [JSObjectMake()](https://developer.apple.com/documentation/javascriptcore/1451624-jsobjectmake)Added [JSObjectMakeArray()](https://developer.apple.com/documentation/javascriptcore/1451661-jsobjectmakearray)Added [JSObjectMakeConstructor()](https://developer.apple.com/documentation/javascriptcore/1451566-jsobjectmakeconstructor)Added [JSObjectMakeDate()](https://developer.apple.com/documentation/javascriptcore/1451745-jsobjectmakedate)Added [JSObjectMakeError()](https://developer.apple.com/documentation/javascriptcore/1451375-jsobjectmakeerror)Added [JSObjectMakeFunction()](https://developer.apple.com/documentation/javascriptcore/1451478-jsobjectmakefunction)Added [JSObjectMakeFunctionWithCallback()](https://developer.apple.com/documentation/javascriptcore/1451336-jsobjectmakefunctionwithcallback)Added [JSObjectMakeRegExp()](https://developer.apple.com/documentation/javascriptcore/1451530-jsobjectmakeregexp)Added [JSObjectSetPrivate()](https://developer.apple.com/documentation/javascriptcore/1451626-jsobjectsetprivate)Added [JSObjectSetProperty()](https://developer.apple.com/documentation/javascriptcore/1451687-jsobjectsetproperty)Added [JSObjectSetPropertyAtIndex()](https://developer.apple.com/documentation/javascriptcore/1451744-jsobjectsetpropertyatindex)Added [JSObjectSetPropertyCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectsetpropertycallback)Added [JSObjectSetPrototype()](https://developer.apple.com/documentation/javascriptcore/1451747-jsobjectsetprototype)Added [JSPropertyAttributes](https://developer.apple.com/documentation/javascriptcore/jspropertyattributes)Added [JSPropertyNameAccumulatorAddName()](https://developer.apple.com/documentation/javascriptcore/1451395-jspropertynameaccumulatoraddname)Added [JSPropertyNameArrayGetCount()](https://developer.apple.com/documentation/javascriptcore/1451573-jspropertynamearraygetcount)Added [JSPropertyNameArrayGetNameAtIndex()](https://developer.apple.com/documentation/javascriptcore/1451592-jspropertynamearraygetnameatinde)Added [JSPropertyNameArrayRelease()](https://developer.apple.com/documentation/javascriptcore/1451569-jspropertynamearrayrelease)Added [JSPropertyNameArrayRetain()](https://developer.apple.com/documentation/javascriptcore/1451352-jspropertynamearrayretain)Added [JSStaticFunction](https://developer.apple.com/documentation/javascriptcore/jsstaticfunction)Added [JSStaticValue](https://developer.apple.com/documentation/javascriptcore/jsstaticvalue)Added [kJSClassAttributeNoAutomaticPrototype](https://developer.apple.com/documentation/javascriptcore/1563361-jsclassattribute/kjsclassattributenoautomaticprototype)Added [kJSClassAttributeNone](https://developer.apple.com/documentation/javascriptcore/1563361-jsclassattribute/kjsclassattributenone)Added [kJSClassDefinitionEmpty](https://developer.apple.com/documentation/javascriptcore/kjsclassdefinitionempty)Added [kJSPropertyAttributeDontDelete](https://developer.apple.com/documentation/javascriptcore/kjspropertyattributedontdelete)Added [kJSPropertyAttributeDontEnum](https://developer.apple.com/documentation/javascriptcore/kjspropertyattributedontenum)Added [kJSPropertyAttributeNone](https://developer.apple.com/documentation/javascriptcore/1563363-jspropertyattribute/kjspropertyattributenone)Added [kJSPropertyAttributeReadOnly](https://developer.apple.com/documentation/javascriptcore/kjspropertyattributereadonly)JSStringRef.hAdded [JSChar](https://developer.apple.com/documentation/javascriptcore/jschar)Added [JSStringCreateWithCharacters()](https://developer.apple.com/documentation/javascriptcore/1412810-jsstringcreatewithcharacters)Added [JSStringCreateWithUTF8CString()](https://developer.apple.com/documentation/javascriptcore/1412806-jsstringcreatewithutf8cstring)Added [JSStringGetCharactersPtr()](https://developer.apple.com/documentation/javascriptcore/1412796-jsstringgetcharactersptr)Added [JSStringGetLength()](https://developer.apple.com/documentation/javascriptcore/1412802-jsstringgetlength)Added [JSStringGetMaximumUTF8CStringSize()](https://developer.apple.com/documentation/javascriptcore/1412800-jsstringgetmaximumutf8cstringsiz)Added [JSStringGetUTF8CString()](https://developer.apple.com/documentation/javascriptcore/1412812-jsstringgetutf8cstring)Added [JSStringIsEqual()](https://developer.apple.com/documentation/javascriptcore/1412804-jsstringisequal)Added [JSStringIsEqualToUTF8CString()](https://developer.apple.com/documentation/javascriptcore/1412792-jsstringisequaltoutf8cstring)Added [JSStringRelease()](https://developer.apple.com/documentation/javascriptcore/1412814-jsstringrelease)Added [JSStringRetain()](https://developer.apple.com/documentation/javascriptcore/1412794-jsstringretain)JSStringRefCF.hAdded [JSStringCopyCFString()](https://developer.apple.com/documentation/javascriptcore/1451659-jsstringcopycfstring)Added [JSStringCreateWithCFString()](https://developer.apple.com/documentation/javascriptcore/1451524-jsstringcreatewithcfstring)JSValue.hAdded [JSValue](https://developer.apple.com/documentation/javascriptcore/jsvalue)Added [-[JSValue JSValueRef]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451639-jsvalueref)Added [-[JSValue callWithArguments:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451648-call)Added [-[JSValue constructWithArguments:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451480-constructwitharguments)Added [JSValue.context](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451518-context)Added [-[JSValue defineProperty:descriptor:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451542-defineproperty)Added [-[JSValue deleteProperty:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451609-deleteproperty)Added [-[JSValue hasProperty:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451361-hasproperty)Added [-[JSValue invokeMethod:withArguments:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451666-invokemethod)Added [-[JSValue isBoolean]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451367-isboolean)Added [-[JSValue isEqualToObject:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451504-isequaltoobject)Added [-[JSValue isEqualWithTypeCoercionToObject:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451765-isequalwithtypecoerciontoobject)Added [-[JSValue isInstanceOf:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451691-isinstance)Added [-[JSValue isNull]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451369-isnull)Added [-[JSValue isNumber]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451682-isnumber)Added [-[JSValue isObject]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451461-isobject)Added [-[JSValue isString]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451427-isstring)Added [-[JSValue isUndefined]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451365-isundefined)Added [-[JSValue objectAtIndexedSubscript:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451549-objectatindexedsubscript)Added [-[JSValue objectForKeyedSubscript:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451371-objectforkeyedsubscript)Added [-[JSValue setObject:atIndexedSubscript:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451583-setobject)Added [-[JSValue setObject:forKeyedSubscript:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451672-setobject)Added [-[JSValue setValue:atIndex:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451533-setvalue)Added [-[JSValue setValue:forProperty:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451676-setvalue)Added [-[JSValue toArray]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451465-toarray)Added [-[JSValue toBool]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451373-tobool)Added [-[JSValue toDate]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451753-todate)Added [-[JSValue toDictionary]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451728-todictionary)Added [-[JSValue toDouble]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451581-todouble)Added [-[JSValue toInt32]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451493-toint32)Added [-[JSValue toNumber]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451459-tonumber)Added [-[JSValue toObject]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451725-toobject)Added [-[JSValue toObjectOfClass:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451760-toobjectof)Added [-[JSValue toPoint]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451591-topoint)Added [-[JSValue toRange]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451423-torange)Added [-[JSValue toRect]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451389-torect)Added [-[JSValue toSize]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451495-tosize)Added [-[JSValue toString]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451409-tostring)Added [-[JSValue toUInt32]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451739-touint32)Added [-[JSValue valueAtIndex:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451602-valueatindex)Added [-[JSValue valueForProperty:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451438-valueforproperty)Added [+[JSValue valueWithBool:inContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451616-init)Added [+[JSValue valueWithDouble:inContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451482-valuewithdouble)Added [+[JSValue valueWithInt32:inContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451434-init)Added [+[JSValue valueWithJSValueRef:inContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451641-init)Added [+[JSValue valueWithNewArrayInContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451473-init)Added [+[JSValue valueWithNewErrorFromMessage:inContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451630-valuewithnewerrorfrommessage)Added [+[JSValue valueWithNewObjectInContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451751-init)Added [+[JSValue valueWithNewRegularExpressionFromPattern:flags:inContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451539-valuewithnewregularexpressionfro)Added [+[JSValue valueWithNullInContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451463-valuewithnullincontext)Added [+[JSValue valueWithObject:inContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451694-valuewithobject)Added [+[JSValue valueWithPoint:inContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451382-valuewithpoint)Added [+[JSValue valueWithRange:inContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451628-valuewithrange)Added [+[JSValue valueWithRect:inContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451664-init)Added [+[JSValue valueWithSize:inContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451715-valuewithsize)Added [+[JSValue valueWithUInt32:inContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451402-init)Added [+[JSValue valueWithUndefinedInContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451387-init)Added [JSPropertyDescriptorConfigurableKey](https://developer.apple.com/documentation/javascriptcore/jspropertydescriptorconfigurablekey)Added [JSPropertyDescriptorEnumerableKey](https://developer.apple.com/documentation/javascriptcore/jspropertydescriptorenumerablekey)Added [JSPropertyDescriptorGetKey](https://developer.apple.com/documentation/javascriptcore/jspropertydescriptorgetkey)Added [JSPropertyDescriptorSetKey](https://developer.apple.com/documentation/javascriptcore/jspropertydescriptorsetkey)Added [JSPropertyDescriptorValueKey](https://developer.apple.com/documentation/javascriptcore/jspropertydescriptorvaluekey)Added [JSPropertyDescriptorWritableKey](https://developer.apple.com/documentation/javascriptcore/jspropertydescriptorwritablekey)Added JSValue(JSValueRefSupport)Added JSValue(StructSupport)Added JSValue(SubscriptSupport)Added #def JSValue_hJSValueRef.hAdded [JSType](https://developer.apple.com/documentation/javascriptcore/jstype)Added [JSValueCreateJSONString()](https://developer.apple.com/documentation/javascriptcore/1395934-jsvaluecreatejsonstring)Added [JSValueGetType()](https://developer.apple.com/documentation/javascriptcore/1395918-jsvaluegettype)Added [JSValueIsBoolean()](https://developer.apple.com/documentation/javascriptcore/1395970-jsvalueisboolean)Added [JSValueIsEqual()](https://developer.apple.com/documentation/javascriptcore/1395960-jsvalueisequal)Added [JSValueIsInstanceOfConstructor()](https://developer.apple.com/documentation/javascriptcore/1395944-jsvalueisinstanceofconstructor)Added [JSValueIsNull()](https://developer.apple.com/documentation/javascriptcore/1395966-jsvalueisnull)Added [JSValueIsNumber()](https://developer.apple.com/documentation/javascriptcore/1395958-jsvalueisnumber)Added [JSValueIsObject()](https://developer.apple.com/documentation/javascriptcore/1395954-jsvalueisobject)Added [JSValueIsObjectOfClass()](https://developer.apple.com/documentation/javascriptcore/1395932-jsvalueisobjectofclass)Added [JSValueIsStrictEqual()](https://developer.apple.com/documentation/javascriptcore/1395920-jsvalueisstrictequal)Added [JSValueIsString()](https://developer.apple.com/documentation/javascriptcore/1395940-jsvalueisstring)Added [JSValueIsUndefined()](https://developer.apple.com/documentation/javascriptcore/1395964-jsvalueisundefined)Added [JSValueMakeBoolean()](https://developer.apple.com/documentation/javascriptcore/1395946-jsvaluemakeboolean)Added [JSValueMakeFromJSONString()](https://developer.apple.com/documentation/javascriptcore/1395928-jsvaluemakefromjsonstring)Added [JSValueMakeNull()](https://developer.apple.com/documentation/javascriptcore/1395942-jsvaluemakenull)Added [JSValueMakeNumber()](https://developer.apple.com/documentation/javascriptcore/1395952-jsvaluemakenumber)Added [JSValueMakeString()](https://developer.apple.com/documentation/javascriptcore/1395980-jsvaluemakestring)Added [JSValueMakeUndefined()](https://developer.apple.com/documentation/javascriptcore/1395974-jsvaluemakeundefined)Added [JSValueProtect()](https://developer.apple.com/documentation/javascriptcore/1395978-jsvalueprotect)Added [JSValueToBoolean()](https://developer.apple.com/documentation/javascriptcore/1395930-jsvaluetoboolean)Added [JSValueToNumber()](https://developer.apple.com/documentation/javascriptcore/1395968-jsvaluetonumber)Added [JSValueToObject()](https://developer.apple.com/documentation/javascriptcore/1395950-jsvaluetoobject)Added [JSValueToStringCopy()](https://developer.apple.com/documentation/javascriptcore/1395972-jsvaluetostringcopy)Added [JSValueUnprotect()](https://developer.apple.com/documentation/javascriptcore/1395922-jsvalueunprotect)Added [kJSTypeBoolean](https://developer.apple.com/documentation/javascriptcore/kjstypeboolean)Added [kJSTypeNull](https://developer.apple.com/documentation/javascriptcore/kjstypenull)Added [kJSTypeNumber](https://developer.apple.com/documentation/javascriptcore/jstype/kjstypenumber)Added [kJSTypeObject](https://developer.apple.com/documentation/javascriptcore/kjstypeobject)Added [kJSTypeString](https://developer.apple.com/documentation/javascriptcore/kjstypestring)Added [kJSTypeUndefined](https://developer.apple.com/documentation/javascriptcore/kjstypeundefined)JSVirtualMachine.hAdded [JSVirtualMachine](https://developer.apple.com/documentation/javascriptcore/jsvirtualmachine)Added [-[JSVirtualMachine addManagedReference:withOwner:]](https://developer.apple.com/documentation/javascriptcore/jsvirtualmachine/1451354-addmanagedreference)Added [-[JSVirtualMachine init]](https://developer.apple.com/documentation/javascriptcore/jsvirtualmachine/1451568-init)Added [-[JSVirtualMachine removeManagedReference:withOwner:]](https://developer.apple.com/documentation/javascriptcore/jsvirtualmachine/1451452-removemanagedreference)JavaScript.hJavaScriptCore.hWebKitAvailability.hAdded #def AVAILABLE_AFTER_WEBKIT_VERSION_5_1Added #def AVAILABLE_WEBKIT_VERSION_1_3_AND_LATER_BUT_DEPRECATED_AFTER_WEBKIT_VERSION_5_1Added #def WEBKIT_OBJC_METHOD_ANNOTATIONAdded #def WEBKIT_VERSION_1_0Added #def WEBKIT_VERSION_1_1Added #def WEBKIT_VERSION_1_2Added #def WEBKIT_VERSION_1_3Added #def WEBKIT_VERSION_2_0Added #def WEBKIT_VERSION_3_0Added #def WEBKIT_VERSION_3_1Added #def WEBKIT_VERSION_4_0Added #def WEBKIT_VERSION_LATESTAdded #def WEBKIT_VERSION_MAX_ALLOWEDAdded #def WEBKIT_VERSION_MIN_REQUIRED

## MapKit

MKCircleRenderer.hAdded [MKCircleRenderer](https://developer.apple.com/documentation/mapkit/mkcirclerenderer)Added [MKCircleRenderer.circle](https://developer.apple.com/documentation/mapkit/mkcirclerenderer/1452413-circle)Added [-[MKCircleRenderer initWithCircle:]](https://developer.apple.com/documentation/mapkit/mkcirclerenderer/1452547-initwithcircle)MKCircleView.hModified [MKCircleView.circle](https://developer.apple.com/documentation/mapkit/mkcircleview/1623525-circle)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[MKCircleView initWithCircle:]](https://developer.apple.com/documentation/mapkit/mkcircleview/1623524-initwithcircle)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

MKDirections.hAdded [MKDirections](https://developer.apple.com/documentation/mapkit/mkdirections)Added [-[MKDirections calculateDirectionsWithCompletionHandler:]](https://developer.apple.com/documentation/mapkit/mkdirections/1452078-calculate)Added [-[MKDirections calculateETAWithCompletionHandler:]](https://developer.apple.com/documentation/mapkit/mkdirections/1452736-calculateeta)Added [MKDirections.calculating](https://developer.apple.com/documentation/mapkit/mkdirections/1452217-iscalculating)Added [-[MKDirections cancel]](https://developer.apple.com/documentation/mapkit/mkdirections/1452656-cancel)Added [-[MKDirections initWithRequest:]](https://developer.apple.com/documentation/mapkit/mkdirections/1452197-init)Added [MKDirectionsHandler](https://developer.apple.com/documentation/mapkit/mkdirectionshandler)Added [MKETAHandler](https://developer.apple.com/documentation/mapkit/mkdirections/etahandler)MKDirectionsRequest.hRemoved [MKDirectionsRequest.destination](https://developer.apple.com/documentation/mapkit/mkdirections/request/1433146-destination)Removed [MKDirectionsRequest.source](https://developer.apple.com/documentation/mapkit/mkdirectionsrequest/1433144-source)Added [MKDirectionsRequest.arrivalDate](https://developer.apple.com/documentation/mapkit/mkdirections/request/1433148-arrivaldate)Added [MKDirectionsRequest.departureDate](https://developer.apple.com/documentation/mapkit/mkdirections/request/1433155-departuredate)Added [-[MKDirectionsRequest destination]](https://developer.apple.com/documentation/mapkit/mkdirectionsrequest/1433146-destination)Added [MKDirectionsRequest.requestsAlternateRoutes](https://developer.apple.com/documentation/mapkit/mkdirectionsrequest/1433154-requestsalternateroutes)Added [-[MKDirectionsRequest setDestination:]](https://developer.apple.com/documentation/mapkit/mkdirectionsrequest/1433157-setdestination)Added [-[MKDirectionsRequest setSource:]](https://developer.apple.com/documentation/mapkit/mkdirectionsrequest/1433156-setsource)Added [-[MKDirectionsRequest source]](https://developer.apple.com/documentation/mapkit/mkdirections/request/1433144-source)Added [MKDirectionsRequest.transportType](https://developer.apple.com/documentation/mapkit/mkdirections/request/1433152-transporttype)Added MKDirectionsRequest(MKDirectionsURL)Added MKDirectionsRequest(MKRequestOptions)MKDirectionsResponse.hAdded [MKDirectionsResponse](https://developer.apple.com/documentation/mapkit/mkdirections/response)Added [MKDirectionsResponse.destination](https://developer.apple.com/documentation/mapkit/mkdirections/response/1451981-destination)Added [MKDirectionsResponse.routes](https://developer.apple.com/documentation/mapkit/mkdirections/response/1452071-routes)Added [MKDirectionsResponse.source](https://developer.apple.com/documentation/mapkit/mkdirectionsresponse/1452261-source)Added [MKETAResponse](https://developer.apple.com/documentation/mapkit/mketaresponse)Added [MKETAResponse.destination](https://developer.apple.com/documentation/mapkit/mketaresponse/1452611-destination)Added [MKETAResponse.expectedTravelTime](https://developer.apple.com/documentation/mapkit/mketaresponse/1452551-expectedtraveltime)Added [MKETAResponse.source](https://developer.apple.com/documentation/mapkit/mketaresponse/1451947-source)Added [MKRoute](https://developer.apple.com/documentation/mapkit/mkroute)Added [MKRoute.advisoryNotices](https://developer.apple.com/documentation/mapkit/mkroute/1452359-advisorynotices)Added [MKRoute.distance](https://developer.apple.com/documentation/mapkit/mkroute/1452405-distance)Added [MKRoute.expectedTravelTime](https://developer.apple.com/documentation/mapkit/mkroute/1452297-expectedtraveltime)Added [MKRoute.name](https://developer.apple.com/documentation/mapkit/mkroute/1452684-name)Added [MKRoute.polyline](https://developer.apple.com/documentation/mapkit/mkroute/1451943-polyline)Added [MKRoute.steps](https://developer.apple.com/documentation/mapkit/mkroute/1452173-steps)Added [MKRoute.transportType](https://developer.apple.com/documentation/mapkit/mkroute/1452674-transporttype)Added [MKRouteStep](https://developer.apple.com/documentation/mapkit/mkroutestep)Added [MKRouteStep.distance](https://developer.apple.com/documentation/mapkit/mkroutestep/1452004-distance)Added [MKRouteStep.instructions](https://developer.apple.com/documentation/mapkit/mkroutestep/1452447-instructions)Added [MKRouteStep.notice](https://developer.apple.com/documentation/mapkit/mkroutestep/1452347-notice)Added [MKRouteStep.polyline](https://developer.apple.com/documentation/mapkit/mkroute/step/1452223-polyline)Added [MKRouteStep.transportType](https://developer.apple.com/documentation/mapkit/mkroute/step/1452051-transporttype)MKDirectionsTypes.hAdded [MKDirectionsTransportType](https://developer.apple.com/documentation/mapkit/mkdirectionstransporttype)Added [MKDirectionsTransportTypeAny](https://developer.apple.com/documentation/mapkit/mkdirectionstransporttype/1451972-any)Added [MKDirectionsTransportTypeAutomobile](https://developer.apple.com/documentation/mapkit/mkdirectionstransporttype/1452629-automobile)Added [MKDirectionsTransportTypeWalking](https://developer.apple.com/documentation/mapkit/mkdirectionstransporttype/mkdirectionstransporttypewalking)MKDistanceFormatter.hAdded [MKDistanceFormatter](https://developer.apple.com/documentation/mapkit/mkdistanceformatter)Added [-[MKDistanceFormatter distanceFromString:]](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/1452766-distance)Added [MKDistanceFormatter.locale](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/1452235-locale)Added [-[MKDistanceFormatter stringFromDistance:]](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/1451994-string)Added [MKDistanceFormatter.unitStyle](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/1452128-unitstyle)Added [MKDistanceFormatter.units](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/1452775-units)Added [MKDistanceFormatterUnitStyle](https://developer.apple.com/documentation/mapkit/mkdistanceformatterunitstyle)Added [MKDistanceFormatterUnitStyleAbbreviated](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/unitstyle/abbreviated)Added [MKDistanceFormatterUnitStyleDefault](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/unitstyle/default)Added [MKDistanceFormatterUnitStyleFull](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/unitstyle/full)Added [MKDistanceFormatterUnits](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/units)Added [MKDistanceFormatterUnitsDefault](https://developer.apple.com/documentation/mapkit/mkdistanceformatterunits/mkdistanceformatterunitsdefault)Added [MKDistanceFormatterUnitsImperial](https://developer.apple.com/documentation/mapkit/mkdistanceformatterunits/mkdistanceformatterunitsimperial)Added [MKDistanceFormatterUnitsImperialWithYards](https://developer.apple.com/documentation/mapkit/mkdistanceformatterunits/mkdistanceformatterunitsimperialwithyards)Added [MKDistanceFormatterUnitsMetric](https://developer.apple.com/documentation/mapkit/mkdistanceformatterunits/mkdistanceformatterunitsmetric)MKGeodesicPolyline.hAdded [MKGeodesicPolyline](https://developer.apple.com/documentation/mapkit/mkgeodesicpolyline)Added [+[MKGeodesicPolyline polylineWithCoordinates:count:]](https://developer.apple.com/documentation/mapkit/mkgeodesicpolyline/1452314-init)Added [+[MKGeodesicPolyline polylineWithPoints:count:]](https://developer.apple.com/documentation/mapkit/mkgeodesicpolyline/1452053-polylinewithpoints)MKMapCamera.hAdded [MKMapCamera](https://developer.apple.com/documentation/mapkit/mkmapcamera)Added [MKMapCamera.altitude](https://developer.apple.com/documentation/mapkit/mkmapcamera/1411078-altitude)Added [+[MKMapCamera camera]](https://developer.apple.com/documentation/mapkit/mkmapcamera/1411085-camera)Added [+[MKMapCamera cameraLookingAtCenterCoordinate:fromEyeCoordinate:eyeAltitude:]](https://developer.apple.com/documentation/mapkit/mkmapcamera/1411092-init)Added [MKMapCamera.centerCoordinate](https://developer.apple.com/documentation/mapkit/mkmapcamera/1411081-centercoordinate)Added [MKMapCamera.heading](https://developer.apple.com/documentation/mapkit/mkmapcamera/1411087-heading)Added [MKMapCamera.pitch](https://developer.apple.com/documentation/mapkit/mkmapcamera/1411083-pitch)MKMapSnapshot.hAdded [MKMapSnapshot](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/snapshot)Added [MKMapSnapshot.image](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/snapshot/1452701-image)Added [-[MKMapSnapshot pointForCoordinate:]](https://developer.apple.com/documentation/mapkit/mkmapsnapshot/1452523-pointforcoordinate)MKMapSnapshotOptions.hAdded [MKMapSnapshotOptions](https://developer.apple.com/documentation/mapkit/mkmapsnapshotoptions)Added [MKMapSnapshotOptions.camera](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/1452082-camera)Added [MKMapSnapshotOptions.mapRect](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/1452727-maprect)Added [MKMapSnapshotOptions.mapType](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/1452341-maptype)Added [MKMapSnapshotOptions.region](https://developer.apple.com/documentation/mapkit/mkmapsnapshotoptions/1452323-region)Added [MKMapSnapshotOptions.scale](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/1615960-scale)Added [MKMapSnapshotOptions.showsBuildings](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/1452191-showsbuildings)Added [MKMapSnapshotOptions.showsPointsOfInterest](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/1452316-showspointsofinterest)Added [MKMapSnapshotOptions.size](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/1452485-size)MKMapSnapshotter.hAdded [MKMapSnapshotter](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter)Added [-[MKMapSnapshotter cancel]](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/1452388-cancel)Added [-[MKMapSnapshotter initWithOptions:]](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/1452090-init)Added [MKMapSnapshotter.loading](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/1451960-isloading)Added [-[MKMapSnapshotter startWithCompletionHandler:]](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/1452479-start)Added [-[MKMapSnapshotter startWithQueue:completionHandler:]](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/1452419-start)Added [MKMapSnapshotCompletionHandler](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/completionhandler)MKMapView.hAdded [-[MKMapView addOverlay:level:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452635-addoverlay)Added [-[MKMapView addOverlays:level:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452518-addoverlays)Added [MKMapView.camera](https://developer.apple.com/documentation/mapkit/mkmapview/1452277-camera)Added [-[MKMapView exchangeOverlay:withOverlay:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452491-exchangeoverlay)Added [-[MKMapView insertOverlay:atIndex:level:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452723-insertoverlay)Added [-[MKMapView overlaysInLevel:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452757-overlays)Added [MKMapView.pitchEnabled](https://developer.apple.com/documentation/mapkit/mkmapview/1452265-pitchenabled)Added [-[MKMapView rendererForOverlay:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452464-renderer)Added [MKMapView.rotateEnabled](https://developer.apple.com/documentation/mapkit/mkmapview/1452274-rotateenabled)Added [-[MKMapView setCamera:animated:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452476-setcamera)Added [-[MKMapView showAnnotations:animated:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452309-showannotations)Added [MKMapView.showsBuildings](https://developer.apple.com/documentation/mapkit/mkmapview/1452483-showsbuildings)Added [MKMapView.showsPointsOfInterest](https://developer.apple.com/documentation/mapkit/mkmapview/1452102-showspointsofinterest)Added [-[MKMapViewDelegate mapView:didAddOverlayRenderers:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452609-mapview)Added [-[MKMapViewDelegate mapView:rendererForOverlay:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452203-mapview)Added [-[MKMapViewDelegate mapViewDidFinishRenderingMap:fullyRendered:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1451897-mapviewdidfinishrenderingmap)Added [-[MKMapViewDelegate mapViewWillStartRenderingMap:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1451970-mapviewwillstartrenderingmap)Added [MKOverlayLevel](https://developer.apple.com/documentation/mapkit/mkoverlaylevel)Added [MKOverlayLevelAboveLabels](https://developer.apple.com/documentation/mapkit/mkoverlaylevel/abovelabels)Added [MKOverlayLevelAboveRoads](https://developer.apple.com/documentation/mapkit/mkoverlaylevel/aboveroads)Modified [-[MKMapView viewForOverlay:]](https://developer.apple.com/documentation/mapkit/mkmapview/1616201-viewforoverlay)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[MKMapViewDelegate mapView:didAddOverlayViews:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1616206-mapview)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[MKMapViewDelegate mapView:viewForOverlay:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1616210-mapview)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

MKOverlay.hAdded [-[MKOverlay canReplaceMapContent]](https://developer.apple.com/documentation/mapkit/mkoverlay/1452399-canreplacemapcontent)MKOverlayPathRenderer.hAdded [MKOverlayPathRenderer](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer)Added [-[MKOverlayPathRenderer applyFillPropertiesToContext:atZoomScale:]](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452281-applyfillproperties)Added [-[MKOverlayPathRenderer applyStrokePropertiesToContext:atZoomScale:]](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452713-applystrokeproperties)Added [-[MKOverlayPathRenderer createPath]](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452686-createpath)Added [MKOverlayPathRenderer.fillColor](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452668-fillcolor)Added [-[MKOverlayPathRenderer fillPath:inContext:]](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452100-fillpath)Added [-[MKOverlayPathRenderer invalidatePath]](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452076-invalidatepath)Added [MKOverlayPathRenderer.lineCap](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452556-linecap)Added [MKOverlayPathRenderer.lineDashPattern](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452493-linedashpattern)Added [MKOverlayPathRenderer.lineDashPhase](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452363-linedashphase)Added [MKOverlayPathRenderer.lineJoin](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452031-linejoin)Added [MKOverlayPathRenderer.lineWidth](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452441-linewidth)Added [MKOverlayPathRenderer.miterLimit](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452395-miterlimit)Added [MKOverlayPathRenderer.path](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1451875-path)Added [MKOverlayPathRenderer.strokeColor](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452175-strokecolor)Added [-[MKOverlayPathRenderer strokePath:inContext:]](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452549-strokepath)MKOverlayPathView.hModified [-[MKOverlayPathView applyFillPropertiesToContext:atZoomScale:]](https://developer.apple.com/documentation/mapkit/mkoverlaypathview/1617207-applyfillpropertiestocontext)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[MKOverlayPathView applyStrokePropertiesToContext:atZoomScale:]](https://developer.apple.com/documentation/mapkit/mkoverlaypathview/1617205-applystrokepropertiestocontext)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[MKOverlayPathView createPath]](https://developer.apple.com/documentation/mapkit/mkoverlaypathview/1617216-createpath)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [MKOverlayPathView.fillColor](https://developer.apple.com/documentation/mapkit/mkoverlaypathview/1617215-fillcolor)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[MKOverlayPathView fillPath:inContext:]](https://developer.apple.com/documentation/mapkit/mkoverlaypathview/1617213-fillpath)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[MKOverlayPathView invalidatePath]](https://developer.apple.com/documentation/mapkit/mkoverlaypathview/1617217-invalidatepath)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [MKOverlayPathView.lineCap](https://developer.apple.com/documentation/mapkit/mkoverlaypathview/1617212-linecap)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [MKOverlayPathView.lineDashPattern](https://developer.apple.com/documentation/mapkit/mkoverlaypathview/1617210-linedashpattern)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [MKOverlayPathView.lineDashPhase](https://developer.apple.com/documentation/mapkit/mkoverlaypathview/1617211-linedashphase)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [MKOverlayPathView.lineJoin](https://developer.apple.com/documentation/mapkit/mkoverlaypathview/1617206-linejoin)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [MKOverlayPathView.lineWidth](https://developer.apple.com/documentation/mapkit/mkoverlaypathview/1617218-linewidth)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [MKOverlayPathView.miterLimit](https://developer.apple.com/documentation/mapkit/mkoverlaypathview/1617219-miterlimit)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [MKOverlayPathView.path](https://developer.apple.com/documentation/mapkit/mkoverlaypathview/1617208-path)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [MKOverlayPathView.strokeColor](https://developer.apple.com/documentation/mapkit/mkoverlaypathview/1617209-strokecolor)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[MKOverlayPathView strokePath:inContext:]](https://developer.apple.com/documentation/mapkit/mkoverlaypathview/1617214-strokepath)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

MKOverlayRenderer.hAdded [MKOverlayRenderer](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer)Added [MKOverlayRenderer.alpha](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/1452699-alpha)Added [-[MKOverlayRenderer canDrawMapRect:zoomScale:]](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/1451891-candraw)Added [MKOverlayRenderer.contentScaleFactor](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/1451931-contentscalefactor)Added [-[MKOverlayRenderer drawMapRect:zoomScale:inContext:]](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/1452184-draw)Added [-[MKOverlayRenderer initWithOverlay:]](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/1451915-init)Added [-[MKOverlayRenderer mapPointForPoint:]](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/1452670-mappoint)Added [-[MKOverlayRenderer mapRectForRect:]](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/1452680-maprectforrect)Added [MKOverlayRenderer.overlay](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/1452307-overlay)Added [-[MKOverlayRenderer pointForMapPoint:]](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/1451899-pointformappoint)Added [-[MKOverlayRenderer rectForMapRect:]](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/1452738-rectformaprect)Added [-[MKOverlayRenderer setNeedsDisplay]](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/1452104-setneedsdisplay)Added [-[MKOverlayRenderer setNeedsDisplayInMapRect:]](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/1452564-setneedsdisplay)Added [-[MKOverlayRenderer setNeedsDisplayInMapRect:zoomScale:]](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/1452793-setneedsdisplayinmaprect)Added [MKRoadWidthAtZoomScale()](https://developer.apple.com/documentation/mapkit/1452156-mkroadwidthatzoomscale)MKOverlayView.hModified [-[MKOverlayView canDrawMapRect:zoomScale:]](https://developer.apple.com/documentation/mapkit/mkoverlayview/1613864-candrawmaprect)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[MKOverlayView drawMapRect:zoomScale:inContext:]](https://developer.apple.com/documentation/mapkit/mkoverlayview/1613868-drawmaprect)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[MKOverlayView initWithOverlay:]](https://developer.apple.com/documentation/mapkit/mkoverlayview/1613884-initwithoverlay)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[MKOverlayView mapPointForPoint:]](https://developer.apple.com/documentation/mapkit/mkoverlayview/1613878-mappointforpoint)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[MKOverlayView mapRectForRect:]](https://developer.apple.com/documentation/mapkit/mkoverlayview/1613882-maprectforrect)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [MKOverlayView.overlay](https://developer.apple.com/documentation/mapkit/mkoverlayview/1613872-overlay)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[MKOverlayView pointForMapPoint:]](https://developer.apple.com/documentation/mapkit/mkoverlayview/1613874-pointformappoint)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[MKOverlayView rectForMapRect:]](https://developer.apple.com/documentation/mapkit/mkoverlayview/1613870-rectformaprect)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[MKOverlayView setNeedsDisplayInMapRect:]](https://developer.apple.com/documentation/mapkit/mkoverlayview/1613866-setneedsdisplayinmaprect)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[MKOverlayView setNeedsDisplayInMapRect:zoomScale:]](https://developer.apple.com/documentation/mapkit/mkoverlayview/1613876-setneedsdisplayinmaprect)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

MKPolygonRenderer.hAdded [MKPolygonRenderer](https://developer.apple.com/documentation/mapkit/mkpolygonrenderer)Added [-[MKPolygonRenderer initWithPolygon:]](https://developer.apple.com/documentation/mapkit/mkpolygonrenderer/1448129-init)Added [MKPolygonRenderer.polygon](https://developer.apple.com/documentation/mapkit/mkpolygonrenderer/1448132-polygon)MKPolygonView.hModified [-[MKPolygonView initWithPolygon:]](https://developer.apple.com/documentation/mapkit/mkpolygonview/1614141-initwithpolygon)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [MKPolygonView.polygon](https://developer.apple.com/documentation/mapkit/mkpolygonview/1614140-polygon)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

MKPolyline.hModified [+[MKPolyline polylineWithCoordinates:count:]](https://developer.apple.com/documentation/mapkit/mkpolyline/1452205-init)

|  | Declaration |
| --- | --- |
| From | + (MKPolyline \*)polylineWithCoordinates:(CLLocationCoordinate2D \*)coords count:(NSUInteger)count |
| To | + (instancetype)polylineWithCoordinates:(CLLocationCoordinate2D \*)coords count:(NSUInteger)count |

Modified [+[MKPolyline polylineWithPoints:count:]](https://developer.apple.com/documentation/mapkit/mkpolyline/1452773-init)

|  | Declaration |
| --- | --- |
| From | + (MKPolyline \*)polylineWithPoints:(MKMapPoint \*)points count:(NSUInteger)count |
| To | + (instancetype)polylineWithPoints:(MKMapPoint \*)points count:(NSUInteger)count |

MKPolylineRenderer.hAdded [MKPolylineRenderer](https://developer.apple.com/documentation/mapkit/mkpolylinerenderer)Added [-[MKPolylineRenderer initWithPolyline:]](https://developer.apple.com/documentation/mapkit/mkpolylinerenderer/1452074-initwithpolyline)Added [MKPolylineRenderer.polyline](https://developer.apple.com/documentation/mapkit/mkpolylinerenderer/1452465-polyline)MKPolylineView.hModified [-[MKPolylineView initWithPolyline:]](https://developer.apple.com/documentation/mapkit/mkpolylineview/1618189-initwithpolyline)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [MKPolylineView.polyline](https://developer.apple.com/documentation/mapkit/mkpolylineview/1618188-polyline)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

MKTileOverlay.hAdded [MKTileOverlay](https://developer.apple.com/documentation/mapkit/mktileoverlay)Added [-[MKTileOverlay URLForTilePath:]](https://developer.apple.com/documentation/mapkit/mktileoverlay/1452606-url)Added [MKTileOverlay.URLTemplate](https://developer.apple.com/documentation/mapkit/mktileoverlay/1452256-urltemplate)Added [MKTileOverlay.canReplaceMapContent](https://developer.apple.com/documentation/mapkit/mktileoverlay/1452604-canreplacemapcontent)Added [MKTileOverlay.geometryFlipped](https://developer.apple.com/documentation/mapkit/mktileoverlay/1452251-isgeometryflipped)Added [-[MKTileOverlay initWithURLTemplate:]](https://developer.apple.com/documentation/mapkit/mktileoverlay/1452705-init)Added [-[MKTileOverlay loadTileAtPath:result:]](https://developer.apple.com/documentation/mapkit/mktileoverlay/1452445-loadtileatpath)Added [MKTileOverlay.maximumZ](https://developer.apple.com/documentation/mapkit/mktileoverlay/1452660-maximumz)Added [MKTileOverlay.minimumZ](https://developer.apple.com/documentation/mapkit/mktileoverlay/1452199-minimumz)Added [MKTileOverlay.tileSize](https://developer.apple.com/documentation/mapkit/mktileoverlay/1452108-tilesize)Added MKTileOverlay(CustomLoading)Added [MKTileOverlayPath](https://developer.apple.com/documentation/mapkit/mktileoverlaypath)MKTileOverlayRenderer.hAdded [MKTileOverlayRenderer](https://developer.apple.com/documentation/mapkit/mktileoverlayrenderer)Added [-[MKTileOverlayRenderer initWithTileOverlay:]](https://developer.apple.com/documentation/mapkit/mktileoverlayrenderer/1452303-init)Added [-[MKTileOverlayRenderer reloadData]](https://developer.apple.com/documentation/mapkit/mktileoverlayrenderer/1452676-reloaddata)MKTypes.hRemoved MKErrorCodeAdded [MKErrorCode](https://developer.apple.com/documentation/mapkit/mkerror/code)Added [MKErrorDirectionsNotFound](https://developer.apple.com/documentation/mapkit/mkerrorcode/mkerrordirectionsnotfound)

## MediaAccessibility

MACaptionAppearance.hAdded [MACaptionAppearanceAddSelectedLanguage()](https://developer.apple.com/documentation/mediaaccessibility/1464869-macaptionappearanceaddselectedla)Added [MACaptionAppearanceBehavior](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancebehavior)Added [MACaptionAppearanceCopyBackgroundColor()](https://developer.apple.com/documentation/mediaaccessibility/1464822-macaptionappearancecopybackgroun)Added [MACaptionAppearanceCopyFontDescriptorForStyle()](https://developer.apple.com/documentation/mediaaccessibility/1464816-macaptionappearancecopyfontdescr)Added [MACaptionAppearanceCopyForegroundColor()](https://developer.apple.com/documentation/mediaaccessibility/1464828-macaptionappearancecopyforegroun)Added [MACaptionAppearanceCopyPreferredCaptioningMediaCharacteristics()](https://developer.apple.com/documentation/mediaaccessibility/1464881-macaptionappearancecopypreferred)Added [MACaptionAppearanceCopySelectedLanguages()](https://developer.apple.com/documentation/mediaaccessibility/1464855-macaptionappearancecopyselectedl)Added [MACaptionAppearanceCopyWindowColor()](https://developer.apple.com/documentation/mediaaccessibility/1464842-macaptionappearancecopywindowcol)Added [MACaptionAppearanceDisplayType](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancedisplaytype)Added [MACaptionAppearanceDomain](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancedomain)Added [MACaptionAppearanceFontStyle](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancefontstyle)Added [MACaptionAppearanceGetBackgroundOpacity()](https://developer.apple.com/documentation/mediaaccessibility/1464840-macaptionappearancegetbackground)Added [MACaptionAppearanceGetDisplayType()](https://developer.apple.com/documentation/mediaaccessibility/1464897-macaptionappearancegetdisplaytyp)Added [MACaptionAppearanceGetForegroundOpacity()](https://developer.apple.com/documentation/mediaaccessibility/1464887-macaptionappearancegetforeground)Added [MACaptionAppearanceGetRelativeCharacterSize()](https://developer.apple.com/documentation/mediaaccessibility/1464820-macaptionappearancegetrelativech)Added [MACaptionAppearanceGetTextEdgeStyle()](https://developer.apple.com/documentation/mediaaccessibility/1464824-macaptionappearancegettextedgest)Added [MACaptionAppearanceGetWindowOpacity()](https://developer.apple.com/documentation/mediaaccessibility/1464844-macaptionappearancegetwindowopac)Added [MACaptionAppearanceGetWindowRoundedCornerRadius()](https://developer.apple.com/documentation/mediaaccessibility/1464826-macaptionappearancegetwindowroun)Added [MACaptionAppearanceSetDisplayType()](https://developer.apple.com/documentation/mediaaccessibility/1464812-macaptionappearancesetdisplaytyp)Added [MACaptionAppearanceTextEdgeStyle](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancetextedgestyle)Added [MAMediaCharacteristicDescribesMusicAndSoundForAccessibility](https://developer.apple.com/documentation/mediaaccessibility/mamediacharacteristicdescribesmusicandsoundforaccessibility)Added [MAMediaCharacteristicTranscribesSpokenDialogForAccessibility](https://developer.apple.com/documentation/mediaaccessibility/mamediacharacteristictranscribesspokendialogforaccessibility)Added #def MediaAccessibility_MACaptionAppearance_hAdded [kMACaptionAppearanceBehaviorUseContentIfAvailable](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancebehavior/usecontentifavailable)Added [kMACaptionAppearanceBehaviorUseValue](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancebehavior/usevalue)Added [kMACaptionAppearanceDisplayTypeAlwaysOn](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancedisplaytype/alwayson)Added [kMACaptionAppearanceDisplayTypeAutomatic](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancedisplaytype/automatic)Added [kMACaptionAppearanceDisplayTypeForcedOnly](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancedisplaytype/kmacaptionappearancedisplaytypeforcedonly)Added [kMACaptionAppearanceDomainDefault](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancedomain/kmacaptionappearancedomaindefault)Added [kMACaptionAppearanceDomainUser](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancedomain/kmacaptionappearancedomainuser)Added [kMACaptionAppearanceFontStyleCasual](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancefontstyle/kmacaptionappearancefontstylecasual)Added [kMACaptionAppearanceFontStyleCursive](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancefontstyle/cursive)Added [kMACaptionAppearanceFontStyleDefault](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancefontstyle/default)Added [kMACaptionAppearanceFontStyleMonospacedWithSerif](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancefontstyle/kmacaptionappearancefontstylemonospacedwithserif)Added [kMACaptionAppearanceFontStyleMonospacedWithoutSerif](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancefontstyle/monospacedwithoutserif)Added [kMACaptionAppearanceFontStyleProportionalWithSerif](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancefontstyle/kmacaptionappearancefontstyleproportionalwithserif)Added [kMACaptionAppearanceFontStyleProportionalWithoutSerif](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancefontstyle/proportionalwithoutserif)Added [kMACaptionAppearanceFontStyleSmallCapital](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancefontstyle/smallcapital)Added [kMACaptionAppearanceSettingsChangedNotification](https://developer.apple.com/documentation/mediaaccessibility/kmacaptionappearancesettingschangednotification)Added [kMACaptionAppearanceTextEdgeStyleDepressed](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancetextedgestyle/depressed)Added [kMACaptionAppearanceTextEdgeStyleDropShadow](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancetextedgestyle/kmacaptionappearancetextedgestyledropshadow)Added [kMACaptionAppearanceTextEdgeStyleNone](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancetextedgestyle/kmacaptionappearancetextedgestylenone)Added [kMACaptionAppearanceTextEdgeStyleRaised](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancetextedgestyle/raised)Added [kMACaptionAppearanceTextEdgeStyleUndefined](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancetextedgestyle/kmacaptionappearancetextedgestyleundefined)Added [kMACaptionAppearanceTextEdgeStyleUniform](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancetextedgestyle/uniform)MADefinitions.hAdded #def MA_EXPORTAdded #def MA_EXTERNAdded #def MA_EXTERN_C_BEGINAdded #def MA_EXTERN_C_ENDAdded #def MA_VISIBLEAdded #def MediaAccessibility_Definitions_hMediaAccessibility.hAdded #def MediaAccessibility_MediaAccessibility_h

## MediaPlayer

MPMediaEntity.hModified [MPMediaEntity](https://developer.apple.com/documentation/mediaplayer/mpmediaentity)

|  | Protocols |
| --- | --- |
| From | NSCoding |
| To | NSSecureCoding |

MPMediaItem.hAdded [MPMediaTypeHomeVideo](https://developer.apple.com/documentation/mediaplayer/mpmediatype/mpmediatypehomevideo)MPMediaLibrary.hModified [MPMediaLibrary](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary)

|  | Protocols |
| --- | --- |
| From | NSCoding |
| To | NSSecureCoding |

MPMediaPickerController.hModified [MPMediaPickerController.delegate](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontroller/1614655-delegate)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, assign) id<MPMediaPickerControllerDelegate> delegate |
| To | @property(nonatomic, weak) id<MPMediaPickerControllerDelegate> delegate |

Modified [-[MPMediaPickerController init]](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontroller/1808935-init)

|  | Declaration |
| --- | --- |
| From | - (id)init |
| To | - (instancetype)init |

Modified [-[MPMediaPickerController initWithMediaTypes:]](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontroller/1614663-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithMediaTypes:(MPMediaType)mediaTypes |
| To | - (instancetype)initWithMediaTypes:(MPMediaType)mediaTypes |

MPMediaQuery.hModified [MPMediaPredicate](https://developer.apple.com/documentation/mediaplayer/mpmediapredicate)

|  | Protocols |
| --- | --- |
| From | NSCoding |
| To | NSSecureCoding |

Modified [MPMediaQuery](https://developer.apple.com/documentation/mediaplayer/mpmediaquery)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

Modified [MPMediaQuery.filterPredicates](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621781-filterpredicates)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, retain) NSSet \*filterPredicates |
| To | @property(nonatomic, strong) NSSet \*filterPredicates |

MPMediaQuerySection.hModified [MPMediaQuerySection](https://developer.apple.com/documentation/mediaplayer/mpmediaquerysection)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

MPMoviePlayerController.hModified [-[MPMoviePlayerController thumbnailImageAtTime:timeOption:]](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620954-thumbnailimageattime)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

MPMoviePlayerViewController.hRemoved [-[MPMoviePlayerViewController shouldAutorotateToInterfaceOrientation:]](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerviewcontroller/1809000-shouldautorotatetointerfaceorien)Added -[MPMoviePlayerViewController shouldAutorotate]Added -[MPMoviePlayerViewController supportedInterfaceOrientations]MPMusicPlayerController.hModified [MPMusicPlayerController.volume](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/1624567-volume)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

MPVolumeView.hAdded [MPVolumeView.volumeWarningSliderImage](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620066-volumewarningsliderimage)Added [MPVolumeView.wirelessRouteActive](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620071-wirelessrouteactive)Added [MPVolumeView.wirelessRoutesAvailable](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620073-arewirelessroutesavailable)Added [MPVolumeViewWirelessRouteActiveDidChangeNotification](https://developer.apple.com/documentation/mediaplayer/mpvolumeviewwirelessrouteactivedidchangenotification)Added [MPVolumeViewWirelessRoutesAvailableDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1620065-mpvolumeviewwirelessroutesavaila)

## MediaToolbox

No changes

## MessageUI

MFMessageComposeViewController.hAdded [-[MFMessageComposeViewController addAttachmentData:typeIdentifier:filename:]](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/1614069-addattachmentdata)Added [-[MFMessageComposeViewController addAttachmentURL:withAlternateFilename:]](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/1614078-addattachmenturl)Added [MFMessageComposeViewController.attachments](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/1614066-attachments)Added [+[MFMessageComposeViewController canSendAttachments]](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/1614076-cansendattachments)Added [+[MFMessageComposeViewController canSendSubject]](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/1614065-cansendsubject)Added [-[MFMessageComposeViewController disableUserAttachments]](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/1614063-disableuserattachments)Added [+[MFMessageComposeViewController isSupportedAttachmentUTI:]](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/1614075-issupportedattachmentuti)Added [MFMessageComposeViewController.subject](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/1614062-subject)Added [MFMessageComposeViewControllerAttachmentAlternateFilename](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontrollerattachmentalternatefilename)Added [MFMessageComposeViewControllerAttachmentURL](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontrollerattachmenturl)

## MobileCoreServices

No changes

## MultipeerConnectivity

MCAdvertiserAssistant.hAdded [MCAdvertiserAssistant](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant)Added [MCAdvertiserAssistant.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1407041-delegate)Added [MCAdvertiserAssistant.discoveryInfo](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1406952-discoveryinfo)Added [-[MCAdvertiserAssistant initWithServiceType:discoveryInfo:session:]](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1406990-init)Added [MCAdvertiserAssistant.serviceType](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1407062-servicetype)Added [MCAdvertiserAssistant.session](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1406924-session)Added [-[MCAdvertiserAssistant start]](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1407085-start)Added [-[MCAdvertiserAssistant stop]](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1406986-stop)Added [MCAdvertiserAssistantDelegate](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistantdelegate)Added [-[MCAdvertiserAssistantDelegate advertiserAssistantDidDismissInvitation:]](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistantdelegate/1406922-advertiserassistantdiddismissinv)Added [-[MCAdvertiserAssistantDelegate advertiserAssitantWillPresentInvitation:]](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistantdelegate/1809093-advertiserassitantwillpresentinv)MCBrowserViewController.hAdded [MCBrowserViewController](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller)Added [MCBrowserViewController.browser](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1406969-browser)Added [MCBrowserViewController.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1406982-delegate)Added [-[MCBrowserViewController initWithBrowser:session:]](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1406963-init)Added [-[MCBrowserViewController initWithServiceType:session:]](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1406915-init)Added [MCBrowserViewController.maximumNumberOfPeers](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1406954-maximumnumberofpeers)Added [MCBrowserViewController.minimumNumberOfPeers](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1407043-minimumnumberofpeers)Added [MCBrowserViewController.session](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1406976-session)Added [MCBrowserViewControllerDelegate](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontrollerdelegate)Added [-[MCBrowserViewControllerDelegate browserViewController:shouldPresentNearbyPeer:withDiscoveryInfo:]](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontrollerdelegate/1407039-browserviewcontroller)Added [-[MCBrowserViewControllerDelegate browserViewControllerDidFinish:]](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontrollerdelegate/1407002-browserviewcontrollerdidfinish)Added [-[MCBrowserViewControllerDelegate browserViewControllerWasCancelled:]](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontrollerdelegate/1406942-browserviewcontrollerwascancelle)MCError.hAdded [MCErrorCancelled](https://developer.apple.com/documentation/multipeerconnectivity/mcerrorcode/mcerrorcancelled)Added [MCErrorCode](https://developer.apple.com/documentation/multipeerconnectivity/mcerrorcode)Added [MCErrorDomain](https://developer.apple.com/documentation/multipeerconnectivity/mcerrordomain)Added [MCErrorInvalidParameter](https://developer.apple.com/documentation/multipeerconnectivity/mcerror/code/invalidparameter)Added [MCErrorNotConnected](https://developer.apple.com/documentation/multipeerconnectivity/mcerrorcode/mcerrornotconnected)Added [MCErrorTimedOut](https://developer.apple.com/documentation/multipeerconnectivity/mcerrorcode/mcerrortimedout)Added [MCErrorUnavailable](https://developer.apple.com/documentation/multipeerconnectivity/mcerrorcode/mcerrorunavailable)Added [MCErrorUnknown](https://developer.apple.com/documentation/multipeerconnectivity/mcerrorcode/mcerrorunknown)Added [MCErrorUnsupported](https://developer.apple.com/documentation/multipeerconnectivity/mcerrorcode/mcerrorunsupported)Added #def MC_EXTERNAdded #def MC_EXTERN_CLASSAdded #def MC_EXTERN_WEAKMCNearbyServiceAdvertiser.hAdded [MCNearbyServiceAdvertiser](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser)Added [MCNearbyServiceAdvertiser.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1407031-delegate)Added [MCNearbyServiceAdvertiser.discoveryInfo](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1406967-discoveryinfo)Added [-[MCNearbyServiceAdvertiser initWithPeer:discoveryInfo:serviceType:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1407102-initwithpeer)Added [MCNearbyServiceAdvertiser.myPeerID](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1407022-mypeerid)Added [MCNearbyServiceAdvertiser.serviceType](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1407108-servicetype)Added [-[MCNearbyServiceAdvertiser startAdvertisingPeer]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1407006-startadvertisingpeer)Added [-[MCNearbyServiceAdvertiser stopAdvertisingPeer]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1407010-stopadvertisingpeer)Added [MCNearbyServiceAdvertiserDelegate](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiserdelegate)Added [-[MCNearbyServiceAdvertiserDelegate advertiser:didNotStartAdvertisingPeer:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiserdelegate/1407100-advertiser)Added [-[MCNearbyServiceAdvertiserDelegate advertiser:didReceiveInvitationFromPeer:withContext:invitationHandler:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiserdelegate/1406971-advertiser)MCNearbyServiceBrowser.hAdded [MCNearbyServiceBrowser](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser)Added [MCNearbyServiceBrowser.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/1407079-delegate)Added [-[MCNearbyServiceBrowser initWithPeer:serviceType:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/1407094-init)Added [-[MCNearbyServiceBrowser invitePeer:toSession:withContext:timeout:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/1406944-invitepeer)Added [MCNearbyServiceBrowser.myPeerID](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/1407050-mypeerid)Added [MCNearbyServiceBrowser.serviceType](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/1407110-servicetype)Added [-[MCNearbyServiceBrowser startBrowsingForPeers]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/1406956-startbrowsingforpeers)Added [-[MCNearbyServiceBrowser stopBrowsingForPeers]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/1407033-stopbrowsingforpeers)Added [MCNearbyServiceBrowserDelegate](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate)Added [-[MCNearbyServiceBrowserDelegate browser:didNotStartBrowsingForPeers:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate/1406913-browser)Added [-[MCNearbyServiceBrowserDelegate browser:foundPeer:withDiscoveryInfo:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate/1406926-browser)Added [-[MCNearbyServiceBrowserDelegate browser:lostPeer:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate/1407014-browser)MCPeerID.hAdded [MCPeerID](https://developer.apple.com/documentation/multipeerconnectivity/mcpeerid)Added [MCPeerID.displayName](https://developer.apple.com/documentation/multipeerconnectivity/mcpeerid/1407077-displayname)Added [-[MCPeerID initWithDisplayName:]](https://developer.apple.com/documentation/multipeerconnectivity/mcpeerid/1407089-init)MCSession.hAdded [MCSession](https://developer.apple.com/documentation/multipeerconnectivity/mcsession)Added [-[MCSession cancelConnectPeer:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407106-cancelconnectpeer)Added [-[MCSession connectPeer:withNearbyConnectionData:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407054-connectpeer)Added [MCSession.connectedPeers](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1406911-connectedpeers)Added [MCSession.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407112-delegate)Added [-[MCSession disconnect]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407004-disconnect)Added [MCSession.encryptionPreference](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407081-encryptionpreference)Added [-[MCSession initWithPeer:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407000-initwithpeer)Added [-[MCSession initWithPeer:securityIdentity:encryptionPreference:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407025-init)Added [MCSession.myPeerID](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1406992-mypeerid)Added [-[MCSession nearbyConnectionDataForPeer:withCompletionHandler:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407060-nearbyconnectiondata)Added [MCSession.securityIdentity](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1406980-securityidentity)Added [-[MCSession sendData:toPeers:withMode:error:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1406997-send)Added [-[MCSession sendResourceAtURL:withName:toPeer:withCompletionHandler:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407056-sendresourceaturl)Added [-[MCSession startStreamWithName:toPeer:error:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407071-startstream)Added [MCSessionDelegate](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate)Added [-[MCSessionDelegate session:didFinishReceivingResourceWithName:fromPeer:atURL:withError:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/1406984-session)Added [-[MCSessionDelegate session:didReceiveCertificate:fromPeer:certificateHandler:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/1407067-session)Added [-[MCSessionDelegate session:didReceiveData:fromPeer:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/1406934-session)Added [-[MCSessionDelegate session:didReceiveStream:withName:fromPeer:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/1406917-session)Added [-[MCSessionDelegate session:didStartReceivingResourceWithName:fromPeer:withProgress:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/1406965-session)Added [-[MCSessionDelegate session:peer:didChangeState:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/1406958-session)Added [MCEncryptionNone](https://developer.apple.com/documentation/multipeerconnectivity/mcencryptionpreference/mcencryptionnone)Added [MCEncryptionOptional](https://developer.apple.com/documentation/multipeerconnectivity/mcencryptionpreference/mcencryptionoptional)Added [MCEncryptionPreference](https://developer.apple.com/documentation/multipeerconnectivity/mcencryptionpreference)Added [MCEncryptionRequired](https://developer.apple.com/documentation/multipeerconnectivity/mcencryptionpreference/mcencryptionrequired)Added MCSession(MCSessionCustomDiscovery)Added [MCSessionSendDataMode](https://developer.apple.com/documentation/multipeerconnectivity/mcsessionsenddatamode)Added [MCSessionSendDataReliable](https://developer.apple.com/documentation/multipeerconnectivity/mcsessionsenddatamode/mcsessionsenddatareliable)Added [MCSessionSendDataUnreliable](https://developer.apple.com/documentation/multipeerconnectivity/mcsessionsenddatamode/mcsessionsenddataunreliable)Added [MCSessionState](https://developer.apple.com/documentation/multipeerconnectivity/mcsessionstate)Added [MCSessionStateConnected](https://developer.apple.com/documentation/multipeerconnectivity/mcsessionstate/mcsessionstateconnected)Added [MCSessionStateConnecting](https://developer.apple.com/documentation/multipeerconnectivity/mcsessionstate/mcsessionstateconnecting)Added [MCSessionStateNotConnected](https://developer.apple.com/documentation/multipeerconnectivity/mcsessionstate/mcsessionstatenotconnected)Added [kMCSessionMaximumNumberOfPeers](https://developer.apple.com/documentation/multipeerconnectivity/kmcsessionmaximumnumberofpeers)Added [kMCSessionMinimumNumberOfPeers](https://developer.apple.com/documentation/multipeerconnectivity/kmcsessionminimumnumberofpeers)MultipeerConnectivity.h

## NewsstandKit

No changes

## OpenAL

oalMacOSX_OALExtensions.hAdded #def ALC_MAC_OSX_RENDER_CHANNEL_COUNT_MULTICHANNELAdded alSourceGetRenderingQualityProcPtrAdded alSourceRenderingQualityProcPtrAdded alcOutputCapturerAvailableSamplesProcPtrAdded alcOutputCapturerPrepareProcPtrAdded alcOutputCapturerSamplesProcPtrAdded alcOutputCapturerStartProcPtrAdded alcOutputCapturerStopProcPtr

## OpenGLES

EAGL.hAdded [kEAGLRenderingAPIOpenGLES3](https://developer.apple.com/documentation/opengles/eaglrenderingapi/keaglrenderingapiopengles3)EAGLDrawable.hAdded [kEAGLColorFormatSRGBA8](https://developer.apple.com/documentation/opengles/keaglcolorformatsrgba8)gl.hRemoved #def GL_STENCIL_INDEXModified [glBlendColor()](https://developer.apple.com/documentation/opengles/1617234-glblendcolor)

|  | Declaration |
| --- | --- |
| From | void glBlendColor ( GLclampf red, GLclampf green, GLclampf blue, GLclampf alpha); |
| To | void glBlendColor ( GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha); |

Modified [glClearColor()](https://developer.apple.com/documentation/opengles/1617582-glclearcolor)

|  | Declaration |
| --- | --- |
| From | void glClearColor ( GLclampf red, GLclampf green, GLclampf blue, GLclampf alpha); |
| To | void glClearColor ( GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha); |

Modified [glShaderSource()](https://developer.apple.com/documentation/opengles/1617674-glshadersource)

|  | Declaration |
| --- | --- |
| From | void glShaderSource ( GLuint shader, GLsizei count, const GLchar \*\*string, const GLint \*length); |
| To | void glShaderSource ( GLuint shader, GLsizei count, const GLchar \*const \*string, const GLint \*length); |

gl.hAdded [#def GL_ACTIVE_ATTRIBUTES](https://developer.apple.com/documentation/opengles/gl_active_attributes)Added [#def GL_ACTIVE_ATTRIBUTE_MAX_LENGTH](https://developer.apple.com/documentation/opengles/gl_active_attribute_max_length)Added [#def GL_ACTIVE_TEXTURE](https://developer.apple.com/documentation/opengles/gl_active_texture)Added [#def GL_ACTIVE_UNIFORMS](https://developer.apple.com/documentation/opengles/gl_active_uniforms)Added #def GL_ACTIVE_UNIFORM_BLOCKSAdded #def GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTHAdded [#def GL_ACTIVE_UNIFORM_MAX_LENGTH](https://developer.apple.com/documentation/opengles/gl_active_uniform_max_length)Added [#def GL_ALIASED_LINE_WIDTH_RANGE](https://developer.apple.com/documentation/opengles/gl_aliased_line_width_range)Added [#def GL_ALIASED_POINT_SIZE_RANGE](https://developer.apple.com/documentation/opengles/gl_aliased_point_size_range)Added [#def GL_ALPHA](https://developer.apple.com/documentation/opengles/gl_alpha)Added [#def GL_ALPHA_BITS](https://developer.apple.com/documentation/opengles/gl_alpha_bits)Added #def GL_ALREADY_SIGNALEDAdded [#def GL_ALWAYS](https://developer.apple.com/documentation/opengles/gl_always)Added #def GL_ANY_SAMPLES_PASSEDAdded [#def GL_ANY_SAMPLES_PASSED_CONSERVATIVE](https://developer.apple.com/documentation/opengles/gl_any_samples_passed_conservative)Added #def GL_APIAdded #def GL_APIENTRYAdded [#def GL_ARRAY_BUFFER](https://developer.apple.com/documentation/opengles/gl_array_buffer)Added [#def GL_ARRAY_BUFFER_BINDING](https://developer.apple.com/documentation/opengles/gl_array_buffer_binding)Added [#def GL_ATTACHED_SHADERS](https://developer.apple.com/documentation/opengles/gl_attached_shaders)Added [#def GL_BACK](https://developer.apple.com/documentation/opengles/gl_back)Added [#def GL_BLEND](https://developer.apple.com/documentation/opengles/gl_blend)Added [#def GL_BLEND_COLOR](https://developer.apple.com/documentation/opengles/gl_blend_color)Added [#def GL_BLEND_DST_ALPHA](https://developer.apple.com/documentation/opengles/gl_blend_dst_alpha)Added [#def GL_BLEND_DST_RGB](https://developer.apple.com/documentation/opengles/gl_blend_dst_rgb)Added [#def GL_BLEND_EQUATION](https://developer.apple.com/documentation/opengles/gl_blend_equation)Added [#def GL_BLEND_EQUATION_ALPHA](https://developer.apple.com/documentation/opengles/gl_blend_equation_alpha)Added [#def GL_BLEND_EQUATION_RGB](https://developer.apple.com/documentation/opengles/gl_blend_equation_rgb)Added [#def GL_BLEND_SRC_ALPHA](https://developer.apple.com/documentation/opengles/gl_blend_src_alpha)Added [#def GL_BLEND_SRC_RGB](https://developer.apple.com/documentation/opengles/gl_blend_src_rgb)Added #def GL_BLUEAdded [#def GL_BLUE_BITS](https://developer.apple.com/documentation/opengles/gl_blue_bits)Added [#def GL_BOOL](https://developer.apple.com/documentation/opengles/gl_bool)Added [#def GL_BOOL_VEC2](https://developer.apple.com/documentation/opengles/gl_bool_vec2)Added [#def GL_BOOL_VEC3](https://developer.apple.com/documentation/opengles/gl_bool_vec3)Added [#def GL_BOOL_VEC4](https://developer.apple.com/documentation/opengles/gl_bool_vec4)Added #def GL_BUFFER_ACCESS_FLAGSAdded #def GL_BUFFER_MAPPEDAdded #def GL_BUFFER_MAP_LENGTHAdded #def GL_BUFFER_MAP_OFFSETAdded #def GL_BUFFER_MAP_POINTERAdded [#def GL_BUFFER_SIZE](https://developer.apple.com/documentation/opengles/gl_buffer_size)Added [#def GL_BUFFER_USAGE](https://developer.apple.com/documentation/opengles/gl_buffer_usage)Added [#def GL_BYTE](https://developer.apple.com/documentation/opengles/gl_byte)Added [#def GL_CCW](https://developer.apple.com/documentation/opengles/gl_ccw)Added [#def GL_CLAMP_TO_EDGE](https://developer.apple.com/documentation/opengles/gl_clamp_to_edge)Added #def GL_COLORAdded [#def GL_COLOR_ATTACHMENT0](https://developer.apple.com/documentation/opengles/gl_color_attachment0)Added #def GL_COLOR_ATTACHMENT1Added #def GL_COLOR_ATTACHMENT10Added #def GL_COLOR_ATTACHMENT11Added #def GL_COLOR_ATTACHMENT12Added #def GL_COLOR_ATTACHMENT13Added #def GL_COLOR_ATTACHMENT14Added #def GL_COLOR_ATTACHMENT15Added #def GL_COLOR_ATTACHMENT2Added #def GL_COLOR_ATTACHMENT3Added #def GL_COLOR_ATTACHMENT4Added #def GL_COLOR_ATTACHMENT5Added #def GL_COLOR_ATTACHMENT6Added #def GL_COLOR_ATTACHMENT7Added #def GL_COLOR_ATTACHMENT8Added #def GL_COLOR_ATTACHMENT9Added [#def GL_COLOR_BUFFER_BIT](https://developer.apple.com/documentation/opengles/gl_color_buffer_bit)Added [#def GL_COLOR_CLEAR_VALUE](https://developer.apple.com/documentation/opengles/gl_color_clear_value)Added [#def GL_COLOR_WRITEMASK](https://developer.apple.com/documentation/opengles/gl_color_writemask)Added #def GL_COMPARE_REF_TO_TEXTUREAdded [#def GL_COMPILE_STATUS](https://developer.apple.com/documentation/opengles/gl_compile_status)Added [#def GL_COMPRESSED_R11_EAC](https://developer.apple.com/documentation/opengles/gl_compressed_r11_eac)Added [#def GL_COMPRESSED_RG11_EAC](https://developer.apple.com/documentation/opengles/gl_compressed_rg11_eac)Added [#def GL_COMPRESSED_RGB8_ETC2](https://developer.apple.com/documentation/opengles/gl_compressed_rgb8_etc2)Added [#def GL_COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2](https://developer.apple.com/documentation/opengles/gl_compressed_rgb8_punchthrough_alpha1_etc2)Added [#def GL_COMPRESSED_RGBA8_ETC2_EAC](https://developer.apple.com/documentation/opengles/gl_compressed_rgba8_etc2_eac)Added [#def GL_COMPRESSED_SIGNED_R11_EAC](https://developer.apple.com/documentation/opengles/gl_compressed_signed_r11_eac)Added [#def GL_COMPRESSED_SIGNED_RG11_EAC](https://developer.apple.com/documentation/opengles/gl_compressed_signed_rg11_eac)Added [#def GL_COMPRESSED_SRGB8_ALPHA8_ETC2_EAC](https://developer.apple.com/documentation/opengles/gl_compressed_srgb8_alpha8_etc2_eac)Added [#def GL_COMPRESSED_SRGB8_ETC2](https://developer.apple.com/documentation/opengles/gl_compressed_srgb8_etc2)Added [#def GL_COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2](https://developer.apple.com/documentation/opengles/gl_compressed_srgb8_punchthrough_alpha1_etc2)Added [#def GL_COMPRESSED_TEXTURE_FORMATS](https://developer.apple.com/documentation/opengles/gl_compressed_texture_formats)Added #def GL_CONDITION_SATISFIEDAdded [#def GL_CONSTANT_ALPHA](https://developer.apple.com/documentation/opengles/gl_constant_alpha)Added [#def GL_CONSTANT_COLOR](https://developer.apple.com/documentation/opengles/gl_constant_color)Added #def GL_COPY_READ_BUFFERAdded [#def GL_COPY_READ_BUFFER_BINDING](https://developer.apple.com/documentation/opengles/gl_copy_read_buffer_binding)Added #def GL_COPY_WRITE_BUFFERAdded [#def GL_COPY_WRITE_BUFFER_BINDING](https://developer.apple.com/documentation/opengles/gl_copy_write_buffer_binding)Added [#def GL_CULL_FACE](https://developer.apple.com/documentation/opengles/gl_cull_face)Added [#def GL_CULL_FACE_MODE](https://developer.apple.com/documentation/opengles/gl_cull_face_mode)Added [#def GL_CURRENT_PROGRAM](https://developer.apple.com/documentation/opengles/gl_current_program)Added #def GL_CURRENT_QUERYAdded [#def GL_CURRENT_VERTEX_ATTRIB](https://developer.apple.com/documentation/opengles/gl_current_vertex_attrib)Added [#def GL_CW](https://developer.apple.com/documentation/opengles/gl_cw)Added [#def GL_DECR](https://developer.apple.com/documentation/opengles/gl_decr)Added [#def GL_DECR_WRAP](https://developer.apple.com/documentation/opengles/gl_decr_wrap)Added [#def GL_DELETE_STATUS](https://developer.apple.com/documentation/opengles/gl_delete_status)Added #def GL_DEPTHAdded #def GL_DEPTH24_STENCIL8Added #def GL_DEPTH32F_STENCIL8Added [#def GL_DEPTH_ATTACHMENT](https://developer.apple.com/documentation/opengles/gl_depth_attachment)Added [#def GL_DEPTH_BITS](https://developer.apple.com/documentation/opengles/gl_depth_bits)Added [#def GL_DEPTH_BUFFER_BIT](https://developer.apple.com/documentation/opengles/gl_depth_buffer_bit)Added [#def GL_DEPTH_CLEAR_VALUE](https://developer.apple.com/documentation/opengles/gl_depth_clear_value)Added [#def GL_DEPTH_COMPONENT](https://developer.apple.com/documentation/opengles/gl_depth_component)Added [#def GL_DEPTH_COMPONENT16](https://developer.apple.com/documentation/opengles/gl_depth_component16)Added #def GL_DEPTH_COMPONENT24Added #def GL_DEPTH_COMPONENT32FAdded [#def GL_DEPTH_FUNC](https://developer.apple.com/documentation/opengles/gl_depth_func)Added [#def GL_DEPTH_RANGE](https://developer.apple.com/documentation/opengles/gl_depth_range)Added #def GL_DEPTH_STENCILAdded #def GL_DEPTH_STENCIL_ATTACHMENTAdded [#def GL_DEPTH_TEST](https://developer.apple.com/documentation/opengles/gl_depth_test)Added [#def GL_DEPTH_WRITEMASK](https://developer.apple.com/documentation/opengles/gl_depth_writemask)Added [#def GL_DITHER](https://developer.apple.com/documentation/opengles/gl_dither)Added [#def GL_DONT_CARE](https://developer.apple.com/documentation/opengles/gl_dont_care)Added #def GL_DRAW_BUFFER0Added #def GL_DRAW_BUFFER1Added #def GL_DRAW_BUFFER10Added #def GL_DRAW_BUFFER11Added #def GL_DRAW_BUFFER12Added #def GL_DRAW_BUFFER13Added #def GL_DRAW_BUFFER14Added #def GL_DRAW_BUFFER15Added #def GL_DRAW_BUFFER2Added #def GL_DRAW_BUFFER3Added #def GL_DRAW_BUFFER4Added #def GL_DRAW_BUFFER5Added #def GL_DRAW_BUFFER6Added #def GL_DRAW_BUFFER7Added #def GL_DRAW_BUFFER8Added #def GL_DRAW_BUFFER9Added #def GL_DRAW_FRAMEBUFFERAdded #def GL_DRAW_FRAMEBUFFER_BINDINGAdded [#def GL_DST_ALPHA](https://developer.apple.com/documentation/opengles/gl_dst_alpha)Added [#def GL_DST_COLOR](https://developer.apple.com/documentation/opengles/gl_dst_color)Added #def GL_DYNAMIC_COPYAdded [#def GL_DYNAMIC_DRAW](https://developer.apple.com/documentation/opengles/gl_dynamic_draw)Added #def GL_DYNAMIC_READAdded [#def GL_ELEMENT_ARRAY_BUFFER](https://developer.apple.com/documentation/opengles/gl_element_array_buffer)Added [#def GL_ELEMENT_ARRAY_BUFFER_BINDING](https://developer.apple.com/documentation/opengles/gl_element_array_buffer_binding)Added [#def GL_EQUAL](https://developer.apple.com/documentation/opengles/gl_equal)Added [#def GL_ES_VERSION_2_0](https://developer.apple.com/documentation/opengles/gl_es_version_2_0)Added [#def GL_ES_VERSION_3_0](https://developer.apple.com/documentation/opengles/gl_es_version_3_0)Added [#def GL_EXTENSIONS](https://developer.apple.com/documentation/opengles/gl_extensions)Added [#def GL_FALSE](https://developer.apple.com/documentation/opengles/gl_false)Added [#def GL_FASTEST](https://developer.apple.com/documentation/opengles/gl_fastest)Added [#def GL_FIXED](https://developer.apple.com/documentation/opengles/gl_fixed)Added [#def GL_FLOAT](https://developer.apple.com/documentation/opengles/gl_float)Added #def GL_FLOAT_32_UNSIGNED_INT_24_8_REVAdded [#def GL_FLOAT_MAT2](https://developer.apple.com/documentation/opengles/gl_float_mat2)Added #def GL_FLOAT_MAT2x3Added #def GL_FLOAT_MAT2x4Added [#def GL_FLOAT_MAT3](https://developer.apple.com/documentation/opengles/gl_float_mat3)Added #def GL_FLOAT_MAT3x2Added #def GL_FLOAT_MAT3x4Added [#def GL_FLOAT_MAT4](https://developer.apple.com/documentation/opengles/gl_float_mat4)Added #def GL_FLOAT_MAT4x2Added #def GL_FLOAT_MAT4x3Added [#def GL_FLOAT_VEC2](https://developer.apple.com/documentation/opengles/gl_float_vec2)Added [#def GL_FLOAT_VEC3](https://developer.apple.com/documentation/opengles/gl_float_vec3)Added [#def GL_FLOAT_VEC4](https://developer.apple.com/documentation/opengles/gl_float_vec4)Added [#def GL_FRAGMENT_SHADER](https://developer.apple.com/documentation/opengles/gl_fragment_shader)Added #def GL_FRAGMENT_SHADER_DERIVATIVE_HINTAdded [#def GL_FRAMEBUFFER](https://developer.apple.com/documentation/opengles/gl_framebuffer)Added #def GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZEAdded #def GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZEAdded #def GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODINGAdded #def GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPEAdded #def GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZEAdded #def GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZEAdded [#def GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME](https://developer.apple.com/documentation/opengles/gl_framebuffer_attachment_object_name)Added [#def GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE](https://developer.apple.com/documentation/opengles/gl_framebuffer_attachment_object_type)Added #def GL_FRAMEBUFFER_ATTACHMENT_RED_SIZEAdded #def GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZEAdded [#def GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE](https://developer.apple.com/documentation/opengles/gl_framebuffer_attachment_texture_cube_map_face)Added #def GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYERAdded [#def GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL](https://developer.apple.com/documentation/opengles/gl_framebuffer_attachment_texture_level)Added [#def GL_FRAMEBUFFER_BINDING](https://developer.apple.com/documentation/opengles/gl_framebuffer_binding)Added [#def GL_FRAMEBUFFER_COMPLETE](https://developer.apple.com/documentation/opengles/gl_framebuffer_complete)Added #def GL_FRAMEBUFFER_DEFAULTAdded [#def GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT](https://developer.apple.com/documentation/opengles/gl_framebuffer_incomplete_attachment)Added [#def GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS](https://developer.apple.com/documentation/opengles/gl_framebuffer_incomplete_dimensions)Added [#def GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT](https://developer.apple.com/documentation/opengles/gl_framebuffer_incomplete_missing_attachment)Added #def GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLEAdded #def GL_FRAMEBUFFER_UNDEFINEDAdded [#def GL_FRAMEBUFFER_UNSUPPORTED](https://developer.apple.com/documentation/opengles/gl_framebuffer_unsupported)Added [#def GL_FRONT](https://developer.apple.com/documentation/opengles/gl_front)Added [#def GL_FRONT_AND_BACK](https://developer.apple.com/documentation/opengles/gl_front_and_back)Added [#def GL_FRONT_FACE](https://developer.apple.com/documentation/opengles/gl_front_face)Added [#def GL_FUNC_ADD](https://developer.apple.com/documentation/opengles/gl_func_add)Added [#def GL_FUNC_REVERSE_SUBTRACT](https://developer.apple.com/documentation/opengles/gl_func_reverse_subtract)Added [#def GL_FUNC_SUBTRACT](https://developer.apple.com/documentation/opengles/gl_func_subtract)Added [#def GL_GENERATE_MIPMAP_HINT](https://developer.apple.com/documentation/opengles/gl_generate_mipmap_hint)Added [#def GL_GEQUAL](https://developer.apple.com/documentation/opengles/gl_gequal)Added [#def GL_GREATER](https://developer.apple.com/documentation/opengles/gl_greater)Added #def GL_GREENAdded [#def GL_GREEN_BITS](https://developer.apple.com/documentation/opengles/gl_green_bits)Added #def GL_HALF_FLOATAdded [#def GL_HIGH_FLOAT](https://developer.apple.com/documentation/opengles/gl_high_float)Added [#def GL_HIGH_INT](https://developer.apple.com/documentation/opengles/gl_high_int)Added [#def GL_IMPLEMENTATION_COLOR_READ_FORMAT](https://developer.apple.com/documentation/opengles/gl_implementation_color_read_format)Added [#def GL_IMPLEMENTATION_COLOR_READ_TYPE](https://developer.apple.com/documentation/opengles/gl_implementation_color_read_type)Added [#def GL_INCR](https://developer.apple.com/documentation/opengles/gl_incr)Added [#def GL_INCR_WRAP](https://developer.apple.com/documentation/opengles/gl_incr_wrap)Added [#def GL_INFO_LOG_LENGTH](https://developer.apple.com/documentation/opengles/gl_info_log_length)Added [#def GL_INT](https://developer.apple.com/documentation/opengles/gl_int)Added #def GL_INTERLEAVED_ATTRIBSAdded #def GL_INT_2_10_10_10_REVAdded #def GL_INT_SAMPLER_2DAdded #def GL_INT_SAMPLER_2D_ARRAYAdded #def GL_INT_SAMPLER_3DAdded #def GL_INT_SAMPLER_CUBEAdded [#def GL_INT_VEC2](https://developer.apple.com/documentation/opengles/gl_int_vec2)Added [#def GL_INT_VEC3](https://developer.apple.com/documentation/opengles/gl_int_vec3)Added [#def GL_INT_VEC4](https://developer.apple.com/documentation/opengles/gl_int_vec4)Added [#def GL_INVALID_ENUM](https://developer.apple.com/documentation/opengles/gl_invalid_enum)Added [#def GL_INVALID_FRAMEBUFFER_OPERATION](https://developer.apple.com/documentation/opengles/gl_invalid_framebuffer_operation)Added #def GL_INVALID_INDEXAdded [#def GL_INVALID_OPERATION](https://developer.apple.com/documentation/opengles/gl_invalid_operation)Added [#def GL_INVALID_VALUE](https://developer.apple.com/documentation/opengles/gl_invalid_value)Added [#def GL_INVERT](https://developer.apple.com/documentation/opengles/gl_invert)Added [#def GL_KEEP](https://developer.apple.com/documentation/opengles/gl_keep)Added [#def GL_LEQUAL](https://developer.apple.com/documentation/opengles/gl_lequal)Added [#def GL_LESS](https://developer.apple.com/documentation/opengles/gl_less)Added [#def GL_LINEAR](https://developer.apple.com/documentation/opengles/gl_linear)Added [#def GL_LINEAR_MIPMAP_LINEAR](https://developer.apple.com/documentation/opengles/gl_linear_mipmap_linear)Added [#def GL_LINEAR_MIPMAP_NEAREST](https://developer.apple.com/documentation/opengles/gl_linear_mipmap_nearest)Added [#def GL_LINES](https://developer.apple.com/documentation/opengles/gl_lines)Added [#def GL_LINE_LOOP](https://developer.apple.com/documentation/opengles/gl_line_loop)Added [#def GL_LINE_STRIP](https://developer.apple.com/documentation/opengles/gl_line_strip)Added [#def GL_LINE_WIDTH](https://developer.apple.com/documentation/opengles/gl_line_width)Added [#def GL_LINK_STATUS](https://developer.apple.com/documentation/opengles/gl_link_status)Added [#def GL_LOW_FLOAT](https://developer.apple.com/documentation/opengles/gl_low_float)Added [#def GL_LOW_INT](https://developer.apple.com/documentation/opengles/gl_low_int)Added [#def GL_LUMINANCE](https://developer.apple.com/documentation/opengles/gl_luminance)Added [#def GL_LUMINANCE_ALPHA](https://developer.apple.com/documentation/opengles/gl_luminance_alpha)Added #def GL_MAJOR_VERSIONAdded #def GL_MAP_FLUSH_EXPLICIT_BITAdded #def GL_MAP_INVALIDATE_BUFFER_BITAdded #def GL_MAP_INVALIDATE_RANGE_BITAdded #def GL_MAP_READ_BITAdded #def GL_MAP_UNSYNCHRONIZED_BITAdded #def GL_MAP_WRITE_BITAdded #def GL_MAXAdded #def GL_MAX_3D_TEXTURE_SIZEAdded #def GL_MAX_ARRAY_TEXTURE_LAYERSAdded #def GL_MAX_COLOR_ATTACHMENTSAdded #def GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTSAdded [#def GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS](https://developer.apple.com/documentation/opengles/gl_max_combined_texture_image_units)Added #def GL_MAX_COMBINED_UNIFORM_BLOCKSAdded #def GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTSAdded [#def GL_MAX_CUBE_MAP_TEXTURE_SIZE](https://developer.apple.com/documentation/opengles/gl_max_cube_map_texture_size)Added #def GL_MAX_DRAW_BUFFERSAdded #def GL_MAX_ELEMENTS_INDICESAdded #def GL_MAX_ELEMENTS_VERTICESAdded [#def GL_MAX_ELEMENT_INDEX](https://developer.apple.com/documentation/opengles/gl_max_element_index)Added #def GL_MAX_FRAGMENT_INPUT_COMPONENTSAdded #def GL_MAX_FRAGMENT_UNIFORM_BLOCKSAdded #def GL_MAX_FRAGMENT_UNIFORM_COMPONENTSAdded [#def GL_MAX_FRAGMENT_UNIFORM_VECTORS](https://developer.apple.com/documentation/opengles/gl_max_fragment_uniform_vectors)Added #def GL_MAX_PROGRAM_TEXEL_OFFSETAdded [#def GL_MAX_RENDERBUFFER_SIZE](https://developer.apple.com/documentation/opengles/gl_max_renderbuffer_size)Added #def GL_MAX_SAMPLESAdded #def GL_MAX_SERVER_WAIT_TIMEOUTAdded [#def GL_MAX_TEXTURE_IMAGE_UNITS](https://developer.apple.com/documentation/opengles/gl_max_texture_image_units)Added #def GL_MAX_TEXTURE_LOD_BIASAdded [#def GL_MAX_TEXTURE_SIZE](https://developer.apple.com/documentation/opengles/gl_max_texture_size)Added #def GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTSAdded #def GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBSAdded #def GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTSAdded #def GL_MAX_UNIFORM_BLOCK_SIZEAdded #def GL_MAX_UNIFORM_BUFFER_BINDINGSAdded #def GL_MAX_VARYING_COMPONENTSAdded [#def GL_MAX_VARYING_VECTORS](https://developer.apple.com/documentation/opengles/gl_max_varying_vectors)Added [#def GL_MAX_VERTEX_ATTRIBS](https://developer.apple.com/documentation/opengles/gl_max_vertex_attribs)Added #def GL_MAX_VERTEX_OUTPUT_COMPONENTSAdded [#def GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS](https://developer.apple.com/documentation/opengles/gl_max_vertex_texture_image_units)Added #def GL_MAX_VERTEX_UNIFORM_BLOCKSAdded #def GL_MAX_VERTEX_UNIFORM_COMPONENTSAdded [#def GL_MAX_VERTEX_UNIFORM_VECTORS](https://developer.apple.com/documentation/opengles/gl_max_vertex_uniform_vectors)Added [#def GL_MAX_VIEWPORT_DIMS](https://developer.apple.com/documentation/opengles/gl_max_viewport_dims)Added [#def GL_MEDIUM_FLOAT](https://developer.apple.com/documentation/opengles/gl_medium_float)Added [#def GL_MEDIUM_INT](https://developer.apple.com/documentation/opengles/gl_medium_int)Added #def GL_MINAdded #def GL_MINOR_VERSIONAdded #def GL_MIN_PROGRAM_TEXEL_OFFSETAdded [#def GL_MIRRORED_REPEAT](https://developer.apple.com/documentation/opengles/gl_mirrored_repeat)Added [#def GL_NEAREST](https://developer.apple.com/documentation/opengles/gl_nearest)Added [#def GL_NEAREST_MIPMAP_LINEAR](https://developer.apple.com/documentation/opengles/gl_nearest_mipmap_linear)Added [#def GL_NEAREST_MIPMAP_NEAREST](https://developer.apple.com/documentation/opengles/gl_nearest_mipmap_nearest)Added [#def GL_NEVER](https://developer.apple.com/documentation/opengles/gl_never)Added [#def GL_NICEST](https://developer.apple.com/documentation/opengles/gl_nicest)Added [#def GL_NONE](https://developer.apple.com/documentation/opengles/gl_none)Added [#def GL_NOTEQUAL](https://developer.apple.com/documentation/opengles/gl_notequal)Added [#def GL_NO_ERROR](https://developer.apple.com/documentation/opengles/gl_no_error)Added [#def GL_NUM_COMPRESSED_TEXTURE_FORMATS](https://developer.apple.com/documentation/opengles/gl_num_compressed_texture_formats)Added #def GL_NUM_EXTENSIONSAdded #def GL_NUM_PROGRAM_BINARY_FORMATSAdded #def GL_NUM_SAMPLE_COUNTSAdded [#def GL_NUM_SHADER_BINARY_FORMATS](https://developer.apple.com/documentation/opengles/gl_num_shader_binary_formats)Added #def GL_OBJECT_TYPEAdded [#def GL_ONE](https://developer.apple.com/documentation/opengles/gl_one)Added [#def GL_ONE_MINUS_CONSTANT_ALPHA](https://developer.apple.com/documentation/opengles/gl_one_minus_constant_alpha)Added [#def GL_ONE_MINUS_CONSTANT_COLOR](https://developer.apple.com/documentation/opengles/gl_one_minus_constant_color)Added [#def GL_ONE_MINUS_DST_ALPHA](https://developer.apple.com/documentation/opengles/gl_one_minus_dst_alpha)Added [#def GL_ONE_MINUS_DST_COLOR](https://developer.apple.com/documentation/opengles/gl_one_minus_dst_color)Added [#def GL_ONE_MINUS_SRC_ALPHA](https://developer.apple.com/documentation/opengles/gl_one_minus_src_alpha)Added [#def GL_ONE_MINUS_SRC_COLOR](https://developer.apple.com/documentation/opengles/gl_one_minus_src_color)Added [#def GL_OUT_OF_MEMORY](https://developer.apple.com/documentation/opengles/gl_out_of_memory)Added [#def GL_PACK_ALIGNMENT](https://developer.apple.com/documentation/opengles/gl_pack_alignment)Added #def GL_PACK_ROW_LENGTHAdded #def GL_PACK_SKIP_PIXELSAdded #def GL_PACK_SKIP_ROWSAdded #def GL_PIXEL_PACK_BUFFERAdded #def GL_PIXEL_PACK_BUFFER_BINDINGAdded #def GL_PIXEL_UNPACK_BUFFERAdded #def GL_PIXEL_UNPACK_BUFFER_BINDINGAdded [#def GL_POINTS](https://developer.apple.com/documentation/opengles/gl_points)Added [#def GL_POLYGON_OFFSET_FACTOR](https://developer.apple.com/documentation/opengles/gl_polygon_offset_factor)Added [#def GL_POLYGON_OFFSET_FILL](https://developer.apple.com/documentation/opengles/gl_polygon_offset_fill)Added [#def GL_POLYGON_OFFSET_UNITS](https://developer.apple.com/documentation/opengles/gl_polygon_offset_units)Added [#def GL_PRIMITIVE_RESTART_FIXED_INDEX](https://developer.apple.com/documentation/opengles/gl_primitive_restart_fixed_index)Added #def GL_PROGRAM_BINARY_FORMATSAdded #def GL_PROGRAM_BINARY_LENGTHAdded #def GL_PROGRAM_BINARY_RETRIEVABLE_HINTAdded #def GL_QUERY_RESULTAdded #def GL_QUERY_RESULT_AVAILABLEAdded #def GL_R11F_G11F_B10FAdded #def GL_R16FAdded #def GL_R16IAdded #def GL_R16UIAdded #def GL_R32FAdded #def GL_R32IAdded #def GL_R32UIAdded #def GL_R8Added #def GL_R8IAdded #def GL_R8UIAdded #def GL_R8_SNORMAdded #def GL_RASTERIZER_DISCARDAdded #def GL_READ_BUFFERAdded #def GL_READ_FRAMEBUFFERAdded #def GL_READ_FRAMEBUFFER_BINDINGAdded #def GL_REDAdded [#def GL_RED_BITS](https://developer.apple.com/documentation/opengles/gl_red_bits)Added #def GL_RED_INTEGERAdded [#def GL_RENDERBUFFER](https://developer.apple.com/documentation/opengles/gl_renderbuffer)Added [#def GL_RENDERBUFFER_ALPHA_SIZE](https://developer.apple.com/documentation/opengles/gl_renderbuffer_alpha_size)Added [#def GL_RENDERBUFFER_BINDING](https://developer.apple.com/documentation/opengles/gl_renderbuffer_binding)Added [#def GL_RENDERBUFFER_BLUE_SIZE](https://developer.apple.com/documentation/opengles/gl_renderbuffer_blue_size)Added [#def GL_RENDERBUFFER_DEPTH_SIZE](https://developer.apple.com/documentation/opengles/gl_renderbuffer_depth_size)Added [#def GL_RENDERBUFFER_GREEN_SIZE](https://developer.apple.com/documentation/opengles/gl_renderbuffer_green_size)Added [#def GL_RENDERBUFFER_HEIGHT](https://developer.apple.com/documentation/opengles/gl_renderbuffer_height)Added [#def GL_RENDERBUFFER_INTERNAL_FORMAT](https://developer.apple.com/documentation/opengles/gl_renderbuffer_internal_format)Added [#def GL_RENDERBUFFER_RED_SIZE](https://developer.apple.com/documentation/opengles/gl_renderbuffer_red_size)Added #def GL_RENDERBUFFER_SAMPLESAdded [#def GL_RENDERBUFFER_STENCIL_SIZE](https://developer.apple.com/documentation/opengles/gl_renderbuffer_stencil_size)Added [#def GL_RENDERBUFFER_WIDTH](https://developer.apple.com/documentation/opengles/gl_renderbuffer_width)Added [#def GL_RENDERER](https://developer.apple.com/documentation/opengles/gl_renderer)Added [#def GL_REPEAT](https://developer.apple.com/documentation/opengles/gl_repeat)Added [#def GL_REPLACE](https://developer.apple.com/documentation/opengles/gl_replace)Added #def GL_RGAdded #def GL_RG16FAdded #def GL_RG16IAdded #def GL_RG16UIAdded #def GL_RG32FAdded #def GL_RG32IAdded #def GL_RG32UIAdded #def GL_RG8Added #def GL_RG8IAdded #def GL_RG8UIAdded #def GL_RG8_SNORMAdded [#def GL_RGB](https://developer.apple.com/documentation/opengles/gl_rgb)Added #def GL_RGB10_A2Added #def GL_RGB10_A2UIAdded #def GL_RGB16FAdded #def GL_RGB16IAdded #def GL_RGB16UIAdded #def GL_RGB32FAdded #def GL_RGB32IAdded #def GL_RGB32UIAdded [#def GL_RGB565](https://developer.apple.com/documentation/opengles/gl_rgb565)Added [#def GL_RGB5_A1](https://developer.apple.com/documentation/opengles/gl_rgb5_a1)Added #def GL_RGB8Added #def GL_RGB8IAdded #def GL_RGB8UIAdded #def GL_RGB8_SNORMAdded #def GL_RGB9_E5Added [#def GL_RGBA](https://developer.apple.com/documentation/opengles/gl_rgba)Added #def GL_RGBA16FAdded #def GL_RGBA16IAdded #def GL_RGBA16UIAdded #def GL_RGBA32FAdded #def GL_RGBA32IAdded #def GL_RGBA32UIAdded [#def GL_RGBA4](https://developer.apple.com/documentation/opengles/gl_rgba4)Added #def GL_RGBA8Added #def GL_RGBA8IAdded #def GL_RGBA8UIAdded #def GL_RGBA8_SNORMAdded #def GL_RGBA_INTEGERAdded #def GL_RGB_INTEGERAdded #def GL_RG_INTEGERAdded [#def GL_SAMPLER_2D](https://developer.apple.com/documentation/opengles/gl_sampler_2d)Added #def GL_SAMPLER_2D_ARRAYAdded #def GL_SAMPLER_2D_ARRAY_SHADOWAdded #def GL_SAMPLER_2D_SHADOWAdded #def GL_SAMPLER_3DAdded #def GL_SAMPLER_BINDINGAdded [#def GL_SAMPLER_CUBE](https://developer.apple.com/documentation/opengles/gl_sampler_cube)Added #def GL_SAMPLER_CUBE_SHADOWAdded [#def GL_SAMPLES](https://developer.apple.com/documentation/opengles/gl_samples)Added [#def GL_SAMPLE_ALPHA_TO_COVERAGE](https://developer.apple.com/documentation/opengles/gl_sample_alpha_to_coverage)Added [#def GL_SAMPLE_BUFFERS](https://developer.apple.com/documentation/opengles/gl_sample_buffers)Added [#def GL_SAMPLE_COVERAGE](https://developer.apple.com/documentation/opengles/gl_sample_coverage)Added [#def GL_SAMPLE_COVERAGE_INVERT](https://developer.apple.com/documentation/opengles/gl_sample_coverage_invert)Added [#def GL_SAMPLE_COVERAGE_VALUE](https://developer.apple.com/documentation/opengles/gl_sample_coverage_value)Added [#def GL_SCISSOR_BOX](https://developer.apple.com/documentation/opengles/gl_scissor_box)Added [#def GL_SCISSOR_TEST](https://developer.apple.com/documentation/opengles/gl_scissor_test)Added #def GL_SEPARATE_ATTRIBSAdded [#def GL_SHADER_BINARY_FORMATS](https://developer.apple.com/documentation/opengles/gl_shader_binary_formats)Added [#def GL_SHADER_COMPILER](https://developer.apple.com/documentation/opengles/gl_shader_compiler)Added [#def GL_SHADER_SOURCE_LENGTH](https://developer.apple.com/documentation/opengles/gl_shader_source_length)Added [#def GL_SHADER_TYPE](https://developer.apple.com/documentation/opengles/gl_shader_type)Added [#def GL_SHADING_LANGUAGE_VERSION](https://developer.apple.com/documentation/opengles/gl_shading_language_version)Added [#def GL_SHORT](https://developer.apple.com/documentation/opengles/gl_short)Added #def GL_SIGNALEDAdded #def GL_SIGNED_NORMALIZEDAdded [#def GL_SRC_ALPHA](https://developer.apple.com/documentation/opengles/gl_src_alpha)Added [#def GL_SRC_ALPHA_SATURATE](https://developer.apple.com/documentation/opengles/gl_src_alpha_saturate)Added [#def GL_SRC_COLOR](https://developer.apple.com/documentation/opengles/gl_src_color)Added #def GL_SRGBAdded #def GL_SRGB8Added #def GL_SRGB8_ALPHA8Added #def GL_STATIC_COPYAdded [#def GL_STATIC_DRAW](https://developer.apple.com/documentation/opengles/gl_static_draw)Added #def GL_STATIC_READAdded #def GL_STENCILAdded [#def GL_STENCIL_ATTACHMENT](https://developer.apple.com/documentation/opengles/gl_stencil_attachment)Added [#def GL_STENCIL_BACK_FAIL](https://developer.apple.com/documentation/opengles/gl_stencil_back_fail)Added [#def GL_STENCIL_BACK_FUNC](https://developer.apple.com/documentation/opengles/gl_stencil_back_func)Added [#def GL_STENCIL_BACK_PASS_DEPTH_FAIL](https://developer.apple.com/documentation/opengles/gl_stencil_back_pass_depth_fail)Added [#def GL_STENCIL_BACK_PASS_DEPTH_PASS](https://developer.apple.com/documentation/opengles/gl_stencil_back_pass_depth_pass)Added [#def GL_STENCIL_BACK_REF](https://developer.apple.com/documentation/opengles/gl_stencil_back_ref)Added [#def GL_STENCIL_BACK_VALUE_MASK](https://developer.apple.com/documentation/opengles/gl_stencil_back_value_mask)Added [#def GL_STENCIL_BACK_WRITEMASK](https://developer.apple.com/documentation/opengles/gl_stencil_back_writemask)Added [#def GL_STENCIL_BITS](https://developer.apple.com/documentation/opengles/gl_stencil_bits)Added [#def GL_STENCIL_BUFFER_BIT](https://developer.apple.com/documentation/opengles/gl_stencil_buffer_bit)Added [#def GL_STENCIL_CLEAR_VALUE](https://developer.apple.com/documentation/opengles/gl_stencil_clear_value)Added [#def GL_STENCIL_FAIL](https://developer.apple.com/documentation/opengles/gl_stencil_fail)Added [#def GL_STENCIL_FUNC](https://developer.apple.com/documentation/opengles/gl_stencil_func)Added [#def GL_STENCIL_INDEX8](https://developer.apple.com/documentation/opengles/gl_stencil_index8)Added [#def GL_STENCIL_PASS_DEPTH_FAIL](https://developer.apple.com/documentation/opengles/gl_stencil_pass_depth_fail)Added [#def GL_STENCIL_PASS_DEPTH_PASS](https://developer.apple.com/documentation/opengles/gl_stencil_pass_depth_pass)Added [#def GL_STENCIL_REF](https://developer.apple.com/documentation/opengles/gl_stencil_ref)Added [#def GL_STENCIL_TEST](https://developer.apple.com/documentation/opengles/gl_stencil_test)Added [#def GL_STENCIL_VALUE_MASK](https://developer.apple.com/documentation/opengles/gl_stencil_value_mask)Added [#def GL_STENCIL_WRITEMASK](https://developer.apple.com/documentation/opengles/gl_stencil_writemask)Added #def GL_STREAM_COPYAdded [#def GL_STREAM_DRAW](https://developer.apple.com/documentation/opengles/gl_stream_draw)Added #def GL_STREAM_READAdded [#def GL_SUBPIXEL_BITS](https://developer.apple.com/documentation/opengles/gl_subpixel_bits)Added #def GL_SYNC_CONDITIONAdded #def GL_SYNC_FENCEAdded #def GL_SYNC_FLAGSAdded #def GL_SYNC_FLUSH_COMMANDS_BITAdded #def GL_SYNC_GPU_COMMANDS_COMPLETEAdded #def GL_SYNC_STATUSAdded [#def GL_TEXTURE](https://developer.apple.com/documentation/opengles/gl_texture)Added [#def GL_TEXTURE0](https://developer.apple.com/documentation/opengles/gl_texture0)Added [#def GL_TEXTURE1](https://developer.apple.com/documentation/opengles/gl_texture1)Added [#def GL_TEXTURE10](https://developer.apple.com/documentation/opengles/gl_texture10)Added [#def GL_TEXTURE11](https://developer.apple.com/documentation/opengles/gl_texture11)Added [#def GL_TEXTURE12](https://developer.apple.com/documentation/opengles/gl_texture12)Added [#def GL_TEXTURE13](https://developer.apple.com/documentation/opengles/gl_texture13)Added [#def GL_TEXTURE14](https://developer.apple.com/documentation/opengles/gl_texture14)Added [#def GL_TEXTURE15](https://developer.apple.com/documentation/opengles/gl_texture15)Added [#def GL_TEXTURE16](https://developer.apple.com/documentation/opengles/gl_texture16)Added [#def GL_TEXTURE17](https://developer.apple.com/documentation/opengles/gl_texture17)Added [#def GL_TEXTURE18](https://developer.apple.com/documentation/opengles/gl_texture18)Added [#def GL_TEXTURE19](https://developer.apple.com/documentation/opengles/gl_texture19)Added [#def GL_TEXTURE2](https://developer.apple.com/documentation/opengles/gl_texture2)Added [#def GL_TEXTURE20](https://developer.apple.com/documentation/opengles/gl_texture20)Added [#def GL_TEXTURE21](https://developer.apple.com/documentation/opengles/gl_texture21)Added [#def GL_TEXTURE22](https://developer.apple.com/documentation/opengles/gl_texture22)Added [#def GL_TEXTURE23](https://developer.apple.com/documentation/opengles/gl_texture23)Added [#def GL_TEXTURE24](https://developer.apple.com/documentation/opengles/gl_texture24)Added [#def GL_TEXTURE25](https://developer.apple.com/documentation/opengles/gl_texture25)Added [#def GL_TEXTURE26](https://developer.apple.com/documentation/opengles/gl_texture26)Added [#def GL_TEXTURE27](https://developer.apple.com/documentation/opengles/gl_texture27)Added [#def GL_TEXTURE28](https://developer.apple.com/documentation/opengles/gl_texture28)Added [#def GL_TEXTURE29](https://developer.apple.com/documentation/opengles/gl_texture29)Added [#def GL_TEXTURE3](https://developer.apple.com/documentation/opengles/gl_texture3)Added [#def GL_TEXTURE30](https://developer.apple.com/documentation/opengles/gl_texture30)Added [#def GL_TEXTURE31](https://developer.apple.com/documentation/opengles/gl_texture31)Added [#def GL_TEXTURE4](https://developer.apple.com/documentation/opengles/gl_texture4)Added [#def GL_TEXTURE5](https://developer.apple.com/documentation/opengles/gl_texture5)Added [#def GL_TEXTURE6](https://developer.apple.com/documentation/opengles/gl_texture6)Added [#def GL_TEXTURE7](https://developer.apple.com/documentation/opengles/gl_texture7)Added [#def GL_TEXTURE8](https://developer.apple.com/documentation/opengles/gl_texture8)Added [#def GL_TEXTURE9](https://developer.apple.com/documentation/opengles/gl_texture9)Added [#def GL_TEXTURE_2D](https://developer.apple.com/documentation/opengles/gl_texture_2d)Added #def GL_TEXTURE_2D_ARRAYAdded #def GL_TEXTURE_3DAdded #def GL_TEXTURE_BASE_LEVELAdded [#def GL_TEXTURE_BINDING_2D](https://developer.apple.com/documentation/opengles/gl_texture_binding_2d)Added #def GL_TEXTURE_BINDING_2D_ARRAYAdded #def GL_TEXTURE_BINDING_3DAdded [#def GL_TEXTURE_BINDING_CUBE_MAP](https://developer.apple.com/documentation/opengles/gl_texture_binding_cube_map)Added #def GL_TEXTURE_COMPARE_FUNCAdded #def GL_TEXTURE_COMPARE_MODEAdded [#def GL_TEXTURE_CUBE_MAP](https://developer.apple.com/documentation/opengles/gl_texture_cube_map)Added [#def GL_TEXTURE_CUBE_MAP_NEGATIVE_X](https://developer.apple.com/documentation/opengles/gl_texture_cube_map_negative_x)Added [#def GL_TEXTURE_CUBE_MAP_NEGATIVE_Y](https://developer.apple.com/documentation/opengles/gl_texture_cube_map_negative_y)Added [#def GL_TEXTURE_CUBE_MAP_NEGATIVE_Z](https://developer.apple.com/documentation/opengles/gl_texture_cube_map_negative_z)Added [#def GL_TEXTURE_CUBE_MAP_POSITIVE_X](https://developer.apple.com/documentation/opengles/gl_texture_cube_map_positive_x)Added [#def GL_TEXTURE_CUBE_MAP_POSITIVE_Y](https://developer.apple.com/documentation/opengles/gl_texture_cube_map_positive_y)Added [#def GL_TEXTURE_CUBE_MAP_POSITIVE_Z](https://developer.apple.com/documentation/opengles/gl_texture_cube_map_positive_z)Added #def GL_TEXTURE_IMMUTABLE_FORMATAdded [#def GL_TEXTURE_IMMUTABLE_LEVELS](https://developer.apple.com/documentation/opengles/gl_texture_immutable_levels)Added [#def GL_TEXTURE_MAG_FILTER](https://developer.apple.com/documentation/opengles/gl_texture_mag_filter)Added #def GL_TEXTURE_MAX_LEVELAdded #def GL_TEXTURE_MAX_LODAdded [#def GL_TEXTURE_MIN_FILTER](https://developer.apple.com/documentation/opengles/gl_texture_min_filter)Added #def GL_TEXTURE_MIN_LODAdded #def GL_TEXTURE_SWIZZLE_AAdded #def GL_TEXTURE_SWIZZLE_BAdded #def GL_TEXTURE_SWIZZLE_GAdded #def GL_TEXTURE_SWIZZLE_RAdded #def GL_TEXTURE_WRAP_RAdded [#def GL_TEXTURE_WRAP_S](https://developer.apple.com/documentation/opengles/gl_texture_wrap_s)Added [#def GL_TEXTURE_WRAP_T](https://developer.apple.com/documentation/opengles/gl_texture_wrap_t)Added #def GL_TIMEOUT_EXPIREDAdded #def GL_TIMEOUT_IGNOREDAdded #def GL_TRANSFORM_FEEDBACKAdded [#def GL_TRANSFORM_FEEDBACK_ACTIVE](https://developer.apple.com/documentation/opengles/gl_transform_feedback_active)Added #def GL_TRANSFORM_FEEDBACK_BINDINGAdded #def GL_TRANSFORM_FEEDBACK_BUFFERAdded #def GL_TRANSFORM_FEEDBACK_BUFFER_BINDINGAdded #def GL_TRANSFORM_FEEDBACK_BUFFER_MODEAdded #def GL_TRANSFORM_FEEDBACK_BUFFER_SIZEAdded #def GL_TRANSFORM_FEEDBACK_BUFFER_STARTAdded [#def GL_TRANSFORM_FEEDBACK_PAUSED](https://developer.apple.com/documentation/opengles/gl_transform_feedback_paused)Added #def GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTENAdded #def GL_TRANSFORM_FEEDBACK_VARYINGSAdded #def GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTHAdded [#def GL_TRIANGLES](https://developer.apple.com/documentation/opengles/gl_triangles)Added [#def GL_TRIANGLE_FAN](https://developer.apple.com/documentation/opengles/gl_triangle_fan)Added [#def GL_TRIANGLE_STRIP](https://developer.apple.com/documentation/opengles/gl_triangle_strip)Added [#def GL_TRUE](https://developer.apple.com/documentation/opengles/gl_true)Added #def GL_UNIFORM_ARRAY_STRIDEAdded #def GL_UNIFORM_BLOCK_ACTIVE_UNIFORMSAdded #def GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICESAdded #def GL_UNIFORM_BLOCK_BINDINGAdded #def GL_UNIFORM_BLOCK_DATA_SIZEAdded #def GL_UNIFORM_BLOCK_INDEXAdded #def GL_UNIFORM_BLOCK_NAME_LENGTHAdded #def GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADERAdded #def GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADERAdded #def GL_UNIFORM_BUFFERAdded #def GL_UNIFORM_BUFFER_BINDINGAdded #def GL_UNIFORM_BUFFER_OFFSET_ALIGNMENTAdded #def GL_UNIFORM_BUFFER_SIZEAdded #def GL_UNIFORM_BUFFER_STARTAdded #def GL_UNIFORM_IS_ROW_MAJORAdded #def GL_UNIFORM_MATRIX_STRIDEAdded #def GL_UNIFORM_NAME_LENGTHAdded #def GL_UNIFORM_OFFSETAdded #def GL_UNIFORM_SIZEAdded #def GL_UNIFORM_TYPEAdded [#def GL_UNPACK_ALIGNMENT](https://developer.apple.com/documentation/opengles/gl_unpack_alignment)Added #def GL_UNPACK_IMAGE_HEIGHTAdded #def GL_UNPACK_ROW_LENGTHAdded #def GL_UNPACK_SKIP_IMAGESAdded #def GL_UNPACK_SKIP_PIXELSAdded #def GL_UNPACK_SKIP_ROWSAdded #def GL_UNSIGNALEDAdded [#def GL_UNSIGNED_BYTE](https://developer.apple.com/documentation/opengles/gl_unsigned_byte)Added [#def GL_UNSIGNED_INT](https://developer.apple.com/documentation/opengles/gl_unsigned_int)Added #def GL_UNSIGNED_INT_10F_11F_11F_REVAdded #def GL_UNSIGNED_INT_24_8Added #def GL_UNSIGNED_INT_2_10_10_10_REVAdded #def GL_UNSIGNED_INT_5_9_9_9_REVAdded #def GL_UNSIGNED_INT_SAMPLER_2DAdded #def GL_UNSIGNED_INT_SAMPLER_2D_ARRAYAdded #def GL_UNSIGNED_INT_SAMPLER_3DAdded #def GL_UNSIGNED_INT_SAMPLER_CUBEAdded #def GL_UNSIGNED_INT_VEC2Added #def GL_UNSIGNED_INT_VEC3Added #def GL_UNSIGNED_INT_VEC4Added #def GL_UNSIGNED_NORMALIZEDAdded [#def GL_UNSIGNED_SHORT](https://developer.apple.com/documentation/opengles/gl_unsigned_short)Added [#def GL_UNSIGNED_SHORT_4_4_4_4](https://developer.apple.com/documentation/opengles/gl_unsigned_short_4_4_4_4)Added [#def GL_UNSIGNED_SHORT_5_5_5_1](https://developer.apple.com/documentation/opengles/gl_unsigned_short_5_5_5_1)Added [#def GL_UNSIGNED_SHORT_5_6_5](https://developer.apple.com/documentation/opengles/gl_unsigned_short_5_6_5)Added [#def GL_VALIDATE_STATUS](https://developer.apple.com/documentation/opengles/gl_validate_status)Added [#def GL_VENDOR](https://developer.apple.com/documentation/opengles/gl_vendor)Added [#def GL_VERSION](https://developer.apple.com/documentation/opengles/gl_version)Added #def GL_VERTEX_ARRAY_BINDINGAdded [#def GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING](https://developer.apple.com/documentation/opengles/gl_vertex_attrib_array_buffer_binding)Added #def GL_VERTEX_ATTRIB_ARRAY_DIVISORAdded [#def GL_VERTEX_ATTRIB_ARRAY_ENABLED](https://developer.apple.com/documentation/opengles/gl_vertex_attrib_array_enabled)Added #def GL_VERTEX_ATTRIB_ARRAY_INTEGERAdded [#def GL_VERTEX_ATTRIB_ARRAY_NORMALIZED](https://developer.apple.com/documentation/opengles/gl_vertex_attrib_array_normalized)Added [#def GL_VERTEX_ATTRIB_ARRAY_POINTER](https://developer.apple.com/documentation/opengles/gl_vertex_attrib_array_pointer)Added [#def GL_VERTEX_ATTRIB_ARRAY_SIZE](https://developer.apple.com/documentation/opengles/gl_vertex_attrib_array_size)Added [#def GL_VERTEX_ATTRIB_ARRAY_STRIDE](https://developer.apple.com/documentation/opengles/gl_vertex_attrib_array_stride)Added [#def GL_VERTEX_ATTRIB_ARRAY_TYPE](https://developer.apple.com/documentation/opengles/gl_vertex_attrib_array_type)Added [#def GL_VERTEX_SHADER](https://developer.apple.com/documentation/opengles/gl_vertex_shader)Added [#def GL_VIEWPORT](https://developer.apple.com/documentation/opengles/gl_viewport)Added #def GL_WAIT_FAILEDAdded [#def GL_ZERO](https://developer.apple.com/documentation/opengles/gl_zero)Added GLbitfieldAdded GLbooleanAdded GLbyteAdded GLcharAdded GLclampfAdded GLenumAdded GLfixedAdded GLfloatAdded GLhalfAdded GLintAdded GLint64Added GLintptrAdded GLshortAdded GLsizeiAdded GLsizeiptrAdded GLsyncAdded GLubyteAdded GLuintAdded GLuint64Added GLushortAdded GLvoidAdded [glActiveTexture()](https://developer.apple.com/documentation/opengles/1617480-glactivetexture)Added [glAttachShader()](https://developer.apple.com/documentation/opengles/1617323-glattachshader)Added glBeginQuery()Added glBeginTransformFeedback()Added [glBindAttribLocation()](https://developer.apple.com/documentation/opengles/1617262-glbindattriblocation)Added [glBindBuffer()](https://developer.apple.com/documentation/opengles/1617375-glbindbuffer)Added glBindBufferBase()Added glBindBufferRange()Added [glBindFramebuffer()](https://developer.apple.com/documentation/opengles/1617397-glbindframebuffer)Added [glBindRenderbuffer()](https://developer.apple.com/documentation/opengles/1617423-glbindrenderbuffer)Added glBindSampler()Added [glBindTexture()](https://developer.apple.com/documentation/opengles/1617415-glbindtexture)Added glBindTransformFeedback()Added glBindVertexArray()Added [glBlendColor()](https://developer.apple.com/documentation/opengles/1617234-glblendcolor)Added [glBlendEquation()](https://developer.apple.com/documentation/opengles/1617293-glblendequation)Added [glBlendEquationSeparate()](https://developer.apple.com/documentation/opengles/1617440-glblendequationseparate)Added [glBlendFunc()](https://developer.apple.com/documentation/opengles/1617298-glblendfunc)Added [glBlendFuncSeparate()](https://developer.apple.com/documentation/opengles/1617264-glblendfuncseparate)Added glBlitFramebuffer()Added [glBufferData()](https://developer.apple.com/documentation/opengles/1617693-glbufferdata)Added [glBufferSubData()](https://developer.apple.com/documentation/opengles/1617644-glbuffersubdata)Added [glCheckFramebufferStatus()](https://developer.apple.com/documentation/opengles/1617279-glcheckframebufferstatus)Added [glClear()](https://developer.apple.com/documentation/opengles/1617499-glclear)Added glClearBufferfi()Added glClearBufferfv()Added glClearBufferiv()Added glClearBufferuiv()Added [glClearColor()](https://developer.apple.com/documentation/opengles/1617582-glclearcolor)Added [glClearDepthf()](https://developer.apple.com/documentation/opengles/1617581-glcleardepthf)Added [glClearStencil()](https://developer.apple.com/documentation/opengles/1617555-glclearstencil)Added glClientWaitSync()Added [glColorMask()](https://developer.apple.com/documentation/opengles/1617442-glcolormask)Added [glCompileShader()](https://developer.apple.com/documentation/opengles/1617441-glcompileshader)Added [glCompressedTexImage2D()](https://developer.apple.com/documentation/opengles/1617532-glcompressedteximage2d)Added glCompressedTexImage3D()Added [glCompressedTexSubImage2D()](https://developer.apple.com/documentation/opengles/1617488-glcompressedtexsubimage2d)Added glCompressedTexSubImage3D()Added glCopyBufferSubData()Added [glCopyTexImage2D()](https://developer.apple.com/documentation/opengles/1617312-glcopyteximage2d)Added [glCopyTexSubImage2D()](https://developer.apple.com/documentation/opengles/1617592-glcopytexsubimage2d)Added glCopyTexSubImage3D()Added [glCreateProgram()](https://developer.apple.com/documentation/opengles/1617490-glcreateprogram)Added [glCreateShader()](https://developer.apple.com/documentation/opengles/1617228-glcreateshader)Added [glCullFace()](https://developer.apple.com/documentation/opengles/1617654-glcullface)Added [glDeleteBuffers()](https://developer.apple.com/documentation/opengles/1617677-gldeletebuffers)Added [glDeleteFramebuffers()](https://developer.apple.com/documentation/opengles/1617575-gldeleteframebuffers)Added [glDeleteProgram()](https://developer.apple.com/documentation/opengles/1617377-gldeleteprogram)Added glDeleteQueries()Added [glDeleteRenderbuffers()](https://developer.apple.com/documentation/opengles/1617550-gldeleterenderbuffers)Added glDeleteSamplers()Added [glDeleteShader()](https://developer.apple.com/documentation/opengles/1617595-gldeleteshader)Added glDeleteSync()Added [glDeleteTextures()](https://developer.apple.com/documentation/opengles/1617330-gldeletetextures)Added glDeleteTransformFeedbacks()Added glDeleteVertexArrays()Added [glDepthFunc()](https://developer.apple.com/documentation/opengles/1617331-gldepthfunc)Added [glDepthMask()](https://developer.apple.com/documentation/opengles/1617557-gldepthmask)Added [glDepthRangef()](https://developer.apple.com/documentation/opengles/1617401-gldepthrangef)Added [glDetachShader()](https://developer.apple.com/documentation/opengles/1617456-gldetachshader)Added [glDisable()](https://developer.apple.com/documentation/opengles/1617617-gldisable)Added [glDisableVertexAttribArray()](https://developer.apple.com/documentation/opengles/1617399-gldisablevertexattribarray)Added [glDrawArrays()](https://developer.apple.com/documentation/opengles/1617507-gldrawarrays)Added glDrawArraysInstanced()Added glDrawBuffers()Added [glDrawElements()](https://developer.apple.com/documentation/opengles/1617598-gldrawelements)Added glDrawElementsInstanced()Added glDrawRangeElements()Added [glEnable()](https://developer.apple.com/documentation/opengles/1617342-glenable)Added [glEnableVertexAttribArray()](https://developer.apple.com/documentation/opengles/1617541-glenablevertexattribarray)Added glEndQuery()Added glEndTransformFeedback()Added glFenceSync()Added [glFinish()](https://developer.apple.com/documentation/opengles/1617640-glfinish)Added [glFlush()](https://developer.apple.com/documentation/opengles/1617433-glflush)Added glFlushMappedBufferRange()Added [glFramebufferRenderbuffer()](https://developer.apple.com/documentation/opengles/1617686-glframebufferrenderbuffer)Added [glFramebufferTexture2D()](https://developer.apple.com/documentation/opengles/1617405-glframebuffertexture2d)Added glFramebufferTextureLayer()Added [glFrontFace()](https://developer.apple.com/documentation/opengles/1617260-glfrontface)Added [glGenBuffers()](https://developer.apple.com/documentation/opengles/1617417-glgenbuffers)Added [glGenFramebuffers()](https://developer.apple.com/documentation/opengles/1617341-glgenframebuffers)Added glGenQueries()Added [glGenRenderbuffers()](https://developer.apple.com/documentation/opengles/1617681-glgenrenderbuffers)Added glGenSamplers()Added [glGenTextures()](https://developer.apple.com/documentation/opengles/1617621-glgentextures)Added glGenTransformFeedbacks()Added glGenVertexArrays()Added [glGenerateMipmap()](https://developer.apple.com/documentation/opengles/1617469-glgeneratemipmap)Added [glGetActiveAttrib()](https://developer.apple.com/documentation/opengles/1617596-glgetactiveattrib)Added [glGetActiveUniform()](https://developer.apple.com/documentation/opengles/1617325-glgetactiveuniform)Added glGetActiveUniformBlockName()Added glGetActiveUniformBlockiv()Added glGetActiveUniformsiv()Added [glGetAttachedShaders()](https://developer.apple.com/documentation/opengles/1617610-glgetattachedshaders)Added [glGetAttribLocation()](https://developer.apple.com/documentation/opengles/1617398-glgetattriblocation)Added [glGetBooleanv()](https://developer.apple.com/documentation/opengles/1617391-glgetbooleanv)Added glGetBufferParameteri64v()Added [glGetBufferParameteriv()](https://developer.apple.com/documentation/opengles/1617520-glgetbufferparameteriv)Added glGetBufferPointerv()Added [glGetError()](https://developer.apple.com/documentation/opengles/1617613-glgeterror)Added [glGetFloatv()](https://developer.apple.com/documentation/opengles/1617275-glgetfloatv)Added glGetFragDataLocation()Added [glGetFramebufferAttachmentParameteriv()](https://developer.apple.com/documentation/opengles/1617682-glgetframebufferattachmentparame)Added glGetInteger64i_v()Added glGetInteger64v()Added glGetIntegeri_v()Added [glGetIntegerv()](https://developer.apple.com/documentation/opengles/1617284-glgetintegerv)Added glGetInternalformativ()Added glGetProgramBinary()Added [glGetProgramInfoLog()](https://developer.apple.com/documentation/opengles/1617233-glgetprograminfolog)Added [glGetProgramiv()](https://developer.apple.com/documentation/opengles/1617643-glgetprogramiv)Added glGetQueryObjectuiv()Added glGetQueryiv()Added [glGetRenderbufferParameteriv()](https://developer.apple.com/documentation/opengles/1617615-glgetrenderbufferparameteriv)Added glGetSamplerParameterfv()Added glGetSamplerParameteriv()Added [glGetShaderInfoLog()](https://developer.apple.com/documentation/opengles/1617419-glgetshaderinfolog)Added [glGetShaderPrecisionFormat()](https://developer.apple.com/documentation/opengles/1617276-glgetshaderprecisionformat)Added [glGetShaderSource()](https://developer.apple.com/documentation/opengles/1617452-glgetshadersource)Added [glGetShaderiv()](https://developer.apple.com/documentation/opengles/1617370-glgetshaderiv)Added [glGetString()](https://developer.apple.com/documentation/opengles/1617676-glgetstring)Added glGetStringi()Added glGetSynciv()Added [glGetTexParameterfv()](https://developer.apple.com/documentation/opengles/1617309-glgettexparameterfv)Added [glGetTexParameteriv()](https://developer.apple.com/documentation/opengles/1617366-glgettexparameteriv)Added glGetTransformFeedbackVarying()Added glGetUniformBlockIndex()Added glGetUniformIndices()Added [glGetUniformLocation()](https://developer.apple.com/documentation/opengles/1617403-glgetuniformlocation)Added [glGetUniformfv()](https://developer.apple.com/documentation/opengles/1617597-glgetuniformfv)Added [glGetUniformiv()](https://developer.apple.com/documentation/opengles/1617629-glgetuniformiv)Added glGetUniformuiv()Added glGetVertexAttribIiv()Added glGetVertexAttribIuiv()Added [glGetVertexAttribPointerv()](https://developer.apple.com/documentation/opengles/1617511-glgetvertexattribpointerv)Added [glGetVertexAttribfv()](https://developer.apple.com/documentation/opengles/1617512-glgetvertexattribfv)Added [glGetVertexAttribiv()](https://developer.apple.com/documentation/opengles/1617255-glgetvertexattribiv)Added [glHint()](https://developer.apple.com/documentation/opengles/1617647-glhint)Added [glInvalidateFramebuffer()](https://developer.apple.com/documentation/opengles/1617652-glinvalidateframebuffer)Added [glInvalidateSubFramebuffer()](https://developer.apple.com/documentation/opengles/1617516-glinvalidatesubframebuffer)Added [glIsBuffer()](https://developer.apple.com/documentation/opengles/1617571-glisbuffer)Added [glIsEnabled()](https://developer.apple.com/documentation/opengles/1617464-glisenabled)Added [glIsFramebuffer()](https://developer.apple.com/documentation/opengles/1617527-glisframebuffer)Added [glIsProgram()](https://developer.apple.com/documentation/opengles/1617431-glisprogram)Added glIsQuery()Added [glIsRenderbuffer()](https://developer.apple.com/documentation/opengles/1617548-glisrenderbuffer)Added glIsSampler()Added [glIsShader()](https://developer.apple.com/documentation/opengles/1617286-glisshader)Added glIsSync()Added [glIsTexture()](https://developer.apple.com/documentation/opengles/1617524-glistexture)Added glIsTransformFeedback()Added glIsVertexArray()Added [glLineWidth()](https://developer.apple.com/documentation/opengles/1617268-gllinewidth)Added [glLinkProgram()](https://developer.apple.com/documentation/opengles/1617274-gllinkprogram)Added glMapBufferRange()Added glPauseTransformFeedback()Added [glPixelStorei()](https://developer.apple.com/documentation/opengles/1617455-glpixelstorei)Added [glPolygonOffset()](https://developer.apple.com/documentation/opengles/1617287-glpolygonoffset)Added glProgramBinary()Added glProgramParameteri()Added glReadBuffer()Added [glReadPixels()](https://developer.apple.com/documentation/opengles/1617321-glreadpixels)Added [glReleaseShaderCompiler()](https://developer.apple.com/documentation/opengles/1617304-glreleaseshadercompiler)Added [glRenderbufferStorage()](https://developer.apple.com/documentation/opengles/1617587-glrenderbufferstorage)Added glRenderbufferStorageMultisample()Added glResumeTransformFeedback()Added [glSampleCoverage()](https://developer.apple.com/documentation/opengles/1617505-glsamplecoverage)Added glSamplerParameterf()Added glSamplerParameterfv()Added glSamplerParameteri()Added glSamplerParameteriv()Added [glScissor()](https://developer.apple.com/documentation/opengles/1617285-glscissor)Added [glShaderBinary()](https://developer.apple.com/documentation/opengles/1617514-glshaderbinary)Added [glShaderSource()](https://developer.apple.com/documentation/opengles/1617674-glshadersource)Added [glStencilFunc()](https://developer.apple.com/documentation/opengles/1617221-glstencilfunc)Added [glStencilFuncSeparate()](https://developer.apple.com/documentation/opengles/1617222-glstencilfuncseparate)Added [glStencilMask()](https://developer.apple.com/documentation/opengles/1617248-glstencilmask)Added [glStencilMaskSeparate()](https://developer.apple.com/documentation/opengles/1617471-glstencilmaskseparate)Added [glStencilOp()](https://developer.apple.com/documentation/opengles/1617476-glstencilop)Added [glStencilOpSeparate()](https://developer.apple.com/documentation/opengles/1617687-glstencilopseparate)Added [glTexImage2D()](https://developer.apple.com/documentation/opengles/1617448-glteximage2d)Added glTexImage3D()Added [glTexParameterf()](https://developer.apple.com/documentation/opengles/1617637-gltexparameterf)Added [glTexParameterfv()](https://developer.apple.com/documentation/opengles/1617517-gltexparameterfv)Added [glTexParameteri()](https://developer.apple.com/documentation/opengles/1617671-gltexparameteri)Added [glTexParameteriv()](https://developer.apple.com/documentation/opengles/1617318-gltexparameteriv)Added glTexStorage2D()Added glTexStorage3D()Added [glTexSubImage2D()](https://developer.apple.com/documentation/opengles/1617588-gltexsubimage2d)Added glTexSubImage3D()Added glTransformFeedbackVaryings()Added [glUniform1f()](https://developer.apple.com/documentation/opengles/1617660-gluniform1f)Added [glUniform1fv()](https://developer.apple.com/documentation/opengles/1617478-gluniform1fv)Added [glUniform1i()](https://developer.apple.com/documentation/opengles/1617363-gluniform1i)Added [glUniform1iv()](https://developer.apple.com/documentation/opengles/1617393-gluniform1iv)Added glUniform1ui()Added glUniform1uiv()Added [glUniform2f()](https://developer.apple.com/documentation/opengles/1617534-gluniform2f)Added [glUniform2fv()](https://developer.apple.com/documentation/opengles/1617460-gluniform2fv)Added [glUniform2i()](https://developer.apple.com/documentation/opengles/1617244-gluniform2i)Added [glUniform2iv()](https://developer.apple.com/documentation/opengles/1617688-gluniform2iv)Added glUniform2ui()Added glUniform2uiv()Added [glUniform3f()](https://developer.apple.com/documentation/opengles/1617410-gluniform3f)Added [glUniform3fv()](https://developer.apple.com/documentation/opengles/1617425-gluniform3fv)Added [glUniform3i()](https://developer.apple.com/documentation/opengles/1617695-gluniform3i)Added [glUniform3iv()](https://developer.apple.com/documentation/opengles/1617225-gluniform3iv)Added glUniform3ui()Added glUniform3uiv()Added [glUniform4f()](https://developer.apple.com/documentation/opengles/1617685-gluniform4f)Added [glUniform4fv()](https://developer.apple.com/documentation/opengles/1617566-gluniform4fv)Added [glUniform4i()](https://developer.apple.com/documentation/opengles/1617586-gluniform4i)Added [glUniform4iv()](https://developer.apple.com/documentation/opengles/1617314-gluniform4iv)Added glUniform4ui()Added glUniform4uiv()Added glUniformBlockBinding()Added [glUniformMatrix2fv()](https://developer.apple.com/documentation/opengles/1617513-gluniformmatrix2fv)Added glUniformMatrix2x3fv()Added glUniformMatrix2x4fv()Added [glUniformMatrix3fv()](https://developer.apple.com/documentation/opengles/1617396-gluniformmatrix3fv)Added glUniformMatrix3x2fv()Added glUniformMatrix3x4fv()Added [glUniformMatrix4fv()](https://developer.apple.com/documentation/opengles/1617249-gluniformmatrix4fv)Added glUniformMatrix4x2fv()Added glUniformMatrix4x3fv()Added glUnmapBuffer()Added [glUseProgram()](https://developer.apple.com/documentation/opengles/1617650-gluseprogram)Added [glValidateProgram()](https://developer.apple.com/documentation/opengles/1617467-glvalidateprogram)Added [glVertexAttrib1f()](https://developer.apple.com/documentation/opengles/1617657-glvertexattrib1f)Added [glVertexAttrib1fv()](https://developer.apple.com/documentation/opengles/1617573-glvertexattrib1fv)Added [glVertexAttrib2f()](https://developer.apple.com/documentation/opengles/1617523-glvertexattrib2f)Added [glVertexAttrib2fv()](https://developer.apple.com/documentation/opengles/1617479-glvertexattrib2fv)Added [glVertexAttrib3f()](https://developer.apple.com/documentation/opengles/1617503-glvertexattrib3f)Added [glVertexAttrib3fv()](https://developer.apple.com/documentation/opengles/1617226-glvertexattrib3fv)Added [glVertexAttrib4f()](https://developer.apple.com/documentation/opengles/1617384-glvertexattrib4f)Added [glVertexAttrib4fv()](https://developer.apple.com/documentation/opengles/1617484-glvertexattrib4fv)Added glVertexAttribDivisor()Added glVertexAttribI4i()Added glVertexAttribI4iv()Added glVertexAttribI4ui()Added glVertexAttribI4uiv()Added glVertexAttribIPointer()Added [glVertexAttribPointer()](https://developer.apple.com/documentation/opengles/1617630-glvertexattribpointer)Added [glViewport()](https://developer.apple.com/documentation/opengles/1617443-glviewport)Added glWaitSync()glext.hAdded [#def GL_ACTIVE_PROGRAM_EXT](https://developer.apple.com/documentation/opengles/gl_active_program_ext)Added [#def GL_ALL_SHADER_BITS_EXT](https://developer.apple.com/documentation/opengles/gl_all_shader_bits_ext)Added #def GL_APIENTRYPAdded [#def GL_APPLE_copy_texture_levels](https://developer.apple.com/documentation/opengles/gl_apple_copy_texture_levels)Added [#def GL_APPLE_rgb_422](https://developer.apple.com/documentation/opengles/gl_apple_rgb_422)Added [#def GL_APPLE_texture_format_BGRA8888](https://developer.apple.com/documentation/opengles/gl_apple_texture_format_bgra8888)Added [#def GL_BGRA](https://developer.apple.com/documentation/opengles/gl_bgra)Added [#def GL_BGRA8_EXT](https://developer.apple.com/documentation/opengles/gl_bgra8_ext)Added [#def GL_BGRA_EXT](https://developer.apple.com/documentation/opengles/gl_bgra_ext)Added [#def GL_BGRA_IMG](https://developer.apple.com/documentation/opengles/gl_bgra_img)Added [#def GL_BUFFER_OBJECT_EXT](https://developer.apple.com/documentation/opengles/gl_buffer_object_ext)Added [#def GL_COMPARE_REF_TO_TEXTURE_EXT](https://developer.apple.com/documentation/opengles/gl_compare_ref_to_texture_ext)Added [#def GL_COMPRESSED_RGBA_PVRTC_2BPPV1_IMG](https://developer.apple.com/documentation/opengles/gl_compressed_rgba_pvrtc_2bppv1_img)Added [#def GL_COMPRESSED_RGBA_PVRTC_4BPPV1_IMG](https://developer.apple.com/documentation/opengles/gl_compressed_rgba_pvrtc_4bppv1_img)Added [#def GL_COMPRESSED_RGB_PVRTC_2BPPV1_IMG](https://developer.apple.com/documentation/opengles/gl_compressed_rgb_pvrtc_2bppv1_img)Added [#def GL_COMPRESSED_RGB_PVRTC_4BPPV1_IMG](https://developer.apple.com/documentation/opengles/gl_compressed_rgb_pvrtc_4bppv1_img)Added [#def GL_COMPRESSED_SRGB_ALPHA_PVRTC_2BPPV1_EXT](https://developer.apple.com/documentation/opengles/gl_compressed_srgb_alpha_pvrtc_2bppv1_ext)Added [#def GL_COMPRESSED_SRGB_ALPHA_PVRTC_4BPPV1_EXT](https://developer.apple.com/documentation/opengles/gl_compressed_srgb_alpha_pvrtc_4bppv1_ext)Added [#def GL_COMPRESSED_SRGB_PVRTC_2BPPV1_EXT](https://developer.apple.com/documentation/opengles/gl_compressed_srgb_pvrtc_2bppv1_ext)Added [#def GL_COMPRESSED_SRGB_PVRTC_4BPPV1_EXT](https://developer.apple.com/documentation/opengles/gl_compressed_srgb_pvrtc_4bppv1_ext)Added [#def GL_EXT_color_buffer_half_float](https://developer.apple.com/documentation/opengles/gl_ext_color_buffer_half_float)Added [#def GL_EXT_debug_label](https://developer.apple.com/documentation/opengles/gl_ext_debug_label)Added [#def GL_EXT_debug_marker](https://developer.apple.com/documentation/opengles/gl_ext_debug_marker)Added [#def GL_EXT_pvrtc_sRGB](https://developer.apple.com/documentation/opengles/gl_ext_pvrtc_srgb)Added [#def GL_EXT_read_format_bgra](https://developer.apple.com/documentation/opengles/gl_ext_read_format_bgra)Added [#def GL_EXT_separate_shader_objects](https://developer.apple.com/documentation/opengles/gl_ext_separate_shader_objects)Added [#def GL_EXT_shader_framebuffer_fetch](https://developer.apple.com/documentation/opengles/gl_ext_shader_framebuffer_fetch)Added [#def GL_EXT_shader_texture_lod](https://developer.apple.com/documentation/opengles/gl_ext_shader_texture_lod)Added [#def GL_EXT_shadow_samplers](https://developer.apple.com/documentation/opengles/gl_ext_shadow_samplers)Added [#def GL_EXT_texture_filter_anisotropic](https://developer.apple.com/documentation/opengles/gl_ext_texture_filter_anisotropic)Added [#def GL_FRAGMENT_SHADER_BIT_EXT](https://developer.apple.com/documentation/opengles/gl_fragment_shader_bit_ext)Added [#def GL_FRAGMENT_SHADER_DERIVATIVE_HINT_OES](https://developer.apple.com/documentation/opengles/gl_fragment_shader_derivative_hint_oes)Added [#def GL_FRAGMENT_SHADER_DISCARDS_SAMPLES_EXT](https://developer.apple.com/documentation/opengles/gl_fragment_shader_discards_samples_ext)Added [#def GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE_EXT](https://developer.apple.com/documentation/opengles/gl_framebuffer_attachment_component_type_ext)Added [#def GL_IMG_read_format](https://developer.apple.com/documentation/opengles/gl_img_read_format)Added [#def GL_IMG_texture_compression_pvrtc](https://developer.apple.com/documentation/opengles/gl_img_texture_compression_pvrtc)Added [#def GL_MAX_TEXTURE_MAX_ANISOTROPY_EXT](https://developer.apple.com/documentation/opengles/gl_max_texture_max_anisotropy_ext)Added [#def GL_OES_standard_derivatives](https://developer.apple.com/documentation/opengles/gl_oes_standard_derivatives)Added [#def GL_PROGRAM_OBJECT_EXT](https://developer.apple.com/documentation/opengles/gl_program_object_ext)Added [#def GL_PROGRAM_PIPELINE_BINDING_EXT](https://developer.apple.com/documentation/opengles/gl_program_pipeline_binding_ext)Added [#def GL_PROGRAM_PIPELINE_OBJECT_EXT](https://developer.apple.com/documentation/opengles/gl_program_pipeline_object_ext)Added [#def GL_PROGRAM_SEPARABLE_EXT](https://developer.apple.com/documentation/opengles/gl_program_separable_ext)Added [#def GL_QUERY_OBJECT_EXT](https://developer.apple.com/documentation/opengles/gl_query_object_ext)Added [#def GL_R16F_EXT](https://developer.apple.com/documentation/opengles/gl_r16f_ext)Added [#def GL_RG16F_EXT](https://developer.apple.com/documentation/opengles/gl_rg16f_ext)Added [#def GL_RGB16F_EXT](https://developer.apple.com/documentation/opengles/gl_rgb16f_ext)Added [#def GL_RGBA16F_EXT](https://developer.apple.com/documentation/opengles/gl_rgba16f_ext)Added [#def GL_RGB_422_APPLE](https://developer.apple.com/documentation/opengles/gl_rgb_422_apple)Added [#def GL_RGB_RAW_422_APPLE](https://developer.apple.com/documentation/opengles/gl_rgb_raw_422_apple)Added #def GL_SAMPLERAdded [#def GL_SAMPLER_2D_SHADOW_EXT](https://developer.apple.com/documentation/opengles/gl_sampler_2d_shadow_ext)Added [#def GL_SHADER_OBJECT_EXT](https://developer.apple.com/documentation/opengles/gl_shader_object_ext)Added [#def GL_SYNC_OBJECT_APPLE](https://developer.apple.com/documentation/opengles/gl_sync_object_apple)Added [#def GL_TEXTURE_COMPARE_FUNC_EXT](https://developer.apple.com/documentation/opengles/gl_texture_compare_func_ext)Added [#def GL_TEXTURE_COMPARE_MODE_EXT](https://developer.apple.com/documentation/opengles/gl_texture_compare_mode_ext)Added [#def GL_TEXTURE_MAX_ANISOTROPY_EXT](https://developer.apple.com/documentation/opengles/gl_texture_max_anisotropy_ext)Added [#def GL_UNSIGNED_NORMALIZED_EXT](https://developer.apple.com/documentation/opengles/gl_unsigned_normalized_ext)Added [#def GL_UNSIGNED_SHORT_1_5_5_5_REV](https://developer.apple.com/documentation/opengles/gl_unsigned_short_1_5_5_5_rev)Added [#def GL_UNSIGNED_SHORT_1_5_5_5_REV_EXT](https://developer.apple.com/documentation/opengles/gl_unsigned_short_1_5_5_5_rev_ext)Added [#def GL_UNSIGNED_SHORT_4_4_4_4_REV](https://developer.apple.com/documentation/opengles/gl_unsigned_short_4_4_4_4_rev)Added [#def GL_UNSIGNED_SHORT_4_4_4_4_REV_EXT](https://developer.apple.com/documentation/opengles/gl_unsigned_short_4_4_4_4_rev_ext)Added [#def GL_UNSIGNED_SHORT_4_4_4_4_REV_IMG](https://developer.apple.com/documentation/opengles/gl_unsigned_short_4_4_4_4_rev_img)Added [#def GL_UNSIGNED_SHORT_8_8_APPLE](https://developer.apple.com/documentation/opengles/gl_unsigned_short_8_8_apple)Added [#def GL_UNSIGNED_SHORT_8_8_REV_APPLE](https://developer.apple.com/documentation/opengles/gl_unsigned_short_8_8_rev_apple)Added [#def GL_VERTEX_ARRAY_OBJECT_EXT](https://developer.apple.com/documentation/opengles/gl_vertex_array_object_ext)Added [#def GL_VERTEX_SHADER_BIT_EXT](https://developer.apple.com/documentation/opengles/gl_vertex_shader_bit_ext)Added [glActiveShaderProgramEXT()](https://developer.apple.com/documentation/opengles/1623883-glactiveshaderprogramext)Added [glBindProgramPipelineEXT()](https://developer.apple.com/documentation/opengles/1623765-glbindprogrampipelineext)Added [glCopyTextureLevelsAPPLE()](https://developer.apple.com/documentation/opengles/1614355-glcopytexturelevelsapple)Added [glCreateShaderProgramvEXT()](https://developer.apple.com/documentation/opengles/1623803-glcreateshaderprogramvext)Added [glDeleteProgramPipelinesEXT()](https://developer.apple.com/documentation/opengles/1623799-gldeleteprogrampipelinesext)Added [glGenProgramPipelinesEXT()](https://developer.apple.com/documentation/opengles/1623828-glgenprogrampipelinesext)Added [glGetObjectLabelEXT()](https://developer.apple.com/documentation/opengles/1614334-glgetobjectlabelext)Added [glGetProgramPipelineInfoLogEXT()](https://developer.apple.com/documentation/opengles/1623790-glgetprogrampipelineinfologext)Added [glGetProgramPipelineivEXT()](https://developer.apple.com/documentation/opengles/1623867-glgetprogrampipelineivext)Added [glInsertEventMarkerEXT()](https://developer.apple.com/documentation/opengles/1614284-glinserteventmarkerext)Added [glIsProgramPipelineEXT()](https://developer.apple.com/documentation/opengles/1623823-glisprogrampipelineext)Added [glLabelObjectEXT()](https://developer.apple.com/documentation/opengles/1614324-gllabelobjectext)Added [glPopGroupMarkerEXT()](https://developer.apple.com/documentation/opengles/1614338-glpopgroupmarkerext)Added [glProgramParameteriEXT()](https://developer.apple.com/documentation/opengles/1623862-glprogramparameteriext)Added [glProgramUniform1fEXT()](https://developer.apple.com/documentation/opengles/1623822-glprogramuniform1fext)Added [glProgramUniform1fvEXT()](https://developer.apple.com/documentation/opengles/1623778-glprogramuniform1fvext)Added [glProgramUniform1iEXT()](https://developer.apple.com/documentation/opengles/1623830-glprogramuniform1iext)Added [glProgramUniform1ivEXT()](https://developer.apple.com/documentation/opengles/1623805-glprogramuniform1ivext)Added [glProgramUniform1uiEXT()](https://developer.apple.com/documentation/opengles/1623879-glprogramuniform1uiext)Added [glProgramUniform1uivEXT()](https://developer.apple.com/documentation/opengles/1623788-glprogramuniform1uivext)Added [glProgramUniform2fEXT()](https://developer.apple.com/documentation/opengles/1623858-glprogramuniform2fext)Added [glProgramUniform2fvEXT()](https://developer.apple.com/documentation/opengles/1623769-glprogramuniform2fvext)Added [glProgramUniform2iEXT()](https://developer.apple.com/documentation/opengles/1623782-glprogramuniform2iext)Added [glProgramUniform2ivEXT()](https://developer.apple.com/documentation/opengles/1623880-glprogramuniform2ivext)Added [glProgramUniform2uiEXT()](https://developer.apple.com/documentation/opengles/1623848-glprogramuniform2uiext)Added [glProgramUniform2uivEXT()](https://developer.apple.com/documentation/opengles/1623831-glprogramuniform2uivext)Added [glProgramUniform3fEXT()](https://developer.apple.com/documentation/opengles/1623780-glprogramuniform3fext)Added [glProgramUniform3fvEXT()](https://developer.apple.com/documentation/opengles/1623770-glprogramuniform3fvext)Added [glProgramUniform3iEXT()](https://developer.apple.com/documentation/opengles/1623793-glprogramuniform3iext)Added [glProgramUniform3ivEXT()](https://developer.apple.com/documentation/opengles/1623784-glprogramuniform3ivext)Added [glProgramUniform3uiEXT()](https://developer.apple.com/documentation/opengles/1623859-glprogramuniform3uiext)Added [glProgramUniform3uivEXT()](https://developer.apple.com/documentation/opengles/1623837-glprogramuniform3uivext)Added [glProgramUniform4fEXT()](https://developer.apple.com/documentation/opengles/1623829-glprogramuniform4fext)Added [glProgramUniform4fvEXT()](https://developer.apple.com/documentation/opengles/1623804-glprogramuniform4fvext)Added [glProgramUniform4iEXT()](https://developer.apple.com/documentation/opengles/1623851-glprogramuniform4iext)Added [glProgramUniform4ivEXT()](https://developer.apple.com/documentation/opengles/1623791-glprogramuniform4ivext)Added [glProgramUniform4uiEXT()](https://developer.apple.com/documentation/opengles/1623870-glprogramuniform4uiext)Added [glProgramUniform4uivEXT()](https://developer.apple.com/documentation/opengles/1623818-glprogramuniform4uivext)Added [glProgramUniformMatrix2fvEXT()](https://developer.apple.com/documentation/opengles/1623814-glprogramuniformmatrix2fvext)Added [glProgramUniformMatrix2x3fvEXT()](https://developer.apple.com/documentation/opengles/1623845-glprogramuniformmatrix2x3fvext)Added [glProgramUniformMatrix2x4fvEXT()](https://developer.apple.com/documentation/opengles/1623794-glprogramuniformmatrix2x4fvext)Added [glProgramUniformMatrix3fvEXT()](https://developer.apple.com/documentation/opengles/1623873-glprogramuniformmatrix3fvext)Added [glProgramUniformMatrix3x2fvEXT()](https://developer.apple.com/documentation/opengles/1623806-glprogramuniformmatrix3x2fvext)Added [glProgramUniformMatrix3x4fvEXT()](https://developer.apple.com/documentation/opengles/1623812-glprogramuniformmatrix3x4fvext)Added [glProgramUniformMatrix4fvEXT()](https://developer.apple.com/documentation/opengles/1623777-glprogramuniformmatrix4fvext)Added [glProgramUniformMatrix4x2fvEXT()](https://developer.apple.com/documentation/opengles/1623786-glprogramuniformmatrix4x2fvext)Added [glProgramUniformMatrix4x3fvEXT()](https://developer.apple.com/documentation/opengles/1623887-glprogramuniformmatrix4x3fvext)Added [glPushGroupMarkerEXT()](https://developer.apple.com/documentation/opengles/1614275-glpushgroupmarkerext)Added [glUseProgramStagesEXT()](https://developer.apple.com/documentation/opengles/1623776-gluseprogramstagesext)Added [glValidateProgramPipelineEXT()](https://developer.apple.com/documentation/opengles/1623826-glvalidateprogrampipelineext)glext.hAdded [#def GL_COMPRESSED_SRGB_ALPHA_PVRTC_2BPPV1_EXT](https://developer.apple.com/documentation/opengles/gl_compressed_srgb_alpha_pvrtc_2bppv1_ext)Added [#def GL_COMPRESSED_SRGB_ALPHA_PVRTC_4BPPV1_EXT](https://developer.apple.com/documentation/opengles/gl_compressed_srgb_alpha_pvrtc_4bppv1_ext)Added [#def GL_COMPRESSED_SRGB_PVRTC_2BPPV1_EXT](https://developer.apple.com/documentation/opengles/gl_compressed_srgb_pvrtc_2bppv1_ext)Added [#def GL_COMPRESSED_SRGB_PVRTC_4BPPV1_EXT](https://developer.apple.com/documentation/opengles/gl_compressed_srgb_pvrtc_4bppv1_ext)Added [#def GL_EXT_draw_instanced](https://developer.apple.com/documentation/opengles/gl_ext_draw_instanced)Added [#def GL_EXT_instanced_arrays](https://developer.apple.com/documentation/opengles/gl_ext_instanced_arrays)Added [#def GL_EXT_pvrtc_sRGB](https://developer.apple.com/documentation/opengles/gl_ext_pvrtc_srgb)Added [#def GL_EXT_sRGB](https://developer.apple.com/documentation/opengles/gl_ext_srgb)Added [#def GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING_EXT](https://developer.apple.com/documentation/opengles/gl_framebuffer_attachment_color_encoding_ext)Added [#def GL_OES_texture_half_float_linear](https://developer.apple.com/documentation/opengles/gl_oes_texture_half_float_linear)Added #def GL_SRGB8_ALPHA8_EXTAdded #def GL_SRGB_ALPHA_EXTAdded #def GL_SRGB_EXTAdded [#def GL_VERTEX_ATTRIB_ARRAY_DIVISOR_EXT](https://developer.apple.com/documentation/opengles/gl_vertex_attrib_array_divisor_ext)Added [glDrawArraysInstancedEXT()](https://developer.apple.com/documentation/opengles/1624715-gldrawarraysinstancedext)Added [glDrawElementsInstancedEXT()](https://developer.apple.com/documentation/opengles/1624690-gldrawelementsinstancedext)Added [glVertexAttribDivisorEXT()](https://developer.apple.com/documentation/opengles/1624718-glvertexattribdivisorext)Modified [glCreateShaderProgramvEXT()](https://developer.apple.com/documentation/opengles/1623803-glcreateshaderprogramvext)

|  | Declaration |
| --- | --- |
| From | GLuint glCreateShaderProgramvEXT ( GLenum type, GLsizei count, const GLchar \*\*strings); |
| To | GLuint glCreateShaderProgramvEXT ( GLenum type, GLsizei count, const GLchar \*const \*strings); |

## PassKit

PKAddPassesViewController.hAdded [-[PKAddPassesViewController initWithPasses:]](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller/1619217-initwithpasses)PKError.hAdded PKErrorPermissionDeniedPKPass.hAdded [PKPass.userInfo](https://developer.apple.com/documentation/passkit/pkpass/1618794-userinfo)PKPassLibrary.hAdded [-[PKPassLibrary addPasses:withCompletionHandler:]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617093-addpasses)Added [PKPassLibraryAddPassesStatus](https://developer.apple.com/documentation/passkit/pkpasslibraryaddpassesstatus)Added [PKPassLibraryDidAddPasses](https://developer.apple.com/documentation/passkit/pkpasslibraryaddpassesstatus/didaddpasses)Added [PKPassLibraryDidCancelAddPasses](https://developer.apple.com/documentation/passkit/pkpasslibraryaddpassesstatus/pkpasslibrarydidcanceladdpasses)Added [PKPassLibraryShouldReviewPasses](https://developer.apple.com/documentation/passkit/pkpasslibraryaddpassesstatus/pkpasslibraryshouldreviewpasses)

## QuartzCore

CAEmitterBehavior.hAdded CAEmitterBehaviorAdded +[CAEmitterBehavior behaviorTypes]Added +[CAEmitterBehavior behaviorWithType:]Added CAEmitterBehavior.enabledAdded -[CAEmitterBehavior initWithType:]Added CAEmitterBehavior.nameAdded CAEmitterBehavior.typeAdded kCAEmitterBehaviorAlignToMotionAdded kCAEmitterBehaviorAttractorAdded kCAEmitterBehaviorColorOverLifeAdded kCAEmitterBehaviorDragAdded kCAEmitterBehaviorLightAdded kCAEmitterBehaviorValueOverLifeAdded kCAEmitterBehaviorWaveCALayer.hAdded [CALayer.allowsEdgeAntialiasing](https://developer.apple.com/documentation/quartzcore/calayer/1621285-allowsedgeantialiasing)Added [CALayer.allowsGroupOpacity](https://developer.apple.com/documentation/quartzcore/calayer/1621277-allowsgroupopacity)

## QuickLook

No changes

## SafariServices

SSReadingList.hAdded [SSReadingList](https://developer.apple.com/documentation/safariservices/ssreadinglist)Added [-[SSReadingList addReadingListItemWithURL:title:previewText:error:]](https://developer.apple.com/documentation/safariservices/ssreadinglist/1621226-addreadinglistitemwithurl)Added [+[SSReadingList defaultReadingList]](https://developer.apple.com/documentation/safariservices/ssreadinglist/1621220-defaultreadinglist)Added [+[SSReadingList supportsURL:]](https://developer.apple.com/documentation/safariservices/ssreadinglist/1621224-supportsurl)Added [SSReadingListErrorCode](https://developer.apple.com/documentation/safariservices/ssreadinglisterror/code)Added [SSReadingListErrorDomain](https://developer.apple.com/documentation/safariservices/ssreadinglisterrordomain)Added [SSReadingListErrorURLSchemeNotAllowed](https://developer.apple.com/documentation/safariservices/ssreadinglisterrorcode/ssreadinglisterrorurlschemenotallowed)SafariServices.h

## Security

CipherSuite.hAdded [TLS_DHE_PSK_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_psk_with_3des_ede_cbc_sha)Added [TLS_DHE_PSK_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_psk_with_aes_128_cbc_sha)Added [TLS_DHE_PSK_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/tls_dhe_psk_with_aes_128_cbc_sha256)Added [TLS_DHE_PSK_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/tls_dhe_psk_with_aes_128_gcm_sha256)Added [TLS_DHE_PSK_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/tls_dhe_psk_with_aes_256_cbc_sha)Added [TLS_DHE_PSK_WITH_AES_256_CBC_SHA384](https://developer.apple.com/documentation/security/tls_dhe_psk_with_aes_256_cbc_sha384)Added [TLS_DHE_PSK_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_psk_with_aes_256_gcm_sha384)Added [TLS_DHE_PSK_WITH_NULL_SHA](https://developer.apple.com/documentation/security/tls_dhe_psk_with_null_sha)Added [TLS_DHE_PSK_WITH_NULL_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_psk_with_null_sha256)Added [TLS_DHE_PSK_WITH_NULL_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_psk_with_null_sha384)Added [TLS_DHE_PSK_WITH_RC4_128_SHA](https://developer.apple.com/documentation/security/tls_dhe_psk_with_rc4_128_sha)Added [TLS_PSK_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_psk_with_3des_ede_cbc_sha)Added [TLS_PSK_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_psk_with_aes_128_cbc_sha)Added [TLS_PSK_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_psk_with_aes_128_cbc_sha256)Added [TLS_PSK_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_psk_with_aes_128_gcm_sha256)Added [TLS_PSK_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_psk_with_aes_256_cbc_sha)Added [TLS_PSK_WITH_AES_256_CBC_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_psk_with_aes_256_cbc_sha384)Added [TLS_PSK_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/tls_psk_with_aes_256_gcm_sha384)Added [TLS_PSK_WITH_NULL_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_psk_with_null_sha)Added [TLS_PSK_WITH_NULL_SHA256](https://developer.apple.com/documentation/security/tls_psk_with_null_sha256)Added [TLS_PSK_WITH_NULL_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_psk_with_null_sha384)Added [TLS_PSK_WITH_RC4_128_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_psk_with_rc4_128_sha)Added [TLS_RSA_PSK_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/tls_rsa_psk_with_3des_ede_cbc_sha)Added [TLS_RSA_PSK_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/tls_rsa_psk_with_aes_128_cbc_sha)Added [TLS_RSA_PSK_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/tls_rsa_psk_with_aes_128_cbc_sha256)Added [TLS_RSA_PSK_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_psk_with_aes_128_gcm_sha256)Added [TLS_RSA_PSK_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/tls_rsa_psk_with_aes_256_cbc_sha)Added [TLS_RSA_PSK_WITH_AES_256_CBC_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_psk_with_aes_256_cbc_sha384)Added [TLS_RSA_PSK_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_psk_with_aes_256_gcm_sha384)Added [TLS_RSA_PSK_WITH_NULL_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_psk_with_null_sha)Added [TLS_RSA_PSK_WITH_NULL_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_psk_with_null_sha256)Added [TLS_RSA_PSK_WITH_NULL_SHA384](https://developer.apple.com/documentation/security/tls_rsa_psk_with_null_sha384)Added [TLS_RSA_PSK_WITH_RC4_128_SHA](https://developer.apple.com/documentation/security/tls_rsa_psk_with_rc4_128_sha)SecBase.hAdded [errSecBadReq](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecbadreq)Added [errSecIO](https://developer.apple.com/documentation/security/errsecio)Added [errSecInternalComponent](https://developer.apple.com/documentation/security/errsecinternalcomponent)Added [errSecOpWr](https://developer.apple.com/documentation/security/errsecopwr)Added [errSecUserCanceled](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecusercanceled)Modified [SecPolicyRef](https://developer.apple.com/documentation/security/secpolicy)

|  | Header |
| --- | --- |
| From | Security/SecPolicy.h |
| To | Security/SecBase.h |

SecItem.hAdded [kSecAttrSynchronizable](https://developer.apple.com/documentation/security/ksecattrsynchronizable)Added [kSecAttrSynchronizableAny](https://developer.apple.com/documentation/security/ksecattrsynchronizableany)SecPolicy.hAdded [SecPolicyCopyProperties()](https://developer.apple.com/documentation/security/1401915-secpolicycopyproperties)Added [SecPolicyCreateRevocation()](https://developer.apple.com/documentation/security/1400026-secpolicycreaterevocation)Added [SecPolicyCreateWithProperties()](https://developer.apple.com/documentation/security/1394568-secpolicycreatewithproperties)Added [kSecPolicyAppleCodeSigning](https://developer.apple.com/documentation/security/ksecpolicyapplecodesigning)Added [kSecPolicyAppleEAP](https://developer.apple.com/documentation/security/ksecpolicyappleeap)Added [kSecPolicyAppleIDValidation](https://developer.apple.com/documentation/security/ksecpolicyappleidvalidation)Added [kSecPolicyAppleIPsec](https://developer.apple.com/documentation/security/ksecpolicyappleipsec)Added [kSecPolicyAppleRevocation](https://developer.apple.com/documentation/security/ksecpolicyapplerevocation)Added [kSecPolicyAppleSMIME](https://developer.apple.com/documentation/security/ksecpolicyapplesmime)Added [kSecPolicyAppleSSL](https://developer.apple.com/documentation/security/ksecpolicyapplessl)Added [kSecPolicyAppleTimeStamping](https://developer.apple.com/documentation/security/ksecpolicyappletimestamping)Added [kSecPolicyAppleX509Basic](https://developer.apple.com/documentation/security/ksecpolicyapplex509basic)Added [kSecPolicyClient](https://developer.apple.com/documentation/security/ksecpolicyclient)Added [kSecPolicyName](https://developer.apple.com/documentation/security/ksecpolicyname)Added [kSecPolicyOid](https://developer.apple.com/documentation/security/ksecpolicyoid)Added [kSecPolicyRevocationFlags](https://developer.apple.com/documentation/security/ksecpolicyrevocationflags)Added [kSecRevocationCRLMethod](https://developer.apple.com/documentation/security/ksecrevocationcrlmethod)Added [kSecRevocationNetworkAccessDisabled](https://developer.apple.com/documentation/security/ksecrevocationnetworkaccessdisabled)Added [kSecRevocationOCSPMethod](https://developer.apple.com/documentation/security/1563600-revocation_policy_constants/ksecrevocationocspmethod)Added [kSecRevocationPreferCRL](https://developer.apple.com/documentation/security/ksecrevocationprefercrl)Added [kSecRevocationRequirePositiveResponse](https://developer.apple.com/documentation/security/1563600-revocation_policy_constants/ksecrevocationrequirepositiveresponse)Added [kSecRevocationUseAnyAvailableMethod](https://developer.apple.com/documentation/security/ksecrevocationuseanyavailablemethod)Modified [SecPolicyRef](https://developer.apple.com/documentation/security/secpolicy)

|  | Header |
| --- | --- |
| From | Security/SecPolicy.h |
| To | Security/SecBase.h |

SecTrust.hAdded [SecTrustCallback](https://developer.apple.com/documentation/security/sectrustcallback)Added [SecTrustCopyCustomAnchorCertificates()](https://developer.apple.com/documentation/security/1401743-sectrustcopycustomanchorcertific)Added [SecTrustCopyPolicies()](https://developer.apple.com/documentation/security/1392716-sectrustcopypolicies)Added [SecTrustCopyProperties()](https://developer.apple.com/documentation/security/1401567-sectrustcopyproperties)Added [SecTrustCopyResult()](https://developer.apple.com/documentation/security/1398612-sectrustcopyresult)Added [SecTrustEvaluateAsync()](https://developer.apple.com/documentation/security/1400632-sectrustevaluateasync)Added [SecTrustGetNetworkFetchAllowed()](https://developer.apple.com/documentation/security/1400259-sectrustgetnetworkfetchallowed)Added [SecTrustGetTrustResult()](https://developer.apple.com/documentation/security/1396077-sectrustgettrustresult)Added [SecTrustSetNetworkFetchAllowed()](https://developer.apple.com/documentation/security/1395083-sectrustsetnetworkfetchallowed)Added [SecTrustSetOCSPResponse()](https://developer.apple.com/documentation/security/1400880-sectrustsetocspresponse)Added [SecTrustSetPolicies()](https://developer.apple.com/documentation/security/1398399-sectrustsetpolicies)Added [kSecPropertyTypeError](https://developer.apple.com/documentation/security/ksecpropertytypeerror)Added [kSecPropertyTypeTitle](https://developer.apple.com/documentation/security/ksecpropertytypetitle)Added [kSecTrustEvaluationDate](https://developer.apple.com/documentation/security/ksectrustevaluationdate)Added [kSecTrustExtendedValidation](https://developer.apple.com/documentation/security/ksectrustextendedvalidation)Added [kSecTrustOrganizationName](https://developer.apple.com/documentation/security/ksectrustorganizationname)Added [kSecTrustResultValue](https://developer.apple.com/documentation/security/ksectrustresultvalue)Added [kSecTrustRevocationChecked](https://developer.apple.com/documentation/security/ksectrustrevocationchecked)Added [kSecTrustRevocationValidUntilDate](https://developer.apple.com/documentation/security/ksectrustrevocationvaliduntildate)Modified [kSecTrustResultConfirm](https://developer.apple.com/documentation/security/sectrustresulttype/ksectrustresultconfirm)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

SecureTransport.hRemoved errSSLClientAuthCompletedRemoved errSSLLastRemoved [errSSLServerAuthCompleted](https://developer.apple.com/documentation/security/secure_transport/1503828-secure_transport_result_codes/errsslserverauthcompleted)Added #def errSSLClientAuthCompletedAdded #def errSSLLastAdded #def errSSLServerAuthCompletedAdded [kSSLSessionOptionFalseStart](https://developer.apple.com/documentation/security/sslsessionoption/falsestart)Added [kSSLSessionOptionSendOneByteRecord](https://developer.apple.com/documentation/security/sslsessionoption/sendonebyterecord)

## Social

SLRequest.hAdded [SLRequestMethodPUT](https://developer.apple.com/documentation/social/slrequestmethod/put)Modified [-[SLRequest addMultipartData:withName:type:filename:]](https://developer.apple.com/documentation/social/slrequest/1488593-addmultipartdata)

|  | Introduction |
| --- | --- |
| From | iOS 6.0 |
| To | _none_ |

SLServiceTypes.hAdded [SLServiceTypeTencentWeibo](https://developer.apple.com/documentation/social/slservicetypetencentweibo)

## SpriteKit

SKAction.hAdded [SKAction](https://developer.apple.com/documentation/spritekit/skaction)Added [+[SKAction animateWithTextures:timePerFrame:]](https://developer.apple.com/documentation/spritekit/skaction/1417828-animate)Added [+[SKAction animateWithTextures:timePerFrame:resize:restore:]](https://developer.apple.com/documentation/spritekit/skaction/1417656-animate)Added [+[SKAction colorizeWithColor:colorBlendFactor:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417678-colorizewithcolor)Added [+[SKAction colorizeWithColorBlendFactor:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417736-colorize)Added [+[SKAction customActionWithDuration:actionBlock:]](https://developer.apple.com/documentation/spritekit/skaction/1417745-customactionwithduration)Added [SKAction.duration](https://developer.apple.com/documentation/spritekit/skaction/1417790-duration)Added [+[SKAction fadeAlphaBy:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417716-fadealphaby)Added [+[SKAction fadeAlphaTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417673-fadealphato)Added [+[SKAction fadeInWithDuration:]](https://developer.apple.com/documentation/spritekit/skaction/1417818-fadein)Added [+[SKAction fadeOutWithDuration:]](https://developer.apple.com/documentation/spritekit/skaction/1417738-fadeoutwithduration)Added [+[SKAction followPath:asOffset:orientToPath:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417662-followpath)Added [+[SKAction followPath:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417822-follow)Added [+[SKAction group:]](https://developer.apple.com/documentation/spritekit/skaction/1417688-group)Added [+[SKAction moveBy:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417739-moveby)Added [+[SKAction moveByX:y:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417722-movebyx)Added [+[SKAction moveTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417768-moveto)Added [+[SKAction moveToX:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417779-moveto)Added [+[SKAction moveToY:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417781-movetoy)Added [+[SKAction performSelector:onTarget:]](https://developer.apple.com/documentation/spritekit/skaction/1417764-perform)Added [+[SKAction playSoundFileNamed:waitForCompletion:]](https://developer.apple.com/documentation/spritekit/skaction/1417664-playsoundfilenamed)Added [+[SKAction removeFromParent]](https://developer.apple.com/documentation/spritekit/skaction/1417748-removefromparent)Added [+[SKAction repeatAction:count:]](https://developer.apple.com/documentation/spritekit/skaction/1417750-repeat)Added [+[SKAction repeatActionForever:]](https://developer.apple.com/documentation/spritekit/skaction/1417676-repeatforever)Added [+[SKAction resizeByWidth:height:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417812-resize)Added [+[SKAction resizeToHeight:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417825-resizetoheight)Added [+[SKAction resizeToWidth:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417686-resizetowidth)Added [+[SKAction resizeToWidth:height:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417724-resizetowidth)Added [-[SKAction reversedAction]](https://developer.apple.com/documentation/spritekit/skaction/1417803-reversedaction)Added [+[SKAction rotateByAngle:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417805-rotate)Added [+[SKAction rotateToAngle:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417668-rotatetoangle)Added [+[SKAction rotateToAngle:duration:shortestUnitArc:]](https://developer.apple.com/documentation/spritekit/skaction/1417700-rotatetoangle)Added [+[SKAction runAction:onChildWithName:]](https://developer.apple.com/documentation/spritekit/skaction/1417671-run)Added [+[SKAction runBlock:]](https://developer.apple.com/documentation/spritekit/skaction/1417692-run)Added [+[SKAction runBlock:queue:]](https://developer.apple.com/documentation/spritekit/skaction/1417799-runblock)Added [+[SKAction scaleBy:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417741-scaleby)Added [+[SKAction scaleTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417712-scale)Added [+[SKAction scaleXBy:y:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417796-scalexby)Added [+[SKAction scaleXTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417699-scalex)Added [+[SKAction scaleXTo:y:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417728-scalexto)Added [+[SKAction scaleYTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417708-scaley)Added [+[SKAction sequence:]](https://developer.apple.com/documentation/spritekit/skaction/1417817-sequence)Added [+[SKAction setTexture:]](https://developer.apple.com/documentation/spritekit/skaction/1417784-settexture)Added [SKAction.speed](https://developer.apple.com/documentation/spritekit/skaction/1417718-speed)Added [+[SKAction speedBy:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417690-speedby)Added [+[SKAction speedTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417684-speedto)Added [SKAction.timingMode](https://developer.apple.com/documentation/spritekit/skaction/1417807-timingmode)Added [+[SKAction waitForDuration:]](https://developer.apple.com/documentation/spritekit/skaction/1417788-wait)Added [+[SKAction waitForDuration:withRange:]](https://developer.apple.com/documentation/spritekit/skaction/1417760-waitforduration)Added SKAction(SKActions)Added [SKActionTimingEaseIn](https://developer.apple.com/documentation/spritekit/skactiontimingmode/skactiontimingeasein)Added [SKActionTimingEaseInEaseOut](https://developer.apple.com/documentation/spritekit/skactiontimingmode/skactiontimingeaseineaseout)Added [SKActionTimingEaseOut](https://developer.apple.com/documentation/spritekit/skactiontimingmode/easeout)Added [SKActionTimingLinear](https://developer.apple.com/documentation/spritekit/skactiontimingmode/skactiontiminglinear)Added [SKActionTimingMode](https://developer.apple.com/documentation/spritekit/skactiontimingmode)SKCropNode.hAdded [SKCropNode](https://developer.apple.com/documentation/spritekit/skcropnode)Added [SKCropNode.maskNode](https://developer.apple.com/documentation/spritekit/skcropnode/1520449-masknode)SKEffectNode.hAdded [SKEffectNode](https://developer.apple.com/documentation/spritekit/skeffectnode)Added [SKEffectNode.blendMode](https://developer.apple.com/documentation/spritekit/skeffectnode/1459386-blendmode)Added [SKEffectNode.filter](https://developer.apple.com/documentation/spritekit/skeffectnode/1459392-filter)Added [SKEffectNode.shouldCenterFilter](https://developer.apple.com/documentation/spritekit/skeffectnode/1459390-shouldcenterfilter)Added [SKEffectNode.shouldEnableEffects](https://developer.apple.com/documentation/spritekit/skeffectnode/1459385-shouldenableeffects)Added [SKEffectNode.shouldRasterize](https://developer.apple.com/documentation/spritekit/skeffectnode/1459381-shouldrasterize)SKEmitterNode.hAdded [SKEmitterNode](https://developer.apple.com/documentation/spritekit/skemitternode)Added [-[SKEmitterNode advanceSimulationTime:]](https://developer.apple.com/documentation/spritekit/skemitternode/1398027-advancesimulationtime)Added [SKEmitterNode.emissionAngle](https://developer.apple.com/documentation/spritekit/skemitternode/1398035-emissionangle)Added [SKEmitterNode.emissionAngleRange](https://developer.apple.com/documentation/spritekit/skemitternode/1398067-emissionanglerange)Added [SKEmitterNode.numParticlesToEmit](https://developer.apple.com/documentation/spritekit/skemitternode/1398043-numparticlestoemit)Added [SKEmitterNode.particleAction](https://developer.apple.com/documentation/spritekit/skemitternode/1397970-particleaction)Added [SKEmitterNode.particleAlpha](https://developer.apple.com/documentation/spritekit/skemitternode/1397988-particlealpha)Added [SKEmitterNode.particleAlphaRange](https://developer.apple.com/documentation/spritekit/skemitternode/1398031-particlealpharange)Added [SKEmitterNode.particleAlphaSequence](https://developer.apple.com/documentation/spritekit/skemitternode/1398057-particlealphasequence)Added [SKEmitterNode.particleAlphaSpeed](https://developer.apple.com/documentation/spritekit/skemitternode/1398021-particlealphaspeed)Added [SKEmitterNode.particleBirthRate](https://developer.apple.com/documentation/spritekit/skemitternode/1398039-particlebirthrate)Added [SKEmitterNode.particleBlendMode](https://developer.apple.com/documentation/spritekit/skemitternode/1397978-particleblendmode)Added [SKEmitterNode.particleColor](https://developer.apple.com/documentation/spritekit/skemitternode/1398049-particlecolor)Added [SKEmitterNode.particleColorAlphaRange](https://developer.apple.com/documentation/spritekit/skemitternode/1397976-particlecoloralpharange)Added [SKEmitterNode.particleColorAlphaSpeed](https://developer.apple.com/documentation/spritekit/skemitternode/1398051-particlecoloralphaspeed)Added [SKEmitterNode.particleColorBlendFactor](https://developer.apple.com/documentation/spritekit/skemitternode/1398071-particlecolorblendfactor)Added [SKEmitterNode.particleColorBlendFactorRange](https://developer.apple.com/documentation/spritekit/skemitternode/1398047-particlecolorblendfactorrange)Added [SKEmitterNode.particleColorBlendFactorSequence](https://developer.apple.com/documentation/spritekit/skemitternode/1397980-particlecolorblendfactorsequence)Added [SKEmitterNode.particleColorBlendFactorSpeed](https://developer.apple.com/documentation/spritekit/skemitternode/1398037-particlecolorblendfactorspeed)Added [SKEmitterNode.particleColorBlueRange](https://developer.apple.com/documentation/spritekit/skemitternode/1398075-particlecolorbluerange)Added [SKEmitterNode.particleColorBlueSpeed](https://developer.apple.com/documentation/spritekit/skemitternode/1398023-particlecolorbluespeed)Added [SKEmitterNode.particleColorGreenRange](https://developer.apple.com/documentation/spritekit/skemitternode/1398065-particlecolorgreenrange)Added [SKEmitterNode.particleColorGreenSpeed](https://developer.apple.com/documentation/spritekit/skemitternode/1398033-particlecolorgreenspeed)Added [SKEmitterNode.particleColorRedRange](https://developer.apple.com/documentation/spritekit/skemitternode/1397998-particlecolorredrange)Added [SKEmitterNode.particleColorRedSpeed](https://developer.apple.com/documentation/spritekit/skemitternode/1398041-particlecolorredspeed)Added [SKEmitterNode.particleColorSequence](https://developer.apple.com/documentation/spritekit/skemitternode/1397992-particlecolorsequence)Added [SKEmitterNode.particleLifetime](https://developer.apple.com/documentation/spritekit/skemitternode/1398000-particlelifetime)Added [SKEmitterNode.particleLifetimeRange](https://developer.apple.com/documentation/spritekit/skemitternode/1397994-particlelifetimerange)Added [SKEmitterNode.particlePosition](https://developer.apple.com/documentation/spritekit/skemitternode/1398019-particleposition)Added [SKEmitterNode.particlePositionRange](https://developer.apple.com/documentation/spritekit/skemitternode/1397972-particlepositionrange)Added [SKEmitterNode.particleRotation](https://developer.apple.com/documentation/spritekit/skemitternode/1398025-particlerotation)Added [SKEmitterNode.particleRotationRange](https://developer.apple.com/documentation/spritekit/skemitternode/1397996-particlerotationrange)Added [SKEmitterNode.particleRotationSpeed](https://developer.apple.com/documentation/spritekit/skemitternode/1397968-particlerotationspeed)Added [SKEmitterNode.particleScale](https://developer.apple.com/documentation/spritekit/skemitternode/1398014-particlescale)Added [SKEmitterNode.particleScaleRange](https://developer.apple.com/documentation/spritekit/skemitternode/1397990-particlescalerange)Added [SKEmitterNode.particleScaleSequence](https://developer.apple.com/documentation/spritekit/skemitternode/1398029-particlescalesequence)Added [SKEmitterNode.particleScaleSpeed](https://developer.apple.com/documentation/spritekit/skemitternode/1398073-particlescalespeed)Added [SKEmitterNode.particleSize](https://developer.apple.com/documentation/spritekit/skemitternode/1398063-particlesize)Added [SKEmitterNode.particleSpeed](https://developer.apple.com/documentation/spritekit/skemitternode/1398061-particlespeed)Added [SKEmitterNode.particleSpeedRange](https://developer.apple.com/documentation/spritekit/skemitternode/1398045-particlespeedrange)Added [SKEmitterNode.particleTexture](https://developer.apple.com/documentation/spritekit/skemitternode/1398004-particletexture)Added [SKEmitterNode.particleZPosition](https://developer.apple.com/documentation/spritekit/skemitternode/1398055-particlezposition)Added [SKEmitterNode.particleZPositionRange](https://developer.apple.com/documentation/spritekit/skemitternode/1397974-particlezpositionrange)Added [-[SKEmitterNode resetSimulation]](https://developer.apple.com/documentation/spritekit/skemitternode/1398053-resetsimulation)Added [SKEmitterNode.targetNode](https://developer.apple.com/documentation/spritekit/skemitternode/1398012-targetnode)Added [SKEmitterNode.xAcceleration](https://developer.apple.com/documentation/spritekit/skemitternode/1398017-xacceleration)Added [SKEmitterNode.yAcceleration](https://developer.apple.com/documentation/spritekit/skemitternode/1397982-yacceleration)SKKeyframeSequence.hAdded [SKKeyframeSequence](https://developer.apple.com/documentation/spritekit/skkeyframesequence)Added [-[SKKeyframeSequence addKeyframeValue:time:]](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390894-addkeyframevalue)Added [-[SKKeyframeSequence count]](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390928-count)Added [-[SKKeyframeSequence getKeyframeTimeForIndex:]](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390908-getkeyframetimeforindex)Added [-[SKKeyframeSequence getKeyframeValueForIndex:]](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390898-getkeyframevalue)Added [-[SKKeyframeSequence initWithCapacity:]](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390910-init)Added [-[SKKeyframeSequence initWithKeyframeValues:times:]](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390896-init)Added [SKKeyframeSequence.interpolationMode](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390914-interpolationmode)Added [-[SKKeyframeSequence removeKeyframeAtIndex:]](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390920-removekeyframeatindex)Added [-[SKKeyframeSequence removeLastKeyframe]](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390912-removelastkeyframe)Added [SKKeyframeSequence.repeatMode](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390900-repeatmode)Added [-[SKKeyframeSequence sampleAtTime:]](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390904-sample)Added [-[SKKeyframeSequence setKeyframeTime:forIndex:]](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390924-setkeyframetime)Added [-[SKKeyframeSequence setKeyframeValue:forIndex:]](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390883-setkeyframevalue)Added [-[SKKeyframeSequence setKeyframeValue:time:forIndex:]](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390890-setkeyframevalue)Added [SKInterpolationMode](https://developer.apple.com/documentation/spritekit/skinterpolationmode)Added [SKInterpolationModeLinear](https://developer.apple.com/documentation/spritekit/skinterpolationmode/linear)Added [SKInterpolationModeSpline](https://developer.apple.com/documentation/spritekit/skinterpolationmode/spline)Added [SKInterpolationModeStep](https://developer.apple.com/documentation/spritekit/skinterpolationmode/step)Added [SKRepeatMode](https://developer.apple.com/documentation/spritekit/skrepeatmode)Added [SKRepeatModeClamp](https://developer.apple.com/documentation/spritekit/skrepeatmode/skrepeatmodeclamp)Added [SKRepeatModeLoop](https://developer.apple.com/documentation/spritekit/skrepeatmode/loop)SKLabelNode.hAdded [SKLabelNode](https://developer.apple.com/documentation/spritekit/sklabelnode)Added [SKLabelNode.blendMode](https://developer.apple.com/documentation/spritekit/sklabelnode/1519598-blendmode)Added [SKLabelNode.color](https://developer.apple.com/documentation/spritekit/sklabelnode/1519938-color)Added [SKLabelNode.colorBlendFactor](https://developer.apple.com/documentation/spritekit/sklabelnode/1519724-colorblendfactor)Added [SKLabelNode.fontColor](https://developer.apple.com/documentation/spritekit/sklabelnode/1520057-fontcolor)Added [SKLabelNode.fontName](https://developer.apple.com/documentation/spritekit/sklabelnode/1520129-fontname)Added [SKLabelNode.fontSize](https://developer.apple.com/documentation/spritekit/sklabelnode/1520208-fontsize)Added [SKLabelNode.horizontalAlignmentMode](https://developer.apple.com/documentation/spritekit/sklabelnode/1519711-horizontalalignmentmode)Added [-[SKLabelNode initWithFontNamed:]](https://developer.apple.com/documentation/spritekit/sklabelnode/1519917-initwithfontnamed)Added [+[SKLabelNode labelNodeWithFontNamed:]](https://developer.apple.com/documentation/spritekit/sklabelnode/1576448-labelnodewithfontnamed)Added [SKLabelNode.text](https://developer.apple.com/documentation/spritekit/sklabelnode/1519788-text)Added [SKLabelNode.verticalAlignmentMode](https://developer.apple.com/documentation/spritekit/sklabelnode/1519933-verticalalignmentmode)Added [SKLabelHorizontalAlignmentMode](https://developer.apple.com/documentation/spritekit/sklabelhorizontalalignmentmode)Added [SKLabelHorizontalAlignmentModeCenter](https://developer.apple.com/documentation/spritekit/sklabelhorizontalalignmentmode/sklabelhorizontalalignmentmodecenter)Added [SKLabelHorizontalAlignmentModeLeft](https://developer.apple.com/documentation/spritekit/sklabelhorizontalalignmentmode/sklabelhorizontalalignmentmodeleft)Added [SKLabelHorizontalAlignmentModeRight](https://developer.apple.com/documentation/spritekit/sklabelhorizontalalignmentmode/sklabelhorizontalalignmentmoderight)Added [SKLabelVerticalAlignmentMode](https://developer.apple.com/documentation/spritekit/sklabelverticalalignmentmode)Added [SKLabelVerticalAlignmentModeBaseline](https://developer.apple.com/documentation/spritekit/sklabelverticalalignmentmode/sklabelverticalalignmentmodebaseline)Added [SKLabelVerticalAlignmentModeBottom](https://developer.apple.com/documentation/spritekit/sklabelverticalalignmentmode/sklabelverticalalignmentmodebottom)Added [SKLabelVerticalAlignmentModeCenter](https://developer.apple.com/documentation/spritekit/sklabelverticalalignmentmode/sklabelverticalalignmentmodecenter)Added [SKLabelVerticalAlignmentModeTop](https://developer.apple.com/documentation/spritekit/sklabelverticalalignmentmode/sklabelverticalalignmentmodetop)SKNode.hAdded [SKNode](https://developer.apple.com/documentation/spritekit/sknode)Added [-[SKNode actionForKey:]](https://developer.apple.com/documentation/spritekit/sknode/1483138-action)Added [-[SKNode addChild:]](https://developer.apple.com/documentation/spritekit/sknode/1483054-addchild)Added [SKNode.alpha](https://developer.apple.com/documentation/spritekit/sknode/1483023-alpha)Added [-[SKNode calculateAccumulatedFrame]](https://developer.apple.com/documentation/spritekit/sknode/1483066-calculateaccumulatedframe)Added [-[SKNode childNodeWithName:]](https://developer.apple.com/documentation/spritekit/sknode/1483060-childnode)Added [SKNode.children](https://developer.apple.com/documentation/spritekit/sknode/1483028-children)Added [-[SKNode containsPoint:]](https://developer.apple.com/documentation/spritekit/sknode/1483044-containspoint)Added [-[SKNode convertPoint:fromNode:]](https://developer.apple.com/documentation/spritekit/sknode/1483058-convertpoint)Added [-[SKNode convertPoint:toNode:]](https://developer.apple.com/documentation/spritekit/sknode/1483056-convert)Added [-[SKNode enumerateChildNodesWithName:usingBlock:]](https://developer.apple.com/documentation/spritekit/sknode/1483024-enumeratechildnodeswithname)Added [SKNode.frame](https://developer.apple.com/documentation/spritekit/sknode/1483026-frame)Added [-[SKNode hasActions]](https://developer.apple.com/documentation/spritekit/sknode/1483081-hasactions)Added [SKNode.hidden](https://developer.apple.com/documentation/spritekit/sknode/1483048-hidden)Added [-[SKNode inParentHierarchy:]](https://developer.apple.com/documentation/spritekit/sknode/1483111-inparenthierarchy)Added [-[SKNode insertChild:atIndex:]](https://developer.apple.com/documentation/spritekit/sknode/1483062-insertchild)Added [-[SKNode intersectsNode:]](https://developer.apple.com/documentation/spritekit/sknode/1483140-intersects)Added [SKNode.name](https://developer.apple.com/documentation/spritekit/sknode/1483136-name)Added [+[SKNode node]](https://developer.apple.com/documentation/spritekit/sknode/1483038-node)Added [-[SKNode nodeAtPoint:]](https://developer.apple.com/documentation/spritekit/sknode/1483099-nodeatpoint)Added [-[SKNode nodesAtPoint:]](https://developer.apple.com/documentation/spritekit/sknode/1483072-nodes)Added [SKNode.parent](https://developer.apple.com/documentation/spritekit/sknode/1483080-parent)Added [SKNode.paused](https://developer.apple.com/documentation/spritekit/sknode/1483113-paused)Added [SKNode.physicsBody](https://developer.apple.com/documentation/spritekit/sknode/1483117-physicsbody)Added [SKNode.position](https://developer.apple.com/documentation/spritekit/sknode/1483101-position)Added [-[SKNode removeActionForKey:]](https://developer.apple.com/documentation/spritekit/sknode/1483076-removeactionforkey)Added [-[SKNode removeAllActions]](https://developer.apple.com/documentation/spritekit/sknode/1483030-removeallactions)Added [-[SKNode removeAllChildren]](https://developer.apple.com/documentation/spritekit/sknode/1483040-removeallchildren)Added [-[SKNode removeChildrenInArray:]](https://developer.apple.com/documentation/spritekit/sknode/1483091-removechildreninarray)Added [-[SKNode removeFromParent]](https://developer.apple.com/documentation/spritekit/sknode/1483119-removefromparent)Added [-[SKNode runAction:]](https://developer.apple.com/documentation/spritekit/sknode/1483093-runaction)Added [-[SKNode runAction:completion:]](https://developer.apple.com/documentation/spritekit/sknode/1483103-runaction)Added [-[SKNode runAction:withKey:]](https://developer.apple.com/documentation/spritekit/sknode/1483042-run)Added [SKNode.scene](https://developer.apple.com/documentation/spritekit/sknode/1483064-scene)Added [-[SKNode setScale:]](https://developer.apple.com/documentation/spritekit/sknode/1483126-setscale)Added [SKNode.speed](https://developer.apple.com/documentation/spritekit/sknode/1483036-speed)Added [SKNode.userData](https://developer.apple.com/documentation/spritekit/sknode/1483121-userdata)Added [SKNode.userInteractionEnabled](https://developer.apple.com/documentation/spritekit/sknode/1483109-userinteractionenabled)Added [SKNode.xScale](https://developer.apple.com/documentation/spritekit/sknode/1483087-xscale)Added [SKNode.yScale](https://developer.apple.com/documentation/spritekit/sknode/1483046-yscale)Added [SKNode.zPosition](https://developer.apple.com/documentation/spritekit/sknode/1483107-zposition)Added [SKNode.zRotation](https://developer.apple.com/documentation/spritekit/sknode/1483089-zrotation)Added [-[UITouch locationInNode:]](https://developer.apple.com/documentation/uikit/uitouch/1614836-location)Added [-[UITouch previousLocationInNode:]](https://developer.apple.com/documentation/uikit/uitouch/1615023-previouslocation)Added [SKBlendMode](https://developer.apple.com/documentation/spritekit/skblendmode)Added [SKBlendModeAdd](https://developer.apple.com/documentation/spritekit/skblendmode/skblendmodeadd)Added [SKBlendModeAlpha](https://developer.apple.com/documentation/spritekit/skblendmode/alpha)Added [SKBlendModeMultiply](https://developer.apple.com/documentation/spritekit/skblendmode/multiply)Added [SKBlendModeMultiplyX2](https://developer.apple.com/documentation/spritekit/skblendmode/multiplyx2)Added [SKBlendModeReplace](https://developer.apple.com/documentation/spritekit/skblendmode/replace)Added [SKBlendModeScreen](https://developer.apple.com/documentation/spritekit/skblendmode/screen)Added [SKBlendModeSubtract](https://developer.apple.com/documentation/spritekit/skblendmode/subtract)Added UITouch(SKNodeTouches)SKPhysicsBody.hAdded [SKPhysicsBody](https://developer.apple.com/documentation/spritekit/skphysicsbody)Added [SKPhysicsBody.affectedByGravity](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519774-affectedbygravity)Added [-[SKPhysicsBody allContactedBodies]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520397-allcontactedbodies)Added [SKPhysicsBody.allowsRotation](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519986-allowsrotation)Added [SKPhysicsBody.angularDamping](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519913-angulardamping)Added [SKPhysicsBody.angularVelocity](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519766-angularvelocity)Added [-[SKPhysicsBody applyAngularImpulse:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520122-applyangularimpulse)Added [-[SKPhysicsBody applyForce:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520430-applyforce)Added [-[SKPhysicsBody applyForce:atPoint:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520032-applyforce)Added [-[SKPhysicsBody applyImpulse:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519900-applyimpulse)Added [-[SKPhysicsBody applyImpulse:atPoint:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520407-applyimpulse)Added [-[SKPhysicsBody applyTorque:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519588-applytorque)Added [SKPhysicsBody.area](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520034-area)Added [+[SKPhysicsBody bodyWithCircleOfRadius:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520261-init)Added [+[SKPhysicsBody bodyWithEdgeChainFromPath:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519871-bodywithedgechainfrompath)Added [+[SKPhysicsBody bodyWithEdgeFromPoint:toPoint:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520401-bodywithedgefrompoint)Added [+[SKPhysicsBody bodyWithEdgeLoopFromPath:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519732-init)Added [+[SKPhysicsBody bodyWithEdgeLoopFromRect:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520055-bodywithedgeloopfromrect)Added [+[SKPhysicsBody bodyWithPolygonFromPath:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520379-bodywithpolygonfrompath)Added [+[SKPhysicsBody bodyWithRectangleOfSize:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520295-bodywithrectangleofsize)Added [SKPhysicsBody.categoryBitMask](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519869-categorybitmask)Added [SKPhysicsBody.collisionBitMask](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520003-collisionbitmask)Added [SKPhysicsBody.contactTestBitMask](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519781-contacttestbitmask)Added [SKPhysicsBody.density](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519983-density)Added [SKPhysicsBody.dynamic](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520132-isdynamic)Added [SKPhysicsBody.friction](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519840-friction)Added [SKPhysicsBody.joints](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519849-joints)Added [SKPhysicsBody.linearDamping](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519796-lineardamping)Added [SKPhysicsBody.mass](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519906-mass)Added [SKPhysicsBody.node](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520049-node)Added [SKPhysicsBody.resting](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520256-resting)Added [SKPhysicsBody.restitution](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520447-restitution)Added [SKPhysicsBody.usesPreciseCollisionDetection](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520014-usesprecisecollisiondetection)Added [SKPhysicsBody.velocity](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519635-velocity)SKPhysicsContact.hAdded [SKPhysicsContact](https://developer.apple.com/documentation/spritekit/skphysicscontact)Added [SKPhysicsContact.bodyA](https://developer.apple.com/documentation/spritekit/skphysicscontact/1478533-bodya)Added [SKPhysicsContact.bodyB](https://developer.apple.com/documentation/spritekit/skphysicscontact/1478526-bodyb)Added [SKPhysicsContact.collisionImpulse](https://developer.apple.com/documentation/spritekit/skphysicscontact/1478523-collisionimpulse)Added [SKPhysicsContact.contactPoint](https://developer.apple.com/documentation/spritekit/skphysicscontact/1478524-contactpoint)SKPhysicsJoint.hAdded [SKPhysicsJoint](https://developer.apple.com/documentation/spritekit/skphysicsjoint)Added [SKPhysicsJoint.bodyA](https://developer.apple.com/documentation/spritekit/skphysicsjoint/1520403-bodya)Added [SKPhysicsJoint.bodyB](https://developer.apple.com/documentation/spritekit/skphysicsjoint/1519693-bodyb)Added [SKPhysicsJointFixed](https://developer.apple.com/documentation/spritekit/skphysicsjointfixed)Added [+[SKPhysicsJointFixed jointWithBodyA:bodyB:anchor:]](https://developer.apple.com/documentation/spritekit/skphysicsjointfixed/1520076-joint)Added [SKPhysicsJointLimit](https://developer.apple.com/documentation/spritekit/skphysicsjointlimit)Added [+[SKPhysicsJointLimit jointWithBodyA:bodyB:anchorA:anchorB:]](https://developer.apple.com/documentation/spritekit/skphysicsjointlimit/1520402-jointwithbodya)Added [SKPhysicsJointLimit.maxLength](https://developer.apple.com/documentation/spritekit/skphysicsjointlimit/1519978-maxlength)Added [SKPhysicsJointPin](https://developer.apple.com/documentation/spritekit/skphysicsjointpin)Added [SKPhysicsJointPin.frictionTorque](https://developer.apple.com/documentation/spritekit/skphysicsjointpin/1520299-frictiontorque)Added [+[SKPhysicsJointPin jointWithBodyA:bodyB:anchor:]](https://developer.apple.com/documentation/spritekit/skphysicsjointpin/1519698-jointwithbodya)Added [SKPhysicsJointPin.lowerAngleLimit](https://developer.apple.com/documentation/spritekit/skphysicsjointpin/1520130-loweranglelimit)Added [SKPhysicsJointPin.shouldEnableLimits](https://developer.apple.com/documentation/spritekit/skphysicsjointpin/1520292-shouldenablelimits)Added [SKPhysicsJointPin.upperAngleLimit](https://developer.apple.com/documentation/spritekit/skphysicsjointpin/1519967-upperanglelimit)Added [SKPhysicsJointSliding](https://developer.apple.com/documentation/spritekit/skphysicsjointsliding)Added [+[SKPhysicsJointSliding jointWithBodyA:bodyB:anchor:axis:]](https://developer.apple.com/documentation/spritekit/skphysicsjointsliding/1520333-jointwithbodya)Added [SKPhysicsJointSliding.lowerDistanceLimit](https://developer.apple.com/documentation/spritekit/skphysicsjointsliding/1519969-lowerdistancelimit)Added [SKPhysicsJointSliding.shouldEnableLimits](https://developer.apple.com/documentation/spritekit/skphysicsjointsliding/1520053-shouldenablelimits)Added [SKPhysicsJointSliding.upperDistanceLimit](https://developer.apple.com/documentation/spritekit/skphysicsjointsliding/1519836-upperdistancelimit)Added [SKPhysicsJointSpring](https://developer.apple.com/documentation/spritekit/skphysicsjointspring)Added [SKPhysicsJointSpring.damping](https://developer.apple.com/documentation/spritekit/skphysicsjointspring/1519709-damping)Added [SKPhysicsJointSpring.frequency](https://developer.apple.com/documentation/spritekit/skphysicsjointspring/1519806-frequency)Added [+[SKPhysicsJointSpring jointWithBodyA:bodyB:anchorA:anchorB:]](https://developer.apple.com/documentation/spritekit/skphysicsjointspring/1519665-joint)SKPhysicsWorld.hAdded [SKPhysicsContactDelegate](https://developer.apple.com/documentation/spritekit/skphysicscontactdelegate)Added [-[SKPhysicsContactDelegate didBeginContact:]](https://developer.apple.com/documentation/spritekit/skphysicscontactdelegate/1449595-didbegin)Added [-[SKPhysicsContactDelegate didEndContact:]](https://developer.apple.com/documentation/spritekit/skphysicscontactdelegate/1449599-didendcontact)Added [SKPhysicsWorld](https://developer.apple.com/documentation/spritekit/skphysicsworld)Added [-[SKPhysicsWorld addJoint:]](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449617-add)Added [-[SKPhysicsWorld bodyAlongRayStart:end:]](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449613-bodyalongraystart)Added [-[SKPhysicsWorld bodyAtPoint:]](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449625-bodyatpoint)Added [-[SKPhysicsWorld bodyInRect:]](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449604-body)Added [SKPhysicsWorld.contactDelegate](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449602-contactdelegate)Added [-[SKPhysicsWorld enumerateBodiesAlongRayStart:end:usingBlock:]](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449615-enumeratebodies)Added [-[SKPhysicsWorld enumerateBodiesAtPoint:usingBlock:]](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449597-enumeratebodiesatpoint)Added [-[SKPhysicsWorld enumerateBodiesInRect:usingBlock:]](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449619-enumeratebodies)Added [SKPhysicsWorld.gravity](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449623-gravity)Added [-[SKPhysicsWorld removeAllJoints]](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449621-removealljoints)Added [-[SKPhysicsWorld removeJoint:]](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449609-remove)Added [SKPhysicsWorld.speed](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449611-speed)SKScene.hAdded [SKScene](https://developer.apple.com/documentation/spritekit/skscene)Added [SKScene.anchorPoint](https://developer.apple.com/documentation/spritekit/skscene/1519864-anchorpoint)Added [SKScene.backgroundColor](https://developer.apple.com/documentation/spritekit/skscene/1520278-backgroundcolor)Added [-[SKScene convertPointFromView:]](https://developer.apple.com/documentation/spritekit/skscene/1520395-convertpointfromview)Added [-[SKScene convertPointToView:]](https://developer.apple.com/documentation/spritekit/skscene/1520082-convertpointtoview)Added [-[SKScene didChangeSize:]](https://developer.apple.com/documentation/spritekit/skscene/1519545-didchangesize)Added [-[SKScene didEvaluateActions]](https://developer.apple.com/documentation/spritekit/skscene/1519903-didevaluateactions)Added [-[SKScene didMoveToView:]](https://developer.apple.com/documentation/spritekit/skscene/1519607-didmove)Added [-[SKScene didSimulatePhysics]](https://developer.apple.com/documentation/spritekit/skscene/1519965-didsimulatephysics)Added [-[SKScene initWithSize:]](https://developer.apple.com/documentation/spritekit/skscene/1520435-init)Added [SKScene.physicsWorld](https://developer.apple.com/documentation/spritekit/skscene/1519584-physicsworld)Added [SKScene.scaleMode](https://developer.apple.com/documentation/spritekit/skscene/1519562-scalemode)Added [+[SKScene sceneWithSize:]](https://developer.apple.com/documentation/spritekit/skscene/1536393-scenewithsize)Added [SKScene.size](https://developer.apple.com/documentation/spritekit/skscene/1519831-size)Added [-[SKScene update:]](https://developer.apple.com/documentation/spritekit/skscene/1519802-update)Added [SKScene.view](https://developer.apple.com/documentation/spritekit/skscene/1519726-view)Added [-[SKScene willMoveFromView:]](https://developer.apple.com/documentation/spritekit/skscene/1519703-willmovefromview)Added [SKSceneScaleMode](https://developer.apple.com/documentation/spritekit/skscenescalemode)Added [SKSceneScaleModeAspectFill](https://developer.apple.com/documentation/spritekit/skscenescalemode/skscenescalemodeaspectfill)Added [SKSceneScaleModeAspectFit](https://developer.apple.com/documentation/spritekit/skscenescalemode/skscenescalemodeaspectfit)Added [SKSceneScaleModeFill](https://developer.apple.com/documentation/spritekit/skscenescalemode/fill)Added [SKSceneScaleModeResizeFill](https://developer.apple.com/documentation/spritekit/skscenescalemode/skscenescalemoderesizefill)SKShapeNode.hAdded [SKShapeNode](https://developer.apple.com/documentation/spritekit/skshapenode)Added [SKShapeNode.antialiased](https://developer.apple.com/documentation/spritekit/skshapenode/1519719-antialiased)Added [SKShapeNode.blendMode](https://developer.apple.com/documentation/spritekit/skshapenode/1520045-blendmode)Added [SKShapeNode.fillColor](https://developer.apple.com/documentation/spritekit/skshapenode/1520154-fillcolor)Added [SKShapeNode.glowWidth](https://developer.apple.com/documentation/spritekit/skshapenode/1520116-glowwidth)Added [SKShapeNode.lineWidth](https://developer.apple.com/documentation/spritekit/skshapenode/1519885-linewidth)Added [SKShapeNode.path](https://developer.apple.com/documentation/spritekit/skshapenode/1519741-path)Added [SKShapeNode.strokeColor](https://developer.apple.com/documentation/spritekit/skshapenode/1519748-strokecolor)SKSpriteNode.hAdded [SKSpriteNode](https://developer.apple.com/documentation/spritekit/skspritenode)Added [SKSpriteNode.anchorPoint](https://developer.apple.com/documentation/spritekit/skspritenode/1519877-anchorpoint)Added [SKSpriteNode.blendMode](https://developer.apple.com/documentation/spritekit/skspritenode/1519931-blendmode)Added [SKSpriteNode.centerRect](https://developer.apple.com/documentation/spritekit/skspritenode/1520119-centerrect)Added [SKSpriteNode.color](https://developer.apple.com/documentation/spritekit/skspritenode/1519639-color)Added [SKSpriteNode.colorBlendFactor](https://developer.apple.com/documentation/spritekit/skspritenode/1519780-colorblendfactor)Added [-[SKSpriteNode initWithColor:size:]](https://developer.apple.com/documentation/spritekit/skspritenode/1519762-initwithcolor)Added [-[SKSpriteNode initWithImageNamed:]](https://developer.apple.com/documentation/spritekit/skspritenode/1520391-initwithimagenamed)Added [-[SKSpriteNode initWithTexture:]](https://developer.apple.com/documentation/spritekit/skspritenode/1519942-initwithtexture)Added [-[SKSpriteNode initWithTexture:color:size:]](https://developer.apple.com/documentation/spritekit/skspritenode/1520029-init)Added [SKSpriteNode.size](https://developer.apple.com/documentation/spritekit/skspritenode/1519668-size)Added [+[SKSpriteNode spriteNodeWithColor:size:]](https://developer.apple.com/documentation/spritekit/skspritenode/1579717-spritenodewithcolor)Added [+[SKSpriteNode spriteNodeWithImageNamed:]](https://developer.apple.com/documentation/spritekit/skspritenode/1579718-spritenodewithimagenamed)Added [+[SKSpriteNode spriteNodeWithTexture:]](https://developer.apple.com/documentation/spritekit/skspritenode/1579716-spritenodewithtexture)Added [+[SKSpriteNode spriteNodeWithTexture:size:]](https://developer.apple.com/documentation/spritekit/skspritenode/1519812-init)Added [SKSpriteNode.texture](https://developer.apple.com/documentation/spritekit/skspritenode/1520011-texture)SKTexture.hAdded [SKTexture](https://developer.apple.com/documentation/spritekit/sktexture)Added [SKTexture.filteringMode](https://developer.apple.com/documentation/spritekit/sktexture/1519659-filteringmode)Added [+[SKTexture preloadTextures:withCompletionHandler:]](https://developer.apple.com/documentation/spritekit/sktexture/1519817-preloadtextures)Added [-[SKTexture preloadWithCompletionHandler:]](https://developer.apple.com/documentation/spritekit/sktexture/1520172-preload)Added [-[SKTexture size]](https://developer.apple.com/documentation/spritekit/sktexture/1519772-size)Added [-[SKTexture textureByApplyingCIFilter:]](https://developer.apple.com/documentation/spritekit/sktexture/1520388-texturebyapplyingcifilter)Added [-[SKTexture textureRect]](https://developer.apple.com/documentation/spritekit/sktexture/1519707-texturerect)Added [+[SKTexture textureWithCGImage:]](https://developer.apple.com/documentation/spritekit/sktexture/1519576-init)Added [+[SKTexture textureWithData:size:]](https://developer.apple.com/documentation/spritekit/sktexture/1519962-texturewithdata)Added [+[SKTexture textureWithData:size:rowLength:alignment:]](https://developer.apple.com/documentation/spritekit/sktexture/1520181-texturewithdata)Added [+[SKTexture textureWithImage:]](https://developer.apple.com/documentation/spritekit/sktexture/1520136-init)Added [+[SKTexture textureWithImageNamed:]](https://developer.apple.com/documentation/spritekit/sktexture/1520086-texturewithimagenamed)Added [+[SKTexture textureWithRect:inTexture:]](https://developer.apple.com/documentation/spritekit/sktexture/1520425-texturewithrect)Added [SKTexture.usesMipmaps](https://developer.apple.com/documentation/spritekit/sktexture/1519960-usesmipmaps)Added [SKTextureFilteringLinear](https://developer.apple.com/documentation/spritekit/sktexturefilteringmode/sktexturefilteringlinear)Added [SKTextureFilteringMode](https://developer.apple.com/documentation/spritekit/sktexturefilteringmode)Added [SKTextureFilteringNearest](https://developer.apple.com/documentation/spritekit/sktexturefilteringmode/sktexturefilteringnearest)SKTextureAtlas.hAdded [SKTextureAtlas](https://developer.apple.com/documentation/spritekit/sktextureatlas)Added [+[SKTextureAtlas atlasNamed:]](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427381-atlasnamed)Added [+[SKTextureAtlas preloadTextureAtlases:withCompletionHandler:]](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427379-preloadtextureatlases)Added [-[SKTextureAtlas preloadWithCompletionHandler:]](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427385-preloadwithcompletionhandler)Added [-[SKTextureAtlas textureNamed:]](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427375-texturenamed)Added [SKTextureAtlas.textureNames](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427373-texturenames)SKTransition.hAdded [SKTransition](https://developer.apple.com/documentation/spritekit/sktransition)Added [+[SKTransition crossFadeWithDuration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395897-crossfade)Added [+[SKTransition doorsCloseHorizontalWithDuration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395899-doorsclosehorizontal)Added [+[SKTransition doorsCloseVerticalWithDuration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395914-doorscloseverticalwithduration)Added [+[SKTransition doorsOpenHorizontalWithDuration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395875-doorsopenhorizontalwithduration)Added [+[SKTransition doorsOpenVerticalWithDuration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395909-doorsopenverticalwithduration)Added [+[SKTransition doorwayWithDuration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395881-doorwaywithduration)Added [+[SKTransition fadeWithColor:duration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395871-fade)Added [+[SKTransition fadeWithDuration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395907-fadewithduration)Added [+[SKTransition flipHorizontalWithDuration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395901-fliphorizontalwithduration)Added [+[SKTransition flipVerticalWithDuration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395889-flipvertical)Added [+[SKTransition moveInWithDirection:duration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395905-moveinwithdirection)Added [SKTransition.pausesIncomingScene](https://developer.apple.com/documentation/spritekit/sktransition/1395883-pausesincomingscene)Added [SKTransition.pausesOutgoingScene](https://developer.apple.com/documentation/spritekit/sktransition/1395877-pausesoutgoingscene)Added [+[SKTransition pushWithDirection:duration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395903-push)Added [+[SKTransition revealWithDirection:duration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395887-reveal)Added [+[SKTransition transitionWithCIFilter:duration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395895-init)Added [SKTransitionDirection](https://developer.apple.com/documentation/spritekit/sktransitiondirection)Added [SKTransitionDirectionDown](https://developer.apple.com/documentation/spritekit/sktransitiondirection/sktransitiondirectiondown)Added [SKTransitionDirectionLeft](https://developer.apple.com/documentation/spritekit/sktransitiondirection/left)Added [SKTransitionDirectionRight](https://developer.apple.com/documentation/spritekit/sktransitiondirection/sktransitiondirectionright)Added [SKTransitionDirectionUp](https://developer.apple.com/documentation/spritekit/sktransitiondirection/up)SKVideoNode.hAdded [SKVideoNode](https://developer.apple.com/documentation/spritekit/skvideonode)Added [SKVideoNode.anchorPoint](https://developer.apple.com/documentation/spritekit/skvideonode/1407904-anchorpoint)Added [-[SKVideoNode initWithAVPlayer:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407900-init)Added [-[SKVideoNode initWithVideoFileNamed:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407918-init)Added [-[SKVideoNode initWithVideoURL:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407908-initwithvideourl)Added [-[SKVideoNode pause]](https://developer.apple.com/documentation/spritekit/skvideonode/1407910-pause)Added [-[SKVideoNode play]](https://developer.apple.com/documentation/spritekit/skvideonode/1407896-play)Added [SKVideoNode.size](https://developer.apple.com/documentation/spritekit/skvideonode/1407916-size)Added [+[SKVideoNode videoNodeWithAVPlayer:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407920-videonodewithavplayer)Added [+[SKVideoNode videoNodeWithVideoFileNamed:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407914-videonodewithvideofilenamed)Added [+[SKVideoNode videoNodeWithVideoURL:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407906-videonodewithvideourl)SKView.hAdded [SKView](https://developer.apple.com/documentation/spritekit/skview)Added [SKView.asynchronous](https://developer.apple.com/documentation/spritekit/skview/1520229-asynchronous)Added [-[SKView convertPoint:fromScene:]](https://developer.apple.com/documentation/spritekit/skview/1520328-convert)Added [-[SKView convertPoint:toScene:]](https://developer.apple.com/documentation/spritekit/skview/1519847-convert)Added [SKView.frameInterval](https://developer.apple.com/documentation/spritekit/skview/1520008-frameinterval)Added [SKView.ignoresSiblingOrder](https://developer.apple.com/documentation/spritekit/skview/1520215-ignoressiblingorder)Added [SKView.paused](https://developer.apple.com/documentation/spritekit/skview/1519654-ispaused)Added [-[SKView presentScene:]](https://developer.apple.com/documentation/spritekit/skview/1519705-presentscene)Added [-[SKView presentScene:transition:]](https://developer.apple.com/documentation/spritekit/skview/1520090-presentscene)Added [SKView.scene](https://developer.apple.com/documentation/spritekit/skview/1520084-scene)Added [SKView.showsDrawCount](https://developer.apple.com/documentation/spritekit/skview/1520112-showsdrawcount)Added [SKView.showsFPS](https://developer.apple.com/documentation/spritekit/skview/1519590-showsfps)Added [SKView.showsNodeCount](https://developer.apple.com/documentation/spritekit/skview/1520156-showsnodecount)Added [-[SKView textureFromNode:]](https://developer.apple.com/documentation/spritekit/skview/1520114-texture)SpriteKit.hSpriteKitBase.hAdded #def SKColor

## StoreKit

SKPayment.hAdded [SKMutablePayment.applicationUsername](https://developer.apple.com/documentation/storekit/skmutablepayment/1506088-applicationusername)Added [SKPayment.applicationUsername](https://developer.apple.com/documentation/storekit/skpayment/1506116-applicationusername)SKPaymentQueue.hAdded [-[SKPaymentQueue restoreCompletedTransactionsWithApplicationUsername:]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1505992-restorecompletedtransactions)SKPaymentTransaction.hModified [SKPaymentTransaction.transactionReceipt](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1617722-transactionreceipt)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

SKReceiptRefreshRequest.hAdded [SKReceiptRefreshRequest](https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest)Added [-[SKReceiptRefreshRequest initWithReceiptProperties:]](https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest/1506038-init)Added [SKReceiptRefreshRequest.receiptProperties](https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest/1506029-receiptproperties)Added [SKReceiptPropertyIsExpired](https://developer.apple.com/documentation/storekit/skreceiptpropertyisexpired)Added [SKReceiptPropertyIsRevoked](https://developer.apple.com/documentation/storekit/skreceiptpropertyisrevoked)Added [SKReceiptPropertyIsVolumePurchase](https://developer.apple.com/documentation/storekit/skreceiptpropertyisvolumepurchase)

## SystemConfiguration

No changes

## Twitter

No changes

## UIKit

NSAttributedString.hAdded [-[NSAttributedString dataFromRange:documentAttributes:error:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1534090-datafromrange)Added [-[NSAttributedString fileWrapperFromRange:documentAttributes:error:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1530461-filewrapperfromrange)Added [-[NSAttributedString initWithData:options:documentAttributes:error:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1524613-initwithdata)Added [-[NSAttributedString initWithFileURL:options:documentAttributes:error:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1620492-init)Added [-[NSMutableAttributedString fixAttributesInRange:]](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1533823-fixattributesinrange)Added [-[NSMutableAttributedString readFromData:options:documentAttributes:error:]](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1535465-readfromdata)Added [-[NSMutableAttributedString readFromFileURL:options:documentAttributes:error:]](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1620496-readfromfileurl)Added [NSAttachmentAttributeName](https://developer.apple.com/documentation/uikit/nsattachmentattributename)Added NSAttributedString(NSAttributedStringDocumentFormats)Added [NSBackgroundColorDocumentAttribute](https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/1532293-backgroundcolor)Added [NSBaselineOffsetAttributeName](https://developer.apple.com/documentation/appkit/nsbaselineoffsetattributename)Added [NSCharacterEncodingDocumentAttribute](https://developer.apple.com/documentation/appkit/nscharacterencodingdocumentattribute)Added [NSDefaultAttributesDocumentAttribute](https://developer.apple.com/documentation/appkit/nsdefaultattributesdocumentattribute)Added [NSDefaultTabIntervalDocumentAttribute](https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/1526177-defaulttabinterval)Added [NSDocumentTypeDocumentAttribute](https://developer.apple.com/documentation/uikit/nsdocumenttypedocumentattribute)Added [NSExpansionAttributeName](https://developer.apple.com/documentation/appkit/nsexpansionattributename)Added [NSHTMLTextDocumentType](https://developer.apple.com/documentation/appkit/nshtmltextdocumenttype)Added [NSHyphenationFactorDocumentAttribute](https://developer.apple.com/documentation/uikit/nshyphenationfactordocumentattribute)Added [NSLinkAttributeName](https://developer.apple.com/documentation/appkit/nslinkattributename)Added NSMutableAttributedString(NSMutableAttributedStringDocumentFormats)Added NSMutableAttributedString(NSMutableAttributedStringKitAdditions)Added [NSObliquenessAttributeName](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1535353-obliqueness)Added [NSPaperMarginDocumentAttribute](https://developer.apple.com/documentation/uikit/nspapermargindocumentattribute)Added [NSPaperSizeDocumentAttribute](https://developer.apple.com/documentation/uikit/nspapersizedocumentattribute)Added [NSPlainTextDocumentType](https://developer.apple.com/documentation/foundation/nsattributedstring/documenttype/1529054-plain)Added [NSRTFDTextDocumentType](https://developer.apple.com/documentation/appkit/nsrtfdtextdocumenttype)Added [NSRTFTextDocumentType](https://developer.apple.com/documentation/foundation/nsattributedstring/documenttype/1532538-rtf)Added [NSReadOnlyDocumentAttribute](https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/1532888-readonly)Added [NSStrikethroughColorAttributeName](https://developer.apple.com/documentation/uikit/nsstrikethroughcolorattributename)Added [NSTextEffectAttributeName](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1524319-texteffect)Added [NSTextEffectLetterpressStyle](https://developer.apple.com/documentation/foundation/nsattributedstring/texteffectstyle/1532217-letterpressstyle)Added [NSTextLayoutSectionOrientation](https://developer.apple.com/documentation/foundation/nsattributedstring/textlayoutsectionkey/1533613-orientation)Added [NSTextLayoutSectionRange](https://developer.apple.com/documentation/appkit/nstextlayoutsectionrange)Added [NSTextLayoutSectionsAttribute](https://developer.apple.com/documentation/appkit/nstextlayoutsectionsattribute)Added [NSTextWritingDirection](https://developer.apple.com/documentation/uikit/nstextwritingdirection)Added [NSTextWritingDirectionEmbedding](https://developer.apple.com/documentation/appkit/nstextwritingdirectionembedding)Added [NSTextWritingDirectionOverride](https://developer.apple.com/documentation/uikit/nstextwritingdirection/override)Added [NSUnderlineByWord](https://developer.apple.com/documentation/appkit/nsunderlinestylebyword)Added [NSUnderlineColorAttributeName](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1528834-underlinecolor)Added [NSUnderlinePatternDash](https://developer.apple.com/documentation/uikit/nsunderlinestylepatterndash)Added [NSUnderlinePatternDashDot](https://developer.apple.com/documentation/appkit/nsunderlinestylepatterndashdot)Added [NSUnderlinePatternDashDotDot](https://developer.apple.com/documentation/appkit/nsunderlinestyle/1524607-patterndashdotdot)Added [NSUnderlinePatternDot](https://developer.apple.com/documentation/uikit/nsunderlinestyle/1527165-patterndot)Added [NSUnderlinePatternSolid](https://developer.apple.com/documentation/uikit/nsunderlinestyle/nsunderlinestylepatternsolid)Added [NSUnderlineStyle](https://developer.apple.com/documentation/appkit/nsunderlinestyle)Added [NSUnderlineStyleDouble](https://developer.apple.com/documentation/uikit/nsunderlinestyle/1527838-double)Added [NSUnderlineStyleThick](https://developer.apple.com/documentation/uikit/nsunderlinestyle/1526911-thick)Added [NSViewModeDocumentAttribute](https://developer.apple.com/documentation/appkit/nsviewmodedocumentattribute)Added [NSViewSizeDocumentAttribute](https://developer.apple.com/documentation/appkit/nsviewsizedocumentattribute)Added [NSViewZoomDocumentAttribute](https://developer.apple.com/documentation/appkit/nsviewzoomdocumentattribute)Added [NSWritingDirectionAttributeName](https://developer.apple.com/documentation/appkit/nswritingdirectionattributename)NSLayoutConstraint.hAdded [UILayoutSupport](https://developer.apple.com/documentation/uikit/uilayoutsupport)Added [UILayoutSupport.length](https://developer.apple.com/documentation/uikit/uilayoutsupport/1622253-length)NSLayoutManager.hAdded [NSLayoutManager](https://developer.apple.com/documentation/appkit/nslayoutmanager)Added [-[NSLayoutManager addTextContainer:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1402946-addtextcontainer)Added [NSLayoutManager.allowsNonContiguousLayout](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403197-allowsnoncontiguouslayout)Added [-[NSLayoutManager attachmentSizeForGlyphAtIndex:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403099-attachmentsize)Added [-[NSLayoutManager boundingRectForGlyphRange:inTextContainer:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403255-boundingrect)Added [-[NSLayoutManager characterIndexForGlyphAtIndex:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1402944-characterindexforglyphatindex)Added [-[NSLayoutManager characterIndexForPoint:inTextContainer:fractionOfDistanceBetweenInsertionPoints:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403028-characterindex)Added [-[NSLayoutManager characterRangeForGlyphRange:actualGlyphRange:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403225-characterrangeforglyphrange)Added [NSLayoutManager.delegate](https://developer.apple.com/documentation/uikit/nslayoutmanager/1402920-delegate)Added [-[NSLayoutManager drawBackgroundForGlyphRange:atPoint:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1402949-drawbackground)Added [-[NSLayoutManager drawGlyphsForGlyphRange:atPoint:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403158-drawglyphsforglyphrange)Added [-[NSLayoutManager drawStrikethroughForGlyphRange:strikethroughType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403169-drawstrikethroughforglyphrange)Added [-[NSLayoutManager drawUnderlineForGlyphRange:underlineType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403079-drawunderlineforglyphrange)Added [-[NSLayoutManager drawsOutsideLineFragmentForGlyphAtIndex:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403003-drawsoutsidelinefragment)Added [-[NSLayoutManager ensureGlyphsForCharacterRange:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403189-ensureglyphsforcharacterrange)Added [-[NSLayoutManager ensureGlyphsForGlyphRange:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403219-ensureglyphsforglyphrange)Added [-[NSLayoutManager ensureLayoutForBoundingRect:inTextContainer:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1402962-ensurelayout)Added [-[NSLayoutManager ensureLayoutForCharacterRange:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1402986-ensurelayoutforcharacterrange)Added [-[NSLayoutManager ensureLayoutForGlyphRange:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1402939-ensurelayout)Added [-[NSLayoutManager ensureLayoutForTextContainer:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1402967-ensurelayout)Added [-[NSLayoutManager enumerateEnclosingRectsForGlyphRange:withinSelectedGlyphRange:inTextContainer:usingBlock:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403021-enumerateenclosingrects)Added [-[NSLayoutManager enumerateLineFragmentsForGlyphRange:usingBlock:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403160-enumeratelinefragments)Added [NSLayoutManager.extraLineFragmentRect](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403175-extralinefragmentrect)Added [NSLayoutManager.extraLineFragmentTextContainer](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403165-extralinefragmenttextcontainer)Added [NSLayoutManager.extraLineFragmentUsedRect](https://developer.apple.com/documentation/appkit/nslayoutmanager/1402988-extralinefragmentusedrect)Added [-[NSLayoutManager fillBackgroundRectArray:count:forCharacterRange:color:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403161-fillbackgroundrectarray)Added [-[NSLayoutManager firstUnlaidCharacterIndex]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403067-firstunlaidcharacterindex)Added [-[NSLayoutManager firstUnlaidGlyphIndex]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403245-firstunlaidglyphindex)Added [-[NSLayoutManager fractionOfDistanceThroughGlyphForPoint:inTextContainer:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403097-fractionofdistancethroughglyphfo)Added [-[NSLayoutManager getFirstUnlaidCharacterIndex:glyphIndex:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403187-getfirstunlaidcharacterindex)Added [-[NSLayoutManager getGlyphsInRange:glyphs:properties:characterIndexes:bidiLevels:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403104-getglyphs)Added [-[NSLayoutManager getLineFragmentInsertionPointsForCharacterAtIndex:alternatePositions:inDisplayOrder:positions:characterIndexes:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403012-getlinefragmentinsertionpoints)Added [-[NSLayoutManager glyphAtIndex:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403083-glyphatindex)Added [-[NSLayoutManager glyphAtIndex:isValidIndex:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403120-glyph)Added [-[NSLayoutManager glyphIndexForCharacterAtIndex:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403001-glyphindexforcharacter)Added [-[NSLayoutManager glyphIndexForPoint:inTextContainer:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403112-glyphindex)Added [-[NSLayoutManager glyphIndexForPoint:inTextContainer:fractionOfDistanceThroughGlyph:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1402933-glyphindexforpoint)Added [-[NSLayoutManager glyphRangeForBoundingRect:inTextContainer:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403053-glyphrange)Added [-[NSLayoutManager glyphRangeForBoundingRectWithoutAdditionalLayout:inTextContainer:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403183-glyphrange)Added [-[NSLayoutManager glyphRangeForCharacterRange:actualCharacterRange:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1402999-glyphrangeforcharacterrange)Added [-[NSLayoutManager glyphRangeForTextContainer:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403041-glyphrange)Added [NSLayoutManager.hasNonContiguousLayout](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403207-hasnoncontiguouslayout)Added [NSLayoutManager.hyphenationFactor](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403134-hyphenationfactor)Added [-[NSLayoutManager insertTextContainer:atIndex:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403010-inserttextcontainer)Added [-[NSLayoutManager invalidateDisplayForCharacterRange:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1402924-invalidatedisplayforcharacterran)Added [-[NSLayoutManager invalidateDisplayForGlyphRange:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403118-invalidatedisplay)Added [-[NSLayoutManager invalidateGlyphsForCharacterRange:changeInLength:actualCharacterRange:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403171-invalidateglyphsforcharacterrang)Added [-[NSLayoutManager invalidateLayoutForCharacterRange:actualCharacterRange:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403248-invalidatelayout)Added [-[NSLayoutManager isValidGlyphIndex:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1402950-isvalidglyphindex)Added [-[NSLayoutManager lineFragmentRectForGlyphAtIndex:effectiveRange:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403140-linefragmentrectforglyphatindex)Added [-[NSLayoutManager lineFragmentUsedRectForGlyphAtIndex:effectiveRange:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403193-linefragmentusedrect)Added [-[NSLayoutManager locationForGlyphAtIndex:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403239-locationforglyphatindex)Added [-[NSLayoutManager notShownAttributeForGlyphAtIndex:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1402931-notshownattributeforglyphatindex)Added [NSLayoutManager.numberOfGlyphs](https://developer.apple.com/documentation/uikit/nslayoutmanager/1402937-numberofglyphs)Added [-[NSLayoutManager processEditingForTextStorage:edited:range:changeInLength:invalidatedRange:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403065-processediting)Added [-[NSLayoutManager propertyForGlyphAtIndex:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403014-propertyforglyph)Added [-[NSLayoutManager rangeOfNominallySpacedGlyphsContainingIndex:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403152-range)Added [-[NSLayoutManager removeTextContainerAtIndex:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403017-removetextcontaineratindex)Added [-[NSLayoutManager setAttachmentSize:forGlyphRange:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403047-setattachmentsize)Added [-[NSLayoutManager setDrawsOutsideLineFragment:forGlyphAtIndex:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1402964-setdrawsoutsidelinefragment)Added [-[NSLayoutManager setExtraLineFragmentRect:usedRect:textContainer:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403071-setextralinefragmentrect)Added [-[NSLayoutManager setGlyphs:properties:characterIndexes:font:forGlyphRange:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403030-setglyphs)Added [-[NSLayoutManager setLineFragmentRect:forGlyphRange:usedRect:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1402935-setlinefragmentrect)Added [-[NSLayoutManager setLocation:forStartOfGlyphRange:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1402982-setlocation)Added [-[NSLayoutManager setNotShownAttribute:forGlyphAtIndex:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403078-setnotshownattribute)Added [-[NSLayoutManager setTextContainer:forGlyphRange:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403241-settextcontainer)Added [-[NSLayoutManager showCGGlyphs:positions:count:font:matrix:attributes:inContext:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403247-showcgglyphs)Added [NSLayoutManager.showsControlCharacters](https://developer.apple.com/documentation/uikit/nslayoutmanager/1402912-showscontrolcharacters)Added [NSLayoutManager.showsInvisibleCharacters](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403254-showsinvisiblecharacters)Added [-[NSLayoutManager strikethroughGlyphRange:strikethroughType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403009-strikethroughglyphrange)Added [-[NSLayoutManager textContainerChangedGeometry:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403091-textcontainerchangedgeometry)Added [-[NSLayoutManager textContainerForGlyphAtIndex:effectiveRange:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403110-textcontainerforglyphatindex)Added [NSLayoutManager.textContainers](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403144-textcontainers)Added [NSLayoutManager.textStorage](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403015-textstorage)Added [-[NSLayoutManager truncatedGlyphRangeInLineFragmentForGlyphAtIndex:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403203-truncatedglyphrangeinlinefragmen)Added [-[NSLayoutManager underlineGlyphRange:underlineType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403114-underlineglyphrange)Added [-[NSLayoutManager usedRectForTextContainer:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1402980-usedrectfortextcontainer)Added [NSLayoutManager.usesFontLeading](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403156-usesfontleading)Added [NSLayoutManagerDelegate](https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate)Added [-[NSLayoutManagerDelegate layoutManager:boundingBoxForControlGlyphAtIndex:forTextContainer:proposedLineFragment:glyphPosition:characterIndex:]](https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/1402922-layoutmanager)Added [-[NSLayoutManagerDelegate layoutManager:didCompleteLayoutForTextContainer:atEnd:]](https://developer.apple.com/documentation/appkit/nslayoutmanagerdelegate/1402926-layoutmanager)Added [-[NSLayoutManagerDelegate layoutManager:lineSpacingAfterGlyphAtIndex:withProposedLineFragmentRect:]](https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/1402948-layoutmanager)Added [-[NSLayoutManagerDelegate layoutManager:paragraphSpacingAfterGlyphAtIndex:withProposedLineFragmentRect:]](https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/1403076-layoutmanager)Added [-[NSLayoutManagerDelegate layoutManager:paragraphSpacingBeforeGlyphAtIndex:withProposedLineFragmentRect:]](https://developer.apple.com/documentation/appkit/nslayoutmanagerdelegate/1403177-layoutmanager)Added [-[NSLayoutManagerDelegate layoutManager:shouldBreakLineByHyphenatingBeforeCharacterAtIndex:]](https://developer.apple.com/documentation/appkit/nslayoutmanagerdelegate/1403128-layoutmanager)Added [-[NSLayoutManagerDelegate layoutManager:shouldBreakLineByWordBeforeCharacterAtIndex:]](https://developer.apple.com/documentation/appkit/nslayoutmanagerdelegate/1403051-layoutmanager)Added [-[NSLayoutManagerDelegate layoutManager:shouldGenerateGlyphs:properties:characterIndexes:font:forGlyphRange:]](https://developer.apple.com/documentation/appkit/nslayoutmanagerdelegate/1403073-layoutmanager)Added [-[NSLayoutManagerDelegate layoutManager:shouldUseAction:forControlCharacterAtIndex:]](https://developer.apple.com/documentation/appkit/nslayoutmanagerdelegate/1403167-layoutmanager)Added [-[NSLayoutManagerDelegate layoutManager:textContainer:didChangeGeometryFromSize:]](https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/1403049-layoutmanager)Added [-[NSLayoutManagerDelegate layoutManagerDidInvalidateLayout:]](https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/1402993-layoutmanagerdidinvalidatelayout)Added [NSTextLayoutOrientationProvider](https://developer.apple.com/documentation/appkit/nstextlayoutorientationprovider)Added [NSTextLayoutOrientationProvider.layoutOrientation](https://developer.apple.com/documentation/uikit/nstextlayoutorientationprovider/1402990-layoutorientation)Added [NSControlCharacterAction](https://developer.apple.com/documentation/uikit/nscontrolcharacteraction)Added [NSControlCharacterContainerBreakAction](https://developer.apple.com/documentation/uikit/1619233-anonymous/nscontrolcharactercontainerbreakaction)Added [NSControlCharacterHorizontalTabAction](https://developer.apple.com/documentation/uikit/nscontrolcharacterhorizontaltabaction)Added [NSControlCharacterLineBreakAction](https://developer.apple.com/documentation/uikit/1619233-anonymous/nscontrolcharacterlinebreakaction)Added [NSControlCharacterParagraphBreakAction](https://developer.apple.com/documentation/uikit/1619233-anonymous/nscontrolcharacterparagraphbreakaction)Added [NSControlCharacterWhitespaceAction](https://developer.apple.com/documentation/uikit/nscontrolcharacterwhitespaceaction)Added [NSControlCharacterZeroAdvancementAction](https://developer.apple.com/documentation/uikit/nscontrolcharacterzeroadvancementaction)Added [NSGlyphProperty](https://developer.apple.com/documentation/appkit/nslayoutmanager/glyphproperty)Added [NSGlyphPropertyControlCharacter](https://developer.apple.com/documentation/uikit/nsglyphproperty/nsglyphpropertycontrolcharacter)Added [NSGlyphPropertyElastic](https://developer.apple.com/documentation/appkit/nsglyphproperty/nsglyphpropertyelastic)Added [NSGlyphPropertyNonBaseCharacter](https://developer.apple.com/documentation/uikit/nslayoutmanager/glyphproperty/1403108-nonbasecharacter)Added [NSGlyphPropertyNull](https://developer.apple.com/documentation/appkit/nslayoutmanager/glyphproperty/1402918-null)Added [NSTextLayoutOrientation](https://developer.apple.com/documentation/uikit/nstextlayoutorientation)Added [NSTextLayoutOrientationHorizontal](https://developer.apple.com/documentation/appkit/nstextlayoutorientation/nstextlayoutorientationhorizontal)Added [NSTextLayoutOrientationVertical](https://developer.apple.com/documentation/uikit/nslayoutmanager/textlayoutorientation/vertical)NSParagraphStyle.hAdded [NSMutableParagraphStyle.defaultTabInterval](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1529861-defaulttabinterval)Added [NSMutableParagraphStyle.tabStops](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1531988-tabstops)Added [NSParagraphStyle.defaultTabInterval](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1535614-defaulttabinterval)Added [NSParagraphStyle.tabStops](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1532841-tabstops)Added [NSTextTab](https://developer.apple.com/documentation/uikit/nstexttab)Added [NSTextTab.alignment](https://developer.apple.com/documentation/appkit/nstexttab/1527212-alignment)Added [+[NSTextTab columnTerminatorsForLocale:]](https://developer.apple.com/documentation/uikit/nstexttab/1535107-columnterminatorsforlocale)Added [-[NSTextTab initWithTextAlignment:location:options:]](https://developer.apple.com/documentation/uikit/nstexttab/1526080-init)Added [NSTextTab.location](https://developer.apple.com/documentation/appkit/nstexttab/1527968-location)Added [NSTextTab.options](https://developer.apple.com/documentation/appkit/nstexttab/1534965-options)Added [NSTabColumnTerminatorsAttributeName](https://developer.apple.com/documentation/appkit/nstabcolumnterminatorsattributename)NSStringDrawing.hAdded [-[NSString boundingRectWithSize:options:attributes:context:]](https://developer.apple.com/documentation/foundation/nsstring/1524729-boundingrect)Added [-[NSString drawAtPoint:withAttributes:]](https://developer.apple.com/documentation/foundation/nsstring/1533109-drawatpoint)Added [-[NSString drawInRect:withAttributes:]](https://developer.apple.com/documentation/foundation/nsstring/1529855-drawinrect)Added [-[NSString drawWithRect:options:attributes:context:]](https://developer.apple.com/documentation/foundation/nsstring/1530195-drawwithrect)Added [-[NSString sizeWithAttributes:]](https://developer.apple.com/documentation/foundation/nsstring/1531844-size)Added NSString(NSExtendedStringDrawing)Added NSString(NSStringDrawing)Modified [NSStringDrawingContext.actualTrackingAdjustment](https://developer.apple.com/documentation/uikit/nsstringdrawingcontext/1624042-actualtrackingadjustment)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [NSStringDrawingContext.minimumTrackingAdjustment](https://developer.apple.com/documentation/uikit/nsstringdrawingcontext/1624043-minimumtrackingadjustment)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

NSTextAttachment.hAdded [+[NSAttributedString attributedStringWithAttachment:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1508376-init)Added [NSTextAttachment](https://developer.apple.com/documentation/appkit/nstextattachment)Added [NSTextAttachment.bounds](https://developer.apple.com/documentation/uikit/nstextattachment/1508394-bounds)Added [NSTextAttachment.contents](https://developer.apple.com/documentation/appkit/nstextattachment/1508401-contents)Added [NSTextAttachment.fileType](https://developer.apple.com/documentation/uikit/nstextattachment/1508416-filetype)Added [NSTextAttachment.fileWrapper](https://developer.apple.com/documentation/uikit/nstextattachment/1508398-filewrapper)Added [NSTextAttachment.image](https://developer.apple.com/documentation/uikit/nstextattachment/1508378-image)Added [-[NSTextAttachment initWithData:ofType:]](https://developer.apple.com/documentation/appkit/nstextattachment/1508374-init)Added [NSTextAttachmentContainer](https://developer.apple.com/documentation/uikit/nstextattachmentcontainer)Added [-[NSTextAttachmentContainer attachmentBoundsForTextContainer:proposedLineFragment:glyphPosition:characterIndex:]](https://developer.apple.com/documentation/uikit/nstextattachmentcontainer/1508382-attachmentbounds)Added [-[NSTextAttachmentContainer imageForBounds:textContainer:characterIndex:]](https://developer.apple.com/documentation/appkit/nstextattachmentcontainer/1508386-imageforbounds)Added [NSAttachmentCharacter](https://developer.apple.com/documentation/uikit/1508411-attachment_character/nsattachmentcharacter)Added NSAttributedString(NSAttributedStringAttachmentConveniences)NSTextContainer.hAdded [NSTextContainer](https://developer.apple.com/documentation/appkit/nstextcontainer)Added [NSTextContainer.exclusionPaths](https://developer.apple.com/documentation/uikit/nstextcontainer/1444569-exclusionpaths)Added [NSTextContainer.heightTracksTextView](https://developer.apple.com/documentation/appkit/nstextcontainer/1444559-heighttrackstextview)Added [-[NSTextContainer initWithSize:]](https://developer.apple.com/documentation/uikit/nstextcontainer/1444529-init)Added [NSTextContainer.layoutManager](https://developer.apple.com/documentation/uikit/nstextcontainer/1444517-layoutmanager)Added [NSTextContainer.lineBreakMode](https://developer.apple.com/documentation/appkit/nstextcontainer/1444519-linebreakmode)Added [NSTextContainer.lineFragmentPadding](https://developer.apple.com/documentation/uikit/nstextcontainer/1444527-linefragmentpadding)Added [-[NSTextContainer lineFragmentRectForProposedRect:atIndex:writingDirection:remainingRect:]](https://developer.apple.com/documentation/appkit/nstextcontainer/1444555-linefragmentrect)Added [NSTextContainer.maximumNumberOfLines](https://developer.apple.com/documentation/appkit/nstextcontainer/1444531-maximumnumberoflines)Added [NSTextContainer.size](https://developer.apple.com/documentation/uikit/nstextcontainer/1444553-size)Added [NSTextContainer.widthTracksTextView](https://developer.apple.com/documentation/uikit/nstextcontainer/1444563-widthtrackstextview)NSTextStorage.hAdded [NSTextStorage](https://developer.apple.com/documentation/uikit/nstextstorage)Added [-[NSTextStorage addLayoutManager:]](https://developer.apple.com/documentation/appkit/nstextstorage/1533459-addlayoutmanager)Added [NSTextStorage.changeInLength](https://developer.apple.com/documentation/uikit/nstextstorage/1528400-changeinlength)Added [NSTextStorage.delegate](https://developer.apple.com/documentation/uikit/nstextstorage/1532704-delegate)Added [-[NSTextStorage edited:range:changeInLength:]](https://developer.apple.com/documentation/appkit/nstextstorage/1529793-edited)Added [NSTextStorage.editedMask](https://developer.apple.com/documentation/appkit/nstextstorage/1525323-editedmask)Added [NSTextStorage.editedRange](https://developer.apple.com/documentation/appkit/nstextstorage/1524379-editedrange)Added [-[NSTextStorage ensureAttributesAreFixedInRange:]](https://developer.apple.com/documentation/appkit/nstextstorage/1533947-ensureattributesarefixedinrange)Added [NSTextStorage.fixesAttributesLazily](https://developer.apple.com/documentation/uikit/nstextstorage/1532043-fixesattributeslazily)Added [-[NSTextStorage invalidateAttributesInRange:]](https://developer.apple.com/documentation/uikit/nstextstorage/1534025-invalidateattributesinrange)Added [NSTextStorage.layoutManagers](https://developer.apple.com/documentation/uikit/nstextstorage/1527938-layoutmanagers)Added [-[NSTextStorage processEditing]](https://developer.apple.com/documentation/appkit/nstextstorage/1525980-processediting)Added [-[NSTextStorage removeLayoutManager:]](https://developer.apple.com/documentation/appkit/nstextstorage/1528755-removelayoutmanager)Added [NSTextStorageDelegate](https://developer.apple.com/documentation/appkit/nstextstoragedelegate)Added [-[NSTextStorageDelegate textStorage:didProcessEditing:range:changeInLength:]](https://developer.apple.com/documentation/uikit/nstextstoragedelegate/1534375-textstorage)Added [-[NSTextStorageDelegate textStorage:willProcessEditing:range:changeInLength:]](https://developer.apple.com/documentation/uikit/nstextstoragedelegate/1534795-textstorage)Added [NSTextStorageDidProcessEditingNotification](https://developer.apple.com/documentation/uikit/nstextstorage/1525483-didprocesseditingnotification)Added [NSTextStorageEditActions](https://developer.apple.com/documentation/appkit/nstextstorageeditactions)Added [NSTextStorageEditedAttributes](https://developer.apple.com/documentation/uikit/nstextstorage/editactions/1532736-editedattributes)Added [NSTextStorageEditedCharacters](https://developer.apple.com/documentation/uikit/nstextstorageeditactions/nstextstorageeditedcharacters)Added [NSTextStorageWillProcessEditingNotification](https://developer.apple.com/documentation/appkit/nstextstorage/1529695-willprocesseditingnotification)UIAccelerometer.hModified [UIAcceleration](https://developer.apple.com/documentation/uikit/uiacceleration)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

Modified [UIAccelerometer](https://developer.apple.com/documentation/uikit/uiaccelerometer)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

UIAccessibility.hAdded [-[NSObject accessibilityActivate]](https://developer.apple.com/documentation/objectivec/nsobject/1615165-accessibilityactivate)Added [NSObject.accessibilityPath](https://developer.apple.com/documentation/objectivec/nsobject/1615159-accessibilitypath)Added [UIAccessibilityConvertFrameToScreenCoordinates()](https://developer.apple.com/documentation/uikit/1615145-uiaccessibilityconvertframetoscr)Added [UIAccessibilityConvertPathToScreenCoordinates()](https://developer.apple.com/documentation/uikit/uiaccessibility/1615139-converttoscreencoordinates)Added [UIAccessibilityRequestGuidedAccessSession()](https://developer.apple.com/documentation/uikit/uiaccessibility/1615186-requestguidedaccesssession)UIAccessibilityConstants.hAdded [UIAccessibilitySpeechAttributeLanguage](https://developer.apple.com/documentation/uikit/uiaccessibilityspeechattributelanguage)Added [UIAccessibilitySpeechAttributePitch](https://developer.apple.com/documentation/uikit/uiaccessibilityspeechattributepitch)Added [UIAccessibilitySpeechAttributePunctuation](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1620201-accessibilityspeechpunctuation)UIActivity.hAdded [+[UIActivity activityCategory]](https://developer.apple.com/documentation/uikit/uiactivity/1620656-activitycategory)Added [UIActivityCategory](https://developer.apple.com/documentation/uikit/uiactivitycategory)Added [UIActivityCategoryAction](https://developer.apple.com/documentation/uikit/uiactivity/category/action)Added [UIActivityCategoryShare](https://developer.apple.com/documentation/uikit/uiactivitycategory/uiactivitycategoryshare)Added [UIActivityTypeAddToReadingList](https://developer.apple.com/documentation/uikit/uiactivity/activitytype/1620667-addtoreadinglist)Added [UIActivityTypeAirDrop](https://developer.apple.com/documentation/uikit/uiactivitytypeairdrop)Added [UIActivityTypePostToFlickr](https://developer.apple.com/documentation/uikit/uiactivity/activitytype/1620664-posttoflickr)Added [UIActivityTypePostToTencentWeibo](https://developer.apple.com/documentation/uikit/uiactivitytypeposttotencentweibo)Added [UIActivityTypePostToVimeo](https://developer.apple.com/documentation/uikit/uiactivity/activitytype/1620683-posttovimeo)UIActivityItemProvider.hAdded [-[UIActivityItemSource activityViewController:dataTypeIdentifierForActivityType:]](https://developer.apple.com/documentation/uikit/uiactivityitemsource/1620456-activityviewcontroller)Added [-[UIActivityItemSource activityViewController:subjectForActivityType:]](https://developer.apple.com/documentation/uikit/uiactivityitemsource/1620455-activityviewcontroller)Added [-[UIActivityItemSource activityViewController:thumbnailImageForActivityType:suggestedSize:]](https://developer.apple.com/documentation/uikit/uiactivityitemsource/1620462-activityviewcontroller)UIAppearance.hModified [+[UIAppearance appearance]](https://developer.apple.com/documentation/uikit/uiappearance/1615010-appearance)

|  | Declaration |
| --- | --- |
| From | + (id)appearance |
| To | + (instancetype)appearance |

Modified [+[UIAppearance appearanceWhenContainedIn:]](https://developer.apple.com/documentation/uikit/uiappearance/1615006-appearancewhencontainedin)

|  | Declaration |
| --- | --- |
| From | + (id)appearanceWhenContainedIn:(Class<UIAppearanceContainer> \*)ContainerClass, ... |
| To | + (instancetype)appearanceWhenContainedIn:(Class<UIAppearanceContainer> \*)ContainerClass, ... |

UIApplication.hAdded [UIApplication.backgroundRefreshStatus](https://developer.apple.com/documentation/uikit/uiapplication/1622994-backgroundrefreshstatus)Added [-[UIApplication beginBackgroundTaskWithName:expirationHandler:]](https://developer.apple.com/documentation/uikit/uiapplication/1623051-beginbackgroundtask)Added [-[UIApplication ignoreSnapshotOnNextApplicationLaunch]](https://developer.apple.com/documentation/uikit/uiapplication/1623097-ignoresnapshotonnextapplicationl)Added [UIApplication.preferredContentSizeCategory](https://developer.apple.com/documentation/uikit/uiapplication/1623048-preferredcontentsizecategory)Added [+[UIApplication registerObjectForStateRestoration:restorationIdentifier:]](https://developer.apple.com/documentation/uikit/uiapplication/1623027-registerobject)Added [-[UIApplication setMinimumBackgroundFetchInterval:]](https://developer.apple.com/documentation/uikit/uiapplication/1623100-setminimumbackgroundfetchinterva)Added [-[UIApplicationDelegate application:didReceiveRemoteNotification:fetchCompletionHandler:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application)Added [-[UIApplicationDelegate application:handleEventsForBackgroundURLSession:completionHandler:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622941-application)Added [-[UIApplicationDelegate application:performFetchWithCompletionHandler:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623125-application)Added [UIApplicationBackgroundFetchIntervalMinimum](https://developer.apple.com/documentation/uikit/uiapplicationbackgroundfetchintervalminimum)Added [UIApplicationBackgroundFetchIntervalNever](https://developer.apple.com/documentation/uikit/uiapplication/1623023-backgroundfetchintervalnever)Added [UIApplicationBackgroundRefreshStatusDidChangeNotification](https://developer.apple.com/documentation/uikit/uiapplicationbackgroundrefreshstatusdidchangenotification)Added [UIApplicationLaunchOptionsBluetoothCentralsKey](https://developer.apple.com/documentation/uikit/uiapplication/launchoptionskey/1622965-bluetoothcentrals)Added [UIApplicationLaunchOptionsBluetoothPeripheralsKey](https://developer.apple.com/documentation/uikit/uiapplication/launchoptionskey/1623116-bluetoothperipherals)Added [UIApplicationUserDidTakeScreenshotNotification](https://developer.apple.com/documentation/uikit/uiapplication/1622966-userdidtakescreenshotnotificatio)Added [UIBackgroundFetchResult](https://developer.apple.com/documentation/uikit/uibackgroundfetchresult)Added [UIBackgroundFetchResultFailed](https://developer.apple.com/documentation/uikit/uibackgroundfetchresult/failed)Added [UIBackgroundFetchResultNewData](https://developer.apple.com/documentation/uikit/uibackgroundfetchresult/uibackgroundfetchresultnewdata)Added [UIBackgroundFetchResultNoData](https://developer.apple.com/documentation/uikit/uibackgroundfetchresult/nodata)Added [UIBackgroundRefreshStatus](https://developer.apple.com/documentation/uikit/uibackgroundrefreshstatus)Added [UIBackgroundRefreshStatusAvailable](https://developer.apple.com/documentation/uikit/uibackgroundrefreshstatus/uibackgroundrefreshstatusavailable)Added [UIBackgroundRefreshStatusDenied](https://developer.apple.com/documentation/uikit/uibackgroundrefreshstatus/denied)Added [UIBackgroundRefreshStatusRestricted](https://developer.apple.com/documentation/uikit/uibackgroundrefreshstatus/uibackgroundrefreshstatusrestricted)Added [UIContentSizeCategoryAccessibilityExtraExtraExtraLarge](https://developer.apple.com/documentation/uikit/uicontentsizecategoryaccessibilityextraextraextralarge)Added [UIContentSizeCategoryAccessibilityExtraExtraLarge](https://developer.apple.com/documentation/uikit/uicontentsizecategoryaccessibilityextraextralarge)Added [UIContentSizeCategoryAccessibilityExtraLarge](https://developer.apple.com/documentation/uikit/uicontentsizecategoryaccessibilityextralarge)Added [UIContentSizeCategoryAccessibilityLarge](https://developer.apple.com/documentation/uikit/uicontentsizecategoryaccessibilitylarge)Added [UIContentSizeCategoryAccessibilityMedium](https://developer.apple.com/documentation/uikit/uicontentsizecategoryaccessibilitymedium)Added [UIContentSizeCategoryDidChangeNotification](https://developer.apple.com/documentation/uikit/uicontentsizecategorydidchangenotification)Added [UIContentSizeCategoryExtraExtraExtraLarge](https://developer.apple.com/documentation/uikit/uicontentsizecategoryextraextraextralarge)Added [UIContentSizeCategoryExtraExtraLarge](https://developer.apple.com/documentation/uikit/uicontentsizecategory/1623007-extraextralarge)Added [UIContentSizeCategoryExtraLarge](https://developer.apple.com/documentation/uikit/uicontentsizecategory/1622960-extralarge)Added [UIContentSizeCategoryExtraSmall](https://developer.apple.com/documentation/uikit/uicontentsizecategoryextrasmall)Added [UIContentSizeCategoryLarge](https://developer.apple.com/documentation/uikit/uicontentsizecategorylarge)Added [UIContentSizeCategoryMedium](https://developer.apple.com/documentation/uikit/uicontentsizecategory/1622928-medium)Added [UIContentSizeCategoryNewValueKey](https://developer.apple.com/documentation/uikit/uicontentsizecategorynewvaluekey)Added [UIContentSizeCategorySmall](https://developer.apple.com/documentation/uikit/uicontentsizecategorysmall)Added [UIStatusBarStyleLightContent](https://developer.apple.com/documentation/uikit/uistatusbarstyle/lightcontent)Modified [UIStatusBarStyleBlackOpaque](https://developer.apple.com/documentation/uikit/uistatusbarstyle/uistatusbarstyleblackopaque)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [UIStatusBarStyleBlackTranslucent](https://developer.apple.com/documentation/uikit/uistatusbarstyle/uistatusbarstyleblacktranslucent)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

UIAttachmentBehavior.hAdded [UIAttachmentBehavior](https://developer.apple.com/documentation/uikit/uiattachmentbehavior)Added [UIAttachmentBehavior.anchorPoint](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621315-anchorpoint)Added [UIAttachmentBehavior.attachedBehaviorType](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621312-attachedbehaviortype)Added [UIAttachmentBehavior.damping](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621302-damping)Added [UIAttachmentBehavior.frequency](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621321-frequency)Added [-[UIAttachmentBehavior initWithItem:attachedToAnchor:]](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621297-initwithitem)Added [-[UIAttachmentBehavior initWithItem:attachedToItem:]](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621309-init)Added [-[UIAttachmentBehavior initWithItem:offsetFromCenter:attachedToAnchor:]](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621301-initwithitem)Added [-[UIAttachmentBehavior initWithItem:offsetFromCenter:attachedToItem:offsetFromCenter:]](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621298-initwithitem)Added [UIAttachmentBehavior.items](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621311-items)Added [UIAttachmentBehavior.length](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621304-length)Added [UIAttachmentBehaviorType](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/attachmenttype)Added [UIAttachmentBehaviorTypeAnchor](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/attachmenttype/anchor)Added [UIAttachmentBehaviorTypeItems](https://developer.apple.com/documentation/uikit/uiattachmentbehaviortype/uiattachmentbehaviortypeitems)UIBarButtonItem.hModified [UIBarMetrics](https://developer.apple.com/documentation/uikit/uibarmetrics)

|  | Header |
| --- | --- |
| From | UIKit/UIBarButtonItem.h |
| To | UIKit/UIBarCommon.h |

Modified [UIBarMetricsDefault](https://developer.apple.com/documentation/uikit/uibarmetrics/default)

|  | Header |
| --- | --- |
| From | UIKit/UIBarButtonItem.h |
| To | UIKit/UIBarCommon.h |

Modified [UIBarMetricsLandscapePhone](https://developer.apple.com/documentation/uikit/uibarmetrics/1624859-landscapephone)

|  | Header |
| --- | --- |
| From | UIKit/UIBarButtonItem.h |
| To | UIKit/UIBarCommon.h |

UIBarCommon.hAdded [UIBarPositioning](https://developer.apple.com/documentation/uikit/uibarpositioning)Added [UIBarPositioning.barPosition](https://developer.apple.com/documentation/uikit/uibarpositioning/1624857-barposition)Added [UIBarPositioningDelegate](https://developer.apple.com/documentation/uikit/uibarpositioningdelegate)Added [-[UIBarPositioningDelegate positionForBar:]](https://developer.apple.com/documentation/uikit/uibarpositioningdelegate/1624872-positionforbar)Added [UIBarMetricsDefaultPrompt](https://developer.apple.com/documentation/uikit/uibarmetrics/defaultprompt)Added [UIBarMetricsLandscapePhonePrompt](https://developer.apple.com/documentation/uikit/uibarmetrics/uibarmetricslandscapephoneprompt)Added [UIBarPosition](https://developer.apple.com/documentation/uikit/uibarposition)Added [UIBarPositionAny](https://developer.apple.com/documentation/uikit/uibarposition/uibarpositionany)Added [UIBarPositionBottom](https://developer.apple.com/documentation/uikit/uibarposition/uibarpositionbottom)Added [UIBarPositionTop](https://developer.apple.com/documentation/uikit/uibarposition/top)Added [UIBarPositionTopAttached](https://developer.apple.com/documentation/uikit/uibarposition/topattached)Added #def UIToolbarPositionAdded #def UIToolbarPositionAnyAdded #def UIToolbarPositionBottomAdded #def UIToolbarPositionTopModified [UIBarMetrics](https://developer.apple.com/documentation/uikit/uibarmetrics)

|  | Header |
| --- | --- |
| From | UIKit/UIBarButtonItem.h |
| To | UIKit/UIBarCommon.h |

Modified [UIBarMetricsDefault](https://developer.apple.com/documentation/uikit/uibarmetrics/default)

|  | Header |
| --- | --- |
| From | UIKit/UIBarButtonItem.h |
| To | UIKit/UIBarCommon.h |

Modified [UIBarMetricsLandscapePhone](https://developer.apple.com/documentation/uikit/uibarmetrics/1624859-landscapephone)

|  | Header |
| --- | --- |
| From | UIKit/UIBarButtonItem.h |
| To | UIKit/UIBarCommon.h |

UIBezierPath.hAdded [-[UIBezierPath CGPath]](https://developer.apple.com/documentation/uikit/uibezierpath/1624376-cgpath)UIButton.hAdded [UIButtonTypeSystem](https://developer.apple.com/documentation/uikit/uibutton/buttontype/system)UICollectionView.hAdded [-[UICollectionView cancelInteractiveTransition]](https://developer.apple.com/documentation/uikit/uicollectionview/1618075-cancelinteractivetransition)Added [-[UICollectionView finishInteractiveTransition]](https://developer.apple.com/documentation/uikit/uicollectionview/1618080-finishinteractivetransition)Added [-[UICollectionView setCollectionViewLayout:animated:completion:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618017-setcollectionviewlayout)Added [-[UICollectionView startInteractiveTransitionToCollectionViewLayout:completion:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618098-startinteractivetransitiontocoll)Added [-[UICollectionViewDelegate collectionView:transitionLayoutForOldLayout:newLayout:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618100-collectionview)Added [UICollectionViewLayoutInteractiveTransitionCompletion](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinteractivetransitioncompletion)UICollectionViewController.hAdded [UICollectionViewController.collectionViewLayout](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/1623980-collectionviewlayout)Added [UICollectionViewController.useLayoutToLayoutNavigationTransitions](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/1623978-uselayouttolayoutnavigationtrans)UICollectionViewFlowLayout.hAdded [UICollectionViewFlowLayoutInvalidationContext](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayoutinvalidationcontext)Added [UICollectionViewFlowLayoutInvalidationContext.invalidateFlowLayoutAttributes](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayoutinvalidationcontext/1617707-invalidateflowlayoutattributes)Added [UICollectionViewFlowLayoutInvalidationContext.invalidateFlowLayoutDelegateMetrics](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayoutinvalidationcontext/1617721-invalidateflowlayoutdelegatemetr)UICollectionViewLayout.hAdded [-[UICollectionViewLayout finalizeLayoutTransition]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617794-finalizelayouttransition)Added [-[UICollectionViewLayout indexPathsToDeleteForDecorationViewOfKind:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617730-indexpathstodeletefordecorationv)Added [-[UICollectionViewLayout indexPathsToDeleteForSupplementaryViewOfKind:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617807-indexpathstodeleteforsupplementa)Added [-[UICollectionViewLayout indexPathsToInsertForDecorationViewOfKind:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617750-indexpathstoinsertfordecorationv)Added [-[UICollectionViewLayout indexPathsToInsertForSupplementaryViewOfKind:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617770-indexpathstoinsertforsupplementa)Added [-[UICollectionViewLayout invalidateLayoutWithContext:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617771-invalidatelayout)Added [+[UICollectionViewLayout invalidationContextClass]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617790-invalidationcontextclass)Added [-[UICollectionViewLayout invalidationContextForBoundsChange:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617754-invalidationcontext)Added [-[UICollectionViewLayout prepareForTransitionFromLayout:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617802-preparefortransition)Added [-[UICollectionViewLayout prepareForTransitionToLayout:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617791-preparefortransition)Added [-[UICollectionViewLayout targetContentOffsetForProposedContentOffset:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617724-targetcontentoffset)Added [UICollectionViewLayoutAttributes.bounds](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/1617782-bounds)Added [UICollectionViewLayoutAttributes.transform](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/1617779-transform)Added [UICollectionViewLayoutInvalidationContext](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext)Added [UICollectionViewLayoutInvalidationContext.invalidateDataSourceCounts](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617760-invalidatedatasourcecounts)Added [UICollectionViewLayoutInvalidationContext.invalidateEverything](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617793-invalidateeverything)Modified [UICollectionViewLayoutAttributes](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes)

|  | Protocols |
| --- | --- |
| From | NSCopying |
| To | NSCopying, UIDynamicItem |

UICollectionViewTransitionLayout.hAdded [UICollectionViewTransitionLayout](https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout)Added [UICollectionViewTransitionLayout.currentLayout](https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout/1622190-currentlayout)Added [-[UICollectionViewTransitionLayout initWithCurrentLayout:nextLayout:]](https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout/1622189-init)Added [UICollectionViewTransitionLayout.nextLayout](https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout/1622188-nextlayout)Added [UICollectionViewTransitionLayout.transitionProgress](https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout/1622191-transitionprogress)Added [-[UICollectionViewTransitionLayout updateValue:forAnimatedKey:]](https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout/1622194-updatevalue)Added [-[UICollectionViewTransitionLayout valueForAnimatedKey:]](https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout/1622193-valueforanimatedkey)UICollisionBehavior.hAdded [UICollisionBehavior](https://developer.apple.com/documentation/uikit/uicollisionbehavior)Added [-[UICollisionBehavior addBoundaryWithIdentifier:forPath:]](https://developer.apple.com/documentation/uikit/uicollisionbehavior/1624822-addboundary)Added [-[UICollisionBehavior addBoundaryWithIdentifier:fromPoint:toPoint:]](https://developer.apple.com/documentation/uikit/uicollisionbehavior/1624821-addboundarywithidentifier)Added [-[UICollisionBehavior addItem:]](https://developer.apple.com/documentation/uikit/uicollisionbehavior/1624829-additem)Added [UICollisionBehavior.boundaryIdentifiers](https://developer.apple.com/documentation/uikit/uicollisionbehavior/1624812-boundaryidentifiers)Added [-[UICollisionBehavior boundaryWithIdentifier:]](https://developer.apple.com/documentation/uikit/uicollisionbehavior/1624825-boundarywithidentifier)Added [UICollisionBehavior.collisionDelegate](https://developer.apple.com/documentation/uikit/uicollisionbehavior/1624828-collisiondelegate)Added [UICollisionBehavior.collisionMode](https://developer.apple.com/documentation/uikit/uicollisionbehavior/1624832-collisionmode)Added [-[UICollisionBehavior initWithItems:]](https://developer.apple.com/documentation/uikit/uicollisionbehavior/1624820-initwithitems)Added [UICollisionBehavior.items](https://developer.apple.com/documentation/uikit/uicollisionbehavior/1624819-items)Added [-[UICollisionBehavior removeAllBoundaries]](https://developer.apple.com/documentation/uikit/uicollisionbehavior/1624827-removeallboundaries)Added [-[UICollisionBehavior removeBoundaryWithIdentifier:]](https://developer.apple.com/documentation/uikit/uicollisionbehavior/1624823-removeboundarywithidentifier)Added [-[UICollisionBehavior removeItem:]](https://developer.apple.com/documentation/uikit/uicollisionbehavior/1624830-removeitem)Added [-[UICollisionBehavior setTranslatesReferenceBoundsIntoBoundaryWithInsets:]](https://developer.apple.com/documentation/uikit/uicollisionbehavior/1624818-settranslatesreferenceboundsinto)Added [UICollisionBehavior.translatesReferenceBoundsIntoBoundary](https://developer.apple.com/documentation/uikit/uicollisionbehavior/1624826-translatesreferenceboundsintobou)Added [UICollisionBehaviorDelegate](https://developer.apple.com/documentation/uikit/uicollisionbehaviordelegate)Added [-[UICollisionBehaviorDelegate collisionBehavior:beganContactForItem:withBoundaryIdentifier:atPoint:]](https://developer.apple.com/documentation/uikit/uicollisionbehaviordelegate/1624816-collisionbehavior)Added [-[UICollisionBehaviorDelegate collisionBehavior:beganContactForItem:withItem:atPoint:]](https://developer.apple.com/documentation/uikit/uicollisionbehaviordelegate/1624835-collisionbehavior)Added [-[UICollisionBehaviorDelegate collisionBehavior:endedContactForItem:withBoundaryIdentifier:]](https://developer.apple.com/documentation/uikit/uicollisionbehaviordelegate/1624834-collisionbehavior)Added [-[UICollisionBehaviorDelegate collisionBehavior:endedContactForItem:withItem:]](https://developer.apple.com/documentation/uikit/uicollisionbehaviordelegate/1624833-collisionbehavior)Added [UICollisionBehaviorMode](https://developer.apple.com/documentation/uikit/uicollisionbehaviormode)Added [UICollisionBehaviorModeBoundaries](https://developer.apple.com/documentation/uikit/uicollisionbehaviormode/uicollisionbehaviormodeboundaries)Added [UICollisionBehaviorModeEverything](https://developer.apple.com/documentation/uikit/uicollisionbehaviormode/uicollisionbehaviormodeeverything)Added [UICollisionBehaviorModeItems](https://developer.apple.com/documentation/uikit/uicollisionbehavior/mode/1624814-items)UIColor.hAdded [-[UIColor CGColor]](https://developer.apple.com/documentation/uikit/uicolor/1621943-cgcolor)Modified [UIColor](https://developer.apple.com/documentation/uikit/uicolor)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

UIDevice.hRemoved UIDevice.uniqueIdentifierUIDynamicAnimator.hAdded [UIDynamicAnimator](https://developer.apple.com/documentation/uikit/uidynamicanimator)Added [-[UIDynamicAnimator addBehavior:]](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621189-addbehavior)Added [UIDynamicAnimator.behaviors](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621198-behaviors)Added [UIDynamicAnimator.delegate](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621199-delegate)Added [-[UIDynamicAnimator elapsedTime]](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621202-elapsedtime)Added [-[UIDynamicAnimator initWithCollectionViewLayout:]](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621196-initwithcollectionviewlayout)Added [-[UIDynamicAnimator initWithReferenceView:]](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621203-initwithreferenceview)Added [-[UIDynamicAnimator itemsInRect:]](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621191-itemsinrect)Added [-[UIDynamicAnimator layoutAttributesForCellAtIndexPath:]](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621204-layoutattributesforcellatindexpa)Added [-[UIDynamicAnimator layoutAttributesForDecorationViewOfKind:atIndexPath:]](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621195-layoutattributesfordecorationvie)Added [-[UIDynamicAnimator layoutAttributesForSupplementaryViewOfKind:atIndexPath:]](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621186-layoutattributesforsupplementary)Added [UIDynamicAnimator.referenceView](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621200-referenceview)Added [-[UIDynamicAnimator removeAllBehaviors]](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621197-removeallbehaviors)Added [-[UIDynamicAnimator removeBehavior:]](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621201-removebehavior)Added [UIDynamicAnimator.running](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621192-running)Added [-[UIDynamicAnimator updateItemUsingCurrentState:]](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621190-updateitem)Added [UIDynamicAnimatorDelegate](https://developer.apple.com/documentation/uikit/uidynamicanimatordelegate)Added [-[UIDynamicAnimatorDelegate dynamicAnimatorDidPause:]](https://developer.apple.com/documentation/uikit/uidynamicanimatordelegate/1621193-dynamicanimatordidpause)Added [-[UIDynamicAnimatorDelegate dynamicAnimatorWillResume:]](https://developer.apple.com/documentation/uikit/uidynamicanimatordelegate/1621188-dynamicanimatorwillresume)Added UIDynamicAnimator(UICollectionViewAdditions)UIDynamicBehavior.hAdded [UIDynamicBehavior](https://developer.apple.com/documentation/uikit/uidynamicbehavior)Added [UIDynamicBehavior.action](https://developer.apple.com/documentation/uikit/uidynamicbehavior/1618499-action)Added [-[UIDynamicBehavior addChildBehavior:]](https://developer.apple.com/documentation/uikit/uidynamicbehavior/1618496-addchildbehavior)Added [UIDynamicBehavior.childBehaviors](https://developer.apple.com/documentation/uikit/uidynamicbehavior/1618482-childbehaviors)Added [UIDynamicBehavior.dynamicAnimator](https://developer.apple.com/documentation/uikit/uidynamicbehavior/1618501-dynamicanimator)Added [-[UIDynamicBehavior removeChildBehavior:]](https://developer.apple.com/documentation/uikit/uidynamicbehavior/1618486-removechildbehavior)Added [-[UIDynamicBehavior willMoveToAnimator:]](https://developer.apple.com/documentation/uikit/uidynamicbehavior/1618488-willmovetoanimator)Added [UIDynamicItem](https://developer.apple.com/documentation/uikit/uidynamicitem)Added [UIDynamicItem.bounds](https://developer.apple.com/documentation/uikit/uidynamicitem/1618495-bounds)Added [UIDynamicItem.center](https://developer.apple.com/documentation/uikit/uidynamicitem/1618491-center)Added [UIDynamicItem.transform](https://developer.apple.com/documentation/uikit/uidynamicitem/1618483-transform)UIDynamicItemBehavior.hAdded [UIDynamicItemBehavior](https://developer.apple.com/documentation/uikit/uidynamicitembehavior)Added [-[UIDynamicItemBehavior addAngularVelocity:forItem:]](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/1624384-addangularvelocity)Added [-[UIDynamicItemBehavior addItem:]](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/1624393-additem)Added [-[UIDynamicItemBehavior addLinearVelocity:forItem:]](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/1624391-addlinearvelocity)Added [UIDynamicItemBehavior.allowsRotation](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/1624386-allowsrotation)Added [UIDynamicItemBehavior.angularResistance](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/1624396-angularresistance)Added [-[UIDynamicItemBehavior angularVelocityForItem:]](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/1624389-angularvelocityforitem)Added [UIDynamicItemBehavior.density](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/1624395-density)Added [UIDynamicItemBehavior.elasticity](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/1624387-elasticity)Added [UIDynamicItemBehavior.friction](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/1624392-friction)Added [-[UIDynamicItemBehavior initWithItems:]](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/1624397-initwithitems)Added [UIDynamicItemBehavior.items](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/1624400-items)Added [-[UIDynamicItemBehavior linearVelocityForItem:]](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/1624388-linearvelocity)Added [-[UIDynamicItemBehavior removeItem:]](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/1624385-removeitem)Added [UIDynamicItemBehavior.resistance](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/1624399-resistance)UIFont.hRemoved UIFont(UIFontDeprecated)Added [-[UIFont fontDescriptor]](https://developer.apple.com/documentation/uikit/uifont/1619037-fontdescriptor)Added [+[UIFont fontWithDescriptor:size:]](https://developer.apple.com/documentation/uikit/uifont/1619025-init)Added [+[UIFont preferredFontForTextStyle:]](https://developer.apple.com/documentation/uikit/uifont/1619030-preferredfont)Modified [UIFont.leading](https://developer.apple.com/documentation/uikit/uifont/1619026-leading)

|  | Deprecation |
| --- | --- |
| From | iOS 4.0 |
| To | _none_ |

UIFontDescriptor.hAdded [UIFontDescriptor](https://developer.apple.com/documentation/uikit/uifontdescriptor)Added [-[UIFontDescriptor fontAttributes]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616698-fontattributes)Added [-[UIFontDescriptor fontDescriptorByAddingAttributes:]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616666-addingattributes)Added [-[UIFontDescriptor fontDescriptorWithFace:]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616681-withface)Added [-[UIFontDescriptor fontDescriptorWithFamily:]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616676-withfamily)Added [+[UIFontDescriptor fontDescriptorWithFontAttributes:]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616717-fontdescriptorwithfontattributes)Added [-[UIFontDescriptor fontDescriptorWithMatrix:]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616731-fontdescriptorwithmatrix)Added [+[UIFontDescriptor fontDescriptorWithName:matrix:]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616670-fontdescriptorwithname)Added [+[UIFontDescriptor fontDescriptorWithName:size:]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616674-fontdescriptorwithname)Added [-[UIFontDescriptor fontDescriptorWithSize:]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616675-withsize)Added [-[UIFontDescriptor fontDescriptorWithSymbolicTraits:]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616665-fontdescriptorwithsymbolictraits)Added [-[UIFontDescriptor initWithFontAttributes:]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616679-initwithfontattributes)Added [-[UIFontDescriptor matchingFontDescriptorsWithMandatoryKeys:]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616699-matchingfontdescriptorswithmanda)Added [UIFontDescriptor.matrix](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616713-matrix)Added [-[UIFontDescriptor objectForKey:]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616733-object)Added [UIFontDescriptor.pointSize](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616696-pointsize)Added [UIFontDescriptor.postscriptName](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616693-postscriptname)Added [+[UIFontDescriptor preferredFontDescriptorWithTextStyle:]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616705-preferredfontdescriptor)Added [UIFontDescriptor.symbolicTraits](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616723-symbolictraits)Added [UIFontDescriptorCascadeListAttribute](https://developer.apple.com/documentation/uikit/uifontdescriptor/attributename/1616711-cascadelist)Added [UIFontDescriptorCharacterSetAttribute](https://developer.apple.com/documentation/uikit/uifontdescriptor/attributename/1616727-characterset)Added [UIFontDescriptorClass](https://developer.apple.com/documentation/uikit/uifontdescriptorclass)Added [UIFontDescriptorClassClarendonSerifs](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits/1616730-classclarendonserifs)Added [UIFontDescriptorClassFreeformSerifs](https://developer.apple.com/documentation/uikit/uifontdescriptorsymbolictraits/uifontdescriptorclassfreeformserifs)Added [UIFontDescriptorClassMask](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits/1616672-classmask)Added [UIFontDescriptorClassModernSerifs](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits/1616734-classmodernserifs)Added [UIFontDescriptorClassOldStyleSerifs](https://developer.apple.com/documentation/uikit/uifontdescriptorsymbolictraits/uifontdescriptorclassoldstyleserifs)Added [UIFontDescriptorClassOrnamentals](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits/1616716-classornamentals)Added [UIFontDescriptorClassSansSerif](https://developer.apple.com/documentation/uikit/uifontdescriptorsymbolictraits/uifontdescriptorclasssansserif)Added [UIFontDescriptorClassScripts](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits/1616663-classscripts)Added [UIFontDescriptorClassSlabSerifs](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits/1616740-classslabserifs)Added [UIFontDescriptorClassSymbolic](https://developer.apple.com/documentation/uikit/uifontdescriptorsymbolictraits/uifontdescriptorclasssymbolic)Added [UIFontDescriptorClassTransitionalSerifs](https://developer.apple.com/documentation/uikit/uifontdescriptorsymbolictraits/uifontdescriptorclasstransitionalserifs)Added [UIFontDescriptorClassUnknown](https://developer.apple.com/documentation/uikit/uifontdescriptorsymbolictraits/uifontdescriptorclassunknown)Added [UIFontDescriptorFaceAttribute](https://developer.apple.com/documentation/uikit/uifontdescriptorfaceattribute)Added [UIFontDescriptorFamilyAttribute](https://developer.apple.com/documentation/uikit/uifontdescriptorfamilyattribute)Added [UIFontDescriptorFeatureSettingsAttribute](https://developer.apple.com/documentation/uikit/uifontdescriptor/attributename/1616701-featuresettings)Added [UIFontDescriptorFixedAdvanceAttribute](https://developer.apple.com/documentation/uikit/uifontdescriptor/attributename/1616739-fixedadvance)Added [UIFontDescriptorMatrixAttribute](https://developer.apple.com/documentation/uikit/uifontdescriptormatrixattribute)Added [UIFontDescriptorNameAttribute](https://developer.apple.com/documentation/uikit/uifontdescriptor/attributename/1616685-name)Added [UIFontDescriptorSizeAttribute](https://developer.apple.com/documentation/uikit/uifontdescriptor/attributename/1616728-size)Added [UIFontDescriptorSymbolicTraits](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits)Added [UIFontDescriptorTextStyleAttribute](https://developer.apple.com/documentation/uikit/uifontdescriptortextstyleattribute)Added [UIFontDescriptorTraitBold](https://developer.apple.com/documentation/uikit/uifontdescriptorsymbolictraits/uifontdescriptortraitbold)Added [UIFontDescriptorTraitCondensed](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits/1616661-traitcondensed)Added [UIFontDescriptorTraitExpanded](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits/1616691-traitexpanded)Added [UIFontDescriptorTraitItalic](https://developer.apple.com/documentation/uikit/uifontdescriptorsymbolictraits/uifontdescriptortraititalic)Added [UIFontDescriptorTraitLooseLeading](https://developer.apple.com/documentation/uikit/uifontdescriptorsymbolictraits/uifontdescriptortraitlooseleading)Added [UIFontDescriptorTraitMonoSpace](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits/1616708-traitmonospace)Added [UIFontDescriptorTraitTightLeading](https://developer.apple.com/documentation/uikit/uifontdescriptorsymbolictraits/uifontdescriptortraittightleading)Added [UIFontDescriptorTraitUIOptimized](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits/1616737-traituioptimized)Added [UIFontDescriptorTraitVertical](https://developer.apple.com/documentation/uikit/uifontdescriptorsymbolictraits/uifontdescriptortraitvertical)Added [UIFontDescriptorTraitsAttribute](https://developer.apple.com/documentation/uikit/uifontdescriptortraitsattribute)Added [UIFontDescriptorVisibleNameAttribute](https://developer.apple.com/documentation/uikit/uifontdescriptor/attributename/1616690-visiblename)Added [UIFontFeatureSelectorIdentifierKey](https://developer.apple.com/documentation/uikit/uifontdescriptor/featurekey/1616687-typeidentifier)Added [UIFontFeatureTypeIdentifierKey](https://developer.apple.com/documentation/uikit/uifontfeaturetypeidentifierkey)Added [UIFontSlantTrait](https://developer.apple.com/documentation/uikit/uifontdescriptor/traitkey/1616686-slant)Added [UIFontSymbolicTrait](https://developer.apple.com/documentation/uikit/uifontsymbolictrait)Added [UIFontTextStyleBody](https://developer.apple.com/documentation/uikit/uifonttextstylebody)Added [UIFontTextStyleCaption1](https://developer.apple.com/documentation/uikit/uifont/textstyle/1616735-caption1)Added [UIFontTextStyleCaption2](https://developer.apple.com/documentation/uikit/uifonttextstylecaption2)Added [UIFontTextStyleFootnote](https://developer.apple.com/documentation/uikit/uifont/textstyle/1616700-footnote)Added [UIFontTextStyleHeadline](https://developer.apple.com/documentation/uikit/uifonttextstyleheadline)Added [UIFontTextStyleSubheadline](https://developer.apple.com/documentation/uikit/uifonttextstylesubheadline)Added [UIFontWeightTrait](https://developer.apple.com/documentation/uikit/uifontweighttrait)Added [UIFontWidthTrait](https://developer.apple.com/documentation/uikit/uifontwidthtrait)UIGeometry.hAdded [UIRectEdge](https://developer.apple.com/documentation/uikit/uirectedge)Added [UIRectEdgeAll](https://developer.apple.com/documentation/uikit/uirectedge/1624535-all)Added [UIRectEdgeBottom](https://developer.apple.com/documentation/uikit/uirectedge/uirectedgebottom)Added [UIRectEdgeLeft](https://developer.apple.com/documentation/uikit/uirectedge/1624495-left)Added [UIRectEdgeNone](https://developer.apple.com/documentation/uikit/uirectedge/uirectedgenone)Added [UIRectEdgeRight](https://developer.apple.com/documentation/uikit/uirectedge/uirectedgeright)Added [UIRectEdgeTop](https://developer.apple.com/documentation/uikit/uirectedge/uirectedgetop)UIGestureRecognizer.hAdded [-[UIGestureRecognizerDelegate gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:]](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/1624222-gesturerecognizer)Added [-[UIGestureRecognizerDelegate gestureRecognizer:shouldRequireFailureOfGestureRecognizer:]](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/1624229-gesturerecognizer)UIGestureRecognizerSubclass.hAdded [-[UIGestureRecognizer shouldBeRequiredToFailByGestureRecognizer:]](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1619994-shouldberequiredtofailbygesturer)Added [-[UIGestureRecognizer shouldRequireFailureOfGestureRecognizer:]](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1620006-shouldrequirefailure)UIGravityBehavior.hAdded [UIGravityBehavior](https://developer.apple.com/documentation/uikit/uigravitybehavior)Added [-[UIGravityBehavior addItem:]](https://developer.apple.com/documentation/uikit/uigravitybehavior/1620415-additem)Added [UIGravityBehavior.angle](https://developer.apple.com/documentation/uikit/uigravitybehavior/1620417-angle)Added [UIGravityBehavior.gravityDirection](https://developer.apple.com/documentation/uikit/uigravitybehavior/1620423-gravitydirection)Added [-[UIGravityBehavior initWithItems:]](https://developer.apple.com/documentation/uikit/uigravitybehavior/1620416-init)Added [UIGravityBehavior.items](https://developer.apple.com/documentation/uikit/uigravitybehavior/1620420-items)Added [UIGravityBehavior.magnitude](https://developer.apple.com/documentation/uikit/uigravitybehavior/1620418-magnitude)Added [-[UIGravityBehavior removeItem:]](https://developer.apple.com/documentation/uikit/uigravitybehavior/1620422-removeitem)Added [-[UIGravityBehavior setAngle:magnitude:]](https://developer.apple.com/documentation/uikit/uigravitybehavior/1620414-setangle)UIGuidedAccessRestrictions.hAdded [UIGuidedAccessRestrictionDelegate](https://developer.apple.com/documentation/uikit/uiguidedaccessrestrictiondelegate)Added [-[UIGuidedAccessRestrictionDelegate detailTextForGuidedAccessRestrictionWithIdentifier:]](https://developer.apple.com/documentation/uikit/uiguidedaccessrestrictiondelegate/1621158-detailtextforguidedaccessrestric)Added [-[UIGuidedAccessRestrictionDelegate guidedAccessRestrictionIdentifiers]](https://developer.apple.com/documentation/uikit/uiguidedaccessrestrictiondelegate/1621160-guidedaccessrestrictionidentifie)Added [-[UIGuidedAccessRestrictionDelegate guidedAccessRestrictionWithIdentifier:didChangeState:]](https://developer.apple.com/documentation/uikit/uiguidedaccessrestrictiondelegate/1621156-guidedaccessrestrictionwithident)Added [-[UIGuidedAccessRestrictionDelegate textForGuidedAccessRestrictionWithIdentifier:]](https://developer.apple.com/documentation/uikit/uiguidedaccessrestrictiondelegate/1621161-textforguidedaccessrestrictionwi)Added [UIGuidedAccessRestrictionState](https://developer.apple.com/documentation/uikit/uiguidedaccessrestrictionstate)Added [UIGuidedAccessRestrictionStateAllow](https://developer.apple.com/documentation/uikit/uiaccessibility/guidedaccessrestrictionstate/allow)Added [UIGuidedAccessRestrictionStateDeny](https://developer.apple.com/documentation/uikit/uiguidedaccessrestrictionstate/uiguidedaccessrestrictionstatedeny)Added [UIGuidedAccessRestrictionStateForIdentifier()](https://developer.apple.com/documentation/uikit/uiaccessibility/1621153-guidedaccessrestrictionstate)UIImage.hAdded [-[UIImage CGImage]](https://developer.apple.com/documentation/uikit/uiimage/1624159-cgimage)Added [-[UIImage imageWithRenderingMode:]](https://developer.apple.com/documentation/uikit/uiimage/1624153-imagewithrenderingmode)Added [UIImage.renderingMode](https://developer.apple.com/documentation/uikit/uiimage/1624122-renderingmode)Added [UIImageRenderingMode](https://developer.apple.com/documentation/uikit/uiimagerenderingmode)Added [UIImageRenderingModeAlwaysOriginal](https://developer.apple.com/documentation/uikit/uiimage/renderingmode/alwaysoriginal)Added [UIImageRenderingModeAlwaysTemplate](https://developer.apple.com/documentation/uikit/uiimage/renderingmode/alwaystemplate)Added [UIImageRenderingModeAutomatic](https://developer.apple.com/documentation/uikit/uiimage/renderingmode/automatic)UIImageView.hAdded [UIImageView.tintColor](https://developer.apple.com/documentation/uikit/uiimageview/1621059-tintcolor)UIInputView.hAdded [UIInputView](https://developer.apple.com/documentation/uikit/uiinputview)Added [-[UIInputView initWithFrame:inputViewStyle:]](https://developer.apple.com/documentation/uikit/uiinputview/1619477-initwithframe)Added [UIInputView.inputViewStyle](https://developer.apple.com/documentation/uikit/uiinputview/1619471-inputviewstyle)Added [UIInputViewStyle](https://developer.apple.com/documentation/uikit/uiinputview/style)Added [UIInputViewStyleDefault](https://developer.apple.com/documentation/uikit/uiinputview/style/default)Added [UIInputViewStyleKeyboard](https://developer.apple.com/documentation/uikit/uiinputview/style/keyboard)UIInterface.hModified [+[UIColor scrollViewTexturedBackgroundColor]](https://developer.apple.com/documentation/uikit/uicolor/1623405-scrollviewtexturedbackgroundcolo)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [+[UIColor underPageBackgroundColor]](https://developer.apple.com/documentation/uikit/uicolor/1623406-underpagebackgroundcolor)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [+[UIColor viewFlipsideBackgroundColor]](https://developer.apple.com/documentation/uikit/uicolor/1623409-viewflipsidebackgroundcolor)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

UILabel.hModified [UILabel.adjustsLetterSpacingToFitWidth](https://developer.apple.com/documentation/uikit/uilabel/1620535-adjustsletterspacingtofitwidth)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

UIMotionEffect.hAdded [UIInterpolatingMotionEffect](https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect)Added [-[UIInterpolatingMotionEffect initWithKeyPath:type:]](https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect/1622372-init)Added [UIInterpolatingMotionEffect.keyPath](https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect/1622378-keypath)Added [UIInterpolatingMotionEffect.maximumRelativeValue](https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect/1622376-maximumrelativevalue)Added [UIInterpolatingMotionEffect.minimumRelativeValue](https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect/1622365-minimumrelativevalue)Added [UIInterpolatingMotionEffect.type](https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect/1622377-type)Added [UIMotionEffect](https://developer.apple.com/documentation/uikit/uimotioneffect)Added [-[UIMotionEffect keyPathsAndRelativeValuesForViewerOffset:]](https://developer.apple.com/documentation/uikit/uimotioneffect/1622380-keypathsandrelativevaluesforview)Added [UIMotionEffectGroup](https://developer.apple.com/documentation/uikit/uimotioneffectgroup)Added [UIMotionEffectGroup.motionEffects](https://developer.apple.com/documentation/uikit/uimotioneffectgroup/1622374-motioneffects)Added [UIInterpolatingMotionEffectType](https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffecttype)Added [UIInterpolatingMotionEffectTypeTiltAlongHorizontalAxis](https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect/effecttype/tiltalonghorizontalaxis)Added [UIInterpolatingMotionEffectTypeTiltAlongVerticalAxis](https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect/effecttype/tiltalongverticalaxis)UINavigationBar.hAdded [UINavigationBar.backIndicatorImage](https://developer.apple.com/documentation/uikit/uinavigationbar/1624942-backindicatorimage)Added [UINavigationBar.backIndicatorTransitionMaskImage](https://developer.apple.com/documentation/uikit/uinavigationbar/1624938-backindicatortransitionmaskimage)Added [-[UINavigationBar backgroundImageForBarPosition:barMetrics:]](https://developer.apple.com/documentation/uikit/uinavigationbar/1624940-backgroundimage)Added [UINavigationBar.barTintColor](https://developer.apple.com/documentation/uikit/uinavigationbar/1624931-bartintcolor)Added [-[UINavigationBar setBackgroundImage:forBarPosition:barMetrics:]](https://developer.apple.com/documentation/uikit/uinavigationbar/1624968-setbackgroundimage)Modified [UINavigationBar](https://developer.apple.com/documentation/uikit/uinavigationbar)

|  | Protocols |
| --- | --- |
| From | NSCoding |
| To | NSCoding, UIBarPositioning |

Modified [UINavigationBarDelegate](https://developer.apple.com/documentation/uikit/uinavigationbardelegate)

|  | Protocols |
| --- | --- |
| From | NSObject |
| To | UIBarPositioningDelegate |

UINavigationController.hAdded [UINavigationController.interactivePopGestureRecognizer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621847-interactivepopgesturerecognizer)Added [-[UINavigationControllerDelegate navigationController:animationControllerForOperation:fromViewController:toViewController:]](https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate/1621846-navigationcontroller)Added [-[UINavigationControllerDelegate navigationController:interactionControllerForAnimationController:]](https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate/1621880-navigationcontroller)Added [-[UINavigationControllerDelegate navigationControllerPreferredInterfaceOrientationForPresentation:]](https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate/1621864-navigationcontrollerpreferredint)Added [-[UINavigationControllerDelegate navigationControllerSupportedInterfaceOrientations:]](https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate/1621884-navigationcontrollersupportedint)Added [UINavigationControllerOperation](https://developer.apple.com/documentation/uikit/uinavigationcontroller/operation)Added [UINavigationControllerOperationNone](https://developer.apple.com/documentation/uikit/uinavigationcontroller/operation/none)Added [UINavigationControllerOperationPop](https://developer.apple.com/documentation/uikit/uinavigationcontroller/operation/pop)Added [UINavigationControllerOperationPush](https://developer.apple.com/documentation/uikit/uinavigationcontroller/operation/push)UIPageViewController.hAdded [-[UIPageViewControllerDelegate pageViewControllerPreferredInterfaceOrientationForPresentation:]](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/1614119-pageviewcontrollerpreferredinter)Added [-[UIPageViewControllerDelegate pageViewControllerSupportedInterfaceOrientations:]](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/1614100-pageviewcontrollersupportedinter)UIPopoverController.hAdded [UIPopoverController.backgroundColor](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624673-backgroundcolor)Added [-[UIPopoverControllerDelegate popoverController:willRepositionPopoverToRect:inView:]](https://developer.apple.com/documentation/uikit/uipopovercontrollerdelegate/1624664-popovercontroller)Modified [UIViewController.contentSizeForViewInPopover](https://developer.apple.com/documentation/uikit/uiviewcontroller/1619323-contentsizeforviewinpopover)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

UIPrintFormatter.hAdded [UISimpleTextPrintFormatter.attributedText](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/1621820-attributedtext)Added [-[UISimpleTextPrintFormatter initWithAttributedText:]](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/1621838-init)UIPrintInfo.hAdded [UIPrintInfoOutputPhotoGrayscale](https://developer.apple.com/documentation/uikit/uiprintinfo/outputtype/photograyscale)UIPrintInteractionController.hAdded [UIPrintInteractionController.showsNumberOfCopies](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618177-showsnumberofcopies)Added [-[UIPrintInteractionControllerDelegate printInteractionController:cutLengthForPaper:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618179-printinteractioncontroller)UIPushBehavior.hAdded [UIPushBehavior](https://developer.apple.com/documentation/uikit/uipushbehavior)Added [UIPushBehavior.active](https://developer.apple.com/documentation/uikit/uipushbehavior/1623336-active)Added [-[UIPushBehavior addItem:]](https://developer.apple.com/documentation/uikit/uipushbehavior/1623333-additem)Added [UIPushBehavior.angle](https://developer.apple.com/documentation/uikit/uipushbehavior/1623332-angle)Added [-[UIPushBehavior initWithItems:mode:]](https://developer.apple.com/documentation/uikit/uipushbehavior/1623329-init)Added [UIPushBehavior.items](https://developer.apple.com/documentation/uikit/uipushbehavior/1623339-items)Added [UIPushBehavior.magnitude](https://developer.apple.com/documentation/uikit/uipushbehavior/1623330-magnitude)Added [UIPushBehavior.mode](https://developer.apple.com/documentation/uikit/uipushbehavior/1623340-mode)Added [UIPushBehavior.pushDirection](https://developer.apple.com/documentation/uikit/uipushbehavior/1623331-pushdirection)Added [-[UIPushBehavior removeItem:]](https://developer.apple.com/documentation/uikit/uipushbehavior/1623343-removeitem)Added [-[UIPushBehavior setAngle:magnitude:]](https://developer.apple.com/documentation/uikit/uipushbehavior/1623335-setangle)Added [-[UIPushBehavior setTargetOffsetFromCenter:forItem:]](https://developer.apple.com/documentation/uikit/uipushbehavior/1623341-settargetoffsetfromcenter)Added [-[UIPushBehavior targetOffsetFromCenterForItem:]](https://developer.apple.com/documentation/uikit/uipushbehavior/1623338-targetoffsetfromcenterforitem)Added [UIPushBehaviorMode](https://developer.apple.com/documentation/uikit/uipushbehavior/mode)Added [UIPushBehaviorModeContinuous](https://developer.apple.com/documentation/uikit/uipushbehaviormode/uipushbehaviormodecontinuous)Added [UIPushBehaviorModeInstantaneous](https://developer.apple.com/documentation/uikit/uipushbehaviormode/uipushbehaviormodeinstantaneous)UIResponder.hAdded -[NSObject decreaseSize:]Added -[NSObject increaseSize:]Added [UIKeyCommand](https://developer.apple.com/documentation/uikit/uikeycommand)Added [UIKeyCommand.input](https://developer.apple.com/documentation/uikit/uikeycommand/1621143-input)Added [+[UIKeyCommand keyCommandWithInput:modifierFlags:action:]](https://developer.apple.com/documentation/uikit/uikeycommand/1621131-keycommandwithinput)Added [UIKeyCommand.modifierFlags](https://developer.apple.com/documentation/uikit/uikeycommand/1621140-modifierflags)Added [+[UIResponder clearTextInputContextIdentifier:]](https://developer.apple.com/documentation/uikit/uiresponder/1621138-cleartextinputcontextidentifier)Added [UIResponder.keyCommands](https://developer.apple.com/documentation/uikit/uiresponder/1621141-keycommands)Added [-[UIResponder targetForAction:withSender:]](https://developer.apple.com/documentation/uikit/uiresponder/1621146-target)Added [UIResponder.textInputContextIdentifier](https://developer.apple.com/documentation/uikit/uiresponder/1621091-textinputcontextidentifier)Added [UIResponder.textInputMode](https://developer.apple.com/documentation/uikit/uiresponder/1621133-textinputmode)Added [UIKeyInputDownArrow](https://developer.apple.com/documentation/uikit/uikeycommand/1621088-inputdownarrow)Added [UIKeyInputEscape](https://developer.apple.com/documentation/uikit/uikeycommand/1621144-inputescape)Added [UIKeyInputLeftArrow](https://developer.apple.com/documentation/uikit/uikeyinputleftarrow)Added [UIKeyInputRightArrow](https://developer.apple.com/documentation/uikit/uikeyinputrightarrow)Added [UIKeyInputUpArrow](https://developer.apple.com/documentation/uikit/uikeyinputuparrow)Added [UIKeyModifierAlphaShift](https://developer.apple.com/documentation/uikit/uikeymodifierflags/uikeymodifieralphashift)Added [UIKeyModifierAlternate](https://developer.apple.com/documentation/uikit/uikeymodifierflags/uikeymodifieralternate)Added [UIKeyModifierCommand](https://developer.apple.com/documentation/uikit/uikeymodifierflags/1621085-command)Added [UIKeyModifierControl](https://developer.apple.com/documentation/uikit/uikeymodifierflags/uikeymodifiercontrol)Added [UIKeyModifierFlags](https://developer.apple.com/documentation/uikit/uikeymodifierflags)Added [UIKeyModifierNumericPad](https://developer.apple.com/documentation/uikit/uikeymodifierflags/1621132-numericpad)Added [UIKeyModifierShift](https://developer.apple.com/documentation/uikit/uikeymodifierflags/uikeymodifiershift)Added UIResponder(UIResponderKeyCommands)UIScreen.hAdded [-[UIScreen snapshotViewAfterScreenUpdates:]](https://developer.apple.com/documentation/uikit/uiscreen/1617814-snapshotview)Added UIScreen(UISnapshotting)UIScreenEdgePanGestureRecognizer.hAdded [UIScreenEdgePanGestureRecognizer](https://developer.apple.com/documentation/uikit/uiscreenedgepangesturerecognizer)Added [UIScreenEdgePanGestureRecognizer.edges](https://developer.apple.com/documentation/uikit/uiscreenedgepangesturerecognizer/1614142-edges)UIScrollView.hAdded [UIScrollView.keyboardDismissMode](https://developer.apple.com/documentation/uikit/uiscrollview/1619437-keyboarddismissmode)Added [UIScrollViewKeyboardDismissMode](https://developer.apple.com/documentation/uikit/uiscrollview/keyboarddismissmode)Added [UIScrollViewKeyboardDismissModeInteractive](https://developer.apple.com/documentation/uikit/uiscrollview/keyboarddismissmode/interactive)Added [UIScrollViewKeyboardDismissModeNone](https://developer.apple.com/documentation/uikit/uiscrollviewkeyboarddismissmode/uiscrollviewkeyboarddismissmodenone)Added [UIScrollViewKeyboardDismissModeOnDrag](https://developer.apple.com/documentation/uikit/uiscrollviewkeyboarddismissmode/uiscrollviewkeyboarddismissmodeondrag)Modified [UIScrollView.decelerationRate](https://developer.apple.com/documentation/uikit/uiscrollview/1619438-decelerationrate)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic) float decelerationRate |
| To | @property(nonatomic) CGFloat decelerationRate |

Modified [UIScrollView.maximumZoomScale](https://developer.apple.com/documentation/uikit/uiscrollview/1619408-maximumzoomscale)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic) float maximumZoomScale |
| To | @property(nonatomic) CGFloat maximumZoomScale |

Modified [UIScrollView.minimumZoomScale](https://developer.apple.com/documentation/uikit/uiscrollview/1619428-minimumzoomscale)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic) float minimumZoomScale |
| To | @property(nonatomic) CGFloat minimumZoomScale |

Modified [-[UIScrollView setZoomScale:animated:]](https://developer.apple.com/documentation/uikit/uiscrollview/1619412-setzoomscale)

|  | Declaration |
| --- | --- |
| From | - (void)setZoomScale:(float)scale animated:(BOOL)animated |
| To | - (void)setZoomScale:(CGFloat)scale animated:(BOOL)animated |

Modified [UIScrollView.zoomScale](https://developer.apple.com/documentation/uikit/uiscrollview/1619419-zoomscale)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic) float zoomScale |
| To | @property(nonatomic) CGFloat zoomScale |

Modified [-[UIScrollViewDelegate scrollViewDidEndZooming:withView:atScale:]](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/1619407-scrollviewdidendzooming)

|  | Declaration |
| --- | --- |
| From | - (void)scrollViewDidEndZooming:(UIScrollView \*)scrollView withView:(UIView \*)view atScale:(float)scale |
| To | - (void)scrollViewDidEndZooming:(UIScrollView \*)scrollView withView:(UIView \*)view atScale:(CGFloat)scale |

UISearchBar.hAdded -[UISearchBar backgroundImageForBarMetrics:]Added [-[UISearchBar backgroundImageForBarPosition:barMetrics:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624274-backgroundimageforbarposition)Added [UISearchBar.barTintColor](https://developer.apple.com/documentation/uikit/uisearchbar/1624295-bartintcolor)Added [UISearchBar.searchBarStyle](https://developer.apple.com/documentation/uikit/uisearchbar/1624281-searchbarstyle)Added -[UISearchBar setBackgroundImage:forBarMetrics:]Added [-[UISearchBar setBackgroundImage:forBarPosition:barMetrics:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624325-setbackgroundimage)Added [UISearchBarStyle](https://developer.apple.com/documentation/uikit/uisearchbar/style)Added [UISearchBarStyleDefault](https://developer.apple.com/documentation/uikit/uisearchbarstyle/uisearchbarstyledefault)Added [UISearchBarStyleMinimal](https://developer.apple.com/documentation/uikit/uisearchbarstyle/uisearchbarstyleminimal)Added [UISearchBarStyleProminent](https://developer.apple.com/documentation/uikit/uisearchbar/style/prominent)Modified [UISearchBar](https://developer.apple.com/documentation/uikit/uisearchbar)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | UIBarPositioning |

Modified [UISearchBarDelegate](https://developer.apple.com/documentation/uikit/uisearchbardelegate)

|  | Protocols |
| --- | --- |
| From | NSObject |
| To | UIBarPositioningDelegate |

UISearchDisplayController.hAdded [UISearchDisplayController.displaysSearchBarInNavigationBar](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/1620394-displayssearchbarinnavigationbar)Added [UISearchDisplayController.navigationItem](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/1620408-navigationitem)UISegmentedControl.hModified [UISegmentedControl.segmentedControlStyle](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/1618577-segmentedcontrolstyle)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

UISnapBehavior.hAdded [UISnapBehavior](https://developer.apple.com/documentation/uikit/uisnapbehavior)Added [UISnapBehavior.damping](https://developer.apple.com/documentation/uikit/uisnapbehavior/1621012-damping)Added [-[UISnapBehavior initWithItem:snapToPoint:]](https://developer.apple.com/documentation/uikit/uisnapbehavior/1621011-initwithitem)UISplitViewController.hAdded [-[UISplitViewControllerDelegate splitViewControllerPreferredInterfaceOrientationForPresentation:]](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/1623169-splitviewcontrollerpreferredinte)Added [-[UISplitViewControllerDelegate splitViewControllerSupportedInterfaceOrientations:]](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/1623178-splitviewcontrollersupportedinte)UIStateRestoration.hAdded [UIObjectRestoration](https://developer.apple.com/documentation/uikit/uiobjectrestoration)Added [+[UIObjectRestoration objectWithRestorationIdentifierPath:coder:]](https://developer.apple.com/documentation/uikit/uiobjectrestoration/1616855-object)Added [UIStateRestoring](https://developer.apple.com/documentation/uikit/uistaterestoring)Added [-[UIStateRestoring applicationFinishedRestoringState]](https://developer.apple.com/documentation/uikit/uistaterestoring/1616864-applicationfinishedrestoringstat)Added [-[UIStateRestoring decodeRestorableStateWithCoder:]](https://developer.apple.com/documentation/uikit/uistaterestoring/1616854-decoderestorablestate)Added [-[UIStateRestoring encodeRestorableStateWithCoder:]](https://developer.apple.com/documentation/uikit/uistaterestoring/1616866-encoderestorablestatewithcoder)Added [UIStateRestoring.objectRestorationClass](https://developer.apple.com/documentation/uikit/uistaterestoring/1616851-objectrestorationclass)Added [UIStateRestoring.restorationParent](https://developer.apple.com/documentation/uikit/uistaterestoring/1616867-restorationparent)Added [UIApplicationStateRestorationSystemVersionKey](https://developer.apple.com/documentation/uikit/uiapplicationstaterestorationsystemversionkey)Added [UIApplicationStateRestorationTimestampKey](https://developer.apple.com/documentation/uikit/uiapplicationstaterestorationtimestampkey)UIStringDrawing.hModified [-[NSString drawAtPoint:forWidth:withFont:fontSize:lineBreakMode:baselineAdjustment:]](https://developer.apple.com/documentation/foundation/nsstring/1619919-drawatpoint)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[NSString drawAtPoint:forWidth:withFont:lineBreakMode:]](https://developer.apple.com/documentation/foundation/nsstring/1619896-drawatpoint)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[NSString drawAtPoint:forWidth:withFont:minFontSize:actualFontSize:lineBreakMode:baselineAdjustment:]](https://developer.apple.com/documentation/foundation/nsstring/1619894-drawatpoint)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[NSString drawAtPoint:withFont:]](https://developer.apple.com/documentation/foundation/nsstring/1619898-drawatpoint)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[NSString drawInRect:withFont:]](https://developer.apple.com/documentation/foundation/nsstring/1619909-drawinrect)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[NSString drawInRect:withFont:lineBreakMode:]](https://developer.apple.com/documentation/foundation/nsstring/1619908-drawinrect)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[NSString drawInRect:withFont:lineBreakMode:alignment:]](https://developer.apple.com/documentation/foundation/nsstring/1619912-drawinrect)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[NSString sizeWithFont:]](https://developer.apple.com/documentation/foundation/nsstring/1619917-sizewithfont)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[NSString sizeWithFont:constrainedToSize:]](https://developer.apple.com/documentation/foundation/nsstring/1619910-sizewithfont)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[NSString sizeWithFont:constrainedToSize:lineBreakMode:]](https://developer.apple.com/documentation/foundation/nsstring/1619915-sizewithfont)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[NSString sizeWithFont:forWidth:lineBreakMode:]](https://developer.apple.com/documentation/foundation/nsstring/1619914-sizewithfont)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[NSString sizeWithFont:minFontSize:actualFontSize:forWidth:lineBreakMode:]](https://developer.apple.com/documentation/foundation/nsstring/1619903-sizewithfont)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [UITextAttributeFont](https://developer.apple.com/documentation/uikit/uitextattributefont)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [UITextAttributeTextColor](https://developer.apple.com/documentation/uikit/uitextattributetextcolor)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [UITextAttributeTextShadowColor](https://developer.apple.com/documentation/uikit/uitextattributetextshadowcolor)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [UITextAttributeTextShadowOffset](https://developer.apple.com/documentation/uikit/uitextattributetextshadowoffset)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

UITabBar.hAdded [UITabBar.barStyle](https://developer.apple.com/documentation/uikit/uitabbar/1623454-barstyle)Added [UITabBar.barTintColor](https://developer.apple.com/documentation/uikit/uitabbar/1623445-bartintcolor)Added [UITabBar.itemPositioning](https://developer.apple.com/documentation/uikit/uitabbar/1623468-itempositioning)Added [UITabBar.itemSpacing](https://developer.apple.com/documentation/uikit/uitabbar/1623446-itemspacing)Added [UITabBar.itemWidth](https://developer.apple.com/documentation/uikit/uitabbar/1623465-itemwidth)Added [UITabBar.translucent](https://developer.apple.com/documentation/uikit/uitabbar/1623458-istranslucent)Added [UITabBarItemPositioning](https://developer.apple.com/documentation/uikit/uitabbaritempositioning)Added [UITabBarItemPositioningAutomatic](https://developer.apple.com/documentation/uikit/uitabbar/itempositioning/automatic)Added [UITabBarItemPositioningCentered](https://developer.apple.com/documentation/uikit/uitabbar/itempositioning/centered)Added [UITabBarItemPositioningFill](https://developer.apple.com/documentation/uikit/uitabbaritempositioning/uitabbaritempositioningfill)UITabBarController.hAdded [-[UITabBarControllerDelegate tabBarController:animationControllerForTransitionFromViewController:toViewController:]](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/1621167-tabbarcontroller)Added [-[UITabBarControllerDelegate tabBarController:interactionControllerForAnimationController:]](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/1621170-tabbarcontroller)Added [-[UITabBarControllerDelegate tabBarControllerPreferredInterfaceOrientationForPresentation:]](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/1621176-tabbarcontrollerpreferredinterfa)Added [-[UITabBarControllerDelegate tabBarControllerSupportedInterfaceOrientations:]](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/1621180-tabbarcontrollersupportedinterfa)UITabBarItem.hAdded [-[UITabBarItem initWithTitle:image:selectedImage:]](https://developer.apple.com/documentation/uikit/uitabbaritem/1617066-init)Added [UITabBarItem.selectedImage](https://developer.apple.com/documentation/uikit/uitabbaritem/1617072-selectedimage)Modified [-[UITabBarItem finishedSelectedImage]](https://developer.apple.com/documentation/uikit/uitabbaritem/1617051-finishedselectedimage)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[UITabBarItem finishedUnselectedImage]](https://developer.apple.com/documentation/uikit/uitabbaritem/1617053-finishedunselectedimage)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

Modified [-[UITabBarItem setFinishedSelectedImage:withFinishedUnselectedImage:]](https://developer.apple.com/documentation/uikit/uitabbaritem/1617063-setfinishedselectedimage)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

UITableView.hAdded [UITableView.estimatedRowHeight](https://developer.apple.com/documentation/uikit/uitableview/1614925-estimatedrowheight)Added [UITableView.estimatedSectionFooterHeight](https://developer.apple.com/documentation/uikit/uitableview/1614979-estimatedsectionfooterheight)Added [UITableView.estimatedSectionHeaderHeight](https://developer.apple.com/documentation/uikit/uitableview/1614957-estimatedsectionheaderheight)Added [UITableView.sectionIndexBackgroundColor](https://developer.apple.com/documentation/uikit/uitableview/1614918-sectionindexbackgroundcolor)Added [UITableView.separatorInset](https://developer.apple.com/documentation/uikit/uitableview/1614851-separatorinset)Added [-[UITableViewDelegate tableView:estimatedHeightForFooterInSection:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614939-tableview)Added [-[UITableViewDelegate tableView:estimatedHeightForHeaderInSection:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614854-tableview)Added [-[UITableViewDelegate tableView:estimatedHeightForRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614926-tableview)UITableViewCell.hAdded [UITableViewCell.separatorInset](https://developer.apple.com/documentation/uikit/uitableviewcell/1623250-separatorinset)Added [UITableViewCellAccessoryDetailButton](https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype/detailbutton)Added [UITableViewCellSelectionStyleDefault](https://developer.apple.com/documentation/uikit/uitableviewcell/selectionstyle/default)UITextField.hAdded [UITextField.defaultTextAttributes](https://developer.apple.com/documentation/uikit/uitextfield/1619618-defaulttextattributes)UITextInput.hModified [UITextInputMode](https://developer.apple.com/documentation/uikit/uitextinputmode)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSSecureCoding |

Modified [+[UITextInputMode currentInputMode]](https://developer.apple.com/documentation/uikit/uitextinputmode/1614538-currentinputmode)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

UITextInputTraits.hAdded [UIKeyboardAppearanceDark](https://developer.apple.com/documentation/uikit/uikeyboardappearance/uikeyboardappearancedark)Added [UIKeyboardAppearanceLight](https://developer.apple.com/documentation/uikit/uikeyboardappearance/light)Added [UIKeyboardTypeWebSearch](https://developer.apple.com/documentation/uikit/uikeyboardtype/uikeyboardtypewebsearch)UITextView.hRemoved [-[UITextView hasText]](https://developer.apple.com/documentation/uikit/uitextview/1807137-hastext)Added [-[UITextView initWithFrame:textContainer:]](https://developer.apple.com/documentation/uikit/uitextview/1618597-init)Added [UITextView.layoutManager](https://developer.apple.com/documentation/uikit/uitextview/1618602-layoutmanager)Added [UITextView.linkTextAttributes](https://developer.apple.com/documentation/uikit/uitextview/1618632-linktextattributes)Added [UITextView.selectable](https://developer.apple.com/documentation/uikit/uitextview/1618627-isselectable)Added [UITextView.textContainer](https://developer.apple.com/documentation/uikit/uitextview/1618624-textcontainer)Added [UITextView.textContainerInset](https://developer.apple.com/documentation/uikit/uitextview/1618619-textcontainerinset)Added [UITextView.textStorage](https://developer.apple.com/documentation/uikit/uitextview/1618611-textstorage)Added [-[UITextViewDelegate textView:shouldInteractWithTextAttachment:inRange:]](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618621-textview)Added [-[UITextViewDelegate textView:shouldInteractWithURL:inRange:]](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618606-textview)UIToolbar.hRemoved [UIToolbarPosition](https://developer.apple.com/documentation/uikit/uitoolbar/uitoolbarposition)Removed [UIToolbarPositionAny](https://developer.apple.com/documentation/uikit/uitoolbar/uitoolbarposition/uitoolbarpositionany)Removed [UIToolbarPositionBottom](https://developer.apple.com/documentation/uikit/uitoolbar/uitoolbarposition/uitoolbarpositionbottom)Removed [UIToolbarPositionTop](https://developer.apple.com/documentation/uikit/uitoolbar/uitoolbarposition/uitoolbarpositiontop)Added [UIToolbar.barTintColor](https://developer.apple.com/documentation/uikit/uitoolbar/1618002-bartintcolor)Added [UIToolbar.delegate](https://developer.apple.com/documentation/uikit/uitoolbar/1617992-delegate)Added [UIToolbarDelegate](https://developer.apple.com/documentation/uikit/uitoolbardelegate)Modified [UIToolbar](https://developer.apple.com/documentation/uikit/uitoolbar)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | UIBarPositioning |

Modified [-[UIToolbar backgroundImageForToolbarPosition:barMetrics:]](https://developer.apple.com/documentation/uikit/uitoolbar/1617998-backgroundimagefortoolbarpositio)

|  | Declaration |
| --- | --- |
| From | - (UIImage \*)backgroundImageForToolbarPosition:(UIToolbarPosition)topOrBottom barMetrics:(UIBarMetrics)barMetrics |
| To | - (UIImage \*)backgroundImageForToolbarPosition:(UIBarPosition)topOrBottom barMetrics:(UIBarMetrics)barMetrics |

Modified [-[UIToolbar setBackgroundImage:forToolbarPosition:barMetrics:]](https://developer.apple.com/documentation/uikit/uitoolbar/1618003-setbackgroundimage)

|  | Declaration |
| --- | --- |
| From | - (void)setBackgroundImage:(UIImage \*)backgroundImage forToolbarPosition:(UIToolbarPosition)topOrBottom barMetrics:(UIBarMetrics)barMetrics |
| To | - (void)setBackgroundImage:(UIImage \*)backgroundImage forToolbarPosition:(UIBarPosition)topOrBottom barMetrics:(UIBarMetrics)barMetrics |

Modified [-[UIToolbar setShadowImage:forToolbarPosition:]](https://developer.apple.com/documentation/uikit/uitoolbar/1617991-setshadowimage)

|  | Declaration |
| --- | --- |
| From | - (void)setShadowImage:(UIImage \*)shadowImage forToolbarPosition:(UIToolbarPosition)topOrBottom |
| To | - (void)setShadowImage:(UIImage \*)shadowImage forToolbarPosition:(UIBarPosition)topOrBottom |

Modified [-[UIToolbar shadowImageForToolbarPosition:]](https://developer.apple.com/documentation/uikit/uitoolbar/1618000-shadowimage)

|  | Declaration |
| --- | --- |
| From | - (UIImage \*)shadowImageForToolbarPosition:(UIToolbarPosition)topOrBottom |
| To | - (UIImage \*)shadowImageForToolbarPosition:(UIBarPosition)topOrBottom |

UIView.hAdded [+[UIView addKeyframeWithRelativeStartTime:relativeDuration:animations:]](https://developer.apple.com/documentation/uikit/uiview/1622554-addkeyframewithrelativestarttime)Added [-[UIView addMotionEffect:]](https://developer.apple.com/documentation/uikit/uiview/1622586-addmotioneffect)Added [+[UIView animateKeyframesWithDuration:delay:options:animations:completion:]](https://developer.apple.com/documentation/uikit/uiview/1622552-animatekeyframes)Added [+[UIView animateWithDuration:delay:usingSpringWithDamping:initialSpringVelocity:options:animations:completion:]](https://developer.apple.com/documentation/uikit/uiview/1622594-animate)Added [-[UIView drawViewHierarchyInRect:afterScreenUpdates:]](https://developer.apple.com/documentation/uikit/uiview/1622589-drawviewhierarchyinrect)Added [UIView.motionEffects](https://developer.apple.com/documentation/uikit/uiview/1622428-motioneffects)Added [+[UIView performSystemAnimation:onViews:options:animations:completion:]](https://developer.apple.com/documentation/uikit/uiview/1622635-perform)Added [+[UIView performWithoutAnimation:]](https://developer.apple.com/documentation/uikit/uiview/1622484-performwithoutanimation)Added [-[UIView removeMotionEffect:]](https://developer.apple.com/documentation/uikit/uiview/1622481-removemotioneffect)Added [-[UIView resizableSnapshotViewFromRect:afterScreenUpdates:withCapInsets:]](https://developer.apple.com/documentation/uikit/uiview/1622597-resizablesnapshotview)Added [-[UIView snapshotViewAfterScreenUpdates:]](https://developer.apple.com/documentation/uikit/uiview/1622531-snapshotviewafterscreenupdates)Added [UIView.tintAdjustmentMode](https://developer.apple.com/documentation/uikit/uiview/1622555-tintadjustmentmode)Added [UIView.tintColor](https://developer.apple.com/documentation/uikit/uiview/1622467-tintcolor)Added [-[UIView tintColorDidChange]](https://developer.apple.com/documentation/uikit/uiview/1622620-tintcolordidchange)Added [UISystemAnimation](https://developer.apple.com/documentation/uikit/uisystemanimation)Added [UISystemAnimationDelete](https://developer.apple.com/documentation/uikit/uisystemanimation/uisystemanimationdelete)Added UIView(UISnapshotting)Added UIView(UIViewKeyframeAnimations)Added UIView(UIViewMotionEffects)Added [UIViewAnimationOptionOverrideInheritedOptions](https://developer.apple.com/documentation/uikit/uiviewanimationoptions/uiviewanimationoptionoverrideinheritedoptions)Added [UIViewKeyframeAnimationOptionAllowUserInteraction](https://developer.apple.com/documentation/uikit/uiview/keyframeanimationoptions/1622578-allowuserinteraction)Added [UIViewKeyframeAnimationOptionAutoreverse](https://developer.apple.com/documentation/uikit/uiview/keyframeanimationoptions/1622560-autoreverse)Added [UIViewKeyframeAnimationOptionBeginFromCurrentState](https://developer.apple.com/documentation/uikit/uiviewkeyframeanimationoptions/uiviewkeyframeanimationoptionbeginfromcurrentstate)Added [UIViewKeyframeAnimationOptionCalculationModeCubic](https://developer.apple.com/documentation/uikit/uiviewkeyframeanimationoptions/uiviewkeyframeanimationoptioncalculationmodecubic)Added [UIViewKeyframeAnimationOptionCalculationModeCubicPaced](https://developer.apple.com/documentation/uikit/uiviewkeyframeanimationoptions/uiviewkeyframeanimationoptioncalculationmodecubicpaced)Added [UIViewKeyframeAnimationOptionCalculationModeDiscrete](https://developer.apple.com/documentation/uikit/uiview/keyframeanimationoptions/1622537-calculationmodediscrete)Added [UIViewKeyframeAnimationOptionCalculationModeLinear](https://developer.apple.com/documentation/uikit/uiview/keyframeanimationoptions/1622592-calculationmodelinear)Added [UIViewKeyframeAnimationOptionCalculationModePaced](https://developer.apple.com/documentation/uikit/uiview/keyframeanimationoptions/1622525-calculationmodepaced)Added [UIViewKeyframeAnimationOptionLayoutSubviews](https://developer.apple.com/documentation/uikit/uiview/keyframeanimationoptions/1622492-layoutsubviews)Added [UIViewKeyframeAnimationOptionOverrideInheritedDuration](https://developer.apple.com/documentation/uikit/uiview/keyframeanimationoptions/1622569-overrideinheritedduration)Added [UIViewKeyframeAnimationOptionOverrideInheritedOptions](https://developer.apple.com/documentation/uikit/uiview/keyframeanimationoptions/1622530-overrideinheritedoptions)Added [UIViewKeyframeAnimationOptionRepeat](https://developer.apple.com/documentation/uikit/uiviewkeyframeanimationoptions/uiviewkeyframeanimationoptionrepeat)Added [UIViewKeyframeAnimationOptions](https://developer.apple.com/documentation/uikit/uiviewkeyframeanimationoptions)Added [UIViewTintAdjustmentMode](https://developer.apple.com/documentation/uikit/uiview/tintadjustmentmode)Added [UIViewTintAdjustmentModeAutomatic](https://developer.apple.com/documentation/uikit/uiviewtintadjustmentmode/uiviewtintadjustmentmodeautomatic)Added [UIViewTintAdjustmentModeDimmed](https://developer.apple.com/documentation/uikit/uiviewtintadjustmentmode/uiviewtintadjustmentmodedimmed)Added [UIViewTintAdjustmentModeNormal](https://developer.apple.com/documentation/uikit/uiviewtintadjustmentmode/uiviewtintadjustmentmodenormal)Modified [UIView](https://developer.apple.com/documentation/uikit/uiview)

|  | Protocols |
| --- | --- |
| From | NSCoding, UIAppearance, UIAppearanceContainer |
| To | NSCoding, UIAppearance, UIAppearanceContainer, UIDynamicItem |

UIViewController.hAdded [-[UIViewController applicationFinishedRestoringState]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621482-applicationfinishedrestoringstat)Added [UIViewController.automaticallyAdjustsScrollViewInsets](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621372-automaticallyadjustsscrollviewin)Added [UIViewController.bottomLayoutGuide](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621504-bottomlayoutguide)Added [-[UIViewController childViewControllerForStatusBarHidden]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621451-childviewcontrollerforstatusbarh)Added [-[UIViewController childViewControllerForStatusBarStyle]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621433-childviewcontrollerforstatusbars)Added [UIViewController.edgesForExtendedLayout](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621515-edgesforextendedlayout)Added [UIViewController.extendedLayoutIncludesOpaqueBars](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621404-extendedlayoutincludesopaquebars)Added [UIViewController.modalPresentationCapturesStatusBarAppearance](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621453-modalpresentationcapturesstatusb)Added [UIViewController.preferredContentSize](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621476-preferredcontentsize)Added [-[UIViewController preferredStatusBarStyle]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621416-preferredstatusbarstyle)Added [-[UIViewController preferredStatusBarUpdateAnimation]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621434-preferredstatusbarupdateanimatio)Added [-[UIViewController prefersStatusBarHidden]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621440-prefersstatusbarhidden)Added [-[UIViewController setNeedsStatusBarAppearanceUpdate]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621354-setneedsstatusbarappearanceupdat)Added [UIViewController.topLayoutGuide](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621367-toplayoutguide)Added [UIViewController.transitioningDelegate](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621421-transitioningdelegate)Added [UIModalPresentationCustom](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle/custom)Added [UIModalPresentationNone](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle/none)Added UIViewController(CustomTransitioning)Added UIViewController(UILayoutSupport)Modified [UIViewController.wantsFullScreenLayout](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621390-wantsfullscreenlayout)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 7.0 |

UIViewControllerTransitionCoordinator.hAdded [-[UIViewController transitionCoordinator]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1619294-transitioncoordinator)Added [UIViewControllerTransitionCoordinator](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinator)Added [-[UIViewControllerTransitionCoordinator animateAlongsideTransition:completion:]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinator/1619300-animatealongsidetransition)Added [-[UIViewControllerTransitionCoordinator animateAlongsideTransitionInView:animation:completion:]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinator/1619295-animatealongsidetransition)Added [-[UIViewControllerTransitionCoordinator notifyWhenInteractionEndsUsingBlock:]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinator/1619292-notifywheninteractionends)Added [UIViewControllerTransitionCoordinatorContext](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext)Added [-[UIViewControllerTransitionCoordinatorContext completionCurve]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/1619299-completioncurve)Added [-[UIViewControllerTransitionCoordinatorContext completionVelocity]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/1619282-completionvelocity)Added [-[UIViewControllerTransitionCoordinatorContext containerView]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/1619280-containerview)Added [-[UIViewControllerTransitionCoordinatorContext initiallyInteractive]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/1619285-initiallyinteractive)Added -[UIViewControllerTransitionCoordinatorContext isAnimated]Added -[UIViewControllerTransitionCoordinatorContext isCancelled]Added -[UIViewControllerTransitionCoordinatorContext isInteractive]Added [-[UIViewControllerTransitionCoordinatorContext percentComplete]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/1619290-percentcomplete)Added [-[UIViewControllerTransitionCoordinatorContext presentationStyle]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/1619287-presentationstyle)Added [-[UIViewControllerTransitionCoordinatorContext transitionDuration]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/1619286-transitionduration)Added [-[UIViewControllerTransitionCoordinatorContext viewControllerForKey:]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/1619293-viewcontrollerforkey)Added UIViewController(TransitionCoordinator)UIViewControllerTransitioning.hAdded [UIPercentDrivenInteractiveTransition](https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition)Added [-[UIPercentDrivenInteractiveTransition cancelInteractiveTransition]](https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/1622026-cancelinteractivetransition)Added [UIPercentDrivenInteractiveTransition.completionCurve](https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/1622048-completioncurve)Added [UIPercentDrivenInteractiveTransition.completionSpeed](https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/1622052-completionspeed)Added [UIPercentDrivenInteractiveTransition.duration](https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/1622029-duration)Added [-[UIPercentDrivenInteractiveTransition finishInteractiveTransition]](https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/1622035-finish)Added [UIPercentDrivenInteractiveTransition.percentComplete](https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/1622053-percentcomplete)Added [-[UIPercentDrivenInteractiveTransition updateInteractiveTransition:]](https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/1622051-update)Added [UIViewControllerAnimatedTransitioning](https://developer.apple.com/documentation/uikit/uiviewcontrolleranimatedtransitioning)Added [-[UIViewControllerAnimatedTransitioning animateTransition:]](https://developer.apple.com/documentation/uikit/uiviewcontrolleranimatedtransitioning/1622061-animatetransition)Added [-[UIViewControllerAnimatedTransitioning animationEnded:]](https://developer.apple.com/documentation/uikit/uiviewcontrolleranimatedtransitioning/1622059-animationended)Added [-[UIViewControllerAnimatedTransitioning transitionDuration:]](https://developer.apple.com/documentation/uikit/uiviewcontrolleranimatedtransitioning/1622032-transitionduration)Added [UIViewControllerContextTransitioning](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning)Added [-[UIViewControllerContextTransitioning cancelInteractiveTransition]](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/1622038-cancelinteractivetransition)Added [-[UIViewControllerContextTransitioning completeTransition:]](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/1622042-completetransition)Added [-[UIViewControllerContextTransitioning containerView]](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/1622045-containerview)Added [-[UIViewControllerContextTransitioning finalFrameForViewController:]](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/1622024-finalframe)Added [-[UIViewControllerContextTransitioning finishInteractiveTransition]](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/1622056-finishinteractivetransition)Added [-[UIViewControllerContextTransitioning initialFrameForViewController:]](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/1622033-initialframeforviewcontroller)Added -[UIViewControllerContextTransitioning isAnimated]Added -[UIViewControllerContextTransitioning isInteractive]Added [-[UIViewControllerContextTransitioning presentationStyle]](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/1622049-presentationstyle)Added [-[UIViewControllerContextTransitioning transitionWasCancelled]](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/1622039-transitionwascancelled)Added [-[UIViewControllerContextTransitioning updateInteractiveTransition:]](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/1622025-updateinteractivetransition)Added [-[UIViewControllerContextTransitioning viewControllerForKey:]](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/1622043-viewcontrollerforkey)Added [UIViewControllerInteractiveTransitioning](https://developer.apple.com/documentation/uikit/uiviewcontrollerinteractivetransitioning)Added [-[UIViewControllerInteractiveTransitioning completionCurve]](https://developer.apple.com/documentation/uikit/uiviewcontrollerinteractivetransitioning/1622027-completioncurve)Added [-[UIViewControllerInteractiveTransitioning completionSpeed]](https://developer.apple.com/documentation/uikit/uiviewcontrollerinteractivetransitioning/1622031-completionspeed)Added [-[UIViewControllerInteractiveTransitioning startInteractiveTransition:]](https://developer.apple.com/documentation/uikit/uiviewcontrollerinteractivetransitioning/1622028-startinteractivetransition)Added [UIViewControllerTransitioningDelegate](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioningdelegate)Added [-[UIViewControllerTransitioningDelegate animationControllerForDismissedController:]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioningdelegate/1622047-animationcontroller)Added [-[UIViewControllerTransitioningDelegate animationControllerForPresentedController:presentingController:sourceController:]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioningdelegate/1622037-animationcontroller)Added [-[UIViewControllerTransitioningDelegate interactionControllerForDismissal:]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioningdelegate/1622030-interactioncontrollerfordismissa)Added [-[UIViewControllerTransitioningDelegate interactionControllerForPresentation:]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioningdelegate/1622050-interactioncontrollerforpresenta)Added [UITransitionContextFromViewControllerKey](https://developer.apple.com/documentation/uikit/uitransitioncontextfromviewcontrollerkey)Added [UITransitionContextToViewControllerKey](https://developer.apple.com/documentation/uikit/uitransitioncontexttoviewcontrollerkey)UIWebView.hAdded [UIWebView.gapBetweenPages](https://developer.apple.com/documentation/uikit/uiwebview/1617943-gapbetweenpages)Added [UIWebView.pageCount](https://developer.apple.com/documentation/uikit/uiwebview/1617968-pagecount)Added [UIWebView.pageLength](https://developer.apple.com/documentation/uikit/uiwebview/1617980-pagelength)Added [UIWebView.paginationBreakingMode](https://developer.apple.com/documentation/uikit/uiwebview/1617933-paginationbreakingmode)Added [UIWebView.paginationMode](https://developer.apple.com/documentation/uikit/uiwebview/1617985-paginationmode)Added [UIWebPaginationBreakingMode](https://developer.apple.com/documentation/uikit/uiwebpaginationbreakingmode)Added [UIWebPaginationBreakingModeColumn](https://developer.apple.com/documentation/uikit/uiwebview/paginationbreakingmode/column)Added [UIWebPaginationBreakingModePage](https://developer.apple.com/documentation/uikit/uiwebview/paginationbreakingmode/page)Added [UIWebPaginationMode](https://developer.apple.com/documentation/uikit/uiwebview/paginationmode)Added [UIWebPaginationModeBottomToTop](https://developer.apple.com/documentation/uikit/uiwebview/paginationmode/bottomtotop)Added [UIWebPaginationModeLeftToRight](https://developer.apple.com/documentation/uikit/uiwebpaginationmode/uiwebpaginationmodelefttoright)Added [UIWebPaginationModeRightToLeft](https://developer.apple.com/documentation/uikit/uiwebpaginationmode/uiwebpaginationmoderighttoleft)Added [UIWebPaginationModeTopToBottom](https://developer.apple.com/documentation/uikit/uiwebview/paginationmode/toptobottom)Added [UIWebPaginationModeUnpaginated](https://developer.apple.com/documentation/uikit/uiwebview/paginationmode/unpaginated)

## VideoToolbox

No changes

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
