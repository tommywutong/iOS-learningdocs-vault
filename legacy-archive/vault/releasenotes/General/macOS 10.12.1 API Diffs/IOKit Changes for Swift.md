---
title: macOS 10.12.1 API Diffs
apple_id: TP40017565
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12_1/Swift/IOKit.html
archived_at: '2026-07-18T02:51:46.216171Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12.1 API Diffs](macOS%2010.12%20to%20macOS%2010.12.1%20API%20Differences.md)


# IOKit Changes for Swift

### IOKit

Modified [IOCFPlugInInterfaceStruct [struct]](https://developer.apple.com/documentation/iokit/iocfplugininterfacestruct)

|  | Declaration |
| --- | --- |
| From | ``` struct IOCFPlugInInterfaceStruct {     var _reserved: UnsafeMutableRawPointer!     var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!     var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!     var Release: ((UnsafeMutableRawPointer?) -> ULONG)!     var version: UInt16     var revision: UInt16     var Probe: ((UnsafeMutableRawPointer?, CFDictionary?, io_service_t, UnsafeMutablePointer<Int32>?) -> IOReturn)!     var Start: ((UnsafeMutableRawPointer?, CFDictionary?, io_service_t) -> IOReturn)!     var Stop: ((UnsafeMutableRawPointer?) -> IOReturn)!     init()     init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: (@escaping (UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, Release Release: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, version version: UInt16, revision revision: UInt16, Probe Probe: (@escaping (UnsafeMutableRawPointer?, CFDictionary?, io_service_t, UnsafeMutablePointer<Int32>?) -> IOReturn)!, Start Start: (@escaping (UnsafeMutableRawPointer?, CFDictionary?, io_service_t) -> IOReturn)!, Stop Stop: (@escaping (UnsafeMutableRawPointer?) -> IOReturn)!) } ``` |
| To | ``` struct IOCFPlugInInterfaceStruct {     var _reserved: UnsafeMutableRawPointer!     var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!     var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!     var Release: ((UnsafeMutableRawPointer?) -> ULONG)!     var version: UInt16     var revision: UInt16     var Probe: ((UnsafeMutableRawPointer?, CFDictionary?, io_service_t, UnsafeMutablePointer<Int32>?) -> IOReturn)!     var Start: ((UnsafeMutableRawPointer?, CFDictionary?, io_service_t) -> IOReturn)!     var Stop: ((UnsafeMutableRawPointer?) -> IOReturn)!     init()     init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!, Release Release: ((UnsafeMutableRawPointer?) -> ULONG)!, version version: UInt16, revision revision: UInt16, Probe Probe: ((UnsafeMutableRawPointer?, CFDictionary?, io_service_t, UnsafeMutablePointer<Int32>?) -> IOReturn)!, Start Start: ((UnsafeMutableRawPointer?, CFDictionary?, io_service_t) -> IOReturn)!, Stop Stop: ((UnsafeMutableRawPointer?) -> IOReturn)!) } ``` |

Modified [IOCFPlugInInterfaceStruct.init(_reserved: UnsafeMutableRawPointer!, QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!, Release: ((UnsafeMutableRawPointer?) -> ULONG)!, version: UInt16, revision: UInt16, Probe: ((UnsafeMutableRawPointer?, CFDictionary?, io_service_t, UnsafeMutablePointer<Int32>?) -> IOReturn)!, Start: ((UnsafeMutableRawPointer?, CFDictionary?, io_service_t) -> IOReturn)!, Stop: ((UnsafeMutableRawPointer?) -> IOReturn)!)](https://developer.apple.com/documentation/iokit/iocfplugininterfacestruct/1792000-init)

|  | Declaration |
| --- | --- |
| From | ``` init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: (@escaping (UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, Release Release: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, version version: UInt16, revision revision: UInt16, Probe Probe: (@escaping (UnsafeMutableRawPointer?, CFDictionary?, io_service_t, UnsafeMutablePointer<Int32>?) -> IOReturn)!, Start Start: (@escaping (UnsafeMutableRawPointer?, CFDictionary?, io_service_t) -> IOReturn)!, Stop Stop: (@escaping (UnsafeMutableRawPointer?) -> IOReturn)!) ``` |
| To | ``` init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!, Release Release: ((UnsafeMutableRawPointer?) -> ULONG)!, version version: UInt16, revision revision: UInt16, Probe Probe: ((UnsafeMutableRawPointer?, CFDictionary?, io_service_t, UnsafeMutablePointer<Int32>?) -> IOReturn)!, Start Start: ((UnsafeMutableRawPointer?, CFDictionary?, io_service_t) -> IOReturn)!, Stop Stop: ((UnsafeMutableRawPointer?) -> IOReturn)!) ``` |

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
