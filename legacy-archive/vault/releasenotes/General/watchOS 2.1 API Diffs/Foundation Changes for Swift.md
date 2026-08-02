---
title: watchOS 2.1 API Diffs
apple_id: TP40016636
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2015-12-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS21APIDiffs/Swift/Foundation.html
archived_at: '2026-07-18T02:58:08.468297Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 2.1 API Diffs](watchOS%202.0%20to%20watchOS%202.1%20API%20Differences.md)


# Foundation Changes for Swift

### Foundation

Added NSDecimal.init(_exponent: Int32, _length: UInt32, _isNegative: UInt32, _isCompact: UInt32, _reserved: UInt32, _mantissa: (UInt16, UInt16, UInt16, UInt16, UInt16, UInt16, UInt16, UInt16))Added NSURL.init(fileReferenceLiteral: String)Modified [NSArray](https://developer.apple.com/documentation/foundation/nsarray)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSArray : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding, NSFastEnumeration {     var count: Int { get }     func objectAtIndex(_ index: Int) -> AnyObject     init()     init(objects objects: UnsafePointer<AnyObject?>, count cnt: Int)     init?(coder aDecoder: NSCoder) } extension NSArray : ArrayLiteralConvertible {     required convenience init(arrayLiteral elements: AnyObject...) } extension NSArray : SequenceType {     final func generate() -> NSFastGenerator } extension NSArray {     convenience init(objects elements: AnyObject...) } extension NSArray {     @objc(_swiftInitWithArray_NSArray:) convenience init(array anArray: NSArray) } extension NSArray : _Reflectable { } extension NSArray {     func arrayByAddingObject(_ anObject: AnyObject) -> [AnyObject]     func arrayByAddingObjectsFromArray(_ otherArray: [AnyObject]) -> [AnyObject]     func componentsJoinedByString(_ separator: String) -> String     func containsObject(_ anObject: AnyObject) -> Bool     var description: String { get }     func descriptionWithLocale(_ locale: AnyObject?) -> String     func descriptionWithLocale(_ locale: AnyObject?, indent level: Int) -> String     func firstObjectCommonWithArray(_ otherArray: [AnyObject]) -> AnyObject?     func getObjects(_ objects: AutoreleasingUnsafeMutablePointer<AnyObject?>, range range: NSRange)     func indexOfObject(_ anObject: AnyObject) -> Int     func indexOfObject(_ anObject: AnyObject, inRange range: NSRange) -> Int     func indexOfObjectIdenticalTo(_ anObject: AnyObject) -> Int     func indexOfObjectIdenticalTo(_ anObject: AnyObject, inRange range: NSRange) -> Int     func isEqualToArray(_ otherArray: [AnyObject]) -> Bool     var firstObject: AnyObject? { get }     var lastObject: AnyObject? { get }     func objectEnumerator() -> NSEnumerator     func reverseObjectEnumerator() -> NSEnumerator     @NSCopying var sortedArrayHint: NSData { get }     func sortedArrayUsingFunction(_ comparator: (AnyObject, AnyObject, UnsafeMutablePointer<Void>) -> Int, context context: UnsafeMutablePointer<Void>) -> [AnyObject]     func sortedArrayUsingFunction(_ comparator: (AnyObject, AnyObject, UnsafeMutablePointer<Void>) -> Int, context context: UnsafeMutablePointer<Void>, hint hint: NSData?) -> [AnyObject]     func sortedArrayUsingSelector(_ comparator: Selector) -> [AnyObject]     func subarrayWithRange(_ range: NSRange) -> [AnyObject]     func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool) -> Bool     func writeToURL(_ url: NSURL, atomically atomically: Bool) -> Bool     func makeObjectsPerformSelector(_ aSelector: Selector)     func makeObjectsPerformSelector(_ aSelector: Selector, withObject argument: AnyObject?)     func objectsAtIndexes(_ indexes: NSIndexSet) -> [AnyObject]     subscript (_ idx: Int) -> AnyObject { get }     func objectAtIndexedSubscript(_ idx: Int) -> AnyObject     func enumerateObjectsUsingBlock(_ block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, usingBlock block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func indexOfObjectPassingTest(_ predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexOfObjectWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexOfObjectAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexesOfObjectsPassingTest(_ predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexesOfObjectsWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexesOfObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func sortedArrayUsingComparator(_ cmptr: NSComparator) -> [AnyObject]     func sortedArrayWithOptions(_ opts: NSSortOptions, usingComparator cmptr: NSComparator) -> [AnyObject]     func indexOfObject(_ obj: AnyObject, inSortedRange r: NSRange, options opts: NSBinarySearchingOptions, usingComparator cmp: NSComparator) -> Int } extension NSArray {     convenience init()     class func array() -> Self     convenience init(object anObject: AnyObject)     class func arrayWithObject(_ anObject: AnyObject) -> Self     convenience init(objects objects: UnsafePointer<AnyObject?>, count cnt: Int)     class func arrayWithObjects(_ objects: UnsafePointer<AnyObject?>, count cnt: Int) -> Self     convenience init(array array: [AnyObject])     class func arrayWithArray(_ array: [AnyObject]) -> Self     convenience init(array array: [AnyObject])     convenience init(array array: [AnyObject], copyItems flag: Bool)      init?(contentsOfFile path: String)     class func arrayWithContentsOfFile(_ path: String) -> [AnyObject]?      init?(contentsOfURL url: NSURL)     class func arrayWithContentsOfURL(_ url: NSURL) -> [AnyObject]?     convenience init?(contentsOfFile path: String)     convenience init?(contentsOfURL url: NSURL) } extension NSArray {     func getObjects(_ objects: AutoreleasingUnsafeMutablePointer<AnyObject?>) } extension NSArray {     func valueForKey(_ key: String) -> AnyObject     func setValue(_ value: AnyObject?, forKey key: String) } extension NSArray {     func addObserver(_ observer: NSObject, toObjectsAtIndexes indexes: NSIndexSet, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, fromObjectsAtIndexes indexes: NSIndexSet, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, fromObjectsAtIndexes indexes: NSIndexSet, forKeyPath keyPath: String)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String) } extension NSArray {     func pathsMatchingExtensions(_ filterTypes: [String]) -> [String] } extension NSArray {     func filteredArrayUsingPredicate(_ predicate: NSPredicate) -> [AnyObject] } extension NSArray {     func sortedArrayUsingDescriptors(_ sortDescriptors: [NSSortDescriptor]) -> [AnyObject] } extension NSArray : _Reflectable { } extension NSArray {     @objc(_swiftInitWithArray_NSArray:) convenience init(array anArray: NSArray) } extension NSArray {     convenience init(objects elements: AnyObject...) } extension NSArray : SequenceType {     final func generate() -> NSFastGenerator } extension NSArray : ArrayLiteralConvertible {     required convenience init(arrayLiteral elements: AnyObject...) } ``` | AnyObject, ArrayLiteralConvertible, NSCoding, NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding, SequenceType |
| To | ``` class NSArray : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSFastEnumeration {     var count: Int { get }     func objectAtIndex(_ index: Int) -> AnyObject     init()     init(objects objects: UnsafePointer<AnyObject?>, count cnt: Int)     init?(coder aDecoder: NSCoder) } extension NSArray : ArrayLiteralConvertible {     required convenience init(arrayLiteral elements: AnyObject...) } extension NSArray : SequenceType {     final func generate() -> NSFastGenerator } extension NSArray {     convenience init(objects elements: AnyObject...) } extension NSArray {     @objc(_swiftInitWithArray_NSArray:) convenience init(array anArray: NSArray) } extension NSArray : _Reflectable { } extension NSArray {     func arrayByAddingObject(_ anObject: AnyObject) -> [AnyObject]     func arrayByAddingObjectsFromArray(_ otherArray: [AnyObject]) -> [AnyObject]     func componentsJoinedByString(_ separator: String) -> String     func containsObject(_ anObject: AnyObject) -> Bool     var description: String { get }     func descriptionWithLocale(_ locale: AnyObject?) -> String     func descriptionWithLocale(_ locale: AnyObject?, indent level: Int) -> String     func firstObjectCommonWithArray(_ otherArray: [AnyObject]) -> AnyObject?     func getObjects(_ objects: AutoreleasingUnsafeMutablePointer<AnyObject?>, range range: NSRange)     func indexOfObject(_ anObject: AnyObject) -> Int     func indexOfObject(_ anObject: AnyObject, inRange range: NSRange) -> Int     func indexOfObjectIdenticalTo(_ anObject: AnyObject) -> Int     func indexOfObjectIdenticalTo(_ anObject: AnyObject, inRange range: NSRange) -> Int     func isEqualToArray(_ otherArray: [AnyObject]) -> Bool     var firstObject: AnyObject? { get }     var lastObject: AnyObject? { get }     func objectEnumerator() -> NSEnumerator     func reverseObjectEnumerator() -> NSEnumerator     @NSCopying var sortedArrayHint: NSData { get }     func sortedArrayUsingFunction(_ comparator: (AnyObject, AnyObject, UnsafeMutablePointer<Void>) -> Int, context context: UnsafeMutablePointer<Void>) -> [AnyObject]     func sortedArrayUsingFunction(_ comparator: (AnyObject, AnyObject, UnsafeMutablePointer<Void>) -> Int, context context: UnsafeMutablePointer<Void>, hint hint: NSData?) -> [AnyObject]     func sortedArrayUsingSelector(_ comparator: Selector) -> [AnyObject]     func subarrayWithRange(_ range: NSRange) -> [AnyObject]     func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool) -> Bool     func writeToURL(_ url: NSURL, atomically atomically: Bool) -> Bool     func makeObjectsPerformSelector(_ aSelector: Selector)     func makeObjectsPerformSelector(_ aSelector: Selector, withObject argument: AnyObject?)     func objectsAtIndexes(_ indexes: NSIndexSet) -> [AnyObject]     subscript (_ idx: Int) -> AnyObject { get }     func objectAtIndexedSubscript(_ idx: Int) -> AnyObject     func enumerateObjectsUsingBlock(_ block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, usingBlock block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func indexOfObjectPassingTest(_ predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexOfObjectWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexOfObjectAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexesOfObjectsPassingTest(_ predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexesOfObjectsWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexesOfObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func sortedArrayUsingComparator(_ cmptr: NSComparator) -> [AnyObject]     func sortedArrayWithOptions(_ opts: NSSortOptions, usingComparator cmptr: NSComparator) -> [AnyObject]     func indexOfObject(_ obj: AnyObject, inSortedRange r: NSRange, options opts: NSBinarySearchingOptions, usingComparator cmp: NSComparator) -> Int } extension NSArray {     convenience init()     class func array() -> Self     convenience init(object anObject: AnyObject)     class func arrayWithObject(_ anObject: AnyObject) -> Self     convenience init(objects objects: UnsafePointer<AnyObject?>, count cnt: Int)     class func arrayWithObjects(_ objects: UnsafePointer<AnyObject?>, count cnt: Int) -> Self     convenience init(array array: [AnyObject])     class func arrayWithArray(_ array: [AnyObject]) -> Self     convenience init(array array: [AnyObject])     convenience init(array array: [AnyObject], copyItems flag: Bool)      init?(contentsOfFile path: String)     class func arrayWithContentsOfFile(_ path: String) -> [AnyObject]?      init?(contentsOfURL url: NSURL)     class func arrayWithContentsOfURL(_ url: NSURL) -> [AnyObject]?     convenience init?(contentsOfFile path: String)     convenience init?(contentsOfURL url: NSURL) } extension NSArray {     func getObjects(_ objects: AutoreleasingUnsafeMutablePointer<AnyObject?>) } extension NSArray {     func valueForKey(_ key: String) -> AnyObject     func setValue(_ value: AnyObject?, forKey key: String) } extension NSArray {     func addObserver(_ observer: NSObject, toObjectsAtIndexes indexes: NSIndexSet, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, fromObjectsAtIndexes indexes: NSIndexSet, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, fromObjectsAtIndexes indexes: NSIndexSet, forKeyPath keyPath: String)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String) } extension NSArray {     func pathsMatchingExtensions(_ filterTypes: [String]) -> [String] } extension NSArray {     func filteredArrayUsingPredicate(_ predicate: NSPredicate) -> [AnyObject] } extension NSArray {     func sortedArrayUsingDescriptors(_ sortDescriptors: [NSSortDescriptor]) -> [AnyObject] } extension NSArray : _Reflectable { } extension NSArray {     @objc(_swiftInitWithArray_NSArray:) convenience init(array anArray: NSArray) } extension NSArray {     convenience init(objects elements: AnyObject...) } extension NSArray : SequenceType {     final func generate() -> NSFastGenerator } extension NSArray : ArrayLiteralConvertible {     required convenience init(arrayLiteral elements: AnyObject...) } ``` | ArrayLiteralConvertible, NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding, SequenceType |

Modified [NSAssertionHandler](https://developer.apple.com/documentation/foundation/nsassertionhandler)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSAttributedString](https://developer.apple.com/documentation/foundation/nsattributedstring)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSAttributedString : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     var string: String { get }     func attributesAtIndex(_ location: Int, effectiveRange range: NSRangePointer) -> [String : AnyObject] } extension NSAttributedString {     var length: Int { get }     func attribute(_ attrName: String, atIndex location: Int, effectiveRange range: NSRangePointer) -> AnyObject?     func attributedSubstringFromRange(_ range: NSRange) -> NSAttributedString     func attributesAtIndex(_ location: Int, longestEffectiveRange range: NSRangePointer, inRange rangeLimit: NSRange) -> [String : AnyObject]     func attribute(_ attrName: String, atIndex location: Int, longestEffectiveRange range: NSRangePointer, inRange rangeLimit: NSRange) -> AnyObject?     func isEqualToAttributedString(_ other: NSAttributedString) -> Bool     init(string str: String)     init(string str: String, attributes attrs: [String : AnyObject]?)     init(attributedString attrStr: NSAttributedString)     func enumerateAttributesInRange(_ enumerationRange: NSRange, options opts: NSAttributedStringEnumerationOptions, usingBlock block: ([String : AnyObject], NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateAttribute(_ attrName: String, inRange enumerationRange: NSRange, options opts: NSAttributedStringEnumerationOptions, usingBlock block: (AnyObject?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) } extension NSAttributedString {     init(URL url: NSURL, options options: [String : AnyObject], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws     init(data data: NSData, options options: [String : AnyObject], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws     func dataFromRange(_ range: NSRange, documentAttributes dict: [String : AnyObject]) throws -> NSData     func fileWrapperFromRange(_ range: NSRange, documentAttributes dict: [String : AnyObject]) throws -> NSFileWrapper } extension NSAttributedString {     func containsAttachmentsInRange(_ range: NSRange) -> Bool } extension NSAttributedString {     init(fileURL url: NSURL, options options: [NSObject : AnyObject], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws } extension NSAttributedString {     func size() -> CGSize     func drawAtPoint(_ point: CGPoint)     func drawInRect(_ rect: CGRect) } extension NSAttributedString {     func drawWithRect(_ rect: CGRect, options options: NSStringDrawingOptions, context context: NSStringDrawingContext?)     func boundingRectWithSize(_ size: CGSize, options options: NSStringDrawingOptions, context context: NSStringDrawingContext?) -> CGRect } ``` | AnyObject, NSCoding, NSCopying, NSMutableCopying, NSSecureCoding |
| To | ``` class NSAttributedString : NSObject, NSCopying, NSMutableCopying, NSSecureCoding {     var string: String { get }     func attributesAtIndex(_ location: Int, effectiveRange range: NSRangePointer) -> [String : AnyObject] } extension NSAttributedString {     var length: Int { get }     func attribute(_ attrName: String, atIndex location: Int, effectiveRange range: NSRangePointer) -> AnyObject?     func attributedSubstringFromRange(_ range: NSRange) -> NSAttributedString     func attributesAtIndex(_ location: Int, longestEffectiveRange range: NSRangePointer, inRange rangeLimit: NSRange) -> [String : AnyObject]     func attribute(_ attrName: String, atIndex location: Int, longestEffectiveRange range: NSRangePointer, inRange rangeLimit: NSRange) -> AnyObject?     func isEqualToAttributedString(_ other: NSAttributedString) -> Bool     init(string str: String)     init(string str: String, attributes attrs: [String : AnyObject]?)     init(attributedString attrStr: NSAttributedString)     func enumerateAttributesInRange(_ enumerationRange: NSRange, options opts: NSAttributedStringEnumerationOptions, usingBlock block: ([String : AnyObject], NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateAttribute(_ attrName: String, inRange enumerationRange: NSRange, options opts: NSAttributedStringEnumerationOptions, usingBlock block: (AnyObject?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) } extension NSAttributedString {     init(URL url: NSURL, options options: [String : AnyObject], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws     init(data data: NSData, options options: [String : AnyObject], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws     func dataFromRange(_ range: NSRange, documentAttributes dict: [String : AnyObject]) throws -> NSData     func fileWrapperFromRange(_ range: NSRange, documentAttributes dict: [String : AnyObject]) throws -> NSFileWrapper } extension NSAttributedString {     func containsAttachmentsInRange(_ range: NSRange) -> Bool } extension NSAttributedString {     init(fileURL url: NSURL, options options: [NSObject : AnyObject], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws } extension NSAttributedString {     func size() -> CGSize     func drawAtPoint(_ point: CGPoint)     func drawInRect(_ rect: CGRect) } extension NSAttributedString {     func drawWithRect(_ rect: CGRect, options options: NSStringDrawingOptions, context context: NSStringDrawingContext?)     func boundingRectWithSize(_ size: CGSize, options options: NSStringDrawingOptions, context context: NSStringDrawingContext?) -> CGRect } ``` | NSCopying, NSMutableCopying, NSSecureCoding |

Modified [NSBlockOperation](https://developer.apple.com/documentation/foundation/nsblockoperation)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSBundle](https://developer.apple.com/documentation/foundation/nsbundle)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSBundleResourceRequest](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSObjectProtocol, NSProgressReporting |
| To | NSProgressReporting |

Modified [NSByteCountFormatter](https://developer.apple.com/documentation/foundation/nsbytecountformatter)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSByteCountFormatterCountStyle [enum]](https://developer.apple.com/documentation/foundation/nsbytecountformattercountstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSCache](https://developer.apple.com/documentation/foundation/nscache)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSCachedURLResponse](https://developer.apple.com/documentation/foundation/cachedurlresponse)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSCachedURLResponse : NSObject, NSSecureCoding, NSCoding, NSCopying {     init(response response: NSURLResponse, data data: NSData)     init(response response: NSURLResponse, data data: NSData, userInfo userInfo: [NSObject : AnyObject]?, storagePolicy storagePolicy: NSURLCacheStoragePolicy)     @NSCopying var response: NSURLResponse { get }     @NSCopying var data: NSData { get }     var userInfo: [NSObject : AnyObject]? { get }     var storagePolicy: NSURLCacheStoragePolicy { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NSCachedURLResponse : NSObject, NSSecureCoding, NSCopying {     init(response response: NSURLResponse, data data: NSData)     init(response response: NSURLResponse, data data: NSData, userInfo userInfo: [NSObject : AnyObject]?, storagePolicy storagePolicy: NSURLCacheStoragePolicy)     @NSCopying var response: NSURLResponse { get }     @NSCopying var data: NSData { get }     var userInfo: [NSObject : AnyObject]? { get }     var storagePolicy: NSURLCacheStoragePolicy { get } } ``` | NSCopying, NSSecureCoding |

Modified [NSCalculationError [enum]](https://developer.apple.com/documentation/foundation/nscalculationerror)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSCalendar](https://developer.apple.com/documentation/foundation/nscalendar)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSCalendar : NSObject, NSCopying, NSSecureCoding, NSCoding {     class func currentCalendar() -> NSCalendar     class func autoupdatingCurrentCalendar() -> NSCalendar      init?(identifier calendarIdentifierConstant: String)     class func calendarWithIdentifier(_ calendarIdentifierConstant: String) -> NSCalendar?     convenience init()     init?(calendarIdentifier ident: String)     var calendarIdentifier: String { get }     @NSCopying var locale: NSLocale?     @NSCopying var timeZone: NSTimeZone     var firstWeekday: Int     var minimumDaysInFirstWeek: Int     var eraSymbols: [String] { get }     var longEraSymbols: [String] { get }     var monthSymbols: [String] { get }     var shortMonthSymbols: [String] { get }     var veryShortMonthSymbols: [String] { get }     var standaloneMonthSymbols: [String] { get }     var shortStandaloneMonthSymbols: [String] { get }     var veryShortStandaloneMonthSymbols: [String] { get }     var weekdaySymbols: [String] { get }     var shortWeekdaySymbols: [String] { get }     var veryShortWeekdaySymbols: [String] { get }     var standaloneWeekdaySymbols: [String] { get }     var shortStandaloneWeekdaySymbols: [String] { get }     var veryShortStandaloneWeekdaySymbols: [String] { get }     var quarterSymbols: [String] { get }     var shortQuarterSymbols: [String] { get }     var standaloneQuarterSymbols: [String] { get }     var shortStandaloneQuarterSymbols: [String] { get }     var AMSymbol: String { get }     var PMSymbol: String { get }     func minimumRangeOfUnit(_ unit: NSCalendarUnit) -> NSRange     func maximumRangeOfUnit(_ unit: NSCalendarUnit) -> NSRange     func rangeOfUnit(_ smaller: NSCalendarUnit, inUnit larger: NSCalendarUnit, forDate date: NSDate) -> NSRange     func ordinalityOfUnit(_ smaller: NSCalendarUnit, inUnit larger: NSCalendarUnit, forDate date: NSDate) -> Int     func rangeOfUnit(_ unit: NSCalendarUnit, startDate datep: AutoreleasingUnsafeMutablePointer<NSDate?>, interval tip: UnsafeMutablePointer<NSTimeInterval>, forDate date: NSDate) -> Bool     func dateFromComponents(_ comps: NSDateComponents) -> NSDate?     func components(_ unitFlags: NSCalendarUnit, fromDate date: NSDate) -> NSDateComponents     func dateByAddingComponents(_ comps: NSDateComponents, toDate date: NSDate, options opts: NSCalendarOptions) -> NSDate?     func components(_ unitFlags: NSCalendarUnit, fromDate startingDate: NSDate, toDate resultDate: NSDate, options opts: NSCalendarOptions) -> NSDateComponents     func getEra(_ eraValuePointer: UnsafeMutablePointer<Int>, year yearValuePointer: UnsafeMutablePointer<Int>, month monthValuePointer: UnsafeMutablePointer<Int>, day dayValuePointer: UnsafeMutablePointer<Int>, fromDate date: NSDate)     func getEra(_ eraValuePointer: UnsafeMutablePointer<Int>, yearForWeekOfYear yearValuePointer: UnsafeMutablePointer<Int>, weekOfYear weekValuePointer: UnsafeMutablePointer<Int>, weekday weekdayValuePointer: UnsafeMutablePointer<Int>, fromDate date: NSDate)     func getHour(_ hourValuePointer: UnsafeMutablePointer<Int>, minute minuteValuePointer: UnsafeMutablePointer<Int>, second secondValuePointer: UnsafeMutablePointer<Int>, nanosecond nanosecondValuePointer: UnsafeMutablePointer<Int>, fromDate date: NSDate)     func component(_ unit: NSCalendarUnit, fromDate date: NSDate) -> Int     func dateWithEra(_ eraValue: Int, year yearValue: Int, month monthValue: Int, day dayValue: Int, hour hourValue: Int, minute minuteValue: Int, second secondValue: Int, nanosecond nanosecondValue: Int) -> NSDate?     func dateWithEra(_ eraValue: Int, yearForWeekOfYear yearValue: Int, weekOfYear weekValue: Int, weekday weekdayValue: Int, hour hourValue: Int, minute minuteValue: Int, second secondValue: Int, nanosecond nanosecondValue: Int) -> NSDate?     func startOfDayForDate(_ date: NSDate) -> NSDate     func componentsInTimeZone(_ timezone: NSTimeZone, fromDate date: NSDate) -> NSDateComponents     func compareDate(_ date1: NSDate, toDate date2: NSDate, toUnitGranularity unit: NSCalendarUnit) -> NSComparisonResult     func isDate(_ date1: NSDate, equalToDate date2: NSDate, toUnitGranularity unit: NSCalendarUnit) -> Bool     func isDate(_ date1: NSDate, inSameDayAsDate date2: NSDate) -> Bool     func isDateInToday(_ date: NSDate) -> Bool     func isDateInYesterday(_ date: NSDate) -> Bool     func isDateInTomorrow(_ date: NSDate) -> Bool     func isDateInWeekend(_ date: NSDate) -> Bool     func rangeOfWeekendStartDate(_ datep: AutoreleasingUnsafeMutablePointer<NSDate?>, interval tip: UnsafeMutablePointer<NSTimeInterval>, containingDate date: NSDate) -> Bool     func nextWeekendStartDate(_ datep: AutoreleasingUnsafeMutablePointer<NSDate?>, interval tip: UnsafeMutablePointer<NSTimeInterval>, options options: NSCalendarOptions, afterDate date: NSDate) -> Bool     func components(_ unitFlags: NSCalendarUnit, fromDateComponents startingDateComp: NSDateComponents, toDateComponents resultDateComp: NSDateComponents, options options: NSCalendarOptions) -> NSDateComponents     func dateByAddingUnit(_ unit: NSCalendarUnit, value value: Int, toDate date: NSDate, options options: NSCalendarOptions) -> NSDate?     func enumerateDatesStartingAfterDate(_ start: NSDate, matchingComponents comps: NSDateComponents, options opts: NSCalendarOptions, usingBlock block: (NSDate?, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)     func nextDateAfterDate(_ date: NSDate, matchingComponents comps: NSDateComponents, options options: NSCalendarOptions) -> NSDate?     func nextDateAfterDate(_ date: NSDate, matchingUnit unit: NSCalendarUnit, value value: Int, options options: NSCalendarOptions) -> NSDate?     func nextDateAfterDate(_ date: NSDate, matchingHour hourValue: Int, minute minuteValue: Int, second secondValue: Int, options options: NSCalendarOptions) -> NSDate?     func dateBySettingUnit(_ unit: NSCalendarUnit, value v: Int, ofDate date: NSDate, options opts: NSCalendarOptions) -> NSDate?     func dateBySettingHour(_ h: Int, minute m: Int, second s: Int, ofDate date: NSDate, options opts: NSCalendarOptions) -> NSDate?     func date(_ date: NSDate, matchesComponents components: NSDateComponents) -> Bool } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NSCalendar : NSObject, NSCopying, NSSecureCoding {     class func currentCalendar() -> NSCalendar     class func autoupdatingCurrentCalendar() -> NSCalendar      init?(identifier calendarIdentifierConstant: String)     class func calendarWithIdentifier(_ calendarIdentifierConstant: String) -> NSCalendar?     convenience init()     init?(calendarIdentifier ident: String)     var calendarIdentifier: String { get }     @NSCopying var locale: NSLocale?     @NSCopying var timeZone: NSTimeZone     var firstWeekday: Int     var minimumDaysInFirstWeek: Int     var eraSymbols: [String] { get }     var longEraSymbols: [String] { get }     var monthSymbols: [String] { get }     var shortMonthSymbols: [String] { get }     var veryShortMonthSymbols: [String] { get }     var standaloneMonthSymbols: [String] { get }     var shortStandaloneMonthSymbols: [String] { get }     var veryShortStandaloneMonthSymbols: [String] { get }     var weekdaySymbols: [String] { get }     var shortWeekdaySymbols: [String] { get }     var veryShortWeekdaySymbols: [String] { get }     var standaloneWeekdaySymbols: [String] { get }     var shortStandaloneWeekdaySymbols: [String] { get }     var veryShortStandaloneWeekdaySymbols: [String] { get }     var quarterSymbols: [String] { get }     var shortQuarterSymbols: [String] { get }     var standaloneQuarterSymbols: [String] { get }     var shortStandaloneQuarterSymbols: [String] { get }     var AMSymbol: String { get }     var PMSymbol: String { get }     func minimumRangeOfUnit(_ unit: NSCalendarUnit) -> NSRange     func maximumRangeOfUnit(_ unit: NSCalendarUnit) -> NSRange     func rangeOfUnit(_ smaller: NSCalendarUnit, inUnit larger: NSCalendarUnit, forDate date: NSDate) -> NSRange     func ordinalityOfUnit(_ smaller: NSCalendarUnit, inUnit larger: NSCalendarUnit, forDate date: NSDate) -> Int     func rangeOfUnit(_ unit: NSCalendarUnit, startDate datep: AutoreleasingUnsafeMutablePointer<NSDate?>, interval tip: UnsafeMutablePointer<NSTimeInterval>, forDate date: NSDate) -> Bool     func dateFromComponents(_ comps: NSDateComponents) -> NSDate?     func components(_ unitFlags: NSCalendarUnit, fromDate date: NSDate) -> NSDateComponents     func dateByAddingComponents(_ comps: NSDateComponents, toDate date: NSDate, options opts: NSCalendarOptions) -> NSDate?     func components(_ unitFlags: NSCalendarUnit, fromDate startingDate: NSDate, toDate resultDate: NSDate, options opts: NSCalendarOptions) -> NSDateComponents     func getEra(_ eraValuePointer: UnsafeMutablePointer<Int>, year yearValuePointer: UnsafeMutablePointer<Int>, month monthValuePointer: UnsafeMutablePointer<Int>, day dayValuePointer: UnsafeMutablePointer<Int>, fromDate date: NSDate)     func getEra(_ eraValuePointer: UnsafeMutablePointer<Int>, yearForWeekOfYear yearValuePointer: UnsafeMutablePointer<Int>, weekOfYear weekValuePointer: UnsafeMutablePointer<Int>, weekday weekdayValuePointer: UnsafeMutablePointer<Int>, fromDate date: NSDate)     func getHour(_ hourValuePointer: UnsafeMutablePointer<Int>, minute minuteValuePointer: UnsafeMutablePointer<Int>, second secondValuePointer: UnsafeMutablePointer<Int>, nanosecond nanosecondValuePointer: UnsafeMutablePointer<Int>, fromDate date: NSDate)     func component(_ unit: NSCalendarUnit, fromDate date: NSDate) -> Int     func dateWithEra(_ eraValue: Int, year yearValue: Int, month monthValue: Int, day dayValue: Int, hour hourValue: Int, minute minuteValue: Int, second secondValue: Int, nanosecond nanosecondValue: Int) -> NSDate?     func dateWithEra(_ eraValue: Int, yearForWeekOfYear yearValue: Int, weekOfYear weekValue: Int, weekday weekdayValue: Int, hour hourValue: Int, minute minuteValue: Int, second secondValue: Int, nanosecond nanosecondValue: Int) -> NSDate?     func startOfDayForDate(_ date: NSDate) -> NSDate     func componentsInTimeZone(_ timezone: NSTimeZone, fromDate date: NSDate) -> NSDateComponents     func compareDate(_ date1: NSDate, toDate date2: NSDate, toUnitGranularity unit: NSCalendarUnit) -> NSComparisonResult     func isDate(_ date1: NSDate, equalToDate date2: NSDate, toUnitGranularity unit: NSCalendarUnit) -> Bool     func isDate(_ date1: NSDate, inSameDayAsDate date2: NSDate) -> Bool     func isDateInToday(_ date: NSDate) -> Bool     func isDateInYesterday(_ date: NSDate) -> Bool     func isDateInTomorrow(_ date: NSDate) -> Bool     func isDateInWeekend(_ date: NSDate) -> Bool     func rangeOfWeekendStartDate(_ datep: AutoreleasingUnsafeMutablePointer<NSDate?>, interval tip: UnsafeMutablePointer<NSTimeInterval>, containingDate date: NSDate) -> Bool     func nextWeekendStartDate(_ datep: AutoreleasingUnsafeMutablePointer<NSDate?>, interval tip: UnsafeMutablePointer<NSTimeInterval>, options options: NSCalendarOptions, afterDate date: NSDate) -> Bool     func components(_ unitFlags: NSCalendarUnit, fromDateComponents startingDateComp: NSDateComponents, toDateComponents resultDateComp: NSDateComponents, options options: NSCalendarOptions) -> NSDateComponents     func dateByAddingUnit(_ unit: NSCalendarUnit, value value: Int, toDate date: NSDate, options options: NSCalendarOptions) -> NSDate?     func enumerateDatesStartingAfterDate(_ start: NSDate, matchingComponents comps: NSDateComponents, options opts: NSCalendarOptions, usingBlock block: (NSDate?, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)     func nextDateAfterDate(_ date: NSDate, matchingComponents comps: NSDateComponents, options options: NSCalendarOptions) -> NSDate?     func nextDateAfterDate(_ date: NSDate, matchingUnit unit: NSCalendarUnit, value value: Int, options options: NSCalendarOptions) -> NSDate?     func nextDateAfterDate(_ date: NSDate, matchingHour hourValue: Int, minute minuteValue: Int, second secondValue: Int, options options: NSCalendarOptions) -> NSDate?     func dateBySettingUnit(_ unit: NSCalendarUnit, value v: Int, ofDate date: NSDate, options opts: NSCalendarOptions) -> NSDate?     func dateBySettingHour(_ h: Int, minute m: Int, second s: Int, ofDate date: NSDate, options opts: NSCalendarOptions) -> NSDate?     func date(_ date: NSDate, matchesComponents components: NSDateComponents) -> Bool } ``` | NSCopying, NSSecureCoding |

Modified [NSCharacterSet](https://developer.apple.com/documentation/foundation/nscharacterset)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying, NSMutableCopying |
| To | NSCoding, NSCopying, NSMutableCopying |

Modified NSCocoaError [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSCocoaError : _ObjectiveCBridgeableErrorType, ErrorType, __BridgedNSError, RawRepresentable, _BridgedNSError, Hashable, Equatable {     let rawValue: Int     init(rawValue rawValue: Int) } extension NSCocoaError {     static let ManagedObjectValidationError: NSCocoaError     static let ValidationMultipleErrorsError: NSCocoaError     static let ValidationMissingMandatoryPropertyError: NSCocoaError     static let ValidationRelationshipLacksMinimumCountError: NSCocoaError     static let ValidationRelationshipExceedsMaximumCountError: NSCocoaError     static let ValidationRelationshipDeniedDeleteError: NSCocoaError     static let ValidationNumberTooLargeError: NSCocoaError     static let ValidationNumberTooSmallError: NSCocoaError     static let ValidationDateTooLateError: NSCocoaError     static let ValidationDateTooSoonError: NSCocoaError     static let ValidationInvalidDateError: NSCocoaError     static let ValidationStringTooLongError: NSCocoaError     static let ValidationStringTooShortError: NSCocoaError     static let ValidationStringPatternMatchingError: NSCocoaError     static let ManagedObjectContextLockingError: NSCocoaError     static let PersistentStoreCoordinatorLockingError: NSCocoaError     static let ManagedObjectReferentialIntegrityError: NSCocoaError     static let ManagedObjectExternalRelationshipError: NSCocoaError     static let ManagedObjectMergeError: NSCocoaError     static let ManagedObjectConstraintMergeError: NSCocoaError     static let PersistentStoreInvalidTypeError: NSCocoaError     static let PersistentStoreTypeMismatchError: NSCocoaError     static let PersistentStoreIncompatibleSchemaError: NSCocoaError     static let PersistentStoreSaveError: NSCocoaError     static let PersistentStoreIncompleteSaveError: NSCocoaError     static let PersistentStoreSaveConflictsError: NSCocoaError     static let CoreDataError: NSCocoaError     static let PersistentStoreOperationError: NSCocoaError     static let PersistentStoreOpenError: NSCocoaError     static let PersistentStoreTimeoutError: NSCocoaError     static let PersistentStoreUnsupportedRequestTypeError: NSCocoaError     static let PersistentStoreIncompatibleVersionHashError: NSCocoaError     static let MigrationError: NSCocoaError     static let MigrationCancelledError: NSCocoaError     static let MigrationMissingSourceModelError: NSCocoaError     static let MigrationMissingMappingModelError: NSCocoaError     static let MigrationManagerSourceStoreError: NSCocoaError     static let MigrationManagerDestinationStoreError: NSCocoaError     static let EntityMigrationPolicyError: NSCocoaError     static let SQLiteError: NSCocoaError     static let InferredMappingModelError: NSCocoaError     static let ExternalRecordImportError: NSCocoaError } extension NSCocoaError {     static let FileNoSuchFileError: NSCocoaError     static let FileLockingError: NSCocoaError     static let FileReadUnknownError: NSCocoaError     static let FileReadNoPermissionError: NSCocoaError     static let FileReadInvalidFileNameError: NSCocoaError     static let FileReadCorruptFileError: NSCocoaError     static let FileReadNoSuchFileError: NSCocoaError     static let FileReadInapplicableStringEncodingError: NSCocoaError     static let FileReadUnsupportedSchemeError: NSCocoaError     static let FileReadTooLargeError: NSCocoaError     static let FileReadUnknownStringEncodingError: NSCocoaError     static let FileWriteUnknownError: NSCocoaError     static let FileWriteNoPermissionError: NSCocoaError     static let FileWriteInvalidFileNameError: NSCocoaError     static let FileWriteFileExistsError: NSCocoaError     static let FileWriteInapplicableStringEncodingError: NSCocoaError     static let FileWriteUnsupportedSchemeError: NSCocoaError     static let FileWriteOutOfSpaceError: NSCocoaError     static let FileWriteVolumeReadOnlyError: NSCocoaError     static let FileManagerUnmountUnknownError: NSCocoaError     static let FileManagerUnmountBusyError: NSCocoaError     static let KeyValueValidationError: NSCocoaError     static let FormattingError: NSCocoaError     static let UserCancelledError: NSCocoaError     static let FeatureUnsupportedError: NSCocoaError     static let ExecutableNotLoadableError: NSCocoaError     static let ExecutableArchitectureMismatchError: NSCocoaError     static let ExecutableRuntimeMismatchError: NSCocoaError     static let ExecutableLoadError: NSCocoaError     static let ExecutableLinkError: NSCocoaError     static let PropertyListReadCorruptError: NSCocoaError     static let PropertyListReadUnknownVersionError: NSCocoaError     static let PropertyListReadStreamError: NSCocoaError     static let PropertyListWriteStreamError: NSCocoaError     static let PropertyListWriteInvalidError: NSCocoaError     static let XPCConnectionInterrupted: NSCocoaError     static let XPCConnectionInvalid: NSCocoaError     static let XPCConnectionReplyInvalid: NSCocoaError     static let UbiquitousFileUnavailableError: NSCocoaError     static let UbiquitousFileNotUploadedDueToQuotaError: NSCocoaError     static let UbiquitousFileUbiquityServerNotAvailable: NSCocoaError     static let UserActivityHandoffFailedError: NSCocoaError     static let UserActivityConnectionUnavailableError: NSCocoaError     static let UserActivityRemoteApplicationTimedOutError: NSCocoaError     static let UserActivityHandoffUserInfoTooLargeError: NSCocoaError     static let CoderReadCorruptError: NSCocoaError     static let CoderValueNotFoundError: NSCocoaError     var isCoderError: Bool { get }     var isExecutableError: Bool { get }     var isFileError: Bool { get }     var isFormattingError: Bool { get }     var isPropertyListError: Bool { get }     var isUbiquitousFileError: Bool { get }     var isUserActivityError: Bool { get }     var isValidationError: Bool { get }     var isXPCConnectionError: Bool { get } } ``` | Equatable, ErrorType, Hashable, RawRepresentable |
| To | ``` struct NSCocoaError : RawRepresentable, _BridgedNSError {     let rawValue: Int     init(rawValue rawValue: Int) } extension NSCocoaError {     static var ManagedObjectValidationError: NSCocoaError { get }     static var ValidationMultipleErrorsError: NSCocoaError { get }     static var ValidationMissingMandatoryPropertyError: NSCocoaError { get }     static var ValidationRelationshipLacksMinimumCountError: NSCocoaError { get }     static var ValidationRelationshipExceedsMaximumCountError: NSCocoaError { get }     static var ValidationRelationshipDeniedDevareError: NSCocoaError { get }     static var ValidationNumberTooLargeError: NSCocoaError { get }     static var ValidationNumberTooSmallError: NSCocoaError { get }     static var ValidationDateTooLateError: NSCocoaError { get }     static var ValidationDateTooSoonError: NSCocoaError { get }     static var ValidationInvalidDateError: NSCocoaError { get }     static var ValidationStringTooLongError: NSCocoaError { get }     static var ValidationStringTooShortError: NSCocoaError { get }     static var ValidationStringPatternMatchingError: NSCocoaError { get }     static var ManagedObjectContextLockingError: NSCocoaError { get }     static var PersistentStoreCoordinatorLockingError: NSCocoaError { get }     static var ManagedObjectReferentialIntegrityError: NSCocoaError { get }     static var ManagedObjectExternalRelationshipError: NSCocoaError { get }     static var ManagedObjectMergeError: NSCocoaError { get }     static var ManagedObjectConstraintMergeError: NSCocoaError { get }     static var PersistentStoreInvalidTypeError: NSCocoaError { get }     static var PersistentStoreTypeMismatchError: NSCocoaError { get }     static var PersistentStoreIncompatibleSchemaError: NSCocoaError { get }     static var PersistentStoreSaveError: NSCocoaError { get }     static var PersistentStoreIncompvareSaveError: NSCocoaError { get }     static var PersistentStoreSaveConflictsError: NSCocoaError { get }     static var CoreDataError: NSCocoaError { get }     static var PersistentStoreOperationError: NSCocoaError { get }     static var PersistentStoreOpenError: NSCocoaError { get }     static var PersistentStoreTimeoutError: NSCocoaError { get }     static var PersistentStoreUnsupportedRequestTypeError: NSCocoaError { get }     static var PersistentStoreIncompatibleVersionHashError: NSCocoaError { get }     static var MigrationError: NSCocoaError { get }     static var MigrationCancelledError: NSCocoaError { get }     static var MigrationMissingSourceModelError: NSCocoaError { get }     static var MigrationMissingMappingModelError: NSCocoaError { get }     static var MigrationManagerSourceStoreError: NSCocoaError { get }     static var MigrationManagerDestinationStoreError: NSCocoaError { get }     static var EntityMigrationPolicyError: NSCocoaError { get }     static var SQLiteError: NSCocoaError { get }     static var InferredMappingModelError: NSCocoaError { get }     static var ExternalRecordImportError: NSCocoaError { get } } extension NSCocoaError {     static var FileNoSuchFileError: NSCocoaError { get }     static var FileLockingError: NSCocoaError { get }     static var FileReadUnknownError: NSCocoaError { get }     static var FileReadNoPermissionError: NSCocoaError { get }     static var FileReadInvalidFileNameError: NSCocoaError { get }     static var FileReadCorruptFileError: NSCocoaError { get }     static var FileReadNoSuchFileError: NSCocoaError { get }     static var FileReadInapplicableStringEncodingError: NSCocoaError { get }     static var FileReadUnsupportedSchemeError: NSCocoaError { get }     static var FileReadTooLargeError: NSCocoaError { get }     static var FileReadUnknownStringEncodingError: NSCocoaError { get }     static var FileWriteUnknownError: NSCocoaError { get }     static var FileWriteNoPermissionError: NSCocoaError { get }     static var FileWriteInvalidFileNameError: NSCocoaError { get }     static var FileWriteFileExistsError: NSCocoaError { get }     static var FileWriteInapplicableStringEncodingError: NSCocoaError { get }     static var FileWriteUnsupportedSchemeError: NSCocoaError { get }     static var FileWriteOutOfSpaceError: NSCocoaError { get }     static var FileWriteVolumeReadOnlyError: NSCocoaError { get }     static var FileManagerUnmountUnknownError: NSCocoaError { get }     static var FileManagerUnmountBusyError: NSCocoaError { get }     static var KeyValueValidationError: NSCocoaError { get }     static var FormattingError: NSCocoaError { get }     static var UserCancelledError: NSCocoaError { get }     static var FeatureUnsupportedError: NSCocoaError { get }     static var ExecutableNotLoadableError: NSCocoaError { get }     static var ExecutableArchitectureMismatchError: NSCocoaError { get }     static var ExecutableRuntimeMismatchError: NSCocoaError { get }     static var ExecutableLoadError: NSCocoaError { get }     static var ExecutableLinkError: NSCocoaError { get }     static var PropertyListReadCorruptError: NSCocoaError { get }     static var PropertyListReadUnknownVersionError: NSCocoaError { get }     static var PropertyListReadStreamError: NSCocoaError { get }     static var PropertyListWriteStreamError: NSCocoaError { get }     static var PropertyListWriteInvalidError: NSCocoaError { get }     static var XPCConnectionInterrupted: NSCocoaError { get }     static var XPCConnectionInvalid: NSCocoaError { get }     static var XPCConnectionReplyInvalid: NSCocoaError { get }     static var UbiquitousFileUnavailableError: NSCocoaError { get }     static var UbiquitousFileNotUploadedDueToQuotaError: NSCocoaError { get }     static var UbiquitousFileUbiquityServerNotAvailable: NSCocoaError { get }     static var UserActivityHandoffFailedError: NSCocoaError { get }     static var UserActivityConnectionUnavailableError: NSCocoaError { get }     static var UserActivityRemoteApplicationTimedOutError: NSCocoaError { get }     static var UserActivityHandoffUserInfoTooLargeError: NSCocoaError { get }     static var CoderReadCorruptError: NSCocoaError { get }     static var CoderValueNotFoundError: NSCocoaError { get }     var isCoderError: Bool { get }     var isExecutableError: Bool { get }     var isFileError: Bool { get }     var isFormattingError: Bool { get }     var isPropertyListError: Bool { get }     var isUbiquitousFileError: Bool { get }     var isUserActivityError: Bool { get }     var isValidationError: Bool { get }     var isXPCConnectionError: Bool { get } } ``` | RawRepresentable |

Modified NSCocoaError.CoderReadCorruptError

|  | Declaration |
| --- | --- |
| From | ``` static let CoderReadCorruptError: NSCocoaError ``` |
| To | ``` static var CoderReadCorruptError: NSCocoaError { get } ``` |

Modified NSCocoaError.CoderValueNotFoundError

|  | Declaration |
| --- | --- |
| From | ``` static let CoderValueNotFoundError: NSCocoaError ``` |
| To | ``` static var CoderValueNotFoundError: NSCocoaError { get } ``` |

Modified NSCocoaError.ExecutableArchitectureMismatchError

|  | Declaration |
| --- | --- |
| From | ``` static let ExecutableArchitectureMismatchError: NSCocoaError ``` |
| To | ``` static var ExecutableArchitectureMismatchError: NSCocoaError { get } ``` |

Modified NSCocoaError.ExecutableLinkError

|  | Declaration |
| --- | --- |
| From | ``` static let ExecutableLinkError: NSCocoaError ``` |
| To | ``` static var ExecutableLinkError: NSCocoaError { get } ``` |

Modified NSCocoaError.ExecutableLoadError

|  | Declaration |
| --- | --- |
| From | ``` static let ExecutableLoadError: NSCocoaError ``` |
| To | ``` static var ExecutableLoadError: NSCocoaError { get } ``` |

Modified NSCocoaError.ExecutableNotLoadableError

|  | Declaration |
| --- | --- |
| From | ``` static let ExecutableNotLoadableError: NSCocoaError ``` |
| To | ``` static var ExecutableNotLoadableError: NSCocoaError { get } ``` |

Modified NSCocoaError.ExecutableRuntimeMismatchError

|  | Declaration |
| --- | --- |
| From | ``` static let ExecutableRuntimeMismatchError: NSCocoaError ``` |
| To | ``` static var ExecutableRuntimeMismatchError: NSCocoaError { get } ``` |

Modified NSCocoaError.FeatureUnsupportedError

|  | Declaration |
| --- | --- |
| From | ``` static let FeatureUnsupportedError: NSCocoaError ``` |
| To | ``` static var FeatureUnsupportedError: NSCocoaError { get } ``` |

Modified NSCocoaError.FileLockingError

|  | Declaration |
| --- | --- |
| From | ``` static let FileLockingError: NSCocoaError ``` |
| To | ``` static var FileLockingError: NSCocoaError { get } ``` |

Modified NSCocoaError.FileManagerUnmountBusyError

|  | Declaration |
| --- | --- |
| From | ``` static let FileManagerUnmountBusyError: NSCocoaError ``` |
| To | ``` static var FileManagerUnmountBusyError: NSCocoaError { get } ``` |

Modified NSCocoaError.FileManagerUnmountUnknownError

|  | Declaration |
| --- | --- |
| From | ``` static let FileManagerUnmountUnknownError: NSCocoaError ``` |
| To | ``` static var FileManagerUnmountUnknownError: NSCocoaError { get } ``` |

Modified NSCocoaError.FileNoSuchFileError

|  | Declaration |
| --- | --- |
| From | ``` static let FileNoSuchFileError: NSCocoaError ``` |
| To | ``` static var FileNoSuchFileError: NSCocoaError { get } ``` |

Modified NSCocoaError.FileReadCorruptFileError

|  | Declaration |
| --- | --- |
| From | ``` static let FileReadCorruptFileError: NSCocoaError ``` |
| To | ``` static var FileReadCorruptFileError: NSCocoaError { get } ``` |

Modified NSCocoaError.FileReadInapplicableStringEncodingError

|  | Declaration |
| --- | --- |
| From | ``` static let FileReadInapplicableStringEncodingError: NSCocoaError ``` |
| To | ``` static var FileReadInapplicableStringEncodingError: NSCocoaError { get } ``` |

Modified NSCocoaError.FileReadInvalidFileNameError

|  | Declaration |
| --- | --- |
| From | ``` static let FileReadInvalidFileNameError: NSCocoaError ``` |
| To | ``` static var FileReadInvalidFileNameError: NSCocoaError { get } ``` |

Modified NSCocoaError.FileReadNoPermissionError

|  | Declaration |
| --- | --- |
| From | ``` static let FileReadNoPermissionError: NSCocoaError ``` |
| To | ``` static var FileReadNoPermissionError: NSCocoaError { get } ``` |

Modified NSCocoaError.FileReadNoSuchFileError

|  | Declaration |
| --- | --- |
| From | ``` static let FileReadNoSuchFileError: NSCocoaError ``` |
| To | ``` static var FileReadNoSuchFileError: NSCocoaError { get } ``` |

Modified NSCocoaError.FileReadTooLargeError

|  | Declaration |
| --- | --- |
| From | ``` static let FileReadTooLargeError: NSCocoaError ``` |
| To | ``` static var FileReadTooLargeError: NSCocoaError { get } ``` |

Modified NSCocoaError.FileReadUnknownError

|  | Declaration |
| --- | --- |
| From | ``` static let FileReadUnknownError: NSCocoaError ``` |
| To | ``` static var FileReadUnknownError: NSCocoaError { get } ``` |

Modified NSCocoaError.FileReadUnknownStringEncodingError

|  | Declaration |
| --- | --- |
| From | ``` static let FileReadUnknownStringEncodingError: NSCocoaError ``` |
| To | ``` static var FileReadUnknownStringEncodingError: NSCocoaError { get } ``` |

Modified NSCocoaError.FileReadUnsupportedSchemeError

|  | Declaration |
| --- | --- |
| From | ``` static let FileReadUnsupportedSchemeError: NSCocoaError ``` |
| To | ``` static var FileReadUnsupportedSchemeError: NSCocoaError { get } ``` |

Modified NSCocoaError.FileWriteFileExistsError

|  | Declaration |
| --- | --- |
| From | ``` static let FileWriteFileExistsError: NSCocoaError ``` |
| To | ``` static var FileWriteFileExistsError: NSCocoaError { get } ``` |

Modified NSCocoaError.FileWriteInapplicableStringEncodingError

|  | Declaration |
| --- | --- |
| From | ``` static let FileWriteInapplicableStringEncodingError: NSCocoaError ``` |
| To | ``` static var FileWriteInapplicableStringEncodingError: NSCocoaError { get } ``` |

Modified NSCocoaError.FileWriteInvalidFileNameError

|  | Declaration |
| --- | --- |
| From | ``` static let FileWriteInvalidFileNameError: NSCocoaError ``` |
| To | ``` static var FileWriteInvalidFileNameError: NSCocoaError { get } ``` |

Modified NSCocoaError.FileWriteNoPermissionError

|  | Declaration |
| --- | --- |
| From | ``` static let FileWriteNoPermissionError: NSCocoaError ``` |
| To | ``` static var FileWriteNoPermissionError: NSCocoaError { get } ``` |

Modified NSCocoaError.FileWriteOutOfSpaceError

|  | Declaration |
| --- | --- |
| From | ``` static let FileWriteOutOfSpaceError: NSCocoaError ``` |
| To | ``` static var FileWriteOutOfSpaceError: NSCocoaError { get } ``` |

Modified NSCocoaError.FileWriteUnknownError

|  | Declaration |
| --- | --- |
| From | ``` static let FileWriteUnknownError: NSCocoaError ``` |
| To | ``` static var FileWriteUnknownError: NSCocoaError { get } ``` |

Modified NSCocoaError.FileWriteUnsupportedSchemeError

|  | Declaration |
| --- | --- |
| From | ``` static let FileWriteUnsupportedSchemeError: NSCocoaError ``` |
| To | ``` static var FileWriteUnsupportedSchemeError: NSCocoaError { get } ``` |

Modified NSCocoaError.FileWriteVolumeReadOnlyError

|  | Declaration |
| --- | --- |
| From | ``` static let FileWriteVolumeReadOnlyError: NSCocoaError ``` |
| To | ``` static var FileWriteVolumeReadOnlyError: NSCocoaError { get } ``` |

Modified NSCocoaError.FormattingError

|  | Declaration |
| --- | --- |
| From | ``` static let FormattingError: NSCocoaError ``` |
| To | ``` static var FormattingError: NSCocoaError { get } ``` |

Modified NSCocoaError.KeyValueValidationError

|  | Declaration |
| --- | --- |
| From | ``` static let KeyValueValidationError: NSCocoaError ``` |
| To | ``` static var KeyValueValidationError: NSCocoaError { get } ``` |

Modified NSCocoaError.PropertyListReadCorruptError

|  | Declaration |
| --- | --- |
| From | ``` static let PropertyListReadCorruptError: NSCocoaError ``` |
| To | ``` static var PropertyListReadCorruptError: NSCocoaError { get } ``` |

Modified NSCocoaError.PropertyListReadStreamError

|  | Declaration |
| --- | --- |
| From | ``` static let PropertyListReadStreamError: NSCocoaError ``` |
| To | ``` static var PropertyListReadStreamError: NSCocoaError { get } ``` |

Modified NSCocoaError.PropertyListReadUnknownVersionError

|  | Declaration |
| --- | --- |
| From | ``` static let PropertyListReadUnknownVersionError: NSCocoaError ``` |
| To | ``` static var PropertyListReadUnknownVersionError: NSCocoaError { get } ``` |

Modified NSCocoaError.PropertyListWriteInvalidError

|  | Declaration |
| --- | --- |
| From | ``` static let PropertyListWriteInvalidError: NSCocoaError ``` |
| To | ``` static var PropertyListWriteInvalidError: NSCocoaError { get } ``` |

Modified NSCocoaError.PropertyListWriteStreamError

|  | Declaration |
| --- | --- |
| From | ``` static let PropertyListWriteStreamError: NSCocoaError ``` |
| To | ``` static var PropertyListWriteStreamError: NSCocoaError { get } ``` |

Modified NSCocoaError.UbiquitousFileNotUploadedDueToQuotaError

|  | Declaration |
| --- | --- |
| From | ``` static let UbiquitousFileNotUploadedDueToQuotaError: NSCocoaError ``` |
| To | ``` static var UbiquitousFileNotUploadedDueToQuotaError: NSCocoaError { get } ``` |

Modified NSCocoaError.UbiquitousFileUbiquityServerNotAvailable

|  | Declaration |
| --- | --- |
| From | ``` static let UbiquitousFileUbiquityServerNotAvailable: NSCocoaError ``` |
| To | ``` static var UbiquitousFileUbiquityServerNotAvailable: NSCocoaError { get } ``` |

Modified NSCocoaError.UbiquitousFileUnavailableError

|  | Declaration |
| --- | --- |
| From | ``` static let UbiquitousFileUnavailableError: NSCocoaError ``` |
| To | ``` static var UbiquitousFileUnavailableError: NSCocoaError { get } ``` |

Modified NSCocoaError.UserActivityConnectionUnavailableError

|  | Declaration |
| --- | --- |
| From | ``` static let UserActivityConnectionUnavailableError: NSCocoaError ``` |
| To | ``` static var UserActivityConnectionUnavailableError: NSCocoaError { get } ``` |

Modified NSCocoaError.UserActivityHandoffFailedError

|  | Declaration |
| --- | --- |
| From | ``` static let UserActivityHandoffFailedError: NSCocoaError ``` |
| To | ``` static var UserActivityHandoffFailedError: NSCocoaError { get } ``` |

Modified NSCocoaError.UserActivityHandoffUserInfoTooLargeError

|  | Declaration |
| --- | --- |
| From | ``` static let UserActivityHandoffUserInfoTooLargeError: NSCocoaError ``` |
| To | ``` static var UserActivityHandoffUserInfoTooLargeError: NSCocoaError { get } ``` |

Modified NSCocoaError.UserActivityRemoteApplicationTimedOutError

|  | Declaration |
| --- | --- |
| From | ``` static let UserActivityRemoteApplicationTimedOutError: NSCocoaError ``` |
| To | ``` static var UserActivityRemoteApplicationTimedOutError: NSCocoaError { get } ``` |

Modified NSCocoaError.UserCancelledError

|  | Declaration |
| --- | --- |
| From | ``` static let UserCancelledError: NSCocoaError ``` |
| To | ``` static var UserCancelledError: NSCocoaError { get } ``` |

Modified NSCocoaError.XPCConnectionInterrupted

|  | Declaration |
| --- | --- |
| From | ``` static let XPCConnectionInterrupted: NSCocoaError ``` |
| To | ``` static var XPCConnectionInterrupted: NSCocoaError { get } ``` |

Modified NSCocoaError.XPCConnectionInvalid

|  | Declaration |
| --- | --- |
| From | ``` static let XPCConnectionInvalid: NSCocoaError ``` |
| To | ``` static var XPCConnectionInvalid: NSCocoaError { get } ``` |

Modified NSCocoaError.XPCConnectionReplyInvalid

|  | Declaration |
| --- | --- |
| From | ``` static let XPCConnectionReplyInvalid: NSCocoaError ``` |
| To | ``` static var XPCConnectionReplyInvalid: NSCocoaError { get } ``` |

Modified [NSCoder](https://developer.apple.com/documentation/foundation/nscoder)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSComparisonPredicate](https://developer.apple.com/documentation/foundation/nscomparisonpredicate)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSComparisonPredicateModifier [enum]](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/modifier)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSComparisonResult [enum]](https://developer.apple.com/documentation/foundation/nscomparisonresult)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSCompoundPredicate](https://developer.apple.com/documentation/foundation/nscompoundpredicate)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSCompoundPredicateType [enum]](https://developer.apple.com/documentation/foundation/nscompoundpredicate/logicaltype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSCondition](https://developer.apple.com/documentation/foundation/nscondition)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSLocking |
| To | NSLocking |

Modified [NSConditionLock](https://developer.apple.com/documentation/foundation/nsconditionlock)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSLocking |
| To | NSLocking |

Modified NSConstantString

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSCountedSet](https://developer.apple.com/documentation/foundation/nscountedset)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSData](https://developer.apple.com/documentation/foundation/nsdata)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSData : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     var length: Int { get }     var bytes: UnsafePointer<Void> { get } } extension NSData {     var description: String { get }     func getBytes(_ buffer: UnsafeMutablePointer<Void>, length length: Int)     func getBytes(_ buffer: UnsafeMutablePointer<Void>, range range: NSRange)     func isEqualToData(_ other: NSData) -> Bool     func subdataWithRange(_ range: NSRange) -> NSData     func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool) -> Bool     func writeToURL(_ url: NSURL, atomically atomically: Bool) -> Bool     func writeToFile(_ path: String, options writeOptionsMask: NSDataWritingOptions) throws     func writeToURL(_ url: NSURL, options writeOptionsMask: NSDataWritingOptions) throws     func rangeOfData(_ dataToFind: NSData, options mask: NSDataSearchOptions, range searchRange: NSRange) -> NSRange     func enumerateByteRangesUsingBlock(_ block: (UnsafePointer<Void>, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) } extension NSData {     convenience init()     class func data() -> Self     convenience init(bytes bytes: UnsafePointer<Void>, length length: Int)     class func dataWithBytes(_ bytes: UnsafePointer<Void>, length length: Int) -> Self     convenience init(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length length: Int)     class func dataWithBytesNoCopy(_ bytes: UnsafeMutablePointer<Void>, length length: Int) -> Self     convenience init(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length length: Int, freeWhenDone b: Bool)     class func dataWithBytesNoCopy(_ bytes: UnsafeMutablePointer<Void>, length length: Int, freeWhenDone b: Bool) -> Self     convenience init(contentsOfFile path: String, options readOptionsMask: NSDataReadingOptions) throws     class func dataWithContentsOfFile(_ path: String, options readOptionsMask: NSDataReadingOptions) throws -> Self     convenience init(contentsOfURL url: NSURL, options readOptionsMask: NSDataReadingOptions) throws     class func dataWithContentsOfURL(_ url: NSURL, options readOptionsMask: NSDataReadingOptions) throws -> Self     convenience init?(contentsOfFile path: String)     class func dataWithContentsOfFile(_ path: String) -> Self?     convenience init?(contentsOfURL url: NSURL)     class func dataWithContentsOfURL(_ url: NSURL) -> Self?     init(bytes bytes: UnsafePointer<Void>, length length: Int)     init(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length length: Int)     init(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length length: Int, freeWhenDone b: Bool)     init(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length length: Int, deallocator deallocator: ((UnsafeMutablePointer<Void>, Int) -> Void)?)     init(contentsOfFile path: String, options readOptionsMask: NSDataReadingOptions) throws     init(contentsOfURL url: NSURL, options readOptionsMask: NSDataReadingOptions) throws     init?(contentsOfFile path: String)     init?(contentsOfURL url: NSURL)     init(data data: NSData)     class func dataWithData(_ data: NSData) -> Self } extension NSData {     init?(base64EncodedString base64String: String, options options: NSDataBase64DecodingOptions)     func base64EncodedStringWithOptions(_ options: NSDataBase64EncodingOptions) -> String     init?(base64EncodedData base64Data: NSData, options options: NSDataBase64DecodingOptions)     func base64EncodedDataWithOptions(_ options: NSDataBase64EncodingOptions) -> NSData } extension NSData {     func getBytes(_ buffer: UnsafeMutablePointer<Void>)     class func dataWithContentsOfMappedFile(_ path: String) -> AnyObject?     init?(contentsOfMappedFile path: String)     init?(base64Encoding base64String: String)     func base64Encoding() -> String } ``` | AnyObject, NSCoding, NSCopying, NSMutableCopying, NSSecureCoding |
| To | ``` class NSData : NSObject, NSCopying, NSMutableCopying, NSSecureCoding {     var length: Int { get }     var bytes: UnsafePointer<Void> { get } } extension NSData {     var description: String { get }     func getBytes(_ buffer: UnsafeMutablePointer<Void>, length length: Int)     func getBytes(_ buffer: UnsafeMutablePointer<Void>, range range: NSRange)     func isEqualToData(_ other: NSData) -> Bool     func subdataWithRange(_ range: NSRange) -> NSData     func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool) -> Bool     func writeToURL(_ url: NSURL, atomically atomically: Bool) -> Bool     func writeToFile(_ path: String, options writeOptionsMask: NSDataWritingOptions) throws     func writeToURL(_ url: NSURL, options writeOptionsMask: NSDataWritingOptions) throws     func rangeOfData(_ dataToFind: NSData, options mask: NSDataSearchOptions, range searchRange: NSRange) -> NSRange     func enumerateByteRangesUsingBlock(_ block: (UnsafePointer<Void>, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) } extension NSData {     convenience init()     class func data() -> Self     convenience init(bytes bytes: UnsafePointer<Void>, length length: Int)     class func dataWithBytes(_ bytes: UnsafePointer<Void>, length length: Int) -> Self     convenience init(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length length: Int)     class func dataWithBytesNoCopy(_ bytes: UnsafeMutablePointer<Void>, length length: Int) -> Self     convenience init(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length length: Int, freeWhenDone b: Bool)     class func dataWithBytesNoCopy(_ bytes: UnsafeMutablePointer<Void>, length length: Int, freeWhenDone b: Bool) -> Self     convenience init(contentsOfFile path: String, options readOptionsMask: NSDataReadingOptions) throws     class func dataWithContentsOfFile(_ path: String, options readOptionsMask: NSDataReadingOptions) throws -> Self     convenience init(contentsOfURL url: NSURL, options readOptionsMask: NSDataReadingOptions) throws     class func dataWithContentsOfURL(_ url: NSURL, options readOptionsMask: NSDataReadingOptions) throws -> Self     convenience init?(contentsOfFile path: String)     class func dataWithContentsOfFile(_ path: String) -> Self?     convenience init?(contentsOfURL url: NSURL)     class func dataWithContentsOfURL(_ url: NSURL) -> Self?     init(bytes bytes: UnsafePointer<Void>, length length: Int)     init(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length length: Int)     init(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length length: Int, freeWhenDone b: Bool)     init(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length length: Int, deallocator deallocator: ((UnsafeMutablePointer<Void>, Int) -> Void)?)     init(contentsOfFile path: String, options readOptionsMask: NSDataReadingOptions) throws     init(contentsOfURL url: NSURL, options readOptionsMask: NSDataReadingOptions) throws     init?(contentsOfFile path: String)     init?(contentsOfURL url: NSURL)     init(data data: NSData)     class func dataWithData(_ data: NSData) -> Self } extension NSData {     init?(base64EncodedString base64String: String, options options: NSDataBase64DecodingOptions)     func base64EncodedStringWithOptions(_ options: NSDataBase64EncodingOptions) -> String     init?(base64EncodedData base64Data: NSData, options options: NSDataBase64DecodingOptions)     func base64EncodedDataWithOptions(_ options: NSDataBase64EncodingOptions) -> NSData } extension NSData {     func getBytes(_ buffer: UnsafeMutablePointer<Void>)     class func dataWithContentsOfMappedFile(_ path: String) -> AnyObject?     init?(contentsOfMappedFile path: String)     init?(base64Encoding base64String: String)     func base64Encoding() -> String } ``` | NSCopying, NSMutableCopying, NSSecureCoding |

Modified [NSDataDetector](https://developer.apple.com/documentation/foundation/nsdatadetector)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSDate](https://developer.apple.com/documentation/foundation/nsdate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSDate : NSObject, NSCopying, NSSecureCoding, NSCoding {     var timeIntervalSinceReferenceDate: NSTimeInterval { get }     init()     init(timeIntervalSinceReferenceDate ti: NSTimeInterval)     init?(coder aDecoder: NSCoder) } extension NSDate : _Reflectable { } extension NSDate {     func timeIntervalSinceDate(_ anotherDate: NSDate) -> NSTimeInterval     var timeIntervalSinceNow: NSTimeInterval { get }     var timeIntervalSince1970: NSTimeInterval { get }     func addTimeInterval(_ seconds: NSTimeInterval) -> AnyObject     func dateByAddingTimeInterval(_ ti: NSTimeInterval) -> Self     func earlierDate(_ anotherDate: NSDate) -> NSDate     func laterDate(_ anotherDate: NSDate) -> NSDate     func compare(_ other: NSDate) -> NSComparisonResult     func isEqualToDate(_ otherDate: NSDate) -> Bool     var description: String { get }     func descriptionWithLocale(_ locale: AnyObject?) -> String     class func timeIntervalSinceReferenceDate() -> NSTimeInterval } extension NSDate {     convenience init()     class func date() -> Self     convenience init(timeIntervalSinceNow secs: NSTimeInterval)     class func dateWithTimeIntervalSinceNow(_ secs: NSTimeInterval) -> Self     convenience init(timeIntervalSinceReferenceDate ti: NSTimeInterval)     class func dateWithTimeIntervalSinceReferenceDate(_ ti: NSTimeInterval) -> Self     convenience init(timeIntervalSince1970 secs: NSTimeInterval)     class func dateWithTimeIntervalSince1970(_ secs: NSTimeInterval) -> Self     convenience init(timeInterval secsToBeAdded: NSTimeInterval, sinceDate date: NSDate)     class func dateWithTimeInterval(_ secsToBeAdded: NSTimeInterval, sinceDate date: NSDate) -> Self     class func distantFuture() -> NSDate     class func distantPast() -> NSDate     convenience init(timeIntervalSinceNow secs: NSTimeInterval)     convenience init(timeIntervalSince1970 secs: NSTimeInterval)     convenience init(timeInterval secsToBeAdded: NSTimeInterval, sinceDate date: NSDate) } extension NSDate : _Reflectable { } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NSDate : NSObject, NSCopying, NSSecureCoding {     var timeIntervalSinceReferenceDate: NSTimeInterval { get }     init()     init(timeIntervalSinceReferenceDate ti: NSTimeInterval)     init?(coder aDecoder: NSCoder) } extension NSDate : _Reflectable { } extension NSDate {     func timeIntervalSinceDate(_ anotherDate: NSDate) -> NSTimeInterval     var timeIntervalSinceNow: NSTimeInterval { get }     var timeIntervalSince1970: NSTimeInterval { get }     func addTimeInterval(_ seconds: NSTimeInterval) -> AnyObject     func dateByAddingTimeInterval(_ ti: NSTimeInterval) -> Self     func earlierDate(_ anotherDate: NSDate) -> NSDate     func laterDate(_ anotherDate: NSDate) -> NSDate     func compare(_ other: NSDate) -> NSComparisonResult     func isEqualToDate(_ otherDate: NSDate) -> Bool     var description: String { get }     func descriptionWithLocale(_ locale: AnyObject?) -> String     class func timeIntervalSinceReferenceDate() -> NSTimeInterval } extension NSDate {     convenience init()     class func date() -> Self     convenience init(timeIntervalSinceNow secs: NSTimeInterval)     class func dateWithTimeIntervalSinceNow(_ secs: NSTimeInterval) -> Self     convenience init(timeIntervalSinceReferenceDate ti: NSTimeInterval)     class func dateWithTimeIntervalSinceReferenceDate(_ ti: NSTimeInterval) -> Self     convenience init(timeIntervalSince1970 secs: NSTimeInterval)     class func dateWithTimeIntervalSince1970(_ secs: NSTimeInterval) -> Self     convenience init(timeInterval secsToBeAdded: NSTimeInterval, sinceDate date: NSDate)     class func dateWithTimeInterval(_ secsToBeAdded: NSTimeInterval, sinceDate date: NSDate) -> Self     class func distantFuture() -> NSDate     class func distantPast() -> NSDate     convenience init(timeIntervalSinceNow secs: NSTimeInterval)     convenience init(timeIntervalSince1970 secs: NSTimeInterval)     convenience init(timeInterval secsToBeAdded: NSTimeInterval, sinceDate date: NSDate) } extension NSDate : _Reflectable { } ``` | NSCopying, NSSecureCoding |

Modified [NSDateComponents](https://developer.apple.com/documentation/foundation/nsdatecomponents)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSDateComponents : NSObject, NSCopying, NSSecureCoding, NSCoding {     @NSCopying var calendar: NSCalendar?     @NSCopying var timeZone: NSTimeZone?     var era: Int     var year: Int     var month: Int     var day: Int     var hour: Int     var minute: Int     var second: Int     var nanosecond: Int     var weekday: Int     var weekdayOrdinal: Int     var quarter: Int     var weekOfMonth: Int     var weekOfYear: Int     var yearForWeekOfYear: Int     var leapMonth: Bool     @NSCopying var date: NSDate? { get }     func week() -> Int     func setWeek(_ v: Int)     func setValue(_ value: Int, forComponent unit: NSCalendarUnit)     func valueForComponent(_ unit: NSCalendarUnit) -> Int     var validDate: Bool { get }     func isValidDateInCalendar(_ calendar: NSCalendar) -> Bool } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NSDateComponents : NSObject, NSCopying, NSSecureCoding {     @NSCopying var calendar: NSCalendar?     @NSCopying var timeZone: NSTimeZone?     var era: Int     var year: Int     var month: Int     var day: Int     var hour: Int     var minute: Int     var second: Int     var nanosecond: Int     var weekday: Int     var weekdayOrdinal: Int     var quarter: Int     var weekOfMonth: Int     var weekOfYear: Int     var yearForWeekOfYear: Int     var leapMonth: Bool     @NSCopying var date: NSDate? { get }     func week() -> Int     func setWeek(_ v: Int)     func setValue(_ value: Int, forComponent unit: NSCalendarUnit)     func valueForComponent(_ unit: NSCalendarUnit) -> Int     var validDate: Bool { get }     func isValidDateInCalendar(_ calendar: NSCalendar) -> Bool } ``` | NSCopying, NSSecureCoding |

Modified [NSDateComponentsFormatter](https://developer.apple.com/documentation/foundation/datecomponentsformatter)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSDateComponentsFormatterUnitsStyle [enum]](https://developer.apple.com/documentation/foundation/datecomponentsformatter/unitsstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSDateFormatter](https://developer.apple.com/documentation/foundation/dateformatter)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSDateFormatterBehavior [enum]](https://developer.apple.com/documentation/foundation/nsdateformatterbehavior)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSDateFormatterStyle [enum]](https://developer.apple.com/documentation/foundation/nsdateformatterstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSDateIntervalFormatter](https://developer.apple.com/documentation/foundation/dateintervalformatter)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSDateIntervalFormatterStyle [enum]](https://developer.apple.com/documentation/foundation/nsdateintervalformatterstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSDecimal [struct]](https://developer.apple.com/documentation/foundation/decimal)

|  | Declaration |
| --- | --- |
| From | ``` struct NSDecimal {     var _mantissa: (UInt16, UInt16, UInt16, UInt16, UInt16, UInt16, UInt16, UInt16)     init() } ``` |
| To | ``` struct NSDecimal {     var _exponent: Int32     var _length: UInt32     var _isNegative: UInt32     var _isCompact: UInt32     var _reserved: UInt32     var _mantissa: (UInt16, UInt16, UInt16, UInt16, UInt16, UInt16, UInt16, UInt16)     init()     init(_exponent _exponent: Int32, _length _length: UInt32, _isNegative _isNegative: UInt32, _isCompact _isCompact: UInt32, _reserved _reserved: UInt32, _mantissa _mantissa: (UInt16, UInt16, UInt16, UInt16, UInt16, UInt16, UInt16, UInt16)) } ``` |

Modified [NSDecimalNumber](https://developer.apple.com/documentation/foundation/nsdecimalnumber)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSDecimalNumberHandler](https://developer.apple.com/documentation/foundation/nsdecimalnumberhandler)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSDecimalNumberBehaviors |
| To | NSCoding, NSDecimalNumberBehaviors |

Modified [NSDictionary](https://developer.apple.com/documentation/foundation/nsdictionary)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSDictionary : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding, NSFastEnumeration {     var count: Int { get }     func objectForKey(_ aKey: AnyObject) -> AnyObject?     func keyEnumerator() -> NSEnumerator     init()     init(objects objects: UnsafePointer<AnyObject?>, forKeys keys: UnsafePointer<NSCopying?>, count cnt: Int)     init?(coder aDecoder: NSCoder) } extension NSDictionary : SequenceType {     final class Generator : GeneratorType {         func next() -> (key: AnyObject, value: AnyObject)?     }     func generate() -> NSDictionary.Generator } extension NSDictionary : DictionaryLiteralConvertible {     required convenience init(dictionaryLiteral elements: (NSCopying, AnyObject)...) } extension NSDictionary {     @objc(_swiftInitWithDictionary_NSDictionary:) convenience init(dictionary otherDictionary: NSDictionary) } extension NSDictionary : _Reflectable { } extension NSDictionary {     var allKeys: [AnyObject] { get }     func allKeysForObject(_ anObject: AnyObject) -> [AnyObject]     var allValues: [AnyObject] { get }     var description: String { get }     var descriptionInStringsFileFormat: String { get }     func descriptionWithLocale(_ locale: AnyObject?) -> String     func descriptionWithLocale(_ locale: AnyObject?, indent level: Int) -> String     func isEqualToDictionary(_ otherDictionary: [NSObject : AnyObject]) -> Bool     func objectEnumerator() -> NSEnumerator     func objectsForKeys(_ keys: [AnyObject], notFoundMarker marker: AnyObject) -> [AnyObject]     func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool) -> Bool     func writeToURL(_ url: NSURL, atomically atomically: Bool) -> Bool     func keysSortedByValueUsingSelector(_ comparator: Selector) -> [AnyObject]     func getObjects(_ objects: AutoreleasingUnsafeMutablePointer<AnyObject?>, andKeys keys: AutoreleasingUnsafeMutablePointer<AnyObject?>, count count: Int)     subscript (_ key: NSCopying) -> AnyObject? { get }     func objectForKeyedSubscript(_ key: NSCopying) -> AnyObject?     func enumerateKeysAndObjectsUsingBlock(_ block: (AnyObject, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateKeysAndObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void)     func keysSortedByValueUsingComparator(_ cmptr: NSComparator) -> [AnyObject]     func keysSortedByValueWithOptions(_ opts: NSSortOptions, usingComparator cmptr: NSComparator) -> [AnyObject]     func keysOfEntriesPassingTest(_ predicate: (AnyObject, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject>     func keysOfEntriesWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject> } extension NSDictionary {     func getObjects(_ objects: AutoreleasingUnsafeMutablePointer<AnyObject?>, andKeys keys: AutoreleasingUnsafeMutablePointer<AnyObject?>) } extension NSDictionary {     convenience init()     class func dictionary() -> Self     convenience init(object object: AnyObject, forKey key: NSCopying)     class func dictionaryWithObject(_ object: AnyObject, forKey key: NSCopying) -> Self     convenience init(objects objects: UnsafePointer<AnyObject?>, forKeys keys: UnsafePointer<NSCopying?>, count cnt: Int)     class func dictionaryWithObjects(_ objects: UnsafePointer<AnyObject?>, forKeys keys: UnsafePointer<NSCopying?>, count cnt: Int) -> Self     convenience init(dictionary dict: [NSObject : AnyObject])     class func dictionaryWithDictionary(_ dict: [NSObject : AnyObject]) -> Self     convenience init(objects objects: [AnyObject], forKeys keys: [NSCopying])     class func dictionaryWithObjects(_ objects: [AnyObject], forKeys keys: [NSCopying]) -> Self     convenience init(dictionary otherDictionary: [NSObject : AnyObject])     convenience init(dictionary otherDictionary: [NSObject : AnyObject], copyItems flag: Bool)     convenience init(objects objects: [AnyObject], forKeys keys: [NSCopying])      init?(contentsOfFile path: String)     class func dictionaryWithContentsOfFile(_ path: String) -> [NSObject : AnyObject]?      init?(contentsOfURL url: NSURL)     class func dictionaryWithContentsOfURL(_ url: NSURL) -> [NSObject : AnyObject]?     convenience init?(contentsOfFile path: String)     convenience init?(contentsOfURL url: NSURL) } extension NSDictionary {     class func sharedKeySetForKeys(_ keys: [NSCopying]) -> AnyObject } extension NSDictionary {     func fileSize() -> UInt64     func fileModificationDate() -> NSDate?     func fileType() -> String?     func filePosixPermissions() -> Int     func fileOwnerAccountName() -> String?     func fileGroupOwnerAccountName() -> String?     func fileSystemNumber() -> Int     func fileSystemFileNumber() -> Int     func fileExtensionHidden() -> Bool     func fileHFSCreatorCode() -> OSType     func fileHFSTypeCode() -> OSType     func fileIsImmutable() -> Bool     func fileIsAppendOnly() -> Bool     func fileCreationDate() -> NSDate?     func fileOwnerAccountID() -> NSNumber?     func fileGroupOwnerAccountID() -> NSNumber? } extension NSDictionary {     func valueForKey(_ key: String) -> AnyObject? } extension NSDictionary : _Reflectable { } extension NSDictionary {     @objc(_swiftInitWithDictionary_NSDictionary:) convenience init(dictionary otherDictionary: NSDictionary) } extension NSDictionary : SequenceType {     final class Generator : GeneratorType {         func next() -> (key: AnyObject, value: AnyObject)?     }     func generate() -> NSDictionary.Generator } extension NSDictionary : DictionaryLiteralConvertible {     required convenience init(dictionaryLiteral elements: (NSCopying, AnyObject)...) } ``` | AnyObject, DictionaryLiteralConvertible, NSCoding, NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding, SequenceType |
| To | ``` class NSDictionary : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSFastEnumeration {     var count: Int { get }     func objectForKey(_ aKey: AnyObject) -> AnyObject?     func keyEnumerator() -> NSEnumerator     init()     init(objects objects: UnsafePointer<AnyObject?>, forKeys keys: UnsafePointer<NSCopying?>, count cnt: Int)     init?(coder aDecoder: NSCoder) } extension NSDictionary : DictionaryLiteralConvertible {     required convenience init(dictionaryLiteral elements: (NSCopying, AnyObject)...) } extension NSDictionary : SequenceType {     final class Generator : GeneratorType {         func next() -> (key: AnyObject, value: AnyObject)?     }     func generate() -> NSDictionary.Generator } extension NSDictionary {     @objc(_swiftInitWithDictionary_NSDictionary:) convenience init(dictionary otherDictionary: NSDictionary) } extension NSDictionary : _Reflectable { } extension NSDictionary {     var allKeys: [AnyObject] { get }     func allKeysForObject(_ anObject: AnyObject) -> [AnyObject]     var allValues: [AnyObject] { get }     var description: String { get }     var descriptionInStringsFileFormat: String { get }     func descriptionWithLocale(_ locale: AnyObject?) -> String     func descriptionWithLocale(_ locale: AnyObject?, indent level: Int) -> String     func isEqualToDictionary(_ otherDictionary: [NSObject : AnyObject]) -> Bool     func objectEnumerator() -> NSEnumerator     func objectsForKeys(_ keys: [AnyObject], notFoundMarker marker: AnyObject) -> [AnyObject]     func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool) -> Bool     func writeToURL(_ url: NSURL, atomically atomically: Bool) -> Bool     func keysSortedByValueUsingSelector(_ comparator: Selector) -> [AnyObject]     func getObjects(_ objects: AutoreleasingUnsafeMutablePointer<AnyObject?>, andKeys keys: AutoreleasingUnsafeMutablePointer<AnyObject?>, count count: Int)     subscript (_ key: NSCopying) -> AnyObject? { get }     func objectForKeyedSubscript(_ key: NSCopying) -> AnyObject?     func enumerateKeysAndObjectsUsingBlock(_ block: (AnyObject, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateKeysAndObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void)     func keysSortedByValueUsingComparator(_ cmptr: NSComparator) -> [AnyObject]     func keysSortedByValueWithOptions(_ opts: NSSortOptions, usingComparator cmptr: NSComparator) -> [AnyObject]     func keysOfEntriesPassingTest(_ predicate: (AnyObject, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject>     func keysOfEntriesWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject> } extension NSDictionary {     func getObjects(_ objects: AutoreleasingUnsafeMutablePointer<AnyObject?>, andKeys keys: AutoreleasingUnsafeMutablePointer<AnyObject?>) } extension NSDictionary {     convenience init()     class func dictionary() -> Self     convenience init(object object: AnyObject, forKey key: NSCopying)     class func dictionaryWithObject(_ object: AnyObject, forKey key: NSCopying) -> Self     convenience init(objects objects: UnsafePointer<AnyObject?>, forKeys keys: UnsafePointer<NSCopying?>, count cnt: Int)     class func dictionaryWithObjects(_ objects: UnsafePointer<AnyObject?>, forKeys keys: UnsafePointer<NSCopying?>, count cnt: Int) -> Self     convenience init(dictionary dict: [NSObject : AnyObject])     class func dictionaryWithDictionary(_ dict: [NSObject : AnyObject]) -> Self     convenience init(objects objects: [AnyObject], forKeys keys: [NSCopying])     class func dictionaryWithObjects(_ objects: [AnyObject], forKeys keys: [NSCopying]) -> Self     convenience init(dictionary otherDictionary: [NSObject : AnyObject])     convenience init(dictionary otherDictionary: [NSObject : AnyObject], copyItems flag: Bool)     convenience init(objects objects: [AnyObject], forKeys keys: [NSCopying])      init?(contentsOfFile path: String)     class func dictionaryWithContentsOfFile(_ path: String) -> [NSObject : AnyObject]?      init?(contentsOfURL url: NSURL)     class func dictionaryWithContentsOfURL(_ url: NSURL) -> [NSObject : AnyObject]?     convenience init?(contentsOfFile path: String)     convenience init?(contentsOfURL url: NSURL) } extension NSDictionary {     class func sharedKeySetForKeys(_ keys: [NSCopying]) -> AnyObject } extension NSDictionary {     func fileSize() -> UInt64     func fileModificationDate() -> NSDate?     func fileType() -> String?     func filePosixPermissions() -> Int     func fileOwnerAccountName() -> String?     func fileGroupOwnerAccountName() -> String?     func fileSystemNumber() -> Int     func fileSystemFileNumber() -> Int     func fileExtensionHidden() -> Bool     func fileHFSCreatorCode() -> OSType     func fileHFSTypeCode() -> OSType     func fileIsImmutable() -> Bool     func fileIsAppendOnly() -> Bool     func fileCreationDate() -> NSDate?     func fileOwnerAccountID() -> NSNumber?     func fileGroupOwnerAccountID() -> NSNumber? } extension NSDictionary {     func valueForKey(_ key: String) -> AnyObject? } extension NSDictionary : _Reflectable { } extension NSDictionary {     @objc(_swiftInitWithDictionary_NSDictionary:) convenience init(dictionary otherDictionary: NSDictionary) } extension NSDictionary : SequenceType {     final class Generator : GeneratorType {         func next() -> (key: AnyObject, value: AnyObject)?     }     func generate() -> NSDictionary.Generator } extension NSDictionary : DictionaryLiteralConvertible {     required convenience init(dictionaryLiteral elements: (NSCopying, AnyObject)...) } ``` | DictionaryLiteralConvertible, NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding, SequenceType |

Modified NSDictionary.Generator

|  | Protocols |
| --- | --- |
| From | AnyObject, GeneratorType |
| To | GeneratorType |

Modified [NSDirectoryEnumerator](https://developer.apple.com/documentation/foundation/nsdirectoryenumerator)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSEnergyFormatter](https://developer.apple.com/documentation/foundation/energyformatter)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSEnergyFormatterUnit [enum]](https://developer.apple.com/documentation/foundation/nsenergyformatterunit)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSEnumerator](https://developer.apple.com/documentation/foundation/nsenumerator)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSFastEnumeration, SequenceType |
| To | NSFastEnumeration, SequenceType |

Modified [NSError](https://developer.apple.com/documentation/foundation/nserror)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSError : NSObject, NSCopying, NSSecureCoding, NSCoding {     init(domain domain: String, code code: Int, userInfo dict: [NSObject : AnyObject]?)     class func errorWithDomain(_ domain: String, code code: Int, userInfo dict: [NSObject : AnyObject]?) -> Self     var domain: String { get }     var code: Int { get }     var userInfo: [NSObject : AnyObject] { get }     var localizedDescription: String { get }     var localizedFailureReason: String? { get }     var localizedRecoverySuggestion: String? { get }     var localizedRecoveryOptions: [String]? { get }     var recoveryAttempter: AnyObject? { get }     var helpAnchor: String? { get }     class func setUserInfoValueProviderForDomain(_ errorDomain: String, provider provider: ((NSError, String) -> AnyObject?)?)     class func userInfoValueProviderForDomain(_ errorDomain: String) -> ((NSError, String) -> AnyObject?)? } extension NSError : ErrorType { } extension NSError : ErrorType { } ``` | AnyObject, ErrorType, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NSError : NSObject, NSCopying, NSSecureCoding {     init(domain domain: String, code code: Int, userInfo dict: [NSObject : AnyObject]?)     class func errorWithDomain(_ domain: String, code code: Int, userInfo dict: [NSObject : AnyObject]?) -> Self     var domain: String { get }     var code: Int { get }     var userInfo: [NSObject : AnyObject] { get }     var localizedDescription: String { get }     var localizedFailureReason: String? { get }     var localizedRecoverySuggestion: String? { get }     var localizedRecoveryOptions: [String]? { get }     var recoveryAttempter: AnyObject? { get }     var helpAnchor: String? { get }     class func setUserInfoValueProviderForDomain(_ errorDomain: String, provider provider: ((NSError, String) -> AnyObject?)?)     class func userInfoValueProviderForDomain(_ errorDomain: String) -> ((NSError, String) -> AnyObject?)? } extension NSError : ErrorType { } extension NSError : ErrorType { } ``` | ErrorType, NSCopying, NSSecureCoding |

Modified [NSException](https://developer.apple.com/documentation/foundation/nsexception)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [NSExpression](https://developer.apple.com/documentation/foundation/nsexpression)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSExpression : NSObject, NSSecureCoding, NSCoding, NSCopying {      init(format expressionFormat: String, argumentArray arguments: [AnyObject])     class func expressionWithFormat(_ expressionFormat: String, argumentArray arguments: [AnyObject]) -> NSExpression      init(format expressionFormat: String, arguments argList: CVaListPointer)     class func expressionWithFormat(_ expressionFormat: String, arguments argList: CVaListPointer) -> NSExpression      init(forConstantValue obj: AnyObject?)     class func expressionForConstantValue(_ obj: AnyObject?) -> NSExpression     class func expressionForEvaluatedObject() -> NSExpression      init(forVariable string: String)     class func expressionForVariable(_ string: String) -> NSExpression      init(forKeyPath keyPath: String)     class func expressionForKeyPath(_ keyPath: String) -> NSExpression      init(forFunction name: String, arguments parameters: [AnyObject])     class func expressionForFunction(_ name: String, arguments parameters: [AnyObject]) -> NSExpression      init(forAggregate subexpressions: [AnyObject])     class func expressionForAggregate(_ subexpressions: [AnyObject]) -> NSExpression      init(forUnionSet left: NSExpression, with right: NSExpression)     class func expressionForUnionSet(_ left: NSExpression, with right: NSExpression) -> NSExpression      init(forIntersectSet left: NSExpression, with right: NSExpression)     class func expressionForIntersectSet(_ left: NSExpression, with right: NSExpression) -> NSExpression      init(forMinusSet left: NSExpression, with right: NSExpression)     class func expressionForMinusSet(_ left: NSExpression, with right: NSExpression) -> NSExpression      init(forSubquery expression: NSExpression, usingIteratorVariable variable: String, predicate predicate: AnyObject)     class func expressionForSubquery(_ expression: NSExpression, usingIteratorVariable variable: String, predicate predicate: AnyObject) -> NSExpression      init(forFunction target: NSExpression, selectorName name: String, arguments parameters: [AnyObject]?)     class func expressionForFunction(_ target: NSExpression, selectorName name: String, arguments parameters: [AnyObject]?) -> NSExpression     class func expressionForAnyKey() -> NSExpression      init(forBlock block: (AnyObject?, [AnyObject], NSMutableDictionary?) -> AnyObject, arguments arguments: [NSExpression]?)     class func expressionForBlock(_ block: (AnyObject?, [AnyObject], NSMutableDictionary?) -> AnyObject, arguments arguments: [NSExpression]?) -> NSExpression      init(forConditional predicate: NSPredicate, trueExpression trueExpression: NSExpression, falseExpression falseExpression: NSExpression)     class func expressionForConditional(_ predicate: NSPredicate, trueExpression trueExpression: NSExpression, falseExpression falseExpression: NSExpression) -> NSExpression     init(expressionType type: NSExpressionType)     init?(coder coder: NSCoder)     var expressionType: NSExpressionType { get }     var constantValue: AnyObject { get }     var keyPath: String { get }     var function: String { get }     var variable: String { get }     @NSCopying var operand: NSExpression { get }     var arguments: [NSExpression]? { get }     var collection: AnyObject { get }     @NSCopying var predicate: NSPredicate { get }     @NSCopying var leftExpression: NSExpression { get }     @NSCopying var rightExpression: NSExpression { get }     @NSCopying var trueExpression: NSExpression { get }     @NSCopying var falseExpression: NSExpression { get }     var expressionBlock: (AnyObject?, [AnyObject], NSMutableDictionary?) -> AnyObject { get }     func expressionValueWithObject(_ object: AnyObject?, context context: NSMutableDictionary?) -> AnyObject     func allowEvaluation() } extension NSExpression {     convenience init(format expressionFormat: String, _ args: CVarArgType...) } extension NSExpression {     convenience init(format expressionFormat: String, _ args: CVarArgType...) } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NSExpression : NSObject, NSSecureCoding, NSCopying {      init(format expressionFormat: String, argumentArray arguments: [AnyObject])     class func expressionWithFormat(_ expressionFormat: String, argumentArray arguments: [AnyObject]) -> NSExpression      init(format expressionFormat: String, arguments argList: CVaListPointer)     class func expressionWithFormat(_ expressionFormat: String, arguments argList: CVaListPointer) -> NSExpression      init(forConstantValue obj: AnyObject?)     class func expressionForConstantValue(_ obj: AnyObject?) -> NSExpression     class func expressionForEvaluatedObject() -> NSExpression      init(forVariable string: String)     class func expressionForVariable(_ string: String) -> NSExpression      init(forKeyPath keyPath: String)     class func expressionForKeyPath(_ keyPath: String) -> NSExpression      init(forFunction name: String, arguments parameters: [AnyObject])     class func expressionForFunction(_ name: String, arguments parameters: [AnyObject]) -> NSExpression      init(forAggregate subexpressions: [AnyObject])     class func expressionForAggregate(_ subexpressions: [AnyObject]) -> NSExpression      init(forUnionSet left: NSExpression, with right: NSExpression)     class func expressionForUnionSet(_ left: NSExpression, with right: NSExpression) -> NSExpression      init(forIntersectSet left: NSExpression, with right: NSExpression)     class func expressionForIntersectSet(_ left: NSExpression, with right: NSExpression) -> NSExpression      init(forMinusSet left: NSExpression, with right: NSExpression)     class func expressionForMinusSet(_ left: NSExpression, with right: NSExpression) -> NSExpression      init(forSubquery expression: NSExpression, usingIteratorVariable variable: String, predicate predicate: AnyObject)     class func expressionForSubquery(_ expression: NSExpression, usingIteratorVariable variable: String, predicate predicate: AnyObject) -> NSExpression      init(forFunction target: NSExpression, selectorName name: String, arguments parameters: [AnyObject]?)     class func expressionForFunction(_ target: NSExpression, selectorName name: String, arguments parameters: [AnyObject]?) -> NSExpression     class func expressionForAnyKey() -> NSExpression      init(forBlock block: (AnyObject?, [AnyObject], NSMutableDictionary?) -> AnyObject, arguments arguments: [NSExpression]?)     class func expressionForBlock(_ block: (AnyObject?, [AnyObject], NSMutableDictionary?) -> AnyObject, arguments arguments: [NSExpression]?) -> NSExpression      init(forConditional predicate: NSPredicate, trueExpression trueExpression: NSExpression, falseExpression falseExpression: NSExpression)     class func expressionForConditional(_ predicate: NSPredicate, trueExpression trueExpression: NSExpression, falseExpression falseExpression: NSExpression) -> NSExpression     init(expressionType type: NSExpressionType)     init?(coder coder: NSCoder)     var expressionType: NSExpressionType { get }     var constantValue: AnyObject { get }     var keyPath: String { get }     var function: String { get }     var variable: String { get }     @NSCopying var operand: NSExpression { get }     var arguments: [NSExpression]? { get }     var collection: AnyObject { get }     @NSCopying var predicate: NSPredicate { get }     @NSCopying var leftExpression: NSExpression { get }     @NSCopying var rightExpression: NSExpression { get }     @NSCopying var trueExpression: NSExpression { get }     @NSCopying var falseExpression: NSExpression { get }     var expressionBlock: (AnyObject?, [AnyObject], NSMutableDictionary?) -> AnyObject { get }     func expressionValueWithObject(_ object: AnyObject?, context context: NSMutableDictionary?) -> AnyObject     func allowEvaluation() } extension NSExpression {     convenience init(format expressionFormat: String, _ args: CVarArgType...) } extension NSExpression {     convenience init(format expressionFormat: String, _ args: CVarArgType...) } ``` | NSCopying, NSSecureCoding |

Modified [NSExpressionType [enum]](https://developer.apple.com/documentation/foundation/nsexpressiontype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSExtensionContext](https://developer.apple.com/documentation/foundation/nsextensioncontext)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSExtensionItem](https://developer.apple.com/documentation/foundation/nsextensionitem)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSExtensionItem : NSObject, NSCopying, NSSecureCoding, NSCoding {     @NSCopying var attributedTitle: NSAttributedString?     @NSCopying var attributedContentText: NSAttributedString?     var attachments: [AnyObject]?     var userInfo: [NSObject : AnyObject]? } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NSExtensionItem : NSObject, NSCopying, NSSecureCoding {     @NSCopying var attributedTitle: NSAttributedString?     @NSCopying var attributedContentText: NSAttributedString?     var attachments: [AnyObject]?     var userInfo: [NSObject : AnyObject]? } ``` | NSCopying, NSSecureCoding |

Modified NSFastGenerator

|  | Protocols |
| --- | --- |
| From | AnyObject, GeneratorType |
| To | GeneratorType |

Modified [NSFileAccessIntent](https://developer.apple.com/documentation/foundation/nsfileaccessintent)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSFileCoordinator](https://developer.apple.com/documentation/foundation/nsfilecoordinator)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSFileHandle](https://developer.apple.com/documentation/foundation/filehandle)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSFileHandle : NSObject, NSSecureCoding, NSCoding {     @NSCopying var availableData: NSData { get }     func readDataToEndOfFile() -> NSData     func readDataOfLength(_ length: Int) -> NSData     func writeData(_ data: NSData)     var offsetInFile: UInt64 { get }     func seekToEndOfFile() -> UInt64     func seekToFileOffset(_ offset: UInt64)     func truncateFileAtOffset(_ offset: UInt64)     func synchronizeFile()     func closeFile()     init(fileDescriptor fd: Int32, closeOnDealloc closeopt: Bool)     init?(coder coder: NSCoder) } extension NSFileHandle {     class func fileHandleWithStandardInput() -> NSFileHandle     class func fileHandleWithStandardOutput() -> NSFileHandle     class func fileHandleWithStandardError() -> NSFileHandle     class func fileHandleWithNullDevice() -> NSFileHandle     convenience init?(forReadingAtPath path: String)     class func fileHandleForReadingAtPath(_ path: String) -> Self?     convenience init?(forWritingAtPath path: String)     class func fileHandleForWritingAtPath(_ path: String) -> Self?     convenience init?(forUpdatingAtPath path: String)     class func fileHandleForUpdatingAtPath(_ path: String) -> Self?     convenience init(forReadingFromURL url: NSURL) throws     class func fileHandleForReadingFromURL(_ url: NSURL) throws -> Self     convenience init(forWritingToURL url: NSURL) throws     class func fileHandleForWritingToURL(_ url: NSURL) throws -> Self     convenience init(forUpdatingURL url: NSURL) throws     class func fileHandleForUpdatingURL(_ url: NSURL) throws -> Self } extension NSFileHandle {     func readInBackgroundAndNotifyForModes(_ modes: [String]?)     func readInBackgroundAndNotify()     func readToEndOfFileInBackgroundAndNotifyForModes(_ modes: [String]?)     func readToEndOfFileInBackgroundAndNotify()     func acceptConnectionInBackgroundAndNotifyForModes(_ modes: [String]?)     func acceptConnectionInBackgroundAndNotify()     func waitForDataInBackgroundAndNotifyForModes(_ modes: [String]?)     func waitForDataInBackgroundAndNotify()     var readabilityHandler: ((NSFileHandle) -> Void)?     var writeabilityHandler: ((NSFileHandle) -> Void)? } extension NSFileHandle {     convenience init(fileDescriptor fd: Int32)     var fileDescriptor: Int32 { get } } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class NSFileHandle : NSObject, NSSecureCoding {     @NSCopying var availableData: NSData { get }     func readDataToEndOfFile() -> NSData     func readDataOfLength(_ length: Int) -> NSData     func writeData(_ data: NSData)     var offsetInFile: UInt64 { get }     func seekToEndOfFile() -> UInt64     func seekToFileOffset(_ offset: UInt64)     func truncateFileAtOffset(_ offset: UInt64)     func synchronizeFile()     func closeFile()     init(fileDescriptor fd: Int32, closeOnDealloc closeopt: Bool)     init?(coder coder: NSCoder) } extension NSFileHandle {     class func fileHandleWithStandardInput() -> NSFileHandle     class func fileHandleWithStandardOutput() -> NSFileHandle     class func fileHandleWithStandardError() -> NSFileHandle     class func fileHandleWithNullDevice() -> NSFileHandle     convenience init?(forReadingAtPath path: String)     class func fileHandleForReadingAtPath(_ path: String) -> Self?     convenience init?(forWritingAtPath path: String)     class func fileHandleForWritingAtPath(_ path: String) -> Self?     convenience init?(forUpdatingAtPath path: String)     class func fileHandleForUpdatingAtPath(_ path: String) -> Self?     convenience init(forReadingFromURL url: NSURL) throws     class func fileHandleForReadingFromURL(_ url: NSURL) throws -> Self     convenience init(forWritingToURL url: NSURL) throws     class func fileHandleForWritingToURL(_ url: NSURL) throws -> Self     convenience init(forUpdatingURL url: NSURL) throws     class func fileHandleForUpdatingURL(_ url: NSURL) throws -> Self } extension NSFileHandle {     func readInBackgroundAndNotifyForModes(_ modes: [String]?)     func readInBackgroundAndNotify()     func readToEndOfFileInBackgroundAndNotifyForModes(_ modes: [String]?)     func readToEndOfFileInBackgroundAndNotify()     func acceptConnectionInBackgroundAndNotifyForModes(_ modes: [String]?)     func acceptConnectionInBackgroundAndNotify()     func waitForDataInBackgroundAndNotifyForModes(_ modes: [String]?)     func waitForDataInBackgroundAndNotify()     var readabilityHandler: ((NSFileHandle) -> Void)?     var writeabilityHandler: ((NSFileHandle) -> Void)? } extension NSFileHandle {     convenience init(fileDescriptor fd: Int32)     var fileDescriptor: Int32 { get } } ``` | NSSecureCoding |

Modified [NSFileManager](https://developer.apple.com/documentation/foundation/filemanager)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSFileSecurity](https://developer.apple.com/documentation/foundation/nsfilesecurity)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [NSFileVersion](https://developer.apple.com/documentation/foundation/nsfileversion)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSFileWrapper](https://developer.apple.com/documentation/foundation/filewrapper)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding |
| To | NSCoding |

Modified [NSFormatter](https://developer.apple.com/documentation/foundation/formatter)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [NSFormattingContext [enum]](https://developer.apple.com/documentation/foundation/nsformattingcontext)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSFormattingUnitStyle [enum]](https://developer.apple.com/documentation/foundation/nsformattingunitstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSHashTable](https://developer.apple.com/documentation/foundation/nshashtable)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying, NSFastEnumeration |
| To | NSCoding, NSCopying, NSFastEnumeration |

Modified [NSHTTPCookie](https://developer.apple.com/documentation/foundation/httpcookie)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSHTTPCookieAcceptPolicy [enum]](https://developer.apple.com/documentation/foundation/httpcookie/acceptpolicy)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSHTTPCookieStorage](https://developer.apple.com/documentation/foundation/nshttpcookiestorage)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSHTTPURLResponse](https://developer.apple.com/documentation/foundation/httpurlresponse)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSIndexPath](https://developer.apple.com/documentation/foundation/nsindexpath)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSIndexPath : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init(index index: Int)     class func indexPathWithIndex(_ index: Int) -> Self     convenience init(indexes indexes: UnsafePointer<Int>, length length: Int)     class func indexPathWithIndexes(_ indexes: UnsafePointer<Int>, length length: Int) -> Self     init(indexes indexes: UnsafePointer<Int>, length length: Int)     convenience init(index index: Int)     func indexPathByAddingIndex(_ index: Int) -> NSIndexPath     func indexPathByRemovingLastIndex() -> NSIndexPath     func indexAtPosition(_ position: Int) -> Int     var length: Int { get }     func getIndexes(_ indexes: UnsafeMutablePointer<Int>, range positionRange: NSRange)     func compare(_ otherObject: NSIndexPath) -> NSComparisonResult } extension NSIndexPath {     func getIndexes(_ indexes: UnsafeMutablePointer<Int>) } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NSIndexPath : NSObject, NSCopying, NSSecureCoding {     convenience init(index index: Int)     class func indexPathWithIndex(_ index: Int) -> Self     convenience init(indexes indexes: UnsafePointer<Int>, length length: Int)     class func indexPathWithIndexes(_ indexes: UnsafePointer<Int>, length length: Int) -> Self     init(indexes indexes: UnsafePointer<Int>, length length: Int)     convenience init(index index: Int)     func indexPathByAddingIndex(_ index: Int) -> NSIndexPath     func indexPathByRemovingLastIndex() -> NSIndexPath     func indexAtPosition(_ position: Int) -> Int     var length: Int { get }     func getIndexes(_ indexes: UnsafeMutablePointer<Int>, range positionRange: NSRange)     func compare(_ otherObject: NSIndexPath) -> NSComparisonResult } extension NSIndexPath {     func getIndexes(_ indexes: UnsafeMutablePointer<Int>) } ``` | NSCopying, NSSecureCoding |

Modified [NSIndexSet](https://developer.apple.com/documentation/foundation/nsindexset)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSIndexSet : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     convenience init()     class func indexSet() -> Self     convenience init(index value: Int)     class func indexSetWithIndex(_ value: Int) -> Self     convenience init(indexesInRange range: NSRange)     class func indexSetWithIndexesInRange(_ range: NSRange) -> Self     init(indexesInRange range: NSRange)     init(indexSet indexSet: NSIndexSet)     convenience init(index value: Int)     func isEqualToIndexSet(_ indexSet: NSIndexSet) -> Bool     var count: Int { get }     var firstIndex: Int { get }     var lastIndex: Int { get }     func indexGreaterThanIndex(_ value: Int) -> Int     func indexLessThanIndex(_ value: Int) -> Int     func indexGreaterThanOrEqualToIndex(_ value: Int) -> Int     func indexLessThanOrEqualToIndex(_ value: Int) -> Int     func getIndexes(_ indexBuffer: UnsafeMutablePointer<Int>, maxCount bufferSize: Int, inIndexRange range: NSRangePointer) -> Int     func countOfIndexesInRange(_ range: NSRange) -> Int     func containsIndex(_ value: Int) -> Bool     func containsIndexesInRange(_ range: NSRange) -> Bool     func containsIndexes(_ indexSet: NSIndexSet) -> Bool     func intersectsIndexesInRange(_ range: NSRange) -> Bool     func enumerateIndexesUsingBlock(_ block: (Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateIndexesWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateIndexesInRange(_ range: NSRange, options opts: NSEnumerationOptions, usingBlock block: (Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func indexPassingTest(_ predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexInRange(_ range: NSRange, options opts: NSEnumerationOptions, passingTest predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexesPassingTest(_ predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexesWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexesInRange(_ range: NSRange, options opts: NSEnumerationOptions, passingTest predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func enumerateRangesUsingBlock(_ block: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateRangesWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateRangesInRange(_ range: NSRange, options opts: NSEnumerationOptions, usingBlock block: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) } extension NSIndexSet : SequenceType {     func generate() -> NSIndexSetGenerator } extension NSIndexSet : SequenceType {     func generate() -> NSIndexSetGenerator } ``` | AnyObject, NSCoding, NSCopying, NSMutableCopying, NSSecureCoding, SequenceType |
| To | ``` class NSIndexSet : NSObject, NSCopying, NSMutableCopying, NSSecureCoding {     convenience init()     class func indexSet() -> Self     convenience init(index value: Int)     class func indexSetWithIndex(_ value: Int) -> Self     convenience init(indexesInRange range: NSRange)     class func indexSetWithIndexesInRange(_ range: NSRange) -> Self     init(indexesInRange range: NSRange)     init(indexSet indexSet: NSIndexSet)     convenience init(index value: Int)     func isEqualToIndexSet(_ indexSet: NSIndexSet) -> Bool     var count: Int { get }     var firstIndex: Int { get }     var lastIndex: Int { get }     func indexGreaterThanIndex(_ value: Int) -> Int     func indexLessThanIndex(_ value: Int) -> Int     func indexGreaterThanOrEqualToIndex(_ value: Int) -> Int     func indexLessThanOrEqualToIndex(_ value: Int) -> Int     func getIndexes(_ indexBuffer: UnsafeMutablePointer<Int>, maxCount bufferSize: Int, inIndexRange range: NSRangePointer) -> Int     func countOfIndexesInRange(_ range: NSRange) -> Int     func containsIndex(_ value: Int) -> Bool     func containsIndexesInRange(_ range: NSRange) -> Bool     func containsIndexes(_ indexSet: NSIndexSet) -> Bool     func intersectsIndexesInRange(_ range: NSRange) -> Bool     func enumerateIndexesUsingBlock(_ block: (Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateIndexesWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateIndexesInRange(_ range: NSRange, options opts: NSEnumerationOptions, usingBlock block: (Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func indexPassingTest(_ predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexInRange(_ range: NSRange, options opts: NSEnumerationOptions, passingTest predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexesPassingTest(_ predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexesWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexesInRange(_ range: NSRange, options opts: NSEnumerationOptions, passingTest predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func enumerateRangesUsingBlock(_ block: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateRangesWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateRangesInRange(_ range: NSRange, options opts: NSEnumerationOptions, usingBlock block: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) } extension NSIndexSet : SequenceType {     func generate() -> NSIndexSetGenerator } extension NSIndexSet : SequenceType {     func generate() -> NSIndexSetGenerator } ``` | NSCopying, NSMutableCopying, NSSecureCoding, SequenceType |

Modified [NSInputStream](https://developer.apple.com/documentation/foundation/inputstream)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSItemProvider](https://developer.apple.com/documentation/foundation/nsitemprovider)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [NSItemProviderErrorCode [enum]](https://developer.apple.com/documentation/foundation/nsitemprovidererrorcode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSJSONSerialization](https://developer.apple.com/documentation/foundation/nsjsonserialization)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSKeyedArchiver](https://developer.apple.com/documentation/foundation/nskeyedarchiver)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSKeyedUnarchiver](https://developer.apple.com/documentation/foundation/nskeyedunarchiver)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSKeyValueChange [enum]](https://developer.apple.com/documentation/foundation/nskeyvaluechange)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSKeyValueSetMutationKind [enum]](https://developer.apple.com/documentation/foundation/nskeyvaluesetmutationkind)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSLengthFormatter](https://developer.apple.com/documentation/foundation/nslengthformatter)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSLengthFormatterUnit [enum]](https://developer.apple.com/documentation/foundation/nslengthformatterunit)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSLinguisticTagger](https://developer.apple.com/documentation/foundation/nslinguistictagger)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSLocale](https://developer.apple.com/documentation/foundation/nslocale)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSLocale : NSObject, NSCopying, NSSecureCoding, NSCoding {     func objectForKey(_ key: AnyObject) -> AnyObject?     func displayNameForKey(_ key: AnyObject, value value: AnyObject) -> String?     init(localeIdentifier string: String)     init?(coder aDecoder: NSCoder) } extension NSLocale {     var localeIdentifier: String { get } } extension NSLocale {     class func autoupdatingCurrentLocale() -> NSLocale     class func currentLocale() -> NSLocale     class func systemLocale() -> NSLocale     convenience init(localeIdentifier ident: String)     class func localeWithLocaleIdentifier(_ ident: String) -> Self     convenience init() } extension NSLocale {     class func availableLocaleIdentifiers() -> [String]     class func ISOLanguageCodes() -> [String]     class func ISOCountryCodes() -> [String]     class func ISOCurrencyCodes() -> [String]     class func commonISOCurrencyCodes() -> [String]     class func preferredLanguages() -> [String]     class func componentsFromLocaleIdentifier(_ string: String) -> [String : String]     class func localeIdentifierFromComponents(_ dict: [String : String]) -> String     class func canonicalLocaleIdentifierFromString(_ string: String) -> String     class func canonicalLanguageIdentifierFromString(_ string: String) -> String     class func localeIdentifierFromWindowsLocaleCode(_ lcid: UInt32) -> String?     class func windowsLocaleCodeFromLocaleIdentifier(_ localeIdentifier: String) -> UInt32     class func characterDirectionForLanguage(_ isoLangCode: String) -> NSLocaleLanguageDirection     class func lineDirectionForLanguage(_ isoLangCode: String) -> NSLocaleLanguageDirection } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NSLocale : NSObject, NSCopying, NSSecureCoding {     func objectForKey(_ key: AnyObject) -> AnyObject?     func displayNameForKey(_ key: AnyObject, value value: AnyObject) -> String?     init(localeIdentifier string: String)     init?(coder aDecoder: NSCoder) } extension NSLocale {     var localeIdentifier: String { get } } extension NSLocale {     class func autoupdatingCurrentLocale() -> NSLocale     class func currentLocale() -> NSLocale     class func systemLocale() -> NSLocale     convenience init(localeIdentifier ident: String)     class func localeWithLocaleIdentifier(_ ident: String) -> Self     convenience init() } extension NSLocale {     class func availableLocaleIdentifiers() -> [String]     class func ISOLanguageCodes() -> [String]     class func ISOCountryCodes() -> [String]     class func ISOCurrencyCodes() -> [String]     class func commonISOCurrencyCodes() -> [String]     class func preferredLanguages() -> [String]     class func componentsFromLocaleIdentifier(_ string: String) -> [String : String]     class func localeIdentifierFromComponents(_ dict: [String : String]) -> String     class func canonicalLocaleIdentifierFromString(_ string: String) -> String     class func canonicalLanguageIdentifierFromString(_ string: String) -> String     class func localeIdentifierFromWindowsLocaleCode(_ lcid: UInt32) -> String?     class func windowsLocaleCodeFromLocaleIdentifier(_ localeIdentifier: String) -> UInt32     class func characterDirectionForLanguage(_ isoLangCode: String) -> NSLocaleLanguageDirection     class func lineDirectionForLanguage(_ isoLangCode: String) -> NSLocaleLanguageDirection } ``` | NSCopying, NSSecureCoding |

Modified [NSLocaleLanguageDirection [enum]](https://developer.apple.com/documentation/foundation/nslocale/languagedirection)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSLock](https://developer.apple.com/documentation/foundation/nslock)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSLocking |
| To | NSLocking |

Modified [NSMachPort](https://developer.apple.com/documentation/foundation/nsmachport)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSMachPortDelegate](https://developer.apple.com/documentation/foundation/nsmachportdelegate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol NSMachPortDelegate : NSPortDelegate, NSObjectProtocol {     optional func handleMachMessage(_ msg: UnsafeMutablePointer<Void>) } ``` | NSObjectProtocol, NSPortDelegate |
| To | ``` protocol NSMachPortDelegate : NSPortDelegate {     optional func handleMachMessage(_ msg: UnsafeMutablePointer<Void>) } ``` | NSPortDelegate |

Modified [NSMapTable](https://developer.apple.com/documentation/foundation/nsmaptable)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying, NSFastEnumeration |
| To | NSCoding, NSCopying, NSFastEnumeration |

Modified [NSMassFormatter](https://developer.apple.com/documentation/foundation/massformatter)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSMassFormatterUnit [enum]](https://developer.apple.com/documentation/foundation/massformatter/unit)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSMessagePort](https://developer.apple.com/documentation/foundation/messageport)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSMetadataItem](https://developer.apple.com/documentation/foundation/nsmetadataitem)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSMetadataQuery](https://developer.apple.com/documentation/foundation/nsmetadataquery)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSMetadataQueryAttributeValueTuple](https://developer.apple.com/documentation/foundation/nsmetadataqueryattributevaluetuple)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSMetadataQueryResultGroup](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSMutableArray](https://developer.apple.com/documentation/foundation/nsmutablearray)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSMutableAttributedString](https://developer.apple.com/documentation/foundation/nsmutableattributedstring)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSMutableCharacterSet](https://developer.apple.com/documentation/foundation/nsmutablecharacterset)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSMutableCharacterSet : NSCharacterSet {     func addCharactersInRange(_ aRange: NSRange)     func removeCharactersInRange(_ aRange: NSRange)     func addCharactersInString(_ aString: String)     func removeCharactersInString(_ aString: String)     func formUnionWithCharacterSet(_ otherSet: NSCharacterSet)     func formIntersectionWithCharacterSet(_ otherSet: NSCharacterSet)     func invert()     class func controlCharacterSet() -> NSMutableCharacterSet     class func whitespaceCharacterSet() -> NSMutableCharacterSet     class func whitespaceAndNewlineCharacterSet() -> NSMutableCharacterSet     class func decimalDigitCharacterSet() -> NSMutableCharacterSet     class func letterCharacterSet() -> NSMutableCharacterSet     class func lowercaseLetterCharacterSet() -> NSMutableCharacterSet     class func uppercaseLetterCharacterSet() -> NSMutableCharacterSet     class func nonBaseCharacterSet() -> NSMutableCharacterSet     class func alphanumericCharacterSet() -> NSMutableCharacterSet     class func decomposableCharacterSet() -> NSMutableCharacterSet     class func illegalCharacterSet() -> NSMutableCharacterSet     class func punctuationCharacterSet() -> NSMutableCharacterSet     class func capitalizedLetterCharacterSet() -> NSMutableCharacterSet     class func symbolCharacterSet() -> NSMutableCharacterSet     class func newlineCharacterSet() -> NSMutableCharacterSet      init(range aRange: NSRange)     class func characterSetWithRange(_ aRange: NSRange) -> NSMutableCharacterSet      init(charactersInString aString: String)     class func characterSetWithCharactersInString(_ aString: String) -> NSMutableCharacterSet      init(bitmapRepresentation data: NSData)     class func characterSetWithBitmapRepresentation(_ data: NSData) -> NSMutableCharacterSet      init?(contentsOfFile fName: String)     class func characterSetWithContentsOfFile(_ fName: String) -> NSMutableCharacterSet? } ``` | AnyObject, NSCopying, NSMutableCopying |
| To | ``` class NSMutableCharacterSet : NSCharacterSet, NSCopying, NSMutableCopying {     func addCharactersInRange(_ aRange: NSRange)     func removeCharactersInRange(_ aRange: NSRange)     func addCharactersInString(_ aString: String)     func removeCharactersInString(_ aString: String)     func formUnionWithCharacterSet(_ otherSet: NSCharacterSet)     func formIntersectionWithCharacterSet(_ otherSet: NSCharacterSet)     func invert()     class func controlCharacterSet() -> NSMutableCharacterSet     class func whitespaceCharacterSet() -> NSMutableCharacterSet     class func whitespaceAndNewlineCharacterSet() -> NSMutableCharacterSet     class func decimalDigitCharacterSet() -> NSMutableCharacterSet     class func letterCharacterSet() -> NSMutableCharacterSet     class func lowercaseLetterCharacterSet() -> NSMutableCharacterSet     class func uppercaseLetterCharacterSet() -> NSMutableCharacterSet     class func nonBaseCharacterSet() -> NSMutableCharacterSet     class func alphanumericCharacterSet() -> NSMutableCharacterSet     class func decomposableCharacterSet() -> NSMutableCharacterSet     class func illegalCharacterSet() -> NSMutableCharacterSet     class func punctuationCharacterSet() -> NSMutableCharacterSet     class func capitalizedLetterCharacterSet() -> NSMutableCharacterSet     class func symbolCharacterSet() -> NSMutableCharacterSet     class func newlineCharacterSet() -> NSMutableCharacterSet      init(range aRange: NSRange)     class func characterSetWithRange(_ aRange: NSRange) -> NSMutableCharacterSet      init(charactersInString aString: String)     class func characterSetWithCharactersInString(_ aString: String) -> NSMutableCharacterSet      init(bitmapRepresentation data: NSData)     class func characterSetWithBitmapRepresentation(_ data: NSData) -> NSMutableCharacterSet      init?(contentsOfFile fName: String)     class func characterSetWithContentsOfFile(_ fName: String) -> NSMutableCharacterSet? } ``` | NSCopying, NSMutableCopying |

Modified [NSMutableData](https://developer.apple.com/documentation/foundation/nsmutabledata)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSMutableDictionary](https://developer.apple.com/documentation/foundation/nsmutabledictionary)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSMutableIndexSet](https://developer.apple.com/documentation/foundation/nsmutableindexset)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSMutableOrderedSet](https://developer.apple.com/documentation/foundation/nsmutableorderedset)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSMutableSet](https://developer.apple.com/documentation/foundation/nsmutableset)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSMutableString](https://developer.apple.com/documentation/foundation/nsmutablestring)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSMutableURLRequest](https://developer.apple.com/documentation/foundation/nsmutableurlrequest)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSNetServicesError [enum]](https://developer.apple.com/documentation/foundation/netservice/errorcode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSNotification](https://developer.apple.com/documentation/foundation/nsnotification)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [NSNotificationCenter](https://developer.apple.com/documentation/foundation/notificationcenter)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSNotificationQueue](https://developer.apple.com/documentation/foundation/nsnotificationqueue)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSNull](https://developer.apple.com/documentation/foundation/nsnull)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSNull : NSObject, NSCopying, NSSecureCoding, NSCoding {      init()     class func null() -> NSNull } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NSNull : NSObject, NSCopying, NSSecureCoding {      init()     class func null() -> NSNull } ``` | NSCopying, NSSecureCoding |

Modified [NSNumber](https://developer.apple.com/documentation/foundation/nsnumber)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSNumber : NSValue {     init?(coder aDecoder: NSCoder)     init(char value: Int8)     init(unsignedChar value: UInt8)     init(short value: Int16)     init(unsignedShort value: UInt16)     init(int value: Int32)     init(unsignedInt value: UInt32)     init(long value: Int)     init(unsignedLong value: UInt)     init(longLong value: Int64)     init(unsignedLongLong value: UInt64)     init(float value: Float)     init(double value: Double)     init(bool value: Bool)     init(integer value: Int)     init(unsignedInteger value: Int)     var charValue: Int8 { get }     var unsignedCharValue: UInt8 { get }     var shortValue: Int16 { get }     var unsignedShortValue: UInt16 { get }     var intValue: Int32 { get }     var unsignedIntValue: UInt32 { get }     var longValue: Int { get }     var unsignedLongValue: UInt { get }     var longLongValue: Int64 { get }     var unsignedLongLongValue: UInt64 { get }     var floatValue: Float { get }     var doubleValue: Double { get }     var boolValue: Bool { get }     var integerValue: Int { get }     var unsignedIntegerValue: Int { get }     var stringValue: String { get }     func compare(_ otherNumber: NSNumber) -> NSComparisonResult     func isEqualToNumber(_ number: NSNumber) -> Bool     func descriptionWithLocale(_ locale: AnyObject?) -> String } extension NSNumber {     var decimalValue: NSDecimal { get } } extension NSNumber : FloatLiteralConvertible, IntegerLiteralConvertible, BooleanLiteralConvertible {     required convenience init(integerLiteral value: Int)     required convenience init(floatLiteral value: Double)     required convenience init(booleanLiteral value: Bool) } extension NSNumber {     class func numberWithChar(_ value: Int8) -> NSNumber     class func numberWithUnsignedChar(_ value: UInt8) -> NSNumber     class func numberWithShort(_ value: Int16) -> NSNumber     class func numberWithUnsignedShort(_ value: UInt16) -> NSNumber     class func numberWithInt(_ value: Int32) -> NSNumber     class func numberWithUnsignedInt(_ value: UInt32) -> NSNumber     class func numberWithLong(_ value: Int) -> NSNumber     class func numberWithUnsignedLong(_ value: UInt) -> NSNumber     class func numberWithLongLong(_ value: Int64) -> NSNumber     class func numberWithUnsignedLongLong(_ value: UInt64) -> NSNumber     class func numberWithFloat(_ value: Float) -> NSNumber     class func numberWithDouble(_ value: Double) -> NSNumber     class func numberWithBool(_ value: Bool) -> NSNumber     class func numberWithInteger(_ value: Int) -> NSNumber     class func numberWithUnsignedInteger(_ value: Int) -> NSNumber } extension NSNumber : FloatLiteralConvertible, IntegerLiteralConvertible, BooleanLiteralConvertible {     required convenience init(integerLiteral value: Int)     required convenience init(floatLiteral value: Double)     required convenience init(booleanLiteral value: Bool) } ``` | AnyObject, BooleanLiteralConvertible, FloatLiteralConvertible, IntegerLiteralConvertible |
| To | ``` class NSNumber : NSValue {     init?(coder aDecoder: NSCoder)     init(char value: Int8)     init(unsignedChar value: UInt8)     init(short value: Int16)     init(unsignedShort value: UInt16)     init(int value: Int32)     init(unsignedInt value: UInt32)     init(long value: Int)     init(unsignedLong value: UInt)     init(longLong value: Int64)     init(unsignedLongLong value: UInt64)     init(float value: Float)     init(double value: Double)     init(bool value: Bool)     init(integer value: Int)     init(unsignedInteger value: UInt)     var charValue: Int8 { get }     var unsignedCharValue: UInt8 { get }     var shortValue: Int16 { get }     var unsignedShortValue: UInt16 { get }     var intValue: Int32 { get }     var unsignedIntValue: UInt32 { get }     var longValue: Int { get }     var unsignedLongValue: UInt { get }     var longLongValue: Int64 { get }     var unsignedLongLongValue: UInt64 { get }     var floatValue: Float { get }     var doubleValue: Double { get }     var boolValue: Bool { get }     var integerValue: Int { get }     var unsignedIntegerValue: UInt { get }     var stringValue: String { get }     func compare(_ otherNumber: NSNumber) -> NSComparisonResult     func isEqualToNumber(_ number: NSNumber) -> Bool     func descriptionWithLocale(_ locale: AnyObject?) -> String } extension NSNumber {     var decimalValue: NSDecimal { get } } extension NSNumber : FloatLiteralConvertible, IntegerLiteralConvertible, BooleanLiteralConvertible {     required convenience init(integerLiteral value: Int)     required convenience init(floatLiteral value: Double)     required convenience init(booleanLiteral value: Bool) } extension NSNumber {     class func numberWithChar(_ value: Int8) -> NSNumber     class func numberWithUnsignedChar(_ value: UInt8) -> NSNumber     class func numberWithShort(_ value: Int16) -> NSNumber     class func numberWithUnsignedShort(_ value: UInt16) -> NSNumber     class func numberWithInt(_ value: Int32) -> NSNumber     class func numberWithUnsignedInt(_ value: UInt32) -> NSNumber     class func numberWithLong(_ value: Int) -> NSNumber     class func numberWithUnsignedLong(_ value: UInt) -> NSNumber     class func numberWithLongLong(_ value: Int64) -> NSNumber     class func numberWithUnsignedLongLong(_ value: UInt64) -> NSNumber     class func numberWithFloat(_ value: Float) -> NSNumber     class func numberWithDouble(_ value: Double) -> NSNumber     class func numberWithBool(_ value: Bool) -> NSNumber     class func numberWithInteger(_ value: Int) -> NSNumber     class func numberWithUnsignedInteger(_ value: UInt) -> NSNumber } extension NSNumber : FloatLiteralConvertible, IntegerLiteralConvertible, BooleanLiteralConvertible {     required convenience init(integerLiteral value: Int)     required convenience init(floatLiteral value: Double)     required convenience init(booleanLiteral value: Bool) } ``` | BooleanLiteralConvertible, FloatLiteralConvertible, IntegerLiteralConvertible |

Modified [NSNumber.init(unsignedInteger: UInt)](https://developer.apple.com/documentation/foundation/nsnumber/1412531-init)

|  | Declaration |
| --- | --- |
| From | ``` init(unsignedInteger value: Int) ``` |
| To | ``` init(unsignedInteger value: UInt) ``` |

Modified [NSNumber.unsignedIntegerValue](https://developer.apple.com/documentation/foundation/nsnumber/1413324-unsignedintegervalue)

|  | Declaration |
| --- | --- |
| From | ``` var unsignedIntegerValue: Int { get } ``` |
| To | ``` var unsignedIntegerValue: UInt { get } ``` |

Modified [NSNumberFormatter](https://developer.apple.com/documentation/foundation/numberformatter)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSNumberFormatterBehavior [enum]](https://developer.apple.com/documentation/foundation/numberformatter/behavior)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSNumberFormatterPadPosition [enum]](https://developer.apple.com/documentation/foundation/numberformatter/padposition)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSNumberFormatterRoundingMode [enum]](https://developer.apple.com/documentation/foundation/nsnumberformatterroundingmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSNumberFormatterStyle [enum]](https://developer.apple.com/documentation/foundation/numberformatter/style)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSOperation](https://developer.apple.com/documentation/foundation/nsoperation)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSOperationQueue](https://developer.apple.com/documentation/foundation/operationqueue)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSOperationQueuePriority [enum]](https://developer.apple.com/documentation/foundation/nsoperationqueuepriority)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSOrderedSet](https://developer.apple.com/documentation/foundation/nsorderedset)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSOrderedSet : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding, NSFastEnumeration {     var count: Int { get }     func objectAtIndex(_ idx: Int) -> AnyObject     func indexOfObject(_ object: AnyObject) -> Int     init()     init(objects objects: UnsafePointer<AnyObject?>, count cnt: Int)     init?(coder aDecoder: NSCoder) } extension NSOrderedSet {     func valueForKey(_ key: String) -> AnyObject     func setValue(_ value: AnyObject?, forKey key: String) } extension NSOrderedSet {     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String) } extension NSOrderedSet : SequenceType {     func generate() -> NSFastGenerator } extension NSOrderedSet {     convenience init(objects elements: AnyObject...) } extension NSOrderedSet : ArrayLiteralConvertible {     required convenience init(arrayLiteral elements: AnyObject...) } extension NSOrderedSet {     func getObjects(_ objects: AutoreleasingUnsafeMutablePointer<AnyObject?>, range range: NSRange)     func objectsAtIndexes(_ indexes: NSIndexSet) -> [AnyObject]     var firstObject: AnyObject? { get }     var lastObject: AnyObject? { get }     func isEqualToOrderedSet(_ other: NSOrderedSet) -> Bool     func containsObject(_ object: AnyObject) -> Bool     func intersectsOrderedSet(_ other: NSOrderedSet) -> Bool     func intersectsSet(_ set: Set<NSObject>) -> Bool     func isSubsetOfOrderedSet(_ other: NSOrderedSet) -> Bool     func isSubsetOfSet(_ set: Set<NSObject>) -> Bool     subscript (_ idx: Int) -> AnyObject { get }     func objectAtIndexedSubscript(_ idx: Int) -> AnyObject     func objectEnumerator() -> NSEnumerator     func reverseObjectEnumerator() -> NSEnumerator     @NSCopying var reversedOrderedSet: NSOrderedSet { get }     var array: [AnyObject] { get }     var set: Set<NSObject> { get }     func enumerateObjectsUsingBlock(_ block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, usingBlock block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func indexOfObjectPassingTest(_ predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexOfObjectWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexOfObjectAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexesOfObjectsPassingTest(_ predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexesOfObjectsWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexesOfObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexOfObject(_ object: AnyObject, inSortedRange range: NSRange, options opts: NSBinarySearchingOptions, usingComparator cmp: NSComparator) -> Int     func sortedArrayUsingComparator(_ cmptr: NSComparator) -> [AnyObject]     func sortedArrayWithOptions(_ opts: NSSortOptions, usingComparator cmptr: NSComparator) -> [AnyObject]     var description: String { get }     func descriptionWithLocale(_ locale: AnyObject?) -> String     func descriptionWithLocale(_ locale: AnyObject?, indent level: Int) -> String } extension NSOrderedSet {     convenience init()     class func orderedSet() -> Self     convenience init(object object: AnyObject)     class func orderedSetWithObject(_ object: AnyObject) -> Self     convenience init(objects objects: UnsafePointer<AnyObject?>, count cnt: Int)     class func orderedSetWithObjects(_ objects: UnsafePointer<AnyObject?>, count cnt: Int) -> Self     convenience init(orderedSet set: NSOrderedSet)     class func orderedSetWithOrderedSet(_ set: NSOrderedSet) -> Self     convenience init(orderedSet set: NSOrderedSet, range range: NSRange, copyItems flag: Bool)     class func orderedSetWithOrderedSet(_ set: NSOrderedSet, range range: NSRange, copyItems flag: Bool) -> Self     convenience init(array array: [AnyObject])     class func orderedSetWithArray(_ array: [AnyObject]) -> Self     convenience init(array array: [AnyObject], range range: NSRange, copyItems flag: Bool)     class func orderedSetWithArray(_ array: [AnyObject], range range: NSRange, copyItems flag: Bool) -> Self     convenience init(set set: Set<NSObject>)     class func orderedSetWithSet(_ set: Set<NSObject>) -> Self     convenience init(set set: Set<NSObject>, copyItems flag: Bool)     class func orderedSetWithSet(_ set: Set<NSObject>, copyItems flag: Bool) -> Self     convenience init(object object: AnyObject)     convenience init(orderedSet set: NSOrderedSet)     convenience init(orderedSet set: NSOrderedSet, copyItems flag: Bool)     convenience init(orderedSet set: NSOrderedSet, range range: NSRange, copyItems flag: Bool)     convenience init(array array: [AnyObject])     convenience init(array set: [AnyObject], copyItems flag: Bool)     convenience init(array set: [AnyObject], range range: NSRange, copyItems flag: Bool)     convenience init(set set: Set<NSObject>)     convenience init(set set: Set<NSObject>, copyItems flag: Bool) } extension NSOrderedSet {     func filteredOrderedSetUsingPredicate(_ p: NSPredicate) -> NSOrderedSet } extension NSOrderedSet {     func sortedArrayUsingDescriptors(_ sortDescriptors: [NSSortDescriptor]) -> [AnyObject] } extension NSOrderedSet : ArrayLiteralConvertible {     required convenience init(arrayLiteral elements: AnyObject...) } extension NSOrderedSet {     convenience init(objects elements: AnyObject...) } extension NSOrderedSet : SequenceType {     func generate() -> NSFastGenerator } ``` | AnyObject, ArrayLiteralConvertible, NSCoding, NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding, SequenceType |
| To | ``` class NSOrderedSet : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSFastEnumeration {     var count: Int { get }     func objectAtIndex(_ idx: Int) -> AnyObject     func indexOfObject(_ object: AnyObject) -> Int     init()     init(objects objects: UnsafePointer<AnyObject?>, count cnt: Int)     init?(coder aDecoder: NSCoder) } extension NSOrderedSet {     func valueForKey(_ key: String) -> AnyObject     func setValue(_ value: AnyObject?, forKey key: String) } extension NSOrderedSet {     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String) } extension NSOrderedSet : SequenceType {     func generate() -> NSFastGenerator } extension NSOrderedSet {     convenience init(objects elements: AnyObject...) } extension NSOrderedSet : ArrayLiteralConvertible {     required convenience init(arrayLiteral elements: AnyObject...) } extension NSOrderedSet {     func getObjects(_ objects: AutoreleasingUnsafeMutablePointer<AnyObject?>, range range: NSRange)     func objectsAtIndexes(_ indexes: NSIndexSet) -> [AnyObject]     var firstObject: AnyObject? { get }     var lastObject: AnyObject? { get }     func isEqualToOrderedSet(_ other: NSOrderedSet) -> Bool     func containsObject(_ object: AnyObject) -> Bool     func intersectsOrderedSet(_ other: NSOrderedSet) -> Bool     func intersectsSet(_ set: Set<NSObject>) -> Bool     func isSubsetOfOrderedSet(_ other: NSOrderedSet) -> Bool     func isSubsetOfSet(_ set: Set<NSObject>) -> Bool     subscript (_ idx: Int) -> AnyObject { get }     func objectAtIndexedSubscript(_ idx: Int) -> AnyObject     func objectEnumerator() -> NSEnumerator     func reverseObjectEnumerator() -> NSEnumerator     @NSCopying var reversedOrderedSet: NSOrderedSet { get }     var array: [AnyObject] { get }     var set: Set<NSObject> { get }     func enumerateObjectsUsingBlock(_ block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, usingBlock block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func indexOfObjectPassingTest(_ predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexOfObjectWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexOfObjectAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexesOfObjectsPassingTest(_ predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexesOfObjectsWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexesOfObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexOfObject(_ object: AnyObject, inSortedRange range: NSRange, options opts: NSBinarySearchingOptions, usingComparator cmp: NSComparator) -> Int     func sortedArrayUsingComparator(_ cmptr: NSComparator) -> [AnyObject]     func sortedArrayWithOptions(_ opts: NSSortOptions, usingComparator cmptr: NSComparator) -> [AnyObject]     var description: String { get }     func descriptionWithLocale(_ locale: AnyObject?) -> String     func descriptionWithLocale(_ locale: AnyObject?, indent level: Int) -> String } extension NSOrderedSet {     convenience init()     class func orderedSet() -> Self     convenience init(object object: AnyObject)     class func orderedSetWithObject(_ object: AnyObject) -> Self     convenience init(objects objects: UnsafePointer<AnyObject?>, count cnt: Int)     class func orderedSetWithObjects(_ objects: UnsafePointer<AnyObject?>, count cnt: Int) -> Self     convenience init(orderedSet set: NSOrderedSet)     class func orderedSetWithOrderedSet(_ set: NSOrderedSet) -> Self     convenience init(orderedSet set: NSOrderedSet, range range: NSRange, copyItems flag: Bool)     class func orderedSetWithOrderedSet(_ set: NSOrderedSet, range range: NSRange, copyItems flag: Bool) -> Self     convenience init(array array: [AnyObject])     class func orderedSetWithArray(_ array: [AnyObject]) -> Self     convenience init(array array: [AnyObject], range range: NSRange, copyItems flag: Bool)     class func orderedSetWithArray(_ array: [AnyObject], range range: NSRange, copyItems flag: Bool) -> Self     convenience init(set set: Set<NSObject>)     class func orderedSetWithSet(_ set: Set<NSObject>) -> Self     convenience init(set set: Set<NSObject>, copyItems flag: Bool)     class func orderedSetWithSet(_ set: Set<NSObject>, copyItems flag: Bool) -> Self     convenience init(object object: AnyObject)     convenience init(orderedSet set: NSOrderedSet)     convenience init(orderedSet set: NSOrderedSet, copyItems flag: Bool)     convenience init(orderedSet set: NSOrderedSet, range range: NSRange, copyItems flag: Bool)     convenience init(array array: [AnyObject])     convenience init(array set: [AnyObject], copyItems flag: Bool)     convenience init(array set: [AnyObject], range range: NSRange, copyItems flag: Bool)     convenience init(set set: Set<NSObject>)     convenience init(set set: Set<NSObject>, copyItems flag: Bool) } extension NSOrderedSet {     func filteredOrderedSetUsingPredicate(_ p: NSPredicate) -> NSOrderedSet } extension NSOrderedSet {     func sortedArrayUsingDescriptors(_ sortDescriptors: [NSSortDescriptor]) -> [AnyObject] } extension NSOrderedSet : ArrayLiteralConvertible {     required convenience init(arrayLiteral elements: AnyObject...) } extension NSOrderedSet {     convenience init(objects elements: AnyObject...) } extension NSOrderedSet : SequenceType {     func generate() -> NSFastGenerator } ``` | ArrayLiteralConvertible, NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding, SequenceType |

Modified [NSOrthography](https://developer.apple.com/documentation/foundation/nsorthography)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [NSOutputStream](https://developer.apple.com/documentation/foundation/nsoutputstream)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSPersonNameComponents](https://developer.apple.com/documentation/foundation/nspersonnamecomponents)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSPersonNameComponents : NSObject, NSCopying, NSSecureCoding, NSCoding {     var namePrefix: String?     var givenName: String?     var middleName: String?     var familyName: String?     var nameSuffix: String?     var nickname: String?     @NSCopying var phoneticRepresentation: NSPersonNameComponents? } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NSPersonNameComponents : NSObject, NSCopying, NSSecureCoding {     var namePrefix: String?     var givenName: String?     var middleName: String?     var familyName: String?     var nameSuffix: String?     var nickname: String?     @NSCopying var phoneticRepresentation: NSPersonNameComponents? } ``` | NSCopying, NSSecureCoding |

Modified [NSPersonNameComponentsFormatter](https://developer.apple.com/documentation/foundation/nspersonnamecomponentsformatter)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSPersonNameComponentsFormatterStyle [enum]](https://developer.apple.com/documentation/foundation/nspersonnamecomponentsformatterstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSPipe](https://developer.apple.com/documentation/foundation/nspipe)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSPointerArray](https://developer.apple.com/documentation/foundation/nspointerarray)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying, NSFastEnumeration |
| To | NSCoding, NSCopying, NSFastEnumeration |

Modified [NSPointerFunctions](https://developer.apple.com/documentation/foundation/nspointerfunctions)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [NSPort](https://developer.apple.com/documentation/foundation/nsport)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [NSPostingStyle [enum]](https://developer.apple.com/documentation/foundation/nspostingstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSPredicate](https://developer.apple.com/documentation/foundation/nspredicate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSPredicate : NSObject, NSSecureCoding, NSCoding, NSCopying {      init(format predicateFormat: String, argumentArray arguments: [AnyObject]?)     class func predicateWithFormat(_ predicateFormat: String, argumentArray arguments: [AnyObject]?) -> NSPredicate      init(format predicateFormat: String, arguments argList: CVaListPointer)     class func predicateWithFormat(_ predicateFormat: String, arguments argList: CVaListPointer) -> NSPredicate      init?(fromMetadataQueryString queryString: String)     class func predicateFromMetadataQueryString(_ queryString: String) -> NSPredicate?      init(value value: Bool)     class func predicateWithValue(_ value: Bool) -> NSPredicate      init(block block: (AnyObject, [String : AnyObject]?) -> Bool)     class func predicateWithBlock(_ block: (AnyObject, [String : AnyObject]?) -> Bool) -> NSPredicate     var predicateFormat: String { get }     func predicateWithSubstitutionVariables(_ variables: [String : AnyObject]) -> Self     func evaluateWithObject(_ object: AnyObject?) -> Bool     func evaluateWithObject(_ object: AnyObject?, substitutionVariables bindings: [String : AnyObject]?) -> Bool     func allowEvaluation() } extension NSPredicate {     convenience init(format predicateFormat: String, _ args: CVarArgType...) } extension NSPredicate {     convenience init(format predicateFormat: String, _ args: CVarArgType...) } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NSPredicate : NSObject, NSSecureCoding, NSCopying {      init(format predicateFormat: String, argumentArray arguments: [AnyObject]?)     class func predicateWithFormat(_ predicateFormat: String, argumentArray arguments: [AnyObject]?) -> NSPredicate      init(format predicateFormat: String, arguments argList: CVaListPointer)     class func predicateWithFormat(_ predicateFormat: String, arguments argList: CVaListPointer) -> NSPredicate      init?(fromMetadataQueryString queryString: String)     class func predicateFromMetadataQueryString(_ queryString: String) -> NSPredicate?      init(value value: Bool)     class func predicateWithValue(_ value: Bool) -> NSPredicate      init(block block: (AnyObject, [String : AnyObject]?) -> Bool)     class func predicateWithBlock(_ block: (AnyObject, [String : AnyObject]?) -> Bool) -> NSPredicate     var predicateFormat: String { get }     func predicateWithSubstitutionVariables(_ variables: [String : AnyObject]) -> Self     func evaluateWithObject(_ object: AnyObject?) -> Bool     func evaluateWithObject(_ object: AnyObject?, substitutionVariables bindings: [String : AnyObject]?) -> Bool     func allowEvaluation() } extension NSPredicate {     convenience init(format predicateFormat: String, _ args: CVarArgType...) } extension NSPredicate {     convenience init(format predicateFormat: String, _ args: CVarArgType...) } ``` | NSCopying, NSSecureCoding |

Modified [NSPredicateOperatorType [enum]](https://developer.apple.com/documentation/foundation/nspredicateoperatortype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSProcessInfo](https://developer.apple.com/documentation/foundation/processinfo)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSProgress](https://developer.apple.com/documentation/foundation/nsprogress)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSPropertyListFormat [enum]](https://developer.apple.com/documentation/foundation/nspropertylistformat)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSPropertyListSerialization](https://developer.apple.com/documentation/foundation/nspropertylistserialization)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSProxy](https://developer.apple.com/documentation/foundation/nsproxy)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSObjectProtocol |
| To | NSObjectProtocol |

Modified [NSPurgeableData](https://developer.apple.com/documentation/foundation/nspurgeabledata)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSDiscardableContent |
| To | NSDiscardableContent |

Modified [NSQualityOfService [enum]](https://developer.apple.com/documentation/foundation/nsqualityofservice)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSRecursiveLock](https://developer.apple.com/documentation/foundation/nsrecursivelock)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSLocking |
| To | NSLocking |

Modified [NSRegularExpression](https://developer.apple.com/documentation/foundation/nsregularexpression)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [NSRoundingMode [enum]](https://developer.apple.com/documentation/foundation/decimal/roundingmode-vau)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSRunLoop](https://developer.apple.com/documentation/foundation/nsrunloop)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSScanner](https://developer.apple.com/documentation/foundation/scanner)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [NSSearchPathDirectory [enum]](https://developer.apple.com/documentation/foundation/filemanager/searchpathdirectory)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSSet](https://developer.apple.com/documentation/foundation/nsset)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSSet : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding, NSFastEnumeration {     var count: Int { get }     func member(_ object: AnyObject) -> AnyObject?     func objectEnumerator() -> NSEnumerator     init()     init(objects objects: UnsafePointer<AnyObject?>, count cnt: Int)     init?(coder aDecoder: NSCoder) } extension NSSet {     func valueForKey(_ key: String) -> AnyObject     func setValue(_ value: AnyObject?, forKey key: String) } extension NSSet {     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String) } extension NSSet {     func filteredSetUsingPredicate(_ predicate: NSPredicate) -> Set<NSObject> } extension NSSet : SequenceType {     func generate() -> NSFastGenerator } extension NSSet {     convenience init(objects elements: AnyObject...) } extension NSSet : ArrayLiteralConvertible {     required convenience init(arrayLiteral elements: AnyObject...) } extension NSSet {     @objc(_swiftInitWithSet_NSSet:) convenience init(set anSet: NSSet) } extension NSSet : _Reflectable { } extension NSSet {     var allObjects: [AnyObject] { get }     func anyObject() -> AnyObject?     func containsObject(_ anObject: AnyObject) -> Bool     var description: String { get }     func descriptionWithLocale(_ locale: AnyObject?) -> String     func intersectsSet(_ otherSet: Set<NSObject>) -> Bool     func isEqualToSet(_ otherSet: Set<NSObject>) -> Bool     func isSubsetOfSet(_ otherSet: Set<NSObject>) -> Bool     func makeObjectsPerformSelector(_ aSelector: Selector)     func makeObjectsPerformSelector(_ aSelector: Selector, withObject argument: AnyObject?)     func setByAddingObject(_ anObject: AnyObject) -> Set<NSObject>     func setByAddingObjectsFromSet(_ other: Set<NSObject>) -> Set<NSObject>     func setByAddingObjectsFromArray(_ other: [AnyObject]) -> Set<NSObject>     func enumerateObjectsUsingBlock(_ block: (AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void)     func objectsPassingTest(_ predicate: (AnyObject, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject>     func objectsWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject> } extension NSSet {     class func set() -> Self     convenience init(object object: AnyObject)     class func setWithObject(_ object: AnyObject) -> Self     class func setWithObjects(_ objects: UnsafePointer<AnyObject?>, count cnt: Int) -> Self     convenience init(set set: Set<NSObject>)     class func setWithSet(_ set: Set<NSObject>) -> Self     convenience init(array array: [AnyObject])     class func setWithArray(_ array: [AnyObject]) -> Self     convenience init(set set: Set<NSObject>)     convenience init(set set: Set<NSObject>, copyItems flag: Bool)     convenience init(array array: [AnyObject]) } extension NSSet {     func sortedArrayUsingDescriptors(_ sortDescriptors: [NSSortDescriptor]) -> [AnyObject] } extension NSSet : _Reflectable { } extension NSSet {     @objc(_swiftInitWithSet_NSSet:) convenience init(set anSet: NSSet) } extension NSSet : ArrayLiteralConvertible {     required convenience init(arrayLiteral elements: AnyObject...) } extension NSSet {     convenience init(objects elements: AnyObject...) } extension NSSet : SequenceType {     func generate() -> NSFastGenerator } ``` | AnyObject, ArrayLiteralConvertible, NSCoding, NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding, SequenceType |
| To | ``` class NSSet : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSFastEnumeration {     var count: Int { get }     func member(_ object: AnyObject) -> AnyObject?     func objectEnumerator() -> NSEnumerator     init()     init(objects objects: UnsafePointer<AnyObject?>, count cnt: Int)     init?(coder aDecoder: NSCoder) } extension NSSet {     func valueForKey(_ key: String) -> AnyObject     func setValue(_ value: AnyObject?, forKey key: String) } extension NSSet {     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String) } extension NSSet {     func filteredSetUsingPredicate(_ predicate: NSPredicate) -> Set<NSObject> } extension NSSet : SequenceType {     func generate() -> NSFastGenerator } extension NSSet {     convenience init(objects elements: AnyObject...) } extension NSSet : ArrayLiteralConvertible {     required convenience init(arrayLiteral elements: AnyObject...) } extension NSSet {     @objc(_swiftInitWithSet_NSSet:) convenience init(set anSet: NSSet) } extension NSSet : _Reflectable { } extension NSSet {     var allObjects: [AnyObject] { get }     func anyObject() -> AnyObject?     func containsObject(_ anObject: AnyObject) -> Bool     var description: String { get }     func descriptionWithLocale(_ locale: AnyObject?) -> String     func intersectsSet(_ otherSet: Set<NSObject>) -> Bool     func isEqualToSet(_ otherSet: Set<NSObject>) -> Bool     func isSubsetOfSet(_ otherSet: Set<NSObject>) -> Bool     func makeObjectsPerformSelector(_ aSelector: Selector)     func makeObjectsPerformSelector(_ aSelector: Selector, withObject argument: AnyObject?)     func setByAddingObject(_ anObject: AnyObject) -> Set<NSObject>     func setByAddingObjectsFromSet(_ other: Set<NSObject>) -> Set<NSObject>     func setByAddingObjectsFromArray(_ other: [AnyObject]) -> Set<NSObject>     func enumerateObjectsUsingBlock(_ block: (AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void)     func objectsPassingTest(_ predicate: (AnyObject, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject>     func objectsWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject> } extension NSSet {     class func set() -> Self     convenience init(object object: AnyObject)     class func setWithObject(_ object: AnyObject) -> Self     class func setWithObjects(_ objects: UnsafePointer<AnyObject?>, count cnt: Int) -> Self     convenience init(set set: Set<NSObject>)     class func setWithSet(_ set: Set<NSObject>) -> Self     convenience init(array array: [AnyObject])     class func setWithArray(_ array: [AnyObject]) -> Self     convenience init(set set: Set<NSObject>)     convenience init(set set: Set<NSObject>, copyItems flag: Bool)     convenience init(array array: [AnyObject]) } extension NSSet {     func sortedArrayUsingDescriptors(_ sortDescriptors: [NSSortDescriptor]) -> [AnyObject] } extension NSSet : _Reflectable { } extension NSSet {     @objc(_swiftInitWithSet_NSSet:) convenience init(set anSet: NSSet) } extension NSSet : ArrayLiteralConvertible {     required convenience init(arrayLiteral elements: AnyObject...) } extension NSSet {     convenience init(objects elements: AnyObject...) } extension NSSet : SequenceType {     func generate() -> NSFastGenerator } ``` | ArrayLiteralConvertible, NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding, SequenceType |

Modified NSSimpleCString

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSSortDescriptor](https://developer.apple.com/documentation/foundation/nssortdescriptor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSSortDescriptor : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init(key key: String?, ascending ascending: Bool)     class func sortDescriptorWithKey(_ key: String?, ascending ascending: Bool) -> Self     convenience init(key key: String?, ascending ascending: Bool, selector selector: Selector)     class func sortDescriptorWithKey(_ key: String?, ascending ascending: Bool, selector selector: Selector) -> Self     init(key key: String?, ascending ascending: Bool)     init(key key: String?, ascending ascending: Bool, selector selector: Selector)     init?(coder coder: NSCoder)     var key: String? { get }     var ascending: Bool { get }     var selector: Selector { get }     func allowEvaluation()     convenience init(key key: String?, ascending ascending: Bool, comparator cmptr: NSComparator)     class func sortDescriptorWithKey(_ key: String?, ascending ascending: Bool, comparator cmptr: NSComparator) -> Self     init(key key: String?, ascending ascending: Bool, comparator cmptr: NSComparator)     var comparator: NSComparator { get }     func compareObject(_ object1: AnyObject, toObject object2: AnyObject) -> NSComparisonResult     var reversedSortDescriptor: AnyObject { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NSSortDescriptor : NSObject, NSSecureCoding, NSCopying {     convenience init(key key: String?, ascending ascending: Bool)     class func sortDescriptorWithKey(_ key: String?, ascending ascending: Bool) -> Self     convenience init(key key: String?, ascending ascending: Bool, selector selector: Selector)     class func sortDescriptorWithKey(_ key: String?, ascending ascending: Bool, selector selector: Selector) -> Self     init(key key: String?, ascending ascending: Bool)     init(key key: String?, ascending ascending: Bool, selector selector: Selector)     init?(coder coder: NSCoder)     var key: String? { get }     var ascending: Bool { get }     var selector: Selector { get }     func allowEvaluation()     convenience init(key key: String?, ascending ascending: Bool, comparator cmptr: NSComparator)     class func sortDescriptorWithKey(_ key: String?, ascending ascending: Bool, comparator cmptr: NSComparator) -> Self     init(key key: String?, ascending ascending: Bool, comparator cmptr: NSComparator)     var comparator: NSComparator { get }     func compareObject(_ object1: AnyObject, toObject object2: AnyObject) -> NSComparisonResult     var reversedSortDescriptor: AnyObject { get } } ``` | NSCopying, NSSecureCoding |

Modified [NSStream](https://developer.apple.com/documentation/foundation/nsstream)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSStreamStatus [enum]](https://developer.apple.com/documentation/foundation/nsstreamstatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSString](https://developer.apple.com/documentation/foundation/nsstring)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSString : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     var length: Int { get }     func characterAtIndex(_ index: Int) -> unichar     init()     init?(coder aDecoder: NSCoder) } extension NSString : CNKeyDescriptor { } extension NSString {     func variantFittingPresentationWidth(_ width: Int) -> String } extension NSString {     func linguisticTagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, orthography orthography: NSOrthography?, tokenRanges tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [String]     func enumerateLinguisticTagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, orthography orthography: NSOrthography?, usingBlock block: (String, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) } extension NSString {     class func pathWithComponents(_ components: [String]) -> String     var pathComponents: [String] { get }     var absolutePath: Bool { get }     var lastPathComponent: String { get }     var stringByDeletingLastPathComponent: String { get }     func stringByAppendingPathComponent(_ str: String) -> String     var pathExtension: String { get }     var stringByDeletingPathExtension: String { get }     func stringByAppendingPathExtension(_ str: String) -> String?     var stringByAbbreviatingWithTildeInPath: String { get }     var stringByExpandingTildeInPath: String { get }     var stringByStandardizingPath: String { get }     var stringByResolvingSymlinksInPath: String { get }     func stringsByAppendingPaths(_ paths: [String]) -> [String]     func completePathIntoString(_ outputName: AutoreleasingUnsafeMutablePointer<NSString?>, caseSensitive flag: Bool, matchesIntoArray outputArray: AutoreleasingUnsafeMutablePointer<NSArray?>, filterTypes filterTypes: [String]?) -> Int     var fileSystemRepresentation: UnsafePointer<Int8> { get }     func getFileSystemRepresentation(_ cname: UnsafeMutablePointer<Int8>, maxLength max: Int) -> Bool } extension NSString : StringLiteralConvertible, ExtendedGraphemeClusterLiteralConvertible, UnicodeScalarLiteralConvertible {     required convenience init(unicodeScalarLiteral value: StaticString)     required convenience init(extendedGraphemeClusterLiteral value: StaticString)     required convenience init(stringLiteral value: StaticString) } extension NSString : _CocoaStringType { } extension NSString {     convenience init(format format: NSString, _ args: CVarArgType...)     convenience init(format format: NSString, locale locale: NSLocale?, _ args: CVarArgType...)     @warn_unused_result     class func localizedStringWithFormat(_ format: NSString, _ args: CVarArgType...) -> Self     @warn_unused_result     func stringByAppendingFormat(_ format: NSString, _ args: CVarArgType...) -> NSString } extension NSString {     @objc(_swiftInitWithString_NSString:) convenience init(string aString: NSString) } extension NSString : _Reflectable { } extension NSString {     func substringFromIndex(_ from: Int) -> String     func substringToIndex(_ to: Int) -> String     func substringWithRange(_ range: NSRange) -> String     func getCharacters(_ buffer: UnsafeMutablePointer<unichar>, range range: NSRange)     func compare(_ string: String) -> NSComparisonResult     func compare(_ string: String, options mask: NSStringCompareOptions) -> NSComparisonResult     func compare(_ string: String, options mask: NSStringCompareOptions, range compareRange: NSRange) -> NSComparisonResult     func compare(_ string: String, options mask: NSStringCompareOptions, range compareRange: NSRange, locale locale: AnyObject?) -> NSComparisonResult     func caseInsensitiveCompare(_ string: String) -> NSComparisonResult     func localizedCompare(_ string: String) -> NSComparisonResult     func localizedCaseInsensitiveCompare(_ string: String) -> NSComparisonResult     func localizedStandardCompare(_ string: String) -> NSComparisonResult     func isEqualToString(_ aString: String) -> Bool     func hasPrefix(_ str: String) -> Bool     func hasSuffix(_ str: String) -> Bool     func commonPrefixWithString(_ str: String, options mask: NSStringCompareOptions) -> String     func containsString(_ str: String) -> Bool     func localizedCaseInsensitiveContainsString(_ str: String) -> Bool     func localizedStandardContainsString(_ str: String) -> Bool     func localizedStandardRangeOfString(_ str: String) -> NSRange     func rangeOfString(_ searchString: String) -> NSRange     func rangeOfString(_ searchString: String, options mask: NSStringCompareOptions) -> NSRange     func rangeOfString(_ searchString: String, options mask: NSStringCompareOptions, range searchRange: NSRange) -> NSRange     func rangeOfString(_ searchString: String, options mask: NSStringCompareOptions, range searchRange: NSRange, locale locale: NSLocale?) -> NSRange     func rangeOfCharacterFromSet(_ searchSet: NSCharacterSet) -> NSRange     func rangeOfCharacterFromSet(_ searchSet: NSCharacterSet, options mask: NSStringCompareOptions) -> NSRange     func rangeOfCharacterFromSet(_ searchSet: NSCharacterSet, options mask: NSStringCompareOptions, range searchRange: NSRange) -> NSRange     func rangeOfComposedCharacterSequenceAtIndex(_ index: Int) -> NSRange     func rangeOfComposedCharacterSequencesForRange(_ range: NSRange) -> NSRange     func stringByAppendingString(_ aString: String) -> String     var doubleValue: Double { get }     var floatValue: Float { get }     var intValue: Int32 { get }     var integerValue: Int { get }     var longLongValue: Int64 { get }     var boolValue: Bool { get }     var uppercaseString: String { get }     var lowercaseString: String { get }     var capitalizedString: String { get }     var localizedUppercaseString: String { get }     var localizedLowercaseString: String { get }     var localizedCapitalizedString: String { get }     func uppercaseStringWithLocale(_ locale: NSLocale?) -> String     func lowercaseStringWithLocale(_ locale: NSLocale?) -> String     func capitalizedStringWithLocale(_ locale: NSLocale?) -> String     func getLineStart(_ startPtr: UnsafeMutablePointer<Int>, end lineEndPtr: UnsafeMutablePointer<Int>, contentsEnd contentsEndPtr: UnsafeMutablePointer<Int>, forRange range: NSRange)     func lineRangeForRange(_ range: NSRange) -> NSRange     func getParagraphStart(_ startPtr: UnsafeMutablePointer<Int>, end parEndPtr: UnsafeMutablePointer<Int>, contentsEnd contentsEndPtr: UnsafeMutablePointer<Int>, forRange range: NSRange)     func paragraphRangeForRange(_ range: NSRange) -> NSRange     func enumerateSubstringsInRange(_ range: NSRange, options opts: NSStringEnumerationOptions, usingBlock block: (String?, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateLinesUsingBlock(_ block: (String, UnsafeMutablePointer<ObjCBool>) -> Void)     var UTF8String: UnsafePointer<Int8> { get }     var fastestEncoding: UInt { get }     var smallestEncoding: UInt { get }     func dataUsingEncoding(_ encoding: UInt, allowLossyConversion lossy: Bool) -> NSData?     func dataUsingEncoding(_ encoding: UInt) -> NSData?     func canBeConvertedToEncoding(_ encoding: UInt) -> Bool     func cStringUsingEncoding(_ encoding: UInt) -> UnsafePointer<Int8>     func getCString(_ buffer: UnsafeMutablePointer<Int8>, maxLength maxBufferCount: Int, encoding encoding: UInt) -> Bool     func getBytes(_ buffer: UnsafeMutablePointer<Void>, maxLength maxBufferCount: Int, usedLength usedBufferCount: UnsafeMutablePointer<Int>, encoding encoding: UInt, options options: NSStringEncodingConversionOptions, range range: NSRange, remainingRange leftover: NSRangePointer) -> Bool     func maximumLengthOfBytesUsingEncoding(_ enc: UInt) -> Int     func lengthOfBytesUsingEncoding(_ enc: UInt) -> Int     class func availableStringEncodings() -> UnsafePointer<UInt>     class func localizedNameOfStringEncoding(_ encoding: UInt) -> String     class func defaultCStringEncoding() -> UInt     var decomposedStringWithCanonicalMapping: String { get }     var precomposedStringWithCanonicalMapping: String { get }     var decomposedStringWithCompatibilityMapping: String { get }     var precomposedStringWithCompatibilityMapping: String { get }     func componentsSeparatedByString(_ separator: String) -> [String]     func componentsSeparatedByCharactersInSet(_ separator: NSCharacterSet) -> [String]     func stringByTrimmingCharactersInSet(_ set: NSCharacterSet) -> String     func stringByPaddingToLength(_ newLength: Int, withString padString: String, startingAtIndex padIndex: Int) -> String     func stringByFoldingWithOptions(_ options: NSStringCompareOptions, locale locale: NSLocale?) -> String     func stringByReplacingOccurrencesOfString(_ target: String, withString replacement: String, options options: NSStringCompareOptions, range searchRange: NSRange) -> String     func stringByReplacingOccurrencesOfString(_ target: String, withString replacement: String) -> String     func stringByReplacingCharactersInRange(_ range: NSRange, withString replacement: String) -> String     func stringByApplyingTransform(_ transform: String, reverse reverse: Bool) -> String?     func writeToURL(_ url: NSURL, atomically useAuxiliaryFile: Bool, encoding enc: UInt) throws     func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool, encoding enc: UInt) throws     var description: String { get }     var hash: Int { get }     convenience init(charactersNoCopy characters: UnsafeMutablePointer<unichar>, length length: Int, freeWhenDone freeBuffer: Bool)     convenience init(characters characters: UnsafePointer<unichar>, length length: Int)     convenience init?(UTF8String nullTerminatedCString: UnsafePointer<Int8>)     convenience init(string aString: String)     convenience init(format format: String, arguments argList: CVaListPointer)     convenience init(format format: String, locale locale: AnyObject?, arguments argList: CVaListPointer)     convenience init?(data data: NSData, encoding encoding: UInt)     convenience init?(bytes bytes: UnsafePointer<Void>, length len: Int, encoding encoding: UInt)     convenience init?(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length len: Int, encoding encoding: UInt, freeWhenDone freeBuffer: Bool)     class func string() -> Self     class func stringWithString(_ string: String) -> Self     class func stringWithCharacters(_ characters: UnsafePointer<unichar>, length length: Int) -> Self     class func stringWithUTF8String(_ nullTerminatedCString: UnsafePointer<Int8>) -> Self?     convenience init?(CString nullTerminatedCString: UnsafePointer<Int8>, encoding encoding: UInt)     class func stringWithCString(_ cString: UnsafePointer<Int8>, encoding enc: UInt) -> Self?     convenience init(contentsOfURL url: NSURL, encoding enc: UInt) throws     convenience init(contentsOfFile path: String, encoding enc: UInt) throws     class func stringWithContentsOfURL(_ url: NSURL, encoding enc: UInt) throws -> Self     class func stringWithContentsOfFile(_ path: String, encoding enc: UInt) throws -> Self     convenience init(contentsOfURL url: NSURL, usedEncoding enc: UnsafeMutablePointer<UInt>) throws     convenience init(contentsOfFile path: String, usedEncoding enc: UnsafeMutablePointer<UInt>) throws     class func stringWithContentsOfURL(_ url: NSURL, usedEncoding enc: UnsafeMutablePointer<UInt>) throws -> Self     class func stringWithContentsOfFile(_ path: String, usedEncoding enc: UnsafeMutablePointer<UInt>) throws -> Self } extension NSString {     class func stringEncodingForData(_ data: NSData, encodingOptions opts: [String : AnyObject]?, convertedString string: AutoreleasingUnsafeMutablePointer<NSString?>, usedLossyConversion usedLossyConversion: UnsafeMutablePointer<ObjCBool>) -> UInt } extension NSString {     func propertyList() -> AnyObject     func propertyListFromStringsFileFormat() -> [NSObject : AnyObject]? } extension NSString {     func cString() -> UnsafePointer<Int8>     func lossyCString() -> UnsafePointer<Int8>     func cStringLength() -> Int     func getCString(_ bytes: UnsafeMutablePointer<Int8>)     func getCString(_ bytes: UnsafeMutablePointer<Int8>, maxLength maxLength: Int)     func getCString(_ bytes: UnsafeMutablePointer<Int8>, maxLength maxLength: Int, range aRange: NSRange, remainingRange leftoverRange: NSRangePointer)     func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool) -> Bool     func writeToURL(_ url: NSURL, atomically atomically: Bool) -> Bool     convenience init?(contentsOfFile path: String)     convenience init?(contentsOfURL url: NSURL)     class func stringWithContentsOfFile(_ path: String) -> AnyObject?     class func stringWithContentsOfURL(_ url: NSURL) -> AnyObject?     convenience init?(CStringNoCopy bytes: UnsafeMutablePointer<Int8>, length length: Int, freeWhenDone freeBuffer: Bool)     convenience init?(CString bytes: UnsafePointer<Int8>, length length: Int)     convenience init?(CString bytes: UnsafePointer<Int8>)     class func stringWithCString(_ bytes: UnsafePointer<Int8>, length length: Int) -> AnyObject?     class func stringWithCString(_ bytes: UnsafePointer<Int8>) -> AnyObject?     func getCharacters(_ buffer: UnsafeMutablePointer<unichar>) } extension NSString {     func stringByAddingPercentEncodingWithAllowedCharacters(_ allowedCharacters: NSCharacterSet) -> String?     var stringByRemovingPercentEncoding: String? { get }     func stringByAddingPercentEscapesUsingEncoding(_ enc: UInt) -> String?     func stringByReplacingPercentEscapesUsingEncoding(_ enc: UInt) -> String? } extension NSString : _Reflectable { } extension NSString {     @objc(_swiftInitWithString_NSString:) convenience init(string aString: NSString) } extension NSString {     convenience init(format format: NSString, _ args: CVarArgType...)     convenience init(format format: NSString, locale locale: NSLocale?, _ args: CVarArgType...)     @warn_unused_result     class func localizedStringWithFormat(_ format: NSString, _ args: CVarArgType...) -> Self     @warn_unused_result     func stringByAppendingFormat(_ format: NSString, _ args: CVarArgType...) -> NSString } extension NSString : _CocoaStringType { } extension NSString : StringLiteralConvertible, ExtendedGraphemeClusterLiteralConvertible, UnicodeScalarLiteralConvertible {     required convenience init(unicodeScalarLiteral value: StaticString)     required convenience init(extendedGraphemeClusterLiteral value: StaticString)     required convenience init(stringLiteral value: StaticString) } extension NSString {     func sizeWithAttributes(_ attrs: [String : AnyObject]?) -> CGSize     func drawAtPoint(_ point: CGPoint, withAttributes attrs: [String : AnyObject]?)     func drawInRect(_ rect: CGRect, withAttributes attrs: [String : AnyObject]?) } extension NSString {     func drawWithRect(_ rect: CGRect, options options: NSStringDrawingOptions, attributes attributes: [String : AnyObject]?, context context: NSStringDrawingContext?)     func boundingRectWithSize(_ size: CGSize, options options: NSStringDrawingOptions, attributes attributes: [String : AnyObject]?, context context: NSStringDrawingContext?) -> CGRect } ``` | AnyObject, CNKeyDescriptor, ExtendedGraphemeClusterLiteralConvertible, NSCoding, NSCopying, NSMutableCopying, NSObjectProtocol, NSSecureCoding, StringLiteralConvertible, UnicodeScalarLiteralConvertible |
| To | ``` class NSString : NSObject, NSCopying, NSMutableCopying, NSSecureCoding {     var length: Int { get }     func characterAtIndex(_ index: Int) -> unichar     init()     init?(coder aDecoder: NSCoder) } extension NSString : CNKeyDescriptor { } extension NSString {     func variantFittingPresentationWidth(_ width: Int) -> String } extension NSString {     func linguisticTagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, orthography orthography: NSOrthography?, tokenRanges tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [String]     func enumerateLinguisticTagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, orthography orthography: NSOrthography?, usingBlock block: (String, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) } extension NSString {     class func pathWithComponents(_ components: [String]) -> String     var pathComponents: [String] { get }     var absolutePath: Bool { get }     var lastPathComponent: String { get }     var stringByDeletingLastPathComponent: String { get }     func stringByAppendingPathComponent(_ str: String) -> String     var pathExtension: String { get }     var stringByDeletingPathExtension: String { get }     func stringByAppendingPathExtension(_ str: String) -> String?     var stringByAbbreviatingWithTildeInPath: String { get }     var stringByExpandingTildeInPath: String { get }     var stringByStandardizingPath: String { get }     var stringByResolvingSymlinksInPath: String { get }     func stringsByAppendingPaths(_ paths: [String]) -> [String]     func completePathIntoString(_ outputName: AutoreleasingUnsafeMutablePointer<NSString?>, caseSensitive flag: Bool, matchesIntoArray outputArray: AutoreleasingUnsafeMutablePointer<NSArray?>, filterTypes filterTypes: [String]?) -> Int     var fileSystemRepresentation: UnsafePointer<Int8> { get }     func getFileSystemRepresentation(_ cname: UnsafeMutablePointer<Int8>, maxLength max: Int) -> Bool } extension NSString : StringLiteralConvertible {     required convenience init(unicodeScalarLiteral value: StaticString)     required convenience init(extendedGraphemeClusterLiteral value: StaticString)     required convenience init(stringLiteral value: StaticString) } extension NSString : _CocoaStringType { } extension NSString {     convenience init(format format: NSString, _ args: CVarArgType...)     convenience init(format format: NSString, locale locale: NSLocale?, _ args: CVarArgType...)     @warn_unused_result     class func localizedStringWithFormat(_ format: NSString, _ args: CVarArgType...) -> Self     @warn_unused_result     func stringByAppendingFormat(_ format: NSString, _ args: CVarArgType...) -> NSString } extension NSString {     @objc(_swiftInitWithString_NSString:) convenience init(string aString: NSString) } extension NSString : _Reflectable { } extension NSString {     func substringFromIndex(_ from: Int) -> String     func substringToIndex(_ to: Int) -> String     func substringWithRange(_ range: NSRange) -> String     func getCharacters(_ buffer: UnsafeMutablePointer<unichar>, range range: NSRange)     func compare(_ string: String) -> NSComparisonResult     func compare(_ string: String, options mask: NSStringCompareOptions) -> NSComparisonResult     func compare(_ string: String, options mask: NSStringCompareOptions, range compareRange: NSRange) -> NSComparisonResult     func compare(_ string: String, options mask: NSStringCompareOptions, range compareRange: NSRange, locale locale: AnyObject?) -> NSComparisonResult     func caseInsensitiveCompare(_ string: String) -> NSComparisonResult     func localizedCompare(_ string: String) -> NSComparisonResult     func localizedCaseInsensitiveCompare(_ string: String) -> NSComparisonResult     func localizedStandardCompare(_ string: String) -> NSComparisonResult     func isEqualToString(_ aString: String) -> Bool     func hasPrefix(_ str: String) -> Bool     func hasSuffix(_ str: String) -> Bool     func commonPrefixWithString(_ str: String, options mask: NSStringCompareOptions) -> String     func containsString(_ str: String) -> Bool     func localizedCaseInsensitiveContainsString(_ str: String) -> Bool     func localizedStandardContainsString(_ str: String) -> Bool     func localizedStandardRangeOfString(_ str: String) -> NSRange     func rangeOfString(_ searchString: String) -> NSRange     func rangeOfString(_ searchString: String, options mask: NSStringCompareOptions) -> NSRange     func rangeOfString(_ searchString: String, options mask: NSStringCompareOptions, range searchRange: NSRange) -> NSRange     func rangeOfString(_ searchString: String, options mask: NSStringCompareOptions, range searchRange: NSRange, locale locale: NSLocale?) -> NSRange     func rangeOfCharacterFromSet(_ searchSet: NSCharacterSet) -> NSRange     func rangeOfCharacterFromSet(_ searchSet: NSCharacterSet, options mask: NSStringCompareOptions) -> NSRange     func rangeOfCharacterFromSet(_ searchSet: NSCharacterSet, options mask: NSStringCompareOptions, range searchRange: NSRange) -> NSRange     func rangeOfComposedCharacterSequenceAtIndex(_ index: Int) -> NSRange     func rangeOfComposedCharacterSequencesForRange(_ range: NSRange) -> NSRange     func stringByAppendingString(_ aString: String) -> String     var doubleValue: Double { get }     var floatValue: Float { get }     var intValue: Int32 { get }     var integerValue: Int { get }     var longLongValue: Int64 { get }     var boolValue: Bool { get }     var uppercaseString: String { get }     var lowercaseString: String { get }     var capitalizedString: String { get }     var localizedUppercaseString: String { get }     var localizedLowercaseString: String { get }     var localizedCapitalizedString: String { get }     func uppercaseStringWithLocale(_ locale: NSLocale?) -> String     func lowercaseStringWithLocale(_ locale: NSLocale?) -> String     func capitalizedStringWithLocale(_ locale: NSLocale?) -> String     func getLineStart(_ startPtr: UnsafeMutablePointer<Int>, end lineEndPtr: UnsafeMutablePointer<Int>, contentsEnd contentsEndPtr: UnsafeMutablePointer<Int>, forRange range: NSRange)     func lineRangeForRange(_ range: NSRange) -> NSRange     func getParagraphStart(_ startPtr: UnsafeMutablePointer<Int>, end parEndPtr: UnsafeMutablePointer<Int>, contentsEnd contentsEndPtr: UnsafeMutablePointer<Int>, forRange range: NSRange)     func paragraphRangeForRange(_ range: NSRange) -> NSRange     func enumerateSubstringsInRange(_ range: NSRange, options opts: NSStringEnumerationOptions, usingBlock block: (String?, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateLinesUsingBlock(_ block: (String, UnsafeMutablePointer<ObjCBool>) -> Void)     var UTF8String: UnsafePointer<Int8> { get }     var fastestEncoding: UInt { get }     var smallestEncoding: UInt { get }     func dataUsingEncoding(_ encoding: UInt, allowLossyConversion lossy: Bool) -> NSData?     func dataUsingEncoding(_ encoding: UInt) -> NSData?     func canBeConvertedToEncoding(_ encoding: UInt) -> Bool     func cStringUsingEncoding(_ encoding: UInt) -> UnsafePointer<Int8>     func getCString(_ buffer: UnsafeMutablePointer<Int8>, maxLength maxBufferCount: Int, encoding encoding: UInt) -> Bool     func getBytes(_ buffer: UnsafeMutablePointer<Void>, maxLength maxBufferCount: Int, usedLength usedBufferCount: UnsafeMutablePointer<Int>, encoding encoding: UInt, options options: NSStringEncodingConversionOptions, range range: NSRange, remainingRange leftover: NSRangePointer) -> Bool     func maximumLengthOfBytesUsingEncoding(_ enc: UInt) -> Int     func lengthOfBytesUsingEncoding(_ enc: UInt) -> Int     class func availableStringEncodings() -> UnsafePointer<UInt>     class func localizedNameOfStringEncoding(_ encoding: UInt) -> String     class func defaultCStringEncoding() -> UInt     var decomposedStringWithCanonicalMapping: String { get }     var precomposedStringWithCanonicalMapping: String { get }     var decomposedStringWithCompatibilityMapping: String { get }     var precomposedStringWithCompatibilityMapping: String { get }     func componentsSeparatedByString(_ separator: String) -> [String]     func componentsSeparatedByCharactersInSet(_ separator: NSCharacterSet) -> [String]     func stringByTrimmingCharactersInSet(_ set: NSCharacterSet) -> String     func stringByPaddingToLength(_ newLength: Int, withString padString: String, startingAtIndex padIndex: Int) -> String     func stringByFoldingWithOptions(_ options: NSStringCompareOptions, locale locale: NSLocale?) -> String     func stringByReplacingOccurrencesOfString(_ target: String, withString replacement: String, options options: NSStringCompareOptions, range searchRange: NSRange) -> String     func stringByReplacingOccurrencesOfString(_ target: String, withString replacement: String) -> String     func stringByReplacingCharactersInRange(_ range: NSRange, withString replacement: String) -> String     func stringByApplyingTransform(_ transform: String, reverse reverse: Bool) -> String?     func writeToURL(_ url: NSURL, atomically useAuxiliaryFile: Bool, encoding enc: UInt) throws     func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool, encoding enc: UInt) throws     var description: String { get }     var hash: Int { get }     convenience init(charactersNoCopy characters: UnsafeMutablePointer<unichar>, length length: Int, freeWhenDone freeBuffer: Bool)     convenience init(characters characters: UnsafePointer<unichar>, length length: Int)     convenience init?(UTF8String nullTerminatedCString: UnsafePointer<Int8>)     convenience init(string aString: String)     convenience init(format format: String, arguments argList: CVaListPointer)     convenience init(format format: String, locale locale: AnyObject?, arguments argList: CVaListPointer)     convenience init?(data data: NSData, encoding encoding: UInt)     convenience init?(bytes bytes: UnsafePointer<Void>, length len: Int, encoding encoding: UInt)     convenience init?(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length len: Int, encoding encoding: UInt, freeWhenDone freeBuffer: Bool)     class func string() -> Self     class func stringWithString(_ string: String) -> Self     class func stringWithCharacters(_ characters: UnsafePointer<unichar>, length length: Int) -> Self     class func stringWithUTF8String(_ nullTerminatedCString: UnsafePointer<Int8>) -> Self?     convenience init?(CString nullTerminatedCString: UnsafePointer<Int8>, encoding encoding: UInt)     class func stringWithCString(_ cString: UnsafePointer<Int8>, encoding enc: UInt) -> Self?     convenience init(contentsOfURL url: NSURL, encoding enc: UInt) throws     convenience init(contentsOfFile path: String, encoding enc: UInt) throws     class func stringWithContentsOfURL(_ url: NSURL, encoding enc: UInt) throws -> Self     class func stringWithContentsOfFile(_ path: String, encoding enc: UInt) throws -> Self     convenience init(contentsOfURL url: NSURL, usedEncoding enc: UnsafeMutablePointer<UInt>) throws     convenience init(contentsOfFile path: String, usedEncoding enc: UnsafeMutablePointer<UInt>) throws     class func stringWithContentsOfURL(_ url: NSURL, usedEncoding enc: UnsafeMutablePointer<UInt>) throws -> Self     class func stringWithContentsOfFile(_ path: String, usedEncoding enc: UnsafeMutablePointer<UInt>) throws -> Self } extension NSString {     class func stringEncodingForData(_ data: NSData, encodingOptions opts: [String : AnyObject]?, convertedString string: AutoreleasingUnsafeMutablePointer<NSString?>, usedLossyConversion usedLossyConversion: UnsafeMutablePointer<ObjCBool>) -> UInt } extension NSString {     func propertyList() -> AnyObject     func propertyListFromStringsFileFormat() -> [NSObject : AnyObject]? } extension NSString {     func cString() -> UnsafePointer<Int8>     func lossyCString() -> UnsafePointer<Int8>     func cStringLength() -> Int     func getCString(_ bytes: UnsafeMutablePointer<Int8>)     func getCString(_ bytes: UnsafeMutablePointer<Int8>, maxLength maxLength: Int)     func getCString(_ bytes: UnsafeMutablePointer<Int8>, maxLength maxLength: Int, range aRange: NSRange, remainingRange leftoverRange: NSRangePointer)     func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool) -> Bool     func writeToURL(_ url: NSURL, atomically atomically: Bool) -> Bool     convenience init?(contentsOfFile path: String)     convenience init?(contentsOfURL url: NSURL)     class func stringWithContentsOfFile(_ path: String) -> AnyObject?     class func stringWithContentsOfURL(_ url: NSURL) -> AnyObject?     convenience init?(CStringNoCopy bytes: UnsafeMutablePointer<Int8>, length length: Int, freeWhenDone freeBuffer: Bool)     convenience init?(CString bytes: UnsafePointer<Int8>, length length: Int)     convenience init?(CString bytes: UnsafePointer<Int8>)     class func stringWithCString(_ bytes: UnsafePointer<Int8>, length length: Int) -> AnyObject?     class func stringWithCString(_ bytes: UnsafePointer<Int8>) -> AnyObject?     func getCharacters(_ buffer: UnsafeMutablePointer<unichar>) } extension NSString {     func stringByAddingPercentEncodingWithAllowedCharacters(_ allowedCharacters: NSCharacterSet) -> String?     var stringByRemovingPercentEncoding: String? { get }     func stringByAddingPercentEscapesUsingEncoding(_ enc: UInt) -> String?     func stringByReplacingPercentEscapesUsingEncoding(_ enc: UInt) -> String? } extension NSString : _Reflectable { } extension NSString {     @objc(_swiftInitWithString_NSString:) convenience init(string aString: NSString) } extension NSString {     convenience init(format format: NSString, _ args: CVarArgType...)     convenience init(format format: NSString, locale locale: NSLocale?, _ args: CVarArgType...)     @warn_unused_result     class func localizedStringWithFormat(_ format: NSString, _ args: CVarArgType...) -> Self     @warn_unused_result     func stringByAppendingFormat(_ format: NSString, _ args: CVarArgType...) -> NSString } extension NSString : _CocoaStringType { } extension NSString : StringLiteralConvertible {     required convenience init(unicodeScalarLiteral value: StaticString)     required convenience init(extendedGraphemeClusterLiteral value: StaticString)     required convenience init(stringLiteral value: StaticString) } extension NSString {     func sizeWithAttributes(_ attrs: [String : AnyObject]?) -> CGSize     func drawAtPoint(_ point: CGPoint, withAttributes attrs: [String : AnyObject]?)     func drawInRect(_ rect: CGRect, withAttributes attrs: [String : AnyObject]?) } extension NSString {     func drawWithRect(_ rect: CGRect, options options: NSStringDrawingOptions, attributes attributes: [String : AnyObject]?, context context: NSStringDrawingContext?)     func boundingRectWithSize(_ size: CGSize, options options: NSStringDrawingOptions, attributes attributes: [String : AnyObject]?, context context: NSStringDrawingContext?) -> CGRect } ``` | CNKeyDescriptor, NSCopying, NSMutableCopying, NSSecureCoding, StringLiteralConvertible |

Modified [NSTextCheckingResult](https://developer.apple.com/documentation/foundation/nstextcheckingresult)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [NSThread](https://developer.apple.com/documentation/foundation/thread)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSTimer](https://developer.apple.com/documentation/foundation/timer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSTimeZone](https://developer.apple.com/documentation/foundation/nstimezone)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSTimeZone : NSObject, NSCopying, NSSecureCoding, NSCoding {     var name: String { get }     @NSCopying var data: NSData { get }     func secondsFromGMTForDate(_ aDate: NSDate) -> Int     func abbreviationForDate(_ aDate: NSDate) -> String?     func isDaylightSavingTimeForDate(_ aDate: NSDate) -> Bool     func daylightSavingTimeOffsetForDate(_ aDate: NSDate) -> NSTimeInterval     func nextDaylightSavingTimeTransitionAfterDate(_ aDate: NSDate) -> NSDate? } extension NSTimeZone {     class func systemTimeZone() -> NSTimeZone     class func resetSystemTimeZone()     class func defaultTimeZone() -> NSTimeZone     class func setDefaultTimeZone(_ aTimeZone: NSTimeZone)     class func localTimeZone() -> NSTimeZone     class func knownTimeZoneNames() -> [String]     class func abbreviationDictionary() -> [String : String]     class func setAbbreviationDictionary(_ dict: [String : String])     class func timeZoneDataVersion() -> String     var secondsFromGMT: Int { get }     var abbreviation: String? { get }     var daylightSavingTime: Bool { get }     var daylightSavingTimeOffset: NSTimeInterval { get }     @NSCopying var nextDaylightSavingTimeTransition: NSDate? { get }     var description: String { get }     func isEqualToTimeZone(_ aTimeZone: NSTimeZone) -> Bool     func localizedName(_ style: NSTimeZoneNameStyle, locale locale: NSLocale?) -> String? } extension NSTimeZone {     convenience init?(name tzName: String)     class func timeZoneWithName(_ tzName: String) -> Self?     convenience init?(name tzName: String, data aData: NSData?)     class func timeZoneWithName(_ tzName: String, data aData: NSData?) -> Self?     init?(name tzName: String)     init?(name tzName: String, data aData: NSData?)     convenience init(forSecondsFromGMT seconds: Int)     class func timeZoneForSecondsFromGMT(_ seconds: Int) -> Self     convenience init?(abbreviation abbreviation: String)     class func timeZoneWithAbbreviation(_ abbreviation: String) -> Self? } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NSTimeZone : NSObject, NSCopying, NSSecureCoding {     var name: String { get }     @NSCopying var data: NSData { get }     func secondsFromGMTForDate(_ aDate: NSDate) -> Int     func abbreviationForDate(_ aDate: NSDate) -> String?     func isDaylightSavingTimeForDate(_ aDate: NSDate) -> Bool     func daylightSavingTimeOffsetForDate(_ aDate: NSDate) -> NSTimeInterval     func nextDaylightSavingTimeTransitionAfterDate(_ aDate: NSDate) -> NSDate? } extension NSTimeZone {     class func systemTimeZone() -> NSTimeZone     class func resetSystemTimeZone()     class func defaultTimeZone() -> NSTimeZone     class func setDefaultTimeZone(_ aTimeZone: NSTimeZone)     class func localTimeZone() -> NSTimeZone     class func knownTimeZoneNames() -> [String]     class func abbreviationDictionary() -> [String : String]     class func setAbbreviationDictionary(_ dict: [String : String])     class func timeZoneDataVersion() -> String     var secondsFromGMT: Int { get }     var abbreviation: String? { get }     var daylightSavingTime: Bool { get }     var daylightSavingTimeOffset: NSTimeInterval { get }     @NSCopying var nextDaylightSavingTimeTransition: NSDate? { get }     var description: String { get }     func isEqualToTimeZone(_ aTimeZone: NSTimeZone) -> Bool     func localizedName(_ style: NSTimeZoneNameStyle, locale locale: NSLocale?) -> String? } extension NSTimeZone {     convenience init?(name tzName: String)     class func timeZoneWithName(_ tzName: String) -> Self?     convenience init?(name tzName: String, data aData: NSData?)     class func timeZoneWithName(_ tzName: String, data aData: NSData?) -> Self?     init?(name tzName: String)     init?(name tzName: String, data aData: NSData?)     convenience init(forSecondsFromGMT seconds: Int)     class func timeZoneForSecondsFromGMT(_ seconds: Int) -> Self     convenience init?(abbreviation abbreviation: String)     class func timeZoneWithAbbreviation(_ abbreviation: String) -> Self? } ``` | NSCopying, NSSecureCoding |

Modified [NSTimeZoneNameStyle [enum]](https://developer.apple.com/documentation/foundation/nstimezone/namestyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSUbiquitousKeyValueStore](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSUndoManager](https://developer.apple.com/documentation/foundation/nsundomanager)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSUndoManager : NSObject {     func beginUndoGrouping()     func endUndoGrouping()     var groupingLevel: Int { get }     func disableUndoRegistration()     func enableUndoRegistration()     var undoRegistrationEnabled: Bool { get }     var groupsByEvent: Bool     var levelsOfUndo: Int     var runLoopModes: [String]     func undo()     func redo()     func undoNestedGroup()     var canUndo: Bool { get }     var canRedo: Bool { get }     var undoing: Bool { get }     var redoing: Bool { get }     func removeAllActions()     func removeAllActionsWithTarget(_ target: AnyObject)     func registerUndoWithTarget(_ target: AnyObject, selector selector: Selector, object anObject: AnyObject?)     func prepareWithInvocationTarget(_ target: AnyObject) -> AnyObject     func __registerUndoWithTarget(_ target: AnyObject, handler undoHandler: (AnyObject) -> Void)     func setActionIsDiscardable(_ discardable: Bool)     var undoActionIsDiscardable: Bool { get }     var redoActionIsDiscardable: Bool { get }     var undoActionName: String { get }     var redoActionName: String { get }     func setActionName(_ actionName: String)     var undoMenuItemTitle: String { get }     var redoMenuItemTitle: String { get }     func undoMenuTitleForUndoActionName(_ actionName: String) -> String     func redoMenuTitleForUndoActionName(_ actionName: String) -> String } extension NSUndoManager {     func registerUndoWithTarget<TargetType>(_ target: TargetType, handler handler: TargetType -> ()) } extension NSUndoManager {     func registerUndoWithTarget<TargetType>(_ target: TargetType, handler handler: TargetType -> ()) } ``` | AnyObject |
| To | ``` class NSUndoManager : NSObject {     func beginUndoGrouping()     func endUndoGrouping()     var groupingLevel: Int { get }     func disableUndoRegistration()     func enableUndoRegistration()     var undoRegistrationEnabled: Bool { get }     var groupsByEvent: Bool     var levelsOfUndo: Int     var runLoopModes: [String]     func undo()     func redo()     func undoNestedGroup()     var canUndo: Bool { get }     var canRedo: Bool { get }     var undoing: Bool { get }     var redoing: Bool { get }     func removeAllActions()     func removeAllActionsWithTarget(_ target: AnyObject)     func registerUndoWithTarget(_ target: AnyObject, selector selector: Selector, object anObject: AnyObject?)     func prepareWithInvocationTarget(_ target: AnyObject) -> AnyObject     func __registerUndoWithTarget(_ target: AnyObject, handler undoHandler: (AnyObject) -> Void)     func setActionIsDiscardable(_ discardable: Bool)     var undoActionIsDiscardable: Bool { get }     var redoActionIsDiscardable: Bool { get }     var undoActionName: String { get }     var redoActionName: String { get }     func setActionName(_ actionName: String)     var undoMenuItemTitle: String { get }     var redoMenuItemTitle: String { get }     func undoMenuTitleForUndoActionName(_ actionName: String) -> String     func redoMenuTitleForUndoActionName(_ actionName: String) -> String } extension NSUndoManager {     func registerUndoWithTarget<TargetType : AnyObject>(_ target: TargetType, handler handler: TargetType -> ()) } extension NSUndoManager {     func registerUndoWithTarget<TargetType : AnyObject>(_ target: TargetType, handler handler: TargetType -> ()) } ``` | -- |

Modified NSUndoManager.registerUndoWithTarget<TargetType : AnyObject>(_: TargetType, handler: TargetType -> ())

|  | Declaration |
| --- | --- |
| From | ``` func registerUndoWithTarget<TargetType>(_ target: TargetType, handler handler: TargetType -> ()) ``` |
| To | ``` func registerUndoWithTarget<TargetType : AnyObject>(_ target: TargetType, handler handler: TargetType -> ()) ``` |

Modified [NSURL](https://developer.apple.com/documentation/foundation/nsurl)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSURL : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init?(scheme scheme: String, host host: String?, path path: String)     init(fileURLWithPath path: String, isDirectory isDir: Bool, relativeToURL baseURL: NSURL?)     init(fileURLWithPath path: String, relativeToURL baseURL: NSURL?)     init(fileURLWithPath path: String, isDirectory isDir: Bool)     init(fileURLWithPath path: String)     class func fileURLWithPath(_ path: String, isDirectory isDir: Bool, relativeToURL baseURL: NSURL?) -> NSURL     class func fileURLWithPath(_ path: String, relativeToURL baseURL: NSURL?) -> NSURL     class func fileURLWithPath(_ path: String, isDirectory isDir: Bool) -> NSURL     class func fileURLWithPath(_ path: String) -> NSURL     init(fileURLWithFileSystemRepresentation path: UnsafePointer<Int8>, isDirectory isDir: Bool, relativeToURL baseURL: NSURL?)     class func fileURLWithFileSystemRepresentation(_ path: UnsafePointer<Int8>, isDirectory isDir: Bool, relativeToURL baseURL: NSURL?) -> NSURL     convenience init?(string URLString: String)     init?(string URLString: String, relativeToURL baseURL: NSURL?)     class func URLWithString(_ URLString: String) -> Self?     class func URLWithString(_ URLString: String, relativeToURL baseURL: NSURL?) -> Self?     init(dataRepresentation data: NSData, relativeToURL baseURL: NSURL?)     class func URLWithDataRepresentation(_ data: NSData, relativeToURL baseURL: NSURL?) -> NSURL     init(absoluteURLWithDataRepresentation data: NSData, relativeToURL baseURL: NSURL?)     class func absoluteURLWithDataRepresentation(_ data: NSData, relativeToURL baseURL: NSURL?) -> NSURL     @NSCopying var dataRepresentation: NSData { get }     var absoluteString: String { get }     var relativeString: String? { get }     @NSCopying var baseURL: NSURL? { get }     @NSCopying var absoluteURL: NSURL { get }     var scheme: String { get }     var resourceSpecifier: String { get }     var host: String? { get }     @NSCopying var port: NSNumber? { get }     var user: String? { get }     var password: String? { get }     var path: String? { get }     var fragment: String? { get }     var parameterString: String? { get }     var query: String? { get }     var relativePath: String? { get }     var hasDirectoryPath: Bool { get }     func getFileSystemRepresentation(_ buffer: UnsafeMutablePointer<Int8>, maxLength maxBufferLength: Int) -> Bool     var fileSystemRepresentation: UnsafePointer<Int8> { get }     var fileURL: Bool { get }     @NSCopying var standardizedURL: NSURL? { get }     func checkResourceIsReachableAndReturnError(_ error: NSErrorPointer) -> Bool     func isFileReferenceURL() -> Bool     func fileReferenceURL() -> NSURL?     @NSCopying var filePathURL: NSURL? { get }     func getResourceValue(_ value: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey key: String) throws     func resourceValuesForKeys(_ keys: [String]) throws -> [String : AnyObject]     func setResourceValue(_ value: AnyObject?, forKey key: String) throws     func setResourceValues(_ keyedValues: [String : AnyObject]) throws     func removeCachedResourceValueForKey(_ key: String)     func removeAllCachedResourceValues()     func setTemporaryResourceValue(_ value: AnyObject?, forKey key: String)     func bookmarkDataWithOptions(_ options: NSURLBookmarkCreationOptions, includingResourceValuesForKeys keys: [String]?, relativeToURL relativeURL: NSURL?) throws -> NSData     convenience init(byResolvingBookmarkData bookmarkData: NSData, options options: NSURLBookmarkResolutionOptions, relativeToURL relativeURL: NSURL?, bookmarkDataIsStale isStale: UnsafeMutablePointer<ObjCBool>) throws     class func URLByResolvingBookmarkData(_ bookmarkData: NSData, options options: NSURLBookmarkResolutionOptions, relativeToURL relativeURL: NSURL?, bookmarkDataIsStale isStale: UnsafeMutablePointer<ObjCBool>) throws -> Self     class func resourceValuesForKeys(_ keys: [String], fromBookmarkData bookmarkData: NSData) -> [String : AnyObject]?     class func writeBookmarkData(_ bookmarkData: NSData, toURL bookmarkFileURL: NSURL, options options: NSURLBookmarkFileCreationOptions) throws     class func bookmarkDataWithContentsOfURL(_ bookmarkFileURL: NSURL) throws -> NSData     convenience init(byResolvingAliasFileAtURL url: NSURL, options options: NSURLBookmarkResolutionOptions) throws     class func URLByResolvingAliasFileAtURL(_ url: NSURL, options options: NSURLBookmarkResolutionOptions) throws -> Self     func startAccessingSecurityScopedResource() -> Bool     func stopAccessingSecurityScopedResource() } extension NSURL : _Reflectable { } extension NSURL {     func getPromisedItemResourceValue(_ value: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey key: String) throws     func promisedItemResourceValuesForKeys(_ keys: [String]) throws -> [String : AnyObject]     func checkPromisedItemIsReachableAndReturnError(_ error: NSErrorPointer) -> Bool } extension NSURL {     class func fileURLWithPathComponents(_ components: [String]) -> NSURL?     var pathComponents: [String]? { get }     var lastPathComponent: String? { get }     var pathExtension: String? { get }     func URLByAppendingPathComponent(_ pathComponent: String) -> NSURL     func URLByAppendingPathComponent(_ pathComponent: String, isDirectory isDirectory: Bool) -> NSURL     @NSCopying var URLByDeletingLastPathComponent: NSURL? { get }     func URLByAppendingPathExtension(_ pathExtension: String) -> NSURL     @NSCopying var URLByDeletingPathExtension: NSURL? { get }     @NSCopying var URLByStandardizingPath: NSURL? { get }     @NSCopying var URLByResolvingSymlinksInPath: NSURL? { get } } extension NSURL : _Reflectable { } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NSURL : NSObject, NSSecureCoding, NSCopying {     convenience init?(scheme scheme: String, host host: String?, path path: String)     init(fileURLWithPath path: String, isDirectory isDir: Bool, relativeToURL baseURL: NSURL?)     init(fileURLWithPath path: String, relativeToURL baseURL: NSURL?)     init(fileURLWithPath path: String, isDirectory isDir: Bool)     init(fileURLWithPath path: String)     class func fileURLWithPath(_ path: String, isDirectory isDir: Bool, relativeToURL baseURL: NSURL?) -> NSURL     class func fileURLWithPath(_ path: String, relativeToURL baseURL: NSURL?) -> NSURL     class func fileURLWithPath(_ path: String, isDirectory isDir: Bool) -> NSURL     class func fileURLWithPath(_ path: String) -> NSURL     init(fileURLWithFileSystemRepresentation path: UnsafePointer<Int8>, isDirectory isDir: Bool, relativeToURL baseURL: NSURL?)     class func fileURLWithFileSystemRepresentation(_ path: UnsafePointer<Int8>, isDirectory isDir: Bool, relativeToURL baseURL: NSURL?) -> NSURL     convenience init?(string URLString: String)     init?(string URLString: String, relativeToURL baseURL: NSURL?)     class func URLWithString(_ URLString: String) -> Self?     class func URLWithString(_ URLString: String, relativeToURL baseURL: NSURL?) -> Self?     init(dataRepresentation data: NSData, relativeToURL baseURL: NSURL?)     class func URLWithDataRepresentation(_ data: NSData, relativeToURL baseURL: NSURL?) -> NSURL     init(absoluteURLWithDataRepresentation data: NSData, relativeToURL baseURL: NSURL?)     class func absoluteURLWithDataRepresentation(_ data: NSData, relativeToURL baseURL: NSURL?) -> NSURL     @NSCopying var dataRepresentation: NSData { get }     var absoluteString: String { get }     var relativeString: String? { get }     @NSCopying var baseURL: NSURL? { get }     @NSCopying var absoluteURL: NSURL { get }     var scheme: String { get }     var resourceSpecifier: String { get }     var host: String? { get }     @NSCopying var port: NSNumber? { get }     var user: String? { get }     var password: String? { get }     var path: String? { get }     var fragment: String? { get }     var parameterString: String? { get }     var query: String? { get }     var relativePath: String? { get }     var hasDirectoryPath: Bool { get }     func getFileSystemRepresentation(_ buffer: UnsafeMutablePointer<Int8>, maxLength maxBufferLength: Int) -> Bool     var fileSystemRepresentation: UnsafePointer<Int8> { get }     var fileURL: Bool { get }     @NSCopying var standardizedURL: NSURL? { get }     func checkResourceIsReachableAndReturnError(_ error: NSErrorPointer) -> Bool     func isFileReferenceURL() -> Bool     func fileReferenceURL() -> NSURL?     @NSCopying var filePathURL: NSURL? { get }     func getResourceValue(_ value: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey key: String) throws     func resourceValuesForKeys(_ keys: [String]) throws -> [String : AnyObject]     func setResourceValue(_ value: AnyObject?, forKey key: String) throws     func setResourceValues(_ keyedValues: [String : AnyObject]) throws     func removeCachedResourceValueForKey(_ key: String)     func removeAllCachedResourceValues()     func setTemporaryResourceValue(_ value: AnyObject?, forKey key: String)     func bookmarkDataWithOptions(_ options: NSURLBookmarkCreationOptions, includingResourceValuesForKeys keys: [String]?, relativeToURL relativeURL: NSURL?) throws -> NSData     convenience init(byResolvingBookmarkData bookmarkData: NSData, options options: NSURLBookmarkResolutionOptions, relativeToURL relativeURL: NSURL?, bookmarkDataIsStale isStale: UnsafeMutablePointer<ObjCBool>) throws     class func URLByResolvingBookmarkData(_ bookmarkData: NSData, options options: NSURLBookmarkResolutionOptions, relativeToURL relativeURL: NSURL?, bookmarkDataIsStale isStale: UnsafeMutablePointer<ObjCBool>) throws -> Self     class func resourceValuesForKeys(_ keys: [String], fromBookmarkData bookmarkData: NSData) -> [String : AnyObject]?     class func writeBookmarkData(_ bookmarkData: NSData, toURL bookmarkFileURL: NSURL, options options: NSURLBookmarkFileCreationOptions) throws     class func bookmarkDataWithContentsOfURL(_ bookmarkFileURL: NSURL) throws -> NSData     convenience init(byResolvingAliasFileAtURL url: NSURL, options options: NSURLBookmarkResolutionOptions) throws     class func URLByResolvingAliasFileAtURL(_ url: NSURL, options options: NSURLBookmarkResolutionOptions) throws -> Self     func startAccessingSecurityScopedResource() -> Bool     func stopAccessingSecurityScopedResource() } extension NSURL : _FileReferenceLiteralConvertible {     required convenience init(fileReferenceLiteral path: String) } extension NSURL : _Reflectable { } extension NSURL {     func getPromisedItemResourceValue(_ value: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey key: String) throws     func promisedItemResourceValuesForKeys(_ keys: [String]) throws -> [String : AnyObject]     func checkPromisedItemIsReachableAndReturnError(_ error: NSErrorPointer) -> Bool } extension NSURL {     class func fileURLWithPathComponents(_ components: [String]) -> NSURL?     var pathComponents: [String]? { get }     var lastPathComponent: String? { get }     var pathExtension: String? { get }     func URLByAppendingPathComponent(_ pathComponent: String) -> NSURL     func URLByAppendingPathComponent(_ pathComponent: String, isDirectory isDirectory: Bool) -> NSURL     @NSCopying var URLByDeletingLastPathComponent: NSURL? { get }     func URLByAppendingPathExtension(_ pathExtension: String) -> NSURL     @NSCopying var URLByDeletingPathExtension: NSURL? { get }     @NSCopying var URLByStandardizingPath: NSURL? { get }     @NSCopying var URLByResolvingSymlinksInPath: NSURL? { get } } extension NSURL : _Reflectable { } extension NSURL : _FileReferenceLiteralConvertible {     required convenience init(fileReferenceLiteral path: String) } ``` | NSCopying, NSSecureCoding |

Modified [NSURLAuthenticationChallenge](https://developer.apple.com/documentation/foundation/nsurlauthenticationchallenge)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSURLAuthenticationChallenge : NSObject, NSSecureCoding, NSCoding {     init(protectionSpace space: NSURLProtectionSpace, proposedCredential credential: NSURLCredential?, previousFailureCount previousFailureCount: Int, failureResponse response: NSURLResponse?, error error: NSError?, sender sender: NSURLAuthenticationChallengeSender)     init(authenticationChallenge challenge: NSURLAuthenticationChallenge, sender sender: NSURLAuthenticationChallengeSender)     @NSCopying var protectionSpace: NSURLProtectionSpace { get }     @NSCopying var proposedCredential: NSURLCredential? { get }     var previousFailureCount: Int { get }     @NSCopying var failureResponse: NSURLResponse? { get }     @NSCopying var error: NSError? { get }     var sender: NSURLAuthenticationChallengeSender? { get } } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class NSURLAuthenticationChallenge : NSObject, NSSecureCoding {     init(protectionSpace space: NSURLProtectionSpace, proposedCredential credential: NSURLCredential?, previousFailureCount previousFailureCount: Int, failureResponse response: NSURLResponse?, error error: NSError?, sender sender: NSURLAuthenticationChallengeSender)     init(authenticationChallenge challenge: NSURLAuthenticationChallenge, sender sender: NSURLAuthenticationChallengeSender)     @NSCopying var protectionSpace: NSURLProtectionSpace { get }     @NSCopying var proposedCredential: NSURLCredential? { get }     var previousFailureCount: Int { get }     @NSCopying var failureResponse: NSURLResponse? { get }     @NSCopying var error: NSError? { get }     var sender: NSURLAuthenticationChallengeSender? { get } } ``` | NSSecureCoding |

Modified [NSURLCache](https://developer.apple.com/documentation/foundation/nsurlcache)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSURLCacheStoragePolicy [enum]](https://developer.apple.com/documentation/foundation/urlcache/storagepolicy)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSURLComponents](https://developer.apple.com/documentation/foundation/nsurlcomponents)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [NSURLConnection](https://developer.apple.com/documentation/foundation/nsurlconnection)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSURLConnectionDataDelegate](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol NSURLConnectionDataDelegate : NSURLConnectionDelegate, NSObjectProtocol {     optional func connection(_ connection: NSURLConnection, willSendRequest request: NSURLRequest, redirectResponse response: NSURLResponse?) -> NSURLRequest?     optional func connection(_ connection: NSURLConnection, didReceiveResponse response: NSURLResponse)     optional func connection(_ connection: NSURLConnection, didReceiveData data: NSData)     optional func connection(_ connection: NSURLConnection, needNewBodyStream request: NSURLRequest) -> NSInputStream?     optional func connection(_ connection: NSURLConnection, didSendBodyData bytesWritten: Int, totalBytesWritten totalBytesWritten: Int, totalBytesExpectedToWrite totalBytesExpectedToWrite: Int)     optional func connection(_ connection: NSURLConnection, willCacheResponse cachedResponse: NSCachedURLResponse) -> NSCachedURLResponse?     optional func connectionDidFinishLoading(_ connection: NSURLConnection) } ``` | NSObjectProtocol, NSURLConnectionDelegate |
| To | ``` protocol NSURLConnectionDataDelegate : NSURLConnectionDelegate {     optional func connection(_ connection: NSURLConnection, willSendRequest request: NSURLRequest, redirectResponse response: NSURLResponse?) -> NSURLRequest?     optional func connection(_ connection: NSURLConnection, didReceiveResponse response: NSURLResponse)     optional func connection(_ connection: NSURLConnection, didReceiveData data: NSData)     optional func connection(_ connection: NSURLConnection, needNewBodyStream request: NSURLRequest) -> NSInputStream?     optional func connection(_ connection: NSURLConnection, didSendBodyData bytesWritten: Int, totalBytesWritten totalBytesWritten: Int, totalBytesExpectedToWrite totalBytesExpectedToWrite: Int)     optional func connection(_ connection: NSURLConnection, willCacheResponse cachedResponse: NSCachedURLResponse) -> NSCachedURLResponse?     optional func connectionDidFinishLoading(_ connection: NSURLConnection) } ``` | NSURLConnectionDelegate |

Modified [NSURLConnectionDownloadDelegate](https://developer.apple.com/documentation/foundation/nsurlconnectiondownloaddelegate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol NSURLConnectionDownloadDelegate : NSURLConnectionDelegate, NSObjectProtocol {     optional func connection(_ connection: NSURLConnection, didWriteData bytesWritten: Int64, totalBytesWritten totalBytesWritten: Int64, expectedTotalBytes expectedTotalBytes: Int64)     optional func connectionDidResumeDownloading(_ connection: NSURLConnection, totalBytesWritten totalBytesWritten: Int64, expectedTotalBytes expectedTotalBytes: Int64)     func connectionDidFinishDownloading(_ connection: NSURLConnection, destinationURL destinationURL: NSURL) } ``` | NSObjectProtocol, NSURLConnectionDelegate |
| To | ``` protocol NSURLConnectionDownloadDelegate : NSURLConnectionDelegate {     optional func connection(_ connection: NSURLConnection, didWriteData bytesWritten: Int64, totalBytesWritten totalBytesWritten: Int64, expectedTotalBytes expectedTotalBytes: Int64)     optional func connectionDidResumeDownloading(_ connection: NSURLConnection, totalBytesWritten totalBytesWritten: Int64, expectedTotalBytes expectedTotalBytes: Int64)     func connectionDidFinishDownloading(_ connection: NSURLConnection, destinationURL destinationURL: NSURL) } ``` | NSURLConnectionDelegate |

Modified [NSURLCredential](https://developer.apple.com/documentation/foundation/nsurlcredential)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSURLCredential : NSObject, NSSecureCoding, NSCoding, NSCopying {     var persistence: NSURLCredentialPersistence { get } } extension NSURLCredential {     init(user user: String, password password: String, persistence persistence: NSURLCredentialPersistence)     class func credentialWithUser(_ user: String, password password: String, persistence persistence: NSURLCredentialPersistence) -> NSURLCredential     var user: String? { get }     var password: String? { get }     var hasPassword: Bool { get } } extension NSURLCredential {     init(identity identity: SecIdentity, certificates certArray: [AnyObject]?, persistence persistence: NSURLCredentialPersistence)     class func credentialWithIdentity(_ identity: SecIdentity, certificates certArray: [AnyObject]?, persistence persistence: NSURLCredentialPersistence) -> NSURLCredential     var identity: SecIdentity? { get }     var certificates: [AnyObject] { get } } extension NSURLCredential {     init(trust trust: SecTrust)      init(forTrust trust: SecTrust)     class func credentialForTrust(_ trust: SecTrust) -> NSURLCredential } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NSURLCredential : NSObject, NSSecureCoding, NSCopying {     var persistence: NSURLCredentialPersistence { get } } extension NSURLCredential {     init(user user: String, password password: String, persistence persistence: NSURLCredentialPersistence)     class func credentialWithUser(_ user: String, password password: String, persistence persistence: NSURLCredentialPersistence) -> NSURLCredential     var user: String? { get }     var password: String? { get }     var hasPassword: Bool { get } } extension NSURLCredential {     init(identity identity: SecIdentity, certificates certArray: [AnyObject]?, persistence persistence: NSURLCredentialPersistence)     class func credentialWithIdentity(_ identity: SecIdentity, certificates certArray: [AnyObject]?, persistence persistence: NSURLCredentialPersistence) -> NSURLCredential     var identity: SecIdentity? { get }     var certificates: [AnyObject] { get } } extension NSURLCredential {     init(trust trust: SecTrust)      init(forTrust trust: SecTrust)     class func credentialForTrust(_ trust: SecTrust) -> NSURLCredential } ``` | NSCopying, NSSecureCoding |

Modified [NSURLCredentialPersistence [enum]](https://developer.apple.com/documentation/foundation/urlcredential/persistence)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSURLCredentialStorage](https://developer.apple.com/documentation/foundation/urlcredentialstorage)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified NSURLError [enum]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` @objc enum NSURLError : Int, __BridgedNSError, ErrorType, _ObjectiveCBridgeableErrorType, _BridgedNSError {     case Unknown     case Cancelled     case BadURL     case TimedOut     case UnsupportedURL     case CannotFindHost     case CannotConnectToHost     case NetworkConnectionLost     case DNSLookupFailed     case HTTPTooManyRedirects     case ResourceUnavailable     case NotConnectedToInternet     case RedirectToNonExistentLocation     case BadServerResponse     case UserCancelledAuthentication     case UserAuthenticationRequired     case ZeroByteResource     case CannotDecodeRawData     case CannotDecodeContentData     case CannotParseResponse     case FileDoesNotExist     case FileIsDirectory     case NoPermissionsToReadFile     case SecureConnectionFailed     case ServerCertificateHasBadDate     case ServerCertificateUntrusted     case ServerCertificateHasUnknownRoot     case ServerCertificateNotYetValid     case ClientCertificateRejected     case ClientCertificateRequired     case CannotLoadFromNetwork     case CannotCreateFile     case CannotOpenFile     case CannotCloseFile     case CannotWriteToFile     case CannotRemoveFile     case CannotMoveFile     case DownloadDecodingFailedMidStream     case DownloadDecodingFailedToComplete     case InternationalRoamingOff     case CallIsActive     case DataNotAllowed     case RequestBodyStreamExhausted     case BackgroundSessionRequiresSharedContainer     case BackgroundSessionInUseByAnotherProcess     case BackgroundSessionWasDisconnected } ``` | Equatable, ErrorType, Hashable, RawRepresentable |
| To | ``` @objc enum NSURLError : Int, _BridgedNSError {     case Unknown     case Cancelled     case BadURL     case TimedOut     case UnsupportedURL     case CannotFindHost     case CannotConnectToHost     case NetworkConnectionLost     case DNSLookupFailed     case HTTPTooManyRedirects     case ResourceUnavailable     case NotConnectedToInternet     case RedirectToNonExistentLocation     case BadServerResponse     case UserCancelledAuthentication     case UserAuthenticationRequired     case ZeroByteResource     case CannotDecodeRawData     case CannotDecodeContentData     case CannotParseResponse     case FileDoesNotExist     case FileIsDirectory     case NoPermissionsToReadFile     case SecureConnectionFailed     case ServerCertificateHasBadDate     case ServerCertificateUntrusted     case ServerCertificateHasUnknownRoot     case ServerCertificateNotYetValid     case ClientCertificateRejected     case ClientCertificateRequired     case CannotLoadFromNetwork     case CannotCreateFile     case CannotOpenFile     case CannotCloseFile     case CannotWriteToFile     case CannotRemoveFile     case CannotMoveFile     case DownloadDecodingFailedMidStream     case DownloadDecodingFailedToComplete     case InternationalRoamingOff     case CallIsActive     case DataNotAllowed     case RequestBodyStreamExhausted     case BackgroundSessionRequiresSharedContainer     case BackgroundSessionInUseByAnotherProcess     case BackgroundSessionWasDisconnected } ``` | -- |

Modified [NSURLProtectionSpace](https://developer.apple.com/documentation/foundation/nsurlprotectionspace)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSURLProtectionSpace : NSObject, NSSecureCoding, NSCoding, NSCopying {     init(host host: String, port port: Int, `protocol` `protocol`: String?, realm realm: String?, authenticationMethod authenticationMethod: String?)     init(proxyHost host: String, port port: Int, type type: String?, realm realm: String?, authenticationMethod authenticationMethod: String?)     var realm: String? { get }     var receivesCredentialSecurely: Bool { get }     var host: String { get }     var port: Int { get }     var proxyType: String? { get }     var `protocol`: String? { get }     var authenticationMethod: String { get }     func isProxy() -> Bool } extension NSURLProtectionSpace {     var distinguishedNames: [NSData]? { get } } extension NSURLProtectionSpace {     var serverTrust: SecTrust? { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NSURLProtectionSpace : NSObject, NSSecureCoding, NSCopying {     init(host host: String, port port: Int, `protocol` `protocol`: String?, realm realm: String?, authenticationMethod authenticationMethod: String?)     init(proxyHost host: String, port port: Int, type type: String?, realm realm: String?, authenticationMethod authenticationMethod: String?)     var realm: String? { get }     var receivesCredentialSecurely: Bool { get }     var host: String { get }     var port: Int { get }     var proxyType: String? { get }     var `protocol`: String? { get }     var authenticationMethod: String { get }     func isProxy() -> Bool } extension NSURLProtectionSpace {     var distinguishedNames: [NSData]? { get } } extension NSURLProtectionSpace {     var serverTrust: SecTrust? { get } } ``` | NSCopying, NSSecureCoding |

Modified [NSURLProtocol](https://developer.apple.com/documentation/foundation/nsurlprotocol)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSURLQueryItem](https://developer.apple.com/documentation/foundation/nsurlqueryitem)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSURLQueryItem : NSObject, NSSecureCoding, NSCoding, NSCopying {     init(name name: String, value value: String?)     class func queryItemWithName(_ name: String, value value: String?) -> Self     var name: String { get }     var value: String? { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NSURLQueryItem : NSObject, NSSecureCoding, NSCopying {     init(name name: String, value value: String?)     class func queryItemWithName(_ name: String, value value: String?) -> Self     var name: String { get }     var value: String? { get } } ``` | NSCopying, NSSecureCoding |

Modified [NSURLRelationship [enum]](https://developer.apple.com/documentation/foundation/nsurlrelationship)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSURLRequest](https://developer.apple.com/documentation/foundation/nsurlrequest)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSURLRequest : NSObject, NSSecureCoding, NSCoding, NSCopying, NSMutableCopying {     convenience init(URL URL: NSURL)     class func requestWithURL(_ URL: NSURL) -> Self     class func supportsSecureCoding() -> Bool     convenience init(URL URL: NSURL, cachePolicy cachePolicy: NSURLRequestCachePolicy, timeoutInterval timeoutInterval: NSTimeInterval)     class func requestWithURL(_ URL: NSURL, cachePolicy cachePolicy: NSURLRequestCachePolicy, timeoutInterval timeoutInterval: NSTimeInterval) -> Self     convenience init(URL URL: NSURL)     init(URL URL: NSURL, cachePolicy cachePolicy: NSURLRequestCachePolicy, timeoutInterval timeoutInterval: NSTimeInterval)     @NSCopying var URL: NSURL? { get }     var cachePolicy: NSURLRequestCachePolicy { get }     var timeoutInterval: NSTimeInterval { get }     @NSCopying var mainDocumentURL: NSURL? { get }     var networkServiceType: NSURLRequestNetworkServiceType { get }     var allowsCellularAccess: Bool { get } } extension NSURLRequest {     var HTTPMethod: String? { get }     var allHTTPHeaderFields: [String : String]? { get }     func valueForHTTPHeaderField(_ field: String) -> String?     @NSCopying var HTTPBody: NSData? { get }     var HTTPBodyStream: NSInputStream? { get }     var HTTPShouldHandleCookies: Bool { get }     var HTTPShouldUsePipelining: Bool { get } } ``` | AnyObject, NSCoding, NSCopying, NSMutableCopying, NSSecureCoding |
| To | ``` class NSURLRequest : NSObject, NSSecureCoding, NSCopying, NSMutableCopying {     convenience init(URL URL: NSURL)     class func requestWithURL(_ URL: NSURL) -> Self     class func supportsSecureCoding() -> Bool     convenience init(URL URL: NSURL, cachePolicy cachePolicy: NSURLRequestCachePolicy, timeoutInterval timeoutInterval: NSTimeInterval)     class func requestWithURL(_ URL: NSURL, cachePolicy cachePolicy: NSURLRequestCachePolicy, timeoutInterval timeoutInterval: NSTimeInterval) -> Self     convenience init(URL URL: NSURL)     init(URL URL: NSURL, cachePolicy cachePolicy: NSURLRequestCachePolicy, timeoutInterval timeoutInterval: NSTimeInterval)     @NSCopying var URL: NSURL? { get }     var cachePolicy: NSURLRequestCachePolicy { get }     var timeoutInterval: NSTimeInterval { get }     @NSCopying var mainDocumentURL: NSURL? { get }     var networkServiceType: NSURLRequestNetworkServiceType { get }     var allowsCellularAccess: Bool { get } } extension NSURLRequest {     var HTTPMethod: String? { get }     var allHTTPHeaderFields: [String : String]? { get }     func valueForHTTPHeaderField(_ field: String) -> String?     @NSCopying var HTTPBody: NSData? { get }     var HTTPBodyStream: NSInputStream? { get }     var HTTPShouldHandleCookies: Bool { get }     var HTTPShouldUsePipelining: Bool { get } } ``` | NSCopying, NSMutableCopying, NSSecureCoding |

Modified [NSURLRequestCachePolicy [enum]](https://developer.apple.com/documentation/foundation/nsurlrequest/cachepolicy)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSURLRequestNetworkServiceType [enum]](https://developer.apple.com/documentation/foundation/nsurlrequest/networkservicetype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSURLResponse](https://developer.apple.com/documentation/foundation/nsurlresponse)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSURLResponse : NSObject, NSSecureCoding, NSCoding, NSCopying {     init(URL URL: NSURL, MIMEType MIMEType: String?, expectedContentLength length: Int, textEncodingName name: String?)     @NSCopying var URL: NSURL? { get }     var MIMEType: String? { get }     var expectedContentLength: Int64 { get }     var textEncodingName: String? { get }     var suggestedFilename: String? { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NSURLResponse : NSObject, NSSecureCoding, NSCopying {     init(URL URL: NSURL, MIMEType MIMEType: String?, expectedContentLength length: Int, textEncodingName name: String?)     @NSCopying var URL: NSURL? { get }     var MIMEType: String? { get }     var expectedContentLength: Int64 { get }     var textEncodingName: String? { get }     var suggestedFilename: String? { get } } ``` | NSCopying, NSSecureCoding |

Modified [NSURLSession](https://developer.apple.com/documentation/foundation/nsurlsession)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSURLSessionAuthChallengeDisposition [enum]](https://developer.apple.com/documentation/foundation/urlsession/authchallengedisposition)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSURLSessionConfiguration](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [NSURLSessionDataDelegate](https://developer.apple.com/documentation/foundation/urlsessiondatadelegate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol NSURLSessionDataDelegate : NSURLSessionTaskDelegate, NSURLSessionDelegate, NSObjectProtocol {     optional func URLSession(_ session: NSURLSession, dataTask dataTask: NSURLSessionDataTask, didReceiveResponse response: NSURLResponse, completionHandler completionHandler: (NSURLSessionResponseDisposition) -> Void)     optional func URLSession(_ session: NSURLSession, dataTask dataTask: NSURLSessionDataTask, didBecomeDownloadTask downloadTask: NSURLSessionDownloadTask)     optional func URLSession(_ session: NSURLSession, dataTask dataTask: NSURLSessionDataTask, didBecomeStreamTask streamTask: NSURLSessionStreamTask)     optional func URLSession(_ session: NSURLSession, dataTask dataTask: NSURLSessionDataTask, didReceiveData data: NSData)     optional func URLSession(_ session: NSURLSession, dataTask dataTask: NSURLSessionDataTask, willCacheResponse proposedResponse: NSCachedURLResponse, completionHandler completionHandler: (NSCachedURLResponse?) -> Void) } ``` | NSObjectProtocol, NSURLSessionDelegate, NSURLSessionTaskDelegate |
| To | ``` protocol NSURLSessionDataDelegate : NSURLSessionTaskDelegate {     optional func URLSession(_ session: NSURLSession, dataTask dataTask: NSURLSessionDataTask, didReceiveResponse response: NSURLResponse, completionHandler completionHandler: (NSURLSessionResponseDisposition) -> Void)     optional func URLSession(_ session: NSURLSession, dataTask dataTask: NSURLSessionDataTask, didBecomeDownloadTask downloadTask: NSURLSessionDownloadTask)     optional func URLSession(_ session: NSURLSession, dataTask dataTask: NSURLSessionDataTask, didBecomeStreamTask streamTask: NSURLSessionStreamTask)     optional func URLSession(_ session: NSURLSession, dataTask dataTask: NSURLSessionDataTask, didReceiveData data: NSData)     optional func URLSession(_ session: NSURLSession, dataTask dataTask: NSURLSessionDataTask, willCacheResponse proposedResponse: NSCachedURLResponse, completionHandler completionHandler: (NSCachedURLResponse?) -> Void) } ``` | NSURLSessionTaskDelegate |

Modified [NSURLSessionDataTask](https://developer.apple.com/documentation/foundation/urlsessiondatatask)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSURLSessionDownloadDelegate](https://developer.apple.com/documentation/foundation/nsurlsessiondownloaddelegate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol NSURLSessionDownloadDelegate : NSURLSessionTaskDelegate, NSURLSessionDelegate, NSObjectProtocol {     func URLSession(_ session: NSURLSession, downloadTask downloadTask: NSURLSessionDownloadTask, didFinishDownloadingToURL location: NSURL)     optional func URLSession(_ session: NSURLSession, downloadTask downloadTask: NSURLSessionDownloadTask, didWriteData bytesWritten: Int64, totalBytesWritten totalBytesWritten: Int64, totalBytesExpectedToWrite totalBytesExpectedToWrite: Int64)     optional func URLSession(_ session: NSURLSession, downloadTask downloadTask: NSURLSessionDownloadTask, didResumeAtOffset fileOffset: Int64, expectedTotalBytes expectedTotalBytes: Int64) } ``` | NSObjectProtocol, NSURLSessionDelegate, NSURLSessionTaskDelegate |
| To | ``` protocol NSURLSessionDownloadDelegate : NSURLSessionTaskDelegate {     func URLSession(_ session: NSURLSession, downloadTask downloadTask: NSURLSessionDownloadTask, didFinishDownloadingToURL location: NSURL)     optional func URLSession(_ session: NSURLSession, downloadTask downloadTask: NSURLSessionDownloadTask, didWriteData bytesWritten: Int64, totalBytesWritten totalBytesWritten: Int64, totalBytesExpectedToWrite totalBytesExpectedToWrite: Int64)     optional func URLSession(_ session: NSURLSession, downloadTask downloadTask: NSURLSessionDownloadTask, didResumeAtOffset fileOffset: Int64, expectedTotalBytes expectedTotalBytes: Int64) } ``` | NSURLSessionTaskDelegate |

Modified [NSURLSessionDownloadTask](https://developer.apple.com/documentation/foundation/nsurlsessiondownloadtask)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSURLSessionResponseDisposition [enum]](https://developer.apple.com/documentation/foundation/nsurlsessionresponsedisposition)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSURLSessionStreamDelegate](https://developer.apple.com/documentation/foundation/urlsessionstreamdelegate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol NSURLSessionStreamDelegate : NSURLSessionTaskDelegate, NSURLSessionDelegate, NSObjectProtocol {     optional func URLSession(_ session: NSURLSession, readClosedForStreamTask streamTask: NSURLSessionStreamTask)     optional func URLSession(_ session: NSURLSession, writeClosedForStreamTask streamTask: NSURLSessionStreamTask)     optional func URLSession(_ session: NSURLSession, betterRouteDiscoveredForStreamTask streamTask: NSURLSessionStreamTask)     optional func URLSession(_ session: NSURLSession, streamTask streamTask: NSURLSessionStreamTask, didBecomeInputStream inputStream: NSInputStream, outputStream outputStream: NSOutputStream) } ``` | NSObjectProtocol, NSURLSessionDelegate, NSURLSessionTaskDelegate |
| To | ``` protocol NSURLSessionStreamDelegate : NSURLSessionTaskDelegate {     optional func URLSession(_ session: NSURLSession, readClosedForStreamTask streamTask: NSURLSessionStreamTask)     optional func URLSession(_ session: NSURLSession, writeClosedForStreamTask streamTask: NSURLSessionStreamTask)     optional func URLSession(_ session: NSURLSession, betterRouteDiscoveredForStreamTask streamTask: NSURLSessionStreamTask)     optional func URLSession(_ session: NSURLSession, streamTask streamTask: NSURLSessionStreamTask, didBecomeInputStream inputStream: NSInputStream, outputStream outputStream: NSOutputStream) } ``` | NSURLSessionTaskDelegate |

Modified [NSURLSessionStreamTask](https://developer.apple.com/documentation/foundation/nsurlsessionstreamtask)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSURLSessionTask](https://developer.apple.com/documentation/foundation/nsurlsessiontask)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [NSURLSessionTaskDelegate](https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol NSURLSessionTaskDelegate : NSURLSessionDelegate, NSObjectProtocol {     optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, willPerformHTTPRedirection response: NSHTTPURLResponse, newRequest request: NSURLRequest, completionHandler completionHandler: (NSURLRequest?) -> Void)     optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, didReceiveChallenge challenge: NSURLAuthenticationChallenge, completionHandler completionHandler: (NSURLSessionAuthChallengeDisposition, NSURLCredential?) -> Void)     optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, needNewBodyStream completionHandler: (NSInputStream?) -> Void)     optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, didSendBodyData bytesSent: Int64, totalBytesSent totalBytesSent: Int64, totalBytesExpectedToSend totalBytesExpectedToSend: Int64)     optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, didCompleteWithError error: NSError?) } ``` | NSObjectProtocol, NSURLSessionDelegate |
| To | ``` protocol NSURLSessionTaskDelegate : NSURLSessionDelegate {     optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, willPerformHTTPRedirection response: NSHTTPURLResponse, newRequest request: NSURLRequest, completionHandler completionHandler: (NSURLRequest?) -> Void)     optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, didReceiveChallenge challenge: NSURLAuthenticationChallenge, completionHandler completionHandler: (NSURLSessionAuthChallengeDisposition, NSURLCredential?) -> Void)     optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, needNewBodyStream completionHandler: (NSInputStream?) -> Void)     optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, didSendBodyData bytesSent: Int64, totalBytesSent totalBytesSent: Int64, totalBytesExpectedToSend totalBytesExpectedToSend: Int64)     optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, didCompleteWithError error: NSError?) } ``` | NSURLSessionDelegate |

Modified [NSURLSessionTaskState [enum]](https://developer.apple.com/documentation/foundation/nsurlsessiontaskstate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSURLSessionUploadTask](https://developer.apple.com/documentation/foundation/nsurlsessionuploadtask)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSUserDefaults](https://developer.apple.com/documentation/foundation/userdefaults)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSUUID](https://developer.apple.com/documentation/foundation/nsuuid)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSUUID : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init()     class func UUID() -> Self     init()     convenience init?(UUIDString string: String)     convenience init(UUIDBytes bytes: UnsafePointer<UInt8>)     func getUUIDBytes(_ uuid: UnsafeMutablePointer<UInt8>)     var UUIDString: String { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NSUUID : NSObject, NSCopying, NSSecureCoding {     convenience init()     class func UUID() -> Self     init()     convenience init?(UUIDString string: String)     convenience init(UUIDBytes bytes: UnsafePointer<UInt8>)     func getUUIDBytes(_ uuid: UnsafeMutablePointer<UInt8>)     var UUIDString: String { get } } ``` | NSCopying, NSSecureCoding |

Modified [NSValue](https://developer.apple.com/documentation/foundation/nsvalue)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSValue : NSObject, NSCopying, NSSecureCoding, NSCoding {     func getValue(_ value: UnsafeMutablePointer<Void>)     var objCType: UnsafePointer<Int8> { get }     init(bytes value: UnsafePointer<Void>, objCType type: UnsafePointer<Int8>)     init?(coder aDecoder: NSCoder) } extension NSValue {      init(range range: NSRange)     class func valueWithRange(_ range: NSRange) -> NSValue     var rangeValue: NSRange { get } } extension NSValue {     class func valueWithBytes(_ value: UnsafePointer<Void>, objCType type: UnsafePointer<Int8>) -> NSValue      init(_ value: UnsafePointer<Void>, withObjCType type: UnsafePointer<Int8>)     class func value(_ value: UnsafePointer<Void>, withObjCType type: UnsafePointer<Int8>) -> NSValue } extension NSValue {      init(nonretainedObject anObject: AnyObject?)     class func valueWithNonretainedObject(_ anObject: AnyObject?) -> NSValue     var nonretainedObjectValue: AnyObject? { get }      init(pointer pointer: UnsafePointer<Void>)     class func valueWithPointer(_ pointer: UnsafePointer<Void>) -> NSValue     var pointerValue: UnsafeMutablePointer<Void> { get }     func isEqualToValue(_ value: NSValue) -> Bool } extension NSValue {      init(MKCoordinate coordinate: CLLocationCoordinate2D)     class func valueWithMKCoordinate(_ coordinate: CLLocationCoordinate2D) -> NSValue      init(MKCoordinateSpan span: MKCoordinateSpan)     class func valueWithMKCoordinateSpan(_ span: MKCoordinateSpan) -> NSValue     var MKCoordinateValue: CLLocationCoordinate2D { get }     var MKCoordinateSpanValue: MKCoordinateSpan { get } } extension NSValue {      init(CGPoint point: CGPoint)     class func valueWithCGPoint(_ point: CGPoint) -> NSValue      init(CGVector vector: CGVector)     class func valueWithCGVector(_ vector: CGVector) -> NSValue      init(CGSize size: CGSize)     class func valueWithCGSize(_ size: CGSize) -> NSValue      init(CGRect rect: CGRect)     class func valueWithCGRect(_ rect: CGRect) -> NSValue      init(CGAffineTransform transform: CGAffineTransform)     class func valueWithCGAffineTransform(_ transform: CGAffineTransform) -> NSValue      init(UIEdgeInsets insets: UIEdgeInsets)     class func valueWithUIEdgeInsets(_ insets: UIEdgeInsets) -> NSValue      init(UIOffset insets: UIOffset)     class func valueWithUIOffset(_ insets: UIOffset) -> NSValue     func CGPointValue() -> CGPoint     func CGVectorValue() -> CGVector     func CGSizeValue() -> CGSize     func CGRectValue() -> CGRect     func CGAffineTransformValue() -> CGAffineTransform     func UIEdgeInsetsValue() -> UIEdgeInsets     func UIOffsetValue() -> UIOffset } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NSValue : NSObject, NSCopying, NSSecureCoding {     func getValue(_ value: UnsafeMutablePointer<Void>)     var objCType: UnsafePointer<Int8> { get }     init(bytes value: UnsafePointer<Void>, objCType type: UnsafePointer<Int8>)     init?(coder aDecoder: NSCoder) } extension NSValue {      init(range range: NSRange)     class func valueWithRange(_ range: NSRange) -> NSValue     var rangeValue: NSRange { get } } extension NSValue {     class func valueWithBytes(_ value: UnsafePointer<Void>, objCType type: UnsafePointer<Int8>) -> NSValue      init(_ value: UnsafePointer<Void>, withObjCType type: UnsafePointer<Int8>)     class func value(_ value: UnsafePointer<Void>, withObjCType type: UnsafePointer<Int8>) -> NSValue } extension NSValue {      init(nonretainedObject anObject: AnyObject?)     class func valueWithNonretainedObject(_ anObject: AnyObject?) -> NSValue     var nonretainedObjectValue: AnyObject? { get }      init(pointer pointer: UnsafePointer<Void>)     class func valueWithPointer(_ pointer: UnsafePointer<Void>) -> NSValue     var pointerValue: UnsafeMutablePointer<Void> { get }     func isEqualToValue(_ value: NSValue) -> Bool } extension NSValue {      init(MKCoordinate coordinate: CLLocationCoordinate2D)     class func valueWithMKCoordinate(_ coordinate: CLLocationCoordinate2D) -> NSValue      init(MKCoordinateSpan span: MKCoordinateSpan)     class func valueWithMKCoordinateSpan(_ span: MKCoordinateSpan) -> NSValue     var MKCoordinateValue: CLLocationCoordinate2D { get }     var MKCoordinateSpanValue: MKCoordinateSpan { get } } extension NSValue {      init(CGPoint point: CGPoint)     class func valueWithCGPoint(_ point: CGPoint) -> NSValue      init(CGVector vector: CGVector)     class func valueWithCGVector(_ vector: CGVector) -> NSValue      init(CGSize size: CGSize)     class func valueWithCGSize(_ size: CGSize) -> NSValue      init(CGRect rect: CGRect)     class func valueWithCGRect(_ rect: CGRect) -> NSValue      init(CGAffineTransform transform: CGAffineTransform)     class func valueWithCGAffineTransform(_ transform: CGAffineTransform) -> NSValue      init(UIEdgeInsets insets: UIEdgeInsets)     class func valueWithUIEdgeInsets(_ insets: UIEdgeInsets) -> NSValue      init(UIOffset insets: UIOffset)     class func valueWithUIOffset(_ insets: UIOffset) -> NSValue     func CGPointValue() -> CGPoint     func CGVectorValue() -> CGVector     func CGSizeValue() -> CGSize     func CGRectValue() -> CGRect     func CGAffineTransformValue() -> CGAffineTransform     func UIEdgeInsetsValue() -> UIEdgeInsets     func UIOffsetValue() -> UIOffset } ``` | NSCopying, NSSecureCoding |

Modified [NSValueTransformer](https://developer.apple.com/documentation/foundation/nsvaluetransformer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSXMLParser](https://developer.apple.com/documentation/foundation/xmlparser)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSXMLParserError [enum]](https://developer.apple.com/documentation/foundation/nsxmlparsererror)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSXMLParserExternalEntityResolvingPolicy [enum]](https://developer.apple.com/documentation/foundation/nsxmlparserexternalentityresolvingpolicy)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified kCFStringEncodingASCII

|  | Declaration |
| --- | --- |
| From | ``` let kCFStringEncodingASCII: CFStringEncoding ``` |
| To | ``` var kCFStringEncodingASCII: CFStringEncoding { get } ``` |

Modified NSASCIIStringEncoding

|  | Declaration |
| --- | --- |
| From | ``` let NSASCIIStringEncoding: UInt ``` |
| To | ``` var NSASCIIStringEncoding: UInt { get } ``` |

Modified NSISO2022JPStringEncoding

|  | Declaration |
| --- | --- |
| From | ``` let NSISO2022JPStringEncoding: UInt ``` |
| To | ``` var NSISO2022JPStringEncoding: UInt { get } ``` |

Modified NSISOLatin1StringEncoding

|  | Declaration |
| --- | --- |
| From | ``` let NSISOLatin1StringEncoding: UInt ``` |
| To | ``` var NSISOLatin1StringEncoding: UInt { get } ``` |

Modified NSISOLatin2StringEncoding

|  | Declaration |
| --- | --- |
| From | ``` let NSISOLatin2StringEncoding: UInt ``` |
| To | ``` var NSISOLatin2StringEncoding: UInt { get } ``` |

Modified NSJapaneseEUCStringEncoding

|  | Declaration |
| --- | --- |
| From | ``` let NSJapaneseEUCStringEncoding: UInt ``` |
| To | ``` var NSJapaneseEUCStringEncoding: UInt { get } ``` |

Modified NSMacOSRomanStringEncoding

|  | Declaration |
| --- | --- |
| From | ``` let NSMacOSRomanStringEncoding: UInt ``` |
| To | ``` var NSMacOSRomanStringEncoding: UInt { get } ``` |

Modified NSNEXTSTEPStringEncoding

|  | Declaration |
| --- | --- |
| From | ``` let NSNEXTSTEPStringEncoding: UInt ``` |
| To | ``` var NSNEXTSTEPStringEncoding: UInt { get } ``` |

Modified NSNonLossyASCIIStringEncoding

|  | Declaration |
| --- | --- |
| From | ``` let NSNonLossyASCIIStringEncoding: UInt ``` |
| To | ``` var NSNonLossyASCIIStringEncoding: UInt { get } ``` |

Modified NSShiftJISStringEncoding

|  | Declaration |
| --- | --- |
| From | ``` let NSShiftJISStringEncoding: UInt ``` |
| To | ``` var NSShiftJISStringEncoding: UInt { get } ``` |

Modified NSSymbolStringEncoding

|  | Declaration |
| --- | --- |
| From | ``` let NSSymbolStringEncoding: UInt ``` |
| To | ``` var NSSymbolStringEncoding: UInt { get } ``` |

Modified NSUnicodeStringEncoding

|  | Declaration |
| --- | --- |
| From | ``` let NSUnicodeStringEncoding: UInt ``` |
| To | ``` var NSUnicodeStringEncoding: UInt { get } ``` |

Modified NSUTF16BigEndianStringEncoding

|  | Declaration |
| --- | --- |
| From | ``` let NSUTF16BigEndianStringEncoding: UInt ``` |
| To | ``` var NSUTF16BigEndianStringEncoding: UInt { get } ``` |

Modified NSUTF16LittleEndianStringEncoding

|  | Declaration |
| --- | --- |
| From | ``` let NSUTF16LittleEndianStringEncoding: UInt ``` |
| To | ``` var NSUTF16LittleEndianStringEncoding: UInt { get } ``` |

Modified NSUTF16StringEncoding

|  | Declaration |
| --- | --- |
| From | ``` let NSUTF16StringEncoding: UInt ``` |
| To | ``` var NSUTF16StringEncoding: UInt { get } ``` |

Modified NSUTF32BigEndianStringEncoding

|  | Declaration |
| --- | --- |
| From | ``` let NSUTF32BigEndianStringEncoding: UInt ``` |
| To | ``` var NSUTF32BigEndianStringEncoding: UInt { get } ``` |

Modified NSUTF32LittleEndianStringEncoding

|  | Declaration |
| --- | --- |
| From | ``` let NSUTF32LittleEndianStringEncoding: UInt ``` |
| To | ``` var NSUTF32LittleEndianStringEncoding: UInt { get } ``` |

Modified NSUTF32StringEncoding

|  | Declaration |
| --- | --- |
| From | ``` let NSUTF32StringEncoding: UInt ``` |
| To | ``` var NSUTF32StringEncoding: UInt { get } ``` |

Modified NSUTF8StringEncoding

|  | Declaration |
| --- | --- |
| From | ``` let NSUTF8StringEncoding: UInt ``` |
| To | ``` var NSUTF8StringEncoding: UInt { get } ``` |

Modified NSWindowsCP1250StringEncoding

|  | Declaration |
| --- | --- |
| From | ``` let NSWindowsCP1250StringEncoding: UInt ``` |
| To | ``` var NSWindowsCP1250StringEncoding: UInt { get } ``` |

Modified NSWindowsCP1251StringEncoding

|  | Declaration |
| --- | --- |
| From | ``` let NSWindowsCP1251StringEncoding: UInt ``` |
| To | ``` var NSWindowsCP1251StringEncoding: UInt { get } ``` |

Modified NSWindowsCP1252StringEncoding

|  | Declaration |
| --- | --- |
| From | ``` let NSWindowsCP1252StringEncoding: UInt ``` |
| To | ``` var NSWindowsCP1252StringEncoding: UInt { get } ``` |

Modified NSWindowsCP1253StringEncoding

|  | Declaration |
| --- | --- |
| From | ``` let NSWindowsCP1253StringEncoding: UInt ``` |
| To | ``` var NSWindowsCP1253StringEncoding: UInt { get } ``` |

Modified NSWindowsCP1254StringEncoding

|  | Declaration |
| --- | --- |
| From | ``` let NSWindowsCP1254StringEncoding: UInt ``` |
| To | ``` var NSWindowsCP1254StringEncoding: UInt { get } ``` |

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
