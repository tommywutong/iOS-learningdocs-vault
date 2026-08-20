---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/CoreFoundation.html
archived_at: '2026-07-18T02:56:08.717218Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# CoreFoundation Changes

## CoreFoundation

Removed CFCalendarUnit.valueRemoved CFDataSearchFlags.valueRemoved CFFileSecurityClearOptions.valueRemoved CFGregorianUnitFlags.valueRemoved CFNumberFormatterOptionFlags.valueRemoved CFPropertyListMutabilityOptions.valueRemoved CFRunLoopActivity.valueRemoved CFSocketCallBackType.valueRemoved CFStreamEventType.valueRemoved CFStringCompareFlags.valueRemoved CFStringTokenizerTokenType.valueRemoved CFURLBookmarkCreationOptions.valueRemoved CFURLBookmarkResolutionOptions.valueRemoved CFURLEnumeratorOptions.valueAdded CFCalendarUnit.init(rawValue: CFOptionFlags)Added CFDataSearchFlags.init(rawValue: CFOptionFlags)Added CFFileSecurityClearOptions.init(rawValue: CFOptionFlags)Added CFGregorianUnitFlags.init(rawValue: CFOptionFlags)Added CFNumberFormatterOptionFlags.init(rawValue: CFOptionFlags)Added CFPropertyListMutabilityOptions.init(rawValue: CFOptionFlags)Added CFRunLoopActivity.init(rawValue: CFOptionFlags)Added CFSocketCallBackType.init(rawValue: CFOptionFlags)Added CFStreamEventType.init(rawValue: CFOptionFlags)Added CFStringCompareFlags.init(rawValue: CFOptionFlags)Added CFStringTokenizerTokenType.init(rawValue: CFOptionFlags)Added CFURLBookmarkCreationOptions.init(rawValue: CFOptionFlags)Added CFURLBookmarkResolutionOptions.init(rawValue: CFOptionFlags)Added CFURLEnumeratorOptions.init(rawValue: CFOptionFlags)Modified CFCalendarUnit [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFCalendarUnit : RawOptionSetType {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var Era: CFCalendarUnit { get }     static var Year: CFCalendarUnit { get }     static var Month: CFCalendarUnit { get }     static var Day: CFCalendarUnit { get }     static var Hour: CFCalendarUnit { get }     static var Minute: CFCalendarUnit { get }     static var Second: CFCalendarUnit { get }     static var Week: CFCalendarUnit { get }     static var Weekday: CFCalendarUnit { get }     static var WeekdayOrdinal: CFCalendarUnit { get }     static var Quarter: CFCalendarUnit { get }     static var WeekOfMonth: CFCalendarUnit { get }     static var WeekOfYear: CFCalendarUnit { get }     static var YearForWeekOfYear: CFCalendarUnit { get } } ``` |
| To | ``` struct CFCalendarUnit : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var Era: CFCalendarUnit { get }     static var Year: CFCalendarUnit { get }     static var Month: CFCalendarUnit { get }     static var Day: CFCalendarUnit { get }     static var Hour: CFCalendarUnit { get }     static var Minute: CFCalendarUnit { get }     static var Second: CFCalendarUnit { get }     static var Week: CFCalendarUnit { get }     static var Weekday: CFCalendarUnit { get }     static var WeekdayOrdinal: CFCalendarUnit { get }     static var Quarter: CFCalendarUnit { get }     static var WeekOfMonth: CFCalendarUnit { get }     static var WeekOfYear: CFCalendarUnit { get }     static var YearForWeekOfYear: CFCalendarUnit { get } } ``` |

Modified CFCalendarUnit.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFDataSearchFlags [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct CFDataSearchFlags : RawOptionSetType {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var Backwards: CFDataSearchFlags { get }     static var Anchored: CFDataSearchFlags { get } } ``` | iOS 8.0 |
| To | ``` struct CFDataSearchFlags : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var Backwards: CFDataSearchFlags { get }     static var Anchored: CFDataSearchFlags { get } } ``` | iOS 4.0 |

