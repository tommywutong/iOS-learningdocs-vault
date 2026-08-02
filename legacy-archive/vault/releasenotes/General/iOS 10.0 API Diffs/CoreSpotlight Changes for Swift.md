---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/CoreSpotlight.html
archived_at: '2026-07-18T02:55:16.568441Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# CoreSpotlight Changes for Swift

### CoreSpotlight

Added [CSIndexError [struct]](https://developer.apple.com/documentation/corespotlight/csindexerror)Added [CSIndexError.indexingUnsupported](https://developer.apple.com/documentation/corespotlight/csindexerror/2340123-indexingunsupported)Added [CSIndexError.indexUnavailableError](https://developer.apple.com/documentation/corespotlight/csindexerror/2340131-indexunavailableerror)Added CSIndexError.init(_nsError: NSError)Added [CSIndexError.invalidClientStateError](https://developer.apple.com/documentation/corespotlight/csindexerror/2340125-invalidclientstateerror)Added [CSIndexError.invalidItemError](https://developer.apple.com/documentation/corespotlight/csindexerror/2340126-invaliditemerror)Added [CSIndexError.quotaExceeded](https://developer.apple.com/documentation/corespotlight/csindexerror/2340129-quotaexceeded)Added [CSIndexError.remoteConnectionError](https://developer.apple.com/documentation/corespotlight/csindexerror/2340130-remoteconnectionerror)Added [CSIndexError.unknownError](https://developer.apple.com/documentation/corespotlight/csindexerror/2340121-unknownerror)Added [CSSearchableItemAttributeSet.domainIdentifier](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1649285-domainidentifier)Added [CSSearchableItemAttributeSet.fullyFormattedAddress](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1649301-fullyformattedaddress)Added [CSSearchableItemAttributeSet.postalCode](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1649284-postalcode)Added [CSSearchableItemAttributeSet.subThoroughfare](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1649290-subthoroughfare)Added [CSSearchableItemAttributeSet.thoroughfare](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1649310-thoroughfare)Added [CSSearchableItemAttributeSet.weakRelatedUniqueIdentifier](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1649297-weakrelateduniqueidentifier)Added [CSSearchQuery](https://developer.apple.com/documentation/corespotlight/cssearchquery)Added [CSSearchQuery.cancel()](https://developer.apple.com/documentation/corespotlight/cssearchquery/1649309-cancel)Added [CSSearchQuery.completionHandler](https://developer.apple.com/documentation/corespotlight/cssearchquery/1649312-completionhandler)Added [CSSearchQuery.foundItemCount](https://developer.apple.com/documentation/corespotlight/cssearchquery/1649300-founditemcount)Added [CSSearchQuery.foundItemsHandler](https://developer.apple.com/documentation/corespotlight/cssearchquery/1649306-founditemshandler)Added [CSSearchQuery.init(queryString: String, attributes: [String]?)](https://developer.apple.com/documentation/corespotlight/cssearchquery/1649308-initwithquerystring)Added [CSSearchQuery.isCancelled](https://developer.apple.com/documentation/corespotlight/cssearchquery/1649294-iscancelled)Added [CSSearchQuery.protectionClasses](https://developer.apple.com/documentation/corespotlight/cssearchquery/1649311-protectionclasses)Added [CSSearchQuery.start()](https://developer.apple.com/documentation/corespotlight/cssearchquery/1649296-start)Added [CSSearchQueryError [struct]](https://developer.apple.com/documentation/corespotlight/cssearchqueryerror)Added [CSSearchQueryError.cancelled](https://developer.apple.com/documentation/corespotlight/cssearchqueryerror/2340124-cancelled)Added [CSSearchQueryError.indexUnreachable](https://developer.apple.com/documentation/corespotlight/cssearchqueryerror/2340128-indexunreachable)Added CSSearchQueryError.init(_nsError: NSError)Added [CSSearchQueryError.invalidQuery](https://developer.apple.com/documentation/corespotlight/cssearchqueryerror/2340127-invalidquery)Added [CSSearchQueryError.unknown](https://developer.apple.com/documentation/corespotlight/cssearchqueryerror/2340122-unknown)Added [CSSearchQueryError.Code [enum]](https://developer.apple.com/documentation/corespotlight/cssearchqueryerror/code)Added [CSSearchQueryError.Code.cancelled](https://developer.apple.com/documentation/corespotlight/cssearchqueryerror/code/cancelled)Added [CSSearchQueryError.Code.indexUnreachable](https://developer.apple.com/documentation/corespotlight/cssearchqueryerror/code/indexunreachable)Added [CSSearchQueryError.Code.invalidQuery](https://developer.apple.com/documentation/corespotlight/cssearchqueryerror/code/invalidquery)Added [CSSearchQueryError.Code.unknown](https://developer.apple.com/documentation/corespotlight/cssearchqueryerrorcode/cssearchqueryerrorcodeunknown)Added [CSQueryContinuationActionType](https://developer.apple.com/documentation/corespotlight/csquerycontinuationactiontype)Added [CSSearchQueryErrorDomain](https://developer.apple.com/documentation/corespotlight/cssearchqueryerrordomain)Added [CSSearchQueryString](https://developer.apple.com/documentation/corespotlight/cssearchquerystring)Modified [CSCustomAttributeKey](https://developer.apple.com/documentation/corespotlight/cscustomattributekey)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CSCustomAttributeKey : NSObject, NSCopying, NSSecureCoding {     convenience init?(keyName keyName: String)     init?(keyName keyName: String, searchable searchable: Bool, searchableByDefault searchableByDefault: Bool, unique unique: Bool, multiValued multiValued: Bool)     var keyName: String { get }     var searchable: Bool { get }     var searchableByDefault: Bool { get }     var unique: Bool { get }     var multiValued: Bool { get } } ``` | NSCopying, NSSecureCoding |
| To | ``` class CSCustomAttributeKey : NSObject, NSCopying, NSSecureCoding {     convenience init()     convenience init?(keyName keyName: String)     init?(keyName keyName: String, searchable searchable: Bool, searchableByDefault searchableByDefault: Bool, unique unique: Bool, multiValued multiValued: Bool)     var keyName: String { get }     var isSearchable: Bool { get }     var isSearchableByDefault: Bool { get }     var isUnique: Bool { get }     var isMultiValued: Bool { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CSCustomAttributeKey : CVarArg { } extension CSCustomAttributeKey : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [CSCustomAttributeKey.isMultiValued](https://developer.apple.com/documentation/corespotlight/cscustomattributekey/1616400-multivalued)

|  | Declaration |
| --- | --- |
| From | ``` var multiValued: Bool { get } ``` |
| To | ``` var isMultiValued: Bool { get } ``` |

Modified [CSCustomAttributeKey.isSearchable](https://developer.apple.com/documentation/corespotlight/cscustomattributekey/1616397-searchable)

|  | Declaration |
| --- | --- |
| From | ``` var searchable: Bool { get } ``` |
| To | ``` var isSearchable: Bool { get } ``` |

Modified [CSCustomAttributeKey.isSearchableByDefault](https://developer.apple.com/documentation/corespotlight/cscustomattributekey/1616396-issearchablebydefault)

|  | Declaration |
| --- | --- |
| From | ``` var searchableByDefault: Bool { get } ``` |
| To | ``` var isSearchableByDefault: Bool { get } ``` |

Modified [CSCustomAttributeKey.isUnique](https://developer.apple.com/documentation/corespotlight/cscustomattributekey/1616409-unique)

|  | Declaration |
| --- | --- |
| From | ``` var unique: Bool { get } ``` |
| To | ``` var isUnique: Bool { get } ``` |

Modified [CSIndexError.Code [enum]](https://developer.apple.com/documentation/corespotlight/csindexerror/code)

|  | Declaration |
| --- | --- |
| From | ``` enum CSIndexErrorCode : Int {     case UnknownError     case IndexUnavailableError     case InvalidItemError     case InvalidClientStateError     case RemoteConnectionError     case QuotaExceeded     case IndexingUnsupported } ``` |
| To | ``` enum Code : Int {         typealias _ErrorType = CSIndexError         case unknownError         case indexUnavailableError         case invalidItemError         case invalidClientStateError         case remoteConnectionError         case quotaExceeded         case indexingUnsupported     } ``` |

Modified [CSIndexError.Code.indexingUnsupported](https://developer.apple.com/documentation/corespotlight/csindexerrorcode/csindexerrorcodeindexingunsupported)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case IndexingUnsupported ``` | iOS 9.0 |
| To | ``` case indexingUnsupported ``` | iOS 10.0 |

Modified [CSIndexError.Code.indexUnavailableError](https://developer.apple.com/documentation/corespotlight/csindexerrorcode/csindexerrorcodeindexunavailableerror)

|  | Declaration |
| --- | --- |
| From | ``` case IndexUnavailableError ``` |
| To | ``` case indexUnavailableError ``` |

Modified [CSIndexError.Code.invalidClientStateError](https://developer.apple.com/documentation/corespotlight/csindexerror/code/invalidclientstateerror)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case InvalidClientStateError ``` | iOS 9.0 |
| To | ``` case invalidClientStateError ``` | iOS 10.0 |

Modified [CSIndexError.Code.invalidItemError](https://developer.apple.com/documentation/corespotlight/csindexerror/code/invaliditemerror)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case InvalidItemError ``` | iOS 9.0 |
| To | ``` case invalidItemError ``` | iOS 10.0 |

Modified [CSIndexError.Code.quotaExceeded](https://developer.apple.com/documentation/corespotlight/csindexerror/code/quotaexceeded)

|  | Declaration |
| --- | --- |
| From | ``` case QuotaExceeded ``` |
| To | ``` case quotaExceeded ``` |

Modified [CSIndexError.Code.remoteConnectionError](https://developer.apple.com/documentation/corespotlight/csindexerrorcode/csindexerrorcoderemoteconnectionerror)

|  | Declaration |
| --- | --- |
| From | ``` case RemoteConnectionError ``` |
| To | ``` case remoteConnectionError ``` |

Modified [CSIndexError.Code.unknownError](https://developer.apple.com/documentation/corespotlight/csindexerrorcode/csindexerrorcodeunknownerror)

|  | Declaration |
| --- | --- |
| From | ``` case UnknownError ``` |
| To | ``` case unknownError ``` |

Modified [CSIndexExtensionRequestHandler](https://developer.apple.com/documentation/corespotlight/csindexextensionrequesthandler)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CSIndexExtensionRequestHandler : NSObject, NSExtensionRequestHandling, CSSearchableIndexDelegate { } ``` | CSSearchableIndexDelegate, NSExtensionRequestHandling |
| To | ``` class CSIndexExtensionRequestHandler : NSObject, NSExtensionRequestHandling, CSSearchableIndexDelegate {     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CSIndexExtensionRequestHandler : CVarArg { } extension CSIndexExtensionRequestHandler : Equatable, Hashable {     var hashValue: Int { get } } ``` | CSSearchableIndexDelegate, CVarArg, Equatable, Hashable, NSExtensionRequestHandling |

Modified [CSLocalizedString](https://developer.apple.com/documentation/corespotlight/cslocalizedstring)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CSLocalizedString : NSString {     init(localizedStrings localizedStrings: [NSObject : AnyObject])     func localizedString() -> String } ``` | -- |
| To | ``` class CSLocalizedString : NSString {     init(localizedStrings localizedStrings: [AnyHashable : Any])     func localizedString() -> String     convenience init(format format: NSString, _ args: CVarArg...)     convenience init(format format: NSString, locale locale: Locale?, _ args: CVarArg...)     class func localizedStringWithFormat(_ format: NSString, _ args: CVarArg...) -> Self     func appendingFormat(_ format: NSString, _ args: CVarArg...) -> NSString     @nonobjc convenience init(string aString: NSString)     func linguisticTags(in range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTagger.Options = [], orthography orthography: NSOrthography?, tokenRanges tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [String]     func enumerateLinguisticTags(in range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTagger.Options = [], orthography orthography: NSOrthography?, using block: (String, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)     func addingPercentEncoding(withAllowedCharacters allowedCharacters: CharacterSet) -> String?     var removingPercentEncoding: String? { get }     func addingPercentEscapes(using enc: UInt) -> String?     func replacingPercentEscapes(using enc: UInt) -> String?     class func path(withComponents components: [String]) -> String     var pathComponents: [String] { get }     var isAbsolutePath: Bool { get }     var lastPathComponent: String { get }     var deletingLastPathComponent: String { get }     func appendingPathComponent(_ str: String) -> String     var pathExtension: String { get }     var deletingPathExtension: String { get }     func appendingPathExtension(_ str: String) -> String?     var abbreviatingWithTildeInPath: String { get }     var expandingTildeInPath: String { get }     var standardizingPath: String { get }     var resolvingSymlinksInPath: String { get }     func strings(byAppendingPaths paths: [String]) -> [String]     func completePath(into outputName: AutoreleasingUnsafeMutablePointer<NSString?>?, caseSensitive flag: Bool, matchesInto outputArray: AutoreleasingUnsafeMutablePointer<NSArray?>?, filterTypes filterTypes: [String]?) -> Int     var fileSystemRepresentation: UnsafePointer<Int8> { get }     func getFileSystemRepresentation(_ cname: UnsafeMutablePointer<Int8>, maxLength max: Int) -> Bool     func variantFittingPresentationWidth(_ width: Int) -> String     func cString() -> UnsafePointer<Int8>?     func lossyCString() -> UnsafePointer<Int8>?     func cStringLength() -> Int     func getCString(_ bytes: UnsafeMutablePointer<Int8>)     func getCString(_ bytes: UnsafeMutablePointer<Int8>, maxLength maxLength: Int)     func getCString(_ bytes: UnsafeMutablePointer<Int8>, maxLength maxLength: Int, range aRange: NSRange, remaining leftoverRange: NSRangePointer?)     func write(toFile path: String, atomically useAuxiliaryFile: Bool) -> Bool     func write(to url: URL, atomically atomically: Bool) -> Bool     convenience init?(contentsOfFile path: String)     convenience init?(contentsOf url: URL)     class func string(withContentsOfFile path: String) -> Any?     class func string(withContentsOf url: URL) -> Any?     convenience init?(cStringNoCopy bytes: UnsafeMutablePointer<Int8>, length length: Int, freeWhenDone freeBuffer: Bool)     convenience init?(cString bytes: UnsafePointer<Int8>, length length: Int)     convenience init?(cString bytes: UnsafePointer<Int8>)     class func string(withCString bytes: UnsafePointer<Int8>, length length: Int) -> Any?     class func string(withCString bytes: UnsafePointer<Int8>) -> Any?     func getCharacters(_ buffer: UnsafeMutablePointer<unichar>)     func propertyList() -> Any     func propertyListFromStringsFileFormat() -> [AnyHashable : Any]?     class func stringEncoding(for data: Data, encodingOptions opts: [StringEncodingDetectionOptionsKey : Any]? = nil, convertedString string: AutoreleasingUnsafeMutablePointer<NSString?>?, usedLossyConversion usedLossyConversion: UnsafeMutablePointer<ObjCBool>?) -> UInt     func substring(from from: Int) -> String     func substring(to to: Int) -> String     func substring(with range: NSRange) -> String     func getCharacters(_ buffer: UnsafeMutablePointer<unichar>, range range: NSRange)     func compare(_ string: String) -> ComparisonResult     func compare(_ string: String, options mask: NSString.CompareOptions = []) -> ComparisonResult     func compare(_ string: String, options mask: NSString.CompareOptions = [], range rangeOfReceiverToCompare: NSRange) -> ComparisonResult     func compare(_ string: String, options mask: NSString.CompareOptions = [], range rangeOfReceiverToCompare: NSRange, locale locale: Any?) -> ComparisonResult     func caseInsensitiveCompare(_ string: String) -> ComparisonResult     func localizedCompare(_ string: String) -> ComparisonResult     func localizedCaseInsensitiveCompare(_ string: String) -> ComparisonResult     func localizedStandardCompare(_ string: String) -> ComparisonResult     func isEqual(to aString: String) -> Bool     func hasPrefix(_ str: String) -> Bool     func hasSuffix(_ str: String) -> Bool     func commonPrefix(with str: String, options mask: NSString.CompareOptions = []) -> String     func contains(_ str: String) -> Bool     func localizedCaseInsensitiveContains(_ str: String) -> Bool     func localizedStandardContains(_ str: String) -> Bool     func localizedStandardRange(of str: String) -> NSRange     func range(of searchString: String) -> NSRange     func range(of searchString: String, options mask: NSString.CompareOptions = []) -> NSRange     func range(of searchString: String, options mask: NSString.CompareOptions = [], range rangeOfReceiverToSearch: NSRange) -> NSRange     func range(of searchString: String, options mask: NSString.CompareOptions = [], range rangeOfReceiverToSearch: NSRange, locale locale: Locale?) -> NSRange     func rangeOfCharacter(from searchSet: CharacterSet) -> NSRange     func rangeOfCharacter(from searchSet: CharacterSet, options mask: NSString.CompareOptions = []) -> NSRange     func rangeOfCharacter(from searchSet: CharacterSet, options mask: NSString.CompareOptions = [], range rangeOfReceiverToSearch: NSRange) -> NSRange     func rangeOfComposedCharacterSequence(at index: Int) -> NSRange     func rangeOfComposedCharacterSequences(for range: NSRange) -> NSRange     func appending(_ aString: String) -> String     var doubleValue: Double { get }     var floatValue: Float { get }     var intValue: Int32 { get }     var integerValue: Int { get }     var longLongValue: Int64 { get }     var boolValue: Bool { get }     var uppercased: String { get }     var lowercased: String { get }     var capitalized: String { get }     var localizedUppercase: String { get }     var localizedLowercase: String { get }     var localizedCapitalized: String { get }     func uppercased(with locale: Locale?) -> String     func lowercased(with locale: Locale?) -> String     func capitalized(with locale: Locale?) -> String     func getLineStart(_ startPtr: UnsafeMutablePointer<Int>?, end lineEndPtr: UnsafeMutablePointer<Int>?, contentsEnd contentsEndPtr: UnsafeMutablePointer<Int>?, for range: NSRange)     func lineRange(for range: NSRange) -> NSRange     func getParagraphStart(_ startPtr: UnsafeMutablePointer<Int>?, end parEndPtr: UnsafeMutablePointer<Int>?, contentsEnd contentsEndPtr: UnsafeMutablePointer<Int>?, for range: NSRange)     func paragraphRange(for range: NSRange) -> NSRange     func enumerateSubstrings(in range: NSRange, options opts: NSString.EnumerationOptions = [], using block: @escaping (String?, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateLines(_ block: @escaping (String, UnsafeMutablePointer<ObjCBool>) -> Void)     var utf8String: UnsafePointer<Int8>? { get }     var fastestEncoding: UInt { get }     var smallestEncoding: UInt { get }     func data(using encoding: UInt, allowLossyConversion lossy: Bool) -> Data?     func data(using encoding: UInt) -> Data?     func canBeConverted(to encoding: UInt) -> Bool     func cString(using encoding: UInt) -> UnsafePointer<Int8>?     func getCString(_ buffer: UnsafeMutablePointer<Int8>, maxLength maxBufferCount: Int, encoding encoding: UInt) -> Bool     func getBytes(_ buffer: UnsafeMutableRawPointer?, maxLength maxBufferCount: Int, usedLength usedBufferCount: UnsafeMutablePointer<Int>?, encoding encoding: UInt, options options: NSString.EncodingConversionOptions = [], range range: NSRange, remaining leftover: NSRangePointer?) -> Bool     func maximumLengthOfBytes(using enc: UInt) -> Int     func lengthOfBytes(using enc: UInt) -> Int     class var availableStringEncodings: UnsafePointer<UInt> { get }     class func localizedName(of encoding: UInt) -> String     class var defaultCStringEncoding: UInt { get }     var decomposedStringWithCanonicalMapping: String { get }     var precomposedStringWithCanonicalMapping: String { get }     var decomposedStringWithCompatibilityMapping: String { get }     var precomposedStringWithCompatibilityMapping: String { get }     func components(separatedBy separator: String) -> [String]     func components(separatedBy separator: CharacterSet) -> [String]     func trimmingCharacters(in set: CharacterSet) -> String     func padding(toLength newLength: Int, withPad padString: String, startingAt padIndex: Int) -> String     func folding(options options: NSString.CompareOptions = [], locale locale: Locale?) -> String     func replacingOccurrences(of target: String, with replacement: String, options options: NSString.CompareOptions = [], range searchRange: NSRange) -> String     func replacingOccurrences(of target: String, with replacement: String) -> String     func replacingCharacters(in range: NSRange, with replacement: String) -> String     func applyingTransform(_ transform: StringTransform, reverse reverse: Bool) -> String?     func write(to url: URL, atomically useAuxiliaryFile: Bool, encoding enc: UInt) throws     func write(toFile path: String, atomically useAuxiliaryFile: Bool, encoding enc: UInt) throws     var description: String { get }     var hash: Int { get }     convenience init(charactersNoCopy characters: UnsafeMutablePointer<unichar>, length length: Int, freeWhenDone freeBuffer: Bool)     convenience init(characters characters: UnsafePointer<unichar>, length length: Int)     convenience init?(utf8String nullTerminatedCString: UnsafePointer<Int8>)     convenience init(string aString: String)     convenience init(format format: String, arguments argList: CVaListPointer)     convenience init(format format: String, locale locale: Any?, arguments argList: CVaListPointer)     convenience init?(data data: Data, encoding encoding: UInt)     convenience init?(bytes bytes: UnsafeRawPointer, length len: Int, encoding encoding: UInt)     convenience init?(bytesNoCopy bytes: UnsafeMutableRawPointer, length len: Int, encoding encoding: UInt, freeWhenDone freeBuffer: Bool)     class func string() -> Self     class func withString(_ string: String) -> Self     class func withCharacters(_ characters: UnsafePointer<unichar>, length length: Int) -> Self     class func withUTF8String(_ nullTerminatedCString: UnsafePointer<Int8>) -> Self?     convenience init?(cString nullTerminatedCString: UnsafePointer<Int8>, encoding encoding: UInt)     class func withCString(_ cString: UnsafePointer<Int8>, encoding enc: UInt) -> Self?     convenience init(contentsOf url: URL, encoding enc: UInt) throws     convenience init(contentsOfFile path: String, encoding enc: UInt) throws     class func withContentsOf(_ url: URL, encoding enc: UInt) throws -> Self     class func withContentsOfFile(_ path: String, encoding enc: UInt) throws -> Self     convenience init(contentsOf url: URL, usedEncoding enc: UnsafeMutablePointer<UInt>?) throws     convenience init(contentsOfFile path: String, usedEncoding enc: UnsafeMutablePointer<UInt>?) throws     class func withContentsOf(_ url: URL, usedEncoding enc: UnsafeMutablePointer<UInt>?) throws -> Self     class func withContentsOfFile(_ path: String, usedEncoding enc: UnsafeMutablePointer<UInt>?) throws -> Self     struct CompareOptions : OptionSet {         init(rawValue rawValue: UInt)         static var caseInsensitive: NSString.CompareOptions { get }         static var literal: NSString.CompareOptions { get }         static var backwards: NSString.CompareOptions { get }         static var anchored: NSString.CompareOptions { get }         static var numeric: NSString.CompareOptions { get }         static var diacriticInsensitive: NSString.CompareOptions { get }         static var widthInsensitive: NSString.CompareOptions { get }         static var forcedOrdering: NSString.CompareOptions { get }         static var regularExpression: NSString.CompareOptions { get }     }     struct EncodingConversionOptions : OptionSet {         init(rawValue rawValue: UInt)         static var allowLossy: NSString.EncodingConversionOptions { get }         static var externalRepresentation: NSString.EncodingConversionOptions { get }     }     struct EnumerationOptions : OptionSet {         init(rawValue rawValue: UInt)         static var byLines: NSString.EnumerationOptions { get }         static var byParagraphs: NSString.EnumerationOptions { get }         static var byComposedCharacterSequences: NSString.EnumerationOptions { get }         static var byWords: NSString.EnumerationOptions { get }         static var bySentences: NSString.EnumerationOptions { get }         static var reverse: NSString.EnumerationOptions { get }         static var substringNotRequired: NSString.EnumerationOptions { get }         static var localized: NSString.EnumerationOptions { get }     }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CSLocalizedString : ExpressibleByStringLiteral {     required convenience init(unicodeScalarLiteral value: StaticString)     required convenience init(extendedGraphemeClusterLiteral value: StaticString)     required convenience init(stringLiteral value: StaticString) } extension CSLocalizedString : CustomPlaygroundQuickLookable {     var customPlaygroundQuickLook: PlaygroundQuickLook { get } } extension CSLocalizedString : CVarArg { } extension CSLocalizedString : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, CustomPlaygroundQuickLookable, Equatable, ExpressibleByStringLiteral, Hashable |

Modified [CSLocalizedString.init(localizedStrings: [AnyHashable : Any])](https://developer.apple.com/documentation/corespotlight/cslocalizedstring/1616403-initwithlocalizedstrings)

|  | Declaration |
| --- | --- |
| From | ``` init(localizedStrings localizedStrings: [NSObject : AnyObject]) ``` |
| To | ``` init(localizedStrings localizedStrings: [AnyHashable : Any]) ``` |

Modified [CSPerson](https://developer.apple.com/documentation/corespotlight/csperson)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CSPerson : NSObject, NSSecureCoding, NSCopying {     init(displayName displayName: String?, handles handles: [String], handleIdentifier handleIdentifier: String)     var displayName: String? { get }     var handles: [String] { get }     var handleIdentifier: String { get }     var contactIdentifier: String? } ``` | NSCopying, NSSecureCoding |
| To | ``` class CSPerson : NSObject, NSSecureCoding, NSCopying {     init(displayName displayName: String?, handles handles: [String], handleIdentifier handleIdentifier: String)     var displayName: String? { get }     var handles: [String] { get }     var handleIdentifier: String { get }     var contactIdentifier: String?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CSPerson : CVarArg { } extension CSPerson : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [CSSearchableIndex](https://developer.apple.com/documentation/corespotlight/cssearchableindex)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CSSearchableIndex : NSObject {     weak var indexDelegate: CSSearchableIndexDelegate?     class func isIndexingAvailable() -> Bool     class func defaultSearchableIndex() -> Self     init(name name: String)     init(name name: String, protectionClass protectionClass: String?)     func indexSearchableItems(_ items: [CSSearchableItem], completionHandler completionHandler: ((NSError?) -> Void)?)     func deleteSearchableItemsWithIdentifiers(_ identifiers: [String], completionHandler completionHandler: ((NSError?) -> Void)?)     func deleteSearchableItemsWithDomainIdentifiers(_ domainIdentifiers: [String], completionHandler completionHandler: ((NSError?) -> Void)?)     func deleteAllSearchableItemsWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?) } extension CSSearchableIndex {     func beginIndexBatch()     func endIndexBatchWithClientState(_ clientState: NSData, completionHandler completionHandler: ((NSError?) -> Void)?)     func fetchLastClientStateWithCompletionHandler(_ completionHandler: (NSData?, NSError?) -> Void) } ``` | -- |
| To | ``` class CSSearchableIndex : NSObject {     weak var indexDelegate: CSSearchableIndexDelegate?     class func isIndexingAvailable() -> Bool     class func `default`() -> Self     init(name name: String)     init(name name: String, protectionClass protectionClass: String?)     func indexSearchableItems(_ items: [CSSearchableItem], completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func deleteSearchableItems(withIdentifiers identifiers: [String], completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func deleteSearchableItems(withDomainIdentifiers domainIdentifiers: [String], completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func deleteAllSearchableItems(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func beginBatch()     func endBatch(withClientState clientState: Data, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func fetchLastClientState(completionHandler completionHandler: @escaping (Data?, Error?) -> Swift.Void)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CSSearchableIndex : CVarArg { } extension CSSearchableIndex : Equatable, Hashable {     var hashValue: Int { get } } extension CSSearchableIndex {     func beginBatch()     func endBatch(withClientState clientState: Data, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func fetchLastClientState(completionHandler completionHandler: @escaping (Data?, Error?) -> Swift.Void) } ``` | CVarArg, Equatable, Hashable |

Modified [CSSearchableIndex.beginBatch()](https://developer.apple.com/documentation/corespotlight/cssearchableindex/1620331-beginindexbatch)

|  | Declaration |
| --- | --- |
| From | ``` func beginIndexBatch() ``` |
| To | ``` func beginBatch() ``` |

Modified [CSSearchableIndex.default() [class]](https://developer.apple.com/documentation/corespotlight/cssearchableindex/1620341-defaultsearchableindex)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultSearchableIndex() -> Self ``` |
| To | ``` class func `default`() -> Self ``` |

Modified [CSSearchableIndex.deleteAllSearchableItems(completionHandler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/corespotlight/cssearchableindex/1620342-deleteallsearchableitems)

|  | Declaration |
| --- | --- |
| From | ``` func deleteAllSearchableItemsWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` func deleteAllSearchableItems(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [CSSearchableIndex.deleteSearchableItems(withDomainIdentifiers: [String], completionHandler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/corespotlight/cssearchableindex/1620351-deletesearchableitemswithdomaini)

|  | Declaration |
| --- | --- |
| From | ``` func deleteSearchableItemsWithDomainIdentifiers(_ domainIdentifiers: [String], completionHandler completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` func deleteSearchableItems(withDomainIdentifiers domainIdentifiers: [String], completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [CSSearchableIndex.deleteSearchableItems(withIdentifiers: [String], completionHandler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/corespotlight/cssearchableindex/1620337-deletesearchableitemswithidentif)

|  | Declaration |
| --- | --- |
| From | ``` func deleteSearchableItemsWithIdentifiers(_ identifiers: [String], completionHandler completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` func deleteSearchableItems(withIdentifiers identifiers: [String], completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [CSSearchableIndex.endBatch(withClientState: Data, completionHandler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/corespotlight/cssearchableindex/1620344-endindexbatchwithclientstate)

|  | Declaration |
| --- | --- |
| From | ``` func endIndexBatchWithClientState(_ clientState: NSData, completionHandler completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` func endBatch(withClientState clientState: Data, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [CSSearchableIndex.fetchLastClientState(completionHandler: (Data?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/corespotlight/cssearchableindex/1620346-fetchlastclientstate)

|  | Declaration |
| --- | --- |
| From | ``` func fetchLastClientStateWithCompletionHandler(_ completionHandler: (NSData?, NSError?) -> Void) ``` |
| To | ``` func fetchLastClientState(completionHandler completionHandler: @escaping (Data?, Error?) -> Swift.Void) ``` |

Modified [CSSearchableIndex.indexSearchableItems(_: [CSSearchableItem], completionHandler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/corespotlight/cssearchableindex/1620333-indexsearchableitems)

|  | Declaration |
| --- | --- |
| From | ``` func indexSearchableItems(_ items: [CSSearchableItem], completionHandler completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` func indexSearchableItems(_ items: [CSSearchableItem], completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [CSSearchableIndexDelegate](https://developer.apple.com/documentation/corespotlight/cssearchableindexdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol CSSearchableIndexDelegate : NSObjectProtocol {     func searchableIndex(_ searchableIndex: CSSearchableIndex, reindexAllSearchableItemsWithAcknowledgementHandler acknowledgementHandler: () -> Void)     func searchableIndex(_ searchableIndex: CSSearchableIndex, reindexSearchableItemsWithIdentifiers identifiers: [String], acknowledgementHandler acknowledgementHandler: () -> Void)     optional func searchableIndexDidThrottle(_ searchableIndex: CSSearchableIndex)     optional func searchableIndexDidFinishThrottle(_ searchableIndex: CSSearchableIndex) } ``` |
| To | ``` protocol CSSearchableIndexDelegate : NSObjectProtocol {     func searchableIndex(_ searchableIndex: CSSearchableIndex, reindexAllSearchableItemsWithAcknowledgementHandler acknowledgementHandler: @escaping () -> Swift.Void)     func searchableIndex(_ searchableIndex: CSSearchableIndex, reindexSearchableItemsWithIdentifiers identifiers: [String], acknowledgementHandler acknowledgementHandler: @escaping () -> Swift.Void)     optional func searchableIndexDidThrottle(_ searchableIndex: CSSearchableIndex)     optional func searchableIndexDidFinishThrottle(_ searchableIndex: CSSearchableIndex) } ``` |

Modified [CSSearchableIndexDelegate.searchableIndex(_: CSSearchableIndex, reindexAllSearchableItemsWithAcknowledgementHandler: () -> Swift.Void)](https://developer.apple.com/documentation/corespotlight/cssearchableindexdelegate/1620348-searchableindex)

|  | Declaration |
| --- | --- |
| From | ``` func searchableIndex(_ searchableIndex: CSSearchableIndex, reindexAllSearchableItemsWithAcknowledgementHandler acknowledgementHandler: () -> Void) ``` |
| To | ``` func searchableIndex(_ searchableIndex: CSSearchableIndex, reindexAllSearchableItemsWithAcknowledgementHandler acknowledgementHandler: @escaping () -> Swift.Void) ``` |

Modified [CSSearchableIndexDelegate.searchableIndex(_: CSSearchableIndex, reindexSearchableItemsWithIdentifiers: [String], acknowledgementHandler: () -> Swift.Void)](https://developer.apple.com/documentation/corespotlight/cssearchableindexdelegate/1620338-searchableindex)

|  | Declaration |
| --- | --- |
| From | ``` func searchableIndex(_ searchableIndex: CSSearchableIndex, reindexSearchableItemsWithIdentifiers identifiers: [String], acknowledgementHandler acknowledgementHandler: () -> Void) ``` |
| To | ``` func searchableIndex(_ searchableIndex: CSSearchableIndex, reindexSearchableItemsWithIdentifiers identifiers: [String], acknowledgementHandler acknowledgementHandler: @escaping () -> Swift.Void) ``` |

Modified [CSSearchableItem](https://developer.apple.com/documentation/corespotlight/cssearchableitem)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CSSearchableItem : NSObject, NSSecureCoding, NSCopying {     init(uniqueIdentifier uniqueIdentifier: String?, domainIdentifier domainIdentifier: String?, attributeSet attributeSet: CSSearchableItemAttributeSet)     var uniqueIdentifier: String     var domainIdentifier: String?     @NSCopying var expirationDate: NSDate!     var attributeSet: CSSearchableItemAttributeSet } ``` | NSCopying, NSSecureCoding |
| To | ``` class CSSearchableItem : NSObject, NSSecureCoding, NSCopying {     init(uniqueIdentifier uniqueIdentifier: String?, domainIdentifier domainIdentifier: String?, attributeSet attributeSet: CSSearchableItemAttributeSet)     var uniqueIdentifier: String     var domainIdentifier: String?     var expirationDate: Date!     var attributeSet: CSSearchableItemAttributeSet     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CSSearchableItem : CVarArg { } extension CSSearchableItem : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [CSSearchableItem.expirationDate](https://developer.apple.com/documentation/corespotlight/cssearchableitem/1621680-expirationdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var expirationDate: NSDate! ``` |
| To | ``` var expirationDate: Date! ``` |

Modified [CSSearchableItemAttributeSet](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CSSearchableItemAttributeSet : NSObject, NSCopying, NSSecureCoding {     init(itemContentType itemContentType: String) } extension CSSearchableItemAttributeSet {     func setValue(_ value: NSSecureCoding?, forCustomKey key: CSCustomAttributeKey)     func valueForCustomKey(_ key: CSCustomAttributeKey) -> NSSecureCoding? } extension CSSearchableItemAttributeSet {     var subject: String?     var theme: String?     var contentDescription: String?     var identifier: String?     var audiences: [String]?     var fileSize: NSNumber?     var pageCount: NSNumber?     var pageWidth: NSNumber?     var pageHeight: NSNumber?     var securityMethod: String?     var creator: String?     var encodingApplications: [String]?     var kind: String?     var fontNames: [String]? } extension CSSearchableItemAttributeSet {     var dueDate: NSDate?     var completionDate: NSDate?     var startDate: NSDate?     var endDate: NSDate?     var importantDates: [NSDate]?     @NSCopying var allDay: NSNumber? } extension CSSearchableItemAttributeSet {     var displayName: String?     var alternateNames: [String]?     var path: String?     var contentURL: NSURL?     var thumbnailURL: NSURL?     @NSCopying var thumbnailData: NSData?     var relatedUniqueIdentifier: String?     var metadataModificationDate: NSDate?     var contentType: String?     var contentTypeTree: [String]?     var keywords: [String]?     var title: String? } extension CSSearchableItemAttributeSet {     @NSCopying var supportsPhoneCall: NSNumber?     @NSCopying var supportsNavigation: NSNumber? } extension CSSearchableItemAttributeSet {     var containerTitle: String?     var containerDisplayName: String?     var containerIdentifier: String?     @NSCopying var containerOrder: NSNumber? } extension CSSearchableItemAttributeSet {     var pixelHeight: NSNumber?     var pixelWidth: NSNumber?     var pixelCount: NSNumber?     var colorSpace: String?     var bitsPerSample: NSNumber?     var flashOn: NSNumber?     var focalLength: NSNumber?     var focalLength35mm: NSNumber?     var acquisitionMake: String?     var acquisitionModel: String?     var cameraOwner: String?     var lensModel: String?     var ISOSpeed: NSNumber?     var orientation: NSNumber?     var layerNames: [String]?     var whiteBalance: NSNumber?     var aperture: NSNumber?     var profileName: String?     var resolutionWidthDPI: NSNumber?     var resolutionHeightDPI: NSNumber?     var exposureMode: NSNumber?     var exposureTime: NSNumber?     var EXIFVersion: String?     var EXIFGPSVersion: String?     var hasAlphaChannel: NSNumber?     var redEyeOn: NSNumber?     var meteringMode: String?     var maxAperture: NSNumber?     var fNumber: NSNumber?     var exposureProgram: String?     var exposureTimeString: String? } extension CSSearchableItemAttributeSet {     var editors: [String]?     var participants: [String]?     var projects: [String]?     var downloadedDate: NSDate?     var contentSources: [String]?     var comment: String?     var copyright: String?     var lastUsedDate: NSDate?     var contentCreationDate: NSDate?     var contentModificationDate: NSDate?     var addedDate: NSDate?     var duration: NSNumber?     var contactKeywords: [String]?     var version: String?     var codecs: [String]?     var mediaTypes: [String]?     var streamable: NSNumber?     var totalBitRate: NSNumber?     var videoBitRate: NSNumber?     var audioBitRate: NSNumber?     var deliveryType: NSNumber?     var organizations: [String]?     var role: String?     var languages: [String]?     var rights: String?     var publishers: [String]?     var contributors: [String]?     var coverage: [String]?     var rating: NSNumber?     var ratingDescription: String?     var playCount: NSNumber?     var information: String?     var director: String?     var producer: String?     var genre: String?     var performers: [String]?     var originalFormat: String?     var originalSource: String?     var local: NSNumber?     var contentRating: NSNumber?     var URL: NSURL? } extension CSSearchableItemAttributeSet {     var audioSampleRate: NSNumber?     var audioChannelCount: NSNumber?     var tempo: NSNumber?     var keySignature: String?     var timeSignature: String?     var audioEncodingApplication: String?     var composer: String?     var lyricist: String?     var album: String?     var artist: String?     var audioTrackNumber: NSNumber?     var recordingDate: NSDate?     var musicalGenre: String?     var generalMIDISequence: NSNumber?     var musicalInstrumentCategory: String?     var musicalInstrumentName: String? } extension CSSearchableItemAttributeSet {     var accountIdentifier: String?     var accountHandles: [String]?     @NSCopying var HTMLContentData: NSData?     var textContent: String?     var authors: [CSPerson]?     var primaryRecipients: [CSPerson]?     var additionalRecipients: [CSPerson]?     var hiddenAdditionalRecipients: [CSPerson]?     var emailHeaders: [String : [AnyObject]]?     var mailboxIdentifiers: [String]?     var authorNames: [String]?     var recipientNames: [String]?     var authorEmailAddresses: [String]?     var recipientEmailAddresses: [String]?     var authorAddresses: [String]?     var recipientAddresses: [String]?     var phoneNumbers: [String]?     var emailAddresses: [String]?     var instantMessageAddresses: [String]?     var likelyJunk: NSNumber } extension CSSearchableItemAttributeSet {     var headline: String?     var instructions: String?     var city: String?     var stateOrProvince: String?     var country: String?     var altitude: NSNumber?     var latitude: NSNumber?     var longitude: NSNumber?     var speed: NSNumber?     var timestamp: NSDate?     var imageDirection: NSNumber?     var namedLocation: String?     var GPSTrack: NSNumber?     var GPSStatus: String?     var GPSMeasureMode: String?     var GPSDOP: NSNumber?     var GPSMapDatum: String?     var GPSDestLatitude: NSNumber?     var GPSDestLongitude: NSNumber?     var GPSDestBearing: NSNumber?     var GPSDestDistance: NSNumber?     var GPSProcessingMethod: String?     var GPSAreaInformation: String?     var GPSDateStamp: NSDate?     var GPSDifferental: NSNumber? } ``` | NSCopying, NSSecureCoding |
| To | ``` class CSSearchableItemAttributeSet : NSObject, NSCopying, NSSecureCoding {     init(itemContentType itemContentType: String)     var headline: String?     var instructions: String?     var thoroughfare: String?     var subThoroughfare: String?     var postalCode: String?     var city: String?     var stateOrProvince: String?     var country: String?     var fullyFormattedAddress: String?     var altitude: NSNumber?     var latitude: NSNumber?     var longitude: NSNumber?     var speed: NSNumber?     var timestamp: Date?     var imageDirection: NSNumber?     var namedLocation: String?     var gpsTrack: NSNumber?     var gpsStatus: String?     var gpsMeasureMode: String?     var gpsdop: NSNumber?     var gpsMapDatum: String?     var gpsDestLatitude: NSNumber?     var gpsDestLongitude: NSNumber?     var gpsDestBearing: NSNumber?     var gpsDestDistance: NSNumber?     var gpsProcessingMethod: String?     var gpsAreaInformation: String?     var gpsDateStamp: Date?     var gpsDifferental: NSNumber?     var pixelHeight: NSNumber?     var pixelWidth: NSNumber?     var pixelCount: NSNumber?     var colorSpace: String?     var bitsPerSample: NSNumber?     var flashOn: NSNumber?     var focalLength: NSNumber?     var focalLength35mm: NSNumber?     var acquisitionMake: String?     var acquisitionModel: String?     var cameraOwner: String?     var lensModel: String?     var isoSpeed: NSNumber?     var orientation: NSNumber?     var layerNames: [String]?     var whiteBalance: NSNumber?     var aperture: NSNumber?     var profileName: String?     var resolutionWidthDPI: NSNumber?     var resolutionHeightDPI: NSNumber?     var exposureMode: NSNumber?     var exposureTime: NSNumber?     var exifVersion: String?     var exifgpsVersion: String?     var hasAlphaChannel: NSNumber?     var redEyeOn: NSNumber?     var meteringMode: String?     var maxAperture: NSNumber?     var fNumber: NSNumber?     var exposureProgram: String?     var exposureTimeString: String?     var audioSampleRate: NSNumber?     var audioChannelCount: NSNumber?     var tempo: NSNumber?     var keySignature: String?     var timeSignature: String?     var audioEncodingApplication: String?     var composer: String?     var lyricist: String?     var album: String?     var artist: String?     var audioTrackNumber: NSNumber?     var recordingDate: Date?     var musicalGenre: String?     var generalMIDISequence: NSNumber?     var musicalInstrumentCategory: String?     var musicalInstrumentName: String?     var editors: [String]?     var participants: [String]?     var projects: [String]?     var downloadedDate: Date?     var contentSources: [String]?     var comment: String?     var copyright: String?     var lastUsedDate: Date?     var contentCreationDate: Date?     var contentModificationDate: Date?     var addedDate: Date?     var duration: NSNumber?     var contactKeywords: [String]?     var codecs: [String]?     var mediaTypes: [String]?     var streamable: NSNumber?     var totalBitRate: NSNumber?     var videoBitRate: NSNumber?     var audioBitRate: NSNumber?     var deliveryType: NSNumber?     var organizations: [String]?     var role: String?     var languages: [String]?     var rights: String?     var publishers: [String]?     var contributors: [String]?     var coverage: [String]?     var rating: NSNumber?     var ratingDescription: String?     var playCount: NSNumber?     var information: String?     var director: String?     var producer: String?     var genre: String?     var performers: [String]?     var originalFormat: String?     var originalSource: String?     var local: NSNumber?     var contentRating: NSNumber?     var url: URL?     var accountIdentifier: String?     var accountHandles: [String]?     var htmlContentData: Data?     var textContent: String?     var authors: [CSPerson]?     var primaryRecipients: [CSPerson]?     var additionalRecipients: [CSPerson]?     var hiddenAdditionalRecipients: [CSPerson]?     var emailHeaders: [String : [Any]]?     var mailboxIdentifiers: [String]?     var authorNames: [String]?     var recipientNames: [String]?     var authorEmailAddresses: [String]?     var recipientEmailAddresses: [String]?     var authorAddresses: [String]?     var recipientAddresses: [String]?     var phoneNumbers: [String]?     var emailAddresses: [String]?     var instantMessageAddresses: [String]?     var likelyJunk: NSNumber     var dueDate: Date?     var completionDate: Date?     var startDate: Date?     var endDate: Date?     var importantDates: [Date]?     var allDay: NSNumber?     var subject: String?     var theme: String?     var contentDescription: String?     var identifier: String?     var audiences: [String]?     var fileSize: NSNumber?     var pageCount: NSNumber?     var pageWidth: NSNumber?     var pageHeight: NSNumber?     var securityMethod: String?     var creator: String?     var encodingApplications: [String]?     var kind: String?     var fontNames: [String]?     var containerTitle: String?     var containerDisplayName: String?     var containerIdentifier: String?     var containerOrder: NSNumber?     var supportsPhoneCall: NSNumber?     var supportsNavigation: NSNumber?     var displayName: String?     var alternateNames: [String]?     var path: String?     var contentURL: URL?     var thumbnailURL: URL?     var thumbnailData: Data?     var relatedUniqueIdentifier: String?     var weakRelatedUniqueIdentifier: String?     var metadataModificationDate: Date?     var contentType: String?     var contentTypeTree: [String]?     var keywords: [String]?     var title: String?     var version: String?     var domainIdentifier: String?     func setValue(_ value: NSSecureCoding?, forCustomKey key: CSCustomAttributeKey)     func value(forCustomKey key: CSCustomAttributeKey) -> NSSecureCoding?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CSSearchableItemAttributeSet : CVarArg { } extension CSSearchableItemAttributeSet : Equatable, Hashable {     var hashValue: Int { get } } extension CSSearchableItemAttributeSet {     func setValue(_ value: NSSecureCoding?, forCustomKey key: CSCustomAttributeKey)     func value(forCustomKey key: CSCustomAttributeKey) -> NSSecureCoding? } extension CSSearchableItemAttributeSet {     var subject: String?     var theme: String?     var contentDescription: String?     var identifier: String?     var audiences: [String]?     var fileSize: NSNumber?     var pageCount: NSNumber?     var pageWidth: NSNumber?     var pageHeight: NSNumber?     var securityMethod: String?     var creator: String?     var encodingApplications: [String]?     var kind: String?     var fontNames: [String]? } extension CSSearchableItemAttributeSet {     var dueDate: Date?     var completionDate: Date?     var startDate: Date?     var endDate: Date?     var importantDates: [Date]?     var allDay: NSNumber? } extension CSSearchableItemAttributeSet {     var displayName: String?     var alternateNames: [String]?     var path: String?     var contentURL: URL?     var thumbnailURL: URL?     var thumbnailData: Data?     var relatedUniqueIdentifier: String?     var weakRelatedUniqueIdentifier: String?     var metadataModificationDate: Date?     var contentType: String?     var contentTypeTree: [String]?     var keywords: [String]?     var title: String?     var version: String?     var domainIdentifier: String? } extension CSSearchableItemAttributeSet {     var supportsPhoneCall: NSNumber?     var supportsNavigation: NSNumber? } extension CSSearchableItemAttributeSet {     var containerTitle: String?     var containerDisplayName: String?     var containerIdentifier: String?     var containerOrder: NSNumber? } extension CSSearchableItemAttributeSet {     var pixelHeight: NSNumber?     var pixelWidth: NSNumber?     var pixelCount: NSNumber?     var colorSpace: String?     var bitsPerSample: NSNumber?     var flashOn: NSNumber?     var focalLength: NSNumber?     var focalLength35mm: NSNumber?     var acquisitionMake: String?     var acquisitionModel: String?     var cameraOwner: String?     var lensModel: String?     var isoSpeed: NSNumber?     var orientation: NSNumber?     var layerNames: [String]?     var whiteBalance: NSNumber?     var aperture: NSNumber?     var profileName: String?     var resolutionWidthDPI: NSNumber?     var resolutionHeightDPI: NSNumber?     var exposureMode: NSNumber?     var exposureTime: NSNumber?     var exifVersion: String?     var exifgpsVersion: String?     var hasAlphaChannel: NSNumber?     var redEyeOn: NSNumber?     var meteringMode: String?     var maxAperture: NSNumber?     var fNumber: NSNumber?     var exposureProgram: String?     var exposureTimeString: String? } extension CSSearchableItemAttributeSet {     var editors: [String]?     var participants: [String]?     var projects: [String]?     var downloadedDate: Date?     var contentSources: [String]?     var comment: String?     var copyright: String?     var lastUsedDate: Date?     var contentCreationDate: Date?     var contentModificationDate: Date?     var addedDate: Date?     var duration: NSNumber?     var contactKeywords: [String]?     var codecs: [String]?     var mediaTypes: [String]?     var streamable: NSNumber?     var totalBitRate: NSNumber?     var videoBitRate: NSNumber?     var audioBitRate: NSNumber?     var deliveryType: NSNumber?     var organizations: [String]?     var role: String?     var languages: [String]?     var rights: String?     var publishers: [String]?     var contributors: [String]?     var coverage: [String]?     var rating: NSNumber?     var ratingDescription: String?     var playCount: NSNumber?     var information: String?     var director: String?     var producer: String?     var genre: String?     var performers: [String]?     var originalFormat: String?     var originalSource: String?     var local: NSNumber?     var contentRating: NSNumber?     var url: URL? } extension CSSearchableItemAttributeSet {     var audioSampleRate: NSNumber?     var audioChannelCount: NSNumber?     var tempo: NSNumber?     var keySignature: String?     var timeSignature: String?     var audioEncodingApplication: String?     var composer: String?     var lyricist: String?     var album: String?     var artist: String?     var audioTrackNumber: NSNumber?     var recordingDate: Date?     var musicalGenre: String?     var generalMIDISequence: NSNumber?     var musicalInstrumentCategory: String?     var musicalInstrumentName: String? } extension CSSearchableItemAttributeSet {     var accountIdentifier: String?     var accountHandles: [String]?     var htmlContentData: Data?     var textContent: String?     var authors: [CSPerson]?     var primaryRecipients: [CSPerson]?     var additionalRecipients: [CSPerson]?     var hiddenAdditionalRecipients: [CSPerson]?     var emailHeaders: [String : [Any]]?     var mailboxIdentifiers: [String]?     var authorNames: [String]?     var recipientNames: [String]?     var authorEmailAddresses: [String]?     var recipientEmailAddresses: [String]?     var authorAddresses: [String]?     var recipientAddresses: [String]?     var phoneNumbers: [String]?     var emailAddresses: [String]?     var instantMessageAddresses: [String]?     var likelyJunk: NSNumber } extension CSSearchableItemAttributeSet {     var headline: String?     var instructions: String?     var thoroughfare: String?     var subThoroughfare: String?     var postalCode: String?     var city: String?     var stateOrProvince: String?     var country: String?     var fullyFormattedAddress: String?     var altitude: NSNumber?     var latitude: NSNumber?     var longitude: NSNumber?     var speed: NSNumber?     var timestamp: Date?     var imageDirection: NSNumber?     var namedLocation: String?     var gpsTrack: NSNumber?     var gpsStatus: String?     var gpsMeasureMode: String?     var gpsdop: NSNumber?     var gpsMapDatum: String?     var gpsDestLatitude: NSNumber?     var gpsDestLongitude: NSNumber?     var gpsDestBearing: NSNumber?     var gpsDestDistance: NSNumber?     var gpsProcessingMethod: String?     var gpsAreaInformation: String?     var gpsDateStamp: Date?     var gpsDifferental: NSNumber? } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [CSSearchableItemAttributeSet.addedDate](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616029-addeddate)

|  | Declaration |
| --- | --- |
| From | ``` var addedDate: NSDate? ``` |
| To | ``` var addedDate: Date? ``` |

Modified [CSSearchableItemAttributeSet.allDay](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616636-allday)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var allDay: NSNumber? ``` |
| To | ``` var allDay: NSNumber? ``` |

Modified [CSSearchableItemAttributeSet.completionDate](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616637-completiondate)

|  | Declaration |
| --- | --- |
| From | ``` var completionDate: NSDate? ``` |
| To | ``` var completionDate: Date? ``` |

Modified [CSSearchableItemAttributeSet.containerOrder](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621586-containerorder)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var containerOrder: NSNumber? ``` |
| To | ``` var containerOrder: NSNumber? ``` |

Modified [CSSearchableItemAttributeSet.contentCreationDate](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616001-contentcreationdate)

|  | Declaration |
| --- | --- |
| From | ``` var contentCreationDate: NSDate? ``` |
| To | ``` var contentCreationDate: Date? ``` |

Modified [CSSearchableItemAttributeSet.contentModificationDate](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616085-contentmodificationdate)

|  | Declaration |
| --- | --- |
| From | ``` var contentModificationDate: NSDate? ``` |
| To | ``` var contentModificationDate: Date? ``` |

Modified [CSSearchableItemAttributeSet.contentURL](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621651-contenturl)

|  | Declaration |
| --- | --- |
| From | ``` var contentURL: NSURL? ``` |
| To | ``` var contentURL: URL? ``` |

Modified [CSSearchableItemAttributeSet.downloadedDate](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616035-downloadeddate)

|  | Declaration |
| --- | --- |
| From | ``` var downloadedDate: NSDate? ``` |
| To | ``` var downloadedDate: Date? ``` |

Modified [CSSearchableItemAttributeSet.dueDate](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616641-duedate)

|  | Declaration |
| --- | --- |
| From | ``` var dueDate: NSDate? ``` |
| To | ``` var dueDate: Date? ``` |

Modified [CSSearchableItemAttributeSet.emailHeaders](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621568-emailheaders)

|  | Declaration |
| --- | --- |
| From | ``` var emailHeaders: [String : [AnyObject]]? ``` |
| To | ``` var emailHeaders: [String : [Any]]? ``` |

Modified [CSSearchableItemAttributeSet.endDate](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616638-enddate)

|  | Declaration |
| --- | --- |
| From | ``` var endDate: NSDate? ``` |
| To | ``` var endDate: Date? ``` |

Modified [CSSearchableItemAttributeSet.exifgpsVersion](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621543-exifgpsversion)

|  | Declaration |
| --- | --- |
| From | ``` var EXIFGPSVersion: String? ``` |
| To | ``` var exifgpsVersion: String? ``` |

Modified [CSSearchableItemAttributeSet.exifVersion](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621550-exifversion)

|  | Declaration |
| --- | --- |
| From | ``` var EXIFVersion: String? ``` |
| To | ``` var exifVersion: String? ``` |

Modified [CSSearchableItemAttributeSet.gpsAreaInformation](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620581-gpsareainformation)

|  | Declaration |
| --- | --- |
| From | ``` var GPSAreaInformation: String? ``` |
| To | ``` var gpsAreaInformation: String? ``` |

Modified [CSSearchableItemAttributeSet.gpsDateStamp](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620587-gpsdatestamp)

|  | Declaration |
| --- | --- |
| From | ``` var GPSDateStamp: NSDate? ``` |
| To | ``` var gpsDateStamp: Date? ``` |

Modified [CSSearchableItemAttributeSet.gpsDestBearing](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620577-gpsdestbearing)

|  | Declaration |
| --- | --- |
| From | ``` var GPSDestBearing: NSNumber? ``` |
| To | ``` var gpsDestBearing: NSNumber? ``` |

Modified [CSSearchableItemAttributeSet.gpsDestDistance](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620582-gpsdestdistance)

|  | Declaration |
| --- | --- |
| From | ``` var GPSDestDistance: NSNumber? ``` |
| To | ``` var gpsDestDistance: NSNumber? ``` |

Modified [CSSearchableItemAttributeSet.gpsDestLatitude](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620572-gpsdestlatitude)

|  | Declaration |
| --- | --- |
| From | ``` var GPSDestLatitude: NSNumber? ``` |
| To | ``` var gpsDestLatitude: NSNumber? ``` |

Modified [CSSearchableItemAttributeSet.gpsDestLongitude](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620580-gpsdestlongitude)

|  | Declaration |
| --- | --- |
| From | ``` var GPSDestLongitude: NSNumber? ``` |
| To | ``` var gpsDestLongitude: NSNumber? ``` |

Modified [CSSearchableItemAttributeSet.gpsDifferental](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620592-gpsdifferental)

|  | Declaration |
| --- | --- |
| From | ``` var GPSDifferental: NSNumber? ``` |
| To | ``` var gpsDifferental: NSNumber? ``` |

Modified [CSSearchableItemAttributeSet.gpsdop](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620593-gpsdop)

|  | Declaration |
| --- | --- |
| From | ``` var GPSDOP: NSNumber? ``` |
| To | ``` var gpsdop: NSNumber? ``` |

Modified [CSSearchableItemAttributeSet.gpsMapDatum](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620583-gpsmapdatum)

|  | Declaration |
| --- | --- |
| From | ``` var GPSMapDatum: String? ``` |
| To | ``` var gpsMapDatum: String? ``` |

Modified [CSSearchableItemAttributeSet.gpsMeasureMode](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620573-gpsmeasuremode)

|  | Declaration |
| --- | --- |
| From | ``` var GPSMeasureMode: String? ``` |
| To | ``` var gpsMeasureMode: String? ``` |

Modified [CSSearchableItemAttributeSet.gpsProcessingMethod](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620575-gpsprocessingmethod)

|  | Declaration |
| --- | --- |
| From | ``` var GPSProcessingMethod: String? ``` |
| To | ``` var gpsProcessingMethod: String? ``` |

Modified [CSSearchableItemAttributeSet.gpsStatus](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620589-gpsstatus)

|  | Declaration |
| --- | --- |
| From | ``` var GPSStatus: String? ``` |
| To | ``` var gpsStatus: String? ``` |

Modified [CSSearchableItemAttributeSet.gpsTrack](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620588-gpstrack)

|  | Declaration |
| --- | --- |
| From | ``` var GPSTrack: NSNumber? ``` |
| To | ``` var gpsTrack: NSNumber? ``` |

Modified [CSSearchableItemAttributeSet.htmlContentData](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621669-htmlcontentdata)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var HTMLContentData: NSData? ``` |
| To | ``` var htmlContentData: Data? ``` |

Modified [CSSearchableItemAttributeSet.importantDates](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616639-importantdates)

|  | Declaration |
| --- | --- |
| From | ``` var importantDates: [NSDate]? ``` |
| To | ``` var importantDates: [Date]? ``` |

Modified [CSSearchableItemAttributeSet.isoSpeed](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621548-isospeed)

|  | Declaration |
| --- | --- |
| From | ``` var ISOSpeed: NSNumber? ``` |
| To | ``` var isoSpeed: NSNumber? ``` |

Modified [CSSearchableItemAttributeSet.lastUsedDate](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616018-lastuseddate)

|  | Declaration |
| --- | --- |
| From | ``` var lastUsedDate: NSDate? ``` |
| To | ``` var lastUsedDate: Date? ``` |

Modified [CSSearchableItemAttributeSet.metadataModificationDate](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621657-metadatamodificationdate)

|  | Declaration |
| --- | --- |
| From | ``` var metadataModificationDate: NSDate? ``` |
| To | ``` var metadataModificationDate: Date? ``` |

Modified [CSSearchableItemAttributeSet.recordingDate](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616051-recordingdate)

|  | Declaration |
| --- | --- |
| From | ``` var recordingDate: NSDate? ``` |
| To | ``` var recordingDate: Date? ``` |

Modified [CSSearchableItemAttributeSet.startDate](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616640-startdate)

|  | Declaration |
| --- | --- |
| From | ``` var startDate: NSDate? ``` |
| To | ``` var startDate: Date? ``` |

Modified [CSSearchableItemAttributeSet.supportsNavigation](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621564-supportsnavigation)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var supportsNavigation: NSNumber? ``` |
| To | ``` var supportsNavigation: NSNumber? ``` |

Modified [CSSearchableItemAttributeSet.supportsPhoneCall](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621653-supportsphonecall)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var supportsPhoneCall: NSNumber? ``` |
| To | ``` var supportsPhoneCall: NSNumber? ``` |

Modified [CSSearchableItemAttributeSet.thumbnailData](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621582-thumbnaildata)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var thumbnailData: NSData? ``` |
| To | ``` var thumbnailData: Data? ``` |

Modified [CSSearchableItemAttributeSet.thumbnailURL](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621560-thumbnailurl)

|  | Declaration |
| --- | --- |
| From | ``` var thumbnailURL: NSURL? ``` |
| To | ``` var thumbnailURL: URL? ``` |

Modified [CSSearchableItemAttributeSet.timestamp](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620574-timestamp)

|  | Declaration |
| --- | --- |
| From | ``` var timestamp: NSDate? ``` |
| To | ``` var timestamp: Date? ``` |

Modified [CSSearchableItemAttributeSet.url](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616087-url)

|  | Declaration |
| --- | --- |
| From | ``` var URL: NSURL? ``` |
| To | ``` var url: URL? ``` |

Modified [CSSearchableItemAttributeSet.value(forCustomKey: CSCustomAttributeKey) -> NSSecureCoding?](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616407-value)

|  | Declaration |
| --- | --- |
| From | ``` func valueForCustomKey(_ key: CSCustomAttributeKey) -> NSSecureCoding? ``` |
| To | ``` func value(forCustomKey key: CSCustomAttributeKey) -> NSSecureCoding? ``` |

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
