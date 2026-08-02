---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/ObjectiveC.html
archived_at: '2026-07-18T02:52:34.329532Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# ObjectiveC Changes

## ObjectiveC

Removed ObjCBool.convertFromBooleanLiteral(Bool) -> ObjCBool [static]Removed ObjCBool.getLogicValue() -> BoolRemoved ObjCBool.getMirror() -> MirrorRemoved Selector.convertFromExtendedGraphemeClusterLiteral(String) -> Selector [static]Removed Selector.convertFromNilLiteral() -> Selector [static]Removed Selector.convertFromStringLiteral(String) -> Selector [static]Removed Selector.getMirror() -> MirrorRemoved NSUIntegerMaxAdded NSObject.debugDescription() -> String [class]Added NSObject.description() -> String [class]Added NSObjectProtocol.debugDescriptionAdded NSObjectProtocol.descriptionAdded NSZone.init(nilLiteral: ())Added ObjCBool.boolValueAdded ObjCBool.init(booleanLiteral: Bool)Added ObjCBool.getMirror() -> MirrorTypeAdded Selector.init(extendedGraphemeClusterLiteral: String)Added Selector.getMirror() -> MirrorTypeAdded Selector.init(nilLiteral: ())Added Selector.init(stringLiteral: String)Added Selector.init(unicodeScalarLiteral: String)Added objc_method_description.init()Added objc_method_description.init(name: Selector, types: UnsafeMutablePointer<Int8>)Added objc_object.init()Added objc_object.init(isa: AnyClass!)Added objc_property_attribute_t.init()Added objc_property_attribute_t.init(name: UnsafePointer<Int8>, value: UnsafePointer<Int8>)Added objc_super.init()Added objc_super.init(receiver: AnyObject!, super_class: AnyClass!)Added object_isClass(AnyObject!) -> BoolModified NSObject

|  | Protocols | Introduction |
| --- | --- | --- |
| From | AnyObject, NSObjectProtocol | OS X 10.10 |
| To | AnyObject, CVarArgType, Equatable, Hashable, NSObjectProtocol, Printable | OS X 10.0 |

Modified NSObject.alloc() -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func alloc() -> Self! ``` | OS X 10.10 |
| To | ``` class func alloc() -> Self ``` | OS X 10.10.3 |

Modified NSObject.allocWithZone(NSZone) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func allocWithZone(_ zone: COpaquePointer) -> Self! ``` | OS X 10.10 |
| To | ``` class func allocWithZone(_ zone: NSZone) -> Self ``` | OS X 10.10.3 |

Modified NSObject.conformsToProtocol(Protocol) -> Bool [class]

|  | Declaration |
| --- | --- |
| From | ``` class func conformsToProtocol(_ `protocol`: Protocol!) -> Bool ``` |
| To | ``` class func conformsToProtocol(_ `protocol`: Protocol) -> Bool ``` |

Modified NSObject.copy() -> AnyObject

|  | Declaration |
| --- | --- |
| From | ``` func copy() -> AnyObject! ``` |
| To | ``` func copy() -> AnyObject ``` |

Modified NSObject.forwardingTargetForSelector(Selector) -> AnyObject?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func forwardingTargetForSelector(_ aSelector: Selector) -> AnyObject! ``` | OS X 10.10 |
| To | ``` func forwardingTargetForSelector(_ aSelector: Selector) -> AnyObject? ``` | OS X 10.5 |

Modified NSObject.isSubclassOfClass(AnyClass) -> Bool [class]

|  | Declaration |
| --- | --- |
| From | ``` class func isSubclassOfClass(_ aClass: AnyClass!) -> Bool ``` |
| To | ``` class func isSubclassOfClass(_ aClass: AnyClass) -> Bool ``` |

Modified NSObject.mutableCopy() -> AnyObject

|  | Declaration |
| --- | --- |
| From | ``` func mutableCopy() -> AnyObject! ``` |
| To | ``` func mutableCopy() -> AnyObject ``` |

Modified NSObject.new() -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func `new`() -> Self! ``` | OS X 10.10 |
| To | ``` class func new() -> Self ``` | OS X 10.10.3 |

