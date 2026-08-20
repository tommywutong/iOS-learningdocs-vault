---
title: Core Foundation Release Notes for iOS
apple_id: TP40011690
resource_type: Release Note
platform: watchOS|iOS
topic: null
technology: CoreFoundation
published: '2012-02-16'
source_url: https://developer.apple.com/library/archive/releasenotes/CoreFoundation/RN-CoreFoundation-iOS/CoreFoundation_iOS5.html
archived_at: '2026-07-18T02:50:22.918817Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)


iOS Release Notes Copyright © 2011 Apple Inc. All Rights Reserved.

# iOS 5 Release Notes CoreFoundation Framework

CoreFoundation (aka CF) is a framework which provides C APIs for strings, collections, user preferences, property lists, plug-ins, bundles, notifications, runloop, etc. These APIs are designed with portability, performance, and consistency in mind, and are available to Cocoa Touch applications.

CoreFoundation is accessible directly as a public framework.

---

#### CFXMLParser

CFXMLParser and CFXMLNode are deprecated. CFXMLParser has some deficiencies in terms of standards compliance and performance, and clients should migrate their uses of the CFXMLParser classes over to NSXMLParser, NSXMLDocument, or other XML parsing technologies on iOS 5.

#### CFPreferences and Threading

In earlier releases of iOS, CFPreferences (and NSUserDefaults) serialized all access; if you've been avoiding using the preferences system in heavily threaded apps due to contention, this should be greatly improved.

#### CFPreferencesAppSynchronize() and automatic synchronization

CFPreferences now uses the automatic synchronization system for the current application's domain that NSUserDefaults has always used. Additionally, automatic synchronization is now non-blocking in most cases. You should consider any calls to CFPreferencesAppSynchronize() carefully to see if they're really necessary, as you can avoid blocking IO by removing them.

#### CFPreferences euid/uid handling

Prior to iOS 5, CFPreferences (and therefore NSUserDefaults) would change the owner of the plist files it wrote to the uid/gid of the application writing to preferences. In iOS 5, for apps linked against iOS 5 or later, the file will be owned by the euid/egid instead. You can temporarily revert to the old behavior for testing purposes by setting __CFPREFERENCES_USE_OLD_UID_BEHAVIOR to a non-null value in your environment. This will primarily impact applications with privileged helper tools that write to the preferences of non-privileged apps such as the Dock or the parent process.

#### CFString Hyphenation

CFString now includes a facility for locating potential hyphenation points within a word. This is intended for the use of text layout engines such as NSTypesetter, when automatic hyphenation is enabled. Hyphenation depends heavily on the language of the text to be hyphenated, and the CFStringGetHyphenationLocationBeforeIndex() requires that this be specified as a CFLocale. Hyphenation data is available only for certain languages, currently English (US and GB), French, German, Italian, Spanish, Dutch, and Russian, although this list may be expanded in the future. A runtime determination of whether hyphenation data is available for a given language may be made using CFStringIsHyphenationAvailableForLocale().

The functions associated with the hyphenation facility are as follows:

```
CFIndex CFStringGetHyphenationLocationBeforeIndex(CFStringRef string, CFIndex location, CFRange limitRange,                                      CFOptionFlags options, CFLocaleRef locale, UTF32Char *character);
```

```
Boolean CFStringIsHyphenationAvailableForLocale(CFLocaleRef locale);
```

To use CFStringGetHyphenationLocationBeforeIndex(), a client should pass in a string containing the text intended to be hyphenated, a location before which a hyphenation point is to be found, a range limiting the portion of the text to be examined, and the locale. The return value will be an index within the string where it is appropriate to insert a hyphen, or CFNotFound if none is found that is both before the specified location and within the limiting range. There may be cases in certain languages in which a character other than the standard hyphen is used to indicate hyphenation, and the character argument is intended to return a suggested character by reference; clients may pass NULL for this argument if they are not interested in this information.

#### CFStringGetFileSystemRepresentation

