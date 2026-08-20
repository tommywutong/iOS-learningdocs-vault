---
title: watchOS 3.1 API Diffs
apple_id: TP40017546
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS31APIDiffs/Swift/CoreFoundation.html
archived_at: '2026-07-18T02:58:37.955590Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 3.1 API Diffs](watchOS%203.0%20to%20watchOS%203.1%20API%20Differences.md)


# CoreFoundation Changes for Swift

### CoreFoundation

Modified [CFBinaryHeapCallBacks [struct]](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CFBinaryHeapCallBacks {     var version: CFIndex     var retain: ((CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((CFAllocator?, UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     var compare: ((UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> CFComparisonResult)!     init()     init(version version: CFIndex, retain retain: (@escaping (CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (CFAllocator?, UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!, compare compare: (@escaping (UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> CFComparisonResult)!) } ``` |
| To | ``` struct CFBinaryHeapCallBacks {     var version: CFIndex     var retain: ((CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((CFAllocator?, UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     var compare: ((UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> CFComparisonResult)!     init()     init(version version: CFIndex, retain retain: ((CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: ((CFAllocator?, UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!, compare compare: ((UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> CFComparisonResult)!) } ``` |

Modified [CFBinaryHeapCallBacks.init(version: CFIndex, retain: ((CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer?)!, release: ((CFAllocator?, UnsafeRawPointer?) -> Swift.Void)!, copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!, compare: ((UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> CFComparisonResult)!)](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcallbacks/1780514-init)

|  | Declaration |
| --- | --- |
| From | ``` init(version version: CFIndex, retain retain: (@escaping (CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (CFAllocator?, UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!, compare compare: (@escaping (UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> CFComparisonResult)!) ``` |
| To | ``` init(version version: CFIndex, retain retain: ((CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: ((CFAllocator?, UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!, compare compare: ((UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> CFComparisonResult)!) ``` |

Modified [CFBinaryHeapCompareContext [struct]](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcomparecontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFBinaryHeapCompareContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!) } ``` |
| To | ``` struct CFBinaryHeapCompareContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: ((UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!) } ``` |

Modified [CFBinaryHeapCompareContext.init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release: ((UnsafeRawPointer?) -> Swift.Void)!, copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!)](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcomparecontext/1780495-init)

|  | Declaration |
| --- | --- |
| From | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!) ``` |
| To | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: ((UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!) ``` |

Modified [CFFileDescriptorContext [struct]](https://developer.apple.com/documentation/corefoundation/cffiledescriptorcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFFileDescriptorContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!     var release: ((UnsafeMutableRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!, release release: (@escaping (UnsafeMutableRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!) } ``` |
| To | ``` struct CFFileDescriptorContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!     var release: ((UnsafeMutableRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: ((UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!, release release: ((UnsafeMutableRawPointer?) -> Swift.Void)!, copyDescription copyDescription: ((UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!) } ``` |

Modified [CFFileDescriptorContext.init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ((UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!, release: ((UnsafeMutableRawPointer?) -> Swift.Void)!, copyDescription: ((UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!)](https://developer.apple.com/documentation/corefoundation/cffiledescriptorcontext/1780513-init)

|  | Declaration |
| --- | --- |
| From | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!, release release: (@escaping (UnsafeMutableRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!) ``` |
| To | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: ((UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!, release release: ((UnsafeMutableRawPointer?) -> Swift.Void)!, copyDescription copyDescription: ((UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!) ``` |

Modified [CFMachPortContext [struct]](https://developer.apple.com/documentation/corefoundation/cfmachportcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFMachPortContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!) } ``` |
| To | ``` struct CFMachPortContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: ((UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!) } ``` |

Modified [CFMachPortContext.init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release: ((UnsafeRawPointer?) -> Swift.Void)!, copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!)](https://developer.apple.com/documentation/corefoundation/cfmachportcontext/1780503-init)

|  | Declaration |
| --- | --- |
| From | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!) ``` |
| To | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: ((UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!) ``` |

Modified [CFMessagePortContext [struct]](https://developer.apple.com/documentation/corefoundation/cfmessageportcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFMessagePortContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!) } ``` |
| To | ``` struct CFMessagePortContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: ((UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!) } ``` |

Modified [CFMessagePortContext.init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release: ((UnsafeRawPointer?) -> Swift.Void)!, copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!)](https://developer.apple.com/documentation/corefoundation/cfmessageportcontext/1780493-init)

|  | Declaration |
| --- | --- |
| From | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!) ``` |
| To | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: ((UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!) ``` |

Modified [CFRunLoopObserverContext [struct]](https://developer.apple.com/documentation/corefoundation/cfrunloopobservercontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFRunLoopObserverContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!) } ``` |
| To | ``` struct CFRunLoopObserverContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: ((UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!) } ``` |

Modified [CFRunLoopObserverContext.init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release: ((UnsafeRawPointer?) -> Swift.Void)!, copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!)](https://developer.apple.com/documentation/corefoundation/cfrunloopobservercontext/1780510-init)

|  | Declaration |
| --- | --- |
| From | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!) ``` |
| To | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: ((UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!) ``` |

Modified [CFRunLoopSourceContext [struct]](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFRunLoopSourceContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     var equal: ((UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!     var hash: ((UnsafeRawPointer?) -> CFHashCode)!     var schedule: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Swift.Void)!     var cancel: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Swift.Void)!     var perform: ((UnsafeMutableRawPointer?) -> Swift.Void)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!, equal equal: (@escaping (UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!, hash hash: (@escaping (UnsafeRawPointer?) -> CFHashCode)!, schedule schedule: (@escaping (UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Swift.Void)!, cancel cancel: (@escaping (UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Swift.Void)!, perform perform: (@escaping (UnsafeMutableRawPointer?) -> Swift.Void)!) } ``` |
| To | ``` struct CFRunLoopSourceContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     var equal: ((UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!     var hash: ((UnsafeRawPointer?) -> CFHashCode)!     var schedule: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Swift.Void)!     var cancel: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Swift.Void)!     var perform: ((UnsafeMutableRawPointer?) -> Swift.Void)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: ((UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!, equal equal: ((UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!, hash hash: ((UnsafeRawPointer?) -> CFHashCode)!, schedule schedule: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Swift.Void)!, cancel cancel: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Swift.Void)!, perform perform: ((UnsafeMutableRawPointer?) -> Swift.Void)!) } ``` |

Modified [CFRunLoopSourceContext.init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release: ((UnsafeRawPointer?) -> Swift.Void)!, copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!, equal: ((UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!, hash: ((UnsafeRawPointer?) -> CFHashCode)!, schedule: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Swift.Void)!, cancel: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Swift.Void)!, perform: ((UnsafeMutableRawPointer?) -> Swift.Void)!)](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext/1780501-init)

|  | Declaration |
| --- | --- |
| From | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!, equal equal: (@escaping (UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!, hash hash: (@escaping (UnsafeRawPointer?) -> CFHashCode)!, schedule schedule: (@escaping (UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Swift.Void)!, cancel cancel: (@escaping (UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Swift.Void)!, perform perform: (@escaping (UnsafeMutableRawPointer?) -> Swift.Void)!) ``` |
| To | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: ((UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!, equal equal: ((UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!, hash hash: ((UnsafeRawPointer?) -> CFHashCode)!, schedule schedule: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Swift.Void)!, cancel cancel: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Swift.Void)!, perform perform: ((UnsafeMutableRawPointer?) -> Swift.Void)!) ``` |

Modified [CFRunLoopSourceContext1 [struct]](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1)

|  | Declaration |
| --- | --- |
| From | ``` struct CFRunLoopSourceContext1 {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     var equal: ((UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!     var hash: ((UnsafeRawPointer?) -> CFHashCode)!     var getPort: ((UnsafeMutableRawPointer?) -> mach_port_t)!     var perform: ((UnsafeMutableRawPointer?, CFIndex, CFAllocator?, UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!, equal equal: (@escaping (UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!, hash hash: (@escaping (UnsafeRawPointer?) -> CFHashCode)!, getPort getPort: (@escaping (UnsafeMutableRawPointer?) -> mach_port_t)!, perform perform: (@escaping (UnsafeMutableRawPointer?, CFIndex, CFAllocator?, UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!) } ``` |
| To | ``` struct CFRunLoopSourceContext1 {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     var equal: ((UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!     var hash: ((UnsafeRawPointer?) -> CFHashCode)!     var getPort: ((UnsafeMutableRawPointer?) -> mach_port_t)!     var perform: ((UnsafeMutableRawPointer?, CFIndex, CFAllocator?, UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: ((UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!, equal equal: ((UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!, hash hash: ((UnsafeRawPointer?) -> CFHashCode)!, getPort getPort: ((UnsafeMutableRawPointer?) -> mach_port_t)!, perform perform: ((UnsafeMutableRawPointer?, CFIndex, CFAllocator?, UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!) } ``` |

Modified [CFRunLoopSourceContext1.init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release: ((UnsafeRawPointer?) -> Swift.Void)!, copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!, equal: ((UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!, hash: ((UnsafeRawPointer?) -> CFHashCode)!, getPort: ((UnsafeMutableRawPointer?) -> mach_port_t)!, perform: ((UnsafeMutableRawPointer?, CFIndex, CFAllocator?, UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!)](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1/1780506-init)

|  | Declaration |
| --- | --- |
| From | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!, equal equal: (@escaping (UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!, hash hash: (@escaping (UnsafeRawPointer?) -> CFHashCode)!, getPort getPort: (@escaping (UnsafeMutableRawPointer?) -> mach_port_t)!, perform perform: (@escaping (UnsafeMutableRawPointer?, CFIndex, CFAllocator?, UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!) ``` |
| To | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: ((UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!, equal equal: ((UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!, hash hash: ((UnsafeRawPointer?) -> CFHashCode)!, getPort getPort: ((UnsafeMutableRawPointer?) -> mach_port_t)!, perform perform: ((UnsafeMutableRawPointer?, CFIndex, CFAllocator?, UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!) ``` |

Modified [CFRunLoopTimerContext [struct]](https://developer.apple.com/documentation/corefoundation/cfrunlooptimercontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFRunLoopTimerContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!) } ``` |
| To | ``` struct CFRunLoopTimerContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: ((UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!) } ``` |

Modified [CFRunLoopTimerContext.init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release: ((UnsafeRawPointer?) -> Swift.Void)!, copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!)](https://developer.apple.com/documentation/corefoundation/cfrunlooptimercontext/1780492-init)

|  | Declaration |
| --- | --- |
| From | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!) ``` |
| To | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: ((UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!) ``` |

Modified [CFSocketContext [struct]](https://developer.apple.com/documentation/corefoundation/cfsocketcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFSocketContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!) } ``` |
| To | ``` struct CFSocketContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: ((UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!) } ``` |

Modified [CFSocketContext.init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release: ((UnsafeRawPointer?) -> Swift.Void)!, copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!)](https://developer.apple.com/documentation/corefoundation/cfsocketcontext/1780502-init)

|  | Declaration |
| --- | --- |
| From | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!) ``` |
| To | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: ((UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!) ``` |

Modified [CFStreamClientContext [struct]](https://developer.apple.com/documentation/corefoundation/cfstreamclientcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFStreamClientContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!     var release: ((UnsafeMutableRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!, release release: (@escaping (UnsafeMutableRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!) } ``` |
| To | ``` struct CFStreamClientContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!     var release: ((UnsafeMutableRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: ((UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!, release release: ((UnsafeMutableRawPointer?) -> Swift.Void)!, copyDescription copyDescription: ((UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!) } ``` |

Modified [CFStreamClientContext.init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ((UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!, release: ((UnsafeMutableRawPointer?) -> Swift.Void)!, copyDescription: ((UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!)](https://developer.apple.com/documentation/corefoundation/cfstreamclientcontext/1780497-init)

|  | Declaration |
| --- | --- |
| From | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!, release release: (@escaping (UnsafeMutableRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!) ``` |
| To | ``` init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: ((UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!, release release: ((UnsafeMutableRawPointer?) -> Swift.Void)!, copyDescription copyDescription: ((UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!) ``` |

Modified [CFRunLoopObserverCreateWithHandler(_: CFAllocator!, _: CFOptionFlags, _: Bool, _: CFIndex, _: ((CFRunLoopObserver?, CFRunLoopActivity) -> Swift.Void)!) -> CFRunLoopObserver!](https://developer.apple.com/documentation/corefoundation/1542816-cfrunloopobservercreatewithhandl)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopObserverCreateWithHandler(_ allocator: CFAllocator!, _ activities: CFOptionFlags, _ repeats: Bool, _ order: CFIndex, _ block: (@escaping (CFRunLoopObserver?, CFRunLoopActivity) -> Swift.Void)!) -> CFRunLoopObserver! ``` |
| To | ``` func CFRunLoopObserverCreateWithHandler(_ allocator: CFAllocator!, _ activities: CFOptionFlags, _ repeats: Bool, _ order: CFIndex, _ block: ((CFRunLoopObserver?, CFRunLoopActivity) -> Swift.Void)!) -> CFRunLoopObserver! ``` |

Modified [CFRunLoopPerformBlock(_: CFRunLoop!, _: CFTypeRef!, _: (() -> Swift.Void)!)](https://developer.apple.com/documentation/corefoundation/1542985-cfrunloopperformblock)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopPerformBlock(_ rl: CFRunLoop!, _ mode: CFTypeRef!, _ block: (@escaping () -> Swift.Void)!) ``` |
| To | ``` func CFRunLoopPerformBlock(_ rl: CFRunLoop!, _ mode: CFTypeRef!, _ block: (() -> Swift.Void)!) ``` |

Modified [CFRunLoopTimerCreateWithHandler(_: CFAllocator!, _: CFAbsoluteTime, _: CFTimeInterval, _: CFOptionFlags, _: CFIndex, _: ((CFRunLoopTimer?) -> Swift.Void)!) -> CFRunLoopTimer!](https://developer.apple.com/documentation/corefoundation/1542555-cfrunlooptimercreatewithhandler)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopTimerCreateWithHandler(_ allocator: CFAllocator!, _ fireDate: CFAbsoluteTime, _ interval: CFTimeInterval, _ flags: CFOptionFlags, _ order: CFIndex, _ block: (@escaping (CFRunLoopTimer?) -> Swift.Void)!) -> CFRunLoopTimer! ``` |
| To | ``` func CFRunLoopTimerCreateWithHandler(_ allocator: CFAllocator!, _ fireDate: CFAbsoluteTime, _ interval: CFTimeInterval, _ flags: CFOptionFlags, _ order: CFIndex, _ block: ((CFRunLoopTimer?) -> Swift.Void)!) -> CFRunLoopTimer! ``` |

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
