---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/CoreFoundation.html
archived_at: '2026-07-18T02:56:22.380701Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# CoreFoundation Changes

## CoreFoundation

Removed CFURLBookmarkCreationOptions.PreferFileIDResolutionMaskRemoved CFURLBookmarkCreationOptions.SecurityScopeAllowOnlyReadAccessRemoved CFURLBookmarkCreationOptions.WithSecurityScopeRemoved CFURLBookmarkResolutionOptions.CFURLBookmarkResolutionWithSecurityScopeRemoved CFURLPathStyle.CFURLHFSPathStyleRemoved CF_USE_OSBYTEORDER_HAdded CFAllocatorContext.init()Added CFAllocatorContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFAllocatorRetainCallBack, release: CFAllocatorReleaseCallBack, copyDescription: CFAllocatorCopyDescriptionCallBack, allocate: CFAllocatorAllocateCallBack, reallocate: CFAllocatorReallocateCallBack, deallocate: CFAllocatorDeallocateCallBack, preferredSize: CFAllocatorPreferredSizeCallBack)Added CFArrayCallBacks.init()Added CFArrayCallBacks.init(version: CFIndex, retain: CFArrayRetainCallBack, release: CFArrayReleaseCallBack, copyDescription: CFArrayCopyDescriptionCallBack, equal: CFArrayEqualCallBack)Added CFBagCallBacks.init()Added CFBagCallBacks.init(version: CFIndex, retain: CFBagRetainCallBack, release: CFBagReleaseCallBack, copyDescription: CFBagCopyDescriptionCallBack, equal: CFBagEqualCallBack, hash: CFBagHashCallBack)Added CFBinaryHeapCallBacks.init()Added CFBinaryHeapCallBacks.init(version: CFIndex, retain: CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>, compare: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> CFComparisonResult)>)Added CFBinaryHeapCompareContext.init()Added CFBinaryHeapCompareContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Added CFDictionaryKeyCallBacks.init()Added CFDictionaryKeyCallBacks.init(version: CFIndex, retain: CFDictionaryRetainCallBack, release: CFDictionaryReleaseCallBack, copyDescription: CFDictionaryCopyDescriptionCallBack, equal: CFDictionaryEqualCallBack, hash: CFDictionaryHashCallBack)Added CFDictionaryValueCallBacks.init()Added CFDictionaryValueCallBacks.init(version: CFIndex, retain: CFDictionaryRetainCallBack, release: CFDictionaryReleaseCallBack, copyDescription: CFDictionaryCopyDescriptionCallBack, equal: CFDictionaryEqualCallBack)Added CFFileDescriptorContext.init()Added CFFileDescriptorContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>, release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)>)Added CFGregorianDate.init()Added CFGregorianDate.init(year: Int32, month: Int8, day: Int8, hour: Int8, minute: Int8, second: Double)Added CFGregorianUnits.init()Added CFGregorianUnits.init(years: Int32, months: Int32, days: Int32, hours: Int32, minutes: Int32, seconds: Double)Added CFMachPortContext.init()Added CFMachPortContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Added CFMessagePortContext.init()Added CFMessagePortContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Added CFRange.init()Added CFRange.init(location: CFIndex, length: CFIndex)Added CFRunLoopObserverContext.init()Added CFRunLoopObserverContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Added CFRunLoopSourceContext.init()Added CFRunLoopSourceContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>, equal: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)>, hash: CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)>, schedule: CFunctionPointer<((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)>, cancel: CFunctionPointer<((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)>, perform: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>)Added CFRunLoopSourceContext1.init()Added CFRunLoopSourceContext1.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>, equal: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)>, hash: CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)>, getPort: CFunctionPointer<((UnsafeMutablePointer<Void>) -> mach_port_t)>, perform: CFunctionPointer<((UnsafeMutablePointer<Void>, CFIndex, CFAllocator!, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>)Added CFRunLoopTimerContext.init()Added CFRunLoopTimerContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Added CFSetCallBacks.init()Added CFSetCallBacks.init(version: CFIndex, retain: CFSetRetainCallBack, release: CFSetReleaseCallBack, copyDescription: CFSetCopyDescriptionCallBack, equal: CFSetEqualCallBack, hash: CFSetHashCallBack)Added CFSocketContext.init()Added CFSocketContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Added CFSocketSignature.init()Added CFSocketSignature.init(protocolFamily: Int32, socketType: Int32, protocol: Int32, address: Unmanaged<CFData>!)Added CFStreamClientContext.init()Added CFStreamClientContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>, release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)>)Added CFStreamError.init()Added CFStreamError.init(domain: CFIndex, error: Int32)Added CFStringInlineBuffer.init()Added CFStringInlineBuffer.init(buffer: (UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar), theString: Unmanaged<CFString>!, directUniCharBuffer: UnsafePointer<UniChar>, directCStringBuffer: UnsafePointer<Int8>, rangeToBuffer: CFRange, bufferedRangeStart: CFIndex, bufferedRangeEnd: CFIndex)Added CFSwappedFloat32.init()Added CFSwappedFloat32.init(v: UInt32)Added CFSwappedFloat64.init()Added CFSwappedFloat64.init(v: UInt64)Added CFTreeContext.init()Added CFTreeContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFTreeRetainCallBack, release: CFTreeReleaseCallBack, copyDescription: CFTreeCopyDescriptionCallBack)Added CFUUIDBytes.init()Added CFUUIDBytes.init(byte0: UInt8, byte1: UInt8, byte2: UInt8, byte3: UInt8, byte4: UInt8, byte5: UInt8, byte6: UInt8, byte7: UInt8, byte8: UInt8, byte9: UInt8, byte10: UInt8, byte11: UInt8, byte12: UInt8, byte13: UInt8, byte14: UInt8, byte15: UInt8)Modified CFAllocatorContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFAllocatorContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack     var release: CFAllocatorReleaseCallBack     var copyDescription: CFAllocatorCopyDescriptionCallBack     var allocate: CFAllocatorAllocateCallBack     var reallocate: CFAllocatorReallocateCallBack     var deallocate: CFAllocatorDeallocateCallBack     var preferredSize: CFAllocatorPreferredSizeCallBack } ``` |
| To | ``` struct CFAllocatorContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack     var release: CFAllocatorReleaseCallBack     var copyDescription: CFAllocatorCopyDescriptionCallBack     var allocate: CFAllocatorAllocateCallBack     var reallocate: CFAllocatorReallocateCallBack     var deallocate: CFAllocatorDeallocateCallBack     var preferredSize: CFAllocatorPreferredSizeCallBack     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFAllocatorRetainCallBack, release release: CFAllocatorReleaseCallBack, copyDescription copyDescription: CFAllocatorCopyDescriptionCallBack, allocate allocate: CFAllocatorAllocateCallBack, reallocate reallocate: CFAllocatorReallocateCallBack, deallocate deallocate: CFAllocatorDeallocateCallBack, preferredSize preferredSize: CFAllocatorPreferredSizeCallBack) } ``` |

Modified CFArrayCallBacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFArrayCallBacks {     var version: CFIndex     var retain: CFArrayRetainCallBack     var release: CFArrayReleaseCallBack     var copyDescription: CFArrayCopyDescriptionCallBack     var equal: CFArrayEqualCallBack } ``` |
| To | ``` struct CFArrayCallBacks {     var version: CFIndex     var retain: CFArrayRetainCallBack     var release: CFArrayReleaseCallBack     var copyDescription: CFArrayCopyDescriptionCallBack     var equal: CFArrayEqualCallBack     init()     init(version version: CFIndex, retain retain: CFArrayRetainCallBack, release release: CFArrayReleaseCallBack, copyDescription copyDescription: CFArrayCopyDescriptionCallBack, equal equal: CFArrayEqualCallBack) } ``` |

