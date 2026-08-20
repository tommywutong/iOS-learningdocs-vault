---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/Foundation.html
archived_at: '2026-07-18T02:56:11.952452Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# Foundation Changes

## Foundation

Removed NSActivityOptions.valueRemoved NSArray.convertFromArrayLiteral(AnyObject) -> Self [class]Removed NSArray.objectAtIndexedSubscript(Int) -> AnyObjectRemoved NSAttributedStringEnumerationOptions.valueRemoved NSBinarySearchingOptions.valueRemoved NSByteCountFormatterUnits.valueRemoved NSCalendarOptions.valueRemoved NSCalendarUnit.valueRemoved NSComparisonPredicateOptions.valueRemoved NSData.dataWithContentsOfFile(String, options: NSDataReadingOptions, error: NSErrorPointer) -> Self! [class]Removed NSData.dataWithContentsOfURL(NSURL, options: NSDataReadingOptions, error: NSErrorPointer) -> Self! [class]Removed NSData.dataWithData(NSData) -> Self! [class]Removed NSDataBase64DecodingOptions.valueRemoved NSDataBase64EncodingOptions.valueRemoved NSDataDetector.dataDetectorWithTypes(NSTextCheckingTypes, error: NSErrorPointer) -> NSDataDetector? [class]Removed NSDataReadingOptions.valueRemoved NSDataSearchOptions.valueRemoved NSDataWritingOptions.valueRemoved NSDateComponentsFormatterZeroFormattingBehavior.valueRemoved NSDecimalNumber.decimalNumberWithMantissa(UInt64, exponent: Int16, isNegative: Bool) -> NSDecimalNumber [class]Removed NSDecimalNumber.decimalNumberWithString(String?) -> NSDecimalNumber [class]Removed NSDecimalNumber.decimalNumberWithString(String?, locale: AnyObject?) -> NSDecimalNumber [class]Removed NSDecimalNumberHandler.decimalNumberHandlerWithRoundingMode(NSRoundingMode, scale: Int16, raiseOnExactness: Bool, raiseOnOverflow: Bool, raiseOnUnderflow: Bool, raiseOnDivideByZero: Bool) -> Self! [class]Removed NSDictionary.convertFromDictionaryLiteral((NSCopying, AnyObject)) -> Self [class]Removed NSDictionary.objectForKeyedSubscript(NSCopying) -> AnyObject?Removed NSDirectoryEnumerationOptions.valueRemoved NSEnumerationOptions.valueRemoved NSError.errorWithDomain(String, code: Int, userInfo:[NSObject: AnyObject]?) -> Self! [class]Removed NSException.init(name: String, reason: String, userInfo:[NSObject: AnyObject]?)Removed NSFileCoordinatorReadingOptions.valueRemoved NSFileCoordinatorWritingOptions.valueRemoved NSFileManagerItemReplacementOptions.valueRemoved NSFileVersionAddingOptions.valueRemoved NSFileVersionReplacingOptions.valueRemoved NSFileWrapperReadingOptions.valueRemoved NSFileWrapperWritingOptions.valueRemoved NSHTTPCookie.cookieWithProperties([NSObject: AnyObject]) -> NSHTTPCookie? [class]Removed NSInputStream.inputStreamWithFileAtPath(String) -> Self! [class]Removed NSInvocationOperationRemoved NSInvocationOperation.invocationRemoved NSInvocationOperation.init(invocation: NSInvocation)Removed NSInvocationOperation.resultRemoved NSInvocationOperation.init(target: AnyObject, selector: Selector, object: AnyObject?)Removed NSJSONReadingOptions.valueRemoved NSJSONWritingOptions.valueRemoved NSKeyValueObservingOptions.valueRemoved NSLinguisticTaggerOptions.valueRemoved NSMatchingFlags.valueRemoved NSMatchingOptions.valueRemoved NSMethodSignatureRemoved NSMethodSignature.frameLengthRemoved NSMethodSignature.getArgumentTypeAtIndex(Int) -> UnsafePointer<Int8>Removed NSMethodSignature.isOneway() -> BoolRemoved NSMethodSignature.methodReturnLengthRemoved NSMethodSignature.methodReturnTypeRemoved NSMethodSignature.numberOfArgumentsRemoved NSMethodSignature.init(objCTypes: UnsafePointer<Int8>)Removed NSMutableArray.setObject(AnyObject, atIndexedSubscript: Int)Removed NSMutableDictionary.setObject(AnyObject?, forKeyedSubscript: NSCopying)Removed NSMutableOrderedSet.setObject(AnyObject, atIndexedSubscript: Int)Removed NSMutableString.stringWithCapacity(Int) -> NSMutableString [class]Removed NSNetServiceOptions.valueRemoved NSNumber.convertFromBooleanLiteral(Bool) -> Self [class]Removed NSNumber.convertFromFloatLiteral(Double) -> Self [class]Removed NSNumber.convertFromIntegerLiteral(Int) -> Self [class]Removed NSNumber.numberWithBool(Bool) -> NSNumber [class]Removed NSNumber.numberWithChar(Int8) -> NSNumber [class]Removed NSNumber.numberWithDouble(Double) -> NSNumber [class]Removed NSNumber.numberWithFloat(Float) -> NSNumber [class]Removed NSNumber.numberWithInt(Int32) -> NSNumber [class]Removed NSNumber.numberWithInteger(Int) -> NSNumber [class]Removed NSNumber.numberWithLong(Int) -> NSNumber [class]Removed NSNumber.numberWithLongLong(Int64) -> NSNumber [class]Removed NSNumber.numberWithShort(Int16) -> NSNumber [class]Removed NSNumber.numberWithUnsignedChar(UInt8) -> NSNumber [class]Removed NSNumber.numberWithUnsignedInt(UInt32) -> NSNumber [class]Removed NSNumber.numberWithUnsignedInteger(Int) -> NSNumber [class]Removed NSNumber.numberWithUnsignedLong(UInt) -> NSNumber [class]Removed NSNumber.numberWithUnsignedLongLong(UInt64) -> NSNumber [class]Removed NSNumber.numberWithUnsignedShort(UInt16) -> NSNumber [class]Removed NSOrderedSet.objectAtIndexedSubscript(Int) -> AnyObjectRemoved NSOutputStream.outputStreamToFileAtPath(String, append: Bool) -> Self! [class]Removed NSPointerArray.pointerArrayWithOptions(NSPointerFunctionsOptions) -> NSPointerArray [class]Removed NSPointerArray.pointerArrayWithPointerFunctions(NSPointerFunctions) -> NSPointerArray [class]Removed NSPointerFunctions.pointerFunctionsWithOptions(NSPointerFunctionsOptions) -> NSPointerFunctions! [class]Removed NSPropertyListMutabilityOptions.valueRemoved NSProxy.methodSignatureForSelector(Selector) -> NSMethodSignature?Removed NSRegularExpression.regularExpressionWithPattern(String, options: NSRegularExpressionOptions, error: NSErrorPointer) -> NSRegularExpression? [class]Removed NSRegularExpressionOptions.valueRemoved NSSearchPathDomainMask.valueRemoved NSSortOptions.valueRemoved NSStreamEvent.valueRemoved NSString.convertFromExtendedGraphemeClusterLiteral(StaticString) -> Self [class]Removed NSString.convertFromStringLiteral(StaticString) -> Self [class]Removed NSString.stringWithCString(UnsafePointer<Int8>, encoding: UInt) -> Self! [class]Removed NSString.stringWithCharacters(UnsafePointer<unichar>, length: Int) -> Self! [class]Removed NSString.stringWithContentsOfFile(String, encoding: UInt, error: NSErrorPointer) -> Self! [class]Removed NSString.stringWithContentsOfFile(String, usedEncoding: UnsafeMutablePointer<UInt>, error: NSErrorPointer) -> Self! [class]Removed NSString.stringWithContentsOfURL(NSURL, encoding: UInt, error: NSErrorPointer) -> Self! [class]Removed NSString.stringWithContentsOfURL(NSURL, usedEncoding: UnsafeMutablePointer<UInt>, error: NSErrorPointer) -> Self! [class]Removed NSString.stringWithString(String) -> Self! [class]Removed NSString.stringWithUTF8String(UnsafePointer<Int8>) -> Self! [class]Removed NSStringCompareOptions.valueRemoved NSStringEncodingConversionOptions.valueRemoved NSStringEnumerationOptions.valueRemoved NSTextCheckingType.valueRemoved NSURL.URLByResolvingBookmarkData(NSData, options: NSURLBookmarkResolutionOptions, relativeToURL: NSURL?, bookmarkDataIsStale: UnsafeMutablePointer<ObjCBool>, error: NSErrorPointer) -> Self! [class]Removed NSURL.URLWithString(String) -> Self! [class]Removed NSURL.URLWithString(String, relativeToURL: NSURL!) -> Self! [class]Removed NSURLBookmarkCreationOptions.valueRemoved NSURLBookmarkResolutionOptions.valueRemoved NSURLComponents.componentsWithString(String) -> Self! [class]Removed NSURLComponents.componentsWithURL(NSURL, resolvingAgainstBaseURL: Bool) -> Self! [class]Removed NSURLConnection.connectionWithRequest(NSURLRequest, delegate: AnyObject?) -> NSURLConnection? [class]Removed NSURLCredential.credentialWithUser(String, password: String, persistence: NSURLCredentialPersistence) -> NSURLCredential [class]Removed NSURLQueryItem.queryItemWithName(String, value: String) -> Self! [class]Removed NSUUID.UUID() -> Self! [class]Removed NSValue.valueWithBytes(UnsafePointer<Void>, objCType: UnsafePointer<Int8>) -> NSValue [class]Removed NSVolumeEnumerationOptions.valueRemoved NSZone.convertFromNilLiteral() -> NSZone [static]Removed NSCreateZone(Int, Int, Bool) -> NSZoneRemoved NSRecycleZone(NSZone)Removed NSSetZoneName(NSZone, String)Removed NSZoneCalloc(NSZone, Int, Int) -> UnsafeMutablePointer<Void>Removed NSZoneFree(NSZone, UnsafeMutablePointer<Void>)Removed NSZoneFromPointer(UnsafeMutablePointer<Void>) -> NSZoneRemoved NSZoneMalloc(NSZone, Int) -> UnsafeMutablePointer<Void>Removed NSZoneName(NSZone) -> StringRemoved NSZoneRealloc(NSZone, UnsafeMutablePointer<Void>, Int) -> UnsafeMutablePointer<Void>Added Array.init(_fromNSArray: NSArray, noCopy: Bool)Added Bool.init(_: NSNumber)Added CGFloat.init(_: NSNumber)Added Double.init(_: NSNumber)Added Float.init(_: NSNumber)Added Int.init(_: NSNumber)Added NSActivityOptions.init(rawValue: UInt64)Added NSArray.init(arrayLiteral: AnyObject)Added NSAttributedStringEnumerationOptions.init(rawValue: UInt)Added NSBinarySearchingOptions.init(rawValue: UInt)Added NSByteCountFormatterUnits.init(rawValue: UInt)Added NSCalendarOptions.init(rawValue: UInt)Added NSCalendarUnit.init(rawValue: UInt)Added NSComparisonPredicateOptions.init(rawValue: UInt)Added NSDataBase64DecodingOptions.init(rawValue: UInt)Added NSDataBase64EncodingOptions.init(rawValue: UInt)Added NSDataReadingOptions.init(rawValue: UInt)Added NSDataSearchOptions.init(rawValue: UInt)Added NSDataWritingOptions.init(rawValue: UInt)Added NSDateComponentsFormatterZeroFormattingBehavior.init(rawValue: UInt)Added NSDictionary.init(dictionaryLiteral: (NSCopying, AnyObject))Added NSDirectoryEnumerationOptions.init(rawValue: UInt)Added NSEnumerationOptions.init(rawValue: UInt)Added NSFileCoordinatorReadingOptions.init(rawValue: UInt)Added NSFileCoordinatorWritingOptions.init(rawValue: UInt)Added NSFileManagerItemReplacementOptions.init(rawValue: UInt)Added NSFileVersionAddingOptions.init(rawValue: UInt)Added NSFileVersionReplacingOptions.init(rawValue: UInt)Added NSFileWrapperReadingOptions.init(rawValue: UInt)Added NSFileWrapperWritingOptions.init(rawValue: UInt)Added NSJSONReadingOptions.init(rawValue: UInt)Added NSJSONWritingOptions.init(rawValue: UInt)Added NSKeyValueObservingOptions.init(rawValue: UInt)Added NSLinguisticTaggerOptions.init(rawValue: UInt)Added NSMatchingFlags.init(rawValue: UInt)Added NSMatchingOptions.init(rawValue: UInt)Added NSNetServiceOptions.init(rawValue: UInt)Added NSNumber.init(booleanLiteral: Bool)Added NSNumber.init(floatLiteral: Double)Added NSNumber.init(integerLiteral: Int)Added NSObject.accessInstanceVariablesDirectly() -> Bool [class]Added NSObject.addObserver(NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutablePointer<Void>)Added NSObject.attemptRecoveryFromError(NSError!, optionIndex: Int) -> BoolAdded NSObject.attemptRecoveryFromError(NSError!, optionIndex: Int, delegate: AnyObject!, didRecoverSelector: Selector, contextInfo: UnsafeMutablePointer<Void>)Added NSObject.autoContentAccessingProxyAdded NSObject.automaticallyNotifiesObserversForKey(String) -> Bool [class]Added NSObject.awakeAfterUsingCoder(NSCoder) -> AnyObject?Added NSObject.cancelPreviousPerformRequestsWithTarget(AnyObject) [class]Added NSObject.cancelPreviousPerformRequestsWithTarget(AnyObject, selector: Selector, object: AnyObject?) [class]Added NSObject.classFallbacksForKeyedArchiver() -> [AnyObject] [class]Added NSObject.classForCoderAdded NSObject.classForKeyedArchiverAdded NSObject.classForKeyedUnarchiver() -> AnyClass [class]Added NSObject.dictionaryWithValuesForKeys([AnyObject]) -> [NSObject: AnyObject]Added NSObject.didChange(NSKeyValueChange, valuesAtIndexes: NSIndexSet, forKey: String)Added NSObject.didChangeValueForKey(String)Added NSObject.didChangeValueForKey(String, withSetMutation: NSKeyValueSetMutationKind, usingObjects: NSSet)Added NSObject.encode() -> [Word]Added NSObject.hashValueAdded NSObject.keyPathsForValuesAffectingValueForKey(String) -> NSSet [class]Added NSObject.mutableArrayValueForKey(String) -> NSMutableArrayAdded NSObject.mutableArrayValueForKeyPath(String) -> NSMutableArrayAdded NSObject.mutableOrderedSetValueForKey(String) -> NSMutableOrderedSetAdded NSObject.mutableOrderedSetValueForKeyPath(String) -> NSMutableOrderedSetAdded NSObject.mutableSetValueForKey(String) -> NSMutableSetAdded NSObject.mutableSetValueForKeyPath(String) -> NSMutableSetAdded NSObject.observationInfoAdded NSObject.observeValueForKeyPath(String, ofObject: AnyObject, change:[NSObject: AnyObject], context: UnsafeMutablePointer<Void>)Added NSObject.removeObserver(NSObject, forKeyPath: String)Added NSObject.removeObserver(NSObject, forKeyPath: String, context: UnsafeMutablePointer<Void>)Added NSObject.replacementObjectForCoder(NSCoder) -> AnyObject?Added NSObject.replacementObjectForKeyedArchiver(NSKeyedArchiver) -> AnyObject?Added NSObject.setNilValueForKey(String)Added NSObject.setValue(AnyObject?, forKey: String)Added NSObject.setValue(AnyObject?, forKeyPath: String)Added NSObject.setValue(AnyObject?, forUndefinedKey: String)Added NSObject.setValuesForKeysWithDictionary([NSObject: AnyObject])Added NSObject.setVersion(Int) [class]Added NSObject.validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey: String, error: NSErrorPointer) -> BoolAdded NSObject.validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath: String, error: NSErrorPointer) -> BoolAdded NSObject.valueForKey(String) -> AnyObject?Added NSObject.valueForKeyPath(String) -> AnyObject?Added NSObject.valueForUndefinedKey(String) -> AnyObject?Added NSObject.version() -> Int [class]Added NSObject.willChange(NSKeyValueChange, valuesAtIndexes: NSIndexSet, forKey: String)Added NSObject.willChangeValueForKey(String)Added NSObject.willChangeValueForKey(String, withSetMutation: NSKeyValueSetMutationKind, usingObjects: NSSet)Added NSPortDelegate.handlePortMessage(NSPortMessage!)Added NSPropertyListMutabilityOptions.init(rawValue: UInt)Added NSRegularExpressionOptions.init(rawValue: UInt)Added NSSearchPathDomainMask.init(rawValue: UInt)Added NSSortOptions.init(rawValue: UInt)Added NSStreamEvent.init(rawValue: UInt)Added NSString.init(extendedGraphemeClusterLiteral: StaticString)Added NSString.init(stringLiteral: StaticString)Added NSString.init(unicodeScalarLiteral: StaticString)Added NSStringCompareOptions.init(rawValue: UInt)Added NSStringEncodingConversionOptions.init(rawValue: UInt)Added NSStringEnumerationOptions.init(rawValue: UInt)Added NSTextCheckingType.init(rawValue: UInt64)Added NSURLBookmarkCreationOptions.init(rawValue: UInt)Added NSURLBookmarkResolutionOptions.init(rawValue: UInt)Added NSVolumeEnumerationOptions.init(rawValue: UInt)Added String.init(CString: UnsafePointer<CChar>, encoding: NSStringEncoding)Added String.init(UTF8String: UnsafePointer<CChar>)Added String.init(_: NSString)Added String.availableStringEncodings() -> [NSStringEncoding] [static]Added String.init(bytes: S, encoding: NSStringEncoding)Added String.init(bytesNoCopy: UnsafeMutablePointer<Void>, length: Int, encoding: NSStringEncoding, freeWhenDone: Bool)Added String.cStringUsingEncoding(NSStringEncoding) -> [CChar]?Added String.canBeConvertedToEncoding(NSStringEncoding) -> BoolAdded String.capitalizedStringAdded String.capitalizedStringWithLocale(NSLocale?) -> StringAdded String.caseInsensitiveCompare(String) -> NSComparisonResultAdded String.commonPrefixWithString(String, options: NSStringCompareOptions) -> StringAdded String.compare(String, options: NSStringCompareOptions, range: Range<String.Index>?, locale: NSLocale?) -> NSComparisonResultAdded String.completePathIntoString(UnsafeMutablePointer<String>, caseSensitive: Bool, matchesIntoArray: UnsafeMutablePointer<[String]>, filterTypes:[String]?) -> IntAdded String.componentsSeparatedByCharactersInSet(NSCharacterSet) -> [String]Added String.componentsSeparatedByString(String) -> [String]Added String.init(contentsOfFile: String, encoding: NSStringEncoding, error: NSErrorPointer)Added String.init(contentsOfFile: String, usedEncoding: UnsafeMutablePointer<NSStringEncoding>, error: NSErrorPointer)Added String.init(contentsOfURL: NSURL, encoding: NSStringEncoding, error: NSErrorPointer)Added String.init(contentsOfURL: NSURL, usedEncoding: UnsafeMutablePointer<NSStringEncoding>, error: NSErrorPointer)Added String.dataUsingEncoding(NSStringEncoding, allowLossyConversion: Bool) -> NSData?Added String.decomposedStringWithCanonicalMappingAdded String.decomposedStringWithCompatibilityMappingAdded String.defaultCStringEncoding() -> NSStringEncoding [static]Added String.enumerateLines((line: String, inoutstop: Bool) -> ())Added String.enumerateLinguisticTagsInRange(Range<String.Index>, scheme: String, options: NSLinguisticTaggerOptions, orthography: NSOrthography?, _:(String, Range<String.Index>, Range<String.Index>, inoutBool) -> ())Added String.enumerateSubstringsInRange(Range<String.Index>, options: NSStringEnumerationOptions, _:(substring: String, substringRange: Range<String.Index>, enclosingRange: Range<String.Index>, inoutBool) -> ())Added String.fastestEncodingAdded String.fileSystemRepresentation() -> [CChar]Added String.init(format: String, _: CVarArgType)Added String.init(format: String, arguments:[CVarArgType])Added String.init(format: String, locale: NSLocale?, _: CVarArgType)Added String.init(format: String, locale: NSLocale?, arguments:[CVarArgType])Added String.getBytes([UInt8], maxLength: Int, usedLength: UnsafeMutablePointer<Int>, encoding: NSStringEncoding, options: NSStringEncodingConversionOptions, range: Range<String.Index>, remainingRange: UnsafeMutablePointer<Range<String.Index>>) -> BoolAdded String.getCString([CChar], maxLength: Int, encoding: NSStringEncoding) -> BoolAdded String.getFileSystemRepresentation([CChar], maxLength: Int) -> BoolAdded String.getLineStart(UnsafeMutablePointer<String.Index>, end: UnsafeMutablePointer<String.Index>, contentsEnd: UnsafeMutablePointer<String.Index>, forRange: Range<String.Index>)Added String.getParagraphStart(UnsafeMutablePointer<String.Index>, end: UnsafeMutablePointer<String.Index>, contentsEnd: UnsafeMutablePointer<String.Index>, forRange: Range<String.Index>)Added String.hashAdded String.lastPathComponentAdded String.lengthOfBytesUsingEncoding(NSStringEncoding) -> IntAdded String.lineRangeForRange(Range<String.Index>) -> Range<String.Index>Added String.linguisticTagsInRange(Range<String.Index>, scheme: String, options: NSLinguisticTaggerOptions, orthography: NSOrthography?, tokenRanges: UnsafeMutablePointer<[Range<String.Index>]>) -> [String]Added String.localizedCaseInsensitiveCompare(String) -> NSComparisonResultAdded String.localizedCompare(String) -> NSComparisonResultAdded String.localizedNameOfStringEncoding(NSStringEncoding) -> String [static]Added String.localizedStandardCompare(String) -> NSComparisonResultAdded String.localizedStringWithFormat(String, _: CVarArgType) -> String [static]Added String.lowercaseStringAdded String.lowercaseStringWithLocale(NSLocale) -> StringAdded String.maximumLengthOfBytesUsingEncoding(NSStringEncoding) -> IntAdded String.paragraphRangeForRange(Range<String.Index>) -> Range<String.Index>Added String.pathComponentsAdded String.pathExtensionAdded String.pathWithComponents([String]) -> String [static]Added String.precomposedStringWithCanonicalMappingAdded String.precomposedStringWithCompatibilityMappingAdded String.propertyList() -> AnyObjectAdded String.propertyListFromStringsFileFormat() -> [String: String]Added String.rangeOfCharacterFromSet(NSCharacterSet, options: NSStringCompareOptions, range: Range<String.Index>?) -> Range<String.Index>?Added String.rangeOfComposedCharacterSequenceAtIndex(String.Index) -> Range<String.Index>Added String.rangeOfComposedCharacterSequencesForRange(Range<String.Index>) -> Range<String.Index>Added String.rangeOfString(String, options: NSStringCompareOptions, range: Range<String.Index>?, locale: NSLocale?) -> Range<String.Index>?Added String.smallestEncodingAdded String.stringByAbbreviatingWithTildeInPathAdded String.stringByAddingPercentEncodingWithAllowedCharacters(NSCharacterSet) -> String?Added String.stringByAddingPercentEscapesUsingEncoding(NSStringEncoding) -> String?Added String.stringByAppendingFormat(String, _: CVarArgType) -> StringAdded String.stringByAppendingPathComponent(String) -> StringAdded String.stringByAppendingPathExtension(String) -> String?Added String.stringByAppendingString(String) -> StringAdded String.stringByDeletingLastPathComponentAdded String.stringByDeletingPathExtensionAdded String.stringByExpandingTildeInPathAdded String.stringByFoldingWithOptions(NSStringCompareOptions, locale: NSLocale) -> StringAdded String.stringByPaddingToLength(Int, withString: String, startingAtIndex: Int) -> StringAdded String.stringByRemovingPercentEncodingAdded String.stringByReplacingCharactersInRange(Range<String.Index>, withString: String) -> StringAdded String.stringByReplacingOccurrencesOfString(String, withString: String, options: NSStringCompareOptions, range: Range<String.Index>?) -> StringAdded String.stringByReplacingPercentEscapesUsingEncoding(NSStringEncoding) -> String?Added String.stringByResolvingSymlinksInPathAdded String.stringByStandardizingPathAdded String.stringByTrimmingCharactersInSet(NSCharacterSet) -> StringAdded String.stringsByAppendingPaths([String]) -> [String]Added String.substringFromIndex(String.Index) -> StringAdded String.substringToIndex(String.Index) -> StringAdded String.substringWithRange(Range<String.Index>) -> StringAdded String.uppercaseStringAdded String.uppercaseStringWithLocale(NSLocale) -> StringAdded String.init(utf16CodeUnits: UnsafePointer<unichar>, count: Int)Added String.init(utf16CodeUnitsNoCopy: UnsafePointer<unichar>, count: Int, freeWhenDone: Bool)Added String.utf16CountAdded String.writeToFile(String, atomically: Bool, encoding: NSStringEncoding, error: NSErrorPointer) -> BoolAdded String.writeToURL(NSURL, atomically: Bool, encoding: NSStringEncoding, error: NSErrorPointer) -> BoolAdded UInt.init(_: NSNumber)Added NSUserActivityConnectionUnavailableErrorAdded NSUserActivityErrorMaximumAdded NSUserActivityErrorMinimumAdded NSUserActivityHandoffFailedErrorAdded NSUserActivityHandoffUserInfoTooLargeErrorAdded NSUserActivityRemoteApplicationTimedOutErrorModified NSActivityOptions [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct NSActivityOptions : RawOptionSetType {     init(_ value: UInt64)     var value: UInt64     static var IdleDisplaySleepDisabled: NSActivityOptions { get }     static var IdleSystemSleepDisabled: NSActivityOptions { get }     static var SuddenTerminationDisabled: NSActivityOptions { get }     static var AutomaticTerminationDisabled: NSActivityOptions { get }     static var UserInitiated: NSActivityOptions { get }     static var UserInitiatedAllowingIdleSystemSleep: NSActivityOptions { get }     static var Background: NSActivityOptions { get }     static var LatencyCritical: NSActivityOptions { get } } ``` | iOS 8.0 |
| To | ``` struct NSActivityOptions : RawOptionSetType {     init(_ rawValue: UInt64)     init(rawValue rawValue: UInt64)     static var IdleDisplaySleepDisabled: NSActivityOptions { get }     static var IdleSystemSleepDisabled: NSActivityOptions { get }     static var SuddenTerminationDisabled: NSActivityOptions { get }     static var AutomaticTerminationDisabled: NSActivityOptions { get }     static var UserInitiated: NSActivityOptions { get }     static var UserInitiatedAllowingIdleSystemSleep: NSActivityOptions { get }     static var Background: NSActivityOptions { get }     static var LatencyCritical: NSActivityOptions { get } } ``` | iOS 7.0 |

Modified NSActivityOptions.init(_: UInt64)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt64) ``` |
| To | ``` init(_ rawValue: UInt64) ``` |

Modified NSArray

|  | Protocols |
| --- | --- |
| From | AnyObject, ArrayLiteralConvertible, NSCoding, NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding, Reflectable, SequenceType |
| To | AnyObject, ArrayLiteralConvertible, CKRecordValue, NSCoding, NSCopying, NSFastEnumeration, NSMutableCopying, NSObjectProtocol, NSSecureCoding, Reflectable, SequenceType |

Modified NSArray.init(contentsOfFile: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(contentsOfFile path: String) ``` |
| To | ``` convenience init?(contentsOfFile path: String) ``` |

Modified NSArray.init(contentsOfURL: NSURL)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(contentsOfURL url: NSURL) ``` |
| To | ``` convenience init?(contentsOfURL url: NSURL) ``` |

Modified NSArray.enumerateObjectsAtIndexes(NSIndexSet, options: NSEnumerationOptions, usingBlock:(AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSArray.enumerateObjectsUsingBlock((AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSArray.enumerateObjectsWithOptions(NSEnumerationOptions, usingBlock:(AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSArray.firstObject

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSArray.indexOfObject(AnyObject, inSortedRange: NSRange, options: NSBinarySearchingOptions, usingComparator: NSComparator) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSArray.indexOfObjectAtIndexes(NSIndexSet, options: NSEnumerationOptions, passingTest:(AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSArray.indexOfObjectPassingTest((AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSArray.indexOfObjectWithOptions(NSEnumerationOptions, passingTest:(AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSArray.indexesOfObjectsAtIndexes(NSIndexSet, options: NSEnumerationOptions, passingTest:(AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSArray.indexesOfObjectsPassingTest((AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSArray.indexesOfObjectsWithOptions(NSEnumerationOptions, passingTest:(AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSArray.removeObserver(NSObject, forKeyPath: String, context: UnsafeMutablePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSArray.removeObserver(NSObject, fromObjectsAtIndexes: NSIndexSet, forKeyPath: String, context: UnsafeMutablePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSArray.sortedArrayUsingComparator(NSComparator) -> [AnyObject]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSArray.sortedArrayWithOptions(NSSortOptions, usingComparator: NSComparator) -> [AnyObject]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSAttributedString

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified NSAttributedString.enumerateAttribute(String, inRange: NSRange, options: NSAttributedStringEnumerationOptions, usingBlock:(AnyObject!, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSAttributedString.enumerateAttributesInRange(NSRange, options: NSAttributedStringEnumerationOptions, usingBlock:([NSObject: AnyObject]!, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSAttributedStringEnumerationOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSAttributedStringEnumerationOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var Reverse: NSAttributedStringEnumerationOptions { get }     static var LongestEffectiveRangeNotRequired: NSAttributedStringEnumerationOptions { get } } ``` |
| To | ``` struct NSAttributedStringEnumerationOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Reverse: NSAttributedStringEnumerationOptions { get }     static var LongestEffectiveRangeNotRequired: NSAttributedStringEnumerationOptions { get } } ``` |

Modified NSAttributedStringEnumerationOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSBinarySearchingOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSBinarySearchingOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var FirstEqual: NSBinarySearchingOptions { get }     static var LastEqual: NSBinarySearchingOptions { get }     static var InsertionIndex: NSBinarySearchingOptions { get } } ``` |
| To | ``` struct NSBinarySearchingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var FirstEqual: NSBinarySearchingOptions { get }     static var LastEqual: NSBinarySearchingOptions { get }     static var InsertionIndex: NSBinarySearchingOptions { get } } ``` |

Modified NSBinarySearchingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSBlockOperation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSBundle.init(URL: NSURL)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` convenience init(URL url: NSURL) ``` | iOS 8.0 |
| To | ``` convenience init?(URL url: NSURL) ``` | iOS 4.0 |

Modified NSBundle.URLForAuxiliaryExecutable(String) -> NSURL?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSBundle.URLForResource(String, withExtension: String?) -> NSURL?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSBundle.URLForResource(String, withExtension: String?, subdirectory: String?) -> NSURL?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSBundle.URLForResource(String, withExtension: String?, subdirectory: String?, inBundleWithURL: NSURL) -> NSURL? [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSBundle.URLForResource(String, withExtension: String?, subdirectory: String?, localization: String?) -> NSURL?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSBundle.URLsForResourcesWithExtension(String?, subdirectory: String?) -> [AnyObject]?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSBundle.URLsForResourcesWithExtension(String?, subdirectory: String?, inBundleWithURL: NSURL) -> [AnyObject]? [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSBundle.URLsForResourcesWithExtension(String?, subdirectory: String?, localization: String?) -> [AnyObject]?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSBundle.appStoreReceiptURL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSBundle.builtInPlugInsURL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSBundle.bundleURL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSBundle.executableArchitectures

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSBundle.executableURL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSBundle.init(forClass: AnyClass)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(forClass aClass: AnyClass!) -> NSBundle ``` | iOS 8.0 |
| To | ``` init(forClass aClass: AnyClass) -> NSBundle ``` | iOS 8.1 |

Modified NSBundle.init(identifier: String)

|  | Declaration |
| --- | --- |
| From | ``` init(identifier identifier: String) -> NSBundle ``` |
| To | ``` init?(identifier identifier: String) -> NSBundle ``` |

Modified NSBundle.infoDictionary

|  | Declaration |
| --- | --- |
| From | ``` var infoDictionary: [NSObject : AnyObject] { get } ``` |
| To | ``` var infoDictionary: [NSObject : AnyObject]? { get } ``` |

Modified NSBundle.loadAndReturnError(NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSBundle.localizations

|  | Declaration |
| --- | --- |
| From | ``` var localizations: [AnyObject] { get } ``` |
| To | ``` var localizations: [AnyObject]? { get } ``` |

Modified NSBundle.localizedInfoDictionary

|  | Declaration |
| --- | --- |
| From | ``` var localizedInfoDictionary: [NSObject : AnyObject] { get } ``` |
| To | ``` var localizedInfoDictionary: [NSObject : AnyObject]? { get } ``` |

Modified NSBundle.init(path: String)

|  | Declaration |
| --- | --- |
| From | ``` init(path path: String) ``` |
| To | ``` init?(path path: String) ``` |

Modified NSBundle.preflightAndReturnError(NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSBundle.privateFrameworksURL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSBundle.resourceURL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSBundle.sharedFrameworksURL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSBundle.sharedSupportURL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSByteCountFormatter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSByteCountFormatterUnits [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSByteCountFormatterUnits : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var UseDefault: NSByteCountFormatterUnits { get }     static var UseBytes: NSByteCountFormatterUnits { get }     static var UseKB: NSByteCountFormatterUnits { get }     static var UseMB: NSByteCountFormatterUnits { get }     static var UseGB: NSByteCountFormatterUnits { get }     static var UseTB: NSByteCountFormatterUnits { get }     static var UsePB: NSByteCountFormatterUnits { get }     static var UseEB: NSByteCountFormatterUnits { get }     static var UseZB: NSByteCountFormatterUnits { get }     static var UseYBOrHigher: NSByteCountFormatterUnits { get }     static var UseAll: NSByteCountFormatterUnits { get } } ``` |
| To | ``` struct NSByteCountFormatterUnits : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var UseDefault: NSByteCountFormatterUnits { get }     static var UseBytes: NSByteCountFormatterUnits { get }     static var UseKB: NSByteCountFormatterUnits { get }     static var UseMB: NSByteCountFormatterUnits { get }     static var UseGB: NSByteCountFormatterUnits { get }     static var UseTB: NSByteCountFormatterUnits { get }     static var UsePB: NSByteCountFormatterUnits { get }     static var UseEB: NSByteCountFormatterUnits { get }     static var UseZB: NSByteCountFormatterUnits { get }     static var UseYBOrHigher: NSByteCountFormatterUnits { get }     static var UseAll: NSByteCountFormatterUnits { get } } ``` |

Modified NSByteCountFormatterUnits.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSCache

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSCalendar.AMSymbol

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSCalendar.PMSymbol

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSCalendar.autoupdatingCurrentCalendar() -> NSCalendar [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSCalendar.init(calendarIdentifier: String)

|  | Declaration |
| --- | --- |
| From | ``` init(calendarIdentifier ident: String) ``` |
| To | ``` init?(calendarIdentifier ident: String) ``` |

Modified NSCalendar.dateByAddingUnit(NSCalendarUnit, value: Int, toDate: NSDate, options: NSCalendarOptions) -> NSDate?

|  | Declaration |
| --- | --- |
| From | ``` func dateByAddingUnit(_ unit: NSCalendarUnit, value value: Int, toDate date: NSDate, options options: NSCalendarOptions) -> NSDate ``` |
| To | ``` func dateByAddingUnit(_ unit: NSCalendarUnit, value value: Int, toDate date: NSDate, options options: NSCalendarOptions) -> NSDate? ``` |

Modified NSCalendar.dateBySettingHour(Int, minute: Int, second: Int, ofDate: NSDate, options: NSCalendarOptions) -> NSDate?

|  | Declaration |
| --- | --- |
| From | ``` func dateBySettingHour(_ h: Int, minute m: Int, second s: Int, ofDate date: NSDate, options opts: NSCalendarOptions) -> NSDate ``` |
| To | ``` func dateBySettingHour(_ h: Int, minute m: Int, second s: Int, ofDate date: NSDate, options opts: NSCalendarOptions) -> NSDate? ``` |

Modified NSCalendar.eraSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSCalendar.init(identifier: String)

|  | Declaration |
| --- | --- |
| From | ``` init(identifier calendarIdentifierConstant: String) -> NSCalendar ``` |
| To | ``` init?(identifier calendarIdentifierConstant: String) -> NSCalendar ``` |

Modified NSCalendar.longEraSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSCalendar.monthSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSCalendar.nextDateAfterDate(NSDate, matchingHour: Int, minute: Int, second: Int, options: NSCalendarOptions) -> NSDate?

|  | Declaration |
| --- | --- |
| From | ``` func nextDateAfterDate(_ date: NSDate, matchingHour hourValue: Int, minute minuteValue: Int, second secondValue: Int, options options: NSCalendarOptions) -> NSDate! ``` |
| To | ``` func nextDateAfterDate(_ date: NSDate, matchingHour hourValue: Int, minute minuteValue: Int, second secondValue: Int, options options: NSCalendarOptions) -> NSDate? ``` |

Modified NSCalendar.quarterSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSCalendar.rangeOfUnit(NSCalendarUnit, startDate: AutoreleasingUnsafeMutablePointer<NSDate?>, interval: UnsafeMutablePointer<NSTimeInterval>, forDate: NSDate) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSCalendar.shortMonthSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSCalendar.shortQuarterSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSCalendar.shortStandaloneMonthSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSCalendar.shortStandaloneQuarterSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSCalendar.shortStandaloneWeekdaySymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSCalendar.shortWeekdaySymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSCalendar.standaloneMonthSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSCalendar.standaloneQuarterSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSCalendar.standaloneWeekdaySymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSCalendar.veryShortMonthSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSCalendar.veryShortStandaloneMonthSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSCalendar.veryShortStandaloneWeekdaySymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSCalendar.veryShortWeekdaySymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSCalendar.weekdaySymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSCalendarOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSCalendarOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var WrapComponents: NSCalendarOptions { get }     static var MatchStrictly: NSCalendarOptions { get }     static var SearchBackwards: NSCalendarOptions { get }     static var MatchPreviousTimePreservingSmallerUnits: NSCalendarOptions { get }     static var MatchNextTimePreservingSmallerUnits: NSCalendarOptions { get }     static var MatchNextTime: NSCalendarOptions { get }     static var MatchFirst: NSCalendarOptions { get }     static var MatchLast: NSCalendarOptions { get } } ``` |
| To | ``` struct NSCalendarOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var WrapComponents: NSCalendarOptions { get }     static var MatchStrictly: NSCalendarOptions { get }     static var SearchBackwards: NSCalendarOptions { get }     static var MatchPreviousTimePreservingSmallerUnits: NSCalendarOptions { get }     static var MatchNextTimePreservingSmallerUnits: NSCalendarOptions { get }     static var MatchNextTime: NSCalendarOptions { get }     static var MatchFirst: NSCalendarOptions { get }     static var MatchLast: NSCalendarOptions { get } } ``` |

Modified NSCalendarOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSCalendarUnit [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSCalendarUnit : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var CalendarUnitEra: NSCalendarUnit { get }     static var CalendarUnitYear: NSCalendarUnit { get }     static var CalendarUnitMonth: NSCalendarUnit { get }     static var CalendarUnitDay: NSCalendarUnit { get }     static var CalendarUnitHour: NSCalendarUnit { get }     static var CalendarUnitMinute: NSCalendarUnit { get }     static var CalendarUnitSecond: NSCalendarUnit { get }     static var CalendarUnitWeekday: NSCalendarUnit { get }     static var CalendarUnitWeekdayOrdinal: NSCalendarUnit { get }     static var CalendarUnitQuarter: NSCalendarUnit { get }     static var CalendarUnitWeekOfMonth: NSCalendarUnit { get }     static var CalendarUnitWeekOfYear: NSCalendarUnit { get }     static var CalendarUnitYearForWeekOfYear: NSCalendarUnit { get }     static var CalendarUnitNanosecond: NSCalendarUnit { get }     static var CalendarUnitCalendar: NSCalendarUnit { get }     static var CalendarUnitTimeZone: NSCalendarUnit { get }     static var EraCalendarUnit: NSCalendarUnit { get }     static var YearCalendarUnit: NSCalendarUnit { get }     static var MonthCalendarUnit: NSCalendarUnit { get }     static var DayCalendarUnit: NSCalendarUnit { get }     static var HourCalendarUnit: NSCalendarUnit { get }     static var MinuteCalendarUnit: NSCalendarUnit { get }     static var SecondCalendarUnit: NSCalendarUnit { get }     static var WeekCalendarUnit: NSCalendarUnit { get }     static var WeekdayCalendarUnit: NSCalendarUnit { get }     static var WeekdayOrdinalCalendarUnit: NSCalendarUnit { get }     static var QuarterCalendarUnit: NSCalendarUnit { get }     static var WeekOfMonthCalendarUnit: NSCalendarUnit { get }     static var WeekOfYearCalendarUnit: NSCalendarUnit { get }     static var YearForWeekOfYearCalendarUnit: NSCalendarUnit { get }     static var CalendarCalendarUnit: NSCalendarUnit { get }     static var TimeZoneCalendarUnit: NSCalendarUnit { get } } ``` |
| To | ``` struct NSCalendarUnit : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var CalendarUnitEra: NSCalendarUnit { get }     static var CalendarUnitYear: NSCalendarUnit { get }     static var CalendarUnitMonth: NSCalendarUnit { get }     static var CalendarUnitDay: NSCalendarUnit { get }     static var CalendarUnitHour: NSCalendarUnit { get }     static var CalendarUnitMinute: NSCalendarUnit { get }     static var CalendarUnitSecond: NSCalendarUnit { get }     static var CalendarUnitWeekday: NSCalendarUnit { get }     static var CalendarUnitWeekdayOrdinal: NSCalendarUnit { get }     static var CalendarUnitQuarter: NSCalendarUnit { get }     static var CalendarUnitWeekOfMonth: NSCalendarUnit { get }     static var CalendarUnitWeekOfYear: NSCalendarUnit { get }     static var CalendarUnitYearForWeekOfYear: NSCalendarUnit { get }     static var CalendarUnitNanosecond: NSCalendarUnit { get }     static var CalendarUnitCalendar: NSCalendarUnit { get }     static var CalendarUnitTimeZone: NSCalendarUnit { get }     static var EraCalendarUnit: NSCalendarUnit { get }     static var YearCalendarUnit: NSCalendarUnit { get }     static var MonthCalendarUnit: NSCalendarUnit { get }     static var DayCalendarUnit: NSCalendarUnit { get }     static var HourCalendarUnit: NSCalendarUnit { get }     static var MinuteCalendarUnit: NSCalendarUnit { get }     static var SecondCalendarUnit: NSCalendarUnit { get }     static var WeekCalendarUnit: NSCalendarUnit { get }     static var WeekdayCalendarUnit: NSCalendarUnit { get }     static var WeekdayOrdinalCalendarUnit: NSCalendarUnit { get }     static var QuarterCalendarUnit: NSCalendarUnit { get }     static var WeekOfMonthCalendarUnit: NSCalendarUnit { get }     static var WeekOfYearCalendarUnit: NSCalendarUnit { get }     static var YearForWeekOfYearCalendarUnit: NSCalendarUnit { get }     static var CalendarCalendarUnit: NSCalendarUnit { get }     static var TimeZoneCalendarUnit: NSCalendarUnit { get } } ``` |

Modified NSCalendarUnit.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSCharacterSet.URLFragmentAllowedCharacterSet() -> NSCharacterSet [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSCharacterSet.URLHostAllowedCharacterSet() -> NSCharacterSet [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSCharacterSet.URLPasswordAllowedCharacterSet() -> NSCharacterSet [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSCharacterSet.URLPathAllowedCharacterSet() -> NSCharacterSet [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSCharacterSet.URLQueryAllowedCharacterSet() -> NSCharacterSet [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSCharacterSet.URLUserAllowedCharacterSet() -> NSCharacterSet [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSCharacterSet.init(contentsOfFile: String)

|  | Declaration |
| --- | --- |
| From | ``` init(contentsOfFile fName: String) -> NSCharacterSet ``` |
| To | ``` init?(contentsOfFile fName: String) -> NSCharacterSet ``` |

Modified NSCharacterSet.newlineCharacterSet() -> NSCharacterSet [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSCoder.allowedClasses

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSCoder.decodeIntegerForKey(String) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSCoder.decodeObjectOfClass(AnyClass, forKey: String) -> AnyObject?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSCoder.decodeObjectOfClasses(NSSet, forKey: String) -> AnyObject?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSCoder.decodePropertyListForKey(String) -> AnyObject?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSCoder.encodeConditionalObject(AnyObject?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func encodeConditionalObject(_ object: AnyObject) ``` | iOS 8.0 |
| To | ``` func encodeConditionalObject(_ object: AnyObject?) ``` | iOS 8.1 |

Modified NSCoder.encodeConditionalObject(AnyObject?, forKey: String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func encodeConditionalObject(_ objv: AnyObject, forKey key: String) ``` | iOS 8.0 |
| To | ``` func encodeConditionalObject(_ objv: AnyObject?, forKey key: String) ``` | iOS 8.1 |

Modified NSCoder.encodeInteger(Int, forKey: String)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSCoder.encodeObject(AnyObject?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func encodeObject(_ object: AnyObject) ``` | iOS 8.0 |
| To | ``` func encodeObject(_ object: AnyObject?) ``` | iOS 8.1 |

Modified NSCoder.encodeObject(AnyObject?, forKey: String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func encodeObject(_ objv: AnyObject, forKey key: String) ``` | iOS 8.0 |
| To | ``` func encodeObject(_ objv: AnyObject?, forKey key: String) ``` | iOS 8.1 |

Modified NSCoder.requiresSecureCoding

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSComparisonPredicate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSComparisonPredicateOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSComparisonPredicateOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var CaseInsensitivePredicateOption: NSComparisonPredicateOptions { get }     static var DiacriticInsensitivePredicateOption: NSComparisonPredicateOptions { get }     static var NormalizedPredicateOption: NSComparisonPredicateOptions { get } } ``` |
| To | ``` struct NSComparisonPredicateOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var CaseInsensitivePredicateOption: NSComparisonPredicateOptions { get }     static var DiacriticInsensitivePredicateOption: NSComparisonPredicateOptions { get }     static var NormalizedPredicateOption: NSComparisonPredicateOptions { get } } ``` |

Modified NSComparisonPredicateOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSCompoundPredicate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSCompoundPredicate.andPredicateWithSubpredicates([AnyObject]) -> NSCompoundPredicate [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func andPredicateWithSubpredicates(_ subpredicates: [AnyObject]!) -> NSCompoundPredicate ``` | iOS 8.0 |
| To | ``` class func andPredicateWithSubpredicates(_ subpredicates: [AnyObject]) -> NSCompoundPredicate ``` | iOS 8.1 |

Modified NSCompoundPredicate.orPredicateWithSubpredicates([AnyObject]) -> NSCompoundPredicate [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func orPredicateWithSubpredicates(_ subpredicates: [AnyObject]!) -> NSCompoundPredicate ``` | iOS 8.0 |
| To | ``` class func orPredicateWithSubpredicates(_ subpredicates: [AnyObject]) -> NSCompoundPredicate ``` | iOS 8.1 |

Modified NSCompoundPredicate.subpredicates

|  | Declaration |
| --- | --- |
| From | ``` var subpredicates: [AnyObject]! { get } ``` |
| To | ``` var subpredicates: [AnyObject] { get } ``` |

Modified NSCondition

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSCondition.name

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSConditionLock.name

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSData

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying, NSMutableCopying, NSSecureCoding |
| To | AnyObject, CKRecordValue, NSCoding, NSCopying, NSMutableCopying, NSObjectProtocol, NSSecureCoding |

Modified NSData.init(base64EncodedData: NSData, options: NSDataBase64DecodingOptions)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(base64EncodedData base64Data: NSData, options options: NSDataBase64DecodingOptions) ``` | iOS 8.0 |
| To | ``` init?(base64EncodedData base64Data: NSData, options options: NSDataBase64DecodingOptions) ``` | iOS 7.0 |

Modified NSData.base64EncodedDataWithOptions(NSDataBase64EncodingOptions) -> NSData

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSData.init(base64EncodedString: String, options: NSDataBase64DecodingOptions)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(base64EncodedString base64String: String, options options: NSDataBase64DecodingOptions) ``` | iOS 8.0 |
| To | ``` init?(base64EncodedString base64String: String, options options: NSDataBase64DecodingOptions) ``` | iOS 7.0 |

Modified NSData.base64EncodedStringWithOptions(NSDataBase64EncodingOptions) -> String

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSData.init(bytesNoCopy: UnsafeMutablePointer<Void>, length: Int, deallocator:((UnsafeMutablePointer<Void>, Int) -> Void)?)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSData.init(contentsOfFile: String)

|  | Declaration |
| --- | --- |
| From | ``` init(contentsOfFile path: String) ``` |
| To | ``` init?(contentsOfFile path: String) ``` |

Modified NSData.init(contentsOfFile: String, options: NSDataReadingOptions, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(contentsOfFile path: String, options readOptionsMask: NSDataReadingOptions, error errorPtr: NSErrorPointer) ``` |
| To | ``` init?(contentsOfFile path: String, options readOptionsMask: NSDataReadingOptions, error errorPtr: NSErrorPointer) ``` |

Modified NSData.init(contentsOfMappedFile: String)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` init(contentsOfMappedFile path: String) ``` | iOS 8.0 | -- |
| To | ``` init?(contentsOfMappedFile path: String) ``` | iOS 2.0 | iOS 8.0 |

Modified NSData.init(contentsOfURL: NSURL)

|  | Declaration |
| --- | --- |
| From | ``` init(contentsOfURL url: NSURL) ``` |
| To | ``` init?(contentsOfURL url: NSURL) ``` |

Modified NSData.init(contentsOfURL: NSURL, options: NSDataReadingOptions, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(contentsOfURL url: NSURL, options readOptionsMask: NSDataReadingOptions, error errorPtr: NSErrorPointer) ``` |
| To | ``` init?(contentsOfURL url: NSURL, options readOptionsMask: NSDataReadingOptions, error errorPtr: NSErrorPointer) ``` |

Modified NSData.dataWithContentsOfMappedFile(String) -> AnyObject? [class]

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSData.enumerateByteRangesUsingBlock((UnsafePointer<Void>, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSData.getBytes(UnsafeMutablePointer<Void>)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSData.rangeOfData(NSData, options: NSDataSearchOptions, range: NSRange) -> NSRange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSDataBase64DecodingOptions [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct NSDataBase64DecodingOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var IgnoreUnknownCharacters: NSDataBase64DecodingOptions { get } } ``` | iOS 8.0 |
| To | ``` struct NSDataBase64DecodingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var IgnoreUnknownCharacters: NSDataBase64DecodingOptions { get } } ``` | iOS 7.0 |

Modified NSDataBase64DecodingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSDataBase64EncodingOptions [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct NSDataBase64EncodingOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var Encoding64CharacterLineLength: NSDataBase64EncodingOptions { get }     static var Encoding76CharacterLineLength: NSDataBase64EncodingOptions { get }     static var EncodingEndLineWithCarriageReturn: NSDataBase64EncodingOptions { get }     static var EncodingEndLineWithLineFeed: NSDataBase64EncodingOptions { get } } ``` | iOS 8.0 |
| To | ``` struct NSDataBase64EncodingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Encoding64CharacterLineLength: NSDataBase64EncodingOptions { get }     static var Encoding76CharacterLineLength: NSDataBase64EncodingOptions { get }     static var EncodingEndLineWithCarriageReturn: NSDataBase64EncodingOptions { get }     static var EncodingEndLineWithLineFeed: NSDataBase64EncodingOptions { get } } ``` | iOS 7.0 |

Modified NSDataBase64EncodingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSDataDetector

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSDataDetector.init(types: NSTextCheckingTypes, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(types checkingTypes: NSTextCheckingTypes, error error: NSErrorPointer) ``` |
| To | ``` init?(types checkingTypes: NSTextCheckingTypes, error error: NSErrorPointer) ``` |

Modified NSDataReadingOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSDataReadingOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var DataReadingMappedIfSafe: NSDataReadingOptions { get }     static var DataReadingUncached: NSDataReadingOptions { get }     static var DataReadingMappedAlways: NSDataReadingOptions { get }     static var DataReadingMapped: NSDataReadingOptions { get }     static var MappedRead: NSDataReadingOptions { get }     static var UncachedRead: NSDataReadingOptions { get } } ``` |
| To | ``` struct NSDataReadingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var DataReadingMappedIfSafe: NSDataReadingOptions { get }     static var DataReadingUncached: NSDataReadingOptions { get }     static var DataReadingMappedAlways: NSDataReadingOptions { get }     static var DataReadingMapped: NSDataReadingOptions { get }     static var MappedRead: NSDataReadingOptions { get }     static var UncachedRead: NSDataReadingOptions { get } } ``` |

Modified NSDataReadingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSDataSearchOptions [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct NSDataSearchOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var Backwards: NSDataSearchOptions { get }     static var Anchored: NSDataSearchOptions { get } } ``` | iOS 8.0 |
| To | ``` struct NSDataSearchOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Backwards: NSDataSearchOptions { get }     static var Anchored: NSDataSearchOptions { get } } ``` | iOS 4.0 |

Modified NSDataSearchOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSDataWritingOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSDataWritingOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var DataWritingAtomic: NSDataWritingOptions { get }     static var DataWritingWithoutOverwriting: NSDataWritingOptions { get }     static var DataWritingFileProtectionNone: NSDataWritingOptions { get }     static var DataWritingFileProtectionComplete: NSDataWritingOptions { get }     static var DataWritingFileProtectionCompleteUnlessOpen: NSDataWritingOptions { get }     static var DataWritingFileProtectionCompleteUntilFirstUserAuthentication: NSDataWritingOptions { get }     static var DataWritingFileProtectionMask: NSDataWritingOptions { get }     static var AtomicWrite: NSDataWritingOptions { get } } ``` |
| To | ``` struct NSDataWritingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var DataWritingAtomic: NSDataWritingOptions { get }     static var DataWritingWithoutOverwriting: NSDataWritingOptions { get }     static var DataWritingFileProtectionNone: NSDataWritingOptions { get }     static var DataWritingFileProtectionComplete: NSDataWritingOptions { get }     static var DataWritingFileProtectionCompleteUnlessOpen: NSDataWritingOptions { get }     static var DataWritingFileProtectionCompleteUntilFirstUserAuthentication: NSDataWritingOptions { get }     static var DataWritingFileProtectionMask: NSDataWritingOptions { get }     static var AtomicWrite: NSDataWritingOptions { get } } ``` |

Modified NSDataWritingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSDate

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying, NSSecureCoding, Reflectable |
| To | AnyObject, CKRecordValue, NSCoding, NSCopying, NSObjectProtocol, NSSecureCoding, Reflectable |

Modified NSDate.dateByAddingTimeInterval(NSTimeInterval) -> Self!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSDateComponents.calendar

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSDateComponents.date

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSDateComponents.leapMonth

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSDateComponents.nanosecond

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSDateComponents.quarter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSDateComponents.timeZone

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSDateComponents.weekOfMonth

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSDateComponents.weekOfYear

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSDateComponents.yearForWeekOfYear

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSDateComponentsFormatter.calendar

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var calendar: NSCalendar! ``` |
| To | ``` @NSCopying var calendar: NSCalendar? ``` |

Modified NSDateComponentsFormatterZeroFormattingBehavior [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSDateComponentsFormatterZeroFormattingBehavior : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var None: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var Default: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var DropLeading: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var DropMiddle: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var DropTrailing: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var DropAll: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var Pad: NSDateComponentsFormatterZeroFormattingBehavior { get } } ``` |
| To | ``` struct NSDateComponentsFormatterZeroFormattingBehavior : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var Default: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var DropLeading: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var DropMiddle: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var DropTrailing: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var DropAll: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var Pad: NSDateComponentsFormatterZeroFormattingBehavior { get } } ``` |

Modified NSDateComponentsFormatterZeroFormattingBehavior.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSDateFormatter.dateFormatFromTemplate(String, options: Int, locale: NSLocale?) -> String? [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSDateFormatter.doesRelativeDateFormatting

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSDateFormatter.gregorianStartDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSDateFormatter.localizedStringFromDate(NSDate, dateStyle: NSDateFormatterStyle, timeStyle: NSDateFormatterStyle) -> String [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func localizedStringFromDate(_ date: NSDate, dateStyle dstyle: NSDateFormatterStyle, timeStyle tstyle: NSDateFormatterStyle) -> String! ``` | iOS 8.0 |
| To | ``` class func localizedStringFromDate(_ date: NSDate, dateStyle dstyle: NSDateFormatterStyle, timeStyle tstyle: NSDateFormatterStyle) -> String ``` | iOS 4.0 |

Modified NSDateFormatter.longEraSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSDateFormatter.quarterSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSDateFormatter.shortQuarterSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSDateFormatter.shortStandaloneMonthSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSDateFormatter.shortStandaloneQuarterSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSDateFormatter.shortStandaloneWeekdaySymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSDateFormatter.standaloneMonthSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSDateFormatter.standaloneQuarterSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSDateFormatter.standaloneWeekdaySymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSDateFormatter.veryShortMonthSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSDateFormatter.veryShortStandaloneMonthSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSDateFormatter.veryShortStandaloneWeekdaySymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSDateFormatter.veryShortWeekdaySymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSDictionary.init(contentsOfFile: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(contentsOfFile path: String) ``` |
| To | ``` convenience init?(contentsOfFile path: String) ``` |

Modified NSDictionary.init(contentsOfURL: NSURL)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(contentsOfURL url: NSURL) ``` |
| To | ``` convenience init?(contentsOfURL url: NSURL) ``` |

Modified NSDictionary.enumerateKeysAndObjectsUsingBlock((AnyObject!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSDictionary.enumerateKeysAndObjectsWithOptions(NSEnumerationOptions, usingBlock:(AnyObject!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSDictionary.keysOfEntriesPassingTest((AnyObject!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSSet

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSDictionary.keysOfEntriesWithOptions(NSEnumerationOptions, passingTest:(AnyObject!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSSet

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSDictionary.keysSortedByValueUsingComparator(NSComparator) -> [AnyObject]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSDictionary.keysSortedByValueWithOptions(NSSortOptions, usingComparator: NSComparator) -> [AnyObject]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSDictionary.sharedKeySetForKeys([AnyObject]) -> AnyObject [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSDirectoryEnumerationOptions [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct NSDirectoryEnumerationOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var SkipsSubdirectoryDescendants: NSDirectoryEnumerationOptions { get }     static var SkipsPackageDescendants: NSDirectoryEnumerationOptions { get }     static var SkipsHiddenFiles: NSDirectoryEnumerationOptions { get } } ``` | iOS 8.0 |
| To | ``` struct NSDirectoryEnumerationOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var SkipsSubdirectoryDescendants: NSDirectoryEnumerationOptions { get }     static var SkipsPackageDescendants: NSDirectoryEnumerationOptions { get }     static var SkipsHiddenFiles: NSDirectoryEnumerationOptions { get } } ``` | iOS 4.0 |

Modified NSDirectoryEnumerationOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSDirectoryEnumerator.level

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSDirectoryEnumerator.skipDescendants()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSEnumerationOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSEnumerationOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var Concurrent: NSEnumerationOptions { get }     static var Reverse: NSEnumerationOptions { get } } ``` |
| To | ``` struct NSEnumerationOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Concurrent: NSEnumerationOptions { get }     static var Reverse: NSEnumerationOptions { get } } ``` |

Modified NSEnumerationOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSException.callStackReturnAddresses

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSException.callStackSymbols

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSExpression

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSExpression.allowEvaluation()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSExpression.collection

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSExpression.expressionBlock

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSExpression.expressionForAnyKey() -> NSExpression [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSExpression.leftExpression

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSExpression.predicate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSExpression.rightExpression

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSFileCoordinator

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSFileCoordinator.itemAtURL(NSURL, willMoveToURL: NSURL)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSFileCoordinator.purposeIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSFileCoordinatorReadingOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSFileCoordinatorReadingOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var WithoutChanges: NSFileCoordinatorReadingOptions { get }     static var ResolvesSymbolicLink: NSFileCoordinatorReadingOptions { get }     static var ImmediatelyAvailableMetadataOnly: NSFileCoordinatorReadingOptions { get }     static var ForUploading: NSFileCoordinatorReadingOptions { get } } ``` |
| To | ``` struct NSFileCoordinatorReadingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var WithoutChanges: NSFileCoordinatorReadingOptions { get }     static var ResolvesSymbolicLink: NSFileCoordinatorReadingOptions { get }     static var ImmediatelyAvailableMetadataOnly: NSFileCoordinatorReadingOptions { get }     static var ForUploading: NSFileCoordinatorReadingOptions { get } } ``` |

Modified NSFileCoordinatorReadingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSFileCoordinatorWritingOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSFileCoordinatorWritingOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var ForDeleting: NSFileCoordinatorWritingOptions { get }     static var ForMoving: NSFileCoordinatorWritingOptions { get }     static var ForMerging: NSFileCoordinatorWritingOptions { get }     static var ForReplacing: NSFileCoordinatorWritingOptions { get }     static var ContentIndependentMetadataOnly: NSFileCoordinatorWritingOptions { get } } ``` |
| To | ``` struct NSFileCoordinatorWritingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var ForDeleting: NSFileCoordinatorWritingOptions { get }     static var ForMoving: NSFileCoordinatorWritingOptions { get }     static var ForMerging: NSFileCoordinatorWritingOptions { get }     static var ForReplacing: NSFileCoordinatorWritingOptions { get }     static var ContentIndependentMetadataOnly: NSFileCoordinatorWritingOptions { get } } ``` |

Modified NSFileCoordinatorWritingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSFileHandle.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder coder: NSCoder) ``` |
| To | ``` init?(coder coder: NSCoder) ``` |

Modified NSFileHandle.init(forReadingAtPath: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(forReadingAtPath path: String) ``` |
| To | ``` convenience init?(forReadingAtPath path: String) ``` |

Modified NSFileHandle.init(forReadingFromURL: NSURL, error: NSErrorPointer)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | fileHandleForReadingFromURL(_:error:) | ``` class func fileHandleForReadingFromURL(_ url: NSURL, error error: NSErrorPointer) -> Self! ``` | iOS 8.0 |
| To | init(forReadingFromURL:error:) | ``` convenience init?(forReadingFromURL url: NSURL, error error: NSErrorPointer) ``` | iOS 8.1 |

Modified NSFileHandle.init(forUpdatingAtPath: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(forUpdatingAtPath path: String) ``` |
| To | ``` convenience init?(forUpdatingAtPath path: String) ``` |

Modified NSFileHandle.init(forUpdatingURL: NSURL, error: NSErrorPointer)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | fileHandleForUpdatingURL(_:error:) | ``` class func fileHandleForUpdatingURL(_ url: NSURL, error error: NSErrorPointer) -> Self! ``` | iOS 8.0 |
| To | init(forUpdatingURL:error:) | ``` convenience init?(forUpdatingURL url: NSURL, error error: NSErrorPointer) ``` | iOS 8.1 |

Modified NSFileHandle.init(forWritingAtPath: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(forWritingAtPath path: String) ``` |
| To | ``` convenience init?(forWritingAtPath path: String) ``` |

Modified NSFileHandle.init(forWritingToURL: NSURL, error: NSErrorPointer)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | fileHandleForWritingToURL(_:error:) | ``` class func fileHandleForWritingToURL(_ url: NSURL, error error: NSErrorPointer) -> Self! ``` | iOS 8.0 |
| To | init(forWritingToURL:error:) | ``` convenience init?(forWritingToURL url: NSURL, error error: NSErrorPointer) ``` | iOS 8.1 |

Modified NSFileHandle.readabilityHandler

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSFileHandle.writeabilityHandler

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSFileManager.URLForDirectory(NSSearchPathDirectory, inDomain: NSSearchPathDomainMask, appropriateForURL: NSURL?, create: Bool, error: NSErrorPointer) -> NSURL?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileManager.URLForPublishingUbiquitousItemAtURL(NSURL, expirationDate: AutoreleasingUnsafeMutablePointer<NSDate?>, error: NSErrorPointer) -> NSURL?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSFileManager.URLForUbiquityContainerIdentifier(String?) -> NSURL?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSFileManager.URLsForDirectory(NSSearchPathDirectory, inDomains: NSSearchPathDomainMask) -> [AnyObject]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileManager.attributesOfFileSystemForPath(String, error: NSErrorPointer) -> [NSObject: AnyObject]?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSFileManager.attributesOfItemAtPath(String, error: NSErrorPointer) -> [NSObject: AnyObject]?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSFileManager.containerURLForSecurityApplicationGroupIdentifier(String) -> NSURL?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSFileManager.contentsOfDirectoryAtPath(String, error: NSErrorPointer) -> [AnyObject]?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSFileManager.contentsOfDirectoryAtURL(NSURL, includingPropertiesForKeys:[AnyObject]?, options: NSDirectoryEnumerationOptions, error: NSErrorPointer) -> [AnyObject]?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileManager.copyItemAtPath(String, toPath: String, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSFileManager.copyItemAtURL(NSURL, toURL: NSURL, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileManager.createDirectoryAtPath(String, withIntermediateDirectories: Bool, attributes:[NSObject: AnyObject]?, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSFileManager.createDirectoryAtURL(NSURL, withIntermediateDirectories: Bool, attributes:[NSObject: AnyObject]?, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSFileManager.createSymbolicLinkAtPath(String, withDestinationPath: String, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSFileManager.createSymbolicLinkAtURL(NSURL, withDestinationURL: NSURL, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSFileManager.delegate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSFileManager.destinationOfSymbolicLinkAtPath(String, error: NSErrorPointer) -> String?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSFileManager.enumeratorAtURL(NSURL, includingPropertiesForKeys:[AnyObject]?, options: NSDirectoryEnumerationOptions, errorHandler:((NSURL!, NSError!) -> Bool)?) -> NSDirectoryEnumerator?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileManager.evictUbiquitousItemAtURL(NSURL, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSFileManager.isUbiquitousItemAtURL(NSURL) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSFileManager.linkItemAtPath(String, toPath: String, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSFileManager.linkItemAtURL(NSURL, toURL: NSURL, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileManager.mountedVolumeURLsIncludingResourceValuesForKeys([AnyObject]?, options: NSVolumeEnumerationOptions) -> [AnyObject]?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileManager.moveItemAtPath(String, toPath: String, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSFileManager.moveItemAtURL(NSURL, toURL: NSURL, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileManager.removeItemAtPath(String, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSFileManager.removeItemAtURL(NSURL, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileManager.replaceItemAtURL(NSURL, withItemAtURL: NSURL, backupItemName: String?, options: NSFileManagerItemReplacementOptions, resultingItemURL: AutoreleasingUnsafeMutablePointer<NSURL?>, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileManager.setAttributes([NSObject: AnyObject], ofItemAtPath: String, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSFileManager.setUbiquitous(Bool, itemAtURL: NSURL, destinationURL: NSURL, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSFileManager.startDownloadingUbiquitousItemAtURL(NSURL, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSFileManager.subpathsOfDirectoryAtPath(String, error: NSErrorPointer) -> [AnyObject]?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSFileManager.ubiquityIdentityToken

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSFileManagerDelegate.fileManager(NSFileManager, shouldCopyItemAtURL: NSURL, toURL: NSURL) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileManagerDelegate.fileManager(NSFileManager, shouldLinkItemAtURL: NSURL, toURL: NSURL) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileManagerDelegate.fileManager(NSFileManager, shouldMoveItemAtURL: NSURL, toURL: NSURL) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileManagerDelegate.fileManager(NSFileManager, shouldProceedAfterError: NSError, copyingItemAtURL: NSURL, toURL: NSURL) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileManagerDelegate.fileManager(NSFileManager, shouldProceedAfterError: NSError, linkingItemAtURL: NSURL, toURL: NSURL) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileManagerDelegate.fileManager(NSFileManager, shouldProceedAfterError: NSError, movingItemAtURL: NSURL, toURL: NSURL) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileManagerDelegate.fileManager(NSFileManager, shouldProceedAfterError: NSError, removingItemAtURL: NSURL) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileManagerDelegate.fileManager(NSFileManager, shouldRemoveItemAtURL: NSURL) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileManagerItemReplacementOptions [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct NSFileManagerItemReplacementOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var UsingNewMetadataOnly: NSFileManagerItemReplacementOptions { get }     static var WithoutDeletingBackupItem: NSFileManagerItemReplacementOptions { get } } ``` | iOS 8.0 |
| To | ``` struct NSFileManagerItemReplacementOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var UsingNewMetadataOnly: NSFileManagerItemReplacementOptions { get }     static var WithoutDeletingBackupItem: NSFileManagerItemReplacementOptions { get } } ``` | iOS 4.0 |

Modified NSFileManagerItemReplacementOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSFileSecurity

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSFileSecurity.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified NSFileVersion

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSFileVersion.init(ofItemAtURL: NSURL, forPersistentIdentifier: AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` init(ofItemAtURL url: NSURL, forPersistentIdentifier persistentIdentifier: AnyObject) -> NSFileVersion ``` |
| To | ``` init?(ofItemAtURL url: NSURL, forPersistentIdentifier persistentIdentifier: AnyObject) -> NSFileVersion ``` |

Modified NSFileVersionAddingOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSFileVersionAddingOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var ByMoving: NSFileVersionAddingOptions { get } } ``` |
| To | ``` struct NSFileVersionAddingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var ByMoving: NSFileVersionAddingOptions { get } } ``` |

Modified NSFileVersionAddingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSFileVersionReplacingOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSFileVersionReplacingOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var ByMoving: NSFileVersionReplacingOptions { get } } ``` |
| To | ``` struct NSFileVersionReplacingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var ByMoving: NSFileVersionReplacingOptions { get } } ``` |

Modified NSFileVersionReplacingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSFileWrapper

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileWrapper.init(URL: NSURL, options: NSFileWrapperReadingOptions, error: NSErrorPointer)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(URL url: NSURL, options options: NSFileWrapperReadingOptions, error outError: NSErrorPointer) ``` | iOS 8.0 |
| To | ``` init?(URL url: NSURL, options options: NSFileWrapperReadingOptions, error outError: NSErrorPointer) ``` | iOS 4.0 |

Modified NSFileWrapper.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder inCoder: NSCoder) ``` |
| To | ``` init?(coder inCoder: NSCoder) ``` |

Modified NSFileWrapper.matchesContentsOfURL(NSURL) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileWrapper.readFromURL(NSURL, options: NSFileWrapperReadingOptions, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileWrapper.init(serializedRepresentation: NSData)

|  | Declaration |
| --- | --- |
| From | ``` init(serializedRepresentation serializeRepresentation: NSData) ``` |
| To | ``` init?(serializedRepresentation serializeRepresentation: NSData) ``` |

Modified NSFileWrapper.symbolicLinkDestinationURL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileWrapper.init(symbolicLinkWithDestinationURL: NSURL)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileWrapper.writeToURL(NSURL, options: NSFileWrapperWritingOptions, originalContentsURL: NSURL?, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileWrapperReadingOptions [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct NSFileWrapperReadingOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var Immediate: NSFileWrapperReadingOptions { get }     static var WithoutMapping: NSFileWrapperReadingOptions { get } } ``` | iOS 8.0 |
| To | ``` struct NSFileWrapperReadingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Immediate: NSFileWrapperReadingOptions { get }     static var WithoutMapping: NSFileWrapperReadingOptions { get } } ``` | iOS 4.0 |

Modified NSFileWrapperReadingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSFileWrapperWritingOptions [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct NSFileWrapperWritingOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var Atomic: NSFileWrapperWritingOptions { get }     static var WithNameUpdating: NSFileWrapperWritingOptions { get } } ``` | iOS 8.0 |
| To | ``` struct NSFileWrapperWritingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Atomic: NSFileWrapperWritingOptions { get }     static var WithNameUpdating: NSFileWrapperWritingOptions { get } } ``` | iOS 4.0 |

Modified NSFileWrapperWritingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSFormatter.isPartialStringValid(String, newEditingString: AutoreleasingUnsafeMutablePointer<NSString?>, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func isPartialStringValid(_ partialString: String?, newEditingString newString: AutoreleasingUnsafeMutablePointer<NSString?>, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool ``` | iOS 8.0 |
| To | ``` func isPartialStringValid(_ partialString: String, newEditingString newString: AutoreleasingUnsafeMutablePointer<NSString?>, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool ``` | iOS 8.1 |

Modified NSHTTPCookie.init(properties: [NSObject: AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` init(properties properties: [NSObject : AnyObject]) ``` |
| To | ``` init?(properties properties: [NSObject : AnyObject]) ``` |

Modified NSHTTPCookieStorage.sortedCookiesUsingDescriptors([AnyObject]) -> [AnyObject]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSHTTPURLResponse.init(URL: NSURL, statusCode: Int, HTTPVersion: String?, headerFields:[NSObject: AnyObject]?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(URL url: NSURL, statusCode statusCode: Int, HTTPVersion HTTPVersion: String?, headerFields headerFields: [NSObject : AnyObject]?) ``` | iOS 8.0 |
| To | ``` init?(URL url: NSURL, statusCode statusCode: Int, HTTPVersion HTTPVersion: String?, headerFields headerFields: [NSObject : AnyObject]?) ``` | iOS 5.0 |

Modified NSHashTable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSHashTable.weakObjectsHashTable() -> NSHashTable [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSIndexSet.countOfIndexesInRange(NSRange) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSIndexSet.enumerateIndexesInRange(NSRange, options: NSEnumerationOptions, usingBlock:((Int, UnsafeMutablePointer<ObjCBool>) -> Void)?)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSIndexSet.enumerateIndexesUsingBlock((Int, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSIndexSet.enumerateIndexesWithOptions(NSEnumerationOptions, usingBlock:(Int, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSIndexSet.enumerateRangesInRange(NSRange, options: NSEnumerationOptions, usingBlock:(NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSIndexSet.enumerateRangesUsingBlock((NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSIndexSet.enumerateRangesWithOptions(NSEnumerationOptions, usingBlock:(NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSIndexSet.indexInRange(NSRange, options: NSEnumerationOptions, passingTest:(Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSIndexSet.indexPassingTest((Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSIndexSet.indexWithOptions(NSEnumerationOptions, passingTest:(Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSIndexSet.indexesInRange(NSRange, options: NSEnumerationOptions, passingTest:(Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSIndexSet.indexesPassingTest((Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSIndexSet.indexesWithOptions(NSEnumerationOptions, passingTest:(Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSInputStream.init(URL: NSURL)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(URL url: NSURL) ``` | iOS 8.0 |
| To | ``` init?(URL url: NSURL) ``` | iOS 4.0 |

Modified NSInputStream.init(fileAtPath: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(fileAtPath path: String) ``` |
| To | ``` convenience init?(fileAtPath path: String) ``` |

Modified NSItemProvider.init(contentsOfURL: NSURL!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(contentsOfURL fileURL: NSURL!) ``` |
| To | ``` convenience init?(contentsOfURL fileURL: NSURL!) ``` |

Modified NSJSONReadingOptions [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct NSJSONReadingOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var MutableContainers: NSJSONReadingOptions { get }     static var MutableLeaves: NSJSONReadingOptions { get }     static var AllowFragments: NSJSONReadingOptions { get } } ``` | iOS 8.0 |
| To | ``` struct NSJSONReadingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var MutableContainers: NSJSONReadingOptions { get }     static var MutableLeaves: NSJSONReadingOptions { get }     static var AllowFragments: NSJSONReadingOptions { get } } ``` | iOS 5.0 |

Modified NSJSONReadingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSJSONSerialization

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSJSONWritingOptions [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct NSJSONWritingOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var PrettyPrinted: NSJSONWritingOptions { get } } ``` | iOS 8.0 |
| To | ``` struct NSJSONWritingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var PrettyPrinted: NSJSONWritingOptions { get } } ``` | iOS 5.0 |

Modified NSJSONWritingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSKeyValueObservingOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSKeyValueObservingOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var New: NSKeyValueObservingOptions { get }     static var Old: NSKeyValueObservingOptions { get }     static var Initial: NSKeyValueObservingOptions { get }     static var Prior: NSKeyValueObservingOptions { get } } ``` |
| To | ``` struct NSKeyValueObservingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var New: NSKeyValueObservingOptions { get }     static var Old: NSKeyValueObservingOptions { get }     static var Initial: NSKeyValueObservingOptions { get }     static var Prior: NSKeyValueObservingOptions { get } } ``` |

Modified NSKeyValueObservingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSKeyedArchiver.encodeConditionalObject(AnyObject?, forKey: String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func encodeConditionalObject(_ objv: AnyObject, forKey key: String) ``` | iOS 8.0 |
| To | ``` func encodeConditionalObject(_ objv: AnyObject?, forKey key: String) ``` | iOS 8.1 |

Modified NSKeyedArchiver.setClassName(String?, forClass: AnyClass) [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func setClassName(_ codedName: String!, forClass cls: AnyClass) ``` | iOS 8.0 |
| To | ``` class func setClassName(_ codedName: String?, forClass cls: AnyClass) ``` | iOS 8.1 |

Modified NSKeyedArchiver.setClassName(String?, forClass: AnyClass)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setClassName(_ codedName: String!, forClass cls: AnyClass) ``` | iOS 8.0 |
| To | ``` func setClassName(_ codedName: String?, forClass cls: AnyClass) ``` | iOS 8.1 |

Modified NSKeyedArchiver.setRequiresSecureCoding(Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSKeyedUnarchiver.setClass(AnyClass?, forClassName: String) [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func setClass(_ cls: AnyClass!, forClassName codedName: String) ``` | iOS 8.0 |
| To | ``` class func setClass(_ cls: AnyClass?, forClassName codedName: String) ``` | iOS 8.1 |

Modified NSKeyedUnarchiver.setClass(AnyClass?, forClassName: String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setClass(_ cls: AnyClass!, forClassName codedName: String) ``` | iOS 8.0 |
| To | ``` func setClass(_ cls: AnyClass?, forClassName codedName: String) ``` | iOS 8.1 |

Modified NSKeyedUnarchiver.setRequiresSecureCoding(Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSLengthFormatter.unitStringFromValue(Double, unit: NSLengthFormatterUnit) -> String

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func unitStringFromValue(_ value: Double, unit unit: NSLengthFormatterUnit) -> String! ``` | iOS 8.0 |
| To | ``` func unitStringFromValue(_ value: Double, unit unit: NSLengthFormatterUnit) -> String ``` | iOS 8.1 |

Modified NSLinguisticTagger

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagger.availableTagSchemesForLanguage(String) -> [AnyObject] [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagger.enumerateTagsInRange(NSRange, scheme: String, options: NSLinguisticTaggerOptions, usingBlock:(String!, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagger.orthographyAtIndex(Int, effectiveRange: NSRangePointer) -> NSOrthography?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagger.possibleTagsAtIndex(Int, scheme: String, tokenRange: NSRangePointer, sentenceRange: NSRangePointer, scores: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [AnyObject]?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagger.sentenceRangeForRange(NSRange) -> NSRange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagger.setOrthography(NSOrthography?, range: NSRange)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagger.string

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagger.stringEditedInRange(NSRange, changeInLength: Int)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagger.tagAtIndex(Int, scheme: String, tokenRange: NSRangePointer, sentenceRange: NSRangePointer) -> String?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagger.tagSchemes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagger.init(tagSchemes: [AnyObject], options: Int)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagger.tagsInRange(NSRange, scheme: String, options: NSLinguisticTaggerOptions, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [AnyObject]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func tagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, tokenRanges tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [AnyObject]! ``` | iOS 8.0 |
| To | ``` func tagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, tokenRanges tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [AnyObject] ``` | iOS 5.0 |

Modified NSLinguisticTaggerOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSLinguisticTaggerOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var OmitWords: NSLinguisticTaggerOptions { get }     static var OmitPunctuation: NSLinguisticTaggerOptions { get }     static var OmitWhitespace: NSLinguisticTaggerOptions { get }     static var OmitOther: NSLinguisticTaggerOptions { get }     static var JoinNames: NSLinguisticTaggerOptions { get } } ``` |
| To | ``` struct NSLinguisticTaggerOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var OmitWords: NSLinguisticTaggerOptions { get }     static var OmitPunctuation: NSLinguisticTaggerOptions { get }     static var OmitWhitespace: NSLinguisticTaggerOptions { get }     static var OmitOther: NSLinguisticTaggerOptions { get }     static var JoinNames: NSLinguisticTaggerOptions { get } } ``` |

Modified NSLinguisticTaggerOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSLocale.autoupdatingCurrentLocale() -> NSLocale [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSLocale.canonicalLocaleIdentifierFromString(String) -> String [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func canonicalLocaleIdentifierFromString(_ string: String) -> String! ``` | iOS 8.0 |
| To | ``` class func canonicalLocaleIdentifierFromString(_ string: String) -> String ``` | iOS 8.1 |

Modified NSLocale.characterDirectionForLanguage(String) -> NSLocaleLanguageDirection [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSLocale.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified NSLocale.commonISOCurrencyCodes() -> [AnyObject] [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSLocale.lineDirectionForLanguage(String) -> NSLocaleLanguageDirection [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSLocale.localeIdentifierFromComponents([NSObject: AnyObject]) -> String [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func localeIdentifierFromComponents(_ dict: [NSObject : AnyObject]) -> String! ``` | iOS 8.0 |
| To | ``` class func localeIdentifierFromComponents(_ dict: [NSObject : AnyObject]) -> String ``` | iOS 8.1 |

Modified NSLocale.localeIdentifierFromWindowsLocaleCode(UInt32) -> String? [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSLocale.preferredLanguages() -> [AnyObject] [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSLocale.windowsLocaleCodeFromLocaleIdentifier(String) -> UInt32 [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSLock.name

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSMachPort.init(machPort: UInt32, options: Int)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSMachPort.portWithMachPort(UInt32, options: Int) -> NSPort [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSMapTable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSMapTable.strongToStrongObjectsMapTable() -> NSMapTable [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSMapTable.strongToWeakObjectsMapTable() -> NSMapTable [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSMapTable.weakToStrongObjectsMapTable() -> NSMapTable [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSMapTable.weakToWeakObjectsMapTable() -> NSMapTable [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSMatchingFlags [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSMatchingFlags : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var Progress: NSMatchingFlags { get }     static var Completed: NSMatchingFlags { get }     static var HitEnd: NSMatchingFlags { get }     static var RequiredEnd: NSMatchingFlags { get }     static var InternalError: NSMatchingFlags { get } } ``` |
| To | ``` struct NSMatchingFlags : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Progress: NSMatchingFlags { get }     static var Completed: NSMatchingFlags { get }     static var HitEnd: NSMatchingFlags { get }     static var RequiredEnd: NSMatchingFlags { get }     static var InternalError: NSMatchingFlags { get } } ``` |

Modified NSMatchingFlags.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSMatchingOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSMatchingOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var ReportProgress: NSMatchingOptions { get }     static var ReportCompletion: NSMatchingOptions { get }     static var Anchored: NSMatchingOptions { get }     static var WithTransparentBounds: NSMatchingOptions { get }     static var WithoutAnchoringBounds: NSMatchingOptions { get } } ``` |
| To | ``` struct NSMatchingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var ReportProgress: NSMatchingOptions { get }     static var ReportCompletion: NSMatchingOptions { get }     static var Anchored: NSMatchingOptions { get }     static var WithTransparentBounds: NSMatchingOptions { get }     static var WithoutAnchoringBounds: NSMatchingOptions { get } } ``` |

Modified NSMatchingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSMetadataItem

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMetadataQuery

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMetadataQuery.enumerateResultsUsingBlock((AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSMetadataQuery.enumerateResultsWithOptions(NSEnumerationOptions, usingBlock:(AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSMetadataQuery.operationQueue

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSMetadataQuery.searchItems

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSMetadataQueryAttributeValueTuple

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMetadataQueryResultGroup

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMutableArray.init(contentsOfFile: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(contentsOfFile path: String) ``` |
| To | ``` convenience init?(contentsOfFile path: String) ``` |

Modified NSMutableArray.init(contentsOfURL: NSURL)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(contentsOfURL url: NSURL) ``` |
| To | ``` convenience init?(contentsOfURL url: NSURL) ``` |

Modified NSMutableArray.sortUsingComparator(NSComparator)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSMutableArray.sortWithOptions(NSSortOptions, usingComparator: NSComparator)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSMutableAttributedString

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified NSMutableCharacterSet.init(contentsOfFile: String)

|  | Declaration |
| --- | --- |
| From | ``` init(contentsOfFile fName: String) -> NSMutableCharacterSet ``` |
| To | ``` init?(contentsOfFile fName: String) -> NSMutableCharacterSet ``` |

Modified NSMutableCharacterSet.newlineCharacterSet() -> NSMutableCharacterSet [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSMutableData.init(capacity: Int)

|  | Declaration |
| --- | --- |
| From | ``` init(capacity capacity: Int) ``` |
| To | ``` init?(capacity capacity: Int) ``` |

Modified NSMutableData.init(length: Int)

|  | Declaration |
| --- | --- |
| From | ``` init(length length: Int) ``` |
| To | ``` init?(length length: Int) ``` |

Modified NSMutableDictionary.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified NSMutableDictionary.init(contentsOfFile: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(contentsOfFile path: String) ``` |
| To | ``` convenience init?(contentsOfFile path: String) ``` |

Modified NSMutableDictionary.init(contentsOfURL: NSURL)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(contentsOfURL url: NSURL) ``` |
| To | ``` convenience init?(contentsOfURL url: NSURL) ``` |

Modified NSMutableOrderedSet

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMutableOrderedSet.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified NSMutableOrderedSet.filterUsingPredicate(NSPredicate)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMutableOrderedSet.sortUsingDescriptors([AnyObject])

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMutableSet.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified NSMutableSet.filterUsingPredicate(NSPredicate)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSMutableURLRequest.HTTPShouldUsePipelining

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSMutableURLRequest.addValue(String?, forHTTPHeaderField: String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func addValue(_ value: String!, forHTTPHeaderField field: String) ``` | iOS 8.0 |
| To | ``` func addValue(_ value: String?, forHTTPHeaderField field: String) ``` | iOS 8.1 |

Modified NSMutableURLRequest.allowsCellularAccess

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSMutableURLRequest.networkServiceType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSNetService.init(domain: String, type: String, name: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(domain domain: String, type type: String, name name: String) ``` |
| To | ``` convenience init!(domain domain: String, type type: String, name name: String) ``` |

Modified NSNetService.init(domain: String, type: String, name: String, port: Int32)

|  | Declaration |
| --- | --- |
| From | ``` init(domain domain: String, type type: String, name name: String, port port: Int32) ``` |
| To | ``` init!(domain domain: String, type type: String, name name: String, port port: Int32) ``` |

Modified NSNetService.includesPeerToPeer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSNetService.port

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSNetService.publishWithOptions(NSNetServiceOptions)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSNetServiceBrowser.includesPeerToPeer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSNetServiceDelegate.netService(NSNetService, didAcceptConnectionWithInputStream: NSInputStream, outputStream: NSOutputStream)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSNetServiceOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSNetServiceOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var NoAutoRename: NSNetServiceOptions { get }     static var ListenForConnections: NSNetServiceOptions { get } } ``` |
| To | ``` struct NSNetServiceOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var NoAutoRename: NSNetServiceOptions { get }     static var ListenForConnections: NSNetServiceOptions { get } } ``` |

Modified NSNetServiceOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSNotification.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified NSNotification.init(name: String, object: AnyObject?, userInfo:[NSObject: AnyObject]?)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSNotificationCenter.addObserverForName(String?, object: AnyObject?, queue: NSOperationQueue?, usingBlock:(NSNotification!) -> Void) -> NSObjectProtocol

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSNumber

|  | Protocols |
| --- | --- |
| From | AnyObject, BooleanLiteralConvertible, FloatLiteralConvertible, IntegerLiteralConvertible |
| To | AnyObject, BooleanLiteralConvertible, CKRecordValue, FloatLiteralConvertible, IntegerLiteralConvertible, NSObjectProtocol |

Modified NSNumber.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified NSNumber.init(integer: Int)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSNumber.integerValue

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSNumber.init(unsignedInteger: Int)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSNumber.unsignedIntegerValue

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSNumberFormatter.currencyDecimalSeparator

|  | Declaration |
| --- | --- |
| From | ``` var currencyDecimalSeparator: String! ``` |
| To | ``` var currencyDecimalSeparator: String? ``` |

Modified NSNumberFormatter.currencyGroupingSeparator

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var currencyGroupingSeparator: String! ``` | iOS 8.0 |
| To | ``` var currencyGroupingSeparator: String? ``` | iOS 2.0 |

Modified NSNumberFormatter.currencySymbol

|  | Declaration |
| --- | --- |
| From | ``` var currencySymbol: String! ``` |
| To | ``` var currencySymbol: String? ``` |

Modified NSNumberFormatter.decimalSeparator

|  | Declaration |
| --- | --- |
| From | ``` var decimalSeparator: String! ``` |
| To | ``` var decimalSeparator: String? ``` |

Modified NSNumberFormatter.internationalCurrencySymbol

|  | Declaration |
| --- | --- |
| From | ``` var internationalCurrencySymbol: String! ``` |
| To | ``` var internationalCurrencySymbol: String? ``` |

Modified NSNumberFormatter.lenient

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSNumberFormatter.localizedStringFromNumber(NSNumber, numberStyle: NSNumberFormatterStyle) -> String [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSNumberFormatter.maximumSignificantDigits

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSNumberFormatter.minimumSignificantDigits

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSNumberFormatter.multiplier

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var multiplier: NSNumber! ``` |
| To | ``` @NSCopying var multiplier: NSNumber? ``` |

Modified NSNumberFormatter.paddingCharacter

|  | Declaration |
| --- | --- |
| From | ``` var paddingCharacter: String! ``` |
| To | ``` var paddingCharacter: String? ``` |

Modified NSNumberFormatter.partialStringValidationEnabled

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSNumberFormatter.roundingIncrement

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var roundingIncrement: NSNumber! ``` |
| To | ``` @NSCopying var roundingIncrement: NSNumber? ``` |

Modified NSNumberFormatter.stringFromNumber(NSNumber) -> String?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func stringFromNumber(_ number: NSNumber) -> String! ``` | iOS 8.0 |
| To | ``` func stringFromNumber(_ number: NSNumber) -> String? ``` | iOS 8.1 |

Modified NSNumberFormatter.textAttributesForNegativeInfinity

|  | Declaration |
| --- | --- |
| From | ``` var textAttributesForNegativeInfinity: [NSObject : AnyObject]! ``` |
| To | ``` var textAttributesForNegativeInfinity: [NSObject : AnyObject]? ``` |

Modified NSNumberFormatter.textAttributesForNegativeValues

|  | Declaration |
| --- | --- |
| From | ``` var textAttributesForNegativeValues: [NSObject : AnyObject]! ``` |
| To | ``` var textAttributesForNegativeValues: [NSObject : AnyObject]? ``` |

Modified NSNumberFormatter.textAttributesForNil

|  | Declaration |
| --- | --- |
| From | ``` var textAttributesForNil: [NSObject : AnyObject]! ``` |
| To | ``` var textAttributesForNil: [NSObject : AnyObject]? ``` |

Modified NSNumberFormatter.usesSignificantDigits

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSOperation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSOperation.asynchronous

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSOperation.completionBlock

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSOperation.threadPriority

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 8.0 |

Modified NSOperation.waitUntilFinished()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSOperationQueue

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSOperationQueue.addOperationWithBlock(() -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSOperationQueue.addOperations([AnyObject], waitUntilFinished: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSOperationQueue.currentQueue() -> NSOperationQueue? [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSOperationQueue.mainQueue() -> NSOperationQueue [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSOperationQueue.name

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSOperationQueue.operationCount

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSOrderedSet

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSOrderedSet.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified NSOrderedSet.filteredOrderedSetUsingPredicate(NSPredicate) -> NSOrderedSet

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSOrderedSet.removeObserver(NSObject, forKeyPath: String, context: UnsafeMutablePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSOrderedSet.setValue(AnyObject?, forKey: String)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSOrderedSet.sortedArrayUsingDescriptors([AnyObject]) -> [AnyObject]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSOrderedSet.valueForKey(String) -> AnyObject

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func valueForKey(_ key: String) -> AnyObject! ``` | iOS 8.0 |
| To | ``` func valueForKey(_ key: String) -> AnyObject ``` | iOS 5.0 |

Modified NSOrthography

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSOrthography.allLanguages

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSOrthography.allScripts

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSOrthography.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified NSOrthography.dominantLanguage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSOrthography.dominantLanguageForScript(String) -> String

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSOrthography.init(dominantScript: String, languageMap:[NSObject: AnyObject])

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSOrthography.languagesForScript(String) -> [AnyObject]?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSOutputStream.init(URL: NSURL, append: Bool)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(URL url: NSURL, append shouldAppend: Bool) ``` | iOS 8.0 |
| To | ``` init?(URL url: NSURL, append shouldAppend: Bool) ``` | iOS 4.0 |

Modified NSOutputStream.init(toFileAtPath: String, append: Bool)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(toFileAtPath path: String, append shouldAppend: Bool) ``` |
| To | ``` convenience init?(toFileAtPath path: String, append shouldAppend: Bool) ``` |

Modified NSPointerArray

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSPointerArray.strongObjectsPointerArray() -> NSPointerArray [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSPointerArray.weakObjectsPointerArray() -> NSPointerArray [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSPointerFunctions

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSPredicate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSPredicate.allowEvaluation()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSPredicate.evaluateWithObject(AnyObject, substitutionVariables:[NSObject: AnyObject]?) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSPredicate.init(format: String, _: CVarArgType)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(format predicateFormat: String, _ args: CVarArgType...) ``` |
| To | ``` convenience init?(format predicateFormat: String, _ args: CVarArgType...) ``` |

Modified NSPredicate.init(fromMetadataQueryString: String)

|  | Declaration |
| --- | --- |
| From | ``` init(fromMetadataQueryString queryString: String) -> NSPredicate ``` |
| To | ``` init?(fromMetadataQueryString queryString: String) -> NSPredicate ``` |

Modified NSProcessInfo.activeProcessorCount

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSProcessInfo.beginActivityWithOptions(NSActivityOptions, reason: String) -> NSObjectProtocol

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSProcessInfo.endActivity(NSObjectProtocol)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSProcessInfo.operatingSystem() -> Int

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSProcessInfo.operatingSystemName() -> String

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSProcessInfo.performActivityWithOptions(NSActivityOptions, reason: String, usingBlock:() -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSProcessInfo.physicalMemory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSProcessInfo.processorCount

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSProcessInfo.systemUptime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSProgress

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSPropertyListMutabilityOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSPropertyListMutabilityOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var Immutable: NSPropertyListMutabilityOptions { get }     static var MutableContainers: NSPropertyListMutabilityOptions { get }     static var MutableContainersAndLeaves: NSPropertyListMutabilityOptions { get } } ``` |
| To | ``` struct NSPropertyListMutabilityOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Immutable: NSPropertyListMutabilityOptions { get }     static var MutableContainers: NSPropertyListMutabilityOptions { get }     static var MutableContainersAndLeaves: NSPropertyListMutabilityOptions { get } } ``` |

Modified NSPropertyListMutabilityOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSPropertyListSerialization.dataFromPropertyList(AnyObject, format: NSPropertyListFormat, errorDescription: UnsafeMutablePointer<NSString?>) -> NSData? [class]

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSPropertyListSerialization.dataWithPropertyList(AnyObject, format: NSPropertyListFormat, options: NSPropertyListWriteOptions, error: NSErrorPointer) -> NSData? [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSPropertyListSerialization.propertyListFromData(NSData, mutabilityOption: NSPropertyListMutabilityOptions, format: UnsafeMutablePointer<NSPropertyListFormat>, errorDescription: UnsafeMutablePointer<NSString?>) -> AnyObject? [class]

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSPropertyListSerialization.propertyListWithData(NSData, options: NSPropertyListReadOptions, format: UnsafeMutablePointer<NSPropertyListFormat>, error: NSErrorPointer) -> AnyObject? [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSPropertyListSerialization.propertyListWithStream(NSInputStream, options: NSPropertyListReadOptions, format: UnsafeMutablePointer<NSPropertyListFormat>, error: NSErrorPointer) -> AnyObject? [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSPropertyListSerialization.writePropertyList(AnyObject, toStream: NSOutputStream, format: NSPropertyListFormat, options: NSPropertyListWriteOptions, error: NSErrorPointer) -> Int [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSPurgeableData

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSRecursiveLock.name

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSRegularExpression

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSRegularExpression.init(pattern: String, options: NSRegularExpressionOptions, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(pattern pattern: String, options options: NSRegularExpressionOptions, error error: NSErrorPointer) ``` |
| To | ``` init?(pattern pattern: String, options options: NSRegularExpressionOptions, error error: NSErrorPointer) ``` |

Modified NSRegularExpressionOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSRegularExpressionOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var CaseInsensitive: NSRegularExpressionOptions { get }     static var AllowCommentsAndWhitespace: NSRegularExpressionOptions { get }     static var IgnoreMetacharacters: NSRegularExpressionOptions { get }     static var DotMatchesLineSeparators: NSRegularExpressionOptions { get }     static var AnchorsMatchLines: NSRegularExpressionOptions { get }     static var UseUnixLineSeparators: NSRegularExpressionOptions { get }     static var UseUnicodeWordBoundaries: NSRegularExpressionOptions { get } } ``` |
| To | ``` struct NSRegularExpressionOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var CaseInsensitive: NSRegularExpressionOptions { get }     static var AllowCommentsAndWhitespace: NSRegularExpressionOptions { get }     static var IgnoreMetacharacters: NSRegularExpressionOptions { get }     static var DotMatchesLineSeparators: NSRegularExpressionOptions { get }     static var AnchorsMatchLines: NSRegularExpressionOptions { get }     static var UseUnixLineSeparators: NSRegularExpressionOptions { get }     static var UseUnicodeWordBoundaries: NSRegularExpressionOptions { get } } ``` |

Modified NSRegularExpressionOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSRunLoop.mainRunLoop() -> NSRunLoop [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSScanner.scanHexDouble(UnsafeMutablePointer<Double>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSScanner.scanHexFloat(UnsafeMutablePointer<Float>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSScanner.scanHexLongLong(UnsafeMutablePointer<UInt64>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSScanner.scanInteger(UnsafeMutablePointer<Int>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSScanner.scanUnsignedLongLong(UnsafeMutablePointer<UInt64>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSSearchPathDomainMask [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSSearchPathDomainMask : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var UserDomainMask: NSSearchPathDomainMask { get }     static var LocalDomainMask: NSSearchPathDomainMask { get }     static var NetworkDomainMask: NSSearchPathDomainMask { get }     static var SystemDomainMask: NSSearchPathDomainMask { get }     static var AllDomainsMask: NSSearchPathDomainMask { get } } ``` |
| To | ``` struct NSSearchPathDomainMask : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var UserDomainMask: NSSearchPathDomainMask { get }     static var LocalDomainMask: NSSearchPathDomainMask { get }     static var NetworkDomainMask: NSSearchPathDomainMask { get }     static var SystemDomainMask: NSSearchPathDomainMask { get }     static var AllDomainsMask: NSSearchPathDomainMask { get } } ``` |

Modified NSSearchPathDomainMask.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSSet.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified NSSet.enumerateObjectsUsingBlock((AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSSet.enumerateObjectsWithOptions(NSEnumerationOptions, usingBlock:(AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSSet.filteredSetUsingPredicate(NSPredicate) -> NSSet

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSSet.objectsPassingTest((AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSSet

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSSet.objectsWithOptions(NSEnumerationOptions, passingTest:(AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSSet

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSSet.removeObserver(NSObject, forKeyPath: String, context: UnsafeMutablePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSSet.setByAddingObject(AnyObject) -> NSSet

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSSet.setByAddingObjectsFromArray([AnyObject]) -> NSSet

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSSet.setByAddingObjectsFromSet(NSSet) -> NSSet

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSSet.sortedArrayUsingDescriptors([AnyObject]) -> [AnyObject]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSSortDescriptor.allowEvaluation()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSSortDescriptor.comparator

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSSortDescriptor.init(key: String, ascending: Bool, comparator: NSComparator)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSSortOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSSortOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var Concurrent: NSSortOptions { get }     static var Stable: NSSortOptions { get } } ``` |
| To | ``` struct NSSortOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Concurrent: NSSortOptions { get }     static var Stable: NSSortOptions { get } } ``` |

Modified NSSortOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSStreamEvent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSStreamEvent : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var None: NSStreamEvent { get }     static var OpenCompleted: NSStreamEvent { get }     static var HasBytesAvailable: NSStreamEvent { get }     static var HasSpaceAvailable: NSStreamEvent { get }     static var ErrorOccurred: NSStreamEvent { get }     static var EndEncountered: NSStreamEvent { get } } ``` |
| To | ``` struct NSStreamEvent : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: NSStreamEvent { get }     static var OpenCompleted: NSStreamEvent { get }     static var HasBytesAvailable: NSStreamEvent { get }     static var HasSpaceAvailable: NSStreamEvent { get }     static var ErrorOccurred: NSStreamEvent { get }     static var EndEncountered: NSStreamEvent { get } } ``` |

Modified NSStreamEvent.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSString

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying, NSMutableCopying, NSSecureCoding, Reflectable, StringLiteralConvertible |
| To | AnyObject, CKRecordValue, NSCoding, NSCopying, NSMutableCopying, NSObjectProtocol, NSSecureCoding, Reflectable, StringLiteralConvertible |

Modified NSString.init(CString: UnsafePointer<Int8>, encoding: UInt)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(CString nullTerminatedCString: UnsafePointer<Int8>, encoding encoding: UInt) ``` |
| To | ``` convenience init?(CString nullTerminatedCString: UnsafePointer<Int8>, encoding encoding: UInt) ``` |

Modified NSString.init(UTF8String: UnsafePointer<Int8>)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(UTF8String nullTerminatedCString: UnsafePointer<Int8>) ``` |
| To | ``` convenience init?(UTF8String nullTerminatedCString: UnsafePointer<Int8>) ``` |

Modified NSString.boolValue

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSString.init(bytes: UnsafePointer<Void>, length: Int, encoding: UInt)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(bytes bytes: UnsafePointer<Void>, length len: Int, encoding encoding: UInt) ``` |
| To | ``` convenience init?(bytes bytes: UnsafePointer<Void>, length len: Int, encoding encoding: UInt) ``` |

Modified NSString.init(bytesNoCopy: UnsafeMutablePointer<Void>, length: Int, encoding: UInt, freeWhenDone: Bool)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length len: Int, encoding encoding: UInt, freeWhenDone freeBuffer: Bool) ``` |
| To | ``` convenience init?(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length len: Int, encoding encoding: UInt, freeWhenDone freeBuffer: Bool) ``` |

Modified NSString.capitalizedStringWithLocale(NSLocale?) -> String

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSString.componentsSeparatedByCharactersInSet(NSCharacterSet) -> [AnyObject]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSString.init(contentsOfFile: String, encoding: UInt, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(contentsOfFile path: String, encoding enc: UInt, error error: NSErrorPointer) ``` |
| To | ``` convenience init?(contentsOfFile path: String, encoding enc: UInt, error error: NSErrorPointer) ``` |

Modified NSString.init(contentsOfFile: String, usedEncoding: UnsafeMutablePointer<UInt>, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(contentsOfFile path: String, usedEncoding enc: UnsafeMutablePointer<UInt>, error error: NSErrorPointer) ``` |
| To | ``` convenience init?(contentsOfFile path: String, usedEncoding enc: UnsafeMutablePointer<UInt>, error error: NSErrorPointer) ``` |

Modified NSString.init(contentsOfURL: NSURL, encoding: UInt, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(contentsOfURL url: NSURL, encoding enc: UInt, error error: NSErrorPointer) ``` |
| To | ``` convenience init?(contentsOfURL url: NSURL, encoding enc: UInt, error error: NSErrorPointer) ``` |

Modified NSString.init(contentsOfURL: NSURL, usedEncoding: UnsafeMutablePointer<UInt>, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(contentsOfURL url: NSURL, usedEncoding enc: UnsafeMutablePointer<UInt>, error error: NSErrorPointer) ``` |
| To | ``` convenience init?(contentsOfURL url: NSURL, usedEncoding enc: UnsafeMutablePointer<UInt>, error error: NSErrorPointer) ``` |

Modified NSString.init(data: NSData, encoding: UInt)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(data data: NSData, encoding encoding: UInt) ``` |
| To | ``` convenience init?(data data: NSData, encoding encoding: UInt) ``` |

Modified NSString.enumerateLinesUsingBlock((String!, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSString.enumerateLinguisticTagsInRange(NSRange, scheme: String, options: NSLinguisticTaggerOptions, orthography: NSOrthography?, usingBlock:(String!, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumerateLinguisticTagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, orthography orthography: NSOrthography?, usingBlock block: ((String!, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)!) ``` | iOS 8.0 |
| To | ``` func enumerateLinguisticTagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, orthography orthography: NSOrthography?, usingBlock block: (String!, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) ``` | iOS 5.0 |

Modified NSString.enumerateSubstringsInRange(NSRange, options: NSStringEnumerationOptions, usingBlock:(String!, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSString.integerValue

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSString.linguisticTagsInRange(NSRange, scheme: String, options: NSLinguisticTaggerOptions, orthography: NSOrthography?, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [AnyObject]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSString.localizedStandardCompare(String) -> NSComparisonResult

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSString.longLongValue

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSString.lowercaseStringWithLocale(NSLocale?) -> String

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSString.rangeOfComposedCharacterSequencesForRange(NSRange) -> NSRange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSString.rangeOfString(String, options: NSStringCompareOptions, range: NSRange, locale: NSLocale?) -> NSRange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSString.stringByAddingPercentEncodingWithAllowedCharacters(NSCharacterSet) -> String?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSString.stringByFoldingWithOptions(NSStringCompareOptions, locale: NSLocale?) -> String

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSString.stringByRemovingPercentEncoding

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSString.stringByReplacingCharactersInRange(NSRange, withString: String) -> String

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSString.stringByReplacingOccurrencesOfString(String, withString: String) -> String

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSString.stringByReplacingOccurrencesOfString(String, withString: String, options: NSStringCompareOptions, range: NSRange) -> String

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSString.uppercaseStringWithLocale(NSLocale?) -> String

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSStringCompareOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSStringCompareOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var CaseInsensitiveSearch: NSStringCompareOptions { get }     static var LiteralSearch: NSStringCompareOptions { get }     static var BackwardsSearch: NSStringCompareOptions { get }     static var AnchoredSearch: NSStringCompareOptions { get }     static var NumericSearch: NSStringCompareOptions { get }     static var DiacriticInsensitiveSearch: NSStringCompareOptions { get }     static var WidthInsensitiveSearch: NSStringCompareOptions { get }     static var ForcedOrderingSearch: NSStringCompareOptions { get }     static var RegularExpressionSearch: NSStringCompareOptions { get } } ``` |
| To | ``` struct NSStringCompareOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var CaseInsensitiveSearch: NSStringCompareOptions { get }     static var LiteralSearch: NSStringCompareOptions { get }     static var BackwardsSearch: NSStringCompareOptions { get }     static var AnchoredSearch: NSStringCompareOptions { get }     static var NumericSearch: NSStringCompareOptions { get }     static var DiacriticInsensitiveSearch: NSStringCompareOptions { get }     static var WidthInsensitiveSearch: NSStringCompareOptions { get }     static var ForcedOrderingSearch: NSStringCompareOptions { get }     static var RegularExpressionSearch: NSStringCompareOptions { get } } ``` |

Modified NSStringCompareOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSStringEncodingConversionOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSStringEncodingConversionOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var AllowLossy: NSStringEncodingConversionOptions { get }     static var ExternalRepresentation: NSStringEncodingConversionOptions { get } } ``` |
| To | ``` struct NSStringEncodingConversionOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var AllowLossy: NSStringEncodingConversionOptions { get }     static var ExternalRepresentation: NSStringEncodingConversionOptions { get } } ``` |

Modified NSStringEncodingConversionOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSStringEnumerationOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSStringEnumerationOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var ByLines: NSStringEnumerationOptions { get }     static var ByParagraphs: NSStringEnumerationOptions { get }     static var ByComposedCharacterSequences: NSStringEnumerationOptions { get }     static var ByWords: NSStringEnumerationOptions { get }     static var BySentences: NSStringEnumerationOptions { get }     static var Reverse: NSStringEnumerationOptions { get }     static var SubstringNotRequired: NSStringEnumerationOptions { get }     static var Localized: NSStringEnumerationOptions { get } } ``` |
| To | ``` struct NSStringEnumerationOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var ByLines: NSStringEnumerationOptions { get }     static var ByParagraphs: NSStringEnumerationOptions { get }     static var ByComposedCharacterSequences: NSStringEnumerationOptions { get }     static var ByWords: NSStringEnumerationOptions { get }     static var BySentences: NSStringEnumerationOptions { get }     static var Reverse: NSStringEnumerationOptions { get }     static var SubstringNotRequired: NSStringEnumerationOptions { get }     static var Localized: NSStringEnumerationOptions { get } } ``` |

Modified NSStringEnumerationOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSTextCheckingResult

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSTextCheckingResult.alternativeStrings

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSTextCheckingResult.components

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSTextCheckingResult.correctionCheckingResultWithRange(NSRange, replacementString: String, alternativeStrings:[AnyObject]) -> NSTextCheckingResult [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSTextCheckingResult.numberOfRanges

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSTextCheckingResult.phoneNumber

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSTextCheckingResult.phoneNumberCheckingResultWithRange(NSRange, phoneNumber: String) -> NSTextCheckingResult [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSTextCheckingResult.rangeAtIndex(Int) -> NSRange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSTextCheckingResult.regularExpression

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSTextCheckingResult.regularExpressionCheckingResultWithRanges(NSRangePointer, count: Int, regularExpression: NSRegularExpression) -> NSTextCheckingResult [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSTextCheckingResult.resultByAdjustingRangesWithOffset(Int) -> NSTextCheckingResult

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSTextCheckingResult.transitInformationCheckingResultWithRange(NSRange, components:[NSObject: AnyObject]) -> NSTextCheckingResult [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSTextCheckingType [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSTextCheckingType : RawOptionSetType {     init(_ value: UInt64)     var value: UInt64     static var Orthography: NSTextCheckingType { get }     static var Spelling: NSTextCheckingType { get }     static var Grammar: NSTextCheckingType { get }     static var Date: NSTextCheckingType { get }     static var Address: NSTextCheckingType { get }     static var Link: NSTextCheckingType { get }     static var Quote: NSTextCheckingType { get }     static var Dash: NSTextCheckingType { get }     static var Replacement: NSTextCheckingType { get }     static var Correction: NSTextCheckingType { get }     static var RegularExpression: NSTextCheckingType { get }     static var PhoneNumber: NSTextCheckingType { get }     static var TransitInformation: NSTextCheckingType { get } } ``` |
| To | ``` struct NSTextCheckingType : RawOptionSetType {     init(_ rawValue: UInt64)     init(rawValue rawValue: UInt64)     static var Orthography: NSTextCheckingType { get }     static var Spelling: NSTextCheckingType { get }     static var Grammar: NSTextCheckingType { get }     static var Date: NSTextCheckingType { get }     static var Address: NSTextCheckingType { get }     static var Link: NSTextCheckingType { get }     static var Quote: NSTextCheckingType { get }     static var Dash: NSTextCheckingType { get }     static var Replacement: NSTextCheckingType { get }     static var Correction: NSTextCheckingType { get }     static var RegularExpression: NSTextCheckingType { get }     static var PhoneNumber: NSTextCheckingType { get }     static var TransitInformation: NSTextCheckingType { get } } ``` |

Modified NSTextCheckingType.init(_: UInt64)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt64) ``` |
| To | ``` init(_ rawValue: UInt64) ``` |

Modified NSThread.init()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSThread.callStackReturnAddresses() -> [AnyObject] [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSThread.callStackSymbols() -> [AnyObject] [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSThread.cancel()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSThread.cancelled

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSThread.executing

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSThread.finished

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSThread.isMainThread

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSThread.isMainThread() -> Bool [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSThread.main()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSThread.mainThread() -> NSThread [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSThread.name

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSThread.stackSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSThread.start()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSThread.init(target: AnyObject, selector: Selector, object: AnyObject?)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSThread.threadPriority

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSTimeZone.init(abbreviation: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(abbreviation abbreviation: String) ``` |
| To | ``` convenience init?(abbreviation abbreviation: String) ``` |

Modified NSTimeZone.daylightSavingTimeOffset

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSTimeZone.daylightSavingTimeOffsetForDate(NSDate) -> NSTimeInterval

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSTimeZone.localizedName(NSTimeZoneNameStyle, locale: NSLocale?) -> String?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSTimeZone.init(name: String)

|  | Declaration |
| --- | --- |
| From | ``` init(name tzName: String) ``` |
| To | ``` init?(name tzName: String) ``` |

Modified NSTimeZone.init(name: String, data: NSData?)

|  | Declaration |
| --- | --- |
| From | ``` init(name tzName: String, data aData: NSData?) ``` |
| To | ``` init?(name tzName: String, data aData: NSData?) ``` |

Modified NSTimeZone.nextDaylightSavingTimeTransition

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSTimeZone.nextDaylightSavingTimeTransitionAfterDate(NSDate) -> NSDate?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSTimeZone.setAbbreviationDictionary([NSObject: AnyObject]) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSTimeZone.timeZoneDataVersion() -> String [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSTimer.tolerance

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURL

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying, NSSecureCoding, Reflectable |
| To | AnyObject, NSCoding, NSCopying, NSObjectProtocol, NSSecureCoding, QLPreviewItem, Reflectable |

Modified NSURL.URLByAppendingPathComponent(String) -> NSURL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURL.URLByAppendingPathComponent(String, isDirectory: Bool) -> NSURL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURL.URLByAppendingPathExtension(String) -> NSURL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURL.URLByDeletingLastPathComponent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURL.URLByDeletingPathExtension

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURL.URLByResolvingSymlinksInPath

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURL.URLByStandardizingPath

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURL.bookmarkDataWithContentsOfURL(NSURL, error: NSErrorPointer) -> NSData? [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURL.bookmarkDataWithOptions(NSURLBookmarkCreationOptions, includingResourceValuesForKeys:[AnyObject]?, relativeToURL: NSURL?, error: NSErrorPointer) -> NSData?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURL.init(byResolvingAliasFileAtURL: NSURL, options: NSURLBookmarkResolutionOptions, error: NSErrorPointer)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | URLByResolvingAliasFileAtURL(_:options:error:) | ``` class func URLByResolvingAliasFileAtURL(_ url: NSURL, options options: NSURLBookmarkResolutionOptions, error error: NSErrorPointer) -> Self! ``` | iOS 8.0 |
| To | init(byResolvingAliasFileAtURL:options:error:) | ``` convenience init?(byResolvingAliasFileAtURL url: NSURL, options options: NSURLBookmarkResolutionOptions, error error: NSErrorPointer) ``` | iOS 8.1 |

Modified NSURL.init(byResolvingBookmarkData: NSData, options: NSURLBookmarkResolutionOptions, relativeToURL: NSURL?, bookmarkDataIsStale: UnsafeMutablePointer<ObjCBool>, error: NSErrorPointer)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` convenience init(byResolvingBookmarkData bookmarkData: NSData, options options: NSURLBookmarkResolutionOptions, relativeToURL relativeURL: NSURL?, bookmarkDataIsStale isStale: UnsafeMutablePointer<ObjCBool>, error error: NSErrorPointer) ``` | iOS 8.0 |
| To | ``` convenience init?(byResolvingBookmarkData bookmarkData: NSData, options options: NSURLBookmarkResolutionOptions, relativeToURL relativeURL: NSURL?, bookmarkDataIsStale isStale: UnsafeMutablePointer<ObjCBool>, error error: NSErrorPointer) ``` | iOS 4.0 |

Modified NSURL.checkResourceIsReachableAndReturnError(NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURL.filePathURL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURL.fileReferenceURL() -> NSURL?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURL.fileSystemRepresentation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURL.init(fileURLWithFileSystemRepresentation: UnsafePointer<Int8>, isDirectory: Bool, relativeToURL: NSURL?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(fileURLWithFileSystemRepresentation path: UnsafePointer<Int8>, isDirectory isDir: Bool, relativeToURL baseURL: NSURL?) ``` | iOS 8.0 |
| To | ``` init?(fileURLWithFileSystemRepresentation path: UnsafePointer<Int8>, isDirectory isDir: Bool, relativeToURL baseURL: NSURL?) ``` | iOS 7.0 |

Modified NSURL.fileURLWithFileSystemRepresentation(UnsafePointer<Int8>, isDirectory: Bool, relativeToURL: NSURL?) -> NSURL? [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func fileURLWithFileSystemRepresentation(_ path: UnsafePointer<Int8>, isDirectory isDir: Bool, relativeToURL baseURL: NSURL!) -> NSURL? ``` | iOS 8.0 |
| To | ``` class func fileURLWithFileSystemRepresentation(_ path: UnsafePointer<Int8>, isDirectory isDir: Bool, relativeToURL baseURL: NSURL?) -> NSURL? ``` | iOS 7.0 |

Modified NSURL.init(fileURLWithPath: String)

|  | Declaration |
| --- | --- |
| From | ``` init(fileURLWithPath path: String) ``` |
| To | ``` init?(fileURLWithPath path: String) ``` |

Modified NSURL.init(fileURLWithPath: String, isDirectory: Bool)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(fileURLWithPath path: String, isDirectory isDir: Bool) ``` | iOS 8.0 |
| To | ``` init?(fileURLWithPath path: String, isDirectory isDir: Bool) ``` | iOS 2.0 |

Modified NSURL.fileURLWithPath(String, isDirectory: Bool) -> NSURL? [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSURL.fileURLWithPathComponents([AnyObject]) -> NSURL? [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func fileURLWithPathComponents(_ components: [AnyObject]) -> NSURL! ``` | iOS 8.0 |
| To | ``` class func fileURLWithPathComponents(_ components: [AnyObject]) -> NSURL? ``` | iOS 4.0 |

Modified NSURL.getFileSystemRepresentation(UnsafeMutablePointer<Int8>, maxLength: Int) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURL.getResourceValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey: String, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURL.isFileReferenceURL() -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURL.lastPathComponent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURL.pathComponents

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURL.pathExtension

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURL.removeAllCachedResourceValues()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURL.removeCachedResourceValueForKey(String)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURL.resourceValuesForKeys([AnyObject], error: NSErrorPointer) -> [NSObject: AnyObject]?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURL.resourceValuesForKeys([AnyObject], fromBookmarkData: NSData) -> [NSObject: AnyObject]? [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURL.init(scheme: String, host: String?, path: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(scheme scheme: String, host host: String?, path path: String) ``` |
| To | ``` convenience init?(scheme scheme: String, host host: String?, path path: String) ``` |

Modified NSURL.setResourceValue(AnyObject?, forKey: String, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURL.setResourceValues([NSObject: AnyObject], error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURL.setTemporaryResourceValue(AnyObject?, forKey: String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setTemporaryResourceValue(_ value: AnyObject!, forKey key: String!) ``` | iOS 8.0 |
| To | ``` func setTemporaryResourceValue(_ value: AnyObject?, forKey key: String) ``` | iOS 7.0 |

Modified NSURL.init(string: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(string URLString: String) ``` |
| To | ``` convenience init?(string URLString: String) ``` |

Modified NSURL.init(string: String, relativeToURL: NSURL?)

|  | Declaration |
| --- | --- |
| From | ``` init(string URLString: String, relativeToURL baseURL: NSURL?) ``` |
| To | ``` init?(string URLString: String, relativeToURL baseURL: NSURL?) ``` |

Modified NSURL.writeBookmarkData(NSData, toURL: NSURL, options: NSURLBookmarkFileCreationOptions, error: NSErrorPointer) -> Bool [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLBookmarkCreationOptions [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct NSURLBookmarkCreationOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var PreferFileIDResolution: NSURLBookmarkCreationOptions { get }     static var MinimalBookmark: NSURLBookmarkCreationOptions { get }     static var SuitableForBookmarkFile: NSURLBookmarkCreationOptions { get }     static var WithSecurityScope: NSURLBookmarkCreationOptions { get }     static var SecurityScopeAllowOnlyReadAccess: NSURLBookmarkCreationOptions { get } } ``` | iOS 8.0 |
| To | ``` struct NSURLBookmarkCreationOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var PreferFileIDResolution: NSURLBookmarkCreationOptions { get }     static var MinimalBookmark: NSURLBookmarkCreationOptions { get }     static var SuitableForBookmarkFile: NSURLBookmarkCreationOptions { get }     static var WithSecurityScope: NSURLBookmarkCreationOptions { get }     static var SecurityScopeAllowOnlyReadAccess: NSURLBookmarkCreationOptions { get } } ``` | iOS 4.0 |

Modified NSURLBookmarkCreationOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSURLBookmarkResolutionOptions [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct NSURLBookmarkResolutionOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var WithoutUI: NSURLBookmarkResolutionOptions { get }     static var WithoutMounting: NSURLBookmarkResolutionOptions { get }     static var WithSecurityScope: NSURLBookmarkResolutionOptions { get } } ``` | iOS 8.0 |
| To | ``` struct NSURLBookmarkResolutionOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var WithoutUI: NSURLBookmarkResolutionOptions { get }     static var WithoutMounting: NSURLBookmarkResolutionOptions { get }     static var WithSecurityScope: NSURLBookmarkResolutionOptions { get } } ``` | iOS 4.0 |

Modified NSURLBookmarkResolutionOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSURLComponents

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURLComponents.init(URL: NSURL, resolvingAgainstBaseURL: Bool)

|  | Declaration |
| --- | --- |
| From | ``` init(URL url: NSURL, resolvingAgainstBaseURL resolve: Bool) ``` |
| To | ``` init?(URL url: NSURL, resolvingAgainstBaseURL resolve: Bool) ``` |

Modified NSURLComponents.init(string: String)

|  | Declaration |
| --- | --- |
| From | ``` init(string URLString: String) ``` |
| To | ``` init?(string URLString: String) ``` |

Modified NSURLConnection.currentRequest

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLConnection.originalRequest

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLConnection.init(request: NSURLRequest, delegate: AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` init(request request: NSURLRequest, delegate delegate: AnyObject?) ``` |
| To | ``` init?(request request: NSURLRequest, delegate delegate: AnyObject?) ``` |

Modified NSURLConnection.init(request: NSURLRequest, delegate: AnyObject?, startImmediately: Bool)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(request request: NSURLRequest, delegate delegate: AnyObject?, startImmediately startImmediately: Bool) ``` | iOS 8.0 |
| To | ``` init?(request request: NSURLRequest, delegate delegate: AnyObject?, startImmediately startImmediately: Bool) ``` | iOS 2.0 |

Modified NSURLConnection.scheduleInRunLoop(NSRunLoop, forMode: String)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSURLConnection.sendAsynchronousRequest(NSURLRequest, queue: NSOperationQueue!, completionHandler:(NSURLResponse!, NSData!, NSError!) -> Void) [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func sendAsynchronousRequest(_ request: NSURLRequest, queue queue: NSOperationQueue!, completionHandler handler: ((NSURLResponse!, NSData!, NSError!) -> Void)!) ``` | iOS 8.0 |
| To | ``` class func sendAsynchronousRequest(_ request: NSURLRequest, queue queue: NSOperationQueue!, completionHandler handler: (NSURLResponse!, NSData!, NSError!) -> Void) ``` | iOS 5.0 |

Modified NSURLConnection.setDelegateQueue(NSOperationQueue!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLConnection.start()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSURLConnection.unscheduleFromRunLoop(NSRunLoop, forMode: String)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSURLConnectionDelegate.connection(NSURLConnection, canAuthenticateAgainstProtectionSpace: NSURLProtectionSpace) -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 8.0 |

Modified NSURLConnectionDelegate.connection(NSURLConnection, didCancelAuthenticationChallenge: NSURLAuthenticationChallenge)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSURLConnectionDelegate.connection(NSURLConnection, didReceiveAuthenticationChallenge: NSURLAuthenticationChallenge)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSURLCredential.certificates

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSURLCredential.init(identity: SecIdentity!, certificates:[AnyObject], persistence: NSURLCredentialPersistence)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSURLCredential.init(trust: SecTrust!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSURLCredentialStorage.removeCredential(NSURLCredential, forProtectionSpace: NSURLProtectionSpace, options:[NSObject: AnyObject]?)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURLProtectionSpace.distinguishedNames

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSURLProtectionSpace.serverTrust

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSURLQueryItem.value

|  | Declaration |
| --- | --- |
| From | ``` var value: String { get } ``` |
| To | ``` var value: String? { get } ``` |

Modified NSURLRequest.HTTPShouldUsePipelining

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLRequest.allowsCellularAccess

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSURLRequest.networkServiceType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLSession

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURLSession.dataTaskWithRequest(NSURLRequest, completionHandler:((NSData!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionDataTask

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURLSession.dataTaskWithURL(NSURL, completionHandler:((NSData!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionDataTask

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURLSession.downloadTaskWithRequest(NSURLRequest, completionHandler:((NSURL!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionDownloadTask

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURLSession.downloadTaskWithResumeData(NSData, completionHandler:((NSURL!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionDownloadTask

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURLSession.downloadTaskWithURL(NSURL, completionHandler:((NSURL!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionDownloadTask

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURLSession.uploadTaskWithRequest(NSURLRequest, fromData: NSData?, completionHandler:((NSData!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionUploadTask

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURLSession.uploadTaskWithRequest(NSURLRequest, fromFile: NSURL, completionHandler:((NSData!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionUploadTask

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURLSessionAuthChallengeDisposition [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURLSessionConfiguration

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURLSessionConfiguration.backgroundSessionConfiguration(String) -> NSURLSessionConfiguration [class]

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 8.0 |

Modified NSURLSessionConfiguration.discretionary

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURLSessionConfiguration.sessionSendsLaunchEvents

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURLSessionDelegate.URLSessionDidFinishEventsForBackgroundURLSession(NSURLSession)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURLSessionResponseDisposition [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURLSessionTask

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURLSessionTaskState [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSUUID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSUUID.init(UUIDString: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(UUIDString string: String) ``` |
| To | ``` convenience init?(UUIDString string: String) ``` |

Modified NSUbiquitousKeyValueStore

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSUndoManager

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSUndoManager.redoActionIsDiscardable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSUndoManager.setActionIsDiscardable(Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSUndoManager.undoActionIsDiscardable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSUserDefaults.URLForKey(String) -> NSURL?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSUserDefaults.setURL(NSURL, forKey: String)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSUserDefaults.init(suiteName: String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(suiteName suitename: String) ``` | iOS 8.0 |
| To | ``` init?(suiteName suitename: String) ``` | iOS 7.0 |

Modified NSValueTransformer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSValueTransformer.init(forName: String)

|  | Declaration |
| --- | --- |
| From | ``` init(forName name: String) -> NSValueTransformer ``` |
| To | ``` init?(forName name: String) -> NSValueTransformer ``` |

Modified NSVolumeEnumerationOptions [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct NSVolumeEnumerationOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var SkipHiddenVolumes: NSVolumeEnumerationOptions { get }     static var ProduceFileReferenceURLs: NSVolumeEnumerationOptions { get } } ``` | iOS 8.0 |
| To | ``` struct NSVolumeEnumerationOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var SkipHiddenVolumes: NSVolumeEnumerationOptions { get }     static var ProduceFileReferenceURLs: NSVolumeEnumerationOptions { get } } ``` | iOS 4.0 |

Modified NSVolumeEnumerationOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSXMLParser.init(contentsOfURL: NSURL!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(contentsOfURL url: NSURL!) ``` |
| To | ``` convenience init?(contentsOfURL url: NSURL!) ``` |

Modified NSXMLParser.init(stream: NSInputStream)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSXMLParserDelegate.parser(NSXMLParser!, didEndElement: String!, namespaceURI: String!, qualifiedName: String!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser, didEndElement elementName: String, namespaceURI namespaceURI: String, qualifiedName qName: String) ``` | iOS 8.0 |
| To | ``` optional func parser(_ parser: NSXMLParser!, didEndElement elementName: String!, namespaceURI namespaceURI: String!, qualifiedName qName: String!) ``` | iOS 8.1 |

Modified NSXMLParserDelegate.parser(NSXMLParser!, didEndMappingPrefix: String!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser, didEndMappingPrefix prefix: String) ``` | iOS 8.0 |
| To | ``` optional func parser(_ parser: NSXMLParser!, didEndMappingPrefix prefix: String!) ``` | iOS 8.1 |

Modified NSXMLParserDelegate.parser(NSXMLParser!, didStartElement: String!, namespaceURI: String!, qualifiedName: String!, attributes:[NSObject: AnyObject]!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser, didStartElement elementName: String, namespaceURI namespaceURI: String, qualifiedName qName: String, attributes attributeDict: [NSObject : AnyObject]) ``` | iOS 8.0 |
| To | ``` optional func parser(_ parser: NSXMLParser!, didStartElement elementName: String!, namespaceURI namespaceURI: String!, qualifiedName qName: String!, attributes attributeDict: [NSObject : AnyObject]!) ``` | iOS 8.1 |

Modified NSXMLParserDelegate.parser(NSXMLParser!, didStartMappingPrefix: String!, toURI: String!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser, didStartMappingPrefix prefix: String, toURI namespaceURI: String?) ``` | iOS 8.0 |
| To | ``` optional func parser(_ parser: NSXMLParser!, didStartMappingPrefix prefix: String!, toURI namespaceURI: String!) ``` | iOS 8.1 |

Modified NSXMLParserDelegate.parser(NSXMLParser!, foundAttributeDeclarationWithName: String!, forElement: String!, type: String!, defaultValue: String!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser, foundAttributeDeclarationWithName attributeName: String, forElement elementName: String, type type: String, defaultValue defaultValue: String) ``` | iOS 8.0 |
| To | ``` optional func parser(_ parser: NSXMLParser!, foundAttributeDeclarationWithName attributeName: String!, forElement elementName: String!, type type: String!, defaultValue defaultValue: String!) ``` | iOS 8.1 |

Modified NSXMLParserDelegate.parser(NSXMLParser!, foundCDATA: NSData!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser, foundCDATA CDATABlock: NSData) ``` | iOS 8.0 |
| To | ``` optional func parser(_ parser: NSXMLParser!, foundCDATA CDATABlock: NSData!) ``` | iOS 8.1 |

Modified NSXMLParserDelegate.parser(NSXMLParser!, foundCharacters: String!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser, foundCharacters string: String) ``` | iOS 8.0 |
| To | ``` optional func parser(_ parser: NSXMLParser!, foundCharacters string: String!) ``` | iOS 8.1 |

Modified NSXMLParserDelegate.parser(NSXMLParser!, foundComment: String!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser, foundComment comment: String) ``` | iOS 8.0 |
| To | ``` optional func parser(_ parser: NSXMLParser!, foundComment comment: String!) ``` | iOS 8.1 |

Modified NSXMLParserDelegate.parser(NSXMLParser!, foundElementDeclarationWithName: String!, model: String!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser, foundElementDeclarationWithName elementName: String, model model: String) ``` | iOS 8.0 |
| To | ``` optional func parser(_ parser: NSXMLParser!, foundElementDeclarationWithName elementName: String!, model model: String!) ``` | iOS 8.1 |

Modified NSXMLParserDelegate.parser(NSXMLParser!, foundExternalEntityDeclarationWithName: String!, publicID: String!, systemID: String!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser, foundExternalEntityDeclarationWithName name: String, publicID publicID: String, systemID systemID: String) ``` | iOS 8.0 |
| To | ``` optional func parser(_ parser: NSXMLParser!, foundExternalEntityDeclarationWithName name: String!, publicID publicID: String!, systemID systemID: String!) ``` | iOS 8.1 |

Modified NSXMLParserDelegate.parser(NSXMLParser!, foundIgnorableWhitespace: String!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser, foundIgnorableWhitespace whitespaceString: String) ``` | iOS 8.0 |
| To | ``` optional func parser(_ parser: NSXMLParser!, foundIgnorableWhitespace whitespaceString: String!) ``` | iOS 8.1 |

Modified NSXMLParserDelegate.parser(NSXMLParser!, foundInternalEntityDeclarationWithName: String!, value: String!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser, foundInternalEntityDeclarationWithName name: String, value value: String) ``` | iOS 8.0 |
| To | ``` optional func parser(_ parser: NSXMLParser!, foundInternalEntityDeclarationWithName name: String!, value value: String!) ``` | iOS 8.1 |

Modified NSXMLParserDelegate.parser(NSXMLParser!, foundNotationDeclarationWithName: String!, publicID: String!, systemID: String!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser, foundNotationDeclarationWithName name: String, publicID publicID: String, systemID systemID: String) ``` | iOS 8.0 |
| To | ``` optional func parser(_ parser: NSXMLParser!, foundNotationDeclarationWithName name: String!, publicID publicID: String!, systemID systemID: String!) ``` | iOS 8.1 |

Modified NSXMLParserDelegate.parser(NSXMLParser!, foundProcessingInstructionWithTarget: String!, data: String!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser, foundProcessingInstructionWithTarget target: String, data data: String) ``` | iOS 8.0 |
| To | ``` optional func parser(_ parser: NSXMLParser!, foundProcessingInstructionWithTarget target: String!, data data: String!) ``` | iOS 8.1 |

Modified NSXMLParserDelegate.parser(NSXMLParser!, foundUnparsedEntityDeclarationWithName: String!, publicID: String!, systemID: String!, notationName: String!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser, foundUnparsedEntityDeclarationWithName name: String, publicID publicID: String, systemID systemID: String, notationName notationName: String) ``` | iOS 8.0 |
| To | ``` optional func parser(_ parser: NSXMLParser!, foundUnparsedEntityDeclarationWithName name: String!, publicID publicID: String!, systemID systemID: String!, notationName notationName: String!) ``` | iOS 8.1 |

Modified NSXMLParserDelegate.parser(NSXMLParser!, parseErrorOccurred: NSError!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser, parseErrorOccurred parseError: NSError) ``` | iOS 8.0 |
| To | ``` optional func parser(_ parser: NSXMLParser!, parseErrorOccurred parseError: NSError!) ``` | iOS 8.1 |

Modified NSXMLParserDelegate.parser(NSXMLParser!, resolveExternalEntityName: String!, systemID: String!) -> NSData!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser, resolveExternalEntityName name: String, systemID systemID: String?) -> NSData? ``` | iOS 8.0 |
| To | ``` optional func parser(_ parser: NSXMLParser!, resolveExternalEntityName name: String!, systemID systemID: String!) -> NSData! ``` | iOS 8.1 |

Modified NSXMLParserDelegate.parser(NSXMLParser!, validationErrorOccurred: NSError!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser, validationErrorOccurred validationError: NSError) ``` | iOS 8.0 |
| To | ``` optional func parser(_ parser: NSXMLParser!, validationErrorOccurred validationError: NSError!) ``` | iOS 8.1 |

Modified NSXMLParserDelegate.parserDidEndDocument(NSXMLParser!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parserDidEndDocument(_ parser: NSXMLParser) ``` | iOS 8.0 |
| To | ``` optional func parserDidEndDocument(_ parser: NSXMLParser!) ``` | iOS 8.1 |

Modified NSXMLParserDelegate.parserDidStartDocument(NSXMLParser!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func parserDidStartDocument(_ parser: NSXMLParser) ``` | iOS 8.0 |
| To | ``` optional func parserDidStartDocument(_ parser: NSXMLParser!) ``` | iOS 8.1 |

Modified NSZone [struct]

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` struct NSZone : NilLiteralConvertible {     var pointer: COpaquePointer     init()     static func convertFromNilLiteral() -> NSZone } ``` | Foundation |
| To | ``` struct NSZone : NilLiteralConvertible {     var pointer: COpaquePointer     init()     init(nilLiteral nilLiteral: ()) } ``` | ObjectiveC |

Modified NSZone.init()

|  | Module |
| --- | --- |
| From | Foundation |
| To | ObjectiveC |

Modified NSZone.pointer

|  | Module |
| --- | --- |
| From | Foundation |
| To | ObjectiveC |

Modified NSAssertionHandlerKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSBuddhistCalendar

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSCalendarIdentifierBuddhist

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSCalendarIdentifierChinese

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSCalendarIdentifierCoptic

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSCalendarIdentifierEthiopicAmeteAlem

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSCalendarIdentifierEthiopicAmeteMihret

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSCalendarIdentifierGregorian

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSCalendarIdentifierHebrew

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSCalendarIdentifierISO8601

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSCalendarIdentifierIndian

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSCalendarIdentifierIslamic

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSCalendarIdentifierIslamicCivil

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSCalendarIdentifierJapanese

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSCalendarIdentifierPersian

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSCalendarIdentifierRepublicOfChina

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSChineseCalendar

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSCurrentLocaleDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSExecutableArchitectureMismatchError

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSExecutableErrorMaximum

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSExecutableErrorMinimum

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSExecutableLinkError

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSExecutableLoadError

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSExecutableNotLoadableError

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSExecutableRuntimeMismatchError

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSFeatureUnsupportedError

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSFileProtectionComplete

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileProtectionCompleteUnlessOpen

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSFileProtectionCompleteUntilFirstUserAuthentication

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSFileProtectionKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileProtectionNone

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFileReadTooLargeError

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSFileReadUnknownStringEncodingError

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSFileWriteFileExistsError

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSFileWriteVolumeReadOnlyError

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSGregorianCalendar

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSHashTableCopyIn

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSHashTableObjectPointerPersonality

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSHashTableStrongMemory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSHashTableWeakMemory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSHebrewCalendar

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSISO8601Calendar

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 8.0 |

Modified NSIndianCalendar

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 8.0 |

Modified NSInvocationOperationCancelledException

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSInvocationOperationVoidResultException

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSIsNilTransformerName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSIsNotNilTransformerName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSIslamicCalendar

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSIslamicCivilCalendar

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSJapaneseCalendar

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSKeyValueChangeNotificationIsPriorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSKeyedArchiveRootObjectKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSKeyedUnarchiveFromDataTransformerName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSLinguisticTagAdjective

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagAdverb

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagClassifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagCloseParenthesis

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagCloseQuote

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagConjunction

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagDash

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagDeterminer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagIdiom

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagInterjection

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagNoun

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagNumber

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagOpenParenthesis

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagOpenQuote

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagOrganizationName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagOther

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagOtherPunctuation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagOtherWhitespace

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagOtherWord

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagParagraphBreak

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagParticle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagPersonalName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagPlaceName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagPreposition

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagPronoun

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagPunctuation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagSchemeLanguage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagSchemeLemma

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagSchemeLexicalClass

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagSchemeNameType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagSchemeNameTypeOrLexicalClass

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagSchemeScript

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagSchemeTokenType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagSentenceTerminator

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagVerb

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagWhitespace

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagWord

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLinguisticTagWordJoiner

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSLocaleAlternateQuotationBeginDelimiterKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSLocaleAlternateQuotationEndDelimiterKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSLocaleCollatorIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSLocaleQuotationBeginDelimiterKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSLocaleQuotationEndDelimiterKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSMapTableCopyIn

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSMapTableObjectPointerPersonality

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSMapTableStrongMemory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSMapTableWeakMemory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSMetadataItemDisplayNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMetadataItemFSContentChangeDateKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMetadataItemFSCreationDateKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMetadataItemFSNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMetadataItemFSSizeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMetadataItemIsUbiquitousKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMetadataItemPathKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMetadataItemURLKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMetadataQueryDidFinishGatheringNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMetadataQueryDidStartGatheringNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMetadataQueryDidUpdateNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMetadataQueryGatheringProgressNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMetadataQueryResultContentRelevanceAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMetadataQueryUbiquitousDataScope

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMetadataQueryUbiquitousDocumentsScope

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMetadataUbiquitousItemDownloadingErrorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSMetadataUbiquitousItemDownloadingStatusCurrent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSMetadataUbiquitousItemDownloadingStatusDownloaded

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSMetadataUbiquitousItemDownloadingStatusKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSMetadataUbiquitousItemDownloadingStatusNotDownloaded

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSMetadataUbiquitousItemHasUnresolvedConflictsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMetadataUbiquitousItemIsDownloadingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMetadataUbiquitousItemIsUploadedKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMetadataUbiquitousItemIsUploadingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMetadataUbiquitousItemPercentDownloadedKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMetadataUbiquitousItemPercentUploadedKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMetadataUbiquitousItemUploadingErrorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSNegateBooleanTransformerName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSPersianCalendar

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 8.0 |

Modified NSPointerFunctionsCStringPersonality

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSPointerFunctionsCopyIn

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSPointerFunctionsIntegerPersonality

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSPointerFunctionsMachVirtualMemory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSPointerFunctionsMallocMemory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSPointerFunctionsObjectPersonality

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSPointerFunctionsObjectPointerPersonality

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSPointerFunctionsOpaqueMemory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSPointerFunctionsOpaquePersonality

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSPointerFunctionsStrongMemory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSPointerFunctionsStructPersonality

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSPointerFunctionsWeakMemory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSProgressEstimatedTimeRemainingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSProgressFileCompletedCountKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSProgressFileOperationKindCopying

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSProgressFileOperationKindDecompressingAfterDownloading

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSProgressFileOperationKindDownloading

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSProgressFileOperationKindKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSProgressFileOperationKindReceiving

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSProgressFileTotalCountKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSProgressFileURLKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSProgressKindFile

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSProgressThroughputKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSPropertyListErrorMaximum

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSPropertyListErrorMinimum

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSPropertyListReadCorruptError

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSPropertyListReadStreamError

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSPropertyListReadUnknownVersionError

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSPropertyListWriteStreamError

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSProtocolFromString(String!) -> Protocol!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSRepublicOfChinaCalendar

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 8.0 |

Modified NSRunLoopCommonModes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSStreamDataWrittenToMemoryStreamKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSStreamFileCurrentOffsetKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSStreamNetworkServiceType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSStreamNetworkServiceTypeBackground

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSStreamNetworkServiceTypeVideo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSStreamNetworkServiceTypeVoIP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSStreamNetworkServiceTypeVoice

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSStreamSOCKSErrorDomain

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSStreamSOCKSProxyConfigurationKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSStreamSOCKSProxyHostKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSStreamSOCKSProxyPasswordKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSStreamSOCKSProxyPortKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSStreamSOCKSProxyUserKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSStreamSOCKSProxyVersion4

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSStreamSOCKSProxyVersion5

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSStreamSOCKSProxyVersionKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSStreamSocketSSLErrorDomain

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSStreamSocketSecurityLevelKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSStreamSocketSecurityLevelNegotiatedSSL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSStreamSocketSecurityLevelNone

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSStreamSocketSecurityLevelSSLv2

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSStreamSocketSecurityLevelSSLv3

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSStreamSocketSecurityLevelTLSv1

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSStringFromProtocol(Protocol!) -> String!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSSystemClockDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSSystemTimeZoneDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSTextCheckingAirlineKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSTextCheckingCityKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSTextCheckingCountryKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSTextCheckingFlightKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSTextCheckingJobTitleKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSTextCheckingNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSTextCheckingOrganizationKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSTextCheckingPhoneKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSTextCheckingStateKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSTextCheckingStreetKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSTextCheckingZIPKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLAttributeModificationDateKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLAuthenticationMethodClientCertificate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSURLAuthenticationMethodNTLM

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSURLAuthenticationMethodNegotiate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSURLAuthenticationMethodServerTrust

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSURLContentAccessDateKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLContentModificationDateKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLCreationDateKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLCredentialStorageRemoveSynchronizableCredentials

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURLCustomIconKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLEffectiveIconKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLErrorCallIsActive

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSURLErrorDataLengthExceedsMaximum

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSURLErrorDataNotAllowed

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSURLErrorFailingURLErrorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLErrorFailingURLPeerTrustErrorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLErrorFailingURLStringErrorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLErrorInternationalRoamingOff

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSURLErrorRequestBodyStreamExhausted

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSURLFileAllocatedSizeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLFileResourceIdentifierKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLFileResourceTypeBlockSpecial

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLFileResourceTypeCharacterSpecial

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLFileResourceTypeDirectory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLFileResourceTypeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLFileResourceTypeNamedPipe

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLFileResourceTypeRegular

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLFileResourceTypeSocket

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLFileResourceTypeSymbolicLink

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLFileResourceTypeUnknown

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLFileSecurityKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLFileSizeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLHasHiddenExtensionKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLIsAliasFileKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLIsDirectoryKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLIsExcludedFromBackupKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.1 |

Modified NSURLIsExecutableKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLIsHiddenKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLIsMountTriggerKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLIsPackageKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLIsReadableKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLIsRegularFileKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLIsSymbolicLinkKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLIsSystemImmutableKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLIsUbiquitousItemKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLIsUserImmutableKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLIsVolumeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLIsWritableKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLKeysOfUnsetValuesKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLLabelColorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLLabelNumberKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLLinkCountKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLLocalizedLabelKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLLocalizedNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLLocalizedTypeDescriptionKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLParentDirectoryURLKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLPathKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSURLPreferredIOBlockSizeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLProtectionSpaceFTP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSURLProtectionSpaceHTTP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSURLProtectionSpaceHTTPS

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSURLSessionDownloadTaskResumeData

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURLSessionTransferSizeUnknown

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURLTotalFileAllocatedSizeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLTotalFileSizeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLTypeIdentifierKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLUbiquitousItemDownloadingErrorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURLUbiquitousItemDownloadingStatusCurrent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURLUbiquitousItemDownloadingStatusDownloaded

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURLUbiquitousItemDownloadingStatusKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURLUbiquitousItemDownloadingStatusNotDownloaded

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURLUbiquitousItemHasUnresolvedConflictsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLUbiquitousItemIsDownloadingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLUbiquitousItemIsUploadedKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLUbiquitousItemIsUploadingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLUbiquitousItemUploadingErrorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSURLVolumeAvailableCapacityKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLVolumeCreationDateKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLVolumeIdentifierKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLVolumeIsAutomountedKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLVolumeIsBrowsableKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLVolumeIsEjectableKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLVolumeIsInternalKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLVolumeIsJournalingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLVolumeIsLocalKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLVolumeIsReadOnlyKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLVolumeIsRemovableKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLVolumeLocalizedFormatDescriptionKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLVolumeLocalizedNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLVolumeMaximumFileSizeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLVolumeNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLVolumeResourceCountKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLVolumeSupportsAdvisoryFileLockingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLVolumeSupportsCasePreservedNamesKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLVolumeSupportsCaseSensitiveNamesKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLVolumeSupportsExtendedSecurityKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLVolumeSupportsHardLinksKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLVolumeSupportsJournalingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLVolumeSupportsPersistentIDsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLVolumeSupportsRenamingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLVolumeSupportsRootDirectoryDatesKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLVolumeSupportsSparseFilesKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLVolumeSupportsSymbolicLinksKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLVolumeSupportsVolumeSizesKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLVolumeSupportsZeroRunsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLVolumeTotalCapacityKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLVolumeURLForRemountingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSURLVolumeURLKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSURLVolumeUUIDStringKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSUbiquitousFileErrorMaximum

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSUbiquitousFileErrorMinimum

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSUbiquitousFileNotUploadedDueToQuotaError

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSUbiquitousFileUbiquityServerNotAvailable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSUbiquitousFileUnavailableError

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSUbiquitousKeyValueStoreAccountChange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSUbiquitousKeyValueStoreChangeReasonKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSUbiquitousKeyValueStoreChangedKeysKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSUbiquitousKeyValueStoreDidChangeExternallyNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSUbiquitousKeyValueStoreInitialSyncChange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSUbiquitousKeyValueStoreQuotaViolationChange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSUbiquitousKeyValueStoreServerChange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSUbiquityIdentityDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSUnarchiveFromDataTransformerName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSUndefinedDateComponent

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSUndoManagerCheckpointNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSUndoManagerDidCloseUndoGroupNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSUndoManagerDidOpenUndoGroupNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSUndoManagerDidRedoChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSUndoManagerDidUndoChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSUndoManagerGroupIsDiscardableKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSUndoManagerWillCloseUndoGroupNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSUndoManagerWillRedoChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSUndoManagerWillUndoChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSWrapCalendarComponents

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified NSXMLParserErrorDomain

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NSXPCConnectionErrorMaximum

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSXPCConnectionErrorMinimum

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSXPCConnectionInterrupted

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSXPCConnectionInvalid

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSXPCConnectionReplyInvalid

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

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