Modified CFDataSearchFlags.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFFileSecurityClearOptions [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct CFFileSecurityClearOptions : RawOptionSetType {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var Owner: CFFileSecurityClearOptions { get }     static var Group: CFFileSecurityClearOptions { get }     static var Mode: CFFileSecurityClearOptions { get }     static var OwnerUUID: CFFileSecurityClearOptions { get }     static var GroupUUID: CFFileSecurityClearOptions { get }     static var AccessControlList: CFFileSecurityClearOptions { get } } ``` | iOS 8.0 |
| To | ``` struct CFFileSecurityClearOptions : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var Owner: CFFileSecurityClearOptions { get }     static var Group: CFFileSecurityClearOptions { get }     static var Mode: CFFileSecurityClearOptions { get }     static var OwnerUUID: CFFileSecurityClearOptions { get }     static var GroupUUID: CFFileSecurityClearOptions { get }     static var AccessControlList: CFFileSecurityClearOptions { get } } ``` | iOS 6.0 |

Modified CFFileSecurityClearOptions.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFGregorianDate [struct]

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified CFGregorianUnitFlags [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFGregorianUnitFlags : RawOptionSetType {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var UnitsYears: CFGregorianUnitFlags { get }     static var UnitsMonths: CFGregorianUnitFlags { get }     static var UnitsDays: CFGregorianUnitFlags { get }     static var UnitsHours: CFGregorianUnitFlags { get }     static var UnitsMinutes: CFGregorianUnitFlags { get }     static var UnitsSeconds: CFGregorianUnitFlags { get }     static var AllUnits: CFGregorianUnitFlags { get } } ``` |
| To | ``` struct CFGregorianUnitFlags : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var UnitsYears: CFGregorianUnitFlags { get }     static var UnitsMonths: CFGregorianUnitFlags { get }     static var UnitsDays: CFGregorianUnitFlags { get }     static var UnitsHours: CFGregorianUnitFlags { get }     static var UnitsMinutes: CFGregorianUnitFlags { get }     static var UnitsSeconds: CFGregorianUnitFlags { get }     static var AllUnits: CFGregorianUnitFlags { get } } ``` |

Modified CFGregorianUnitFlags.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFGregorianUnits [struct]

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified CFNumberFormatterOptionFlags [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFNumberFormatterOptionFlags : RawOptionSetType {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var ParseIntegersOnly: CFNumberFormatterOptionFlags { get } } ``` |
| To | ``` struct CFNumberFormatterOptionFlags : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var ParseIntegersOnly: CFNumberFormatterOptionFlags { get } } ``` |

Modified CFNumberFormatterOptionFlags.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFPropertyListMutabilityOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFPropertyListMutabilityOptions : RawOptionSetType {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var Immutable: CFPropertyListMutabilityOptions { get }     static var MutableContainers: CFPropertyListMutabilityOptions { get }     static var MutableContainersAndLeaves: CFPropertyListMutabilityOptions { get } } ``` |
| To | ``` struct CFPropertyListMutabilityOptions : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var Immutable: CFPropertyListMutabilityOptions { get }     static var MutableContainers: CFPropertyListMutabilityOptions { get }     static var MutableContainersAndLeaves: CFPropertyListMutabilityOptions { get } } ``` |

Modified CFPropertyListMutabilityOptions.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFRunLoopActivity [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFRunLoopActivity : RawOptionSetType {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var Entry: CFRunLoopActivity { get }     static var BeforeTimers: CFRunLoopActivity { get }     static var BeforeSources: CFRunLoopActivity { get }     static var BeforeWaiting: CFRunLoopActivity { get }     static var AfterWaiting: CFRunLoopActivity { get }     static var Exit: CFRunLoopActivity { get }     static var AllActivities: CFRunLoopActivity { get } } ``` |
| To | ``` struct CFRunLoopActivity : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var Entry: CFRunLoopActivity { get }     static var BeforeTimers: CFRunLoopActivity { get }     static var BeforeSources: CFRunLoopActivity { get }     static var BeforeWaiting: CFRunLoopActivity { get }     static var AfterWaiting: CFRunLoopActivity { get }     static var Exit: CFRunLoopActivity { get }     static var AllActivities: CFRunLoopActivity { get } } ``` |

Modified CFRunLoopActivity.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFSocketCallBackType [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFSocketCallBackType : RawOptionSetType {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var NoCallBack: CFSocketCallBackType { get }     static var ReadCallBack: CFSocketCallBackType { get }     static var AcceptCallBack: CFSocketCallBackType { get }     static var DataCallBack: CFSocketCallBackType { get }     static var ConnectCallBack: CFSocketCallBackType { get }     static var WriteCallBack: CFSocketCallBackType { get } } ``` |
| To | ``` struct CFSocketCallBackType : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var NoCallBack: CFSocketCallBackType { get }     static var ReadCallBack: CFSocketCallBackType { get }     static var AcceptCallBack: CFSocketCallBackType { get }     static var DataCallBack: CFSocketCallBackType { get }     static var ConnectCallBack: CFSocketCallBackType { get }     static var WriteCallBack: CFSocketCallBackType { get } } ``` |

