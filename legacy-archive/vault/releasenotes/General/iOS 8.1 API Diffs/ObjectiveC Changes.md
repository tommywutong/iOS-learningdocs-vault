---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/ObjectiveC.html
archived_at: '2026-07-18T02:56:15.197294Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# ObjectiveC Changes

## ObjectiveC

Removed ObjCBool.convertFromBooleanLiteral(Bool) -> ObjCBool [static]Removed Selector.convertFromExtendedGraphemeClusterLiteral(String) -> Selector [static]Removed Selector.convertFromNilLiteral() -> Selector [static]Removed Selector.convertFromStringLiteral(String) -> Selector [static]Added NSObject.debugDescription() -> String [class]Added NSObject.description() -> String [class]Added NSObjectProtocol.debugDescriptionAdded NSObjectProtocol.descriptionAdded NSZone.init(nilLiteral: ())Added ObjCBool.init(booleanLiteral: Bool)Added Selector.init(extendedGraphemeClusterLiteral: String)Added Selector.init(nilLiteral: ())Added Selector.init(stringLiteral: String)Added Selector.init(unicodeScalarLiteral: String)Modified NSObject

|  | Protocols | Introduction |
| --- | --- | --- |
| From | AnyObject, NSObjectProtocol | iOS 8.0 |
| To | AnyObject, CVarArgType, Equatable, Hashable, NSObjectProtocol, Printable | iOS 2.0 |

