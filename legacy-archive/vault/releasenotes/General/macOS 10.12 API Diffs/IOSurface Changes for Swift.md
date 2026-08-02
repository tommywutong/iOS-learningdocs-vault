---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/IOSurface.html
archived_at: '2026-07-18T02:51:26.706772Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# IOSurface Changes for Swift

### IOSurface

Added [IOSurface](https://developer.apple.com/documentation/iosurface/iosurface)Added [IOSurface.allAttachments() -> [AnyHashable : Any]?](https://developer.apple.com/documentation/iosurface/iosurface/2092487-allattachments)Added [IOSurface.allocationSize](https://developer.apple.com/documentation/iosurface/iosurface/2092534-allocationsize)Added [IOSurface.allowsPixelSizeCasting](https://developer.apple.com/documentation/iosurface/iosurface/2092536-allowspixelsizecasting)Added [IOSurface.attachment(forKey: String) -> Any?](https://developer.apple.com/documentation/iosurface/iosurface/2092535-attachmentforkey)Added [IOSurface.baseAddress](https://developer.apple.com/documentation/iosurface/iosurface/2092525-baseaddress)Added [IOSurface.baseAddressOfPlane(at: Int) -> UnsafeMutableRawPointer](https://developer.apple.com/documentation/iosurface/iosurface/2092494-baseaddressofplane)Added [IOSurface.bytesPerElement](https://developer.apple.com/documentation/iosurface/iosurface/2092503-bytesperelement)Added [IOSurface.bytesPerElementOfPlane(at: Int) -> Int](https://developer.apple.com/documentation/iosurface/iosurface/2092511-bytesperelementofplane)Added [IOSurface.bytesPerRow](https://developer.apple.com/documentation/iosurface/iosurface/2092502-bytesperrow)Added [IOSurface.bytesPerRowOfPlane(at: Int) -> Int](https://developer.apple.com/documentation/iosurface/iosurface/2092497-bytesperrowofplaneatindex)Added [IOSurface.decrementUseCount()](https://developer.apple.com/documentation/iosurface/iosurface/2092538-decrementusecount)Added [IOSurface.elementHeight](https://developer.apple.com/documentation/iosurface/iosurface/2092539-elementheight)Added [IOSurface.elementHeightOfPlane(at: Int) -> Int](https://developer.apple.com/documentation/iosurface/iosurface/2092515-elementheightofplaneatindex)Added [IOSurface.elementWidth](https://developer.apple.com/documentation/iosurface/iosurface/2092514-elementwidth)Added [IOSurface.elementWidthOfPlane(at: Int) -> Int](https://developer.apple.com/documentation/iosurface/iosurface/2092498-elementwidthofplane)Added [IOSurface.height](https://developer.apple.com/documentation/iosurface/iosurface/2092501-height)Added [IOSurface.heightOfPlane(at: Int) -> Int](https://developer.apple.com/documentation/iosurface/iosurface/2092493-heightofplaneatindex)Added [IOSurface.incrementUseCount()](https://developer.apple.com/documentation/iosurface/iosurface/2092506-incrementusecount)Added [IOSurface.init(properties: [IOSurfacePropertyKey : Any])](https://developer.apple.com/documentation/iosurface/iosurface/2092523-init)Added [IOSurface.isInUse](https://developer.apple.com/documentation/iosurface/iosurface/2092504-isinuse)Added [IOSurface.localUseCount](https://developer.apple.com/documentation/iosurface/iosurface/2092529-localusecount)Added [IOSurface.lock(options: IOSurfaceLockOptions, seed: UnsafeMutablePointer<UInt32>?) -> IOReturn](https://developer.apple.com/documentation/iosurface/iosurface/2092522-lock)Added [IOSurface.pixelFormat](https://developer.apple.com/documentation/iosurface/iosurface/2092537-pixelformat)Added [IOSurface.planeCount](https://developer.apple.com/documentation/iosurface/iosurface/2092508-planecount)Added [IOSurface.removeAllAttachments()](https://developer.apple.com/documentation/iosurface/iosurface/2092490-removeallattachments)Added [IOSurface.removeAttachment(forKey: String)](https://developer.apple.com/documentation/iosurface/iosurface/2092541-removeattachment)Added [IOSurface.seed](https://developer.apple.com/documentation/iosurface/iosurface/2092533-seed)Added [IOSurface.setAllAttachments(_: [AnyHashable : Any])](https://developer.apple.com/documentation/iosurface/iosurface/2092532-setallattachments)Added [IOSurface.setAttachment(_: Any, forKey: String)](https://developer.apple.com/documentation/iosurface/iosurface/2092540-setattachment)Added [IOSurface.unlock(options: IOSurfaceLockOptions, seed: UnsafeMutablePointer<UInt32>?) -> IOReturn](https://developer.apple.com/documentation/iosurface/iosurface/2092530-unlockwithoptions)Added [IOSurface.width](https://developer.apple.com/documentation/iosurface/iosurface/2092516-width)Added [IOSurface.widthOfPlane(at: Int) -> Int](https://developer.apple.com/documentation/iosurface/iosurface/2092520-widthofplane)Added [IOSurfacePropertyKey [struct]](https://developer.apple.com/documentation/iosurface/iosurfacepropertykey)Added [IOSurfacePropertyKey.allocSizeKey](https://developer.apple.com/documentation/iosurface/iosurfacepropertykey/2092518-allocsizekey)Added [IOSurfacePropertyKey.bytesPerElement](https://developer.apple.com/documentation/iosurface/iosurfacepropertykeybytesperelement)Added [IOSurfacePropertyKey.bytesPerRow](https://developer.apple.com/documentation/iosurface/iosurfacepropertykeybytesperrow)Added [IOSurfacePropertyKey.cacheMode](https://developer.apple.com/documentation/iosurface/iosurfacepropertykey/2092528-cachemode)Added [IOSurfacePropertyKey.elementHeight](https://developer.apple.com/documentation/iosurface/iosurfacepropertykeyelementheight)Added [IOSurfacePropertyKey.elementWidth](https://developer.apple.com/documentation/iosurface/iosurfacepropertykeyelementwidth)Added [IOSurfacePropertyKey.height](https://developer.apple.com/documentation/iosurface/iosurfacepropertykey/2092542-height)Added [IOSurfacePropertyKey.init(rawValue: String)](https://developer.apple.com/documentation/iosurface/iosurfacepropertykey/2097152-init)Added [IOSurfacePropertyKey.offset](https://developer.apple.com/documentation/iosurface/iosurfacepropertykeyoffset)Added [IOSurfacePropertyKey.pixelFormat](https://developer.apple.com/documentation/iosurface/iosurfacepropertykey/2092521-pixelformat)Added [IOSurfacePropertyKey.pixelSizeCastingAllowed](https://developer.apple.com/documentation/iosurface/iosurfacepropertykey/2092527-pixelsizecastingallowed)Added [IOSurfacePropertyKey.planeBase](https://developer.apple.com/documentation/iosurface/iosurfacepropertykey/2092488-planebase)Added [IOSurfacePropertyKey.planeBytesPerElement](https://developer.apple.com/documentation/iosurface/iosurfacepropertykeyplanebytesperelement)Added [IOSurfacePropertyKey.planeBytesPerRow](https://developer.apple.com/documentation/iosurface/iosurfacepropertykeyplanebytesperrow)Added [IOSurfacePropertyKey.planeElementHeight](https://developer.apple.com/documentation/iosurface/iosurfacepropertykeyplaneelementheight)Added [IOSurfacePropertyKey.planeElementWidth](https://developer.apple.com/documentation/iosurface/iosurfacepropertykey/2092517-planeelementwidth)Added [IOSurfacePropertyKey.planeHeight](https://developer.apple.com/documentation/iosurface/iosurfacepropertykey/2092500-planeheight)Added [IOSurfacePropertyKey.planeInfo](https://developer.apple.com/documentation/iosurface/iosurfacepropertykey/2092505-planeinfo)Added [IOSurfacePropertyKey.planeOffset](https://developer.apple.com/documentation/iosurface/iosurfacepropertykeyplaneoffset)Added [IOSurfacePropertyKey.planeSize](https://developer.apple.com/documentation/iosurface/iosurfacepropertykeyplanesize)Added [IOSurfacePropertyKey.planeWidth](https://developer.apple.com/documentation/iosurface/iosurfacepropertykey/2092513-planewidth)Added [IOSurfacePropertyKey.width](https://developer.apple.com/documentation/iosurface/iosurfacepropertykey/2092509-width)Added [IOSurfaceAllowsPixelSizeCasting(_: IOSurfaceRef) -> Bool](https://developer.apple.com/documentation/iosurface/1642028-iosurfaceallowspixelsizecasting)Added [kIOSurfacePixelSizeCastingAllowed](https://developer.apple.com/documentation/iosurface/kiosurfacepixelsizecastingallowed)Modified [IOSurfaceLockOptions [struct]](https://developer.apple.com/documentation/iosurface/iosurfacelockoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct IOSurfaceLockOptions : OptionSetType {     init(rawValue rawValue: UInt32)     static var ReadOnly: IOSurfaceLockOptions { get }     static var AvoidSync: IOSurfaceLockOptions { get } } ``` | OptionSetType |
| To | ``` struct IOSurfaceLockOptions : OptionSet {     init(rawValue rawValue: UInt32)     static var readOnly: IOSurfaceLockOptions { get }     static var avoidSync: IOSurfaceLockOptions { get }     func intersect(_ other: IOSurfaceLockOptions) -> IOSurfaceLockOptions     func exclusiveOr(_ other: IOSurfaceLockOptions) -> IOSurfaceLockOptions     mutating func unionInPlace(_ other: IOSurfaceLockOptions)     mutating func intersectInPlace(_ other: IOSurfaceLockOptions)     mutating func exclusiveOrInPlace(_ other: IOSurfaceLockOptions)     func isSubsetOf(_ other: IOSurfaceLockOptions) -> Bool     func isDisjointWith(_ other: IOSurfaceLockOptions) -> Bool     func isSupersetOf(_ other: IOSurfaceLockOptions) -> Bool     mutating func subtractInPlace(_ other: IOSurfaceLockOptions)     func isStrictSupersetOf(_ other: IOSurfaceLockOptions) -> Bool     func isStrictSubsetOf(_ other: IOSurfaceLockOptions) -> Bool } extension IOSurfaceLockOptions {     func union(_ other: IOSurfaceLockOptions) -> IOSurfaceLockOptions     func intersection(_ other: IOSurfaceLockOptions) -> IOSurfaceLockOptions     func symmetricDifference(_ other: IOSurfaceLockOptions) -> IOSurfaceLockOptions } extension IOSurfaceLockOptions {     func contains(_ member: IOSurfaceLockOptions) -> Bool     mutating func insert(_ newMember: IOSurfaceLockOptions) -> (inserted: Bool, memberAfterInsert: IOSurfaceLockOptions)     mutating func remove(_ member: IOSurfaceLockOptions) -> IOSurfaceLockOptions?     mutating func update(with newMember: IOSurfaceLockOptions) -> IOSurfaceLockOptions? } extension IOSurfaceLockOptions {     convenience init()     mutating func formUnion(_ other: IOSurfaceLockOptions)     mutating func formIntersection(_ other: IOSurfaceLockOptions)     mutating func formSymmetricDifference(_ other: IOSurfaceLockOptions) } extension IOSurfaceLockOptions {     convenience init<S : Sequence where S.Iterator.Element == IOSurfaceLockOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: IOSurfaceLockOptions...)     mutating func subtract(_ other: IOSurfaceLockOptions)     func isSubset(of other: IOSurfaceLockOptions) -> Bool     func isSuperset(of other: IOSurfaceLockOptions) -> Bool     func isDisjoint(with other: IOSurfaceLockOptions) -> Bool     func subtracting(_ other: IOSurfaceLockOptions) -> IOSurfaceLockOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: IOSurfaceLockOptions) -> Bool     func isStrictSubset(of other: IOSurfaceLockOptions) -> Bool } ``` | OptionSet |

Modified [IOSurfaceLockOptions.avoidSync](https://developer.apple.com/documentation/iosurface/iosurfacelockoptions/kiosurfacelockavoidsync)

|  | Declaration |
| --- | --- |
| From | ``` static var AvoidSync: IOSurfaceLockOptions { get } ``` |
| To | ``` static var avoidSync: IOSurfaceLockOptions { get } ``` |

Modified [IOSurfaceLockOptions.readOnly](https://developer.apple.com/documentation/iosurface/iosurfacelockoptions/kiosurfacelockreadonly)

|  | Declaration |
| --- | --- |
| From | ``` static var ReadOnly: IOSurfaceLockOptions { get } ``` |
| To | ``` static var readOnly: IOSurfaceLockOptions { get } ``` |

Modified [IOSurfaceRef](https://developer.apple.com/documentation/iosurface/iosurfaceref)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` class IOSurface { } ``` | IOSurface |
| To | ``` class IOSurfaceRef { } ``` | CoreGraphics |

Modified [IOSurfaceCopyAllValues(_: IOSurfaceRef) -> CFDictionary?](https://developer.apple.com/documentation/iosurface/1419387-iosurfacecopyallvalues)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceCopyAllValues(_ buffer: IOSurface) -> CFDictionary? ``` |
| To | ``` func IOSurfaceCopyAllValues(_ buffer: IOSurfaceRef) -> CFDictionary? ``` |

Modified [IOSurfaceCopyValue(_: IOSurfaceRef, _: CFString) -> CFTypeRef?](https://developer.apple.com/documentation/iosurface/1419365-iosurfacecopyvalue)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceCopyValue(_ buffer: IOSurface, _ key: CFString) -> AnyObject? ``` |
| To | ``` func IOSurfaceCopyValue(_ buffer: IOSurfaceRef, _ key: CFString) -> CFTypeRef? ``` |

Modified [IOSurfaceCreate(_: CFDictionary) -> IOSurfaceRef?](https://developer.apple.com/documentation/iosurface/1419383-iosurfacecreate)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceCreate(_ properties: CFDictionary) -> IOSurface? ``` |
| To | ``` func IOSurfaceCreate(_ properties: CFDictionary) -> IOSurfaceRef? ``` |

Modified [IOSurfaceCreateMachPort(_: IOSurfaceRef) -> mach_port_t](https://developer.apple.com/documentation/iosurface/1419486-iosurfacecreatemachport)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceCreateMachPort(_ buffer: IOSurface) -> mach_port_t ``` |
| To | ``` func IOSurfaceCreateMachPort(_ buffer: IOSurfaceRef) -> mach_port_t ``` |

Modified [IOSurfaceCreateXPCObject(_: IOSurfaceRef) -> xpc_object_t](https://developer.apple.com/documentation/iosurface/1419429-iosurfacecreatexpcobject)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceCreateXPCObject(_ aSurface: IOSurface) -> xpc_object_t ``` |
| To | ``` func IOSurfaceCreateXPCObject(_ aSurface: IOSurfaceRef) -> xpc_object_t ``` |

Modified [IOSurfaceDecrementUseCount(_: IOSurfaceRef)](https://developer.apple.com/documentation/iosurface/1419377-iosurfacedecrementusecount)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceDecrementUseCount(_ buffer: IOSurface) ``` |
| To | ``` func IOSurfaceDecrementUseCount(_ buffer: IOSurfaceRef) ``` |

Modified [IOSurfaceGetAllocSize(_: IOSurfaceRef) -> Int](https://developer.apple.com/documentation/iosurface/1419391-iosurfacegetallocsize)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetAllocSize(_ buffer: IOSurface) -> Int ``` |
| To | ``` func IOSurfaceGetAllocSize(_ buffer: IOSurfaceRef) -> Int ``` |

Modified [IOSurfaceGetBaseAddress(_: IOSurfaceRef) -> UnsafeMutableRawPointer](https://developer.apple.com/documentation/iosurface/1419490-iosurfacegetbaseaddress)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetBaseAddress(_ buffer: IOSurface) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func IOSurfaceGetBaseAddress(_ buffer: IOSurfaceRef) -> UnsafeMutableRawPointer ``` |

Modified [IOSurfaceGetBaseAddressOfPlane(_: IOSurfaceRef, _: Int) -> UnsafeMutableRawPointer](https://developer.apple.com/documentation/iosurface/1419379-iosurfacegetbaseaddressofplane)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetBaseAddressOfPlane(_ buffer: IOSurface, _ planeIndex: Int) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func IOSurfaceGetBaseAddressOfPlane(_ buffer: IOSurfaceRef, _ planeIndex: Int) -> UnsafeMutableRawPointer ``` |

Modified [IOSurfaceGetBytesPerElement(_: IOSurfaceRef) -> Int](https://developer.apple.com/documentation/iosurface/1419389-iosurfacegetbytesperelement)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetBytesPerElement(_ buffer: IOSurface) -> Int ``` |
| To | ``` func IOSurfaceGetBytesPerElement(_ buffer: IOSurfaceRef) -> Int ``` |

Modified [IOSurfaceGetBytesPerElementOfPlane(_: IOSurfaceRef, _: Int) -> Int](https://developer.apple.com/documentation/iosurface/1419409-iosurfacegetbytesperelementofpla)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetBytesPerElementOfPlane(_ buffer: IOSurface, _ planeIndex: Int) -> Int ``` |
| To | ``` func IOSurfaceGetBytesPerElementOfPlane(_ buffer: IOSurfaceRef, _ planeIndex: Int) -> Int ``` |

Modified [IOSurfaceGetBytesPerRow(_: IOSurfaceRef) -> Int](https://developer.apple.com/documentation/iosurface/1419397-iosurfacegetbytesperrow)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetBytesPerRow(_ buffer: IOSurface) -> Int ``` |
| To | ``` func IOSurfaceGetBytesPerRow(_ buffer: IOSurfaceRef) -> Int ``` |

Modified [IOSurfaceGetBytesPerRowOfPlane(_: IOSurfaceRef, _: Int) -> Int](https://developer.apple.com/documentation/iosurface/1419488-iosurfacegetbytesperrowofplane)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetBytesPerRowOfPlane(_ buffer: IOSurface, _ planeIndex: Int) -> Int ``` |
| To | ``` func IOSurfaceGetBytesPerRowOfPlane(_ buffer: IOSurfaceRef, _ planeIndex: Int) -> Int ``` |

Modified [IOSurfaceGetElementHeight(_: IOSurfaceRef) -> Int](https://developer.apple.com/documentation/iosurface/1419415-iosurfacegetelementheight)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetElementHeight(_ buffer: IOSurface) -> Int ``` |
| To | ``` func IOSurfaceGetElementHeight(_ buffer: IOSurfaceRef) -> Int ``` |

Modified [IOSurfaceGetElementHeightOfPlane(_: IOSurfaceRef, _: Int) -> Int](https://developer.apple.com/documentation/iosurface/1419492-iosurfacegetelementheightofplane)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetElementHeightOfPlane(_ buffer: IOSurface, _ planeIndex: Int) -> Int ``` |
| To | ``` func IOSurfaceGetElementHeightOfPlane(_ buffer: IOSurfaceRef, _ planeIndex: Int) -> Int ``` |

Modified [IOSurfaceGetElementWidth(_: IOSurfaceRef) -> Int](https://developer.apple.com/documentation/iosurface/1419375-iosurfacegetelementwidth)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetElementWidth(_ buffer: IOSurface) -> Int ``` |
| To | ``` func IOSurfaceGetElementWidth(_ buffer: IOSurfaceRef) -> Int ``` |

Modified [IOSurfaceGetElementWidthOfPlane(_: IOSurfaceRef, _: Int) -> Int](https://developer.apple.com/documentation/iosurface/1419457-iosurfacegetelementwidthofplane)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetElementWidthOfPlane(_ buffer: IOSurface, _ planeIndex: Int) -> Int ``` |
| To | ``` func IOSurfaceGetElementWidthOfPlane(_ buffer: IOSurfaceRef, _ planeIndex: Int) -> Int ``` |

Modified [IOSurfaceGetHeight(_: IOSurfaceRef) -> Int](https://developer.apple.com/documentation/iosurface/1419425-iosurfacegetheight)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetHeight(_ buffer: IOSurface) -> Int ``` |
| To | ``` func IOSurfaceGetHeight(_ buffer: IOSurfaceRef) -> Int ``` |

Modified [IOSurfaceGetHeightOfPlane(_: IOSurfaceRef, _: Int) -> Int](https://developer.apple.com/documentation/iosurface/1419433-iosurfacegetheightofplane)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetHeightOfPlane(_ buffer: IOSurface, _ planeIndex: Int) -> Int ``` |
| To | ``` func IOSurfaceGetHeightOfPlane(_ buffer: IOSurfaceRef, _ planeIndex: Int) -> Int ``` |

Modified [IOSurfaceGetID(_: IOSurfaceRef) -> IOSurfaceID](https://developer.apple.com/documentation/iosurface/1419472-iosurfacegetid)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetID(_ buffer: IOSurface) -> IOSurfaceID ``` |
| To | ``` func IOSurfaceGetID(_ buffer: IOSurfaceRef) -> IOSurfaceID ``` |

Modified [IOSurfaceGetPixelFormat(_: IOSurfaceRef) -> OSType](https://developer.apple.com/documentation/iosurface/1419445-iosurfacegetpixelformat)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetPixelFormat(_ buffer: IOSurface) -> OSType ``` |
| To | ``` func IOSurfaceGetPixelFormat(_ buffer: IOSurfaceRef) -> OSType ``` |

Modified [IOSurfaceGetPlaneCount(_: IOSurfaceRef) -> Int](https://developer.apple.com/documentation/iosurface/1419427-iosurfacegetplanecount)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetPlaneCount(_ buffer: IOSurface) -> Int ``` |
| To | ``` func IOSurfaceGetPlaneCount(_ buffer: IOSurfaceRef) -> Int ``` |

Modified [IOSurfaceGetSeed(_: IOSurfaceRef) -> UInt32](https://developer.apple.com/documentation/iosurface/1419431-iosurfacegetseed)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetSeed(_ buffer: IOSurface) -> UInt32 ``` |
| To | ``` func IOSurfaceGetSeed(_ buffer: IOSurfaceRef) -> UInt32 ``` |

Modified [IOSurfaceGetUseCount(_: IOSurfaceRef) -> Int32](https://developer.apple.com/documentation/iosurface/1419478-iosurfacegetusecount)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetUseCount(_ buffer: IOSurface) -> Int32 ``` |
| To | ``` func IOSurfaceGetUseCount(_ buffer: IOSurfaceRef) -> Int32 ``` |

Modified [IOSurfaceGetWidth(_: IOSurfaceRef) -> Int](https://developer.apple.com/documentation/iosurface/1419385-iosurfacegetwidth)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetWidth(_ buffer: IOSurface) -> Int ``` |
| To | ``` func IOSurfaceGetWidth(_ buffer: IOSurfaceRef) -> Int ``` |

Modified [IOSurfaceGetWidthOfPlane(_: IOSurfaceRef, _: Int) -> Int](https://developer.apple.com/documentation/iosurface/1419451-iosurfacegetwidthofplane)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetWidthOfPlane(_ buffer: IOSurface, _ planeIndex: Int) -> Int ``` |
| To | ``` func IOSurfaceGetWidthOfPlane(_ buffer: IOSurfaceRef, _ planeIndex: Int) -> Int ``` |

Modified [IOSurfaceIncrementUseCount(_: IOSurfaceRef)](https://developer.apple.com/documentation/iosurface/1419455-iosurfaceincrementusecount)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceIncrementUseCount(_ buffer: IOSurface) ``` |
| To | ``` func IOSurfaceIncrementUseCount(_ buffer: IOSurfaceRef) ``` |

Modified [IOSurfaceIsInUse(_: IOSurfaceRef) -> Bool](https://developer.apple.com/documentation/iosurface/1419357-iosurfaceisinuse)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceIsInUse(_ buffer: IOSurface) -> Bool ``` |
| To | ``` func IOSurfaceIsInUse(_ buffer: IOSurfaceRef) -> Bool ``` |

Modified [IOSurfaceLock(_: IOSurfaceRef, _: IOSurfaceLockOptions, _: UnsafeMutablePointer<UInt32>?) -> IOReturn](https://developer.apple.com/documentation/iosurface/1419474-iosurfacelock)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceLock(_ buffer: IOSurface, _ options: IOSurfaceLockOptions, _ seed: UnsafeMutablePointer<UInt32>) -> IOReturn ``` |
| To | ``` func IOSurfaceLock(_ buffer: IOSurfaceRef, _ options: IOSurfaceLockOptions, _ seed: UnsafeMutablePointer<UInt32>?) -> IOReturn ``` |

Modified [IOSurfaceLookup(_: IOSurfaceID) -> IOSurfaceRef?](https://developer.apple.com/documentation/iosurface/1419361-iosurfacelookup)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceLookup(_ csid: IOSurfaceID) -> IOSurface? ``` |
| To | ``` func IOSurfaceLookup(_ csid: IOSurfaceID) -> IOSurfaceRef? ``` |

Modified [IOSurfaceLookupFromMachPort(_: mach_port_t) -> IOSurfaceRef?](https://developer.apple.com/documentation/iosurface/1419480-iosurfacelookupfrommachport)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceLookupFromMachPort(_ port: mach_port_t) -> IOSurface? ``` |
| To | ``` func IOSurfaceLookupFromMachPort(_ port: mach_port_t) -> IOSurfaceRef? ``` |

Modified [IOSurfaceLookupFromXPCObject(_: xpc_object_t) -> IOSurfaceRef?](https://developer.apple.com/documentation/iosurface/1419449-iosurfacelookupfromxpcobject)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceLookupFromXPCObject(_ xobj: xpc_object_t) -> IOSurface? ``` |
| To | ``` func IOSurfaceLookupFromXPCObject(_ xobj: xpc_object_t) -> IOSurfaceRef? ``` |

Modified [IOSurfaceRemoveAllValues(_: IOSurfaceRef)](https://developer.apple.com/documentation/iosurface/1419413-iosurfaceremoveallvalues)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceRemoveAllValues(_ buffer: IOSurface) ``` |
| To | ``` func IOSurfaceRemoveAllValues(_ buffer: IOSurfaceRef) ``` |

Modified [IOSurfaceRemoveValue(_: IOSurfaceRef, _: CFString)](https://developer.apple.com/documentation/iosurface/1419401-iosurfaceremovevalue)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceRemoveValue(_ buffer: IOSurface, _ key: CFString) ``` |
| To | ``` func IOSurfaceRemoveValue(_ buffer: IOSurfaceRef, _ key: CFString) ``` |

Modified [IOSurfaceSetValue(_: IOSurfaceRef, _: CFString, _: CFTypeRef)](https://developer.apple.com/documentation/iosurface/1419437-iosurfacesetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceSetValue(_ buffer: IOSurface, _ key: CFString, _ value: AnyObject) ``` |
| To | ``` func IOSurfaceSetValue(_ buffer: IOSurfaceRef, _ key: CFString, _ value: CFTypeRef) ``` |

Modified [IOSurfaceSetValues(_: IOSurfaceRef, _: CFDictionary)](https://developer.apple.com/documentation/iosurface/1419403-iosurfacesetvalues)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceSetValues(_ buffer: IOSurface, _ keysAndValues: CFDictionary) ``` |
| To | ``` func IOSurfaceSetValues(_ buffer: IOSurfaceRef, _ keysAndValues: CFDictionary) ``` |

Modified [IOSurfaceUnlock(_: IOSurfaceRef, _: IOSurfaceLockOptions, _: UnsafeMutablePointer<UInt32>?) -> IOReturn](https://developer.apple.com/documentation/iosurface/1419367-iosurfaceunlock)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceUnlock(_ buffer: IOSurface, _ options: IOSurfaceLockOptions, _ seed: UnsafeMutablePointer<UInt32>) -> IOReturn ``` |
| To | ``` func IOSurfaceUnlock(_ buffer: IOSurfaceRef, _ options: IOSurfaceLockOptions, _ seed: UnsafeMutablePointer<UInt32>?) -> IOReturn ``` |

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
