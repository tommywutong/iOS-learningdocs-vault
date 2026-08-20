---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/IOSurface.html
archived_at: '2026-07-18T02:53:07.778938Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# IOSurface Changes for Objective-C

### IOSurface

#### IOSurfaceAPI.h

Added [IOSurfaceCopyAllValues()](https://developer.apple.com/documentation/iosurface/1419387-iosurfacecopyallvalues)Added [IOSurfaceLockOptions](https://developer.apple.com/documentation/iosurface/iosurfacelockoptions)Added [IOSurfaceRemoveAllValues()](https://developer.apple.com/documentation/iosurface/1419413-iosurfaceremoveallvalues)Added [IOSurfaceSetValues()](https://developer.apple.com/documentation/iosurface/1419403-iosurfacesetvalues)Modified [IOSurfaceAlignProperty()](https://developer.apple.com/documentation/iosurface/1419447-iosurfacealignproperty)

|  | Declaration |
| --- | --- |
| From | ``` size_t IOSurfaceAlignProperty (     CFStringRef property,     size_t value ); ``` |
| To | ``` size_t IOSurfaceAlignProperty (     CFStringRef _Nonnull property,     size_t value ); ``` |

Modified [IOSurfaceCopyValue()](https://developer.apple.com/documentation/iosurface/1419365-iosurfacecopyvalue)

|  | Declaration |
| --- | --- |
| From | ``` CFTypeRef IOSurfaceCopyValue (     IOSurfaceRef buffer,     CFStringRef key ); ``` |
| To | ``` CFTypeRef _Nullable IOSurfaceCopyValue (     IOSurfaceRef _Nonnull buffer,     CFStringRef _Nonnull key ); ``` |

Modified [IOSurfaceCreate()](https://developer.apple.com/documentation/iosurface/1419383-iosurfacecreate)

|  | Declaration |
| --- | --- |
| From | ``` IOSurfaceRef IOSurfaceCreate (     CFDictionaryRef properties ); ``` |
| To | ``` IOSurfaceRef _Nullable IOSurfaceCreate (     CFDictionaryRef _Nonnull properties ); ``` |

Modified [IOSurfaceCreateMachPort()](https://developer.apple.com/documentation/iosurface/1419486-iosurfacecreatemachport)

|  | Declaration |
| --- | --- |
| From | ``` mach_port_t IOSurfaceCreateMachPort (     IOSurfaceRef buffer ); ``` |
| To | ``` mach_port_t IOSurfaceCreateMachPort (     IOSurfaceRef _Nonnull buffer ); ``` |

Modified [IOSurfaceCreateXPCObject()](https://developer.apple.com/documentation/iosurface/1419429-iosurfacecreatexpcobject)

|  | Declaration |
| --- | --- |
| From | ``` xpc_object_t IOSurfaceCreateXPCObject (     IOSurfaceRef aSurface ); ``` |
| To | ``` xpc_object_t _Nonnull IOSurfaceCreateXPCObject (     IOSurfaceRef _Nonnull aSurface ); ``` |

Modified [IOSurfaceDecrementUseCount()](https://developer.apple.com/documentation/iosurface/1419377-iosurfacedecrementusecount)

|  | Declaration |
| --- | --- |
| From | ``` void IOSurfaceDecrementUseCount (     IOSurfaceRef buffer ); ``` |
| To | ``` void IOSurfaceDecrementUseCount (     IOSurfaceRef _Nonnull buffer ); ``` |

Modified [IOSurfaceGetAllocSize()](https://developer.apple.com/documentation/iosurface/1419391-iosurfacegetallocsize)

|  | Declaration |
| --- | --- |
| From | ``` size_t IOSurfaceGetAllocSize (     IOSurfaceRef buffer ); ``` |
| To | ``` size_t IOSurfaceGetAllocSize (     IOSurfaceRef _Nonnull buffer ); ``` |

Modified [IOSurfaceGetBaseAddress()](https://developer.apple.com/documentation/iosurface/1419490-iosurfacegetbaseaddress)

|  | Declaration |
| --- | --- |
| From | ``` void * IOSurfaceGetBaseAddress (     IOSurfaceRef buffer ); ``` |
| To | ``` void * _Nonnull IOSurfaceGetBaseAddress (     IOSurfaceRef _Nonnull buffer ); ``` |

Modified [IOSurfaceGetBaseAddressOfPlane()](https://developer.apple.com/documentation/iosurface/1419379-iosurfacegetbaseaddressofplane)

|  | Declaration |
| --- | --- |
| From | ``` void * IOSurfaceGetBaseAddressOfPlane (     IOSurfaceRef buffer,     size_t planeIndex ); ``` |
| To | ``` void * _Nonnull IOSurfaceGetBaseAddressOfPlane (     IOSurfaceRef _Nonnull buffer,     size_t planeIndex ); ``` |

Modified [IOSurfaceGetBytesPerElement()](https://developer.apple.com/documentation/iosurface/1419389-iosurfacegetbytesperelement)

|  | Declaration |
| --- | --- |
| From | ``` size_t IOSurfaceGetBytesPerElement (     IOSurfaceRef buffer ); ``` |
| To | ``` size_t IOSurfaceGetBytesPerElement (     IOSurfaceRef _Nonnull buffer ); ``` |

Modified [IOSurfaceGetBytesPerElementOfPlane()](https://developer.apple.com/documentation/iosurface/1419409-iosurfacegetbytesperelementofpla)

|  | Declaration |
| --- | --- |
| From | ``` size_t IOSurfaceGetBytesPerElementOfPlane (     IOSurfaceRef buffer,     size_t planeIndex ); ``` |
| To | ``` size_t IOSurfaceGetBytesPerElementOfPlane (     IOSurfaceRef _Nonnull buffer,     size_t planeIndex ); ``` |

Modified [IOSurfaceGetBytesPerRow()](https://developer.apple.com/documentation/iosurface/1419397-iosurfacegetbytesperrow)

|  | Declaration |
| --- | --- |
| From | ``` size_t IOSurfaceGetBytesPerRow (     IOSurfaceRef buffer ); ``` |
| To | ``` size_t IOSurfaceGetBytesPerRow (     IOSurfaceRef _Nonnull buffer ); ``` |

Modified [IOSurfaceGetBytesPerRowOfPlane()](https://developer.apple.com/documentation/iosurface/1419488-iosurfacegetbytesperrowofplane)

|  | Declaration |
| --- | --- |
| From | ``` size_t IOSurfaceGetBytesPerRowOfPlane (     IOSurfaceRef buffer,     size_t planeIndex ); ``` |
| To | ``` size_t IOSurfaceGetBytesPerRowOfPlane (     IOSurfaceRef _Nonnull buffer,     size_t planeIndex ); ``` |

Modified [IOSurfaceGetElementHeight()](https://developer.apple.com/documentation/iosurface/1419415-iosurfacegetelementheight)

|  | Declaration |
| --- | --- |
| From | ``` size_t IOSurfaceGetElementHeight (     IOSurfaceRef buffer ); ``` |
| To | ``` size_t IOSurfaceGetElementHeight (     IOSurfaceRef _Nonnull buffer ); ``` |

Modified [IOSurfaceGetElementHeightOfPlane()](https://developer.apple.com/documentation/iosurface/1419492-iosurfacegetelementheightofplane)

|  | Declaration |
| --- | --- |
| From | ``` size_t IOSurfaceGetElementHeightOfPlane (     IOSurfaceRef buffer,     size_t planeIndex ); ``` |
| To | ``` size_t IOSurfaceGetElementHeightOfPlane (     IOSurfaceRef _Nonnull buffer,     size_t planeIndex ); ``` |

Modified [IOSurfaceGetElementWidth()](https://developer.apple.com/documentation/iosurface/1419375-iosurfacegetelementwidth)

|  | Declaration |
| --- | --- |
| From | ``` size_t IOSurfaceGetElementWidth (     IOSurfaceRef buffer ); ``` |
| To | ``` size_t IOSurfaceGetElementWidth (     IOSurfaceRef _Nonnull buffer ); ``` |

Modified [IOSurfaceGetElementWidthOfPlane()](https://developer.apple.com/documentation/iosurface/1419457-iosurfacegetelementwidthofplane)

|  | Declaration |
| --- | --- |
| From | ``` size_t IOSurfaceGetElementWidthOfPlane (     IOSurfaceRef buffer,     size_t planeIndex ); ``` |
| To | ``` size_t IOSurfaceGetElementWidthOfPlane (     IOSurfaceRef _Nonnull buffer,     size_t planeIndex ); ``` |

Modified [IOSurfaceGetHeight()](https://developer.apple.com/documentation/iosurface/1419425-iosurfacegetheight)

|  | Declaration |
| --- | --- |
| From | ``` size_t IOSurfaceGetHeight (     IOSurfaceRef buffer ); ``` |
| To | ``` size_t IOSurfaceGetHeight (     IOSurfaceRef _Nonnull buffer ); ``` |

Modified [IOSurfaceGetHeightOfPlane()](https://developer.apple.com/documentation/iosurface/1419433-iosurfacegetheightofplane)

|  | Declaration |
| --- | --- |
| From | ``` size_t IOSurfaceGetHeightOfPlane (     IOSurfaceRef buffer,     size_t planeIndex ); ``` |
| To | ``` size_t IOSurfaceGetHeightOfPlane (     IOSurfaceRef _Nonnull buffer,     size_t planeIndex ); ``` |

Modified [IOSurfaceGetID()](https://developer.apple.com/documentation/iosurface/1419472-iosurfacegetid)

|  | Declaration |
| --- | --- |
| From | ``` IOSurfaceID IOSurfaceGetID (     IOSurfaceRef buffer ); ``` |
| To | ``` IOSurfaceID IOSurfaceGetID (     IOSurfaceRef _Nonnull buffer ); ``` |

Modified [IOSurfaceGetPixelFormat()](https://developer.apple.com/documentation/iosurface/1419445-iosurfacegetpixelformat)

|  | Declaration |
| --- | --- |
| From | ``` OSType IOSurfaceGetPixelFormat (     IOSurfaceRef buffer ); ``` |
| To | ``` OSType IOSurfaceGetPixelFormat (     IOSurfaceRef _Nonnull buffer ); ``` |

Modified [IOSurfaceGetPlaneCount()](https://developer.apple.com/documentation/iosurface/1419427-iosurfacegetplanecount)

|  | Declaration |
| --- | --- |
| From | ``` size_t IOSurfaceGetPlaneCount (     IOSurfaceRef buffer ); ``` |
| To | ``` size_t IOSurfaceGetPlaneCount (     IOSurfaceRef _Nonnull buffer ); ``` |

Modified [IOSurfaceGetPropertyAlignment()](https://developer.apple.com/documentation/iosurface/1419453-iosurfacegetpropertyalignment)

|  | Declaration |
| --- | --- |
| From | ``` size_t IOSurfaceGetPropertyAlignment (     CFStringRef property ); ``` |
| To | ``` size_t IOSurfaceGetPropertyAlignment (     CFStringRef _Nonnull property ); ``` |

Modified [IOSurfaceGetPropertyMaximum()](https://developer.apple.com/documentation/iosurface/1419421-iosurfacegetpropertymaximum)

|  | Declaration |
| --- | --- |
| From | ``` size_t IOSurfaceGetPropertyMaximum (     CFStringRef property ); ``` |
| To | ``` size_t IOSurfaceGetPropertyMaximum (     CFStringRef _Nonnull property ); ``` |

Modified [IOSurfaceGetSeed()](https://developer.apple.com/documentation/iosurface/1419431-iosurfacegetseed)

|  | Declaration |
| --- | --- |
| From | ``` uint32_t IOSurfaceGetSeed (     IOSurfaceRef buffer ); ``` |
| To | ``` uint32_t IOSurfaceGetSeed (     IOSurfaceRef _Nonnull buffer ); ``` |

Modified [IOSurfaceGetUseCount()](https://developer.apple.com/documentation/iosurface/1419478-iosurfacegetusecount)

|  | Declaration |
| --- | --- |
| From | ``` int32_t IOSurfaceGetUseCount (     IOSurfaceRef buffer ); ``` |
| To | ``` int32_t IOSurfaceGetUseCount (     IOSurfaceRef _Nonnull buffer ); ``` |

Modified [IOSurfaceGetWidth()](https://developer.apple.com/documentation/iosurface/1419385-iosurfacegetwidth)

|  | Declaration |
| --- | --- |
| From | ``` size_t IOSurfaceGetWidth (     IOSurfaceRef buffer ); ``` |
| To | ``` size_t IOSurfaceGetWidth (     IOSurfaceRef _Nonnull buffer ); ``` |

Modified [IOSurfaceGetWidthOfPlane()](https://developer.apple.com/documentation/iosurface/1419451-iosurfacegetwidthofplane)

|  | Declaration |
| --- | --- |
| From | ``` size_t IOSurfaceGetWidthOfPlane (     IOSurfaceRef buffer,     size_t planeIndex ); ``` |
| To | ``` size_t IOSurfaceGetWidthOfPlane (     IOSurfaceRef _Nonnull buffer,     size_t planeIndex ); ``` |

Modified [IOSurfaceIncrementUseCount()](https://developer.apple.com/documentation/iosurface/1419455-iosurfaceincrementusecount)

|  | Declaration |
| --- | --- |
| From | ``` void IOSurfaceIncrementUseCount (     IOSurfaceRef buffer ); ``` |
| To | ``` void IOSurfaceIncrementUseCount (     IOSurfaceRef _Nonnull buffer ); ``` |

Modified [IOSurfaceIsInUse()](https://developer.apple.com/documentation/iosurface/1419357-iosurfaceisinuse)

|  | Declaration |
| --- | --- |
| From | ``` Boolean IOSurfaceIsInUse (     IOSurfaceRef buffer ); ``` |
| To | ``` Boolean IOSurfaceIsInUse (     IOSurfaceRef _Nonnull buffer ); ``` |

Modified [IOSurfaceLock()](https://developer.apple.com/documentation/iosurface/1419474-iosurfacelock)

|  | Declaration |
| --- | --- |
| From | ``` IOReturn IOSurfaceLock (     IOSurfaceRef buffer,     uint32_t options,     uint32_t *seed ); ``` |
| To | ``` IOReturn IOSurfaceLock (     IOSurfaceRef _Nonnull buffer,     IOSurfaceLockOptions options,     uint32_t * _Nullable seed ); ``` |

Modified [IOSurfaceLookup()](https://developer.apple.com/documentation/iosurface/1419361-iosurfacelookup)

|  | Declaration |
| --- | --- |
| From | ``` IOSurfaceRef IOSurfaceLookup (     IOSurfaceID csid ); ``` |
| To | ``` IOSurfaceRef _Nullable IOSurfaceLookup (     IOSurfaceID csid ); ``` |

Modified [IOSurfaceLookupFromMachPort()](https://developer.apple.com/documentation/iosurface/1419480-iosurfacelookupfrommachport)

|  | Declaration |
| --- | --- |
| From | ``` IOSurfaceRef IOSurfaceLookupFromMachPort (     mach_port_t port ); ``` |
| To | ``` IOSurfaceRef _Nullable IOSurfaceLookupFromMachPort (     mach_port_t port ); ``` |

Modified [IOSurfaceLookupFromXPCObject()](https://developer.apple.com/documentation/iosurface/1419449-iosurfacelookupfromxpcobject)

|  | Declaration |
| --- | --- |
| From | ``` IOSurfaceRef IOSurfaceLookupFromXPCObject (     xpc_object_t xobj ); ``` |
| To | ``` IOSurfaceRef _Nullable IOSurfaceLookupFromXPCObject (     xpc_object_t _Nonnull xobj ); ``` |

Modified [IOSurfaceRemoveValue()](https://developer.apple.com/documentation/iosurface/1419401-iosurfaceremovevalue)

|  | Declaration |
| --- | --- |
| From | ``` void IOSurfaceRemoveValue (     IOSurfaceRef buffer,     CFStringRef key ); ``` |
| To | ``` void IOSurfaceRemoveValue (     IOSurfaceRef _Nonnull buffer,     CFStringRef _Nonnull key ); ``` |

Modified [IOSurfaceSetValue()](https://developer.apple.com/documentation/iosurface/1419437-iosurfacesetvalue)

|  | Declaration |
| --- | --- |
| From | ``` void IOSurfaceSetValue (     IOSurfaceRef buffer,     CFStringRef key,     CFTypeRef value ); ``` |
| To | ``` void IOSurfaceSetValue (     IOSurfaceRef _Nonnull buffer,     CFStringRef _Nonnull key,     CFTypeRef _Nonnull value ); ``` |

Modified [IOSurfaceUnlock()](https://developer.apple.com/documentation/iosurface/1419367-iosurfaceunlock)

|  | Declaration |
| --- | --- |
| From | ``` IOReturn IOSurfaceUnlock (     IOSurfaceRef buffer,     uint32_t options,     uint32_t *seed ); ``` |
| To | ``` IOReturn IOSurfaceUnlock (     IOSurfaceRef _Nonnull buffer,     IOSurfaceLockOptions options,     uint32_t * _Nullable seed ); ``` |

Modified [kIOSurfaceIsGlobal](https://developer.apple.com/documentation/iosurface/kiosurfaceisglobal)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

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
