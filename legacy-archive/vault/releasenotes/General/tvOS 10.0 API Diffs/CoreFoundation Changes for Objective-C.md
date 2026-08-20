---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Objective-C/CoreFoundation.html
archived_at: '2026-07-18T02:57:25.434040Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# CoreFoundation Changes for Objective-C

### CoreFoundation

#### CFAvailability.h

Added #def CF_EXTENSIBLE_STRING_ENUMAdded #def CF_STRING_ENUM

#### CFBase.h

Added #def CF_NO_TAIL_CALLAdded #def CF_NOESCAPEAdded [#def kCFCoreFoundationVersionNumber10_10_4](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_10_4)Added [#def kCFCoreFoundationVersionNumber10_10_5](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_10_5)Added [#def kCFCoreFoundationVersionNumber10_10_Max](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_10_max)Added [#def kCFCoreFoundationVersionNumber10_11](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_11)Added [#def kCFCoreFoundationVersionNumber10_11_1](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_11_1)Added [#def kCFCoreFoundationVersionNumber10_11_2](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_11_2)Added [#def kCFCoreFoundationVersionNumber10_11_3](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_11_3)Added [#def kCFCoreFoundationVersionNumber10_11_4](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_11_4)Added [#def kCFCoreFoundationVersionNumber10_11_Max](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_11_max)Added [#def kCFCoreFoundationVersionNumber_iOS_8_x_Max](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber_ios_8_x_max)Added [#def kCFCoreFoundationVersionNumber_iOS_9_0](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber_ios_9_0)Added [#def kCFCoreFoundationVersionNumber_iOS_9_1](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber_ios_9_1)Added [#def kCFCoreFoundationVersionNumber_iOS_9_2](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber_ios_9_2)Added [#def kCFCoreFoundationVersionNumber_iOS_9_3](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber_ios_9_3)Added [#def kCFCoreFoundationVersionNumber_iOS_9_4](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber_ios_9_4)Added [#def kCFCoreFoundationVersionNumber_iOS_9_x_Max](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber_ios_9_x_max)

#### CFCalendar.h

