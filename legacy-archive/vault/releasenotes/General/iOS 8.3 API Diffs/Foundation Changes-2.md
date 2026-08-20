---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/Foundation.html
archived_at: '2026-07-18T02:56:24.748902Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# Foundation Changes

## Foundation

Removed NSPredicate.init(fromMetadataQueryString: String)Removed NSSearchPathDirectory.ApplicationScriptsDirectoryRemoved NSSearchPathDirectory.TrashDirectoryRemoved NSURLBookmarkCreationOptions.PreferFileIDResolutionRemoved NSURLBookmarkCreationOptions.SecurityScopeAllowOnlyReadAccessRemoved NSURLBookmarkCreationOptions.WithSecurityScopeRemoved NSURLBookmarkResolutionOptions.WithSecurityScopeRemoved NSURLCredential.init(identity: SecIdentity!, certificates:[AnyObject], persistence: NSURLCredentialPersistence)Removed String.utf16CountAdded Index.init(_: Int)Added Index.advancedBy(Int) -> String.UTF16View.IndexAdded Index.distanceTo(String.UTF16View.Index) -> IntAdded NSArray.init(array: NSArray)Added NSDecimal [struct]Added NSDecimal.init()Added NSDecimalNumber.init(decimal: NSDecimal)Added NSDecimalNumber.decimalValueAdded NSDictionary.init(dictionary: NSDictionary)Added NSEnumerator.generate() -> NSFastGeneratorAdded NSFastEnumerationState.init(state: UInt, itemsPtr: AutoreleasingUnsafeMutablePointer<AnyObject?>, mutationsPtr: UnsafeMutablePointer<UInt>, extra:(UInt, UInt, UInt, UInt, UInt))Added NSIndexSet.generate() -> NSIndexSetGeneratorAdded NSIndexSetGenerator [struct]Added NSIndexSetGenerator.next() -> Int?Added NSIndexSetGenerator.init(set: NSIndexSet)Added NSNumber.decimalValueAdded NSOperatingSystemVersion.init()Added NSOperatingSystemVersion.init(majorVersion: Int, minorVersion: Int, patchVersion: Int)Added NSOrderedSet.init(arrayLiteral: AnyObject)Added NSOrderedSet.generate() -> NSFastGeneratorAdded NSSet.init(arrayLiteral: AnyObject)Added NSSet.init(set: Set<NSObject>)Added NSString.init(string: NSString)Added NSSwappedDouble.init()Added NSSwappedDouble.init(v: UInt64)Added NSSwappedFloat.init()Added NSSwappedFloat.init(v: UInt32)Added NSIndexSetGenerator.ElementModified NSCalendarOptions.MatchFirst

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSCalendarOptions.MatchLast

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSCalendarOptions.MatchNextTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSCalendarOptions.MatchNextTimePreservingSmallerUnits

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSCalendarOptions.MatchPreviousTimePreservingSmallerUnits

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSCalendarOptions.MatchStrictly

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSCalendarOptions.SearchBackwards

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSCalendarUnit.CalendarCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 8.0 |

Modified NSCalendarUnit.CalendarUnitCalendar

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSCalendarUnit.CalendarUnitNanosecond

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSCalendarUnit.CalendarUnitQuarter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSCalendarUnit.CalendarUnitTimeZone

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSCalendarUnit.CalendarUnitWeekOfMonth

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSCalendarUnit.CalendarUnitWeekOfYear

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSCalendarUnit.CalendarUnitYearForWeekOfYear

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSCalendarUnit.DayCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSCalendarUnit.EraCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSCalendarUnit.HourCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSCalendarUnit.MinuteCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSCalendarUnit.MonthCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSCalendarUnit.QuarterCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 8.0 |

Modified NSCalendarUnit.SecondCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSCalendarUnit.TimeZoneCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 8.0 |

Modified NSCalendarUnit.WeekCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSCalendarUnit.WeekOfMonthCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 5.0 | iOS 8.0 |

Modified NSCalendarUnit.WeekOfYearCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 5.0 | iOS 8.0 |

Modified NSCalendarUnit.WeekdayCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSCalendarUnit.WeekdayOrdinalCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSCalendarUnit.YearCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSCalendarUnit.YearForWeekOfYearCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 5.0 | iOS 8.0 |

Modified NSCoder.allowedClasses

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var allowedClasses: NSSet? { get } ``` |
| To | ``` var allowedClasses: Set<NSObject>? { get } ``` |

Modified NSCoder.decodeObjectOfClasses(Set<NSObject>, forKey: String) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func decodeObjectOfClasses(_ classes: NSSet, forKey key: String) -> AnyObject? ``` |
| To | ``` func decodeObjectOfClasses(_ classes: Set<NSObject>, forKey key: String) -> AnyObject? ``` |

