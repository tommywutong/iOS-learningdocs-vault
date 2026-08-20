---
title: watchOS 3.0 API Diffs
apple_id: TP40017328
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS30APIDiffs/Swift/ClockKit.html
archived_at: '2026-07-18T02:58:16.819576Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 3.0 API Diffs](watchOS%202.2%20to%20watchOS%203.0%20API%20Differences.md)


# ClockKit Changes for Swift

### ClockKit

Removed [CLKComplicationTimeTravelDirections.None](https://developer.apple.com/documentation/clockkit/clkcomplicationtimetraveldirections/clkcomplicationtimetraveldirectionnone)Added [CLKComplicationDataSource.getLocalizableSampleTemplate(for: CLKComplication, withHandler: (CLKComplicationTemplate?) -> Swift.Void)](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/1650686-getlocalizablesampletemplateforc)Added [CLKComplicationFamily.extraLarge](https://developer.apple.com/documentation/clockkit/clkcomplicationfamily/extralarge)Added [CLKComplicationFamily.utilitarianSmallFlat](https://developer.apple.com/documentation/clockkit/clkcomplicationfamily/clkcomplicationfamilyutilitariansmallflat)Added [CLKComplicationTemplateExtraLargeColumnsText](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargecolumnstext)Added [CLKComplicationTemplateExtraLargeColumnsText.column2Alignment](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargecolumnstext/1650719-column2alignment)Added [CLKComplicationTemplateExtraLargeColumnsText.highlightColumn2](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargecolumnstext/1650698-highlightcolumn2)Added [CLKComplicationTemplateExtraLargeColumnsText.row1Column1TextProvider](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargecolumnstext/1650716-row1column1textprovider)Added [CLKComplicationTemplateExtraLargeColumnsText.row1Column2TextProvider](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargecolumnstext/1650700-row1column2textprovider)Added [CLKComplicationTemplateExtraLargeColumnsText.row2Column1TextProvider](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargecolumnstext/1650708-row2column1textprovider)Added [CLKComplicationTemplateExtraLargeColumnsText.row2Column2TextProvider](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargecolumnstext/1650706-row2column2textprovider)Added [CLKComplicationTemplateExtraLargeRingImage](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargeringimage)Added [CLKComplicationTemplateExtraLargeRingImage.fillFraction](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargeringimage/1650713-fillfraction)Added [CLKComplicationTemplateExtraLargeRingImage.imageProvider](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargeringimage/1650704-imageprovider)Added [CLKComplicationTemplateExtraLargeRingImage.ringStyle](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargeringimage/1650723-ringstyle)Added [CLKComplicationTemplateExtraLargeRingText](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargeringtext)Added [CLKComplicationTemplateExtraLargeRingText.fillFraction](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargeringtext/1650711-fillfraction)Added [CLKComplicationTemplateExtraLargeRingText.ringStyle](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargeringtext/1650722-ringstyle)Added [CLKComplicationTemplateExtraLargeRingText.textProvider](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargeringtext/1650703-textprovider)Added [CLKComplicationTemplateExtraLargeSimpleImage](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargesimpleimage)Added [CLKComplicationTemplateExtraLargeSimpleImage.imageProvider](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargesimpleimage/1650709-imageprovider)Added [CLKComplicationTemplateExtraLargeSimpleText](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargesimpletext)Added [CLKComplicationTemplateExtraLargeSimpleText.textProvider](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargesimpletext/1650724-textprovider)Added [CLKComplicationTemplateExtraLargeStackImage](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargestackimage)Added [CLKComplicationTemplateExtraLargeStackImage.highlightLine2](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargestackimage/1650715-highlightline2)Added [CLKComplicationTemplateExtraLargeStackImage.line1ImageProvider](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargestackimage/1650718-line1imageprovider)Added [CLKComplicationTemplateExtraLargeStackImage.line2TextProvider](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargestackimage/1650714-line2textprovider)Added [CLKComplicationTemplateExtraLargeStackText](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargestacktext)Added [CLKComplicationTemplateExtraLargeStackText.highlightLine2](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargestacktext/1650701-highlightline2)Added [CLKComplicationTemplateExtraLargeStackText.line1TextProvider](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargestacktext/1650707-line1textprovider)Added [CLKComplicationTemplateExtraLargeStackText.line2TextProvider](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargestacktext/1650695-line2textprovider)Added [CLKTextProvider.localizableTextProvider(withStringsFileFormatKey: String, textProviders: [CLKTextProvider]) -> Self [class]](https://developer.apple.com/documentation/clockkit/clktextprovider/1650721-localizabletextproviderwithstrin)Added [CLKTextProvider.localizableTextProvider(withStringsFileTextKey: String) -> Self [class]](https://developer.apple.com/documentation/clockkit/clktextprovider/1650705-localizabletextproviderwithstrin)Added [CLKTextProvider.localizableTextProvider(withStringsFileTextKey: String, shortTextKey: String?) -> Self [class]](https://developer.apple.com/documentation/clockkit/clktextprovider/1650696-localizabletextprovider)Modified [CLKComplication](https://developer.apple.com/documentation/clockkit/clkcomplication)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CLKComplication : NSObject, NSCopying {     var family: CLKComplicationFamily { get } } ``` | NSCopying |
| To | ``` class CLKComplication : NSObject, NSCopying {     var family: CLKComplicationFamily { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CLKComplication : CVarArg { } extension CLKComplication : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [CLKComplicationColumnAlignment [enum]](https://developer.apple.com/documentation/clockkit/clkcomplicationcolumnalignment)

|  | Declaration |
| --- | --- |
| From | ``` enum CLKComplicationColumnAlignment : Int {     case Leading     case Trailing     static var Left: CLKComplicationColumnAlignment { get }     static var Right: CLKComplicationColumnAlignment { get } } ``` |
| To | ``` enum CLKComplicationColumnAlignment : Int {     case leading     case trailing     static var left: CLKComplicationColumnAlignment { get }     static var right: CLKComplicationColumnAlignment { get } } ``` |

Modified [CLKComplicationColumnAlignment.leading](https://developer.apple.com/documentation/clockkit/clkcomplicationcolumnalignment/clkcomplicationcolumnalignmentleading)

|  | Declaration |
| --- | --- |
| From | ``` case Leading ``` |
| To | ``` case leading ``` |

Modified [CLKComplicationColumnAlignment.left](https://developer.apple.com/documentation/clockkit/clkcomplicationcolumnalignment/1628104-left)

|  | Declaration |
| --- | --- |
| From | ``` static var Left: CLKComplicationColumnAlignment { get } ``` |
| To | ``` static var left: CLKComplicationColumnAlignment { get } ``` |

Modified [CLKComplicationColumnAlignment.right](https://developer.apple.com/documentation/clockkit/clkcomplicationcolumnalignment/1627996-right)

|  | Declaration |
| --- | --- |
| From | ``` static var Right: CLKComplicationColumnAlignment { get } ``` |
| To | ``` static var right: CLKComplicationColumnAlignment { get } ``` |

Modified [CLKComplicationColumnAlignment.trailing](https://developer.apple.com/documentation/clockkit/clkcomplicationcolumnalignment/clkcomplicationcolumnalignmenttrailing)

|  | Declaration |
| --- | --- |
| From | ``` case Trailing ``` |
| To | ``` case trailing ``` |

Modified [CLKComplicationDataSource](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource)

|  | Declaration |
| --- | --- |
| From | ``` protocol CLKComplicationDataSource : NSObjectProtocol {     func getSupportedTimeTravelDirectionsForComplication(_ complication: CLKComplication, withHandler handler: (CLKComplicationTimeTravelDirections) -> Void)     optional func getTimelineStartDateForComplication(_ complication: CLKComplication, withHandler handler: (NSDate?) -> Void)     optional func getTimelineEndDateForComplication(_ complication: CLKComplication, withHandler handler: (NSDate?) -> Void)     optional func getPrivacyBehaviorForComplication(_ complication: CLKComplication, withHandler handler: (CLKComplicationPrivacyBehavior) -> Void)     optional func getTimelineAnimationBehaviorForComplication(_ complication: CLKComplication, withHandler handler: (CLKComplicationTimelineAnimationBehavior) -> Void)     func getCurrentTimelineEntryForComplication(_ complication: CLKComplication, withHandler handler: (CLKComplicationTimelineEntry?) -> Void)     optional func getTimelineEntriesForComplication(_ complication: CLKComplication, beforeDate date: NSDate, limit limit: Int, withHandler handler: ([CLKComplicationTimelineEntry]?) -> Void)     optional func getTimelineEntriesForComplication(_ complication: CLKComplication, afterDate date: NSDate, limit limit: Int, withHandler handler: ([CLKComplicationTimelineEntry]?) -> Void)     optional func getNextRequestedUpdateDateWithHandler(_ handler: (NSDate?) -> Void)     optional func requestedUpdateDidBegin()     optional func requestedUpdateBudgetExhausted()     func getPlaceholderTemplateForComplication(_ complication: CLKComplication, withHandler handler: (CLKComplicationTemplate?) -> Void) } ``` |
| To | ``` protocol CLKComplicationDataSource : NSObjectProtocol {     func getSupportedTimeTravelDirections(for complication: CLKComplication, withHandler handler: @escaping (CLKComplicationTimeTravelDirections) -> Swift.Void)     optional func getTimelineStartDate(for complication: CLKComplication, withHandler handler: @escaping (Date?) -> Swift.Void)     optional func getTimelineEndDate(for complication: CLKComplication, withHandler handler: @escaping (Date?) -> Swift.Void)     optional func getPrivacyBehavior(for complication: CLKComplication, withHandler handler: @escaping (CLKComplicationPrivacyBehavior) -> Swift.Void)     optional func getTimelineAnimationBehavior(for complication: CLKComplication, withHandler handler: @escaping (CLKComplicationTimelineAnimationBehavior) -> Swift.Void)     func getCurrentTimelineEntry(for complication: CLKComplication, withHandler handler: @escaping (CLKComplicationTimelineEntry?) -> Swift.Void)     optional func getTimelineEntries(for complication: CLKComplication, before date: Date, limit limit: Int, withHandler handler: @escaping ([CLKComplicationTimelineEntry]?) -> Swift.Void)     optional func getTimelineEntries(for complication: CLKComplication, after date: Date, limit limit: Int, withHandler handler: @escaping ([CLKComplicationTimelineEntry]?) -> Swift.Void)     optional func getNextRequestedUpdateDate(handler handler: @escaping (Date?) -> Swift.Void)     optional func requestedUpdateDidBegin()     optional func requestedUpdateBudgetExhausted()     optional func getLocalizableSampleTemplate(for complication: CLKComplication, withHandler handler: @escaping (CLKComplicationTemplate?) -> Swift.Void)     optional func getPlaceholderTemplate(for complication: CLKComplication, withHandler handler: @escaping (CLKComplicationTemplate?) -> Swift.Void) } ``` |

Modified [CLKComplicationDataSource.getCurrentTimelineEntry(for: CLKComplication, withHandler: (CLKComplicationTimelineEntry?) -> Swift.Void)](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/1628051-getcurrenttimelineentry)

|  | Declaration |
| --- | --- |
| From | ``` func getCurrentTimelineEntryForComplication(_ complication: CLKComplication, withHandler handler: (CLKComplicationTimelineEntry?) -> Void) ``` |
| To | ``` func getCurrentTimelineEntry(for complication: CLKComplication, withHandler handler: @escaping (CLKComplicationTimelineEntry?) -> Swift.Void) ``` |

Modified [CLKComplicationDataSource.getNextRequestedUpdateDate(handler: (Date?) -> Swift.Void)](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/1628062-getnextrequestedupdatedate)

|  | Declaration |
| --- | --- |
| From | ``` optional func getNextRequestedUpdateDateWithHandler(_ handler: (NSDate?) -> Void) ``` |
| To | ``` optional func getNextRequestedUpdateDate(handler handler: @escaping (Date?) -> Swift.Void) ``` |

Modified [CLKComplicationDataSource.getPlaceholderTemplate(for: CLKComplication, withHandler: (CLKComplicationTemplate?) -> Swift.Void)](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/1628026-getplaceholdertemplate)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` func getPlaceholderTemplateForComplication(_ complication: CLKComplication, withHandler handler: (CLKComplicationTemplate?) -> Void) ``` | -- |
| To | ``` optional func getPlaceholderTemplate(for complication: CLKComplication, withHandler handler: @escaping (CLKComplicationTemplate?) -> Swift.Void) ``` | yes |

Modified [CLKComplicationDataSource.getPrivacyBehavior(for: CLKComplication, withHandler: (CLKComplicationPrivacyBehavior) -> Swift.Void)](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/1627965-getprivacybehaviorforcomplicatio)

|  | Declaration |
| --- | --- |
| From | ``` optional func getPrivacyBehaviorForComplication(_ complication: CLKComplication, withHandler handler: (CLKComplicationPrivacyBehavior) -> Void) ``` |
| To | ``` optional func getPrivacyBehavior(for complication: CLKComplication, withHandler handler: @escaping (CLKComplicationPrivacyBehavior) -> Swift.Void) ``` |

Modified [CLKComplicationDataSource.getSupportedTimeTravelDirections(for: CLKComplication, withHandler: (CLKComplicationTimeTravelDirections) -> Swift.Void)](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/1628002-getsupportedtimetraveldirections)

|  | Declaration |
| --- | --- |
| From | ``` func getSupportedTimeTravelDirectionsForComplication(_ complication: CLKComplication, withHandler handler: (CLKComplicationTimeTravelDirections) -> Void) ``` |
| To | ``` func getSupportedTimeTravelDirections(for complication: CLKComplication, withHandler handler: @escaping (CLKComplicationTimeTravelDirections) -> Swift.Void) ``` |

Modified [CLKComplicationDataSource.getTimelineAnimationBehavior(for: CLKComplication, withHandler: (CLKComplicationTimelineAnimationBehavior) -> Swift.Void)](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/1628074-gettimelineanimationbehavior)

|  | Declaration |
| --- | --- |
| From | ``` optional func getTimelineAnimationBehaviorForComplication(_ complication: CLKComplication, withHandler handler: (CLKComplicationTimelineAnimationBehavior) -> Void) ``` |
| To | ``` optional func getTimelineAnimationBehavior(for complication: CLKComplication, withHandler handler: @escaping (CLKComplicationTimelineAnimationBehavior) -> Swift.Void) ``` |

Modified [CLKComplicationDataSource.getTimelineEndDate(for: CLKComplication, withHandler: (Date?) -> Swift.Void)](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/1628056-gettimelineenddate)

|  | Declaration |
| --- | --- |
| From | ``` optional func getTimelineEndDateForComplication(_ complication: CLKComplication, withHandler handler: (NSDate?) -> Void) ``` |
| To | ``` optional func getTimelineEndDate(for complication: CLKComplication, withHandler handler: @escaping (Date?) -> Swift.Void) ``` |

Modified [CLKComplicationDataSource.getTimelineEntries(for: CLKComplication, after: Date, limit: Int, withHandler: ([CLKComplicationTimelineEntry]?) -> Swift.Void)](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/1628094-gettimelineentriesforcomplicatio)

|  | Declaration |
| --- | --- |
| From | ``` optional func getTimelineEntriesForComplication(_ complication: CLKComplication, afterDate date: NSDate, limit limit: Int, withHandler handler: ([CLKComplicationTimelineEntry]?) -> Void) ``` |
| To | ``` optional func getTimelineEntries(for complication: CLKComplication, after date: Date, limit limit: Int, withHandler handler: @escaping ([CLKComplicationTimelineEntry]?) -> Swift.Void) ``` |

Modified [CLKComplicationDataSource.getTimelineEntries(for: CLKComplication, before: Date, limit: Int, withHandler: ([CLKComplicationTimelineEntry]?) -> Swift.Void)](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/1628008-gettimelineentries)

|  | Declaration |
| --- | --- |
| From | ``` optional func getTimelineEntriesForComplication(_ complication: CLKComplication, beforeDate date: NSDate, limit limit: Int, withHandler handler: ([CLKComplicationTimelineEntry]?) -> Void) ``` |
| To | ``` optional func getTimelineEntries(for complication: CLKComplication, before date: Date, limit limit: Int, withHandler handler: @escaping ([CLKComplicationTimelineEntry]?) -> Swift.Void) ``` |

Modified [CLKComplicationDataSource.getTimelineStartDate(for: CLKComplication, withHandler: (Date?) -> Swift.Void)](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/1627967-gettimelinestartdateforcomplicat)

|  | Declaration |
| --- | --- |
| From | ``` optional func getTimelineStartDateForComplication(_ complication: CLKComplication, withHandler handler: (NSDate?) -> Void) ``` |
| To | ``` optional func getTimelineStartDate(for complication: CLKComplication, withHandler handler: @escaping (Date?) -> Swift.Void) ``` |

Modified [CLKComplicationFamily [enum]](https://developer.apple.com/documentation/clockkit/clkcomplicationfamily)

|  | Declaration |
| --- | --- |
| From | ``` enum CLKComplicationFamily : Int {     case ModularSmall     case ModularLarge     case UtilitarianSmall     case UtilitarianLarge     case CircularSmall } ``` |
| To | ``` enum CLKComplicationFamily : Int {     case modularSmall     case modularLarge     case utilitarianSmall     case utilitarianSmallFlat     case utilitarianLarge     case circularSmall     case extraLarge } ``` |

Modified [CLKComplicationFamily.circularSmall](https://developer.apple.com/documentation/clockkit/clkcomplicationfamily/circularsmall)

|  | Declaration |
| --- | --- |
| From | ``` case CircularSmall ``` |
| To | ``` case circularSmall ``` |

Modified [CLKComplicationFamily.modularLarge](https://developer.apple.com/documentation/clockkit/clkcomplicationfamily/clkcomplicationfamilymodularlarge)

|  | Declaration |
| --- | --- |
| From | ``` case ModularLarge ``` |
| To | ``` case modularLarge ``` |

Modified [CLKComplicationFamily.modularSmall](https://developer.apple.com/documentation/clockkit/clkcomplicationfamily/modularsmall)

|  | Declaration |
| --- | --- |
| From | ``` case ModularSmall ``` |
| To | ``` case modularSmall ``` |

Modified [CLKComplicationFamily.utilitarianLarge](https://developer.apple.com/documentation/clockkit/clkcomplicationfamily/utilitarianlarge)

|  | Declaration |
| --- | --- |
| From | ``` case UtilitarianLarge ``` |
| To | ``` case utilitarianLarge ``` |

Modified [CLKComplicationFamily.utilitarianSmall](https://developer.apple.com/documentation/clockkit/clkcomplicationfamily/utilitariansmall)

|  | Declaration |
| --- | --- |
| From | ``` case UtilitarianSmall ``` |
| To | ``` case utilitarianSmall ``` |

Modified [CLKComplicationPrivacyBehavior [enum]](https://developer.apple.com/documentation/clockkit/clkcomplicationprivacybehavior)

|  | Declaration |
| --- | --- |
| From | ``` enum CLKComplicationPrivacyBehavior : UInt {     case ShowOnLockScreen     case HideOnLockScreen } ``` |
| To | ``` enum CLKComplicationPrivacyBehavior : UInt {     case showOnLockScreen     case hideOnLockScreen } ``` |

Modified [CLKComplicationPrivacyBehavior.hideOnLockScreen](https://developer.apple.com/documentation/clockkit/clkcomplicationprivacybehavior/clkcomplicationprivacybehaviorhideonlockscreen)

|  | Declaration |
| --- | --- |
| From | ``` case HideOnLockScreen ``` |
| To | ``` case hideOnLockScreen ``` |

Modified [CLKComplicationPrivacyBehavior.showOnLockScreen](https://developer.apple.com/documentation/clockkit/clkcomplicationprivacybehavior/showonlockscreen)

|  | Declaration |
| --- | --- |
| From | ``` case ShowOnLockScreen ``` |
| To | ``` case showOnLockScreen ``` |

Modified [CLKComplicationRingStyle [enum]](https://developer.apple.com/documentation/clockkit/clkcomplicationringstyle)

|  | Declaration |
| --- | --- |
| From | ``` enum CLKComplicationRingStyle : Int {     case Closed     case Open } ``` |
| To | ``` enum CLKComplicationRingStyle : Int {     case closed     case open } ``` |

Modified [CLKComplicationRingStyle.closed](https://developer.apple.com/documentation/clockkit/clkcomplicationringstyle/clkcomplicationringstyleclosed)

|  | Declaration |
| --- | --- |
| From | ``` case Closed ``` |
| To | ``` case closed ``` |

Modified [CLKComplicationRingStyle.open](https://developer.apple.com/documentation/clockkit/clkcomplicationringstyle/open)

|  | Declaration |
| --- | --- |
| From | ``` case Open ``` |
| To | ``` case open ``` |

Modified [CLKComplicationServer](https://developer.apple.com/documentation/clockkit/clkcomplicationserver)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CLKComplicationServer : NSObject {     class func sharedInstance() -> Self     var activeComplications: [CLKComplication]? { get }     var earliestTimeTravelDate: NSDate { get }     var latestTimeTravelDate: NSDate { get }     func reloadTimelineForComplication(_ complication: CLKComplication)     func extendTimelineForComplication(_ complication: CLKComplication) } ``` | -- |
| To | ``` class CLKComplicationServer : NSObject {     class func sharedInstance() -> Self     var activeComplications: [CLKComplication]? { get }     var earliestTimeTravelDate: Date { get }     var latestTimeTravelDate: Date { get }     func reloadTimeline(for complication: CLKComplication)     func extendTimeline(for complication: CLKComplication)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CLKComplicationServer : CVarArg { } extension CLKComplicationServer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CLKComplicationServer.earliestTimeTravelDate](https://developer.apple.com/documentation/clockkit/clkcomplicationserver/1627896-earliesttimetraveldate)

|  | Declaration |
| --- | --- |
| From | ``` var earliestTimeTravelDate: NSDate { get } ``` |
| To | ``` var earliestTimeTravelDate: Date { get } ``` |

Modified [CLKComplicationServer.extendTimeline(for: CLKComplication)](https://developer.apple.com/documentation/clockkit/clkcomplicationserver/1627895-extendtimeline)

|  | Declaration |
| --- | --- |
| From | ``` func extendTimelineForComplication(_ complication: CLKComplication) ``` |
| To | ``` func extendTimeline(for complication: CLKComplication) ``` |

Modified [CLKComplicationServer.latestTimeTravelDate](https://developer.apple.com/documentation/clockkit/clkcomplicationserver/1627890-latesttimetraveldate)

|  | Declaration |
| --- | --- |
| From | ``` var latestTimeTravelDate: NSDate { get } ``` |
| To | ``` var latestTimeTravelDate: Date { get } ``` |

Modified [CLKComplicationServer.reloadTimeline(for: CLKComplication)](https://developer.apple.com/documentation/clockkit/clkcomplicationserver/1627891-reloadtimeline)

|  | Declaration |
| --- | --- |
| From | ``` func reloadTimelineForComplication(_ complication: CLKComplication) ``` |
| To | ``` func reloadTimeline(for complication: CLKComplication) ``` |

Modified [CLKComplicationTemplate](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CLKComplicationTemplate : NSObject, NSCopying {     @NSCopying var tintColor: UIColor? } ``` | NSCopying |
| To | ``` class CLKComplicationTemplate : NSObject, NSCopying {     @NSCopying var tintColor: UIColor?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CLKComplicationTemplate : CVarArg { } extension CLKComplicationTemplate : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [CLKComplicationTimelineAnimationBehavior [enum]](https://developer.apple.com/documentation/clockkit/clkcomplicationtimelineanimationbehavior)

|  | Declaration |
| --- | --- |
| From | ``` enum CLKComplicationTimelineAnimationBehavior : UInt {     case Never     case Grouped     case Always } ``` |
| To | ``` enum CLKComplicationTimelineAnimationBehavior : UInt {     case never     case grouped     case always } ``` |

Modified [CLKComplicationTimelineAnimationBehavior.always](https://developer.apple.com/documentation/clockkit/clkcomplicationtimelineanimationbehavior/clkcomplicationtimelineanimationbehavioralways)

|  | Declaration |
| --- | --- |
| From | ``` case Always ``` |
| To | ``` case always ``` |

Modified [CLKComplicationTimelineAnimationBehavior.grouped](https://developer.apple.com/documentation/clockkit/clkcomplicationtimelineanimationbehavior/clkcomplicationtimelineanimationbehaviorgrouped)

|  | Declaration |
| --- | --- |
| From | ``` case Grouped ``` |
| To | ``` case grouped ``` |

Modified [CLKComplicationTimelineAnimationBehavior.never](https://developer.apple.com/documentation/clockkit/clkcomplicationtimelineanimationbehavior/clkcomplicationtimelineanimationbehaviornever)

|  | Declaration |
| --- | --- |
| From | ``` case Never ``` |
| To | ``` case never ``` |

Modified [CLKComplicationTimelineEntry](https://developer.apple.com/documentation/clockkit/clkcomplicationtimelineentry)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CLKComplicationTimelineEntry : NSObject {     convenience init(date date: NSDate, complicationTemplate complicationTemplate: CLKComplicationTemplate)     class func entryWithDate(_ date: NSDate, complicationTemplate complicationTemplate: CLKComplicationTemplate) -> Self     convenience init(date date: NSDate, complicationTemplate complicationTemplate: CLKComplicationTemplate, timelineAnimationGroup timelineAnimationGroup: String?)     class func entryWithDate(_ date: NSDate, complicationTemplate complicationTemplate: CLKComplicationTemplate, timelineAnimationGroup timelineAnimationGroup: String?) -> Self     var date: NSDate     @NSCopying var complicationTemplate: CLKComplicationTemplate     var timelineAnimationGroup: String? } ``` | -- |
| To | ``` class CLKComplicationTimelineEntry : NSObject {     convenience init(date date: Date, complicationTemplate complicationTemplate: CLKComplicationTemplate)     class func withDate(_ date: Date, complicationTemplate complicationTemplate: CLKComplicationTemplate) -> Self     convenience init(date date: Date, complicationTemplate complicationTemplate: CLKComplicationTemplate, timelineAnimationGroup timelineAnimationGroup: String?)     class func withDate(_ date: Date, complicationTemplate complicationTemplate: CLKComplicationTemplate, timelineAnimationGroup timelineAnimationGroup: String?) -> Self     var date: Date     @NSCopying var complicationTemplate: CLKComplicationTemplate     var timelineAnimationGroup: String?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CLKComplicationTimelineEntry : CVarArg { } extension CLKComplicationTimelineEntry : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CLKComplicationTimelineEntry.date](https://developer.apple.com/documentation/clockkit/clkcomplicationtimelineentry/1627973-date)

|  | Declaration |
| --- | --- |
| From | ``` var date: NSDate ``` |
| To | ``` var date: Date ``` |

Modified [CLKComplicationTimelineEntry.init(date: Date, complicationTemplate: CLKComplicationTemplate)](https://developer.apple.com/documentation/clockkit/clkcomplicationtimelineentry/1627988-entrywithdate)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(date date: NSDate, complicationTemplate complicationTemplate: CLKComplicationTemplate) ``` |
| To | ``` convenience init(date date: Date, complicationTemplate complicationTemplate: CLKComplicationTemplate) ``` |

Modified [CLKComplicationTimelineEntry.init(date: Date, complicationTemplate: CLKComplicationTemplate, timelineAnimationGroup: String?)](https://developer.apple.com/documentation/clockkit/clkcomplicationtimelineentry/1628005-entrywithdate)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(date date: NSDate, complicationTemplate complicationTemplate: CLKComplicationTemplate, timelineAnimationGroup timelineAnimationGroup: String?) ``` |
| To | ``` convenience init(date date: Date, complicationTemplate complicationTemplate: CLKComplicationTemplate, timelineAnimationGroup timelineAnimationGroup: String?) ``` |

Modified [CLKComplicationTimeTravelDirections [struct]](https://developer.apple.com/documentation/clockkit/clkcomplicationtimetraveldirections)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CLKComplicationTimeTravelDirections : OptionSetType {     init(rawValue rawValue: UInt)     static var None: CLKComplicationTimeTravelDirections { get }     static var Forward: CLKComplicationTimeTravelDirections { get }     static var Backward: CLKComplicationTimeTravelDirections { get } } ``` | OptionSetType |
| To | ``` struct CLKComplicationTimeTravelDirections : OptionSet {     init(rawValue rawValue: UInt)     static var none: CLKComplicationTimeTravelDirections { get }     static var forward: CLKComplicationTimeTravelDirections { get }     static var backward: CLKComplicationTimeTravelDirections { get }     func intersect(_ other: CLKComplicationTimeTravelDirections) -> CLKComplicationTimeTravelDirections     func exclusiveOr(_ other: CLKComplicationTimeTravelDirections) -> CLKComplicationTimeTravelDirections     mutating func unionInPlace(_ other: CLKComplicationTimeTravelDirections)     mutating func intersectInPlace(_ other: CLKComplicationTimeTravelDirections)     mutating func exclusiveOrInPlace(_ other: CLKComplicationTimeTravelDirections)     func isSubsetOf(_ other: CLKComplicationTimeTravelDirections) -> Bool     func isDisjointWith(_ other: CLKComplicationTimeTravelDirections) -> Bool     func isSupersetOf(_ other: CLKComplicationTimeTravelDirections) -> Bool     mutating func subtractInPlace(_ other: CLKComplicationTimeTravelDirections)     func isStrictSupersetOf(_ other: CLKComplicationTimeTravelDirections) -> Bool     func isStrictSubsetOf(_ other: CLKComplicationTimeTravelDirections) -> Bool } extension CLKComplicationTimeTravelDirections {     func union(_ other: CLKComplicationTimeTravelDirections) -> CLKComplicationTimeTravelDirections     func intersection(_ other: CLKComplicationTimeTravelDirections) -> CLKComplicationTimeTravelDirections     func symmetricDifference(_ other: CLKComplicationTimeTravelDirections) -> CLKComplicationTimeTravelDirections } extension CLKComplicationTimeTravelDirections {     func contains(_ member: CLKComplicationTimeTravelDirections) -> Bool     mutating func insert(_ newMember: CLKComplicationTimeTravelDirections) -> (inserted: Bool, memberAfterInsert: CLKComplicationTimeTravelDirections)     mutating func remove(_ member: CLKComplicationTimeTravelDirections) -> CLKComplicationTimeTravelDirections?     mutating func update(with newMember: CLKComplicationTimeTravelDirections) -> CLKComplicationTimeTravelDirections? } extension CLKComplicationTimeTravelDirections {     convenience init()     mutating func formUnion(_ other: CLKComplicationTimeTravelDirections)     mutating func formIntersection(_ other: CLKComplicationTimeTravelDirections)     mutating func formSymmetricDifference(_ other: CLKComplicationTimeTravelDirections) } extension CLKComplicationTimeTravelDirections {     convenience init<S : Sequence where S.Iterator.Element == CLKComplicationTimeTravelDirections>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CLKComplicationTimeTravelDirections...)     mutating func subtract(_ other: CLKComplicationTimeTravelDirections)     func isSubset(of other: CLKComplicationTimeTravelDirections) -> Bool     func isSuperset(of other: CLKComplicationTimeTravelDirections) -> Bool     func isDisjoint(with other: CLKComplicationTimeTravelDirections) -> Bool     func subtracting(_ other: CLKComplicationTimeTravelDirections) -> CLKComplicationTimeTravelDirections     var isEmpty: Bool { get }     func isStrictSuperset(of other: CLKComplicationTimeTravelDirections) -> Bool     func isStrictSubset(of other: CLKComplicationTimeTravelDirections) -> Bool } ``` | OptionSet |

Modified [CLKComplicationTimeTravelDirections.backward](https://developer.apple.com/documentation/clockkit/clkcomplicationtimetraveldirections/clkcomplicationtimetraveldirectionbackward)

|  | Declaration |
| --- | --- |
| From | ``` static var Backward: CLKComplicationTimeTravelDirections { get } ``` |
| To | ``` static var backward: CLKComplicationTimeTravelDirections { get } ``` |

Modified [CLKComplicationTimeTravelDirections.forward](https://developer.apple.com/documentation/clockkit/clkcomplicationtimetraveldirections/1628096-forward)

|  | Declaration |
| --- | --- |
| From | ``` static var Forward: CLKComplicationTimeTravelDirections { get } ``` |
| To | ``` static var forward: CLKComplicationTimeTravelDirections { get } ``` |

Modified [CLKDateTextProvider](https://developer.apple.com/documentation/clockkit/clkdatetextprovider)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CLKDateTextProvider : CLKTextProvider {     convenience init(date date: NSDate, units calendarUnits: NSCalendarUnit)     class func textProviderWithDate(_ date: NSDate, units calendarUnits: NSCalendarUnit) -> Self     convenience init(date date: NSDate, units calendarUnits: NSCalendarUnit, timeZone timeZone: NSTimeZone?)     class func textProviderWithDate(_ date: NSDate, units calendarUnits: NSCalendarUnit, timeZone timeZone: NSTimeZone?) -> Self     var date: NSDate     var calendarUnits: NSCalendarUnit     var timeZone: NSTimeZone? } ``` | -- |
| To | ``` class CLKDateTextProvider : CLKTextProvider {     convenience init(date date: Date, units calendarUnits: NSCalendar.Unit)     class func withDate(_ date: Date, units calendarUnits: NSCalendar.Unit) -> Self     convenience init(date date: Date, units calendarUnits: NSCalendar.Unit, timeZone timeZone: TimeZone?)     class func withDate(_ date: Date, units calendarUnits: NSCalendar.Unit, timeZone timeZone: TimeZone?) -> Self     var date: Date     var calendarUnits: NSCalendar.Unit     var timeZone: TimeZone?     class func localizableTextProvider(withStringsFileTextKey textKey: String) -> Self     class func localizableTextProvider(withStringsFileTextKey textKey: String, shortTextKey shortTextKey: String?) -> Self     class func localizableTextProvider(withStringsFileFormatKey formatKey: String, textProviders textProviders: [CLKTextProvider]) -> Self     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CLKDateTextProvider : CVarArg { } extension CLKDateTextProvider : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CLKDateTextProvider.calendarUnits](https://developer.apple.com/documentation/clockkit/clkdatetextprovider/1627918-calendarunits)

|  | Declaration |
| --- | --- |
| From | ``` var calendarUnits: NSCalendarUnit ``` |
| To | ``` var calendarUnits: NSCalendar.Unit ``` |

Modified [CLKDateTextProvider.date](https://developer.apple.com/documentation/clockkit/clkdatetextprovider/1627911-date)

|  | Declaration |
| --- | --- |
| From | ``` var date: NSDate ``` |
| To | ``` var date: Date ``` |

Modified [CLKDateTextProvider.init(date: Date, units: NSCalendar.Unit)](https://developer.apple.com/documentation/clockkit/clkdatetextprovider/1627920-textproviderwithdate)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(date date: NSDate, units calendarUnits: NSCalendarUnit) ``` |
| To | ``` convenience init(date date: Date, units calendarUnits: NSCalendar.Unit) ``` |

Modified [CLKDateTextProvider.init(date: Date, units: NSCalendar.Unit, timeZone: TimeZone?)](https://developer.apple.com/documentation/clockkit/clkdatetextprovider/1627916-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(date date: NSDate, units calendarUnits: NSCalendarUnit, timeZone timeZone: NSTimeZone?) ``` |
| To | ``` convenience init(date date: Date, units calendarUnits: NSCalendar.Unit, timeZone timeZone: TimeZone?) ``` |

Modified [CLKDateTextProvider.timeZone](https://developer.apple.com/documentation/clockkit/clkdatetextprovider/1627927-timezone)

|  | Declaration |
| --- | --- |
| From | ``` var timeZone: NSTimeZone? ``` |
| To | ``` var timeZone: TimeZone? ``` |

Modified [CLKImageProvider](https://developer.apple.com/documentation/clockkit/clkimageprovider)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CLKImageProvider : NSObject, NSCopying {     convenience init(onePieceImage onePieceImage: UIImage)     class func imageProviderWithOnePieceImage(_ onePieceImage: UIImage) -> Self     convenience init(onePieceImage onePieceImage: UIImage, twoPieceImageBackground twoPieceImageBackground: UIImage?, twoPieceImageForeground twoPieceImageForeground: UIImage?)     class func imageProviderWithOnePieceImage(_ onePieceImage: UIImage, twoPieceImageBackground twoPieceImageBackground: UIImage?, twoPieceImageForeground twoPieceImageForeground: UIImage?) -> Self     var onePieceImage: UIImage     var tintColor: UIColor?     var twoPieceImageBackground: UIImage?     var twoPieceImageForeground: UIImage?     var accessibilityLabel: String? } ``` | NSCopying |
| To | ``` class CLKImageProvider : NSObject, NSCopying {     convenience init(onePieceImage onePieceImage: UIImage)     class func withOnePieceImage(_ onePieceImage: UIImage) -> Self     convenience init(onePieceImage onePieceImage: UIImage, twoPieceImageBackground twoPieceImageBackground: UIImage?, twoPieceImageForeground twoPieceImageForeground: UIImage?)     class func withOnePieceImage(_ onePieceImage: UIImage, twoPieceImageBackground twoPieceImageBackground: UIImage?, twoPieceImageForeground twoPieceImageForeground: UIImage?) -> Self     var onePieceImage: UIImage     var tintColor: UIColor?     var twoPieceImageBackground: UIImage?     var twoPieceImageForeground: UIImage?     var accessibilityLabel: String?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CLKImageProvider : CVarArg { } extension CLKImageProvider : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [CLKRelativeDateStyle [enum]](https://developer.apple.com/documentation/clockkit/clkrelativedatestyle)

|  | Declaration |
| --- | --- |
| From | ``` enum CLKRelativeDateStyle : Int {     case Natural     case Offset     case Timer } ``` |
| To | ``` enum CLKRelativeDateStyle : Int {     case natural     case offset     case timer } ``` |

Modified [CLKRelativeDateStyle.natural](https://developer.apple.com/documentation/clockkit/clkrelativedatestyle/natural)

|  | Declaration |
| --- | --- |
| From | ``` case Natural ``` |
| To | ``` case natural ``` |

Modified [CLKRelativeDateStyle.offset](https://developer.apple.com/documentation/clockkit/clkrelativedatestyle/clkrelativedatestyleoffset)

|  | Declaration |
| --- | --- |
| From | ``` case Offset ``` |
| To | ``` case offset ``` |

Modified [CLKRelativeDateStyle.timer](https://developer.apple.com/documentation/clockkit/clkrelativedatestyle/clkrelativedatestyletimer)

|  | Declaration |
| --- | --- |
| From | ``` case Timer ``` |
| To | ``` case timer ``` |

Modified [CLKRelativeDateTextProvider](https://developer.apple.com/documentation/clockkit/clkrelativedatetextprovider)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CLKRelativeDateTextProvider : CLKTextProvider {     convenience init(date date: NSDate, style style: CLKRelativeDateStyle, units calendarUnits: NSCalendarUnit)     class func textProviderWithDate(_ date: NSDate, style style: CLKRelativeDateStyle, units calendarUnits: NSCalendarUnit) -> Self     var date: NSDate     var relativeDateStyle: CLKRelativeDateStyle     var calendarUnits: NSCalendarUnit } ``` | -- |
| To | ``` class CLKRelativeDateTextProvider : CLKTextProvider {     convenience init(date date: Date, style style: CLKRelativeDateStyle, units calendarUnits: NSCalendar.Unit)     class func withDate(_ date: Date, style style: CLKRelativeDateStyle, units calendarUnits: NSCalendar.Unit) -> Self     var date: Date     var relativeDateStyle: CLKRelativeDateStyle     var calendarUnits: NSCalendar.Unit     class func localizableTextProvider(withStringsFileTextKey textKey: String) -> Self     class func localizableTextProvider(withStringsFileTextKey textKey: String, shortTextKey shortTextKey: String?) -> Self     class func localizableTextProvider(withStringsFileFormatKey formatKey: String, textProviders textProviders: [CLKTextProvider]) -> Self     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CLKRelativeDateTextProvider : CVarArg { } extension CLKRelativeDateTextProvider : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CLKRelativeDateTextProvider.calendarUnits](https://developer.apple.com/documentation/clockkit/clkrelativedatetextprovider/1627923-calendarunits)

|  | Declaration |
| --- | --- |
| From | ``` var calendarUnits: NSCalendarUnit ``` |
| To | ``` var calendarUnits: NSCalendar.Unit ``` |

Modified [CLKRelativeDateTextProvider.date](https://developer.apple.com/documentation/clockkit/clkrelativedatetextprovider/1627912-date)

|  | Declaration |
| --- | --- |
| From | ``` var date: NSDate ``` |
| To | ``` var date: Date ``` |

Modified [CLKRelativeDateTextProvider.init(date: Date, style: CLKRelativeDateStyle, units: NSCalendar.Unit)](https://developer.apple.com/documentation/clockkit/clkrelativedatetextprovider/1627905-textproviderwithdate)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(date date: NSDate, style style: CLKRelativeDateStyle, units calendarUnits: NSCalendarUnit) ``` |
| To | ``` convenience init(date date: Date, style style: CLKRelativeDateStyle, units calendarUnits: NSCalendar.Unit) ``` |

Modified [CLKSimpleTextProvider](https://developer.apple.com/documentation/clockkit/clksimpletextprovider)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CLKSimpleTextProvider : CLKTextProvider {     convenience init(text text: String)     class func textProviderWithText(_ text: String) -> Self     convenience init(text text: String, shortText shortText: String?)     class func textProviderWithText(_ text: String, shortText shortText: String?) -> Self     convenience init(text text: String, shortText shortText: String?, accessibilityLabel accessibilityLabel: String?)     class func textProviderWithText(_ text: String, shortText shortText: String?, accessibilityLabel accessibilityLabel: String?) -> Self     var text: String     var shortText: String?     var accessibilityLabel: String? } ``` | -- |
| To | ``` class CLKSimpleTextProvider : CLKTextProvider {     convenience init(text text: String)     class func withText(_ text: String) -> Self     convenience init(text text: String, shortText shortText: String?)     class func withText(_ text: String, shortText shortText: String?) -> Self     convenience init(text text: String, shortText shortText: String?, accessibilityLabel accessibilityLabel: String?)     class func withText(_ text: String, shortText shortText: String?, accessibilityLabel accessibilityLabel: String?) -> Self     var text: String     var shortText: String?     var accessibilityLabel: String?     class func localizableTextProvider(withStringsFileTextKey textKey: String) -> Self     class func localizableTextProvider(withStringsFileTextKey textKey: String, shortTextKey shortTextKey: String?) -> Self     class func localizableTextProvider(withStringsFileFormatKey formatKey: String, textProviders textProviders: [CLKTextProvider]) -> Self     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CLKSimpleTextProvider : CVarArg { } extension CLKSimpleTextProvider : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CLKTextProvider](https://developer.apple.com/documentation/clockkit/clktextprovider)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CLKTextProvider : NSObject, NSCopying {     var tintColor: UIColor } ``` | NSCopying |
| To | ``` class CLKTextProvider : NSObject, NSCopying {     var tintColor: UIColor     class func localizableTextProvider(withStringsFileTextKey textKey: String) -> Self     class func localizableTextProvider(withStringsFileTextKey textKey: String, shortTextKey shortTextKey: String?) -> Self     class func localizableTextProvider(withStringsFileFormatKey formatKey: String, textProviders textProviders: [CLKTextProvider]) -> Self     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CLKTextProvider : CVarArg { } extension CLKTextProvider : Equatable, Hashable {     var hashValue: Int { get } } extension CLKTextProvider {     class func localizableTextProvider(withStringsFileTextKey textKey: String) -> Self     class func localizableTextProvider(withStringsFileTextKey textKey: String, shortTextKey shortTextKey: String?) -> Self     class func localizableTextProvider(withStringsFileFormatKey formatKey: String, textProviders textProviders: [CLKTextProvider]) -> Self } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [CLKTimeIntervalTextProvider](https://developer.apple.com/documentation/clockkit/clktimeintervaltextprovider)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CLKTimeIntervalTextProvider : CLKTextProvider {     convenience init(startDate startDate: NSDate, endDate endDate: NSDate)     class func textProviderWithStartDate(_ startDate: NSDate, endDate endDate: NSDate) -> Self     convenience init(startDate startDate: NSDate, endDate endDate: NSDate, timeZone timeZone: NSTimeZone?)     class func textProviderWithStartDate(_ startDate: NSDate, endDate endDate: NSDate, timeZone timeZone: NSTimeZone?) -> Self     var startDate: NSDate     var endDate: NSDate     var timeZone: NSTimeZone? } ``` | -- |
| To | ``` class CLKTimeIntervalTextProvider : CLKTextProvider {     convenience init(start startDate: Date, end endDate: Date)     class func withStart(_ startDate: Date, end endDate: Date) -> Self     convenience init(start startDate: Date, end endDate: Date, timeZone timeZone: TimeZone?)     class func withStart(_ startDate: Date, end endDate: Date, timeZone timeZone: TimeZone?) -> Self     var startDate: Date     var endDate: Date     var timeZone: TimeZone?     class func localizableTextProvider(withStringsFileTextKey textKey: String) -> Self     class func localizableTextProvider(withStringsFileTextKey textKey: String, shortTextKey shortTextKey: String?) -> Self     class func localizableTextProvider(withStringsFileFormatKey formatKey: String, textProviders textProviders: [CLKTextProvider]) -> Self     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CLKTimeIntervalTextProvider : CVarArg { } extension CLKTimeIntervalTextProvider : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CLKTimeIntervalTextProvider.endDate](https://developer.apple.com/documentation/clockkit/clktimeintervaltextprovider/1627932-enddate)

|  | Declaration |
| --- | --- |
| From | ``` var endDate: NSDate ``` |
| To | ``` var endDate: Date ``` |

Modified [CLKTimeIntervalTextProvider.init(start: Date, end: Date)](https://developer.apple.com/documentation/clockkit/clktimeintervaltextprovider/1627928-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(startDate startDate: NSDate, endDate endDate: NSDate) ``` |
| To | ``` convenience init(start startDate: Date, end endDate: Date) ``` |

Modified [CLKTimeIntervalTextProvider.init(start: Date, end: Date, timeZone: TimeZone?)](https://developer.apple.com/documentation/clockkit/clktimeintervaltextprovider/1627897-textproviderwithstartdate)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(startDate startDate: NSDate, endDate endDate: NSDate, timeZone timeZone: NSTimeZone?) ``` |
| To | ``` convenience init(start startDate: Date, end endDate: Date, timeZone timeZone: TimeZone?) ``` |

Modified [CLKTimeIntervalTextProvider.startDate](https://developer.apple.com/documentation/clockkit/clktimeintervaltextprovider/1627925-startdate)

|  | Declaration |
| --- | --- |
| From | ``` var startDate: NSDate ``` |
| To | ``` var startDate: Date ``` |

Modified [CLKTimeIntervalTextProvider.timeZone](https://developer.apple.com/documentation/clockkit/clktimeintervaltextprovider/1627908-timezone)

|  | Declaration |
| --- | --- |
| From | ``` var timeZone: NSTimeZone? ``` |
| To | ``` var timeZone: TimeZone? ``` |

Modified [CLKTimeTextProvider](https://developer.apple.com/documentation/clockkit/clktimetextprovider)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CLKTimeTextProvider : CLKTextProvider {     convenience init(date date: NSDate)     class func textProviderWithDate(_ date: NSDate) -> Self     convenience init(date date: NSDate, timeZone timeZone: NSTimeZone?)     class func textProviderWithDate(_ date: NSDate, timeZone timeZone: NSTimeZone?) -> Self     var date: NSDate     var timeZone: NSTimeZone? } ``` | -- |
| To | ``` class CLKTimeTextProvider : CLKTextProvider {     convenience init(date date: Date)     class func withDate(_ date: Date) -> Self     convenience init(date date: Date, timeZone timeZone: TimeZone?)     class func withDate(_ date: Date, timeZone timeZone: TimeZone?) -> Self     var date: Date     var timeZone: TimeZone?     class func localizableTextProvider(withStringsFileTextKey textKey: String) -> Self     class func localizableTextProvider(withStringsFileTextKey textKey: String, shortTextKey shortTextKey: String?) -> Self     class func localizableTextProvider(withStringsFileFormatKey formatKey: String, textProviders textProviders: [CLKTextProvider]) -> Self     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CLKTimeTextProvider : CVarArg { } extension CLKTimeTextProvider : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CLKTimeTextProvider.date](https://developer.apple.com/documentation/clockkit/clktimetextprovider/1627903-date)

|  | Declaration |
| --- | --- |
| From | ``` var date: NSDate ``` |
| To | ``` var date: Date ``` |

Modified [CLKTimeTextProvider.init(date: Date)](https://developer.apple.com/documentation/clockkit/clktimetextprovider/1627898-textproviderwithdate)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(date date: NSDate) ``` |
| To | ``` convenience init(date date: Date) ``` |

Modified [CLKTimeTextProvider.init(date: Date, timeZone: TimeZone?)](https://developer.apple.com/documentation/clockkit/clktimetextprovider/1627926-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(date date: NSDate, timeZone timeZone: NSTimeZone?) ``` |
| To | ``` convenience init(date date: Date, timeZone timeZone: TimeZone?) ``` |

Modified [CLKTimeTextProvider.timeZone](https://developer.apple.com/documentation/clockkit/clktimetextprovider/1627913-timezone)

|  | Declaration |
| --- | --- |
| From | ``` var timeZone: NSTimeZone? ``` |
| To | ``` var timeZone: TimeZone? ``` |

Modified [NSNotification.Name.CLKComplicationServerActiveComplicationsDidChange](https://developer.apple.com/documentation/foundation/nsnotification/name/1627889-clkcomplicationserveractivecompl)

|  | Name | Declaration |
| --- | --- | --- |
| From | CLKComplicationServerActiveComplicationsDidChangeNotification | ``` let CLKComplicationServerActiveComplicationsDidChangeNotification: String ``` |
| To | CLKComplicationServerActiveComplicationsDidChange | ``` static let CLKComplicationServerActiveComplicationsDidChange: NSNotification.Name ``` |

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
