---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/CoreFoundation.html
archived_at: '2026-07-18T02:52:10.874091Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# CoreFoundation Changes

## CoreFoundation

Removed CFCalendarUnit.valueRemoved CFDataSearchFlags.valueRemoved CFFileSecurityClearOptions.valueRemoved CFGregorianUnitFlags.valueRemoved CFNumberFormatterOptionFlags.valueRemoved CFPropertyListMutabilityOptions.valueRemoved CFRunLoopActivity.valueRemoved CFSocketCallBackType.valueRemoved CFStreamEventType.valueRemoved CFStringCompareFlags.valueRemoved CFStringTokenizerTokenType.valueRemoved CFURLBookmarkCreationOptions.PreferFileIDResolutionMaskRemoved CFURLBookmarkCreationOptions.valueRemoved CFURLBookmarkResolutionOptions.valueRemoved CFURLEnumeratorOptions.valueRemoved CFURLPathStyle.CFURLHFSPathStyleRemoved CFXMLParserOptions.valueRemoved CFXMLParserStatusCode.valueRemoved CF_USE_OSBYTEORDER_HAdded CFAllocatorContext.init()Added CFAllocatorContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFAllocatorRetainCallBack, release: CFAllocatorReleaseCallBack, copyDescription: CFAllocatorCopyDescriptionCallBack, allocate: CFAllocatorAllocateCallBack, reallocate: CFAllocatorReallocateCallBack, deallocate: CFAllocatorDeallocateCallBack, preferredSize: CFAllocatorPreferredSizeCallBack)Added CFArrayCallBacks.init()Added CFArrayCallBacks.init(version: CFIndex, retain: CFArrayRetainCallBack, release: CFArrayReleaseCallBack, copyDescription: CFArrayCopyDescriptionCallBack, equal: CFArrayEqualCallBack)Added CFBagCallBacks.init()Added CFBagCallBacks.init(version: CFIndex, retain: CFBagRetainCallBack, release: CFBagReleaseCallBack, copyDescription: CFBagCopyDescriptionCallBack, equal: CFBagEqualCallBack, hash: CFBagHashCallBack)Added CFBinaryHeapCallBacks.init()Added CFBinaryHeapCallBacks.init(version: CFIndex, retain: CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>, compare: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> CFComparisonResult)>)Added CFBinaryHeapCompareContext.init()Added CFBinaryHeapCompareContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Added CFCalendarUnit.init(rawValue: CFOptionFlags)Added CFDataSearchFlags.init(rawValue: CFOptionFlags)Added CFDictionaryKeyCallBacks.init()Added CFDictionaryKeyCallBacks.init(version: CFIndex, retain: CFDictionaryRetainCallBack, release: CFDictionaryReleaseCallBack, copyDescription: CFDictionaryCopyDescriptionCallBack, equal: CFDictionaryEqualCallBack, hash: CFDictionaryHashCallBack)Added CFDictionaryValueCallBacks.init()Added CFDictionaryValueCallBacks.init(version: CFIndex, retain: CFDictionaryRetainCallBack, release: CFDictionaryReleaseCallBack, copyDescription: CFDictionaryCopyDescriptionCallBack, equal: CFDictionaryEqualCallBack)Added CFFileDescriptorContext.init()Added CFFileDescriptorContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>, release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)>)Added CFFileSecurityClearOptions.init(rawValue: CFOptionFlags)Added CFGregorianDate.init()Added CFGregorianDate.init(year: Int32, month: Int8, day: Int8, hour: Int8, minute: Int8, second: Double)Added CFGregorianUnitFlags.init(rawValue: CFOptionFlags)Added CFGregorianUnits.init()Added CFGregorianUnits.init(years: Int32, months: Int32, days: Int32, hours: Int32, minutes: Int32, seconds: Double)Added CFMachPortContext.init()Added CFMachPortContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Added CFMessagePortContext.init()Added CFMessagePortContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Added CFNumberFormatterOptionFlags.init(rawValue: CFOptionFlags)Added CFPropertyListMutabilityOptions.init(rawValue: CFOptionFlags)Added CFRange.init()Added CFRange.init(location: CFIndex, length: CFIndex)Added CFRunLoopActivity.init(rawValue: CFOptionFlags)Added CFRunLoopObserverContext.init()Added CFRunLoopObserverContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Added CFRunLoopSourceContext.init()Added CFRunLoopSourceContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>, equal: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)>, hash: CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)>, schedule: CFunctionPointer<((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)>, cancel: CFunctionPointer<((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)>, perform: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>)Added CFRunLoopSourceContext1.init()Added CFRunLoopSourceContext1.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>, equal: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)>, hash: CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)>, getPort: CFunctionPointer<((UnsafeMutablePointer<Void>) -> mach_port_t)>, perform: CFunctionPointer<((UnsafeMutablePointer<Void>, CFIndex, CFAllocator!, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>)Added CFRunLoopTimerContext.init()Added CFRunLoopTimerContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Added CFSetCallBacks.init()Added CFSetCallBacks.init(version: CFIndex, retain: CFSetRetainCallBack, release: CFSetReleaseCallBack, copyDescription: CFSetCopyDescriptionCallBack, equal: CFSetEqualCallBack, hash: CFSetHashCallBack)Added CFSocketCallBackType.init(rawValue: CFOptionFlags)Added CFSocketContext.init()Added CFSocketContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Added CFSocketSignature.init()Added CFSocketSignature.init(protocolFamily: Int32, socketType: Int32, protocol: Int32, address: Unmanaged<CFData>!)Added CFStreamClientContext.init()Added CFStreamClientContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>, release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)>)Added CFStreamError.init()Added CFStreamError.init(domain: CFIndex, error: Int32)Added CFStreamEventType.init(rawValue: CFOptionFlags)Added CFStringCompareFlags.init(rawValue: CFOptionFlags)Added CFStringInlineBuffer.init()Added CFStringInlineBuffer.init(buffer: (UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar), theString: Unmanaged<CFString>!, directUniCharBuffer: UnsafePointer<UniChar>, directCStringBuffer: UnsafePointer<Int8>, rangeToBuffer: CFRange, bufferedRangeStart: CFIndex, bufferedRangeEnd: CFIndex)Added CFStringTokenizerTokenType.init(rawValue: CFOptionFlags)Added CFSwappedFloat32.init()Added CFSwappedFloat32.init(v: UInt32)Added CFSwappedFloat64.init()Added CFSwappedFloat64.init(v: UInt64)Added CFTreeContext.init()Added CFTreeContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFTreeRetainCallBack, release: CFTreeReleaseCallBack, copyDescription: CFTreeCopyDescriptionCallBack)Added CFURLBookmarkCreationOptions.init(rawValue: CFOptionFlags)Added CFURLBookmarkResolutionOptions.init(rawValue: CFOptionFlags)Added CFURLEnumeratorOptions.init(rawValue: CFOptionFlags)Added CFUUIDBytes.init()Added CFUUIDBytes.init(byte0: UInt8, byte1: UInt8, byte2: UInt8, byte3: UInt8, byte4: UInt8, byte5: UInt8, byte6: UInt8, byte7: UInt8, byte8: UInt8, byte9: UInt8, byte10: UInt8, byte11: UInt8, byte12: UInt8, byte13: UInt8, byte14: UInt8, byte15: UInt8)Added CFXMLAttributeDeclarationInfo.init()Added CFXMLAttributeDeclarationInfo.init(attributeName: Unmanaged<CFString>!, typeString: Unmanaged<CFString>!, defaultString: Unmanaged<CFString>!)Added CFXMLAttributeListDeclarationInfo.init()Added CFXMLAttributeListDeclarationInfo.init(numberOfAttributes: CFIndex, attributes: UnsafeMutablePointer<CFXMLAttributeDeclarationInfo>)Added CFXMLDocumentInfo.init()Added CFXMLDocumentInfo.init(sourceURL: Unmanaged<CFURL>!, encoding: CFStringEncoding)Added CFXMLDocumentTypeInfo.init()Added CFXMLDocumentTypeInfo.init(externalID: CFXMLExternalID)Added CFXMLElementInfo.init()Added CFXMLElementInfo.init(attributes: Unmanaged<CFDictionary>!, attributeOrder: Unmanaged<CFArray>!, isEmpty: Boolean, _reserved:(Int8, Int8, Int8))Added CFXMLElementTypeDeclarationInfo.init()Added CFXMLElementTypeDeclarationInfo.init(contentDescription: Unmanaged<CFString>!)Added CFXMLEntityInfo.init()Added CFXMLEntityInfo.init(entityType: CFXMLEntityTypeCode, replacementText: Unmanaged<CFString>!, entityID: CFXMLExternalID, notationName: Unmanaged<CFString>!)Added CFXMLEntityReferenceInfo.init()Added CFXMLEntityReferenceInfo.init(entityType: CFXMLEntityTypeCode)Added CFXMLExternalID.init()Added CFXMLExternalID.init(systemID: Unmanaged<CFURL>!, publicID: Unmanaged<CFString>!)Added CFXMLNotationInfo.init()Added CFXMLNotationInfo.init(externalID: CFXMLExternalID)Added CFXMLParserCallBacks.init()Added CFXMLParserCallBacks.init(version: CFIndex, createXMLStructure: CFXMLParserCreateXMLStructureCallBack, addChild: CFXMLParserAddChildCallBack, endXMLStructure: CFXMLParserEndXMLStructureCallBack, resolveExternalEntity: CFXMLParserResolveExternalEntityCallBack, handleError: CFXMLParserHandleErrorCallBack)Added CFXMLParserContext.init()Added CFXMLParserContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFXMLParserRetainCallBack, release: CFXMLParserReleaseCallBack, copyDescription: CFXMLParserCopyDescriptionCallBack)Added CFXMLParserOptions.init(rawValue: CFOptionFlags)Added CFXMLParserStatusCode.init(rawValue: CFIndex)Added CFXMLProcessingInstructionInfo.init()Added CFXMLProcessingInstructionInfo.init(dataString: Unmanaged<CFString>!)Modified CFAllocatorContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFAllocatorContext {     var version: CFIndex     var info: UnsafePointer<()>     var retain: CFAllocatorRetainCallBack     var release: CFAllocatorReleaseCallBack     var copyDescription: CFAllocatorCopyDescriptionCallBack     var allocate: CFAllocatorAllocateCallBack     var reallocate: CFAllocatorReallocateCallBack     var deallocate: CFAllocatorDeallocateCallBack     var preferredSize: CFAllocatorPreferredSizeCallBack } ``` |
| To | ``` struct CFAllocatorContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack     var release: CFAllocatorReleaseCallBack     var copyDescription: CFAllocatorCopyDescriptionCallBack     var allocate: CFAllocatorAllocateCallBack     var reallocate: CFAllocatorReallocateCallBack     var deallocate: CFAllocatorDeallocateCallBack     var preferredSize: CFAllocatorPreferredSizeCallBack     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFAllocatorRetainCallBack, release release: CFAllocatorReleaseCallBack, copyDescription copyDescription: CFAllocatorCopyDescriptionCallBack, allocate allocate: CFAllocatorAllocateCallBack, reallocate reallocate: CFAllocatorReallocateCallBack, deallocate deallocate: CFAllocatorDeallocateCallBack, preferredSize preferredSize: CFAllocatorPreferredSizeCallBack) } ``` |

Modified CFAllocatorContext.info

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafePointer<()> ``` |
| To | ``` var info: UnsafeMutablePointer<Void> ``` |

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
| From | ``` struct CFBinaryHeapCallBacks {     var version: CFIndex     var retain: CFunctionPointer<((CFAllocator!, ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)>     var release: CFunctionPointer<((CFAllocator!, ConstUnsafePointer<()>) -> Void)>     var copyDescription: CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)>     var compare: CFunctionPointer<((ConstUnsafePointer<()>, ConstUnsafePointer<()>, UnsafePointer<()>) -> CFComparisonResult)> } ``` |
| To | ``` struct CFBinaryHeapCallBacks {     var version: CFIndex     var retain: CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     var compare: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> CFComparisonResult)>     init()     init(version version: CFIndex, retain retain: CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>, compare compare: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> CFComparisonResult)>) } ``` |

Modified CFBinaryHeapCallBacks.compare

|  | Declaration |
| --- | --- |
| From | ``` var compare: CFunctionPointer<((ConstUnsafePointer<()>, ConstUnsafePointer<()>, UnsafePointer<()>) -> CFComparisonResult)> ``` |
| To | ``` var compare: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> CFComparisonResult)> ``` |

Modified CFBinaryHeapCallBacks.copyDescription

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |

Modified CFBinaryHeapCallBacks.release

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((CFAllocator!, ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` var release: CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> Void)> ``` |

Modified CFBinaryHeapCallBacks.retain

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((CFAllocator!, ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)> ``` |
| To | ``` var retain: CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |

Modified CFBinaryHeapCompareContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFBinaryHeapCompareContext {     var version: CFIndex     var info: UnsafePointer<()>     var retain: CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)>     var release: CFunctionPointer<((ConstUnsafePointer<()>) -> Void)>     var copyDescription: CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> } ``` |
| To | ``` struct CFBinaryHeapCompareContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |

Modified CFBinaryHeapCompareContext.copyDescription

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |

Modified CFBinaryHeapCompareContext.info

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafePointer<()> ``` |
| To | ``` var info: UnsafeMutablePointer<Void> ``` |

Modified CFBinaryHeapCompareContext.release

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |

Modified CFBinaryHeapCompareContext.retain

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)> ``` |
| To | ``` var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |

Modified CFCalendarUnit [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFCalendarUnit : RawOptionSet {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var Era: CFCalendarUnit { get }     static var Year: CFCalendarUnit { get }     static var Month: CFCalendarUnit { get }     static var Day: CFCalendarUnit { get }     static var Hour: CFCalendarUnit { get }     static var Minute: CFCalendarUnit { get }     static var Second: CFCalendarUnit { get }     static var Week: CFCalendarUnit { get }     static var Weekday: CFCalendarUnit { get }     static var WeekdayOrdinal: CFCalendarUnit { get }     static var Quarter: CFCalendarUnit { get }     static var WeekOfMonth: CFCalendarUnit { get }     static var WeekOfYear: CFCalendarUnit { get }     static var YearForWeekOfYear: CFCalendarUnit { get } } ``` | RawOptionSet |
| To | ``` struct CFCalendarUnit : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var Era: CFCalendarUnit { get }     static var Year: CFCalendarUnit { get }     static var Month: CFCalendarUnit { get }     static var Day: CFCalendarUnit { get }     static var Hour: CFCalendarUnit { get }     static var Minute: CFCalendarUnit { get }     static var Second: CFCalendarUnit { get }     static var Week: CFCalendarUnit { get }     static var Weekday: CFCalendarUnit { get }     static var WeekdayOrdinal: CFCalendarUnit { get }     static var Quarter: CFCalendarUnit { get }     static var WeekOfMonth: CFCalendarUnit { get }     static var WeekOfYear: CFCalendarUnit { get }     static var YearForWeekOfYear: CFCalendarUnit { get } } ``` | RawOptionSetType |

Modified CFCalendarUnit.Quarter

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CFCalendarUnit.Week

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified CFCalendarUnit.WeekOfMonth

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CFCalendarUnit.WeekOfYear

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CFCalendarUnit.YearForWeekOfYear

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CFCalendarUnit.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFCharacterSetPredefinedSet.Newline

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFDataSearchFlags [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct CFDataSearchFlags : RawOptionSet {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var Backwards: CFDataSearchFlags { get }     static var Anchored: CFDataSearchFlags { get } } ``` | RawOptionSet | OS X 10.10 |
| To | ``` struct CFDataSearchFlags : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var Backwards: CFDataSearchFlags { get }     static var Anchored: CFDataSearchFlags { get } } ``` | RawOptionSetType | OS X 10.6 |

Modified CFDataSearchFlags.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

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
| From | ``` struct CFFileDescriptorContext {     var version: CFIndex     var info: UnsafePointer<()>     var retain: CFunctionPointer<((UnsafePointer<()>) -> UnsafePointer<()>)>     var release: CFunctionPointer<((UnsafePointer<()>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<()>) -> Unmanaged<CFString>!)> } ``` |
| To | ``` struct CFFileDescriptorContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>     var release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>, release release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |

Modified CFFileDescriptorContext.copyDescription

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((UnsafePointer<()>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)> ``` |

Modified CFFileDescriptorContext.info

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafePointer<()> ``` |
| To | ``` var info: UnsafeMutablePointer<Void> ``` |

Modified CFFileDescriptorContext.release

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((UnsafePointer<()>) -> Void)> ``` |
| To | ``` var release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CFFileDescriptorContext.retain

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((UnsafePointer<()>) -> UnsafePointer<()>)> ``` |
| To | ``` var retain: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)> ``` |

Modified CFFileSecurityClearOptions [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct CFFileSecurityClearOptions : RawOptionSet {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var Owner: CFFileSecurityClearOptions { get }     static var Group: CFFileSecurityClearOptions { get }     static var Mode: CFFileSecurityClearOptions { get }     static var OwnerUUID: CFFileSecurityClearOptions { get }     static var GroupUUID: CFFileSecurityClearOptions { get }     static var AccessControlList: CFFileSecurityClearOptions { get } } ``` | RawOptionSet | OS X 10.10 |
| To | ``` struct CFFileSecurityClearOptions : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var Owner: CFFileSecurityClearOptions { get }     static var Group: CFFileSecurityClearOptions { get }     static var Mode: CFFileSecurityClearOptions { get }     static var OwnerUUID: CFFileSecurityClearOptions { get }     static var GroupUUID: CFFileSecurityClearOptions { get }     static var AccessControlList: CFFileSecurityClearOptions { get } } ``` | RawOptionSetType | OS X 10.8 |

Modified CFFileSecurityClearOptions.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFGregorianDate [struct]

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` struct CFGregorianDate {     var year: Int32     var month: Int8     var day: Int8     var hour: Int8     var minute: Int8     var second: Double } ``` | OS X 10.10 | -- |
| To | ``` struct CFGregorianDate {     var year: Int32     var month: Int8     var day: Int8     var hour: Int8     var minute: Int8     var second: Double     init()     init(year year: Int32, month month: Int8, day day: Int8, hour hour: Int8, minute minute: Int8, second second: Double) } ``` | OS X 10.4 | OS X 10.10 |

Modified CFGregorianDate.day

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified CFGregorianDate.hour

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified CFGregorianDate.minute

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified CFGregorianDate.month

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified CFGregorianDate.second

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified CFGregorianDate.year

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified CFGregorianUnitFlags [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFGregorianUnitFlags : RawOptionSet {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var UnitsYears: CFGregorianUnitFlags { get }     static var UnitsMonths: CFGregorianUnitFlags { get }     static var UnitsDays: CFGregorianUnitFlags { get }     static var UnitsHours: CFGregorianUnitFlags { get }     static var UnitsMinutes: CFGregorianUnitFlags { get }     static var UnitsSeconds: CFGregorianUnitFlags { get }     static var AllUnits: CFGregorianUnitFlags { get } } ``` | RawOptionSet |
| To | ``` struct CFGregorianUnitFlags : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var UnitsYears: CFGregorianUnitFlags { get }     static var UnitsMonths: CFGregorianUnitFlags { get }     static var UnitsDays: CFGregorianUnitFlags { get }     static var UnitsHours: CFGregorianUnitFlags { get }     static var UnitsMinutes: CFGregorianUnitFlags { get }     static var UnitsSeconds: CFGregorianUnitFlags { get }     static var AllUnits: CFGregorianUnitFlags { get } } ``` | RawOptionSetType |

Modified CFGregorianUnitFlags.AllUnits

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified CFGregorianUnitFlags.UnitsDays

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified CFGregorianUnitFlags.UnitsHours

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified CFGregorianUnitFlags.UnitsMinutes

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified CFGregorianUnitFlags.UnitsMonths

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified CFGregorianUnitFlags.UnitsSeconds

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified CFGregorianUnitFlags.UnitsYears

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified CFGregorianUnitFlags.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFGregorianUnits [struct]

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` struct CFGregorianUnits {     var years: Int32     var months: Int32     var days: Int32     var hours: Int32     var minutes: Int32     var seconds: Double } ``` | OS X 10.10 | -- |
| To | ``` struct CFGregorianUnits {     var years: Int32     var months: Int32     var days: Int32     var hours: Int32     var minutes: Int32     var seconds: Double     init()     init(years years: Int32, months months: Int32, days days: Int32, hours hours: Int32, minutes minutes: Int32, seconds seconds: Double) } ``` | OS X 10.4 | OS X 10.10 |

Modified CFGregorianUnits.days

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified CFGregorianUnits.hours

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified CFGregorianUnits.minutes

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified CFGregorianUnits.months

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified CFGregorianUnits.seconds

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified CFGregorianUnits.years

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified CFMachPortContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFMachPortContext {     var version: CFIndex     var info: UnsafePointer<()>     var retain: CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)>     var release: CFunctionPointer<((ConstUnsafePointer<()>) -> Void)>     var copyDescription: CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> } ``` |
| To | ``` struct CFMachPortContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |

Modified CFMachPortContext.copyDescription

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |

Modified CFMachPortContext.info

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafePointer<()> ``` |
| To | ``` var info: UnsafeMutablePointer<Void> ``` |

Modified CFMachPortContext.release

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |

Modified CFMachPortContext.retain

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)> ``` |
| To | ``` var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |

Modified CFMessagePortContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFMessagePortContext {     var version: CFIndex     var info: UnsafePointer<()>     var retain: CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)>     var release: CFunctionPointer<((ConstUnsafePointer<()>) -> Void)>     var copyDescription: CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> } ``` |
| To | ``` struct CFMessagePortContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |

Modified CFMessagePortContext.copyDescription

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |

Modified CFMessagePortContext.info

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafePointer<()> ``` |
| To | ``` var info: UnsafeMutablePointer<Void> ``` |

Modified CFMessagePortContext.release

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |

Modified CFMessagePortContext.retain

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)> ``` |
| To | ``` var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |

Modified CFNumberFormatterOptionFlags [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFNumberFormatterOptionFlags : RawOptionSet {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var ParseIntegersOnly: CFNumberFormatterOptionFlags { get } } ``` | RawOptionSet |
| To | ``` struct CFNumberFormatterOptionFlags : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var ParseIntegersOnly: CFNumberFormatterOptionFlags { get } } ``` | RawOptionSetType |

Modified CFNumberFormatterOptionFlags.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFNumberType.CGFloatType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFNumberType.NSIntegerType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFPropertyListMutabilityOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFPropertyListMutabilityOptions : RawOptionSet {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var Immutable: CFPropertyListMutabilityOptions { get }     static var MutableContainers: CFPropertyListMutabilityOptions { get }     static var MutableContainersAndLeaves: CFPropertyListMutabilityOptions { get } } ``` | RawOptionSet |
| To | ``` struct CFPropertyListMutabilityOptions : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var Immutable: CFPropertyListMutabilityOptions { get }     static var MutableContainers: CFPropertyListMutabilityOptions { get }     static var MutableContainersAndLeaves: CFPropertyListMutabilityOptions { get } } ``` | RawOptionSetType |

Modified CFPropertyListMutabilityOptions.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFRange [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFRange {     var location: CFIndex     var length: CFIndex } ``` |
| To | ``` struct CFRange {     var location: CFIndex     var length: CFIndex     init()     init(location location: CFIndex, length length: CFIndex) } ``` |

Modified CFRunLoopActivity [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFRunLoopActivity : RawOptionSet {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var Entry: CFRunLoopActivity { get }     static var BeforeTimers: CFRunLoopActivity { get }     static var BeforeSources: CFRunLoopActivity { get }     static var BeforeWaiting: CFRunLoopActivity { get }     static var AfterWaiting: CFRunLoopActivity { get }     static var Exit: CFRunLoopActivity { get }     static var AllActivities: CFRunLoopActivity { get } } ``` | RawOptionSet |
| To | ``` struct CFRunLoopActivity : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var Entry: CFRunLoopActivity { get }     static var BeforeTimers: CFRunLoopActivity { get }     static var BeforeSources: CFRunLoopActivity { get }     static var BeforeWaiting: CFRunLoopActivity { get }     static var AfterWaiting: CFRunLoopActivity { get }     static var Exit: CFRunLoopActivity { get }     static var AllActivities: CFRunLoopActivity { get } } ``` | RawOptionSetType |

Modified CFRunLoopActivity.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFRunLoopObserverContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFRunLoopObserverContext {     var version: CFIndex     var info: UnsafePointer<()>     var retain: CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)>     var release: CFunctionPointer<((ConstUnsafePointer<()>) -> Void)>     var copyDescription: CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> } ``` |
| To | ``` struct CFRunLoopObserverContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |

Modified CFRunLoopObserverContext.copyDescription

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |

Modified CFRunLoopObserverContext.info

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafePointer<()> ``` |
| To | ``` var info: UnsafeMutablePointer<Void> ``` |

Modified CFRunLoopObserverContext.release

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |

Modified CFRunLoopObserverContext.retain

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)> ``` |
| To | ``` var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |

Modified CFRunLoopSourceContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFRunLoopSourceContext {     var version: CFIndex     var info: UnsafePointer<()>     var retain: CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)>     var release: CFunctionPointer<((ConstUnsafePointer<()>) -> Void)>     var copyDescription: CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)>     var equal: CFunctionPointer<((ConstUnsafePointer<()>, ConstUnsafePointer<()>) -> Boolean)>     var hash: CFunctionPointer<((ConstUnsafePointer<()>) -> CFHashCode)>     var schedule: CFunctionPointer<((UnsafePointer<()>, CFRunLoop!, CFString!) -> Void)>     var cancel: CFunctionPointer<((UnsafePointer<()>, CFRunLoop!, CFString!) -> Void)>     var perform: CFunctionPointer<((UnsafePointer<()>) -> Void)> } ``` |
| To | ``` struct CFRunLoopSourceContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     var equal: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)>     var hash: CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)>     var schedule: CFunctionPointer<((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)>     var cancel: CFunctionPointer<((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)>     var perform: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>, equal equal: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)>, hash hash: CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)>, schedule schedule: CFunctionPointer<((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)>, cancel cancel: CFunctionPointer<((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)>, perform perform: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>) } ``` |

Modified CFRunLoopSourceContext.cancel

|  | Declaration |
| --- | --- |
| From | ``` var cancel: CFunctionPointer<((UnsafePointer<()>, CFRunLoop!, CFString!) -> Void)> ``` |
| To | ``` var cancel: CFunctionPointer<((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)> ``` |

Modified CFRunLoopSourceContext.copyDescription

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |

Modified CFRunLoopSourceContext.equal

|  | Declaration |
| --- | --- |
| From | ``` var equal: CFunctionPointer<((ConstUnsafePointer<()>, ConstUnsafePointer<()>) -> Boolean)> ``` |
| To | ``` var equal: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)> ``` |

Modified CFRunLoopSourceContext.hash

|  | Declaration |
| --- | --- |
| From | ``` var hash: CFunctionPointer<((ConstUnsafePointer<()>) -> CFHashCode)> ``` |
| To | ``` var hash: CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)> ``` |

Modified CFRunLoopSourceContext.info

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafePointer<()> ``` |
| To | ``` var info: UnsafeMutablePointer<Void> ``` |