Modified NSObject.resolveClassMethod(Selector) -> Bool [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSObject.resolveInstanceMethod(Selector) -> Bool [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSObject.superclass() -> AnyClass? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func superclass() -> AnyClass! ``` |
| To | ``` class func superclass() -> AnyClass? ``` |

Modified NSObjectProtocol.conformsToProtocol(Protocol) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func conformsToProtocol(_ aProtocol: Protocol!) -> Bool ``` |
| To | ``` func conformsToProtocol(_ aProtocol: Protocol) -> Bool ``` |

Modified NSObjectProtocol.isEqual(AnyObject?) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isEqual(_ object: AnyObject!) -> Bool ``` |
| To | ``` func isEqual(_ object: AnyObject?) -> Bool ``` |

Modified NSObjectProtocol.isKindOfClass(AnyClass) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isKindOfClass(_ aClass: AnyClass!) -> Bool ``` |
| To | ``` func isKindOfClass(_ aClass: AnyClass) -> Bool ``` |

Modified NSObjectProtocol.isMemberOfClass(AnyClass) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isMemberOfClass(_ aClass: AnyClass!) -> Bool ``` |
| To | ``` func isMemberOfClass(_ aClass: AnyClass) -> Bool ``` |

Modified NSObjectProtocol.self() -> Self

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func `self`() -> Self! ``` | OS X 10.10 |
| To | ``` func `self`() -> Self ``` | OS X 10.10.3 |

Modified NSObjectProtocol.superclass

|  | Declaration |
| --- | --- |
| From | ``` var superclass: AnyClass! { get } ``` |
| To | ``` var superclass: AnyClass? { get } ``` |

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

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct ObjCBool : LogicValue, BooleanLiteralConvertible {     var value: Int8     init(_ value: Int8)     init(_ value: Bool)     func getLogicValue() -> Bool     static func convertFromBooleanLiteral(_ value: Bool) -> ObjCBool } ``` | BooleanLiteralConvertible, LogicValue, Printable, Reflectable |
| To | ``` struct ObjCBool : BooleanType, BooleanLiteralConvertible {     var value: Int8     init(_ value: Int8)     init(_ value: Bool)     var boolValue: Bool { get }     init(booleanLiteral value: Bool) } ``` | BooleanLiteralConvertible, BooleanType, Printable, Reflectable |

Modified Protocol

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified Selector [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Selector : StringLiteralConvertible, NilLiteralConvertible {     var ptr: COpaquePointer     init(_ str: String)     static func convertFromExtendedGraphemeClusterLiteral(_ value: String) -> Selector     static func convertFromStringLiteral(_ value: String) -> Selector     init()     static func convertFromNilLiteral() -> Selector } ``` |
| To | ``` struct Selector : StringLiteralConvertible, NilLiteralConvertible {     var ptr: COpaquePointer     init(_ str: String)     init(unicodeScalarLiteral value: String)     init(extendedGraphemeClusterLiteral value: String)     init(stringLiteral value: String)     init()     init(nilLiteral nilLiteral: ()) } ``` |

Modified objc_method_description [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct objc_method_description {     var name: Selector     var types: UnsafePointer<Int8> } ``` |
| To | ``` struct objc_method_description {     var name: Selector     var types: UnsafeMutablePointer<Int8>     init()     init(name name: Selector, types types: UnsafeMutablePointer<Int8>) } ``` |

Modified objc_method_description.types

|  | Declaration |
| --- | --- |
| From | ``` var types: UnsafePointer<Int8> ``` |
| To | ``` var types: UnsafeMutablePointer<Int8> ``` |

Modified objc_object [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct objc_object { } ``` |
| To | ``` struct objc_object {     var isa: AnyClass!     init()     init(isa isa: AnyClass!) } ``` |

Modified objc_property_attribute_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct objc_property_attribute_t {     var name: ConstUnsafePointer<Int8>     var value: ConstUnsafePointer<Int8> } ``` |
| To | ``` struct objc_property_attribute_t {     var name: UnsafePointer<Int8>     var value: UnsafePointer<Int8>     init()     init(name name: UnsafePointer<Int8>, value value: UnsafePointer<Int8>) } ``` |

Modified objc_property_attribute_t.name

|  | Declaration |
| --- | --- |
| From | ``` var name: ConstUnsafePointer<Int8> ``` |
| To | ``` var name: UnsafePointer<Int8> ``` |

Modified objc_property_attribute_t.value

|  | Declaration |
| --- | --- |
| From | ``` var value: ConstUnsafePointer<Int8> ``` |
| To | ``` var value: UnsafePointer<Int8> ``` |

Modified objc_super [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct objc_super {     var receiver: AnyObject!     var super_class: AnyClass! } ``` |
| To | ``` struct objc_super {     var receiver: AnyObject!     var super_class: AnyClass!     init()     init(receiver receiver: AnyObject!, super_class super_class: AnyClass!) } ``` |

Modified autoreleasepool(() -> ())

|  | Declaration |
| --- | --- |
| From | ``` func autoreleasepool(_ code: () -> ()) ``` |
| To | ``` func autoreleasepool(_ code: @noescape () -> ()) ``` |

Modified class_addIvar(AnyClass!, UnsafePointer<Int8>, Int, UInt8, UnsafePointer<Int8>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func class_addIvar(_ cls: AnyClass!, _ name: ConstUnsafePointer<Int8>, _ size: UInt, _ alignment: UInt8, _ types: ConstUnsafePointer<Int8>) -> Bool ``` | OS X 10.10 |
| To | ``` func class_addIvar(_ cls: AnyClass!, _ name: UnsafePointer<Int8>, _ size: Int, _ alignment: UInt8, _ types: UnsafePointer<Int8>) -> Bool ``` | OS X 10.5 |

Modified class_addMethod(AnyClass!, Selector, IMP, UnsafePointer<Int8>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func class_addMethod(_ cls: AnyClass!, _ name: Selector, _ imp: IMP, _ types: ConstUnsafePointer<Int8>) -> Bool ``` | OS X 10.10 |
| To | ``` func class_addMethod(_ cls: AnyClass!, _ name: Selector, _ imp: IMP, _ types: UnsafePointer<Int8>) -> Bool ``` | OS X 10.5 |

Modified class_addProperty(AnyClass!, UnsafePointer<Int8>, UnsafePointer<objc_property_attribute_t>, UInt32) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func class_addProperty(_ cls: AnyClass!, _ name: ConstUnsafePointer<Int8>, _ attributes: ConstUnsafePointer<objc_property_attribute_t>, _ attributeCount: UInt32) -> Bool ``` | OS X 10.10 |
| To | ``` func class_addProperty(_ cls: AnyClass!, _ name: UnsafePointer<Int8>, _ attributes: UnsafePointer<objc_property_attribute_t>, _ attributeCount: UInt32) -> Bool ``` | OS X 10.7 |

Modified class_addProtocol(AnyClass!, Protocol!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified class_conformsToProtocol(AnyClass!, Protocol!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified class_copyIvarList(AnyClass!, UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<Ivar>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func class_copyIvarList(_ cls: AnyClass!, _ outCount: UnsafePointer<UInt32>) -> UnsafePointer<Ivar> ``` | OS X 10.10 |
| To | ``` func class_copyIvarList(_ cls: AnyClass!, _ outCount: UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<Ivar> ``` | OS X 10.5 |

Modified class_copyMethodList(AnyClass!, UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<Method>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func class_copyMethodList(_ cls: AnyClass!, _ outCount: UnsafePointer<UInt32>) -> UnsafePointer<Method> ``` | OS X 10.10 |
| To | ``` func class_copyMethodList(_ cls: AnyClass!, _ outCount: UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<Method> ``` | OS X 10.5 |

Modified class_copyPropertyList(AnyClass!, UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<objc_property_t>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func class_copyPropertyList(_ cls: AnyClass!, _ outCount: UnsafePointer<UInt32>) -> UnsafePointer<objc_property_t> ``` | OS X 10.10 |
| To | ``` func class_copyPropertyList(_ cls: AnyClass!, _ outCount: UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<objc_property_t> ``` | OS X 10.5 |

Modified class_copyProtocolList(AnyClass!, UnsafeMutablePointer<UInt32>) -> AutoreleasingUnsafeMutablePointer<Protocol?>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func class_copyProtocolList(_ cls: AnyClass!, _ outCount: UnsafePointer<UInt32>) -> AutoreleasingUnsafePointer<Protocol?> ``` | OS X 10.10 |
| To | ``` func class_copyProtocolList(_ cls: AnyClass!, _ outCount: UnsafeMutablePointer<UInt32>) -> AutoreleasingUnsafeMutablePointer<Protocol?> ``` | OS X 10.5 |

Modified class_getClassMethod(AnyClass!, Selector) -> Method

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified class_getClassVariable(AnyClass!, UnsafePointer<Int8>) -> Ivar

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func class_getClassVariable(_ cls: AnyClass!, _ name: ConstUnsafePointer<Int8>) -> Ivar ``` | OS X 10.10 |
| To | ``` func class_getClassVariable(_ cls: AnyClass!, _ name: UnsafePointer<Int8>) -> Ivar ``` | OS X 10.5 |

Modified class_getImageName(AnyClass!) -> UnsafePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func class_getImageName(_ cls: AnyClass!) -> ConstUnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` func class_getImageName(_ cls: AnyClass!) -> UnsafePointer<Int8> ``` | OS X 10.5 |

Modified class_getInstanceMethod(AnyClass!, Selector) -> Method

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified class_getInstanceSize(AnyClass!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func class_getInstanceSize(_ cls: AnyClass!) -> UInt ``` | OS X 10.10 |
| To | ``` func class_getInstanceSize(_ cls: AnyClass!) -> Int ``` | OS X 10.5 |

Modified class_getInstanceVariable(AnyClass!, UnsafePointer<Int8>) -> Ivar

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func class_getInstanceVariable(_ cls: AnyClass!, _ name: ConstUnsafePointer<Int8>) -> Ivar ``` | OS X 10.10 |
| To | ``` func class_getInstanceVariable(_ cls: AnyClass!, _ name: UnsafePointer<Int8>) -> Ivar ``` | OS X 10.0 |

Modified class_getIvarLayout(AnyClass!) -> UnsafePointer<UInt8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func class_getIvarLayout(_ cls: AnyClass!) -> ConstUnsafePointer<UInt8> ``` | OS X 10.10 |
| To | ``` func class_getIvarLayout(_ cls: AnyClass!) -> UnsafePointer<UInt8> ``` | OS X 10.5 |

Modified class_getMethodImplementation(AnyClass!, Selector) -> IMP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified class_getMethodImplementation_stret(AnyClass!, Selector) -> IMP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified class_getName(AnyClass!) -> UnsafePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func class_getName(_ cls: AnyClass!) -> ConstUnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` func class_getName(_ cls: AnyClass!) -> UnsafePointer<Int8> ``` | OS X 10.5 |

Modified class_getProperty(AnyClass!, UnsafePointer<Int8>) -> objc_property_t

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func class_getProperty(_ cls: AnyClass!, _ name: ConstUnsafePointer<Int8>) -> objc_property_t ``` | OS X 10.10 |
| To | ``` func class_getProperty(_ cls: AnyClass!, _ name: UnsafePointer<Int8>) -> objc_property_t ``` | OS X 10.5 |

Modified class_getSuperclass(AnyClass!) -> AnyClass!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified class_getVersion(AnyClass!) -> Int32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified class_getWeakIvarLayout(AnyClass!) -> UnsafePointer<UInt8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func class_getWeakIvarLayout(_ cls: AnyClass!) -> ConstUnsafePointer<UInt8> ``` | OS X 10.10 |
| To | ``` func class_getWeakIvarLayout(_ cls: AnyClass!) -> UnsafePointer<UInt8> ``` | OS X 10.5 |

Modified class_isMetaClass(AnyClass!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified class_replaceMethod(AnyClass!, Selector, IMP, UnsafePointer<Int8>) -> IMP

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func class_replaceMethod(_ cls: AnyClass!, _ name: Selector, _ imp: IMP, _ types: ConstUnsafePointer<Int8>) -> IMP ``` | OS X 10.10 |
| To | ``` func class_replaceMethod(_ cls: AnyClass!, _ name: Selector, _ imp: IMP, _ types: UnsafePointer<Int8>) -> IMP ``` | OS X 10.5 |

Modified class_replaceProperty(AnyClass!, UnsafePointer<Int8>, UnsafePointer<objc_property_attribute_t>, UInt32)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func class_replaceProperty(_ cls: AnyClass!, _ name: ConstUnsafePointer<Int8>, _ attributes: ConstUnsafePointer<objc_property_attribute_t>, _ attributeCount: UInt32) ``` | OS X 10.10 |
| To | ``` func class_replaceProperty(_ cls: AnyClass!, _ name: UnsafePointer<Int8>, _ attributes: UnsafePointer<objc_property_attribute_t>, _ attributeCount: UInt32) ``` | OS X 10.7 |

Modified class_respondsToSelector(AnyClass!, Selector) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified class_setIvarLayout(AnyClass!, UnsafePointer<UInt8>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func class_setIvarLayout(_ cls: AnyClass!, _ layout: ConstUnsafePointer<UInt8>) ``` | OS X 10.10 |
| To | ``` func class_setIvarLayout(_ cls: AnyClass!, _ layout: UnsafePointer<UInt8>) ``` | OS X 10.5 |

Modified class_setVersion(AnyClass!, Int32)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified class_setWeakIvarLayout(AnyClass!, UnsafePointer<UInt8>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func class_setWeakIvarLayout(_ cls: AnyClass!, _ layout: ConstUnsafePointer<UInt8>) ``` | OS X 10.10 |
| To | ``` func class_setWeakIvarLayout(_ cls: AnyClass!, _ layout: UnsafePointer<UInt8>) ``` | OS X 10.5 |

Modified imp_getBlock(IMP) -> AnyObject!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified imp_implementationWithBlock(AnyObject!) -> IMP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified imp_removeBlock(IMP) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified ivar_getName(Ivar) -> UnsafePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ivar_getName(_ v: Ivar) -> ConstUnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` func ivar_getName(_ v: Ivar) -> UnsafePointer<Int8> ``` | OS X 10.5 |

Modified ivar_getOffset(Ivar) -> Int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified ivar_getTypeEncoding(Ivar) -> UnsafePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ivar_getTypeEncoding(_ v: Ivar) -> ConstUnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` func ivar_getTypeEncoding(_ v: Ivar) -> UnsafePointer<Int8> ``` | OS X 10.5 |

Modified marg_list

|  | Declaration |
| --- | --- |
| From | ``` typealias marg_list = UnsafePointer<()> ``` |
| To | ``` typealias marg_list = UnsafeMutablePointer<Void> ``` |

Modified method_copyArgumentType(Method, UInt32) -> UnsafeMutablePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func method_copyArgumentType(_ m: Method, _ index: UInt32) -> UnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` func method_copyArgumentType(_ m: Method, _ index: UInt32) -> UnsafeMutablePointer<Int8> ``` | OS X 10.5 |

Modified method_copyReturnType(Method) -> UnsafeMutablePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func method_copyReturnType(_ m: Method) -> UnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` func method_copyReturnType(_ m: Method) -> UnsafeMutablePointer<Int8> ``` | OS X 10.5 |

Modified method_exchangeImplementations(Method, Method)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified method_getArgumentType(Method, UInt32, UnsafeMutablePointer<Int8>, Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func method_getArgumentType(_ m: Method, _ index: UInt32, _ dst: UnsafePointer<Int8>, _ dst_len: UInt) ``` | OS X 10.10 |
| To | ``` func method_getArgumentType(_ m: Method, _ index: UInt32, _ dst: UnsafeMutablePointer<Int8>, _ dst_len: Int) ``` | OS X 10.5 |

Modified method_getDescription(Method) -> UnsafeMutablePointer<objc_method_description>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func method_getDescription(_ m: Method) -> UnsafePointer<objc_method_description> ``` | OS X 10.10 |
| To | ``` func method_getDescription(_ m: Method) -> UnsafeMutablePointer<objc_method_description> ``` | OS X 10.5 |

Modified method_getImplementation(Method) -> IMP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified method_getName(Method) -> Selector

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified method_getNumberOfArguments(Method) -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified method_getReturnType(Method, UnsafeMutablePointer<Int8>, Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func method_getReturnType(_ m: Method, _ dst: UnsafePointer<Int8>, _ dst_len: UInt) ``` | OS X 10.10 |
| To | ``` func method_getReturnType(_ m: Method, _ dst: UnsafeMutablePointer<Int8>, _ dst_len: Int) ``` | OS X 10.5 |

Modified method_getTypeEncoding(Method) -> UnsafePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func method_getTypeEncoding(_ m: Method) -> ConstUnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` func method_getTypeEncoding(_ m: Method) -> UnsafePointer<Int8> ``` | OS X 10.5 |

Modified method_setImplementation(Method, IMP) -> IMP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified objc_addExceptionHandler(objc_exception_handler, UnsafeMutablePointer<Void>) -> UInt

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_addExceptionHandler(_ fn: objc_exception_handler, _ context: UnsafePointer<()>) -> UInt ``` | OS X 10.10 |
| To | ``` func objc_addExceptionHandler(_ fn: objc_exception_handler, _ context: UnsafeMutablePointer<Void>) -> UInt ``` | OS X 10.5 |

Modified objc_allocateClassPair(AnyClass!, UnsafePointer<Int8>, Int) -> AnyClass!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_allocateClassPair(_ superclass: AnyClass!, _ name: ConstUnsafePointer<Int8>, _ extraBytes: UInt) -> AnyClass! ``` | OS X 10.10 |
| To | ``` func objc_allocateClassPair(_ superclass: AnyClass!, _ name: UnsafePointer<Int8>, _ extraBytes: Int) -> AnyClass! ``` | OS X 10.5 |

Modified objc_allocateProtocol(UnsafePointer<Int8>) -> Protocol!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_allocateProtocol(_ name: ConstUnsafePointer<Int8>) -> Protocol! ``` | OS X 10.10 |
| To | ``` func objc_allocateProtocol(_ name: UnsafePointer<Int8>) -> Protocol! ``` | OS X 10.7 |

Modified objc_assertRegisteredThreadWithCollector()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified objc_assign_global(AnyObject!, AutoreleasingUnsafeMutablePointer<AnyObject?>) -> AnyObject!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_assign_global(_ val: AnyObject!, _ dest: AutoreleasingUnsafePointer<AnyObject?>) -> AnyObject! ``` | OS X 10.10 |
| To | ``` func objc_assign_global(_ val: AnyObject!, _ dest: AutoreleasingUnsafeMutablePointer<AnyObject?>) -> AnyObject! ``` | OS X 10.4 |

Modified objc_assign_ivar(AnyObject!, AnyObject!, Int) -> AnyObject!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified objc_assign_strongCast(AnyObject!, AutoreleasingUnsafeMutablePointer<AnyObject?>) -> AnyObject!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_assign_strongCast(_ val: AnyObject!, _ dest: AutoreleasingUnsafePointer<AnyObject?>) -> AnyObject! ``` | OS X 10.10 |
| To | ``` func objc_assign_strongCast(_ val: AnyObject!, _ dest: AutoreleasingUnsafeMutablePointer<AnyObject?>) -> AnyObject! ``` | OS X 10.4 |

Modified objc_assign_threadlocal(AnyObject!, AutoreleasingUnsafeMutablePointer<AnyObject?>) -> AnyObject!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_assign_threadlocal(_ val: AnyObject!, _ dest: AutoreleasingUnsafePointer<AnyObject?>) -> AnyObject! ``` | OS X 10.10 |
| To | ``` func objc_assign_threadlocal(_ val: AnyObject!, _ dest: AutoreleasingUnsafeMutablePointer<AnyObject?>) -> AnyObject! ``` | OS X 10.7 |

Modified objc_assign_weak(AnyObject!, AutoreleasingUnsafeMutablePointer<AnyObject?>) -> AnyObject!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_assign_weak(_ value: AnyObject!, _ location: AutoreleasingUnsafePointer<AnyObject?>) -> AnyObject! ``` | OS X 10.10 |
| To | ``` func objc_assign_weak(_ value: AnyObject!, _ location: AutoreleasingUnsafeMutablePointer<AnyObject?>) -> AnyObject! ``` | OS X 10.5 |

Modified objc_begin_catch(UnsafeMutablePointer<Void>) -> AnyObject!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_begin_catch(_ exc_buf: UnsafePointer<()>) -> AnyObject! ``` | OS X 10.10 |
| To | ``` func objc_begin_catch(_ exc_buf: UnsafeMutablePointer<Void>) -> AnyObject! ``` | OS X 10.5 |

Modified objc_clear_stack(UInt)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified objc_collect(UInt)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified objc_collectableZone() -> UnsafeMutablePointer<malloc_zone_t>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_collectableZone() -> UnsafePointer<malloc_zone_t> ``` | OS X 10.10 |
| To | ``` func objc_collectableZone() -> UnsafeMutablePointer<malloc_zone_t> ``` | OS X 10.7 |

Modified objc_collectingEnabled() -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified objc_copyClassList(UnsafeMutablePointer<UInt32>) -> AutoreleasingUnsafeMutablePointer<AnyClass?>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_copyClassList(_ outCount: UnsafePointer<UInt32>) -> AutoreleasingUnsafePointer<AnyClass?> ``` | OS X 10.10 |
| To | ``` func objc_copyClassList(_ outCount: UnsafeMutablePointer<UInt32>) -> AutoreleasingUnsafeMutablePointer<AnyClass?> ``` | OS X 10.7 |

Modified objc_copyClassNamesForImage(UnsafePointer<Int8>, UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<UnsafePointer<Int8>>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_copyClassNamesForImage(_ image: ConstUnsafePointer<Int8>, _ outCount: UnsafePointer<UInt32>) -> UnsafePointer<ConstUnsafePointer<Int8>> ``` | OS X 10.10 |
| To | ``` func objc_copyClassNamesForImage(_ image: UnsafePointer<Int8>, _ outCount: UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<UnsafePointer<Int8>> ``` | OS X 10.5 |

Modified objc_copyImageNames(UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<UnsafePointer<Int8>>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_copyImageNames(_ outCount: UnsafePointer<UInt32>) -> UnsafePointer<ConstUnsafePointer<Int8>> ``` | OS X 10.10 |
| To | ``` func objc_copyImageNames(_ outCount: UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<UnsafePointer<Int8>> ``` | OS X 10.5 |

Modified objc_copyProtocolList(UnsafeMutablePointer<UInt32>) -> AutoreleasingUnsafeMutablePointer<Protocol?>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_copyProtocolList(_ outCount: UnsafePointer<UInt32>) -> AutoreleasingUnsafePointer<Protocol?> ``` | OS X 10.10 |
| To | ``` func objc_copyProtocolList(_ outCount: UnsafeMutablePointer<UInt32>) -> AutoreleasingUnsafeMutablePointer<Protocol?> ``` | OS X 10.5 |

Modified objc_disposeClassPair(AnyClass!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified objc_duplicateClass(AnyClass!, UnsafePointer<Int8>, Int) -> AnyClass!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_duplicateClass(_ original: AnyClass!, _ name: ConstUnsafePointer<Int8>, _ extraBytes: UInt) -> AnyClass! ``` | OS X 10.10 |
| To | ``` func objc_duplicateClass(_ original: AnyClass!, _ name: UnsafePointer<Int8>, _ extraBytes: Int) -> AnyClass! ``` | OS X 10.5 |

Modified objc_end_catch()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified objc_enumerationMutation(AnyObject!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified objc_exception_handler

|  | Declaration |
| --- | --- |
| From | ``` typealias objc_exception_handler = CFunctionPointer<((AnyObject!, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias objc_exception_handler = CFunctionPointer<((AnyObject!, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified objc_exception_rethrow()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified objc_exception_throw(AnyObject!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified objc_getAssociatedObject(AnyObject!, UnsafePointer<Void>) -> AnyObject!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_getAssociatedObject(_ object: AnyObject!, _ key: ConstUnsafePointer<()>) -> AnyObject! ``` | OS X 10.10 |
| To | ``` func objc_getAssociatedObject(_ object: AnyObject!, _ key: UnsafePointer<Void>) -> AnyObject! ``` | OS X 10.6 |

Modified objc_getClass(UnsafePointer<Int8>) -> AnyObject!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_getClass(_ name: ConstUnsafePointer<Int8>) -> AnyObject! ``` | OS X 10.10 |
| To | ``` func objc_getClass(_ name: UnsafePointer<Int8>) -> AnyObject! ``` | OS X 10.0 |

Modified objc_getClassList(AutoreleasingUnsafeMutablePointer<AnyClass?>, Int32) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_getClassList(_ buffer: AutoreleasingUnsafePointer<AnyClass?>, _ bufferCount: Int32) -> Int32 ``` | OS X 10.10 |
| To | ``` func objc_getClassList(_ buffer: AutoreleasingUnsafeMutablePointer<AnyClass?>, _ bufferCount: Int32) -> Int32 ``` | OS X 10.0 |

Modified objc_getMetaClass(UnsafePointer<Int8>) -> AnyObject!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_getMetaClass(_ name: ConstUnsafePointer<Int8>) -> AnyObject! ``` | OS X 10.10 |
| To | ``` func objc_getMetaClass(_ name: UnsafePointer<Int8>) -> AnyObject! ``` | OS X 10.0 |

Modified objc_getProtocol(UnsafePointer<Int8>) -> Protocol!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_getProtocol(_ name: ConstUnsafePointer<Int8>) -> Protocol! ``` | OS X 10.10 |
| To | ``` func objc_getProtocol(_ name: UnsafePointer<Int8>) -> Protocol! ``` | OS X 10.5 |

Modified objc_getRequiredClass(UnsafePointer<Int8>) -> AnyClass!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_getRequiredClass(_ name: ConstUnsafePointer<Int8>) -> AnyClass! ``` | OS X 10.10 |
| To | ``` func objc_getRequiredClass(_ name: UnsafePointer<Int8>) -> AnyClass! ``` | OS X 10.0 |

Modified objc_is_finalized(UnsafeMutablePointer<Void>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_is_finalized(_ ptr: UnsafePointer<()>) -> Bool ``` | OS X 10.10 |
| To | ``` func objc_is_finalized(_ ptr: UnsafeMutablePointer<Void>) -> Bool ``` | OS X 10.4 |

Modified objc_loadWeak(AutoreleasingUnsafeMutablePointer<AnyObject?>) -> AnyObject!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_loadWeak(_ location: AutoreleasingUnsafePointer<AnyObject?>) -> AnyObject! ``` | OS X 10.10 |
| To | ``` func objc_loadWeak(_ location: AutoreleasingUnsafeMutablePointer<AnyObject?>) -> AnyObject! ``` | OS X 10.7 |

Modified objc_lookUpClass(UnsafePointer<Int8>) -> AnyClass!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_lookUpClass(_ name: ConstUnsafePointer<Int8>) -> AnyClass! ``` | OS X 10.10 |
| To | ``` func objc_lookUpClass(_ name: UnsafePointer<Int8>) -> AnyClass! ``` | OS X 10.0 |

Modified objc_memmove_collectable(UnsafeMutablePointer<Void>, UnsafePointer<Void>, Int) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_memmove_collectable(_ dst: UnsafePointer<()>, _ src: ConstUnsafePointer<()>, _ size: UInt) -> UnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func objc_memmove_collectable(_ dst: UnsafeMutablePointer<Void>, _ src: UnsafePointer<Void>, _ size: Int) -> UnsafeMutablePointer<Void> ``` | OS X 10.4 |

Modified objc_objectptr_t

|  | Declaration |
| --- | --- |
| From | ``` typealias objc_objectptr_t = ConstUnsafePointer<()> ``` |
| To | ``` typealias objc_objectptr_t = UnsafePointer<Void> ``` |

Modified objc_read_weak(AutoreleasingUnsafeMutablePointer<AnyObject?>) -> AnyObject!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_read_weak(_ location: AutoreleasingUnsafePointer<AnyObject?>) -> AnyObject! ``` | OS X 10.10 |
| To | ``` func objc_read_weak(_ location: AutoreleasingUnsafeMutablePointer<AnyObject?>) -> AnyObject! ``` | OS X 10.5 |

Modified objc_registerClassPair(AnyClass!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified objc_registerProtocol(Protocol!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified objc_registerThreadWithCollector()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified objc_removeAssociatedObjects(AnyObject!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified objc_removeExceptionHandler(UInt)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified objc_setAssociatedObject(AnyObject!, UnsafePointer<Void>, AnyObject!, objc_AssociationPolicy)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_setAssociatedObject(_ object: AnyObject!, _ key: ConstUnsafePointer<()>, _ value: AnyObject!, _ policy: objc_AssociationPolicy) ``` | OS X 10.10 |
| To | ``` func objc_setAssociatedObject(_ object: AnyObject!, _ key: UnsafePointer<Void>, _ value: AnyObject!, _ policy: objc_AssociationPolicy) ``` | OS X 10.6 |

Modified objc_setCollectionRatio(Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_setCollectionRatio(_ ratio: UInt) ``` | OS X 10.10 |
| To | ``` func objc_setCollectionRatio(_ ratio: Int) ``` | OS X 10.5 |

Modified objc_setCollectionThreshold(Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_setCollectionThreshold(_ threshold: UInt) ``` | OS X 10.10 |
| To | ``` func objc_setCollectionThreshold(_ threshold: Int) ``` | OS X 10.5 |

Modified objc_setEnumerationMutationHandler(CFunctionPointer<((AnyObject!) -> Void)>)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified objc_setExceptionMatcher(objc_exception_matcher) -> objc_exception_matcher

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified objc_setExceptionPreprocessor(objc_exception_preprocessor) -> objc_exception_preprocessor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified objc_setForwardHandler(UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_setForwardHandler(_ fwd: UnsafePointer<()>, _ fwd_stret: UnsafePointer<()>) ``` | OS X 10.10 |
| To | ``` func objc_setForwardHandler(_ fwd: UnsafeMutablePointer<Void>, _ fwd_stret: UnsafeMutablePointer<Void>) ``` | OS X 10.5 |

Modified objc_setUncaughtExceptionHandler(objc_uncaught_exception_handler) -> objc_uncaught_exception_handler

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified objc_storeWeak(AutoreleasingUnsafeMutablePointer<AnyObject?>, AnyObject!) -> AnyObject!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_storeWeak(_ location: AutoreleasingUnsafePointer<AnyObject?>, _ obj: AnyObject!) -> AnyObject! ``` | OS X 10.10 |
| To | ``` func objc_storeWeak(_ location: AutoreleasingUnsafeMutablePointer<AnyObject?>, _ obj: AnyObject!) -> AnyObject! ``` | OS X 10.7 |

Modified objc_sync_enter(AnyObject!) -> Int32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified objc_sync_exit(AnyObject!) -> Int32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified objc_terminate()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified objc_unregisterThreadWithCollector()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified object_getClass(AnyObject!) -> AnyClass!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified object_getClassName(AnyObject!) -> UnsafePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func object_getClassName(_ obj: AnyObject!) -> ConstUnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` func object_getClassName(_ obj: AnyObject!) -> UnsafePointer<Int8> ``` | OS X 10.0 |

Modified object_getIvar(AnyObject!, Ivar) -> AnyObject!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified object_setClass(AnyObject!, AnyClass!) -> AnyClass!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified object_setIvar(AnyObject!, Ivar, AnyObject!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified property_copyAttributeList(objc_property_t, UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<objc_property_attribute_t>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func property_copyAttributeList(_ property: objc_property_t, _ outCount: UnsafePointer<UInt32>) -> UnsafePointer<objc_property_attribute_t> ``` | OS X 10.10 |
| To | ``` func property_copyAttributeList(_ property: objc_property_t, _ outCount: UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<objc_property_attribute_t> ``` | OS X 10.7 |

Modified property_copyAttributeValue(objc_property_t, UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func property_copyAttributeValue(_ property: objc_property_t, _ attributeName: ConstUnsafePointer<Int8>) -> UnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` func property_copyAttributeValue(_ property: objc_property_t, _ attributeName: UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` | OS X 10.7 |

Modified property_getAttributes(objc_property_t) -> UnsafePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func property_getAttributes(_ property: objc_property_t) -> ConstUnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` func property_getAttributes(_ property: objc_property_t) -> UnsafePointer<Int8> ``` | OS X 10.5 |

Modified property_getName(objc_property_t) -> UnsafePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func property_getName(_ property: objc_property_t) -> ConstUnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` func property_getName(_ property: objc_property_t) -> UnsafePointer<Int8> ``` | OS X 10.5 |

Modified protocol_addMethodDescription(Protocol!, Selector, UnsafePointer<Int8>, Bool, Bool)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func protocol_addMethodDescription(_ proto: Protocol!, _ name: Selector, _ types: ConstUnsafePointer<Int8>, _ isRequiredMethod: Bool, _ isInstanceMethod: Bool) ``` | OS X 10.10 |
| To | ``` func protocol_addMethodDescription(_ proto: Protocol!, _ name: Selector, _ types: UnsafePointer<Int8>, _ isRequiredMethod: Bool, _ isInstanceMethod: Bool) ``` | OS X 10.7 |

Modified protocol_addProperty(Protocol!, UnsafePointer<Int8>, UnsafePointer<objc_property_attribute_t>, UInt32, Bool, Bool)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func protocol_addProperty(_ proto: Protocol!, _ name: ConstUnsafePointer<Int8>, _ attributes: ConstUnsafePointer<objc_property_attribute_t>, _ attributeCount: UInt32, _ isRequiredProperty: Bool, _ isInstanceProperty: Bool) ``` | OS X 10.10 |
| To | ``` func protocol_addProperty(_ proto: Protocol!, _ name: UnsafePointer<Int8>, _ attributes: UnsafePointer<objc_property_attribute_t>, _ attributeCount: UInt32, _ isRequiredProperty: Bool, _ isInstanceProperty: Bool) ``` | OS X 10.7 |

Modified protocol_addProtocol(Protocol!, Protocol!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified protocol_conformsToProtocol(Protocol!, Protocol!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified protocol_copyMethodDescriptionList(Protocol!, Bool, Bool, UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<objc_method_description>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func protocol_copyMethodDescriptionList(_ p: Protocol!, _ isRequiredMethod: Bool, _ isInstanceMethod: Bool, _ outCount: UnsafePointer<UInt32>) -> UnsafePointer<objc_method_description> ``` | OS X 10.10 |
| To | ``` func protocol_copyMethodDescriptionList(_ p: Protocol!, _ isRequiredMethod: Bool, _ isInstanceMethod: Bool, _ outCount: UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<objc_method_description> ``` | OS X 10.5 |

Modified protocol_copyPropertyList(Protocol!, UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<objc_property_t>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func protocol_copyPropertyList(_ proto: Protocol!, _ outCount: UnsafePointer<UInt32>) -> UnsafePointer<objc_property_t> ``` | OS X 10.10 |
| To | ``` func protocol_copyPropertyList(_ proto: Protocol!, _ outCount: UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<objc_property_t> ``` | OS X 10.5 |

Modified protocol_copyProtocolList(Protocol!, UnsafeMutablePointer<UInt32>) -> AutoreleasingUnsafeMutablePointer<Protocol?>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func protocol_copyProtocolList(_ proto: Protocol!, _ outCount: UnsafePointer<UInt32>) -> AutoreleasingUnsafePointer<Protocol?> ``` | OS X 10.10 |
| To | ``` func protocol_copyProtocolList(_ proto: Protocol!, _ outCount: UnsafeMutablePointer<UInt32>) -> AutoreleasingUnsafeMutablePointer<Protocol?> ``` | OS X 10.5 |

Modified protocol_getMethodDescription(Protocol!, Selector, Bool, Bool) -> objc_method_description

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified protocol_getName(Protocol!) -> UnsafePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func protocol_getName(_ p: Protocol!) -> ConstUnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` func protocol_getName(_ p: Protocol!) -> UnsafePointer<Int8> ``` | OS X 10.5 |

Modified protocol_getProperty(Protocol!, UnsafePointer<Int8>, Bool, Bool) -> objc_property_t

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func protocol_getProperty(_ proto: Protocol!, _ name: ConstUnsafePointer<Int8>, _ isRequiredProperty: Bool, _ isInstanceProperty: Bool) -> objc_property_t ``` | OS X 10.10 |
| To | ``` func protocol_getProperty(_ proto: Protocol!, _ name: UnsafePointer<Int8>, _ isRequiredProperty: Bool, _ isInstanceProperty: Bool) -> objc_property_t ``` | OS X 10.5 |

Modified protocol_isEqual(Protocol!, Protocol!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified sel_getName(Selector) -> UnsafePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func sel_getName(_ sel: Selector) -> ConstUnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` func sel_getName(_ sel: Selector) -> UnsafePointer<Int8> ``` | OS X 10.0 |

Modified sel_getUid(UnsafePointer<Int8>) -> Selector

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func sel_getUid(_ str: ConstUnsafePointer<Int8>) -> Selector ``` | OS X 10.10 |
| To | ``` func sel_getUid(_ str: UnsafePointer<Int8>) -> Selector ``` | OS X 10.0 |

Modified sel_isEqual(Selector, Selector) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified sel_isMapped(Selector) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified sel_registerName(UnsafePointer<Int8>) -> Selector

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func sel_registerName(_ str: ConstUnsafePointer<Int8>) -> Selector ``` | OS X 10.10 |
| To | ``` func sel_registerName(_ str: UnsafePointer<Int8>) -> Selector ``` | OS X 10.0 |

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