Modified NSObject.allocWithZone(NSZone) -> Self! [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func allocWithZone(_ zone: COpaquePointer) -> Self! ``` | iOS 8.0 |
| To | ``` class func allocWithZone(_ zone: NSZone) -> Self! ``` | iOS 8.1 |

Modified NSObject.forwardingTargetForSelector(Selector) -> AnyObject?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSObject.resolveClassMethod(Selector) -> Bool [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSObject.resolveInstanceMethod(Selector) -> Bool [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSZone [struct]

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` struct NSZone : NilLiteralConvertible {     var pointer: COpaquePointer     init()     static func convertFromNilLiteral() -> NSZone } ``` | Foundation |
| To | ``` struct NSZone : NilLiteralConvertible {     var pointer: COpaquePointer     init()     init(nilLiteral nilLiteral: ()) } ``` | ObjectiveC |

Modified NSZone.init()

|  | Module |
| --- | --- |
| From | Foundation |
| To | ObjectiveC |

Modified NSZone.pointer

|  | Module |
| --- | --- |
| From | Foundation |
| To | ObjectiveC |

Modified ObjCBool [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ObjCBool : BooleanType, BooleanLiteralConvertible {     var value: Int8     init(_ value: Int8)     init(_ value: Bool)     var boolValue: Bool { get }     static func convertFromBooleanLiteral(_ value: Bool) -> ObjCBool } ``` |
| To | ``` struct ObjCBool : BooleanType, BooleanLiteralConvertible {     var value: Int8     init(_ value: Int8)     init(_ value: Bool)     var boolValue: Bool { get }     init(booleanLiteral value: Bool) } ``` |

Modified Selector [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Selector : StringLiteralConvertible, NilLiteralConvertible {     var ptr: COpaquePointer     init(_ str: String)     static func convertFromExtendedGraphemeClusterLiteral(_ value: String) -> Selector     static func convertFromStringLiteral(_ value: String) -> Selector     init()     static func convertFromNilLiteral() -> Selector } ``` |
| To | ``` struct Selector : StringLiteralConvertible, NilLiteralConvertible {     var ptr: COpaquePointer     init(_ str: String)     init(unicodeScalarLiteral value: String)     init(extendedGraphemeClusterLiteral value: String)     init(stringLiteral value: String)     init()     init(nilLiteral nilLiteral: ()) } ``` |

Modified objc_object [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct objc_object { } ``` |
| To | ``` struct objc_object {     var isa: AnyClass! } ``` |

Modified class_addIvar(AnyClass!, UnsafePointer<Int8>, UInt, UInt8, UnsafePointer<Int8>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_addMethod(AnyClass!, Selector, IMP, UnsafePointer<Int8>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_addProperty(AnyClass!, UnsafePointer<Int8>, UnsafePointer<objc_property_attribute_t>, UInt32) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified class_addProtocol(AnyClass!, Protocol!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_conformsToProtocol(AnyClass!, Protocol!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_copyIvarList(AnyClass!, UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<Ivar>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_copyMethodList(AnyClass!, UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<Method>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_copyPropertyList(AnyClass!, UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<objc_property_t>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_copyProtocolList(AnyClass!, UnsafeMutablePointer<UInt32>) -> AutoreleasingUnsafeMutablePointer<Protocol?>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_getClassMethod(AnyClass!, Selector) -> Method

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_getClassVariable(AnyClass!, UnsafePointer<Int8>) -> Ivar

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_getImageName(AnyClass!) -> UnsafePointer<Int8>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_getInstanceMethod(AnyClass!, Selector) -> Method

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_getInstanceSize(AnyClass!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_getInstanceVariable(AnyClass!, UnsafePointer<Int8>) -> Ivar

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_getIvarLayout(AnyClass!) -> UnsafePointer<UInt8>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_getMethodImplementation(AnyClass!, Selector) -> IMP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_getMethodImplementation_stret(AnyClass!, Selector) -> IMP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_getName(AnyClass!) -> UnsafePointer<Int8>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_getProperty(AnyClass!, UnsafePointer<Int8>) -> objc_property_t

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_getSuperclass(AnyClass!) -> AnyClass!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_getVersion(AnyClass!) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_getWeakIvarLayout(AnyClass!) -> UnsafePointer<UInt8>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_isMetaClass(AnyClass!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_replaceMethod(AnyClass!, Selector, IMP, UnsafePointer<Int8>) -> IMP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_replaceProperty(AnyClass!, UnsafePointer<Int8>, UnsafePointer<objc_property_attribute_t>, UInt32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified class_respondsToSelector(AnyClass!, Selector) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_setIvarLayout(AnyClass!, UnsafePointer<UInt8>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_setVersion(AnyClass!, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified class_setWeakIvarLayout(AnyClass!, UnsafePointer<UInt8>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified imp_getBlock(IMP) -> AnyObject!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified imp_implementationWithBlock(AnyObject!) -> IMP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified imp_removeBlock(IMP) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified ivar_getName(Ivar) -> UnsafePointer<Int8>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified ivar_getOffset(Ivar) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified ivar_getTypeEncoding(Ivar) -> UnsafePointer<Int8>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified method_copyArgumentType(Method, UInt32) -> UnsafeMutablePointer<Int8>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified method_copyReturnType(Method) -> UnsafeMutablePointer<Int8>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified method_exchangeImplementations(Method, Method)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified method_getArgumentType(Method, UInt32, UnsafeMutablePointer<Int8>, UInt)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified method_getDescription(Method) -> UnsafeMutablePointer<objc_method_description>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified method_getImplementation(Method) -> IMP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified method_getName(Method) -> Selector

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified method_getNumberOfArguments(Method) -> UInt32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified method_getReturnType(Method, UnsafeMutablePointer<Int8>, UInt)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified method_getTypeEncoding(Method) -> UnsafePointer<Int8>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified method_setImplementation(Method, IMP) -> IMP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified objc_allocateClassPair(AnyClass!, UnsafePointer<Int8>, UInt) -> AnyClass!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified objc_allocateProtocol(UnsafePointer<Int8>) -> Protocol!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified objc_begin_catch(UnsafeMutablePointer<Void>) -> AnyObject!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified objc_copyClassList(UnsafeMutablePointer<UInt32>) -> AutoreleasingUnsafeMutablePointer<AnyClass?>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.1 |

Modified objc_copyClassNamesForImage(UnsafePointer<Int8>, UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<UnsafePointer<Int8>>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified objc_copyImageNames(UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<UnsafePointer<Int8>>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified objc_copyProtocolList(UnsafeMutablePointer<UInt32>) -> AutoreleasingUnsafeMutablePointer<Protocol?>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified objc_disposeClassPair(AnyClass!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified objc_duplicateClass(AnyClass!, UnsafePointer<Int8>, UInt) -> AnyClass!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified objc_end_catch()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified objc_enumerationMutation(AnyObject!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified objc_exception_rethrow()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified objc_exception_throw(AnyObject!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified objc_getAssociatedObject(AnyObject!, UnsafePointer<Void>) -> AnyObject!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.1 |

Modified objc_getClass(UnsafePointer<Int8>) -> AnyObject!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified objc_getClassList(AutoreleasingUnsafeMutablePointer<AnyClass?>, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified objc_getMetaClass(UnsafePointer<Int8>) -> AnyObject!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified objc_getProtocol(UnsafePointer<Int8>) -> Protocol!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified objc_getRequiredClass(UnsafePointer<Int8>) -> AnyClass!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified objc_loadWeak(AutoreleasingUnsafeMutablePointer<AnyObject?>) -> AnyObject!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified objc_lookUpClass(UnsafePointer<Int8>) -> AnyClass!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified objc_registerClassPair(AnyClass!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified objc_registerProtocol(Protocol!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified objc_removeAssociatedObjects(AnyObject!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.1 |

Modified objc_setAssociatedObject(AnyObject!, UnsafePointer<Void>, AnyObject!, objc_AssociationPolicy)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.1 |

Modified objc_setEnumerationMutationHandler(CFunctionPointer<((AnyObject!) -> Void)>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified objc_setExceptionMatcher(objc_exception_matcher) -> objc_exception_matcher

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified objc_setExceptionPreprocessor(objc_exception_preprocessor) -> objc_exception_preprocessor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified objc_setForwardHandler(UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified objc_setUncaughtExceptionHandler(objc_uncaught_exception_handler) -> objc_uncaught_exception_handler

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified objc_storeWeak(AutoreleasingUnsafeMutablePointer<AnyObject?>, AnyObject!) -> AnyObject!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified objc_sync_enter(AnyObject!) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified objc_sync_exit(AnyObject!) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified objc_terminate()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified object_getClass(AnyObject!) -> AnyClass!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified object_getClassName(AnyObject!) -> UnsafePointer<Int8>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified object_getIvar(AnyObject!, Ivar) -> AnyObject!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified object_setClass(AnyObject!, AnyClass!) -> AnyClass!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified object_setIvar(AnyObject!, Ivar, AnyObject!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified property_copyAttributeList(objc_property_t, UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<objc_property_attribute_t>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified property_copyAttributeValue(objc_property_t, UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified property_getAttributes(objc_property_t) -> UnsafePointer<Int8>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified property_getName(objc_property_t) -> UnsafePointer<Int8>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified protocol_addMethodDescription(Protocol!, Selector, UnsafePointer<Int8>, Bool, Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified protocol_addProperty(Protocol!, UnsafePointer<Int8>, UnsafePointer<objc_property_attribute_t>, UInt32, Bool, Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified protocol_addProtocol(Protocol!, Protocol!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified protocol_conformsToProtocol(Protocol!, Protocol!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified protocol_copyMethodDescriptionList(Protocol!, Bool, Bool, UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<objc_method_description>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified protocol_copyPropertyList(Protocol!, UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<objc_property_t>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified protocol_copyProtocolList(Protocol!, UnsafeMutablePointer<UInt32>) -> AutoreleasingUnsafeMutablePointer<Protocol?>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified protocol_getMethodDescription(Protocol!, Selector, Bool, Bool) -> objc_method_description

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified protocol_getName(Protocol!) -> UnsafePointer<Int8>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified protocol_getProperty(Protocol!, UnsafePointer<Int8>, Bool, Bool) -> objc_property_t

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified protocol_isEqual(Protocol!, Protocol!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified sel_getName(Selector) -> UnsafePointer<Int8>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified sel_getUid(UnsafePointer<Int8>) -> Selector

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified sel_isEqual(Selector, Selector) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified sel_isMapped(Selector) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified sel_registerName(UnsafePointer<Int8>) -> Selector

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

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