Modified NSComparisonPredicateOptions.NormalizedPredicateOption

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSCountedSet.init(set: Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` convenience init(set set: NSSet) ``` | iOS 8.0 |
| To | ``` convenience init(set set: Set<NSObject>) ``` | iOS 8.3 |

Modified NSDataReadingOptions.DataReadingMappedAlways

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSDataWritingOptions.DataWritingFileProtectionComplete

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSDataWritingOptions.DataWritingFileProtectionCompleteUnlessOpen

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSDataWritingOptions.DataWritingFileProtectionCompleteUntilFirstUserAuthentication

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSDataWritingOptions.DataWritingFileProtectionMask

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSDataWritingOptions.DataWritingFileProtectionNone

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSDataWritingOptions.DataWritingWithoutOverwriting

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSDate.dateByAddingTimeInterval(NSTimeInterval) -> Self

|  | Declaration |
| --- | --- |
| From | ``` func dateByAddingTimeInterval(_ ti: NSTimeInterval) -> Self! ``` |
| To | ``` func dateByAddingTimeInterval(_ ti: NSTimeInterval) -> Self ``` |

Modified NSDateFormatter.dateFormatFromTemplate(String, options: Int, locale: NSLocale) -> String? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func dateFormatFromTemplate(_ tmplate: String, options opts: Int, locale locale: NSLocale?) -> String? ``` |
| To | ``` class func dateFormatFromTemplate(_ tmplate: String, options opts: Int, locale locale: NSLocale) -> String? ``` |

Modified NSDictionary.keysOfEntriesPassingTest((AnyObject!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject>

|  | Declaration |
| --- | --- |
| From | ``` func keysOfEntriesPassingTest(_ predicate: (AnyObject!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSSet ``` |
| To | ``` func keysOfEntriesPassingTest(_ predicate: (AnyObject!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject> ``` |

Modified NSDictionary.keysOfEntriesWithOptions(NSEnumerationOptions, passingTest:(AnyObject!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject>

|  | Declaration |
| --- | --- |
| From | ``` func keysOfEntriesWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSSet ``` |
| To | ``` func keysOfEntriesWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject> ``` |

Modified NSEnumerator

|  | Protocols |
| --- | --- |
| From | AnyObject, NSFastEnumeration |
| To | AnyObject, NSFastEnumeration, SequenceType |

Modified NSExpression.init(forAggregate: [AnyObject])

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSExpression.init(forBlock: (AnyObject!,[AnyObject]!, NSMutableDictionary!) -> AnyObject!, arguments:[AnyObject])

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSExpression.init(forFunction: NSExpression, selectorName: String, arguments:[AnyObject])

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSExpression.init(forIntersectSet: NSExpression, with: NSExpression)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSExpression.init(forMinusSet: NSExpression, with: NSExpression)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSExpression.init(forSubquery: NSExpression, usingIteratorVariable: String, predicate: AnyObject)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSExpression.init(forUnionSet: NSExpression, with: NSExpression)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSExpression.init(format: String, argumentArray:[AnyObject])

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSExpression.init(format: String, arguments: CVaListPointer)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSExpressionType.AggregateExpressionType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSExpressionType.AnyKeyExpressionType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSExpressionType.IntersectSetExpressionType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSExpressionType.MinusSetExpressionType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSExpressionType.SubqueryExpressionType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSExpressionType.UnionSetExpressionType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSFastEnumerationState [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSFastEnumerationState {     var state: UInt     var itemsPtr: AutoreleasingUnsafeMutablePointer<AnyObject?>     var mutationsPtr: UnsafeMutablePointer<UInt>     var extra: (UInt, UInt, UInt, UInt, UInt) } ``` |
| To | ``` struct NSFastEnumerationState {     var state: UInt     var itemsPtr: AutoreleasingUnsafeMutablePointer<AnyObject?>     var mutationsPtr: UnsafeMutablePointer<UInt>     var extra: (UInt, UInt, UInt, UInt, UInt)     init()     init(state state: UInt, itemsPtr itemsPtr: AutoreleasingUnsafeMutablePointer<AnyObject?>, mutationsPtr mutationsPtr: UnsafeMutablePointer<UInt>, extra extra: (UInt, UInt, UInt, UInt, UInt)) } ``` |

Modified NSFileAccessIntent.readingIntentWithURL(NSURL, options: NSFileCoordinatorReadingOptions) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func readingIntentWithURL(_ url: NSURL, options options: NSFileCoordinatorReadingOptions) -> Self! ``` | iOS 8.0 |
| To | ``` class func readingIntentWithURL(_ url: NSURL, options options: NSFileCoordinatorReadingOptions) -> Self ``` | iOS 8.3 |

Modified NSFileAccessIntent.writingIntentWithURL(NSURL, options: NSFileCoordinatorWritingOptions) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func writingIntentWithURL(_ url: NSURL, options options: NSFileCoordinatorWritingOptions) -> Self! ``` | iOS 8.0 |
| To | ``` class func writingIntentWithURL(_ url: NSURL, options options: NSFileCoordinatorWritingOptions) -> Self ``` | iOS 8.3 |

Modified NSFileHandle.init(forReadingFromURL: NSURL, error: NSErrorPointer)

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 4.0 |

Modified NSFileHandle.init(forUpdatingURL: NSURL, error: NSErrorPointer)

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 4.0 |

Modified NSFileHandle.init(forWritingToURL: NSURL, error: NSErrorPointer)

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 4.0 |

Modified NSHashTable.setRepresentation

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var setRepresentation: NSSet { get } ``` |
| To | ``` var setRepresentation: Set<NSObject> { get } ``` |

Modified NSIndexSet

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying, NSMutableCopying, NSSecureCoding |
| To | AnyObject, NSCoding, NSCopying, NSMutableCopying, NSSecureCoding, SequenceType |

Modified NSKeyValueObservingOptions.Initial

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSKeyValueObservingOptions.Prior

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSMutableDictionary.init(sharedKeySet: AnyObject)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSMutableOrderedSet.intersectSet(Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func intersectSet(_ other: NSSet) ``` | iOS 8.0 |
| To | ``` func intersectSet(_ other: Set<NSObject>) ``` | iOS 8.3 |

Modified NSMutableOrderedSet.minusSet(Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func minusSet(_ other: NSSet) ``` | iOS 8.0 |
| To | ``` func minusSet(_ other: Set<NSObject>) ``` | iOS 8.3 |

Modified NSMutableOrderedSet.unionSet(Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func unionSet(_ other: NSSet) ``` | iOS 8.0 |
| To | ``` func unionSet(_ other: Set<NSObject>) ``` | iOS 8.3 |

Modified NSMutableSet.intersectSet(Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func intersectSet(_ otherSet: NSSet) ``` | iOS 8.0 |
| To | ``` func intersectSet(_ otherSet: Set<NSObject>) ``` | iOS 8.3 |

Modified NSMutableSet.minusSet(Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func minusSet(_ otherSet: NSSet) ``` | iOS 8.0 |
| To | ``` func minusSet(_ otherSet: Set<NSObject>) ``` | iOS 8.3 |

Modified NSMutableSet.setSet(Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setSet(_ otherSet: NSSet) ``` | iOS 8.0 |
| To | ``` func setSet(_ otherSet: Set<NSObject>) ``` | iOS 8.3 |

Modified NSMutableSet.unionSet(Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func unionSet(_ otherSet: NSSet) ``` | iOS 8.0 |
| To | ``` func unionSet(_ otherSet: Set<NSObject>) ``` | iOS 8.3 |

Modified NSNetServiceOptions.ListenForConnections

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSNull

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | AnyObject, CAAction, NSCoding, NSCopying, NSSecureCoding |

Modified NSObject.didChangeValueForKey(String, withSetMutation: NSKeyValueSetMutationKind, usingObjects: Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func didChangeValueForKey(_ key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, usingObjects objects: NSSet) ``` | iOS 8.1 |
| To | ``` func didChangeValueForKey(_ key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, usingObjects objects: Set<NSObject>) ``` | iOS 8.3 |

Modified NSObject.keyPathsForValuesAffectingValueForKey(String) -> Set<NSObject> [class]

|  | Declaration |
| --- | --- |
| From | ``` class func keyPathsForValuesAffectingValueForKey(_ key: String) -> NSSet ``` |
| To | ``` class func keyPathsForValuesAffectingValueForKey(_ key: String) -> Set<NSObject> ``` |

Modified NSObject.willChangeValueForKey(String, withSetMutation: NSKeyValueSetMutationKind, usingObjects: Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func willChangeValueForKey(_ key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, usingObjects objects: NSSet) ``` | iOS 8.1 |
| To | ``` func willChangeValueForKey(_ key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, usingObjects objects: Set<NSObject>) ``` | iOS 8.3 |

Modified NSOperatingSystemVersion [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSOperatingSystemVersion {     var majorVersion: Int     var minorVersion: Int     var patchVersion: Int } ``` |
| To | ``` struct NSOperatingSystemVersion {     var majorVersion: Int     var minorVersion: Int     var patchVersion: Int     init()     init(majorVersion majorVersion: Int, minorVersion minorVersion: Int, patchVersion patchVersion: Int) } ``` |

Modified NSOrderedSet

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding |
| To | AnyObject, ArrayLiteralConvertible, NSCoding, NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding, SequenceType |

Modified NSOrderedSet.intersectsSet(Set<NSObject>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func intersectsSet(_ set: NSSet) -> Bool ``` | iOS 8.0 |
| To | ``` func intersectsSet(_ set: Set<NSObject>) -> Bool ``` | iOS 8.3 |

Modified NSOrderedSet.isSubsetOfSet(Set<NSObject>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func isSubsetOfSet(_ set: NSSet) -> Bool ``` | iOS 8.0 |
| To | ``` func isSubsetOfSet(_ set: Set<NSObject>) -> Bool ``` | iOS 8.3 |

Modified NSOrderedSet.set

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var set: NSSet { get } ``` |
| To | ``` var set: Set<NSObject> { get } ``` |

Modified NSOrderedSet.init(set: Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` convenience init(set set: NSSet) ``` | iOS 8.0 |
| To | ``` convenience init(set set: Set<NSObject>) ``` | iOS 8.3 |

Modified NSOrderedSet.init(set: Set<NSObject>, copyItems: Bool)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` convenience init(set set: NSSet, copyItems flag: Bool) ``` | iOS 8.0 |
| To | ``` convenience init(set set: Set<NSObject>, copyItems flag: Bool) ``` | iOS 8.3 |

Modified NSOrderedSet.init(set: Set<NSObject>?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` convenience init(set set: NSSet?) ``` | iOS 8.0 |
| To | ``` convenience init(set set: Set<NSObject>?) ``` | iOS 8.3 |

Modified NSOrderedSet.init(set: Set<NSObject>?, copyItems: Bool)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` convenience init(set set: NSSet?, copyItems flag: Bool) ``` | iOS 8.0 |
| To | ``` convenience init(set set: Set<NSObject>?, copyItems flag: Bool) ``` | iOS 8.3 |

Modified NSOutputStream.outputStreamToMemory() -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func outputStreamToMemory() -> Self! ``` | iOS 8.0 |
| To | ``` class func outputStreamToMemory() -> Self ``` | iOS 8.3 |

Modified NSPredicate.init(block: (AnyObject!,[NSObject: AnyObject]!) -> Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSPredicate.init(format: String, _: CVarArgType)

|  | Declaration |
| --- | --- |
| From | ``` convenience init?(format predicateFormat: String, _ args: CVarArgType...) ``` |
| To | ``` convenience init(format predicateFormat: String, _ args: CVarArgType...) ``` |

Modified NSPredicate.predicateWithSubstitutionVariables([NSObject: AnyObject]) -> Self

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func predicateWithSubstitutionVariables(_ variables: [NSObject : AnyObject]) -> Self! ``` | iOS 8.0 |
| To | ``` func predicateWithSubstitutionVariables(_ variables: [NSObject : AnyObject]) -> Self ``` | iOS 8.3 |

Modified NSPredicateOperatorType.BetweenPredicateOperatorType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSPredicateOperatorType.ContainsPredicateOperatorType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSProxy.alloc() -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func alloc() -> Self! ``` | iOS 8.0 |
| To | ``` class func alloc() -> Self ``` | iOS 8.3 |

Modified NSScanner.scanDecimal(UnsafeMutablePointer<NSDecimal>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func scanDecimal(_ dcm: COpaquePointer) -> Bool ``` | iOS 8.0 |
| To | ``` func scanDecimal(_ dcm: UnsafeMutablePointer<NSDecimal>) -> Bool ``` | iOS 8.3 |

Modified NSSearchPathDirectory.AutosavedInformationDirectory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSSearchPathDirectory.DownloadsDirectory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSSearchPathDirectory.InputMethodsDirectory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSSearchPathDirectory.ItemReplacementDirectory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSSearchPathDirectory.MoviesDirectory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSSearchPathDirectory.MusicDirectory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSSearchPathDirectory.PicturesDirectory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSSearchPathDirectory.PreferencePanesDirectory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSSearchPathDirectory.PrinterDescriptionDirectory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSSearchPathDirectory.SharedPublicDirectory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSSecureCoding.supportsSecureCoding() -> Bool [class]

|  | Declaration |
| --- | --- |
| From | ``` class func supportsSecureCoding() -> Bool ``` |
| To | ``` static func supportsSecureCoding() -> Bool ``` |

Modified NSSet

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding, Reflectable, SequenceType |
| To | AnyObject, ArrayLiteralConvertible, NSCoding, NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding, Reflectable, SequenceType |

Modified NSSet.filteredSetUsingPredicate(NSPredicate) -> Set<NSObject>

|  | Declaration |
| --- | --- |
| From | ``` func filteredSetUsingPredicate(_ predicate: NSPredicate) -> NSSet ``` |
| To | ``` func filteredSetUsingPredicate(_ predicate: NSPredicate) -> Set<NSObject> ``` |

Modified NSSet.intersectsSet(Set<NSObject>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func intersectsSet(_ otherSet: NSSet) -> Bool ``` | iOS 8.0 |
| To | ``` func intersectsSet(_ otherSet: Set<NSObject>) -> Bool ``` | iOS 8.3 |

Modified NSSet.isEqualToSet(Set<NSObject>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func isEqualToSet(_ otherSet: NSSet) -> Bool ``` | iOS 8.0 |
| To | ``` func isEqualToSet(_ otherSet: Set<NSObject>) -> Bool ``` | iOS 8.3 |

Modified NSSet.isSubsetOfSet(Set<NSObject>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func isSubsetOfSet(_ otherSet: NSSet) -> Bool ``` | iOS 8.0 |
| To | ``` func isSubsetOfSet(_ otherSet: Set<NSObject>) -> Bool ``` | iOS 8.3 |

Modified NSSet.objectsPassingTest((AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject>

|  | Declaration |
| --- | --- |
| From | ``` func objectsPassingTest(_ predicate: (AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSSet ``` |
| To | ``` func objectsPassingTest(_ predicate: (AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject> ``` |

Modified NSSet.objectsWithOptions(NSEnumerationOptions, passingTest:(AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject>

|  | Declaration |
| --- | --- |
| From | ``` func objectsWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSSet ``` |
| To | ``` func objectsWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject> ``` |

Modified NSSet.init(set: NSSet)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(set set: NSSet) ``` |
| To | ``` @objc(_swiftInitWithSet_NSSet:) convenience init(set anSet: NSSet) ``` |

Modified NSSet.init(set: Set<NSObject>, copyItems: Bool)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` convenience init(set set: NSSet, copyItems flag: Bool) ``` | iOS 8.0 |
| To | ``` convenience init(set set: Set<NSObject>, copyItems flag: Bool) ``` | iOS 8.3 |

Modified NSSet.setByAddingObject(AnyObject) -> Set<NSObject>

|  | Declaration |
| --- | --- |
| From | ``` func setByAddingObject(_ anObject: AnyObject) -> NSSet ``` |
| To | ``` func setByAddingObject(_ anObject: AnyObject) -> Set<NSObject> ``` |

Modified NSSet.setByAddingObjectsFromArray([AnyObject]) -> Set<NSObject>

|  | Declaration |
| --- | --- |
| From | ``` func setByAddingObjectsFromArray(_ other: [AnyObject]) -> NSSet ``` |
| To | ``` func setByAddingObjectsFromArray(_ other: [AnyObject]) -> Set<NSObject> ``` |

Modified NSSet.setByAddingObjectsFromSet(Set<NSObject>) -> Set<NSObject>

|  | Declaration |
| --- | --- |
| From | ``` func setByAddingObjectsFromSet(_ other: NSSet) -> NSSet ``` |
| To | ``` func setByAddingObjectsFromSet(_ other: Set<NSObject>) -> Set<NSObject> ``` |

Modified NSStringCompareOptions.DiacriticInsensitiveSearch

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSStringCompareOptions.ForcedOrderingSearch

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSStringCompareOptions.RegularExpressionSearch

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified NSStringCompareOptions.WidthInsensitiveSearch

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSSwappedDouble [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSSwappedDouble {     var v: UInt64 } ``` |
| To | ``` struct NSSwappedDouble {     var v: UInt64     init()     init(v v: UInt64) } ``` |

Modified NSSwappedFloat [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSSwappedFloat {     var v: UInt32 } ``` |
| To | ``` struct NSSwappedFloat {     var v: UInt32     init()     init(v v: UInt32) } ``` |

Modified NSTextCheckingType.PhoneNumber

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSTextCheckingType.RegularExpression

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSTextCheckingType.TransitInformation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURL.init(byResolvingAliasFileAtURL: NSURL, options: NSURLBookmarkResolutionOptions, error: NSErrorPointer)

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 8.0 |

Modified NSURLCredential.init(forTrust: SecTrust!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSURLCredential.init(identity: SecIdentity, certificates:[AnyObject], persistence: NSURLCredentialPersistence)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(identity identity: SecIdentity, certificates certArray: [AnyObject], persistence persistence: NSURLCredentialPersistence) -> NSURLCredential ``` | iOS 8.0 |
| To | ``` init(identity identity: SecIdentity, certificates certArray: [AnyObject], persistence persistence: NSURLCredentialPersistence) ``` | iOS 3.0 |

Modified NSURLCredentialPersistence.Synchronizable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSURLRequest.URL

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var URL: NSURL { get } ``` |
| To | ``` @NSCopying var URL: NSURL? { get } ``` |

Modified NSUserDefaults.init(suiteName: String?)

|  | Declaration |
| --- | --- |
| From | ``` init?(suiteName suitename: String) ``` |
| To | ``` init?(suiteName suitename: String?) ``` |

Modified NSXMLParser.allowedExternalEntityURLs

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var allowedExternalEntityURLs: NSSet? ``` |
| To | ``` var allowedExternalEntityURLs: Set<NSObject>? ``` |

Modified NSXMLParser.init(data: NSData)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(data data: NSData!) ``` | iOS 8.0 |
| To | ``` init(data data: NSData) ``` | iOS 8.3 |

Modified NSXMLParserDelegate.parser(NSXMLParser, didEndElement: String, namespaceURI: String?, qualifiedName: String?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, didEndElement elementName: String!, namespaceURI namespaceURI: String!, qualifiedName qName: String!) ``` | iOS 8.1 |
| To | ``` optional func parser(_ parser: NSXMLParser, didEndElement elementName: String, namespaceURI namespaceURI: String?, qualifiedName qName: String?) ``` | iOS 8.3 |

Modified NSXMLParserDelegate.parser(NSXMLParser, didEndMappingPrefix: String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, didEndMappingPrefix prefix: String!) ``` | iOS 8.1 |
| To | ``` optional func parser(_ parser: NSXMLParser, didEndMappingPrefix prefix: String) ``` | iOS 8.0 |

Modified NSXMLParserDelegate.parser(NSXMLParser, didStartElement: String, namespaceURI: String?, qualifiedName: String?, attributes:[NSObject: AnyObject])

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, didStartElement elementName: String!, namespaceURI namespaceURI: String!, qualifiedName qName: String!, attributes attributeDict: [NSObject : AnyObject]!) ``` | iOS 8.1 |
| To | ``` optional func parser(_ parser: NSXMLParser, didStartElement elementName: String, namespaceURI namespaceURI: String?, qualifiedName qName: String?, attributes attributeDict: [NSObject : AnyObject]) ``` | iOS 8.3 |

Modified NSXMLParserDelegate.parser(NSXMLParser, didStartMappingPrefix: String, toURI: String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, didStartMappingPrefix prefix: String!, toURI namespaceURI: String!) ``` | iOS 8.1 |
| To | ``` optional func parser(_ parser: NSXMLParser, didStartMappingPrefix prefix: String, toURI namespaceURI: String) ``` | iOS 8.3 |

Modified NSXMLParserDelegate.parser(NSXMLParser, foundAttributeDeclarationWithName: String, forElement: String, type: String?, defaultValue: String?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, foundAttributeDeclarationWithName attributeName: String!, forElement elementName: String!, type type: String!, defaultValue defaultValue: String!) ``` | iOS 8.1 |
| To | ``` optional func parser(_ parser: NSXMLParser, foundAttributeDeclarationWithName attributeName: String, forElement elementName: String, type type: String?, defaultValue defaultValue: String?) ``` | iOS 8.3 |

Modified NSXMLParserDelegate.parser(NSXMLParser, foundCDATA: NSData)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, foundCDATA CDATABlock: NSData!) ``` | iOS 8.1 |
| To | ``` optional func parser(_ parser: NSXMLParser, foundCDATA CDATABlock: NSData) ``` | iOS 8.0 |

Modified NSXMLParserDelegate.parser(NSXMLParser, foundCharacters: String?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, foundCharacters string: String!) ``` | iOS 8.1 |
| To | ``` optional func parser(_ parser: NSXMLParser, foundCharacters string: String?) ``` | iOS 8.3 |

Modified NSXMLParserDelegate.parser(NSXMLParser, foundComment: String?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, foundComment comment: String!) ``` | iOS 8.1 |
| To | ``` optional func parser(_ parser: NSXMLParser, foundComment comment: String?) ``` | iOS 8.3 |

Modified NSXMLParserDelegate.parser(NSXMLParser, foundElementDeclarationWithName: String, model: String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, foundElementDeclarationWithName elementName: String!, model model: String!) ``` | iOS 8.1 |
| To | ``` optional func parser(_ parser: NSXMLParser, foundElementDeclarationWithName elementName: String, model model: String) ``` | iOS 8.0 |

Modified NSXMLParserDelegate.parser(NSXMLParser, foundExternalEntityDeclarationWithName: String, publicID: String?, systemID: String?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, foundExternalEntityDeclarationWithName name: String!, publicID publicID: String!, systemID systemID: String!) ``` | iOS 8.1 |
| To | ``` optional func parser(_ parser: NSXMLParser, foundExternalEntityDeclarationWithName name: String, publicID publicID: String?, systemID systemID: String?) ``` | iOS 8.3 |

Modified NSXMLParserDelegate.parser(NSXMLParser, foundIgnorableWhitespace: String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, foundIgnorableWhitespace whitespaceString: String!) ``` | iOS 8.1 |
| To | ``` optional func parser(_ parser: NSXMLParser, foundIgnorableWhitespace whitespaceString: String) ``` | iOS 8.0 |

Modified NSXMLParserDelegate.parser(NSXMLParser, foundInternalEntityDeclarationWithName: String, value: String?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, foundInternalEntityDeclarationWithName name: String!, value value: String!) ``` | iOS 8.1 |
| To | ``` optional func parser(_ parser: NSXMLParser, foundInternalEntityDeclarationWithName name: String, value value: String?) ``` | iOS 8.3 |

Modified NSXMLParserDelegate.parser(NSXMLParser, foundNotationDeclarationWithName: String, publicID: String?, systemID: String?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, foundNotationDeclarationWithName name: String!, publicID publicID: String!, systemID systemID: String!) ``` | iOS 8.1 |
| To | ``` optional func parser(_ parser: NSXMLParser, foundNotationDeclarationWithName name: String, publicID publicID: String?, systemID systemID: String?) ``` | iOS 8.3 |

Modified NSXMLParserDelegate.parser(NSXMLParser, foundProcessingInstructionWithTarget: String, data: String?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, foundProcessingInstructionWithTarget target: String!, data data: String!) ``` | iOS 8.1 |
| To | ``` optional func parser(_ parser: NSXMLParser, foundProcessingInstructionWithTarget target: String, data data: String?) ``` | iOS 8.3 |

Modified NSXMLParserDelegate.parser(NSXMLParser, foundUnparsedEntityDeclarationWithName: String, publicID: String?, systemID: String?, notationName: String?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, foundUnparsedEntityDeclarationWithName name: String!, publicID publicID: String!, systemID systemID: String!, notationName notationName: String!) ``` | iOS 8.1 |
| To | ``` optional func parser(_ parser: NSXMLParser, foundUnparsedEntityDeclarationWithName name: String, publicID publicID: String?, systemID systemID: String?, notationName notationName: String?) ``` | iOS 8.3 |

Modified NSXMLParserDelegate.parser(NSXMLParser, parseErrorOccurred: NSError)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, parseErrorOccurred parseError: NSError!) ``` | iOS 8.1 |
| To | ``` optional func parser(_ parser: NSXMLParser, parseErrorOccurred parseError: NSError) ``` | iOS 8.0 |

Modified NSXMLParserDelegate.parser(NSXMLParser, resolveExternalEntityName: String, systemID: String?) -> NSData?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, resolveExternalEntityName name: String!, systemID systemID: String!) -> NSData! ``` | iOS 8.1 |
| To | ``` optional func parser(_ parser: NSXMLParser, resolveExternalEntityName name: String, systemID systemID: String?) -> NSData? ``` | iOS 8.0 |

Modified NSXMLParserDelegate.parser(NSXMLParser, validationErrorOccurred: NSError)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, validationErrorOccurred validationError: NSError!) ``` | iOS 8.1 |
| To | ``` optional func parser(_ parser: NSXMLParser, validationErrorOccurred validationError: NSError) ``` | iOS 8.0 |

Modified NSXMLParserDelegate.parserDidEndDocument(NSXMLParser)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parserDidEndDocument(_ parser: NSXMLParser!) ``` | iOS 8.1 |
| To | ``` optional func parserDidEndDocument(_ parser: NSXMLParser) ``` | iOS 8.0 |

Modified NSXMLParserDelegate.parserDidStartDocument(NSXMLParser)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parserDidStartDocument(_ parser: NSXMLParser!) ``` | iOS 8.1 |
| To | ``` optional func parserDidStartDocument(_ parser: NSXMLParser) ``` | iOS 8.0 |

Modified String.lowercaseString

|  | Module |
| --- | --- |
| From | Foundation |
| To | Swift |

Modified String.uppercaseString

|  | Module |
| --- | --- |
| From | Foundation |
| To | Swift |

Modified NSArgumentDomain

|  | Declaration |
| --- | --- |
| From | ``` let NSArgumentDomain: NSString! ``` |
| To | ``` let NSArgumentDomain: String ``` |

Modified NSAssertionHandlerKey

|  | Declaration |
| --- | --- |
| From | ``` let NSAssertionHandlerKey: NSString! ``` |
| To | ``` let NSAssertionHandlerKey: String ``` |

Modified NSAverageKeyValueOperator

|  | Declaration |
| --- | --- |
| From | ``` let NSAverageKeyValueOperator: NSString! ``` |
| To | ``` let NSAverageKeyValueOperator: String ``` |

Modified NSBuddhistCalendar

|  | Declaration |
| --- | --- |
| From | ``` let NSBuddhistCalendar: NSString! ``` |
| To | ``` let NSBuddhistCalendar: String ``` |

Modified NSBundleDidLoadNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSBundleDidLoadNotification: NSString! ``` |
| To | ``` let NSBundleDidLoadNotification: String ``` |

Modified NSCalendarDayChangedNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSCalendarDayChangedNotification: NSString! ``` |
| To | ``` let NSCalendarDayChangedNotification: String ``` |

Modified NSCalendarIdentifierBuddhist

|  | Declaration |
| --- | --- |
| From | ``` let NSCalendarIdentifierBuddhist: NSString! ``` |
| To | ``` let NSCalendarIdentifierBuddhist: String ``` |

Modified NSCalendarIdentifierChinese

|  | Declaration |
| --- | --- |
| From | ``` let NSCalendarIdentifierChinese: NSString! ``` |
| To | ``` let NSCalendarIdentifierChinese: String ``` |

Modified NSCalendarIdentifierCoptic

|  | Declaration |
| --- | --- |
| From | ``` let NSCalendarIdentifierCoptic: NSString! ``` |
| To | ``` let NSCalendarIdentifierCoptic: String ``` |

Modified NSCalendarIdentifierEthiopicAmeteAlem

|  | Declaration |
| --- | --- |
| From | ``` let NSCalendarIdentifierEthiopicAmeteAlem: NSString! ``` |
| To | ``` let NSCalendarIdentifierEthiopicAmeteAlem: String ``` |

Modified NSCalendarIdentifierEthiopicAmeteMihret

|  | Declaration |
| --- | --- |
| From | ``` let NSCalendarIdentifierEthiopicAmeteMihret: NSString! ``` |
| To | ``` let NSCalendarIdentifierEthiopicAmeteMihret: String ``` |

Modified NSCalendarIdentifierGregorian

|  | Declaration |
| --- | --- |
| From | ``` let NSCalendarIdentifierGregorian: NSString! ``` |
| To | ``` let NSCalendarIdentifierGregorian: String ``` |

Modified NSCalendarIdentifierHebrew

|  | Declaration |
| --- | --- |
| From | ``` let NSCalendarIdentifierHebrew: NSString! ``` |
| To | ``` let NSCalendarIdentifierHebrew: String ``` |

Modified NSCalendarIdentifierISO8601

|  | Declaration |
| --- | --- |
| From | ``` let NSCalendarIdentifierISO8601: NSString! ``` |
| To | ``` let NSCalendarIdentifierISO8601: String ``` |

Modified NSCalendarIdentifierIndian

|  | Declaration |
| --- | --- |
| From | ``` let NSCalendarIdentifierIndian: NSString! ``` |
| To | ``` let NSCalendarIdentifierIndian: String ``` |

Modified NSCalendarIdentifierIslamic

|  | Declaration |
| --- | --- |
| From | ``` let NSCalendarIdentifierIslamic: NSString! ``` |
| To | ``` let NSCalendarIdentifierIslamic: String ``` |

Modified NSCalendarIdentifierIslamicCivil

|  | Declaration |
| --- | --- |
| From | ``` let NSCalendarIdentifierIslamicCivil: NSString! ``` |
| To | ``` let NSCalendarIdentifierIslamicCivil: String ``` |

Modified NSCalendarIdentifierIslamicTabular

|  | Declaration |
| --- | --- |
| From | ``` let NSCalendarIdentifierIslamicTabular: NSString! ``` |
| To | ``` let NSCalendarIdentifierIslamicTabular: String ``` |

Modified NSCalendarIdentifierIslamicUmmAlQura

|  | Declaration |
| --- | --- |
| From | ``` let NSCalendarIdentifierIslamicUmmAlQura: NSString! ``` |
| To | ``` let NSCalendarIdentifierIslamicUmmAlQura: String ``` |

Modified NSCalendarIdentifierJapanese

|  | Declaration |
| --- | --- |
| From | ``` let NSCalendarIdentifierJapanese: NSString! ``` |
| To | ``` let NSCalendarIdentifierJapanese: String ``` |

Modified NSCalendarIdentifierPersian

|  | Declaration |
| --- | --- |
| From | ``` let NSCalendarIdentifierPersian: NSString! ``` |
| To | ``` let NSCalendarIdentifierPersian: String ``` |

Modified NSCalendarIdentifierRepublicOfChina

|  | Declaration |
| --- | --- |
| From | ``` let NSCalendarIdentifierRepublicOfChina: NSString! ``` |
| To | ``` let NSCalendarIdentifierRepublicOfChina: String ``` |

Modified NSCharacterConversionException

|  | Declaration |
| --- | --- |
| From | ``` let NSCharacterConversionException: NSString! ``` |
| To | ``` let NSCharacterConversionException: String ``` |

Modified NSChineseCalendar

|  | Declaration |
| --- | --- |
| From | ``` let NSChineseCalendar: NSString! ``` |
| To | ``` let NSChineseCalendar: String ``` |

Modified NSCocoaErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let NSCocoaErrorDomain: NSString! ``` |
| To | ``` let NSCocoaErrorDomain: String ``` |

Modified NSCountKeyValueOperator

|  | Declaration |
| --- | --- |
| From | ``` let NSCountKeyValueOperator: NSString! ``` |
| To | ``` let NSCountKeyValueOperator: String ``` |

Modified NSCurrentLocaleDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSCurrentLocaleDidChangeNotification: NSString! ``` |
| To | ``` let NSCurrentLocaleDidChangeNotification: String ``` |

Modified NSDecimalAdd(UnsafeMutablePointer<NSDecimal>, UnsafePointer<NSDecimal>, UnsafePointer<NSDecimal>, NSRoundingMode) -> NSCalculationError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NSDecimalAdd(_ result: COpaquePointer, _ leftOperand: COpaquePointer, _ rightOperand: COpaquePointer, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | iOS 8.0 |
| To | ``` func NSDecimalAdd(_ result: UnsafeMutablePointer<NSDecimal>, _ leftOperand: UnsafePointer<NSDecimal>, _ rightOperand: UnsafePointer<NSDecimal>, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | iOS 8.3 |

Modified NSDecimalCompact(UnsafeMutablePointer<NSDecimal>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NSDecimalCompact(_ number: COpaquePointer) ``` | iOS 8.0 |
| To | ``` func NSDecimalCompact(_ number: UnsafeMutablePointer<NSDecimal>) ``` | iOS 8.3 |

Modified NSDecimalCompare(UnsafePointer<NSDecimal>, UnsafePointer<NSDecimal>) -> NSComparisonResult

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NSDecimalCompare(_ leftOperand: COpaquePointer, _ rightOperand: COpaquePointer) -> NSComparisonResult ``` | iOS 8.0 |
| To | ``` func NSDecimalCompare(_ leftOperand: UnsafePointer<NSDecimal>, _ rightOperand: UnsafePointer<NSDecimal>) -> NSComparisonResult ``` | iOS 8.3 |

Modified NSDecimalCopy(UnsafeMutablePointer<NSDecimal>, UnsafePointer<NSDecimal>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NSDecimalCopy(_ destination: COpaquePointer, _ source: COpaquePointer) ``` | iOS 8.0 |
| To | ``` func NSDecimalCopy(_ destination: UnsafeMutablePointer<NSDecimal>, _ source: UnsafePointer<NSDecimal>) ``` | iOS 8.3 |

Modified NSDecimalDivide(UnsafeMutablePointer<NSDecimal>, UnsafePointer<NSDecimal>, UnsafePointer<NSDecimal>, NSRoundingMode) -> NSCalculationError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NSDecimalDivide(_ result: COpaquePointer, _ leftOperand: COpaquePointer, _ rightOperand: COpaquePointer, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | iOS 8.0 |
| To | ``` func NSDecimalDivide(_ result: UnsafeMutablePointer<NSDecimal>, _ leftOperand: UnsafePointer<NSDecimal>, _ rightOperand: UnsafePointer<NSDecimal>, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | iOS 8.3 |

Modified NSDecimalIsNotANumber(UnsafePointer<NSDecimal>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NSDecimalIsNotANumber(_ dcm: COpaquePointer) -> Bool ``` | iOS 8.0 |
| To | ``` func NSDecimalIsNotANumber(_ dcm: UnsafePointer<NSDecimal>) -> Bool ``` | iOS 8.3 |

Modified NSDecimalMultiply(UnsafeMutablePointer<NSDecimal>, UnsafePointer<NSDecimal>, UnsafePointer<NSDecimal>, NSRoundingMode) -> NSCalculationError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NSDecimalMultiply(_ result: COpaquePointer, _ leftOperand: COpaquePointer, _ rightOperand: COpaquePointer, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | iOS 8.0 |
| To | ``` func NSDecimalMultiply(_ result: UnsafeMutablePointer<NSDecimal>, _ leftOperand: UnsafePointer<NSDecimal>, _ rightOperand: UnsafePointer<NSDecimal>, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | iOS 8.3 |

Modified NSDecimalMultiplyByPowerOf10(UnsafeMutablePointer<NSDecimal>, UnsafePointer<NSDecimal>, Int16, NSRoundingMode) -> NSCalculationError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NSDecimalMultiplyByPowerOf10(_ result: COpaquePointer, _ number: COpaquePointer, _ power: Int16, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | iOS 8.0 |
| To | ``` func NSDecimalMultiplyByPowerOf10(_ result: UnsafeMutablePointer<NSDecimal>, _ number: UnsafePointer<NSDecimal>, _ power: Int16, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | iOS 8.3 |

Modified NSDecimalNormalize(UnsafeMutablePointer<NSDecimal>, UnsafeMutablePointer<NSDecimal>, NSRoundingMode) -> NSCalculationError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NSDecimalNormalize(_ number1: COpaquePointer, _ number2: COpaquePointer, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | iOS 8.0 |
| To | ``` func NSDecimalNormalize(_ number1: UnsafeMutablePointer<NSDecimal>, _ number2: UnsafeMutablePointer<NSDecimal>, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | iOS 8.3 |

Modified NSDecimalNumberDivideByZeroException

|  | Declaration |
| --- | --- |
| From | ``` let NSDecimalNumberDivideByZeroException: NSString! ``` |
| To | ``` let NSDecimalNumberDivideByZeroException: String ``` |

Modified NSDecimalNumberExactnessException

|  | Declaration |
| --- | --- |
| From | ``` let NSDecimalNumberExactnessException: NSString! ``` |
| To | ``` let NSDecimalNumberExactnessException: String ``` |

Modified NSDecimalNumberOverflowException

|  | Declaration |
| --- | --- |
| From | ``` let NSDecimalNumberOverflowException: NSString! ``` |
| To | ``` let NSDecimalNumberOverflowException: String ``` |

Modified NSDecimalNumberUnderflowException

|  | Declaration |
| --- | --- |
| From | ``` let NSDecimalNumberUnderflowException: NSString! ``` |
| To | ``` let NSDecimalNumberUnderflowException: String ``` |

Modified NSDecimalPower(UnsafeMutablePointer<NSDecimal>, UnsafePointer<NSDecimal>, Int, NSRoundingMode) -> NSCalculationError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NSDecimalPower(_ result: COpaquePointer, _ number: COpaquePointer, _ power: Int, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | iOS 8.0 |
| To | ``` func NSDecimalPower(_ result: UnsafeMutablePointer<NSDecimal>, _ number: UnsafePointer<NSDecimal>, _ power: Int, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | iOS 8.3 |

Modified NSDecimalRound(UnsafeMutablePointer<NSDecimal>, UnsafePointer<NSDecimal>, Int, NSRoundingMode)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NSDecimalRound(_ result: COpaquePointer, _ number: COpaquePointer, _ scale: Int, _ roundingMode: NSRoundingMode) ``` | iOS 8.0 |
| To | ``` func NSDecimalRound(_ result: UnsafeMutablePointer<NSDecimal>, _ number: UnsafePointer<NSDecimal>, _ scale: Int, _ roundingMode: NSRoundingMode) ``` | iOS 8.3 |

Modified NSDecimalString(UnsafePointer<NSDecimal>, AnyObject!) -> String!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NSDecimalString(_ dcm: COpaquePointer, _ locale: AnyObject!) -> String! ``` | iOS 8.0 |
| To | ``` func NSDecimalString(_ dcm: UnsafePointer<NSDecimal>, _ locale: AnyObject!) -> String! ``` | iOS 8.3 |

Modified NSDecimalSubtract(UnsafeMutablePointer<NSDecimal>, UnsafePointer<NSDecimal>, UnsafePointer<NSDecimal>, NSRoundingMode) -> NSCalculationError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NSDecimalSubtract(_ result: COpaquePointer, _ leftOperand: COpaquePointer, _ rightOperand: COpaquePointer, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | iOS 8.0 |
| To | ``` func NSDecimalSubtract(_ result: UnsafeMutablePointer<NSDecimal>, _ leftOperand: UnsafePointer<NSDecimal>, _ rightOperand: UnsafePointer<NSDecimal>, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | iOS 8.3 |

Modified NSDefaultRunLoopMode

|  | Declaration |
| --- | --- |
| From | ``` let NSDefaultRunLoopMode: NSString! ``` |
| To | ``` let NSDefaultRunLoopMode: String ``` |

Modified NSDestinationInvalidException

|  | Declaration |
| --- | --- |
| From | ``` let NSDestinationInvalidException: NSString! ``` |
| To | ``` let NSDestinationInvalidException: String ``` |

Modified NSDidBecomeSingleThreadedNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSDidBecomeSingleThreadedNotification: NSString! ``` |
| To | ``` let NSDidBecomeSingleThreadedNotification: String ``` |

Modified NSDistinctUnionOfArraysKeyValueOperator

|  | Declaration |
| --- | --- |
| From | ``` let NSDistinctUnionOfArraysKeyValueOperator: NSString! ``` |
| To | ``` let NSDistinctUnionOfArraysKeyValueOperator: String ``` |

Modified NSDistinctUnionOfObjectsKeyValueOperator

|  | Declaration |
| --- | --- |
| From | ``` let NSDistinctUnionOfObjectsKeyValueOperator: NSString! ``` |
| To | ``` let NSDistinctUnionOfObjectsKeyValueOperator: String ``` |

Modified NSDistinctUnionOfSetsKeyValueOperator

|  | Declaration |
| --- | --- |
| From | ``` let NSDistinctUnionOfSetsKeyValueOperator: NSString! ``` |
| To | ``` let NSDistinctUnionOfSetsKeyValueOperator: String ``` |

Modified NSExtensionHostDidBecomeActiveNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSExtensionHostDidBecomeActiveNotification: NSString! ``` |
| To | ``` let NSExtensionHostDidBecomeActiveNotification: String ``` |

Modified NSExtensionHostDidEnterBackgroundNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSExtensionHostDidEnterBackgroundNotification: NSString! ``` |
| To | ``` let NSExtensionHostDidEnterBackgroundNotification: String ``` |

Modified NSExtensionHostWillEnterForegroundNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSExtensionHostWillEnterForegroundNotification: NSString! ``` |
| To | ``` let NSExtensionHostWillEnterForegroundNotification: String ``` |

Modified NSExtensionHostWillResignActiveNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSExtensionHostWillResignActiveNotification: NSString! ``` |
| To | ``` let NSExtensionHostWillResignActiveNotification: String ``` |

Modified NSExtensionItemAttachmentsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSExtensionItemAttachmentsKey: NSString! ``` |
| To | ``` let NSExtensionItemAttachmentsKey: String ``` |

Modified NSExtensionItemAttributedContentTextKey

|  | Declaration |
| --- | --- |
| From | ``` let NSExtensionItemAttributedContentTextKey: NSString! ``` |
| To | ``` let NSExtensionItemAttributedContentTextKey: String ``` |

Modified NSExtensionItemAttributedTitleKey

|  | Declaration |
| --- | --- |
| From | ``` let NSExtensionItemAttributedTitleKey: NSString! ``` |
| To | ``` let NSExtensionItemAttributedTitleKey: String ``` |

Modified NSExtensionItemsAndErrorsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSExtensionItemsAndErrorsKey: NSString! ``` |
| To | ``` let NSExtensionItemsAndErrorsKey: String ``` |

Modified NSExtensionJavaScriptFinalizeArgumentKey

|  | Declaration |
| --- | --- |
| From | ``` let NSExtensionJavaScriptFinalizeArgumentKey: NSString! ``` |
| To | ``` let NSExtensionJavaScriptFinalizeArgumentKey: String ``` |

Modified NSExtensionJavaScriptPreprocessingResultsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSExtensionJavaScriptPreprocessingResultsKey: NSString! ``` |
| To | ``` let NSExtensionJavaScriptPreprocessingResultsKey: String ``` |

Modified NSFileAppendOnly

|  | Declaration |
| --- | --- |
| From | ``` let NSFileAppendOnly: NSString! ``` |
| To | ``` let NSFileAppendOnly: String ``` |

Modified NSFileBusy

|  | Declaration |
| --- | --- |
| From | ``` let NSFileBusy: NSString! ``` |
| To | ``` let NSFileBusy: String ``` |

Modified NSFileCreationDate

|  | Declaration |
| --- | --- |
| From | ``` let NSFileCreationDate: NSString! ``` |
| To | ``` let NSFileCreationDate: String ``` |

Modified NSFileDeviceIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let NSFileDeviceIdentifier: NSString! ``` |
| To | ``` let NSFileDeviceIdentifier: String ``` |

Modified NSFileExtensionHidden

|  | Declaration |
| --- | --- |
| From | ``` let NSFileExtensionHidden: NSString! ``` |
| To | ``` let NSFileExtensionHidden: String ``` |

Modified NSFileGroupOwnerAccountID

|  | Declaration |
| --- | --- |
| From | ``` let NSFileGroupOwnerAccountID: NSString! ``` |
| To | ``` let NSFileGroupOwnerAccountID: String ``` |

Modified NSFileGroupOwnerAccountName

|  | Declaration |
| --- | --- |
| From | ``` let NSFileGroupOwnerAccountName: NSString! ``` |
| To | ``` let NSFileGroupOwnerAccountName: String ``` |

Modified NSFileHFSCreatorCode

|  | Declaration |
| --- | --- |
| From | ``` let NSFileHFSCreatorCode: NSString! ``` |
| To | ``` let NSFileHFSCreatorCode: String ``` |

Modified NSFileHFSTypeCode

|  | Declaration |
| --- | --- |
| From | ``` let NSFileHFSTypeCode: NSString! ``` |
| To | ``` let NSFileHFSTypeCode: String ``` |

Modified NSFileHandleConnectionAcceptedNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSFileHandleConnectionAcceptedNotification: NSString! ``` |
| To | ``` let NSFileHandleConnectionAcceptedNotification: String ``` |

Modified NSFileHandleDataAvailableNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSFileHandleDataAvailableNotification: NSString! ``` |
| To | ``` let NSFileHandleDataAvailableNotification: String ``` |

Modified NSFileHandleNotificationDataItem

|  | Declaration |
| --- | --- |
| From | ``` let NSFileHandleNotificationDataItem: NSString! ``` |
| To | ``` let NSFileHandleNotificationDataItem: String ``` |

Modified NSFileHandleNotificationFileHandleItem

|  | Declaration |
| --- | --- |
| From | ``` let NSFileHandleNotificationFileHandleItem: NSString! ``` |
| To | ``` let NSFileHandleNotificationFileHandleItem: String ``` |

Modified NSFileHandleOperationException

|  | Declaration |
| --- | --- |
| From | ``` let NSFileHandleOperationException: NSString! ``` |
| To | ``` let NSFileHandleOperationException: String ``` |

Modified NSFileHandleReadCompletionNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSFileHandleReadCompletionNotification: NSString! ``` |
| To | ``` let NSFileHandleReadCompletionNotification: String ``` |

Modified NSFileHandleReadToEndOfFileCompletionNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSFileHandleReadToEndOfFileCompletionNotification: NSString! ``` |
| To | ``` let NSFileHandleReadToEndOfFileCompletionNotification: String ``` |

Modified NSFileImmutable

|  | Declaration |
| --- | --- |
| From | ``` let NSFileImmutable: NSString! ``` |
| To | ``` let NSFileImmutable: String ``` |

Modified NSFileModificationDate

|  | Declaration |
| --- | --- |
| From | ``` let NSFileModificationDate: NSString! ``` |
| To | ``` let NSFileModificationDate: String ``` |

Modified NSFileOwnerAccountID

|  | Declaration |
| --- | --- |
| From | ``` let NSFileOwnerAccountID: NSString! ``` |
| To | ``` let NSFileOwnerAccountID: String ``` |

Modified NSFileOwnerAccountName

|  | Declaration |
| --- | --- |
| From | ``` let NSFileOwnerAccountName: NSString! ``` |
| To | ``` let NSFileOwnerAccountName: String ``` |

Modified NSFilePathErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSFilePathErrorKey: NSString! ``` |
| To | ``` let NSFilePathErrorKey: String ``` |

Modified NSFilePosixPermissions

|  | Declaration |
| --- | --- |
| From | ``` let NSFilePosixPermissions: NSString! ``` |
| To | ``` let NSFilePosixPermissions: String ``` |

Modified NSFileProtectionComplete

|  | Declaration |
| --- | --- |
| From | ``` let NSFileProtectionComplete: NSString! ``` |
| To | ``` let NSFileProtectionComplete: String ``` |

Modified NSFileProtectionCompleteUnlessOpen

|  | Declaration |
| --- | --- |
| From | ``` let NSFileProtectionCompleteUnlessOpen: NSString! ``` |
| To | ``` let NSFileProtectionCompleteUnlessOpen: String ``` |

Modified NSFileProtectionCompleteUntilFirstUserAuthentication

|  | Declaration |
| --- | --- |
| From | ``` let NSFileProtectionCompleteUntilFirstUserAuthentication: NSString! ``` |
| To | ``` let NSFileProtectionCompleteUntilFirstUserAuthentication: String ``` |

Modified NSFileProtectionKey

|  | Declaration |
| --- | --- |
| From | ``` let NSFileProtectionKey: NSString! ``` |
| To | ``` let NSFileProtectionKey: String ``` |

Modified NSFileProtectionNone

|  | Declaration |
| --- | --- |
| From | ``` let NSFileProtectionNone: NSString! ``` |
| To | ``` let NSFileProtectionNone: String ``` |

Modified NSFileReferenceCount

|  | Declaration |
| --- | --- |
| From | ``` let NSFileReferenceCount: NSString! ``` |
| To | ``` let NSFileReferenceCount: String ``` |

Modified NSFileSize

|  | Declaration |
| --- | --- |
| From | ``` let NSFileSize: NSString! ``` |
| To | ``` let NSFileSize: String ``` |

Modified NSFileSystemFileNumber

|  | Declaration |
| --- | --- |
| From | ``` let NSFileSystemFileNumber: NSString! ``` |
| To | ``` let NSFileSystemFileNumber: String ``` |

Modified NSFileSystemFreeNodes

|  | Declaration |
| --- | --- |
| From | ``` let NSFileSystemFreeNodes: NSString! ``` |
| To | ``` let NSFileSystemFreeNodes: String ``` |

Modified NSFileSystemFreeSize

|  | Declaration |
| --- | --- |
| From | ``` let NSFileSystemFreeSize: NSString! ``` |
| To | ``` let NSFileSystemFreeSize: String ``` |

Modified NSFileSystemNodes

|  | Declaration |
| --- | --- |
| From | ``` let NSFileSystemNodes: NSString! ``` |
| To | ``` let NSFileSystemNodes: String ``` |

Modified NSFileSystemNumber

|  | Declaration |
| --- | --- |
| From | ``` let NSFileSystemNumber: NSString! ``` |
| To | ``` let NSFileSystemNumber: String ``` |

Modified NSFileSystemSize

|  | Declaration |
| --- | --- |
| From | ``` let NSFileSystemSize: NSString! ``` |
| To | ``` let NSFileSystemSize: String ``` |

Modified NSFileType

|  | Declaration |
| --- | --- |
| From | ``` let NSFileType: NSString! ``` |
| To | ``` let NSFileType: String ``` |

Modified NSFileTypeBlockSpecial

|  | Declaration |
| --- | --- |
| From | ``` let NSFileTypeBlockSpecial: NSString! ``` |
| To | ``` let NSFileTypeBlockSpecial: String ``` |

Modified NSFileTypeCharacterSpecial

|  | Declaration |
| --- | --- |
| From | ``` let NSFileTypeCharacterSpecial: NSString! ``` |
| To | ``` let NSFileTypeCharacterSpecial: String ``` |

Modified NSFileTypeDirectory

|  | Declaration |
| --- | --- |
| From | ``` let NSFileTypeDirectory: NSString! ``` |
| To | ``` let NSFileTypeDirectory: String ``` |

Modified NSFileTypeRegular

|  | Declaration |
| --- | --- |
| From | ``` let NSFileTypeRegular: NSString! ``` |
| To | ``` let NSFileTypeRegular: String ``` |

Modified NSFileTypeSocket

|  | Declaration |
| --- | --- |
| From | ``` let NSFileTypeSocket: NSString! ``` |
| To | ``` let NSFileTypeSocket: String ``` |

Modified NSFileTypeSymbolicLink

|  | Declaration |
| --- | --- |
| From | ``` let NSFileTypeSymbolicLink: NSString! ``` |
| To | ``` let NSFileTypeSymbolicLink: String ``` |

Modified NSFileTypeUnknown

|  | Declaration |
| --- | --- |
| From | ``` let NSFileTypeUnknown: NSString! ``` |
| To | ``` let NSFileTypeUnknown: String ``` |

Modified NSGenericException

|  | Declaration |
| --- | --- |
| From | ``` let NSGenericException: NSString! ``` |
| To | ``` let NSGenericException: String ``` |

Modified NSGlobalDomain

|  | Declaration |
| --- | --- |
| From | ``` let NSGlobalDomain: NSString! ``` |
| To | ``` let NSGlobalDomain: String ``` |

Modified NSGregorianCalendar

|  | Declaration |
| --- | --- |
| From | ``` let NSGregorianCalendar: NSString! ``` |
| To | ``` let NSGregorianCalendar: String ``` |

Modified NSHTTPCookieComment

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookieComment: NSString! ``` |
| To | ``` let NSHTTPCookieComment: String ``` |

Modified NSHTTPCookieCommentURL

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookieCommentURL: NSString! ``` |
| To | ``` let NSHTTPCookieCommentURL: String ``` |

Modified NSHTTPCookieDiscard

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookieDiscard: NSString! ``` |
| To | ``` let NSHTTPCookieDiscard: String ``` |

Modified NSHTTPCookieDomain

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookieDomain: NSString! ``` |
| To | ``` let NSHTTPCookieDomain: String ``` |

Modified NSHTTPCookieExpires

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookieExpires: NSString! ``` |
| To | ``` let NSHTTPCookieExpires: String ``` |

Modified NSHTTPCookieManagerAcceptPolicyChangedNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookieManagerAcceptPolicyChangedNotification: NSString! ``` |
| To | ``` let NSHTTPCookieManagerAcceptPolicyChangedNotification: String ``` |

Modified NSHTTPCookieManagerCookiesChangedNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookieManagerCookiesChangedNotification: NSString! ``` |
| To | ``` let NSHTTPCookieManagerCookiesChangedNotification: String ``` |

Modified NSHTTPCookieMaximumAge

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookieMaximumAge: NSString! ``` |
| To | ``` let NSHTTPCookieMaximumAge: String ``` |

Modified NSHTTPCookieName

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookieName: NSString! ``` |
| To | ``` let NSHTTPCookieName: String ``` |

Modified NSHTTPCookieOriginURL

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookieOriginURL: NSString! ``` |
| To | ``` let NSHTTPCookieOriginURL: String ``` |

Modified NSHTTPCookiePath

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookiePath: NSString! ``` |
| To | ``` let NSHTTPCookiePath: String ``` |

Modified NSHTTPCookiePort

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookiePort: NSString! ``` |
| To | ``` let NSHTTPCookiePort: String ``` |

Modified NSHTTPCookieSecure

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookieSecure: NSString! ``` |
| To | ``` let NSHTTPCookieSecure: String ``` |

Modified NSHTTPCookieValue

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookieValue: NSString! ``` |
| To | ``` let NSHTTPCookieValue: String ``` |

Modified NSHTTPCookieVersion

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookieVersion: NSString! ``` |
| To | ``` let NSHTTPCookieVersion: String ``` |

Modified NSHebrewCalendar

|  | Declaration |
| --- | --- |
| From | ``` let NSHebrewCalendar: NSString! ``` |
| To | ``` let NSHebrewCalendar: String ``` |

Modified NSHelpAnchorErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSHelpAnchorErrorKey: NSString! ``` |
| To | ``` let NSHelpAnchorErrorKey: String ``` |

Modified NSISO8601Calendar

|  | Declaration |
| --- | --- |
| From | ``` let NSISO8601Calendar: NSString! ``` |
| To | ``` let NSISO8601Calendar: String ``` |

Modified NSIndianCalendar

|  | Declaration |
| --- | --- |
| From | ``` let NSIndianCalendar: NSString! ``` |
| To | ``` let NSIndianCalendar: String ``` |

Modified NSInternalInconsistencyException

|  | Declaration |
| --- | --- |
| From | ``` let NSInternalInconsistencyException: NSString! ``` |
| To | ``` let NSInternalInconsistencyException: String ``` |

Modified NSInvalidArchiveOperationException

|  | Declaration |
| --- | --- |
| From | ``` let NSInvalidArchiveOperationException: NSString! ``` |
| To | ``` let NSInvalidArchiveOperationException: String ``` |

Modified NSInvalidArgumentException

|  | Declaration |
| --- | --- |
| From | ``` let NSInvalidArgumentException: NSString! ``` |
| To | ``` let NSInvalidArgumentException: String ``` |

Modified NSInvalidReceivePortException

|  | Declaration |
| --- | --- |
| From | ``` let NSInvalidReceivePortException: NSString! ``` |
| To | ``` let NSInvalidReceivePortException: String ``` |

Modified NSInvalidSendPortException

|  | Declaration |
| --- | --- |
| From | ``` let NSInvalidSendPortException: NSString! ``` |
| To | ``` let NSInvalidSendPortException: String ``` |

Modified NSInvalidUnarchiveOperationException

|  | Declaration |
| --- | --- |
| From | ``` let NSInvalidUnarchiveOperationException: NSString! ``` |
| To | ``` let NSInvalidUnarchiveOperationException: String ``` |

Modified NSInvocationOperationCancelledException

|  | Declaration |
| --- | --- |
| From | ``` let NSInvocationOperationCancelledException: NSString! ``` |
| To | ``` let NSInvocationOperationCancelledException: String ``` |

Modified NSInvocationOperationVoidResultException

|  | Declaration |
| --- | --- |
| From | ``` let NSInvocationOperationVoidResultException: NSString! ``` |
| To | ``` let NSInvocationOperationVoidResultException: String ``` |

Modified NSIsNilTransformerName

|  | Declaration |
| --- | --- |
| From | ``` let NSIsNilTransformerName: NSString! ``` |
| To | ``` let NSIsNilTransformerName: String ``` |

Modified NSIsNotNilTransformerName

|  | Declaration |
| --- | --- |
| From | ``` let NSIsNotNilTransformerName: NSString! ``` |
| To | ``` let NSIsNotNilTransformerName: String ``` |

Modified NSIslamicCalendar

|  | Declaration |
| --- | --- |
| From | ``` let NSIslamicCalendar: NSString! ``` |
| To | ``` let NSIslamicCalendar: String ``` |

Modified NSIslamicCivilCalendar

|  | Declaration |
| --- | --- |
| From | ``` let NSIslamicCivilCalendar: NSString! ``` |
| To | ``` let NSIslamicCivilCalendar: String ``` |

Modified NSItemProviderErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let NSItemProviderErrorDomain: NSString! ``` |
| To | ``` let NSItemProviderErrorDomain: String ``` |

Modified NSItemProviderPreferredImageSizeKey

|  | Declaration |
| --- | --- |
| From | ``` let NSItemProviderPreferredImageSizeKey: NSString! ``` |
| To | ``` let NSItemProviderPreferredImageSizeKey: String ``` |

Modified NSJapaneseCalendar

|  | Declaration |
| --- | --- |
| From | ``` let NSJapaneseCalendar: NSString! ``` |
| To | ``` let NSJapaneseCalendar: String ``` |

Modified NSKeyValueChangeIndexesKey

|  | Declaration |
| --- | --- |
| From | ``` let NSKeyValueChangeIndexesKey: NSString! ``` |
| To | ``` let NSKeyValueChangeIndexesKey: String ``` |

Modified NSKeyValueChangeKindKey

|  | Declaration |
| --- | --- |
| From | ``` let NSKeyValueChangeKindKey: NSString! ``` |
| To | ``` let NSKeyValueChangeKindKey: String ``` |

Modified NSKeyValueChangeNewKey

|  | Declaration |
| --- | --- |
| From | ``` let NSKeyValueChangeNewKey: NSString! ``` |
| To | ``` let NSKeyValueChangeNewKey: String ``` |

Modified NSKeyValueChangeNotificationIsPriorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSKeyValueChangeNotificationIsPriorKey: NSString! ``` |
| To | ``` let NSKeyValueChangeNotificationIsPriorKey: String ``` |

Modified NSKeyValueChangeOldKey

|  | Declaration |
| --- | --- |
| From | ``` let NSKeyValueChangeOldKey: NSString! ``` |
| To | ``` let NSKeyValueChangeOldKey: String ``` |

Modified NSKeyedArchiveRootObjectKey

|  | Declaration |
| --- | --- |
| From | ``` let NSKeyedArchiveRootObjectKey: NSString! ``` |
| To | ``` let NSKeyedArchiveRootObjectKey: String ``` |

Modified NSKeyedUnarchiveFromDataTransformerName

|  | Declaration |
| --- | --- |
| From | ``` let NSKeyedUnarchiveFromDataTransformerName: NSString! ``` |
| To | ``` let NSKeyedUnarchiveFromDataTransformerName: String ``` |

Modified NSLinguisticTagAdjective

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagAdjective: NSString! ``` |
| To | ``` let NSLinguisticTagAdjective: String ``` |

Modified NSLinguisticTagAdverb

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagAdverb: NSString! ``` |
| To | ``` let NSLinguisticTagAdverb: String ``` |

Modified NSLinguisticTagClassifier

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagClassifier: NSString! ``` |
| To | ``` let NSLinguisticTagClassifier: String ``` |

Modified NSLinguisticTagCloseParenthesis

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagCloseParenthesis: NSString! ``` |
| To | ``` let NSLinguisticTagCloseParenthesis: String ``` |

Modified NSLinguisticTagCloseQuote

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagCloseQuote: NSString! ``` |
| To | ``` let NSLinguisticTagCloseQuote: String ``` |

Modified NSLinguisticTagConjunction

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagConjunction: NSString! ``` |
| To | ``` let NSLinguisticTagConjunction: String ``` |

Modified NSLinguisticTagDash

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagDash: NSString! ``` |
| To | ``` let NSLinguisticTagDash: String ``` |

Modified NSLinguisticTagDeterminer

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagDeterminer: NSString! ``` |
| To | ``` let NSLinguisticTagDeterminer: String ``` |

Modified NSLinguisticTagIdiom

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagIdiom: NSString! ``` |
| To | ``` let NSLinguisticTagIdiom: String ``` |

Modified NSLinguisticTagInterjection

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagInterjection: NSString! ``` |
| To | ``` let NSLinguisticTagInterjection: String ``` |

Modified NSLinguisticTagNoun

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagNoun: NSString! ``` |
| To | ``` let NSLinguisticTagNoun: String ``` |

Modified NSLinguisticTagNumber

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagNumber: NSString! ``` |
| To | ``` let NSLinguisticTagNumber: String ``` |

Modified NSLinguisticTagOpenParenthesis

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagOpenParenthesis: NSString! ``` |
| To | ``` let NSLinguisticTagOpenParenthesis: String ``` |

Modified NSLinguisticTagOpenQuote

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagOpenQuote: NSString! ``` |
| To | ``` let NSLinguisticTagOpenQuote: String ``` |

Modified NSLinguisticTagOrganizationName

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagOrganizationName: NSString! ``` |
| To | ``` let NSLinguisticTagOrganizationName: String ``` |

Modified NSLinguisticTagOther

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagOther: NSString! ``` |
| To | ``` let NSLinguisticTagOther: String ``` |

Modified NSLinguisticTagOtherPunctuation

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagOtherPunctuation: NSString! ``` |
| To | ``` let NSLinguisticTagOtherPunctuation: String ``` |

Modified NSLinguisticTagOtherWhitespace

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagOtherWhitespace: NSString! ``` |
| To | ``` let NSLinguisticTagOtherWhitespace: String ``` |

Modified NSLinguisticTagOtherWord

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagOtherWord: NSString! ``` |
| To | ``` let NSLinguisticTagOtherWord: String ``` |

Modified NSLinguisticTagParagraphBreak

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagParagraphBreak: NSString! ``` |
| To | ``` let NSLinguisticTagParagraphBreak: String ``` |

Modified NSLinguisticTagParticle

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagParticle: NSString! ``` |
| To | ``` let NSLinguisticTagParticle: String ``` |

Modified NSLinguisticTagPersonalName

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagPersonalName: NSString! ``` |
| To | ``` let NSLinguisticTagPersonalName: String ``` |

Modified NSLinguisticTagPlaceName

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagPlaceName: NSString! ``` |
| To | ``` let NSLinguisticTagPlaceName: String ``` |

Modified NSLinguisticTagPreposition

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagPreposition: NSString! ``` |
| To | ``` let NSLinguisticTagPreposition: String ``` |

Modified NSLinguisticTagPronoun

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagPronoun: NSString! ``` |
| To | ``` let NSLinguisticTagPronoun: String ``` |

Modified NSLinguisticTagPunctuation

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagPunctuation: NSString! ``` |
| To | ``` let NSLinguisticTagPunctuation: String ``` |

Modified NSLinguisticTagSchemeLanguage

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagSchemeLanguage: NSString! ``` |
| To | ``` let NSLinguisticTagSchemeLanguage: String ``` |

Modified NSLinguisticTagSchemeLemma

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagSchemeLemma: NSString! ``` |
| To | ``` let NSLinguisticTagSchemeLemma: String ``` |

Modified NSLinguisticTagSchemeLexicalClass

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagSchemeLexicalClass: NSString! ``` |
| To | ``` let NSLinguisticTagSchemeLexicalClass: String ``` |

Modified NSLinguisticTagSchemeNameType

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagSchemeNameType: NSString! ``` |
| To | ``` let NSLinguisticTagSchemeNameType: String ``` |

Modified NSLinguisticTagSchemeNameTypeOrLexicalClass

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagSchemeNameTypeOrLexicalClass: NSString! ``` |
| To | ``` let NSLinguisticTagSchemeNameTypeOrLexicalClass: String ``` |

Modified NSLinguisticTagSchemeScript

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagSchemeScript: NSString! ``` |
| To | ``` let NSLinguisticTagSchemeScript: String ``` |

Modified NSLinguisticTagSchemeTokenType

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagSchemeTokenType: NSString! ``` |
| To | ``` let NSLinguisticTagSchemeTokenType: String ``` |

Modified NSLinguisticTagSentenceTerminator

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagSentenceTerminator: NSString! ``` |
| To | ``` let NSLinguisticTagSentenceTerminator: String ``` |

Modified NSLinguisticTagVerb

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagVerb: NSString! ``` |
| To | ``` let NSLinguisticTagVerb: String ``` |

Modified NSLinguisticTagWhitespace

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagWhitespace: NSString! ``` |
| To | ``` let NSLinguisticTagWhitespace: String ``` |

Modified NSLinguisticTagWord

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagWord: NSString! ``` |
| To | ``` let NSLinguisticTagWord: String ``` |

Modified NSLinguisticTagWordJoiner

|  | Declaration |
| --- | --- |
| From | ``` let NSLinguisticTagWordJoiner: NSString! ``` |
| To | ``` let NSLinguisticTagWordJoiner: String ``` |

Modified NSLoadedClasses

|  | Declaration |
| --- | --- |
| From | ``` let NSLoadedClasses: NSString! ``` |
| To | ``` let NSLoadedClasses: String ``` |

Modified NSLocaleAlternateQuotationBeginDelimiterKey

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleAlternateQuotationBeginDelimiterKey: NSString! ``` |
| To | ``` let NSLocaleAlternateQuotationBeginDelimiterKey: String ``` |

Modified NSLocaleAlternateQuotationEndDelimiterKey

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleAlternateQuotationEndDelimiterKey: NSString! ``` |
| To | ``` let NSLocaleAlternateQuotationEndDelimiterKey: String ``` |

Modified NSLocaleCalendar

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleCalendar: NSString! ``` |
| To | ``` let NSLocaleCalendar: String ``` |

Modified NSLocaleCollationIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleCollationIdentifier: NSString! ``` |
| To | ``` let NSLocaleCollationIdentifier: String ``` |

Modified NSLocaleCollatorIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleCollatorIdentifier: NSString! ``` |
| To | ``` let NSLocaleCollatorIdentifier: String ``` |

Modified NSLocaleCountryCode

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleCountryCode: NSString! ``` |
| To | ``` let NSLocaleCountryCode: String ``` |

Modified NSLocaleCurrencyCode

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleCurrencyCode: NSString! ``` |
| To | ``` let NSLocaleCurrencyCode: String ``` |

Modified NSLocaleCurrencySymbol

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleCurrencySymbol: NSString! ``` |
| To | ``` let NSLocaleCurrencySymbol: String ``` |

Modified NSLocaleDecimalSeparator

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleDecimalSeparator: NSString! ``` |
| To | ``` let NSLocaleDecimalSeparator: String ``` |

Modified NSLocaleExemplarCharacterSet

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleExemplarCharacterSet: NSString! ``` |
| To | ``` let NSLocaleExemplarCharacterSet: String ``` |

Modified NSLocaleGroupingSeparator

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleGroupingSeparator: NSString! ``` |
| To | ``` let NSLocaleGroupingSeparator: String ``` |

Modified NSLocaleIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleIdentifier: NSString! ``` |
| To | ``` let NSLocaleIdentifier: String ``` |

Modified NSLocaleLanguageCode

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleLanguageCode: NSString! ``` |
| To | ``` let NSLocaleLanguageCode: String ``` |

Modified NSLocaleMeasurementSystem

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleMeasurementSystem: NSString! ``` |
| To | ``` let NSLocaleMeasurementSystem: String ``` |

Modified NSLocaleQuotationBeginDelimiterKey

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleQuotationBeginDelimiterKey: NSString! ``` |
| To | ``` let NSLocaleQuotationBeginDelimiterKey: String ``` |

Modified NSLocaleQuotationEndDelimiterKey

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleQuotationEndDelimiterKey: NSString! ``` |
| To | ``` let NSLocaleQuotationEndDelimiterKey: String ``` |

Modified NSLocaleScriptCode

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleScriptCode: NSString! ``` |
| To | ``` let NSLocaleScriptCode: String ``` |

Modified NSLocaleUsesMetricSystem

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleUsesMetricSystem: NSString! ``` |
| To | ``` let NSLocaleUsesMetricSystem: String ``` |

Modified NSLocaleVariantCode

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleVariantCode: NSString! ``` |
| To | ``` let NSLocaleVariantCode: String ``` |

Modified NSLocalizedDescriptionKey

|  | Declaration |
| --- | --- |
| From | ``` let NSLocalizedDescriptionKey: NSString! ``` |
| To | ``` let NSLocalizedDescriptionKey: String ``` |

Modified NSLocalizedFailureReasonErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSLocalizedFailureReasonErrorKey: NSString! ``` |
| To | ``` let NSLocalizedFailureReasonErrorKey: String ``` |

Modified NSLocalizedRecoveryOptionsErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSLocalizedRecoveryOptionsErrorKey: NSString! ``` |
| To | ``` let NSLocalizedRecoveryOptionsErrorKey: String ``` |

Modified NSLocalizedRecoverySuggestionErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSLocalizedRecoverySuggestionErrorKey: NSString! ``` |
| To | ``` let NSLocalizedRecoverySuggestionErrorKey: String ``` |

Modified NSMachErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let NSMachErrorDomain: NSString! ``` |
| To | ``` let NSMachErrorDomain: String ``` |

Modified NSMallocException

|  | Declaration |
| --- | --- |
| From | ``` let NSMallocException: NSString! ``` |
| To | ``` let NSMallocException: String ``` |

Modified NSMaximumKeyValueOperator

|  | Declaration |
| --- | --- |
| From | ``` let NSMaximumKeyValueOperator: NSString! ``` |
| To | ``` let NSMaximumKeyValueOperator: String ``` |

Modified NSMetadataItemContentTypeKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataItemContentTypeKey: NSString! ``` |
| To | ``` let NSMetadataItemContentTypeKey: String ``` |

Modified NSMetadataItemContentTypeTreeKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataItemContentTypeTreeKey: NSString! ``` |
| To | ``` let NSMetadataItemContentTypeTreeKey: String ``` |

Modified NSMetadataItemDisplayNameKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataItemDisplayNameKey: NSString! ``` |
| To | ``` let NSMetadataItemDisplayNameKey: String ``` |

Modified NSMetadataItemFSContentChangeDateKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataItemFSContentChangeDateKey: NSString! ``` |
| To | ``` let NSMetadataItemFSContentChangeDateKey: String ``` |

Modified NSMetadataItemFSCreationDateKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataItemFSCreationDateKey: NSString! ``` |
| To | ``` let NSMetadataItemFSCreationDateKey: String ``` |

Modified NSMetadataItemFSNameKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataItemFSNameKey: NSString! ``` |
| To | ``` let NSMetadataItemFSNameKey: String ``` |

Modified NSMetadataItemFSSizeKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataItemFSSizeKey: NSString! ``` |
| To | ``` let NSMetadataItemFSSizeKey: String ``` |

Modified NSMetadataItemIsUbiquitousKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataItemIsUbiquitousKey: NSString! ``` |
| To | ``` let NSMetadataItemIsUbiquitousKey: String ``` |

Modified NSMetadataItemPathKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataItemPathKey: NSString! ``` |
| To | ``` let NSMetadataItemPathKey: String ``` |

Modified NSMetadataItemURLKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataItemURLKey: NSString! ``` |
| To | ``` let NSMetadataItemURLKey: String ``` |

Modified NSMetadataQueryAccessibleUbiquitousExternalDocumentsScope

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataQueryAccessibleUbiquitousExternalDocumentsScope: NSString! ``` |
| To | ``` let NSMetadataQueryAccessibleUbiquitousExternalDocumentsScope: String ``` |

Modified NSMetadataQueryDidFinishGatheringNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataQueryDidFinishGatheringNotification: NSString! ``` |
| To | ``` let NSMetadataQueryDidFinishGatheringNotification: String ``` |

Modified NSMetadataQueryDidStartGatheringNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataQueryDidStartGatheringNotification: NSString! ``` |
| To | ``` let NSMetadataQueryDidStartGatheringNotification: String ``` |

Modified NSMetadataQueryDidUpdateNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataQueryDidUpdateNotification: NSString! ``` |
| To | ``` let NSMetadataQueryDidUpdateNotification: String ``` |

Modified NSMetadataQueryGatheringProgressNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataQueryGatheringProgressNotification: NSString! ``` |
| To | ``` let NSMetadataQueryGatheringProgressNotification: String ``` |

Modified NSMetadataQueryResultContentRelevanceAttribute

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataQueryResultContentRelevanceAttribute: NSString! ``` |
| To | ``` let NSMetadataQueryResultContentRelevanceAttribute: String ``` |

Modified NSMetadataQueryUbiquitousDataScope

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataQueryUbiquitousDataScope: NSString! ``` |
| To | ``` let NSMetadataQueryUbiquitousDataScope: String ``` |

Modified NSMetadataQueryUbiquitousDocumentsScope

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataQueryUbiquitousDocumentsScope: NSString! ``` |
| To | ``` let NSMetadataQueryUbiquitousDocumentsScope: String ``` |

Modified NSMetadataQueryUpdateAddedItemsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataQueryUpdateAddedItemsKey: NSString! ``` |
| To | ``` let NSMetadataQueryUpdateAddedItemsKey: String ``` |

Modified NSMetadataQueryUpdateChangedItemsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataQueryUpdateChangedItemsKey: NSString! ``` |
| To | ``` let NSMetadataQueryUpdateChangedItemsKey: String ``` |

Modified NSMetadataQueryUpdateRemovedItemsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataQueryUpdateRemovedItemsKey: NSString! ``` |
| To | ``` let NSMetadataQueryUpdateRemovedItemsKey: String ``` |

Modified NSMetadataUbiquitousItemContainerDisplayNameKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataUbiquitousItemContainerDisplayNameKey: NSString! ``` |
| To | ``` let NSMetadataUbiquitousItemContainerDisplayNameKey: String ``` |

Modified NSMetadataUbiquitousItemDownloadRequestedKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataUbiquitousItemDownloadRequestedKey: NSString! ``` |
| To | ``` let NSMetadataUbiquitousItemDownloadRequestedKey: String ``` |

Modified NSMetadataUbiquitousItemDownloadingErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataUbiquitousItemDownloadingErrorKey: NSString! ``` |
| To | ``` let NSMetadataUbiquitousItemDownloadingErrorKey: String ``` |

Modified NSMetadataUbiquitousItemDownloadingStatusCurrent

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataUbiquitousItemDownloadingStatusCurrent: NSString! ``` |
| To | ``` let NSMetadataUbiquitousItemDownloadingStatusCurrent: String ``` |

Modified NSMetadataUbiquitousItemDownloadingStatusDownloaded

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataUbiquitousItemDownloadingStatusDownloaded: NSString! ``` |
| To | ``` let NSMetadataUbiquitousItemDownloadingStatusDownloaded: String ``` |

Modified NSMetadataUbiquitousItemDownloadingStatusKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataUbiquitousItemDownloadingStatusKey: NSString! ``` |
| To | ``` let NSMetadataUbiquitousItemDownloadingStatusKey: String ``` |

Modified NSMetadataUbiquitousItemDownloadingStatusNotDownloaded

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataUbiquitousItemDownloadingStatusNotDownloaded: NSString! ``` |
| To | ``` let NSMetadataUbiquitousItemDownloadingStatusNotDownloaded: String ``` |

Modified NSMetadataUbiquitousItemHasUnresolvedConflictsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataUbiquitousItemHasUnresolvedConflictsKey: NSString! ``` |
| To | ``` let NSMetadataUbiquitousItemHasUnresolvedConflictsKey: String ``` |

Modified NSMetadataUbiquitousItemIsDownloadingKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataUbiquitousItemIsDownloadingKey: NSString! ``` |
| To | ``` let NSMetadataUbiquitousItemIsDownloadingKey: String ``` |

Modified NSMetadataUbiquitousItemIsExternalDocumentKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataUbiquitousItemIsExternalDocumentKey: NSString! ``` |
| To | ``` let NSMetadataUbiquitousItemIsExternalDocumentKey: String ``` |

Modified NSMetadataUbiquitousItemIsUploadedKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataUbiquitousItemIsUploadedKey: NSString! ``` |
| To | ``` let NSMetadataUbiquitousItemIsUploadedKey: String ``` |

Modified NSMetadataUbiquitousItemIsUploadingKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataUbiquitousItemIsUploadingKey: NSString! ``` |
| To | ``` let NSMetadataUbiquitousItemIsUploadingKey: String ``` |

Modified NSMetadataUbiquitousItemPercentDownloadedKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataUbiquitousItemPercentDownloadedKey: NSString! ``` |
| To | ``` let NSMetadataUbiquitousItemPercentDownloadedKey: String ``` |

Modified NSMetadataUbiquitousItemPercentUploadedKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataUbiquitousItemPercentUploadedKey: NSString! ``` |
| To | ``` let NSMetadataUbiquitousItemPercentUploadedKey: String ``` |

Modified NSMetadataUbiquitousItemURLInLocalContainerKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataUbiquitousItemURLInLocalContainerKey: NSString! ``` |
| To | ``` let NSMetadataUbiquitousItemURLInLocalContainerKey: String ``` |

Modified NSMetadataUbiquitousItemUploadingErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataUbiquitousItemUploadingErrorKey: NSString! ``` |
| To | ``` let NSMetadataUbiquitousItemUploadingErrorKey: String ``` |

Modified NSMinimumKeyValueOperator

|  | Declaration |
| --- | --- |
| From | ``` let NSMinimumKeyValueOperator: NSString! ``` |
| To | ``` let NSMinimumKeyValueOperator: String ``` |

Modified NSNegateBooleanTransformerName

|  | Declaration |
| --- | --- |
| From | ``` let NSNegateBooleanTransformerName: NSString! ``` |
| To | ``` let NSNegateBooleanTransformerName: String ``` |

Modified NSNetServicesErrorCode

|  | Declaration |
| --- | --- |
| From | ``` let NSNetServicesErrorCode: NSString! ``` |
| To | ``` let NSNetServicesErrorCode: String ``` |

Modified NSNetServicesErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let NSNetServicesErrorDomain: NSString! ``` |
| To | ``` let NSNetServicesErrorDomain: String ``` |

Modified NSOSStatusErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let NSOSStatusErrorDomain: NSString! ``` |
| To | ``` let NSOSStatusErrorDomain: String ``` |

Modified NSObjectInaccessibleException

|  | Declaration |
| --- | --- |
| From | ``` let NSObjectInaccessibleException: NSString! ``` |
| To | ``` let NSObjectInaccessibleException: String ``` |

Modified NSObjectNotAvailableException

|  | Declaration |
| --- | --- |
| From | ``` let NSObjectNotAvailableException: NSString! ``` |
| To | ``` let NSObjectNotAvailableException: String ``` |

Modified NSOldStyleException

|  | Declaration |
| --- | --- |
| From | ``` let NSOldStyleException: NSString! ``` |
| To | ``` let NSOldStyleException: String ``` |

Modified NSPOSIXErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let NSPOSIXErrorDomain: NSString! ``` |
| To | ``` let NSPOSIXErrorDomain: String ``` |

Modified NSParseErrorException

|  | Declaration |
| --- | --- |
| From | ``` let NSParseErrorException: NSString! ``` |
| To | ``` let NSParseErrorException: String ``` |

Modified NSPersianCalendar

|  | Declaration |
| --- | --- |
| From | ``` let NSPersianCalendar: NSString! ``` |
| To | ``` let NSPersianCalendar: String ``` |

Modified NSPortDidBecomeInvalidNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSPortDidBecomeInvalidNotification: NSString! ``` |
| To | ``` let NSPortDidBecomeInvalidNotification: String ``` |

Modified NSPortReceiveException

|  | Declaration |
| --- | --- |
| From | ``` let NSPortReceiveException: NSString! ``` |
| To | ``` let NSPortReceiveException: String ``` |

Modified NSPortSendException

|  | Declaration |
| --- | --- |
| From | ``` let NSPortSendException: NSString! ``` |
| To | ``` let NSPortSendException: String ``` |

Modified NSPortTimeoutException

|  | Declaration |
| --- | --- |
| From | ``` let NSPortTimeoutException: NSString! ``` |
| To | ``` let NSPortTimeoutException: String ``` |

Modified NSProgressEstimatedTimeRemainingKey

|  | Declaration |
| --- | --- |
| From | ``` let NSProgressEstimatedTimeRemainingKey: NSString! ``` |
| To | ``` let NSProgressEstimatedTimeRemainingKey: String ``` |

Modified NSProgressFileCompletedCountKey

|  | Declaration |
| --- | --- |
| From | ``` let NSProgressFileCompletedCountKey: NSString! ``` |
| To | ``` let NSProgressFileCompletedCountKey: String ``` |

Modified NSProgressFileOperationKindCopying

|  | Declaration |
| --- | --- |
| From | ``` let NSProgressFileOperationKindCopying: NSString! ``` |
| To | ``` let NSProgressFileOperationKindCopying: String ``` |

Modified NSProgressFileOperationKindDecompressingAfterDownloading

|  | Declaration |
| --- | --- |
| From | ``` let NSProgressFileOperationKindDecompressingAfterDownloading: NSString! ``` |
| To | ``` let NSProgressFileOperationKindDecompressingAfterDownloading: String ``` |

Modified NSProgressFileOperationKindDownloading

|  | Declaration |
| --- | --- |
| From | ``` let NSProgressFileOperationKindDownloading: NSString! ``` |
| To | ``` let NSProgressFileOperationKindDownloading: String ``` |

Modified NSProgressFileOperationKindKey

|  | Declaration |
| --- | --- |
| From | ``` let NSProgressFileOperationKindKey: NSString! ``` |
| To | ``` let NSProgressFileOperationKindKey: String ``` |

Modified NSProgressFileOperationKindReceiving

|  | Declaration |
| --- | --- |
| From | ``` let NSProgressFileOperationKindReceiving: NSString! ``` |
| To | ``` let NSProgressFileOperationKindReceiving: String ``` |

Modified NSProgressFileTotalCountKey

|  | Declaration |
| --- | --- |
| From | ``` let NSProgressFileTotalCountKey: NSString! ``` |
| To | ``` let NSProgressFileTotalCountKey: String ``` |

Modified NSProgressFileURLKey

|  | Declaration |
| --- | --- |
| From | ``` let NSProgressFileURLKey: NSString! ``` |
| To | ``` let NSProgressFileURLKey: String ``` |

Modified NSProgressKindFile

|  | Declaration |
| --- | --- |
| From | ``` let NSProgressKindFile: NSString! ``` |
| To | ``` let NSProgressKindFile: String ``` |

Modified NSProgressThroughputKey

|  | Declaration |
| --- | --- |
| From | ``` let NSProgressThroughputKey: NSString! ``` |
| To | ``` let NSProgressThroughputKey: String ``` |

Modified NSRangeException

|  | Declaration |
| --- | --- |
| From | ``` let NSRangeException: NSString! ``` |
| To | ``` let NSRangeException: String ``` |

Modified NSRecoveryAttempterErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSRecoveryAttempterErrorKey: NSString! ``` |
| To | ``` let NSRecoveryAttempterErrorKey: String ``` |

Modified NSRegistrationDomain

|  | Declaration |
| --- | --- |
| From | ``` let NSRegistrationDomain: NSString! ``` |
| To | ``` let NSRegistrationDomain: String ``` |

Modified NSRepublicOfChinaCalendar

|  | Declaration |
| --- | --- |
| From | ``` let NSRepublicOfChinaCalendar: NSString! ``` |
| To | ``` let NSRepublicOfChinaCalendar: String ``` |

Modified NSRunLoopCommonModes

|  | Declaration |
| --- | --- |
| From | ``` let NSRunLoopCommonModes: NSString! ``` |
| To | ``` let NSRunLoopCommonModes: String ``` |

Modified NSStreamDataWrittenToMemoryStreamKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStreamDataWrittenToMemoryStreamKey: NSString! ``` |
| To | ``` let NSStreamDataWrittenToMemoryStreamKey: String ``` |

Modified NSStreamFileCurrentOffsetKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStreamFileCurrentOffsetKey: NSString! ``` |
| To | ``` let NSStreamFileCurrentOffsetKey: String ``` |

Modified NSStreamNetworkServiceType

|  | Declaration |
| --- | --- |
| From | ``` let NSStreamNetworkServiceType: NSString! ``` |
| To | ``` let NSStreamNetworkServiceType: String ``` |

Modified NSStreamNetworkServiceTypeBackground

|  | Declaration |
| --- | --- |
| From | ``` let NSStreamNetworkServiceTypeBackground: NSString! ``` |
| To | ``` let NSStreamNetworkServiceTypeBackground: String ``` |

Modified NSStreamNetworkServiceTypeVideo

|  | Declaration |
| --- | --- |
| From | ``` let NSStreamNetworkServiceTypeVideo: NSString! ``` |
| To | ``` let NSStreamNetworkServiceTypeVideo: String ``` |

Modified NSStreamNetworkServiceTypeVoIP

|  | Declaration |
| --- | --- |
| From | ``` let NSStreamNetworkServiceTypeVoIP: NSString! ``` |
| To | ``` let NSStreamNetworkServiceTypeVoIP: String ``` |

Modified NSStreamNetworkServiceTypeVoice

|  | Declaration |
| --- | --- |
| From | ``` let NSStreamNetworkServiceTypeVoice: NSString! ``` |
| To | ``` let NSStreamNetworkServiceTypeVoice: String ``` |

Modified NSStreamSOCKSErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let NSStreamSOCKSErrorDomain: NSString! ``` |
| To | ``` let NSStreamSOCKSErrorDomain: String ``` |

Modified NSStreamSOCKSProxyConfigurationKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStreamSOCKSProxyConfigurationKey: NSString! ``` |
| To | ``` let NSStreamSOCKSProxyConfigurationKey: String ``` |

Modified NSStreamSOCKSProxyHostKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStreamSOCKSProxyHostKey: NSString! ``` |
| To | ``` let NSStreamSOCKSProxyHostKey: String ``` |

Modified NSStreamSOCKSProxyPasswordKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStreamSOCKSProxyPasswordKey: NSString! ``` |
| To | ``` let NSStreamSOCKSProxyPasswordKey: String ``` |

Modified NSStreamSOCKSProxyPortKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStreamSOCKSProxyPortKey: NSString! ``` |
| To | ``` let NSStreamSOCKSProxyPortKey: String ``` |

Modified NSStreamSOCKSProxyUserKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStreamSOCKSProxyUserKey: NSString! ``` |
| To | ``` let NSStreamSOCKSProxyUserKey: String ``` |

Modified NSStreamSOCKSProxyVersion4

|  | Declaration |
| --- | --- |
| From | ``` let NSStreamSOCKSProxyVersion4: NSString! ``` |
| To | ``` let NSStreamSOCKSProxyVersion4: String ``` |

Modified NSStreamSOCKSProxyVersion5

|  | Declaration |
| --- | --- |
| From | ``` let NSStreamSOCKSProxyVersion5: NSString! ``` |
| To | ``` let NSStreamSOCKSProxyVersion5: String ``` |

Modified NSStreamSOCKSProxyVersionKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStreamSOCKSProxyVersionKey: NSString! ``` |
| To | ``` let NSStreamSOCKSProxyVersionKey: String ``` |

Modified NSStreamSocketSSLErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let NSStreamSocketSSLErrorDomain: NSString! ``` |
| To | ``` let NSStreamSocketSSLErrorDomain: String ``` |

Modified NSStreamSocketSecurityLevelKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStreamSocketSecurityLevelKey: NSString! ``` |
| To | ``` let NSStreamSocketSecurityLevelKey: String ``` |

Modified NSStreamSocketSecurityLevelNegotiatedSSL

|  | Declaration |
| --- | --- |
| From | ``` let NSStreamSocketSecurityLevelNegotiatedSSL: NSString! ``` |
| To | ``` let NSStreamSocketSecurityLevelNegotiatedSSL: String ``` |

Modified NSStreamSocketSecurityLevelNone

|  | Declaration |
| --- | --- |
| From | ``` let NSStreamSocketSecurityLevelNone: NSString! ``` |
| To | ``` let NSStreamSocketSecurityLevelNone: String ``` |

Modified NSStreamSocketSecurityLevelSSLv2

|  | Declaration |
| --- | --- |
| From | ``` let NSStreamSocketSecurityLevelSSLv2: NSString! ``` |
| To | ``` let NSStreamSocketSecurityLevelSSLv2: String ``` |

Modified NSStreamSocketSecurityLevelSSLv3

|  | Declaration |
| --- | --- |
| From | ``` let NSStreamSocketSecurityLevelSSLv3: NSString! ``` |
| To | ``` let NSStreamSocketSecurityLevelSSLv3: String ``` |

Modified NSStreamSocketSecurityLevelTLSv1

|  | Declaration |
| --- | --- |
| From | ``` let NSStreamSocketSecurityLevelTLSv1: NSString! ``` |
| To | ``` let NSStreamSocketSecurityLevelTLSv1: String ``` |

Modified NSStringEncodingDetectionAllowLossyKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStringEncodingDetectionAllowLossyKey: NSString! ``` |
| To | ``` let NSStringEncodingDetectionAllowLossyKey: String ``` |

Modified NSStringEncodingDetectionDisallowedEncodingsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStringEncodingDetectionDisallowedEncodingsKey: NSString! ``` |
| To | ``` let NSStringEncodingDetectionDisallowedEncodingsKey: String ``` |

Modified NSStringEncodingDetectionFromWindowsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStringEncodingDetectionFromWindowsKey: NSString! ``` |
| To | ``` let NSStringEncodingDetectionFromWindowsKey: String ``` |

Modified NSStringEncodingDetectionLikelyLanguageKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStringEncodingDetectionLikelyLanguageKey: NSString! ``` |
| To | ``` let NSStringEncodingDetectionLikelyLanguageKey: String ``` |

Modified NSStringEncodingDetectionLossySubstitutionKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStringEncodingDetectionLossySubstitutionKey: NSString! ``` |
| To | ``` let NSStringEncodingDetectionLossySubstitutionKey: String ``` |

Modified NSStringEncodingDetectionSuggestedEncodingsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStringEncodingDetectionSuggestedEncodingsKey: NSString! ``` |
| To | ``` let NSStringEncodingDetectionSuggestedEncodingsKey: String ``` |

Modified NSStringEncodingDetectionUseOnlySuggestedEncodingsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStringEncodingDetectionUseOnlySuggestedEncodingsKey: NSString! ``` |
| To | ``` let NSStringEncodingDetectionUseOnlySuggestedEncodingsKey: String ``` |

Modified NSStringEncodingErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStringEncodingErrorKey: NSString! ``` |
| To | ``` let NSStringEncodingErrorKey: String ``` |

Modified NSSumKeyValueOperator

|  | Declaration |
| --- | --- |
| From | ``` let NSSumKeyValueOperator: NSString! ``` |
| To | ``` let NSSumKeyValueOperator: String ``` |

Modified NSSystemClockDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSSystemClockDidChangeNotification: NSString! ``` |
| To | ``` let NSSystemClockDidChangeNotification: String ``` |

Modified NSSystemTimeZoneDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSSystemTimeZoneDidChangeNotification: NSString! ``` |
| To | ``` let NSSystemTimeZoneDidChangeNotification: String ``` |

Modified NSTextCheckingAirlineKey

|  | Declaration |
| --- | --- |
| From | ``` let NSTextCheckingAirlineKey: NSString! ``` |
| To | ``` let NSTextCheckingAirlineKey: String ``` |

Modified NSTextCheckingCityKey

|  | Declaration |
| --- | --- |
| From | ``` let NSTextCheckingCityKey: NSString! ``` |
| To | ``` let NSTextCheckingCityKey: String ``` |

Modified NSTextCheckingCountryKey

|  | Declaration |
| --- | --- |
| From | ``` let NSTextCheckingCountryKey: NSString! ``` |
| To | ``` let NSTextCheckingCountryKey: String ``` |

Modified NSTextCheckingFlightKey

|  | Declaration |
| --- | --- |
| From | ``` let NSTextCheckingFlightKey: NSString! ``` |
| To | ``` let NSTextCheckingFlightKey: String ``` |

Modified NSTextCheckingJobTitleKey

|  | Declaration |
| --- | --- |
| From | ``` let NSTextCheckingJobTitleKey: NSString! ``` |
| To | ``` let NSTextCheckingJobTitleKey: String ``` |

Modified NSTextCheckingNameKey

|  | Declaration |
| --- | --- |
| From | ``` let NSTextCheckingNameKey: NSString! ``` |
| To | ``` let NSTextCheckingNameKey: String ``` |

Modified NSTextCheckingOrganizationKey

|  | Declaration |
| --- | --- |
| From | ``` let NSTextCheckingOrganizationKey: NSString! ``` |
| To | ``` let NSTextCheckingOrganizationKey: String ``` |

Modified NSTextCheckingPhoneKey

|  | Declaration |
| --- | --- |
| From | ``` let NSTextCheckingPhoneKey: NSString! ``` |
| To | ``` let NSTextCheckingPhoneKey: String ``` |

Modified NSTextCheckingStateKey

|  | Declaration |
| --- | --- |
| From | ``` let NSTextCheckingStateKey: NSString! ``` |
| To | ``` let NSTextCheckingStateKey: String ``` |

Modified NSTextCheckingStreetKey

|  | Declaration |
| --- | --- |
| From | ``` let NSTextCheckingStreetKey: NSString! ``` |
| To | ``` let NSTextCheckingStreetKey: String ``` |

Modified NSTextCheckingZIPKey

|  | Declaration |
| --- | --- |
| From | ``` let NSTextCheckingZIPKey: NSString! ``` |
| To | ``` let NSTextCheckingZIPKey: String ``` |

Modified NSThreadWillExitNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSThreadWillExitNotification: NSString! ``` |
| To | ``` let NSThreadWillExitNotification: String ``` |

Modified NSThumbnail1024x1024SizeKey

|  | Declaration |
| --- | --- |
| From | ``` let NSThumbnail1024x1024SizeKey: NSString! ``` |
| To | ``` let NSThumbnail1024x1024SizeKey: String ``` |

Modified NSURLAddedToDirectoryDateKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLAddedToDirectoryDateKey: NSString! ``` |
| To | ``` let NSURLAddedToDirectoryDateKey: String ``` |

Modified NSURLAttributeModificationDateKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLAttributeModificationDateKey: NSString! ``` |
| To | ``` let NSURLAttributeModificationDateKey: String ``` |

Modified NSURLAuthenticationMethodClientCertificate

|  | Declaration |
| --- | --- |
| From | ``` let NSURLAuthenticationMethodClientCertificate: NSString! ``` |
| To | ``` let NSURLAuthenticationMethodClientCertificate: String ``` |

Modified NSURLAuthenticationMethodDefault

|  | Declaration |
| --- | --- |
| From | ``` let NSURLAuthenticationMethodDefault: NSString! ``` |
| To | ``` let NSURLAuthenticationMethodDefault: String ``` |

Modified NSURLAuthenticationMethodHTMLForm

|  | Declaration |
| --- | --- |
| From | ``` let NSURLAuthenticationMethodHTMLForm: NSString! ``` |
| To | ``` let NSURLAuthenticationMethodHTMLForm: String ``` |

Modified NSURLAuthenticationMethodHTTPBasic

|  | Declaration |
| --- | --- |
| From | ``` let NSURLAuthenticationMethodHTTPBasic: NSString! ``` |
| To | ``` let NSURLAuthenticationMethodHTTPBasic: String ``` |

Modified NSURLAuthenticationMethodHTTPDigest

|  | Declaration |
| --- | --- |
| From | ``` let NSURLAuthenticationMethodHTTPDigest: NSString! ``` |
| To | ``` let NSURLAuthenticationMethodHTTPDigest: String ``` |

Modified NSURLAuthenticationMethodNTLM

|  | Declaration |
| --- | --- |
| From | ``` let NSURLAuthenticationMethodNTLM: NSString! ``` |
| To | ``` let NSURLAuthenticationMethodNTLM: String ``` |

Modified NSURLAuthenticationMethodNegotiate

|  | Declaration |
| --- | --- |
| From | ``` let NSURLAuthenticationMethodNegotiate: NSString! ``` |
| To | ``` let NSURLAuthenticationMethodNegotiate: String ``` |

Modified NSURLAuthenticationMethodServerTrust

|  | Declaration |
| --- | --- |
| From | ``` let NSURLAuthenticationMethodServerTrust: NSString! ``` |
| To | ``` let NSURLAuthenticationMethodServerTrust: String ``` |

Modified NSURLContentAccessDateKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLContentAccessDateKey: NSString! ``` |
| To | ``` let NSURLContentAccessDateKey: String ``` |

Modified NSURLContentModificationDateKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLContentModificationDateKey: NSString! ``` |
| To | ``` let NSURLContentModificationDateKey: String ``` |

Modified NSURLCreationDateKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLCreationDateKey: NSString! ``` |
| To | ``` let NSURLCreationDateKey: String ``` |

Modified NSURLCredentialStorageChangedNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSURLCredentialStorageChangedNotification: NSString! ``` |
| To | ``` let NSURLCredentialStorageChangedNotification: String ``` |

Modified NSURLCredentialStorageRemoveSynchronizableCredentials

|  | Declaration |
| --- | --- |
| From | ``` let NSURLCredentialStorageRemoveSynchronizableCredentials: NSString! ``` |
| To | ``` let NSURLCredentialStorageRemoveSynchronizableCredentials: String ``` |

Modified NSURLCustomIconKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLCustomIconKey: NSString! ``` |
| To | ``` let NSURLCustomIconKey: String ``` |

Modified NSURLDocumentIdentifierKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLDocumentIdentifierKey: NSString! ``` |
| To | ``` let NSURLDocumentIdentifierKey: String ``` |

Modified NSURLEffectiveIconKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLEffectiveIconKey: NSString! ``` |
| To | ``` let NSURLEffectiveIconKey: String ``` |

Modified NSURLErrorBackgroundTaskCancelledReasonKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLErrorBackgroundTaskCancelledReasonKey: NSString! ``` |
| To | ``` let NSURLErrorBackgroundTaskCancelledReasonKey: String ``` |

Modified NSURLErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let NSURLErrorDomain: NSString! ``` |
| To | ``` let NSURLErrorDomain: String ``` |

Modified NSURLErrorFailingURLErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLErrorFailingURLErrorKey: NSString! ``` |
| To | ``` let NSURLErrorFailingURLErrorKey: String ``` |

Modified NSURLErrorFailingURLPeerTrustErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLErrorFailingURLPeerTrustErrorKey: NSString! ``` |
| To | ``` let NSURLErrorFailingURLPeerTrustErrorKey: String ``` |

Modified NSURLErrorFailingURLStringErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLErrorFailingURLStringErrorKey: NSString! ``` |
| To | ``` let NSURLErrorFailingURLStringErrorKey: String ``` |

Modified NSURLErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLErrorKey: NSString! ``` |
| To | ``` let NSURLErrorKey: String ``` |

Modified NSURLFileAllocatedSizeKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLFileAllocatedSizeKey: NSString! ``` |
| To | ``` let NSURLFileAllocatedSizeKey: String ``` |

Modified NSURLFileResourceIdentifierKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLFileResourceIdentifierKey: NSString! ``` |
| To | ``` let NSURLFileResourceIdentifierKey: String ``` |

Modified NSURLFileResourceTypeBlockSpecial

|  | Declaration |
| --- | --- |
| From | ``` let NSURLFileResourceTypeBlockSpecial: NSString! ``` |
| To | ``` let NSURLFileResourceTypeBlockSpecial: String ``` |

Modified NSURLFileResourceTypeCharacterSpecial

|  | Declaration |
| --- | --- |
| From | ``` let NSURLFileResourceTypeCharacterSpecial: NSString! ``` |
| To | ``` let NSURLFileResourceTypeCharacterSpecial: String ``` |

Modified NSURLFileResourceTypeDirectory

|  | Declaration |
| --- | --- |
| From | ``` let NSURLFileResourceTypeDirectory: NSString! ``` |
| To | ``` let NSURLFileResourceTypeDirectory: String ``` |

Modified NSURLFileResourceTypeKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLFileResourceTypeKey: NSString! ``` |
| To | ``` let NSURLFileResourceTypeKey: String ``` |

Modified NSURLFileResourceTypeNamedPipe

|  | Declaration |
| --- | --- |
| From | ``` let NSURLFileResourceTypeNamedPipe: NSString! ``` |
| To | ``` let NSURLFileResourceTypeNamedPipe: String ``` |

Modified NSURLFileResourceTypeRegular

|  | Declaration |
| --- | --- |
| From | ``` let NSURLFileResourceTypeRegular: NSString! ``` |
| To | ``` let NSURLFileResourceTypeRegular: String ``` |

Modified NSURLFileResourceTypeSocket

|  | Declaration |
| --- | --- |
| From | ``` let NSURLFileResourceTypeSocket: NSString! ``` |
| To | ``` let NSURLFileResourceTypeSocket: String ``` |

Modified NSURLFileResourceTypeSymbolicLink

|  | Declaration |
| --- | --- |
| From | ``` let NSURLFileResourceTypeSymbolicLink: NSString! ``` |
| To | ``` let NSURLFileResourceTypeSymbolicLink: String ``` |

Modified NSURLFileResourceTypeUnknown

|  | Declaration |
| --- | --- |
| From | ``` let NSURLFileResourceTypeUnknown: NSString! ``` |
| To | ``` let NSURLFileResourceTypeUnknown: String ``` |

Modified NSURLFileScheme

|  | Declaration |
| --- | --- |
| From | ``` var NSURLFileScheme: NSString! ``` |
| To | ``` let NSURLFileScheme: String ``` |

Modified NSURLFileSecurityKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLFileSecurityKey: NSString! ``` |
| To | ``` let NSURLFileSecurityKey: String ``` |

Modified NSURLFileSizeKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLFileSizeKey: NSString! ``` |
| To | ``` let NSURLFileSizeKey: String ``` |

Modified NSURLGenerationIdentifierKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLGenerationIdentifierKey: NSString! ``` |
| To | ``` let NSURLGenerationIdentifierKey: String ``` |

Modified NSURLHasHiddenExtensionKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLHasHiddenExtensionKey: NSString! ``` |
| To | ``` let NSURLHasHiddenExtensionKey: String ``` |

Modified NSURLIsAliasFileKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLIsAliasFileKey: NSString! ``` |
| To | ``` let NSURLIsAliasFileKey: String ``` |

Modified NSURLIsDirectoryKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLIsDirectoryKey: NSString! ``` |
| To | ``` let NSURLIsDirectoryKey: String ``` |

Modified NSURLIsExcludedFromBackupKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLIsExcludedFromBackupKey: NSString! ``` |
| To | ``` let NSURLIsExcludedFromBackupKey: String ``` |

Modified NSURLIsExecutableKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLIsExecutableKey: NSString! ``` |
| To | ``` let NSURLIsExecutableKey: String ``` |

Modified NSURLIsHiddenKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLIsHiddenKey: NSString! ``` |
| To | ``` let NSURLIsHiddenKey: String ``` |

Modified NSURLIsMountTriggerKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLIsMountTriggerKey: NSString! ``` |
| To | ``` let NSURLIsMountTriggerKey: String ``` |

Modified NSURLIsPackageKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLIsPackageKey: NSString! ``` |
| To | ``` let NSURLIsPackageKey: String ``` |

Modified NSURLIsReadableKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLIsReadableKey: NSString! ``` |
| To | ``` let NSURLIsReadableKey: String ``` |

Modified NSURLIsRegularFileKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLIsRegularFileKey: NSString! ``` |
| To | ``` let NSURLIsRegularFileKey: String ``` |

Modified NSURLIsSymbolicLinkKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLIsSymbolicLinkKey: NSString! ``` |
| To | ``` let NSURLIsSymbolicLinkKey: String ``` |

Modified NSURLIsSystemImmutableKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLIsSystemImmutableKey: NSString! ``` |
| To | ``` let NSURLIsSystemImmutableKey: String ``` |

Modified NSURLIsUbiquitousItemKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLIsUbiquitousItemKey: NSString! ``` |
| To | ``` let NSURLIsUbiquitousItemKey: String ``` |

Modified NSURLIsUserImmutableKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLIsUserImmutableKey: NSString! ``` |
| To | ``` let NSURLIsUserImmutableKey: String ``` |

Modified NSURLIsVolumeKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLIsVolumeKey: NSString! ``` |
| To | ``` let NSURLIsVolumeKey: String ``` |

Modified NSURLIsWritableKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLIsWritableKey: NSString! ``` |
| To | ``` let NSURLIsWritableKey: String ``` |

Modified NSURLKeysOfUnsetValuesKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLKeysOfUnsetValuesKey: NSString! ``` |
| To | ``` let NSURLKeysOfUnsetValuesKey: String ``` |

Modified NSURLLabelColorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLLabelColorKey: NSString! ``` |
| To | ``` let NSURLLabelColorKey: String ``` |

Modified NSURLLabelNumberKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLLabelNumberKey: NSString! ``` |
| To | ``` let NSURLLabelNumberKey: String ``` |

Modified NSURLLinkCountKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLLinkCountKey: NSString! ``` |
| To | ``` let NSURLLinkCountKey: String ``` |

Modified NSURLLocalizedLabelKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLLocalizedLabelKey: NSString! ``` |
| To | ``` let NSURLLocalizedLabelKey: String ``` |

Modified NSURLLocalizedNameKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLLocalizedNameKey: NSString! ``` |
| To | ``` let NSURLLocalizedNameKey: String ``` |

Modified NSURLLocalizedTypeDescriptionKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLLocalizedTypeDescriptionKey: NSString! ``` |
| To | ``` let NSURLLocalizedTypeDescriptionKey: String ``` |

Modified NSURLNameKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLNameKey: NSString! ``` |
| To | ``` let NSURLNameKey: String ``` |

Modified NSURLParentDirectoryURLKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLParentDirectoryURLKey: NSString! ``` |
| To | ``` let NSURLParentDirectoryURLKey: String ``` |

Modified NSURLPathKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLPathKey: NSString! ``` |
| To | ``` let NSURLPathKey: String ``` |

Modified NSURLPreferredIOBlockSizeKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLPreferredIOBlockSizeKey: NSString! ``` |
| To | ``` let NSURLPreferredIOBlockSizeKey: String ``` |

Modified NSURLProtectionSpaceFTP

|  | Declaration |
| --- | --- |
| From | ``` let NSURLProtectionSpaceFTP: NSString! ``` |
| To | ``` let NSURLProtectionSpaceFTP: String ``` |

Modified NSURLProtectionSpaceFTPProxy

|  | Declaration |
| --- | --- |
| From | ``` let NSURLProtectionSpaceFTPProxy: NSString! ``` |
| To | ``` let NSURLProtectionSpaceFTPProxy: String ``` |

Modified NSURLProtectionSpaceHTTP

|  | Declaration |
| --- | --- |
| From | ``` let NSURLProtectionSpaceHTTP: NSString! ``` |
| To | ``` let NSURLProtectionSpaceHTTP: String ``` |

Modified NSURLProtectionSpaceHTTPProxy

|  | Declaration |
| --- | --- |
| From | ``` let NSURLProtectionSpaceHTTPProxy: NSString! ``` |
| To | ``` let NSURLProtectionSpaceHTTPProxy: String ``` |

Modified NSURLProtectionSpaceHTTPS

|  | Declaration |
| --- | --- |
| From | ``` let NSURLProtectionSpaceHTTPS: NSString! ``` |
| To | ``` let NSURLProtectionSpaceHTTPS: String ``` |

Modified NSURLProtectionSpaceHTTPSProxy

|  | Declaration |
| --- | --- |
| From | ``` let NSURLProtectionSpaceHTTPSProxy: NSString! ``` |
| To | ``` let NSURLProtectionSpaceHTTPSProxy: String ``` |

Modified NSURLProtectionSpaceSOCKSProxy

|  | Declaration |
| --- | --- |
| From | ``` let NSURLProtectionSpaceSOCKSProxy: NSString! ``` |
| To | ``` let NSURLProtectionSpaceSOCKSProxy: String ``` |

Modified NSURLSessionDownloadTaskResumeData

|  | Declaration |
| --- | --- |
| From | ``` let NSURLSessionDownloadTaskResumeData: NSString! ``` |
| To | ``` let NSURLSessionDownloadTaskResumeData: String ``` |

Modified NSURLThumbnailDictionaryKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLThumbnailDictionaryKey: NSString! ``` |
| To | ``` let NSURLThumbnailDictionaryKey: String ``` |

Modified NSURLTotalFileAllocatedSizeKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLTotalFileAllocatedSizeKey: NSString! ``` |
| To | ``` let NSURLTotalFileAllocatedSizeKey: String ``` |

Modified NSURLTotalFileSizeKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLTotalFileSizeKey: NSString! ``` |
| To | ``` let NSURLTotalFileSizeKey: String ``` |

Modified NSURLTypeIdentifierKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLTypeIdentifierKey: NSString! ``` |
| To | ``` let NSURLTypeIdentifierKey: String ``` |

Modified NSURLUbiquitousItemContainerDisplayNameKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLUbiquitousItemContainerDisplayNameKey: NSString! ``` |
| To | ``` let NSURLUbiquitousItemContainerDisplayNameKey: String ``` |

Modified NSURLUbiquitousItemDownloadRequestedKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLUbiquitousItemDownloadRequestedKey: NSString! ``` |
| To | ``` let NSURLUbiquitousItemDownloadRequestedKey: String ``` |

Modified NSURLUbiquitousItemDownloadingErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLUbiquitousItemDownloadingErrorKey: NSString! ``` |
| To | ``` let NSURLUbiquitousItemDownloadingErrorKey: String ``` |

Modified NSURLUbiquitousItemDownloadingStatusCurrent

|  | Declaration |
| --- | --- |
| From | ``` let NSURLUbiquitousItemDownloadingStatusCurrent: NSString! ``` |
| To | ``` let NSURLUbiquitousItemDownloadingStatusCurrent: String ``` |

Modified NSURLUbiquitousItemDownloadingStatusDownloaded

|  | Declaration |
| --- | --- |
| From | ``` let NSURLUbiquitousItemDownloadingStatusDownloaded: NSString! ``` |
| To | ``` let NSURLUbiquitousItemDownloadingStatusDownloaded: String ``` |

Modified NSURLUbiquitousItemDownloadingStatusKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLUbiquitousItemDownloadingStatusKey: NSString! ``` |
| To | ``` let NSURLUbiquitousItemDownloadingStatusKey: String ``` |

Modified NSURLUbiquitousItemDownloadingStatusNotDownloaded

|  | Declaration |
| --- | --- |
| From | ``` let NSURLUbiquitousItemDownloadingStatusNotDownloaded: NSString! ``` |
| To | ``` let NSURLUbiquitousItemDownloadingStatusNotDownloaded: String ``` |

Modified NSURLUbiquitousItemHasUnresolvedConflictsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLUbiquitousItemHasUnresolvedConflictsKey: NSString! ``` |
| To | ``` let NSURLUbiquitousItemHasUnresolvedConflictsKey: String ``` |

Modified NSURLUbiquitousItemIsDownloadingKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLUbiquitousItemIsDownloadingKey: NSString! ``` |
| To | ``` let NSURLUbiquitousItemIsDownloadingKey: String ``` |

Modified NSURLUbiquitousItemIsUploadedKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLUbiquitousItemIsUploadedKey: NSString! ``` |
| To | ``` let NSURLUbiquitousItemIsUploadedKey: String ``` |

Modified NSURLUbiquitousItemIsUploadingKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLUbiquitousItemIsUploadingKey: NSString! ``` |
| To | ``` let NSURLUbiquitousItemIsUploadingKey: String ``` |

Modified NSURLUbiquitousItemUploadingErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLUbiquitousItemUploadingErrorKey: NSString! ``` |
| To | ``` let NSURLUbiquitousItemUploadingErrorKey: String ``` |

Modified NSURLVolumeAvailableCapacityKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeAvailableCapacityKey: NSString! ``` |
| To | ``` let NSURLVolumeAvailableCapacityKey: String ``` |

Modified NSURLVolumeCreationDateKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeCreationDateKey: NSString! ``` |
| To | ``` let NSURLVolumeCreationDateKey: String ``` |

Modified NSURLVolumeIdentifierKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeIdentifierKey: NSString! ``` |
| To | ``` let NSURLVolumeIdentifierKey: String ``` |

Modified NSURLVolumeIsAutomountedKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeIsAutomountedKey: NSString! ``` |
| To | ``` let NSURLVolumeIsAutomountedKey: String ``` |

Modified NSURLVolumeIsBrowsableKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeIsBrowsableKey: NSString! ``` |
| To | ``` let NSURLVolumeIsBrowsableKey: String ``` |

Modified NSURLVolumeIsEjectableKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeIsEjectableKey: NSString! ``` |
| To | ``` let NSURLVolumeIsEjectableKey: String ``` |

Modified NSURLVolumeIsInternalKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeIsInternalKey: NSString! ``` |
| To | ``` let NSURLVolumeIsInternalKey: String ``` |

Modified NSURLVolumeIsJournalingKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeIsJournalingKey: NSString! ``` |
| To | ``` let NSURLVolumeIsJournalingKey: String ``` |

Modified NSURLVolumeIsLocalKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeIsLocalKey: NSString! ``` |
| To | ``` let NSURLVolumeIsLocalKey: String ``` |

Modified NSURLVolumeIsReadOnlyKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeIsReadOnlyKey: NSString! ``` |
| To | ``` let NSURLVolumeIsReadOnlyKey: String ``` |

Modified NSURLVolumeIsRemovableKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeIsRemovableKey: NSString! ``` |
| To | ``` let NSURLVolumeIsRemovableKey: String ``` |

Modified NSURLVolumeLocalizedFormatDescriptionKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeLocalizedFormatDescriptionKey: NSString! ``` |
| To | ``` let NSURLVolumeLocalizedFormatDescriptionKey: String ``` |

Modified NSURLVolumeLocalizedNameKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeLocalizedNameKey: NSString! ``` |
| To | ``` let NSURLVolumeLocalizedNameKey: String ``` |

Modified NSURLVolumeMaximumFileSizeKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeMaximumFileSizeKey: NSString! ``` |
| To | ``` let NSURLVolumeMaximumFileSizeKey: String ``` |

Modified NSURLVolumeNameKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeNameKey: NSString! ``` |
| To | ``` let NSURLVolumeNameKey: String ``` |

Modified NSURLVolumeResourceCountKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeResourceCountKey: NSString! ``` |
| To | ``` let NSURLVolumeResourceCountKey: String ``` |

Modified NSURLVolumeSupportsAdvisoryFileLockingKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeSupportsAdvisoryFileLockingKey: NSString! ``` |
| To | ``` let NSURLVolumeSupportsAdvisoryFileLockingKey: String ``` |

Modified NSURLVolumeSupportsCasePreservedNamesKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeSupportsCasePreservedNamesKey: NSString! ``` |
| To | ``` let NSURLVolumeSupportsCasePreservedNamesKey: String ``` |

Modified NSURLVolumeSupportsCaseSensitiveNamesKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeSupportsCaseSensitiveNamesKey: NSString! ``` |
| To | ``` let NSURLVolumeSupportsCaseSensitiveNamesKey: String ``` |

Modified NSURLVolumeSupportsExtendedSecurityKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeSupportsExtendedSecurityKey: NSString! ``` |
| To | ``` let NSURLVolumeSupportsExtendedSecurityKey: String ``` |

Modified NSURLVolumeSupportsHardLinksKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeSupportsHardLinksKey: NSString! ``` |
| To | ``` let NSURLVolumeSupportsHardLinksKey: String ``` |

Modified NSURLVolumeSupportsJournalingKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeSupportsJournalingKey: NSString! ``` |
| To | ``` let NSURLVolumeSupportsJournalingKey: String ``` |

Modified NSURLVolumeSupportsPersistentIDsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeSupportsPersistentIDsKey: NSString! ``` |
| To | ``` let NSURLVolumeSupportsPersistentIDsKey: String ``` |

Modified NSURLVolumeSupportsRenamingKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeSupportsRenamingKey: NSString! ``` |
| To | ``` let NSURLVolumeSupportsRenamingKey: String ``` |

Modified NSURLVolumeSupportsRootDirectoryDatesKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeSupportsRootDirectoryDatesKey: NSString! ``` |
| To | ``` let NSURLVolumeSupportsRootDirectoryDatesKey: String ``` |

Modified NSURLVolumeSupportsSparseFilesKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeSupportsSparseFilesKey: NSString! ``` |
| To | ``` let NSURLVolumeSupportsSparseFilesKey: String ``` |

Modified NSURLVolumeSupportsSymbolicLinksKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeSupportsSymbolicLinksKey: NSString! ``` |
| To | ``` let NSURLVolumeSupportsSymbolicLinksKey: String ``` |

Modified NSURLVolumeSupportsVolumeSizesKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeSupportsVolumeSizesKey: NSString! ``` |
| To | ``` let NSURLVolumeSupportsVolumeSizesKey: String ``` |

Modified NSURLVolumeSupportsZeroRunsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeSupportsZeroRunsKey: NSString! ``` |
| To | ``` let NSURLVolumeSupportsZeroRunsKey: String ``` |

Modified NSURLVolumeTotalCapacityKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeTotalCapacityKey: NSString! ``` |
| To | ``` let NSURLVolumeTotalCapacityKey: String ``` |

Modified NSURLVolumeURLForRemountingKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeURLForRemountingKey: NSString! ``` |
| To | ``` let NSURLVolumeURLForRemountingKey: String ``` |

Modified NSURLVolumeURLKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeURLKey: NSString! ``` |
| To | ``` let NSURLVolumeURLKey: String ``` |

Modified NSURLVolumeUUIDStringKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLVolumeUUIDStringKey: NSString! ``` |
| To | ``` let NSURLVolumeUUIDStringKey: String ``` |

Modified NSUbiquitousKeyValueStoreChangeReasonKey

|  | Declaration |
| --- | --- |
| From | ``` let NSUbiquitousKeyValueStoreChangeReasonKey: NSString! ``` |
| To | ``` let NSUbiquitousKeyValueStoreChangeReasonKey: String ``` |

Modified NSUbiquitousKeyValueStoreChangedKeysKey

|  | Declaration |
| --- | --- |
| From | ``` let NSUbiquitousKeyValueStoreChangedKeysKey: NSString! ``` |
| To | ``` let NSUbiquitousKeyValueStoreChangedKeysKey: String ``` |

Modified NSUbiquitousKeyValueStoreDidChangeExternallyNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSUbiquitousKeyValueStoreDidChangeExternallyNotification: NSString! ``` |
| To | ``` let NSUbiquitousKeyValueStoreDidChangeExternallyNotification: String ``` |

Modified NSUbiquityIdentityDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSUbiquityIdentityDidChangeNotification: NSString! ``` |
| To | ``` let NSUbiquityIdentityDidChangeNotification: String ``` |

Modified NSUnarchiveFromDataTransformerName

|  | Declaration |
| --- | --- |
| From | ``` let NSUnarchiveFromDataTransformerName: NSString! ``` |
| To | ``` let NSUnarchiveFromDataTransformerName: String ``` |

Modified NSUndefinedKeyException

|  | Declaration |
| --- | --- |
| From | ``` let NSUndefinedKeyException: NSString! ``` |
| To | ``` let NSUndefinedKeyException: String ``` |

Modified NSUnderlyingErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSUnderlyingErrorKey: NSString! ``` |
| To | ``` let NSUnderlyingErrorKey: String ``` |

Modified NSUndoManagerCheckpointNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSUndoManagerCheckpointNotification: NSString! ``` |
| To | ``` let NSUndoManagerCheckpointNotification: String ``` |

Modified NSUndoManagerDidCloseUndoGroupNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSUndoManagerDidCloseUndoGroupNotification: NSString! ``` |
| To | ``` let NSUndoManagerDidCloseUndoGroupNotification: String ``` |

Modified NSUndoManagerDidOpenUndoGroupNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSUndoManagerDidOpenUndoGroupNotification: NSString! ``` |
| To | ``` let NSUndoManagerDidOpenUndoGroupNotification: String ``` |

Modified NSUndoManagerDidRedoChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSUndoManagerDidRedoChangeNotification: NSString! ``` |
| To | ``` let NSUndoManagerDidRedoChangeNotification: String ``` |

Modified NSUndoManagerDidUndoChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSUndoManagerDidUndoChangeNotification: NSString! ``` |
| To | ``` let NSUndoManagerDidUndoChangeNotification: String ``` |

Modified NSUndoManagerGroupIsDiscardableKey

|  | Declaration |
| --- | --- |
| From | ``` let NSUndoManagerGroupIsDiscardableKey: NSString! ``` |
| To | ``` let NSUndoManagerGroupIsDiscardableKey: String ``` |

Modified NSUndoManagerWillCloseUndoGroupNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSUndoManagerWillCloseUndoGroupNotification: NSString! ``` |
| To | ``` let NSUndoManagerWillCloseUndoGroupNotification: String ``` |

Modified NSUndoManagerWillRedoChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSUndoManagerWillRedoChangeNotification: NSString! ``` |
| To | ``` let NSUndoManagerWillRedoChangeNotification: String ``` |

Modified NSUndoManagerWillUndoChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSUndoManagerWillUndoChangeNotification: NSString! ``` |
| To | ``` let NSUndoManagerWillUndoChangeNotification: String ``` |

Modified NSUnionOfArraysKeyValueOperator

|  | Declaration |
| --- | --- |
| From | ``` let NSUnionOfArraysKeyValueOperator: NSString! ``` |
| To | ``` let NSUnionOfArraysKeyValueOperator: String ``` |

Modified NSUnionOfObjectsKeyValueOperator

|  | Declaration |
| --- | --- |
| From | ``` let NSUnionOfObjectsKeyValueOperator: NSString! ``` |
| To | ``` let NSUnionOfObjectsKeyValueOperator: String ``` |

Modified NSUnionOfSetsKeyValueOperator

|  | Declaration |
| --- | --- |
| From | ``` let NSUnionOfSetsKeyValueOperator: NSString! ``` |
| To | ``` let NSUnionOfSetsKeyValueOperator: String ``` |

Modified NSUserActivityTypeBrowsingWeb

|  | Declaration |
| --- | --- |
| From | ``` let NSUserActivityTypeBrowsingWeb: NSString! ``` |
| To | ``` let NSUserActivityTypeBrowsingWeb: String ``` |

Modified NSUserDefaultsDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSUserDefaultsDidChangeNotification: NSString! ``` |
| To | ``` let NSUserDefaultsDidChangeNotification: String ``` |

Modified NSWillBecomeMultiThreadedNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSWillBecomeMultiThreadedNotification: NSString! ``` |
| To | ``` let NSWillBecomeMultiThreadedNotification: String ``` |

Modified NSXMLParserErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let NSXMLParserErrorDomain: NSString! ``` |
| To | ``` let NSXMLParserErrorDomain: String ``` |

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