CFStringGetFileSystemRepresentation() will now return false for any input string which contains embedded null characters, rather than returning a what is effectively a truncated (and outright wrong) string.

#### CFStringCapitalize

The capitalization logic is enhanced to support the digraph, "IJ", with Dutch locale.

#### CoreFoundation Unicode Database

The CoreFoundation Unicode Database is updated to version 6.0.

#### kCFCompareForcedOrdering and kCFCompareNumerically with CFStringCompareWithOptionsAndLocale()

We were not able to force ordering for differences in numeric characters when the two numeric values are equal. Also, in some cases, we were not producing ideal results (i.e. 001 < 01). We're evaluating the ordering based on the number of digits involved in the numeric value.

#### Distributed notification delivery

If you want a posted distributed notification to be received immediately, be sure you are passing the CFNotificationSuspensionBehaviorDeliverImmediately suspension behavior flag when registering for the notification, or using the kCFNotificationDeliverImmediately flag when posting. Bugs in iOS releases prior to 5.0 meant that sometimes a distributed notification would get delivered through to suspended observers, and not be properly queued, even when those flags weren't used.

#### CFCalendar

The CFCalendar algorithms have several differences depending on which OS SDK version you build your app against. CFCalendarGetRangeOfUnit() can produce materially different results for iOS 2, 3, 4/5. CFCalendarGetOrdinalityOfUnit() can produce materially different results for iOS 2/3 and iOS 4/5. CFCalendarComposeAbsoluteTime() can produce different results on iOS 5 than previous releases when working with Week units.

But of course, most of the algorithms can produce different results between OS releases, as bugs are fixed or changes made, either in Foundation or CoreFoundation or in libraries beneath them. The differences noted in the previous paragraph are the significant ones.

There are 3 new Week-related unit/component constants in CFCalendar:

```
kCFCalendarUnitWeekOfMonth, kCFCalendarUnitWeekOfYear, kCFCalendarUnitYearForWeekOfYear
```

and the values of these quantities are week numbers or amounts relating to the month or the year that the week is in, and the year number for week-based interpretations of a calendar, such as the ISO 8601 calendar.

For many operations, there is no difference in meaning between kCFCalendarUnitWeekOfMonth and kCFCalendarUnitWeekOfYear, but for some there is a difference. Obviously getting the ordinality of a week with the month will usually give a different answer than the ordinality of the week within the year. The kCFCalendarUnitWeek constant is not yet officially deprecated, but its use in new code is discouraged. It has a behavior like either kCFCalendarUnitWeekOfMonth or kCFCalendarUnitWeekOfYear, as the case may be, to give it behavior like it had prior to iOS 5.

#### CFURL

We've added lots of new resource property keys.
The functions CFURLCreateBookmarkDataFromFile() and CFURLWriteBookmarkDataToFile() have been introduced to iOS 5.0. They were previously introduced to Mac OS X 10.6.

#### CFURLEnumerator

CFURLEnumeratorGetSourceDidChange() is now deprecated.

The kCFURLEnumeratorIncludeDirectoriesPreOrder and kCFURLEnumeratorIncludeDirectoriesPostOrder options for recursive directory enumerators were added.

#### CFError

We've added the kCFErrorURLKey and kCFErrorFilePathKey userInfo dictionary keys.

#### New CFRunLoop API

There are two new functions to create CFRunLoopObservers and CFRunLoopTimers, respectively, which take a Block to execute, rather than function pointer and context arguments:

```
CFRunLoopObserverRef CFRunLoopObserverCreateWithHandler(CFAllocatorRef allocator, CFOptionFlags activities, Boolean repeats,                                CFIndex order, void (^block)(CFRunLoopObserverRef observer, CFRunLoopActivity activity))
```

```
CFRunLoopTimerRef CFRunLoopTimerCreateWithHandler(CFAllocatorRef allocator, CFAbsoluteTime fireDate, CFTimeInterval interval,                                CFOptionFlags flags, CFIndex order, void (^block)(CFRunLoopTimerRef timer))
```