Modified CFBagCallBacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFBagCallBacks {     var version: CFIndex     var retain: CFBagRetainCallBack     var release: CFBagReleaseCallBack     var copyDescription: CFBagCopyDescriptionCallBack     var equal: CFBagEqualCallBack     var hash: CFBagHashCallBack } ``` |
| To | ``` struct CFBagCallBacks {     var version: CFIndex     var retain: CFBagRetainCallBack     var release: CFBagReleaseCallBack     var copyDescription: CFBagCopyDescriptionCallBack     var equal: CFBagEqualCallBack     var hash: CFBagHashCallBack     init()     init(version version: CFIndex, retain retain: CFBagRetainCallBack, release release: CFBagReleaseCallBack, copyDescription copyDescription: CFBagCopyDescriptionCallBack, equal equal: CFBagEqualCallBack, hash hash: CFBagHashCallBack) } ``` |

Modified CFBinaryHeapCallBacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFBinaryHeapCallBacks {     var version: CFIndex     var retain: CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     var compare: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> CFComparisonResult)> } ``` |
| To | ``` struct CFBinaryHeapCallBacks {     var version: CFIndex     var retain: CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     var compare: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> CFComparisonResult)>     init()     init(version version: CFIndex, retain retain: CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>, compare compare: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> CFComparisonResult)>) } ``` |

Modified CFBinaryHeapCompareContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFBinaryHeapCompareContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> } ``` |
| To | ``` struct CFBinaryHeapCompareContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |

Modified CFCalendarUnit.Quarter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFCalendarUnit.Week

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified CFCalendarUnit.WeekOfMonth

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CFCalendarUnit.WeekOfYear

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CFCalendarUnit.YearForWeekOfYear

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CFCharacterSetPredefinedSet.Newline

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFDictionaryKeyCallBacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFDictionaryKeyCallBacks {     var version: CFIndex     var retain: CFDictionaryRetainCallBack     var release: CFDictionaryReleaseCallBack     var copyDescription: CFDictionaryCopyDescriptionCallBack     var equal: CFDictionaryEqualCallBack     var hash: CFDictionaryHashCallBack } ``` |
| To | ``` struct CFDictionaryKeyCallBacks {     var version: CFIndex     var retain: CFDictionaryRetainCallBack     var release: CFDictionaryReleaseCallBack     var copyDescription: CFDictionaryCopyDescriptionCallBack     var equal: CFDictionaryEqualCallBack     var hash: CFDictionaryHashCallBack     init()     init(version version: CFIndex, retain retain: CFDictionaryRetainCallBack, release release: CFDictionaryReleaseCallBack, copyDescription copyDescription: CFDictionaryCopyDescriptionCallBack, equal equal: CFDictionaryEqualCallBack, hash hash: CFDictionaryHashCallBack) } ``` |

Modified CFDictionaryValueCallBacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFDictionaryValueCallBacks {     var version: CFIndex     var retain: CFDictionaryRetainCallBack     var release: CFDictionaryReleaseCallBack     var copyDescription: CFDictionaryCopyDescriptionCallBack     var equal: CFDictionaryEqualCallBack } ``` |
| To | ``` struct CFDictionaryValueCallBacks {     var version: CFIndex     var retain: CFDictionaryRetainCallBack     var release: CFDictionaryReleaseCallBack     var copyDescription: CFDictionaryCopyDescriptionCallBack     var equal: CFDictionaryEqualCallBack     init()     init(version version: CFIndex, retain retain: CFDictionaryRetainCallBack, release release: CFDictionaryReleaseCallBack, copyDescription copyDescription: CFDictionaryCopyDescriptionCallBack, equal equal: CFDictionaryEqualCallBack) } ``` |

Modified CFFileDescriptorContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFFileDescriptorContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>     var release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)> } ``` |
| To | ``` struct CFFileDescriptorContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>     var release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>, release release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |

Modified CFGregorianDate [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFGregorianDate {     var year: Int32     var month: Int8     var day: Int8     var hour: Int8     var minute: Int8     var second: Double } ``` |
| To | ``` struct CFGregorianDate {     var year: Int32     var month: Int8     var day: Int8     var hour: Int8     var minute: Int8     var second: Double     init()     init(year year: Int32, month month: Int8, day day: Int8, hour hour: Int8, minute minute: Int8, second second: Double) } ``` |

Modified CFGregorianUnitFlags.AllUnits

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified CFGregorianUnitFlags.UnitsDays

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified CFGregorianUnitFlags.UnitsHours

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified CFGregorianUnitFlags.UnitsMinutes

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified CFGregorianUnitFlags.UnitsMonths

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified CFGregorianUnitFlags.UnitsSeconds

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified CFGregorianUnitFlags.UnitsYears

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified CFGregorianUnits [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFGregorianUnits {     var years: Int32     var months: Int32     var days: Int32     var hours: Int32     var minutes: Int32     var seconds: Double } ``` |
| To | ``` struct CFGregorianUnits {     var years: Int32     var months: Int32     var days: Int32     var hours: Int32     var minutes: Int32     var seconds: Double     init()     init(years years: Int32, months months: Int32, days days: Int32, hours hours: Int32, minutes minutes: Int32, seconds seconds: Double) } ``` |

Modified CFMachPortContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFMachPortContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> } ``` |
| To | ``` struct CFMachPortContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |

Modified CFMessagePortContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFMessagePortContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> } ``` |
| To | ``` struct CFMessagePortContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |

Modified CFNumberType.CGFloatType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNumberType.NSIntegerType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFRange [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFRange {     var location: CFIndex     var length: CFIndex } ``` |
| To | ``` struct CFRange {     var location: CFIndex     var length: CFIndex     init()     init(location location: CFIndex, length length: CFIndex) } ``` |

Modified CFRunLoopObserverContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFRunLoopObserverContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> } ``` |
| To | ``` struct CFRunLoopObserverContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |

Modified CFRunLoopSourceContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFRunLoopSourceContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     var equal: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)>     var hash: CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)>     var schedule: CFunctionPointer<((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)>     var cancel: CFunctionPointer<((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)>     var perform: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> } ``` |
| To | ``` struct CFRunLoopSourceContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     var equal: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)>     var hash: CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)>     var schedule: CFunctionPointer<((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)>     var cancel: CFunctionPointer<((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)>     var perform: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>, equal equal: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)>, hash hash: CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)>, schedule schedule: CFunctionPointer<((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)>, cancel cancel: CFunctionPointer<((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)>, perform perform: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>) } ``` |

Modified CFRunLoopSourceContext1 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFRunLoopSourceContext1 {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     var equal: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)>     var hash: CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)>     var getPort: CFunctionPointer<((UnsafeMutablePointer<Void>) -> mach_port_t)>     var perform: CFunctionPointer<((UnsafeMutablePointer<Void>, CFIndex, CFAllocator!, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)> } ``` |
| To | ``` struct CFRunLoopSourceContext1 {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     var equal: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)>     var hash: CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)>     var getPort: CFunctionPointer<((UnsafeMutablePointer<Void>) -> mach_port_t)>     var perform: CFunctionPointer<((UnsafeMutablePointer<Void>, CFIndex, CFAllocator!, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>, equal equal: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)>, hash hash: CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)>, getPort getPort: CFunctionPointer<((UnsafeMutablePointer<Void>) -> mach_port_t)>, perform perform: CFunctionPointer<((UnsafeMutablePointer<Void>, CFIndex, CFAllocator!, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>) } ``` |

Modified CFRunLoopTimerContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFRunLoopTimerContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> } ``` |
| To | ``` struct CFRunLoopTimerContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |

Modified CFSetCallBacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFSetCallBacks {     var version: CFIndex     var retain: CFSetRetainCallBack     var release: CFSetReleaseCallBack     var copyDescription: CFSetCopyDescriptionCallBack     var equal: CFSetEqualCallBack     var hash: CFSetHashCallBack } ``` |
| To | ``` struct CFSetCallBacks {     var version: CFIndex     var retain: CFSetRetainCallBack     var release: CFSetReleaseCallBack     var copyDescription: CFSetCopyDescriptionCallBack     var equal: CFSetEqualCallBack     var hash: CFSetHashCallBack     init()     init(version version: CFIndex, retain retain: CFSetRetainCallBack, release release: CFSetReleaseCallBack, copyDescription copyDescription: CFSetCopyDescriptionCallBack, equal equal: CFSetEqualCallBack, hash hash: CFSetHashCallBack) } ``` |

Modified CFSocketContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFSocketContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> } ``` |
| To | ``` struct CFSocketContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |

Modified CFSocketSignature [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFSocketSignature {     var protocolFamily: Int32     var socketType: Int32     var `protocol`: Int32     var address: Unmanaged<CFData>! } ``` |
| To | ``` struct CFSocketSignature {     var protocolFamily: Int32     var socketType: Int32     var `protocol`: Int32     var address: Unmanaged<CFData>!     init()     init(protocolFamily protocolFamily: Int32, socketType socketType: Int32, `protocol` `protocol`: Int32, address address: Unmanaged<CFData>!) } ``` |

Modified CFStreamClientContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFStreamClientContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>     var release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)> } ``` |
| To | ``` struct CFStreamClientContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>     var release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>, release release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |

Modified CFStreamError [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFStreamError {     var domain: CFIndex     var error: Int32 } ``` |
| To | ``` struct CFStreamError {     var domain: CFIndex     var error: Int32     init()     init(domain domain: CFIndex, error error: Int32) } ``` |

Modified CFStringCompareFlags.CompareDiacriticInsensitive

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFStringCompareFlags.CompareForcedOrdering

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFStringCompareFlags.CompareWidthInsensitive

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFStringEncodings.ShiftJIS_X0213

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFStringEncodings.UTF7

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFStringEncodings.UTF7_IMAP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFStringInlineBuffer [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFStringInlineBuffer {     var buffer: (UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar)     var theString: Unmanaged<CFString>!     var directUniCharBuffer: UnsafePointer<UniChar>     var directCStringBuffer: UnsafePointer<Int8>     var rangeToBuffer: CFRange     var bufferedRangeStart: CFIndex     var bufferedRangeEnd: CFIndex } ``` |
| To | ``` struct CFStringInlineBuffer {     var buffer: (UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar)     var theString: Unmanaged<CFString>!     var directUniCharBuffer: UnsafePointer<UniChar>     var directCStringBuffer: UnsafePointer<Int8>     var rangeToBuffer: CFRange     var bufferedRangeStart: CFIndex     var bufferedRangeEnd: CFIndex     init()     init(buffer buffer: (UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar), theString theString: Unmanaged<CFString>!, directUniCharBuffer directUniCharBuffer: UnsafePointer<UniChar>, directCStringBuffer directCStringBuffer: UnsafePointer<Int8>, rangeToBuffer rangeToBuffer: CFRange, bufferedRangeStart bufferedRangeStart: CFIndex, bufferedRangeEnd bufferedRangeEnd: CFIndex) } ``` |

Modified CFSwappedFloat32 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFSwappedFloat32 {     var v: UInt32 } ``` |
| To | ``` struct CFSwappedFloat32 {     var v: UInt32     init()     init(v v: UInt32) } ``` |

Modified CFSwappedFloat64 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFSwappedFloat64 {     var v: UInt64 } ``` |
| To | ``` struct CFSwappedFloat64 {     var v: UInt64     init()     init(v v: UInt64) } ``` |

Modified CFTreeContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFTreeContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFTreeRetainCallBack     var release: CFTreeReleaseCallBack     var copyDescription: CFTreeCopyDescriptionCallBack } ``` |
| To | ``` struct CFTreeContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFTreeRetainCallBack     var release: CFTreeReleaseCallBack     var copyDescription: CFTreeCopyDescriptionCallBack     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFTreeRetainCallBack, release release: CFTreeReleaseCallBack, copyDescription copyDescription: CFTreeCopyDescriptionCallBack) } ``` |

Modified CFUUIDBytes [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFUUIDBytes {     var byte0: UInt8     var byte1: UInt8     var byte2: UInt8     var byte3: UInt8     var byte4: UInt8     var byte5: UInt8     var byte6: UInt8     var byte7: UInt8     var byte8: UInt8     var byte9: UInt8     var byte10: UInt8     var byte11: UInt8     var byte12: UInt8     var byte13: UInt8     var byte14: UInt8     var byte15: UInt8 } ``` |
| To | ``` struct CFUUIDBytes {     var byte0: UInt8     var byte1: UInt8     var byte2: UInt8     var byte3: UInt8     var byte4: UInt8     var byte5: UInt8     var byte6: UInt8     var byte7: UInt8     var byte8: UInt8     var byte9: UInt8     var byte10: UInt8     var byte11: UInt8     var byte12: UInt8     var byte13: UInt8     var byte14: UInt8     var byte15: UInt8     init()     init(byte0 byte0: UInt8, byte1 byte1: UInt8, byte2 byte2: UInt8, byte3 byte3: UInt8, byte4 byte4: UInt8, byte5 byte5: UInt8, byte6 byte6: UInt8, byte7 byte7: UInt8, byte8 byte8: UInt8, byte9 byte9: UInt8, byte10 byte10: UInt8, byte11 byte11: UInt8, byte12 byte12: UInt8, byte13 byte13: UInt8, byte14 byte14: UInt8, byte15 byte15: UInt8) } ``` |

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