Modified CFRunLoopSourceContext.perform

|  | Declaration |
| --- | --- |
| From | ``` var perform: CFunctionPointer<((UnsafePointer<()>) -> Void)> ``` |
| To | ``` var perform: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CFRunLoopSourceContext.release

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |

Modified CFRunLoopSourceContext.retain

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)> ``` |
| To | ``` var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |

Modified CFRunLoopSourceContext.schedule

|  | Declaration |
| --- | --- |
| From | ``` var schedule: CFunctionPointer<((UnsafePointer<()>, CFRunLoop!, CFString!) -> Void)> ``` |
| To | ``` var schedule: CFunctionPointer<((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)> ``` |

Modified CFRunLoopSourceContext1 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFRunLoopSourceContext1 {     var version: CFIndex     var info: UnsafePointer<()>     var retain: CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)>     var release: CFunctionPointer<((ConstUnsafePointer<()>) -> Void)>     var copyDescription: CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)>     var equal: CFunctionPointer<((ConstUnsafePointer<()>, ConstUnsafePointer<()>) -> Boolean)>     var hash: CFunctionPointer<((ConstUnsafePointer<()>) -> CFHashCode)>     var getPort: CFunctionPointer<((UnsafePointer<()>) -> mach_port_t)>     var perform: CFunctionPointer<((UnsafePointer<()>, CFIndex, CFAllocator!, UnsafePointer<()>) -> UnsafePointer<()>)> } ``` |
| To | ``` struct CFRunLoopSourceContext1 {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     var equal: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)>     var hash: CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)>     var getPort: CFunctionPointer<((UnsafeMutablePointer<Void>) -> mach_port_t)>     var perform: CFunctionPointer<((UnsafeMutablePointer<Void>, CFIndex, CFAllocator!, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>, equal equal: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)>, hash hash: CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)>, getPort getPort: CFunctionPointer<((UnsafeMutablePointer<Void>) -> mach_port_t)>, perform perform: CFunctionPointer<((UnsafeMutablePointer<Void>, CFIndex, CFAllocator!, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>) } ``` |

Modified CFRunLoopSourceContext1.copyDescription

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |

Modified CFRunLoopSourceContext1.equal

|  | Declaration |
| --- | --- |
| From | ``` var equal: CFunctionPointer<((ConstUnsafePointer<()>, ConstUnsafePointer<()>) -> Boolean)> ``` |
| To | ``` var equal: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)> ``` |

Modified CFRunLoopSourceContext1.getPort

|  | Declaration |
| --- | --- |
| From | ``` var getPort: CFunctionPointer<((UnsafePointer<()>) -> mach_port_t)> ``` |
| To | ``` var getPort: CFunctionPointer<((UnsafeMutablePointer<Void>) -> mach_port_t)> ``` |

Modified CFRunLoopSourceContext1.hash

|  | Declaration |
| --- | --- |
| From | ``` var hash: CFunctionPointer<((ConstUnsafePointer<()>) -> CFHashCode)> ``` |
| To | ``` var hash: CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)> ``` |

Modified CFRunLoopSourceContext1.info

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafePointer<()> ``` |
| To | ``` var info: UnsafeMutablePointer<Void> ``` |

Modified CFRunLoopSourceContext1.perform

|  | Declaration |
| --- | --- |
| From | ``` var perform: CFunctionPointer<((UnsafePointer<()>, CFIndex, CFAllocator!, UnsafePointer<()>) -> UnsafePointer<()>)> ``` |
| To | ``` var perform: CFunctionPointer<((UnsafeMutablePointer<Void>, CFIndex, CFAllocator!, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)> ``` |

Modified CFRunLoopSourceContext1.release

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |

Modified CFRunLoopSourceContext1.retain

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)> ``` |
| To | ``` var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |

Modified CFRunLoopTimerContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFRunLoopTimerContext {     var version: CFIndex     var info: UnsafePointer<()>     var retain: CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)>     var release: CFunctionPointer<((ConstUnsafePointer<()>) -> Void)>     var copyDescription: CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> } ``` |
| To | ``` struct CFRunLoopTimerContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |

Modified CFRunLoopTimerContext.copyDescription

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |

Modified CFRunLoopTimerContext.info

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafePointer<()> ``` |
| To | ``` var info: UnsafeMutablePointer<Void> ``` |

Modified CFRunLoopTimerContext.release

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |

Modified CFRunLoopTimerContext.retain

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)> ``` |
| To | ``` var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |

Modified CFSetCallBacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFSetCallBacks {     var version: CFIndex     var retain: CFSetRetainCallBack     var release: CFSetReleaseCallBack     var copyDescription: CFSetCopyDescriptionCallBack     var equal: CFSetEqualCallBack     var hash: CFSetHashCallBack } ``` |
| To | ``` struct CFSetCallBacks {     var version: CFIndex     var retain: CFSetRetainCallBack     var release: CFSetReleaseCallBack     var copyDescription: CFSetCopyDescriptionCallBack     var equal: CFSetEqualCallBack     var hash: CFSetHashCallBack     init()     init(version version: CFIndex, retain retain: CFSetRetainCallBack, release release: CFSetReleaseCallBack, copyDescription copyDescription: CFSetCopyDescriptionCallBack, equal equal: CFSetEqualCallBack, hash hash: CFSetHashCallBack) } ``` |

Modified CFSocketCallBackType [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFSocketCallBackType : RawOptionSet {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var NoCallBack: CFSocketCallBackType { get }     static var ReadCallBack: CFSocketCallBackType { get }     static var AcceptCallBack: CFSocketCallBackType { get }     static var DataCallBack: CFSocketCallBackType { get }     static var ConnectCallBack: CFSocketCallBackType { get }     static var WriteCallBack: CFSocketCallBackType { get } } ``` | RawOptionSet |
| To | ``` struct CFSocketCallBackType : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var NoCallBack: CFSocketCallBackType { get }     static var ReadCallBack: CFSocketCallBackType { get }     static var AcceptCallBack: CFSocketCallBackType { get }     static var DataCallBack: CFSocketCallBackType { get }     static var ConnectCallBack: CFSocketCallBackType { get }     static var WriteCallBack: CFSocketCallBackType { get } } ``` | RawOptionSetType |

Modified CFSocketCallBackType.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFSocketContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFSocketContext {     var version: CFIndex     var info: UnsafePointer<()>     var retain: CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)>     var release: CFunctionPointer<((ConstUnsafePointer<()>) -> Void)>     var copyDescription: CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> } ``` |
| To | ``` struct CFSocketContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |

Modified CFSocketContext.copyDescription

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |

Modified CFSocketContext.info

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafePointer<()> ``` |
| To | ``` var info: UnsafeMutablePointer<Void> ``` |

Modified CFSocketContext.release

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |

Modified CFSocketContext.retain

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)> ``` |
| To | ``` var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |

Modified CFSocketSignature [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFSocketSignature {     var protocolFamily: Int32     var socketType: Int32     var `protocol`: Int32     var address: Unmanaged<CFData>! } ``` |
| To | ``` struct CFSocketSignature {     var protocolFamily: Int32     var socketType: Int32     var `protocol`: Int32     var address: Unmanaged<CFData>!     init()     init(protocolFamily protocolFamily: Int32, socketType socketType: Int32, `protocol` `protocol`: Int32, address address: Unmanaged<CFData>!) } ``` |

Modified CFStreamClientContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFStreamClientContext {     var version: CFIndex     var info: UnsafePointer<()>     var retain: CFunctionPointer<((UnsafePointer<()>) -> UnsafePointer<()>)>     var release: CFunctionPointer<((UnsafePointer<()>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<()>) -> Unmanaged<CFString>!)> } ``` |
| To | ``` struct CFStreamClientContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>     var release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>, release release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |

Modified CFStreamClientContext.copyDescription

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((UnsafePointer<()>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)> ``` |

Modified CFStreamClientContext.info

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafePointer<()> ``` |
| To | ``` var info: UnsafeMutablePointer<Void> ``` |

Modified CFStreamClientContext.release

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((UnsafePointer<()>) -> Void)> ``` |
| To | ``` var release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CFStreamClientContext.retain

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((UnsafePointer<()>) -> UnsafePointer<()>)> ``` |
| To | ``` var retain: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)> ``` |

Modified CFStreamError [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFStreamError {     var domain: CFIndex     var error: Int32 } ``` |
| To | ``` struct CFStreamError {     var domain: CFIndex     var error: Int32     init()     init(domain domain: CFIndex, error error: Int32) } ``` |

Modified CFStreamEventType [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFStreamEventType : RawOptionSet {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var None: CFStreamEventType { get }     static var OpenCompleted: CFStreamEventType { get }     static var HasBytesAvailable: CFStreamEventType { get }     static var CanAcceptBytes: CFStreamEventType { get }     static var ErrorOccurred: CFStreamEventType { get }     static var EndEncountered: CFStreamEventType { get } } ``` | RawOptionSet |
| To | ``` struct CFStreamEventType : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var None: CFStreamEventType { get }     static var OpenCompleted: CFStreamEventType { get }     static var HasBytesAvailable: CFStreamEventType { get }     static var CanAcceptBytes: CFStreamEventType { get }     static var ErrorOccurred: CFStreamEventType { get }     static var EndEncountered: CFStreamEventType { get } } ``` | RawOptionSetType |

Modified CFStreamEventType.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFStringCompareFlags [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFStringCompareFlags : RawOptionSet {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var CompareCaseInsensitive: CFStringCompareFlags { get }     static var CompareBackwards: CFStringCompareFlags { get }     static var CompareAnchored: CFStringCompareFlags { get }     static var CompareNonliteral: CFStringCompareFlags { get }     static var CompareLocalized: CFStringCompareFlags { get }     static var CompareNumerically: CFStringCompareFlags { get }     static var CompareDiacriticInsensitive: CFStringCompareFlags { get }     static var CompareWidthInsensitive: CFStringCompareFlags { get }     static var CompareForcedOrdering: CFStringCompareFlags { get } } ``` | RawOptionSet |
| To | ``` struct CFStringCompareFlags : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var CompareCaseInsensitive: CFStringCompareFlags { get }     static var CompareBackwards: CFStringCompareFlags { get }     static var CompareAnchored: CFStringCompareFlags { get }     static var CompareNonliteral: CFStringCompareFlags { get }     static var CompareLocalized: CFStringCompareFlags { get }     static var CompareNumerically: CFStringCompareFlags { get }     static var CompareDiacriticInsensitive: CFStringCompareFlags { get }     static var CompareWidthInsensitive: CFStringCompareFlags { get }     static var CompareForcedOrdering: CFStringCompareFlags { get } } ``` | RawOptionSetType |

Modified CFStringCompareFlags.CompareDiacriticInsensitive

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFStringCompareFlags.CompareForcedOrdering

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFStringCompareFlags.CompareWidthInsensitive

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFStringCompareFlags.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFStringEncodings.ShiftJIS_X0213

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFStringEncodings.UTF7

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CFStringEncodings.UTF7_IMAP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CFStringInlineBuffer [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFStringInlineBuffer {     var buffer: (UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar)     var theString: Unmanaged<CFString>!     var directUniCharBuffer: ConstUnsafePointer<UniChar>     var directCStringBuffer: ConstUnsafePointer<Int8>     var rangeToBuffer: CFRange     var bufferedRangeStart: CFIndex     var bufferedRangeEnd: CFIndex } ``` |
| To | ``` struct CFStringInlineBuffer {     var buffer: (UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar)     var theString: Unmanaged<CFString>!     var directUniCharBuffer: UnsafePointer<UniChar>     var directCStringBuffer: UnsafePointer<Int8>     var rangeToBuffer: CFRange     var bufferedRangeStart: CFIndex     var bufferedRangeEnd: CFIndex     init()     init(buffer buffer: (UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar), theString theString: Unmanaged<CFString>!, directUniCharBuffer directUniCharBuffer: UnsafePointer<UniChar>, directCStringBuffer directCStringBuffer: UnsafePointer<Int8>, rangeToBuffer rangeToBuffer: CFRange, bufferedRangeStart bufferedRangeStart: CFIndex, bufferedRangeEnd bufferedRangeEnd: CFIndex) } ``` |

Modified CFStringInlineBuffer.directCStringBuffer

|  | Declaration |
| --- | --- |
| From | ``` var directCStringBuffer: ConstUnsafePointer<Int8> ``` |
| To | ``` var directCStringBuffer: UnsafePointer<Int8> ``` |

Modified CFStringInlineBuffer.directUniCharBuffer

|  | Declaration |
| --- | --- |
| From | ``` var directUniCharBuffer: ConstUnsafePointer<UniChar> ``` |
| To | ``` var directUniCharBuffer: UnsafePointer<UniChar> ``` |

Modified CFStringTokenizerTokenType [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFStringTokenizerTokenType : RawOptionSet {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var None: CFStringTokenizerTokenType { get }     static var Normal: CFStringTokenizerTokenType { get }     static var HasSubTokensMask: CFStringTokenizerTokenType { get }     static var HasDerivedSubTokensMask: CFStringTokenizerTokenType { get }     static var HasHasNumbersMask: CFStringTokenizerTokenType { get }     static var HasNonLettersMask: CFStringTokenizerTokenType { get }     static var IsCJWordMask: CFStringTokenizerTokenType { get } } ``` | RawOptionSet |
| To | ``` struct CFStringTokenizerTokenType : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var None: CFStringTokenizerTokenType { get }     static var Normal: CFStringTokenizerTokenType { get }     static var HasSubTokensMask: CFStringTokenizerTokenType { get }     static var HasDerivedSubTokensMask: CFStringTokenizerTokenType { get }     static var HasHasNumbersMask: CFStringTokenizerTokenType { get }     static var HasNonLettersMask: CFStringTokenizerTokenType { get }     static var IsCJWordMask: CFStringTokenizerTokenType { get } } ``` | RawOptionSetType |

Modified CFStringTokenizerTokenType.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

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

Modified CFTimeZoneNameStyle [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFTreeContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFTreeContext {     var version: CFIndex     var info: UnsafePointer<()>     var retain: CFTreeRetainCallBack     var release: CFTreeReleaseCallBack     var copyDescription: CFTreeCopyDescriptionCallBack } ``` |
| To | ``` struct CFTreeContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFTreeRetainCallBack     var release: CFTreeReleaseCallBack     var copyDescription: CFTreeCopyDescriptionCallBack     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFTreeRetainCallBack, release release: CFTreeReleaseCallBack, copyDescription copyDescription: CFTreeCopyDescriptionCallBack) } ``` |

Modified CFTreeContext.info

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafePointer<()> ``` |
| To | ``` var info: UnsafeMutablePointer<Void> ``` |

Modified CFURLBookmarkCreationOptions [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct CFURLBookmarkCreationOptions : RawOptionSet {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var MinimalBookmarkMask: CFURLBookmarkCreationOptions { get }     static var SuitableForBookmarkFile: CFURLBookmarkCreationOptions { get }     static var WithSecurityScope: CFURLBookmarkCreationOptions { get }     static var SecurityScopeAllowOnlyReadAccess: CFURLBookmarkCreationOptions { get }     static var PreferFileIDResolutionMask: CFURLBookmarkCreationOptions { get } } ``` | RawOptionSet | OS X 10.10 |
| To | ``` struct CFURLBookmarkCreationOptions : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var MinimalBookmarkMask: CFURLBookmarkCreationOptions { get }     static var SuitableForBookmarkFile: CFURLBookmarkCreationOptions { get }     static var WithSecurityScope: CFURLBookmarkCreationOptions { get }     static var SecurityScopeAllowOnlyReadAccess: CFURLBookmarkCreationOptions { get }     static var PreferFileIDResolutionMask: CFURLBookmarkCreationOptions { get } } ``` | RawOptionSetType | OS X 10.6 |

Modified CFURLBookmarkCreationOptions.SecurityScopeAllowOnlyReadAccess

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CFURLBookmarkCreationOptions.WithSecurityScope

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CFURLBookmarkCreationOptions.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFURLBookmarkResolutionOptions [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct CFURLBookmarkResolutionOptions : RawOptionSet {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var CFURLBookmarkResolutionWithoutUIMask: CFURLBookmarkResolutionOptions { get }     static var CFURLBookmarkResolutionWithoutMountingMask: CFURLBookmarkResolutionOptions { get }     static var CFURLBookmarkResolutionWithSecurityScope: CFURLBookmarkResolutionOptions { get }     static var CFBookmarkResolutionWithoutUIMask: CFURLBookmarkResolutionOptions { get }     static var CFBookmarkResolutionWithoutMountingMask: CFURLBookmarkResolutionOptions { get } } ``` | RawOptionSet | OS X 10.10 |
| To | ``` struct CFURLBookmarkResolutionOptions : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var CFURLBookmarkResolutionWithoutUIMask: CFURLBookmarkResolutionOptions { get }     static var CFURLBookmarkResolutionWithoutMountingMask: CFURLBookmarkResolutionOptions { get }     static var CFURLBookmarkResolutionWithSecurityScope: CFURLBookmarkResolutionOptions { get }     static var CFBookmarkResolutionWithoutUIMask: CFURLBookmarkResolutionOptions { get }     static var CFBookmarkResolutionWithoutMountingMask: CFURLBookmarkResolutionOptions { get } } ``` | RawOptionSetType | OS X 10.6 |

Modified CFURLBookmarkResolutionOptions.CFURLBookmarkResolutionWithSecurityScope

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CFURLBookmarkResolutionOptions.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFURLEnumeratorOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFURLEnumeratorOptions : RawOptionSet {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var DefaultBehavior: CFURLEnumeratorOptions { get }     static var DescendRecursively: CFURLEnumeratorOptions { get }     static var SkipInvisibles: CFURLEnumeratorOptions { get }     static var GenerateFileReferenceURLs: CFURLEnumeratorOptions { get }     static var SkipPackageContents: CFURLEnumeratorOptions { get }     static var IncludeDirectoriesPreOrder: CFURLEnumeratorOptions { get }     static var IncludeDirectoriesPostOrder: CFURLEnumeratorOptions { get } } ``` | RawOptionSet |
| To | ``` struct CFURLEnumeratorOptions : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var DefaultBehavior: CFURLEnumeratorOptions { get }     static var DescendRecursively: CFURLEnumeratorOptions { get }     static var SkipInvisibles: CFURLEnumeratorOptions { get }     static var GenerateFileReferenceURLs: CFURLEnumeratorOptions { get }     static var SkipPackageContents: CFURLEnumeratorOptions { get }     static var IncludeDirectoriesPreOrder: CFURLEnumeratorOptions { get }     static var IncludeDirectoriesPostOrder: CFURLEnumeratorOptions { get } } ``` | RawOptionSetType |

Modified CFURLEnumeratorOptions.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFUUIDBytes [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFUUIDBytes {     var byte0: UInt8     var byte1: UInt8     var byte2: UInt8     var byte3: UInt8     var byte4: UInt8     var byte5: UInt8     var byte6: UInt8     var byte7: UInt8     var byte8: UInt8     var byte9: UInt8     var byte10: UInt8     var byte11: UInt8     var byte12: UInt8     var byte13: UInt8     var byte14: UInt8     var byte15: UInt8 } ``` |
| To | ``` struct CFUUIDBytes {     var byte0: UInt8     var byte1: UInt8     var byte2: UInt8     var byte3: UInt8     var byte4: UInt8     var byte5: UInt8     var byte6: UInt8     var byte7: UInt8     var byte8: UInt8     var byte9: UInt8     var byte10: UInt8     var byte11: UInt8     var byte12: UInt8     var byte13: UInt8     var byte14: UInt8     var byte15: UInt8     init()     init(byte0 byte0: UInt8, byte1 byte1: UInt8, byte2 byte2: UInt8, byte3 byte3: UInt8, byte4 byte4: UInt8, byte5 byte5: UInt8, byte6 byte6: UInt8, byte7 byte7: UInt8, byte8 byte8: UInt8, byte9 byte9: UInt8, byte10 byte10: UInt8, byte11 byte11: UInt8, byte12 byte12: UInt8, byte13 byte13: UInt8, byte14 byte14: UInt8, byte15 byte15: UInt8) } ``` |

Modified CFXMLAttributeDeclarationInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFXMLAttributeDeclarationInfo {     var attributeName: Unmanaged<CFString>!     var typeString: Unmanaged<CFString>!     var defaultString: Unmanaged<CFString>! } ``` |
| To | ``` struct CFXMLAttributeDeclarationInfo {     var attributeName: Unmanaged<CFString>!     var typeString: Unmanaged<CFString>!     var defaultString: Unmanaged<CFString>!     init()     init(attributeName attributeName: Unmanaged<CFString>!, typeString typeString: Unmanaged<CFString>!, defaultString defaultString: Unmanaged<CFString>!) } ``` |

Modified CFXMLAttributeListDeclarationInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFXMLAttributeListDeclarationInfo {     var numberOfAttributes: CFIndex     var attributes: UnsafePointer<CFXMLAttributeDeclarationInfo> } ``` |
| To | ``` struct CFXMLAttributeListDeclarationInfo {     var numberOfAttributes: CFIndex     var attributes: UnsafeMutablePointer<CFXMLAttributeDeclarationInfo>     init()     init(numberOfAttributes numberOfAttributes: CFIndex, attributes attributes: UnsafeMutablePointer<CFXMLAttributeDeclarationInfo>) } ``` |

Modified CFXMLAttributeListDeclarationInfo.attributes

|  | Declaration |
| --- | --- |
| From | ``` var attributes: UnsafePointer<CFXMLAttributeDeclarationInfo> ``` |
| To | ``` var attributes: UnsafeMutablePointer<CFXMLAttributeDeclarationInfo> ``` |

Modified CFXMLDocumentInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFXMLDocumentInfo {     var sourceURL: Unmanaged<CFURL>!     var encoding: CFStringEncoding } ``` |
| To | ``` struct CFXMLDocumentInfo {     var sourceURL: Unmanaged<CFURL>!     var encoding: CFStringEncoding     init()     init(sourceURL sourceURL: Unmanaged<CFURL>!, encoding encoding: CFStringEncoding) } ``` |

Modified CFXMLDocumentTypeInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFXMLDocumentTypeInfo {     var externalID: CFXMLExternalID } ``` |
| To | ``` struct CFXMLDocumentTypeInfo {     var externalID: CFXMLExternalID     init()     init(externalID externalID: CFXMLExternalID) } ``` |

Modified CFXMLElementInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFXMLElementInfo {     var attributes: Unmanaged<CFDictionary>!     var attributeOrder: Unmanaged<CFArray>!     var isEmpty: Boolean     var _reserved: (Int8, Int8, Int8) } ``` |
| To | ``` struct CFXMLElementInfo {     var attributes: Unmanaged<CFDictionary>!     var attributeOrder: Unmanaged<CFArray>!     var isEmpty: Boolean     var _reserved: (Int8, Int8, Int8)     init()     init(attributes attributes: Unmanaged<CFDictionary>!, attributeOrder attributeOrder: Unmanaged<CFArray>!, isEmpty isEmpty: Boolean, _reserved _reserved: (Int8, Int8, Int8)) } ``` |

Modified CFXMLElementTypeDeclarationInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFXMLElementTypeDeclarationInfo {     var contentDescription: Unmanaged<CFString>! } ``` |
| To | ``` struct CFXMLElementTypeDeclarationInfo {     var contentDescription: Unmanaged<CFString>!     init()     init(contentDescription contentDescription: Unmanaged<CFString>!) } ``` |

Modified CFXMLEntityInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFXMLEntityInfo {     var entityType: CFXMLEntityTypeCode     var replacementText: Unmanaged<CFString>!     var entityID: CFXMLExternalID     var notationName: Unmanaged<CFString>! } ``` |
| To | ``` struct CFXMLEntityInfo {     var entityType: CFXMLEntityTypeCode     var replacementText: Unmanaged<CFString>!     var entityID: CFXMLExternalID     var notationName: Unmanaged<CFString>!     init()     init(entityType entityType: CFXMLEntityTypeCode, replacementText replacementText: Unmanaged<CFString>!, entityID entityID: CFXMLExternalID, notationName notationName: Unmanaged<CFString>!) } ``` |

Modified CFXMLEntityReferenceInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFXMLEntityReferenceInfo {     var entityType: CFXMLEntityTypeCode } ``` |
| To | ``` struct CFXMLEntityReferenceInfo {     var entityType: CFXMLEntityTypeCode     init()     init(entityType entityType: CFXMLEntityTypeCode) } ``` |

