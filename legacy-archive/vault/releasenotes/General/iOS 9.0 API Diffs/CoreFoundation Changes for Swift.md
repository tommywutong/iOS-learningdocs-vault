---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/CoreFoundation.html
archived_at: '2026-07-18T02:56:43.729770Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# CoreFoundation Changes for Swift

### CoreFoundation

Removed CFAllocatorContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFAllocatorRetainCallBack, release: CFAllocatorReleaseCallBack, copyDescription: CFAllocatorCopyDescriptionCallBack, allocate: CFAllocatorAllocateCallBack, reallocate: CFAllocatorReallocateCallBack, deallocate: CFAllocatorDeallocateCallBack, preferredSize: CFAllocatorPreferredSizeCallBack)Removed CFArrayCallBacks.init(version: CFIndex, retain: CFArrayRetainCallBack, release: CFArrayReleaseCallBack, copyDescription: CFArrayCopyDescriptionCallBack, equal: CFArrayEqualCallBack)Removed CFBagCallBacks.init(version: CFIndex, retain: CFBagRetainCallBack, release: CFBagReleaseCallBack, copyDescription: CFBagCopyDescriptionCallBack, equal: CFBagEqualCallBack, hash: CFBagHashCallBack)Removed CFBinaryHeapCallBacks.init(version: CFIndex, retain: CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>, compare: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> CFComparisonResult)>)Removed CFBinaryHeapCompareContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Removed CFCalendarUnit.init(_: CFOptionFlags)Removed CFDataSearchFlags.init(_: CFOptionFlags)Removed CFDictionaryKeyCallBacks.init(version: CFIndex, retain: CFDictionaryRetainCallBack, release: CFDictionaryReleaseCallBack, copyDescription: CFDictionaryCopyDescriptionCallBack, equal: CFDictionaryEqualCallBack, hash: CFDictionaryHashCallBack)Removed CFDictionaryValueCallBacks.init(version: CFIndex, retain: CFDictionaryRetainCallBack, release: CFDictionaryReleaseCallBack, copyDescription: CFDictionaryCopyDescriptionCallBack, equal: CFDictionaryEqualCallBack)Removed CFFileDescriptorContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>, release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)>)Removed CFFileSecurityClearOptions.init(_: CFOptionFlags)Removed CFGregorianUnitFlags.init(_: CFOptionFlags)Removed CFMachPortContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Removed CFMessagePortContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Removed CFNumberFormatterOptionFlags.init(_: CFOptionFlags)Removed CFPropertyListMutabilityOptions.init(_: CFOptionFlags)Removed CFRunLoopActivity.init(_: CFOptionFlags)Removed CFRunLoopObserverContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Removed CFRunLoopSourceContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>, equal: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)>, hash: CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)>, schedule: CFunctionPointer<((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)>, cancel: CFunctionPointer<((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)>, perform: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>)Removed CFRunLoopSourceContext1.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>, equal: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)>, hash: CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)>, getPort: CFunctionPointer<((UnsafeMutablePointer<Void>) -> mach_port_t)>, perform: CFunctionPointer<((UnsafeMutablePointer<Void>, CFIndex, CFAllocator!, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>)Removed CFRunLoopTimerContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Removed CFSetCallBacks.init(version: CFIndex, retain: CFSetRetainCallBack, release: CFSetReleaseCallBack, copyDescription: CFSetCopyDescriptionCallBack, equal: CFSetEqualCallBack, hash: CFSetHashCallBack)Removed CFSocketCallBackType.init(_: CFOptionFlags)Removed CFSocketContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Removed CFStreamClientContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>, release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)>)Removed CFStreamEventType.init(_: CFOptionFlags)Removed CFStringCompareFlags.init(_: CFOptionFlags)Removed CFStringTokenizerTokenType.init(_: CFOptionFlags)Removed CFTreeContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFTreeRetainCallBack, release: CFTreeReleaseCallBack, copyDescription: CFTreeCopyDescriptionCallBack)Removed CFURLBookmarkCreationOptions.init(_: CFOptionFlags)Removed CFURLBookmarkResolutionOptions.init(_: CFOptionFlags)Removed CFURLEnumeratorOptions.init(_: CFOptionFlags)Removed kCFRunLoopRunFinishedRemoved kCFRunLoopRunHandledSourceRemoved kCFRunLoopRunStoppedRemoved kCFRunLoopRunTimedOutAdded CFAllocatorContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFAllocatorRetainCallBack!, release: CFAllocatorReleaseCallBack!, copyDescription: CFAllocatorCopyDescriptionCallBack!, allocate: CFAllocatorAllocateCallBack!, reallocate: CFAllocatorReallocateCallBack!, deallocate: CFAllocatorDeallocateCallBack!, preferredSize: CFAllocatorPreferredSizeCallBack!)Added CFArrayCallBacks.init(version: CFIndex, retain: CFArrayRetainCallBack!, release: CFArrayReleaseCallBack!, copyDescription: CFArrayCopyDescriptionCallBack!, equal: CFArrayEqualCallBack!)Added CFBagCallBacks.init(version: CFIndex, retain: CFBagRetainCallBack!, release: CFBagReleaseCallBack!, copyDescription: CFBagCopyDescriptionCallBack!, equal: CFBagEqualCallBack!, hash: CFBagHashCallBack!)Added CFBinaryHeapCallBacks.init(version: CFIndex, retain: ((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)!, release: ((CFAllocator!, UnsafePointer<Void>) -> Void)!, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!, compare: ((UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> CFComparisonResult)!)Added CFBinaryHeapCompareContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release: ((UnsafePointer<Void>) -> Void)!, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!)Added CFDictionaryKeyCallBacks.init(version: CFIndex, retain: CFDictionaryRetainCallBack!, release: CFDictionaryReleaseCallBack!, copyDescription: CFDictionaryCopyDescriptionCallBack!, equal: CFDictionaryEqualCallBack!, hash: CFDictionaryHashCallBack!)Added CFDictionaryValueCallBacks.init(version: CFIndex, retain: CFDictionaryRetainCallBack!, release: CFDictionaryReleaseCallBack!, copyDescription: CFDictionaryCopyDescriptionCallBack!, equal: CFDictionaryEqualCallBack!)Added CFFileDescriptorContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)!, release: ((UnsafeMutablePointer<Void>) -> Void)!, copyDescription: ((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)!)Added CFMachPortContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release: ((UnsafePointer<Void>) -> Void)!, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!)Added CFMessagePortContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release: ((UnsafePointer<Void>) -> Void)!, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!)Added [CFNumberFormatterStyle.CurrencyAccountingStyle](https://developer.apple.com/documentation/corefoundation/cfnumberformatterstyle/currencyaccountingstyle)Added [CFNumberFormatterStyle.CurrencyISOCodeStyle](https://developer.apple.com/documentation/corefoundation/cfnumberformatterstyle/kcfnumberformattercurrencyisocodestyle)Added [CFNumberFormatterStyle.CurrencyPluralStyle](https://developer.apple.com/documentation/corefoundation/cfnumberformatterstyle/currencypluralstyle)Added [CFNumberFormatterStyle.OrdinalStyle](https://developer.apple.com/documentation/corefoundation/cfnumberformatterstyle/ordinalstyle)Added [CFNumberType.MaxType](https://developer.apple.com/documentation/corefoundation/cfnumbertype/kcfnumbermaxtype)Added CFRunLoopObserverContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release: ((UnsafePointer<Void>) -> Void)!, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!)Added [CFRunLoopRunResult [enum]](https://developer.apple.com/documentation/corefoundation/cfrunlooprunresult)Added [CFRunLoopRunResult.Finished](https://developer.apple.com/documentation/corefoundation/cfrunlooprunresult/kcfrunlooprunfinished)Added [CFRunLoopRunResult.HandledSource](https://developer.apple.com/documentation/corefoundation/cfrunlooprunresult/kcfrunlooprunhandledsource)Added [CFRunLoopRunResult.Stopped](https://developer.apple.com/documentation/corefoundation/cfrunlooprunresult/stopped)Added [CFRunLoopRunResult.TimedOut](https://developer.apple.com/documentation/corefoundation/cfrunlooprunresult/timedout)Added CFRunLoopSourceContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release: ((UnsafePointer<Void>) -> Void)!, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!, equal: ((UnsafePointer<Void>, UnsafePointer<Void>) -> DarwinBoolean)!, hash: ((UnsafePointer<Void>) -> CFHashCode)!, schedule: ((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)!, cancel: ((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)!, perform: ((UnsafeMutablePointer<Void>) -> Void)!)Added CFRunLoopSourceContext1.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release: ((UnsafePointer<Void>) -> Void)!, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!, equal: ((UnsafePointer<Void>, UnsafePointer<Void>) -> DarwinBoolean)!, hash: ((UnsafePointer<Void>) -> CFHashCode)!, getPort: ((UnsafeMutablePointer<Void>) -> mach_port_t)!, perform: ((UnsafeMutablePointer<Void>, CFIndex, CFAllocator!, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)!)Added CFRunLoopTimerContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release: ((UnsafePointer<Void>) -> Void)!, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!)Added CFSetCallBacks.init(version: CFIndex, retain: CFSetRetainCallBack!, release: CFSetReleaseCallBack!, copyDescription: CFSetCopyDescriptionCallBack!, equal: CFSetEqualCallBack!, hash: CFSetHashCallBack!)Added CFSocketContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release: ((UnsafePointer<Void>) -> Void)!, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!)Added CFStreamClientContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)!, release: ((UnsafeMutablePointer<Void>) -> Void)!, copyDescription: ((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)!)Added [CFStringBuiltInEncodings.UTF16](https://developer.apple.com/documentation/corefoundation/cfstringbuiltinencodings/kcfstringencodingutf16)Added [CFStringEncodings.ShiftJIS_X0213_00](https://developer.apple.com/documentation/corefoundation/cfstringencodings/1543375-shiftjis_x0213_00)Added CFTreeContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFTreeRetainCallBack!, release: CFTreeReleaseCallBack!, copyDescription: CFTreeCopyDescriptionCallBack!)Added [kCFCoreFoundationVersionNumber10_10](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_10)Added [kCFCoreFoundationVersionNumber10_10_1](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_10_1)Added [kCFCoreFoundationVersionNumber10_10_2](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_10_2)Added [kCFCoreFoundationVersionNumber10_10_3](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_10_3)Added [kCFCoreFoundationVersionNumber_iOS_8_0](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber_ios_8_0)Added [kCFCoreFoundationVersionNumber_iOS_8_1](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber_ios_8_1)Added [kCFCoreFoundationVersionNumber_iOS_8_2](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber_ios_8_2)Added [kCFURLFileProtectionComplete](https://developer.apple.com/documentation/corefoundation/kcfurlfileprotectioncomplete)Added [kCFURLFileProtectionCompleteUnlessOpen](https://developer.apple.com/documentation/corefoundation/kcfurlfileprotectioncompleteunlessopen)Added [kCFURLFileProtectionCompleteUntilFirstUserAuthentication](https://developer.apple.com/documentation/corefoundation/kcfurlfileprotectioncompleteuntilfirstuserauthentication)Added [kCFURLFileProtectionKey](https://developer.apple.com/documentation/corefoundation/kcfurlfileprotectionkey)Added [kCFURLFileProtectionNone](https://developer.apple.com/documentation/corefoundation/kcfurlfileprotectionnone)Added [kCFURLIsApplicationKey](https://developer.apple.com/documentation/corefoundation/kcfurlisapplicationkey)Modified [CFAllocatorContext [struct]](https://developer.apple.com/documentation/corefoundation/cfallocatorcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFAllocatorContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack     var release: CFAllocatorReleaseCallBack     var copyDescription: CFAllocatorCopyDescriptionCallBack     var allocate: CFAllocatorAllocateCallBack     var reallocate: CFAllocatorReallocateCallBack     var deallocate: CFAllocatorDeallocateCallBack     var preferredSize: CFAllocatorPreferredSizeCallBack     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFAllocatorRetainCallBack, release release: CFAllocatorReleaseCallBack, copyDescription copyDescription: CFAllocatorCopyDescriptionCallBack, allocate allocate: CFAllocatorAllocateCallBack, reallocate reallocate: CFAllocatorReallocateCallBack, deallocate deallocate: CFAllocatorDeallocateCallBack, preferredSize preferredSize: CFAllocatorPreferredSizeCallBack) } ``` |
| To | ``` struct CFAllocatorContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack!     var release: CFAllocatorReleaseCallBack!     var copyDescription: CFAllocatorCopyDescriptionCallBack!     var allocate: CFAllocatorAllocateCallBack!     var reallocate: CFAllocatorReallocateCallBack!     var deallocate: CFAllocatorDeallocateCallBack!     var preferredSize: CFAllocatorPreferredSizeCallBack!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFAllocatorRetainCallBack!, release release: CFAllocatorReleaseCallBack!, copyDescription copyDescription: CFAllocatorCopyDescriptionCallBack!, allocate allocate: CFAllocatorAllocateCallBack!, reallocate reallocate: CFAllocatorReallocateCallBack!, deallocate deallocate: CFAllocatorDeallocateCallBack!, preferredSize preferredSize: CFAllocatorPreferredSizeCallBack!) } ``` |

Modified [CFAllocatorContext.allocate](https://developer.apple.com/documentation/corefoundation/cfallocatorcontext/1521286-allocate)

|  | Declaration |
| --- | --- |
| From | ``` var allocate: CFAllocatorAllocateCallBack ``` |
| To | ``` var allocate: CFAllocatorAllocateCallBack! ``` |

Modified [CFAllocatorContext.copyDescription](https://developer.apple.com/documentation/corefoundation/cfallocatorcontext/1521301-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFAllocatorCopyDescriptionCallBack ``` |
| To | ``` var copyDescription: CFAllocatorCopyDescriptionCallBack! ``` |

Modified [CFAllocatorContext.deallocate](https://developer.apple.com/documentation/corefoundation/cfallocatorcontext/1521339-deallocate)

|  | Declaration |
| --- | --- |
| From | ``` var deallocate: CFAllocatorDeallocateCallBack ``` |
| To | ``` var deallocate: CFAllocatorDeallocateCallBack! ``` |

Modified [CFAllocatorContext.preferredSize](https://developer.apple.com/documentation/corefoundation/cfallocatorcontext/1521307-preferredsize)

|  | Declaration |
| --- | --- |
| From | ``` var preferredSize: CFAllocatorPreferredSizeCallBack ``` |
| To | ``` var preferredSize: CFAllocatorPreferredSizeCallBack! ``` |

Modified [CFAllocatorContext.reallocate](https://developer.apple.com/documentation/corefoundation/cfallocatorcontext/1521222-reallocate)

|  | Declaration |
| --- | --- |
| From | ``` var reallocate: CFAllocatorReallocateCallBack ``` |
| To | ``` var reallocate: CFAllocatorReallocateCallBack! ``` |

Modified [CFAllocatorContext.release](https://developer.apple.com/documentation/corefoundation/cfallocatorcontext/1521148-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFAllocatorReleaseCallBack ``` |
| To | ``` var release: CFAllocatorReleaseCallBack! ``` |

Modified [CFAllocatorContext.retain](https://developer.apple.com/documentation/corefoundation/cfallocatorcontext/1521359-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFAllocatorRetainCallBack ``` |
| To | ``` var retain: CFAllocatorRetainCallBack! ``` |

Modified [CFArrayCallBacks [struct]](https://developer.apple.com/documentation/corefoundation/cfarraycallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CFArrayCallBacks {     var version: CFIndex     var retain: CFArrayRetainCallBack     var release: CFArrayReleaseCallBack     var copyDescription: CFArrayCopyDescriptionCallBack     var equal: CFArrayEqualCallBack     init()     init(version version: CFIndex, retain retain: CFArrayRetainCallBack, release release: CFArrayReleaseCallBack, copyDescription copyDescription: CFArrayCopyDescriptionCallBack, equal equal: CFArrayEqualCallBack) } ``` |
| To | ``` struct CFArrayCallBacks {     var version: CFIndex     var retain: CFArrayRetainCallBack!     var release: CFArrayReleaseCallBack!     var copyDescription: CFArrayCopyDescriptionCallBack!     var equal: CFArrayEqualCallBack!     init()     init(version version: CFIndex, retain retain: CFArrayRetainCallBack!, release release: CFArrayReleaseCallBack!, copyDescription copyDescription: CFArrayCopyDescriptionCallBack!, equal equal: CFArrayEqualCallBack!) } ``` |

Modified [CFArrayCallBacks.copyDescription](https://developer.apple.com/documentation/corefoundation/cfarraycallbacks/1388780-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFArrayCopyDescriptionCallBack ``` |
| To | ``` var copyDescription: CFArrayCopyDescriptionCallBack! ``` |

Modified [CFArrayCallBacks.equal](https://developer.apple.com/documentation/corefoundation/cfarraycallbacks/1388790-equal)

|  | Declaration |
| --- | --- |
| From | ``` var equal: CFArrayEqualCallBack ``` |
| To | ``` var equal: CFArrayEqualCallBack! ``` |

Modified [CFArrayCallBacks.release](https://developer.apple.com/documentation/corefoundation/cfarraycallbacks/1388743-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFArrayReleaseCallBack ``` |
| To | ``` var release: CFArrayReleaseCallBack! ``` |

Modified [CFArrayCallBacks.retain](https://developer.apple.com/documentation/corefoundation/cfarraycallbacks/1388784-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFArrayRetainCallBack ``` |
| To | ``` var retain: CFArrayRetainCallBack! ``` |

Modified [CFBagCallBacks [struct]](https://developer.apple.com/documentation/corefoundation/cfbagcallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CFBagCallBacks {     var version: CFIndex     var retain: CFBagRetainCallBack     var release: CFBagReleaseCallBack     var copyDescription: CFBagCopyDescriptionCallBack     var equal: CFBagEqualCallBack     var hash: CFBagHashCallBack     init()     init(version version: CFIndex, retain retain: CFBagRetainCallBack, release release: CFBagReleaseCallBack, copyDescription copyDescription: CFBagCopyDescriptionCallBack, equal equal: CFBagEqualCallBack, hash hash: CFBagHashCallBack) } ``` |
| To | ``` struct CFBagCallBacks {     var version: CFIndex     var retain: CFBagRetainCallBack!     var release: CFBagReleaseCallBack!     var copyDescription: CFBagCopyDescriptionCallBack!     var equal: CFBagEqualCallBack!     var hash: CFBagHashCallBack!     init()     init(version version: CFIndex, retain retain: CFBagRetainCallBack!, release release: CFBagReleaseCallBack!, copyDescription copyDescription: CFBagCopyDescriptionCallBack!, equal equal: CFBagEqualCallBack!, hash hash: CFBagHashCallBack!) } ``` |

Modified [CFBagCallBacks.copyDescription](https://developer.apple.com/documentation/corefoundation/cfbagcallbacks/1469256-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFBagCopyDescriptionCallBack ``` |
| To | ``` var copyDescription: CFBagCopyDescriptionCallBack! ``` |

Modified [CFBagCallBacks.equal](https://developer.apple.com/documentation/corefoundation/cfbagcallbacks/1469316-equal)

|  | Declaration |
| --- | --- |
| From | ``` var equal: CFBagEqualCallBack ``` |
| To | ``` var equal: CFBagEqualCallBack! ``` |

Modified [CFBagCallBacks.hash](https://developer.apple.com/documentation/corefoundation/cfbagcallbacks/1469293-hash)

|  | Declaration |
| --- | --- |
| From | ``` var hash: CFBagHashCallBack ``` |
| To | ``` var hash: CFBagHashCallBack! ``` |

Modified [CFBagCallBacks.release](https://developer.apple.com/documentation/corefoundation/cfbagcallbacks/1469307-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFBagReleaseCallBack ``` |
| To | ``` var release: CFBagReleaseCallBack! ``` |

Modified [CFBagCallBacks.retain](https://developer.apple.com/documentation/corefoundation/cfbagcallbacks/1469278-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFBagRetainCallBack ``` |
| To | ``` var retain: CFBagRetainCallBack! ``` |

Modified [CFBinaryHeapCallBacks [struct]](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CFBinaryHeapCallBacks {     var version: CFIndex     var retain: CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     var compare: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> CFComparisonResult)>     init()     init(version version: CFIndex, retain retain: CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>, compare compare: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> CFComparisonResult)>) } ``` |
| To | ``` struct CFBinaryHeapCallBacks {     var version: CFIndex     var retain: ((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)!     var release: ((CFAllocator!, UnsafePointer<Void>) -> Void)!     var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!     var compare: ((UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> CFComparisonResult)!     init()     init(version version: CFIndex, retain retain: ((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)!, release release: ((CFAllocator!, UnsafePointer<Void>) -> Void)!, copyDescription copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!, compare compare: ((UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> CFComparisonResult)!) } ``` |

Modified [CFBinaryHeapCallBacks.compare](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcallbacks/1509307-compare)

|  | Declaration |
| --- | --- |
| From | ``` var compare: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> CFComparisonResult)> ``` |
| To | ``` var compare: ((UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> CFComparisonResult)! ``` |

Modified [CFBinaryHeapCallBacks.copyDescription](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcallbacks/1509329-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)! ``` |

Modified [CFBinaryHeapCallBacks.release](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcallbacks/1509326-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> Void)> ``` |
| To | ``` var release: ((CFAllocator!, UnsafePointer<Void>) -> Void)! ``` |

Modified [CFBinaryHeapCallBacks.retain](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcallbacks/1509294-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |
| To | ``` var retain: ((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)! ``` |

Modified [CFBinaryHeapCompareContext [struct]](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcomparecontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFBinaryHeapCompareContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |
| To | ``` struct CFBinaryHeapCompareContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!     var release: ((UnsafePointer<Void>) -> Void)!     var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release release: ((UnsafePointer<Void>) -> Void)!, copyDescription copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!) } ``` |

Modified [CFBinaryHeapCompareContext.copyDescription](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcomparecontext/1509311-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)! ``` |

Modified [CFBinaryHeapCompareContext.release](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcomparecontext/1509299-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |
| To | ``` var release: ((UnsafePointer<Void>) -> Void)! ``` |

Modified [CFBinaryHeapCompareContext.retain](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcomparecontext/1509313-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |
| To | ``` var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)! ``` |

Modified [CFCalendarUnit [struct]](https://developer.apple.com/documentation/corefoundation/cfcalendarunit)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFCalendarUnit : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var Era: CFCalendarUnit { get }     static var Year: CFCalendarUnit { get }     static var Month: CFCalendarUnit { get }     static var Day: CFCalendarUnit { get }     static var Hour: CFCalendarUnit { get }     static var Minute: CFCalendarUnit { get }     static var Second: CFCalendarUnit { get }     static var Week: CFCalendarUnit { get }     static var Weekday: CFCalendarUnit { get }     static var WeekdayOrdinal: CFCalendarUnit { get }     static var Quarter: CFCalendarUnit { get }     static var WeekOfMonth: CFCalendarUnit { get }     static var WeekOfYear: CFCalendarUnit { get }     static var YearForWeekOfYear: CFCalendarUnit { get } } ``` | RawOptionSetType |
| To | ``` struct CFCalendarUnit : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var Era: CFCalendarUnit { get }     static var Year: CFCalendarUnit { get }     static var Month: CFCalendarUnit { get }     static var Day: CFCalendarUnit { get }     static var Hour: CFCalendarUnit { get }     static var Minute: CFCalendarUnit { get }     static var Second: CFCalendarUnit { get }     static var Week: CFCalendarUnit { get }     static var Weekday: CFCalendarUnit { get }     static var WeekdayOrdinal: CFCalendarUnit { get }     static var Quarter: CFCalendarUnit { get }     static var WeekOfMonth: CFCalendarUnit { get }     static var WeekOfYear: CFCalendarUnit { get }     static var YearForWeekOfYear: CFCalendarUnit { get } } ``` | OptionSetType |

Modified [CFDataSearchFlags [struct]](https://developer.apple.com/documentation/corefoundation/cfdatasearchflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFDataSearchFlags : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var Backwards: CFDataSearchFlags { get }     static var Anchored: CFDataSearchFlags { get } } ``` | RawOptionSetType |
| To | ``` struct CFDataSearchFlags : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var Backwards: CFDataSearchFlags { get }     static var Anchored: CFDataSearchFlags { get } } ``` | OptionSetType |

Modified [CFDictionaryKeyCallBacks [struct]](https://developer.apple.com/documentation/corefoundation/cfdictionarykeycallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CFDictionaryKeyCallBacks {     var version: CFIndex     var retain: CFDictionaryRetainCallBack     var release: CFDictionaryReleaseCallBack     var copyDescription: CFDictionaryCopyDescriptionCallBack     var equal: CFDictionaryEqualCallBack     var hash: CFDictionaryHashCallBack     init()     init(version version: CFIndex, retain retain: CFDictionaryRetainCallBack, release release: CFDictionaryReleaseCallBack, copyDescription copyDescription: CFDictionaryCopyDescriptionCallBack, equal equal: CFDictionaryEqualCallBack, hash hash: CFDictionaryHashCallBack) } ``` |
| To | ``` struct CFDictionaryKeyCallBacks {     var version: CFIndex     var retain: CFDictionaryRetainCallBack!     var release: CFDictionaryReleaseCallBack!     var copyDescription: CFDictionaryCopyDescriptionCallBack!     var equal: CFDictionaryEqualCallBack!     var hash: CFDictionaryHashCallBack!     init()     init(version version: CFIndex, retain retain: CFDictionaryRetainCallBack!, release release: CFDictionaryReleaseCallBack!, copyDescription copyDescription: CFDictionaryCopyDescriptionCallBack!, equal equal: CFDictionaryEqualCallBack!, hash hash: CFDictionaryHashCallBack!) } ``` |

Modified [CFDictionaryKeyCallBacks.copyDescription](https://developer.apple.com/documentation/corefoundation/cfdictionarykeycallbacks/1516761-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFDictionaryCopyDescriptionCallBack ``` |
| To | ``` var copyDescription: CFDictionaryCopyDescriptionCallBack! ``` |

Modified [CFDictionaryKeyCallBacks.equal](https://developer.apple.com/documentation/corefoundation/cfdictionarykeycallbacks/1516802-equal)

|  | Declaration |
| --- | --- |
| From | ``` var equal: CFDictionaryEqualCallBack ``` |
| To | ``` var equal: CFDictionaryEqualCallBack! ``` |

Modified [CFDictionaryKeyCallBacks.hash](https://developer.apple.com/documentation/corefoundation/cfdictionarykeycallbacks/1516784-hash)

|  | Declaration |
| --- | --- |
| From | ``` var hash: CFDictionaryHashCallBack ``` |
| To | ``` var hash: CFDictionaryHashCallBack! ``` |

Modified [CFDictionaryKeyCallBacks.release](https://developer.apple.com/documentation/corefoundation/cfdictionarykeycallbacks/1516780-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFDictionaryReleaseCallBack ``` |
| To | ``` var release: CFDictionaryReleaseCallBack! ``` |

Modified [CFDictionaryKeyCallBacks.retain](https://developer.apple.com/documentation/corefoundation/cfdictionarykeycallbacks/1516804-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFDictionaryRetainCallBack ``` |
| To | ``` var retain: CFDictionaryRetainCallBack! ``` |

Modified [CFDictionaryValueCallBacks [struct]](https://developer.apple.com/documentation/corefoundation/cfdictionaryvaluecallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CFDictionaryValueCallBacks {     var version: CFIndex     var retain: CFDictionaryRetainCallBack     var release: CFDictionaryReleaseCallBack     var copyDescription: CFDictionaryCopyDescriptionCallBack     var equal: CFDictionaryEqualCallBack     init()     init(version version: CFIndex, retain retain: CFDictionaryRetainCallBack, release release: CFDictionaryReleaseCallBack, copyDescription copyDescription: CFDictionaryCopyDescriptionCallBack, equal equal: CFDictionaryEqualCallBack) } ``` |
| To | ``` struct CFDictionaryValueCallBacks {     var version: CFIndex     var retain: CFDictionaryRetainCallBack!     var release: CFDictionaryReleaseCallBack!     var copyDescription: CFDictionaryCopyDescriptionCallBack!     var equal: CFDictionaryEqualCallBack!     init()     init(version version: CFIndex, retain retain: CFDictionaryRetainCallBack!, release release: CFDictionaryReleaseCallBack!, copyDescription copyDescription: CFDictionaryCopyDescriptionCallBack!, equal equal: CFDictionaryEqualCallBack!) } ``` |

Modified [CFDictionaryValueCallBacks.copyDescription](https://developer.apple.com/documentation/corefoundation/cfdictionaryvaluecallbacks/1516773-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFDictionaryCopyDescriptionCallBack ``` |
| To | ``` var copyDescription: CFDictionaryCopyDescriptionCallBack! ``` |

Modified [CFDictionaryValueCallBacks.equal](https://developer.apple.com/documentation/corefoundation/cfdictionaryvaluecallbacks/1516767-equal)

|  | Declaration |
| --- | --- |
| From | ``` var equal: CFDictionaryEqualCallBack ``` |
| To | ``` var equal: CFDictionaryEqualCallBack! ``` |

Modified [CFDictionaryValueCallBacks.release](https://developer.apple.com/documentation/corefoundation/cfdictionaryvaluecallbacks/1516793-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFDictionaryReleaseCallBack ``` |
| To | ``` var release: CFDictionaryReleaseCallBack! ``` |

Modified [CFDictionaryValueCallBacks.retain](https://developer.apple.com/documentation/corefoundation/cfdictionaryvaluecallbacks/1516775-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFDictionaryRetainCallBack ``` |
| To | ``` var retain: CFDictionaryRetainCallBack! ``` |

Modified [CFFileDescriptorContext [struct]](https://developer.apple.com/documentation/corefoundation/cffiledescriptorcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFFileDescriptorContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>     var release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>, release release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |
| To | ``` struct CFFileDescriptorContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)!     var release: ((UnsafeMutablePointer<Void>) -> Void)!     var copyDescription: ((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)!, release release: ((UnsafeMutablePointer<Void>) -> Void)!, copyDescription copyDescription: ((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)!) } ``` |

Modified [CFFileDescriptorContext.copyDescription](https://developer.apple.com/documentation/corefoundation/cffiledescriptorcontext/1477577-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: ((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)! ``` |

Modified [CFFileDescriptorContext.release](https://developer.apple.com/documentation/corefoundation/cffiledescriptorcontext/1477589-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` var release: ((UnsafeMutablePointer<Void>) -> Void)! ``` |

Modified [CFFileDescriptorContext.retain](https://developer.apple.com/documentation/corefoundation/cffiledescriptorcontext/1477599-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)> ``` |
| To | ``` var retain: ((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)! ``` |

Modified [CFFileSecurityClearOptions [struct]](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFFileSecurityClearOptions : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var Owner: CFFileSecurityClearOptions { get }     static var Group: CFFileSecurityClearOptions { get }     static var Mode: CFFileSecurityClearOptions { get }     static var OwnerUUID: CFFileSecurityClearOptions { get }     static var GroupUUID: CFFileSecurityClearOptions { get }     static var AccessControlList: CFFileSecurityClearOptions { get } } ``` | RawOptionSetType |
| To | ``` struct CFFileSecurityClearOptions : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var Owner: CFFileSecurityClearOptions { get }     static var Group: CFFileSecurityClearOptions { get }     static var Mode: CFFileSecurityClearOptions { get }     static var OwnerUUID: CFFileSecurityClearOptions { get }     static var GroupUUID: CFFileSecurityClearOptions { get }     static var AccessControlList: CFFileSecurityClearOptions { get } } ``` | OptionSetType |

Modified [CFGregorianUnitFlags [struct]](https://developer.apple.com/documentation/corefoundation/cfgregorianunitflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFGregorianUnitFlags : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var UnitsYears: CFGregorianUnitFlags { get }     static var UnitsMonths: CFGregorianUnitFlags { get }     static var UnitsDays: CFGregorianUnitFlags { get }     static var UnitsHours: CFGregorianUnitFlags { get }     static var UnitsMinutes: CFGregorianUnitFlags { get }     static var UnitsSeconds: CFGregorianUnitFlags { get }     static var AllUnits: CFGregorianUnitFlags { get } } ``` | RawOptionSetType |
| To | ``` struct CFGregorianUnitFlags : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var UnitsYears: CFGregorianUnitFlags { get }     static var UnitsMonths: CFGregorianUnitFlags { get }     static var UnitsDays: CFGregorianUnitFlags { get }     static var UnitsHours: CFGregorianUnitFlags { get }     static var UnitsMinutes: CFGregorianUnitFlags { get }     static var UnitsSeconds: CFGregorianUnitFlags { get }     static var AllUnits: CFGregorianUnitFlags { get } } ``` | OptionSetType |

Modified [CFMachPortContext [struct]](https://developer.apple.com/documentation/corefoundation/cfmachportcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFMachPortContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |
| To | ``` struct CFMachPortContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!     var release: ((UnsafePointer<Void>) -> Void)!     var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release release: ((UnsafePointer<Void>) -> Void)!, copyDescription copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!) } ``` |

Modified [CFMachPortContext.copyDescription](https://developer.apple.com/documentation/corefoundation/cfmachportcontext/1400944-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)! ``` |

Modified [CFMachPortContext.release](https://developer.apple.com/documentation/corefoundation/cfmachportcontext/1400920-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |
| To | ``` var release: ((UnsafePointer<Void>) -> Void)! ``` |

Modified [CFMachPortContext.retain](https://developer.apple.com/documentation/corefoundation/cfmachportcontext/1400912-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |
| To | ``` var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)! ``` |

Modified [CFMessagePortContext [struct]](https://developer.apple.com/documentation/corefoundation/cfmessageportcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFMessagePortContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |
| To | ``` struct CFMessagePortContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!     var release: ((UnsafePointer<Void>) -> Void)!     var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release release: ((UnsafePointer<Void>) -> Void)!, copyDescription copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!) } ``` |

Modified [CFMessagePortContext.copyDescription](https://developer.apple.com/documentation/corefoundation/cfmessageportcontext/1542175-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)! ``` |

Modified [CFMessagePortContext.release](https://developer.apple.com/documentation/corefoundation/cfmessageportcontext/1542528-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |
| To | ``` var release: ((UnsafePointer<Void>) -> Void)! ``` |

Modified [CFMessagePortContext.retain](https://developer.apple.com/documentation/corefoundation/cfmessageportcontext/1542526-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |
| To | ``` var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)! ``` |

Modified [CFNumberFormatterOptionFlags [struct]](https://developer.apple.com/documentation/corefoundation/cfnumberformatteroptionflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFNumberFormatterOptionFlags : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var ParseIntegersOnly: CFNumberFormatterOptionFlags { get } } ``` | RawOptionSetType |
| To | ``` struct CFNumberFormatterOptionFlags : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var ParseIntegersOnly: CFNumberFormatterOptionFlags { get } } ``` | OptionSetType |

Modified [CFNumberFormatterStyle [enum]](https://developer.apple.com/documentation/corefoundation/cfnumberformatterstyle)

|  | Declaration |
| --- | --- |
| From | ``` enum CFNumberFormatterStyle : CFIndex {     case NoStyle     case DecimalStyle     case CurrencyStyle     case PercentStyle     case ScientificStyle     case SpellOutStyle } ``` |
| To | ``` enum CFNumberFormatterStyle : CFIndex {     case NoStyle     case DecimalStyle     case CurrencyStyle     case PercentStyle     case ScientificStyle     case SpellOutStyle     case OrdinalStyle     case CurrencyISOCodeStyle     case CurrencyPluralStyle     case CurrencyAccountingStyle } ``` |

Modified [CFNumberType [enum]](https://developer.apple.com/documentation/corefoundation/cfnumbertype)

|  | Declaration |
| --- | --- |
| From | ``` enum CFNumberType : CFIndex {     case SInt8Type     case SInt16Type     case SInt32Type     case SInt64Type     case Float32Type     case Float64Type     case CharType     case ShortType     case IntType     case LongType     case LongLongType     case FloatType     case DoubleType     case CFIndexType     case NSIntegerType     case CGFloatType } ``` |
| To | ``` enum CFNumberType : CFIndex {     case SInt8Type     case SInt16Type     case SInt32Type     case SInt64Type     case Float32Type     case Float64Type     case CharType     case ShortType     case IntType     case LongType     case LongLongType     case FloatType     case DoubleType     case CFIndexType     case NSIntegerType     case CGFloatType     static var MaxType: CFNumberType { get } } ``` |

Modified [CFPropertyListMutabilityOptions [struct]](https://developer.apple.com/documentation/corefoundation/cfpropertylistmutabilityoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFPropertyListMutabilityOptions : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var Immutable: CFPropertyListMutabilityOptions { get }     static var MutableContainers: CFPropertyListMutabilityOptions { get }     static var MutableContainersAndLeaves: CFPropertyListMutabilityOptions { get } } ``` | RawOptionSetType |
| To | ``` struct CFPropertyListMutabilityOptions : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var Immutable: CFPropertyListMutabilityOptions { get }     static var MutableContainers: CFPropertyListMutabilityOptions { get }     static var MutableContainersAndLeaves: CFPropertyListMutabilityOptions { get } } ``` | OptionSetType |

Modified [CFRunLoopActivity [struct]](https://developer.apple.com/documentation/corefoundation/cfrunloopactivity)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFRunLoopActivity : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var Entry: CFRunLoopActivity { get }     static var BeforeTimers: CFRunLoopActivity { get }     static var BeforeSources: CFRunLoopActivity { get }     static var BeforeWaiting: CFRunLoopActivity { get }     static var AfterWaiting: CFRunLoopActivity { get }     static var Exit: CFRunLoopActivity { get }     static var AllActivities: CFRunLoopActivity { get } } ``` | RawOptionSetType |
| To | ``` struct CFRunLoopActivity : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var Entry: CFRunLoopActivity { get }     static var BeforeTimers: CFRunLoopActivity { get }     static var BeforeSources: CFRunLoopActivity { get }     static var BeforeWaiting: CFRunLoopActivity { get }     static var AfterWaiting: CFRunLoopActivity { get }     static var Exit: CFRunLoopActivity { get }     static var AllActivities: CFRunLoopActivity { get } } ``` | OptionSetType |

Modified [CFRunLoopObserverContext [struct]](https://developer.apple.com/documentation/corefoundation/cfrunloopobservercontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFRunLoopObserverContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |
| To | ``` struct CFRunLoopObserverContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!     var release: ((UnsafePointer<Void>) -> Void)!     var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release release: ((UnsafePointer<Void>) -> Void)!, copyDescription copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!) } ``` |

Modified [CFRunLoopObserverContext.copyDescription](https://developer.apple.com/documentation/corefoundation/cfrunloopobservercontext/1541528-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)! ``` |

Modified [CFRunLoopObserverContext.release](https://developer.apple.com/documentation/corefoundation/cfrunloopobservercontext/1542732-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |
| To | ``` var release: ((UnsafePointer<Void>) -> Void)! ``` |

Modified [CFRunLoopObserverContext.retain](https://developer.apple.com/documentation/corefoundation/cfrunloopobservercontext/1541985-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |
| To | ``` var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)! ``` |

Modified [CFRunLoopSourceContext [struct]](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFRunLoopSourceContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     var equal: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)>     var hash: CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)>     var schedule: CFunctionPointer<((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)>     var cancel: CFunctionPointer<((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)>     var perform: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>, equal equal: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)>, hash hash: CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)>, schedule schedule: CFunctionPointer<((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)>, cancel cancel: CFunctionPointer<((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)>, perform perform: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>) } ``` |
| To | ``` struct CFRunLoopSourceContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!     var release: ((UnsafePointer<Void>) -> Void)!     var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!     var equal: ((UnsafePointer<Void>, UnsafePointer<Void>) -> DarwinBoolean)!     var hash: ((UnsafePointer<Void>) -> CFHashCode)!     var schedule: ((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)!     var cancel: ((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)!     var perform: ((UnsafeMutablePointer<Void>) -> Void)!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release release: ((UnsafePointer<Void>) -> Void)!, copyDescription copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!, equal equal: ((UnsafePointer<Void>, UnsafePointer<Void>) -> DarwinBoolean)!, hash hash: ((UnsafePointer<Void>) -> CFHashCode)!, schedule schedule: ((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)!, cancel cancel: ((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)!, perform perform: ((UnsafeMutablePointer<Void>) -> Void)!) } ``` |

Modified [CFRunLoopSourceContext.cancel](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext/1541753-cancel)

|  | Declaration |
| --- | --- |
| From | ``` var cancel: CFunctionPointer<((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)> ``` |
| To | ``` var cancel: ((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)! ``` |

Modified [CFRunLoopSourceContext.copyDescription](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext/1542769-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)! ``` |

Modified [CFRunLoopSourceContext.equal](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext/1543639-equal)

|  | Declaration |
| --- | --- |
| From | ``` var equal: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)> ``` |
| To | ``` var equal: ((UnsafePointer<Void>, UnsafePointer<Void>) -> DarwinBoolean)! ``` |

Modified [CFRunLoopSourceContext.hash](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext/1543398-hash)

|  | Declaration |
| --- | --- |
| From | ``` var hash: CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)> ``` |
| To | ``` var hash: ((UnsafePointer<Void>) -> CFHashCode)! ``` |

Modified [CFRunLoopSourceContext.perform](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext/1541994-perform)

|  | Declaration |
| --- | --- |
| From | ``` var perform: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` var perform: ((UnsafeMutablePointer<Void>) -> Void)! ``` |

Modified [CFRunLoopSourceContext.release](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext/1542971-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |
| To | ``` var release: ((UnsafePointer<Void>) -> Void)! ``` |

Modified [CFRunLoopSourceContext.retain](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext/1543359-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |
| To | ``` var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)! ``` |

Modified [CFRunLoopSourceContext.schedule](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext/1542029-schedule)

|  | Declaration |
| --- | --- |
| From | ``` var schedule: CFunctionPointer<((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)> ``` |
| To | ``` var schedule: ((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)! ``` |

Modified [CFRunLoopSourceContext1 [struct]](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1)

|  | Declaration |
| --- | --- |
| From | ``` struct CFRunLoopSourceContext1 {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     var equal: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)>     var hash: CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)>     var getPort: CFunctionPointer<((UnsafeMutablePointer<Void>) -> mach_port_t)>     var perform: CFunctionPointer<((UnsafeMutablePointer<Void>, CFIndex, CFAllocator!, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>, equal equal: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)>, hash hash: CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)>, getPort getPort: CFunctionPointer<((UnsafeMutablePointer<Void>) -> mach_port_t)>, perform perform: CFunctionPointer<((UnsafeMutablePointer<Void>, CFIndex, CFAllocator!, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>) } ``` |
| To | ``` struct CFRunLoopSourceContext1 {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!     var release: ((UnsafePointer<Void>) -> Void)!     var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!     var equal: ((UnsafePointer<Void>, UnsafePointer<Void>) -> DarwinBoolean)!     var hash: ((UnsafePointer<Void>) -> CFHashCode)!     var getPort: ((UnsafeMutablePointer<Void>) -> mach_port_t)!     var perform: ((UnsafeMutablePointer<Void>, CFIndex, CFAllocator!, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release release: ((UnsafePointer<Void>) -> Void)!, copyDescription copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!, equal equal: ((UnsafePointer<Void>, UnsafePointer<Void>) -> DarwinBoolean)!, hash hash: ((UnsafePointer<Void>) -> CFHashCode)!, getPort getPort: ((UnsafeMutablePointer<Void>) -> mach_port_t)!, perform perform: ((UnsafeMutablePointer<Void>, CFIndex, CFAllocator!, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)!) } ``` |

Modified [CFRunLoopSourceContext1.copyDescription](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1/1542892-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)! ``` |

Modified [CFRunLoopSourceContext1.equal](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1/1542103-equal)

|  | Declaration |
| --- | --- |
| From | ``` var equal: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)> ``` |
| To | ``` var equal: ((UnsafePointer<Void>, UnsafePointer<Void>) -> DarwinBoolean)! ``` |

Modified [CFRunLoopSourceContext1.getPort](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1/1542846-getport)

|  | Declaration |
| --- | --- |
| From | ``` var getPort: CFunctionPointer<((UnsafeMutablePointer<Void>) -> mach_port_t)> ``` |
| To | ``` var getPort: ((UnsafeMutablePointer<Void>) -> mach_port_t)! ``` |

Modified [CFRunLoopSourceContext1.hash](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1/1543040-hash)

|  | Declaration |
| --- | --- |
| From | ``` var hash: CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)> ``` |
| To | ``` var hash: ((UnsafePointer<Void>) -> CFHashCode)! ``` |

Modified [CFRunLoopSourceContext1.perform](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1/1543410-perform)

|  | Declaration |
| --- | --- |
| From | ``` var perform: CFunctionPointer<((UnsafeMutablePointer<Void>, CFIndex, CFAllocator!, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)> ``` |
| To | ``` var perform: ((UnsafeMutablePointer<Void>, CFIndex, CFAllocator!, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)! ``` |

Modified [CFRunLoopSourceContext1.release](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1/1542161-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |
| To | ``` var release: ((UnsafePointer<Void>) -> Void)! ``` |

Modified [CFRunLoopSourceContext1.retain](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1/1542518-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |
| To | ``` var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)! ``` |

Modified [CFRunLoopTimerContext [struct]](https://developer.apple.com/documentation/corefoundation/cfrunlooptimercontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFRunLoopTimerContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |
| To | ``` struct CFRunLoopTimerContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!     var release: ((UnsafePointer<Void>) -> Void)!     var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release release: ((UnsafePointer<Void>) -> Void)!, copyDescription copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!) } ``` |

Modified [CFRunLoopTimerContext.copyDescription](https://developer.apple.com/documentation/corefoundation/cfrunlooptimercontext/1541599-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)! ``` |

Modified [CFRunLoopTimerContext.release](https://developer.apple.com/documentation/corefoundation/cfrunlooptimercontext/1542982-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |
| To | ``` var release: ((UnsafePointer<Void>) -> Void)! ``` |

Modified [CFRunLoopTimerContext.retain](https://developer.apple.com/documentation/corefoundation/cfrunlooptimercontext/1543444-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |
| To | ``` var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)! ``` |

Modified [CFSetCallBacks [struct]](https://developer.apple.com/documentation/corefoundation/cfsetcallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CFSetCallBacks {     var version: CFIndex     var retain: CFSetRetainCallBack     var release: CFSetReleaseCallBack     var copyDescription: CFSetCopyDescriptionCallBack     var equal: CFSetEqualCallBack     var hash: CFSetHashCallBack     init()     init(version version: CFIndex, retain retain: CFSetRetainCallBack, release release: CFSetReleaseCallBack, copyDescription copyDescription: CFSetCopyDescriptionCallBack, equal equal: CFSetEqualCallBack, hash hash: CFSetHashCallBack) } ``` |
| To | ``` struct CFSetCallBacks {     var version: CFIndex     var retain: CFSetRetainCallBack!     var release: CFSetReleaseCallBack!     var copyDescription: CFSetCopyDescriptionCallBack!     var equal: CFSetEqualCallBack!     var hash: CFSetHashCallBack!     init()     init(version version: CFIndex, retain retain: CFSetRetainCallBack!, release release: CFSetReleaseCallBack!, copyDescription copyDescription: CFSetCopyDescriptionCallBack!, equal equal: CFSetEqualCallBack!, hash hash: CFSetHashCallBack!) } ``` |

Modified [CFSetCallBacks.copyDescription](https://developer.apple.com/documentation/corefoundation/cfsetcallbacks/1520442-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFSetCopyDescriptionCallBack ``` |
| To | ``` var copyDescription: CFSetCopyDescriptionCallBack! ``` |

Modified [CFSetCallBacks.equal](https://developer.apple.com/documentation/corefoundation/cfsetcallbacks/1520421-equal)

|  | Declaration |
| --- | --- |
| From | ``` var equal: CFSetEqualCallBack ``` |
| To | ``` var equal: CFSetEqualCallBack! ``` |

Modified [CFSetCallBacks.hash](https://developer.apple.com/documentation/corefoundation/cfsetcallbacks/1520417-hash)

|  | Declaration |
| --- | --- |
| From | ``` var hash: CFSetHashCallBack ``` |
| To | ``` var hash: CFSetHashCallBack! ``` |

Modified [CFSetCallBacks.release](https://developer.apple.com/documentation/corefoundation/cfsetcallbacks/1520410-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFSetReleaseCallBack ``` |
| To | ``` var release: CFSetReleaseCallBack! ``` |

Modified [CFSetCallBacks.retain](https://developer.apple.com/documentation/corefoundation/cfsetcallbacks/1520439-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFSetRetainCallBack ``` |
| To | ``` var retain: CFSetRetainCallBack! ``` |

Modified [CFSocketCallBackType [struct]](https://developer.apple.com/documentation/corefoundation/cfsocketcallbacktype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFSocketCallBackType : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var NoCallBack: CFSocketCallBackType { get }     static var ReadCallBack: CFSocketCallBackType { get }     static var AcceptCallBack: CFSocketCallBackType { get }     static var DataCallBack: CFSocketCallBackType { get }     static var ConnectCallBack: CFSocketCallBackType { get }     static var WriteCallBack: CFSocketCallBackType { get } } ``` | RawOptionSetType |
| To | ``` struct CFSocketCallBackType : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var NoCallBack: CFSocketCallBackType { get }     static var ReadCallBack: CFSocketCallBackType { get }     static var AcceptCallBack: CFSocketCallBackType { get }     static var DataCallBack: CFSocketCallBackType { get }     static var ConnectCallBack: CFSocketCallBackType { get }     static var WriteCallBack: CFSocketCallBackType { get } } ``` | OptionSetType |

Modified [CFSocketContext [struct]](https://developer.apple.com/documentation/corefoundation/cfsocketcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFSocketContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |
| To | ``` struct CFSocketContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!     var release: ((UnsafePointer<Void>) -> Void)!     var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release release: ((UnsafePointer<Void>) -> Void)!, copyDescription copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!) } ``` |

Modified [CFSocketContext.copyDescription](https://developer.apple.com/documentation/corefoundation/cfsocketcontext/1542148-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)! ``` |

Modified [CFSocketContext.release](https://developer.apple.com/documentation/corefoundation/cfsocketcontext/1541856-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |
| To | ``` var release: ((UnsafePointer<Void>) -> Void)! ``` |

Modified [CFSocketContext.retain](https://developer.apple.com/documentation/corefoundation/cfsocketcontext/1543095-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |
| To | ``` var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)! ``` |

Modified [CFStreamClientContext [struct]](https://developer.apple.com/documentation/corefoundation/cfstreamclientcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFStreamClientContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>     var release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>, release release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |
| To | ``` struct CFStreamClientContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)!     var release: ((UnsafeMutablePointer<Void>) -> Void)!     var copyDescription: ((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)!, release release: ((UnsafeMutablePointer<Void>) -> Void)!, copyDescription copyDescription: ((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)!) } ``` |

Modified [CFStreamClientContext.copyDescription](https://developer.apple.com/documentation/corefoundation/cfstreamclientcontext/1539745-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: ((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)! ``` |

Modified [CFStreamClientContext.release](https://developer.apple.com/documentation/corefoundation/cfstreamclientcontext/1539664-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` var release: ((UnsafeMutablePointer<Void>) -> Void)! ``` |

Modified [CFStreamClientContext.retain](https://developer.apple.com/documentation/corefoundation/cfstreamclientcontext/1539696-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)> ``` |
| To | ``` var retain: ((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)! ``` |

Modified [CFStreamEventType [struct]](https://developer.apple.com/documentation/corefoundation/cfstreameventtype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFStreamEventType : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var None: CFStreamEventType { get }     static var OpenCompleted: CFStreamEventType { get }     static var HasBytesAvailable: CFStreamEventType { get }     static var CanAcceptBytes: CFStreamEventType { get }     static var ErrorOccurred: CFStreamEventType { get }     static var EndEncountered: CFStreamEventType { get } } ``` | RawOptionSetType |
| To | ``` struct CFStreamEventType : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var None: CFStreamEventType { get }     static var OpenCompleted: CFStreamEventType { get }     static var HasBytesAvailable: CFStreamEventType { get }     static var CanAcceptBytes: CFStreamEventType { get }     static var ErrorOccurred: CFStreamEventType { get }     static var EndEncountered: CFStreamEventType { get } } ``` | OptionSetType |

Modified [CFStringBuiltInEncodings [enum]](https://developer.apple.com/documentation/corefoundation/cfstringbuiltinencodings)

|  | Declaration |
| --- | --- |
| From | ``` enum CFStringBuiltInEncodings : CFStringEncoding {     case MacRoman     case WindowsLatin1     case ISOLatin1     case NextStepLatin     case ASCII     case Unicode     case UTF8     case NonLossyASCII     case UTF16BE     case UTF16LE     case UTF32     case UTF32BE     case UTF32LE } ``` |
| To | ``` enum CFStringBuiltInEncodings : CFStringEncoding {     case MacRoman     case WindowsLatin1     case ISOLatin1     case NextStepLatin     case ASCII     case Unicode     case UTF8     case NonLossyASCII     static var UTF16: CFStringBuiltInEncodings { get }     case UTF16BE     case UTF16LE     case UTF32     case UTF32BE     case UTF32LE } ``` |

Modified [CFStringCompareFlags [struct]](https://developer.apple.com/documentation/corefoundation/cfstringcompareflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFStringCompareFlags : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var CompareCaseInsensitive: CFStringCompareFlags { get }     static var CompareBackwards: CFStringCompareFlags { get }     static var CompareAnchored: CFStringCompareFlags { get }     static var CompareNonliteral: CFStringCompareFlags { get }     static var CompareLocalized: CFStringCompareFlags { get }     static var CompareNumerically: CFStringCompareFlags { get }     static var CompareDiacriticInsensitive: CFStringCompareFlags { get }     static var CompareWidthInsensitive: CFStringCompareFlags { get }     static var CompareForcedOrdering: CFStringCompareFlags { get } } ``` | RawOptionSetType |
| To | ``` struct CFStringCompareFlags : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var CompareCaseInsensitive: CFStringCompareFlags { get }     static var CompareBackwards: CFStringCompareFlags { get }     static var CompareAnchored: CFStringCompareFlags { get }     static var CompareNonliteral: CFStringCompareFlags { get }     static var CompareLocalized: CFStringCompareFlags { get }     static var CompareNumerically: CFStringCompareFlags { get }     static var CompareDiacriticInsensitive: CFStringCompareFlags { get }     static var CompareWidthInsensitive: CFStringCompareFlags { get }     static var CompareForcedOrdering: CFStringCompareFlags { get } } ``` | OptionSetType |

Modified [CFStringEncodings [enum]](https://developer.apple.com/documentation/corefoundation/cfstringencodings)

|  | Declaration |
| --- | --- |
| From | ``` enum CFStringEncodings : CFIndex {     case MacJapanese     case MacChineseTrad     case MacKorean     case MacArabic     case MacHebrew     case MacGreek     case MacCyrillic     case MacDevanagari     case MacGurmukhi     case MacGujarati     case MacOriya     case MacBengali     case MacTamil     case MacTelugu     case MacKannada     case MacMalayalam     case MacSinhalese     case MacBurmese     case MacKhmer     case MacThai     case MacLaotian     case MacGeorgian     case MacArmenian     case MacChineseSimp     case MacTibetan     case MacMongolian     case MacEthiopic     case MacCentralEurRoman     case MacVietnamese     case MacExtArabic     case MacSymbol     case MacDingbats     case MacTurkish     case MacCroatian     case MacIcelandic     case MacRomanian     case MacCeltic     case MacGaelic     case MacFarsi     case MacUkrainian     case MacInuit     case MacVT100     case MacHFS     case ISOLatin2     case ISOLatin3     case ISOLatin4     case ISOLatinCyrillic     case ISOLatinArabic     case ISOLatinGreek     case ISOLatinHebrew     case ISOLatin5     case ISOLatin6     case ISOLatinThai     case ISOLatin7     case ISOLatin8     case ISOLatin9     case ISOLatin10     case DOSLatinUS     case DOSGreek     case DOSBalticRim     case DOSLatin1     case DOSGreek1     case DOSLatin2     case DOSCyrillic     case DOSTurkish     case DOSPortuguese     case DOSIcelandic     case DOSHebrew     case DOSCanadianFrench     case DOSArabic     case DOSNordic     case DOSRussian     case DOSGreek2     case DOSThai     case DOSJapanese     case DOSChineseSimplif     case DOSKorean     case DOSChineseTrad     case WindowsLatin2     case WindowsCyrillic     case WindowsGreek     case WindowsLatin5     case WindowsHebrew     case WindowsArabic     case WindowsBalticRim     case WindowsVietnamese     case WindowsKoreanJohab     case ANSEL     case JIS_X0201_76     case JIS_X0208_83     case JIS_X0208_90     case JIS_X0212_90     case JIS_C6226_78     case ShiftJIS_X0213     case ShiftJIS_X0213_MenKuTen     case GB_2312_80     case GBK_95     case GB_18030_2000     case KSC_5601_87     case KSC_5601_92_Johab     case CNS_11643_92_P1     case CNS_11643_92_P2     case CNS_11643_92_P3     case ISO_2022_JP     case ISO_2022_JP_2     case ISO_2022_JP_1     case ISO_2022_JP_3     case ISO_2022_CN     case ISO_2022_CN_EXT     case ISO_2022_KR     case EUC_JP     case EUC_CN     case EUC_TW     case EUC_KR     case ShiftJIS     case KOI8_R     case Big5     case MacRomanLatin1     case HZ_GB_2312     case Big5_HKSCS_1999     case VISCII     case KOI8_U     case Big5_E     case NextStepJapanese     case EBCDIC_US     case EBCDIC_CP037     case UTF7     case UTF7_IMAP } ``` |
| To | ``` enum CFStringEncodings : CFIndex {     case MacJapanese     case MacChineseTrad     case MacKorean     case MacArabic     case MacHebrew     case MacGreek     case MacCyrillic     case MacDevanagari     case MacGurmukhi     case MacGujarati     case MacOriya     case MacBengali     case MacTamil     case MacTelugu     case MacKannada     case MacMalayalam     case MacSinhalese     case MacBurmese     case MacKhmer     case MacThai     case MacLaotian     case MacGeorgian     case MacArmenian     case MacChineseSimp     case MacTibetan     case MacMongolian     case MacEthiopic     case MacCentralEurRoman     case MacVietnamese     case MacExtArabic     case MacSymbol     case MacDingbats     case MacTurkish     case MacCroatian     case MacIcelandic     case MacRomanian     case MacCeltic     case MacGaelic     case MacFarsi     case MacUkrainian     case MacInuit     case MacVT100     case MacHFS     case ISOLatin2     case ISOLatin3     case ISOLatin4     case ISOLatinCyrillic     case ISOLatinArabic     case ISOLatinGreek     case ISOLatinHebrew     case ISOLatin5     case ISOLatin6     case ISOLatinThai     case ISOLatin7     case ISOLatin8     case ISOLatin9     case ISOLatin10     case DOSLatinUS     case DOSGreek     case DOSBalticRim     case DOSLatin1     case DOSGreek1     case DOSLatin2     case DOSCyrillic     case DOSTurkish     case DOSPortuguese     case DOSIcelandic     case DOSHebrew     case DOSCanadianFrench     case DOSArabic     case DOSNordic     case DOSRussian     case DOSGreek2     case DOSThai     case DOSJapanese     case DOSChineseSimplif     case DOSKorean     case DOSChineseTrad     case WindowsLatin2     case WindowsCyrillic     case WindowsGreek     case WindowsLatin5     case WindowsHebrew     case WindowsArabic     case WindowsBalticRim     case WindowsVietnamese     case WindowsKoreanJohab     case ANSEL     case JIS_X0201_76     case JIS_X0208_83     case JIS_X0208_90     case JIS_X0212_90     case JIS_C6226_78     case ShiftJIS_X0213     case ShiftJIS_X0213_MenKuTen     case GB_2312_80     case GBK_95     case GB_18030_2000     case KSC_5601_87     case KSC_5601_92_Johab     case CNS_11643_92_P1     case CNS_11643_92_P2     case CNS_11643_92_P3     case ISO_2022_JP     case ISO_2022_JP_2     case ISO_2022_JP_1     case ISO_2022_JP_3     case ISO_2022_CN     case ISO_2022_CN_EXT     case ISO_2022_KR     case EUC_JP     case EUC_CN     case EUC_TW     case EUC_KR     case ShiftJIS     case KOI8_R     case Big5     case MacRomanLatin1     case HZ_GB_2312     case Big5_HKSCS_1999     case VISCII     case KOI8_U     case Big5_E     case NextStepJapanese     case EBCDIC_US     case EBCDIC_CP037     case UTF7     case UTF7_IMAP     static var ShiftJIS_X0213_00: CFStringEncodings { get } } ``` |

Modified [CFStringTokenizerTokenType [struct]](https://developer.apple.com/documentation/corefoundation/cfstringtokenizertokentype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFStringTokenizerTokenType : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var None: CFStringTokenizerTokenType { get }     static var Normal: CFStringTokenizerTokenType { get }     static var HasSubTokensMask: CFStringTokenizerTokenType { get }     static var HasDerivedSubTokensMask: CFStringTokenizerTokenType { get }     static var HasHasNumbersMask: CFStringTokenizerTokenType { get }     static var HasNonLettersMask: CFStringTokenizerTokenType { get }     static var IsCJWordMask: CFStringTokenizerTokenType { get } } ``` | RawOptionSetType |
| To | ``` struct CFStringTokenizerTokenType : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var None: CFStringTokenizerTokenType { get }     static var Normal: CFStringTokenizerTokenType { get }     static var HasSubTokensMask: CFStringTokenizerTokenType { get }     static var HasDerivedSubTokensMask: CFStringTokenizerTokenType { get }     static var HasHasNumbersMask: CFStringTokenizerTokenType { get }     static var HasNonLettersMask: CFStringTokenizerTokenType { get }     static var IsCJWordMask: CFStringTokenizerTokenType { get } } ``` | OptionSetType |

Modified [CFTreeContext [struct]](https://developer.apple.com/documentation/corefoundation/cftreecontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFTreeContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFTreeRetainCallBack     var release: CFTreeReleaseCallBack     var copyDescription: CFTreeCopyDescriptionCallBack     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFTreeRetainCallBack, release release: CFTreeReleaseCallBack, copyDescription copyDescription: CFTreeCopyDescriptionCallBack) } ``` |
| To | ``` struct CFTreeContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFTreeRetainCallBack!     var release: CFTreeReleaseCallBack!     var copyDescription: CFTreeCopyDescriptionCallBack!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFTreeRetainCallBack!, release release: CFTreeReleaseCallBack!, copyDescription copyDescription: CFTreeCopyDescriptionCallBack!) } ``` |

Modified [CFTreeContext.copyDescription](https://developer.apple.com/documentation/corefoundation/cftreecontext/1401800-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFTreeCopyDescriptionCallBack ``` |
| To | ``` var copyDescription: CFTreeCopyDescriptionCallBack! ``` |

Modified [CFTreeContext.release](https://developer.apple.com/documentation/corefoundation/cftreecontext/1401779-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFTreeReleaseCallBack ``` |
| To | ``` var release: CFTreeReleaseCallBack! ``` |

Modified [CFTreeContext.retain](https://developer.apple.com/documentation/corefoundation/cftreecontext/1401767-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFTreeRetainCallBack ``` |
| To | ``` var retain: CFTreeRetainCallBack! ``` |

Modified [CFURLBookmarkCreationOptions [struct]](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkcreationoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFURLBookmarkCreationOptions : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var MinimalBookmarkMask: CFURLBookmarkCreationOptions { get }     static var SuitableForBookmarkFile: CFURLBookmarkCreationOptions { get }     static var WithSecurityScope: CFURLBookmarkCreationOptions { get }     static var SecurityScopeAllowOnlyReadAccess: CFURLBookmarkCreationOptions { get }     static var PreferFileIDResolutionMask: CFURLBookmarkCreationOptions { get } } ``` | RawOptionSetType |
| To | ``` struct CFURLBookmarkCreationOptions : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var MinimalBookmarkMask: CFURLBookmarkCreationOptions { get }     static var SuitableForBookmarkFile: CFURLBookmarkCreationOptions { get }     static var WithSecurityScope: CFURLBookmarkCreationOptions { get }     static var SecurityScopeAllowOnlyReadAccess: CFURLBookmarkCreationOptions { get }     static var PreferFileIDResolutionMask: CFURLBookmarkCreationOptions { get } } ``` | OptionSetType |

Modified [CFURLBookmarkResolutionOptions [struct]](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkresolutionoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFURLBookmarkResolutionOptions : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var CFURLBookmarkResolutionWithoutUIMask: CFURLBookmarkResolutionOptions { get }     static var CFURLBookmarkResolutionWithoutMountingMask: CFURLBookmarkResolutionOptions { get }     static var CFURLBookmarkResolutionWithSecurityScope: CFURLBookmarkResolutionOptions { get }     static var CFBookmarkResolutionWithoutUIMask: CFURLBookmarkResolutionOptions { get }     static var CFBookmarkResolutionWithoutMountingMask: CFURLBookmarkResolutionOptions { get } } ``` | RawOptionSetType |
| To | ``` struct CFURLBookmarkResolutionOptions : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var CFURLBookmarkResolutionWithoutUIMask: CFURLBookmarkResolutionOptions { get }     static var CFURLBookmarkResolutionWithoutMountingMask: CFURLBookmarkResolutionOptions { get }     static var CFURLBookmarkResolutionWithSecurityScope: CFURLBookmarkResolutionOptions { get }     static var CFBookmarkResolutionWithoutUIMask: CFURLBookmarkResolutionOptions { get }     static var CFBookmarkResolutionWithoutMountingMask: CFURLBookmarkResolutionOptions { get } } ``` | OptionSetType |

Modified [CFURLEnumeratorOptions [struct]](https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFURLEnumeratorOptions : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var DefaultBehavior: CFURLEnumeratorOptions { get }     static var DescendRecursively: CFURLEnumeratorOptions { get }     static var SkipInvisibles: CFURLEnumeratorOptions { get }     static var GenerateFileReferenceURLs: CFURLEnumeratorOptions { get }     static var SkipPackageContents: CFURLEnumeratorOptions { get }     static var IncludeDirectoriesPreOrder: CFURLEnumeratorOptions { get }     static var IncludeDirectoriesPostOrder: CFURLEnumeratorOptions { get } } ``` | RawOptionSetType |
| To | ``` struct CFURLEnumeratorOptions : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var DefaultBehavior: CFURLEnumeratorOptions { get }     static var DescendRecursively: CFURLEnumeratorOptions { get }     static var SkipInvisibles: CFURLEnumeratorOptions { get }     static var GenerateFileReferenceURLs: CFURLEnumeratorOptions { get }     static var SkipPackageContents: CFURLEnumeratorOptions { get }     static var IncludeDirectoriesPreOrder: CFURLEnumeratorOptions { get }     static var IncludeDirectoriesPostOrder: CFURLEnumeratorOptions { get } } ``` | OptionSetType |

Modified [CFAllocatorAllocateCallBack](https://developer.apple.com/documentation/corefoundation/cfallocatorallocatecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFAllocatorAllocateCallBack = CFunctionPointer<((CFIndex, CFOptionFlags, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)> ``` |
| To | ``` typealias CFAllocatorAllocateCallBack = (CFIndex, CFOptionFlags, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void> ``` |

Modified [CFAllocatorCopyDescriptionCallBack](https://developer.apple.com/documentation/corefoundation/cfallocatorcopydescriptioncallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFAllocatorCopyDescriptionCallBack = CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |
| To | ``` typealias CFAllocatorCopyDescriptionCallBack = (UnsafePointer<Void>) -> Unmanaged<CFString>! ``` |

Modified [CFAllocatorDeallocateCallBack](https://developer.apple.com/documentation/corefoundation/cfallocatordeallocatecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFAllocatorDeallocateCallBack = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFAllocatorDeallocateCallBack = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CFAllocatorPreferredSizeCallBack](https://developer.apple.com/documentation/corefoundation/cfallocatorpreferredsizecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFAllocatorPreferredSizeCallBack = CFunctionPointer<((CFIndex, CFOptionFlags, UnsafeMutablePointer<Void>) -> CFIndex)> ``` |
| To | ``` typealias CFAllocatorPreferredSizeCallBack = (CFIndex, CFOptionFlags, UnsafeMutablePointer<Void>) -> CFIndex ``` |

Modified [CFAllocatorReallocateCallBack](https://developer.apple.com/documentation/corefoundation/cfallocatorreallocatecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFAllocatorReallocateCallBack = CFunctionPointer<((UnsafeMutablePointer<Void>, CFIndex, CFOptionFlags, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)> ``` |
| To | ``` typealias CFAllocatorReallocateCallBack = (UnsafeMutablePointer<Void>, CFIndex, CFOptionFlags, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void> ``` |

Modified [CFAllocatorReleaseCallBack](https://developer.apple.com/documentation/corefoundation/cfallocatorreleasecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFAllocatorReleaseCallBack = CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFAllocatorReleaseCallBack = (UnsafePointer<Void>) -> Void ``` |

Modified [CFAllocatorRetainCallBack](https://developer.apple.com/documentation/corefoundation/cfallocatorretaincallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFAllocatorRetainCallBack = CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |
| To | ``` typealias CFAllocatorRetainCallBack = (UnsafePointer<Void>) -> UnsafePointer<Void> ``` |

Modified [CFArrayApplierFunction](https://developer.apple.com/documentation/corefoundation/cfarrayapplierfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFArrayApplierFunction = CFunctionPointer<((UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFArrayApplierFunction = (UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CFArrayApplyFunction(_: CFArray!, _: CFRange, _: CFArrayApplierFunction!, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/corefoundation/1388737-cfarrayapplyfunction)

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayApplyFunction(_ theArray: CFArray!, _ range: CFRange, _ applier: CFArrayApplierFunction, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func CFArrayApplyFunction(_ theArray: CFArray!, _ range: CFRange, _ applier: CFArrayApplierFunction!, _ context: UnsafeMutablePointer<Void>) ``` |

Modified [CFArrayBSearchValues(_: CFArray!, _: CFRange, _: UnsafePointer<Void>, _: CFComparatorFunction!, _: UnsafeMutablePointer<Void>) -> CFIndex](https://developer.apple.com/documentation/corefoundation/1388773-cfarraybsearchvalues)

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayBSearchValues(_ theArray: CFArray!, _ range: CFRange, _ value: UnsafePointer<Void>, _ comparator: CFComparatorFunction, _ context: UnsafeMutablePointer<Void>) -> CFIndex ``` |
| To | ``` func CFArrayBSearchValues(_ theArray: CFArray!, _ range: CFRange, _ value: UnsafePointer<Void>, _ comparator: CFComparatorFunction!, _ context: UnsafeMutablePointer<Void>) -> CFIndex ``` |

Modified [CFArrayContainsValue(_: CFArray!, _: CFRange, _: UnsafePointer<Void>) -> Bool](https://developer.apple.com/documentation/corefoundation/1388801-cfarraycontainsvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayContainsValue(_ theArray: CFArray!, _ range: CFRange, _ value: UnsafePointer<Void>) -> Boolean ``` |
| To | ``` func CFArrayContainsValue(_ theArray: CFArray!, _ range: CFRange, _ value: UnsafePointer<Void>) -> Bool ``` |

Modified [CFArrayCopyDescriptionCallBack](https://developer.apple.com/documentation/corefoundation/cfarraycopydescriptioncallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFArrayCopyDescriptionCallBack = CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |
| To | ``` typealias CFArrayCopyDescriptionCallBack = (UnsafePointer<Void>) -> Unmanaged<CFString>! ``` |

Modified [CFArrayEqualCallBack](https://developer.apple.com/documentation/corefoundation/cfarrayequalcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFArrayEqualCallBack = CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)> ``` |
| To | ``` typealias CFArrayEqualCallBack = (UnsafePointer<Void>, UnsafePointer<Void>) -> DarwinBoolean ``` |

Modified [CFArrayReleaseCallBack](https://developer.apple.com/documentation/corefoundation/cfarrayreleasecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFArrayReleaseCallBack = CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFArrayReleaseCallBack = (CFAllocator!, UnsafePointer<Void>) -> Void ``` |

Modified [CFArrayRetainCallBack](https://developer.apple.com/documentation/corefoundation/cfarrayretaincallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFArrayRetainCallBack = CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |
| To | ``` typealias CFArrayRetainCallBack = (CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void> ``` |

Modified [CFArraySortValues(_: CFMutableArray!, _: CFRange, _: CFComparatorFunction!, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/corefoundation/1388749-cfarraysortvalues)

|  | Declaration |
| --- | --- |
| From | ``` func CFArraySortValues(_ theArray: CFMutableArray!, _ range: CFRange, _ comparator: CFComparatorFunction, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func CFArraySortValues(_ theArray: CFMutableArray!, _ range: CFRange, _ comparator: CFComparatorFunction!, _ context: UnsafeMutablePointer<Void>) ``` |

Modified [CFAttributedStringSetAttributes(_: CFMutableAttributedString!, _: CFRange, _: CFDictionary!, _: Bool)](https://developer.apple.com/documentation/corefoundation/1541808-cfattributedstringsetattributes)

|  | Declaration |
| --- | --- |
| From | ``` func CFAttributedStringSetAttributes(_ aStr: CFMutableAttributedString!, _ range: CFRange, _ replacement: CFDictionary!, _ clearOtherAttributes: Boolean) ``` |
| To | ``` func CFAttributedStringSetAttributes(_ aStr: CFMutableAttributedString!, _ range: CFRange, _ replacement: CFDictionary!, _ clearOtherAttributes: Bool) ``` |

Modified [CFBagApplierFunction](https://developer.apple.com/documentation/corefoundation/cfbagapplierfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFBagApplierFunction = CFunctionPointer<((UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFBagApplierFunction = (UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CFBagApplyFunction(_: CFBag!, _: CFBagApplierFunction!, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/corefoundation/1469283-cfbagapplyfunction)

|  | Declaration |
| --- | --- |
| From | ``` func CFBagApplyFunction(_ theBag: CFBag!, _ applier: CFBagApplierFunction, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func CFBagApplyFunction(_ theBag: CFBag!, _ applier: CFBagApplierFunction!, _ context: UnsafeMutablePointer<Void>) ``` |

Modified [CFBagContainsValue(_: CFBag!, _: UnsafePointer<Void>) -> Bool](https://developer.apple.com/documentation/corefoundation/1469322-cfbagcontainsvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFBagContainsValue(_ theBag: CFBag!, _ value: UnsafePointer<Void>) -> Boolean ``` |
| To | ``` func CFBagContainsValue(_ theBag: CFBag!, _ value: UnsafePointer<Void>) -> Bool ``` |

Modified [CFBagCopyDescriptionCallBack](https://developer.apple.com/documentation/corefoundation/cfbagcopydescriptioncallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFBagCopyDescriptionCallBack = CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |
| To | ``` typealias CFBagCopyDescriptionCallBack = (UnsafePointer<Void>) -> Unmanaged<CFString>! ``` |

Modified [CFBagEqualCallBack](https://developer.apple.com/documentation/corefoundation/cfbagequalcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFBagEqualCallBack = CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)> ``` |
| To | ``` typealias CFBagEqualCallBack = (UnsafePointer<Void>, UnsafePointer<Void>) -> DarwinBoolean ``` |

Modified [CFBagGetValueIfPresent(_: CFBag!, _: UnsafePointer<Void>, _: UnsafeMutablePointer<UnsafePointer<Void>>) -> Bool](https://developer.apple.com/documentation/corefoundation/1469314-cfbaggetvalueifpresent)

|  | Declaration |
| --- | --- |
| From | ``` func CFBagGetValueIfPresent(_ theBag: CFBag!, _ candidate: UnsafePointer<Void>, _ value: UnsafeMutablePointer<UnsafePointer<Void>>) -> Boolean ``` |
| To | ``` func CFBagGetValueIfPresent(_ theBag: CFBag!, _ candidate: UnsafePointer<Void>, _ value: UnsafeMutablePointer<UnsafePointer<Void>>) -> Bool ``` |

Modified [CFBagHashCallBack](https://developer.apple.com/documentation/corefoundation/cfbaghashcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFBagHashCallBack = CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)> ``` |
| To | ``` typealias CFBagHashCallBack = (UnsafePointer<Void>) -> CFHashCode ``` |

Modified [CFBagReleaseCallBack](https://developer.apple.com/documentation/corefoundation/cfbagreleasecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFBagReleaseCallBack = CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFBagReleaseCallBack = (CFAllocator!, UnsafePointer<Void>) -> Void ``` |

Modified [CFBagRetainCallBack](https://developer.apple.com/documentation/corefoundation/cfbagretaincallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFBagRetainCallBack = CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |
| To | ``` typealias CFBagRetainCallBack = (CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void> ``` |

Modified [CFBinaryHeapApplierFunction](https://developer.apple.com/documentation/corefoundation/cfbinaryheapapplierfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFBinaryHeapApplierFunction = CFunctionPointer<((UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFBinaryHeapApplierFunction = (UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CFBinaryHeapApplyFunction(_: CFBinaryHeap!, _: CFBinaryHeapApplierFunction!, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/corefoundation/1509308-cfbinaryheapapplyfunction)

|  | Declaration |
| --- | --- |
| From | ``` func CFBinaryHeapApplyFunction(_ heap: CFBinaryHeap!, _ applier: CFBinaryHeapApplierFunction, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func CFBinaryHeapApplyFunction(_ heap: CFBinaryHeap!, _ applier: CFBinaryHeapApplierFunction!, _ context: UnsafeMutablePointer<Void>) ``` |

Modified [CFBinaryHeapContainsValue(_: CFBinaryHeap!, _: UnsafePointer<Void>) -> Bool](https://developer.apple.com/documentation/corefoundation/1509305-cfbinaryheapcontainsvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFBinaryHeapContainsValue(_ heap: CFBinaryHeap!, _ value: UnsafePointer<Void>) -> Boolean ``` |
| To | ``` func CFBinaryHeapContainsValue(_ heap: CFBinaryHeap!, _ value: UnsafePointer<Void>) -> Bool ``` |

Modified [CFBinaryHeapGetMinimumIfPresent(_: CFBinaryHeap!, _: UnsafeMutablePointer<UnsafePointer<Void>>) -> Bool](https://developer.apple.com/documentation/corefoundation/1509310-cfbinaryheapgetminimumifpresent)

|  | Declaration |
| --- | --- |
| From | ``` func CFBinaryHeapGetMinimumIfPresent(_ heap: CFBinaryHeap!, _ value: UnsafeMutablePointer<UnsafePointer<Void>>) -> Boolean ``` |
| To | ``` func CFBinaryHeapGetMinimumIfPresent(_ heap: CFBinaryHeap!, _ value: UnsafeMutablePointer<UnsafePointer<Void>>) -> Bool ``` |

Modified [CFBitVectorContainsBit(_: CFBitVector!, _: CFRange, _: CFBit) -> Bool](https://developer.apple.com/documentation/corefoundation/1543534-cfbitvectorcontainsbit)

|  | Declaration |
| --- | --- |
| From | ``` func CFBitVectorContainsBit(_ bv: CFBitVector!, _ range: CFRange, _ value: CFBit) -> Boolean ``` |
| To | ``` func CFBitVectorContainsBit(_ bv: CFBitVector!, _ range: CFRange, _ value: CFBit) -> Bool ``` |

Modified [CFBooleanGetValue(_: CFBoolean!) -> Bool](https://developer.apple.com/documentation/corefoundation/1541447-cfbooleangetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFBooleanGetValue(_ boolean: CFBoolean!) -> Boolean ``` |
| To | ``` func CFBooleanGetValue(_ boolean: CFBoolean!) -> Bool ``` |

Modified [CFBundleGetPackageInfoInDirectory(_: CFURL!, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutablePointer<UInt32>) -> Bool](https://developer.apple.com/documentation/corefoundation/1537156-cfbundlegetpackageinfoindirector)

|  | Declaration |
| --- | --- |
| From | ``` func CFBundleGetPackageInfoInDirectory(_ url: CFURL!, _ packageType: UnsafeMutablePointer<UInt32>, _ packageCreator: UnsafeMutablePointer<UInt32>) -> Boolean ``` |
| To | ``` func CFBundleGetPackageInfoInDirectory(_ url: CFURL!, _ packageType: UnsafeMutablePointer<UInt32>, _ packageCreator: UnsafeMutablePointer<UInt32>) -> Bool ``` |

Modified [CFBundleIsExecutableLoaded(_: CFBundle!) -> Bool](https://developer.apple.com/documentation/corefoundation/1537151-cfbundleisexecutableloaded)

|  | Declaration |
| --- | --- |
| From | ``` func CFBundleIsExecutableLoaded(_ bundle: CFBundle!) -> Boolean ``` |
| To | ``` func CFBundleIsExecutableLoaded(_ bundle: CFBundle!) -> Bool ``` |

Modified [CFBundleLoadExecutable(_: CFBundle!) -> Bool](https://developer.apple.com/documentation/corefoundation/1537116-cfbundleloadexecutable)

|  | Declaration |
| --- | --- |
| From | ``` func CFBundleLoadExecutable(_ bundle: CFBundle!) -> Boolean ``` |
| To | ``` func CFBundleLoadExecutable(_ bundle: CFBundle!) -> Bool ``` |

Modified [CFBundleLoadExecutableAndReturnError(_: CFBundle!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/corefoundation/1537114-cfbundleloadexecutableandreturne)

|  | Declaration |
| --- | --- |
| From | ``` func CFBundleLoadExecutableAndReturnError(_ bundle: CFBundle!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean ``` |
| To | ``` func CFBundleLoadExecutableAndReturnError(_ bundle: CFBundle!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [CFBundlePreflightExecutable(_: CFBundle!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/corefoundation/1537128-cfbundlepreflightexecutable)

|  | Declaration |
| --- | --- |
| From | ``` func CFBundlePreflightExecutable(_ bundle: CFBundle!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean ``` |
| To | ``` func CFBundlePreflightExecutable(_ bundle: CFBundle!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [CFCalendarGetTimeRangeOfUnit(_: CFCalendar!, _: CFCalendarUnit, _: CFAbsoluteTime, _: UnsafeMutablePointer<CFAbsoluteTime>, _: UnsafeMutablePointer<CFTimeInterval>) -> Bool](https://developer.apple.com/documentation/corefoundation/1533501-cfcalendargettimerangeofunit)

|  | Declaration |
| --- | --- |
| From | ``` func CFCalendarGetTimeRangeOfUnit(_ calendar: CFCalendar!, _ unit: CFCalendarUnit, _ at: CFAbsoluteTime, _ startp: UnsafeMutablePointer<CFAbsoluteTime>, _ tip: UnsafeMutablePointer<CFTimeInterval>) -> Boolean ``` |
| To | ``` func CFCalendarGetTimeRangeOfUnit(_ calendar: CFCalendar!, _ unit: CFCalendarUnit, _ at: CFAbsoluteTime, _ startp: UnsafeMutablePointer<CFAbsoluteTime>, _ tip: UnsafeMutablePointer<CFTimeInterval>) -> Bool ``` |

Modified [CFCharacterSetHasMemberInPlane(_: CFCharacterSet!, _: CFIndex) -> Bool](https://developer.apple.com/documentation/corefoundation/1542152-cfcharactersethasmemberinplane)

|  | Declaration |
| --- | --- |
| From | ``` func CFCharacterSetHasMemberInPlane(_ theSet: CFCharacterSet!, _ thePlane: CFIndex) -> Boolean ``` |
| To | ``` func CFCharacterSetHasMemberInPlane(_ theSet: CFCharacterSet!, _ thePlane: CFIndex) -> Bool ``` |

Modified [CFCharacterSetIsCharacterMember(_: CFCharacterSet!, _: UniChar) -> Bool](https://developer.apple.com/documentation/corefoundation/1542024-cfcharactersetischaractermember)

|  | Declaration |
| --- | --- |
| From | ``` func CFCharacterSetIsCharacterMember(_ theSet: CFCharacterSet!, _ theChar: UniChar) -> Boolean ``` |
| To | ``` func CFCharacterSetIsCharacterMember(_ theSet: CFCharacterSet!, _ theChar: UniChar) -> Bool ``` |

Modified [CFCharacterSetIsLongCharacterMember(_: CFCharacterSet!, _: UTF32Char) -> Bool](https://developer.apple.com/documentation/corefoundation/1542959-cfcharactersetislongcharactermem)

|  | Declaration |
| --- | --- |
| From | ``` func CFCharacterSetIsLongCharacterMember(_ theSet: CFCharacterSet!, _ theChar: UTF32Char) -> Boolean ``` |
| To | ``` func CFCharacterSetIsLongCharacterMember(_ theSet: CFCharacterSet!, _ theChar: UTF32Char) -> Bool ``` |

Modified [CFCharacterSetIsSupersetOfSet(_: CFCharacterSet!, _: CFCharacterSet!) -> Bool](https://developer.apple.com/documentation/corefoundation/1542915-cfcharactersetissupersetofset)

|  | Declaration |
| --- | --- |
| From | ``` func CFCharacterSetIsSupersetOfSet(_ theSet: CFCharacterSet!, _ theOtherset: CFCharacterSet!) -> Boolean ``` |
| To | ``` func CFCharacterSetIsSupersetOfSet(_ theSet: CFCharacterSet!, _ theOtherset: CFCharacterSet!) -> Bool ``` |

Modified [CFComparatorFunction](https://developer.apple.com/documentation/corefoundation/cfcomparatorfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFComparatorFunction = CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> CFComparisonResult)> ``` |
| To | ``` typealias CFComparatorFunction = (UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> CFComparisonResult ``` |

Modified [CFDateFormatterGetAbsoluteTimeFromString(_: CFDateFormatter!, _: CFString!, _: UnsafeMutablePointer<CFRange>, _: UnsafeMutablePointer<CFAbsoluteTime>) -> Bool](https://developer.apple.com/documentation/corefoundation/1396232-cfdateformattergetabsolutetimefr)

|  | Declaration |
| --- | --- |
| From | ``` func CFDateFormatterGetAbsoluteTimeFromString(_ formatter: CFDateFormatter!, _ string: CFString!, _ rangep: UnsafeMutablePointer<CFRange>, _ atp: UnsafeMutablePointer<CFAbsoluteTime>) -> Boolean ``` |
| To | ``` func CFDateFormatterGetAbsoluteTimeFromString(_ formatter: CFDateFormatter!, _ string: CFString!, _ rangep: UnsafeMutablePointer<CFRange>, _ atp: UnsafeMutablePointer<CFAbsoluteTime>) -> Bool ``` |

Modified [CFDictionaryApplierFunction](https://developer.apple.com/documentation/corefoundation/cfdictionaryapplierfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFDictionaryApplierFunction = CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFDictionaryApplierFunction = (UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CFDictionaryApplyFunction(_: CFDictionary!, _: CFDictionaryApplierFunction!, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/corefoundation/1516745-cfdictionaryapplyfunction)

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryApplyFunction(_ theDict: CFDictionary!, _ applier: CFDictionaryApplierFunction, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func CFDictionaryApplyFunction(_ theDict: CFDictionary!, _ applier: CFDictionaryApplierFunction!, _ context: UnsafeMutablePointer<Void>) ``` |

Modified [CFDictionaryContainsKey(_: CFDictionary!, _: UnsafePointer<Void>) -> Bool](https://developer.apple.com/documentation/corefoundation/1516808-cfdictionarycontainskey)

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryContainsKey(_ theDict: CFDictionary!, _ key: UnsafePointer<Void>) -> Boolean ``` |
| To | ``` func CFDictionaryContainsKey(_ theDict: CFDictionary!, _ key: UnsafePointer<Void>) -> Bool ``` |

Modified [CFDictionaryContainsValue(_: CFDictionary!, _: UnsafePointer<Void>) -> Bool](https://developer.apple.com/documentation/corefoundation/1516809-cfdictionarycontainsvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryContainsValue(_ theDict: CFDictionary!, _ value: UnsafePointer<Void>) -> Boolean ``` |
| To | ``` func CFDictionaryContainsValue(_ theDict: CFDictionary!, _ value: UnsafePointer<Void>) -> Bool ``` |

Modified [CFDictionaryCopyDescriptionCallBack](https://developer.apple.com/documentation/corefoundation/cfdictionarycopydescriptioncallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFDictionaryCopyDescriptionCallBack = CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |
| To | ``` typealias CFDictionaryCopyDescriptionCallBack = (UnsafePointer<Void>) -> Unmanaged<CFString>! ``` |

Modified [CFDictionaryEqualCallBack](https://developer.apple.com/documentation/corefoundation/cfdictionaryequalcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFDictionaryEqualCallBack = CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)> ``` |
| To | ``` typealias CFDictionaryEqualCallBack = (UnsafePointer<Void>, UnsafePointer<Void>) -> DarwinBoolean ``` |

Modified [CFDictionaryGetValueIfPresent(_: CFDictionary!, _: UnsafePointer<Void>, _: UnsafeMutablePointer<UnsafePointer<Void>>) -> Bool](https://developer.apple.com/documentation/corefoundation/1516739-cfdictionarygetvalueifpresent)

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryGetValueIfPresent(_ theDict: CFDictionary!, _ key: UnsafePointer<Void>, _ value: UnsafeMutablePointer<UnsafePointer<Void>>) -> Boolean ``` |
| To | ``` func CFDictionaryGetValueIfPresent(_ theDict: CFDictionary!, _ key: UnsafePointer<Void>, _ value: UnsafeMutablePointer<UnsafePointer<Void>>) -> Bool ``` |

Modified [CFDictionaryHashCallBack](https://developer.apple.com/documentation/corefoundation/cfdictionaryhashcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFDictionaryHashCallBack = CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)> ``` |
| To | ``` typealias CFDictionaryHashCallBack = (UnsafePointer<Void>) -> CFHashCode ``` |

Modified [CFDictionaryReleaseCallBack](https://developer.apple.com/documentation/corefoundation/cfdictionaryreleasecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFDictionaryReleaseCallBack = CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFDictionaryReleaseCallBack = (CFAllocator!, UnsafePointer<Void>) -> Void ``` |

Modified [CFDictionaryRetainCallBack](https://developer.apple.com/documentation/corefoundation/cfdictionaryretaincallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFDictionaryRetainCallBack = CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |
| To | ``` typealias CFDictionaryRetainCallBack = (CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void> ``` |

Modified [CFEqual(_: AnyObject!, _: AnyObject!) -> Bool](https://developer.apple.com/documentation/corefoundation/1521287-cfequal)

|  | Declaration |
| --- | --- |
| From | ``` func CFEqual(_ cf1: AnyObject!, _ cf2: AnyObject!) -> Boolean ``` |
| To | ``` func CFEqual(_ cf1: AnyObject!, _ cf2: AnyObject!) -> Bool ``` |

Modified [CFFileDescriptorCallBack](https://developer.apple.com/documentation/corefoundation/cffiledescriptorcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFFileDescriptorCallBack = CFunctionPointer<((CFFileDescriptor!, CFOptionFlags, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFFileDescriptorCallBack = (CFFileDescriptor!, CFOptionFlags, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CFFileDescriptorCreate(_: CFAllocator!, _: CFFileDescriptorNativeDescriptor, _: Bool, _: CFFileDescriptorCallBack!, _: UnsafePointer<CFFileDescriptorContext>) -> CFFileDescriptor!](https://developer.apple.com/documentation/corefoundation/1477591-cffiledescriptorcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFFileDescriptorCreate(_ allocator: CFAllocator!, _ fd: CFFileDescriptorNativeDescriptor, _ closeOnInvalidate: Boolean, _ callout: CFFileDescriptorCallBack, _ context: UnsafePointer<CFFileDescriptorContext>) -> CFFileDescriptor! ``` |
| To | ``` func CFFileDescriptorCreate(_ allocator: CFAllocator!, _ fd: CFFileDescriptorNativeDescriptor, _ closeOnInvalidate: Bool, _ callout: CFFileDescriptorCallBack!, _ context: UnsafePointer<CFFileDescriptorContext>) -> CFFileDescriptor! ``` |

Modified [CFFileDescriptorIsValid(_: CFFileDescriptor!) -> Bool](https://developer.apple.com/documentation/corefoundation/1477575-cffiledescriptorisvalid)

|  | Declaration |
| --- | --- |
| From | ``` func CFFileDescriptorIsValid(_ f: CFFileDescriptor!) -> Boolean ``` |
| To | ``` func CFFileDescriptorIsValid(_ f: CFFileDescriptor!) -> Bool ``` |

Modified [CFFileSecurityClearProperties(_: CFFileSecurity!, _: CFFileSecurityClearOptions) -> Bool](https://developer.apple.com/documentation/corefoundation/1426500-cffilesecurityclearproperties)

|  | Declaration |
| --- | --- |
| From | ``` func CFFileSecurityClearProperties(_ fileSec: CFFileSecurity!, _ clearPropertyMask: CFFileSecurityClearOptions) -> Boolean ``` |
| To | ``` func CFFileSecurityClearProperties(_ fileSec: CFFileSecurity!, _ clearPropertyMask: CFFileSecurityClearOptions) -> Bool ``` |

Modified [CFFileSecurityCopyAccessControlList(_: CFFileSecurity!, _: UnsafeMutablePointer<acl_t>) -> Bool](https://developer.apple.com/documentation/corefoundation/1426508-cffilesecuritycopyaccesscontroll)

|  | Declaration |
| --- | --- |
| From | ``` func CFFileSecurityCopyAccessControlList(_ fileSec: CFFileSecurity!, _ accessControlList: UnsafeMutablePointer<acl_t>) -> Boolean ``` |
| To | ``` func CFFileSecurityCopyAccessControlList(_ fileSec: CFFileSecurity!, _ accessControlList: UnsafeMutablePointer<acl_t>) -> Bool ``` |

Modified [CFFileSecurityCopyGroupUUID(_: CFFileSecurity!, _: UnsafeMutablePointer<Unmanaged<CFUUID>?>) -> Bool](https://developer.apple.com/documentation/corefoundation/1426512-cffilesecuritycopygroupuuid)

|  | Declaration |
| --- | --- |
| From | ``` func CFFileSecurityCopyGroupUUID(_ fileSec: CFFileSecurity!, _ groupUUID: UnsafeMutablePointer<Unmanaged<CFUUID>?>) -> Boolean ``` |
| To | ``` func CFFileSecurityCopyGroupUUID(_ fileSec: CFFileSecurity!, _ groupUUID: UnsafeMutablePointer<Unmanaged<CFUUID>?>) -> Bool ``` |

Modified [CFFileSecurityCopyOwnerUUID(_: CFFileSecurity!, _: UnsafeMutablePointer<Unmanaged<CFUUID>?>) -> Bool](https://developer.apple.com/documentation/corefoundation/1426519-cffilesecuritycopyowneruuid)

|  | Declaration |
| --- | --- |
| From | ``` func CFFileSecurityCopyOwnerUUID(_ fileSec: CFFileSecurity!, _ ownerUUID: UnsafeMutablePointer<Unmanaged<CFUUID>?>) -> Boolean ``` |
| To | ``` func CFFileSecurityCopyOwnerUUID(_ fileSec: CFFileSecurity!, _ ownerUUID: UnsafeMutablePointer<Unmanaged<CFUUID>?>) -> Bool ``` |

Modified [CFFileSecurityGetGroup(_: CFFileSecurity!, _: UnsafeMutablePointer<gid_t>) -> Bool](https://developer.apple.com/documentation/corefoundation/1426526-cffilesecuritygetgroup)

|  | Declaration |
| --- | --- |
| From | ``` func CFFileSecurityGetGroup(_ fileSec: CFFileSecurity!, _ group: UnsafeMutablePointer<gid_t>) -> Boolean ``` |
| To | ``` func CFFileSecurityGetGroup(_ fileSec: CFFileSecurity!, _ group: UnsafeMutablePointer<gid_t>) -> Bool ``` |

Modified [CFFileSecurityGetMode(_: CFFileSecurity!, _: UnsafeMutablePointer<mode_t>) -> Bool](https://developer.apple.com/documentation/corefoundation/1426517-cffilesecuritygetmode)

|  | Declaration |
| --- | --- |
| From | ``` func CFFileSecurityGetMode(_ fileSec: CFFileSecurity!, _ mode: UnsafeMutablePointer<mode_t>) -> Boolean ``` |
| To | ``` func CFFileSecurityGetMode(_ fileSec: CFFileSecurity!, _ mode: UnsafeMutablePointer<mode_t>) -> Bool ``` |

Modified [CFFileSecurityGetOwner(_: CFFileSecurity!, _: UnsafeMutablePointer<uid_t>) -> Bool](https://developer.apple.com/documentation/corefoundation/1426516-cffilesecuritygetowner)

|  | Declaration |
| --- | --- |
| From | ``` func CFFileSecurityGetOwner(_ fileSec: CFFileSecurity!, _ owner: UnsafeMutablePointer<uid_t>) -> Boolean ``` |
| To | ``` func CFFileSecurityGetOwner(_ fileSec: CFFileSecurity!, _ owner: UnsafeMutablePointer<uid_t>) -> Bool ``` |

Modified [CFFileSecuritySetAccessControlList(_: CFFileSecurity!, _: acl_t) -> Bool](https://developer.apple.com/documentation/corefoundation/1426506-cffilesecuritysetaccesscontrolli)

|  | Declaration |
| --- | --- |
| From | ``` func CFFileSecuritySetAccessControlList(_ fileSec: CFFileSecurity!, _ accessControlList: acl_t) -> Boolean ``` |
| To | ``` func CFFileSecuritySetAccessControlList(_ fileSec: CFFileSecurity!, _ accessControlList: acl_t) -> Bool ``` |

Modified [CFFileSecuritySetGroup(_: CFFileSecurity!, _: gid_t) -> Bool](https://developer.apple.com/documentation/corefoundation/1426524-cffilesecuritysetgroup)

|  | Declaration |
| --- | --- |
| From | ``` func CFFileSecuritySetGroup(_ fileSec: CFFileSecurity!, _ group: gid_t) -> Boolean ``` |
| To | ``` func CFFileSecuritySetGroup(_ fileSec: CFFileSecurity!, _ group: gid_t) -> Bool ``` |

Modified [CFFileSecuritySetGroupUUID(_: CFFileSecurity!, _: CFUUID!) -> Bool](https://developer.apple.com/documentation/corefoundation/1426492-cffilesecuritysetgroupuuid)

|  | Declaration |
| --- | --- |
| From | ``` func CFFileSecuritySetGroupUUID(_ fileSec: CFFileSecurity!, _ groupUUID: CFUUID!) -> Boolean ``` |
| To | ``` func CFFileSecuritySetGroupUUID(_ fileSec: CFFileSecurity!, _ groupUUID: CFUUID!) -> Bool ``` |

Modified [CFFileSecuritySetMode(_: CFFileSecurity!, _: mode_t) -> Bool](https://developer.apple.com/documentation/corefoundation/1426496-cffilesecuritysetmode)

|  | Declaration |
| --- | --- |
| From | ``` func CFFileSecuritySetMode(_ fileSec: CFFileSecurity!, _ mode: mode_t) -> Boolean ``` |
| To | ``` func CFFileSecuritySetMode(_ fileSec: CFFileSecurity!, _ mode: mode_t) -> Bool ``` |

Modified [CFFileSecuritySetOwner(_: CFFileSecurity!, _: uid_t) -> Bool](https://developer.apple.com/documentation/corefoundation/1426528-cffilesecuritysetowner)

|  | Declaration |
| --- | --- |
| From | ``` func CFFileSecuritySetOwner(_ fileSec: CFFileSecurity!, _ owner: uid_t) -> Boolean ``` |
| To | ``` func CFFileSecuritySetOwner(_ fileSec: CFFileSecurity!, _ owner: uid_t) -> Bool ``` |

Modified [CFFileSecuritySetOwnerUUID(_: CFFileSecurity!, _: CFUUID!) -> Bool](https://developer.apple.com/documentation/corefoundation/1426494-cffilesecuritysetowneruuid)

|  | Declaration |
| --- | --- |
| From | ``` func CFFileSecuritySetOwnerUUID(_ fileSec: CFFileSecurity!, _ ownerUUID: CFUUID!) -> Boolean ``` |
| To | ``` func CFFileSecuritySetOwnerUUID(_ fileSec: CFFileSecurity!, _ ownerUUID: CFUUID!) -> Bool ``` |

Modified [CFGregorianDateIsValid(_: CFGregorianDate, _: CFOptionFlags) -> Bool](https://developer.apple.com/documentation/corefoundation/1543317-cfgregoriandateisvalid)

|  | Declaration |
| --- | --- |
| From | ``` func CFGregorianDateIsValid(_ gdate: CFGregorianDate, _ unitFlags: CFOptionFlags) -> Boolean ``` |
| To | ``` func CFGregorianDateIsValid(_ gdate: CFGregorianDate, _ unitFlags: CFOptionFlags) -> Bool ``` |

Modified [CFMachPortCallBack](https://developer.apple.com/documentation/corefoundation/cfmachportcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFMachPortCallBack = CFunctionPointer<((CFMachPort!, UnsafeMutablePointer<Void>, CFIndex, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFMachPortCallBack = (CFMachPort!, UnsafeMutablePointer<Void>, CFIndex, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CFMachPortCreate(_: CFAllocator!, _: CFMachPortCallBack!, _: UnsafeMutablePointer<CFMachPortContext>, _: UnsafeMutablePointer<DarwinBoolean>) -> CFMachPort!](https://developer.apple.com/documentation/corefoundation/1400934-cfmachportcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFMachPortCreate(_ allocator: CFAllocator!, _ callout: CFMachPortCallBack, _ context: UnsafeMutablePointer<CFMachPortContext>, _ shouldFreeInfo: UnsafeMutablePointer<Boolean>) -> CFMachPort! ``` |
| To | ``` func CFMachPortCreate(_ allocator: CFAllocator!, _ callout: CFMachPortCallBack!, _ context: UnsafeMutablePointer<CFMachPortContext>, _ shouldFreeInfo: UnsafeMutablePointer<DarwinBoolean>) -> CFMachPort! ``` |

Modified [CFMachPortCreateWithPort(_: CFAllocator!, _: mach_port_t, _: CFMachPortCallBack!, _: UnsafeMutablePointer<CFMachPortContext>, _: UnsafeMutablePointer<DarwinBoolean>) -> CFMachPort!](https://developer.apple.com/documentation/corefoundation/1400924-cfmachportcreatewithport)

|  | Declaration |
| --- | --- |
| From | ``` func CFMachPortCreateWithPort(_ allocator: CFAllocator!, _ portNum: mach_port_t, _ callout: CFMachPortCallBack, _ context: UnsafeMutablePointer<CFMachPortContext>, _ shouldFreeInfo: UnsafeMutablePointer<Boolean>) -> CFMachPort! ``` |
| To | ``` func CFMachPortCreateWithPort(_ allocator: CFAllocator!, _ portNum: mach_port_t, _ callout: CFMachPortCallBack!, _ context: UnsafeMutablePointer<CFMachPortContext>, _ shouldFreeInfo: UnsafeMutablePointer<DarwinBoolean>) -> CFMachPort! ``` |

Modified [CFMachPortGetInvalidationCallBack(_: CFMachPort!) -> CFMachPortInvalidationCallBack!](https://developer.apple.com/documentation/corefoundation/1400946-cfmachportgetinvalidationcallbac)

|  | Declaration |
| --- | --- |
| From | ``` func CFMachPortGetInvalidationCallBack(_ port: CFMachPort!) -> CFMachPortInvalidationCallBack ``` |
| To | ``` func CFMachPortGetInvalidationCallBack(_ port: CFMachPort!) -> CFMachPortInvalidationCallBack! ``` |

Modified [CFMachPortInvalidationCallBack](https://developer.apple.com/documentation/corefoundation/cfmachportinvalidationcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFMachPortInvalidationCallBack = CFunctionPointer<((CFMachPort!, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFMachPortInvalidationCallBack = (CFMachPort!, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CFMachPortIsValid(_: CFMachPort!) -> Bool](https://developer.apple.com/documentation/corefoundation/1400936-cfmachportisvalid)

|  | Declaration |
| --- | --- |
| From | ``` func CFMachPortIsValid(_ port: CFMachPort!) -> Boolean ``` |
| To | ``` func CFMachPortIsValid(_ port: CFMachPort!) -> Bool ``` |

Modified [CFMachPortSetInvalidationCallBack(_: CFMachPort!, _: CFMachPortInvalidationCallBack!)](https://developer.apple.com/documentation/corefoundation/1400942-cfmachportsetinvalidationcallbac)

|  | Declaration |
| --- | --- |
| From | ``` func CFMachPortSetInvalidationCallBack(_ port: CFMachPort!, _ callout: CFMachPortInvalidationCallBack) ``` |
| To | ``` func CFMachPortSetInvalidationCallBack(_ port: CFMachPort!, _ callout: CFMachPortInvalidationCallBack!) ``` |

Modified [CFMessagePortCallBack](https://developer.apple.com/documentation/corefoundation/cfmessageportcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFMessagePortCallBack = CFunctionPointer<((CFMessagePort!, Int32, CFData!, UnsafeMutablePointer<Void>) -> Unmanaged<CFData>!)> ``` |
| To | ``` typealias CFMessagePortCallBack = (CFMessagePort!, Int32, CFData!, UnsafeMutablePointer<Void>) -> Unmanaged<CFData>! ``` |

Modified [CFMessagePortCreateLocal(_: CFAllocator!, _: CFString!, _: CFMessagePortCallBack!, _: UnsafeMutablePointer<CFMessagePortContext>, _: UnsafeMutablePointer<DarwinBoolean>) -> CFMessagePort!](https://developer.apple.com/documentation/corefoundation/1543289-cfmessageportcreatelocal)

|  | Declaration |
| --- | --- |
| From | ``` func CFMessagePortCreateLocal(_ allocator: CFAllocator!, _ name: CFString!, _ callout: CFMessagePortCallBack, _ context: UnsafeMutablePointer<CFMessagePortContext>, _ shouldFreeInfo: UnsafeMutablePointer<Boolean>) -> CFMessagePort! ``` |
| To | ``` func CFMessagePortCreateLocal(_ allocator: CFAllocator!, _ name: CFString!, _ callout: CFMessagePortCallBack!, _ context: UnsafeMutablePointer<CFMessagePortContext>, _ shouldFreeInfo: UnsafeMutablePointer<DarwinBoolean>) -> CFMessagePort! ``` |

Modified [CFMessagePortGetInvalidationCallBack(_: CFMessagePort!) -> CFMessagePortInvalidationCallBack!](https://developer.apple.com/documentation/corefoundation/1542568-cfmessageportgetinvalidationcall)

|  | Declaration |
| --- | --- |
| From | ``` func CFMessagePortGetInvalidationCallBack(_ ms: CFMessagePort!) -> CFMessagePortInvalidationCallBack ``` |
| To | ``` func CFMessagePortGetInvalidationCallBack(_ ms: CFMessagePort!) -> CFMessagePortInvalidationCallBack! ``` |

Modified [CFMessagePortInvalidationCallBack](https://developer.apple.com/documentation/corefoundation/cfmessageportinvalidationcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFMessagePortInvalidationCallBack = CFunctionPointer<((CFMessagePort!, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFMessagePortInvalidationCallBack = (CFMessagePort!, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CFMessagePortIsRemote(_: CFMessagePort!) -> Bool](https://developer.apple.com/documentation/corefoundation/1543277-cfmessageportisremote)

|  | Declaration |
| --- | --- |
| From | ``` func CFMessagePortIsRemote(_ ms: CFMessagePort!) -> Boolean ``` |
| To | ``` func CFMessagePortIsRemote(_ ms: CFMessagePort!) -> Bool ``` |

Modified [CFMessagePortIsValid(_: CFMessagePort!) -> Bool](https://developer.apple.com/documentation/corefoundation/1541942-cfmessageportisvalid)

|  | Declaration |
| --- | --- |
| From | ``` func CFMessagePortIsValid(_ ms: CFMessagePort!) -> Boolean ``` |
| To | ``` func CFMessagePortIsValid(_ ms: CFMessagePort!) -> Bool ``` |

Modified [CFMessagePortSetInvalidationCallBack(_: CFMessagePort!, _: CFMessagePortInvalidationCallBack!)](https://developer.apple.com/documentation/corefoundation/1541999-cfmessageportsetinvalidationcall)

|  | Declaration |
| --- | --- |
| From | ``` func CFMessagePortSetInvalidationCallBack(_ ms: CFMessagePort!, _ callout: CFMessagePortInvalidationCallBack) ``` |
| To | ``` func CFMessagePortSetInvalidationCallBack(_ ms: CFMessagePort!, _ callout: CFMessagePortInvalidationCallBack!) ``` |

Modified [CFMessagePortSetName(_: CFMessagePort!, _: CFString!) -> Bool](https://developer.apple.com/documentation/corefoundation/1543116-cfmessageportsetname)

|  | Declaration |
| --- | --- |
| From | ``` func CFMessagePortSetName(_ ms: CFMessagePort!, _ newName: CFString!) -> Boolean ``` |
| To | ``` func CFMessagePortSetName(_ ms: CFMessagePort!, _ newName: CFString!) -> Bool ``` |

Modified [CFNotificationCallback](https://developer.apple.com/documentation/corefoundation/cfnotificationcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFNotificationCallback = CFunctionPointer<((CFNotificationCenter!, UnsafeMutablePointer<Void>, CFString!, UnsafePointer<Void>, CFDictionary!) -> Void)> ``` |
| To | ``` typealias CFNotificationCallback = (CFNotificationCenter!, UnsafeMutablePointer<Void>, CFString!, UnsafePointer<Void>, CFDictionary!) -> Void ``` |

Modified [CFNotificationCenterAddObserver(_: CFNotificationCenter!, _: UnsafePointer<Void>, _: CFNotificationCallback!, _: CFString!, _: UnsafePointer<Void>, _: CFNotificationSuspensionBehavior)](https://developer.apple.com/documentation/corefoundation/1543316-cfnotificationcenteraddobserver)

|  | Declaration |
| --- | --- |
| From | ``` func CFNotificationCenterAddObserver(_ center: CFNotificationCenter!, _ observer: UnsafePointer<Void>, _ callBack: CFNotificationCallback, _ name: CFString!, _ object: UnsafePointer<Void>, _ suspensionBehavior: CFNotificationSuspensionBehavior) ``` |
| To | ``` func CFNotificationCenterAddObserver(_ center: CFNotificationCenter!, _ observer: UnsafePointer<Void>, _ callBack: CFNotificationCallback!, _ name: CFString!, _ object: UnsafePointer<Void>, _ suspensionBehavior: CFNotificationSuspensionBehavior) ``` |

Modified [CFNotificationCenterPostNotification(_: CFNotificationCenter!, _: CFString!, _: UnsafePointer<Void>, _: CFDictionary!, _: Bool)](https://developer.apple.com/documentation/corefoundation/1542592-cfnotificationcenterpostnotifica)

|  | Declaration |
| --- | --- |
| From | ``` func CFNotificationCenterPostNotification(_ center: CFNotificationCenter!, _ name: CFString!, _ object: UnsafePointer<Void>, _ userInfo: CFDictionary!, _ deliverImmediately: Boolean) ``` |
| To | ``` func CFNotificationCenterPostNotification(_ center: CFNotificationCenter!, _ name: CFString!, _ object: UnsafePointer<Void>, _ userInfo: CFDictionary!, _ deliverImmediately: Bool) ``` |

Modified [CFNumberFormatterGetDecimalInfoForCurrencyCode(_: CFString!, _: UnsafeMutablePointer<Int32>, _: UnsafeMutablePointer<Double>) -> Bool](https://developer.apple.com/documentation/corefoundation/1390757-cfnumberformattergetdecimalinfof)

|  | Declaration |
| --- | --- |
| From | ``` func CFNumberFormatterGetDecimalInfoForCurrencyCode(_ currencyCode: CFString!, _ defaultFractionDigits: UnsafeMutablePointer<Int32>, _ roundingIncrement: UnsafeMutablePointer<Double>) -> Boolean ``` |
| To | ``` func CFNumberFormatterGetDecimalInfoForCurrencyCode(_ currencyCode: CFString!, _ defaultFractionDigits: UnsafeMutablePointer<Int32>, _ roundingIncrement: UnsafeMutablePointer<Double>) -> Bool ``` |

Modified [CFNumberFormatterGetValueFromString(_: CFNumberFormatter!, _: CFString!, _: UnsafeMutablePointer<CFRange>, _: CFNumberType, _: UnsafeMutablePointer<Void>) -> Bool](https://developer.apple.com/documentation/corefoundation/1390720-cfnumberformattergetvaluefromstr)

|  | Declaration |
| --- | --- |
| From | ``` func CFNumberFormatterGetValueFromString(_ formatter: CFNumberFormatter!, _ string: CFString!, _ rangep: UnsafeMutablePointer<CFRange>, _ numberType: CFNumberType, _ valuePtr: UnsafeMutablePointer<Void>) -> Boolean ``` |
| To | ``` func CFNumberFormatterGetValueFromString(_ formatter: CFNumberFormatter!, _ string: CFString!, _ rangep: UnsafeMutablePointer<CFRange>, _ numberType: CFNumberType, _ valuePtr: UnsafeMutablePointer<Void>) -> Bool ``` |

Modified [CFNumberGetValue(_: CFNumber!, _: CFNumberType, _: UnsafeMutablePointer<Void>) -> Bool](https://developer.apple.com/documentation/corefoundation/1543114-cfnumbergetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFNumberGetValue(_ number: CFNumber!, _ theType: CFNumberType, _ valuePtr: UnsafeMutablePointer<Void>) -> Boolean ``` |
| To | ``` func CFNumberGetValue(_ number: CFNumber!, _ theType: CFNumberType, _ valuePtr: UnsafeMutablePointer<Void>) -> Bool ``` |

Modified [CFNumberIsFloatType(_: CFNumber!) -> Bool](https://developer.apple.com/documentation/corefoundation/1543131-cfnumberisfloattype)

|  | Declaration |
| --- | --- |
| From | ``` func CFNumberIsFloatType(_ number: CFNumber!) -> Boolean ``` |
| To | ``` func CFNumberIsFloatType(_ number: CFNumber!) -> Bool ``` |

Modified [CFPlugInDynamicRegisterFunction](https://developer.apple.com/documentation/corefoundation/cfplugindynamicregisterfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFPlugInDynamicRegisterFunction = CFunctionPointer<((CFPlugIn!) -> Void)> ``` |
| To | ``` typealias CFPlugInDynamicRegisterFunction = (CFPlugIn!) -> Void ``` |

Modified [CFPlugInFactoryFunction](https://developer.apple.com/documentation/corefoundation/cfpluginfactoryfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFPlugInFactoryFunction = CFunctionPointer<((CFAllocator!, CFUUID!) -> UnsafeMutablePointer<Void>)> ``` |
| To | ``` typealias CFPlugInFactoryFunction = (CFAllocator!, CFUUID!) -> UnsafeMutablePointer<Void> ``` |

Modified [CFPlugInInstanceCreateWithInstanceDataSize(_: CFAllocator!, _: CFIndex, _: CFPlugInInstanceDeallocateInstanceDataFunction!, _: CFString!, _: CFPlugInInstanceGetInterfaceFunction!) -> CFPlugInInstance!](https://developer.apple.com/documentation/corefoundation/1493882-cfplugininstancecreatewithinstan)

|  | Declaration |
| --- | --- |
| From | ``` func CFPlugInInstanceCreateWithInstanceDataSize(_ allocator: CFAllocator!, _ instanceDataSize: CFIndex, _ deallocateInstanceFunction: CFPlugInInstanceDeallocateInstanceDataFunction, _ factoryName: CFString!, _ getInterfaceFunction: CFPlugInInstanceGetInterfaceFunction) -> CFPlugInInstance! ``` |
| To | ``` func CFPlugInInstanceCreateWithInstanceDataSize(_ allocator: CFAllocator!, _ instanceDataSize: CFIndex, _ deallocateInstanceFunction: CFPlugInInstanceDeallocateInstanceDataFunction!, _ factoryName: CFString!, _ getInterfaceFunction: CFPlugInInstanceGetInterfaceFunction!) -> CFPlugInInstance! ``` |

Modified [CFPlugInInstanceDeallocateInstanceDataFunction](https://developer.apple.com/documentation/corefoundation/cfplugininstancedeallocateinstancedatafunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFPlugInInstanceDeallocateInstanceDataFunction = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFPlugInInstanceDeallocateInstanceDataFunction = (UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CFPlugInInstanceGetInterfaceFunction](https://developer.apple.com/documentation/corefoundation/cfplugininstancegetinterfacefunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFPlugInInstanceGetInterfaceFunction = CFunctionPointer<((CFPlugInInstance!, CFString!, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Boolean)> ``` |
| To | ``` typealias CFPlugInInstanceGetInterfaceFunction = (CFPlugInInstance!, CFString!, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> DarwinBoolean ``` |

Modified [CFPlugInInstanceGetInterfaceFunctionTable(_: CFPlugInInstance!, _: CFString!, _: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Bool](https://developer.apple.com/documentation/corefoundation/1493862-cfplugininstancegetinterfacefunc)

|  | Declaration |
| --- | --- |
| From | ``` func CFPlugInInstanceGetInterfaceFunctionTable(_ instance: CFPlugInInstance!, _ interfaceName: CFString!, _ ftbl: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Boolean ``` |
| To | ``` func CFPlugInInstanceGetInterfaceFunctionTable(_ instance: CFPlugInInstance!, _ interfaceName: CFString!, _ ftbl: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Bool ``` |

Modified [CFPlugInIsLoadOnDemand(_: CFPlugIn!) -> Bool](https://developer.apple.com/documentation/corefoundation/1493872-cfpluginisloadondemand)

|  | Declaration |
| --- | --- |
| From | ``` func CFPlugInIsLoadOnDemand(_ plugIn: CFPlugIn!) -> Boolean ``` |
| To | ``` func CFPlugInIsLoadOnDemand(_ plugIn: CFPlugIn!) -> Bool ``` |

Modified [CFPlugInRegisterFactoryFunction(_: CFUUID!, _: CFPlugInFactoryFunction!) -> Bool](https://developer.apple.com/documentation/corefoundation/1493868-cfpluginregisterfactoryfunction)

|  | Declaration |
| --- | --- |
| From | ``` func CFPlugInRegisterFactoryFunction(_ factoryUUID: CFUUID!, _ `func`: CFPlugInFactoryFunction) -> Boolean ``` |
| To | ``` func CFPlugInRegisterFactoryFunction(_ factoryUUID: CFUUID!, _ `func`: CFPlugInFactoryFunction!) -> Bool ``` |

Modified [CFPlugInRegisterFactoryFunctionByName(_: CFUUID!, _: CFPlugIn!, _: CFString!) -> Bool](https://developer.apple.com/documentation/corefoundation/1493893-cfpluginregisterfactoryfunctionb)

|  | Declaration |
| --- | --- |
| From | ``` func CFPlugInRegisterFactoryFunctionByName(_ factoryUUID: CFUUID!, _ plugIn: CFPlugIn!, _ functionName: CFString!) -> Boolean ``` |
| To | ``` func CFPlugInRegisterFactoryFunctionByName(_ factoryUUID: CFUUID!, _ plugIn: CFPlugIn!, _ functionName: CFString!) -> Bool ``` |

Modified [CFPlugInRegisterPlugInType(_: CFUUID!, _: CFUUID!) -> Bool](https://developer.apple.com/documentation/corefoundation/1493853-cfpluginregisterplugintype)

|  | Declaration |
| --- | --- |
| From | ``` func CFPlugInRegisterPlugInType(_ factoryUUID: CFUUID!, _ typeUUID: CFUUID!) -> Boolean ``` |
| To | ``` func CFPlugInRegisterPlugInType(_ factoryUUID: CFUUID!, _ typeUUID: CFUUID!) -> Bool ``` |

Modified [CFPlugInSetLoadOnDemand(_: CFPlugIn!, _: Bool)](https://developer.apple.com/documentation/corefoundation/1493898-cfpluginsetloadondemand)

|  | Declaration |
| --- | --- |
| From | ``` func CFPlugInSetLoadOnDemand(_ plugIn: CFPlugIn!, _ flag: Boolean) ``` |
| To | ``` func CFPlugInSetLoadOnDemand(_ plugIn: CFPlugIn!, _ flag: Bool) ``` |

Modified [CFPlugInUnloadFunction](https://developer.apple.com/documentation/corefoundation/cfpluginunloadfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFPlugInUnloadFunction = CFunctionPointer<((CFPlugIn!) -> Void)> ``` |
| To | ``` typealias CFPlugInUnloadFunction = (CFPlugIn!) -> Void ``` |

Modified [CFPlugInUnregisterFactory(_: CFUUID!) -> Bool](https://developer.apple.com/documentation/corefoundation/1493856-cfpluginunregisterfactory)

|  | Declaration |
| --- | --- |
| From | ``` func CFPlugInUnregisterFactory(_ factoryUUID: CFUUID!) -> Boolean ``` |
| To | ``` func CFPlugInUnregisterFactory(_ factoryUUID: CFUUID!) -> Bool ``` |

Modified [CFPlugInUnregisterPlugInType(_: CFUUID!, _: CFUUID!) -> Bool](https://developer.apple.com/documentation/corefoundation/1493874-cfpluginunregisterplugintype)

|  | Declaration |
| --- | --- |
| From | ``` func CFPlugInUnregisterPlugInType(_ factoryUUID: CFUUID!, _ typeUUID: CFUUID!) -> Boolean ``` |
| To | ``` func CFPlugInUnregisterPlugInType(_ factoryUUID: CFUUID!, _ typeUUID: CFUUID!) -> Bool ``` |

Modified [CFPreferencesAppSynchronize(_: CFString!) -> Bool](https://developer.apple.com/documentation/corefoundation/1515510-cfpreferencesappsynchronize)

|  | Declaration |
| --- | --- |
| From | ``` func CFPreferencesAppSynchronize(_ applicationID: CFString!) -> Boolean ``` |
| To | ``` func CFPreferencesAppSynchronize(_ applicationID: CFString!) -> Bool ``` |

Modified [CFPreferencesAppValueIsForced(_: CFString!, _: CFString!) -> Bool](https://developer.apple.com/documentation/corefoundation/1515521-cfpreferencesappvalueisforced)

|  | Declaration |
| --- | --- |
| From | ``` func CFPreferencesAppValueIsForced(_ key: CFString!, _ applicationID: CFString!) -> Boolean ``` |
| To | ``` func CFPreferencesAppValueIsForced(_ key: CFString!, _ applicationID: CFString!) -> Bool ``` |

Modified [CFPreferencesGetAppBooleanValue(_: CFString!, _: CFString!, _: UnsafeMutablePointer<DarwinBoolean>) -> Bool](https://developer.apple.com/documentation/corefoundation/1515514-cfpreferencesgetappbooleanvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFPreferencesGetAppBooleanValue(_ key: CFString!, _ applicationID: CFString!, _ keyExistsAndHasValidFormat: UnsafeMutablePointer<Boolean>) -> Boolean ``` |
| To | ``` func CFPreferencesGetAppBooleanValue(_ key: CFString!, _ applicationID: CFString!, _ keyExistsAndHasValidFormat: UnsafeMutablePointer<DarwinBoolean>) -> Bool ``` |

Modified [CFPreferencesGetAppIntegerValue(_: CFString!, _: CFString!, _: UnsafeMutablePointer<DarwinBoolean>) -> CFIndex](https://developer.apple.com/documentation/corefoundation/1515526-cfpreferencesgetappintegervalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFPreferencesGetAppIntegerValue(_ key: CFString!, _ applicationID: CFString!, _ keyExistsAndHasValidFormat: UnsafeMutablePointer<Boolean>) -> CFIndex ``` |
| To | ``` func CFPreferencesGetAppIntegerValue(_ key: CFString!, _ applicationID: CFString!, _ keyExistsAndHasValidFormat: UnsafeMutablePointer<DarwinBoolean>) -> CFIndex ``` |

Modified [CFPreferencesSynchronize(_: CFString!, _: CFString!, _: CFString!) -> Bool](https://developer.apple.com/documentation/corefoundation/1515504-cfpreferencessynchronize)

|  | Declaration |
| --- | --- |
| From | ``` func CFPreferencesSynchronize(_ applicationID: CFString!, _ userName: CFString!, _ hostName: CFString!) -> Boolean ``` |
| To | ``` func CFPreferencesSynchronize(_ applicationID: CFString!, _ userName: CFString!, _ hostName: CFString!) -> Bool ``` |

Modified [CFPropertyListIsValid(_: CFPropertyList!, _: CFPropertyListFormat) -> Bool](https://developer.apple.com/documentation/corefoundation/1430019-cfpropertylistisvalid)

|  | Declaration |
| --- | --- |
| From | ``` func CFPropertyListIsValid(_ plist: CFPropertyList!, _ format: CFPropertyListFormat) -> Boolean ``` |
| To | ``` func CFPropertyListIsValid(_ plist: CFPropertyList!, _ format: CFPropertyListFormat) -> Bool ``` |

Modified [CFReadStreamClientCallBack](https://developer.apple.com/documentation/corefoundation/cfreadstreamclientcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFReadStreamClientCallBack = CFunctionPointer<((CFReadStream!, CFStreamEventType, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFReadStreamClientCallBack = (CFReadStream!, CFStreamEventType, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CFReadStreamHasBytesAvailable(_: CFReadStream!) -> Bool](https://developer.apple.com/documentation/corefoundation/1539638-cfreadstreamhasbytesavailable)

|  | Declaration |
| --- | --- |
| From | ``` func CFReadStreamHasBytesAvailable(_ stream: CFReadStream!) -> Boolean ``` |
| To | ``` func CFReadStreamHasBytesAvailable(_ stream: CFReadStream!) -> Bool ``` |

Modified [CFReadStreamOpen(_: CFReadStream!) -> Bool](https://developer.apple.com/documentation/corefoundation/1539743-cfreadstreamopen)

|  | Declaration |
| --- | --- |
| From | ``` func CFReadStreamOpen(_ stream: CFReadStream!) -> Boolean ``` |
| To | ``` func CFReadStreamOpen(_ stream: CFReadStream!) -> Bool ``` |

Modified [CFReadStreamSetClient(_: CFReadStream!, _: CFOptionFlags, _: CFReadStreamClientCallBack!, _: UnsafeMutablePointer<CFStreamClientContext>) -> Bool](https://developer.apple.com/documentation/corefoundation/1539670-cfreadstreamsetclient)

|  | Declaration |
| --- | --- |
| From | ``` func CFReadStreamSetClient(_ stream: CFReadStream!, _ streamEvents: CFOptionFlags, _ clientCB: CFReadStreamClientCallBack, _ clientContext: UnsafeMutablePointer<CFStreamClientContext>) -> Boolean ``` |
| To | ``` func CFReadStreamSetClient(_ stream: CFReadStream!, _ streamEvents: CFOptionFlags, _ clientCB: CFReadStreamClientCallBack!, _ clientContext: UnsafeMutablePointer<CFStreamClientContext>) -> Bool ``` |

Modified [CFReadStreamSetProperty(_: CFReadStream!, _: CFString!, _: AnyObject!) -> Bool](https://developer.apple.com/documentation/corefoundation/1539615-cfreadstreamsetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func CFReadStreamSetProperty(_ stream: CFReadStream!, _ propertyName: CFString!, _ propertyValue: AnyObject!) -> Boolean ``` |
| To | ``` func CFReadStreamSetProperty(_ stream: CFReadStream!, _ propertyName: CFString!, _ propertyValue: AnyObject!) -> Bool ``` |

Modified [CFRunLoopContainsObserver(_: CFRunLoop!, _: CFRunLoopObserver!, _: CFString!) -> Bool](https://developer.apple.com/documentation/corefoundation/1542815-cfrunloopcontainsobserver)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopContainsObserver(_ rl: CFRunLoop!, _ observer: CFRunLoopObserver!, _ mode: CFString!) -> Boolean ``` |
| To | ``` func CFRunLoopContainsObserver(_ rl: CFRunLoop!, _ observer: CFRunLoopObserver!, _ mode: CFString!) -> Bool ``` |

Modified [CFRunLoopContainsSource(_: CFRunLoop!, _: CFRunLoopSource!, _: CFString!) -> Bool](https://developer.apple.com/documentation/corefoundation/1542250-cfrunloopcontainssource)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopContainsSource(_ rl: CFRunLoop!, _ source: CFRunLoopSource!, _ mode: CFString!) -> Boolean ``` |
| To | ``` func CFRunLoopContainsSource(_ rl: CFRunLoop!, _ source: CFRunLoopSource!, _ mode: CFString!) -> Bool ``` |

Modified [CFRunLoopContainsTimer(_: CFRunLoop!, _: CFRunLoopTimer!, _: CFString!) -> Bool](https://developer.apple.com/documentation/corefoundation/1543011-cfrunloopcontainstimer)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopContainsTimer(_ rl: CFRunLoop!, _ timer: CFRunLoopTimer!, _ mode: CFString!) -> Boolean ``` |
| To | ``` func CFRunLoopContainsTimer(_ rl: CFRunLoop!, _ timer: CFRunLoopTimer!, _ mode: CFString!) -> Bool ``` |

Modified [CFRunLoopIsWaiting(_: CFRunLoop!) -> Bool](https://developer.apple.com/documentation/corefoundation/1542956-cfrunloopiswaiting)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopIsWaiting(_ rl: CFRunLoop!) -> Boolean ``` |
| To | ``` func CFRunLoopIsWaiting(_ rl: CFRunLoop!) -> Bool ``` |

Modified [CFRunLoopObserverCallBack](https://developer.apple.com/documentation/corefoundation/cfrunloopobservercallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFRunLoopObserverCallBack = CFunctionPointer<((CFRunLoopObserver!, CFRunLoopActivity, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFRunLoopObserverCallBack = (CFRunLoopObserver!, CFRunLoopActivity, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CFRunLoopObserverCreate(_: CFAllocator!, _: CFOptionFlags, _: Bool, _: CFIndex, _: CFRunLoopObserverCallBack!, _: UnsafeMutablePointer<CFRunLoopObserverContext>) -> CFRunLoopObserver!](https://developer.apple.com/documentation/corefoundation/1541546-cfrunloopobservercreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopObserverCreate(_ allocator: CFAllocator!, _ activities: CFOptionFlags, _ repeats: Boolean, _ order: CFIndex, _ callout: CFRunLoopObserverCallBack, _ context: UnsafeMutablePointer<CFRunLoopObserverContext>) -> CFRunLoopObserver! ``` |
| To | ``` func CFRunLoopObserverCreate(_ allocator: CFAllocator!, _ activities: CFOptionFlags, _ repeats: Bool, _ order: CFIndex, _ callout: CFRunLoopObserverCallBack!, _ context: UnsafeMutablePointer<CFRunLoopObserverContext>) -> CFRunLoopObserver! ``` |

Modified [CFRunLoopObserverCreateWithHandler(_: CFAllocator!, _: CFOptionFlags, _: Bool, _: CFIndex, _: ((CFRunLoopObserver!, CFRunLoopActivity) -> Void)!) -> CFRunLoopObserver!](https://developer.apple.com/documentation/corefoundation/1542816-cfrunloopobservercreatewithhandl)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopObserverCreateWithHandler(_ allocator: CFAllocator!, _ activities: CFOptionFlags, _ repeats: Boolean, _ order: CFIndex, _ block: ((CFRunLoopObserver!, CFRunLoopActivity) -> Void)!) -> CFRunLoopObserver! ``` |
| To | ``` func CFRunLoopObserverCreateWithHandler(_ allocator: CFAllocator!, _ activities: CFOptionFlags, _ repeats: Bool, _ order: CFIndex, _ block: ((CFRunLoopObserver!, CFRunLoopActivity) -> Void)!) -> CFRunLoopObserver! ``` |

Modified [CFRunLoopObserverDoesRepeat(_: CFRunLoopObserver!) -> Bool](https://developer.apple.com/documentation/corefoundation/1542616-cfrunloopobserverdoesrepeat)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopObserverDoesRepeat(_ observer: CFRunLoopObserver!) -> Boolean ``` |
| To | ``` func CFRunLoopObserverDoesRepeat(_ observer: CFRunLoopObserver!) -> Bool ``` |

Modified [CFRunLoopObserverIsValid(_: CFRunLoopObserver!) -> Bool](https://developer.apple.com/documentation/corefoundation/1543205-cfrunloopobserverisvalid)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopObserverIsValid(_ observer: CFRunLoopObserver!) -> Boolean ``` |
| To | ``` func CFRunLoopObserverIsValid(_ observer: CFRunLoopObserver!) -> Bool ``` |

Modified [CFRunLoopRunInMode(_: CFString!, _: CFTimeInterval, _: Bool) -> CFRunLoopRunResult](https://developer.apple.com/documentation/corefoundation/1541988-cfrunloopruninmode)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopRunInMode(_ mode: CFString!, _ seconds: CFTimeInterval, _ returnAfterSourceHandled: Boolean) -> Int32 ``` |
| To | ``` func CFRunLoopRunInMode(_ mode: CFString!, _ seconds: CFTimeInterval, _ returnAfterSourceHandled: Bool) -> CFRunLoopRunResult ``` |

Modified [CFRunLoopSourceIsValid(_: CFRunLoopSource!) -> Bool](https://developer.apple.com/documentation/corefoundation/1541509-cfrunloopsourceisvalid)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopSourceIsValid(_ source: CFRunLoopSource!) -> Boolean ``` |
| To | ``` func CFRunLoopSourceIsValid(_ source: CFRunLoopSource!) -> Bool ``` |

Modified [CFRunLoopTimerCallBack](https://developer.apple.com/documentation/corefoundation/cfrunlooptimercallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFRunLoopTimerCallBack = CFunctionPointer<((CFRunLoopTimer!, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFRunLoopTimerCallBack = (CFRunLoopTimer!, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CFRunLoopTimerCreate(_: CFAllocator!, _: CFAbsoluteTime, _: CFTimeInterval, _: CFOptionFlags, _: CFIndex, _: CFRunLoopTimerCallBack!, _: UnsafeMutablePointer<CFRunLoopTimerContext>) -> CFRunLoopTimer!](https://developer.apple.com/documentation/corefoundation/1543570-cfrunlooptimercreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopTimerCreate(_ allocator: CFAllocator!, _ fireDate: CFAbsoluteTime, _ interval: CFTimeInterval, _ flags: CFOptionFlags, _ order: CFIndex, _ callout: CFRunLoopTimerCallBack, _ context: UnsafeMutablePointer<CFRunLoopTimerContext>) -> CFRunLoopTimer! ``` |
| To | ``` func CFRunLoopTimerCreate(_ allocator: CFAllocator!, _ fireDate: CFAbsoluteTime, _ interval: CFTimeInterval, _ flags: CFOptionFlags, _ order: CFIndex, _ callout: CFRunLoopTimerCallBack!, _ context: UnsafeMutablePointer<CFRunLoopTimerContext>) -> CFRunLoopTimer! ``` |

Modified [CFRunLoopTimerDoesRepeat(_: CFRunLoopTimer!) -> Bool](https://developer.apple.com/documentation/corefoundation/1543545-cfrunlooptimerdoesrepeat)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopTimerDoesRepeat(_ timer: CFRunLoopTimer!) -> Boolean ``` |
| To | ``` func CFRunLoopTimerDoesRepeat(_ timer: CFRunLoopTimer!) -> Bool ``` |

Modified [CFRunLoopTimerIsValid(_: CFRunLoopTimer!) -> Bool](https://developer.apple.com/documentation/corefoundation/1543110-cfrunlooptimerisvalid)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopTimerIsValid(_ timer: CFRunLoopTimer!) -> Boolean ``` |
| To | ``` func CFRunLoopTimerIsValid(_ timer: CFRunLoopTimer!) -> Bool ``` |

Modified [CFSetApplierFunction](https://developer.apple.com/documentation/corefoundation/cfsetapplierfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFSetApplierFunction = CFunctionPointer<((UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFSetApplierFunction = (UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CFSetApplyFunction(_: CFSet!, _: CFSetApplierFunction!, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/corefoundation/1520450-cfsetapplyfunction)

|  | Declaration |
| --- | --- |
| From | ``` func CFSetApplyFunction(_ theSet: CFSet!, _ applier: CFSetApplierFunction, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func CFSetApplyFunction(_ theSet: CFSet!, _ applier: CFSetApplierFunction!, _ context: UnsafeMutablePointer<Void>) ``` |

Modified [CFSetContainsValue(_: CFSet!, _: UnsafePointer<Void>) -> Bool](https://developer.apple.com/documentation/corefoundation/1520436-cfsetcontainsvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFSetContainsValue(_ theSet: CFSet!, _ value: UnsafePointer<Void>) -> Boolean ``` |
| To | ``` func CFSetContainsValue(_ theSet: CFSet!, _ value: UnsafePointer<Void>) -> Bool ``` |

Modified [CFSetCopyDescriptionCallBack](https://developer.apple.com/documentation/corefoundation/cfsetcopydescriptioncallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFSetCopyDescriptionCallBack = CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |
| To | ``` typealias CFSetCopyDescriptionCallBack = (UnsafePointer<Void>) -> Unmanaged<CFString>! ``` |

Modified [CFSetEqualCallBack](https://developer.apple.com/documentation/corefoundation/cfsetequalcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFSetEqualCallBack = CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Boolean)> ``` |
| To | ``` typealias CFSetEqualCallBack = (UnsafePointer<Void>, UnsafePointer<Void>) -> DarwinBoolean ``` |

Modified [CFSetGetValueIfPresent(_: CFSet!, _: UnsafePointer<Void>, _: UnsafeMutablePointer<UnsafePointer<Void>>) -> Bool](https://developer.apple.com/documentation/corefoundation/1520409-cfsetgetvalueifpresent)

|  | Declaration |
| --- | --- |
| From | ``` func CFSetGetValueIfPresent(_ theSet: CFSet!, _ candidate: UnsafePointer<Void>, _ value: UnsafeMutablePointer<UnsafePointer<Void>>) -> Boolean ``` |
| To | ``` func CFSetGetValueIfPresent(_ theSet: CFSet!, _ candidate: UnsafePointer<Void>, _ value: UnsafeMutablePointer<UnsafePointer<Void>>) -> Bool ``` |

Modified [CFSetHashCallBack](https://developer.apple.com/documentation/corefoundation/cfsethashcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFSetHashCallBack = CFunctionPointer<((UnsafePointer<Void>) -> CFHashCode)> ``` |
| To | ``` typealias CFSetHashCallBack = (UnsafePointer<Void>) -> CFHashCode ``` |

Modified [CFSetReleaseCallBack](https://developer.apple.com/documentation/corefoundation/cfsetreleasecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFSetReleaseCallBack = CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFSetReleaseCallBack = (CFAllocator!, UnsafePointer<Void>) -> Void ``` |

Modified [CFSetRetainCallBack](https://developer.apple.com/documentation/corefoundation/cfsetretaincallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFSetRetainCallBack = CFunctionPointer<((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |
| To | ``` typealias CFSetRetainCallBack = (CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void> ``` |

Modified [CFSocketCallBack](https://developer.apple.com/documentation/corefoundation/cfsocketcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFSocketCallBack = CFunctionPointer<((CFSocket!, CFSocketCallBackType, CFData!, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFSocketCallBack = (CFSocket!, CFSocketCallBackType, CFData!, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CFSocketCreate(_: CFAllocator!, _: Int32, _: Int32, _: Int32, _: CFOptionFlags, _: CFSocketCallBack!, _: UnsafePointer<CFSocketContext>) -> CFSocket!](https://developer.apple.com/documentation/corefoundation/1543527-cfsocketcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketCreate(_ allocator: CFAllocator!, _ protocolFamily: Int32, _ socketType: Int32, _ `protocol`: Int32, _ callBackTypes: CFOptionFlags, _ callout: CFSocketCallBack, _ context: UnsafePointer<CFSocketContext>) -> CFSocket! ``` |
| To | ``` func CFSocketCreate(_ allocator: CFAllocator!, _ protocolFamily: Int32, _ socketType: Int32, _ `protocol`: Int32, _ callBackTypes: CFOptionFlags, _ callout: CFSocketCallBack!, _ context: UnsafePointer<CFSocketContext>) -> CFSocket! ``` |

Modified [CFSocketCreateConnectedToSocketSignature(_: CFAllocator!, _: UnsafePointer<CFSocketSignature>, _: CFOptionFlags, _: CFSocketCallBack!, _: UnsafePointer<CFSocketContext>, _: CFTimeInterval) -> CFSocket!](https://developer.apple.com/documentation/corefoundation/1542283-cfsocketcreateconnectedtosockets)

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketCreateConnectedToSocketSignature(_ allocator: CFAllocator!, _ signature: UnsafePointer<CFSocketSignature>, _ callBackTypes: CFOptionFlags, _ callout: CFSocketCallBack, _ context: UnsafePointer<CFSocketContext>, _ timeout: CFTimeInterval) -> CFSocket! ``` |
| To | ``` func CFSocketCreateConnectedToSocketSignature(_ allocator: CFAllocator!, _ signature: UnsafePointer<CFSocketSignature>, _ callBackTypes: CFOptionFlags, _ callout: CFSocketCallBack!, _ context: UnsafePointer<CFSocketContext>, _ timeout: CFTimeInterval) -> CFSocket! ``` |

Modified [CFSocketCreateWithNative(_: CFAllocator!, _: CFSocketNativeHandle, _: CFOptionFlags, _: CFSocketCallBack!, _: UnsafePointer<CFSocketContext>) -> CFSocket!](https://developer.apple.com/documentation/corefoundation/1543295-cfsocketcreatewithnative)

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketCreateWithNative(_ allocator: CFAllocator!, _ sock: CFSocketNativeHandle, _ callBackTypes: CFOptionFlags, _ callout: CFSocketCallBack, _ context: UnsafePointer<CFSocketContext>) -> CFSocket! ``` |
| To | ``` func CFSocketCreateWithNative(_ allocator: CFAllocator!, _ sock: CFSocketNativeHandle, _ callBackTypes: CFOptionFlags, _ callout: CFSocketCallBack!, _ context: UnsafePointer<CFSocketContext>) -> CFSocket! ``` |

Modified [CFSocketCreateWithSocketSignature(_: CFAllocator!, _: UnsafePointer<CFSocketSignature>, _: CFOptionFlags, _: CFSocketCallBack!, _: UnsafePointer<CFSocketContext>) -> CFSocket!](https://developer.apple.com/documentation/corefoundation/1542862-cfsocketcreatewithsocketsignatur)

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketCreateWithSocketSignature(_ allocator: CFAllocator!, _ signature: UnsafePointer<CFSocketSignature>, _ callBackTypes: CFOptionFlags, _ callout: CFSocketCallBack, _ context: UnsafePointer<CFSocketContext>) -> CFSocket! ``` |
| To | ``` func CFSocketCreateWithSocketSignature(_ allocator: CFAllocator!, _ signature: UnsafePointer<CFSocketSignature>, _ callBackTypes: CFOptionFlags, _ callout: CFSocketCallBack!, _ context: UnsafePointer<CFSocketContext>) -> CFSocket! ``` |

Modified [CFSocketIsValid(_: CFSocket!) -> Bool](https://developer.apple.com/documentation/corefoundation/1543588-cfsocketisvalid)

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketIsValid(_ s: CFSocket!) -> Boolean ``` |
| To | ``` func CFSocketIsValid(_ s: CFSocket!) -> Bool ``` |

Modified [CFStringCreateWithBytes(_: CFAllocator!, _: UnsafePointer<UInt8>, _: CFIndex, _: CFStringEncoding, _: Bool) -> CFString!](https://developer.apple.com/documentation/corefoundation/1543419-cfstringcreatewithbytes)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringCreateWithBytes(_ alloc: CFAllocator!, _ bytes: UnsafePointer<UInt8>, _ numBytes: CFIndex, _ encoding: CFStringEncoding, _ isExternalRepresentation: Boolean) -> CFString! ``` |
| To | ``` func CFStringCreateWithBytes(_ alloc: CFAllocator!, _ bytes: UnsafePointer<UInt8>, _ numBytes: CFIndex, _ encoding: CFStringEncoding, _ isExternalRepresentation: Bool) -> CFString! ``` |

Modified [CFStringCreateWithBytesNoCopy(_: CFAllocator!, _: UnsafePointer<UInt8>, _: CFIndex, _: CFStringEncoding, _: Bool, _: CFAllocator!) -> CFString!](https://developer.apple.com/documentation/corefoundation/1543597-cfstringcreatewithbytesnocopy)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringCreateWithBytesNoCopy(_ alloc: CFAllocator!, _ bytes: UnsafePointer<UInt8>, _ numBytes: CFIndex, _ encoding: CFStringEncoding, _ isExternalRepresentation: Boolean, _ contentsDeallocator: CFAllocator!) -> CFString! ``` |
| To | ``` func CFStringCreateWithBytesNoCopy(_ alloc: CFAllocator!, _ bytes: UnsafePointer<UInt8>, _ numBytes: CFIndex, _ encoding: CFStringEncoding, _ isExternalRepresentation: Bool, _ contentsDeallocator: CFAllocator!) -> CFString! ``` |

Modified [CFStringFindCharacterFromSet(_: CFString!, _: CFCharacterSet!, _: CFRange, _: CFStringCompareFlags, _: UnsafeMutablePointer<CFRange>) -> Bool](https://developer.apple.com/documentation/corefoundation/1542060-cfstringfindcharacterfromset)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringFindCharacterFromSet(_ theString: CFString!, _ theSet: CFCharacterSet!, _ rangeToSearch: CFRange, _ searchOptions: CFStringCompareFlags, _ result: UnsafeMutablePointer<CFRange>) -> Boolean ``` |
| To | ``` func CFStringFindCharacterFromSet(_ theString: CFString!, _ theSet: CFCharacterSet!, _ rangeToSearch: CFRange, _ searchOptions: CFStringCompareFlags, _ result: UnsafeMutablePointer<CFRange>) -> Bool ``` |

Modified [CFStringFindWithOptions(_: CFString!, _: CFString!, _: CFRange, _: CFStringCompareFlags, _: UnsafeMutablePointer<CFRange>) -> Bool](https://developer.apple.com/documentation/corefoundation/1543522-cfstringfindwithoptions)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringFindWithOptions(_ theString: CFString!, _ stringToFind: CFString!, _ rangeToSearch: CFRange, _ searchOptions: CFStringCompareFlags, _ result: UnsafeMutablePointer<CFRange>) -> Boolean ``` |
| To | ``` func CFStringFindWithOptions(_ theString: CFString!, _ stringToFind: CFString!, _ rangeToSearch: CFRange, _ searchOptions: CFStringCompareFlags, _ result: UnsafeMutablePointer<CFRange>) -> Bool ``` |

Modified [CFStringFindWithOptionsAndLocale(_: CFString!, _: CFString!, _: CFRange, _: CFStringCompareFlags, _: CFLocale!, _: UnsafeMutablePointer<CFRange>) -> Bool](https://developer.apple.com/documentation/corefoundation/1543620-cfstringfindwithoptionsandlocale)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringFindWithOptionsAndLocale(_ theString: CFString!, _ stringToFind: CFString!, _ rangeToSearch: CFRange, _ searchOptions: CFStringCompareFlags, _ locale: CFLocale!, _ result: UnsafeMutablePointer<CFRange>) -> Boolean ``` |
| To | ``` func CFStringFindWithOptionsAndLocale(_ theString: CFString!, _ stringToFind: CFString!, _ rangeToSearch: CFRange, _ searchOptions: CFStringCompareFlags, _ locale: CFLocale!, _ result: UnsafeMutablePointer<CFRange>) -> Bool ``` |

Modified [CFStringGetBytes(_: CFString!, _: CFRange, _: CFStringEncoding, _: UInt8, _: Bool, _: UnsafeMutablePointer<UInt8>, _: CFIndex, _: UnsafeMutablePointer<CFIndex>) -> CFIndex](https://developer.apple.com/documentation/corefoundation/1543006-cfstringgetbytes)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetBytes(_ theString: CFString!, _ range: CFRange, _ encoding: CFStringEncoding, _ lossByte: UInt8, _ isExternalRepresentation: Boolean, _ buffer: UnsafeMutablePointer<UInt8>, _ maxBufLen: CFIndex, _ usedBufLen: UnsafeMutablePointer<CFIndex>) -> CFIndex ``` |
| To | ``` func CFStringGetBytes(_ theString: CFString!, _ range: CFRange, _ encoding: CFStringEncoding, _ lossByte: UInt8, _ isExternalRepresentation: Bool, _ buffer: UnsafeMutablePointer<UInt8>, _ maxBufLen: CFIndex, _ usedBufLen: UnsafeMutablePointer<CFIndex>) -> CFIndex ``` |

Modified [CFStringGetCString(_: CFString!, _: UnsafeMutablePointer<Int8>, _: CFIndex, _: CFStringEncoding) -> Bool](https://developer.apple.com/documentation/corefoundation/1542721-cfstringgetcstring)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetCString(_ theString: CFString!, _ buffer: UnsafeMutablePointer<Int8>, _ bufferSize: CFIndex, _ encoding: CFStringEncoding) -> Boolean ``` |
| To | ``` func CFStringGetCString(_ theString: CFString!, _ buffer: UnsafeMutablePointer<Int8>, _ bufferSize: CFIndex, _ encoding: CFStringEncoding) -> Bool ``` |

Modified [CFStringGetFileSystemRepresentation(_: CFString!, _: UnsafeMutablePointer<Int8>, _: CFIndex) -> Bool](https://developer.apple.com/documentation/corefoundation/1542019-cfstringgetfilesystemrepresentat)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetFileSystemRepresentation(_ string: CFString!, _ buffer: UnsafeMutablePointer<Int8>, _ maxBufLen: CFIndex) -> Boolean ``` |
| To | ``` func CFStringGetFileSystemRepresentation(_ string: CFString!, _ buffer: UnsafeMutablePointer<Int8>, _ maxBufLen: CFIndex) -> Bool ``` |

Modified [CFStringGetPascalString(_: CFString!, _: StringPtr, _: CFIndex, _: CFStringEncoding) -> Bool](https://developer.apple.com/documentation/corefoundation/1543322-cfstringgetpascalstring)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetPascalString(_ theString: CFString!, _ buffer: StringPtr, _ bufferSize: CFIndex, _ encoding: CFStringEncoding) -> Boolean ``` |
| To | ``` func CFStringGetPascalString(_ theString: CFString!, _ buffer: StringPtr, _ bufferSize: CFIndex, _ encoding: CFStringEncoding) -> Bool ``` |

Modified [CFStringGetSurrogatePairForLongCharacter(_: UTF32Char, _: UnsafeMutablePointer<UniChar>) -> Bool](https://developer.apple.com/documentation/corefoundation/1541601-cfstringgetsurrogatepairforlongc)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetSurrogatePairForLongCharacter(_ character: UTF32Char, _ surrogates: UnsafeMutablePointer<UniChar>) -> Boolean ``` |
| To | ``` func CFStringGetSurrogatePairForLongCharacter(_ character: UTF32Char, _ surrogates: UnsafeMutablePointer<UniChar>) -> Bool ``` |

Modified [CFStringHasPrefix(_: CFString!, _: CFString!) -> Bool](https://developer.apple.com/documentation/corefoundation/1542014-cfstringhasprefix)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringHasPrefix(_ theString: CFString!, _ prefix: CFString!) -> Boolean ``` |
| To | ``` func CFStringHasPrefix(_ theString: CFString!, _ prefix: CFString!) -> Bool ``` |

Modified [CFStringHasSuffix(_: CFString!, _: CFString!) -> Bool](https://developer.apple.com/documentation/corefoundation/1542768-cfstringhassuffix)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringHasSuffix(_ theString: CFString!, _ suffix: CFString!) -> Boolean ``` |
| To | ``` func CFStringHasSuffix(_ theString: CFString!, _ suffix: CFString!) -> Bool ``` |

Modified [CFStringIsEncodingAvailable(_: CFStringEncoding) -> Bool](https://developer.apple.com/documentation/corefoundation/1542860-cfstringisencodingavailable)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringIsEncodingAvailable(_ encoding: CFStringEncoding) -> Boolean ``` |
| To | ``` func CFStringIsEncodingAvailable(_ encoding: CFStringEncoding) -> Bool ``` |

Modified [CFStringIsHyphenationAvailableForLocale(_: CFLocale!) -> Bool](https://developer.apple.com/documentation/corefoundation/1543237-cfstringishyphenationavailablefo)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringIsHyphenationAvailableForLocale(_ locale: CFLocale!) -> Boolean ``` |
| To | ``` func CFStringIsHyphenationAvailableForLocale(_ locale: CFLocale!) -> Bool ``` |

Modified [CFStringIsSurrogateHighCharacter(_: UniChar) -> Bool](https://developer.apple.com/documentation/corefoundation/1543284-cfstringissurrogatehighcharacter)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringIsSurrogateHighCharacter(_ character: UniChar) -> Boolean ``` |
| To | ``` func CFStringIsSurrogateHighCharacter(_ character: UniChar) -> Bool ``` |

Modified [CFStringIsSurrogateLowCharacter(_: UniChar) -> Bool](https://developer.apple.com/documentation/corefoundation/1541963-cfstringissurrogatelowcharacter)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringIsSurrogateLowCharacter(_ character: UniChar) -> Boolean ``` |
| To | ``` func CFStringIsSurrogateLowCharacter(_ character: UniChar) -> Bool ``` |

Modified [CFStringTransform(_: CFMutableString!, _: UnsafeMutablePointer<CFRange>, _: CFString!, _: Bool) -> Bool](https://developer.apple.com/documentation/corefoundation/1542411-cfstringtransform)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringTransform(_ string: CFMutableString!, _ range: UnsafeMutablePointer<CFRange>, _ transform: CFString!, _ reverse: Boolean) -> Boolean ``` |
| To | ``` func CFStringTransform(_ string: CFMutableString!, _ range: UnsafeMutablePointer<CFRange>, _ transform: CFString!, _ reverse: Bool) -> Bool ``` |

Modified [CFTimeZoneCreateWithName(_: CFAllocator!, _: CFString!, _: Bool) -> CFTimeZone!](https://developer.apple.com/documentation/corefoundation/1541923-cftimezonecreatewithname)

|  | Declaration |
| --- | --- |
| From | ``` func CFTimeZoneCreateWithName(_ allocator: CFAllocator!, _ name: CFString!, _ tryAbbrev: Boolean) -> CFTimeZone! ``` |
| To | ``` func CFTimeZoneCreateWithName(_ allocator: CFAllocator!, _ name: CFString!, _ tryAbbrev: Bool) -> CFTimeZone! ``` |

Modified [CFTimeZoneIsDaylightSavingTime(_: CFTimeZone!, _: CFAbsoluteTime) -> Bool](https://developer.apple.com/documentation/corefoundation/1541793-cftimezoneisdaylightsavingtime)

|  | Declaration |
| --- | --- |
| From | ``` func CFTimeZoneIsDaylightSavingTime(_ tz: CFTimeZone!, _ at: CFAbsoluteTime) -> Boolean ``` |
| To | ``` func CFTimeZoneIsDaylightSavingTime(_ tz: CFTimeZone!, _ at: CFAbsoluteTime) -> Bool ``` |

Modified [CFTreeApplierFunction](https://developer.apple.com/documentation/corefoundation/cftreeapplierfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFTreeApplierFunction = CFunctionPointer<((UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFTreeApplierFunction = (UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CFTreeApplyFunctionToChildren(_: CFTree!, _: CFTreeApplierFunction!, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/corefoundation/1401759-cftreeapplyfunctiontochildren)

|  | Declaration |
| --- | --- |
| From | ``` func CFTreeApplyFunctionToChildren(_ tree: CFTree!, _ applier: CFTreeApplierFunction, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func CFTreeApplyFunctionToChildren(_ tree: CFTree!, _ applier: CFTreeApplierFunction!, _ context: UnsafeMutablePointer<Void>) ``` |

Modified [CFTreeCopyDescriptionCallBack](https://developer.apple.com/documentation/corefoundation/cftreecopydescriptioncallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFTreeCopyDescriptionCallBack = CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |
| To | ``` typealias CFTreeCopyDescriptionCallBack = (UnsafePointer<Void>) -> Unmanaged<CFString>! ``` |

Modified [CFTreeReleaseCallBack](https://developer.apple.com/documentation/corefoundation/cftreereleasecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFTreeReleaseCallBack = CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFTreeReleaseCallBack = (UnsafePointer<Void>) -> Void ``` |

Modified [CFTreeRetainCallBack](https://developer.apple.com/documentation/corefoundation/cftreeretaincallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFTreeRetainCallBack = CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |
| To | ``` typealias CFTreeRetainCallBack = (UnsafePointer<Void>) -> UnsafePointer<Void> ``` |

Modified [CFTreeSortChildren(_: CFTree!, _: CFComparatorFunction!, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/corefoundation/1401787-cftreesortchildren)

|  | Declaration |
| --- | --- |
| From | ``` func CFTreeSortChildren(_ tree: CFTree!, _ comparator: CFComparatorFunction, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func CFTreeSortChildren(_ tree: CFTree!, _ comparator: CFComparatorFunction!, _ context: UnsafeMutablePointer<Void>) ``` |

Modified [CFURLCanBeDecomposed(_: CFURL!) -> Bool](https://developer.apple.com/documentation/corefoundation/1542131-cfurlcanbedecomposed)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCanBeDecomposed(_ anURL: CFURL!) -> Boolean ``` |
| To | ``` func CFURLCanBeDecomposed(_ anURL: CFURL!) -> Bool ``` |

Modified [CFURLCopyResourcePropertyForKey(_: CFURL!, _: CFString!, _: UnsafeMutablePointer<Void>, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/corefoundation/1542764-cfurlcopyresourcepropertyforkey)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCopyResourcePropertyForKey(_ url: CFURL!, _ key: CFString!, _ propertyValueTypeRefPtr: UnsafeMutablePointer<Void>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean ``` |
| To | ``` func CFURLCopyResourcePropertyForKey(_ url: CFURL!, _ key: CFString!, _ propertyValueTypeRefPtr: UnsafeMutablePointer<Void>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [CFURLCopyStrictPath(_: CFURL!, _: UnsafeMutablePointer<DarwinBoolean>) -> CFString!](https://developer.apple.com/documentation/corefoundation/1542952-cfurlcopystrictpath)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCopyStrictPath(_ anURL: CFURL!, _ isAbsolute: UnsafeMutablePointer<Boolean>) -> CFString! ``` |
| To | ``` func CFURLCopyStrictPath(_ anURL: CFURL!, _ isAbsolute: UnsafeMutablePointer<DarwinBoolean>) -> CFString! ``` |

Modified [CFURLCreateAbsoluteURLWithBytes(_: CFAllocator!, _: UnsafePointer<UInt8>, _: CFIndex, _: CFStringEncoding, _: CFURL!, _: Bool) -> CFURL!](https://developer.apple.com/documentation/corefoundation/1542795-cfurlcreateabsoluteurlwithbytes)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCreateAbsoluteURLWithBytes(_ alloc: CFAllocator!, _ relativeURLBytes: UnsafePointer<UInt8>, _ length: CFIndex, _ encoding: CFStringEncoding, _ baseURL: CFURL!, _ useCompatibilityMode: Boolean) -> CFURL! ``` |
| To | ``` func CFURLCreateAbsoluteURLWithBytes(_ alloc: CFAllocator!, _ relativeURLBytes: UnsafePointer<UInt8>, _ length: CFIndex, _ encoding: CFStringEncoding, _ baseURL: CFURL!, _ useCompatibilityMode: Bool) -> CFURL! ``` |

Modified [CFURLCreateByResolvingBookmarkData(_: CFAllocator!, _: CFData!, _: CFURLBookmarkResolutionOptions, _: CFURL!, _: CFArray!, _: UnsafeMutablePointer<DarwinBoolean>, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>!](https://developer.apple.com/documentation/corefoundation/1543252-cfurlcreatebyresolvingbookmarkda)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCreateByResolvingBookmarkData(_ allocator: CFAllocator!, _ bookmark: CFData!, _ options: CFURLBookmarkResolutionOptions, _ relativeToURL: CFURL!, _ resourcePropertiesToInclude: CFArray!, _ isStale: UnsafeMutablePointer<Boolean>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>! ``` |
| To | ``` func CFURLCreateByResolvingBookmarkData(_ allocator: CFAllocator!, _ bookmark: CFData!, _ options: CFURLBookmarkResolutionOptions, _ relativeToURL: CFURL!, _ resourcePropertiesToInclude: CFArray!, _ isStale: UnsafeMutablePointer<DarwinBoolean>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>! ``` |

Modified [CFURLCreateCopyAppendingPathComponent(_: CFAllocator!, _: CFURL!, _: CFString!, _: Bool) -> CFURL!](https://developer.apple.com/documentation/corefoundation/1542127-cfurlcreatecopyappendingpathcomp)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCreateCopyAppendingPathComponent(_ allocator: CFAllocator!, _ url: CFURL!, _ pathComponent: CFString!, _ isDirectory: Boolean) -> CFURL! ``` |
| To | ``` func CFURLCreateCopyAppendingPathComponent(_ allocator: CFAllocator!, _ url: CFURL!, _ pathComponent: CFString!, _ isDirectory: Bool) -> CFURL! ``` |

Modified [CFURLCreateData(_: CFAllocator!, _: CFURL!, _: CFStringEncoding, _: Bool) -> CFData!](https://developer.apple.com/documentation/corefoundation/1543276-cfurlcreatedata)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCreateData(_ allocator: CFAllocator!, _ url: CFURL!, _ encoding: CFStringEncoding, _ escapeWhitespace: Boolean) -> CFData! ``` |
| To | ``` func CFURLCreateData(_ allocator: CFAllocator!, _ url: CFURL!, _ encoding: CFStringEncoding, _ escapeWhitespace: Bool) -> CFData! ``` |

Modified [CFURLCreateFromFileSystemRepresentation(_: CFAllocator!, _: UnsafePointer<UInt8>, _: CFIndex, _: Bool) -> CFURL!](https://developer.apple.com/documentation/corefoundation/1543314-cfurlcreatefromfilesystemreprese)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCreateFromFileSystemRepresentation(_ allocator: CFAllocator!, _ buffer: UnsafePointer<UInt8>, _ bufLen: CFIndex, _ isDirectory: Boolean) -> CFURL! ``` |
| To | ``` func CFURLCreateFromFileSystemRepresentation(_ allocator: CFAllocator!, _ buffer: UnsafePointer<UInt8>, _ bufLen: CFIndex, _ isDirectory: Bool) -> CFURL! ``` |

Modified [CFURLCreateFromFileSystemRepresentationRelativeToBase(_: CFAllocator!, _: UnsafePointer<UInt8>, _: CFIndex, _: Bool, _: CFURL!) -> CFURL!](https://developer.apple.com/documentation/corefoundation/1542053-cfurlcreatefromfilesystemreprese)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCreateFromFileSystemRepresentationRelativeToBase(_ allocator: CFAllocator!, _ buffer: UnsafePointer<UInt8>, _ bufLen: CFIndex, _ isDirectory: Boolean, _ baseURL: CFURL!) -> CFURL! ``` |
| To | ``` func CFURLCreateFromFileSystemRepresentationRelativeToBase(_ allocator: CFAllocator!, _ buffer: UnsafePointer<UInt8>, _ bufLen: CFIndex, _ isDirectory: Bool, _ baseURL: CFURL!) -> CFURL! ``` |

Modified [CFURLCreateStringByAddingPercentEscapes(_: CFAllocator!, _: CFString!, _: CFString!, _: CFString!, _: CFStringEncoding) -> CFString!](https://developer.apple.com/documentation/corefoundation/1542665-cfurlcreatestringbyaddingpercent)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [CFURLCreateStringByReplacingPercentEscapesUsingEncoding(_: CFAllocator!, _: CFString!, _: CFString!, _: CFStringEncoding) -> CFString!](https://developer.apple.com/documentation/corefoundation/1541974-cfurlcreatestringbyreplacingperc)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [CFURLCreateWithFileSystemPath(_: CFAllocator!, _: CFString!, _: CFURLPathStyle, _: Bool) -> CFURL!](https://developer.apple.com/documentation/corefoundation/1543250-cfurlcreatewithfilesystempath)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCreateWithFileSystemPath(_ allocator: CFAllocator!, _ filePath: CFString!, _ pathStyle: CFURLPathStyle, _ isDirectory: Boolean) -> CFURL! ``` |
| To | ``` func CFURLCreateWithFileSystemPath(_ allocator: CFAllocator!, _ filePath: CFString!, _ pathStyle: CFURLPathStyle, _ isDirectory: Bool) -> CFURL! ``` |

Modified [CFURLCreateWithFileSystemPathRelativeToBase(_: CFAllocator!, _: CFString!, _: CFURLPathStyle, _: Bool, _: CFURL!) -> CFURL!](https://developer.apple.com/documentation/corefoundation/1543552-cfurlcreatewithfilesystempathrel)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCreateWithFileSystemPathRelativeToBase(_ allocator: CFAllocator!, _ filePath: CFString!, _ pathStyle: CFURLPathStyle, _ isDirectory: Boolean, _ baseURL: CFURL!) -> CFURL! ``` |
| To | ``` func CFURLCreateWithFileSystemPathRelativeToBase(_ allocator: CFAllocator!, _ filePath: CFString!, _ pathStyle: CFURLPathStyle, _ isDirectory: Bool, _ baseURL: CFURL!) -> CFURL! ``` |

Modified [CFURLGetFileSystemRepresentation(_: CFURL!, _: Bool, _: UnsafeMutablePointer<UInt8>, _: CFIndex) -> Bool](https://developer.apple.com/documentation/corefoundation/1541515-cfurlgetfilesystemrepresentation)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLGetFileSystemRepresentation(_ url: CFURL!, _ resolveAgainstBase: Boolean, _ buffer: UnsafeMutablePointer<UInt8>, _ maxBufLen: CFIndex) -> Boolean ``` |
| To | ``` func CFURLGetFileSystemRepresentation(_ url: CFURL!, _ resolveAgainstBase: Bool, _ buffer: UnsafeMutablePointer<UInt8>, _ maxBufLen: CFIndex) -> Bool ``` |

Modified [CFURLHasDirectoryPath(_: CFURL!) -> Bool](https://developer.apple.com/documentation/corefoundation/1542229-cfurlhasdirectorypath)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLHasDirectoryPath(_ anURL: CFURL!) -> Boolean ``` |
| To | ``` func CFURLHasDirectoryPath(_ anURL: CFURL!) -> Bool ``` |

Modified [CFURLIsFileReferenceURL(_: CFURL!) -> Bool](https://developer.apple.com/documentation/corefoundation/1543161-cfurlisfilereferenceurl)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLIsFileReferenceURL(_ url: CFURL!) -> Boolean ``` |
| To | ``` func CFURLIsFileReferenceURL(_ url: CFURL!) -> Bool ``` |

Modified [CFURLResourceIsReachable(_: CFURL!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/corefoundation/1543666-cfurlresourceisreachable)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLResourceIsReachable(_ url: CFURL!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean ``` |
| To | ``` func CFURLResourceIsReachable(_ url: CFURL!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [CFURLSetResourcePropertiesForKeys(_: CFURL!, _: CFDictionary!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/corefoundation/1542947-cfurlsetresourcepropertiesforkey)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLSetResourcePropertiesForKeys(_ url: CFURL!, _ keyedPropertyValues: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean ``` |
| To | ``` func CFURLSetResourcePropertiesForKeys(_ url: CFURL!, _ keyedPropertyValues: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [CFURLSetResourcePropertyForKey(_: CFURL!, _: CFString!, _: AnyObject!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/corefoundation/1541607-cfurlsetresourcepropertyforkey)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLSetResourcePropertyForKey(_ url: CFURL!, _ key: CFString!, _ propertyValue: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean ``` |
| To | ``` func CFURLSetResourcePropertyForKey(_ url: CFURL!, _ key: CFString!, _ propertyValue: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [CFURLStartAccessingSecurityScopedResource(_: CFURL!) -> Bool](https://developer.apple.com/documentation/corefoundation/1543318-cfurlstartaccessingsecurityscope)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLStartAccessingSecurityScopedResource(_ url: CFURL!) -> Boolean ``` |
| To | ``` func CFURLStartAccessingSecurityScopedResource(_ url: CFURL!) -> Bool ``` |

Modified [CFURLWriteBookmarkDataToFile(_: CFData!, _: CFURL!, _: CFURLBookmarkFileCreationOptions, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/corefoundation/1541737-cfurlwritebookmarkdatatofile)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLWriteBookmarkDataToFile(_ bookmarkRef: CFData!, _ fileURL: CFURL!, _ options: CFURLBookmarkFileCreationOptions, _ errorRef: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean ``` |
| To | ``` func CFURLWriteBookmarkDataToFile(_ bookmarkRef: CFData!, _ fileURL: CFURL!, _ options: CFURLBookmarkFileCreationOptions, _ errorRef: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [CFWriteStreamCanAcceptBytes(_: CFWriteStream!) -> Bool](https://developer.apple.com/documentation/corefoundation/1539684-cfwritestreamcanacceptbytes)

|  | Declaration |
| --- | --- |
| From | ``` func CFWriteStreamCanAcceptBytes(_ stream: CFWriteStream!) -> Boolean ``` |
| To | ``` func CFWriteStreamCanAcceptBytes(_ stream: CFWriteStream!) -> Bool ``` |

Modified [CFWriteStreamClientCallBack](https://developer.apple.com/documentation/corefoundation/cfwritestreamclientcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFWriteStreamClientCallBack = CFunctionPointer<((CFWriteStream!, CFStreamEventType, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFWriteStreamClientCallBack = (CFWriteStream!, CFStreamEventType, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CFWriteStreamOpen(_: CFWriteStream!) -> Bool](https://developer.apple.com/documentation/corefoundation/1539753-cfwritestreamopen)

|  | Declaration |
| --- | --- |
| From | ``` func CFWriteStreamOpen(_ stream: CFWriteStream!) -> Boolean ``` |
| To | ``` func CFWriteStreamOpen(_ stream: CFWriteStream!) -> Bool ``` |

Modified [CFWriteStreamSetClient(_: CFWriteStream!, _: CFOptionFlags, _: CFWriteStreamClientCallBack!, _: UnsafeMutablePointer<CFStreamClientContext>) -> Bool](https://developer.apple.com/documentation/corefoundation/1539678-cfwritestreamsetclient)

|  | Declaration |
| --- | --- |
| From | ``` func CFWriteStreamSetClient(_ stream: CFWriteStream!, _ streamEvents: CFOptionFlags, _ clientCB: CFWriteStreamClientCallBack, _ clientContext: UnsafeMutablePointer<CFStreamClientContext>) -> Boolean ``` |
| To | ``` func CFWriteStreamSetClient(_ stream: CFWriteStream!, _ streamEvents: CFOptionFlags, _ clientCB: CFWriteStreamClientCallBack!, _ clientContext: UnsafeMutablePointer<CFStreamClientContext>) -> Bool ``` |

Modified [CFWriteStreamSetProperty(_: CFWriteStream!, _: CFString!, _: AnyObject!) -> Bool](https://developer.apple.com/documentation/corefoundation/1539609-cfwritestreamsetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func CFWriteStreamSetProperty(_ stream: CFWriteStream!, _ propertyName: CFString!, _ propertyValue: AnyObject!) -> Boolean ``` |
| To | ``` func CFWriteStreamSetProperty(_ stream: CFWriteStream!, _ propertyName: CFString!, _ propertyValue: AnyObject!) -> Bool ``` |

Modified [kCFCalendarComponentsWrap](https://developer.apple.com/documentation/corefoundation/kcfcalendarcomponentswrap)

|  | Declaration |
| --- | --- |
| From | ``` var kCFCalendarComponentsWrap: Int { get } ``` |
| To | ``` var kCFCalendarComponentsWrap: CFOptionFlags { get } ``` |

Modified [kCFFileDescriptorReadCallBack](https://developer.apple.com/documentation/corefoundation/kcffiledescriptorreadcallback)

|  | Declaration |
| --- | --- |
| From | ``` var kCFFileDescriptorReadCallBack: Int { get } ``` |
| To | ``` var kCFFileDescriptorReadCallBack: CFOptionFlags { get } ``` |

Modified [kCFFileDescriptorWriteCallBack](https://developer.apple.com/documentation/corefoundation/1477595-callback_identifiers/kcffiledescriptorwritecallback)

|  | Declaration |
| --- | --- |
| From | ``` var kCFFileDescriptorWriteCallBack: Int { get } ``` |
| To | ``` var kCFFileDescriptorWriteCallBack: CFOptionFlags { get } ``` |

Modified [kCFMessagePortBecameInvalidError](https://developer.apple.com/documentation/corefoundation/1561514-cfmessageportsendrequest_error_c/kcfmessageportbecameinvaliderror)

|  | Declaration |
| --- | --- |
| From | ``` var kCFMessagePortBecameInvalidError: Int { get } ``` |
| To | ``` var kCFMessagePortBecameInvalidError: Int32 { get } ``` |

Modified [kCFMessagePortIsInvalid](https://developer.apple.com/documentation/corefoundation/kcfmessageportisinvalid)

|  | Declaration |
| --- | --- |
| From | ``` var kCFMessagePortIsInvalid: Int { get } ``` |
| To | ``` var kCFMessagePortIsInvalid: Int32 { get } ``` |

Modified [kCFMessagePortReceiveTimeout](https://developer.apple.com/documentation/corefoundation/1561514-cfmessageportsendrequest_error_c/kcfmessageportreceivetimeout)

|  | Declaration |
| --- | --- |
| From | ``` var kCFMessagePortReceiveTimeout: Int { get } ``` |
| To | ``` var kCFMessagePortReceiveTimeout: Int32 { get } ``` |

Modified [kCFMessagePortSendTimeout](https://developer.apple.com/documentation/corefoundation/1561514-cfmessageportsendrequest_error_c/kcfmessageportsendtimeout)

|  | Declaration |
| --- | --- |
| From | ``` var kCFMessagePortSendTimeout: Int { get } ``` |
| To | ``` var kCFMessagePortSendTimeout: Int32 { get } ``` |

Modified [kCFMessagePortSuccess](https://developer.apple.com/documentation/corefoundation/kcfmessageportsuccess)

|  | Declaration |
| --- | --- |
| From | ``` var kCFMessagePortSuccess: Int { get } ``` |
| To | ``` var kCFMessagePortSuccess: Int32 { get } ``` |

Modified [kCFMessagePortTransportError](https://developer.apple.com/documentation/corefoundation/1561514-cfmessageportsendrequest_error_c/kcfmessageporttransporterror)

|  | Declaration |
| --- | --- |
| From | ``` var kCFMessagePortTransportError: Int { get } ``` |
| To | ``` var kCFMessagePortTransportError: Int32 { get } ``` |

Modified [kCFNotFound](https://developer.apple.com/documentation/corefoundation/kcfnotfound)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCFNotFound: Int { get } ``` | iOS 8.0 |
| To | ``` let kCFNotFound: CFIndex ``` | iOS 9.0 |

Modified [kCFNotificationDeliverImmediately](https://developer.apple.com/documentation/corefoundation/1569610-notification_posting_options/kcfnotificationdeliverimmediately)

|  | Declaration |
| --- | --- |
| From | ``` var kCFNotificationDeliverImmediately: Int { get } ``` |
| To | ``` var kCFNotificationDeliverImmediately: CFOptionFlags { get } ``` |

Modified [kCFNotificationPostToAllSessions](https://developer.apple.com/documentation/corefoundation/kcfnotificationposttoallsessions)

|  | Declaration |
| --- | --- |
| From | ``` var kCFNotificationPostToAllSessions: Int { get } ``` |
| To | ``` var kCFNotificationPostToAllSessions: CFOptionFlags { get } ``` |

Modified [kCFPropertyListReadCorruptError](https://developer.apple.com/documentation/corefoundation/1429999-reading_and_writing_error_codes/kcfpropertylistreadcorrupterror)

|  | Declaration |
| --- | --- |
| From | ``` var kCFPropertyListReadCorruptError: Int { get } ``` |
| To | ``` var kCFPropertyListReadCorruptError: CFIndex { get } ``` |

Modified [kCFPropertyListReadStreamError](https://developer.apple.com/documentation/corefoundation/kcfpropertylistreadstreamerror)

|  | Declaration |
| --- | --- |
| From | ``` var kCFPropertyListReadStreamError: Int { get } ``` |
| To | ``` var kCFPropertyListReadStreamError: CFIndex { get } ``` |

Modified [kCFPropertyListReadUnknownVersionError](https://developer.apple.com/documentation/corefoundation/kcfpropertylistreadunknownversionerror)

|  | Declaration |
| --- | --- |
| From | ``` var kCFPropertyListReadUnknownVersionError: Int { get } ``` |
| To | ``` var kCFPropertyListReadUnknownVersionError: CFIndex { get } ``` |

Modified [kCFPropertyListWriteStreamError](https://developer.apple.com/documentation/corefoundation/1429999-reading_and_writing_error_codes/kcfpropertylistwritestreamerror)

|  | Declaration |
| --- | --- |
| From | ``` var kCFPropertyListWriteStreamError: Int { get } ``` |
| To | ``` var kCFPropertyListWriteStreamError: CFIndex { get } ``` |

Modified [kCFSocketAutomaticallyReenableAcceptCallBack](https://developer.apple.com/documentation/corefoundation/1560944-cfsocket_flags/kcfsocketautomaticallyreenableacceptcallback)

|  | Declaration |
| --- | --- |
| From | ``` var kCFSocketAutomaticallyReenableAcceptCallBack: Int { get } ``` |
| To | ``` var kCFSocketAutomaticallyReenableAcceptCallBack: CFOptionFlags { get } ``` |

Modified [kCFSocketAutomaticallyReenableDataCallBack](https://developer.apple.com/documentation/corefoundation/kcfsocketautomaticallyreenabledatacallback)

|  | Declaration |
| --- | --- |
| From | ``` var kCFSocketAutomaticallyReenableDataCallBack: Int { get } ``` |
| To | ``` var kCFSocketAutomaticallyReenableDataCallBack: CFOptionFlags { get } ``` |

Modified [kCFSocketAutomaticallyReenableReadCallBack](https://developer.apple.com/documentation/corefoundation/1560944-cfsocket_flags/kcfsocketautomaticallyreenablereadcallback)

|  | Declaration |
| --- | --- |
| From | ``` var kCFSocketAutomaticallyReenableReadCallBack: Int { get } ``` |
| To | ``` var kCFSocketAutomaticallyReenableReadCallBack: CFOptionFlags { get } ``` |

Modified [kCFSocketAutomaticallyReenableWriteCallBack](https://developer.apple.com/documentation/corefoundation/kcfsocketautomaticallyreenablewritecallback)

|  | Declaration |
| --- | --- |
| From | ``` var kCFSocketAutomaticallyReenableWriteCallBack: Int { get } ``` |
| To | ``` var kCFSocketAutomaticallyReenableWriteCallBack: CFOptionFlags { get } ``` |

Modified [kCFSocketCloseOnInvalidate](https://developer.apple.com/documentation/corefoundation/kcfsocketcloseoninvalidate)

|  | Declaration |
| --- | --- |
| From | ``` var kCFSocketCloseOnInvalidate: Int { get } ``` |
| To | ``` var kCFSocketCloseOnInvalidate: CFOptionFlags { get } ``` |

Modified [kCFSocketLeaveErrors](https://developer.apple.com/documentation/corefoundation/kcfsocketleaveerrors)

|  | Declaration |
| --- | --- |
| From | ``` var kCFSocketLeaveErrors: Int { get } ``` |
| To | ``` var kCFSocketLeaveErrors: CFOptionFlags { get } ``` |

Modified [kCFStringTokenizerAttributeLanguage](https://developer.apple.com/documentation/corefoundation/kcfstringtokenizerattributelanguage)

|  | Declaration |
| --- | --- |
| From | ``` var kCFStringTokenizerAttributeLanguage: Int { get } ``` |
| To | ``` var kCFStringTokenizerAttributeLanguage: CFOptionFlags { get } ``` |

Modified [kCFStringTokenizerAttributeLatinTranscription](https://developer.apple.com/documentation/corefoundation/1588024-tokenization_modifiers/kcfstringtokenizerattributelatintranscription)

|  | Declaration |
| --- | --- |
| From | ``` var kCFStringTokenizerAttributeLatinTranscription: Int { get } ``` |
| To | ``` var kCFStringTokenizerAttributeLatinTranscription: CFOptionFlags { get } ``` |

Modified [kCFStringTokenizerUnitLineBreak](https://developer.apple.com/documentation/corefoundation/1588024-tokenization_modifiers/kcfstringtokenizerunitlinebreak)

|  | Declaration |
| --- | --- |
| From | ``` var kCFStringTokenizerUnitLineBreak: Int { get } ``` |
| To | ``` var kCFStringTokenizerUnitLineBreak: CFOptionFlags { get } ``` |

Modified [kCFStringTokenizerUnitParagraph](https://developer.apple.com/documentation/corefoundation/kcfstringtokenizerunitparagraph)

|  | Declaration |
| --- | --- |
| From | ``` var kCFStringTokenizerUnitParagraph: Int { get } ``` |
| To | ``` var kCFStringTokenizerUnitParagraph: CFOptionFlags { get } ``` |

Modified [kCFStringTokenizerUnitSentence](https://developer.apple.com/documentation/corefoundation/1588024-tokenization_modifiers/kcfstringtokenizerunitsentence)

|  | Declaration |
| --- | --- |
| From | ``` var kCFStringTokenizerUnitSentence: Int { get } ``` |
| To | ``` var kCFStringTokenizerUnitSentence: CFOptionFlags { get } ``` |

Modified [kCFStringTokenizerUnitWord](https://developer.apple.com/documentation/corefoundation/kcfstringtokenizerunitword)

|  | Declaration |
| --- | --- |
| From | ``` var kCFStringTokenizerUnitWord: Int { get } ``` |
| To | ``` var kCFStringTokenizerUnitWord: CFOptionFlags { get } ``` |

Modified [kCFStringTokenizerUnitWordBoundary](https://developer.apple.com/documentation/corefoundation/kcfstringtokenizerunitwordboundary)

|  | Declaration |
| --- | --- |
| From | ``` var kCFStringTokenizerUnitWordBoundary: Int { get } ``` |
| To | ``` var kCFStringTokenizerUnitWordBoundary: CFOptionFlags { get } ``` |

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
