---
title: Core Foundation Release Notes for OS X (10.8 and earlier)
apple_id: TP40012903
resource_type: Release Note
platform: macOS
topic: Data Management
technology: CoreFoundation
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/DataManagement/RN-CoreFoundationOlderNotes/index.html
archived_at: '2026-07-18T02:50:23.666480Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# OS X Developer Release Note

OS X Release Notes Copyright © 2011 Apple Inc. All Rights Reserved.

#### Contents:

- [OS X Mountain Lion Release Notes for CoreFoundation Framework](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdsmbtfvkfeqkokngecvcfirpugscbkbkekus7he3dklktk4za)
- [OS X Lion Release Notes for CoreFoundation Framework](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdsmbtfvkfeqkokngecvcfirpugscbkbkekus7he3dklkukjau4u2mifkekrc7ircvgvc7ga)
- [OS X SnowLeopard Release Notes for CoreFoundation Framework](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdsmbtfvkfeqkokngecvcfirpugscbkbkekus7he3dklkukjau4u2mifkekrc7ircvgvc7ge3q)

### OS X Mountain Lion Release Notes for CoreFoundation Framework

### CoreFoundation Framework

CoreFoundation (aka CF) is a framework which provides C APIs for strings, collections, user preferences, property lists, plug-ins, bundles, notifications, runloop, etc. These APIs are designed with portability, performance, and consistency in mind, and are available to Cocoa and Carbon applications.

CoreFoundation is accessible directly as a public framework. But it is also within the CoreServices umbrella framework and is very often pulled into your application simply by linking against CoreServices or one of the higher level umbrellas such as Cocoa or Carbon which bring in CoreServices.

### CFPreferences Synchronization

CFPreferencesSynchronize() (and therefore CFPreferencesAppSynchronize() and -[NSUserDefaults synchronize]) is now automatic in virtually all cases. The only remaining reason to call it is if you need a separate process to be able to synchronously access the values you just set; for example if you set a preference, then post a notification which another process receives and reads the same preference. Most regular applications will never need to do this, and applications that do are encouraged to use an inter-process communication API (for example XPC) to communicate with the other process rather than using the preferences system for IPC.

CFPreferencesSynchronize() is also much faster in 10.8, and will avoid doing any work if there are no outstanding changes to read or write.

### CFPreferences Plist Files

The on-disk property list files used by CFPreferences have always been a private implementation detail, but in previous releases, directly modifying them has mostly worked (though there are some potential data-loss issues for applications that do so, even on previous systems). In 10.8 and later, the CFPreferences agent process (cfprefsd) will cache information from these files and asynchronously write to them. This means that directly modifying plist files is unlikely to have the expected results (new settings will not necessarily be read, and may even be overwritten). You should use the NSUserDefaults or CFPreferences APIs, or the defaults(1) command, to interact with the preferences system.

### CF/NSString Localized Formatting