Modified CFSocketCallBackType.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFStreamEventType [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFStreamEventType : RawOptionSetType {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var None: CFStreamEventType { get }     static var OpenCompleted: CFStreamEventType { get }     static var HasBytesAvailable: CFStreamEventType { get }     static var CanAcceptBytes: CFStreamEventType { get }     static var ErrorOccurred: CFStreamEventType { get }     static var EndEncountered: CFStreamEventType { get } } ``` |
| To | ``` struct CFStreamEventType : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var None: CFStreamEventType { get }     static var OpenCompleted: CFStreamEventType { get }     static var HasBytesAvailable: CFStreamEventType { get }     static var CanAcceptBytes: CFStreamEventType { get }     static var ErrorOccurred: CFStreamEventType { get }     static var EndEncountered: CFStreamEventType { get } } ``` |

Modified CFStreamEventType.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFStringCompareFlags [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFStringCompareFlags : RawOptionSetType {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var CompareCaseInsensitive: CFStringCompareFlags { get }     static var CompareBackwards: CFStringCompareFlags { get }     static var CompareAnchored: CFStringCompareFlags { get }     static var CompareNonliteral: CFStringCompareFlags { get }     static var CompareLocalized: CFStringCompareFlags { get }     static var CompareNumerically: CFStringCompareFlags { get }     static var CompareDiacriticInsensitive: CFStringCompareFlags { get }     static var CompareWidthInsensitive: CFStringCompareFlags { get }     static var CompareForcedOrdering: CFStringCompareFlags { get } } ``` |
| To | ``` struct CFStringCompareFlags : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var CompareCaseInsensitive: CFStringCompareFlags { get }     static var CompareBackwards: CFStringCompareFlags { get }     static var CompareAnchored: CFStringCompareFlags { get }     static var CompareNonliteral: CFStringCompareFlags { get }     static var CompareLocalized: CFStringCompareFlags { get }     static var CompareNumerically: CFStringCompareFlags { get }     static var CompareDiacriticInsensitive: CFStringCompareFlags { get }     static var CompareWidthInsensitive: CFStringCompareFlags { get }     static var CompareForcedOrdering: CFStringCompareFlags { get } } ``` |

Modified CFStringCompareFlags.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFStringTokenizerTokenType [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFStringTokenizerTokenType : RawOptionSetType {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var None: CFStringTokenizerTokenType { get }     static var Normal: CFStringTokenizerTokenType { get }     static var HasSubTokensMask: CFStringTokenizerTokenType { get }     static var HasDerivedSubTokensMask: CFStringTokenizerTokenType { get }     static var HasHasNumbersMask: CFStringTokenizerTokenType { get }     static var HasNonLettersMask: CFStringTokenizerTokenType { get }     static var IsCJWordMask: CFStringTokenizerTokenType { get } } ``` |
| To | ``` struct CFStringTokenizerTokenType : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var None: CFStringTokenizerTokenType { get }     static var Normal: CFStringTokenizerTokenType { get }     static var HasSubTokensMask: CFStringTokenizerTokenType { get }     static var HasDerivedSubTokensMask: CFStringTokenizerTokenType { get }     static var HasHasNumbersMask: CFStringTokenizerTokenType { get }     static var HasNonLettersMask: CFStringTokenizerTokenType { get }     static var IsCJWordMask: CFStringTokenizerTokenType { get } } ``` |

Modified CFStringTokenizerTokenType.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFTimeZoneNameStyle [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFURLBookmarkCreationOptions [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct CFURLBookmarkCreationOptions : RawOptionSetType {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var MinimalBookmarkMask: CFURLBookmarkCreationOptions { get }     static var SuitableForBookmarkFile: CFURLBookmarkCreationOptions { get }     static var WithSecurityScope: CFURLBookmarkCreationOptions { get }     static var SecurityScopeAllowOnlyReadAccess: CFURLBookmarkCreationOptions { get }     static var PreferFileIDResolutionMask: CFURLBookmarkCreationOptions { get } } ``` | iOS 8.0 |
| To | ``` struct CFURLBookmarkCreationOptions : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var MinimalBookmarkMask: CFURLBookmarkCreationOptions { get }     static var SuitableForBookmarkFile: CFURLBookmarkCreationOptions { get }     static var WithSecurityScope: CFURLBookmarkCreationOptions { get }     static var SecurityScopeAllowOnlyReadAccess: CFURLBookmarkCreationOptions { get }     static var PreferFileIDResolutionMask: CFURLBookmarkCreationOptions { get } } ``` | iOS 4.0 |

