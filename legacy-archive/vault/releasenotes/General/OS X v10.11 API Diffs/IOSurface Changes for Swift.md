---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/IOSurface.html
archived_at: '2026-07-18T02:53:36.462566Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# IOSurface Changes for Swift

### IOSurface

Removed kIOSurfaceLockAvoidSyncRemoved kIOSurfaceLockReadOnlyAdded [IOSurfaceLockOptions [struct]](https://developer.apple.com/documentation/iosurface/iosurfacelockoptions)Added [IOSurfaceLockOptions.AvoidSync](https://developer.apple.com/documentation/iosurface/iosurfacelockoptions/kiosurfacelockavoidsync)Added IOSurfaceLockOptions.init(rawValue: UInt32)Added [IOSurfaceLockOptions.ReadOnly](https://developer.apple.com/documentation/iosurface/iosurfacelockoptions/kiosurfacelockreadonly)Added [IOSurfaceCopyAllValues(_: IOSurface) -> CFDictionary?](https://developer.apple.com/documentation/iosurface/1419387-iosurfacecopyallvalues)Added [IOSurfaceRemoveAllValues(_: IOSurface)](https://developer.apple.com/documentation/iosurface/1419413-iosurfaceremoveallvalues)Added [IOSurfaceSetValues(_: IOSurface, _: CFDictionary)](https://developer.apple.com/documentation/iosurface/1419403-iosurfacesetvalues)Modified [IOSurfaceAlignProperty(_: CFString, _: Int) -> Int](https://developer.apple.com/documentation/iosurface/1419447-iosurfacealignproperty)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceAlignProperty(_ property: CFString!, _ value: Int) -> Int ``` |
| To | ``` func IOSurfaceAlignProperty(_ property: CFString, _ value: Int) -> Int ``` |

Modified [IOSurfaceCopyValue(_: IOSurface, _: CFString) -> AnyObject?](https://developer.apple.com/documentation/iosurface/1419365-iosurfacecopyvalue)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceCopyValue(_ buffer: IOSurface!, _ key: CFString!) -> Unmanaged<AnyObject>! ``` |
| To | ``` func IOSurfaceCopyValue(_ buffer: IOSurface, _ key: CFString) -> AnyObject? ``` |

Modified [IOSurfaceCreate(_: CFDictionary) -> IOSurface?](https://developer.apple.com/documentation/iosurface/1419383-iosurfacecreate)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceCreate(_ properties: CFDictionary!) -> Unmanaged<IOSurface>! ``` |
| To | ``` func IOSurfaceCreate(_ properties: CFDictionary) -> IOSurface? ``` |

Modified [IOSurfaceCreateMachPort(_: IOSurface) -> mach_port_t](https://developer.apple.com/documentation/iosurface/1419486-iosurfacecreatemachport)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceCreateMachPort(_ buffer: IOSurface!) -> mach_port_t ``` |
| To | ``` func IOSurfaceCreateMachPort(_ buffer: IOSurface) -> mach_port_t ``` |

Modified [IOSurfaceCreateXPCObject(_: IOSurface) -> xpc_object_t](https://developer.apple.com/documentation/iosurface/1419429-iosurfacecreatexpcobject)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceCreateXPCObject(_ aSurface: IOSurface!) -> xpc_object_t! ``` |
| To | ``` func IOSurfaceCreateXPCObject(_ aSurface: IOSurface) -> xpc_object_t ``` |

Modified [IOSurfaceDecrementUseCount(_: IOSurface)](https://developer.apple.com/documentation/iosurface/1419377-iosurfacedecrementusecount)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceDecrementUseCount(_ buffer: IOSurface!) ``` |
| To | ``` func IOSurfaceDecrementUseCount(_ buffer: IOSurface) ``` |

Modified [IOSurfaceGetAllocSize(_: IOSurface) -> Int](https://developer.apple.com/documentation/iosurface/1419391-iosurfacegetallocsize)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetAllocSize(_ buffer: IOSurface!) -> Int ``` |
| To | ``` func IOSurfaceGetAllocSize(_ buffer: IOSurface) -> Int ``` |

Modified [IOSurfaceGetBaseAddress(_: IOSurface) -> UnsafeMutablePointer<Void>](https://developer.apple.com/documentation/iosurface/1419490-iosurfacegetbaseaddress)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetBaseAddress(_ buffer: IOSurface!) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func IOSurfaceGetBaseAddress(_ buffer: IOSurface) -> UnsafeMutablePointer<Void> ``` |

Modified [IOSurfaceGetBaseAddressOfPlane(_: IOSurface, _: Int) -> UnsafeMutablePointer<Void>](https://developer.apple.com/documentation/iosurface/1419379-iosurfacegetbaseaddressofplane)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetBaseAddressOfPlane(_ buffer: IOSurface!, _ planeIndex: Int) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func IOSurfaceGetBaseAddressOfPlane(_ buffer: IOSurface, _ planeIndex: Int) -> UnsafeMutablePointer<Void> ``` |

Modified [IOSurfaceGetBytesPerElement(_: IOSurface) -> Int](https://developer.apple.com/documentation/iosurface/1419389-iosurfacegetbytesperelement)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetBytesPerElement(_ buffer: IOSurface!) -> Int ``` |
| To | ``` func IOSurfaceGetBytesPerElement(_ buffer: IOSurface) -> Int ``` |

Modified [IOSurfaceGetBytesPerElementOfPlane(_: IOSurface, _: Int) -> Int](https://developer.apple.com/documentation/iosurface/1419409-iosurfacegetbytesperelementofpla)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetBytesPerElementOfPlane(_ buffer: IOSurface!, _ planeIndex: Int) -> Int ``` |
| To | ``` func IOSurfaceGetBytesPerElementOfPlane(_ buffer: IOSurface, _ planeIndex: Int) -> Int ``` |

Modified [IOSurfaceGetBytesPerRow(_: IOSurface) -> Int](https://developer.apple.com/documentation/iosurface/1419397-iosurfacegetbytesperrow)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetBytesPerRow(_ buffer: IOSurface!) -> Int ``` |
| To | ``` func IOSurfaceGetBytesPerRow(_ buffer: IOSurface) -> Int ``` |

Modified [IOSurfaceGetBytesPerRowOfPlane(_: IOSurface, _: Int) -> Int](https://developer.apple.com/documentation/iosurface/1419488-iosurfacegetbytesperrowofplane)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetBytesPerRowOfPlane(_ buffer: IOSurface!, _ planeIndex: Int) -> Int ``` |
| To | ``` func IOSurfaceGetBytesPerRowOfPlane(_ buffer: IOSurface, _ planeIndex: Int) -> Int ``` |

Modified [IOSurfaceGetElementHeight(_: IOSurface) -> Int](https://developer.apple.com/documentation/iosurface/1419415-iosurfacegetelementheight)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetElementHeight(_ buffer: IOSurface!) -> Int ``` |
| To | ``` func IOSurfaceGetElementHeight(_ buffer: IOSurface) -> Int ``` |

Modified [IOSurfaceGetElementHeightOfPlane(_: IOSurface, _: Int) -> Int](https://developer.apple.com/documentation/iosurface/1419492-iosurfacegetelementheightofplane)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetElementHeightOfPlane(_ buffer: IOSurface!, _ planeIndex: Int) -> Int ``` |
| To | ``` func IOSurfaceGetElementHeightOfPlane(_ buffer: IOSurface, _ planeIndex: Int) -> Int ``` |

Modified [IOSurfaceGetElementWidth(_: IOSurface) -> Int](https://developer.apple.com/documentation/iosurface/1419375-iosurfacegetelementwidth)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetElementWidth(_ buffer: IOSurface!) -> Int ``` |
| To | ``` func IOSurfaceGetElementWidth(_ buffer: IOSurface) -> Int ``` |

Modified [IOSurfaceGetElementWidthOfPlane(_: IOSurface, _: Int) -> Int](https://developer.apple.com/documentation/iosurface/1419457-iosurfacegetelementwidthofplane)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetElementWidthOfPlane(_ buffer: IOSurface!, _ planeIndex: Int) -> Int ``` |
| To | ``` func IOSurfaceGetElementWidthOfPlane(_ buffer: IOSurface, _ planeIndex: Int) -> Int ``` |

Modified [IOSurfaceGetHeight(_: IOSurface) -> Int](https://developer.apple.com/documentation/iosurface/1419425-iosurfacegetheight)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetHeight(_ buffer: IOSurface!) -> Int ``` |
| To | ``` func IOSurfaceGetHeight(_ buffer: IOSurface) -> Int ``` |

Modified [IOSurfaceGetHeightOfPlane(_: IOSurface, _: Int) -> Int](https://developer.apple.com/documentation/iosurface/1419433-iosurfacegetheightofplane)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetHeightOfPlane(_ buffer: IOSurface!, _ planeIndex: Int) -> Int ``` |
| To | ``` func IOSurfaceGetHeightOfPlane(_ buffer: IOSurface, _ planeIndex: Int) -> Int ``` |

Modified [IOSurfaceGetID(_: IOSurface) -> IOSurfaceID](https://developer.apple.com/documentation/iosurface/1419472-iosurfacegetid)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetID(_ buffer: IOSurface!) -> IOSurfaceID ``` |
| To | ``` func IOSurfaceGetID(_ buffer: IOSurface) -> IOSurfaceID ``` |

Modified [IOSurfaceGetPixelFormat(_: IOSurface) -> OSType](https://developer.apple.com/documentation/iosurface/1419445-iosurfacegetpixelformat)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetPixelFormat(_ buffer: IOSurface!) -> OSType ``` |
| To | ``` func IOSurfaceGetPixelFormat(_ buffer: IOSurface) -> OSType ``` |

Modified [IOSurfaceGetPlaneCount(_: IOSurface) -> Int](https://developer.apple.com/documentation/iosurface/1419427-iosurfacegetplanecount)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetPlaneCount(_ buffer: IOSurface!) -> Int ``` |
| To | ``` func IOSurfaceGetPlaneCount(_ buffer: IOSurface) -> Int ``` |

Modified [IOSurfaceGetPropertyAlignment(_: CFString) -> Int](https://developer.apple.com/documentation/iosurface/1419453-iosurfacegetpropertyalignment)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetPropertyAlignment(_ property: CFString!) -> Int ``` |
| To | ``` func IOSurfaceGetPropertyAlignment(_ property: CFString) -> Int ``` |

Modified [IOSurfaceGetPropertyMaximum(_: CFString) -> Int](https://developer.apple.com/documentation/iosurface/1419421-iosurfacegetpropertymaximum)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetPropertyMaximum(_ property: CFString!) -> Int ``` |
| To | ``` func IOSurfaceGetPropertyMaximum(_ property: CFString) -> Int ``` |

Modified [IOSurfaceGetSeed(_: IOSurface) -> UInt32](https://developer.apple.com/documentation/iosurface/1419431-iosurfacegetseed)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetSeed(_ buffer: IOSurface!) -> UInt32 ``` |
| To | ``` func IOSurfaceGetSeed(_ buffer: IOSurface) -> UInt32 ``` |

Modified [IOSurfaceGetUseCount(_: IOSurface) -> Int32](https://developer.apple.com/documentation/iosurface/1419478-iosurfacegetusecount)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetUseCount(_ buffer: IOSurface!) -> Int32 ``` |
| To | ``` func IOSurfaceGetUseCount(_ buffer: IOSurface) -> Int32 ``` |

Modified [IOSurfaceGetWidth(_: IOSurface) -> Int](https://developer.apple.com/documentation/iosurface/1419385-iosurfacegetwidth)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetWidth(_ buffer: IOSurface!) -> Int ``` |
| To | ``` func IOSurfaceGetWidth(_ buffer: IOSurface) -> Int ``` |

Modified [IOSurfaceGetWidthOfPlane(_: IOSurface, _: Int) -> Int](https://developer.apple.com/documentation/iosurface/1419451-iosurfacegetwidthofplane)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceGetWidthOfPlane(_ buffer: IOSurface!, _ planeIndex: Int) -> Int ``` |
| To | ``` func IOSurfaceGetWidthOfPlane(_ buffer: IOSurface, _ planeIndex: Int) -> Int ``` |

Modified [IOSurfaceIncrementUseCount(_: IOSurface)](https://developer.apple.com/documentation/iosurface/1419455-iosurfaceincrementusecount)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceIncrementUseCount(_ buffer: IOSurface!) ``` |
| To | ``` func IOSurfaceIncrementUseCount(_ buffer: IOSurface) ``` |

Modified [IOSurfaceIsInUse(_: IOSurface) -> Bool](https://developer.apple.com/documentation/iosurface/1419357-iosurfaceisinuse)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceIsInUse(_ buffer: IOSurface!) -> Boolean ``` |
| To | ``` func IOSurfaceIsInUse(_ buffer: IOSurface) -> Bool ``` |

Modified [IOSurfaceLock(_: IOSurface, _: IOSurfaceLockOptions, _: UnsafeMutablePointer<UInt32>) -> IOReturn](https://developer.apple.com/documentation/iosurface/1419474-iosurfacelock)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceLock(_ buffer: IOSurface!, _ options: UInt32, _ seed: UnsafeMutablePointer<UInt32>) -> IOReturn ``` |
| To | ``` func IOSurfaceLock(_ buffer: IOSurface, _ options: IOSurfaceLockOptions, _ seed: UnsafeMutablePointer<UInt32>) -> IOReturn ``` |

Modified [IOSurfaceLookup(_: IOSurfaceID) -> IOSurface?](https://developer.apple.com/documentation/iosurface/1419361-iosurfacelookup)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceLookup(_ csid: IOSurfaceID) -> IOSurface! ``` |
| To | ``` func IOSurfaceLookup(_ csid: IOSurfaceID) -> IOSurface? ``` |

Modified [IOSurfaceLookupFromMachPort(_: mach_port_t) -> IOSurface?](https://developer.apple.com/documentation/iosurface/1419480-iosurfacelookupfrommachport)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceLookupFromMachPort(_ port: mach_port_t) -> IOSurface! ``` |
| To | ``` func IOSurfaceLookupFromMachPort(_ port: mach_port_t) -> IOSurface? ``` |

Modified [IOSurfaceLookupFromXPCObject(_: xpc_object_t) -> IOSurface?](https://developer.apple.com/documentation/iosurface/1419449-iosurfacelookupfromxpcobject)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceLookupFromXPCObject(_ xobj: xpc_object_t!) -> IOSurface! ``` |
| To | ``` func IOSurfaceLookupFromXPCObject(_ xobj: xpc_object_t) -> IOSurface? ``` |

Modified [IOSurfaceRemoveValue(_: IOSurface, _: CFString)](https://developer.apple.com/documentation/iosurface/1419401-iosurfaceremovevalue)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceRemoveValue(_ buffer: IOSurface!, _ key: CFString!) ``` |
| To | ``` func IOSurfaceRemoveValue(_ buffer: IOSurface, _ key: CFString) ``` |

Modified [IOSurfaceSetValue(_: IOSurface, _: CFString, _: AnyObject)](https://developer.apple.com/documentation/iosurface/1419437-iosurfacesetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceSetValue(_ buffer: IOSurface!, _ key: CFString!, _ value: AnyObject!) ``` |
| To | ``` func IOSurfaceSetValue(_ buffer: IOSurface, _ key: CFString, _ value: AnyObject) ``` |

Modified [IOSurfaceUnlock(_: IOSurface, _: IOSurfaceLockOptions, _: UnsafeMutablePointer<UInt32>) -> IOReturn](https://developer.apple.com/documentation/iosurface/1419367-iosurfaceunlock)

|  | Declaration |
| --- | --- |
| From | ``` func IOSurfaceUnlock(_ buffer: IOSurface!, _ options: UInt32, _ seed: UnsafeMutablePointer<UInt32>) -> IOReturn ``` |
| To | ``` func IOSurfaceUnlock(_ buffer: IOSurface, _ options: IOSurfaceLockOptions, _ seed: UnsafeMutablePointer<UInt32>) -> IOReturn ``` |

Modified [kIOSurfaceAllocSize](https://developer.apple.com/documentation/iosurface/kiosurfaceallocsize)

|  | Declaration |
| --- | --- |
| From | ``` let kIOSurfaceAllocSize: CFString! ``` |
| To | ``` let kIOSurfaceAllocSize: CFString ``` |

Modified [kIOSurfaceBytesPerElement](https://developer.apple.com/documentation/iosurface/kiosurfacebytesperelement)

|  | Declaration |
| --- | --- |
| From | ``` let kIOSurfaceBytesPerElement: CFString! ``` |
| To | ``` let kIOSurfaceBytesPerElement: CFString ``` |

Modified [kIOSurfaceBytesPerRow](https://developer.apple.com/documentation/iosurface/kiosurfacebytesperrow)

|  | Declaration |
| --- | --- |
| From | ``` let kIOSurfaceBytesPerRow: CFString! ``` |
| To | ``` let kIOSurfaceBytesPerRow: CFString ``` |

Modified [kIOSurfaceCacheMode](https://developer.apple.com/documentation/iosurface/kiosurfacecachemode)

|  | Declaration |
| --- | --- |
| From | ``` let kIOSurfaceCacheMode: CFString! ``` |
| To | ``` let kIOSurfaceCacheMode: CFString ``` |

Modified [kIOSurfaceElementHeight](https://developer.apple.com/documentation/iosurface/kiosurfaceelementheight)

|  | Declaration |
| --- | --- |
| From | ``` let kIOSurfaceElementHeight: CFString! ``` |
| To | ``` let kIOSurfaceElementHeight: CFString ``` |

Modified [kIOSurfaceElementWidth](https://developer.apple.com/documentation/iosurface/kiosurfaceelementwidth)

|  | Declaration |
| --- | --- |
| From | ``` let kIOSurfaceElementWidth: CFString! ``` |
| To | ``` let kIOSurfaceElementWidth: CFString ``` |

Modified [kIOSurfaceHeight](https://developer.apple.com/documentation/iosurface/kiosurfaceheight)

|  | Declaration |
| --- | --- |
| From | ``` let kIOSurfaceHeight: CFString! ``` |
| To | ``` let kIOSurfaceHeight: CFString ``` |

Modified [kIOSurfaceIsGlobal](https://developer.apple.com/documentation/iosurface/kiosurfaceisglobal)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kIOSurfaceIsGlobal: CFString! ``` | -- |
| To | ``` let kIOSurfaceIsGlobal: CFString ``` | OS X 10.11 |

Modified [kIOSurfaceOffset](https://developer.apple.com/documentation/iosurface/kiosurfaceoffset)

|  | Declaration |
| --- | --- |
| From | ``` let kIOSurfaceOffset: CFString! ``` |
| To | ``` let kIOSurfaceOffset: CFString ``` |

Modified [kIOSurfacePixelFormat](https://developer.apple.com/documentation/iosurface/kiosurfacepixelformat)

|  | Declaration |
| --- | --- |
| From | ``` let kIOSurfacePixelFormat: CFString! ``` |
| To | ``` let kIOSurfacePixelFormat: CFString ``` |

Modified [kIOSurfacePlaneBase](https://developer.apple.com/documentation/iosurface/kiosurfaceplanebase)

|  | Declaration |
| --- | --- |
| From | ``` let kIOSurfacePlaneBase: CFString! ``` |
| To | ``` let kIOSurfacePlaneBase: CFString ``` |

Modified [kIOSurfacePlaneBytesPerElement](https://developer.apple.com/documentation/iosurface/kiosurfaceplanebytesperelement)

|  | Declaration |
| --- | --- |
| From | ``` let kIOSurfacePlaneBytesPerElement: CFString! ``` |
| To | ``` let kIOSurfacePlaneBytesPerElement: CFString ``` |

Modified [kIOSurfacePlaneBytesPerRow](https://developer.apple.com/documentation/iosurface/kiosurfaceplanebytesperrow)

|  | Declaration |
| --- | --- |
| From | ``` let kIOSurfacePlaneBytesPerRow: CFString! ``` |
| To | ``` let kIOSurfacePlaneBytesPerRow: CFString ``` |

Modified [kIOSurfacePlaneElementHeight](https://developer.apple.com/documentation/iosurface/kiosurfaceplaneelementheight)

|  | Declaration |
| --- | --- |
| From | ``` let kIOSurfacePlaneElementHeight: CFString! ``` |
| To | ``` let kIOSurfacePlaneElementHeight: CFString ``` |

Modified [kIOSurfacePlaneElementWidth](https://developer.apple.com/documentation/iosurface/kiosurfaceplaneelementwidth)

|  | Declaration |
| --- | --- |
| From | ``` let kIOSurfacePlaneElementWidth: CFString! ``` |
| To | ``` let kIOSurfacePlaneElementWidth: CFString ``` |

Modified [kIOSurfacePlaneHeight](https://developer.apple.com/documentation/iosurface/kiosurfaceplaneheight)

|  | Declaration |
| --- | --- |
| From | ``` let kIOSurfacePlaneHeight: CFString! ``` |
| To | ``` let kIOSurfacePlaneHeight: CFString ``` |

Modified [kIOSurfacePlaneInfo](https://developer.apple.com/documentation/iosurface/kiosurfaceplaneinfo)

|  | Declaration |
| --- | --- |
| From | ``` let kIOSurfacePlaneInfo: CFString! ``` |
| To | ``` let kIOSurfacePlaneInfo: CFString ``` |

Modified [kIOSurfacePlaneOffset](https://developer.apple.com/documentation/iosurface/kiosurfaceplaneoffset)

|  | Declaration |
| --- | --- |
| From | ``` let kIOSurfacePlaneOffset: CFString! ``` |
| To | ``` let kIOSurfacePlaneOffset: CFString ``` |

Modified [kIOSurfacePlaneSize](https://developer.apple.com/documentation/iosurface/kiosurfaceplanesize)

|  | Declaration |
| --- | --- |
| From | ``` let kIOSurfacePlaneSize: CFString! ``` |
| To | ``` let kIOSurfacePlaneSize: CFString ``` |

Modified [kIOSurfacePlaneWidth](https://developer.apple.com/documentation/iosurface/kiosurfaceplanewidth)

|  | Declaration |
| --- | --- |
| From | ``` let kIOSurfacePlaneWidth: CFString! ``` |
| To | ``` let kIOSurfacePlaneWidth: CFString ``` |

Modified [kIOSurfaceWidth](https://developer.apple.com/documentation/iosurface/kiosurfacewidth)

|  | Declaration |
| --- | --- |
| From | ``` let kIOSurfaceWidth: CFString! ``` |
| To | ``` let kIOSurfaceWidth: CFString ``` |

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
