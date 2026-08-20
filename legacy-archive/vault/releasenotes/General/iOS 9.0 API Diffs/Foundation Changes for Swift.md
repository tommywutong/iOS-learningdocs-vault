---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/Foundation.html
archived_at: '2026-07-18T02:56:49.075402Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# Foundation Changes for Swift

### Foundation

Removed Array.init(_fromNSArray: NSArray, noCopy: Bool)Removed Index.advancedBy(_: Int) -> String.UTF16View.IndexRemoved Index.distanceTo(_: String.UTF16View.Index) -> IntRemoved Index.init(_: Int)Removed NSActivityOptions.init(_: UInt64)Removed NSArray.getMirror() -> MirrorTypeRemoved NSAttributedStringEnumerationOptions.init(_: UInt)Removed NSBinarySearchingOptions.init(_: UInt)Removed NSByteCountFormatterUnits.init(_: UInt)Removed NSCalendarOptions.init(_: UInt)Removed NSCalendarUnit.init(_: UInt)Removed NSCoder.decodeObjectOfClass(_: AnyClass, forKey: String) -> AnyObject?Removed NSCoder.decodeObjectOfClasses(_: Set<NSObject>, forKey: String) -> AnyObject?Removed NSComparisonPredicateOptions.init(_: UInt)Removed NSDataBase64DecodingOptions.init(_: UInt)Removed NSDataBase64EncodingOptions.init(_: UInt)Removed NSDataReadingOptions.init(_: UInt)Removed NSDataSearchOptions.init(_: UInt)Removed NSDataWritingOptions.init(_: UInt)Removed NSDate.getMirror() -> MirrorTypeRemoved NSDateComponentsFormatterZeroFormattingBehavior.init(_: UInt)Removed NSDictionary.getMirror() -> MirrorTypeRemoved NSDictionary.init(objectsAndKeys: AnyObject)Removed NSDirectoryEnumerationOptions.init(_: UInt)Removed NSEnumerationOptions.init(_: UInt)Removed NSFastGenerator.countRemoved NSFastGenerator.enumerableRemoved NSFastGenerator.nRemoved NSFastGenerator.objectsRemoved NSFastGenerator.refresh()Removed NSFastGenerator.STACK_BUF_SIZERemoved NSFastGenerator.stateRemoved NSFastGenerator.ObjectsBuffer [struct]Removed NSFastGenerator.ObjectsBuffer.bufRemoved NSFileCoordinatorReadingOptions.init(_: UInt)Removed NSFileCoordinatorWritingOptions.init(_: UInt)Removed NSFileManagerItemReplacementOptions.init(_: UInt)Removed NSFileVersionAddingOptions.init(_: UInt)Removed NSFileVersionReplacingOptions.init(_: UInt)Removed NSFileWrapperReadingOptions.init(_: UInt)Removed NSFileWrapperWritingOptions.init(_: UInt)Removed NSIndexSetGenerator.init(set: NSIndexSet)Removed NSJSONReadingOptions.init(_: UInt)Removed NSJSONWritingOptions.init(_: UInt)Removed NSKeyedArchiver.setRequiresSecureCoding(_: Bool)Removed NSKeyedUnarchiver.setRequiresSecureCoding(_: Bool)Removed NSKeyValueObservingOptions.init(_: UInt)Removed NSLinguisticTaggerOptions.init(_: UInt)Removed NSMatchingFlags.init(_: UInt)Removed NSMatchingOptions.init(_: UInt)Removed NSMutableArray.subscript() -> AnyObjectRemoved NSMutableDictionary.subscript() -> AnyObject?Removed NSMutableOrderedSet.subscript() -> AnyObjectRemoved NSNetServiceOptions.init(_: UInt)Removed NSObject.encode() -> [Word]Removed NSObject.hashValueRemoved NSOrderedSet.init(orderedSet: NSOrderedSet?)Removed NSOrderedSet.init(set: Set<NSObject>?)Removed NSOrderedSet.init(set: Set<NSObject>?, copyItems: Bool)Removed NSPropertyListMutabilityOptions.init(_: UInt)Removed NSProxy.dealloc()Removed NSRange.getMirror() -> MirrorTypeRemoved NSRegularExpressionOptions.init(_: UInt)Removed NSSearchPathDomainMask.init(_: UInt)Removed NSSet.getMirror() -> MirrorTypeRemoved NSSortOptions.init(_: UInt)Removed NSStreamEvent.init(_: UInt)Removed NSString.getMirror() -> MirrorTypeRemoved NSStringCompareOptions.init(_: UInt)Removed NSStringEncodingConversionOptions.init(_: UInt)Removed NSStringEnumerationOptions.init(_: UInt)Removed NSTextCheckingType.init(_: UInt64)Removed NSURL.getMirror() -> MirrorTypeRemoved NSURLBookmarkCreationOptions.init(_: UInt)Removed NSURLBookmarkResolutionOptions.init(_: UInt)Removed NSValue.pointerValue() -> UnsafeMutablePointer<Void>Removed NSVolumeEnumerationOptions.init(_: UInt)Removed String.compare(_: String, options: NSStringCompareOptions, range: Range<String.Index>?, locale: NSLocale?) -> NSComparisonResultRemoved String.enumerateLinguisticTagsInRange(_: Range<String.Index>, scheme: String, options: NSLinguisticTaggerOptions, orthography: NSOrthography?, _: (String, Range<String.Index>, Range<String.Index>, inout Bool) -> ())Removed String.enumerateSubstringsInRange(_: Range<String.Index>, options: NSStringEnumerationOptions, _: (substring: String, substringRange: Range<String.Index>, enclosingRange: Range<String.Index>, inout Bool) -> ())Removed String.fileSystemRepresentation() -> [CChar]Removed String.getBytes(_: [UInt8], maxLength: Int, usedLength: UnsafeMutablePointer<Int>, encoding: NSStringEncoding, options: NSStringEncodingConversionOptions, range: Range<String.Index>, remainingRange: UnsafeMutablePointer<Range<String.Index>>) -> BoolRemoved String.getFileSystemRepresentation(_: [CChar], maxLength: Int) -> BoolRemoved String.getLineStart(_: UnsafeMutablePointer<String.Index>, end: UnsafeMutablePointer<String.Index>, contentsEnd: UnsafeMutablePointer<String.Index>, forRange: Range<String.Index>)Removed String.getParagraphStart(_: UnsafeMutablePointer<String.Index>, end: UnsafeMutablePointer<String.Index>, contentsEnd: UnsafeMutablePointer<String.Index>, forRange: Range<String.Index>)Removed String.init(contentsOfFile: String, encoding: NSStringEncoding, error: NSErrorPointer)Removed String.init(contentsOfFile: String, usedEncoding: UnsafeMutablePointer<NSStringEncoding>, error: NSErrorPointer)Removed String.init(contentsOfURL: NSURL, encoding: NSStringEncoding, error: NSErrorPointer)Removed String.init(contentsOfURL: NSURL, usedEncoding: UnsafeMutablePointer<NSStringEncoding>, error: NSErrorPointer)Removed String.lastPathComponentRemoved String.lineRangeForRange(_: Range<String.Index>) -> Range<String.Index>Removed String.linguisticTagsInRange(_: Range<String.Index>, scheme: String, options: NSLinguisticTaggerOptions, orthography: NSOrthography?, tokenRanges: UnsafeMutablePointer<[Range<String.Index>]>) -> [String]Removed String.lowercaseStringWithLocale(_: NSLocale) -> StringRemoved String.paragraphRangeForRange(_: Range<String.Index>) -> Range<String.Index>Removed String.pathComponentsRemoved String.pathExtensionRemoved String.pathWithComponents(_: [String]) -> String [static]Removed String.rangeOfCharacterFromSet(_: NSCharacterSet, options: NSStringCompareOptions, range: Range<String.Index>?) -> Range<String.Index>?Removed String.rangeOfComposedCharacterSequenceAtIndex(_: String.Index) -> Range<String.Index>Removed String.rangeOfComposedCharacterSequencesForRange(_: Range<String.Index>) -> Range<String.Index>Removed String.rangeOfString(_: String, options: NSStringCompareOptions, range: Range<String.Index>?, locale: NSLocale?) -> Range<String.Index>?Removed String.stringByAbbreviatingWithTildeInPathRemoved String.stringByAppendingPathComponent(_: String) -> StringRemoved String.stringByAppendingPathExtension(_: String) -> String?Removed String.stringByDeletingLastPathComponentRemoved String.stringByDeletingPathExtensionRemoved String.stringByExpandingTildeInPathRemoved String.stringByFoldingWithOptions(_: NSStringCompareOptions, locale: NSLocale) -> StringRemoved String.stringByReplacingCharactersInRange(_: Range<String.Index>, withString: String) -> StringRemoved String.stringByReplacingOccurrencesOfString(_: String, withString: String, options: NSStringCompareOptions, range: Range<String.Index>?) -> StringRemoved String.stringByResolvingSymlinksInPathRemoved String.stringByStandardizingPathRemoved String.stringsByAppendingPaths(_: [String]) -> [String]Removed String.substringFromIndex(_: String.Index) -> StringRemoved String.substringToIndex(_: String.Index) -> StringRemoved String.substringWithRange(_: Range<String.Index>) -> StringRemoved String.uppercaseStringWithLocale(_: NSLocale) -> StringRemoved String.writeToFile(_: String, atomically: Bool, encoding: NSStringEncoding, error: NSErrorPointer) -> BoolRemoved String.writeToURL(_: NSURL, atomically: Bool, encoding: NSStringEncoding, error: NSErrorPointer) -> BoolRemoved ==(_: NSObject, _: NSObject) -> BoolRemoved NSDefaultMallocZone() -> NSZoneRemoved NSMachPortDeallocateNoneRemoved NSMachPortDeallocateReceiveRightRemoved NSMachPortDeallocateSendRightRemoved NSPointerFunctionsCopyInRemoved NSPointerFunctionsCStringPersonalityRemoved NSPointerFunctionsIntegerPersonalityRemoved NSPointerFunctionsMachVirtualMemoryRemoved NSPointerFunctionsMallocMemoryRemoved NSPointerFunctionsObjectPersonalityRemoved NSPointerFunctionsObjectPointerPersonalityRemoved NSPointerFunctionsOpaqueMemoryRemoved NSPointerFunctionsOpaquePersonalityRemoved NSPointerFunctionsOptionsRemoved NSPointerFunctionsStrongMemoryRemoved NSPointerFunctionsStructPersonalityRemoved NSPointerFunctionsWeakMemoryAdded [NSBundle.preservationPriorityForTag(_: String) -> Double](https://developer.apple.com/documentation/foundation/nsbundle/1614839-preservationpriorityfortag)Added [NSBundle.setPreservationPriority(_: Double, forTags: Set<String>)](https://developer.apple.com/documentation/foundation/nsbundle/1614845-setpreservationpriority)Added [NSBundleResourceRequest](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest)Added [NSBundleResourceRequest.beginAccessingResourcesWithCompletionHandler(_: (NSError?) -> Void)](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614840-beginaccessingresources)Added [NSBundleResourceRequest.bundle](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614844-bundle)Added [NSBundleResourceRequest.conditionallyBeginAccessingResourcesWithCompletionHandler(_: (Bool) -> Void)](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614834-conditionallybeginaccessingresou)Added [NSBundleResourceRequest.endAccessingResources()](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614843-endaccessingresources)Added [NSBundleResourceRequest.init(tags: Set<String>)](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614837-initwithtags)Added [NSBundleResourceRequest.init(tags: Set<String>, bundle: NSBundle)](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614842-init)Added [NSBundleResourceRequest.loadingPriority](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614841-loadingpriority)Added [NSBundleResourceRequest.progress](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614838-progress)Added [NSBundleResourceRequest.tags](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614833-tags)Added NSCocoaError [struct]Added NSCocoaError.CoderReadCorruptErrorAdded NSCocoaError.CoderValueNotFoundErrorAdded NSCocoaError.ExecutableArchitectureMismatchErrorAdded NSCocoaError.ExecutableLinkErrorAdded NSCocoaError.ExecutableLoadErrorAdded NSCocoaError.ExecutableNotLoadableErrorAdded NSCocoaError.ExecutableRuntimeMismatchErrorAdded NSCocoaError.FeatureUnsupportedErrorAdded NSCocoaError.FileLockingErrorAdded NSCocoaError.FileNoSuchFileErrorAdded NSCocoaError.FileReadCorruptFileErrorAdded NSCocoaError.FileReadInapplicableStringEncodingErrorAdded NSCocoaError.FileReadInvalidFileNameErrorAdded NSCocoaError.FileReadNoPermissionErrorAdded NSCocoaError.FileReadNoSuchFileErrorAdded NSCocoaError.FileReadTooLargeErrorAdded NSCocoaError.FileReadUnknownErrorAdded NSCocoaError.FileReadUnknownStringEncodingErrorAdded NSCocoaError.FileReadUnsupportedSchemeErrorAdded NSCocoaError.FileWriteFileExistsErrorAdded NSCocoaError.FileWriteInapplicableStringEncodingErrorAdded NSCocoaError.FileWriteInvalidFileNameErrorAdded NSCocoaError.FileWriteNoPermissionErrorAdded NSCocoaError.FileWriteOutOfSpaceErrorAdded NSCocoaError.FileWriteUnknownErrorAdded NSCocoaError.FileWriteUnsupportedSchemeErrorAdded NSCocoaError.FileWriteVolumeReadOnlyErrorAdded NSCocoaError.FormattingErrorAdded NSCocoaError.init(rawValue: Int)Added NSCocoaError.isCoderErrorAdded NSCocoaError.isExecutableErrorAdded NSCocoaError.isFileErrorAdded NSCocoaError.isFormattingErrorAdded NSCocoaError.isPropertyListErrorAdded NSCocoaError.isUbiquitousFileErrorAdded NSCocoaError.isUserActivityErrorAdded NSCocoaError.isValidationErrorAdded NSCocoaError.isXPCConnectionErrorAdded NSCocoaError.KeyValueValidationErrorAdded NSCocoaError.PropertyListReadCorruptErrorAdded NSCocoaError.PropertyListReadStreamErrorAdded NSCocoaError.PropertyListReadUnknownVersionErrorAdded NSCocoaError.PropertyListWriteInvalidErrorAdded NSCocoaError.PropertyListWriteStreamErrorAdded NSCocoaError.rawValueAdded NSCocoaError.UbiquitousFileNotUploadedDueToQuotaErrorAdded NSCocoaError.UbiquitousFileUbiquityServerNotAvailableAdded NSCocoaError.UbiquitousFileUnavailableErrorAdded NSCocoaError.UserActivityConnectionUnavailableErrorAdded NSCocoaError.UserActivityHandoffFailedErrorAdded NSCocoaError.UserActivityHandoffUserInfoTooLargeErrorAdded NSCocoaError.UserActivityRemoteApplicationTimedOutErrorAdded NSCocoaError.UserCancelledErrorAdded NSCocoaError.XPCConnectionInterruptedAdded NSCocoaError.XPCConnectionInvalidAdded NSCocoaError.XPCConnectionReplyInvalidAdded NSCoder.decodeObjectOfClass<DecodedObjectType : NSCoding where DecodedObjectType : NSObject>(_: DecodedObjectType.Type, forKey: String) -> DecodedObjectType?Added NSCoder.decodeObjectOfClasses(_: NSSet?, forKey: String) -> AnyObject?Added NSCoder.decodeTopLevelObject() throws -> AnyObject?Added NSCoder.decodeTopLevelObjectForKey(_: String) throws -> AnyObject?Added NSCoder.decodeTopLevelObjectOfClass<DecodedObjectType : NSCoding where DecodedObjectType : NSObject>(_: DecodedObjectType.Type, forKey: String) throws -> DecodedObjectType?Added NSCoder.decodeTopLevelObjectOfClasses(_: NSSet?, forKey: String) throws -> AnyObject?Added [NSCoder.failWithError(_: NSError)](https://developer.apple.com/documentation/foundation/nscoder/1411455-failwitherror)Added [NSComparisonPredicate.init(coder: NSCoder)](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/1417900-init)Added [NSCompoundPredicate.init(coder: NSCoder)](https://developer.apple.com/documentation/foundation/nscompoundpredicate/1417889-initwithcoder)Added [NSDictionary.getObjects(_: AutoreleasingUnsafeMutablePointer<AnyObject?>, andKeys: AutoreleasingUnsafeMutablePointer<AnyObject?>, count: Int)](https://developer.apple.com/documentation/foundation/nsdictionary/1409973-getobjects)Added [NSError.setUserInfoValueProviderForDomain(_: String, provider: ((NSError, String) -> AnyObject?)?) [class]](https://developer.apple.com/documentation/foundation/nserror/1408064-setuserinfovalueprovider)Added [NSError.userInfoValueProviderForDomain(_: String) -> ((NSError, String) -> AnyObject?)? [class]](https://developer.apple.com/documentation/foundation/nserror/1413427-userinfovalueprovider)Added [NSExpression.falseExpression](https://developer.apple.com/documentation/foundation/nsexpression/1416488-false)Added [NSExpression.init(coder: NSCoder)](https://developer.apple.com/documentation/foundation/nsexpression/1415409-initwithcoder)Added [NSExpression.init(forConditional: NSPredicate, trueExpression: NSExpression, falseExpression: NSExpression)](https://developer.apple.com/documentation/foundation/nsexpression/1418004-expressionforconditional)Added [NSExpression.trueExpression](https://developer.apple.com/documentation/foundation/nsexpression/1411874-true)Added [NSExpressionType.ConditionalExpressionType](https://developer.apple.com/documentation/foundation/nsexpressiontype/nsconditionalexpressiontype)Added [NSHTTPCookieStorage.sharedCookieStorageForGroupContainerIdentifier(_: String) -> NSHTTPCookieStorage [class]](https://developer.apple.com/documentation/foundation/nshttpcookiestorage/1411361-sharedcookiestorageforgroupconta)Added [NSIndexPath.getIndexes(_: UnsafeMutablePointer<Int>, range: NSRange)](https://developer.apple.com/documentation/foundation/nsindexpath/1413360-getindexes)Added [NSItemProviderErrorCode.UnavailableCoercionError](https://developer.apple.com/documentation/foundation/nsitemprovider/errorcode/unavailablecoercionerror)Added [NSKeyedArchiver.requiresSecureCoding](https://developer.apple.com/documentation/foundation/nskeyedarchiver/1417084-requiressecurecoding)Added [NSKeyedUnarchiver.requiresSecureCoding](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/1410824-requiressecurecoding)Added NSKeyedUnarchiver.unarchiveTopLevelObjectWithData(_: NSData) throws -> AnyObject? [class]Added [NSMachPortOptions [struct]](https://developer.apple.com/documentation/foundation/nsmachport/options)Added [NSMachPortOptions.DeallocateNone](https://developer.apple.com/documentation/foundation/nsmachportoptions/nsmachportdeallocatenone)Added [NSMachPortOptions.DeallocateReceiveRight](https://developer.apple.com/documentation/foundation/nsmachport/options/1399505-deallocatereceiveright)Added [NSMachPortOptions.DeallocateSendRight](https://developer.apple.com/documentation/foundation/nsmachport/options/1399490-deallocatesendright)Added NSMachPortOptions.init(rawValue: UInt)Added [NSMutableString.applyTransform(_: String, reverse: Bool, range: NSRange, updatedRange: NSRangePointer) -> Bool](https://developer.apple.com/documentation/foundation/nsmutablestring/1415742-applytransform)Added NSNotificationCoalescing.init(rawValue: UInt)Added [NSNumberFormatterStyle.CurrencyAccountingStyle](https://developer.apple.com/documentation/foundation/numberformatter/style/currencyaccounting)Added [NSNumberFormatterStyle.CurrencyISOCodeStyle](https://developer.apple.com/documentation/foundation/nsnumberformatterstyle/nsnumberformattercurrencyisocodestyle)Added [NSNumberFormatterStyle.CurrencyPluralStyle](https://developer.apple.com/documentation/foundation/numberformatter/style/currencyplural)Added [NSNumberFormatterStyle.OrdinalStyle](https://developer.apple.com/documentation/foundation/numberformatter/style/ordinal)Added [NSObject.performSelector(_: Selector, onThread: NSThread, withObject: AnyObject?, waitUntilDone: Bool)](https://developer.apple.com/documentation/objectivec/nsobject/1414476-performselector)Added [NSObject.performSelector(_: Selector, onThread: NSThread, withObject: AnyObject?, waitUntilDone: Bool, modes: [String]?)](https://developer.apple.com/documentation/objectivec/nsobject/1417922-performselector)Added [NSObject.performSelector(_: Selector, withObject: AnyObject?, afterDelay: NSTimeInterval)](https://developer.apple.com/documentation/objectivec/nsobject/1416176-performselector)Added [NSObject.performSelector(_: Selector, withObject: AnyObject?, afterDelay: NSTimeInterval, inModes: [String])](https://developer.apple.com/documentation/objectivec/nsobject/1415652-perform)Added [NSObject.performSelectorInBackground(_: Selector, withObject: AnyObject?)](https://developer.apple.com/documentation/objectivec/nsobject/1412390-performselectorinbackground)Added [NSObject.performSelectorOnMainThread(_: Selector, withObject: AnyObject?, waitUntilDone: Bool)](https://developer.apple.com/documentation/objectivec/nsobject/1414900-performselector)Added [NSObject.performSelectorOnMainThread(_: Selector, withObject: AnyObject?, waitUntilDone: Bool, modes: [String]?)](https://developer.apple.com/documentation/objectivec/nsobject/1411637-performselector)Added [NSPersonNameComponents](https://developer.apple.com/documentation/foundation/nspersonnamecomponents)Added [NSPersonNameComponents.familyName](https://developer.apple.com/documentation/foundation/nspersonnamecomponents/1413354-familyname)Added [NSPersonNameComponents.givenName](https://developer.apple.com/documentation/foundation/nspersonnamecomponents/1407259-givenname)Added [NSPersonNameComponents.middleName](https://developer.apple.com/documentation/foundation/nspersonnamecomponents/1418183-middlename)Added [NSPersonNameComponents.namePrefix](https://developer.apple.com/documentation/foundation/nspersonnamecomponents/1410275-nameprefix)Added [NSPersonNameComponents.nameSuffix](https://developer.apple.com/documentation/foundation/nspersonnamecomponents/1410776-namesuffix)Added [NSPersonNameComponents.nickname](https://developer.apple.com/documentation/foundation/nspersonnamecomponents/1414892-nickname)Added [NSPersonNameComponents.phoneticRepresentation](https://developer.apple.com/documentation/foundation/nspersonnamecomponents/1412193-phoneticrepresentation)Added [NSPersonNameComponentsFormatter](https://developer.apple.com/documentation/foundation/nspersonnamecomponentsformatter)Added [NSPersonNameComponentsFormatter.annotatedStringFromPersonNameComponents(_: NSPersonNameComponents) -> NSAttributedString](https://developer.apple.com/documentation/foundation/nspersonnamecomponentsformatter/1408241-annotatedstringfrompersonnamecom)Added [NSPersonNameComponentsFormatter.getObjectValue(_: AutoreleasingUnsafeMutablePointer<AnyObject?>, forString: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool](https://developer.apple.com/documentation/foundation/nspersonnamecomponentsformatter/1408262-getobjectvalue)Added [NSPersonNameComponentsFormatter.localizedStringFromPersonNameComponents(_: NSPersonNameComponents, style: NSPersonNameComponentsFormatterStyle, options: NSPersonNameComponentsFormatterOptions) -> String [class]](https://developer.apple.com/documentation/foundation/nspersonnamecomponentsformatter/1408258-localizedstringfrompersonnamecom)Added [NSPersonNameComponentsFormatter.phonetic](https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/1408242-isphonetic)Added [NSPersonNameComponentsFormatter.stringFromPersonNameComponents(_: NSPersonNameComponents) -> String](https://developer.apple.com/documentation/foundation/nspersonnamecomponentsformatter/1408243-stringfrompersonnamecomponents)Added [NSPersonNameComponentsFormatter.style](https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/1408260-style)Added [NSPersonNameComponentsFormatterOptions [struct]](https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/options)Added NSPersonNameComponentsFormatterOptions.init(rawValue: UInt)Added [NSPersonNameComponentsFormatterOptions.Phonetic](https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/options/1408240-phonetic)Added [NSPersonNameComponentsFormatterStyle [enum]](https://developer.apple.com/documentation/foundation/nspersonnamecomponentsformatterstyle)Added [NSPersonNameComponentsFormatterStyle.Abbreviated](https://developer.apple.com/documentation/foundation/nspersonnamecomponentsformatterstyle/nspersonnamecomponentsformatterstyleabbreviated)Added [NSPersonNameComponentsFormatterStyle.Default](https://developer.apple.com/documentation/foundation/nspersonnamecomponentsformatterstyle/nspersonnamecomponentsformatterstyledefault)Added [NSPersonNameComponentsFormatterStyle.Long](https://developer.apple.com/documentation/foundation/nspersonnamecomponentsformatterstyle/nspersonnamecomponentsformatterstylelong)Added [NSPersonNameComponentsFormatterStyle.Medium](https://developer.apple.com/documentation/foundation/nspersonnamecomponentsformatterstyle/nspersonnamecomponentsformatterstylemedium)Added [NSPersonNameComponentsFormatterStyle.Short](https://developer.apple.com/documentation/foundation/nspersonnamecomponentsformatterstyle/nspersonnamecomponentsformatterstyleshort)Added [NSPointerFunctionsOptions [struct]](https://developer.apple.com/documentation/foundation/nspointerfunctions/options)Added [NSPointerFunctionsOptions.CopyIn](https://developer.apple.com/documentation/foundation/nspointerfunctionsoptions/nspointerfunctionscopyin)Added [NSPointerFunctionsOptions.CStringPersonality](https://developer.apple.com/documentation/foundation/nspointerfunctions/options/1412902-cstringpersonality)Added NSPointerFunctionsOptions.init(rawValue: UInt)Added [NSPointerFunctionsOptions.IntegerPersonality](https://developer.apple.com/documentation/foundation/nspointerfunctionsoptions/nspointerfunctionsintegerpersonality)Added [NSPointerFunctionsOptions.MachVirtualMemory](https://developer.apple.com/documentation/foundation/nspointerfunctions/options/1409230-machvirtualmemory)Added [NSPointerFunctionsOptions.MallocMemory](https://developer.apple.com/documentation/foundation/nspointerfunctionsoptions/nspointerfunctionsmallocmemory)Added [NSPointerFunctionsOptions.ObjectPersonality](https://developer.apple.com/documentation/foundation/nspointerfunctionsoptions/nspointerfunctionsobjectpersonality)Added [NSPointerFunctionsOptions.ObjectPointerPersonality](https://developer.apple.com/documentation/foundation/nspointerfunctions/options/1411202-objectpointerpersonality)Added [NSPointerFunctionsOptions.OpaqueMemory](https://developer.apple.com/documentation/foundation/nspointerfunctionsoptions/nspointerfunctionsopaquememory)Added [NSPointerFunctionsOptions.OpaquePersonality](https://developer.apple.com/documentation/foundation/nspointerfunctions/options/1417363-opaquepersonality)Added [NSPointerFunctionsOptions.StrongMemory](https://developer.apple.com/documentation/foundation/nspointerfunctions/options/1408849-strongmemory)Added [NSPointerFunctionsOptions.StructPersonality](https://developer.apple.com/documentation/foundation/nspointerfunctionsoptions/nspointerfunctionsstructpersonality)Added [NSPointerFunctionsOptions.WeakMemory](https://developer.apple.com/documentation/foundation/nspointerfunctions/options/1415896-weakmemory)Added [NSProcessInfo.lowPowerModeEnabled](https://developer.apple.com/documentation/foundation/processinfo/1617047-islowpowermodeenabled)Added [NSProgress.addChild(_: NSProgress, withPendingUnitCount: Int64)](https://developer.apple.com/documentation/foundation/nsprogress/1417260-addchild)Added [NSProgress.discreteProgressWithTotalUnitCount(_: Int64) -> NSProgress [class]](https://developer.apple.com/documentation/foundation/progress/1410951-discreteprogress)Added [NSProgress.init(totalUnitCount: Int64, parent: NSProgress, pendingUnitCount: Int64)](https://developer.apple.com/documentation/foundation/progress/1409014-init)Added [NSProgress.resume()](https://developer.apple.com/documentation/foundation/progress/1413616-resume)Added [NSProgress.resumingHandler](https://developer.apple.com/documentation/foundation/nsprogress/1410158-resuminghandler)Added [NSProgressReporting](https://developer.apple.com/documentation/foundation/progressreporting)Added [NSProgressReporting.progress](https://developer.apple.com/documentation/foundation/progressreporting/1412781-progress)Added [NSRunLoop.performSelector(_: Selector, target: AnyObject, argument: AnyObject?, order: Int, modes: [String])](https://developer.apple.com/documentation/foundation/nsrunloop/1409310-performselector)Added [NSSortDescriptor.init(coder: NSCoder)](https://developer.apple.com/documentation/foundation/nssortdescriptor/1412503-init)Added [NSString.localizedCapitalizedString](https://developer.apple.com/documentation/foundation/nsstring/1414885-localizedcapitalizedstring)Added [NSString.localizedLowercaseString](https://developer.apple.com/documentation/foundation/nsstring/1414125-localizedlowercasestring)Added [NSString.localizedStandardContainsString(_: String) -> Bool](https://developer.apple.com/documentation/foundation/nsstring/1416328-localizedstandardcontains)Added [NSString.localizedStandardRangeOfString(_: String) -> NSRange](https://developer.apple.com/documentation/foundation/nsstring/1413574-localizedstandardrangeofstring)Added [NSString.localizedUppercaseString](https://developer.apple.com/documentation/foundation/nsstring/1413331-localizeduppercasestring)Added [NSString.stringByApplyingTransform(_: String, reverse: Bool) -> String?](https://developer.apple.com/documentation/foundation/nsstring/1407787-stringbyapplyingtransform)Added [NSString.variantFittingPresentationWidth(_: Int) -> String](https://developer.apple.com/documentation/foundation/nsstring/1413104-variantfittingpresentationwidth)Added NSUndoManager.registerUndoWithTarget<TargetType>(_: TargetType, handler: TargetType -> ())Added [NSURL.absoluteURLWithDataRepresentation(_: NSData, relativeToURL: NSURL?) -> NSURL [class]](https://developer.apple.com/documentation/foundation/nsurl/1412404-absoluteurl)Added [NSURL.dataRepresentation](https://developer.apple.com/documentation/foundation/nsurl/1407656-datarepresentation)Added [NSURL.fileURLWithPath(_: String, isDirectory: Bool, relativeToURL: NSURL?) -> NSURL [class]](https://developer.apple.com/documentation/foundation/nsurl/1413020-fileurl)Added [NSURL.fileURLWithPath(_: String, relativeToURL: NSURL?) -> NSURL [class]](https://developer.apple.com/documentation/foundation/nsurl/1413201-fileurl)Added [NSURL.hasDirectoryPath](https://developer.apple.com/documentation/foundation/nsurl/1411475-hasdirectorypath)Added [NSURL.init(absoluteURLWithDataRepresentation: NSData, relativeToURL: NSURL?)](https://developer.apple.com/documentation/foundation/nsurl/1410750-init)Added [NSURL.init(dataRepresentation: NSData, relativeToURL: NSURL?)](https://developer.apple.com/documentation/foundation/nsurl/1416851-initwithdatarepresentation)Added [NSURL.init(fileURLWithPath: String, isDirectory: Bool, relativeToURL: NSURL?)](https://developer.apple.com/documentation/foundation/nsurl/1417932-initfileurlwithpath)Added [NSURL.init(fileURLWithPath: String, relativeToURL: NSURL?)](https://developer.apple.com/documentation/foundation/nsurl/1415077-initfileurlwithpath)Added [NSURLComponents.rangeOfFragment](https://developer.apple.com/documentation/foundation/nsurlcomponents/1415180-rangeoffragment)Added [NSURLComponents.rangeOfHost](https://developer.apple.com/documentation/foundation/nsurlcomponents/1408894-rangeofhost)Added [NSURLComponents.rangeOfPassword](https://developer.apple.com/documentation/foundation/nsurlcomponents/1415024-rangeofpassword)Added [NSURLComponents.rangeOfPath](https://developer.apple.com/documentation/foundation/nsurlcomponents/1418459-rangeofpath)Added [NSURLComponents.rangeOfPort](https://developer.apple.com/documentation/foundation/nsurlcomponents/1411790-rangeofport)Added [NSURLComponents.rangeOfQuery](https://developer.apple.com/documentation/foundation/nsurlcomponents/1409456-rangeofquery)Added [NSURLComponents.rangeOfScheme](https://developer.apple.com/documentation/foundation/nsurlcomponents/1410099-rangeofscheme)Added [NSURLComponents.rangeOfUser](https://developer.apple.com/documentation/foundation/nsurlcomponents/1414961-rangeofuser)Added NSURLError [enum]Added NSURLError.BackgroundSessionInUseByAnotherProcessAdded NSURLError.BackgroundSessionRequiresSharedContainerAdded NSURLError.BackgroundSessionWasDisconnectedAdded NSURLError.BadServerResponseAdded NSURLError.BadURLAdded NSURLError.CallIsActiveAdded NSURLError.CancelledAdded NSURLError.CannotCloseFileAdded NSURLError.CannotConnectToHostAdded NSURLError.CannotCreateFileAdded NSURLError.CannotDecodeContentDataAdded NSURLError.CannotDecodeRawDataAdded NSURLError.CannotFindHostAdded NSURLError.CannotLoadFromNetworkAdded NSURLError.CannotMoveFileAdded NSURLError.CannotOpenFileAdded NSURLError.CannotParseResponseAdded NSURLError.CannotRemoveFileAdded NSURLError.CannotWriteToFileAdded NSURLError.ClientCertificateRejectedAdded NSURLError.ClientCertificateRequiredAdded NSURLError.DataNotAllowedAdded NSURLError.DNSLookupFailedAdded NSURLError.DownloadDecodingFailedMidStreamAdded NSURLError.DownloadDecodingFailedToCompleteAdded NSURLError.FileDoesNotExistAdded NSURLError.FileIsDirectoryAdded NSURLError.HTTPTooManyRedirectsAdded NSURLError.InternationalRoamingOffAdded NSURLError.NetworkConnectionLostAdded NSURLError.NoPermissionsToReadFileAdded NSURLError.NotConnectedToInternetAdded NSURLError.RedirectToNonExistentLocationAdded NSURLError.RequestBodyStreamExhaustedAdded NSURLError.ResourceUnavailableAdded NSURLError.SecureConnectionFailedAdded NSURLError.ServerCertificateHasBadDateAdded NSURLError.ServerCertificateHasUnknownRootAdded NSURLError.ServerCertificateNotYetValidAdded NSURLError.ServerCertificateUntrustedAdded NSURLError.TimedOutAdded NSURLError.UnknownAdded NSURLError.UnsupportedURLAdded NSURLError.UserAuthenticationRequiredAdded NSURLError.UserCancelledAuthenticationAdded NSURLError.ZeroByteResourceAdded [NSURLRequestCachePolicy.ReloadIgnoringCacheData](https://developer.apple.com/documentation/foundation/nsurlrequest/cachepolicy/1417522-reloadignoringcachedata)Added [NSURLSession.getAllTasksWithCompletionHandler(_: ([NSURLSessionTask]) -> Void)](https://developer.apple.com/documentation/foundation/urlsession/1411618-getalltasks)Added [NSURLSession.streamTaskWithHostName(_: String, port: Int) -> NSURLSessionStreamTask](https://developer.apple.com/documentation/foundation/urlsession/1411587-streamtask)Added [NSURLSession.streamTaskWithNetService(_: NSNetService) -> NSURLSessionStreamTask](https://developer.apple.com/documentation/foundation/urlsession/1411545-streamtask)Added [NSURLSessionConfiguration.shouldUseExtendedBackgroundIdleMode](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1409517-shoulduseextendedbackgroundidlem)Added [NSURLSessionDataDelegate.URLSession(_: NSURLSession, dataTask: NSURLSessionDataTask, didBecomeStreamTask: NSURLSessionStreamTask)](https://developer.apple.com/documentation/foundation/nsurlsessiondatadelegate/1411648-urlsession)Added [NSURLSessionResponseDisposition.BecomeStream](https://developer.apple.com/documentation/foundation/nsurlsessionresponsedisposition/nsurlsessionresponsebecomestream)Added [NSURLSessionStreamDelegate](https://developer.apple.com/documentation/foundation/urlsessionstreamdelegate)Added [NSURLSessionStreamDelegate.URLSession(_: NSURLSession, betterRouteDiscoveredForStreamTask: NSURLSessionStreamTask)](https://developer.apple.com/documentation/foundation/urlsessionstreamdelegate/1407527-urlsession)Added [NSURLSessionStreamDelegate.URLSession(_: NSURLSession, readClosedForStreamTask: NSURLSessionStreamTask)](https://developer.apple.com/documentation/foundation/urlsessionstreamdelegate/1411501-urlsession)Added [NSURLSessionStreamDelegate.URLSession(_: NSURLSession, streamTask: NSURLSessionStreamTask, didBecomeInputStream: NSInputStream, outputStream: NSOutputStream)](https://developer.apple.com/documentation/foundation/nsurlsessionstreamdelegate/1411625-urlsession)Added [NSURLSessionStreamDelegate.URLSession(_: NSURLSession, writeClosedForStreamTask: NSURLSessionStreamTask)](https://developer.apple.com/documentation/foundation/nsurlsessionstreamdelegate/1411507-urlsession)Added [NSURLSessionStreamTask](https://developer.apple.com/documentation/foundation/nsurlsessionstreamtask)Added [NSURLSessionStreamTask.captureStreams()](https://developer.apple.com/documentation/foundation/urlsessionstreamtask/1410132-capturestreams)Added [NSURLSessionStreamTask.closeRead()](https://developer.apple.com/documentation/foundation/urlsessionstreamtask/1411558-closeread)Added [NSURLSessionStreamTask.closeWrite()](https://developer.apple.com/documentation/foundation/nsurlsessionstreamtask/1411347-closewrite)Added [NSURLSessionStreamTask.readDataOfMinLength(_: Int, maxLength: Int, timeout: NSTimeInterval, completionHandler: (NSData?, Bool, NSError?) -> Void)](https://developer.apple.com/documentation/foundation/urlsessionstreamtask/1411604-readdata)Added [NSURLSessionStreamTask.startSecureConnection()](https://developer.apple.com/documentation/foundation/urlsessionstreamtask/1411567-startsecureconnection)Added [NSURLSessionStreamTask.stopSecureConnection()](https://developer.apple.com/documentation/foundation/nsurlsessionstreamtask/1407337-stopsecureconnection)Added [NSURLSessionStreamTask.writeData(_: NSData, timeout: NSTimeInterval, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/foundation/nsurlsessionstreamtask/1411602-writedata)Added [NSUserActivity.eligibleForHandoff](https://developer.apple.com/documentation/foundation/nsuseractivity/1410971-eligibleforhandoff)Added [NSUserActivity.eligibleForPublicIndexing](https://developer.apple.com/documentation/foundation/nsuseractivity/1414701-eligibleforpublicindexing)Added [NSUserActivity.eligibleForSearch](https://developer.apple.com/documentation/foundation/nsuseractivity/1417761-iseligibleforsearch)Added [NSUserActivity.expirationDate](https://developer.apple.com/documentation/foundation/nsuseractivity/1413745-expirationdate)Added [NSUserActivity.keywords](https://developer.apple.com/documentation/foundation/nsuseractivity/1408023-keywords)Added [NSUserActivity.requiredUserInfoKeys](https://developer.apple.com/documentation/foundation/nsuseractivity/1417256-requireduserinfokeys)Added [NSUserActivity.resignCurrent()](https://developer.apple.com/documentation/foundation/nsuseractivity/1409596-resigncurrent)Added [NSValue.pointerValue](https://developer.apple.com/documentation/foundation/nsvalue/1410668-pointervalue)Added String.compare(_: String, options: NSStringCompareOptions, range: Range<Index>?, locale: NSLocale?) -> NSComparisonResultAdded String.containsString(_: String) -> BoolAdded String.enumerateLinguisticTagsInRange(_: Range<Index>, scheme: String, options: NSLinguisticTaggerOptions, orthography: NSOrthography?, _: (String, Range<Index>, Range<Index>, inout Bool) -> ())Added String.enumerateSubstringsInRange(_: Range<Index>, options: NSStringEnumerationOptions, _: (substring: String?, substringRange: Range<Index>, enclosingRange: Range<Index>, inout Bool) -> ())Added String.getBytes(_: [UInt8], maxLength: Int, usedLength: UnsafeMutablePointer<Int>, encoding: NSStringEncoding, options: NSStringEncodingConversionOptions, range: Range<Index>, remainingRange: UnsafeMutablePointer<Range<Index>>) -> BoolAdded String.getLineStart(_: UnsafeMutablePointer<Index>, end: UnsafeMutablePointer<Index>, contentsEnd: UnsafeMutablePointer<Index>, forRange: Range<Index>)Added String.getParagraphStart(_: UnsafeMutablePointer<Index>, end: UnsafeMutablePointer<Index>, contentsEnd: UnsafeMutablePointer<Index>, forRange: Range<Index>)Added String.init(contentsOfFile: String, encoding: NSStringEncoding) throwsAdded String.init(contentsOfFile: String, usedEncoding: UnsafeMutablePointer<NSStringEncoding>) throwsAdded String.init(contentsOfURL: NSURL, encoding: NSStringEncoding) throwsAdded String.init(contentsOfURL: NSURL, usedEncoding: UnsafeMutablePointer<NSStringEncoding>) throwsAdded String.init(data: NSData, encoding: NSStringEncoding)Added String.lineRangeForRange(_: Range<Index>) -> Range<Index>Added String.linguisticTagsInRange(_: Range<Index>, scheme: String, options: NSLinguisticTaggerOptions, orthography: NSOrthography?, tokenRanges: UnsafeMutablePointer<[Range<Index>]>) -> [String]Added String.localizedCapitalizedStringAdded String.localizedCaseInsensitiveContainsString(_: String) -> BoolAdded String.localizedLowercaseStringAdded String.localizedStandardContainsString(_: String) -> BoolAdded String.localizedStandardRangeOfString(_: String) -> Range<Index>?Added String.localizedUppercaseStringAdded String.lowercaseStringWithLocale(_: NSLocale?) -> StringAdded String.paragraphRangeForRange(_: Range<Index>) -> Range<Index>Added String.rangeOfCharacterFromSet(_: NSCharacterSet, options: NSStringCompareOptions, range: Range<Index>?) -> Range<Index>?Added String.rangeOfComposedCharacterSequenceAtIndex(_: Index) -> Range<Index>Added String.rangeOfComposedCharacterSequencesForRange(_: Range<Index>) -> Range<Index>Added String.rangeOfString(_: String, options: NSStringCompareOptions, range: Range<Index>?, locale: NSLocale?) -> Range<Index>?Added String.stringByApplyingTransform(_: String, reverse: Bool) -> String?Added String.stringByFoldingWithOptions(_: NSStringCompareOptions, locale: NSLocale?) -> StringAdded String.stringByReplacingCharactersInRange(_: Range<Index>, withString: String) -> StringAdded String.stringByReplacingOccurrencesOfString(_: String, withString: String, options: NSStringCompareOptions, range: Range<Index>?) -> StringAdded String.substringFromIndex(_: Index) -> StringAdded String.substringToIndex(_: Index) -> StringAdded String.substringWithRange(_: Range<Index>) -> StringAdded String.uppercaseStringWithLocale(_: NSLocale?) -> StringAdded String.writeToFile(_: String, atomically: Bool, encoding: NSStringEncoding) throwsAdded String.writeToURL(_: NSURL, atomically: Bool, encoding: NSStringEncoding) throwsAdded ==(_: T, _: T) -> BoolAdded ==(_: T, _: T) -> BoolAdded [NSBundleErrorMaximum](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nsbundleerrormaximum)Added [NSBundleErrorMinimum](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nsbundleerrorminimum)Added [NSBundleOnDemandResourceExceededMaximumSizeError](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nsbundleondemandresourceexceededmaximumsizeerror)Added [NSBundleOnDemandResourceInvalidTagError](https://developer.apple.com/documentation/foundation/nsbundleondemandresourceinvalidtagerror)Added [NSBundleOnDemandResourceOutOfSpaceError](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nsbundleondemandresourceoutofspaceerror)Added [NSBundleResourceRequestLoadingPriorityUrgent](https://developer.apple.com/documentation/foundation/nsbundleresourcerequestloadingpriorityurgent)Added [NSBundleResourceRequestLowDiskSpaceNotification](https://developer.apple.com/documentation/foundation/nsbundleresourcerequestlowdiskspacenotification)Added [NSCoderErrorMaximum](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nscodererrormaximum)Added [NSCoderErrorMinimum](https://developer.apple.com/documentation/foundation/nscodererrorminimum)Added [NSCoderReadCorruptError](https://developer.apple.com/documentation/foundation/nscoderreadcorrupterror)Added [NSCoderValueNotFoundError](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nscodervaluenotfounderror)Added [NSFoundationVersionNumber10_10](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_10)Added [NSFoundationVersionNumber10_10_1](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_10_1)Added [NSFoundationVersionNumber10_10_2](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_10_2)Added [NSFoundationVersionNumber10_10_3](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_10_3)Added [NSFoundationVersionNumber_iOS_8_0](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber_ios_8_0)Added [NSFoundationVersionNumber_iOS_8_1](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber_ios_8_1)Added [NSFoundationVersionNumber_iOS_8_2](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber_ios_8_2)Added [NSFoundationVersionNumber_iOS_8_3](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber_ios_8_3)Added [NSPersonNameComponentDelimiter](https://developer.apple.com/documentation/foundation/nspersonnamecomponentdelimiter)Added [NSPersonNameComponentFamilyName](https://developer.apple.com/documentation/foundation/nspersonnamecomponentfamilyname)Added [NSPersonNameComponentGivenName](https://developer.apple.com/documentation/foundation/nspersonnamecomponentgivenname)Added [NSPersonNameComponentKey](https://developer.apple.com/documentation/foundation/nspersonnamecomponentkey)Added [NSPersonNameComponentMiddleName](https://developer.apple.com/documentation/foundation/nspersonnamecomponentmiddlename)Added [NSPersonNameComponentNickname](https://developer.apple.com/documentation/foundation/nspersonnamecomponentnickname)Added [NSPersonNameComponentPrefix](https://developer.apple.com/documentation/foundation/nspersonnamecomponentprefix)Added [NSPersonNameComponentSuffix](https://developer.apple.com/documentation/foundation/nspersonnamecomponentsuffix)Added [NSProcessInfoPowerStateDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1617322-nsprocessinfopowerstatedidchange)Added [NSStringTransformFullwidthToHalfwidth](https://developer.apple.com/documentation/foundation/nsstringtransformfullwidthtohalfwidth)Added [NSStringTransformHiraganaToKatakana](https://developer.apple.com/documentation/foundation/nsstringtransformhiraganatokatakana)Added [NSStringTransformLatinToArabic](https://developer.apple.com/documentation/foundation/stringtransform/1409724-latintoarabic)Added [NSStringTransformLatinToCyrillic](https://developer.apple.com/documentation/foundation/nsstringtransformlatintocyrillic)Added [NSStringTransformLatinToGreek](https://developer.apple.com/documentation/foundation/nsstringtransformlatintogreek)Added [NSStringTransformLatinToHangul](https://developer.apple.com/documentation/foundation/nsstringtransformlatintohangul)Added [NSStringTransformLatinToHebrew](https://developer.apple.com/documentation/foundation/nsstringtransformlatintohebrew)Added [NSStringTransformLatinToHiragana](https://developer.apple.com/documentation/foundation/stringtransform/1412376-latintohiragana)Added [NSStringTransformLatinToKatakana](https://developer.apple.com/documentation/foundation/nsstringtransformlatintokatakana)Added [NSStringTransformLatinToThai](https://developer.apple.com/documentation/foundation/nsstringtransformlatintothai)Added [NSStringTransformMandarinToLatin](https://developer.apple.com/documentation/foundation/stringtransform/1409304-mandarintolatin)Added [NSStringTransformStripCombiningMarks](https://developer.apple.com/documentation/foundation/nsstringtransformstripcombiningmarks)Added [NSStringTransformStripDiacritics](https://developer.apple.com/documentation/foundation/stringtransform/1416044-stripdiacritics)Added [NSStringTransformToLatin](https://developer.apple.com/documentation/foundation/nsstringtransformtolatin)Added [NSStringTransformToUnicodeName](https://developer.apple.com/documentation/foundation/nsstringtransformtounicodename)Added [NSStringTransformToXMLHex](https://developer.apple.com/documentation/foundation/stringtransform/1407218-toxmlhex)Added [NSURLErrorAppTransportSecurityRequiresSecureConnection](https://developer.apple.com/documentation/foundation/nsurlerrorapptransportsecurityrequiressecureconnection)Added [NSURLFileProtectionComplete](https://developer.apple.com/documentation/foundation/nsurlfileprotectioncomplete)Added [NSURLFileProtectionCompleteUnlessOpen](https://developer.apple.com/documentation/foundation/urlfileprotection/1616775-completeunlessopen)Added [NSURLFileProtectionCompleteUntilFirstUserAuthentication](https://developer.apple.com/documentation/foundation/nsurlfileprotectioncompleteuntilfirstuserauthentication)Added [NSURLFileProtectionKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1616246-fileprotectionkey)Added [NSURLFileProtectionNone](https://developer.apple.com/documentation/foundation/urlfileprotection/1616634-none)Added [NSURLIsApplicationKey](https://developer.apple.com/documentation/foundation/nsurlisapplicationkey)Added ~=(_: NSCocoaError, _: ErrorType) -> BoolModified [NSActivityOptions [struct]](https://developer.apple.com/documentation/foundation/nsactivityoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSActivityOptions : RawOptionSetType {     init(_ rawValue: UInt64)     init(rawValue rawValue: UInt64)     static var IdleDisplaySleepDisabled: NSActivityOptions { get }     static var IdleSystemSleepDisabled: NSActivityOptions { get }     static var SuddenTerminationDisabled: NSActivityOptions { get }     static var AutomaticTerminationDisabled: NSActivityOptions { get }     static var UserInitiated: NSActivityOptions { get }     static var UserInitiatedAllowingIdleSystemSleep: NSActivityOptions { get }     static var Background: NSActivityOptions { get }     static var LatencyCritical: NSActivityOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSActivityOptions : OptionSetType {     init(rawValue rawValue: UInt64)     static var IdleDisplaySleepDisabled: NSActivityOptions { get }     static var IdleSystemSleepDisabled: NSActivityOptions { get }     static var SuddenTerminationDisabled: NSActivityOptions { get }     static var AutomaticTerminationDisabled: NSActivityOptions { get }     static var UserInitiated: NSActivityOptions { get }     static var UserInitiatedAllowingIdleSystemSleep: NSActivityOptions { get }     static var Background: NSActivityOptions { get }     static var LatencyCritical: NSActivityOptions { get } } ``` | OptionSetType |

Modified [NSArray](https://developer.apple.com/documentation/foundation/nsarray)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSArray : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding, NSFastEnumeration {     var count: Int { get }     func objectAtIndex(_ index: Int) -> AnyObject     init()     init(objects objects: UnsafePointer<AnyObject?>, count cnt: Int)     init(coder aDecoder: NSCoder) } extension NSArray : CKRecordValue, NSObjectProtocol { } extension NSArray : ArrayLiteralConvertible {     required convenience init(arrayLiteral elements: AnyObject...) } extension NSArray : SequenceType {     final func generate() -> NSFastGenerator } extension NSArray {     convenience init(objects elements: AnyObject...) } extension NSArray {     @objc(_swiftInitWithArray_NSArray:) convenience init(array anArray: NSArray) } extension NSArray : Reflectable {     func getMirror() -> MirrorType } extension NSArray {     func arrayByAddingObject(_ anObject: AnyObject) -> [AnyObject]     func arrayByAddingObjectsFromArray(_ otherArray: [AnyObject]) -> [AnyObject]     func componentsJoinedByString(_ separator: String) -> String     func containsObject(_ anObject: AnyObject) -> Bool     var description: String { get }     func descriptionWithLocale(_ locale: AnyObject?) -> String     func descriptionWithLocale(_ locale: AnyObject?, indent level: Int) -> String     func firstObjectCommonWithArray(_ otherArray: [AnyObject]) -> AnyObject?     func getObjects(_ objects: AutoreleasingUnsafeMutablePointer<AnyObject?>, range range: NSRange)     func indexOfObject(_ anObject: AnyObject) -> Int     func indexOfObject(_ anObject: AnyObject, inRange range: NSRange) -> Int     func indexOfObjectIdenticalTo(_ anObject: AnyObject) -> Int     func indexOfObjectIdenticalTo(_ anObject: AnyObject, inRange range: NSRange) -> Int     func isEqualToArray(_ otherArray: [AnyObject]) -> Bool     var firstObject: AnyObject? { get }     var lastObject: AnyObject? { get }     func objectEnumerator() -> NSEnumerator     func reverseObjectEnumerator() -> NSEnumerator     @NSCopying var sortedArrayHint: NSData { get }     func sortedArrayUsingFunction(_ comparator: CFunctionPointer<((AnyObject!, AnyObject!, UnsafeMutablePointer<Void>) -> Int)>, context context: UnsafeMutablePointer<Void>) -> [AnyObject]     func sortedArrayUsingFunction(_ comparator: CFunctionPointer<((AnyObject!, AnyObject!, UnsafeMutablePointer<Void>) -> Int)>, context context: UnsafeMutablePointer<Void>, hint hint: NSData?) -> [AnyObject]     func sortedArrayUsingSelector(_ comparator: Selector) -> [AnyObject]     func subarrayWithRange(_ range: NSRange) -> [AnyObject]     func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool) -> Bool     func writeToURL(_ url: NSURL, atomically atomically: Bool) -> Bool     func makeObjectsPerformSelector(_ aSelector: Selector)     func makeObjectsPerformSelector(_ aSelector: Selector, withObject argument: AnyObject?)     func objectsAtIndexes(_ indexes: NSIndexSet) -> [AnyObject]     subscript (idx: Int) -> AnyObject { get }     func objectAtIndexedSubscript(_ idx: Int) -> AnyObject     func enumerateObjectsUsingBlock(_ block: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, usingBlock block: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func indexOfObjectPassingTest(_ predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexOfObjectWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexOfObjectAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexesOfObjectsPassingTest(_ predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexesOfObjectsWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexesOfObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func sortedArrayUsingComparator(_ cmptr: NSComparator) -> [AnyObject]     func sortedArrayWithOptions(_ opts: NSSortOptions, usingComparator cmptr: NSComparator) -> [AnyObject]     func indexOfObject(_ obj: AnyObject, inSortedRange r: NSRange, options opts: NSBinarySearchingOptions, usingComparator cmp: NSComparator) -> Int } extension NSArray {     convenience init!()     class func array() -> Self!     convenience init(object anObject: AnyObject)     class func arrayWithObject(_ anObject: AnyObject) -> Self     convenience init!(objects objects: UnsafePointer<AnyObject?>, count cnt: Int)     class func arrayWithObjects(_ objects: UnsafePointer<AnyObject?>, count cnt: Int) -> Self!     convenience init(array array: [AnyObject])     class func arrayWithArray(_ array: [AnyObject]) -> Self     convenience init(array array: [AnyObject])     convenience init(array array: [AnyObject], copyItems flag: Bool)     init?(contentsOfFile path: String) -> NSArray     class func arrayWithContentsOfFile(_ path: String) -> [AnyObject]?     init?(contentsOfURL url: NSURL) -> NSArray     class func arrayWithContentsOfURL(_ url: NSURL) -> [AnyObject]?     convenience init?(contentsOfFile path: String)     convenience init?(contentsOfURL url: NSURL) } extension NSArray {     func getObjects(_ objects: AutoreleasingUnsafeMutablePointer<AnyObject?>) } extension NSArray {     func valueForKey(_ key: String) -> AnyObject?     func setValue(_ value: AnyObject?, forKey key: String) } extension NSArray {     func addObserver(_ observer: NSObject, toObjectsAtIndexes indexes: NSIndexSet, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, fromObjectsAtIndexes indexes: NSIndexSet, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, fromObjectsAtIndexes indexes: NSIndexSet, forKeyPath keyPath: String)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String) } extension NSArray {     func pathsMatchingExtensions(_ filterTypes: [AnyObject]) -> [AnyObject] } extension NSArray {     func filteredArrayUsingPredicate(_ predicate: NSPredicate) -> [AnyObject] } extension NSArray {     func sortedArrayUsingDescriptors(_ sortDescriptors: [AnyObject]) -> [AnyObject] } extension NSArray : Reflectable {     func getMirror() -> MirrorType } extension NSArray {     @objc(_swiftInitWithArray_NSArray:) convenience init(array anArray: NSArray) } extension NSArray {     convenience init(objects elements: AnyObject...) } extension NSArray : SequenceType {     final func generate() -> NSFastGenerator } extension NSArray : ArrayLiteralConvertible {     required convenience init(arrayLiteral elements: AnyObject...) } ``` | AnyObject, ArrayLiteralConvertible, CKRecordValue, NSCoding, NSCopying, NSFastEnumeration, NSMutableCopying, NSObjectProtocol, NSSecureCoding, Reflectable, SequenceType |
| To | ``` class NSArray : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding, NSFastEnumeration {     var count: Int { get }     func objectAtIndex(_ index: Int) -> AnyObject     init()     init(objects objects: UnsafePointer<AnyObject?>, count cnt: Int)     init?(coder aDecoder: NSCoder) } extension NSArray : CKRecordValue { } extension NSArray : ArrayLiteralConvertible {     required convenience init(arrayLiteral elements: AnyObject...) } extension NSArray : SequenceType {     final func generate() -> NSFastGenerator } extension NSArray {     convenience init(objects elements: AnyObject...) } extension NSArray {     @objc(_swiftInitWithArray_NSArray:) convenience init(array anArray: NSArray) } extension NSArray : _Reflectable { } extension NSArray {     func arrayByAddingObject(_ anObject: AnyObject) -> [AnyObject]     func arrayByAddingObjectsFromArray(_ otherArray: [AnyObject]) -> [AnyObject]     func componentsJoinedByString(_ separator: String) -> String     func containsObject(_ anObject: AnyObject) -> Bool     var description: String { get }     func descriptionWithLocale(_ locale: AnyObject?) -> String     func descriptionWithLocale(_ locale: AnyObject?, indent level: Int) -> String     func firstObjectCommonWithArray(_ otherArray: [AnyObject]) -> AnyObject?     func getObjects(_ objects: AutoreleasingUnsafeMutablePointer<AnyObject?>, range range: NSRange)     func indexOfObject(_ anObject: AnyObject) -> Int     func indexOfObject(_ anObject: AnyObject, inRange range: NSRange) -> Int     func indexOfObjectIdenticalTo(_ anObject: AnyObject) -> Int     func indexOfObjectIdenticalTo(_ anObject: AnyObject, inRange range: NSRange) -> Int     func isEqualToArray(_ otherArray: [AnyObject]) -> Bool     var firstObject: AnyObject? { get }     var lastObject: AnyObject? { get }     func objectEnumerator() -> NSEnumerator     func reverseObjectEnumerator() -> NSEnumerator     @NSCopying var sortedArrayHint: NSData { get }     func sortedArrayUsingFunction(_ comparator: (AnyObject, AnyObject, UnsafeMutablePointer<Void>) -> Int, context context: UnsafeMutablePointer<Void>) -> [AnyObject]     func sortedArrayUsingFunction(_ comparator: (AnyObject, AnyObject, UnsafeMutablePointer<Void>) -> Int, context context: UnsafeMutablePointer<Void>, hint hint: NSData?) -> [AnyObject]     func sortedArrayUsingSelector(_ comparator: Selector) -> [AnyObject]     func subarrayWithRange(_ range: NSRange) -> [AnyObject]     func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool) -> Bool     func writeToURL(_ url: NSURL, atomically atomically: Bool) -> Bool     func makeObjectsPerformSelector(_ aSelector: Selector)     func makeObjectsPerformSelector(_ aSelector: Selector, withObject argument: AnyObject?)     func objectsAtIndexes(_ indexes: NSIndexSet) -> [AnyObject]     subscript (_ idx: Int) -> AnyObject { get }     func objectAtIndexedSubscript(_ idx: Int) -> AnyObject     func enumerateObjectsUsingBlock(_ block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, usingBlock block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func indexOfObjectPassingTest(_ predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexOfObjectWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexOfObjectAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexesOfObjectsPassingTest(_ predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexesOfObjectsWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexesOfObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func sortedArrayUsingComparator(_ cmptr: NSComparator) -> [AnyObject]     func sortedArrayWithOptions(_ opts: NSSortOptions, usingComparator cmptr: NSComparator) -> [AnyObject]     func indexOfObject(_ obj: AnyObject, inSortedRange r: NSRange, options opts: NSBinarySearchingOptions, usingComparator cmp: NSComparator) -> Int } extension NSArray {     convenience init()     class func array() -> Self     convenience init(object anObject: AnyObject)     class func arrayWithObject(_ anObject: AnyObject) -> Self     convenience init(objects objects: UnsafePointer<AnyObject?>, count cnt: Int)     class func arrayWithObjects(_ objects: UnsafePointer<AnyObject?>, count cnt: Int) -> Self     convenience init(array array: [AnyObject])     class func arrayWithArray(_ array: [AnyObject]) -> Self     convenience init(array array: [AnyObject])     convenience init(array array: [AnyObject], copyItems flag: Bool)      init?(contentsOfFile path: String)     class func arrayWithContentsOfFile(_ path: String) -> [AnyObject]?      init?(contentsOfURL url: NSURL)     class func arrayWithContentsOfURL(_ url: NSURL) -> [AnyObject]?     convenience init?(contentsOfFile path: String)     convenience init?(contentsOfURL url: NSURL) } extension NSArray {     func getObjects(_ objects: AutoreleasingUnsafeMutablePointer<AnyObject?>) } extension NSArray {     func valueForKey(_ key: String) -> AnyObject     func setValue(_ value: AnyObject?, forKey key: String) } extension NSArray {     func addObserver(_ observer: NSObject, toObjectsAtIndexes indexes: NSIndexSet, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, fromObjectsAtIndexes indexes: NSIndexSet, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, fromObjectsAtIndexes indexes: NSIndexSet, forKeyPath keyPath: String)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String) } extension NSArray {     func pathsMatchingExtensions(_ filterTypes: [String]) -> [String] } extension NSArray {     func filteredArrayUsingPredicate(_ predicate: NSPredicate) -> [AnyObject] } extension NSArray {     func sortedArrayUsingDescriptors(_ sortDescriptors: [NSSortDescriptor]) -> [AnyObject] } extension NSArray : _Reflectable { } extension NSArray {     @objc(_swiftInitWithArray_NSArray:) convenience init(array anArray: NSArray) } extension NSArray {     convenience init(objects elements: AnyObject...) } extension NSArray : SequenceType {     final func generate() -> NSFastGenerator } extension NSArray : ArrayLiteralConvertible {     required convenience init(arrayLiteral elements: AnyObject...) } ``` | AnyObject, ArrayLiteralConvertible, CKRecordValue, NSCoding, NSCopying, NSFastEnumeration, NSMutableCopying, NSObjectProtocol, NSSecureCoding, SequenceType |

Modified [NSArray.enumerateObjectsAtIndexes(_: NSIndexSet, options: NSEnumerationOptions, usingBlock: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/foundation/nsarray/1417577-enumerateobjects)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, usingBlock block: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, usingBlock block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [NSArray.enumerateObjectsUsingBlock(_: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/foundation/nsarray/1415846-enumerateobjectsusingblock)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateObjectsUsingBlock(_ block: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateObjectsUsingBlock(_ block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [NSArray.enumerateObjectsWithOptions(_: NSEnumerationOptions, usingBlock: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/foundation/nsarray/1413010-enumerateobjectswithoptions)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [NSArray.indexesOfObjectsAtIndexes(_: NSIndexSet, options: NSEnumerationOptions, passingTest: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet](https://developer.apple.com/documentation/foundation/nsarray/1413512-indexesofobjectsatindexes)

|  | Declaration |
| --- | --- |
| From | ``` func indexesOfObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet ``` |
| To | ``` func indexesOfObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet ``` |

Modified [NSArray.indexesOfObjectsPassingTest(_: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet](https://developer.apple.com/documentation/foundation/nsarray/1417603-indexesofobjects)

|  | Declaration |
| --- | --- |
| From | ``` func indexesOfObjectsPassingTest(_ predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet ``` |
| To | ``` func indexesOfObjectsPassingTest(_ predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet ``` |

Modified [NSArray.indexesOfObjectsWithOptions(_: NSEnumerationOptions, passingTest: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet](https://developer.apple.com/documentation/foundation/nsarray/1415087-indexesofobjects)

|  | Declaration |
| --- | --- |
| From | ``` func indexesOfObjectsWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet ``` |
| To | ``` func indexesOfObjectsWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet ``` |

Modified [NSArray.indexOfObjectAtIndexes(_: NSIndexSet, options: NSEnumerationOptions, passingTest: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](https://developer.apple.com/documentation/foundation/nsarray/1407652-indexofobjectatindexes)

|  | Declaration |
| --- | --- |
| From | ``` func indexOfObjectAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int ``` |
| To | ``` func indexOfObjectAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int ``` |

Modified [NSArray.indexOfObjectPassingTest(_: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](https://developer.apple.com/documentation/foundation/nsarray/1408043-indexofobjectpassingtest)

|  | Declaration |
| --- | --- |
| From | ``` func indexOfObjectPassingTest(_ predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int ``` |
| To | ``` func indexOfObjectPassingTest(_ predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int ``` |

Modified [NSArray.indexOfObjectWithOptions(_: NSEnumerationOptions, passingTest: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](https://developer.apple.com/documentation/foundation/nsarray/1417053-indexofobjectwithoptions)

|  | Declaration |
| --- | --- |
| From | ``` func indexOfObjectWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int ``` |
| To | ``` func indexOfObjectWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int ``` |

Modified [NSArray.init(coder: NSCoder)](https://developer.apple.com/documentation/foundation/nsarray/1407810-init)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified [NSArray.pathsMatchingExtensions(_: [String]) -> [String]](https://developer.apple.com/documentation/foundation/nsarray/1418275-pathsmatchingextensions)

|  | Declaration |
| --- | --- |
| From | ``` func pathsMatchingExtensions(_ filterTypes: [AnyObject]) -> [AnyObject] ``` |
| To | ``` func pathsMatchingExtensions(_ filterTypes: [String]) -> [String] ``` |

Modified [NSArray.sortedArrayUsingDescriptors(_: [NSSortDescriptor]) -> [AnyObject]](https://developer.apple.com/documentation/foundation/nsarray/1415069-sortedarray)

|  | Declaration |
| --- | --- |
| From | ``` func sortedArrayUsingDescriptors(_ sortDescriptors: [AnyObject]) -> [AnyObject] ``` |
| To | ``` func sortedArrayUsingDescriptors(_ sortDescriptors: [NSSortDescriptor]) -> [AnyObject] ``` |

Modified [NSArray.sortedArrayUsingFunction(_: (AnyObject, AnyObject, UnsafeMutablePointer<Void>) -> Int, context: UnsafeMutablePointer<Void>) -> [AnyObject]](https://developer.apple.com/documentation/foundation/nsarray/1408213-sortedarray)

|  | Declaration |
| --- | --- |
| From | ``` func sortedArrayUsingFunction(_ comparator: CFunctionPointer<((AnyObject!, AnyObject!, UnsafeMutablePointer<Void>) -> Int)>, context context: UnsafeMutablePointer<Void>) -> [AnyObject] ``` |
| To | ``` func sortedArrayUsingFunction(_ comparator: (AnyObject, AnyObject, UnsafeMutablePointer<Void>) -> Int, context context: UnsafeMutablePointer<Void>) -> [AnyObject] ``` |

Modified [NSArray.sortedArrayUsingFunction(_: (AnyObject, AnyObject, UnsafeMutablePointer<Void>) -> Int, context: UnsafeMutablePointer<Void>, hint: NSData?) -> [AnyObject]](https://developer.apple.com/documentation/foundation/nsarray/1414839-sortedarrayusingfunction)

|  | Declaration |
| --- | --- |
| From | ``` func sortedArrayUsingFunction(_ comparator: CFunctionPointer<((AnyObject!, AnyObject!, UnsafeMutablePointer<Void>) -> Int)>, context context: UnsafeMutablePointer<Void>, hint hint: NSData?) -> [AnyObject] ``` |
| To | ``` func sortedArrayUsingFunction(_ comparator: (AnyObject, AnyObject, UnsafeMutablePointer<Void>) -> Int, context context: UnsafeMutablePointer<Void>, hint hint: NSData?) -> [AnyObject] ``` |

Modified [NSArray.subscript(_: Int) -> AnyObject](https://developer.apple.com/documentation/foundation/nsarray/1414084-objectatindexedsubscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (idx: Int) -> AnyObject { get } ``` |
| To | ``` subscript (_ idx: Int) -> AnyObject { get } ``` |

Modified [NSArray.valueForKey(_: String) -> AnyObject](https://developer.apple.com/documentation/foundation/nsarray/1412219-valueforkey)

|  | Declaration |
| --- | --- |
| From | ``` func valueForKey(_ key: String) -> AnyObject? ``` |
| To | ``` func valueForKey(_ key: String) -> AnyObject ``` |

Modified [NSAttributedString](https://developer.apple.com/documentation/foundation/nsattributedstring)

|  | Declaration |
| --- | --- |
| From | ``` class NSAttributedString : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     var string: String { get }     func attributesAtIndex(_ location: Int, effectiveRange range: NSRangePointer) -> [NSObject : AnyObject] } extension NSAttributedString {     var length: Int { get }     func attribute(_ attrName: String, atIndex location: Int, effectiveRange range: NSRangePointer) -> AnyObject?     func attributedSubstringFromRange(_ range: NSRange) -> NSAttributedString     func attributesAtIndex(_ location: Int, longestEffectiveRange range: NSRangePointer, inRange rangeLimit: NSRange) -> [NSObject : AnyObject]     func attribute(_ attrName: String, atIndex location: Int, longestEffectiveRange range: NSRangePointer, inRange rangeLimit: NSRange) -> AnyObject?     func isEqualToAttributedString(_ other: NSAttributedString) -> Bool     init(string str: String)     init(string str: String, attributes attrs: [NSObject : AnyObject]?)     init(attributedString attrStr: NSAttributedString)     func enumerateAttributesInRange(_ enumerationRange: NSRange, options opts: NSAttributedStringEnumerationOptions, usingBlock block: ([NSObject : AnyObject]!, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateAttribute(_ attrName: String, inRange enumerationRange: NSRange, options opts: NSAttributedStringEnumerationOptions, usingBlock block: (AnyObject!, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) } extension NSAttributedString {     init?(fileURL url: NSURL!, options options: [NSObject : AnyObject]!, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>, error error: NSErrorPointer)     init?(data data: NSData, options options: [NSObject : AnyObject]?, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>, error error: NSErrorPointer)     func dataFromRange(_ range: NSRange, documentAttributes dict: [NSObject : AnyObject], error error: NSErrorPointer) -> NSData?     func fileWrapperFromRange(_ range: NSRange, documentAttributes dict: [NSObject : AnyObject], error error: NSErrorPointer) -> NSFileWrapper? } extension NSAttributedString {     func size() -> CGSize     func drawAtPoint(_ point: CGPoint)     func drawInRect(_ rect: CGRect) } extension NSAttributedString {     func drawWithRect(_ rect: CGRect, options options: NSStringDrawingOptions, context context: NSStringDrawingContext?)     func boundingRectWithSize(_ size: CGSize, options options: NSStringDrawingOptions, context context: NSStringDrawingContext?) -> CGRect } extension NSAttributedString {     init(attachment attachment: NSTextAttachment) -> NSAttributedString     class func attributedStringWithAttachment(_ attachment: NSTextAttachment) -> NSAttributedString } ``` |
| To | ``` class NSAttributedString : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     var string: String { get }     func attributesAtIndex(_ location: Int, effectiveRange range: NSRangePointer) -> [String : AnyObject] } extension NSAttributedString {     var length: Int { get }     func attribute(_ attrName: String, atIndex location: Int, effectiveRange range: NSRangePointer) -> AnyObject?     func attributedSubstringFromRange(_ range: NSRange) -> NSAttributedString     func attributesAtIndex(_ location: Int, longestEffectiveRange range: NSRangePointer, inRange rangeLimit: NSRange) -> [String : AnyObject]     func attribute(_ attrName: String, atIndex location: Int, longestEffectiveRange range: NSRangePointer, inRange rangeLimit: NSRange) -> AnyObject?     func isEqualToAttributedString(_ other: NSAttributedString) -> Bool     init(string str: String)     init(string str: String, attributes attrs: [String : AnyObject]?)     init(attributedString attrStr: NSAttributedString)     func enumerateAttributesInRange(_ enumerationRange: NSRange, options opts: NSAttributedStringEnumerationOptions, usingBlock block: ([String : AnyObject], NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateAttribute(_ attrName: String, inRange enumerationRange: NSRange, options opts: NSAttributedStringEnumerationOptions, usingBlock block: (AnyObject?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) } extension NSAttributedString {     init(URL url: NSURL, options options: [String : AnyObject], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws     init(data data: NSData, options options: [String : AnyObject], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws     func dataFromRange(_ range: NSRange, documentAttributes dict: [String : AnyObject]) throws -> NSData     func fileWrapperFromRange(_ range: NSRange, documentAttributes dict: [String : AnyObject]) throws -> NSFileWrapper } extension NSAttributedString {     func containsAttachmentsInRange(_ range: NSRange) -> Bool } extension NSAttributedString {     init(fileURL url: NSURL, options options: [NSObject : AnyObject], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws } extension NSAttributedString {     func size() -> CGSize     func drawAtPoint(_ point: CGPoint)     func drawInRect(_ rect: CGRect) } extension NSAttributedString {     func drawWithRect(_ rect: CGRect, options options: NSStringDrawingOptions, context context: NSStringDrawingContext?)     func boundingRectWithSize(_ size: CGSize, options options: NSStringDrawingOptions, context context: NSStringDrawingContext?) -> CGRect } extension NSAttributedString {      init(attachment attachment: NSTextAttachment)     class func attributedStringWithAttachment(_ attachment: NSTextAttachment) -> NSAttributedString } ``` |

Modified [NSAttributedString.attributesAtIndex(_: Int, effectiveRange: NSRangePointer) -> [String : AnyObject]](https://developer.apple.com/documentation/foundation/nsattributedstring/1415682-attributes)

|  | Declaration |
| --- | --- |
| From | ``` func attributesAtIndex(_ location: Int, effectiveRange range: NSRangePointer) -> [NSObject : AnyObject] ``` |
| To | ``` func attributesAtIndex(_ location: Int, effectiveRange range: NSRangePointer) -> [String : AnyObject] ``` |

Modified [NSAttributedString.attributesAtIndex(_: Int, longestEffectiveRange: NSRangePointer, inRange: NSRange) -> [String : AnyObject]](https://developer.apple.com/documentation/foundation/nsattributedstring/1410494-attributesatindex)

|  | Declaration |
| --- | --- |
| From | ``` func attributesAtIndex(_ location: Int, longestEffectiveRange range: NSRangePointer, inRange rangeLimit: NSRange) -> [NSObject : AnyObject] ``` |
| To | ``` func attributesAtIndex(_ location: Int, longestEffectiveRange range: NSRangePointer, inRange rangeLimit: NSRange) -> [String : AnyObject] ``` |

Modified [NSAttributedString.enumerateAttribute(_: String, inRange: NSRange, options: NSAttributedStringEnumerationOptions, usingBlock: (AnyObject?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/foundation/nsattributedstring/1412461-enumerateattribute)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateAttribute(_ attrName: String, inRange enumerationRange: NSRange, options opts: NSAttributedStringEnumerationOptions, usingBlock block: (AnyObject!, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateAttribute(_ attrName: String, inRange enumerationRange: NSRange, options opts: NSAttributedStringEnumerationOptions, usingBlock block: (AnyObject?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [NSAttributedString.enumerateAttributesInRange(_: NSRange, options: NSAttributedStringEnumerationOptions, usingBlock: ([String : AnyObject], NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/foundation/nsattributedstring/1412070-enumerateattributesinrange)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateAttributesInRange(_ enumerationRange: NSRange, options opts: NSAttributedStringEnumerationOptions, usingBlock block: ([NSObject : AnyObject]!, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateAttributesInRange(_ enumerationRange: NSRange, options opts: NSAttributedStringEnumerationOptions, usingBlock block: ([String : AnyObject], NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [NSAttributedString.init(string: String, attributes: [String : AnyObject]?)](https://developer.apple.com/documentation/foundation/nsattributedstring/1408136-init)

|  | Declaration |
| --- | --- |
| From | ``` init(string str: String, attributes attrs: [NSObject : AnyObject]?) ``` |
| To | ``` init(string str: String, attributes attrs: [String : AnyObject]?) ``` |

Modified [NSAttributedStringEnumerationOptions [struct]](https://developer.apple.com/documentation/foundation/nsattributedstring/enumerationoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSAttributedStringEnumerationOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Reverse: NSAttributedStringEnumerationOptions { get }     static var LongestEffectiveRangeNotRequired: NSAttributedStringEnumerationOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSAttributedStringEnumerationOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var Reverse: NSAttributedStringEnumerationOptions { get }     static var LongestEffectiveRangeNotRequired: NSAttributedStringEnumerationOptions { get } } ``` | OptionSetType |

Modified [NSBinarySearchingOptions [struct]](https://developer.apple.com/documentation/foundation/nsbinarysearchingoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSBinarySearchingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var FirstEqual: NSBinarySearchingOptions { get }     static var LastEqual: NSBinarySearchingOptions { get }     static var InsertionIndex: NSBinarySearchingOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSBinarySearchingOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var FirstEqual: NSBinarySearchingOptions { get }     static var LastEqual: NSBinarySearchingOptions { get }     static var InsertionIndex: NSBinarySearchingOptions { get } } ``` | OptionSetType |

Modified [NSBlockOperation](https://developer.apple.com/documentation/foundation/nsblockoperation)

|  | Declaration |
| --- | --- |
| From | ``` class NSBlockOperation : NSOperation {     convenience init(block block: () -> Void)     class func blockOperationWithBlock(_ block: () -> Void) -> Self     func addExecutionBlock(_ block: () -> Void)     var executionBlocks: [AnyObject] { get } } ``` |
| To | ``` class NSBlockOperation : NSOperation {     convenience init(block block: () -> Void)     class func blockOperationWithBlock(_ block: () -> Void) -> Self     func addExecutionBlock(_ block: () -> Void)     var executionBlocks: [() -> Void] { get } } ``` |

Modified [NSBlockOperation.executionBlocks](https://developer.apple.com/documentation/foundation/nsblockoperation/1416555-executionblocks)

|  | Declaration |
| --- | --- |
| From | ``` var executionBlocks: [AnyObject] { get } ``` |
| To | ``` var executionBlocks: [() -> Void] { get } ``` |

Modified [NSBundle](https://developer.apple.com/documentation/foundation/nsbundle)

|  | Declaration |
| --- | --- |
| From | ``` class NSBundle : NSObject {     class func mainBundle() -> NSBundle     convenience init?(path path: String)     class func bundleWithPath(_ path: String) -> Self?     init?(path path: String)     convenience init?(URL url: NSURL)     class func bundleWithURL(_ url: NSURL) -> Self?     convenience init?(URL url: NSURL)     init(forClass aClass: AnyClass) -> NSBundle     class func bundleForClass(_ aClass: AnyClass) -> NSBundle     init?(identifier identifier: String) -> NSBundle     class func bundleWithIdentifier(_ identifier: String) -> NSBundle?     class func allBundles() -> [AnyObject]     class func allFrameworks() -> [AnyObject]     func load() -> Bool     var loaded: Bool { get }     func unload() -> Bool     func preflightAndReturnError(_ error: NSErrorPointer) -> Bool     func loadAndReturnError(_ error: NSErrorPointer) -> Bool     @NSCopying var bundleURL: NSURL { get }     @NSCopying var resourceURL: NSURL? { get }     @NSCopying var executableURL: NSURL? { get }     func URLForAuxiliaryExecutable(_ executableName: String) -> NSURL?     @NSCopying var privateFrameworksURL: NSURL? { get }     @NSCopying var sharedFrameworksURL: NSURL? { get }     @NSCopying var sharedSupportURL: NSURL? { get }     @NSCopying var builtInPlugInsURL: NSURL? { get }     @NSCopying var appStoreReceiptURL: NSURL? { get }     var bundlePath: String { get }     var resourcePath: String? { get }     var executablePath: String? { get }     func pathForAuxiliaryExecutable(_ executableName: String) -> String?     var privateFrameworksPath: String? { get }     var sharedFrameworksPath: String? { get }     var sharedSupportPath: String? { get }     var builtInPlugInsPath: String? { get }     class func URLForResource(_ name: String, withExtension ext: String?, subdirectory subpath: String?, inBundleWithURL bundleURL: NSURL) -> NSURL?     class func URLsForResourcesWithExtension(_ ext: String?, subdirectory subpath: String?, inBundleWithURL bundleURL: NSURL) -> [AnyObject]?     func URLForResource(_ name: String, withExtension ext: String?) -> NSURL?     func URLForResource(_ name: String, withExtension ext: String?, subdirectory subpath: String?) -> NSURL?     func URLForResource(_ name: String, withExtension ext: String?, subdirectory subpath: String?, localization localizationName: String?) -> NSURL?     func URLsForResourcesWithExtension(_ ext: String?, subdirectory subpath: String?) -> [AnyObject]?     func URLsForResourcesWithExtension(_ ext: String?, subdirectory subpath: String?, localization localizationName: String?) -> [AnyObject]?     class func pathForResource(_ name: String?, ofType ext: String?, inDirectory bundlePath: String) -> String?     class func pathsForResourcesOfType(_ ext: String?, inDirectory bundlePath: String) -> [AnyObject]     func pathForResource(_ name: String?, ofType ext: String?) -> String?     func pathForResource(_ name: String?, ofType ext: String?, inDirectory subpath: String?) -> String?     func pathForResource(_ name: String?, ofType ext: String?, inDirectory subpath: String?, forLocalization localizationName: String?) -> String?     func pathsForResourcesOfType(_ ext: String?, inDirectory subpath: String?) -> [AnyObject]     func pathsForResourcesOfType(_ ext: String?, inDirectory subpath: String?, forLocalization localizationName: String?) -> [AnyObject]     func localizedStringForKey(_ key: String, value value: String?, table tableName: String?) -> String     var bundleIdentifier: String? { get }     var infoDictionary: [NSObject : AnyObject]? { get }     var localizedInfoDictionary: [NSObject : AnyObject]? { get }     func objectForInfoDictionaryKey(_ key: String) -> AnyObject?     func classNamed(_ className: String) -> AnyClass?     var principalClass: AnyClass? { get }     var preferredLocalizations: [AnyObject] { get }     var localizations: [AnyObject]? { get }     var developmentLocalization: String? { get }     class func preferredLocalizationsFromArray(_ localizationsArray: [AnyObject]) -> [AnyObject]     class func preferredLocalizationsFromArray(_ localizationsArray: [AnyObject], forPreferences preferencesArray: [AnyObject]?) -> [AnyObject]     var executableArchitectures: [AnyObject]? { get } } extension NSBundle {     func loadNibNamed(_ name: String!, owner owner: AnyObject!, options options: [NSObject : AnyObject]!) -> [AnyObject]! } ``` |
| To | ``` class NSBundle : NSObject {     class func mainBundle() -> NSBundle     convenience init?(path path: String)     class func bundleWithPath(_ path: String) -> Self?     init?(path path: String)     convenience init?(URL url: NSURL)     class func bundleWithURL(_ url: NSURL) -> Self?     convenience init?(URL url: NSURL)      init(forClass aClass: AnyClass)     class func bundleForClass(_ aClass: AnyClass) -> NSBundle      init?(identifier identifier: String)     class func bundleWithIdentifier(_ identifier: String) -> NSBundle?     class func allBundles() -> [NSBundle]     class func allFrameworks() -> [NSBundle]     func load() -> Bool     var loaded: Bool { get }     func unload() -> Bool     func preflight() throws     func loadAndReturnError() throws     @NSCopying var bundleURL: NSURL { get }     @NSCopying var resourceURL: NSURL? { get }     @NSCopying var executableURL: NSURL? { get }     func URLForAuxiliaryExecutable(_ executableName: String) -> NSURL?     @NSCopying var privateFrameworksURL: NSURL? { get }     @NSCopying var sharedFrameworksURL: NSURL? { get }     @NSCopying var sharedSupportURL: NSURL? { get }     @NSCopying var builtInPlugInsURL: NSURL? { get }     @NSCopying var appStoreReceiptURL: NSURL? { get }     var bundlePath: String { get }     var resourcePath: String? { get }     var executablePath: String? { get }     func pathForAuxiliaryExecutable(_ executableName: String) -> String?     var privateFrameworksPath: String? { get }     var sharedFrameworksPath: String? { get }     var sharedSupportPath: String? { get }     var builtInPlugInsPath: String? { get }     class func URLForResource(_ name: String?, withExtension ext: String?, subdirectory subpath: String?, inBundleWithURL bundleURL: NSURL) -> NSURL?     class func URLsForResourcesWithExtension(_ ext: String?, subdirectory subpath: String?, inBundleWithURL bundleURL: NSURL) -> [NSURL]?     func URLForResource(_ name: String?, withExtension ext: String?) -> NSURL?     func URLForResource(_ name: String?, withExtension ext: String?, subdirectory subpath: String?) -> NSURL?     func URLForResource(_ name: String?, withExtension ext: String?, subdirectory subpath: String?, localization localizationName: String?) -> NSURL?     func URLsForResourcesWithExtension(_ ext: String?, subdirectory subpath: String?) -> [NSURL]?     func URLsForResourcesWithExtension(_ ext: String?, subdirectory subpath: String?, localization localizationName: String?) -> [NSURL]?     class func pathForResource(_ name: String?, ofType ext: String?, inDirectory bundlePath: String) -> String?     class func pathsForResourcesOfType(_ ext: String?, inDirectory bundlePath: String) -> [String]     func pathForResource(_ name: String?, ofType ext: String?) -> String?     func pathForResource(_ name: String?, ofType ext: String?, inDirectory subpath: String?) -> String?     func pathForResource(_ name: String?, ofType ext: String?, inDirectory subpath: String?, forLocalization localizationName: String?) -> String?     func pathsForResourcesOfType(_ ext: String?, inDirectory subpath: String?) -> [String]     func pathsForResourcesOfType(_ ext: String?, inDirectory subpath: String?, forLocalization localizationName: String?) -> [String]     func localizedStringForKey(_ key: String, value value: String?, table tableName: String?) -> String     var bundleIdentifier: String? { get }     var infoDictionary: [String : AnyObject]? { get }     var localizedInfoDictionary: [String : AnyObject]? { get }     func objectForInfoDictionaryKey(_ key: String) -> AnyObject?     func classNamed(_ className: String) -> AnyClass?     var principalClass: AnyClass? { get }     var preferredLocalizations: [String] { get }     var localizations: [String] { get }     var developmentLocalization: String? { get }     class func preferredLocalizationsFromArray(_ localizationsArray: [String]) -> [String]     class func preferredLocalizationsFromArray(_ localizationsArray: [String], forPreferences preferencesArray: [String]?) -> [String]     var executableArchitectures: [NSNumber]? { get } } extension NSBundle {     func setPreservationPriority(_ priority: Double, forTags tags: Set<String>)     func preservationPriorityForTag(_ tag: String) -> Double } extension NSBundle {     func loadNibNamed(_ name: String!, owner owner: AnyObject!, options options: [NSObject : AnyObject]!) -> [AnyObject]! } ``` |

Modified [NSBundle.allBundles() -> [NSBundle] [class]](https://developer.apple.com/documentation/foundation/bundle/1413705-allbundles)

|  | Declaration |
| --- | --- |
| From | ``` class func allBundles() -> [AnyObject] ``` |
| To | ``` class func allBundles() -> [NSBundle] ``` |

Modified [NSBundle.allFrameworks() -> [NSBundle] [class]](https://developer.apple.com/documentation/foundation/nsbundle/1408056-allframeworks)

|  | Declaration |
| --- | --- |
| From | ``` class func allFrameworks() -> [AnyObject] ``` |
| To | ``` class func allFrameworks() -> [NSBundle] ``` |

Modified [NSBundle.executableArchitectures](https://developer.apple.com/documentation/foundation/bundle/1415499-executablearchitectures)

|  | Declaration |
| --- | --- |
| From | ``` var executableArchitectures: [AnyObject]? { get } ``` |
| To | ``` var executableArchitectures: [NSNumber]? { get } ``` |

Modified [NSBundle.infoDictionary](https://developer.apple.com/documentation/foundation/bundle/1413477-infodictionary)

|  | Declaration |
| --- | --- |
| From | ``` var infoDictionary: [NSObject : AnyObject]? { get } ``` |
| To | ``` var infoDictionary: [String : AnyObject]? { get } ``` |

Modified [NSBundle.init(forClass: AnyClass)](https://developer.apple.com/documentation/foundation/bundle/1417717-init)

|  | Declaration |
| --- | --- |
| From | ``` init(forClass aClass: AnyClass) -> NSBundle ``` |
| To | ``` init(forClass aClass: AnyClass) ``` |

Modified [NSBundle.init(identifier: String)](https://developer.apple.com/documentation/foundation/bundle/1411929-init)

|  | Declaration |
| --- | --- |
| From | ``` init?(identifier identifier: String) -> NSBundle ``` |
| To | ``` init?(identifier identifier: String) ``` |

Modified [NSBundle.loadAndReturnError() throws](https://developer.apple.com/documentation/foundation/bundle/1411819-loadandreturnerror)

|  | Declaration |
| --- | --- |
| From | ``` func loadAndReturnError(_ error: NSErrorPointer) -> Bool ``` |
| To | ``` func loadAndReturnError() throws ``` |

Modified [NSBundle.localizations](https://developer.apple.com/documentation/foundation/bundle/1417415-localizations)

|  | Declaration |
| --- | --- |
| From | ``` var localizations: [AnyObject]? { get } ``` |
| To | ``` var localizations: [String] { get } ``` |

Modified [NSBundle.localizedInfoDictionary](https://developer.apple.com/documentation/foundation/bundle/1407645-localizedinfodictionary)

|  | Declaration |
| --- | --- |
| From | ``` var localizedInfoDictionary: [NSObject : AnyObject]? { get } ``` |
| To | ``` var localizedInfoDictionary: [String : AnyObject]? { get } ``` |

Modified [NSBundle.pathsForResourcesOfType(_: String?, inDirectory: String) -> [String] [class]](https://developer.apple.com/documentation/foundation/bundle/1415876-paths)

|  | Declaration |
| --- | --- |
| From | ``` class func pathsForResourcesOfType(_ ext: String?, inDirectory bundlePath: String) -> [AnyObject] ``` |
| To | ``` class func pathsForResourcesOfType(_ ext: String?, inDirectory bundlePath: String) -> [String] ``` |

Modified [NSBundle.pathsForResourcesOfType(_: String?, inDirectory: String?) -> [String]](https://developer.apple.com/documentation/foundation/bundle/1413058-paths)

|  | Declaration |
| --- | --- |
| From | ``` func pathsForResourcesOfType(_ ext: String?, inDirectory subpath: String?) -> [AnyObject] ``` |
| To | ``` func pathsForResourcesOfType(_ ext: String?, inDirectory subpath: String?) -> [String] ``` |

Modified [NSBundle.pathsForResourcesOfType(_: String?, inDirectory: String?, forLocalization: String?) -> [String]](https://developer.apple.com/documentation/foundation/bundle/1416940-paths)

|  | Declaration |
| --- | --- |
| From | ``` func pathsForResourcesOfType(_ ext: String?, inDirectory subpath: String?, forLocalization localizationName: String?) -> [AnyObject] ``` |
| To | ``` func pathsForResourcesOfType(_ ext: String?, inDirectory subpath: String?, forLocalization localizationName: String?) -> [String] ``` |

Modified [NSBundle.preferredLocalizations](https://developer.apple.com/documentation/foundation/bundle/1413220-preferredlocalizations)

|  | Declaration |
| --- | --- |
| From | ``` var preferredLocalizations: [AnyObject] { get } ``` |
| To | ``` var preferredLocalizations: [String] { get } ``` |

Modified [NSBundle.preferredLocalizationsFromArray(_: [String]) -> [String] [class]](https://developer.apple.com/documentation/foundation/bundle/1417249-preferredlocalizations)

|  | Declaration |
| --- | --- |
| From | ``` class func preferredLocalizationsFromArray(_ localizationsArray: [AnyObject]) -> [AnyObject] ``` |
| To | ``` class func preferredLocalizationsFromArray(_ localizationsArray: [String]) -> [String] ``` |

Modified [NSBundle.preferredLocalizationsFromArray(_: [String], forPreferences: [String]?) -> [String] [class]](https://developer.apple.com/documentation/foundation/bundle/1409418-preferredlocalizations)

|  | Declaration |
| --- | --- |
| From | ``` class func preferredLocalizationsFromArray(_ localizationsArray: [AnyObject], forPreferences preferencesArray: [AnyObject]?) -> [AnyObject] ``` |
| To | ``` class func preferredLocalizationsFromArray(_ localizationsArray: [String], forPreferences preferencesArray: [String]?) -> [String] ``` |

Modified [NSBundle.preflight() throws](https://developer.apple.com/documentation/foundation/bundle/1415083-preflight)

|  | Declaration |
| --- | --- |
| From | ``` func preflightAndReturnError(_ error: NSErrorPointer) -> Bool ``` |
| To | ``` func preflight() throws ``` |

Modified [NSBundle.URLForResource(_: String?, withExtension: String?) -> NSURL?](https://developer.apple.com/documentation/foundation/nsbundle/1411540-urlforresource)

|  | Declaration |
| --- | --- |
| From | ``` func URLForResource(_ name: String, withExtension ext: String?) -> NSURL? ``` |
| To | ``` func URLForResource(_ name: String?, withExtension ext: String?) -> NSURL? ``` |

Modified [NSBundle.URLForResource(_: String?, withExtension: String?, subdirectory: String?) -> NSURL?](https://developer.apple.com/documentation/foundation/nsbundle/1416712-urlforresource)

|  | Declaration |
| --- | --- |
| From | ``` func URLForResource(_ name: String, withExtension ext: String?, subdirectory subpath: String?) -> NSURL? ``` |
| To | ``` func URLForResource(_ name: String?, withExtension ext: String?, subdirectory subpath: String?) -> NSURL? ``` |

Modified [NSBundle.URLForResource(_: String?, withExtension: String?, subdirectory: String?, inBundleWithURL: NSURL) -> NSURL? [class]](https://developer.apple.com/documentation/foundation/nsbundle/1416361-urlforresource)

|  | Declaration |
| --- | --- |
| From | ``` class func URLForResource(_ name: String, withExtension ext: String?, subdirectory subpath: String?, inBundleWithURL bundleURL: NSURL) -> NSURL? ``` |
| To | ``` class func URLForResource(_ name: String?, withExtension ext: String?, subdirectory subpath: String?, inBundleWithURL bundleURL: NSURL) -> NSURL? ``` |

Modified [NSBundle.URLForResource(_: String?, withExtension: String?, subdirectory: String?, localization: String?) -> NSURL?](https://developer.apple.com/documentation/foundation/bundle/1417378-url)

|  | Declaration |
| --- | --- |
| From | ``` func URLForResource(_ name: String, withExtension ext: String?, subdirectory subpath: String?, localization localizationName: String?) -> NSURL? ``` |
| To | ``` func URLForResource(_ name: String?, withExtension ext: String?, subdirectory subpath: String?, localization localizationName: String?) -> NSURL? ``` |

Modified [NSBundle.URLsForResourcesWithExtension(_: String?, subdirectory: String?) -> [NSURL]?](https://developer.apple.com/documentation/foundation/nsbundle/1407424-urlsforresourceswithextension)

|  | Declaration |
| --- | --- |
| From | ``` func URLsForResourcesWithExtension(_ ext: String?, subdirectory subpath: String?) -> [AnyObject]? ``` |
| To | ``` func URLsForResourcesWithExtension(_ ext: String?, subdirectory subpath: String?) -> [NSURL]? ``` |

Modified [NSBundle.URLsForResourcesWithExtension(_: String?, subdirectory: String?, inBundleWithURL: NSURL) -> [NSURL]? [class]](https://developer.apple.com/documentation/foundation/nsbundle/1409807-urlsforresourceswithextension)

|  | Declaration |
| --- | --- |
| From | ``` class func URLsForResourcesWithExtension(_ ext: String?, subdirectory subpath: String?, inBundleWithURL bundleURL: NSURL) -> [AnyObject]? ``` |
| To | ``` class func URLsForResourcesWithExtension(_ ext: String?, subdirectory subpath: String?, inBundleWithURL bundleURL: NSURL) -> [NSURL]? ``` |

Modified [NSBundle.URLsForResourcesWithExtension(_: String?, subdirectory: String?, localization: String?) -> [NSURL]?](https://developer.apple.com/documentation/foundation/bundle/1414688-urls)

|  | Declaration |
| --- | --- |
| From | ``` func URLsForResourcesWithExtension(_ ext: String?, subdirectory subpath: String?, localization localizationName: String?) -> [AnyObject]? ``` |
| To | ``` func URLsForResourcesWithExtension(_ ext: String?, subdirectory subpath: String?, localization localizationName: String?) -> [NSURL]? ``` |

Modified [NSByteCountFormatterCountStyle [enum]](https://developer.apple.com/documentation/foundation/nsbytecountformattercountstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NSByteCountFormatterUnits [struct]](https://developer.apple.com/documentation/foundation/bytecountformatter/units)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSByteCountFormatterUnits : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var UseDefault: NSByteCountFormatterUnits { get }     static var UseBytes: NSByteCountFormatterUnits { get }     static var UseKB: NSByteCountFormatterUnits { get }     static var UseMB: NSByteCountFormatterUnits { get }     static var UseGB: NSByteCountFormatterUnits { get }     static var UseTB: NSByteCountFormatterUnits { get }     static var UsePB: NSByteCountFormatterUnits { get }     static var UseEB: NSByteCountFormatterUnits { get }     static var UseZB: NSByteCountFormatterUnits { get }     static var UseYBOrHigher: NSByteCountFormatterUnits { get }     static var UseAll: NSByteCountFormatterUnits { get } } ``` | RawOptionSetType |
| To | ``` struct NSByteCountFormatterUnits : OptionSetType {     init(rawValue rawValue: UInt)     static var UseDefault: NSByteCountFormatterUnits { get }     static var UseBytes: NSByteCountFormatterUnits { get }     static var UseKB: NSByteCountFormatterUnits { get }     static var UseMB: NSByteCountFormatterUnits { get }     static var UseGB: NSByteCountFormatterUnits { get }     static var UseTB: NSByteCountFormatterUnits { get }     static var UsePB: NSByteCountFormatterUnits { get }     static var UseEB: NSByteCountFormatterUnits { get }     static var UseZB: NSByteCountFormatterUnits { get }     static var UseYBOrHigher: NSByteCountFormatterUnits { get }     static var UseAll: NSByteCountFormatterUnits { get } } ``` | OptionSetType |

Modified [NSCacheDelegate.cache(_: NSCache, willEvictObject: AnyObject)](https://developer.apple.com/documentation/foundation/nscachedelegate/1416107-cache)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified [NSCalculationError [enum]](https://developer.apple.com/documentation/foundation/nscalculationerror)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSCalendar](https://developer.apple.com/documentation/foundation/nscalendar)

|  | Declaration |
| --- | --- |
| From | ``` class NSCalendar : NSObject, NSCopying, NSSecureCoding, NSCoding {     class func currentCalendar() -> NSCalendar     class func autoupdatingCurrentCalendar() -> NSCalendar     init?(identifier calendarIdentifierConstant: String) -> NSCalendar     class func calendarWithIdentifier(_ calendarIdentifierConstant: String) -> NSCalendar?     init?(calendarIdentifier ident: String)     var calendarIdentifier: String { get }     @NSCopying var locale: NSLocale?     @NSCopying var timeZone: NSTimeZone     var firstWeekday: Int     var minimumDaysInFirstWeek: Int     var eraSymbols: [AnyObject] { get }     var longEraSymbols: [AnyObject] { get }     var monthSymbols: [AnyObject] { get }     var shortMonthSymbols: [AnyObject] { get }     var veryShortMonthSymbols: [AnyObject] { get }     var standaloneMonthSymbols: [AnyObject] { get }     var shortStandaloneMonthSymbols: [AnyObject] { get }     var veryShortStandaloneMonthSymbols: [AnyObject] { get }     var weekdaySymbols: [AnyObject] { get }     var shortWeekdaySymbols: [AnyObject] { get }     var veryShortWeekdaySymbols: [AnyObject] { get }     var standaloneWeekdaySymbols: [AnyObject] { get }     var shortStandaloneWeekdaySymbols: [AnyObject] { get }     var veryShortStandaloneWeekdaySymbols: [AnyObject] { get }     var quarterSymbols: [AnyObject] { get }     var shortQuarterSymbols: [AnyObject] { get }     var standaloneQuarterSymbols: [AnyObject] { get }     var shortStandaloneQuarterSymbols: [AnyObject] { get }     var AMSymbol: String { get }     var PMSymbol: String { get }     func minimumRangeOfUnit(_ unit: NSCalendarUnit) -> NSRange     func maximumRangeOfUnit(_ unit: NSCalendarUnit) -> NSRange     func rangeOfUnit(_ smaller: NSCalendarUnit, inUnit larger: NSCalendarUnit, forDate date: NSDate) -> NSRange     func ordinalityOfUnit(_ smaller: NSCalendarUnit, inUnit larger: NSCalendarUnit, forDate date: NSDate) -> Int     func rangeOfUnit(_ unit: NSCalendarUnit, startDate datep: AutoreleasingUnsafeMutablePointer<NSDate?>, interval tip: UnsafeMutablePointer<NSTimeInterval>, forDate date: NSDate) -> Bool     func dateFromComponents(_ comps: NSDateComponents) -> NSDate?     func components(_ unitFlags: NSCalendarUnit, fromDate date: NSDate) -> NSDateComponents     func dateByAddingComponents(_ comps: NSDateComponents, toDate date: NSDate, options opts: NSCalendarOptions) -> NSDate?     func components(_ unitFlags: NSCalendarUnit, fromDate startingDate: NSDate, toDate resultDate: NSDate, options opts: NSCalendarOptions) -> NSDateComponents     func getEra(_ eraValuePointer: UnsafeMutablePointer<Int>, year yearValuePointer: UnsafeMutablePointer<Int>, month monthValuePointer: UnsafeMutablePointer<Int>, day dayValuePointer: UnsafeMutablePointer<Int>, fromDate date: NSDate)     func getEra(_ eraValuePointer: UnsafeMutablePointer<Int>, yearForWeekOfYear yearValuePointer: UnsafeMutablePointer<Int>, weekOfYear weekValuePointer: UnsafeMutablePointer<Int>, weekday weekdayValuePointer: UnsafeMutablePointer<Int>, fromDate date: NSDate)     func getHour(_ hourValuePointer: UnsafeMutablePointer<Int>, minute minuteValuePointer: UnsafeMutablePointer<Int>, second secondValuePointer: UnsafeMutablePointer<Int>, nanosecond nanosecondValuePointer: UnsafeMutablePointer<Int>, fromDate date: NSDate)     func component(_ unit: NSCalendarUnit, fromDate date: NSDate) -> Int     func dateWithEra(_ eraValue: Int, year yearValue: Int, month monthValue: Int, day dayValue: Int, hour hourValue: Int, minute minuteValue: Int, second secondValue: Int, nanosecond nanosecondValue: Int) -> NSDate?     func dateWithEra(_ eraValue: Int, yearForWeekOfYear yearValue: Int, weekOfYear weekValue: Int, weekday weekdayValue: Int, hour hourValue: Int, minute minuteValue: Int, second secondValue: Int, nanosecond nanosecondValue: Int) -> NSDate?     func startOfDayForDate(_ date: NSDate) -> NSDate     func componentsInTimeZone(_ timezone: NSTimeZone, fromDate date: NSDate) -> NSDateComponents     func compareDate(_ date1: NSDate, toDate date2: NSDate, toUnitGranularity unit: NSCalendarUnit) -> NSComparisonResult     func isDate(_ date1: NSDate, equalToDate date2: NSDate, toUnitGranularity unit: NSCalendarUnit) -> Bool     func isDate(_ date1: NSDate, inSameDayAsDate date2: NSDate) -> Bool     func isDateInToday(_ date: NSDate) -> Bool     func isDateInYesterday(_ date: NSDate) -> Bool     func isDateInTomorrow(_ date: NSDate) -> Bool     func isDateInWeekend(_ date: NSDate) -> Bool     func rangeOfWeekendStartDate(_ datep: AutoreleasingUnsafeMutablePointer<NSDate?>, interval tip: UnsafeMutablePointer<NSTimeInterval>, containingDate date: NSDate) -> Bool     func nextWeekendStartDate(_ datep: AutoreleasingUnsafeMutablePointer<NSDate?>, interval tip: UnsafeMutablePointer<NSTimeInterval>, options options: NSCalendarOptions, afterDate date: NSDate) -> Bool     func components(_ unitFlags: NSCalendarUnit, fromDateComponents startingDateComp: NSDateComponents, toDateComponents resultDateComp: NSDateComponents, options options: NSCalendarOptions) -> NSDateComponents     func dateByAddingUnit(_ unit: NSCalendarUnit, value value: Int, toDate date: NSDate, options options: NSCalendarOptions) -> NSDate?     func enumerateDatesStartingAfterDate(_ start: NSDate, matchingComponents comps: NSDateComponents, options opts: NSCalendarOptions, usingBlock block: (NSDate!, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)     func nextDateAfterDate(_ date: NSDate, matchingComponents comps: NSDateComponents, options options: NSCalendarOptions) -> NSDate?     func nextDateAfterDate(_ date: NSDate, matchingUnit unit: NSCalendarUnit, value value: Int, options options: NSCalendarOptions) -> NSDate?     func nextDateAfterDate(_ date: NSDate, matchingHour hourValue: Int, minute minuteValue: Int, second secondValue: Int, options options: NSCalendarOptions) -> NSDate?     func dateBySettingUnit(_ unit: NSCalendarUnit, value v: Int, ofDate date: NSDate, options opts: NSCalendarOptions) -> NSDate?     func dateBySettingHour(_ h: Int, minute m: Int, second s: Int, ofDate date: NSDate, options opts: NSCalendarOptions) -> NSDate?     func date(_ date: NSDate, matchesComponents components: NSDateComponents) -> Bool } ``` |
| To | ``` class NSCalendar : NSObject, NSCopying, NSSecureCoding, NSCoding {     class func currentCalendar() -> NSCalendar     class func autoupdatingCurrentCalendar() -> NSCalendar      init?(identifier calendarIdentifierConstant: String)     class func calendarWithIdentifier(_ calendarIdentifierConstant: String) -> NSCalendar?     convenience init()     init?(calendarIdentifier ident: String)     var calendarIdentifier: String { get }     @NSCopying var locale: NSLocale?     @NSCopying var timeZone: NSTimeZone     var firstWeekday: Int     var minimumDaysInFirstWeek: Int     var eraSymbols: [String] { get }     var longEraSymbols: [String] { get }     var monthSymbols: [String] { get }     var shortMonthSymbols: [String] { get }     var veryShortMonthSymbols: [String] { get }     var standaloneMonthSymbols: [String] { get }     var shortStandaloneMonthSymbols: [String] { get }     var veryShortStandaloneMonthSymbols: [String] { get }     var weekdaySymbols: [String] { get }     var shortWeekdaySymbols: [String] { get }     var veryShortWeekdaySymbols: [String] { get }     var standaloneWeekdaySymbols: [String] { get }     var shortStandaloneWeekdaySymbols: [String] { get }     var veryShortStandaloneWeekdaySymbols: [String] { get }     var quarterSymbols: [String] { get }     var shortQuarterSymbols: [String] { get }     var standaloneQuarterSymbols: [String] { get }     var shortStandaloneQuarterSymbols: [String] { get }     var AMSymbol: String { get }     var PMSymbol: String { get }     func minimumRangeOfUnit(_ unit: NSCalendarUnit) -> NSRange     func maximumRangeOfUnit(_ unit: NSCalendarUnit) -> NSRange     func rangeOfUnit(_ smaller: NSCalendarUnit, inUnit larger: NSCalendarUnit, forDate date: NSDate) -> NSRange     func ordinalityOfUnit(_ smaller: NSCalendarUnit, inUnit larger: NSCalendarUnit, forDate date: NSDate) -> Int     func rangeOfUnit(_ unit: NSCalendarUnit, startDate datep: AutoreleasingUnsafeMutablePointer<NSDate?>, interval tip: UnsafeMutablePointer<NSTimeInterval>, forDate date: NSDate) -> Bool     func dateFromComponents(_ comps: NSDateComponents) -> NSDate?     func components(_ unitFlags: NSCalendarUnit, fromDate date: NSDate) -> NSDateComponents     func dateByAddingComponents(_ comps: NSDateComponents, toDate date: NSDate, options opts: NSCalendarOptions) -> NSDate?     func components(_ unitFlags: NSCalendarUnit, fromDate startingDate: NSDate, toDate resultDate: NSDate, options opts: NSCalendarOptions) -> NSDateComponents     func getEra(_ eraValuePointer: UnsafeMutablePointer<Int>, year yearValuePointer: UnsafeMutablePointer<Int>, month monthValuePointer: UnsafeMutablePointer<Int>, day dayValuePointer: UnsafeMutablePointer<Int>, fromDate date: NSDate)     func getEra(_ eraValuePointer: UnsafeMutablePointer<Int>, yearForWeekOfYear yearValuePointer: UnsafeMutablePointer<Int>, weekOfYear weekValuePointer: UnsafeMutablePointer<Int>, weekday weekdayValuePointer: UnsafeMutablePointer<Int>, fromDate date: NSDate)     func getHour(_ hourValuePointer: UnsafeMutablePointer<Int>, minute minuteValuePointer: UnsafeMutablePointer<Int>, second secondValuePointer: UnsafeMutablePointer<Int>, nanosecond nanosecondValuePointer: UnsafeMutablePointer<Int>, fromDate date: NSDate)     func component(_ unit: NSCalendarUnit, fromDate date: NSDate) -> Int     func dateWithEra(_ eraValue: Int, year yearValue: Int, month monthValue: Int, day dayValue: Int, hour hourValue: Int, minute minuteValue: Int, second secondValue: Int, nanosecond nanosecondValue: Int) -> NSDate?     func dateWithEra(_ eraValue: Int, yearForWeekOfYear yearValue: Int, weekOfYear weekValue: Int, weekday weekdayValue: Int, hour hourValue: Int, minute minuteValue: Int, second secondValue: Int, nanosecond nanosecondValue: Int) -> NSDate?     func startOfDayForDate(_ date: NSDate) -> NSDate     func componentsInTimeZone(_ timezone: NSTimeZone, fromDate date: NSDate) -> NSDateComponents     func compareDate(_ date1: NSDate, toDate date2: NSDate, toUnitGranularity unit: NSCalendarUnit) -> NSComparisonResult     func isDate(_ date1: NSDate, equalToDate date2: NSDate, toUnitGranularity unit: NSCalendarUnit) -> Bool     func isDate(_ date1: NSDate, inSameDayAsDate date2: NSDate) -> Bool     func isDateInToday(_ date: NSDate) -> Bool     func isDateInYesterday(_ date: NSDate) -> Bool     func isDateInTomorrow(_ date: NSDate) -> Bool     func isDateInWeekend(_ date: NSDate) -> Bool     func rangeOfWeekendStartDate(_ datep: AutoreleasingUnsafeMutablePointer<NSDate?>, interval tip: UnsafeMutablePointer<NSTimeInterval>, containingDate date: NSDate) -> Bool     func nextWeekendStartDate(_ datep: AutoreleasingUnsafeMutablePointer<NSDate?>, interval tip: UnsafeMutablePointer<NSTimeInterval>, options options: NSCalendarOptions, afterDate date: NSDate) -> Bool     func components(_ unitFlags: NSCalendarUnit, fromDateComponents startingDateComp: NSDateComponents, toDateComponents resultDateComp: NSDateComponents, options options: NSCalendarOptions) -> NSDateComponents     func dateByAddingUnit(_ unit: NSCalendarUnit, value value: Int, toDate date: NSDate, options options: NSCalendarOptions) -> NSDate?     func enumerateDatesStartingAfterDate(_ start: NSDate, matchingComponents comps: NSDateComponents, options opts: NSCalendarOptions, usingBlock block: (NSDate?, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)     func nextDateAfterDate(_ date: NSDate, matchingComponents comps: NSDateComponents, options options: NSCalendarOptions) -> NSDate?     func nextDateAfterDate(_ date: NSDate, matchingUnit unit: NSCalendarUnit, value value: Int, options options: NSCalendarOptions) -> NSDate?     func nextDateAfterDate(_ date: NSDate, matchingHour hourValue: Int, minute minuteValue: Int, second secondValue: Int, options options: NSCalendarOptions) -> NSDate?     func dateBySettingUnit(_ unit: NSCalendarUnit, value v: Int, ofDate date: NSDate, options opts: NSCalendarOptions) -> NSDate?     func dateBySettingHour(_ h: Int, minute m: Int, second s: Int, ofDate date: NSDate, options opts: NSCalendarOptions) -> NSDate?     func date(_ date: NSDate, matchesComponents components: NSDateComponents) -> Bool } ``` |

Modified [NSCalendar.enumerateDatesStartingAfterDate(_: NSDate, matchingComponents: NSDateComponents, options: NSCalendarOptions, usingBlock: (NSDate?, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/foundation/nscalendar/1413938-enumeratedatesstartingafterdate)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateDatesStartingAfterDate(_ start: NSDate, matchingComponents comps: NSDateComponents, options opts: NSCalendarOptions, usingBlock block: (NSDate!, Bool, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateDatesStartingAfterDate(_ start: NSDate, matchingComponents comps: NSDateComponents, options opts: NSCalendarOptions, usingBlock block: (NSDate?, Bool, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [NSCalendar.eraSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1415038-erasymbols)

|  | Declaration |
| --- | --- |
| From | ``` var eraSymbols: [AnyObject] { get } ``` |
| To | ``` var eraSymbols: [String] { get } ``` |

Modified [NSCalendar.init(identifier: String)](https://developer.apple.com/documentation/foundation/nscalendar/1412400-calendarwithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` init?(identifier calendarIdentifierConstant: String) -> NSCalendar ``` |
| To | ``` init?(identifier calendarIdentifierConstant: String) ``` |

Modified [NSCalendar.longEraSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1414285-longerasymbols)

|  | Declaration |
| --- | --- |
| From | ``` var longEraSymbols: [AnyObject] { get } ``` |
| To | ``` var longEraSymbols: [String] { get } ``` |

Modified [NSCalendar.monthSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1414872-monthsymbols)

|  | Declaration |
| --- | --- |
| From | ``` var monthSymbols: [AnyObject] { get } ``` |
| To | ``` var monthSymbols: [String] { get } ``` |

Modified [NSCalendar.quarterSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1411517-quartersymbols)

|  | Declaration |
| --- | --- |
| From | ``` var quarterSymbols: [AnyObject] { get } ``` |
| To | ``` var quarterSymbols: [String] { get } ``` |

Modified [NSCalendar.shortMonthSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1408952-shortmonthsymbols)

|  | Declaration |
| --- | --- |
| From | ``` var shortMonthSymbols: [AnyObject] { get } ``` |
| To | ``` var shortMonthSymbols: [String] { get } ``` |

Modified [NSCalendar.shortQuarterSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1414864-shortquartersymbols)

|  | Declaration |
| --- | --- |
| From | ``` var shortQuarterSymbols: [AnyObject] { get } ``` |
| To | ``` var shortQuarterSymbols: [String] { get } ``` |

Modified [NSCalendar.shortStandaloneMonthSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1418180-shortstandalonemonthsymbols)

|  | Declaration |
| --- | --- |
| From | ``` var shortStandaloneMonthSymbols: [AnyObject] { get } ``` |
| To | ``` var shortStandaloneMonthSymbols: [String] { get } ``` |

Modified [NSCalendar.shortStandaloneQuarterSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1409823-shortstandalonequartersymbols)

|  | Declaration |
| --- | --- |
| From | ``` var shortStandaloneQuarterSymbols: [AnyObject] { get } ``` |
| To | ``` var shortStandaloneQuarterSymbols: [String] { get } ``` |

Modified [NSCalendar.shortStandaloneWeekdaySymbols](https://developer.apple.com/documentation/foundation/nscalendar/1413871-shortstandaloneweekdaysymbols)

|  | Declaration |
| --- | --- |
| From | ``` var shortStandaloneWeekdaySymbols: [AnyObject] { get } ``` |
| To | ``` var shortStandaloneWeekdaySymbols: [String] { get } ``` |

Modified [NSCalendar.shortWeekdaySymbols](https://developer.apple.com/documentation/foundation/nscalendar/1407268-shortweekdaysymbols)

|  | Declaration |
| --- | --- |
| From | ``` var shortWeekdaySymbols: [AnyObject] { get } ``` |
| To | ``` var shortWeekdaySymbols: [String] { get } ``` |

Modified [NSCalendar.standaloneMonthSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1409598-standalonemonthsymbols)

|  | Declaration |
| --- | --- |
| From | ``` var standaloneMonthSymbols: [AnyObject] { get } ``` |
| To | ``` var standaloneMonthSymbols: [String] { get } ``` |

Modified [NSCalendar.standaloneQuarterSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1407159-standalonequartersymbols)

|  | Declaration |
| --- | --- |
| From | ``` var standaloneQuarterSymbols: [AnyObject] { get } ``` |
| To | ``` var standaloneQuarterSymbols: [String] { get } ``` |

Modified [NSCalendar.standaloneWeekdaySymbols](https://developer.apple.com/documentation/foundation/nscalendar/1411219-standaloneweekdaysymbols)

|  | Declaration |
| --- | --- |
| From | ``` var standaloneWeekdaySymbols: [AnyObject] { get } ``` |
| To | ``` var standaloneWeekdaySymbols: [String] { get } ``` |

Modified [NSCalendar.veryShortMonthSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1412779-veryshortmonthsymbols)

|  | Declaration |
| --- | --- |
| From | ``` var veryShortMonthSymbols: [AnyObject] { get } ``` |
| To | ``` var veryShortMonthSymbols: [String] { get } ``` |

Modified [NSCalendar.veryShortStandaloneMonthSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1408035-veryshortstandalonemonthsymbols)

|  | Declaration |
| --- | --- |
| From | ``` var veryShortStandaloneMonthSymbols: [AnyObject] { get } ``` |
| To | ``` var veryShortStandaloneMonthSymbols: [String] { get } ``` |

Modified [NSCalendar.veryShortStandaloneWeekdaySymbols](https://developer.apple.com/documentation/foundation/nscalendar/1418273-veryshortstandaloneweekdaysymbol)

|  | Declaration |
| --- | --- |
| From | ``` var veryShortStandaloneWeekdaySymbols: [AnyObject] { get } ``` |
| To | ``` var veryShortStandaloneWeekdaySymbols: [String] { get } ``` |

Modified [NSCalendar.veryShortWeekdaySymbols](https://developer.apple.com/documentation/foundation/nscalendar/1417207-veryshortweekdaysymbols)

|  | Declaration |
| --- | --- |
| From | ``` var veryShortWeekdaySymbols: [AnyObject] { get } ``` |
| To | ``` var veryShortWeekdaySymbols: [String] { get } ``` |

Modified [NSCalendar.weekdaySymbols](https://developer.apple.com/documentation/foundation/nscalendar/1412939-weekdaysymbols)

|  | Declaration |
| --- | --- |
| From | ``` var weekdaySymbols: [AnyObject] { get } ``` |
| To | ``` var weekdaySymbols: [String] { get } ``` |

Modified [NSCalendarOptions [struct]](https://developer.apple.com/documentation/foundation/nscalendaroptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSCalendarOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var WrapComponents: NSCalendarOptions { get }     static var MatchStrictly: NSCalendarOptions { get }     static var SearchBackwards: NSCalendarOptions { get }     static var MatchPreviousTimePreservingSmallerUnits: NSCalendarOptions { get }     static var MatchNextTimePreservingSmallerUnits: NSCalendarOptions { get }     static var MatchNextTime: NSCalendarOptions { get }     static var MatchFirst: NSCalendarOptions { get }     static var MatchLast: NSCalendarOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSCalendarOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var WrapComponents: NSCalendarOptions { get }     static var MatchStrictly: NSCalendarOptions { get }     static var SearchBackwards: NSCalendarOptions { get }     static var MatchPreviousTimePreservingSmallerUnits: NSCalendarOptions { get }     static var MatchNextTimePreservingSmallerUnits: NSCalendarOptions { get }     static var MatchNextTime: NSCalendarOptions { get }     static var MatchFirst: NSCalendarOptions { get }     static var MatchLast: NSCalendarOptions { get } } ``` | OptionSetType |

Modified [NSCalendarUnit [struct]](https://developer.apple.com/documentation/foundation/nscalendarunit)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSCalendarUnit : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var CalendarUnitEra: NSCalendarUnit { get }     static var CalendarUnitYear: NSCalendarUnit { get }     static var CalendarUnitMonth: NSCalendarUnit { get }     static var CalendarUnitDay: NSCalendarUnit { get }     static var CalendarUnitHour: NSCalendarUnit { get }     static var CalendarUnitMinute: NSCalendarUnit { get }     static var CalendarUnitSecond: NSCalendarUnit { get }     static var CalendarUnitWeekday: NSCalendarUnit { get }     static var CalendarUnitWeekdayOrdinal: NSCalendarUnit { get }     static var CalendarUnitQuarter: NSCalendarUnit { get }     static var CalendarUnitWeekOfMonth: NSCalendarUnit { get }     static var CalendarUnitWeekOfYear: NSCalendarUnit { get }     static var CalendarUnitYearForWeekOfYear: NSCalendarUnit { get }     static var CalendarUnitNanosecond: NSCalendarUnit { get }     static var CalendarUnitCalendar: NSCalendarUnit { get }     static var CalendarUnitTimeZone: NSCalendarUnit { get }     static var EraCalendarUnit: NSCalendarUnit { get }     static var YearCalendarUnit: NSCalendarUnit { get }     static var MonthCalendarUnit: NSCalendarUnit { get }     static var DayCalendarUnit: NSCalendarUnit { get }     static var HourCalendarUnit: NSCalendarUnit { get }     static var MinuteCalendarUnit: NSCalendarUnit { get }     static var SecondCalendarUnit: NSCalendarUnit { get }     static var WeekCalendarUnit: NSCalendarUnit { get }     static var WeekdayCalendarUnit: NSCalendarUnit { get }     static var WeekdayOrdinalCalendarUnit: NSCalendarUnit { get }     static var QuarterCalendarUnit: NSCalendarUnit { get }     static var WeekOfMonthCalendarUnit: NSCalendarUnit { get }     static var WeekOfYearCalendarUnit: NSCalendarUnit { get }     static var YearForWeekOfYearCalendarUnit: NSCalendarUnit { get }     static var CalendarCalendarUnit: NSCalendarUnit { get }     static var TimeZoneCalendarUnit: NSCalendarUnit { get } } ``` | RawOptionSetType |
| To | ``` struct NSCalendarUnit : OptionSetType {     init(rawValue rawValue: UInt)     static var Era: NSCalendarUnit { get }     static var Year: NSCalendarUnit { get }     static var Month: NSCalendarUnit { get }     static var Day: NSCalendarUnit { get }     static var Hour: NSCalendarUnit { get }     static var Minute: NSCalendarUnit { get }     static var Second: NSCalendarUnit { get }     static var Weekday: NSCalendarUnit { get }     static var WeekdayOrdinal: NSCalendarUnit { get }     static var Quarter: NSCalendarUnit { get }     static var WeekOfMonth: NSCalendarUnit { get }     static var WeekOfYear: NSCalendarUnit { get }     static var YearForWeekOfYear: NSCalendarUnit { get }     static var Nanosecond: NSCalendarUnit { get }     static var Calendar: NSCalendarUnit { get }     static var TimeZone: NSCalendarUnit { get }     static var NSEraCalendarUnit: NSCalendarUnit { get }     static var NSYearCalendarUnit: NSCalendarUnit { get }     static var NSMonthCalendarUnit: NSCalendarUnit { get }     static var NSDayCalendarUnit: NSCalendarUnit { get }     static var NSHourCalendarUnit: NSCalendarUnit { get }     static var NSMinuteCalendarUnit: NSCalendarUnit { get }     static var NSSecondCalendarUnit: NSCalendarUnit { get }     static var NSWeekCalendarUnit: NSCalendarUnit { get }     static var NSWeekdayCalendarUnit: NSCalendarUnit { get }     static var NSWeekdayOrdinalCalendarUnit: NSCalendarUnit { get }     static var NSQuarterCalendarUnit: NSCalendarUnit { get }     static var NSWeekOfMonthCalendarUnit: NSCalendarUnit { get }     static var NSWeekOfYearCalendarUnit: NSCalendarUnit { get }     static var NSYearForWeekOfYearCalendarUnit: NSCalendarUnit { get }     static var NSCalendarCalendarUnit: NSCalendarUnit { get }     static var NSTimeZoneCalendarUnit: NSCalendarUnit { get } } ``` | OptionSetType |

Modified [NSCalendarUnit.Calendar](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunitcalendar)

|  | Declaration |
| --- | --- |
| From | ``` static var CalendarUnitCalendar: NSCalendarUnit { get } ``` |
| To | ``` static var Calendar: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.Day](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunitday)

|  | Declaration |
| --- | --- |
| From | ``` static var CalendarUnitDay: NSCalendarUnit { get } ``` |
| To | ``` static var Day: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.Era](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunitera)

|  | Declaration |
| --- | --- |
| From | ``` static var CalendarUnitEra: NSCalendarUnit { get } ``` |
| To | ``` static var Era: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.Hour](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunithour)

|  | Declaration |
| --- | --- |
| From | ``` static var CalendarUnitHour: NSCalendarUnit { get } ``` |
| To | ``` static var Hour: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.Minute](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunitminute)

|  | Declaration |
| --- | --- |
| From | ``` static var CalendarUnitMinute: NSCalendarUnit { get } ``` |
| To | ``` static var Minute: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.Month](https://developer.apple.com/documentation/foundation/nscalendar/unit/1418371-month)

|  | Declaration |
| --- | --- |
| From | ``` static var CalendarUnitMonth: NSCalendarUnit { get } ``` |
| To | ``` static var Month: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.Nanosecond](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunitnanosecond)

|  | Declaration |
| --- | --- |
| From | ``` static var CalendarUnitNanosecond: NSCalendarUnit { get } ``` |
| To | ``` static var Nanosecond: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.NSCalendarCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarcalendarunit)

|  | Declaration |
| --- | --- |
| From | ``` static var CalendarCalendarUnit: NSCalendarUnit { get } ``` |
| To | ``` static var NSCalendarCalendarUnit: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.NSDayCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendar/unit/1409435-nsdaycalendarunit)

|  | Declaration |
| --- | --- |
| From | ``` static var DayCalendarUnit: NSCalendarUnit { get } ``` |
| To | ``` static var NSDayCalendarUnit: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.NSEraCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendar/unit/1409052-nseracalendarunit)

|  | Declaration |
| --- | --- |
| From | ``` static var EraCalendarUnit: NSCalendarUnit { get } ``` |
| To | ``` static var NSEraCalendarUnit: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.NSHourCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendar/unit/1411272-nshourcalendarunit)

|  | Declaration |
| --- | --- |
| From | ``` static var HourCalendarUnit: NSCalendarUnit { get } ``` |
| To | ``` static var NSHourCalendarUnit: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.NSMinuteCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendar/unit/1413292-nsminutecalendarunit)

|  | Declaration |
| --- | --- |
| From | ``` static var MinuteCalendarUnit: NSCalendarUnit { get } ``` |
| To | ``` static var NSMinuteCalendarUnit: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.NSMonthCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendarunit/nsmonthcalendarunit)

|  | Declaration |
| --- | --- |
| From | ``` static var MonthCalendarUnit: NSCalendarUnit { get } ``` |
| To | ``` static var NSMonthCalendarUnit: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.NSQuarterCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendarunit/nsquartercalendarunit)

|  | Declaration |
| --- | --- |
| From | ``` static var QuarterCalendarUnit: NSCalendarUnit { get } ``` |
| To | ``` static var NSQuarterCalendarUnit: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.NSSecondCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendar/unit/1416859-nssecondcalendarunit)

|  | Declaration |
| --- | --- |
| From | ``` static var SecondCalendarUnit: NSCalendarUnit { get } ``` |
| To | ``` static var NSSecondCalendarUnit: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.NSTimeZoneCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendar/unit/1415063-nstimezonecalendarunit)

|  | Declaration |
| --- | --- |
| From | ``` static var TimeZoneCalendarUnit: NSCalendarUnit { get } ``` |
| To | ``` static var NSTimeZoneCalendarUnit: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.NSWeekCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendarunit/nsweekcalendarunit)

|  | Declaration |
| --- | --- |
| From | ``` static var WeekCalendarUnit: NSCalendarUnit { get } ``` |
| To | ``` static var NSWeekCalendarUnit: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.NSWeekdayCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendarunit/nsweekdaycalendarunit)

|  | Declaration |
| --- | --- |
| From | ``` static var WeekdayCalendarUnit: NSCalendarUnit { get } ``` |
| To | ``` static var NSWeekdayCalendarUnit: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.NSWeekdayOrdinalCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendar/unit/1417765-nsweekdayordinalcalendarunit)

|  | Declaration |
| --- | --- |
| From | ``` static var WeekdayOrdinalCalendarUnit: NSCalendarUnit { get } ``` |
| To | ``` static var NSWeekdayOrdinalCalendarUnit: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.NSWeekOfMonthCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendar/unit/1411920-nsweekofmonthcalendarunit)

|  | Declaration |
| --- | --- |
| From | ``` static var WeekOfMonthCalendarUnit: NSCalendarUnit { get } ``` |
| To | ``` static var NSWeekOfMonthCalendarUnit: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.NSWeekOfYearCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendar/unit/1412633-nsweekofyearcalendarunit)

|  | Declaration |
| --- | --- |
| From | ``` static var WeekOfYearCalendarUnit: NSCalendarUnit { get } ``` |
| To | ``` static var NSWeekOfYearCalendarUnit: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.NSYearCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendarunit/nsyearcalendarunit)

|  | Declaration |
| --- | --- |
| From | ``` static var YearCalendarUnit: NSCalendarUnit { get } ``` |
| To | ``` static var NSYearCalendarUnit: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.NSYearForWeekOfYearCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendarunit/nsyearforweekofyearcalendarunit)

|  | Declaration |
| --- | --- |
| From | ``` static var YearForWeekOfYearCalendarUnit: NSCalendarUnit { get } ``` |
| To | ``` static var NSYearForWeekOfYearCalendarUnit: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.Quarter](https://developer.apple.com/documentation/foundation/nscalendar/unit/1408257-quarter)

|  | Declaration |
| --- | --- |
| From | ``` static var CalendarUnitQuarter: NSCalendarUnit { get } ``` |
| To | ``` static var Quarter: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.Second](https://developer.apple.com/documentation/foundation/nscalendar/unit/1409279-second)

|  | Declaration |
| --- | --- |
| From | ``` static var CalendarUnitSecond: NSCalendarUnit { get } ``` |
| To | ``` static var Second: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.TimeZone](https://developer.apple.com/documentation/foundation/nscalendar/unit/1413153-timezone)

|  | Declaration |
| --- | --- |
| From | ``` static var CalendarUnitTimeZone: NSCalendarUnit { get } ``` |
| To | ``` static var TimeZone: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.Weekday](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunitweekday)

|  | Declaration |
| --- | --- |
| From | ``` static var CalendarUnitWeekday: NSCalendarUnit { get } ``` |
| To | ``` static var Weekday: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.WeekdayOrdinal](https://developer.apple.com/documentation/foundation/nscalendar/unit/1414275-weekdayordinal)

|  | Declaration |
| --- | --- |
| From | ``` static var CalendarUnitWeekdayOrdinal: NSCalendarUnit { get } ``` |
| To | ``` static var WeekdayOrdinal: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.WeekOfMonth](https://developer.apple.com/documentation/foundation/nscalendar/unit/1412656-weekofmonth)

|  | Declaration |
| --- | --- |
| From | ``` static var CalendarUnitWeekOfMonth: NSCalendarUnit { get } ``` |
| To | ``` static var WeekOfMonth: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.WeekOfYear](https://developer.apple.com/documentation/foundation/nscalendar/unit/1411748-weekofyear)

|  | Declaration |
| --- | --- |
| From | ``` static var CalendarUnitWeekOfYear: NSCalendarUnit { get } ``` |
| To | ``` static var WeekOfYear: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.Year](https://developer.apple.com/documentation/foundation/nscalendar/unit/1416016-year)

|  | Declaration |
| --- | --- |
| From | ``` static var CalendarUnitYear: NSCalendarUnit { get } ``` |
| To | ``` static var Year: NSCalendarUnit { get } ``` |

Modified [NSCalendarUnit.YearForWeekOfYear](https://developer.apple.com/documentation/foundation/nscalendar/unit/1412761-yearforweekofyear)

|  | Declaration |
| --- | --- |
| From | ``` static var CalendarUnitYearForWeekOfYear: NSCalendarUnit { get } ``` |
| To | ``` static var YearForWeekOfYear: NSCalendarUnit { get } ``` |

Modified [NSCharacterSet](https://developer.apple.com/documentation/foundation/nscharacterset)

|  | Declaration |
| --- | --- |
| From | ``` class NSCharacterSet : NSObject, NSCopying, NSMutableCopying, NSCoding {     class func controlCharacterSet() -> NSCharacterSet     class func whitespaceCharacterSet() -> NSCharacterSet     class func whitespaceAndNewlineCharacterSet() -> NSCharacterSet     class func decimalDigitCharacterSet() -> NSCharacterSet     class func letterCharacterSet() -> NSCharacterSet     class func lowercaseLetterCharacterSet() -> NSCharacterSet     class func uppercaseLetterCharacterSet() -> NSCharacterSet     class func nonBaseCharacterSet() -> NSCharacterSet     class func alphanumericCharacterSet() -> NSCharacterSet     class func decomposableCharacterSet() -> NSCharacterSet     class func illegalCharacterSet() -> NSCharacterSet     class func punctuationCharacterSet() -> NSCharacterSet     class func capitalizedLetterCharacterSet() -> NSCharacterSet     class func symbolCharacterSet() -> NSCharacterSet     class func newlineCharacterSet() -> NSCharacterSet     init(range aRange: NSRange) -> NSCharacterSet     class func characterSetWithRange(_ aRange: NSRange) -> NSCharacterSet     init(charactersInString aString: String) -> NSCharacterSet     class func characterSetWithCharactersInString(_ aString: String) -> NSCharacterSet     init(bitmapRepresentation data: NSData) -> NSCharacterSet     class func characterSetWithBitmapRepresentation(_ data: NSData) -> NSCharacterSet     init?(contentsOfFile fName: String) -> NSCharacterSet     class func characterSetWithContentsOfFile(_ fName: String) -> NSCharacterSet?     init(coder aDecoder: NSCoder)     func characterIsMember(_ aCharacter: unichar) -> Bool     @NSCopying var bitmapRepresentation: NSData { get }     @NSCopying var invertedSet: NSCharacterSet { get }     func longCharacterIsMember(_ theLongChar: UTF32Char) -> Bool     func isSupersetOfSet(_ theOtherSet: NSCharacterSet) -> Bool     func hasMemberInPlane(_ thePlane: UInt8) -> Bool } extension NSCharacterSet {     class func URLUserAllowedCharacterSet() -> NSCharacterSet     class func URLPasswordAllowedCharacterSet() -> NSCharacterSet     class func URLHostAllowedCharacterSet() -> NSCharacterSet     class func URLPathAllowedCharacterSet() -> NSCharacterSet     class func URLQueryAllowedCharacterSet() -> NSCharacterSet     class func URLFragmentAllowedCharacterSet() -> NSCharacterSet } ``` |
| To | ``` class NSCharacterSet : NSObject, NSCopying, NSMutableCopying, NSCoding {     class func controlCharacterSet() -> NSCharacterSet     class func whitespaceCharacterSet() -> NSCharacterSet     class func whitespaceAndNewlineCharacterSet() -> NSCharacterSet     class func decimalDigitCharacterSet() -> NSCharacterSet     class func letterCharacterSet() -> NSCharacterSet     class func lowercaseLetterCharacterSet() -> NSCharacterSet     class func uppercaseLetterCharacterSet() -> NSCharacterSet     class func nonBaseCharacterSet() -> NSCharacterSet     class func alphanumericCharacterSet() -> NSCharacterSet     class func decomposableCharacterSet() -> NSCharacterSet     class func illegalCharacterSet() -> NSCharacterSet     class func punctuationCharacterSet() -> NSCharacterSet     class func capitalizedLetterCharacterSet() -> NSCharacterSet     class func symbolCharacterSet() -> NSCharacterSet     class func newlineCharacterSet() -> NSCharacterSet      init(range aRange: NSRange)     class func characterSetWithRange(_ aRange: NSRange) -> NSCharacterSet      init(charactersInString aString: String)     class func characterSetWithCharactersInString(_ aString: String) -> NSCharacterSet      init(bitmapRepresentation data: NSData)     class func characterSetWithBitmapRepresentation(_ data: NSData) -> NSCharacterSet      init?(contentsOfFile fName: String)     class func characterSetWithContentsOfFile(_ fName: String) -> NSCharacterSet?     init(coder aDecoder: NSCoder)     func characterIsMember(_ aCharacter: unichar) -> Bool     @NSCopying var bitmapRepresentation: NSData { get }     @NSCopying var invertedSet: NSCharacterSet { get }     func longCharacterIsMember(_ theLongChar: UTF32Char) -> Bool     func isSupersetOfSet(_ theOtherSet: NSCharacterSet) -> Bool     func hasMemberInPlane(_ thePlane: UInt8) -> Bool } extension NSCharacterSet {     class func URLUserAllowedCharacterSet() -> NSCharacterSet     class func URLPasswordAllowedCharacterSet() -> NSCharacterSet     class func URLHostAllowedCharacterSet() -> NSCharacterSet     class func URLPathAllowedCharacterSet() -> NSCharacterSet     class func URLQueryAllowedCharacterSet() -> NSCharacterSet     class func URLFragmentAllowedCharacterSet() -> NSCharacterSet } ``` |

Modified [NSCharacterSet.init(bitmapRepresentation: NSData)](https://developer.apple.com/documentation/foundation/nscharacterset/1415042-init)

|  | Declaration |
| --- | --- |
| From | ``` init(bitmapRepresentation data: NSData) -> NSCharacterSet ``` |
| To | ``` init(bitmapRepresentation data: NSData) ``` |

Modified [NSCharacterSet.init(charactersInString: String)](https://developer.apple.com/documentation/foundation/nscharacterset/1414061-init)

|  | Declaration |
| --- | --- |
| From | ``` init(charactersInString aString: String) -> NSCharacterSet ``` |
| To | ``` init(charactersInString aString: String) ``` |

Modified [NSCharacterSet.init(contentsOfFile: String)](https://developer.apple.com/documentation/foundation/nscharacterset/1418269-charactersetwithcontentsoffile)

|  | Declaration |
| --- | --- |
| From | ``` init?(contentsOfFile fName: String) -> NSCharacterSet ``` |
| To | ``` init?(contentsOfFile fName: String) ``` |

Modified [NSCharacterSet.init(range: NSRange)](https://developer.apple.com/documentation/foundation/nscharacterset/1414398-init)

|  | Declaration |
| --- | --- |
| From | ``` init(range aRange: NSRange) -> NSCharacterSet ``` |
| To | ``` init(range aRange: NSRange) ``` |

Modified [NSCoder](https://developer.apple.com/documentation/foundation/nscoder)

|  | Declaration |
| --- | --- |
| From | ``` class NSCoder : NSObject {     func encodeValueOfObjCType(_ type: UnsafePointer<Int8>, at addr: UnsafePointer<Void>)     func encodeDataObject(_ data: NSData)     func decodeValueOfObjCType(_ type: UnsafePointer<Int8>, at data: UnsafeMutablePointer<Void>)     func decodeDataObject() -> NSData?     func versionForClassName(_ className: String) -> Int } extension NSCoder {     func encodeCMTime(_ time: CMTime, forKey key: String!)     func decodeCMTimeForKey(_ key: String!) -> CMTime     func encodeCMTimeRange(_ timeRange: CMTimeRange, forKey key: String!)     func decodeCMTimeRangeForKey(_ key: String!) -> CMTimeRange     func encodeCMTimeMapping(_ timeMapping: CMTimeMapping, forKey key: String!)     func decodeCMTimeMappingForKey(_ key: String!) -> CMTimeMapping } extension NSCoder {     func encodeObject(_ object: AnyObject?)     func encodeRootObject(_ rootObject: AnyObject)     func encodeBycopyObject(_ anObject: AnyObject?)     func encodeByrefObject(_ anObject: AnyObject?)     func encodeConditionalObject(_ object: AnyObject?)     func encodeArrayOfObjCType(_ type: UnsafePointer<Int8>, count count: Int, at array: UnsafePointer<Void>)     func encodeBytes(_ byteaddr: UnsafePointer<Void>, length length: Int)     func decodeObject() -> AnyObject?     func decodeArrayOfObjCType(_ itemType: UnsafePointer<Int8>, count count: Int, at array: UnsafeMutablePointer<Void>)     func decodeBytesWithReturnedLength(_ lengthp: UnsafeMutablePointer<Int>) -> UnsafeMutablePointer<Void>     func setObjectZone(_ zone: NSZone)     func objectZone() -> NSZone     var systemVersion: UInt32 { get }     var allowsKeyedCoding: Bool { get }     func encodeObject(_ objv: AnyObject?, forKey key: String)     func encodeConditionalObject(_ objv: AnyObject?, forKey key: String)     func encodeBool(_ boolv: Bool, forKey key: String)     func encodeInt(_ intv: Int32, forKey key: String)     func encodeInt32(_ intv: Int32, forKey key: String)     func encodeInt64(_ intv: Int64, forKey key: String)     func encodeFloat(_ realv: Float, forKey key: String)     func encodeDouble(_ realv: Double, forKey key: String)     func encodeBytes(_ bytesp: UnsafePointer<UInt8>, length lenv: Int, forKey key: String)     func containsValueForKey(_ key: String) -> Bool     func decodeObjectForKey(_ key: String) -> AnyObject?     func decodeBoolForKey(_ key: String) -> Bool     func decodeIntForKey(_ key: String) -> Int32     func decodeInt32ForKey(_ key: String) -> Int32     func decodeInt64ForKey(_ key: String) -> Int64     func decodeFloatForKey(_ key: String) -> Float     func decodeDoubleForKey(_ key: String) -> Double     func decodeBytesForKey(_ key: String, returnedLength lengthp: UnsafeMutablePointer<Int>) -> UnsafePointer<UInt8>     func encodeInteger(_ intv: Int, forKey key: String)     func decodeIntegerForKey(_ key: String) -> Int     var requiresSecureCoding: Bool { get }     func decodeObjectOfClass(_ aClass: AnyClass, forKey key: String) -> AnyObject?     func decodeObjectOfClasses(_ classes: Set<NSObject>, forKey key: String) -> AnyObject?     func decodePropertyListForKey(_ key: String) -> AnyObject?     var allowedClasses: Set<NSObject>? { get } } extension NSCoder {     func encodeCGPoint(_ point: CGPoint, forKey key: String!)     func encodeCGVector(_ vector: CGVector, forKey key: String!)     func encodeCGSize(_ size: CGSize, forKey key: String!)     func encodeCGRect(_ rect: CGRect, forKey key: String!)     func encodeCGAffineTransform(_ transform: CGAffineTransform, forKey key: String!)     func encodeUIEdgeInsets(_ insets: UIEdgeInsets, forKey key: String!)     func encodeUIOffset(_ offset: UIOffset, forKey key: String!)     func decodeCGPointForKey(_ key: String!) -> CGPoint     func decodeCGVectorForKey(_ key: String!) -> CGVector     func decodeCGSizeForKey(_ key: String!) -> CGSize     func decodeCGRectForKey(_ key: String!) -> CGRect     func decodeCGAffineTransformForKey(_ key: String!) -> CGAffineTransform     func decodeUIEdgeInsetsForKey(_ key: String!) -> UIEdgeInsets     func decodeUIOffsetForKey(_ key: String!) -> UIOffset } ``` |
| To | ``` class NSCoder : NSObject {     func encodeValueOfObjCType(_ type: UnsafePointer<Int8>, at addr: UnsafePointer<Void>)     func encodeDataObject(_ data: NSData)     func decodeValueOfObjCType(_ type: UnsafePointer<Int8>, at data: UnsafeMutablePointer<Void>)     func decodeDataObject() -> NSData?     func versionForClassName(_ className: String) -> Int } extension NSCoder {     func encodeCMTime(_ time: CMTime, forKey key: String)     func decodeCMTimeForKey(_ key: String) -> CMTime     func encodeCMTimeRange(_ timeRange: CMTimeRange, forKey key: String)     func decodeCMTimeRangeForKey(_ key: String) -> CMTimeRange     func encodeCMTimeMapping(_ timeMapping: CMTimeMapping, forKey key: String)     func decodeCMTimeMappingForKey(_ key: String) -> CMTimeMapping } extension NSCoder {     @warn_unused_result     func decodeObjectOfClass<DecodedObjectType : NSCoding where DecodedObjectType : NSObject>(_ cls: DecodedObjectType.Type, forKey key: String) -> DecodedObjectType?     @warn_unused_result     @nonobjc func decodeObjectOfClasses(_ classes: NSSet?, forKey key: String) -> AnyObject?     @warn_unused_result     func decodeTopLevelObject() throws -> AnyObject?     @warn_unused_result     func decodeTopLevelObjectForKey(_ key: String) throws -> AnyObject?     @warn_unused_result     func decodeTopLevelObjectOfClass<DecodedObjectType : NSCoding where DecodedObjectType : NSObject>(_ cls: DecodedObjectType.Type, forKey key: String) throws -> DecodedObjectType?     @warn_unused_result     func decodeTopLevelObjectOfClasses(_ classes: NSSet?, forKey key: String) throws -> AnyObject? } extension NSCoder {     func encodeObject(_ object: AnyObject?)     func encodeRootObject(_ rootObject: AnyObject)     func encodeBycopyObject(_ anObject: AnyObject?)     func encodeByrefObject(_ anObject: AnyObject?)     func encodeConditionalObject(_ object: AnyObject?)     func encodeArrayOfObjCType(_ type: UnsafePointer<Int8>, count count: Int, at array: UnsafePointer<Void>)     func encodeBytes(_ byteaddr: UnsafePointer<Void>, length length: Int)     func decodeObject() -> AnyObject?     func decodeTopLevelObject() throws -> AnyObject     func decodeArrayOfObjCType(_ itemType: UnsafePointer<Int8>, count count: Int, at array: UnsafeMutablePointer<Void>)     func decodeBytesWithReturnedLength(_ lengthp: UnsafeMutablePointer<Int>) -> UnsafeMutablePointer<Void>     func setObjectZone(_ zone: NSZone)     func objectZone() -> NSZone     var systemVersion: UInt32 { get }     var allowsKeyedCoding: Bool { get }     func encodeObject(_ objv: AnyObject?, forKey key: String)     func encodeConditionalObject(_ objv: AnyObject?, forKey key: String)     func encodeBool(_ boolv: Bool, forKey key: String)     func encodeInt(_ intv: Int32, forKey key: String)     func encodeInt32(_ intv: Int32, forKey key: String)     func encodeInt64(_ intv: Int64, forKey key: String)     func encodeFloat(_ realv: Float, forKey key: String)     func encodeDouble(_ realv: Double, forKey key: String)     func encodeBytes(_ bytesp: UnsafePointer<UInt8>, length lenv: Int, forKey key: String)     func containsValueForKey(_ key: String) -> Bool     func decodeObjectForKey(_ key: String) -> AnyObject?     func decodeTopLevelObjectForKey(_ key: String) throws -> AnyObject     func decodeBoolForKey(_ key: String) -> Bool     func decodeIntForKey(_ key: String) -> Int32     func decodeInt32ForKey(_ key: String) -> Int32     func decodeInt64ForKey(_ key: String) -> Int64     func decodeFloatForKey(_ key: String) -> Float     func decodeDoubleForKey(_ key: String) -> Double     func decodeBytesForKey(_ key: String, returnedLength lengthp: UnsafeMutablePointer<Int>) -> UnsafePointer<UInt8>     func encodeInteger(_ intv: Int, forKey key: String)     func decodeIntegerForKey(_ key: String) -> Int     var requiresSecureCoding: Bool { get }     func decodeObjectOfClass(_ aClass: AnyClass, forKey key: String) -> AnyObject?     func decodeTopLevelObjectOfClass(_ aClass: AnyClass, forKey key: String) throws -> AnyObject     func __decodeObjectOfClasses(_ classes: Set<NSObject>?, forKey key: String) -> AnyObject?     func decodeTopLevelObjectOfClasses(_ classes: Set<NSObject>?, forKey key: String) throws -> AnyObject     func decodePropertyListForKey(_ key: String) -> AnyObject?     var allowedClasses: Set<NSObject>? { get }     func failWithError(_ error: NSError) } extension NSCoder {     @warn_unused_result     func decodeObjectOfClass<DecodedObjectType : NSCoding where DecodedObjectType : NSObject>(_ cls: DecodedObjectType.Type, forKey key: String) -> DecodedObjectType?     @warn_unused_result     @nonobjc func decodeObjectOfClasses(_ classes: NSSet?, forKey key: String) -> AnyObject?     @warn_unused_result     func decodeTopLevelObject() throws -> AnyObject?     @warn_unused_result     func decodeTopLevelObjectForKey(_ key: String) throws -> AnyObject?     @warn_unused_result     func decodeTopLevelObjectOfClass<DecodedObjectType : NSCoding where DecodedObjectType : NSObject>(_ cls: DecodedObjectType.Type, forKey key: String) throws -> DecodedObjectType?     @warn_unused_result     func decodeTopLevelObjectOfClasses(_ classes: NSSet?, forKey key: String) throws -> AnyObject? } extension NSCoder {     func encodeCGPoint(_ point: CGPoint, forKey key: String)     func encodeCGVector(_ vector: CGVector, forKey key: String)     func encodeCGSize(_ size: CGSize, forKey key: String)     func encodeCGRect(_ rect: CGRect, forKey key: String)     func encodeCGAffineTransform(_ transform: CGAffineTransform, forKey key: String)     func encodeUIEdgeInsets(_ insets: UIEdgeInsets, forKey key: String)     func encodeUIOffset(_ offset: UIOffset, forKey key: String)     func decodeCGPointForKey(_ key: String) -> CGPoint     func decodeCGVectorForKey(_ key: String) -> CGVector     func decodeCGSizeForKey(_ key: String) -> CGSize     func decodeCGRectForKey(_ key: String) -> CGRect     func decodeCGAffineTransformForKey(_ key: String) -> CGAffineTransform     func decodeUIEdgeInsetsForKey(_ key: String) -> UIEdgeInsets     func decodeUIOffsetForKey(_ key: String) -> UIOffset } ``` |

Modified [NSCoding](https://developer.apple.com/documentation/foundation/nscoding)

|  | Declaration |
| --- | --- |
| From | ``` protocol NSCoding {     func encodeWithCoder(_ aCoder: NSCoder)     init(coder aDecoder: NSCoder) } ``` |
| To | ``` protocol NSCoding {     func encodeWithCoder(_ aCoder: NSCoder)     init?(coder aDecoder: NSCoder) } ``` |

Modified [NSCoding.init(coder: NSCoder)](https://developer.apple.com/documentation/foundation/nscoding/1416145-init)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified [NSComparisonPredicate](https://developer.apple.com/documentation/foundation/nscomparisonpredicate)

|  | Declaration |
| --- | --- |
| From | ``` class NSComparisonPredicate : NSPredicate {     init(leftExpression lhs: NSExpression, rightExpression rhs: NSExpression, modifier modifier: NSComparisonPredicateModifier, type type: NSPredicateOperatorType, options options: NSComparisonPredicateOptions) -> NSComparisonPredicate     class func predicateWithLeftExpression(_ lhs: NSExpression, rightExpression rhs: NSExpression, modifier modifier: NSComparisonPredicateModifier, type type: NSPredicateOperatorType, options options: NSComparisonPredicateOptions) -> NSComparisonPredicate     init(leftExpression lhs: NSExpression, rightExpression rhs: NSExpression, customSelector selector: Selector) -> NSComparisonPredicate     class func predicateWithLeftExpression(_ lhs: NSExpression, rightExpression rhs: NSExpression, customSelector selector: Selector) -> NSComparisonPredicate     init(leftExpression lhs: NSExpression, rightExpression rhs: NSExpression, modifier modifier: NSComparisonPredicateModifier, type type: NSPredicateOperatorType, options options: NSComparisonPredicateOptions)     init(leftExpression lhs: NSExpression, rightExpression rhs: NSExpression, customSelector selector: Selector)     var predicateOperatorType: NSPredicateOperatorType { get }     var comparisonPredicateModifier: NSComparisonPredicateModifier { get }     var leftExpression: NSExpression { get }     var rightExpression: NSExpression { get }     var customSelector: Selector { get }     var options: NSComparisonPredicateOptions { get } } ``` |
| To | ``` class NSComparisonPredicate : NSPredicate {      init(leftExpression lhs: NSExpression, rightExpression rhs: NSExpression, modifier modifier: NSComparisonPredicateModifier, type type: NSPredicateOperatorType, options options: NSComparisonPredicateOptions)     class func predicateWithLeftExpression(_ lhs: NSExpression, rightExpression rhs: NSExpression, modifier modifier: NSComparisonPredicateModifier, type type: NSPredicateOperatorType, options options: NSComparisonPredicateOptions) -> NSComparisonPredicate      init(leftExpression lhs: NSExpression, rightExpression rhs: NSExpression, customSelector selector: Selector)     class func predicateWithLeftExpression(_ lhs: NSExpression, rightExpression rhs: NSExpression, customSelector selector: Selector) -> NSComparisonPredicate     init(leftExpression lhs: NSExpression, rightExpression rhs: NSExpression, modifier modifier: NSComparisonPredicateModifier, type type: NSPredicateOperatorType, options options: NSComparisonPredicateOptions)     init(leftExpression lhs: NSExpression, rightExpression rhs: NSExpression, customSelector selector: Selector)     init?(coder coder: NSCoder)     var predicateOperatorType: NSPredicateOperatorType { get }     var comparisonPredicateModifier: NSComparisonPredicateModifier { get }     var leftExpression: NSExpression { get }     var rightExpression: NSExpression { get }     var customSelector: Selector { get }     var options: NSComparisonPredicateOptions { get } } ``` |

Modified [NSComparisonPredicateModifier [enum]](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/modifier)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSComparisonPredicateOptions [struct]](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/options)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSComparisonPredicateOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var CaseInsensitivePredicateOption: NSComparisonPredicateOptions { get }     static var DiacriticInsensitivePredicateOption: NSComparisonPredicateOptions { get }     static var NormalizedPredicateOption: NSComparisonPredicateOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSComparisonPredicateOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var CaseInsensitivePredicateOption: NSComparisonPredicateOptions { get }     static var DiacriticInsensitivePredicateOption: NSComparisonPredicateOptions { get }     static var NormalizedPredicateOption: NSComparisonPredicateOptions { get } } ``` | OptionSetType |

Modified [NSComparisonResult [enum]](https://developer.apple.com/documentation/foundation/nscomparisonresult)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NSCompoundPredicate](https://developer.apple.com/documentation/foundation/nscompoundpredicate)

|  | Declaration |
| --- | --- |
| From | ``` class NSCompoundPredicate : NSPredicate {     init(type type: NSCompoundPredicateType, subpredicates subpredicates: [AnyObject]!)     var compoundPredicateType: NSCompoundPredicateType { get }     var subpredicates: [AnyObject] { get }     class func andPredicateWithSubpredicates(_ subpredicates: [AnyObject]) -> NSCompoundPredicate     class func orPredicateWithSubpredicates(_ subpredicates: [AnyObject]) -> NSCompoundPredicate     class func notPredicateWithSubpredicate(_ predicate: NSPredicate) -> NSCompoundPredicate } ``` |
| To | ``` class NSCompoundPredicate : NSPredicate {     init(type type: NSCompoundPredicateType, subpredicates subpredicates: [NSPredicate])     init?(coder coder: NSCoder)     var compoundPredicateType: NSCompoundPredicateType { get }     var subpredicates: [AnyObject] { get }      init(andPredicateWithSubpredicates subpredicates: [NSPredicate])     class func andPredicateWithSubpredicates(_ subpredicates: [NSPredicate]) -> NSCompoundPredicate      init(orPredicateWithSubpredicates subpredicates: [NSPredicate])     class func orPredicateWithSubpredicates(_ subpredicates: [NSPredicate]) -> NSCompoundPredicate      init(notPredicateWithSubpredicate predicate: NSPredicate)     class func notPredicateWithSubpredicate(_ predicate: NSPredicate) -> NSCompoundPredicate } ``` |

Modified [NSCompoundPredicate.init(andPredicateWithSubpredicates: [NSPredicate])](https://developer.apple.com/documentation/foundation/nscompoundpredicate/1407855-init)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | andPredicateWithSubpredicates(_:) | ``` class func andPredicateWithSubpredicates(_ subpredicates: [AnyObject]) -> NSCompoundPredicate ``` | iOS 8.0 |
| To | init(andPredicateWithSubpredicates:) | ``` init(andPredicateWithSubpredicates subpredicates: [NSPredicate]) ``` | iOS 9.0 |

Modified [NSCompoundPredicate.init(notPredicateWithSubpredicate: NSPredicate)](https://developer.apple.com/documentation/foundation/nscompoundpredicate/1409462-notpredicatewithsubpredicate)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | notPredicateWithSubpredicate(_:) | ``` class func notPredicateWithSubpredicate(_ predicate: NSPredicate) -> NSCompoundPredicate ``` | iOS 8.0 |
| To | init(notPredicateWithSubpredicate:) | ``` init(notPredicateWithSubpredicate predicate: NSPredicate) ``` | iOS 9.0 |

Modified [NSCompoundPredicate.init(orPredicateWithSubpredicates: [NSPredicate])](https://developer.apple.com/documentation/foundation/nscompoundpredicate/1417873-orpredicatewithsubpredicates)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | orPredicateWithSubpredicates(_:) | ``` class func orPredicateWithSubpredicates(_ subpredicates: [AnyObject]) -> NSCompoundPredicate ``` | iOS 8.0 |
| To | init(orPredicateWithSubpredicates:) | ``` init(orPredicateWithSubpredicates subpredicates: [NSPredicate]) ``` | iOS 9.0 |

Modified [NSCompoundPredicate.init(type: NSCompoundPredicateType, subpredicates: [NSPredicate])](https://developer.apple.com/documentation/foundation/nscompoundpredicate/1407744-init)

|  | Declaration |
| --- | --- |
| From | ``` init(type type: NSCompoundPredicateType, subpredicates subpredicates: [AnyObject]!) ``` |
| To | ``` init(type type: NSCompoundPredicateType, subpredicates subpredicates: [NSPredicate]) ``` |

Modified [NSCompoundPredicateType [enum]](https://developer.apple.com/documentation/foundation/nscompoundpredicate/logicaltype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSData](https://developer.apple.com/documentation/foundation/nsdata)

|  | Declaration |
| --- | --- |
| From | ``` class NSData : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     var length: Int { get }     var bytes: UnsafePointer<Void> { get } } extension NSData : CKRecordValue, NSObjectProtocol { } extension NSData {     var description: String { get }     func getBytes(_ buffer: UnsafeMutablePointer<Void>, length length: Int)     func getBytes(_ buffer: UnsafeMutablePointer<Void>, range range: NSRange)     func isEqualToData(_ other: NSData) -> Bool     func subdataWithRange(_ range: NSRange) -> NSData     func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool) -> Bool     func writeToURL(_ url: NSURL, atomically atomically: Bool) -> Bool     func writeToFile(_ path: String, options writeOptionsMask: NSDataWritingOptions, error errorPtr: NSErrorPointer) -> Bool     func writeToURL(_ url: NSURL, options writeOptionsMask: NSDataWritingOptions, error errorPtr: NSErrorPointer) -> Bool     func rangeOfData(_ dataToFind: NSData, options mask: NSDataSearchOptions, range searchRange: NSRange) -> NSRange     func enumerateByteRangesUsingBlock(_ block: (UnsafePointer<Void>, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) } extension NSData {     convenience init!()     class func data() -> Self!     convenience init!(bytes bytes: UnsafePointer<Void>, length length: Int)     class func dataWithBytes(_ bytes: UnsafePointer<Void>, length length: Int) -> Self!     convenience init!(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length length: Int)     class func dataWithBytesNoCopy(_ bytes: UnsafeMutablePointer<Void>, length length: Int) -> Self!     convenience init!(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length length: Int, freeWhenDone b: Bool)     class func dataWithBytesNoCopy(_ bytes: UnsafeMutablePointer<Void>, length length: Int, freeWhenDone b: Bool) -> Self!     convenience init?(contentsOfFile path: String, options readOptionsMask: NSDataReadingOptions, error errorPtr: NSErrorPointer)     class func dataWithContentsOfFile(_ path: String, options readOptionsMask: NSDataReadingOptions, error errorPtr: NSErrorPointer) -> Self?     convenience init?(contentsOfURL url: NSURL, options readOptionsMask: NSDataReadingOptions, error errorPtr: NSErrorPointer)     class func dataWithContentsOfURL(_ url: NSURL, options readOptionsMask: NSDataReadingOptions, error errorPtr: NSErrorPointer) -> Self?     convenience init?(contentsOfFile path: String)     class func dataWithContentsOfFile(_ path: String) -> Self?     convenience init?(contentsOfURL url: NSURL)     class func dataWithContentsOfURL(_ url: NSURL) -> Self?     init(bytes bytes: UnsafePointer<Void>, length length: Int)     init(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length length: Int)     init(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length length: Int, freeWhenDone b: Bool)     init(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length length: Int, deallocator deallocator: ((UnsafeMutablePointer<Void>, Int) -> Void)?)     init?(contentsOfFile path: String, options readOptionsMask: NSDataReadingOptions, error errorPtr: NSErrorPointer)     init?(contentsOfURL url: NSURL, options readOptionsMask: NSDataReadingOptions, error errorPtr: NSErrorPointer)     init?(contentsOfFile path: String)     init?(contentsOfURL url: NSURL)     init(data data: NSData)     class func dataWithData(_ data: NSData) -> Self } extension NSData {     init?(base64EncodedString base64String: String, options options: NSDataBase64DecodingOptions)     func base64EncodedStringWithOptions(_ options: NSDataBase64EncodingOptions) -> String     init?(base64EncodedData base64Data: NSData, options options: NSDataBase64DecodingOptions)     func base64EncodedDataWithOptions(_ options: NSDataBase64EncodingOptions) -> NSData } extension NSData {     func getBytes(_ buffer: UnsafeMutablePointer<Void>)     class func dataWithContentsOfMappedFile(_ path: String) -> AnyObject?     init?(contentsOfMappedFile path: String)     init!(base64Encoding base64String: String!)     func base64Encoding() -> String! } ``` |
| To | ``` class NSData : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     var length: Int { get }     var bytes: UnsafePointer<Void> { get } } extension NSData : CKRecordValue { } extension NSData {     var description: String { get }     func getBytes(_ buffer: UnsafeMutablePointer<Void>, length length: Int)     func getBytes(_ buffer: UnsafeMutablePointer<Void>, range range: NSRange)     func isEqualToData(_ other: NSData) -> Bool     func subdataWithRange(_ range: NSRange) -> NSData     func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool) -> Bool     func writeToURL(_ url: NSURL, atomically atomically: Bool) -> Bool     func writeToFile(_ path: String, options writeOptionsMask: NSDataWritingOptions) throws     func writeToURL(_ url: NSURL, options writeOptionsMask: NSDataWritingOptions) throws     func rangeOfData(_ dataToFind: NSData, options mask: NSDataSearchOptions, range searchRange: NSRange) -> NSRange     func enumerateByteRangesUsingBlock(_ block: (UnsafePointer<Void>, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) } extension NSData {     convenience init()     class func data() -> Self     convenience init(bytes bytes: UnsafePointer<Void>, length length: Int)     class func dataWithBytes(_ bytes: UnsafePointer<Void>, length length: Int) -> Self     convenience init(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length length: Int)     class func dataWithBytesNoCopy(_ bytes: UnsafeMutablePointer<Void>, length length: Int) -> Self     convenience init(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length length: Int, freeWhenDone b: Bool)     class func dataWithBytesNoCopy(_ bytes: UnsafeMutablePointer<Void>, length length: Int, freeWhenDone b: Bool) -> Self     convenience init(contentsOfFile path: String, options readOptionsMask: NSDataReadingOptions) throws     class func dataWithContentsOfFile(_ path: String, options readOptionsMask: NSDataReadingOptions) throws -> Self     convenience init(contentsOfURL url: NSURL, options readOptionsMask: NSDataReadingOptions) throws     class func dataWithContentsOfURL(_ url: NSURL, options readOptionsMask: NSDataReadingOptions) throws -> Self     convenience init?(contentsOfFile path: String)     class func dataWithContentsOfFile(_ path: String) -> Self?     convenience init?(contentsOfURL url: NSURL)     class func dataWithContentsOfURL(_ url: NSURL) -> Self?     init(bytes bytes: UnsafePointer<Void>, length length: Int)     init(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length length: Int)     init(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length length: Int, freeWhenDone b: Bool)     init(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length length: Int, deallocator deallocator: ((UnsafeMutablePointer<Void>, Int) -> Void)?)     init(contentsOfFile path: String, options readOptionsMask: NSDataReadingOptions) throws     init(contentsOfURL url: NSURL, options readOptionsMask: NSDataReadingOptions) throws     init?(contentsOfFile path: String)     init?(contentsOfURL url: NSURL)     init(data data: NSData)     class func dataWithData(_ data: NSData) -> Self } extension NSData {     init?(base64EncodedString base64String: String, options options: NSDataBase64DecodingOptions)     func base64EncodedStringWithOptions(_ options: NSDataBase64EncodingOptions) -> String     init?(base64EncodedData base64Data: NSData, options options: NSDataBase64DecodingOptions)     func base64EncodedDataWithOptions(_ options: NSDataBase64EncodingOptions) -> NSData } extension NSData {     func getBytes(_ buffer: UnsafeMutablePointer<Void>)     class func dataWithContentsOfMappedFile(_ path: String) -> AnyObject?     init?(contentsOfMappedFile path: String)     init?(base64Encoding base64String: String)     func base64Encoding() -> String } ``` |

Modified [NSData.init(contentsOfFile: String, options: NSDataReadingOptions) throws](https://developer.apple.com/documentation/foundation/nsdata/1411145-init)

|  | Declaration |
| --- | --- |
| From | ``` init?(contentsOfFile path: String, options readOptionsMask: NSDataReadingOptions, error errorPtr: NSErrorPointer) ``` |
| To | ``` init(contentsOfFile path: String, options readOptionsMask: NSDataReadingOptions) throws ``` |

Modified [NSData.init(contentsOfURL: NSURL, options: NSDataReadingOptions) throws](https://developer.apple.com/documentation/foundation/nsdata/1407864-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` init?(contentsOfURL url: NSURL, options readOptionsMask: NSDataReadingOptions, error errorPtr: NSErrorPointer) ``` |
| To | ``` init(contentsOfURL url: NSURL, options readOptionsMask: NSDataReadingOptions) throws ``` |

Modified [NSData.writeToFile(_: String, options: NSDataWritingOptions) throws](https://developer.apple.com/documentation/foundation/nsdata/1414800-write)

|  | Declaration |
| --- | --- |
| From | ``` func writeToFile(_ path: String, options writeOptionsMask: NSDataWritingOptions, error errorPtr: NSErrorPointer) -> Bool ``` |
| To | ``` func writeToFile(_ path: String, options writeOptionsMask: NSDataWritingOptions) throws ``` |

Modified [NSData.writeToURL(_: NSURL, options: NSDataWritingOptions) throws](https://developer.apple.com/documentation/foundation/nsdata/1410595-writetourl)

|  | Declaration |
| --- | --- |
| From | ``` func writeToURL(_ url: NSURL, options writeOptionsMask: NSDataWritingOptions, error errorPtr: NSErrorPointer) -> Bool ``` |
| To | ``` func writeToURL(_ url: NSURL, options writeOptionsMask: NSDataWritingOptions) throws ``` |

Modified [NSDataBase64DecodingOptions [struct]](https://developer.apple.com/documentation/foundation/nsdatabase64decodingoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSDataBase64DecodingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var IgnoreUnknownCharacters: NSDataBase64DecodingOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSDataBase64DecodingOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var IgnoreUnknownCharacters: NSDataBase64DecodingOptions { get } } ``` | OptionSetType |

Modified [NSDataBase64EncodingOptions [struct]](https://developer.apple.com/documentation/foundation/nsdata/base64encodingoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSDataBase64EncodingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Encoding64CharacterLineLength: NSDataBase64EncodingOptions { get }     static var Encoding76CharacterLineLength: NSDataBase64EncodingOptions { get }     static var EncodingEndLineWithCarriageReturn: NSDataBase64EncodingOptions { get }     static var EncodingEndLineWithLineFeed: NSDataBase64EncodingOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSDataBase64EncodingOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var Encoding64CharacterLineLength: NSDataBase64EncodingOptions { get }     static var Encoding76CharacterLineLength: NSDataBase64EncodingOptions { get }     static var EncodingEndLineWithCarriageReturn: NSDataBase64EncodingOptions { get }     static var EncodingEndLineWithLineFeed: NSDataBase64EncodingOptions { get } } ``` | OptionSetType |

Modified [NSDataDetector](https://developer.apple.com/documentation/foundation/nsdatadetector)

|  | Declaration |
| --- | --- |
| From | ``` class NSDataDetector : NSRegularExpression {     init?(types checkingTypes: NSTextCheckingTypes, error error: NSErrorPointer) -> NSDataDetector     class func dataDetectorWithTypes(_ checkingTypes: NSTextCheckingTypes, error error: NSErrorPointer) -> NSDataDetector?     init?(types checkingTypes: NSTextCheckingTypes, error error: NSErrorPointer)     var checkingTypes: NSTextCheckingTypes { get } } ``` |
| To | ``` class NSDataDetector : NSRegularExpression {      init(types checkingTypes: NSTextCheckingTypes) throws     class func dataDetectorWithTypes(_ checkingTypes: NSTextCheckingTypes) throws -> NSDataDetector     init(types checkingTypes: NSTextCheckingTypes) throws     var checkingTypes: NSTextCheckingTypes { get } } ``` |

Modified [NSDataDetector.init(types: NSTextCheckingTypes) throws](https://developer.apple.com/documentation/foundation/nsdatadetector/1409829-initwithtypes)

|  | Declaration |
| --- | --- |
| From | ``` init?(types checkingTypes: NSTextCheckingTypes, error error: NSErrorPointer) ``` |
| To | ``` init(types checkingTypes: NSTextCheckingTypes) throws ``` |

Modified [NSDataReadingOptions [struct]](https://developer.apple.com/documentation/foundation/nsdatareadingoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSDataReadingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var DataReadingMappedIfSafe: NSDataReadingOptions { get }     static var DataReadingUncached: NSDataReadingOptions { get }     static var DataReadingMappedAlways: NSDataReadingOptions { get }     static var DataReadingMapped: NSDataReadingOptions { get }     static var MappedRead: NSDataReadingOptions { get }     static var UncachedRead: NSDataReadingOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSDataReadingOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var DataReadingMappedIfSafe: NSDataReadingOptions { get }     static var DataReadingUncached: NSDataReadingOptions { get }     static var DataReadingMappedAlways: NSDataReadingOptions { get }     static var DataReadingMapped: NSDataReadingOptions { get }     static var MappedRead: NSDataReadingOptions { get }     static var UncachedRead: NSDataReadingOptions { get } } ``` | OptionSetType |

Modified [NSDataSearchOptions [struct]](https://developer.apple.com/documentation/foundation/nsdata/searchoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSDataSearchOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Backwards: NSDataSearchOptions { get }     static var Anchored: NSDataSearchOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSDataSearchOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var Backwards: NSDataSearchOptions { get }     static var Anchored: NSDataSearchOptions { get } } ``` | OptionSetType |

Modified [NSDataWritingOptions [struct]](https://developer.apple.com/documentation/foundation/nsdatawritingoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSDataWritingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var DataWritingAtomic: NSDataWritingOptions { get }     static var DataWritingWithoutOverwriting: NSDataWritingOptions { get }     static var DataWritingFileProtectionNone: NSDataWritingOptions { get }     static var DataWritingFileProtectionComplete: NSDataWritingOptions { get }     static var DataWritingFileProtectionCompleteUnlessOpen: NSDataWritingOptions { get }     static var DataWritingFileProtectionCompleteUntilFirstUserAuthentication: NSDataWritingOptions { get }     static var DataWritingFileProtectionMask: NSDataWritingOptions { get }     static var AtomicWrite: NSDataWritingOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSDataWritingOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var DataWritingAtomic: NSDataWritingOptions { get }     static var DataWritingWithoutOverwriting: NSDataWritingOptions { get }     static var DataWritingFileProtectionNone: NSDataWritingOptions { get }     static var DataWritingFileProtectionComplete: NSDataWritingOptions { get }     static var DataWritingFileProtectionCompleteUnlessOpen: NSDataWritingOptions { get }     static var DataWritingFileProtectionCompleteUntilFirstUserAuthentication: NSDataWritingOptions { get }     static var DataWritingFileProtectionMask: NSDataWritingOptions { get }     static var AtomicWrite: NSDataWritingOptions { get } } ``` | OptionSetType |

Modified [NSDate](https://developer.apple.com/documentation/foundation/nsdate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSDate : NSObject, NSCopying, NSSecureCoding, NSCoding {     var timeIntervalSinceReferenceDate: NSTimeInterval { get }     init()     init(timeIntervalSinceReferenceDate ti: NSTimeInterval)     init(coder aDecoder: NSCoder) } extension NSDate : CKRecordValue, NSObjectProtocol { } extension NSDate : Reflectable {     func getMirror() -> MirrorType } extension NSDate {     func timeIntervalSinceDate(_ anotherDate: NSDate) -> NSTimeInterval     var timeIntervalSinceNow: NSTimeInterval { get }     var timeIntervalSince1970: NSTimeInterval { get }     func addTimeInterval(_ seconds: NSTimeInterval) -> AnyObject!     func dateByAddingTimeInterval(_ ti: NSTimeInterval) -> Self     func earlierDate(_ anotherDate: NSDate) -> NSDate     func laterDate(_ anotherDate: NSDate) -> NSDate     func compare(_ other: NSDate) -> NSComparisonResult     func isEqualToDate(_ otherDate: NSDate) -> Bool     var description: String { get }     func descriptionWithLocale(_ locale: AnyObject?) -> String?     class func timeIntervalSinceReferenceDate() -> NSTimeInterval } extension NSDate {     convenience init()     class func date() -> Self     convenience init!(timeIntervalSinceNow secs: NSTimeInterval)     class func dateWithTimeIntervalSinceNow(_ secs: NSTimeInterval) -> Self!     convenience init(timeIntervalSinceReferenceDate ti: NSTimeInterval)     class func dateWithTimeIntervalSinceReferenceDate(_ ti: NSTimeInterval) -> Self     convenience init!(timeIntervalSince1970 secs: NSTimeInterval)     class func dateWithTimeIntervalSince1970(_ secs: NSTimeInterval) -> Self!     convenience init(timeInterval secsToBeAdded: NSTimeInterval, sinceDate date: NSDate)     class func dateWithTimeInterval(_ secsToBeAdded: NSTimeInterval, sinceDate date: NSDate) -> Self     class func distantFuture() -> AnyObject     class func distantPast() -> AnyObject     convenience init(timeIntervalSinceNow secs: NSTimeInterval)     convenience init(timeIntervalSince1970 secs: NSTimeInterval)     convenience init(timeInterval secsToBeAdded: NSTimeInterval, sinceDate date: NSDate) } extension NSDate : Reflectable {     func getMirror() -> MirrorType } ``` | AnyObject, CKRecordValue, NSCoding, NSCopying, NSObjectProtocol, NSSecureCoding, Reflectable |
| To | ``` class NSDate : NSObject, NSCopying, NSSecureCoding, NSCoding {     var timeIntervalSinceReferenceDate: NSTimeInterval { get }     init()     init(timeIntervalSinceReferenceDate ti: NSTimeInterval)     init?(coder aDecoder: NSCoder) } extension NSDate : CKRecordValue { } extension NSDate : _Reflectable { } extension NSDate {     func timeIntervalSinceDate(_ anotherDate: NSDate) -> NSTimeInterval     var timeIntervalSinceNow: NSTimeInterval { get }     var timeIntervalSince1970: NSTimeInterval { get }     func addTimeInterval(_ seconds: NSTimeInterval) -> AnyObject     func dateByAddingTimeInterval(_ ti: NSTimeInterval) -> Self     func earlierDate(_ anotherDate: NSDate) -> NSDate     func laterDate(_ anotherDate: NSDate) -> NSDate     func compare(_ other: NSDate) -> NSComparisonResult     func isEqualToDate(_ otherDate: NSDate) -> Bool     var description: String { get }     func descriptionWithLocale(_ locale: AnyObject?) -> String     class func timeIntervalSinceReferenceDate() -> NSTimeInterval } extension NSDate {     convenience init()     class func date() -> Self     convenience init(timeIntervalSinceNow secs: NSTimeInterval)     class func dateWithTimeIntervalSinceNow(_ secs: NSTimeInterval) -> Self     convenience init(timeIntervalSinceReferenceDate ti: NSTimeInterval)     class func dateWithTimeIntervalSinceReferenceDate(_ ti: NSTimeInterval) -> Self     convenience init(timeIntervalSince1970 secs: NSTimeInterval)     class func dateWithTimeIntervalSince1970(_ secs: NSTimeInterval) -> Self     convenience init(timeInterval secsToBeAdded: NSTimeInterval, sinceDate date: NSDate)     class func dateWithTimeInterval(_ secsToBeAdded: NSTimeInterval, sinceDate date: NSDate) -> Self     class func distantFuture() -> NSDate     class func distantPast() -> NSDate     convenience init(timeIntervalSinceNow secs: NSTimeInterval)     convenience init(timeIntervalSince1970 secs: NSTimeInterval)     convenience init(timeInterval secsToBeAdded: NSTimeInterval, sinceDate date: NSDate) } extension NSDate : _Reflectable { } ``` | AnyObject, CKRecordValue, NSCoding, NSCopying, NSObjectProtocol, NSSecureCoding |

Modified [NSDate.descriptionWithLocale(_: AnyObject?) -> String](https://developer.apple.com/documentation/foundation/nsdate/1414108-descriptionwithlocale)

|  | Declaration |
| --- | --- |
| From | ``` func descriptionWithLocale(_ locale: AnyObject?) -> String? ``` |
| To | ``` func descriptionWithLocale(_ locale: AnyObject?) -> String ``` |

Modified [NSDate.distantFuture() -> NSDate [class]](https://developer.apple.com/documentation/foundation/nsdate/1415385-distantfuture)

|  | Declaration |
| --- | --- |
| From | ``` class func distantFuture() -> AnyObject ``` |
| To | ``` class func distantFuture() -> NSDate ``` |

Modified [NSDate.distantPast() -> NSDate [class]](https://developer.apple.com/documentation/foundation/nsdate/1418197-distantpast)

|  | Declaration |
| --- | --- |
| From | ``` class func distantPast() -> AnyObject ``` |
| To | ``` class func distantPast() -> NSDate ``` |

Modified [NSDate.init(coder: NSCoder)](https://developer.apple.com/documentation/foundation/nsdate/1412602-init)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified [NSDateComponentsFormatterUnitsStyle [enum]](https://developer.apple.com/documentation/foundation/datecomponentsformatter/unitsstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NSDateComponentsFormatterZeroFormattingBehavior [struct]](https://developer.apple.com/documentation/foundation/datecomponentsformatter/zeroformattingbehavior)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSDateComponentsFormatterZeroFormattingBehavior : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var Default: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var DropLeading: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var DropMiddle: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var DropTrailing: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var DropAll: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var Pad: NSDateComponentsFormatterZeroFormattingBehavior { get } } ``` | RawOptionSetType |
| To | ``` struct NSDateComponentsFormatterZeroFormattingBehavior : OptionSetType {     init(rawValue rawValue: UInt)     static var None: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var Default: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var DropLeading: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var DropMiddle: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var DropTrailing: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var DropAll: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var Pad: NSDateComponentsFormatterZeroFormattingBehavior { get } } ``` | OptionSetType |

Modified [NSDateFormatter](https://developer.apple.com/documentation/foundation/dateformatter)

|  | Declaration |
| --- | --- |
| From | ``` class NSDateFormatter : NSFormatter {     var formattingContext: NSFormattingContext     func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>, forString string: String, range rangep: UnsafeMutablePointer<NSRange>, error error: NSErrorPointer) -> Bool     func stringFromDate(_ date: NSDate) -> String     func dateFromString(_ string: String) -> NSDate?     class func localizedStringFromDate(_ date: NSDate, dateStyle dstyle: NSDateFormatterStyle, timeStyle tstyle: NSDateFormatterStyle) -> String     class func dateFormatFromTemplate(_ tmplate: String, options opts: Int, locale locale: NSLocale) -> String?     class func defaultFormatterBehavior() -> NSDateFormatterBehavior     class func setDefaultFormatterBehavior(_ behavior: NSDateFormatterBehavior)     func setLocalizedDateFormatFromTemplate(_ dateFormatTemplate: String)     var dateFormat: String!     var dateStyle: NSDateFormatterStyle     var timeStyle: NSDateFormatterStyle     @NSCopying var locale: NSLocale!     var generatesCalendarDates: Bool     var formatterBehavior: NSDateFormatterBehavior     @NSCopying var timeZone: NSTimeZone!     @NSCopying var calendar: NSCalendar!     var lenient: Bool     @NSCopying var twoDigitStartDate: NSDate!     @NSCopying var defaultDate: NSDate?     var eraSymbols: [AnyObject]!     var monthSymbols: [AnyObject]!     var shortMonthSymbols: [AnyObject]!     var weekdaySymbols: [AnyObject]!     var shortWeekdaySymbols: [AnyObject]!     var AMSymbol: String!     var PMSymbol: String!     var longEraSymbols: [AnyObject]!     var veryShortMonthSymbols: [AnyObject]!     var standaloneMonthSymbols: [AnyObject]!     var shortStandaloneMonthSymbols: [AnyObject]!     var veryShortStandaloneMonthSymbols: [AnyObject]!     var veryShortWeekdaySymbols: [AnyObject]!     var standaloneWeekdaySymbols: [AnyObject]!     var shortStandaloneWeekdaySymbols: [AnyObject]!     var veryShortStandaloneWeekdaySymbols: [AnyObject]!     var quarterSymbols: [AnyObject]!     var shortQuarterSymbols: [AnyObject]!     var standaloneQuarterSymbols: [AnyObject]!     var shortStandaloneQuarterSymbols: [AnyObject]!     @NSCopying var gregorianStartDate: NSDate!     var doesRelativeDateFormatting: Bool } ``` |
| To | ``` class NSDateFormatter : NSFormatter {     var formattingContext: NSFormattingContext     func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>, forString string: String, range rangep: UnsafeMutablePointer<NSRange>) throws     func stringFromDate(_ date: NSDate) -> String     func dateFromString(_ string: String) -> NSDate?     class func localizedStringFromDate(_ date: NSDate, dateStyle dstyle: NSDateFormatterStyle, timeStyle tstyle: NSDateFormatterStyle) -> String     class func dateFormatFromTemplate(_ tmplate: String, options opts: Int, locale locale: NSLocale?) -> String?     class func defaultFormatterBehavior() -> NSDateFormatterBehavior     class func setDefaultFormatterBehavior(_ behavior: NSDateFormatterBehavior)     func setLocalizedDateFormatFromTemplate(_ dateFormatTemplate: String)     var dateFormat: String!     var dateStyle: NSDateFormatterStyle     var timeStyle: NSDateFormatterStyle     @NSCopying var locale: NSLocale!     var generatesCalendarDates: Bool     var formatterBehavior: NSDateFormatterBehavior     @NSCopying var timeZone: NSTimeZone!     @NSCopying var calendar: NSCalendar!     var lenient: Bool     @NSCopying var twoDigitStartDate: NSDate?     @NSCopying var defaultDate: NSDate?     var eraSymbols: [String]!     var monthSymbols: [String]!     var shortMonthSymbols: [String]!     var weekdaySymbols: [String]!     var shortWeekdaySymbols: [String]!     var AMSymbol: String!     var PMSymbol: String!     var longEraSymbols: [String]!     var veryShortMonthSymbols: [String]!     var standaloneMonthSymbols: [String]!     var shortStandaloneMonthSymbols: [String]!     var veryShortStandaloneMonthSymbols: [String]!     var veryShortWeekdaySymbols: [String]!     var standaloneWeekdaySymbols: [String]!     var shortStandaloneWeekdaySymbols: [String]!     var veryShortStandaloneWeekdaySymbols: [String]!     var quarterSymbols: [String]!     var shortQuarterSymbols: [String]!     var standaloneQuarterSymbols: [String]!     var shortStandaloneQuarterSymbols: [String]!     @NSCopying var gregorianStartDate: NSDate?     var doesRelativeDateFormatting: Bool } ``` |

Modified [NSDateFormatter.dateFormatFromTemplate(_: String, options: Int, locale: NSLocale?) -> String? [class]](https://developer.apple.com/documentation/foundation/dateformatter/1408112-dateformat)

|  | Declaration |
| --- | --- |
| From | ``` class func dateFormatFromTemplate(_ tmplate: String, options opts: Int, locale locale: NSLocale) -> String? ``` |
| To | ``` class func dateFormatFromTemplate(_ tmplate: String, options opts: Int, locale locale: NSLocale?) -> String? ``` |

Modified [NSDateFormatter.eraSymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1418282-erasymbols)

|  | Declaration |
| --- | --- |
| From | ``` var eraSymbols: [AnyObject]! ``` |
| To | ``` var eraSymbols: [String]! ``` |

Modified [NSDateFormatter.getObjectValue(_: AutoreleasingUnsafeMutablePointer<AnyObject?>, forString: String, range: UnsafeMutablePointer<NSRange>) throws](https://developer.apple.com/documentation/foundation/nsdateformatter/1409248-getobjectvalue)

|  | Declaration |
| --- | --- |
| From | ``` func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>, forString string: String, range rangep: UnsafeMutablePointer<NSRange>, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>, forString string: String, range rangep: UnsafeMutablePointer<NSRange>) throws ``` |

Modified [NSDateFormatter.gregorianStartDate](https://developer.apple.com/documentation/foundation/nsdateformatter/1416389-gregorianstartdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var gregorianStartDate: NSDate! ``` |
| To | ``` @NSCopying var gregorianStartDate: NSDate? ``` |

Modified [NSDateFormatter.longEraSymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1418081-longerasymbols)

|  | Declaration |
| --- | --- |
| From | ``` var longEraSymbols: [AnyObject]! ``` |
| To | ``` var longEraSymbols: [String]! ``` |

Modified [NSDateFormatter.monthSymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1412049-monthsymbols)

|  | Declaration |
| --- | --- |
| From | ``` var monthSymbols: [AnyObject]! ``` |
| To | ``` var monthSymbols: [String]! ``` |

Modified [NSDateFormatter.quarterSymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1417587-quartersymbols)

|  | Declaration |
| --- | --- |
| From | ``` var quarterSymbols: [AnyObject]! ``` |
| To | ``` var quarterSymbols: [String]! ``` |

Modified [NSDateFormatter.shortMonthSymbols](https://developer.apple.com/documentation/foundation/dateformatter/1409209-shortmonthsymbols)

|  | Declaration |
| --- | --- |
| From | ``` var shortMonthSymbols: [AnyObject]! ``` |
| To | ``` var shortMonthSymbols: [String]! ``` |

Modified [NSDateFormatter.shortQuarterSymbols](https://developer.apple.com/documentation/foundation/dateformatter/1409851-shortquartersymbols)

|  | Declaration |
| --- | --- |
| From | ``` var shortQuarterSymbols: [AnyObject]! ``` |
| To | ``` var shortQuarterSymbols: [String]! ``` |

Modified [NSDateFormatter.shortStandaloneMonthSymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1414771-shortstandalonemonthsymbols)

|  | Declaration |
| --- | --- |
| From | ``` var shortStandaloneMonthSymbols: [AnyObject]! ``` |
| To | ``` var shortStandaloneMonthSymbols: [String]! ``` |

Modified [NSDateFormatter.shortStandaloneQuarterSymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1416421-shortstandalonequartersymbols)

|  | Declaration |
| --- | --- |
| From | ``` var shortStandaloneQuarterSymbols: [AnyObject]! ``` |
| To | ``` var shortStandaloneQuarterSymbols: [String]! ``` |

Modified [NSDateFormatter.shortStandaloneWeekdaySymbols](https://developer.apple.com/documentation/foundation/dateformatter/1409119-shortstandaloneweekdaysymbols)

|  | Declaration |
| --- | --- |
| From | ``` var shortStandaloneWeekdaySymbols: [AnyObject]! ``` |
| To | ``` var shortStandaloneWeekdaySymbols: [String]! ``` |

Modified [NSDateFormatter.shortWeekdaySymbols](https://developer.apple.com/documentation/foundation/dateformatter/1416121-shortweekdaysymbols)

|  | Declaration |
| --- | --- |
| From | ``` var shortWeekdaySymbols: [AnyObject]! ``` |
| To | ``` var shortWeekdaySymbols: [String]! ``` |

Modified [NSDateFormatter.standaloneMonthSymbols](https://developer.apple.com/documentation/foundation/dateformatter/1416227-standalonemonthsymbols)

|  | Declaration |
| --- | --- |
| From | ``` var standaloneMonthSymbols: [AnyObject]! ``` |
| To | ``` var standaloneMonthSymbols: [String]! ``` |

Modified [NSDateFormatter.standaloneQuarterSymbols](https://developer.apple.com/documentation/foundation/dateformatter/1411487-standalonequartersymbols)

|  | Declaration |
| --- | --- |
| From | ``` var standaloneQuarterSymbols: [AnyObject]! ``` |
| To | ``` var standaloneQuarterSymbols: [String]! ``` |

Modified [NSDateFormatter.standaloneWeekdaySymbols](https://developer.apple.com/documentation/foundation/dateformatter/1413618-standaloneweekdaysymbols)

|  | Declaration |
| --- | --- |
| From | ``` var standaloneWeekdaySymbols: [AnyObject]! ``` |
| To | ``` var standaloneWeekdaySymbols: [String]! ``` |

Modified [NSDateFormatter.twoDigitStartDate](https://developer.apple.com/documentation/foundation/nsdateformatter/1417203-twodigitstartdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var twoDigitStartDate: NSDate! ``` |
| To | ``` @NSCopying var twoDigitStartDate: NSDate? ``` |

Modified [NSDateFormatter.veryShortMonthSymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1413632-veryshortmonthsymbols)

|  | Declaration |
| --- | --- |
| From | ``` var veryShortMonthSymbols: [AnyObject]! ``` |
| To | ``` var veryShortMonthSymbols: [String]! ``` |

Modified [NSDateFormatter.veryShortStandaloneMonthSymbols](https://developer.apple.com/documentation/foundation/dateformatter/1413322-veryshortstandalonemonthsymbols)

|  | Declaration |
| --- | --- |
| From | ``` var veryShortStandaloneMonthSymbols: [AnyObject]! ``` |
| To | ``` var veryShortStandaloneMonthSymbols: [String]! ``` |

Modified [NSDateFormatter.veryShortStandaloneWeekdaySymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1418238-veryshortstandaloneweekdaysymbol)

|  | Declaration |
| --- | --- |
| From | ``` var veryShortStandaloneWeekdaySymbols: [AnyObject]! ``` |
| To | ``` var veryShortStandaloneWeekdaySymbols: [String]! ``` |

Modified [NSDateFormatter.veryShortWeekdaySymbols](https://developer.apple.com/documentation/foundation/dateformatter/1415109-veryshortweekdaysymbols)

|  | Declaration |
| --- | --- |
| From | ``` var veryShortWeekdaySymbols: [AnyObject]! ``` |
| To | ``` var veryShortWeekdaySymbols: [String]! ``` |

Modified [NSDateFormatter.weekdaySymbols](https://developer.apple.com/documentation/foundation/dateformatter/1412405-weekdaysymbols)

|  | Declaration |
| --- | --- |
| From | ``` var weekdaySymbols: [AnyObject]! ``` |
| To | ``` var weekdaySymbols: [String]! ``` |

Modified [NSDateFormatterBehavior [enum]](https://developer.apple.com/documentation/foundation/nsdateformatterbehavior)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSDateFormatterStyle [enum]](https://developer.apple.com/documentation/foundation/nsdateformatterstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSDateIntervalFormatter](https://developer.apple.com/documentation/foundation/dateintervalformatter)

|  | Declaration |
| --- | --- |
| From | ``` class NSDateIntervalFormatter : NSFormatter {     @NSCopying var locale: NSLocale?     @NSCopying var calendar: NSCalendar?     @NSCopying var timeZone: NSTimeZone?     var dateTemplate: String?     var dateStyle: NSDateIntervalFormatterStyle     var timeStyle: NSDateIntervalFormatterStyle     func stringFromDate(_ fromDate: NSDate, toDate toDate: NSDate) -> String } ``` |
| To | ``` class NSDateIntervalFormatter : NSFormatter {     @NSCopying var locale: NSLocale!     @NSCopying var calendar: NSCalendar!     @NSCopying var timeZone: NSTimeZone!     var dateTemplate: String!     var dateStyle: NSDateIntervalFormatterStyle     var timeStyle: NSDateIntervalFormatterStyle     func stringFromDate(_ fromDate: NSDate, toDate toDate: NSDate) -> String } ``` |

Modified [NSDateIntervalFormatter.calendar](https://developer.apple.com/documentation/foundation/dateintervalformatter/1417984-calendar)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var calendar: NSCalendar? ``` |
| To | ``` @NSCopying var calendar: NSCalendar! ``` |

Modified [NSDateIntervalFormatter.dateTemplate](https://developer.apple.com/documentation/foundation/dateintervalformatter/1407373-datetemplate)

|  | Declaration |
| --- | --- |
| From | ``` var dateTemplate: String? ``` |
| To | ``` var dateTemplate: String! ``` |

Modified [NSDateIntervalFormatter.locale](https://developer.apple.com/documentation/foundation/nsdateintervalformatter/1409992-locale)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var locale: NSLocale? ``` |
| To | ``` @NSCopying var locale: NSLocale! ``` |

Modified [NSDateIntervalFormatter.timeZone](https://developer.apple.com/documentation/foundation/dateintervalformatter/1410228-timezone)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var timeZone: NSTimeZone? ``` |
| To | ``` @NSCopying var timeZone: NSTimeZone! ``` |

Modified [NSDateIntervalFormatterStyle [enum]](https://developer.apple.com/documentation/foundation/nsdateintervalformatterstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSDecimalNumber](https://developer.apple.com/documentation/foundation/nsdecimalnumber)

|  | Declaration |
| --- | --- |
| From | ``` class NSDecimalNumber : NSNumber {     convenience init(mantissa mantissa: UInt64, exponent exponent: Int16, isNegative flag: Bool)     init!(decimal dcm: NSDecimal)     convenience init(string numberValue: String?)     convenience init(string numberValue: String?, locale locale: AnyObject?)     func descriptionWithLocale(_ locale: AnyObject?) -> String     var decimalValue: NSDecimal { get }     class func decimalNumberWithMantissa(_ mantissa: UInt64, exponent exponent: Int16, isNegative flag: Bool) -> NSDecimalNumber     class func decimalNumberWithDecimal(_ dcm: NSDecimal) -> NSDecimalNumber!     class func decimalNumberWithString(_ numberValue: String?) -> NSDecimalNumber     class func decimalNumberWithString(_ numberValue: String?, locale locale: AnyObject?) -> NSDecimalNumber     class func zero() -> NSDecimalNumber     class func one() -> NSDecimalNumber     class func minimumDecimalNumber() -> NSDecimalNumber     class func maximumDecimalNumber() -> NSDecimalNumber     class func notANumber() -> NSDecimalNumber     func decimalNumberByAdding(_ decimalNumber: NSDecimalNumber) -> NSDecimalNumber     func decimalNumberByAdding(_ decimalNumber: NSDecimalNumber, withBehavior behavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber     func decimalNumberBySubtracting(_ decimalNumber: NSDecimalNumber) -> NSDecimalNumber     func decimalNumberBySubtracting(_ decimalNumber: NSDecimalNumber, withBehavior behavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber     func decimalNumberByMultiplyingBy(_ decimalNumber: NSDecimalNumber) -> NSDecimalNumber     func decimalNumberByMultiplyingBy(_ decimalNumber: NSDecimalNumber, withBehavior behavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber     func decimalNumberByDividingBy(_ decimalNumber: NSDecimalNumber) -> NSDecimalNumber     func decimalNumberByDividingBy(_ decimalNumber: NSDecimalNumber, withBehavior behavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber     func decimalNumberByRaisingToPower(_ power: Int) -> NSDecimalNumber     func decimalNumberByRaisingToPower(_ power: Int, withBehavior behavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber     func decimalNumberByMultiplyingByPowerOf10(_ power: Int16) -> NSDecimalNumber     func decimalNumberByMultiplyingByPowerOf10(_ power: Int16, withBehavior behavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber     func decimalNumberByRoundingAccordingToBehavior(_ behavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber     func compare(_ decimalNumber: NSNumber) -> NSComparisonResult     class func setDefaultBehavior(_ behavior: NSDecimalNumberBehaviors)     class func defaultBehavior() -> NSDecimalNumberBehaviors     var objCType: UnsafePointer<Int8> { get }     var doubleValue: Double { get } } ``` |
| To | ``` class NSDecimalNumber : NSNumber {     convenience init(mantissa mantissa: UInt64, exponent exponent: Int16, isNegative flag: Bool)     init(decimal dcm: NSDecimal)     convenience init(string numberValue: String?)     convenience init(string numberValue: String?, locale locale: AnyObject?)     func descriptionWithLocale(_ locale: AnyObject?) -> String     var decimalValue: NSDecimal { get }     class func decimalNumberWithMantissa(_ mantissa: UInt64, exponent exponent: Int16, isNegative flag: Bool) -> NSDecimalNumber     class func decimalNumberWithDecimal(_ dcm: NSDecimal) -> NSDecimalNumber     class func decimalNumberWithString(_ numberValue: String?) -> NSDecimalNumber     class func decimalNumberWithString(_ numberValue: String?, locale locale: AnyObject?) -> NSDecimalNumber     class func zero() -> NSDecimalNumber     class func one() -> NSDecimalNumber     class func minimumDecimalNumber() -> NSDecimalNumber     class func maximumDecimalNumber() -> NSDecimalNumber     class func notANumber() -> NSDecimalNumber     func decimalNumberByAdding(_ decimalNumber: NSDecimalNumber) -> NSDecimalNumber     func decimalNumberByAdding(_ decimalNumber: NSDecimalNumber, withBehavior behavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber     func decimalNumberBySubtracting(_ decimalNumber: NSDecimalNumber) -> NSDecimalNumber     func decimalNumberBySubtracting(_ decimalNumber: NSDecimalNumber, withBehavior behavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber     func decimalNumberByMultiplyingBy(_ decimalNumber: NSDecimalNumber) -> NSDecimalNumber     func decimalNumberByMultiplyingBy(_ decimalNumber: NSDecimalNumber, withBehavior behavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber     func decimalNumberByDividingBy(_ decimalNumber: NSDecimalNumber) -> NSDecimalNumber     func decimalNumberByDividingBy(_ decimalNumber: NSDecimalNumber, withBehavior behavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber     func decimalNumberByRaisingToPower(_ power: Int) -> NSDecimalNumber     func decimalNumberByRaisingToPower(_ power: Int, withBehavior behavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber     func decimalNumberByMultiplyingByPowerOf10(_ power: Int16) -> NSDecimalNumber     func decimalNumberByMultiplyingByPowerOf10(_ power: Int16, withBehavior behavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber     func decimalNumberByRoundingAccordingToBehavior(_ behavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber     func compare(_ decimalNumber: NSNumber) -> NSComparisonResult     class func setDefaultBehavior(_ behavior: NSDecimalNumberBehaviors)     class func defaultBehavior() -> NSDecimalNumberBehaviors     var objCType: UnsafePointer<Int8> { get }     var doubleValue: Double { get } } ``` |

Modified [NSDecimalNumber.init(decimal: NSDecimal)](https://developer.apple.com/documentation/foundation/nsdecimalnumber/1412692-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(decimal dcm: NSDecimal) ``` |
| To | ``` init(decimal dcm: NSDecimal) ``` |

Modified [NSDecimalNumberBehaviors](https://developer.apple.com/documentation/foundation/nsdecimalnumberbehaviors)

|  | Declaration |
| --- | --- |
| From | ``` protocol NSDecimalNumberBehaviors {     func roundingMode() -> NSRoundingMode     func scale() -> Int16     func exceptionDuringOperation(_ operation: Selector, error error: NSCalculationError, leftOperand leftOperand: NSDecimalNumber, rightOperand rightOperand: NSDecimalNumber) -> NSDecimalNumber? } ``` |
| To | ``` protocol NSDecimalNumberBehaviors {     func roundingMode() -> NSRoundingMode     func scale() -> Int16     func exceptionDuringOperation(_ operation: Selector, error error: NSCalculationError, leftOperand leftOperand: NSDecimalNumber, rightOperand rightOperand: NSDecimalNumber?) -> NSDecimalNumber? } ``` |

Modified [NSDecimalNumberBehaviors.exceptionDuringOperation(_: Selector, error: NSCalculationError, leftOperand: NSDecimalNumber, rightOperand: NSDecimalNumber?) -> NSDecimalNumber?](https://developer.apple.com/documentation/foundation/nsdecimalnumberbehaviors/1411766-exceptionduringoperation)

|  | Declaration |
| --- | --- |
| From | ``` func exceptionDuringOperation(_ operation: Selector, error error: NSCalculationError, leftOperand leftOperand: NSDecimalNumber, rightOperand rightOperand: NSDecimalNumber) -> NSDecimalNumber? ``` |
| To | ``` func exceptionDuringOperation(_ operation: Selector, error error: NSCalculationError, leftOperand leftOperand: NSDecimalNumber, rightOperand rightOperand: NSDecimalNumber?) -> NSDecimalNumber? ``` |

Modified [NSDictionary](https://developer.apple.com/documentation/foundation/nsdictionary)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSDictionary : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding, NSFastEnumeration {     var count: Int { get }     func objectForKey(_ aKey: AnyObject) -> AnyObject?     func keyEnumerator() -> NSEnumerator     init()     init(objects objects: UnsafePointer<AnyObject?>, forKeys keys: UnsafePointer<NSCopying?>, count cnt: Int)     init(coder aDecoder: NSCoder) } extension NSDictionary : DictionaryLiteralConvertible {     required convenience init(dictionaryLiteral elements: (NSCopying, AnyObject)...) } extension NSDictionary : SequenceType {     final class Generator : GeneratorType {         func next() -> (key: AnyObject, value: AnyObject)?     }     func generate() -> NSDictionary.Generator } extension NSDictionary {     convenience init(objectsAndKeys objects: AnyObject...) } extension NSDictionary {     @objc(_swiftInitWithDictionary_NSDictionary:) convenience init(dictionary otherDictionary: NSDictionary) } extension NSDictionary : Reflectable {     func getMirror() -> MirrorType } extension NSDictionary {     var allKeys: [AnyObject] { get }     func allKeysForObject(_ anObject: AnyObject) -> [AnyObject]     var allValues: [AnyObject] { get }     var description: String { get }     var descriptionInStringsFileFormat: String { get }     func descriptionWithLocale(_ locale: AnyObject?) -> String     func descriptionWithLocale(_ locale: AnyObject?, indent level: Int) -> String     func isEqualToDictionary(_ otherDictionary: [NSObject : AnyObject]) -> Bool     func objectEnumerator() -> NSEnumerator     func objectsForKeys(_ keys: [AnyObject], notFoundMarker marker: AnyObject) -> [AnyObject]     func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool) -> Bool     func writeToURL(_ url: NSURL, atomically atomically: Bool) -> Bool     func keysSortedByValueUsingSelector(_ comparator: Selector) -> [AnyObject]     func getObjects(_ objects: AutoreleasingUnsafeMutablePointer<AnyObject?>, andKeys keys: AutoreleasingUnsafeMutablePointer<AnyObject?>)     subscript (key: NSCopying) -> AnyObject? { get }     func objectForKeyedSubscript(_ key: NSCopying) -> AnyObject?     func enumerateKeysAndObjectsUsingBlock(_ block: (AnyObject!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateKeysAndObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Void)     func keysSortedByValueUsingComparator(_ cmptr: NSComparator) -> [AnyObject]     func keysSortedByValueWithOptions(_ opts: NSSortOptions, usingComparator cmptr: NSComparator) -> [AnyObject]     func keysOfEntriesPassingTest(_ predicate: (AnyObject!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject>     func keysOfEntriesWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject> } extension NSDictionary {     convenience init!()     class func dictionary() -> Self!     convenience init(object object: AnyObject, forKey key: NSCopying)     class func dictionaryWithObject(_ object: AnyObject, forKey key: NSCopying) -> Self     convenience init!(objects objects: UnsafePointer<AnyObject?>, forKeys keys: UnsafePointer<NSCopying?>, count cnt: Int)     class func dictionaryWithObjects(_ objects: UnsafePointer<AnyObject?>, forKeys keys: UnsafePointer<NSCopying?>, count cnt: Int) -> Self!     convenience init(dictionary dict: [NSObject : AnyObject])     class func dictionaryWithDictionary(_ dict: [NSObject : AnyObject]) -> Self     convenience init(objects objects: [AnyObject], forKeys keys: [AnyObject])     class func dictionaryWithObjects(_ objects: [AnyObject], forKeys keys: [AnyObject]) -> Self     convenience init(dictionary otherDictionary: [NSObject : AnyObject])     convenience init(dictionary otherDictionary: [NSObject : AnyObject], copyItems flag: Bool)     convenience init(objects objects: [AnyObject], forKeys keys: [AnyObject])     init?(contentsOfFile path: String) -> NSDictionary     class func dictionaryWithContentsOfFile(_ path: String) -> [NSObject : AnyObject]?     init?(contentsOfURL url: NSURL) -> NSDictionary     class func dictionaryWithContentsOfURL(_ url: NSURL) -> [NSObject : AnyObject]?     convenience init?(contentsOfFile path: String)     convenience init?(contentsOfURL url: NSURL) } extension NSDictionary {     class func sharedKeySetForKeys(_ keys: [AnyObject]) -> AnyObject } extension NSDictionary {     func fileSize() -> UInt64     func fileModificationDate() -> NSDate?     func fileType() -> String?     func filePosixPermissions() -> Int     func fileOwnerAccountName() -> String?     func fileGroupOwnerAccountName() -> String?     func fileSystemNumber() -> Int     func fileSystemFileNumber() -> Int     func fileExtensionHidden() -> Bool     func fileHFSCreatorCode() -> OSType     func fileHFSTypeCode() -> OSType     func fileIsImmutable() -> Bool     func fileIsAppendOnly() -> Bool     func fileCreationDate() -> NSDate?     func fileOwnerAccountID() -> NSNumber?     func fileGroupOwnerAccountID() -> NSNumber? } extension NSDictionary {     func valueForKey(_ key: String) -> AnyObject? } extension NSDictionary : Reflectable {     func getMirror() -> MirrorType } extension NSDictionary {     @objc(_swiftInitWithDictionary_NSDictionary:) convenience init(dictionary otherDictionary: NSDictionary) } extension NSDictionary {     convenience init(objectsAndKeys objects: AnyObject...) } extension NSDictionary : SequenceType {     final class Generator : GeneratorType {         func next() -> (key: AnyObject, value: AnyObject)?     }     func generate() -> NSDictionary.Generator } extension NSDictionary : DictionaryLiteralConvertible {     required convenience init(dictionaryLiteral elements: (NSCopying, AnyObject)...) } ``` | AnyObject, DictionaryLiteralConvertible, NSCoding, NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding, Reflectable, SequenceType |
| To | ``` class NSDictionary : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding, NSFastEnumeration {     var count: Int { get }     func objectForKey(_ aKey: AnyObject) -> AnyObject?     func keyEnumerator() -> NSEnumerator     init()     init(objects objects: UnsafePointer<AnyObject?>, forKeys keys: UnsafePointer<NSCopying?>, count cnt: Int)     init?(coder aDecoder: NSCoder) } extension NSDictionary : SequenceType {     final class Generator : GeneratorType {         func next() -> (key: AnyObject, value: AnyObject)?     }     func generate() -> NSDictionary.Generator } extension NSDictionary : DictionaryLiteralConvertible {     required convenience init(dictionaryLiteral elements: (NSCopying, AnyObject)...) } extension NSDictionary {     @objc(_swiftInitWithDictionary_NSDictionary:) convenience init(dictionary otherDictionary: NSDictionary) } extension NSDictionary : _Reflectable { } extension NSDictionary {     var allKeys: [AnyObject] { get }     func allKeysForObject(_ anObject: AnyObject) -> [AnyObject]     var allValues: [AnyObject] { get }     var description: String { get }     var descriptionInStringsFileFormat: String { get }     func descriptionWithLocale(_ locale: AnyObject?) -> String     func descriptionWithLocale(_ locale: AnyObject?, indent level: Int) -> String     func isEqualToDictionary(_ otherDictionary: [NSObject : AnyObject]) -> Bool     func objectEnumerator() -> NSEnumerator     func objectsForKeys(_ keys: [AnyObject], notFoundMarker marker: AnyObject) -> [AnyObject]     func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool) -> Bool     func writeToURL(_ url: NSURL, atomically atomically: Bool) -> Bool     func keysSortedByValueUsingSelector(_ comparator: Selector) -> [AnyObject]     func getObjects(_ objects: AutoreleasingUnsafeMutablePointer<AnyObject?>, andKeys keys: AutoreleasingUnsafeMutablePointer<AnyObject?>, count count: Int)     subscript (_ key: NSCopying) -> AnyObject? { get }     func objectForKeyedSubscript(_ key: NSCopying) -> AnyObject?     func enumerateKeysAndObjectsUsingBlock(_ block: (AnyObject, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateKeysAndObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void)     func keysSortedByValueUsingComparator(_ cmptr: NSComparator) -> [AnyObject]     func keysSortedByValueWithOptions(_ opts: NSSortOptions, usingComparator cmptr: NSComparator) -> [AnyObject]     func keysOfEntriesPassingTest(_ predicate: (AnyObject, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject>     func keysOfEntriesWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject> } extension NSDictionary {     func getObjects(_ objects: AutoreleasingUnsafeMutablePointer<AnyObject?>, andKeys keys: AutoreleasingUnsafeMutablePointer<AnyObject?>) } extension NSDictionary {     convenience init()     class func dictionary() -> Self     convenience init(object object: AnyObject, forKey key: NSCopying)     class func dictionaryWithObject(_ object: AnyObject, forKey key: NSCopying) -> Self     convenience init(objects objects: UnsafePointer<AnyObject?>, forKeys keys: UnsafePointer<NSCopying?>, count cnt: Int)     class func dictionaryWithObjects(_ objects: UnsafePointer<AnyObject?>, forKeys keys: UnsafePointer<NSCopying?>, count cnt: Int) -> Self     convenience init(dictionary dict: [NSObject : AnyObject])     class func dictionaryWithDictionary(_ dict: [NSObject : AnyObject]) -> Self     convenience init(objects objects: [AnyObject], forKeys keys: [NSCopying])     class func dictionaryWithObjects(_ objects: [AnyObject], forKeys keys: [NSCopying]) -> Self     convenience init(dictionary otherDictionary: [NSObject : AnyObject])     convenience init(dictionary otherDictionary: [NSObject : AnyObject], copyItems flag: Bool)     convenience init(objects objects: [AnyObject], forKeys keys: [NSCopying])      init?(contentsOfFile path: String)     class func dictionaryWithContentsOfFile(_ path: String) -> [NSObject : AnyObject]?      init?(contentsOfURL url: NSURL)     class func dictionaryWithContentsOfURL(_ url: NSURL) -> [NSObject : AnyObject]?     convenience init?(contentsOfFile path: String)     convenience init?(contentsOfURL url: NSURL) } extension NSDictionary {     class func sharedKeySetForKeys(_ keys: [NSCopying]) -> AnyObject } extension NSDictionary {     func fileSize() -> UInt64     func fileModificationDate() -> NSDate?     func fileType() -> String?     func filePosixPermissions() -> Int     func fileOwnerAccountName() -> String?     func fileGroupOwnerAccountName() -> String?     func fileSystemNumber() -> Int     func fileSystemFileNumber() -> Int     func fileExtensionHidden() -> Bool     func fileHFSCreatorCode() -> OSType     func fileHFSTypeCode() -> OSType     func fileIsImmutable() -> Bool     func fileIsAppendOnly() -> Bool     func fileCreationDate() -> NSDate?     func fileOwnerAccountID() -> NSNumber?     func fileGroupOwnerAccountID() -> NSNumber? } extension NSDictionary {     func valueForKey(_ key: String) -> AnyObject? } extension NSDictionary : _Reflectable { } extension NSDictionary {     @objc(_swiftInitWithDictionary_NSDictionary:) convenience init(dictionary otherDictionary: NSDictionary) } extension NSDictionary : SequenceType {     final class Generator : GeneratorType {         func next() -> (key: AnyObject, value: AnyObject)?     }     func generate() -> NSDictionary.Generator } extension NSDictionary : DictionaryLiteralConvertible {     required convenience init(dictionaryLiteral elements: (NSCopying, AnyObject)...) } ``` | AnyObject, DictionaryLiteralConvertible, NSCoding, NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding, SequenceType |

Modified [NSDictionary.enumerateKeysAndObjectsUsingBlock(_: (AnyObject, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/foundation/nsdictionary/1414570-enumeratekeysandobjectsusingbloc)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateKeysAndObjectsUsingBlock(_ block: (AnyObject!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateKeysAndObjectsUsingBlock(_ block: (AnyObject, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [NSDictionary.enumerateKeysAndObjectsWithOptions(_: NSEnumerationOptions, usingBlock: (AnyObject, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/foundation/nsdictionary/1409739-enumeratekeysandobjects)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateKeysAndObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateKeysAndObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [NSDictionary.init(coder: NSCoder)](https://developer.apple.com/documentation/foundation/nsdictionary/1417987-initwithcoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified [NSDictionary.init(objects: [AnyObject], forKeys: [NSCopying])](https://developer.apple.com/documentation/foundation/nsdictionary/1410010-initwithobjects)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(objects objects: [AnyObject], forKeys keys: [AnyObject]) ``` |
| To | ``` convenience init(objects objects: [AnyObject], forKeys keys: [NSCopying]) ``` |

Modified [NSDictionary.keysOfEntriesPassingTest(_: (AnyObject, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject>](https://developer.apple.com/documentation/foundation/nsdictionary/1407186-keysofentries)

|  | Declaration |
| --- | --- |
| From | ``` func keysOfEntriesPassingTest(_ predicate: (AnyObject!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject> ``` |
| To | ``` func keysOfEntriesPassingTest(_ predicate: (AnyObject, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject> ``` |

Modified [NSDictionary.keysOfEntriesWithOptions(_: NSEnumerationOptions, passingTest: (AnyObject, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject>](https://developer.apple.com/documentation/foundation/nsdictionary/1416706-keysofentries)

|  | Declaration |
| --- | --- |
| From | ``` func keysOfEntriesWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject> ``` |
| To | ``` func keysOfEntriesWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject> ``` |

Modified [NSDictionary.sharedKeySetForKeys(_: [NSCopying]) -> AnyObject [class]](https://developer.apple.com/documentation/foundation/nsdictionary/1408190-sharedkeyset)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedKeySetForKeys(_ keys: [AnyObject]) -> AnyObject ``` |
| To | ``` class func sharedKeySetForKeys(_ keys: [NSCopying]) -> AnyObject ``` |

Modified [NSDictionary.subscript(_: NSCopying) -> AnyObject?](https://developer.apple.com/documentation/foundation/nsdictionary/1415430-subscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (key: NSCopying) -> AnyObject? { get } ``` |
| To | ``` subscript (_ key: NSCopying) -> AnyObject? { get } ``` |

Modified [NSDirectoryEnumerationOptions [struct]](https://developer.apple.com/documentation/foundation/filemanager/directoryenumerationoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSDirectoryEnumerationOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var SkipsSubdirectoryDescendants: NSDirectoryEnumerationOptions { get }     static var SkipsPackageDescendants: NSDirectoryEnumerationOptions { get }     static var SkipsHiddenFiles: NSDirectoryEnumerationOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSDirectoryEnumerationOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var SkipsSubdirectoryDescendants: NSDirectoryEnumerationOptions { get }     static var SkipsPackageDescendants: NSDirectoryEnumerationOptions { get }     static var SkipsHiddenFiles: NSDirectoryEnumerationOptions { get } } ``` | OptionSetType |

Modified [NSDirectoryEnumerator](https://developer.apple.com/documentation/foundation/nsdirectoryenumerator)

|  | Declaration |
| --- | --- |
| From | ``` class NSDirectoryEnumerator : NSEnumerator {     var fileAttributes: [NSObject : AnyObject]? { get }     var directoryAttributes: [NSObject : AnyObject]? { get }     func skipDescendents()     var level: Int { get }     func skipDescendants() } ``` |
| To | ``` class NSDirectoryEnumerator : NSEnumerator {     var fileAttributes: [String : AnyObject]? { get }     var directoryAttributes: [String : AnyObject]? { get }     func skipDescendents()     var level: Int { get }     func skipDescendants() } ``` |

Modified [NSDirectoryEnumerator.directoryAttributes](https://developer.apple.com/documentation/foundation/filemanager/directoryenumerator/1411357-directoryattributes)

|  | Declaration |
| --- | --- |
| From | ``` var directoryAttributes: [NSObject : AnyObject]? { get } ``` |
| To | ``` var directoryAttributes: [String : AnyObject]? { get } ``` |

Modified [NSDirectoryEnumerator.fileAttributes](https://developer.apple.com/documentation/foundation/nsdirectoryenumerator/1413284-fileattributes)

|  | Declaration |
| --- | --- |
| From | ``` var fileAttributes: [NSObject : AnyObject]? { get } ``` |
| To | ``` var fileAttributes: [String : AnyObject]? { get } ``` |

Modified [NSEnergyFormatter](https://developer.apple.com/documentation/foundation/energyformatter)

|  | Declaration |
| --- | --- |
| From | ``` class NSEnergyFormatter : NSFormatter {     @NSCopying var numberFormatter: NSNumberFormatter     var unitStyle: NSFormattingUnitStyle     var forFoodEnergyUse: Bool     func stringFromValue(_ value: Double, unit unit: NSEnergyFormatterUnit) -> String     func stringFromJoules(_ numberInJoules: Double) -> String     func unitStringFromValue(_ value: Double, unit unit: NSEnergyFormatterUnit) -> String     func unitStringFromJoules(_ numberInJoules: Double, usedUnit unitp: UnsafeMutablePointer<NSEnergyFormatterUnit>) -> String     func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>, forString string: String, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool } ``` |
| To | ``` class NSEnergyFormatter : NSFormatter {     @NSCopying var numberFormatter: NSNumberFormatter!     var unitStyle: NSFormattingUnitStyle     var forFoodEnergyUse: Bool     func stringFromValue(_ value: Double, unit unit: NSEnergyFormatterUnit) -> String     func stringFromJoules(_ numberInJoules: Double) -> String     func unitStringFromValue(_ value: Double, unit unit: NSEnergyFormatterUnit) -> String     func unitStringFromJoules(_ numberInJoules: Double, usedUnit unitp: UnsafeMutablePointer<NSEnergyFormatterUnit>) -> String     func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>, forString string: String, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool } ``` |

Modified [NSEnergyFormatter.numberFormatter](https://developer.apple.com/documentation/foundation/energyformatter/1412614-numberformatter)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var numberFormatter: NSNumberFormatter ``` |
| To | ``` @NSCopying var numberFormatter: NSNumberFormatter! ``` |

Modified [NSEnergyFormatterUnit [enum]](https://developer.apple.com/documentation/foundation/nsenergyformatterunit)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NSEnumerationOptions [struct]](https://developer.apple.com/documentation/foundation/nsenumerationoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSEnumerationOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Concurrent: NSEnumerationOptions { get }     static var Reverse: NSEnumerationOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSEnumerationOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var Concurrent: NSEnumerationOptions { get }     static var Reverse: NSEnumerationOptions { get } } ``` | OptionSetType |

Modified [NSError](https://developer.apple.com/documentation/foundation/nserror)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSError : NSObject, NSCopying, NSSecureCoding, NSCoding {     init(domain domain: String, code code: Int, userInfo dict: [NSObject : AnyObject]?)     class func errorWithDomain(_ domain: String, code code: Int, userInfo dict: [NSObject : AnyObject]?) -> Self     var domain: String { get }     var code: Int { get }     var userInfo: [NSObject : AnyObject]? { get }     var localizedDescription: String { get }     var localizedFailureReason: String? { get }     var localizedRecoverySuggestion: String? { get }     var localizedRecoveryOptions: [AnyObject]? { get }     var recoveryAttempter: AnyObject? { get }     var helpAnchor: String? { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NSError : NSObject, NSCopying, NSSecureCoding, NSCoding {     init(domain domain: String, code code: Int, userInfo dict: [NSObject : AnyObject]?)     class func errorWithDomain(_ domain: String, code code: Int, userInfo dict: [NSObject : AnyObject]?) -> Self     var domain: String { get }     var code: Int { get }     var userInfo: [NSObject : AnyObject] { get }     var localizedDescription: String { get }     var localizedFailureReason: String? { get }     var localizedRecoverySuggestion: String? { get }     var localizedRecoveryOptions: [String]? { get }     var recoveryAttempter: AnyObject? { get }     var helpAnchor: String? { get }     class func setUserInfoValueProviderForDomain(_ errorDomain: String, provider provider: ((NSError, String) -> AnyObject?)?)     class func userInfoValueProviderForDomain(_ errorDomain: String) -> ((NSError, String) -> AnyObject?)? } extension NSError : ErrorType { } extension NSError : ErrorType { } ``` | AnyObject, ErrorType, NSCoding, NSCopying, NSSecureCoding |

Modified [NSError.localizedRecoveryOptions](https://developer.apple.com/documentation/foundation/nserror/1415950-localizedrecoveryoptions)

|  | Declaration |
| --- | --- |
| From | ``` var localizedRecoveryOptions: [AnyObject]? { get } ``` |
| To | ``` var localizedRecoveryOptions: [String]? { get } ``` |

Modified [NSError.userInfo](https://developer.apple.com/documentation/foundation/nserror/1411580-userinfo)

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]? { get } ``` |
| To | ``` var userInfo: [NSObject : AnyObject] { get } ``` |

Modified [NSException](https://developer.apple.com/documentation/foundation/nsexception)

|  | Declaration |
| --- | --- |
| From | ``` class NSException : NSObject, NSCopying, NSCoding {     init(name name: String, reason reason: String?, userInfo userInfo: [NSObject : AnyObject]?) -> NSException     class func exceptionWithName(_ name: String, reason reason: String?, userInfo userInfo: [NSObject : AnyObject]?) -> NSException     init(name aName: String, reason aReason: String?, userInfo aUserInfo: [NSObject : AnyObject]?)     var name: String { get }     var reason: String? { get }     var userInfo: [NSObject : AnyObject]? { get }     var callStackReturnAddresses: [AnyObject] { get }     var callStackSymbols: [AnyObject] { get }     func raise() } extension NSException {     class func raise(_ name: String, format format: String, arguments argList: CVaListPointer) } ``` |
| To | ``` class NSException : NSObject, NSCopying, NSCoding {      init(name name: String, reason reason: String?, userInfo userInfo: [NSObject : AnyObject]?)     class func exceptionWithName(_ name: String, reason reason: String?, userInfo userInfo: [NSObject : AnyObject]?) -> NSException     init(name aName: String, reason aReason: String?, userInfo aUserInfo: [NSObject : AnyObject]?)     var name: String { get }     var reason: String? { get }     var userInfo: [NSObject : AnyObject]? { get }     var callStackReturnAddresses: [NSNumber] { get }     var callStackSymbols: [String] { get }     func raise() } extension NSException {     class func raise(_ name: String, format format: String, arguments argList: CVaListPointer) } ``` |

Modified [NSException.callStackReturnAddresses](https://developer.apple.com/documentation/foundation/nsexception/1412165-callstackreturnaddresses)

|  | Declaration |
| --- | --- |
| From | ``` var callStackReturnAddresses: [AnyObject] { get } ``` |
| To | ``` var callStackReturnAddresses: [NSNumber] { get } ``` |

Modified [NSException.callStackSymbols](https://developer.apple.com/documentation/foundation/nsexception/1416845-callstacksymbols)

|  | Declaration |
| --- | --- |
| From | ``` var callStackSymbols: [AnyObject] { get } ``` |
| To | ``` var callStackSymbols: [String] { get } ``` |

Modified [NSExpression](https://developer.apple.com/documentation/foundation/nsexpression)

|  | Declaration |
| --- | --- |
| From | ``` class NSExpression : NSObject, NSSecureCoding, NSCoding, NSCopying {     init(format expressionFormat: String, argumentArray arguments: [AnyObject]) -> NSExpression     class func expressionWithFormat(_ expressionFormat: String, argumentArray arguments: [AnyObject]) -> NSExpression     init(format expressionFormat: String, arguments argList: CVaListPointer) -> NSExpression     class func expressionWithFormat(_ expressionFormat: String, arguments argList: CVaListPointer) -> NSExpression     init(forConstantValue obj: AnyObject) -> NSExpression     class func expressionForConstantValue(_ obj: AnyObject) -> NSExpression     class func expressionForEvaluatedObject() -> NSExpression     init(forVariable string: String) -> NSExpression     class func expressionForVariable(_ string: String) -> NSExpression     init(forKeyPath keyPath: String) -> NSExpression     class func expressionForKeyPath(_ keyPath: String) -> NSExpression     init(forFunction name: String, arguments parameters: [AnyObject]) -> NSExpression     class func expressionForFunction(_ name: String, arguments parameters: [AnyObject]) -> NSExpression     init(forAggregate subexpressions: [AnyObject]) -> NSExpression     class func expressionForAggregate(_ subexpressions: [AnyObject]) -> NSExpression     init(forUnionSet left: NSExpression, with right: NSExpression) -> NSExpression     class func expressionForUnionSet(_ left: NSExpression, with right: NSExpression) -> NSExpression     init(forIntersectSet left: NSExpression, with right: NSExpression) -> NSExpression     class func expressionForIntersectSet(_ left: NSExpression, with right: NSExpression) -> NSExpression     init(forMinusSet left: NSExpression, with right: NSExpression) -> NSExpression     class func expressionForMinusSet(_ left: NSExpression, with right: NSExpression) -> NSExpression     init(forSubquery expression: NSExpression, usingIteratorVariable variable: String, predicate predicate: AnyObject) -> NSExpression     class func expressionForSubquery(_ expression: NSExpression, usingIteratorVariable variable: String, predicate predicate: AnyObject) -> NSExpression     init(forFunction target: NSExpression, selectorName name: String, arguments parameters: [AnyObject]) -> NSExpression     class func expressionForFunction(_ target: NSExpression, selectorName name: String, arguments parameters: [AnyObject]) -> NSExpression     class func expressionForAnyKey() -> NSExpression     init(forBlock block: (AnyObject!, [AnyObject]!, NSMutableDictionary!) -> AnyObject!, arguments arguments: [AnyObject]) -> NSExpression     class func expressionForBlock(_ block: (AnyObject!, [AnyObject]!, NSMutableDictionary!) -> AnyObject!, arguments arguments: [AnyObject]) -> NSExpression     init(expressionType type: NSExpressionType)     var expressionType: NSExpressionType { get }     var constantValue: AnyObject { get }     var keyPath: String { get }     var function: String { get }     var variable: String { get }     @NSCopying var operand: NSExpression { get }     var arguments: [AnyObject] { get }     var collection: AnyObject { get }     @NSCopying var predicate: NSPredicate { get }     @NSCopying var leftExpression: NSExpression { get }     @NSCopying var rightExpression: NSExpression { get }     var expressionBlock: (AnyObject!, [AnyObject]!, NSMutableDictionary!) -> AnyObject! { get }     func expressionValueWithObject(_ object: AnyObject?, context context: NSMutableDictionary?) -> AnyObject     func allowEvaluation() } extension NSExpression {     convenience init(format expressionFormat: String, _ args: CVarArgType...) } extension NSExpression {     convenience init(format expressionFormat: String, _ args: CVarArgType...) } ``` |
| To | ``` class NSExpression : NSObject, NSSecureCoding, NSCoding, NSCopying {      init(format expressionFormat: String, argumentArray arguments: [AnyObject])     class func expressionWithFormat(_ expressionFormat: String, argumentArray arguments: [AnyObject]) -> NSExpression      init(format expressionFormat: String, arguments argList: CVaListPointer)     class func expressionWithFormat(_ expressionFormat: String, arguments argList: CVaListPointer) -> NSExpression      init(forConstantValue obj: AnyObject?)     class func expressionForConstantValue(_ obj: AnyObject?) -> NSExpression     class func expressionForEvaluatedObject() -> NSExpression      init(forVariable string: String)     class func expressionForVariable(_ string: String) -> NSExpression      init(forKeyPath keyPath: String)     class func expressionForKeyPath(_ keyPath: String) -> NSExpression      init(forFunction name: String, arguments parameters: [AnyObject])     class func expressionForFunction(_ name: String, arguments parameters: [AnyObject]) -> NSExpression      init(forAggregate subexpressions: [AnyObject])     class func expressionForAggregate(_ subexpressions: [AnyObject]) -> NSExpression      init(forUnionSet left: NSExpression, with right: NSExpression)     class func expressionForUnionSet(_ left: NSExpression, with right: NSExpression) -> NSExpression      init(forIntersectSet left: NSExpression, with right: NSExpression)     class func expressionForIntersectSet(_ left: NSExpression, with right: NSExpression) -> NSExpression      init(forMinusSet left: NSExpression, with right: NSExpression)     class func expressionForMinusSet(_ left: NSExpression, with right: NSExpression) -> NSExpression      init(forSubquery expression: NSExpression, usingIteratorVariable variable: String, predicate predicate: AnyObject)     class func expressionForSubquery(_ expression: NSExpression, usingIteratorVariable variable: String, predicate predicate: AnyObject) -> NSExpression      init(forFunction target: NSExpression, selectorName name: String, arguments parameters: [AnyObject]?)     class func expressionForFunction(_ target: NSExpression, selectorName name: String, arguments parameters: [AnyObject]?) -> NSExpression     class func expressionForAnyKey() -> NSExpression      init(forBlock block: (AnyObject?, [AnyObject], NSMutableDictionary?) -> AnyObject, arguments arguments: [NSExpression]?)     class func expressionForBlock(_ block: (AnyObject?, [AnyObject], NSMutableDictionary?) -> AnyObject, arguments arguments: [NSExpression]?) -> NSExpression      init(forConditional predicate: NSPredicate, trueExpression trueExpression: NSExpression, falseExpression falseExpression: NSExpression)     class func expressionForConditional(_ predicate: NSPredicate, trueExpression trueExpression: NSExpression, falseExpression falseExpression: NSExpression) -> NSExpression     init(expressionType type: NSExpressionType)     init?(coder coder: NSCoder)     var expressionType: NSExpressionType { get }     var constantValue: AnyObject { get }     var keyPath: String { get }     var function: String { get }     var variable: String { get }     @NSCopying var operand: NSExpression { get }     var arguments: [NSExpression]? { get }     var collection: AnyObject { get }     @NSCopying var predicate: NSPredicate { get }     @NSCopying var leftExpression: NSExpression { get }     @NSCopying var rightExpression: NSExpression { get }     @NSCopying var trueExpression: NSExpression { get }     @NSCopying var falseExpression: NSExpression { get }     var expressionBlock: (AnyObject?, [AnyObject], NSMutableDictionary?) -> AnyObject { get }     func expressionValueWithObject(_ object: AnyObject?, context context: NSMutableDictionary?) -> AnyObject     func allowEvaluation() } extension NSExpression {     convenience init(format expressionFormat: String, _ args: CVarArgType...) } extension NSExpression {     convenience init(format expressionFormat: String, _ args: CVarArgType...) } ``` |

Modified [NSExpression.arguments](https://developer.apple.com/documentation/foundation/nsexpression/1411559-arguments)

|  | Declaration |
| --- | --- |
| From | ``` var arguments: [AnyObject] { get } ``` |
| To | ``` var arguments: [NSExpression]? { get } ``` |

Modified [NSExpression.expressionBlock](https://developer.apple.com/documentation/foundation/nsexpression/1409139-expressionblock)

|  | Declaration |
| --- | --- |
| From | ``` var expressionBlock: (AnyObject!, [AnyObject]!, NSMutableDictionary!) -> AnyObject! { get } ``` |
| To | ``` var expressionBlock: (AnyObject?, [AnyObject], NSMutableDictionary?) -> AnyObject { get } ``` |

Modified [NSExpression.init(forAggregate: [AnyObject])](https://developer.apple.com/documentation/foundation/nsexpression/1418366-expressionforaggregate)

|  | Declaration |
| --- | --- |
| From | ``` init(forAggregate subexpressions: [AnyObject]) -> NSExpression ``` |
| To | ``` init(forAggregate subexpressions: [AnyObject]) ``` |

Modified [NSExpression.init(forBlock: (AnyObject?, [AnyObject], NSMutableDictionary?) -> AnyObject, arguments: [NSExpression]?)](https://developer.apple.com/documentation/foundation/nsexpression/1407823-expressionforblock)

|  | Declaration |
| --- | --- |
| From | ``` init(forBlock block: (AnyObject!, [AnyObject]!, NSMutableDictionary!) -> AnyObject!, arguments arguments: [AnyObject]) -> NSExpression ``` |
| To | ``` init(forBlock block: (AnyObject?, [AnyObject], NSMutableDictionary?) -> AnyObject, arguments arguments: [NSExpression]?) ``` |

Modified [NSExpression.init(forConstantValue: AnyObject?)](https://developer.apple.com/documentation/foundation/nsexpression/1415818-init)

|  | Declaration |
| --- | --- |
| From | ``` init(forConstantValue obj: AnyObject) -> NSExpression ``` |
| To | ``` init(forConstantValue obj: AnyObject?) ``` |

Modified [NSExpression.init(forFunction: String, arguments: [AnyObject])](https://developer.apple.com/documentation/foundation/nsexpression/1413747-expressionforfunction)

|  | Declaration |
| --- | --- |
| From | ``` init(forFunction name: String, arguments parameters: [AnyObject]) -> NSExpression ``` |
| To | ``` init(forFunction name: String, arguments parameters: [AnyObject]) ``` |

Modified [NSExpression.init(forFunction: NSExpression, selectorName: String, arguments: [AnyObject]?)](https://developer.apple.com/documentation/foundation/nsexpression/1412905-expressionforfunction)

|  | Declaration |
| --- | --- |
| From | ``` init(forFunction target: NSExpression, selectorName name: String, arguments parameters: [AnyObject]) -> NSExpression ``` |
| To | ``` init(forFunction target: NSExpression, selectorName name: String, arguments parameters: [AnyObject]?) ``` |

Modified [NSExpression.init(forIntersectSet: NSExpression, with: NSExpression)](https://developer.apple.com/documentation/foundation/nsexpression/1409706-init)

|  | Declaration |
| --- | --- |
| From | ``` init(forIntersectSet left: NSExpression, with right: NSExpression) -> NSExpression ``` |
| To | ``` init(forIntersectSet left: NSExpression, with right: NSExpression) ``` |

Modified [NSExpression.init(forKeyPath: String)](https://developer.apple.com/documentation/foundation/nsexpression/1408892-init)

|  | Declaration |
| --- | --- |
| From | ``` init(forKeyPath keyPath: String) -> NSExpression ``` |
| To | ``` init(forKeyPath keyPath: String) ``` |

Modified [NSExpression.init(format: String, argumentArray: [AnyObject])](https://developer.apple.com/documentation/foundation/nsexpression/1413484-init)

|  | Declaration |
| --- | --- |
| From | ``` init(format expressionFormat: String, argumentArray arguments: [AnyObject]) -> NSExpression ``` |
| To | ``` init(format expressionFormat: String, argumentArray arguments: [AnyObject]) ``` |

Modified [NSExpression.init(format: String, arguments: CVaListPointer)](https://developer.apple.com/documentation/foundation/nsexpression/1410346-expressionwithformat)

|  | Declaration |
| --- | --- |
| From | ``` init(format expressionFormat: String, arguments argList: CVaListPointer) -> NSExpression ``` |
| To | ``` init(format expressionFormat: String, arguments argList: CVaListPointer) ``` |

Modified [NSExpression.init(forMinusSet: NSExpression, with: NSExpression)](https://developer.apple.com/documentation/foundation/nsexpression/1417659-expressionforminusset)

|  | Declaration |
| --- | --- |
| From | ``` init(forMinusSet left: NSExpression, with right: NSExpression) -> NSExpression ``` |
| To | ``` init(forMinusSet left: NSExpression, with right: NSExpression) ``` |

Modified [NSExpression.init(forSubquery: NSExpression, usingIteratorVariable: String, predicate: AnyObject)](https://developer.apple.com/documentation/foundation/nsexpression/1411651-expressionforsubquery)

|  | Declaration |
| --- | --- |
| From | ``` init(forSubquery expression: NSExpression, usingIteratorVariable variable: String, predicate predicate: AnyObject) -> NSExpression ``` |
| To | ``` init(forSubquery expression: NSExpression, usingIteratorVariable variable: String, predicate predicate: AnyObject) ``` |

Modified [NSExpression.init(forUnionSet: NSExpression, with: NSExpression)](https://developer.apple.com/documentation/foundation/nsexpression/1411585-expressionforunionset)

|  | Declaration |
| --- | --- |
| From | ``` init(forUnionSet left: NSExpression, with right: NSExpression) -> NSExpression ``` |
| To | ``` init(forUnionSet left: NSExpression, with right: NSExpression) ``` |

Modified [NSExpression.init(forVariable: String)](https://developer.apple.com/documentation/foundation/nsexpression/1417593-expressionforvariable)

|  | Declaration |
| --- | --- |
| From | ``` init(forVariable string: String) -> NSExpression ``` |
| To | ``` init(forVariable string: String) ``` |

Modified [NSExpressionType [enum]](https://developer.apple.com/documentation/foundation/nsexpressiontype)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum NSExpressionType : UInt {     case ConstantValueExpressionType     case EvaluatedObjectExpressionType     case VariableExpressionType     case KeyPathExpressionType     case FunctionExpressionType     case UnionSetExpressionType     case IntersectSetExpressionType     case MinusSetExpressionType     case SubqueryExpressionType     case AggregateExpressionType     case AnyKeyExpressionType     case BlockExpressionType } ``` | -- |
| To | ``` enum NSExpressionType : UInt {     case ConstantValueExpressionType     case EvaluatedObjectExpressionType     case VariableExpressionType     case KeyPathExpressionType     case FunctionExpressionType     case UnionSetExpressionType     case IntersectSetExpressionType     case MinusSetExpressionType     case SubqueryExpressionType     case AggregateExpressionType     case AnyKeyExpressionType     case BlockExpressionType     case ConditionalExpressionType } ``` | UInt |

Modified NSFastGenerator

|  | Declaration |
| --- | --- |
| From | ``` final class NSFastGenerator : GeneratorType {     var enumerable: NSFastEnumeration     var state: [NSFastEnumerationState]     var n: Int     var count: Int     var STACK_BUF_SIZE: Int { get }     struct ObjectsBuffer {         var buf: (COpaquePointer, COpaquePointer, COpaquePointer, COpaquePointer)     }     var objects: [NSFastGenerator.ObjectsBuffer]     func next() -> AnyObject?     func refresh()     init(_ enumerable: NSFastEnumeration) } ``` |
| To | ``` final class NSFastGenerator : GeneratorType {     func next() -> AnyObject?     init(_ enumerable: NSFastEnumeration) } ``` |

Modified [NSFileCoordinator](https://developer.apple.com/documentation/foundation/nsfilecoordinator)

|  | Declaration |
| --- | --- |
| From | ``` class NSFileCoordinator : NSObject {     class func addFilePresenter(_ filePresenter: NSFilePresenter)     class func removeFilePresenter(_ filePresenter: NSFilePresenter)     class func filePresenters() -> [AnyObject]     init(filePresenter filePresenterOrNil: NSFilePresenter?)     var purposeIdentifier: String     func coordinateAccessWithIntents(_ intents: [AnyObject], queue queue: NSOperationQueue, byAccessor accessor: (NSError!) -> Void)     func coordinateReadingItemAtURL(_ url: NSURL, options options: NSFileCoordinatorReadingOptions, error outError: NSErrorPointer, byAccessor reader: (NSURL!) -> Void)     func coordinateWritingItemAtURL(_ url: NSURL, options options: NSFileCoordinatorWritingOptions, error outError: NSErrorPointer, byAccessor writer: (NSURL!) -> Void)     func coordinateReadingItemAtURL(_ readingURL: NSURL, options readingOptions: NSFileCoordinatorReadingOptions, writingItemAtURL writingURL: NSURL, options writingOptions: NSFileCoordinatorWritingOptions, error outError: NSErrorPointer, byAccessor readerWriter: (NSURL!, NSURL!) -> Void)     func coordinateWritingItemAtURL(_ url1: NSURL, options options1: NSFileCoordinatorWritingOptions, writingItemAtURL url2: NSURL, options options2: NSFileCoordinatorWritingOptions, error outError: NSErrorPointer, byAccessor writer: (NSURL!, NSURL!) -> Void)     func prepareForReadingItemsAtURLs(_ readingURLs: [AnyObject], options readingOptions: NSFileCoordinatorReadingOptions, writingItemsAtURLs writingURLs: [AnyObject], options writingOptions: NSFileCoordinatorWritingOptions, error outError: NSErrorPointer, byAccessor batchAccessor: ((() -> Void)!) -> Void)     func itemAtURL(_ oldURL: NSURL, willMoveToURL newURL: NSURL)     func itemAtURL(_ oldURL: NSURL, didMoveToURL newURL: NSURL)     func cancel() } ``` |
| To | ``` class NSFileCoordinator : NSObject {     class func addFilePresenter(_ filePresenter: NSFilePresenter)     class func removeFilePresenter(_ filePresenter: NSFilePresenter)     class func filePresenters() -> [NSFilePresenter]     init(filePresenter filePresenterOrNil: NSFilePresenter?)     var purposeIdentifier: String     func coordinateAccessWithIntents(_ intents: [NSFileAccessIntent], queue queue: NSOperationQueue, byAccessor accessor: (NSError?) -> Void)     func coordinateReadingItemAtURL(_ url: NSURL, options options: NSFileCoordinatorReadingOptions, error outError: NSErrorPointer, byAccessor reader: (NSURL) -> Void)     func coordinateWritingItemAtURL(_ url: NSURL, options options: NSFileCoordinatorWritingOptions, error outError: NSErrorPointer, byAccessor writer: (NSURL) -> Void)     func coordinateReadingItemAtURL(_ readingURL: NSURL, options readingOptions: NSFileCoordinatorReadingOptions, writingItemAtURL writingURL: NSURL, options writingOptions: NSFileCoordinatorWritingOptions, error outError: NSErrorPointer, byAccessor readerWriter: (NSURL, NSURL) -> Void)     func coordinateWritingItemAtURL(_ url1: NSURL, options options1: NSFileCoordinatorWritingOptions, writingItemAtURL url2: NSURL, options options2: NSFileCoordinatorWritingOptions, error outError: NSErrorPointer, byAccessor writer: (NSURL, NSURL) -> Void)     func prepareForReadingItemsAtURLs(_ readingURLs: [NSURL], options readingOptions: NSFileCoordinatorReadingOptions, writingItemsAtURLs writingURLs: [NSURL], options writingOptions: NSFileCoordinatorWritingOptions, error outError: NSErrorPointer, byAccessor batchAccessor: (() -> Void) -> Void)     func itemAtURL(_ oldURL: NSURL, willMoveToURL newURL: NSURL)     func itemAtURL(_ oldURL: NSURL, didMoveToURL newURL: NSURL)     func cancel() } ``` |

Modified [NSFileCoordinator.coordinateAccessWithIntents(_: [NSFileAccessIntent], queue: NSOperationQueue, byAccessor: (NSError?) -> Void)](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1411533-coordinateaccesswithintents)

|  | Declaration |
| --- | --- |
| From | ``` func coordinateAccessWithIntents(_ intents: [AnyObject], queue queue: NSOperationQueue, byAccessor accessor: (NSError!) -> Void) ``` |
| To | ``` func coordinateAccessWithIntents(_ intents: [NSFileAccessIntent], queue queue: NSOperationQueue, byAccessor accessor: (NSError?) -> Void) ``` |

Modified [NSFileCoordinator.coordinateReadingItemAtURL(_: NSURL, options: NSFileCoordinatorReadingOptions, error: NSErrorPointer, byAccessor: (NSURL) -> Void)](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1407416-coordinate)

|  | Declaration |
| --- | --- |
| From | ``` func coordinateReadingItemAtURL(_ url: NSURL, options options: NSFileCoordinatorReadingOptions, error outError: NSErrorPointer, byAccessor reader: (NSURL!) -> Void) ``` |
| To | ``` func coordinateReadingItemAtURL(_ url: NSURL, options options: NSFileCoordinatorReadingOptions, error outError: NSErrorPointer, byAccessor reader: (NSURL) -> Void) ``` |

Modified [NSFileCoordinator.coordinateReadingItemAtURL(_: NSURL, options: NSFileCoordinatorReadingOptions, writingItemAtURL: NSURL, options: NSFileCoordinatorWritingOptions, error: NSErrorPointer, byAccessor: (NSURL, NSURL) -> Void)](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1413385-coordinatereadingitematurl)

|  | Declaration |
| --- | --- |
| From | ``` func coordinateReadingItemAtURL(_ readingURL: NSURL, options readingOptions: NSFileCoordinatorReadingOptions, writingItemAtURL writingURL: NSURL, options writingOptions: NSFileCoordinatorWritingOptions, error outError: NSErrorPointer, byAccessor readerWriter: (NSURL!, NSURL!) -> Void) ``` |
| To | ``` func coordinateReadingItemAtURL(_ readingURL: NSURL, options readingOptions: NSFileCoordinatorReadingOptions, writingItemAtURL writingURL: NSURL, options writingOptions: NSFileCoordinatorWritingOptions, error outError: NSErrorPointer, byAccessor readerWriter: (NSURL, NSURL) -> Void) ``` |

Modified [NSFileCoordinator.coordinateWritingItemAtURL(_: NSURL, options: NSFileCoordinatorWritingOptions, error: NSErrorPointer, byAccessor: (NSURL) -> Void)](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1413344-coordinatewritingitematurl)

|  | Declaration |
| --- | --- |
| From | ``` func coordinateWritingItemAtURL(_ url: NSURL, options options: NSFileCoordinatorWritingOptions, error outError: NSErrorPointer, byAccessor writer: (NSURL!) -> Void) ``` |
| To | ``` func coordinateWritingItemAtURL(_ url: NSURL, options options: NSFileCoordinatorWritingOptions, error outError: NSErrorPointer, byAccessor writer: (NSURL) -> Void) ``` |

Modified [NSFileCoordinator.coordinateWritingItemAtURL(_: NSURL, options: NSFileCoordinatorWritingOptions, writingItemAtURL: NSURL, options: NSFileCoordinatorWritingOptions, error: NSErrorPointer, byAccessor: (NSURL, NSURL) -> Void)](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1408970-coordinatewritingitematurl)

|  | Declaration |
| --- | --- |
| From | ``` func coordinateWritingItemAtURL(_ url1: NSURL, options options1: NSFileCoordinatorWritingOptions, writingItemAtURL url2: NSURL, options options2: NSFileCoordinatorWritingOptions, error outError: NSErrorPointer, byAccessor writer: (NSURL!, NSURL!) -> Void) ``` |
| To | ``` func coordinateWritingItemAtURL(_ url1: NSURL, options options1: NSFileCoordinatorWritingOptions, writingItemAtURL url2: NSURL, options options2: NSFileCoordinatorWritingOptions, error outError: NSErrorPointer, byAccessor writer: (NSURL, NSURL) -> Void) ``` |

Modified [NSFileCoordinator.filePresenters() -> [NSFilePresenter] [class]](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1407685-filepresenters)

|  | Declaration |
| --- | --- |
| From | ``` class func filePresenters() -> [AnyObject] ``` |
| To | ``` class func filePresenters() -> [NSFilePresenter] ``` |

Modified [NSFileCoordinator.prepareForReadingItemsAtURLs(_: [NSURL], options: NSFileCoordinatorReadingOptions, writingItemsAtURLs: [NSURL], options: NSFileCoordinatorWritingOptions, error: NSErrorPointer, byAccessor: (() -> Void) -> Void)](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1412420-prepareforreadingitemsaturls)

|  | Declaration |
| --- | --- |
| From | ``` func prepareForReadingItemsAtURLs(_ readingURLs: [AnyObject], options readingOptions: NSFileCoordinatorReadingOptions, writingItemsAtURLs writingURLs: [AnyObject], options writingOptions: NSFileCoordinatorWritingOptions, error outError: NSErrorPointer, byAccessor batchAccessor: ((() -> Void)!) -> Void) ``` |
| To | ``` func prepareForReadingItemsAtURLs(_ readingURLs: [NSURL], options readingOptions: NSFileCoordinatorReadingOptions, writingItemsAtURLs writingURLs: [NSURL], options writingOptions: NSFileCoordinatorWritingOptions, error outError: NSErrorPointer, byAccessor batchAccessor: (() -> Void) -> Void) ``` |

Modified [NSFileCoordinatorReadingOptions [struct]](https://developer.apple.com/documentation/foundation/nsfilecoordinatorreadingoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSFileCoordinatorReadingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var WithoutChanges: NSFileCoordinatorReadingOptions { get }     static var ResolvesSymbolicLink: NSFileCoordinatorReadingOptions { get }     static var ImmediatelyAvailableMetadataOnly: NSFileCoordinatorReadingOptions { get }     static var ForUploading: NSFileCoordinatorReadingOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSFileCoordinatorReadingOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var WithoutChanges: NSFileCoordinatorReadingOptions { get }     static var ResolvesSymbolicLink: NSFileCoordinatorReadingOptions { get }     static var ImmediatelyAvailableMetadataOnly: NSFileCoordinatorReadingOptions { get }     static var ForUploading: NSFileCoordinatorReadingOptions { get } } ``` | OptionSetType |

Modified [NSFileCoordinatorWritingOptions [struct]](https://developer.apple.com/documentation/foundation/nsfilecoordinatorwritingoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSFileCoordinatorWritingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var ForDeleting: NSFileCoordinatorWritingOptions { get }     static var ForMoving: NSFileCoordinatorWritingOptions { get }     static var ForMerging: NSFileCoordinatorWritingOptions { get }     static var ForReplacing: NSFileCoordinatorWritingOptions { get }     static var ContentIndependentMetadataOnly: NSFileCoordinatorWritingOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSFileCoordinatorWritingOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var ForDeleting: NSFileCoordinatorWritingOptions { get }     static var ForMoving: NSFileCoordinatorWritingOptions { get }     static var ForMerging: NSFileCoordinatorWritingOptions { get }     static var ForReplacing: NSFileCoordinatorWritingOptions { get }     static var ContentIndependentMetadataOnly: NSFileCoordinatorWritingOptions { get } } ``` | OptionSetType |

Modified [NSFileHandle](https://developer.apple.com/documentation/foundation/filehandle)

|  | Declaration |
| --- | --- |
| From | ``` class NSFileHandle : NSObject, NSSecureCoding, NSCoding {     @NSCopying var availableData: NSData { get }     func readDataToEndOfFile() -> NSData     func readDataOfLength(_ length: Int) -> NSData     func writeData(_ data: NSData)     var offsetInFile: UInt64 { get }     func seekToEndOfFile() -> UInt64     func seekToFileOffset(_ offset: UInt64)     func truncateFileAtOffset(_ offset: UInt64)     func synchronizeFile()     func closeFile()     init(fileDescriptor fd: Int32, closeOnDealloc closeopt: Bool)     init?(coder coder: NSCoder) } extension NSFileHandle {     class func fileHandleWithStandardInput() -> NSFileHandle     class func fileHandleWithStandardOutput() -> NSFileHandle     class func fileHandleWithStandardError() -> NSFileHandle     class func fileHandleWithNullDevice() -> NSFileHandle     convenience init?(forReadingAtPath path: String)     class func fileHandleForReadingAtPath(_ path: String) -> Self?     convenience init?(forWritingAtPath path: String)     class func fileHandleForWritingAtPath(_ path: String) -> Self?     convenience init?(forUpdatingAtPath path: String)     class func fileHandleForUpdatingAtPath(_ path: String) -> Self?     convenience init?(forReadingFromURL url: NSURL, error error: NSErrorPointer)     class func fileHandleForReadingFromURL(_ url: NSURL, error error: NSErrorPointer) -> Self?     convenience init?(forWritingToURL url: NSURL, error error: NSErrorPointer)     class func fileHandleForWritingToURL(_ url: NSURL, error error: NSErrorPointer) -> Self?     convenience init?(forUpdatingURL url: NSURL, error error: NSErrorPointer)     class func fileHandleForUpdatingURL(_ url: NSURL, error error: NSErrorPointer) -> Self? } extension NSFileHandle {     func readInBackgroundAndNotifyForModes(_ modes: [AnyObject])     func readInBackgroundAndNotify()     func readToEndOfFileInBackgroundAndNotifyForModes(_ modes: [AnyObject])     func readToEndOfFileInBackgroundAndNotify()     func acceptConnectionInBackgroundAndNotifyForModes(_ modes: [AnyObject])     func acceptConnectionInBackgroundAndNotify()     func waitForDataInBackgroundAndNotifyForModes(_ modes: [AnyObject])     func waitForDataInBackgroundAndNotify()     var readabilityHandler: ((NSFileHandle!) -> Void)?     var writeabilityHandler: ((NSFileHandle!) -> Void)? } extension NSFileHandle {     convenience init(fileDescriptor fd: Int32)     var fileDescriptor: Int32 { get } } ``` |
| To | ``` class NSFileHandle : NSObject, NSSecureCoding, NSCoding {     @NSCopying var availableData: NSData { get }     func readDataToEndOfFile() -> NSData     func readDataOfLength(_ length: Int) -> NSData     func writeData(_ data: NSData)     var offsetInFile: UInt64 { get }     func seekToEndOfFile() -> UInt64     func seekToFileOffset(_ offset: UInt64)     func truncateFileAtOffset(_ offset: UInt64)     func synchronizeFile()     func closeFile()     init(fileDescriptor fd: Int32, closeOnDealloc closeopt: Bool)     init?(coder coder: NSCoder) } extension NSFileHandle {     class func fileHandleWithStandardInput() -> NSFileHandle     class func fileHandleWithStandardOutput() -> NSFileHandle     class func fileHandleWithStandardError() -> NSFileHandle     class func fileHandleWithNullDevice() -> NSFileHandle     convenience init?(forReadingAtPath path: String)     class func fileHandleForReadingAtPath(_ path: String) -> Self?     convenience init?(forWritingAtPath path: String)     class func fileHandleForWritingAtPath(_ path: String) -> Self?     convenience init?(forUpdatingAtPath path: String)     class func fileHandleForUpdatingAtPath(_ path: String) -> Self?     convenience init(forReadingFromURL url: NSURL) throws     class func fileHandleForReadingFromURL(_ url: NSURL) throws -> Self     convenience init(forWritingToURL url: NSURL) throws     class func fileHandleForWritingToURL(_ url: NSURL) throws -> Self     convenience init(forUpdatingURL url: NSURL) throws     class func fileHandleForUpdatingURL(_ url: NSURL) throws -> Self } extension NSFileHandle {     func readInBackgroundAndNotifyForModes(_ modes: [String]?)     func readInBackgroundAndNotify()     func readToEndOfFileInBackgroundAndNotifyForModes(_ modes: [String]?)     func readToEndOfFileInBackgroundAndNotify()     func acceptConnectionInBackgroundAndNotifyForModes(_ modes: [String]?)     func acceptConnectionInBackgroundAndNotify()     func waitForDataInBackgroundAndNotifyForModes(_ modes: [String]?)     func waitForDataInBackgroundAndNotify()     var readabilityHandler: ((NSFileHandle) -> Void)?     var writeabilityHandler: ((NSFileHandle) -> Void)? } extension NSFileHandle {     convenience init(fileDescriptor fd: Int32)     var fileDescriptor: Int32 { get } } ``` |

Modified [NSFileHandle.acceptConnectionInBackgroundAndNotifyForModes(_: [String]?)](https://developer.apple.com/documentation/foundation/filehandle/1412997-acceptconnectioninbackgroundandn)

|  | Declaration |
| --- | --- |
| From | ``` func acceptConnectionInBackgroundAndNotifyForModes(_ modes: [AnyObject]) ``` |
| To | ``` func acceptConnectionInBackgroundAndNotifyForModes(_ modes: [String]?) ``` |

Modified [NSFileHandle.init(forReadingFromURL: NSURL) throws](https://developer.apple.com/documentation/foundation/filehandle/1408422-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init?(forReadingFromURL url: NSURL, error error: NSErrorPointer) ``` |
| To | ``` convenience init(forReadingFromURL url: NSURL) throws ``` |

Modified [NSFileHandle.init(forUpdatingURL: NSURL) throws](https://developer.apple.com/documentation/foundation/filehandle/1417026-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init?(forUpdatingURL url: NSURL, error error: NSErrorPointer) ``` |
| To | ``` convenience init(forUpdatingURL url: NSURL) throws ``` |

Modified [NSFileHandle.init(forWritingToURL: NSURL) throws](https://developer.apple.com/documentation/foundation/nsfilehandle/1416892-filehandleforwritingtourl)

|  | Declaration |
| --- | --- |
| From | ``` convenience init?(forWritingToURL url: NSURL, error error: NSErrorPointer) ``` |
| To | ``` convenience init(forWritingToURL url: NSURL) throws ``` |

Modified [NSFileHandle.readabilityHandler](https://developer.apple.com/documentation/foundation/nsfilehandle/1412413-readabilityhandler)

|  | Declaration |
| --- | --- |
| From | ``` var readabilityHandler: ((NSFileHandle!) -> Void)? ``` |
| To | ``` var readabilityHandler: ((NSFileHandle) -> Void)? ``` |

Modified [NSFileHandle.readInBackgroundAndNotifyForModes(_: [String]?)](https://developer.apple.com/documentation/foundation/nsfilehandle/1416294-readinbackgroundandnotifyformode)

|  | Declaration |
| --- | --- |
| From | ``` func readInBackgroundAndNotifyForModes(_ modes: [AnyObject]) ``` |
| To | ``` func readInBackgroundAndNotifyForModes(_ modes: [String]?) ``` |

Modified [NSFileHandle.readToEndOfFileInBackgroundAndNotifyForModes(_: [String]?)](https://developer.apple.com/documentation/foundation/nsfilehandle/1417321-readtoendoffileinbackgroundandno)

|  | Declaration |
| --- | --- |
| From | ``` func readToEndOfFileInBackgroundAndNotifyForModes(_ modes: [AnyObject]) ``` |
| To | ``` func readToEndOfFileInBackgroundAndNotifyForModes(_ modes: [String]?) ``` |

Modified [NSFileHandle.waitForDataInBackgroundAndNotifyForModes(_: [String]?)](https://developer.apple.com/documentation/foundation/filehandle/1414643-waitfordatainbackgroundandnotify)

|  | Declaration |
| --- | --- |
| From | ``` func waitForDataInBackgroundAndNotifyForModes(_ modes: [AnyObject]) ``` |
| To | ``` func waitForDataInBackgroundAndNotifyForModes(_ modes: [String]?) ``` |

Modified [NSFileHandle.writeabilityHandler](https://developer.apple.com/documentation/foundation/filehandle/1415367-writeabilityhandler)

|  | Declaration |
| --- | --- |
| From | ``` var writeabilityHandler: ((NSFileHandle!) -> Void)? ``` |
| To | ``` var writeabilityHandler: ((NSFileHandle) -> Void)? ``` |

Modified [NSFileManager](https://developer.apple.com/documentation/foundation/filemanager)

|  | Declaration |
| --- | --- |
| From | ``` class NSFileManager : NSObject {     class func defaultManager() -> NSFileManager     func mountedVolumeURLsIncludingResourceValuesForKeys(_ propertyKeys: [AnyObject]?, options options: NSVolumeEnumerationOptions) -> [AnyObject]?     func contentsOfDirectoryAtURL(_ url: NSURL, includingPropertiesForKeys keys: [AnyObject]?, options mask: NSDirectoryEnumerationOptions, error error: NSErrorPointer) -> [AnyObject]?     func URLsForDirectory(_ directory: NSSearchPathDirectory, inDomains domainMask: NSSearchPathDomainMask) -> [AnyObject]     func URLForDirectory(_ directory: NSSearchPathDirectory, inDomain domain: NSSearchPathDomainMask, appropriateForURL url: NSURL?, create shouldCreate: Bool, error error: NSErrorPointer) -> NSURL?     func getRelationship(_ outRelationship: UnsafeMutablePointer<NSURLRelationship>, ofDirectoryAtURL directoryURL: NSURL, toItemAtURL otherURL: NSURL, error error: NSErrorPointer) -> Bool     func getRelationship(_ outRelationship: UnsafeMutablePointer<NSURLRelationship>, ofDirectory directory: NSSearchPathDirectory, inDomain domainMask: NSSearchPathDomainMask, toItemAtURL url: NSURL, error error: NSErrorPointer) -> Bool     func createDirectoryAtURL(_ url: NSURL, withIntermediateDirectories createIntermediates: Bool, attributes attributes: [NSObject : AnyObject]?, error error: NSErrorPointer) -> Bool     func createSymbolicLinkAtURL(_ url: NSURL, withDestinationURL destURL: NSURL, error error: NSErrorPointer) -> Bool     unowned(unsafe) var delegate: NSFileManagerDelegate?     func setAttributes(_ attributes: [NSObject : AnyObject], ofItemAtPath path: String, error error: NSErrorPointer) -> Bool     func createDirectoryAtPath(_ path: String, withIntermediateDirectories createIntermediates: Bool, attributes attributes: [NSObject : AnyObject]?, error error: NSErrorPointer) -> Bool     func contentsOfDirectoryAtPath(_ path: String, error error: NSErrorPointer) -> [AnyObject]?     func subpathsOfDirectoryAtPath(_ path: String, error error: NSErrorPointer) -> [AnyObject]?     func attributesOfItemAtPath(_ path: String, error error: NSErrorPointer) -> [NSObject : AnyObject]?     func attributesOfFileSystemForPath(_ path: String, error error: NSErrorPointer) -> [NSObject : AnyObject]?     func createSymbolicLinkAtPath(_ path: String, withDestinationPath destPath: String, error error: NSErrorPointer) -> Bool     func destinationOfSymbolicLinkAtPath(_ path: String, error error: NSErrorPointer) -> String?     func copyItemAtPath(_ srcPath: String, toPath dstPath: String, error error: NSErrorPointer) -> Bool     func moveItemAtPath(_ srcPath: String, toPath dstPath: String, error error: NSErrorPointer) -> Bool     func linkItemAtPath(_ srcPath: String, toPath dstPath: String, error error: NSErrorPointer) -> Bool     func removeItemAtPath(_ path: String, error error: NSErrorPointer) -> Bool     func copyItemAtURL(_ srcURL: NSURL, toURL dstURL: NSURL, error error: NSErrorPointer) -> Bool     func moveItemAtURL(_ srcURL: NSURL, toURL dstURL: NSURL, error error: NSErrorPointer) -> Bool     func linkItemAtURL(_ srcURL: NSURL, toURL dstURL: NSURL, error error: NSErrorPointer) -> Bool     func removeItemAtURL(_ URL: NSURL, error error: NSErrorPointer) -> Bool     func trashItemAtURL(_ url: NSURL, resultingItemURL outResultingURL: AutoreleasingUnsafeMutablePointer<NSURL?>, error error: NSErrorPointer) -> Bool     func fileAttributesAtPath(_ path: String!, traverseLink yorn: Bool) -> [NSObject : AnyObject]!     func changeFileAttributes(_ attributes: [NSObject : AnyObject]!, atPath path: String!) -> Bool     func directoryContentsAtPath(_ path: String!) -> [AnyObject]!     func fileSystemAttributesAtPath(_ path: String!) -> [NSObject : AnyObject]!     func pathContentOfSymbolicLinkAtPath(_ path: String!) -> String!     func createSymbolicLinkAtPath(_ path: String!, pathContent otherpath: String!) -> Bool     func createDirectoryAtPath(_ path: String!, attributes attributes: [NSObject : AnyObject]!) -> Bool     var currentDirectoryPath: String { get }     func changeCurrentDirectoryPath(_ path: String) -> Bool     func fileExistsAtPath(_ path: String) -> Bool     func fileExistsAtPath(_ path: String, isDirectory isDirectory: UnsafeMutablePointer<ObjCBool>) -> Bool     func isReadableFileAtPath(_ path: String) -> Bool     func isWritableFileAtPath(_ path: String) -> Bool     func isExecutableFileAtPath(_ path: String) -> Bool     func isDeletableFileAtPath(_ path: String) -> Bool     func contentsEqualAtPath(_ path1: String, andPath path2: String) -> Bool     func displayNameAtPath(_ path: String) -> String     func componentsToDisplayForPath(_ path: String) -> [AnyObject]?     func enumeratorAtPath(_ path: String) -> NSDirectoryEnumerator?     func enumeratorAtURL(_ url: NSURL, includingPropertiesForKeys keys: [AnyObject]?, options mask: NSDirectoryEnumerationOptions, errorHandler handler: ((NSURL!, NSError!) -> Bool)?) -> NSDirectoryEnumerator?     func subpathsAtPath(_ path: String) -> [AnyObject]?     func contentsAtPath(_ path: String) -> NSData?     func createFileAtPath(_ path: String, contents data: NSData?, attributes attr: [NSObject : AnyObject]?) -> Bool     func fileSystemRepresentationWithPath(_ path: String) -> UnsafePointer<Int8>     func stringWithFileSystemRepresentation(_ str: UnsafePointer<Int8>, length len: Int) -> String     func replaceItemAtURL(_ originalItemURL: NSURL, withItemAtURL newItemURL: NSURL, backupItemName backupItemName: String?, options options: NSFileManagerItemReplacementOptions, resultingItemURL resultingURL: AutoreleasingUnsafeMutablePointer<NSURL?>, error error: NSErrorPointer) -> Bool     func setUbiquitous(_ flag: Bool, itemAtURL url: NSURL, destinationURL destinationURL: NSURL, error error: NSErrorPointer) -> Bool     func isUbiquitousItemAtURL(_ url: NSURL) -> Bool     func startDownloadingUbiquitousItemAtURL(_ url: NSURL, error error: NSErrorPointer) -> Bool     func evictUbiquitousItemAtURL(_ url: NSURL, error error: NSErrorPointer) -> Bool     func URLForUbiquityContainerIdentifier(_ containerIdentifier: String?) -> NSURL?     func URLForPublishingUbiquitousItemAtURL(_ url: NSURL, expirationDate outDate: AutoreleasingUnsafeMutablePointer<NSDate?>, error error: NSErrorPointer) -> NSURL?     @NSCopying var ubiquityIdentityToken: protocol<NSCoding, NSCopying, NSObjectProtocol>? { get }     func containerURLForSecurityApplicationGroupIdentifier(_ groupIdentifier: String) -> NSURL? } ``` |
| To | ``` class NSFileManager : NSObject {     class func defaultManager() -> NSFileManager     func mountedVolumeURLsIncludingResourceValuesForKeys(_ propertyKeys: [String]?, options options: NSVolumeEnumerationOptions) -> [NSURL]?     func unmountVolumeAtURL(_ url: NSURL, options mask: NSFileManagerUnmountOptions, completionHandler completionHandler: (NSError?) -> Void)     func contentsOfDirectoryAtURL(_ url: NSURL, includingPropertiesForKeys keys: [String]?, options mask: NSDirectoryEnumerationOptions) throws -> [NSURL]     func URLsForDirectory(_ directory: NSSearchPathDirectory, inDomains domainMask: NSSearchPathDomainMask) -> [NSURL]     func URLForDirectory(_ directory: NSSearchPathDirectory, inDomain domain: NSSearchPathDomainMask, appropriateForURL url: NSURL?, create shouldCreate: Bool) throws -> NSURL     func getRelationship(_ outRelationship: UnsafeMutablePointer<NSURLRelationship>, ofDirectoryAtURL directoryURL: NSURL, toItemAtURL otherURL: NSURL) throws     func getRelationship(_ outRelationship: UnsafeMutablePointer<NSURLRelationship>, ofDirectory directory: NSSearchPathDirectory, inDomain domainMask: NSSearchPathDomainMask, toItemAtURL url: NSURL) throws     func createDirectoryAtURL(_ url: NSURL, withIntermediateDirectories createIntermediates: Bool, attributes attributes: [String : AnyObject]?) throws     func createSymbolicLinkAtURL(_ url: NSURL, withDestinationURL destURL: NSURL) throws     unowned(unsafe) var delegate: NSFileManagerDelegate?     func setAttributes(_ attributes: [String : AnyObject], ofItemAtPath path: String) throws     func createDirectoryAtPath(_ path: String, withIntermediateDirectories createIntermediates: Bool, attributes attributes: [String : AnyObject]?) throws     func contentsOfDirectoryAtPath(_ path: String) throws -> [String]     func subpathsOfDirectoryAtPath(_ path: String) throws -> [String]     func attributesOfItemAtPath(_ path: String) throws -> [String : AnyObject]     func attributesOfFileSystemForPath(_ path: String) throws -> [String : AnyObject]     func createSymbolicLinkAtPath(_ path: String, withDestinationPath destPath: String) throws     func destinationOfSymbolicLinkAtPath(_ path: String) throws -> String     func copyItemAtPath(_ srcPath: String, toPath dstPath: String) throws     func moveItemAtPath(_ srcPath: String, toPath dstPath: String) throws     func linkItemAtPath(_ srcPath: String, toPath dstPath: String) throws     func removeItemAtPath(_ path: String) throws     func copyItemAtURL(_ srcURL: NSURL, toURL dstURL: NSURL) throws     func moveItemAtURL(_ srcURL: NSURL, toURL dstURL: NSURL) throws     func linkItemAtURL(_ srcURL: NSURL, toURL dstURL: NSURL) throws     func removeItemAtURL(_ URL: NSURL) throws     func trashItemAtURL(_ url: NSURL, resultingItemURL outResultingURL: AutoreleasingUnsafeMutablePointer<NSURL?>) throws     func fileAttributesAtPath(_ path: String, traverseLink yorn: Bool) -> [NSObject : AnyObject]?     func changeFileAttributes(_ attributes: [NSObject : AnyObject], atPath path: String) -> Bool     func directoryContentsAtPath(_ path: String) -> [AnyObject]?     func fileSystemAttributesAtPath(_ path: String) -> [NSObject : AnyObject]?     func pathContentOfSymbolicLinkAtPath(_ path: String) -> String?     func createSymbolicLinkAtPath(_ path: String, pathContent otherpath: String) -> Bool     func createDirectoryAtPath(_ path: String, attributes attributes: [NSObject : AnyObject]) -> Bool     var currentDirectoryPath: String { get }     func changeCurrentDirectoryPath(_ path: String) -> Bool     func fileExistsAtPath(_ path: String) -> Bool     func fileExistsAtPath(_ path: String, isDirectory isDirectory: UnsafeMutablePointer<ObjCBool>) -> Bool     func isReadableFileAtPath(_ path: String) -> Bool     func isWritableFileAtPath(_ path: String) -> Bool     func isExecutableFileAtPath(_ path: String) -> Bool     func isDeletableFileAtPath(_ path: String) -> Bool     func contentsEqualAtPath(_ path1: String, andPath path2: String) -> Bool     func displayNameAtPath(_ path: String) -> String     func componentsToDisplayForPath(_ path: String) -> [String]?     func enumeratorAtPath(_ path: String) -> NSDirectoryEnumerator?     func enumeratorAtURL(_ url: NSURL, includingPropertiesForKeys keys: [String]?, options mask: NSDirectoryEnumerationOptions, errorHandler handler: ((NSURL, NSError) -> Bool)?) -> NSDirectoryEnumerator?     func subpathsAtPath(_ path: String) -> [String]?     func contentsAtPath(_ path: String) -> NSData?     func createFileAtPath(_ path: String, contents data: NSData?, attributes attr: [String : AnyObject]?) -> Bool     func fileSystemRepresentationWithPath(_ path: String) -> UnsafePointer<Int8>     func stringWithFileSystemRepresentation(_ str: UnsafePointer<Int8>, length len: Int) -> String     func replaceItemAtURL(_ originalItemURL: NSURL, withItemAtURL newItemURL: NSURL, backupItemName backupItemName: String?, options options: NSFileManagerItemReplacementOptions, resultingItemURL resultingURL: AutoreleasingUnsafeMutablePointer<NSURL?>) throws     func setUbiquitous(_ flag: Bool, itemAtURL url: NSURL, destinationURL destinationURL: NSURL) throws     func isUbiquitousItemAtURL(_ url: NSURL) -> Bool     func startDownloadingUbiquitousItemAtURL(_ url: NSURL) throws     func evictUbiquitousItemAtURL(_ url: NSURL) throws     func URLForUbiquityContainerIdentifier(_ containerIdentifier: String?) -> NSURL?     func URLForPublishingUbiquitousItemAtURL(_ url: NSURL, expirationDate outDate: AutoreleasingUnsafeMutablePointer<NSDate?>) throws -> NSURL     @NSCopying var ubiquityIdentityToken: protocol<NSCoding, NSCopying, NSObjectProtocol>? { get }     func containerURLForSecurityApplicationGroupIdentifier(_ groupIdentifier: String) -> NSURL? } ``` |

Modified [NSFileManager.attributesOfFileSystemForPath(_: String) throws -> [String : AnyObject]](https://developer.apple.com/documentation/foundation/filemanager/1411896-attributesoffilesystem)

|  | Declaration |
| --- | --- |
| From | ``` func attributesOfFileSystemForPath(_ path: String, error error: NSErrorPointer) -> [NSObject : AnyObject]? ``` |
| To | ``` func attributesOfFileSystemForPath(_ path: String) throws -> [String : AnyObject] ``` |

Modified [NSFileManager.attributesOfItemAtPath(_: String) throws -> [String : AnyObject]](https://developer.apple.com/documentation/foundation/filemanager/1410452-attributesofitem)

|  | Declaration |
| --- | --- |
| From | ``` func attributesOfItemAtPath(_ path: String, error error: NSErrorPointer) -> [NSObject : AnyObject]? ``` |
| To | ``` func attributesOfItemAtPath(_ path: String) throws -> [String : AnyObject] ``` |

Modified [NSFileManager.componentsToDisplayForPath(_: String) -> [String]?](https://developer.apple.com/documentation/foundation/filemanager/1413929-componentstodisplay)

|  | Declaration |
| --- | --- |
| From | ``` func componentsToDisplayForPath(_ path: String) -> [AnyObject]? ``` |
| To | ``` func componentsToDisplayForPath(_ path: String) -> [String]? ``` |

Modified [NSFileManager.contentsOfDirectoryAtPath(_: String) throws -> [String]](https://developer.apple.com/documentation/foundation/filemanager/1414584-contentsofdirectory)

|  | Declaration |
| --- | --- |
| From | ``` func contentsOfDirectoryAtPath(_ path: String, error error: NSErrorPointer) -> [AnyObject]? ``` |
| To | ``` func contentsOfDirectoryAtPath(_ path: String) throws -> [String] ``` |

Modified [NSFileManager.contentsOfDirectoryAtURL(_: NSURL, includingPropertiesForKeys: [String]?, options: NSDirectoryEnumerationOptions) throws -> [NSURL]](https://developer.apple.com/documentation/foundation/nsfilemanager/1413768-contentsofdirectoryaturl)

|  | Declaration |
| --- | --- |
| From | ``` func contentsOfDirectoryAtURL(_ url: NSURL, includingPropertiesForKeys keys: [AnyObject]?, options mask: NSDirectoryEnumerationOptions, error error: NSErrorPointer) -> [AnyObject]? ``` |
| To | ``` func contentsOfDirectoryAtURL(_ url: NSURL, includingPropertiesForKeys keys: [String]?, options mask: NSDirectoryEnumerationOptions) throws -> [NSURL] ``` |

Modified [NSFileManager.copyItemAtPath(_: String, toPath: String) throws](https://developer.apple.com/documentation/foundation/nsfilemanager/1407903-copyitematpath)

|  | Declaration |
| --- | --- |
| From | ``` func copyItemAtPath(_ srcPath: String, toPath dstPath: String, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func copyItemAtPath(_ srcPath: String, toPath dstPath: String) throws ``` |

Modified [NSFileManager.copyItemAtURL(_: NSURL, toURL: NSURL) throws](https://developer.apple.com/documentation/foundation/nsfilemanager/1412957-copyitematurl)

|  | Declaration |
| --- | --- |
| From | ``` func copyItemAtURL(_ srcURL: NSURL, toURL dstURL: NSURL, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func copyItemAtURL(_ srcURL: NSURL, toURL dstURL: NSURL) throws ``` |

Modified [NSFileManager.createDirectoryAtPath(_: String, withIntermediateDirectories: Bool, attributes: [String : AnyObject]?) throws](https://developer.apple.com/documentation/foundation/filemanager/1407884-createdirectory)

|  | Declaration |
| --- | --- |
| From | ``` func createDirectoryAtPath(_ path: String, withIntermediateDirectories createIntermediates: Bool, attributes attributes: [NSObject : AnyObject]?, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func createDirectoryAtPath(_ path: String, withIntermediateDirectories createIntermediates: Bool, attributes attributes: [String : AnyObject]?) throws ``` |

Modified [NSFileManager.createDirectoryAtURL(_: NSURL, withIntermediateDirectories: Bool, attributes: [String : AnyObject]?) throws](https://developer.apple.com/documentation/foundation/nsfilemanager/1415371-createdirectoryaturl)

|  | Declaration |
| --- | --- |
| From | ``` func createDirectoryAtURL(_ url: NSURL, withIntermediateDirectories createIntermediates: Bool, attributes attributes: [NSObject : AnyObject]?, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func createDirectoryAtURL(_ url: NSURL, withIntermediateDirectories createIntermediates: Bool, attributes attributes: [String : AnyObject]?) throws ``` |

Modified [NSFileManager.createFileAtPath(_: String, contents: NSData?, attributes: [String : AnyObject]?) -> Bool](https://developer.apple.com/documentation/foundation/filemanager/1410695-createfile)

|  | Declaration |
| --- | --- |
| From | ``` func createFileAtPath(_ path: String, contents data: NSData?, attributes attr: [NSObject : AnyObject]?) -> Bool ``` |
| To | ``` func createFileAtPath(_ path: String, contents data: NSData?, attributes attr: [String : AnyObject]?) -> Bool ``` |

Modified [NSFileManager.createSymbolicLinkAtPath(_: String, withDestinationPath: String) throws](https://developer.apple.com/documentation/foundation/filemanager/1411007-createsymboliclink)

|  | Declaration |
| --- | --- |
| From | ``` func createSymbolicLinkAtPath(_ path: String, withDestinationPath destPath: String, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func createSymbolicLinkAtPath(_ path: String, withDestinationPath destPath: String) throws ``` |

Modified [NSFileManager.createSymbolicLinkAtURL(_: NSURL, withDestinationURL: NSURL) throws](https://developer.apple.com/documentation/foundation/filemanager/1414652-createsymboliclink)

|  | Declaration |
| --- | --- |
| From | ``` func createSymbolicLinkAtURL(_ url: NSURL, withDestinationURL destURL: NSURL, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func createSymbolicLinkAtURL(_ url: NSURL, withDestinationURL destURL: NSURL) throws ``` |

Modified [NSFileManager.destinationOfSymbolicLinkAtPath(_: String) throws -> String](https://developer.apple.com/documentation/foundation/nsfilemanager/1415161-destinationofsymboliclinkatpath)

|  | Declaration |
| --- | --- |
| From | ``` func destinationOfSymbolicLinkAtPath(_ path: String, error error: NSErrorPointer) -> String? ``` |
| To | ``` func destinationOfSymbolicLinkAtPath(_ path: String) throws -> String ``` |

Modified [NSFileManager.enumeratorAtURL(_: NSURL, includingPropertiesForKeys: [String]?, options: NSDirectoryEnumerationOptions, errorHandler: ((NSURL, NSError) -> Bool)?) -> NSDirectoryEnumerator?](https://developer.apple.com/documentation/foundation/nsfilemanager/1409571-enumeratoraturl)

|  | Declaration |
| --- | --- |
| From | ``` func enumeratorAtURL(_ url: NSURL, includingPropertiesForKeys keys: [AnyObject]?, options mask: NSDirectoryEnumerationOptions, errorHandler handler: ((NSURL!, NSError!) -> Bool)?) -> NSDirectoryEnumerator? ``` |
| To | ``` func enumeratorAtURL(_ url: NSURL, includingPropertiesForKeys keys: [String]?, options mask: NSDirectoryEnumerationOptions, errorHandler handler: ((NSURL, NSError) -> Bool)?) -> NSDirectoryEnumerator? ``` |

Modified [NSFileManager.evictUbiquitousItemAtURL(_: NSURL) throws](https://developer.apple.com/documentation/foundation/nsfilemanager/1409696-evictubiquitousitematurl)

|  | Declaration |
| --- | --- |
| From | ``` func evictUbiquitousItemAtURL(_ url: NSURL, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func evictUbiquitousItemAtURL(_ url: NSURL) throws ``` |

Modified [NSFileManager.getRelationship(_: UnsafeMutablePointer<NSURLRelationship>, ofDirectory: NSSearchPathDirectory, inDomain: NSSearchPathDomainMask, toItemAtURL: NSURL) throws](https://developer.apple.com/documentation/foundation/nsfilemanager/1411439-getrelationship)

|  | Declaration |
| --- | --- |
| From | ``` func getRelationship(_ outRelationship: UnsafeMutablePointer<NSURLRelationship>, ofDirectory directory: NSSearchPathDirectory, inDomain domainMask: NSSearchPathDomainMask, toItemAtURL url: NSURL, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func getRelationship(_ outRelationship: UnsafeMutablePointer<NSURLRelationship>, ofDirectory directory: NSSearchPathDirectory, inDomain domainMask: NSSearchPathDomainMask, toItemAtURL url: NSURL) throws ``` |

Modified [NSFileManager.getRelationship(_: UnsafeMutablePointer<NSURLRelationship>, ofDirectoryAtURL: NSURL, toItemAtURL: NSURL) throws](https://developer.apple.com/documentation/foundation/filemanager/1407229-getrelationship)

|  | Declaration |
| --- | --- |
| From | ``` func getRelationship(_ outRelationship: UnsafeMutablePointer<NSURLRelationship>, ofDirectoryAtURL directoryURL: NSURL, toItemAtURL otherURL: NSURL, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func getRelationship(_ outRelationship: UnsafeMutablePointer<NSURLRelationship>, ofDirectoryAtURL directoryURL: NSURL, toItemAtURL otherURL: NSURL) throws ``` |

Modified [NSFileManager.linkItemAtPath(_: String, toPath: String) throws](https://developer.apple.com/documentation/foundation/nsfilemanager/1411206-linkitematpath)

|  | Declaration |
| --- | --- |
| From | ``` func linkItemAtPath(_ srcPath: String, toPath dstPath: String, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func linkItemAtPath(_ srcPath: String, toPath dstPath: String) throws ``` |

Modified [NSFileManager.linkItemAtURL(_: NSURL, toURL: NSURL) throws](https://developer.apple.com/documentation/foundation/filemanager/1414456-linkitem)

|  | Declaration |
| --- | --- |
| From | ``` func linkItemAtURL(_ srcURL: NSURL, toURL dstURL: NSURL, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func linkItemAtURL(_ srcURL: NSURL, toURL dstURL: NSURL) throws ``` |

Modified [NSFileManager.mountedVolumeURLsIncludingResourceValuesForKeys(_: [String]?, options: NSVolumeEnumerationOptions) -> [NSURL]?](https://developer.apple.com/documentation/foundation/nsfilemanager/1409626-mountedvolumeurlsincludingresour)

|  | Declaration |
| --- | --- |
| From | ``` func mountedVolumeURLsIncludingResourceValuesForKeys(_ propertyKeys: [AnyObject]?, options options: NSVolumeEnumerationOptions) -> [AnyObject]? ``` |
| To | ``` func mountedVolumeURLsIncludingResourceValuesForKeys(_ propertyKeys: [String]?, options options: NSVolumeEnumerationOptions) -> [NSURL]? ``` |

Modified [NSFileManager.moveItemAtPath(_: String, toPath: String) throws](https://developer.apple.com/documentation/foundation/nsfilemanager/1413529-moveitematpath)

|  | Declaration |
| --- | --- |
| From | ``` func moveItemAtPath(_ srcPath: String, toPath dstPath: String, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func moveItemAtPath(_ srcPath: String, toPath dstPath: String) throws ``` |

Modified [NSFileManager.moveItemAtURL(_: NSURL, toURL: NSURL) throws](https://developer.apple.com/documentation/foundation/nsfilemanager/1414750-moveitematurl)

|  | Declaration |
| --- | --- |
| From | ``` func moveItemAtURL(_ srcURL: NSURL, toURL dstURL: NSURL, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func moveItemAtURL(_ srcURL: NSURL, toURL dstURL: NSURL) throws ``` |

Modified [NSFileManager.removeItemAtPath(_: String) throws](https://developer.apple.com/documentation/foundation/filemanager/1408573-removeitem)

|  | Declaration |
| --- | --- |
| From | ``` func removeItemAtPath(_ path: String, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func removeItemAtPath(_ path: String) throws ``` |

Modified [NSFileManager.removeItemAtURL(_: NSURL) throws](https://developer.apple.com/documentation/foundation/filemanager/1413590-removeitem)

|  | Declaration |
| --- | --- |
| From | ``` func removeItemAtURL(_ URL: NSURL, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func removeItemAtURL(_ URL: NSURL) throws ``` |

Modified [NSFileManager.replaceItemAtURL(_: NSURL, withItemAtURL: NSURL, backupItemName: String?, options: NSFileManagerItemReplacementOptions, resultingItemURL: AutoreleasingUnsafeMutablePointer<NSURL?>) throws](https://developer.apple.com/documentation/foundation/nsfilemanager/1412432-replaceitematurl)

|  | Declaration |
| --- | --- |
| From | ``` func replaceItemAtURL(_ originalItemURL: NSURL, withItemAtURL newItemURL: NSURL, backupItemName backupItemName: String?, options options: NSFileManagerItemReplacementOptions, resultingItemURL resultingURL: AutoreleasingUnsafeMutablePointer<NSURL?>, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func replaceItemAtURL(_ originalItemURL: NSURL, withItemAtURL newItemURL: NSURL, backupItemName backupItemName: String?, options options: NSFileManagerItemReplacementOptions, resultingItemURL resultingURL: AutoreleasingUnsafeMutablePointer<NSURL?>) throws ``` |

Modified [NSFileManager.setAttributes(_: [String : AnyObject], ofItemAtPath: String) throws](https://developer.apple.com/documentation/foundation/filemanager/1413667-setattributes)

|  | Declaration |
| --- | --- |
| From | ``` func setAttributes(_ attributes: [NSObject : AnyObject], ofItemAtPath path: String, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func setAttributes(_ attributes: [String : AnyObject], ofItemAtPath path: String) throws ``` |

Modified [NSFileManager.setUbiquitous(_: Bool, itemAtURL: NSURL, destinationURL: NSURL) throws](https://developer.apple.com/documentation/foundation/filemanager/1413989-setubiquitous)

|  | Declaration |
| --- | --- |
| From | ``` func setUbiquitous(_ flag: Bool, itemAtURL url: NSURL, destinationURL destinationURL: NSURL, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func setUbiquitous(_ flag: Bool, itemAtURL url: NSURL, destinationURL destinationURL: NSURL) throws ``` |

Modified [NSFileManager.startDownloadingUbiquitousItemAtURL(_: NSURL) throws](https://developer.apple.com/documentation/foundation/filemanager/1410377-startdownloadingubiquitousitem)

|  | Declaration |
| --- | --- |
| From | ``` func startDownloadingUbiquitousItemAtURL(_ url: NSURL, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func startDownloadingUbiquitousItemAtURL(_ url: NSURL) throws ``` |

Modified [NSFileManager.subpathsAtPath(_: String) -> [String]?](https://developer.apple.com/documentation/foundation/nsfilemanager/1413742-subpathsatpath)

|  | Declaration |
| --- | --- |
| From | ``` func subpathsAtPath(_ path: String) -> [AnyObject]? ``` |
| To | ``` func subpathsAtPath(_ path: String) -> [String]? ``` |

Modified [NSFileManager.subpathsOfDirectoryAtPath(_: String) throws -> [String]](https://developer.apple.com/documentation/foundation/filemanager/1417353-subpathsofdirectory)

|  | Declaration |
| --- | --- |
| From | ``` func subpathsOfDirectoryAtPath(_ path: String, error error: NSErrorPointer) -> [AnyObject]? ``` |
| To | ``` func subpathsOfDirectoryAtPath(_ path: String) throws -> [String] ``` |

Modified [NSFileManager.URLForDirectory(_: NSSearchPathDirectory, inDomain: NSSearchPathDomainMask, appropriateForURL: NSURL?, create: Bool) throws -> NSURL](https://developer.apple.com/documentation/foundation/nsfilemanager/1407693-urlfordirectory)

|  | Declaration |
| --- | --- |
| From | ``` func URLForDirectory(_ directory: NSSearchPathDirectory, inDomain domain: NSSearchPathDomainMask, appropriateForURL url: NSURL?, create shouldCreate: Bool, error error: NSErrorPointer) -> NSURL? ``` |
| To | ``` func URLForDirectory(_ directory: NSSearchPathDirectory, inDomain domain: NSSearchPathDomainMask, appropriateForURL url: NSURL?, create shouldCreate: Bool) throws -> NSURL ``` |

Modified [NSFileManager.URLForPublishingUbiquitousItemAtURL(_: NSURL, expirationDate: AutoreleasingUnsafeMutablePointer<NSDate?>) throws -> NSURL](https://developer.apple.com/documentation/foundation/filemanager/1411577-url)

|  | Declaration |
| --- | --- |
| From | ``` func URLForPublishingUbiquitousItemAtURL(_ url: NSURL, expirationDate outDate: AutoreleasingUnsafeMutablePointer<NSDate?>, error error: NSErrorPointer) -> NSURL? ``` |
| To | ``` func URLForPublishingUbiquitousItemAtURL(_ url: NSURL, expirationDate outDate: AutoreleasingUnsafeMutablePointer<NSDate?>) throws -> NSURL ``` |

Modified [NSFileManager.URLsForDirectory(_: NSSearchPathDirectory, inDomains: NSSearchPathDomainMask) -> [NSURL]](https://developer.apple.com/documentation/foundation/nsfilemanager/1407726-urlsfordirectory)

|  | Declaration |
| --- | --- |
| From | ``` func URLsForDirectory(_ directory: NSSearchPathDirectory, inDomains domainMask: NSSearchPathDomainMask) -> [AnyObject] ``` |
| To | ``` func URLsForDirectory(_ directory: NSSearchPathDirectory, inDomains domainMask: NSSearchPathDomainMask) -> [NSURL] ``` |

Modified [NSFileManagerItemReplacementOptions [struct]](https://developer.apple.com/documentation/foundation/nsfilemanageritemreplacementoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSFileManagerItemReplacementOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var UsingNewMetadataOnly: NSFileManagerItemReplacementOptions { get }     static var WithoutDeletingBackupItem: NSFileManagerItemReplacementOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSFileManagerItemReplacementOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var UsingNewMetadataOnly: NSFileManagerItemReplacementOptions { get }     static var WithoutDeletingBackupItem: NSFileManagerItemReplacementOptions { get } } ``` | OptionSetType |

Modified [NSFilePresenter](https://developer.apple.com/documentation/foundation/nsfilepresenter)

|  | Declaration |
| --- | --- |
| From | ``` protocol NSFilePresenter : NSObjectProtocol {     @NSCopying var presentedItemURL: NSURL? { get }     var presentedItemOperationQueue: NSOperationQueue { get }     @NSCopying optional var primaryPresentedItemURL: NSURL? { get }     optional func relinquishPresentedItemToReader(_ reader: ((() -> Void)!) -> Void)     optional func relinquishPresentedItemToWriter(_ writer: ((() -> Void)!) -> Void)     optional func savePresentedItemChangesWithCompletionHandler(_ completionHandler: (NSError!) -> Void)     optional func accommodatePresentedItemDeletionWithCompletionHandler(_ completionHandler: (NSError!) -> Void)     optional func presentedItemDidMoveToURL(_ newURL: NSURL)     optional func presentedItemDidChange()     optional func presentedItemDidGainVersion(_ version: NSFileVersion)     optional func presentedItemDidLoseVersion(_ version: NSFileVersion)     optional func presentedItemDidResolveConflictVersion(_ version: NSFileVersion)     optional func accommodatePresentedSubitemDeletionAtURL(_ url: NSURL, completionHandler completionHandler: (NSError!) -> Void)     optional func presentedSubitemDidAppearAtURL(_ url: NSURL)     optional func presentedSubitemAtURL(_ oldURL: NSURL, didMoveToURL newURL: NSURL)     optional func presentedSubitemDidChangeAtURL(_ url: NSURL)     optional func presentedSubitemAtURL(_ url: NSURL, didGainVersion version: NSFileVersion)     optional func presentedSubitemAtURL(_ url: NSURL, didLoseVersion version: NSFileVersion)     optional func presentedSubitemAtURL(_ url: NSURL, didResolveConflictVersion version: NSFileVersion) } ``` |
| To | ``` protocol NSFilePresenter : NSObjectProtocol {     @NSCopying var presentedItemURL: NSURL? { get }     var presentedItemOperationQueue: NSOperationQueue { get }     @NSCopying optional var primaryPresentedItemURL: NSURL? { get }     optional func relinquishPresentedItemToReader(_ reader: ((() -> Void)?) -> Void)     optional func relinquishPresentedItemToWriter(_ writer: ((() -> Void)?) -> Void)     optional func savePresentedItemChangesWithCompletionHandler(_ completionHandler: (NSError?) -> Void)     optional func accommodatePresentedItemDeletionWithCompletionHandler(_ completionHandler: (NSError?) -> Void)     optional func presentedItemDidMoveToURL(_ newURL: NSURL)     optional func presentedItemDidChange()     optional func presentedItemDidGainVersion(_ version: NSFileVersion)     optional func presentedItemDidLoseVersion(_ version: NSFileVersion)     optional func presentedItemDidResolveConflictVersion(_ version: NSFileVersion)     optional func accommodatePresentedSubitemDeletionAtURL(_ url: NSURL, completionHandler completionHandler: (NSError?) -> Void)     optional func presentedSubitemDidAppearAtURL(_ url: NSURL)     optional func presentedSubitemAtURL(_ oldURL: NSURL, didMoveToURL newURL: NSURL)     optional func presentedSubitemDidChangeAtURL(_ url: NSURL)     optional func presentedSubitemAtURL(_ url: NSURL, didGainVersion version: NSFileVersion)     optional func presentedSubitemAtURL(_ url: NSURL, didLoseVersion version: NSFileVersion)     optional func presentedSubitemAtURL(_ url: NSURL, didResolveConflictVersion version: NSFileVersion) } ``` |

Modified [NSFilePresenter.accommodatePresentedItemDeletionWithCompletionHandler(_: (NSError?) -> Void)](https://developer.apple.com/documentation/foundation/nsfilepresenter/1414732-accommodatepresenteditemdeletion)

|  | Declaration |
| --- | --- |
| From | ``` optional func accommodatePresentedItemDeletionWithCompletionHandler(_ completionHandler: (NSError!) -> Void) ``` |
| To | ``` optional func accommodatePresentedItemDeletionWithCompletionHandler(_ completionHandler: (NSError?) -> Void) ``` |

Modified [NSFilePresenter.accommodatePresentedSubitemDeletionAtURL(_: NSURL, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/foundation/nsfilepresenter/1415657-accommodatepresentedsubitemdelet)

|  | Declaration |
| --- | --- |
| From | ``` optional func accommodatePresentedSubitemDeletionAtURL(_ url: NSURL, completionHandler completionHandler: (NSError!) -> Void) ``` |
| To | ``` optional func accommodatePresentedSubitemDeletionAtURL(_ url: NSURL, completionHandler completionHandler: (NSError?) -> Void) ``` |

Modified [NSFilePresenter.presentedItemDidGainVersion(_: NSFileVersion)](https://developer.apple.com/documentation/foundation/nsfilepresenter/1415018-presenteditemdidgainversion)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified [NSFilePresenter.presentedItemDidLoseVersion(_: NSFileVersion)](https://developer.apple.com/documentation/foundation/nsfilepresenter/1417258-presenteditemdidloseversion)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified [NSFilePresenter.presentedItemDidResolveConflictVersion(_: NSFileVersion)](https://developer.apple.com/documentation/foundation/nsfilepresenter/1418445-presenteditemdidresolveconflict)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified [NSFilePresenter.presentedItemOperationQueue](https://developer.apple.com/documentation/foundation/nsfilepresenter/1415250-presenteditemoperationqueue)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [NSFilePresenter.presentedSubitemAtURL(_: NSURL, didGainVersion: NSFileVersion)](https://developer.apple.com/documentation/foundation/nsfilepresenter/1415472-presentedsubitematurl)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified [NSFilePresenter.presentedSubitemAtURL(_: NSURL, didLoseVersion: NSFileVersion)](https://developer.apple.com/documentation/foundation/nsfilepresenter/1413957-presentedsubitem)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified [NSFilePresenter.presentedSubitemAtURL(_: NSURL, didResolveConflictVersion: NSFileVersion)](https://developer.apple.com/documentation/foundation/nsfilepresenter/1416913-presentedsubitem)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified [NSFilePresenter.relinquishPresentedItemToReader(_: ((() -> Void)?) -> Void)](https://developer.apple.com/documentation/foundation/nsfilepresenter/1410743-relinquishpresenteditem)

|  | Declaration |
| --- | --- |
| From | ``` optional func relinquishPresentedItemToReader(_ reader: ((() -> Void)!) -> Void) ``` |
| To | ``` optional func relinquishPresentedItemToReader(_ reader: ((() -> Void)?) -> Void) ``` |

Modified [NSFilePresenter.relinquishPresentedItemToWriter(_: ((() -> Void)?) -> Void)](https://developer.apple.com/documentation/foundation/nsfilepresenter/1413688-relinquishpresenteditem)

|  | Declaration |
| --- | --- |
| From | ``` optional func relinquishPresentedItemToWriter(_ writer: ((() -> Void)!) -> Void) ``` |
| To | ``` optional func relinquishPresentedItemToWriter(_ writer: ((() -> Void)?) -> Void) ``` |

Modified [NSFilePresenter.savePresentedItemChangesWithCompletionHandler(_: (NSError?) -> Void)](https://developer.apple.com/documentation/foundation/nsfilepresenter/1414407-savepresenteditemchangeswithcomp)

|  | Declaration |
| --- | --- |
| From | ``` optional func savePresentedItemChangesWithCompletionHandler(_ completionHandler: (NSError!) -> Void) ``` |
| To | ``` optional func savePresentedItemChangesWithCompletionHandler(_ completionHandler: (NSError?) -> Void) ``` |

Modified [NSFileVersion](https://developer.apple.com/documentation/foundation/nsfileversion)

|  | Declaration |
| --- | --- |
| From | ``` class NSFileVersion : NSObject {     class func currentVersionOfItemAtURL(_ url: NSURL) -> NSFileVersion?     class func otherVersionsOfItemAtURL(_ url: NSURL) -> [AnyObject]?     class func unresolvedConflictVersionsOfItemAtURL(_ url: NSURL) -> [AnyObject]?     class func getNonlocalVersionsOfItemAtURL(_ url: NSURL, completionHandler completionHandler: ([AnyObject]!, NSError!) -> Void)     init?(ofItemAtURL url: NSURL, forPersistentIdentifier persistentIdentifier: AnyObject) -> NSFileVersion     class func versionOfItemAtURL(_ url: NSURL, forPersistentIdentifier persistentIdentifier: AnyObject) -> NSFileVersion?     class func addVersionOfItemAtURL(_ url: NSURL, withContentsOfURL contentsURL: NSURL, options options: NSFileVersionAddingOptions, error outError: NSErrorPointer) -> NSFileVersion?     class func temporaryDirectoryURLForNewVersionOfItemAtURL(_ url: NSURL) -> NSURL     @NSCopying var URL: NSURL { get }     var localizedName: String? { get }     var localizedNameOfSavingComputer: String? { get }     @NSCopying var modificationDate: NSDate? { get }     var persistentIdentifier: NSCoding { get }     var conflict: Bool { get }     var resolved: Bool     var discardable: Bool     var hasLocalContents: Bool { get }     var hasThumbnail: Bool { get }     func replaceItemAtURL(_ url: NSURL, options options: NSFileVersionReplacingOptions, error error: NSErrorPointer) -> NSURL?     func removeAndReturnError(_ outError: NSErrorPointer) -> Bool     class func removeOtherVersionsOfItemAtURL(_ url: NSURL, error outError: NSErrorPointer) -> Bool } ``` |
| To | ``` class NSFileVersion : NSObject {     class func currentVersionOfItemAtURL(_ url: NSURL) -> NSFileVersion?     class func otherVersionsOfItemAtURL(_ url: NSURL) -> [NSFileVersion]?     class func unresolvedConflictVersionsOfItemAtURL(_ url: NSURL) -> [NSFileVersion]?     class func getNonlocalVersionsOfItemAtURL(_ url: NSURL, completionHandler completionHandler: ([NSFileVersion]?, NSError?) -> Void)      init?(ofItemAtURL url: NSURL, forPersistentIdentifier persistentIdentifier: AnyObject)     class func versionOfItemAtURL(_ url: NSURL, forPersistentIdentifier persistentIdentifier: AnyObject) -> NSFileVersion?     class func addVersionOfItemAtURL(_ url: NSURL, withContentsOfURL contentsURL: NSURL, options options: NSFileVersionAddingOptions) throws -> NSFileVersion     class func temporaryDirectoryURLForNewVersionOfItemAtURL(_ url: NSURL) -> NSURL     @NSCopying var URL: NSURL { get }     var localizedName: String? { get }     var localizedNameOfSavingComputer: String? { get }     @NSCopying var modificationDate: NSDate? { get }     var persistentIdentifier: NSCoding { get }     var conflict: Bool { get }     var resolved: Bool     var discardable: Bool     var hasLocalContents: Bool { get }     var hasThumbnail: Bool { get }     func replaceItemAtURL(_ url: NSURL, options options: NSFileVersionReplacingOptions) throws -> NSURL     func remove() throws     class func removeOtherVersionsOfItemAtURL(_ url: NSURL) throws } ``` |

Modified [NSFileVersion.getNonlocalVersionsOfItemAtURL(_: NSURL, completionHandler: ([NSFileVersion]?, NSError?) -> Void) [class]](https://developer.apple.com/documentation/foundation/nsfileversion/1416051-getnonlocalversionsofitem)

|  | Declaration |
| --- | --- |
| From | ``` class func getNonlocalVersionsOfItemAtURL(_ url: NSURL, completionHandler completionHandler: ([AnyObject]!, NSError!) -> Void) ``` |
| To | ``` class func getNonlocalVersionsOfItemAtURL(_ url: NSURL, completionHandler completionHandler: ([NSFileVersion]?, NSError?) -> Void) ``` |

Modified [NSFileVersion.init(ofItemAtURL: NSURL, forPersistentIdentifier: AnyObject)](https://developer.apple.com/documentation/foundation/nsfileversion/1415443-version)

|  | Declaration |
| --- | --- |
| From | ``` init?(ofItemAtURL url: NSURL, forPersistentIdentifier persistentIdentifier: AnyObject) -> NSFileVersion ``` |
| To | ``` init?(ofItemAtURL url: NSURL, forPersistentIdentifier persistentIdentifier: AnyObject) ``` |

Modified [NSFileVersion.otherVersionsOfItemAtURL(_: NSURL) -> [NSFileVersion]? [class]](https://developer.apple.com/documentation/foundation/nsfileversion/1418163-otherversionsofitematurl)

|  | Declaration |
| --- | --- |
| From | ``` class func otherVersionsOfItemAtURL(_ url: NSURL) -> [AnyObject]? ``` |
| To | ``` class func otherVersionsOfItemAtURL(_ url: NSURL) -> [NSFileVersion]? ``` |

Modified [NSFileVersion.remove() throws](https://developer.apple.com/documentation/foundation/nsfileversion/1407486-remove)

|  | Declaration |
| --- | --- |
| From | ``` func removeAndReturnError(_ outError: NSErrorPointer) -> Bool ``` |
| To | ``` func remove() throws ``` |

Modified [NSFileVersion.removeOtherVersionsOfItemAtURL(_: NSURL) throws [class]](https://developer.apple.com/documentation/foundation/nsfileversion/1411537-removeotherversionsofitem)

|  | Declaration |
| --- | --- |
| From | ``` class func removeOtherVersionsOfItemAtURL(_ url: NSURL, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` class func removeOtherVersionsOfItemAtURL(_ url: NSURL) throws ``` |

Modified [NSFileVersion.replaceItemAtURL(_: NSURL, options: NSFileVersionReplacingOptions) throws -> NSURL](https://developer.apple.com/documentation/foundation/nsfileversion/1412297-replaceitem)

|  | Declaration |
| --- | --- |
| From | ``` func replaceItemAtURL(_ url: NSURL, options options: NSFileVersionReplacingOptions, error error: NSErrorPointer) -> NSURL? ``` |
| To | ``` func replaceItemAtURL(_ url: NSURL, options options: NSFileVersionReplacingOptions) throws -> NSURL ``` |

Modified [NSFileVersion.unresolvedConflictVersionsOfItemAtURL(_: NSURL) -> [NSFileVersion]? [class]](https://developer.apple.com/documentation/foundation/nsfileversion/1417854-unresolvedconflictversionsofitem)

|  | Declaration |
| --- | --- |
| From | ``` class func unresolvedConflictVersionsOfItemAtURL(_ url: NSURL) -> [AnyObject]? ``` |
| To | ``` class func unresolvedConflictVersionsOfItemAtURL(_ url: NSURL) -> [NSFileVersion]? ``` |

Modified [NSFileVersionAddingOptions [struct]](https://developer.apple.com/documentation/foundation/nsfileversionaddingoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSFileVersionAddingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var ByMoving: NSFileVersionAddingOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSFileVersionAddingOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var ByMoving: NSFileVersionAddingOptions { get } } ``` | OptionSetType |

Modified [NSFileVersionReplacingOptions [struct]](https://developer.apple.com/documentation/foundation/nsfileversionreplacingoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSFileVersionReplacingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var ByMoving: NSFileVersionReplacingOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSFileVersionReplacingOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var ByMoving: NSFileVersionReplacingOptions { get } } ``` | OptionSetType |

Modified [NSFileWrapper](https://developer.apple.com/documentation/foundation/filewrapper)

|  | Declaration |
| --- | --- |
| From | ``` class NSFileWrapper : NSObject, NSCoding {     init?(URL url: NSURL, options options: NSFileWrapperReadingOptions, error outError: NSErrorPointer)     init(directoryWithFileWrappers childrenByPreferredName: [NSObject : AnyObject])     init(regularFileWithContents contents: NSData)     init(symbolicLinkWithDestinationURL url: NSURL)     init?(serializedRepresentation serializeRepresentation: NSData)     init?(coder inCoder: NSCoder)     var directory: Bool { get }     var regularFile: Bool { get }     var symbolicLink: Bool { get }     var preferredFilename: String     var filename: String?     var fileAttributes: [NSObject : AnyObject]     func matchesContentsOfURL(_ url: NSURL) -> Bool     func readFromURL(_ url: NSURL, options options: NSFileWrapperReadingOptions, error outError: NSErrorPointer) -> Bool     func writeToURL(_ url: NSURL, options options: NSFileWrapperWritingOptions, originalContentsURL originalContentsURL: NSURL?, error outError: NSErrorPointer) -> Bool     @NSCopying var serializedRepresentation: NSData { get }     func addFileWrapper(_ child: NSFileWrapper) -> String     func addRegularFileWithContents(_ data: NSData, preferredFilename fileName: String) -> String     func removeFileWrapper(_ child: NSFileWrapper)     var fileWrappers: [NSObject : AnyObject] { get }     func keyForFileWrapper(_ child: NSFileWrapper) -> String?     @NSCopying var regularFileContents: NSData? { get }     @NSCopying var symbolicLinkDestinationURL: NSURL { get } } ``` |
| To | ``` class NSFileWrapper : NSObject, NSCoding {     init(URL url: NSURL, options options: NSFileWrapperReadingOptions) throws     init(directoryWithFileWrappers childrenByPreferredName: [String : NSFileWrapper])     init(regularFileWithContents contents: NSData)     init(symbolicLinkWithDestinationURL url: NSURL)     init?(serializedRepresentation serializeRepresentation: NSData)     init?(coder inCoder: NSCoder)     var directory: Bool { get }     var regularFile: Bool { get }     var symbolicLink: Bool { get }     var preferredFilename: String?     var filename: String?     var fileAttributes: [String : AnyObject]     func matchesContentsOfURL(_ url: NSURL) -> Bool     func readFromURL(_ url: NSURL, options options: NSFileWrapperReadingOptions) throws     func writeToURL(_ url: NSURL, options options: NSFileWrapperWritingOptions, originalContentsURL originalContentsURL: NSURL?) throws     @NSCopying var serializedRepresentation: NSData? { get }     func addFileWrapper(_ child: NSFileWrapper) -> String     func addRegularFileWithContents(_ data: NSData, preferredFilename fileName: String) -> String     func removeFileWrapper(_ child: NSFileWrapper)     var fileWrappers: [String : NSFileWrapper]? { get }     func keyForFileWrapper(_ child: NSFileWrapper) -> String?     @NSCopying var regularFileContents: NSData? { get }     @NSCopying var symbolicLinkDestinationURL: NSURL? { get } } ``` |

Modified [NSFileWrapper.fileAttributes](https://developer.apple.com/documentation/foundation/filewrapper/1412745-fileattributes)

|  | Declaration |
| --- | --- |
| From | ``` var fileAttributes: [NSObject : AnyObject] ``` |
| To | ``` var fileAttributes: [String : AnyObject] ``` |

Modified [NSFileWrapper.fileWrappers](https://developer.apple.com/documentation/foundation/nsfilewrapper/1409437-filewrappers)

|  | Declaration |
| --- | --- |
| From | ``` var fileWrappers: [NSObject : AnyObject] { get } ``` |
| To | ``` var fileWrappers: [String : NSFileWrapper]? { get } ``` |

Modified [NSFileWrapper.init(directoryWithFileWrappers: [String : NSFileWrapper])](https://developer.apple.com/documentation/foundation/filewrapper/1415121-init)

|  | Declaration |
| --- | --- |
| From | ``` init(directoryWithFileWrappers childrenByPreferredName: [NSObject : AnyObject]) ``` |
| To | ``` init(directoryWithFileWrappers childrenByPreferredName: [String : NSFileWrapper]) ``` |

Modified [NSFileWrapper.init(URL: NSURL, options: NSFileWrapperReadingOptions) throws](https://developer.apple.com/documentation/foundation/filewrapper/1415658-init)

|  | Declaration |
| --- | --- |
| From | ``` init?(URL url: NSURL, options options: NSFileWrapperReadingOptions, error outError: NSErrorPointer) ``` |
| To | ``` init(URL url: NSURL, options options: NSFileWrapperReadingOptions) throws ``` |

Modified [NSFileWrapper.preferredFilename](https://developer.apple.com/documentation/foundation/filewrapper/1409368-preferredfilename)

|  | Declaration |
| --- | --- |
| From | ``` var preferredFilename: String ``` |
| To | ``` var preferredFilename: String? ``` |

Modified [NSFileWrapper.readFromURL(_: NSURL, options: NSFileWrapperReadingOptions) throws](https://developer.apple.com/documentation/foundation/filewrapper/1411645-read)

|  | Declaration |
| --- | --- |
| From | ``` func readFromURL(_ url: NSURL, options options: NSFileWrapperReadingOptions, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func readFromURL(_ url: NSURL, options options: NSFileWrapperReadingOptions) throws ``` |

Modified [NSFileWrapper.serializedRepresentation](https://developer.apple.com/documentation/foundation/nsfilewrapper/1412119-serializedrepresentation)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var serializedRepresentation: NSData { get } ``` |
| To | ``` @NSCopying var serializedRepresentation: NSData? { get } ``` |

Modified [NSFileWrapper.symbolicLinkDestinationURL](https://developer.apple.com/documentation/foundation/filewrapper/1408364-symboliclinkdestinationurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var symbolicLinkDestinationURL: NSURL { get } ``` |
| To | ``` @NSCopying var symbolicLinkDestinationURL: NSURL? { get } ``` |

Modified [NSFileWrapper.writeToURL(_: NSURL, options: NSFileWrapperWritingOptions, originalContentsURL: NSURL?) throws](https://developer.apple.com/documentation/foundation/nsfilewrapper/1415981-writetourl)

|  | Declaration |
| --- | --- |
| From | ``` func writeToURL(_ url: NSURL, options options: NSFileWrapperWritingOptions, originalContentsURL originalContentsURL: NSURL?, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func writeToURL(_ url: NSURL, options options: NSFileWrapperWritingOptions, originalContentsURL originalContentsURL: NSURL?) throws ``` |

Modified [NSFileWrapperReadingOptions [struct]](https://developer.apple.com/documentation/foundation/nsfilewrapperreadingoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSFileWrapperReadingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Immediate: NSFileWrapperReadingOptions { get }     static var WithoutMapping: NSFileWrapperReadingOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSFileWrapperReadingOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var Immediate: NSFileWrapperReadingOptions { get }     static var WithoutMapping: NSFileWrapperReadingOptions { get } } ``` | OptionSetType |

Modified [NSFileWrapperWritingOptions [struct]](https://developer.apple.com/documentation/foundation/nsfilewrapperwritingoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSFileWrapperWritingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Atomic: NSFileWrapperWritingOptions { get }     static var WithNameUpdating: NSFileWrapperWritingOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSFileWrapperWritingOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var Atomic: NSFileWrapperWritingOptions { get }     static var WithNameUpdating: NSFileWrapperWritingOptions { get } } ``` | OptionSetType |

Modified [NSFormatter](https://developer.apple.com/documentation/foundation/formatter)

|  | Declaration |
| --- | --- |
| From | ``` class NSFormatter : NSObject, NSCopying, NSCoding {     func stringForObjectValue(_ obj: AnyObject) -> String?     func attributedStringForObjectValue(_ obj: AnyObject, withDefaultAttributes attrs: [NSObject : AnyObject]?) -> NSAttributedString?     func editingStringForObjectValue(_ obj: AnyObject) -> String     func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>, forString string: String, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool     func isPartialStringValid(_ partialString: String, newEditingString newString: AutoreleasingUnsafeMutablePointer<NSString?>, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool     func isPartialStringValid(_ partialStringPtr: AutoreleasingUnsafeMutablePointer<NSString?>, proposedSelectedRange proposedSelRangePtr: NSRangePointer, originalString origString: String, originalSelectedRange origSelRange: NSRange, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool } ``` |
| To | ``` class NSFormatter : NSObject, NSCopying, NSCoding {     func stringForObjectValue(_ obj: AnyObject) -> String?     func attributedStringForObjectValue(_ obj: AnyObject, withDefaultAttributes attrs: [String : AnyObject]?) -> NSAttributedString?     func editingStringForObjectValue(_ obj: AnyObject) -> String?     func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>, forString string: String, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool     func isPartialStringValid(_ partialString: String, newEditingString newString: AutoreleasingUnsafeMutablePointer<NSString?>, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool     func isPartialStringValid(_ partialStringPtr: AutoreleasingUnsafeMutablePointer<NSString?>, proposedSelectedRange proposedSelRangePtr: NSRangePointer, originalString origString: String, originalSelectedRange origSelRange: NSRange, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool } ``` |

Modified [NSFormatter.attributedStringForObjectValue(_: AnyObject, withDefaultAttributes: [String : AnyObject]?) -> NSAttributedString?](https://developer.apple.com/documentation/foundation/formatter/1409478-attributedstring)

|  | Declaration |
| --- | --- |
| From | ``` func attributedStringForObjectValue(_ obj: AnyObject, withDefaultAttributes attrs: [NSObject : AnyObject]?) -> NSAttributedString? ``` |
| To | ``` func attributedStringForObjectValue(_ obj: AnyObject, withDefaultAttributes attrs: [String : AnyObject]?) -> NSAttributedString? ``` |

Modified [NSFormatter.editingStringForObjectValue(_: AnyObject) -> String?](https://developer.apple.com/documentation/foundation/formatter/1416333-editingstring)

|  | Declaration |
| --- | --- |
| From | ``` func editingStringForObjectValue(_ obj: AnyObject) -> String ``` |
| To | ``` func editingStringForObjectValue(_ obj: AnyObject) -> String? ``` |

Modified [NSFormattingContext [enum]](https://developer.apple.com/documentation/foundation/nsformattingcontext)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NSFormattingUnitStyle [enum]](https://developer.apple.com/documentation/foundation/nsformattingunitstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NSHashTable](https://developer.apple.com/documentation/foundation/nshashtable)

|  | Declaration |
| --- | --- |
| From | ``` class NSHashTable : NSObject, NSCopying, NSCoding, NSFastEnumeration {     init(options options: NSPointerFunctionsOptions, capacity initialCapacity: Int)     init(pointerFunctions functions: NSPointerFunctions, capacity initialCapacity: Int)     init(options options: NSPointerFunctionsOptions) -> NSHashTable     class func hashTableWithOptions(_ options: NSPointerFunctionsOptions) -> NSHashTable     class func weakObjectsHashTable() -> NSHashTable     @NSCopying var pointerFunctions: NSPointerFunctions { get }     var count: Int { get }     func member(_ object: AnyObject) -> AnyObject?     func objectEnumerator() -> NSEnumerator     func addObject(_ object: AnyObject)     func removeObject(_ object: AnyObject)     func removeAllObjects()     var allObjects: [AnyObject] { get }     var anyObject: AnyObject? { get }     func containsObject(_ anObject: AnyObject) -> Bool     func intersectsHashTable(_ other: NSHashTable) -> Bool     func isEqualToHashTable(_ other: NSHashTable) -> Bool     func isSubsetOfHashTable(_ other: NSHashTable) -> Bool     func intersectHashTable(_ other: NSHashTable)     func unionHashTable(_ other: NSHashTable)     func minusHashTable(_ other: NSHashTable)     var setRepresentation: Set<NSObject> { get } } ``` |
| To | ``` class NSHashTable : NSObject, NSCopying, NSCoding, NSFastEnumeration {     init(options options: NSPointerFunctionsOptions, capacity initialCapacity: Int)     init(pointerFunctions functions: NSPointerFunctions, capacity initialCapacity: Int)      init(options options: NSPointerFunctionsOptions)     class func hashTableWithOptions(_ options: NSPointerFunctionsOptions) -> NSHashTable     class func weakObjectsHashTable() -> NSHashTable     @NSCopying var pointerFunctions: NSPointerFunctions { get }     var count: Int { get }     func member(_ object: AnyObject?) -> AnyObject?     func objectEnumerator() -> NSEnumerator     func addObject(_ object: AnyObject?)     func removeObject(_ object: AnyObject?)     func removeAllObjects()     var allObjects: [AnyObject] { get }     var anyObject: AnyObject? { get }     func containsObject(_ anObject: AnyObject?) -> Bool     func intersectsHashTable(_ other: NSHashTable) -> Bool     func isEqualToHashTable(_ other: NSHashTable) -> Bool     func isSubsetOfHashTable(_ other: NSHashTable) -> Bool     func intersectHashTable(_ other: NSHashTable)     func unionHashTable(_ other: NSHashTable)     func minusHashTable(_ other: NSHashTable)     var setRepresentation: Set<NSObject> { get } } ``` |

Modified [NSHashTable.addObject(_: AnyObject?)](https://developer.apple.com/documentation/foundation/nshashtable/1411690-addobject)

|  | Declaration |
| --- | --- |
| From | ``` func addObject(_ object: AnyObject) ``` |
| To | ``` func addObject(_ object: AnyObject?) ``` |

Modified [NSHashTable.containsObject(_: AnyObject?) -> Bool](https://developer.apple.com/documentation/foundation/nshashtable/1415113-containsobject)

|  | Declaration |
| --- | --- |
| From | ``` func containsObject(_ anObject: AnyObject) -> Bool ``` |
| To | ``` func containsObject(_ anObject: AnyObject?) -> Bool ``` |

Modified [NSHashTable.init(options: NSPointerFunctionsOptions)](https://developer.apple.com/documentation/foundation/nshashtable/1415284-hashtablewithoptions)

|  | Declaration |
| --- | --- |
| From | ``` init(options options: NSPointerFunctionsOptions) -> NSHashTable ``` |
| To | ``` init(options options: NSPointerFunctionsOptions) ``` |

Modified [NSHashTable.member(_: AnyObject?) -> AnyObject?](https://developer.apple.com/documentation/foundation/nshashtable/1417991-member)

|  | Declaration |
| --- | --- |
| From | ``` func member(_ object: AnyObject) -> AnyObject? ``` |
| To | ``` func member(_ object: AnyObject?) -> AnyObject? ``` |

Modified [NSHashTable.removeObject(_: AnyObject?)](https://developer.apple.com/documentation/foundation/nshashtable/1415369-remove)

|  | Declaration |
| --- | --- |
| From | ``` func removeObject(_ object: AnyObject) ``` |
| To | ``` func removeObject(_ object: AnyObject?) ``` |

Modified [NSHTTPCookie](https://developer.apple.com/documentation/foundation/httpcookie)

|  | Declaration |
| --- | --- |
| From | ``` class NSHTTPCookie : NSObject {     init?(properties properties: [NSObject : AnyObject])     class func cookieWithProperties(_ properties: [NSObject : AnyObject]) -> NSHTTPCookie?     class func requestHeaderFieldsWithCookies(_ cookies: [AnyObject]) -> [NSObject : AnyObject]     class func cookiesWithResponseHeaderFields(_ headerFields: [NSObject : AnyObject], forURL URL: NSURL) -> [AnyObject]     var properties: [NSObject : AnyObject]? { get }     var version: Int { get }     var name: String { get }     var value: String? { get }     @NSCopying var expiresDate: NSDate! { get }     var sessionOnly: Bool { get }     var domain: String { get }     var path: String? { get }     var secure: Bool { get }     var HTTPOnly: Bool { get }     var comment: String? { get }     @NSCopying var commentURL: NSURL? { get }     var portList: [AnyObject]? { get } } ``` |
| To | ``` class NSHTTPCookie : NSObject {     init?(properties properties: [String : AnyObject])     class func cookieWithProperties(_ properties: [String : AnyObject]) -> NSHTTPCookie?     class func requestHeaderFieldsWithCookies(_ cookies: [NSHTTPCookie]) -> [String : String]     class func cookiesWithResponseHeaderFields(_ headerFields: [String : String], forURL URL: NSURL) -> [NSHTTPCookie]     var properties: [String : AnyObject]? { get }     var version: Int { get }     var name: String { get }     var value: String { get }     @NSCopying var expiresDate: NSDate? { get }     var sessionOnly: Bool { get }     var domain: String { get }     var path: String { get }     var secure: Bool { get }     var HTTPOnly: Bool { get }     var comment: String? { get }     @NSCopying var commentURL: NSURL? { get }     var portList: [NSNumber]? { get } } ``` |

Modified [NSHTTPCookie.cookiesWithResponseHeaderFields(_: [String : String], forURL: NSURL) -> [NSHTTPCookie] [class]](https://developer.apple.com/documentation/foundation/nshttpcookie/1393011-cookieswithresponseheaderfields)

|  | Declaration |
| --- | --- |
| From | ``` class func cookiesWithResponseHeaderFields(_ headerFields: [NSObject : AnyObject], forURL URL: NSURL) -> [AnyObject] ``` |
| To | ``` class func cookiesWithResponseHeaderFields(_ headerFields: [String : String], forURL URL: NSURL) -> [NSHTTPCookie] ``` |

Modified [NSHTTPCookie.expiresDate](https://developer.apple.com/documentation/foundation/httpcookie/1393019-expiresdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var expiresDate: NSDate! { get } ``` |
| To | ``` @NSCopying var expiresDate: NSDate? { get } ``` |

Modified [NSHTTPCookie.init(properties: [String : AnyObject])](https://developer.apple.com/documentation/foundation/httpcookie/1392975-init)

|  | Declaration |
| --- | --- |
| From | ``` init?(properties properties: [NSObject : AnyObject]) ``` |
| To | ``` init?(properties properties: [String : AnyObject]) ``` |

Modified [NSHTTPCookie.path](https://developer.apple.com/documentation/foundation/nshttpcookie/1392981-path)

|  | Declaration |
| --- | --- |
| From | ``` var path: String? { get } ``` |
| To | ``` var path: String { get } ``` |

Modified [NSHTTPCookie.portList](https://developer.apple.com/documentation/foundation/nshttpcookie/1393027-portlist)

|  | Declaration |
| --- | --- |
| From | ``` var portList: [AnyObject]? { get } ``` |
| To | ``` var portList: [NSNumber]? { get } ``` |

Modified [NSHTTPCookie.properties](https://developer.apple.com/documentation/foundation/nshttpcookie/1393017-properties)

|  | Declaration |
| --- | --- |
| From | ``` var properties: [NSObject : AnyObject]? { get } ``` |
| To | ``` var properties: [String : AnyObject]? { get } ``` |

Modified [NSHTTPCookie.requestHeaderFieldsWithCookies(_: [NSHTTPCookie]) -> [String : String] [class]](https://developer.apple.com/documentation/foundation/nshttpcookie/1393021-requestheaderfieldswithcookies)

|  | Declaration |
| --- | --- |
| From | ``` class func requestHeaderFieldsWithCookies(_ cookies: [AnyObject]) -> [NSObject : AnyObject] ``` |
| To | ``` class func requestHeaderFieldsWithCookies(_ cookies: [NSHTTPCookie]) -> [String : String] ``` |

Modified [NSHTTPCookie.value](https://developer.apple.com/documentation/foundation/nshttpcookie/1392995-value)

|  | Declaration |
| --- | --- |
| From | ``` var value: String? { get } ``` |
| To | ``` var value: String { get } ``` |

Modified [NSHTTPCookieAcceptPolicy [enum]](https://developer.apple.com/documentation/foundation/httpcookie/acceptpolicy)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSHTTPCookieStorage](https://developer.apple.com/documentation/foundation/nshttpcookiestorage)

|  | Declaration |
| --- | --- |
| From | ``` class NSHTTPCookieStorage : NSObject {     class func sharedHTTPCookieStorage() -> NSHTTPCookieStorage     var cookies: [AnyObject]? { get }     func setCookie(_ cookie: NSHTTPCookie)     func deleteCookie(_ cookie: NSHTTPCookie)     func removeCookiesSinceDate(_ date: NSDate)     func cookiesForURL(_ URL: NSURL) -> [AnyObject]?     func setCookies(_ cookies: [AnyObject], forURL URL: NSURL?, mainDocumentURL mainDocumentURL: NSURL?)     var cookieAcceptPolicy: NSHTTPCookieAcceptPolicy     func sortedCookiesUsingDescriptors(_ sortOrder: [AnyObject]) -> [AnyObject] } extension NSHTTPCookieStorage {     func storeCookies(_ cookies: [AnyObject], forTask task: NSURLSessionTask)     func getCookiesForTask(_ task: NSURLSessionTask, completionHandler completionHandler: (([AnyObject]!) -> Void)!) } ``` |
| To | ``` class NSHTTPCookieStorage : NSObject {     class func sharedHTTPCookieStorage() -> NSHTTPCookieStorage     class func sharedCookieStorageForGroupContainerIdentifier(_ identifier: String) -> NSHTTPCookieStorage     var cookies: [NSHTTPCookie]? { get }     func setCookie(_ cookie: NSHTTPCookie)     func deleteCookie(_ cookie: NSHTTPCookie)     func removeCookiesSinceDate(_ date: NSDate)     func cookiesForURL(_ URL: NSURL) -> [NSHTTPCookie]?     func setCookies(_ cookies: [NSHTTPCookie], forURL URL: NSURL?, mainDocumentURL mainDocumentURL: NSURL?)     var cookieAcceptPolicy: NSHTTPCookieAcceptPolicy     func sortedCookiesUsingDescriptors(_ sortOrder: [NSSortDescriptor]) -> [NSHTTPCookie] } extension NSHTTPCookieStorage {     func storeCookies(_ cookies: [NSHTTPCookie], forTask task: NSURLSessionTask)     func getCookiesForTask(_ task: NSURLSessionTask, completionHandler completionHandler: ([NSHTTPCookie]?) -> Void) } ``` |

Modified [NSHTTPCookieStorage.cookies](https://developer.apple.com/documentation/foundation/nshttpcookiestorage/1418390-cookies)

|  | Declaration |
| --- | --- |
| From | ``` var cookies: [AnyObject]? { get } ``` |
| To | ``` var cookies: [NSHTTPCookie]? { get } ``` |

Modified [NSHTTPCookieStorage.cookiesForURL(_: NSURL) -> [NSHTTPCookie]?](https://developer.apple.com/documentation/foundation/httpcookiestorage/1412100-cookies)

|  | Declaration |
| --- | --- |
| From | ``` func cookiesForURL(_ URL: NSURL) -> [AnyObject]? ``` |
| To | ``` func cookiesForURL(_ URL: NSURL) -> [NSHTTPCookie]? ``` |

Modified [NSHTTPCookieStorage.getCookiesForTask(_: NSURLSessionTask, completionHandler: ([NSHTTPCookie]?) -> Void)](https://developer.apple.com/documentation/foundation/httpcookiestorage/1408517-getcookiesfor)

|  | Declaration |
| --- | --- |
| From | ``` func getCookiesForTask(_ task: NSURLSessionTask, completionHandler completionHandler: (([AnyObject]!) -> Void)!) ``` |
| To | ``` func getCookiesForTask(_ task: NSURLSessionTask, completionHandler completionHandler: ([NSHTTPCookie]?) -> Void) ``` |

Modified [NSHTTPCookieStorage.setCookies(_: [NSHTTPCookie], forURL: NSURL?, mainDocumentURL: NSURL?)](https://developer.apple.com/documentation/foundation/nshttpcookiestorage/1412510-setcookies)

|  | Declaration |
| --- | --- |
| From | ``` func setCookies(_ cookies: [AnyObject], forURL URL: NSURL?, mainDocumentURL mainDocumentURL: NSURL?) ``` |
| To | ``` func setCookies(_ cookies: [NSHTTPCookie], forURL URL: NSURL?, mainDocumentURL mainDocumentURL: NSURL?) ``` |

Modified [NSHTTPCookieStorage.sortedCookiesUsingDescriptors(_: [NSSortDescriptor]) -> [NSHTTPCookie]](https://developer.apple.com/documentation/foundation/httpcookiestorage/1413730-sortedcookies)

|  | Declaration |
| --- | --- |
| From | ``` func sortedCookiesUsingDescriptors(_ sortOrder: [AnyObject]) -> [AnyObject] ``` |
| To | ``` func sortedCookiesUsingDescriptors(_ sortOrder: [NSSortDescriptor]) -> [NSHTTPCookie] ``` |

Modified [NSHTTPCookieStorage.storeCookies(_: [NSHTTPCookie], forTask: NSURLSessionTask)](https://developer.apple.com/documentation/foundation/httpcookiestorage/1415381-storecookies)

|  | Declaration |
| --- | --- |
| From | ``` func storeCookies(_ cookies: [AnyObject], forTask task: NSURLSessionTask) ``` |
| To | ``` func storeCookies(_ cookies: [NSHTTPCookie], forTask task: NSURLSessionTask) ``` |

Modified [NSHTTPURLResponse](https://developer.apple.com/documentation/foundation/httpurlresponse)

|  | Declaration |
| --- | --- |
| From | ``` class NSHTTPURLResponse : NSURLResponse {     init?(URL url: NSURL, statusCode statusCode: Int, HTTPVersion HTTPVersion: String?, headerFields headerFields: [NSObject : AnyObject]?)     var statusCode: Int { get }     var allHeaderFields: [NSObject : AnyObject] { get }     class func localizedStringForStatusCode(_ statusCode: Int) -> String } ``` |
| To | ``` class NSHTTPURLResponse : NSURLResponse {     init?(URL url: NSURL, statusCode statusCode: Int, HTTPVersion HTTPVersion: String?, headerFields headerFields: [String : String]?)     var statusCode: Int { get }     var allHeaderFields: [NSObject : AnyObject] { get }     class func localizedStringForStatusCode(_ statusCode: Int) -> String } ``` |

Modified [NSHTTPURLResponse.init(URL: NSURL, statusCode: Int, HTTPVersion: String?, headerFields: [String : String]?)](https://developer.apple.com/documentation/foundation/httpurlresponse/1415870-init)

|  | Declaration |
| --- | --- |
| From | ``` init?(URL url: NSURL, statusCode statusCode: Int, HTTPVersion HTTPVersion: String?, headerFields headerFields: [NSObject : AnyObject]?) ``` |
| To | ``` init?(URL url: NSURL, statusCode statusCode: Int, HTTPVersion HTTPVersion: String?, headerFields headerFields: [String : String]?) ``` |

Modified [NSIndexPath](https://developer.apple.com/documentation/foundation/nsindexpath)

|  | Declaration |
| --- | --- |
| From | ``` class NSIndexPath : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init!(index index: Int)     class func indexPathWithIndex(_ index: Int) -> Self!     convenience init!(indexes indexes: UnsafePointer<Int>, length length: Int)     class func indexPathWithIndexes(_ indexes: UnsafePointer<Int>, length length: Int) -> Self!     init(indexes indexes: UnsafePointer<Int>, length length: Int)     convenience init(index index: Int)     func indexPathByAddingIndex(_ index: Int) -> NSIndexPath     func indexPathByRemovingLastIndex() -> NSIndexPath     func indexAtPosition(_ position: Int) -> Int     var length: Int { get }     func getIndexes(_ indexes: UnsafeMutablePointer<Int>)     func compare(_ otherObject: NSIndexPath) -> NSComparisonResult } extension NSIndexPath {     init!(forItem item: Int, inSection section: Int) -> NSIndexPath     class func indexPathForItem(_ item: Int, inSection section: Int) -> NSIndexPath!     var item: Int { get } } extension NSIndexPath {     init!(forRow row: Int, inSection section: Int) -> NSIndexPath     class func indexPathForRow(_ row: Int, inSection section: Int) -> NSIndexPath!     var section: Int { get }     var row: Int { get } } ``` |
| To | ``` class NSIndexPath : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init(index index: Int)     class func indexPathWithIndex(_ index: Int) -> Self     convenience init(indexes indexes: UnsafePointer<Int>, length length: Int)     class func indexPathWithIndexes(_ indexes: UnsafePointer<Int>, length length: Int) -> Self     init(indexes indexes: UnsafePointer<Int>, length length: Int)     convenience init(index index: Int)     func indexPathByAddingIndex(_ index: Int) -> NSIndexPath     func indexPathByRemovingLastIndex() -> NSIndexPath     func indexAtPosition(_ position: Int) -> Int     var length: Int { get }     func getIndexes(_ indexes: UnsafeMutablePointer<Int>, range positionRange: NSRange)     func compare(_ otherObject: NSIndexPath) -> NSComparisonResult } extension NSIndexPath {     func getIndexes(_ indexes: UnsafeMutablePointer<Int>) } extension NSIndexPath {     convenience init(forItem item: Int, inSection section: Int)     class func indexPathForItem(_ item: Int, inSection section: Int) -> Self     var item: Int { get } } extension NSIndexPath {     convenience init(forRow row: Int, inSection section: Int)     class func indexPathForRow(_ row: Int, inSection section: Int) -> Self     var section: Int { get }     var row: Int { get } } ``` |

Modified [NSIndexSet](https://developer.apple.com/documentation/foundation/nsindexset)

|  | Declaration |
| --- | --- |
| From | ``` class NSIndexSet : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     convenience init!()     class func indexSet() -> Self!     convenience init!(index value: Int)     class func indexSetWithIndex(_ value: Int) -> Self!     convenience init!(indexesInRange range: NSRange)     class func indexSetWithIndexesInRange(_ range: NSRange) -> Self!     init(indexesInRange range: NSRange)     init(indexSet indexSet: NSIndexSet)     convenience init(index value: Int)     func isEqualToIndexSet(_ indexSet: NSIndexSet) -> Bool     var count: Int { get }     var firstIndex: Int { get }     var lastIndex: Int { get }     func indexGreaterThanIndex(_ value: Int) -> Int     func indexLessThanIndex(_ value: Int) -> Int     func indexGreaterThanOrEqualToIndex(_ value: Int) -> Int     func indexLessThanOrEqualToIndex(_ value: Int) -> Int     func getIndexes(_ indexBuffer: UnsafeMutablePointer<Int>, maxCount bufferSize: Int, inIndexRange range: NSRangePointer) -> Int     func countOfIndexesInRange(_ range: NSRange) -> Int     func containsIndex(_ value: Int) -> Bool     func containsIndexesInRange(_ range: NSRange) -> Bool     func containsIndexes(_ indexSet: NSIndexSet) -> Bool     func intersectsIndexesInRange(_ range: NSRange) -> Bool     func enumerateIndexesUsingBlock(_ block: (Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateIndexesWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateIndexesInRange(_ range: NSRange, options opts: NSEnumerationOptions, usingBlock block: ((Int, UnsafeMutablePointer<ObjCBool>) -> Void)?)     func indexPassingTest(_ predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexInRange(_ range: NSRange, options opts: NSEnumerationOptions, passingTest predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexesPassingTest(_ predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexesWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexesInRange(_ range: NSRange, options opts: NSEnumerationOptions, passingTest predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func enumerateRangesUsingBlock(_ block: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateRangesWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateRangesInRange(_ range: NSRange, options opts: NSEnumerationOptions, usingBlock block: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) } extension NSIndexSet : SequenceType {     func generate() -> NSIndexSetGenerator } extension NSIndexSet : SequenceType {     func generate() -> NSIndexSetGenerator } ``` |
| To | ``` class NSIndexSet : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     convenience init()     class func indexSet() -> Self     convenience init(index value: Int)     class func indexSetWithIndex(_ value: Int) -> Self     convenience init(indexesInRange range: NSRange)     class func indexSetWithIndexesInRange(_ range: NSRange) -> Self     init(indexesInRange range: NSRange)     init(indexSet indexSet: NSIndexSet)     convenience init(index value: Int)     func isEqualToIndexSet(_ indexSet: NSIndexSet) -> Bool     var count: Int { get }     var firstIndex: Int { get }     var lastIndex: Int { get }     func indexGreaterThanIndex(_ value: Int) -> Int     func indexLessThanIndex(_ value: Int) -> Int     func indexGreaterThanOrEqualToIndex(_ value: Int) -> Int     func indexLessThanOrEqualToIndex(_ value: Int) -> Int     func getIndexes(_ indexBuffer: UnsafeMutablePointer<Int>, maxCount bufferSize: Int, inIndexRange range: NSRangePointer) -> Int     func countOfIndexesInRange(_ range: NSRange) -> Int     func containsIndex(_ value: Int) -> Bool     func containsIndexesInRange(_ range: NSRange) -> Bool     func containsIndexes(_ indexSet: NSIndexSet) -> Bool     func intersectsIndexesInRange(_ range: NSRange) -> Bool     func enumerateIndexesUsingBlock(_ block: (Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateIndexesWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateIndexesInRange(_ range: NSRange, options opts: NSEnumerationOptions, usingBlock block: (Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func indexPassingTest(_ predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexInRange(_ range: NSRange, options opts: NSEnumerationOptions, passingTest predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexesPassingTest(_ predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexesWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexesInRange(_ range: NSRange, options opts: NSEnumerationOptions, passingTest predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func enumerateRangesUsingBlock(_ block: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateRangesWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateRangesInRange(_ range: NSRange, options opts: NSEnumerationOptions, usingBlock block: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) } extension NSIndexSet : SequenceType {     func generate() -> NSIndexSetGenerator } extension NSIndexSet : SequenceType {     func generate() -> NSIndexSetGenerator } ``` |

Modified [NSIndexSet.enumerateIndexesInRange(_: NSRange, options: NSEnumerationOptions, usingBlock: (Int, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/foundation/nsindexset/1408162-enumerateindexesinrange)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateIndexesInRange(_ range: NSRange, options opts: NSEnumerationOptions, usingBlock block: ((Int, UnsafeMutablePointer<ObjCBool>) -> Void)?) ``` |
| To | ``` func enumerateIndexesInRange(_ range: NSRange, options opts: NSEnumerationOptions, usingBlock block: (Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified NSIndexSetGenerator [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSIndexSetGenerator : GeneratorType {     typealias Element = Int     init(set set: NSIndexSet)     mutating func next() -> Int? } ``` |
| To | ``` struct NSIndexSetGenerator : GeneratorType {     typealias Element = Int     mutating func next() -> Int? } ``` |

Modified [NSItemProviderErrorCode [enum]](https://developer.apple.com/documentation/foundation/nsitemprovidererrorcode)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum NSItemProviderErrorCode : Int {     case UnknownError     case ItemUnavailableError     case UnexpectedValueClassError } ``` | -- |
| To | ``` enum NSItemProviderErrorCode : Int {     case UnknownError     case ItemUnavailableError     case UnexpectedValueClassError     case UnavailableCoercionError } ``` | Int |

Modified [NSJSONReadingOptions [struct]](https://developer.apple.com/documentation/foundation/nsjsonreadingoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSJSONReadingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var MutableContainers: NSJSONReadingOptions { get }     static var MutableLeaves: NSJSONReadingOptions { get }     static var AllowFragments: NSJSONReadingOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSJSONReadingOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var MutableContainers: NSJSONReadingOptions { get }     static var MutableLeaves: NSJSONReadingOptions { get }     static var AllowFragments: NSJSONReadingOptions { get } } ``` | OptionSetType |

Modified [NSJSONSerialization](https://developer.apple.com/documentation/foundation/nsjsonserialization)

|  | Declaration |
| --- | --- |
| From | ``` class NSJSONSerialization : NSObject {     class func isValidJSONObject(_ obj: AnyObject) -> Bool     class func dataWithJSONObject(_ obj: AnyObject, options opt: NSJSONWritingOptions, error error: NSErrorPointer) -> NSData?     class func JSONObjectWithData(_ data: NSData, options opt: NSJSONReadingOptions, error error: NSErrorPointer) -> AnyObject?     class func writeJSONObject(_ obj: AnyObject, toStream stream: NSOutputStream, options opt: NSJSONWritingOptions, error error: NSErrorPointer) -> Int     class func JSONObjectWithStream(_ stream: NSInputStream, options opt: NSJSONReadingOptions, error error: NSErrorPointer) -> AnyObject? } ``` |
| To | ``` class NSJSONSerialization : NSObject {     class func isValidJSONObject(_ obj: AnyObject) -> Bool     class func dataWithJSONObject(_ obj: AnyObject, options opt: NSJSONWritingOptions) throws -> NSData     class func JSONObjectWithData(_ data: NSData, options opt: NSJSONReadingOptions) throws -> AnyObject     class func writeJSONObject(_ obj: AnyObject, toStream stream: NSOutputStream, options opt: NSJSONWritingOptions, error error: NSErrorPointer) -> Int     class func JSONObjectWithStream(_ stream: NSInputStream, options opt: NSJSONReadingOptions) throws -> AnyObject } ``` |

Modified [NSJSONSerialization.dataWithJSONObject(_: AnyObject, options: NSJSONWritingOptions) throws -> NSData [class]](https://developer.apple.com/documentation/foundation/jsonserialization/1413636-data)

|  | Declaration |
| --- | --- |
| From | ``` class func dataWithJSONObject(_ obj: AnyObject, options opt: NSJSONWritingOptions, error error: NSErrorPointer) -> NSData? ``` |
| To | ``` class func dataWithJSONObject(_ obj: AnyObject, options opt: NSJSONWritingOptions) throws -> NSData ``` |

Modified [NSJSONSerialization.JSONObjectWithData(_: NSData, options: NSJSONReadingOptions) throws -> AnyObject [class]](https://developer.apple.com/documentation/foundation/nsjsonserialization/1415493-jsonobjectwithdata)

|  | Declaration |
| --- | --- |
| From | ``` class func JSONObjectWithData(_ data: NSData, options opt: NSJSONReadingOptions, error error: NSErrorPointer) -> AnyObject? ``` |
| To | ``` class func JSONObjectWithData(_ data: NSData, options opt: NSJSONReadingOptions) throws -> AnyObject ``` |

Modified [NSJSONSerialization.JSONObjectWithStream(_: NSInputStream, options: NSJSONReadingOptions) throws -> AnyObject [class]](https://developer.apple.com/documentation/foundation/jsonserialization/1418059-jsonobject)

|  | Declaration |
| --- | --- |
| From | ``` class func JSONObjectWithStream(_ stream: NSInputStream, options opt: NSJSONReadingOptions, error error: NSErrorPointer) -> AnyObject? ``` |
| To | ``` class func JSONObjectWithStream(_ stream: NSInputStream, options opt: NSJSONReadingOptions) throws -> AnyObject ``` |

Modified [NSJSONWritingOptions [struct]](https://developer.apple.com/documentation/foundation/jsonserialization/writingoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSJSONWritingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var PrettyPrinted: NSJSONWritingOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSJSONWritingOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var PrettyPrinted: NSJSONWritingOptions { get } } ``` | OptionSetType |

Modified [NSKeyedArchiver](https://developer.apple.com/documentation/foundation/nskeyedarchiver)

|  | Declaration |
| --- | --- |
| From | ``` class NSKeyedArchiver : NSCoder {     class func archivedDataWithRootObject(_ rootObject: AnyObject) -> NSData     class func archiveRootObject(_ rootObject: AnyObject, toFile path: String) -> Bool     init(forWritingWithMutableData data: NSMutableData)     unowned(unsafe) var delegate: NSKeyedArchiverDelegate?     var outputFormat: NSPropertyListFormat     func finishEncoding()     class func setClassName(_ codedName: String?, forClass cls: AnyClass)     func setClassName(_ codedName: String?, forClass cls: AnyClass)     class func classNameForClass(_ cls: AnyClass) -> String?     func classNameForClass(_ cls: AnyClass) -> String?     func encodeObject(_ objv: AnyObject?, forKey key: String)     func encodeConditionalObject(_ objv: AnyObject?, forKey key: String)     func encodeBool(_ boolv: Bool, forKey key: String)     func encodeInt(_ intv: Int32, forKey key: String)     func encodeInt32(_ intv: Int32, forKey key: String)     func encodeInt64(_ intv: Int64, forKey key: String)     func encodeFloat(_ realv: Float, forKey key: String)     func encodeDouble(_ realv: Double, forKey key: String)     func encodeBytes(_ bytesp: UnsafePointer<UInt8>, length lenv: Int, forKey key: String)     func setRequiresSecureCoding(_ b: Bool) } ``` |
| To | ``` class NSKeyedArchiver : NSCoder {     class func archivedDataWithRootObject(_ rootObject: AnyObject) -> NSData     class func archiveRootObject(_ rootObject: AnyObject, toFile path: String) -> Bool     init(forWritingWithMutableData data: NSMutableData)     unowned(unsafe) var delegate: NSKeyedArchiverDelegate?     var outputFormat: NSPropertyListFormat     func finishEncoding()     class func setClassName(_ codedName: String?, forClass cls: AnyClass)     func setClassName(_ codedName: String?, forClass cls: AnyClass)     class func classNameForClass(_ cls: AnyClass) -> String?     func classNameForClass(_ cls: AnyClass) -> String?     func encodeObject(_ objv: AnyObject?, forKey key: String)     func encodeConditionalObject(_ objv: AnyObject?, forKey key: String)     func encodeBool(_ boolv: Bool, forKey key: String)     func encodeInt(_ intv: Int32, forKey key: String)     func encodeInt32(_ intv: Int32, forKey key: String)     func encodeInt64(_ intv: Int64, forKey key: String)     func encodeFloat(_ realv: Float, forKey key: String)     func encodeDouble(_ realv: Double, forKey key: String)     func encodeBytes(_ bytesp: UnsafePointer<UInt8>, length lenv: Int, forKey key: String)     var requiresSecureCoding: Bool } ``` |

Modified [NSKeyedArchiverDelegate](https://developer.apple.com/documentation/foundation/nskeyedarchiverdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol NSKeyedArchiverDelegate : NSObjectProtocol {     optional func archiver(_ archiver: NSKeyedArchiver, willEncodeObject object: AnyObject) -> AnyObject?     optional func archiver(_ archiver: NSKeyedArchiver, didEncodeObject object: AnyObject?)     optional func archiver(_ archiver: NSKeyedArchiver, willReplaceObject object: AnyObject, withObject newObject: AnyObject)     optional func archiverWillFinish(_ archiver: NSKeyedArchiver)     optional func archiverDidFinish(_ archiver: NSKeyedArchiver) } ``` |
| To | ``` protocol NSKeyedArchiverDelegate : NSObjectProtocol {     optional func archiver(_ archiver: NSKeyedArchiver, willEncodeObject object: AnyObject) -> AnyObject?     optional func archiver(_ archiver: NSKeyedArchiver, didEncodeObject object: AnyObject?)     optional func archiver(_ archiver: NSKeyedArchiver, willReplaceObject object: AnyObject?, withObject newObject: AnyObject?)     optional func archiverWillFinish(_ archiver: NSKeyedArchiver)     optional func archiverDidFinish(_ archiver: NSKeyedArchiver) } ``` |

Modified [NSKeyedArchiverDelegate.archiver(_: NSKeyedArchiver, willReplaceObject: AnyObject?, withObject: AnyObject?)](https://developer.apple.com/documentation/foundation/nskeyedarchiverdelegate/1409389-archiver)

|  | Declaration |
| --- | --- |
| From | ``` optional func archiver(_ archiver: NSKeyedArchiver, willReplaceObject object: AnyObject, withObject newObject: AnyObject) ``` |
| To | ``` optional func archiver(_ archiver: NSKeyedArchiver, willReplaceObject object: AnyObject?, withObject newObject: AnyObject?) ``` |

Modified [NSKeyedUnarchiver](https://developer.apple.com/documentation/foundation/nskeyedunarchiver)

|  | Declaration |
| --- | --- |
| From | ``` class NSKeyedUnarchiver : NSCoder {     class func unarchiveObjectWithData(_ data: NSData) -> AnyObject?     class func unarchiveObjectWithFile(_ path: String) -> AnyObject?     init(forReadingWithData data: NSData)     unowned(unsafe) var delegate: NSKeyedUnarchiverDelegate?     func finishDecoding()     class func setClass(_ cls: AnyClass?, forClassName codedName: String)     func setClass(_ cls: AnyClass?, forClassName codedName: String)     class func classForClassName(_ codedName: String) -> AnyClass?     func classForClassName(_ codedName: String) -> AnyClass?     func containsValueForKey(_ key: String) -> Bool     func decodeObjectForKey(_ key: String) -> AnyObject?     func decodeBoolForKey(_ key: String) -> Bool     func decodeIntForKey(_ key: String) -> Int32     func decodeInt32ForKey(_ key: String) -> Int32     func decodeInt64ForKey(_ key: String) -> Int64     func decodeFloatForKey(_ key: String) -> Float     func decodeDoubleForKey(_ key: String) -> Double     func decodeBytesForKey(_ key: String, returnedLength lengthp: UnsafeMutablePointer<Int>) -> UnsafePointer<UInt8>     func setRequiresSecureCoding(_ b: Bool) } ``` |
| To | ``` class NSKeyedUnarchiver : NSCoder {     class func unarchiveObjectWithData(_ data: NSData) -> AnyObject?     class func unarchiveTopLevelObjectWithData(_ data: NSData) throws -> AnyObject     class func unarchiveObjectWithFile(_ path: String) -> AnyObject?     init(forReadingWithData data: NSData)     unowned(unsafe) var delegate: NSKeyedUnarchiverDelegate?     func finishDecoding()     class func setClass(_ cls: AnyClass?, forClassName codedName: String)     func setClass(_ cls: AnyClass?, forClassName codedName: String)     class func classForClassName(_ codedName: String) -> AnyClass?     func classForClassName(_ codedName: String) -> AnyClass?     func containsValueForKey(_ key: String) -> Bool     func decodeObjectForKey(_ key: String) -> AnyObject?     func decodeBoolForKey(_ key: String) -> Bool     func decodeIntForKey(_ key: String) -> Int32     func decodeInt32ForKey(_ key: String) -> Int32     func decodeInt64ForKey(_ key: String) -> Int64     func decodeFloatForKey(_ key: String) -> Float     func decodeDoubleForKey(_ key: String) -> Double     func decodeBytesForKey(_ key: String, returnedLength lengthp: UnsafeMutablePointer<Int>) -> UnsafePointer<UInt8>     var requiresSecureCoding: Bool } extension NSKeyedUnarchiver {     @warn_unused_result     class func unarchiveTopLevelObjectWithData(_ data: NSData) throws -> AnyObject? } extension NSKeyedUnarchiver {     @warn_unused_result     class func unarchiveTopLevelObjectWithData(_ data: NSData) throws -> AnyObject? } ``` |

Modified [NSKeyedUnarchiverDelegate](https://developer.apple.com/documentation/foundation/nskeyedunarchiverdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol NSKeyedUnarchiverDelegate : NSObjectProtocol {     optional func unarchiver(_ unarchiver: NSKeyedUnarchiver, cannotDecodeObjectOfClassName name: String, originalClasses classNames: [AnyObject]) -> AnyClass     optional func unarchiver(_ unarchiver: NSKeyedUnarchiver, didDecodeObject object: AnyObject?) -> AnyObject?     optional func unarchiver(_ unarchiver: NSKeyedUnarchiver, willReplaceObject object: AnyObject, withObject newObject: AnyObject)     optional func unarchiverWillFinish(_ unarchiver: NSKeyedUnarchiver)     optional func unarchiverDidFinish(_ unarchiver: NSKeyedUnarchiver) } ``` |
| To | ``` protocol NSKeyedUnarchiverDelegate : NSObjectProtocol {     optional func unarchiver(_ unarchiver: NSKeyedUnarchiver, cannotDecodeObjectOfClassName name: String, originalClasses classNames: [String]) -> AnyClass?     optional func unarchiver(_ unarchiver: NSKeyedUnarchiver, didDecodeObject object: AnyObject?) -> AnyObject?     optional func unarchiver(_ unarchiver: NSKeyedUnarchiver, willReplaceObject object: AnyObject, withObject newObject: AnyObject)     optional func unarchiverWillFinish(_ unarchiver: NSKeyedUnarchiver)     optional func unarchiverDidFinish(_ unarchiver: NSKeyedUnarchiver) } ``` |

Modified [NSKeyedUnarchiverDelegate.unarchiver(_: NSKeyedUnarchiver, cannotDecodeObjectOfClassName: String, originalClasses: [String]) -> AnyClass?](https://developer.apple.com/documentation/foundation/nskeyedunarchiverdelegate/1409948-unarchiver)

|  | Declaration |
| --- | --- |
| From | ``` optional func unarchiver(_ unarchiver: NSKeyedUnarchiver, cannotDecodeObjectOfClassName name: String, originalClasses classNames: [AnyObject]) -> AnyClass ``` |
| To | ``` optional func unarchiver(_ unarchiver: NSKeyedUnarchiver, cannotDecodeObjectOfClassName name: String, originalClasses classNames: [String]) -> AnyClass? ``` |

Modified [NSKeyValueChange [enum]](https://developer.apple.com/documentation/foundation/nskeyvaluechange)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSKeyValueObservingOptions [struct]](https://developer.apple.com/documentation/foundation/nskeyvalueobservingoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSKeyValueObservingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var New: NSKeyValueObservingOptions { get }     static var Old: NSKeyValueObservingOptions { get }     static var Initial: NSKeyValueObservingOptions { get }     static var Prior: NSKeyValueObservingOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSKeyValueObservingOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var New: NSKeyValueObservingOptions { get }     static var Old: NSKeyValueObservingOptions { get }     static var Initial: NSKeyValueObservingOptions { get }     static var Prior: NSKeyValueObservingOptions { get } } ``` | OptionSetType |

Modified [NSKeyValueSetMutationKind [enum]](https://developer.apple.com/documentation/foundation/nskeyvaluesetmutationkind)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSLengthFormatterUnit [enum]](https://developer.apple.com/documentation/foundation/nslengthformatterunit)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NSLinguisticTagger](https://developer.apple.com/documentation/foundation/nslinguistictagger)

|  | Declaration |
| --- | --- |
| From | ``` class NSLinguisticTagger : NSObject {     init(tagSchemes tagSchemes: [AnyObject], options opts: Int)     var tagSchemes: [AnyObject] { get }     var string: String?     class func availableTagSchemesForLanguage(_ language: String) -> [AnyObject]     func setOrthography(_ orthography: NSOrthography?, range range: NSRange)     func orthographyAtIndex(_ charIndex: Int, effectiveRange effectiveRange: NSRangePointer) -> NSOrthography?     func stringEditedInRange(_ newRange: NSRange, changeInLength delta: Int)     func enumerateTagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, usingBlock block: (String!, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)     func sentenceRangeForRange(_ range: NSRange) -> NSRange     func tagAtIndex(_ charIndex: Int, scheme tagScheme: String, tokenRange tokenRange: NSRangePointer, sentenceRange sentenceRange: NSRangePointer) -> String?     func tagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, tokenRanges tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [AnyObject]     func possibleTagsAtIndex(_ charIndex: Int, scheme tagScheme: String, tokenRange tokenRange: NSRangePointer, sentenceRange sentenceRange: NSRangePointer, scores scores: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [AnyObject]? } ``` |
| To | ``` class NSLinguisticTagger : NSObject {     init(tagSchemes tagSchemes: [String], options opts: Int)     var tagSchemes: [String] { get }     var string: String?     class func availableTagSchemesForLanguage(_ language: String) -> [String]     func setOrthography(_ orthography: NSOrthography?, range range: NSRange)     func orthographyAtIndex(_ charIndex: Int, effectiveRange effectiveRange: NSRangePointer) -> NSOrthography?     func stringEditedInRange(_ newRange: NSRange, changeInLength delta: Int)     func enumerateTagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, usingBlock block: (String, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)     func sentenceRangeForRange(_ range: NSRange) -> NSRange     func tagAtIndex(_ charIndex: Int, scheme tagScheme: String, tokenRange tokenRange: NSRangePointer, sentenceRange sentenceRange: NSRangePointer) -> String?     func tagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, tokenRanges tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [String]     func possibleTagsAtIndex(_ charIndex: Int, scheme tagScheme: String, tokenRange tokenRange: NSRangePointer, sentenceRange sentenceRange: NSRangePointer, scores scores: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [String]? } ``` |

Modified [NSLinguisticTagger.availableTagSchemesForLanguage(_: String) -> [String] [class]](https://developer.apple.com/documentation/foundation/nslinguistictagger/1408694-availabletagschemesforlanguage)

|  | Declaration |
| --- | --- |
| From | ``` class func availableTagSchemesForLanguage(_ language: String) -> [AnyObject] ``` |
| To | ``` class func availableTagSchemesForLanguage(_ language: String) -> [String] ``` |

Modified [NSLinguisticTagger.enumerateTagsInRange(_: NSRange, scheme: String, options: NSLinguisticTaggerOptions, usingBlock: (String, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/foundation/nslinguistictagger/1410036-enumeratetags)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateTagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, usingBlock block: (String!, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateTagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, usingBlock block: (String, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [NSLinguisticTagger.init(tagSchemes: [String], options: Int)](https://developer.apple.com/documentation/foundation/nslinguistictagger/1414576-init)

|  | Declaration |
| --- | --- |
| From | ``` init(tagSchemes tagSchemes: [AnyObject], options opts: Int) ``` |
| To | ``` init(tagSchemes tagSchemes: [String], options opts: Int) ``` |

Modified [NSLinguisticTagger.possibleTagsAtIndex(_: Int, scheme: String, tokenRange: NSRangePointer, sentenceRange: NSRangePointer, scores: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [String]?](https://developer.apple.com/documentation/foundation/nslinguistictagger/1408537-possibletags)

|  | Declaration |
| --- | --- |
| From | ``` func possibleTagsAtIndex(_ charIndex: Int, scheme tagScheme: String, tokenRange tokenRange: NSRangePointer, sentenceRange sentenceRange: NSRangePointer, scores scores: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [AnyObject]? ``` |
| To | ``` func possibleTagsAtIndex(_ charIndex: Int, scheme tagScheme: String, tokenRange tokenRange: NSRangePointer, sentenceRange sentenceRange: NSRangePointer, scores scores: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [String]? ``` |

Modified [NSLinguisticTagger.tagSchemes](https://developer.apple.com/documentation/foundation/nslinguistictagger/1409018-tagschemes)

|  | Declaration |
| --- | --- |
| From | ``` var tagSchemes: [AnyObject] { get } ``` |
| To | ``` var tagSchemes: [String] { get } ``` |

Modified [NSLinguisticTagger.tagsInRange(_: NSRange, scheme: String, options: NSLinguisticTaggerOptions, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [String]](https://developer.apple.com/documentation/foundation/nslinguistictagger/1417826-tagsinrange)

|  | Declaration |
| --- | --- |
| From | ``` func tagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, tokenRanges tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [AnyObject] ``` |
| To | ``` func tagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, tokenRanges tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [String] ``` |

Modified [NSLinguisticTaggerOptions [struct]](https://developer.apple.com/documentation/foundation/nslinguistictagger/options)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSLinguisticTaggerOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var OmitWords: NSLinguisticTaggerOptions { get }     static var OmitPunctuation: NSLinguisticTaggerOptions { get }     static var OmitWhitespace: NSLinguisticTaggerOptions { get }     static var OmitOther: NSLinguisticTaggerOptions { get }     static var JoinNames: NSLinguisticTaggerOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSLinguisticTaggerOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var OmitWords: NSLinguisticTaggerOptions { get }     static var OmitPunctuation: NSLinguisticTaggerOptions { get }     static var OmitWhitespace: NSLinguisticTaggerOptions { get }     static var OmitOther: NSLinguisticTaggerOptions { get }     static var JoinNames: NSLinguisticTaggerOptions { get } } ``` | OptionSetType |

Modified [NSLocale](https://developer.apple.com/documentation/foundation/nslocale)

|  | Declaration |
| --- | --- |
| From | ``` class NSLocale : NSObject, NSCopying, NSSecureCoding, NSCoding {     func objectForKey(_ key: AnyObject) -> AnyObject?     func displayNameForKey(_ key: AnyObject, value value: AnyObject) -> String?     init(localeIdentifier string: String)     init?(coder aDecoder: NSCoder) } extension NSLocale {     var localeIdentifier: String { get } } extension NSLocale {     class func autoupdatingCurrentLocale() -> NSLocale     class func currentLocale() -> NSLocale     class func systemLocale() -> NSLocale     convenience init(localeIdentifier ident: String)     class func localeWithLocaleIdentifier(_ ident: String) -> Self     convenience init!() } extension NSLocale {     class func availableLocaleIdentifiers() -> [AnyObject]     class func ISOLanguageCodes() -> [AnyObject]     class func ISOCountryCodes() -> [AnyObject]     class func ISOCurrencyCodes() -> [AnyObject]     class func commonISOCurrencyCodes() -> [AnyObject]     class func preferredLanguages() -> [AnyObject]     class func componentsFromLocaleIdentifier(_ string: String) -> [NSObject : AnyObject]     class func localeIdentifierFromComponents(_ dict: [NSObject : AnyObject]) -> String     class func canonicalLocaleIdentifierFromString(_ string: String) -> String     class func canonicalLanguageIdentifierFromString(_ string: String) -> String     class func localeIdentifierFromWindowsLocaleCode(_ lcid: UInt32) -> String?     class func windowsLocaleCodeFromLocaleIdentifier(_ localeIdentifier: String) -> UInt32     class func characterDirectionForLanguage(_ isoLangCode: String) -> NSLocaleLanguageDirection     class func lineDirectionForLanguage(_ isoLangCode: String) -> NSLocaleLanguageDirection } ``` |
| To | ``` class NSLocale : NSObject, NSCopying, NSSecureCoding, NSCoding {     func objectForKey(_ key: AnyObject) -> AnyObject?     func displayNameForKey(_ key: AnyObject, value value: AnyObject) -> String?     init(localeIdentifier string: String)     init?(coder aDecoder: NSCoder) } extension NSLocale {     var localeIdentifier: String { get } } extension NSLocale {     class func autoupdatingCurrentLocale() -> NSLocale     class func currentLocale() -> NSLocale     class func systemLocale() -> NSLocale     convenience init(localeIdentifier ident: String)     class func localeWithLocaleIdentifier(_ ident: String) -> Self     convenience init() } extension NSLocale {     class func availableLocaleIdentifiers() -> [String]     class func ISOLanguageCodes() -> [String]     class func ISOCountryCodes() -> [String]     class func ISOCurrencyCodes() -> [String]     class func commonISOCurrencyCodes() -> [String]     class func preferredLanguages() -> [String]     class func componentsFromLocaleIdentifier(_ string: String) -> [String : String]     class func localeIdentifierFromComponents(_ dict: [String : String]) -> String     class func canonicalLocaleIdentifierFromString(_ string: String) -> String     class func canonicalLanguageIdentifierFromString(_ string: String) -> String     class func localeIdentifierFromWindowsLocaleCode(_ lcid: UInt32) -> String?     class func windowsLocaleCodeFromLocaleIdentifier(_ localeIdentifier: String) -> UInt32     class func characterDirectionForLanguage(_ isoLangCode: String) -> NSLocaleLanguageDirection     class func lineDirectionForLanguage(_ isoLangCode: String) -> NSLocaleLanguageDirection } ``` |

Modified [NSLocale.availableLocaleIdentifiers() -> [String] [class]](https://developer.apple.com/documentation/foundation/nslocale/1410448-availablelocaleidentifiers)

|  | Declaration |
| --- | --- |
| From | ``` class func availableLocaleIdentifiers() -> [AnyObject] ``` |
| To | ``` class func availableLocaleIdentifiers() -> [String] ``` |

Modified [NSLocale.commonISOCurrencyCodes() -> [String] [class]](https://developer.apple.com/documentation/foundation/nslocale/1407272-commonisocurrencycodes)

|  | Declaration |
| --- | --- |
| From | ``` class func commonISOCurrencyCodes() -> [AnyObject] ``` |
| To | ``` class func commonISOCurrencyCodes() -> [String] ``` |

Modified [NSLocale.componentsFromLocaleIdentifier(_: String) -> [String : String] [class]](https://developer.apple.com/documentation/foundation/nslocale/1409220-componentsfromlocaleidentifier)

|  | Declaration |
| --- | --- |
| From | ``` class func componentsFromLocaleIdentifier(_ string: String) -> [NSObject : AnyObject] ``` |
| To | ``` class func componentsFromLocaleIdentifier(_ string: String) -> [String : String] ``` |

Modified [NSLocale.ISOCountryCodes() -> [String] [class]](https://developer.apple.com/documentation/foundation/nslocale/1413869-isocountrycodes)

|  | Declaration |
| --- | --- |
| From | ``` class func ISOCountryCodes() -> [AnyObject] ``` |
| To | ``` class func ISOCountryCodes() -> [String] ``` |

Modified [NSLocale.ISOCurrencyCodes() -> [String] [class]](https://developer.apple.com/documentation/foundation/nslocale/1417834-isocurrencycodes)

|  | Declaration |
| --- | --- |
| From | ``` class func ISOCurrencyCodes() -> [AnyObject] ``` |
| To | ``` class func ISOCurrencyCodes() -> [String] ``` |

Modified [NSLocale.ISOLanguageCodes() -> [String] [class]](https://developer.apple.com/documentation/foundation/nslocale/1418015-isolanguagecodes)

|  | Declaration |
| --- | --- |
| From | ``` class func ISOLanguageCodes() -> [AnyObject] ``` |
| To | ``` class func ISOLanguageCodes() -> [String] ``` |

Modified [NSLocale.localeIdentifierFromComponents(_: [String : String]) -> String [class]](https://developer.apple.com/documentation/foundation/nslocale/1412439-localeidentifier)

|  | Declaration |
| --- | --- |
| From | ``` class func localeIdentifierFromComponents(_ dict: [NSObject : AnyObject]) -> String ``` |
| To | ``` class func localeIdentifierFromComponents(_ dict: [String : String]) -> String ``` |

Modified [NSLocale.preferredLanguages() -> [String] [class]](https://developer.apple.com/documentation/foundation/nslocale/1415614-preferredlanguages)

|  | Declaration |
| --- | --- |
| From | ``` class func preferredLanguages() -> [AnyObject] ``` |
| To | ``` class func preferredLanguages() -> [String] ``` |

Modified [NSLocaleLanguageDirection [enum]](https://developer.apple.com/documentation/foundation/nslocale/languagedirection)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSMachPort](https://developer.apple.com/documentation/foundation/nsmachport)

|  | Declaration |
| --- | --- |
| From | ``` class NSMachPort : NSPort {     class func portWithMachPort(_ machPort: UInt32) -> NSPort     convenience init(machPort machPort: UInt32)     func setDelegate(_ anObject: NSMachPortDelegate?)     func delegate() -> NSMachPortDelegate?     class func portWithMachPort(_ machPort: UInt32, options f: Int) -> NSPort     init(machPort machPort: UInt32, options f: Int)     var machPort: UInt32 { get }     func scheduleInRunLoop(_ runLoop: NSRunLoop, forMode mode: String)     func removeFromRunLoop(_ runLoop: NSRunLoop, forMode mode: String) } ``` |
| To | ``` class NSMachPort : NSPort {     class func portWithMachPort(_ machPort: UInt32) -> NSPort     init(machPort machPort: UInt32)     func setDelegate(_ anObject: NSMachPortDelegate?)     func delegate() -> NSMachPortDelegate?     class func portWithMachPort(_ machPort: UInt32, options f: NSMachPortOptions) -> NSPort     init(machPort machPort: UInt32, options f: NSMachPortOptions)     var machPort: UInt32 { get }     func scheduleInRunLoop(_ runLoop: NSRunLoop, forMode mode: String)     func removeFromRunLoop(_ runLoop: NSRunLoop, forMode mode: String) } ``` |

Modified [NSMachPort.init(machPort: UInt32)](https://developer.apple.com/documentation/foundation/nsmachport/1399499-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(machPort machPort: UInt32) ``` |
| To | ``` init(machPort machPort: UInt32) ``` |

Modified [NSMachPort.init(machPort: UInt32, options: NSMachPortOptions)](https://developer.apple.com/documentation/foundation/nsmachport/1399559-initwithmachport)

|  | Declaration |
| --- | --- |
| From | ``` init(machPort machPort: UInt32, options f: Int) ``` |
| To | ``` init(machPort machPort: UInt32, options f: NSMachPortOptions) ``` |

Modified [NSMachPort.portWithMachPort(_: UInt32, options: NSMachPortOptions) -> NSPort [class]](https://developer.apple.com/documentation/foundation/nsmachport/1399551-portwithmachport)

|  | Declaration |
| --- | --- |
| From | ``` class func portWithMachPort(_ machPort: UInt32, options f: Int) -> NSPort ``` |
| To | ``` class func portWithMachPort(_ machPort: UInt32, options f: NSMachPortOptions) -> NSPort ``` |

Modified [NSMapTable](https://developer.apple.com/documentation/foundation/nsmaptable)

|  | Declaration |
| --- | --- |
| From | ``` class NSMapTable : NSObject, NSCopying, NSCoding, NSFastEnumeration {     init(keyOptions keyOptions: NSPointerFunctionsOptions, valueOptions valueOptions: NSPointerFunctionsOptions, capacity initialCapacity: Int)     init(keyPointerFunctions keyFunctions: NSPointerFunctions, valuePointerFunctions valueFunctions: NSPointerFunctions, capacity initialCapacity: Int)     init(keyOptions keyOptions: NSPointerFunctionsOptions, valueOptions valueOptions: NSPointerFunctionsOptions) -> NSMapTable     class func mapTableWithKeyOptions(_ keyOptions: NSPointerFunctionsOptions, valueOptions valueOptions: NSPointerFunctionsOptions) -> NSMapTable     class func strongToStrongObjectsMapTable() -> NSMapTable     class func weakToStrongObjectsMapTable() -> NSMapTable     class func strongToWeakObjectsMapTable() -> NSMapTable     class func weakToWeakObjectsMapTable() -> NSMapTable     @NSCopying var keyPointerFunctions: NSPointerFunctions { get }     @NSCopying var valuePointerFunctions: NSPointerFunctions { get }     func objectForKey(_ aKey: AnyObject) -> AnyObject?     func removeObjectForKey(_ aKey: AnyObject)     func setObject(_ anObject: AnyObject, forKey aKey: AnyObject)     var count: Int { get }     func keyEnumerator() -> NSEnumerator     func objectEnumerator() -> NSEnumerator     func removeAllObjects()     func dictionaryRepresentation() -> [NSObject : AnyObject] } ``` |
| To | ``` class NSMapTable : NSObject, NSCopying, NSCoding, NSFastEnumeration {     init(keyOptions keyOptions: NSPointerFunctionsOptions, valueOptions valueOptions: NSPointerFunctionsOptions, capacity initialCapacity: Int)     init(keyPointerFunctions keyFunctions: NSPointerFunctions, valuePointerFunctions valueFunctions: NSPointerFunctions, capacity initialCapacity: Int)      init(keyOptions keyOptions: NSPointerFunctionsOptions, valueOptions valueOptions: NSPointerFunctionsOptions)     class func mapTableWithKeyOptions(_ keyOptions: NSPointerFunctionsOptions, valueOptions valueOptions: NSPointerFunctionsOptions) -> NSMapTable     class func strongToStrongObjectsMapTable() -> NSMapTable     class func weakToStrongObjectsMapTable() -> NSMapTable     class func strongToWeakObjectsMapTable() -> NSMapTable     class func weakToWeakObjectsMapTable() -> NSMapTable     @NSCopying var keyPointerFunctions: NSPointerFunctions { get }     @NSCopying var valuePointerFunctions: NSPointerFunctions { get }     func objectForKey(_ aKey: AnyObject?) -> AnyObject?     func removeObjectForKey(_ aKey: AnyObject?)     func setObject(_ anObject: AnyObject?, forKey aKey: AnyObject?)     var count: Int { get }     func keyEnumerator() -> NSEnumerator     func objectEnumerator() -> NSEnumerator?     func removeAllObjects()     func dictionaryRepresentation() -> [NSObject : AnyObject] } ``` |

Modified [NSMapTable.init(keyOptions: NSPointerFunctionsOptions, valueOptions: NSPointerFunctionsOptions)](https://developer.apple.com/documentation/foundation/nsmaptable/1391414-init)

|  | Declaration |
| --- | --- |
| From | ``` init(keyOptions keyOptions: NSPointerFunctionsOptions, valueOptions valueOptions: NSPointerFunctionsOptions) -> NSMapTable ``` |
| To | ``` init(keyOptions keyOptions: NSPointerFunctionsOptions, valueOptions valueOptions: NSPointerFunctionsOptions) ``` |

Modified [NSMapTable.objectEnumerator() -> NSEnumerator?](https://developer.apple.com/documentation/foundation/nsmaptable/1391400-objectenumerator)

|  | Declaration |
| --- | --- |
| From | ``` func objectEnumerator() -> NSEnumerator ``` |
| To | ``` func objectEnumerator() -> NSEnumerator? ``` |

Modified [NSMapTable.objectForKey(_: AnyObject?) -> AnyObject?](https://developer.apple.com/documentation/foundation/nsmaptable/1391444-object)

|  | Declaration |
| --- | --- |
| From | ``` func objectForKey(_ aKey: AnyObject) -> AnyObject? ``` |
| To | ``` func objectForKey(_ aKey: AnyObject?) -> AnyObject? ``` |

Modified [NSMapTable.removeObjectForKey(_: AnyObject?)](https://developer.apple.com/documentation/foundation/nsmaptable/1391461-removeobject)

|  | Declaration |
| --- | --- |
| From | ``` func removeObjectForKey(_ aKey: AnyObject) ``` |
| To | ``` func removeObjectForKey(_ aKey: AnyObject?) ``` |

Modified [NSMapTable.setObject(_: AnyObject?, forKey: AnyObject?)](https://developer.apple.com/documentation/foundation/nsmaptable/1391457-setobject)

|  | Declaration |
| --- | --- |
| From | ``` func setObject(_ anObject: AnyObject, forKey aKey: AnyObject) ``` |
| To | ``` func setObject(_ anObject: AnyObject?, forKey aKey: AnyObject?) ``` |

Modified [NSMassFormatterUnit [enum]](https://developer.apple.com/documentation/foundation/massformatter/unit)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NSMatchingFlags [struct]](https://developer.apple.com/documentation/foundation/nsregularexpression/matchingflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSMatchingFlags : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Progress: NSMatchingFlags { get }     static var Completed: NSMatchingFlags { get }     static var HitEnd: NSMatchingFlags { get }     static var RequiredEnd: NSMatchingFlags { get }     static var InternalError: NSMatchingFlags { get } } ``` | RawOptionSetType |
| To | ``` struct NSMatchingFlags : OptionSetType {     init(rawValue rawValue: UInt)     static var Progress: NSMatchingFlags { get }     static var Completed: NSMatchingFlags { get }     static var HitEnd: NSMatchingFlags { get }     static var RequiredEnd: NSMatchingFlags { get }     static var InternalError: NSMatchingFlags { get } } ``` | OptionSetType |

Modified [NSMatchingOptions [struct]](https://developer.apple.com/documentation/foundation/nsregularexpression/matchingoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSMatchingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var ReportProgress: NSMatchingOptions { get }     static var ReportCompletion: NSMatchingOptions { get }     static var Anchored: NSMatchingOptions { get }     static var WithTransparentBounds: NSMatchingOptions { get }     static var WithoutAnchoringBounds: NSMatchingOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSMatchingOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var ReportProgress: NSMatchingOptions { get }     static var ReportCompletion: NSMatchingOptions { get }     static var Anchored: NSMatchingOptions { get }     static var WithTransparentBounds: NSMatchingOptions { get }     static var WithoutAnchoringBounds: NSMatchingOptions { get } } ``` | OptionSetType |

Modified [NSMetadataItem](https://developer.apple.com/documentation/foundation/nsmetadataitem)

|  | Declaration |
| --- | --- |
| From | ``` class NSMetadataItem : NSObject {     init?(URL url: NSURL)     func valueForAttribute(_ key: String) -> AnyObject?     func valuesForAttributes(_ keys: [AnyObject]) -> [NSObject : AnyObject]?     var attributes: [AnyObject] { get } } ``` |
| To | ``` class NSMetadataItem : NSObject {     init?(URL url: NSURL)     func valueForAttribute(_ key: String) -> AnyObject?     func valuesForAttributes(_ keys: [String]) -> [String : AnyObject]?     var attributes: [String] { get } } ``` |

Modified [NSMetadataItem.attributes](https://developer.apple.com/documentation/foundation/nsmetadataitem/1418347-attributes)

|  | Declaration |
| --- | --- |
| From | ``` var attributes: [AnyObject] { get } ``` |
| To | ``` var attributes: [String] { get } ``` |

Modified [NSMetadataItem.valuesForAttributes(_: [String]) -> [String : AnyObject]?](https://developer.apple.com/documentation/foundation/nsmetadataitem/1409934-valuesforattributes)

|  | Declaration |
| --- | --- |
| From | ``` func valuesForAttributes(_ keys: [AnyObject]) -> [NSObject : AnyObject]? ``` |
| To | ``` func valuesForAttributes(_ keys: [String]) -> [String : AnyObject]? ``` |

Modified [NSMetadataQuery](https://developer.apple.com/documentation/foundation/nsmetadataquery)

|  | Declaration |
| --- | --- |
| From | ``` class NSMetadataQuery : NSObject {     unowned(unsafe) var delegate: NSMetadataQueryDelegate?     @NSCopying var predicate: NSPredicate?     var sortDescriptors: [AnyObject]     var valueListAttributes: [AnyObject]     var groupingAttributes: [AnyObject]?     var notificationBatchingInterval: NSTimeInterval     var searchScopes: [AnyObject]     var searchItems: [AnyObject]?     var operationQueue: NSOperationQueue?     func startQuery() -> Bool     func stopQuery()     var started: Bool { get }     var gathering: Bool { get }     var stopped: Bool { get }     func disableUpdates()     func enableUpdates()     var resultCount: Int { get }     func resultAtIndex(_ idx: Int) -> AnyObject     func enumerateResultsUsingBlock(_ block: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateResultsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     var results: [AnyObject] { get }     func indexOfResult(_ result: AnyObject) -> Int     var valueLists: [NSObject : AnyObject] { get }     var groupedResults: [AnyObject] { get }     func valueOfAttribute(_ attrName: String, forResultAtIndex idx: Int) -> AnyObject? } ``` |
| To | ``` class NSMetadataQuery : NSObject {     unowned(unsafe) var delegate: NSMetadataQueryDelegate?     @NSCopying var predicate: NSPredicate?     var sortDescriptors: [NSSortDescriptor]     var valueListAttributes: [String]     var groupingAttributes: [String]?     var notificationBatchingInterval: NSTimeInterval     var searchScopes: [AnyObject]     var searchItems: [AnyObject]?     var operationQueue: NSOperationQueue?     func startQuery() -> Bool     func stopQuery()     var started: Bool { get }     var gathering: Bool { get }     var stopped: Bool { get }     func disableUpdates()     func enableUpdates()     var resultCount: Int { get }     func resultAtIndex(_ idx: Int) -> AnyObject     func enumerateResultsUsingBlock(_ block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateResultsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     var results: [AnyObject] { get }     func indexOfResult(_ result: AnyObject) -> Int     var valueLists: [String : [NSMetadataQueryAttributeValueTuple]] { get }     var groupedResults: [NSMetadataQueryResultGroup] { get }     func valueOfAttribute(_ attrName: String, forResultAtIndex idx: Int) -> AnyObject? } ``` |

Modified [NSMetadataQuery.enumerateResultsUsingBlock(_: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/foundation/nsmetadataquery/1415856-enumerateresults)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateResultsUsingBlock(_ block: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateResultsUsingBlock(_ block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [NSMetadataQuery.enumerateResultsWithOptions(_: NSEnumerationOptions, usingBlock: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/foundation/nsmetadataquery/1415123-enumerateresults)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateResultsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateResultsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [NSMetadataQuery.groupedResults](https://developer.apple.com/documentation/foundation/nsmetadataquery/1416579-groupedresults)

|  | Declaration |
| --- | --- |
| From | ``` var groupedResults: [AnyObject] { get } ``` |
| To | ``` var groupedResults: [NSMetadataQueryResultGroup] { get } ``` |

Modified [NSMetadataQuery.groupingAttributes](https://developer.apple.com/documentation/foundation/nsmetadataquery/1409191-groupingattributes)

|  | Declaration |
| --- | --- |
| From | ``` var groupingAttributes: [AnyObject]? ``` |
| To | ``` var groupingAttributes: [String]? ``` |

Modified [NSMetadataQuery.sortDescriptors](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411847-sortdescriptors)

|  | Declaration |
| --- | --- |
| From | ``` var sortDescriptors: [AnyObject] ``` |
| To | ``` var sortDescriptors: [NSSortDescriptor] ``` |

Modified [NSMetadataQuery.valueListAttributes](https://developer.apple.com/documentation/foundation/nsmetadataquery/1407767-valuelistattributes)

|  | Declaration |
| --- | --- |
| From | ``` var valueListAttributes: [AnyObject] ``` |
| To | ``` var valueListAttributes: [String] ``` |

Modified [NSMetadataQuery.valueLists](https://developer.apple.com/documentation/foundation/nsmetadataquery/1418401-valuelists)

|  | Declaration |
| --- | --- |
| From | ``` var valueLists: [NSObject : AnyObject] { get } ``` |
| To | ``` var valueLists: [String : [NSMetadataQueryAttributeValueTuple]] { get } ``` |

Modified [NSMetadataQueryDelegate.metadataQuery(_: NSMetadataQuery, replacementObjectForResultObject: NSMetadataItem) -> AnyObject](https://developer.apple.com/documentation/foundation/nsmetadataquerydelegate/1407317-metadataquery)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified [NSMetadataQueryDelegate.metadataQuery(_: NSMetadataQuery, replacementValueForAttribute: String, value: AnyObject) -> AnyObject](https://developer.apple.com/documentation/foundation/nsmetadataquerydelegate/1414215-metadataquery)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified [NSMetadataQueryResultGroup](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup)

|  | Declaration |
| --- | --- |
| From | ``` class NSMetadataQueryResultGroup : NSObject {     var attribute: String { get }     var value: AnyObject { get }     var subgroups: [AnyObject]? { get }     var resultCount: Int { get }     func resultAtIndex(_ idx: Int) -> AnyObject!     var results: [AnyObject] { get } } ``` |
| To | ``` class NSMetadataQueryResultGroup : NSObject {     var attribute: String { get }     var value: AnyObject { get }     var subgroups: [NSMetadataQueryResultGroup]? { get }     var resultCount: Int { get }     func resultAtIndex(_ idx: Int) -> AnyObject     var results: [AnyObject] { get } } ``` |

Modified [NSMetadataQueryResultGroup.resultAtIndex(_: Int) -> AnyObject](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/1410397-result)

|  | Declaration |
| --- | --- |
| From | ``` func resultAtIndex(_ idx: Int) -> AnyObject! ``` |
| To | ``` func resultAtIndex(_ idx: Int) -> AnyObject ``` |

Modified [NSMetadataQueryResultGroup.subgroups](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/1409929-subgroups)

|  | Declaration |
| --- | --- |
| From | ``` var subgroups: [AnyObject]? { get } ``` |
| To | ``` var subgroups: [NSMetadataQueryResultGroup]? { get } ``` |

Modified [NSMutableArray](https://developer.apple.com/documentation/foundation/nsmutablearray)

|  | Declaration |
| --- | --- |
| From | ``` class NSMutableArray : NSArray {     func addObject(_ anObject: AnyObject)     func insertObject(_ anObject: AnyObject, atIndex index: Int)     func removeLastObject()     func removeObjectAtIndex(_ index: Int)     func replaceObjectAtIndex(_ index: Int, withObject anObject: AnyObject)     init()     init(capacity numItems: Int)     init(coder aDecoder: NSCoder) } extension NSMutableArray {     func addObjectsFromArray(_ otherArray: [AnyObject])     func exchangeObjectAtIndex(_ idx1: Int, withObjectAtIndex idx2: Int)     func removeAllObjects()     func removeObject(_ anObject: AnyObject, inRange range: NSRange)     func removeObject(_ anObject: AnyObject)     func removeObjectIdenticalTo(_ anObject: AnyObject, inRange range: NSRange)     func removeObjectIdenticalTo(_ anObject: AnyObject)     func removeObjectsFromIndices(_ indices: UnsafeMutablePointer<Int>, numIndices cnt: Int)     func removeObjectsInArray(_ otherArray: [AnyObject])     func removeObjectsInRange(_ range: NSRange)     func replaceObjectsInRange(_ range: NSRange, withObjectsFromArray otherArray: [AnyObject], range otherRange: NSRange)     func replaceObjectsInRange(_ range: NSRange, withObjectsFromArray otherArray: [AnyObject])     func setArray(_ otherArray: [AnyObject])     func sortUsingFunction(_ compare: CFunctionPointer<((AnyObject!, AnyObject!, UnsafeMutablePointer<Void>) -> Int)>, context context: UnsafeMutablePointer<Void>)     func sortUsingSelector(_ comparator: Selector)     func insertObjects(_ objects: [AnyObject], atIndexes indexes: NSIndexSet)     func removeObjectsAtIndexes(_ indexes: NSIndexSet)     func replaceObjectsAtIndexes(_ indexes: NSIndexSet, withObjects objects: [AnyObject])     subscript (idx: Int) -> AnyObject     func setObject(_ obj: AnyObject, atIndexedSubscript idx: Int)     func sortUsingComparator(_ cmptr: NSComparator)     func sortWithOptions(_ opts: NSSortOptions, usingComparator cmptr: NSComparator) } extension NSMutableArray {     convenience init!(capacity numItems: Int)     class func arrayWithCapacity(_ numItems: Int) -> Self!     init?(contentsOfFile path: String) -> NSMutableArray     class func arrayWithContentsOfFile(_ path: String) -> NSMutableArray?     init?(contentsOfURL url: NSURL) -> NSMutableArray     class func arrayWithContentsOfURL(_ url: NSURL) -> NSMutableArray?     convenience init?(contentsOfFile path: String)     convenience init?(contentsOfURL url: NSURL) } extension NSMutableArray {     func filterUsingPredicate(_ predicate: NSPredicate) } extension NSMutableArray {     func sortUsingDescriptors(_ sortDescriptors: [AnyObject]) } ``` |
| To | ``` class NSMutableArray : NSArray {     func addObject(_ anObject: AnyObject)     func insertObject(_ anObject: AnyObject, atIndex index: Int)     func removeLastObject()     func removeObjectAtIndex(_ index: Int)     func replaceObjectAtIndex(_ index: Int, withObject anObject: AnyObject)     init()     init(capacity numItems: Int)     init?(coder aDecoder: NSCoder) } extension NSMutableArray {     func addObjectsFromArray(_ otherArray: [AnyObject])     func exchangeObjectAtIndex(_ idx1: Int, withObjectAtIndex idx2: Int)     func removeAllObjects()     func removeObject(_ anObject: AnyObject, inRange range: NSRange)     func removeObject(_ anObject: AnyObject)     func removeObjectIdenticalTo(_ anObject: AnyObject, inRange range: NSRange)     func removeObjectIdenticalTo(_ anObject: AnyObject)     func removeObjectsFromIndices(_ indices: UnsafeMutablePointer<Int>, numIndices cnt: Int)     func removeObjectsInArray(_ otherArray: [AnyObject])     func removeObjectsInRange(_ range: NSRange)     func replaceObjectsInRange(_ range: NSRange, withObjectsFromArray otherArray: [AnyObject], range otherRange: NSRange)     func replaceObjectsInRange(_ range: NSRange, withObjectsFromArray otherArray: [AnyObject])     func setArray(_ otherArray: [AnyObject])     func sortUsingFunction(_ compare: (AnyObject, AnyObject, UnsafeMutablePointer<Void>) -> Int, context context: UnsafeMutablePointer<Void>)     func sortUsingSelector(_ comparator: Selector)     func insertObjects(_ objects: [AnyObject], atIndexes indexes: NSIndexSet)     func removeObjectsAtIndexes(_ indexes: NSIndexSet)     func replaceObjectsAtIndexes(_ indexes: NSIndexSet, withObjects objects: [AnyObject])     subscript (_ idx: Int) -> AnyObject     func setObject(_ obj: AnyObject, atIndexedSubscript idx: Int)     func sortUsingComparator(_ cmptr: NSComparator)     func sortWithOptions(_ opts: NSSortOptions, usingComparator cmptr: NSComparator) } extension NSMutableArray {     convenience init(capacity numItems: Int)     class func arrayWithCapacity(_ numItems: Int) -> Self      init?(contentsOfFile path: String)     class func arrayWithContentsOfFile(_ path: String) -> NSMutableArray?      init?(contentsOfURL url: NSURL)     class func arrayWithContentsOfURL(_ url: NSURL) -> NSMutableArray?     convenience init?(contentsOfFile path: String)     convenience init?(contentsOfURL url: NSURL) } extension NSMutableArray {     func filterUsingPredicate(_ predicate: NSPredicate) } extension NSMutableArray {     func sortUsingDescriptors(_ sortDescriptors: [NSSortDescriptor]) } ``` |

Modified [NSMutableArray.init(coder: NSCoder)](https://developer.apple.com/documentation/foundation/nsmutablearray/1409527-init)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified [NSMutableArray.sortUsingDescriptors(_: [NSSortDescriptor])](https://developer.apple.com/documentation/foundation/nsmutablearray/1410745-sortusingdescriptors)

|  | Declaration |
| --- | --- |
| From | ``` func sortUsingDescriptors(_ sortDescriptors: [AnyObject]) ``` |
| To | ``` func sortUsingDescriptors(_ sortDescriptors: [NSSortDescriptor]) ``` |

Modified [NSMutableArray.sortUsingFunction(_: (AnyObject, AnyObject, UnsafeMutablePointer<Void>) -> Int, context: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/foundation/nsmutablearray/1408332-sortusingfunction)

|  | Declaration |
| --- | --- |
| From | ``` func sortUsingFunction(_ compare: CFunctionPointer<((AnyObject!, AnyObject!, UnsafeMutablePointer<Void>) -> Int)>, context context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func sortUsingFunction(_ compare: (AnyObject, AnyObject, UnsafeMutablePointer<Void>) -> Int, context context: UnsafeMutablePointer<Void>) ``` |

Modified [NSMutableAttributedString](https://developer.apple.com/documentation/foundation/nsmutableattributedstring)

|  | Declaration |
| --- | --- |
| From | ``` class NSMutableAttributedString : NSAttributedString {     func replaceCharactersInRange(_ range: NSRange, withString str: String)     func setAttributes(_ attrs: [NSObject : AnyObject]?, range range: NSRange) } extension NSMutableAttributedString {     var mutableString: NSMutableString { get }     func addAttribute(_ name: String, value value: AnyObject, range range: NSRange)     func addAttributes(_ attrs: [NSObject : AnyObject], range range: NSRange)     func removeAttribute(_ name: String, range range: NSRange)     func replaceCharactersInRange(_ range: NSRange, withAttributedString attrString: NSAttributedString)     func insertAttributedString(_ attrString: NSAttributedString, atIndex loc: Int)     func appendAttributedString(_ attrString: NSAttributedString)     func deleteCharactersInRange(_ range: NSRange)     func setAttributedString(_ attrString: NSAttributedString)     func beginEditing()     func endEditing() } extension NSMutableAttributedString {     func fixAttributesInRange(_ range: NSRange) } extension NSMutableAttributedString {     func readFromFileURL(_ url: NSURL!, options opts: [NSObject : AnyObject]!, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>, error error: NSErrorPointer) -> Bool     func readFromData(_ data: NSData, options opts: [NSObject : AnyObject]?, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>, error error: NSErrorPointer) -> Bool } ``` |
| To | ``` class NSMutableAttributedString : NSAttributedString {     func replaceCharactersInRange(_ range: NSRange, withString str: String)     func setAttributes(_ attrs: [String : AnyObject]?, range range: NSRange) } extension NSMutableAttributedString {     var mutableString: NSMutableString { get }     func addAttribute(_ name: String, value value: AnyObject, range range: NSRange)     func addAttributes(_ attrs: [String : AnyObject], range range: NSRange)     func removeAttribute(_ name: String, range range: NSRange)     func replaceCharactersInRange(_ range: NSRange, withAttributedString attrString: NSAttributedString)     func insertAttributedString(_ attrString: NSAttributedString, atIndex loc: Int)     func appendAttributedString(_ attrString: NSAttributedString)     func deleteCharactersInRange(_ range: NSRange)     func setAttributedString(_ attrString: NSAttributedString)     func beginEditing()     func endEditing() } extension NSMutableAttributedString {     func fixAttributesInRange(_ range: NSRange) } extension NSMutableAttributedString {     func readFromURL(_ url: NSURL, options opts: [String : AnyObject], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws     func readFromData(_ data: NSData, options opts: [String : AnyObject], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws } extension NSMutableAttributedString {     func readFromFileURL(_ url: NSURL, options opts: [NSObject : AnyObject], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws } ``` |

Modified [NSMutableAttributedString.addAttributes(_: [String : AnyObject], range: NSRange)](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1414304-addattributes)

|  | Declaration |
| --- | --- |
| From | ``` func addAttributes(_ attrs: [NSObject : AnyObject], range range: NSRange) ``` |
| To | ``` func addAttributes(_ attrs: [String : AnyObject], range range: NSRange) ``` |

Modified [NSMutableAttributedString.setAttributes(_: [String : AnyObject]?, range: NSRange)](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1412179-setattributes)

|  | Declaration |
| --- | --- |
| From | ``` func setAttributes(_ attrs: [NSObject : AnyObject]?, range range: NSRange) ``` |
| To | ``` func setAttributes(_ attrs: [String : AnyObject]?, range range: NSRange) ``` |

Modified [NSMutableCharacterSet](https://developer.apple.com/documentation/foundation/nsmutablecharacterset)

|  | Declaration |
| --- | --- |
| From | ``` class NSMutableCharacterSet : NSCharacterSet, NSCopying, NSMutableCopying {     func addCharactersInRange(_ aRange: NSRange)     func removeCharactersInRange(_ aRange: NSRange)     func addCharactersInString(_ aString: String)     func removeCharactersInString(_ aString: String)     func formUnionWithCharacterSet(_ otherSet: NSCharacterSet)     func formIntersectionWithCharacterSet(_ otherSet: NSCharacterSet)     func invert()     class func controlCharacterSet() -> NSMutableCharacterSet     class func whitespaceCharacterSet() -> NSMutableCharacterSet     class func whitespaceAndNewlineCharacterSet() -> NSMutableCharacterSet     class func decimalDigitCharacterSet() -> NSMutableCharacterSet     class func letterCharacterSet() -> NSMutableCharacterSet     class func lowercaseLetterCharacterSet() -> NSMutableCharacterSet     class func uppercaseLetterCharacterSet() -> NSMutableCharacterSet     class func nonBaseCharacterSet() -> NSMutableCharacterSet     class func alphanumericCharacterSet() -> NSMutableCharacterSet     class func decomposableCharacterSet() -> NSMutableCharacterSet     class func illegalCharacterSet() -> NSMutableCharacterSet     class func punctuationCharacterSet() -> NSMutableCharacterSet     class func capitalizedLetterCharacterSet() -> NSMutableCharacterSet     class func symbolCharacterSet() -> NSMutableCharacterSet     class func newlineCharacterSet() -> NSMutableCharacterSet     init(range aRange: NSRange) -> NSMutableCharacterSet     class func characterSetWithRange(_ aRange: NSRange) -> NSMutableCharacterSet     init(charactersInString aString: String) -> NSMutableCharacterSet     class func characterSetWithCharactersInString(_ aString: String) -> NSMutableCharacterSet     init(bitmapRepresentation data: NSData) -> NSMutableCharacterSet     class func characterSetWithBitmapRepresentation(_ data: NSData) -> NSMutableCharacterSet     init?(contentsOfFile fName: String) -> NSMutableCharacterSet     class func characterSetWithContentsOfFile(_ fName: String) -> NSMutableCharacterSet? } ``` |
| To | ``` class NSMutableCharacterSet : NSCharacterSet {     func addCharactersInRange(_ aRange: NSRange)     func removeCharactersInRange(_ aRange: NSRange)     func addCharactersInString(_ aString: String)     func removeCharactersInString(_ aString: String)     func formUnionWithCharacterSet(_ otherSet: NSCharacterSet)     func formIntersectionWithCharacterSet(_ otherSet: NSCharacterSet)     func invert()     class func controlCharacterSet() -> NSMutableCharacterSet     class func whitespaceCharacterSet() -> NSMutableCharacterSet     class func whitespaceAndNewlineCharacterSet() -> NSMutableCharacterSet     class func decimalDigitCharacterSet() -> NSMutableCharacterSet     class func letterCharacterSet() -> NSMutableCharacterSet     class func lowercaseLetterCharacterSet() -> NSMutableCharacterSet     class func uppercaseLetterCharacterSet() -> NSMutableCharacterSet     class func nonBaseCharacterSet() -> NSMutableCharacterSet     class func alphanumericCharacterSet() -> NSMutableCharacterSet     class func decomposableCharacterSet() -> NSMutableCharacterSet     class func illegalCharacterSet() -> NSMutableCharacterSet     class func punctuationCharacterSet() -> NSMutableCharacterSet     class func capitalizedLetterCharacterSet() -> NSMutableCharacterSet     class func symbolCharacterSet() -> NSMutableCharacterSet     class func newlineCharacterSet() -> NSMutableCharacterSet      init(range aRange: NSRange)     class func characterSetWithRange(_ aRange: NSRange) -> NSMutableCharacterSet      init(charactersInString aString: String)     class func characterSetWithCharactersInString(_ aString: String) -> NSMutableCharacterSet      init(bitmapRepresentation data: NSData)     class func characterSetWithBitmapRepresentation(_ data: NSData) -> NSMutableCharacterSet      init?(contentsOfFile fName: String)     class func characterSetWithContentsOfFile(_ fName: String) -> NSMutableCharacterSet? } ``` |

Modified [NSMutableCharacterSet.init(bitmapRepresentation: NSData)](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/1415715-charactersetwithbitmaprepresenta)

|  | Declaration |
| --- | --- |
| From | ``` init(bitmapRepresentation data: NSData) -> NSMutableCharacterSet ``` |
| To | ``` init(bitmapRepresentation data: NSData) ``` |

Modified [NSMutableCharacterSet.init(charactersInString: String)](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/1415362-init)

|  | Declaration |
| --- | --- |
| From | ``` init(charactersInString aString: String) -> NSMutableCharacterSet ``` |
| To | ``` init(charactersInString aString: String) ``` |

Modified [NSMutableCharacterSet.init(contentsOfFile: String)](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/1414233-init)

|  | Declaration |
| --- | --- |
| From | ``` init?(contentsOfFile fName: String) -> NSMutableCharacterSet ``` |
| To | ``` init?(contentsOfFile fName: String) ``` |

Modified [NSMutableCharacterSet.init(range: NSRange)](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/1410070-charactersetwithrange)

|  | Declaration |
| --- | --- |
| From | ``` init(range aRange: NSRange) -> NSMutableCharacterSet ``` |
| To | ``` init(range aRange: NSRange) ``` |

Modified [NSMutableCopying](https://developer.apple.com/documentation/foundation/nsmutablecopying)

|  | Declaration |
| --- | --- |
| From | ``` protocol NSMutableCopying {     func mutableCopyWithZone(_ zone: NSZone) -> AnyObject? } ``` |
| To | ``` protocol NSMutableCopying {     func mutableCopyWithZone(_ zone: NSZone) -> AnyObject } ``` |

Modified [NSMutableCopying.mutableCopyWithZone(_: NSZone) -> AnyObject](https://developer.apple.com/documentation/foundation/nsmutablecopying/1414175-mutablecopywithzone)

|  | Declaration |
| --- | --- |
| From | ``` func mutableCopyWithZone(_ zone: NSZone) -> AnyObject? ``` |
| To | ``` func mutableCopyWithZone(_ zone: NSZone) -> AnyObject ``` |

Modified [NSMutableData](https://developer.apple.com/documentation/foundation/nsmutabledata)

|  | Declaration |
| --- | --- |
| From | ``` class NSMutableData : NSData {     var mutableBytes: UnsafeMutablePointer<Void> { get }     var length: Int } extension NSMutableData {     func appendBytes(_ bytes: UnsafePointer<Void>, length length: Int)     func appendData(_ other: NSData)     func increaseLengthBy(_ extraLength: Int)     func replaceBytesInRange(_ range: NSRange, withBytes bytes: UnsafePointer<Void>)     func resetBytesInRange(_ range: NSRange)     func setData(_ data: NSData)     func replaceBytesInRange(_ range: NSRange, withBytes replacementBytes: UnsafePointer<Void>, length replacementLength: Int) } extension NSMutableData {     convenience init!(capacity aNumItems: Int)     class func dataWithCapacity(_ aNumItems: Int) -> Self!     convenience init!(length length: Int)     class func dataWithLength(_ length: Int) -> Self!     init?(capacity capacity: Int)     init?(length length: Int) } ``` |
| To | ``` class NSMutableData : NSData {     var mutableBytes: UnsafeMutablePointer<Void> { get }     var length: Int } extension NSMutableData {     func appendBytes(_ bytes: UnsafePointer<Void>, length length: Int)     func appendData(_ other: NSData)     func increaseLengthBy(_ extraLength: Int)     func replaceBytesInRange(_ range: NSRange, withBytes bytes: UnsafePointer<Void>)     func resetBytesInRange(_ range: NSRange)     func setData(_ data: NSData)     func replaceBytesInRange(_ range: NSRange, withBytes replacementBytes: UnsafePointer<Void>, length replacementLength: Int) } extension NSMutableData {     convenience init?(capacity aNumItems: Int)     class func dataWithCapacity(_ aNumItems: Int) -> Self?     convenience init?(length length: Int)     class func dataWithLength(_ length: Int) -> Self?     init?(capacity capacity: Int)     init?(length length: Int) } ``` |

Modified [NSMutableDictionary](https://developer.apple.com/documentation/foundation/nsmutabledictionary)

|  | Declaration |
| --- | --- |
| From | ``` class NSMutableDictionary : NSDictionary {     func removeObjectForKey(_ aKey: AnyObject)     func setObject(_ anObject: AnyObject, forKey aKey: NSCopying)     init()     init(capacity numItems: Int)     init?(coder aDecoder: NSCoder) } extension NSMutableDictionary {     func addEntriesFromDictionary(_ otherDictionary: [NSObject : AnyObject])     func removeAllObjects()     func removeObjectsForKeys(_ keyArray: [AnyObject])     func setDictionary(_ otherDictionary: [NSObject : AnyObject])     subscript (key: NSCopying) -> AnyObject?     func setObject(_ obj: AnyObject?, forKeyedSubscript key: NSCopying) } extension NSMutableDictionary {     convenience init!(capacity numItems: Int)     class func dictionaryWithCapacity(_ numItems: Int) -> Self!     init?(contentsOfFile path: String) -> NSMutableDictionary     class func dictionaryWithContentsOfFile(_ path: String) -> NSMutableDictionary?     init?(contentsOfURL url: NSURL) -> NSMutableDictionary     class func dictionaryWithContentsOfURL(_ url: NSURL) -> NSMutableDictionary?     convenience init?(contentsOfFile path: String)     convenience init?(contentsOfURL url: NSURL) } extension NSMutableDictionary {     init(sharedKeySet keyset: AnyObject) -> NSMutableDictionary     class func dictionaryWithSharedKeySet(_ keyset: AnyObject) -> NSMutableDictionary } extension NSMutableDictionary {     func setValue(_ value: AnyObject?, forKey key: String) } ``` |
| To | ``` class NSMutableDictionary : NSDictionary {     func removeObjectForKey(_ aKey: AnyObject)     func setObject(_ anObject: AnyObject, forKey aKey: NSCopying)     init()     init(capacity numItems: Int)     init?(coder aDecoder: NSCoder) } extension NSMutableDictionary {     func addEntriesFromDictionary(_ otherDictionary: [NSObject : AnyObject])     func removeAllObjects()     func removeObjectsForKeys(_ keyArray: [AnyObject])     func setDictionary(_ otherDictionary: [NSObject : AnyObject])     subscript (_ key: NSCopying) -> AnyObject?     func setObject(_ obj: AnyObject?, forKeyedSubscript key: NSCopying) } extension NSMutableDictionary {     convenience init(capacity numItems: Int)     class func dictionaryWithCapacity(_ numItems: Int) -> Self      init?(contentsOfFile path: String)     class func dictionaryWithContentsOfFile(_ path: String) -> NSMutableDictionary?      init?(contentsOfURL url: NSURL)     class func dictionaryWithContentsOfURL(_ url: NSURL) -> NSMutableDictionary?     convenience init?(contentsOfFile path: String)     convenience init?(contentsOfURL url: NSURL) } extension NSMutableDictionary {      init(sharedKeySet keyset: AnyObject)     class func dictionaryWithSharedKeySet(_ keyset: AnyObject) -> NSMutableDictionary } extension NSMutableDictionary {     func setValue(_ value: AnyObject?, forKey key: String) } ``` |

Modified [NSMutableDictionary.init(sharedKeySet: AnyObject)](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1412658-init)

|  | Declaration |
| --- | --- |
| From | ``` init(sharedKeySet keyset: AnyObject) -> NSMutableDictionary ``` |
| To | ``` init(sharedKeySet keyset: AnyObject) ``` |

Modified [NSMutableOrderedSet](https://developer.apple.com/documentation/foundation/nsmutableorderedset)

|  | Declaration |
| --- | --- |
| From | ``` class NSMutableOrderedSet : NSOrderedSet {     func insertObject(_ object: AnyObject, atIndex idx: Int)     func removeObjectAtIndex(_ idx: Int)     func replaceObjectAtIndex(_ idx: Int, withObject object: AnyObject)     init?(coder aDecoder: NSCoder)     init()     init(capacity numItems: Int) } extension NSMutableOrderedSet {     func addObject(_ object: AnyObject)     func addObjects(_ objects: UnsafePointer<AnyObject?>, count count: Int)     func addObjectsFromArray(_ array: [AnyObject])     func exchangeObjectAtIndex(_ idx1: Int, withObjectAtIndex idx2: Int)     func moveObjectsAtIndexes(_ indexes: NSIndexSet, toIndex idx: Int)     func insertObjects(_ objects: [AnyObject], atIndexes indexes: NSIndexSet)     func setObject(_ obj: AnyObject, atIndex idx: Int)     subscript (idx: Int) -> AnyObject     func setObject(_ obj: AnyObject, atIndexedSubscript idx: Int)     func replaceObjectsInRange(_ range: NSRange, withObjects objects: UnsafePointer<AnyObject?>, count count: Int)     func replaceObjectsAtIndexes(_ indexes: NSIndexSet, withObjects objects: [AnyObject])     func removeObjectsInRange(_ range: NSRange)     func removeObjectsAtIndexes(_ indexes: NSIndexSet)     func removeAllObjects()     func removeObject(_ object: AnyObject)     func removeObjectsInArray(_ array: [AnyObject])     func intersectOrderedSet(_ other: NSOrderedSet)     func minusOrderedSet(_ other: NSOrderedSet)     func unionOrderedSet(_ other: NSOrderedSet)     func intersectSet(_ other: Set<NSObject>)     func minusSet(_ other: Set<NSObject>)     func unionSet(_ other: Set<NSObject>)     func sortUsingComparator(_ cmptr: NSComparator)     func sortWithOptions(_ opts: NSSortOptions, usingComparator cmptr: NSComparator)     func sortRange(_ range: NSRange, options opts: NSSortOptions, usingComparator cmptr: NSComparator) } extension NSMutableOrderedSet {     convenience init!(capacity numItems: Int)     class func orderedSetWithCapacity(_ numItems: Int) -> Self! } extension NSMutableOrderedSet {     func filterUsingPredicate(_ p: NSPredicate) } extension NSMutableOrderedSet {     func sortUsingDescriptors(_ sortDescriptors: [AnyObject]) } ``` |
| To | ``` class NSMutableOrderedSet : NSOrderedSet {     func insertObject(_ object: AnyObject, atIndex idx: Int)     func removeObjectAtIndex(_ idx: Int)     func replaceObjectAtIndex(_ idx: Int, withObject object: AnyObject)     init?(coder aDecoder: NSCoder)     init()     init(capacity numItems: Int) } extension NSMutableOrderedSet {     func addObject(_ object: AnyObject)     func addObjects(_ objects: UnsafePointer<AnyObject?>, count count: Int)     func addObjectsFromArray(_ array: [AnyObject])     func exchangeObjectAtIndex(_ idx1: Int, withObjectAtIndex idx2: Int)     func moveObjectsAtIndexes(_ indexes: NSIndexSet, toIndex idx: Int)     func insertObjects(_ objects: [AnyObject], atIndexes indexes: NSIndexSet)     func setObject(_ obj: AnyObject, atIndex idx: Int)     subscript (_ idx: Int) -> AnyObject     func setObject(_ obj: AnyObject, atIndexedSubscript idx: Int)     func replaceObjectsInRange(_ range: NSRange, withObjects objects: UnsafePointer<AnyObject?>, count count: Int)     func replaceObjectsAtIndexes(_ indexes: NSIndexSet, withObjects objects: [AnyObject])     func removeObjectsInRange(_ range: NSRange)     func removeObjectsAtIndexes(_ indexes: NSIndexSet)     func removeAllObjects()     func removeObject(_ object: AnyObject)     func removeObjectsInArray(_ array: [AnyObject])     func intersectOrderedSet(_ other: NSOrderedSet)     func minusOrderedSet(_ other: NSOrderedSet)     func unionOrderedSet(_ other: NSOrderedSet)     func intersectSet(_ other: Set<NSObject>)     func minusSet(_ other: Set<NSObject>)     func unionSet(_ other: Set<NSObject>)     func sortUsingComparator(_ cmptr: NSComparator)     func sortWithOptions(_ opts: NSSortOptions, usingComparator cmptr: NSComparator)     func sortRange(_ range: NSRange, options opts: NSSortOptions, usingComparator cmptr: NSComparator) } extension NSMutableOrderedSet {     convenience init(capacity numItems: Int)     class func orderedSetWithCapacity(_ numItems: Int) -> Self } extension NSMutableOrderedSet {     func filterUsingPredicate(_ p: NSPredicate) } extension NSMutableOrderedSet {     func sortUsingDescriptors(_ sortDescriptors: [NSSortDescriptor]) } ``` |

Modified [NSMutableOrderedSet.sortUsingDescriptors(_: [NSSortDescriptor])](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1410023-sortusingdescriptors)

|  | Declaration |
| --- | --- |
| From | ``` func sortUsingDescriptors(_ sortDescriptors: [AnyObject]) ``` |
| To | ``` func sortUsingDescriptors(_ sortDescriptors: [NSSortDescriptor]) ``` |

Modified [NSMutableSet](https://developer.apple.com/documentation/foundation/nsmutableset)

|  | Declaration |
| --- | --- |
| From | ``` class NSMutableSet : NSSet {     func addObject(_ object: AnyObject)     func removeObject(_ object: AnyObject)     init?(coder aDecoder: NSCoder)     init()     init(capacity numItems: Int) } extension NSMutableSet {     func filterUsingPredicate(_ predicate: NSPredicate) } extension NSMutableSet {     func addObjectsFromArray(_ array: [AnyObject])     func intersectSet(_ otherSet: Set<NSObject>)     func minusSet(_ otherSet: Set<NSObject>)     func removeAllObjects()     func unionSet(_ otherSet: Set<NSObject>)     func setSet(_ otherSet: Set<NSObject>) } extension NSMutableSet {     convenience init!(capacity numItems: Int)     class func setWithCapacity(_ numItems: Int) -> Self! } ``` |
| To | ``` class NSMutableSet : NSSet {     func addObject(_ object: AnyObject)     func removeObject(_ object: AnyObject)     init?(coder aDecoder: NSCoder)     init()     init(capacity numItems: Int) } extension NSMutableSet {     func filterUsingPredicate(_ predicate: NSPredicate) } extension NSMutableSet {     func addObjectsFromArray(_ array: [AnyObject])     func intersectSet(_ otherSet: Set<NSObject>)     func minusSet(_ otherSet: Set<NSObject>)     func removeAllObjects()     func unionSet(_ otherSet: Set<NSObject>)     func setSet(_ otherSet: Set<NSObject>) } extension NSMutableSet {     convenience init(capacity numItems: Int)     class func setWithCapacity(_ numItems: Int) -> Self } ``` |

Modified [NSMutableString](https://developer.apple.com/documentation/foundation/nsmutablestring)

|  | Declaration |
| --- | --- |
| From | ``` class NSMutableString : NSString {     func replaceCharactersInRange(_ range: NSRange, withString aString: String) } extension NSMutableString {     func appendFormat(_ format: NSString, _ args: CVarArgType...) } extension NSMutableString {     func insertString(_ aString: String, atIndex loc: Int)     func deleteCharactersInRange(_ range: NSRange)     func appendString(_ aString: String)     func setString(_ aString: String)     init(capacity capacity: Int)     class func stringWithCapacity(_ capacity: Int) -> NSMutableString     func replaceOccurrencesOfString(_ target: String, withString replacement: String, options options: NSStringCompareOptions, range searchRange: NSRange) -> Int } extension NSMutableString {     func appendFormat(_ format: NSString, _ args: CVarArgType...) } ``` |
| To | ``` class NSMutableString : NSString {     func replaceCharactersInRange(_ range: NSRange, withString aString: String) } extension NSMutableString {     func appendFormat(_ format: NSString, _ args: CVarArgType...) } extension NSMutableString {     func insertString(_ aString: String, atIndex loc: Int)     func deleteCharactersInRange(_ range: NSRange)     func appendString(_ aString: String)     func setString(_ aString: String)     func replaceOccurrencesOfString(_ target: String, withString replacement: String, options options: NSStringCompareOptions, range searchRange: NSRange) -> Int     func applyTransform(_ transform: String, reverse reverse: Bool, range range: NSRange, updatedRange resultingRange: NSRangePointer) -> Bool     init(capacity capacity: Int)     class func stringWithCapacity(_ capacity: Int) -> NSMutableString } extension NSMutableString {     func appendFormat(_ format: NSString, _ args: CVarArgType...) } ``` |

Modified [NSMutableURLRequest](https://developer.apple.com/documentation/foundation/nsmutableurlrequest)

|  | Declaration |
| --- | --- |
| From | ``` class NSMutableURLRequest : NSURLRequest {     @NSCopying var URL: NSURL?     var cachePolicy: NSURLRequestCachePolicy     var timeoutInterval: NSTimeInterval     @NSCopying var mainDocumentURL: NSURL?     var networkServiceType: NSURLRequestNetworkServiceType     var allowsCellularAccess: Bool } extension NSMutableURLRequest {     var HTTPMethod: String     var allHTTPHeaderFields: [NSObject : AnyObject]?     func setValue(_ value: String?, forHTTPHeaderField field: String)     func addValue(_ value: String?, forHTTPHeaderField field: String)     @NSCopying var HTTPBody: NSData?     var HTTPBodyStream: NSInputStream?     var HTTPShouldHandleCookies: Bool     var HTTPShouldUsePipelining: Bool } ``` |
| To | ``` class NSMutableURLRequest : NSURLRequest {     @NSCopying var URL: NSURL?     var cachePolicy: NSURLRequestCachePolicy     var timeoutInterval: NSTimeInterval     @NSCopying var mainDocumentURL: NSURL?     var networkServiceType: NSURLRequestNetworkServiceType     var allowsCellularAccess: Bool } extension NSMutableURLRequest {     var HTTPMethod: String     var allHTTPHeaderFields: [String : String]?     func setValue(_ value: String?, forHTTPHeaderField field: String)     func addValue(_ value: String, forHTTPHeaderField field: String)     @NSCopying var HTTPBody: NSData?     var HTTPBodyStream: NSInputStream?     var HTTPShouldHandleCookies: Bool     var HTTPShouldUsePipelining: Bool } extension NSMutableURLRequest {     func bindToHotspotHelperCommand(_ command: NEHotspotHelperCommand) } ``` |

Modified [NSMutableURLRequest.addValue(_: String, forHTTPHeaderField: String)](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1407676-addvalue)

|  | Declaration |
| --- | --- |
| From | ``` func addValue(_ value: String?, forHTTPHeaderField field: String) ``` |
| To | ``` func addValue(_ value: String, forHTTPHeaderField field: String) ``` |

Modified [NSMutableURLRequest.allHTTPHeaderFields](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1414617-allhttpheaderfields)

|  | Declaration |
| --- | --- |
| From | ``` var allHTTPHeaderFields: [NSObject : AnyObject]? ``` |
| To | ``` var allHTTPHeaderFields: [String : String]? ``` |

Modified [NSNetService](https://developer.apple.com/documentation/foundation/netservice)

|  | Declaration |
| --- | --- |
| From | ``` class NSNetService : NSObject {     init!(domain domain: String, type type: String, name name: String, port port: Int32)     convenience init!(domain domain: String, type type: String, name name: String)     func scheduleInRunLoop(_ aRunLoop: NSRunLoop, forMode mode: String)     func removeFromRunLoop(_ aRunLoop: NSRunLoop, forMode mode: String)     unowned(unsafe) var delegate: NSNetServiceDelegate?     var includesPeerToPeer: Bool     var name: String { get }     var type: String { get }     var domain: String! { get }     var hostName: String? { get }     var addresses: [AnyObject]? { get }     var port: Int { get }     func publish()     func publishWithOptions(_ options: NSNetServiceOptions)     func resolve()     func stop()     class func dictionaryFromTXTRecordData(_ txtData: NSData) -> [NSObject : AnyObject]     class func dataFromTXTRecordDictionary(_ txtDictionary: [NSObject : AnyObject]) -> NSData     func resolveWithTimeout(_ timeout: NSTimeInterval)     func getInputStream(_ inputStream: UnsafeMutablePointer<NSInputStream?>, outputStream outputStream: UnsafeMutablePointer<NSOutputStream?>) -> Bool     func setTXTRecordData(_ recordData: NSData!) -> Bool     func TXTRecordData() -> NSData!     func startMonitoring()     func stopMonitoring() } ``` |
| To | ``` class NSNetService : NSObject {     init(domain domain: String, type type: String, name name: String, port port: Int32)     convenience init(domain domain: String, type type: String, name name: String)     func scheduleInRunLoop(_ aRunLoop: NSRunLoop, forMode mode: String)     func removeFromRunLoop(_ aRunLoop: NSRunLoop, forMode mode: String)     unowned(unsafe) var delegate: NSNetServiceDelegate?     var includesPeerToPeer: Bool     var name: String { get }     var type: String { get }     var domain: String { get }     var hostName: String? { get }     var addresses: [NSData]? { get }     var port: Int { get }     func publish()     func publishWithOptions(_ options: NSNetServiceOptions)     func resolve()     func stop()     class func dictionaryFromTXTRecordData(_ txtData: NSData) -> [String : NSData]     class func dataFromTXTRecordDictionary(_ txtDictionary: [String : NSData]) -> NSData     func resolveWithTimeout(_ timeout: NSTimeInterval)     func getInputStream(_ inputStream: UnsafeMutablePointer<NSInputStream?>, outputStream outputStream: UnsafeMutablePointer<NSOutputStream?>) -> Bool     func setTXTRecordData(_ recordData: NSData?) -> Bool     func TXTRecordData() -> NSData?     func startMonitoring()     func stopMonitoring() } ``` |

Modified [NSNetService.addresses](https://developer.apple.com/documentation/foundation/netservice/1408528-addresses)

|  | Declaration |
| --- | --- |
| From | ``` var addresses: [AnyObject]? { get } ``` |
| To | ``` var addresses: [NSData]? { get } ``` |

Modified [NSNetService.dataFromTXTRecordDictionary(_: [String : NSData]) -> NSData [class]](https://developer.apple.com/documentation/foundation/nsnetservice/1413150-datafromtxtrecorddictionary)

|  | Declaration |
| --- | --- |
| From | ``` class func dataFromTXTRecordDictionary(_ txtDictionary: [NSObject : AnyObject]) -> NSData ``` |
| To | ``` class func dataFromTXTRecordDictionary(_ txtDictionary: [String : NSData]) -> NSData ``` |

Modified [NSNetService.dictionaryFromTXTRecordData(_: NSData) -> [String : NSData] [class]](https://developer.apple.com/documentation/foundation/nsnetservice/1408164-dictionaryfromtxtrecorddata)

|  | Declaration |
| --- | --- |
| From | ``` class func dictionaryFromTXTRecordData(_ txtData: NSData) -> [NSObject : AnyObject] ``` |
| To | ``` class func dictionaryFromTXTRecordData(_ txtData: NSData) -> [String : NSData] ``` |

Modified [NSNetService.domain](https://developer.apple.com/documentation/foundation/netservice/1414495-domain)

|  | Declaration |
| --- | --- |
| From | ``` var domain: String! { get } ``` |
| To | ``` var domain: String { get } ``` |

Modified [NSNetService.init(domain: String, type: String, name: String)](https://developer.apple.com/documentation/foundation/nsnetservice/1417615-initwithdomain)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(domain domain: String, type type: String, name name: String) ``` |
| To | ``` convenience init(domain domain: String, type type: String, name name: String) ``` |

Modified [NSNetService.init(domain: String, type: String, name: String, port: Int32)](https://developer.apple.com/documentation/foundation/netservice/1413364-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(domain domain: String, type type: String, name name: String, port port: Int32) ``` |
| To | ``` init(domain domain: String, type type: String, name name: String, port port: Int32) ``` |

Modified [NSNetService.setTXTRecordData(_: NSData?) -> Bool](https://developer.apple.com/documentation/foundation/nsnetservice/1410648-settxtrecorddata)

|  | Declaration |
| --- | --- |
| From | ``` func setTXTRecordData(_ recordData: NSData!) -> Bool ``` |
| To | ``` func setTXTRecordData(_ recordData: NSData?) -> Bool ``` |

Modified [NSNetService.TXTRecordData() -> NSData?](https://developer.apple.com/documentation/foundation/nsnetservice/1417698-txtrecorddata)

|  | Declaration |
| --- | --- |
| From | ``` func TXTRecordData() -> NSData! ``` |
| To | ``` func TXTRecordData() -> NSData? ``` |

Modified [NSNetServiceBrowserDelegate](https://developer.apple.com/documentation/foundation/nsnetservicebrowserdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol NSNetServiceBrowserDelegate : NSObjectProtocol {     optional func netServiceBrowserWillSearch(_ aNetServiceBrowser: NSNetServiceBrowser)     optional func netServiceBrowserDidStopSearch(_ aNetServiceBrowser: NSNetServiceBrowser)     optional func netServiceBrowser(_ aNetServiceBrowser: NSNetServiceBrowser, didNotSearch errorDict: [NSObject : AnyObject])     optional func netServiceBrowser(_ aNetServiceBrowser: NSNetServiceBrowser, didFindDomain domainString: String, moreComing moreComing: Bool)     optional func netServiceBrowser(_ aNetServiceBrowser: NSNetServiceBrowser, didFindService aNetService: NSNetService, moreComing moreComing: Bool)     optional func netServiceBrowser(_ aNetServiceBrowser: NSNetServiceBrowser, didRemoveDomain domainString: String, moreComing moreComing: Bool)     optional func netServiceBrowser(_ aNetServiceBrowser: NSNetServiceBrowser, didRemoveService aNetService: NSNetService, moreComing moreComing: Bool) } ``` |
| To | ``` protocol NSNetServiceBrowserDelegate : NSObjectProtocol {     optional func netServiceBrowserWillSearch(_ browser: NSNetServiceBrowser)     optional func netServiceBrowserDidStopSearch(_ browser: NSNetServiceBrowser)     optional func netServiceBrowser(_ browser: NSNetServiceBrowser, didNotSearch errorDict: [String : NSNumber])     optional func netServiceBrowser(_ browser: NSNetServiceBrowser, didFindDomain domainString: String, moreComing moreComing: Bool)     optional func netServiceBrowser(_ browser: NSNetServiceBrowser, didFindService service: NSNetService, moreComing moreComing: Bool)     optional func netServiceBrowser(_ browser: NSNetServiceBrowser, didRemoveDomain domainString: String, moreComing moreComing: Bool)     optional func netServiceBrowser(_ browser: NSNetServiceBrowser, didRemoveService service: NSNetService, moreComing moreComing: Bool) } ``` |

Modified [NSNetServiceBrowserDelegate.netServiceBrowser(_: NSNetServiceBrowser, didNotSearch: [String : NSNumber])](https://developer.apple.com/documentation/foundation/netservicebrowserdelegate/1410567-netservicebrowser)

|  | Declaration |
| --- | --- |
| From | ``` optional func netServiceBrowser(_ aNetServiceBrowser: NSNetServiceBrowser, didNotSearch errorDict: [NSObject : AnyObject]) ``` |
| To | ``` optional func netServiceBrowser(_ browser: NSNetServiceBrowser, didNotSearch errorDict: [String : NSNumber]) ``` |

Modified [NSNetServiceDelegate](https://developer.apple.com/documentation/foundation/nsnetservicedelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol NSNetServiceDelegate : NSObjectProtocol {     optional func netServiceWillPublish(_ sender: NSNetService)     optional func netServiceDidPublish(_ sender: NSNetService)     optional func netService(_ sender: NSNetService, didNotPublish errorDict: [NSObject : AnyObject])     optional func netServiceWillResolve(_ sender: NSNetService)     optional func netServiceDidResolveAddress(_ sender: NSNetService)     optional func netService(_ sender: NSNetService, didNotResolve errorDict: [NSObject : AnyObject])     optional func netServiceDidStop(_ sender: NSNetService)     optional func netService(_ sender: NSNetService, didUpdateTXTRecordData data: NSData)     optional func netService(_ sender: NSNetService, didAcceptConnectionWithInputStream inputStream: NSInputStream, outputStream outputStream: NSOutputStream) } ``` |
| To | ``` protocol NSNetServiceDelegate : NSObjectProtocol {     optional func netServiceWillPublish(_ sender: NSNetService)     optional func netServiceDidPublish(_ sender: NSNetService)     optional func netService(_ sender: NSNetService, didNotPublish errorDict: [String : NSNumber])     optional func netServiceWillResolve(_ sender: NSNetService)     optional func netServiceDidResolveAddress(_ sender: NSNetService)     optional func netService(_ sender: NSNetService, didNotResolve errorDict: [String : NSNumber])     optional func netServiceDidStop(_ sender: NSNetService)     optional func netService(_ sender: NSNetService, didUpdateTXTRecordData data: NSData)     optional func netService(_ sender: NSNetService, didAcceptConnectionWithInputStream inputStream: NSInputStream, outputStream outputStream: NSOutputStream) } ``` |

Modified [NSNetServiceDelegate.netService(_: NSNetService, didNotPublish: [String : NSNumber])](https://developer.apple.com/documentation/foundation/netservicedelegate/1417101-netservice)

|  | Declaration |
| --- | --- |
| From | ``` optional func netService(_ sender: NSNetService, didNotPublish errorDict: [NSObject : AnyObject]) ``` |
| To | ``` optional func netService(_ sender: NSNetService, didNotPublish errorDict: [String : NSNumber]) ``` |

Modified [NSNetServiceDelegate.netService(_: NSNetService, didNotResolve: [String : NSNumber])](https://developer.apple.com/documentation/foundation/netservicedelegate/1414161-netservice)

|  | Declaration |
| --- | --- |
| From | ``` optional func netService(_ sender: NSNetService, didNotResolve errorDict: [NSObject : AnyObject]) ``` |
| To | ``` optional func netService(_ sender: NSNetService, didNotResolve errorDict: [String : NSNumber]) ``` |

Modified [NSNetServiceOptions [struct]](https://developer.apple.com/documentation/foundation/nsnetserviceoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSNetServiceOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var NoAutoRename: NSNetServiceOptions { get }     static var ListenForConnections: NSNetServiceOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSNetServiceOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var NoAutoRename: NSNetServiceOptions { get }     static var ListenForConnections: NSNetServiceOptions { get } } ``` | OptionSetType |

Modified [NSNetServicesError [enum]](https://developer.apple.com/documentation/foundation/netservice/errorcode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NSNotificationCenter](https://developer.apple.com/documentation/foundation/notificationcenter)

|  | Declaration |
| --- | --- |
| From | ``` class NSNotificationCenter : NSObject {     class func defaultCenter() -> NSNotificationCenter     func addObserver(_ observer: AnyObject, selector aSelector: Selector, name aName: String?, object anObject: AnyObject?)     func postNotification(_ notification: NSNotification)     func postNotificationName(_ aName: String, object anObject: AnyObject?)     func postNotificationName(_ aName: String, object anObject: AnyObject?, userInfo aUserInfo: [NSObject : AnyObject]?)     func removeObserver(_ observer: AnyObject)     func removeObserver(_ observer: AnyObject, name aName: String?, object anObject: AnyObject?)     func addObserverForName(_ name: String?, object obj: AnyObject?, queue queue: NSOperationQueue?, usingBlock block: (NSNotification!) -> Void) -> NSObjectProtocol } ``` |
| To | ``` class NSNotificationCenter : NSObject {     class func defaultCenter() -> NSNotificationCenter     func addObserver(_ observer: AnyObject, selector aSelector: Selector, name aName: String?, object anObject: AnyObject?)     func postNotification(_ notification: NSNotification)     func postNotificationName(_ aName: String, object anObject: AnyObject?)     func postNotificationName(_ aName: String, object anObject: AnyObject?, userInfo aUserInfo: [NSObject : AnyObject]?)     func removeObserver(_ observer: AnyObject)     func removeObserver(_ observer: AnyObject, name aName: String?, object anObject: AnyObject?)     func addObserverForName(_ name: String?, object obj: AnyObject?, queue queue: NSOperationQueue?, usingBlock block: (NSNotification) -> Void) -> NSObjectProtocol } ``` |

Modified [NSNotificationCenter.addObserverForName(_: String?, object: AnyObject?, queue: NSOperationQueue?, usingBlock: (NSNotification) -> Void) -> NSObjectProtocol](https://developer.apple.com/documentation/foundation/notificationcenter/1411723-addobserver)

|  | Declaration |
| --- | --- |
| From | ``` func addObserverForName(_ name: String?, object obj: AnyObject?, queue queue: NSOperationQueue?, usingBlock block: (NSNotification!) -> Void) -> NSObjectProtocol ``` |
| To | ``` func addObserverForName(_ name: String?, object obj: AnyObject?, queue queue: NSOperationQueue?, usingBlock block: (NSNotification) -> Void) -> NSObjectProtocol ``` |

Modified [NSNotificationCoalescing [struct]](https://developer.apple.com/documentation/foundation/nsnotificationcoalescing)

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` enum NSNotificationCoalescing : UInt {     case NoCoalescing     case CoalescingOnName     case CoalescingOnSender } ``` | Equatable, Hashable, RawRepresentable | iOS 8.1 |
| To | ``` struct NSNotificationCoalescing : OptionSetType {     init(rawValue rawValue: UInt)     static var NoCoalescing: NSNotificationCoalescing { get }     static var CoalescingOnName: NSNotificationCoalescing { get }     static var CoalescingOnSender: NSNotificationCoalescing { get } } ``` | OptionSetType | iOS 9.0 |

Modified [NSNotificationCoalescing.CoalescingOnName](https://developer.apple.com/documentation/foundation/notificationqueue/notificationcoalescing/1410633-onname)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case CoalescingOnName ``` | iOS 8.0 |
| To | ``` static var CoalescingOnName: NSNotificationCoalescing { get } ``` | iOS 9.0 |

Modified [NSNotificationCoalescing.CoalescingOnSender](https://developer.apple.com/documentation/foundation/nsnotificationcoalescing/nsnotificationcoalescingonsender)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case CoalescingOnSender ``` | iOS 8.0 |
| To | ``` static var CoalescingOnSender: NSNotificationCoalescing { get } ``` | iOS 9.0 |

Modified [NSNotificationCoalescing.NoCoalescing](https://developer.apple.com/documentation/foundation/nsnotificationcoalescing/nsnotificationnocoalescing)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case NoCoalescing ``` | iOS 8.0 |
| To | ``` static var NoCoalescing: NSNotificationCoalescing { get } ``` | iOS 9.0 |

Modified [NSNotificationQueue](https://developer.apple.com/documentation/foundation/nsnotificationqueue)

|  | Declaration |
| --- | --- |
| From | ``` class NSNotificationQueue : NSObject {     class func defaultQueue() -> NSNotificationQueue     init(notificationCenter notificationCenter: NSNotificationCenter)     func enqueueNotification(_ notification: NSNotification, postingStyle postingStyle: NSPostingStyle)     func enqueueNotification(_ notification: NSNotification, postingStyle postingStyle: NSPostingStyle, coalesceMask coalesceMask: Int, forModes modes: [AnyObject]?)     func dequeueNotificationsMatching(_ notification: NSNotification, coalesceMask coalesceMask: Int) } ``` |
| To | ``` class NSNotificationQueue : NSObject {     class func defaultQueue() -> NSNotificationQueue     init(notificationCenter notificationCenter: NSNotificationCenter)     func enqueueNotification(_ notification: NSNotification, postingStyle postingStyle: NSPostingStyle)     func enqueueNotification(_ notification: NSNotification, postingStyle postingStyle: NSPostingStyle, coalesceMask coalesceMask: NSNotificationCoalescing, forModes modes: [String]?)     func dequeueNotificationsMatching(_ notification: NSNotification, coalesceMask coalesceMask: Int) } ``` |

Modified [NSNotificationQueue.enqueueNotification(_: NSNotification, postingStyle: NSPostingStyle, coalesceMask: NSNotificationCoalescing, forModes: [String]?)](https://developer.apple.com/documentation/foundation/nsnotificationqueue/1413873-enqueuenotification)

|  | Declaration |
| --- | --- |
| From | ``` func enqueueNotification(_ notification: NSNotification, postingStyle postingStyle: NSPostingStyle, coalesceMask coalesceMask: Int, forModes modes: [AnyObject]?) ``` |
| To | ``` func enqueueNotification(_ notification: NSNotification, postingStyle postingStyle: NSPostingStyle, coalesceMask coalesceMask: NSNotificationCoalescing, forModes modes: [String]?) ``` |

Modified [NSNull](https://developer.apple.com/documentation/foundation/nsnull)

|  | Declaration |
| --- | --- |
| From | ``` class NSNull : NSObject, NSCopying, NSSecureCoding, NSCoding {     init!() -> NSNull     class func null() -> NSNull! } extension NSNull : CAAction { } ``` |
| To | ``` class NSNull : NSObject, NSCopying, NSSecureCoding, NSCoding {      init()     class func null() -> NSNull } extension NSNull : CAAction { } ``` |

Modified [NSNumber](https://developer.apple.com/documentation/foundation/nsnumber)

|  | Declaration |
| --- | --- |
| From | ``` class NSNumber : NSValue {     init?(coder aDecoder: NSCoder)     init(char value: Int8)     init(unsignedChar value: UInt8)     init(short value: Int16)     init(unsignedShort value: UInt16)     init(int value: Int32)     init(unsignedInt value: UInt32)     init(long value: Int)     init(unsignedLong value: UInt)     init(longLong value: Int64)     init(unsignedLongLong value: UInt64)     init(float value: Float)     init(double value: Double)     init(bool value: Bool)     init(integer value: Int)     init(unsignedInteger value: Int)     var charValue: Int8 { get }     var unsignedCharValue: UInt8 { get }     var shortValue: Int16 { get }     var unsignedShortValue: UInt16 { get }     var intValue: Int32 { get }     var unsignedIntValue: UInt32 { get }     var longValue: Int { get }     var unsignedLongValue: UInt { get }     var longLongValue: Int64 { get }     var unsignedLongLongValue: UInt64 { get }     var floatValue: Float { get }     var doubleValue: Double { get }     var boolValue: Bool { get }     var integerValue: Int { get }     var unsignedIntegerValue: Int { get }     var stringValue: String { get }     func compare(_ otherNumber: NSNumber) -> NSComparisonResult     func isEqualToNumber(_ number: NSNumber) -> Bool     func descriptionWithLocale(_ locale: AnyObject?) -> String } extension NSNumber : CKRecordValue, NSObjectProtocol { } extension NSNumber {     var decimalValue: NSDecimal { get } } extension NSNumber : FloatLiteralConvertible, IntegerLiteralConvertible, BooleanLiteralConvertible {     required convenience init(integerLiteral value: Int)     required convenience init(floatLiteral value: Double)     required convenience init(booleanLiteral value: Bool) } extension NSNumber {     class func numberWithChar(_ value: Int8) -> NSNumber     class func numberWithUnsignedChar(_ value: UInt8) -> NSNumber     class func numberWithShort(_ value: Int16) -> NSNumber     class func numberWithUnsignedShort(_ value: UInt16) -> NSNumber     class func numberWithInt(_ value: Int32) -> NSNumber     class func numberWithUnsignedInt(_ value: UInt32) -> NSNumber     class func numberWithLong(_ value: Int) -> NSNumber     class func numberWithUnsignedLong(_ value: UInt) -> NSNumber     class func numberWithLongLong(_ value: Int64) -> NSNumber     class func numberWithUnsignedLongLong(_ value: UInt64) -> NSNumber     class func numberWithFloat(_ value: Float) -> NSNumber     class func numberWithDouble(_ value: Double) -> NSNumber     class func numberWithBool(_ value: Bool) -> NSNumber     class func numberWithInteger(_ value: Int) -> NSNumber     class func numberWithUnsignedInteger(_ value: Int) -> NSNumber } extension NSNumber : FloatLiteralConvertible, IntegerLiteralConvertible, BooleanLiteralConvertible {     required convenience init(integerLiteral value: Int)     required convenience init(floatLiteral value: Double)     required convenience init(booleanLiteral value: Bool) } ``` |
| To | ``` class NSNumber : NSValue {     init?(coder aDecoder: NSCoder)     init(char value: Int8)     init(unsignedChar value: UInt8)     init(short value: Int16)     init(unsignedShort value: UInt16)     init(int value: Int32)     init(unsignedInt value: UInt32)     init(long value: Int)     init(unsignedLong value: UInt)     init(longLong value: Int64)     init(unsignedLongLong value: UInt64)     init(float value: Float)     init(double value: Double)     init(bool value: Bool)     init(integer value: Int)     init(unsignedInteger value: Int)     var charValue: Int8 { get }     var unsignedCharValue: UInt8 { get }     var shortValue: Int16 { get }     var unsignedShortValue: UInt16 { get }     var intValue: Int32 { get }     var unsignedIntValue: UInt32 { get }     var longValue: Int { get }     var unsignedLongValue: UInt { get }     var longLongValue: Int64 { get }     var unsignedLongLongValue: UInt64 { get }     var floatValue: Float { get }     var doubleValue: Double { get }     var boolValue: Bool { get }     var integerValue: Int { get }     var unsignedIntegerValue: Int { get }     var stringValue: String { get }     func compare(_ otherNumber: NSNumber) -> NSComparisonResult     func isEqualToNumber(_ number: NSNumber) -> Bool     func descriptionWithLocale(_ locale: AnyObject?) -> String } extension NSNumber : CKRecordValue { } extension NSNumber {     var decimalValue: NSDecimal { get } } extension NSNumber : FloatLiteralConvertible, IntegerLiteralConvertible, BooleanLiteralConvertible {     required convenience init(integerLiteral value: Int)     required convenience init(floatLiteral value: Double)     required convenience init(booleanLiteral value: Bool) } extension NSNumber {     class func numberWithChar(_ value: Int8) -> NSNumber     class func numberWithUnsignedChar(_ value: UInt8) -> NSNumber     class func numberWithShort(_ value: Int16) -> NSNumber     class func numberWithUnsignedShort(_ value: UInt16) -> NSNumber     class func numberWithInt(_ value: Int32) -> NSNumber     class func numberWithUnsignedInt(_ value: UInt32) -> NSNumber     class func numberWithLong(_ value: Int) -> NSNumber     class func numberWithUnsignedLong(_ value: UInt) -> NSNumber     class func numberWithLongLong(_ value: Int64) -> NSNumber     class func numberWithUnsignedLongLong(_ value: UInt64) -> NSNumber     class func numberWithFloat(_ value: Float) -> NSNumber     class func numberWithDouble(_ value: Double) -> NSNumber     class func numberWithBool(_ value: Bool) -> NSNumber     class func numberWithInteger(_ value: Int) -> NSNumber     class func numberWithUnsignedInteger(_ value: Int) -> NSNumber } extension NSNumber : FloatLiteralConvertible, IntegerLiteralConvertible, BooleanLiteralConvertible {     required convenience init(integerLiteral value: Int)     required convenience init(floatLiteral value: Double)     required convenience init(booleanLiteral value: Bool) } ``` |

Modified [NSNumberFormatter](https://developer.apple.com/documentation/foundation/numberformatter)

|  | Declaration |
| --- | --- |
| From | ``` class NSNumberFormatter : NSFormatter {     var formattingContext: NSFormattingContext     func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>, forString string: String, range rangep: UnsafeMutablePointer<NSRange>, error error: NSErrorPointer) -> Bool     func stringFromNumber(_ number: NSNumber) -> String?     func numberFromString(_ string: String) -> NSNumber?     class func localizedStringFromNumber(_ num: NSNumber, numberStyle nstyle: NSNumberFormatterStyle) -> String     class func defaultFormatterBehavior() -> NSNumberFormatterBehavior     class func setDefaultFormatterBehavior(_ behavior: NSNumberFormatterBehavior)     var numberStyle: NSNumberFormatterStyle     @NSCopying var locale: NSLocale?     var generatesDecimalNumbers: Bool     var formatterBehavior: NSNumberFormatterBehavior     var negativeFormat: String     var textAttributesForNegativeValues: [NSObject : AnyObject]?     var positiveFormat: String!     var textAttributesForPositiveValues: [NSObject : AnyObject]?     var allowsFloats: Bool     var decimalSeparator: String?     var alwaysShowsDecimalSeparator: Bool     var currencyDecimalSeparator: String?     var usesGroupingSeparator: Bool     var groupingSeparator: String!     var zeroSymbol: String?     var textAttributesForZero: [NSObject : AnyObject]?     var nilSymbol: String     var textAttributesForNil: [NSObject : AnyObject]?     var notANumberSymbol: String     var textAttributesForNotANumber: [NSObject : AnyObject]?     var positiveInfinitySymbol: String     var textAttributesForPositiveInfinity: [NSObject : AnyObject]?     var negativeInfinitySymbol: String     var textAttributesForNegativeInfinity: [NSObject : AnyObject]?     var positivePrefix: String     var positiveSuffix: String     var negativePrefix: String     var negativeSuffix: String     var currencyCode: String     var currencySymbol: String?     var internationalCurrencySymbol: String?     var percentSymbol: String     var perMillSymbol: String     var minusSign: String     var plusSign: String     var exponentSymbol: String     var groupingSize: Int     var secondaryGroupingSize: Int     @NSCopying var multiplier: NSNumber?     var formatWidth: Int     var paddingCharacter: String?     var paddingPosition: NSNumberFormatterPadPosition     var roundingMode: NSNumberFormatterRoundingMode     @NSCopying var roundingIncrement: NSNumber?     var minimumIntegerDigits: Int     var maximumIntegerDigits: Int     var minimumFractionDigits: Int     var maximumFractionDigits: Int     @NSCopying var minimum: NSNumber!     @NSCopying var maximum: NSNumber!     var currencyGroupingSeparator: String?     var lenient: Bool     var usesSignificantDigits: Bool     var minimumSignificantDigits: Int     var maximumSignificantDigits: Int     var partialStringValidationEnabled: Bool } ``` |
| To | ``` class NSNumberFormatter : NSFormatter {     var formattingContext: NSFormattingContext     func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>, forString string: String, range rangep: UnsafeMutablePointer<NSRange>) throws     func stringFromNumber(_ number: NSNumber) -> String?     func numberFromString(_ string: String) -> NSNumber?     class func localizedStringFromNumber(_ num: NSNumber, numberStyle nstyle: NSNumberFormatterStyle) -> String     class func defaultFormatterBehavior() -> NSNumberFormatterBehavior     class func setDefaultFormatterBehavior(_ behavior: NSNumberFormatterBehavior)     var numberStyle: NSNumberFormatterStyle     @NSCopying var locale: NSLocale!     var generatesDecimalNumbers: Bool     var formatterBehavior: NSNumberFormatterBehavior     var negativeFormat: String!     var textAttributesForNegativeValues: [String : AnyObject]?     var positiveFormat: String!     var textAttributesForPositiveValues: [String : AnyObject]?     var allowsFloats: Bool     var decimalSeparator: String!     var alwaysShowsDecimalSeparator: Bool     var currencyDecimalSeparator: String!     var usesGroupingSeparator: Bool     var groupingSeparator: String!     var zeroSymbol: String?     var textAttributesForZero: [String : AnyObject]?     var nilSymbol: String     var textAttributesForNil: [String : AnyObject]?     var notANumberSymbol: String!     var textAttributesForNotANumber: [String : AnyObject]?     var positiveInfinitySymbol: String     var textAttributesForPositiveInfinity: [String : AnyObject]?     var negativeInfinitySymbol: String     var textAttributesForNegativeInfinity: [String : AnyObject]?     var positivePrefix: String!     var positiveSuffix: String!     var negativePrefix: String!     var negativeSuffix: String!     var currencyCode: String!     var currencySymbol: String!     var internationalCurrencySymbol: String!     var percentSymbol: String!     var perMillSymbol: String!     var minusSign: String!     var plusSign: String!     var exponentSymbol: String!     var groupingSize: Int     var secondaryGroupingSize: Int     @NSCopying var multiplier: NSNumber?     var formatWidth: Int     var paddingCharacter: String!     var paddingPosition: NSNumberFormatterPadPosition     var roundingMode: NSNumberFormatterRoundingMode     @NSCopying var roundingIncrement: NSNumber!     var minimumIntegerDigits: Int     var maximumIntegerDigits: Int     var minimumFractionDigits: Int     var maximumFractionDigits: Int     @NSCopying var minimum: NSNumber?     @NSCopying var maximum: NSNumber?     var currencyGroupingSeparator: String!     var lenient: Bool     var usesSignificantDigits: Bool     var minimumSignificantDigits: Int     var maximumSignificantDigits: Int     var partialStringValidationEnabled: Bool } ``` |

Modified [NSNumberFormatter.currencyCode](https://developer.apple.com/documentation/foundation/nsnumberformatter/1410463-currencycode)

|  | Declaration |
| --- | --- |
| From | ``` var currencyCode: String ``` |
| To | ``` var currencyCode: String! ``` |

Modified [NSNumberFormatter.currencyDecimalSeparator](https://developer.apple.com/documentation/foundation/nsnumberformatter/1407247-currencydecimalseparator)

|  | Declaration |
| --- | --- |
| From | ``` var currencyDecimalSeparator: String? ``` |
| To | ``` var currencyDecimalSeparator: String! ``` |

Modified [NSNumberFormatter.currencyGroupingSeparator](https://developer.apple.com/documentation/foundation/nsnumberformatter/1416213-currencygroupingseparator)

|  | Declaration |
| --- | --- |
| From | ``` var currencyGroupingSeparator: String? ``` |
| To | ``` var currencyGroupingSeparator: String! ``` |

Modified [NSNumberFormatter.currencySymbol](https://developer.apple.com/documentation/foundation/numberformatter/1414668-currencysymbol)

|  | Declaration |
| --- | --- |
| From | ``` var currencySymbol: String? ``` |
| To | ``` var currencySymbol: String! ``` |

Modified [NSNumberFormatter.decimalSeparator](https://developer.apple.com/documentation/foundation/numberformatter/1408029-decimalseparator)

|  | Declaration |
| --- | --- |
| From | ``` var decimalSeparator: String? ``` |
| To | ``` var decimalSeparator: String! ``` |

Modified [NSNumberFormatter.exponentSymbol](https://developer.apple.com/documentation/foundation/numberformatter/1417223-exponentsymbol)

|  | Declaration |
| --- | --- |
| From | ``` var exponentSymbol: String ``` |
| To | ``` var exponentSymbol: String! ``` |

Modified [NSNumberFormatter.getObjectValue(_: AutoreleasingUnsafeMutablePointer<AnyObject?>, forString: String, range: UnsafeMutablePointer<NSRange>) throws](https://developer.apple.com/documentation/foundation/numberformatter/1412588-getobjectvalue)

|  | Declaration |
| --- | --- |
| From | ``` func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>, forString string: String, range rangep: UnsafeMutablePointer<NSRange>, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>, forString string: String, range rangep: UnsafeMutablePointer<NSRange>) throws ``` |

Modified [NSNumberFormatter.internationalCurrencySymbol](https://developer.apple.com/documentation/foundation/nsnumberformatter/1412755-internationalcurrencysymbol)

|  | Declaration |
| --- | --- |
| From | ``` var internationalCurrencySymbol: String? ``` |
| To | ``` var internationalCurrencySymbol: String! ``` |

Modified [NSNumberFormatter.locale](https://developer.apple.com/documentation/foundation/numberformatter/1416967-locale)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var locale: NSLocale? ``` |
| To | ``` @NSCopying var locale: NSLocale! ``` |

Modified [NSNumberFormatter.maximum](https://developer.apple.com/documentation/foundation/nsnumberformatter/1417787-maximum)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var maximum: NSNumber! ``` |
| To | ``` @NSCopying var maximum: NSNumber? ``` |

Modified [NSNumberFormatter.minimum](https://developer.apple.com/documentation/foundation/nsnumberformatter/1417228-minimum)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var minimum: NSNumber! ``` |
| To | ``` @NSCopying var minimum: NSNumber? ``` |

Modified [NSNumberFormatter.minusSign](https://developer.apple.com/documentation/foundation/numberformatter/1409416-minussign)

|  | Declaration |
| --- | --- |
| From | ``` var minusSign: String ``` |
| To | ``` var minusSign: String! ``` |

Modified [NSNumberFormatter.negativeFormat](https://developer.apple.com/documentation/foundation/numberformatter/1414039-negativeformat)

|  | Declaration |
| --- | --- |
| From | ``` var negativeFormat: String ``` |
| To | ``` var negativeFormat: String! ``` |

Modified [NSNumberFormatter.negativePrefix](https://developer.apple.com/documentation/foundation/nsnumberformatter/1408096-negativeprefix)

|  | Declaration |
| --- | --- |
| From | ``` var negativePrefix: String ``` |
| To | ``` var negativePrefix: String! ``` |

Modified [NSNumberFormatter.negativeSuffix](https://developer.apple.com/documentation/foundation/numberformatter/1413927-negativesuffix)

|  | Declaration |
| --- | --- |
| From | ``` var negativeSuffix: String ``` |
| To | ``` var negativeSuffix: String! ``` |

Modified [NSNumberFormatter.notANumberSymbol](https://developer.apple.com/documentation/foundation/numberformatter/1416993-notanumbersymbol)

|  | Declaration |
| --- | --- |
| From | ``` var notANumberSymbol: String ``` |
| To | ``` var notANumberSymbol: String! ``` |

Modified [NSNumberFormatter.paddingCharacter](https://developer.apple.com/documentation/foundation/nsnumberformatter/1413690-paddingcharacter)

|  | Declaration |
| --- | --- |
| From | ``` var paddingCharacter: String? ``` |
| To | ``` var paddingCharacter: String! ``` |

Modified [NSNumberFormatter.percentSymbol](https://developer.apple.com/documentation/foundation/numberformatter/1407789-percentsymbol)

|  | Declaration |
| --- | --- |
| From | ``` var percentSymbol: String ``` |
| To | ``` var percentSymbol: String! ``` |

Modified [NSNumberFormatter.perMillSymbol](https://developer.apple.com/documentation/foundation/numberformatter/1412399-permillsymbol)

|  | Declaration |
| --- | --- |
| From | ``` var perMillSymbol: String ``` |
| To | ``` var perMillSymbol: String! ``` |

Modified [NSNumberFormatter.plusSign](https://developer.apple.com/documentation/foundation/numberformatter/1416423-plussign)

|  | Declaration |
| --- | --- |
| From | ``` var plusSign: String ``` |
| To | ``` var plusSign: String! ``` |

Modified [NSNumberFormatter.positivePrefix](https://developer.apple.com/documentation/foundation/numberformatter/1414204-positiveprefix)

|  | Declaration |
| --- | --- |
| From | ``` var positivePrefix: String ``` |
| To | ``` var positivePrefix: String! ``` |

Modified [NSNumberFormatter.positiveSuffix](https://developer.apple.com/documentation/foundation/nsnumberformatter/1415071-positivesuffix)

|  | Declaration |
| --- | --- |
| From | ``` var positiveSuffix: String ``` |
| To | ``` var positiveSuffix: String! ``` |

Modified [NSNumberFormatter.roundingIncrement](https://developer.apple.com/documentation/foundation/nsnumberformatter/1412561-roundingincrement)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var roundingIncrement: NSNumber? ``` |
| To | ``` @NSCopying var roundingIncrement: NSNumber! ``` |

Modified [NSNumberFormatter.textAttributesForNegativeInfinity](https://developer.apple.com/documentation/foundation/numberformatter/1410417-textattributesfornegativeinfinit)

|  | Declaration |
| --- | --- |
| From | ``` var textAttributesForNegativeInfinity: [NSObject : AnyObject]? ``` |
| To | ``` var textAttributesForNegativeInfinity: [String : AnyObject]? ``` |

Modified [NSNumberFormatter.textAttributesForNegativeValues](https://developer.apple.com/documentation/foundation/nsnumberformatter/1414530-textattributesfornegativevalues)

|  | Declaration |
| --- | --- |
| From | ``` var textAttributesForNegativeValues: [NSObject : AnyObject]? ``` |
| To | ``` var textAttributesForNegativeValues: [String : AnyObject]? ``` |

Modified [NSNumberFormatter.textAttributesForNil](https://developer.apple.com/documentation/foundation/numberformatter/1408943-textattributesfornil)

|  | Declaration |
| --- | --- |
| From | ``` var textAttributesForNil: [NSObject : AnyObject]? ``` |
| To | ``` var textAttributesForNil: [String : AnyObject]? ``` |

Modified [NSNumberFormatter.textAttributesForNotANumber](https://developer.apple.com/documentation/foundation/numberformatter/1410959-textattributesfornotanumber)

|  | Declaration |
| --- | --- |
| From | ``` var textAttributesForNotANumber: [NSObject : AnyObject]? ``` |
| To | ``` var textAttributesForNotANumber: [String : AnyObject]? ``` |

Modified [NSNumberFormatter.textAttributesForPositiveInfinity](https://developer.apple.com/documentation/foundation/nsnumberformatter/1408176-textattributesforpositiveinfinit)

|  | Declaration |
| --- | --- |
| From | ``` var textAttributesForPositiveInfinity: [NSObject : AnyObject]? ``` |
| To | ``` var textAttributesForPositiveInfinity: [String : AnyObject]? ``` |

Modified [NSNumberFormatter.textAttributesForPositiveValues](https://developer.apple.com/documentation/foundation/nsnumberformatter/1409563-textattributesforpositivevalues)

|  | Declaration |
| --- | --- |
| From | ``` var textAttributesForPositiveValues: [NSObject : AnyObject]? ``` |
| To | ``` var textAttributesForPositiveValues: [String : AnyObject]? ``` |

Modified [NSNumberFormatter.textAttributesForZero](https://developer.apple.com/documentation/foundation/nsnumberformatter/1415971-textattributesforzero)

|  | Declaration |
| --- | --- |
| From | ``` var textAttributesForZero: [NSObject : AnyObject]? ``` |
| To | ``` var textAttributesForZero: [String : AnyObject]? ``` |

Modified [NSNumberFormatterBehavior [enum]](https://developer.apple.com/documentation/foundation/numberformatter/behavior)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSNumberFormatterPadPosition [enum]](https://developer.apple.com/documentation/foundation/numberformatter/padposition)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSNumberFormatterRoundingMode [enum]](https://developer.apple.com/documentation/foundation/nsnumberformatterroundingmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSNumberFormatterStyle [enum]](https://developer.apple.com/documentation/foundation/numberformatter/style)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum NSNumberFormatterStyle : UInt {     case NoStyle     case DecimalStyle     case CurrencyStyle     case PercentStyle     case ScientificStyle     case SpellOutStyle } ``` | -- |
| To | ``` enum NSNumberFormatterStyle : UInt {     case NoStyle     case DecimalStyle     case CurrencyStyle     case PercentStyle     case ScientificStyle     case SpellOutStyle     case OrdinalStyle     case CurrencyISOCodeStyle     case CurrencyPluralStyle     case CurrencyAccountingStyle } ``` | UInt |

Modified [NSObject.attemptRecoveryFromError(_: NSError, optionIndex: Int) -> Bool](https://developer.apple.com/documentation/objectivec/nsobject/1416402-attemptrecovery)

|  | Declaration |
| --- | --- |
| From | ``` func attemptRecoveryFromError(_ error: NSError!, optionIndex recoveryOptionIndex: Int) -> Bool ``` |
| To | ``` func attemptRecoveryFromError(_ error: NSError, optionIndex recoveryOptionIndex: Int) -> Bool ``` |

Modified [NSObject.attemptRecoveryFromError(_: NSError, optionIndex: Int, delegate: AnyObject?, didRecoverSelector: Selector, contextInfo: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/objectivec/nsobject/1411071-attemptrecoveryfromerror)

|  | Declaration |
| --- | --- |
| From | ``` func attemptRecoveryFromError(_ error: NSError!, optionIndex recoveryOptionIndex: Int, delegate delegate: AnyObject!, didRecoverSelector didRecoverSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |
| To | ``` func attemptRecoveryFromError(_ error: NSError, optionIndex recoveryOptionIndex: Int, delegate delegate: AnyObject?, didRecoverSelector didRecoverSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |

Modified [NSObject.classFallbacksForKeyedArchiver() -> [String] [class]](https://developer.apple.com/documentation/objectivec/nsobject/1411048-classfallbacksforkeyedarchiver)

|  | Declaration |
| --- | --- |
| From | ``` class func classFallbacksForKeyedArchiver() -> [AnyObject] ``` |
| To | ``` class func classFallbacksForKeyedArchiver() -> [String] ``` |

Modified [NSObject.dictionaryWithValuesForKeys(_: [String]) -> [String : AnyObject]](https://developer.apple.com/documentation/objectivec/nsobject/1411319-dictionarywithvalues)

|  | Declaration |
| --- | --- |
| From | ``` func dictionaryWithValuesForKeys(_ keys: [AnyObject]) -> [NSObject : AnyObject] ``` |
| To | ``` func dictionaryWithValuesForKeys(_ keys: [String]) -> [String : AnyObject] ``` |

Modified [NSObject.keyPathsForValuesAffectingValueForKey(_: String) -> Set<String> [class]](https://developer.apple.com/documentation/objectivec/nsobject/1414299-keypathsforvaluesaffectingvaluef)

|  | Declaration |
| --- | --- |
| From | ``` class func keyPathsForValuesAffectingValueForKey(_ key: String) -> Set<NSObject> ``` |
| To | ``` class func keyPathsForValuesAffectingValueForKey(_ key: String) -> Set<String> ``` |

Modified [NSObject.observeValueForKeyPath(_: String?, ofObject: AnyObject?, change: [String : AnyObject]?, context: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/objectivec/nsobject/1416553-observevalueforkeypath)

|  | Declaration |
| --- | --- |
| From | ``` func observeValueForKeyPath(_ keyPath: String, ofObject object: AnyObject, change change: [NSObject : AnyObject], context context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func observeValueForKeyPath(_ keyPath: String?, ofObject object: AnyObject?, change change: [String : AnyObject]?, context context: UnsafeMutablePointer<Void>) ``` |

Modified [NSObject.setValuesForKeysWithDictionary(_: [String : AnyObject])](https://developer.apple.com/documentation/objectivec/nsobject/1417515-setvaluesforkeys)

|  | Declaration |
| --- | --- |
| From | ``` func setValuesForKeysWithDictionary(_ keyedValues: [NSObject : AnyObject]) ``` |
| To | ``` func setValuesForKeysWithDictionary(_ keyedValues: [String : AnyObject]) ``` |

Modified [NSObject.validateValue(_: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey: String) throws](https://developer.apple.com/documentation/objectivec/nsobject/1416754-validatevalue)

|  | Declaration |
| --- | --- |
| From | ``` func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws ``` |

Modified [NSObject.validateValue(_: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath: String) throws](https://developer.apple.com/documentation/objectivec/nsobject/1416245-validatevalue)

|  | Declaration |
| --- | --- |
| From | ``` func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws ``` |

Modified [NSOperation](https://developer.apple.com/documentation/foundation/nsoperation)

|  | Declaration |
| --- | --- |
| From | ``` class NSOperation : NSObject {     func start()     func main()     var cancelled: Bool { get }     func cancel()     var executing: Bool { get }     var finished: Bool { get }     var concurrent: Bool { get }     var asynchronous: Bool { get }     var ready: Bool { get }     func addDependency(_ op: NSOperation)     func removeDependency(_ op: NSOperation)     var dependencies: [AnyObject] { get }     var queuePriority: NSOperationQueuePriority     var completionBlock: (() -> Void)?     func waitUntilFinished()     var threadPriority: Double     var qualityOfService: NSQualityOfService     var name: String? } ``` |
| To | ``` class NSOperation : NSObject {     func start()     func main()     var cancelled: Bool { get }     func cancel()     var executing: Bool { get }     var finished: Bool { get }     var concurrent: Bool { get }     var asynchronous: Bool { get }     var ready: Bool { get }     func addDependency(_ op: NSOperation)     func removeDependency(_ op: NSOperation)     var dependencies: [NSOperation] { get }     var queuePriority: NSOperationQueuePriority     var completionBlock: (() -> Void)?     func waitUntilFinished()     var threadPriority: Double     var qualityOfService: NSQualityOfService     var name: String? } ``` |

Modified [NSOperation.dependencies](https://developer.apple.com/documentation/foundation/nsoperation/1416668-dependencies)

|  | Declaration |
| --- | --- |
| From | ``` var dependencies: [AnyObject] { get } ``` |
| To | ``` var dependencies: [NSOperation] { get } ``` |

Modified [NSOperationQueue](https://developer.apple.com/documentation/foundation/operationqueue)

|  | Declaration |
| --- | --- |
| From | ``` class NSOperationQueue : NSObject {     func addOperation(_ op: NSOperation)     func addOperations(_ ops: [AnyObject], waitUntilFinished wait: Bool)     func addOperationWithBlock(_ block: () -> Void)     var operations: [AnyObject] { get }     var operationCount: Int { get }     var maxConcurrentOperationCount: Int     var suspended: Bool     var name: String?     var qualityOfService: NSQualityOfService     unowned(unsafe) var underlyingQueue: dispatch_queue_t     func cancelAllOperations()     func waitUntilAllOperationsAreFinished()     class func currentQueue() -> NSOperationQueue?     class func mainQueue() -> NSOperationQueue } ``` |
| To | ``` class NSOperationQueue : NSObject {     func addOperation(_ op: NSOperation)     func addOperations(_ ops: [NSOperation], waitUntilFinished wait: Bool)     func addOperationWithBlock(_ block: () -> Void)     var operations: [NSOperation] { get }     var operationCount: Int { get }     var maxConcurrentOperationCount: Int     var suspended: Bool     var name: String?     var qualityOfService: NSQualityOfService     unowned(unsafe) var underlyingQueue: dispatch_queue_t?     func cancelAllOperations()     func waitUntilAllOperationsAreFinished()     class func currentQueue() -> NSOperationQueue?     class func mainQueue() -> NSOperationQueue } ``` |

Modified [NSOperationQueue.addOperations(_: [NSOperation], waitUntilFinished: Bool)](https://developer.apple.com/documentation/foundation/nsoperationqueue/1408358-addoperations)

|  | Declaration |
| --- | --- |
| From | ``` func addOperations(_ ops: [AnyObject], waitUntilFinished wait: Bool) ``` |
| To | ``` func addOperations(_ ops: [NSOperation], waitUntilFinished wait: Bool) ``` |

Modified [NSOperationQueue.operations](https://developer.apple.com/documentation/foundation/operationqueue/1415168-operations)

|  | Declaration |
| --- | --- |
| From | ``` var operations: [AnyObject] { get } ``` |
| To | ``` var operations: [NSOperation] { get } ``` |

Modified [NSOperationQueue.underlyingQueue](https://developer.apple.com/documentation/foundation/operationqueue/1415344-underlyingqueue)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var underlyingQueue: dispatch_queue_t ``` |
| To | ``` unowned(unsafe) var underlyingQueue: dispatch_queue_t? ``` |

Modified [NSOperationQueuePriority [enum]](https://developer.apple.com/documentation/foundation/nsoperationqueuepriority)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NSOrderedSet](https://developer.apple.com/documentation/foundation/nsorderedset)

|  | Declaration |
| --- | --- |
| From | ``` class NSOrderedSet : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding, NSFastEnumeration {     var count: Int { get }     func objectAtIndex(_ idx: Int) -> AnyObject     func indexOfObject(_ object: AnyObject) -> Int     init()     init(objects objects: UnsafePointer<AnyObject?>, count cnt: Int)     init?(coder aDecoder: NSCoder) } extension NSOrderedSet {     func valueForKey(_ key: String) -> AnyObject     func setValue(_ value: AnyObject?, forKey key: String) } extension NSOrderedSet {     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String) } extension NSOrderedSet : SequenceType {     func generate() -> NSFastGenerator } extension NSOrderedSet {     convenience init(objects elements: AnyObject...) } extension NSOrderedSet : ArrayLiteralConvertible {     required convenience init(arrayLiteral elements: AnyObject...) } extension NSOrderedSet {     func getObjects(_ objects: AutoreleasingUnsafeMutablePointer<AnyObject?>, range range: NSRange)     func objectsAtIndexes(_ indexes: NSIndexSet) -> [AnyObject]     var firstObject: AnyObject? { get }     var lastObject: AnyObject? { get }     func isEqualToOrderedSet(_ other: NSOrderedSet) -> Bool     func containsObject(_ object: AnyObject) -> Bool     func intersectsOrderedSet(_ other: NSOrderedSet) -> Bool     func intersectsSet(_ set: Set<NSObject>) -> Bool     func isSubsetOfOrderedSet(_ other: NSOrderedSet) -> Bool     func isSubsetOfSet(_ set: Set<NSObject>) -> Bool     subscript (idx: Int) -> AnyObject { get }     func objectAtIndexedSubscript(_ idx: Int) -> AnyObject     func objectEnumerator() -> NSEnumerator     func reverseObjectEnumerator() -> NSEnumerator     @NSCopying var reversedOrderedSet: NSOrderedSet { get }     var array: [AnyObject] { get }     var set: Set<NSObject> { get }     func enumerateObjectsUsingBlock(_ block: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, usingBlock block: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func indexOfObjectPassingTest(_ predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexOfObjectWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexOfObjectAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexesOfObjectsPassingTest(_ predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexesOfObjectsWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexesOfObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexOfObject(_ object: AnyObject, inSortedRange range: NSRange, options opts: NSBinarySearchingOptions, usingComparator cmp: NSComparator) -> Int     func sortedArrayUsingComparator(_ cmptr: NSComparator) -> [AnyObject]     func sortedArrayWithOptions(_ opts: NSSortOptions, usingComparator cmptr: NSComparator) -> [AnyObject]     var description: String { get }     func descriptionWithLocale(_ locale: AnyObject?) -> String?     func descriptionWithLocale(_ locale: AnyObject?, indent level: Int) -> String } extension NSOrderedSet {     convenience init!()     class func orderedSet() -> Self!     convenience init(object object: AnyObject)     class func orderedSetWithObject(_ object: AnyObject) -> Self     convenience init!(objects objects: UnsafePointer<AnyObject?>, count cnt: Int)     class func orderedSetWithObjects(_ objects: UnsafePointer<AnyObject?>, count cnt: Int) -> Self!     convenience init(orderedSet set: NSOrderedSet?)     class func orderedSetWithOrderedSet(_ set: NSOrderedSet?) -> Self     convenience init(orderedSet set: NSOrderedSet, range range: NSRange, copyItems flag: Bool)     class func orderedSetWithOrderedSet(_ set: NSOrderedSet, range range: NSRange, copyItems flag: Bool) -> Self     convenience init(array array: [AnyObject])     class func orderedSetWithArray(_ array: [AnyObject]) -> Self     convenience init(array array: [AnyObject], range range: NSRange, copyItems flag: Bool)     class func orderedSetWithArray(_ array: [AnyObject], range range: NSRange, copyItems flag: Bool) -> Self     convenience init(set set: Set<NSObject>?)     class func orderedSetWithSet(_ set: Set<NSObject>?) -> Self     convenience init(set set: Set<NSObject>?, copyItems flag: Bool)     class func orderedSetWithSet(_ set: Set<NSObject>?, copyItems flag: Bool) -> Self     convenience init(object object: AnyObject)     convenience init(orderedSet set: NSOrderedSet)     convenience init(orderedSet set: NSOrderedSet, copyItems flag: Bool)     convenience init(orderedSet set: NSOrderedSet, range range: NSRange, copyItems flag: Bool)     convenience init(array array: [AnyObject])     convenience init(array set: [AnyObject], copyItems flag: Bool)     convenience init(array set: [AnyObject], range range: NSRange, copyItems flag: Bool)     convenience init(set set: Set<NSObject>)     convenience init(set set: Set<NSObject>, copyItems flag: Bool) } extension NSOrderedSet {     func filteredOrderedSetUsingPredicate(_ p: NSPredicate) -> NSOrderedSet } extension NSOrderedSet {     func sortedArrayUsingDescriptors(_ sortDescriptors: [AnyObject]) -> [AnyObject] } extension NSOrderedSet : ArrayLiteralConvertible {     required convenience init(arrayLiteral elements: AnyObject...) } extension NSOrderedSet {     convenience init(objects elements: AnyObject...) } extension NSOrderedSet : SequenceType {     func generate() -> NSFastGenerator } ``` |
| To | ``` class NSOrderedSet : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding, NSFastEnumeration {     var count: Int { get }     func objectAtIndex(_ idx: Int) -> AnyObject     func indexOfObject(_ object: AnyObject) -> Int     init()     init(objects objects: UnsafePointer<AnyObject?>, count cnt: Int)     init?(coder aDecoder: NSCoder) } extension NSOrderedSet {     func valueForKey(_ key: String) -> AnyObject     func setValue(_ value: AnyObject?, forKey key: String) } extension NSOrderedSet {     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String) } extension NSOrderedSet : SequenceType {     func generate() -> NSFastGenerator } extension NSOrderedSet {     convenience init(objects elements: AnyObject...) } extension NSOrderedSet : ArrayLiteralConvertible {     required convenience init(arrayLiteral elements: AnyObject...) } extension NSOrderedSet {     func getObjects(_ objects: AutoreleasingUnsafeMutablePointer<AnyObject?>, range range: NSRange)     func objectsAtIndexes(_ indexes: NSIndexSet) -> [AnyObject]     var firstObject: AnyObject? { get }     var lastObject: AnyObject? { get }     func isEqualToOrderedSet(_ other: NSOrderedSet) -> Bool     func containsObject(_ object: AnyObject) -> Bool     func intersectsOrderedSet(_ other: NSOrderedSet) -> Bool     func intersectsSet(_ set: Set<NSObject>) -> Bool     func isSubsetOfOrderedSet(_ other: NSOrderedSet) -> Bool     func isSubsetOfSet(_ set: Set<NSObject>) -> Bool     subscript (_ idx: Int) -> AnyObject { get }     func objectAtIndexedSubscript(_ idx: Int) -> AnyObject     func objectEnumerator() -> NSEnumerator     func reverseObjectEnumerator() -> NSEnumerator     @NSCopying var reversedOrderedSet: NSOrderedSet { get }     var array: [AnyObject] { get }     var set: Set<NSObject> { get }     func enumerateObjectsUsingBlock(_ block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, usingBlock block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func indexOfObjectPassingTest(_ predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexOfObjectWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexOfObjectAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexesOfObjectsPassingTest(_ predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexesOfObjectsWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexesOfObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet     func indexOfObject(_ object: AnyObject, inSortedRange range: NSRange, options opts: NSBinarySearchingOptions, usingComparator cmp: NSComparator) -> Int     func sortedArrayUsingComparator(_ cmptr: NSComparator) -> [AnyObject]     func sortedArrayWithOptions(_ opts: NSSortOptions, usingComparator cmptr: NSComparator) -> [AnyObject]     var description: String { get }     func descriptionWithLocale(_ locale: AnyObject?) -> String     func descriptionWithLocale(_ locale: AnyObject?, indent level: Int) -> String } extension NSOrderedSet {     convenience init()     class func orderedSet() -> Self     convenience init(object object: AnyObject)     class func orderedSetWithObject(_ object: AnyObject) -> Self     convenience init(objects objects: UnsafePointer<AnyObject?>, count cnt: Int)     class func orderedSetWithObjects(_ objects: UnsafePointer<AnyObject?>, count cnt: Int) -> Self     convenience init(orderedSet set: NSOrderedSet)     class func orderedSetWithOrderedSet(_ set: NSOrderedSet) -> Self     convenience init(orderedSet set: NSOrderedSet, range range: NSRange, copyItems flag: Bool)     class func orderedSetWithOrderedSet(_ set: NSOrderedSet, range range: NSRange, copyItems flag: Bool) -> Self     convenience init(array array: [AnyObject])     class func orderedSetWithArray(_ array: [AnyObject]) -> Self     convenience init(array array: [AnyObject], range range: NSRange, copyItems flag: Bool)     class func orderedSetWithArray(_ array: [AnyObject], range range: NSRange, copyItems flag: Bool) -> Self     convenience init(set set: Set<NSObject>)     class func orderedSetWithSet(_ set: Set<NSObject>) -> Self     convenience init(set set: Set<NSObject>, copyItems flag: Bool)     class func orderedSetWithSet(_ set: Set<NSObject>, copyItems flag: Bool) -> Self     convenience init(object object: AnyObject)     convenience init(orderedSet set: NSOrderedSet)     convenience init(orderedSet set: NSOrderedSet, copyItems flag: Bool)     convenience init(orderedSet set: NSOrderedSet, range range: NSRange, copyItems flag: Bool)     convenience init(array array: [AnyObject])     convenience init(array set: [AnyObject], copyItems flag: Bool)     convenience init(array set: [AnyObject], range range: NSRange, copyItems flag: Bool)     convenience init(set set: Set<NSObject>)     convenience init(set set: Set<NSObject>, copyItems flag: Bool) } extension NSOrderedSet {     func filteredOrderedSetUsingPredicate(_ p: NSPredicate) -> NSOrderedSet } extension NSOrderedSet {     func sortedArrayUsingDescriptors(_ sortDescriptors: [NSSortDescriptor]) -> [AnyObject] } extension NSOrderedSet : ArrayLiteralConvertible {     required convenience init(arrayLiteral elements: AnyObject...) } extension NSOrderedSet {     convenience init(objects elements: AnyObject...) } extension NSOrderedSet : SequenceType {     func generate() -> NSFastGenerator } ``` |

Modified [NSOrderedSet.descriptionWithLocale(_: AnyObject?) -> String](https://developer.apple.com/documentation/foundation/nsorderedset/1417325-description)

|  | Declaration |
| --- | --- |
| From | ``` func descriptionWithLocale(_ locale: AnyObject?) -> String? ``` |
| To | ``` func descriptionWithLocale(_ locale: AnyObject?) -> String ``` |

Modified [NSOrderedSet.enumerateObjectsAtIndexes(_: NSIndexSet, options: NSEnumerationOptions, usingBlock: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/foundation/nsorderedset/1412332-enumerateobjects)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, usingBlock block: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, usingBlock block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [NSOrderedSet.enumerateObjectsUsingBlock(_: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/foundation/nsorderedset/1413531-enumerateobjectsusingblock)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateObjectsUsingBlock(_ block: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateObjectsUsingBlock(_ block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [NSOrderedSet.enumerateObjectsWithOptions(_: NSEnumerationOptions, usingBlock: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/foundation/nsorderedset/1409354-enumerateobjects)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [NSOrderedSet.indexesOfObjectsAtIndexes(_: NSIndexSet, options: NSEnumerationOptions, passingTest: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet](https://developer.apple.com/documentation/foundation/nsorderedset/1413586-indexes)

|  | Declaration |
| --- | --- |
| From | ``` func indexesOfObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet ``` |
| To | ``` func indexesOfObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet ``` |

Modified [NSOrderedSet.indexesOfObjectsPassingTest(_: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet](https://developer.apple.com/documentation/foundation/nsorderedset/1411331-indexesofobjectspassingtest)

|  | Declaration |
| --- | --- |
| From | ``` func indexesOfObjectsPassingTest(_ predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet ``` |
| To | ``` func indexesOfObjectsPassingTest(_ predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet ``` |

Modified [NSOrderedSet.indexesOfObjectsWithOptions(_: NSEnumerationOptions, passingTest: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet](https://developer.apple.com/documentation/foundation/nsorderedset/1415944-indexes)

|  | Declaration |
| --- | --- |
| From | ``` func indexesOfObjectsWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet ``` |
| To | ``` func indexesOfObjectsWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet ``` |

Modified [NSOrderedSet.indexOfObjectAtIndexes(_: NSIndexSet, options: NSEnumerationOptions, passingTest: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](https://developer.apple.com/documentation/foundation/nsorderedset/1417531-index)

|  | Declaration |
| --- | --- |
| From | ``` func indexOfObjectAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int ``` |
| To | ``` func indexOfObjectAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int ``` |

Modified [NSOrderedSet.indexOfObjectPassingTest(_: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](https://developer.apple.com/documentation/foundation/nsorderedset/1413003-index)

|  | Declaration |
| --- | --- |
| From | ``` func indexOfObjectPassingTest(_ predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int ``` |
| To | ``` func indexOfObjectPassingTest(_ predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int ``` |

Modified [NSOrderedSet.indexOfObjectWithOptions(_: NSEnumerationOptions, passingTest: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](https://developer.apple.com/documentation/foundation/nsorderedset/1408700-indexofobjectwithoptions)

|  | Declaration |
| --- | --- |
| From | ``` func indexOfObjectWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int ``` |
| To | ``` func indexOfObjectWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int ``` |

Modified [NSOrderedSet.sortedArrayUsingDescriptors(_: [NSSortDescriptor]) -> [AnyObject]](https://developer.apple.com/documentation/foundation/nsorderedset/1409953-sortedarrayusingdescriptors)

|  | Declaration |
| --- | --- |
| From | ``` func sortedArrayUsingDescriptors(_ sortDescriptors: [AnyObject]) -> [AnyObject] ``` |
| To | ``` func sortedArrayUsingDescriptors(_ sortDescriptors: [NSSortDescriptor]) -> [AnyObject] ``` |

Modified [NSOrderedSet.subscript(_: Int) -> AnyObject](https://developer.apple.com/documentation/foundation/nsorderedset/1414253-subscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (idx: Int) -> AnyObject { get } ``` |
| To | ``` subscript (_ idx: Int) -> AnyObject { get } ``` |

Modified [NSOrthography](https://developer.apple.com/documentation/foundation/nsorthography)

|  | Declaration |
| --- | --- |
| From | ``` class NSOrthography : NSObject, NSCopying, NSCoding {     var dominantScript: String { get }     var languageMap: [NSObject : AnyObject] { get }     init(dominantScript script: String, languageMap map: [NSObject : AnyObject])     init?(coder aDecoder: NSCoder) } extension NSOrthography {     func languagesForScript(_ script: String) -> [AnyObject]?     func dominantLanguageForScript(_ script: String) -> String     var dominantLanguage: String { get }     var allScripts: [AnyObject] { get }     var allLanguages: [AnyObject] { get } } extension NSOrthography {     convenience init(dominantScript script: String, languageMap map: [NSObject : AnyObject])     class func orthographyWithDominantScript(_ script: String, languageMap map: [NSObject : AnyObject]) -> Self } ``` |
| To | ``` class NSOrthography : NSObject, NSCopying, NSCoding {     var dominantScript: String { get }     var languageMap: [String : [String]] { get }     init(dominantScript script: String, languageMap map: [String : [String]])     init?(coder aDecoder: NSCoder) } extension NSOrthography {     func languagesForScript(_ script: String) -> [String]?     func dominantLanguageForScript(_ script: String) -> String?     var dominantLanguage: String { get }     var allScripts: [String] { get }     var allLanguages: [String] { get } } extension NSOrthography {     convenience init(dominantScript script: String, languageMap map: [String : [String]])     class func orthographyWithDominantScript(_ script: String, languageMap map: [String : [String]]) -> Self } ``` |

Modified [NSOrthography.allLanguages](https://developer.apple.com/documentation/foundation/nsorthography/1416205-alllanguages)

|  | Declaration |
| --- | --- |
| From | ``` var allLanguages: [AnyObject] { get } ``` |
| To | ``` var allLanguages: [String] { get } ``` |

Modified [NSOrthography.allScripts](https://developer.apple.com/documentation/foundation/nsorthography/1410722-allscripts)

|  | Declaration |
| --- | --- |
| From | ``` var allScripts: [AnyObject] { get } ``` |
| To | ``` var allScripts: [String] { get } ``` |

Modified [NSOrthography.dominantLanguageForScript(_: String) -> String?](https://developer.apple.com/documentation/foundation/nsorthography/1407326-dominantlanguage)

|  | Declaration |
| --- | --- |
| From | ``` func dominantLanguageForScript(_ script: String) -> String ``` |
| To | ``` func dominantLanguageForScript(_ script: String) -> String? ``` |

Modified [NSOrthography.init(dominantScript: String, languageMap: [String : [String]])](https://developer.apple.com/documentation/foundation/nsorthography/1408708-init)

|  | Declaration |
| --- | --- |
| From | ``` init(dominantScript script: String, languageMap map: [NSObject : AnyObject]) ``` |
| To | ``` init(dominantScript script: String, languageMap map: [String : [String]]) ``` |

Modified [NSOrthography.languageMap](https://developer.apple.com/documentation/foundation/nsorthography/1409533-languagemap)

|  | Declaration |
| --- | --- |
| From | ``` var languageMap: [NSObject : AnyObject] { get } ``` |
| To | ``` var languageMap: [String : [String]] { get } ``` |

Modified [NSOrthography.languagesForScript(_: String) -> [String]?](https://developer.apple.com/documentation/foundation/nsorthography/1412606-languages)

|  | Declaration |
| --- | --- |
| From | ``` func languagesForScript(_ script: String) -> [AnyObject]? ``` |
| To | ``` func languagesForScript(_ script: String) -> [String]? ``` |

Modified [NSPipe](https://developer.apple.com/documentation/foundation/nspipe)

|  | Declaration |
| --- | --- |
| From | ``` class NSPipe : NSObject {     var fileHandleForReading: NSFileHandle { get }     var fileHandleForWriting: NSFileHandle { get }     init!() -> NSPipe     class func pipe() -> NSPipe! } ``` |
| To | ``` class NSPipe : NSObject {     var fileHandleForReading: NSFileHandle { get }     var fileHandleForWriting: NSFileHandle { get }      init()     class func pipe() -> NSPipe } ``` |

Modified [NSPointerFunctions](https://developer.apple.com/documentation/foundation/nspointerfunctions)

|  | Declaration |
| --- | --- |
| From | ``` class NSPointerFunctions : NSObject, NSCopying {     init(options options: NSPointerFunctionsOptions)     class func pointerFunctionsWithOptions(_ options: NSPointerFunctionsOptions) -> NSPointerFunctions!     var hashFunction: CFunctionPointer<((UnsafePointer<Void>, CFunctionPointer<((UnsafePointer<Void>) -> Int)>) -> Int)>     var isEqualFunction: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>, CFunctionPointer<((UnsafePointer<Void>) -> Int)>) -> Bool)>     var sizeFunction: CFunctionPointer<((UnsafePointer<Void>) -> Int)>     var descriptionFunction: CFunctionPointer<((UnsafePointer<Void>) -> String!)>     var relinquishFunction: CFunctionPointer<((UnsafePointer<Void>, CFunctionPointer<((UnsafePointer<Void>) -> Int)>) -> Void)>     var acquireFunction: CFunctionPointer<((UnsafePointer<Void>, CFunctionPointer<((UnsafePointer<Void>) -> Int)>, Bool) -> UnsafeMutablePointer<Void>)>     var usesStrongWriteBarrier: Bool     var usesWeakReadAndWriteBarriers: Bool } ``` |
| To | ``` class NSPointerFunctions : NSObject, NSCopying {     init(options options: NSPointerFunctionsOptions)     class func pointerFunctionsWithOptions(_ options: NSPointerFunctionsOptions) -> NSPointerFunctions     var hashFunction: ((UnsafePointer<Void>, ((UnsafePointer<Void>) -> Int)?) -> Int)?     var isEqualFunction: ((UnsafePointer<Void>, UnsafePointer<Void>, ((UnsafePointer<Void>) -> Int)?) -> ObjCBool)?     var sizeFunction: ((UnsafePointer<Void>) -> Int)?     var descriptionFunction: ((UnsafePointer<Void>) -> String?)?     var relinquishFunction: ((UnsafePointer<Void>, ((UnsafePointer<Void>) -> Int)?) -> Void)?     var acquireFunction: ((UnsafePointer<Void>, ((UnsafePointer<Void>) -> Int)?, ObjCBool) -> UnsafeMutablePointer<Void>)?     var usesStrongWriteBarrier: Bool     var usesWeakReadAndWriteBarriers: Bool } ``` |

Modified [NSPointerFunctions.acquireFunction](https://developer.apple.com/documentation/foundation/nspointerfunctions/1410537-acquirefunction)

|  | Declaration |
| --- | --- |
| From | ``` var acquireFunction: CFunctionPointer<((UnsafePointer<Void>, CFunctionPointer<((UnsafePointer<Void>) -> Int)>, Bool) -> UnsafeMutablePointer<Void>)> ``` |
| To | ``` var acquireFunction: ((UnsafePointer<Void>, ((UnsafePointer<Void>) -> Int)?, ObjCBool) -> UnsafeMutablePointer<Void>)? ``` |

Modified [NSPointerFunctions.descriptionFunction](https://developer.apple.com/documentation/foundation/nspointerfunctions/1415200-descriptionfunction)

|  | Declaration |
| --- | --- |
| From | ``` var descriptionFunction: CFunctionPointer<((UnsafePointer<Void>) -> String!)> ``` |
| To | ``` var descriptionFunction: ((UnsafePointer<Void>) -> String?)? ``` |

Modified [NSPointerFunctions.hashFunction](https://developer.apple.com/documentation/foundation/nspointerfunctions/1415939-hashfunction)

|  | Declaration |
| --- | --- |
| From | ``` var hashFunction: CFunctionPointer<((UnsafePointer<Void>, CFunctionPointer<((UnsafePointer<Void>) -> Int)>) -> Int)> ``` |
| To | ``` var hashFunction: ((UnsafePointer<Void>, ((UnsafePointer<Void>) -> Int)?) -> Int)? ``` |

Modified [NSPointerFunctions.isEqualFunction](https://developer.apple.com/documentation/foundation/nspointerfunctions/1413473-isequalfunction)

|  | Declaration |
| --- | --- |
| From | ``` var isEqualFunction: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>, CFunctionPointer<((UnsafePointer<Void>) -> Int)>) -> Bool)> ``` |
| To | ``` var isEqualFunction: ((UnsafePointer<Void>, UnsafePointer<Void>, ((UnsafePointer<Void>) -> Int)?) -> ObjCBool)? ``` |

Modified [NSPointerFunctions.relinquishFunction](https://developer.apple.com/documentation/foundation/nspointerfunctions/1408565-relinquishfunction)

|  | Declaration |
| --- | --- |
| From | ``` var relinquishFunction: CFunctionPointer<((UnsafePointer<Void>, CFunctionPointer<((UnsafePointer<Void>) -> Int)>) -> Void)> ``` |
| To | ``` var relinquishFunction: ((UnsafePointer<Void>, ((UnsafePointer<Void>) -> Int)?) -> Void)? ``` |

Modified [NSPointerFunctions.sizeFunction](https://developer.apple.com/documentation/foundation/nspointerfunctions/1408045-sizefunction)

|  | Declaration |
| --- | --- |
| From | ``` var sizeFunction: CFunctionPointer<((UnsafePointer<Void>) -> Int)> ``` |
| To | ``` var sizeFunction: ((UnsafePointer<Void>) -> Int)? ``` |

Modified [NSPort](https://developer.apple.com/documentation/foundation/nsport)

|  | Declaration |
| --- | --- |
| From | ``` class NSPort : NSObject, NSCopying, NSCoding {     init!() -> NSPort     class func port() -> NSPort!     func invalidate()     var valid: Bool { get }     func setDelegate(_ anObject: NSPortDelegate?)     func delegate() -> NSPortDelegate?     func scheduleInRunLoop(_ runLoop: NSRunLoop, forMode mode: String)     func removeFromRunLoop(_ runLoop: NSRunLoop, forMode mode: String)     var reservedSpaceLength: Int { get }     func sendBeforeDate(_ limitDate: NSDate, components components: NSMutableArray, from receivePort: NSPort, reserved headerSpaceReserved: Int) -> Bool     func sendBeforeDate(_ limitDate: NSDate, msgid msgID: Int, components components: NSMutableArray, from receivePort: NSPort, reserved headerSpaceReserved: Int) -> Bool } ``` |
| To | ``` class NSPort : NSObject, NSCopying, NSCoding {      init()     class func port() -> NSPort     func invalidate()     var valid: Bool { get }     func setDelegate(_ anObject: NSPortDelegate?)     func delegate() -> NSPortDelegate?     func scheduleInRunLoop(_ runLoop: NSRunLoop, forMode mode: String)     func removeFromRunLoop(_ runLoop: NSRunLoop, forMode mode: String)     var reservedSpaceLength: Int { get }     func sendBeforeDate(_ limitDate: NSDate, components components: NSMutableArray?, from receivePort: NSPort?, reserved headerSpaceReserved: Int) -> Bool     func sendBeforeDate(_ limitDate: NSDate, msgid msgID: Int, components components: NSMutableArray?, from receivePort: NSPort?, reserved headerSpaceReserved: Int) -> Bool } ``` |

Modified [NSPort.sendBeforeDate(_: NSDate, components: NSMutableArray?, from: NSPort?, reserved: Int) -> Bool](https://developer.apple.com/documentation/foundation/port/1399537-send)

|  | Declaration |
| --- | --- |
| From | ``` func sendBeforeDate(_ limitDate: NSDate, components components: NSMutableArray, from receivePort: NSPort, reserved headerSpaceReserved: Int) -> Bool ``` |
| To | ``` func sendBeforeDate(_ limitDate: NSDate, components components: NSMutableArray?, from receivePort: NSPort?, reserved headerSpaceReserved: Int) -> Bool ``` |

Modified [NSPort.sendBeforeDate(_: NSDate, msgid: Int, components: NSMutableArray?, from: NSPort?, reserved: Int) -> Bool](https://developer.apple.com/documentation/foundation/port/1399482-send)

|  | Declaration |
| --- | --- |
| From | ``` func sendBeforeDate(_ limitDate: NSDate, msgid msgID: Int, components components: NSMutableArray, from receivePort: NSPort, reserved headerSpaceReserved: Int) -> Bool ``` |
| To | ``` func sendBeforeDate(_ limitDate: NSDate, msgid msgID: Int, components components: NSMutableArray?, from receivePort: NSPort?, reserved headerSpaceReserved: Int) -> Bool ``` |

Modified [NSPortDelegate](https://developer.apple.com/documentation/foundation/portdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol NSPortDelegate : NSObjectProtocol {     optional func handlePortMessage(_ message: NSPortMessage!) } ``` |
| To | ``` protocol NSPortDelegate : NSObjectProtocol {     optional func handlePortMessage(_ message: NSPortMessage) } ``` |

Modified [NSPortDelegate.handlePortMessage(_: NSPortMessage)](https://developer.apple.com/documentation/foundation/portdelegate/1399513-handle)

|  | Declaration |
| --- | --- |
| From | ``` optional func handlePortMessage(_ message: NSPortMessage!) ``` |
| To | ``` optional func handlePortMessage(_ message: NSPortMessage) ``` |

Modified [NSPostingStyle [enum]](https://developer.apple.com/documentation/foundation/nspostingstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSPredicate](https://developer.apple.com/documentation/foundation/nspredicate)

|  | Declaration |
| --- | --- |
| From | ``` class NSPredicate : NSObject, NSSecureCoding, NSCoding, NSCopying {     init(format predicateFormat: String, argumentArray arguments: [AnyObject]?) -> NSPredicate     class func predicateWithFormat(_ predicateFormat: String, argumentArray arguments: [AnyObject]?) -> NSPredicate     init(format predicateFormat: String, arguments argList: CVaListPointer) -> NSPredicate     class func predicateWithFormat(_ predicateFormat: String, arguments argList: CVaListPointer) -> NSPredicate     init?(fromMetadataQueryString queryString: String) -> NSPredicate     class func predicateFromMetadataQueryString(_ queryString: String) -> NSPredicate?     init(value value: Bool) -> NSPredicate     class func predicateWithValue(_ value: Bool) -> NSPredicate     init(block block: (AnyObject!, [NSObject : AnyObject]!) -> Bool) -> NSPredicate     class func predicateWithBlock(_ block: (AnyObject!, [NSObject : AnyObject]!) -> Bool) -> NSPredicate     var predicateFormat: String { get }     func predicateWithSubstitutionVariables(_ variables: [NSObject : AnyObject]) -> Self     func evaluateWithObject(_ object: AnyObject) -> Bool     func evaluateWithObject(_ object: AnyObject, substitutionVariables bindings: [NSObject : AnyObject]?) -> Bool     func allowEvaluation() } extension NSPredicate {     convenience init(format predicateFormat: String, _ args: CVarArgType...) } extension NSPredicate {     convenience init(format predicateFormat: String, _ args: CVarArgType...) } ``` |
| To | ``` class NSPredicate : NSObject, NSSecureCoding, NSCoding, NSCopying {      init(format predicateFormat: String, argumentArray arguments: [AnyObject]?)     class func predicateWithFormat(_ predicateFormat: String, argumentArray arguments: [AnyObject]?) -> NSPredicate      init(format predicateFormat: String, arguments argList: CVaListPointer)     class func predicateWithFormat(_ predicateFormat: String, arguments argList: CVaListPointer) -> NSPredicate      init?(fromMetadataQueryString queryString: String)     class func predicateFromMetadataQueryString(_ queryString: String) -> NSPredicate?      init(value value: Bool)     class func predicateWithValue(_ value: Bool) -> NSPredicate      init(block block: (AnyObject, [String : AnyObject]?) -> Bool)     class func predicateWithBlock(_ block: (AnyObject, [String : AnyObject]?) -> Bool) -> NSPredicate     var predicateFormat: String { get }     func predicateWithSubstitutionVariables(_ variables: [String : AnyObject]) -> Self     func evaluateWithObject(_ object: AnyObject?) -> Bool     func evaluateWithObject(_ object: AnyObject?, substitutionVariables bindings: [String : AnyObject]?) -> Bool     func allowEvaluation() } extension NSPredicate {     convenience init(format predicateFormat: String, _ args: CVarArgType...) } extension NSPredicate {     convenience init(format predicateFormat: String, _ args: CVarArgType...) } ``` |

Modified [NSPredicate.evaluateWithObject(_: AnyObject?) -> Bool](https://developer.apple.com/documentation/foundation/nspredicate/1417924-evaluatewithobject)

|  | Declaration |
| --- | --- |
| From | ``` func evaluateWithObject(_ object: AnyObject) -> Bool ``` |
| To | ``` func evaluateWithObject(_ object: AnyObject?) -> Bool ``` |

Modified [NSPredicate.evaluateWithObject(_: AnyObject?, substitutionVariables: [String : AnyObject]?) -> Bool](https://developer.apple.com/documentation/foundation/nspredicate/1407759-evaluatewithobject)

|  | Declaration |
| --- | --- |
| From | ``` func evaluateWithObject(_ object: AnyObject, substitutionVariables bindings: [NSObject : AnyObject]?) -> Bool ``` |
| To | ``` func evaluateWithObject(_ object: AnyObject?, substitutionVariables bindings: [String : AnyObject]?) -> Bool ``` |

Modified [NSPredicate.init(block: (AnyObject, [String : AnyObject]?) -> Bool)](https://developer.apple.com/documentation/foundation/nspredicate/1416182-init)

|  | Declaration |
| --- | --- |
| From | ``` init(block block: (AnyObject!, [NSObject : AnyObject]!) -> Bool) -> NSPredicate ``` |
| To | ``` init(block block: (AnyObject, [String : AnyObject]?) -> Bool) ``` |

Modified [NSPredicate.init(format: String, argumentArray: [AnyObject]?)](https://developer.apple.com/documentation/foundation/nspredicate/1410334-init)

|  | Declaration |
| --- | --- |
| From | ``` init(format predicateFormat: String, argumentArray arguments: [AnyObject]?) -> NSPredicate ``` |
| To | ``` init(format predicateFormat: String, argumentArray arguments: [AnyObject]?) ``` |

Modified [NSPredicate.init(format: String, arguments: CVaListPointer)](https://developer.apple.com/documentation/foundation/nspredicate/1417368-predicatewithformat)

|  | Declaration |
| --- | --- |
| From | ``` init(format predicateFormat: String, arguments argList: CVaListPointer) -> NSPredicate ``` |
| To | ``` init(format predicateFormat: String, arguments argList: CVaListPointer) ``` |

Modified [NSPredicate.init(value: Bool)](https://developer.apple.com/documentation/foundation/nspredicate/1417329-predicatewithvalue)

|  | Declaration |
| --- | --- |
| From | ``` init(value value: Bool) -> NSPredicate ``` |
| To | ``` init(value value: Bool) ``` |

Modified [NSPredicate.predicateWithSubstitutionVariables(_: [String : AnyObject]) -> Self](https://developer.apple.com/documentation/foundation/nspredicate/1413227-withsubstitutionvariables)

|  | Declaration |
| --- | --- |
| From | ``` func predicateWithSubstitutionVariables(_ variables: [NSObject : AnyObject]) -> Self ``` |
| To | ``` func predicateWithSubstitutionVariables(_ variables: [String : AnyObject]) -> Self ``` |

Modified [NSPredicateOperatorType [enum]](https://developer.apple.com/documentation/foundation/nspredicateoperatortype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSProcessInfo](https://developer.apple.com/documentation/foundation/processinfo)

|  | Declaration |
| --- | --- |
| From | ``` class NSProcessInfo : NSObject {     class func processInfo() -> NSProcessInfo     var environment: [NSObject : AnyObject] { get }     var arguments: [AnyObject] { get }     var hostName: String { get }     var processName: String     var processIdentifier: Int32 { get }     var globallyUniqueString: String { get }     func operatingSystem() -> Int     func operatingSystemName() -> String     var operatingSystemVersionString: String { get }     var operatingSystemVersion: NSOperatingSystemVersion { get }     var processorCount: Int { get }     var activeProcessorCount: Int { get }     var physicalMemory: UInt64 { get }     func isOperatingSystemAtLeastVersion(_ version: NSOperatingSystemVersion) -> Bool     var systemUptime: NSTimeInterval { get }     func disableSuddenTermination()     func enableSuddenTermination()     func disableAutomaticTermination(_ reason: String)     func enableAutomaticTermination(_ reason: String)     var automaticTerminationSupportEnabled: Bool } extension NSProcessInfo {     func beginActivityWithOptions(_ options: NSActivityOptions, reason reason: String) -> NSObjectProtocol     func endActivity(_ activity: NSObjectProtocol)     func performActivityWithOptions(_ options: NSActivityOptions, reason reason: String, usingBlock block: () -> Void)     func performExpiringActivityWithReason(_ reason: String!, usingBlock block: ((Bool) -> Void)!) } ``` |
| To | ``` class NSProcessInfo : NSObject {     class func processInfo() -> NSProcessInfo     var environment: [String : String] { get }     var arguments: [String] { get }     var hostName: String { get }     var processName: String     var processIdentifier: Int32 { get }     var globallyUniqueString: String { get }     func operatingSystem() -> Int     func operatingSystemName() -> String     var operatingSystemVersionString: String { get }     var operatingSystemVersion: NSOperatingSystemVersion { get }     var processorCount: Int { get }     var activeProcessorCount: Int { get }     var physicalMemory: UInt64 { get }     func isOperatingSystemAtLeastVersion(_ version: NSOperatingSystemVersion) -> Bool     var systemUptime: NSTimeInterval { get }     func disableSuddenTermination()     func enableSuddenTermination()     func disableAutomaticTermination(_ reason: String)     func enableAutomaticTermination(_ reason: String)     var automaticTerminationSupportEnabled: Bool } extension NSProcessInfo {     func beginActivityWithOptions(_ options: NSActivityOptions, reason reason: String) -> NSObjectProtocol     func endActivity(_ activity: NSObjectProtocol)     func performActivityWithOptions(_ options: NSActivityOptions, reason reason: String, usingBlock block: () -> Void)     func performExpiringActivityWithReason(_ reason: String, usingBlock block: (Bool) -> Void) } extension NSProcessInfo {     var thermalState: NSProcessInfoThermalState { get } } extension NSProcessInfo {     var lowPowerModeEnabled: Bool { get } } ``` |

Modified [NSProcessInfo.arguments](https://developer.apple.com/documentation/foundation/nsprocessinfo/1415596-arguments)

|  | Declaration |
| --- | --- |
| From | ``` var arguments: [AnyObject] { get } ``` |
| To | ``` var arguments: [String] { get } ``` |

Modified [NSProcessInfo.environment](https://developer.apple.com/documentation/foundation/processinfo/1417911-environment)

|  | Declaration |
| --- | --- |
| From | ``` var environment: [NSObject : AnyObject] { get } ``` |
| To | ``` var environment: [String : String] { get } ``` |

Modified [NSProcessInfo.performExpiringActivityWithReason(_: String, usingBlock: (Bool) -> Void)](https://developer.apple.com/documentation/foundation/nsprocessinfo/1617030-performexpiringactivitywithreaso)

|  | Declaration |
| --- | --- |
| From | ``` func performExpiringActivityWithReason(_ reason: String!, usingBlock block: ((Bool) -> Void)!) ``` |
| To | ``` func performExpiringActivityWithReason(_ reason: String, usingBlock block: (Bool) -> Void) ``` |

Modified [NSProgress](https://developer.apple.com/documentation/foundation/nsprogress)

|  | Declaration |
| --- | --- |
| From | ``` class NSProgress : NSObject {     class func currentProgress() -> NSProgress?     init(totalUnitCount unitCount: Int64) -> NSProgress     class func progressWithTotalUnitCount(_ unitCount: Int64) -> NSProgress     init(parent parentProgressOrNil: NSProgress?, userInfo userInfoOrNil: [NSObject : AnyObject]?)     func becomeCurrentWithPendingUnitCount(_ unitCount: Int64)     func resignCurrent()     var totalUnitCount: Int64     var completedUnitCount: Int64     var localizedDescription: String     var localizedAdditionalDescription: String     var cancellable: Bool     var pausable: Bool     var cancelled: Bool { get }     var paused: Bool { get }     var cancellationHandler: (() -> Void)?     var pausingHandler: (() -> Void)?     func setUserInfoObject(_ objectOrNil: AnyObject?, forKey key: String)     var indeterminate: Bool { get }     var fractionCompleted: Double { get }     func cancel()     func pause()     var userInfo: [NSObject : AnyObject]? { get }     var kind: String?     func publish()     func unpublish()     class func addSubscriberForFileURL(_ url: NSURL, withPublishingHandler publishingHandler: NSProgressPublishingHandler) -> AnyObject     class func removeSubscriber(_ subscriber: AnyObject)     var old: Bool { get } } ``` |
| To | ``` class NSProgress : NSObject {     class func currentProgress() -> NSProgress?      init(totalUnitCount unitCount: Int64)     class func progressWithTotalUnitCount(_ unitCount: Int64) -> NSProgress     class func discreteProgressWithTotalUnitCount(_ unitCount: Int64) -> NSProgress      init(totalUnitCount unitCount: Int64, parent parent: NSProgress, pendingUnitCount portionOfParentTotalUnitCount: Int64)     class func progressWithTotalUnitCount(_ unitCount: Int64, parent parent: NSProgress, pendingUnitCount portionOfParentTotalUnitCount: Int64) -> NSProgress     init(parent parentProgressOrNil: NSProgress?, userInfo userInfoOrNil: [NSObject : AnyObject]?)     func becomeCurrentWithPendingUnitCount(_ unitCount: Int64)     func resignCurrent()     func addChild(_ child: NSProgress, withPendingUnitCount inUnitCount: Int64)     var totalUnitCount: Int64     var completedUnitCount: Int64     var localizedDescription: String!     var localizedAdditionalDescription: String!     var cancellable: Bool     var pausable: Bool     var cancelled: Bool { get }     var paused: Bool { get }     var cancellationHandler: (() -> Void)?     var pausingHandler: (() -> Void)?     var resumingHandler: (() -> Void)?     func setUserInfoObject(_ objectOrNil: AnyObject?, forKey key: String)     var indeterminate: Bool { get }     var fractionCompleted: Double { get }     func cancel()     func pause()     func resume()     var userInfo: [NSObject : AnyObject] { get }     var kind: String?     func publish()     func unpublish()     class func addSubscriberForFileURL(_ url: NSURL, withPublishingHandler publishingHandler: NSProgressPublishingHandler) -> AnyObject     class func removeSubscriber(_ subscriber: AnyObject)     var old: Bool { get } } ``` |

Modified [NSProgress.init(totalUnitCount: Int64)](https://developer.apple.com/documentation/foundation/nsprogress/1415509-progresswithtotalunitcount)

|  | Declaration |
| --- | --- |
| From | ``` init(totalUnitCount unitCount: Int64) -> NSProgress ``` |
| To | ``` init(totalUnitCount unitCount: Int64) ``` |

Modified [NSProgress.localizedAdditionalDescription](https://developer.apple.com/documentation/foundation/nsprogress/1412455-localizedadditionaldescription)

|  | Declaration |
| --- | --- |
| From | ``` var localizedAdditionalDescription: String ``` |
| To | ``` var localizedAdditionalDescription: String! ``` |

Modified [NSProgress.localizedDescription](https://developer.apple.com/documentation/foundation/nsprogress/1417251-localizeddescription)

|  | Declaration |
| --- | --- |
| From | ``` var localizedDescription: String ``` |
| To | ``` var localizedDescription: String! ``` |

Modified [NSProgress.userInfo](https://developer.apple.com/documentation/foundation/nsprogress/1413314-userinfo)

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]? { get } ``` |
| To | ``` var userInfo: [NSObject : AnyObject] { get } ``` |

Modified [NSPropertyListFormat [enum]](https://developer.apple.com/documentation/foundation/nspropertylistformat)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSPropertyListMutabilityOptions [struct]](https://developer.apple.com/documentation/foundation/propertylistserialization/mutabilityoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSPropertyListMutabilityOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Immutable: NSPropertyListMutabilityOptions { get }     static var MutableContainers: NSPropertyListMutabilityOptions { get }     static var MutableContainersAndLeaves: NSPropertyListMutabilityOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSPropertyListMutabilityOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var Immutable: NSPropertyListMutabilityOptions { get }     static var MutableContainers: NSPropertyListMutabilityOptions { get }     static var MutableContainersAndLeaves: NSPropertyListMutabilityOptions { get } } ``` | OptionSetType |

Modified [NSPropertyListSerialization](https://developer.apple.com/documentation/foundation/nspropertylistserialization)

|  | Declaration |
| --- | --- |
| From | ``` class NSPropertyListSerialization : NSObject {     class func propertyList(_ plist: AnyObject, isValidForFormat format: NSPropertyListFormat) -> Bool     class func dataWithPropertyList(_ plist: AnyObject, format format: NSPropertyListFormat, options opt: NSPropertyListWriteOptions, error error: NSErrorPointer) -> NSData?     class func writePropertyList(_ plist: AnyObject, toStream stream: NSOutputStream, format format: NSPropertyListFormat, options opt: NSPropertyListWriteOptions, error error: NSErrorPointer) -> Int     class func propertyListWithData(_ data: NSData, options opt: NSPropertyListReadOptions, format format: UnsafeMutablePointer<NSPropertyListFormat>, error error: NSErrorPointer) -> AnyObject?     class func propertyListWithStream(_ stream: NSInputStream, options opt: NSPropertyListReadOptions, format format: UnsafeMutablePointer<NSPropertyListFormat>, error error: NSErrorPointer) -> AnyObject?     class func dataFromPropertyList(_ plist: AnyObject, format format: NSPropertyListFormat, errorDescription errorString: UnsafeMutablePointer<NSString?>) -> NSData?     class func propertyListFromData(_ data: NSData, mutabilityOption opt: NSPropertyListMutabilityOptions, format format: UnsafeMutablePointer<NSPropertyListFormat>, errorDescription errorString: UnsafeMutablePointer<NSString?>) -> AnyObject? } ``` |
| To | ``` class NSPropertyListSerialization : NSObject {     class func propertyList(_ plist: AnyObject, isValidForFormat format: NSPropertyListFormat) -> Bool     class func dataWithPropertyList(_ plist: AnyObject, format format: NSPropertyListFormat, options opt: NSPropertyListWriteOptions) throws -> NSData     class func writePropertyList(_ plist: AnyObject, toStream stream: NSOutputStream, format format: NSPropertyListFormat, options opt: NSPropertyListWriteOptions, error error: NSErrorPointer) -> Int     class func propertyListWithData(_ data: NSData, options opt: NSPropertyListReadOptions, format format: UnsafeMutablePointer<NSPropertyListFormat>) throws -> AnyObject     class func propertyListWithStream(_ stream: NSInputStream, options opt: NSPropertyListReadOptions, format format: UnsafeMutablePointer<NSPropertyListFormat>) throws -> AnyObject     class func dataFromPropertyList(_ plist: AnyObject, format format: NSPropertyListFormat, errorDescription errorString: UnsafeMutablePointer<NSString?>) -> NSData?     class func propertyListFromData(_ data: NSData, mutabilityOption opt: NSPropertyListMutabilityOptions, format format: UnsafeMutablePointer<NSPropertyListFormat>, errorDescription errorString: UnsafeMutablePointer<NSString?>) -> AnyObject? } ``` |

Modified [NSPropertyListSerialization.dataWithPropertyList(_: AnyObject, format: NSPropertyListFormat, options: NSPropertyListWriteOptions) throws -> NSData [class]](https://developer.apple.com/documentation/foundation/propertylistserialization/1418309-data)

|  | Declaration |
| --- | --- |
| From | ``` class func dataWithPropertyList(_ plist: AnyObject, format format: NSPropertyListFormat, options opt: NSPropertyListWriteOptions, error error: NSErrorPointer) -> NSData? ``` |
| To | ``` class func dataWithPropertyList(_ plist: AnyObject, format format: NSPropertyListFormat, options opt: NSPropertyListWriteOptions) throws -> NSData ``` |

Modified [NSPropertyListSerialization.propertyListWithData(_: NSData, options: NSPropertyListReadOptions, format: UnsafeMutablePointer<NSPropertyListFormat>) throws -> AnyObject [class]](https://developer.apple.com/documentation/foundation/nspropertylistserialization/1409678-propertylistwithdata)

|  | Declaration |
| --- | --- |
| From | ``` class func propertyListWithData(_ data: NSData, options opt: NSPropertyListReadOptions, format format: UnsafeMutablePointer<NSPropertyListFormat>, error error: NSErrorPointer) -> AnyObject? ``` |
| To | ``` class func propertyListWithData(_ data: NSData, options opt: NSPropertyListReadOptions, format format: UnsafeMutablePointer<NSPropertyListFormat>) throws -> AnyObject ``` |

Modified [NSPropertyListSerialization.propertyListWithStream(_: NSInputStream, options: NSPropertyListReadOptions, format: UnsafeMutablePointer<NSPropertyListFormat>) throws -> AnyObject [class]](https://developer.apple.com/documentation/foundation/nspropertylistserialization/1415468-propertylistwithstream)

|  | Declaration |
| --- | --- |
| From | ``` class func propertyListWithStream(_ stream: NSInputStream, options opt: NSPropertyListReadOptions, format format: UnsafeMutablePointer<NSPropertyListFormat>, error error: NSErrorPointer) -> AnyObject? ``` |
| To | ``` class func propertyListWithStream(_ stream: NSInputStream, options opt: NSPropertyListReadOptions, format format: UnsafeMutablePointer<NSPropertyListFormat>) throws -> AnyObject ``` |

Modified [NSProxy](https://developer.apple.com/documentation/foundation/nsproxy)

|  | Declaration |
| --- | --- |
| From | ``` class NSProxy : NSObjectProtocol {     class func alloc() -> Self     class func allocWithZone(_ zone: NSZone) -> Self!     class func `class`() -> AnyClass     func forwardInvocation(_ invocation: NSInvocation)     func methodSignatureForSelector(_ sel: Selector) -> NSMethodSignature!     func dealloc()     func finalize()     var description: String { get }     var debugDescription: String { get }     class func respondsToSelector(_ aSelector: Selector) -> Bool     func allowsWeakReference() -> Bool     func retainWeakReference() -> Bool } ``` |
| To | ``` class NSProxy : NSObjectProtocol {     class func alloc() -> Self     class func allocWithZone(_ zone: NSZone) -> Self     class func `class`() -> AnyClass     func forwardInvocation(_ invocation: NSInvocation)     func methodSignatureForSelector(_ sel: Selector) -> NSMethodSignature?     func finalize()     var description: String { get }     var debugDescription: String { get }     class func respondsToSelector(_ aSelector: Selector) -> Bool     func allowsWeakReference() -> Bool     func retainWeakReference() -> Bool } ``` |

Modified [NSQualityOfService [enum]](https://developer.apple.com/documentation/foundation/nsqualityofservice)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified NSRange.toRange() -> Range<Int>?

|  | Declaration |
| --- | --- |
| From | ``` func toRange() -> Range<Int>? ``` |
| To | ``` @warn_unused_result     func toRange() -> Range<Int>? ``` |

Modified [NSRegularExpression](https://developer.apple.com/documentation/foundation/nsregularexpression)

|  | Declaration |
| --- | --- |
| From | ``` class NSRegularExpression : NSObject, NSCopying, NSCoding {     init?(pattern pattern: String, options options: NSRegularExpressionOptions, error error: NSErrorPointer) -> NSRegularExpression     class func regularExpressionWithPattern(_ pattern: String, options options: NSRegularExpressionOptions, error error: NSErrorPointer) -> NSRegularExpression?     init?(pattern pattern: String, options options: NSRegularExpressionOptions, error error: NSErrorPointer)     var pattern: String { get }     var options: NSRegularExpressionOptions { get }     var numberOfCaptureGroups: Int { get }     class func escapedPatternForString(_ string: String) -> String } extension NSRegularExpression {     func enumerateMatchesInString(_ string: String, options options: NSMatchingOptions, range range: NSRange, usingBlock block: (NSTextCheckingResult!, NSMatchingFlags, UnsafeMutablePointer<ObjCBool>) -> Void)     func matchesInString(_ string: String, options options: NSMatchingOptions, range range: NSRange) -> [AnyObject]     func numberOfMatchesInString(_ string: String, options options: NSMatchingOptions, range range: NSRange) -> Int     func firstMatchInString(_ string: String, options options: NSMatchingOptions, range range: NSRange) -> NSTextCheckingResult?     func rangeOfFirstMatchInString(_ string: String, options options: NSMatchingOptions, range range: NSRange) -> NSRange } extension NSRegularExpression {     func stringByReplacingMatchesInString(_ string: String, options options: NSMatchingOptions, range range: NSRange, withTemplate templ: String) -> String     func replaceMatchesInString(_ string: NSMutableString, options options: NSMatchingOptions, range range: NSRange, withTemplate templ: String) -> Int     func replacementStringForResult(_ result: NSTextCheckingResult, inString string: String, offset offset: Int, template templ: String) -> String     class func escapedTemplateForString(_ string: String) -> String } ``` |
| To | ``` class NSRegularExpression : NSObject, NSCopying, NSCoding {      init(pattern pattern: String, options options: NSRegularExpressionOptions) throws     class func regularExpressionWithPattern(_ pattern: String, options options: NSRegularExpressionOptions) throws -> NSRegularExpression     init(pattern pattern: String, options options: NSRegularExpressionOptions) throws     var pattern: String { get }     var options: NSRegularExpressionOptions { get }     var numberOfCaptureGroups: Int { get }     class func escapedPatternForString(_ string: String) -> String } extension NSRegularExpression {     func enumerateMatchesInString(_ string: String, options options: NSMatchingOptions, range range: NSRange, usingBlock block: (NSTextCheckingResult?, NSMatchingFlags, UnsafeMutablePointer<ObjCBool>) -> Void)     func matchesInString(_ string: String, options options: NSMatchingOptions, range range: NSRange) -> [NSTextCheckingResult]     func numberOfMatchesInString(_ string: String, options options: NSMatchingOptions, range range: NSRange) -> Int     func firstMatchInString(_ string: String, options options: NSMatchingOptions, range range: NSRange) -> NSTextCheckingResult?     func rangeOfFirstMatchInString(_ string: String, options options: NSMatchingOptions, range range: NSRange) -> NSRange } extension NSRegularExpression {     func stringByReplacingMatchesInString(_ string: String, options options: NSMatchingOptions, range range: NSRange, withTemplate templ: String) -> String     func replaceMatchesInString(_ string: NSMutableString, options options: NSMatchingOptions, range range: NSRange, withTemplate templ: String) -> Int     func replacementStringForResult(_ result: NSTextCheckingResult, inString string: String, offset offset: Int, template templ: String) -> String     class func escapedTemplateForString(_ string: String) -> String } ``` |

Modified [NSRegularExpression.enumerateMatchesInString(_: String, options: NSMatchingOptions, range: NSRange, usingBlock: (NSTextCheckingResult?, NSMatchingFlags, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/foundation/nsregularexpression/1409687-enumeratematchesinstring)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateMatchesInString(_ string: String, options options: NSMatchingOptions, range range: NSRange, usingBlock block: (NSTextCheckingResult!, NSMatchingFlags, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateMatchesInString(_ string: String, options options: NSMatchingOptions, range range: NSRange, usingBlock block: (NSTextCheckingResult?, NSMatchingFlags, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [NSRegularExpression.init(pattern: String, options: NSRegularExpressionOptions) throws](https://developer.apple.com/documentation/foundation/nsregularexpression/1410900-init)

|  | Declaration |
| --- | --- |
| From | ``` init?(pattern pattern: String, options options: NSRegularExpressionOptions, error error: NSErrorPointer) ``` |
| To | ``` init(pattern pattern: String, options options: NSRegularExpressionOptions) throws ``` |

Modified [NSRegularExpression.matchesInString(_: String, options: NSMatchingOptions, range: NSRange) -> [NSTextCheckingResult]](https://developer.apple.com/documentation/foundation/nsregularexpression/1412446-matches)

|  | Declaration |
| --- | --- |
| From | ``` func matchesInString(_ string: String, options options: NSMatchingOptions, range range: NSRange) -> [AnyObject] ``` |
| To | ``` func matchesInString(_ string: String, options options: NSMatchingOptions, range range: NSRange) -> [NSTextCheckingResult] ``` |

Modified [NSRegularExpressionOptions [struct]](https://developer.apple.com/documentation/foundation/nsregularexpressionoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSRegularExpressionOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var CaseInsensitive: NSRegularExpressionOptions { get }     static var AllowCommentsAndWhitespace: NSRegularExpressionOptions { get }     static var IgnoreMetacharacters: NSRegularExpressionOptions { get }     static var DotMatchesLineSeparators: NSRegularExpressionOptions { get }     static var AnchorsMatchLines: NSRegularExpressionOptions { get }     static var UseUnixLineSeparators: NSRegularExpressionOptions { get }     static var UseUnicodeWordBoundaries: NSRegularExpressionOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSRegularExpressionOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var CaseInsensitive: NSRegularExpressionOptions { get }     static var AllowCommentsAndWhitespace: NSRegularExpressionOptions { get }     static var IgnoreMetacharacters: NSRegularExpressionOptions { get }     static var DotMatchesLineSeparators: NSRegularExpressionOptions { get }     static var AnchorsMatchLines: NSRegularExpressionOptions { get }     static var UseUnixLineSeparators: NSRegularExpressionOptions { get }     static var UseUnicodeWordBoundaries: NSRegularExpressionOptions { get } } ``` | OptionSetType |

Modified [NSRoundingMode [enum]](https://developer.apple.com/documentation/foundation/decimal/roundingmode-vau)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSRunLoop](https://developer.apple.com/documentation/foundation/nsrunloop)

|  | Declaration |
| --- | --- |
| From | ``` class NSRunLoop : NSObject {     class func currentRunLoop() -> NSRunLoop     class func mainRunLoop() -> NSRunLoop     var currentMode: String? { get }     func getCFRunLoop() -> CFRunLoop     func addTimer(_ timer: NSTimer, forMode mode: String)     func addPort(_ aPort: NSPort, forMode mode: String)     func removePort(_ aPort: NSPort, forMode mode: String)     func limitDateForMode(_ mode: String) -> NSDate?     func acceptInputForMode(_ mode: String, beforeDate limitDate: NSDate) } extension NSRunLoop {     func run()     func runUntilDate(_ limitDate: NSDate)     func runMode(_ mode: String, beforeDate limitDate: NSDate) -> Bool } extension NSRunLoop {     func performSelector(_ aSelector: Selector, target target: AnyObject, argument arg: AnyObject?, order order: Int, modes modes: [AnyObject])     func cancelPerformSelector(_ aSelector: Selector, target target: AnyObject, argument arg: AnyObject?)     func cancelPerformSelectorsWithTarget(_ target: AnyObject) } ``` |
| To | ``` class NSRunLoop : NSObject {     class func currentRunLoop() -> NSRunLoop     class func mainRunLoop() -> NSRunLoop     var currentMode: String? { get }     func getCFRunLoop() -> CFRunLoop     func addTimer(_ timer: NSTimer, forMode mode: String)     func addPort(_ aPort: NSPort, forMode mode: String)     func removePort(_ aPort: NSPort, forMode mode: String)     func limitDateForMode(_ mode: String) -> NSDate?     func acceptInputForMode(_ mode: String, beforeDate limitDate: NSDate) } extension NSRunLoop {     func run()     func runUntilDate(_ limitDate: NSDate)     func runMode(_ mode: String, beforeDate limitDate: NSDate) -> Bool } extension NSRunLoop {     func performSelector(_ aSelector: Selector, target target: AnyObject, argument arg: AnyObject?, order order: Int, modes modes: [String])     func cancelPerformSelector(_ aSelector: Selector, target target: AnyObject, argument arg: AnyObject?)     func cancelPerformSelectorsWithTarget(_ target: AnyObject) } ``` |

Modified [NSSearchPathDirectory [enum]](https://developer.apple.com/documentation/foundation/filemanager/searchpathdirectory)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSSearchPathDomainMask [struct]](https://developer.apple.com/documentation/foundation/filemanager/searchpathdomainmask)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSSearchPathDomainMask : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var UserDomainMask: NSSearchPathDomainMask { get }     static var LocalDomainMask: NSSearchPathDomainMask { get }     static var NetworkDomainMask: NSSearchPathDomainMask { get }     static var SystemDomainMask: NSSearchPathDomainMask { get }     static var AllDomainsMask: NSSearchPathDomainMask { get } } ``` | RawOptionSetType |
| To | ``` struct NSSearchPathDomainMask : OptionSetType {     init(rawValue rawValue: UInt)     static var UserDomainMask: NSSearchPathDomainMask { get }     static var LocalDomainMask: NSSearchPathDomainMask { get }     static var NetworkDomainMask: NSSearchPathDomainMask { get }     static var SystemDomainMask: NSSearchPathDomainMask { get }     static var AllDomainsMask: NSSearchPathDomainMask { get } } ``` | OptionSetType |

Modified [NSSet](https://developer.apple.com/documentation/foundation/nsset)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSSet : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding, NSFastEnumeration {     var count: Int { get }     func member(_ object: AnyObject) -> AnyObject?     func objectEnumerator() -> NSEnumerator     init()     init(objects objects: UnsafePointer<AnyObject?>, count cnt: Int)     init?(coder aDecoder: NSCoder) } extension NSSet {     func valueForKey(_ key: String) -> AnyObject     func setValue(_ value: AnyObject?, forKey key: String) } extension NSSet {     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String) } extension NSSet {     func filteredSetUsingPredicate(_ predicate: NSPredicate) -> Set<NSObject> } extension NSSet : SequenceType {     func generate() -> NSFastGenerator } extension NSSet {     convenience init(objects elements: AnyObject...) } extension NSSet : ArrayLiteralConvertible {     required convenience init(arrayLiteral elements: AnyObject...) } extension NSSet {     @objc(_swiftInitWithSet_NSSet:) convenience init(set anSet: NSSet) } extension NSSet : Reflectable {     func getMirror() -> MirrorType } extension NSSet {     var allObjects: [AnyObject] { get }     func anyObject() -> AnyObject?     func containsObject(_ anObject: AnyObject) -> Bool     var description: String { get }     func descriptionWithLocale(_ locale: AnyObject?) -> String     func intersectsSet(_ otherSet: Set<NSObject>) -> Bool     func isEqualToSet(_ otherSet: Set<NSObject>) -> Bool     func isSubsetOfSet(_ otherSet: Set<NSObject>) -> Bool     func makeObjectsPerformSelector(_ aSelector: Selector)     func makeObjectsPerformSelector(_ aSelector: Selector, withObject argument: AnyObject?)     func setByAddingObject(_ anObject: AnyObject) -> Set<NSObject>     func setByAddingObjectsFromSet(_ other: Set<NSObject>) -> Set<NSObject>     func setByAddingObjectsFromArray(_ other: [AnyObject]) -> Set<NSObject>     func enumerateObjectsUsingBlock(_ block: (AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Void)     func objectsPassingTest(_ predicate: (AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject>     func objectsWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject> } extension NSSet {     class func set() -> Self!     convenience init(object object: AnyObject)     class func setWithObject(_ object: AnyObject) -> Self     class func setWithObjects(_ objects: UnsafePointer<AnyObject?>, count cnt: Int) -> Self!     convenience init(set set: Set<NSObject>)     class func setWithSet(_ set: Set<NSObject>) -> Self     convenience init(array array: [AnyObject])     class func setWithArray(_ array: [AnyObject]) -> Self     convenience init(set set: Set<NSObject>)     convenience init(set set: Set<NSObject>, copyItems flag: Bool)     convenience init(array array: [AnyObject]) } extension NSSet {     func sortedArrayUsingDescriptors(_ sortDescriptors: [AnyObject]) -> [AnyObject] } extension NSSet : Reflectable {     func getMirror() -> MirrorType } extension NSSet {     @objc(_swiftInitWithSet_NSSet:) convenience init(set anSet: NSSet) } extension NSSet : ArrayLiteralConvertible {     required convenience init(arrayLiteral elements: AnyObject...) } extension NSSet {     convenience init(objects elements: AnyObject...) } extension NSSet : SequenceType {     func generate() -> NSFastGenerator } ``` | AnyObject, ArrayLiteralConvertible, NSCoding, NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding, Reflectable, SequenceType |
| To | ``` class NSSet : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding, NSFastEnumeration {     var count: Int { get }     func member(_ object: AnyObject) -> AnyObject?     func objectEnumerator() -> NSEnumerator     init()     init(objects objects: UnsafePointer<AnyObject?>, count cnt: Int)     init?(coder aDecoder: NSCoder) } extension NSSet {     func valueForKey(_ key: String) -> AnyObject     func setValue(_ value: AnyObject?, forKey key: String) } extension NSSet {     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String) } extension NSSet {     func filteredSetUsingPredicate(_ predicate: NSPredicate) -> Set<NSObject> } extension NSSet : SequenceType {     func generate() -> NSFastGenerator } extension NSSet {     convenience init(objects elements: AnyObject...) } extension NSSet : ArrayLiteralConvertible {     required convenience init(arrayLiteral elements: AnyObject...) } extension NSSet {     @objc(_swiftInitWithSet_NSSet:) convenience init(set anSet: NSSet) } extension NSSet : _Reflectable { } extension NSSet {     var allObjects: [AnyObject] { get }     func anyObject() -> AnyObject?     func containsObject(_ anObject: AnyObject) -> Bool     var description: String { get }     func descriptionWithLocale(_ locale: AnyObject?) -> String     func intersectsSet(_ otherSet: Set<NSObject>) -> Bool     func isEqualToSet(_ otherSet: Set<NSObject>) -> Bool     func isSubsetOfSet(_ otherSet: Set<NSObject>) -> Bool     func makeObjectsPerformSelector(_ aSelector: Selector)     func makeObjectsPerformSelector(_ aSelector: Selector, withObject argument: AnyObject?)     func setByAddingObject(_ anObject: AnyObject) -> Set<NSObject>     func setByAddingObjectsFromSet(_ other: Set<NSObject>) -> Set<NSObject>     func setByAddingObjectsFromArray(_ other: [AnyObject]) -> Set<NSObject>     func enumerateObjectsUsingBlock(_ block: (AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void)     func objectsPassingTest(_ predicate: (AnyObject, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject>     func objectsWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject> } extension NSSet {     class func set() -> Self     convenience init(object object: AnyObject)     class func setWithObject(_ object: AnyObject) -> Self     class func setWithObjects(_ objects: UnsafePointer<AnyObject?>, count cnt: Int) -> Self     convenience init(set set: Set<NSObject>)     class func setWithSet(_ set: Set<NSObject>) -> Self     convenience init(array array: [AnyObject])     class func setWithArray(_ array: [AnyObject]) -> Self     convenience init(set set: Set<NSObject>)     convenience init(set set: Set<NSObject>, copyItems flag: Bool)     convenience init(array array: [AnyObject]) } extension NSSet {     func sortedArrayUsingDescriptors(_ sortDescriptors: [NSSortDescriptor]) -> [AnyObject] } extension NSSet : _Reflectable { } extension NSSet {     @objc(_swiftInitWithSet_NSSet:) convenience init(set anSet: NSSet) } extension NSSet : ArrayLiteralConvertible {     required convenience init(arrayLiteral elements: AnyObject...) } extension NSSet {     convenience init(objects elements: AnyObject...) } extension NSSet : SequenceType {     func generate() -> NSFastGenerator } ``` | AnyObject, ArrayLiteralConvertible, NSCoding, NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding, SequenceType |

Modified [NSSet.enumerateObjectsUsingBlock(_: (AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/foundation/nsset/1418129-enumerateobjects)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateObjectsUsingBlock(_ block: (AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateObjectsUsingBlock(_ block: (AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [NSSet.enumerateObjectsWithOptions(_: NSEnumerationOptions, usingBlock: (AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/foundation/nsset/1412024-enumerateobjects)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [NSSet.objectsPassingTest(_: (AnyObject, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject>](https://developer.apple.com/documentation/foundation/nsset/1414392-objects)

|  | Declaration |
| --- | --- |
| From | ``` func objectsPassingTest(_ predicate: (AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject> ``` |
| To | ``` func objectsPassingTest(_ predicate: (AnyObject, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject> ``` |

Modified [NSSet.objectsWithOptions(_: NSEnumerationOptions, passingTest: (AnyObject, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject>](https://developer.apple.com/documentation/foundation/nsset/1416826-objects)

|  | Declaration |
| --- | --- |
| From | ``` func objectsWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject> ``` |
| To | ``` func objectsWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject> ``` |

Modified [NSSet.sortedArrayUsingDescriptors(_: [NSSortDescriptor]) -> [AnyObject]](https://developer.apple.com/documentation/foundation/nsset/1416427-sortedarrayusingdescriptors)

|  | Declaration |
| --- | --- |
| From | ``` func sortedArrayUsingDescriptors(_ sortDescriptors: [AnyObject]) -> [AnyObject] ``` |
| To | ``` func sortedArrayUsingDescriptors(_ sortDescriptors: [NSSortDescriptor]) -> [AnyObject] ``` |

Modified [NSSortDescriptor](https://developer.apple.com/documentation/foundation/nssortdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` class NSSortDescriptor : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init(key key: String, ascending ascending: Bool)     class func sortDescriptorWithKey(_ key: String, ascending ascending: Bool) -> Self     convenience init(key key: String, ascending ascending: Bool, selector selector: Selector)     class func sortDescriptorWithKey(_ key: String, ascending ascending: Bool, selector selector: Selector) -> Self     init(key key: String, ascending ascending: Bool)     init(key key: String, ascending ascending: Bool, selector selector: Selector)     var key: String? { get }     var ascending: Bool { get }     var selector: Selector { get }     func allowEvaluation()     convenience init(key key: String, ascending ascending: Bool, comparator cmptr: NSComparator)     class func sortDescriptorWithKey(_ key: String, ascending ascending: Bool, comparator cmptr: NSComparator) -> Self     init(key key: String, ascending ascending: Bool, comparator cmptr: NSComparator)     var comparator: NSComparator? { get }     func compareObject(_ object1: AnyObject, toObject object2: AnyObject) -> NSComparisonResult     var reversedSortDescriptor: AnyObject! { get } } ``` |
| To | ``` class NSSortDescriptor : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init(key key: String?, ascending ascending: Bool)     class func sortDescriptorWithKey(_ key: String?, ascending ascending: Bool) -> Self     convenience init(key key: String?, ascending ascending: Bool, selector selector: Selector)     class func sortDescriptorWithKey(_ key: String?, ascending ascending: Bool, selector selector: Selector) -> Self     init(key key: String?, ascending ascending: Bool)     init(key key: String?, ascending ascending: Bool, selector selector: Selector)     init?(coder coder: NSCoder)     var key: String? { get }     var ascending: Bool { get }     var selector: Selector { get }     func allowEvaluation()     convenience init(key key: String?, ascending ascending: Bool, comparator cmptr: NSComparator)     class func sortDescriptorWithKey(_ key: String?, ascending ascending: Bool, comparator cmptr: NSComparator) -> Self     init(key key: String?, ascending ascending: Bool, comparator cmptr: NSComparator)     var comparator: NSComparator { get }     func compareObject(_ object1: AnyObject, toObject object2: AnyObject) -> NSComparisonResult     var reversedSortDescriptor: AnyObject { get } } ``` |

Modified [NSSortDescriptor.comparator](https://developer.apple.com/documentation/foundation/nssortdescriptor/1411426-comparator)

|  | Declaration |
| --- | --- |
| From | ``` var comparator: NSComparator? { get } ``` |
| To | ``` var comparator: NSComparator { get } ``` |

Modified [NSSortDescriptor.init(key: String?, ascending: Bool)](https://developer.apple.com/documentation/foundation/nssortdescriptor/1413572-initwithkey)

|  | Declaration |
| --- | --- |
| From | ``` init(key key: String, ascending ascending: Bool) ``` |
| To | ``` init(key key: String?, ascending ascending: Bool) ``` |

Modified [NSSortDescriptor.init(key: String?, ascending: Bool, comparator: NSComparator)](https://developer.apple.com/documentation/foundation/nssortdescriptor/1411607-initwithkey)

|  | Declaration |
| --- | --- |
| From | ``` init(key key: String, ascending ascending: Bool, comparator cmptr: NSComparator) ``` |
| To | ``` init(key key: String?, ascending ascending: Bool, comparator cmptr: NSComparator) ``` |

Modified [NSSortDescriptor.init(key: String?, ascending: Bool, selector: Selector)](https://developer.apple.com/documentation/foundation/nssortdescriptor/1412495-initwithkey)

|  | Declaration |
| --- | --- |
| From | ``` init(key key: String, ascending ascending: Bool, selector selector: Selector) ``` |
| To | ``` init(key key: String?, ascending ascending: Bool, selector selector: Selector) ``` |

Modified [NSSortDescriptor.reversedSortDescriptor](https://developer.apple.com/documentation/foundation/nssortdescriptor/1407712-reversedsortdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` var reversedSortDescriptor: AnyObject! { get } ``` |
| To | ``` var reversedSortDescriptor: AnyObject { get } ``` |

Modified [NSSortOptions [struct]](https://developer.apple.com/documentation/foundation/nssortoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSSortOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Concurrent: NSSortOptions { get }     static var Stable: NSSortOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSSortOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var Concurrent: NSSortOptions { get }     static var Stable: NSSortOptions { get } } ``` | OptionSetType |

Modified [NSStreamEvent [struct]](https://developer.apple.com/documentation/foundation/nsstreamevent)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSStreamEvent : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: NSStreamEvent { get }     static var OpenCompleted: NSStreamEvent { get }     static var HasBytesAvailable: NSStreamEvent { get }     static var HasSpaceAvailable: NSStreamEvent { get }     static var ErrorOccurred: NSStreamEvent { get }     static var EndEncountered: NSStreamEvent { get } } ``` | RawOptionSetType |
| To | ``` struct NSStreamEvent : OptionSetType {     init(rawValue rawValue: UInt)     static var None: NSStreamEvent { get }     static var OpenCompleted: NSStreamEvent { get }     static var HasBytesAvailable: NSStreamEvent { get }     static var HasSpaceAvailable: NSStreamEvent { get }     static var ErrorOccurred: NSStreamEvent { get }     static var EndEncountered: NSStreamEvent { get } } ``` | OptionSetType |

Modified [NSStreamStatus [enum]](https://developer.apple.com/documentation/foundation/nsstreamstatus)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSString](https://developer.apple.com/documentation/foundation/nsstring)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSString : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     var length: Int { get }     func characterAtIndex(_ index: Int) -> unichar     init()     init(coder aDecoder: NSCoder) } extension NSString : CKRecordValue, NSObjectProtocol { } extension NSString {     func linguisticTagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, orthography orthography: NSOrthography?, tokenRanges tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [AnyObject]     func enumerateLinguisticTagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, orthography orthography: NSOrthography?, usingBlock block: (String!, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) } extension NSString {     class func pathWithComponents(_ components: [AnyObject]) -> String     var pathComponents: [AnyObject] { get }     var absolutePath: Bool { get }     var lastPathComponent: String { get }     var stringByDeletingLastPathComponent: String { get }     func stringByAppendingPathComponent(_ str: String) -> String     var pathExtension: String { get }     var stringByDeletingPathExtension: String { get }     func stringByAppendingPathExtension(_ str: String) -> String?     var stringByAbbreviatingWithTildeInPath: String { get }     var stringByExpandingTildeInPath: String { get }     var stringByStandardizingPath: String { get }     var stringByResolvingSymlinksInPath: String { get }     func stringsByAppendingPaths(_ paths: [AnyObject]) -> [AnyObject]     func completePathIntoString(_ outputName: AutoreleasingUnsafeMutablePointer<NSString?>, caseSensitive flag: Bool, matchesIntoArray outputArray: AutoreleasingUnsafeMutablePointer<NSArray?>, filterTypes filterTypes: [AnyObject]?) -> Int     var fileSystemRepresentation: UnsafePointer<Int8> { get }     func getFileSystemRepresentation(_ cname: UnsafeMutablePointer<Int8>, maxLength max: Int) -> Bool } extension NSString : StringLiteralConvertible {     required convenience init(unicodeScalarLiteral value: StaticString)     required convenience init(extendedGraphemeClusterLiteral value: StaticString)     required convenience init(stringLiteral value: StaticString) } extension NSString : _CocoaStringType { } extension NSString {     convenience init(format format: NSString, _ args: CVarArgType...)     convenience init(format format: NSString, locale locale: NSLocale?, _ args: CVarArgType...)     class func localizedStringWithFormat(_ format: NSString, _ args: CVarArgType...) -> Self     func stringByAppendingFormat(_ format: NSString, _ args: CVarArgType...) -> NSString } extension NSString {     @objc(_swiftInitWithString_NSString:) convenience init(string aString: NSString) } extension NSString : Reflectable {     func getMirror() -> MirrorType } extension NSString {     func getCharacters(_ buffer: UnsafeMutablePointer<unichar>, range aRange: NSRange)     func substringFromIndex(_ from: Int) -> String     func substringToIndex(_ to: Int) -> String     func substringWithRange(_ range: NSRange) -> String     func compare(_ string: String) -> NSComparisonResult     func compare(_ string: String, options mask: NSStringCompareOptions) -> NSComparisonResult     func compare(_ string: String, options mask: NSStringCompareOptions, range compareRange: NSRange) -> NSComparisonResult     func compare(_ string: String, options mask: NSStringCompareOptions, range compareRange: NSRange, locale locale: AnyObject?) -> NSComparisonResult     func caseInsensitiveCompare(_ string: String) -> NSComparisonResult     func localizedCompare(_ string: String) -> NSComparisonResult     func localizedCaseInsensitiveCompare(_ string: String) -> NSComparisonResult     func localizedStandardCompare(_ string: String) -> NSComparisonResult     func isEqualToString(_ aString: String) -> Bool     func hasPrefix(_ aString: String) -> Bool     func hasSuffix(_ aString: String) -> Bool     func containsString(_ aString: String) -> Bool     func localizedCaseInsensitiveContainsString(_ aString: String) -> Bool     func rangeOfString(_ aString: String) -> NSRange     func rangeOfString(_ aString: String, options mask: NSStringCompareOptions) -> NSRange     func rangeOfString(_ aString: String, options mask: NSStringCompareOptions, range searchRange: NSRange) -> NSRange     func rangeOfString(_ aString: String, options mask: NSStringCompareOptions, range searchRange: NSRange, locale locale: NSLocale?) -> NSRange     func rangeOfCharacterFromSet(_ aSet: NSCharacterSet) -> NSRange     func rangeOfCharacterFromSet(_ aSet: NSCharacterSet, options mask: NSStringCompareOptions) -> NSRange     func rangeOfCharacterFromSet(_ aSet: NSCharacterSet, options mask: NSStringCompareOptions, range searchRange: NSRange) -> NSRange     func rangeOfComposedCharacterSequenceAtIndex(_ index: Int) -> NSRange     func rangeOfComposedCharacterSequencesForRange(_ range: NSRange) -> NSRange     func stringByAppendingString(_ aString: String) -> String     var doubleValue: Double { get }     var floatValue: Float { get }     var intValue: Int32 { get }     var integerValue: Int { get }     var longLongValue: Int64 { get }     var boolValue: Bool { get }     func componentsSeparatedByString(_ separator: String) -> [AnyObject]     func componentsSeparatedByCharactersInSet(_ separator: NSCharacterSet) -> [AnyObject]     func commonPrefixWithString(_ aString: String, options mask: NSStringCompareOptions) -> String     var uppercaseString: String { get }     var lowercaseString: String { get }     var capitalizedString: String { get }     func uppercaseStringWithLocale(_ locale: NSLocale?) -> String     func lowercaseStringWithLocale(_ locale: NSLocale?) -> String     func capitalizedStringWithLocale(_ locale: NSLocale?) -> String     func stringByTrimmingCharactersInSet(_ set: NSCharacterSet) -> String     func stringByPaddingToLength(_ newLength: Int, withString padString: String, startingAtIndex padIndex: Int) -> String     func getLineStart(_ startPtr: UnsafeMutablePointer<Int>, end lineEndPtr: UnsafeMutablePointer<Int>, contentsEnd contentsEndPtr: UnsafeMutablePointer<Int>, forRange range: NSRange)     func lineRangeForRange(_ range: NSRange) -> NSRange     func getParagraphStart(_ startPtr: UnsafeMutablePointer<Int>, end parEndPtr: UnsafeMutablePointer<Int>, contentsEnd contentsEndPtr: UnsafeMutablePointer<Int>, forRange range: NSRange)     func paragraphRangeForRange(_ range: NSRange) -> NSRange     func enumerateSubstringsInRange(_ range: NSRange, options opts: NSStringEnumerationOptions, usingBlock block: (String!, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateLinesUsingBlock(_ block: (String!, UnsafeMutablePointer<ObjCBool>) -> Void)     var description: String { get }     var hash: Int { get }     var fastestEncoding: UInt { get }     var smallestEncoding: UInt { get }     func dataUsingEncoding(_ encoding: UInt, allowLossyConversion lossy: Bool) -> NSData?     func dataUsingEncoding(_ encoding: UInt) -> NSData?     func canBeConvertedToEncoding(_ encoding: UInt) -> Bool     func cStringUsingEncoding(_ encoding: UInt) -> UnsafePointer<Int8>     func getCString(_ buffer: UnsafeMutablePointer<Int8>, maxLength maxBufferCount: Int, encoding encoding: UInt) -> Bool     func getBytes(_ buffer: UnsafeMutablePointer<Void>, maxLength maxBufferCount: Int, usedLength usedBufferCount: UnsafeMutablePointer<Int>, encoding encoding: UInt, options options: NSStringEncodingConversionOptions, range range: NSRange, remainingRange leftover: NSRangePointer) -> Bool     func maximumLengthOfBytesUsingEncoding(_ enc: UInt) -> Int     func lengthOfBytesUsingEncoding(_ enc: UInt) -> Int     var decomposedStringWithCanonicalMapping: String { get }     var precomposedStringWithCanonicalMapping: String { get }     var decomposedStringWithCompatibilityMapping: String { get }     var precomposedStringWithCompatibilityMapping: String { get }     func stringByFoldingWithOptions(_ options: NSStringCompareOptions, locale locale: NSLocale?) -> String     func stringByReplacingOccurrencesOfString(_ target: String, withString replacement: String, options options: NSStringCompareOptions, range searchRange: NSRange) -> String     func stringByReplacingOccurrencesOfString(_ target: String, withString replacement: String) -> String     func stringByReplacingCharactersInRange(_ range: NSRange, withString replacement: String) -> String     var UTF8String: UnsafePointer<Int8> { get }     class func defaultCStringEncoding() -> UInt     class func availableStringEncodings() -> UnsafePointer<UInt>     class func localizedNameOfStringEncoding(_ encoding: UInt) -> String     convenience init(charactersNoCopy characters: UnsafeMutablePointer<unichar>, length length: Int, freeWhenDone freeBuffer: Bool)     convenience init(characters characters: UnsafePointer<unichar>, length length: Int)     convenience init?(UTF8String nullTerminatedCString: UnsafePointer<Int8>)     convenience init(string aString: String)     convenience init(format format: String, arguments argList: CVaListPointer)     convenience init(format format: String, locale locale: AnyObject?, arguments argList: CVaListPointer)     convenience init?(data data: NSData, encoding encoding: UInt)     convenience init?(bytes bytes: UnsafePointer<Void>, length len: Int, encoding encoding: UInt)     convenience init?(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length len: Int, encoding encoding: UInt, freeWhenDone freeBuffer: Bool)     class func string() -> Self!     class func stringWithString(_ string: String) -> Self     class func stringWithCharacters(_ characters: UnsafePointer<unichar>, length length: Int) -> Self     class func stringWithUTF8String(_ nullTerminatedCString: UnsafePointer<Int8>) -> Self     convenience init?(CString nullTerminatedCString: UnsafePointer<Int8>, encoding encoding: UInt)     class func stringWithCString(_ cString: UnsafePointer<Int8>, encoding enc: UInt) -> Self     convenience init?(contentsOfURL url: NSURL, encoding enc: UInt, error error: NSErrorPointer)     convenience init?(contentsOfFile path: String, encoding enc: UInt, error error: NSErrorPointer)     class func stringWithContentsOfURL(_ url: NSURL, encoding enc: UInt, error error: NSErrorPointer) -> Self?     class func stringWithContentsOfFile(_ path: String, encoding enc: UInt, error error: NSErrorPointer) -> Self?     convenience init?(contentsOfURL url: NSURL, usedEncoding enc: UnsafeMutablePointer<UInt>, error error: NSErrorPointer)     convenience init?(contentsOfFile path: String, usedEncoding enc: UnsafeMutablePointer<UInt>, error error: NSErrorPointer)     class func stringWithContentsOfURL(_ url: NSURL, usedEncoding enc: UnsafeMutablePointer<UInt>, error error: NSErrorPointer) -> Self?     class func stringWithContentsOfFile(_ path: String, usedEncoding enc: UnsafeMutablePointer<UInt>, error error: NSErrorPointer) -> Self?     func writeToURL(_ url: NSURL, atomically useAuxiliaryFile: Bool, encoding enc: UInt, error error: NSErrorPointer) -> Bool     func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool, encoding enc: UInt, error error: NSErrorPointer) -> Bool } extension NSString {     class func stringEncodingForData(_ data: NSData, encodingOptions opts: [NSObject : AnyObject]?, convertedString string: AutoreleasingUnsafeMutablePointer<NSString?>, usedLossyConversion usedLossyConversion: UnsafeMutablePointer<ObjCBool>) -> UInt } extension NSString {     func propertyList() -> AnyObject     func propertyListFromStringsFileFormat() -> [NSObject : AnyObject]? } extension NSString {     func cString() -> UnsafePointer<Int8>     func lossyCString() -> UnsafePointer<Int8>     func cStringLength() -> Int     func getCString(_ bytes: UnsafeMutablePointer<Int8>)     func getCString(_ bytes: UnsafeMutablePointer<Int8>, maxLength maxLength: Int)     func getCString(_ bytes: UnsafeMutablePointer<Int8>, maxLength maxLength: Int, range aRange: NSRange, remainingRange leftoverRange: NSRangePointer)     func writeToFile(_ path: String!, atomically useAuxiliaryFile: Bool) -> Bool     func writeToURL(_ url: NSURL!, atomically atomically: Bool) -> Bool     convenience init!(contentsOfFile path: String!)     convenience init!(contentsOfURL url: NSURL!)     class func stringWithContentsOfFile(_ path: String!) -> AnyObject!     class func stringWithContentsOfURL(_ url: NSURL!) -> AnyObject!     convenience init!(CStringNoCopy bytes: UnsafeMutablePointer<Int8>, length length: Int, freeWhenDone freeBuffer: Bool)     convenience init!(CString bytes: UnsafePointer<Int8>, length length: Int)     convenience init!(CString bytes: UnsafePointer<Int8>)     class func stringWithCString(_ bytes: UnsafePointer<Int8>, length length: Int) -> AnyObject!     class func stringWithCString(_ bytes: UnsafePointer<Int8>) -> AnyObject!     func getCharacters(_ buffer: UnsafeMutablePointer<unichar>) } extension NSString {     func stringByAddingPercentEncodingWithAllowedCharacters(_ allowedCharacters: NSCharacterSet) -> String?     var stringByRemovingPercentEncoding: String? { get }     func stringByAddingPercentEscapesUsingEncoding(_ enc: UInt) -> String?     func stringByReplacingPercentEscapesUsingEncoding(_ enc: UInt) -> String? } extension NSString : Reflectable {     func getMirror() -> MirrorType } extension NSString {     @objc(_swiftInitWithString_NSString:) convenience init(string aString: NSString) } extension NSString {     convenience init(format format: NSString, _ args: CVarArgType...)     convenience init(format format: NSString, locale locale: NSLocale?, _ args: CVarArgType...)     class func localizedStringWithFormat(_ format: NSString, _ args: CVarArgType...) -> Self     func stringByAppendingFormat(_ format: NSString, _ args: CVarArgType...) -> NSString } extension NSString : _CocoaStringType { } extension NSString : StringLiteralConvertible {     required convenience init(unicodeScalarLiteral value: StaticString)     required convenience init(extendedGraphemeClusterLiteral value: StaticString)     required convenience init(stringLiteral value: StaticString) } extension NSString {     func sizeWithAttributes(_ attrs: [NSObject : AnyObject]?) -> CGSize     func drawAtPoint(_ point: CGPoint, withAttributes attrs: [NSObject : AnyObject]?)     func drawInRect(_ rect: CGRect, withAttributes attrs: [NSObject : AnyObject]?) } extension NSString {     func drawWithRect(_ rect: CGRect, options options: NSStringDrawingOptions, attributes attributes: [NSObject : AnyObject]!, context context: NSStringDrawingContext!)     func boundingRectWithSize(_ size: CGSize, options options: NSStringDrawingOptions, attributes attributes: [NSObject : AnyObject]!, context context: NSStringDrawingContext!) -> CGRect } extension NSString {     func sizeWithFont(_ font: UIFont!) -> CGSize     func sizeWithFont(_ font: UIFont!, forWidth width: CGFloat, lineBreakMode lineBreakMode: NSLineBreakMode) -> CGSize     func drawAtPoint(_ point: CGPoint, withFont font: UIFont!) -> CGSize     func drawAtPoint(_ point: CGPoint, forWidth width: CGFloat, withFont font: UIFont!, lineBreakMode lineBreakMode: NSLineBreakMode) -> CGSize     func sizeWithFont(_ font: UIFont!, constrainedToSize size: CGSize) -> CGSize     func sizeWithFont(_ font: UIFont!, constrainedToSize size: CGSize, lineBreakMode lineBreakMode: NSLineBreakMode) -> CGSize     func drawInRect(_ rect: CGRect, withFont font: UIFont!) -> CGSize     func drawInRect(_ rect: CGRect, withFont font: UIFont!, lineBreakMode lineBreakMode: NSLineBreakMode) -> CGSize     func drawInRect(_ rect: CGRect, withFont font: UIFont!, lineBreakMode lineBreakMode: NSLineBreakMode, alignment alignment: NSTextAlignment) -> CGSize     func sizeWithFont(_ font: UIFont!, minFontSize minFontSize: CGFloat, actualFontSize actualFontSize: UnsafeMutablePointer<CGFloat>, forWidth width: CGFloat, lineBreakMode lineBreakMode: NSLineBreakMode) -> CGSize     func drawAtPoint(_ point: CGPoint, forWidth width: CGFloat, withFont font: UIFont!, fontSize fontSize: CGFloat, lineBreakMode lineBreakMode: NSLineBreakMode, baselineAdjustment baselineAdjustment: UIBaselineAdjustment) -> CGSize     func drawAtPoint(_ point: CGPoint, forWidth width: CGFloat, withFont font: UIFont!, minFontSize minFontSize: CGFloat, actualFontSize actualFontSize: UnsafeMutablePointer<CGFloat>, lineBreakMode lineBreakMode: NSLineBreakMode, baselineAdjustment baselineAdjustment: UIBaselineAdjustment) -> CGSize } ``` | AnyObject, CKRecordValue, NSCoding, NSCopying, NSMutableCopying, NSObjectProtocol, NSSecureCoding, Reflectable, StringLiteralConvertible |
| To | ``` class NSString : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     var length: Int { get }     func characterAtIndex(_ index: Int) -> unichar     init()     init?(coder aDecoder: NSCoder) } extension NSString : CKRecordValue { } extension NSString : CNKeyDescriptor { } extension NSString {     func variantFittingPresentationWidth(_ width: Int) -> String } extension NSString {     func linguisticTagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, orthography orthography: NSOrthography?, tokenRanges tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [String]     func enumerateLinguisticTagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, orthography orthography: NSOrthography?, usingBlock block: (String, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) } extension NSString {     class func pathWithComponents(_ components: [String]) -> String     var pathComponents: [String] { get }     var absolutePath: Bool { get }     var lastPathComponent: String { get }     var stringByDeletingLastPathComponent: String { get }     func stringByAppendingPathComponent(_ str: String) -> String     var pathExtension: String { get }     var stringByDeletingPathExtension: String { get }     func stringByAppendingPathExtension(_ str: String) -> String?     var stringByAbbreviatingWithTildeInPath: String { get }     var stringByExpandingTildeInPath: String { get }     var stringByStandardizingPath: String { get }     var stringByResolvingSymlinksInPath: String { get }     func stringsByAppendingPaths(_ paths: [String]) -> [String]     func completePathIntoString(_ outputName: AutoreleasingUnsafeMutablePointer<NSString?>, caseSensitive flag: Bool, matchesIntoArray outputArray: AutoreleasingUnsafeMutablePointer<NSArray?>, filterTypes filterTypes: [String]?) -> Int     var fileSystemRepresentation: UnsafePointer<Int8> { get }     func getFileSystemRepresentation(_ cname: UnsafeMutablePointer<Int8>, maxLength max: Int) -> Bool } extension NSString : StringLiteralConvertible, ExtendedGraphemeClusterLiteralConvertible, UnicodeScalarLiteralConvertible {     required convenience init(unicodeScalarLiteral value: StaticString)     required convenience init(extendedGraphemeClusterLiteral value: StaticString)     required convenience init(stringLiteral value: StaticString) } extension NSString : _CocoaStringType { } extension NSString {     convenience init(format format: NSString, _ args: CVarArgType...)     convenience init(format format: NSString, locale locale: NSLocale?, _ args: CVarArgType...)     @warn_unused_result     class func localizedStringWithFormat(_ format: NSString, _ args: CVarArgType...) -> Self     @warn_unused_result     func stringByAppendingFormat(_ format: NSString, _ args: CVarArgType...) -> NSString } extension NSString {     @objc(_swiftInitWithString_NSString:) convenience init(string aString: NSString) } extension NSString : _Reflectable { } extension NSString {     func substringFromIndex(_ from: Int) -> String     func substringToIndex(_ to: Int) -> String     func substringWithRange(_ range: NSRange) -> String     func getCharacters(_ buffer: UnsafeMutablePointer<unichar>, range range: NSRange)     func compare(_ string: String) -> NSComparisonResult     func compare(_ string: String, options mask: NSStringCompareOptions) -> NSComparisonResult     func compare(_ string: String, options mask: NSStringCompareOptions, range compareRange: NSRange) -> NSComparisonResult     func compare(_ string: String, options mask: NSStringCompareOptions, range compareRange: NSRange, locale locale: AnyObject?) -> NSComparisonResult     func caseInsensitiveCompare(_ string: String) -> NSComparisonResult     func localizedCompare(_ string: String) -> NSComparisonResult     func localizedCaseInsensitiveCompare(_ string: String) -> NSComparisonResult     func localizedStandardCompare(_ string: String) -> NSComparisonResult     func isEqualToString(_ aString: String) -> Bool     func hasPrefix(_ str: String) -> Bool     func hasSuffix(_ str: String) -> Bool     func commonPrefixWithString(_ str: String, options mask: NSStringCompareOptions) -> String     func containsString(_ str: String) -> Bool     func localizedCaseInsensitiveContainsString(_ str: String) -> Bool     func localizedStandardContainsString(_ str: String) -> Bool     func localizedStandardRangeOfString(_ str: String) -> NSRange     func rangeOfString(_ searchString: String) -> NSRange     func rangeOfString(_ searchString: String, options mask: NSStringCompareOptions) -> NSRange     func rangeOfString(_ searchString: String, options mask: NSStringCompareOptions, range searchRange: NSRange) -> NSRange     func rangeOfString(_ searchString: String, options mask: NSStringCompareOptions, range searchRange: NSRange, locale locale: NSLocale?) -> NSRange     func rangeOfCharacterFromSet(_ searchSet: NSCharacterSet) -> NSRange     func rangeOfCharacterFromSet(_ searchSet: NSCharacterSet, options mask: NSStringCompareOptions) -> NSRange     func rangeOfCharacterFromSet(_ searchSet: NSCharacterSet, options mask: NSStringCompareOptions, range searchRange: NSRange) -> NSRange     func rangeOfComposedCharacterSequenceAtIndex(_ index: Int) -> NSRange     func rangeOfComposedCharacterSequencesForRange(_ range: NSRange) -> NSRange     func stringByAppendingString(_ aString: String) -> String     var doubleValue: Double { get }     var floatValue: Float { get }     var intValue: Int32 { get }     var integerValue: Int { get }     var longLongValue: Int64 { get }     var boolValue: Bool { get }     var uppercaseString: String { get }     var lowercaseString: String { get }     var capitalizedString: String { get }     var localizedUppercaseString: String { get }     var localizedLowercaseString: String { get }     var localizedCapitalizedString: String { get }     func uppercaseStringWithLocale(_ locale: NSLocale?) -> String     func lowercaseStringWithLocale(_ locale: NSLocale?) -> String     func capitalizedStringWithLocale(_ locale: NSLocale?) -> String     func getLineStart(_ startPtr: UnsafeMutablePointer<Int>, end lineEndPtr: UnsafeMutablePointer<Int>, contentsEnd contentsEndPtr: UnsafeMutablePointer<Int>, forRange range: NSRange)     func lineRangeForRange(_ range: NSRange) -> NSRange     func getParagraphStart(_ startPtr: UnsafeMutablePointer<Int>, end parEndPtr: UnsafeMutablePointer<Int>, contentsEnd contentsEndPtr: UnsafeMutablePointer<Int>, forRange range: NSRange)     func paragraphRangeForRange(_ range: NSRange) -> NSRange     func enumerateSubstringsInRange(_ range: NSRange, options opts: NSStringEnumerationOptions, usingBlock block: (String?, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateLinesUsingBlock(_ block: (String, UnsafeMutablePointer<ObjCBool>) -> Void)     var UTF8String: UnsafePointer<Int8> { get }     var fastestEncoding: UInt { get }     var smallestEncoding: UInt { get }     func dataUsingEncoding(_ encoding: UInt, allowLossyConversion lossy: Bool) -> NSData?     func dataUsingEncoding(_ encoding: UInt) -> NSData?     func canBeConvertedToEncoding(_ encoding: UInt) -> Bool     func cStringUsingEncoding(_ encoding: UInt) -> UnsafePointer<Int8>     func getCString(_ buffer: UnsafeMutablePointer<Int8>, maxLength maxBufferCount: Int, encoding encoding: UInt) -> Bool     func getBytes(_ buffer: UnsafeMutablePointer<Void>, maxLength maxBufferCount: Int, usedLength usedBufferCount: UnsafeMutablePointer<Int>, encoding encoding: UInt, options options: NSStringEncodingConversionOptions, range range: NSRange, remainingRange leftover: NSRangePointer) -> Bool     func maximumLengthOfBytesUsingEncoding(_ enc: UInt) -> Int     func lengthOfBytesUsingEncoding(_ enc: UInt) -> Int     class func availableStringEncodings() -> UnsafePointer<UInt>     class func localizedNameOfStringEncoding(_ encoding: UInt) -> String     class func defaultCStringEncoding() -> UInt     var decomposedStringWithCanonicalMapping: String { get }     var precomposedStringWithCanonicalMapping: String { get }     var decomposedStringWithCompatibilityMapping: String { get }     var precomposedStringWithCompatibilityMapping: String { get }     func componentsSeparatedByString(_ separator: String) -> [String]     func componentsSeparatedByCharactersInSet(_ separator: NSCharacterSet) -> [String]     func stringByTrimmingCharactersInSet(_ set: NSCharacterSet) -> String     func stringByPaddingToLength(_ newLength: Int, withString padString: String, startingAtIndex padIndex: Int) -> String     func stringByFoldingWithOptions(_ options: NSStringCompareOptions, locale locale: NSLocale?) -> String     func stringByReplacingOccurrencesOfString(_ target: String, withString replacement: String, options options: NSStringCompareOptions, range searchRange: NSRange) -> String     func stringByReplacingOccurrencesOfString(_ target: String, withString replacement: String) -> String     func stringByReplacingCharactersInRange(_ range: NSRange, withString replacement: String) -> String     func stringByApplyingTransform(_ transform: String, reverse reverse: Bool) -> String?     func writeToURL(_ url: NSURL, atomically useAuxiliaryFile: Bool, encoding enc: UInt) throws     func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool, encoding enc: UInt) throws     var description: String { get }     var hash: Int { get }     convenience init(charactersNoCopy characters: UnsafeMutablePointer<unichar>, length length: Int, freeWhenDone freeBuffer: Bool)     convenience init(characters characters: UnsafePointer<unichar>, length length: Int)     convenience init?(UTF8String nullTerminatedCString: UnsafePointer<Int8>)     convenience init(string aString: String)     convenience init(format format: String, arguments argList: CVaListPointer)     convenience init(format format: String, locale locale: AnyObject?, arguments argList: CVaListPointer)     convenience init?(data data: NSData, encoding encoding: UInt)     convenience init?(bytes bytes: UnsafePointer<Void>, length len: Int, encoding encoding: UInt)     convenience init?(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length len: Int, encoding encoding: UInt, freeWhenDone freeBuffer: Bool)     class func string() -> Self     class func stringWithString(_ string: String) -> Self     class func stringWithCharacters(_ characters: UnsafePointer<unichar>, length length: Int) -> Self     class func stringWithUTF8String(_ nullTerminatedCString: UnsafePointer<Int8>) -> Self?     convenience init?(CString nullTerminatedCString: UnsafePointer<Int8>, encoding encoding: UInt)     class func stringWithCString(_ cString: UnsafePointer<Int8>, encoding enc: UInt) -> Self?     convenience init(contentsOfURL url: NSURL, encoding enc: UInt) throws     convenience init(contentsOfFile path: String, encoding enc: UInt) throws     class func stringWithContentsOfURL(_ url: NSURL, encoding enc: UInt) throws -> Self     class func stringWithContentsOfFile(_ path: String, encoding enc: UInt) throws -> Self     convenience init(contentsOfURL url: NSURL, usedEncoding enc: UnsafeMutablePointer<UInt>) throws     convenience init(contentsOfFile path: String, usedEncoding enc: UnsafeMutablePointer<UInt>) throws     class func stringWithContentsOfURL(_ url: NSURL, usedEncoding enc: UnsafeMutablePointer<UInt>) throws -> Self     class func stringWithContentsOfFile(_ path: String, usedEncoding enc: UnsafeMutablePointer<UInt>) throws -> Self } extension NSString {     class func stringEncodingForData(_ data: NSData, encodingOptions opts: [String : AnyObject]?, convertedString string: AutoreleasingUnsafeMutablePointer<NSString?>, usedLossyConversion usedLossyConversion: UnsafeMutablePointer<ObjCBool>) -> UInt } extension NSString {     func propertyList() -> AnyObject     func propertyListFromStringsFileFormat() -> [NSObject : AnyObject]? } extension NSString {     func cString() -> UnsafePointer<Int8>     func lossyCString() -> UnsafePointer<Int8>     func cStringLength() -> Int     func getCString(_ bytes: UnsafeMutablePointer<Int8>)     func getCString(_ bytes: UnsafeMutablePointer<Int8>, maxLength maxLength: Int)     func getCString(_ bytes: UnsafeMutablePointer<Int8>, maxLength maxLength: Int, range aRange: NSRange, remainingRange leftoverRange: NSRangePointer)     func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool) -> Bool     func writeToURL(_ url: NSURL, atomically atomically: Bool) -> Bool     convenience init?(contentsOfFile path: String)     convenience init?(contentsOfURL url: NSURL)     class func stringWithContentsOfFile(_ path: String) -> AnyObject?     class func stringWithContentsOfURL(_ url: NSURL) -> AnyObject?     convenience init?(CStringNoCopy bytes: UnsafeMutablePointer<Int8>, length length: Int, freeWhenDone freeBuffer: Bool)     convenience init?(CString bytes: UnsafePointer<Int8>, length length: Int)     convenience init?(CString bytes: UnsafePointer<Int8>)     class func stringWithCString(_ bytes: UnsafePointer<Int8>, length length: Int) -> AnyObject?     class func stringWithCString(_ bytes: UnsafePointer<Int8>) -> AnyObject?     func getCharacters(_ buffer: UnsafeMutablePointer<unichar>) } extension NSString {     func stringByAddingPercentEncodingWithAllowedCharacters(_ allowedCharacters: NSCharacterSet) -> String?     var stringByRemovingPercentEncoding: String? { get }     func stringByAddingPercentEscapesUsingEncoding(_ enc: UInt) -> String?     func stringByReplacingPercentEscapesUsingEncoding(_ enc: UInt) -> String? } extension NSString : _Reflectable { } extension NSString {     @objc(_swiftInitWithString_NSString:) convenience init(string aString: NSString) } extension NSString {     convenience init(format format: NSString, _ args: CVarArgType...)     convenience init(format format: NSString, locale locale: NSLocale?, _ args: CVarArgType...)     @warn_unused_result     class func localizedStringWithFormat(_ format: NSString, _ args: CVarArgType...) -> Self     @warn_unused_result     func stringByAppendingFormat(_ format: NSString, _ args: CVarArgType...) -> NSString } extension NSString : _CocoaStringType { } extension NSString : StringLiteralConvertible, ExtendedGraphemeClusterLiteralConvertible, UnicodeScalarLiteralConvertible {     required convenience init(unicodeScalarLiteral value: StaticString)     required convenience init(extendedGraphemeClusterLiteral value: StaticString)     required convenience init(stringLiteral value: StaticString) } extension NSString {     func sizeWithAttributes(_ attrs: [String : AnyObject]?) -> CGSize     func drawAtPoint(_ point: CGPoint, withAttributes attrs: [String : AnyObject]?)     func drawInRect(_ rect: CGRect, withAttributes attrs: [String : AnyObject]?) } extension NSString {     func drawWithRect(_ rect: CGRect, options options: NSStringDrawingOptions, attributes attributes: [String : AnyObject]?, context context: NSStringDrawingContext?)     func boundingRectWithSize(_ size: CGSize, options options: NSStringDrawingOptions, attributes attributes: [String : AnyObject]?, context context: NSStringDrawingContext?) -> CGRect } extension NSString {     func sizeWithFont(_ font: UIFont!) -> CGSize     func sizeWithFont(_ font: UIFont!, forWidth width: CGFloat, lineBreakMode lineBreakMode: NSLineBreakMode) -> CGSize     func drawAtPoint(_ point: CGPoint, withFont font: UIFont!) -> CGSize     func drawAtPoint(_ point: CGPoint, forWidth width: CGFloat, withFont font: UIFont!, lineBreakMode lineBreakMode: NSLineBreakMode) -> CGSize     func sizeWithFont(_ font: UIFont!, constrainedToSize size: CGSize) -> CGSize     func sizeWithFont(_ font: UIFont!, constrainedToSize size: CGSize, lineBreakMode lineBreakMode: NSLineBreakMode) -> CGSize     func drawInRect(_ rect: CGRect, withFont font: UIFont!) -> CGSize     func drawInRect(_ rect: CGRect, withFont font: UIFont!, lineBreakMode lineBreakMode: NSLineBreakMode) -> CGSize     func drawInRect(_ rect: CGRect, withFont font: UIFont!, lineBreakMode lineBreakMode: NSLineBreakMode, alignment alignment: NSTextAlignment) -> CGSize     func sizeWithFont(_ font: UIFont!, minFontSize minFontSize: CGFloat, actualFontSize actualFontSize: UnsafeMutablePointer<CGFloat>, forWidth width: CGFloat, lineBreakMode lineBreakMode: NSLineBreakMode) -> CGSize     func drawAtPoint(_ point: CGPoint, forWidth width: CGFloat, withFont font: UIFont!, fontSize fontSize: CGFloat, lineBreakMode lineBreakMode: NSLineBreakMode, baselineAdjustment baselineAdjustment: UIBaselineAdjustment) -> CGSize     func drawAtPoint(_ point: CGPoint, forWidth width: CGFloat, withFont font: UIFont!, minFontSize minFontSize: CGFloat, actualFontSize actualFontSize: UnsafeMutablePointer<CGFloat>, lineBreakMode lineBreakMode: NSLineBreakMode, baselineAdjustment baselineAdjustment: UIBaselineAdjustment) -> CGSize } ``` | AnyObject, CKRecordValue, CNKeyDescriptor, ExtendedGraphemeClusterLiteralConvertible, NSCoding, NSCopying, NSMutableCopying, NSObjectProtocol, NSSecureCoding, StringLiteralConvertible, UnicodeScalarLiteralConvertible |

Modified [NSString.completePathIntoString(_: AutoreleasingUnsafeMutablePointer<NSString?>, caseSensitive: Bool, matchesIntoArray: AutoreleasingUnsafeMutablePointer<NSArray?>, filterTypes: [String]?) -> Int](https://developer.apple.com/documentation/foundation/nsstring/1411841-completepathintostring)

|  | Declaration |
| --- | --- |
| From | ``` func completePathIntoString(_ outputName: AutoreleasingUnsafeMutablePointer<NSString?>, caseSensitive flag: Bool, matchesIntoArray outputArray: AutoreleasingUnsafeMutablePointer<NSArray?>, filterTypes filterTypes: [AnyObject]?) -> Int ``` |
| To | ``` func completePathIntoString(_ outputName: AutoreleasingUnsafeMutablePointer<NSString?>, caseSensitive flag: Bool, matchesIntoArray outputArray: AutoreleasingUnsafeMutablePointer<NSArray?>, filterTypes filterTypes: [String]?) -> Int ``` |

Modified [NSString.componentsSeparatedByCharactersInSet(_: NSCharacterSet) -> [String]](https://developer.apple.com/documentation/foundation/nsstring/1410120-components)

|  | Declaration |
| --- | --- |
| From | ``` func componentsSeparatedByCharactersInSet(_ separator: NSCharacterSet) -> [AnyObject] ``` |
| To | ``` func componentsSeparatedByCharactersInSet(_ separator: NSCharacterSet) -> [String] ``` |

Modified [NSString.componentsSeparatedByString(_: String) -> [String]](https://developer.apple.com/documentation/foundation/nsstring/1413214-components)

|  | Declaration |
| --- | --- |
| From | ``` func componentsSeparatedByString(_ separator: String) -> [AnyObject] ``` |
| To | ``` func componentsSeparatedByString(_ separator: String) -> [String] ``` |

Modified [NSString.enumerateLinesUsingBlock(_: (String, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/foundation/nsstring/1408459-enumeratelines)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateLinesUsingBlock(_ block: (String!, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateLinesUsingBlock(_ block: (String, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [NSString.enumerateLinguisticTagsInRange(_: NSRange, scheme: String, options: NSLinguisticTaggerOptions, orthography: NSOrthography?, usingBlock: (String, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/foundation/nsstring/1412161-enumeratelinguistictags)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateLinguisticTagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, orthography orthography: NSOrthography?, usingBlock block: (String!, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateLinguisticTagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, orthography orthography: NSOrthography?, usingBlock block: (String, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [NSString.enumerateSubstringsInRange(_: NSRange, options: NSStringEnumerationOptions, usingBlock: (String?, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/foundation/nsstring/1416774-enumeratesubstringsinrange)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateSubstringsInRange(_ range: NSRange, options opts: NSStringEnumerationOptions, usingBlock block: (String!, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateSubstringsInRange(_ range: NSRange, options opts: NSStringEnumerationOptions, usingBlock block: (String?, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [NSString.init(coder: NSCoder)](https://developer.apple.com/documentation/foundation/nsstring/1407488-initwithcoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified [NSString.init(contentsOfFile: String, encoding: UInt) throws](https://developer.apple.com/documentation/foundation/nsstring/1412610-initwithcontentsoffile)

|  | Declaration |
| --- | --- |
| From | ``` convenience init?(contentsOfFile path: String, encoding enc: UInt, error error: NSErrorPointer) ``` |
| To | ``` convenience init(contentsOfFile path: String, encoding enc: UInt) throws ``` |

Modified [NSString.init(contentsOfFile: String, usedEncoding: UnsafeMutablePointer<UInt>) throws](https://developer.apple.com/documentation/foundation/nsstring/1418227-initwithcontentsoffile)

|  | Declaration |
| --- | --- |
| From | ``` convenience init?(contentsOfFile path: String, usedEncoding enc: UnsafeMutablePointer<UInt>, error error: NSErrorPointer) ``` |
| To | ``` convenience init(contentsOfFile path: String, usedEncoding enc: UnsafeMutablePointer<UInt>) throws ``` |

Modified [NSString.init(contentsOfURL: NSURL, encoding: UInt) throws](https://developer.apple.com/documentation/foundation/nsstring/1414463-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init?(contentsOfURL url: NSURL, encoding enc: UInt, error error: NSErrorPointer) ``` |
| To | ``` convenience init(contentsOfURL url: NSURL, encoding enc: UInt) throws ``` |

Modified [NSString.init(contentsOfURL: NSURL, usedEncoding: UnsafeMutablePointer<UInt>) throws](https://developer.apple.com/documentation/foundation/nsstring/1414472-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` convenience init?(contentsOfURL url: NSURL, usedEncoding enc: UnsafeMutablePointer<UInt>, error error: NSErrorPointer) ``` |
| To | ``` convenience init(contentsOfURL url: NSURL, usedEncoding enc: UnsafeMutablePointer<UInt>) throws ``` |

Modified [NSString.linguisticTagsInRange(_: NSRange, scheme: String, options: NSLinguisticTaggerOptions, orthography: NSOrthography?, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [String]](https://developer.apple.com/documentation/foundation/nsstring/1416530-linguistictagsinrange)

|  | Declaration |
| --- | --- |
| From | ``` func linguisticTagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, orthography orthography: NSOrthography?, tokenRanges tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [AnyObject] ``` |
| To | ``` func linguisticTagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, orthography orthography: NSOrthography?, tokenRanges tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [String] ``` |

Modified NSString.localizedStringWithFormat(_: NSString, _: CVarArgType) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func localizedStringWithFormat(_ format: NSString, _ args: CVarArgType...) -> Self ``` | iOS 8.3 |
| To | ``` @warn_unused_result     class func localizedStringWithFormat(_ format: NSString, _ args: CVarArgType...) -> Self ``` | iOS 9.0 |

Modified [NSString.pathComponents](https://developer.apple.com/documentation/foundation/nsstring/1414489-pathcomponents)

|  | Declaration |
| --- | --- |
| From | ``` var pathComponents: [AnyObject] { get } ``` |
| To | ``` var pathComponents: [String] { get } ``` |

Modified [NSString.pathWithComponents(_: [String]) -> String [class]](https://developer.apple.com/documentation/foundation/nsstring/1417198-path)

|  | Declaration |
| --- | --- |
| From | ``` class func pathWithComponents(_ components: [AnyObject]) -> String ``` |
| To | ``` class func pathWithComponents(_ components: [String]) -> String ``` |

Modified [NSString.stringByAddingPercentEscapesUsingEncoding(_: UInt) -> String?](https://developer.apple.com/documentation/foundation/nsstring/1415058-addingpercentescapes)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified NSString.stringByAppendingFormat(_: NSString, _: CVarArgType) -> NSString

|  | Declaration |
| --- | --- |
| From | ``` func stringByAppendingFormat(_ format: NSString, _ args: CVarArgType...) -> NSString ``` |
| To | ``` @warn_unused_result     func stringByAppendingFormat(_ format: NSString, _ args: CVarArgType...) -> NSString ``` |

Modified [NSString.stringByReplacingPercentEscapesUsingEncoding(_: UInt) -> String?](https://developer.apple.com/documentation/foundation/nsstring/1407783-stringbyreplacingpercentescapesu)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [NSString.stringEncodingForData(_: NSData, encodingOptions: [String : AnyObject]?, convertedString: AutoreleasingUnsafeMutablePointer<NSString?>, usedLossyConversion: UnsafeMutablePointer<ObjCBool>) -> UInt [class]](https://developer.apple.com/documentation/foundation/nsstring/1413576-stringencoding)

|  | Declaration |
| --- | --- |
| From | ``` class func stringEncodingForData(_ data: NSData, encodingOptions opts: [NSObject : AnyObject]?, convertedString string: AutoreleasingUnsafeMutablePointer<NSString?>, usedLossyConversion usedLossyConversion: UnsafeMutablePointer<ObjCBool>) -> UInt ``` |
| To | ``` class func stringEncodingForData(_ data: NSData, encodingOptions opts: [String : AnyObject]?, convertedString string: AutoreleasingUnsafeMutablePointer<NSString?>, usedLossyConversion usedLossyConversion: UnsafeMutablePointer<ObjCBool>) -> UInt ``` |

Modified [NSString.stringsByAppendingPaths(_: [String]) -> [String]](https://developer.apple.com/documentation/foundation/nsstring/1415100-stringsbyappendingpaths)

|  | Declaration |
| --- | --- |
| From | ``` func stringsByAppendingPaths(_ paths: [AnyObject]) -> [AnyObject] ``` |
| To | ``` func stringsByAppendingPaths(_ paths: [String]) -> [String] ``` |

Modified [NSString.writeToFile(_: String, atomically: Bool, encoding: UInt) throws](https://developer.apple.com/documentation/foundation/nsstring/1407654-write)

|  | Declaration |
| --- | --- |
| From | ``` func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool, encoding enc: UInt, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool, encoding enc: UInt) throws ``` |

Modified [NSString.writeToURL(_: NSURL, atomically: Bool, encoding: UInt) throws](https://developer.apple.com/documentation/foundation/nsstring/1417341-writetourl)

|  | Declaration |
| --- | --- |
| From | ``` func writeToURL(_ url: NSURL, atomically useAuxiliaryFile: Bool, encoding enc: UInt, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func writeToURL(_ url: NSURL, atomically useAuxiliaryFile: Bool, encoding enc: UInt) throws ``` |

Modified [NSStringCompareOptions [struct]](https://developer.apple.com/documentation/foundation/nsstring/compareoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSStringCompareOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var CaseInsensitiveSearch: NSStringCompareOptions { get }     static var LiteralSearch: NSStringCompareOptions { get }     static var BackwardsSearch: NSStringCompareOptions { get }     static var AnchoredSearch: NSStringCompareOptions { get }     static var NumericSearch: NSStringCompareOptions { get }     static var DiacriticInsensitiveSearch: NSStringCompareOptions { get }     static var WidthInsensitiveSearch: NSStringCompareOptions { get }     static var ForcedOrderingSearch: NSStringCompareOptions { get }     static var RegularExpressionSearch: NSStringCompareOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSStringCompareOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var CaseInsensitiveSearch: NSStringCompareOptions { get }     static var LiteralSearch: NSStringCompareOptions { get }     static var BackwardsSearch: NSStringCompareOptions { get }     static var AnchoredSearch: NSStringCompareOptions { get }     static var NumericSearch: NSStringCompareOptions { get }     static var DiacriticInsensitiveSearch: NSStringCompareOptions { get }     static var WidthInsensitiveSearch: NSStringCompareOptions { get }     static var ForcedOrderingSearch: NSStringCompareOptions { get }     static var RegularExpressionSearch: NSStringCompareOptions { get } } ``` | OptionSetType |

Modified [NSStringEncodingConversionOptions [struct]](https://developer.apple.com/documentation/foundation/nsstring/encodingconversionoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSStringEncodingConversionOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var AllowLossy: NSStringEncodingConversionOptions { get }     static var ExternalRepresentation: NSStringEncodingConversionOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSStringEncodingConversionOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var AllowLossy: NSStringEncodingConversionOptions { get }     static var ExternalRepresentation: NSStringEncodingConversionOptions { get } } ``` | OptionSetType |

Modified [NSStringEnumerationOptions [struct]](https://developer.apple.com/documentation/foundation/nsstring/enumerationoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSStringEnumerationOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var ByLines: NSStringEnumerationOptions { get }     static var ByParagraphs: NSStringEnumerationOptions { get }     static var ByComposedCharacterSequences: NSStringEnumerationOptions { get }     static var ByWords: NSStringEnumerationOptions { get }     static var BySentences: NSStringEnumerationOptions { get }     static var Reverse: NSStringEnumerationOptions { get }     static var SubstringNotRequired: NSStringEnumerationOptions { get }     static var Localized: NSStringEnumerationOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSStringEnumerationOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var ByLines: NSStringEnumerationOptions { get }     static var ByParagraphs: NSStringEnumerationOptions { get }     static var ByComposedCharacterSequences: NSStringEnumerationOptions { get }     static var ByWords: NSStringEnumerationOptions { get }     static var BySentences: NSStringEnumerationOptions { get }     static var Reverse: NSStringEnumerationOptions { get }     static var SubstringNotRequired: NSStringEnumerationOptions { get }     static var Localized: NSStringEnumerationOptions { get } } ``` | OptionSetType |

Modified [NSTextCheckingResult](https://developer.apple.com/documentation/foundation/nstextcheckingresult)

|  | Declaration |
| --- | --- |
| From | ``` class NSTextCheckingResult : NSObject, NSCopying, NSCoding {     var resultType: NSTextCheckingType { get }     var range: NSRange { get } } extension NSTextCheckingResult {     @NSCopying var orthography: NSOrthography? { get }     var grammarDetails: [AnyObject]? { get }     @NSCopying var date: NSDate? { get }     @NSCopying var timeZone: NSTimeZone? { get }     var duration: NSTimeInterval { get }     var components: [NSObject : AnyObject]? { get }     @NSCopying var URL: NSURL? { get }     var replacementString: String? { get }     var alternativeStrings: [AnyObject]? { get }     @NSCopying var regularExpression: NSRegularExpression? { get }     var phoneNumber: String? { get }     var addressComponents: [NSObject : AnyObject]? { get }     var numberOfRanges: Int { get }     func rangeAtIndex(_ idx: Int) -> NSRange     func resultByAdjustingRangesWithOffset(_ offset: Int) -> NSTextCheckingResult } extension NSTextCheckingResult {     class func orthographyCheckingResultWithRange(_ range: NSRange, orthography orthography: NSOrthography) -> NSTextCheckingResult     class func spellCheckingResultWithRange(_ range: NSRange) -> NSTextCheckingResult     class func grammarCheckingResultWithRange(_ range: NSRange, details details: [AnyObject]) -> NSTextCheckingResult     class func dateCheckingResultWithRange(_ range: NSRange, date date: NSDate) -> NSTextCheckingResult     class func dateCheckingResultWithRange(_ range: NSRange, date date: NSDate, timeZone timeZone: NSTimeZone, duration duration: NSTimeInterval) -> NSTextCheckingResult     class func addressCheckingResultWithRange(_ range: NSRange, components components: [NSObject : AnyObject]) -> NSTextCheckingResult     class func linkCheckingResultWithRange(_ range: NSRange, URL url: NSURL) -> NSTextCheckingResult     class func quoteCheckingResultWithRange(_ range: NSRange, replacementString replacementString: String) -> NSTextCheckingResult     class func dashCheckingResultWithRange(_ range: NSRange, replacementString replacementString: String) -> NSTextCheckingResult     class func replacementCheckingResultWithRange(_ range: NSRange, replacementString replacementString: String) -> NSTextCheckingResult     class func correctionCheckingResultWithRange(_ range: NSRange, replacementString replacementString: String) -> NSTextCheckingResult     class func correctionCheckingResultWithRange(_ range: NSRange, replacementString replacementString: String, alternativeStrings alternativeStrings: [AnyObject]) -> NSTextCheckingResult     class func regularExpressionCheckingResultWithRanges(_ ranges: NSRangePointer, count count: Int, regularExpression regularExpression: NSRegularExpression) -> NSTextCheckingResult     class func phoneNumberCheckingResultWithRange(_ range: NSRange, phoneNumber phoneNumber: String) -> NSTextCheckingResult     class func transitInformationCheckingResultWithRange(_ range: NSRange, components components: [NSObject : AnyObject]) -> NSTextCheckingResult } ``` |
| To | ``` class NSTextCheckingResult : NSObject, NSCopying, NSCoding {     var resultType: NSTextCheckingType { get }     var range: NSRange { get } } extension NSTextCheckingResult {     @NSCopying var orthography: NSOrthography? { get }     var grammarDetails: [String]? { get }     @NSCopying var date: NSDate? { get }     @NSCopying var timeZone: NSTimeZone? { get }     var duration: NSTimeInterval { get }     var components: [String : String]? { get }     @NSCopying var URL: NSURL? { get }     var replacementString: String? { get }     var alternativeStrings: [String]? { get }     @NSCopying var regularExpression: NSRegularExpression? { get }     var phoneNumber: String? { get }     var addressComponents: [String : String]? { get }     var numberOfRanges: Int { get }     func rangeAtIndex(_ idx: Int) -> NSRange     func resultByAdjustingRangesWithOffset(_ offset: Int) -> NSTextCheckingResult } extension NSTextCheckingResult {     class func orthographyCheckingResultWithRange(_ range: NSRange, orthography orthography: NSOrthography) -> NSTextCheckingResult     class func spellCheckingResultWithRange(_ range: NSRange) -> NSTextCheckingResult     class func grammarCheckingResultWithRange(_ range: NSRange, details details: [String]) -> NSTextCheckingResult     class func dateCheckingResultWithRange(_ range: NSRange, date date: NSDate) -> NSTextCheckingResult     class func dateCheckingResultWithRange(_ range: NSRange, date date: NSDate, timeZone timeZone: NSTimeZone, duration duration: NSTimeInterval) -> NSTextCheckingResult     class func addressCheckingResultWithRange(_ range: NSRange, components components: [String : String]) -> NSTextCheckingResult     class func linkCheckingResultWithRange(_ range: NSRange, URL url: NSURL) -> NSTextCheckingResult     class func quoteCheckingResultWithRange(_ range: NSRange, replacementString replacementString: String) -> NSTextCheckingResult     class func dashCheckingResultWithRange(_ range: NSRange, replacementString replacementString: String) -> NSTextCheckingResult     class func replacementCheckingResultWithRange(_ range: NSRange, replacementString replacementString: String) -> NSTextCheckingResult     class func correctionCheckingResultWithRange(_ range: NSRange, replacementString replacementString: String) -> NSTextCheckingResult     class func correctionCheckingResultWithRange(_ range: NSRange, replacementString replacementString: String, alternativeStrings alternativeStrings: [String]) -> NSTextCheckingResult     class func regularExpressionCheckingResultWithRanges(_ ranges: NSRangePointer, count count: Int, regularExpression regularExpression: NSRegularExpression) -> NSTextCheckingResult     class func phoneNumberCheckingResultWithRange(_ range: NSRange, phoneNumber phoneNumber: String) -> NSTextCheckingResult     class func transitInformationCheckingResultWithRange(_ range: NSRange, components components: [String : String]) -> NSTextCheckingResult } ``` |

Modified [NSTextCheckingResult.addressCheckingResultWithRange(_: NSRange, components: [String : String]) -> NSTextCheckingResult [class]](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1413828-addresscheckingresult)

|  | Declaration |
| --- | --- |
| From | ``` class func addressCheckingResultWithRange(_ range: NSRange, components components: [NSObject : AnyObject]) -> NSTextCheckingResult ``` |
| To | ``` class func addressCheckingResultWithRange(_ range: NSRange, components components: [String : String]) -> NSTextCheckingResult ``` |

Modified [NSTextCheckingResult.addressComponents](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1413728-addresscomponents)

|  | Declaration |
| --- | --- |
| From | ``` var addressComponents: [NSObject : AnyObject]? { get } ``` |
| To | ``` var addressComponents: [String : String]? { get } ``` |

Modified [NSTextCheckingResult.alternativeStrings](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1415454-alternativestrings)

|  | Declaration |
| --- | --- |
| From | ``` var alternativeStrings: [AnyObject]? { get } ``` |
| To | ``` var alternativeStrings: [String]? { get } ``` |

Modified [NSTextCheckingResult.components](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1407367-components)

|  | Declaration |
| --- | --- |
| From | ``` var components: [NSObject : AnyObject]? { get } ``` |
| To | ``` var components: [String : String]? { get } ``` |

Modified [NSTextCheckingResult.correctionCheckingResultWithRange(_: NSRange, replacementString: String, alternativeStrings: [String]) -> NSTextCheckingResult [class]](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1416640-correctioncheckingresultwithrang)

|  | Declaration |
| --- | --- |
| From | ``` class func correctionCheckingResultWithRange(_ range: NSRange, replacementString replacementString: String, alternativeStrings alternativeStrings: [AnyObject]) -> NSTextCheckingResult ``` |
| To | ``` class func correctionCheckingResultWithRange(_ range: NSRange, replacementString replacementString: String, alternativeStrings alternativeStrings: [String]) -> NSTextCheckingResult ``` |

Modified [NSTextCheckingResult.grammarCheckingResultWithRange(_: NSRange, details: [String]) -> NSTextCheckingResult [class]](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1407190-grammarcheckingresultwithrange)

|  | Declaration |
| --- | --- |
| From | ``` class func grammarCheckingResultWithRange(_ range: NSRange, details details: [AnyObject]) -> NSTextCheckingResult ``` |
| To | ``` class func grammarCheckingResultWithRange(_ range: NSRange, details details: [String]) -> NSTextCheckingResult ``` |

Modified [NSTextCheckingResult.grammarDetails](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1408959-grammardetails)

|  | Declaration |
| --- | --- |
| From | ``` var grammarDetails: [AnyObject]? { get } ``` |
| To | ``` var grammarDetails: [String]? { get } ``` |

Modified [NSTextCheckingResult.transitInformationCheckingResultWithRange(_: NSRange, components: [String : String]) -> NSTextCheckingResult [class]](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1408575-transitinformationcheckingresult)

|  | Declaration |
| --- | --- |
| From | ``` class func transitInformationCheckingResultWithRange(_ range: NSRange, components components: [NSObject : AnyObject]) -> NSTextCheckingResult ``` |
| To | ``` class func transitInformationCheckingResultWithRange(_ range: NSRange, components components: [String : String]) -> NSTextCheckingResult ``` |

Modified [NSTextCheckingType [struct]](https://developer.apple.com/documentation/foundation/nstextcheckingtype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSTextCheckingType : RawOptionSetType {     init(_ rawValue: UInt64)     init(rawValue rawValue: UInt64)     static var Orthography: NSTextCheckingType { get }     static var Spelling: NSTextCheckingType { get }     static var Grammar: NSTextCheckingType { get }     static var Date: NSTextCheckingType { get }     static var Address: NSTextCheckingType { get }     static var Link: NSTextCheckingType { get }     static var Quote: NSTextCheckingType { get }     static var Dash: NSTextCheckingType { get }     static var Replacement: NSTextCheckingType { get }     static var Correction: NSTextCheckingType { get }     static var RegularExpression: NSTextCheckingType { get }     static var PhoneNumber: NSTextCheckingType { get }     static var TransitInformation: NSTextCheckingType { get } } ``` | RawOptionSetType |
| To | ``` struct NSTextCheckingType : OptionSetType {     init(rawValue rawValue: UInt64)     static var Orthography: NSTextCheckingType { get }     static var Spelling: NSTextCheckingType { get }     static var Grammar: NSTextCheckingType { get }     static var Date: NSTextCheckingType { get }     static var Address: NSTextCheckingType { get }     static var Link: NSTextCheckingType { get }     static var Quote: NSTextCheckingType { get }     static var Dash: NSTextCheckingType { get }     static var Replacement: NSTextCheckingType { get }     static var Correction: NSTextCheckingType { get }     static var RegularExpression: NSTextCheckingType { get }     static var PhoneNumber: NSTextCheckingType { get }     static var TransitInformation: NSTextCheckingType { get } } ``` | OptionSetType |

Modified [NSThread](https://developer.apple.com/documentation/foundation/thread)

|  | Declaration |
| --- | --- |
| From | ``` class NSThread : NSObject {     class func currentThread() -> NSThread     class func detachNewThreadSelector(_ selector: Selector, toTarget target: AnyObject, withObject argument: AnyObject?)     class func isMultiThreaded() -> Bool     var threadDictionary: NSMutableDictionary { get }     class func sleepUntilDate(_ date: NSDate)     class func sleepForTimeInterval(_ ti: NSTimeInterval)     class func exit()     class func threadPriority() -> Double     class func setThreadPriority(_ p: Double) -> Bool     var threadPriority: Double     var qualityOfService: NSQualityOfService     class func callStackReturnAddresses() -> [AnyObject]     class func callStackSymbols() -> [AnyObject]     var name: String!     var stackSize: Int     var isMainThread: Bool { get }     class func isMainThread() -> Bool     class func mainThread() -> NSThread     init()     convenience init(target target: AnyObject, selector selector: Selector, object argument: AnyObject?)     var executing: Bool { get }     var finished: Bool { get }     var cancelled: Bool { get }     func cancel()     func start()     func main() } ``` |
| To | ``` class NSThread : NSObject {     class func currentThread() -> NSThread     class func detachNewThreadSelector(_ selector: Selector, toTarget target: AnyObject, withObject argument: AnyObject?)     class func isMultiThreaded() -> Bool     var threadDictionary: NSMutableDictionary { get }     class func sleepUntilDate(_ date: NSDate)     class func sleepForTimeInterval(_ ti: NSTimeInterval)     class func exit()     class func threadPriority() -> Double     class func setThreadPriority(_ p: Double) -> Bool     var threadPriority: Double     var qualityOfService: NSQualityOfService     class func callStackReturnAddresses() -> [NSNumber]     class func callStackSymbols() -> [String]     var name: String?     var stackSize: Int     var isMainThread: Bool { get }     class func isMainThread() -> Bool     class func mainThread() -> NSThread     init()     convenience init(target target: AnyObject, selector selector: Selector, object argument: AnyObject?)     var executing: Bool { get }     var finished: Bool { get }     var cancelled: Bool { get }     func cancel()     func start()     func main() } ``` |

Modified [NSThread.callStackReturnAddresses() -> [NSNumber] [class]](https://developer.apple.com/documentation/foundation/thread/1409565-callstackreturnaddresses)

|  | Declaration |
| --- | --- |
| From | ``` class func callStackReturnAddresses() -> [AnyObject] ``` |
| To | ``` class func callStackReturnAddresses() -> [NSNumber] ``` |

Modified [NSThread.callStackSymbols() -> [String] [class]](https://developer.apple.com/documentation/foundation/nsthread/1414836-callstacksymbols)

|  | Declaration |
| --- | --- |
| From | ``` class func callStackSymbols() -> [AnyObject] ``` |
| To | ``` class func callStackSymbols() -> [String] ``` |

Modified [NSThread.name](https://developer.apple.com/documentation/foundation/nsthread/1414122-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! ``` |
| To | ``` var name: String? ``` |

Modified [NSTimer](https://developer.apple.com/documentation/foundation/timer)

|  | Declaration |
| --- | --- |
| From | ``` class NSTimer : NSObject {     init(timeInterval ti: NSTimeInterval, invocation invocation: NSInvocation, repeats yesOrNo: Bool) -> NSTimer     class func timerWithTimeInterval(_ ti: NSTimeInterval, invocation invocation: NSInvocation, repeats yesOrNo: Bool) -> NSTimer     class func scheduledTimerWithTimeInterval(_ ti: NSTimeInterval, invocation invocation: NSInvocation, repeats yesOrNo: Bool) -> NSTimer     init(timeInterval ti: NSTimeInterval, target aTarget: AnyObject, selector aSelector: Selector, userInfo userInfo: AnyObject?, repeats yesOrNo: Bool) -> NSTimer     class func timerWithTimeInterval(_ ti: NSTimeInterval, target aTarget: AnyObject, selector aSelector: Selector, userInfo userInfo: AnyObject?, repeats yesOrNo: Bool) -> NSTimer     class func scheduledTimerWithTimeInterval(_ ti: NSTimeInterval, target aTarget: AnyObject, selector aSelector: Selector, userInfo userInfo: AnyObject?, repeats yesOrNo: Bool) -> NSTimer     init(fireDate date: NSDate, interval ti: NSTimeInterval, target t: AnyObject, selector s: Selector, userInfo ui: AnyObject?, repeats rep: Bool)     func fire()     @NSCopying var fireDate: NSDate     var timeInterval: NSTimeInterval { get }     var tolerance: NSTimeInterval     func invalidate()     var valid: Bool { get }     var userInfo: AnyObject? { get } } ``` |
| To | ``` class NSTimer : NSObject {      init(timeInterval ti: NSTimeInterval, invocation invocation: NSInvocation, repeats yesOrNo: Bool)     class func timerWithTimeInterval(_ ti: NSTimeInterval, invocation invocation: NSInvocation, repeats yesOrNo: Bool) -> NSTimer     class func scheduledTimerWithTimeInterval(_ ti: NSTimeInterval, invocation invocation: NSInvocation, repeats yesOrNo: Bool) -> NSTimer      init(timeInterval ti: NSTimeInterval, target aTarget: AnyObject, selector aSelector: Selector, userInfo userInfo: AnyObject?, repeats yesOrNo: Bool)     class func timerWithTimeInterval(_ ti: NSTimeInterval, target aTarget: AnyObject, selector aSelector: Selector, userInfo userInfo: AnyObject?, repeats yesOrNo: Bool) -> NSTimer     class func scheduledTimerWithTimeInterval(_ ti: NSTimeInterval, target aTarget: AnyObject, selector aSelector: Selector, userInfo userInfo: AnyObject?, repeats yesOrNo: Bool) -> NSTimer     init(fireDate date: NSDate, interval ti: NSTimeInterval, target t: AnyObject, selector s: Selector, userInfo ui: AnyObject?, repeats rep: Bool)     func fire()     @NSCopying var fireDate: NSDate     var timeInterval: NSTimeInterval { get }     var tolerance: NSTimeInterval     func invalidate()     var valid: Bool { get }     var userInfo: AnyObject? { get } } ``` |

Modified [NSTimer.init(timeInterval: NSTimeInterval, invocation: NSInvocation, repeats: Bool)](https://developer.apple.com/documentation/foundation/nstimer/1407170-timerwithtimeinterval)

|  | Declaration |
| --- | --- |
| From | ``` init(timeInterval ti: NSTimeInterval, invocation invocation: NSInvocation, repeats yesOrNo: Bool) -> NSTimer ``` |
| To | ``` init(timeInterval ti: NSTimeInterval, invocation invocation: NSInvocation, repeats yesOrNo: Bool) ``` |

Modified [NSTimer.init(timeInterval: NSTimeInterval, target: AnyObject, selector: Selector, userInfo: AnyObject?, repeats: Bool)](https://developer.apple.com/documentation/foundation/nstimer/1408356-timerwithtimeinterval)

|  | Declaration |
| --- | --- |
| From | ``` init(timeInterval ti: NSTimeInterval, target aTarget: AnyObject, selector aSelector: Selector, userInfo userInfo: AnyObject?, repeats yesOrNo: Bool) -> NSTimer ``` |
| To | ``` init(timeInterval ti: NSTimeInterval, target aTarget: AnyObject, selector aSelector: Selector, userInfo userInfo: AnyObject?, repeats yesOrNo: Bool) ``` |

Modified [NSTimeZone](https://developer.apple.com/documentation/foundation/nstimezone)

|  | Declaration |
| --- | --- |
| From | ``` class NSTimeZone : NSObject, NSCopying, NSSecureCoding, NSCoding {     var name: String { get }     @NSCopying var data: NSData { get }     func secondsFromGMTForDate(_ aDate: NSDate) -> Int     func abbreviationForDate(_ aDate: NSDate) -> String?     func isDaylightSavingTimeForDate(_ aDate: NSDate) -> Bool     func daylightSavingTimeOffsetForDate(_ aDate: NSDate) -> NSTimeInterval     func nextDaylightSavingTimeTransitionAfterDate(_ aDate: NSDate) -> NSDate? } extension NSTimeZone {     class func systemTimeZone() -> NSTimeZone     class func resetSystemTimeZone()     class func defaultTimeZone() -> NSTimeZone     class func setDefaultTimeZone(_ aTimeZone: NSTimeZone)     class func localTimeZone() -> NSTimeZone     class func knownTimeZoneNames() -> [AnyObject]     class func abbreviationDictionary() -> [NSObject : AnyObject]     class func setAbbreviationDictionary(_ dict: [NSObject : AnyObject])     class func timeZoneDataVersion() -> String     var secondsFromGMT: Int { get }     var abbreviation: String? { get }     var daylightSavingTime: Bool { get }     var daylightSavingTimeOffset: NSTimeInterval { get }     @NSCopying var nextDaylightSavingTimeTransition: NSDate? { get }     var description: String { get }     func isEqualToTimeZone(_ aTimeZone: NSTimeZone) -> Bool     func localizedName(_ style: NSTimeZoneNameStyle, locale locale: NSLocale?) -> String? } extension NSTimeZone {     convenience init?(name tzName: String)     class func timeZoneWithName(_ tzName: String) -> Self?     convenience init?(name tzName: String, data aData: NSData?)     class func timeZoneWithName(_ tzName: String, data aData: NSData?) -> Self?     init?(name tzName: String)     init?(name tzName: String, data aData: NSData?)     convenience init(forSecondsFromGMT seconds: Int)     class func timeZoneForSecondsFromGMT(_ seconds: Int) -> Self     convenience init?(abbreviation abbreviation: String)     class func timeZoneWithAbbreviation(_ abbreviation: String) -> Self? } ``` |
| To | ``` class NSTimeZone : NSObject, NSCopying, NSSecureCoding, NSCoding {     var name: String { get }     @NSCopying var data: NSData { get }     func secondsFromGMTForDate(_ aDate: NSDate) -> Int     func abbreviationForDate(_ aDate: NSDate) -> String?     func isDaylightSavingTimeForDate(_ aDate: NSDate) -> Bool     func daylightSavingTimeOffsetForDate(_ aDate: NSDate) -> NSTimeInterval     func nextDaylightSavingTimeTransitionAfterDate(_ aDate: NSDate) -> NSDate? } extension NSTimeZone {     class func systemTimeZone() -> NSTimeZone     class func resetSystemTimeZone()     class func defaultTimeZone() -> NSTimeZone     class func setDefaultTimeZone(_ aTimeZone: NSTimeZone)     class func localTimeZone() -> NSTimeZone     class func knownTimeZoneNames() -> [String]     class func abbreviationDictionary() -> [String : String]     class func setAbbreviationDictionary(_ dict: [String : String])     class func timeZoneDataVersion() -> String     var secondsFromGMT: Int { get }     var abbreviation: String? { get }     var daylightSavingTime: Bool { get }     var daylightSavingTimeOffset: NSTimeInterval { get }     @NSCopying var nextDaylightSavingTimeTransition: NSDate? { get }     var description: String { get }     func isEqualToTimeZone(_ aTimeZone: NSTimeZone) -> Bool     func localizedName(_ style: NSTimeZoneNameStyle, locale locale: NSLocale?) -> String? } extension NSTimeZone {     convenience init?(name tzName: String)     class func timeZoneWithName(_ tzName: String) -> Self?     convenience init?(name tzName: String, data aData: NSData?)     class func timeZoneWithName(_ tzName: String, data aData: NSData?) -> Self?     init?(name tzName: String)     init?(name tzName: String, data aData: NSData?)     convenience init(forSecondsFromGMT seconds: Int)     class func timeZoneForSecondsFromGMT(_ seconds: Int) -> Self     convenience init?(abbreviation abbreviation: String)     class func timeZoneWithAbbreviation(_ abbreviation: String) -> Self? } ``` |

Modified [NSTimeZone.abbreviationDictionary() -> [String : String] [class]](https://developer.apple.com/documentation/foundation/nstimezone/1387258-abbreviationdictionary)

|  | Declaration |
| --- | --- |
| From | ``` class func abbreviationDictionary() -> [NSObject : AnyObject] ``` |
| To | ``` class func abbreviationDictionary() -> [String : String] ``` |

Modified [NSTimeZone.knownTimeZoneNames() -> [String] [class]](https://developer.apple.com/documentation/foundation/nstimezone/1387223-knowntimezonenames)

|  | Declaration |
| --- | --- |
| From | ``` class func knownTimeZoneNames() -> [AnyObject] ``` |
| To | ``` class func knownTimeZoneNames() -> [String] ``` |

Modified NSTimeZone.setAbbreviationDictionary(_: [String : String]) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func setAbbreviationDictionary(_ dict: [NSObject : AnyObject]) ``` |
| To | ``` class func setAbbreviationDictionary(_ dict: [String : String]) ``` |

Modified [NSTimeZoneNameStyle [enum]](https://developer.apple.com/documentation/foundation/nstimezone/namestyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NSUbiquitousKeyValueStore](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore)

|  | Declaration |
| --- | --- |
| From | ``` class NSUbiquitousKeyValueStore : NSObject {     class func defaultStore() -> NSUbiquitousKeyValueStore     func objectForKey(_ aKey: String) -> AnyObject?     func setObject(_ anObject: AnyObject?, forKey aKey: String)     func removeObjectForKey(_ aKey: String)     func stringForKey(_ aKey: String) -> String?     func arrayForKey(_ aKey: String) -> [AnyObject]?     func dictionaryForKey(_ aKey: String) -> [NSObject : AnyObject]?     func dataForKey(_ aKey: String) -> NSData?     func longLongForKey(_ aKey: String) -> Int64     func doubleForKey(_ aKey: String) -> Double     func boolForKey(_ aKey: String) -> Bool     func setString(_ aString: String?, forKey aKey: String)     func setData(_ aData: NSData?, forKey aKey: String)     func setArray(_ anArray: [AnyObject]?, forKey aKey: String)     func setDictionary(_ aDictionary: [NSObject : AnyObject]?, forKey aKey: String)     func setLongLong(_ value: Int64, forKey aKey: String)     func setDouble(_ value: Double, forKey aKey: String)     func setBool(_ value: Bool, forKey aKey: String)     var dictionaryRepresentation: [NSObject : AnyObject] { get }     func synchronize() -> Bool } ``` |
| To | ``` class NSUbiquitousKeyValueStore : NSObject {     class func defaultStore() -> NSUbiquitousKeyValueStore     func objectForKey(_ aKey: String) -> AnyObject?     func setObject(_ anObject: AnyObject?, forKey aKey: String)     func removeObjectForKey(_ aKey: String)     func stringForKey(_ aKey: String) -> String?     func arrayForKey(_ aKey: String) -> [AnyObject]?     func dictionaryForKey(_ aKey: String) -> [String : AnyObject]?     func dataForKey(_ aKey: String) -> NSData?     func longLongForKey(_ aKey: String) -> Int64     func doubleForKey(_ aKey: String) -> Double     func boolForKey(_ aKey: String) -> Bool     func setString(_ aString: String?, forKey aKey: String)     func setData(_ aData: NSData?, forKey aKey: String)     func setArray(_ anArray: [AnyObject]?, forKey aKey: String)     func setDictionary(_ aDictionary: [String : AnyObject]?, forKey aKey: String)     func setLongLong(_ value: Int64, forKey aKey: String)     func setDouble(_ value: Double, forKey aKey: String)     func setBool(_ value: Bool, forKey aKey: String)     var dictionaryRepresentation: [String : AnyObject] { get }     func synchronize() -> Bool } ``` |

Modified [NSUbiquitousKeyValueStore.dictionaryForKey(_: String) -> [String : AnyObject]?](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1416241-dictionaryforkey)

|  | Declaration |
| --- | --- |
| From | ``` func dictionaryForKey(_ aKey: String) -> [NSObject : AnyObject]? ``` |
| To | ``` func dictionaryForKey(_ aKey: String) -> [String : AnyObject]? ``` |

Modified [NSUbiquitousKeyValueStore.dictionaryRepresentation](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1411129-dictionaryrepresentation)

|  | Declaration |
| --- | --- |
| From | ``` var dictionaryRepresentation: [NSObject : AnyObject] { get } ``` |
| To | ``` var dictionaryRepresentation: [String : AnyObject] { get } ``` |

Modified [NSUbiquitousKeyValueStore.setDictionary(_: [String : AnyObject]?, forKey: String)](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1417155-set)

|  | Declaration |
| --- | --- |
| From | ``` func setDictionary(_ aDictionary: [NSObject : AnyObject]?, forKey aKey: String) ``` |
| To | ``` func setDictionary(_ aDictionary: [String : AnyObject]?, forKey aKey: String) ``` |

Modified [NSUndoManager](https://developer.apple.com/documentation/foundation/nsundomanager)

|  | Declaration |
| --- | --- |
| From | ``` class NSUndoManager : NSObject {     func beginUndoGrouping()     func endUndoGrouping()     var groupingLevel: Int { get }     func disableUndoRegistration()     func enableUndoRegistration()     var undoRegistrationEnabled: Bool { get }     var groupsByEvent: Bool     var levelsOfUndo: Int     var runLoopModes: [AnyObject]     func undo()     func redo()     func undoNestedGroup()     var canUndo: Bool { get }     var canRedo: Bool { get }     var undoing: Bool { get }     var redoing: Bool { get }     func removeAllActions()     func removeAllActionsWithTarget(_ target: AnyObject)     func registerUndoWithTarget(_ target: AnyObject, selector selector: Selector, object anObject: AnyObject?)     func prepareWithInvocationTarget(_ target: AnyObject) -> AnyObject     func setActionIsDiscardable(_ discardable: Bool)     var undoActionIsDiscardable: Bool { get }     var redoActionIsDiscardable: Bool { get }     var undoActionName: String { get }     var redoActionName: String { get }     func setActionName(_ actionName: String)     var undoMenuItemTitle: String { get }     var redoMenuItemTitle: String { get }     func undoMenuTitleForUndoActionName(_ actionName: String) -> String     func redoMenuTitleForUndoActionName(_ actionName: String) -> String } ``` |
| To | ``` class NSUndoManager : NSObject {     func beginUndoGrouping()     func endUndoGrouping()     var groupingLevel: Int { get }     func disableUndoRegistration()     func enableUndoRegistration()     var undoRegistrationEnabled: Bool { get }     var groupsByEvent: Bool     var levelsOfUndo: Int     var runLoopModes: [String]     func undo()     func redo()     func undoNestedGroup()     var canUndo: Bool { get }     var canRedo: Bool { get }     var undoing: Bool { get }     var redoing: Bool { get }     func removeAllActions()     func removeAllActionsWithTarget(_ target: AnyObject)     func registerUndoWithTarget(_ target: AnyObject, selector selector: Selector, object anObject: AnyObject?)     func prepareWithInvocationTarget(_ target: AnyObject) -> AnyObject     func __registerUndoWithTarget(_ target: AnyObject, handler undoHandler: (AnyObject) -> Void)     func setActionIsDiscardable(_ discardable: Bool)     var undoActionIsDiscardable: Bool { get }     var redoActionIsDiscardable: Bool { get }     var undoActionName: String { get }     var redoActionName: String { get }     func setActionName(_ actionName: String)     var undoMenuItemTitle: String { get }     var redoMenuItemTitle: String { get }     func undoMenuTitleForUndoActionName(_ actionName: String) -> String     func redoMenuTitleForUndoActionName(_ actionName: String) -> String } extension NSUndoManager {     func registerUndoWithTarget<TargetType>(_ target: TargetType, handler handler: TargetType -> ()) } extension NSUndoManager {     func registerUndoWithTarget<TargetType>(_ target: TargetType, handler handler: TargetType -> ()) } ``` |

Modified [NSUndoManager.runLoopModes](https://developer.apple.com/documentation/foundation/nsundomanager/1409504-runloopmodes)

|  | Declaration |
| --- | --- |
| From | ``` var runLoopModes: [AnyObject] ``` |
| To | ``` var runLoopModes: [String] ``` |

Modified [NSURL](https://developer.apple.com/documentation/foundation/nsurl)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSURL : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init?(scheme scheme: String, host host: String?, path path: String)     init?(fileURLWithPath path: String, isDirectory isDir: Bool)     init?(fileURLWithPath path: String)     class func fileURLWithPath(_ path: String, isDirectory isDir: Bool) -> NSURL?     class func fileURLWithPath(_ path: String) -> NSURL?     init?(fileURLWithFileSystemRepresentation path: UnsafePointer<Int8>, isDirectory isDir: Bool, relativeToURL baseURL: NSURL?)     class func fileURLWithFileSystemRepresentation(_ path: UnsafePointer<Int8>, isDirectory isDir: Bool, relativeToURL baseURL: NSURL?) -> NSURL?     convenience init?(string URLString: String)     init?(string URLString: String, relativeToURL baseURL: NSURL?)     class func URLWithString(_ URLString: String) -> Self?     class func URLWithString(_ URLString: String, relativeToURL baseURL: NSURL?) -> Self?     var absoluteString: String? { get }     var relativeString: String? { get }     @NSCopying var baseURL: NSURL? { get }     @NSCopying var absoluteURL: NSURL? { get }     var scheme: String? { get }     var resourceSpecifier: String? { get }     var host: String? { get }     @NSCopying var port: NSNumber? { get }     var user: String? { get }     var password: String? { get }     var path: String? { get }     var fragment: String? { get }     var parameterString: String? { get }     var query: String? { get }     var relativePath: String? { get }     func getFileSystemRepresentation(_ buffer: UnsafeMutablePointer<Int8>, maxLength maxBufferLength: Int) -> Bool     var fileSystemRepresentation: UnsafePointer<Int8> { get }     var fileURL: Bool { get }     @NSCopying var standardizedURL: NSURL? { get }     func checkResourceIsReachableAndReturnError(_ error: NSErrorPointer) -> Bool     func isFileReferenceURL() -> Bool     func fileReferenceURL() -> NSURL?     @NSCopying var filePathURL: NSURL? { get }     func getResourceValue(_ value: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey key: String, error error: NSErrorPointer) -> Bool     func resourceValuesForKeys(_ keys: [AnyObject], error error: NSErrorPointer) -> [NSObject : AnyObject]?     func setResourceValue(_ value: AnyObject?, forKey key: String, error error: NSErrorPointer) -> Bool     func setResourceValues(_ keyedValues: [NSObject : AnyObject], error error: NSErrorPointer) -> Bool     func removeCachedResourceValueForKey(_ key: String)     func removeAllCachedResourceValues()     func setTemporaryResourceValue(_ value: AnyObject?, forKey key: String)     func bookmarkDataWithOptions(_ options: NSURLBookmarkCreationOptions, includingResourceValuesForKeys keys: [AnyObject]?, relativeToURL relativeURL: NSURL?, error error: NSErrorPointer) -> NSData?     convenience init?(byResolvingBookmarkData bookmarkData: NSData, options options: NSURLBookmarkResolutionOptions, relativeToURL relativeURL: NSURL?, bookmarkDataIsStale isStale: UnsafeMutablePointer<ObjCBool>, error error: NSErrorPointer)     class func URLByResolvingBookmarkData(_ bookmarkData: NSData, options options: NSURLBookmarkResolutionOptions, relativeToURL relativeURL: NSURL?, bookmarkDataIsStale isStale: UnsafeMutablePointer<ObjCBool>, error error: NSErrorPointer) -> Self?     class func resourceValuesForKeys(_ keys: [AnyObject], fromBookmarkData bookmarkData: NSData) -> [NSObject : AnyObject]?     class func writeBookmarkData(_ bookmarkData: NSData, toURL bookmarkFileURL: NSURL, options options: NSURLBookmarkFileCreationOptions, error error: NSErrorPointer) -> Bool     class func bookmarkDataWithContentsOfURL(_ bookmarkFileURL: NSURL, error error: NSErrorPointer) -> NSData?     convenience init?(byResolvingAliasFileAtURL url: NSURL, options options: NSURLBookmarkResolutionOptions, error error: NSErrorPointer)     class func URLByResolvingAliasFileAtURL(_ url: NSURL, options options: NSURLBookmarkResolutionOptions, error error: NSErrorPointer) -> Self?     func startAccessingSecurityScopedResource() -> Bool     func stopAccessingSecurityScopedResource() } extension NSURL : Reflectable {     func getMirror() -> MirrorType } extension NSURL {     func getPromisedItemResourceValue(_ value: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey key: String, error error: NSErrorPointer) -> Bool     func promisedItemResourceValuesForKeys(_ keys: [AnyObject], error error: NSErrorPointer) -> [NSObject : AnyObject]?     func checkPromisedItemIsReachableAndReturnError(_ error: NSErrorPointer) -> Bool } extension NSURL {     class func fileURLWithPathComponents(_ components: [AnyObject]) -> NSURL?     var pathComponents: [AnyObject]? { get }     var lastPathComponent: String? { get }     var pathExtension: String? { get }     func URLByAppendingPathComponent(_ pathComponent: String) -> NSURL     func URLByAppendingPathComponent(_ pathComponent: String, isDirectory isDirectory: Bool) -> NSURL     @NSCopying var URLByDeletingLastPathComponent: NSURL? { get }     func URLByAppendingPathExtension(_ pathExtension: String) -> NSURL     @NSCopying var URLByDeletingPathExtension: NSURL? { get }     @NSCopying var URLByStandardizingPath: NSURL? { get }     @NSCopying var URLByResolvingSymlinksInPath: NSURL? { get } } extension NSURL : Reflectable {     func getMirror() -> MirrorType } extension NSURL : QLPreviewItem, NSObjectProtocol { } ``` | AnyObject, NSCoding, NSCopying, NSObjectProtocol, NSSecureCoding, QLPreviewItem, Reflectable |
| To | ``` class NSURL : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init?(scheme scheme: String, host host: String?, path path: String)     init(fileURLWithPath path: String, isDirectory isDir: Bool, relativeToURL baseURL: NSURL?)     init(fileURLWithPath path: String, relativeToURL baseURL: NSURL?)     init(fileURLWithPath path: String, isDirectory isDir: Bool)     init(fileURLWithPath path: String)     class func fileURLWithPath(_ path: String, isDirectory isDir: Bool, relativeToURL baseURL: NSURL?) -> NSURL     class func fileURLWithPath(_ path: String, relativeToURL baseURL: NSURL?) -> NSURL     class func fileURLWithPath(_ path: String, isDirectory isDir: Bool) -> NSURL     class func fileURLWithPath(_ path: String) -> NSURL     init(fileURLWithFileSystemRepresentation path: UnsafePointer<Int8>, isDirectory isDir: Bool, relativeToURL baseURL: NSURL?)     class func fileURLWithFileSystemRepresentation(_ path: UnsafePointer<Int8>, isDirectory isDir: Bool, relativeToURL baseURL: NSURL?) -> NSURL     convenience init?(string URLString: String)     init?(string URLString: String, relativeToURL baseURL: NSURL?)     class func URLWithString(_ URLString: String) -> Self?     class func URLWithString(_ URLString: String, relativeToURL baseURL: NSURL?) -> Self?     init(dataRepresentation data: NSData, relativeToURL baseURL: NSURL?)     class func URLWithDataRepresentation(_ data: NSData, relativeToURL baseURL: NSURL?) -> NSURL     init(absoluteURLWithDataRepresentation data: NSData, relativeToURL baseURL: NSURL?)     class func absoluteURLWithDataRepresentation(_ data: NSData, relativeToURL baseURL: NSURL?) -> NSURL     @NSCopying var dataRepresentation: NSData { get }     var absoluteString: String { get }     var relativeString: String? { get }     @NSCopying var baseURL: NSURL? { get }     @NSCopying var absoluteURL: NSURL { get }     var scheme: String { get }     var resourceSpecifier: String { get }     var host: String? { get }     @NSCopying var port: NSNumber? { get }     var user: String? { get }     var password: String? { get }     var path: String? { get }     var fragment: String? { get }     var parameterString: String? { get }     var query: String? { get }     var relativePath: String? { get }     var hasDirectoryPath: Bool { get }     func getFileSystemRepresentation(_ buffer: UnsafeMutablePointer<Int8>, maxLength maxBufferLength: Int) -> Bool     var fileSystemRepresentation: UnsafePointer<Int8> { get }     var fileURL: Bool { get }     @NSCopying var standardizedURL: NSURL? { get }     func checkResourceIsReachableAndReturnError(_ error: NSErrorPointer) -> Bool     func isFileReferenceURL() -> Bool     func fileReferenceURL() -> NSURL?     @NSCopying var filePathURL: NSURL? { get }     func getResourceValue(_ value: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey key: String) throws     func resourceValuesForKeys(_ keys: [String]) throws -> [String : AnyObject]     func setResourceValue(_ value: AnyObject?, forKey key: String) throws     func setResourceValues(_ keyedValues: [String : AnyObject]) throws     func removeCachedResourceValueForKey(_ key: String)     func removeAllCachedResourceValues()     func setTemporaryResourceValue(_ value: AnyObject?, forKey key: String)     func bookmarkDataWithOptions(_ options: NSURLBookmarkCreationOptions, includingResourceValuesForKeys keys: [String]?, relativeToURL relativeURL: NSURL?) throws -> NSData     convenience init(byResolvingBookmarkData bookmarkData: NSData, options options: NSURLBookmarkResolutionOptions, relativeToURL relativeURL: NSURL?, bookmarkDataIsStale isStale: UnsafeMutablePointer<ObjCBool>) throws     class func URLByResolvingBookmarkData(_ bookmarkData: NSData, options options: NSURLBookmarkResolutionOptions, relativeToURL relativeURL: NSURL?, bookmarkDataIsStale isStale: UnsafeMutablePointer<ObjCBool>) throws -> Self     class func resourceValuesForKeys(_ keys: [String], fromBookmarkData bookmarkData: NSData) -> [String : AnyObject]?     class func writeBookmarkData(_ bookmarkData: NSData, toURL bookmarkFileURL: NSURL, options options: NSURLBookmarkFileCreationOptions) throws     class func bookmarkDataWithContentsOfURL(_ bookmarkFileURL: NSURL) throws -> NSData     convenience init(byResolvingAliasFileAtURL url: NSURL, options options: NSURLBookmarkResolutionOptions) throws     class func URLByResolvingAliasFileAtURL(_ url: NSURL, options options: NSURLBookmarkResolutionOptions) throws -> Self     func startAccessingSecurityScopedResource() -> Bool     func stopAccessingSecurityScopedResource() } extension NSURL : _Reflectable { } extension NSURL {     func getPromisedItemResourceValue(_ value: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey key: String) throws     func promisedItemResourceValuesForKeys(_ keys: [String]) throws -> [String : AnyObject]     func checkPromisedItemIsReachableAndReturnError(_ error: NSErrorPointer) -> Bool } extension NSURL {     class func fileURLWithPathComponents(_ components: [String]) -> NSURL?     var pathComponents: [String]? { get }     var lastPathComponent: String? { get }     var pathExtension: String? { get }     func URLByAppendingPathComponent(_ pathComponent: String) -> NSURL     func URLByAppendingPathComponent(_ pathComponent: String, isDirectory isDirectory: Bool) -> NSURL     @NSCopying var URLByDeletingLastPathComponent: NSURL? { get }     func URLByAppendingPathExtension(_ pathExtension: String) -> NSURL     @NSCopying var URLByDeletingPathExtension: NSURL? { get }     @NSCopying var URLByStandardizingPath: NSURL? { get }     @NSCopying var URLByResolvingSymlinksInPath: NSURL? { get } } extension NSURL : _Reflectable { } extension NSURL : QLPreviewItem { } ``` | AnyObject, NSCoding, NSCopying, NSObjectProtocol, NSSecureCoding, QLPreviewItem |

Modified [NSURL.absoluteString](https://developer.apple.com/documentation/foundation/nsurl/1409868-absolutestring)

|  | Declaration |
| --- | --- |
| From | ``` var absoluteString: String? { get } ``` |
| To | ``` var absoluteString: String { get } ``` |

Modified [NSURL.absoluteURL](https://developer.apple.com/documentation/foundation/nsurl/1414266-absoluteurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var absoluteURL: NSURL? { get } ``` |
| To | ``` @NSCopying var absoluteURL: NSURL { get } ``` |

Modified [NSURL.bookmarkDataWithContentsOfURL(_: NSURL) throws -> NSData [class]](https://developer.apple.com/documentation/foundation/nsurl/1408344-bookmarkdatawithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` class func bookmarkDataWithContentsOfURL(_ bookmarkFileURL: NSURL, error error: NSErrorPointer) -> NSData? ``` |
| To | ``` class func bookmarkDataWithContentsOfURL(_ bookmarkFileURL: NSURL) throws -> NSData ``` |

Modified [NSURL.bookmarkDataWithOptions(_: NSURLBookmarkCreationOptions, includingResourceValuesForKeys: [String]?, relativeToURL: NSURL?) throws -> NSData](https://developer.apple.com/documentation/foundation/nsurl/1417795-bookmarkdatawithoptions)

|  | Declaration |
| --- | --- |
| From | ``` func bookmarkDataWithOptions(_ options: NSURLBookmarkCreationOptions, includingResourceValuesForKeys keys: [AnyObject]?, relativeToURL relativeURL: NSURL?, error error: NSErrorPointer) -> NSData? ``` |
| To | ``` func bookmarkDataWithOptions(_ options: NSURLBookmarkCreationOptions, includingResourceValuesForKeys keys: [String]?, relativeToURL relativeURL: NSURL?) throws -> NSData ``` |

Modified [NSURL.fileURLWithFileSystemRepresentation(_: UnsafePointer<Int8>, isDirectory: Bool, relativeToURL: NSURL?) -> NSURL [class]](https://developer.apple.com/documentation/foundation/nsurl/1411492-fileurl)

|  | Declaration |
| --- | --- |
| From | ``` class func fileURLWithFileSystemRepresentation(_ path: UnsafePointer<Int8>, isDirectory isDir: Bool, relativeToURL baseURL: NSURL?) -> NSURL? ``` |
| To | ``` class func fileURLWithFileSystemRepresentation(_ path: UnsafePointer<Int8>, isDirectory isDir: Bool, relativeToURL baseURL: NSURL?) -> NSURL ``` |

Modified [NSURL.fileURLWithPath(_: String) -> NSURL [class]](https://developer.apple.com/documentation/foundation/nsurl/1410828-fileurl)

|  | Declaration |
| --- | --- |
| From | ``` class func fileURLWithPath(_ path: String) -> NSURL? ``` |
| To | ``` class func fileURLWithPath(_ path: String) -> NSURL ``` |

Modified [NSURL.fileURLWithPath(_: String, isDirectory: Bool) -> NSURL [class]](https://developer.apple.com/documentation/foundation/nsurl/1414650-fileurl)

|  | Declaration |
| --- | --- |
| From | ``` class func fileURLWithPath(_ path: String, isDirectory isDir: Bool) -> NSURL? ``` |
| To | ``` class func fileURLWithPath(_ path: String, isDirectory isDir: Bool) -> NSURL ``` |

Modified [NSURL.fileURLWithPathComponents(_: [String]) -> NSURL? [class]](https://developer.apple.com/documentation/foundation/nsurl/1414206-fileurl)

|  | Declaration |
| --- | --- |
| From | ``` class func fileURLWithPathComponents(_ components: [AnyObject]) -> NSURL? ``` |
| To | ``` class func fileURLWithPathComponents(_ components: [String]) -> NSURL? ``` |

Modified [NSURL.getPromisedItemResourceValue(_: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey: String) throws](https://developer.apple.com/documentation/foundation/nsurl/1414238-getpromiseditemresourcevalue)

|  | Declaration |
| --- | --- |
| From | ``` func getPromisedItemResourceValue(_ value: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey key: String, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func getPromisedItemResourceValue(_ value: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey key: String) throws ``` |

Modified [NSURL.getResourceValue(_: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey: String) throws](https://developer.apple.com/documentation/foundation/nsurl/1408874-getresourcevalue)

|  | Declaration |
| --- | --- |
| From | ``` func getResourceValue(_ value: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey key: String, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func getResourceValue(_ value: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey key: String) throws ``` |

Modified [NSURL.init(byResolvingAliasFileAtURL: NSURL, options: NSURLBookmarkResolutionOptions) throws](https://developer.apple.com/documentation/foundation/nsurl/1416404-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init?(byResolvingAliasFileAtURL url: NSURL, options options: NSURLBookmarkResolutionOptions, error error: NSErrorPointer) ``` |
| To | ``` convenience init(byResolvingAliasFileAtURL url: NSURL, options options: NSURLBookmarkResolutionOptions) throws ``` |

Modified [NSURL.init(byResolvingBookmarkData: NSData, options: NSURLBookmarkResolutionOptions, relativeToURL: NSURL?, bookmarkDataIsStale: UnsafeMutablePointer<ObjCBool>) throws](https://developer.apple.com/documentation/foundation/nsurl/1413475-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init?(byResolvingBookmarkData bookmarkData: NSData, options options: NSURLBookmarkResolutionOptions, relativeToURL relativeURL: NSURL?, bookmarkDataIsStale isStale: UnsafeMutablePointer<ObjCBool>, error error: NSErrorPointer) ``` |
| To | ``` convenience init(byResolvingBookmarkData bookmarkData: NSData, options options: NSURLBookmarkResolutionOptions, relativeToURL relativeURL: NSURL?, bookmarkDataIsStale isStale: UnsafeMutablePointer<ObjCBool>) throws ``` |

Modified [NSURL.init(fileURLWithFileSystemRepresentation: UnsafePointer<Int8>, isDirectory: Bool, relativeToURL: NSURL?)](https://developer.apple.com/documentation/foundation/nsurl/1411210-initfileurlwithfilesystemreprese)

|  | Declaration |
| --- | --- |
| From | ``` init?(fileURLWithFileSystemRepresentation path: UnsafePointer<Int8>, isDirectory isDir: Bool, relativeToURL baseURL: NSURL?) ``` |
| To | ``` init(fileURLWithFileSystemRepresentation path: UnsafePointer<Int8>, isDirectory isDir: Bool, relativeToURL baseURL: NSURL?) ``` |

Modified [NSURL.init(fileURLWithPath: String)](https://developer.apple.com/documentation/foundation/nsurl/1410301-init)

|  | Declaration |
| --- | --- |
| From | ``` init?(fileURLWithPath path: String) ``` |
| To | ``` init(fileURLWithPath path: String) ``` |

Modified [NSURL.init(fileURLWithPath: String, isDirectory: Bool)](https://developer.apple.com/documentation/foundation/nsurl/1417505-initfileurlwithpath)

|  | Declaration |
| --- | --- |
| From | ``` init?(fileURLWithPath path: String, isDirectory isDir: Bool) ``` |
| To | ``` init(fileURLWithPath path: String, isDirectory isDir: Bool) ``` |

Modified [NSURL.init(scheme: String, host: String?, path: String)](https://developer.apple.com/documentation/foundation/nsurl/1414181-init)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [NSURL.pathComponents](https://developer.apple.com/documentation/foundation/nsurl/1407365-pathcomponents)

|  | Declaration |
| --- | --- |
| From | ``` var pathComponents: [AnyObject]? { get } ``` |
| To | ``` var pathComponents: [String]? { get } ``` |

Modified [NSURL.promisedItemResourceValuesForKeys(_: [String]) throws -> [String : AnyObject]](https://developer.apple.com/documentation/foundation/nsurl/1407746-promiseditemresourcevalues)

|  | Declaration |
| --- | --- |
| From | ``` func promisedItemResourceValuesForKeys(_ keys: [AnyObject], error error: NSErrorPointer) -> [NSObject : AnyObject]? ``` |
| To | ``` func promisedItemResourceValuesForKeys(_ keys: [String]) throws -> [String : AnyObject] ``` |

Modified [NSURL.resourceSpecifier](https://developer.apple.com/documentation/foundation/nsurl/1415309-resourcespecifier)

|  | Declaration |
| --- | --- |
| From | ``` var resourceSpecifier: String? { get } ``` |
| To | ``` var resourceSpecifier: String { get } ``` |

Modified [NSURL.resourceValuesForKeys(_: [String]) throws -> [String : AnyObject]](https://developer.apple.com/documentation/foundation/nsurl/1417657-resourcevaluesforkeys)

|  | Declaration |
| --- | --- |
| From | ``` func resourceValuesForKeys(_ keys: [AnyObject], error error: NSErrorPointer) -> [NSObject : AnyObject]? ``` |
| To | ``` func resourceValuesForKeys(_ keys: [String]) throws -> [String : AnyObject] ``` |

Modified [NSURL.resourceValuesForKeys(_: [String], fromBookmarkData: NSData) -> [String : AnyObject]? [class]](https://developer.apple.com/documentation/foundation/nsurl/1418097-resourcevaluesforkeys)

|  | Declaration |
| --- | --- |
| From | ``` class func resourceValuesForKeys(_ keys: [AnyObject], fromBookmarkData bookmarkData: NSData) -> [NSObject : AnyObject]? ``` |
| To | ``` class func resourceValuesForKeys(_ keys: [String], fromBookmarkData bookmarkData: NSData) -> [String : AnyObject]? ``` |

Modified [NSURL.scheme](https://developer.apple.com/documentation/foundation/nsurl/1413437-scheme)

|  | Declaration |
| --- | --- |
| From | ``` var scheme: String? { get } ``` |
| To | ``` var scheme: String { get } ``` |

Modified [NSURL.setResourceValue(_: AnyObject?, forKey: String) throws](https://developer.apple.com/documentation/foundation/nsurl/1413819-setresourcevalue)

|  | Declaration |
| --- | --- |
| From | ``` func setResourceValue(_ value: AnyObject?, forKey key: String, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func setResourceValue(_ value: AnyObject?, forKey key: String) throws ``` |

Modified [NSURL.setResourceValues(_: [String : AnyObject]) throws](https://developer.apple.com/documentation/foundation/nsurl/1408208-setresourcevalues)

|  | Declaration |
| --- | --- |
| From | ``` func setResourceValues(_ keyedValues: [NSObject : AnyObject], error error: NSErrorPointer) -> Bool ``` |
| To | ``` func setResourceValues(_ keyedValues: [String : AnyObject]) throws ``` |

Modified [NSURL.writeBookmarkData(_: NSData, toURL: NSURL, options: NSURLBookmarkFileCreationOptions) throws [class]](https://developer.apple.com/documentation/foundation/nsurl/1408532-writebookmarkdata)

|  | Declaration |
| --- | --- |
| From | ``` class func writeBookmarkData(_ bookmarkData: NSData, toURL bookmarkFileURL: NSURL, options options: NSURLBookmarkFileCreationOptions, error error: NSErrorPointer) -> Bool ``` |
| To | ``` class func writeBookmarkData(_ bookmarkData: NSData, toURL bookmarkFileURL: NSURL, options options: NSURLBookmarkFileCreationOptions) throws ``` |

Modified [NSURLAuthenticationChallenge](https://developer.apple.com/documentation/foundation/nsurlauthenticationchallenge)

|  | Declaration |
| --- | --- |
| From | ``` class NSURLAuthenticationChallenge : NSObject, NSSecureCoding, NSCoding {     init(protectionSpace space: NSURLProtectionSpace, proposedCredential credential: NSURLCredential?, previousFailureCount previousFailureCount: Int, failureResponse response: NSURLResponse?, error error: NSError?, sender sender: NSURLAuthenticationChallengeSender)     init(authenticationChallenge challenge: NSURLAuthenticationChallenge, sender sender: NSURLAuthenticationChallengeSender)     @NSCopying var protectionSpace: NSURLProtectionSpace { get }     @NSCopying var proposedCredential: NSURLCredential? { get }     var previousFailureCount: Int { get }     @NSCopying var failureResponse: NSURLResponse? { get }     @NSCopying var error: NSError? { get }     var sender: NSURLAuthenticationChallengeSender { get } } ``` |
| To | ``` class NSURLAuthenticationChallenge : NSObject, NSSecureCoding, NSCoding {     init(protectionSpace space: NSURLProtectionSpace, proposedCredential credential: NSURLCredential?, previousFailureCount previousFailureCount: Int, failureResponse response: NSURLResponse?, error error: NSError?, sender sender: NSURLAuthenticationChallengeSender)     init(authenticationChallenge challenge: NSURLAuthenticationChallenge, sender sender: NSURLAuthenticationChallengeSender)     @NSCopying var protectionSpace: NSURLProtectionSpace { get }     @NSCopying var proposedCredential: NSURLCredential? { get }     var previousFailureCount: Int { get }     @NSCopying var failureResponse: NSURLResponse? { get }     @NSCopying var error: NSError? { get }     var sender: NSURLAuthenticationChallengeSender? { get } } ``` |

Modified [NSURLAuthenticationChallenge.sender](https://developer.apple.com/documentation/foundation/nsurlauthenticationchallenge/1407533-sender)

|  | Declaration |
| --- | --- |
| From | ``` var sender: NSURLAuthenticationChallengeSender { get } ``` |
| To | ``` var sender: NSURLAuthenticationChallengeSender? { get } ``` |

Modified [NSURLBookmarkCreationOptions [struct]](https://developer.apple.com/documentation/foundation/nsurl/bookmarkcreationoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSURLBookmarkCreationOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var PreferFileIDResolution: NSURLBookmarkCreationOptions { get }     static var MinimalBookmark: NSURLBookmarkCreationOptions { get }     static var SuitableForBookmarkFile: NSURLBookmarkCreationOptions { get }     static var WithSecurityScope: NSURLBookmarkCreationOptions { get }     static var SecurityScopeAllowOnlyReadAccess: NSURLBookmarkCreationOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSURLBookmarkCreationOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var PreferFileIDResolution: NSURLBookmarkCreationOptions { get }     static var MinimalBookmark: NSURLBookmarkCreationOptions { get }     static var SuitableForBookmarkFile: NSURLBookmarkCreationOptions { get }     static var WithSecurityScope: NSURLBookmarkCreationOptions { get }     static var SecurityScopeAllowOnlyReadAccess: NSURLBookmarkCreationOptions { get } } ``` | OptionSetType |

Modified [NSURLBookmarkResolutionOptions [struct]](https://developer.apple.com/documentation/foundation/nsurl/bookmarkresolutionoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSURLBookmarkResolutionOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var WithoutUI: NSURLBookmarkResolutionOptions { get }     static var WithoutMounting: NSURLBookmarkResolutionOptions { get }     static var WithSecurityScope: NSURLBookmarkResolutionOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSURLBookmarkResolutionOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var WithoutUI: NSURLBookmarkResolutionOptions { get }     static var WithoutMounting: NSURLBookmarkResolutionOptions { get }     static var WithSecurityScope: NSURLBookmarkResolutionOptions { get } } ``` | OptionSetType |

Modified [NSURLCache](https://developer.apple.com/documentation/foundation/nsurlcache)

|  | Declaration |
| --- | --- |
| From | ``` class NSURLCache : NSObject {     class func sharedURLCache() -> NSURLCache     class func setSharedURLCache(_ cache: NSURLCache)     init(memoryCapacity memoryCapacity: Int, diskCapacity diskCapacity: Int, diskPath path: String?)     func cachedResponseForRequest(_ request: NSURLRequest) -> NSCachedURLResponse?     func storeCachedResponse(_ cachedResponse: NSCachedURLResponse, forRequest request: NSURLRequest)     func removeCachedResponseForRequest(_ request: NSURLRequest)     func removeAllCachedResponses()     func removeCachedResponsesSinceDate(_ date: NSDate)     var memoryCapacity: Int     var diskCapacity: Int     var currentMemoryUsage: Int { get }     var currentDiskUsage: Int { get } } extension NSURLCache {     func storeCachedResponse(_ cachedResponse: NSCachedURLResponse, forDataTask dataTask: NSURLSessionDataTask)     func getCachedResponseForDataTask(_ dataTask: NSURLSessionDataTask, completionHandler completionHandler: (NSCachedURLResponse!) -> Void)     func removeCachedResponseForDataTask(_ dataTask: NSURLSessionDataTask) } ``` |
| To | ``` class NSURLCache : NSObject {     class func sharedURLCache() -> NSURLCache     class func setSharedURLCache(_ cache: NSURLCache)     init(memoryCapacity memoryCapacity: Int, diskCapacity diskCapacity: Int, diskPath path: String?)     func cachedResponseForRequest(_ request: NSURLRequest) -> NSCachedURLResponse?     func storeCachedResponse(_ cachedResponse: NSCachedURLResponse, forRequest request: NSURLRequest)     func removeCachedResponseForRequest(_ request: NSURLRequest)     func removeAllCachedResponses()     func removeCachedResponsesSinceDate(_ date: NSDate)     var memoryCapacity: Int     var diskCapacity: Int     var currentMemoryUsage: Int { get }     var currentDiskUsage: Int { get } } extension NSURLCache {     func storeCachedResponse(_ cachedResponse: NSCachedURLResponse, forDataTask dataTask: NSURLSessionDataTask)     func getCachedResponseForDataTask(_ dataTask: NSURLSessionDataTask, completionHandler completionHandler: (NSCachedURLResponse?) -> Void)     func removeCachedResponseForDataTask(_ dataTask: NSURLSessionDataTask) } ``` |

Modified [NSURLCache.getCachedResponseForDataTask(_: NSURLSessionDataTask, completionHandler: (NSCachedURLResponse?) -> Void)](https://developer.apple.com/documentation/foundation/nsurlcache/1409184-getcachedresponsefordatatask)

|  | Declaration |
| --- | --- |
| From | ``` func getCachedResponseForDataTask(_ dataTask: NSURLSessionDataTask, completionHandler completionHandler: (NSCachedURLResponse!) -> Void) ``` |
| To | ``` func getCachedResponseForDataTask(_ dataTask: NSURLSessionDataTask, completionHandler completionHandler: (NSCachedURLResponse?) -> Void) ``` |

Modified [NSURLCacheStoragePolicy [enum]](https://developer.apple.com/documentation/foundation/urlcache/storagepolicy)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSURLComponents](https://developer.apple.com/documentation/foundation/nsurlcomponents)

|  | Declaration |
| --- | --- |
| From | ``` class NSURLComponents : NSObject, NSCopying {     init()     init?(URL url: NSURL, resolvingAgainstBaseURL resolve: Bool)     class func componentsWithURL(_ url: NSURL, resolvingAgainstBaseURL resolve: Bool) -> Self?     init?(string URLString: String)     class func componentsWithString(_ URLString: String) -> Self?     @NSCopying var URL: NSURL? { get }     func URLRelativeToURL(_ baseURL: NSURL?) -> NSURL?     var string: String? { get }     var scheme: String?     var user: String?     var password: String?     var host: String?     @NSCopying var port: NSNumber?     var path: String?     var query: String?     var fragment: String?     var percentEncodedUser: String?     var percentEncodedPassword: String?     var percentEncodedHost: String?     var percentEncodedPath: String?     var percentEncodedQuery: String?     var percentEncodedFragment: String?     var queryItems: [AnyObject]? } ``` |
| To | ``` class NSURLComponents : NSObject, NSCopying {     init()     init?(URL url: NSURL, resolvingAgainstBaseURL resolve: Bool)     class func componentsWithURL(_ url: NSURL, resolvingAgainstBaseURL resolve: Bool) -> Self?     init?(string URLString: String)     class func componentsWithString(_ URLString: String) -> Self?     @NSCopying var URL: NSURL? { get }     func URLRelativeToURL(_ baseURL: NSURL?) -> NSURL?     var string: String? { get }     var scheme: String?     var user: String?     var password: String?     var host: String?     @NSCopying var port: NSNumber?     var path: String?     var query: String?     var fragment: String?     var percentEncodedUser: String?     var percentEncodedPassword: String?     var percentEncodedHost: String?     var percentEncodedPath: String?     var percentEncodedQuery: String?     var percentEncodedFragment: String?     var rangeOfScheme: NSRange { get }     var rangeOfUser: NSRange { get }     var rangeOfPassword: NSRange { get }     var rangeOfHost: NSRange { get }     var rangeOfPort: NSRange { get }     var rangeOfPath: NSRange { get }     var rangeOfQuery: NSRange { get }     var rangeOfFragment: NSRange { get }     var queryItems: [NSURLQueryItem]? } ``` |

Modified [NSURLComponents.queryItems](https://developer.apple.com/documentation/foundation/nsurlcomponents/1407752-queryitems)

|  | Declaration |
| --- | --- |
| From | ``` var queryItems: [AnyObject]? ``` |
| To | ``` var queryItems: [NSURLQueryItem]? ``` |

Modified [NSURLConnection](https://developer.apple.com/documentation/foundation/nsurlconnection)

|  | Declaration |
| --- | --- |
| From | ``` class NSURLConnection : NSObject {     init?(request request: NSURLRequest, delegate delegate: AnyObject?, startImmediately startImmediately: Bool)     init?(request request: NSURLRequest, delegate delegate: AnyObject?)     class func connectionWithRequest(_ request: NSURLRequest, delegate delegate: AnyObject?) -> NSURLConnection?     @NSCopying var originalRequest: NSURLRequest { get }     @NSCopying var currentRequest: NSURLRequest { get }     func start()     func cancel()     func scheduleInRunLoop(_ aRunLoop: NSRunLoop, forMode mode: String)     func unscheduleFromRunLoop(_ aRunLoop: NSRunLoop, forMode mode: String)     func setDelegateQueue(_ queue: NSOperationQueue!)     class func canHandleRequest(_ request: NSURLRequest) -> Bool } extension NSURLConnection {     class func sendSynchronousRequest(_ request: NSURLRequest, returningResponse response: AutoreleasingUnsafeMutablePointer<NSURLResponse?>, error error: NSErrorPointer) -> NSData? } extension NSURLConnection {     class func sendAsynchronousRequest(_ request: NSURLRequest, queue queue: NSOperationQueue!, completionHandler handler: (NSURLResponse!, NSData!, NSError!) -> Void) } extension NSURLConnection {     weak var newsstandAssetDownload: NKAssetDownload! { get } } ``` |
| To | ``` class NSURLConnection : NSObject {     init?(request request: NSURLRequest, delegate delegate: AnyObject?, startImmediately startImmediately: Bool)     init?(request request: NSURLRequest, delegate delegate: AnyObject?)     class func connectionWithRequest(_ request: NSURLRequest, delegate delegate: AnyObject?) -> NSURLConnection?     @NSCopying var originalRequest: NSURLRequest { get }     @NSCopying var currentRequest: NSURLRequest { get }     func start()     func cancel()     func scheduleInRunLoop(_ aRunLoop: NSRunLoop, forMode mode: String)     func unscheduleFromRunLoop(_ aRunLoop: NSRunLoop, forMode mode: String)     func setDelegateQueue(_ queue: NSOperationQueue?)     class func canHandleRequest(_ request: NSURLRequest) -> Bool } extension NSURLConnection {     class func sendSynchronousRequest(_ request: NSURLRequest, returningResponse response: AutoreleasingUnsafeMutablePointer<NSURLResponse?>) throws -> NSData } extension NSURLConnection {     class func sendAsynchronousRequest(_ request: NSURLRequest, queue queue: NSOperationQueue, completionHandler handler: (NSURLResponse?, NSData?, NSError?) -> Void) } extension NSURLConnection {     weak var newsstandAssetDownload: NKAssetDownload? { get } } ``` |

Modified [NSURLConnection.init(request: NSURLRequest, delegate: AnyObject?)](https://developer.apple.com/documentation/foundation/nsurlconnection/1414520-init)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [NSURLConnection.init(request: NSURLRequest, delegate: AnyObject?, startImmediately: Bool)](https://developer.apple.com/documentation/foundation/nsurlconnection/1418425-init)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [NSURLConnection.sendAsynchronousRequest(_: NSURLRequest, queue: NSOperationQueue, completionHandler: (NSURLResponse?, NSData?, NSError?) -> Void) [class]](https://developer.apple.com/documentation/foundation/nsurlconnection/1418125-sendasynchronousrequest)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` class func sendAsynchronousRequest(_ request: NSURLRequest, queue queue: NSOperationQueue!, completionHandler handler: (NSURLResponse!, NSData!, NSError!) -> Void) ``` | -- |
| To | ``` class func sendAsynchronousRequest(_ request: NSURLRequest, queue queue: NSOperationQueue, completionHandler handler: (NSURLResponse?, NSData?, NSError?) -> Void) ``` | iOS 9.0 |

Modified [NSURLConnection.sendSynchronousRequest(_: NSURLRequest, returningResponse: AutoreleasingUnsafeMutablePointer<NSURLResponse?>) throws -> NSData [class]](https://developer.apple.com/documentation/foundation/nsurlconnection/1411393-sendsynchronousrequest)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` class func sendSynchronousRequest(_ request: NSURLRequest, returningResponse response: AutoreleasingUnsafeMutablePointer<NSURLResponse?>, error error: NSErrorPointer) -> NSData? ``` | iOS 8.0 | -- |
| To | ``` class func sendSynchronousRequest(_ request: NSURLRequest, returningResponse response: AutoreleasingUnsafeMutablePointer<NSURLResponse?>) throws -> NSData ``` | iOS 2.0 | iOS 9.0 |

Modified [NSURLConnection.setDelegateQueue(_: NSOperationQueue?)](https://developer.apple.com/documentation/foundation/nsurlconnection/1411849-setdelegatequeue)

|  | Declaration |
| --- | --- |
| From | ``` func setDelegateQueue(_ queue: NSOperationQueue!) ``` |
| To | ``` func setDelegateQueue(_ queue: NSOperationQueue?) ``` |

Modified [NSURLCredential](https://developer.apple.com/documentation/foundation/nsurlcredential)

|  | Declaration |
| --- | --- |
| From | ``` class NSURLCredential : NSObject, NSSecureCoding, NSCoding, NSCopying {     var persistence: NSURLCredentialPersistence { get } } extension NSURLCredential {     init(user user: String, password password: String, persistence persistence: NSURLCredentialPersistence)     class func credentialWithUser(_ user: String, password password: String, persistence persistence: NSURLCredentialPersistence) -> NSURLCredential     var user: String? { get }     var password: String? { get }     var hasPassword: Bool { get } } extension NSURLCredential {     init(identity identity: SecIdentity, certificates certArray: [AnyObject], persistence persistence: NSURLCredentialPersistence)     class func credentialWithIdentity(_ identity: SecIdentity, certificates certArray: [AnyObject], persistence persistence: NSURLCredentialPersistence) -> NSURLCredential     var identity: SecIdentity? { get }     var certificates: [AnyObject] { get } } extension NSURLCredential {     init(trust trust: SecTrust!)     init(forTrust trust: SecTrust!) -> NSURLCredential     class func credentialForTrust(_ trust: SecTrust!) -> NSURLCredential } ``` |
| To | ``` class NSURLCredential : NSObject, NSSecureCoding, NSCoding, NSCopying {     var persistence: NSURLCredentialPersistence { get } } extension NSURLCredential {     init(user user: String, password password: String, persistence persistence: NSURLCredentialPersistence)     class func credentialWithUser(_ user: String, password password: String, persistence persistence: NSURLCredentialPersistence) -> NSURLCredential     var user: String? { get }     var password: String? { get }     var hasPassword: Bool { get } } extension NSURLCredential {     init(identity identity: SecIdentity, certificates certArray: [AnyObject]?, persistence persistence: NSURLCredentialPersistence)     class func credentialWithIdentity(_ identity: SecIdentity, certificates certArray: [AnyObject]?, persistence persistence: NSURLCredentialPersistence) -> NSURLCredential     var identity: SecIdentity? { get }     var certificates: [AnyObject] { get } } extension NSURLCredential {     init(trust trust: SecTrust)      init(forTrust trust: SecTrust)     class func credentialForTrust(_ trust: SecTrust) -> NSURLCredential } ``` |

Modified [NSURLCredential.init(forTrust: SecTrust)](https://developer.apple.com/documentation/foundation/nsurlcredential/1407330-credentialfortrust)

|  | Declaration |
| --- | --- |
| From | ``` init(forTrust trust: SecTrust!) -> NSURLCredential ``` |
| To | ``` init(forTrust trust: SecTrust) ``` |

Modified [NSURLCredential.init(identity: SecIdentity, certificates: [AnyObject]?, persistence: NSURLCredentialPersistence)](https://developer.apple.com/documentation/foundation/nsurlcredential/1418121-initwithidentity)

|  | Declaration |
| --- | --- |
| From | ``` init(identity identity: SecIdentity, certificates certArray: [AnyObject], persistence persistence: NSURLCredentialPersistence) ``` |
| To | ``` init(identity identity: SecIdentity, certificates certArray: [AnyObject]?, persistence persistence: NSURLCredentialPersistence) ``` |

Modified [NSURLCredential.init(trust: SecTrust)](https://developer.apple.com/documentation/foundation/nsurlcredential/1413935-initwithtrust)

|  | Declaration |
| --- | --- |
| From | ``` init(trust trust: SecTrust!) ``` |
| To | ``` init(trust trust: SecTrust) ``` |

Modified [NSURLCredentialPersistence [enum]](https://developer.apple.com/documentation/foundation/urlcredential/persistence)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSURLCredentialStorage](https://developer.apple.com/documentation/foundation/urlcredentialstorage)

|  | Declaration |
| --- | --- |
| From | ``` class NSURLCredentialStorage : NSObject {     class func sharedCredentialStorage() -> NSURLCredentialStorage     func credentialsForProtectionSpace(_ space: NSURLProtectionSpace) -> [NSObject : AnyObject]?     var allCredentials: [NSObject : AnyObject] { get }     func setCredential(_ credential: NSURLCredential, forProtectionSpace space: NSURLProtectionSpace)     func removeCredential(_ credential: NSURLCredential, forProtectionSpace space: NSURLProtectionSpace)     func removeCredential(_ credential: NSURLCredential, forProtectionSpace space: NSURLProtectionSpace, options options: [NSObject : AnyObject]?)     func defaultCredentialForProtectionSpace(_ space: NSURLProtectionSpace) -> NSURLCredential?     func setDefaultCredential(_ credential: NSURLCredential, forProtectionSpace space: NSURLProtectionSpace) } extension NSURLCredentialStorage {     func getCredentialsForProtectionSpace(_ protectionSpace: NSURLProtectionSpace, task task: NSURLSessionTask?, completionHandler completionHandler: (([NSObject : AnyObject]!) -> Void)!)     func setCredential(_ credential: NSURLCredential, forProtectionSpace protectionSpace: NSURLProtectionSpace, task task: NSURLSessionTask)     func removeCredential(_ credential: NSURLCredential, forProtectionSpace protectionSpace: NSURLProtectionSpace, options options: [NSObject : AnyObject]?, task task: NSURLSessionTask?)     func getDefaultCredentialForProtectionSpace(_ space: NSURLProtectionSpace, task task: NSURLSessionTask?, completionHandler completionHandler: ((NSURLCredential!) -> Void)!)     func setDefaultCredential(_ credential: NSURLCredential, forProtectionSpace protectionSpace: NSURLProtectionSpace, task task: NSURLSessionTask) } ``` |
| To | ``` class NSURLCredentialStorage : NSObject {     class func sharedCredentialStorage() -> NSURLCredentialStorage     func credentialsForProtectionSpace(_ space: NSURLProtectionSpace) -> [String : NSURLCredential]?     var allCredentials: [NSURLProtectionSpace : [String : NSURLCredential]] { get }     func setCredential(_ credential: NSURLCredential, forProtectionSpace space: NSURLProtectionSpace)     func removeCredential(_ credential: NSURLCredential, forProtectionSpace space: NSURLProtectionSpace)     func removeCredential(_ credential: NSURLCredential, forProtectionSpace space: NSURLProtectionSpace, options options: [String : AnyObject]?)     func defaultCredentialForProtectionSpace(_ space: NSURLProtectionSpace) -> NSURLCredential?     func setDefaultCredential(_ credential: NSURLCredential, forProtectionSpace space: NSURLProtectionSpace) } extension NSURLCredentialStorage {     func getCredentialsForProtectionSpace(_ protectionSpace: NSURLProtectionSpace, task task: NSURLSessionTask, completionHandler completionHandler: ([String : NSURLCredential]?) -> Void)     func setCredential(_ credential: NSURLCredential, forProtectionSpace protectionSpace: NSURLProtectionSpace, task task: NSURLSessionTask)     func removeCredential(_ credential: NSURLCredential, forProtectionSpace protectionSpace: NSURLProtectionSpace, options options: [String : AnyObject]?, task task: NSURLSessionTask)     func getDefaultCredentialForProtectionSpace(_ space: NSURLProtectionSpace, task task: NSURLSessionTask, completionHandler completionHandler: (NSURLCredential?) -> Void)     func setDefaultCredential(_ credential: NSURLCredential, forProtectionSpace protectionSpace: NSURLProtectionSpace, task task: NSURLSessionTask) } ``` |

Modified [NSURLCredentialStorage.allCredentials](https://developer.apple.com/documentation/foundation/urlcredentialstorage/1413859-allcredentials)

|  | Declaration |
| --- | --- |
| From | ``` var allCredentials: [NSObject : AnyObject] { get } ``` |
| To | ``` var allCredentials: [NSURLProtectionSpace : [String : NSURLCredential]] { get } ``` |

Modified [NSURLCredentialStorage.credentialsForProtectionSpace(_: NSURLProtectionSpace) -> [String : NSURLCredential]?](https://developer.apple.com/documentation/foundation/urlcredentialstorage/1413910-credentials)

|  | Declaration |
| --- | --- |
| From | ``` func credentialsForProtectionSpace(_ space: NSURLProtectionSpace) -> [NSObject : AnyObject]? ``` |
| To | ``` func credentialsForProtectionSpace(_ space: NSURLProtectionSpace) -> [String : NSURLCredential]? ``` |

Modified [NSURLCredentialStorage.getCredentialsForProtectionSpace(_: NSURLProtectionSpace, task: NSURLSessionTask, completionHandler: ([String : NSURLCredential]?) -> Void)](https://developer.apple.com/documentation/foundation/urlcredentialstorage/1418119-getcredentials)

|  | Declaration |
| --- | --- |
| From | ``` func getCredentialsForProtectionSpace(_ protectionSpace: NSURLProtectionSpace, task task: NSURLSessionTask?, completionHandler completionHandler: (([NSObject : AnyObject]!) -> Void)!) ``` |
| To | ``` func getCredentialsForProtectionSpace(_ protectionSpace: NSURLProtectionSpace, task task: NSURLSessionTask, completionHandler completionHandler: ([String : NSURLCredential]?) -> Void) ``` |

Modified [NSURLCredentialStorage.getDefaultCredentialForProtectionSpace(_: NSURLProtectionSpace, task: NSURLSessionTask, completionHandler: (NSURLCredential?) -> Void)](https://developer.apple.com/documentation/foundation/urlcredentialstorage/1411794-getdefaultcredential)

|  | Declaration |
| --- | --- |
| From | ``` func getDefaultCredentialForProtectionSpace(_ space: NSURLProtectionSpace, task task: NSURLSessionTask?, completionHandler completionHandler: ((NSURLCredential!) -> Void)!) ``` |
| To | ``` func getDefaultCredentialForProtectionSpace(_ space: NSURLProtectionSpace, task task: NSURLSessionTask, completionHandler completionHandler: (NSURLCredential?) -> Void) ``` |

Modified [NSURLCredentialStorage.removeCredential(_: NSURLCredential, forProtectionSpace: NSURLProtectionSpace, options: [String : AnyObject]?)](https://developer.apple.com/documentation/foundation/nsurlcredentialstorage/1407695-removecredential)

|  | Declaration |
| --- | --- |
| From | ``` func removeCredential(_ credential: NSURLCredential, forProtectionSpace space: NSURLProtectionSpace, options options: [NSObject : AnyObject]?) ``` |
| To | ``` func removeCredential(_ credential: NSURLCredential, forProtectionSpace space: NSURLProtectionSpace, options options: [String : AnyObject]?) ``` |

Modified [NSURLCredentialStorage.removeCredential(_: NSURLCredential, forProtectionSpace: NSURLProtectionSpace, options: [String : AnyObject]?, task: NSURLSessionTask)](https://developer.apple.com/documentation/foundation/nsurlcredentialstorage/1407237-removecredential)

|  | Declaration |
| --- | --- |
| From | ``` func removeCredential(_ credential: NSURLCredential, forProtectionSpace protectionSpace: NSURLProtectionSpace, options options: [NSObject : AnyObject]?, task task: NSURLSessionTask?) ``` |
| To | ``` func removeCredential(_ credential: NSURLCredential, forProtectionSpace protectionSpace: NSURLProtectionSpace, options options: [String : AnyObject]?, task task: NSURLSessionTask) ``` |

Modified [NSURLProtectionSpace](https://developer.apple.com/documentation/foundation/nsurlprotectionspace)

|  | Declaration |
| --- | --- |
| From | ``` class NSURLProtectionSpace : NSObject, NSSecureCoding, NSCoding, NSCopying {     init(host host: String, port port: Int, `protocol` `protocol`: String?, realm realm: String?, authenticationMethod authenticationMethod: String?)     init(proxyHost host: String, port port: Int, type type: String?, realm realm: String?, authenticationMethod authenticationMethod: String?)     var realm: String? { get }     var receivesCredentialSecurely: Bool { get }     var host: String { get }     var port: Int { get }     var proxyType: String? { get }     var `protocol`: String? { get }     var authenticationMethod: String? { get }     func isProxy() -> Bool } extension NSURLProtectionSpace {     var distinguishedNames: [AnyObject]? { get } } extension NSURLProtectionSpace {     var serverTrust: SecTrust? { get } } ``` |
| To | ``` class NSURLProtectionSpace : NSObject, NSSecureCoding, NSCoding, NSCopying {     init(host host: String, port port: Int, `protocol` `protocol`: String?, realm realm: String?, authenticationMethod authenticationMethod: String?)     init(proxyHost host: String, port port: Int, type type: String?, realm realm: String?, authenticationMethod authenticationMethod: String?)     var realm: String? { get }     var receivesCredentialSecurely: Bool { get }     var host: String { get }     var port: Int { get }     var proxyType: String? { get }     var `protocol`: String? { get }     var authenticationMethod: String { get }     func isProxy() -> Bool } extension NSURLProtectionSpace {     var distinguishedNames: [NSData]? { get } } extension NSURLProtectionSpace {     var serverTrust: SecTrust? { get } } ``` |

Modified [NSURLProtectionSpace.authenticationMethod](https://developer.apple.com/documentation/foundation/nsurlprotectionspace/1415028-authenticationmethod)

|  | Declaration |
| --- | --- |
| From | ``` var authenticationMethod: String? { get } ``` |
| To | ``` var authenticationMethod: String { get } ``` |

Modified [NSURLProtectionSpace.distinguishedNames](https://developer.apple.com/documentation/foundation/urlprotectionspace/1417061-distinguishednames)

|  | Declaration |
| --- | --- |
| From | ``` var distinguishedNames: [AnyObject]? { get } ``` |
| To | ``` var distinguishedNames: [NSData]? { get } ``` |

Modified [NSURLQueryItem](https://developer.apple.com/documentation/foundation/nsurlqueryitem)

|  | Declaration |
| --- | --- |
| From | ``` class NSURLQueryItem : NSObject, NSSecureCoding, NSCoding, NSCopying {     init(name name: String, value value: String)     class func queryItemWithName(_ name: String, value value: String) -> Self     var name: String { get }     var value: String? { get } } ``` |
| To | ``` class NSURLQueryItem : NSObject, NSSecureCoding, NSCoding, NSCopying {     init(name name: String, value value: String?)     class func queryItemWithName(_ name: String, value value: String?) -> Self     var name: String { get }     var value: String? { get } } ``` |

Modified [NSURLQueryItem.init(name: String, value: String?)](https://developer.apple.com/documentation/foundation/nsurlqueryitem/1410963-init)

|  | Declaration |
| --- | --- |
| From | ``` init(name name: String, value value: String) ``` |
| To | ``` init(name name: String, value value: String?) ``` |

Modified [NSURLRelationship [enum]](https://developer.apple.com/documentation/foundation/nsurlrelationship)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NSURLRequest](https://developer.apple.com/documentation/foundation/nsurlrequest)

|  | Declaration |
| --- | --- |
| From | ``` class NSURLRequest : NSObject, NSSecureCoding, NSCoding, NSCopying, NSMutableCopying {     convenience init(URL URL: NSURL)     class func requestWithURL(_ URL: NSURL) -> Self     class func supportsSecureCoding() -> Bool     convenience init(URL URL: NSURL, cachePolicy cachePolicy: NSURLRequestCachePolicy, timeoutInterval timeoutInterval: NSTimeInterval)     class func requestWithURL(_ URL: NSURL, cachePolicy cachePolicy: NSURLRequestCachePolicy, timeoutInterval timeoutInterval: NSTimeInterval) -> Self     convenience init(URL URL: NSURL)     init(URL URL: NSURL, cachePolicy cachePolicy: NSURLRequestCachePolicy, timeoutInterval timeoutInterval: NSTimeInterval)     @NSCopying var URL: NSURL? { get }     var cachePolicy: NSURLRequestCachePolicy { get }     var timeoutInterval: NSTimeInterval { get }     @NSCopying var mainDocumentURL: NSURL? { get }     var networkServiceType: NSURLRequestNetworkServiceType { get }     var allowsCellularAccess: Bool { get } } extension NSURLRequest {     var HTTPMethod: String? { get }     var allHTTPHeaderFields: [NSObject : AnyObject]? { get }     func valueForHTTPHeaderField(_ field: String) -> String?     @NSCopying var HTTPBody: NSData? { get }     var HTTPBodyStream: NSInputStream? { get }     var HTTPShouldHandleCookies: Bool { get }     var HTTPShouldUsePipelining: Bool { get } } ``` |
| To | ``` class NSURLRequest : NSObject, NSSecureCoding, NSCoding, NSCopying, NSMutableCopying {     convenience init(URL URL: NSURL)     class func requestWithURL(_ URL: NSURL) -> Self     class func supportsSecureCoding() -> Bool     convenience init(URL URL: NSURL, cachePolicy cachePolicy: NSURLRequestCachePolicy, timeoutInterval timeoutInterval: NSTimeInterval)     class func requestWithURL(_ URL: NSURL, cachePolicy cachePolicy: NSURLRequestCachePolicy, timeoutInterval timeoutInterval: NSTimeInterval) -> Self     convenience init(URL URL: NSURL)     init(URL URL: NSURL, cachePolicy cachePolicy: NSURLRequestCachePolicy, timeoutInterval timeoutInterval: NSTimeInterval)     @NSCopying var URL: NSURL? { get }     var cachePolicy: NSURLRequestCachePolicy { get }     var timeoutInterval: NSTimeInterval { get }     @NSCopying var mainDocumentURL: NSURL? { get }     var networkServiceType: NSURLRequestNetworkServiceType { get }     var allowsCellularAccess: Bool { get } } extension NSURLRequest {     var HTTPMethod: String? { get }     var allHTTPHeaderFields: [String : String]? { get }     func valueForHTTPHeaderField(_ field: String) -> String?     @NSCopying var HTTPBody: NSData? { get }     var HTTPBodyStream: NSInputStream? { get }     var HTTPShouldHandleCookies: Bool { get }     var HTTPShouldUsePipelining: Bool { get } } ``` |

Modified [NSURLRequest.allHTTPHeaderFields](https://developer.apple.com/documentation/foundation/nsurlrequest/1418477-allhttpheaderfields)

|  | Declaration |
| --- | --- |
| From | ``` var allHTTPHeaderFields: [NSObject : AnyObject]? { get } ``` |
| To | ``` var allHTTPHeaderFields: [String : String]? { get } ``` |

Modified [NSURLRequestCachePolicy [enum]](https://developer.apple.com/documentation/foundation/nsurlrequest/cachepolicy)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum NSURLRequestCachePolicy : UInt {     case UseProtocolCachePolicy     case ReloadIgnoringLocalCacheData     case ReloadIgnoringLocalAndRemoteCacheData     case ReturnCacheDataElseLoad     case ReturnCacheDataDontLoad     case ReloadRevalidatingCacheData } ``` | -- |
| To | ``` enum NSURLRequestCachePolicy : UInt {     case UseProtocolCachePolicy     case ReloadIgnoringLocalCacheData     case ReloadIgnoringLocalAndRemoteCacheData     static var ReloadIgnoringCacheData: NSURLRequestCachePolicy { get }     case ReturnCacheDataElseLoad     case ReturnCacheDataDontLoad     case ReloadRevalidatingCacheData } ``` | UInt |

Modified [NSURLRequestNetworkServiceType [enum]](https://developer.apple.com/documentation/foundation/nsurlrequest/networkservicetype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSURLSession](https://developer.apple.com/documentation/foundation/nsurlsession)

|  | Declaration |
| --- | --- |
| From | ``` class NSURLSession : NSObject {     class func sharedSession() -> NSURLSession     init(configuration configuration: NSURLSessionConfiguration) -> NSURLSession     class func sessionWithConfiguration(_ configuration: NSURLSessionConfiguration) -> NSURLSession     init(configuration configuration: NSURLSessionConfiguration?, delegate delegate: NSURLSessionDelegate?, delegateQueue queue: NSOperationQueue?) -> NSURLSession     class func sessionWithConfiguration(_ configuration: NSURLSessionConfiguration?, delegate delegate: NSURLSessionDelegate?, delegateQueue queue: NSOperationQueue?) -> NSURLSession     var delegateQueue: NSOperationQueue { get }     var delegate: NSURLSessionDelegate? { get }     @NSCopying var configuration: NSURLSessionConfiguration { get }     var sessionDescription: String?     func finishTasksAndInvalidate()     func invalidateAndCancel()     func resetWithCompletionHandler(_ completionHandler: () -> Void)     func flushWithCompletionHandler(_ completionHandler: () -> Void)     func getTasksWithCompletionHandler(_ completionHandler: ([AnyObject]!, [AnyObject]!, [AnyObject]!) -> Void)     func dataTaskWithRequest(_ request: NSURLRequest) -> NSURLSessionDataTask     func dataTaskWithURL(_ url: NSURL) -> NSURLSessionDataTask     func uploadTaskWithRequest(_ request: NSURLRequest, fromFile fileURL: NSURL) -> NSURLSessionUploadTask     func uploadTaskWithRequest(_ request: NSURLRequest, fromData bodyData: NSData?) -> NSURLSessionUploadTask     func uploadTaskWithStreamedRequest(_ request: NSURLRequest) -> NSURLSessionUploadTask     func downloadTaskWithRequest(_ request: NSURLRequest) -> NSURLSessionDownloadTask     func downloadTaskWithURL(_ url: NSURL) -> NSURLSessionDownloadTask     func downloadTaskWithResumeData(_ resumeData: NSData) -> NSURLSessionDownloadTask } extension NSURLSession {     func dataTaskWithRequest(_ request: NSURLRequest, completionHandler completionHandler: ((NSData!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionDataTask     func dataTaskWithURL(_ url: NSURL, completionHandler completionHandler: ((NSData!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionDataTask     func uploadTaskWithRequest(_ request: NSURLRequest, fromFile fileURL: NSURL, completionHandler completionHandler: ((NSData!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionUploadTask     func uploadTaskWithRequest(_ request: NSURLRequest, fromData bodyData: NSData?, completionHandler completionHandler: ((NSData!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionUploadTask     func downloadTaskWithRequest(_ request: NSURLRequest, completionHandler completionHandler: ((NSURL!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionDownloadTask     func downloadTaskWithURL(_ url: NSURL, completionHandler completionHandler: ((NSURL!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionDownloadTask     func downloadTaskWithResumeData(_ resumeData: NSData, completionHandler completionHandler: ((NSURL!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionDownloadTask } extension NSURLSession {     func dataTaskWithHTTPGetRequest(_ url: NSURL!) -> NSURLSessionDataTask!     func dataTaskWithHTTPGetRequest(_ url: NSURL!, completionHandler completionHandler: ((NSData!, NSURLResponse!, NSError!) -> Void)!) -> NSURLSessionDataTask! } ``` |
| To | ``` class NSURLSession : NSObject {     class func sharedSession() -> NSURLSession      init(configuration configuration: NSURLSessionConfiguration)     class func sessionWithConfiguration(_ configuration: NSURLSessionConfiguration) -> NSURLSession      init(configuration configuration: NSURLSessionConfiguration, delegate delegate: NSURLSessionDelegate?, delegateQueue queue: NSOperationQueue?)     class func sessionWithConfiguration(_ configuration: NSURLSessionConfiguration, delegate delegate: NSURLSessionDelegate?, delegateQueue queue: NSOperationQueue?) -> NSURLSession     var delegateQueue: NSOperationQueue { get }     var delegate: NSURLSessionDelegate? { get }     @NSCopying var configuration: NSURLSessionConfiguration { get }     var sessionDescription: String?     func finishTasksAndInvalidate()     func invalidateAndCancel()     func resetWithCompletionHandler(_ completionHandler: () -> Void)     func flushWithCompletionHandler(_ completionHandler: () -> Void)     func getTasksWithCompletionHandler(_ completionHandler: ([NSURLSessionDataTask], [NSURLSessionUploadTask], [NSURLSessionDownloadTask]) -> Void)     func getAllTasksWithCompletionHandler(_ completionHandler: ([NSURLSessionTask]) -> Void)     func dataTaskWithRequest(_ request: NSURLRequest) -> NSURLSessionDataTask     func dataTaskWithURL(_ url: NSURL) -> NSURLSessionDataTask     func uploadTaskWithRequest(_ request: NSURLRequest, fromFile fileURL: NSURL) -> NSURLSessionUploadTask     func uploadTaskWithRequest(_ request: NSURLRequest, fromData bodyData: NSData) -> NSURLSessionUploadTask     func uploadTaskWithStreamedRequest(_ request: NSURLRequest) -> NSURLSessionUploadTask     func downloadTaskWithRequest(_ request: NSURLRequest) -> NSURLSessionDownloadTask     func downloadTaskWithURL(_ url: NSURL) -> NSURLSessionDownloadTask     func downloadTaskWithResumeData(_ resumeData: NSData) -> NSURLSessionDownloadTask     func streamTaskWithHostName(_ hostname: String, port port: Int) -> NSURLSessionStreamTask     func streamTaskWithNetService(_ service: NSNetService) -> NSURLSessionStreamTask } extension NSURLSession {     func dataTaskWithRequest(_ request: NSURLRequest, completionHandler completionHandler: (NSData?, NSURLResponse?, NSError?) -> Void) -> NSURLSessionDataTask     func dataTaskWithURL(_ url: NSURL, completionHandler completionHandler: (NSData?, NSURLResponse?, NSError?) -> Void) -> NSURLSessionDataTask     func uploadTaskWithRequest(_ request: NSURLRequest, fromFile fileURL: NSURL, completionHandler completionHandler: (NSData?, NSURLResponse?, NSError?) -> Void) -> NSURLSessionUploadTask     func uploadTaskWithRequest(_ request: NSURLRequest, fromData bodyData: NSData?, completionHandler completionHandler: (NSData?, NSURLResponse?, NSError?) -> Void) -> NSURLSessionUploadTask     func downloadTaskWithRequest(_ request: NSURLRequest, completionHandler completionHandler: (NSURL?, NSURLResponse?, NSError?) -> Void) -> NSURLSessionDownloadTask     func downloadTaskWithURL(_ url: NSURL, completionHandler completionHandler: (NSURL?, NSURLResponse?, NSError?) -> Void) -> NSURLSessionDownloadTask     func downloadTaskWithResumeData(_ resumeData: NSData, completionHandler completionHandler: (NSURL?, NSURLResponse?, NSError?) -> Void) -> NSURLSessionDownloadTask } ``` |

Modified [NSURLSession.dataTaskWithRequest(_: NSURLRequest, completionHandler: (NSData?, NSURLResponse?, NSError?) -> Void) -> NSURLSessionDataTask](https://developer.apple.com/documentation/foundation/nsurlsession/1407613-datataskwithrequest)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func dataTaskWithRequest(_ request: NSURLRequest, completionHandler completionHandler: ((NSData!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionDataTask ``` | iOS 7.0 |
| To | ``` func dataTaskWithRequest(_ request: NSURLRequest, completionHandler completionHandler: (NSData?, NSURLResponse?, NSError?) -> Void) -> NSURLSessionDataTask ``` | iOS 8.0 |

Modified [NSURLSession.dataTaskWithURL(_: NSURL, completionHandler: (NSData?, NSURLResponse?, NSError?) -> Void) -> NSURLSessionDataTask](https://developer.apple.com/documentation/foundation/urlsession/1410330-datatask)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func dataTaskWithURL(_ url: NSURL, completionHandler completionHandler: ((NSData!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionDataTask ``` | iOS 7.0 |
| To | ``` func dataTaskWithURL(_ url: NSURL, completionHandler completionHandler: (NSData?, NSURLResponse?, NSError?) -> Void) -> NSURLSessionDataTask ``` | iOS 8.0 |

Modified [NSURLSession.downloadTaskWithRequest(_: NSURLRequest, completionHandler: (NSURL?, NSURLResponse?, NSError?) -> Void) -> NSURLSessionDownloadTask](https://developer.apple.com/documentation/foundation/urlsession/1411511-downloadtask)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func downloadTaskWithRequest(_ request: NSURLRequest, completionHandler completionHandler: ((NSURL!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionDownloadTask ``` | iOS 7.0 |
| To | ``` func downloadTaskWithRequest(_ request: NSURLRequest, completionHandler completionHandler: (NSURL?, NSURLResponse?, NSError?) -> Void) -> NSURLSessionDownloadTask ``` | iOS 8.0 |

Modified [NSURLSession.downloadTaskWithResumeData(_: NSData, completionHandler: (NSURL?, NSURLResponse?, NSError?) -> Void) -> NSURLSessionDownloadTask](https://developer.apple.com/documentation/foundation/nsurlsession/1411598-downloadtaskwithresumedata)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func downloadTaskWithResumeData(_ resumeData: NSData, completionHandler completionHandler: ((NSURL!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionDownloadTask ``` | iOS 7.0 |
| To | ``` func downloadTaskWithResumeData(_ resumeData: NSData, completionHandler completionHandler: (NSURL?, NSURLResponse?, NSError?) -> Void) -> NSURLSessionDownloadTask ``` | iOS 8.0 |

Modified [NSURLSession.downloadTaskWithURL(_: NSURL, completionHandler: (NSURL?, NSURLResponse?, NSError?) -> Void) -> NSURLSessionDownloadTask](https://developer.apple.com/documentation/foundation/urlsession/1411608-downloadtask)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func downloadTaskWithURL(_ url: NSURL, completionHandler completionHandler: ((NSURL!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionDownloadTask ``` | iOS 7.0 |
| To | ``` func downloadTaskWithURL(_ url: NSURL, completionHandler completionHandler: (NSURL?, NSURLResponse?, NSError?) -> Void) -> NSURLSessionDownloadTask ``` | iOS 8.0 |

Modified [NSURLSession.getTasksWithCompletionHandler(_: ([NSURLSessionDataTask], [NSURLSessionUploadTask], [NSURLSessionDownloadTask]) -> Void)](https://developer.apple.com/documentation/foundation/nsurlsession/1411578-gettaskswithcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` func getTasksWithCompletionHandler(_ completionHandler: ([AnyObject]!, [AnyObject]!, [AnyObject]!) -> Void) ``` |
| To | ``` func getTasksWithCompletionHandler(_ completionHandler: ([NSURLSessionDataTask], [NSURLSessionUploadTask], [NSURLSessionDownloadTask]) -> Void) ``` |

Modified [NSURLSession.init(configuration: NSURLSessionConfiguration)](https://developer.apple.com/documentation/foundation/nsurlsession/1411474-sessionwithconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` init(configuration configuration: NSURLSessionConfiguration) -> NSURLSession ``` |
| To | ``` init(configuration configuration: NSURLSessionConfiguration) ``` |

Modified [NSURLSession.init(configuration: NSURLSessionConfiguration, delegate: NSURLSessionDelegate?, delegateQueue: NSOperationQueue?)](https://developer.apple.com/documentation/foundation/nsurlsession/1411597-sessionwithconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` init(configuration configuration: NSURLSessionConfiguration?, delegate delegate: NSURLSessionDelegate?, delegateQueue queue: NSOperationQueue?) -> NSURLSession ``` |
| To | ``` init(configuration configuration: NSURLSessionConfiguration, delegate delegate: NSURLSessionDelegate?, delegateQueue queue: NSOperationQueue?) ``` |

Modified [NSURLSession.uploadTaskWithRequest(_: NSURLRequest, fromData: NSData) -> NSURLSessionUploadTask](https://developer.apple.com/documentation/foundation/urlsession/1409763-uploadtask)

|  | Declaration |
| --- | --- |
| From | ``` func uploadTaskWithRequest(_ request: NSURLRequest, fromData bodyData: NSData?) -> NSURLSessionUploadTask ``` |
| To | ``` func uploadTaskWithRequest(_ request: NSURLRequest, fromData bodyData: NSData) -> NSURLSessionUploadTask ``` |

Modified [NSURLSession.uploadTaskWithRequest(_: NSURLRequest, fromData: NSData?, completionHandler: (NSData?, NSURLResponse?, NSError?) -> Void) -> NSURLSessionUploadTask](https://developer.apple.com/documentation/foundation/nsurlsession/1411518-uploadtaskwithrequest)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func uploadTaskWithRequest(_ request: NSURLRequest, fromData bodyData: NSData?, completionHandler completionHandler: ((NSData!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionUploadTask ``` | iOS 7.0 |
| To | ``` func uploadTaskWithRequest(_ request: NSURLRequest, fromData bodyData: NSData?, completionHandler completionHandler: (NSData?, NSURLResponse?, NSError?) -> Void) -> NSURLSessionUploadTask ``` | iOS 8.0 |

Modified [NSURLSession.uploadTaskWithRequest(_: NSURLRequest, fromFile: NSURL, completionHandler: (NSData?, NSURLResponse?, NSError?) -> Void) -> NSURLSessionUploadTask](https://developer.apple.com/documentation/foundation/urlsession/1411638-uploadtask)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func uploadTaskWithRequest(_ request: NSURLRequest, fromFile fileURL: NSURL, completionHandler completionHandler: ((NSData!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionUploadTask ``` | iOS 7.0 |
| To | ``` func uploadTaskWithRequest(_ request: NSURLRequest, fromFile fileURL: NSURL, completionHandler completionHandler: (NSData?, NSURLResponse?, NSError?) -> Void) -> NSURLSessionUploadTask ``` | iOS 8.0 |

Modified [NSURLSessionAuthChallengeDisposition [enum]](https://developer.apple.com/documentation/foundation/urlsession/authchallengedisposition)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NSURLSessionConfiguration](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` class NSURLSessionConfiguration : NSObject, NSCopying {     class func defaultSessionConfiguration() -> NSURLSessionConfiguration     class func ephemeralSessionConfiguration() -> NSURLSessionConfiguration     class func backgroundSessionConfigurationWithIdentifier(_ identifier: String) -> NSURLSessionConfiguration     var identifier: String { get }     var requestCachePolicy: NSURLRequestCachePolicy     var timeoutIntervalForRequest: NSTimeInterval     var timeoutIntervalForResource: NSTimeInterval     var networkServiceType: NSURLRequestNetworkServiceType     var allowsCellularAccess: Bool     var discretionary: Bool     var sharedContainerIdentifier: String?     var sessionSendsLaunchEvents: Bool     var connectionProxyDictionary: [NSObject : AnyObject]?     var TLSMinimumSupportedProtocol: SSLProtocol     var TLSMaximumSupportedProtocol: SSLProtocol     var HTTPShouldUsePipelining: Bool     var HTTPShouldSetCookies: Bool     var HTTPCookieAcceptPolicy: NSHTTPCookieAcceptPolicy     var HTTPAdditionalHeaders: [NSObject : AnyObject]?     var HTTPMaximumConnectionsPerHost: Int     var HTTPCookieStorage: NSHTTPCookieStorage?     var URLCredentialStorage: NSURLCredentialStorage?     var URLCache: NSURLCache?     var protocolClasses: [AnyObject]? } extension NSURLSessionConfiguration {     class func backgroundSessionConfiguration(_ identifier: String) -> NSURLSessionConfiguration } ``` |
| To | ``` class NSURLSessionConfiguration : NSObject, NSCopying {     class func defaultSessionConfiguration() -> NSURLSessionConfiguration     class func ephemeralSessionConfiguration() -> NSURLSessionConfiguration     class func backgroundSessionConfigurationWithIdentifier(_ identifier: String) -> NSURLSessionConfiguration     var identifier: String? { get }     var requestCachePolicy: NSURLRequestCachePolicy     var timeoutIntervalForRequest: NSTimeInterval     var timeoutIntervalForResource: NSTimeInterval     var networkServiceType: NSURLRequestNetworkServiceType     var allowsCellularAccess: Bool     var discretionary: Bool     var sharedContainerIdentifier: String?     var sessionSendsLaunchEvents: Bool     var connectionProxyDictionary: [NSObject : AnyObject]?     var TLSMinimumSupportedProtocol: SSLProtocol     var TLSMaximumSupportedProtocol: SSLProtocol     var HTTPShouldUsePipelining: Bool     var HTTPShouldSetCookies: Bool     var HTTPCookieAcceptPolicy: NSHTTPCookieAcceptPolicy     var HTTPAdditionalHeaders: [NSObject : AnyObject]?     var HTTPMaximumConnectionsPerHost: Int     var HTTPCookieStorage: NSHTTPCookieStorage?     var URLCredentialStorage: NSURLCredentialStorage?     var URLCache: NSURLCache?     var shouldUseExtendedBackgroundIdleMode: Bool     var protocolClasses: [AnyClass]? } extension NSURLSessionConfiguration {     class func backgroundSessionConfiguration(_ identifier: String) -> NSURLSessionConfiguration } ``` |

Modified [NSURLSessionConfiguration.identifier](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1408987-identifier)

|  | Declaration |
| --- | --- |
| From | ``` var identifier: String { get } ``` |
| To | ``` var identifier: String? { get } ``` |

Modified [NSURLSessionConfiguration.protocolClasses](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1411050-protocolclasses)

|  | Declaration |
| --- | --- |
| From | ``` var protocolClasses: [AnyObject]? ``` |
| To | ``` var protocolClasses: [AnyClass]? ``` |

Modified [NSURLSessionDataDelegate](https://developer.apple.com/documentation/foundation/urlsessiondatadelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol NSURLSessionDataDelegate : NSURLSessionTaskDelegate, NSURLSessionDelegate, NSObjectProtocol {     optional func URLSession(_ session: NSURLSession, dataTask dataTask: NSURLSessionDataTask, didReceiveResponse response: NSURLResponse, completionHandler completionHandler: (NSURLSessionResponseDisposition) -> Void)     optional func URLSession(_ session: NSURLSession, dataTask dataTask: NSURLSessionDataTask, didBecomeDownloadTask downloadTask: NSURLSessionDownloadTask)     optional func URLSession(_ session: NSURLSession, dataTask dataTask: NSURLSessionDataTask, didReceiveData data: NSData)     optional func URLSession(_ session: NSURLSession, dataTask dataTask: NSURLSessionDataTask, willCacheResponse proposedResponse: NSCachedURLResponse, completionHandler completionHandler: (NSCachedURLResponse!) -> Void) } ``` |
| To | ``` protocol NSURLSessionDataDelegate : NSURLSessionTaskDelegate, NSURLSessionDelegate, NSObjectProtocol {     optional func URLSession(_ session: NSURLSession, dataTask dataTask: NSURLSessionDataTask, didReceiveResponse response: NSURLResponse, completionHandler completionHandler: (NSURLSessionResponseDisposition) -> Void)     optional func URLSession(_ session: NSURLSession, dataTask dataTask: NSURLSessionDataTask, didBecomeDownloadTask downloadTask: NSURLSessionDownloadTask)     optional func URLSession(_ session: NSURLSession, dataTask dataTask: NSURLSessionDataTask, didBecomeStreamTask streamTask: NSURLSessionStreamTask)     optional func URLSession(_ session: NSURLSession, dataTask dataTask: NSURLSessionDataTask, didReceiveData data: NSData)     optional func URLSession(_ session: NSURLSession, dataTask dataTask: NSURLSessionDataTask, willCacheResponse proposedResponse: NSCachedURLResponse, completionHandler completionHandler: (NSCachedURLResponse?) -> Void) } ``` |

Modified [NSURLSessionDataDelegate.URLSession(_: NSURLSession, dataTask: NSURLSessionDataTask, didBecomeDownloadTask: NSURLSessionDownloadTask)](https://developer.apple.com/documentation/foundation/nsurlsessiondatadelegate/1409936-urlsession)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSURLSessionDataDelegate.URLSession(_: NSURLSession, dataTask: NSURLSessionDataTask, didReceiveData: NSData)](https://developer.apple.com/documentation/foundation/urlsessiondatadelegate/1411528-urlsession)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSURLSessionDataDelegate.URLSession(_: NSURLSession, dataTask: NSURLSessionDataTask, didReceiveResponse: NSURLResponse, completionHandler: (NSURLSessionResponseDisposition) -> Void)](https://developer.apple.com/documentation/foundation/nsurlsessiondatadelegate/1410027-urlsession)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSURLSessionDataDelegate.URLSession(_: NSURLSession, dataTask: NSURLSessionDataTask, willCacheResponse: NSCachedURLResponse, completionHandler: (NSCachedURLResponse?) -> Void)](https://developer.apple.com/documentation/foundation/urlsessiondatadelegate/1411612-urlsession)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func URLSession(_ session: NSURLSession, dataTask dataTask: NSURLSessionDataTask, willCacheResponse proposedResponse: NSCachedURLResponse, completionHandler completionHandler: (NSCachedURLResponse!) -> Void) ``` | iOS 8.0 |
| To | ``` optional func URLSession(_ session: NSURLSession, dataTask dataTask: NSURLSessionDataTask, willCacheResponse proposedResponse: NSCachedURLResponse, completionHandler completionHandler: (NSCachedURLResponse?) -> Void) ``` | iOS 7.0 |

Modified [NSURLSessionDelegate](https://developer.apple.com/documentation/foundation/urlsessiondelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol NSURLSessionDelegate : NSObjectProtocol {     optional func URLSession(_ session: NSURLSession, didBecomeInvalidWithError error: NSError?)     optional func URLSession(_ session: NSURLSession, didReceiveChallenge challenge: NSURLAuthenticationChallenge, completionHandler completionHandler: (NSURLSessionAuthChallengeDisposition, NSURLCredential!) -> Void)     optional func URLSessionDidFinishEventsForBackgroundURLSession(_ session: NSURLSession) } ``` |
| To | ``` protocol NSURLSessionDelegate : NSObjectProtocol {     optional func URLSession(_ session: NSURLSession, didBecomeInvalidWithError error: NSError?)     optional func URLSession(_ session: NSURLSession, didReceiveChallenge challenge: NSURLAuthenticationChallenge, completionHandler completionHandler: (NSURLSessionAuthChallengeDisposition, NSURLCredential?) -> Void)     optional func URLSessionDidFinishEventsForBackgroundURLSession(_ session: NSURLSession) } ``` |

Modified [NSURLSessionDelegate.URLSession(_: NSURLSession, didBecomeInvalidWithError: NSError?)](https://developer.apple.com/documentation/foundation/urlsessiondelegate/1407776-urlsession)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSURLSessionDelegate.URLSession(_: NSURLSession, didReceiveChallenge: NSURLAuthenticationChallenge, completionHandler: (NSURLSessionAuthChallengeDisposition, NSURLCredential?) -> Void)](https://developer.apple.com/documentation/foundation/nsurlsessiondelegate/1409308-urlsession)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func URLSession(_ session: NSURLSession, didReceiveChallenge challenge: NSURLAuthenticationChallenge, completionHandler completionHandler: (NSURLSessionAuthChallengeDisposition, NSURLCredential!) -> Void) ``` | iOS 8.0 |
| To | ``` optional func URLSession(_ session: NSURLSession, didReceiveChallenge challenge: NSURLAuthenticationChallenge, completionHandler completionHandler: (NSURLSessionAuthChallengeDisposition, NSURLCredential?) -> Void) ``` | iOS 7.0 |

Modified [NSURLSessionDownloadDelegate.URLSession(_: NSURLSession, downloadTask: NSURLSessionDownloadTask, didFinishDownloadingToURL: NSURL)](https://developer.apple.com/documentation/foundation/nsurlsessiondownloaddelegate/1411575-urlsession)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSURLSessionDownloadDelegate.URLSession(_: NSURLSession, downloadTask: NSURLSessionDownloadTask, didResumeAtOffset: Int64, expectedTotalBytes: Int64)](https://developer.apple.com/documentation/foundation/nsurlsessiondownloaddelegate/1408142-urlsession)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSURLSessionDownloadDelegate.URLSession(_: NSURLSession, downloadTask: NSURLSessionDownloadTask, didWriteData: Int64, totalBytesWritten: Int64, totalBytesExpectedToWrite: Int64)](https://developer.apple.com/documentation/foundation/nsurlsessiondownloaddelegate/1409408-urlsession)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSURLSessionDownloadTask](https://developer.apple.com/documentation/foundation/nsurlsessiondownloadtask)

|  | Declaration |
| --- | --- |
| From | ``` class NSURLSessionDownloadTask : NSURLSessionTask {     func cancelByProducingResumeData(_ completionHandler: (NSData!) -> Void) } ``` |
| To | ``` class NSURLSessionDownloadTask : NSURLSessionTask {     func cancelByProducingResumeData(_ completionHandler: (NSData?) -> Void) } ``` |

Modified [NSURLSessionDownloadTask.cancelByProducingResumeData(_: (NSData?) -> Void)](https://developer.apple.com/documentation/foundation/nsurlsessiondownloadtask/1411634-cancelbyproducingresumedata)

|  | Declaration |
| --- | --- |
| From | ``` func cancelByProducingResumeData(_ completionHandler: (NSData!) -> Void) ``` |
| To | ``` func cancelByProducingResumeData(_ completionHandler: (NSData?) -> Void) ``` |

Modified [NSURLSessionResponseDisposition [enum]](https://developer.apple.com/documentation/foundation/nsurlsessionresponsedisposition)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum NSURLSessionResponseDisposition : Int {     case Cancel     case Allow     case BecomeDownload } ``` | -- |
| To | ``` enum NSURLSessionResponseDisposition : Int {     case Cancel     case Allow     case BecomeDownload     case BecomeStream } ``` | Int |

Modified [NSURLSessionTask](https://developer.apple.com/documentation/foundation/nsurlsessiontask)

|  | Declaration |
| --- | --- |
| From | ``` class NSURLSessionTask : NSObject, NSCopying {     var taskIdentifier: Int { get }     @NSCopying var originalRequest: NSURLRequest { get }     @NSCopying var currentRequest: NSURLRequest { get }     @NSCopying var response: NSURLResponse? { get }     var countOfBytesReceived: Int64 { get }     var countOfBytesSent: Int64 { get }     var countOfBytesExpectedToSend: Int64 { get }     var countOfBytesExpectedToReceive: Int64 { get }     var taskDescription: String     func cancel()     var state: NSURLSessionTaskState { get }     @NSCopying var error: NSError? { get }     func suspend()     func resume()     var priority: Float } ``` |
| To | ``` class NSURLSessionTask : NSObject, NSCopying {     var taskIdentifier: Int { get }     @NSCopying var originalRequest: NSURLRequest? { get }     @NSCopying var currentRequest: NSURLRequest? { get }     @NSCopying var response: NSURLResponse? { get }     var countOfBytesReceived: Int64 { get }     var countOfBytesSent: Int64 { get }     var countOfBytesExpectedToSend: Int64 { get }     var countOfBytesExpectedToReceive: Int64 { get }     var taskDescription: String?     func cancel()     var state: NSURLSessionTaskState { get }     @NSCopying var error: NSError? { get }     func suspend()     func resume()     var priority: Float } ``` |

Modified [NSURLSessionTask.currentRequest](https://developer.apple.com/documentation/foundation/nsurlsessiontask/1411649-currentrequest)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var currentRequest: NSURLRequest { get } ``` |
| To | ``` @NSCopying var currentRequest: NSURLRequest? { get } ``` |

Modified [NSURLSessionTask.originalRequest](https://developer.apple.com/documentation/foundation/nsurlsessiontask/1411572-originalrequest)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var originalRequest: NSURLRequest { get } ``` |
| To | ``` @NSCopying var originalRequest: NSURLRequest? { get } ``` |

Modified [NSURLSessionTask.taskDescription](https://developer.apple.com/documentation/foundation/nsurlsessiontask/1409798-taskdescription)

|  | Declaration |
| --- | --- |
| From | ``` var taskDescription: String ``` |
| To | ``` var taskDescription: String? ``` |

Modified [NSURLSessionTaskDelegate](https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol NSURLSessionTaskDelegate : NSURLSessionDelegate, NSObjectProtocol {     optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, willPerformHTTPRedirection response: NSHTTPURLResponse, newRequest request: NSURLRequest, completionHandler completionHandler: (NSURLRequest!) -> Void)     optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, didReceiveChallenge challenge: NSURLAuthenticationChallenge, completionHandler completionHandler: (NSURLSessionAuthChallengeDisposition, NSURLCredential!) -> Void)     optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, needNewBodyStream completionHandler: (NSInputStream!) -> Void)     optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, didSendBodyData bytesSent: Int64, totalBytesSent totalBytesSent: Int64, totalBytesExpectedToSend totalBytesExpectedToSend: Int64)     optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, didCompleteWithError error: NSError?) } ``` |
| To | ``` protocol NSURLSessionTaskDelegate : NSURLSessionDelegate, NSObjectProtocol {     optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, willPerformHTTPRedirection response: NSHTTPURLResponse, newRequest request: NSURLRequest, completionHandler completionHandler: (NSURLRequest?) -> Void)     optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, didReceiveChallenge challenge: NSURLAuthenticationChallenge, completionHandler completionHandler: (NSURLSessionAuthChallengeDisposition, NSURLCredential?) -> Void)     optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, needNewBodyStream completionHandler: (NSInputStream?) -> Void)     optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, didSendBodyData bytesSent: Int64, totalBytesSent totalBytesSent: Int64, totalBytesExpectedToSend totalBytesExpectedToSend: Int64)     optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, didCompleteWithError error: NSError?) } ``` |

Modified [NSURLSessionTaskDelegate.URLSession(_: NSURLSession, task: NSURLSessionTask, didCompleteWithError: NSError?)](https://developer.apple.com/documentation/foundation/nsurlsessiontaskdelegate/1411610-urlsession)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSURLSessionTaskDelegate.URLSession(_: NSURLSession, task: NSURLSessionTask, didReceiveChallenge: NSURLAuthenticationChallenge, completionHandler: (NSURLSessionAuthChallengeDisposition, NSURLCredential?) -> Void)](https://developer.apple.com/documentation/foundation/nsurlsessiontaskdelegate/1411595-urlsession)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, didReceiveChallenge challenge: NSURLAuthenticationChallenge, completionHandler completionHandler: (NSURLSessionAuthChallengeDisposition, NSURLCredential!) -> Void) ``` | iOS 8.0 |
| To | ``` optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, didReceiveChallenge challenge: NSURLAuthenticationChallenge, completionHandler completionHandler: (NSURLSessionAuthChallengeDisposition, NSURLCredential?) -> Void) ``` | iOS 7.0 |

Modified [NSURLSessionTaskDelegate.URLSession(_: NSURLSession, task: NSURLSessionTask, didSendBodyData: Int64, totalBytesSent: Int64, totalBytesExpectedToSend: Int64)](https://developer.apple.com/documentation/foundation/nsurlsessiontaskdelegate/1408299-urlsession)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSURLSessionTaskDelegate.URLSession(_: NSURLSession, task: NSURLSessionTask, needNewBodyStream: (NSInputStream?) -> Void)](https://developer.apple.com/documentation/foundation/nsurlsessiontaskdelegate/1410001-urlsession)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, needNewBodyStream completionHandler: (NSInputStream!) -> Void) ``` | iOS 8.0 |
| To | ``` optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, needNewBodyStream completionHandler: (NSInputStream?) -> Void) ``` | iOS 7.0 |

Modified [NSURLSessionTaskDelegate.URLSession(_: NSURLSession, task: NSURLSessionTask, willPerformHTTPRedirection: NSHTTPURLResponse, newRequest: NSURLRequest, completionHandler: (NSURLRequest?) -> Void)](https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/1411626-urlsession)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, willPerformHTTPRedirection response: NSHTTPURLResponse, newRequest request: NSURLRequest, completionHandler completionHandler: (NSURLRequest!) -> Void) ``` | iOS 8.0 |
| To | ``` optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, willPerformHTTPRedirection response: NSHTTPURLResponse, newRequest request: NSURLRequest, completionHandler completionHandler: (NSURLRequest?) -> Void) ``` | iOS 7.0 |

Modified [NSURLSessionTaskState [enum]](https://developer.apple.com/documentation/foundation/nsurlsessiontaskstate)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity)

|  | Declaration |
| --- | --- |
| From | ``` class NSUserActivity : NSObject {     init(activityType activityType: String)     init()     var activityType: String { get }     var title: String?     var userInfo: [NSObject : AnyObject]?     func addUserInfoEntriesFromDictionary(_ otherDictionary: [NSObject : AnyObject])     var needsSave: Bool     @NSCopying var webpageURL: NSURL?     var supportsContinuationStreams: Bool     weak var delegate: NSUserActivityDelegate?     func becomeCurrent()     func invalidate()     func getContinuationStreamsWithCompletionHandler(_ completionHandler: (NSInputStream!, NSOutputStream!, NSError!) -> Void) } ``` |
| To | ``` class NSUserActivity : NSObject {     init(activityType activityType: String)     init()     var activityType: String { get }     var title: String?     var userInfo: [NSObject : AnyObject]?     func addUserInfoEntriesFromDictionary(_ otherDictionary: [NSObject : AnyObject])     var requiredUserInfoKeys: Set<String>     var needsSave: Bool     @NSCopying var webpageURL: NSURL?     @NSCopying var expirationDate: NSDate     var keywords: Set<String>     var supportsContinuationStreams: Bool     weak var delegate: NSUserActivityDelegate?     func becomeCurrent()     func resignCurrent()     func invalidate()     func getContinuationStreamsWithCompletionHandler(_ completionHandler: (NSInputStream?, NSOutputStream?, NSError?) -> Void)     var eligibleForHandoff: Bool     var eligibleForSearch: Bool     var eligibleForPublicIndexing: Bool } extension NSUserActivity {     @NSCopying var contentAttributeSet: CSSearchableItemAttributeSet? } ``` |

Modified [NSUserActivity.getContinuationStreamsWithCompletionHandler(_: (NSInputStream?, NSOutputStream?, NSError?) -> Void)](https://developer.apple.com/documentation/foundation/nsuseractivity/1409931-getcontinuationstreams)

|  | Declaration |
| --- | --- |
| From | ``` func getContinuationStreamsWithCompletionHandler(_ completionHandler: (NSInputStream!, NSOutputStream!, NSError!) -> Void) ``` |
| To | ``` func getContinuationStreamsWithCompletionHandler(_ completionHandler: (NSInputStream?, NSOutputStream?, NSError?) -> Void) ``` |

Modified [NSUserActivityDelegate](https://developer.apple.com/documentation/foundation/nsuseractivitydelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol NSUserActivityDelegate : NSObjectProtocol {     optional func userActivityWillSave(_ userActivity: NSUserActivity)     optional func userActivityWasContinued(_ userActivity: NSUserActivity)     optional func userActivity(_ userActivity: NSUserActivity, didReceiveInputStream inputStream: NSInputStream, outputStream outputStream: NSOutputStream) } ``` |
| To | ``` protocol NSUserActivityDelegate : NSObjectProtocol {     optional func userActivityWillSave(_ userActivity: NSUserActivity)     optional func userActivityWasContinued(_ userActivity: NSUserActivity)     optional func userActivity(_ userActivity: NSUserActivity?, didReceiveInputStream inputStream: NSInputStream, outputStream outputStream: NSOutputStream) } ``` |

Modified [NSUserActivityDelegate.userActivity(_: NSUserActivity?, didReceiveInputStream: NSInputStream, outputStream: NSOutputStream)](https://developer.apple.com/documentation/foundation/nsuseractivitydelegate/1407386-useractivity)

|  | Declaration |
| --- | --- |
| From | ``` optional func userActivity(_ userActivity: NSUserActivity, didReceiveInputStream inputStream: NSInputStream, outputStream outputStream: NSOutputStream) ``` |
| To | ``` optional func userActivity(_ userActivity: NSUserActivity?, didReceiveInputStream inputStream: NSInputStream, outputStream outputStream: NSOutputStream) ``` |

Modified [NSUserDefaults](https://developer.apple.com/documentation/foundation/userdefaults)

|  | Declaration |
| --- | --- |
| From | ``` class NSUserDefaults : NSObject {     class func standardUserDefaults() -> NSUserDefaults     class func resetStandardUserDefaults()     convenience init()     init?(suiteName suitename: String?)     convenience init?(user username: String)     func objectForKey(_ defaultName: String) -> AnyObject?     func setObject(_ value: AnyObject?, forKey defaultName: String)     func removeObjectForKey(_ defaultName: String)     func stringForKey(_ defaultName: String) -> String?     func arrayForKey(_ defaultName: String) -> [AnyObject]?     func dictionaryForKey(_ defaultName: String) -> [NSObject : AnyObject]?     func dataForKey(_ defaultName: String) -> NSData?     func stringArrayForKey(_ defaultName: String) -> [AnyObject]?     func integerForKey(_ defaultName: String) -> Int     func floatForKey(_ defaultName: String) -> Float     func doubleForKey(_ defaultName: String) -> Double     func boolForKey(_ defaultName: String) -> Bool     func URLForKey(_ defaultName: String) -> NSURL?     func setInteger(_ value: Int, forKey defaultName: String)     func setFloat(_ value: Float, forKey defaultName: String)     func setDouble(_ value: Double, forKey defaultName: String)     func setBool(_ value: Bool, forKey defaultName: String)     func setURL(_ url: NSURL, forKey defaultName: String)     func registerDefaults(_ registrationDictionary: [NSObject : AnyObject])     func addSuiteNamed(_ suiteName: String)     func removeSuiteNamed(_ suiteName: String)     func dictionaryRepresentation() -> [NSObject : AnyObject]     var volatileDomainNames: [AnyObject] { get }     func volatileDomainForName(_ domainName: String) -> [NSObject : AnyObject]     func setVolatileDomain(_ domain: [NSObject : AnyObject], forName domainName: String)     func removeVolatileDomainForName(_ domainName: String)     func persistentDomainNames() -> [AnyObject]     func persistentDomainForName(_ domainName: String) -> [NSObject : AnyObject]?     func setPersistentDomain(_ domain: [NSObject : AnyObject], forName domainName: String)     func removePersistentDomainForName(_ domainName: String)     func synchronize() -> Bool     func objectIsForcedForKey(_ key: String) -> Bool     func objectIsForcedForKey(_ key: String, inDomain domain: String) -> Bool } ``` |
| To | ``` class NSUserDefaults : NSObject {     class func standardUserDefaults() -> NSUserDefaults     class func resetStandardUserDefaults()     convenience init()     init?(suiteName suitename: String?)     convenience init?(user username: String)     func objectForKey(_ defaultName: String) -> AnyObject?     func setObject(_ value: AnyObject?, forKey defaultName: String)     func removeObjectForKey(_ defaultName: String)     func stringForKey(_ defaultName: String) -> String?     func arrayForKey(_ defaultName: String) -> [AnyObject]?     func dictionaryForKey(_ defaultName: String) -> [String : AnyObject]?     func dataForKey(_ defaultName: String) -> NSData?     func stringArrayForKey(_ defaultName: String) -> [String]?     func integerForKey(_ defaultName: String) -> Int     func floatForKey(_ defaultName: String) -> Float     func doubleForKey(_ defaultName: String) -> Double     func boolForKey(_ defaultName: String) -> Bool     func URLForKey(_ defaultName: String) -> NSURL?     func setInteger(_ value: Int, forKey defaultName: String)     func setFloat(_ value: Float, forKey defaultName: String)     func setDouble(_ value: Double, forKey defaultName: String)     func setBool(_ value: Bool, forKey defaultName: String)     func setURL(_ url: NSURL?, forKey defaultName: String)     func registerDefaults(_ registrationDictionary: [String : AnyObject])     func addSuiteNamed(_ suiteName: String)     func removeSuiteNamed(_ suiteName: String)     func dictionaryRepresentation() -> [String : AnyObject]     var volatileDomainNames: [String] { get }     func volatileDomainForName(_ domainName: String) -> [String : AnyObject]     func setVolatileDomain(_ domain: [String : AnyObject], forName domainName: String)     func removeVolatileDomainForName(_ domainName: String)     func persistentDomainNames() -> [AnyObject]     func persistentDomainForName(_ domainName: String) -> [String : AnyObject]?     func setPersistentDomain(_ domain: [String : AnyObject], forName domainName: String)     func removePersistentDomainForName(_ domainName: String)     func synchronize() -> Bool     func objectIsForcedForKey(_ key: String) -> Bool     func objectIsForcedForKey(_ key: String, inDomain domain: String) -> Bool } ``` |

Modified [NSUserDefaults.dictionaryForKey(_: String) -> [String : AnyObject]?](https://developer.apple.com/documentation/foundation/nsuserdefaults/1408563-dictionaryforkey)

|  | Declaration |
| --- | --- |
| From | ``` func dictionaryForKey(_ defaultName: String) -> [NSObject : AnyObject]? ``` |
| To | ``` func dictionaryForKey(_ defaultName: String) -> [String : AnyObject]? ``` |

Modified [NSUserDefaults.dictionaryRepresentation() -> [String : AnyObject]](https://developer.apple.com/documentation/foundation/nsuserdefaults/1415919-dictionaryrepresentation)

|  | Declaration |
| --- | --- |
| From | ``` func dictionaryRepresentation() -> [NSObject : AnyObject] ``` |
| To | ``` func dictionaryRepresentation() -> [String : AnyObject] ``` |

Modified [NSUserDefaults.persistentDomainForName(_: String) -> [String : AnyObject]?](https://developer.apple.com/documentation/foundation/nsuserdefaults/1412197-persistentdomainforname)

|  | Declaration |
| --- | --- |
| From | ``` func persistentDomainForName(_ domainName: String) -> [NSObject : AnyObject]? ``` |
| To | ``` func persistentDomainForName(_ domainName: String) -> [String : AnyObject]? ``` |

Modified [NSUserDefaults.registerDefaults(_: [String : AnyObject])](https://developer.apple.com/documentation/foundation/nsuserdefaults/1417065-registerdefaults)

|  | Declaration |
| --- | --- |
| From | ``` func registerDefaults(_ registrationDictionary: [NSObject : AnyObject]) ``` |
| To | ``` func registerDefaults(_ registrationDictionary: [String : AnyObject]) ``` |

Modified [NSUserDefaults.setPersistentDomain(_: [String : AnyObject], forName: String)](https://developer.apple.com/documentation/foundation/nsuserdefaults/1408187-setpersistentdomain)

|  | Declaration |
| --- | --- |
| From | ``` func setPersistentDomain(_ domain: [NSObject : AnyObject], forName domainName: String) ``` |
| To | ``` func setPersistentDomain(_ domain: [String : AnyObject], forName domainName: String) ``` |

Modified [NSUserDefaults.setURL(_: NSURL?, forKey: String)](https://developer.apple.com/documentation/foundation/userdefaults/1414194-set)

|  | Declaration |
| --- | --- |
| From | ``` func setURL(_ url: NSURL, forKey defaultName: String) ``` |
| To | ``` func setURL(_ url: NSURL?, forKey defaultName: String) ``` |

Modified [NSUserDefaults.setVolatileDomain(_: [String : AnyObject], forName: String)](https://developer.apple.com/documentation/foundation/nsuserdefaults/1413720-setvolatiledomain)

|  | Declaration |
| --- | --- |
| From | ``` func setVolatileDomain(_ domain: [NSObject : AnyObject], forName domainName: String) ``` |
| To | ``` func setVolatileDomain(_ domain: [String : AnyObject], forName domainName: String) ``` |

Modified [NSUserDefaults.stringArrayForKey(_: String) -> [String]?](https://developer.apple.com/documentation/foundation/nsuserdefaults/1416414-stringarrayforkey)

|  | Declaration |
| --- | --- |
| From | ``` func stringArrayForKey(_ defaultName: String) -> [AnyObject]? ``` |
| To | ``` func stringArrayForKey(_ defaultName: String) -> [String]? ``` |

Modified [NSUserDefaults.volatileDomainForName(_: String) -> [String : AnyObject]](https://developer.apple.com/documentation/foundation/nsuserdefaults/1409592-volatiledomainforname)

|  | Declaration |
| --- | --- |
| From | ``` func volatileDomainForName(_ domainName: String) -> [NSObject : AnyObject] ``` |
| To | ``` func volatileDomainForName(_ domainName: String) -> [String : AnyObject] ``` |

Modified [NSUserDefaults.volatileDomainNames](https://developer.apple.com/documentation/foundation/userdefaults/1414231-volatiledomainnames)

|  | Declaration |
| --- | --- |
| From | ``` var volatileDomainNames: [AnyObject] { get } ``` |
| To | ``` var volatileDomainNames: [String] { get } ``` |

Modified [NSValue](https://developer.apple.com/documentation/foundation/nsvalue)

|  | Declaration |
| --- | --- |
| From | ``` class NSValue : NSObject, NSCopying, NSSecureCoding, NSCoding {     func getValue(_ value: UnsafeMutablePointer<Void>)     var objCType: UnsafePointer<Int8> { get }     init(bytes value: UnsafePointer<Void>, objCType type: UnsafePointer<Int8>)     init(coder aDecoder: NSCoder) } extension NSValue {     init!(CMTime time: CMTime) -> NSValue     class func valueWithCMTime(_ time: CMTime) -> NSValue!     var CMTimeValue: CMTime { get }     init!(CMTimeRange timeRange: CMTimeRange) -> NSValue     class func valueWithCMTimeRange(_ timeRange: CMTimeRange) -> NSValue!     var CMTimeRangeValue: CMTimeRange { get }     init!(CMTimeMapping timeMapping: CMTimeMapping) -> NSValue     class func valueWithCMTimeMapping(_ timeMapping: CMTimeMapping) -> NSValue!     var CMTimeMappingValue: CMTimeMapping { get } } extension NSValue {     init(range range: NSRange) -> NSValue     class func valueWithRange(_ range: NSRange) -> NSValue     var rangeValue: NSRange { get } } extension NSValue {     class func valueWithBytes(_ value: UnsafePointer<Void>, objCType type: UnsafePointer<Int8>) -> NSValue     init(_ value: UnsafePointer<Void>, withObjCType type: UnsafePointer<Int8>) -> NSValue     class func value(_ value: UnsafePointer<Void>, withObjCType type: UnsafePointer<Int8>) -> NSValue } extension NSValue {     init(nonretainedObject anObject: AnyObject?) -> NSValue     class func valueWithNonretainedObject(_ anObject: AnyObject?) -> NSValue     var nonretainedObjectValue: AnyObject? { get }     init(pointer pointer: UnsafePointer<Void>) -> NSValue     class func valueWithPointer(_ pointer: UnsafePointer<Void>) -> NSValue     func pointerValue() -> UnsafeMutablePointer<Void>     func isEqualToValue(_ value: NSValue) -> Bool } extension NSValue {     init!(MKCoordinate coordinate: CLLocationCoordinate2D) -> NSValue     class func valueWithMKCoordinate(_ coordinate: CLLocationCoordinate2D) -> NSValue!     init!(MKCoordinateSpan span: MKCoordinateSpan) -> NSValue     class func valueWithMKCoordinateSpan(_ span: MKCoordinateSpan) -> NSValue!     var MKCoordinateValue: CLLocationCoordinate2D { get }     var MKCoordinateSpanValue: MKCoordinateSpan { get } } extension NSValue {     init!(CATransform3D t: CATransform3D) -> NSValue     class func valueWithCATransform3D(_ t: CATransform3D) -> NSValue!     var CATransform3DValue: CATransform3D { get } } extension NSValue {     init!(SCNVector3 v: SCNVector3) -> NSValue     class func valueWithSCNVector3(_ v: SCNVector3) -> NSValue!     init!(SCNVector4 v: SCNVector4) -> NSValue     class func valueWithSCNVector4(_ v: SCNVector4) -> NSValue!     init!(SCNMatrix4 v: SCNMatrix4) -> NSValue     class func valueWithSCNMatrix4(_ v: SCNMatrix4) -> NSValue!     var SCNVector3Value: SCNVector3 { get }     var SCNVector4Value: SCNVector4 { get }     var SCNMatrix4Value: SCNMatrix4 { get } } extension NSValue {     init!(CGPoint point: CGPoint) -> NSValue     class func valueWithCGPoint(_ point: CGPoint) -> NSValue!     init!(CGVector vector: CGVector) -> NSValue     class func valueWithCGVector(_ vector: CGVector) -> NSValue!     init!(CGSize size: CGSize) -> NSValue     class func valueWithCGSize(_ size: CGSize) -> NSValue!     init!(CGRect rect: CGRect) -> NSValue     class func valueWithCGRect(_ rect: CGRect) -> NSValue!     init!(CGAffineTransform transform: CGAffineTransform) -> NSValue     class func valueWithCGAffineTransform(_ transform: CGAffineTransform) -> NSValue!     init!(UIEdgeInsets insets: UIEdgeInsets) -> NSValue     class func valueWithUIEdgeInsets(_ insets: UIEdgeInsets) -> NSValue!     init!(UIOffset insets: UIOffset) -> NSValue     class func valueWithUIOffset(_ insets: UIOffset) -> NSValue!     func CGPointValue() -> CGPoint     func CGVectorValue() -> CGVector     func CGSizeValue() -> CGSize     func CGRectValue() -> CGRect     func CGAffineTransformValue() -> CGAffineTransform     func UIEdgeInsetsValue() -> UIEdgeInsets     func UIOffsetValue() -> UIOffset } ``` |
| To | ``` class NSValue : NSObject, NSCopying, NSSecureCoding, NSCoding {     func getValue(_ value: UnsafeMutablePointer<Void>)     var objCType: UnsafePointer<Int8> { get }     init(bytes value: UnsafePointer<Void>, objCType type: UnsafePointer<Int8>)     init?(coder aDecoder: NSCoder) } extension NSValue {      init(CMTime time: CMTime)     class func valueWithCMTime(_ time: CMTime) -> NSValue     var CMTimeValue: CMTime { get }      init(CMTimeRange timeRange: CMTimeRange)     class func valueWithCMTimeRange(_ timeRange: CMTimeRange) -> NSValue     var CMTimeRangeValue: CMTimeRange { get }      init(CMTimeMapping timeMapping: CMTimeMapping)     class func valueWithCMTimeMapping(_ timeMapping: CMTimeMapping) -> NSValue     var CMTimeMappingValue: CMTimeMapping { get } } extension NSValue {      init(range range: NSRange)     class func valueWithRange(_ range: NSRange) -> NSValue     var rangeValue: NSRange { get } } extension NSValue {     class func valueWithBytes(_ value: UnsafePointer<Void>, objCType type: UnsafePointer<Int8>) -> NSValue      init(_ value: UnsafePointer<Void>, withObjCType type: UnsafePointer<Int8>)     class func value(_ value: UnsafePointer<Void>, withObjCType type: UnsafePointer<Int8>) -> NSValue } extension NSValue {      init(nonretainedObject anObject: AnyObject?)     class func valueWithNonretainedObject(_ anObject: AnyObject?) -> NSValue     var nonretainedObjectValue: AnyObject? { get }      init(pointer pointer: UnsafePointer<Void>)     class func valueWithPointer(_ pointer: UnsafePointer<Void>) -> NSValue     var pointerValue: UnsafeMutablePointer<Void> { get }     func isEqualToValue(_ value: NSValue) -> Bool } extension NSValue {      init(MKCoordinate coordinate: CLLocationCoordinate2D)     class func valueWithMKCoordinate(_ coordinate: CLLocationCoordinate2D) -> NSValue      init(MKCoordinateSpan span: MKCoordinateSpan)     class func valueWithMKCoordinateSpan(_ span: MKCoordinateSpan) -> NSValue     var MKCoordinateValue: CLLocationCoordinate2D { get }     var MKCoordinateSpanValue: MKCoordinateSpan { get } } extension NSValue {      init(CATransform3D t: CATransform3D)     class func valueWithCATransform3D(_ t: CATransform3D) -> NSValue     var CATransform3DValue: CATransform3D { get } } extension NSValue {      init(SCNVector3 v: SCNVector3)     class func valueWithSCNVector3(_ v: SCNVector3) -> NSValue      init(SCNVector4 v: SCNVector4)     class func valueWithSCNVector4(_ v: SCNVector4) -> NSValue      init(SCNMatrix4 v: SCNMatrix4)     class func valueWithSCNMatrix4(_ v: SCNMatrix4) -> NSValue     var SCNVector3Value: SCNVector3 { get }     var SCNVector4Value: SCNVector4 { get }     var SCNMatrix4Value: SCNMatrix4 { get } } extension NSValue {      init(CGPoint point: CGPoint)     class func valueWithCGPoint(_ point: CGPoint) -> NSValue      init(CGVector vector: CGVector)     class func valueWithCGVector(_ vector: CGVector) -> NSValue      init(CGSize size: CGSize)     class func valueWithCGSize(_ size: CGSize) -> NSValue      init(CGRect rect: CGRect)     class func valueWithCGRect(_ rect: CGRect) -> NSValue      init(CGAffineTransform transform: CGAffineTransform)     class func valueWithCGAffineTransform(_ transform: CGAffineTransform) -> NSValue      init(UIEdgeInsets insets: UIEdgeInsets)     class func valueWithUIEdgeInsets(_ insets: UIEdgeInsets) -> NSValue      init(UIOffset insets: UIOffset)     class func valueWithUIOffset(_ insets: UIOffset) -> NSValue     func CGPointValue() -> CGPoint     func CGVectorValue() -> CGVector     func CGSizeValue() -> CGSize     func CGRectValue() -> CGRect     func CGAffineTransformValue() -> CGAffineTransform     func UIEdgeInsetsValue() -> UIEdgeInsets     func UIOffsetValue() -> UIOffset } ``` |

Modified [NSValue.init(_: UnsafePointer<Void>, withObjCType: UnsafePointer<Int8>)](https://developer.apple.com/documentation/foundation/nsvalue/1417400-init)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UnsafePointer<Void>, withObjCType type: UnsafePointer<Int8>) -> NSValue ``` |
| To | ``` init(_ value: UnsafePointer<Void>, withObjCType type: UnsafePointer<Int8>) ``` |

Modified [NSValue.init(coder: NSCoder)](https://developer.apple.com/documentation/foundation/nsvalue/1417896-init)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified [NSValue.init(nonretainedObject: AnyObject?)](https://developer.apple.com/documentation/foundation/nsvalue/1408098-valuewithnonretainedobject)

|  | Declaration |
| --- | --- |
| From | ``` init(nonretainedObject anObject: AnyObject?) -> NSValue ``` |
| To | ``` init(nonretainedObject anObject: AnyObject?) ``` |

Modified [NSValue.init(pointer: UnsafePointer<Void>)](https://developer.apple.com/documentation/foundation/nsvalue/1415975-valuewithpointer)

|  | Declaration |
| --- | --- |
| From | ``` init(pointer pointer: UnsafePointer<Void>) -> NSValue ``` |
| To | ``` init(pointer pointer: UnsafePointer<Void>) ``` |

Modified [NSValue.init(range: NSRange)](https://developer.apple.com/documentation/foundation/nsvalue/1410315-init)

|  | Declaration |
| --- | --- |
| From | ``` init(range range: NSRange) -> NSValue ``` |
| To | ``` init(range range: NSRange) ``` |

Modified [NSValueTransformer](https://developer.apple.com/documentation/foundation/nsvaluetransformer)

|  | Declaration |
| --- | --- |
| From | ``` class NSValueTransformer : NSObject {     class func setValueTransformer(_ transformer: NSValueTransformer, forName name: String)     init?(forName name: String) -> NSValueTransformer     class func valueTransformerForName(_ name: String) -> NSValueTransformer?     class func valueTransformerNames() -> [AnyObject]     class func transformedValueClass() -> AnyClass     class func allowsReverseTransformation() -> Bool     func transformedValue(_ value: AnyObject?) -> AnyObject?     func reverseTransformedValue(_ value: AnyObject?) -> AnyObject? } ``` |
| To | ``` class NSValueTransformer : NSObject {     class func setValueTransformer(_ transformer: NSValueTransformer?, forName name: String)      init?(forName name: String)     class func valueTransformerForName(_ name: String) -> NSValueTransformer?     class func valueTransformerNames() -> [String]     class func transformedValueClass() -> AnyClass     class func allowsReverseTransformation() -> Bool     func transformedValue(_ value: AnyObject?) -> AnyObject?     func reverseTransformedValue(_ value: AnyObject?) -> AnyObject? } ``` |

Modified [NSValueTransformer.init(forName: String)](https://developer.apple.com/documentation/foundation/valuetransformer/1402010-init)

|  | Declaration |
| --- | --- |
| From | ``` init?(forName name: String) -> NSValueTransformer ``` |
| To | ``` init?(forName name: String) ``` |

Modified [NSValueTransformer.setValueTransformer(_: NSValueTransformer?, forName: String) [class]](https://developer.apple.com/documentation/foundation/nsvaluetransformer/1402018-setvaluetransformer)

|  | Declaration |
| --- | --- |
| From | ``` class func setValueTransformer(_ transformer: NSValueTransformer, forName name: String) ``` |
| To | ``` class func setValueTransformer(_ transformer: NSValueTransformer?, forName name: String) ``` |

Modified [NSValueTransformer.valueTransformerNames() -> [String] [class]](https://developer.apple.com/documentation/foundation/valuetransformer/1402012-valuetransformernames)

|  | Declaration |
| --- | --- |
| From | ``` class func valueTransformerNames() -> [AnyObject] ``` |
| To | ``` class func valueTransformerNames() -> [String] ``` |

Modified [NSVolumeEnumerationOptions [struct]](https://developer.apple.com/documentation/foundation/filemanager/volumeenumerationoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSVolumeEnumerationOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var SkipHiddenVolumes: NSVolumeEnumerationOptions { get }     static var ProduceFileReferenceURLs: NSVolumeEnumerationOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSVolumeEnumerationOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var SkipHiddenVolumes: NSVolumeEnumerationOptions { get }     static var ProduceFileReferenceURLs: NSVolumeEnumerationOptions { get } } ``` | OptionSetType |

Modified [NSXMLParser](https://developer.apple.com/documentation/foundation/xmlparser)

|  | Declaration |
| --- | --- |
| From | ``` class NSXMLParser : NSObject {     convenience init?(contentsOfURL url: NSURL!)     init(data data: NSData)     convenience init(stream stream: NSInputStream)     unowned(unsafe) var delegate: NSXMLParserDelegate?     var shouldProcessNamespaces: Bool     var shouldReportNamespacePrefixes: Bool     var externalEntityResolvingPolicy: NSXMLParserExternalEntityResolvingPolicy     var allowedExternalEntityURLs: Set<NSObject>?     func parse() -> Bool     func abortParsing()     @NSCopying var parserError: NSError? { get }     var shouldResolveExternalEntities: Bool } extension NSXMLParser {     var publicID: String? { get }     var systemID: String? { get }     var lineNumber: Int { get }     var columnNumber: Int { get } } ``` |
| To | ``` class NSXMLParser : NSObject {     convenience init?(contentsOfURL url: NSURL)     init(data data: NSData)     convenience init(stream stream: NSInputStream)     unowned(unsafe) var delegate: NSXMLParserDelegate?     var shouldProcessNamespaces: Bool     var shouldReportNamespacePrefixes: Bool     var externalEntityResolvingPolicy: NSXMLParserExternalEntityResolvingPolicy     var allowedExternalEntityURLs: Set<NSURL>?     func parse() -> Bool     func abortParsing()     @NSCopying var parserError: NSError? { get }     var shouldResolveExternalEntities: Bool } extension NSXMLParser {     var publicID: String? { get }     var systemID: String? { get }     var lineNumber: Int { get }     var columnNumber: Int { get } } ``` |

Modified [NSXMLParser.allowedExternalEntityURLs](https://developer.apple.com/documentation/foundation/nsxmlparser/1412380-allowedexternalentityurls)

|  | Declaration |
| --- | --- |
| From | ``` var allowedExternalEntityURLs: Set<NSObject>? ``` |
| To | ``` var allowedExternalEntityURLs: Set<NSURL>? ``` |

Modified [NSXMLParser.init(contentsOfURL: NSURL)](https://developer.apple.com/documentation/foundation/xmlparser/1415575-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init?(contentsOfURL url: NSURL!) ``` |
| To | ``` convenience init?(contentsOfURL url: NSURL) ``` |

Modified [NSXMLParserDelegate](https://developer.apple.com/documentation/foundation/nsxmlparserdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol NSXMLParserDelegate : NSObjectProtocol {     optional func parserDidStartDocument(_ parser: NSXMLParser)     optional func parserDidEndDocument(_ parser: NSXMLParser)     optional func parser(_ parser: NSXMLParser, foundNotationDeclarationWithName name: String, publicID publicID: String?, systemID systemID: String?)     optional func parser(_ parser: NSXMLParser, foundUnparsedEntityDeclarationWithName name: String, publicID publicID: String?, systemID systemID: String?, notationName notationName: String?)     optional func parser(_ parser: NSXMLParser, foundAttributeDeclarationWithName attributeName: String, forElement elementName: String, type type: String?, defaultValue defaultValue: String?)     optional func parser(_ parser: NSXMLParser, foundElementDeclarationWithName elementName: String, model model: String)     optional func parser(_ parser: NSXMLParser, foundInternalEntityDeclarationWithName name: String, value value: String?)     optional func parser(_ parser: NSXMLParser, foundExternalEntityDeclarationWithName name: String, publicID publicID: String?, systemID systemID: String?)     optional func parser(_ parser: NSXMLParser, didStartElement elementName: String, namespaceURI namespaceURI: String?, qualifiedName qName: String?, attributes attributeDict: [NSObject : AnyObject])     optional func parser(_ parser: NSXMLParser, didEndElement elementName: String, namespaceURI namespaceURI: String?, qualifiedName qName: String?)     optional func parser(_ parser: NSXMLParser, didStartMappingPrefix prefix: String, toURI namespaceURI: String)     optional func parser(_ parser: NSXMLParser, didEndMappingPrefix prefix: String)     optional func parser(_ parser: NSXMLParser, foundCharacters string: String?)     optional func parser(_ parser: NSXMLParser, foundIgnorableWhitespace whitespaceString: String)     optional func parser(_ parser: NSXMLParser, foundProcessingInstructionWithTarget target: String, data data: String?)     optional func parser(_ parser: NSXMLParser, foundComment comment: String?)     optional func parser(_ parser: NSXMLParser, foundCDATA CDATABlock: NSData)     optional func parser(_ parser: NSXMLParser, resolveExternalEntityName name: String, systemID systemID: String?) -> NSData?     optional func parser(_ parser: NSXMLParser, parseErrorOccurred parseError: NSError)     optional func parser(_ parser: NSXMLParser, validationErrorOccurred validationError: NSError) } ``` |
| To | ``` protocol NSXMLParserDelegate : NSObjectProtocol {     optional func parserDidStartDocument(_ parser: NSXMLParser)     optional func parserDidEndDocument(_ parser: NSXMLParser)     optional func parser(_ parser: NSXMLParser, foundNotationDeclarationWithName name: String, publicID publicID: String?, systemID systemID: String?)     optional func parser(_ parser: NSXMLParser, foundUnparsedEntityDeclarationWithName name: String, publicID publicID: String?, systemID systemID: String?, notationName notationName: String?)     optional func parser(_ parser: NSXMLParser, foundAttributeDeclarationWithName attributeName: String, forElement elementName: String, type type: String?, defaultValue defaultValue: String?)     optional func parser(_ parser: NSXMLParser, foundElementDeclarationWithName elementName: String, model model: String)     optional func parser(_ parser: NSXMLParser, foundInternalEntityDeclarationWithName name: String, value value: String?)     optional func parser(_ parser: NSXMLParser, foundExternalEntityDeclarationWithName name: String, publicID publicID: String?, systemID systemID: String?)     optional func parser(_ parser: NSXMLParser, didStartElement elementName: String, namespaceURI namespaceURI: String?, qualifiedName qName: String?, attributes attributeDict: [String : String])     optional func parser(_ parser: NSXMLParser, didEndElement elementName: String, namespaceURI namespaceURI: String?, qualifiedName qName: String?)     optional func parser(_ parser: NSXMLParser, didStartMappingPrefix prefix: String, toURI namespaceURI: String)     optional func parser(_ parser: NSXMLParser, didEndMappingPrefix prefix: String)     optional func parser(_ parser: NSXMLParser, foundCharacters string: String)     optional func parser(_ parser: NSXMLParser, foundIgnorableWhitespace whitespaceString: String)     optional func parser(_ parser: NSXMLParser, foundProcessingInstructionWithTarget target: String, data data: String?)     optional func parser(_ parser: NSXMLParser, foundComment comment: String)     optional func parser(_ parser: NSXMLParser, foundCDATA CDATABlock: NSData)     optional func parser(_ parser: NSXMLParser, resolveExternalEntityName name: String, systemID systemID: String?) -> NSData?     optional func parser(_ parser: NSXMLParser, parseErrorOccurred parseError: NSError)     optional func parser(_ parser: NSXMLParser, validationErrorOccurred validationError: NSError) } ``` |

Modified [NSXMLParserDelegate.parser(_: NSXMLParser, didStartElement: String, namespaceURI: String?, qualifiedName: String?, attributes: [String : String])](https://developer.apple.com/documentation/foundation/nsxmlparserdelegate/1415894-parser)

|  | Declaration |
| --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser, didStartElement elementName: String, namespaceURI namespaceURI: String?, qualifiedName qName: String?, attributes attributeDict: [NSObject : AnyObject]) ``` |
| To | ``` optional func parser(_ parser: NSXMLParser, didStartElement elementName: String, namespaceURI namespaceURI: String?, qualifiedName qName: String?, attributes attributeDict: [String : String]) ``` |

Modified [NSXMLParserDelegate.parser(_: NSXMLParser, foundCharacters: String)](https://developer.apple.com/documentation/foundation/xmlparserdelegate/1412539-parser)

|  | Declaration |
| --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser, foundCharacters string: String?) ``` |
| To | ``` optional func parser(_ parser: NSXMLParser, foundCharacters string: String) ``` |

Modified [NSXMLParserDelegate.parser(_: NSXMLParser, foundComment: String)](https://developer.apple.com/documentation/foundation/nsxmlparserdelegate/1417651-parser)

|  | Declaration |
| --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser, foundComment comment: String?) ``` |
| To | ``` optional func parser(_ parser: NSXMLParser, foundComment comment: String) ``` |

Modified [NSXMLParserError [enum]](https://developer.apple.com/documentation/foundation/nsxmlparsererror)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NSXMLParserExternalEntityResolvingPolicy [enum]](https://developer.apple.com/documentation/foundation/nsxmlparserexternalentityresolvingpolicy)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified String.availableStringEncodings() -> [NSStringEncoding] [static]

|  | Declaration |
| --- | --- |
| From | ``` static func availableStringEncodings() -> [NSStringEncoding] ``` |
| To | ``` @warn_unused_result     static func availableStringEncodings() -> [NSStringEncoding] ``` |

Modified String.canBeConvertedToEncoding(_: NSStringEncoding) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func canBeConvertedToEncoding(_ encoding: NSStringEncoding) -> Bool ``` |
| To | ``` @warn_unused_result     func canBeConvertedToEncoding(_ encoding: NSStringEncoding) -> Bool ``` |

Modified String.capitalizedStringWithLocale(_: NSLocale?) -> String

|  | Declaration |
| --- | --- |
| From | ``` func capitalizedStringWithLocale(_ locale: NSLocale?) -> String ``` |
| To | ``` @warn_unused_result     func capitalizedStringWithLocale(_ locale: NSLocale?) -> String ``` |

Modified String.caseInsensitiveCompare(_: String) -> NSComparisonResult

|  | Declaration |
| --- | --- |
| From | ``` func caseInsensitiveCompare(_ aString: String) -> NSComparisonResult ``` |
| To | ``` @warn_unused_result     func caseInsensitiveCompare(_ aString: String) -> NSComparisonResult ``` |

Modified String.commonPrefixWithString(_: String, options: NSStringCompareOptions) -> String

|  | Declaration |
| --- | --- |
| From | ``` func commonPrefixWithString(_ aString: String, options options: NSStringCompareOptions) -> String ``` |
| To | ``` @warn_unused_result     func commonPrefixWithString(_ aString: String, options options: NSStringCompareOptions) -> String ``` |

Modified String.completePathIntoString(_: UnsafeMutablePointer<String>, caseSensitive: Bool, matchesIntoArray: UnsafeMutablePointer<[String]>, filterTypes: [String]?) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func completePathIntoString(_ outputName: UnsafeMutablePointer<String> = default, caseSensitive caseSensitive: Bool, matchesIntoArray matchesIntoArray: UnsafeMutablePointer<[String]> = default, filterTypes filterTypes: [String]? = default) -> Int ``` |
| To | ``` @warn_unused_result     func completePathIntoString(_ outputName: UnsafeMutablePointer<String> = default, caseSensitive caseSensitive: Bool, matchesIntoArray matchesIntoArray: UnsafeMutablePointer<[String]> = default, filterTypes filterTypes: [String]? = default) -> Int ``` |

Modified String.componentsSeparatedByCharactersInSet(_: NSCharacterSet) -> [String]

|  | Declaration |
| --- | --- |
| From | ``` func componentsSeparatedByCharactersInSet(_ separator: NSCharacterSet) -> [String] ``` |
| To | ``` @warn_unused_result     func componentsSeparatedByCharactersInSet(_ separator: NSCharacterSet) -> [String] ``` |

Modified String.cStringUsingEncoding(_: NSStringEncoding) -> [CChar]?

|  | Declaration |
| --- | --- |
| From | ``` func cStringUsingEncoding(_ encoding: NSStringEncoding) -> [CChar]? ``` |
| To | ``` @warn_unused_result     func cStringUsingEncoding(_ encoding: NSStringEncoding) -> [CChar]? ``` |

Modified String.dataUsingEncoding(_: NSStringEncoding, allowLossyConversion: Bool) -> NSData?

|  | Declaration |
| --- | --- |
| From | ``` func dataUsingEncoding(_ encoding: NSStringEncoding, allowLossyConversion allowLossyConversion: Bool = default) -> NSData? ``` |
| To | ``` @warn_unused_result     func dataUsingEncoding(_ encoding: NSStringEncoding, allowLossyConversion allowLossyConversion: Bool = default) -> NSData? ``` |

Modified String.defaultCStringEncoding() -> NSStringEncoding [static]

|  | Declaration |
| --- | --- |
| From | ``` static func defaultCStringEncoding() -> NSStringEncoding ``` |
| To | ``` @warn_unused_result     static func defaultCStringEncoding() -> NSStringEncoding ``` |

Modified String.init(bytes: S, encoding: NSStringEncoding)

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` init?<S : SequenceType where UInt8 == UInt8>(bytes bytes: S, encoding encoding: NSStringEncoding) ``` | iOS 8.1 | ```  ``` | -- |
| To | ``` init?<S : SequenceType where S.Generator.Element == UInt8>(bytes bytes: S, encoding encoding: NSStringEncoding) ``` | iOS 9.0 | ``` S : SequenceType, S.Generator.Element == UInt8 ``` | S |

Modified String.lengthOfBytesUsingEncoding(_: NSStringEncoding) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func lengthOfBytesUsingEncoding(_ encoding: NSStringEncoding) -> Int ``` |
| To | ``` @warn_unused_result     func lengthOfBytesUsingEncoding(_ encoding: NSStringEncoding) -> Int ``` |

Modified String.localizedCaseInsensitiveCompare(_: String) -> NSComparisonResult

|  | Declaration |
| --- | --- |
| From | ``` func localizedCaseInsensitiveCompare(_ aString: String) -> NSComparisonResult ``` |
| To | ``` @warn_unused_result     func localizedCaseInsensitiveCompare(_ aString: String) -> NSComparisonResult ``` |

Modified String.localizedCompare(_: String) -> NSComparisonResult

|  | Declaration |
| --- | --- |
| From | ``` func localizedCompare(_ aString: String) -> NSComparisonResult ``` |
| To | ``` @warn_unused_result     func localizedCompare(_ aString: String) -> NSComparisonResult ``` |

Modified String.localizedNameOfStringEncoding(_: NSStringEncoding) -> String [static]

|  | Declaration |
| --- | --- |
| From | ``` static func localizedNameOfStringEncoding(_ encoding: NSStringEncoding) -> String ``` |
| To | ``` @warn_unused_result     static func localizedNameOfStringEncoding(_ encoding: NSStringEncoding) -> String ``` |

Modified String.localizedStandardCompare(_: String) -> NSComparisonResult

|  | Declaration |
| --- | --- |
| From | ``` func localizedStandardCompare(_ string: String) -> NSComparisonResult ``` |
| To | ``` @warn_unused_result     func localizedStandardCompare(_ string: String) -> NSComparisonResult ``` |

Modified String.localizedStringWithFormat(_: String, _: CVarArgType) -> String [static]

|  | Declaration |
| --- | --- |
| From | ``` static func localizedStringWithFormat(_ format: String, _ arguments: CVarArgType...) -> String ``` |
| To | ``` @warn_unused_result     static func localizedStringWithFormat(_ format: String, _ arguments: CVarArgType...) -> String ``` |

Modified String.maximumLengthOfBytesUsingEncoding(_: NSStringEncoding) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func maximumLengthOfBytesUsingEncoding(_ encoding: NSStringEncoding) -> Int ``` |
| To | ``` @warn_unused_result     func maximumLengthOfBytesUsingEncoding(_ encoding: NSStringEncoding) -> Int ``` |

Modified String.propertyList() -> AnyObject

|  | Declaration |
| --- | --- |
| From | ``` func propertyList() -> AnyObject ``` |
| To | ``` @warn_unused_result     func propertyList() -> AnyObject ``` |

Modified String.propertyListFromStringsFileFormat() -> [String : String]

|  | Declaration |
| --- | --- |
| From | ``` func propertyListFromStringsFileFormat() -> [String : String] ``` |
| To | ``` @warn_unused_result     func propertyListFromStringsFileFormat() -> [String : String] ``` |

Modified String.stringByAddingPercentEncodingWithAllowedCharacters(_: NSCharacterSet) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func stringByAddingPercentEncodingWithAllowedCharacters(_ allowedCharacters: NSCharacterSet) -> String? ``` |
| To | ``` @warn_unused_result     func stringByAddingPercentEncodingWithAllowedCharacters(_ allowedCharacters: NSCharacterSet) -> String? ``` |

Modified String.stringByAddingPercentEscapesUsingEncoding(_: NSStringEncoding) -> String?

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified String.stringByAppendingFormat(_: String, _: CVarArgType) -> String

|  | Declaration |
| --- | --- |
| From | ``` func stringByAppendingFormat(_ format: String, _ arguments: CVarArgType...) -> String ``` |
| To | ``` @warn_unused_result     func stringByAppendingFormat(_ format: String, _ arguments: CVarArgType...) -> String ``` |

Modified String.stringByAppendingString(_: String) -> String

|  | Declaration |
| --- | --- |
| From | ``` func stringByAppendingString(_ aString: String) -> String ``` |
| To | ``` @warn_unused_result     func stringByAppendingString(_ aString: String) -> String ``` |

Modified String.stringByPaddingToLength(_: Int, withString: String, startingAtIndex: Int) -> String

|  | Declaration |
| --- | --- |
| From | ``` func stringByPaddingToLength(_ newLength: Int, withString padString: String, startingAtIndex padIndex: Int) -> String ``` |
| To | ``` @warn_unused_result     func stringByPaddingToLength(_ newLength: Int, withString padString: String, startingAtIndex padIndex: Int) -> String ``` |

Modified String.stringByReplacingPercentEscapesUsingEncoding(_: NSStringEncoding) -> String?

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified String.stringByTrimmingCharactersInSet(_: NSCharacterSet) -> String

|  | Declaration |
| --- | --- |
| From | ``` func stringByTrimmingCharactersInSet(_ set: NSCharacterSet) -> String ``` |
| To | ``` @warn_unused_result     func stringByTrimmingCharactersInSet(_ set: NSCharacterSet) -> String ``` |

Modified [CFBridgingRetain(_: AnyObject?) -> AnyObject?](https://developer.apple.com/documentation/foundation/1416649-cfbridgingretain)

|  | Declaration |
| --- | --- |
| From | ``` func CFBridgingRetain(_ X: AnyObject!) -> AnyObject! ``` |
| To | ``` func CFBridgingRetain(_ X: AnyObject?) -> AnyObject? ``` |

Modified [NSASCIIStringEncoding](https://developer.apple.com/documentation/foundation/nsasciistringencoding)

|  | Declaration |
| --- | --- |
| From | ``` var NSASCIIStringEncoding: UInt32 { get } ``` |
| To | ``` var NSASCIIStringEncoding: UInt { get } ``` |

Modified [NSClassFromString(_: String) -> AnyClass?](https://developer.apple.com/documentation/foundation/1395135-nsclassfromstring)

|  | Declaration |
| --- | --- |
| From | ``` func NSClassFromString(_ aClassName: String!) -> AnyClass! ``` |
| To | ``` func NSClassFromString(_ aClassName: String) -> AnyClass? ``` |

Modified [NSComparator](https://developer.apple.com/documentation/foundation/nscomparator)

|  | Declaration |
| --- | --- |
| From | ``` typealias NSComparator = (AnyObject!, AnyObject!) -> NSComparisonResult ``` |
| To | ``` typealias NSComparator = (AnyObject, AnyObject) -> NSComparisonResult ``` |

Modified [NSDecimalString(_: UnsafePointer<NSDecimal>, _: AnyObject?) -> String](https://developer.apple.com/documentation/foundation/1407702-nsdecimalstring)

|  | Declaration |
| --- | --- |
| From | ``` func NSDecimalString(_ dcm: UnsafePointer<NSDecimal>, _ locale: AnyObject!) -> String! ``` |
| To | ``` func NSDecimalString(_ dcm: UnsafePointer<NSDecimal>, _ locale: AnyObject?) -> String ``` |

Modified [NSFullUserName() -> String](https://developer.apple.com/documentation/foundation/1410265-nsfullusername)

|  | Declaration |
| --- | --- |
| From | ``` func NSFullUserName() -> String! ``` |
| To | ``` func NSFullUserName() -> String ``` |

Modified [NSGetUncaughtExceptionHandler() -> ((NSException) -> Void)?](https://developer.apple.com/documentation/foundation/1416853-nsgetuncaughtexceptionhandler)

|  | Declaration |
| --- | --- |
| From | ``` func NSGetUncaughtExceptionHandler() -> CFunctionPointer<NSUncaughtExceptionHandler> ``` |
| To | ``` func NSGetUncaughtExceptionHandler() -> ((NSException) -> Void)? ``` |

Modified [NSHashTableCopyIn](https://developer.apple.com/documentation/foundation/nshashtablecopyin)

|  | Declaration |
| --- | --- |
| From | ``` var NSHashTableCopyIn: Int { get } ``` |
| To | ``` let NSHashTableCopyIn: NSPointerFunctionsOptions ``` |

Modified [NSHashTableObjectPointerPersonality](https://developer.apple.com/documentation/foundation/nshashtableobjectpointerpersonality)

|  | Declaration |
| --- | --- |
| From | ``` var NSHashTableObjectPointerPersonality: Int { get } ``` |
| To | ``` let NSHashTableObjectPointerPersonality: NSPointerFunctionsOptions ``` |

Modified [NSHashTableStrongMemory](https://developer.apple.com/documentation/foundation/nshashtablestrongmemory)

|  | Declaration |
| --- | --- |
| From | ``` var NSHashTableStrongMemory: Int { get } ``` |
| To | ``` let NSHashTableStrongMemory: NSPointerFunctionsOptions ``` |

Modified [NSHashTableWeakMemory](https://developer.apple.com/documentation/foundation/nshashtableweakmemory)

|  | Declaration |
| --- | --- |
| From | ``` var NSHashTableWeakMemory: Int { get } ``` |
| To | ``` let NSHashTableWeakMemory: NSPointerFunctionsOptions ``` |

Modified [NSHomeDirectory() -> String](https://developer.apple.com/documentation/foundation/1413045-nshomedirectory)

|  | Declaration |
| --- | --- |
| From | ``` func NSHomeDirectory() -> String! ``` |
| To | ``` func NSHomeDirectory() -> String ``` |

Modified [NSHomeDirectoryForUser(_: String?) -> String?](https://developer.apple.com/documentation/foundation/1413447-nshomedirectoryforuser)

|  | Declaration |
| --- | --- |
| From | ``` func NSHomeDirectoryForUser(_ userName: String!) -> String! ``` |
| To | ``` func NSHomeDirectoryForUser(_ userName: String?) -> String? ``` |

Modified [NSISO2022JPStringEncoding](https://developer.apple.com/documentation/foundation/1497293-anonymous/nsiso2022jpstringencoding)

|  | Declaration |
| --- | --- |
| From | ``` var NSISO2022JPStringEncoding: UInt32 { get } ``` |
| To | ``` var NSISO2022JPStringEncoding: UInt { get } ``` |

Modified [NSISOLatin1StringEncoding](https://developer.apple.com/documentation/foundation/1497293-anonymous/nsisolatin1stringencoding)

|  | Declaration |
| --- | --- |
| From | ``` var NSISOLatin1StringEncoding: UInt32 { get } ``` |
| To | ``` var NSISOLatin1StringEncoding: UInt { get } ``` |

Modified [NSISOLatin2StringEncoding](https://developer.apple.com/documentation/foundation/nsisolatin2stringencoding)

|  | Declaration |
| --- | --- |
| From | ``` var NSISOLatin2StringEncoding: UInt32 { get } ``` |
| To | ``` var NSISOLatin2StringEncoding: UInt { get } ``` |

Modified [NSItemProviderCompletionHandler](https://developer.apple.com/documentation/foundation/nsitemprovider/completionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias NSItemProviderCompletionHandler = (NSSecureCoding!, NSError!) -> Void ``` |
| To | ``` typealias NSItemProviderCompletionHandler = (NSSecureCoding?, NSError!) -> Void ``` |

Modified [NSJapaneseEUCStringEncoding](https://developer.apple.com/documentation/foundation/nsjapaneseeucstringencoding)

|  | Declaration |
| --- | --- |
| From | ``` var NSJapaneseEUCStringEncoding: UInt32 { get } ``` |
| To | ``` var NSJapaneseEUCStringEncoding: UInt { get } ``` |

Modified [NSLocalizedString(_: String, tableName: String?, bundle: NSBundle, value: String, comment: String) -> String](https://developer.apple.com/documentation/foundation/1418095-nslocalizedstring)

|  | Declaration |
| --- | --- |
| From | ``` func NSLocalizedString(_ key: String, tableName tableName: String? = default, bundle bundle: NSBundle = default, value value: String = default, comment comment: String) -> String ``` |
| To | ``` @warn_unused_result func NSLocalizedString(_ key: String, tableName tableName: String? = default, bundle bundle: NSBundle = default, value value: String = default, comment comment: String) -> String ``` |

Modified [NSLogv(_: String, _: CVaListPointer)](https://developer.apple.com/documentation/foundation/1395074-nslogv)

|  | Declaration |
| --- | --- |
| From | ``` func NSLogv(_ format: String!, _ args: CVaListPointer) ``` |
| To | ``` func NSLogv(_ format: String, _ args: CVaListPointer) ``` |

Modified [NSMacOSRomanStringEncoding](https://developer.apple.com/documentation/foundation/nsmacosromanstringencoding)

|  | Declaration |
| --- | --- |
| From | ``` var NSMacOSRomanStringEncoding: UInt32 { get } ``` |
| To | ``` var NSMacOSRomanStringEncoding: UInt { get } ``` |

Modified [NSMapTableCopyIn](https://developer.apple.com/documentation/foundation/nsmaptablecopyin)

|  | Declaration |
| --- | --- |
| From | ``` var NSMapTableCopyIn: Int { get } ``` |
| To | ``` let NSMapTableCopyIn: NSPointerFunctionsOptions ``` |

Modified [NSMapTableObjectPointerPersonality](https://developer.apple.com/documentation/foundation/nsmaptableobjectpointerpersonality)

|  | Declaration |
| --- | --- |
| From | ``` var NSMapTableObjectPointerPersonality: Int { get } ``` |
| To | ``` let NSMapTableObjectPointerPersonality: NSPointerFunctionsOptions ``` |

Modified [NSMapTableStrongMemory](https://developer.apple.com/documentation/foundation/nsmaptablestrongmemory)

|  | Declaration |
| --- | --- |
| From | ``` var NSMapTableStrongMemory: Int { get } ``` |
| To | ``` let NSMapTableStrongMemory: NSPointerFunctionsOptions ``` |

Modified [NSMapTableWeakMemory](https://developer.apple.com/documentation/foundation/nsmaptableweakmemory)

|  | Declaration |
| --- | --- |
| From | ``` var NSMapTableWeakMemory: Int { get } ``` |
| To | ``` let NSMapTableWeakMemory: NSPointerFunctionsOptions ``` |

Modified [NSNEXTSTEPStringEncoding](https://developer.apple.com/documentation/foundation/1497293-anonymous/nsnextstepstringencoding)

|  | Declaration |
| --- | --- |
| From | ``` var NSNEXTSTEPStringEncoding: UInt32 { get } ``` |
| To | ``` var NSNEXTSTEPStringEncoding: UInt { get } ``` |

Modified [NSNonLossyASCIIStringEncoding](https://developer.apple.com/documentation/foundation/nsnonlossyasciistringencoding)

|  | Declaration |
| --- | --- |
| From | ``` var NSNonLossyASCIIStringEncoding: UInt32 { get } ``` |
| To | ``` var NSNonLossyASCIIStringEncoding: UInt { get } ``` |

Modified [NSNotFound](https://developer.apple.com/documentation/foundation/nsnotfound)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var NSNotFound: Int { get } ``` | iOS 8.0 |
| To | ``` let NSNotFound: Int ``` | iOS 9.0 |

Modified [NSOpenStepRootDirectory() -> String](https://developer.apple.com/documentation/foundation/1414132-nsopensteprootdirectory)

|  | Declaration |
| --- | --- |
| From | ``` func NSOpenStepRootDirectory() -> String! ``` |
| To | ``` func NSOpenStepRootDirectory() -> String ``` |

Modified [NSOperationQueueDefaultMaxConcurrentOperationCount](https://developer.apple.com/documentation/foundation/nsoperationqueuedefaultmaxconcurrentoperationcount)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var NSOperationQueueDefaultMaxConcurrentOperationCount: Int { get } ``` | iOS 8.0 |
| To | ``` let NSOperationQueueDefaultMaxConcurrentOperationCount: Int ``` | iOS 9.0 |

Modified [NSProgressPublishingHandler](https://developer.apple.com/documentation/foundation/nsprogresspublishinghandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias NSProgressPublishingHandler = (NSProgress!) -> NSProgressUnpublishingHandler! ``` |
| To | ``` typealias NSProgressPublishingHandler = (NSProgress) -> NSProgressUnpublishingHandler? ``` |

Modified [NSPropertyListReadOptions](https://developer.apple.com/documentation/foundation/nspropertylistreadoptions)

|  | Declaration |
| --- | --- |
| From | ``` typealias NSPropertyListReadOptions = Int ``` |
| To | ``` typealias NSPropertyListReadOptions = NSPropertyListMutabilityOptions ``` |

Modified [NSProprietaryStringEncoding](https://developer.apple.com/documentation/foundation/nsproprietarystringencoding)

|  | Declaration |
| --- | --- |
| From | ``` var NSProprietaryStringEncoding: Int { get } ``` |
| To | ``` var NSProprietaryStringEncoding: UInt { get } ``` |

Modified [NSProtocolFromString(_: String) -> Protocol?](https://developer.apple.com/documentation/foundation/1395147-nsprotocolfromstring)

|  | Declaration |
| --- | --- |
| From | ``` func NSProtocolFromString(_ namestr: String!) -> Protocol! ``` |
| To | ``` func NSProtocolFromString(_ namestr: String) -> Protocol? ``` |

Modified [NSRangeFromString(_: String) -> NSRange](https://developer.apple.com/documentation/foundation/1408420-nsrangefromstring)

|  | Declaration |
| --- | --- |
| From | ``` func NSRangeFromString(_ aString: String!) -> NSRange ``` |
| To | ``` func NSRangeFromString(_ aString: String) -> NSRange ``` |

Modified [NSSearchPathForDirectoriesInDomains(_: NSSearchPathDirectory, _: NSSearchPathDomainMask, _: Bool) -> [String]](https://developer.apple.com/documentation/foundation/1414224-nssearchpathfordirectoriesindoma)

|  | Declaration |
| --- | --- |
| From | ``` func NSSearchPathForDirectoriesInDomains(_ directory: NSSearchPathDirectory, _ domainMask: NSSearchPathDomainMask, _ expandTilde: Bool) -> [AnyObject]! ``` |
| To | ``` func NSSearchPathForDirectoriesInDomains(_ directory: NSSearchPathDirectory, _ domainMask: NSSearchPathDomainMask, _ expandTilde: Bool) -> [String] ``` |

Modified [NSSelectorFromString(_: String) -> Selector](https://developer.apple.com/documentation/foundation/1395294-nsselectorfromstring)

|  | Declaration |
| --- | --- |
| From | ``` func NSSelectorFromString(_ aSelectorName: String!) -> Selector ``` |
| To | ``` func NSSelectorFromString(_ aSelectorName: String) -> Selector ``` |

Modified [NSSetUncaughtExceptionHandler(_: ((NSException) -> Void)?)](https://developer.apple.com/documentation/foundation/1409609-nssetuncaughtexceptionhandler)

|  | Declaration |
| --- | --- |
| From | ``` func NSSetUncaughtExceptionHandler(_ _: CFunctionPointer<NSUncaughtExceptionHandler>) ``` |
| To | ``` func NSSetUncaughtExceptionHandler(_ _: ((NSException) -> Void)?) ``` |

Modified [NSShiftJISStringEncoding](https://developer.apple.com/documentation/foundation/nsshiftjisstringencoding)

|  | Declaration |
| --- | --- |
| From | ``` var NSShiftJISStringEncoding: UInt32 { get } ``` |
| To | ``` var NSShiftJISStringEncoding: UInt { get } ``` |

Modified [NSStringFromClass(_: AnyClass) -> String](https://developer.apple.com/documentation/foundation/1395143-nsstringfromclass)

|  | Declaration |
| --- | --- |
| From | ``` func NSStringFromClass(_ aClass: AnyClass!) -> String! ``` |
| To | ``` func NSStringFromClass(_ aClass: AnyClass) -> String ``` |

Modified [NSStringFromProtocol(_: Protocol) -> String](https://developer.apple.com/documentation/foundation/1395298-nsstringfromprotocol)

|  | Declaration |
| --- | --- |
| From | ``` func NSStringFromProtocol(_ proto: Protocol!) -> String! ``` |
| To | ``` func NSStringFromProtocol(_ proto: Protocol) -> String ``` |

Modified [NSStringFromRange(_: NSRange) -> String](https://developer.apple.com/documentation/foundation/1415155-nsstringfromrange)

|  | Declaration |
| --- | --- |
| From | ``` func NSStringFromRange(_ range: NSRange) -> String! ``` |
| To | ``` func NSStringFromRange(_ range: NSRange) -> String ``` |

Modified [NSStringFromSelector(_: Selector) -> String](https://developer.apple.com/documentation/foundation/1395257-nsstringfromselector)

|  | Declaration |
| --- | --- |
| From | ``` func NSStringFromSelector(_ aSelector: Selector) -> String! ``` |
| To | ``` func NSStringFromSelector(_ aSelector: Selector) -> String ``` |

Modified [NSSymbolStringEncoding](https://developer.apple.com/documentation/foundation/1497293-anonymous/nssymbolstringencoding)

|  | Declaration |
| --- | --- |
| From | ``` var NSSymbolStringEncoding: UInt32 { get } ``` |
| To | ``` var NSSymbolStringEncoding: UInt { get } ``` |

Modified [NSTemporaryDirectory() -> String](https://developer.apple.com/documentation/foundation/1409211-nstemporarydirectory)

|  | Declaration |
| --- | --- |
| From | ``` func NSTemporaryDirectory() -> String! ``` |
| To | ``` func NSTemporaryDirectory() -> String ``` |

Modified [NSTextCheckingAllCustomTypes](https://developer.apple.com/documentation/foundation/1476845-anonymous/nstextcheckingallcustomtypes)

|  | Declaration |
| --- | --- |
| From | ``` var NSTextCheckingAllCustomTypes: UInt64 { get } ``` |
| To | ``` var NSTextCheckingAllCustomTypes: NSTextCheckingTypes { get } ``` |

Modified [NSTextCheckingAllSystemTypes](https://developer.apple.com/documentation/foundation/1476845-anonymous/nstextcheckingallsystemtypes)

|  | Declaration |
| --- | --- |
| From | ``` var NSTextCheckingAllSystemTypes: UInt64 { get } ``` |
| To | ``` var NSTextCheckingAllSystemTypes: NSTextCheckingTypes { get } ``` |

Modified [NSTextCheckingAllTypes](https://developer.apple.com/documentation/foundation/nstextcheckingalltypes)

|  | Declaration |
| --- | --- |
| From | ``` var NSTextCheckingAllTypes: UInt64 { get } ``` |
| To | ``` var NSTextCheckingAllTypes: NSTextCheckingTypes { get } ``` |

Modified [NSUncaughtExceptionHandler](https://developer.apple.com/documentation/foundation/nsuncaughtexceptionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias NSUncaughtExceptionHandler = (NSException!) -> Void ``` |
| To | ``` typealias NSUncaughtExceptionHandler = (NSException) -> Void ``` |

Modified [NSUndoCloseGroupingRunLoopOrdering](https://developer.apple.com/documentation/foundation/nsundoclosegroupingrunloopordering)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var NSUndoCloseGroupingRunLoopOrdering: Int { get } ``` | iOS 8.0 |
| To | ``` let NSUndoCloseGroupingRunLoopOrdering: Int ``` | iOS 9.0 |

Modified [NSUnicodeStringEncoding](https://developer.apple.com/documentation/foundation/1497293-anonymous/nsunicodestringencoding)

|  | Declaration |
| --- | --- |
| From | ``` var NSUnicodeStringEncoding: UInt32 { get } ``` |
| To | ``` var NSUnicodeStringEncoding: UInt { get } ``` |

Modified [NSUserName() -> String](https://developer.apple.com/documentation/foundation/1414297-nsusername)

|  | Declaration |
| --- | --- |
| From | ``` func NSUserName() -> String! ``` |
| To | ``` func NSUserName() -> String ``` |

Modified [NSUTF16BigEndianStringEncoding](https://developer.apple.com/documentation/foundation/1497293-anonymous/nsutf16bigendianstringencoding)

|  | Declaration |
| --- | --- |
| From | ``` var NSUTF16BigEndianStringEncoding: UInt32 { get } ``` |
| To | ``` var NSUTF16BigEndianStringEncoding: UInt { get } ``` |

Modified [NSUTF16LittleEndianStringEncoding](https://developer.apple.com/documentation/foundation/1497293-anonymous/nsutf16littleendianstringencoding)

|  | Declaration |
| --- | --- |
| From | ``` var NSUTF16LittleEndianStringEncoding: UInt32 { get } ``` |
| To | ``` var NSUTF16LittleEndianStringEncoding: UInt { get } ``` |

Modified [NSUTF16StringEncoding](https://developer.apple.com/documentation/foundation/1497293-anonymous/nsutf16stringencoding)

|  | Declaration |
| --- | --- |
| From | ``` var NSUTF16StringEncoding: UInt32 { get } ``` |
| To | ``` var NSUTF16StringEncoding: UInt { get } ``` |

Modified [NSUTF32BigEndianStringEncoding](https://developer.apple.com/documentation/foundation/1497293-anonymous/nsutf32bigendianstringencoding)

|  | Declaration |
| --- | --- |
| From | ``` var NSUTF32BigEndianStringEncoding: UInt32 { get } ``` |
| To | ``` var NSUTF32BigEndianStringEncoding: UInt { get } ``` |

Modified [NSUTF32LittleEndianStringEncoding](https://developer.apple.com/documentation/foundation/1497293-anonymous/nsutf32littleendianstringencoding)

|  | Declaration |
| --- | --- |
| From | ``` var NSUTF32LittleEndianStringEncoding: UInt32 { get } ``` |
| To | ``` var NSUTF32LittleEndianStringEncoding: UInt { get } ``` |

Modified [NSUTF32StringEncoding](https://developer.apple.com/documentation/foundation/1497293-anonymous/nsutf32stringencoding)

|  | Declaration |
| --- | --- |
| From | ``` var NSUTF32StringEncoding: UInt32 { get } ``` |
| To | ``` var NSUTF32StringEncoding: UInt { get } ``` |

Modified [NSUTF8StringEncoding](https://developer.apple.com/documentation/foundation/nsutf8stringencoding)

|  | Declaration |
| --- | --- |
| From | ``` var NSUTF8StringEncoding: UInt32 { get } ``` |
| To | ``` var NSUTF8StringEncoding: UInt { get } ``` |

Modified [NSWindowsCP1250StringEncoding](https://developer.apple.com/documentation/foundation/nswindowscp1250stringencoding)

|  | Declaration |
| --- | --- |
| From | ``` var NSWindowsCP1250StringEncoding: UInt32 { get } ``` |
| To | ``` var NSWindowsCP1250StringEncoding: UInt { get } ``` |

Modified [NSWindowsCP1251StringEncoding](https://developer.apple.com/documentation/foundation/nswindowscp1251stringencoding)

|  | Declaration |
| --- | --- |
| From | ``` var NSWindowsCP1251StringEncoding: UInt32 { get } ``` |
| To | ``` var NSWindowsCP1251StringEncoding: UInt { get } ``` |

Modified [NSWindowsCP1252StringEncoding](https://developer.apple.com/documentation/foundation/1497293-anonymous/nswindowscp1252stringencoding)

|  | Declaration |
| --- | --- |
| From | ``` var NSWindowsCP1252StringEncoding: UInt32 { get } ``` |
| To | ``` var NSWindowsCP1252StringEncoding: UInt { get } ``` |

Modified [NSWindowsCP1253StringEncoding](https://developer.apple.com/documentation/foundation/1497293-anonymous/nswindowscp1253stringencoding)

|  | Declaration |
| --- | --- |
| From | ``` var NSWindowsCP1253StringEncoding: UInt32 { get } ``` |
| To | ``` var NSWindowsCP1253StringEncoding: UInt { get } ``` |

Modified [NSWindowsCP1254StringEncoding](https://developer.apple.com/documentation/foundation/nswindowscp1254stringencoding)

|  | Declaration |
| --- | --- |
| From | ``` var NSWindowsCP1254StringEncoding: UInt32 { get } ``` |
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
