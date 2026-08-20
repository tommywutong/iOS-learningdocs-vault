---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/IOSurface.html
archived_at: '2026-07-18T02:52:31.788391Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# IOSurface Changes

## IOSurface

Modified IOSurfaceAlignProperty(CFString!, Int) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOSurfaceAlignProperty(_ property: CFString!, _ value: UInt) -> UInt ``` | OS X 10.10 |
| To | ``` func IOSurfaceAlignProperty(_ property: CFString!, _ value: Int) -> Int ``` | OS X 10.6 |

Modified IOSurfaceCopyValue(IOSurface!, CFString!) -> Unmanaged<AnyObject>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified IOSurfaceCreate(CFDictionary!) -> Unmanaged<IOSurface>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified IOSurfaceCreateMachPort(IOSurface!) -> mach_port_t

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified IOSurfaceCreateXPCObject(IOSurface!) -> xpc_object_t!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOSurfaceDecrementUseCount(IOSurface!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified IOSurfaceGetAllocSize(IOSurface!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOSurfaceGetAllocSize(_ buffer: IOSurface!) -> UInt ``` | OS X 10.10 |
| To | ``` func IOSurfaceGetAllocSize(_ buffer: IOSurface!) -> Int ``` | OS X 10.6 |

Modified IOSurfaceGetBaseAddress(IOSurface!) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOSurfaceGetBaseAddress(_ buffer: IOSurface!) -> UnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func IOSurfaceGetBaseAddress(_ buffer: IOSurface!) -> UnsafeMutablePointer<Void> ``` | OS X 10.6 |

Modified IOSurfaceGetBaseAddressOfPlane(IOSurface!, Int) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOSurfaceGetBaseAddressOfPlane(_ buffer: IOSurface!, _ planeIndex: UInt) -> UnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func IOSurfaceGetBaseAddressOfPlane(_ buffer: IOSurface!, _ planeIndex: Int) -> UnsafeMutablePointer<Void> ``` | OS X 10.6 |