In 10.8, in apps linked against the 10.8 SDK, existing APIs such as CFStringCreateWithFormat(), CFStringAppendFormat(), as well as NSString APIs +[NSString localizedStringWithFormat:], -[NSString initWithFormat:locale:], will now do localized formatting of numbers when a locale is provided (for +localizedStringWithFormat: this is implied, using the user's default locale.)

Currently these calls already do decimal point handling; so in some locales you currently do get comma instead of period for floating point numbers. This new behavior builds upon this; with this change, you will get additional behaviors, such as:

- use of alternate digits, such as in some Arabic locales

- placement of the negative symbol after the number, in some locales ("-42" -> "42-")

- thousands separators, in many locales including English ("12345" -> "12,345")

- alternate thousands separators ("12,345.6" -> "12.345,6")

The localization applies in the following cases:

- Only e, E, f, F, g, G, d, D, i, u, U are localized; the upper case variants are ignored (and treated as if they were lower case). a, A, o, O, x, X are not localized, and neither are all other non-numeric format characters.

- %@ used with NSNumber/CFNumber is localized.

- The flags +, -, 0, width, and precision are honored, but note that extra characters (beyond the specified width) may be inserted to accommodate thousands separators.

Potential pitfalls include getting localized output where unlocalized was intended, and use of unintended thousands separators (for instance if someone was showing a year with %d, now they may get "2,012").

### Greek letter case mapping

With Greek locale, the uppercase and titlecase mappings strip all Greek tonos characters.

### CoreFoundation Unicode Database

The CoreFoundation Unicode Database is updated to version 6.1.

### OS X Lion Release Notes for CoreFoundation Framework

CoreFoundation (aka CF) is a framework which provides C APIs for strings, collections, user preferences, property lists, plug-ins, bundles, notifications, runloop, etc. These APIs are designed with portability, performance, and consistency in mind, and are available to Cocoa and Carbon applications.

CoreFoundation is accessible directly as a public framework. But it is also within the CoreServices umbrella framework and is very often pulled into your application simply by linking against CoreServices or one of the higher level umbrellas such as Cocoa or Carbon which bring in CoreServices.

### CFXMLParser

CFXMLParser and CFXMLNode are deprecated. CFXMLParser has some deficiencies in terms of standards compliance and performance, and clients should migrate their uses of the CFXMLParser classes over to NSXMLParser, NSXMLDocument, or other XML parsing technologies on OS X.

### CFPreferences and Threading

In earlier releases of OS X, CFPreferences (and NSUserDefaults) serialized all access; if you've been avoiding using the preferences system in heavily threaded apps due to contention, this should be greatly improved.

### CFPreferencesAppSynchronize() and automatic synchronization

CFPreferences now uses the automatic synchronization system for the current application's domain that NSUserDefaults has always used. Additionally, automatic synchronization is now non-blocking in most cases. You should consider any calls to CFPreferencesAppSynchronize() carefully to see if they're really necessary, as you can avoid blocking IO by removing them.

### CFPreferences euid/uid handling

Prior to OS X Lion, CFPreferences (and therefore NSUserDefaults) would change the owner of the plist files it wrote to the uid/gid of the application writing to preferences. In Lion, for apps linked against Lion or later, the file will be owned by the euid/egid instead. You can temporarily revert to the old behavior for testing purposes by setting __CFPREFERENCES_USE_OLD_UID_BEHAVIOR to a non-null value in your environment. This will primarily impact applications with privileged helper tools that write to the preferences of non-privileged apps such as the Dock or the parent process.

### CFString Hyphenation

CFString now includes a facility for locating potential hyphenation points within a word. This is intended for the use of text layout engines such as NSTypesetter, when automatic hyphenation is enabled. Hyphenation depends heavily on the language of the text to be hyphenated, and the CFStringGetHyphenationLocationBeforeIndex() requires that this be specified as a CFLocale. Hyphenation data is available only for certain languages, currently English (US and GB), French, German, Italian, Spanish, Dutch, and Russian, although this list may be expanded in the future. A runtime determination of whether hyphenation data is available for a given language may be made using CFStringIsHyphenationAvailableForLocale().

The functions associated with the hyphenation facility are as follows:

```
CFIndex CFStringGetHyphenationLocationBeforeIndex(CFStringRef string, CFIndex location, CFRange limitRange,
                                      CFOptionFlags options, CFLocaleRef locale, UTF32Char *character);
```

```
Boolean CFStringIsHyphenationAvailableForLocale(CFLocaleRef locale);
```

To use CFStringGetHyphenationLocationBeforeIndex(), a client should pass in a string containing the text intended to be hyphenated, a location before which a hyphenation point is to be found, a range limiting the portion of the text to be examined, and the locale. The return value will be an index within the string where it is appropriate to insert a hyphen, or CFNotFound if none is found that is both before the specified location and within the limiting range. There may be cases in certain languages in which a character other than the standard hyphen is used to indicate hyphenation, and the character argument is intended to return a suggested character by reference; clients may pass NULL for this argument if they are not interested in this information.

### CFStringGetFileSystemRepresentation

CFStringGetFileSystemRepresentation() will now return false for any input string which contains embedded null characters, rather than returning a what is effectively a truncated (and outright wrong) string.

### CFStringCapitalize

The capitalization logic is enhanced to support the digraph, "IJ", with Dutch locale.

### CoreFoundation Unicode Database

The CoreFoundation Unicode Database is updated to version 6.0.

### kCFCompareForcedOrdering and kCFCompareNumerically with CFStringCompareWithOptionsAndLocale()

We were not able to force ordering for differences in numeric characters when the two numeric values are equal. Also, in some cases, we were not producing ideal results (i.e. 001 < 01). We're evaluating the ordering based on the number of digits involved in the numeric value.

### Distributed notification delivery

If you want a posted distributed notification to be received immediately, be sure you are passing the CFNotificationSuspensionBehaviorDeliverImmediately suspension behavior flag when registering for the notification, or using the kCFNotificationDeliverImmediately flag when posting. Bugs in OS X releases prior to 10.7 meant that sometimes a distributed notification would get delivered through to suspended observers, and not be properly queued, even when those flags weren't used.

### CFCalendar

The CFCalendar algorithms have several differences depending on which OS SDK version you build your app against. CFCalendarGetRangeOfUnit() can produce materially different results for OS X 10.4, OS X 10.5, and OS X 10.6/10.7. CFCalendarGetOrdinalityOfUnit() can produce materially different results for pre-OS X 10.6 and OS X 10.6/10.7. CFCalendarComposeAbsoluteTime() can produce different results on OS X 10.7 than previously when working with Week units.

But of course, most of the algorithms can produce different results between OS releases, as bugs are fixed or changes made, either in Foundation or CoreFoundation or in libraries beneath them. The differences noted in the previous paragraph are the significant ones.

There are 3 new Week-related unit/component constants in CFCalendar:

```
kCFCalendarUnitWeekOfMonth, kCFCalendarUnitWeekOfYear, kCFCalendarUnitYearForWeekOfYear
```

and the values of these quantities are week numbers or amounts relating to the month or the year that the week is in, and the year number for week-based interpretations of a calendar, such as the ISO 8601 calendar.

For many operations, there is no difference in meaning between kCFCalendarUnitWeekOfMonth and kCFCalendarUnitWeekOfYear, but for some there is a difference. Obviously getting the ordinality of a week with the month will usually give a different answer than the ordinality of the week within the year. The kCFCalendarUnitWeek constant is not yet officially deprecated, but its use in new code is discouraged. It has a behavior like either kCFCalendarUnitWeekOfMonth or kCFCalendarUnitWeekOfYear, as the case may be, to give it behavior like it had prior to OS X 10.7.

### CFURL

We've added lots of new resource property keys.

The functions CFURLCreateBookmarkDataFromFile() and CFURLWriteBookmarkDataToFile() have been introduced to iOS 5.0. They were previously introduced to OS X 10.6.

### CFURLEnumerator

CFURLEnumeratorGetSourceDidChange() is now deprecated.

The kCFURLEnumeratorIncludeDirectoriesPreOrder and kCFURLEnumeratorIncludeDirectoriesPostOrder options for recursive directory enumerators were added.

### CFFileSecurity

CFFileSecurity is a new object type introduced to replace the Carbon File Manager's FSFileSecurity object. CFFileSecurityRef and FSFileSecurityRef are the same object type (i.e., they have the same type ID and the underlying implementation is the same).

### CFError

We've added the kCFErrorURLKey and kCFErrorFilePathKey userInfo dictionary keys.

### New CFRunLoop API

There are two new functions to create CFRunLoopObservers and CFRunLoopTimers, respectively, which take a Block to execute, rather than function pointer and context arguments:

```
CFRunLoopObserverRef CFRunLoopObserverCreateWithHandler(CFAllocatorRef allocator, CFOptionFlags activities, Boolean repeats,
                                CFIndex order, void (^block)(CFRunLoopObserverRef observer, CFRunLoopActivity activity))
```

```
CFRunLoopTimerRef CFRunLoopTimerCreateWithHandler(CFAllocatorRef allocator, CFAbsoluteTime fireDate, CFTimeInterval interval,
                                CFOptionFlags flags, CFIndex order, void (^block)(CFRunLoopTimerRef timer))
```


### OS X SnowLeopard Release Notes for CoreFoundation Framework

CoreFoundation (aka CF) is a framework which provides C APIs for strings, collections, user preferences, property lists, plug-ins, bundles, notifications, runloop, etc. These APIs are designed with portability, performance, and consistency in mind, and are available to Cocoa and Carbon applications.

CoreFoundation is accessible directly as a public framework. But it is also within the CoreServices umbrella framework and is very often pulled into your application simply by linking against CoreServices or one of the higher level umbrellas such as Cocoa or Carbon which bring in CoreServices.

This document describes the changes in CF since OS X release 10.5. Updates to the document since WWDC 2008 are indicated in the section titles.

### CFURL

There are additions to CFURL API to enable more efficient file property manipulation, as well additional behaviors. More description forthcoming.

### CFPropertyList

The following functions are now obsolete and will be deprecated in a future release:

```
CFPropertyListRef CFPropertyListCreateFromXMLData(CFAllocatorRef allocator, CFDataRef xmlData, CFOptionFlags mutabilityOption,
                                CFStringRef *errorString);
CFPropertyListRef CFPropertyListCreateFromStream(CFAllocatorRef allocator, CFReadStreamRef stream, CFIndex streamLength,
                                CFOptionFlags mutabilityOption, CFPropertyListFormat *format, CFStringRef *errorString);
CFIndex CFPropertyListWriteToStream(CFPropertyListRef propertyList, CFWriteStreamRef stream, CFPropertyListFormat format,
                                CFStringRef *errorString);
CFDataRef CFPropertyListCreateXMLData(CFAllocatorRef allocator, CFPropertyListRef propertyList);
```

The replacement API is:

```
CFPropertyListRef CFPropertyListCreateWithData(CFAllocatorRef allocator, CFDataRef data, CFOptionFlags options,
                                CFPropertyListFormat *format, CFErrorRef *error);
CFPropertyListRef CFPropertyListCreateWithStream(CFAllocatorRef allocator, CFReadStreamRef stream, CFIndex streamLength,
                                CFOptionFlags options, CFPropertyListFormat *format, CFErrorRef *error);
CFIndex CFPropertyListWrite(CFPropertyListRef propertyList, CFWriteStreamRef stream, CFPropertyListFormat format,
                                CFOptionFlags options, CFErrorRef *error);
CFDataRef CFPropertyListCreateData(CFAllocatorRef allocator, CFPropertyListRef propertyList, CFPropertyListFormat format,
                                CFOptionFlags options, CFErrorRef *error);
```

The new API provides better error handling, better support for localization, and easier creation of binary property lists. Any error parameter may be set to NULL if no error information is desired. If a CFErrorRef pointer is passed in and an error occurs, it will be filled out with information about the error and it is the responsibility of the caller to release the new error. The format parameter in the CFPropertyListCreateWIthData and CFPropertyListCreateWithStream functions may also be set to NULL, but if a CFPropertyListFormat pointer is passed in, it will be filled out with the format of the property list.

The option flags on the CFPropertyListCreateWithData and CFPropertyListCreateWithStream functions may be set to any of the CFPropertyListMutabilityOptions values. The options flags on CFPropertyListWrite and CFPropertyListCreateData are currently unused and should be set to 0.

### CFXMLParser (New since WWDC 2008)

CFXMLParser and CFXMLNode will be officially deprecated in a future major release of OS X. CFXMLParser has some deficiencies in terms of standards compliance and performance, and clients should migrate their uses of the CFXMLParser classes over to NSXMLParser, NSXMLDocument, or other XML parsing technologies on OS X.

### CoreFoundation API not available in iOS 2.0

The OS X APIs in CFUserNotification.h, CFXMLParser.h, CFXMLNode.h, and CFStringTokenizer.h are not available in iOS 2.0. Distributed notifications (CFNotificationCenterGetDistributedCenter()) are also not available. Otherwise, iOS 2.0 contains an API matching that in OS X 10.5.

### CoreFoundation API not available in iOS 3.0

The OS X APIs in CFUserNotification.h, CFXMLParser.h, and CFXMLNode.h are not available in iOS 3.0. Distributed notifications (CFNotificationCenterGetDistributedCenter()) are also not available. Otherwise, iOS 3.0 contains an API matching that in OS X 10.5.

### New CFCalendarUnit

A new "quarter" calendar unit (kCFCalendarUnitQuarter) has been added to the set of CFCalendarUnits (CFCalendar.h).

### New calendars

Four new calendar constants (kCFRepublicOfChinaCalendar, kCFPersianCalendar, kCFIndianCalendar, kCFISO8601Calendar) have been added (CFLocale.h). The ISO8601 calendar is not yet implemented. A Chinese calendar can be created, and one can do calendrical calculations with it, but it should not be used for formatting as the necessary underlying functionality is not functioning correctly yet.

### CFDataFind (New since November seed)

CFData now has a function that will efficiently search its contents:

```
    CFRange CFDataFind(CFDataRef theData, CFDataRef dataToFind, CFRange searchRange, CFDataSearchFlags compareOptions);
```

The semantics are nearly identical to CFStringFind. The only significant difference is the lack of 'case insensitive' and 'literal' search options, which are only applicable to strings.

### CFString (Updated since WWDC 2008)

The functions CFStringGetMaximumSizeForEncoding() and CFStringGetMaximumSizeOfFileSystemRepresentation() will now return kCFNotFound if the amount of memory required for storing the results of the encoding conversion would exceed LONG_MAX.

Usage note: When using CFStringCreateWithFormat(), and any other CFString or NSString formatting APIs, it's illegal to pass fewer ordered (n$) arguments than there are arguments. For instance:

```
    CFStringCreateWithFormat(NULL, NULL, CFSTR("%2$d", arg1, arg2);
```

This is because there's no way for CFString to know how to skip the first argument to get to the second. There is no behavior change here, just a clarification.

### CFString

There are now 4 new inline functions for working with UTF-16 surrogate characters declared in CFString.h. CFStringIsSurrogateHighCharacter() and CFStringIsSurrogateLowCharacter() identify surrogate characters. CFStringGetLongCharacterForSurrogatePair() maps a pair of high and low surrogate characters to the Unicode Scalar Value. CFStringGetSurrogatePairForLongCharacter() maps a Unicode Scaler Value back to the surrogate pair.

There are two new CFStringEncoding constants: KCFStringEncodingUTF7 and kCFStringEncodingUTF7_IMAP.

### Unicode (New since WWDC 2008)

The CoreFoundation Unicode Database is updated to version 5.1.

### CFCharacterSet (New since WWDC 2008)

CFCharacterSetCreateWithCharactersInString, CFCharacterSetAddCharactersInString, and CFCharacterSetRemoveCharactersInString now correctly recognizes surrogate paris in the string.