Modified CFXMLExternalID [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFXMLExternalID {     var systemID: Unmanaged<CFURL>!     var publicID: Unmanaged<CFString>! } ``` |
| To | ``` struct CFXMLExternalID {     var systemID: Unmanaged<CFURL>!     var publicID: Unmanaged<CFString>!     init()     init(systemID systemID: Unmanaged<CFURL>!, publicID publicID: Unmanaged<CFString>!) } ``` |

Modified CFXMLNotationInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFXMLNotationInfo {     var externalID: CFXMLExternalID } ``` |
| To | ``` struct CFXMLNotationInfo {     var externalID: CFXMLExternalID     init()     init(externalID externalID: CFXMLExternalID) } ``` |

Modified CFXMLParserCallBacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFXMLParserCallBacks {     var version: CFIndex     var createXMLStructure: CFXMLParserCreateXMLStructureCallBack     var addChild: CFXMLParserAddChildCallBack     var endXMLStructure: CFXMLParserEndXMLStructureCallBack     var resolveExternalEntity: CFXMLParserResolveExternalEntityCallBack     var handleError: CFXMLParserHandleErrorCallBack } ``` |
| To | ``` struct CFXMLParserCallBacks {     var version: CFIndex     var createXMLStructure: CFXMLParserCreateXMLStructureCallBack     var addChild: CFXMLParserAddChildCallBack     var endXMLStructure: CFXMLParserEndXMLStructureCallBack     var resolveExternalEntity: CFXMLParserResolveExternalEntityCallBack     var handleError: CFXMLParserHandleErrorCallBack     init()     init(version version: CFIndex, createXMLStructure createXMLStructure: CFXMLParserCreateXMLStructureCallBack, addChild addChild: CFXMLParserAddChildCallBack, endXMLStructure endXMLStructure: CFXMLParserEndXMLStructureCallBack, resolveExternalEntity resolveExternalEntity: CFXMLParserResolveExternalEntityCallBack, handleError handleError: CFXMLParserHandleErrorCallBack) } ``` |

Modified CFXMLParserContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFXMLParserContext {     var version: CFIndex     var info: UnsafePointer<()>     var retain: CFXMLParserRetainCallBack     var release: CFXMLParserReleaseCallBack     var copyDescription: CFXMLParserCopyDescriptionCallBack } ``` |
| To | ``` struct CFXMLParserContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFXMLParserRetainCallBack     var release: CFXMLParserReleaseCallBack     var copyDescription: CFXMLParserCopyDescriptionCallBack     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFXMLParserRetainCallBack, release release: CFXMLParserReleaseCallBack, copyDescription copyDescription: CFXMLParserCopyDescriptionCallBack) } ``` |

Modified CFXMLParserContext.info

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafePointer<()> ``` |
| To | ``` var info: UnsafeMutablePointer<Void> ``` |

Modified CFXMLParserOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFXMLParserOptions : RawOptionSet {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var ValidateDocument: CFXMLParserOptions { get }     static var SkipMetaData: CFXMLParserOptions { get }     static var ReplacePhysicalEntities: CFXMLParserOptions { get }     static var SkipWhitespace: CFXMLParserOptions { get }     static var ResolveExternalEntities: CFXMLParserOptions { get }     static var AddImpliedAttributes: CFXMLParserOptions { get }     static var AllOptions: CFXMLParserOptions { get }     static var NoOptions: CFXMLParserOptions { get } } ``` | RawOptionSet |
| To | ``` struct CFXMLParserOptions : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var ValidateDocument: CFXMLParserOptions { get }     static var SkipMetaData: CFXMLParserOptions { get }     static var ReplacePhysicalEntities: CFXMLParserOptions { get }     static var SkipWhitespace: CFXMLParserOptions { get }     static var ResolveExternalEntities: CFXMLParserOptions { get }     static var AddImpliedAttributes: CFXMLParserOptions { get }     static var AllOptions: CFXMLParserOptions { get }     static var NoOptions: CFXMLParserOptions { get } } ``` | RawOptionSetType |

Modified CFXMLParserOptions.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFXMLParserStatusCode [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFXMLParserStatusCode : RawOptionSet {     init(_ value: CFIndex)     var value: CFIndex     static var StatusParseNotBegun: CFXMLParserStatusCode { get }     static var StatusParseInProgress: CFXMLParserStatusCode { get }     static var StatusParseSuccessful: CFXMLParserStatusCode { get }     static var ErrorUnexpectedEOF: CFXMLParserStatusCode { get }     static var ErrorUnknownEncoding: CFXMLParserStatusCode { get }     static var ErrorEncodingConversionFailure: CFXMLParserStatusCode { get }     static var ErrorMalformedProcessingInstruction: CFXMLParserStatusCode { get }     static var ErrorMalformedDTD: CFXMLParserStatusCode { get }     static var ErrorMalformedName: CFXMLParserStatusCode { get }     static var ErrorMalformedCDSect: CFXMLParserStatusCode { get }     static var ErrorMalformedCloseTag: CFXMLParserStatusCode { get }     static var ErrorMalformedStartTag: CFXMLParserStatusCode { get }     static var ErrorMalformedDocument: CFXMLParserStatusCode { get }     static var ErrorElementlessDocument: CFXMLParserStatusCode { get }     static var ErrorMalformedComment: CFXMLParserStatusCode { get }     static var ErrorMalformedCharacterReference: CFXMLParserStatusCode { get }     static var ErrorMalformedParsedCharacterData: CFXMLParserStatusCode { get }     static var ErrorNoData: CFXMLParserStatusCode { get } } ``` | RawOptionSet |
| To | ``` struct CFXMLParserStatusCode : RawOptionSetType {     init(_ rawValue: CFIndex)     init(rawValue rawValue: CFIndex)     static var StatusParseNotBegun: CFXMLParserStatusCode { get }     static var StatusParseInProgress: CFXMLParserStatusCode { get }     static var StatusParseSuccessful: CFXMLParserStatusCode { get }     static var ErrorUnexpectedEOF: CFXMLParserStatusCode { get }     static var ErrorUnknownEncoding: CFXMLParserStatusCode { get }     static var ErrorEncodingConversionFailure: CFXMLParserStatusCode { get }     static var ErrorMalformedProcessingInstruction: CFXMLParserStatusCode { get }     static var ErrorMalformedDTD: CFXMLParserStatusCode { get }     static var ErrorMalformedName: CFXMLParserStatusCode { get }     static var ErrorMalformedCDSect: CFXMLParserStatusCode { get }     static var ErrorMalformedCloseTag: CFXMLParserStatusCode { get }     static var ErrorMalformedStartTag: CFXMLParserStatusCode { get }     static var ErrorMalformedDocument: CFXMLParserStatusCode { get }     static var ErrorElementlessDocument: CFXMLParserStatusCode { get }     static var ErrorMalformedComment: CFXMLParserStatusCode { get }     static var ErrorMalformedCharacterReference: CFXMLParserStatusCode { get }     static var ErrorMalformedParsedCharacterData: CFXMLParserStatusCode { get }     static var ErrorNoData: CFXMLParserStatusCode { get } } ``` | RawOptionSetType |

Modified CFXMLParserStatusCode.init(_: CFIndex)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFIndex) ``` |
| To | ``` init(_ rawValue: CFIndex) ``` |

Modified CFXMLProcessingInstructionInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFXMLProcessingInstructionInfo {     var dataString: Unmanaged<CFString>! } ``` |
| To | ``` struct CFXMLProcessingInstructionInfo {     var dataString: Unmanaged<CFString>!     init()     init(dataString dataString: Unmanaged<CFString>!) } ``` |

Modified CFAbsoluteTimeAddGregorianUnits(CFAbsoluteTime, CFTimeZone!, CFGregorianUnits) -> CFAbsoluteTime

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified CFAbsoluteTimeGetDayOfWeek(CFAbsoluteTime, CFTimeZone!) -> Int32

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified CFAbsoluteTimeGetDayOfYear(CFAbsoluteTime, CFTimeZone!) -> Int32

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified CFAbsoluteTimeGetDifferenceAsGregorianUnits(CFAbsoluteTime, CFAbsoluteTime, CFTimeZone!, CFOptionFlags) -> CFGregorianUnits

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified CFAbsoluteTimeGetGregorianDate(CFAbsoluteTime, CFTimeZone!) -> CFGregorianDate

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified CFAbsoluteTimeGetWeekOfYear(CFAbsoluteTime, CFTimeZone!) -> Int32

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified CFAllocatorAllocate(CFAllocator!, CFIndex, CFOptionFlags) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func CFAllocatorAllocate(_ allocator: CFAllocator!, _ size: CFIndex, _ hint: CFOptionFlags) -> UnsafePointer<()> ``` |
| To | ``` func CFAllocatorAllocate(_ allocator: CFAllocator!, _ size: CFIndex, _ hint: CFOptionFlags) -> UnsafeMutablePointer<Void> ``` |

Modified CFAllocatorAllocateCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFAllocatorAllocateCallBack = CFunctionPointer<((CFIndex, CFOptionFlags, UnsafePointer<()>) -> UnsafePointer<()>)> ``` |
| To | ``` typealias CFAllocatorAllocateCallBack = CFunctionPointer<((CFIndex, CFOptionFlags, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)> ``` |

Modified CFAllocatorCopyDescriptionCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFAllocatorCopyDescriptionCallBack = CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> ``` |
| To | ``` typealias CFAllocatorCopyDescriptionCallBack = CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |

Modified CFAllocatorCreate(CFAllocator!, UnsafeMutablePointer<CFAllocatorContext>) -> Unmanaged<CFAllocator>!

|  | Declaration |
| --- | --- |
| From | ``` func CFAllocatorCreate(_ allocator: CFAllocator!, _ context: UnsafePointer<CFAllocatorContext>) -> Unmanaged<CFAllocator>! ``` |
| To | ``` func CFAllocatorCreate(_ allocator: CFAllocator!, _ context: UnsafeMutablePointer<CFAllocatorContext>) -> Unmanaged<CFAllocator>! ``` |

Modified CFAllocatorDeallocate(CFAllocator!, UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFAllocatorDeallocate(_ allocator: CFAllocator!, _ ptr: UnsafePointer<()>) ``` |
| To | ``` func CFAllocatorDeallocate(_ allocator: CFAllocator!, _ ptr: UnsafeMutablePointer<Void>) ``` |

Modified CFAllocatorDeallocateCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFAllocatorDeallocateCallBack = CFunctionPointer<((UnsafePointer<()>, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFAllocatorDeallocateCallBack = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CFAllocatorGetContext(CFAllocator!, UnsafeMutablePointer<CFAllocatorContext>)

|  | Declaration |
| --- | --- |
| From | ``` func CFAllocatorGetContext(_ allocator: CFAllocator!, _ context: UnsafePointer<CFAllocatorContext>) ``` |
| To | ``` func CFAllocatorGetContext(_ allocator: CFAllocator!, _ context: UnsafeMutablePointer<CFAllocatorContext>) ``` |

Modified CFAllocatorPreferredSizeCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFAllocatorPreferredSizeCallBack = CFunctionPointer<((CFIndex, CFOptionFlags, UnsafePointer<()>) -> CFIndex)> ``` |
| To | ``` typealias CFAllocatorPreferredSizeCallBack = CFunctionPointer<((CFIndex, CFOptionFlags, UnsafeMutablePointer<Void>) -> CFIndex)> ``` |

Modified CFAllocatorReallocate(CFAllocator!, UnsafeMutablePointer<Void>, CFIndex, CFOptionFlags) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func CFAllocatorReallocate(_ allocator: CFAllocator!, _ ptr: UnsafePointer<()>, _ newsize: CFIndex, _ hint: CFOptionFlags) -> UnsafePointer<()> ``` |
| To | ``` func CFAllocatorReallocate(_ allocator: CFAllocator!, _ ptr: UnsafeMutablePointer<Void>, _ newsize: CFIndex, _ hint: CFOptionFlags) -> UnsafeMutablePointer<Void> ``` |

Modified CFAllocatorReallocateCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFAllocatorReallocateCallBack = CFunctionPointer<((UnsafePointer<()>, CFIndex, CFOptionFlags, UnsafePointer<()>) -> UnsafePointer<()>)> ``` |
| To | ``` typealias CFAllocatorReallocateCallBack = CFunctionPointer<((UnsafeMutablePointer<Void>, CFIndex, CFOptionFlags, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)> ``` |

Modified CFAllocatorReleaseCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFAllocatorReleaseCallBack = CFunctionPointer<((ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFAllocatorReleaseCallBack = CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |

Modified CFAllocatorRetainCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFAllocatorRetainCallBack = CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)> ``` |
| To | ``` typealias CFAllocatorRetainCallBack = CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |

Modified CFArrayAppendValue(CFMutableArray!, UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayAppendValue(_ theArray: CFMutableArray!, _ value: ConstUnsafePointer<()>) ``` |
| To | ``` func CFArrayAppendValue(_ theArray: CFMutableArray!, _ value: UnsafePointer<Void>) ``` |

Modified CFArrayApplierFunction

|  | Declaration |
| --- | --- |
| From | ``` typealias CFArrayApplierFunction = CFunctionPointer<((ConstUnsafePointer<()>, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFArrayApplierFunction = CFunctionPointer<((UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CFArrayApplyFunction(CFArray!, CFRange, CFArrayApplierFunction, UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayApplyFunction(_ theArray: CFArray!, _ range: CFRange, _ applier: CFArrayApplierFunction, _ context: UnsafePointer<()>) ``` |
| To | ``` func CFArrayApplyFunction(_ theArray: CFArray!, _ range: CFRange, _ applier: CFArrayApplierFunction, _ context: UnsafeMutablePointer<Void>) ``` |

Modified CFArrayBSearchValues(CFArray!, CFRange, UnsafePointer<Void>, CFComparatorFunction, UnsafeMutablePointer<Void>) -> CFIndex

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayBSearchValues(_ theArray: CFArray!, _ range: CFRange, _ value: ConstUnsafePointer<()>, _ comparator: CFComparatorFunction, _ context: UnsafePointer<()>) -> CFIndex ``` |
| To | ``` func CFArrayBSearchValues(_ theArray: CFArray!, _ range: CFRange, _ value: UnsafePointer<Void>, _ comparator: CFComparatorFunction, _ context: UnsafeMutablePointer<Void>) -> CFIndex ``` |

Modified CFArrayContainsValue(CFArray!, CFRange, UnsafePointer<Void>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayContainsValue(_ theArray: CFArray!, _ range: CFRange, _ value: ConstUnsafePointer<()>) -> Boolean ``` |
| To | ``` func CFArrayContainsValue(_ theArray: CFArray!, _ range: CFRange, _ value: UnsafePointer<Void>) -> Boolean ``` |

Modified CFArrayCopyDescriptionCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFArrayCopyDescriptionCallBack = CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> ``` |
| To | ``` typealias CFArrayCopyDescriptionCallBack = CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |

Modified CFArrayCreate(CFAllocator!, UnsafeMutablePointer<UnsafePointer<Void>>, CFIndex, UnsafePointer<CFArrayCallBacks>) -> CFArray!

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayCreate(_ allocator: CFAllocator!, _ values: UnsafePointer<ConstUnsafePointer<()>>, _ numValues: CFIndex, _ callBacks: ConstUnsafePointer<CFArrayCallBacks>) -> CFArray! ``` |
| To | ``` func CFArrayCreate(_ allocator: CFAllocator!, _ values: UnsafeMutablePointer<UnsafePointer<Void>>, _ numValues: CFIndex, _ callBacks: UnsafePointer<CFArrayCallBacks>) -> CFArray! ``` |

Modified CFArrayCreateMutable(CFAllocator!, CFIndex, UnsafePointer<CFArrayCallBacks>) -> CFMutableArray!

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayCreateMutable(_ allocator: CFAllocator!, _ capacity: CFIndex, _ callBacks: ConstUnsafePointer<CFArrayCallBacks>) -> CFMutableArray! ``` |
| To | ``` func CFArrayCreateMutable(_ allocator: CFAllocator!, _ capacity: CFIndex, _ callBacks: UnsafePointer<CFArrayCallBacks>) -> CFMutableArray! ``` |

Modified CFArrayEqualCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFArrayEqualCallBack = CFunctionPointer<((ConstUnsafePointer<()>, ConstUnsafePointer<()>) -> Boolean)> ``` |
| To | ``` typealias CFArrayEqualCallBack = CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)> ``` |

Modified CFArrayGetCountOfValue(CFArray!, CFRange, UnsafePointer<Void>) -> CFIndex

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayGetCountOfValue(_ theArray: CFArray!, _ range: CFRange, _ value: ConstUnsafePointer<()>) -> CFIndex ``` |
| To | ``` func CFArrayGetCountOfValue(_ theArray: CFArray!, _ range: CFRange, _ value: UnsafePointer<Void>) -> CFIndex ``` |

Modified CFArrayGetFirstIndexOfValue(CFArray!, CFRange, UnsafePointer<Void>) -> CFIndex

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayGetFirstIndexOfValue(_ theArray: CFArray!, _ range: CFRange, _ value: ConstUnsafePointer<()>) -> CFIndex ``` |
| To | ``` func CFArrayGetFirstIndexOfValue(_ theArray: CFArray!, _ range: CFRange, _ value: UnsafePointer<Void>) -> CFIndex ``` |

Modified CFArrayGetLastIndexOfValue(CFArray!, CFRange, UnsafePointer<Void>) -> CFIndex

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayGetLastIndexOfValue(_ theArray: CFArray!, _ range: CFRange, _ value: ConstUnsafePointer<()>) -> CFIndex ``` |
| To | ``` func CFArrayGetLastIndexOfValue(_ theArray: CFArray!, _ range: CFRange, _ value: UnsafePointer<Void>) -> CFIndex ``` |

Modified CFArrayGetValueAtIndex(CFArray!, CFIndex) -> UnsafePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayGetValueAtIndex(_ theArray: CFArray!, _ idx: CFIndex) -> ConstUnsafePointer<()> ``` |
| To | ``` func CFArrayGetValueAtIndex(_ theArray: CFArray!, _ idx: CFIndex) -> UnsafePointer<Void> ``` |

Modified CFArrayGetValues(CFArray!, CFRange, UnsafeMutablePointer<UnsafePointer<Void>>)

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayGetValues(_ theArray: CFArray!, _ range: CFRange, _ values: UnsafePointer<ConstUnsafePointer<()>>) ``` |
| To | ``` func CFArrayGetValues(_ theArray: CFArray!, _ range: CFRange, _ values: UnsafeMutablePointer<UnsafePointer<Void>>) ``` |

Modified CFArrayInsertValueAtIndex(CFMutableArray!, CFIndex, UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayInsertValueAtIndex(_ theArray: CFMutableArray!, _ idx: CFIndex, _ value: ConstUnsafePointer<()>) ``` |
| To | ``` func CFArrayInsertValueAtIndex(_ theArray: CFMutableArray!, _ idx: CFIndex, _ value: UnsafePointer<Void>) ``` |

Modified CFArrayReleaseCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFArrayReleaseCallBack = CFunctionPointer<((CFAllocator!, ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFArrayReleaseCallBack = CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> Void)> ``` |

Modified CFArrayReplaceValues(CFMutableArray!, CFRange, UnsafeMutablePointer<UnsafePointer<Void>>, CFIndex)

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayReplaceValues(_ theArray: CFMutableArray!, _ range: CFRange, _ newValues: UnsafePointer<ConstUnsafePointer<()>>, _ newCount: CFIndex) ``` |
| To | ``` func CFArrayReplaceValues(_ theArray: CFMutableArray!, _ range: CFRange, _ newValues: UnsafeMutablePointer<UnsafePointer<Void>>, _ newCount: CFIndex) ``` |

Modified CFArrayRetainCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFArrayRetainCallBack = CFunctionPointer<((CFAllocator!, ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)> ``` |
| To | ``` typealias CFArrayRetainCallBack = CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |

Modified CFArraySetValueAtIndex(CFMutableArray!, CFIndex, UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFArraySetValueAtIndex(_ theArray: CFMutableArray!, _ idx: CFIndex, _ value: ConstUnsafePointer<()>) ``` |
| To | ``` func CFArraySetValueAtIndex(_ theArray: CFMutableArray!, _ idx: CFIndex, _ value: UnsafePointer<Void>) ``` |

Modified CFArraySortValues(CFMutableArray!, CFRange, CFComparatorFunction, UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFArraySortValues(_ theArray: CFMutableArray!, _ range: CFRange, _ comparator: CFComparatorFunction, _ context: UnsafePointer<()>) ``` |
| To | ``` func CFArraySortValues(_ theArray: CFMutableArray!, _ range: CFRange, _ comparator: CFComparatorFunction, _ context: UnsafeMutablePointer<Void>) ``` |

Modified CFAttributedStringGetAttribute(CFAttributedString!, CFIndex, CFString!, UnsafeMutablePointer<CFRange>) -> AnyObject!

|  | Declaration |
| --- | --- |
| From | ``` func CFAttributedStringGetAttribute(_ aStr: CFAttributedString!, _ loc: CFIndex, _ attrName: CFString!, _ effectiveRange: UnsafePointer<CFRange>) -> AnyObject! ``` |
| To | ``` func CFAttributedStringGetAttribute(_ aStr: CFAttributedString!, _ loc: CFIndex, _ attrName: CFString!, _ effectiveRange: UnsafeMutablePointer<CFRange>) -> AnyObject! ``` |

Modified CFAttributedStringGetAttributeAndLongestEffectiveRange(CFAttributedString!, CFIndex, CFString!, CFRange, UnsafeMutablePointer<CFRange>) -> AnyObject!

|  | Declaration |
| --- | --- |
| From | ``` func CFAttributedStringGetAttributeAndLongestEffectiveRange(_ aStr: CFAttributedString!, _ loc: CFIndex, _ attrName: CFString!, _ inRange: CFRange, _ longestEffectiveRange: UnsafePointer<CFRange>) -> AnyObject! ``` |
| To | ``` func CFAttributedStringGetAttributeAndLongestEffectiveRange(_ aStr: CFAttributedString!, _ loc: CFIndex, _ attrName: CFString!, _ inRange: CFRange, _ longestEffectiveRange: UnsafeMutablePointer<CFRange>) -> AnyObject! ``` |

Modified CFAttributedStringGetAttributes(CFAttributedString!, CFIndex, UnsafeMutablePointer<CFRange>) -> CFDictionary!

|  | Declaration |
| --- | --- |
| From | ``` func CFAttributedStringGetAttributes(_ aStr: CFAttributedString!, _ loc: CFIndex, _ effectiveRange: UnsafePointer<CFRange>) -> CFDictionary! ``` |
| To | ``` func CFAttributedStringGetAttributes(_ aStr: CFAttributedString!, _ loc: CFIndex, _ effectiveRange: UnsafeMutablePointer<CFRange>) -> CFDictionary! ``` |

Modified CFAttributedStringGetAttributesAndLongestEffectiveRange(CFAttributedString!, CFIndex, CFRange, UnsafeMutablePointer<CFRange>) -> CFDictionary!

|  | Declaration |
| --- | --- |
| From | ``` func CFAttributedStringGetAttributesAndLongestEffectiveRange(_ aStr: CFAttributedString!, _ loc: CFIndex, _ inRange: CFRange, _ longestEffectiveRange: UnsafePointer<CFRange>) -> CFDictionary! ``` |
| To | ``` func CFAttributedStringGetAttributesAndLongestEffectiveRange(_ aStr: CFAttributedString!, _ loc: CFIndex, _ inRange: CFRange, _ longestEffectiveRange: UnsafeMutablePointer<CFRange>) -> CFDictionary! ``` |

Modified CFBagAddValue(CFMutableBag!, UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFBagAddValue(_ theBag: CFMutableBag!, _ value: ConstUnsafePointer<()>) ``` |
| To | ``` func CFBagAddValue(_ theBag: CFMutableBag!, _ value: UnsafePointer<Void>) ``` |

Modified CFBagApplierFunction

|  | Declaration |
| --- | --- |
| From | ``` typealias CFBagApplierFunction = CFunctionPointer<((ConstUnsafePointer<()>, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFBagApplierFunction = CFunctionPointer<((UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CFBagApplyFunction(CFBag!, CFBagApplierFunction, UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFBagApplyFunction(_ theBag: CFBag!, _ applier: CFBagApplierFunction, _ context: UnsafePointer<()>) ``` |
| To | ``` func CFBagApplyFunction(_ theBag: CFBag!, _ applier: CFBagApplierFunction, _ context: UnsafeMutablePointer<Void>) ``` |

Modified CFBagContainsValue(CFBag!, UnsafePointer<Void>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFBagContainsValue(_ theBag: CFBag!, _ value: ConstUnsafePointer<()>) -> Boolean ``` |
| To | ``` func CFBagContainsValue(_ theBag: CFBag!, _ value: UnsafePointer<Void>) -> Boolean ``` |

Modified CFBagCopyDescriptionCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFBagCopyDescriptionCallBack = CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> ``` |
| To | ``` typealias CFBagCopyDescriptionCallBack = CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |

Modified CFBagCreate(CFAllocator!, UnsafeMutablePointer<UnsafePointer<Void>>, CFIndex, UnsafePointer<CFBagCallBacks>) -> CFBag!

|  | Declaration |
| --- | --- |
| From | ``` func CFBagCreate(_ allocator: CFAllocator!, _ values: UnsafePointer<ConstUnsafePointer<()>>, _ numValues: CFIndex, _ callBacks: ConstUnsafePointer<CFBagCallBacks>) -> CFBag! ``` |
| To | ``` func CFBagCreate(_ allocator: CFAllocator!, _ values: UnsafeMutablePointer<UnsafePointer<Void>>, _ numValues: CFIndex, _ callBacks: UnsafePointer<CFBagCallBacks>) -> CFBag! ``` |

Modified CFBagCreateMutable(CFAllocator!, CFIndex, UnsafePointer<CFBagCallBacks>) -> CFMutableBag!

|  | Declaration |
| --- | --- |
| From | ``` func CFBagCreateMutable(_ allocator: CFAllocator!, _ capacity: CFIndex, _ callBacks: ConstUnsafePointer<CFBagCallBacks>) -> CFMutableBag! ``` |
| To | ``` func CFBagCreateMutable(_ allocator: CFAllocator!, _ capacity: CFIndex, _ callBacks: UnsafePointer<CFBagCallBacks>) -> CFMutableBag! ``` |

Modified CFBagEqualCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFBagEqualCallBack = CFunctionPointer<((ConstUnsafePointer<()>, ConstUnsafePointer<()>) -> Boolean)> ``` |
| To | ``` typealias CFBagEqualCallBack = CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)> ``` |

Modified CFBagGetCountOfValue(CFBag!, UnsafePointer<Void>) -> CFIndex

|  | Declaration |
| --- | --- |
| From | ``` func CFBagGetCountOfValue(_ theBag: CFBag!, _ value: ConstUnsafePointer<()>) -> CFIndex ``` |
| To | ``` func CFBagGetCountOfValue(_ theBag: CFBag!, _ value: UnsafePointer<Void>) -> CFIndex ``` |

Modified CFBagGetValue(CFBag!, UnsafePointer<Void>) -> UnsafePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func CFBagGetValue(_ theBag: CFBag!, _ value: ConstUnsafePointer<()>) -> ConstUnsafePointer<()> ``` |
| To | ``` func CFBagGetValue(_ theBag: CFBag!, _ value: UnsafePointer<Void>) -> UnsafePointer<Void> ``` |

Modified CFBagGetValueIfPresent(CFBag!, UnsafePointer<Void>, UnsafeMutablePointer<UnsafePointer<Void>>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFBagGetValueIfPresent(_ theBag: CFBag!, _ candidate: ConstUnsafePointer<()>, _ value: UnsafePointer<ConstUnsafePointer<()>>) -> Boolean ``` |
| To | ``` func CFBagGetValueIfPresent(_ theBag: CFBag!, _ candidate: UnsafePointer<Void>, _ value: UnsafeMutablePointer<UnsafePointer<Void>>) -> Boolean ``` |

Modified CFBagGetValues(CFBag!, UnsafeMutablePointer<UnsafePointer<Void>>)

|  | Declaration |
| --- | --- |
| From | ``` func CFBagGetValues(_ theBag: CFBag!, _ values: UnsafePointer<ConstUnsafePointer<()>>) ``` |
| To | ``` func CFBagGetValues(_ theBag: CFBag!, _ values: UnsafeMutablePointer<UnsafePointer<Void>>) ``` |

Modified CFBagHashCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFBagHashCallBack = CFunctionPointer<((ConstUnsafePointer<()>) -> CFHashCode)> ``` |
| To | ``` typealias CFBagHashCallBack = CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)> ``` |

Modified CFBagReleaseCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFBagReleaseCallBack = CFunctionPointer<((CFAllocator!, ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFBagReleaseCallBack = CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> Void)> ``` |

Modified CFBagRemoveValue(CFMutableBag!, UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFBagRemoveValue(_ theBag: CFMutableBag!, _ value: ConstUnsafePointer<()>) ``` |
| To | ``` func CFBagRemoveValue(_ theBag: CFMutableBag!, _ value: UnsafePointer<Void>) ``` |

Modified CFBagReplaceValue(CFMutableBag!, UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFBagReplaceValue(_ theBag: CFMutableBag!, _ value: ConstUnsafePointer<()>) ``` |
| To | ``` func CFBagReplaceValue(_ theBag: CFMutableBag!, _ value: UnsafePointer<Void>) ``` |

Modified CFBagRetainCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFBagRetainCallBack = CFunctionPointer<((CFAllocator!, ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)> ``` |
| To | ``` typealias CFBagRetainCallBack = CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |

Modified CFBagSetValue(CFMutableBag!, UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFBagSetValue(_ theBag: CFMutableBag!, _ value: ConstUnsafePointer<()>) ``` |
| To | ``` func CFBagSetValue(_ theBag: CFMutableBag!, _ value: UnsafePointer<Void>) ``` |

Modified CFBinaryHeapAddValue(CFBinaryHeap!, UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFBinaryHeapAddValue(_ heap: CFBinaryHeap!, _ value: ConstUnsafePointer<()>) ``` |
| To | ``` func CFBinaryHeapAddValue(_ heap: CFBinaryHeap!, _ value: UnsafePointer<Void>) ``` |

Modified CFBinaryHeapApplierFunction

|  | Declaration |
| --- | --- |
| From | ``` typealias CFBinaryHeapApplierFunction = CFunctionPointer<((ConstUnsafePointer<()>, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFBinaryHeapApplierFunction = CFunctionPointer<((UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CFBinaryHeapApplyFunction(CFBinaryHeap!, CFBinaryHeapApplierFunction, UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFBinaryHeapApplyFunction(_ heap: CFBinaryHeap!, _ applier: CFBinaryHeapApplierFunction, _ context: UnsafePointer<()>) ``` |
| To | ``` func CFBinaryHeapApplyFunction(_ heap: CFBinaryHeap!, _ applier: CFBinaryHeapApplierFunction, _ context: UnsafeMutablePointer<Void>) ``` |

Modified CFBinaryHeapContainsValue(CFBinaryHeap!, UnsafePointer<Void>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFBinaryHeapContainsValue(_ heap: CFBinaryHeap!, _ value: ConstUnsafePointer<()>) -> Boolean ``` |
| To | ``` func CFBinaryHeapContainsValue(_ heap: CFBinaryHeap!, _ value: UnsafePointer<Void>) -> Boolean ``` |

Modified CFBinaryHeapCreate(CFAllocator!, CFIndex, UnsafePointer<CFBinaryHeapCallBacks>, UnsafePointer<CFBinaryHeapCompareContext>) -> CFBinaryHeap!

|  | Declaration |
| --- | --- |
| From | ``` func CFBinaryHeapCreate(_ allocator: CFAllocator!, _ capacity: CFIndex, _ callBacks: ConstUnsafePointer<CFBinaryHeapCallBacks>, _ compareContext: ConstUnsafePointer<CFBinaryHeapCompareContext>) -> CFBinaryHeap! ``` |
| To | ``` func CFBinaryHeapCreate(_ allocator: CFAllocator!, _ capacity: CFIndex, _ callBacks: UnsafePointer<CFBinaryHeapCallBacks>, _ compareContext: UnsafePointer<CFBinaryHeapCompareContext>) -> CFBinaryHeap! ``` |

Modified CFBinaryHeapGetCountOfValue(CFBinaryHeap!, UnsafePointer<Void>) -> CFIndex

|  | Declaration |
| --- | --- |
| From | ``` func CFBinaryHeapGetCountOfValue(_ heap: CFBinaryHeap!, _ value: ConstUnsafePointer<()>) -> CFIndex ``` |
| To | ``` func CFBinaryHeapGetCountOfValue(_ heap: CFBinaryHeap!, _ value: UnsafePointer<Void>) -> CFIndex ``` |

Modified CFBinaryHeapGetMinimum(CFBinaryHeap!) -> UnsafePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func CFBinaryHeapGetMinimum(_ heap: CFBinaryHeap!) -> ConstUnsafePointer<()> ``` |
| To | ``` func CFBinaryHeapGetMinimum(_ heap: CFBinaryHeap!) -> UnsafePointer<Void> ``` |

Modified CFBinaryHeapGetMinimumIfPresent(CFBinaryHeap!, UnsafeMutablePointer<UnsafePointer<Void>>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFBinaryHeapGetMinimumIfPresent(_ heap: CFBinaryHeap!, _ value: UnsafePointer<ConstUnsafePointer<()>>) -> Boolean ``` |
| To | ``` func CFBinaryHeapGetMinimumIfPresent(_ heap: CFBinaryHeap!, _ value: UnsafeMutablePointer<UnsafePointer<Void>>) -> Boolean ``` |

Modified CFBinaryHeapGetValues(CFBinaryHeap!, UnsafeMutablePointer<UnsafePointer<Void>>)

|  | Declaration |
| --- | --- |
| From | ``` func CFBinaryHeapGetValues(_ heap: CFBinaryHeap!, _ values: UnsafePointer<ConstUnsafePointer<()>>) ``` |
| To | ``` func CFBinaryHeapGetValues(_ heap: CFBinaryHeap!, _ values: UnsafeMutablePointer<UnsafePointer<Void>>) ``` |

Modified CFBitVectorCreate(CFAllocator!, UnsafePointer<UInt8>, CFIndex) -> CFBitVector!

|  | Declaration |
| --- | --- |
| From | ``` func CFBitVectorCreate(_ allocator: CFAllocator!, _ bytes: ConstUnsafePointer<UInt8>, _ numBits: CFIndex) -> CFBitVector! ``` |
| To | ``` func CFBitVectorCreate(_ allocator: CFAllocator!, _ bytes: UnsafePointer<UInt8>, _ numBits: CFIndex) -> CFBitVector! ``` |

Modified CFBitVectorGetBits(CFBitVector!, CFRange, UnsafeMutablePointer<UInt8>)

|  | Declaration |
| --- | --- |
| From | ``` func CFBitVectorGetBits(_ bv: CFBitVector!, _ range: CFRange, _ bytes: UnsafePointer<UInt8>) ``` |
| To | ``` func CFBitVectorGetBits(_ bv: CFBitVector!, _ range: CFRange, _ bytes: UnsafeMutablePointer<UInt8>) ``` |

Modified CFBundleCopyExecutableArchitectures(CFBundle!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFBundleCopyExecutableArchitecturesForURL(CFURL!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFBundleGetDataPointerForName(CFBundle!, CFString!) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func CFBundleGetDataPointerForName(_ bundle: CFBundle!, _ symbolName: CFString!) -> UnsafePointer<()> ``` |
| To | ``` func CFBundleGetDataPointerForName(_ bundle: CFBundle!, _ symbolName: CFString!) -> UnsafeMutablePointer<Void> ``` |

Modified CFBundleGetDataPointersForNames(CFBundle!, CFArray!, UnsafeMutablePointer<UnsafeMutablePointer<Void>>)

|  | Declaration |
| --- | --- |
| From | ``` func CFBundleGetDataPointersForNames(_ bundle: CFBundle!, _ symbolNames: CFArray!, _ stbl: UnsafePointer<UnsafePointer<()>>) ``` |
| To | ``` func CFBundleGetDataPointersForNames(_ bundle: CFBundle!, _ symbolNames: CFArray!, _ stbl: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) ``` |

Modified CFBundleGetFunctionPointerForName(CFBundle!, CFString!) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func CFBundleGetFunctionPointerForName(_ bundle: CFBundle!, _ functionName: CFString!) -> UnsafePointer<()> ``` |
| To | ``` func CFBundleGetFunctionPointerForName(_ bundle: CFBundle!, _ functionName: CFString!) -> UnsafeMutablePointer<Void> ``` |

Modified CFBundleGetFunctionPointersForNames(CFBundle!, CFArray!, UnsafeMutablePointer<UnsafeMutablePointer<Void>>)

|  | Declaration |
| --- | --- |
| From | ``` func CFBundleGetFunctionPointersForNames(_ bundle: CFBundle!, _ functionNames: CFArray!, _ ftbl: UnsafePointer<UnsafePointer<()>>) ``` |
| To | ``` func CFBundleGetFunctionPointersForNames(_ bundle: CFBundle!, _ functionNames: CFArray!, _ ftbl: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) ``` |

Modified CFBundleGetPackageInfo(CFBundle!, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>)

|  | Declaration |
| --- | --- |
| From | ``` func CFBundleGetPackageInfo(_ bundle: CFBundle!, _ packageType: UnsafePointer<UInt32>, _ packageCreator: UnsafePointer<UInt32>) ``` |
| To | ``` func CFBundleGetPackageInfo(_ bundle: CFBundle!, _ packageType: UnsafeMutablePointer<UInt32>, _ packageCreator: UnsafeMutablePointer<UInt32>) ``` |

Modified CFBundleGetPackageInfoInDirectory(CFURL!, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFBundleGetPackageInfoInDirectory(_ url: CFURL!, _ packageType: UnsafePointer<UInt32>, _ packageCreator: UnsafePointer<UInt32>) -> Boolean ``` |
| To | ``` func CFBundleGetPackageInfoInDirectory(_ url: CFURL!, _ packageType: UnsafeMutablePointer<UInt32>, _ packageCreator: UnsafeMutablePointer<UInt32>) -> Boolean ``` |

Modified CFBundleLoadExecutableAndReturnError(CFBundle!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFBundleLoadExecutableAndReturnError(_ bundle: CFBundle!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFBundleLoadExecutableAndReturnError(_ bundle: CFBundle!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean ``` | OS X 10.5 |

Modified CFBundleOpenBundleResourceFiles(CFBundle!, UnsafeMutablePointer<CFBundleRefNum>, UnsafeMutablePointer<CFBundleRefNum>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func CFBundleOpenBundleResourceFiles(_ bundle: CFBundle!, _ refNum: UnsafePointer<CFBundleRefNum>, _ localizedRefNum: UnsafePointer<CFBundleRefNum>) -> Int32 ``` |
| To | ``` func CFBundleOpenBundleResourceFiles(_ bundle: CFBundle!, _ refNum: UnsafeMutablePointer<CFBundleRefNum>, _ localizedRefNum: UnsafeMutablePointer<CFBundleRefNum>) -> Int32 ``` |

Modified CFBundlePreflightExecutable(CFBundle!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFBundlePreflightExecutable(_ bundle: CFBundle!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFBundlePreflightExecutable(_ bundle: CFBundle!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean ``` | OS X 10.5 |

Modified CFCalendarGetTimeRangeOfUnit(CFCalendar!, CFCalendarUnit, CFAbsoluteTime, UnsafeMutablePointer<CFAbsoluteTime>, UnsafeMutablePointer<CFTimeInterval>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFCalendarGetTimeRangeOfUnit(_ calendar: CFCalendar!, _ unit: CFCalendarUnit, _ at: CFAbsoluteTime, _ startp: UnsafePointer<CFAbsoluteTime>, _ tip: UnsafePointer<CFTimeInterval>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFCalendarGetTimeRangeOfUnit(_ calendar: CFCalendar!, _ unit: CFCalendarUnit, _ at: CFAbsoluteTime, _ startp: UnsafeMutablePointer<CFAbsoluteTime>, _ tip: UnsafeMutablePointer<CFTimeInterval>) -> Boolean ``` | OS X 10.5 |

Modified CFComparatorFunction

|  | Declaration |
| --- | --- |
| From | ``` typealias CFComparatorFunction = CFunctionPointer<((ConstUnsafePointer<()>, ConstUnsafePointer<()>, UnsafePointer<()>) -> CFComparisonResult)> ``` |
| To | ``` typealias CFComparatorFunction = CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> CFComparisonResult)> ``` |

Modified CFDataAppendBytes(CFMutableData!, UnsafePointer<UInt8>, CFIndex)

|  | Declaration |
| --- | --- |
| From | ``` func CFDataAppendBytes(_ theData: CFMutableData!, _ bytes: ConstUnsafePointer<UInt8>, _ length: CFIndex) ``` |
| To | ``` func CFDataAppendBytes(_ theData: CFMutableData!, _ bytes: UnsafePointer<UInt8>, _ length: CFIndex) ``` |

Modified CFDataCreate(CFAllocator!, UnsafePointer<UInt8>, CFIndex) -> CFData!

|  | Declaration |
| --- | --- |
| From | ``` func CFDataCreate(_ allocator: CFAllocator!, _ bytes: ConstUnsafePointer<UInt8>, _ length: CFIndex) -> CFData! ``` |
| To | ``` func CFDataCreate(_ allocator: CFAllocator!, _ bytes: UnsafePointer<UInt8>, _ length: CFIndex) -> CFData! ``` |

Modified CFDataCreateWithBytesNoCopy(CFAllocator!, UnsafePointer<UInt8>, CFIndex, CFAllocator!) -> CFData!

|  | Declaration |
| --- | --- |
| From | ``` func CFDataCreateWithBytesNoCopy(_ allocator: CFAllocator!, _ bytes: ConstUnsafePointer<UInt8>, _ length: CFIndex, _ bytesDeallocator: CFAllocator!) -> CFData! ``` |
| To | ``` func CFDataCreateWithBytesNoCopy(_ allocator: CFAllocator!, _ bytes: UnsafePointer<UInt8>, _ length: CFIndex, _ bytesDeallocator: CFAllocator!) -> CFData! ``` |

Modified CFDataFind(CFData!, CFData!, CFRange, CFDataSearchFlags) -> CFRange

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CFDataGetBytePtr(CFData!) -> UnsafePointer<UInt8>

|  | Declaration |
| --- | --- |
| From | ``` func CFDataGetBytePtr(_ theData: CFData!) -> ConstUnsafePointer<UInt8> ``` |
| To | ``` func CFDataGetBytePtr(_ theData: CFData!) -> UnsafePointer<UInt8> ``` |

Modified CFDataGetBytes(CFData!, CFRange, UnsafeMutablePointer<UInt8>)

|  | Declaration |
| --- | --- |
| From | ``` func CFDataGetBytes(_ theData: CFData!, _ range: CFRange, _ buffer: UnsafePointer<UInt8>) ``` |
| To | ``` func CFDataGetBytes(_ theData: CFData!, _ range: CFRange, _ buffer: UnsafeMutablePointer<UInt8>) ``` |

Modified CFDataGetMutableBytePtr(CFMutableData!) -> UnsafeMutablePointer<UInt8>

|  | Declaration |
| --- | --- |
| From | ``` func CFDataGetMutableBytePtr(_ theData: CFMutableData!) -> UnsafePointer<UInt8> ``` |
| To | ``` func CFDataGetMutableBytePtr(_ theData: CFMutableData!) -> UnsafeMutablePointer<UInt8> ``` |

Modified CFDataReplaceBytes(CFMutableData!, CFRange, UnsafePointer<UInt8>, CFIndex)

|  | Declaration |
| --- | --- |
| From | ``` func CFDataReplaceBytes(_ theData: CFMutableData!, _ range: CFRange, _ newBytes: ConstUnsafePointer<UInt8>, _ newLength: CFIndex) ``` |
| To | ``` func CFDataReplaceBytes(_ theData: CFMutableData!, _ range: CFRange, _ newBytes: UnsafePointer<UInt8>, _ newLength: CFIndex) ``` |

Modified CFDateCompare(CFDate!, CFDate!, UnsafeMutablePointer<Void>) -> CFComparisonResult

|  | Declaration |
| --- | --- |
| From | ``` func CFDateCompare(_ theDate: CFDate!, _ otherDate: CFDate!, _ context: UnsafePointer<()>) -> CFComparisonResult ``` |
| To | ``` func CFDateCompare(_ theDate: CFDate!, _ otherDate: CFDate!, _ context: UnsafeMutablePointer<Void>) -> CFComparisonResult ``` |

Modified CFDateFormatterCreateDateFormatFromTemplate(CFAllocator!, CFString!, CFOptionFlags, CFLocale!) -> CFString!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CFDateFormatterCreateDateFromString(CFAllocator!, CFDateFormatter!, CFString!, UnsafeMutablePointer<CFRange>) -> CFDate!

|  | Declaration |
| --- | --- |
| From | ``` func CFDateFormatterCreateDateFromString(_ allocator: CFAllocator!, _ formatter: CFDateFormatter!, _ string: CFString!, _ rangep: UnsafePointer<CFRange>) -> CFDate! ``` |
| To | ``` func CFDateFormatterCreateDateFromString(_ allocator: CFAllocator!, _ formatter: CFDateFormatter!, _ string: CFString!, _ rangep: UnsafeMutablePointer<CFRange>) -> CFDate! ``` |

Modified CFDateFormatterGetAbsoluteTimeFromString(CFDateFormatter!, CFString!, UnsafeMutablePointer<CFRange>, UnsafeMutablePointer<CFAbsoluteTime>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFDateFormatterGetAbsoluteTimeFromString(_ formatter: CFDateFormatter!, _ string: CFString!, _ rangep: UnsafePointer<CFRange>, _ atp: UnsafePointer<CFAbsoluteTime>) -> Boolean ``` |
| To | ``` func CFDateFormatterGetAbsoluteTimeFromString(_ formatter: CFDateFormatter!, _ string: CFString!, _ rangep: UnsafeMutablePointer<CFRange>, _ atp: UnsafeMutablePointer<CFAbsoluteTime>) -> Boolean ``` |

Modified CFDictionaryAddValue(CFMutableDictionary!, UnsafePointer<Void>, UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryAddValue(_ theDict: CFMutableDictionary!, _ key: ConstUnsafePointer<()>, _ value: ConstUnsafePointer<()>) ``` |
| To | ``` func CFDictionaryAddValue(_ theDict: CFMutableDictionary!, _ key: UnsafePointer<Void>, _ value: UnsafePointer<Void>) ``` |

Modified CFDictionaryApplierFunction

|  | Declaration |
| --- | --- |
| From | ``` typealias CFDictionaryApplierFunction = CFunctionPointer<((ConstUnsafePointer<()>, ConstUnsafePointer<()>, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFDictionaryApplierFunction = CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CFDictionaryApplyFunction(CFDictionary!, CFDictionaryApplierFunction, UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryApplyFunction(_ theDict: CFDictionary!, _ applier: CFDictionaryApplierFunction, _ context: UnsafePointer<()>) ``` |
| To | ``` func CFDictionaryApplyFunction(_ theDict: CFDictionary!, _ applier: CFDictionaryApplierFunction, _ context: UnsafeMutablePointer<Void>) ``` |

Modified CFDictionaryContainsKey(CFDictionary!, UnsafePointer<Void>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryContainsKey(_ theDict: CFDictionary!, _ key: ConstUnsafePointer<()>) -> Boolean ``` |
| To | ``` func CFDictionaryContainsKey(_ theDict: CFDictionary!, _ key: UnsafePointer<Void>) -> Boolean ``` |

Modified CFDictionaryContainsValue(CFDictionary!, UnsafePointer<Void>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryContainsValue(_ theDict: CFDictionary!, _ value: ConstUnsafePointer<()>) -> Boolean ``` |
| To | ``` func CFDictionaryContainsValue(_ theDict: CFDictionary!, _ value: UnsafePointer<Void>) -> Boolean ``` |

Modified CFDictionaryCopyDescriptionCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFDictionaryCopyDescriptionCallBack = CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> ``` |
| To | ``` typealias CFDictionaryCopyDescriptionCallBack = CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |

Modified CFDictionaryCreate(CFAllocator!, UnsafeMutablePointer<UnsafePointer<Void>>, UnsafeMutablePointer<UnsafePointer<Void>>, CFIndex, UnsafePointer<CFDictionaryKeyCallBacks>, UnsafePointer<CFDictionaryValueCallBacks>) -> CFDictionary!

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryCreate(_ allocator: CFAllocator!, _ keys: UnsafePointer<ConstUnsafePointer<()>>, _ values: UnsafePointer<ConstUnsafePointer<()>>, _ numValues: CFIndex, _ keyCallBacks: ConstUnsafePointer<CFDictionaryKeyCallBacks>, _ valueCallBacks: ConstUnsafePointer<CFDictionaryValueCallBacks>) -> CFDictionary! ``` |
| To | ``` func CFDictionaryCreate(_ allocator: CFAllocator!, _ keys: UnsafeMutablePointer<UnsafePointer<Void>>, _ values: UnsafeMutablePointer<UnsafePointer<Void>>, _ numValues: CFIndex, _ keyCallBacks: UnsafePointer<CFDictionaryKeyCallBacks>, _ valueCallBacks: UnsafePointer<CFDictionaryValueCallBacks>) -> CFDictionary! ``` |

Modified CFDictionaryCreateMutable(CFAllocator!, CFIndex, UnsafePointer<CFDictionaryKeyCallBacks>, UnsafePointer<CFDictionaryValueCallBacks>) -> CFMutableDictionary!

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryCreateMutable(_ allocator: CFAllocator!, _ capacity: CFIndex, _ keyCallBacks: ConstUnsafePointer<CFDictionaryKeyCallBacks>, _ valueCallBacks: ConstUnsafePointer<CFDictionaryValueCallBacks>) -> CFMutableDictionary! ``` |
| To | ``` func CFDictionaryCreateMutable(_ allocator: CFAllocator!, _ capacity: CFIndex, _ keyCallBacks: UnsafePointer<CFDictionaryKeyCallBacks>, _ valueCallBacks: UnsafePointer<CFDictionaryValueCallBacks>) -> CFMutableDictionary! ``` |

Modified CFDictionaryEqualCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFDictionaryEqualCallBack = CFunctionPointer<((ConstUnsafePointer<()>, ConstUnsafePointer<()>) -> Boolean)> ``` |
| To | ``` typealias CFDictionaryEqualCallBack = CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)> ``` |

Modified CFDictionaryGetCountOfKey(CFDictionary!, UnsafePointer<Void>) -> CFIndex

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryGetCountOfKey(_ theDict: CFDictionary!, _ key: ConstUnsafePointer<()>) -> CFIndex ``` |
| To | ``` func CFDictionaryGetCountOfKey(_ theDict: CFDictionary!, _ key: UnsafePointer<Void>) -> CFIndex ``` |

Modified CFDictionaryGetCountOfValue(CFDictionary!, UnsafePointer<Void>) -> CFIndex

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryGetCountOfValue(_ theDict: CFDictionary!, _ value: ConstUnsafePointer<()>) -> CFIndex ``` |
| To | ``` func CFDictionaryGetCountOfValue(_ theDict: CFDictionary!, _ value: UnsafePointer<Void>) -> CFIndex ``` |

Modified CFDictionaryGetKeysAndValues(CFDictionary!, UnsafeMutablePointer<UnsafePointer<Void>>, UnsafeMutablePointer<UnsafePointer<Void>>)

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryGetKeysAndValues(_ theDict: CFDictionary!, _ keys: UnsafePointer<ConstUnsafePointer<()>>, _ values: UnsafePointer<ConstUnsafePointer<()>>) ``` |
| To | ``` func CFDictionaryGetKeysAndValues(_ theDict: CFDictionary!, _ keys: UnsafeMutablePointer<UnsafePointer<Void>>, _ values: UnsafeMutablePointer<UnsafePointer<Void>>) ``` |

Modified CFDictionaryGetValue(CFDictionary!, UnsafePointer<Void>) -> UnsafePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryGetValue(_ theDict: CFDictionary!, _ key: ConstUnsafePointer<()>) -> ConstUnsafePointer<()> ``` |
| To | ``` func CFDictionaryGetValue(_ theDict: CFDictionary!, _ key: UnsafePointer<Void>) -> UnsafePointer<Void> ``` |

Modified CFDictionaryGetValueIfPresent(CFDictionary!, UnsafePointer<Void>, UnsafeMutablePointer<UnsafePointer<Void>>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryGetValueIfPresent(_ theDict: CFDictionary!, _ key: ConstUnsafePointer<()>, _ value: UnsafePointer<ConstUnsafePointer<()>>) -> Boolean ``` |
| To | ``` func CFDictionaryGetValueIfPresent(_ theDict: CFDictionary!, _ key: UnsafePointer<Void>, _ value: UnsafeMutablePointer<UnsafePointer<Void>>) -> Boolean ``` |

Modified CFDictionaryHashCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFDictionaryHashCallBack = CFunctionPointer<((ConstUnsafePointer<()>) -> CFHashCode)> ``` |
| To | ``` typealias CFDictionaryHashCallBack = CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)> ``` |

Modified CFDictionaryReleaseCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFDictionaryReleaseCallBack = CFunctionPointer<((CFAllocator!, ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFDictionaryReleaseCallBack = CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> Void)> ``` |

Modified CFDictionaryRemoveValue(CFMutableDictionary!, UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryRemoveValue(_ theDict: CFMutableDictionary!, _ key: ConstUnsafePointer<()>) ``` |
| To | ``` func CFDictionaryRemoveValue(_ theDict: CFMutableDictionary!, _ key: UnsafePointer<Void>) ``` |

Modified CFDictionaryReplaceValue(CFMutableDictionary!, UnsafePointer<Void>, UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryReplaceValue(_ theDict: CFMutableDictionary!, _ key: ConstUnsafePointer<()>, _ value: ConstUnsafePointer<()>) ``` |
| To | ``` func CFDictionaryReplaceValue(_ theDict: CFMutableDictionary!, _ key: UnsafePointer<Void>, _ value: UnsafePointer<Void>) ``` |

Modified CFDictionaryRetainCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFDictionaryRetainCallBack = CFunctionPointer<((CFAllocator!, ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)> ``` |
| To | ``` typealias CFDictionaryRetainCallBack = CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |

Modified CFDictionarySetValue(CFMutableDictionary!, UnsafePointer<Void>, UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionarySetValue(_ theDict: CFMutableDictionary!, _ key: ConstUnsafePointer<()>, _ value: ConstUnsafePointer<()>) ``` |
| To | ``` func CFDictionarySetValue(_ theDict: CFMutableDictionary!, _ key: UnsafePointer<Void>, _ value: UnsafePointer<Void>) ``` |

Modified CFErrorCopyDescription(CFError!) -> CFString!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFErrorCopyFailureReason(CFError!) -> CFString!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFErrorCopyRecoverySuggestion(CFError!) -> CFString!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFErrorCopyUserInfo(CFError!) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFErrorCreate(CFAllocator!, CFString!, CFIndex, CFDictionary!) -> CFError!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFErrorCreateWithUserInfoKeysAndValues(CFAllocator!, CFString!, CFIndex, UnsafePointer<UnsafePointer<Void>>, UnsafePointer<UnsafePointer<Void>>, CFIndex) -> CFError!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFErrorCreateWithUserInfoKeysAndValues(_ allocator: CFAllocator!, _ domain: CFString!, _ code: CFIndex, _ userInfoKeys: ConstUnsafePointer<ConstUnsafePointer<()>>, _ userInfoValues: ConstUnsafePointer<ConstUnsafePointer<()>>, _ numUserInfoValues: CFIndex) -> CFError! ``` | OS X 10.10 |
| To | ``` func CFErrorCreateWithUserInfoKeysAndValues(_ allocator: CFAllocator!, _ domain: CFString!, _ code: CFIndex, _ userInfoKeys: UnsafePointer<UnsafePointer<Void>>, _ userInfoValues: UnsafePointer<UnsafePointer<Void>>, _ numUserInfoValues: CFIndex) -> CFError! ``` | OS X 10.5 |

Modified CFErrorGetCode(CFError!) -> CFIndex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFErrorGetDomain(CFError!) -> CFString!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFErrorGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFFileDescriptorCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFFileDescriptorCallBack = CFunctionPointer<((CFFileDescriptor!, CFOptionFlags, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFFileDescriptorCallBack = CFunctionPointer<((CFFileDescriptor!, CFOptionFlags, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CFFileDescriptorCreate(CFAllocator!, CFFileDescriptorNativeDescriptor, Boolean, CFFileDescriptorCallBack, UnsafePointer<CFFileDescriptorContext>) -> CFFileDescriptor!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFFileDescriptorCreate(_ allocator: CFAllocator!, _ fd: CFFileDescriptorNativeDescriptor, _ closeOnInvalidate: Boolean, _ callout: CFFileDescriptorCallBack, _ context: ConstUnsafePointer<CFFileDescriptorContext>) -> CFFileDescriptor! ``` | OS X 10.10 |
| To | ``` func CFFileDescriptorCreate(_ allocator: CFAllocator!, _ fd: CFFileDescriptorNativeDescriptor, _ closeOnInvalidate: Boolean, _ callout: CFFileDescriptorCallBack, _ context: UnsafePointer<CFFileDescriptorContext>) -> CFFileDescriptor! ``` | OS X 10.5 |

Modified CFFileDescriptorCreateRunLoopSource(CFAllocator!, CFFileDescriptor!, CFIndex) -> CFRunLoopSource!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFFileDescriptorDisableCallBacks(CFFileDescriptor!, CFOptionFlags)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFFileDescriptorEnableCallBacks(CFFileDescriptor!, CFOptionFlags)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFFileDescriptorGetContext(CFFileDescriptor!, UnsafeMutablePointer<CFFileDescriptorContext>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFFileDescriptorGetContext(_ f: CFFileDescriptor!, _ context: UnsafePointer<CFFileDescriptorContext>) ``` | OS X 10.10 |
| To | ``` func CFFileDescriptorGetContext(_ f: CFFileDescriptor!, _ context: UnsafeMutablePointer<CFFileDescriptorContext>) ``` | OS X 10.5 |

Modified CFFileDescriptorGetNativeDescriptor(CFFileDescriptor!) -> CFFileDescriptorNativeDescriptor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFFileDescriptorGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFFileDescriptorInvalidate(CFFileDescriptor!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFFileDescriptorIsValid(CFFileDescriptor!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFFileSecurityClearProperties(CFFileSecurity!, CFFileSecurityClearOptions) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CFFileSecurityCopyAccessControlList(CFFileSecurity!, UnsafeMutablePointer<acl_t>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFFileSecurityCopyAccessControlList(_ fileSec: CFFileSecurity!, _ accessControlList: UnsafePointer<acl_t>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFFileSecurityCopyAccessControlList(_ fileSec: CFFileSecurity!, _ accessControlList: UnsafeMutablePointer<acl_t>) -> Boolean ``` | OS X 10.7 |

Modified CFFileSecurityCopyGroupUUID(CFFileSecurity!, UnsafeMutablePointer<Unmanaged<CFUUID>?>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFFileSecurityCopyGroupUUID(_ fileSec: CFFileSecurity!, _ groupUUID: UnsafePointer<Unmanaged<CFUUID>?>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFFileSecurityCopyGroupUUID(_ fileSec: CFFileSecurity!, _ groupUUID: UnsafeMutablePointer<Unmanaged<CFUUID>?>) -> Boolean ``` | OS X 10.7 |

Modified CFFileSecurityCopyOwnerUUID(CFFileSecurity!, UnsafeMutablePointer<Unmanaged<CFUUID>?>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFFileSecurityCopyOwnerUUID(_ fileSec: CFFileSecurity!, _ ownerUUID: UnsafePointer<Unmanaged<CFUUID>?>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFFileSecurityCopyOwnerUUID(_ fileSec: CFFileSecurity!, _ ownerUUID: UnsafeMutablePointer<Unmanaged<CFUUID>?>) -> Boolean ``` | OS X 10.7 |

Modified CFFileSecurityCreate(CFAllocator!) -> CFFileSecurity!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CFFileSecurityCreateCopy(CFAllocator!, CFFileSecurity!) -> CFFileSecurity!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CFFileSecurityGetGroup(CFFileSecurity!, UnsafeMutablePointer<gid_t>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFFileSecurityGetGroup(_ fileSec: CFFileSecurity!, _ group: UnsafePointer<gid_t>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFFileSecurityGetGroup(_ fileSec: CFFileSecurity!, _ group: UnsafeMutablePointer<gid_t>) -> Boolean ``` | OS X 10.7 |

Modified CFFileSecurityGetMode(CFFileSecurity!, UnsafeMutablePointer<mode_t>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFFileSecurityGetMode(_ fileSec: CFFileSecurity!, _ mode: UnsafePointer<mode_t>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFFileSecurityGetMode(_ fileSec: CFFileSecurity!, _ mode: UnsafeMutablePointer<mode_t>) -> Boolean ``` | OS X 10.7 |

Modified CFFileSecurityGetOwner(CFFileSecurity!, UnsafeMutablePointer<uid_t>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFFileSecurityGetOwner(_ fileSec: CFFileSecurity!, _ owner: UnsafePointer<uid_t>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFFileSecurityGetOwner(_ fileSec: CFFileSecurity!, _ owner: UnsafeMutablePointer<uid_t>) -> Boolean ``` | OS X 10.7 |

Modified CFFileSecurityGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CFFileSecuritySetAccessControlList(CFFileSecurity!, acl_t) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CFFileSecuritySetGroup(CFFileSecurity!, gid_t) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CFFileSecuritySetGroupUUID(CFFileSecurity!, CFUUID!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CFFileSecuritySetMode(CFFileSecurity!, mode_t) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CFFileSecuritySetOwner(CFFileSecurity!, uid_t) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CFFileSecuritySetOwnerUUID(CFFileSecurity!, CFUUID!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CFGregorianDateGetAbsoluteTime(CFGregorianDate, CFTimeZone!) -> CFAbsoluteTime

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified CFGregorianDateIsValid(CFGregorianDate, CFOptionFlags) -> Boolean

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified CFLocaleCopyCommonISOCurrencyCodes() -> CFArray!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFLocaleCopyPreferredLanguages() -> CFArray!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFLocaleCreateLocaleIdentifierFromWindowsLocaleCode(CFAllocator!, UInt32) -> CFString!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CFLocaleGetLanguageCharacterDirection(CFString!) -> CFLocaleLanguageDirection

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CFLocaleGetLanguageLineDirection(CFString!) -> CFLocaleLanguageDirection

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CFLocaleGetWindowsLocaleCodeFromLocaleIdentifier(CFString!) -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CFMachPortCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFMachPortCallBack = CFunctionPointer<((CFMachPort!, UnsafePointer<()>, CFIndex, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFMachPortCallBack = CFunctionPointer<((CFMachPort!, UnsafeMutablePointer<Void>, CFIndex, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CFMachPortCreate(CFAllocator!, CFMachPortCallBack, UnsafeMutablePointer<CFMachPortContext>, UnsafeMutablePointer<Boolean>) -> CFMachPort!

|  | Declaration |
| --- | --- |
| From | ``` func CFMachPortCreate(_ allocator: CFAllocator!, _ callout: CFMachPortCallBack, _ context: UnsafePointer<CFMachPortContext>, _ shouldFreeInfo: UnsafePointer<Boolean>) -> CFMachPort! ``` |
| To | ``` func CFMachPortCreate(_ allocator: CFAllocator!, _ callout: CFMachPortCallBack, _ context: UnsafeMutablePointer<CFMachPortContext>, _ shouldFreeInfo: UnsafeMutablePointer<Boolean>) -> CFMachPort! ``` |

Modified CFMachPortCreateWithPort(CFAllocator!, mach_port_t, CFMachPortCallBack, UnsafeMutablePointer<CFMachPortContext>, UnsafeMutablePointer<Boolean>) -> CFMachPort!

|  | Declaration |
| --- | --- |
| From | ``` func CFMachPortCreateWithPort(_ allocator: CFAllocator!, _ portNum: mach_port_t, _ callout: CFMachPortCallBack, _ context: UnsafePointer<CFMachPortContext>, _ shouldFreeInfo: UnsafePointer<Boolean>) -> CFMachPort! ``` |
| To | ``` func CFMachPortCreateWithPort(_ allocator: CFAllocator!, _ portNum: mach_port_t, _ callout: CFMachPortCallBack, _ context: UnsafeMutablePointer<CFMachPortContext>, _ shouldFreeInfo: UnsafeMutablePointer<Boolean>) -> CFMachPort! ``` |

Modified CFMachPortGetContext(CFMachPort!, UnsafeMutablePointer<CFMachPortContext>)

|  | Declaration |
| --- | --- |
| From | ``` func CFMachPortGetContext(_ port: CFMachPort!, _ context: UnsafePointer<CFMachPortContext>) ``` |
| To | ``` func CFMachPortGetContext(_ port: CFMachPort!, _ context: UnsafeMutablePointer<CFMachPortContext>) ``` |

Modified CFMachPortInvalidationCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFMachPortInvalidationCallBack = CFunctionPointer<((CFMachPort!, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFMachPortInvalidationCallBack = CFunctionPointer<((CFMachPort!, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CFMessagePortCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFMessagePortCallBack = CFunctionPointer<((CFMessagePort!, Int32, CFData!, UnsafePointer<()>) -> Unmanaged<CFData>!)> ``` |
| To | ``` typealias CFMessagePortCallBack = CFunctionPointer<((CFMessagePort!, Int32, CFData!, UnsafeMutablePointer<Void>) -> Unmanaged<CFData>!)> ``` |

Modified CFMessagePortCreateLocal(CFAllocator!, CFString!, CFMessagePortCallBack, UnsafeMutablePointer<CFMessagePortContext>, UnsafeMutablePointer<Boolean>) -> CFMessagePort!

|  | Declaration |
| --- | --- |
| From | ``` func CFMessagePortCreateLocal(_ allocator: CFAllocator!, _ name: CFString!, _ callout: CFMessagePortCallBack, _ context: UnsafePointer<CFMessagePortContext>, _ shouldFreeInfo: UnsafePointer<Boolean>) -> CFMessagePort! ``` |
| To | ``` func CFMessagePortCreateLocal(_ allocator: CFAllocator!, _ name: CFString!, _ callout: CFMessagePortCallBack, _ context: UnsafeMutablePointer<CFMessagePortContext>, _ shouldFreeInfo: UnsafeMutablePointer<Boolean>) -> CFMessagePort! ``` |

Modified CFMessagePortGetContext(CFMessagePort!, UnsafeMutablePointer<CFMessagePortContext>)

|  | Declaration |
| --- | --- |
| From | ``` func CFMessagePortGetContext(_ ms: CFMessagePort!, _ context: UnsafePointer<CFMessagePortContext>) ``` |
| To | ``` func CFMessagePortGetContext(_ ms: CFMessagePort!, _ context: UnsafeMutablePointer<CFMessagePortContext>) ``` |

Modified CFMessagePortInvalidationCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFMessagePortInvalidationCallBack = CFunctionPointer<((CFMessagePort!, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFMessagePortInvalidationCallBack = CFunctionPointer<((CFMessagePort!, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CFMessagePortSendRequest(CFMessagePort!, Int32, CFData!, CFTimeInterval, CFTimeInterval, CFString!, UnsafeMutablePointer<Unmanaged<CFData>?>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func CFMessagePortSendRequest(_ remote: CFMessagePort!, _ msgid: Int32, _ data: CFData!, _ sendTimeout: CFTimeInterval, _ rcvTimeout: CFTimeInterval, _ replyMode: CFString!, _ returnData: UnsafePointer<Unmanaged<CFData>?>) -> Int32 ``` |
| To | ``` func CFMessagePortSendRequest(_ remote: CFMessagePort!, _ msgid: Int32, _ data: CFData!, _ sendTimeout: CFTimeInterval, _ rcvTimeout: CFTimeInterval, _ replyMode: CFString!, _ returnData: UnsafeMutablePointer<Unmanaged<CFData>?>) -> Int32 ``` |

Modified CFMessagePortSetDispatchQueue(CFMessagePort!, dispatch_queue_t!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CFNotificationCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CFNotificationCallback = CFunctionPointer<((CFNotificationCenter!, UnsafePointer<()>, CFString!, ConstUnsafePointer<()>, CFDictionary!) -> Void)> ``` |
| To | ``` typealias CFNotificationCallback = CFunctionPointer<((CFNotificationCenter!, UnsafeMutablePointer<Void>, CFString!, UnsafePointer<Void>, CFDictionary!) -> Void)> ``` |

Modified CFNotificationCenterAddObserver(CFNotificationCenter!, UnsafePointer<Void>, CFNotificationCallback, CFString!, UnsafePointer<Void>, CFNotificationSuspensionBehavior)

|  | Declaration |
| --- | --- |
| From | ``` func CFNotificationCenterAddObserver(_ center: CFNotificationCenter!, _ observer: ConstUnsafePointer<()>, _ callBack: CFNotificationCallback, _ name: CFString!, _ object: ConstUnsafePointer<()>, _ suspensionBehavior: CFNotificationSuspensionBehavior) ``` |
| To | ``` func CFNotificationCenterAddObserver(_ center: CFNotificationCenter!, _ observer: UnsafePointer<Void>, _ callBack: CFNotificationCallback, _ name: CFString!, _ object: UnsafePointer<Void>, _ suspensionBehavior: CFNotificationSuspensionBehavior) ``` |

Modified CFNotificationCenterPostNotification(CFNotificationCenter!, CFString!, UnsafePointer<Void>, CFDictionary!, Boolean)

|  | Declaration |
| --- | --- |
| From | ``` func CFNotificationCenterPostNotification(_ center: CFNotificationCenter!, _ name: CFString!, _ object: ConstUnsafePointer<()>, _ userInfo: CFDictionary!, _ deliverImmediately: Boolean) ``` |
| To | ``` func CFNotificationCenterPostNotification(_ center: CFNotificationCenter!, _ name: CFString!, _ object: UnsafePointer<Void>, _ userInfo: CFDictionary!, _ deliverImmediately: Boolean) ``` |

Modified CFNotificationCenterPostNotificationWithOptions(CFNotificationCenter!, CFString!, UnsafePointer<Void>, CFDictionary!, CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` func CFNotificationCenterPostNotificationWithOptions(_ center: CFNotificationCenter!, _ name: CFString!, _ object: ConstUnsafePointer<()>, _ userInfo: CFDictionary!, _ options: CFOptionFlags) ``` |
| To | ``` func CFNotificationCenterPostNotificationWithOptions(_ center: CFNotificationCenter!, _ name: CFString!, _ object: UnsafePointer<Void>, _ userInfo: CFDictionary!, _ options: CFOptionFlags) ``` |

Modified CFNotificationCenterRemoveEveryObserver(CFNotificationCenter!, UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFNotificationCenterRemoveEveryObserver(_ center: CFNotificationCenter!, _ observer: ConstUnsafePointer<()>) ``` |
| To | ``` func CFNotificationCenterRemoveEveryObserver(_ center: CFNotificationCenter!, _ observer: UnsafePointer<Void>) ``` |

Modified CFNotificationCenterRemoveObserver(CFNotificationCenter!, UnsafePointer<Void>, CFString!, UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFNotificationCenterRemoveObserver(_ center: CFNotificationCenter!, _ observer: ConstUnsafePointer<()>, _ name: CFString!, _ object: ConstUnsafePointer<()>) ``` |
| To | ``` func CFNotificationCenterRemoveObserver(_ center: CFNotificationCenter!, _ observer: UnsafePointer<Void>, _ name: CFString!, _ object: UnsafePointer<Void>) ``` |

Modified CFNumberCompare(CFNumber!, CFNumber!, UnsafeMutablePointer<Void>) -> CFComparisonResult

|  | Declaration |
| --- | --- |
| From | ``` func CFNumberCompare(_ number: CFNumber!, _ otherNumber: CFNumber!, _ context: UnsafePointer<()>) -> CFComparisonResult ``` |
| To | ``` func CFNumberCompare(_ number: CFNumber!, _ otherNumber: CFNumber!, _ context: UnsafeMutablePointer<Void>) -> CFComparisonResult ``` |

Modified CFNumberCreate(CFAllocator!, CFNumberType, UnsafePointer<Void>) -> CFNumber!

|  | Declaration |
| --- | --- |
| From | ``` func CFNumberCreate(_ allocator: CFAllocator!, _ theType: CFNumberType, _ valuePtr: ConstUnsafePointer<()>) -> CFNumber! ``` |
| To | ``` func CFNumberCreate(_ allocator: CFAllocator!, _ theType: CFNumberType, _ valuePtr: UnsafePointer<Void>) -> CFNumber! ``` |

Modified CFNumberFormatterCreateNumberFromString(CFAllocator!, CFNumberFormatter!, CFString!, UnsafeMutablePointer<CFRange>, CFOptionFlags) -> CFNumber!

|  | Declaration |
| --- | --- |
| From | ``` func CFNumberFormatterCreateNumberFromString(_ allocator: CFAllocator!, _ formatter: CFNumberFormatter!, _ string: CFString!, _ rangep: UnsafePointer<CFRange>, _ options: CFOptionFlags) -> CFNumber! ``` |
| To | ``` func CFNumberFormatterCreateNumberFromString(_ allocator: CFAllocator!, _ formatter: CFNumberFormatter!, _ string: CFString!, _ rangep: UnsafeMutablePointer<CFRange>, _ options: CFOptionFlags) -> CFNumber! ``` |

Modified CFNumberFormatterCreateStringWithValue(CFAllocator!, CFNumberFormatter!, CFNumberType, UnsafePointer<Void>) -> CFString!

|  | Declaration |
| --- | --- |
| From | ``` func CFNumberFormatterCreateStringWithValue(_ allocator: CFAllocator!, _ formatter: CFNumberFormatter!, _ numberType: CFNumberType, _ valuePtr: ConstUnsafePointer<()>) -> CFString! ``` |
| To | ``` func CFNumberFormatterCreateStringWithValue(_ allocator: CFAllocator!, _ formatter: CFNumberFormatter!, _ numberType: CFNumberType, _ valuePtr: UnsafePointer<Void>) -> CFString! ``` |

Modified CFNumberFormatterGetDecimalInfoForCurrencyCode(CFString!, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Double>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFNumberFormatterGetDecimalInfoForCurrencyCode(_ currencyCode: CFString!, _ defaultFractionDigits: UnsafePointer<Int32>, _ roundingIncrement: UnsafePointer<Double>) -> Boolean ``` |
| To | ``` func CFNumberFormatterGetDecimalInfoForCurrencyCode(_ currencyCode: CFString!, _ defaultFractionDigits: UnsafeMutablePointer<Int32>, _ roundingIncrement: UnsafeMutablePointer<Double>) -> Boolean ``` |

Modified CFNumberFormatterGetValueFromString(CFNumberFormatter!, CFString!, UnsafeMutablePointer<CFRange>, CFNumberType, UnsafeMutablePointer<Void>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFNumberFormatterGetValueFromString(_ formatter: CFNumberFormatter!, _ string: CFString!, _ rangep: UnsafePointer<CFRange>, _ numberType: CFNumberType, _ valuePtr: UnsafePointer<()>) -> Boolean ``` |
| To | ``` func CFNumberFormatterGetValueFromString(_ formatter: CFNumberFormatter!, _ string: CFString!, _ rangep: UnsafeMutablePointer<CFRange>, _ numberType: CFNumberType, _ valuePtr: UnsafeMutablePointer<Void>) -> Boolean ``` |

Modified CFNumberGetValue(CFNumber!, CFNumberType, UnsafeMutablePointer<Void>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFNumberGetValue(_ number: CFNumber!, _ theType: CFNumberType, _ valuePtr: UnsafePointer<()>) -> Boolean ``` |
| To | ``` func CFNumberGetValue(_ number: CFNumber!, _ theType: CFNumberType, _ valuePtr: UnsafeMutablePointer<Void>) -> Boolean ``` |

Modified CFPlugInFactoryFunction

|  | Declaration |
| --- | --- |
| From | ``` typealias CFPlugInFactoryFunction = CFunctionPointer<((CFAllocator!, CFUUID!) -> UnsafePointer<()>)> ``` |
| To | ``` typealias CFPlugInFactoryFunction = CFunctionPointer<((CFAllocator!, CFUUID!) -> UnsafeMutablePointer<Void>)> ``` |

Modified CFPlugInInstanceCreate(CFAllocator!, CFUUID!, CFUUID!) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func CFPlugInInstanceCreate(_ allocator: CFAllocator!, _ factoryUUID: CFUUID!, _ typeUUID: CFUUID!) -> UnsafePointer<()> ``` |
| To | ``` func CFPlugInInstanceCreate(_ allocator: CFAllocator!, _ factoryUUID: CFUUID!, _ typeUUID: CFUUID!) -> UnsafeMutablePointer<Void> ``` |

Modified CFPlugInInstanceDeallocateInstanceDataFunction

|  | Declaration |
| --- | --- |
| From | ``` typealias CFPlugInInstanceDeallocateInstanceDataFunction = CFunctionPointer<((UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFPlugInInstanceDeallocateInstanceDataFunction = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CFPlugInInstanceGetInstanceData(CFPlugInInstance!) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func CFPlugInInstanceGetInstanceData(_ instance: CFPlugInInstance!) -> UnsafePointer<()> ``` |
| To | ``` func CFPlugInInstanceGetInstanceData(_ instance: CFPlugInInstance!) -> UnsafeMutablePointer<Void> ``` |

Modified CFPlugInInstanceGetInterfaceFunction

|  | Declaration |
| --- | --- |
| From | ``` typealias CFPlugInInstanceGetInterfaceFunction = CFunctionPointer<((CFPlugInInstance!, CFString!, UnsafePointer<UnsafePointer<()>>) -> Boolean)> ``` |
| To | ``` typealias CFPlugInInstanceGetInterfaceFunction = CFunctionPointer<((CFPlugInInstance!, CFString!, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Boolean)> ``` |

Modified CFPlugInInstanceGetInterfaceFunctionTable(CFPlugInInstance!, CFString!, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFPlugInInstanceGetInterfaceFunctionTable(_ instance: CFPlugInInstance!, _ interfaceName: CFString!, _ ftbl: UnsafePointer<UnsafePointer<()>>) -> Boolean ``` |
| To | ``` func CFPlugInInstanceGetInterfaceFunctionTable(_ instance: CFPlugInInstance!, _ interfaceName: CFString!, _ ftbl: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Boolean ``` |

Modified CFPreferencesCopyAppValue(CFString!, CFString!) -> CFPropertyList!

|  | Declaration |
| --- | --- |
| From | ``` func CFPreferencesCopyAppValue(_ key: CFString!, _ applicationID: CFString!) -> CFPropertyListRef! ``` |
| To | ``` func CFPreferencesCopyAppValue(_ key: CFString!, _ applicationID: CFString!) -> CFPropertyList! ``` |

Modified CFPreferencesCopyValue(CFString!, CFString!, CFString!, CFString!) -> CFPropertyList!

|  | Declaration |
| --- | --- |
| From | ``` func CFPreferencesCopyValue(_ key: CFString!, _ applicationID: CFString!, _ userName: CFString!, _ hostName: CFString!) -> CFPropertyListRef! ``` |
| To | ``` func CFPreferencesCopyValue(_ key: CFString!, _ applicationID: CFString!, _ userName: CFString!, _ hostName: CFString!) -> CFPropertyList! ``` |

Modified CFPreferencesGetAppBooleanValue(CFString!, CFString!, UnsafeMutablePointer<Boolean>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFPreferencesGetAppBooleanValue(_ key: CFString!, _ applicationID: CFString!, _ keyExistsAndHasValidFormat: UnsafePointer<Boolean>) -> Boolean ``` |
| To | ``` func CFPreferencesGetAppBooleanValue(_ key: CFString!, _ applicationID: CFString!, _ keyExistsAndHasValidFormat: UnsafeMutablePointer<Boolean>) -> Boolean ``` |

Modified CFPreferencesGetAppIntegerValue(CFString!, CFString!, UnsafeMutablePointer<Boolean>) -> CFIndex

|  | Declaration |
| --- | --- |
| From | ``` func CFPreferencesGetAppIntegerValue(_ key: CFString!, _ applicationID: CFString!, _ keyExistsAndHasValidFormat: UnsafePointer<Boolean>) -> CFIndex ``` |
| To | ``` func CFPreferencesGetAppIntegerValue(_ key: CFString!, _ applicationID: CFString!, _ keyExistsAndHasValidFormat: UnsafeMutablePointer<Boolean>) -> CFIndex ``` |

Modified CFPreferencesSetAppValue(CFString!, CFPropertyList!, CFString!)

|  | Declaration |
| --- | --- |
| From | ``` func CFPreferencesSetAppValue(_ key: CFString!, _ value: CFPropertyListRef!, _ applicationID: CFString!) ``` |
| To | ``` func CFPreferencesSetAppValue(_ key: CFString!, _ value: CFPropertyList!, _ applicationID: CFString!) ``` |

Modified CFPreferencesSetValue(CFString!, CFPropertyList!, CFString!, CFString!, CFString!)

|  | Declaration |
| --- | --- |
| From | ``` func CFPreferencesSetValue(_ key: CFString!, _ value: CFPropertyListRef!, _ applicationID: CFString!, _ userName: CFString!, _ hostName: CFString!) ``` |
| To | ``` func CFPreferencesSetValue(_ key: CFString!, _ value: CFPropertyList!, _ applicationID: CFString!, _ userName: CFString!, _ hostName: CFString!) ``` |

Modified CFPropertyListCreateData(CFAllocator!, CFPropertyList!, CFPropertyListFormat, CFOptionFlags, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFPropertyListCreateData(_ allocator: CFAllocator!, _ propertyList: CFPropertyListRef!, _ format: CFPropertyListFormat, _ options: CFOptionFlags, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>! ``` | OS X 10.10 |
| To | ``` func CFPropertyListCreateData(_ allocator: CFAllocator!, _ propertyList: CFPropertyList!, _ format: CFPropertyListFormat, _ options: CFOptionFlags, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>! ``` | OS X 10.6 |

Modified CFPropertyListCreateDeepCopy(CFAllocator!, CFPropertyList!, CFOptionFlags) -> CFPropertyList!

|  | Declaration |
| --- | --- |
| From | ``` func CFPropertyListCreateDeepCopy(_ allocator: CFAllocator!, _ propertyList: CFPropertyListRef!, _ mutabilityOption: CFOptionFlags) -> CFPropertyListRef! ``` |
| To | ``` func CFPropertyListCreateDeepCopy(_ allocator: CFAllocator!, _ propertyList: CFPropertyList!, _ mutabilityOption: CFOptionFlags) -> CFPropertyList! ``` |

Modified CFPropertyListCreateFromStream(CFAllocator!, CFReadStream!, CFIndex, CFOptionFlags, UnsafeMutablePointer<CFPropertyListFormat>, UnsafeMutablePointer<Unmanaged<CFString>?>) -> Unmanaged<CFPropertyList>!

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func CFPropertyListCreateFromStream(_ allocator: CFAllocator!, _ stream: CFReadStream!, _ streamLength: CFIndex, _ mutabilityOption: CFOptionFlags, _ format: UnsafePointer<CFPropertyListFormat>, _ errorString: UnsafePointer<Unmanaged<CFString>?>) -> Unmanaged<CFPropertyListRef>! ``` | OS X 10.10 | -- |
| To | ``` func CFPropertyListCreateFromStream(_ allocator: CFAllocator!, _ stream: CFReadStream!, _ streamLength: CFIndex, _ mutabilityOption: CFOptionFlags, _ format: UnsafeMutablePointer<CFPropertyListFormat>, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>) -> Unmanaged<CFPropertyList>! ``` | OS X 10.2 | OS X 10.10 |

Modified CFPropertyListCreateFromXMLData(CFAllocator!, CFData!, CFOptionFlags, UnsafeMutablePointer<Unmanaged<CFString>?>) -> Unmanaged<CFPropertyList>!

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func CFPropertyListCreateFromXMLData(_ allocator: CFAllocator!, _ xmlData: CFData!, _ mutabilityOption: CFOptionFlags, _ errorString: UnsafePointer<Unmanaged<CFString>?>) -> Unmanaged<CFPropertyListRef>! ``` | OS X 10.10 | -- |
| To | ``` func CFPropertyListCreateFromXMLData(_ allocator: CFAllocator!, _ xmlData: CFData!, _ mutabilityOption: CFOptionFlags, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>) -> Unmanaged<CFPropertyList>! ``` | OS X 10.0 | OS X 10.10 |

Modified CFPropertyListCreateWithData(CFAllocator!, CFData!, CFOptionFlags, UnsafeMutablePointer<CFPropertyListFormat>, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFPropertyList>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFPropertyListCreateWithData(_ allocator: CFAllocator!, _ data: CFData!, _ options: CFOptionFlags, _ format: UnsafePointer<CFPropertyListFormat>, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFPropertyListRef>! ``` | OS X 10.10 |
| To | ``` func CFPropertyListCreateWithData(_ allocator: CFAllocator!, _ data: CFData!, _ options: CFOptionFlags, _ format: UnsafeMutablePointer<CFPropertyListFormat>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFPropertyList>! ``` | OS X 10.6 |

Modified CFPropertyListCreateWithStream(CFAllocator!, CFReadStream!, CFIndex, CFOptionFlags, UnsafeMutablePointer<CFPropertyListFormat>, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFPropertyList>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFPropertyListCreateWithStream(_ allocator: CFAllocator!, _ stream: CFReadStream!, _ streamLength: CFIndex, _ options: CFOptionFlags, _ format: UnsafePointer<CFPropertyListFormat>, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFPropertyListRef>! ``` | OS X 10.10 |
| To | ``` func CFPropertyListCreateWithStream(_ allocator: CFAllocator!, _ stream: CFReadStream!, _ streamLength: CFIndex, _ options: CFOptionFlags, _ format: UnsafeMutablePointer<CFPropertyListFormat>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFPropertyList>! ``` | OS X 10.6 |

Modified CFPropertyListCreateXMLData(CFAllocator!, CFPropertyList!) -> Unmanaged<CFData>!

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func CFPropertyListCreateXMLData(_ allocator: CFAllocator!, _ propertyList: CFPropertyListRef!) -> Unmanaged<CFData>! ``` | OS X 10.10 | -- |
| To | ``` func CFPropertyListCreateXMLData(_ allocator: CFAllocator!, _ propertyList: CFPropertyList!) -> Unmanaged<CFData>! ``` | OS X 10.0 | OS X 10.10 |

Modified CFPropertyListIsValid(CFPropertyList!, CFPropertyListFormat) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFPropertyListIsValid(_ plist: CFPropertyListRef!, _ format: CFPropertyListFormat) -> Boolean ``` |
| To | ``` func CFPropertyListIsValid(_ plist: CFPropertyList!, _ format: CFPropertyListFormat) -> Boolean ``` |

Modified CFPropertyListRef

|  | Declaration |
| --- | --- |
| From | ``` typealias CFPropertyListRef = AnyObject ``` |
| To | ``` typealias CFPropertyListRef = CFPropertyList ``` |

Modified CFPropertyListWrite(CFPropertyList!, CFWriteStream!, CFPropertyListFormat, CFOptionFlags, UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFIndex

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFPropertyListWrite(_ propertyList: CFPropertyListRef!, _ stream: CFWriteStream!, _ format: CFPropertyListFormat, _ options: CFOptionFlags, _ error: UnsafePointer<Unmanaged<CFError>?>) -> CFIndex ``` | OS X 10.10 |
| To | ``` func CFPropertyListWrite(_ propertyList: CFPropertyList!, _ stream: CFWriteStream!, _ format: CFPropertyListFormat, _ options: CFOptionFlags, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFIndex ``` | OS X 10.6 |

Modified CFPropertyListWriteToStream(CFPropertyList!, CFWriteStream!, CFPropertyListFormat, UnsafeMutablePointer<Unmanaged<CFString>?>) -> CFIndex

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func CFPropertyListWriteToStream(_ propertyList: CFPropertyListRef!, _ stream: CFWriteStream!, _ format: CFPropertyListFormat, _ errorString: UnsafePointer<Unmanaged<CFString>?>) -> CFIndex ``` | OS X 10.10 | -- |
| To | ``` func CFPropertyListWriteToStream(_ propertyList: CFPropertyList!, _ stream: CFWriteStream!, _ format: CFPropertyListFormat, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>) -> CFIndex ``` | OS X 10.2 | OS X 10.10 |

Modified CFReadStreamClientCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFReadStreamClientCallBack = CFunctionPointer<((CFReadStream!, CFStreamEventType, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFReadStreamClientCallBack = CFunctionPointer<((CFReadStream!, CFStreamEventType, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CFReadStreamCopyDispatchQueue(CFReadStream!) -> dispatch_queue_t!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CFReadStreamCopyError(CFReadStream!) -> CFError!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFReadStreamCreateWithBytesNoCopy(CFAllocator!, UnsafePointer<UInt8>, CFIndex, CFAllocator!) -> CFReadStream!

|  | Declaration |
| --- | --- |
| From | ``` func CFReadStreamCreateWithBytesNoCopy(_ alloc: CFAllocator!, _ bytes: ConstUnsafePointer<UInt8>, _ length: CFIndex, _ bytesDeallocator: CFAllocator!) -> CFReadStream! ``` |
| To | ``` func CFReadStreamCreateWithBytesNoCopy(_ alloc: CFAllocator!, _ bytes: UnsafePointer<UInt8>, _ length: CFIndex, _ bytesDeallocator: CFAllocator!) -> CFReadStream! ``` |

Modified CFReadStreamGetBuffer(CFReadStream!, CFIndex, UnsafeMutablePointer<CFIndex>) -> UnsafePointer<UInt8>

|  | Declaration |
| --- | --- |
| From | ``` func CFReadStreamGetBuffer(_ stream: CFReadStream!, _ maxBytesToRead: CFIndex, _ numBytesRead: UnsafePointer<CFIndex>) -> ConstUnsafePointer<UInt8> ``` |
| To | ``` func CFReadStreamGetBuffer(_ stream: CFReadStream!, _ maxBytesToRead: CFIndex, _ numBytesRead: UnsafeMutablePointer<CFIndex>) -> UnsafePointer<UInt8> ``` |

Modified CFReadStreamRead(CFReadStream!, UnsafeMutablePointer<UInt8>, CFIndex) -> CFIndex

|  | Declaration |
| --- | --- |
| From | ``` func CFReadStreamRead(_ stream: CFReadStream!, _ buffer: UnsafePointer<UInt8>, _ bufferLength: CFIndex) -> CFIndex ``` |
| To | ``` func CFReadStreamRead(_ stream: CFReadStream!, _ buffer: UnsafeMutablePointer<UInt8>, _ bufferLength: CFIndex) -> CFIndex ``` |

Modified CFReadStreamSetClient(CFReadStream!, CFOptionFlags, CFReadStreamClientCallBack, UnsafeMutablePointer<CFStreamClientContext>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFReadStreamSetClient(_ stream: CFReadStream!, _ streamEvents: CFOptionFlags, _ clientCB: CFReadStreamClientCallBack, _ clientContext: UnsafePointer<CFStreamClientContext>) -> Boolean ``` |
| To | ``` func CFReadStreamSetClient(_ stream: CFReadStream!, _ streamEvents: CFOptionFlags, _ clientCB: CFReadStreamClientCallBack, _ clientContext: UnsafeMutablePointer<CFStreamClientContext>) -> Boolean ``` |

Modified CFReadStreamSetDispatchQueue(CFReadStream!, dispatch_queue_t!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CFRunLoopObserverCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFRunLoopObserverCallBack = CFunctionPointer<((CFRunLoopObserver!, CFRunLoopActivity, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFRunLoopObserverCallBack = CFunctionPointer<((CFRunLoopObserver!, CFRunLoopActivity, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CFRunLoopObserverCreate(CFAllocator!, CFOptionFlags, Boolean, CFIndex, CFRunLoopObserverCallBack, UnsafeMutablePointer<CFRunLoopObserverContext>) -> CFRunLoopObserver!

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopObserverCreate(_ allocator: CFAllocator!, _ activities: CFOptionFlags, _ repeats: Boolean, _ order: CFIndex, _ callout: CFRunLoopObserverCallBack, _ context: UnsafePointer<CFRunLoopObserverContext>) -> CFRunLoopObserver! ``` |
| To | ``` func CFRunLoopObserverCreate(_ allocator: CFAllocator!, _ activities: CFOptionFlags, _ repeats: Boolean, _ order: CFIndex, _ callout: CFRunLoopObserverCallBack, _ context: UnsafeMutablePointer<CFRunLoopObserverContext>) -> CFRunLoopObserver! ``` |

Modified CFRunLoopObserverCreateWithHandler(CFAllocator!, CFOptionFlags, Boolean, CFIndex,((CFRunLoopObserver!, CFRunLoopActivity) -> Void)!) -> CFRunLoopObserver!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CFRunLoopObserverGetContext(CFRunLoopObserver!, UnsafeMutablePointer<CFRunLoopObserverContext>)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopObserverGetContext(_ observer: CFRunLoopObserver!, _ context: UnsafePointer<CFRunLoopObserverContext>) ``` |
| To | ``` func CFRunLoopObserverGetContext(_ observer: CFRunLoopObserver!, _ context: UnsafeMutablePointer<CFRunLoopObserverContext>) ``` |

Modified CFRunLoopPerformBlock(CFRunLoop!, AnyObject!,(() -> Void)!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CFRunLoopSourceCreate(CFAllocator!, CFIndex, UnsafeMutablePointer<CFRunLoopSourceContext>) -> CFRunLoopSource!

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopSourceCreate(_ allocator: CFAllocator!, _ order: CFIndex, _ context: UnsafePointer<CFRunLoopSourceContext>) -> CFRunLoopSource! ``` |
| To | ``` func CFRunLoopSourceCreate(_ allocator: CFAllocator!, _ order: CFIndex, _ context: UnsafeMutablePointer<CFRunLoopSourceContext>) -> CFRunLoopSource! ``` |

Modified CFRunLoopSourceGetContext(CFRunLoopSource!, UnsafeMutablePointer<CFRunLoopSourceContext>)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopSourceGetContext(_ source: CFRunLoopSource!, _ context: UnsafePointer<CFRunLoopSourceContext>) ``` |
| To | ``` func CFRunLoopSourceGetContext(_ source: CFRunLoopSource!, _ context: UnsafeMutablePointer<CFRunLoopSourceContext>) ``` |

Modified CFRunLoopTimerCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFRunLoopTimerCallBack = CFunctionPointer<((CFRunLoopTimer!, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFRunLoopTimerCallBack = CFunctionPointer<((CFRunLoopTimer!, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CFRunLoopTimerCreate(CFAllocator!, CFAbsoluteTime, CFTimeInterval, CFOptionFlags, CFIndex, CFRunLoopTimerCallBack, UnsafeMutablePointer<CFRunLoopTimerContext>) -> CFRunLoopTimer!

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopTimerCreate(_ allocator: CFAllocator!, _ fireDate: CFAbsoluteTime, _ interval: CFTimeInterval, _ flags: CFOptionFlags, _ order: CFIndex, _ callout: CFRunLoopTimerCallBack, _ context: UnsafePointer<CFRunLoopTimerContext>) -> CFRunLoopTimer! ``` |
| To | ``` func CFRunLoopTimerCreate(_ allocator: CFAllocator!, _ fireDate: CFAbsoluteTime, _ interval: CFTimeInterval, _ flags: CFOptionFlags, _ order: CFIndex, _ callout: CFRunLoopTimerCallBack, _ context: UnsafeMutablePointer<CFRunLoopTimerContext>) -> CFRunLoopTimer! ``` |

Modified CFRunLoopTimerCreateWithHandler(CFAllocator!, CFAbsoluteTime, CFTimeInterval, CFOptionFlags, CFIndex,((CFRunLoopTimer!) -> Void)!) -> CFRunLoopTimer!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CFRunLoopTimerGetContext(CFRunLoopTimer!, UnsafeMutablePointer<CFRunLoopTimerContext>)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopTimerGetContext(_ timer: CFRunLoopTimer!, _ context: UnsafePointer<CFRunLoopTimerContext>) ``` |
| To | ``` func CFRunLoopTimerGetContext(_ timer: CFRunLoopTimer!, _ context: UnsafeMutablePointer<CFRunLoopTimerContext>) ``` |

Modified CFRunLoopTimerGetTolerance(CFRunLoopTimer!) -> CFTimeInterval

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CFRunLoopTimerSetTolerance(CFRunLoopTimer!, CFTimeInterval)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CFSetAddValue(CFMutableSet!, UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFSetAddValue(_ theSet: CFMutableSet!, _ value: ConstUnsafePointer<()>) ``` |
| To | ``` func CFSetAddValue(_ theSet: CFMutableSet!, _ value: UnsafePointer<Void>) ``` |

Modified CFSetApplierFunction

|  | Declaration |
| --- | --- |
| From | ``` typealias CFSetApplierFunction = CFunctionPointer<((ConstUnsafePointer<()>, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFSetApplierFunction = CFunctionPointer<((UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CFSetApplyFunction(CFSet!, CFSetApplierFunction, UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFSetApplyFunction(_ theSet: CFSet!, _ applier: CFSetApplierFunction, _ context: UnsafePointer<()>) ``` |
| To | ``` func CFSetApplyFunction(_ theSet: CFSet!, _ applier: CFSetApplierFunction, _ context: UnsafeMutablePointer<Void>) ``` |

Modified CFSetContainsValue(CFSet!, UnsafePointer<Void>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFSetContainsValue(_ theSet: CFSet!, _ value: ConstUnsafePointer<()>) -> Boolean ``` |
| To | ``` func CFSetContainsValue(_ theSet: CFSet!, _ value: UnsafePointer<Void>) -> Boolean ``` |

Modified CFSetCopyDescriptionCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFSetCopyDescriptionCallBack = CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> ``` |
| To | ``` typealias CFSetCopyDescriptionCallBack = CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |

Modified CFSetCreate(CFAllocator!, UnsafeMutablePointer<UnsafePointer<Void>>, CFIndex, UnsafePointer<CFSetCallBacks>) -> CFSet!

|  | Declaration |
| --- | --- |
| From | ``` func CFSetCreate(_ allocator: CFAllocator!, _ values: UnsafePointer<ConstUnsafePointer<()>>, _ numValues: CFIndex, _ callBacks: ConstUnsafePointer<CFSetCallBacks>) -> CFSet! ``` |
| To | ``` func CFSetCreate(_ allocator: CFAllocator!, _ values: UnsafeMutablePointer<UnsafePointer<Void>>, _ numValues: CFIndex, _ callBacks: UnsafePointer<CFSetCallBacks>) -> CFSet! ``` |

Modified CFSetCreateMutable(CFAllocator!, CFIndex, UnsafePointer<CFSetCallBacks>) -> CFMutableSet!

|  | Declaration |
| --- | --- |
| From | ``` func CFSetCreateMutable(_ allocator: CFAllocator!, _ capacity: CFIndex, _ callBacks: ConstUnsafePointer<CFSetCallBacks>) -> CFMutableSet! ``` |
| To | ``` func CFSetCreateMutable(_ allocator: CFAllocator!, _ capacity: CFIndex, _ callBacks: UnsafePointer<CFSetCallBacks>) -> CFMutableSet! ``` |

Modified CFSetEqualCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFSetEqualCallBack = CFunctionPointer<((ConstUnsafePointer<()>, ConstUnsafePointer<()>) -> Boolean)> ``` |
| To | ``` typealias CFSetEqualCallBack = CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)> ``` |

Modified CFSetGetCountOfValue(CFSet!, UnsafePointer<Void>) -> CFIndex

|  | Declaration |
| --- | --- |
| From | ``` func CFSetGetCountOfValue(_ theSet: CFSet!, _ value: ConstUnsafePointer<()>) -> CFIndex ``` |
| To | ``` func CFSetGetCountOfValue(_ theSet: CFSet!, _ value: UnsafePointer<Void>) -> CFIndex ``` |

Modified CFSetGetValue(CFSet!, UnsafePointer<Void>) -> UnsafePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func CFSetGetValue(_ theSet: CFSet!, _ value: ConstUnsafePointer<()>) -> ConstUnsafePointer<()> ``` |
| To | ``` func CFSetGetValue(_ theSet: CFSet!, _ value: UnsafePointer<Void>) -> UnsafePointer<Void> ``` |

Modified CFSetGetValueIfPresent(CFSet!, UnsafePointer<Void>, UnsafeMutablePointer<UnsafePointer<Void>>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFSetGetValueIfPresent(_ theSet: CFSet!, _ candidate: ConstUnsafePointer<()>, _ value: UnsafePointer<ConstUnsafePointer<()>>) -> Boolean ``` |
| To | ``` func CFSetGetValueIfPresent(_ theSet: CFSet!, _ candidate: UnsafePointer<Void>, _ value: UnsafeMutablePointer<UnsafePointer<Void>>) -> Boolean ``` |

Modified CFSetGetValues(CFSet!, UnsafeMutablePointer<UnsafePointer<Void>>)

|  | Declaration |
| --- | --- |
| From | ``` func CFSetGetValues(_ theSet: CFSet!, _ values: UnsafePointer<ConstUnsafePointer<()>>) ``` |
| To | ``` func CFSetGetValues(_ theSet: CFSet!, _ values: UnsafeMutablePointer<UnsafePointer<Void>>) ``` |

Modified CFSetHashCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFSetHashCallBack = CFunctionPointer<((ConstUnsafePointer<()>) -> CFHashCode)> ``` |
| To | ``` typealias CFSetHashCallBack = CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)> ``` |

Modified CFSetReleaseCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFSetReleaseCallBack = CFunctionPointer<((CFAllocator!, ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFSetReleaseCallBack = CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> Void)> ``` |

Modified CFSetRemoveValue(CFMutableSet!, UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFSetRemoveValue(_ theSet: CFMutableSet!, _ value: ConstUnsafePointer<()>) ``` |
| To | ``` func CFSetRemoveValue(_ theSet: CFMutableSet!, _ value: UnsafePointer<Void>) ``` |

Modified CFSetReplaceValue(CFMutableSet!, UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFSetReplaceValue(_ theSet: CFMutableSet!, _ value: ConstUnsafePointer<()>) ``` |
| To | ``` func CFSetReplaceValue(_ theSet: CFMutableSet!, _ value: UnsafePointer<Void>) ``` |

Modified CFSetRetainCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFSetRetainCallBack = CFunctionPointer<((CFAllocator!, ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)> ``` |
| To | ``` typealias CFSetRetainCallBack = CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |

Modified CFSetSetValue(CFMutableSet!, UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFSetSetValue(_ theSet: CFMutableSet!, _ value: ConstUnsafePointer<()>) ``` |
| To | ``` func CFSetSetValue(_ theSet: CFMutableSet!, _ value: UnsafePointer<Void>) ``` |

Modified CFSocketCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFSocketCallBack = CFunctionPointer<((CFSocket!, CFSocketCallBackType, CFData!, ConstUnsafePointer<()>, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFSocketCallBack = CFunctionPointer<((CFSocket!, CFSocketCallBackType, CFData!, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CFSocketCopyRegisteredSocketSignature(UnsafePointer<CFSocketSignature>, CFTimeInterval, CFString!, UnsafeMutablePointer<CFSocketSignature>, UnsafeMutablePointer<Unmanaged<CFData>?>) -> CFSocketError

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketCopyRegisteredSocketSignature(_ nameServerSignature: ConstUnsafePointer<CFSocketSignature>, _ timeout: CFTimeInterval, _ name: CFString!, _ signature: UnsafePointer<CFSocketSignature>, _ nameServerAddress: UnsafePointer<Unmanaged<CFData>?>) -> CFSocketError ``` |
| To | ``` func CFSocketCopyRegisteredSocketSignature(_ nameServerSignature: UnsafePointer<CFSocketSignature>, _ timeout: CFTimeInterval, _ name: CFString!, _ signature: UnsafeMutablePointer<CFSocketSignature>, _ nameServerAddress: UnsafeMutablePointer<Unmanaged<CFData>?>) -> CFSocketError ``` |

Modified CFSocketCopyRegisteredValue(UnsafePointer<CFSocketSignature>, CFTimeInterval, CFString!, UnsafeMutablePointer<Unmanaged<CFPropertyList>?>, UnsafeMutablePointer<Unmanaged<CFData>?>) -> CFSocketError

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketCopyRegisteredValue(_ nameServerSignature: ConstUnsafePointer<CFSocketSignature>, _ timeout: CFTimeInterval, _ name: CFString!, _ value: UnsafePointer<Unmanaged<CFPropertyListRef>?>, _ nameServerAddress: UnsafePointer<Unmanaged<CFData>?>) -> CFSocketError ``` |
| To | ``` func CFSocketCopyRegisteredValue(_ nameServerSignature: UnsafePointer<CFSocketSignature>, _ timeout: CFTimeInterval, _ name: CFString!, _ value: UnsafeMutablePointer<Unmanaged<CFPropertyList>?>, _ nameServerAddress: UnsafeMutablePointer<Unmanaged<CFData>?>) -> CFSocketError ``` |

Modified CFSocketCreate(CFAllocator!, Int32, Int32, Int32, CFOptionFlags, CFSocketCallBack, UnsafePointer<CFSocketContext>) -> CFSocket!

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketCreate(_ allocator: CFAllocator!, _ protocolFamily: Int32, _ socketType: Int32, _ `protocol`: Int32, _ callBackTypes: CFOptionFlags, _ callout: CFSocketCallBack, _ context: ConstUnsafePointer<CFSocketContext>) -> CFSocket! ``` |
| To | ``` func CFSocketCreate(_ allocator: CFAllocator!, _ protocolFamily: Int32, _ socketType: Int32, _ `protocol`: Int32, _ callBackTypes: CFOptionFlags, _ callout: CFSocketCallBack, _ context: UnsafePointer<CFSocketContext>) -> CFSocket! ``` |

Modified CFSocketCreateConnectedToSocketSignature(CFAllocator!, UnsafePointer<CFSocketSignature>, CFOptionFlags, CFSocketCallBack, UnsafePointer<CFSocketContext>, CFTimeInterval) -> CFSocket!

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketCreateConnectedToSocketSignature(_ allocator: CFAllocator!, _ signature: ConstUnsafePointer<CFSocketSignature>, _ callBackTypes: CFOptionFlags, _ callout: CFSocketCallBack, _ context: ConstUnsafePointer<CFSocketContext>, _ timeout: CFTimeInterval) -> CFSocket! ``` |
| To | ``` func CFSocketCreateConnectedToSocketSignature(_ allocator: CFAllocator!, _ signature: UnsafePointer<CFSocketSignature>, _ callBackTypes: CFOptionFlags, _ callout: CFSocketCallBack, _ context: UnsafePointer<CFSocketContext>, _ timeout: CFTimeInterval) -> CFSocket! ``` |

Modified CFSocketCreateWithNative(CFAllocator!, CFSocketNativeHandle, CFOptionFlags, CFSocketCallBack, UnsafePointer<CFSocketContext>) -> CFSocket!

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketCreateWithNative(_ allocator: CFAllocator!, _ sock: CFSocketNativeHandle, _ callBackTypes: CFOptionFlags, _ callout: CFSocketCallBack, _ context: ConstUnsafePointer<CFSocketContext>) -> CFSocket! ``` |
| To | ``` func CFSocketCreateWithNative(_ allocator: CFAllocator!, _ sock: CFSocketNativeHandle, _ callBackTypes: CFOptionFlags, _ callout: CFSocketCallBack, _ context: UnsafePointer<CFSocketContext>) -> CFSocket! ``` |

Modified CFSocketCreateWithSocketSignature(CFAllocator!, UnsafePointer<CFSocketSignature>, CFOptionFlags, CFSocketCallBack, UnsafePointer<CFSocketContext>) -> CFSocket!

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketCreateWithSocketSignature(_ allocator: CFAllocator!, _ signature: ConstUnsafePointer<CFSocketSignature>, _ callBackTypes: CFOptionFlags, _ callout: CFSocketCallBack, _ context: ConstUnsafePointer<CFSocketContext>) -> CFSocket! ``` |
| To | ``` func CFSocketCreateWithSocketSignature(_ allocator: CFAllocator!, _ signature: UnsafePointer<CFSocketSignature>, _ callBackTypes: CFOptionFlags, _ callout: CFSocketCallBack, _ context: UnsafePointer<CFSocketContext>) -> CFSocket! ``` |

Modified CFSocketGetContext(CFSocket!, UnsafeMutablePointer<CFSocketContext>)

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketGetContext(_ s: CFSocket!, _ context: UnsafePointer<CFSocketContext>) ``` |
| To | ``` func CFSocketGetContext(_ s: CFSocket!, _ context: UnsafeMutablePointer<CFSocketContext>) ``` |

Modified CFSocketRegisterSocketSignature(UnsafePointer<CFSocketSignature>, CFTimeInterval, CFString!, UnsafePointer<CFSocketSignature>) -> CFSocketError

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketRegisterSocketSignature(_ nameServerSignature: ConstUnsafePointer<CFSocketSignature>, _ timeout: CFTimeInterval, _ name: CFString!, _ signature: ConstUnsafePointer<CFSocketSignature>) -> CFSocketError ``` |
| To | ``` func CFSocketRegisterSocketSignature(_ nameServerSignature: UnsafePointer<CFSocketSignature>, _ timeout: CFTimeInterval, _ name: CFString!, _ signature: UnsafePointer<CFSocketSignature>) -> CFSocketError ``` |

Modified CFSocketRegisterValue(UnsafePointer<CFSocketSignature>, CFTimeInterval, CFString!, CFPropertyList!) -> CFSocketError

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketRegisterValue(_ nameServerSignature: ConstUnsafePointer<CFSocketSignature>, _ timeout: CFTimeInterval, _ name: CFString!, _ value: CFPropertyListRef!) -> CFSocketError ``` |
| To | ``` func CFSocketRegisterValue(_ nameServerSignature: UnsafePointer<CFSocketSignature>, _ timeout: CFTimeInterval, _ name: CFString!, _ value: CFPropertyList!) -> CFSocketError ``` |

Modified CFSocketUnregister(UnsafePointer<CFSocketSignature>, CFTimeInterval, CFString!) -> CFSocketError

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketUnregister(_ nameServerSignature: ConstUnsafePointer<CFSocketSignature>, _ timeout: CFTimeInterval, _ name: CFString!) -> CFSocketError ``` |
| To | ``` func CFSocketUnregister(_ nameServerSignature: UnsafePointer<CFSocketSignature>, _ timeout: CFTimeInterval, _ name: CFString!) -> CFSocketError ``` |

Modified CFStreamCreateBoundPair(CFAllocator!, UnsafeMutablePointer<Unmanaged<CFReadStream>?>, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>, CFIndex)

|  | Declaration |
| --- | --- |
| From | ``` func CFStreamCreateBoundPair(_ alloc: CFAllocator!, _ readStream: UnsafePointer<Unmanaged<CFReadStream>?>, _ writeStream: UnsafePointer<Unmanaged<CFWriteStream>?>, _ transferBufferSize: CFIndex) ``` |
| To | ``` func CFStreamCreateBoundPair(_ alloc: CFAllocator!, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>, _ transferBufferSize: CFIndex) ``` |

Modified CFStreamCreatePairWithPeerSocketSignature(CFAllocator!, UnsafePointer<CFSocketSignature>, UnsafeMutablePointer<Unmanaged<CFReadStream>?>, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>)

|  | Declaration |
| --- | --- |
| From | ``` func CFStreamCreatePairWithPeerSocketSignature(_ alloc: CFAllocator!, _ signature: ConstUnsafePointer<CFSocketSignature>, _ readStream: UnsafePointer<Unmanaged<CFReadStream>?>, _ writeStream: UnsafePointer<Unmanaged<CFWriteStream>?>) ``` |
| To | ``` func CFStreamCreatePairWithPeerSocketSignature(_ alloc: CFAllocator!, _ signature: UnsafePointer<CFSocketSignature>, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>) ``` |

Modified CFStreamCreatePairWithSocket(CFAllocator!, CFSocketNativeHandle, UnsafeMutablePointer<Unmanaged<CFReadStream>?>, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>)

|  | Declaration |
| --- | --- |
| From | ``` func CFStreamCreatePairWithSocket(_ alloc: CFAllocator!, _ sock: CFSocketNativeHandle, _ readStream: UnsafePointer<Unmanaged<CFReadStream>?>, _ writeStream: UnsafePointer<Unmanaged<CFWriteStream>?>) ``` |
| To | ``` func CFStreamCreatePairWithSocket(_ alloc: CFAllocator!, _ sock: CFSocketNativeHandle, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>) ``` |

Modified CFStreamCreatePairWithSocketToHost(CFAllocator!, CFString!, UInt32, UnsafeMutablePointer<Unmanaged<CFReadStream>?>, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>)

|  | Declaration |
| --- | --- |
| From | ``` func CFStreamCreatePairWithSocketToHost(_ alloc: CFAllocator!, _ host: CFString!, _ port: UInt32, _ readStream: UnsafePointer<Unmanaged<CFReadStream>?>, _ writeStream: UnsafePointer<Unmanaged<CFWriteStream>?>) ``` |
| To | ``` func CFStreamCreatePairWithSocketToHost(_ alloc: CFAllocator!, _ host: CFString!, _ port: UInt32, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>) ``` |

Modified CFStringAppendCString(CFMutableString!, UnsafePointer<Int8>, CFStringEncoding)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringAppendCString(_ theString: CFMutableString!, _ cStr: ConstUnsafePointer<Int8>, _ encoding: CFStringEncoding) ``` |
| To | ``` func CFStringAppendCString(_ theString: CFMutableString!, _ cStr: UnsafePointer<Int8>, _ encoding: CFStringEncoding) ``` |

Modified CFStringAppendCharacters(CFMutableString!, UnsafePointer<UniChar>, CFIndex)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringAppendCharacters(_ theString: CFMutableString!, _ chars: ConstUnsafePointer<UniChar>, _ numChars: CFIndex) ``` |
| To | ``` func CFStringAppendCharacters(_ theString: CFMutableString!, _ chars: UnsafePointer<UniChar>, _ numChars: CFIndex) ``` |

Modified CFStringCompareWithOptionsAndLocale(CFString!, CFString!, CFRange, CFStringCompareFlags, CFLocale!) -> CFComparisonResult

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFStringCreateMutableWithExternalCharactersNoCopy(CFAllocator!, UnsafeMutablePointer<UniChar>, CFIndex, CFIndex, CFAllocator!) -> CFMutableString!

|  | Declaration |
| --- | --- |
| From | ``` func CFStringCreateMutableWithExternalCharactersNoCopy(_ alloc: CFAllocator!, _ chars: UnsafePointer<UniChar>, _ numChars: CFIndex, _ capacity: CFIndex, _ externalCharactersAllocator: CFAllocator!) -> CFMutableString! ``` |
| To | ``` func CFStringCreateMutableWithExternalCharactersNoCopy(_ alloc: CFAllocator!, _ chars: UnsafeMutablePointer<UniChar>, _ numChars: CFIndex, _ capacity: CFIndex, _ externalCharactersAllocator: CFAllocator!) -> CFMutableString! ``` |

Modified CFStringCreateWithBytes(CFAllocator!, UnsafePointer<UInt8>, CFIndex, CFStringEncoding, Boolean) -> CFString!

|  | Declaration |
| --- | --- |
| From | ``` func CFStringCreateWithBytes(_ alloc: CFAllocator!, _ bytes: ConstUnsafePointer<UInt8>, _ numBytes: CFIndex, _ encoding: CFStringEncoding, _ isExternalRepresentation: Boolean) -> CFString! ``` |
| To | ``` func CFStringCreateWithBytes(_ alloc: CFAllocator!, _ bytes: UnsafePointer<UInt8>, _ numBytes: CFIndex, _ encoding: CFStringEncoding, _ isExternalRepresentation: Boolean) -> CFString! ``` |

Modified CFStringCreateWithBytesNoCopy(CFAllocator!, UnsafePointer<UInt8>, CFIndex, CFStringEncoding, Boolean, CFAllocator!) -> CFString!

|  | Declaration |
| --- | --- |
| From | ``` func CFStringCreateWithBytesNoCopy(_ alloc: CFAllocator!, _ bytes: ConstUnsafePointer<UInt8>, _ numBytes: CFIndex, _ encoding: CFStringEncoding, _ isExternalRepresentation: Boolean, _ contentsDeallocator: CFAllocator!) -> CFString! ``` |
| To | ``` func CFStringCreateWithBytesNoCopy(_ alloc: CFAllocator!, _ bytes: UnsafePointer<UInt8>, _ numBytes: CFIndex, _ encoding: CFStringEncoding, _ isExternalRepresentation: Boolean, _ contentsDeallocator: CFAllocator!) -> CFString! ``` |

Modified CFStringCreateWithCString(CFAllocator!, UnsafePointer<Int8>, CFStringEncoding) -> CFString!

|  | Declaration |
| --- | --- |
| From | ``` func CFStringCreateWithCString(_ alloc: CFAllocator!, _ cStr: ConstUnsafePointer<Int8>, _ encoding: CFStringEncoding) -> CFString! ``` |
| To | ``` func CFStringCreateWithCString(_ alloc: CFAllocator!, _ cStr: UnsafePointer<Int8>, _ encoding: CFStringEncoding) -> CFString! ``` |

Modified CFStringCreateWithCStringNoCopy(CFAllocator!, UnsafePointer<Int8>, CFStringEncoding, CFAllocator!) -> CFString!

|  | Declaration |
| --- | --- |
| From | ``` func CFStringCreateWithCStringNoCopy(_ alloc: CFAllocator!, _ cStr: ConstUnsafePointer<Int8>, _ encoding: CFStringEncoding, _ contentsDeallocator: CFAllocator!) -> CFString! ``` |
| To | ``` func CFStringCreateWithCStringNoCopy(_ alloc: CFAllocator!, _ cStr: UnsafePointer<Int8>, _ encoding: CFStringEncoding, _ contentsDeallocator: CFAllocator!) -> CFString! ``` |

Modified CFStringCreateWithCharacters(CFAllocator!, UnsafePointer<UniChar>, CFIndex) -> CFString!

|  | Declaration |
| --- | --- |
| From | ``` func CFStringCreateWithCharacters(_ alloc: CFAllocator!, _ chars: ConstUnsafePointer<UniChar>, _ numChars: CFIndex) -> CFString! ``` |
| To | ``` func CFStringCreateWithCharacters(_ alloc: CFAllocator!, _ chars: UnsafePointer<UniChar>, _ numChars: CFIndex) -> CFString! ``` |

Modified CFStringCreateWithCharactersNoCopy(CFAllocator!, UnsafePointer<UniChar>, CFIndex, CFAllocator!) -> CFString!

|  | Declaration |
| --- | --- |
| From | ``` func CFStringCreateWithCharactersNoCopy(_ alloc: CFAllocator!, _ chars: ConstUnsafePointer<UniChar>, _ numChars: CFIndex, _ contentsDeallocator: CFAllocator!) -> CFString! ``` |
| To | ``` func CFStringCreateWithCharactersNoCopy(_ alloc: CFAllocator!, _ chars: UnsafePointer<UniChar>, _ numChars: CFIndex, _ contentsDeallocator: CFAllocator!) -> CFString! ``` |

Modified CFStringCreateWithFileSystemRepresentation(CFAllocator!, UnsafePointer<Int8>) -> CFString!

|  | Declaration |
| --- | --- |
| From | ``` func CFStringCreateWithFileSystemRepresentation(_ alloc: CFAllocator!, _ buffer: ConstUnsafePointer<Int8>) -> CFString! ``` |
| To | ``` func CFStringCreateWithFileSystemRepresentation(_ alloc: CFAllocator!, _ buffer: UnsafePointer<Int8>) -> CFString! ``` |

Modified CFStringFindCharacterFromSet(CFString!, CFCharacterSet!, CFRange, CFStringCompareFlags, UnsafeMutablePointer<CFRange>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFStringFindCharacterFromSet(_ theString: CFString!, _ theSet: CFCharacterSet!, _ rangeToSearch: CFRange, _ searchOptions: CFStringCompareFlags, _ result: UnsafePointer<CFRange>) -> Boolean ``` |
| To | ``` func CFStringFindCharacterFromSet(_ theString: CFString!, _ theSet: CFCharacterSet!, _ rangeToSearch: CFRange, _ searchOptions: CFStringCompareFlags, _ result: UnsafeMutablePointer<CFRange>) -> Boolean ``` |

Modified CFStringFindWithOptions(CFString!, CFString!, CFRange, CFStringCompareFlags, UnsafeMutablePointer<CFRange>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFStringFindWithOptions(_ theString: CFString!, _ stringToFind: CFString!, _ rangeToSearch: CFRange, _ searchOptions: CFStringCompareFlags, _ result: UnsafePointer<CFRange>) -> Boolean ``` |
| To | ``` func CFStringFindWithOptions(_ theString: CFString!, _ stringToFind: CFString!, _ rangeToSearch: CFRange, _ searchOptions: CFStringCompareFlags, _ result: UnsafeMutablePointer<CFRange>) -> Boolean ``` |

Modified CFStringFindWithOptionsAndLocale(CFString!, CFString!, CFRange, CFStringCompareFlags, CFLocale!, UnsafeMutablePointer<CFRange>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFStringFindWithOptionsAndLocale(_ theString: CFString!, _ stringToFind: CFString!, _ rangeToSearch: CFRange, _ searchOptions: CFStringCompareFlags, _ locale: CFLocale!, _ result: UnsafePointer<CFRange>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFStringFindWithOptionsAndLocale(_ theString: CFString!, _ stringToFind: CFString!, _ rangeToSearch: CFRange, _ searchOptions: CFStringCompareFlags, _ locale: CFLocale!, _ result: UnsafeMutablePointer<CFRange>) -> Boolean ``` | OS X 10.5 |

Modified CFStringFold(CFMutableString!, CFStringCompareFlags, CFLocale!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFStringGetBytes(CFString!, CFRange, CFStringEncoding, UInt8, Boolean, UnsafeMutablePointer<UInt8>, CFIndex, UnsafeMutablePointer<CFIndex>) -> CFIndex

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetBytes(_ theString: CFString!, _ range: CFRange, _ encoding: CFStringEncoding, _ lossByte: UInt8, _ isExternalRepresentation: Boolean, _ buffer: UnsafePointer<UInt8>, _ maxBufLen: CFIndex, _ usedBufLen: UnsafePointer<CFIndex>) -> CFIndex ``` |
| To | ``` func CFStringGetBytes(_ theString: CFString!, _ range: CFRange, _ encoding: CFStringEncoding, _ lossByte: UInt8, _ isExternalRepresentation: Boolean, _ buffer: UnsafeMutablePointer<UInt8>, _ maxBufLen: CFIndex, _ usedBufLen: UnsafeMutablePointer<CFIndex>) -> CFIndex ``` |

Modified CFStringGetCString(CFString!, UnsafeMutablePointer<Int8>, CFIndex, CFStringEncoding) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetCString(_ theString: CFString!, _ buffer: UnsafePointer<Int8>, _ bufferSize: CFIndex, _ encoding: CFStringEncoding) -> Boolean ``` |
| To | ``` func CFStringGetCString(_ theString: CFString!, _ buffer: UnsafeMutablePointer<Int8>, _ bufferSize: CFIndex, _ encoding: CFStringEncoding) -> Boolean ``` |

Modified CFStringGetCStringPtr(CFString!, CFStringEncoding) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetCStringPtr(_ theString: CFString!, _ encoding: CFStringEncoding) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func CFStringGetCStringPtr(_ theString: CFString!, _ encoding: CFStringEncoding) -> UnsafePointer<Int8> ``` |

Modified CFStringGetCharacterFromInlineBuffer(UnsafeMutablePointer<CFStringInlineBuffer>, CFIndex) -> UniChar

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetCharacterFromInlineBuffer(_ buf: UnsafePointer<CFStringInlineBuffer>, _ idx: CFIndex) -> UniChar ``` |
| To | ``` func CFStringGetCharacterFromInlineBuffer(_ buf: UnsafeMutablePointer<CFStringInlineBuffer>, _ idx: CFIndex) -> UniChar ``` |

Modified CFStringGetCharacters(CFString!, CFRange, UnsafeMutablePointer<UniChar>)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetCharacters(_ theString: CFString!, _ range: CFRange, _ buffer: UnsafePointer<UniChar>) ``` |
| To | ``` func CFStringGetCharacters(_ theString: CFString!, _ range: CFRange, _ buffer: UnsafeMutablePointer<UniChar>) ``` |

Modified CFStringGetCharactersPtr(CFString!) -> UnsafePointer<UniChar>

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetCharactersPtr(_ theString: CFString!) -> ConstUnsafePointer<UniChar> ``` |
| To | ``` func CFStringGetCharactersPtr(_ theString: CFString!) -> UnsafePointer<UniChar> ``` |

Modified CFStringGetFileSystemRepresentation(CFString!, UnsafeMutablePointer<Int8>, CFIndex) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetFileSystemRepresentation(_ string: CFString!, _ buffer: UnsafePointer<Int8>, _ maxBufLen: CFIndex) -> Boolean ``` |
| To | ``` func CFStringGetFileSystemRepresentation(_ string: CFString!, _ buffer: UnsafeMutablePointer<Int8>, _ maxBufLen: CFIndex) -> Boolean ``` |

Modified CFStringGetHyphenationLocationBeforeIndex(CFString!, CFIndex, CFRange, CFOptionFlags, CFLocale!, UnsafeMutablePointer<UTF32Char>) -> CFIndex

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFStringGetHyphenationLocationBeforeIndex(_ string: CFString!, _ location: CFIndex, _ limitRange: CFRange, _ options: CFOptionFlags, _ locale: CFLocale!, _ character: UnsafePointer<UTF32Char>) -> CFIndex ``` | OS X 10.10 |
| To | ``` func CFStringGetHyphenationLocationBeforeIndex(_ string: CFString!, _ location: CFIndex, _ limitRange: CFRange, _ options: CFOptionFlags, _ locale: CFLocale!, _ character: UnsafeMutablePointer<UTF32Char>) -> CFIndex ``` | OS X 10.7 |

Modified CFStringGetLineBounds(CFString!, CFRange, UnsafeMutablePointer<CFIndex>, UnsafeMutablePointer<CFIndex>, UnsafeMutablePointer<CFIndex>)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetLineBounds(_ theString: CFString!, _ range: CFRange, _ lineBeginIndex: UnsafePointer<CFIndex>, _ lineEndIndex: UnsafePointer<CFIndex>, _ contentsEndIndex: UnsafePointer<CFIndex>) ``` |
| To | ``` func CFStringGetLineBounds(_ theString: CFString!, _ range: CFRange, _ lineBeginIndex: UnsafeMutablePointer<CFIndex>, _ lineEndIndex: UnsafeMutablePointer<CFIndex>, _ contentsEndIndex: UnsafeMutablePointer<CFIndex>) ``` |

Modified CFStringGetListOfAvailableEncodings() -> UnsafePointer<CFStringEncoding>

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetListOfAvailableEncodings() -> ConstUnsafePointer<CFStringEncoding> ``` |
| To | ``` func CFStringGetListOfAvailableEncodings() -> UnsafePointer<CFStringEncoding> ``` |

Modified CFStringGetParagraphBounds(CFString!, CFRange, UnsafeMutablePointer<CFIndex>, UnsafeMutablePointer<CFIndex>, UnsafeMutablePointer<CFIndex>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFStringGetParagraphBounds(_ string: CFString!, _ range: CFRange, _ parBeginIndex: UnsafePointer<CFIndex>, _ parEndIndex: UnsafePointer<CFIndex>, _ contentsEndIndex: UnsafePointer<CFIndex>) ``` | OS X 10.10 |
| To | ``` func CFStringGetParagraphBounds(_ string: CFString!, _ range: CFRange, _ parBeginIndex: UnsafeMutablePointer<CFIndex>, _ parEndIndex: UnsafeMutablePointer<CFIndex>, _ contentsEndIndex: UnsafeMutablePointer<CFIndex>) ``` | OS X 10.5 |

Modified CFStringGetSurrogatePairForLongCharacter(UTF32Char, UnsafeMutablePointer<UniChar>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetSurrogatePairForLongCharacter(_ character: UTF32Char, _ surrogates: UnsafePointer<UniChar>) -> Boolean ``` |
| To | ``` func CFStringGetSurrogatePairForLongCharacter(_ character: UTF32Char, _ surrogates: UnsafeMutablePointer<UniChar>) -> Boolean ``` |

Modified CFStringInitInlineBuffer(CFString!, UnsafeMutablePointer<CFStringInlineBuffer>, CFRange)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringInitInlineBuffer(_ str: CFString!, _ buf: UnsafePointer<CFStringInlineBuffer>, _ range: CFRange) ``` |
| To | ``` func CFStringInitInlineBuffer(_ str: CFString!, _ buf: UnsafeMutablePointer<CFStringInlineBuffer>, _ range: CFRange) ``` |

Modified CFStringIsHyphenationAvailableForLocale(CFLocale!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CFStringSetExternalCharactersNoCopy(CFMutableString!, UnsafeMutablePointer<UniChar>, CFIndex, CFIndex)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringSetExternalCharactersNoCopy(_ theString: CFMutableString!, _ chars: UnsafePointer<UniChar>, _ length: CFIndex, _ capacity: CFIndex) ``` |
| To | ``` func CFStringSetExternalCharactersNoCopy(_ theString: CFMutableString!, _ chars: UnsafeMutablePointer<UniChar>, _ length: CFIndex, _ capacity: CFIndex) ``` |

Modified CFStringTokenizerAdvanceToNextToken(CFStringTokenizer!) -> CFStringTokenizerTokenType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFStringTokenizerCopyBestStringLanguage(CFString!, CFRange) -> CFString!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFStringTokenizerCopyCurrentTokenAttribute(CFStringTokenizer!, CFOptionFlags) -> AnyObject!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFStringTokenizerCreate(CFAllocator!, CFString!, CFRange, CFOptionFlags, CFLocale!) -> CFStringTokenizer!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFStringTokenizerGetCurrentSubTokens(CFStringTokenizer!, UnsafeMutablePointer<CFRange>, CFIndex, CFMutableArray!) -> CFIndex

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFStringTokenizerGetCurrentSubTokens(_ tokenizer: CFStringTokenizer!, _ ranges: UnsafePointer<CFRange>, _ maxRangeLength: CFIndex, _ derivedSubTokens: CFMutableArray!) -> CFIndex ``` | OS X 10.10 |
| To | ``` func CFStringTokenizerGetCurrentSubTokens(_ tokenizer: CFStringTokenizer!, _ ranges: UnsafeMutablePointer<CFRange>, _ maxRangeLength: CFIndex, _ derivedSubTokens: CFMutableArray!) -> CFIndex ``` | OS X 10.5 |

Modified CFStringTokenizerGetCurrentTokenRange(CFStringTokenizer!) -> CFRange

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFStringTokenizerGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFStringTokenizerGoToTokenAtIndex(CFStringTokenizer!, CFIndex) -> CFStringTokenizerTokenType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFStringTokenizerSetString(CFStringTokenizer!, CFString!, CFRange)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFStringTransform(CFMutableString!, UnsafeMutablePointer<CFRange>, CFString!, Boolean) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFStringTransform(_ string: CFMutableString!, _ range: UnsafePointer<CFRange>, _ transform: CFString!, _ reverse: Boolean) -> Boolean ``` |
| To | ``` func CFStringTransform(_ string: CFMutableString!, _ range: UnsafeMutablePointer<CFRange>, _ transform: CFString!, _ reverse: Boolean) -> Boolean ``` |

Modified CFTimeZoneCopyLocalizedName(CFTimeZone!, CFTimeZoneNameStyle, CFLocale!) -> CFString!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFTimeZoneGetDaylightSavingTimeOffset(CFTimeZone!, CFAbsoluteTime) -> CFTimeInterval

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFTimeZoneGetNextDaylightSavingTimeTransition(CFTimeZone!, CFAbsoluteTime) -> CFAbsoluteTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFTreeApplierFunction

|  | Declaration |
| --- | --- |
| From | ``` typealias CFTreeApplierFunction = CFunctionPointer<((ConstUnsafePointer<()>, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFTreeApplierFunction = CFunctionPointer<((UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CFTreeApplyFunctionToChildren(CFTree!, CFTreeApplierFunction, UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFTreeApplyFunctionToChildren(_ tree: CFTree!, _ applier: CFTreeApplierFunction, _ context: UnsafePointer<()>) ``` |
| To | ``` func CFTreeApplyFunctionToChildren(_ tree: CFTree!, _ applier: CFTreeApplierFunction, _ context: UnsafeMutablePointer<Void>) ``` |

Modified CFTreeCopyDescriptionCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFTreeCopyDescriptionCallBack = CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> ``` |
| To | ``` typealias CFTreeCopyDescriptionCallBack = CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |

Modified CFTreeCreate(CFAllocator!, UnsafePointer<CFTreeContext>) -> CFTree!

|  | Declaration |
| --- | --- |
| From | ``` func CFTreeCreate(_ allocator: CFAllocator!, _ context: ConstUnsafePointer<CFTreeContext>) -> CFTree! ``` |
| To | ``` func CFTreeCreate(_ allocator: CFAllocator!, _ context: UnsafePointer<CFTreeContext>) -> CFTree! ``` |

Modified CFTreeGetChildren(CFTree!, UnsafeMutablePointer<Unmanaged<CFTree>?>)

|  | Declaration |
| --- | --- |
| From | ``` func CFTreeGetChildren(_ tree: CFTree!, _ children: UnsafePointer<Unmanaged<CFTree>?>) ``` |
| To | ``` func CFTreeGetChildren(_ tree: CFTree!, _ children: UnsafeMutablePointer<Unmanaged<CFTree>?>) ``` |

Modified CFTreeGetContext(CFTree!, UnsafeMutablePointer<CFTreeContext>)

|  | Declaration |
| --- | --- |
| From | ``` func CFTreeGetContext(_ tree: CFTree!, _ context: UnsafePointer<CFTreeContext>) ``` |
| To | ``` func CFTreeGetContext(_ tree: CFTree!, _ context: UnsafeMutablePointer<CFTreeContext>) ``` |

Modified CFTreeReleaseCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFTreeReleaseCallBack = CFunctionPointer<((ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFTreeReleaseCallBack = CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |

Modified CFTreeRetainCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFTreeRetainCallBack = CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)> ``` |
| To | ``` typealias CFTreeRetainCallBack = CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |

Modified CFTreeSetContext(CFTree!, UnsafePointer<CFTreeContext>)

|  | Declaration |
| --- | --- |
| From | ``` func CFTreeSetContext(_ tree: CFTree!, _ context: ConstUnsafePointer<CFTreeContext>) ``` |
| To | ``` func CFTreeSetContext(_ tree: CFTree!, _ context: UnsafePointer<CFTreeContext>) ``` |

Modified CFTreeSortChildren(CFTree!, CFComparatorFunction, UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CFTreeSortChildren(_ tree: CFTree!, _ comparator: CFComparatorFunction, _ context: UnsafePointer<()>) ``` |
| To | ``` func CFTreeSortChildren(_ tree: CFTree!, _ comparator: CFComparatorFunction, _ context: UnsafeMutablePointer<Void>) ``` |

Modified CFURLClearResourcePropertyCache(CFURL!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CFURLClearResourcePropertyCacheForKey(CFURL!, CFString!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CFURLCopyResourcePropertiesForKeys(CFURL!, CFArray!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFURLCopyResourcePropertiesForKeys(_ url: CFURL!, _ keys: CFArray!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` | OS X 10.10 |
| To | ``` func CFURLCopyResourcePropertiesForKeys(_ url: CFURL!, _ keys: CFArray!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` | OS X 10.6 |

Modified CFURLCopyResourcePropertyForKey(CFURL!, CFString!, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFURLCopyResourcePropertyForKey(_ url: CFURL!, _ key: CFString!, _ propertyValueTypeRefPtr: UnsafePointer<()>, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFURLCopyResourcePropertyForKey(_ url: CFURL!, _ key: CFString!, _ propertyValueTypeRefPtr: UnsafeMutablePointer<Void>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean ``` | OS X 10.6 |

Modified CFURLCopyStrictPath(CFURL!, UnsafeMutablePointer<Boolean>) -> CFString!

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCopyStrictPath(_ anURL: CFURL!, _ isAbsolute: UnsafePointer<Boolean>) -> CFString! ``` |
| To | ``` func CFURLCopyStrictPath(_ anURL: CFURL!, _ isAbsolute: UnsafeMutablePointer<Boolean>) -> CFString! ``` |

Modified CFURLCreateAbsoluteURLWithBytes(CFAllocator!, UnsafePointer<UInt8>, CFIndex, CFStringEncoding, CFURL!, Boolean) -> CFURL!

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCreateAbsoluteURLWithBytes(_ alloc: CFAllocator!, _ relativeURLBytes: ConstUnsafePointer<UInt8>, _ length: CFIndex, _ encoding: CFStringEncoding, _ baseURL: CFURL!, _ useCompatibilityMode: Boolean) -> CFURL! ``` |
| To | ``` func CFURLCreateAbsoluteURLWithBytes(_ alloc: CFAllocator!, _ relativeURLBytes: UnsafePointer<UInt8>, _ length: CFIndex, _ encoding: CFStringEncoding, _ baseURL: CFURL!, _ useCompatibilityMode: Boolean) -> CFURL! ``` |

Modified CFURLCreateBookmarkData(CFAllocator!, CFURL!, CFURLBookmarkCreationOptions, CFArray!, CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFURLCreateBookmarkData(_ allocator: CFAllocator!, _ url: CFURL!, _ options: CFURLBookmarkCreationOptions, _ resourcePropertiesToInclude: CFArray!, _ relativeToURL: CFURL!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>! ``` | OS X 10.10 |
| To | ``` func CFURLCreateBookmarkData(_ allocator: CFAllocator!, _ url: CFURL!, _ options: CFURLBookmarkCreationOptions, _ resourcePropertiesToInclude: CFArray!, _ relativeToURL: CFURL!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>! ``` | OS X 10.6 |

Modified CFURLCreateBookmarkDataFromAliasRecord(CFAllocator!, CFData!) -> Unmanaged<CFData>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CFURLCreateBookmarkDataFromFile(CFAllocator!, CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFURLCreateBookmarkDataFromFile(_ allocator: CFAllocator!, _ fileURL: CFURL!, _ errorRef: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>! ``` | OS X 10.10 |
| To | ``` func CFURLCreateBookmarkDataFromFile(_ allocator: CFAllocator!, _ fileURL: CFURL!, _ errorRef: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>! ``` | OS X 10.6 |

Modified CFURLCreateByResolvingBookmarkData(CFAllocator!, CFData!, CFURLBookmarkResolutionOptions, CFURL!, CFArray!, UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFURLCreateByResolvingBookmarkData(_ allocator: CFAllocator!, _ bookmark: CFData!, _ options: CFURLBookmarkResolutionOptions, _ relativeToURL: CFURL!, _ resourcePropertiesToInclude: CFArray!, _ isStale: UnsafePointer<Boolean>, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>! ``` | OS X 10.10 |
| To | ``` func CFURLCreateByResolvingBookmarkData(_ allocator: CFAllocator!, _ bookmark: CFData!, _ options: CFURLBookmarkResolutionOptions, _ relativeToURL: CFURL!, _ resourcePropertiesToInclude: CFArray!, _ isStale: UnsafeMutablePointer<Boolean>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>! ``` | OS X 10.6 |

Modified CFURLCreateFilePathURL(CFAllocator!, CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFURLCreateFilePathURL(_ allocator: CFAllocator!, _ url: CFURL!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>! ``` | OS X 10.10 |
| To | ``` func CFURLCreateFilePathURL(_ allocator: CFAllocator!, _ url: CFURL!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>! ``` | OS X 10.6 |

Modified CFURLCreateFileReferenceURL(CFAllocator!, CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFURLCreateFileReferenceURL(_ allocator: CFAllocator!, _ url: CFURL!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>! ``` | OS X 10.10 |
| To | ``` func CFURLCreateFileReferenceURL(_ allocator: CFAllocator!, _ url: CFURL!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>! ``` | OS X 10.6 |

Modified CFURLCreateFromFileSystemRepresentation(CFAllocator!, UnsafePointer<UInt8>, CFIndex, Boolean) -> CFURL!

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCreateFromFileSystemRepresentation(_ allocator: CFAllocator!, _ buffer: ConstUnsafePointer<UInt8>, _ bufLen: CFIndex, _ isDirectory: Boolean) -> CFURL! ``` |
| To | ``` func CFURLCreateFromFileSystemRepresentation(_ allocator: CFAllocator!, _ buffer: UnsafePointer<UInt8>, _ bufLen: CFIndex, _ isDirectory: Boolean) -> CFURL! ``` |

Modified CFURLCreateFromFileSystemRepresentationRelativeToBase(CFAllocator!, UnsafePointer<UInt8>, CFIndex, Boolean, CFURL!) -> CFURL!

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCreateFromFileSystemRepresentationRelativeToBase(_ allocator: CFAllocator!, _ buffer: ConstUnsafePointer<UInt8>, _ bufLen: CFIndex, _ isDirectory: Boolean, _ baseURL: CFURL!) -> CFURL! ``` |
| To | ``` func CFURLCreateFromFileSystemRepresentationRelativeToBase(_ allocator: CFAllocator!, _ buffer: UnsafePointer<UInt8>, _ bufLen: CFIndex, _ isDirectory: Boolean, _ baseURL: CFURL!) -> CFURL! ``` |

Modified CFURLCreateResourcePropertiesForKeysFromBookmarkData(CFAllocator!, CFArray!, CFData!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CFURLCreateResourcePropertyForKeyFromBookmarkData(CFAllocator!, CFString!, CFData!) -> Unmanaged<AnyObject>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CFURLCreateWithBytes(CFAllocator!, UnsafePointer<UInt8>, CFIndex, CFStringEncoding, CFURL!) -> CFURL!

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCreateWithBytes(_ allocator: CFAllocator!, _ URLBytes: ConstUnsafePointer<UInt8>, _ length: CFIndex, _ encoding: CFStringEncoding, _ baseURL: CFURL!) -> CFURL! ``` |
| To | ``` func CFURLCreateWithBytes(_ allocator: CFAllocator!, _ URLBytes: UnsafePointer<UInt8>, _ length: CFIndex, _ encoding: CFStringEncoding, _ baseURL: CFURL!) -> CFURL! ``` |

Modified CFURLEnumeratorCreateForDirectoryURL(CFAllocator!, CFURL!, CFURLEnumeratorOptions, CFArray!) -> CFURLEnumerator!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CFURLEnumeratorCreateForMountedVolumes(CFAllocator!, CFURLEnumeratorOptions, CFArray!) -> CFURLEnumerator!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CFURLEnumeratorGetDescendentLevel(CFURLEnumerator!) -> CFIndex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CFURLEnumeratorGetNextURL(CFURLEnumerator!, UnsafeMutablePointer<Unmanaged<CFURL>?>, UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFURLEnumeratorResult

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFURLEnumeratorGetNextURL(_ enumerator: CFURLEnumerator!, _ url: UnsafePointer<Unmanaged<CFURL>?>, _ error: UnsafePointer<Unmanaged<CFError>?>) -> CFURLEnumeratorResult ``` | OS X 10.10 |
| To | ``` func CFURLEnumeratorGetNextURL(_ enumerator: CFURLEnumerator!, _ url: UnsafeMutablePointer<Unmanaged<CFURL>?>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFURLEnumeratorResult ``` | OS X 10.6 |

Modified CFURLEnumeratorGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CFURLEnumeratorSkipDescendents(CFURLEnumerator!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CFURLGetByteRangeForComponent(CFURL!, CFURLComponentType, UnsafeMutablePointer<CFRange>) -> CFRange

|  | Declaration |
| --- | --- |
| From | ``` func CFURLGetByteRangeForComponent(_ url: CFURL!, _ component: CFURLComponentType, _ rangeIncludingSeparators: UnsafePointer<CFRange>) -> CFRange ``` |
| To | ``` func CFURLGetByteRangeForComponent(_ url: CFURL!, _ component: CFURLComponentType, _ rangeIncludingSeparators: UnsafeMutablePointer<CFRange>) -> CFRange ``` |

Modified CFURLGetBytes(CFURL!, UnsafeMutablePointer<UInt8>, CFIndex) -> CFIndex

|  | Declaration |
| --- | --- |
| From | ``` func CFURLGetBytes(_ url: CFURL!, _ buffer: UnsafePointer<UInt8>, _ bufferLength: CFIndex) -> CFIndex ``` |
| To | ``` func CFURLGetBytes(_ url: CFURL!, _ buffer: UnsafeMutablePointer<UInt8>, _ bufferLength: CFIndex) -> CFIndex ``` |

Modified CFURLGetFileSystemRepresentation(CFURL!, Boolean, UnsafeMutablePointer<UInt8>, CFIndex) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFURLGetFileSystemRepresentation(_ url: CFURL!, _ resolveAgainstBase: Boolean, _ buffer: UnsafePointer<UInt8>, _ maxBufLen: CFIndex) -> Boolean ``` |
| To | ``` func CFURLGetFileSystemRepresentation(_ url: CFURL!, _ resolveAgainstBase: Boolean, _ buffer: UnsafeMutablePointer<UInt8>, _ maxBufLen: CFIndex) -> Boolean ``` |

Modified CFURLIsFileReferenceURL(CFURL!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CFURLResourceIsReachable(CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFURLResourceIsReachable(_ url: CFURL!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFURLResourceIsReachable(_ url: CFURL!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean ``` | OS X 10.6 |

Modified CFURLSetResourcePropertiesForKeys(CFURL!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFURLSetResourcePropertiesForKeys(_ url: CFURL!, _ keyedPropertyValues: CFDictionary!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFURLSetResourcePropertiesForKeys(_ url: CFURL!, _ keyedPropertyValues: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean ``` | OS X 10.6 |

Modified CFURLSetResourcePropertyForKey(CFURL!, CFString!, AnyObject!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFURLSetResourcePropertyForKey(_ url: CFURL!, _ key: CFString!, _ propertyValue: AnyObject!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFURLSetResourcePropertyForKey(_ url: CFURL!, _ key: CFString!, _ propertyValue: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean ``` | OS X 10.6 |

Modified CFURLSetTemporaryResourcePropertyForKey(CFURL!, CFString!, AnyObject!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CFURLStartAccessingSecurityScopedResource(CFURL!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CFURLStopAccessingSecurityScopedResource(CFURL!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CFURLWriteBookmarkDataToFile(CFData!, CFURL!, CFURLBookmarkFileCreationOptions, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFURLWriteBookmarkDataToFile(_ bookmarkRef: CFData!, _ fileURL: CFURL!, _ options: CFURLBookmarkFileCreationOptions, _ errorRef: UnsafePointer<Unmanaged<CFError>?>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFURLWriteBookmarkDataToFile(_ bookmarkRef: CFData!, _ fileURL: CFURL!, _ options: CFURLBookmarkFileCreationOptions, _ errorRef: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean ``` | OS X 10.6 |

Modified CFUserNotificationCreate(CFAllocator!, CFTimeInterval, CFOptionFlags, UnsafeMutablePointer<Int32>, CFDictionary!) -> CFUserNotification!

|  | Declaration |
| --- | --- |
| From | ``` func CFUserNotificationCreate(_ allocator: CFAllocator!, _ timeout: CFTimeInterval, _ flags: CFOptionFlags, _ error: UnsafePointer<Int32>, _ dictionary: CFDictionary!) -> CFUserNotification! ``` |
| To | ``` func CFUserNotificationCreate(_ allocator: CFAllocator!, _ timeout: CFTimeInterval, _ flags: CFOptionFlags, _ error: UnsafeMutablePointer<Int32>, _ dictionary: CFDictionary!) -> CFUserNotification! ``` |

Modified CFUserNotificationDisplayAlert(CFTimeInterval, CFOptionFlags, CFURL!, CFURL!, CFURL!, CFString!, CFString!, CFString!, CFString!, CFString!, UnsafeMutablePointer<CFOptionFlags>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func CFUserNotificationDisplayAlert(_ timeout: CFTimeInterval, _ flags: CFOptionFlags, _ iconURL: CFURL!, _ soundURL: CFURL!, _ localizationURL: CFURL!, _ alertHeader: CFString!, _ alertMessage: CFString!, _ defaultButtonTitle: CFString!, _ alternateButtonTitle: CFString!, _ otherButtonTitle: CFString!, _ responseFlags: UnsafePointer<CFOptionFlags>) -> Int32 ``` |
| To | ``` func CFUserNotificationDisplayAlert(_ timeout: CFTimeInterval, _ flags: CFOptionFlags, _ iconURL: CFURL!, _ soundURL: CFURL!, _ localizationURL: CFURL!, _ alertHeader: CFString!, _ alertMessage: CFString!, _ defaultButtonTitle: CFString!, _ alternateButtonTitle: CFString!, _ otherButtonTitle: CFString!, _ responseFlags: UnsafeMutablePointer<CFOptionFlags>) -> Int32 ``` |

Modified CFUserNotificationReceiveResponse(CFUserNotification!, CFTimeInterval, UnsafeMutablePointer<CFOptionFlags>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func CFUserNotificationReceiveResponse(_ userNotification: CFUserNotification!, _ timeout: CFTimeInterval, _ responseFlags: UnsafePointer<CFOptionFlags>) -> Int32 ``` |
| To | ``` func CFUserNotificationReceiveResponse(_ userNotification: CFUserNotification!, _ timeout: CFTimeInterval, _ responseFlags: UnsafeMutablePointer<CFOptionFlags>) -> Int32 ``` |

Modified CFWriteStreamClientCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFWriteStreamClientCallBack = CFunctionPointer<((CFWriteStream!, CFStreamEventType, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFWriteStreamClientCallBack = CFunctionPointer<((CFWriteStream!, CFStreamEventType, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CFWriteStreamCopyDispatchQueue(CFWriteStream!) -> dispatch_queue_t!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CFWriteStreamCopyError(CFWriteStream!) -> CFError!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFWriteStreamCreateWithBuffer(CFAllocator!, UnsafeMutablePointer<UInt8>, CFIndex) -> CFWriteStream!

|  | Declaration |
| --- | --- |
| From | ``` func CFWriteStreamCreateWithBuffer(_ alloc: CFAllocator!, _ buffer: UnsafePointer<UInt8>, _ bufferCapacity: CFIndex) -> CFWriteStream! ``` |
| To | ``` func CFWriteStreamCreateWithBuffer(_ alloc: CFAllocator!, _ buffer: UnsafeMutablePointer<UInt8>, _ bufferCapacity: CFIndex) -> CFWriteStream! ``` |

Modified CFWriteStreamSetClient(CFWriteStream!, CFOptionFlags, CFWriteStreamClientCallBack, UnsafeMutablePointer<CFStreamClientContext>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CFWriteStreamSetClient(_ stream: CFWriteStream!, _ streamEvents: CFOptionFlags, _ clientCB: CFWriteStreamClientCallBack, _ clientContext: UnsafePointer<CFStreamClientContext>) -> Boolean ``` |
| To | ``` func CFWriteStreamSetClient(_ stream: CFWriteStream!, _ streamEvents: CFOptionFlags, _ clientCB: CFWriteStreamClientCallBack, _ clientContext: UnsafeMutablePointer<CFStreamClientContext>) -> Boolean ``` |

Modified CFWriteStreamSetDispatchQueue(CFWriteStream!, dispatch_queue_t!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CFWriteStreamWrite(CFWriteStream!, UnsafePointer<UInt8>, CFIndex) -> CFIndex

|  | Declaration |
| --- | --- |
| From | ``` func CFWriteStreamWrite(_ stream: CFWriteStream!, _ buffer: ConstUnsafePointer<UInt8>, _ bufferLength: CFIndex) -> CFIndex ``` |
| To | ``` func CFWriteStreamWrite(_ stream: CFWriteStream!, _ buffer: UnsafePointer<UInt8>, _ bufferLength: CFIndex) -> CFIndex ``` |

Modified CFXMLParserAddChildCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFXMLParserAddChildCallBack = CFunctionPointer<((CFXMLParser!, UnsafePointer<()>, UnsafePointer<()>, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFXMLParserAddChildCallBack = CFunctionPointer<((CFXMLParser!, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CFXMLParserCopyDescriptionCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFXMLParserCopyDescriptionCallBack = CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> ``` |
| To | ``` typealias CFXMLParserCopyDescriptionCallBack = CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |

Modified CFXMLParserCreateXMLStructureCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFXMLParserCreateXMLStructureCallBack = CFunctionPointer<((CFXMLParser!, CFXMLNode!, UnsafePointer<()>) -> UnsafePointer<()>)> ``` |
| To | ``` typealias CFXMLParserCreateXMLStructureCallBack = CFunctionPointer<((CFXMLParser!, CFXMLNode!, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)> ``` |

Modified CFXMLParserEndXMLStructureCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFXMLParserEndXMLStructureCallBack = CFunctionPointer<((CFXMLParser!, UnsafePointer<()>, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFXMLParserEndXMLStructureCallBack = CFunctionPointer<((CFXMLParser!, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CFXMLParserHandleErrorCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFXMLParserHandleErrorCallBack = CFunctionPointer<((CFXMLParser!, CFXMLParserStatusCode, UnsafePointer<()>) -> Boolean)> ``` |
| To | ``` typealias CFXMLParserHandleErrorCallBack = CFunctionPointer<((CFXMLParser!, CFXMLParserStatusCode, UnsafeMutablePointer<Void>) -> Boolean)> ``` |

Modified CFXMLParserReleaseCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFXMLParserReleaseCallBack = CFunctionPointer<((ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFXMLParserReleaseCallBack = CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |

Modified CFXMLParserResolveExternalEntityCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFXMLParserResolveExternalEntityCallBack = CFunctionPointer<((CFXMLParser!, UnsafePointer<CFXMLExternalID>, UnsafePointer<()>) -> Unmanaged<CFData>!)> ``` |
| To | ``` typealias CFXMLParserResolveExternalEntityCallBack = CFunctionPointer<((CFXMLParser!, UnsafeMutablePointer<CFXMLExternalID>, UnsafeMutablePointer<Void>) -> Unmanaged<CFData>!)> ``` |

Modified CFXMLParserRetainCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFXMLParserRetainCallBack = CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)> ``` |
| To | ``` typealias CFXMLParserRetainCallBack = CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |

Modified kCFDateFormatterDoesRelativeDateFormattingKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFDateFormatterGregorianStartDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFDateFormatterLongEraSymbols

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFDateFormatterQuarterSymbols

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFDateFormatterShortQuarterSymbols

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFDateFormatterShortStandaloneMonthSymbols

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFDateFormatterShortStandaloneQuarterSymbols

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFDateFormatterShortStandaloneWeekdaySymbols

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFDateFormatterStandaloneMonthSymbols

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFDateFormatterStandaloneQuarterSymbols

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFDateFormatterStandaloneWeekdaySymbols

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFDateFormatterVeryShortMonthSymbols

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFDateFormatterVeryShortStandaloneMonthSymbols

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFDateFormatterVeryShortStandaloneWeekdaySymbols

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFDateFormatterVeryShortWeekdaySymbols

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFErrorDescriptionKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFErrorDomainCocoa

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFErrorDomainMach

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFErrorDomainOSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFErrorDomainPOSIX

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFErrorFilePathKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFErrorLocalizedDescriptionKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFErrorLocalizedFailureReasonKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFErrorLocalizedRecoverySuggestionKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFErrorURLKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFErrorUnderlyingErrorKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFISO8601Calendar

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFIndianCalendar

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFLocaleAlternateQuotationBeginDelimiterKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFLocaleAlternateQuotationEndDelimiterKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFLocaleCollatorIdentifier

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFLocaleCurrentLocaleDidChangeNotification

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFLocaleQuotationBeginDelimiterKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFLocaleQuotationEndDelimiterKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFNumberFormatterCurrencyGroupingSeparator

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFNumberFormatterIsLenient

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFNumberFormatterMaxSignificantDigits

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFNumberFormatterMinSignificantDigits

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFNumberFormatterUseSignificantDigits

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFPersianCalendar

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFRepublicOfChinaCalendar

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFSocketLeaveErrors

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFStringTransformStripDiacritics

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFTimeZoneSystemTimeZoneDidChangeNotification

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFURLAttributeModificationDateKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLContentAccessDateKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLContentModificationDateKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLCreationDateKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLCustomIconKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLEffectiveIconKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLFileAllocatedSizeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLFileResourceIdentifierKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLFileResourceTypeBlockSpecial

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLFileResourceTypeCharacterSpecial

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLFileResourceTypeDirectory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLFileResourceTypeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLFileResourceTypeNamedPipe

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLFileResourceTypeRegular

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLFileResourceTypeSocket

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLFileResourceTypeSymbolicLink

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLFileResourceTypeUnknown

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLFileSecurityKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLFileSizeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLHasHiddenExtensionKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLIsAliasFileKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLIsDirectoryKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLIsExcludedFromBackupKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCFURLIsExecutableKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLIsHiddenKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLIsMountTriggerKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLIsPackageKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLIsReadableKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLIsRegularFileKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLIsSymbolicLinkKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLIsSystemImmutableKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLIsUbiquitousItemKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLIsUserImmutableKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLIsVolumeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLIsWritableKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLKeysOfUnsetValuesKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLLabelColorKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLLabelNumberKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLLinkCountKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLLocalizedLabelKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLLocalizedNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLLocalizedTypeDescriptionKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLParentDirectoryURLKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLPathKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCFURLPreferredIOBlockSizeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLTagNamesKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCFURLTotalFileAllocatedSizeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLTotalFileSizeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLTypeIdentifierKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLUbiquitousItemDownloadingErrorKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCFURLUbiquitousItemDownloadingStatusCurrent

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCFURLUbiquitousItemDownloadingStatusDownloaded

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCFURLUbiquitousItemDownloadingStatusKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCFURLUbiquitousItemDownloadingStatusNotDownloaded

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCFURLUbiquitousItemHasUnresolvedConflictsKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLUbiquitousItemIsDownloadingKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLUbiquitousItemIsUploadedKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLUbiquitousItemIsUploadingKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLUbiquitousItemUploadingErrorKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCFURLVolumeAvailableCapacityKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLVolumeCreationDateKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLVolumeIdentifierKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLVolumeIsAutomountedKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLVolumeIsBrowsableKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLVolumeIsEjectableKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLVolumeIsInternalKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLVolumeIsJournalingKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLVolumeIsLocalKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLVolumeIsReadOnlyKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLVolumeIsRemovableKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLVolumeLocalizedFormatDescriptionKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLVolumeLocalizedNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLVolumeMaximumFileSizeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLVolumeNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLVolumeResourceCountKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLVolumeSupportsAdvisoryFileLockingKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLVolumeSupportsCasePreservedNamesKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLVolumeSupportsCaseSensitiveNamesKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLVolumeSupportsExtendedSecurityKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLVolumeSupportsHardLinksKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLVolumeSupportsJournalingKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLVolumeSupportsPersistentIDsKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLVolumeSupportsRenamingKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLVolumeSupportsRootDirectoryDatesKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLVolumeSupportsSparseFilesKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLVolumeSupportsSymbolicLinksKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLVolumeSupportsVolumeSizesKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLVolumeSupportsZeroRunsKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLVolumeTotalCapacityKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLVolumeURLForRemountingKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFURLVolumeURLKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFURLVolumeUUIDStringKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFUserNotificationPopUpSelectionKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

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