Modified IOSurfaceGetBytesPerElement(IOSurface!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOSurfaceGetBytesPerElement(_ buffer: IOSurface!) -> UInt ``` | OS X 10.10 |
| To | ``` func IOSurfaceGetBytesPerElement(_ buffer: IOSurface!) -> Int ``` | OS X 10.6 |

Modified IOSurfaceGetBytesPerElementOfPlane(IOSurface!, Int) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOSurfaceGetBytesPerElementOfPlane(_ buffer: IOSurface!, _ planeIndex: UInt) -> UInt ``` | OS X 10.10 |
| To | ``` func IOSurfaceGetBytesPerElementOfPlane(_ buffer: IOSurface!, _ planeIndex: Int) -> Int ``` | OS X 10.6 |

Modified IOSurfaceGetBytesPerRow(IOSurface!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOSurfaceGetBytesPerRow(_ buffer: IOSurface!) -> UInt ``` | OS X 10.10 |
| To | ``` func IOSurfaceGetBytesPerRow(_ buffer: IOSurface!) -> Int ``` | OS X 10.6 |

Modified IOSurfaceGetBytesPerRowOfPlane(IOSurface!, Int) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOSurfaceGetBytesPerRowOfPlane(_ buffer: IOSurface!, _ planeIndex: UInt) -> UInt ``` | OS X 10.10 |
| To | ``` func IOSurfaceGetBytesPerRowOfPlane(_ buffer: IOSurface!, _ planeIndex: Int) -> Int ``` | OS X 10.6 |

Modified IOSurfaceGetElementHeight(IOSurface!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOSurfaceGetElementHeight(_ buffer: IOSurface!) -> UInt ``` | OS X 10.10 |
| To | ``` func IOSurfaceGetElementHeight(_ buffer: IOSurface!) -> Int ``` | OS X 10.6 |

Modified IOSurfaceGetElementHeightOfPlane(IOSurface!, Int) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOSurfaceGetElementHeightOfPlane(_ buffer: IOSurface!, _ planeIndex: UInt) -> UInt ``` | OS X 10.10 |
| To | ``` func IOSurfaceGetElementHeightOfPlane(_ buffer: IOSurface!, _ planeIndex: Int) -> Int ``` | OS X 10.6 |

Modified IOSurfaceGetElementWidth(IOSurface!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOSurfaceGetElementWidth(_ buffer: IOSurface!) -> UInt ``` | OS X 10.10 |
| To | ``` func IOSurfaceGetElementWidth(_ buffer: IOSurface!) -> Int ``` | OS X 10.6 |

Modified IOSurfaceGetElementWidthOfPlane(IOSurface!, Int) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOSurfaceGetElementWidthOfPlane(_ buffer: IOSurface!, _ planeIndex: UInt) -> UInt ``` | OS X 10.10 |
| To | ``` func IOSurfaceGetElementWidthOfPlane(_ buffer: IOSurface!, _ planeIndex: Int) -> Int ``` | OS X 10.6 |

Modified IOSurfaceGetHeight(IOSurface!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOSurfaceGetHeight(_ buffer: IOSurface!) -> UInt ``` | OS X 10.10 |
| To | ``` func IOSurfaceGetHeight(_ buffer: IOSurface!) -> Int ``` | OS X 10.6 |

Modified IOSurfaceGetHeightOfPlane(IOSurface!, Int) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOSurfaceGetHeightOfPlane(_ buffer: IOSurface!, _ planeIndex: UInt) -> UInt ``` | OS X 10.10 |
| To | ``` func IOSurfaceGetHeightOfPlane(_ buffer: IOSurface!, _ planeIndex: Int) -> Int ``` | OS X 10.6 |

Modified IOSurfaceGetID(IOSurface!) -> IOSurfaceID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified IOSurfaceGetPixelFormat(IOSurface!) -> OSType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified IOSurfaceGetPlaneCount(IOSurface!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOSurfaceGetPlaneCount(_ buffer: IOSurface!) -> UInt ``` | OS X 10.10 |
| To | ``` func IOSurfaceGetPlaneCount(_ buffer: IOSurface!) -> Int ``` | OS X 10.6 |

Modified IOSurfaceGetPropertyAlignment(CFString!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOSurfaceGetPropertyAlignment(_ property: CFString!) -> UInt ``` | OS X 10.10 |
| To | ``` func IOSurfaceGetPropertyAlignment(_ property: CFString!) -> Int ``` | OS X 10.6 |

Modified IOSurfaceGetPropertyMaximum(CFString!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOSurfaceGetPropertyMaximum(_ property: CFString!) -> UInt ``` | OS X 10.10 |
| To | ``` func IOSurfaceGetPropertyMaximum(_ property: CFString!) -> Int ``` | OS X 10.6 |

Modified IOSurfaceGetSeed(IOSurface!) -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified IOSurfaceGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified IOSurfaceGetUseCount(IOSurface!) -> Int32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified IOSurfaceGetWidth(IOSurface!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOSurfaceGetWidth(_ buffer: IOSurface!) -> UInt ``` | OS X 10.10 |
| To | ``` func IOSurfaceGetWidth(_ buffer: IOSurface!) -> Int ``` | OS X 10.6 |

Modified IOSurfaceGetWidthOfPlane(IOSurface!, Int) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOSurfaceGetWidthOfPlane(_ buffer: IOSurface!, _ planeIndex: UInt) -> UInt ``` | OS X 10.10 |
| To | ``` func IOSurfaceGetWidthOfPlane(_ buffer: IOSurface!, _ planeIndex: Int) -> Int ``` | OS X 10.6 |

Modified IOSurfaceIncrementUseCount(IOSurface!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified IOSurfaceIsInUse(IOSurface!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified IOSurfaceLock(IOSurface!, UInt32, UnsafeMutablePointer<UInt32>) -> IOReturn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOSurfaceLock(_ buffer: IOSurface!, _ options: UInt32, _ seed: UnsafePointer<UInt32>) -> IOReturn ``` | OS X 10.10 |
| To | ``` func IOSurfaceLock(_ buffer: IOSurface!, _ options: UInt32, _ seed: UnsafeMutablePointer<UInt32>) -> IOReturn ``` | OS X 10.6 |

Modified IOSurfaceLookup(IOSurfaceID) -> IOSurface!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified IOSurfaceLookupFromMachPort(mach_port_t) -> IOSurface!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified IOSurfaceLookupFromXPCObject(xpc_object_t!) -> IOSurface!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOSurfaceRemoveValue(IOSurface!, CFString!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified IOSurfaceSetValue(IOSurface!, CFString!, AnyObject!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified IOSurfaceUnlock(IOSurface!, UInt32, UnsafeMutablePointer<UInt32>) -> IOReturn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOSurfaceUnlock(_ buffer: IOSurface!, _ options: UInt32, _ seed: UnsafePointer<UInt32>) -> IOReturn ``` | OS X 10.10 |
| To | ``` func IOSurfaceUnlock(_ buffer: IOSurface!, _ options: UInt32, _ seed: UnsafeMutablePointer<UInt32>) -> IOReturn ``` | OS X 10.6 |

Modified kIOSurfaceAllocSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kIOSurfaceBytesPerElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kIOSurfaceBytesPerRow

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kIOSurfaceCacheMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kIOSurfaceElementHeight

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kIOSurfaceElementWidth

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kIOSurfaceHeight

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kIOSurfaceIsGlobal

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kIOSurfaceOffset

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kIOSurfacePixelFormat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kIOSurfacePlaneBase

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kIOSurfacePlaneBytesPerElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kIOSurfacePlaneBytesPerRow

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kIOSurfacePlaneElementHeight

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kIOSurfacePlaneElementWidth

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kIOSurfacePlaneHeight

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kIOSurfacePlaneInfo

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kIOSurfacePlaneOffset

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kIOSurfacePlaneSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kIOSurfacePlaneWidth

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kIOSurfaceWidth

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

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