Modified CFURLBookmarkCreationOptions.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFURLBookmarkResolutionOptions [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct CFURLBookmarkResolutionOptions : RawOptionSetType {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var CFURLBookmarkResolutionWithoutUIMask: CFURLBookmarkResolutionOptions { get }     static var CFURLBookmarkResolutionWithoutMountingMask: CFURLBookmarkResolutionOptions { get }     static var CFURLBookmarkResolutionWithSecurityScope: CFURLBookmarkResolutionOptions { get }     static var CFBookmarkResolutionWithoutUIMask: CFURLBookmarkResolutionOptions { get }     static var CFBookmarkResolutionWithoutMountingMask: CFURLBookmarkResolutionOptions { get } } ``` | iOS 8.0 |
| To | ``` struct CFURLBookmarkResolutionOptions : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var CFURLBookmarkResolutionWithoutUIMask: CFURLBookmarkResolutionOptions { get }     static var CFURLBookmarkResolutionWithoutMountingMask: CFURLBookmarkResolutionOptions { get }     static var CFURLBookmarkResolutionWithSecurityScope: CFURLBookmarkResolutionOptions { get }     static var CFBookmarkResolutionWithoutUIMask: CFURLBookmarkResolutionOptions { get }     static var CFBookmarkResolutionWithoutMountingMask: CFURLBookmarkResolutionOptions { get } } ``` | iOS 4.0 |

Modified CFURLBookmarkResolutionOptions.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFURLEnumeratorOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFURLEnumeratorOptions : RawOptionSetType {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var DefaultBehavior: CFURLEnumeratorOptions { get }     static var DescendRecursively: CFURLEnumeratorOptions { get }     static var SkipInvisibles: CFURLEnumeratorOptions { get }     static var GenerateFileReferenceURLs: CFURLEnumeratorOptions { get }     static var SkipPackageContents: CFURLEnumeratorOptions { get }     static var IncludeDirectoriesPreOrder: CFURLEnumeratorOptions { get }     static var IncludeDirectoriesPostOrder: CFURLEnumeratorOptions { get } } ``` |
| To | ``` struct CFURLEnumeratorOptions : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var DefaultBehavior: CFURLEnumeratorOptions { get }     static var DescendRecursively: CFURLEnumeratorOptions { get }     static var SkipInvisibles: CFURLEnumeratorOptions { get }     static var GenerateFileReferenceURLs: CFURLEnumeratorOptions { get }     static var SkipPackageContents: CFURLEnumeratorOptions { get }     static var IncludeDirectoriesPreOrder: CFURLEnumeratorOptions { get }     static var IncludeDirectoriesPostOrder: CFURLEnumeratorOptions { get } } ``` |

