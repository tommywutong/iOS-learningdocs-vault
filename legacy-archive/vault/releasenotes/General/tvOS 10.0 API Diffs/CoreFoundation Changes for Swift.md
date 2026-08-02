---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Swift/CoreFoundation.html
archived_at: '2026-07-18T02:57:37.155005Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# CoreFoundation Changes for Swift

### CoreFoundation

Removed CFAllocatorContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFAllocatorRetainCallBack!, release: CFAllocatorReleaseCallBack!, copyDescription: CFAllocatorCopyDescriptionCallBack!, allocate: CFAllocatorAllocateCallBack!, reallocate: CFAllocatorReallocateCallBack!, deallocate: CFAllocatorDeallocateCallBack!, preferredSize: CFAllocatorPreferredSizeCallBack!)Removed CFArrayCallBacks.init(version: CFIndex, retain: CFArrayRetainCallBack!, release: CFArrayReleaseCallBack!, copyDescription: CFArrayCopyDescriptionCallBack!, equal: CFArrayEqualCallBack!)Removed CFBagCallBacks.init(version: CFIndex, retain: CFBagRetainCallBack!, release: CFBagReleaseCallBack!, copyDescription: CFBagCopyDescriptionCallBack!, equal: CFBagEqualCallBack!, hash: CFBagHashCallBack!)Removed CFBinaryHeapCallBacks.init(version: CFIndex, retain: ((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)!, release: ((CFAllocator!, UnsafePointer<Void>) -> Void)!, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!, compare: ((UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> CFComparisonResult)!)Removed CFBinaryHeapCompareContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release: ((UnsafePointer<Void>) -> Void)!, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!)Removed CFDictionaryKeyCallBacks.init(version: CFIndex, retain: CFDictionaryRetainCallBack!, release: CFDictionaryReleaseCallBack!, copyDescription: CFDictionaryCopyDescriptionCallBack!, equal: CFDictionaryEqualCallBack!, hash: CFDictionaryHashCallBack!)Removed CFDictionaryValueCallBacks.init(version: CFIndex, retain: CFDictionaryRetainCallBack!, release: CFDictionaryReleaseCallBack!, copyDescription: CFDictionaryCopyDescriptionCallBack!, equal: CFDictionaryEqualCallBack!)Removed CFFileDescriptorContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)!, release: ((UnsafeMutablePointer<Void>) -> Void)!, copyDescription: ((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)!)Removed CFMachPortContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release: ((UnsafePointer<Void>) -> Void)!, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!)Removed CFMessagePortContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release: ((UnsafePointer<Void>) -> Void)!, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!)Removed [CFPropertyListMutabilityOptions.Immutable](https://developer.apple.com/documentation/corefoundation/cfpropertylistmutabilityoptions/kcfpropertylistimmutable)Removed CFRunLoopObserverContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release: ((UnsafePointer<Void>) -> Void)!, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!)Removed CFRunLoopSourceContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release: ((UnsafePointer<Void>) -> Void)!, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!, equal: ((UnsafePointer<Void>, UnsafePointer<Void>) -> DarwinBoolean)!, hash: ((UnsafePointer<Void>) -> CFHashCode)!, schedule: ((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)!, cancel: ((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)!, perform: ((UnsafeMutablePointer<Void>) -> Void)!)Removed CFRunLoopSourceContext1.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release: ((UnsafePointer<Void>) -> Void)!, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!, equal: ((UnsafePointer<Void>, UnsafePointer<Void>) -> DarwinBoolean)!, hash: ((UnsafePointer<Void>) -> CFHashCode)!, getPort: ((UnsafeMutablePointer<Void>) -> mach_port_t)!, perform: ((UnsafeMutablePointer<Void>, CFIndex, CFAllocator!, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)!)Removed CFRunLoopTimerContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release: ((UnsafePointer<Void>) -> Void)!, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!)Removed CFSetCallBacks.init(version: CFIndex, retain: CFSetRetainCallBack!, release: CFSetReleaseCallBack!, copyDescription: CFSetCopyDescriptionCallBack!, equal: CFSetEqualCallBack!, hash: CFSetHashCallBack!)Removed [CFSocketCallBackType.NoCallBack](https://developer.apple.com/documentation/corefoundation/cfsocketcallbacktype/kcfsocketnocallback)Removed CFSocketContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release: ((UnsafePointer<Void>) -> Void)!, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!)Removed CFStreamClientContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)!, release: ((UnsafeMutablePointer<Void>) -> Void)!, copyDescription: ((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)!)Removed [CFStreamEventType.None](https://developer.apple.com/documentation/corefoundation/cfstreameventtype/kcfstreameventnone)Removed [CFStringInlineBuffer.init(buffer: (UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar), theString: Unmanaged<CFString>!, directUniCharBuffer: UnsafePointer<UniChar>, directCStringBuffer: UnsafePointer<Int8>, rangeToBuffer: CFRange, bufferedRangeStart: CFIndex, bufferedRangeEnd: CFIndex)](https://developer.apple.com/documentation/corefoundation/cfstringinlinebuffer/1542752-init)Removed [CFStringTokenizerTokenType.None](https://developer.apple.com/documentation/corefoundation/cfstringtokenizertokentype/kcfstringtokenizertokennone)Removed CFTreeContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFTreeRetainCallBack!, release: CFTreeReleaseCallBack!, copyDescription: CFTreeCopyDescriptionCallBack!)Removed [CFURLEnumeratorOptions.DefaultBehavior](https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/kcfurlenumeratordefaultbehavior)Added [CFAllocatorContext.init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: CoreFoundation.CFAllocatorRetainCallBack!, release: CoreFoundation.CFAllocatorReleaseCallBack!, copyDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack!, allocate: CoreFoundation.CFAllocatorAllocateCallBack!, reallocate: CoreFoundation.CFAllocatorReallocateCallBack!, deallocate: CoreFoundation.CFAllocatorDeallocateCallBack!, preferredSize: CoreFoundation.CFAllocatorPreferredSizeCallBack!)](https://developer.apple.com/documentation/corefoundation/cfallocatorcontext/1780517-init)Added [CFArrayCallBacks.init(version: CFIndex, retain: CoreFoundation.CFArrayRetainCallBack!, release: CoreFoundation.CFArrayReleaseCallBack!, copyDescription: CoreFoundation.CFArrayCopyDescriptionCallBack!, equal: CoreFoundation.CFArrayEqualCallBack!)](https://developer.apple.com/documentation/corefoundation/cfarraycallbacks/1780507-init)Added [CFBagCallBacks.init(version: CFIndex, retain: CoreFoundation.CFBagRetainCallBack!, release: CoreFoundation.CFBagReleaseCallBack!, copyDescription: CoreFoundation.CFBagCopyDescriptionCallBack!, equal: CoreFoundation.CFBagEqualCallBack!, hash: CoreFoundation.CFBagHashCallBack!)](https://developer.apple.com/documentation/corefoundation/cfbagcallbacks/1780499-init)Added [CFBinaryHeapCallBacks.init(version: CFIndex, retain: ( (CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer?)!, release: ( (CFAllocator?, UnsafeRawPointer?) -> Swift.Void)!, copyDescription: ( (UnsafeRawPointer?) -> Unmanaged<CFString>?)!, compare: ( (UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> CFComparisonResult)!)](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcallbacks/1780514-init)Added [CFBinaryHeapCompareContext.init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ( (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release: ( (UnsafeRawPointer?) -> Swift.Void)!, copyDescription: ( (UnsafeRawPointer?) -> Unmanaged<CFString>?)!)](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcomparecontext/1780495-init)Added [CFCalendarIdentifier [struct]](https://developer.apple.com/documentation/corefoundation/cfcalendaridentifier)Added [CFCalendarIdentifier.init(rawValue: CFString)](https://developer.apple.com/documentation/corefoundation/cfcalendaridentifier/1780515-init)Added [CFDateFormatterKey [struct]](https://developer.apple.com/documentation/corefoundation/cfdateformatterkey)Added [CFDateFormatterKey.init(rawValue: CFString)](https://developer.apple.com/documentation/corefoundation/cfdateformatterkey/1780504-init)Added [CFDictionaryKeyCallBacks.init(version: CFIndex, retain: CoreFoundation.CFDictionaryRetainCallBack!, release: CoreFoundation.CFDictionaryReleaseCallBack!, copyDescription: CoreFoundation.CFDictionaryCopyDescriptionCallBack!, equal: CoreFoundation.CFDictionaryEqualCallBack!, hash: CoreFoundation.CFDictionaryHashCallBack!)](https://developer.apple.com/documentation/corefoundation/cfdictionarykeycallbacks/1780509-init)Added [CFDictionaryValueCallBacks.init(version: CFIndex, retain: CoreFoundation.CFDictionaryRetainCallBack!, release: CoreFoundation.CFDictionaryReleaseCallBack!, copyDescription: CoreFoundation.CFDictionaryCopyDescriptionCallBack!, equal: CoreFoundation.CFDictionaryEqualCallBack!)](https://developer.apple.com/documentation/corefoundation/cfdictionaryvaluecallbacks/1780508-init)Added [CFFileDescriptorContext.init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ( (UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!, release: ( (UnsafeMutableRawPointer?) -> Swift.Void)!, copyDescription: ( (UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!)](https://developer.apple.com/documentation/corefoundation/cffiledescriptorcontext/1780513-init)Added [CFISO8601DateFormatOptions [struct]](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions)Added [CFISO8601DateFormatOptions.init(rawValue: CFOptionFlags)](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/1643415-init)Added [CFISO8601DateFormatOptions.withColonSeparatorInTime](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/1643398-withcolonseparatorintime)Added [CFISO8601DateFormatOptions.withColonSeparatorInTimeZone](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/1643367-withcolonseparatorintimezone)Added [CFISO8601DateFormatOptions.withDashSeparatorInDate](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/kcfiso8601dateformatwithdashseparatorindate)Added [CFISO8601DateFormatOptions.withDay](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/kcfiso8601dateformatwithday)Added [CFISO8601DateFormatOptions.withFullDate](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/kcfiso8601dateformatwithfulldate)Added [CFISO8601DateFormatOptions.withFullTime](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/kcfiso8601dateformatwithfulltime)Added [CFISO8601DateFormatOptions.withInternetDateTime](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/kcfiso8601dateformatwithinternetdatetime)Added [CFISO8601DateFormatOptions.withMonth](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/kcfiso8601dateformatwithmonth)Added [CFISO8601DateFormatOptions.withSpaceBetweenDateAndTime](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/kcfiso8601dateformatwithspacebetweendateandtime)Added [CFISO8601DateFormatOptions.withTime](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/kcfiso8601dateformatwithtime)Added [CFISO8601DateFormatOptions.withTimeZone](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/kcfiso8601dateformatwithtimezone)Added [CFISO8601DateFormatOptions.withWeekOfYear](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/1643355-withweekofyear)Added [CFISO8601DateFormatOptions.withYear](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/1643330-withyear)Added [CFLocaleIdentifier [struct]](https://developer.apple.com/documentation/corefoundation/cflocaleidentifier)Added [CFLocaleIdentifier.init(_: CFString)](https://developer.apple.com/documentation/corefoundation/cflocaleidentifier/1924278-init)Added [CFLocaleIdentifier.init(rawValue: CFString)](https://developer.apple.com/documentation/corefoundation/cflocaleidentifier/1780494-init)Added [CFLocaleKey [struct]](https://developer.apple.com/documentation/corefoundation/cflocalekey)Added [CFLocaleKey.init(rawValue: CFString)](https://developer.apple.com/documentation/corefoundation/cflocalekey/1780516-init)Added [CFMachPortContext.init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ( (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release: ( (UnsafeRawPointer?) -> Swift.Void)!, copyDescription: ( (UnsafeRawPointer?) -> Unmanaged<CFString>?)!)](https://developer.apple.com/documentation/corefoundation/cfmachportcontext/1780503-init)Added [CFMessagePortContext.init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ( (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release: ( (UnsafeRawPointer?) -> Swift.Void)!, copyDescription: ( (UnsafeRawPointer?) -> Unmanaged<CFString>?)!)](https://developer.apple.com/documentation/corefoundation/cfmessageportcontext/1780493-init)Added [CFNotificationName [struct]](https://developer.apple.com/documentation/corefoundation/cfnotificationname)Added [CFNotificationName.init(_: CFString)](https://developer.apple.com/documentation/corefoundation/cfnotificationname/1924277-init)Added [CFNotificationName.init(rawValue: CFString)](https://developer.apple.com/documentation/corefoundation/cfnotificationname/1780500-init)Added [CFNumberFormatterKey [struct]](https://developer.apple.com/documentation/corefoundation/cfnumberformatterkey)Added [CFNumberFormatterKey.init(rawValue: CFString)](https://developer.apple.com/documentation/corefoundation/cfnumberformatterkey/1780511-init)Added [CFRunLoopMode [struct]](https://developer.apple.com/documentation/corefoundation/cfrunloopmode)Added [CFRunLoopMode.init(_: CFString)](https://developer.apple.com/documentation/corefoundation/cfrunloopmode/1924275-init)Added [CFRunLoopMode.init(rawValue: CFString)](https://developer.apple.com/documentation/corefoundation/cfrunloopmode/1780498-init)Added [CFRunLoopObserverContext.init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ( (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release: ( (UnsafeRawPointer?) -> Swift.Void)!, copyDescription: ( (UnsafeRawPointer?) -> Unmanaged<CFString>?)!)](https://developer.apple.com/documentation/corefoundation/cfrunloopobservercontext/1780510-init)Added [CFRunLoopSourceContext.init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ( (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release: ( (UnsafeRawPointer?) -> Swift.Void)!, copyDescription: ( (UnsafeRawPointer?) -> Unmanaged<CFString>?)!, equal: ( (UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!, hash: ( (UnsafeRawPointer?) -> CFHashCode)!, schedule: ( (UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Swift.Void)!, cancel: ( (UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Swift.Void)!, perform: ( (UnsafeMutableRawPointer?) -> Swift.Void)!)](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext/1780501-init)Added [CFRunLoopSourceContext1.init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ( (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release: ( (UnsafeRawPointer?) -> Swift.Void)!, copyDescription: ( (UnsafeRawPointer?) -> Unmanaged<CFString>?)!, equal: ( (UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!, hash: ( (UnsafeRawPointer?) -> CFHashCode)!, getPort: ( (UnsafeMutableRawPointer?) -> mach_port_t)!, perform: ( (UnsafeMutableRawPointer?, CFIndex, CFAllocator?, UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!)](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1/1780506-init)Added [CFRunLoopTimerContext.init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ( (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release: ( (UnsafeRawPointer?) -> Swift.Void)!, copyDescription: ( (UnsafeRawPointer?) -> Unmanaged<CFString>?)!)](https://developer.apple.com/documentation/corefoundation/cfrunlooptimercontext/1780492-init)Added [CFSetCallBacks.init(version: CFIndex, retain: CoreFoundation.CFSetRetainCallBack!, release: CoreFoundation.CFSetReleaseCallBack!, copyDescription: CoreFoundation.CFSetCopyDescriptionCallBack!, equal: CoreFoundation.CFSetEqualCallBack!, hash: CoreFoundation.CFSetHashCallBack!)](https://developer.apple.com/documentation/corefoundation/cfsetcallbacks/1780512-init)Added [CFSocketContext.init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ( (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release: ( (UnsafeRawPointer?) -> Swift.Void)!, copyDescription: ( (UnsafeRawPointer?) -> Unmanaged<CFString>?)!)](https://developer.apple.com/documentation/corefoundation/cfsocketcontext/1780502-init)Added [CFStreamClientContext.init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ( (UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!, release: ( (UnsafeMutableRawPointer?) -> Swift.Void)!, copyDescription: ( (UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!)](https://developer.apple.com/documentation/corefoundation/cfstreamclientcontext/1780497-init)Added [CFStreamPropertyKey [struct]](https://developer.apple.com/documentation/corefoundation/cfstreampropertykey)Added [CFStreamPropertyKey.init(_: CFString)](https://developer.apple.com/documentation/corefoundation/cfstreampropertykey/1924276-init)Added [CFStreamPropertyKey.init(rawValue: CFString)](https://developer.apple.com/documentation/corefoundation/cfstreampropertykey/1780496-init)Added [CFStringInlineBuffer.init(buffer: (UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar), theString: Unmanaged<CFString>!, directUniCharBuffer: UnsafePointer<UniChar>!, directCStringBuffer: UnsafePointer<Int8>!, rangeToBuffer: CFRange, bufferedRangeStart: CFIndex, bufferedRangeEnd: CFIndex)](https://developer.apple.com/documentation/corefoundation/cfstringinlinebuffer/1542752-init)Added [CFTreeContext.init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: CoreFoundation.CFTreeRetainCallBack!, release: CoreFoundation.CFTreeReleaseCallBack!, copyDescription: CoreFoundation.CFTreeCopyDescriptionCallBack!)](https://developer.apple.com/documentation/corefoundation/cftreecontext/1780505-init)Added [CFDateFormatterCreateISO8601Formatter(_: CFAllocator!, _: CFISO8601DateFormatOptions) -> CFDateFormatter!](https://developer.apple.com/documentation/corefoundation/1643402-cfdateformattercreateiso8601form)Added [CFErrorDomain](https://developer.apple.com/documentation/corefoundation/cferrordomain)Added [kCFCoreFoundationVersionNumber10_10_4](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_10_4)Added [kCFCoreFoundationVersionNumber10_10_5](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_10_5)Added [kCFCoreFoundationVersionNumber10_10_Max](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_10_max)Added [kCFCoreFoundationVersionNumber10_11](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_11)Added [kCFCoreFoundationVersionNumber10_11_1](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_11_1)Added [kCFCoreFoundationVersionNumber10_11_2](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_11_2)Added [kCFCoreFoundationVersionNumber10_11_3](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_11_3)Added [kCFCoreFoundationVersionNumber10_11_4](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_11_4)Added [kCFCoreFoundationVersionNumber10_11_Max](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_11_max)Added [kCFCoreFoundationVersionNumber_iOS_8_x_Max](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber_ios_8_x_max)Added [kCFCoreFoundationVersionNumber_iOS_9_0](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber_ios_9_0)Added [kCFCoreFoundationVersionNumber_iOS_9_1](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber_ios_9_1)Added [kCFCoreFoundationVersionNumber_iOS_9_2](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber_ios_9_2)Added [kCFCoreFoundationVersionNumber_iOS_9_3](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber_ios_9_3)Added [kCFCoreFoundationVersionNumber_iOS_9_4](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber_ios_9_4)Added [kCFCoreFoundationVersionNumber_iOS_9_x_Max](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber_ios_9_x_max)Added [kCFURLCanonicalPathKey](https://developer.apple.com/documentation/corefoundation/kcfurlcanonicalpathkey)Added [kCFURLVolumeIsEncryptedKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeisencryptedkey)Added [kCFURLVolumeIsRootFileSystemKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeisrootfilesystemkey)Added [kCFURLVolumeSupportsCompressionKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportscompressionkey)Added [kCFURLVolumeSupportsExclusiveRenamingKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportsexclusiverenamingkey)Added [kCFURLVolumeSupportsFileCloningKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportsfilecloningkey)Added [kCFURLVolumeSupportsSwapRenamingKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportsswaprenamingkey)Modified [CFAllocatorContext [struct]](https://developer.apple.com/documentation/corefoundation/cfallocatorcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFAllocatorContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack!     var release: CFAllocatorReleaseCallBack!     var copyDescription: CFAllocatorCopyDescriptionCallBack!     var allocate: CFAllocatorAllocateCallBack!     var reallocate: CFAllocatorReallocateCallBack!     var deallocate: CFAllocatorDeallocateCallBack!     var preferredSize: CFAllocatorPreferredSizeCallBack!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFAllocatorRetainCallBack!, release release: CFAllocatorReleaseCallBack!, copyDescription copyDescription: CFAllocatorCopyDescriptionCallBack!, allocate allocate: CFAllocatorAllocateCallBack!, reallocate reallocate: CFAllocatorReallocateCallBack!, deallocate deallocate: CFAllocatorDeallocateCallBack!, preferredSize preferredSize: CFAllocatorPreferredSizeCallBack!) } ``` |
| To | ``` struct CFAllocatorContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: CoreFoundation.CFAllocatorRetainCallBack!     var release: CoreFoundation.CFAllocatorReleaseCallBack!     var copyDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack!     var allocate: CoreFoundation.CFAllocatorAllocateCallBack!     var reallocate: CoreFoundation.CFAllocatorReallocateCallBack!     var deallocate: CoreFoundation.CFAllocatorDeallocateCallBack!     var preferredSize: CoreFoundation.CFAllocatorPreferredSizeCallBack!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: CoreFoundation.CFAllocatorRetainCallBack!, release release: CoreFoundation.CFAllocatorReleaseCallBack!, copyDescription copyDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack!, allocate allocate: CoreFoundation.CFAllocatorAllocateCallBack!, reallocate reallocate: CoreFoundation.CFAllocatorReallocateCallBack!, deallocate deallocate: CoreFoundation.CFAllocatorDeallocateCallBack!, preferredSize preferredSize: CoreFoundation.CFAllocatorPreferredSizeCallBack!) } ``` |

Modified [CFAllocatorContext.allocate](https://developer.apple.com/documentation/corefoundation/cfallocatorcontext/1521286-allocate)

|  | Declaration |
| --- | --- |
| From | ``` var allocate: CFAllocatorAllocateCallBack! ``` |
| To | ``` var allocate: CoreFoundation.CFAllocatorAllocateCallBack! ``` |

Modified [CFAllocatorContext.copyDescription](https://developer.apple.com/documentation/corefoundation/cfallocatorcontext/1521301-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFAllocatorCopyDescriptionCallBack! ``` |
| To | ``` var copyDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack! ``` |

Modified [CFAllocatorContext.deallocate](https://developer.apple.com/documentation/corefoundation/cfallocatorcontext/1521339-deallocate)

|  | Declaration |
| --- | --- |
| From | ``` var deallocate: CFAllocatorDeallocateCallBack! ``` |
| To | ``` var deallocate: CoreFoundation.CFAllocatorDeallocateCallBack! ``` |

Modified [CFAllocatorContext.info](https://developer.apple.com/documentation/corefoundation/cfallocatorcontext/1521186-info)

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafeMutablePointer<Void> ``` |
| To | ``` var info: UnsafeMutableRawPointer! ``` |

Modified [CFAllocatorContext.preferredSize](https://developer.apple.com/documentation/corefoundation/cfallocatorcontext/1521307-preferredsize)

|  | Declaration |
| --- | --- |
| From | ``` var preferredSize: CFAllocatorPreferredSizeCallBack! ``` |
| To | ``` var preferredSize: CoreFoundation.CFAllocatorPreferredSizeCallBack! ``` |

Modified [CFAllocatorContext.reallocate](https://developer.apple.com/documentation/corefoundation/cfallocatorcontext/1521222-reallocate)

|  | Declaration |
| --- | --- |
| From | ``` var reallocate: CFAllocatorReallocateCallBack! ``` |
| To | ``` var reallocate: CoreFoundation.CFAllocatorReallocateCallBack! ``` |

Modified [CFAllocatorContext.release](https://developer.apple.com/documentation/corefoundation/cfallocatorcontext/1521148-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFAllocatorReleaseCallBack! ``` |
| To | ``` var release: CoreFoundation.CFAllocatorReleaseCallBack! ``` |

Modified [CFAllocatorContext.retain](https://developer.apple.com/documentation/corefoundation/cfallocatorcontext/1521359-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFAllocatorRetainCallBack! ``` |
| To | ``` var retain: CoreFoundation.CFAllocatorRetainCallBack! ``` |

Modified [CFArrayCallBacks [struct]](https://developer.apple.com/documentation/corefoundation/cfarraycallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CFArrayCallBacks {     var version: CFIndex     var retain: CFArrayRetainCallBack!     var release: CFArrayReleaseCallBack!     var copyDescription: CFArrayCopyDescriptionCallBack!     var equal: CFArrayEqualCallBack!     init()     init(version version: CFIndex, retain retain: CFArrayRetainCallBack!, release release: CFArrayReleaseCallBack!, copyDescription copyDescription: CFArrayCopyDescriptionCallBack!, equal equal: CFArrayEqualCallBack!) } ``` |
| To | ``` struct CFArrayCallBacks {     var version: CFIndex     var retain: CoreFoundation.CFArrayRetainCallBack!     var release: CoreFoundation.CFArrayReleaseCallBack!     var copyDescription: CoreFoundation.CFArrayCopyDescriptionCallBack!     var equal: CoreFoundation.CFArrayEqualCallBack!     init()     init(version version: CFIndex, retain retain: CoreFoundation.CFArrayRetainCallBack!, release release: CoreFoundation.CFArrayReleaseCallBack!, copyDescription copyDescription: CoreFoundation.CFArrayCopyDescriptionCallBack!, equal equal: CoreFoundation.CFArrayEqualCallBack!) } ``` |

Modified [CFArrayCallBacks.copyDescription](https://developer.apple.com/documentation/corefoundation/cfarraycallbacks/1388780-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFArrayCopyDescriptionCallBack! ``` |
| To | ``` var copyDescription: CoreFoundation.CFArrayCopyDescriptionCallBack! ``` |

Modified [CFArrayCallBacks.equal](https://developer.apple.com/documentation/corefoundation/cfarraycallbacks/1388790-equal)

|  | Declaration |
| --- | --- |
| From | ``` var equal: CFArrayEqualCallBack! ``` |
| To | ``` var equal: CoreFoundation.CFArrayEqualCallBack! ``` |

Modified [CFArrayCallBacks.release](https://developer.apple.com/documentation/corefoundation/cfarraycallbacks/1388743-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFArrayReleaseCallBack! ``` |
| To | ``` var release: CoreFoundation.CFArrayReleaseCallBack! ``` |

Modified [CFArrayCallBacks.retain](https://developer.apple.com/documentation/corefoundation/cfarraycallbacks/1388784-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFArrayRetainCallBack! ``` |
| To | ``` var retain: CoreFoundation.CFArrayRetainCallBack! ``` |

Modified [CFBagCallBacks [struct]](https://developer.apple.com/documentation/corefoundation/cfbagcallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CFBagCallBacks {     var version: CFIndex     var retain: CFBagRetainCallBack!     var release: CFBagReleaseCallBack!     var copyDescription: CFBagCopyDescriptionCallBack!     var equal: CFBagEqualCallBack!     var hash: CFBagHashCallBack!     init()     init(version version: CFIndex, retain retain: CFBagRetainCallBack!, release release: CFBagReleaseCallBack!, copyDescription copyDescription: CFBagCopyDescriptionCallBack!, equal equal: CFBagEqualCallBack!, hash hash: CFBagHashCallBack!) } ``` |
| To | ``` struct CFBagCallBacks {     var version: CFIndex     var retain: CoreFoundation.CFBagRetainCallBack!     var release: CoreFoundation.CFBagReleaseCallBack!     var copyDescription: CoreFoundation.CFBagCopyDescriptionCallBack!     var equal: CoreFoundation.CFBagEqualCallBack!     var hash: CoreFoundation.CFBagHashCallBack!     init()     init(version version: CFIndex, retain retain: CoreFoundation.CFBagRetainCallBack!, release release: CoreFoundation.CFBagReleaseCallBack!, copyDescription copyDescription: CoreFoundation.CFBagCopyDescriptionCallBack!, equal equal: CoreFoundation.CFBagEqualCallBack!, hash hash: CoreFoundation.CFBagHashCallBack!) } ``` |

Modified [CFBagCallBacks.copyDescription](https://developer.apple.com/documentation/corefoundation/cfbagcallbacks/1469256-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFBagCopyDescriptionCallBack! ``` |
| To | ``` var copyDescription: CoreFoundation.CFBagCopyDescriptionCallBack! ``` |

Modified [CFBagCallBacks.equal](https://developer.apple.com/documentation/corefoundation/cfbagcallbacks/1469316-equal)

|  | Declaration |
| --- | --- |
| From | ``` var equal: CFBagEqualCallBack! ``` |
| To | ``` var equal: CoreFoundation.CFBagEqualCallBack! ``` |

Modified [CFBagCallBacks.hash](https://developer.apple.com/documentation/corefoundation/cfbagcallbacks/1469293-hash)

|  | Declaration |
| --- | --- |
| From | ``` var hash: CFBagHashCallBack! ``` |
| To | ``` var hash: CoreFoundation.CFBagHashCallBack! ``` |

Modified [CFBagCallBacks.release](https://developer.apple.com/documentation/corefoundation/cfbagcallbacks/1469307-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFBagReleaseCallBack! ``` |
| To | ``` var release: CoreFoundation.CFBagReleaseCallBack! ``` |

Modified [CFBagCallBacks.retain](https://developer.apple.com/documentation/corefoundation/cfbagcallbacks/1469278-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFBagRetainCallBack! ``` |
| To | ``` var retain: CoreFoundation.CFBagRetainCallBack! ``` |

Modified [CFBinaryHeapCallBacks [struct]](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CFBinaryHeapCallBacks {     var version: CFIndex     var retain: ((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)!     var release: ((CFAllocator!, UnsafePointer<Void>) -> Void)!     var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!     var compare: ((UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> CFComparisonResult)!     init()     init(version version: CFIndex, retain retain: ((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)!, release release: ((CFAllocator!, UnsafePointer<Void>) -> Void)!, copyDescription copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!, compare compare: ((UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> CFComparisonResult)!) } ``` |
| To | ``` struct CFBinaryHeapCallBacks {     var version: CFIndex     var retain: ((CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((CFAllocator?, UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     var compare: ((UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> CFComparisonResult)!     init()     init(version version: CFIndex, retain retain: (@escaping (CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (CFAllocator?, UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!, compare compare: (@escaping (UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> CFComparisonResult)!) } ``` |

Modified [CFBinaryHeapCallBacks.compare](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcallbacks/1509307-compare)

|  | Declaration |
| --- | --- |
| From | ``` var compare: ((UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> CFComparisonResult)! ``` |
| To | ``` var compare: ((UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> CFComparisonResult)! ``` |

Modified [CFBinaryHeapCallBacks.copyDescription](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcallbacks/1509329-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)! ``` |
| To | ``` var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)! ``` |

Modified [CFBinaryHeapCallBacks.release](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcallbacks/1509326-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: ((CFAllocator!, UnsafePointer<Void>) -> Void)! ``` |
| To | ``` var release: ((CFAllocator?, UnsafeRawPointer?) -> Swift.Void)! ``` |

Modified [CFBinaryHeapCallBacks.retain](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcallbacks/1509294-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: ((CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void>)! ``` |
| To | ``` var retain: ((CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer?)! ``` |

Modified [CFBinaryHeapCompareContext [struct]](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcomparecontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFBinaryHeapCompareContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!     var release: ((UnsafePointer<Void>) -> Void)!     var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release release: ((UnsafePointer<Void>) -> Void)!, copyDescription copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!) } ``` |
| To | ``` struct CFBinaryHeapCompareContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!) } ``` |

Modified [CFBinaryHeapCompareContext.copyDescription](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcomparecontext/1509311-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)! ``` |
| To | ``` var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)! ``` |

Modified [CFBinaryHeapCompareContext.info](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcomparecontext/1509315-info)

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafeMutablePointer<Void> ``` |
| To | ``` var info: UnsafeMutableRawPointer! ``` |

Modified [CFBinaryHeapCompareContext.release](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcomparecontext/1509299-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: ((UnsafePointer<Void>) -> Void)! ``` |
| To | ``` var release: ((UnsafeRawPointer?) -> Swift.Void)! ``` |

Modified [CFBinaryHeapCompareContext.retain](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcomparecontext/1509313-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)! ``` |
| To | ``` var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)! ``` |

Modified [CFCalendarIdentifier.buddhistCalendar](https://developer.apple.com/documentation/corefoundation/kcfbuddhistcalendar)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFBuddhistCalendar | ``` let kCFBuddhistCalendar: CFString! ``` |
| To | buddhistCalendar | ``` static let buddhistCalendar: CFCalendarIdentifier! ``` |

Modified [CFCalendarIdentifier.cfiso8601Calendar](https://developer.apple.com/documentation/corefoundation/kcfiso8601calendar)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFISO8601Calendar | ``` let kCFISO8601Calendar: CFString! ``` |
| To | cfiso8601Calendar | ``` static let cfiso8601Calendar: CFCalendarIdentifier! ``` |

Modified [CFCalendarIdentifier.chineseCalendar](https://developer.apple.com/documentation/corefoundation/cfcalendaridentifier/1542253-chinesecalendar)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFChineseCalendar | ``` let kCFChineseCalendar: CFString! ``` |
| To | chineseCalendar | ``` static let chineseCalendar: CFCalendarIdentifier! ``` |

Modified [CFCalendarIdentifier.gregorianCalendar](https://developer.apple.com/documentation/corefoundation/kcfgregoriancalendar)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFGregorianCalendar | ``` let kCFGregorianCalendar: CFString! ``` |
| To | gregorianCalendar | ``` static let gregorianCalendar: CFCalendarIdentifier! ``` |

Modified [CFCalendarIdentifier.hebrewCalendar](https://developer.apple.com/documentation/corefoundation/kcfhebrewcalendar)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFHebrewCalendar | ``` let kCFHebrewCalendar: CFString! ``` |
| To | hebrewCalendar | ``` static let hebrewCalendar: CFCalendarIdentifier! ``` |

Modified [CFCalendarIdentifier.indianCalendar](https://developer.apple.com/documentation/corefoundation/kcfindiancalendar)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFIndianCalendar | ``` let kCFIndianCalendar: CFString! ``` |
| To | indianCalendar | ``` static let indianCalendar: CFCalendarIdentifier! ``` |

Modified [CFCalendarIdentifier.islamicCalendar](https://developer.apple.com/documentation/corefoundation/cfcalendaridentifier/1542733-islamiccalendar)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFIslamicCalendar | ``` let kCFIslamicCalendar: CFString! ``` |
| To | islamicCalendar | ``` static let islamicCalendar: CFCalendarIdentifier! ``` |

Modified [CFCalendarIdentifier.islamicCivilCalendar](https://developer.apple.com/documentation/corefoundation/kcfislamiccivilcalendar)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFIslamicCivilCalendar | ``` let kCFIslamicCivilCalendar: CFString! ``` |
| To | islamicCivilCalendar | ``` static let islamicCivilCalendar: CFCalendarIdentifier! ``` |

Modified [CFCalendarIdentifier.islamicTabularCalendar](https://developer.apple.com/documentation/corefoundation/kcfislamictabularcalendar)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFIslamicTabularCalendar | ``` let kCFIslamicTabularCalendar: CFString! ``` |
| To | islamicTabularCalendar | ``` static let islamicTabularCalendar: CFCalendarIdentifier! ``` |

Modified [CFCalendarIdentifier.islamicUmmAlQuraCalendar](https://developer.apple.com/documentation/corefoundation/cfcalendaridentifier/1543123-islamicummalquracalendar)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFIslamicUmmAlQuraCalendar | ``` let kCFIslamicUmmAlQuraCalendar: CFString! ``` |
| To | islamicUmmAlQuraCalendar | ``` static let islamicUmmAlQuraCalendar: CFCalendarIdentifier! ``` |

Modified [CFCalendarIdentifier.japaneseCalendar](https://developer.apple.com/documentation/corefoundation/cfcalendaridentifier/1543390-japanesecalendar)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFJapaneseCalendar | ``` let kCFJapaneseCalendar: CFString! ``` |
| To | japaneseCalendar | ``` static let japaneseCalendar: CFCalendarIdentifier! ``` |

Modified [CFCalendarIdentifier.persianCalendar](https://developer.apple.com/documentation/corefoundation/kcfpersiancalendar)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFPersianCalendar | ``` let kCFPersianCalendar: CFString! ``` |
| To | persianCalendar | ``` static let persianCalendar: CFCalendarIdentifier! ``` |

Modified [CFCalendarIdentifier.republicOfChinaCalendar](https://developer.apple.com/documentation/corefoundation/cfcalendaridentifier/1541531-republicofchinacalendar)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFRepublicOfChinaCalendar | ``` let kCFRepublicOfChinaCalendar: CFString! ``` |
| To | republicOfChinaCalendar | ``` static let republicOfChinaCalendar: CFCalendarIdentifier! ``` |

Modified [CFCalendarUnit [struct]](https://developer.apple.com/documentation/corefoundation/cfcalendarunit)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFCalendarUnit : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var Era: CFCalendarUnit { get }     static var Year: CFCalendarUnit { get }     static var Month: CFCalendarUnit { get }     static var Day: CFCalendarUnit { get }     static var Hour: CFCalendarUnit { get }     static var Minute: CFCalendarUnit { get }     static var Second: CFCalendarUnit { get }     static var Week: CFCalendarUnit { get }     static var Weekday: CFCalendarUnit { get }     static var WeekdayOrdinal: CFCalendarUnit { get }     static var Quarter: CFCalendarUnit { get }     static var WeekOfMonth: CFCalendarUnit { get }     static var WeekOfYear: CFCalendarUnit { get }     static var YearForWeekOfYear: CFCalendarUnit { get } } ``` | OptionSetType |
| To | ``` struct CFCalendarUnit : OptionSet {     init(rawValue rawValue: CFOptionFlags)     static var era: CFCalendarUnit { get }     static var year: CFCalendarUnit { get }     static var month: CFCalendarUnit { get }     static var day: CFCalendarUnit { get }     static var hour: CFCalendarUnit { get }     static var minute: CFCalendarUnit { get }     static var second: CFCalendarUnit { get }     static var week: CFCalendarUnit { get }     static var weekday: CFCalendarUnit { get }     static var weekdayOrdinal: CFCalendarUnit { get }     static var quarter: CFCalendarUnit { get }     static var weekOfMonth: CFCalendarUnit { get }     static var weekOfYear: CFCalendarUnit { get }     static var yearForWeekOfYear: CFCalendarUnit { get }     func intersect(_ other: CFCalendarUnit) -> CFCalendarUnit     func exclusiveOr(_ other: CFCalendarUnit) -> CFCalendarUnit     mutating func unionInPlace(_ other: CFCalendarUnit)     mutating func intersectInPlace(_ other: CFCalendarUnit)     mutating func exclusiveOrInPlace(_ other: CFCalendarUnit)     func isSubsetOf(_ other: CFCalendarUnit) -> Bool     func isDisjointWith(_ other: CFCalendarUnit) -> Bool     func isSupersetOf(_ other: CFCalendarUnit) -> Bool     mutating func subtractInPlace(_ other: CFCalendarUnit)     func isStrictSupersetOf(_ other: CFCalendarUnit) -> Bool     func isStrictSubsetOf(_ other: CFCalendarUnit) -> Bool } extension CFCalendarUnit {     func union(_ other: CFCalendarUnit) -> CFCalendarUnit     func intersection(_ other: CFCalendarUnit) -> CFCalendarUnit     func symmetricDifference(_ other: CFCalendarUnit) -> CFCalendarUnit } extension CFCalendarUnit {     func contains(_ member: CFCalendarUnit) -> Bool     mutating func insert(_ newMember: CFCalendarUnit) -> (inserted: Bool, memberAfterInsert: CFCalendarUnit)     mutating func remove(_ member: CFCalendarUnit) -> CFCalendarUnit?     mutating func update(with newMember: CFCalendarUnit) -> CFCalendarUnit? } extension CFCalendarUnit {     convenience init()     mutating func formUnion(_ other: CFCalendarUnit)     mutating func formIntersection(_ other: CFCalendarUnit)     mutating func formSymmetricDifference(_ other: CFCalendarUnit) } extension CFCalendarUnit {     convenience init<S : Sequence where S.Iterator.Element == CFCalendarUnit>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CFCalendarUnit...)     mutating func subtract(_ other: CFCalendarUnit)     func isSubset(of other: CFCalendarUnit) -> Bool     func isSuperset(of other: CFCalendarUnit) -> Bool     func isDisjoint(with other: CFCalendarUnit) -> Bool     func subtracting(_ other: CFCalendarUnit) -> CFCalendarUnit     var isEmpty: Bool { get }     func isStrictSuperset(of other: CFCalendarUnit) -> Bool     func isStrictSubset(of other: CFCalendarUnit) -> Bool } ``` | OptionSet |

Modified [CFCalendarUnit.day](https://developer.apple.com/documentation/corefoundation/cfcalendarunit/1533502-day)

|  | Declaration |
| --- | --- |
| From | ``` static var Day: CFCalendarUnit { get } ``` |
| To | ``` static var day: CFCalendarUnit { get } ``` |

Modified [CFCalendarUnit.era](https://developer.apple.com/documentation/corefoundation/cfcalendarunit/1533504-era)

|  | Declaration |
| --- | --- |
| From | ``` static var Era: CFCalendarUnit { get } ``` |
| To | ``` static var era: CFCalendarUnit { get } ``` |

Modified [CFCalendarUnit.hour](https://developer.apple.com/documentation/corefoundation/cfcalendarunit/kcfcalendarunithour)

|  | Declaration |
| --- | --- |
| From | ``` static var Hour: CFCalendarUnit { get } ``` |
| To | ``` static var hour: CFCalendarUnit { get } ``` |

Modified [CFCalendarUnit.minute](https://developer.apple.com/documentation/corefoundation/cfcalendarunit/kcfcalendarunitminute)

|  | Declaration |
| --- | --- |
| From | ``` static var Minute: CFCalendarUnit { get } ``` |
| To | ``` static var minute: CFCalendarUnit { get } ``` |

Modified [CFCalendarUnit.month](https://developer.apple.com/documentation/corefoundation/cfcalendarunit/1533484-month)

|  | Declaration |
| --- | --- |
| From | ``` static var Month: CFCalendarUnit { get } ``` |
| To | ``` static var month: CFCalendarUnit { get } ``` |

Modified [CFCalendarUnit.quarter](https://developer.apple.com/documentation/corefoundation/cfcalendarunit/1533474-quarter)

|  | Declaration |
| --- | --- |
| From | ``` static var Quarter: CFCalendarUnit { get } ``` |
| To | ``` static var quarter: CFCalendarUnit { get } ``` |

Modified [CFCalendarUnit.second](https://developer.apple.com/documentation/corefoundation/cfcalendarunit/kcfcalendarunitsecond)

|  | Declaration |
| --- | --- |
| From | ``` static var Second: CFCalendarUnit { get } ``` |
| To | ``` static var second: CFCalendarUnit { get } ``` |

Modified [CFCalendarUnit.week](https://developer.apple.com/documentation/corefoundation/cfcalendarunit/1533481-week)

|  | Declaration |
| --- | --- |
| From | ``` static var Week: CFCalendarUnit { get } ``` |
| To | ``` static var week: CFCalendarUnit { get } ``` |

Modified [CFCalendarUnit.weekday](https://developer.apple.com/documentation/corefoundation/cfcalendarunit/kcfcalendarunitweekday)

|  | Declaration |
| --- | --- |
| From | ``` static var Weekday: CFCalendarUnit { get } ``` |
| To | ``` static var weekday: CFCalendarUnit { get } ``` |

Modified [CFCalendarUnit.weekdayOrdinal](https://developer.apple.com/documentation/corefoundation/cfcalendarunit/1533493-weekdayordinal)

|  | Declaration |
| --- | --- |
| From | ``` static var WeekdayOrdinal: CFCalendarUnit { get } ``` |
| To | ``` static var weekdayOrdinal: CFCalendarUnit { get } ``` |

Modified [CFCalendarUnit.weekOfMonth](https://developer.apple.com/documentation/corefoundation/cfcalendarunit/1533518-weekofmonth)

|  | Declaration |
| --- | --- |
| From | ``` static var WeekOfMonth: CFCalendarUnit { get } ``` |
| To | ``` static var weekOfMonth: CFCalendarUnit { get } ``` |

Modified [CFCalendarUnit.weekOfYear](https://developer.apple.com/documentation/corefoundation/cfcalendarunit/1533486-weekofyear)

|  | Declaration |
| --- | --- |
| From | ``` static var WeekOfYear: CFCalendarUnit { get } ``` |
| To | ``` static var weekOfYear: CFCalendarUnit { get } ``` |

Modified [CFCalendarUnit.year](https://developer.apple.com/documentation/corefoundation/cfcalendarunit/kcfcalendarunityear)

|  | Declaration |
| --- | --- |
| From | ``` static var Year: CFCalendarUnit { get } ``` |
| To | ``` static var year: CFCalendarUnit { get } ``` |

Modified [CFCalendarUnit.yearForWeekOfYear](https://developer.apple.com/documentation/corefoundation/cfcalendarunit/kcfcalendarunityearforweekofyear)

|  | Declaration |
| --- | --- |
| From | ``` static var YearForWeekOfYear: CFCalendarUnit { get } ``` |
| To | ``` static var yearForWeekOfYear: CFCalendarUnit { get } ``` |

Modified [CFCharacterSetPredefinedSet [enum]](https://developer.apple.com/documentation/corefoundation/cfcharactersetpredefinedset)

|  | Declaration |
| --- | --- |
| From | ``` enum CFCharacterSetPredefinedSet : CFIndex {     case Control     case Whitespace     case WhitespaceAndNewline     case DecimalDigit     case Letter     case LowercaseLetter     case UppercaseLetter     case NonBase     case Decomposable     case AlphaNumeric     case Punctuation     case CapitalizedLetter     case Symbol     case Newline     case Illegal } ``` |
| To | ``` enum CFCharacterSetPredefinedSet : CFIndex {     case control     case whitespace     case whitespaceAndNewline     case decimalDigit     case letter     case lowercaseLetter     case uppercaseLetter     case nonBase     case decomposable     case alphaNumeric     case punctuation     case capitalizedLetter     case symbol     case newline     case illegal } ``` |

Modified [CFCharacterSetPredefinedSet.alphaNumeric](https://developer.apple.com/documentation/corefoundation/cfcharactersetpredefinedset/alphanumeric)

|  | Declaration |
| --- | --- |
| From | ``` case AlphaNumeric ``` |
| To | ``` case alphaNumeric ``` |

Modified [CFCharacterSetPredefinedSet.capitalizedLetter](https://developer.apple.com/documentation/corefoundation/cfcharactersetpredefinedset/kcfcharactersetcapitalizedletter)

|  | Declaration |
| --- | --- |
| From | ``` case CapitalizedLetter ``` |
| To | ``` case capitalizedLetter ``` |

Modified [CFCharacterSetPredefinedSet.control](https://developer.apple.com/documentation/corefoundation/cfcharactersetpredefinedset/kcfcharactersetcontrol)

|  | Declaration |
| --- | --- |
| From | ``` case Control ``` |
| To | ``` case control ``` |

Modified [CFCharacterSetPredefinedSet.decimalDigit](https://developer.apple.com/documentation/corefoundation/cfcharactersetpredefinedset/decimaldigit)

|  | Declaration |
| --- | --- |
| From | ``` case DecimalDigit ``` |
| To | ``` case decimalDigit ``` |

Modified [CFCharacterSetPredefinedSet.decomposable](https://developer.apple.com/documentation/corefoundation/cfcharactersetpredefinedset/decomposable)

|  | Declaration |
| --- | --- |
| From | ``` case Decomposable ``` |
| To | ``` case decomposable ``` |

Modified [CFCharacterSetPredefinedSet.illegal](https://developer.apple.com/documentation/corefoundation/cfcharactersetpredefinedset/kcfcharactersetillegal)

|  | Declaration |
| --- | --- |
| From | ``` case Illegal ``` |
| To | ``` case illegal ``` |

Modified [CFCharacterSetPredefinedSet.letter](https://developer.apple.com/documentation/corefoundation/cfcharactersetpredefinedset/kcfcharactersetletter)

|  | Declaration |
| --- | --- |
| From | ``` case Letter ``` |
| To | ``` case letter ``` |

Modified [CFCharacterSetPredefinedSet.lowercaseLetter](https://developer.apple.com/documentation/corefoundation/cfcharactersetpredefinedset/lowercaseletter)

|  | Declaration |
| --- | --- |
| From | ``` case LowercaseLetter ``` |
| To | ``` case lowercaseLetter ``` |

Modified [CFCharacterSetPredefinedSet.newline](https://developer.apple.com/documentation/corefoundation/cfcharactersetpredefinedset/newline)

|  | Declaration |
| --- | --- |
| From | ``` case Newline ``` |
| To | ``` case newline ``` |

Modified [CFCharacterSetPredefinedSet.nonBase](https://developer.apple.com/documentation/corefoundation/cfcharactersetpredefinedset/kcfcharactersetnonbase)

|  | Declaration |
| --- | --- |
| From | ``` case NonBase ``` |
| To | ``` case nonBase ``` |

Modified [CFCharacterSetPredefinedSet.punctuation](https://developer.apple.com/documentation/corefoundation/cfcharactersetpredefinedset/punctuation)

|  | Declaration |
| --- | --- |
| From | ``` case Punctuation ``` |
| To | ``` case punctuation ``` |

Modified [CFCharacterSetPredefinedSet.symbol](https://developer.apple.com/documentation/corefoundation/cfcharactersetpredefinedset/kcfcharactersetsymbol)

|  | Declaration |
| --- | --- |
| From | ``` case Symbol ``` |
| To | ``` case symbol ``` |

Modified [CFCharacterSetPredefinedSet.uppercaseLetter](https://developer.apple.com/documentation/corefoundation/cfcharactersetpredefinedset/kcfcharactersetuppercaseletter)

|  | Declaration |
| --- | --- |
| From | ``` case UppercaseLetter ``` |
| To | ``` case uppercaseLetter ``` |

Modified [CFCharacterSetPredefinedSet.whitespace](https://developer.apple.com/documentation/corefoundation/cfcharactersetpredefinedset/kcfcharactersetwhitespace)

|  | Declaration |
| --- | --- |
| From | ``` case Whitespace ``` |
| To | ``` case whitespace ``` |

Modified [CFCharacterSetPredefinedSet.whitespaceAndNewline](https://developer.apple.com/documentation/corefoundation/cfcharactersetpredefinedset/whitespaceandnewline)

|  | Declaration |
| --- | --- |
| From | ``` case WhitespaceAndNewline ``` |
| To | ``` case whitespaceAndNewline ``` |

Modified [CFComparisonResult [enum]](https://developer.apple.com/documentation/corefoundation/cfcomparisonresult)

|  | Declaration |
| --- | --- |
| From | ``` enum CFComparisonResult : CFIndex {     case CompareLessThan     case CompareEqualTo     case CompareGreaterThan } ``` |
| To | ``` enum CFComparisonResult : CFIndex {     case compareLessThan     case compareEqualTo     case compareGreaterThan } ``` |

Modified [CFComparisonResult.compareEqualTo](https://developer.apple.com/documentation/corefoundation/cfcomparisonresult/compareequalto)

|  | Declaration |
| --- | --- |
| From | ``` case CompareEqualTo ``` |
| To | ``` case compareEqualTo ``` |

Modified [CFComparisonResult.compareGreaterThan](https://developer.apple.com/documentation/corefoundation/cfcomparisonresult/kcfcomparegreaterthan)

|  | Declaration |
| --- | --- |
| From | ``` case CompareGreaterThan ``` |
| To | ``` case compareGreaterThan ``` |

Modified [CFComparisonResult.compareLessThan](https://developer.apple.com/documentation/corefoundation/cfcomparisonresult/kcfcomparelessthan)

|  | Declaration |
| --- | --- |
| From | ``` case CompareLessThan ``` |
| To | ``` case compareLessThan ``` |

Modified [CFDataSearchFlags [struct]](https://developer.apple.com/documentation/corefoundation/cfdatasearchflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFDataSearchFlags : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var Backwards: CFDataSearchFlags { get }     static var Anchored: CFDataSearchFlags { get } } ``` | OptionSetType |
| To | ``` struct CFDataSearchFlags : OptionSet {     init(rawValue rawValue: CFOptionFlags)     static var backwards: CFDataSearchFlags { get }     static var anchored: CFDataSearchFlags { get }     func intersect(_ other: CFDataSearchFlags) -> CFDataSearchFlags     func exclusiveOr(_ other: CFDataSearchFlags) -> CFDataSearchFlags     mutating func unionInPlace(_ other: CFDataSearchFlags)     mutating func intersectInPlace(_ other: CFDataSearchFlags)     mutating func exclusiveOrInPlace(_ other: CFDataSearchFlags)     func isSubsetOf(_ other: CFDataSearchFlags) -> Bool     func isDisjointWith(_ other: CFDataSearchFlags) -> Bool     func isSupersetOf(_ other: CFDataSearchFlags) -> Bool     mutating func subtractInPlace(_ other: CFDataSearchFlags)     func isStrictSupersetOf(_ other: CFDataSearchFlags) -> Bool     func isStrictSubsetOf(_ other: CFDataSearchFlags) -> Bool } extension CFDataSearchFlags {     func union(_ other: CFDataSearchFlags) -> CFDataSearchFlags     func intersection(_ other: CFDataSearchFlags) -> CFDataSearchFlags     func symmetricDifference(_ other: CFDataSearchFlags) -> CFDataSearchFlags } extension CFDataSearchFlags {     func contains(_ member: CFDataSearchFlags) -> Bool     mutating func insert(_ newMember: CFDataSearchFlags) -> (inserted: Bool, memberAfterInsert: CFDataSearchFlags)     mutating func remove(_ member: CFDataSearchFlags) -> CFDataSearchFlags?     mutating func update(with newMember: CFDataSearchFlags) -> CFDataSearchFlags? } extension CFDataSearchFlags {     convenience init()     mutating func formUnion(_ other: CFDataSearchFlags)     mutating func formIntersection(_ other: CFDataSearchFlags)     mutating func formSymmetricDifference(_ other: CFDataSearchFlags) } extension CFDataSearchFlags {     convenience init<S : Sequence where S.Iterator.Element == CFDataSearchFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CFDataSearchFlags...)     mutating func subtract(_ other: CFDataSearchFlags)     func isSubset(of other: CFDataSearchFlags) -> Bool     func isSuperset(of other: CFDataSearchFlags) -> Bool     func isDisjoint(with other: CFDataSearchFlags) -> Bool     func subtracting(_ other: CFDataSearchFlags) -> CFDataSearchFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: CFDataSearchFlags) -> Bool     func isStrictSubset(of other: CFDataSearchFlags) -> Bool } ``` | OptionSet |

Modified [CFDataSearchFlags.anchored](https://developer.apple.com/documentation/corefoundation/cfdatasearchflags/1542388-anchored)

|  | Declaration |
| --- | --- |
| From | ``` static var Anchored: CFDataSearchFlags { get } ``` |
| To | ``` static var anchored: CFDataSearchFlags { get } ``` |

Modified [CFDataSearchFlags.backwards](https://developer.apple.com/documentation/corefoundation/cfdatasearchflags/kcfdatasearchbackwards)

|  | Declaration |
| --- | --- |
| From | ``` static var Backwards: CFDataSearchFlags { get } ``` |
| To | ``` static var backwards: CFDataSearchFlags { get } ``` |

Modified [CFDateFormatterKey.amSymbol](https://developer.apple.com/documentation/corefoundation/kcfdateformatteramsymbol)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterAMSymbol | ``` let kCFDateFormatterAMSymbol: CFString! ``` |
| To | amSymbol | ``` static let amSymbol: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.calendar](https://developer.apple.com/documentation/corefoundation/kcfdateformattercalendar)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterCalendar | ``` let kCFDateFormatterCalendar: CFString! ``` |
| To | calendar | ``` static let calendar: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.calendarName](https://developer.apple.com/documentation/corefoundation/kcfdateformattercalendarname)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterCalendarName | ``` let kCFDateFormatterCalendarName: CFString! ``` |
| To | calendarName | ``` static let calendarName: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.defaultDate](https://developer.apple.com/documentation/corefoundation/cfdateformatterkey/1396249-defaultdate)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterDefaultDate | ``` let kCFDateFormatterDefaultDate: CFString! ``` |
| To | defaultDate | ``` static let defaultDate: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.defaultFormat](https://developer.apple.com/documentation/corefoundation/kcfdateformatterdefaultformat)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterDefaultFormat | ``` let kCFDateFormatterDefaultFormat: CFString! ``` |
| To | defaultFormat | ``` static let defaultFormat: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.doesRelativeDateFormattingKey](https://developer.apple.com/documentation/corefoundation/kcfdateformatterdoesrelativedateformattingkey)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterDoesRelativeDateFormattingKey | ``` let kCFDateFormatterDoesRelativeDateFormattingKey: CFString! ``` |
| To | doesRelativeDateFormattingKey | ``` static let doesRelativeDateFormattingKey: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.eraSymbols](https://developer.apple.com/documentation/corefoundation/cfdateformatterkey/1396251-erasymbols)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterEraSymbols | ``` let kCFDateFormatterEraSymbols: CFString! ``` |
| To | eraSymbols | ``` static let eraSymbols: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.gregorianStartDate](https://developer.apple.com/documentation/corefoundation/cfdateformatterkey/1396259-gregorianstartdate)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterGregorianStartDate | ``` let kCFDateFormatterGregorianStartDate: CFString! ``` |
| To | gregorianStartDate | ``` static let gregorianStartDate: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.isLenient](https://developer.apple.com/documentation/corefoundation/kcfdateformatterislenient)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterIsLenient | ``` let kCFDateFormatterIsLenient: CFString! ``` |
| To | isLenient | ``` static let isLenient: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.longEraSymbols](https://developer.apple.com/documentation/corefoundation/kcfdateformatterlongerasymbols)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterLongEraSymbols | ``` let kCFDateFormatterLongEraSymbols: CFString! ``` |
| To | longEraSymbols | ``` static let longEraSymbols: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.monthSymbols](https://developer.apple.com/documentation/corefoundation/kcfdateformattermonthsymbols)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterMonthSymbols | ``` let kCFDateFormatterMonthSymbols: CFString! ``` |
| To | monthSymbols | ``` static let monthSymbols: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.pmSymbol](https://developer.apple.com/documentation/corefoundation/cfdateformatterkey/1396318-pmsymbol)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterPMSymbol | ``` let kCFDateFormatterPMSymbol: CFString! ``` |
| To | pmSymbol | ``` static let pmSymbol: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.quarterSymbols](https://developer.apple.com/documentation/corefoundation/cfdateformatterkey/1396304-quartersymbols)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterQuarterSymbols | ``` let kCFDateFormatterQuarterSymbols: CFString! ``` |
| To | quarterSymbols | ``` static let quarterSymbols: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.shortMonthSymbols](https://developer.apple.com/documentation/corefoundation/kcfdateformattershortmonthsymbols)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterShortMonthSymbols | ``` let kCFDateFormatterShortMonthSymbols: CFString! ``` |
| To | shortMonthSymbols | ``` static let shortMonthSymbols: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.shortQuarterSymbols](https://developer.apple.com/documentation/corefoundation/cfdateformatterkey/1396316-shortquartersymbols)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterShortQuarterSymbols | ``` let kCFDateFormatterShortQuarterSymbols: CFString! ``` |
| To | shortQuarterSymbols | ``` static let shortQuarterSymbols: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.shortStandaloneMonthSymbols](https://developer.apple.com/documentation/corefoundation/cfdateformatterkey/1396292-shortstandalonemonthsymbols)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterShortStandaloneMonthSymbols | ``` let kCFDateFormatterShortStandaloneMonthSymbols: CFString! ``` |
| To | shortStandaloneMonthSymbols | ``` static let shortStandaloneMonthSymbols: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.shortStandaloneQuarterSymbols](https://developer.apple.com/documentation/corefoundation/cfdateformatterkey/1396288-shortstandalonequartersymbols)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterShortStandaloneQuarterSymbols | ``` let kCFDateFormatterShortStandaloneQuarterSymbols: CFString! ``` |
| To | shortStandaloneQuarterSymbols | ``` static let shortStandaloneQuarterSymbols: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.shortStandaloneWeekdaySymbols](https://developer.apple.com/documentation/corefoundation/kcfdateformattershortstandaloneweekdaysymbols)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterShortStandaloneWeekdaySymbols | ``` let kCFDateFormatterShortStandaloneWeekdaySymbols: CFString! ``` |
| To | shortStandaloneWeekdaySymbols | ``` static let shortStandaloneWeekdaySymbols: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.shortWeekdaySymbols](https://developer.apple.com/documentation/corefoundation/cfdateformatterkey/1396267-shortweekdaysymbols)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterShortWeekdaySymbols | ``` let kCFDateFormatterShortWeekdaySymbols: CFString! ``` |
| To | shortWeekdaySymbols | ``` static let shortWeekdaySymbols: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.standaloneMonthSymbols](https://developer.apple.com/documentation/corefoundation/cfdateformatterkey/1396310-standalonemonthsymbols)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterStandaloneMonthSymbols | ``` let kCFDateFormatterStandaloneMonthSymbols: CFString! ``` |
| To | standaloneMonthSymbols | ``` static let standaloneMonthSymbols: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.standaloneQuarterSymbols](https://developer.apple.com/documentation/corefoundation/kcfdateformatterstandalonequartersymbols)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterStandaloneQuarterSymbols | ``` let kCFDateFormatterStandaloneQuarterSymbols: CFString! ``` |
| To | standaloneQuarterSymbols | ``` static let standaloneQuarterSymbols: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.standaloneWeekdaySymbols](https://developer.apple.com/documentation/corefoundation/kcfdateformatterstandaloneweekdaysymbols)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterStandaloneWeekdaySymbols | ``` let kCFDateFormatterStandaloneWeekdaySymbols: CFString! ``` |
| To | standaloneWeekdaySymbols | ``` static let standaloneWeekdaySymbols: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.timeZone](https://developer.apple.com/documentation/corefoundation/cfdateformatterkey/1396314-timezone)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterTimeZone | ``` let kCFDateFormatterTimeZone: CFString! ``` |
| To | timeZone | ``` static let timeZone: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.twoDigitStartDate](https://developer.apple.com/documentation/corefoundation/kcfdateformattertwodigitstartdate)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterTwoDigitStartDate | ``` let kCFDateFormatterTwoDigitStartDate: CFString! ``` |
| To | twoDigitStartDate | ``` static let twoDigitStartDate: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.veryShortMonthSymbols](https://developer.apple.com/documentation/corefoundation/cfdateformatterkey/1396224-veryshortmonthsymbols)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterVeryShortMonthSymbols | ``` let kCFDateFormatterVeryShortMonthSymbols: CFString! ``` |
| To | veryShortMonthSymbols | ``` static let veryShortMonthSymbols: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.veryShortStandaloneMonthSymbols](https://developer.apple.com/documentation/corefoundation/kcfdateformatterveryshortstandalonemonthsymbols)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterVeryShortStandaloneMonthSymbols | ``` let kCFDateFormatterVeryShortStandaloneMonthSymbols: CFString! ``` |
| To | veryShortStandaloneMonthSymbols | ``` static let veryShortStandaloneMonthSymbols: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.veryShortStandaloneWeekdaySymbols](https://developer.apple.com/documentation/corefoundation/cfdateformatterkey/1396286-veryshortstandaloneweekdaysymbol)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterVeryShortStandaloneWeekdaySymbols | ``` let kCFDateFormatterVeryShortStandaloneWeekdaySymbols: CFString! ``` |
| To | veryShortStandaloneWeekdaySymbols | ``` static let veryShortStandaloneWeekdaySymbols: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.veryShortWeekdaySymbols](https://developer.apple.com/documentation/corefoundation/cfdateformatterkey/1396302-veryshortweekdaysymbols)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterVeryShortWeekdaySymbols | ``` let kCFDateFormatterVeryShortWeekdaySymbols: CFString! ``` |
| To | veryShortWeekdaySymbols | ``` static let veryShortWeekdaySymbols: CFDateFormatterKey! ``` |

Modified [CFDateFormatterKey.weekdaySymbols](https://developer.apple.com/documentation/corefoundation/cfdateformatterkey/1396290-weekdaysymbols)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFDateFormatterWeekdaySymbols | ``` let kCFDateFormatterWeekdaySymbols: CFString! ``` |
| To | weekdaySymbols | ``` static let weekdaySymbols: CFDateFormatterKey! ``` |

Modified [CFDateFormatterStyle [enum]](https://developer.apple.com/documentation/corefoundation/cfdateformatterstyle)

|  | Declaration |
| --- | --- |
| From | ``` enum CFDateFormatterStyle : CFIndex {     case NoStyle     case ShortStyle     case MediumStyle     case LongStyle     case FullStyle } ``` |
| To | ``` enum CFDateFormatterStyle : CFIndex {     case noStyle     case shortStyle     case mediumStyle     case longStyle     case fullStyle } ``` |

Modified [CFDateFormatterStyle.fullStyle](https://developer.apple.com/documentation/corefoundation/cfdateformatterstyle/kcfdateformatterfullstyle)

|  | Declaration |
| --- | --- |
| From | ``` case FullStyle ``` |
| To | ``` case fullStyle ``` |

Modified [CFDateFormatterStyle.longStyle](https://developer.apple.com/documentation/corefoundation/cfdateformatterstyle/kcfdateformatterlongstyle)

|  | Declaration |
| --- | --- |
| From | ``` case LongStyle ``` |
| To | ``` case longStyle ``` |

Modified [CFDateFormatterStyle.mediumStyle](https://developer.apple.com/documentation/corefoundation/cfdateformatterstyle/mediumstyle)

|  | Declaration |
| --- | --- |
| From | ``` case MediumStyle ``` |
| To | ``` case mediumStyle ``` |

Modified [CFDateFormatterStyle.noStyle](https://developer.apple.com/documentation/corefoundation/cfdateformatterstyle/kcfdateformatternostyle)

|  | Declaration |
| --- | --- |
| From | ``` case NoStyle ``` |
| To | ``` case noStyle ``` |

Modified [CFDateFormatterStyle.shortStyle](https://developer.apple.com/documentation/corefoundation/cfdateformatterstyle/shortstyle)

|  | Declaration |
| --- | --- |
| From | ``` case ShortStyle ``` |
| To | ``` case shortStyle ``` |

Modified [CFDictionaryKeyCallBacks [struct]](https://developer.apple.com/documentation/corefoundation/cfdictionarykeycallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CFDictionaryKeyCallBacks {     var version: CFIndex     var retain: CFDictionaryRetainCallBack!     var release: CFDictionaryReleaseCallBack!     var copyDescription: CFDictionaryCopyDescriptionCallBack!     var equal: CFDictionaryEqualCallBack!     var hash: CFDictionaryHashCallBack!     init()     init(version version: CFIndex, retain retain: CFDictionaryRetainCallBack!, release release: CFDictionaryReleaseCallBack!, copyDescription copyDescription: CFDictionaryCopyDescriptionCallBack!, equal equal: CFDictionaryEqualCallBack!, hash hash: CFDictionaryHashCallBack!) } ``` |
| To | ``` struct CFDictionaryKeyCallBacks {     var version: CFIndex     var retain: CoreFoundation.CFDictionaryRetainCallBack!     var release: CoreFoundation.CFDictionaryReleaseCallBack!     var copyDescription: CoreFoundation.CFDictionaryCopyDescriptionCallBack!     var equal: CoreFoundation.CFDictionaryEqualCallBack!     var hash: CoreFoundation.CFDictionaryHashCallBack!     init()     init(version version: CFIndex, retain retain: CoreFoundation.CFDictionaryRetainCallBack!, release release: CoreFoundation.CFDictionaryReleaseCallBack!, copyDescription copyDescription: CoreFoundation.CFDictionaryCopyDescriptionCallBack!, equal equal: CoreFoundation.CFDictionaryEqualCallBack!, hash hash: CoreFoundation.CFDictionaryHashCallBack!) } ``` |

Modified [CFDictionaryKeyCallBacks.copyDescription](https://developer.apple.com/documentation/corefoundation/cfdictionarykeycallbacks/1516761-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFDictionaryCopyDescriptionCallBack! ``` |
| To | ``` var copyDescription: CoreFoundation.CFDictionaryCopyDescriptionCallBack! ``` |

Modified [CFDictionaryKeyCallBacks.equal](https://developer.apple.com/documentation/corefoundation/cfdictionarykeycallbacks/1516802-equal)

|  | Declaration |
| --- | --- |
| From | ``` var equal: CFDictionaryEqualCallBack! ``` |
| To | ``` var equal: CoreFoundation.CFDictionaryEqualCallBack! ``` |

Modified [CFDictionaryKeyCallBacks.hash](https://developer.apple.com/documentation/corefoundation/cfdictionarykeycallbacks/1516784-hash)

|  | Declaration |
| --- | --- |
| From | ``` var hash: CFDictionaryHashCallBack! ``` |
| To | ``` var hash: CoreFoundation.CFDictionaryHashCallBack! ``` |

Modified [CFDictionaryKeyCallBacks.release](https://developer.apple.com/documentation/corefoundation/cfdictionarykeycallbacks/1516780-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFDictionaryReleaseCallBack! ``` |
| To | ``` var release: CoreFoundation.CFDictionaryReleaseCallBack! ``` |

Modified [CFDictionaryKeyCallBacks.retain](https://developer.apple.com/documentation/corefoundation/cfdictionarykeycallbacks/1516804-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFDictionaryRetainCallBack! ``` |
| To | ``` var retain: CoreFoundation.CFDictionaryRetainCallBack! ``` |

Modified [CFDictionaryValueCallBacks [struct]](https://developer.apple.com/documentation/corefoundation/cfdictionaryvaluecallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CFDictionaryValueCallBacks {     var version: CFIndex     var retain: CFDictionaryRetainCallBack!     var release: CFDictionaryReleaseCallBack!     var copyDescription: CFDictionaryCopyDescriptionCallBack!     var equal: CFDictionaryEqualCallBack!     init()     init(version version: CFIndex, retain retain: CFDictionaryRetainCallBack!, release release: CFDictionaryReleaseCallBack!, copyDescription copyDescription: CFDictionaryCopyDescriptionCallBack!, equal equal: CFDictionaryEqualCallBack!) } ``` |
| To | ``` struct CFDictionaryValueCallBacks {     var version: CFIndex     var retain: CoreFoundation.CFDictionaryRetainCallBack!     var release: CoreFoundation.CFDictionaryReleaseCallBack!     var copyDescription: CoreFoundation.CFDictionaryCopyDescriptionCallBack!     var equal: CoreFoundation.CFDictionaryEqualCallBack!     init()     init(version version: CFIndex, retain retain: CoreFoundation.CFDictionaryRetainCallBack!, release release: CoreFoundation.CFDictionaryReleaseCallBack!, copyDescription copyDescription: CoreFoundation.CFDictionaryCopyDescriptionCallBack!, equal equal: CoreFoundation.CFDictionaryEqualCallBack!) } ``` |

Modified [CFDictionaryValueCallBacks.copyDescription](https://developer.apple.com/documentation/corefoundation/cfdictionaryvaluecallbacks/1516773-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFDictionaryCopyDescriptionCallBack! ``` |
| To | ``` var copyDescription: CoreFoundation.CFDictionaryCopyDescriptionCallBack! ``` |

Modified [CFDictionaryValueCallBacks.equal](https://developer.apple.com/documentation/corefoundation/cfdictionaryvaluecallbacks/1516767-equal)

|  | Declaration |
| --- | --- |
| From | ``` var equal: CFDictionaryEqualCallBack! ``` |
| To | ``` var equal: CoreFoundation.CFDictionaryEqualCallBack! ``` |

Modified [CFDictionaryValueCallBacks.release](https://developer.apple.com/documentation/corefoundation/cfdictionaryvaluecallbacks/1516793-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFDictionaryReleaseCallBack! ``` |
| To | ``` var release: CoreFoundation.CFDictionaryReleaseCallBack! ``` |

Modified [CFDictionaryValueCallBacks.retain](https://developer.apple.com/documentation/corefoundation/cfdictionaryvaluecallbacks/1516775-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFDictionaryRetainCallBack! ``` |
| To | ``` var retain: CoreFoundation.CFDictionaryRetainCallBack! ``` |

Modified [CFError](https://developer.apple.com/documentation/corefoundation/cferror)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CFError { } extension CFError : ErrorType { } ``` | ErrorType |
| To | ``` class CFError { } extension CFError : Error { } ``` | Error |

Modified [CFFileDescriptorContext [struct]](https://developer.apple.com/documentation/corefoundation/cffiledescriptorcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFFileDescriptorContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)!     var release: ((UnsafeMutablePointer<Void>) -> Void)!     var copyDescription: ((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)!, release release: ((UnsafeMutablePointer<Void>) -> Void)!, copyDescription copyDescription: ((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)!) } ``` |
| To | ``` struct CFFileDescriptorContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!     var release: ((UnsafeMutableRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!, release release: (@escaping (UnsafeMutableRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!) } ``` |

Modified [CFFileDescriptorContext.copyDescription](https://developer.apple.com/documentation/corefoundation/cffiledescriptorcontext/1477577-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: ((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)! ``` |
| To | ``` var copyDescription: ((UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)! ``` |

Modified [CFFileDescriptorContext.info](https://developer.apple.com/documentation/corefoundation/cffiledescriptorcontext/1477604-info)

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafeMutablePointer<Void> ``` |
| To | ``` var info: UnsafeMutableRawPointer! ``` |

Modified [CFFileDescriptorContext.release](https://developer.apple.com/documentation/corefoundation/cffiledescriptorcontext/1477589-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: ((UnsafeMutablePointer<Void>) -> Void)! ``` |
| To | ``` var release: ((UnsafeMutableRawPointer?) -> Swift.Void)! ``` |

Modified [CFFileDescriptorContext.retain](https://developer.apple.com/documentation/corefoundation/cffiledescriptorcontext/1477599-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: ((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)! ``` |
| To | ``` var retain: ((UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)! ``` |

Modified [CFFileSecurityClearOptions [struct]](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFFileSecurityClearOptions : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var Owner: CFFileSecurityClearOptions { get }     static var Group: CFFileSecurityClearOptions { get }     static var Mode: CFFileSecurityClearOptions { get }     static var OwnerUUID: CFFileSecurityClearOptions { get }     static var GroupUUID: CFFileSecurityClearOptions { get }     static var AccessControlList: CFFileSecurityClearOptions { get } } ``` | OptionSetType |
| To | ``` struct CFFileSecurityClearOptions : OptionSet {     init(rawValue rawValue: CFOptionFlags)     static var owner: CFFileSecurityClearOptions { get }     static var group: CFFileSecurityClearOptions { get }     static var mode: CFFileSecurityClearOptions { get }     static var ownerUUID: CFFileSecurityClearOptions { get }     static var groupUUID: CFFileSecurityClearOptions { get }     static var accessControlList: CFFileSecurityClearOptions { get }     func intersect(_ other: CFFileSecurityClearOptions) -> CFFileSecurityClearOptions     func exclusiveOr(_ other: CFFileSecurityClearOptions) -> CFFileSecurityClearOptions     mutating func unionInPlace(_ other: CFFileSecurityClearOptions)     mutating func intersectInPlace(_ other: CFFileSecurityClearOptions)     mutating func exclusiveOrInPlace(_ other: CFFileSecurityClearOptions)     func isSubsetOf(_ other: CFFileSecurityClearOptions) -> Bool     func isDisjointWith(_ other: CFFileSecurityClearOptions) -> Bool     func isSupersetOf(_ other: CFFileSecurityClearOptions) -> Bool     mutating func subtractInPlace(_ other: CFFileSecurityClearOptions)     func isStrictSupersetOf(_ other: CFFileSecurityClearOptions) -> Bool     func isStrictSubsetOf(_ other: CFFileSecurityClearOptions) -> Bool } extension CFFileSecurityClearOptions {     func union(_ other: CFFileSecurityClearOptions) -> CFFileSecurityClearOptions     func intersection(_ other: CFFileSecurityClearOptions) -> CFFileSecurityClearOptions     func symmetricDifference(_ other: CFFileSecurityClearOptions) -> CFFileSecurityClearOptions } extension CFFileSecurityClearOptions {     func contains(_ member: CFFileSecurityClearOptions) -> Bool     mutating func insert(_ newMember: CFFileSecurityClearOptions) -> (inserted: Bool, memberAfterInsert: CFFileSecurityClearOptions)     mutating func remove(_ member: CFFileSecurityClearOptions) -> CFFileSecurityClearOptions?     mutating func update(with newMember: CFFileSecurityClearOptions) -> CFFileSecurityClearOptions? } extension CFFileSecurityClearOptions {     convenience init()     mutating func formUnion(_ other: CFFileSecurityClearOptions)     mutating func formIntersection(_ other: CFFileSecurityClearOptions)     mutating func formSymmetricDifference(_ other: CFFileSecurityClearOptions) } extension CFFileSecurityClearOptions {     convenience init<S : Sequence where S.Iterator.Element == CFFileSecurityClearOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CFFileSecurityClearOptions...)     mutating func subtract(_ other: CFFileSecurityClearOptions)     func isSubset(of other: CFFileSecurityClearOptions) -> Bool     func isSuperset(of other: CFFileSecurityClearOptions) -> Bool     func isDisjoint(with other: CFFileSecurityClearOptions) -> Bool     func subtracting(_ other: CFFileSecurityClearOptions) -> CFFileSecurityClearOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: CFFileSecurityClearOptions) -> Bool     func isStrictSubset(of other: CFFileSecurityClearOptions) -> Bool } ``` | OptionSet |

Modified [CFFileSecurityClearOptions.accessControlList](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions/1426502-accesscontrollist)

|  | Declaration |
| --- | --- |
| From | ``` static var AccessControlList: CFFileSecurityClearOptions { get } ``` |
| To | ``` static var accessControlList: CFFileSecurityClearOptions { get } ``` |

Modified [CFFileSecurityClearOptions.group](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions/1426529-group)

|  | Declaration |
| --- | --- |
| From | ``` static var Group: CFFileSecurityClearOptions { get } ``` |
| To | ``` static var group: CFFileSecurityClearOptions { get } ``` |

Modified [CFFileSecurityClearOptions.groupUUID](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions/1426522-groupuuid)

|  | Declaration |
| --- | --- |
| From | ``` static var GroupUUID: CFFileSecurityClearOptions { get } ``` |
| To | ``` static var groupUUID: CFFileSecurityClearOptions { get } ``` |

Modified [CFFileSecurityClearOptions.mode](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions/1426504-mode)

|  | Declaration |
| --- | --- |
| From | ``` static var Mode: CFFileSecurityClearOptions { get } ``` |
| To | ``` static var mode: CFFileSecurityClearOptions { get } ``` |

Modified [CFFileSecurityClearOptions.owner](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions/kcffilesecurityclearowner)

|  | Declaration |
| --- | --- |
| From | ``` static var Owner: CFFileSecurityClearOptions { get } ``` |
| To | ``` static var owner: CFFileSecurityClearOptions { get } ``` |

Modified [CFFileSecurityClearOptions.ownerUUID](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions/1426520-owneruuid)

|  | Declaration |
| --- | --- |
| From | ``` static var OwnerUUID: CFFileSecurityClearOptions { get } ``` |
| To | ``` static var ownerUUID: CFFileSecurityClearOptions { get } ``` |

Modified [CFGregorianUnitFlags [struct]](https://developer.apple.com/documentation/corefoundation/cfgregorianunitflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFGregorianUnitFlags : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var UnitsYears: CFGregorianUnitFlags { get }     static var UnitsMonths: CFGregorianUnitFlags { get }     static var UnitsDays: CFGregorianUnitFlags { get }     static var UnitsHours: CFGregorianUnitFlags { get }     static var UnitsMinutes: CFGregorianUnitFlags { get }     static var UnitsSeconds: CFGregorianUnitFlags { get }     static var AllUnits: CFGregorianUnitFlags { get } } ``` | OptionSetType |
| To | ``` struct CFGregorianUnitFlags : OptionSet {     init(rawValue rawValue: CFOptionFlags)     static var unitsYears: CFGregorianUnitFlags { get }     static var unitsMonths: CFGregorianUnitFlags { get }     static var unitsDays: CFGregorianUnitFlags { get }     static var unitsHours: CFGregorianUnitFlags { get }     static var unitsMinutes: CFGregorianUnitFlags { get }     static var unitsSeconds: CFGregorianUnitFlags { get }     static var allUnits: CFGregorianUnitFlags { get }     func intersect(_ other: CFGregorianUnitFlags) -> CFGregorianUnitFlags     func exclusiveOr(_ other: CFGregorianUnitFlags) -> CFGregorianUnitFlags     mutating func unionInPlace(_ other: CFGregorianUnitFlags)     mutating func intersectInPlace(_ other: CFGregorianUnitFlags)     mutating func exclusiveOrInPlace(_ other: CFGregorianUnitFlags)     func isSubsetOf(_ other: CFGregorianUnitFlags) -> Bool     func isDisjointWith(_ other: CFGregorianUnitFlags) -> Bool     func isSupersetOf(_ other: CFGregorianUnitFlags) -> Bool     mutating func subtractInPlace(_ other: CFGregorianUnitFlags)     func isStrictSupersetOf(_ other: CFGregorianUnitFlags) -> Bool     func isStrictSubsetOf(_ other: CFGregorianUnitFlags) -> Bool } extension CFGregorianUnitFlags {     func union(_ other: CFGregorianUnitFlags) -> CFGregorianUnitFlags     func intersection(_ other: CFGregorianUnitFlags) -> CFGregorianUnitFlags     func symmetricDifference(_ other: CFGregorianUnitFlags) -> CFGregorianUnitFlags } extension CFGregorianUnitFlags {     func contains(_ member: CFGregorianUnitFlags) -> Bool     mutating func insert(_ newMember: CFGregorianUnitFlags) -> (inserted: Bool, memberAfterInsert: CFGregorianUnitFlags)     mutating func remove(_ member: CFGregorianUnitFlags) -> CFGregorianUnitFlags?     mutating func update(with newMember: CFGregorianUnitFlags) -> CFGregorianUnitFlags? } extension CFGregorianUnitFlags {     convenience init()     mutating func formUnion(_ other: CFGregorianUnitFlags)     mutating func formIntersection(_ other: CFGregorianUnitFlags)     mutating func formSymmetricDifference(_ other: CFGregorianUnitFlags) } extension CFGregorianUnitFlags {     convenience init<S : Sequence where S.Iterator.Element == CFGregorianUnitFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CFGregorianUnitFlags...)     mutating func subtract(_ other: CFGregorianUnitFlags)     func isSubset(of other: CFGregorianUnitFlags) -> Bool     func isSuperset(of other: CFGregorianUnitFlags) -> Bool     func isDisjoint(with other: CFGregorianUnitFlags) -> Bool     func subtracting(_ other: CFGregorianUnitFlags) -> CFGregorianUnitFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: CFGregorianUnitFlags) -> Bool     func isStrictSubset(of other: CFGregorianUnitFlags) -> Bool } ``` | OptionSet |

Modified [CFGregorianUnitFlags.allUnits](https://developer.apple.com/documentation/corefoundation/cfgregorianunitflags/kcfgregorianallunits)

|  | Declaration |
| --- | --- |
| From | ``` static var AllUnits: CFGregorianUnitFlags { get } ``` |
| To | ``` static var allUnits: CFGregorianUnitFlags { get } ``` |

Modified [CFGregorianUnitFlags.unitsDays](https://developer.apple.com/documentation/corefoundation/cfgregorianunitflags/kcfgregorianunitsdays)

|  | Declaration |
| --- | --- |
| From | ``` static var UnitsDays: CFGregorianUnitFlags { get } ``` |
| To | ``` static var unitsDays: CFGregorianUnitFlags { get } ``` |

Modified [CFGregorianUnitFlags.unitsHours](https://developer.apple.com/documentation/corefoundation/cfgregorianunitflags/1543082-unitshours)

|  | Declaration |
| --- | --- |
| From | ``` static var UnitsHours: CFGregorianUnitFlags { get } ``` |
| To | ``` static var unitsHours: CFGregorianUnitFlags { get } ``` |

Modified [CFGregorianUnitFlags.unitsMinutes](https://developer.apple.com/documentation/corefoundation/cfgregorianunitflags/kcfgregorianunitsminutes)

|  | Declaration |
| --- | --- |
| From | ``` static var UnitsMinutes: CFGregorianUnitFlags { get } ``` |
| To | ``` static var unitsMinutes: CFGregorianUnitFlags { get } ``` |

Modified [CFGregorianUnitFlags.unitsMonths](https://developer.apple.com/documentation/corefoundation/cfgregorianunitflags/kcfgregorianunitsmonths)

|  | Declaration |
| --- | --- |
| From | ``` static var UnitsMonths: CFGregorianUnitFlags { get } ``` |
| To | ``` static var unitsMonths: CFGregorianUnitFlags { get } ``` |

Modified [CFGregorianUnitFlags.unitsSeconds](https://developer.apple.com/documentation/corefoundation/cfgregorianunitflags/1541472-unitsseconds)

|  | Declaration |
| --- | --- |
| From | ``` static var UnitsSeconds: CFGregorianUnitFlags { get } ``` |
| To | ``` static var unitsSeconds: CFGregorianUnitFlags { get } ``` |

Modified [CFGregorianUnitFlags.unitsYears](https://developer.apple.com/documentation/corefoundation/cfgregorianunitflags/1542351-unitsyears)

|  | Declaration |
| --- | --- |
| From | ``` static var UnitsYears: CFGregorianUnitFlags { get } ``` |
| To | ``` static var unitsYears: CFGregorianUnitFlags { get } ``` |

Modified [CFLocaleKey.alternateQuotationBeginDelimiterKey](https://developer.apple.com/documentation/corefoundation/kcflocalealternatequotationbegindelimiterkey)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFLocaleAlternateQuotationBeginDelimiterKey | ``` let kCFLocaleAlternateQuotationBeginDelimiterKey: CFString! ``` |
| To | alternateQuotationBeginDelimiterKey | ``` static let alternateQuotationBeginDelimiterKey: CFLocaleKey! ``` |

Modified [CFLocaleKey.alternateQuotationEndDelimiterKey](https://developer.apple.com/documentation/corefoundation/kcflocalealternatequotationenddelimiterkey)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFLocaleAlternateQuotationEndDelimiterKey | ``` let kCFLocaleAlternateQuotationEndDelimiterKey: CFString! ``` |
| To | alternateQuotationEndDelimiterKey | ``` static let alternateQuotationEndDelimiterKey: CFLocaleKey! ``` |

Modified [CFLocaleKey.calendar](https://developer.apple.com/documentation/corefoundation/cflocalekey/1541806-calendar)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFLocaleCalendar | ``` let kCFLocaleCalendar: CFString! ``` |
| To | calendar | ``` static let calendar: CFLocaleKey! ``` |

Modified [CFLocaleKey.calendarIdentifier](https://developer.apple.com/documentation/corefoundation/kcflocalecalendaridentifier)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFLocaleCalendarIdentifier | ``` let kCFLocaleCalendarIdentifier: CFString! ``` |
| To | calendarIdentifier | ``` static let calendarIdentifier: CFLocaleKey! ``` |

Modified [CFLocaleKey.collationIdentifier](https://developer.apple.com/documentation/corefoundation/cflocalekey/1543603-collationidentifier)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFLocaleCollationIdentifier | ``` let kCFLocaleCollationIdentifier: CFString! ``` |
| To | collationIdentifier | ``` static let collationIdentifier: CFLocaleKey! ``` |

Modified [CFLocaleKey.collatorIdentifier](https://developer.apple.com/documentation/corefoundation/cflocalekey/1542594-collatoridentifier)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFLocaleCollatorIdentifier | ``` let kCFLocaleCollatorIdentifier: CFString! ``` |
| To | collatorIdentifier | ``` static let collatorIdentifier: CFLocaleKey! ``` |

Modified [CFLocaleKey.countryCode](https://developer.apple.com/documentation/corefoundation/kcflocalecountrycode)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFLocaleCountryCode | ``` let kCFLocaleCountryCode: CFString! ``` |
| To | countryCode | ``` static let countryCode: CFLocaleKey! ``` |

Modified [CFLocaleKey.currencyCode](https://developer.apple.com/documentation/corefoundation/kcflocalecurrencycode)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFLocaleCurrencyCode | ``` let kCFLocaleCurrencyCode: CFString! ``` |
| To | currencyCode | ``` static let currencyCode: CFLocaleKey! ``` |

Modified [CFLocaleKey.currencySymbol](https://developer.apple.com/documentation/corefoundation/kcflocalecurrencysymbol)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFLocaleCurrencySymbol | ``` let kCFLocaleCurrencySymbol: CFString! ``` |
| To | currencySymbol | ``` static let currencySymbol: CFLocaleKey! ``` |

Modified [CFLocaleKey.decimalSeparator](https://developer.apple.com/documentation/corefoundation/kcflocaledecimalseparator)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFLocaleDecimalSeparator | ``` let kCFLocaleDecimalSeparator: CFString! ``` |
| To | decimalSeparator | ``` static let decimalSeparator: CFLocaleKey! ``` |

Modified [CFLocaleKey.exemplarCharacterSet](https://developer.apple.com/documentation/corefoundation/kcflocaleexemplarcharacterset)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFLocaleExemplarCharacterSet | ``` let kCFLocaleExemplarCharacterSet: CFString! ``` |
| To | exemplarCharacterSet | ``` static let exemplarCharacterSet: CFLocaleKey! ``` |

Modified [CFLocaleKey.groupingSeparator](https://developer.apple.com/documentation/corefoundation/cflocalekey/1542004-groupingseparator)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFLocaleGroupingSeparator | ``` let kCFLocaleGroupingSeparator: CFString! ``` |
| To | groupingSeparator | ``` static let groupingSeparator: CFLocaleKey! ``` |

Modified [CFLocaleKey.identifier](https://developer.apple.com/documentation/corefoundation/kcflocaleidentifier)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFLocaleIdentifier | ``` let kCFLocaleIdentifier: CFString! ``` |
| To | identifier | ``` static let identifier: CFLocaleKey! ``` |

Modified [CFLocaleKey.languageCode](https://developer.apple.com/documentation/corefoundation/cflocalekey/1541614-languagecode)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFLocaleLanguageCode | ``` let kCFLocaleLanguageCode: CFString! ``` |
| To | languageCode | ``` static let languageCode: CFLocaleKey! ``` |

Modified [CFLocaleKey.measurementSystem](https://developer.apple.com/documentation/corefoundation/cflocalekey/1542727-measurementsystem)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFLocaleMeasurementSystem | ``` let kCFLocaleMeasurementSystem: CFString! ``` |
| To | measurementSystem | ``` static let measurementSystem: CFLocaleKey! ``` |

Modified [CFLocaleKey.quotationBeginDelimiterKey](https://developer.apple.com/documentation/corefoundation/kcflocalequotationbegindelimiterkey)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFLocaleQuotationBeginDelimiterKey | ``` let kCFLocaleQuotationBeginDelimiterKey: CFString! ``` |
| To | quotationBeginDelimiterKey | ``` static let quotationBeginDelimiterKey: CFLocaleKey! ``` |

Modified [CFLocaleKey.quotationEndDelimiterKey](https://developer.apple.com/documentation/corefoundation/kcflocalequotationenddelimiterkey)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFLocaleQuotationEndDelimiterKey | ``` let kCFLocaleQuotationEndDelimiterKey: CFString! ``` |
| To | quotationEndDelimiterKey | ``` static let quotationEndDelimiterKey: CFLocaleKey! ``` |

Modified [CFLocaleKey.scriptCode](https://developer.apple.com/documentation/corefoundation/kcflocalescriptcode)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFLocaleScriptCode | ``` let kCFLocaleScriptCode: CFString! ``` |
| To | scriptCode | ``` static let scriptCode: CFLocaleKey! ``` |

Modified [CFLocaleKey.usesMetricSystem](https://developer.apple.com/documentation/corefoundation/kcflocaleusesmetricsystem)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFLocaleUsesMetricSystem | ``` let kCFLocaleUsesMetricSystem: CFString! ``` |
| To | usesMetricSystem | ``` static let usesMetricSystem: CFLocaleKey! ``` |

Modified [CFLocaleKey.variantCode](https://developer.apple.com/documentation/corefoundation/kcflocalevariantcode)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFLocaleVariantCode | ``` let kCFLocaleVariantCode: CFString! ``` |
| To | variantCode | ``` static let variantCode: CFLocaleKey! ``` |

Modified [CFLocaleLanguageDirection [enum]](https://developer.apple.com/documentation/corefoundation/cflocalelanguagedirection)

|  | Declaration |
| --- | --- |
| From | ``` enum CFLocaleLanguageDirection : CFIndex {     case Unknown     case LeftToRight     case RightToLeft     case TopToBottom     case BottomToTop } ``` |
| To | ``` enum CFLocaleLanguageDirection : CFIndex {     case unknown     case leftToRight     case rightToLeft     case topToBottom     case bottomToTop } ``` |

Modified [CFLocaleLanguageDirection.bottomToTop](https://developer.apple.com/documentation/corefoundation/cflocalelanguagedirection/kcflocalelanguagedirectionbottomtotop)

|  | Declaration |
| --- | --- |
| From | ``` case BottomToTop ``` |
| To | ``` case bottomToTop ``` |

Modified [CFLocaleLanguageDirection.leftToRight](https://developer.apple.com/documentation/corefoundation/cflocalelanguagedirection/kcflocalelanguagedirectionlefttoright)

|  | Declaration |
| --- | --- |
| From | ``` case LeftToRight ``` |
| To | ``` case leftToRight ``` |

Modified [CFLocaleLanguageDirection.rightToLeft](https://developer.apple.com/documentation/corefoundation/cflocalelanguagedirection/kcflocalelanguagedirectionrighttoleft)

|  | Declaration |
| --- | --- |
| From | ``` case RightToLeft ``` |
| To | ``` case rightToLeft ``` |

Modified [CFLocaleLanguageDirection.topToBottom](https://developer.apple.com/documentation/corefoundation/cflocalelanguagedirection/kcflocalelanguagedirectiontoptobottom)

|  | Declaration |
| --- | --- |
| From | ``` case TopToBottom ``` |
| To | ``` case topToBottom ``` |

Modified [CFLocaleLanguageDirection.unknown](https://developer.apple.com/documentation/corefoundation/cflocalelanguagedirection/kcflocalelanguagedirectionunknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [CFMachPortContext [struct]](https://developer.apple.com/documentation/corefoundation/cfmachportcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFMachPortContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!     var release: ((UnsafePointer<Void>) -> Void)!     var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release release: ((UnsafePointer<Void>) -> Void)!, copyDescription copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!) } ``` |
| To | ``` struct CFMachPortContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!) } ``` |

Modified [CFMachPortContext.copyDescription](https://developer.apple.com/documentation/corefoundation/cfmachportcontext/1400944-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)! ``` |
| To | ``` var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)! ``` |

Modified [CFMachPortContext.info](https://developer.apple.com/documentation/corefoundation/cfmachportcontext/1400916-info)

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafeMutablePointer<Void> ``` |
| To | ``` var info: UnsafeMutableRawPointer! ``` |

Modified [CFMachPortContext.release](https://developer.apple.com/documentation/corefoundation/cfmachportcontext/1400920-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: ((UnsafePointer<Void>) -> Void)! ``` |
| To | ``` var release: ((UnsafeRawPointer?) -> Swift.Void)! ``` |

Modified [CFMachPortContext.retain](https://developer.apple.com/documentation/corefoundation/cfmachportcontext/1400912-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)! ``` |
| To | ``` var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)! ``` |

Modified [CFMessagePortContext [struct]](https://developer.apple.com/documentation/corefoundation/cfmessageportcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFMessagePortContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!     var release: ((UnsafePointer<Void>) -> Void)!     var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release release: ((UnsafePointer<Void>) -> Void)!, copyDescription copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!) } ``` |
| To | ``` struct CFMessagePortContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!) } ``` |

Modified [CFMessagePortContext.copyDescription](https://developer.apple.com/documentation/corefoundation/cfmessageportcontext/1542175-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)! ``` |
| To | ``` var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)! ``` |

Modified [CFMessagePortContext.info](https://developer.apple.com/documentation/corefoundation/cfmessageportcontext/1543696-info)

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafeMutablePointer<Void> ``` |
| To | ``` var info: UnsafeMutableRawPointer! ``` |

Modified [CFMessagePortContext.release](https://developer.apple.com/documentation/corefoundation/cfmessageportcontext/1542528-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: ((UnsafePointer<Void>) -> Void)! ``` |
| To | ``` var release: ((UnsafeRawPointer?) -> Swift.Void)! ``` |

Modified [CFMessagePortContext.retain](https://developer.apple.com/documentation/corefoundation/cfmessageportcontext/1542526-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)! ``` |
| To | ``` var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)! ``` |

Modified [CFNotificationName.cfLocaleCurrentLocaleDidChange](https://developer.apple.com/documentation/corefoundation/cfnotificationname/1543467-cflocalecurrentlocaledidchange)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFLocaleCurrentLocaleDidChangeNotification | ``` let kCFLocaleCurrentLocaleDidChangeNotification: CFString! ``` |
| To | cfLocaleCurrentLocaleDidChange | ``` static let cfLocaleCurrentLocaleDidChange: CFNotificationName! ``` |

Modified [CFNotificationName.cfTimeZoneSystemTimeZoneDidChange](https://developer.apple.com/documentation/corefoundation/kcftimezonesystemtimezonedidchangenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFTimeZoneSystemTimeZoneDidChangeNotification | ``` let kCFTimeZoneSystemTimeZoneDidChangeNotification: CFString! ``` |
| To | cfTimeZoneSystemTimeZoneDidChange | ``` static let cfTimeZoneSystemTimeZoneDidChange: CFNotificationName! ``` |

Modified [CFNotificationSuspensionBehavior [enum]](https://developer.apple.com/documentation/corefoundation/cfnotificationsuspensionbehavior)

|  | Declaration |
| --- | --- |
| From | ``` enum CFNotificationSuspensionBehavior : CFIndex {     case Drop     case Coalesce     case Hold     case DeliverImmediately } ``` |
| To | ``` enum CFNotificationSuspensionBehavior : CFIndex {     case drop     case coalesce     case hold     case deliverImmediately } ``` |

Modified [CFNotificationSuspensionBehavior.coalesce](https://developer.apple.com/documentation/corefoundation/cfnotificationsuspensionbehavior/cfnotificationsuspensionbehaviorcoalesce)

|  | Declaration |
| --- | --- |
| From | ``` case Coalesce ``` |
| To | ``` case coalesce ``` |

Modified [CFNotificationSuspensionBehavior.deliverImmediately](https://developer.apple.com/documentation/corefoundation/cfnotificationsuspensionbehavior/cfnotificationsuspensionbehaviordeliverimmediately)

|  | Declaration |
| --- | --- |
| From | ``` case DeliverImmediately ``` |
| To | ``` case deliverImmediately ``` |

Modified [CFNotificationSuspensionBehavior.drop](https://developer.apple.com/documentation/corefoundation/cfnotificationsuspensionbehavior/drop)

|  | Declaration |
| --- | --- |
| From | ``` case Drop ``` |
| To | ``` case drop ``` |

Modified [CFNotificationSuspensionBehavior.hold](https://developer.apple.com/documentation/corefoundation/cfnotificationsuspensionbehavior/cfnotificationsuspensionbehaviorhold)

|  | Declaration |
| --- | --- |
| From | ``` case Hold ``` |
| To | ``` case hold ``` |

Modified [CFNumberFormatterKey.alwaysShowDecimalSeparator](https://developer.apple.com/documentation/corefoundation/kcfnumberformatteralwaysshowdecimalseparator)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterAlwaysShowDecimalSeparator | ``` let kCFNumberFormatterAlwaysShowDecimalSeparator: CFString! ``` |
| To | alwaysShowDecimalSeparator | ``` static let alwaysShowDecimalSeparator: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.currencyCode](https://developer.apple.com/documentation/corefoundation/kcfnumberformattercurrencycode)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterCurrencyCode | ``` let kCFNumberFormatterCurrencyCode: CFString! ``` |
| To | currencyCode | ``` static let currencyCode: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.currencyDecimalSeparator](https://developer.apple.com/documentation/corefoundation/kcfnumberformattercurrencydecimalseparator)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterCurrencyDecimalSeparator | ``` let kCFNumberFormatterCurrencyDecimalSeparator: CFString! ``` |
| To | currencyDecimalSeparator | ``` static let currencyDecimalSeparator: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.currencyGroupingSeparator](https://developer.apple.com/documentation/corefoundation/kcfnumberformattercurrencygroupingseparator)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterCurrencyGroupingSeparator | ``` let kCFNumberFormatterCurrencyGroupingSeparator: CFString! ``` |
| To | currencyGroupingSeparator | ``` static let currencyGroupingSeparator: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.currencySymbol](https://developer.apple.com/documentation/corefoundation/kcfnumberformattercurrencysymbol)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterCurrencySymbol | ``` let kCFNumberFormatterCurrencySymbol: CFString! ``` |
| To | currencySymbol | ``` static let currencySymbol: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.decimalSeparator](https://developer.apple.com/documentation/corefoundation/kcfnumberformatterdecimalseparator)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterDecimalSeparator | ``` let kCFNumberFormatterDecimalSeparator: CFString! ``` |
| To | decimalSeparator | ``` static let decimalSeparator: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.defaultFormat](https://developer.apple.com/documentation/corefoundation/kcfnumberformatterdefaultformat)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterDefaultFormat | ``` let kCFNumberFormatterDefaultFormat: CFString! ``` |
| To | defaultFormat | ``` static let defaultFormat: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.exponentSymbol](https://developer.apple.com/documentation/corefoundation/cfnumberformatterkey/1390763-exponentsymbol)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterExponentSymbol | ``` let kCFNumberFormatterExponentSymbol: CFString! ``` |
| To | exponentSymbol | ``` static let exponentSymbol: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.formatWidth](https://developer.apple.com/documentation/corefoundation/kcfnumberformatterformatwidth)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterFormatWidth | ``` let kCFNumberFormatterFormatWidth: CFString! ``` |
| To | formatWidth | ``` static let formatWidth: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.groupingSeparator](https://developer.apple.com/documentation/corefoundation/cfnumberformatterkey/1390792-groupingseparator)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterGroupingSeparator | ``` let kCFNumberFormatterGroupingSeparator: CFString! ``` |
| To | groupingSeparator | ``` static let groupingSeparator: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.groupingSize](https://developer.apple.com/documentation/corefoundation/kcfnumberformattergroupingsize)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterGroupingSize | ``` let kCFNumberFormatterGroupingSize: CFString! ``` |
| To | groupingSize | ``` static let groupingSize: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.infinitySymbol](https://developer.apple.com/documentation/corefoundation/cfnumberformatterkey/1390718-infinitysymbol)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterInfinitySymbol | ``` let kCFNumberFormatterInfinitySymbol: CFString! ``` |
| To | infinitySymbol | ``` static let infinitySymbol: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.internationalCurrencySymbol](https://developer.apple.com/documentation/corefoundation/kcfnumberformatterinternationalcurrencysymbol)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterInternationalCurrencySymbol | ``` let kCFNumberFormatterInternationalCurrencySymbol: CFString! ``` |
| To | internationalCurrencySymbol | ``` static let internationalCurrencySymbol: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.isLenient](https://developer.apple.com/documentation/corefoundation/kcfnumberformatterislenient)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterIsLenient | ``` let kCFNumberFormatterIsLenient: CFString! ``` |
| To | isLenient | ``` static let isLenient: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.maxFractionDigits](https://developer.apple.com/documentation/corefoundation/kcfnumberformattermaxfractiondigits)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterMaxFractionDigits | ``` let kCFNumberFormatterMaxFractionDigits: CFString! ``` |
| To | maxFractionDigits | ``` static let maxFractionDigits: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.maxIntegerDigits](https://developer.apple.com/documentation/corefoundation/cfnumberformatterkey/1390810-maxintegerdigits)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterMaxIntegerDigits | ``` let kCFNumberFormatterMaxIntegerDigits: CFString! ``` |
| To | maxIntegerDigits | ``` static let maxIntegerDigits: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.maxSignificantDigits](https://developer.apple.com/documentation/corefoundation/cfnumberformatterkey/1390824-maxsignificantdigits)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterMaxSignificantDigits | ``` let kCFNumberFormatterMaxSignificantDigits: CFString! ``` |
| To | maxSignificantDigits | ``` static let maxSignificantDigits: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.minFractionDigits](https://developer.apple.com/documentation/corefoundation/cfnumberformatterkey/1390742-minfractiondigits)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterMinFractionDigits | ``` let kCFNumberFormatterMinFractionDigits: CFString! ``` |
| To | minFractionDigits | ``` static let minFractionDigits: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.minIntegerDigits](https://developer.apple.com/documentation/corefoundation/cfnumberformatterkey/1390706-minintegerdigits)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterMinIntegerDigits | ``` let kCFNumberFormatterMinIntegerDigits: CFString! ``` |
| To | minIntegerDigits | ``` static let minIntegerDigits: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.minSignificantDigits](https://developer.apple.com/documentation/corefoundation/cfnumberformatterkey/1390744-minsignificantdigits)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterMinSignificantDigits | ``` let kCFNumberFormatterMinSignificantDigits: CFString! ``` |
| To | minSignificantDigits | ``` static let minSignificantDigits: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.minusSign](https://developer.apple.com/documentation/corefoundation/kcfnumberformatterminussign)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterMinusSign | ``` let kCFNumberFormatterMinusSign: CFString! ``` |
| To | minusSign | ``` static let minusSign: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.multiplier](https://developer.apple.com/documentation/corefoundation/kcfnumberformattermultiplier)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterMultiplier | ``` let kCFNumberFormatterMultiplier: CFString! ``` |
| To | multiplier | ``` static let multiplier: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.naNSymbol](https://developer.apple.com/documentation/corefoundation/kcfnumberformatternansymbol)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterNaNSymbol | ``` let kCFNumberFormatterNaNSymbol: CFString! ``` |
| To | naNSymbol | ``` static let naNSymbol: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.negativePrefix](https://developer.apple.com/documentation/corefoundation/cfnumberformatterkey/1390782-negativeprefix)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterNegativePrefix | ``` let kCFNumberFormatterNegativePrefix: CFString! ``` |
| To | negativePrefix | ``` static let negativePrefix: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.negativeSuffix](https://developer.apple.com/documentation/corefoundation/kcfnumberformatternegativesuffix)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterNegativeSuffix | ``` let kCFNumberFormatterNegativeSuffix: CFString! ``` |
| To | negativeSuffix | ``` static let negativeSuffix: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.paddingCharacter](https://developer.apple.com/documentation/corefoundation/cfnumberformatterkey/1390749-paddingcharacter)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterPaddingCharacter | ``` let kCFNumberFormatterPaddingCharacter: CFString! ``` |
| To | paddingCharacter | ``` static let paddingCharacter: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.paddingPosition](https://developer.apple.com/documentation/corefoundation/kcfnumberformatterpaddingposition)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterPaddingPosition | ``` let kCFNumberFormatterPaddingPosition: CFString! ``` |
| To | paddingPosition | ``` static let paddingPosition: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.percentSymbol](https://developer.apple.com/documentation/corefoundation/cfnumberformatterkey/1390788-percentsymbol)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterPercentSymbol | ``` let kCFNumberFormatterPercentSymbol: CFString! ``` |
| To | percentSymbol | ``` static let percentSymbol: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.perMillSymbol](https://developer.apple.com/documentation/corefoundation/cfnumberformatterkey/1390700-permillsymbol)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterPerMillSymbol | ``` let kCFNumberFormatterPerMillSymbol: CFString! ``` |
| To | perMillSymbol | ``` static let perMillSymbol: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.plusSign](https://developer.apple.com/documentation/corefoundation/kcfnumberformatterplussign)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterPlusSign | ``` let kCFNumberFormatterPlusSign: CFString! ``` |
| To | plusSign | ``` static let plusSign: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.positivePrefix](https://developer.apple.com/documentation/corefoundation/cfnumberformatterkey/1390698-positiveprefix)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterPositivePrefix | ``` let kCFNumberFormatterPositivePrefix: CFString! ``` |
| To | positivePrefix | ``` static let positivePrefix: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.positiveSuffix](https://developer.apple.com/documentation/corefoundation/kcfnumberformatterpositivesuffix)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterPositiveSuffix | ``` let kCFNumberFormatterPositiveSuffix: CFString! ``` |
| To | positiveSuffix | ``` static let positiveSuffix: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.roundingIncrement](https://developer.apple.com/documentation/corefoundation/cfnumberformatterkey/1390712-roundingincrement)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterRoundingIncrement | ``` let kCFNumberFormatterRoundingIncrement: CFString! ``` |
| To | roundingIncrement | ``` static let roundingIncrement: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.roundingMode](https://developer.apple.com/documentation/corefoundation/kcfnumberformatterroundingmode)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterRoundingMode | ``` let kCFNumberFormatterRoundingMode: CFString! ``` |
| To | roundingMode | ``` static let roundingMode: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.secondaryGroupingSize](https://developer.apple.com/documentation/corefoundation/cfnumberformatterkey/1390767-secondarygroupingsize)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterSecondaryGroupingSize | ``` let kCFNumberFormatterSecondaryGroupingSize: CFString! ``` |
| To | secondaryGroupingSize | ``` static let secondaryGroupingSize: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.useGroupingSeparator](https://developer.apple.com/documentation/corefoundation/cfnumberformatterkey/1390746-usegroupingseparator)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterUseGroupingSeparator | ``` let kCFNumberFormatterUseGroupingSeparator: CFString! ``` |
| To | useGroupingSeparator | ``` static let useGroupingSeparator: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.useSignificantDigits](https://developer.apple.com/documentation/corefoundation/kcfnumberformatterusesignificantdigits)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterUseSignificantDigits | ``` let kCFNumberFormatterUseSignificantDigits: CFString! ``` |
| To | useSignificantDigits | ``` static let useSignificantDigits: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterKey.zeroSymbol](https://developer.apple.com/documentation/corefoundation/cfnumberformatterkey/1390753-zerosymbol)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFNumberFormatterZeroSymbol | ``` let kCFNumberFormatterZeroSymbol: CFString! ``` |
| To | zeroSymbol | ``` static let zeroSymbol: CFNumberFormatterKey! ``` |

Modified [CFNumberFormatterOptionFlags [struct]](https://developer.apple.com/documentation/corefoundation/cfnumberformatteroptionflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFNumberFormatterOptionFlags : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var ParseIntegersOnly: CFNumberFormatterOptionFlags { get } } ``` | OptionSetType |
| To | ``` struct CFNumberFormatterOptionFlags : OptionSet {     init(rawValue rawValue: CFOptionFlags)     static var parseIntegersOnly: CFNumberFormatterOptionFlags { get }     func intersect(_ other: CFNumberFormatterOptionFlags) -> CFNumberFormatterOptionFlags     func exclusiveOr(_ other: CFNumberFormatterOptionFlags) -> CFNumberFormatterOptionFlags     mutating func unionInPlace(_ other: CFNumberFormatterOptionFlags)     mutating func intersectInPlace(_ other: CFNumberFormatterOptionFlags)     mutating func exclusiveOrInPlace(_ other: CFNumberFormatterOptionFlags)     func isSubsetOf(_ other: CFNumberFormatterOptionFlags) -> Bool     func isDisjointWith(_ other: CFNumberFormatterOptionFlags) -> Bool     func isSupersetOf(_ other: CFNumberFormatterOptionFlags) -> Bool     mutating func subtractInPlace(_ other: CFNumberFormatterOptionFlags)     func isStrictSupersetOf(_ other: CFNumberFormatterOptionFlags) -> Bool     func isStrictSubsetOf(_ other: CFNumberFormatterOptionFlags) -> Bool } extension CFNumberFormatterOptionFlags {     func union(_ other: CFNumberFormatterOptionFlags) -> CFNumberFormatterOptionFlags     func intersection(_ other: CFNumberFormatterOptionFlags) -> CFNumberFormatterOptionFlags     func symmetricDifference(_ other: CFNumberFormatterOptionFlags) -> CFNumberFormatterOptionFlags } extension CFNumberFormatterOptionFlags {     func contains(_ member: CFNumberFormatterOptionFlags) -> Bool     mutating func insert(_ newMember: CFNumberFormatterOptionFlags) -> (inserted: Bool, memberAfterInsert: CFNumberFormatterOptionFlags)     mutating func remove(_ member: CFNumberFormatterOptionFlags) -> CFNumberFormatterOptionFlags?     mutating func update(with newMember: CFNumberFormatterOptionFlags) -> CFNumberFormatterOptionFlags? } extension CFNumberFormatterOptionFlags {     convenience init()     mutating func formUnion(_ other: CFNumberFormatterOptionFlags)     mutating func formIntersection(_ other: CFNumberFormatterOptionFlags)     mutating func formSymmetricDifference(_ other: CFNumberFormatterOptionFlags) } extension CFNumberFormatterOptionFlags {     convenience init<S : Sequence where S.Iterator.Element == CFNumberFormatterOptionFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CFNumberFormatterOptionFlags...)     mutating func subtract(_ other: CFNumberFormatterOptionFlags)     func isSubset(of other: CFNumberFormatterOptionFlags) -> Bool     func isSuperset(of other: CFNumberFormatterOptionFlags) -> Bool     func isDisjoint(with other: CFNumberFormatterOptionFlags) -> Bool     func subtracting(_ other: CFNumberFormatterOptionFlags) -> CFNumberFormatterOptionFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: CFNumberFormatterOptionFlags) -> Bool     func isStrictSubset(of other: CFNumberFormatterOptionFlags) -> Bool } ``` | OptionSet |

Modified [CFNumberFormatterOptionFlags.parseIntegersOnly](https://developer.apple.com/documentation/corefoundation/cfnumberformatteroptionflags/1390759-parseintegersonly)

|  | Declaration |
| --- | --- |
| From | ``` static var ParseIntegersOnly: CFNumberFormatterOptionFlags { get } ``` |
| To | ``` static var parseIntegersOnly: CFNumberFormatterOptionFlags { get } ``` |

Modified [CFNumberFormatterPadPosition [enum]](https://developer.apple.com/documentation/corefoundation/cfnumberformatterpadposition)

|  | Declaration |
| --- | --- |
| From | ``` enum CFNumberFormatterPadPosition : CFIndex {     case BeforePrefix     case AfterPrefix     case BeforeSuffix     case AfterSuffix } ``` |
| To | ``` enum CFNumberFormatterPadPosition : CFIndex {     case beforePrefix     case afterPrefix     case beforeSuffix     case afterSuffix } ``` |

Modified [CFNumberFormatterPadPosition.afterPrefix](https://developer.apple.com/documentation/corefoundation/cfnumberformatterpadposition/afterprefix)

|  | Declaration |
| --- | --- |
| From | ``` case AfterPrefix ``` |
| To | ``` case afterPrefix ``` |

Modified [CFNumberFormatterPadPosition.afterSuffix](https://developer.apple.com/documentation/corefoundation/cfnumberformatterpadposition/aftersuffix)

|  | Declaration |
| --- | --- |
| From | ``` case AfterSuffix ``` |
| To | ``` case afterSuffix ``` |

Modified [CFNumberFormatterPadPosition.beforePrefix](https://developer.apple.com/documentation/corefoundation/cfnumberformatterpadposition/kcfnumberformatterpadbeforeprefix)

|  | Declaration |
| --- | --- |
| From | ``` case BeforePrefix ``` |
| To | ``` case beforePrefix ``` |

Modified [CFNumberFormatterPadPosition.beforeSuffix](https://developer.apple.com/documentation/corefoundation/cfnumberformatterpadposition/beforesuffix)

|  | Declaration |
| --- | --- |
| From | ``` case BeforeSuffix ``` |
| To | ``` case beforeSuffix ``` |

Modified [CFNumberFormatterRoundingMode [enum]](https://developer.apple.com/documentation/corefoundation/cfnumberformatterroundingmode)

|  | Declaration |
| --- | --- |
| From | ``` enum CFNumberFormatterRoundingMode : CFIndex {     case RoundCeiling     case RoundFloor     case RoundDown     case RoundUp     case RoundHalfEven     case RoundHalfDown     case RoundHalfUp } ``` |
| To | ``` enum CFNumberFormatterRoundingMode : CFIndex {     case roundCeiling     case roundFloor     case roundDown     case roundUp     case roundHalfEven     case roundHalfDown     case roundHalfUp } ``` |

Modified [CFNumberFormatterRoundingMode.roundCeiling](https://developer.apple.com/documentation/corefoundation/cfnumberformatterroundingmode/kcfnumberformatterroundceiling)

|  | Declaration |
| --- | --- |
| From | ``` case RoundCeiling ``` |
| To | ``` case roundCeiling ``` |

Modified [CFNumberFormatterRoundingMode.roundDown](https://developer.apple.com/documentation/corefoundation/cfnumberformatterroundingmode/rounddown)

|  | Declaration |
| --- | --- |
| From | ``` case RoundDown ``` |
| To | ``` case roundDown ``` |

Modified [CFNumberFormatterRoundingMode.roundFloor](https://developer.apple.com/documentation/corefoundation/cfnumberformatterroundingmode/kcfnumberformatterroundfloor)

|  | Declaration |
| --- | --- |
| From | ``` case RoundFloor ``` |
| To | ``` case roundFloor ``` |

Modified [CFNumberFormatterRoundingMode.roundHalfDown](https://developer.apple.com/documentation/corefoundation/cfnumberformatterroundingmode/kcfnumberformatterroundhalfdown)

|  | Declaration |
| --- | --- |
| From | ``` case RoundHalfDown ``` |
| To | ``` case roundHalfDown ``` |

Modified [CFNumberFormatterRoundingMode.roundHalfEven](https://developer.apple.com/documentation/corefoundation/cfnumberformatterroundingmode/kcfnumberformatterroundhalfeven)

|  | Declaration |
| --- | --- |
| From | ``` case RoundHalfEven ``` |
| To | ``` case roundHalfEven ``` |

Modified [CFNumberFormatterRoundingMode.roundHalfUp](https://developer.apple.com/documentation/corefoundation/cfnumberformatterroundingmode/roundhalfup)

|  | Declaration |
| --- | --- |
| From | ``` case RoundHalfUp ``` |
| To | ``` case roundHalfUp ``` |

Modified [CFNumberFormatterRoundingMode.roundUp](https://developer.apple.com/documentation/corefoundation/cfnumberformatterroundingmode/roundup)

|  | Declaration |
| --- | --- |
| From | ``` case RoundUp ``` |
| To | ``` case roundUp ``` |

Modified [CFNumberFormatterStyle [enum]](https://developer.apple.com/documentation/corefoundation/cfnumberformatterstyle)

|  | Declaration |
| --- | --- |
| From | ``` enum CFNumberFormatterStyle : CFIndex {     case NoStyle     case DecimalStyle     case CurrencyStyle     case PercentStyle     case ScientificStyle     case SpellOutStyle     case OrdinalStyle     case CurrencyISOCodeStyle     case CurrencyPluralStyle     case CurrencyAccountingStyle } ``` |
| To | ``` enum CFNumberFormatterStyle : CFIndex {     case noStyle     case decimalStyle     case currencyStyle     case percentStyle     case scientificStyle     case spellOutStyle     case ordinalStyle     case currencyISOCodeStyle     case currencyPluralStyle     case currencyAccountingStyle } ``` |

Modified [CFNumberFormatterStyle.currencyAccountingStyle](https://developer.apple.com/documentation/corefoundation/cfnumberformatterstyle/currencyaccountingstyle)

|  | Declaration |
| --- | --- |
| From | ``` case CurrencyAccountingStyle ``` |
| To | ``` case currencyAccountingStyle ``` |

Modified [CFNumberFormatterStyle.currencyISOCodeStyle](https://developer.apple.com/documentation/corefoundation/cfnumberformatterstyle/kcfnumberformattercurrencyisocodestyle)

|  | Declaration |
| --- | --- |
| From | ``` case CurrencyISOCodeStyle ``` |
| To | ``` case currencyISOCodeStyle ``` |

Modified [CFNumberFormatterStyle.currencyPluralStyle](https://developer.apple.com/documentation/corefoundation/cfnumberformatterstyle/currencypluralstyle)

|  | Declaration |
| --- | --- |
| From | ``` case CurrencyPluralStyle ``` |
| To | ``` case currencyPluralStyle ``` |

Modified [CFNumberFormatterStyle.currencyStyle](https://developer.apple.com/documentation/corefoundation/cfnumberformatterstyle/kcfnumberformattercurrencystyle)

|  | Declaration |
| --- | --- |
| From | ``` case CurrencyStyle ``` |
| To | ``` case currencyStyle ``` |

Modified [CFNumberFormatterStyle.decimalStyle](https://developer.apple.com/documentation/corefoundation/cfnumberformatterstyle/decimalstyle)

|  | Declaration |
| --- | --- |
| From | ``` case DecimalStyle ``` |
| To | ``` case decimalStyle ``` |

Modified [CFNumberFormatterStyle.noStyle](https://developer.apple.com/documentation/corefoundation/cfnumberformatterstyle/kcfnumberformatternostyle)

|  | Declaration |
| --- | --- |
| From | ``` case NoStyle ``` |
| To | ``` case noStyle ``` |

Modified [CFNumberFormatterStyle.ordinalStyle](https://developer.apple.com/documentation/corefoundation/cfnumberformatterstyle/ordinalstyle)

|  | Declaration |
| --- | --- |
| From | ``` case OrdinalStyle ``` |
| To | ``` case ordinalStyle ``` |

Modified [CFNumberFormatterStyle.percentStyle](https://developer.apple.com/documentation/corefoundation/cfnumberformatterstyle/kcfnumberformatterpercentstyle)

|  | Declaration |
| --- | --- |
| From | ``` case PercentStyle ``` |
| To | ``` case percentStyle ``` |

Modified [CFNumberFormatterStyle.scientificStyle](https://developer.apple.com/documentation/corefoundation/cfnumberformatterstyle/scientificstyle)

|  | Declaration |
| --- | --- |
| From | ``` case ScientificStyle ``` |
| To | ``` case scientificStyle ``` |

Modified [CFNumberFormatterStyle.spellOutStyle](https://developer.apple.com/documentation/corefoundation/cfnumberformatterstyle/kcfnumberformatterspelloutstyle)

|  | Declaration |
| --- | --- |
| From | ``` case SpellOutStyle ``` |
| To | ``` case spellOutStyle ``` |

Modified [CFNumberType [enum]](https://developer.apple.com/documentation/corefoundation/cfnumbertype)

|  | Declaration |
| --- | --- |
| From | ``` enum CFNumberType : CFIndex {     case SInt8Type     case SInt16Type     case SInt32Type     case SInt64Type     case Float32Type     case Float64Type     case CharType     case ShortType     case IntType     case LongType     case LongLongType     case FloatType     case DoubleType     case CFIndexType     case NSIntegerType     case CGFloatType     static var MaxType: CFNumberType { get } } ``` |
| To | ``` enum CFNumberType : CFIndex {     case sInt8Type     case sInt16Type     case sInt32Type     case sInt64Type     case float32Type     case float64Type     case charType     case shortType     case intType     case longType     case longLongType     case floatType     case doubleType     case cfIndexType     case nsIntegerType     case cgFloatType     static var maxType: CFNumberType { get } } ``` |

Modified [CFNumberType.cfIndexType](https://developer.apple.com/documentation/corefoundation/cfnumbertype/kcfnumbercfindextype)

|  | Declaration |
| --- | --- |
| From | ``` case CFIndexType ``` |
| To | ``` case cfIndexType ``` |

Modified [CFNumberType.cgFloatType](https://developer.apple.com/documentation/corefoundation/cfnumbertype/kcfnumbercgfloattype)

|  | Declaration |
| --- | --- |
| From | ``` case CGFloatType ``` |
| To | ``` case cgFloatType ``` |

Modified [CFNumberType.charType](https://developer.apple.com/documentation/corefoundation/cfnumbertype/chartype)

|  | Declaration |
| --- | --- |
| From | ``` case CharType ``` |
| To | ``` case charType ``` |

Modified [CFNumberType.doubleType](https://developer.apple.com/documentation/corefoundation/cfnumbertype/kcfnumberdoubletype)

|  | Declaration |
| --- | --- |
| From | ``` case DoubleType ``` |
| To | ``` case doubleType ``` |

Modified [CFNumberType.float32Type](https://developer.apple.com/documentation/corefoundation/cfnumbertype/kcfnumberfloat32type)

|  | Declaration |
| --- | --- |
| From | ``` case Float32Type ``` |
| To | ``` case float32Type ``` |

Modified [CFNumberType.float64Type](https://developer.apple.com/documentation/corefoundation/cfnumbertype/float64type)

|  | Declaration |
| --- | --- |
| From | ``` case Float64Type ``` |
| To | ``` case float64Type ``` |

Modified [CFNumberType.floatType](https://developer.apple.com/documentation/corefoundation/cfnumbertype/kcfnumberfloattype)

|  | Declaration |
| --- | --- |
| From | ``` case FloatType ``` |
| To | ``` case floatType ``` |

Modified [CFNumberType.intType](https://developer.apple.com/documentation/corefoundation/cfnumbertype/inttype)

|  | Declaration |
| --- | --- |
| From | ``` case IntType ``` |
| To | ``` case intType ``` |

Modified [CFNumberType.longLongType](https://developer.apple.com/documentation/corefoundation/cfnumbertype/longlongtype)

|  | Declaration |
| --- | --- |
| From | ``` case LongLongType ``` |
| To | ``` case longLongType ``` |

Modified [CFNumberType.longType](https://developer.apple.com/documentation/corefoundation/cfnumbertype/kcfnumberlongtype)

|  | Declaration |
| --- | --- |
| From | ``` case LongType ``` |
| To | ``` case longType ``` |

Modified [CFNumberType.maxType](https://developer.apple.com/documentation/corefoundation/cfnumbertype/kcfnumbermaxtype)

|  | Declaration |
| --- | --- |
| From | ``` static var MaxType: CFNumberType { get } ``` |
| To | ``` static var maxType: CFNumberType { get } ``` |

Modified [CFNumberType.nsIntegerType](https://developer.apple.com/documentation/corefoundation/cfnumbertype/nsintegertype)

|  | Declaration |
| --- | --- |
| From | ``` case NSIntegerType ``` |
| To | ``` case nsIntegerType ``` |

Modified [CFNumberType.shortType](https://developer.apple.com/documentation/corefoundation/cfnumbertype/kcfnumbershorttype)

|  | Declaration |
| --- | --- |
| From | ``` case ShortType ``` |
| To | ``` case shortType ``` |

Modified [CFNumberType.sInt16Type](https://developer.apple.com/documentation/corefoundation/cfnumbertype/sint16type)

|  | Declaration |
| --- | --- |
| From | ``` case SInt16Type ``` |
| To | ``` case sInt16Type ``` |

Modified [CFNumberType.sInt32Type](https://developer.apple.com/documentation/corefoundation/cfnumbertype/sint32type)

|  | Declaration |
| --- | --- |
| From | ``` case SInt32Type ``` |
| To | ``` case sInt32Type ``` |

Modified [CFNumberType.sInt64Type](https://developer.apple.com/documentation/corefoundation/cfnumbertype/sint64type)

|  | Declaration |
| --- | --- |
| From | ``` case SInt64Type ``` |
| To | ``` case sInt64Type ``` |

Modified [CFNumberType.sInt8Type](https://developer.apple.com/documentation/corefoundation/cfnumbertype/kcfnumbersint8type)

|  | Declaration |
| --- | --- |
| From | ``` case SInt8Type ``` |
| To | ``` case sInt8Type ``` |

Modified [CFPropertyListFormat [enum]](https://developer.apple.com/documentation/corefoundation/cfpropertylistformat)

|  | Declaration |
| --- | --- |
| From | ``` enum CFPropertyListFormat : CFIndex {     case OpenStepFormat     case XMLFormat_v1_0     case BinaryFormat_v1_0 } ``` |
| To | ``` enum CFPropertyListFormat : CFIndex {     case openStepFormat     case xmlFormat_v1_0     case binaryFormat_v1_0 } ``` |

Modified [CFPropertyListFormat.binaryFormat_v1_0](https://developer.apple.com/documentation/corefoundation/cfpropertylistformat/kcfpropertylistbinaryformat_v1_0)

|  | Declaration |
| --- | --- |
| From | ``` case BinaryFormat_v1_0 ``` |
| To | ``` case binaryFormat_v1_0 ``` |

Modified [CFPropertyListFormat.openStepFormat](https://developer.apple.com/documentation/corefoundation/cfpropertylistformat/kcfpropertylistopenstepformat)

|  | Declaration |
| --- | --- |
| From | ``` case OpenStepFormat ``` |
| To | ``` case openStepFormat ``` |

Modified [CFPropertyListFormat.xmlFormat_v1_0](https://developer.apple.com/documentation/corefoundation/cfpropertylistformat/xmlformat_v1_0)

|  | Declaration |
| --- | --- |
| From | ``` case XMLFormat_v1_0 ``` |
| To | ``` case xmlFormat_v1_0 ``` |

Modified [CFPropertyListMutabilityOptions [struct]](https://developer.apple.com/documentation/corefoundation/cfpropertylistmutabilityoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFPropertyListMutabilityOptions : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var Immutable: CFPropertyListMutabilityOptions { get }     static var MutableContainers: CFPropertyListMutabilityOptions { get }     static var MutableContainersAndLeaves: CFPropertyListMutabilityOptions { get } } ``` | OptionSetType |
| To | ``` struct CFPropertyListMutabilityOptions : OptionSet {     init(rawValue rawValue: CFOptionFlags)     static var immutable: CFPropertyListMutabilityOptions { get }     static var mutableContainers: CFPropertyListMutabilityOptions { get }     static var mutableContainersAndLeaves: CFPropertyListMutabilityOptions { get }     func intersect(_ other: CFPropertyListMutabilityOptions) -> CFPropertyListMutabilityOptions     func exclusiveOr(_ other: CFPropertyListMutabilityOptions) -> CFPropertyListMutabilityOptions     mutating func unionInPlace(_ other: CFPropertyListMutabilityOptions)     mutating func intersectInPlace(_ other: CFPropertyListMutabilityOptions)     mutating func exclusiveOrInPlace(_ other: CFPropertyListMutabilityOptions)     func isSubsetOf(_ other: CFPropertyListMutabilityOptions) -> Bool     func isDisjointWith(_ other: CFPropertyListMutabilityOptions) -> Bool     func isSupersetOf(_ other: CFPropertyListMutabilityOptions) -> Bool     mutating func subtractInPlace(_ other: CFPropertyListMutabilityOptions)     func isStrictSupersetOf(_ other: CFPropertyListMutabilityOptions) -> Bool     func isStrictSubsetOf(_ other: CFPropertyListMutabilityOptions) -> Bool } extension CFPropertyListMutabilityOptions {     func union(_ other: CFPropertyListMutabilityOptions) -> CFPropertyListMutabilityOptions     func intersection(_ other: CFPropertyListMutabilityOptions) -> CFPropertyListMutabilityOptions     func symmetricDifference(_ other: CFPropertyListMutabilityOptions) -> CFPropertyListMutabilityOptions } extension CFPropertyListMutabilityOptions {     func contains(_ member: CFPropertyListMutabilityOptions) -> Bool     mutating func insert(_ newMember: CFPropertyListMutabilityOptions) -> (inserted: Bool, memberAfterInsert: CFPropertyListMutabilityOptions)     mutating func remove(_ member: CFPropertyListMutabilityOptions) -> CFPropertyListMutabilityOptions?     mutating func update(with newMember: CFPropertyListMutabilityOptions) -> CFPropertyListMutabilityOptions? } extension CFPropertyListMutabilityOptions {     convenience init()     mutating func formUnion(_ other: CFPropertyListMutabilityOptions)     mutating func formIntersection(_ other: CFPropertyListMutabilityOptions)     mutating func formSymmetricDifference(_ other: CFPropertyListMutabilityOptions) } extension CFPropertyListMutabilityOptions {     convenience init<S : Sequence where S.Iterator.Element == CFPropertyListMutabilityOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CFPropertyListMutabilityOptions...)     mutating func subtract(_ other: CFPropertyListMutabilityOptions)     func isSubset(of other: CFPropertyListMutabilityOptions) -> Bool     func isSuperset(of other: CFPropertyListMutabilityOptions) -> Bool     func isDisjoint(with other: CFPropertyListMutabilityOptions) -> Bool     func subtracting(_ other: CFPropertyListMutabilityOptions) -> CFPropertyListMutabilityOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: CFPropertyListMutabilityOptions) -> Bool     func isStrictSubset(of other: CFPropertyListMutabilityOptions) -> Bool } ``` | OptionSet |

Modified [CFPropertyListMutabilityOptions.mutableContainers](https://developer.apple.com/documentation/corefoundation/cfpropertylistmutabilityoptions/1430003-mutablecontainers)

|  | Declaration |
| --- | --- |
| From | ``` static var MutableContainers: CFPropertyListMutabilityOptions { get } ``` |
| To | ``` static var mutableContainers: CFPropertyListMutabilityOptions { get } ``` |

Modified [CFPropertyListMutabilityOptions.mutableContainersAndLeaves](https://developer.apple.com/documentation/corefoundation/cfpropertylistmutabilityoptions/kcfpropertylistmutablecontainersandleaves)

|  | Declaration |
| --- | --- |
| From | ``` static var MutableContainersAndLeaves: CFPropertyListMutabilityOptions { get } ``` |
| To | ``` static var mutableContainersAndLeaves: CFPropertyListMutabilityOptions { get } ``` |

Modified [CFRunLoopActivity [struct]](https://developer.apple.com/documentation/corefoundation/cfrunloopactivity)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFRunLoopActivity : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var Entry: CFRunLoopActivity { get }     static var BeforeTimers: CFRunLoopActivity { get }     static var BeforeSources: CFRunLoopActivity { get }     static var BeforeWaiting: CFRunLoopActivity { get }     static var AfterWaiting: CFRunLoopActivity { get }     static var Exit: CFRunLoopActivity { get }     static var AllActivities: CFRunLoopActivity { get } } ``` | OptionSetType |
| To | ``` struct CFRunLoopActivity : OptionSet {     init(rawValue rawValue: CFOptionFlags)     static var entry: CFRunLoopActivity { get }     static var beforeTimers: CFRunLoopActivity { get }     static var beforeSources: CFRunLoopActivity { get }     static var beforeWaiting: CFRunLoopActivity { get }     static var afterWaiting: CFRunLoopActivity { get }     static var exit: CFRunLoopActivity { get }     static var allActivities: CFRunLoopActivity { get }     func intersect(_ other: CFRunLoopActivity) -> CFRunLoopActivity     func exclusiveOr(_ other: CFRunLoopActivity) -> CFRunLoopActivity     mutating func unionInPlace(_ other: CFRunLoopActivity)     mutating func intersectInPlace(_ other: CFRunLoopActivity)     mutating func exclusiveOrInPlace(_ other: CFRunLoopActivity)     func isSubsetOf(_ other: CFRunLoopActivity) -> Bool     func isDisjointWith(_ other: CFRunLoopActivity) -> Bool     func isSupersetOf(_ other: CFRunLoopActivity) -> Bool     mutating func subtractInPlace(_ other: CFRunLoopActivity)     func isStrictSupersetOf(_ other: CFRunLoopActivity) -> Bool     func isStrictSubsetOf(_ other: CFRunLoopActivity) -> Bool } extension CFRunLoopActivity {     func union(_ other: CFRunLoopActivity) -> CFRunLoopActivity     func intersection(_ other: CFRunLoopActivity) -> CFRunLoopActivity     func symmetricDifference(_ other: CFRunLoopActivity) -> CFRunLoopActivity } extension CFRunLoopActivity {     func contains(_ member: CFRunLoopActivity) -> Bool     mutating func insert(_ newMember: CFRunLoopActivity) -> (inserted: Bool, memberAfterInsert: CFRunLoopActivity)     mutating func remove(_ member: CFRunLoopActivity) -> CFRunLoopActivity?     mutating func update(with newMember: CFRunLoopActivity) -> CFRunLoopActivity? } extension CFRunLoopActivity {     convenience init()     mutating func formUnion(_ other: CFRunLoopActivity)     mutating func formIntersection(_ other: CFRunLoopActivity)     mutating func formSymmetricDifference(_ other: CFRunLoopActivity) } extension CFRunLoopActivity {     convenience init<S : Sequence where S.Iterator.Element == CFRunLoopActivity>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CFRunLoopActivity...)     mutating func subtract(_ other: CFRunLoopActivity)     func isSubset(of other: CFRunLoopActivity) -> Bool     func isSuperset(of other: CFRunLoopActivity) -> Bool     func isDisjoint(with other: CFRunLoopActivity) -> Bool     func subtracting(_ other: CFRunLoopActivity) -> CFRunLoopActivity     var isEmpty: Bool { get }     func isStrictSuperset(of other: CFRunLoopActivity) -> Bool     func isStrictSubset(of other: CFRunLoopActivity) -> Bool } ``` | OptionSet |

Modified [CFRunLoopActivity.afterWaiting](https://developer.apple.com/documentation/corefoundation/cfrunloopactivity/1541980-afterwaiting)

|  | Declaration |
| --- | --- |
| From | ``` static var AfterWaiting: CFRunLoopActivity { get } ``` |
| To | ``` static var afterWaiting: CFRunLoopActivity { get } ``` |

Modified [CFRunLoopActivity.allActivities](https://developer.apple.com/documentation/corefoundation/cfrunloopactivity/kcfrunloopallactivities)

|  | Declaration |
| --- | --- |
| From | ``` static var AllActivities: CFRunLoopActivity { get } ``` |
| To | ``` static var allActivities: CFRunLoopActivity { get } ``` |

Modified [CFRunLoopActivity.beforeSources](https://developer.apple.com/documentation/corefoundation/cfrunloopactivity/kcfrunloopbeforesources)

|  | Declaration |
| --- | --- |
| From | ``` static var BeforeSources: CFRunLoopActivity { get } ``` |
| To | ``` static var beforeSources: CFRunLoopActivity { get } ``` |

Modified [CFRunLoopActivity.beforeTimers](https://developer.apple.com/documentation/corefoundation/cfrunloopactivity/kcfrunloopbeforetimers)

|  | Declaration |
| --- | --- |
| From | ``` static var BeforeTimers: CFRunLoopActivity { get } ``` |
| To | ``` static var beforeTimers: CFRunLoopActivity { get } ``` |

Modified [CFRunLoopActivity.beforeWaiting](https://developer.apple.com/documentation/corefoundation/cfrunloopactivity/1543144-beforewaiting)

|  | Declaration |
| --- | --- |
| From | ``` static var BeforeWaiting: CFRunLoopActivity { get } ``` |
| To | ``` static var beforeWaiting: CFRunLoopActivity { get } ``` |

Modified [CFRunLoopActivity.entry](https://developer.apple.com/documentation/corefoundation/cfrunloopactivity/kcfrunloopentry)

|  | Declaration |
| --- | --- |
| From | ``` static var Entry: CFRunLoopActivity { get } ``` |
| To | ``` static var entry: CFRunLoopActivity { get } ``` |

Modified [CFRunLoopActivity.exit](https://developer.apple.com/documentation/corefoundation/cfrunloopactivity/1543656-exit)

|  | Declaration |
| --- | --- |
| From | ``` static var Exit: CFRunLoopActivity { get } ``` |
| To | ``` static var exit: CFRunLoopActivity { get } ``` |

Modified [CFRunLoopMode.commonModes](https://developer.apple.com/documentation/corefoundation/cfrunloopmode/1542364-commonmodes)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFRunLoopCommonModes | ``` let kCFRunLoopCommonModes: CFString! ``` |
| To | commonModes | ``` static let commonModes: CFRunLoopMode! ``` |

Modified [CFRunLoopMode.defaultMode](https://developer.apple.com/documentation/corefoundation/kcfrunloopdefaultmode)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFRunLoopDefaultMode | ``` let kCFRunLoopDefaultMode: CFString! ``` |
| To | defaultMode | ``` static let defaultMode: CFRunLoopMode! ``` |

Modified [CFRunLoopObserverContext [struct]](https://developer.apple.com/documentation/corefoundation/cfrunloopobservercontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFRunLoopObserverContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!     var release: ((UnsafePointer<Void>) -> Void)!     var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release release: ((UnsafePointer<Void>) -> Void)!, copyDescription copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!) } ``` |
| To | ``` struct CFRunLoopObserverContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!) } ``` |

Modified [CFRunLoopObserverContext.copyDescription](https://developer.apple.com/documentation/corefoundation/cfrunloopobservercontext/1541528-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)! ``` |
| To | ``` var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)! ``` |

Modified [CFRunLoopObserverContext.info](https://developer.apple.com/documentation/corefoundation/cfrunloopobservercontext/1541896-info)

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafeMutablePointer<Void> ``` |
| To | ``` var info: UnsafeMutableRawPointer! ``` |

Modified [CFRunLoopObserverContext.release](https://developer.apple.com/documentation/corefoundation/cfrunloopobservercontext/1542732-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: ((UnsafePointer<Void>) -> Void)! ``` |
| To | ``` var release: ((UnsafeRawPointer?) -> Swift.Void)! ``` |

Modified [CFRunLoopObserverContext.retain](https://developer.apple.com/documentation/corefoundation/cfrunloopobservercontext/1541985-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)! ``` |
| To | ``` var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)! ``` |

Modified [CFRunLoopRunResult [enum]](https://developer.apple.com/documentation/corefoundation/cfrunlooprunresult)

|  | Declaration |
| --- | --- |
| From | ``` enum CFRunLoopRunResult : Int32 {     case Finished     case Stopped     case TimedOut     case HandledSource } ``` |
| To | ``` enum CFRunLoopRunResult : Int32 {     case finished     case stopped     case timedOut     case handledSource } ``` |

Modified [CFRunLoopRunResult.finished](https://developer.apple.com/documentation/corefoundation/cfrunlooprunresult/kcfrunlooprunfinished)

|  | Declaration |
| --- | --- |
| From | ``` case Finished ``` |
| To | ``` case finished ``` |

Modified [CFRunLoopRunResult.handledSource](https://developer.apple.com/documentation/corefoundation/cfrunlooprunresult/kcfrunlooprunhandledsource)

|  | Declaration |
| --- | --- |
| From | ``` case HandledSource ``` |
| To | ``` case handledSource ``` |

Modified [CFRunLoopRunResult.stopped](https://developer.apple.com/documentation/corefoundation/cfrunlooprunresult/stopped)

|  | Declaration |
| --- | --- |
| From | ``` case Stopped ``` |
| To | ``` case stopped ``` |

Modified [CFRunLoopRunResult.timedOut](https://developer.apple.com/documentation/corefoundation/cfrunlooprunresult/timedout)

|  | Declaration |
| --- | --- |
| From | ``` case TimedOut ``` |
| To | ``` case timedOut ``` |

Modified [CFRunLoopSourceContext [struct]](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFRunLoopSourceContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!     var release: ((UnsafePointer<Void>) -> Void)!     var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!     var equal: ((UnsafePointer<Void>, UnsafePointer<Void>) -> DarwinBoolean)!     var hash: ((UnsafePointer<Void>) -> CFHashCode)!     var schedule: ((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)!     var cancel: ((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)!     var perform: ((UnsafeMutablePointer<Void>) -> Void)!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release release: ((UnsafePointer<Void>) -> Void)!, copyDescription copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!, equal equal: ((UnsafePointer<Void>, UnsafePointer<Void>) -> DarwinBoolean)!, hash hash: ((UnsafePointer<Void>) -> CFHashCode)!, schedule schedule: ((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)!, cancel cancel: ((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)!, perform perform: ((UnsafeMutablePointer<Void>) -> Void)!) } ``` |
| To | ``` struct CFRunLoopSourceContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     var equal: ((UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!     var hash: ((UnsafeRawPointer?) -> CFHashCode)!     var schedule: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Swift.Void)!     var cancel: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Swift.Void)!     var perform: ((UnsafeMutableRawPointer?) -> Swift.Void)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!, equal equal: (@escaping (UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!, hash hash: (@escaping (UnsafeRawPointer?) -> CFHashCode)!, schedule schedule: (@escaping (UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Swift.Void)!, cancel cancel: (@escaping (UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Swift.Void)!, perform perform: (@escaping (UnsafeMutableRawPointer?) -> Swift.Void)!) } ``` |

Modified [CFRunLoopSourceContext.cancel](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext/1541753-cancel)

|  | Declaration |
| --- | --- |
| From | ``` var cancel: ((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)! ``` |
| To | ``` var cancel: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Swift.Void)! ``` |

Modified [CFRunLoopSourceContext.copyDescription](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext/1542769-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)! ``` |
| To | ``` var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)! ``` |

Modified [CFRunLoopSourceContext.equal](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext/1543639-equal)

|  | Declaration |
| --- | --- |
| From | ``` var equal: ((UnsafePointer<Void>, UnsafePointer<Void>) -> DarwinBoolean)! ``` |
| To | ``` var equal: ((UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)! ``` |

Modified [CFRunLoopSourceContext.hash](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext/1543398-hash)

|  | Declaration |
| --- | --- |
| From | ``` var hash: ((UnsafePointer<Void>) -> CFHashCode)! ``` |
| To | ``` var hash: ((UnsafeRawPointer?) -> CFHashCode)! ``` |

Modified [CFRunLoopSourceContext.info](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext/1542099-info)

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafeMutablePointer<Void> ``` |
| To | ``` var info: UnsafeMutableRawPointer! ``` |

Modified [CFRunLoopSourceContext.perform](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext/1541994-perform)

|  | Declaration |
| --- | --- |
| From | ``` var perform: ((UnsafeMutablePointer<Void>) -> Void)! ``` |
| To | ``` var perform: ((UnsafeMutableRawPointer?) -> Swift.Void)! ``` |

Modified [CFRunLoopSourceContext.release](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext/1542971-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: ((UnsafePointer<Void>) -> Void)! ``` |
| To | ``` var release: ((UnsafeRawPointer?) -> Swift.Void)! ``` |

Modified [CFRunLoopSourceContext.retain](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext/1543359-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)! ``` |
| To | ``` var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)! ``` |

Modified [CFRunLoopSourceContext.schedule](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext/1542029-schedule)

|  | Declaration |
| --- | --- |
| From | ``` var schedule: ((UnsafeMutablePointer<Void>, CFRunLoop!, CFString!) -> Void)! ``` |
| To | ``` var schedule: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Swift.Void)! ``` |

Modified [CFRunLoopSourceContext1 [struct]](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1)

|  | Declaration |
| --- | --- |
| From | ``` struct CFRunLoopSourceContext1 {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!     var release: ((UnsafePointer<Void>) -> Void)!     var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!     var equal: ((UnsafePointer<Void>, UnsafePointer<Void>) -> DarwinBoolean)!     var hash: ((UnsafePointer<Void>) -> CFHashCode)!     var getPort: ((UnsafeMutablePointer<Void>) -> mach_port_t)!     var perform: ((UnsafeMutablePointer<Void>, CFIndex, CFAllocator!, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release release: ((UnsafePointer<Void>) -> Void)!, copyDescription copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!, equal equal: ((UnsafePointer<Void>, UnsafePointer<Void>) -> DarwinBoolean)!, hash hash: ((UnsafePointer<Void>) -> CFHashCode)!, getPort getPort: ((UnsafeMutablePointer<Void>) -> mach_port_t)!, perform perform: ((UnsafeMutablePointer<Void>, CFIndex, CFAllocator!, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)!) } ``` |
| To | ``` struct CFRunLoopSourceContext1 {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     var equal: ((UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!     var hash: ((UnsafeRawPointer?) -> CFHashCode)!     var getPort: ((UnsafeMutableRawPointer?) -> mach_port_t)!     var perform: ((UnsafeMutableRawPointer?, CFIndex, CFAllocator?, UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!, equal equal: (@escaping (UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!, hash hash: (@escaping (UnsafeRawPointer?) -> CFHashCode)!, getPort getPort: (@escaping (UnsafeMutableRawPointer?) -> mach_port_t)!, perform perform: (@escaping (UnsafeMutableRawPointer?, CFIndex, CFAllocator?, UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!) } ``` |

Modified [CFRunLoopSourceContext1.copyDescription](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1/1542892-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)! ``` |
| To | ``` var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)! ``` |

Modified [CFRunLoopSourceContext1.equal](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1/1542103-equal)

|  | Declaration |
| --- | --- |
| From | ``` var equal: ((UnsafePointer<Void>, UnsafePointer<Void>) -> DarwinBoolean)! ``` |
| To | ``` var equal: ((UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)! ``` |

Modified [CFRunLoopSourceContext1.getPort](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1/1542846-getport)

|  | Declaration |
| --- | --- |
| From | ``` var getPort: ((UnsafeMutablePointer<Void>) -> mach_port_t)! ``` |
| To | ``` var getPort: ((UnsafeMutableRawPointer?) -> mach_port_t)! ``` |

Modified [CFRunLoopSourceContext1.hash](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1/1543040-hash)

|  | Declaration |
| --- | --- |
| From | ``` var hash: ((UnsafePointer<Void>) -> CFHashCode)! ``` |
| To | ``` var hash: ((UnsafeRawPointer?) -> CFHashCode)! ``` |

Modified [CFRunLoopSourceContext1.info](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1/1543248-info)

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafeMutablePointer<Void> ``` |
| To | ``` var info: UnsafeMutableRawPointer! ``` |

Modified [CFRunLoopSourceContext1.perform](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1/1543410-perform)

|  | Declaration |
| --- | --- |
| From | ``` var perform: ((UnsafeMutablePointer<Void>, CFIndex, CFAllocator!, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)! ``` |
| To | ``` var perform: ((UnsafeMutableRawPointer?, CFIndex, CFAllocator?, UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)! ``` |

Modified [CFRunLoopSourceContext1.release](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1/1542161-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: ((UnsafePointer<Void>) -> Void)! ``` |
| To | ``` var release: ((UnsafeRawPointer?) -> Swift.Void)! ``` |

Modified [CFRunLoopSourceContext1.retain](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1/1542518-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)! ``` |
| To | ``` var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)! ``` |

Modified [CFRunLoopTimerContext [struct]](https://developer.apple.com/documentation/corefoundation/cfrunlooptimercontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFRunLoopTimerContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!     var release: ((UnsafePointer<Void>) -> Void)!     var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release release: ((UnsafePointer<Void>) -> Void)!, copyDescription copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!) } ``` |
| To | ``` struct CFRunLoopTimerContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!) } ``` |

Modified [CFRunLoopTimerContext.copyDescription](https://developer.apple.com/documentation/corefoundation/cfrunlooptimercontext/1541599-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)! ``` |
| To | ``` var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)! ``` |

Modified [CFRunLoopTimerContext.info](https://developer.apple.com/documentation/corefoundation/cfrunlooptimercontext/1542937-info)

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafeMutablePointer<Void> ``` |
| To | ``` var info: UnsafeMutableRawPointer! ``` |

Modified [CFRunLoopTimerContext.release](https://developer.apple.com/documentation/corefoundation/cfrunlooptimercontext/1542982-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: ((UnsafePointer<Void>) -> Void)! ``` |
| To | ``` var release: ((UnsafeRawPointer?) -> Swift.Void)! ``` |

Modified [CFRunLoopTimerContext.retain](https://developer.apple.com/documentation/corefoundation/cfrunlooptimercontext/1543444-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)! ``` |
| To | ``` var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)! ``` |

Modified [CFSetCallBacks [struct]](https://developer.apple.com/documentation/corefoundation/cfsetcallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CFSetCallBacks {     var version: CFIndex     var retain: CFSetRetainCallBack!     var release: CFSetReleaseCallBack!     var copyDescription: CFSetCopyDescriptionCallBack!     var equal: CFSetEqualCallBack!     var hash: CFSetHashCallBack!     init()     init(version version: CFIndex, retain retain: CFSetRetainCallBack!, release release: CFSetReleaseCallBack!, copyDescription copyDescription: CFSetCopyDescriptionCallBack!, equal equal: CFSetEqualCallBack!, hash hash: CFSetHashCallBack!) } ``` |
| To | ``` struct CFSetCallBacks {     var version: CFIndex     var retain: CoreFoundation.CFSetRetainCallBack!     var release: CoreFoundation.CFSetReleaseCallBack!     var copyDescription: CoreFoundation.CFSetCopyDescriptionCallBack!     var equal: CoreFoundation.CFSetEqualCallBack!     var hash: CoreFoundation.CFSetHashCallBack!     init()     init(version version: CFIndex, retain retain: CoreFoundation.CFSetRetainCallBack!, release release: CoreFoundation.CFSetReleaseCallBack!, copyDescription copyDescription: CoreFoundation.CFSetCopyDescriptionCallBack!, equal equal: CoreFoundation.CFSetEqualCallBack!, hash hash: CoreFoundation.CFSetHashCallBack!) } ``` |

Modified [CFSetCallBacks.copyDescription](https://developer.apple.com/documentation/corefoundation/cfsetcallbacks/1520442-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFSetCopyDescriptionCallBack! ``` |
| To | ``` var copyDescription: CoreFoundation.CFSetCopyDescriptionCallBack! ``` |

Modified [CFSetCallBacks.equal](https://developer.apple.com/documentation/corefoundation/cfsetcallbacks/1520421-equal)

|  | Declaration |
| --- | --- |
| From | ``` var equal: CFSetEqualCallBack! ``` |
| To | ``` var equal: CoreFoundation.CFSetEqualCallBack! ``` |

Modified [CFSetCallBacks.hash](https://developer.apple.com/documentation/corefoundation/cfsetcallbacks/1520417-hash)

|  | Declaration |
| --- | --- |
| From | ``` var hash: CFSetHashCallBack! ``` |
| To | ``` var hash: CoreFoundation.CFSetHashCallBack! ``` |

Modified [CFSetCallBacks.release](https://developer.apple.com/documentation/corefoundation/cfsetcallbacks/1520410-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFSetReleaseCallBack! ``` |
| To | ``` var release: CoreFoundation.CFSetReleaseCallBack! ``` |

Modified [CFSetCallBacks.retain](https://developer.apple.com/documentation/corefoundation/cfsetcallbacks/1520439-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFSetRetainCallBack! ``` |
| To | ``` var retain: CoreFoundation.CFSetRetainCallBack! ``` |

Modified [CFSocketCallBackType [struct]](https://developer.apple.com/documentation/corefoundation/cfsocketcallbacktype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFSocketCallBackType : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var NoCallBack: CFSocketCallBackType { get }     static var ReadCallBack: CFSocketCallBackType { get }     static var AcceptCallBack: CFSocketCallBackType { get }     static var DataCallBack: CFSocketCallBackType { get }     static var ConnectCallBack: CFSocketCallBackType { get }     static var WriteCallBack: CFSocketCallBackType { get } } ``` | OptionSetType |
| To | ``` struct CFSocketCallBackType : OptionSet {     init(rawValue rawValue: CFOptionFlags)     static var noCallBack: CFSocketCallBackType { get }     static var readCallBack: CFSocketCallBackType { get }     static var acceptCallBack: CFSocketCallBackType { get }     static var dataCallBack: CFSocketCallBackType { get }     static var connectCallBack: CFSocketCallBackType { get }     static var writeCallBack: CFSocketCallBackType { get }     func intersect(_ other: CFSocketCallBackType) -> CFSocketCallBackType     func exclusiveOr(_ other: CFSocketCallBackType) -> CFSocketCallBackType     mutating func unionInPlace(_ other: CFSocketCallBackType)     mutating func intersectInPlace(_ other: CFSocketCallBackType)     mutating func exclusiveOrInPlace(_ other: CFSocketCallBackType)     func isSubsetOf(_ other: CFSocketCallBackType) -> Bool     func isDisjointWith(_ other: CFSocketCallBackType) -> Bool     func isSupersetOf(_ other: CFSocketCallBackType) -> Bool     mutating func subtractInPlace(_ other: CFSocketCallBackType)     func isStrictSupersetOf(_ other: CFSocketCallBackType) -> Bool     func isStrictSubsetOf(_ other: CFSocketCallBackType) -> Bool } extension CFSocketCallBackType {     func union(_ other: CFSocketCallBackType) -> CFSocketCallBackType     func intersection(_ other: CFSocketCallBackType) -> CFSocketCallBackType     func symmetricDifference(_ other: CFSocketCallBackType) -> CFSocketCallBackType } extension CFSocketCallBackType {     func contains(_ member: CFSocketCallBackType) -> Bool     mutating func insert(_ newMember: CFSocketCallBackType) -> (inserted: Bool, memberAfterInsert: CFSocketCallBackType)     mutating func remove(_ member: CFSocketCallBackType) -> CFSocketCallBackType?     mutating func update(with newMember: CFSocketCallBackType) -> CFSocketCallBackType? } extension CFSocketCallBackType {     convenience init()     mutating func formUnion(_ other: CFSocketCallBackType)     mutating func formIntersection(_ other: CFSocketCallBackType)     mutating func formSymmetricDifference(_ other: CFSocketCallBackType) } extension CFSocketCallBackType {     convenience init<S : Sequence where S.Iterator.Element == CFSocketCallBackType>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CFSocketCallBackType...)     mutating func subtract(_ other: CFSocketCallBackType)     func isSubset(of other: CFSocketCallBackType) -> Bool     func isSuperset(of other: CFSocketCallBackType) -> Bool     func isDisjoint(with other: CFSocketCallBackType) -> Bool     func subtracting(_ other: CFSocketCallBackType) -> CFSocketCallBackType     var isEmpty: Bool { get }     func isStrictSuperset(of other: CFSocketCallBackType) -> Bool     func isStrictSubset(of other: CFSocketCallBackType) -> Bool } ``` | OptionSet |

Modified [CFSocketCallBackType.acceptCallBack](https://developer.apple.com/documentation/corefoundation/cfsocketcallbacktype/1541536-acceptcallback)

|  | Declaration |
| --- | --- |
| From | ``` static var AcceptCallBack: CFSocketCallBackType { get } ``` |
| To | ``` static var acceptCallBack: CFSocketCallBackType { get } ``` |

Modified [CFSocketCallBackType.connectCallBack](https://developer.apple.com/documentation/corefoundation/cfsocketcallbacktype/kcfsocketconnectcallback)

|  | Declaration |
| --- | --- |
| From | ``` static var ConnectCallBack: CFSocketCallBackType { get } ``` |
| To | ``` static var connectCallBack: CFSocketCallBackType { get } ``` |

Modified [CFSocketCallBackType.dataCallBack](https://developer.apple.com/documentation/corefoundation/cfsocketcallbacktype/kcfsocketdatacallback)

|  | Declaration |
| --- | --- |
| From | ``` static var DataCallBack: CFSocketCallBackType { get } ``` |
| To | ``` static var dataCallBack: CFSocketCallBackType { get } ``` |

Modified [CFSocketCallBackType.readCallBack](https://developer.apple.com/documentation/corefoundation/cfsocketcallbacktype/kcfsocketreadcallback)

|  | Declaration |
| --- | --- |
| From | ``` static var ReadCallBack: CFSocketCallBackType { get } ``` |
| To | ``` static var readCallBack: CFSocketCallBackType { get } ``` |

Modified [CFSocketCallBackType.writeCallBack](https://developer.apple.com/documentation/corefoundation/cfsocketcallbacktype/kcfsocketwritecallback)

|  | Declaration |
| --- | --- |
| From | ``` static var WriteCallBack: CFSocketCallBackType { get } ``` |
| To | ``` static var writeCallBack: CFSocketCallBackType { get } ``` |

Modified [CFSocketContext [struct]](https://developer.apple.com/documentation/corefoundation/cfsocketcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFSocketContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!     var release: ((UnsafePointer<Void>) -> Void)!     var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)!, release release: ((UnsafePointer<Void>) -> Void)!, copyDescription copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)!) } ``` |
| To | ``` struct CFSocketContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!     var release: ((UnsafeRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeRawPointer?) -> UnsafeRawPointer?)!, release release: (@escaping (UnsafeRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeRawPointer?) -> Unmanaged<CFString>?)!) } ``` |

Modified [CFSocketContext.copyDescription](https://developer.apple.com/documentation/corefoundation/cfsocketcontext/1542148-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>!)! ``` |
| To | ``` var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)! ``` |

Modified [CFSocketContext.info](https://developer.apple.com/documentation/corefoundation/cfsocketcontext/1542688-info)

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafeMutablePointer<Void> ``` |
| To | ``` var info: UnsafeMutableRawPointer! ``` |

Modified [CFSocketContext.release](https://developer.apple.com/documentation/corefoundation/cfsocketcontext/1541856-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: ((UnsafePointer<Void>) -> Void)! ``` |
| To | ``` var release: ((UnsafeRawPointer?) -> Swift.Void)! ``` |

Modified [CFSocketContext.retain](https://developer.apple.com/documentation/corefoundation/cfsocketcontext/1543095-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)! ``` |
| To | ``` var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)! ``` |

Modified [CFSocketError [enum]](https://developer.apple.com/documentation/corefoundation/cfsocketerror)

|  | Declaration |
| --- | --- |
| From | ``` enum CFSocketError : CFIndex {     case Success     case Error     case Timeout } ``` |
| To | ``` enum CFSocketError : CFIndex {     case success     case error     case timeout } ``` |

Modified [CFSocketError.error](https://developer.apple.com/documentation/corefoundation/cfsocketerror/error)

|  | Declaration |
| --- | --- |
| From | ``` case Error ``` |
| To | ``` case error ``` |

Modified [CFSocketError.success](https://developer.apple.com/documentation/corefoundation/cfsocketerror/success)

|  | Declaration |
| --- | --- |
| From | ``` case Success ``` |
| To | ``` case success ``` |

Modified [CFSocketError.timeout](https://developer.apple.com/documentation/corefoundation/cfsocketerror/kcfsockettimeout)

|  | Declaration |
| --- | --- |
| From | ``` case Timeout ``` |
| To | ``` case timeout ``` |

Modified [CFStreamClientContext [struct]](https://developer.apple.com/documentation/corefoundation/cfstreamclientcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFStreamClientContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)!     var release: ((UnsafeMutablePointer<Void>) -> Void)!     var copyDescription: ((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)!, release release: ((UnsafeMutablePointer<Void>) -> Void)!, copyDescription copyDescription: ((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)!) } ``` |
| To | ``` struct CFStreamClientContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: ((UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!     var release: ((UnsafeMutableRawPointer?) -> Swift.Void)!     var copyDescription: ((UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: (@escaping (UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!, release release: (@escaping (UnsafeMutableRawPointer?) -> Swift.Void)!, copyDescription copyDescription: (@escaping (UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!) } ``` |

Modified [CFStreamClientContext.copyDescription](https://developer.apple.com/documentation/corefoundation/cfstreamclientcontext/1539745-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: ((UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)! ``` |
| To | ``` var copyDescription: ((UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)! ``` |

Modified [CFStreamClientContext.info](https://developer.apple.com/documentation/corefoundation/cfstreamclientcontext/1539613-info)

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafeMutablePointer<Void> ``` |
| To | ``` var info: UnsafeMutableRawPointer! ``` |

Modified [CFStreamClientContext.release](https://developer.apple.com/documentation/corefoundation/cfstreamclientcontext/1539664-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: ((UnsafeMutablePointer<Void>) -> Void)! ``` |
| To | ``` var release: ((UnsafeMutableRawPointer?) -> Swift.Void)! ``` |

Modified [CFStreamClientContext.retain](https://developer.apple.com/documentation/corefoundation/cfstreamclientcontext/1539696-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: ((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)! ``` |
| To | ``` var retain: ((UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)! ``` |

Modified [CFStreamErrorDomain [enum]](https://developer.apple.com/documentation/corefoundation/cfstreamerrordomain)

|  | Declaration |
| --- | --- |
| From | ``` enum CFStreamErrorDomain : CFIndex {     case Custom     case POSIX     case MacOSStatus } ``` |
| To | ``` enum CFStreamErrorDomain : CFIndex {     case custom     case POSIX     case macOSStatus } ``` |

Modified [CFStreamErrorDomain.custom](https://developer.apple.com/documentation/corefoundation/cfstreamerrordomain/custom)

|  | Declaration |
| --- | --- |
| From | ``` case Custom ``` |
| To | ``` case custom ``` |

Modified [CFStreamErrorDomain.macOSStatus](https://developer.apple.com/documentation/corefoundation/cfstreamerrordomain/macosstatus)

|  | Declaration |
| --- | --- |
| From | ``` case MacOSStatus ``` |
| To | ``` case macOSStatus ``` |

Modified [CFStreamEventType [struct]](https://developer.apple.com/documentation/corefoundation/cfstreameventtype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFStreamEventType : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var None: CFStreamEventType { get }     static var OpenCompleted: CFStreamEventType { get }     static var HasBytesAvailable: CFStreamEventType { get }     static var CanAcceptBytes: CFStreamEventType { get }     static var ErrorOccurred: CFStreamEventType { get }     static var EndEncountered: CFStreamEventType { get } } ``` | OptionSetType |
| To | ``` struct CFStreamEventType : OptionSet {     init(rawValue rawValue: CFOptionFlags)     static var none: CFStreamEventType { get }     static var openCompleted: CFStreamEventType { get }     static var hasBytesAvailable: CFStreamEventType { get }     static var canAcceptBytes: CFStreamEventType { get }     static var errorOccurred: CFStreamEventType { get }     static var endEncountered: CFStreamEventType { get }     func intersect(_ other: CFStreamEventType) -> CFStreamEventType     func exclusiveOr(_ other: CFStreamEventType) -> CFStreamEventType     mutating func unionInPlace(_ other: CFStreamEventType)     mutating func intersectInPlace(_ other: CFStreamEventType)     mutating func exclusiveOrInPlace(_ other: CFStreamEventType)     func isSubsetOf(_ other: CFStreamEventType) -> Bool     func isDisjointWith(_ other: CFStreamEventType) -> Bool     func isSupersetOf(_ other: CFStreamEventType) -> Bool     mutating func subtractInPlace(_ other: CFStreamEventType)     func isStrictSupersetOf(_ other: CFStreamEventType) -> Bool     func isStrictSubsetOf(_ other: CFStreamEventType) -> Bool } extension CFStreamEventType {     func union(_ other: CFStreamEventType) -> CFStreamEventType     func intersection(_ other: CFStreamEventType) -> CFStreamEventType     func symmetricDifference(_ other: CFStreamEventType) -> CFStreamEventType } extension CFStreamEventType {     func contains(_ member: CFStreamEventType) -> Bool     mutating func insert(_ newMember: CFStreamEventType) -> (inserted: Bool, memberAfterInsert: CFStreamEventType)     mutating func remove(_ member: CFStreamEventType) -> CFStreamEventType?     mutating func update(with newMember: CFStreamEventType) -> CFStreamEventType? } extension CFStreamEventType {     convenience init()     mutating func formUnion(_ other: CFStreamEventType)     mutating func formIntersection(_ other: CFStreamEventType)     mutating func formSymmetricDifference(_ other: CFStreamEventType) } extension CFStreamEventType {     convenience init<S : Sequence where S.Iterator.Element == CFStreamEventType>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CFStreamEventType...)     mutating func subtract(_ other: CFStreamEventType)     func isSubset(of other: CFStreamEventType) -> Bool     func isSuperset(of other: CFStreamEventType) -> Bool     func isDisjoint(with other: CFStreamEventType) -> Bool     func subtracting(_ other: CFStreamEventType) -> CFStreamEventType     var isEmpty: Bool { get }     func isStrictSuperset(of other: CFStreamEventType) -> Bool     func isStrictSubset(of other: CFStreamEventType) -> Bool } ``` | OptionSet |

Modified [CFStreamEventType.canAcceptBytes](https://developer.apple.com/documentation/corefoundation/cfstreameventtype/1539627-canacceptbytes)

|  | Declaration |
| --- | --- |
| From | ``` static var CanAcceptBytes: CFStreamEventType { get } ``` |
| To | ``` static var canAcceptBytes: CFStreamEventType { get } ``` |

Modified [CFStreamEventType.endEncountered](https://developer.apple.com/documentation/corefoundation/cfstreameventtype/1539676-endencountered)

|  | Declaration |
| --- | --- |
| From | ``` static var EndEncountered: CFStreamEventType { get } ``` |
| To | ``` static var endEncountered: CFStreamEventType { get } ``` |

Modified [CFStreamEventType.errorOccurred](https://developer.apple.com/documentation/corefoundation/cfstreameventtype/kcfstreameventerroroccurred)

|  | Declaration |
| --- | --- |
| From | ``` static var ErrorOccurred: CFStreamEventType { get } ``` |
| To | ``` static var errorOccurred: CFStreamEventType { get } ``` |

Modified [CFStreamEventType.hasBytesAvailable](https://developer.apple.com/documentation/corefoundation/cfstreameventtype/kcfstreameventhasbytesavailable)

|  | Declaration |
| --- | --- |
| From | ``` static var HasBytesAvailable: CFStreamEventType { get } ``` |
| To | ``` static var hasBytesAvailable: CFStreamEventType { get } ``` |

Modified [CFStreamEventType.openCompleted](https://developer.apple.com/documentation/corefoundation/cfstreameventtype/1539640-opencompleted)

|  | Declaration |
| --- | --- |
| From | ``` static var OpenCompleted: CFStreamEventType { get } ``` |
| To | ``` static var openCompleted: CFStreamEventType { get } ``` |

Modified [CFStreamPropertyKey.appendToFile](https://developer.apple.com/documentation/corefoundation/kcfstreampropertyappendtofile)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFStreamPropertyAppendToFile | ``` let kCFStreamPropertyAppendToFile: CFString! ``` |
| To | appendToFile | ``` static let appendToFile: CFStreamPropertyKey! ``` |

Modified [CFStreamPropertyKey.dataWritten](https://developer.apple.com/documentation/corefoundation/cfstreampropertykey/1539604-datawritten)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFStreamPropertyDataWritten | ``` let kCFStreamPropertyDataWritten: CFString! ``` |
| To | dataWritten | ``` static let dataWritten: CFStreamPropertyKey! ``` |

Modified [CFStreamPropertyKey.fileCurrentOffset](https://developer.apple.com/documentation/corefoundation/kcfstreampropertyfilecurrentoffset)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFStreamPropertyFileCurrentOffset | ``` let kCFStreamPropertyFileCurrentOffset: CFString! ``` |
| To | fileCurrentOffset | ``` static let fileCurrentOffset: CFStreamPropertyKey! ``` |

Modified [CFStreamPropertyKey.socketNativeHandle](https://developer.apple.com/documentation/corefoundation/kcfstreampropertysocketnativehandle)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFStreamPropertySocketNativeHandle | ``` let kCFStreamPropertySocketNativeHandle: CFString! ``` |
| To | socketNativeHandle | ``` static let socketNativeHandle: CFStreamPropertyKey! ``` |

Modified [CFStreamPropertyKey.socketRemoteHostName](https://developer.apple.com/documentation/corefoundation/kcfstreampropertysocketremotehostname)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFStreamPropertySocketRemoteHostName | ``` let kCFStreamPropertySocketRemoteHostName: CFString! ``` |
| To | socketRemoteHostName | ``` static let socketRemoteHostName: CFStreamPropertyKey! ``` |

Modified [CFStreamPropertyKey.socketRemotePortNumber](https://developer.apple.com/documentation/corefoundation/cfstreampropertykey/1539602-socketremoteportnumber)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCFStreamPropertySocketRemotePortNumber | ``` let kCFStreamPropertySocketRemotePortNumber: CFString! ``` |
| To | socketRemotePortNumber | ``` static let socketRemotePortNumber: CFStreamPropertyKey! ``` |

Modified [CFStreamStatus [enum]](https://developer.apple.com/documentation/corefoundation/cfstreamstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum CFStreamStatus : CFIndex {     case NotOpen     case Opening     case Open     case Reading     case Writing     case AtEnd     case Closed     case Error } ``` |
| To | ``` enum CFStreamStatus : CFIndex {     case notOpen     case opening     case open     case reading     case writing     case atEnd     case closed     case error } ``` |

Modified [CFStreamStatus.atEnd](https://developer.apple.com/documentation/corefoundation/cfstreamstatus/kcfstreamstatusatend)

|  | Declaration |
| --- | --- |
| From | ``` case AtEnd ``` |
| To | ``` case atEnd ``` |

Modified [CFStreamStatus.closed](https://developer.apple.com/documentation/corefoundation/cfstreamstatus/kcfstreamstatusclosed)

|  | Declaration |
| --- | --- |
| From | ``` case Closed ``` |
| To | ``` case closed ``` |

Modified [CFStreamStatus.error](https://developer.apple.com/documentation/corefoundation/cfstreamstatus/kcfstreamstatuserror)

|  | Declaration |
| --- | --- |
| From | ``` case Error ``` |
| To | ``` case error ``` |

Modified [CFStreamStatus.notOpen](https://developer.apple.com/documentation/corefoundation/cfstreamstatus/kcfstreamstatusnotopen)

|  | Declaration |
| --- | --- |
| From | ``` case NotOpen ``` |
| To | ``` case notOpen ``` |

Modified [CFStreamStatus.open](https://developer.apple.com/documentation/corefoundation/cfstreamstatus/kcfstreamstatusopen)

|  | Declaration |
| --- | --- |
| From | ``` case Open ``` |
| To | ``` case open ``` |

Modified [CFStreamStatus.opening](https://developer.apple.com/documentation/corefoundation/cfstreamstatus/kcfstreamstatusopening)

|  | Declaration |
| --- | --- |
| From | ``` case Opening ``` |
| To | ``` case opening ``` |

Modified [CFStreamStatus.reading](https://developer.apple.com/documentation/corefoundation/cfstreamstatus/kcfstreamstatusreading)

|  | Declaration |
| --- | --- |
| From | ``` case Reading ``` |
| To | ``` case reading ``` |

Modified [CFStreamStatus.writing](https://developer.apple.com/documentation/corefoundation/cfstreamstatus/writing)

|  | Declaration |
| --- | --- |
| From | ``` case Writing ``` |
| To | ``` case writing ``` |

Modified [CFStringBuiltInEncodings [enum]](https://developer.apple.com/documentation/corefoundation/cfstringbuiltinencodings)

|  | Declaration |
| --- | --- |
| From | ``` enum CFStringBuiltInEncodings : CFStringEncoding {     case MacRoman     case WindowsLatin1     case ISOLatin1     case NextStepLatin     case ASCII     case Unicode     case UTF8     case NonLossyASCII     static var UTF16: CFStringBuiltInEncodings { get }     case UTF16BE     case UTF16LE     case UTF32     case UTF32BE     case UTF32LE } ``` |
| To | ``` enum CFStringBuiltInEncodings : CFStringEncoding {     case macRoman     case windowsLatin1     case isoLatin1     case nextStepLatin     case ASCII     case unicode     case UTF8     case nonLossyASCII     static var UTF16: CFStringBuiltInEncodings { get }     case UTF16BE     case UTF16LE     case UTF32     case UTF32BE     case UTF32LE } ``` |

Modified [CFStringBuiltInEncodings.isoLatin1](https://developer.apple.com/documentation/corefoundation/cfstringbuiltinencodings/isolatin1)

|  | Declaration |
| --- | --- |
| From | ``` case ISOLatin1 ``` |
| To | ``` case isoLatin1 ``` |

Modified [CFStringBuiltInEncodings.macRoman](https://developer.apple.com/documentation/corefoundation/cfstringbuiltinencodings/macroman)

|  | Declaration |
| --- | --- |
| From | ``` case MacRoman ``` |
| To | ``` case macRoman ``` |

Modified [CFStringBuiltInEncodings.nextStepLatin](https://developer.apple.com/documentation/corefoundation/cfstringbuiltinencodings/kcfstringencodingnextsteplatin)

|  | Declaration |
| --- | --- |
| From | ``` case NextStepLatin ``` |
| To | ``` case nextStepLatin ``` |

Modified [CFStringBuiltInEncodings.nonLossyASCII](https://developer.apple.com/documentation/corefoundation/cfstringbuiltinencodings/kcfstringencodingnonlossyascii)

|  | Declaration |
| --- | --- |
| From | ``` case NonLossyASCII ``` |
| To | ``` case nonLossyASCII ``` |

Modified [CFStringBuiltInEncodings.unicode](https://developer.apple.com/documentation/corefoundation/cfstringbuiltinencodings/kcfstringencodingunicode)

|  | Declaration |
| --- | --- |
| From | ``` case Unicode ``` |
| To | ``` case unicode ``` |

Modified [CFStringBuiltInEncodings.windowsLatin1](https://developer.apple.com/documentation/corefoundation/cfstringbuiltinencodings/kcfstringencodingwindowslatin1)

|  | Declaration |
| --- | --- |
| From | ``` case WindowsLatin1 ``` |
| To | ``` case windowsLatin1 ``` |

Modified [CFStringCompareFlags [struct]](https://developer.apple.com/documentation/corefoundation/cfstringcompareflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFStringCompareFlags : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var CompareCaseInsensitive: CFStringCompareFlags { get }     static var CompareBackwards: CFStringCompareFlags { get }     static var CompareAnchored: CFStringCompareFlags { get }     static var CompareNonliteral: CFStringCompareFlags { get }     static var CompareLocalized: CFStringCompareFlags { get }     static var CompareNumerically: CFStringCompareFlags { get }     static var CompareDiacriticInsensitive: CFStringCompareFlags { get }     static var CompareWidthInsensitive: CFStringCompareFlags { get }     static var CompareForcedOrdering: CFStringCompareFlags { get } } ``` | OptionSetType |
| To | ``` struct CFStringCompareFlags : OptionSet {     init(rawValue rawValue: CFOptionFlags)     static var compareCaseInsensitive: CFStringCompareFlags { get }     static var compareBackwards: CFStringCompareFlags { get }     static var compareAnchored: CFStringCompareFlags { get }     static var compareNonliteral: CFStringCompareFlags { get }     static var compareLocalized: CFStringCompareFlags { get }     static var compareNumerically: CFStringCompareFlags { get }     static var compareDiacriticInsensitive: CFStringCompareFlags { get }     static var compareWidthInsensitive: CFStringCompareFlags { get }     static var compareForcedOrdering: CFStringCompareFlags { get }     func intersect(_ other: CFStringCompareFlags) -> CFStringCompareFlags     func exclusiveOr(_ other: CFStringCompareFlags) -> CFStringCompareFlags     mutating func unionInPlace(_ other: CFStringCompareFlags)     mutating func intersectInPlace(_ other: CFStringCompareFlags)     mutating func exclusiveOrInPlace(_ other: CFStringCompareFlags)     func isSubsetOf(_ other: CFStringCompareFlags) -> Bool     func isDisjointWith(_ other: CFStringCompareFlags) -> Bool     func isSupersetOf(_ other: CFStringCompareFlags) -> Bool     mutating func subtractInPlace(_ other: CFStringCompareFlags)     func isStrictSupersetOf(_ other: CFStringCompareFlags) -> Bool     func isStrictSubsetOf(_ other: CFStringCompareFlags) -> Bool } extension CFStringCompareFlags {     func union(_ other: CFStringCompareFlags) -> CFStringCompareFlags     func intersection(_ other: CFStringCompareFlags) -> CFStringCompareFlags     func symmetricDifference(_ other: CFStringCompareFlags) -> CFStringCompareFlags } extension CFStringCompareFlags {     func contains(_ member: CFStringCompareFlags) -> Bool     mutating func insert(_ newMember: CFStringCompareFlags) -> (inserted: Bool, memberAfterInsert: CFStringCompareFlags)     mutating func remove(_ member: CFStringCompareFlags) -> CFStringCompareFlags?     mutating func update(with newMember: CFStringCompareFlags) -> CFStringCompareFlags? } extension CFStringCompareFlags {     convenience init()     mutating func formUnion(_ other: CFStringCompareFlags)     mutating func formIntersection(_ other: CFStringCompareFlags)     mutating func formSymmetricDifference(_ other: CFStringCompareFlags) } extension CFStringCompareFlags {     convenience init<S : Sequence where S.Iterator.Element == CFStringCompareFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CFStringCompareFlags...)     mutating func subtract(_ other: CFStringCompareFlags)     func isSubset(of other: CFStringCompareFlags) -> Bool     func isSuperset(of other: CFStringCompareFlags) -> Bool     func isDisjoint(with other: CFStringCompareFlags) -> Bool     func subtracting(_ other: CFStringCompareFlags) -> CFStringCompareFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: CFStringCompareFlags) -> Bool     func isStrictSubset(of other: CFStringCompareFlags) -> Bool } ``` | OptionSet |

Modified [CFStringCompareFlags.compareAnchored](https://developer.apple.com/documentation/corefoundation/cfstringcompareflags/kcfcompareanchored)

|  | Declaration |
| --- | --- |
| From | ``` static var CompareAnchored: CFStringCompareFlags { get } ``` |
| To | ``` static var compareAnchored: CFStringCompareFlags { get } ``` |

Modified [CFStringCompareFlags.compareBackwards](https://developer.apple.com/documentation/corefoundation/cfstringcompareflags/kcfcomparebackwards)

|  | Declaration |
| --- | --- |
| From | ``` static var CompareBackwards: CFStringCompareFlags { get } ``` |
| To | ``` static var compareBackwards: CFStringCompareFlags { get } ``` |

Modified [CFStringCompareFlags.compareCaseInsensitive](https://developer.apple.com/documentation/corefoundation/cfstringcompareflags/kcfcomparecaseinsensitive)

|  | Declaration |
| --- | --- |
| From | ``` static var CompareCaseInsensitive: CFStringCompareFlags { get } ``` |
| To | ``` static var compareCaseInsensitive: CFStringCompareFlags { get } ``` |

Modified [CFStringCompareFlags.compareDiacriticInsensitive](https://developer.apple.com/documentation/corefoundation/cfstringcompareflags/kcfcomparediacriticinsensitive)

|  | Declaration |
| --- | --- |
| From | ``` static var CompareDiacriticInsensitive: CFStringCompareFlags { get } ``` |
| To | ``` static var compareDiacriticInsensitive: CFStringCompareFlags { get } ``` |

Modified [CFStringCompareFlags.compareForcedOrdering](https://developer.apple.com/documentation/corefoundation/cfstringcompareflags/1543506-compareforcedordering)

|  | Declaration |
| --- | --- |
| From | ``` static var CompareForcedOrdering: CFStringCompareFlags { get } ``` |
| To | ``` static var compareForcedOrdering: CFStringCompareFlags { get } ``` |

Modified [CFStringCompareFlags.compareLocalized](https://developer.apple.com/documentation/corefoundation/cfstringcompareflags/kcfcomparelocalized)

|  | Declaration |
| --- | --- |
| From | ``` static var CompareLocalized: CFStringCompareFlags { get } ``` |
| To | ``` static var compareLocalized: CFStringCompareFlags { get } ``` |

Modified [CFStringCompareFlags.compareNonliteral](https://developer.apple.com/documentation/corefoundation/cfstringcompareflags/kcfcomparenonliteral)

|  | Declaration |
| --- | --- |
| From | ``` static var CompareNonliteral: CFStringCompareFlags { get } ``` |
| To | ``` static var compareNonliteral: CFStringCompareFlags { get } ``` |

Modified [CFStringCompareFlags.compareNumerically](https://developer.apple.com/documentation/corefoundation/cfstringcompareflags/kcfcomparenumerically)

|  | Declaration |
| --- | --- |
| From | ``` static var CompareNumerically: CFStringCompareFlags { get } ``` |
| To | ``` static var compareNumerically: CFStringCompareFlags { get } ``` |

Modified [CFStringCompareFlags.compareWidthInsensitive](https://developer.apple.com/documentation/corefoundation/cfstringcompareflags/kcfcomparewidthinsensitive)

|  | Declaration |
| --- | --- |
| From | ``` static var CompareWidthInsensitive: CFStringCompareFlags { get } ``` |
| To | ``` static var compareWidthInsensitive: CFStringCompareFlags { get } ``` |

Modified [CFStringEncodings [enum]](https://developer.apple.com/documentation/corefoundation/cfstringencodings)

|  | Declaration |
| --- | --- |
| From | ``` enum CFStringEncodings : CFIndex {     case MacJapanese     case MacChineseTrad     case MacKorean     case MacArabic     case MacHebrew     case MacGreek     case MacCyrillic     case MacDevanagari     case MacGurmukhi     case MacGujarati     case MacOriya     case MacBengali     case MacTamil     case MacTelugu     case MacKannada     case MacMalayalam     case MacSinhalese     case MacBurmese     case MacKhmer     case MacThai     case MacLaotian     case MacGeorgian     case MacArmenian     case MacChineseSimp     case MacTibetan     case MacMongolian     case MacEthiopic     case MacCentralEurRoman     case MacVietnamese     case MacExtArabic     case MacSymbol     case MacDingbats     case MacTurkish     case MacCroatian     case MacIcelandic     case MacRomanian     case MacCeltic     case MacGaelic     case MacFarsi     case MacUkrainian     case MacInuit     case MacVT100     case MacHFS     case ISOLatin2     case ISOLatin3     case ISOLatin4     case ISOLatinCyrillic     case ISOLatinArabic     case ISOLatinGreek     case ISOLatinHebrew     case ISOLatin5     case ISOLatin6     case ISOLatinThai     case ISOLatin7     case ISOLatin8     case ISOLatin9     case ISOLatin10     case DOSLatinUS     case DOSGreek     case DOSBalticRim     case DOSLatin1     case DOSGreek1     case DOSLatin2     case DOSCyrillic     case DOSTurkish     case DOSPortuguese     case DOSIcelandic     case DOSHebrew     case DOSCanadianFrench     case DOSArabic     case DOSNordic     case DOSRussian     case DOSGreek2     case DOSThai     case DOSJapanese     case DOSChineseSimplif     case DOSKorean     case DOSChineseTrad     case WindowsLatin2     case WindowsCyrillic     case WindowsGreek     case WindowsLatin5     case WindowsHebrew     case WindowsArabic     case WindowsBalticRim     case WindowsVietnamese     case WindowsKoreanJohab     case ANSEL     case JIS_X0201_76     case JIS_X0208_83     case JIS_X0208_90     case JIS_X0212_90     case JIS_C6226_78     case ShiftJIS_X0213     case ShiftJIS_X0213_MenKuTen     case GB_2312_80     case GBK_95     case GB_18030_2000     case KSC_5601_87     case KSC_5601_92_Johab     case CNS_11643_92_P1     case CNS_11643_92_P2     case CNS_11643_92_P3     case ISO_2022_JP     case ISO_2022_JP_2     case ISO_2022_JP_1     case ISO_2022_JP_3     case ISO_2022_CN     case ISO_2022_CN_EXT     case ISO_2022_KR     case EUC_JP     case EUC_CN     case EUC_TW     case EUC_KR     case ShiftJIS     case KOI8_R     case Big5     case MacRomanLatin1     case HZ_GB_2312     case Big5_HKSCS_1999     case VISCII     case KOI8_U     case Big5_E     case NextStepJapanese     case EBCDIC_US     case EBCDIC_CP037     case UTF7     case UTF7_IMAP     static var ShiftJIS_X0213_00: CFStringEncodings { get } } ``` |
| To | ``` enum CFStringEncodings : CFIndex {     case macJapanese     case macChineseTrad     case macKorean     case macArabic     case macHebrew     case macGreek     case macCyrillic     case macDevanagari     case macGurmukhi     case macGujarati     case macOriya     case macBengali     case macTamil     case macTelugu     case macKannada     case macMalayalam     case macSinhalese     case macBurmese     case macKhmer     case macThai     case macLaotian     case macGeorgian     case macArmenian     case macChineseSimp     case macTibetan     case macMongolian     case macEthiopic     case macCentralEurRoman     case macVietnamese     case macExtArabic     case macSymbol     case macDingbats     case macTurkish     case macCroatian     case macIcelandic     case macRomanian     case macCeltic     case macGaelic     case macFarsi     case macUkrainian     case macInuit     case macVT100     case macHFS     case isoLatin2     case isoLatin3     case isoLatin4     case isoLatinCyrillic     case isoLatinArabic     case isoLatinGreek     case isoLatinHebrew     case isoLatin5     case isoLatin6     case isoLatinThai     case isoLatin7     case isoLatin8     case isoLatin9     case isoLatin10     case dosLatinUS     case dosGreek     case dosBalticRim     case dosLatin1     case dosGreek1     case dosLatin2     case dosCyrillic     case dosTurkish     case dosPortuguese     case dosIcelandic     case dosHebrew     case dosCanadianFrench     case dosArabic     case dosNordic     case dosRussian     case dosGreek2     case dosThai     case dosJapanese     case dosChineseSimplif     case dosKorean     case dosChineseTrad     case windowsLatin2     case windowsCyrillic     case windowsGreek     case windowsLatin5     case windowsHebrew     case windowsArabic     case windowsBalticRim     case windowsVietnamese     case windowsKoreanJohab     case ANSEL     case JIS_X0201_76     case JIS_X0208_83     case JIS_X0208_90     case JIS_X0212_90     case JIS_C6226_78     case shiftJIS_X0213     case shiftJIS_X0213_MenKuTen     case GB_2312_80     case GBK_95     case GB_18030_2000     case KSC_5601_87     case ksc_5601_92_Johab     case CNS_11643_92_P1     case CNS_11643_92_P2     case CNS_11643_92_P3     case ISO_2022_JP     case ISO_2022_JP_2     case ISO_2022_JP_1     case ISO_2022_JP_3     case ISO_2022_CN     case ISO_2022_CN_EXT     case ISO_2022_KR     case EUC_JP     case EUC_CN     case EUC_TW     case EUC_KR     case shiftJIS     case KOI8_R     case big5     case macRomanLatin1     case HZ_GB_2312     case big5_HKSCS_1999     case VISCII     case KOI8_U     case big5_E     case nextStepJapanese     case EBCDIC_US     case EBCDIC_CP037     case UTF7     case UTF7_IMAP     static var shiftJIS_X0213_00: CFStringEncodings { get } } ``` |

Modified [CFStringEncodings.big5](https://developer.apple.com/documentation/corefoundation/cfstringencodings/big5)

|  | Declaration |
| --- | --- |
| From | ``` case Big5 ``` |
| To | ``` case big5 ``` |

Modified [CFStringEncodings.big5_E](https://developer.apple.com/documentation/corefoundation/cfstringencodings/big5_e)

|  | Declaration |
| --- | --- |
| From | ``` case Big5_E ``` |
| To | ``` case big5_E ``` |

Modified [CFStringEncodings.big5_HKSCS_1999](https://developer.apple.com/documentation/corefoundation/cfstringencodings/big5_hkscs_1999)

|  | Declaration |
| --- | --- |
| From | ``` case Big5_HKSCS_1999 ``` |
| To | ``` case big5_HKSCS_1999 ``` |

Modified [CFStringEncodings.dosArabic](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingdosarabic)

|  | Declaration |
| --- | --- |
| From | ``` case DOSArabic ``` |
| To | ``` case dosArabic ``` |

Modified [CFStringEncodings.dosBalticRim](https://developer.apple.com/documentation/corefoundation/cfstringencodings/dosbalticrim)

|  | Declaration |
| --- | --- |
| From | ``` case DOSBalticRim ``` |
| To | ``` case dosBalticRim ``` |

Modified [CFStringEncodings.dosCanadianFrench](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingdoscanadianfrench)

|  | Declaration |
| --- | --- |
| From | ``` case DOSCanadianFrench ``` |
| To | ``` case dosCanadianFrench ``` |

Modified [CFStringEncodings.dosChineseSimplif](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingdoschinesesimplif)

|  | Declaration |
| --- | --- |
| From | ``` case DOSChineseSimplif ``` |
| To | ``` case dosChineseSimplif ``` |

Modified [CFStringEncodings.dosChineseTrad](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingdoschinesetrad)

|  | Declaration |
| --- | --- |
| From | ``` case DOSChineseTrad ``` |
| To | ``` case dosChineseTrad ``` |

Modified [CFStringEncodings.dosCyrillic](https://developer.apple.com/documentation/corefoundation/cfstringencodings/doscyrillic)

|  | Declaration |
| --- | --- |
| From | ``` case DOSCyrillic ``` |
| To | ``` case dosCyrillic ``` |

Modified [CFStringEncodings.dosGreek](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingdosgreek)

|  | Declaration |
| --- | --- |
| From | ``` case DOSGreek ``` |
| To | ``` case dosGreek ``` |

Modified [CFStringEncodings.dosGreek1](https://developer.apple.com/documentation/corefoundation/cfstringencodings/dosgreek1)

|  | Declaration |
| --- | --- |
| From | ``` case DOSGreek1 ``` |
| To | ``` case dosGreek1 ``` |

Modified [CFStringEncodings.dosGreek2](https://developer.apple.com/documentation/corefoundation/cfstringencodings/dosgreek2)

|  | Declaration |
| --- | --- |
| From | ``` case DOSGreek2 ``` |
| To | ``` case dosGreek2 ``` |

Modified [CFStringEncodings.dosHebrew](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingdoshebrew)

|  | Declaration |
| --- | --- |
| From | ``` case DOSHebrew ``` |
| To | ``` case dosHebrew ``` |

Modified [CFStringEncodings.dosIcelandic](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingdosicelandic)

|  | Declaration |
| --- | --- |
| From | ``` case DOSIcelandic ``` |
| To | ``` case dosIcelandic ``` |

Modified [CFStringEncodings.dosJapanese](https://developer.apple.com/documentation/corefoundation/cfstringencodings/dosjapanese)

|  | Declaration |
| --- | --- |
| From | ``` case DOSJapanese ``` |
| To | ``` case dosJapanese ``` |

Modified [CFStringEncodings.dosKorean](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingdoskorean)

|  | Declaration |
| --- | --- |
| From | ``` case DOSKorean ``` |
| To | ``` case dosKorean ``` |

Modified [CFStringEncodings.dosLatin1](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingdoslatin1)

|  | Declaration |
| --- | --- |
| From | ``` case DOSLatin1 ``` |
| To | ``` case dosLatin1 ``` |

Modified [CFStringEncodings.dosLatin2](https://developer.apple.com/documentation/corefoundation/cfstringencodings/doslatin2)

|  | Declaration |
| --- | --- |
| From | ``` case DOSLatin2 ``` |
| To | ``` case dosLatin2 ``` |

Modified [CFStringEncodings.dosLatinUS](https://developer.apple.com/documentation/corefoundation/cfstringencodings/doslatinus)

|  | Declaration |
| --- | --- |
| From | ``` case DOSLatinUS ``` |
| To | ``` case dosLatinUS ``` |

Modified [CFStringEncodings.dosNordic](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingdosnordic)

|  | Declaration |
| --- | --- |
| From | ``` case DOSNordic ``` |
| To | ``` case dosNordic ``` |

Modified [CFStringEncodings.dosPortuguese](https://developer.apple.com/documentation/corefoundation/cfstringencodings/dosportuguese)

|  | Declaration |
| --- | --- |
| From | ``` case DOSPortuguese ``` |
| To | ``` case dosPortuguese ``` |

Modified [CFStringEncodings.dosRussian](https://developer.apple.com/documentation/corefoundation/cfstringencodings/dosrussian)

|  | Declaration |
| --- | --- |
| From | ``` case DOSRussian ``` |
| To | ``` case dosRussian ``` |

Modified [CFStringEncodings.dosThai](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingdosthai)

|  | Declaration |
| --- | --- |
| From | ``` case DOSThai ``` |
| To | ``` case dosThai ``` |

Modified [CFStringEncodings.dosTurkish](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingdosturkish)

|  | Declaration |
| --- | --- |
| From | ``` case DOSTurkish ``` |
| To | ``` case dosTurkish ``` |

Modified [CFStringEncodings.isoLatin10](https://developer.apple.com/documentation/corefoundation/cfstringencodings/isolatin10)

|  | Declaration |
| --- | --- |
| From | ``` case ISOLatin10 ``` |
| To | ``` case isoLatin10 ``` |

Modified [CFStringEncodings.isoLatin2](https://developer.apple.com/documentation/corefoundation/cfstringencodings/isolatin2)

|  | Declaration |
| --- | --- |
| From | ``` case ISOLatin2 ``` |
| To | ``` case isoLatin2 ``` |

Modified [CFStringEncodings.isoLatin3](https://developer.apple.com/documentation/corefoundation/cfstringencodings/isolatin3)

|  | Declaration |
| --- | --- |
| From | ``` case ISOLatin3 ``` |
| To | ``` case isoLatin3 ``` |

Modified [CFStringEncodings.isoLatin4](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingisolatin4)

|  | Declaration |
| --- | --- |
| From | ``` case ISOLatin4 ``` |
| To | ``` case isoLatin4 ``` |

Modified [CFStringEncodings.isoLatin5](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingisolatin5)

|  | Declaration |
| --- | --- |
| From | ``` case ISOLatin5 ``` |
| To | ``` case isoLatin5 ``` |

Modified [CFStringEncodings.isoLatin6](https://developer.apple.com/documentation/corefoundation/cfstringencodings/isolatin6)

|  | Declaration |
| --- | --- |
| From | ``` case ISOLatin6 ``` |
| To | ``` case isoLatin6 ``` |

Modified [CFStringEncodings.isoLatin7](https://developer.apple.com/documentation/corefoundation/cfstringencodings/isolatin7)

|  | Declaration |
| --- | --- |
| From | ``` case ISOLatin7 ``` |
| To | ``` case isoLatin7 ``` |

Modified [CFStringEncodings.isoLatin8](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingisolatin8)

|  | Declaration |
| --- | --- |
| From | ``` case ISOLatin8 ``` |
| To | ``` case isoLatin8 ``` |

Modified [CFStringEncodings.isoLatin9](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingisolatin9)

|  | Declaration |
| --- | --- |
| From | ``` case ISOLatin9 ``` |
| To | ``` case isoLatin9 ``` |

Modified [CFStringEncodings.isoLatinArabic](https://developer.apple.com/documentation/corefoundation/cfstringencodings/isolatinarabic)

|  | Declaration |
| --- | --- |
| From | ``` case ISOLatinArabic ``` |
| To | ``` case isoLatinArabic ``` |

Modified [CFStringEncodings.isoLatinCyrillic](https://developer.apple.com/documentation/corefoundation/cfstringencodings/isolatincyrillic)

|  | Declaration |
| --- | --- |
| From | ``` case ISOLatinCyrillic ``` |
| To | ``` case isoLatinCyrillic ``` |

Modified [CFStringEncodings.isoLatinGreek](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingisolatingreek)

|  | Declaration |
| --- | --- |
| From | ``` case ISOLatinGreek ``` |
| To | ``` case isoLatinGreek ``` |

Modified [CFStringEncodings.isoLatinHebrew](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingisolatinhebrew)

|  | Declaration |
| --- | --- |
| From | ``` case ISOLatinHebrew ``` |
| To | ``` case isoLatinHebrew ``` |

Modified [CFStringEncodings.isoLatinThai](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingisolatinthai)

|  | Declaration |
| --- | --- |
| From | ``` case ISOLatinThai ``` |
| To | ``` case isoLatinThai ``` |

Modified [CFStringEncodings.ksc_5601_92_Johab](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingksc_5601_92_johab)

|  | Declaration |
| --- | --- |
| From | ``` case KSC_5601_92_Johab ``` |
| To | ``` case ksc_5601_92_Johab ``` |

Modified [CFStringEncodings.macArabic](https://developer.apple.com/documentation/corefoundation/cfstringencodings/macarabic)

|  | Declaration |
| --- | --- |
| From | ``` case MacArabic ``` |
| To | ``` case macArabic ``` |

Modified [CFStringEncodings.macArmenian](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingmacarmenian)

|  | Declaration |
| --- | --- |
| From | ``` case MacArmenian ``` |
| To | ``` case macArmenian ``` |

Modified [CFStringEncodings.macBengali](https://developer.apple.com/documentation/corefoundation/cfstringencodings/macbengali)

|  | Declaration |
| --- | --- |
| From | ``` case MacBengali ``` |
| To | ``` case macBengali ``` |

Modified [CFStringEncodings.macBurmese](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingmacburmese)

|  | Declaration |
| --- | --- |
| From | ``` case MacBurmese ``` |
| To | ``` case macBurmese ``` |

Modified [CFStringEncodings.macCeltic](https://developer.apple.com/documentation/corefoundation/cfstringencodings/macceltic)

|  | Declaration |
| --- | --- |
| From | ``` case MacCeltic ``` |
| To | ``` case macCeltic ``` |

Modified [CFStringEncodings.macCentralEurRoman](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingmaccentraleurroman)

|  | Declaration |
| --- | --- |
| From | ``` case MacCentralEurRoman ``` |
| To | ``` case macCentralEurRoman ``` |

Modified [CFStringEncodings.macChineseSimp](https://developer.apple.com/documentation/corefoundation/cfstringencodings/macchinesesimp)

|  | Declaration |
| --- | --- |
| From | ``` case MacChineseSimp ``` |
| To | ``` case macChineseSimp ``` |

Modified [CFStringEncodings.macChineseTrad](https://developer.apple.com/documentation/corefoundation/cfstringencodings/macchinesetrad)

|  | Declaration |
| --- | --- |
| From | ``` case MacChineseTrad ``` |
| To | ``` case macChineseTrad ``` |

Modified [CFStringEncodings.macCroatian](https://developer.apple.com/documentation/corefoundation/cfstringencodings/maccroatian)

|  | Declaration |
| --- | --- |
| From | ``` case MacCroatian ``` |
| To | ``` case macCroatian ``` |

Modified [CFStringEncodings.macCyrillic](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingmaccyrillic)

|  | Declaration |
| --- | --- |
| From | ``` case MacCyrillic ``` |
| To | ``` case macCyrillic ``` |

Modified [CFStringEncodings.macDevanagari](https://developer.apple.com/documentation/corefoundation/cfstringencodings/macdevanagari)

|  | Declaration |
| --- | --- |
| From | ``` case MacDevanagari ``` |
| To | ``` case macDevanagari ``` |

Modified [CFStringEncodings.macDingbats](https://developer.apple.com/documentation/corefoundation/cfstringencodings/macdingbats)

|  | Declaration |
| --- | --- |
| From | ``` case MacDingbats ``` |
| To | ``` case macDingbats ``` |

Modified [CFStringEncodings.macEthiopic](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingmacethiopic)

|  | Declaration |
| --- | --- |
| From | ``` case MacEthiopic ``` |
| To | ``` case macEthiopic ``` |

Modified [CFStringEncodings.macExtArabic](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingmacextarabic)

|  | Declaration |
| --- | --- |
| From | ``` case MacExtArabic ``` |
| To | ``` case macExtArabic ``` |

Modified [CFStringEncodings.macFarsi](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingmacfarsi)

|  | Declaration |
| --- | --- |
| From | ``` case MacFarsi ``` |
| To | ``` case macFarsi ``` |

Modified [CFStringEncodings.macGaelic](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingmacgaelic)

|  | Declaration |
| --- | --- |
| From | ``` case MacGaelic ``` |
| To | ``` case macGaelic ``` |

Modified [CFStringEncodings.macGeorgian](https://developer.apple.com/documentation/corefoundation/cfstringencodings/macgeorgian)

|  | Declaration |
| --- | --- |
| From | ``` case MacGeorgian ``` |
| To | ``` case macGeorgian ``` |

Modified [CFStringEncodings.macGreek](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingmacgreek)

|  | Declaration |
| --- | --- |
| From | ``` case MacGreek ``` |
| To | ``` case macGreek ``` |

Modified [CFStringEncodings.macGujarati](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingmacgujarati)

|  | Declaration |
| --- | --- |
| From | ``` case MacGujarati ``` |
| To | ``` case macGujarati ``` |

Modified [CFStringEncodings.macGurmukhi](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingmacgurmukhi)

|  | Declaration |
| --- | --- |
| From | ``` case MacGurmukhi ``` |
| To | ``` case macGurmukhi ``` |

Modified [CFStringEncodings.macHebrew](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingmachebrew)

|  | Declaration |
| --- | --- |
| From | ``` case MacHebrew ``` |
| To | ``` case macHebrew ``` |

Modified [CFStringEncodings.macHFS](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingmachfs)

|  | Declaration |
| --- | --- |
| From | ``` case MacHFS ``` |
| To | ``` case macHFS ``` |

Modified [CFStringEncodings.macIcelandic](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingmacicelandic)

|  | Declaration |
| --- | --- |
| From | ``` case MacIcelandic ``` |
| To | ``` case macIcelandic ``` |

Modified [CFStringEncodings.macInuit](https://developer.apple.com/documentation/corefoundation/cfstringencodings/macinuit)

|  | Declaration |
| --- | --- |
| From | ``` case MacInuit ``` |
| To | ``` case macInuit ``` |

Modified [CFStringEncodings.macJapanese](https://developer.apple.com/documentation/corefoundation/cfstringencodings/macjapanese)

|  | Declaration |
| --- | --- |
| From | ``` case MacJapanese ``` |
| To | ``` case macJapanese ``` |

Modified [CFStringEncodings.macKannada](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingmackannada)

|  | Declaration |
| --- | --- |
| From | ``` case MacKannada ``` |
| To | ``` case macKannada ``` |

Modified [CFStringEncodings.macKhmer](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingmackhmer)

|  | Declaration |
| --- | --- |
| From | ``` case MacKhmer ``` |
| To | ``` case macKhmer ``` |

Modified [CFStringEncodings.macKorean](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingmackorean)

|  | Declaration |
| --- | --- |
| From | ``` case MacKorean ``` |
| To | ``` case macKorean ``` |

Modified [CFStringEncodings.macLaotian](https://developer.apple.com/documentation/corefoundation/cfstringencodings/maclaotian)

|  | Declaration |
| --- | --- |
| From | ``` case MacLaotian ``` |
| To | ``` case macLaotian ``` |

Modified [CFStringEncodings.macMalayalam](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingmacmalayalam)

|  | Declaration |
| --- | --- |
| From | ``` case MacMalayalam ``` |
| To | ``` case macMalayalam ``` |

Modified [CFStringEncodings.macMongolian](https://developer.apple.com/documentation/corefoundation/cfstringencodings/macmongolian)

|  | Declaration |
| --- | --- |
| From | ``` case MacMongolian ``` |
| To | ``` case macMongolian ``` |

Modified [CFStringEncodings.macOriya](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingmacoriya)

|  | Declaration |
| --- | --- |
| From | ``` case MacOriya ``` |
| To | ``` case macOriya ``` |

Modified [CFStringEncodings.macRomanian](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingmacromanian)

|  | Declaration |
| --- | --- |
| From | ``` case MacRomanian ``` |
| To | ``` case macRomanian ``` |

Modified [CFStringEncodings.macRomanLatin1](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingmacromanlatin1)

|  | Declaration |
| --- | --- |
| From | ``` case MacRomanLatin1 ``` |
| To | ``` case macRomanLatin1 ``` |

Modified [CFStringEncodings.macSinhalese](https://developer.apple.com/documentation/corefoundation/cfstringencodings/macsinhalese)

|  | Declaration |
| --- | --- |
| From | ``` case MacSinhalese ``` |
| To | ``` case macSinhalese ``` |

Modified [CFStringEncodings.macSymbol](https://developer.apple.com/documentation/corefoundation/cfstringencodings/macsymbol)

|  | Declaration |
| --- | --- |
| From | ``` case MacSymbol ``` |
| To | ``` case macSymbol ``` |

Modified [CFStringEncodings.macTamil](https://developer.apple.com/documentation/corefoundation/cfstringencodings/mactamil)

|  | Declaration |
| --- | --- |
| From | ``` case MacTamil ``` |
| To | ``` case macTamil ``` |

Modified [CFStringEncodings.macTelugu](https://developer.apple.com/documentation/corefoundation/cfstringencodings/mactelugu)

|  | Declaration |
| --- | --- |
| From | ``` case MacTelugu ``` |
| To | ``` case macTelugu ``` |

Modified [CFStringEncodings.macThai](https://developer.apple.com/documentation/corefoundation/cfstringencodings/macthai)

|  | Declaration |
| --- | --- |
| From | ``` case MacThai ``` |
| To | ``` case macThai ``` |

Modified [CFStringEncodings.macTibetan](https://developer.apple.com/documentation/corefoundation/cfstringencodings/mactibetan)

|  | Declaration |
| --- | --- |
| From | ``` case MacTibetan ``` |
| To | ``` case macTibetan ``` |

Modified [CFStringEncodings.macTurkish](https://developer.apple.com/documentation/corefoundation/cfstringencodings/macturkish)

|  | Declaration |
| --- | --- |
| From | ``` case MacTurkish ``` |
| To | ``` case macTurkish ``` |

Modified [CFStringEncodings.macUkrainian](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingmacukrainian)

|  | Declaration |
| --- | --- |
| From | ``` case MacUkrainian ``` |
| To | ``` case macUkrainian ``` |

Modified [CFStringEncodings.macVietnamese](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingmacvietnamese)

|  | Declaration |
| --- | --- |
| From | ``` case MacVietnamese ``` |
| To | ``` case macVietnamese ``` |

Modified [CFStringEncodings.macVT100](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingmacvt100)

|  | Declaration |
| --- | --- |
| From | ``` case MacVT100 ``` |
| To | ``` case macVT100 ``` |

Modified [CFStringEncodings.nextStepJapanese](https://developer.apple.com/documentation/corefoundation/cfstringencodings/nextstepjapanese)

|  | Declaration |
| --- | --- |
| From | ``` case NextStepJapanese ``` |
| To | ``` case nextStepJapanese ``` |

Modified [CFStringEncodings.shiftJIS](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingshiftjis)

|  | Declaration |
| --- | --- |
| From | ``` case ShiftJIS ``` |
| To | ``` case shiftJIS ``` |

Modified [CFStringEncodings.shiftJIS_X0213](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingshiftjis_x0213)

|  | Declaration |
| --- | --- |
| From | ``` case ShiftJIS_X0213 ``` |
| To | ``` case shiftJIS_X0213 ``` |

Modified [CFStringEncodings.shiftJIS_X0213_00](https://developer.apple.com/documentation/corefoundation/cfstringencodings/1543375-shiftjis_x0213_00)

|  | Declaration |
| --- | --- |
| From | ``` static var ShiftJIS_X0213_00: CFStringEncodings { get } ``` |
| To | ``` static var shiftJIS_X0213_00: CFStringEncodings { get } ``` |

Modified [CFStringEncodings.shiftJIS_X0213_MenKuTen](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingshiftjis_x0213_menkuten)

|  | Declaration |
| --- | --- |
| From | ``` case ShiftJIS_X0213_MenKuTen ``` |
| To | ``` case shiftJIS_X0213_MenKuTen ``` |

Modified [CFStringEncodings.windowsArabic](https://developer.apple.com/documentation/corefoundation/cfstringencodings/windowsarabic)

|  | Declaration |
| --- | --- |
| From | ``` case WindowsArabic ``` |
| To | ``` case windowsArabic ``` |

Modified [CFStringEncodings.windowsBalticRim](https://developer.apple.com/documentation/corefoundation/cfstringencodings/windowsbalticrim)

|  | Declaration |
| --- | --- |
| From | ``` case WindowsBalticRim ``` |
| To | ``` case windowsBalticRim ``` |

Modified [CFStringEncodings.windowsCyrillic](https://developer.apple.com/documentation/corefoundation/cfstringencodings/windowscyrillic)

|  | Declaration |
| --- | --- |
| From | ``` case WindowsCyrillic ``` |
| To | ``` case windowsCyrillic ``` |

Modified [CFStringEncodings.windowsGreek](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingwindowsgreek)

|  | Declaration |
| --- | --- |
| From | ``` case WindowsGreek ``` |
| To | ``` case windowsGreek ``` |

Modified [CFStringEncodings.windowsHebrew](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingwindowshebrew)

|  | Declaration |
| --- | --- |
| From | ``` case WindowsHebrew ``` |
| To | ``` case windowsHebrew ``` |

Modified [CFStringEncodings.windowsKoreanJohab](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingwindowskoreanjohab)

|  | Declaration |
| --- | --- |
| From | ``` case WindowsKoreanJohab ``` |
| To | ``` case windowsKoreanJohab ``` |

Modified [CFStringEncodings.windowsLatin2](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingwindowslatin2)

|  | Declaration |
| --- | --- |
| From | ``` case WindowsLatin2 ``` |
| To | ``` case windowsLatin2 ``` |

Modified [CFStringEncodings.windowsLatin5](https://developer.apple.com/documentation/corefoundation/cfstringencodings/windowslatin5)

|  | Declaration |
| --- | --- |
| From | ``` case WindowsLatin5 ``` |
| To | ``` case windowsLatin5 ``` |

Modified [CFStringEncodings.windowsVietnamese](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingwindowsvietnamese)

|  | Declaration |
| --- | --- |
| From | ``` case WindowsVietnamese ``` |
| To | ``` case windowsVietnamese ``` |

Modified [CFStringInlineBuffer [struct]](https://developer.apple.com/documentation/corefoundation/cfstringinlinebuffer)

|  | Declaration |
| --- | --- |
| From | ``` struct CFStringInlineBuffer {     var buffer: (UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar)     var theString: Unmanaged<CFString>!     var directUniCharBuffer: UnsafePointer<UniChar>     var directCStringBuffer: UnsafePointer<Int8>     var rangeToBuffer: CFRange     var bufferedRangeStart: CFIndex     var bufferedRangeEnd: CFIndex     init()     init(buffer buffer: (UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar), theString theString: Unmanaged<CFString>!, directUniCharBuffer directUniCharBuffer: UnsafePointer<UniChar>, directCStringBuffer directCStringBuffer: UnsafePointer<Int8>, rangeToBuffer rangeToBuffer: CFRange, bufferedRangeStart bufferedRangeStart: CFIndex, bufferedRangeEnd bufferedRangeEnd: CFIndex) } ``` |
| To | ``` struct CFStringInlineBuffer {     var buffer: (UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar)     var theString: Unmanaged<CFString>!     var directUniCharBuffer: UnsafePointer<UniChar>!     var directCStringBuffer: UnsafePointer<Int8>!     var rangeToBuffer: CFRange     var bufferedRangeStart: CFIndex     var bufferedRangeEnd: CFIndex     init()     init(buffer buffer: (UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar), theString theString: Unmanaged<CFString>!, directUniCharBuffer directUniCharBuffer: UnsafePointer<UniChar>!, directCStringBuffer directCStringBuffer: UnsafePointer<Int8>!, rangeToBuffer rangeToBuffer: CFRange, bufferedRangeStart bufferedRangeStart: CFIndex, bufferedRangeEnd bufferedRangeEnd: CFIndex) } ``` |

Modified [CFStringInlineBuffer.directCStringBuffer](https://developer.apple.com/documentation/corefoundation/cfstringinlinebuffer/1541983-directcstringbuffer)

|  | Declaration |
| --- | --- |
| From | ``` var directCStringBuffer: UnsafePointer<Int8> ``` |
| To | ``` var directCStringBuffer: UnsafePointer<Int8>! ``` |

Modified [CFStringInlineBuffer.directUniCharBuffer](https://developer.apple.com/documentation/corefoundation/cfstringinlinebuffer/1542027-directunicharbuffer)

|  | Declaration |
| --- | --- |
| From | ``` var directUniCharBuffer: UnsafePointer<UniChar> ``` |
| To | ``` var directUniCharBuffer: UnsafePointer<UniChar>! ``` |

Modified [CFStringTokenizerTokenType [struct]](https://developer.apple.com/documentation/corefoundation/cfstringtokenizertokentype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFStringTokenizerTokenType : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var None: CFStringTokenizerTokenType { get }     static var Normal: CFStringTokenizerTokenType { get }     static var HasSubTokensMask: CFStringTokenizerTokenType { get }     static var HasDerivedSubTokensMask: CFStringTokenizerTokenType { get }     static var HasHasNumbersMask: CFStringTokenizerTokenType { get }     static var HasNonLettersMask: CFStringTokenizerTokenType { get }     static var IsCJWordMask: CFStringTokenizerTokenType { get } } ``` | OptionSetType |
| To | ``` struct CFStringTokenizerTokenType : OptionSet {     init(rawValue rawValue: CFOptionFlags)     static var none: CFStringTokenizerTokenType { get }     static var normal: CFStringTokenizerTokenType { get }     static var hasSubTokensMask: CFStringTokenizerTokenType { get }     static var hasDerivedSubTokensMask: CFStringTokenizerTokenType { get }     static var hasHasNumbersMask: CFStringTokenizerTokenType { get }     static var hasNonLettersMask: CFStringTokenizerTokenType { get }     static var isCJWordMask: CFStringTokenizerTokenType { get }     func intersect(_ other: CFStringTokenizerTokenType) -> CFStringTokenizerTokenType     func exclusiveOr(_ other: CFStringTokenizerTokenType) -> CFStringTokenizerTokenType     mutating func unionInPlace(_ other: CFStringTokenizerTokenType)     mutating func intersectInPlace(_ other: CFStringTokenizerTokenType)     mutating func exclusiveOrInPlace(_ other: CFStringTokenizerTokenType)     func isSubsetOf(_ other: CFStringTokenizerTokenType) -> Bool     func isDisjointWith(_ other: CFStringTokenizerTokenType) -> Bool     func isSupersetOf(_ other: CFStringTokenizerTokenType) -> Bool     mutating func subtractInPlace(_ other: CFStringTokenizerTokenType)     func isStrictSupersetOf(_ other: CFStringTokenizerTokenType) -> Bool     func isStrictSubsetOf(_ other: CFStringTokenizerTokenType) -> Bool } extension CFStringTokenizerTokenType {     func union(_ other: CFStringTokenizerTokenType) -> CFStringTokenizerTokenType     func intersection(_ other: CFStringTokenizerTokenType) -> CFStringTokenizerTokenType     func symmetricDifference(_ other: CFStringTokenizerTokenType) -> CFStringTokenizerTokenType } extension CFStringTokenizerTokenType {     func contains(_ member: CFStringTokenizerTokenType) -> Bool     mutating func insert(_ newMember: CFStringTokenizerTokenType) -> (inserted: Bool, memberAfterInsert: CFStringTokenizerTokenType)     mutating func remove(_ member: CFStringTokenizerTokenType) -> CFStringTokenizerTokenType?     mutating func update(with newMember: CFStringTokenizerTokenType) -> CFStringTokenizerTokenType? } extension CFStringTokenizerTokenType {     convenience init()     mutating func formUnion(_ other: CFStringTokenizerTokenType)     mutating func formIntersection(_ other: CFStringTokenizerTokenType)     mutating func formSymmetricDifference(_ other: CFStringTokenizerTokenType) } extension CFStringTokenizerTokenType {     convenience init<S : Sequence where S.Iterator.Element == CFStringTokenizerTokenType>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CFStringTokenizerTokenType...)     mutating func subtract(_ other: CFStringTokenizerTokenType)     func isSubset(of other: CFStringTokenizerTokenType) -> Bool     func isSuperset(of other: CFStringTokenizerTokenType) -> Bool     func isDisjoint(with other: CFStringTokenizerTokenType) -> Bool     func subtracting(_ other: CFStringTokenizerTokenType) -> CFStringTokenizerTokenType     var isEmpty: Bool { get }     func isStrictSuperset(of other: CFStringTokenizerTokenType) -> Bool     func isStrictSubset(of other: CFStringTokenizerTokenType) -> Bool } ``` | OptionSet |

Modified [CFStringTokenizerTokenType.hasDerivedSubTokensMask](https://developer.apple.com/documentation/corefoundation/cfstringtokenizertokentype/1542073-hasderivedsubtokensmask)

|  | Declaration |
| --- | --- |
| From | ``` static var HasDerivedSubTokensMask: CFStringTokenizerTokenType { get } ``` |
| To | ``` static var hasDerivedSubTokensMask: CFStringTokenizerTokenType { get } ``` |

Modified [CFStringTokenizerTokenType.hasHasNumbersMask](https://developer.apple.com/documentation/corefoundation/cfstringtokenizertokentype/1542955-hashasnumbersmask)

|  | Declaration |
| --- | --- |
| From | ``` static var HasHasNumbersMask: CFStringTokenizerTokenType { get } ``` |
| To | ``` static var hasHasNumbersMask: CFStringTokenizerTokenType { get } ``` |

Modified [CFStringTokenizerTokenType.hasNonLettersMask](https://developer.apple.com/documentation/corefoundation/cfstringtokenizertokentype/kcfstringtokenizertokenhasnonlettersmask)

|  | Declaration |
| --- | --- |
| From | ``` static var HasNonLettersMask: CFStringTokenizerTokenType { get } ``` |
| To | ``` static var hasNonLettersMask: CFStringTokenizerTokenType { get } ``` |

Modified [CFStringTokenizerTokenType.hasSubTokensMask](https://developer.apple.com/documentation/corefoundation/cfstringtokenizertokentype/kcfstringtokenizertokenhassubtokensmask)

|  | Declaration |
| --- | --- |
| From | ``` static var HasSubTokensMask: CFStringTokenizerTokenType { get } ``` |
| To | ``` static var hasSubTokensMask: CFStringTokenizerTokenType { get } ``` |

Modified [CFStringTokenizerTokenType.isCJWordMask](https://developer.apple.com/documentation/corefoundation/cfstringtokenizertokentype/kcfstringtokenizertokeniscjwordmask)

|  | Declaration |
| --- | --- |
| From | ``` static var IsCJWordMask: CFStringTokenizerTokenType { get } ``` |
| To | ``` static var isCJWordMask: CFStringTokenizerTokenType { get } ``` |

Modified [CFStringTokenizerTokenType.normal](https://developer.apple.com/documentation/corefoundation/cfstringtokenizertokentype/1543263-normal)

|  | Declaration |
| --- | --- |
| From | ``` static var Normal: CFStringTokenizerTokenType { get } ``` |
| To | ``` static var normal: CFStringTokenizerTokenType { get } ``` |

Modified [CFTimeZoneNameStyle [enum]](https://developer.apple.com/documentation/corefoundation/cftimezonenamestyle)

|  | Declaration |
| --- | --- |
| From | ``` enum CFTimeZoneNameStyle : CFIndex {     case Standard     case ShortStandard     case DaylightSaving     case ShortDaylightSaving     case Generic     case ShortGeneric } ``` |
| To | ``` enum CFTimeZoneNameStyle : CFIndex {     case standard     case shortStandard     case daylightSaving     case shortDaylightSaving     case generic     case shortGeneric } ``` |

Modified [CFTimeZoneNameStyle.daylightSaving](https://developer.apple.com/documentation/corefoundation/cftimezonenamestyle/daylightsaving)

|  | Declaration |
| --- | --- |
| From | ``` case DaylightSaving ``` |
| To | ``` case daylightSaving ``` |

Modified [CFTimeZoneNameStyle.generic](https://developer.apple.com/documentation/corefoundation/cftimezonenamestyle/generic)

|  | Declaration |
| --- | --- |
| From | ``` case Generic ``` |
| To | ``` case generic ``` |

Modified [CFTimeZoneNameStyle.shortDaylightSaving](https://developer.apple.com/documentation/corefoundation/cftimezonenamestyle/kcftimezonenamestyleshortdaylightsaving)

|  | Declaration |
| --- | --- |
| From | ``` case ShortDaylightSaving ``` |
| To | ``` case shortDaylightSaving ``` |

Modified [CFTimeZoneNameStyle.shortGeneric](https://developer.apple.com/documentation/corefoundation/cftimezonenamestyle/kcftimezonenamestyleshortgeneric)

|  | Declaration |
| --- | --- |
| From | ``` case ShortGeneric ``` |
| To | ``` case shortGeneric ``` |

Modified [CFTimeZoneNameStyle.shortStandard](https://developer.apple.com/documentation/corefoundation/cftimezonenamestyle/kcftimezonenamestyleshortstandard)

|  | Declaration |
| --- | --- |
| From | ``` case ShortStandard ``` |
| To | ``` case shortStandard ``` |

Modified [CFTimeZoneNameStyle.standard](https://developer.apple.com/documentation/corefoundation/cftimezonenamestyle/standard)

|  | Declaration |
| --- | --- |
| From | ``` case Standard ``` |
| To | ``` case standard ``` |

Modified [CFTreeContext [struct]](https://developer.apple.com/documentation/corefoundation/cftreecontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFTreeContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFTreeRetainCallBack!     var release: CFTreeReleaseCallBack!     var copyDescription: CFTreeCopyDescriptionCallBack!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFTreeRetainCallBack!, release release: CFTreeReleaseCallBack!, copyDescription copyDescription: CFTreeCopyDescriptionCallBack!) } ``` |
| To | ``` struct CFTreeContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: CoreFoundation.CFTreeRetainCallBack!     var release: CoreFoundation.CFTreeReleaseCallBack!     var copyDescription: CoreFoundation.CFTreeCopyDescriptionCallBack!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: CoreFoundation.CFTreeRetainCallBack!, release release: CoreFoundation.CFTreeReleaseCallBack!, copyDescription copyDescription: CoreFoundation.CFTreeCopyDescriptionCallBack!) } ``` |

Modified [CFTreeContext.copyDescription](https://developer.apple.com/documentation/corefoundation/cftreecontext/1401800-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFTreeCopyDescriptionCallBack! ``` |
| To | ``` var copyDescription: CoreFoundation.CFTreeCopyDescriptionCallBack! ``` |

Modified [CFTreeContext.info](https://developer.apple.com/documentation/corefoundation/cftreecontext/1401796-info)

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafeMutablePointer<Void> ``` |
| To | ``` var info: UnsafeMutableRawPointer! ``` |

Modified [CFTreeContext.release](https://developer.apple.com/documentation/corefoundation/cftreecontext/1401779-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFTreeReleaseCallBack! ``` |
| To | ``` var release: CoreFoundation.CFTreeReleaseCallBack! ``` |

Modified [CFTreeContext.retain](https://developer.apple.com/documentation/corefoundation/cftreecontext/1401767-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFTreeRetainCallBack! ``` |
| To | ``` var retain: CoreFoundation.CFTreeRetainCallBack! ``` |

Modified [CFURLBookmarkCreationOptions [struct]](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkcreationoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFURLBookmarkCreationOptions : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var MinimalBookmarkMask: CFURLBookmarkCreationOptions { get }     static var SuitableForBookmarkFile: CFURLBookmarkCreationOptions { get }     static var WithSecurityScope: CFURLBookmarkCreationOptions { get }     static var SecurityScopeAllowOnlyReadAccess: CFURLBookmarkCreationOptions { get }     static var PreferFileIDResolutionMask: CFURLBookmarkCreationOptions { get } } ``` | OptionSetType |
| To | ``` struct CFURLBookmarkCreationOptions : OptionSet {     init(rawValue rawValue: CFOptionFlags)     static var minimalBookmarkMask: CFURLBookmarkCreationOptions { get }     static var suitableForBookmarkFile: CFURLBookmarkCreationOptions { get }     static var withSecurityScope: CFURLBookmarkCreationOptions { get }     static var securityScopeAllowOnlyReadAccess: CFURLBookmarkCreationOptions { get }     static var preferFileIDResolutionMask: CFURLBookmarkCreationOptions { get }     func intersect(_ other: CFURLBookmarkCreationOptions) -> CFURLBookmarkCreationOptions     func exclusiveOr(_ other: CFURLBookmarkCreationOptions) -> CFURLBookmarkCreationOptions     mutating func unionInPlace(_ other: CFURLBookmarkCreationOptions)     mutating func intersectInPlace(_ other: CFURLBookmarkCreationOptions)     mutating func exclusiveOrInPlace(_ other: CFURLBookmarkCreationOptions)     func isSubsetOf(_ other: CFURLBookmarkCreationOptions) -> Bool     func isDisjointWith(_ other: CFURLBookmarkCreationOptions) -> Bool     func isSupersetOf(_ other: CFURLBookmarkCreationOptions) -> Bool     mutating func subtractInPlace(_ other: CFURLBookmarkCreationOptions)     func isStrictSupersetOf(_ other: CFURLBookmarkCreationOptions) -> Bool     func isStrictSubsetOf(_ other: CFURLBookmarkCreationOptions) -> Bool } extension CFURLBookmarkCreationOptions {     func union(_ other: CFURLBookmarkCreationOptions) -> CFURLBookmarkCreationOptions     func intersection(_ other: CFURLBookmarkCreationOptions) -> CFURLBookmarkCreationOptions     func symmetricDifference(_ other: CFURLBookmarkCreationOptions) -> CFURLBookmarkCreationOptions } extension CFURLBookmarkCreationOptions {     func contains(_ member: CFURLBookmarkCreationOptions) -> Bool     mutating func insert(_ newMember: CFURLBookmarkCreationOptions) -> (inserted: Bool, memberAfterInsert: CFURLBookmarkCreationOptions)     mutating func remove(_ member: CFURLBookmarkCreationOptions) -> CFURLBookmarkCreationOptions?     mutating func update(with newMember: CFURLBookmarkCreationOptions) -> CFURLBookmarkCreationOptions? } extension CFURLBookmarkCreationOptions {     convenience init()     mutating func formUnion(_ other: CFURLBookmarkCreationOptions)     mutating func formIntersection(_ other: CFURLBookmarkCreationOptions)     mutating func formSymmetricDifference(_ other: CFURLBookmarkCreationOptions) } extension CFURLBookmarkCreationOptions {     convenience init<S : Sequence where S.Iterator.Element == CFURLBookmarkCreationOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CFURLBookmarkCreationOptions...)     mutating func subtract(_ other: CFURLBookmarkCreationOptions)     func isSubset(of other: CFURLBookmarkCreationOptions) -> Bool     func isSuperset(of other: CFURLBookmarkCreationOptions) -> Bool     func isDisjoint(with other: CFURLBookmarkCreationOptions) -> Bool     func subtracting(_ other: CFURLBookmarkCreationOptions) -> CFURLBookmarkCreationOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: CFURLBookmarkCreationOptions) -> Bool     func isStrictSubset(of other: CFURLBookmarkCreationOptions) -> Bool } ``` | OptionSet |

Modified [CFURLBookmarkCreationOptions.minimalBookmarkMask](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkcreationoptions/1541966-minimalbookmarkmask)

|  | Declaration |
| --- | --- |
| From | ``` static var MinimalBookmarkMask: CFURLBookmarkCreationOptions { get } ``` |
| To | ``` static var minimalBookmarkMask: CFURLBookmarkCreationOptions { get } ``` |

Modified [CFURLBookmarkCreationOptions.suitableForBookmarkFile](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkcreationoptions/kcfurlbookmarkcreationsuitableforbookmarkfile)

|  | Declaration |
| --- | --- |
| From | ``` static var SuitableForBookmarkFile: CFURLBookmarkCreationOptions { get } ``` |
| To | ``` static var suitableForBookmarkFile: CFURLBookmarkCreationOptions { get } ``` |

Modified [CFURLBookmarkResolutionOptions [struct]](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkresolutionoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFURLBookmarkResolutionOptions : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var CFURLBookmarkResolutionWithoutUIMask: CFURLBookmarkResolutionOptions { get }     static var CFURLBookmarkResolutionWithoutMountingMask: CFURLBookmarkResolutionOptions { get }     static var CFURLBookmarkResolutionWithSecurityScope: CFURLBookmarkResolutionOptions { get }     static var CFBookmarkResolutionWithoutUIMask: CFURLBookmarkResolutionOptions { get }     static var CFBookmarkResolutionWithoutMountingMask: CFURLBookmarkResolutionOptions { get } } ``` | OptionSetType |
| To | ``` struct CFURLBookmarkResolutionOptions : OptionSet {     init(rawValue rawValue: CFOptionFlags)     static var cfurlBookmarkResolutionWithoutUIMask: CFURLBookmarkResolutionOptions { get }     static var cfurlBookmarkResolutionWithoutMountingMask: CFURLBookmarkResolutionOptions { get }     static var cfurlBookmarkResolutionWithSecurityScope: CFURLBookmarkResolutionOptions { get }     static var cfBookmarkResolutionWithoutUIMask: CFURLBookmarkResolutionOptions { get }     static var cfBookmarkResolutionWithoutMountingMask: CFURLBookmarkResolutionOptions { get }     func intersect(_ other: CFURLBookmarkResolutionOptions) -> CFURLBookmarkResolutionOptions     func exclusiveOr(_ other: CFURLBookmarkResolutionOptions) -> CFURLBookmarkResolutionOptions     mutating func unionInPlace(_ other: CFURLBookmarkResolutionOptions)     mutating func intersectInPlace(_ other: CFURLBookmarkResolutionOptions)     mutating func exclusiveOrInPlace(_ other: CFURLBookmarkResolutionOptions)     func isSubsetOf(_ other: CFURLBookmarkResolutionOptions) -> Bool     func isDisjointWith(_ other: CFURLBookmarkResolutionOptions) -> Bool     func isSupersetOf(_ other: CFURLBookmarkResolutionOptions) -> Bool     mutating func subtractInPlace(_ other: CFURLBookmarkResolutionOptions)     func isStrictSupersetOf(_ other: CFURLBookmarkResolutionOptions) -> Bool     func isStrictSubsetOf(_ other: CFURLBookmarkResolutionOptions) -> Bool } extension CFURLBookmarkResolutionOptions {     func union(_ other: CFURLBookmarkResolutionOptions) -> CFURLBookmarkResolutionOptions     func intersection(_ other: CFURLBookmarkResolutionOptions) -> CFURLBookmarkResolutionOptions     func symmetricDifference(_ other: CFURLBookmarkResolutionOptions) -> CFURLBookmarkResolutionOptions } extension CFURLBookmarkResolutionOptions {     func contains(_ member: CFURLBookmarkResolutionOptions) -> Bool     mutating func insert(_ newMember: CFURLBookmarkResolutionOptions) -> (inserted: Bool, memberAfterInsert: CFURLBookmarkResolutionOptions)     mutating func remove(_ member: CFURLBookmarkResolutionOptions) -> CFURLBookmarkResolutionOptions?     mutating func update(with newMember: CFURLBookmarkResolutionOptions) -> CFURLBookmarkResolutionOptions? } extension CFURLBookmarkResolutionOptions {     convenience init()     mutating func formUnion(_ other: CFURLBookmarkResolutionOptions)     mutating func formIntersection(_ other: CFURLBookmarkResolutionOptions)     mutating func formSymmetricDifference(_ other: CFURLBookmarkResolutionOptions) } extension CFURLBookmarkResolutionOptions {     convenience init<S : Sequence where S.Iterator.Element == CFURLBookmarkResolutionOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CFURLBookmarkResolutionOptions...)     mutating func subtract(_ other: CFURLBookmarkResolutionOptions)     func isSubset(of other: CFURLBookmarkResolutionOptions) -> Bool     func isSuperset(of other: CFURLBookmarkResolutionOptions) -> Bool     func isDisjoint(with other: CFURLBookmarkResolutionOptions) -> Bool     func subtracting(_ other: CFURLBookmarkResolutionOptions) -> CFURLBookmarkResolutionOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: CFURLBookmarkResolutionOptions) -> Bool     func isStrictSubset(of other: CFURLBookmarkResolutionOptions) -> Bool } ``` | OptionSet |

Modified [CFURLBookmarkResolutionOptions.cfBookmarkResolutionWithoutMountingMask](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkresolutionoptions/1541888-cfbookmarkresolutionwithoutmount)

|  | Declaration |
| --- | --- |
| From | ``` static var CFBookmarkResolutionWithoutMountingMask: CFURLBookmarkResolutionOptions { get } ``` |
| To | ``` static var cfBookmarkResolutionWithoutMountingMask: CFURLBookmarkResolutionOptions { get } ``` |

Modified [CFURLBookmarkResolutionOptions.cfBookmarkResolutionWithoutUIMask](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkresolutionoptions/kcfbookmarkresolutionwithoutuimask)

|  | Declaration |
| --- | --- |
| From | ``` static var CFBookmarkResolutionWithoutUIMask: CFURLBookmarkResolutionOptions { get } ``` |
| To | ``` static var cfBookmarkResolutionWithoutUIMask: CFURLBookmarkResolutionOptions { get } ``` |

Modified [CFURLBookmarkResolutionOptions.cfurlBookmarkResolutionWithoutMountingMask](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkresolutionoptions/1542479-cfurlbookmarkresolutionwithoutmo)

|  | Declaration |
| --- | --- |
| From | ``` static var CFURLBookmarkResolutionWithoutMountingMask: CFURLBookmarkResolutionOptions { get } ``` |
| To | ``` static var cfurlBookmarkResolutionWithoutMountingMask: CFURLBookmarkResolutionOptions { get } ``` |

Modified [CFURLBookmarkResolutionOptions.cfurlBookmarkResolutionWithoutUIMask](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkresolutionoptions/kcfurlbookmarkresolutionwithoutuimask)

|  | Declaration |
| --- | --- |
| From | ``` static var CFURLBookmarkResolutionWithoutUIMask: CFURLBookmarkResolutionOptions { get } ``` |
| To | ``` static var cfurlBookmarkResolutionWithoutUIMask: CFURLBookmarkResolutionOptions { get } ``` |

Modified [CFURLComponentType [enum]](https://developer.apple.com/documentation/corefoundation/cfurlcomponenttype)

|  | Declaration |
| --- | --- |
| From | ``` enum CFURLComponentType : CFIndex {     case Scheme     case NetLocation     case Path     case ResourceSpecifier     case User     case Password     case UserInfo     case Host     case Port     case ParameterString     case Query     case Fragment } ``` |
| To | ``` enum CFURLComponentType : CFIndex {     case scheme     case netLocation     case path     case resourceSpecifier     case user     case password     case userInfo     case host     case port     case parameterString     case query     case fragment } ``` |

Modified [CFURLComponentType.fragment](https://developer.apple.com/documentation/corefoundation/cfurlcomponenttype/kcfurlcomponentfragment)

|  | Declaration |
| --- | --- |
| From | ``` case Fragment ``` |
| To | ``` case fragment ``` |

Modified [CFURLComponentType.host](https://developer.apple.com/documentation/corefoundation/cfurlcomponenttype/host)

|  | Declaration |
| --- | --- |
| From | ``` case Host ``` |
| To | ``` case host ``` |

Modified [CFURLComponentType.netLocation](https://developer.apple.com/documentation/corefoundation/cfurlcomponenttype/netlocation)

|  | Declaration |
| --- | --- |
| From | ``` case NetLocation ``` |
| To | ``` case netLocation ``` |

Modified [CFURLComponentType.parameterString](https://developer.apple.com/documentation/corefoundation/cfurlcomponenttype/kcfurlcomponentparameterstring)

|  | Declaration |
| --- | --- |
| From | ``` case ParameterString ``` |
| To | ``` case parameterString ``` |

Modified [CFURLComponentType.password](https://developer.apple.com/documentation/corefoundation/cfurlcomponenttype/kcfurlcomponentpassword)

|  | Declaration |
| --- | --- |
| From | ``` case Password ``` |
| To | ``` case password ``` |

Modified [CFURLComponentType.path](https://developer.apple.com/documentation/corefoundation/cfurlcomponenttype/kcfurlcomponentpath)

|  | Declaration |
| --- | --- |
| From | ``` case Path ``` |
| To | ``` case path ``` |

Modified [CFURLComponentType.port](https://developer.apple.com/documentation/corefoundation/cfurlcomponenttype/kcfurlcomponentport)

|  | Declaration |
| --- | --- |
| From | ``` case Port ``` |
| To | ``` case port ``` |

Modified [CFURLComponentType.query](https://developer.apple.com/documentation/corefoundation/cfurlcomponenttype/query)

|  | Declaration |
| --- | --- |
| From | ``` case Query ``` |
| To | ``` case query ``` |

Modified [CFURLComponentType.resourceSpecifier](https://developer.apple.com/documentation/corefoundation/cfurlcomponenttype/resourcespecifier)

|  | Declaration |
| --- | --- |
| From | ``` case ResourceSpecifier ``` |
| To | ``` case resourceSpecifier ``` |

Modified [CFURLComponentType.scheme](https://developer.apple.com/documentation/corefoundation/cfurlcomponenttype/scheme)

|  | Declaration |
| --- | --- |
| From | ``` case Scheme ``` |
| To | ``` case scheme ``` |

Modified [CFURLComponentType.user](https://developer.apple.com/documentation/corefoundation/cfurlcomponenttype/kcfurlcomponentuser)

|  | Declaration |
| --- | --- |
| From | ``` case User ``` |
| To | ``` case user ``` |

Modified [CFURLComponentType.userInfo](https://developer.apple.com/documentation/corefoundation/cfurlcomponenttype/kcfurlcomponentuserinfo)

|  | Declaration |
| --- | --- |
| From | ``` case UserInfo ``` |
| To | ``` case userInfo ``` |

Modified [CFURLEnumeratorOptions [struct]](https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFURLEnumeratorOptions : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var DefaultBehavior: CFURLEnumeratorOptions { get }     static var DescendRecursively: CFURLEnumeratorOptions { get }     static var SkipInvisibles: CFURLEnumeratorOptions { get }     static var GenerateFileReferenceURLs: CFURLEnumeratorOptions { get }     static var SkipPackageContents: CFURLEnumeratorOptions { get }     static var IncludeDirectoriesPreOrder: CFURLEnumeratorOptions { get }     static var IncludeDirectoriesPostOrder: CFURLEnumeratorOptions { get } } ``` | OptionSetType |
| To | ``` struct CFURLEnumeratorOptions : OptionSet {     init(rawValue rawValue: CFOptionFlags)     static var defaultBehavior: CFURLEnumeratorOptions { get }     static var descendRecursively: CFURLEnumeratorOptions { get }     static var skipInvisibles: CFURLEnumeratorOptions { get }     static var generateFileReferenceURLs: CFURLEnumeratorOptions { get }     static var skipPackageContents: CFURLEnumeratorOptions { get }     static var includeDirectoriesPreOrder: CFURLEnumeratorOptions { get }     static var includeDirectoriesPostOrder: CFURLEnumeratorOptions { get }     func intersect(_ other: CFURLEnumeratorOptions) -> CFURLEnumeratorOptions     func exclusiveOr(_ other: CFURLEnumeratorOptions) -> CFURLEnumeratorOptions     mutating func unionInPlace(_ other: CFURLEnumeratorOptions)     mutating func intersectInPlace(_ other: CFURLEnumeratorOptions)     mutating func exclusiveOrInPlace(_ other: CFURLEnumeratorOptions)     func isSubsetOf(_ other: CFURLEnumeratorOptions) -> Bool     func isDisjointWith(_ other: CFURLEnumeratorOptions) -> Bool     func isSupersetOf(_ other: CFURLEnumeratorOptions) -> Bool     mutating func subtractInPlace(_ other: CFURLEnumeratorOptions)     func isStrictSupersetOf(_ other: CFURLEnumeratorOptions) -> Bool     func isStrictSubsetOf(_ other: CFURLEnumeratorOptions) -> Bool } extension CFURLEnumeratorOptions {     func union(_ other: CFURLEnumeratorOptions) -> CFURLEnumeratorOptions     func intersection(_ other: CFURLEnumeratorOptions) -> CFURLEnumeratorOptions     func symmetricDifference(_ other: CFURLEnumeratorOptions) -> CFURLEnumeratorOptions } extension CFURLEnumeratorOptions {     func contains(_ member: CFURLEnumeratorOptions) -> Bool     mutating func insert(_ newMember: CFURLEnumeratorOptions) -> (inserted: Bool, memberAfterInsert: CFURLEnumeratorOptions)     mutating func remove(_ member: CFURLEnumeratorOptions) -> CFURLEnumeratorOptions?     mutating func update(with newMember: CFURLEnumeratorOptions) -> CFURLEnumeratorOptions? } extension CFURLEnumeratorOptions {     convenience init()     mutating func formUnion(_ other: CFURLEnumeratorOptions)     mutating func formIntersection(_ other: CFURLEnumeratorOptions)     mutating func formSymmetricDifference(_ other: CFURLEnumeratorOptions) } extension CFURLEnumeratorOptions {     convenience init<S : Sequence where S.Iterator.Element == CFURLEnumeratorOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CFURLEnumeratorOptions...)     mutating func subtract(_ other: CFURLEnumeratorOptions)     func isSubset(of other: CFURLEnumeratorOptions) -> Bool     func isSuperset(of other: CFURLEnumeratorOptions) -> Bool     func isDisjoint(with other: CFURLEnumeratorOptions) -> Bool     func subtracting(_ other: CFURLEnumeratorOptions) -> CFURLEnumeratorOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: CFURLEnumeratorOptions) -> Bool     func isStrictSubset(of other: CFURLEnumeratorOptions) -> Bool } ``` | OptionSet |

Modified [CFURLEnumeratorOptions.descendRecursively](https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/1542771-descendrecursively)

|  | Declaration |
| --- | --- |
| From | ``` static var DescendRecursively: CFURLEnumeratorOptions { get } ``` |
| To | ``` static var descendRecursively: CFURLEnumeratorOptions { get } ``` |

Modified [CFURLEnumeratorOptions.generateFileReferenceURLs](https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/1543024-generatefilereferenceurls)

|  | Declaration |
| --- | --- |
| From | ``` static var GenerateFileReferenceURLs: CFURLEnumeratorOptions { get } ``` |
| To | ``` static var generateFileReferenceURLs: CFURLEnumeratorOptions { get } ``` |

Modified [CFURLEnumeratorOptions.includeDirectoriesPostOrder](https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/1542791-includedirectoriespostorder)

|  | Declaration |
| --- | --- |
| From | ``` static var IncludeDirectoriesPostOrder: CFURLEnumeratorOptions { get } ``` |
| To | ``` static var includeDirectoriesPostOrder: CFURLEnumeratorOptions { get } ``` |

Modified [CFURLEnumeratorOptions.includeDirectoriesPreOrder](https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/kcfurlenumeratorincludedirectoriespreorder)

|  | Declaration |
| --- | --- |
| From | ``` static var IncludeDirectoriesPreOrder: CFURLEnumeratorOptions { get } ``` |
| To | ``` static var includeDirectoriesPreOrder: CFURLEnumeratorOptions { get } ``` |

Modified [CFURLEnumeratorOptions.skipInvisibles](https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/1542108-skipinvisibles)

|  | Declaration |
| --- | --- |
| From | ``` static var SkipInvisibles: CFURLEnumeratorOptions { get } ``` |
| To | ``` static var skipInvisibles: CFURLEnumeratorOptions { get } ``` |

Modified [CFURLEnumeratorOptions.skipPackageContents](https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/kcfurlenumeratorskippackagecontents)

|  | Declaration |
| --- | --- |
| From | ``` static var SkipPackageContents: CFURLEnumeratorOptions { get } ``` |
| To | ``` static var skipPackageContents: CFURLEnumeratorOptions { get } ``` |

Modified [CFURLEnumeratorResult [enum]](https://developer.apple.com/documentation/corefoundation/cfurlenumeratorresult)

|  | Declaration |
| --- | --- |
| From | ``` enum CFURLEnumeratorResult : CFIndex {     case Success     case End     case Error     case DirectoryPostOrderSuccess } ``` |
| To | ``` enum CFURLEnumeratorResult : CFIndex {     case success     case end     case error     case directoryPostOrderSuccess } ``` |

Modified [CFURLEnumeratorResult.directoryPostOrderSuccess](https://developer.apple.com/documentation/corefoundation/cfurlenumeratorresult/directorypostordersuccess)

|  | Declaration |
| --- | --- |
| From | ``` case DirectoryPostOrderSuccess ``` |
| To | ``` case directoryPostOrderSuccess ``` |

Modified [CFURLEnumeratorResult.end](https://developer.apple.com/documentation/corefoundation/cfurlenumeratorresult/end)

|  | Declaration |
| --- | --- |
| From | ``` case End ``` |
| To | ``` case end ``` |

Modified [CFURLEnumeratorResult.error](https://developer.apple.com/documentation/corefoundation/cfurlenumeratorresult/kcfurlenumeratorerror)

|  | Declaration |
| --- | --- |
| From | ``` case Error ``` |
| To | ``` case error ``` |

Modified [CFURLEnumeratorResult.success](https://developer.apple.com/documentation/corefoundation/cfurlenumeratorresult/success)

|  | Declaration |
| --- | --- |
| From | ``` case Success ``` |
| To | ``` case success ``` |

Modified [CFURLPathStyle [enum]](https://developer.apple.com/documentation/corefoundation/cfurlpathstyle)

|  | Declaration |
| --- | --- |
| From | ``` enum CFURLPathStyle : CFIndex {     case CFURLPOSIXPathStyle     case CFURLHFSPathStyle     case CFURLWindowsPathStyle } ``` |
| To | ``` enum CFURLPathStyle : CFIndex {     case cfurlposixPathStyle     case cfurlhfsPathStyle     case cfurlWindowsPathStyle } ``` |

Modified [CFURLPathStyle.cfurlposixPathStyle](https://developer.apple.com/documentation/corefoundation/cfurlpathstyle/kcfurlposixpathstyle)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLPOSIXPathStyle ``` |
| To | ``` case cfurlposixPathStyle ``` |

Modified [CFURLPathStyle.cfurlWindowsPathStyle](https://developer.apple.com/documentation/corefoundation/cfurlpathstyle/kcfurlwindowspathstyle)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLWindowsPathStyle ``` |
| To | ``` case cfurlWindowsPathStyle ``` |

Modified [CFAllocatorAllocate(_: CFAllocator!, _: CFIndex, _: CFOptionFlags) -> UnsafeMutableRawPointer!](https://developer.apple.com/documentation/corefoundation/1521250-cfallocatorallocate)

|  | Declaration |
| --- | --- |
| From | ``` func CFAllocatorAllocate(_ allocator: CFAllocator!, _ size: CFIndex, _ hint: CFOptionFlags) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func CFAllocatorAllocate(_ allocator: CFAllocator!, _ size: CFIndex, _ hint: CFOptionFlags) -> UnsafeMutableRawPointer! ``` |

Modified [CFAllocatorAllocateCallBack](https://developer.apple.com/documentation/corefoundation/cfallocatorallocatecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFAllocatorAllocateCallBack = (CFIndex, CFOptionFlags, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void> ``` |
| To | ``` typealias CFAllocatorAllocateCallBack = (CFIndex, CFOptionFlags, UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer? ``` |

Modified [CFAllocatorCopyDescriptionCallBack](https://developer.apple.com/documentation/corefoundation/cfallocatorcopydescriptioncallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFAllocatorCopyDescriptionCallBack = (UnsafePointer<Void>) -> Unmanaged<CFString>! ``` |
| To | ``` typealias CFAllocatorCopyDescriptionCallBack = (UnsafeRawPointer?) -> Unmanaged<CFString>? ``` |

Modified [CFAllocatorCreate(_: CFAllocator!, _: UnsafeMutablePointer<CFAllocatorContext>!) -> Unmanaged<CFAllocator>!](https://developer.apple.com/documentation/corefoundation/1521159-cfallocatorcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFAllocatorCreate(_ allocator: CFAllocator!, _ context: UnsafeMutablePointer<CFAllocatorContext>) -> Unmanaged<CFAllocator>! ``` |
| To | ``` func CFAllocatorCreate(_ allocator: CFAllocator!, _ context: UnsafeMutablePointer<CFAllocatorContext>!) -> Unmanaged<CFAllocator>! ``` |

Modified [CFAllocatorDeallocate(_: CFAllocator!, _: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/corefoundation/1521299-cfallocatordeallocate)

|  | Declaration |
| --- | --- |
| From | ``` func CFAllocatorDeallocate(_ allocator: CFAllocator!, _ ptr: UnsafeMutablePointer<Void>) ``` |
| To | ``` func CFAllocatorDeallocate(_ allocator: CFAllocator!, _ ptr: UnsafeMutableRawPointer!) ``` |

Modified [CFAllocatorDeallocateCallBack](https://developer.apple.com/documentation/corefoundation/cfallocatordeallocatecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFAllocatorDeallocateCallBack = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CFAllocatorDeallocateCallBack = (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CFAllocatorGetContext(_: CFAllocator!, _: UnsafeMutablePointer<CFAllocatorContext>!)](https://developer.apple.com/documentation/corefoundation/1521267-cfallocatorgetcontext)

|  | Declaration |
| --- | --- |
| From | ``` func CFAllocatorGetContext(_ allocator: CFAllocator!, _ context: UnsafeMutablePointer<CFAllocatorContext>) ``` |
| To | ``` func CFAllocatorGetContext(_ allocator: CFAllocator!, _ context: UnsafeMutablePointer<CFAllocatorContext>!) ``` |

Modified [CFAllocatorPreferredSizeCallBack](https://developer.apple.com/documentation/corefoundation/cfallocatorpreferredsizecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFAllocatorPreferredSizeCallBack = (CFIndex, CFOptionFlags, UnsafeMutablePointer<Void>) -> CFIndex ``` |
| To | ``` typealias CFAllocatorPreferredSizeCallBack = (CFIndex, CFOptionFlags, UnsafeMutableRawPointer?) -> CFIndex ``` |

Modified [CFAllocatorReallocate(_: CFAllocator!, _: UnsafeMutableRawPointer!, _: CFIndex, _: CFOptionFlags) -> UnsafeMutableRawPointer!](https://developer.apple.com/documentation/corefoundation/1521324-cfallocatorreallocate)

|  | Declaration |
| --- | --- |
| From | ``` func CFAllocatorReallocate(_ allocator: CFAllocator!, _ ptr: UnsafeMutablePointer<Void>, _ newsize: CFIndex, _ hint: CFOptionFlags) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func CFAllocatorReallocate(_ allocator: CFAllocator!, _ ptr: UnsafeMutableRawPointer!, _ newsize: CFIndex, _ hint: CFOptionFlags) -> UnsafeMutableRawPointer! ``` |

Modified [CFAllocatorReallocateCallBack](https://developer.apple.com/documentation/corefoundation/cfallocatorreallocatecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFAllocatorReallocateCallBack = (UnsafeMutablePointer<Void>, CFIndex, CFOptionFlags, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void> ``` |
| To | ``` typealias CFAllocatorReallocateCallBack = (UnsafeMutableRawPointer?, CFIndex, CFOptionFlags, UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer? ``` |

Modified [CFAllocatorReleaseCallBack](https://developer.apple.com/documentation/corefoundation/cfallocatorreleasecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFAllocatorReleaseCallBack = (UnsafePointer<Void>) -> Void ``` |
| To | ``` typealias CFAllocatorReleaseCallBack = (UnsafeRawPointer?) -> Swift.Void ``` |

Modified [CFAllocatorRetainCallBack](https://developer.apple.com/documentation/corefoundation/cfallocatorretaincallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFAllocatorRetainCallBack = (UnsafePointer<Void>) -> UnsafePointer<Void> ``` |
| To | ``` typealias CFAllocatorRetainCallBack = (UnsafeRawPointer?) -> UnsafeRawPointer? ``` |

Modified [CFArrayAppendValue(_: CFMutableArray!, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/corefoundation/1388802-cfarrayappendvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayAppendValue(_ theArray: CFMutableArray!, _ value: UnsafePointer<Void>) ``` |
| To | ``` func CFArrayAppendValue(_ theArray: CFMutableArray!, _ value: UnsafeRawPointer!) ``` |

Modified [CFArrayApplierFunction](https://developer.apple.com/documentation/corefoundation/cfarrayapplierfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFArrayApplierFunction = (UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CFArrayApplierFunction = (UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CFArrayApplyFunction(_: CFArray!, _: CFRange, _: ((UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)!, _: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/corefoundation/1388737-cfarrayapplyfunction)

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayApplyFunction(_ theArray: CFArray!, _ range: CFRange, _ applier: CFArrayApplierFunction!, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func CFArrayApplyFunction(_ theArray: CFArray!, _ range: CFRange, _ applier: ((UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)!, _ context: UnsafeMutableRawPointer!) ``` |

Modified [CFArrayBSearchValues(_: CFArray!, _: CFRange, _: UnsafeRawPointer!, _: CoreFoundation.CFComparatorFunction!, _: UnsafeMutableRawPointer!) -> CFIndex](https://developer.apple.com/documentation/corefoundation/1388773-cfarraybsearchvalues)

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayBSearchValues(_ theArray: CFArray!, _ range: CFRange, _ value: UnsafePointer<Void>, _ comparator: CFComparatorFunction!, _ context: UnsafeMutablePointer<Void>) -> CFIndex ``` |
| To | ``` func CFArrayBSearchValues(_ theArray: CFArray!, _ range: CFRange, _ value: UnsafeRawPointer!, _ comparator: CoreFoundation.CFComparatorFunction!, _ context: UnsafeMutableRawPointer!) -> CFIndex ``` |

Modified [CFArrayContainsValue(_: CFArray!, _: CFRange, _: UnsafeRawPointer!) -> Bool](https://developer.apple.com/documentation/corefoundation/1388801-cfarraycontainsvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayContainsValue(_ theArray: CFArray!, _ range: CFRange, _ value: UnsafePointer<Void>) -> Bool ``` |
| To | ``` func CFArrayContainsValue(_ theArray: CFArray!, _ range: CFRange, _ value: UnsafeRawPointer!) -> Bool ``` |

Modified [CFArrayCopyDescriptionCallBack](https://developer.apple.com/documentation/corefoundation/cfarraycopydescriptioncallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFArrayCopyDescriptionCallBack = (UnsafePointer<Void>) -> Unmanaged<CFString>! ``` |
| To | ``` typealias CFArrayCopyDescriptionCallBack = (UnsafeRawPointer?) -> Unmanaged<CFString>? ``` |

Modified [CFArrayCreate(_: CFAllocator!, _: UnsafeMutablePointer<UnsafeRawPointer?>!, _: CFIndex, _: UnsafePointer<CFArrayCallBacks>!) -> CFArray!](https://developer.apple.com/documentation/corefoundation/1388741-cfarraycreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayCreate(_ allocator: CFAllocator!, _ values: UnsafeMutablePointer<UnsafePointer<Void>>, _ numValues: CFIndex, _ callBacks: UnsafePointer<CFArrayCallBacks>) -> CFArray! ``` |
| To | ``` func CFArrayCreate(_ allocator: CFAllocator!, _ values: UnsafeMutablePointer<UnsafeRawPointer?>!, _ numValues: CFIndex, _ callBacks: UnsafePointer<CFArrayCallBacks>!) -> CFArray! ``` |

Modified [CFArrayCreateMutable(_: CFAllocator!, _: CFIndex, _: UnsafePointer<CFArrayCallBacks>!) -> CFMutableArray!](https://developer.apple.com/documentation/corefoundation/1388770-cfarraycreatemutable)

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayCreateMutable(_ allocator: CFAllocator!, _ capacity: CFIndex, _ callBacks: UnsafePointer<CFArrayCallBacks>) -> CFMutableArray! ``` |
| To | ``` func CFArrayCreateMutable(_ allocator: CFAllocator!, _ capacity: CFIndex, _ callBacks: UnsafePointer<CFArrayCallBacks>!) -> CFMutableArray! ``` |

Modified [CFArrayEqualCallBack](https://developer.apple.com/documentation/corefoundation/cfarrayequalcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFArrayEqualCallBack = (UnsafePointer<Void>, UnsafePointer<Void>) -> DarwinBoolean ``` |
| To | ``` typealias CFArrayEqualCallBack = (UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean ``` |

Modified [CFArrayGetCountOfValue(_: CFArray!, _: CFRange, _: UnsafeRawPointer!) -> CFIndex](https://developer.apple.com/documentation/corefoundation/1388755-cfarraygetcountofvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayGetCountOfValue(_ theArray: CFArray!, _ range: CFRange, _ value: UnsafePointer<Void>) -> CFIndex ``` |
| To | ``` func CFArrayGetCountOfValue(_ theArray: CFArray!, _ range: CFRange, _ value: UnsafeRawPointer!) -> CFIndex ``` |

Modified [CFArrayGetFirstIndexOfValue(_: CFArray!, _: CFRange, _: UnsafeRawPointer!) -> CFIndex](https://developer.apple.com/documentation/corefoundation/1388782-cfarraygetfirstindexofvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayGetFirstIndexOfValue(_ theArray: CFArray!, _ range: CFRange, _ value: UnsafePointer<Void>) -> CFIndex ``` |
| To | ``` func CFArrayGetFirstIndexOfValue(_ theArray: CFArray!, _ range: CFRange, _ value: UnsafeRawPointer!) -> CFIndex ``` |

Modified [CFArrayGetLastIndexOfValue(_: CFArray!, _: CFRange, _: UnsafeRawPointer!) -> CFIndex](https://developer.apple.com/documentation/corefoundation/1388774-cfarraygetlastindexofvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayGetLastIndexOfValue(_ theArray: CFArray!, _ range: CFRange, _ value: UnsafePointer<Void>) -> CFIndex ``` |
| To | ``` func CFArrayGetLastIndexOfValue(_ theArray: CFArray!, _ range: CFRange, _ value: UnsafeRawPointer!) -> CFIndex ``` |

Modified [CFArrayGetValueAtIndex(_: CFArray!, _: CFIndex) -> UnsafeRawPointer!](https://developer.apple.com/documentation/corefoundation/1388767-cfarraygetvalueatindex)

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayGetValueAtIndex(_ theArray: CFArray!, _ idx: CFIndex) -> UnsafePointer<Void> ``` |
| To | ``` func CFArrayGetValueAtIndex(_ theArray: CFArray!, _ idx: CFIndex) -> UnsafeRawPointer! ``` |

Modified [CFArrayGetValues(_: CFArray!, _: CFRange, _: UnsafeMutablePointer<UnsafeRawPointer?>!)](https://developer.apple.com/documentation/corefoundation/1388769-cfarraygetvalues)

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayGetValues(_ theArray: CFArray!, _ range: CFRange, _ values: UnsafeMutablePointer<UnsafePointer<Void>>) ``` |
| To | ``` func CFArrayGetValues(_ theArray: CFArray!, _ range: CFRange, _ values: UnsafeMutablePointer<UnsafeRawPointer?>!) ``` |

Modified [CFArrayInsertValueAtIndex(_: CFMutableArray!, _: CFIndex, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/corefoundation/1388747-cfarrayinsertvalueatindex)

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayInsertValueAtIndex(_ theArray: CFMutableArray!, _ idx: CFIndex, _ value: UnsafePointer<Void>) ``` |
| To | ``` func CFArrayInsertValueAtIndex(_ theArray: CFMutableArray!, _ idx: CFIndex, _ value: UnsafeRawPointer!) ``` |

Modified [CFArrayReleaseCallBack](https://developer.apple.com/documentation/corefoundation/cfarrayreleasecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFArrayReleaseCallBack = (CFAllocator!, UnsafePointer<Void>) -> Void ``` |
| To | ``` typealias CFArrayReleaseCallBack = (CFAllocator?, UnsafeRawPointer?) -> Swift.Void ``` |

Modified [CFArrayReplaceValues(_: CFMutableArray!, _: CFRange, _: UnsafeMutablePointer<UnsafeRawPointer?>!, _: CFIndex)](https://developer.apple.com/documentation/corefoundation/1388757-cfarrayreplacevalues)

|  | Declaration |
| --- | --- |
| From | ``` func CFArrayReplaceValues(_ theArray: CFMutableArray!, _ range: CFRange, _ newValues: UnsafeMutablePointer<UnsafePointer<Void>>, _ newCount: CFIndex) ``` |
| To | ``` func CFArrayReplaceValues(_ theArray: CFMutableArray!, _ range: CFRange, _ newValues: UnsafeMutablePointer<UnsafeRawPointer?>!, _ newCount: CFIndex) ``` |

Modified [CFArrayRetainCallBack](https://developer.apple.com/documentation/corefoundation/cfarrayretaincallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFArrayRetainCallBack = (CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void> ``` |
| To | ``` typealias CFArrayRetainCallBack = (CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer? ``` |

Modified [CFArraySetValueAtIndex(_: CFMutableArray!, _: CFIndex, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/corefoundation/1388759-cfarraysetvalueatindex)

|  | Declaration |
| --- | --- |
| From | ``` func CFArraySetValueAtIndex(_ theArray: CFMutableArray!, _ idx: CFIndex, _ value: UnsafePointer<Void>) ``` |
| To | ``` func CFArraySetValueAtIndex(_ theArray: CFMutableArray!, _ idx: CFIndex, _ value: UnsafeRawPointer!) ``` |

Modified [CFArraySortValues(_: CFMutableArray!, _: CFRange, _: CoreFoundation.CFComparatorFunction!, _: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/corefoundation/1388749-cfarraysortvalues)

|  | Declaration |
| --- | --- |
| From | ``` func CFArraySortValues(_ theArray: CFMutableArray!, _ range: CFRange, _ comparator: CFComparatorFunction!, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func CFArraySortValues(_ theArray: CFMutableArray!, _ range: CFRange, _ comparator: CoreFoundation.CFComparatorFunction!, _ context: UnsafeMutableRawPointer!) ``` |

Modified [CFAttributedStringGetAttribute(_: CFAttributedString!, _: CFIndex, _: CFString!, _: UnsafeMutablePointer<CFRange>!) -> CFTypeRef!](https://developer.apple.com/documentation/corefoundation/1541978-cfattributedstringgetattribute)

|  | Declaration |
| --- | --- |
| From | ``` func CFAttributedStringGetAttribute(_ aStr: CFAttributedString!, _ loc: CFIndex, _ attrName: CFString!, _ effectiveRange: UnsafeMutablePointer<CFRange>) -> AnyObject! ``` |
| To | ``` func CFAttributedStringGetAttribute(_ aStr: CFAttributedString!, _ loc: CFIndex, _ attrName: CFString!, _ effectiveRange: UnsafeMutablePointer<CFRange>!) -> CFTypeRef! ``` |

Modified [CFAttributedStringGetAttributeAndLongestEffectiveRange(_: CFAttributedString!, _: CFIndex, _: CFString!, _: CFRange, _: UnsafeMutablePointer<CFRange>!) -> CFTypeRef!](https://developer.apple.com/documentation/corefoundation/1543465-cfattributedstringgetattributean)

|  | Declaration |
| --- | --- |
| From | ``` func CFAttributedStringGetAttributeAndLongestEffectiveRange(_ aStr: CFAttributedString!, _ loc: CFIndex, _ attrName: CFString!, _ inRange: CFRange, _ longestEffectiveRange: UnsafeMutablePointer<CFRange>) -> AnyObject! ``` |
| To | ``` func CFAttributedStringGetAttributeAndLongestEffectiveRange(_ aStr: CFAttributedString!, _ loc: CFIndex, _ attrName: CFString!, _ inRange: CFRange, _ longestEffectiveRange: UnsafeMutablePointer<CFRange>!) -> CFTypeRef! ``` |

Modified [CFAttributedStringGetAttributes(_: CFAttributedString!, _: CFIndex, _: UnsafeMutablePointer<CFRange>!) -> CFDictionary!](https://developer.apple.com/documentation/corefoundation/1542215-cfattributedstringgetattributes)

|  | Declaration |
| --- | --- |
| From | ``` func CFAttributedStringGetAttributes(_ aStr: CFAttributedString!, _ loc: CFIndex, _ effectiveRange: UnsafeMutablePointer<CFRange>) -> CFDictionary! ``` |
| To | ``` func CFAttributedStringGetAttributes(_ aStr: CFAttributedString!, _ loc: CFIndex, _ effectiveRange: UnsafeMutablePointer<CFRange>!) -> CFDictionary! ``` |

Modified [CFAttributedStringGetAttributesAndLongestEffectiveRange(_: CFAttributedString!, _: CFIndex, _: CFRange, _: UnsafeMutablePointer<CFRange>!) -> CFDictionary!](https://developer.apple.com/documentation/corefoundation/1542790-cfattributedstringgetattributesa)

|  | Declaration |
| --- | --- |
| From | ``` func CFAttributedStringGetAttributesAndLongestEffectiveRange(_ aStr: CFAttributedString!, _ loc: CFIndex, _ inRange: CFRange, _ longestEffectiveRange: UnsafeMutablePointer<CFRange>) -> CFDictionary! ``` |
| To | ``` func CFAttributedStringGetAttributesAndLongestEffectiveRange(_ aStr: CFAttributedString!, _ loc: CFIndex, _ inRange: CFRange, _ longestEffectiveRange: UnsafeMutablePointer<CFRange>!) -> CFDictionary! ``` |

Modified [CFAttributedStringSetAttribute(_: CFMutableAttributedString!, _: CFRange, _: CFString!, _: CFTypeRef!)](https://developer.apple.com/documentation/corefoundation/1542905-cfattributedstringsetattribute)

|  | Declaration |
| --- | --- |
| From | ``` func CFAttributedStringSetAttribute(_ aStr: CFMutableAttributedString!, _ range: CFRange, _ attrName: CFString!, _ value: AnyObject!) ``` |
| To | ``` func CFAttributedStringSetAttribute(_ aStr: CFMutableAttributedString!, _ range: CFRange, _ attrName: CFString!, _ value: CFTypeRef!) ``` |

Modified [CFBagAddValue(_: CFMutableBag!, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/corefoundation/1469297-cfbagaddvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFBagAddValue(_ theBag: CFMutableBag!, _ value: UnsafePointer<Void>) ``` |
| To | ``` func CFBagAddValue(_ theBag: CFMutableBag!, _ value: UnsafeRawPointer!) ``` |

Modified [CFBagApplierFunction](https://developer.apple.com/documentation/corefoundation/cfbagapplierfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFBagApplierFunction = (UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CFBagApplierFunction = (UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CFBagApplyFunction(_: CFBag!, _: ((UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)!, _: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/corefoundation/1469283-cfbagapplyfunction)

|  | Declaration |
| --- | --- |
| From | ``` func CFBagApplyFunction(_ theBag: CFBag!, _ applier: CFBagApplierFunction!, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func CFBagApplyFunction(_ theBag: CFBag!, _ applier: ((UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)!, _ context: UnsafeMutableRawPointer!) ``` |

Modified [CFBagContainsValue(_: CFBag!, _: UnsafeRawPointer!) -> Bool](https://developer.apple.com/documentation/corefoundation/1469322-cfbagcontainsvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFBagContainsValue(_ theBag: CFBag!, _ value: UnsafePointer<Void>) -> Bool ``` |
| To | ``` func CFBagContainsValue(_ theBag: CFBag!, _ value: UnsafeRawPointer!) -> Bool ``` |

Modified [CFBagCopyDescriptionCallBack](https://developer.apple.com/documentation/corefoundation/cfbagcopydescriptioncallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFBagCopyDescriptionCallBack = (UnsafePointer<Void>) -> Unmanaged<CFString>! ``` |
| To | ``` typealias CFBagCopyDescriptionCallBack = (UnsafeRawPointer?) -> Unmanaged<CFString>? ``` |

Modified [CFBagCreate(_: CFAllocator!, _: UnsafeMutablePointer<UnsafeRawPointer?>!, _: CFIndex, _: UnsafePointer<CFBagCallBacks>!) -> CFBag!](https://developer.apple.com/documentation/corefoundation/1469274-cfbagcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFBagCreate(_ allocator: CFAllocator!, _ values: UnsafeMutablePointer<UnsafePointer<Void>>, _ numValues: CFIndex, _ callBacks: UnsafePointer<CFBagCallBacks>) -> CFBag! ``` |
| To | ``` func CFBagCreate(_ allocator: CFAllocator!, _ values: UnsafeMutablePointer<UnsafeRawPointer?>!, _ numValues: CFIndex, _ callBacks: UnsafePointer<CFBagCallBacks>!) -> CFBag! ``` |

Modified [CFBagCreateMutable(_: CFAllocator!, _: CFIndex, _: UnsafePointer<CFBagCallBacks>!) -> CFMutableBag!](https://developer.apple.com/documentation/corefoundation/1469295-cfbagcreatemutable)

|  | Declaration |
| --- | --- |
| From | ``` func CFBagCreateMutable(_ allocator: CFAllocator!, _ capacity: CFIndex, _ callBacks: UnsafePointer<CFBagCallBacks>) -> CFMutableBag! ``` |
| To | ``` func CFBagCreateMutable(_ allocator: CFAllocator!, _ capacity: CFIndex, _ callBacks: UnsafePointer<CFBagCallBacks>!) -> CFMutableBag! ``` |

Modified [CFBagEqualCallBack](https://developer.apple.com/documentation/corefoundation/cfbagequalcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFBagEqualCallBack = (UnsafePointer<Void>, UnsafePointer<Void>) -> DarwinBoolean ``` |
| To | ``` typealias CFBagEqualCallBack = (UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean ``` |

Modified [CFBagGetCountOfValue(_: CFBag!, _: UnsafeRawPointer!) -> CFIndex](https://developer.apple.com/documentation/corefoundation/1469254-cfbaggetcountofvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFBagGetCountOfValue(_ theBag: CFBag!, _ value: UnsafePointer<Void>) -> CFIndex ``` |
| To | ``` func CFBagGetCountOfValue(_ theBag: CFBag!, _ value: UnsafeRawPointer!) -> CFIndex ``` |

Modified [CFBagGetValue(_: CFBag!, _: UnsafeRawPointer!) -> UnsafeRawPointer!](https://developer.apple.com/documentation/corefoundation/1469280-cfbaggetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFBagGetValue(_ theBag: CFBag!, _ value: UnsafePointer<Void>) -> UnsafePointer<Void> ``` |
| To | ``` func CFBagGetValue(_ theBag: CFBag!, _ value: UnsafeRawPointer!) -> UnsafeRawPointer! ``` |

Modified [CFBagGetValueIfPresent(_: CFBag!, _: UnsafeRawPointer!, _: UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1469314-cfbaggetvalueifpresent)

|  | Declaration |
| --- | --- |
| From | ``` func CFBagGetValueIfPresent(_ theBag: CFBag!, _ candidate: UnsafePointer<Void>, _ value: UnsafeMutablePointer<UnsafePointer<Void>>) -> Bool ``` |
| To | ``` func CFBagGetValueIfPresent(_ theBag: CFBag!, _ candidate: UnsafeRawPointer!, _ value: UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool ``` |

Modified [CFBagGetValues(_: CFBag!, _: UnsafeMutablePointer<UnsafeRawPointer?>!)](https://developer.apple.com/documentation/corefoundation/1469262-cfbaggetvalues)

|  | Declaration |
| --- | --- |
| From | ``` func CFBagGetValues(_ theBag: CFBag!, _ values: UnsafeMutablePointer<UnsafePointer<Void>>) ``` |
| To | ``` func CFBagGetValues(_ theBag: CFBag!, _ values: UnsafeMutablePointer<UnsafeRawPointer?>!) ``` |

Modified [CFBagHashCallBack](https://developer.apple.com/documentation/corefoundation/cfbaghashcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFBagHashCallBack = (UnsafePointer<Void>) -> CFHashCode ``` |
| To | ``` typealias CFBagHashCallBack = (UnsafeRawPointer?) -> CFHashCode ``` |

Modified [CFBagReleaseCallBack](https://developer.apple.com/documentation/corefoundation/cfbagreleasecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFBagReleaseCallBack = (CFAllocator!, UnsafePointer<Void>) -> Void ``` |
| To | ``` typealias CFBagReleaseCallBack = (CFAllocator?, UnsafeRawPointer?) -> Swift.Void ``` |

Modified [CFBagRemoveValue(_: CFMutableBag!, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/corefoundation/1469270-cfbagremovevalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFBagRemoveValue(_ theBag: CFMutableBag!, _ value: UnsafePointer<Void>) ``` |
| To | ``` func CFBagRemoveValue(_ theBag: CFMutableBag!, _ value: UnsafeRawPointer!) ``` |

Modified [CFBagReplaceValue(_: CFMutableBag!, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/corefoundation/1469272-cfbagreplacevalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFBagReplaceValue(_ theBag: CFMutableBag!, _ value: UnsafePointer<Void>) ``` |
| To | ``` func CFBagReplaceValue(_ theBag: CFMutableBag!, _ value: UnsafeRawPointer!) ``` |

Modified [CFBagRetainCallBack](https://developer.apple.com/documentation/corefoundation/cfbagretaincallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFBagRetainCallBack = (CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void> ``` |
| To | ``` typealias CFBagRetainCallBack = (CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer? ``` |

Modified [CFBagSetValue(_: CFMutableBag!, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/corefoundation/1469320-cfbagsetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFBagSetValue(_ theBag: CFMutableBag!, _ value: UnsafePointer<Void>) ``` |
| To | ``` func CFBagSetValue(_ theBag: CFMutableBag!, _ value: UnsafeRawPointer!) ``` |

Modified [CFBinaryHeapAddValue(_: CFBinaryHeap!, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/corefoundation/1509317-cfbinaryheapaddvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFBinaryHeapAddValue(_ heap: CFBinaryHeap!, _ value: UnsafePointer<Void>) ``` |
| To | ``` func CFBinaryHeapAddValue(_ heap: CFBinaryHeap!, _ value: UnsafeRawPointer!) ``` |

Modified [CFBinaryHeapApplierFunction](https://developer.apple.com/documentation/corefoundation/cfbinaryheapapplierfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFBinaryHeapApplierFunction = (UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CFBinaryHeapApplierFunction = (UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CFBinaryHeapApplyFunction(_: CFBinaryHeap!, _: ((UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)!, _: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/corefoundation/1509308-cfbinaryheapapplyfunction)

|  | Declaration |
| --- | --- |
| From | ``` func CFBinaryHeapApplyFunction(_ heap: CFBinaryHeap!, _ applier: CFBinaryHeapApplierFunction!, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func CFBinaryHeapApplyFunction(_ heap: CFBinaryHeap!, _ applier: ((UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)!, _ context: UnsafeMutableRawPointer!) ``` |

Modified [CFBinaryHeapContainsValue(_: CFBinaryHeap!, _: UnsafeRawPointer!) -> Bool](https://developer.apple.com/documentation/corefoundation/1509305-cfbinaryheapcontainsvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFBinaryHeapContainsValue(_ heap: CFBinaryHeap!, _ value: UnsafePointer<Void>) -> Bool ``` |
| To | ``` func CFBinaryHeapContainsValue(_ heap: CFBinaryHeap!, _ value: UnsafeRawPointer!) -> Bool ``` |

Modified [CFBinaryHeapCreate(_: CFAllocator!, _: CFIndex, _: UnsafePointer<CFBinaryHeapCallBacks>!, _: UnsafePointer<CFBinaryHeapCompareContext>!) -> CFBinaryHeap!](https://developer.apple.com/documentation/corefoundation/1509301-cfbinaryheapcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFBinaryHeapCreate(_ allocator: CFAllocator!, _ capacity: CFIndex, _ callBacks: UnsafePointer<CFBinaryHeapCallBacks>, _ compareContext: UnsafePointer<CFBinaryHeapCompareContext>) -> CFBinaryHeap! ``` |
| To | ``` func CFBinaryHeapCreate(_ allocator: CFAllocator!, _ capacity: CFIndex, _ callBacks: UnsafePointer<CFBinaryHeapCallBacks>!, _ compareContext: UnsafePointer<CFBinaryHeapCompareContext>!) -> CFBinaryHeap! ``` |

Modified [CFBinaryHeapGetCountOfValue(_: CFBinaryHeap!, _: UnsafeRawPointer!) -> CFIndex](https://developer.apple.com/documentation/corefoundation/1509320-cfbinaryheapgetcountofvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFBinaryHeapGetCountOfValue(_ heap: CFBinaryHeap!, _ value: UnsafePointer<Void>) -> CFIndex ``` |
| To | ``` func CFBinaryHeapGetCountOfValue(_ heap: CFBinaryHeap!, _ value: UnsafeRawPointer!) -> CFIndex ``` |

Modified [CFBinaryHeapGetMinimum(_: CFBinaryHeap!) -> UnsafeRawPointer!](https://developer.apple.com/documentation/corefoundation/1509325-cfbinaryheapgetminimum)

|  | Declaration |
| --- | --- |
| From | ``` func CFBinaryHeapGetMinimum(_ heap: CFBinaryHeap!) -> UnsafePointer<Void> ``` |
| To | ``` func CFBinaryHeapGetMinimum(_ heap: CFBinaryHeap!) -> UnsafeRawPointer! ``` |

Modified [CFBinaryHeapGetMinimumIfPresent(_: CFBinaryHeap!, _: UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1509310-cfbinaryheapgetminimumifpresent)

|  | Declaration |
| --- | --- |
| From | ``` func CFBinaryHeapGetMinimumIfPresent(_ heap: CFBinaryHeap!, _ value: UnsafeMutablePointer<UnsafePointer<Void>>) -> Bool ``` |
| To | ``` func CFBinaryHeapGetMinimumIfPresent(_ heap: CFBinaryHeap!, _ value: UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool ``` |

Modified [CFBinaryHeapGetValues(_: CFBinaryHeap!, _: UnsafeMutablePointer<UnsafeRawPointer?>!)](https://developer.apple.com/documentation/corefoundation/1509303-cfbinaryheapgetvalues)

|  | Declaration |
| --- | --- |
| From | ``` func CFBinaryHeapGetValues(_ heap: CFBinaryHeap!, _ values: UnsafeMutablePointer<UnsafePointer<Void>>) ``` |
| To | ``` func CFBinaryHeapGetValues(_ heap: CFBinaryHeap!, _ values: UnsafeMutablePointer<UnsafeRawPointer?>!) ``` |

Modified [CFBitVectorCreate(_: CFAllocator!, _: UnsafePointer<UInt8>!, _: CFIndex) -> CFBitVector!](https://developer.apple.com/documentation/corefoundation/1543718-cfbitvectorcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFBitVectorCreate(_ allocator: CFAllocator!, _ bytes: UnsafePointer<UInt8>, _ numBits: CFIndex) -> CFBitVector! ``` |
| To | ``` func CFBitVectorCreate(_ allocator: CFAllocator!, _ bytes: UnsafePointer<UInt8>!, _ numBits: CFIndex) -> CFBitVector! ``` |

Modified [CFBitVectorGetBits(_: CFBitVector!, _: CFRange, _: UnsafeMutablePointer<UInt8>!)](https://developer.apple.com/documentation/corefoundation/1543663-cfbitvectorgetbits)

|  | Declaration |
| --- | --- |
| From | ``` func CFBitVectorGetBits(_ bv: CFBitVector!, _ range: CFRange, _ bytes: UnsafeMutablePointer<UInt8>) ``` |
| To | ``` func CFBitVectorGetBits(_ bv: CFBitVector!, _ range: CFRange, _ bytes: UnsafeMutablePointer<UInt8>!) ``` |

Modified [CFBundleGetDataPointerForName(_: CFBundle!, _: CFString!) -> UnsafeMutableRawPointer!](https://developer.apple.com/documentation/corefoundation/1537120-cfbundlegetdatapointerforname)

|  | Declaration |
| --- | --- |
| From | ``` func CFBundleGetDataPointerForName(_ bundle: CFBundle!, _ symbolName: CFString!) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func CFBundleGetDataPointerForName(_ bundle: CFBundle!, _ symbolName: CFString!) -> UnsafeMutableRawPointer! ``` |

Modified [CFBundleGetDataPointersForNames(_: CFBundle!, _: CFArray!, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!)](https://developer.apple.com/documentation/corefoundation/1537150-cfbundlegetdatapointersfornames)

|  | Declaration |
| --- | --- |
| From | ``` func CFBundleGetDataPointersForNames(_ bundle: CFBundle!, _ symbolNames: CFArray!, _ stbl: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) ``` |
| To | ``` func CFBundleGetDataPointersForNames(_ bundle: CFBundle!, _ symbolNames: CFArray!, _ stbl: UnsafeMutablePointer<UnsafeMutableRawPointer?>!) ``` |

Modified [CFBundleGetFunctionPointerForName(_: CFBundle!, _: CFString!) -> UnsafeMutableRawPointer!](https://developer.apple.com/documentation/corefoundation/1537143-cfbundlegetfunctionpointerfornam)

|  | Declaration |
| --- | --- |
| From | ``` func CFBundleGetFunctionPointerForName(_ bundle: CFBundle!, _ functionName: CFString!) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func CFBundleGetFunctionPointerForName(_ bundle: CFBundle!, _ functionName: CFString!) -> UnsafeMutableRawPointer! ``` |

Modified [CFBundleGetFunctionPointersForNames(_: CFBundle!, _: CFArray!, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!)](https://developer.apple.com/documentation/corefoundation/1537109-cfbundlegetfunctionpointersforna)

|  | Declaration |
| --- | --- |
| From | ``` func CFBundleGetFunctionPointersForNames(_ bundle: CFBundle!, _ functionNames: CFArray!, _ ftbl: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) ``` |
| To | ``` func CFBundleGetFunctionPointersForNames(_ bundle: CFBundle!, _ functionNames: CFArray!, _ ftbl: UnsafeMutablePointer<UnsafeMutableRawPointer?>!) ``` |

Modified [CFBundleGetPackageInfo(_: CFBundle!, _: UnsafeMutablePointer<UInt32>!, _: UnsafeMutablePointer<UInt32>!)](https://developer.apple.com/documentation/corefoundation/1537089-cfbundlegetpackageinfo)

|  | Declaration |
| --- | --- |
| From | ``` func CFBundleGetPackageInfo(_ bundle: CFBundle!, _ packageType: UnsafeMutablePointer<UInt32>, _ packageCreator: UnsafeMutablePointer<UInt32>) ``` |
| To | ``` func CFBundleGetPackageInfo(_ bundle: CFBundle!, _ packageType: UnsafeMutablePointer<UInt32>!, _ packageCreator: UnsafeMutablePointer<UInt32>!) ``` |

Modified [CFBundleGetPackageInfoInDirectory(_: CFURL!, _: UnsafeMutablePointer<UInt32>!, _: UnsafeMutablePointer<UInt32>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1537156-cfbundlegetpackageinfoindirector)

|  | Declaration |
| --- | --- |
| From | ``` func CFBundleGetPackageInfoInDirectory(_ url: CFURL!, _ packageType: UnsafeMutablePointer<UInt32>, _ packageCreator: UnsafeMutablePointer<UInt32>) -> Bool ``` |
| To | ``` func CFBundleGetPackageInfoInDirectory(_ url: CFURL!, _ packageType: UnsafeMutablePointer<UInt32>!, _ packageCreator: UnsafeMutablePointer<UInt32>!) -> Bool ``` |

Modified [CFBundleGetValueForInfoDictionaryKey(_: CFBundle!, _: CFString!) -> CFTypeRef!](https://developer.apple.com/documentation/corefoundation/1537102-cfbundlegetvalueforinfodictionar)

|  | Declaration |
| --- | --- |
| From | ``` func CFBundleGetValueForInfoDictionaryKey(_ bundle: CFBundle!, _ key: CFString!) -> AnyObject! ``` |
| To | ``` func CFBundleGetValueForInfoDictionaryKey(_ bundle: CFBundle!, _ key: CFString!) -> CFTypeRef! ``` |

Modified [CFBundleLoadExecutableAndReturnError(_: CFBundle!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1537114-cfbundleloadexecutableandreturne)

|  | Declaration |
| --- | --- |
| From | ``` func CFBundleLoadExecutableAndReturnError(_ bundle: CFBundle!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func CFBundleLoadExecutableAndReturnError(_ bundle: CFBundle!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [CFBundleOpenBundleResourceFiles(_: CFBundle!, _: UnsafeMutablePointer<CFBundleRefNum>!, _: UnsafeMutablePointer<CFBundleRefNum>!) -> Int32](https://developer.apple.com/documentation/corefoundation/1537123-cfbundleopenbundleresourcefiles)

|  | Declaration |
| --- | --- |
| From | ``` func CFBundleOpenBundleResourceFiles(_ bundle: CFBundle!, _ refNum: UnsafeMutablePointer<CFBundleRefNum>, _ localizedRefNum: UnsafeMutablePointer<CFBundleRefNum>) -> Int32 ``` |
| To | ``` func CFBundleOpenBundleResourceFiles(_ bundle: CFBundle!, _ refNum: UnsafeMutablePointer<CFBundleRefNum>!, _ localizedRefNum: UnsafeMutablePointer<CFBundleRefNum>!) -> Int32 ``` |

Modified [CFBundlePreflightExecutable(_: CFBundle!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1537128-cfbundlepreflightexecutable)

|  | Declaration |
| --- | --- |
| From | ``` func CFBundlePreflightExecutable(_ bundle: CFBundle!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func CFBundlePreflightExecutable(_ bundle: CFBundle!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [CFCalendarCreateWithIdentifier(_: CFAllocator!, _: CFCalendarIdentifier!) -> CFCalendar!](https://developer.apple.com/documentation/corefoundation/1533511-cfcalendarcreatewithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func CFCalendarCreateWithIdentifier(_ allocator: CFAllocator!, _ identifier: CFString!) -> CFCalendar! ``` |
| To | ``` func CFCalendarCreateWithIdentifier(_ allocator: CFAllocator!, _ identifier: CFCalendarIdentifier!) -> CFCalendar! ``` |

Modified [CFCalendarGetIdentifier(_: CFCalendar!) -> CFCalendarIdentifier!](https://developer.apple.com/documentation/corefoundation/1533495-cfcalendargetidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func CFCalendarGetIdentifier(_ calendar: CFCalendar!) -> CFString! ``` |
| To | ``` func CFCalendarGetIdentifier(_ calendar: CFCalendar!) -> CFCalendarIdentifier! ``` |

Modified [CFCalendarGetTimeRangeOfUnit(_: CFCalendar!, _: CFCalendarUnit, _: CFAbsoluteTime, _: UnsafeMutablePointer<CFAbsoluteTime>!, _: UnsafeMutablePointer<CFTimeInterval>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1533501-cfcalendargettimerangeofunit)

|  | Declaration |
| --- | --- |
| From | ``` func CFCalendarGetTimeRangeOfUnit(_ calendar: CFCalendar!, _ unit: CFCalendarUnit, _ at: CFAbsoluteTime, _ startp: UnsafeMutablePointer<CFAbsoluteTime>, _ tip: UnsafeMutablePointer<CFTimeInterval>) -> Bool ``` |
| To | ``` func CFCalendarGetTimeRangeOfUnit(_ calendar: CFCalendar!, _ unit: CFCalendarUnit, _ at: CFAbsoluteTime, _ startp: UnsafeMutablePointer<CFAbsoluteTime>!, _ tip: UnsafeMutablePointer<CFTimeInterval>!) -> Bool ``` |

Modified [CFComparatorFunction](https://developer.apple.com/documentation/corefoundation/cfcomparatorfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFComparatorFunction = (UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> CFComparisonResult ``` |
| To | ``` typealias CFComparatorFunction = (UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> CFComparisonResult ``` |

Modified [CFCopyDescription(_: CFTypeRef!) -> CFString!](https://developer.apple.com/documentation/corefoundation/1521252-cfcopydescription)

|  | Declaration |
| --- | --- |
| From | ``` func CFCopyDescription(_ cf: AnyObject!) -> CFString! ``` |
| To | ``` func CFCopyDescription(_ cf: CFTypeRef!) -> CFString! ``` |

Modified [CFDataAppendBytes(_: CFMutableData!, _: UnsafePointer<UInt8>!, _: CFIndex)](https://developer.apple.com/documentation/corefoundation/1541769-cfdataappendbytes)

|  | Declaration |
| --- | --- |
| From | ``` func CFDataAppendBytes(_ theData: CFMutableData!, _ bytes: UnsafePointer<UInt8>, _ length: CFIndex) ``` |
| To | ``` func CFDataAppendBytes(_ theData: CFMutableData!, _ bytes: UnsafePointer<UInt8>!, _ length: CFIndex) ``` |

Modified [CFDataCreate(_: CFAllocator!, _: UnsafePointer<UInt8>!, _: CFIndex) -> CFData!](https://developer.apple.com/documentation/corefoundation/1542359-cfdatacreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFDataCreate(_ allocator: CFAllocator!, _ bytes: UnsafePointer<UInt8>, _ length: CFIndex) -> CFData! ``` |
| To | ``` func CFDataCreate(_ allocator: CFAllocator!, _ bytes: UnsafePointer<UInt8>!, _ length: CFIndex) -> CFData! ``` |

Modified [CFDataCreateWithBytesNoCopy(_: CFAllocator!, _: UnsafePointer<UInt8>!, _: CFIndex, _: CFAllocator!) -> CFData!](https://developer.apple.com/documentation/corefoundation/1541971-cfdatacreatewithbytesnocopy)

|  | Declaration |
| --- | --- |
| From | ``` func CFDataCreateWithBytesNoCopy(_ allocator: CFAllocator!, _ bytes: UnsafePointer<UInt8>, _ length: CFIndex, _ bytesDeallocator: CFAllocator!) -> CFData! ``` |
| To | ``` func CFDataCreateWithBytesNoCopy(_ allocator: CFAllocator!, _ bytes: UnsafePointer<UInt8>!, _ length: CFIndex, _ bytesDeallocator: CFAllocator!) -> CFData! ``` |

Modified [CFDataGetBytePtr(_: CFData!) -> UnsafePointer<UInt8>!](https://developer.apple.com/documentation/corefoundation/1543330-cfdatagetbyteptr)

|  | Declaration |
| --- | --- |
| From | ``` func CFDataGetBytePtr(_ theData: CFData!) -> UnsafePointer<UInt8> ``` |
| To | ``` func CFDataGetBytePtr(_ theData: CFData!) -> UnsafePointer<UInt8>! ``` |

Modified [CFDataGetBytes(_: CFData!, _: CFRange, _: UnsafeMutablePointer<UInt8>!)](https://developer.apple.com/documentation/corefoundation/1541940-cfdatagetbytes)

|  | Declaration |
| --- | --- |
| From | ``` func CFDataGetBytes(_ theData: CFData!, _ range: CFRange, _ buffer: UnsafeMutablePointer<UInt8>) ``` |
| To | ``` func CFDataGetBytes(_ theData: CFData!, _ range: CFRange, _ buffer: UnsafeMutablePointer<UInt8>!) ``` |

Modified [CFDataGetMutableBytePtr(_: CFMutableData!) -> UnsafeMutablePointer<UInt8>!](https://developer.apple.com/documentation/corefoundation/1542870-cfdatagetmutablebyteptr)

|  | Declaration |
| --- | --- |
| From | ``` func CFDataGetMutableBytePtr(_ theData: CFMutableData!) -> UnsafeMutablePointer<UInt8> ``` |
| To | ``` func CFDataGetMutableBytePtr(_ theData: CFMutableData!) -> UnsafeMutablePointer<UInt8>! ``` |

Modified [CFDataReplaceBytes(_: CFMutableData!, _: CFRange, _: UnsafePointer<UInt8>!, _: CFIndex)](https://developer.apple.com/documentation/corefoundation/1543650-cfdatareplacebytes)

|  | Declaration |
| --- | --- |
| From | ``` func CFDataReplaceBytes(_ theData: CFMutableData!, _ range: CFRange, _ newBytes: UnsafePointer<UInt8>, _ newLength: CFIndex) ``` |
| To | ``` func CFDataReplaceBytes(_ theData: CFMutableData!, _ range: CFRange, _ newBytes: UnsafePointer<UInt8>!, _ newLength: CFIndex) ``` |

Modified [CFDateCompare(_: CFDate!, _: CFDate!, _: UnsafeMutableRawPointer!) -> CFComparisonResult](https://developer.apple.com/documentation/corefoundation/1542671-cfdatecompare)

|  | Declaration |
| --- | --- |
| From | ``` func CFDateCompare(_ theDate: CFDate!, _ otherDate: CFDate!, _ context: UnsafeMutablePointer<Void>) -> CFComparisonResult ``` |
| To | ``` func CFDateCompare(_ theDate: CFDate!, _ otherDate: CFDate!, _ context: UnsafeMutableRawPointer!) -> CFComparisonResult ``` |

Modified [CFDateFormatterCopyProperty(_: CFDateFormatter!, _: CFDateFormatterKey!) -> CFTypeRef!](https://developer.apple.com/documentation/corefoundation/1396296-cfdateformattercopyproperty)

|  | Declaration |
| --- | --- |
| From | ``` func CFDateFormatterCopyProperty(_ formatter: CFDateFormatter!, _ key: CFString!) -> AnyObject! ``` |
| To | ``` func CFDateFormatterCopyProperty(_ formatter: CFDateFormatter!, _ key: CFDateFormatterKey!) -> CFTypeRef! ``` |

Modified [CFDateFormatterCreateDateFromString(_: CFAllocator!, _: CFDateFormatter!, _: CFString!, _: UnsafeMutablePointer<CFRange>!) -> CFDate!](https://developer.apple.com/documentation/corefoundation/1396238-cfdateformattercreatedatefromstr)

|  | Declaration |
| --- | --- |
| From | ``` func CFDateFormatterCreateDateFromString(_ allocator: CFAllocator!, _ formatter: CFDateFormatter!, _ string: CFString!, _ rangep: UnsafeMutablePointer<CFRange>) -> CFDate! ``` |
| To | ``` func CFDateFormatterCreateDateFromString(_ allocator: CFAllocator!, _ formatter: CFDateFormatter!, _ string: CFString!, _ rangep: UnsafeMutablePointer<CFRange>!) -> CFDate! ``` |

Modified [CFDateFormatterGetAbsoluteTimeFromString(_: CFDateFormatter!, _: CFString!, _: UnsafeMutablePointer<CFRange>!, _: UnsafeMutablePointer<CFAbsoluteTime>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1396232-cfdateformattergetabsolutetimefr)

|  | Declaration |
| --- | --- |
| From | ``` func CFDateFormatterGetAbsoluteTimeFromString(_ formatter: CFDateFormatter!, _ string: CFString!, _ rangep: UnsafeMutablePointer<CFRange>, _ atp: UnsafeMutablePointer<CFAbsoluteTime>) -> Bool ``` |
| To | ``` func CFDateFormatterGetAbsoluteTimeFromString(_ formatter: CFDateFormatter!, _ string: CFString!, _ rangep: UnsafeMutablePointer<CFRange>!, _ atp: UnsafeMutablePointer<CFAbsoluteTime>!) -> Bool ``` |

Modified [CFDateFormatterSetProperty(_: CFDateFormatter!, _: CFString!, _: CFTypeRef!)](https://developer.apple.com/documentation/corefoundation/1396265-cfdateformattersetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func CFDateFormatterSetProperty(_ formatter: CFDateFormatter!, _ key: CFString!, _ value: AnyObject!) ``` |
| To | ``` func CFDateFormatterSetProperty(_ formatter: CFDateFormatter!, _ key: CFString!, _ value: CFTypeRef!) ``` |

Modified [CFDictionaryAddValue(_: CFMutableDictionary!, _: UnsafeRawPointer!, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/corefoundation/1516777-cfdictionaryaddvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryAddValue(_ theDict: CFMutableDictionary!, _ key: UnsafePointer<Void>, _ value: UnsafePointer<Void>) ``` |
| To | ``` func CFDictionaryAddValue(_ theDict: CFMutableDictionary!, _ key: UnsafeRawPointer!, _ value: UnsafeRawPointer!) ``` |

Modified [CFDictionaryApplierFunction](https://developer.apple.com/documentation/corefoundation/cfdictionaryapplierfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFDictionaryApplierFunction = (UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CFDictionaryApplierFunction = (UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CFDictionaryApplyFunction(_: CFDictionary!, _: ((UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)!, _: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/corefoundation/1516745-cfdictionaryapplyfunction)

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryApplyFunction(_ theDict: CFDictionary!, _ applier: CFDictionaryApplierFunction!, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func CFDictionaryApplyFunction(_ theDict: CFDictionary!, _ applier: ((UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)!, _ context: UnsafeMutableRawPointer!) ``` |

Modified [CFDictionaryContainsKey(_: CFDictionary!, _: UnsafeRawPointer!) -> Bool](https://developer.apple.com/documentation/corefoundation/1516808-cfdictionarycontainskey)

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryContainsKey(_ theDict: CFDictionary!, _ key: UnsafePointer<Void>) -> Bool ``` |
| To | ``` func CFDictionaryContainsKey(_ theDict: CFDictionary!, _ key: UnsafeRawPointer!) -> Bool ``` |

Modified [CFDictionaryContainsValue(_: CFDictionary!, _: UnsafeRawPointer!) -> Bool](https://developer.apple.com/documentation/corefoundation/1516809-cfdictionarycontainsvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryContainsValue(_ theDict: CFDictionary!, _ value: UnsafePointer<Void>) -> Bool ``` |
| To | ``` func CFDictionaryContainsValue(_ theDict: CFDictionary!, _ value: UnsafeRawPointer!) -> Bool ``` |

Modified [CFDictionaryCopyDescriptionCallBack](https://developer.apple.com/documentation/corefoundation/cfdictionarycopydescriptioncallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFDictionaryCopyDescriptionCallBack = (UnsafePointer<Void>) -> Unmanaged<CFString>! ``` |
| To | ``` typealias CFDictionaryCopyDescriptionCallBack = (UnsafeRawPointer?) -> Unmanaged<CFString>? ``` |

Modified [CFDictionaryCreate(_: CFAllocator!, _: UnsafeMutablePointer<UnsafeRawPointer?>!, _: UnsafeMutablePointer<UnsafeRawPointer?>!, _: CFIndex, _: UnsafePointer<CFDictionaryKeyCallBacks>!, _: UnsafePointer<CFDictionaryValueCallBacks>!) -> CFDictionary!](https://developer.apple.com/documentation/corefoundation/1516782-cfdictionarycreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryCreate(_ allocator: CFAllocator!, _ keys: UnsafeMutablePointer<UnsafePointer<Void>>, _ values: UnsafeMutablePointer<UnsafePointer<Void>>, _ numValues: CFIndex, _ keyCallBacks: UnsafePointer<CFDictionaryKeyCallBacks>, _ valueCallBacks: UnsafePointer<CFDictionaryValueCallBacks>) -> CFDictionary! ``` |
| To | ``` func CFDictionaryCreate(_ allocator: CFAllocator!, _ keys: UnsafeMutablePointer<UnsafeRawPointer?>!, _ values: UnsafeMutablePointer<UnsafeRawPointer?>!, _ numValues: CFIndex, _ keyCallBacks: UnsafePointer<CFDictionaryKeyCallBacks>!, _ valueCallBacks: UnsafePointer<CFDictionaryValueCallBacks>!) -> CFDictionary! ``` |

Modified [CFDictionaryCreateMutable(_: CFAllocator!, _: CFIndex, _: UnsafePointer<CFDictionaryKeyCallBacks>!, _: UnsafePointer<CFDictionaryValueCallBacks>!) -> CFMutableDictionary!](https://developer.apple.com/documentation/corefoundation/1516791-cfdictionarycreatemutable)

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryCreateMutable(_ allocator: CFAllocator!, _ capacity: CFIndex, _ keyCallBacks: UnsafePointer<CFDictionaryKeyCallBacks>, _ valueCallBacks: UnsafePointer<CFDictionaryValueCallBacks>) -> CFMutableDictionary! ``` |
| To | ``` func CFDictionaryCreateMutable(_ allocator: CFAllocator!, _ capacity: CFIndex, _ keyCallBacks: UnsafePointer<CFDictionaryKeyCallBacks>!, _ valueCallBacks: UnsafePointer<CFDictionaryValueCallBacks>!) -> CFMutableDictionary! ``` |

Modified [CFDictionaryEqualCallBack](https://developer.apple.com/documentation/corefoundation/cfdictionaryequalcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFDictionaryEqualCallBack = (UnsafePointer<Void>, UnsafePointer<Void>) -> DarwinBoolean ``` |
| To | ``` typealias CFDictionaryEqualCallBack = (UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean ``` |

Modified [CFDictionaryGetCountOfKey(_: CFDictionary!, _: UnsafeRawPointer!) -> CFIndex](https://developer.apple.com/documentation/corefoundation/1516759-cfdictionarygetcountofkey)

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryGetCountOfKey(_ theDict: CFDictionary!, _ key: UnsafePointer<Void>) -> CFIndex ``` |
| To | ``` func CFDictionaryGetCountOfKey(_ theDict: CFDictionary!, _ key: UnsafeRawPointer!) -> CFIndex ``` |

Modified [CFDictionaryGetCountOfValue(_: CFDictionary!, _: UnsafeRawPointer!) -> CFIndex](https://developer.apple.com/documentation/corefoundation/1516751-cfdictionarygetcountofvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryGetCountOfValue(_ theDict: CFDictionary!, _ value: UnsafePointer<Void>) -> CFIndex ``` |
| To | ``` func CFDictionaryGetCountOfValue(_ theDict: CFDictionary!, _ value: UnsafeRawPointer!) -> CFIndex ``` |

Modified [CFDictionaryGetKeysAndValues(_: CFDictionary!, _: UnsafeMutablePointer<UnsafeRawPointer?>!, _: UnsafeMutablePointer<UnsafeRawPointer?>!)](https://developer.apple.com/documentation/corefoundation/1516790-cfdictionarygetkeysandvalues)

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryGetKeysAndValues(_ theDict: CFDictionary!, _ keys: UnsafeMutablePointer<UnsafePointer<Void>>, _ values: UnsafeMutablePointer<UnsafePointer<Void>>) ``` |
| To | ``` func CFDictionaryGetKeysAndValues(_ theDict: CFDictionary!, _ keys: UnsafeMutablePointer<UnsafeRawPointer?>!, _ values: UnsafeMutablePointer<UnsafeRawPointer?>!) ``` |

Modified [CFDictionaryGetValue(_: CFDictionary!, _: UnsafeRawPointer!) -> UnsafeRawPointer!](https://developer.apple.com/documentation/corefoundation/1516757-cfdictionarygetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryGetValue(_ theDict: CFDictionary!, _ key: UnsafePointer<Void>) -> UnsafePointer<Void> ``` |
| To | ``` func CFDictionaryGetValue(_ theDict: CFDictionary!, _ key: UnsafeRawPointer!) -> UnsafeRawPointer! ``` |

Modified [CFDictionaryGetValueIfPresent(_: CFDictionary!, _: UnsafeRawPointer!, _: UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1516739-cfdictionarygetvalueifpresent)

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryGetValueIfPresent(_ theDict: CFDictionary!, _ key: UnsafePointer<Void>, _ value: UnsafeMutablePointer<UnsafePointer<Void>>) -> Bool ``` |
| To | ``` func CFDictionaryGetValueIfPresent(_ theDict: CFDictionary!, _ key: UnsafeRawPointer!, _ value: UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool ``` |

Modified [CFDictionaryHashCallBack](https://developer.apple.com/documentation/corefoundation/cfdictionaryhashcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFDictionaryHashCallBack = (UnsafePointer<Void>) -> CFHashCode ``` |
| To | ``` typealias CFDictionaryHashCallBack = (UnsafeRawPointer?) -> CFHashCode ``` |

Modified [CFDictionaryReleaseCallBack](https://developer.apple.com/documentation/corefoundation/cfdictionaryreleasecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFDictionaryReleaseCallBack = (CFAllocator!, UnsafePointer<Void>) -> Void ``` |
| To | ``` typealias CFDictionaryReleaseCallBack = (CFAllocator?, UnsafeRawPointer?) -> Swift.Void ``` |

Modified [CFDictionaryRemoveValue(_: CFMutableDictionary!, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/corefoundation/1516771-cfdictionaryremovevalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryRemoveValue(_ theDict: CFMutableDictionary!, _ key: UnsafePointer<Void>) ``` |
| To | ``` func CFDictionaryRemoveValue(_ theDict: CFMutableDictionary!, _ key: UnsafeRawPointer!) ``` |

Modified [CFDictionaryReplaceValue(_: CFMutableDictionary!, _: UnsafeRawPointer!, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/corefoundation/1516743-cfdictionaryreplacevalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionaryReplaceValue(_ theDict: CFMutableDictionary!, _ key: UnsafePointer<Void>, _ value: UnsafePointer<Void>) ``` |
| To | ``` func CFDictionaryReplaceValue(_ theDict: CFMutableDictionary!, _ key: UnsafeRawPointer!, _ value: UnsafeRawPointer!) ``` |

Modified [CFDictionaryRetainCallBack](https://developer.apple.com/documentation/corefoundation/cfdictionaryretaincallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFDictionaryRetainCallBack = (CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void> ``` |
| To | ``` typealias CFDictionaryRetainCallBack = (CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer? ``` |

Modified [CFDictionarySetValue(_: CFMutableDictionary!, _: UnsafeRawPointer!, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/corefoundation/1516787-cfdictionarysetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFDictionarySetValue(_ theDict: CFMutableDictionary!, _ key: UnsafePointer<Void>, _ value: UnsafePointer<Void>) ``` |
| To | ``` func CFDictionarySetValue(_ theDict: CFMutableDictionary!, _ key: UnsafeRawPointer!, _ value: UnsafeRawPointer!) ``` |

Modified [CFEqual(_: CFTypeRef!, _: CFTypeRef!) -> Bool](https://developer.apple.com/documentation/corefoundation/1521287-cfequal)

|  | Declaration |
| --- | --- |
| From | ``` func CFEqual(_ cf1: AnyObject!, _ cf2: AnyObject!) -> Bool ``` |
| To | ``` func CFEqual(_ cf1: CFTypeRef!, _ cf2: CFTypeRef!) -> Bool ``` |

Modified [CFErrorCreate(_: CFAllocator!, _: CFErrorDomain!, _: CFIndex, _: CFDictionary!) -> CFError!](https://developer.apple.com/documentation/corefoundation/1494643-cferrorcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFErrorCreate(_ allocator: CFAllocator!, _ domain: CFString!, _ code: CFIndex, _ userInfo: CFDictionary!) -> CFError! ``` |
| To | ``` func CFErrorCreate(_ allocator: CFAllocator!, _ domain: CFErrorDomain!, _ code: CFIndex, _ userInfo: CFDictionary!) -> CFError! ``` |

Modified [CFErrorCreateWithUserInfoKeysAndValues(_: CFAllocator!, _: CFErrorDomain!, _: CFIndex, _: UnsafePointer<UnsafeRawPointer?>!, _: UnsafePointer<UnsafeRawPointer?>!, _: CFIndex) -> CFError!](https://developer.apple.com/documentation/corefoundation/1494658-cferrorcreatewithuserinfokeysand)

|  | Declaration |
| --- | --- |
| From | ``` func CFErrorCreateWithUserInfoKeysAndValues(_ allocator: CFAllocator!, _ domain: CFString!, _ code: CFIndex, _ userInfoKeys: UnsafePointer<UnsafePointer<Void>>, _ userInfoValues: UnsafePointer<UnsafePointer<Void>>, _ numUserInfoValues: CFIndex) -> CFError! ``` |
| To | ``` func CFErrorCreateWithUserInfoKeysAndValues(_ allocator: CFAllocator!, _ domain: CFErrorDomain!, _ code: CFIndex, _ userInfoKeys: UnsafePointer<UnsafeRawPointer?>!, _ userInfoValues: UnsafePointer<UnsafeRawPointer?>!, _ numUserInfoValues: CFIndex) -> CFError! ``` |

Modified [CFErrorGetDomain(_: CFError!) -> CFErrorDomain!](https://developer.apple.com/documentation/corefoundation/1494657-cferrorgetdomain)

|  | Declaration |
| --- | --- |
| From | ``` func CFErrorGetDomain(_ err: CFError!) -> CFString! ``` |
| To | ``` func CFErrorGetDomain(_ err: CFError!) -> CFErrorDomain! ``` |

Modified [CFFileDescriptorCallBack](https://developer.apple.com/documentation/corefoundation/cffiledescriptorcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFFileDescriptorCallBack = (CFFileDescriptor!, CFOptionFlags, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CFFileDescriptorCallBack = (CFFileDescriptor?, CFOptionFlags, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CFFileDescriptorCreate(_: CFAllocator!, _: CFFileDescriptorNativeDescriptor, _: Bool, _: CoreFoundation.CFFileDescriptorCallBack!, _: UnsafePointer<CFFileDescriptorContext>!) -> CFFileDescriptor!](https://developer.apple.com/documentation/corefoundation/1477591-cffiledescriptorcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFFileDescriptorCreate(_ allocator: CFAllocator!, _ fd: CFFileDescriptorNativeDescriptor, _ closeOnInvalidate: Bool, _ callout: CFFileDescriptorCallBack!, _ context: UnsafePointer<CFFileDescriptorContext>) -> CFFileDescriptor! ``` |
| To | ``` func CFFileDescriptorCreate(_ allocator: CFAllocator!, _ fd: CFFileDescriptorNativeDescriptor, _ closeOnInvalidate: Bool, _ callout: CoreFoundation.CFFileDescriptorCallBack!, _ context: UnsafePointer<CFFileDescriptorContext>!) -> CFFileDescriptor! ``` |

Modified [CFFileDescriptorGetContext(_: CFFileDescriptor!, _: UnsafeMutablePointer<CFFileDescriptorContext>!)](https://developer.apple.com/documentation/corefoundation/1477602-cffiledescriptorgetcontext)

|  | Declaration |
| --- | --- |
| From | ``` func CFFileDescriptorGetContext(_ f: CFFileDescriptor!, _ context: UnsafeMutablePointer<CFFileDescriptorContext>) ``` |
| To | ``` func CFFileDescriptorGetContext(_ f: CFFileDescriptor!, _ context: UnsafeMutablePointer<CFFileDescriptorContext>!) ``` |

Modified [CFFileSecurityCopyAccessControlList(_: CFFileSecurity!, _: UnsafeMutablePointer<acl_t?>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1426508-cffilesecuritycopyaccesscontroll)

|  | Declaration |
| --- | --- |
| From | ``` func CFFileSecurityCopyAccessControlList(_ fileSec: CFFileSecurity!, _ accessControlList: UnsafeMutablePointer<acl_t>) -> Bool ``` |
| To | ``` func CFFileSecurityCopyAccessControlList(_ fileSec: CFFileSecurity!, _ accessControlList: UnsafeMutablePointer<acl_t?>!) -> Bool ``` |

Modified [CFFileSecurityCopyGroupUUID(_: CFFileSecurity!, _: UnsafeMutablePointer<Unmanaged<CFUUID>?>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1426512-cffilesecuritycopygroupuuid)

|  | Declaration |
| --- | --- |
| From | ``` func CFFileSecurityCopyGroupUUID(_ fileSec: CFFileSecurity!, _ groupUUID: UnsafeMutablePointer<Unmanaged<CFUUID>?>) -> Bool ``` |
| To | ``` func CFFileSecurityCopyGroupUUID(_ fileSec: CFFileSecurity!, _ groupUUID: UnsafeMutablePointer<Unmanaged<CFUUID>?>!) -> Bool ``` |

Modified [CFFileSecurityCopyOwnerUUID(_: CFFileSecurity!, _: UnsafeMutablePointer<Unmanaged<CFUUID>?>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1426519-cffilesecuritycopyowneruuid)

|  | Declaration |
| --- | --- |
| From | ``` func CFFileSecurityCopyOwnerUUID(_ fileSec: CFFileSecurity!, _ ownerUUID: UnsafeMutablePointer<Unmanaged<CFUUID>?>) -> Bool ``` |
| To | ``` func CFFileSecurityCopyOwnerUUID(_ fileSec: CFFileSecurity!, _ ownerUUID: UnsafeMutablePointer<Unmanaged<CFUUID>?>!) -> Bool ``` |

Modified [CFFileSecurityGetGroup(_: CFFileSecurity!, _: UnsafeMutablePointer<gid_t>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1426526-cffilesecuritygetgroup)

|  | Declaration |
| --- | --- |
| From | ``` func CFFileSecurityGetGroup(_ fileSec: CFFileSecurity!, _ group: UnsafeMutablePointer<gid_t>) -> Bool ``` |
| To | ``` func CFFileSecurityGetGroup(_ fileSec: CFFileSecurity!, _ group: UnsafeMutablePointer<gid_t>!) -> Bool ``` |

Modified [CFFileSecurityGetMode(_: CFFileSecurity!, _: UnsafeMutablePointer<mode_t>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1426517-cffilesecuritygetmode)

|  | Declaration |
| --- | --- |
| From | ``` func CFFileSecurityGetMode(_ fileSec: CFFileSecurity!, _ mode: UnsafeMutablePointer<mode_t>) -> Bool ``` |
| To | ``` func CFFileSecurityGetMode(_ fileSec: CFFileSecurity!, _ mode: UnsafeMutablePointer<mode_t>!) -> Bool ``` |

Modified [CFFileSecurityGetOwner(_: CFFileSecurity!, _: UnsafeMutablePointer<uid_t>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1426516-cffilesecuritygetowner)

|  | Declaration |
| --- | --- |
| From | ``` func CFFileSecurityGetOwner(_ fileSec: CFFileSecurity!, _ owner: UnsafeMutablePointer<uid_t>) -> Bool ``` |
| To | ``` func CFFileSecurityGetOwner(_ fileSec: CFFileSecurity!, _ owner: UnsafeMutablePointer<uid_t>!) -> Bool ``` |

Modified [CFFileSecuritySetAccessControlList(_: CFFileSecurity!, _: acl_t!) -> Bool](https://developer.apple.com/documentation/corefoundation/1426506-cffilesecuritysetaccesscontrolli)

|  | Declaration |
| --- | --- |
| From | ``` func CFFileSecuritySetAccessControlList(_ fileSec: CFFileSecurity!, _ accessControlList: acl_t) -> Bool ``` |
| To | ``` func CFFileSecuritySetAccessControlList(_ fileSec: CFFileSecurity!, _ accessControlList: acl_t!) -> Bool ``` |

Modified [CFGetAllocator(_: CFTypeRef!) -> CFAllocator!](https://developer.apple.com/documentation/corefoundation/1521280-cfgetallocator)

|  | Declaration |
| --- | --- |
| From | ``` func CFGetAllocator(_ cf: AnyObject!) -> CFAllocator! ``` |
| To | ``` func CFGetAllocator(_ cf: CFTypeRef!) -> CFAllocator! ``` |

Modified [CFGetRetainCount(_: CFTypeRef!) -> CFIndex](https://developer.apple.com/documentation/corefoundation/1521288-cfgetretaincount)

|  | Declaration |
| --- | --- |
| From | ``` func CFGetRetainCount(_ cf: AnyObject!) -> CFIndex ``` |
| To | ``` func CFGetRetainCount(_ cf: CFTypeRef!) -> CFIndex ``` |

Modified [CFGetTypeID(_: CFTypeRef!) -> CFTypeID](https://developer.apple.com/documentation/corefoundation/1521218-cfgettypeid)

|  | Declaration |
| --- | --- |
| From | ``` func CFGetTypeID(_ cf: AnyObject!) -> CFTypeID ``` |
| To | ``` func CFGetTypeID(_ cf: CFTypeRef!) -> CFTypeID ``` |

Modified [CFHash(_: CFTypeRef!) -> CFHashCode](https://developer.apple.com/documentation/corefoundation/1521137-cfhash)

|  | Declaration |
| --- | --- |
| From | ``` func CFHash(_ cf: AnyObject!) -> CFHashCode ``` |
| To | ``` func CFHash(_ cf: CFTypeRef!) -> CFHashCode ``` |

Modified [CFLocaleCopyDisplayNameForPropertyValue(_: CFLocale!, _: CFLocaleKey!, _: CFString!) -> CFString!](https://developer.apple.com/documentation/corefoundation/1542344-cflocalecopydisplaynameforproper)

|  | Declaration |
| --- | --- |
| From | ``` func CFLocaleCopyDisplayNameForPropertyValue(_ displayLocale: CFLocale!, _ key: CFString!, _ value: CFString!) -> CFString! ``` |
| To | ``` func CFLocaleCopyDisplayNameForPropertyValue(_ displayLocale: CFLocale!, _ key: CFLocaleKey!, _ value: CFString!) -> CFString! ``` |

Modified [CFLocaleCreate(_: CFAllocator!, _: CFLocaleIdentifier!) -> CFLocale!](https://developer.apple.com/documentation/corefoundation/1542689-cflocalecreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFLocaleCreate(_ allocator: CFAllocator!, _ localeIdentifier: CFString!) -> CFLocale! ``` |
| To | ``` func CFLocaleCreate(_ allocator: CFAllocator!, _ localeIdentifier: CFLocaleIdentifier!) -> CFLocale! ``` |

Modified [CFLocaleCreateCanonicalLanguageIdentifierFromString(_: CFAllocator!, _: CFString!) -> CFLocaleIdentifier!](https://developer.apple.com/documentation/corefoundation/1542757-cflocalecreatecanonicallanguagei)

|  | Declaration |
| --- | --- |
| From | ``` func CFLocaleCreateCanonicalLanguageIdentifierFromString(_ allocator: CFAllocator!, _ localeIdentifier: CFString!) -> CFString! ``` |
| To | ``` func CFLocaleCreateCanonicalLanguageIdentifierFromString(_ allocator: CFAllocator!, _ localeIdentifier: CFString!) -> CFLocaleIdentifier! ``` |

Modified [CFLocaleCreateCanonicalLocaleIdentifierFromScriptManagerCodes(_: CFAllocator!, _: LangCode, _: RegionCode) -> CFLocaleIdentifier!](https://developer.apple.com/documentation/corefoundation/1543446-cflocalecreatecanonicallocaleide)

|  | Declaration |
| --- | --- |
| From | ``` func CFLocaleCreateCanonicalLocaleIdentifierFromScriptManagerCodes(_ allocator: CFAllocator!, _ lcode: LangCode, _ rcode: RegionCode) -> CFString! ``` |
| To | ``` func CFLocaleCreateCanonicalLocaleIdentifierFromScriptManagerCodes(_ allocator: CFAllocator!, _ lcode: LangCode, _ rcode: RegionCode) -> CFLocaleIdentifier! ``` |

Modified [CFLocaleCreateCanonicalLocaleIdentifierFromString(_: CFAllocator!, _: CFString!) -> CFLocaleIdentifier!](https://developer.apple.com/documentation/corefoundation/1542725-cflocalecreatecanonicallocaleide)

|  | Declaration |
| --- | --- |
| From | ``` func CFLocaleCreateCanonicalLocaleIdentifierFromString(_ allocator: CFAllocator!, _ localeIdentifier: CFString!) -> CFString! ``` |
| To | ``` func CFLocaleCreateCanonicalLocaleIdentifierFromString(_ allocator: CFAllocator!, _ localeIdentifier: CFString!) -> CFLocaleIdentifier! ``` |

Modified [CFLocaleCreateComponentsFromLocaleIdentifier(_: CFAllocator!, _: CFLocaleIdentifier!) -> CFDictionary!](https://developer.apple.com/documentation/corefoundation/1543644-cflocalecreatecomponentsfromloca)

|  | Declaration |
| --- | --- |
| From | ``` func CFLocaleCreateComponentsFromLocaleIdentifier(_ allocator: CFAllocator!, _ localeID: CFString!) -> CFDictionary! ``` |
| To | ``` func CFLocaleCreateComponentsFromLocaleIdentifier(_ allocator: CFAllocator!, _ localeID: CFLocaleIdentifier!) -> CFDictionary! ``` |

Modified [CFLocaleCreateLocaleIdentifierFromComponents(_: CFAllocator!, _: CFDictionary!) -> CFLocaleIdentifier!](https://developer.apple.com/documentation/corefoundation/1541724-cflocalecreatelocaleidentifierfr)

|  | Declaration |
| --- | --- |
| From | ``` func CFLocaleCreateLocaleIdentifierFromComponents(_ allocator: CFAllocator!, _ dictionary: CFDictionary!) -> CFString! ``` |
| To | ``` func CFLocaleCreateLocaleIdentifierFromComponents(_ allocator: CFAllocator!, _ dictionary: CFDictionary!) -> CFLocaleIdentifier! ``` |

Modified [CFLocaleCreateLocaleIdentifierFromWindowsLocaleCode(_: CFAllocator!, _: UInt32) -> CFLocaleIdentifier!](https://developer.apple.com/documentation/corefoundation/1541772-cflocalecreatelocaleidentifierfr)

|  | Declaration |
| --- | --- |
| From | ``` func CFLocaleCreateLocaleIdentifierFromWindowsLocaleCode(_ allocator: CFAllocator!, _ lcid: UInt32) -> CFString! ``` |
| To | ``` func CFLocaleCreateLocaleIdentifierFromWindowsLocaleCode(_ allocator: CFAllocator!, _ lcid: UInt32) -> CFLocaleIdentifier! ``` |

Modified [CFLocaleGetIdentifier(_: CFLocale!) -> CFLocaleIdentifier!](https://developer.apple.com/documentation/corefoundation/1543634-cflocalegetidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func CFLocaleGetIdentifier(_ locale: CFLocale!) -> CFString! ``` |
| To | ``` func CFLocaleGetIdentifier(_ locale: CFLocale!) -> CFLocaleIdentifier! ``` |

Modified [CFLocaleGetValue(_: CFLocale!, _: CFLocaleKey!) -> CFTypeRef!](https://developer.apple.com/documentation/corefoundation/1543547-cflocalegetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFLocaleGetValue(_ locale: CFLocale!, _ key: CFString!) -> AnyObject! ``` |
| To | ``` func CFLocaleGetValue(_ locale: CFLocale!, _ key: CFLocaleKey!) -> CFTypeRef! ``` |

Modified [CFLocaleGetWindowsLocaleCodeFromLocaleIdentifier(_: CFLocaleIdentifier!) -> UInt32](https://developer.apple.com/documentation/corefoundation/1542147-cflocalegetwindowslocalecodefrom)

|  | Declaration |
| --- | --- |
| From | ``` func CFLocaleGetWindowsLocaleCodeFromLocaleIdentifier(_ localeIdentifier: CFString!) -> UInt32 ``` |
| To | ``` func CFLocaleGetWindowsLocaleCodeFromLocaleIdentifier(_ localeIdentifier: CFLocaleIdentifier!) -> UInt32 ``` |

Modified [CFMachPortCallBack](https://developer.apple.com/documentation/corefoundation/cfmachportcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFMachPortCallBack = (CFMachPort!, UnsafeMutablePointer<Void>, CFIndex, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CFMachPortCallBack = (CFMachPort?, UnsafeMutableRawPointer?, CFIndex, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CFMachPortCreate(_: CFAllocator!, _: CoreFoundation.CFMachPortCallBack!, _: UnsafeMutablePointer<CFMachPortContext>!, _: UnsafeMutablePointer<DarwinBoolean>!) -> CFMachPort!](https://developer.apple.com/documentation/corefoundation/1400934-cfmachportcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFMachPortCreate(_ allocator: CFAllocator!, _ callout: CFMachPortCallBack!, _ context: UnsafeMutablePointer<CFMachPortContext>, _ shouldFreeInfo: UnsafeMutablePointer<DarwinBoolean>) -> CFMachPort! ``` |
| To | ``` func CFMachPortCreate(_ allocator: CFAllocator!, _ callout: CoreFoundation.CFMachPortCallBack!, _ context: UnsafeMutablePointer<CFMachPortContext>!, _ shouldFreeInfo: UnsafeMutablePointer<DarwinBoolean>!) -> CFMachPort! ``` |

Modified [CFMachPortCreateWithPort(_: CFAllocator!, _: mach_port_t, _: CoreFoundation.CFMachPortCallBack!, _: UnsafeMutablePointer<CFMachPortContext>!, _: UnsafeMutablePointer<DarwinBoolean>!) -> CFMachPort!](https://developer.apple.com/documentation/corefoundation/1400924-cfmachportcreatewithport)

|  | Declaration |
| --- | --- |
| From | ``` func CFMachPortCreateWithPort(_ allocator: CFAllocator!, _ portNum: mach_port_t, _ callout: CFMachPortCallBack!, _ context: UnsafeMutablePointer<CFMachPortContext>, _ shouldFreeInfo: UnsafeMutablePointer<DarwinBoolean>) -> CFMachPort! ``` |
| To | ``` func CFMachPortCreateWithPort(_ allocator: CFAllocator!, _ portNum: mach_port_t, _ callout: CoreFoundation.CFMachPortCallBack!, _ context: UnsafeMutablePointer<CFMachPortContext>!, _ shouldFreeInfo: UnsafeMutablePointer<DarwinBoolean>!) -> CFMachPort! ``` |

Modified [CFMachPortGetContext(_: CFMachPort!, _: UnsafeMutablePointer<CFMachPortContext>!)](https://developer.apple.com/documentation/corefoundation/1400932-cfmachportgetcontext)

|  | Declaration |
| --- | --- |
| From | ``` func CFMachPortGetContext(_ port: CFMachPort!, _ context: UnsafeMutablePointer<CFMachPortContext>) ``` |
| To | ``` func CFMachPortGetContext(_ port: CFMachPort!, _ context: UnsafeMutablePointer<CFMachPortContext>!) ``` |

Modified [CFMachPortGetInvalidationCallBack(_: CFMachPort!) -> CoreFoundation.CFMachPortInvalidationCallBack!](https://developer.apple.com/documentation/corefoundation/1400946-cfmachportgetinvalidationcallbac)

|  | Declaration |
| --- | --- |
| From | ``` func CFMachPortGetInvalidationCallBack(_ port: CFMachPort!) -> CFMachPortInvalidationCallBack! ``` |
| To | ``` func CFMachPortGetInvalidationCallBack(_ port: CFMachPort!) -> CoreFoundation.CFMachPortInvalidationCallBack! ``` |

Modified [CFMachPortInvalidationCallBack](https://developer.apple.com/documentation/corefoundation/cfmachportinvalidationcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFMachPortInvalidationCallBack = (CFMachPort!, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CFMachPortInvalidationCallBack = (CFMachPort?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CFMachPortSetInvalidationCallBack(_: CFMachPort!, _: CoreFoundation.CFMachPortInvalidationCallBack!)](https://developer.apple.com/documentation/corefoundation/1400942-cfmachportsetinvalidationcallbac)

|  | Declaration |
| --- | --- |
| From | ``` func CFMachPortSetInvalidationCallBack(_ port: CFMachPort!, _ callout: CFMachPortInvalidationCallBack!) ``` |
| To | ``` func CFMachPortSetInvalidationCallBack(_ port: CFMachPort!, _ callout: CoreFoundation.CFMachPortInvalidationCallBack!) ``` |

Modified [CFMessagePortCallBack](https://developer.apple.com/documentation/corefoundation/cfmessageportcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFMessagePortCallBack = (CFMessagePort!, Int32, CFData!, UnsafeMutablePointer<Void>) -> Unmanaged<CFData>! ``` |
| To | ``` typealias CFMessagePortCallBack = (CFMessagePort?, Int32, CFData?, UnsafeMutableRawPointer?) -> Unmanaged<CFData>? ``` |

Modified [CFMessagePortCreateLocal(_: CFAllocator!, _: CFString!, _: CoreFoundation.CFMessagePortCallBack!, _: UnsafeMutablePointer<CFMessagePortContext>!, _: UnsafeMutablePointer<DarwinBoolean>!) -> CFMessagePort!](https://developer.apple.com/documentation/corefoundation/1543289-cfmessageportcreatelocal)

|  | Declaration |
| --- | --- |
| From | ``` func CFMessagePortCreateLocal(_ allocator: CFAllocator!, _ name: CFString!, _ callout: CFMessagePortCallBack!, _ context: UnsafeMutablePointer<CFMessagePortContext>, _ shouldFreeInfo: UnsafeMutablePointer<DarwinBoolean>) -> CFMessagePort! ``` |
| To | ``` func CFMessagePortCreateLocal(_ allocator: CFAllocator!, _ name: CFString!, _ callout: CoreFoundation.CFMessagePortCallBack!, _ context: UnsafeMutablePointer<CFMessagePortContext>!, _ shouldFreeInfo: UnsafeMutablePointer<DarwinBoolean>!) -> CFMessagePort! ``` |

Modified [CFMessagePortGetContext(_: CFMessagePort!, _: UnsafeMutablePointer<CFMessagePortContext>!)](https://developer.apple.com/documentation/corefoundation/1542662-cfmessageportgetcontext)

|  | Declaration |
| --- | --- |
| From | ``` func CFMessagePortGetContext(_ ms: CFMessagePort!, _ context: UnsafeMutablePointer<CFMessagePortContext>) ``` |
| To | ``` func CFMessagePortGetContext(_ ms: CFMessagePort!, _ context: UnsafeMutablePointer<CFMessagePortContext>!) ``` |

Modified [CFMessagePortGetInvalidationCallBack(_: CFMessagePort!) -> CoreFoundation.CFMessagePortInvalidationCallBack!](https://developer.apple.com/documentation/corefoundation/1542568-cfmessageportgetinvalidationcall)

|  | Declaration |
| --- | --- |
| From | ``` func CFMessagePortGetInvalidationCallBack(_ ms: CFMessagePort!) -> CFMessagePortInvalidationCallBack! ``` |
| To | ``` func CFMessagePortGetInvalidationCallBack(_ ms: CFMessagePort!) -> CoreFoundation.CFMessagePortInvalidationCallBack! ``` |

Modified [CFMessagePortInvalidationCallBack](https://developer.apple.com/documentation/corefoundation/cfmessageportinvalidationcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFMessagePortInvalidationCallBack = (CFMessagePort!, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CFMessagePortInvalidationCallBack = (CFMessagePort?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CFMessagePortSendRequest(_: CFMessagePort!, _: Int32, _: CFData!, _: CFTimeInterval, _: CFTimeInterval, _: CFString!, _: UnsafeMutablePointer<Unmanaged<CFData>?>!) -> Int32](https://developer.apple.com/documentation/corefoundation/1543076-cfmessageportsendrequest)

|  | Declaration |
| --- | --- |
| From | ``` func CFMessagePortSendRequest(_ remote: CFMessagePort!, _ msgid: Int32, _ data: CFData!, _ sendTimeout: CFTimeInterval, _ rcvTimeout: CFTimeInterval, _ replyMode: CFString!, _ returnData: UnsafeMutablePointer<Unmanaged<CFData>?>) -> Int32 ``` |
| To | ``` func CFMessagePortSendRequest(_ remote: CFMessagePort!, _ msgid: Int32, _ data: CFData!, _ sendTimeout: CFTimeInterval, _ rcvTimeout: CFTimeInterval, _ replyMode: CFString!, _ returnData: UnsafeMutablePointer<Unmanaged<CFData>?>!) -> Int32 ``` |

Modified [CFMessagePortSetDispatchQueue(_: CFMessagePort!, _: DispatchQueue!)](https://developer.apple.com/documentation/corefoundation/1542637-cfmessageportsetdispatchqueue)

|  | Declaration |
| --- | --- |
| From | ``` func CFMessagePortSetDispatchQueue(_ ms: CFMessagePort!, _ queue: dispatch_queue_t!) ``` |
| To | ``` func CFMessagePortSetDispatchQueue(_ ms: CFMessagePort!, _ queue: DispatchQueue!) ``` |

Modified [CFMessagePortSetInvalidationCallBack(_: CFMessagePort!, _: CoreFoundation.CFMessagePortInvalidationCallBack!)](https://developer.apple.com/documentation/corefoundation/1541999-cfmessageportsetinvalidationcall)

|  | Declaration |
| --- | --- |
| From | ``` func CFMessagePortSetInvalidationCallBack(_ ms: CFMessagePort!, _ callout: CFMessagePortInvalidationCallBack!) ``` |
| To | ``` func CFMessagePortSetInvalidationCallBack(_ ms: CFMessagePort!, _ callout: CoreFoundation.CFMessagePortInvalidationCallBack!) ``` |

Modified [CFNotificationCallback](https://developer.apple.com/documentation/corefoundation/cfnotificationcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFNotificationCallback = (CFNotificationCenter!, UnsafeMutablePointer<Void>, CFString!, UnsafePointer<Void>, CFDictionary!) -> Void ``` |
| To | ``` typealias CFNotificationCallback = (CFNotificationCenter?, UnsafeMutableRawPointer?, CFNotificationName?, UnsafeRawPointer?, CFDictionary?) -> Swift.Void ``` |

Modified [CFNotificationCenterAddObserver(_: CFNotificationCenter!, _: UnsafeRawPointer!, _: CoreFoundation.CFNotificationCallback!, _: CFString!, _: UnsafeRawPointer!, _: CFNotificationSuspensionBehavior)](https://developer.apple.com/documentation/corefoundation/1543316-cfnotificationcenteraddobserver)

|  | Declaration |
| --- | --- |
| From | ``` func CFNotificationCenterAddObserver(_ center: CFNotificationCenter!, _ observer: UnsafePointer<Void>, _ callBack: CFNotificationCallback!, _ name: CFString!, _ object: UnsafePointer<Void>, _ suspensionBehavior: CFNotificationSuspensionBehavior) ``` |
| To | ``` func CFNotificationCenterAddObserver(_ center: CFNotificationCenter!, _ observer: UnsafeRawPointer!, _ callBack: CoreFoundation.CFNotificationCallback!, _ name: CFString!, _ object: UnsafeRawPointer!, _ suspensionBehavior: CFNotificationSuspensionBehavior) ``` |

Modified [CFNotificationCenterPostNotification(_: CFNotificationCenter!, _: CFNotificationName!, _: UnsafeRawPointer!, _: CFDictionary!, _: Bool)](https://developer.apple.com/documentation/corefoundation/1542592-cfnotificationcenterpostnotifica)

|  | Declaration |
| --- | --- |
| From | ``` func CFNotificationCenterPostNotification(_ center: CFNotificationCenter!, _ name: CFString!, _ object: UnsafePointer<Void>, _ userInfo: CFDictionary!, _ deliverImmediately: Bool) ``` |
| To | ``` func CFNotificationCenterPostNotification(_ center: CFNotificationCenter!, _ name: CFNotificationName!, _ object: UnsafeRawPointer!, _ userInfo: CFDictionary!, _ deliverImmediately: Bool) ``` |

Modified [CFNotificationCenterPostNotificationWithOptions(_: CFNotificationCenter!, _: CFNotificationName!, _: UnsafeRawPointer!, _: CFDictionary!, _: CFOptionFlags)](https://developer.apple.com/documentation/corefoundation/1541969-cfnotificationcenterpostnotifica)

|  | Declaration |
| --- | --- |
| From | ``` func CFNotificationCenterPostNotificationWithOptions(_ center: CFNotificationCenter!, _ name: CFString!, _ object: UnsafePointer<Void>, _ userInfo: CFDictionary!, _ options: CFOptionFlags) ``` |
| To | ``` func CFNotificationCenterPostNotificationWithOptions(_ center: CFNotificationCenter!, _ name: CFNotificationName!, _ object: UnsafeRawPointer!, _ userInfo: CFDictionary!, _ options: CFOptionFlags) ``` |

Modified [CFNotificationCenterRemoveEveryObserver(_: CFNotificationCenter!, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/corefoundation/1543518-cfnotificationcenterremoveeveryo)

|  | Declaration |
| --- | --- |
| From | ``` func CFNotificationCenterRemoveEveryObserver(_ center: CFNotificationCenter!, _ observer: UnsafePointer<Void>) ``` |
| To | ``` func CFNotificationCenterRemoveEveryObserver(_ center: CFNotificationCenter!, _ observer: UnsafeRawPointer!) ``` |

Modified [CFNotificationCenterRemoveObserver(_: CFNotificationCenter!, _: UnsafeRawPointer!, _: CFNotificationName!, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/corefoundation/1542672-cfnotificationcenterremoveobserv)

|  | Declaration |
| --- | --- |
| From | ``` func CFNotificationCenterRemoveObserver(_ center: CFNotificationCenter!, _ observer: UnsafePointer<Void>, _ name: CFString!, _ object: UnsafePointer<Void>) ``` |
| To | ``` func CFNotificationCenterRemoveObserver(_ center: CFNotificationCenter!, _ observer: UnsafeRawPointer!, _ name: CFNotificationName!, _ object: UnsafeRawPointer!) ``` |

Modified [CFNumberCompare(_: CFNumber!, _: CFNumber!, _: UnsafeMutableRawPointer!) -> CFComparisonResult](https://developer.apple.com/documentation/corefoundation/1542018-cfnumbercompare)

|  | Declaration |
| --- | --- |
| From | ``` func CFNumberCompare(_ number: CFNumber!, _ otherNumber: CFNumber!, _ context: UnsafeMutablePointer<Void>) -> CFComparisonResult ``` |
| To | ``` func CFNumberCompare(_ number: CFNumber!, _ otherNumber: CFNumber!, _ context: UnsafeMutableRawPointer!) -> CFComparisonResult ``` |

Modified [CFNumberCreate(_: CFAllocator!, _: CFNumberType, _: UnsafeRawPointer!) -> CFNumber!](https://developer.apple.com/documentation/corefoundation/1542182-cfnumbercreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFNumberCreate(_ allocator: CFAllocator!, _ theType: CFNumberType, _ valuePtr: UnsafePointer<Void>) -> CFNumber! ``` |
| To | ``` func CFNumberCreate(_ allocator: CFAllocator!, _ theType: CFNumberType, _ valuePtr: UnsafeRawPointer!) -> CFNumber! ``` |

Modified [CFNumberFormatterCopyProperty(_: CFNumberFormatter!, _: CFNumberFormatterKey!) -> CFTypeRef!](https://developer.apple.com/documentation/corefoundation/1390801-cfnumberformattercopyproperty)

|  | Declaration |
| --- | --- |
| From | ``` func CFNumberFormatterCopyProperty(_ formatter: CFNumberFormatter!, _ key: CFString!) -> AnyObject! ``` |
| To | ``` func CFNumberFormatterCopyProperty(_ formatter: CFNumberFormatter!, _ key: CFNumberFormatterKey!) -> CFTypeRef! ``` |

Modified [CFNumberFormatterCreateNumberFromString(_: CFAllocator!, _: CFNumberFormatter!, _: CFString!, _: UnsafeMutablePointer<CFRange>!, _: CFOptionFlags) -> CFNumber!](https://developer.apple.com/documentation/corefoundation/1390807-cfnumberformattercreatenumberfro)

|  | Declaration |
| --- | --- |
| From | ``` func CFNumberFormatterCreateNumberFromString(_ allocator: CFAllocator!, _ formatter: CFNumberFormatter!, _ string: CFString!, _ rangep: UnsafeMutablePointer<CFRange>, _ options: CFOptionFlags) -> CFNumber! ``` |
| To | ``` func CFNumberFormatterCreateNumberFromString(_ allocator: CFAllocator!, _ formatter: CFNumberFormatter!, _ string: CFString!, _ rangep: UnsafeMutablePointer<CFRange>!, _ options: CFOptionFlags) -> CFNumber! ``` |

Modified [CFNumberFormatterCreateStringWithValue(_: CFAllocator!, _: CFNumberFormatter!, _: CFNumberType, _: UnsafeRawPointer!) -> CFString!](https://developer.apple.com/documentation/corefoundation/1390755-cfnumberformattercreatestringwit)

|  | Declaration |
| --- | --- |
| From | ``` func CFNumberFormatterCreateStringWithValue(_ allocator: CFAllocator!, _ formatter: CFNumberFormatter!, _ numberType: CFNumberType, _ valuePtr: UnsafePointer<Void>) -> CFString! ``` |
| To | ``` func CFNumberFormatterCreateStringWithValue(_ allocator: CFAllocator!, _ formatter: CFNumberFormatter!, _ numberType: CFNumberType, _ valuePtr: UnsafeRawPointer!) -> CFString! ``` |

Modified [CFNumberFormatterGetDecimalInfoForCurrencyCode(_: CFString!, _: UnsafeMutablePointer<Int32>!, _: UnsafeMutablePointer<Double>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1390757-cfnumberformattergetdecimalinfof)

|  | Declaration |
| --- | --- |
| From | ``` func CFNumberFormatterGetDecimalInfoForCurrencyCode(_ currencyCode: CFString!, _ defaultFractionDigits: UnsafeMutablePointer<Int32>, _ roundingIncrement: UnsafeMutablePointer<Double>) -> Bool ``` |
| To | ``` func CFNumberFormatterGetDecimalInfoForCurrencyCode(_ currencyCode: CFString!, _ defaultFractionDigits: UnsafeMutablePointer<Int32>!, _ roundingIncrement: UnsafeMutablePointer<Double>!) -> Bool ``` |

Modified [CFNumberFormatterGetValueFromString(_: CFNumberFormatter!, _: CFString!, _: UnsafeMutablePointer<CFRange>!, _: CFNumberType, _: UnsafeMutableRawPointer!) -> Bool](https://developer.apple.com/documentation/corefoundation/1390720-cfnumberformattergetvaluefromstr)

|  | Declaration |
| --- | --- |
| From | ``` func CFNumberFormatterGetValueFromString(_ formatter: CFNumberFormatter!, _ string: CFString!, _ rangep: UnsafeMutablePointer<CFRange>, _ numberType: CFNumberType, _ valuePtr: UnsafeMutablePointer<Void>) -> Bool ``` |
| To | ``` func CFNumberFormatterGetValueFromString(_ formatter: CFNumberFormatter!, _ string: CFString!, _ rangep: UnsafeMutablePointer<CFRange>!, _ numberType: CFNumberType, _ valuePtr: UnsafeMutableRawPointer!) -> Bool ``` |

Modified [CFNumberFormatterSetProperty(_: CFNumberFormatter!, _: CFNumberFormatterKey!, _: CFTypeRef!)](https://developer.apple.com/documentation/corefoundation/1390800-cfnumberformattersetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func CFNumberFormatterSetProperty(_ formatter: CFNumberFormatter!, _ key: CFString!, _ value: AnyObject!) ``` |
| To | ``` func CFNumberFormatterSetProperty(_ formatter: CFNumberFormatter!, _ key: CFNumberFormatterKey!, _ value: CFTypeRef!) ``` |

Modified [CFNumberGetValue(_: CFNumber!, _: CFNumberType, _: UnsafeMutableRawPointer!) -> Bool](https://developer.apple.com/documentation/corefoundation/1543114-cfnumbergetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFNumberGetValue(_ number: CFNumber!, _ theType: CFNumberType, _ valuePtr: UnsafeMutablePointer<Void>) -> Bool ``` |
| To | ``` func CFNumberGetValue(_ number: CFNumber!, _ theType: CFNumberType, _ valuePtr: UnsafeMutableRawPointer!) -> Bool ``` |

Modified [CFPlugInDynamicRegisterFunction](https://developer.apple.com/documentation/corefoundation/cfplugindynamicregisterfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFPlugInDynamicRegisterFunction = (CFPlugIn!) -> Void ``` |
| To | ``` typealias CFPlugInDynamicRegisterFunction = (CFPlugIn?) -> Swift.Void ``` |

Modified [CFPlugInFactoryFunction](https://developer.apple.com/documentation/corefoundation/cfpluginfactoryfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFPlugInFactoryFunction = (CFAllocator!, CFUUID!) -> UnsafeMutablePointer<Void> ``` |
| To | ``` typealias CFPlugInFactoryFunction = (CFAllocator?, CFUUID?) -> UnsafeMutableRawPointer? ``` |

Modified [CFPlugInInstanceCreate(_: CFAllocator!, _: CFUUID!, _: CFUUID!) -> UnsafeMutableRawPointer!](https://developer.apple.com/documentation/corefoundation/1493857-cfplugininstancecreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFPlugInInstanceCreate(_ allocator: CFAllocator!, _ factoryUUID: CFUUID!, _ typeUUID: CFUUID!) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func CFPlugInInstanceCreate(_ allocator: CFAllocator!, _ factoryUUID: CFUUID!, _ typeUUID: CFUUID!) -> UnsafeMutableRawPointer! ``` |

Modified [CFPlugInInstanceCreateWithInstanceDataSize(_: CFAllocator!, _: CFIndex, _: CoreFoundation.CFPlugInInstanceDeallocateInstanceDataFunction!, _: CFString!, _: CoreFoundation.CFPlugInInstanceGetInterfaceFunction!) -> CFPlugInInstance!](https://developer.apple.com/documentation/corefoundation/1493882-cfplugininstancecreatewithinstan)

|  | Declaration |
| --- | --- |
| From | ``` func CFPlugInInstanceCreateWithInstanceDataSize(_ allocator: CFAllocator!, _ instanceDataSize: CFIndex, _ deallocateInstanceFunction: CFPlugInInstanceDeallocateInstanceDataFunction!, _ factoryName: CFString!, _ getInterfaceFunction: CFPlugInInstanceGetInterfaceFunction!) -> CFPlugInInstance! ``` |
| To | ``` func CFPlugInInstanceCreateWithInstanceDataSize(_ allocator: CFAllocator!, _ instanceDataSize: CFIndex, _ deallocateInstanceFunction: CoreFoundation.CFPlugInInstanceDeallocateInstanceDataFunction!, _ factoryName: CFString!, _ getInterfaceFunction: CoreFoundation.CFPlugInInstanceGetInterfaceFunction!) -> CFPlugInInstance! ``` |

Modified [CFPlugInInstanceDeallocateInstanceDataFunction](https://developer.apple.com/documentation/corefoundation/cfplugininstancedeallocateinstancedatafunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFPlugInInstanceDeallocateInstanceDataFunction = (UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CFPlugInInstanceDeallocateInstanceDataFunction = (UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CFPlugInInstanceGetInstanceData(_: CFPlugInInstance!) -> UnsafeMutableRawPointer!](https://developer.apple.com/documentation/corefoundation/1493848-cfplugininstancegetinstancedata)

|  | Declaration |
| --- | --- |
| From | ``` func CFPlugInInstanceGetInstanceData(_ instance: CFPlugInInstance!) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func CFPlugInInstanceGetInstanceData(_ instance: CFPlugInInstance!) -> UnsafeMutableRawPointer! ``` |

Modified [CFPlugInInstanceGetInterfaceFunction](https://developer.apple.com/documentation/corefoundation/cfplugininstancegetinterfacefunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFPlugInInstanceGetInterfaceFunction = (CFPlugInInstance!, CFString!, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> DarwinBoolean ``` |
| To | ``` typealias CFPlugInInstanceGetInterfaceFunction = (CFPlugInInstance?, CFString?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> DarwinBoolean ``` |

Modified [CFPlugInInstanceGetInterfaceFunctionTable(_: CFPlugInInstance!, _: CFString!, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1493862-cfplugininstancegetinterfacefunc)

|  | Declaration |
| --- | --- |
| From | ``` func CFPlugInInstanceGetInterfaceFunctionTable(_ instance: CFPlugInInstance!, _ interfaceName: CFString!, _ ftbl: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Bool ``` |
| To | ``` func CFPlugInInstanceGetInterfaceFunctionTable(_ instance: CFPlugInInstance!, _ interfaceName: CFString!, _ ftbl: UnsafeMutablePointer<UnsafeMutableRawPointer?>!) -> Bool ``` |

Modified [CFPlugInRegisterFactoryFunction(_: CFUUID!, _: CoreFoundation.CFPlugInFactoryFunction!) -> Bool](https://developer.apple.com/documentation/corefoundation/1493868-cfpluginregisterfactoryfunction)

|  | Declaration |
| --- | --- |
| From | ``` func CFPlugInRegisterFactoryFunction(_ factoryUUID: CFUUID!, _ func: CFPlugInFactoryFunction!) -> Bool ``` |
| To | ``` func CFPlugInRegisterFactoryFunction(_ factoryUUID: CFUUID!, _ func: CoreFoundation.CFPlugInFactoryFunction!) -> Bool ``` |

Modified [CFPlugInUnloadFunction](https://developer.apple.com/documentation/corefoundation/cfpluginunloadfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFPlugInUnloadFunction = (CFPlugIn!) -> Void ``` |
| To | ``` typealias CFPlugInUnloadFunction = (CFPlugIn?) -> Swift.Void ``` |

Modified [CFPreferencesAddSuitePreferencesToApp(_: CFString, _: CFString)](https://developer.apple.com/documentation/corefoundation/1515518-cfpreferencesaddsuitepreferences)

|  | Declaration |
| --- | --- |
| From | ``` func CFPreferencesAddSuitePreferencesToApp(_ applicationID: CFString!, _ suiteID: CFString!) ``` |
| To | ``` func CFPreferencesAddSuitePreferencesToApp(_ applicationID: CFString, _ suiteID: CFString) ``` |

Modified [CFPreferencesAppSynchronize(_: CFString) -> Bool](https://developer.apple.com/documentation/corefoundation/1515510-cfpreferencesappsynchronize)

|  | Declaration |
| --- | --- |
| From | ``` func CFPreferencesAppSynchronize(_ applicationID: CFString!) -> Bool ``` |
| To | ``` func CFPreferencesAppSynchronize(_ applicationID: CFString) -> Bool ``` |

Modified [CFPreferencesAppValueIsForced(_: CFString, _: CFString) -> Bool](https://developer.apple.com/documentation/corefoundation/1515521-cfpreferencesappvalueisforced)

|  | Declaration |
| --- | --- |
| From | ``` func CFPreferencesAppValueIsForced(_ key: CFString!, _ applicationID: CFString!) -> Bool ``` |
| To | ``` func CFPreferencesAppValueIsForced(_ key: CFString, _ applicationID: CFString) -> Bool ``` |

Modified [CFPreferencesCopyAppValue(_: CFString, _: CFString) -> CFPropertyList?](https://developer.apple.com/documentation/corefoundation/1515497-cfpreferencescopyappvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFPreferencesCopyAppValue(_ key: CFString!, _ applicationID: CFString!) -> CFPropertyList! ``` |
| To | ``` func CFPreferencesCopyAppValue(_ key: CFString, _ applicationID: CFString) -> CFPropertyList? ``` |

Modified [CFPreferencesCopyKeyList(_: CFString, _: CFString, _: CFString) -> CFArray?](https://developer.apple.com/documentation/corefoundation/1515512-cfpreferencescopykeylist)

|  | Declaration |
| --- | --- |
| From | ``` func CFPreferencesCopyKeyList(_ applicationID: CFString!, _ userName: CFString!, _ hostName: CFString!) -> CFArray! ``` |
| To | ``` func CFPreferencesCopyKeyList(_ applicationID: CFString, _ userName: CFString, _ hostName: CFString) -> CFArray? ``` |

Modified [CFPreferencesCopyMultiple(_: CFArray?, _: CFString, _: CFString, _: CFString) -> CFDictionary](https://developer.apple.com/documentation/corefoundation/1515498-cfpreferencescopymultiple)

|  | Declaration |
| --- | --- |
| From | ``` func CFPreferencesCopyMultiple(_ keysToFetch: CFArray!, _ applicationID: CFString!, _ userName: CFString!, _ hostName: CFString!) -> CFDictionary! ``` |
| To | ``` func CFPreferencesCopyMultiple(_ keysToFetch: CFArray?, _ applicationID: CFString, _ userName: CFString, _ hostName: CFString) -> CFDictionary ``` |

Modified [CFPreferencesCopyValue(_: CFString, _: CFString, _: CFString, _: CFString) -> CFPropertyList?](https://developer.apple.com/documentation/corefoundation/1515500-cfpreferencescopyvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFPreferencesCopyValue(_ key: CFString!, _ applicationID: CFString!, _ userName: CFString!, _ hostName: CFString!) -> CFPropertyList! ``` |
| To | ``` func CFPreferencesCopyValue(_ key: CFString, _ applicationID: CFString, _ userName: CFString, _ hostName: CFString) -> CFPropertyList? ``` |

Modified [CFPreferencesGetAppBooleanValue(_: CFString, _: CFString, _: UnsafeMutablePointer<DarwinBoolean>?) -> Bool](https://developer.apple.com/documentation/corefoundation/1515514-cfpreferencesgetappbooleanvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFPreferencesGetAppBooleanValue(_ key: CFString!, _ applicationID: CFString!, _ keyExistsAndHasValidFormat: UnsafeMutablePointer<DarwinBoolean>) -> Bool ``` |
| To | ``` func CFPreferencesGetAppBooleanValue(_ key: CFString, _ applicationID: CFString, _ keyExistsAndHasValidFormat: UnsafeMutablePointer<DarwinBoolean>?) -> Bool ``` |

Modified [CFPreferencesGetAppIntegerValue(_: CFString, _: CFString, _: UnsafeMutablePointer<DarwinBoolean>?) -> CFIndex](https://developer.apple.com/documentation/corefoundation/1515526-cfpreferencesgetappintegervalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFPreferencesGetAppIntegerValue(_ key: CFString!, _ applicationID: CFString!, _ keyExistsAndHasValidFormat: UnsafeMutablePointer<DarwinBoolean>) -> CFIndex ``` |
| To | ``` func CFPreferencesGetAppIntegerValue(_ key: CFString, _ applicationID: CFString, _ keyExistsAndHasValidFormat: UnsafeMutablePointer<DarwinBoolean>?) -> CFIndex ``` |

Modified [CFPreferencesRemoveSuitePreferencesFromApp(_: CFString, _: CFString)](https://developer.apple.com/documentation/corefoundation/1515501-cfpreferencesremovesuitepreferen)

|  | Declaration |
| --- | --- |
| From | ``` func CFPreferencesRemoveSuitePreferencesFromApp(_ applicationID: CFString!, _ suiteID: CFString!) ``` |
| To | ``` func CFPreferencesRemoveSuitePreferencesFromApp(_ applicationID: CFString, _ suiteID: CFString) ``` |

Modified [CFPreferencesSetAppValue(_: CFString, _: CFPropertyList?, _: CFString)](https://developer.apple.com/documentation/corefoundation/1515528-cfpreferencessetappvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFPreferencesSetAppValue(_ key: CFString!, _ value: CFPropertyList!, _ applicationID: CFString!) ``` |
| To | ``` func CFPreferencesSetAppValue(_ key: CFString, _ value: CFPropertyList?, _ applicationID: CFString) ``` |

Modified [CFPreferencesSetMultiple(_: CFDictionary?, _: CFArray?, _: CFString, _: CFString, _: CFString)](https://developer.apple.com/documentation/corefoundation/1515513-cfpreferencessetmultiple)

|  | Declaration |
| --- | --- |
| From | ``` func CFPreferencesSetMultiple(_ keysToSet: CFDictionary!, _ keysToRemove: CFArray!, _ applicationID: CFString!, _ userName: CFString!, _ hostName: CFString!) ``` |
| To | ``` func CFPreferencesSetMultiple(_ keysToSet: CFDictionary?, _ keysToRemove: CFArray?, _ applicationID: CFString, _ userName: CFString, _ hostName: CFString) ``` |

Modified [CFPreferencesSetValue(_: CFString, _: CFPropertyList?, _: CFString, _: CFString, _: CFString)](https://developer.apple.com/documentation/corefoundation/1515525-cfpreferencessetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFPreferencesSetValue(_ key: CFString!, _ value: CFPropertyList!, _ applicationID: CFString!, _ userName: CFString!, _ hostName: CFString!) ``` |
| To | ``` func CFPreferencesSetValue(_ key: CFString, _ value: CFPropertyList?, _ applicationID: CFString, _ userName: CFString, _ hostName: CFString) ``` |

Modified [CFPreferencesSynchronize(_: CFString, _: CFString, _: CFString) -> Bool](https://developer.apple.com/documentation/corefoundation/1515504-cfpreferencessynchronize)

|  | Declaration |
| --- | --- |
| From | ``` func CFPreferencesSynchronize(_ applicationID: CFString!, _ userName: CFString!, _ hostName: CFString!) -> Bool ``` |
| To | ``` func CFPreferencesSynchronize(_ applicationID: CFString, _ userName: CFString, _ hostName: CFString) -> Bool ``` |

Modified [CFPropertyList](https://developer.apple.com/documentation/corefoundation/cfpropertylist)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFPropertyListRef = CFPropertyList ``` |
| To | ``` typealias CFPropertyList = CFTypeRef ``` |

Modified [CFPropertyListCreateData(_: CFAllocator!, _: CFPropertyList!, _: CFPropertyListFormat, _: CFOptionFlags, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFData>!](https://developer.apple.com/documentation/corefoundation/1429998-cfpropertylistcreatedata)

|  | Declaration |
| --- | --- |
| From | ``` func CFPropertyListCreateData(_ allocator: CFAllocator!, _ propertyList: CFPropertyList!, _ format: CFPropertyListFormat, _ options: CFOptionFlags, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>! ``` |
| To | ``` func CFPropertyListCreateData(_ allocator: CFAllocator!, _ propertyList: CFPropertyList!, _ format: CFPropertyListFormat, _ options: CFOptionFlags, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFData>! ``` |

Modified [CFPropertyListCreateFromStream(_: CFAllocator!, _: CFReadStream!, _: CFIndex, _: CFOptionFlags, _: UnsafeMutablePointer<CFPropertyListFormat>!, _: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Unmanaged<CFPropertyList>!](https://developer.apple.com/documentation/corefoundation/1429993-cfpropertylistcreatefromstream)

|  | Declaration |
| --- | --- |
| From | ``` func CFPropertyListCreateFromStream(_ allocator: CFAllocator!, _ stream: CFReadStream!, _ streamLength: CFIndex, _ mutabilityOption: CFOptionFlags, _ format: UnsafeMutablePointer<CFPropertyListFormat>, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>) -> Unmanaged<CFPropertyList>! ``` |
| To | ``` func CFPropertyListCreateFromStream(_ allocator: CFAllocator!, _ stream: CFReadStream!, _ streamLength: CFIndex, _ mutabilityOption: CFOptionFlags, _ format: UnsafeMutablePointer<CFPropertyListFormat>!, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Unmanaged<CFPropertyList>! ``` |

Modified [CFPropertyListCreateFromXMLData(_: CFAllocator!, _: CFData!, _: CFOptionFlags, _: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Unmanaged<CFPropertyList>!](https://developer.apple.com/documentation/corefoundation/1429995-cfpropertylistcreatefromxmldata)

|  | Declaration |
| --- | --- |
| From | ``` func CFPropertyListCreateFromXMLData(_ allocator: CFAllocator!, _ xmlData: CFData!, _ mutabilityOption: CFOptionFlags, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>) -> Unmanaged<CFPropertyList>! ``` |
| To | ``` func CFPropertyListCreateFromXMLData(_ allocator: CFAllocator!, _ xmlData: CFData!, _ mutabilityOption: CFOptionFlags, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Unmanaged<CFPropertyList>! ``` |

Modified [CFPropertyListCreateWithData(_: CFAllocator!, _: CFData!, _: CFOptionFlags, _: UnsafeMutablePointer<CFPropertyListFormat>!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFPropertyList>!](https://developer.apple.com/documentation/corefoundation/1430002-cfpropertylistcreatewithdata)

|  | Declaration |
| --- | --- |
| From | ``` func CFPropertyListCreateWithData(_ allocator: CFAllocator!, _ data: CFData!, _ options: CFOptionFlags, _ format: UnsafeMutablePointer<CFPropertyListFormat>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFPropertyList>! ``` |
| To | ``` func CFPropertyListCreateWithData(_ allocator: CFAllocator!, _ data: CFData!, _ options: CFOptionFlags, _ format: UnsafeMutablePointer<CFPropertyListFormat>!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFPropertyList>! ``` |

Modified [CFPropertyListCreateWithStream(_: CFAllocator!, _: CFReadStream!, _: CFIndex, _: CFOptionFlags, _: UnsafeMutablePointer<CFPropertyListFormat>!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFPropertyList>!](https://developer.apple.com/documentation/corefoundation/1430023-cfpropertylistcreatewithstream)

|  | Declaration |
| --- | --- |
| From | ``` func CFPropertyListCreateWithStream(_ allocator: CFAllocator!, _ stream: CFReadStream!, _ streamLength: CFIndex, _ options: CFOptionFlags, _ format: UnsafeMutablePointer<CFPropertyListFormat>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFPropertyList>! ``` |
| To | ``` func CFPropertyListCreateWithStream(_ allocator: CFAllocator!, _ stream: CFReadStream!, _ streamLength: CFIndex, _ options: CFOptionFlags, _ format: UnsafeMutablePointer<CFPropertyListFormat>!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFPropertyList>! ``` |

Modified [CFPropertyListWrite(_: CFPropertyList!, _: CFWriteStream!, _: CFPropertyListFormat, _: CFOptionFlags, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFIndex](https://developer.apple.com/documentation/corefoundation/1430001-cfpropertylistwrite)

|  | Declaration |
| --- | --- |
| From | ``` func CFPropertyListWrite(_ propertyList: CFPropertyList!, _ stream: CFWriteStream!, _ format: CFPropertyListFormat, _ options: CFOptionFlags, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFIndex ``` |
| To | ``` func CFPropertyListWrite(_ propertyList: CFPropertyList!, _ stream: CFWriteStream!, _ format: CFPropertyListFormat, _ options: CFOptionFlags, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFIndex ``` |

Modified [CFPropertyListWriteToStream(_: CFPropertyList!, _: CFWriteStream!, _: CFPropertyListFormat, _: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> CFIndex](https://developer.apple.com/documentation/corefoundation/1430031-cfpropertylistwritetostream)

|  | Declaration |
| --- | --- |
| From | ``` func CFPropertyListWriteToStream(_ propertyList: CFPropertyList!, _ stream: CFWriteStream!, _ format: CFPropertyListFormat, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>) -> CFIndex ``` |
| To | ``` func CFPropertyListWriteToStream(_ propertyList: CFPropertyList!, _ stream: CFWriteStream!, _ format: CFPropertyListFormat, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> CFIndex ``` |

Modified [CFReadStreamClientCallBack](https://developer.apple.com/documentation/corefoundation/cfreadstreamclientcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFReadStreamClientCallBack = (CFReadStream!, CFStreamEventType, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CFReadStreamClientCallBack = (CFReadStream?, CFStreamEventType, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CFReadStreamCopyDispatchQueue(_: CFReadStream!) -> DispatchQueue!](https://developer.apple.com/documentation/corefoundation/1539632-cfreadstreamcopydispatchqueue)

|  | Declaration |
| --- | --- |
| From | ``` func CFReadStreamCopyDispatchQueue(_ stream: CFReadStream!) -> dispatch_queue_t! ``` |
| To | ``` func CFReadStreamCopyDispatchQueue(_ stream: CFReadStream!) -> DispatchQueue! ``` |

Modified [CFReadStreamCopyProperty(_: CFReadStream!, _: CFStreamPropertyKey!) -> CFTypeRef!](https://developer.apple.com/documentation/corefoundation/1539715-cfreadstreamcopyproperty)

|  | Declaration |
| --- | --- |
| From | ``` func CFReadStreamCopyProperty(_ stream: CFReadStream!, _ propertyName: CFString!) -> AnyObject! ``` |
| To | ``` func CFReadStreamCopyProperty(_ stream: CFReadStream!, _ propertyName: CFStreamPropertyKey!) -> CFTypeRef! ``` |

Modified [CFReadStreamCreateWithBytesNoCopy(_: CFAllocator!, _: UnsafePointer<UInt8>!, _: CFIndex, _: CFAllocator!) -> CFReadStream!](https://developer.apple.com/documentation/corefoundation/1539646-cfreadstreamcreatewithbytesnocop)

|  | Declaration |
| --- | --- |
| From | ``` func CFReadStreamCreateWithBytesNoCopy(_ alloc: CFAllocator!, _ bytes: UnsafePointer<UInt8>, _ length: CFIndex, _ bytesDeallocator: CFAllocator!) -> CFReadStream! ``` |
| To | ``` func CFReadStreamCreateWithBytesNoCopy(_ alloc: CFAllocator!, _ bytes: UnsafePointer<UInt8>!, _ length: CFIndex, _ bytesDeallocator: CFAllocator!) -> CFReadStream! ``` |

Modified [CFReadStreamGetBuffer(_: CFReadStream!, _: CFIndex, _: UnsafeMutablePointer<CFIndex>!) -> UnsafePointer<UInt8>!](https://developer.apple.com/documentation/corefoundation/1539692-cfreadstreamgetbuffer)

|  | Declaration |
| --- | --- |
| From | ``` func CFReadStreamGetBuffer(_ stream: CFReadStream!, _ maxBytesToRead: CFIndex, _ numBytesRead: UnsafeMutablePointer<CFIndex>) -> UnsafePointer<UInt8> ``` |
| To | ``` func CFReadStreamGetBuffer(_ stream: CFReadStream!, _ maxBytesToRead: CFIndex, _ numBytesRead: UnsafeMutablePointer<CFIndex>!) -> UnsafePointer<UInt8>! ``` |

Modified [CFReadStreamRead(_: CFReadStream!, _: UnsafeMutablePointer<UInt8>!, _: CFIndex) -> CFIndex](https://developer.apple.com/documentation/corefoundation/1539700-cfreadstreamread)

|  | Declaration |
| --- | --- |
| From | ``` func CFReadStreamRead(_ stream: CFReadStream!, _ buffer: UnsafeMutablePointer<UInt8>, _ bufferLength: CFIndex) -> CFIndex ``` |
| To | ``` func CFReadStreamRead(_ stream: CFReadStream!, _ buffer: UnsafeMutablePointer<UInt8>!, _ bufferLength: CFIndex) -> CFIndex ``` |

Modified [CFReadStreamScheduleWithRunLoop(_: CFReadStream!, _: CFRunLoop!, _: CFRunLoopMode!)](https://developer.apple.com/documentation/corefoundation/1539611-cfreadstreamschedulewithrunloop)

|  | Declaration |
| --- | --- |
| From | ``` func CFReadStreamScheduleWithRunLoop(_ stream: CFReadStream!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) ``` |
| To | ``` func CFReadStreamScheduleWithRunLoop(_ stream: CFReadStream!, _ runLoop: CFRunLoop!, _ runLoopMode: CFRunLoopMode!) ``` |

Modified [CFReadStreamSetClient(_: CFReadStream!, _: CFOptionFlags, _: CoreFoundation.CFReadStreamClientCallBack!, _: UnsafeMutablePointer<CFStreamClientContext>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1539670-cfreadstreamsetclient)

|  | Declaration |
| --- | --- |
| From | ``` func CFReadStreamSetClient(_ stream: CFReadStream!, _ streamEvents: CFOptionFlags, _ clientCB: CFReadStreamClientCallBack!, _ clientContext: UnsafeMutablePointer<CFStreamClientContext>) -> Bool ``` |
| To | ``` func CFReadStreamSetClient(_ stream: CFReadStream!, _ streamEvents: CFOptionFlags, _ clientCB: CoreFoundation.CFReadStreamClientCallBack!, _ clientContext: UnsafeMutablePointer<CFStreamClientContext>!) -> Bool ``` |

Modified [CFReadStreamSetDispatchQueue(_: CFReadStream!, _: DispatchQueue!)](https://developer.apple.com/documentation/corefoundation/1539688-cfreadstreamsetdispatchqueue)

|  | Declaration |
| --- | --- |
| From | ``` func CFReadStreamSetDispatchQueue(_ stream: CFReadStream!, _ q: dispatch_queue_t!) ``` |
| To | ``` func CFReadStreamSetDispatchQueue(_ stream: CFReadStream!, _ q: DispatchQueue!) ``` |

Modified [CFReadStreamSetProperty(_: CFReadStream!, _: CFStreamPropertyKey!, _: CFTypeRef!) -> Bool](https://developer.apple.com/documentation/corefoundation/1539615-cfreadstreamsetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func CFReadStreamSetProperty(_ stream: CFReadStream!, _ propertyName: CFString!, _ propertyValue: AnyObject!) -> Bool ``` |
| To | ``` func CFReadStreamSetProperty(_ stream: CFReadStream!, _ propertyName: CFStreamPropertyKey!, _ propertyValue: CFTypeRef!) -> Bool ``` |

Modified [CFReadStreamUnscheduleFromRunLoop(_: CFReadStream!, _: CFRunLoop!, _: CFRunLoopMode!)](https://developer.apple.com/documentation/corefoundation/1539674-cfreadstreamunschedulefromrunloo)

|  | Declaration |
| --- | --- |
| From | ``` func CFReadStreamUnscheduleFromRunLoop(_ stream: CFReadStream!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) ``` |
| To | ``` func CFReadStreamUnscheduleFromRunLoop(_ stream: CFReadStream!, _ runLoop: CFRunLoop!, _ runLoopMode: CFRunLoopMode!) ``` |

Modified [CFRunLoopAddCommonMode(_: CFRunLoop!, _: CFRunLoopMode!)](https://developer.apple.com/documentation/corefoundation/1542137-cfrunloopaddcommonmode)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopAddCommonMode(_ rl: CFRunLoop!, _ mode: CFString!) ``` |
| To | ``` func CFRunLoopAddCommonMode(_ rl: CFRunLoop!, _ mode: CFRunLoopMode!) ``` |

Modified [CFRunLoopAddObserver(_: CFRunLoop!, _: CFRunLoopObserver!, _: CFRunLoopMode!)](https://developer.apple.com/documentation/corefoundation/1542504-cfrunloopaddobserver)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopAddObserver(_ rl: CFRunLoop!, _ observer: CFRunLoopObserver!, _ mode: CFString!) ``` |
| To | ``` func CFRunLoopAddObserver(_ rl: CFRunLoop!, _ observer: CFRunLoopObserver!, _ mode: CFRunLoopMode!) ``` |

Modified [CFRunLoopAddSource(_: CFRunLoop!, _: CFRunLoopSource!, _: CFRunLoopMode!)](https://developer.apple.com/documentation/corefoundation/1543356-cfrunloopaddsource)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopAddSource(_ rl: CFRunLoop!, _ source: CFRunLoopSource!, _ mode: CFString!) ``` |
| To | ``` func CFRunLoopAddSource(_ rl: CFRunLoop!, _ source: CFRunLoopSource!, _ mode: CFRunLoopMode!) ``` |

Modified [CFRunLoopAddTimer(_: CFRunLoop!, _: CFRunLoopTimer!, _: CFRunLoopMode!)](https://developer.apple.com/documentation/corefoundation/1542132-cfrunloopaddtimer)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopAddTimer(_ rl: CFRunLoop!, _ timer: CFRunLoopTimer!, _ mode: CFString!) ``` |
| To | ``` func CFRunLoopAddTimer(_ rl: CFRunLoop!, _ timer: CFRunLoopTimer!, _ mode: CFRunLoopMode!) ``` |

Modified [CFRunLoopContainsObserver(_: CFRunLoop!, _: CFRunLoopObserver!, _: CFRunLoopMode!) -> Bool](https://developer.apple.com/documentation/corefoundation/1542815-cfrunloopcontainsobserver)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopContainsObserver(_ rl: CFRunLoop!, _ observer: CFRunLoopObserver!, _ mode: CFString!) -> Bool ``` |
| To | ``` func CFRunLoopContainsObserver(_ rl: CFRunLoop!, _ observer: CFRunLoopObserver!, _ mode: CFRunLoopMode!) -> Bool ``` |

Modified [CFRunLoopContainsSource(_: CFRunLoop!, _: CFRunLoopSource!, _: CFRunLoopMode!) -> Bool](https://developer.apple.com/documentation/corefoundation/1542250-cfrunloopcontainssource)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopContainsSource(_ rl: CFRunLoop!, _ source: CFRunLoopSource!, _ mode: CFString!) -> Bool ``` |
| To | ``` func CFRunLoopContainsSource(_ rl: CFRunLoop!, _ source: CFRunLoopSource!, _ mode: CFRunLoopMode!) -> Bool ``` |

Modified [CFRunLoopContainsTimer(_: CFRunLoop!, _: CFRunLoopTimer!, _: CFRunLoopMode!) -> Bool](https://developer.apple.com/documentation/corefoundation/1543011-cfrunloopcontainstimer)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopContainsTimer(_ rl: CFRunLoop!, _ timer: CFRunLoopTimer!, _ mode: CFString!) -> Bool ``` |
| To | ``` func CFRunLoopContainsTimer(_ rl: CFRunLoop!, _ timer: CFRunLoopTimer!, _ mode: CFRunLoopMode!) -> Bool ``` |

Modified [CFRunLoopCopyCurrentMode(_: CFRunLoop!) -> CFRunLoopMode!](https://developer.apple.com/documentation/corefoundation/1541775-cfrunloopcopycurrentmode)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopCopyCurrentMode(_ rl: CFRunLoop!) -> CFString! ``` |
| To | ``` func CFRunLoopCopyCurrentMode(_ rl: CFRunLoop!) -> CFRunLoopMode! ``` |

Modified [CFRunLoopGetNextTimerFireDate(_: CFRunLoop!, _: CFRunLoopMode!) -> CFAbsoluteTime](https://developer.apple.com/documentation/corefoundation/1542092-cfrunloopgetnexttimerfiredate)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopGetNextTimerFireDate(_ rl: CFRunLoop!, _ mode: CFString!) -> CFAbsoluteTime ``` |
| To | ``` func CFRunLoopGetNextTimerFireDate(_ rl: CFRunLoop!, _ mode: CFRunLoopMode!) -> CFAbsoluteTime ``` |

Modified [CFRunLoopObserverCallBack](https://developer.apple.com/documentation/corefoundation/cfrunloopobservercallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFRunLoopObserverCallBack = (CFRunLoopObserver!, CFRunLoopActivity, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CFRunLoopObserverCallBack = (CFRunLoopObserver?, CFRunLoopActivity, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CFRunLoopObserverCreate(_: CFAllocator!, _: CFOptionFlags, _: Bool, _: CFIndex, _: CoreFoundation.CFRunLoopObserverCallBack!, _: UnsafeMutablePointer<CFRunLoopObserverContext>!) -> CFRunLoopObserver!](https://developer.apple.com/documentation/corefoundation/1541546-cfrunloopobservercreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopObserverCreate(_ allocator: CFAllocator!, _ activities: CFOptionFlags, _ repeats: Bool, _ order: CFIndex, _ callout: CFRunLoopObserverCallBack!, _ context: UnsafeMutablePointer<CFRunLoopObserverContext>) -> CFRunLoopObserver! ``` |
| To | ``` func CFRunLoopObserverCreate(_ allocator: CFAllocator!, _ activities: CFOptionFlags, _ repeats: Bool, _ order: CFIndex, _ callout: CoreFoundation.CFRunLoopObserverCallBack!, _ context: UnsafeMutablePointer<CFRunLoopObserverContext>!) -> CFRunLoopObserver! ``` |

Modified [CFRunLoopObserverCreateWithHandler(_: CFAllocator!, _: CFOptionFlags, _: Bool, _: CFIndex, _: ( (CFRunLoopObserver?, CFRunLoopActivity) -> Swift.Void)!) -> CFRunLoopObserver!](https://developer.apple.com/documentation/corefoundation/1542816-cfrunloopobservercreatewithhandl)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopObserverCreateWithHandler(_ allocator: CFAllocator!, _ activities: CFOptionFlags, _ repeats: Bool, _ order: CFIndex, _ block: ((CFRunLoopObserver!, CFRunLoopActivity) -> Void)!) -> CFRunLoopObserver! ``` |
| To | ``` func CFRunLoopObserverCreateWithHandler(_ allocator: CFAllocator!, _ activities: CFOptionFlags, _ repeats: Bool, _ order: CFIndex, _ block: (@escaping (CFRunLoopObserver?, CFRunLoopActivity) -> Swift.Void)!) -> CFRunLoopObserver! ``` |

Modified [CFRunLoopObserverGetContext(_: CFRunLoopObserver!, _: UnsafeMutablePointer<CFRunLoopObserverContext>!)](https://developer.apple.com/documentation/corefoundation/1543497-cfrunloopobservergetcontext)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopObserverGetContext(_ observer: CFRunLoopObserver!, _ context: UnsafeMutablePointer<CFRunLoopObserverContext>) ``` |
| To | ``` func CFRunLoopObserverGetContext(_ observer: CFRunLoopObserver!, _ context: UnsafeMutablePointer<CFRunLoopObserverContext>!) ``` |

Modified [CFRunLoopPerformBlock(_: CFRunLoop!, _: CFTypeRef!, _: ( () -> Swift.Void)!)](https://developer.apple.com/documentation/corefoundation/1542985-cfrunloopperformblock)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopPerformBlock(_ rl: CFRunLoop!, _ mode: AnyObject!, _ block: (() -> Void)!) ``` |
| To | ``` func CFRunLoopPerformBlock(_ rl: CFRunLoop!, _ mode: CFTypeRef!, _ block: (@escaping () -> Swift.Void)!) ``` |

Modified [CFRunLoopRemoveObserver(_: CFRunLoop!, _: CFRunLoopObserver!, _: CFRunLoopMode!)](https://developer.apple.com/documentation/corefoundation/1542818-cfrunloopremoveobserver)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopRemoveObserver(_ rl: CFRunLoop!, _ observer: CFRunLoopObserver!, _ mode: CFString!) ``` |
| To | ``` func CFRunLoopRemoveObserver(_ rl: CFRunLoop!, _ observer: CFRunLoopObserver!, _ mode: CFRunLoopMode!) ``` |

Modified [CFRunLoopRemoveSource(_: CFRunLoop!, _: CFRunLoopSource!, _: CFRunLoopMode!)](https://developer.apple.com/documentation/corefoundation/1542145-cfrunloopremovesource)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopRemoveSource(_ rl: CFRunLoop!, _ source: CFRunLoopSource!, _ mode: CFString!) ``` |
| To | ``` func CFRunLoopRemoveSource(_ rl: CFRunLoop!, _ source: CFRunLoopSource!, _ mode: CFRunLoopMode!) ``` |

Modified [CFRunLoopRemoveTimer(_: CFRunLoop!, _: CFRunLoopTimer!, _: CFRunLoopMode!)](https://developer.apple.com/documentation/corefoundation/1541992-cfrunloopremovetimer)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopRemoveTimer(_ rl: CFRunLoop!, _ timer: CFRunLoopTimer!, _ mode: CFString!) ``` |
| To | ``` func CFRunLoopRemoveTimer(_ rl: CFRunLoop!, _ timer: CFRunLoopTimer!, _ mode: CFRunLoopMode!) ``` |

Modified [CFRunLoopRunInMode(_: CFRunLoopMode!, _: CFTimeInterval, _: Bool) -> CFRunLoopRunResult](https://developer.apple.com/documentation/corefoundation/1541988-cfrunloopruninmode)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopRunInMode(_ mode: CFString!, _ seconds: CFTimeInterval, _ returnAfterSourceHandled: Bool) -> CFRunLoopRunResult ``` |
| To | ``` func CFRunLoopRunInMode(_ mode: CFRunLoopMode!, _ seconds: CFTimeInterval, _ returnAfterSourceHandled: Bool) -> CFRunLoopRunResult ``` |

Modified [CFRunLoopSourceCreate(_: CFAllocator!, _: CFIndex, _: UnsafeMutablePointer<CFRunLoopSourceContext>!) -> CFRunLoopSource!](https://developer.apple.com/documentation/corefoundation/1542679-cfrunloopsourcecreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopSourceCreate(_ allocator: CFAllocator!, _ order: CFIndex, _ context: UnsafeMutablePointer<CFRunLoopSourceContext>) -> CFRunLoopSource! ``` |
| To | ``` func CFRunLoopSourceCreate(_ allocator: CFAllocator!, _ order: CFIndex, _ context: UnsafeMutablePointer<CFRunLoopSourceContext>!) -> CFRunLoopSource! ``` |

Modified [CFRunLoopSourceGetContext(_: CFRunLoopSource!, _: UnsafeMutablePointer<CFRunLoopSourceContext>!)](https://developer.apple.com/documentation/corefoundation/1541961-cfrunloopsourcegetcontext)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopSourceGetContext(_ source: CFRunLoopSource!, _ context: UnsafeMutablePointer<CFRunLoopSourceContext>) ``` |
| To | ``` func CFRunLoopSourceGetContext(_ source: CFRunLoopSource!, _ context: UnsafeMutablePointer<CFRunLoopSourceContext>!) ``` |

Modified [CFRunLoopTimerCallBack](https://developer.apple.com/documentation/corefoundation/cfrunlooptimercallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFRunLoopTimerCallBack = (CFRunLoopTimer!, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CFRunLoopTimerCallBack = (CFRunLoopTimer?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CFRunLoopTimerCreate(_: CFAllocator!, _: CFAbsoluteTime, _: CFTimeInterval, _: CFOptionFlags, _: CFIndex, _: CoreFoundation.CFRunLoopTimerCallBack!, _: UnsafeMutablePointer<CFRunLoopTimerContext>!) -> CFRunLoopTimer!](https://developer.apple.com/documentation/corefoundation/1543570-cfrunlooptimercreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopTimerCreate(_ allocator: CFAllocator!, _ fireDate: CFAbsoluteTime, _ interval: CFTimeInterval, _ flags: CFOptionFlags, _ order: CFIndex, _ callout: CFRunLoopTimerCallBack!, _ context: UnsafeMutablePointer<CFRunLoopTimerContext>) -> CFRunLoopTimer! ``` |
| To | ``` func CFRunLoopTimerCreate(_ allocator: CFAllocator!, _ fireDate: CFAbsoluteTime, _ interval: CFTimeInterval, _ flags: CFOptionFlags, _ order: CFIndex, _ callout: CoreFoundation.CFRunLoopTimerCallBack!, _ context: UnsafeMutablePointer<CFRunLoopTimerContext>!) -> CFRunLoopTimer! ``` |

Modified [CFRunLoopTimerCreateWithHandler(_: CFAllocator!, _: CFAbsoluteTime, _: CFTimeInterval, _: CFOptionFlags, _: CFIndex, _: ( (CFRunLoopTimer?) -> Swift.Void)!) -> CFRunLoopTimer!](https://developer.apple.com/documentation/corefoundation/1542555-cfrunlooptimercreatewithhandler)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopTimerCreateWithHandler(_ allocator: CFAllocator!, _ fireDate: CFAbsoluteTime, _ interval: CFTimeInterval, _ flags: CFOptionFlags, _ order: CFIndex, _ block: ((CFRunLoopTimer!) -> Void)!) -> CFRunLoopTimer! ``` |
| To | ``` func CFRunLoopTimerCreateWithHandler(_ allocator: CFAllocator!, _ fireDate: CFAbsoluteTime, _ interval: CFTimeInterval, _ flags: CFOptionFlags, _ order: CFIndex, _ block: (@escaping (CFRunLoopTimer?) -> Swift.Void)!) -> CFRunLoopTimer! ``` |

Modified [CFRunLoopTimerGetContext(_: CFRunLoopTimer!, _: UnsafeMutablePointer<CFRunLoopTimerContext>!)](https://developer.apple.com/documentation/corefoundation/1541439-cfrunlooptimergetcontext)

|  | Declaration |
| --- | --- |
| From | ``` func CFRunLoopTimerGetContext(_ timer: CFRunLoopTimer!, _ context: UnsafeMutablePointer<CFRunLoopTimerContext>) ``` |
| To | ``` func CFRunLoopTimerGetContext(_ timer: CFRunLoopTimer!, _ context: UnsafeMutablePointer<CFRunLoopTimerContext>!) ``` |

Modified [CFSetAddValue(_: CFMutableSet!, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/corefoundation/1520438-cfsetaddvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFSetAddValue(_ theSet: CFMutableSet!, _ value: UnsafePointer<Void>) ``` |
| To | ``` func CFSetAddValue(_ theSet: CFMutableSet!, _ value: UnsafeRawPointer!) ``` |

Modified [CFSetApplierFunction](https://developer.apple.com/documentation/corefoundation/cfsetapplierfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFSetApplierFunction = (UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CFSetApplierFunction = (UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CFSetApplyFunction(_: CFSet!, _: ((UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)!, _: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/corefoundation/1520450-cfsetapplyfunction)

|  | Declaration |
| --- | --- |
| From | ``` func CFSetApplyFunction(_ theSet: CFSet!, _ applier: CFSetApplierFunction!, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func CFSetApplyFunction(_ theSet: CFSet!, _ applier: ((UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)!, _ context: UnsafeMutableRawPointer!) ``` |

Modified [CFSetContainsValue(_: CFSet!, _: UnsafeRawPointer!) -> Bool](https://developer.apple.com/documentation/corefoundation/1520436-cfsetcontainsvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFSetContainsValue(_ theSet: CFSet!, _ value: UnsafePointer<Void>) -> Bool ``` |
| To | ``` func CFSetContainsValue(_ theSet: CFSet!, _ value: UnsafeRawPointer!) -> Bool ``` |

Modified [CFSetCopyDescriptionCallBack](https://developer.apple.com/documentation/corefoundation/cfsetcopydescriptioncallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFSetCopyDescriptionCallBack = (UnsafePointer<Void>) -> Unmanaged<CFString>! ``` |
| To | ``` typealias CFSetCopyDescriptionCallBack = (UnsafeRawPointer?) -> Unmanaged<CFString>? ``` |

Modified [CFSetCreate(_: CFAllocator!, _: UnsafeMutablePointer<UnsafeRawPointer?>!, _: CFIndex, _: UnsafePointer<CFSetCallBacks>!) -> CFSet!](https://developer.apple.com/documentation/corefoundation/1520424-cfsetcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFSetCreate(_ allocator: CFAllocator!, _ values: UnsafeMutablePointer<UnsafePointer<Void>>, _ numValues: CFIndex, _ callBacks: UnsafePointer<CFSetCallBacks>) -> CFSet! ``` |
| To | ``` func CFSetCreate(_ allocator: CFAllocator!, _ values: UnsafeMutablePointer<UnsafeRawPointer?>!, _ numValues: CFIndex, _ callBacks: UnsafePointer<CFSetCallBacks>!) -> CFSet! ``` |

Modified [CFSetCreateMutable(_: CFAllocator!, _: CFIndex, _: UnsafePointer<CFSetCallBacks>!) -> CFMutableSet!](https://developer.apple.com/documentation/corefoundation/1520422-cfsetcreatemutable)

|  | Declaration |
| --- | --- |
| From | ``` func CFSetCreateMutable(_ allocator: CFAllocator!, _ capacity: CFIndex, _ callBacks: UnsafePointer<CFSetCallBacks>) -> CFMutableSet! ``` |
| To | ``` func CFSetCreateMutable(_ allocator: CFAllocator!, _ capacity: CFIndex, _ callBacks: UnsafePointer<CFSetCallBacks>!) -> CFMutableSet! ``` |

Modified [CFSetEqualCallBack](https://developer.apple.com/documentation/corefoundation/cfsetequalcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFSetEqualCallBack = (UnsafePointer<Void>, UnsafePointer<Void>) -> DarwinBoolean ``` |
| To | ``` typealias CFSetEqualCallBack = (UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean ``` |

Modified [CFSetGetCountOfValue(_: CFSet!, _: UnsafeRawPointer!) -> CFIndex](https://developer.apple.com/documentation/corefoundation/1520405-cfsetgetcountofvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFSetGetCountOfValue(_ theSet: CFSet!, _ value: UnsafePointer<Void>) -> CFIndex ``` |
| To | ``` func CFSetGetCountOfValue(_ theSet: CFSet!, _ value: UnsafeRawPointer!) -> CFIndex ``` |

Modified [CFSetGetValue(_: CFSet!, _: UnsafeRawPointer!) -> UnsafeRawPointer!](https://developer.apple.com/documentation/corefoundation/1520426-cfsetgetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFSetGetValue(_ theSet: CFSet!, _ value: UnsafePointer<Void>) -> UnsafePointer<Void> ``` |
| To | ``` func CFSetGetValue(_ theSet: CFSet!, _ value: UnsafeRawPointer!) -> UnsafeRawPointer! ``` |

Modified [CFSetGetValueIfPresent(_: CFSet!, _: UnsafeRawPointer!, _: UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1520409-cfsetgetvalueifpresent)

|  | Declaration |
| --- | --- |
| From | ``` func CFSetGetValueIfPresent(_ theSet: CFSet!, _ candidate: UnsafePointer<Void>, _ value: UnsafeMutablePointer<UnsafePointer<Void>>) -> Bool ``` |
| To | ``` func CFSetGetValueIfPresent(_ theSet: CFSet!, _ candidate: UnsafeRawPointer!, _ value: UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool ``` |

Modified [CFSetGetValues(_: CFSet!, _: UnsafeMutablePointer<UnsafeRawPointer?>!)](https://developer.apple.com/documentation/corefoundation/1520437-cfsetgetvalues)

|  | Declaration |
| --- | --- |
| From | ``` func CFSetGetValues(_ theSet: CFSet!, _ values: UnsafeMutablePointer<UnsafePointer<Void>>) ``` |
| To | ``` func CFSetGetValues(_ theSet: CFSet!, _ values: UnsafeMutablePointer<UnsafeRawPointer?>!) ``` |

Modified [CFSetHashCallBack](https://developer.apple.com/documentation/corefoundation/cfsethashcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFSetHashCallBack = (UnsafePointer<Void>) -> CFHashCode ``` |
| To | ``` typealias CFSetHashCallBack = (UnsafeRawPointer?) -> CFHashCode ``` |

Modified [CFSetReleaseCallBack](https://developer.apple.com/documentation/corefoundation/cfsetreleasecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFSetReleaseCallBack = (CFAllocator!, UnsafePointer<Void>) -> Void ``` |
| To | ``` typealias CFSetReleaseCallBack = (CFAllocator?, UnsafeRawPointer?) -> Swift.Void ``` |

Modified [CFSetRemoveValue(_: CFMutableSet!, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/corefoundation/1520411-cfsetremovevalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFSetRemoveValue(_ theSet: CFMutableSet!, _ value: UnsafePointer<Void>) ``` |
| To | ``` func CFSetRemoveValue(_ theSet: CFMutableSet!, _ value: UnsafeRawPointer!) ``` |

Modified [CFSetReplaceValue(_: CFMutableSet!, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/corefoundation/1520431-cfsetreplacevalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFSetReplaceValue(_ theSet: CFMutableSet!, _ value: UnsafePointer<Void>) ``` |
| To | ``` func CFSetReplaceValue(_ theSet: CFMutableSet!, _ value: UnsafeRawPointer!) ``` |

Modified [CFSetRetainCallBack](https://developer.apple.com/documentation/corefoundation/cfsetretaincallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFSetRetainCallBack = (CFAllocator!, UnsafePointer<Void>) -> UnsafePointer<Void> ``` |
| To | ``` typealias CFSetRetainCallBack = (CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer? ``` |

Modified [CFSetSetValue(_: CFMutableSet!, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/corefoundation/1520414-cfsetsetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFSetSetValue(_ theSet: CFMutableSet!, _ value: UnsafePointer<Void>) ``` |
| To | ``` func CFSetSetValue(_ theSet: CFMutableSet!, _ value: UnsafeRawPointer!) ``` |

Modified [CFShow(_: CFTypeRef!)](https://developer.apple.com/documentation/corefoundation/1541433-cfshow)

|  | Declaration |
| --- | --- |
| From | ``` func CFShow(_ obj: AnyObject!) ``` |
| To | ``` func CFShow(_ obj: CFTypeRef!) ``` |

Modified [CFSocketCallBack](https://developer.apple.com/documentation/corefoundation/cfsocketcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFSocketCallBack = (CFSocket!, CFSocketCallBackType, CFData!, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CFSocketCallBack = (CFSocket?, CFSocketCallBackType, CFData?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CFSocketCopyRegisteredSocketSignature(_: UnsafePointer<CFSocketSignature>!, _: CFTimeInterval, _: CFString!, _: UnsafeMutablePointer<CFSocketSignature>!, _: UnsafeMutablePointer<Unmanaged<CFData>?>!) -> CFSocketError](https://developer.apple.com/documentation/corefoundation/1542772-cfsocketcopyregisteredsocketsign)

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketCopyRegisteredSocketSignature(_ nameServerSignature: UnsafePointer<CFSocketSignature>, _ timeout: CFTimeInterval, _ name: CFString!, _ signature: UnsafeMutablePointer<CFSocketSignature>, _ nameServerAddress: UnsafeMutablePointer<Unmanaged<CFData>?>) -> CFSocketError ``` |
| To | ``` func CFSocketCopyRegisteredSocketSignature(_ nameServerSignature: UnsafePointer<CFSocketSignature>!, _ timeout: CFTimeInterval, _ name: CFString!, _ signature: UnsafeMutablePointer<CFSocketSignature>!, _ nameServerAddress: UnsafeMutablePointer<Unmanaged<CFData>?>!) -> CFSocketError ``` |

Modified [CFSocketCopyRegisteredValue(_: UnsafePointer<CFSocketSignature>!, _: CFTimeInterval, _: CFString!, _: UnsafeMutablePointer<Unmanaged<CFPropertyList>?>!, _: UnsafeMutablePointer<Unmanaged<CFData>?>!) -> CFSocketError](https://developer.apple.com/documentation/corefoundation/1542084-cfsocketcopyregisteredvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketCopyRegisteredValue(_ nameServerSignature: UnsafePointer<CFSocketSignature>, _ timeout: CFTimeInterval, _ name: CFString!, _ value: UnsafeMutablePointer<Unmanaged<CFPropertyList>?>, _ nameServerAddress: UnsafeMutablePointer<Unmanaged<CFData>?>) -> CFSocketError ``` |
| To | ``` func CFSocketCopyRegisteredValue(_ nameServerSignature: UnsafePointer<CFSocketSignature>!, _ timeout: CFTimeInterval, _ name: CFString!, _ value: UnsafeMutablePointer<Unmanaged<CFPropertyList>?>!, _ nameServerAddress: UnsafeMutablePointer<Unmanaged<CFData>?>!) -> CFSocketError ``` |

Modified [CFSocketCreate(_: CFAllocator!, _: Int32, _: Int32, _: Int32, _: CFOptionFlags, _: CoreFoundation.CFSocketCallBack!, _: UnsafePointer<CFSocketContext>!) -> CFSocket!](https://developer.apple.com/documentation/corefoundation/1543527-cfsocketcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketCreate(_ allocator: CFAllocator!, _ protocolFamily: Int32, _ socketType: Int32, _ protocol: Int32, _ callBackTypes: CFOptionFlags, _ callout: CFSocketCallBack!, _ context: UnsafePointer<CFSocketContext>) -> CFSocket! ``` |
| To | ``` func CFSocketCreate(_ allocator: CFAllocator!, _ protocolFamily: Int32, _ socketType: Int32, _ protocol: Int32, _ callBackTypes: CFOptionFlags, _ callout: CoreFoundation.CFSocketCallBack!, _ context: UnsafePointer<CFSocketContext>!) -> CFSocket! ``` |

Modified [CFSocketCreateConnectedToSocketSignature(_: CFAllocator!, _: UnsafePointer<CFSocketSignature>!, _: CFOptionFlags, _: CoreFoundation.CFSocketCallBack!, _: UnsafePointer<CFSocketContext>!, _: CFTimeInterval) -> CFSocket!](https://developer.apple.com/documentation/corefoundation/1542283-cfsocketcreateconnectedtosockets)

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketCreateConnectedToSocketSignature(_ allocator: CFAllocator!, _ signature: UnsafePointer<CFSocketSignature>, _ callBackTypes: CFOptionFlags, _ callout: CFSocketCallBack!, _ context: UnsafePointer<CFSocketContext>, _ timeout: CFTimeInterval) -> CFSocket! ``` |
| To | ``` func CFSocketCreateConnectedToSocketSignature(_ allocator: CFAllocator!, _ signature: UnsafePointer<CFSocketSignature>!, _ callBackTypes: CFOptionFlags, _ callout: CoreFoundation.CFSocketCallBack!, _ context: UnsafePointer<CFSocketContext>!, _ timeout: CFTimeInterval) -> CFSocket! ``` |

Modified [CFSocketCreateWithNative(_: CFAllocator!, _: CFSocketNativeHandle, _: CFOptionFlags, _: CoreFoundation.CFSocketCallBack!, _: UnsafePointer<CFSocketContext>!) -> CFSocket!](https://developer.apple.com/documentation/corefoundation/1543295-cfsocketcreatewithnative)

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketCreateWithNative(_ allocator: CFAllocator!, _ sock: CFSocketNativeHandle, _ callBackTypes: CFOptionFlags, _ callout: CFSocketCallBack!, _ context: UnsafePointer<CFSocketContext>) -> CFSocket! ``` |
| To | ``` func CFSocketCreateWithNative(_ allocator: CFAllocator!, _ sock: CFSocketNativeHandle, _ callBackTypes: CFOptionFlags, _ callout: CoreFoundation.CFSocketCallBack!, _ context: UnsafePointer<CFSocketContext>!) -> CFSocket! ``` |

Modified [CFSocketCreateWithSocketSignature(_: CFAllocator!, _: UnsafePointer<CFSocketSignature>!, _: CFOptionFlags, _: CoreFoundation.CFSocketCallBack!, _: UnsafePointer<CFSocketContext>!) -> CFSocket!](https://developer.apple.com/documentation/corefoundation/1542862-cfsocketcreatewithsocketsignatur)

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketCreateWithSocketSignature(_ allocator: CFAllocator!, _ signature: UnsafePointer<CFSocketSignature>, _ callBackTypes: CFOptionFlags, _ callout: CFSocketCallBack!, _ context: UnsafePointer<CFSocketContext>) -> CFSocket! ``` |
| To | ``` func CFSocketCreateWithSocketSignature(_ allocator: CFAllocator!, _ signature: UnsafePointer<CFSocketSignature>!, _ callBackTypes: CFOptionFlags, _ callout: CoreFoundation.CFSocketCallBack!, _ context: UnsafePointer<CFSocketContext>!) -> CFSocket! ``` |

Modified [CFSocketGetContext(_: CFSocket!, _: UnsafeMutablePointer<CFSocketContext>!)](https://developer.apple.com/documentation/corefoundation/1541549-cfsocketgetcontext)

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketGetContext(_ s: CFSocket!, _ context: UnsafeMutablePointer<CFSocketContext>) ``` |
| To | ``` func CFSocketGetContext(_ s: CFSocket!, _ context: UnsafeMutablePointer<CFSocketContext>!) ``` |

Modified [CFSocketRegisterSocketSignature(_: UnsafePointer<CFSocketSignature>!, _: CFTimeInterval, _: CFString!, _: UnsafePointer<CFSocketSignature>!) -> CFSocketError](https://developer.apple.com/documentation/corefoundation/1542142-cfsocketregistersocketsignature)

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketRegisterSocketSignature(_ nameServerSignature: UnsafePointer<CFSocketSignature>, _ timeout: CFTimeInterval, _ name: CFString!, _ signature: UnsafePointer<CFSocketSignature>) -> CFSocketError ``` |
| To | ``` func CFSocketRegisterSocketSignature(_ nameServerSignature: UnsafePointer<CFSocketSignature>!, _ timeout: CFTimeInterval, _ name: CFString!, _ signature: UnsafePointer<CFSocketSignature>!) -> CFSocketError ``` |

Modified [CFSocketRegisterValue(_: UnsafePointer<CFSocketSignature>!, _: CFTimeInterval, _: CFString!, _: CFPropertyList!) -> CFSocketError](https://developer.apple.com/documentation/corefoundation/1542420-cfsocketregistervalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketRegisterValue(_ nameServerSignature: UnsafePointer<CFSocketSignature>, _ timeout: CFTimeInterval, _ name: CFString!, _ value: CFPropertyList!) -> CFSocketError ``` |
| To | ``` func CFSocketRegisterValue(_ nameServerSignature: UnsafePointer<CFSocketSignature>!, _ timeout: CFTimeInterval, _ name: CFString!, _ value: CFPropertyList!) -> CFSocketError ``` |

Modified [CFSocketUnregister(_: UnsafePointer<CFSocketSignature>!, _: CFTimeInterval, _: CFString!) -> CFSocketError](https://developer.apple.com/documentation/corefoundation/1543652-cfsocketunregister)

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketUnregister(_ nameServerSignature: UnsafePointer<CFSocketSignature>, _ timeout: CFTimeInterval, _ name: CFString!) -> CFSocketError ``` |
| To | ``` func CFSocketUnregister(_ nameServerSignature: UnsafePointer<CFSocketSignature>!, _ timeout: CFTimeInterval, _ name: CFString!) -> CFSocketError ``` |

Modified [CFStreamCreateBoundPair(_: CFAllocator!, _: UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, _: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!, _: CFIndex)](https://developer.apple.com/documentation/corefoundation/1539710-cfstreamcreateboundpair)

|  | Declaration |
| --- | --- |
| From | ``` func CFStreamCreateBoundPair(_ alloc: CFAllocator!, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>, _ transferBufferSize: CFIndex) ``` |
| To | ``` func CFStreamCreateBoundPair(_ alloc: CFAllocator!, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!, _ transferBufferSize: CFIndex) ``` |

Modified [CFStreamCreatePairWithPeerSocketSignature(_: CFAllocator!, _: UnsafePointer<CFSocketSignature>!, _: UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, _: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!)](https://developer.apple.com/documentation/corefoundation/1539702-cfstreamcreatepairwithpeersocket)

|  | Declaration |
| --- | --- |
| From | ``` func CFStreamCreatePairWithPeerSocketSignature(_ alloc: CFAllocator!, _ signature: UnsafePointer<CFSocketSignature>, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>) ``` |
| To | ``` func CFStreamCreatePairWithPeerSocketSignature(_ alloc: CFAllocator!, _ signature: UnsafePointer<CFSocketSignature>!, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!) ``` |

Modified [CFStreamCreatePairWithSocket(_: CFAllocator!, _: CFSocketNativeHandle, _: UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, _: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!)](https://developer.apple.com/documentation/corefoundation/1539642-cfstreamcreatepairwithsocket)

|  | Declaration |
| --- | --- |
| From | ``` func CFStreamCreatePairWithSocket(_ alloc: CFAllocator!, _ sock: CFSocketNativeHandle, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>) ``` |
| To | ``` func CFStreamCreatePairWithSocket(_ alloc: CFAllocator!, _ sock: CFSocketNativeHandle, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!) ``` |

Modified [CFStreamCreatePairWithSocketToHost(_: CFAllocator!, _: CFString!, _: UInt32, _: UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, _: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!)](https://developer.apple.com/documentation/corefoundation/1539739-cfstreamcreatepairwithsockettoho)

|  | Declaration |
| --- | --- |
| From | ``` func CFStreamCreatePairWithSocketToHost(_ alloc: CFAllocator!, _ host: CFString!, _ port: UInt32, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>) ``` |
| To | ``` func CFStreamCreatePairWithSocketToHost(_ alloc: CFAllocator!, _ host: CFString!, _ port: UInt32, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!) ``` |

Modified [CFStringAppendCharacters(_: CFMutableString!, _: UnsafePointer<UniChar>!, _: CFIndex)](https://developer.apple.com/documentation/corefoundation/1543667-cfstringappendcharacters)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringAppendCharacters(_ theString: CFMutableString!, _ chars: UnsafePointer<UniChar>, _ numChars: CFIndex) ``` |
| To | ``` func CFStringAppendCharacters(_ theString: CFMutableString!, _ chars: UnsafePointer<UniChar>!, _ numChars: CFIndex) ``` |

Modified [CFStringAppendCString(_: CFMutableString!, _: UnsafePointer<Int8>!, _: CFStringEncoding)](https://developer.apple.com/documentation/corefoundation/1543219-cfstringappendcstring)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringAppendCString(_ theString: CFMutableString!, _ cStr: UnsafePointer<Int8>, _ encoding: CFStringEncoding) ``` |
| To | ``` func CFStringAppendCString(_ theString: CFMutableString!, _ cStr: UnsafePointer<Int8>!, _ encoding: CFStringEncoding) ``` |

Modified [CFStringAppendFormatAndArguments(_: CFMutableString!, _: CFDictionary!, _: CFString!, _: CVaListPointer!)](https://developer.apple.com/documentation/corefoundation/1541757-cfstringappendformatandarguments)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringAppendFormatAndArguments(_ theString: CFMutableString!, _ formatOptions: CFDictionary!, _ format: CFString!, _ arguments: CVaListPointer) ``` |
| To | ``` func CFStringAppendFormatAndArguments(_ theString: CFMutableString!, _ formatOptions: CFDictionary!, _ format: CFString!, _ arguments: CVaListPointer!) ``` |

Modified [CFStringAppendPascalString(_: CFMutableString!, _: ConstStr255Param!, _: CFStringEncoding)](https://developer.apple.com/documentation/corefoundation/1541784-cfstringappendpascalstring)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringAppendPascalString(_ theString: CFMutableString!, _ pStr: ConstStr255Param, _ encoding: CFStringEncoding) ``` |
| To | ``` func CFStringAppendPascalString(_ theString: CFMutableString!, _ pStr: ConstStr255Param!, _ encoding: CFStringEncoding) ``` |

Modified [CFStringCreateMutableWithExternalCharactersNoCopy(_: CFAllocator!, _: UnsafeMutablePointer<UniChar>!, _: CFIndex, _: CFIndex, _: CFAllocator!) -> CFMutableString!](https://developer.apple.com/documentation/corefoundation/1542308-cfstringcreatemutablewithexterna)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringCreateMutableWithExternalCharactersNoCopy(_ alloc: CFAllocator!, _ chars: UnsafeMutablePointer<UniChar>, _ numChars: CFIndex, _ capacity: CFIndex, _ externalCharactersAllocator: CFAllocator!) -> CFMutableString! ``` |
| To | ``` func CFStringCreateMutableWithExternalCharactersNoCopy(_ alloc: CFAllocator!, _ chars: UnsafeMutablePointer<UniChar>!, _ numChars: CFIndex, _ capacity: CFIndex, _ externalCharactersAllocator: CFAllocator!) -> CFMutableString! ``` |

Modified [CFStringCreateWithBytes(_: CFAllocator!, _: UnsafePointer<UInt8>!, _: CFIndex, _: CFStringEncoding, _: Bool) -> CFString!](https://developer.apple.com/documentation/corefoundation/1543419-cfstringcreatewithbytes)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringCreateWithBytes(_ alloc: CFAllocator!, _ bytes: UnsafePointer<UInt8>, _ numBytes: CFIndex, _ encoding: CFStringEncoding, _ isExternalRepresentation: Bool) -> CFString! ``` |
| To | ``` func CFStringCreateWithBytes(_ alloc: CFAllocator!, _ bytes: UnsafePointer<UInt8>!, _ numBytes: CFIndex, _ encoding: CFStringEncoding, _ isExternalRepresentation: Bool) -> CFString! ``` |

Modified [CFStringCreateWithBytesNoCopy(_: CFAllocator!, _: UnsafePointer<UInt8>!, _: CFIndex, _: CFStringEncoding, _: Bool, _: CFAllocator!) -> CFString!](https://developer.apple.com/documentation/corefoundation/1543597-cfstringcreatewithbytesnocopy)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringCreateWithBytesNoCopy(_ alloc: CFAllocator!, _ bytes: UnsafePointer<UInt8>, _ numBytes: CFIndex, _ encoding: CFStringEncoding, _ isExternalRepresentation: Bool, _ contentsDeallocator: CFAllocator!) -> CFString! ``` |
| To | ``` func CFStringCreateWithBytesNoCopy(_ alloc: CFAllocator!, _ bytes: UnsafePointer<UInt8>!, _ numBytes: CFIndex, _ encoding: CFStringEncoding, _ isExternalRepresentation: Bool, _ contentsDeallocator: CFAllocator!) -> CFString! ``` |

Modified [CFStringCreateWithCharacters(_: CFAllocator!, _: UnsafePointer<UniChar>!, _: CFIndex) -> CFString!](https://developer.apple.com/documentation/corefoundation/1541779-cfstringcreatewithcharacters)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringCreateWithCharacters(_ alloc: CFAllocator!, _ chars: UnsafePointer<UniChar>, _ numChars: CFIndex) -> CFString! ``` |
| To | ``` func CFStringCreateWithCharacters(_ alloc: CFAllocator!, _ chars: UnsafePointer<UniChar>!, _ numChars: CFIndex) -> CFString! ``` |

Modified [CFStringCreateWithCharactersNoCopy(_: CFAllocator!, _: UnsafePointer<UniChar>!, _: CFIndex, _: CFAllocator!) -> CFString!](https://developer.apple.com/documentation/corefoundation/1542856-cfstringcreatewithcharactersnoco)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringCreateWithCharactersNoCopy(_ alloc: CFAllocator!, _ chars: UnsafePointer<UniChar>, _ numChars: CFIndex, _ contentsDeallocator: CFAllocator!) -> CFString! ``` |
| To | ``` func CFStringCreateWithCharactersNoCopy(_ alloc: CFAllocator!, _ chars: UnsafePointer<UniChar>!, _ numChars: CFIndex, _ contentsDeallocator: CFAllocator!) -> CFString! ``` |

Modified [CFStringCreateWithCString(_: CFAllocator!, _: UnsafePointer<Int8>!, _: CFStringEncoding) -> CFString!](https://developer.apple.com/documentation/corefoundation/1542942-cfstringcreatewithcstring)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringCreateWithCString(_ alloc: CFAllocator!, _ cStr: UnsafePointer<Int8>, _ encoding: CFStringEncoding) -> CFString! ``` |
| To | ``` func CFStringCreateWithCString(_ alloc: CFAllocator!, _ cStr: UnsafePointer<Int8>!, _ encoding: CFStringEncoding) -> CFString! ``` |

Modified [CFStringCreateWithCStringNoCopy(_: CFAllocator!, _: UnsafePointer<Int8>!, _: CFStringEncoding, _: CFAllocator!) -> CFString!](https://developer.apple.com/documentation/corefoundation/1542134-cfstringcreatewithcstringnocopy)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringCreateWithCStringNoCopy(_ alloc: CFAllocator!, _ cStr: UnsafePointer<Int8>, _ encoding: CFStringEncoding, _ contentsDeallocator: CFAllocator!) -> CFString! ``` |
| To | ``` func CFStringCreateWithCStringNoCopy(_ alloc: CFAllocator!, _ cStr: UnsafePointer<Int8>!, _ encoding: CFStringEncoding, _ contentsDeallocator: CFAllocator!) -> CFString! ``` |

Modified [CFStringCreateWithFileSystemRepresentation(_: CFAllocator!, _: UnsafePointer<Int8>!) -> CFString!](https://developer.apple.com/documentation/corefoundation/1543636-cfstringcreatewithfilesystemrepr)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringCreateWithFileSystemRepresentation(_ alloc: CFAllocator!, _ buffer: UnsafePointer<Int8>) -> CFString! ``` |
| To | ``` func CFStringCreateWithFileSystemRepresentation(_ alloc: CFAllocator!, _ buffer: UnsafePointer<Int8>!) -> CFString! ``` |

Modified [CFStringCreateWithFormatAndArguments(_: CFAllocator!, _: CFDictionary!, _: CFString!, _: CVaListPointer!) -> CFString!](https://developer.apple.com/documentation/corefoundation/1542177-cfstringcreatewithformatandargum)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringCreateWithFormatAndArguments(_ alloc: CFAllocator!, _ formatOptions: CFDictionary!, _ format: CFString!, _ arguments: CVaListPointer) -> CFString! ``` |
| To | ``` func CFStringCreateWithFormatAndArguments(_ alloc: CFAllocator!, _ formatOptions: CFDictionary!, _ format: CFString!, _ arguments: CVaListPointer!) -> CFString! ``` |

Modified [CFStringCreateWithPascalString(_: CFAllocator!, _: ConstStr255Param!, _: CFStringEncoding) -> CFString!](https://developer.apple.com/documentation/corefoundation/1542754-cfstringcreatewithpascalstring)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringCreateWithPascalString(_ alloc: CFAllocator!, _ pStr: ConstStr255Param, _ encoding: CFStringEncoding) -> CFString! ``` |
| To | ``` func CFStringCreateWithPascalString(_ alloc: CFAllocator!, _ pStr: ConstStr255Param!, _ encoding: CFStringEncoding) -> CFString! ``` |

Modified [CFStringCreateWithPascalStringNoCopy(_: CFAllocator!, _: ConstStr255Param!, _: CFStringEncoding, _: CFAllocator!) -> CFString!](https://developer.apple.com/documentation/corefoundation/1543159-cfstringcreatewithpascalstringno)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringCreateWithPascalStringNoCopy(_ alloc: CFAllocator!, _ pStr: ConstStr255Param, _ encoding: CFStringEncoding, _ contentsDeallocator: CFAllocator!) -> CFString! ``` |
| To | ``` func CFStringCreateWithPascalStringNoCopy(_ alloc: CFAllocator!, _ pStr: ConstStr255Param!, _ encoding: CFStringEncoding, _ contentsDeallocator: CFAllocator!) -> CFString! ``` |

Modified [CFStringFindCharacterFromSet(_: CFString!, _: CFCharacterSet!, _: CFRange, _: CFStringCompareFlags, _: UnsafeMutablePointer<CFRange>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1542060-cfstringfindcharacterfromset)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringFindCharacterFromSet(_ theString: CFString!, _ theSet: CFCharacterSet!, _ rangeToSearch: CFRange, _ searchOptions: CFStringCompareFlags, _ result: UnsafeMutablePointer<CFRange>) -> Bool ``` |
| To | ``` func CFStringFindCharacterFromSet(_ theString: CFString!, _ theSet: CFCharacterSet!, _ rangeToSearch: CFRange, _ searchOptions: CFStringCompareFlags, _ result: UnsafeMutablePointer<CFRange>!) -> Bool ``` |

Modified [CFStringFindWithOptions(_: CFString!, _: CFString!, _: CFRange, _: CFStringCompareFlags, _: UnsafeMutablePointer<CFRange>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1543522-cfstringfindwithoptions)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringFindWithOptions(_ theString: CFString!, _ stringToFind: CFString!, _ rangeToSearch: CFRange, _ searchOptions: CFStringCompareFlags, _ result: UnsafeMutablePointer<CFRange>) -> Bool ``` |
| To | ``` func CFStringFindWithOptions(_ theString: CFString!, _ stringToFind: CFString!, _ rangeToSearch: CFRange, _ searchOptions: CFStringCompareFlags, _ result: UnsafeMutablePointer<CFRange>!) -> Bool ``` |

Modified [CFStringFindWithOptionsAndLocale(_: CFString!, _: CFString!, _: CFRange, _: CFStringCompareFlags, _: CFLocale!, _: UnsafeMutablePointer<CFRange>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1543620-cfstringfindwithoptionsandlocale)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringFindWithOptionsAndLocale(_ theString: CFString!, _ stringToFind: CFString!, _ rangeToSearch: CFRange, _ searchOptions: CFStringCompareFlags, _ locale: CFLocale!, _ result: UnsafeMutablePointer<CFRange>) -> Bool ``` |
| To | ``` func CFStringFindWithOptionsAndLocale(_ theString: CFString!, _ stringToFind: CFString!, _ rangeToSearch: CFRange, _ searchOptions: CFStringCompareFlags, _ locale: CFLocale!, _ result: UnsafeMutablePointer<CFRange>!) -> Bool ``` |

Modified [CFStringGetBytes(_: CFString!, _: CFRange, _: CFStringEncoding, _: UInt8, _: Bool, _: UnsafeMutablePointer<UInt8>!, _: CFIndex, _: UnsafeMutablePointer<CFIndex>!) -> CFIndex](https://developer.apple.com/documentation/corefoundation/1543006-cfstringgetbytes)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetBytes(_ theString: CFString!, _ range: CFRange, _ encoding: CFStringEncoding, _ lossByte: UInt8, _ isExternalRepresentation: Bool, _ buffer: UnsafeMutablePointer<UInt8>, _ maxBufLen: CFIndex, _ usedBufLen: UnsafeMutablePointer<CFIndex>) -> CFIndex ``` |
| To | ``` func CFStringGetBytes(_ theString: CFString!, _ range: CFRange, _ encoding: CFStringEncoding, _ lossByte: UInt8, _ isExternalRepresentation: Bool, _ buffer: UnsafeMutablePointer<UInt8>!, _ maxBufLen: CFIndex, _ usedBufLen: UnsafeMutablePointer<CFIndex>!) -> CFIndex ``` |

Modified [CFStringGetCharacterFromInlineBuffer(_: UnsafeMutablePointer<CFStringInlineBuffer>!, _: CFIndex) -> UniChar](https://developer.apple.com/documentation/corefoundation/1542834-cfstringgetcharacterfrominlinebu)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetCharacterFromInlineBuffer(_ buf: UnsafeMutablePointer<CFStringInlineBuffer>, _ idx: CFIndex) -> UniChar ``` |
| To | ``` func CFStringGetCharacterFromInlineBuffer(_ buf: UnsafeMutablePointer<CFStringInlineBuffer>!, _ idx: CFIndex) -> UniChar ``` |

Modified [CFStringGetCharacters(_: CFString!, _: CFRange, _: UnsafeMutablePointer<UniChar>!)](https://developer.apple.com/documentation/corefoundation/1542656-cfstringgetcharacters)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetCharacters(_ theString: CFString!, _ range: CFRange, _ buffer: UnsafeMutablePointer<UniChar>) ``` |
| To | ``` func CFStringGetCharacters(_ theString: CFString!, _ range: CFRange, _ buffer: UnsafeMutablePointer<UniChar>!) ``` |

Modified [CFStringGetCharactersPtr(_: CFString!) -> UnsafePointer<UniChar>!](https://developer.apple.com/documentation/corefoundation/1542939-cfstringgetcharactersptr)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetCharactersPtr(_ theString: CFString!) -> UnsafePointer<UniChar> ``` |
| To | ``` func CFStringGetCharactersPtr(_ theString: CFString!) -> UnsafePointer<UniChar>! ``` |

Modified [CFStringGetCString(_: CFString!, _: UnsafeMutablePointer<Int8>!, _: CFIndex, _: CFStringEncoding) -> Bool](https://developer.apple.com/documentation/corefoundation/1542721-cfstringgetcstring)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetCString(_ theString: CFString!, _ buffer: UnsafeMutablePointer<Int8>, _ bufferSize: CFIndex, _ encoding: CFStringEncoding) -> Bool ``` |
| To | ``` func CFStringGetCString(_ theString: CFString!, _ buffer: UnsafeMutablePointer<Int8>!, _ bufferSize: CFIndex, _ encoding: CFStringEncoding) -> Bool ``` |

Modified [CFStringGetCStringPtr(_: CFString!, _: CFStringEncoding) -> UnsafePointer<Int8>!](https://developer.apple.com/documentation/corefoundation/1542133-cfstringgetcstringptr)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetCStringPtr(_ theString: CFString!, _ encoding: CFStringEncoding) -> UnsafePointer<Int8> ``` |
| To | ``` func CFStringGetCStringPtr(_ theString: CFString!, _ encoding: CFStringEncoding) -> UnsafePointer<Int8>! ``` |

Modified [CFStringGetFileSystemRepresentation(_: CFString!, _: UnsafeMutablePointer<Int8>!, _: CFIndex) -> Bool](https://developer.apple.com/documentation/corefoundation/1542019-cfstringgetfilesystemrepresentat)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetFileSystemRepresentation(_ string: CFString!, _ buffer: UnsafeMutablePointer<Int8>, _ maxBufLen: CFIndex) -> Bool ``` |
| To | ``` func CFStringGetFileSystemRepresentation(_ string: CFString!, _ buffer: UnsafeMutablePointer<Int8>!, _ maxBufLen: CFIndex) -> Bool ``` |

Modified [CFStringGetHyphenationLocationBeforeIndex(_: CFString!, _: CFIndex, _: CFRange, _: CFOptionFlags, _: CFLocale!, _: UnsafeMutablePointer<UTF32Char>!) -> CFIndex](https://developer.apple.com/documentation/corefoundation/1542693-cfstringgethyphenationlocationbe)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetHyphenationLocationBeforeIndex(_ string: CFString!, _ location: CFIndex, _ limitRange: CFRange, _ options: CFOptionFlags, _ locale: CFLocale!, _ character: UnsafeMutablePointer<UTF32Char>) -> CFIndex ``` |
| To | ``` func CFStringGetHyphenationLocationBeforeIndex(_ string: CFString!, _ location: CFIndex, _ limitRange: CFRange, _ options: CFOptionFlags, _ locale: CFLocale!, _ character: UnsafeMutablePointer<UTF32Char>!) -> CFIndex ``` |

Modified [CFStringGetLineBounds(_: CFString!, _: CFRange, _: UnsafeMutablePointer<CFIndex>!, _: UnsafeMutablePointer<CFIndex>!, _: UnsafeMutablePointer<CFIndex>!)](https://developer.apple.com/documentation/corefoundation/1541640-cfstringgetlinebounds)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetLineBounds(_ theString: CFString!, _ range: CFRange, _ lineBeginIndex: UnsafeMutablePointer<CFIndex>, _ lineEndIndex: UnsafeMutablePointer<CFIndex>, _ contentsEndIndex: UnsafeMutablePointer<CFIndex>) ``` |
| To | ``` func CFStringGetLineBounds(_ theString: CFString!, _ range: CFRange, _ lineBeginIndex: UnsafeMutablePointer<CFIndex>!, _ lineEndIndex: UnsafeMutablePointer<CFIndex>!, _ contentsEndIndex: UnsafeMutablePointer<CFIndex>!) ``` |

Modified [CFStringGetListOfAvailableEncodings() -> UnsafePointer<CFStringEncoding>!](https://developer.apple.com/documentation/corefoundation/1542932-cfstringgetlistofavailableencodi)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetListOfAvailableEncodings() -> UnsafePointer<CFStringEncoding> ``` |
| To | ``` func CFStringGetListOfAvailableEncodings() -> UnsafePointer<CFStringEncoding>! ``` |

Modified [CFStringGetParagraphBounds(_: CFString!, _: CFRange, _: UnsafeMutablePointer<CFIndex>!, _: UnsafeMutablePointer<CFIndex>!, _: UnsafeMutablePointer<CFIndex>!)](https://developer.apple.com/documentation/corefoundation/1542144-cfstringgetparagraphbounds)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetParagraphBounds(_ string: CFString!, _ range: CFRange, _ parBeginIndex: UnsafeMutablePointer<CFIndex>, _ parEndIndex: UnsafeMutablePointer<CFIndex>, _ contentsEndIndex: UnsafeMutablePointer<CFIndex>) ``` |
| To | ``` func CFStringGetParagraphBounds(_ string: CFString!, _ range: CFRange, _ parBeginIndex: UnsafeMutablePointer<CFIndex>!, _ parEndIndex: UnsafeMutablePointer<CFIndex>!, _ contentsEndIndex: UnsafeMutablePointer<CFIndex>!) ``` |

Modified [CFStringGetPascalString(_: CFString!, _: StringPtr!, _: CFIndex, _: CFStringEncoding) -> Bool](https://developer.apple.com/documentation/corefoundation/1543322-cfstringgetpascalstring)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetPascalString(_ theString: CFString!, _ buffer: StringPtr, _ bufferSize: CFIndex, _ encoding: CFStringEncoding) -> Bool ``` |
| To | ``` func CFStringGetPascalString(_ theString: CFString!, _ buffer: StringPtr!, _ bufferSize: CFIndex, _ encoding: CFStringEncoding) -> Bool ``` |

Modified [CFStringGetPascalStringPtr(_: CFString!, _: CFStringEncoding) -> ConstStringPtr!](https://developer.apple.com/documentation/corefoundation/1541777-cfstringgetpascalstringptr)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetPascalStringPtr(_ theString: CFString!, _ encoding: CFStringEncoding) -> ConstStringPtr ``` |
| To | ``` func CFStringGetPascalStringPtr(_ theString: CFString!, _ encoding: CFStringEncoding) -> ConstStringPtr! ``` |

Modified [CFStringGetSurrogatePairForLongCharacter(_: UTF32Char, _: UnsafeMutablePointer<UniChar>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1541601-cfstringgetsurrogatepairforlongc)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringGetSurrogatePairForLongCharacter(_ character: UTF32Char, _ surrogates: UnsafeMutablePointer<UniChar>) -> Bool ``` |
| To | ``` func CFStringGetSurrogatePairForLongCharacter(_ character: UTF32Char, _ surrogates: UnsafeMutablePointer<UniChar>!) -> Bool ``` |

Modified [CFStringInitInlineBuffer(_: CFString!, _: UnsafeMutablePointer<CFStringInlineBuffer>!, _: CFRange)](https://developer.apple.com/documentation/corefoundation/1543661-cfstringinitinlinebuffer)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringInitInlineBuffer(_ str: CFString!, _ buf: UnsafeMutablePointer<CFStringInlineBuffer>, _ range: CFRange) ``` |
| To | ``` func CFStringInitInlineBuffer(_ str: CFString!, _ buf: UnsafeMutablePointer<CFStringInlineBuffer>!, _ range: CFRange) ``` |

Modified [CFStringSetExternalCharactersNoCopy(_: CFMutableString!, _: UnsafeMutablePointer<UniChar>!, _: CFIndex, _: CFIndex)](https://developer.apple.com/documentation/corefoundation/1542035-cfstringsetexternalcharactersnoc)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringSetExternalCharactersNoCopy(_ theString: CFMutableString!, _ chars: UnsafeMutablePointer<UniChar>, _ length: CFIndex, _ capacity: CFIndex) ``` |
| To | ``` func CFStringSetExternalCharactersNoCopy(_ theString: CFMutableString!, _ chars: UnsafeMutablePointer<UniChar>!, _ length: CFIndex, _ capacity: CFIndex) ``` |

Modified [CFStringTokenizerCopyCurrentTokenAttribute(_: CFStringTokenizer!, _: CFOptionFlags) -> CFTypeRef!](https://developer.apple.com/documentation/corefoundation/1542839-cfstringtokenizercopycurrenttoke)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringTokenizerCopyCurrentTokenAttribute(_ tokenizer: CFStringTokenizer!, _ attribute: CFOptionFlags) -> AnyObject! ``` |
| To | ``` func CFStringTokenizerCopyCurrentTokenAttribute(_ tokenizer: CFStringTokenizer!, _ attribute: CFOptionFlags) -> CFTypeRef! ``` |

Modified [CFStringTokenizerGetCurrentSubTokens(_: CFStringTokenizer!, _: UnsafeMutablePointer<CFRange>!, _: CFIndex, _: CFMutableArray!) -> CFIndex](https://developer.apple.com/documentation/corefoundation/1542209-cfstringtokenizergetcurrentsubto)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringTokenizerGetCurrentSubTokens(_ tokenizer: CFStringTokenizer!, _ ranges: UnsafeMutablePointer<CFRange>, _ maxRangeLength: CFIndex, _ derivedSubTokens: CFMutableArray!) -> CFIndex ``` |
| To | ``` func CFStringTokenizerGetCurrentSubTokens(_ tokenizer: CFStringTokenizer!, _ ranges: UnsafeMutablePointer<CFRange>!, _ maxRangeLength: CFIndex, _ derivedSubTokens: CFMutableArray!) -> CFIndex ``` |

Modified [CFStringTransform(_: CFMutableString!, _: UnsafeMutablePointer<CFRange>!, _: CFString!, _: Bool) -> Bool](https://developer.apple.com/documentation/corefoundation/1542411-cfstringtransform)

|  | Declaration |
| --- | --- |
| From | ``` func CFStringTransform(_ string: CFMutableString!, _ range: UnsafeMutablePointer<CFRange>, _ transform: CFString!, _ reverse: Bool) -> Bool ``` |
| To | ``` func CFStringTransform(_ string: CFMutableString!, _ range: UnsafeMutablePointer<CFRange>!, _ transform: CFString!, _ reverse: Bool) -> Bool ``` |

Modified [CFTreeApplierFunction](https://developer.apple.com/documentation/corefoundation/cftreeapplierfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFTreeApplierFunction = (UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CFTreeApplierFunction = (UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CFTreeApplyFunctionToChildren(_: CFTree!, _: ((UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)!, _: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/corefoundation/1401759-cftreeapplyfunctiontochildren)

|  | Declaration |
| --- | --- |
| From | ``` func CFTreeApplyFunctionToChildren(_ tree: CFTree!, _ applier: CFTreeApplierFunction!, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func CFTreeApplyFunctionToChildren(_ tree: CFTree!, _ applier: ((UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)!, _ context: UnsafeMutableRawPointer!) ``` |

Modified [CFTreeCopyDescriptionCallBack](https://developer.apple.com/documentation/corefoundation/cftreecopydescriptioncallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFTreeCopyDescriptionCallBack = (UnsafePointer<Void>) -> Unmanaged<CFString>! ``` |
| To | ``` typealias CFTreeCopyDescriptionCallBack = (UnsafeRawPointer?) -> Unmanaged<CFString>? ``` |

Modified [CFTreeCreate(_: CFAllocator!, _: UnsafePointer<CFTreeContext>!) -> CFTree!](https://developer.apple.com/documentation/corefoundation/1401814-cftreecreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFTreeCreate(_ allocator: CFAllocator!, _ context: UnsafePointer<CFTreeContext>) -> CFTree! ``` |
| To | ``` func CFTreeCreate(_ allocator: CFAllocator!, _ context: UnsafePointer<CFTreeContext>!) -> CFTree! ``` |

Modified [CFTreeGetChildren(_: CFTree!, _: UnsafeMutablePointer<Unmanaged<CFTree>?>!)](https://developer.apple.com/documentation/corefoundation/1401761-cftreegetchildren)

|  | Declaration |
| --- | --- |
| From | ``` func CFTreeGetChildren(_ tree: CFTree!, _ children: UnsafeMutablePointer<Unmanaged<CFTree>?>) ``` |
| To | ``` func CFTreeGetChildren(_ tree: CFTree!, _ children: UnsafeMutablePointer<Unmanaged<CFTree>?>!) ``` |

Modified [CFTreeGetContext(_: CFTree!, _: UnsafeMutablePointer<CFTreeContext>!)](https://developer.apple.com/documentation/corefoundation/1401802-cftreegetcontext)

|  | Declaration |
| --- | --- |
| From | ``` func CFTreeGetContext(_ tree: CFTree!, _ context: UnsafeMutablePointer<CFTreeContext>) ``` |
| To | ``` func CFTreeGetContext(_ tree: CFTree!, _ context: UnsafeMutablePointer<CFTreeContext>!) ``` |

Modified [CFTreeReleaseCallBack](https://developer.apple.com/documentation/corefoundation/cftreereleasecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFTreeReleaseCallBack = (UnsafePointer<Void>) -> Void ``` |
| To | ``` typealias CFTreeReleaseCallBack = (UnsafeRawPointer?) -> Swift.Void ``` |

Modified [CFTreeRetainCallBack](https://developer.apple.com/documentation/corefoundation/cftreeretaincallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFTreeRetainCallBack = (UnsafePointer<Void>) -> UnsafePointer<Void> ``` |
| To | ``` typealias CFTreeRetainCallBack = (UnsafeRawPointer?) -> UnsafeRawPointer? ``` |

Modified [CFTreeSetContext(_: CFTree!, _: UnsafePointer<CFTreeContext>!)](https://developer.apple.com/documentation/corefoundation/1401775-cftreesetcontext)

|  | Declaration |
| --- | --- |
| From | ``` func CFTreeSetContext(_ tree: CFTree!, _ context: UnsafePointer<CFTreeContext>) ``` |
| To | ``` func CFTreeSetContext(_ tree: CFTree!, _ context: UnsafePointer<CFTreeContext>!) ``` |

Modified [CFTreeSortChildren(_: CFTree!, _: CoreFoundation.CFComparatorFunction!, _: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/corefoundation/1401787-cftreesortchildren)

|  | Declaration |
| --- | --- |
| From | ``` func CFTreeSortChildren(_ tree: CFTree!, _ comparator: CFComparatorFunction!, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func CFTreeSortChildren(_ tree: CFTree!, _ comparator: CoreFoundation.CFComparatorFunction!, _ context: UnsafeMutableRawPointer!) ``` |

Modified [CFURLCopyResourcePropertiesForKeys(_: CFURL!, _: CFArray!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](https://developer.apple.com/documentation/corefoundation/1542370-cfurlcopyresourcepropertiesforke)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCopyResourcePropertiesForKeys(_ url: CFURL!, _ keys: CFArray!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func CFURLCopyResourcePropertiesForKeys(_ url: CFURL!, _ keys: CFArray!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>! ``` |

Modified [CFURLCopyResourcePropertyForKey(_: CFURL!, _: CFString!, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1542764-cfurlcopyresourcepropertyforkey)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCopyResourcePropertyForKey(_ url: CFURL!, _ key: CFString!, _ propertyValueTypeRefPtr: UnsafeMutablePointer<Void>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func CFURLCopyResourcePropertyForKey(_ url: CFURL!, _ key: CFString!, _ propertyValueTypeRefPtr: UnsafeMutableRawPointer!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [CFURLCopyStrictPath(_: CFURL!, _: UnsafeMutablePointer<DarwinBoolean>!) -> CFString!](https://developer.apple.com/documentation/corefoundation/1542952-cfurlcopystrictpath)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCopyStrictPath(_ anURL: CFURL!, _ isAbsolute: UnsafeMutablePointer<DarwinBoolean>) -> CFString! ``` |
| To | ``` func CFURLCopyStrictPath(_ anURL: CFURL!, _ isAbsolute: UnsafeMutablePointer<DarwinBoolean>!) -> CFString! ``` |

Modified [CFURLCreateAbsoluteURLWithBytes(_: CFAllocator!, _: UnsafePointer<UInt8>!, _: CFIndex, _: CFStringEncoding, _: CFURL!, _: Bool) -> CFURL!](https://developer.apple.com/documentation/corefoundation/1542795-cfurlcreateabsoluteurlwithbytes)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCreateAbsoluteURLWithBytes(_ alloc: CFAllocator!, _ relativeURLBytes: UnsafePointer<UInt8>, _ length: CFIndex, _ encoding: CFStringEncoding, _ baseURL: CFURL!, _ useCompatibilityMode: Bool) -> CFURL! ``` |
| To | ``` func CFURLCreateAbsoluteURLWithBytes(_ alloc: CFAllocator!, _ relativeURLBytes: UnsafePointer<UInt8>!, _ length: CFIndex, _ encoding: CFStringEncoding, _ baseURL: CFURL!, _ useCompatibilityMode: Bool) -> CFURL! ``` |

Modified [CFURLCreateBookmarkData(_: CFAllocator!, _: CFURL!, _: CFURLBookmarkCreationOptions, _: CFArray!, _: CFURL!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFData>!](https://developer.apple.com/documentation/corefoundation/1542923-cfurlcreatebookmarkdata)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCreateBookmarkData(_ allocator: CFAllocator!, _ url: CFURL!, _ options: CFURLBookmarkCreationOptions, _ resourcePropertiesToInclude: CFArray!, _ relativeToURL: CFURL!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>! ``` |
| To | ``` func CFURLCreateBookmarkData(_ allocator: CFAllocator!, _ url: CFURL!, _ options: CFURLBookmarkCreationOptions, _ resourcePropertiesToInclude: CFArray!, _ relativeToURL: CFURL!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFData>! ``` |

Modified [CFURLCreateBookmarkDataFromFile(_: CFAllocator!, _: CFURL!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFData>!](https://developer.apple.com/documentation/corefoundation/1543258-cfurlcreatebookmarkdatafromfile)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCreateBookmarkDataFromFile(_ allocator: CFAllocator!, _ fileURL: CFURL!, _ errorRef: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>! ``` |
| To | ``` func CFURLCreateBookmarkDataFromFile(_ allocator: CFAllocator!, _ fileURL: CFURL!, _ errorRef: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFData>! ``` |

Modified [CFURLCreateByResolvingBookmarkData(_: CFAllocator!, _: CFData!, _: CFURLBookmarkResolutionOptions, _: CFURL!, _: CFArray!, _: UnsafeMutablePointer<DarwinBoolean>!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFURL>!](https://developer.apple.com/documentation/corefoundation/1543252-cfurlcreatebyresolvingbookmarkda)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCreateByResolvingBookmarkData(_ allocator: CFAllocator!, _ bookmark: CFData!, _ options: CFURLBookmarkResolutionOptions, _ relativeToURL: CFURL!, _ resourcePropertiesToInclude: CFArray!, _ isStale: UnsafeMutablePointer<DarwinBoolean>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>! ``` |
| To | ``` func CFURLCreateByResolvingBookmarkData(_ allocator: CFAllocator!, _ bookmark: CFData!, _ options: CFURLBookmarkResolutionOptions, _ relativeToURL: CFURL!, _ resourcePropertiesToInclude: CFArray!, _ isStale: UnsafeMutablePointer<DarwinBoolean>!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFURL>! ``` |

Modified [CFURLCreateFilePathURL(_: CFAllocator!, _: CFURL!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFURL>!](https://developer.apple.com/documentation/corefoundation/1542076-cfurlcreatefilepathurl)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCreateFilePathURL(_ allocator: CFAllocator!, _ url: CFURL!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>! ``` |
| To | ``` func CFURLCreateFilePathURL(_ allocator: CFAllocator!, _ url: CFURL!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFURL>! ``` |

Modified [CFURLCreateFileReferenceURL(_: CFAllocator!, _: CFURL!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFURL>!](https://developer.apple.com/documentation/corefoundation/1543282-cfurlcreatefilereferenceurl)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCreateFileReferenceURL(_ allocator: CFAllocator!, _ url: CFURL!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>! ``` |
| To | ``` func CFURLCreateFileReferenceURL(_ allocator: CFAllocator!, _ url: CFURL!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFURL>! ``` |

Modified [CFURLCreateFromFileSystemRepresentation(_: CFAllocator!, _: UnsafePointer<UInt8>!, _: CFIndex, _: Bool) -> CFURL!](https://developer.apple.com/documentation/corefoundation/1543314-cfurlcreatefromfilesystemreprese)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCreateFromFileSystemRepresentation(_ allocator: CFAllocator!, _ buffer: UnsafePointer<UInt8>, _ bufLen: CFIndex, _ isDirectory: Bool) -> CFURL! ``` |
| To | ``` func CFURLCreateFromFileSystemRepresentation(_ allocator: CFAllocator!, _ buffer: UnsafePointer<UInt8>!, _ bufLen: CFIndex, _ isDirectory: Bool) -> CFURL! ``` |

Modified [CFURLCreateFromFileSystemRepresentationRelativeToBase(_: CFAllocator!, _: UnsafePointer<UInt8>!, _: CFIndex, _: Bool, _: CFURL!) -> CFURL!](https://developer.apple.com/documentation/corefoundation/1542053-cfurlcreatefromfilesystemreprese)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCreateFromFileSystemRepresentationRelativeToBase(_ allocator: CFAllocator!, _ buffer: UnsafePointer<UInt8>, _ bufLen: CFIndex, _ isDirectory: Bool, _ baseURL: CFURL!) -> CFURL! ``` |
| To | ``` func CFURLCreateFromFileSystemRepresentationRelativeToBase(_ allocator: CFAllocator!, _ buffer: UnsafePointer<UInt8>!, _ bufLen: CFIndex, _ isDirectory: Bool, _ baseURL: CFURL!) -> CFURL! ``` |

Modified [CFURLCreateResourcePropertyForKeyFromBookmarkData(_: CFAllocator!, _: CFString!, _: CFData!) -> Unmanaged<CFTypeRef>!](https://developer.apple.com/documentation/corefoundation/1543031-cfurlcreateresourcepropertyforke)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCreateResourcePropertyForKeyFromBookmarkData(_ allocator: CFAllocator!, _ resourcePropertyKey: CFString!, _ bookmark: CFData!) -> Unmanaged<AnyObject>! ``` |
| To | ``` func CFURLCreateResourcePropertyForKeyFromBookmarkData(_ allocator: CFAllocator!, _ resourcePropertyKey: CFString!, _ bookmark: CFData!) -> Unmanaged<CFTypeRef>! ``` |

Modified [CFURLCreateWithBytes(_: CFAllocator!, _: UnsafePointer<UInt8>!, _: CFIndex, _: CFStringEncoding, _: CFURL!) -> CFURL!](https://developer.apple.com/documentation/corefoundation/1542075-cfurlcreatewithbytes)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCreateWithBytes(_ allocator: CFAllocator!, _ URLBytes: UnsafePointer<UInt8>, _ length: CFIndex, _ encoding: CFStringEncoding, _ baseURL: CFURL!) -> CFURL! ``` |
| To | ``` func CFURLCreateWithBytes(_ allocator: CFAllocator!, _ URLBytes: UnsafePointer<UInt8>!, _ length: CFIndex, _ encoding: CFStringEncoding, _ baseURL: CFURL!) -> CFURL! ``` |

Modified [CFURLEnumeratorGetNextURL(_: CFURLEnumerator!, _: UnsafeMutablePointer<Unmanaged<CFURL>?>!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFURLEnumeratorResult](https://developer.apple.com/documentation/corefoundation/1542747-cfurlenumeratorgetnexturl)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLEnumeratorGetNextURL(_ enumerator: CFURLEnumerator!, _ url: UnsafeMutablePointer<Unmanaged<CFURL>?>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFURLEnumeratorResult ``` |
| To | ``` func CFURLEnumeratorGetNextURL(_ enumerator: CFURLEnumerator!, _ url: UnsafeMutablePointer<Unmanaged<CFURL>?>!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFURLEnumeratorResult ``` |

Modified [CFURLGetByteRangeForComponent(_: CFURL!, _: CFURLComponentType, _: UnsafeMutablePointer<CFRange>!) -> CFRange](https://developer.apple.com/documentation/corefoundation/1543146-cfurlgetbyterangeforcomponent)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLGetByteRangeForComponent(_ url: CFURL!, _ component: CFURLComponentType, _ rangeIncludingSeparators: UnsafeMutablePointer<CFRange>) -> CFRange ``` |
| To | ``` func CFURLGetByteRangeForComponent(_ url: CFURL!, _ component: CFURLComponentType, _ rangeIncludingSeparators: UnsafeMutablePointer<CFRange>!) -> CFRange ``` |

Modified [CFURLGetBytes(_: CFURL!, _: UnsafeMutablePointer<UInt8>!, _: CFIndex) -> CFIndex](https://developer.apple.com/documentation/corefoundation/1541551-cfurlgetbytes)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLGetBytes(_ url: CFURL!, _ buffer: UnsafeMutablePointer<UInt8>, _ bufferLength: CFIndex) -> CFIndex ``` |
| To | ``` func CFURLGetBytes(_ url: CFURL!, _ buffer: UnsafeMutablePointer<UInt8>!, _ bufferLength: CFIndex) -> CFIndex ``` |

Modified [CFURLGetFileSystemRepresentation(_: CFURL!, _: Bool, _: UnsafeMutablePointer<UInt8>!, _: CFIndex) -> Bool](https://developer.apple.com/documentation/corefoundation/1541515-cfurlgetfilesystemrepresentation)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLGetFileSystemRepresentation(_ url: CFURL!, _ resolveAgainstBase: Bool, _ buffer: UnsafeMutablePointer<UInt8>, _ maxBufLen: CFIndex) -> Bool ``` |
| To | ``` func CFURLGetFileSystemRepresentation(_ url: CFURL!, _ resolveAgainstBase: Bool, _ buffer: UnsafeMutablePointer<UInt8>!, _ maxBufLen: CFIndex) -> Bool ``` |

Modified [CFURLResourceIsReachable(_: CFURL!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1543666-cfurlresourceisreachable)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLResourceIsReachable(_ url: CFURL!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func CFURLResourceIsReachable(_ url: CFURL!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [CFURLSetResourcePropertiesForKeys(_: CFURL!, _: CFDictionary!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1542947-cfurlsetresourcepropertiesforkey)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLSetResourcePropertiesForKeys(_ url: CFURL!, _ keyedPropertyValues: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func CFURLSetResourcePropertiesForKeys(_ url: CFURL!, _ keyedPropertyValues: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [CFURLSetResourcePropertyForKey(_: CFURL!, _: CFString!, _: CFTypeRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1541607-cfurlsetresourcepropertyforkey)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLSetResourcePropertyForKey(_ url: CFURL!, _ key: CFString!, _ propertyValue: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func CFURLSetResourcePropertyForKey(_ url: CFURL!, _ key: CFString!, _ propertyValue: CFTypeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [CFURLSetTemporaryResourcePropertyForKey(_: CFURL!, _: CFString!, _: CFTypeRef!)](https://developer.apple.com/documentation/corefoundation/1542384-cfurlsettemporaryresourcepropert)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLSetTemporaryResourcePropertyForKey(_ url: CFURL!, _ key: CFString!, _ propertyValue: AnyObject!) ``` |
| To | ``` func CFURLSetTemporaryResourcePropertyForKey(_ url: CFURL!, _ key: CFString!, _ propertyValue: CFTypeRef!) ``` |

Modified [CFURLWriteBookmarkDataToFile(_: CFData!, _: CFURL!, _: CFURLBookmarkFileCreationOptions, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1541737-cfurlwritebookmarkdatatofile)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLWriteBookmarkDataToFile(_ bookmarkRef: CFData!, _ fileURL: CFURL!, _ options: CFURLBookmarkFileCreationOptions, _ errorRef: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func CFURLWriteBookmarkDataToFile(_ bookmarkRef: CFData!, _ fileURL: CFURL!, _ options: CFURLBookmarkFileCreationOptions, _ errorRef: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [CFWriteStreamClientCallBack](https://developer.apple.com/documentation/corefoundation/cfwritestreamclientcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFWriteStreamClientCallBack = (CFWriteStream!, CFStreamEventType, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CFWriteStreamClientCallBack = (CFWriteStream?, CFStreamEventType, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CFWriteStreamCopyDispatchQueue(_: CFWriteStream!) -> DispatchQueue!](https://developer.apple.com/documentation/corefoundation/1539741-cfwritestreamcopydispatchqueue)

|  | Declaration |
| --- | --- |
| From | ``` func CFWriteStreamCopyDispatchQueue(_ stream: CFWriteStream!) -> dispatch_queue_t! ``` |
| To | ``` func CFWriteStreamCopyDispatchQueue(_ stream: CFWriteStream!) -> DispatchQueue! ``` |

Modified [CFWriteStreamCopyProperty(_: CFWriteStream!, _: CFStreamPropertyKey!) -> CFTypeRef!](https://developer.apple.com/documentation/corefoundation/1539717-cfwritestreamcopyproperty)

|  | Declaration |
| --- | --- |
| From | ``` func CFWriteStreamCopyProperty(_ stream: CFWriteStream!, _ propertyName: CFString!) -> AnyObject! ``` |
| To | ``` func CFWriteStreamCopyProperty(_ stream: CFWriteStream!, _ propertyName: CFStreamPropertyKey!) -> CFTypeRef! ``` |

Modified [CFWriteStreamCreateWithBuffer(_: CFAllocator!, _: UnsafeMutablePointer<UInt8>!, _: CFIndex) -> CFWriteStream!](https://developer.apple.com/documentation/corefoundation/1539650-cfwritestreamcreatewithbuffer)

|  | Declaration |
| --- | --- |
| From | ``` func CFWriteStreamCreateWithBuffer(_ alloc: CFAllocator!, _ buffer: UnsafeMutablePointer<UInt8>, _ bufferCapacity: CFIndex) -> CFWriteStream! ``` |
| To | ``` func CFWriteStreamCreateWithBuffer(_ alloc: CFAllocator!, _ buffer: UnsafeMutablePointer<UInt8>!, _ bufferCapacity: CFIndex) -> CFWriteStream! ``` |

Modified [CFWriteStreamScheduleWithRunLoop(_: CFWriteStream!, _: CFRunLoop!, _: CFRunLoopMode!)](https://developer.apple.com/documentation/corefoundation/1539621-cfwritestreamschedulewithrunloop)

|  | Declaration |
| --- | --- |
| From | ``` func CFWriteStreamScheduleWithRunLoop(_ stream: CFWriteStream!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) ``` |
| To | ``` func CFWriteStreamScheduleWithRunLoop(_ stream: CFWriteStream!, _ runLoop: CFRunLoop!, _ runLoopMode: CFRunLoopMode!) ``` |

Modified [CFWriteStreamSetClient(_: CFWriteStream!, _: CFOptionFlags, _: CoreFoundation.CFWriteStreamClientCallBack!, _: UnsafeMutablePointer<CFStreamClientContext>!) -> Bool](https://developer.apple.com/documentation/corefoundation/1539678-cfwritestreamsetclient)

|  | Declaration |
| --- | --- |
| From | ``` func CFWriteStreamSetClient(_ stream: CFWriteStream!, _ streamEvents: CFOptionFlags, _ clientCB: CFWriteStreamClientCallBack!, _ clientContext: UnsafeMutablePointer<CFStreamClientContext>) -> Bool ``` |
| To | ``` func CFWriteStreamSetClient(_ stream: CFWriteStream!, _ streamEvents: CFOptionFlags, _ clientCB: CoreFoundation.CFWriteStreamClientCallBack!, _ clientContext: UnsafeMutablePointer<CFStreamClientContext>!) -> Bool ``` |

Modified [CFWriteStreamSetDispatchQueue(_: CFWriteStream!, _: DispatchQueue!)](https://developer.apple.com/documentation/corefoundation/1539656-cfwritestreamsetdispatchqueue)

|  | Declaration |
| --- | --- |
| From | ``` func CFWriteStreamSetDispatchQueue(_ stream: CFWriteStream!, _ q: dispatch_queue_t!) ``` |
| To | ``` func CFWriteStreamSetDispatchQueue(_ stream: CFWriteStream!, _ q: DispatchQueue!) ``` |

Modified [CFWriteStreamSetProperty(_: CFWriteStream!, _: CFStreamPropertyKey!, _: CFTypeRef!) -> Bool](https://developer.apple.com/documentation/corefoundation/1539609-cfwritestreamsetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func CFWriteStreamSetProperty(_ stream: CFWriteStream!, _ propertyName: CFString!, _ propertyValue: AnyObject!) -> Bool ``` |
| To | ``` func CFWriteStreamSetProperty(_ stream: CFWriteStream!, _ propertyName: CFStreamPropertyKey!, _ propertyValue: CFTypeRef!) -> Bool ``` |

Modified [CFWriteStreamUnscheduleFromRunLoop(_: CFWriteStream!, _: CFRunLoop!, _: CFRunLoopMode!)](https://developer.apple.com/documentation/corefoundation/1539749-cfwritestreamunschedulefromrunlo)

|  | Declaration |
| --- | --- |
| From | ``` func CFWriteStreamUnscheduleFromRunLoop(_ stream: CFWriteStream!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) ``` |
| To | ``` func CFWriteStreamUnscheduleFromRunLoop(_ stream: CFWriteStream!, _ runLoop: CFRunLoop!, _ runLoopMode: CFRunLoopMode!) ``` |

Modified [CFWriteStreamWrite(_: CFWriteStream!, _: UnsafePointer<UInt8>!, _: CFIndex) -> CFIndex](https://developer.apple.com/documentation/corefoundation/1539680-cfwritestreamwrite)

|  | Declaration |
| --- | --- |
| From | ``` func CFWriteStreamWrite(_ stream: CFWriteStream!, _ buffer: UnsafePointer<UInt8>, _ bufferLength: CFIndex) -> CFIndex ``` |
| To | ``` func CFWriteStreamWrite(_ stream: CFWriteStream!, _ buffer: UnsafePointer<UInt8>!, _ bufferLength: CFIndex) -> CFIndex ``` |

Modified [kCFErrorDomainCocoa](https://developer.apple.com/documentation/corefoundation/kcferrordomaincocoa)

|  | Declaration |
| --- | --- |
| From | ``` let kCFErrorDomainCocoa: CFString! ``` |
| To | ``` let kCFErrorDomainCocoa: CFErrorDomain! ``` |

Modified [kCFErrorDomainMach](https://developer.apple.com/documentation/corefoundation/kcferrordomainmach)

|  | Declaration |
| --- | --- |
| From | ``` let kCFErrorDomainMach: CFString! ``` |
| To | ``` let kCFErrorDomainMach: CFErrorDomain! ``` |

Modified [kCFErrorDomainOSStatus](https://developer.apple.com/documentation/corefoundation/kcferrordomainosstatus)

|  | Declaration |
| --- | --- |
| From | ``` let kCFErrorDomainOSStatus: CFString! ``` |
| To | ``` let kCFErrorDomainOSStatus: CFErrorDomain! ``` |

Modified [kCFErrorDomainPOSIX](https://developer.apple.com/documentation/corefoundation/kcferrordomainposix)

|  | Declaration |
| --- | --- |
| From | ``` let kCFErrorDomainPOSIX: CFString! ``` |
| To | ``` let kCFErrorDomainPOSIX: CFErrorDomain! ``` |

Modified [kCFPreferencesAnyApplication](https://developer.apple.com/documentation/corefoundation/kcfpreferencesanyapplication)

|  | Declaration |
| --- | --- |
| From | ``` let kCFPreferencesAnyApplication: CFString! ``` |
| To | ``` let kCFPreferencesAnyApplication: CFString ``` |

Modified [kCFPreferencesAnyHost](https://developer.apple.com/documentation/corefoundation/kcfpreferencesanyhost)

|  | Declaration |
| --- | --- |
| From | ``` let kCFPreferencesAnyHost: CFString! ``` |
| To | ``` let kCFPreferencesAnyHost: CFString ``` |

Modified [kCFPreferencesAnyUser](https://developer.apple.com/documentation/corefoundation/kcfpreferencesanyuser)

|  | Declaration |
| --- | --- |
| From | ``` let kCFPreferencesAnyUser: CFString! ``` |
| To | ``` let kCFPreferencesAnyUser: CFString ``` |

Modified [kCFPreferencesCurrentApplication](https://developer.apple.com/documentation/corefoundation/kcfpreferencescurrentapplication)

|  | Declaration |
| --- | --- |
| From | ``` let kCFPreferencesCurrentApplication: CFString! ``` |
| To | ``` let kCFPreferencesCurrentApplication: CFString ``` |

Modified [kCFPreferencesCurrentHost](https://developer.apple.com/documentation/corefoundation/kcfpreferencescurrenthost)

|  | Declaration |
| --- | --- |
| From | ``` let kCFPreferencesCurrentHost: CFString! ``` |
| To | ``` let kCFPreferencesCurrentHost: CFString ``` |

Modified [kCFPreferencesCurrentUser](https://developer.apple.com/documentation/corefoundation/kcfpreferencescurrentuser)

|  | Declaration |
| --- | --- |
| From | ``` let kCFPreferencesCurrentUser: CFString! ``` |
| To | ``` let kCFPreferencesCurrentUser: CFString ``` |

Modified [kCFURLCustomIconKey](https://developer.apple.com/documentation/corefoundation/kcfurlcustomiconkey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 10.0 |

Modified [kCFURLEffectiveIconKey](https://developer.apple.com/documentation/corefoundation/kcfurleffectiveiconkey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 10.0 |

Modified [kCFURLLabelColorKey](https://developer.apple.com/documentation/corefoundation/kcfurllabelcolorkey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 10.0 |

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
