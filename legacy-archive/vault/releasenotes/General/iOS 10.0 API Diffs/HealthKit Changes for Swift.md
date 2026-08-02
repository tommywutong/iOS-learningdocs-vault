---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/HealthKit.html
archived_at: '2026-07-18T02:55:28.235152Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# HealthKit Changes for Swift

### HealthKit

Removed [HKQueryOptions.None](https://developer.apple.com/documentation/healthkit/hkqueryoptions/hkqueryoptionnone)Removed [HKStatisticsOptions.None](https://developer.apple.com/documentation/healthkit/hkstatisticsoptions/hkstatisticsoptionnone)Added [HKCategoryTypeIdentifier [struct]](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier)Added [HKCategoryTypeIdentifier.init(rawValue: String)](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/1780522-init)Added [HKCategoryTypeIdentifier.mindfulSession](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifiermindfulsession)Added [HKCategoryValueSleepAnalysis.awake](https://developer.apple.com/documentation/healthkit/hkcategoryvaluesleepanalysis/awake)Added [HKCDADocument](https://developer.apple.com/documentation/healthkit/hkcdadocument)Added [HKCDADocument.authorName](https://developer.apple.com/documentation/healthkit/hkcdadocument/1779381-authorname)Added [HKCDADocument.custodianName](https://developer.apple.com/documentation/healthkit/hkcdadocument/1779390-custodianname)Added [HKCDADocument.documentData](https://developer.apple.com/documentation/healthkit/hkcdadocument/1779391-documentdata)Added [HKCDADocument.patientName](https://developer.apple.com/documentation/healthkit/hkcdadocument/1779384-patientname)Added [HKCDADocument.title](https://developer.apple.com/documentation/healthkit/hkcdadocument/1779387-title)Added [HKCDADocumentSample](https://developer.apple.com/documentation/healthkit/hkcdadocumentsample)Added [HKCDADocumentSample.document](https://developer.apple.com/documentation/healthkit/hkcdadocumentsample/1779383-document)Added [HKCDADocumentSample.init(data: Data, start: Date, end: Date, metadata: [String : Any]?) throws](https://developer.apple.com/documentation/healthkit/hkcdadocumentsample/1779395-init)Added [HKCharacteristicTypeIdentifier [struct]](https://developer.apple.com/documentation/healthkit/hkcharacteristictypeidentifier)Added [HKCharacteristicTypeIdentifier.init(rawValue: String)](https://developer.apple.com/documentation/healthkit/hkcharacteristictypeidentifier/1780518-init)Added [HKCharacteristicTypeIdentifier.wheelchairUse](https://developer.apple.com/documentation/healthkit/hkcharacteristictypeidentifier/1648572-wheelchairuse)Added [HKCorrelationTypeIdentifier [struct]](https://developer.apple.com/documentation/healthkit/hkcorrelationtypeidentifier)Added [HKCorrelationTypeIdentifier.init(rawValue: String)](https://developer.apple.com/documentation/healthkit/hkcorrelationtypeidentifier/1780520-init)Added [HKDocumentQuery](https://developer.apple.com/documentation/healthkit/hkdocumentquery)Added [HKDocumentQuery.includeDocumentData](https://developer.apple.com/documentation/healthkit/hkdocumentquery/1779564-includedocumentdata)Added [HKDocumentQuery.init(documentType: HKDocumentType, predicate: NSPredicate?, limit: Int, sortDescriptors: [NSSortDescriptor]?, includeDocumentData: Bool, resultsHandler: (HKDocumentQuery, [HKDocumentSample]?, Bool, Error?) -> Swift.Void)](https://developer.apple.com/documentation/healthkit/hkdocumentquery/1779561-initwithdocumenttype)Added [HKDocumentQuery.limit](https://developer.apple.com/documentation/healthkit/hkdocumentquery/1779563-limit)Added [HKDocumentQuery.sortDescriptors](https://developer.apple.com/documentation/healthkit/hkdocumentquery/1779560-sortdescriptors)Added [HKDocumentSample](https://developer.apple.com/documentation/healthkit/hkdocumentsample)Added [HKDocumentSample.documentType](https://developer.apple.com/documentation/healthkit/hkdocumentsample/1779250-documenttype)Added [HKDocumentType](https://developer.apple.com/documentation/healthkit/hkdocumenttype)Added [HKDocumentTypeIdentifier [struct]](https://developer.apple.com/documentation/healthkit/hkdocumenttypeidentifier)Added [HKDocumentTypeIdentifier.CDA](https://developer.apple.com/documentation/healthkit/hkdocumenttypeidentifiercda)Added [HKDocumentTypeIdentifier.init(rawValue: String)](https://developer.apple.com/documentation/healthkit/hkdocumenttypeidentifier/1780521-init)Added [HKError [struct]](https://developer.apple.com/documentation/healthkit/hkerror)Added [HKError.errorAnotherWorkoutSessionStarted](https://developer.apple.com/documentation/healthkit/hkerror/2320687-erroranotherworkoutsessionstarte)Added [HKError.errorAuthorizationDenied](https://developer.apple.com/documentation/healthkit/hkerror/2320689-errorauthorizationdenied)Added [HKError.errorAuthorizationNotDetermined](https://developer.apple.com/documentation/healthkit/hkerror/2320688-errorauthorizationnotdetermined)Added [HKError.errorDatabaseInaccessible](https://developer.apple.com/documentation/healthkit/hkerror/2320684-errordatabaseinaccessible)Added [HKError.errorHealthDataRestricted](https://developer.apple.com/documentation/healthkit/hkerror/2320683-errorhealthdatarestricted)Added [HKError.errorHealthDataUnavailable](https://developer.apple.com/documentation/healthkit/hkerror/2320691-errorhealthdataunavailable)Added [HKError.errorInvalidArgument](https://developer.apple.com/documentation/healthkit/hkerror/2320686-errorinvalidargument)Added [HKError.errorUserCanceled](https://developer.apple.com/documentation/healthkit/hkerror/2320685-errorusercanceled)Added [HKError.errorUserExitedWorkoutSession](https://developer.apple.com/documentation/healthkit/hkerror/2320692-erroruserexitedworkoutsession)Added HKError.init(_nsError: NSError)Added [HKError.noError](https://developer.apple.com/documentation/healthkit/hkerror/2320690-noerror)Added [HKHealthStore.dateOfBirthComponents() throws -> DateComponents](https://developer.apple.com/documentation/healthkit/hkhealthstore/1648357-dateofbirthcomponents)Added [HKHealthStore.startWatchApp(with: HKWorkoutConfiguration, completion: (Bool, Error?) -> Swift.Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1648358-startwatchapp)Added [HKHealthStore.wheelchairUse() throws -> HKWheelchairUseObject](https://developer.apple.com/documentation/healthkit/hkhealthstore/1648356-wheelchairusewitherror)Added [HKObjectType.documentType(forIdentifier: HKDocumentTypeIdentifier) -> HKDocumentType? [class]](https://developer.apple.com/documentation/healthkit/hkobjecttype/1778757-documenttypeforidentifier)Added [HKQuantityTypeIdentifier [struct]](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier)Added [HKQuantityTypeIdentifier.distanceSwimming](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierdistanceswimming)Added [HKQuantityTypeIdentifier.distanceWheelchair](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierdistancewheelchair)Added [HKQuantityTypeIdentifier.init(rawValue: String)](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1780519-init)Added [HKQuantityTypeIdentifier.pushCount](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierpushcount)Added [HKQuantityTypeIdentifier.swimmingStrokeCount](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/2344687-swimmingstrokecount)Added [HKQuery.predicateForWorkouts(with: NSComparisonPredicate.Operator, totalSwimmingStrokeCount: HKQuantity) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/2344688-predicateforworkouts)Added [HKSwimmingStrokeStyle [enum]](https://developer.apple.com/documentation/healthkit/hkswimmingstrokestyle)Added [HKSwimmingStrokeStyle.backstroke](https://developer.apple.com/documentation/healthkit/hkswimmingstrokestyle/hkswimmingstrokestylebackstroke)Added [HKSwimmingStrokeStyle.breaststroke](https://developer.apple.com/documentation/healthkit/hkswimmingstrokestyle/breaststroke)Added [HKSwimmingStrokeStyle.butterfly](https://developer.apple.com/documentation/healthkit/hkswimmingstrokestyle/hkswimmingstrokestylebutterfly)Added [HKSwimmingStrokeStyle.freestyle](https://developer.apple.com/documentation/healthkit/hkswimmingstrokestyle/hkswimmingstrokestylefreestyle)Added [HKSwimmingStrokeStyle.mixed](https://developer.apple.com/documentation/healthkit/hkswimmingstrokestyle/mixed)Added [HKSwimmingStrokeStyle.unknown](https://developer.apple.com/documentation/healthkit/hkswimmingstrokestyle/hkswimmingstrokestyleunknown)Added [HKWeatherCondition [enum]](https://developer.apple.com/documentation/healthkit/hkweathercondition)Added [HKWeatherCondition.blustery](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditionblustery)Added [HKWeatherCondition.clear](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditionclear)Added [HKWeatherCondition.cloudy](https://developer.apple.com/documentation/healthkit/hkweathercondition/cloudy)Added [HKWeatherCondition.drizzle](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditiondrizzle)Added [HKWeatherCondition.dust](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditiondust)Added [HKWeatherCondition.fair](https://developer.apple.com/documentation/healthkit/hkweathercondition/fair)Added [HKWeatherCondition.foggy](https://developer.apple.com/documentation/healthkit/hkweathercondition/foggy)Added [HKWeatherCondition.freezingDrizzle](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditionfreezingdrizzle)Added [HKWeatherCondition.freezingRain](https://developer.apple.com/documentation/healthkit/hkweathercondition/freezingrain)Added [HKWeatherCondition.hail](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditionhail)Added [HKWeatherCondition.haze](https://developer.apple.com/documentation/healthkit/hkweathercondition/haze)Added [HKWeatherCondition.hurricane](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditionhurricane)Added [HKWeatherCondition.mixedRainAndHail](https://developer.apple.com/documentation/healthkit/hkweathercondition/mixedrainandhail)Added [HKWeatherCondition.mixedRainAndSleet](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditionmixedrainandsleet)Added [HKWeatherCondition.mixedRainAndSnow](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditionmixedrainandsnow)Added [HKWeatherCondition.mixedSnowAndSleet](https://developer.apple.com/documentation/healthkit/hkweathercondition/mixedsnowandsleet)Added [HKWeatherCondition.mostlyCloudy](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditionmostlycloudy)Added [HKWeatherCondition.none](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditionnone)Added [HKWeatherCondition.partlyCloudy](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditionpartlycloudy)Added [HKWeatherCondition.scatteredShowers](https://developer.apple.com/documentation/healthkit/hkweathercondition/scatteredshowers)Added [HKWeatherCondition.showers](https://developer.apple.com/documentation/healthkit/hkweathercondition/showers)Added [HKWeatherCondition.sleet](https://developer.apple.com/documentation/healthkit/hkweathercondition/sleet)Added [HKWeatherCondition.smoky](https://developer.apple.com/documentation/healthkit/hkweathercondition/smoky)Added [HKWeatherCondition.snow](https://developer.apple.com/documentation/healthkit/hkweathercondition/snow)Added [HKWeatherCondition.thunderstorms](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditionthunderstorms)Added [HKWeatherCondition.tornado](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditiontornado)Added [HKWeatherCondition.tropicalStorm](https://developer.apple.com/documentation/healthkit/hkweathercondition/tropicalstorm)Added [HKWeatherCondition.windy](https://developer.apple.com/documentation/healthkit/hkweathercondition/windy)Added [HKWheelchairUse [enum]](https://developer.apple.com/documentation/healthkit/hkwheelchairuse)Added [HKWheelchairUse.no](https://developer.apple.com/documentation/healthkit/hkwheelchairuse/no)Added [HKWheelchairUse.notSet](https://developer.apple.com/documentation/healthkit/hkwheelchairuse/notset)Added [HKWheelchairUse.yes](https://developer.apple.com/documentation/healthkit/hkwheelchairuse/hkwheelchairuseyes)Added [HKWheelchairUseObject](https://developer.apple.com/documentation/healthkit/hkwheelchairuseobject)Added [HKWheelchairUseObject.wheelchairUse](https://developer.apple.com/documentation/healthkit/hkwheelchairuseobject/1649241-wheelchairuse)Added [HKWorkout.init(activityType: HKWorkoutActivityType, start: Date, end: Date, workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, totalSwimmingStrokeCount: HKQuantity?, device: HKDevice?, metadata: [String : Any]?)](https://developer.apple.com/documentation/healthkit/hkworkout/2341569-workoutwithactivitytype)Added [HKWorkout.totalSwimmingStrokeCount](https://developer.apple.com/documentation/healthkit/hkworkout/2341561-totalswimmingstrokecount)Added [HKWorkoutActivityType.barre](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/barre)Added [HKWorkoutActivityType.coreTraining](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypecoretraining)Added [HKWorkoutActivityType.crossCountrySkiing](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/crosscountryskiing)Added [HKWorkoutActivityType.downhillSkiing](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypedownhillskiing)Added [HKWorkoutActivityType.flexibility](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypeflexibility)Added [HKWorkoutActivityType.highIntensityIntervalTraining](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypehighintensityintervaltraining)Added [HKWorkoutActivityType.jumpRope](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/jumprope)Added [HKWorkoutActivityType.kickboxing](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypekickboxing)Added [HKWorkoutActivityType.pilates](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/pilates)Added [HKWorkoutActivityType.snowboarding](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/snowboarding)Added [HKWorkoutActivityType.stairs](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/stairs)Added [HKWorkoutActivityType.stepTraining](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypesteptraining)Added [HKWorkoutActivityType.wheelchairRunPace](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/wheelchairrunpace)Added [HKWorkoutActivityType.wheelchairWalkPace](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypewheelchairwalkpace)Added [HKWorkoutConfiguration](https://developer.apple.com/documentation/healthkit/hkworkoutconfiguration)Added [HKWorkoutConfiguration.activityType](https://developer.apple.com/documentation/healthkit/hkworkoutconfiguration/1649492-activitytype)Added [HKWorkoutConfiguration.lapLength](https://developer.apple.com/documentation/healthkit/hkworkoutconfiguration/2342795-laplength)Added [HKWorkoutConfiguration.locationType](https://developer.apple.com/documentation/healthkit/hkworkoutconfiguration/1649491-locationtype)Added [HKWorkoutConfiguration.swimmingLocationType](https://developer.apple.com/documentation/healthkit/hkworkoutconfiguration/2342785-swimminglocationtype)Added [HKWorkoutEvent.init(type: HKWorkoutEventType, date: Date, metadata: [String : Any])](https://developer.apple.com/documentation/healthkit/hkworkoutevent/1649819-workouteventwithtype)Added [HKWorkoutEvent.metadata](https://developer.apple.com/documentation/healthkit/hkworkoutevent/1649817-metadata)Added [HKWorkoutEventType.lap](https://developer.apple.com/documentation/healthkit/hkworkouteventtype/hkworkouteventtypelap)Added [HKWorkoutEventType.marker](https://developer.apple.com/documentation/healthkit/hkworkouteventtype/hkworkouteventtypemarker)Added [HKWorkoutEventType.motionPaused](https://developer.apple.com/documentation/healthkit/hkworkouteventtype/motionpaused)Added [HKWorkoutEventType.motionResumed](https://developer.apple.com/documentation/healthkit/hkworkouteventtype/hkworkouteventtypemotionresumed)Added [HKWorkoutSessionLocationType [enum]](https://developer.apple.com/documentation/healthkit/hkworkoutsessionlocationtype)Added [HKWorkoutSessionLocationType.indoor](https://developer.apple.com/documentation/healthkit/hkworkoutsessionlocationtype/indoor)Added [HKWorkoutSessionLocationType.outdoor](https://developer.apple.com/documentation/healthkit/hkworkoutsessionlocationtype/outdoor)Added [HKWorkoutSessionLocationType.unknown](https://developer.apple.com/documentation/healthkit/hkworkoutsessionlocationtype/hkworkoutsessionlocationtypeunknown)Added [HKWorkoutSwimmingLocationType [enum]](https://developer.apple.com/documentation/healthkit/hkworkoutswimminglocationtype)Added [HKWorkoutSwimmingLocationType.openWater](https://developer.apple.com/documentation/healthkit/hkworkoutswimminglocationtype/openwater)Added [HKWorkoutSwimmingLocationType.pool](https://developer.apple.com/documentation/healthkit/hkworkoutswimminglocationtype/hkworkoutswimminglocationtypepool)Added [HKWorkoutSwimmingLocationType.unknown](https://developer.apple.com/documentation/healthkit/hkworkoutswimminglocationtype/unknown)Added [HKDetailedCDAValidationErrorKey](https://developer.apple.com/documentation/healthkit/hkdetailedcdavalidationerrorkey)Added [HKMetadataKeyLapLength](https://developer.apple.com/documentation/healthkit/hkmetadatakeylaplength)Added [HKMetadataKeySwimmingLocationType](https://developer.apple.com/documentation/healthkit/hkmetadatakeyswimminglocationtype)Added [HKMetadataKeySwimmingStrokeStyle](https://developer.apple.com/documentation/healthkit/hkmetadatakeyswimmingstrokestyle)Added [HKMetadataKeyWeatherCondition](https://developer.apple.com/documentation/healthkit/hkmetadatakeyweathercondition)Added [HKMetadataKeyWeatherHumidity](https://developer.apple.com/documentation/healthkit/hkmetadatakeyweatherhumidity)Added [HKMetadataKeyWeatherTemperature](https://developer.apple.com/documentation/healthkit/hkmetadatakeyweathertemperature)Added [HKPredicateKeyPathCDAAuthorName](https://developer.apple.com/documentation/healthkit/hkpredicatekeypathcdaauthorname)Added [HKPredicateKeyPathCDACustodianName](https://developer.apple.com/documentation/healthkit/hkpredicatekeypathcdacustodianname)Added [HKPredicateKeyPathCDAPatientName](https://developer.apple.com/documentation/healthkit/hkpredicatekeypathcdapatientname)Added [HKPredicateKeyPathCDATitle](https://developer.apple.com/documentation/healthkit/hkpredicatekeypathcdatitle)Added [HKPredicateKeyPathWorkoutTotalSwimmingStrokeCount](https://developer.apple.com/documentation/healthkit/hkpredicatekeypathworkouttotalswimmingstrokecount)Added [HKWorkoutSortIdentifierTotalSwimmingStrokeCount](https://developer.apple.com/documentation/healthkit/hkworkoutsortidentifiertotalswimmingstrokecount)Modified [HKActivitySummary](https://developer.apple.com/documentation/healthkit/hkactivitysummary)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKActivitySummary : NSObject, NSSecureCoding, NSCopying {     func dateComponentsForCalendar(_ calendar: NSCalendar) -> NSDateComponents     var activeEnergyBurned: HKQuantity     var appleExerciseTime: HKQuantity     var appleStandHours: HKQuantity     var activeEnergyBurnedGoal: HKQuantity     var appleExerciseTimeGoal: HKQuantity     var appleStandHoursGoal: HKQuantity } ``` | NSCopying, NSSecureCoding |
| To | ``` class HKActivitySummary : NSObject, NSSecureCoding, NSCopying {     func dateComponents(for calendar: Calendar) -> DateComponents     var activeEnergyBurned: HKQuantity     var appleExerciseTime: HKQuantity     var appleStandHours: HKQuantity     var activeEnergyBurnedGoal: HKQuantity     var appleExerciseTimeGoal: HKQuantity     var appleStandHoursGoal: HKQuantity     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HKActivitySummary : CVarArg { } extension HKActivitySummary : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [HKActivitySummary.dateComponents(for: Calendar) -> DateComponents](https://developer.apple.com/documentation/healthkit/hkactivitysummary/1615628-datecomponents)

|  | Declaration |
| --- | --- |
| From | ``` func dateComponentsForCalendar(_ calendar: NSCalendar) -> NSDateComponents ``` |
| To | ``` func dateComponents(for calendar: Calendar) -> DateComponents ``` |

Modified [HKActivitySummaryQuery](https://developer.apple.com/documentation/healthkit/hkactivitysummaryquery)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKActivitySummaryQuery : HKQuery {     var updateHandler: ((HKActivitySummaryQuery, [HKActivitySummary]?, NSError?) -> Void)?     init(predicate predicate: NSPredicate?, resultsHandler handler: (HKActivitySummaryQuery, [HKActivitySummary]?, NSError?) -> Void) } ``` | -- |
| To | ``` class HKActivitySummaryQuery : HKQuery {     var updateHandler: ((HKActivitySummaryQuery, [HKActivitySummary]?, Error?) -> Swift.Void)?     init(predicate predicate: NSPredicate?, resultsHandler handler: @escaping (HKActivitySummaryQuery, [HKActivitySummary]?, Error?) -> Swift.Void)     class func predicateForActivitySummary(with dateComponents: DateComponents) -> NSPredicate     class func predicate(forActivitySummariesBetweenStart startDateComponents: DateComponents, end endDateComponents: DateComponents) -> NSPredicate     class func predicateForWorkouts(with workoutActivityType: HKWorkoutActivityType) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, duration duration: TimeInterval) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalEnergyBurned totalEnergyBurned: HKQuantity) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalDistance totalDistance: HKQuantity) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalSwimmingStrokeCount totalSwimmingStrokeCount: HKQuantity) -> NSPredicate     class func predicateForCategorySamples(with operatorType: NSComparisonPredicate.Operator, value value: Int) -> NSPredicate     class func predicateForQuantitySamples(with operatorType: NSComparisonPredicate.Operator, quantity quantity: HKQuantity) -> NSPredicate     class func predicateForSamples(withStart startDate: Date?, end endDate: Date?, options options: HKQueryOptions = []) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String, allowedValues allowedValues: [Any]) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String, operatorType operatorType: NSComparisonPredicate.Operator, value value: Any) -> NSPredicate     class func predicateForObjects(from source: HKSource) -> NSPredicate     class func predicateForObjects(from sources: Set<HKSource>) -> NSPredicate     class func predicateForObjects(from sourceRevisions: Set<HKSourceRevision>) -> NSPredicate     class func predicateForObjects(from devices: Set<HKDevice>) -> NSPredicate     class func predicateForObjects(withDeviceProperty key: String, allowedValues allowedValues: Set<String>) -> NSPredicate     class func predicateForObject(with UUID: UUID) -> NSPredicate     class func predicateForObjects(with UUIDs: Set<UUID>) -> NSPredicate     class func predicateForObjectsWithNoCorrelation() -> NSPredicate     class func predicateForObjects(from workout: HKWorkout) -> NSPredicate     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HKActivitySummaryQuery : CVarArg { } extension HKActivitySummaryQuery : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [HKActivitySummaryQuery.init(predicate: NSPredicate?, resultsHandler: (HKActivitySummaryQuery, [HKActivitySummary]?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/healthkit/hkactivitysummaryquery/1615312-init)

|  | Declaration |
| --- | --- |
| From | ``` init(predicate predicate: NSPredicate?, resultsHandler handler: (HKActivitySummaryQuery, [HKActivitySummary]?, NSError?) -> Void) ``` |
| To | ``` init(predicate predicate: NSPredicate?, resultsHandler handler: @escaping (HKActivitySummaryQuery, [HKActivitySummary]?, Error?) -> Swift.Void) ``` |

Modified [HKActivitySummaryQuery.updateHandler](https://developer.apple.com/documentation/healthkit/hkactivitysummaryquery/1615203-updatehandler)

|  | Declaration |
| --- | --- |
| From | ``` var updateHandler: ((HKActivitySummaryQuery, [HKActivitySummary]?, NSError?) -> Void)? ``` |
| To | ``` var updateHandler: ((HKActivitySummaryQuery, [HKActivitySummary]?, Error?) -> Swift.Void)? ``` |

Modified [HKAnchoredObjectQuery](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquery)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKAnchoredObjectQuery : HKQuery {     var updateHandler: ((HKAnchoredObjectQuery, [HKSample]?, [HKDeletedObject]?, HKQueryAnchor?, NSError?) -> Void)?     init(type type: HKSampleType, predicate predicate: NSPredicate?, anchor anchor: Int, limit limit: Int, completionHandler handler: (HKAnchoredObjectQuery, [HKSample]?, Int, NSError?) -> Void)     init(type type: HKSampleType, predicate predicate: NSPredicate?, anchor anchor: HKQueryAnchor?, limit limit: Int, resultsHandler handler: (HKAnchoredObjectQuery, [HKSample]?, [HKDeletedObject]?, HKQueryAnchor?, NSError?) -> Void) } ``` | -- |
| To | ``` class HKAnchoredObjectQuery : HKQuery {     var updateHandler: ((HKAnchoredObjectQuery, [HKSample]?, [HKDeletedObject]?, HKQueryAnchor?, Error?) -> Swift.Void)?     init(type type: HKSampleType, predicate predicate: NSPredicate?, anchor anchor: HKQueryAnchor?, limit limit: Int, resultsHandler handler: @escaping (HKAnchoredObjectQuery, [HKSample]?, [HKDeletedObject]?, HKQueryAnchor?, Error?) -> Swift.Void)     init(type type: HKSampleType, predicate predicate: NSPredicate?, anchor anchor: Int, limit limit: Int, completionHandler handler: @escaping (HKAnchoredObjectQuery, [HKSample]?, Int, Error?) -> Swift.Void)     class func predicateForActivitySummary(with dateComponents: DateComponents) -> NSPredicate     class func predicate(forActivitySummariesBetweenStart startDateComponents: DateComponents, end endDateComponents: DateComponents) -> NSPredicate     class func predicateForWorkouts(with workoutActivityType: HKWorkoutActivityType) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, duration duration: TimeInterval) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalEnergyBurned totalEnergyBurned: HKQuantity) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalDistance totalDistance: HKQuantity) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalSwimmingStrokeCount totalSwimmingStrokeCount: HKQuantity) -> NSPredicate     class func predicateForCategorySamples(with operatorType: NSComparisonPredicate.Operator, value value: Int) -> NSPredicate     class func predicateForQuantitySamples(with operatorType: NSComparisonPredicate.Operator, quantity quantity: HKQuantity) -> NSPredicate     class func predicateForSamples(withStart startDate: Date?, end endDate: Date?, options options: HKQueryOptions = []) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String, allowedValues allowedValues: [Any]) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String, operatorType operatorType: NSComparisonPredicate.Operator, value value: Any) -> NSPredicate     class func predicateForObjects(from source: HKSource) -> NSPredicate     class func predicateForObjects(from sources: Set<HKSource>) -> NSPredicate     class func predicateForObjects(from sourceRevisions: Set<HKSourceRevision>) -> NSPredicate     class func predicateForObjects(from devices: Set<HKDevice>) -> NSPredicate     class func predicateForObjects(withDeviceProperty key: String, allowedValues allowedValues: Set<String>) -> NSPredicate     class func predicateForObject(with UUID: UUID) -> NSPredicate     class func predicateForObjects(with UUIDs: Set<UUID>) -> NSPredicate     class func predicateForObjectsWithNoCorrelation() -> NSPredicate     class func predicateForObjects(from workout: HKWorkout) -> NSPredicate     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HKAnchoredObjectQuery : CVarArg { } extension HKAnchoredObjectQuery : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [HKAnchoredObjectQuery.init(type: HKSampleType, predicate: NSPredicate?, anchor: Int, limit: Int, completionHandler: (HKAnchoredObjectQuery, [HKSample]?, Int, Error?) -> Swift.Void)](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquery/1615388-initwithtype)

|  | Declaration |
| --- | --- |
| From | ``` init(type type: HKSampleType, predicate predicate: NSPredicate?, anchor anchor: Int, limit limit: Int, completionHandler handler: (HKAnchoredObjectQuery, [HKSample]?, Int, NSError?) -> Void) ``` |
| To | ``` init(type type: HKSampleType, predicate predicate: NSPredicate?, anchor anchor: Int, limit limit: Int, completionHandler handler: @escaping (HKAnchoredObjectQuery, [HKSample]?, Int, Error?) -> Swift.Void) ``` |

Modified [HKAnchoredObjectQuery.init(type: HKSampleType, predicate: NSPredicate?, anchor: HKQueryAnchor?, limit: Int, resultsHandler: (HKAnchoredObjectQuery, [HKSample]?, [HKDeletedObject]?, HKQueryAnchor?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquery/1615071-initwithtype)

|  | Declaration |
| --- | --- |
| From | ``` init(type type: HKSampleType, predicate predicate: NSPredicate?, anchor anchor: HKQueryAnchor?, limit limit: Int, resultsHandler handler: (HKAnchoredObjectQuery, [HKSample]?, [HKDeletedObject]?, HKQueryAnchor?, NSError?) -> Void) ``` |
| To | ``` init(type type: HKSampleType, predicate predicate: NSPredicate?, anchor anchor: HKQueryAnchor?, limit limit: Int, resultsHandler handler: @escaping (HKAnchoredObjectQuery, [HKSample]?, [HKDeletedObject]?, HKQueryAnchor?, Error?) -> Swift.Void) ``` |

Modified [HKAnchoredObjectQuery.updateHandler](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquery/1615691-updatehandler)

|  | Declaration |
| --- | --- |
| From | ``` var updateHandler: ((HKAnchoredObjectQuery, [HKSample]?, [HKDeletedObject]?, HKQueryAnchor?, NSError?) -> Void)? ``` |
| To | ``` var updateHandler: ((HKAnchoredObjectQuery, [HKSample]?, [HKDeletedObject]?, HKQueryAnchor?, Error?) -> Swift.Void)? ``` |

Modified [HKAuthorizationStatus [enum]](https://developer.apple.com/documentation/healthkit/hkauthorizationstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum HKAuthorizationStatus : Int {     case NotDetermined     case SharingDenied     case SharingAuthorized } ``` |
| To | ``` enum HKAuthorizationStatus : Int {     case notDetermined     case sharingDenied     case sharingAuthorized } ``` |

Modified [HKAuthorizationStatus.notDetermined](https://developer.apple.com/documentation/healthkit/hkauthorizationstatus/hkauthorizationstatusnotdetermined)

|  | Declaration |
| --- | --- |
| From | ``` case NotDetermined ``` |
| To | ``` case notDetermined ``` |

Modified [HKAuthorizationStatus.sharingAuthorized](https://developer.apple.com/documentation/healthkit/hkauthorizationstatus/sharingauthorized)

|  | Declaration |
| --- | --- |
| From | ``` case SharingAuthorized ``` |
| To | ``` case sharingAuthorized ``` |

Modified [HKAuthorizationStatus.sharingDenied](https://developer.apple.com/documentation/healthkit/hkauthorizationstatus/sharingdenied)

|  | Declaration |
| --- | --- |
| From | ``` case SharingDenied ``` |
| To | ``` case sharingDenied ``` |

Modified [HKBiologicalSex [enum]](https://developer.apple.com/documentation/healthkit/hkbiologicalsex)

|  | Declaration |
| --- | --- |
| From | ``` enum HKBiologicalSex : Int {     case NotSet     case Female     case Male     case Other } ``` |
| To | ``` enum HKBiologicalSex : Int {     case notSet     case female     case male     case other } ``` |

Modified [HKBiologicalSex.female](https://developer.apple.com/documentation/healthkit/hkbiologicalsex/female)

|  | Declaration |
| --- | --- |
| From | ``` case Female ``` |
| To | ``` case female ``` |

Modified [HKBiologicalSex.male](https://developer.apple.com/documentation/healthkit/hkbiologicalsex/hkbiologicalsexmale)

|  | Declaration |
| --- | --- |
| From | ``` case Male ``` |
| To | ``` case male ``` |

Modified [HKBiologicalSex.notSet](https://developer.apple.com/documentation/healthkit/hkbiologicalsex/hkbiologicalsexnotset)

|  | Declaration |
| --- | --- |
| From | ``` case NotSet ``` |
| To | ``` case notSet ``` |

Modified [HKBiologicalSex.other](https://developer.apple.com/documentation/healthkit/hkbiologicalsex/other)

|  | Declaration |
| --- | --- |
| From | ``` case Other ``` |
| To | ``` case other ``` |

Modified [HKBiologicalSexObject](https://developer.apple.com/documentation/healthkit/hkbiologicalsexobject)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKBiologicalSexObject : NSObject, NSCopying, NSSecureCoding {     var biologicalSex: HKBiologicalSex { get } } ``` | NSCopying, NSSecureCoding |
| To | ``` class HKBiologicalSexObject : NSObject, NSCopying, NSSecureCoding {     var biologicalSex: HKBiologicalSex { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HKBiologicalSexObject : CVarArg { } extension HKBiologicalSexObject : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [HKBloodType [enum]](https://developer.apple.com/documentation/healthkit/hkbloodtype)

|  | Declaration |
| --- | --- |
| From | ``` enum HKBloodType : Int {     case NotSet     case APositive     case ANegative     case BPositive     case BNegative     case ABPositive     case ABNegative     case OPositive     case ONegative } ``` |
| To | ``` enum HKBloodType : Int {     case notSet     case aPositive     case aNegative     case bPositive     case bNegative     case abPositive     case abNegative     case oPositive     case oNegative } ``` |

Modified [HKBloodType.abNegative](https://developer.apple.com/documentation/healthkit/hkbloodtype/abnegative)

|  | Declaration |
| --- | --- |
| From | ``` case ABNegative ``` |
| To | ``` case abNegative ``` |

Modified [HKBloodType.abPositive](https://developer.apple.com/documentation/healthkit/hkbloodtype/hkbloodtypeabpositive)

|  | Declaration |
| --- | --- |
| From | ``` case ABPositive ``` |
| To | ``` case abPositive ``` |

Modified [HKBloodType.aNegative](https://developer.apple.com/documentation/healthkit/hkbloodtype/anegative)

|  | Declaration |
| --- | --- |
| From | ``` case ANegative ``` |
| To | ``` case aNegative ``` |

Modified [HKBloodType.aPositive](https://developer.apple.com/documentation/healthkit/hkbloodtype/hkbloodtypeapositive)

|  | Declaration |
| --- | --- |
| From | ``` case APositive ``` |
| To | ``` case aPositive ``` |

Modified [HKBloodType.bNegative](https://developer.apple.com/documentation/healthkit/hkbloodtype/bnegative)

|  | Declaration |
| --- | --- |
| From | ``` case BNegative ``` |
| To | ``` case bNegative ``` |

Modified [HKBloodType.bPositive](https://developer.apple.com/documentation/healthkit/hkbloodtype/hkbloodtypebpositive)

|  | Declaration |
| --- | --- |
| From | ``` case BPositive ``` |
| To | ``` case bPositive ``` |

Modified [HKBloodType.notSet](https://developer.apple.com/documentation/healthkit/hkbloodtype/notset)

|  | Declaration |
| --- | --- |
| From | ``` case NotSet ``` |
| To | ``` case notSet ``` |

Modified [HKBloodType.oNegative](https://developer.apple.com/documentation/healthkit/hkbloodtype/onegative)

|  | Declaration |
| --- | --- |
| From | ``` case ONegative ``` |
| To | ``` case oNegative ``` |

Modified [HKBloodType.oPositive](https://developer.apple.com/documentation/healthkit/hkbloodtype/opositive)

|  | Declaration |
| --- | --- |
| From | ``` case OPositive ``` |
| To | ``` case oPositive ``` |

Modified [HKBloodTypeObject](https://developer.apple.com/documentation/healthkit/hkbloodtypeobject)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKBloodTypeObject : NSObject, NSCopying, NSSecureCoding {     var bloodType: HKBloodType { get } } ``` | NSCopying, NSSecureCoding |
| To | ``` class HKBloodTypeObject : NSObject, NSCopying, NSSecureCoding {     var bloodType: HKBloodType { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HKBloodTypeObject : CVarArg { } extension HKBloodTypeObject : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [HKBodyTemperatureSensorLocation [enum]](https://developer.apple.com/documentation/healthkit/hkbodytemperaturesensorlocation)

|  | Declaration |
| --- | --- |
| From | ``` enum HKBodyTemperatureSensorLocation : Int {     case Other     case Armpit     case Body     case Ear     case Finger     case GastroIntestinal     case Mouth     case Rectum     case Toe     case EarDrum     case TemporalArtery     case Forehead } ``` |
| To | ``` enum HKBodyTemperatureSensorLocation : Int {     case other     case armpit     case body     case ear     case finger     case gastroIntestinal     case mouth     case rectum     case toe     case earDrum     case temporalArtery     case forehead } ``` |

Modified [HKBodyTemperatureSensorLocation.armpit](https://developer.apple.com/documentation/healthkit/hkbodytemperaturesensorlocation/armpit)

|  | Declaration |
| --- | --- |
| From | ``` case Armpit ``` |
| To | ``` case armpit ``` |

Modified [HKBodyTemperatureSensorLocation.body](https://developer.apple.com/documentation/healthkit/hkbodytemperaturesensorlocation/body)

|  | Declaration |
| --- | --- |
| From | ``` case Body ``` |
| To | ``` case body ``` |

Modified [HKBodyTemperatureSensorLocation.ear](https://developer.apple.com/documentation/healthkit/hkbodytemperaturesensorlocation/ear)

|  | Declaration |
| --- | --- |
| From | ``` case Ear ``` |
| To | ``` case ear ``` |

Modified [HKBodyTemperatureSensorLocation.earDrum](https://developer.apple.com/documentation/healthkit/hkbodytemperaturesensorlocation/hkbodytemperaturesensorlocationeardrum)

|  | Declaration |
| --- | --- |
| From | ``` case EarDrum ``` |
| To | ``` case earDrum ``` |

Modified [HKBodyTemperatureSensorLocation.finger](https://developer.apple.com/documentation/healthkit/hkbodytemperaturesensorlocation/finger)

|  | Declaration |
| --- | --- |
| From | ``` case Finger ``` |
| To | ``` case finger ``` |

Modified [HKBodyTemperatureSensorLocation.forehead](https://developer.apple.com/documentation/healthkit/hkbodytemperaturesensorlocation/forehead)

|  | Declaration |
| --- | --- |
| From | ``` case Forehead ``` |
| To | ``` case forehead ``` |

Modified [HKBodyTemperatureSensorLocation.gastroIntestinal](https://developer.apple.com/documentation/healthkit/hkbodytemperaturesensorlocation/hkbodytemperaturesensorlocationgastrointestinal)

|  | Declaration |
| --- | --- |
| From | ``` case GastroIntestinal ``` |
| To | ``` case gastroIntestinal ``` |

Modified [HKBodyTemperatureSensorLocation.mouth](https://developer.apple.com/documentation/healthkit/hkbodytemperaturesensorlocation/mouth)

|  | Declaration |
| --- | --- |
| From | ``` case Mouth ``` |
| To | ``` case mouth ``` |

Modified [HKBodyTemperatureSensorLocation.other](https://developer.apple.com/documentation/healthkit/hkbodytemperaturesensorlocation/hkbodytemperaturesensorlocationother)

|  | Declaration |
| --- | --- |
| From | ``` case Other ``` |
| To | ``` case other ``` |

Modified [HKBodyTemperatureSensorLocation.rectum](https://developer.apple.com/documentation/healthkit/hkbodytemperaturesensorlocation/rectum)

|  | Declaration |
| --- | --- |
| From | ``` case Rectum ``` |
| To | ``` case rectum ``` |

Modified [HKBodyTemperatureSensorLocation.temporalArtery](https://developer.apple.com/documentation/healthkit/hkbodytemperaturesensorlocation/temporalartery)

|  | Declaration |
| --- | --- |
| From | ``` case TemporalArtery ``` |
| To | ``` case temporalArtery ``` |

Modified [HKBodyTemperatureSensorLocation.toe](https://developer.apple.com/documentation/healthkit/hkbodytemperaturesensorlocation/toe)

|  | Declaration |
| --- | --- |
| From | ``` case Toe ``` |
| To | ``` case toe ``` |

Modified [HKCategorySample](https://developer.apple.com/documentation/healthkit/hkcategorysample)

|  | Declaration |
| --- | --- |
| From | ``` class HKCategorySample : HKSample {     var categoryType: HKCategoryType { get }     var value: Int { get }     init()     convenience init(type type: HKCategoryType, value value: Int, startDate startDate: NSDate, endDate endDate: NSDate, metadata metadata: [String : AnyObject]?)     class func categorySampleWithType(_ type: HKCategoryType, value value: Int, startDate startDate: NSDate, endDate endDate: NSDate, metadata metadata: [String : AnyObject]?) -> Self     convenience init(type type: HKCategoryType, value value: Int, startDate startDate: NSDate, endDate endDate: NSDate)     class func categorySampleWithType(_ type: HKCategoryType, value value: Int, startDate startDate: NSDate, endDate endDate: NSDate) -> Self     convenience init(type type: HKCategoryType, value value: Int, startDate startDate: NSDate, endDate endDate: NSDate, device device: HKDevice?, metadata metadata: [String : AnyObject]?)     class func categorySampleWithType(_ type: HKCategoryType, value value: Int, startDate startDate: NSDate, endDate endDate: NSDate, device device: HKDevice?, metadata metadata: [String : AnyObject]?) -> Self } ``` |
| To | ``` class HKCategorySample : HKSample {     var categoryType: HKCategoryType { get }     var value: Int { get }     init()     convenience init(type type: HKCategoryType, value value: Int, start startDate: Date, end endDate: Date, metadata metadata: [String : Any]?)     class func withType(_ type: HKCategoryType, value value: Int, start startDate: Date, end endDate: Date, metadata metadata: [String : Any]?) -> Self     convenience init(type type: HKCategoryType, value value: Int, start startDate: Date, end endDate: Date)     class func withType(_ type: HKCategoryType, value value: Int, start startDate: Date, end endDate: Date) -> Self     convenience init(type type: HKCategoryType, value value: Int, start startDate: Date, end endDate: Date, device device: HKDevice?, metadata metadata: [String : Any]?)     class func withType(_ type: HKCategoryType, value value: Int, start startDate: Date, end endDate: Date, device device: HKDevice?, metadata metadata: [String : Any]?) -> Self } ``` |

Modified [HKCategorySample.init(type: HKCategoryType, value: Int, start: Date, end: Date)](https://developer.apple.com/documentation/healthkit/hkcategorysample/1615063-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(type type: HKCategoryType, value value: Int, startDate startDate: NSDate, endDate endDate: NSDate) ``` |
| To | ``` convenience init(type type: HKCategoryType, value value: Int, start startDate: Date, end endDate: Date) ``` |

Modified [HKCategorySample.init(type: HKCategoryType, value: Int, start: Date, end: Date, device: HKDevice?, metadata: [String : Any]?)](https://developer.apple.com/documentation/healthkit/hkcategorysample/1615287-categorysamplewithtype)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(type type: HKCategoryType, value value: Int, startDate startDate: NSDate, endDate endDate: NSDate, device device: HKDevice?, metadata metadata: [String : AnyObject]?) ``` |
| To | ``` convenience init(type type: HKCategoryType, value value: Int, start startDate: Date, end endDate: Date, device device: HKDevice?, metadata metadata: [String : Any]?) ``` |

Modified [HKCategorySample.init(type: HKCategoryType, value: Int, start: Date, end: Date, metadata: [String : Any]?)](https://developer.apple.com/documentation/healthkit/hkcategorysample/1615596-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(type type: HKCategoryType, value value: Int, startDate startDate: NSDate, endDate endDate: NSDate, metadata metadata: [String : AnyObject]?) ``` |
| To | ``` convenience init(type type: HKCategoryType, value value: Int, start startDate: Date, end endDate: Date, metadata metadata: [String : Any]?) ``` |

Modified [HKCategoryTypeIdentifier.appleStandHour](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifierapplestandhour)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKCategoryTypeIdentifierAppleStandHour | ``` let HKCategoryTypeIdentifierAppleStandHour: String ``` |
| To | appleStandHour | ``` static let appleStandHour: HKCategoryTypeIdentifier ``` |

Modified [HKCategoryTypeIdentifier.cervicalMucusQuality](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/1615429-cervicalmucusquality)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKCategoryTypeIdentifierCervicalMucusQuality | ``` let HKCategoryTypeIdentifierCervicalMucusQuality: String ``` |
| To | cervicalMucusQuality | ``` static let cervicalMucusQuality: HKCategoryTypeIdentifier ``` |

Modified [HKCategoryTypeIdentifier.intermenstrualBleeding](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifierintermenstrualbleeding)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKCategoryTypeIdentifierIntermenstrualBleeding | ``` let HKCategoryTypeIdentifierIntermenstrualBleeding: String ``` |
| To | intermenstrualBleeding | ``` static let intermenstrualBleeding: HKCategoryTypeIdentifier ``` |

Modified [HKCategoryTypeIdentifier.menstrualFlow](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/1615136-menstrualflow)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKCategoryTypeIdentifierMenstrualFlow | ``` let HKCategoryTypeIdentifierMenstrualFlow: String ``` |
| To | menstrualFlow | ``` static let menstrualFlow: HKCategoryTypeIdentifier ``` |

Modified [HKCategoryTypeIdentifier.ovulationTestResult](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/1615252-ovulationtestresult)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKCategoryTypeIdentifierOvulationTestResult | ``` let HKCategoryTypeIdentifierOvulationTestResult: String ``` |
| To | ovulationTestResult | ``` static let ovulationTestResult: HKCategoryTypeIdentifier ``` |

Modified [HKCategoryTypeIdentifier.sexualActivity](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/1615769-sexualactivity)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKCategoryTypeIdentifierSexualActivity | ``` let HKCategoryTypeIdentifierSexualActivity: String ``` |
| To | sexualActivity | ``` static let sexualActivity: HKCategoryTypeIdentifier ``` |

Modified [HKCategoryTypeIdentifier.sleepAnalysis](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/1615425-sleepanalysis)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKCategoryTypeIdentifierSleepAnalysis | ``` let HKCategoryTypeIdentifierSleepAnalysis: String ``` |
| To | sleepAnalysis | ``` static let sleepAnalysis: HKCategoryTypeIdentifier ``` |

Modified [HKCategoryValue [enum]](https://developer.apple.com/documentation/healthkit/hkcategoryvalue)

|  | Declaration |
| --- | --- |
| From | ``` enum HKCategoryValue : Int {     case NotApplicable } ``` |
| To | ``` enum HKCategoryValue : Int {     case notApplicable } ``` |

Modified [HKCategoryValue.notApplicable](https://developer.apple.com/documentation/healthkit/hkcategoryvalue/hkcategoryvaluenotapplicable)

|  | Declaration |
| --- | --- |
| From | ``` case NotApplicable ``` |
| To | ``` case notApplicable ``` |

Modified [HKCategoryValueAppleStandHour [enum]](https://developer.apple.com/documentation/healthkit/hkcategoryvalueapplestandhour)

|  | Declaration |
| --- | --- |
| From | ``` enum HKCategoryValueAppleStandHour : Int {     case Stood     case Idle } ``` |
| To | ``` enum HKCategoryValueAppleStandHour : Int {     case stood     case idle } ``` |

Modified [HKCategoryValueAppleStandHour.idle](https://developer.apple.com/documentation/healthkit/hkcategoryvalueapplestandhour/idle)

|  | Declaration |
| --- | --- |
| From | ``` case Idle ``` |
| To | ``` case idle ``` |

Modified [HKCategoryValueAppleStandHour.stood](https://developer.apple.com/documentation/healthkit/hkcategoryvalueapplestandhour/hkcategoryvalueapplestandhourstood)

|  | Declaration |
| --- | --- |
| From | ``` case Stood ``` |
| To | ``` case stood ``` |

Modified [HKCategoryValueCervicalMucusQuality [enum]](https://developer.apple.com/documentation/healthkit/hkcategoryvaluecervicalmucusquality)

|  | Declaration |
| --- | --- |
| From | ``` enum HKCategoryValueCervicalMucusQuality : Int {     case Dry     case Sticky     case Creamy     case Watery     case EggWhite } ``` |
| To | ``` enum HKCategoryValueCervicalMucusQuality : Int {     case dry     case sticky     case creamy     case watery     case eggWhite } ``` |

Modified [HKCategoryValueCervicalMucusQuality.creamy](https://developer.apple.com/documentation/healthkit/hkcategoryvaluecervicalmucusquality/creamy)

|  | Declaration |
| --- | --- |
| From | ``` case Creamy ``` |
| To | ``` case creamy ``` |

Modified [HKCategoryValueCervicalMucusQuality.dry](https://developer.apple.com/documentation/healthkit/hkcategoryvaluecervicalmucusquality/dry)

|  | Declaration |
| --- | --- |
| From | ``` case Dry ``` |
| To | ``` case dry ``` |

Modified [HKCategoryValueCervicalMucusQuality.eggWhite](https://developer.apple.com/documentation/healthkit/hkcategoryvaluecervicalmucusquality/hkcategoryvaluecervicalmucusqualityeggwhite)

|  | Declaration |
| --- | --- |
| From | ``` case EggWhite ``` |
| To | ``` case eggWhite ``` |

Modified [HKCategoryValueCervicalMucusQuality.sticky](https://developer.apple.com/documentation/healthkit/hkcategoryvaluecervicalmucusquality/hkcategoryvaluecervicalmucusqualitysticky)

|  | Declaration |
| --- | --- |
| From | ``` case Sticky ``` |
| To | ``` case sticky ``` |

Modified [HKCategoryValueCervicalMucusQuality.watery](https://developer.apple.com/documentation/healthkit/hkcategoryvaluecervicalmucusquality/watery)

|  | Declaration |
| --- | --- |
| From | ``` case Watery ``` |
| To | ``` case watery ``` |

Modified [HKCategoryValueMenstrualFlow [enum]](https://developer.apple.com/documentation/healthkit/hkcategoryvaluemenstrualflow)

|  | Declaration |
| --- | --- |
| From | ``` enum HKCategoryValueMenstrualFlow : Int {     case Unspecified     case Light     case Medium     case Heavy } ``` |
| To | ``` enum HKCategoryValueMenstrualFlow : Int {     case unspecified     case light     case medium     case heavy } ``` |

Modified [HKCategoryValueMenstrualFlow.heavy](https://developer.apple.com/documentation/healthkit/hkcategoryvaluemenstrualflow/heavy)

|  | Declaration |
| --- | --- |
| From | ``` case Heavy ``` |
| To | ``` case heavy ``` |

Modified [HKCategoryValueMenstrualFlow.light](https://developer.apple.com/documentation/healthkit/hkcategoryvaluemenstrualflow/hkcategoryvaluemenstrualflowlight)

|  | Declaration |
| --- | --- |
| From | ``` case Light ``` |
| To | ``` case light ``` |

Modified [HKCategoryValueMenstrualFlow.medium](https://developer.apple.com/documentation/healthkit/hkcategoryvaluemenstrualflow/hkcategoryvaluemenstrualflowmedium)

|  | Declaration |
| --- | --- |
| From | ``` case Medium ``` |
| To | ``` case medium ``` |

Modified [HKCategoryValueMenstrualFlow.unspecified](https://developer.apple.com/documentation/healthkit/hkcategoryvaluemenstrualflow/unspecified)

|  | Declaration |
| --- | --- |
| From | ``` case Unspecified ``` |
| To | ``` case unspecified ``` |

Modified [HKCategoryValueOvulationTestResult [enum]](https://developer.apple.com/documentation/healthkit/hkcategoryvalueovulationtestresult)

|  | Declaration |
| --- | --- |
| From | ``` enum HKCategoryValueOvulationTestResult : Int {     case Negative     case Positive     case Indeterminate } ``` |
| To | ``` enum HKCategoryValueOvulationTestResult : Int {     case negative     case positive     case indeterminate } ``` |

Modified [HKCategoryValueOvulationTestResult.indeterminate](https://developer.apple.com/documentation/healthkit/hkcategoryvalueovulationtestresult/hkcategoryvalueovulationtestresultindeterminate)

|  | Declaration |
| --- | --- |
| From | ``` case Indeterminate ``` |
| To | ``` case indeterminate ``` |

Modified [HKCategoryValueOvulationTestResult.negative](https://developer.apple.com/documentation/healthkit/hkcategoryvalueovulationtestresult/negative)

|  | Declaration |
| --- | --- |
| From | ``` case Negative ``` |
| To | ``` case negative ``` |

Modified [HKCategoryValueOvulationTestResult.positive](https://developer.apple.com/documentation/healthkit/hkcategoryvalueovulationtestresult/hkcategoryvalueovulationtestresultpositive)

|  | Declaration |
| --- | --- |
| From | ``` case Positive ``` |
| To | ``` case positive ``` |

Modified [HKCategoryValueSleepAnalysis [enum]](https://developer.apple.com/documentation/healthkit/hkcategoryvaluesleepanalysis)

|  | Declaration |
| --- | --- |
| From | ``` enum HKCategoryValueSleepAnalysis : Int {     case InBed     case Asleep } ``` |
| To | ``` enum HKCategoryValueSleepAnalysis : Int {     case inBed     case asleep     case awake } ``` |

Modified [HKCategoryValueSleepAnalysis.asleep](https://developer.apple.com/documentation/healthkit/hkcategoryvaluesleepanalysis/asleep)

|  | Declaration |
| --- | --- |
| From | ``` case Asleep ``` |
| To | ``` case asleep ``` |

Modified [HKCategoryValueSleepAnalysis.inBed](https://developer.apple.com/documentation/healthkit/hkcategoryvaluesleepanalysis/inbed)

|  | Declaration |
| --- | --- |
| From | ``` case InBed ``` |
| To | ``` case inBed ``` |

Modified [HKCharacteristicTypeIdentifier.biologicalSex](https://developer.apple.com/documentation/healthkit/hkcharacteristictypeidentifierbiologicalsex)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKCharacteristicTypeIdentifierBiologicalSex | ``` let HKCharacteristicTypeIdentifierBiologicalSex: String ``` |
| To | biologicalSex | ``` static let biologicalSex: HKCharacteristicTypeIdentifier ``` |

Modified [HKCharacteristicTypeIdentifier.bloodType](https://developer.apple.com/documentation/healthkit/hkcharacteristictypeidentifierbloodtype)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKCharacteristicTypeIdentifierBloodType | ``` let HKCharacteristicTypeIdentifierBloodType: String ``` |
| To | bloodType | ``` static let bloodType: HKCharacteristicTypeIdentifier ``` |

Modified [HKCharacteristicTypeIdentifier.dateOfBirth](https://developer.apple.com/documentation/healthkit/hkcharacteristictypeidentifierdateofbirth)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKCharacteristicTypeIdentifierDateOfBirth | ``` let HKCharacteristicTypeIdentifierDateOfBirth: String ``` |
| To | dateOfBirth | ``` static let dateOfBirth: HKCharacteristicTypeIdentifier ``` |

Modified [HKCharacteristicTypeIdentifier.fitzpatrickSkinType](https://developer.apple.com/documentation/healthkit/hkcharacteristictypeidentifier/1615075-fitzpatrickskintype)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKCharacteristicTypeIdentifierFitzpatrickSkinType | ``` let HKCharacteristicTypeIdentifierFitzpatrickSkinType: String ``` |
| To | fitzpatrickSkinType | ``` static let fitzpatrickSkinType: HKCharacteristicTypeIdentifier ``` |

Modified [HKCorrelation](https://developer.apple.com/documentation/healthkit/hkcorrelation)

|  | Declaration |
| --- | --- |
| From | ``` class HKCorrelation : HKSample {     var correlationType: HKCorrelationType { get }     var objects: Set<HKSample> { get }     convenience init(type correlationType: HKCorrelationType, startDate startDate: NSDate, endDate endDate: NSDate, objects objects: Set<HKSample>)     class func correlationWithType(_ correlationType: HKCorrelationType, startDate startDate: NSDate, endDate endDate: NSDate, objects objects: Set<HKSample>) -> Self     convenience init(type correlationType: HKCorrelationType, startDate startDate: NSDate, endDate endDate: NSDate, objects objects: Set<HKSample>, metadata metadata: [String : AnyObject]?)     class func correlationWithType(_ correlationType: HKCorrelationType, startDate startDate: NSDate, endDate endDate: NSDate, objects objects: Set<HKSample>, metadata metadata: [String : AnyObject]?) -> Self     convenience init(type correlationType: HKCorrelationType, startDate startDate: NSDate, endDate endDate: NSDate, objects objects: Set<HKSample>, device device: HKDevice?, metadata metadata: [String : AnyObject]?)     class func correlationWithType(_ correlationType: HKCorrelationType, startDate startDate: NSDate, endDate endDate: NSDate, objects objects: Set<HKSample>, device device: HKDevice?, metadata metadata: [String : AnyObject]?) -> Self     func objectsForType(_ objectType: HKObjectType) -> Set<HKSample> } ``` |
| To | ``` class HKCorrelation : HKSample {     var correlationType: HKCorrelationType { get }     var objects: Set<HKSample> { get }     convenience init(type correlationType: HKCorrelationType, start startDate: Date, end endDate: Date, objects objects: Set<HKSample>)     class func withType(_ correlationType: HKCorrelationType, start startDate: Date, end endDate: Date, objects objects: Set<HKSample>) -> Self     convenience init(type correlationType: HKCorrelationType, start startDate: Date, end endDate: Date, objects objects: Set<HKSample>, metadata metadata: [String : Any]?)     class func withType(_ correlationType: HKCorrelationType, start startDate: Date, end endDate: Date, objects objects: Set<HKSample>, metadata metadata: [String : Any]?) -> Self     convenience init(type correlationType: HKCorrelationType, start startDate: Date, end endDate: Date, objects objects: Set<HKSample>, device device: HKDevice?, metadata metadata: [String : Any]?)     class func withType(_ correlationType: HKCorrelationType, start startDate: Date, end endDate: Date, objects objects: Set<HKSample>, device device: HKDevice?, metadata metadata: [String : Any]?) -> Self     func objects(for objectType: HKObjectType) -> Set<HKSample> } ``` |

Modified [HKCorrelation.init(type: HKCorrelationType, start: Date, end: Date, objects: Set<HKSample>)](https://developer.apple.com/documentation/healthkit/hkcorrelation/1614359-correlationwithtype)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(type correlationType: HKCorrelationType, startDate startDate: NSDate, endDate endDate: NSDate, objects objects: Set<HKSample>) ``` |
| To | ``` convenience init(type correlationType: HKCorrelationType, start startDate: Date, end endDate: Date, objects objects: Set<HKSample>) ``` |

Modified [HKCorrelation.init(type: HKCorrelationType, start: Date, end: Date, objects: Set<HKSample>, device: HKDevice?, metadata: [String : Any]?)](https://developer.apple.com/documentation/healthkit/hkcorrelation/1614363-correlationwithtype)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(type correlationType: HKCorrelationType, startDate startDate: NSDate, endDate endDate: NSDate, objects objects: Set<HKSample>, device device: HKDevice?, metadata metadata: [String : AnyObject]?) ``` |
| To | ``` convenience init(type correlationType: HKCorrelationType, start startDate: Date, end endDate: Date, objects objects: Set<HKSample>, device device: HKDevice?, metadata metadata: [String : Any]?) ``` |

Modified [HKCorrelation.init(type: HKCorrelationType, start: Date, end: Date, objects: Set<HKSample>, metadata: [String : Any]?)](https://developer.apple.com/documentation/healthkit/hkcorrelation/1614362-correlationwithtype)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(type correlationType: HKCorrelationType, startDate startDate: NSDate, endDate endDate: NSDate, objects objects: Set<HKSample>, metadata metadata: [String : AnyObject]?) ``` |
| To | ``` convenience init(type correlationType: HKCorrelationType, start startDate: Date, end endDate: Date, objects objects: Set<HKSample>, metadata metadata: [String : Any]?) ``` |

Modified [HKCorrelation.objects(for: HKObjectType) -> Set<HKSample>](https://developer.apple.com/documentation/healthkit/hkcorrelation/1614360-objects)

|  | Declaration |
| --- | --- |
| From | ``` func objectsForType(_ objectType: HKObjectType) -> Set<HKSample> ``` |
| To | ``` func objects(for objectType: HKObjectType) -> Set<HKSample> ``` |

Modified [HKCorrelationQuery](https://developer.apple.com/documentation/healthkit/hkcorrelationquery)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKCorrelationQuery : HKQuery {     @NSCopying var correlationType: HKCorrelationType { get }     var samplePredicates: [HKSampleType : NSPredicate]? { get }     init(type correlationType: HKCorrelationType, predicate predicate: NSPredicate?, samplePredicates samplePredicates: [HKSampleType : NSPredicate]?, completion completion: (HKCorrelationQuery, [HKCorrelation]?, NSError?) -> Void) } ``` | -- |
| To | ``` class HKCorrelationQuery : HKQuery {     @NSCopying var correlationType: HKCorrelationType { get }     var samplePredicates: [HKSampleType : NSPredicate]? { get }     init(type correlationType: HKCorrelationType, predicate predicate: NSPredicate?, samplePredicates samplePredicates: [HKSampleType : NSPredicate]?, completion completion: @escaping (HKCorrelationQuery, [HKCorrelation]?, Error?) -> Swift.Void)     class func predicateForActivitySummary(with dateComponents: DateComponents) -> NSPredicate     class func predicate(forActivitySummariesBetweenStart startDateComponents: DateComponents, end endDateComponents: DateComponents) -> NSPredicate     class func predicateForWorkouts(with workoutActivityType: HKWorkoutActivityType) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, duration duration: TimeInterval) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalEnergyBurned totalEnergyBurned: HKQuantity) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalDistance totalDistance: HKQuantity) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalSwimmingStrokeCount totalSwimmingStrokeCount: HKQuantity) -> NSPredicate     class func predicateForCategorySamples(with operatorType: NSComparisonPredicate.Operator, value value: Int) -> NSPredicate     class func predicateForQuantitySamples(with operatorType: NSComparisonPredicate.Operator, quantity quantity: HKQuantity) -> NSPredicate     class func predicateForSamples(withStart startDate: Date?, end endDate: Date?, options options: HKQueryOptions = []) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String, allowedValues allowedValues: [Any]) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String, operatorType operatorType: NSComparisonPredicate.Operator, value value: Any) -> NSPredicate     class func predicateForObjects(from source: HKSource) -> NSPredicate     class func predicateForObjects(from sources: Set<HKSource>) -> NSPredicate     class func predicateForObjects(from sourceRevisions: Set<HKSourceRevision>) -> NSPredicate     class func predicateForObjects(from devices: Set<HKDevice>) -> NSPredicate     class func predicateForObjects(withDeviceProperty key: String, allowedValues allowedValues: Set<String>) -> NSPredicate     class func predicateForObject(with UUID: UUID) -> NSPredicate     class func predicateForObjects(with UUIDs: Set<UUID>) -> NSPredicate     class func predicateForObjectsWithNoCorrelation() -> NSPredicate     class func predicateForObjects(from workout: HKWorkout) -> NSPredicate     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HKCorrelationQuery : CVarArg { } extension HKCorrelationQuery : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [HKCorrelationQuery.init(type: HKCorrelationType, predicate: NSPredicate?, samplePredicates: [HKSampleType : NSPredicate]?, completion: (HKCorrelationQuery, [HKCorrelation]?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/healthkit/hkcorrelationquery/1614145-initwithtype)

|  | Declaration |
| --- | --- |
| From | ``` init(type correlationType: HKCorrelationType, predicate predicate: NSPredicate?, samplePredicates samplePredicates: [HKSampleType : NSPredicate]?, completion completion: (HKCorrelationQuery, [HKCorrelation]?, NSError?) -> Void) ``` |
| To | ``` init(type correlationType: HKCorrelationType, predicate predicate: NSPredicate?, samplePredicates samplePredicates: [HKSampleType : NSPredicate]?, completion completion: @escaping (HKCorrelationQuery, [HKCorrelation]?, Error?) -> Swift.Void) ``` |

Modified [HKCorrelationTypeIdentifier.bloodPressure](https://developer.apple.com/documentation/healthkit/hkcorrelationtypeidentifierbloodpressure)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKCorrelationTypeIdentifierBloodPressure | ``` let HKCorrelationTypeIdentifierBloodPressure: String ``` |
| To | bloodPressure | ``` static let bloodPressure: HKCorrelationTypeIdentifier ``` |

Modified [HKCorrelationTypeIdentifier.food](https://developer.apple.com/documentation/healthkit/hkcorrelationtypeidentifierfood)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKCorrelationTypeIdentifierFood | ``` let HKCorrelationTypeIdentifierFood: String ``` |
| To | food | ``` static let food: HKCorrelationTypeIdentifier ``` |

Modified [HKDeletedObject](https://developer.apple.com/documentation/healthkit/hkdeletedobject)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKDeletedObject : NSObject, NSSecureCoding {     var UUID: NSUUID { get }     init() } ``` | NSSecureCoding |
| To | ``` class HKDeletedObject : NSObject, NSSecureCoding {     var uuid: UUID { get }     init()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HKDeletedObject : CVarArg { } extension HKDeletedObject : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSSecureCoding |

Modified [HKDeletedObject.uuid](https://developer.apple.com/documentation/healthkit/hkdeletedobject/1615423-uuid)

|  | Declaration |
| --- | --- |
| From | ``` var UUID: NSUUID { get } ``` |
| To | ``` var uuid: UUID { get } ``` |

Modified [HKDevice](https://developer.apple.com/documentation/healthkit/hkdevice)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKDevice : NSObject, NSSecureCoding, NSCopying {     var name: String { get }     var manufacturer: String? { get }     var model: String? { get }     var hardwareVersion: String? { get }     var firmwareVersion: String? { get }     var softwareVersion: String? { get }     var localIdentifier: String? { get }     var UDIDeviceIdentifier: String? { get }     init(name name: String?, manufacturer manufacturer: String?, model model: String?, hardwareVersion hardwareVersion: String?, firmwareVersion firmwareVersion: String?, softwareVersion softwareVersion: String?, localIdentifier localIdentifier: String?, UDIDeviceIdentifier UDIDeviceIdentifier: String?)     init()     class func localDevice() -> HKDevice } ``` | NSCopying, NSSecureCoding |
| To | ``` class HKDevice : NSObject, NSSecureCoding, NSCopying {     var name: String? { get }     var manufacturer: String? { get }     var model: String? { get }     var hardwareVersion: String? { get }     var firmwareVersion: String? { get }     var softwareVersion: String? { get }     var localIdentifier: String? { get }     var udiDeviceIdentifier: String? { get }     init(name name: String?, manufacturer manufacturer: String?, model model: String?, hardwareVersion hardwareVersion: String?, firmwareVersion firmwareVersion: String?, softwareVersion softwareVersion: String?, localIdentifier localIdentifier: String?, udiDeviceIdentifier UDIDeviceIdentifier: String?)     init()     class func local() -> HKDevice     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HKDevice : CVarArg { } extension HKDevice : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [HKDevice.init(name: String?, manufacturer: String?, model: String?, hardwareVersion: String?, firmwareVersion: String?, softwareVersion: String?, localIdentifier: String?, udiDeviceIdentifier: String?)](https://developer.apple.com/documentation/healthkit/hkdevice/1615582-initwithname)

|  | Declaration |
| --- | --- |
| From | ``` init(name name: String?, manufacturer manufacturer: String?, model model: String?, hardwareVersion hardwareVersion: String?, firmwareVersion firmwareVersion: String?, softwareVersion softwareVersion: String?, localIdentifier localIdentifier: String?, UDIDeviceIdentifier UDIDeviceIdentifier: String?) ``` |
| To | ``` init(name name: String?, manufacturer manufacturer: String?, model model: String?, hardwareVersion hardwareVersion: String?, firmwareVersion firmwareVersion: String?, softwareVersion softwareVersion: String?, localIdentifier localIdentifier: String?, udiDeviceIdentifier UDIDeviceIdentifier: String?) ``` |

Modified [HKDevice.local() -> HKDevice [class]](https://developer.apple.com/documentation/healthkit/hkdevice/1615276-local)

|  | Declaration |
| --- | --- |
| From | ``` class func localDevice() -> HKDevice ``` |
| To | ``` class func local() -> HKDevice ``` |

Modified [HKDevice.name](https://developer.apple.com/documentation/healthkit/hkdevice/1615731-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String { get } ``` |
| To | ``` var name: String? { get } ``` |

Modified [HKDevice.udiDeviceIdentifier](https://developer.apple.com/documentation/healthkit/hkdevice/1615296-udideviceidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var UDIDeviceIdentifier: String? { get } ``` |
| To | ``` var udiDeviceIdentifier: String? { get } ``` |

Modified [HKError.Code [enum]](https://developer.apple.com/documentation/healthkit/hkerrorcode)

|  | Declaration |
| --- | --- |
| From | ``` enum HKErrorCode : Int {     case NoError     case ErrorHealthDataUnavailable     case ErrorHealthDataRestricted     case ErrorInvalidArgument     case ErrorAuthorizationDenied     case ErrorAuthorizationNotDetermined     case ErrorDatabaseInaccessible     case ErrorUserCanceled     case ErrorAnotherWorkoutSessionStarted     case ErrorUserExitedWorkoutSession } ``` |
| To | ``` enum Code : Int {         typealias _ErrorType = HKError         case noError         case errorHealthDataUnavailable         case errorHealthDataRestricted         case errorInvalidArgument         case errorAuthorizationDenied         case errorAuthorizationNotDetermined         case errorDatabaseInaccessible         case errorUserCanceled         case errorAnotherWorkoutSessionStarted         case errorUserExitedWorkoutSession     } ``` |

Modified [HKError.Code.errorAnotherWorkoutSessionStarted](https://developer.apple.com/documentation/healthkit/hkerrorcode/hkerroranotherworkoutsessionstarted)

|  | Declaration |
| --- | --- |
| From | ``` case ErrorAnotherWorkoutSessionStarted ``` |
| To | ``` case errorAnotherWorkoutSessionStarted ``` |

Modified [HKError.Code.errorAuthorizationDenied](https://developer.apple.com/documentation/healthkit/hkerrorcode/hkerrorauthorizationdenied)

|  | Declaration |
| --- | --- |
| From | ``` case ErrorAuthorizationDenied ``` |
| To | ``` case errorAuthorizationDenied ``` |

Modified [HKError.Code.errorAuthorizationNotDetermined](https://developer.apple.com/documentation/healthkit/hkerror/code/errorauthorizationnotdetermined)

|  | Declaration |
| --- | --- |
| From | ``` case ErrorAuthorizationNotDetermined ``` |
| To | ``` case errorAuthorizationNotDetermined ``` |

Modified [HKError.Code.errorDatabaseInaccessible](https://developer.apple.com/documentation/healthkit/hkerror/code/errordatabaseinaccessible)

|  | Declaration |
| --- | --- |
| From | ``` case ErrorDatabaseInaccessible ``` |
| To | ``` case errorDatabaseInaccessible ``` |

Modified [HKError.Code.errorHealthDataRestricted](https://developer.apple.com/documentation/healthkit/hkerrorcode/hkerrorhealthdatarestricted)

|  | Declaration |
| --- | --- |
| From | ``` case ErrorHealthDataRestricted ``` |
| To | ``` case errorHealthDataRestricted ``` |

Modified [HKError.Code.errorHealthDataUnavailable](https://developer.apple.com/documentation/healthkit/hkerror/code/errorhealthdataunavailable)

|  | Declaration |
| --- | --- |
| From | ``` case ErrorHealthDataUnavailable ``` |
| To | ``` case errorHealthDataUnavailable ``` |

Modified [HKError.Code.errorInvalidArgument](https://developer.apple.com/documentation/healthkit/hkerror/code/errorinvalidargument)

|  | Declaration |
| --- | --- |
| From | ``` case ErrorInvalidArgument ``` |
| To | ``` case errorInvalidArgument ``` |

Modified [HKError.Code.errorUserCanceled](https://developer.apple.com/documentation/healthkit/hkerrorcode/hkerrorusercanceled)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case ErrorUserCanceled ``` | iOS 8.0 |
| To | ``` case errorUserCanceled ``` | iOS 10.0 |

Modified [HKError.Code.errorUserExitedWorkoutSession](https://developer.apple.com/documentation/healthkit/hkerrorcode/hkerroruserexitedworkoutsession)

|  | Declaration |
| --- | --- |
| From | ``` case ErrorUserExitedWorkoutSession ``` |
| To | ``` case errorUserExitedWorkoutSession ``` |

Modified [HKError.Code.noError](https://developer.apple.com/documentation/healthkit/hkerror/code/noerror)

|  | Declaration |
| --- | --- |
| From | ``` case NoError ``` |
| To | ``` case noError ``` |

Modified [HKFitzpatrickSkinType [enum]](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintype)

|  | Declaration |
| --- | --- |
| From | ``` enum HKFitzpatrickSkinType : Int {     case NotSet     case I     case II     case III     case IV     case V     case VI } ``` |
| To | ``` enum HKFitzpatrickSkinType : Int {     case notSet     case I     case II     case III     case IV     case V     case VI } ``` |

Modified [HKFitzpatrickSkinType.notSet](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintype/hkfitzpatrickskintypenotset)

|  | Declaration |
| --- | --- |
| From | ``` case NotSet ``` |
| To | ``` case notSet ``` |

Modified [HKFitzpatrickSkinTypeObject](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintypeobject)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKFitzpatrickSkinTypeObject : NSObject, NSCopying, NSSecureCoding {     var skinType: HKFitzpatrickSkinType { get } } ``` | NSCopying, NSSecureCoding |
| To | ``` class HKFitzpatrickSkinTypeObject : NSObject, NSCopying, NSSecureCoding {     var skinType: HKFitzpatrickSkinType { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HKFitzpatrickSkinTypeObject : CVarArg { } extension HKFitzpatrickSkinTypeObject : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [HKHealthStore](https://developer.apple.com/documentation/healthkit/hkhealthstore)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKHealthStore : NSObject {     class func isHealthDataAvailable() -> Bool     func authorizationStatusForType(_ type: HKObjectType) -> HKAuthorizationStatus     func requestAuthorizationToShareTypes(_ typesToShare: Set<HKSampleType>?, readTypes typesToRead: Set<HKObjectType>?, completion completion: (Bool, NSError?) -> Void)     func handleAuthorizationForExtensionWithCompletion(_ completion: (Bool, NSError?) -> Void)     func earliestPermittedSampleDate() -> NSDate     func saveObject(_ object: HKObject, withCompletion completion: (Bool, NSError?) -> Void)     func saveObjects(_ objects: [HKObject], withCompletion completion: (Bool, NSError?) -> Void)     func deleteObject(_ object: HKObject, withCompletion completion: (Bool, NSError?) -> Void)     func deleteObjects(_ objects: [HKObject], withCompletion completion: (Bool, NSError?) -> Void)     func deleteObjectsOfType(_ objectType: HKObjectType, predicate predicate: NSPredicate, withCompletion completion: (Bool, Int, NSError?) -> Void)     func executeQuery(_ query: HKQuery)     func stopQuery(_ query: HKQuery)     func splitTotalEnergy(_ totalEnergy: HKQuantity, startDate startDate: NSDate, endDate endDate: NSDate, resultsHandler resultsHandler: (HKQuantity?, HKQuantity?, NSError?) -> Void)     func dateOfBirth() throws -> NSDate     func biologicalSex() throws -> HKBiologicalSexObject     func bloodType() throws -> HKBloodTypeObject     func fitzpatrickSkinType() throws -> HKFitzpatrickSkinTypeObject } extension HKHealthStore {     func addSamples(_ samples: [HKSample], toWorkout workout: HKWorkout, completion completion: (Bool, NSError?) -> Void)     func startWorkoutSession(_ workoutSession: HKWorkoutSession)     func endWorkoutSession(_ workoutSession: HKWorkoutSession) } extension HKHealthStore {     func enableBackgroundDeliveryForType(_ type: HKObjectType, frequency frequency: HKUpdateFrequency, withCompletion completion: (Bool, NSError?) -> Void)     func disableBackgroundDeliveryForType(_ type: HKObjectType, withCompletion completion: (Bool, NSError?) -> Void)     func disableAllBackgroundDeliveryWithCompletion(_ completion: (Bool, NSError?) -> Void) } extension HKHealthStore {     func preferredUnitsForQuantityTypes(_ quantityTypes: Set<HKQuantityType>, completion completion: ([HKQuantityType : HKUnit], NSError?) -> Void) } ``` | -- |
| To | ``` class HKHealthStore : NSObject {     class func isHealthDataAvailable() -> Bool     func authorizationStatus(for type: HKObjectType) -> HKAuthorizationStatus     func requestAuthorization(toShare typesToShare: Set<HKSampleType>?, read typesToRead: Set<HKObjectType>?, completion completion: @escaping (Bool, Error?) -> Swift.Void)     func handleAuthorizationForExtension(completion completion: @escaping (Bool, Error?) -> Swift.Void)     func earliestPermittedSampleDate() -> Date     func save(_ object: HKObject, withCompletion completion: @escaping (Bool, Error?) -> Swift.Void)     func save(_ objects: [HKObject], withCompletion completion: @escaping (Bool, Error?) -> Swift.Void)     func delete(_ object: HKObject, withCompletion completion: @escaping (Bool, Error?) -> Swift.Void)     func delete(_ objects: [HKObject], withCompletion completion: @escaping (Bool, Error?) -> Swift.Void)     func deleteObjects(of objectType: HKObjectType, predicate predicate: NSPredicate, withCompletion completion: @escaping (Bool, Int, Error?) -> Swift.Void)     func execute(_ query: HKQuery)     func stop(_ query: HKQuery)     func splitTotalEnergy(_ totalEnergy: HKQuantity, start startDate: Date, end endDate: Date, resultsHandler resultsHandler: @escaping (HKQuantity?, HKQuantity?, Error?) -> Swift.Void)     func dateOfBirth() throws -> Date     func dateOfBirthComponents() throws -> DateComponents     func biologicalSex() throws -> HKBiologicalSexObject     func bloodType() throws -> HKBloodTypeObject     func fitzpatrickSkinType() throws -> HKFitzpatrickSkinTypeObject     func wheelchairUse() throws -> HKWheelchairUseObject     func preferredUnits(for quantityTypes: Set<HKQuantityType>, completion completion: @escaping ([HKQuantityType : HKUnit], Error?) -> Swift.Void)     func enableBackgroundDelivery(for type: HKObjectType, frequency frequency: HKUpdateFrequency, withCompletion completion: @escaping (Bool, Error?) -> Swift.Void)     func disableBackgroundDelivery(for type: HKObjectType, withCompletion completion: @escaping (Bool, Error?) -> Swift.Void)     func disableAllBackgroundDelivery(completion completion: @escaping (Bool, Error?) -> Swift.Void)     func add(_ samples: [HKSample], to workout: HKWorkout, completion completion: @escaping (Bool, Error?) -> Swift.Void)     func start(_ workoutSession: HKWorkoutSession)     func end(_ workoutSession: HKWorkoutSession)     func pause(_ workoutSession: HKWorkoutSession)     func resumeWorkoutSession(_ workoutSession: HKWorkoutSession)     func startWatchApp(with workoutConfiguration: HKWorkoutConfiguration, completion completion: @escaping (Bool, Error?) -> Swift.Void)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HKHealthStore : CVarArg { } extension HKHealthStore : Equatable, Hashable {     var hashValue: Int { get } } extension HKHealthStore {     func add(_ samples: [HKSample], to workout: HKWorkout, completion completion: @escaping (Bool, Error?) -> Swift.Void)     func start(_ workoutSession: HKWorkoutSession)     func end(_ workoutSession: HKWorkoutSession)     func pause(_ workoutSession: HKWorkoutSession)     func resumeWorkoutSession(_ workoutSession: HKWorkoutSession)     func startWatchApp(with workoutConfiguration: HKWorkoutConfiguration, completion completion: @escaping (Bool, Error?) -> Swift.Void) } extension HKHealthStore {     func enableBackgroundDelivery(for type: HKObjectType, frequency frequency: HKUpdateFrequency, withCompletion completion: @escaping (Bool, Error?) -> Swift.Void)     func disableBackgroundDelivery(for type: HKObjectType, withCompletion completion: @escaping (Bool, Error?) -> Swift.Void)     func disableAllBackgroundDelivery(completion completion: @escaping (Bool, Error?) -> Swift.Void) } extension HKHealthStore {     func preferredUnits(for quantityTypes: Set<HKQuantityType>, completion completion: @escaping ([HKQuantityType : HKUnit], Error?) -> Swift.Void) } ``` | CVarArg, Equatable, Hashable |

Modified [HKHealthStore.add(_: [HKSample], to: HKWorkout, completion: (Bool, Error?) -> Swift.Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614165-addsamples)

|  | Declaration |
| --- | --- |
| From | ``` func addSamples(_ samples: [HKSample], toWorkout workout: HKWorkout, completion completion: (Bool, NSError?) -> Void) ``` |
| To | ``` func add(_ samples: [HKSample], to workout: HKWorkout, completion completion: @escaping (Bool, Error?) -> Swift.Void) ``` |

Modified [HKHealthStore.authorizationStatus(for: HKObjectType) -> HKAuthorizationStatus](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614154-authorizationstatus)

|  | Declaration |
| --- | --- |
| From | ``` func authorizationStatusForType(_ type: HKObjectType) -> HKAuthorizationStatus ``` |
| To | ``` func authorizationStatus(for type: HKObjectType) -> HKAuthorizationStatus ``` |

Modified [HKHealthStore.dateOfBirth() throws -> Date](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614160-dateofbirthwitherror)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func dateOfBirth() throws -> NSDate ``` | -- |
| To | ``` func dateOfBirth() throws -> Date ``` | iOS 10.0 |

Modified [HKHealthStore.delete(_: [HKObject], withCompletion: (Bool, Error?) -> Swift.Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614163-delete)

|  | Declaration |
| --- | --- |
| From | ``` func deleteObjects(_ objects: [HKObject], withCompletion completion: (Bool, NSError?) -> Void) ``` |
| To | ``` func delete(_ objects: [HKObject], withCompletion completion: @escaping (Bool, Error?) -> Swift.Void) ``` |

Modified [HKHealthStore.delete(_: HKObject, withCompletion: (Bool, Error?) -> Swift.Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614155-delete)

|  | Declaration |
| --- | --- |
| From | ``` func deleteObject(_ object: HKObject, withCompletion completion: (Bool, NSError?) -> Void) ``` |
| To | ``` func delete(_ object: HKObject, withCompletion completion: @escaping (Bool, Error?) -> Swift.Void) ``` |

Modified [HKHealthStore.deleteObjects(of: HKObjectType, predicate: NSPredicate, withCompletion: (Bool, Int, Error?) -> Swift.Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614162-deleteobjects)

|  | Declaration |
| --- | --- |
| From | ``` func deleteObjectsOfType(_ objectType: HKObjectType, predicate predicate: NSPredicate, withCompletion completion: (Bool, Int, NSError?) -> Void) ``` |
| To | ``` func deleteObjects(of objectType: HKObjectType, predicate predicate: NSPredicate, withCompletion completion: @escaping (Bool, Int, Error?) -> Swift.Void) ``` |

Modified [HKHealthStore.disableAllBackgroundDelivery(completion: (Bool, Error?) -> Swift.Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614158-disableallbackgrounddelivery)

|  | Declaration |
| --- | --- |
| From | ``` func disableAllBackgroundDeliveryWithCompletion(_ completion: (Bool, NSError?) -> Void) ``` |
| To | ``` func disableAllBackgroundDelivery(completion completion: @escaping (Bool, Error?) -> Swift.Void) ``` |

Modified [HKHealthStore.disableBackgroundDelivery(for: HKObjectType, withCompletion: (Bool, Error?) -> Swift.Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614177-disablebackgrounddelivery)

|  | Declaration |
| --- | --- |
| From | ``` func disableBackgroundDeliveryForType(_ type: HKObjectType, withCompletion completion: (Bool, NSError?) -> Void) ``` |
| To | ``` func disableBackgroundDelivery(for type: HKObjectType, withCompletion completion: @escaping (Bool, Error?) -> Swift.Void) ``` |

Modified [HKHealthStore.earliestPermittedSampleDate() -> Date](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614166-earliestpermittedsampledate)

|  | Declaration |
| --- | --- |
| From | ``` func earliestPermittedSampleDate() -> NSDate ``` |
| To | ``` func earliestPermittedSampleDate() -> Date ``` |

Modified [HKHealthStore.enableBackgroundDelivery(for: HKObjectType, frequency: HKUpdateFrequency, withCompletion: (Bool, Error?) -> Swift.Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614175-enablebackgrounddelivery)

|  | Declaration |
| --- | --- |
| From | ``` func enableBackgroundDeliveryForType(_ type: HKObjectType, frequency frequency: HKUpdateFrequency, withCompletion completion: (Bool, NSError?) -> Void) ``` |
| To | ``` func enableBackgroundDelivery(for type: HKObjectType, frequency frequency: HKUpdateFrequency, withCompletion completion: @escaping (Bool, Error?) -> Swift.Void) ``` |

Modified [HKHealthStore.execute(_: HKQuery)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614179-execute)

|  | Declaration |
| --- | --- |
| From | ``` func executeQuery(_ query: HKQuery) ``` |
| To | ``` func execute(_ query: HKQuery) ``` |

Modified [HKHealthStore.handleAuthorizationForExtension(completion: (Bool, Error?) -> Swift.Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614153-handleauthorizationforextension)

|  | Declaration |
| --- | --- |
| From | ``` func handleAuthorizationForExtensionWithCompletion(_ completion: (Bool, NSError?) -> Void) ``` |
| To | ``` func handleAuthorizationForExtension(completion completion: @escaping (Bool, Error?) -> Swift.Void) ``` |

Modified [HKHealthStore.preferredUnits(for: Set<HKQuantityType>, completion: ([HKQuantityType : HKUnit], Error?) -> Swift.Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614172-preferredunits)

|  | Declaration |
| --- | --- |
| From | ``` func preferredUnitsForQuantityTypes(_ quantityTypes: Set<HKQuantityType>, completion completion: ([HKQuantityType : HKUnit], NSError?) -> Void) ``` |
| To | ``` func preferredUnits(for quantityTypes: Set<HKQuantityType>, completion completion: @escaping ([HKQuantityType : HKUnit], Error?) -> Swift.Void) ``` |

Modified [HKHealthStore.requestAuthorization(toShare: Set<HKSampleType>?, read: Set<HKObjectType>?, completion: (Bool, Error?) -> Swift.Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614152-requestauthorizationtosharetypes)

|  | Declaration |
| --- | --- |
| From | ``` func requestAuthorizationToShareTypes(_ typesToShare: Set<HKSampleType>?, readTypes typesToRead: Set<HKObjectType>?, completion completion: (Bool, NSError?) -> Void) ``` |
| To | ``` func requestAuthorization(toShare typesToShare: Set<HKSampleType>?, read typesToRead: Set<HKObjectType>?, completion completion: @escaping (Bool, Error?) -> Swift.Void) ``` |

Modified [HKHealthStore.save(_: HKObject, withCompletion: (Bool, Error?) -> Swift.Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614168-save)

|  | Declaration |
| --- | --- |
| From | ``` func saveObject(_ object: HKObject, withCompletion completion: (Bool, NSError?) -> Void) ``` |
| To | ``` func save(_ object: HKObject, withCompletion completion: @escaping (Bool, Error?) -> Swift.Void) ``` |

Modified [HKHealthStore.save(_: [HKObject], withCompletion: (Bool, Error?) -> Swift.Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614176-save)

|  | Declaration |
| --- | --- |
| From | ``` func saveObjects(_ objects: [HKObject], withCompletion completion: (Bool, NSError?) -> Void) ``` |
| To | ``` func save(_ objects: [HKObject], withCompletion completion: @escaping (Bool, Error?) -> Swift.Void) ``` |

Modified [HKHealthStore.splitTotalEnergy(_: HKQuantity, start: Date, end: Date, resultsHandler: (HKQuantity?, HKQuantity?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614170-splittotalenergy)

|  | Declaration |
| --- | --- |
| From | ``` func splitTotalEnergy(_ totalEnergy: HKQuantity, startDate startDate: NSDate, endDate endDate: NSDate, resultsHandler resultsHandler: (HKQuantity?, HKQuantity?, NSError?) -> Void) ``` |
| To | ``` func splitTotalEnergy(_ totalEnergy: HKQuantity, start startDate: Date, end endDate: Date, resultsHandler resultsHandler: @escaping (HKQuantity?, HKQuantity?, Error?) -> Swift.Void) ``` |

Modified [HKHealthStore.stop(_: HKQuery)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614173-stopquery)

|  | Declaration |
| --- | --- |
| From | ``` func stopQuery(_ query: HKQuery) ``` |
| To | ``` func stop(_ query: HKQuery) ``` |

Modified [HKHeartRateSensorLocation [enum]](https://developer.apple.com/documentation/healthkit/hkheartratesensorlocation)

|  | Declaration |
| --- | --- |
| From | ``` enum HKHeartRateSensorLocation : Int {     case Other     case Chest     case Wrist     case Finger     case Hand     case EarLobe     case Foot } ``` |
| To | ``` enum HKHeartRateSensorLocation : Int {     case other     case chest     case wrist     case finger     case hand     case earLobe     case foot } ``` |

Modified [HKHeartRateSensorLocation.chest](https://developer.apple.com/documentation/healthkit/hkheartratesensorlocation/chest)

|  | Declaration |
| --- | --- |
| From | ``` case Chest ``` |
| To | ``` case chest ``` |

Modified [HKHeartRateSensorLocation.earLobe](https://developer.apple.com/documentation/healthkit/hkheartratesensorlocation/earlobe)

|  | Declaration |
| --- | --- |
| From | ``` case EarLobe ``` |
| To | ``` case earLobe ``` |

Modified [HKHeartRateSensorLocation.finger](https://developer.apple.com/documentation/healthkit/hkheartratesensorlocation/finger)

|  | Declaration |
| --- | --- |
| From | ``` case Finger ``` |
| To | ``` case finger ``` |

Modified [HKHeartRateSensorLocation.foot](https://developer.apple.com/documentation/healthkit/hkheartratesensorlocation/foot)

|  | Declaration |
| --- | --- |
| From | ``` case Foot ``` |
| To | ``` case foot ``` |

Modified [HKHeartRateSensorLocation.hand](https://developer.apple.com/documentation/healthkit/hkheartratesensorlocation/hkheartratesensorlocationhand)

|  | Declaration |
| --- | --- |
| From | ``` case Hand ``` |
| To | ``` case hand ``` |

Modified [HKHeartRateSensorLocation.other](https://developer.apple.com/documentation/healthkit/hkheartratesensorlocation/other)

|  | Declaration |
| --- | --- |
| From | ``` case Other ``` |
| To | ``` case other ``` |

Modified [HKHeartRateSensorLocation.wrist](https://developer.apple.com/documentation/healthkit/hkheartratesensorlocation/hkheartratesensorlocationwrist)

|  | Declaration |
| --- | --- |
| From | ``` case Wrist ``` |
| To | ``` case wrist ``` |

Modified [HKMetricPrefix [enum]](https://developer.apple.com/documentation/healthkit/hkmetricprefix)

|  | Declaration |
| --- | --- |
| From | ``` enum HKMetricPrefix : Int {     case None     case Pico     case Nano     case Micro     case Milli     case Centi     case Deci     case Deca     case Hecto     case Kilo     case Mega     case Giga     case Tera } ``` |
| To | ``` enum HKMetricPrefix : Int {     case none     case pico     case nano     case micro     case milli     case centi     case deci     case deca     case hecto     case kilo     case mega     case giga     case tera } ``` |

Modified [HKMetricPrefix.centi](https://developer.apple.com/documentation/healthkit/hkmetricprefix/hkmetricprefixcenti)

|  | Declaration |
| --- | --- |
| From | ``` case Centi ``` |
| To | ``` case centi ``` |

Modified [HKMetricPrefix.deca](https://developer.apple.com/documentation/healthkit/hkmetricprefix/deca)

|  | Declaration |
| --- | --- |
| From | ``` case Deca ``` |
| To | ``` case deca ``` |

Modified [HKMetricPrefix.deci](https://developer.apple.com/documentation/healthkit/hkmetricprefix/deci)

|  | Declaration |
| --- | --- |
| From | ``` case Deci ``` |
| To | ``` case deci ``` |

Modified [HKMetricPrefix.giga](https://developer.apple.com/documentation/healthkit/hkmetricprefix/hkmetricprefixgiga)

|  | Declaration |
| --- | --- |
| From | ``` case Giga ``` |
| To | ``` case giga ``` |

Modified [HKMetricPrefix.hecto](https://developer.apple.com/documentation/healthkit/hkmetricprefix/hkmetricprefixhecto)

|  | Declaration |
| --- | --- |
| From | ``` case Hecto ``` |
| To | ``` case hecto ``` |

Modified [HKMetricPrefix.kilo](https://developer.apple.com/documentation/healthkit/hkmetricprefix/hkmetricprefixkilo)

|  | Declaration |
| --- | --- |
| From | ``` case Kilo ``` |
| To | ``` case kilo ``` |

Modified [HKMetricPrefix.mega](https://developer.apple.com/documentation/healthkit/hkmetricprefix/mega)

|  | Declaration |
| --- | --- |
| From | ``` case Mega ``` |
| To | ``` case mega ``` |

Modified [HKMetricPrefix.micro](https://developer.apple.com/documentation/healthkit/hkmetricprefix/micro)

|  | Declaration |
| --- | --- |
| From | ``` case Micro ``` |
| To | ``` case micro ``` |

Modified [HKMetricPrefix.milli](https://developer.apple.com/documentation/healthkit/hkmetricprefix/hkmetricprefixmilli)

|  | Declaration |
| --- | --- |
| From | ``` case Milli ``` |
| To | ``` case milli ``` |

Modified [HKMetricPrefix.nano](https://developer.apple.com/documentation/healthkit/hkmetricprefix/nano)

|  | Declaration |
| --- | --- |
| From | ``` case Nano ``` |
| To | ``` case nano ``` |

Modified [HKMetricPrefix.none](https://developer.apple.com/documentation/healthkit/hkmetricprefix/hkmetricprefixnone)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [HKMetricPrefix.pico](https://developer.apple.com/documentation/healthkit/hkmetricprefix/pico)

|  | Declaration |
| --- | --- |
| From | ``` case Pico ``` |
| To | ``` case pico ``` |

Modified [HKMetricPrefix.tera](https://developer.apple.com/documentation/healthkit/hkmetricprefix/tera)

|  | Declaration |
| --- | --- |
| From | ``` case Tera ``` |
| To | ``` case tera ``` |

Modified [HKObject](https://developer.apple.com/documentation/healthkit/hkobject)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKObject : NSObject, NSSecureCoding {     var UUID: NSUUID { get }     var source: HKSource { get }     var sourceRevision: HKSourceRevision { get }     var device: HKDevice? { get }     var metadata: [String : AnyObject]? { get }     init() } ``` | NSSecureCoding |
| To | ``` class HKObject : NSObject, NSSecureCoding {     var uuid: UUID { get }     var source: HKSource { get }     var sourceRevision: HKSourceRevision { get }     var device: HKDevice? { get }     var metadata: [String : Any]? { get }     init()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HKObject : CVarArg { } extension HKObject : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSSecureCoding |

Modified [HKObject.metadata](https://developer.apple.com/documentation/healthkit/hkobject/1615598-metadata)

|  | Declaration |
| --- | --- |
| From | ``` var metadata: [String : AnyObject]? { get } ``` |
| To | ``` var metadata: [String : Any]? { get } ``` |

Modified [HKObject.uuid](https://developer.apple.com/documentation/healthkit/hkobject/1615721-uuid)

|  | Declaration |
| --- | --- |
| From | ``` var UUID: NSUUID { get } ``` |
| To | ``` var uuid: UUID { get } ``` |

Modified [HKObjectType](https://developer.apple.com/documentation/healthkit/hkobjecttype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKObjectType : NSObject, NSSecureCoding, NSCopying {     var identifier: String { get }     init()     class func quantityTypeForIdentifier(_ identifier: String) -> HKQuantityType?     class func categoryTypeForIdentifier(_ identifier: String) -> HKCategoryType?     class func characteristicTypeForIdentifier(_ identifier: String) -> HKCharacteristicType?     class func correlationTypeForIdentifier(_ identifier: String) -> HKCorrelationType?     class func workoutType() -> HKWorkoutType     class func activitySummaryType() -> HKActivitySummaryType } ``` | NSCopying, NSSecureCoding |
| To | ``` class HKObjectType : NSObject, NSSecureCoding, NSCopying {     var identifier: String { get }     init()     class func quantityType(forIdentifier identifier: HKQuantityTypeIdentifier) -> HKQuantityType?     class func categoryType(forIdentifier identifier: HKCategoryTypeIdentifier) -> HKCategoryType?     class func characteristicType(forIdentifier identifier: HKCharacteristicTypeIdentifier) -> HKCharacteristicType?     class func correlationType(forIdentifier identifier: HKCorrelationTypeIdentifier) -> HKCorrelationType?     class func documentType(forIdentifier identifier: HKDocumentTypeIdentifier) -> HKDocumentType?     class func workoutType() -> HKWorkoutType     class func activitySummaryType() -> HKActivitySummaryType     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HKObjectType : CVarArg { } extension HKObjectType : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [HKObjectType.categoryType(forIdentifier: HKCategoryTypeIdentifier) -> HKCategoryType? [class]](https://developer.apple.com/documentation/healthkit/hkobjecttype/1615526-categorytype)

|  | Declaration |
| --- | --- |
| From | ``` class func categoryTypeForIdentifier(_ identifier: String) -> HKCategoryType? ``` |
| To | ``` class func categoryType(forIdentifier identifier: HKCategoryTypeIdentifier) -> HKCategoryType? ``` |

Modified [HKObjectType.characteristicType(forIdentifier: HKCharacteristicTypeIdentifier) -> HKCharacteristicType? [class]](https://developer.apple.com/documentation/healthkit/hkobjecttype/1615558-characteristictype)

|  | Declaration |
| --- | --- |
| From | ``` class func characteristicTypeForIdentifier(_ identifier: String) -> HKCharacteristicType? ``` |
| To | ``` class func characteristicType(forIdentifier identifier: HKCharacteristicTypeIdentifier) -> HKCharacteristicType? ``` |

Modified [HKObjectType.correlationType(forIdentifier: HKCorrelationTypeIdentifier) -> HKCorrelationType? [class]](https://developer.apple.com/documentation/healthkit/hkobjecttype/1615580-correlationtype)

|  | Declaration |
| --- | --- |
| From | ``` class func correlationTypeForIdentifier(_ identifier: String) -> HKCorrelationType? ``` |
| To | ``` class func correlationType(forIdentifier identifier: HKCorrelationTypeIdentifier) -> HKCorrelationType? ``` |

Modified [HKObjectType.quantityType(forIdentifier: HKQuantityTypeIdentifier) -> HKQuantityType? [class]](https://developer.apple.com/documentation/healthkit/hkobjecttype/1615298-quantitytypeforidentifier)

|  | Declaration |
| --- | --- |
| From | ``` class func quantityTypeForIdentifier(_ identifier: String) -> HKQuantityType? ``` |
| To | ``` class func quantityType(forIdentifier identifier: HKQuantityTypeIdentifier) -> HKQuantityType? ``` |

Modified [HKObserverQuery](https://developer.apple.com/documentation/healthkit/hkobserverquery)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKObserverQuery : HKQuery {     init(sampleType sampleType: HKSampleType, predicate predicate: NSPredicate?, updateHandler updateHandler: (HKObserverQuery, HKObserverQueryCompletionHandler, NSError?) -> Void) } ``` | -- |
| To | ``` class HKObserverQuery : HKQuery {     init(sampleType sampleType: HKSampleType, predicate predicate: NSPredicate?, updateHandler updateHandler: @escaping (HKObserverQuery, HealthKit.HKObserverQueryCompletionHandler, Error?) -> Swift.Void)     class func predicateForActivitySummary(with dateComponents: DateComponents) -> NSPredicate     class func predicate(forActivitySummariesBetweenStart startDateComponents: DateComponents, end endDateComponents: DateComponents) -> NSPredicate     class func predicateForWorkouts(with workoutActivityType: HKWorkoutActivityType) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, duration duration: TimeInterval) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalEnergyBurned totalEnergyBurned: HKQuantity) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalDistance totalDistance: HKQuantity) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalSwimmingStrokeCount totalSwimmingStrokeCount: HKQuantity) -> NSPredicate     class func predicateForCategorySamples(with operatorType: NSComparisonPredicate.Operator, value value: Int) -> NSPredicate     class func predicateForQuantitySamples(with operatorType: NSComparisonPredicate.Operator, quantity quantity: HKQuantity) -> NSPredicate     class func predicateForSamples(withStart startDate: Date?, end endDate: Date?, options options: HKQueryOptions = []) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String, allowedValues allowedValues: [Any]) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String, operatorType operatorType: NSComparisonPredicate.Operator, value value: Any) -> NSPredicate     class func predicateForObjects(from source: HKSource) -> NSPredicate     class func predicateForObjects(from sources: Set<HKSource>) -> NSPredicate     class func predicateForObjects(from sourceRevisions: Set<HKSourceRevision>) -> NSPredicate     class func predicateForObjects(from devices: Set<HKDevice>) -> NSPredicate     class func predicateForObjects(withDeviceProperty key: String, allowedValues allowedValues: Set<String>) -> NSPredicate     class func predicateForObject(with UUID: UUID) -> NSPredicate     class func predicateForObjects(with UUIDs: Set<UUID>) -> NSPredicate     class func predicateForObjectsWithNoCorrelation() -> NSPredicate     class func predicateForObjects(from workout: HKWorkout) -> NSPredicate     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HKObserverQuery : CVarArg { } extension HKObserverQuery : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [HKObserverQuery.init(sampleType: HKSampleType, predicate: NSPredicate?, updateHandler: (HKObserverQuery, HealthKit.HKObserverQueryCompletionHandler, Error?) -> Swift.Void)](https://developer.apple.com/documentation/healthkit/hkobserverquery/1615317-init)

|  | Declaration |
| --- | --- |
| From | ``` init(sampleType sampleType: HKSampleType, predicate predicate: NSPredicate?, updateHandler updateHandler: (HKObserverQuery, HKObserverQueryCompletionHandler, NSError?) -> Void) ``` |
| To | ``` init(sampleType sampleType: HKSampleType, predicate predicate: NSPredicate?, updateHandler updateHandler: @escaping (HKObserverQuery, HealthKit.HKObserverQueryCompletionHandler, Error?) -> Swift.Void) ``` |

Modified [HKQuantity](https://developer.apple.com/documentation/healthkit/hkquantity)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKQuantity : NSObject, NSSecureCoding, NSCopying {     init()     convenience init(unit unit: HKUnit, doubleValue value: Double)     class func quantityWithUnit(_ unit: HKUnit, doubleValue value: Double) -> Self     func isCompatibleWithUnit(_ unit: HKUnit) -> Bool     func doubleValueForUnit(_ unit: HKUnit) -> Double     func compare(_ quantity: HKQuantity) -> NSComparisonResult } ``` | NSCopying, NSSecureCoding |
| To | ``` class HKQuantity : NSObject, NSSecureCoding, NSCopying {     init()     convenience init(unit unit: HKUnit, doubleValue value: Double)     class func withUnit(_ unit: HKUnit, doubleValue value: Double) -> Self     func `is`(compatibleWith unit: HKUnit) -> Bool     func doubleValue(for unit: HKUnit) -> Double     func compare(_ quantity: HKQuantity) -> ComparisonResult     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HKQuantity : CVarArg { } extension HKQuantity : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [HKQuantity.compare(_: HKQuantity) -> ComparisonResult](https://developer.apple.com/documentation/healthkit/hkquantity/1615160-compare)

|  | Declaration |
| --- | --- |
| From | ``` func compare(_ quantity: HKQuantity) -> NSComparisonResult ``` |
| To | ``` func compare(_ quantity: HKQuantity) -> ComparisonResult ``` |

Modified [HKQuantity.doubleValue(for: HKUnit) -> Double](https://developer.apple.com/documentation/healthkit/hkquantity/1615245-doublevalueforunit)

|  | Declaration |
| --- | --- |
| From | ``` func doubleValueForUnit(_ unit: HKUnit) -> Double ``` |
| To | ``` func doubleValue(for unit: HKUnit) -> Double ``` |

Modified [HKQuantity.is(compatibleWith: HKUnit) -> Bool](https://developer.apple.com/documentation/healthkit/hkquantity/1615508-iscompatiblewithunit)

|  | Declaration |
| --- | --- |
| From | ``` func isCompatibleWithUnit(_ unit: HKUnit) -> Bool ``` |
| To | ``` func `is`(compatibleWith unit: HKUnit) -> Bool ``` |

Modified [HKQuantityAggregationStyle [enum]](https://developer.apple.com/documentation/healthkit/hkquantityaggregationstyle)

|  | Declaration |
| --- | --- |
| From | ``` enum HKQuantityAggregationStyle : Int {     case Cumulative     case Discrete } ``` |
| To | ``` enum HKQuantityAggregationStyle : Int {     case cumulative     case discrete } ``` |

Modified [HKQuantityAggregationStyle.cumulative](https://developer.apple.com/documentation/healthkit/hkquantityaggregationstyle/hkquantityaggregationstylecumulative)

|  | Declaration |
| --- | --- |
| From | ``` case Cumulative ``` |
| To | ``` case cumulative ``` |

Modified [HKQuantityAggregationStyle.discrete](https://developer.apple.com/documentation/healthkit/hkquantityaggregationstyle/hkquantityaggregationstylediscrete)

|  | Declaration |
| --- | --- |
| From | ``` case Discrete ``` |
| To | ``` case discrete ``` |

Modified [HKQuantitySample](https://developer.apple.com/documentation/healthkit/hkquantitysample)

|  | Declaration |
| --- | --- |
| From | ``` class HKQuantitySample : HKSample {     var quantityType: HKQuantityType { get }     var quantity: HKQuantity { get }     convenience init(type quantityType: HKQuantityType, quantity quantity: HKQuantity, startDate startDate: NSDate, endDate endDate: NSDate)     class func quantitySampleWithType(_ quantityType: HKQuantityType, quantity quantity: HKQuantity, startDate startDate: NSDate, endDate endDate: NSDate) -> Self     convenience init(type quantityType: HKQuantityType, quantity quantity: HKQuantity, startDate startDate: NSDate, endDate endDate: NSDate, metadata metadata: [String : AnyObject]?)     class func quantitySampleWithType(_ quantityType: HKQuantityType, quantity quantity: HKQuantity, startDate startDate: NSDate, endDate endDate: NSDate, metadata metadata: [String : AnyObject]?) -> Self     convenience init(type quantityType: HKQuantityType, quantity quantity: HKQuantity, startDate startDate: NSDate, endDate endDate: NSDate, device device: HKDevice?, metadata metadata: [String : AnyObject]?)     class func quantitySampleWithType(_ quantityType: HKQuantityType, quantity quantity: HKQuantity, startDate startDate: NSDate, endDate endDate: NSDate, device device: HKDevice?, metadata metadata: [String : AnyObject]?) -> Self } ``` |
| To | ``` class HKQuantitySample : HKSample {     var quantityType: HKQuantityType { get }     var quantity: HKQuantity { get }     convenience init(type quantityType: HKQuantityType, quantity quantity: HKQuantity, start startDate: Date, end endDate: Date)     class func withType(_ quantityType: HKQuantityType, quantity quantity: HKQuantity, start startDate: Date, end endDate: Date) -> Self     convenience init(type quantityType: HKQuantityType, quantity quantity: HKQuantity, start startDate: Date, end endDate: Date, metadata metadata: [String : Any]?)     class func withType(_ quantityType: HKQuantityType, quantity quantity: HKQuantity, start startDate: Date, end endDate: Date, metadata metadata: [String : Any]?) -> Self     convenience init(type quantityType: HKQuantityType, quantity quantity: HKQuantity, start startDate: Date, end endDate: Date, device device: HKDevice?, metadata metadata: [String : Any]?)     class func withType(_ quantityType: HKQuantityType, quantity quantity: HKQuantity, start startDate: Date, end endDate: Date, device device: HKDevice?, metadata metadata: [String : Any]?) -> Self } ``` |

Modified [HKQuantitySample.init(type: HKQuantityType, quantity: HKQuantity, start: Date, end: Date)](https://developer.apple.com/documentation/healthkit/hkquantitysample/1615016-quantitysamplewithtype)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(type quantityType: HKQuantityType, quantity quantity: HKQuantity, startDate startDate: NSDate, endDate endDate: NSDate) ``` |
| To | ``` convenience init(type quantityType: HKQuantityType, quantity quantity: HKQuantity, start startDate: Date, end endDate: Date) ``` |

Modified [HKQuantitySample.init(type: HKQuantityType, quantity: HKQuantity, start: Date, end: Date, device: HKDevice?, metadata: [String : Any]?)](https://developer.apple.com/documentation/healthkit/hkquantitysample/1615019-quantitysamplewithtype)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(type quantityType: HKQuantityType, quantity quantity: HKQuantity, startDate startDate: NSDate, endDate endDate: NSDate, device device: HKDevice?, metadata metadata: [String : AnyObject]?) ``` |
| To | ``` convenience init(type quantityType: HKQuantityType, quantity quantity: HKQuantity, start startDate: Date, end endDate: Date, device device: HKDevice?, metadata metadata: [String : Any]?) ``` |

Modified [HKQuantitySample.init(type: HKQuantityType, quantity: HKQuantity, start: Date, end: Date, metadata: [String : Any]?)](https://developer.apple.com/documentation/healthkit/hkquantitysample/1615017-quantitysamplewithtype)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(type quantityType: HKQuantityType, quantity quantity: HKQuantity, startDate startDate: NSDate, endDate endDate: NSDate, metadata metadata: [String : AnyObject]?) ``` |
| To | ``` convenience init(type quantityType: HKQuantityType, quantity quantity: HKQuantity, start startDate: Date, end endDate: Date, metadata metadata: [String : Any]?) ``` |

Modified [HKQuantityType](https://developer.apple.com/documentation/healthkit/hkquantitytype)

|  | Declaration |
| --- | --- |
| From | ``` class HKQuantityType : HKSampleType {     var aggregationStyle: HKQuantityAggregationStyle { get }     func isCompatibleWithUnit(_ unit: HKUnit) -> Bool } ``` |
| To | ``` class HKQuantityType : HKSampleType {     var aggregationStyle: HKQuantityAggregationStyle { get }     func `is`(compatibleWith unit: HKUnit) -> Bool } ``` |

Modified [HKQuantityType.is(compatibleWith: HKUnit) -> Bool](https://developer.apple.com/documentation/healthkit/hkquantitytype/1615719-iscompatiblewithunit)

|  | Declaration |
| --- | --- |
| From | ``` func isCompatibleWithUnit(_ unit: HKUnit) -> Bool ``` |
| To | ``` func `is`(compatibleWith unit: HKUnit) -> Bool ``` |

Modified [HKQuantityTypeIdentifier.activeEnergyBurned](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615771-activeenergyburned)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierActiveEnergyBurned | ``` let HKQuantityTypeIdentifierActiveEnergyBurned: String ``` |
| To | activeEnergyBurned | ``` static let activeEnergyBurned: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.appleExerciseTime](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615696-appleexercisetime)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierAppleExerciseTime | ``` let HKQuantityTypeIdentifierAppleExerciseTime: String ``` |
| To | appleExerciseTime | ``` static let appleExerciseTime: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.basalBodyTemperature](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierbasalbodytemperature)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierBasalBodyTemperature | ``` let HKQuantityTypeIdentifierBasalBodyTemperature: String ``` |
| To | basalBodyTemperature | ``` static let basalBodyTemperature: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.basalEnergyBurned](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615512-basalenergyburned)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierBasalEnergyBurned | ``` let HKQuantityTypeIdentifierBasalEnergyBurned: String ``` |
| To | basalEnergyBurned | ``` static let basalEnergyBurned: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.bloodAlcoholContent](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierbloodalcoholcontent)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierBloodAlcoholContent | ``` let HKQuantityTypeIdentifierBloodAlcoholContent: String ``` |
| To | bloodAlcoholContent | ``` static let bloodAlcoholContent: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.bloodGlucose](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615455-bloodglucose)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierBloodGlucose | ``` let HKQuantityTypeIdentifierBloodGlucose: String ``` |
| To | bloodGlucose | ``` static let bloodGlucose: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.bloodPressureDiastolic](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierbloodpressurediastolic)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierBloodPressureDiastolic | ``` let HKQuantityTypeIdentifierBloodPressureDiastolic: String ``` |
| To | bloodPressureDiastolic | ``` static let bloodPressureDiastolic: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.bloodPressureSystolic](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierbloodpressuresystolic)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierBloodPressureSystolic | ``` let HKQuantityTypeIdentifierBloodPressureSystolic: String ``` |
| To | bloodPressureSystolic | ``` static let bloodPressureSystolic: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.bodyFatPercentage](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierbodyfatpercentage)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierBodyFatPercentage | ``` let HKQuantityTypeIdentifierBodyFatPercentage: String ``` |
| To | bodyFatPercentage | ``` static let bodyFatPercentage: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.bodyMass](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615693-bodymass)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierBodyMass | ``` let HKQuantityTypeIdentifierBodyMass: String ``` |
| To | bodyMass | ``` static let bodyMass: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.bodyMassIndex](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierbodymassindex)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierBodyMassIndex | ``` let HKQuantityTypeIdentifierBodyMassIndex: String ``` |
| To | bodyMassIndex | ``` static let bodyMassIndex: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.bodyTemperature](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierbodytemperature)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierBodyTemperature | ``` let HKQuantityTypeIdentifierBodyTemperature: String ``` |
| To | bodyTemperature | ``` static let bodyTemperature: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryBiotin](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierdietarybiotin)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryBiotin | ``` let HKQuantityTypeIdentifierDietaryBiotin: String ``` |
| To | dietaryBiotin | ``` static let dietaryBiotin: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryCaffeine](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierdietarycaffeine)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryCaffeine | ``` let HKQuantityTypeIdentifierDietaryCaffeine: String ``` |
| To | dietaryCaffeine | ``` static let dietaryCaffeine: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryCalcium](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierdietarycalcium)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryCalcium | ``` let HKQuantityTypeIdentifierDietaryCalcium: String ``` |
| To | dietaryCalcium | ``` static let dietaryCalcium: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryCarbohydrates](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615699-dietarycarbohydrates)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryCarbohydrates | ``` let HKQuantityTypeIdentifierDietaryCarbohydrates: String ``` |
| To | dietaryCarbohydrates | ``` static let dietaryCarbohydrates: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryChloride](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615497-dietarychloride)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryChloride | ``` let HKQuantityTypeIdentifierDietaryChloride: String ``` |
| To | dietaryChloride | ``` static let dietaryChloride: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryCholesterol](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierdietarycholesterol)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryCholesterol | ``` let HKQuantityTypeIdentifierDietaryCholesterol: String ``` |
| To | dietaryCholesterol | ``` static let dietaryCholesterol: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryChromium](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierdietarychromium)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryChromium | ``` let HKQuantityTypeIdentifierDietaryChromium: String ``` |
| To | dietaryChromium | ``` static let dietaryChromium: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryCopper](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615774-dietarycopper)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryCopper | ``` let HKQuantityTypeIdentifierDietaryCopper: String ``` |
| To | dietaryCopper | ``` static let dietaryCopper: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryEnergyConsumed](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierdietaryenergyconsumed)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryEnergyConsumed | ``` let HKQuantityTypeIdentifierDietaryEnergyConsumed: String ``` |
| To | dietaryEnergyConsumed | ``` static let dietaryEnergyConsumed: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryFatMonounsaturated](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierdietaryfatmonounsaturated)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryFatMonounsaturated | ``` let HKQuantityTypeIdentifierDietaryFatMonounsaturated: String ``` |
| To | dietaryFatMonounsaturated | ``` static let dietaryFatMonounsaturated: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryFatPolyunsaturated](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierdietaryfatpolyunsaturated)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryFatPolyunsaturated | ``` let HKQuantityTypeIdentifierDietaryFatPolyunsaturated: String ``` |
| To | dietaryFatPolyunsaturated | ``` static let dietaryFatPolyunsaturated: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryFatSaturated](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615685-dietaryfatsaturated)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryFatSaturated | ``` let HKQuantityTypeIdentifierDietaryFatSaturated: String ``` |
| To | dietaryFatSaturated | ``` static let dietaryFatSaturated: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryFatTotal](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierdietaryfattotal)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryFatTotal | ``` let HKQuantityTypeIdentifierDietaryFatTotal: String ``` |
| To | dietaryFatTotal | ``` static let dietaryFatTotal: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryFiber](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615040-dietaryfiber)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryFiber | ``` let HKQuantityTypeIdentifierDietaryFiber: String ``` |
| To | dietaryFiber | ``` static let dietaryFiber: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryFolate](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615578-dietaryfolate)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryFolate | ``` let HKQuantityTypeIdentifierDietaryFolate: String ``` |
| To | dietaryFolate | ``` static let dietaryFolate: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryIodine](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615151-dietaryiodine)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryIodine | ``` let HKQuantityTypeIdentifierDietaryIodine: String ``` |
| To | dietaryIodine | ``` static let dietaryIodine: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryIron](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615227-dietaryiron)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryIron | ``` let HKQuantityTypeIdentifierDietaryIron: String ``` |
| To | dietaryIron | ``` static let dietaryIron: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryMagnesium](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615184-dietarymagnesium)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryMagnesium | ``` let HKQuantityTypeIdentifierDietaryMagnesium: String ``` |
| To | dietaryMagnesium | ``` static let dietaryMagnesium: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryManganese](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierdietarymanganese)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryManganese | ``` let HKQuantityTypeIdentifierDietaryManganese: String ``` |
| To | dietaryManganese | ``` static let dietaryManganese: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryMolybdenum](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierdietarymolybdenum)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryMolybdenum | ``` let HKQuantityTypeIdentifierDietaryMolybdenum: String ``` |
| To | dietaryMolybdenum | ``` static let dietaryMolybdenum: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryNiacin](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierdietaryniacin)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryNiacin | ``` let HKQuantityTypeIdentifierDietaryNiacin: String ``` |
| To | dietaryNiacin | ``` static let dietaryNiacin: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryPantothenicAcid](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615122-dietarypantothenicacid)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryPantothenicAcid | ``` let HKQuantityTypeIdentifierDietaryPantothenicAcid: String ``` |
| To | dietaryPantothenicAcid | ``` static let dietaryPantothenicAcid: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryPhosphorus](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierdietaryphosphorus)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryPhosphorus | ``` let HKQuantityTypeIdentifierDietaryPhosphorus: String ``` |
| To | dietaryPhosphorus | ``` static let dietaryPhosphorus: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryPotassium](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierdietarypotassium)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryPotassium | ``` let HKQuantityTypeIdentifierDietaryPotassium: String ``` |
| To | dietaryPotassium | ``` static let dietaryPotassium: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryProtein](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615652-dietaryprotein)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryProtein | ``` let HKQuantityTypeIdentifierDietaryProtein: String ``` |
| To | dietaryProtein | ``` static let dietaryProtein: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryRiboflavin](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615353-dietaryriboflavin)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryRiboflavin | ``` let HKQuantityTypeIdentifierDietaryRiboflavin: String ``` |
| To | dietaryRiboflavin | ``` static let dietaryRiboflavin: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietarySelenium](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierdietaryselenium)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietarySelenium | ``` let HKQuantityTypeIdentifierDietarySelenium: String ``` |
| To | dietarySelenium | ``` static let dietarySelenium: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietarySodium](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615402-dietarysodium)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietarySodium | ``` let HKQuantityTypeIdentifierDietarySodium: String ``` |
| To | dietarySodium | ``` static let dietarySodium: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietarySugar](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615674-dietarysugar)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietarySugar | ``` let HKQuantityTypeIdentifierDietarySugar: String ``` |
| To | dietarySugar | ``` static let dietarySugar: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryThiamin](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierdietarythiamin)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryThiamin | ``` let HKQuantityTypeIdentifierDietaryThiamin: String ``` |
| To | dietaryThiamin | ``` static let dietaryThiamin: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryVitaminA](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615711-dietaryvitamina)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryVitaminA | ``` let HKQuantityTypeIdentifierDietaryVitaminA: String ``` |
| To | dietaryVitaminA | ``` static let dietaryVitaminA: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryVitaminB12](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615244-dietaryvitaminb12)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryVitaminB12 | ``` let HKQuantityTypeIdentifierDietaryVitaminB12: String ``` |
| To | dietaryVitaminB12 | ``` static let dietaryVitaminB12: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryVitaminB6](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615239-dietaryvitaminb6)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryVitaminB6 | ``` let HKQuantityTypeIdentifierDietaryVitaminB6: String ``` |
| To | dietaryVitaminB6 | ``` static let dietaryVitaminB6: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryVitaminC](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierdietaryvitaminc)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryVitaminC | ``` let HKQuantityTypeIdentifierDietaryVitaminC: String ``` |
| To | dietaryVitaminC | ``` static let dietaryVitaminC: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryVitaminD](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierdietaryvitamind)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryVitaminD | ``` let HKQuantityTypeIdentifierDietaryVitaminD: String ``` |
| To | dietaryVitaminD | ``` static let dietaryVitaminD: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryVitaminE](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615330-dietaryvitamine)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryVitaminE | ``` let HKQuantityTypeIdentifierDietaryVitaminE: String ``` |
| To | dietaryVitaminE | ``` static let dietaryVitaminE: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryVitaminK](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierdietaryvitamink)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryVitaminK | ``` let HKQuantityTypeIdentifierDietaryVitaminK: String ``` |
| To | dietaryVitaminK | ``` static let dietaryVitaminK: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryWater](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierdietarywater)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryWater | ``` let HKQuantityTypeIdentifierDietaryWater: String ``` |
| To | dietaryWater | ``` static let dietaryWater: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.dietaryZinc](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615345-dietaryzinc)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDietaryZinc | ``` let HKQuantityTypeIdentifierDietaryZinc: String ``` |
| To | dietaryZinc | ``` static let dietaryZinc: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.distanceCycling](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierdistancecycling)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDistanceCycling | ``` let HKQuantityTypeIdentifierDistanceCycling: String ``` |
| To | distanceCycling | ``` static let distanceCycling: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.distanceWalkingRunning](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615230-distancewalkingrunning)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierDistanceWalkingRunning | ``` let HKQuantityTypeIdentifierDistanceWalkingRunning: String ``` |
| To | distanceWalkingRunning | ``` static let distanceWalkingRunning: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.electrodermalActivity](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615574-electrodermalactivity)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierElectrodermalActivity | ``` let HKQuantityTypeIdentifierElectrodermalActivity: String ``` |
| To | electrodermalActivity | ``` static let electrodermalActivity: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.flightsClimbed](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierflightsclimbed)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierFlightsClimbed | ``` let HKQuantityTypeIdentifierFlightsClimbed: String ``` |
| To | flightsClimbed | ``` static let flightsClimbed: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.forcedExpiratoryVolume1](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615661-forcedexpiratoryvolume1)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierForcedExpiratoryVolume1 | ``` let HKQuantityTypeIdentifierForcedExpiratoryVolume1: String ``` |
| To | forcedExpiratoryVolume1 | ``` static let forcedExpiratoryVolume1: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.forcedVitalCapacity](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierforcedvitalcapacity)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierForcedVitalCapacity | ``` let HKQuantityTypeIdentifierForcedVitalCapacity: String ``` |
| To | forcedVitalCapacity | ``` static let forcedVitalCapacity: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.heartRate](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615138-heartrate)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierHeartRate | ``` let HKQuantityTypeIdentifierHeartRate: String ``` |
| To | heartRate | ``` static let heartRate: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.height](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierheight)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierHeight | ``` let HKQuantityTypeIdentifierHeight: String ``` |
| To | height | ``` static let height: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.inhalerUsage](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierinhalerusage)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierInhalerUsage | ``` let HKQuantityTypeIdentifierInhalerUsage: String ``` |
| To | inhalerUsage | ``` static let inhalerUsage: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.leanBodyMass](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615664-leanbodymass)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierLeanBodyMass | ``` let HKQuantityTypeIdentifierLeanBodyMass: String ``` |
| To | leanBodyMass | ``` static let leanBodyMass: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.nikeFuel](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifiernikefuel)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierNikeFuel | ``` let HKQuantityTypeIdentifierNikeFuel: String ``` |
| To | nikeFuel | ``` static let nikeFuel: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.numberOfTimesFallen](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifiernumberoftimesfallen)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierNumberOfTimesFallen | ``` let HKQuantityTypeIdentifierNumberOfTimesFallen: String ``` |
| To | numberOfTimesFallen | ``` static let numberOfTimesFallen: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.oxygenSaturation](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifieroxygensaturation)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierOxygenSaturation | ``` let HKQuantityTypeIdentifierOxygenSaturation: String ``` |
| To | oxygenSaturation | ``` static let oxygenSaturation: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.peakExpiratoryFlowRate](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierpeakexpiratoryflowrate)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierPeakExpiratoryFlowRate | ``` let HKQuantityTypeIdentifierPeakExpiratoryFlowRate: String ``` |
| To | peakExpiratoryFlowRate | ``` static let peakExpiratoryFlowRate: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.peripheralPerfusionIndex](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615442-peripheralperfusionindex)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierPeripheralPerfusionIndex | ``` let HKQuantityTypeIdentifierPeripheralPerfusionIndex: String ``` |
| To | peripheralPerfusionIndex | ``` static let peripheralPerfusionIndex: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.respiratoryRate](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierrespiratoryrate)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierRespiratoryRate | ``` let HKQuantityTypeIdentifierRespiratoryRate: String ``` |
| To | respiratoryRate | ``` static let respiratoryRate: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.stepCount](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615548-stepcount)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierStepCount | ``` let HKQuantityTypeIdentifierStepCount: String ``` |
| To | stepCount | ``` static let stepCount: HKQuantityTypeIdentifier ``` |

Modified [HKQuantityTypeIdentifier.uvExposure](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615195-uvexposure)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKQuantityTypeIdentifierUVExposure | ``` let HKQuantityTypeIdentifierUVExposure: String ``` |
| To | uvExposure | ``` static let uvExposure: HKQuantityTypeIdentifier ``` |

Modified [HKQuery](https://developer.apple.com/documentation/healthkit/hkquery)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKQuery : NSObject {     var objectType: HKObjectType? { get }     var sampleType: HKSampleType? { get }     var predicate: NSPredicate? { get }     init() } extension HKQuery {     class func predicateForObjectsWithMetadataKey(_ key: String) -> NSPredicate     class func predicateForObjectsWithMetadataKey(_ key: String, allowedValues allowedValues: [AnyObject]) -> NSPredicate     class func predicateForObjectsWithMetadataKey(_ key: String, operatorType operatorType: NSPredicateOperatorType, value value: AnyObject) -> NSPredicate     class func predicateForObjectsFromSource(_ source: HKSource) -> NSPredicate     class func predicateForObjectsFromSources(_ sources: Set<HKSource>) -> NSPredicate     class func predicateForObjectsFromSourceRevisions(_ sourceRevisions: Set<HKSourceRevision>) -> NSPredicate     class func predicateForObjectsFromDevices(_ devices: Set<HKDevice>) -> NSPredicate     class func predicateForObjectsWithDeviceProperty(_ key: String, allowedValues allowedValues: Set<String>) -> NSPredicate     class func predicateForObjectWithUUID(_ UUID: NSUUID) -> NSPredicate     class func predicateForObjectsWithUUIDs(_ UUIDs: Set<NSUUID>) -> NSPredicate     class func predicateForObjectsWithNoCorrelation() -> NSPredicate     class func predicateForObjectsFromWorkout(_ workout: HKWorkout) -> NSPredicate } extension HKQuery {     class func predicateForSamplesWithStartDate(_ startDate: NSDate?, endDate endDate: NSDate?, options options: HKQueryOptions) -> NSPredicate } extension HKQuery {     class func predicateForQuantitySamplesWithOperatorType(_ operatorType: NSPredicateOperatorType, quantity quantity: HKQuantity) -> NSPredicate } extension HKQuery {     class func predicateForCategorySamplesWithOperatorType(_ operatorType: NSPredicateOperatorType, value value: Int) -> NSPredicate } extension HKQuery {     class func predicateForWorkoutsWithWorkoutActivityType(_ workoutActivityType: HKWorkoutActivityType) -> NSPredicate     class func predicateForWorkoutsWithOperatorType(_ operatorType: NSPredicateOperatorType, duration duration: NSTimeInterval) -> NSPredicate     class func predicateForWorkoutsWithOperatorType(_ operatorType: NSPredicateOperatorType, totalEnergyBurned totalEnergyBurned: HKQuantity) -> NSPredicate     class func predicateForWorkoutsWithOperatorType(_ operatorType: NSPredicateOperatorType, totalDistance totalDistance: HKQuantity) -> NSPredicate } extension HKQuery {     class func predicateForActivitySummaryWithDateComponents(_ dateComponents: NSDateComponents) -> NSPredicate     class func predicateForActivitySummariesBetweenStartDateComponents(_ startDateComponents: NSDateComponents, endDateComponents endDateComponents: NSDateComponents) -> NSPredicate } ``` | -- |
| To | ``` class HKQuery : NSObject {     var objectType: HKObjectType? { get }     var sampleType: HKSampleType? { get }     var predicate: NSPredicate? { get }     init()     class func predicateForActivitySummary(with dateComponents: DateComponents) -> NSPredicate     class func predicate(forActivitySummariesBetweenStart startDateComponents: DateComponents, end endDateComponents: DateComponents) -> NSPredicate     class func predicateForWorkouts(with workoutActivityType: HKWorkoutActivityType) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, duration duration: TimeInterval) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalEnergyBurned totalEnergyBurned: HKQuantity) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalDistance totalDistance: HKQuantity) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalSwimmingStrokeCount totalSwimmingStrokeCount: HKQuantity) -> NSPredicate     class func predicateForCategorySamples(with operatorType: NSComparisonPredicate.Operator, value value: Int) -> NSPredicate     class func predicateForQuantitySamples(with operatorType: NSComparisonPredicate.Operator, quantity quantity: HKQuantity) -> NSPredicate     class func predicateForSamples(withStart startDate: Date?, end endDate: Date?, options options: HKQueryOptions = []) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String, allowedValues allowedValues: [Any]) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String, operatorType operatorType: NSComparisonPredicate.Operator, value value: Any) -> NSPredicate     class func predicateForObjects(from source: HKSource) -> NSPredicate     class func predicateForObjects(from sources: Set<HKSource>) -> NSPredicate     class func predicateForObjects(from sourceRevisions: Set<HKSourceRevision>) -> NSPredicate     class func predicateForObjects(from devices: Set<HKDevice>) -> NSPredicate     class func predicateForObjects(withDeviceProperty key: String, allowedValues allowedValues: Set<String>) -> NSPredicate     class func predicateForObject(with UUID: UUID) -> NSPredicate     class func predicateForObjects(with UUIDs: Set<UUID>) -> NSPredicate     class func predicateForObjectsWithNoCorrelation() -> NSPredicate     class func predicateForObjects(from workout: HKWorkout) -> NSPredicate     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HKQuery : CVarArg { } extension HKQuery : Equatable, Hashable {     var hashValue: Int { get } } extension HKQuery {     class func predicateForObjects(withMetadataKey key: String) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String, allowedValues allowedValues: [Any]) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String, operatorType operatorType: NSComparisonPredicate.Operator, value value: Any) -> NSPredicate     class func predicateForObjects(from source: HKSource) -> NSPredicate     class func predicateForObjects(from sources: Set<HKSource>) -> NSPredicate     class func predicateForObjects(from sourceRevisions: Set<HKSourceRevision>) -> NSPredicate     class func predicateForObjects(from devices: Set<HKDevice>) -> NSPredicate     class func predicateForObjects(withDeviceProperty key: String, allowedValues allowedValues: Set<String>) -> NSPredicate     class func predicateForObject(with UUID: UUID) -> NSPredicate     class func predicateForObjects(with UUIDs: Set<UUID>) -> NSPredicate     class func predicateForObjectsWithNoCorrelation() -> NSPredicate     class func predicateForObjects(from workout: HKWorkout) -> NSPredicate } extension HKQuery {     class func predicateForSamples(withStart startDate: Date?, end endDate: Date?, options options: HKQueryOptions = []) -> NSPredicate } extension HKQuery {     class func predicateForQuantitySamples(with operatorType: NSComparisonPredicate.Operator, quantity quantity: HKQuantity) -> NSPredicate } extension HKQuery {     class func predicateForCategorySamples(with operatorType: NSComparisonPredicate.Operator, value value: Int) -> NSPredicate } extension HKQuery {     class func predicateForWorkouts(with workoutActivityType: HKWorkoutActivityType) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, duration duration: TimeInterval) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalEnergyBurned totalEnergyBurned: HKQuantity) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalDistance totalDistance: HKQuantity) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalSwimmingStrokeCount totalSwimmingStrokeCount: HKQuantity) -> NSPredicate } extension HKQuery {     class func predicateForActivitySummary(with dateComponents: DateComponents) -> NSPredicate     class func predicate(forActivitySummariesBetweenStart startDateComponents: DateComponents, end endDateComponents: DateComponents) -> NSPredicate } ``` | CVarArg, Equatable, Hashable |

Modified [HKQuery.predicate(forActivitySummariesBetweenStart: DateComponents, end: DateComponents) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614777-predicate)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForActivitySummariesBetweenStartDateComponents(_ startDateComponents: NSDateComponents, endDateComponents endDateComponents: NSDateComponents) -> NSPredicate ``` |
| To | ``` class func predicate(forActivitySummariesBetweenStart startDateComponents: DateComponents, end endDateComponents: DateComponents) -> NSPredicate ``` |

Modified [HKQuery.predicateForActivitySummary(with: DateComponents) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614790-predicateforactivitysummarywithd)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForActivitySummaryWithDateComponents(_ dateComponents: NSDateComponents) -> NSPredicate ``` |
| To | ``` class func predicateForActivitySummary(with dateComponents: DateComponents) -> NSPredicate ``` |

Modified [HKQuery.predicateForCategorySamples(with: NSComparisonPredicate.Operator, value: Int) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614781-predicateforcategorysampleswitho)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForCategorySamplesWithOperatorType(_ operatorType: NSPredicateOperatorType, value value: Int) -> NSPredicate ``` |
| To | ``` class func predicateForCategorySamples(with operatorType: NSComparisonPredicate.Operator, value value: Int) -> NSPredicate ``` |

Modified [HKQuery.predicateForObject(with: UUID) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614783-predicateforobject)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForObjectWithUUID(_ UUID: NSUUID) -> NSPredicate ``` |
| To | ``` class func predicateForObject(with UUID: UUID) -> NSPredicate ``` |

Modified [HKQuery.predicateForObjects(from: HKSource) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614769-predicateforobjectsfromsource)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForObjectsFromSource(_ source: HKSource) -> NSPredicate ``` |
| To | ``` class func predicateForObjects(from source: HKSource) -> NSPredicate ``` |

Modified [HKQuery.predicateForObjects(from: Set<HKDevice>) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614765-predicateforobjects)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForObjectsFromDevices(_ devices: Set<HKDevice>) -> NSPredicate ``` |
| To | ``` class func predicateForObjects(from devices: Set<HKDevice>) -> NSPredicate ``` |

Modified [HKQuery.predicateForObjects(from: Set<HKSourceRevision>) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614791-predicateforobjects)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForObjectsFromSourceRevisions(_ sourceRevisions: Set<HKSourceRevision>) -> NSPredicate ``` |
| To | ``` class func predicateForObjects(from sourceRevisions: Set<HKSourceRevision>) -> NSPredicate ``` |

Modified [HKQuery.predicateForObjects(from: Set<HKSource>) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614767-predicateforobjects)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForObjectsFromSources(_ sources: Set<HKSource>) -> NSPredicate ``` |
| To | ``` class func predicateForObjects(from sources: Set<HKSource>) -> NSPredicate ``` |

Modified [HKQuery.predicateForObjects(from: HKWorkout) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614773-predicateforobjects)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForObjectsFromWorkout(_ workout: HKWorkout) -> NSPredicate ``` |
| To | ``` class func predicateForObjects(from workout: HKWorkout) -> NSPredicate ``` |

Modified [HKQuery.predicateForObjects(with: Set<UUID>) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614785-predicateforobjects)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForObjectsWithUUIDs(_ UUIDs: Set<NSUUID>) -> NSPredicate ``` |
| To | ``` class func predicateForObjects(with UUIDs: Set<UUID>) -> NSPredicate ``` |

Modified [HKQuery.predicateForObjects(withDeviceProperty: String, allowedValues: Set<String>) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614775-predicateforobjects)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForObjectsWithDeviceProperty(_ key: String, allowedValues allowedValues: Set<String>) -> NSPredicate ``` |
| To | ``` class func predicateForObjects(withDeviceProperty key: String, allowedValues allowedValues: Set<String>) -> NSPredicate ``` |

Modified [HKQuery.predicateForObjects(withMetadataKey: String) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614782-predicateforobjects)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForObjectsWithMetadataKey(_ key: String) -> NSPredicate ``` |
| To | ``` class func predicateForObjects(withMetadataKey key: String) -> NSPredicate ``` |

Modified [HKQuery.predicateForObjects(withMetadataKey: String, allowedValues: [Any]) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614780-predicateforobjects)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForObjectsWithMetadataKey(_ key: String, allowedValues allowedValues: [AnyObject]) -> NSPredicate ``` |
| To | ``` class func predicateForObjects(withMetadataKey key: String, allowedValues allowedValues: [Any]) -> NSPredicate ``` |

Modified [HKQuery.predicateForObjects(withMetadataKey: String, operatorType: NSComparisonPredicate.Operator, value: Any) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614764-predicateforobjectswithmetadatak)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForObjectsWithMetadataKey(_ key: String, operatorType operatorType: NSPredicateOperatorType, value value: AnyObject) -> NSPredicate ``` |
| To | ``` class func predicateForObjects(withMetadataKey key: String, operatorType operatorType: NSComparisonPredicate.Operator, value value: Any) -> NSPredicate ``` |

Modified [HKQuery.predicateForQuantitySamples(with: NSComparisonPredicate.Operator, quantity: HKQuantity) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614761-predicateforquantitysamples)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForQuantitySamplesWithOperatorType(_ operatorType: NSPredicateOperatorType, quantity quantity: HKQuantity) -> NSPredicate ``` |
| To | ``` class func predicateForQuantitySamples(with operatorType: NSComparisonPredicate.Operator, quantity quantity: HKQuantity) -> NSPredicate ``` |

Modified [HKQuery.predicateForSamples(withStart: Date?, end: Date?, options: HKQueryOptions) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614771-predicateforsampleswithstartdate)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForSamplesWithStartDate(_ startDate: NSDate?, endDate endDate: NSDate?, options options: HKQueryOptions) -> NSPredicate ``` |
| To | ``` class func predicateForSamples(withStart startDate: Date?, end endDate: Date?, options options: HKQueryOptions = []) -> NSPredicate ``` |

Modified [HKQuery.predicateForWorkouts(with: HKWorkoutActivityType) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614787-predicateforworkoutswithworkouta)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForWorkoutsWithWorkoutActivityType(_ workoutActivityType: HKWorkoutActivityType) -> NSPredicate ``` |
| To | ``` class func predicateForWorkouts(with workoutActivityType: HKWorkoutActivityType) -> NSPredicate ``` |

Modified [HKQuery.predicateForWorkouts(with: NSComparisonPredicate.Operator, duration: TimeInterval) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614772-predicateforworkouts)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForWorkoutsWithOperatorType(_ operatorType: NSPredicateOperatorType, duration duration: NSTimeInterval) -> NSPredicate ``` |
| To | ``` class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, duration duration: TimeInterval) -> NSPredicate ``` |

Modified [HKQuery.predicateForWorkouts(with: NSComparisonPredicate.Operator, totalDistance: HKQuantity) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614779-predicateforworkoutswithoperator)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForWorkoutsWithOperatorType(_ operatorType: NSPredicateOperatorType, totalDistance totalDistance: HKQuantity) -> NSPredicate ``` |
| To | ``` class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalDistance totalDistance: HKQuantity) -> NSPredicate ``` |

Modified [HKQuery.predicateForWorkouts(with: NSComparisonPredicate.Operator, totalEnergyBurned: HKQuantity) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614788-predicateforworkouts)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForWorkoutsWithOperatorType(_ operatorType: NSPredicateOperatorType, totalEnergyBurned totalEnergyBurned: HKQuantity) -> NSPredicate ``` |
| To | ``` class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalEnergyBurned totalEnergyBurned: HKQuantity) -> NSPredicate ``` |

Modified [HKQueryAnchor](https://developer.apple.com/documentation/healthkit/hkqueryanchor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKQueryAnchor : NSObject, NSSecureCoding, NSCopying {     convenience init(fromValue value: Int)     class func anchorFromValue(_ value: Int) -> Self     init() } ``` | NSCopying, NSSecureCoding |
| To | ``` class HKQueryAnchor : NSObject, NSSecureCoding, NSCopying {     convenience init(fromValue value: Int)     class func fromValue(_ value: Int) -> Self     init()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HKQueryAnchor : CVarArg { } extension HKQueryAnchor : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [HKQueryOptions [struct]](https://developer.apple.com/documentation/healthkit/hkqueryoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct HKQueryOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var None: HKQueryOptions { get }     static var StrictStartDate: HKQueryOptions { get }     static var StrictEndDate: HKQueryOptions { get } } ``` | OptionSetType |
| To | ``` struct HKQueryOptions : OptionSet {     init(rawValue rawValue: UInt)     static var none: HKQueryOptions { get }     static var strictStartDate: HKQueryOptions { get }     static var strictEndDate: HKQueryOptions { get }     func intersect(_ other: HKQueryOptions) -> HKQueryOptions     func exclusiveOr(_ other: HKQueryOptions) -> HKQueryOptions     mutating func unionInPlace(_ other: HKQueryOptions)     mutating func intersectInPlace(_ other: HKQueryOptions)     mutating func exclusiveOrInPlace(_ other: HKQueryOptions)     func isSubsetOf(_ other: HKQueryOptions) -> Bool     func isDisjointWith(_ other: HKQueryOptions) -> Bool     func isSupersetOf(_ other: HKQueryOptions) -> Bool     mutating func subtractInPlace(_ other: HKQueryOptions)     func isStrictSupersetOf(_ other: HKQueryOptions) -> Bool     func isStrictSubsetOf(_ other: HKQueryOptions) -> Bool } extension HKQueryOptions {     func union(_ other: HKQueryOptions) -> HKQueryOptions     func intersection(_ other: HKQueryOptions) -> HKQueryOptions     func symmetricDifference(_ other: HKQueryOptions) -> HKQueryOptions } extension HKQueryOptions {     func contains(_ member: HKQueryOptions) -> Bool     mutating func insert(_ newMember: HKQueryOptions) -> (inserted: Bool, memberAfterInsert: HKQueryOptions)     mutating func remove(_ member: HKQueryOptions) -> HKQueryOptions?     mutating func update(with newMember: HKQueryOptions) -> HKQueryOptions? } extension HKQueryOptions {     convenience init()     mutating func formUnion(_ other: HKQueryOptions)     mutating func formIntersection(_ other: HKQueryOptions)     mutating func formSymmetricDifference(_ other: HKQueryOptions) } extension HKQueryOptions {     convenience init<S : Sequence where S.Iterator.Element == HKQueryOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: HKQueryOptions...)     mutating func subtract(_ other: HKQueryOptions)     func isSubset(of other: HKQueryOptions) -> Bool     func isSuperset(of other: HKQueryOptions) -> Bool     func isDisjoint(with other: HKQueryOptions) -> Bool     func subtracting(_ other: HKQueryOptions) -> HKQueryOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: HKQueryOptions) -> Bool     func isStrictSubset(of other: HKQueryOptions) -> Bool } ``` | OptionSet |

Modified [HKQueryOptions.strictEndDate](https://developer.apple.com/documentation/healthkit/hkqueryoptions/hkqueryoptionstrictenddate)

|  | Declaration |
| --- | --- |
| From | ``` static var StrictEndDate: HKQueryOptions { get } ``` |
| To | ``` static var strictEndDate: HKQueryOptions { get } ``` |

Modified [HKQueryOptions.strictStartDate](https://developer.apple.com/documentation/healthkit/hkqueryoptions/hkqueryoptionstrictstartdate)

|  | Declaration |
| --- | --- |
| From | ``` static var StrictStartDate: HKQueryOptions { get } ``` |
| To | ``` static var strictStartDate: HKQueryOptions { get } ``` |

Modified [HKSample](https://developer.apple.com/documentation/healthkit/hksample)

|  | Declaration |
| --- | --- |
| From | ``` class HKSample : HKObject {     var sampleType: HKSampleType { get }     var startDate: NSDate { get }     var endDate: NSDate { get } } ``` |
| To | ``` class HKSample : HKObject {     var sampleType: HKSampleType { get }     var startDate: Date { get }     var endDate: Date { get } } ``` |

Modified [HKSample.endDate](https://developer.apple.com/documentation/healthkit/hksample/1615170-enddate)

|  | Declaration |
| --- | --- |
| From | ``` var endDate: NSDate { get } ``` |
| To | ``` var endDate: Date { get } ``` |

Modified [HKSample.startDate](https://developer.apple.com/documentation/healthkit/hksample/1615481-startdate)

|  | Declaration |
| --- | --- |
| From | ``` var startDate: NSDate { get } ``` |
| To | ``` var startDate: Date { get } ``` |

Modified [HKSampleQuery](https://developer.apple.com/documentation/healthkit/hksamplequery)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKSampleQuery : HKQuery {     var limit: Int { get }     var sortDescriptors: [NSSortDescriptor]? { get }     init(sampleType sampleType: HKSampleType, predicate predicate: NSPredicate?, limit limit: Int, sortDescriptors sortDescriptors: [NSSortDescriptor]?, resultsHandler resultsHandler: (HKSampleQuery, [HKSample]?, NSError?) -> Void) } ``` | -- |
| To | ``` class HKSampleQuery : HKQuery {     var limit: Int { get }     var sortDescriptors: [NSSortDescriptor]? { get }     init(sampleType sampleType: HKSampleType, predicate predicate: NSPredicate?, limit limit: Int, sortDescriptors sortDescriptors: [NSSortDescriptor]?, resultsHandler resultsHandler: @escaping (HKSampleQuery, [HKSample]?, Error?) -> Swift.Void)     class func predicateForActivitySummary(with dateComponents: DateComponents) -> NSPredicate     class func predicate(forActivitySummariesBetweenStart startDateComponents: DateComponents, end endDateComponents: DateComponents) -> NSPredicate     class func predicateForWorkouts(with workoutActivityType: HKWorkoutActivityType) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, duration duration: TimeInterval) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalEnergyBurned totalEnergyBurned: HKQuantity) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalDistance totalDistance: HKQuantity) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalSwimmingStrokeCount totalSwimmingStrokeCount: HKQuantity) -> NSPredicate     class func predicateForCategorySamples(with operatorType: NSComparisonPredicate.Operator, value value: Int) -> NSPredicate     class func predicateForQuantitySamples(with operatorType: NSComparisonPredicate.Operator, quantity quantity: HKQuantity) -> NSPredicate     class func predicateForSamples(withStart startDate: Date?, end endDate: Date?, options options: HKQueryOptions = []) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String, allowedValues allowedValues: [Any]) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String, operatorType operatorType: NSComparisonPredicate.Operator, value value: Any) -> NSPredicate     class func predicateForObjects(from source: HKSource) -> NSPredicate     class func predicateForObjects(from sources: Set<HKSource>) -> NSPredicate     class func predicateForObjects(from sourceRevisions: Set<HKSourceRevision>) -> NSPredicate     class func predicateForObjects(from devices: Set<HKDevice>) -> NSPredicate     class func predicateForObjects(withDeviceProperty key: String, allowedValues allowedValues: Set<String>) -> NSPredicate     class func predicateForObject(with UUID: UUID) -> NSPredicate     class func predicateForObjects(with UUIDs: Set<UUID>) -> NSPredicate     class func predicateForObjectsWithNoCorrelation() -> NSPredicate     class func predicateForObjects(from workout: HKWorkout) -> NSPredicate     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HKSampleQuery : CVarArg { } extension HKSampleQuery : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [HKSampleQuery.init(sampleType: HKSampleType, predicate: NSPredicate?, limit: Int, sortDescriptors: [NSSortDescriptor]?, resultsHandler: (HKSampleQuery, [HKSample]?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/healthkit/hksamplequery/1615055-initwithsampletype)

|  | Declaration |
| --- | --- |
| From | ``` init(sampleType sampleType: HKSampleType, predicate predicate: NSPredicate?, limit limit: Int, sortDescriptors sortDescriptors: [NSSortDescriptor]?, resultsHandler resultsHandler: (HKSampleQuery, [HKSample]?, NSError?) -> Void) ``` |
| To | ``` init(sampleType sampleType: HKSampleType, predicate predicate: NSPredicate?, limit limit: Int, sortDescriptors sortDescriptors: [NSSortDescriptor]?, resultsHandler resultsHandler: @escaping (HKSampleQuery, [HKSample]?, Error?) -> Swift.Void) ``` |

Modified [HKSource](https://developer.apple.com/documentation/healthkit/hksource)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKSource : NSObject, NSSecureCoding, NSCopying {     var name: String { get }     var bundleIdentifier: String { get }     class func defaultSource() -> HKSource     init() } ``` | NSCopying, NSSecureCoding |
| To | ``` class HKSource : NSObject, NSSecureCoding, NSCopying {     var name: String { get }     var bundleIdentifier: String { get }     class func `default`() -> HKSource     init()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HKSource : CVarArg { } extension HKSource : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [HKSource.default() [class]](https://developer.apple.com/documentation/healthkit/hksource/1615046-defaultsource)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultSource() -> HKSource ``` |
| To | ``` class func `default`() -> HKSource ``` |

Modified [HKSourceQuery](https://developer.apple.com/documentation/healthkit/hksourcequery)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKSourceQuery : HKQuery {     init(sampleType sampleType: HKSampleType, samplePredicate objectPredicate: NSPredicate?, completionHandler completionHandler: (HKSourceQuery, Set<HKSource>?, NSError?) -> Void) } ``` | -- |
| To | ``` class HKSourceQuery : HKQuery {     init(sampleType sampleType: HKSampleType, samplePredicate objectPredicate: NSPredicate?, completionHandler completionHandler: @escaping (HKSourceQuery, Set<HKSource>?, Error?) -> Swift.Void)     class func predicateForActivitySummary(with dateComponents: DateComponents) -> NSPredicate     class func predicate(forActivitySummariesBetweenStart startDateComponents: DateComponents, end endDateComponents: DateComponents) -> NSPredicate     class func predicateForWorkouts(with workoutActivityType: HKWorkoutActivityType) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, duration duration: TimeInterval) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalEnergyBurned totalEnergyBurned: HKQuantity) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalDistance totalDistance: HKQuantity) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalSwimmingStrokeCount totalSwimmingStrokeCount: HKQuantity) -> NSPredicate     class func predicateForCategorySamples(with operatorType: NSComparisonPredicate.Operator, value value: Int) -> NSPredicate     class func predicateForQuantitySamples(with operatorType: NSComparisonPredicate.Operator, quantity quantity: HKQuantity) -> NSPredicate     class func predicateForSamples(withStart startDate: Date?, end endDate: Date?, options options: HKQueryOptions = []) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String, allowedValues allowedValues: [Any]) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String, operatorType operatorType: NSComparisonPredicate.Operator, value value: Any) -> NSPredicate     class func predicateForObjects(from source: HKSource) -> NSPredicate     class func predicateForObjects(from sources: Set<HKSource>) -> NSPredicate     class func predicateForObjects(from sourceRevisions: Set<HKSourceRevision>) -> NSPredicate     class func predicateForObjects(from devices: Set<HKDevice>) -> NSPredicate     class func predicateForObjects(withDeviceProperty key: String, allowedValues allowedValues: Set<String>) -> NSPredicate     class func predicateForObject(with UUID: UUID) -> NSPredicate     class func predicateForObjects(with UUIDs: Set<UUID>) -> NSPredicate     class func predicateForObjectsWithNoCorrelation() -> NSPredicate     class func predicateForObjects(from workout: HKWorkout) -> NSPredicate     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HKSourceQuery : CVarArg { } extension HKSourceQuery : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [HKSourceQuery.init(sampleType: HKSampleType, samplePredicate: NSPredicate?, completionHandler: (HKSourceQuery, Set<HKSource>?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/healthkit/hksourcequery/1614367-init)

|  | Declaration |
| --- | --- |
| From | ``` init(sampleType sampleType: HKSampleType, samplePredicate objectPredicate: NSPredicate?, completionHandler completionHandler: (HKSourceQuery, Set<HKSource>?, NSError?) -> Void) ``` |
| To | ``` init(sampleType sampleType: HKSampleType, samplePredicate objectPredicate: NSPredicate?, completionHandler completionHandler: @escaping (HKSourceQuery, Set<HKSource>?, Error?) -> Swift.Void) ``` |

Modified [HKSourceRevision](https://developer.apple.com/documentation/healthkit/hksourcerevision)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKSourceRevision : NSObject, NSSecureCoding, NSCopying {     var source: HKSource { get }     var version: String? { get }     init(source source: HKSource, version version: String)     init() } ``` | NSCopying, NSSecureCoding |
| To | ``` class HKSourceRevision : NSObject, NSSecureCoding, NSCopying {     var source: HKSource { get }     var version: String? { get }     init(source source: HKSource, version version: String?)     init()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HKSourceRevision : CVarArg { } extension HKSourceRevision : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [HKSourceRevision.init(source: HKSource, version: String?)](https://developer.apple.com/documentation/healthkit/hksourcerevision/1614799-init)

|  | Declaration |
| --- | --- |
| From | ``` init(source source: HKSource, version version: String) ``` |
| To | ``` init(source source: HKSource, version version: String?) ``` |

Modified [HKStatistics](https://developer.apple.com/documentation/healthkit/hkstatistics)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKStatistics : NSObject, NSSecureCoding, NSCopying {     var quantityType: HKQuantityType { get }     var startDate: NSDate { get }     var endDate: NSDate { get }     var sources: [HKSource]? { get }     init()     func averageQuantityForSource(_ source: HKSource) -> HKQuantity?     func averageQuantity() -> HKQuantity?     func minimumQuantityForSource(_ source: HKSource) -> HKQuantity?     func minimumQuantity() -> HKQuantity?     func maximumQuantityForSource(_ source: HKSource) -> HKQuantity?     func maximumQuantity() -> HKQuantity?     func sumQuantityForSource(_ source: HKSource) -> HKQuantity?     func sumQuantity() -> HKQuantity? } ``` | NSCopying, NSSecureCoding |
| To | ``` class HKStatistics : NSObject, NSSecureCoding, NSCopying {     var quantityType: HKQuantityType { get }     var startDate: Date { get }     var endDate: Date { get }     var sources: [HKSource]? { get }     init()     func averageQuantity(for source: HKSource) -> HKQuantity?     func averageQuantity() -> HKQuantity?     func minimumQuantity(for source: HKSource) -> HKQuantity?     func minimumQuantity() -> HKQuantity?     func maximumQuantity(for source: HKSource) -> HKQuantity?     func maximumQuantity() -> HKQuantity?     func sumQuantity(for source: HKSource) -> HKQuantity?     func sumQuantity() -> HKQuantity?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HKStatistics : CVarArg { } extension HKStatistics : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [HKStatistics.averageQuantity(for: HKSource) -> HKQuantity?](https://developer.apple.com/documentation/healthkit/hkstatistics/1615307-averagequantity)

|  | Declaration |
| --- | --- |
| From | ``` func averageQuantityForSource(_ source: HKSource) -> HKQuantity? ``` |
| To | ``` func averageQuantity(for source: HKSource) -> HKQuantity? ``` |

Modified [HKStatistics.endDate](https://developer.apple.com/documentation/healthkit/hkstatistics/1615067-enddate)

|  | Declaration |
| --- | --- |
| From | ``` var endDate: NSDate { get } ``` |
| To | ``` var endDate: Date { get } ``` |

Modified [HKStatistics.maximumQuantity(for: HKSource) -> HKQuantity?](https://developer.apple.com/documentation/healthkit/hkstatistics/1615630-maximumquantityforsource)

|  | Declaration |
| --- | --- |
| From | ``` func maximumQuantityForSource(_ source: HKSource) -> HKQuantity? ``` |
| To | ``` func maximumQuantity(for source: HKSource) -> HKQuantity? ``` |

Modified [HKStatistics.minimumQuantity(for: HKSource) -> HKQuantity?](https://developer.apple.com/documentation/healthkit/hkstatistics/1615065-minimumquantityforsource)

|  | Declaration |
| --- | --- |
| From | ``` func minimumQuantityForSource(_ source: HKSource) -> HKQuantity? ``` |
| To | ``` func minimumQuantity(for source: HKSource) -> HKQuantity? ``` |

Modified [HKStatistics.startDate](https://developer.apple.com/documentation/healthkit/hkstatistics/1615351-startdate)

|  | Declaration |
| --- | --- |
| From | ``` var startDate: NSDate { get } ``` |
| To | ``` var startDate: Date { get } ``` |

Modified [HKStatistics.sumQuantity(for: HKSource) -> HKQuantity?](https://developer.apple.com/documentation/healthkit/hkstatistics/1615502-sumquantityforsource)

|  | Declaration |
| --- | --- |
| From | ``` func sumQuantityForSource(_ source: HKSource) -> HKQuantity? ``` |
| To | ``` func sumQuantity(for source: HKSource) -> HKQuantity? ``` |

Modified [HKStatisticsCollection](https://developer.apple.com/documentation/healthkit/hkstatisticscollection)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKStatisticsCollection : NSObject {     init()     func statisticsForDate(_ date: NSDate) -> HKStatistics?     func enumerateStatisticsFromDate(_ startDate: NSDate, toDate endDate: NSDate, withBlock block: (HKStatistics, UnsafeMutablePointer<ObjCBool>) -> Void)     func statistics() -> [HKStatistics]     func sources() -> Set<HKSource> } ``` | -- |
| To | ``` class HKStatisticsCollection : NSObject {     init()     func statistics(for date: Date) -> HKStatistics?     func enumerateStatistics(from startDate: Date, to endDate: Date, with block: @escaping (HKStatistics, UnsafeMutablePointer<ObjCBool>) -> Swift.Void)     func statistics() -> [HKStatistics]     func sources() -> Set<HKSource>     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HKStatisticsCollection : CVarArg { } extension HKStatisticsCollection : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [HKStatisticsCollection.enumerateStatistics(from: Date, to: Date, with: (HKStatistics, UnsafeMutablePointer<ObjCBool>) -> Swift.Void)](https://developer.apple.com/documentation/healthkit/hkstatisticscollection/1615783-enumeratestatisticsfromdate)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateStatisticsFromDate(_ startDate: NSDate, toDate endDate: NSDate, withBlock block: (HKStatistics, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateStatistics(from startDate: Date, to endDate: Date, with block: @escaping (HKStatistics, UnsafeMutablePointer<ObjCBool>) -> Swift.Void) ``` |

Modified [HKStatisticsCollection.statistics(for: Date) -> HKStatistics?](https://developer.apple.com/documentation/healthkit/hkstatisticscollection/1615300-statistics)

|  | Declaration |
| --- | --- |
| From | ``` func statisticsForDate(_ date: NSDate) -> HKStatistics? ``` |
| To | ``` func statistics(for date: Date) -> HKStatistics? ``` |

Modified [HKStatisticsCollectionQuery](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquery)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKStatisticsCollectionQuery : HKQuery {     var anchorDate: NSDate { get }     var options: HKStatisticsOptions { get }     @NSCopying var intervalComponents: NSDateComponents { get }     var initialResultsHandler: ((HKStatisticsCollectionQuery, HKStatisticsCollection?, NSError?) -> Void)?     var statisticsUpdateHandler: ((HKStatisticsCollectionQuery, HKStatistics?, HKStatisticsCollection?, NSError?) -> Void)?     init(quantityType quantityType: HKQuantityType, quantitySamplePredicate quantitySamplePredicate: NSPredicate?, options options: HKStatisticsOptions, anchorDate anchorDate: NSDate, intervalComponents intervalComponents: NSDateComponents) } ``` | -- |
| To | ``` class HKStatisticsCollectionQuery : HKQuery {     var anchorDate: Date { get }     var options: HKStatisticsOptions { get }     var intervalComponents: DateComponents { get }     var initialResultsHandler: ((HKStatisticsCollectionQuery, HKStatisticsCollection?, Error?) -> Swift.Void)?     var statisticsUpdateHandler: ((HKStatisticsCollectionQuery, HKStatistics?, HKStatisticsCollection?, Error?) -> Swift.Void)?     init(quantityType quantityType: HKQuantityType, quantitySamplePredicate quantitySamplePredicate: NSPredicate?, options options: HKStatisticsOptions = [], anchorDate anchorDate: Date, intervalComponents intervalComponents: DateComponents)     class func predicateForActivitySummary(with dateComponents: DateComponents) -> NSPredicate     class func predicate(forActivitySummariesBetweenStart startDateComponents: DateComponents, end endDateComponents: DateComponents) -> NSPredicate     class func predicateForWorkouts(with workoutActivityType: HKWorkoutActivityType) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, duration duration: TimeInterval) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalEnergyBurned totalEnergyBurned: HKQuantity) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalDistance totalDistance: HKQuantity) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalSwimmingStrokeCount totalSwimmingStrokeCount: HKQuantity) -> NSPredicate     class func predicateForCategorySamples(with operatorType: NSComparisonPredicate.Operator, value value: Int) -> NSPredicate     class func predicateForQuantitySamples(with operatorType: NSComparisonPredicate.Operator, quantity quantity: HKQuantity) -> NSPredicate     class func predicateForSamples(withStart startDate: Date?, end endDate: Date?, options options: HKQueryOptions = []) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String, allowedValues allowedValues: [Any]) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String, operatorType operatorType: NSComparisonPredicate.Operator, value value: Any) -> NSPredicate     class func predicateForObjects(from source: HKSource) -> NSPredicate     class func predicateForObjects(from sources: Set<HKSource>) -> NSPredicate     class func predicateForObjects(from sourceRevisions: Set<HKSourceRevision>) -> NSPredicate     class func predicateForObjects(from devices: Set<HKDevice>) -> NSPredicate     class func predicateForObjects(withDeviceProperty key: String, allowedValues allowedValues: Set<String>) -> NSPredicate     class func predicateForObject(with UUID: UUID) -> NSPredicate     class func predicateForObjects(with UUIDs: Set<UUID>) -> NSPredicate     class func predicateForObjectsWithNoCorrelation() -> NSPredicate     class func predicateForObjects(from workout: HKWorkout) -> NSPredicate     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HKStatisticsCollectionQuery : CVarArg { } extension HKStatisticsCollectionQuery : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [HKStatisticsCollectionQuery.anchorDate](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquery/1615241-anchordate)

|  | Declaration |
| --- | --- |
| From | ``` var anchorDate: NSDate { get } ``` |
| To | ``` var anchorDate: Date { get } ``` |

Modified [HKStatisticsCollectionQuery.init(quantityType: HKQuantityType, quantitySamplePredicate: NSPredicate?, options: HKStatisticsOptions, anchorDate: Date, intervalComponents: DateComponents)](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquery/1615199-initwithquantitytype)

|  | Declaration |
| --- | --- |
| From | ``` init(quantityType quantityType: HKQuantityType, quantitySamplePredicate quantitySamplePredicate: NSPredicate?, options options: HKStatisticsOptions, anchorDate anchorDate: NSDate, intervalComponents intervalComponents: NSDateComponents) ``` |
| To | ``` init(quantityType quantityType: HKQuantityType, quantitySamplePredicate quantitySamplePredicate: NSPredicate?, options options: HKStatisticsOptions = [], anchorDate anchorDate: Date, intervalComponents intervalComponents: DateComponents) ``` |

Modified [HKStatisticsCollectionQuery.initialResultsHandler](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquery/1615755-initialresultshandler)

|  | Declaration |
| --- | --- |
| From | ``` var initialResultsHandler: ((HKStatisticsCollectionQuery, HKStatisticsCollection?, NSError?) -> Void)? ``` |
| To | ``` var initialResultsHandler: ((HKStatisticsCollectionQuery, HKStatisticsCollection?, Error?) -> Swift.Void)? ``` |

Modified [HKStatisticsCollectionQuery.intervalComponents](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquery/1615108-intervalcomponents)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var intervalComponents: NSDateComponents { get } ``` |
| To | ``` var intervalComponents: DateComponents { get } ``` |

Modified [HKStatisticsCollectionQuery.statisticsUpdateHandler](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquery/1615723-statisticsupdatehandler)

|  | Declaration |
| --- | --- |
| From | ``` var statisticsUpdateHandler: ((HKStatisticsCollectionQuery, HKStatistics?, HKStatisticsCollection?, NSError?) -> Void)? ``` |
| To | ``` var statisticsUpdateHandler: ((HKStatisticsCollectionQuery, HKStatistics?, HKStatisticsCollection?, Error?) -> Swift.Void)? ``` |

Modified [HKStatisticsOptions [struct]](https://developer.apple.com/documentation/healthkit/hkstatisticsoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct HKStatisticsOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var None: HKStatisticsOptions { get }     static var SeparateBySource: HKStatisticsOptions { get }     static var DiscreteAverage: HKStatisticsOptions { get }     static var DiscreteMin: HKStatisticsOptions { get }     static var DiscreteMax: HKStatisticsOptions { get }     static var CumulativeSum: HKStatisticsOptions { get } } ``` | OptionSetType |
| To | ``` struct HKStatisticsOptions : OptionSet {     init(rawValue rawValue: UInt)     static var none: HKStatisticsOptions { get }     static var separateBySource: HKStatisticsOptions { get }     static var discreteAverage: HKStatisticsOptions { get }     static var discreteMin: HKStatisticsOptions { get }     static var discreteMax: HKStatisticsOptions { get }     static var cumulativeSum: HKStatisticsOptions { get }     func intersect(_ other: HKStatisticsOptions) -> HKStatisticsOptions     func exclusiveOr(_ other: HKStatisticsOptions) -> HKStatisticsOptions     mutating func unionInPlace(_ other: HKStatisticsOptions)     mutating func intersectInPlace(_ other: HKStatisticsOptions)     mutating func exclusiveOrInPlace(_ other: HKStatisticsOptions)     func isSubsetOf(_ other: HKStatisticsOptions) -> Bool     func isDisjointWith(_ other: HKStatisticsOptions) -> Bool     func isSupersetOf(_ other: HKStatisticsOptions) -> Bool     mutating func subtractInPlace(_ other: HKStatisticsOptions)     func isStrictSupersetOf(_ other: HKStatisticsOptions) -> Bool     func isStrictSubsetOf(_ other: HKStatisticsOptions) -> Bool } extension HKStatisticsOptions {     func union(_ other: HKStatisticsOptions) -> HKStatisticsOptions     func intersection(_ other: HKStatisticsOptions) -> HKStatisticsOptions     func symmetricDifference(_ other: HKStatisticsOptions) -> HKStatisticsOptions } extension HKStatisticsOptions {     func contains(_ member: HKStatisticsOptions) -> Bool     mutating func insert(_ newMember: HKStatisticsOptions) -> (inserted: Bool, memberAfterInsert: HKStatisticsOptions)     mutating func remove(_ member: HKStatisticsOptions) -> HKStatisticsOptions?     mutating func update(with newMember: HKStatisticsOptions) -> HKStatisticsOptions? } extension HKStatisticsOptions {     convenience init()     mutating func formUnion(_ other: HKStatisticsOptions)     mutating func formIntersection(_ other: HKStatisticsOptions)     mutating func formSymmetricDifference(_ other: HKStatisticsOptions) } extension HKStatisticsOptions {     convenience init<S : Sequence where S.Iterator.Element == HKStatisticsOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: HKStatisticsOptions...)     mutating func subtract(_ other: HKStatisticsOptions)     func isSubset(of other: HKStatisticsOptions) -> Bool     func isSuperset(of other: HKStatisticsOptions) -> Bool     func isDisjoint(with other: HKStatisticsOptions) -> Bool     func subtracting(_ other: HKStatisticsOptions) -> HKStatisticsOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: HKStatisticsOptions) -> Bool     func isStrictSubset(of other: HKStatisticsOptions) -> Bool } ``` | OptionSet |

Modified [HKStatisticsOptions.cumulativeSum](https://developer.apple.com/documentation/healthkit/hkstatisticsoptions/1615784-cumulativesum)

|  | Declaration |
| --- | --- |
| From | ``` static var CumulativeSum: HKStatisticsOptions { get } ``` |
| To | ``` static var cumulativeSum: HKStatisticsOptions { get } ``` |

Modified [HKStatisticsOptions.discreteAverage](https://developer.apple.com/documentation/healthkit/hkstatisticsoptions/1615371-discreteaverage)

|  | Declaration |
| --- | --- |
| From | ``` static var DiscreteAverage: HKStatisticsOptions { get } ``` |
| To | ``` static var discreteAverage: HKStatisticsOptions { get } ``` |

Modified [HKStatisticsOptions.discreteMax](https://developer.apple.com/documentation/healthkit/hkstatisticsoptions/1615588-discretemax)

|  | Declaration |
| --- | --- |
| From | ``` static var DiscreteMax: HKStatisticsOptions { get } ``` |
| To | ``` static var discreteMax: HKStatisticsOptions { get } ``` |

Modified [HKStatisticsOptions.discreteMin](https://developer.apple.com/documentation/healthkit/hkstatisticsoptions/1615716-discretemin)

|  | Declaration |
| --- | --- |
| From | ``` static var DiscreteMin: HKStatisticsOptions { get } ``` |
| To | ``` static var discreteMin: HKStatisticsOptions { get } ``` |

Modified [HKStatisticsOptions.separateBySource](https://developer.apple.com/documentation/healthkit/hkstatisticsoptions/1615479-separatebysource)

|  | Declaration |
| --- | --- |
| From | ``` static var SeparateBySource: HKStatisticsOptions { get } ``` |
| To | ``` static var separateBySource: HKStatisticsOptions { get } ``` |

Modified [HKStatisticsQuery](https://developer.apple.com/documentation/healthkit/hkstatisticsquery)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKStatisticsQuery : HKQuery {     init(quantityType quantityType: HKQuantityType, quantitySamplePredicate quantitySamplePredicate: NSPredicate?, options options: HKStatisticsOptions, completionHandler handler: (HKStatisticsQuery, HKStatistics?, NSError?) -> Void) } ``` | -- |
| To | ``` class HKStatisticsQuery : HKQuery {     init(quantityType quantityType: HKQuantityType, quantitySamplePredicate quantitySamplePredicate: NSPredicate?, options options: HKStatisticsOptions = [], completionHandler handler: @escaping (HKStatisticsQuery, HKStatistics?, Error?) -> Swift.Void)     class func predicateForActivitySummary(with dateComponents: DateComponents) -> NSPredicate     class func predicate(forActivitySummariesBetweenStart startDateComponents: DateComponents, end endDateComponents: DateComponents) -> NSPredicate     class func predicateForWorkouts(with workoutActivityType: HKWorkoutActivityType) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, duration duration: TimeInterval) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalEnergyBurned totalEnergyBurned: HKQuantity) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalDistance totalDistance: HKQuantity) -> NSPredicate     class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalSwimmingStrokeCount totalSwimmingStrokeCount: HKQuantity) -> NSPredicate     class func predicateForCategorySamples(with operatorType: NSComparisonPredicate.Operator, value value: Int) -> NSPredicate     class func predicateForQuantitySamples(with operatorType: NSComparisonPredicate.Operator, quantity quantity: HKQuantity) -> NSPredicate     class func predicateForSamples(withStart startDate: Date?, end endDate: Date?, options options: HKQueryOptions = []) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String, allowedValues allowedValues: [Any]) -> NSPredicate     class func predicateForObjects(withMetadataKey key: String, operatorType operatorType: NSComparisonPredicate.Operator, value value: Any) -> NSPredicate     class func predicateForObjects(from source: HKSource) -> NSPredicate     class func predicateForObjects(from sources: Set<HKSource>) -> NSPredicate     class func predicateForObjects(from sourceRevisions: Set<HKSourceRevision>) -> NSPredicate     class func predicateForObjects(from devices: Set<HKDevice>) -> NSPredicate     class func predicateForObjects(withDeviceProperty key: String, allowedValues allowedValues: Set<String>) -> NSPredicate     class func predicateForObject(with UUID: UUID) -> NSPredicate     class func predicateForObjects(with UUIDs: Set<UUID>) -> NSPredicate     class func predicateForObjectsWithNoCorrelation() -> NSPredicate     class func predicateForObjects(from workout: HKWorkout) -> NSPredicate     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HKStatisticsQuery : CVarArg { } extension HKStatisticsQuery : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [HKStatisticsQuery.init(quantityType: HKQuantityType, quantitySamplePredicate: NSPredicate?, options: HKStatisticsOptions, completionHandler: (HKStatisticsQuery, HKStatistics?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/healthkit/hkstatisticsquery/1615536-init)

|  | Declaration |
| --- | --- |
| From | ``` init(quantityType quantityType: HKQuantityType, quantitySamplePredicate quantitySamplePredicate: NSPredicate?, options options: HKStatisticsOptions, completionHandler handler: (HKStatisticsQuery, HKStatistics?, NSError?) -> Void) ``` |
| To | ``` init(quantityType quantityType: HKQuantityType, quantitySamplePredicate quantitySamplePredicate: NSPredicate?, options options: HKStatisticsOptions = [], completionHandler handler: @escaping (HKStatisticsQuery, HKStatistics?, Error?) -> Swift.Void) ``` |

Modified [HKUnit](https://developer.apple.com/documentation/healthkit/hkunit)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKUnit : NSObject, NSSecureCoding, NSCopying {     var unitString: String { get }     init()     convenience init(fromString string: String)     class func unitFromString(_ string: String) -> Self     convenience init(fromMassFormatterUnit massFormatterUnit: NSMassFormatterUnit)     class func unitFromMassFormatterUnit(_ massFormatterUnit: NSMassFormatterUnit) -> Self     class func massFormatterUnitFromUnit(_ unit: HKUnit) -> NSMassFormatterUnit     convenience init(fromLengthFormatterUnit lengthFormatterUnit: NSLengthFormatterUnit)     class func unitFromLengthFormatterUnit(_ lengthFormatterUnit: NSLengthFormatterUnit) -> Self     class func lengthFormatterUnitFromUnit(_ unit: HKUnit) -> NSLengthFormatterUnit     convenience init(fromEnergyFormatterUnit energyFormatterUnit: NSEnergyFormatterUnit)     class func unitFromEnergyFormatterUnit(_ energyFormatterUnit: NSEnergyFormatterUnit) -> Self     class func energyFormatterUnitFromUnit(_ unit: HKUnit) -> NSEnergyFormatterUnit     func isNull() -> Bool } extension HKUnit {     class func gramUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func gramUnit() -> Self     class func ounceUnit() -> Self     class func poundUnit() -> Self     class func stoneUnit() -> Self     class func moleUnitWithMetricPrefix(_ prefix: HKMetricPrefix, molarMass gramsPerMole: Double) -> Self     class func moleUnitWithMolarMass(_ gramsPerMole: Double) -> Self } extension HKUnit {     class func meterUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func meterUnit() -> Self     class func inchUnit() -> Self     class func footUnit() -> Self     class func yardUnit() -> Self     class func mileUnit() -> Self } extension HKUnit {     class func literUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func literUnit() -> Self     class func fluidOunceUSUnit() -> Self     class func fluidOunceImperialUnit() -> Self     class func pintUSUnit() -> Self     class func pintImperialUnit() -> Self     class func cupUSUnit() -> Self     class func cupImperialUnit() -> Self } extension HKUnit {     class func pascalUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func pascalUnit() -> Self     class func millimeterOfMercuryUnit() -> Self     class func centimeterOfWaterUnit() -> Self     class func atmosphereUnit() -> Self } extension HKUnit {     class func secondUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func secondUnit() -> Self     class func minuteUnit() -> Self     class func hourUnit() -> Self     class func dayUnit() -> Self } extension HKUnit {     class func jouleUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func jouleUnit() -> Self     class func calorieUnit() -> Self     class func kilocalorieUnit() -> Self } extension HKUnit {     class func degreeCelsiusUnit() -> Self     class func degreeFahrenheitUnit() -> Self     class func kelvinUnit() -> Self } extension HKUnit {     class func siemenUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func siemenUnit() -> Self } extension HKUnit {     class func countUnit() -> Self     class func percentUnit() -> Self } extension HKUnit {     func unitMultipliedByUnit(_ unit: HKUnit) -> HKUnit     func unitDividedByUnit(_ unit: HKUnit) -> HKUnit     func unitRaisedToPower(_ power: Int) -> HKUnit     func reciprocalUnit() -> HKUnit } ``` | NSCopying, NSSecureCoding |
| To | ``` class HKUnit : NSObject, NSSecureCoding, NSCopying {     var unitString: String { get }     init()     convenience init(from string: String)     class func fromString(_ string: String) -> Self     convenience init(from massFormatterUnit: MassFormatter.Unit)     class func fromMassFormatterUnit(_ massFormatterUnit: MassFormatter.Unit) -> Self     class func massFormatterUnit(from unit: HKUnit) -> MassFormatter.Unit     convenience init(from lengthFormatterUnit: LengthFormatter.Unit)     class func fromLengthFormatterUnit(_ lengthFormatterUnit: LengthFormatter.Unit) -> Self     class func lengthFormatterUnit(from unit: HKUnit) -> LengthFormatter.Unit     convenience init(from energyFormatterUnit: EnergyFormatter.Unit)     class func fromEnergyFormatterUnit(_ energyFormatterUnit: EnergyFormatter.Unit) -> Self     class func energyFormatterUnit(from unit: HKUnit) -> EnergyFormatter.Unit     func isNull() -> Bool     func unitMultiplied(by unit: HKUnit) -> HKUnit     func unitDivided(by unit: HKUnit) -> HKUnit     func unitRaised(toPower power: Int) -> HKUnit     func reciprocal() -> HKUnit     class func count() -> Self     class func percent() -> Self     class func siemenUnit(with prefix: HKMetricPrefix) -> Self     class func siemen() -> Self     class func degreeCelsius() -> Self     class func degreeFahrenheit() -> Self     class func kelvin() -> Self     class func jouleUnit(with prefix: HKMetricPrefix) -> Self     class func joule() -> Self     class func calorie() -> Self     class func kilocalorie() -> Self     class func secondUnit(with prefix: HKMetricPrefix) -> Self     class func second() -> Self     class func minute() -> Self     class func hour() -> Self     class func day() -> Self     class func pascalUnit(with prefix: HKMetricPrefix) -> Self     class func pascal() -> Self     class func millimeterOfMercury() -> Self     class func centimeterOfWater() -> Self     class func atmosphere() -> Self     class func literUnit(with prefix: HKMetricPrefix) -> Self     class func liter() -> Self     class func fluidOunceUS() -> Self     class func fluidOunceImperial() -> Self     class func pintUS() -> Self     class func pintImperial() -> Self     class func cupUS() -> Self     class func cupImperial() -> Self     class func meterUnit(with prefix: HKMetricPrefix) -> Self     class func meter() -> Self     class func inch() -> Self     class func foot() -> Self     class func yard() -> Self     class func mile() -> Self     class func gramUnit(with prefix: HKMetricPrefix) -> Self     class func gram() -> Self     class func ounce() -> Self     class func pound() -> Self     class func stone() -> Self     class func moleUnit(with prefix: HKMetricPrefix, molarMass gramsPerMole: Double) -> Self     class func moleUnit(withMolarMass gramsPerMole: Double) -> Self     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HKUnit : CVarArg { } extension HKUnit : Equatable, Hashable {     var hashValue: Int { get } } extension HKUnit {     class func gramUnit(with prefix: HKMetricPrefix) -> Self     class func gram() -> Self     class func ounce() -> Self     class func pound() -> Self     class func stone() -> Self     class func moleUnit(with prefix: HKMetricPrefix, molarMass gramsPerMole: Double) -> Self     class func moleUnit(withMolarMass gramsPerMole: Double) -> Self } extension HKUnit {     class func meterUnit(with prefix: HKMetricPrefix) -> Self     class func meter() -> Self     class func inch() -> Self     class func foot() -> Self     class func yard() -> Self     class func mile() -> Self } extension HKUnit {     class func literUnit(with prefix: HKMetricPrefix) -> Self     class func liter() -> Self     class func fluidOunceUS() -> Self     class func fluidOunceImperial() -> Self     class func pintUS() -> Self     class func pintImperial() -> Self     class func cupUS() -> Self     class func cupImperial() -> Self } extension HKUnit {     class func pascalUnit(with prefix: HKMetricPrefix) -> Self     class func pascal() -> Self     class func millimeterOfMercury() -> Self     class func centimeterOfWater() -> Self     class func atmosphere() -> Self } extension HKUnit {     class func secondUnit(with prefix: HKMetricPrefix) -> Self     class func second() -> Self     class func minute() -> Self     class func hour() -> Self     class func day() -> Self } extension HKUnit {     class func jouleUnit(with prefix: HKMetricPrefix) -> Self     class func joule() -> Self     class func calorie() -> Self     class func kilocalorie() -> Self } extension HKUnit {     class func degreeCelsius() -> Self     class func degreeFahrenheit() -> Self     class func kelvin() -> Self } extension HKUnit {     class func siemenUnit(with prefix: HKMetricPrefix) -> Self     class func siemen() -> Self } extension HKUnit {     class func count() -> Self     class func percent() -> Self } extension HKUnit {     func unitMultiplied(by unit: HKUnit) -> HKUnit     func unitDivided(by unit: HKUnit) -> HKUnit     func unitRaised(toPower power: Int) -> HKUnit     func reciprocal() -> HKUnit } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [HKUnit.atmosphere() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615672-atmosphereunit)

|  | Declaration |
| --- | --- |
| From | ``` class func atmosphereUnit() -> Self ``` |
| To | ``` class func atmosphere() -> Self ``` |

Modified [HKUnit.calorie() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615359-calorie)

|  | Declaration |
| --- | --- |
| From | ``` class func calorieUnit() -> Self ``` |
| To | ``` class func calorie() -> Self ``` |

Modified [HKUnit.centimeterOfWater() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615036-centimeterofwater)

|  | Declaration |
| --- | --- |
| From | ``` class func centimeterOfWaterUnit() -> Self ``` |
| To | ``` class func centimeterOfWater() -> Self ``` |

Modified [HKUnit.count() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615529-countunit)

|  | Declaration |
| --- | --- |
| From | ``` class func countUnit() -> Self ``` |
| To | ``` class func count() -> Self ``` |

Modified [HKUnit.cupImperial() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615506-cupimperialunit)

|  | Declaration |
| --- | --- |
| From | ``` class func cupImperialUnit() -> Self ``` |
| To | ``` class func cupImperial() -> Self ``` |

Modified [HKUnit.cupUS() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615542-cupus)

|  | Declaration |
| --- | --- |
| From | ``` class func cupUSUnit() -> Self ``` |
| To | ``` class func cupUS() -> Self ``` |

Modified [HKUnit.day() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615707-dayunit)

|  | Declaration |
| --- | --- |
| From | ``` class func dayUnit() -> Self ``` |
| To | ``` class func day() -> Self ``` |

Modified [HKUnit.degreeCelsius() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615180-degreecelsius)

|  | Declaration |
| --- | --- |
| From | ``` class func degreeCelsiusUnit() -> Self ``` |
| To | ``` class func degreeCelsius() -> Self ``` |

Modified [HKUnit.degreeFahrenheit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615444-degreefahrenheitunit)

|  | Declaration |
| --- | --- |
| From | ``` class func degreeFahrenheitUnit() -> Self ``` |
| To | ``` class func degreeFahrenheit() -> Self ``` |

Modified [HKUnit.energyFormatterUnit(from: HKUnit) -> EnergyFormatter.Unit [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615211-energyformatterunitfromunit)

|  | Declaration |
| --- | --- |
| From | ``` class func energyFormatterUnitFromUnit(_ unit: HKUnit) -> NSEnergyFormatterUnit ``` |
| To | ``` class func energyFormatterUnit(from unit: HKUnit) -> EnergyFormatter.Unit ``` |

Modified [HKUnit.fluidOunceImperial() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615614-fluidounceimperial)

|  | Declaration |
| --- | --- |
| From | ``` class func fluidOunceImperialUnit() -> Self ``` |
| To | ``` class func fluidOunceImperial() -> Self ``` |

Modified [HKUnit.fluidOunceUS() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615310-fluidounceus)

|  | Declaration |
| --- | --- |
| From | ``` class func fluidOunceUSUnit() -> Self ``` |
| To | ``` class func fluidOunceUS() -> Self ``` |

Modified [HKUnit.foot() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615043-footunit)

|  | Declaration |
| --- | --- |
| From | ``` class func footUnit() -> Self ``` |
| To | ``` class func foot() -> Self ``` |

Modified [HKUnit.gram() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615050-gramunit)

|  | Declaration |
| --- | --- |
| From | ``` class func gramUnit() -> Self ``` |
| To | ``` class func gram() -> Self ``` |

Modified [HKUnit.gramUnit(with: HKMetricPrefix) -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615164-gramunitwithmetricprefix)

|  | Declaration |
| --- | --- |
| From | ``` class func gramUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self ``` |
| To | ``` class func gramUnit(with prefix: HKMetricPrefix) -> Self ``` |

Modified [HKUnit.hour() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615214-hourunit)

|  | Declaration |
| --- | --- |
| From | ``` class func hourUnit() -> Self ``` |
| To | ``` class func hour() -> Self ``` |

Modified [HKUnit.inch() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615144-inch)

|  | Declaration |
| --- | --- |
| From | ``` class func inchUnit() -> Self ``` |
| To | ``` class func inch() -> Self ``` |

Modified [HKUnit.init(from: MassFormatter.Unit)](https://developer.apple.com/documentation/healthkit/hkunit/1615182-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(fromMassFormatterUnit massFormatterUnit: NSMassFormatterUnit) ``` |
| To | ``` convenience init(from massFormatterUnit: MassFormatter.Unit) ``` |

Modified [HKUnit.init(from: LengthFormatter.Unit)](https://developer.apple.com/documentation/healthkit/hkunit/1615057-unitfromlengthformatterunit)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(fromLengthFormatterUnit lengthFormatterUnit: NSLengthFormatterUnit) ``` |
| To | ``` convenience init(from lengthFormatterUnit: LengthFormatter.Unit) ``` |

Modified [HKUnit.init(from: String)](https://developer.apple.com/documentation/healthkit/hkunit/1615733-unitfromstring)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(fromString string: String) ``` |
| To | ``` convenience init(from string: String) ``` |

Modified [HKUnit.init(from: EnergyFormatter.Unit)](https://developer.apple.com/documentation/healthkit/hkunit/1615218-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(fromEnergyFormatterUnit energyFormatterUnit: NSEnergyFormatterUnit) ``` |
| To | ``` convenience init(from energyFormatterUnit: EnergyFormatter.Unit) ``` |

Modified [HKUnit.joule() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615640-jouleunit)

|  | Declaration |
| --- | --- |
| From | ``` class func jouleUnit() -> Self ``` |
| To | ``` class func joule() -> Self ``` |

Modified [HKUnit.jouleUnit(with: HKMetricPrefix) -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615248-jouleunit)

|  | Declaration |
| --- | --- |
| From | ``` class func jouleUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self ``` |
| To | ``` class func jouleUnit(with prefix: HKMetricPrefix) -> Self ``` |

Modified [HKUnit.kelvin() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615289-kelvin)

|  | Declaration |
| --- | --- |
| From | ``` class func kelvinUnit() -> Self ``` |
| To | ``` class func kelvin() -> Self ``` |

Modified [HKUnit.kilocalorie() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615576-kilocalorieunit)

|  | Declaration |
| --- | --- |
| From | ``` class func kilocalorieUnit() -> Self ``` |
| To | ``` class func kilocalorie() -> Self ``` |

Modified [HKUnit.lengthFormatterUnit(from: HKUnit) -> LengthFormatter.Unit [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615309-lengthformatterunit)

|  | Declaration |
| --- | --- |
| From | ``` class func lengthFormatterUnitFromUnit(_ unit: HKUnit) -> NSLengthFormatterUnit ``` |
| To | ``` class func lengthFormatterUnit(from unit: HKUnit) -> LengthFormatter.Unit ``` |

Modified [HKUnit.liter() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615768-liter)

|  | Declaration |
| --- | --- |
| From | ``` class func literUnit() -> Self ``` |
| To | ``` class func liter() -> Self ``` |

Modified [HKUnit.literUnit(with: HKMetricPrefix) -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615369-literunit)

|  | Declaration |
| --- | --- |
| From | ``` class func literUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self ``` |
| To | ``` class func literUnit(with prefix: HKMetricPrefix) -> Self ``` |

Modified [HKUnit.massFormatterUnit(from: HKUnit) -> MassFormatter.Unit [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615100-massformatterunitfromunit)

|  | Declaration |
| --- | --- |
| From | ``` class func massFormatterUnitFromUnit(_ unit: HKUnit) -> NSMassFormatterUnit ``` |
| To | ``` class func massFormatterUnit(from unit: HKUnit) -> MassFormatter.Unit ``` |

Modified [HKUnit.meter() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615061-meter)

|  | Declaration |
| --- | --- |
| From | ``` class func meterUnit() -> Self ``` |
| To | ``` class func meter() -> Self ``` |

Modified [HKUnit.meterUnit(with: HKMetricPrefix) -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615489-meterunitwithmetricprefix)

|  | Declaration |
| --- | --- |
| From | ``` class func meterUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self ``` |
| To | ``` class func meterUnit(with prefix: HKMetricPrefix) -> Self ``` |

Modified [HKUnit.mile() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615390-mileunit)

|  | Declaration |
| --- | --- |
| From | ``` class func mileUnit() -> Self ``` |
| To | ``` class func mile() -> Self ``` |

Modified [HKUnit.millimeterOfMercury() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615410-millimeterofmercury)

|  | Declaration |
| --- | --- |
| From | ``` class func millimeterOfMercuryUnit() -> Self ``` |
| To | ``` class func millimeterOfMercury() -> Self ``` |

Modified [HKUnit.minute() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615362-minute)

|  | Declaration |
| --- | --- |
| From | ``` class func minuteUnit() -> Self ``` |
| To | ``` class func minute() -> Self ``` |

Modified [HKUnit.moleUnit(with: HKMetricPrefix, molarMass: Double) -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615608-moleunit)

|  | Declaration |
| --- | --- |
| From | ``` class func moleUnitWithMetricPrefix(_ prefix: HKMetricPrefix, molarMass gramsPerMole: Double) -> Self ``` |
| To | ``` class func moleUnit(with prefix: HKMetricPrefix, molarMass gramsPerMole: Double) -> Self ``` |

Modified [HKUnit.moleUnit(withMolarMass: Double) -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615515-moleunitwithmolarmass)

|  | Declaration |
| --- | --- |
| From | ``` class func moleUnitWithMolarMass(_ gramsPerMole: Double) -> Self ``` |
| To | ``` class func moleUnit(withMolarMass gramsPerMole: Double) -> Self ``` |

Modified [HKUnit.ounce() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615118-ounceunit)

|  | Declaration |
| --- | --- |
| From | ``` class func ounceUnit() -> Self ``` |
| To | ``` class func ounce() -> Self ``` |

Modified [HKUnit.pascal() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615172-pascal)

|  | Declaration |
| --- | --- |
| From | ``` class func pascalUnit() -> Self ``` |
| To | ``` class func pascal() -> Self ``` |

Modified [HKUnit.pascalUnit(with: HKMetricPrefix) -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615168-pascalunitwithmetricprefix)

|  | Declaration |
| --- | --- |
| From | ``` class func pascalUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self ``` |
| To | ``` class func pascalUnit(with prefix: HKMetricPrefix) -> Self ``` |

Modified [HKUnit.percent() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615517-percent)

|  | Declaration |
| --- | --- |
| From | ``` class func percentUnit() -> Self ``` |
| To | ``` class func percent() -> Self ``` |

Modified [HKUnit.pintImperial() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615306-pintimperial)

|  | Declaration |
| --- | --- |
| From | ``` class func pintImperialUnit() -> Self ``` |
| To | ``` class func pintImperial() -> Self ``` |

Modified [HKUnit.pintUS() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615528-pintus)

|  | Declaration |
| --- | --- |
| From | ``` class func pintUSUnit() -> Self ``` |
| To | ``` class func pintUS() -> Self ``` |

Modified [HKUnit.pound() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615563-poundunit)

|  | Declaration |
| --- | --- |
| From | ``` class func poundUnit() -> Self ``` |
| To | ``` class func pound() -> Self ``` |

Modified [HKUnit.reciprocal() -> HKUnit](https://developer.apple.com/documentation/healthkit/hkunit/1615494-reciprocalunit)

|  | Declaration |
| --- | --- |
| From | ``` func reciprocalUnit() -> HKUnit ``` |
| To | ``` func reciprocal() -> HKUnit ``` |

Modified [HKUnit.second() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615440-second)

|  | Declaration |
| --- | --- |
| From | ``` class func secondUnit() -> Self ``` |
| To | ``` class func second() -> Self ``` |

Modified [HKUnit.secondUnit(with: HKMetricPrefix) -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615644-secondunit)

|  | Declaration |
| --- | --- |
| From | ``` class func secondUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self ``` |
| To | ``` class func secondUnit(with prefix: HKMetricPrefix) -> Self ``` |

Modified [HKUnit.siemen() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615703-siemen)

|  | Declaration |
| --- | --- |
| From | ``` class func siemenUnit() -> Self ``` |
| To | ``` class func siemen() -> Self ``` |

Modified [HKUnit.siemenUnit(with: HKMetricPrefix) -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615648-siemenunitwithmetricprefix)

|  | Declaration |
| --- | --- |
| From | ``` class func siemenUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self ``` |
| To | ``` class func siemenUnit(with prefix: HKMetricPrefix) -> Self ``` |

Modified [HKUnit.stone() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615318-stoneunit)

|  | Declaration |
| --- | --- |
| From | ``` class func stoneUnit() -> Self ``` |
| To | ``` class func stone() -> Self ``` |

Modified [HKUnit.unitDivided(by: HKUnit) -> HKUnit](https://developer.apple.com/documentation/healthkit/hkunit/1615242-unitdividedbyunit)

|  | Declaration |
| --- | --- |
| From | ``` func unitDividedByUnit(_ unit: HKUnit) -> HKUnit ``` |
| To | ``` func unitDivided(by unit: HKUnit) -> HKUnit ``` |

Modified [HKUnit.unitMultiplied(by: HKUnit) -> HKUnit](https://developer.apple.com/documentation/healthkit/hkunit/1615718-unitmultiplied)

|  | Declaration |
| --- | --- |
| From | ``` func unitMultipliedByUnit(_ unit: HKUnit) -> HKUnit ``` |
| To | ``` func unitMultiplied(by unit: HKUnit) -> HKUnit ``` |

Modified [HKUnit.unitRaised(toPower: Int) -> HKUnit](https://developer.apple.com/documentation/healthkit/hkunit/1615495-unitraised)

|  | Declaration |
| --- | --- |
| From | ``` func unitRaisedToPower(_ power: Int) -> HKUnit ``` |
| To | ``` func unitRaised(toPower power: Int) -> HKUnit ``` |

Modified [HKUnit.yard() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615106-yardunit)

|  | Declaration |
| --- | --- |
| From | ``` class func yardUnit() -> Self ``` |
| To | ``` class func yard() -> Self ``` |

Modified [HKUpdateFrequency [enum]](https://developer.apple.com/documentation/healthkit/hkupdatefrequency)

|  | Declaration |
| --- | --- |
| From | ``` enum HKUpdateFrequency : Int {     case Immediate     case Hourly     case Daily     case Weekly } ``` |
| To | ``` enum HKUpdateFrequency : Int {     case immediate     case hourly     case daily     case weekly } ``` |

Modified [HKUpdateFrequency.daily](https://developer.apple.com/documentation/healthkit/hkupdatefrequency/daily)

|  | Declaration |
| --- | --- |
| From | ``` case Daily ``` |
| To | ``` case daily ``` |

Modified [HKUpdateFrequency.hourly](https://developer.apple.com/documentation/healthkit/hkupdatefrequency/hkupdatefrequencyhourly)

|  | Declaration |
| --- | --- |
| From | ``` case Hourly ``` |
| To | ``` case hourly ``` |

Modified [HKUpdateFrequency.immediate](https://developer.apple.com/documentation/healthkit/hkupdatefrequency/immediate)

|  | Declaration |
| --- | --- |
| From | ``` case Immediate ``` |
| To | ``` case immediate ``` |

Modified [HKUpdateFrequency.weekly](https://developer.apple.com/documentation/healthkit/hkupdatefrequency/hkupdatefrequencyweekly)

|  | Declaration |
| --- | --- |
| From | ``` case Weekly ``` |
| To | ``` case weekly ``` |

Modified [HKWorkout](https://developer.apple.com/documentation/healthkit/hkworkout)

|  | Declaration |
| --- | --- |
| From | ``` class HKWorkout : HKSample {     var workoutActivityType: HKWorkoutActivityType { get }     var workoutEvents: [HKWorkoutEvent]? { get }     var duration: NSTimeInterval { get }     var totalEnergyBurned: HKQuantity? { get }     var totalDistance: HKQuantity? { get }     convenience init(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate)     class func workoutWithActivityType(_ workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate) -> Self     convenience init(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate, workoutEvents workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, metadata metadata: [String : AnyObject]?)     class func workoutWithActivityType(_ workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate, workoutEvents workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, metadata metadata: [String : AnyObject]?) -> Self     convenience init(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate, workoutEvents workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, device device: HKDevice?, metadata metadata: [String : AnyObject]?)     class func workoutWithActivityType(_ workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate, workoutEvents workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, device device: HKDevice?, metadata metadata: [String : AnyObject]?) -> Self     convenience init(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate, duration duration: NSTimeInterval, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, metadata metadata: [String : AnyObject]?)     class func workoutWithActivityType(_ workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate, duration duration: NSTimeInterval, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, metadata metadata: [String : AnyObject]?) -> Self     convenience init(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate, duration duration: NSTimeInterval, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, device device: HKDevice?, metadata metadata: [String : AnyObject]?)     class func workoutWithActivityType(_ workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate, duration duration: NSTimeInterval, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, device device: HKDevice?, metadata metadata: [String : AnyObject]?) -> Self } ``` |
| To | ``` class HKWorkout : HKSample {     var workoutActivityType: HKWorkoutActivityType { get }     var workoutEvents: [HKWorkoutEvent]? { get }     var duration: TimeInterval { get }     var totalEnergyBurned: HKQuantity? { get }     var totalDistance: HKQuantity? { get }     var totalSwimmingStrokeCount: HKQuantity? { get }     convenience init(activityType workoutActivityType: HKWorkoutActivityType, start startDate: Date, end endDate: Date)     class func withActivityType(_ workoutActivityType: HKWorkoutActivityType, start startDate: Date, end endDate: Date) -> Self     convenience init(activityType workoutActivityType: HKWorkoutActivityType, start startDate: Date, end endDate: Date, workoutEvents workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, metadata metadata: [String : Any]?)     class func withActivityType(_ workoutActivityType: HKWorkoutActivityType, start startDate: Date, end endDate: Date, workoutEvents workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, metadata metadata: [String : Any]?) -> Self     convenience init(activityType workoutActivityType: HKWorkoutActivityType, start startDate: Date, end endDate: Date, workoutEvents workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, device device: HKDevice?, metadata metadata: [String : Any]?)     class func withActivityType(_ workoutActivityType: HKWorkoutActivityType, start startDate: Date, end endDate: Date, workoutEvents workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, device device: HKDevice?, metadata metadata: [String : Any]?) -> Self     convenience init(activityType workoutActivityType: HKWorkoutActivityType, start startDate: Date, end endDate: Date, duration duration: TimeInterval, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, metadata metadata: [String : Any]?)     class func withActivityType(_ workoutActivityType: HKWorkoutActivityType, start startDate: Date, end endDate: Date, duration duration: TimeInterval, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, metadata metadata: [String : Any]?) -> Self     convenience init(activityType workoutActivityType: HKWorkoutActivityType, start startDate: Date, end endDate: Date, duration duration: TimeInterval, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, device device: HKDevice?, metadata metadata: [String : Any]?)     class func withActivityType(_ workoutActivityType: HKWorkoutActivityType, start startDate: Date, end endDate: Date, duration duration: TimeInterval, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, device device: HKDevice?, metadata metadata: [String : Any]?) -> Self     convenience init(activityType workoutActivityType: HKWorkoutActivityType, start startDate: Date, end endDate: Date, workoutEvents workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, totalSwimmingStrokeCount totalSwimmingStrokeCount: HKQuantity?, device device: HKDevice?, metadata metadata: [String : Any]?)     class func withActivityType(_ workoutActivityType: HKWorkoutActivityType, start startDate: Date, end endDate: Date, workoutEvents workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, totalSwimmingStrokeCount totalSwimmingStrokeCount: HKQuantity?, device device: HKDevice?, metadata metadata: [String : Any]?) -> Self } ``` |

Modified [HKWorkout.duration](https://developer.apple.com/documentation/healthkit/hkworkout/1615240-duration)

|  | Declaration |
| --- | --- |
| From | ``` var duration: NSTimeInterval { get } ``` |
| To | ``` var duration: TimeInterval { get } ``` |

Modified [HKWorkout.init(activityType: HKWorkoutActivityType, start: Date, end: Date)](https://developer.apple.com/documentation/healthkit/hkworkout/1615340-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate) ``` |
| To | ``` convenience init(activityType workoutActivityType: HKWorkoutActivityType, start startDate: Date, end endDate: Date) ``` |

Modified [HKWorkout.init(activityType: HKWorkoutActivityType, start: Date, end: Date, duration: TimeInterval, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, device: HKDevice?, metadata: [String : Any]?)](https://developer.apple.com/documentation/healthkit/hkworkout/1615048-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate, duration duration: NSTimeInterval, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, device device: HKDevice?, metadata metadata: [String : AnyObject]?) ``` |
| To | ``` convenience init(activityType workoutActivityType: HKWorkoutActivityType, start startDate: Date, end endDate: Date, duration duration: TimeInterval, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, device device: HKDevice?, metadata metadata: [String : Any]?) ``` |

Modified [HKWorkout.init(activityType: HKWorkoutActivityType, start: Date, end: Date, duration: TimeInterval, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, metadata: [String : Any]?)](https://developer.apple.com/documentation/healthkit/hkworkout/1615739-workoutwithactivitytype)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate, duration duration: NSTimeInterval, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, metadata metadata: [String : AnyObject]?) ``` |
| To | ``` convenience init(activityType workoutActivityType: HKWorkoutActivityType, start startDate: Date, end endDate: Date, duration duration: TimeInterval, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, metadata metadata: [String : Any]?) ``` |

Modified [HKWorkout.init(activityType: HKWorkoutActivityType, start: Date, end: Date, workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, device: HKDevice?, metadata: [String : Any]?)](https://developer.apple.com/documentation/healthkit/hkworkout/1615713-workoutwithactivitytype)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate, workoutEvents workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, device device: HKDevice?, metadata metadata: [String : AnyObject]?) ``` |
| To | ``` convenience init(activityType workoutActivityType: HKWorkoutActivityType, start startDate: Date, end endDate: Date, workoutEvents workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, device device: HKDevice?, metadata metadata: [String : Any]?) ``` |

Modified [HKWorkout.init(activityType: HKWorkoutActivityType, start: Date, end: Date, workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, metadata: [String : Any]?)](https://developer.apple.com/documentation/healthkit/hkworkout/1615212-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate, workoutEvents workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, metadata metadata: [String : AnyObject]?) ``` |
| To | ``` convenience init(activityType workoutActivityType: HKWorkoutActivityType, start startDate: Date, end endDate: Date, workoutEvents workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, metadata metadata: [String : Any]?) ``` |

Modified [HKWorkoutActivityType [enum]](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype)

|  | Declaration |
| --- | --- |
| From | ``` enum HKWorkoutActivityType : UInt {     case AmericanFootball     case Archery     case AustralianFootball     case Badminton     case Baseball     case Basketball     case Bowling     case Boxing     case Climbing     case Cricket     case CrossTraining     case Curling     case Cycling     case Dance     case DanceInspiredTraining     case Elliptical     case EquestrianSports     case Fencing     case Fishing     case FunctionalStrengthTraining     case Golf     case Gymnastics     case Handball     case Hiking     case Hockey     case Hunting     case Lacrosse     case MartialArts     case MindAndBody     case MixedMetabolicCardioTraining     case PaddleSports     case Play     case PreparationAndRecovery     case Racquetball     case Rowing     case Rugby     case Running     case Sailing     case SkatingSports     case SnowSports     case Soccer     case Softball     case Squash     case StairClimbing     case SurfingSports     case Swimming     case TableTennis     case Tennis     case TrackAndField     case TraditionalStrengthTraining     case Volleyball     case Walking     case WaterFitness     case WaterPolo     case WaterSports     case Wrestling     case Yoga     case Other } ``` |
| To | ``` enum HKWorkoutActivityType : UInt {     case americanFootball     case archery     case australianFootball     case badminton     case baseball     case basketball     case bowling     case boxing     case climbing     case cricket     case crossTraining     case curling     case cycling     case dance     case danceInspiredTraining     case elliptical     case equestrianSports     case fencing     case fishing     case functionalStrengthTraining     case golf     case gymnastics     case handball     case hiking     case hockey     case hunting     case lacrosse     case martialArts     case mindAndBody     case mixedMetabolicCardioTraining     case paddleSports     case play     case preparationAndRecovery     case racquetball     case rowing     case rugby     case running     case sailing     case skatingSports     case snowSports     case soccer     case softball     case squash     case stairClimbing     case surfingSports     case swimming     case tableTennis     case tennis     case trackAndField     case traditionalStrengthTraining     case volleyball     case walking     case waterFitness     case waterPolo     case waterSports     case wrestling     case yoga     case barre     case coreTraining     case crossCountrySkiing     case downhillSkiing     case flexibility     case highIntensityIntervalTraining     case jumpRope     case kickboxing     case pilates     case snowboarding     case stairs     case stepTraining     case wheelchairWalkPace     case wheelchairRunPace     case other } ``` |

Modified [HKWorkoutActivityType.americanFootball](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/americanfootball)

|  | Declaration |
| --- | --- |
| From | ``` case AmericanFootball ``` |
| To | ``` case americanFootball ``` |

Modified [HKWorkoutActivityType.archery](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypearchery)

|  | Declaration |
| --- | --- |
| From | ``` case Archery ``` |
| To | ``` case archery ``` |

Modified [HKWorkoutActivityType.australianFootball](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypeaustralianfootball)

|  | Declaration |
| --- | --- |
| From | ``` case AustralianFootball ``` |
| To | ``` case australianFootball ``` |

Modified [HKWorkoutActivityType.badminton](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypebadminton)

|  | Declaration |
| --- | --- |
| From | ``` case Badminton ``` |
| To | ``` case badminton ``` |

Modified [HKWorkoutActivityType.baseball](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/baseball)

|  | Declaration |
| --- | --- |
| From | ``` case Baseball ``` |
| To | ``` case baseball ``` |

Modified [HKWorkoutActivityType.basketball](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/basketball)

|  | Declaration |
| --- | --- |
| From | ``` case Basketball ``` |
| To | ``` case basketball ``` |

Modified [HKWorkoutActivityType.bowling](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypebowling)

|  | Declaration |
| --- | --- |
| From | ``` case Bowling ``` |
| To | ``` case bowling ``` |

Modified [HKWorkoutActivityType.boxing](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/boxing)

|  | Declaration |
| --- | --- |
| From | ``` case Boxing ``` |
| To | ``` case boxing ``` |

Modified [HKWorkoutActivityType.climbing](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypeclimbing)

|  | Declaration |
| --- | --- |
| From | ``` case Climbing ``` |
| To | ``` case climbing ``` |

Modified [HKWorkoutActivityType.cricket](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/cricket)

|  | Declaration |
| --- | --- |
| From | ``` case Cricket ``` |
| To | ``` case cricket ``` |

Modified [HKWorkoutActivityType.crossTraining](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/crosstraining)

|  | Declaration |
| --- | --- |
| From | ``` case CrossTraining ``` |
| To | ``` case crossTraining ``` |

Modified [HKWorkoutActivityType.curling](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypecurling)

|  | Declaration |
| --- | --- |
| From | ``` case Curling ``` |
| To | ``` case curling ``` |

Modified [HKWorkoutActivityType.cycling](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypecycling)

|  | Declaration |
| --- | --- |
| From | ``` case Cycling ``` |
| To | ``` case cycling ``` |

Modified [HKWorkoutActivityType.dance](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypedance)

|  | Declaration |
| --- | --- |
| From | ``` case Dance ``` |
| To | ``` case dance ``` |

Modified [HKWorkoutActivityType.danceInspiredTraining](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypedanceinspiredtraining)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` case DanceInspiredTraining ``` | -- |
| To | ``` case danceInspiredTraining ``` | iOS 10.0 |

Modified [HKWorkoutActivityType.elliptical](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/elliptical)

|  | Declaration |
| --- | --- |
| From | ``` case Elliptical ``` |
| To | ``` case elliptical ``` |

Modified [HKWorkoutActivityType.equestrianSports](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/equestriansports)

|  | Declaration |
| --- | --- |
| From | ``` case EquestrianSports ``` |
| To | ``` case equestrianSports ``` |

Modified [HKWorkoutActivityType.fencing](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypefencing)

|  | Declaration |
| --- | --- |
| From | ``` case Fencing ``` |
| To | ``` case fencing ``` |

Modified [HKWorkoutActivityType.fishing](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypefishing)

|  | Declaration |
| --- | --- |
| From | ``` case Fishing ``` |
| To | ``` case fishing ``` |

Modified [HKWorkoutActivityType.functionalStrengthTraining](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypefunctionalstrengthtraining)

|  | Declaration |
| --- | --- |
| From | ``` case FunctionalStrengthTraining ``` |
| To | ``` case functionalStrengthTraining ``` |

Modified [HKWorkoutActivityType.golf](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypegolf)

|  | Declaration |
| --- | --- |
| From | ``` case Golf ``` |
| To | ``` case golf ``` |

Modified [HKWorkoutActivityType.gymnastics](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/gymnastics)

|  | Declaration |
| --- | --- |
| From | ``` case Gymnastics ``` |
| To | ``` case gymnastics ``` |

Modified [HKWorkoutActivityType.handball](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypehandball)

|  | Declaration |
| --- | --- |
| From | ``` case Handball ``` |
| To | ``` case handball ``` |

Modified [HKWorkoutActivityType.hiking](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hiking)

|  | Declaration |
| --- | --- |
| From | ``` case Hiking ``` |
| To | ``` case hiking ``` |

Modified [HKWorkoutActivityType.hockey](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypehockey)

|  | Declaration |
| --- | --- |
| From | ``` case Hockey ``` |
| To | ``` case hockey ``` |

Modified [HKWorkoutActivityType.hunting](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypehunting)

|  | Declaration |
| --- | --- |
| From | ``` case Hunting ``` |
| To | ``` case hunting ``` |

Modified [HKWorkoutActivityType.lacrosse](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypelacrosse)

|  | Declaration |
| --- | --- |
| From | ``` case Lacrosse ``` |
| To | ``` case lacrosse ``` |

Modified [HKWorkoutActivityType.martialArts](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypemartialarts)

|  | Declaration |
| --- | --- |
| From | ``` case MartialArts ``` |
| To | ``` case martialArts ``` |

Modified [HKWorkoutActivityType.mindAndBody](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/mindandbody)

|  | Declaration |
| --- | --- |
| From | ``` case MindAndBody ``` |
| To | ``` case mindAndBody ``` |

Modified [HKWorkoutActivityType.mixedMetabolicCardioTraining](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypemixedmetaboliccardiotraining)

|  | Declaration |
| --- | --- |
| From | ``` case MixedMetabolicCardioTraining ``` |
| To | ``` case mixedMetabolicCardioTraining ``` |

Modified [HKWorkoutActivityType.other](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/other)

|  | Declaration |
| --- | --- |
| From | ``` case Other ``` |
| To | ``` case other ``` |

Modified [HKWorkoutActivityType.paddleSports](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypepaddlesports)

|  | Declaration |
| --- | --- |
| From | ``` case PaddleSports ``` |
| To | ``` case paddleSports ``` |

Modified [HKWorkoutActivityType.play](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypeplay)

|  | Declaration |
| --- | --- |
| From | ``` case Play ``` |
| To | ``` case play ``` |

Modified [HKWorkoutActivityType.preparationAndRecovery](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/preparationandrecovery)

|  | Declaration |
| --- | --- |
| From | ``` case PreparationAndRecovery ``` |
| To | ``` case preparationAndRecovery ``` |

Modified [HKWorkoutActivityType.racquetball](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytyperacquetball)

|  | Declaration |
| --- | --- |
| From | ``` case Racquetball ``` |
| To | ``` case racquetball ``` |

Modified [HKWorkoutActivityType.rowing](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/rowing)

|  | Declaration |
| --- | --- |
| From | ``` case Rowing ``` |
| To | ``` case rowing ``` |

Modified [HKWorkoutActivityType.rugby](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytyperugby)

|  | Declaration |
| --- | --- |
| From | ``` case Rugby ``` |
| To | ``` case rugby ``` |

Modified [HKWorkoutActivityType.running](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytyperunning)

|  | Declaration |
| --- | --- |
| From | ``` case Running ``` |
| To | ``` case running ``` |

Modified [HKWorkoutActivityType.sailing](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypesailing)

|  | Declaration |
| --- | --- |
| From | ``` case Sailing ``` |
| To | ``` case sailing ``` |

Modified [HKWorkoutActivityType.skatingSports](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/skatingsports)

|  | Declaration |
| --- | --- |
| From | ``` case SkatingSports ``` |
| To | ``` case skatingSports ``` |

Modified [HKWorkoutActivityType.snowSports](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypesnowsports)

|  | Declaration |
| --- | --- |
| From | ``` case SnowSports ``` |
| To | ``` case snowSports ``` |

Modified [HKWorkoutActivityType.soccer](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/soccer)

|  | Declaration |
| --- | --- |
| From | ``` case Soccer ``` |
| To | ``` case soccer ``` |

Modified [HKWorkoutActivityType.softball](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/softball)

|  | Declaration |
| --- | --- |
| From | ``` case Softball ``` |
| To | ``` case softball ``` |

Modified [HKWorkoutActivityType.squash](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/squash)

|  | Declaration |
| --- | --- |
| From | ``` case Squash ``` |
| To | ``` case squash ``` |

Modified [HKWorkoutActivityType.stairClimbing](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypestairclimbing)

|  | Declaration |
| --- | --- |
| From | ``` case StairClimbing ``` |
| To | ``` case stairClimbing ``` |

Modified [HKWorkoutActivityType.surfingSports](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypesurfingsports)

|  | Declaration |
| --- | --- |
| From | ``` case SurfingSports ``` |
| To | ``` case surfingSports ``` |

Modified [HKWorkoutActivityType.swimming](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/swimming)

|  | Declaration |
| --- | --- |
| From | ``` case Swimming ``` |
| To | ``` case swimming ``` |

Modified [HKWorkoutActivityType.tableTennis](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/tabletennis)

|  | Declaration |
| --- | --- |
| From | ``` case TableTennis ``` |
| To | ``` case tableTennis ``` |

Modified [HKWorkoutActivityType.tennis](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/tennis)

|  | Declaration |
| --- | --- |
| From | ``` case Tennis ``` |
| To | ``` case tennis ``` |

Modified [HKWorkoutActivityType.trackAndField](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/trackandfield)

|  | Declaration |
| --- | --- |
| From | ``` case TrackAndField ``` |
| To | ``` case trackAndField ``` |

Modified [HKWorkoutActivityType.traditionalStrengthTraining](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/traditionalstrengthtraining)

|  | Declaration |
| --- | --- |
| From | ``` case TraditionalStrengthTraining ``` |
| To | ``` case traditionalStrengthTraining ``` |

Modified [HKWorkoutActivityType.volleyball](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/volleyball)

|  | Declaration |
| --- | --- |
| From | ``` case Volleyball ``` |
| To | ``` case volleyball ``` |

Modified [HKWorkoutActivityType.walking](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypewalking)

|  | Declaration |
| --- | --- |
| From | ``` case Walking ``` |
| To | ``` case walking ``` |

Modified [HKWorkoutActivityType.waterFitness](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypewaterfitness)

|  | Declaration |
| --- | --- |
| From | ``` case WaterFitness ``` |
| To | ``` case waterFitness ``` |

Modified [HKWorkoutActivityType.waterPolo](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/waterpolo)

|  | Declaration |
| --- | --- |
| From | ``` case WaterPolo ``` |
| To | ``` case waterPolo ``` |

Modified [HKWorkoutActivityType.waterSports](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/watersports)

|  | Declaration |
| --- | --- |
| From | ``` case WaterSports ``` |
| To | ``` case waterSports ``` |

Modified [HKWorkoutActivityType.wrestling](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypewrestling)

|  | Declaration |
| --- | --- |
| From | ``` case Wrestling ``` |
| To | ``` case wrestling ``` |

Modified [HKWorkoutActivityType.yoga](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/yoga)

|  | Declaration |
| --- | --- |
| From | ``` case Yoga ``` |
| To | ``` case yoga ``` |

Modified [HKWorkoutEvent](https://developer.apple.com/documentation/healthkit/hkworkoutevent)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKWorkoutEvent : NSObject, NSSecureCoding {     var type: HKWorkoutEventType { get }     @NSCopying var date: NSDate { get }     convenience init(type type: HKWorkoutEventType, date date: NSDate)     class func workoutEventWithType(_ type: HKWorkoutEventType, date date: NSDate) -> Self     init() } ``` | NSSecureCoding |
| To | ``` class HKWorkoutEvent : NSObject, NSSecureCoding, NSCopying {     var type: HKWorkoutEventType { get }     var date: Date { get }     var metadata: [String : Any]? { get }     convenience init(type type: HKWorkoutEventType, date date: Date)     class func withType(_ type: HKWorkoutEventType, date date: Date) -> Self     convenience init(type type: HKWorkoutEventType, date date: Date, metadata metadata: [String : Any])     class func withType(_ type: HKWorkoutEventType, date date: Date, metadata metadata: [String : Any]) -> Self     init()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HKWorkoutEvent : CVarArg { } extension HKWorkoutEvent : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [HKWorkoutEvent.date](https://developer.apple.com/documentation/healthkit/hkworkoutevent/1615392-date)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var date: NSDate { get } ``` |
| To | ``` var date: Date { get } ``` |

Modified [HKWorkoutEvent.init(type: HKWorkoutEventType, date: Date)](https://developer.apple.com/documentation/healthkit/hkworkoutevent/1615600-workouteventwithtype)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(type type: HKWorkoutEventType, date date: NSDate) ``` |
| To | ``` convenience init(type type: HKWorkoutEventType, date date: Date) ``` |

Modified [HKWorkoutEventType [enum]](https://developer.apple.com/documentation/healthkit/hkworkouteventtype)

|  | Declaration |
| --- | --- |
| From | ``` enum HKWorkoutEventType : Int {     case Pause     case Resume } ``` |
| To | ``` enum HKWorkoutEventType : Int {     case pause     case resume     case lap     case marker     case motionPaused     case motionResumed } ``` |

Modified [HKWorkoutEventType.pause](https://developer.apple.com/documentation/healthkit/hkworkouteventtype/hkworkouteventtypepause)

|  | Declaration |
| --- | --- |
| From | ``` case Pause ``` |
| To | ``` case pause ``` |

Modified [HKWorkoutEventType.resume](https://developer.apple.com/documentation/healthkit/hkworkouteventtype/resume)

|  | Declaration |
| --- | --- |
| From | ``` case Resume ``` |
| To | ``` case resume ``` |

Modified [NSNotification.Name.HKUserPreferencesDidChange](https://developer.apple.com/documentation/foundation/nsnotification/name/1614169-hkuserpreferencesdidchange)

|  | Name | Declaration |
| --- | --- | --- |
| From | HKUserPreferencesDidChangeNotification | ``` let HKUserPreferencesDidChangeNotification: String ``` |
| To | HKUserPreferencesDidChange | ``` static let HKUserPreferencesDidChange: NSNotification.Name ``` |

Modified [HKObserverQueryCompletionHandler](https://developer.apple.com/documentation/healthkit/hkobserverquerycompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias HKObserverQueryCompletionHandler = () -> Void ``` |
| To | ``` typealias HKObserverQueryCompletionHandler = () -> Swift.Void ``` |

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
