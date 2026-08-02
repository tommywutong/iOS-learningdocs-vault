---
title: macOS 10.12.1 API Diffs
apple_id: TP40017565
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12_1/Swift/CoreServices.html
archived_at: '2026-07-18T02:51:45.381139Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12.1 API Diffs](macOS%2010.12%20to%20macOS%2010.12.1%20API%20Differences.md)


# CoreServices Changes for Swift

### CoreServices

Modified [MDExporterInterfaceStruct [struct]](https://developer.apple.com/documentation/coreservices/mdexporterinterfacestruct)

|  | Declaration |
| --- | --- |
| From | ``` struct MDExporterInterfaceStruct {     var _reserved: UnsafeMutableRawPointer!     var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!     var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!     var Release: ((UnsafeMutableRawPointer?) -> ULONG)!     var ImporterExportData: ((UnsafeMutableRawPointer?, CFDictionary?, CFString?, CFString?) -> DarwinBoolean)!     init()     init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: (@escaping (UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, Release Release: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, ImporterExportData ImporterExportData: (@escaping (UnsafeMutableRawPointer?, CFDictionary?, CFString?, CFString?) -> DarwinBoolean)!) } ``` |
| To | ``` struct MDExporterInterfaceStruct {     var _reserved: UnsafeMutableRawPointer!     var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!     var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!     var Release: ((UnsafeMutableRawPointer?) -> ULONG)!     var ImporterExportData: ((UnsafeMutableRawPointer?, CFDictionary?, CFString?, CFString?) -> DarwinBoolean)!     init()     init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!, Release Release: ((UnsafeMutableRawPointer?) -> ULONG)!, ImporterExportData ImporterExportData: ((UnsafeMutableRawPointer?, CFDictionary?, CFString?, CFString?) -> DarwinBoolean)!) } ``` |

Modified [MDExporterInterfaceStruct.init(_reserved: UnsafeMutableRawPointer!, QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!, Release: ((UnsafeMutableRawPointer?) -> ULONG)!, ImporterExportData: ((UnsafeMutableRawPointer?, CFDictionary?, CFString?, CFString?) -> DarwinBoolean)!)](https://developer.apple.com/documentation/coreservices/mdexporterinterfacestruct/1792091-init)

|  | Declaration |
| --- | --- |
| From | ``` init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: (@escaping (UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, Release Release: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, ImporterExportData ImporterExportData: (@escaping (UnsafeMutableRawPointer?, CFDictionary?, CFString?, CFString?) -> DarwinBoolean)!) ``` |
| To | ``` init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!, Release Release: ((UnsafeMutableRawPointer?) -> ULONG)!, ImporterExportData ImporterExportData: ((UnsafeMutableRawPointer?, CFDictionary?, CFString?, CFString?) -> DarwinBoolean)!) ``` |

Modified [MDImporterBundleWrapperURLInterfaceStruct [struct]](https://developer.apple.com/documentation/coreservices/mdimporterbundlewrapperurlinterfacestruct)

|  | Declaration |
| --- | --- |
| From | ``` struct MDImporterBundleWrapperURLInterfaceStruct {     var _reserved: UnsafeMutableRawPointer!     var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!     var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!     var Release: ((UnsafeMutableRawPointer?) -> ULONG)!     var ImporterImportBundleWrapperURLData: ((UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFURL?) -> DarwinBoolean)!     init()     init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: (@escaping (UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, Release Release: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, ImporterImportBundleWrapperURLData ImporterImportBundleWrapperURLData: (@escaping (UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFURL?) -> DarwinBoolean)!) } ``` |
| To | ``` struct MDImporterBundleWrapperURLInterfaceStruct {     var _reserved: UnsafeMutableRawPointer!     var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!     var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!     var Release: ((UnsafeMutableRawPointer?) -> ULONG)!     var ImporterImportBundleWrapperURLData: ((UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFURL?) -> DarwinBoolean)!     init()     init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!, Release Release: ((UnsafeMutableRawPointer?) -> ULONG)!, ImporterImportBundleWrapperURLData ImporterImportBundleWrapperURLData: ((UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFURL?) -> DarwinBoolean)!) } ``` |

Modified [MDImporterBundleWrapperURLInterfaceStruct.init(_reserved: UnsafeMutableRawPointer!, QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!, Release: ((UnsafeMutableRawPointer?) -> ULONG)!, ImporterImportBundleWrapperURLData: ((UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFURL?) -> DarwinBoolean)!)](https://developer.apple.com/documentation/coreservices/mdimporterbundlewrapperurlinterfacestruct/1792098-init)

|  | Declaration |
| --- | --- |
| From | ``` init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: (@escaping (UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, Release Release: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, ImporterImportBundleWrapperURLData ImporterImportBundleWrapperURLData: (@escaping (UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFURL?) -> DarwinBoolean)!) ``` |
| To | ``` init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!, Release Release: ((UnsafeMutableRawPointer?) -> ULONG)!, ImporterImportBundleWrapperURLData ImporterImportBundleWrapperURLData: ((UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFURL?) -> DarwinBoolean)!) ``` |

Modified [MDImporterInterfaceStruct [struct]](https://developer.apple.com/documentation/coreservices/mdimporterinterfacestruct)

|  | Declaration |
| --- | --- |
| From | ``` struct MDImporterInterfaceStruct {     var _reserved: UnsafeMutableRawPointer!     var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!     var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!     var Release: ((UnsafeMutableRawPointer?) -> ULONG)!     var ImporterImportData: ((UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFString?) -> DarwinBoolean)!     init()     init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: (@escaping (UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, Release Release: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, ImporterImportData ImporterImportData: (@escaping (UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFString?) -> DarwinBoolean)!) } ``` |
| To | ``` struct MDImporterInterfaceStruct {     var _reserved: UnsafeMutableRawPointer!     var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!     var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!     var Release: ((UnsafeMutableRawPointer?) -> ULONG)!     var ImporterImportData: ((UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFString?) -> DarwinBoolean)!     init()     init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!, Release Release: ((UnsafeMutableRawPointer?) -> ULONG)!, ImporterImportData ImporterImportData: ((UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFString?) -> DarwinBoolean)!) } ``` |

Modified [MDImporterInterfaceStruct.init(_reserved: UnsafeMutableRawPointer!, QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!, Release: ((UnsafeMutableRawPointer?) -> ULONG)!, ImporterImportData: ((UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFString?) -> DarwinBoolean)!)](https://developer.apple.com/documentation/coreservices/mdimporterinterfacestruct/1792094-init)

|  | Declaration |
| --- | --- |
| From | ``` init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: (@escaping (UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, Release Release: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, ImporterImportData ImporterImportData: (@escaping (UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFString?) -> DarwinBoolean)!) ``` |
| To | ``` init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!, Release Release: ((UnsafeMutableRawPointer?) -> ULONG)!, ImporterImportData ImporterImportData: ((UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFString?) -> DarwinBoolean)!) ``` |

Modified [MDImporterURLInterfaceStruct [struct]](https://developer.apple.com/documentation/coreservices/mdimporterurlinterfacestruct)

|  | Declaration |
| --- | --- |
| From | ``` struct MDImporterURLInterfaceStruct {     var _reserved: UnsafeMutableRawPointer!     var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!     var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!     var Release: ((UnsafeMutableRawPointer?) -> ULONG)!     var ImporterImportURLData: ((UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFURL?) -> DarwinBoolean)!     init()     init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: (@escaping (UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, Release Release: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, ImporterImportURLData ImporterImportURLData: (@escaping (UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFURL?) -> DarwinBoolean)!) } ``` |
| To | ``` struct MDImporterURLInterfaceStruct {     var _reserved: UnsafeMutableRawPointer!     var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!     var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!     var Release: ((UnsafeMutableRawPointer?) -> ULONG)!     var ImporterImportURLData: ((UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFURL?) -> DarwinBoolean)!     init()     init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!, Release Release: ((UnsafeMutableRawPointer?) -> ULONG)!, ImporterImportURLData ImporterImportURLData: ((UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFURL?) -> DarwinBoolean)!) } ``` |

Modified [MDImporterURLInterfaceStruct.init(_reserved: UnsafeMutableRawPointer!, QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!, Release: ((UnsafeMutableRawPointer?) -> ULONG)!, ImporterImportURLData: ((UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFURL?) -> DarwinBoolean)!)](https://developer.apple.com/documentation/coreservices/mdimporterurlinterfacestruct/1792096-init)

|  | Declaration |
| --- | --- |
| From | ``` init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: (@escaping (UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, Release Release: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, ImporterImportURLData ImporterImportURLData: (@escaping (UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFURL?) -> DarwinBoolean)!) ``` |
| To | ``` init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!, Release Release: ((UnsafeMutableRawPointer?) -> ULONG)!, ImporterImportURLData ImporterImportURLData: ((UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFURL?) -> DarwinBoolean)!) ``` |

Modified [FSEventStreamCreate(_: CFAllocator?, _: CoreServices.FSEventStreamCallback, _: UnsafeMutablePointer<FSEventStreamContext>?, _: CFArray, _: FSEventStreamEventId, _: CFTimeInterval, _: FSEventStreamCreateFlags) -> FSEventStreamRef?](https://developer.apple.com/documentation/coreservices/1443980-fseventstreamcreate)

|  | Declaration |
| --- | --- |
| From | ``` func FSEventStreamCreate(_ allocator: CFAllocator?, _ callback: CoreServices.FSEventStreamCallback, _ context: UnsafeMutablePointer<FSEventStreamContext>?, _ pathsToWatch: CFArray, _ sinceWhen: FSEventStreamEventId, _ latency: CFTimeInterval, _ flags: FSEventStreamCreateFlags) -> FSEventStreamRef? ``` |
| To | ``` func FSEventStreamCreate(_ allocator: CFAllocator?, _ callback: @escaping CoreServices.FSEventStreamCallback, _ context: UnsafeMutablePointer<FSEventStreamContext>?, _ pathsToWatch: CFArray, _ sinceWhen: FSEventStreamEventId, _ latency: CFTimeInterval, _ flags: FSEventStreamCreateFlags) -> FSEventStreamRef? ``` |

Modified [FSEventStreamCreateRelativeToDevice(_: CFAllocator?, _: CoreServices.FSEventStreamCallback, _: UnsafeMutablePointer<FSEventStreamContext>?, _: dev_t, _: CFArray, _: FSEventStreamEventId, _: CFTimeInterval, _: FSEventStreamCreateFlags) -> FSEventStreamRef?](https://developer.apple.com/documentation/coreservices/1447341-fseventstreamcreaterelativetodev)

|  | Declaration |
| --- | --- |
| From | ``` func FSEventStreamCreateRelativeToDevice(_ allocator: CFAllocator?, _ callback: CoreServices.FSEventStreamCallback, _ context: UnsafeMutablePointer<FSEventStreamContext>?, _ deviceToWatch: dev_t, _ pathsToWatchRelativeToDevice: CFArray, _ sinceWhen: FSEventStreamEventId, _ latency: CFTimeInterval, _ flags: FSEventStreamCreateFlags) -> FSEventStreamRef? ``` |
| To | ``` func FSEventStreamCreateRelativeToDevice(_ allocator: CFAllocator?, _ callback: @escaping CoreServices.FSEventStreamCallback, _ context: UnsafeMutablePointer<FSEventStreamContext>?, _ deviceToWatch: dev_t, _ pathsToWatchRelativeToDevice: CFArray, _ sinceWhen: FSEventStreamEventId, _ latency: CFTimeInterval, _ flags: FSEventStreamCreateFlags) -> FSEventStreamRef? ``` |

Modified [MDQuerySetSortComparatorBlock(_: MDQuery!, _: ((UnsafePointer<Unmanaged<CFTypeRef>?>?, UnsafePointer<Unmanaged<CFTypeRef>?>?) -> CFComparisonResult)!)](https://developer.apple.com/documentation/coreservices/1413021-mdquerysetsortcomparatorblock)

|  | Declaration |
| --- | --- |
| From | ``` func MDQuerySetSortComparatorBlock(_ query: MDQuery!, _ comparator: (@escaping (UnsafePointer<Unmanaged<CFTypeRef>?>?, UnsafePointer<Unmanaged<CFTypeRef>?>?) -> CFComparisonResult)!) ``` |
| To | ``` func MDQuerySetSortComparatorBlock(_ query: MDQuery!, _ comparator: ((UnsafePointer<Unmanaged<CFTypeRef>?>?, UnsafePointer<Unmanaged<CFTypeRef>?>?) -> CFComparisonResult)!) ``` |

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