Modified CFURLEnumeratorOptions.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFAbsoluteTimeAddGregorianUnits(CFAbsoluteTime, CFTimeZone!, CFGregorianUnits) -> CFAbsoluteTime

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified CFAbsoluteTimeGetDayOfWeek(CFAbsoluteTime, CFTimeZone!) -> Int32

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified CFAbsoluteTimeGetDayOfYear(CFAbsoluteTime, CFTimeZone!) -> Int32

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified CFAbsoluteTimeGetDifferenceAsGregorianUnits(CFAbsoluteTime, CFAbsoluteTime, CFTimeZone!, CFOptionFlags) -> CFGregorianUnits

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified CFAbsoluteTimeGetGregorianDate(CFAbsoluteTime, CFTimeZone!) -> CFGregorianDate

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified CFAbsoluteTimeGetWeekOfYear(CFAbsoluteTime, CFTimeZone!) -> Int32

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified CFBundleCopyExecutableArchitectures(CFBundle!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFBundleCopyExecutableArchitecturesForURL(CFURL!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFBundleGetPlugIn(CFBundle!) -> CFPlugIn!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFBundleGetPlugIn(_ bundle: CFBundle!) -> CFPlugInRef ``` | iOS 8.0 |
| To | ``` func CFBundleGetPlugIn(_ bundle: CFBundle!) -> CFPlugIn! ``` | iOS 8.1 |

Modified CFBundleLoadExecutableAndReturnError(CFBundle!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFBundlePreflightExecutable(CFBundle!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFCalendarGetTimeRangeOfUnit(CFCalendar!, CFCalendarUnit, CFAbsoluteTime, UnsafeMutablePointer<CFAbsoluteTime>, UnsafeMutablePointer<CFTimeInterval>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFCopyHomeDirectoryURL() -> CFURL!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CFDataFind(CFData!, CFData!, CFRange, CFDataSearchFlags) -> CFRange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFDateFormatterCreateDateFormatFromTemplate(CFAllocator!, CFString!, CFOptionFlags, CFLocale!) -> CFString!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFErrorCopyDescription(CFError!) -> CFString!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFErrorCopyFailureReason(CFError!) -> CFString!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFErrorCopyRecoverySuggestion(CFError!) -> CFString!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFErrorCopyUserInfo(CFError!) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFErrorCreate(CFAllocator!, CFString!, CFIndex, CFDictionary!) -> CFError!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFErrorCreateWithUserInfoKeysAndValues(CFAllocator!, CFString!, CFIndex, UnsafePointer<UnsafePointer<Void>>, UnsafePointer<UnsafePointer<Void>>, CFIndex) -> CFError!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFErrorGetCode(CFError!) -> CFIndex

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFErrorGetDomain(CFError!) -> CFString!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFErrorGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFFileDescriptorCreate(CFAllocator!, CFFileDescriptorNativeDescriptor, Boolean, CFFileDescriptorCallBack, UnsafePointer<CFFileDescriptorContext>) -> CFFileDescriptor!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFFileDescriptorCreateRunLoopSource(CFAllocator!, CFFileDescriptor!, CFIndex) -> CFRunLoopSource!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFFileDescriptorDisableCallBacks(CFFileDescriptor!, CFOptionFlags)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFFileDescriptorEnableCallBacks(CFFileDescriptor!, CFOptionFlags)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFFileDescriptorGetContext(CFFileDescriptor!, UnsafeMutablePointer<CFFileDescriptorContext>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFFileDescriptorGetNativeDescriptor(CFFileDescriptor!) -> CFFileDescriptorNativeDescriptor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFFileDescriptorGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFFileDescriptorInvalidate(CFFileDescriptor!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFFileDescriptorIsValid(CFFileDescriptor!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFFileSecurityClearProperties(CFFileSecurity!, CFFileSecurityClearOptions) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CFFileSecurityCopyAccessControlList(CFFileSecurity!, UnsafeMutablePointer<acl_t>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CFFileSecurityCopyGroupUUID(CFFileSecurity!, UnsafeMutablePointer<Unmanaged<CFUUID>?>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CFFileSecurityCopyOwnerUUID(CFFileSecurity!, UnsafeMutablePointer<Unmanaged<CFUUID>?>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CFFileSecurityCreate(CFAllocator!) -> CFFileSecurity!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CFFileSecurityCreateCopy(CFAllocator!, CFFileSecurity!) -> CFFileSecurity!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CFFileSecurityGetGroup(CFFileSecurity!, UnsafeMutablePointer<gid_t>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CFFileSecurityGetMode(CFFileSecurity!, UnsafeMutablePointer<mode_t>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CFFileSecurityGetOwner(CFFileSecurity!, UnsafeMutablePointer<uid_t>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CFFileSecurityGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CFFileSecuritySetAccessControlList(CFFileSecurity!, acl_t) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CFFileSecuritySetGroup(CFFileSecurity!, gid_t) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CFFileSecuritySetGroupUUID(CFFileSecurity!, CFUUID!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CFFileSecuritySetMode(CFFileSecurity!, mode_t) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CFFileSecuritySetOwner(CFFileSecurity!, uid_t) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CFFileSecuritySetOwnerUUID(CFFileSecurity!, CFUUID!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CFGregorianDateGetAbsoluteTime(CFGregorianDate, CFTimeZone!) -> CFAbsoluteTime

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified CFGregorianDateIsValid(CFGregorianDate, CFOptionFlags) -> Boolean

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified CFLocaleCopyCommonISOCurrencyCodes() -> CFArray!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFLocaleCopyPreferredLanguages() -> CFArray!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFLocaleCreateLocaleIdentifierFromWindowsLocaleCode(CFAllocator!, UInt32) -> CFString!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFLocaleGetLanguageCharacterDirection(CFString!) -> CFLocaleLanguageDirection

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFLocaleGetLanguageLineDirection(CFString!) -> CFLocaleLanguageDirection

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFLocaleGetWindowsLocaleCodeFromLocaleIdentifier(CFString!) -> UInt32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFMessagePortSetDispatchQueue(CFMessagePort!, dispatch_queue_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFPlugInCreate(CFAllocator!, CFURL!) -> CFPlugIn!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFPlugInCreate(_ allocator: CFAllocator!, _ plugInURL: CFURL!) -> CFPlugInRef ``` | iOS 8.0 |
| To | ``` func CFPlugInCreate(_ allocator: CFAllocator!, _ plugInURL: CFURL!) -> CFPlugIn! ``` | iOS 8.1 |

Modified CFPlugInDynamicRegisterFunction

|  | Declaration |
| --- | --- |
| From | ``` typealias CFPlugInDynamicRegisterFunction = CFunctionPointer<((CFPlugInRef) -> Void)> ``` |
| To | ``` typealias CFPlugInDynamicRegisterFunction = CFunctionPointer<((CFPlugIn!) -> Void)> ``` |

Modified CFPlugInFindFactoriesForPlugInTypeInPlugIn(CFUUID!, CFPlugIn!) -> CFArray!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFPlugInFindFactoriesForPlugInTypeInPlugIn(_ typeUUID: CFUUID!, _ plugIn: CFPlugInRef) -> CFArray! ``` | iOS 8.0 |
| To | ``` func CFPlugInFindFactoriesForPlugInTypeInPlugIn(_ typeUUID: CFUUID!, _ plugIn: CFPlugIn!) -> CFArray! ``` | iOS 8.1 |

Modified CFPlugInGetBundle(CFPlugIn!) -> CFBundle!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFPlugInGetBundle(_ plugIn: CFPlugInRef) -> CFBundle! ``` | iOS 8.0 |
| To | ``` func CFPlugInGetBundle(_ plugIn: CFPlugIn!) -> CFBundle! ``` | iOS 8.1 |

Modified CFPlugInIsLoadOnDemand(CFPlugIn!) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFPlugInIsLoadOnDemand(_ plugIn: CFPlugInRef) -> Boolean ``` | iOS 8.0 |
| To | ``` func CFPlugInIsLoadOnDemand(_ plugIn: CFPlugIn!) -> Boolean ``` | iOS 8.1 |

Modified CFPlugInRef

|  | Declaration |
| --- | --- |
| From | ``` typealias CFPlugInRef = COpaquePointer ``` |
| To | ``` typealias CFPlugInRef = CFPlugIn ``` |

Modified CFPlugInRegisterFactoryFunctionByName(CFUUID!, CFPlugIn!, CFString!) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFPlugInRegisterFactoryFunctionByName(_ factoryUUID: CFUUID!, _ plugIn: CFPlugInRef, _ functionName: CFString!) -> Boolean ``` | iOS 8.0 |
| To | ``` func CFPlugInRegisterFactoryFunctionByName(_ factoryUUID: CFUUID!, _ plugIn: CFPlugIn!, _ functionName: CFString!) -> Boolean ``` | iOS 8.1 |

Modified CFPlugInSetLoadOnDemand(CFPlugIn!, Boolean)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFPlugInSetLoadOnDemand(_ plugIn: CFPlugInRef, _ flag: Boolean) ``` | iOS 8.0 |
| To | ``` func CFPlugInSetLoadOnDemand(_ plugIn: CFPlugIn!, _ flag: Boolean) ``` | iOS 8.1 |

Modified CFPlugInUnloadFunction

|  | Declaration |
| --- | --- |
| From | ``` typealias CFPlugInUnloadFunction = CFunctionPointer<((CFPlugInRef) -> Void)> ``` |
| To | ``` typealias CFPlugInUnloadFunction = CFunctionPointer<((CFPlugIn!) -> Void)> ``` |

Modified CFPropertyListCreateData(CFAllocator!, CFPropertyList!, CFPropertyListFormat, CFOptionFlags, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFPropertyListCreateFromStream(CFAllocator!, CFReadStream!, CFIndex, CFOptionFlags, UnsafeMutablePointer<CFPropertyListFormat>, UnsafeMutablePointer<Unmanaged<CFString>?>) -> Unmanaged<CFPropertyList>!

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified CFPropertyListCreateFromXMLData(CFAllocator!, CFData!, CFOptionFlags, UnsafeMutablePointer<Unmanaged<CFString>?>) -> Unmanaged<CFPropertyList>!

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified CFPropertyListCreateWithData(CFAllocator!, CFData!, CFOptionFlags, UnsafeMutablePointer<CFPropertyListFormat>, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFPropertyList>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFPropertyListCreateWithStream(CFAllocator!, CFReadStream!, CFIndex, CFOptionFlags, UnsafeMutablePointer<CFPropertyListFormat>, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFPropertyList>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFPropertyListCreateXMLData(CFAllocator!, CFPropertyList!) -> Unmanaged<CFData>!

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified CFPropertyListWrite(CFPropertyList!, CFWriteStream!, CFPropertyListFormat, CFOptionFlags, UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFIndex

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFPropertyListWriteToStream(CFPropertyList!, CFWriteStream!, CFPropertyListFormat, UnsafeMutablePointer<Unmanaged<CFString>?>) -> CFIndex

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified CFReadStreamCopyDispatchQueue(CFReadStream!) -> dispatch_queue_t!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CFReadStreamCopyError(CFReadStream!) -> CFError!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFReadStreamSetDispatchQueue(CFReadStream!, dispatch_queue_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CFRunLoopObserverCreateWithHandler(CFAllocator!, CFOptionFlags, Boolean, CFIndex,((CFRunLoopObserver!, CFRunLoopActivity) -> Void)!) -> CFRunLoopObserver!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CFRunLoopPerformBlock(CFRunLoop!, AnyObject!,(() -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFRunLoopTimerCreateWithHandler(CFAllocator!, CFAbsoluteTime, CFTimeInterval, CFOptionFlags, CFIndex,((CFRunLoopTimer!) -> Void)!) -> CFRunLoopTimer!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CFRunLoopTimerGetTolerance(CFRunLoopTimer!) -> CFTimeInterval

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CFRunLoopTimerSetTolerance(CFRunLoopTimer!, CFTimeInterval)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CFStringCompareWithOptionsAndLocale(CFString!, CFString!, CFRange, CFStringCompareFlags, CFLocale!) -> CFComparisonResult

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFStringFindWithOptionsAndLocale(CFString!, CFString!, CFRange, CFStringCompareFlags, CFLocale!, UnsafeMutablePointer<CFRange>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFStringFold(CFMutableString!, CFStringCompareFlags, CFLocale!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFStringGetHyphenationLocationBeforeIndex(CFString!, CFIndex, CFRange, CFOptionFlags, CFLocale!, UnsafeMutablePointer<UTF32Char>) -> CFIndex

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified CFStringGetParagraphBounds(CFString!, CFRange, UnsafeMutablePointer<CFIndex>, UnsafeMutablePointer<CFIndex>, UnsafeMutablePointer<CFIndex>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFStringIsHyphenationAvailableForLocale(CFLocale!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified CFStringTokenizerAdvanceToNextToken(CFStringTokenizer!) -> CFStringTokenizerTokenType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified CFStringTokenizerCopyBestStringLanguage(CFString!, CFRange) -> CFString!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified CFStringTokenizerCopyCurrentTokenAttribute(CFStringTokenizer!, CFOptionFlags) -> AnyObject!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified CFStringTokenizerCreate(CFAllocator!, CFString!, CFRange, CFOptionFlags, CFLocale!) -> CFStringTokenizer!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified CFStringTokenizerGetCurrentSubTokens(CFStringTokenizer!, UnsafeMutablePointer<CFRange>, CFIndex, CFMutableArray!) -> CFIndex

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified CFStringTokenizerGetCurrentTokenRange(CFStringTokenizer!) -> CFRange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified CFStringTokenizerGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified CFStringTokenizerGoToTokenAtIndex(CFStringTokenizer!, CFIndex) -> CFStringTokenizerTokenType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified CFStringTokenizerSetString(CFStringTokenizer!, CFString!, CFRange)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified CFTimeZoneCopyLocalizedName(CFTimeZone!, CFTimeZoneNameStyle, CFLocale!) -> CFString!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFTimeZoneGetDaylightSavingTimeOffset(CFTimeZone!, CFAbsoluteTime) -> CFTimeInterval

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFTimeZoneGetNextDaylightSavingTimeTransition(CFTimeZone!, CFAbsoluteTime) -> CFAbsoluteTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFURLClearResourcePropertyCache(CFURL!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFURLClearResourcePropertyCacheForKey(CFURL!, CFString!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFURLCopyResourcePropertiesForKeys(CFURL!, CFArray!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFURLCopyResourcePropertyForKey(CFURL!, CFString!, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFURLCreateBookmarkData(CFAllocator!, CFURL!, CFURLBookmarkCreationOptions, CFArray!, CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFURLCreateBookmarkDataFromFile(CFAllocator!, CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CFURLCreateByResolvingBookmarkData(CFAllocator!, CFData!, CFURLBookmarkResolutionOptions, CFURL!, CFArray!, UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFURLCreateFilePathURL(CFAllocator!, CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFURLCreateFileReferenceURL(CFAllocator!, CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFURLCreateResourcePropertiesForKeysFromBookmarkData(CFAllocator!, CFArray!, CFData!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFURLCreateResourcePropertyForKeyFromBookmarkData(CFAllocator!, CFString!, CFData!) -> Unmanaged<AnyObject>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFURLEnumeratorCreateForDirectoryURL(CFAllocator!, CFURL!, CFURLEnumeratorOptions, CFArray!) -> CFURLEnumerator!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFURLEnumeratorCreateForMountedVolumes(CFAllocator!, CFURLEnumeratorOptions, CFArray!) -> CFURLEnumerator!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFURLEnumeratorGetDescendentLevel(CFURLEnumerator!) -> CFIndex

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFURLEnumeratorGetNextURL(CFURLEnumerator!, UnsafeMutablePointer<Unmanaged<CFURL>?>, UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFURLEnumeratorResult

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFURLEnumeratorGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFURLEnumeratorSkipDescendents(CFURLEnumerator!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFURLIsFileReferenceURL(CFURL!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CFURLResourceIsReachable(CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFURLSetResourcePropertiesForKeys(CFURL!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFURLSetResourcePropertyForKey(CFURL!, CFString!, AnyObject!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFURLSetTemporaryResourcePropertyForKey(CFURL!, CFString!, AnyObject!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CFURLWriteBookmarkDataToFile(CFData!, CFURL!, CFURLBookmarkFileCreationOptions, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CFWriteStreamCopyDispatchQueue(CFWriteStream!) -> dispatch_queue_t!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CFWriteStreamCopyError(CFWriteStream!) -> CFError!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFWriteStreamSetDispatchQueue(CFWriteStream!, dispatch_queue_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCFDateFormatterDoesRelativeDateFormattingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFDateFormatterGregorianStartDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFDateFormatterLongEraSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFDateFormatterQuarterSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFDateFormatterShortQuarterSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFDateFormatterShortStandaloneMonthSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFDateFormatterShortStandaloneQuarterSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFDateFormatterShortStandaloneWeekdaySymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFDateFormatterStandaloneMonthSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFDateFormatterStandaloneQuarterSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFDateFormatterStandaloneWeekdaySymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFDateFormatterVeryShortMonthSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFDateFormatterVeryShortStandaloneMonthSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFDateFormatterVeryShortStandaloneWeekdaySymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFDateFormatterVeryShortWeekdaySymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFErrorDescriptionKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFErrorDomainCocoa

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFErrorDomainMach

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFErrorDomainOSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFErrorDomainPOSIX

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFErrorFilePathKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFErrorLocalizedDescriptionKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFErrorLocalizedFailureReasonKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFErrorLocalizedRecoverySuggestionKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFErrorURLKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFErrorUnderlyingErrorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFISO8601Calendar

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFIndianCalendar

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFLocaleAlternateQuotationBeginDelimiterKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFLocaleAlternateQuotationEndDelimiterKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFLocaleCollatorIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFLocaleCurrentLocaleDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFLocaleQuotationBeginDelimiterKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFLocaleQuotationEndDelimiterKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFNumberFormatterCurrencyGroupingSeparator

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFNumberFormatterIsLenient

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFNumberFormatterMaxSignificantDigits

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFNumberFormatterMinSignificantDigits

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFNumberFormatterUseSignificantDigits

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFPersianCalendar

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFRepublicOfChinaCalendar

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFSocketLeaveErrors

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStringTransformStripDiacritics

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFTimeZoneSystemTimeZoneDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFURLAttributeModificationDateKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLContentAccessDateKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLContentModificationDateKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLCreationDateKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLCustomIconKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLEffectiveIconKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLFileAllocatedSizeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLFileResourceIdentifierKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLFileResourceTypeBlockSpecial

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLFileResourceTypeCharacterSpecial

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLFileResourceTypeDirectory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLFileResourceTypeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLFileResourceTypeNamedPipe

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLFileResourceTypeRegular

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLFileResourceTypeSocket

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLFileResourceTypeSymbolicLink

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLFileResourceTypeUnknown

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLFileSecurityKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLFileSizeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLHasHiddenExtensionKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLIsAliasFileKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLIsDirectoryKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLIsExcludedFromBackupKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.1 |

Modified kCFURLIsExecutableKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLIsHiddenKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLIsMountTriggerKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLIsPackageKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLIsReadableKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLIsRegularFileKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLIsSymbolicLinkKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLIsSystemImmutableKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLIsUbiquitousItemKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLIsUserImmutableKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLIsVolumeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLIsWritableKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLKeysOfUnsetValuesKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLLabelColorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLLabelNumberKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLLinkCountKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLLocalizedLabelKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLLocalizedNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLLocalizedTypeDescriptionKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLParentDirectoryURLKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLPathKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCFURLPreferredIOBlockSizeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLTotalFileAllocatedSizeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLTotalFileSizeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLTypeIdentifierKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLUbiquitousItemDownloadingErrorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCFURLUbiquitousItemDownloadingStatusCurrent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCFURLUbiquitousItemDownloadingStatusDownloaded

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCFURLUbiquitousItemDownloadingStatusKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCFURLUbiquitousItemDownloadingStatusNotDownloaded

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCFURLUbiquitousItemHasUnresolvedConflictsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLUbiquitousItemIsDownloadingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLUbiquitousItemIsUploadedKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLUbiquitousItemIsUploadingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLUbiquitousItemUploadingErrorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCFURLVolumeAvailableCapacityKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLVolumeCreationDateKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLVolumeIdentifierKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLVolumeIsAutomountedKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLVolumeIsBrowsableKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLVolumeIsEjectableKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLVolumeIsInternalKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLVolumeIsJournalingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLVolumeIsLocalKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLVolumeIsReadOnlyKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLVolumeIsRemovableKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLVolumeLocalizedFormatDescriptionKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLVolumeLocalizedNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLVolumeMaximumFileSizeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLVolumeNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLVolumeResourceCountKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLVolumeSupportsAdvisoryFileLockingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLVolumeSupportsCasePreservedNamesKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLVolumeSupportsCaseSensitiveNamesKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLVolumeSupportsExtendedSecurityKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLVolumeSupportsHardLinksKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLVolumeSupportsJournalingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLVolumeSupportsPersistentIDsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLVolumeSupportsRenamingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLVolumeSupportsRootDirectoryDatesKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLVolumeSupportsSparseFilesKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLVolumeSupportsSymbolicLinksKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLVolumeSupportsVolumeSizesKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLVolumeSupportsZeroRunsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLVolumeTotalCapacityKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLVolumeURLForRemountingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFURLVolumeURLKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFURLVolumeUUIDStringKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

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