Modified [CFCalendarCreateWithIdentifier()](https://developer.apple.com/documentation/corefoundation/1533511-cfcalendarcreatewithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` CFCalendarRef CFCalendarCreateWithIdentifier (     CFAllocatorRef allocator,     CFStringRef identifier ); ``` |
| To | ``` CFCalendarRef CFCalendarCreateWithIdentifier (     CFAllocatorRef allocator,     CFCalendarIdentifier identifier ); ``` |

Modified [CFCalendarGetIdentifier()](https://developer.apple.com/documentation/corefoundation/1533495-cfcalendargetidentifier)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CFCalendarGetIdentifier (     CFCalendarRef calendar ); ``` |
| To | ``` CFCalendarIdentifier CFCalendarGetIdentifier (     CFCalendarRef calendar ); ``` |

#### CFDateFormatter.h

Added [CFDateFormatterCreateISO8601Formatter()](https://developer.apple.com/documentation/corefoundation/1643402-cfdateformattercreateiso8601form)Added [CFDateFormatterKey](https://developer.apple.com/documentation/corefoundation/cfdateformatterkey)Added [CFISO8601DateFormatOptions](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions)Added [kCFISO8601DateFormatWithColonSeparatorInTime](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/1643398-withcolonseparatorintime)Added [kCFISO8601DateFormatWithColonSeparatorInTimeZone](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/1643367-withcolonseparatorintimezone)Added [kCFISO8601DateFormatWithDashSeparatorInDate](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/kcfiso8601dateformatwithdashseparatorindate)Added [kCFISO8601DateFormatWithDay](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/kcfiso8601dateformatwithday)Added [kCFISO8601DateFormatWithFullDate](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/kcfiso8601dateformatwithfulldate)Added [kCFISO8601DateFormatWithFullTime](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/kcfiso8601dateformatwithfulltime)Added [kCFISO8601DateFormatWithInternetDateTime](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/kcfiso8601dateformatwithinternetdatetime)Added [kCFISO8601DateFormatWithMonth](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/1643353-withmonth)Added [kCFISO8601DateFormatWithSpaceBetweenDateAndTime](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/kcfiso8601dateformatwithspacebetweendateandtime)Added [kCFISO8601DateFormatWithTime](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/1643346-withtime)Added [kCFISO8601DateFormatWithTimeZone](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/kcfiso8601dateformatwithtimezone)Added [kCFISO8601DateFormatWithWeekOfYear](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/1643355-withweekofyear)Added [kCFISO8601DateFormatWithYear](https://developer.apple.com/documentation/corefoundation/cfiso8601dateformatoptions/kcfiso8601dateformatwithyear)Modified [CFDateFormatterCopyProperty()](https://developer.apple.com/documentation/corefoundation/1396296-cfdateformattercopyproperty)

|  | Declaration |
| --- | --- |
| From | ``` CFTypeRef CFDateFormatterCopyProperty (     CFDateFormatterRef formatter,     CFStringRef key ); ``` |
| To | ``` CFTypeRef CFDateFormatterCopyProperty (     CFDateFormatterRef formatter,     CFDateFormatterKey key ); ``` |

#### CFError.h

Added [CFErrorDomain](https://developer.apple.com/documentation/corefoundation/cferrordomain)Modified [CFErrorCreate()](https://developer.apple.com/documentation/corefoundation/1494643-cferrorcreate)

|  | Declaration |
| --- | --- |
| From | ``` CFErrorRef CFErrorCreate (     CFAllocatorRef allocator,     CFStringRef domain,     CFIndex code,     CFDictionaryRef userInfo ); ``` |
| To | ``` CFErrorRef CFErrorCreate (     CFAllocatorRef allocator,     CFErrorDomain domain,     CFIndex code,     CFDictionaryRef userInfo ); ``` |

Modified [CFErrorCreateWithUserInfoKeysAndValues()](https://developer.apple.com/documentation/corefoundation/1494658-cferrorcreatewithuserinfokeysand)

|  | Declaration |
| --- | --- |
| From | ``` CFErrorRef CFErrorCreateWithUserInfoKeysAndValues (     CFAllocatorRef allocator,     CFStringRef domain,     CFIndex code,     const void *const *userInfoKeys,     const void *const *userInfoValues,     CFIndex numUserInfoValues ); ``` |
| To | ``` CFErrorRef CFErrorCreateWithUserInfoKeysAndValues (     CFAllocatorRef allocator,     CFErrorDomain domain,     CFIndex code,     const void *const *userInfoKeys,     const void *const *userInfoValues,     CFIndex numUserInfoValues ); ``` |

Modified [CFErrorGetDomain()](https://developer.apple.com/documentation/corefoundation/1494657-cferrorgetdomain)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CFErrorGetDomain (     CFErrorRef err ); ``` |
| To | ``` CFErrorDomain CFErrorGetDomain (     CFErrorRef err ); ``` |

#### CFLocale.h

Added [CFCalendarIdentifier](https://developer.apple.com/documentation/corefoundation/cfcalendaridentifier)Added [CFLocaleIdentifier](https://developer.apple.com/documentation/corefoundation/cflocaleidentifier)Added [CFLocaleKey](https://developer.apple.com/documentation/corefoundation/cflocalekey)Modified [CFLocaleCopyDisplayNameForPropertyValue()](https://developer.apple.com/documentation/corefoundation/1542344-cflocalecopydisplaynameforproper)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CFLocaleCopyDisplayNameForPropertyValue (     CFLocaleRef displayLocale,     CFStringRef key,     CFStringRef value ); ``` |
| To | ``` CFStringRef CFLocaleCopyDisplayNameForPropertyValue (     CFLocaleRef displayLocale,     CFLocaleKey key,     CFStringRef value ); ``` |

Modified [CFLocaleCreate()](https://developer.apple.com/documentation/corefoundation/1542689-cflocalecreate)

|  | Declaration |
| --- | --- |
| From | ``` CFLocaleRef CFLocaleCreate (     CFAllocatorRef allocator,     CFStringRef localeIdentifier ); ``` |
| To | ``` CFLocaleRef CFLocaleCreate (     CFAllocatorRef allocator,     CFLocaleIdentifier localeIdentifier ); ``` |

Modified [CFLocaleCreateCanonicalLanguageIdentifierFromString()](https://developer.apple.com/documentation/corefoundation/1542757-cflocalecreatecanonicallanguagei)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CFLocaleCreateCanonicalLanguageIdentifierFromString (     CFAllocatorRef allocator,     CFStringRef localeIdentifier ); ``` |
| To | ``` CFLocaleIdentifier CFLocaleCreateCanonicalLanguageIdentifierFromString (     CFAllocatorRef allocator,     CFStringRef localeIdentifier ); ``` |

Modified [CFLocaleCreateCanonicalLocaleIdentifierFromScriptManagerCodes()](https://developer.apple.com/documentation/corefoundation/1543446-cflocalecreatecanonicallocaleide)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CFLocaleCreateCanonicalLocaleIdentifierFromScriptManagerCodes (     CFAllocatorRef allocator,     LangCode lcode,     RegionCode rcode ); ``` |
| To | ``` CFLocaleIdentifier CFLocaleCreateCanonicalLocaleIdentifierFromScriptManagerCodes (     CFAllocatorRef allocator,     LangCode lcode,     RegionCode rcode ); ``` |

Modified [CFLocaleCreateCanonicalLocaleIdentifierFromString()](https://developer.apple.com/documentation/corefoundation/1542725-cflocalecreatecanonicallocaleide)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CFLocaleCreateCanonicalLocaleIdentifierFromString (     CFAllocatorRef allocator,     CFStringRef localeIdentifier ); ``` |
| To | ``` CFLocaleIdentifier CFLocaleCreateCanonicalLocaleIdentifierFromString (     CFAllocatorRef allocator,     CFStringRef localeIdentifier ); ``` |

Modified [CFLocaleCreateComponentsFromLocaleIdentifier()](https://developer.apple.com/documentation/corefoundation/1543644-cflocalecreatecomponentsfromloca)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CFLocaleCreateComponentsFromLocaleIdentifier (     CFAllocatorRef allocator,     CFStringRef localeID ); ``` |
| To | ``` CFDictionaryRef CFLocaleCreateComponentsFromLocaleIdentifier (     CFAllocatorRef allocator,     CFLocaleIdentifier localeID ); ``` |

Modified [CFLocaleCreateLocaleIdentifierFromComponents()](https://developer.apple.com/documentation/corefoundation/1541724-cflocalecreatelocaleidentifierfr)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CFLocaleCreateLocaleIdentifierFromComponents (     CFAllocatorRef allocator,     CFDictionaryRef dictionary ); ``` |
| To | ``` CFLocaleIdentifier CFLocaleCreateLocaleIdentifierFromComponents (     CFAllocatorRef allocator,     CFDictionaryRef dictionary ); ``` |

Modified [CFLocaleCreateLocaleIdentifierFromWindowsLocaleCode()](https://developer.apple.com/documentation/corefoundation/1541772-cflocalecreatelocaleidentifierfr)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CFLocaleCreateLocaleIdentifierFromWindowsLocaleCode (     CFAllocatorRef allocator,     uint32_t lcid ); ``` |
| To | ``` CFLocaleIdentifier CFLocaleCreateLocaleIdentifierFromWindowsLocaleCode (     CFAllocatorRef allocator,     uint32_t lcid ); ``` |

Modified [CFLocaleGetIdentifier()](https://developer.apple.com/documentation/corefoundation/1543634-cflocalegetidentifier)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CFLocaleGetIdentifier (     CFLocaleRef locale ); ``` |
| To | ``` CFLocaleIdentifier CFLocaleGetIdentifier (     CFLocaleRef locale ); ``` |

Modified [CFLocaleGetValue()](https://developer.apple.com/documentation/corefoundation/1543547-cflocalegetvalue)

|  | Declaration |
| --- | --- |
| From | ``` CFTypeRef CFLocaleGetValue (     CFLocaleRef locale,     CFStringRef key ); ``` |
| To | ``` CFTypeRef CFLocaleGetValue (     CFLocaleRef locale,     CFLocaleKey key ); ``` |

Modified [CFLocaleGetWindowsLocaleCodeFromLocaleIdentifier()](https://developer.apple.com/documentation/corefoundation/1542147-cflocalegetwindowslocalecodefrom)

|  | Declaration |
| --- | --- |
| From | ``` uint32_t CFLocaleGetWindowsLocaleCodeFromLocaleIdentifier (     CFStringRef localeIdentifier ); ``` |
| To | ``` uint32_t CFLocaleGetWindowsLocaleCodeFromLocaleIdentifier (     CFLocaleIdentifier localeIdentifier ); ``` |

#### CFNotificationCenter.h

Added [CFNotificationName](https://developer.apple.com/documentation/corefoundation/cfnotificationname)Modified [CFNotificationCenterPostNotification()](https://developer.apple.com/documentation/corefoundation/1542592-cfnotificationcenterpostnotifica)

|  | Declaration |
| --- | --- |
| From | ``` void CFNotificationCenterPostNotification (     CFNotificationCenterRef center,     CFStringRef name,     const void *object,     CFDictionaryRef userInfo,     Boolean deliverImmediately ); ``` |
| To | ``` void CFNotificationCenterPostNotification (     CFNotificationCenterRef center,     CFNotificationName name,     const void *object,     CFDictionaryRef userInfo,     Boolean deliverImmediately ); ``` |

Modified [CFNotificationCenterPostNotificationWithOptions()](https://developer.apple.com/documentation/corefoundation/1541969-cfnotificationcenterpostnotifica)

|  | Declaration |
| --- | --- |
| From | ``` void CFNotificationCenterPostNotificationWithOptions (     CFNotificationCenterRef center,     CFStringRef name,     const void *object,     CFDictionaryRef userInfo,     CFOptionFlags options ); ``` |
| To | ``` void CFNotificationCenterPostNotificationWithOptions (     CFNotificationCenterRef center,     CFNotificationName name,     const void *object,     CFDictionaryRef userInfo,     CFOptionFlags options ); ``` |

Modified [CFNotificationCenterRemoveObserver()](https://developer.apple.com/documentation/corefoundation/1542672-cfnotificationcenterremoveobserv)

|  | Declaration |
| --- | --- |
| From | ``` void CFNotificationCenterRemoveObserver (     CFNotificationCenterRef center,     const void *observer,     CFStringRef name,     const void *object ); ``` |
| To | ``` void CFNotificationCenterRemoveObserver (     CFNotificationCenterRef center,     const void *observer,     CFNotificationName name,     const void *object ); ``` |

#### CFNumberFormatter.h

Added [CFNumberFormatterKey](https://developer.apple.com/documentation/corefoundation/cfnumberformatterkey)Modified [CFNumberFormatterCopyProperty()](https://developer.apple.com/documentation/corefoundation/1390801-cfnumberformattercopyproperty)

|  | Declaration |
| --- | --- |
| From | ``` CFTypeRef CFNumberFormatterCopyProperty (     CFNumberFormatterRef formatter,     CFStringRef key ); ``` |
| To | ``` CFTypeRef CFNumberFormatterCopyProperty (     CFNumberFormatterRef formatter,     CFNumberFormatterKey key ); ``` |

Modified [CFNumberFormatterSetProperty()](https://developer.apple.com/documentation/corefoundation/1390800-cfnumberformattersetproperty)

|  | Declaration |
| --- | --- |
| From | ``` void CFNumberFormatterSetProperty (     CFNumberFormatterRef formatter,     CFStringRef key,     CFTypeRef value ); ``` |
| To | ``` void CFNumberFormatterSetProperty (     CFNumberFormatterRef formatter,     CFNumberFormatterKey key,     CFTypeRef value ); ``` |

#### CFRunLoop.h

Added [CFRunLoopMode](https://developer.apple.com/documentation/corefoundation/cfrunloopmode)Modified [CFRunLoopAddCommonMode()](https://developer.apple.com/documentation/corefoundation/1542137-cfrunloopaddcommonmode)

|  | Declaration |
| --- | --- |
| From | ``` void CFRunLoopAddCommonMode (     CFRunLoopRef rl,     CFStringRef mode ); ``` |
| To | ``` void CFRunLoopAddCommonMode (     CFRunLoopRef rl,     CFRunLoopMode mode ); ``` |

Modified [CFRunLoopAddObserver()](https://developer.apple.com/documentation/corefoundation/1542504-cfrunloopaddobserver)

|  | Declaration |
| --- | --- |
| From | ``` void CFRunLoopAddObserver (     CFRunLoopRef rl,     CFRunLoopObserverRef observer,     CFStringRef mode ); ``` |
| To | ``` void CFRunLoopAddObserver (     CFRunLoopRef rl,     CFRunLoopObserverRef observer,     CFRunLoopMode mode ); ``` |

Modified [CFRunLoopAddSource()](https://developer.apple.com/documentation/corefoundation/1543356-cfrunloopaddsource)

|  | Declaration |
| --- | --- |
| From | ``` void CFRunLoopAddSource (     CFRunLoopRef rl,     CFRunLoopSourceRef source,     CFStringRef mode ); ``` |
| To | ``` void CFRunLoopAddSource (     CFRunLoopRef rl,     CFRunLoopSourceRef source,     CFRunLoopMode mode ); ``` |

Modified [CFRunLoopAddTimer()](https://developer.apple.com/documentation/corefoundation/1542132-cfrunloopaddtimer)

|  | Declaration |
| --- | --- |
| From | ``` void CFRunLoopAddTimer (     CFRunLoopRef rl,     CFRunLoopTimerRef timer,     CFStringRef mode ); ``` |
| To | ``` void CFRunLoopAddTimer (     CFRunLoopRef rl,     CFRunLoopTimerRef timer,     CFRunLoopMode mode ); ``` |

Modified [CFRunLoopContainsObserver()](https://developer.apple.com/documentation/corefoundation/1542815-cfrunloopcontainsobserver)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFRunLoopContainsObserver (     CFRunLoopRef rl,     CFRunLoopObserverRef observer,     CFStringRef mode ); ``` |
| To | ``` Boolean CFRunLoopContainsObserver (     CFRunLoopRef rl,     CFRunLoopObserverRef observer,     CFRunLoopMode mode ); ``` |

Modified [CFRunLoopContainsSource()](https://developer.apple.com/documentation/corefoundation/1542250-cfrunloopcontainssource)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFRunLoopContainsSource (     CFRunLoopRef rl,     CFRunLoopSourceRef source,     CFStringRef mode ); ``` |
| To | ``` Boolean CFRunLoopContainsSource (     CFRunLoopRef rl,     CFRunLoopSourceRef source,     CFRunLoopMode mode ); ``` |

Modified [CFRunLoopContainsTimer()](https://developer.apple.com/documentation/corefoundation/1543011-cfrunloopcontainstimer)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFRunLoopContainsTimer (     CFRunLoopRef rl,     CFRunLoopTimerRef timer,     CFStringRef mode ); ``` |
| To | ``` Boolean CFRunLoopContainsTimer (     CFRunLoopRef rl,     CFRunLoopTimerRef timer,     CFRunLoopMode mode ); ``` |

Modified [CFRunLoopCopyCurrentMode()](https://developer.apple.com/documentation/corefoundation/1541775-cfrunloopcopycurrentmode)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CFRunLoopCopyCurrentMode (     CFRunLoopRef rl ); ``` |
| To | ``` CFRunLoopMode CFRunLoopCopyCurrentMode (     CFRunLoopRef rl ); ``` |

Modified [CFRunLoopGetNextTimerFireDate()](https://developer.apple.com/documentation/corefoundation/1542092-cfrunloopgetnexttimerfiredate)

|  | Declaration |
| --- | --- |
| From | ``` CFAbsoluteTime CFRunLoopGetNextTimerFireDate (     CFRunLoopRef rl,     CFStringRef mode ); ``` |
| To | ``` CFAbsoluteTime CFRunLoopGetNextTimerFireDate (     CFRunLoopRef rl,     CFRunLoopMode mode ); ``` |

Modified [CFRunLoopRemoveObserver()](https://developer.apple.com/documentation/corefoundation/1542818-cfrunloopremoveobserver)

|  | Declaration |
| --- | --- |
| From | ``` void CFRunLoopRemoveObserver (     CFRunLoopRef rl,     CFRunLoopObserverRef observer,     CFStringRef mode ); ``` |
| To | ``` void CFRunLoopRemoveObserver (     CFRunLoopRef rl,     CFRunLoopObserverRef observer,     CFRunLoopMode mode ); ``` |

Modified [CFRunLoopRemoveSource()](https://developer.apple.com/documentation/corefoundation/1542145-cfrunloopremovesource)

|  | Declaration |
| --- | --- |
| From | ``` void CFRunLoopRemoveSource (     CFRunLoopRef rl,     CFRunLoopSourceRef source,     CFStringRef mode ); ``` |
| To | ``` void CFRunLoopRemoveSource (     CFRunLoopRef rl,     CFRunLoopSourceRef source,     CFRunLoopMode mode ); ``` |

Modified [CFRunLoopRemoveTimer()](https://developer.apple.com/documentation/corefoundation/1541992-cfrunloopremovetimer)

|  | Declaration |
| --- | --- |
| From | ``` void CFRunLoopRemoveTimer (     CFRunLoopRef rl,     CFRunLoopTimerRef timer,     CFStringRef mode ); ``` |
| To | ``` void CFRunLoopRemoveTimer (     CFRunLoopRef rl,     CFRunLoopTimerRef timer,     CFRunLoopMode mode ); ``` |

Modified [CFRunLoopRunInMode()](https://developer.apple.com/documentation/corefoundation/1541988-cfrunloopruninmode)

|  | Declaration |
| --- | --- |
| From | ``` CFRunLoopRunResult CFRunLoopRunInMode (     CFStringRef mode,     CFTimeInterval seconds,     Boolean returnAfterSourceHandled ); ``` |
| To | ``` CFRunLoopRunResult CFRunLoopRunInMode (     CFRunLoopMode mode,     CFTimeInterval seconds,     Boolean returnAfterSourceHandled ); ``` |

#### CFStream.h

Added [CFStreamPropertyKey](https://developer.apple.com/documentation/corefoundation/cfstreampropertykey)Modified [CFReadStreamCopyProperty()](https://developer.apple.com/documentation/corefoundation/1539715-cfreadstreamcopyproperty)

|  | Declaration |
| --- | --- |
| From | ``` CFTypeRef CFReadStreamCopyProperty (     CFReadStreamRef stream,     CFStringRef propertyName ); ``` |
| To | ``` CFTypeRef CFReadStreamCopyProperty (     CFReadStreamRef stream,     CFStreamPropertyKey propertyName ); ``` |

Modified [CFReadStreamScheduleWithRunLoop()](https://developer.apple.com/documentation/corefoundation/1539611-cfreadstreamschedulewithrunloop)

|  | Declaration |
| --- | --- |
| From | ``` void CFReadStreamScheduleWithRunLoop (     CFReadStreamRef stream,     CFRunLoopRef runLoop,     CFStringRef runLoopMode ); ``` |
| To | ``` void CFReadStreamScheduleWithRunLoop (     CFReadStreamRef stream,     CFRunLoopRef runLoop,     CFRunLoopMode runLoopMode ); ``` |

Modified [CFReadStreamSetProperty()](https://developer.apple.com/documentation/corefoundation/1539615-cfreadstreamsetproperty)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFReadStreamSetProperty (     CFReadStreamRef stream,     CFStringRef propertyName,     CFTypeRef propertyValue ); ``` |
| To | ``` Boolean CFReadStreamSetProperty (     CFReadStreamRef stream,     CFStreamPropertyKey propertyName,     CFTypeRef propertyValue ); ``` |

Modified [CFReadStreamUnscheduleFromRunLoop()](https://developer.apple.com/documentation/corefoundation/1539674-cfreadstreamunschedulefromrunloo)

|  | Declaration |
| --- | --- |
| From | ``` void CFReadStreamUnscheduleFromRunLoop (     CFReadStreamRef stream,     CFRunLoopRef runLoop,     CFStringRef runLoopMode ); ``` |
| To | ``` void CFReadStreamUnscheduleFromRunLoop (     CFReadStreamRef stream,     CFRunLoopRef runLoop,     CFRunLoopMode runLoopMode ); ``` |

Modified [CFWriteStreamCopyProperty()](https://developer.apple.com/documentation/corefoundation/1539717-cfwritestreamcopyproperty)

|  | Declaration |
| --- | --- |
| From | ``` CFTypeRef CFWriteStreamCopyProperty (     CFWriteStreamRef stream,     CFStringRef propertyName ); ``` |
| To | ``` CFTypeRef CFWriteStreamCopyProperty (     CFWriteStreamRef stream,     CFStreamPropertyKey propertyName ); ``` |

Modified [CFWriteStreamScheduleWithRunLoop()](https://developer.apple.com/documentation/corefoundation/1539621-cfwritestreamschedulewithrunloop)

|  | Declaration |
| --- | --- |
| From | ``` void CFWriteStreamScheduleWithRunLoop (     CFWriteStreamRef stream,     CFRunLoopRef runLoop,     CFStringRef runLoopMode ); ``` |
| To | ``` void CFWriteStreamScheduleWithRunLoop (     CFWriteStreamRef stream,     CFRunLoopRef runLoop,     CFRunLoopMode runLoopMode ); ``` |

Modified [CFWriteStreamSetProperty()](https://developer.apple.com/documentation/corefoundation/1539609-cfwritestreamsetproperty)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFWriteStreamSetProperty (     CFWriteStreamRef stream,     CFStringRef propertyName,     CFTypeRef propertyValue ); ``` |
| To | ``` Boolean CFWriteStreamSetProperty (     CFWriteStreamRef stream,     CFStreamPropertyKey propertyName,     CFTypeRef propertyValue ); ``` |

Modified [CFWriteStreamUnscheduleFromRunLoop()](https://developer.apple.com/documentation/corefoundation/1539749-cfwritestreamunschedulefromrunlo)

|  | Declaration |
| --- | --- |
| From | ``` void CFWriteStreamUnscheduleFromRunLoop (     CFWriteStreamRef stream,     CFRunLoopRef runLoop,     CFStringRef runLoopMode ); ``` |
| To | ``` void CFWriteStreamUnscheduleFromRunLoop (     CFWriteStreamRef stream,     CFRunLoopRef runLoop,     CFRunLoopMode runLoopMode ); ``` |

#### CFURL.h

Added [kCFURLCanonicalPathKey](https://developer.apple.com/documentation/corefoundation/kcfurlcanonicalpathkey)Added [kCFURLVolumeIsEncryptedKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeisencryptedkey)Added [kCFURLVolumeIsRootFileSystemKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeisrootfilesystemkey)Added [kCFURLVolumeSupportsCompressionKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportscompressionkey)Added [kCFURLVolumeSupportsExclusiveRenamingKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportsexclusiverenamingkey)Added [kCFURLVolumeSupportsFileCloningKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportsfilecloningkey)Added [kCFURLVolumeSupportsSwapRenamingKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportsswaprenamingkey)Modified [kCFURLCustomIconKey](https://developer.apple.com/documentation/corefoundation/kcfurlcustomiconkey)

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
