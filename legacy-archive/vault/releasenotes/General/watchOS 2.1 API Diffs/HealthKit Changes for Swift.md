---
title: watchOS 2.1 API Diffs
apple_id: TP40016636
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2015-12-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS21APIDiffs/Swift/HealthKit.html
archived_at: '2026-07-18T02:58:08.780090Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 2.1 API Diffs](watchOS%202.0%20to%20watchOS%202.1%20API%20Differences.md)


# HealthKit Changes for Swift

### HealthKit

Modified [HKAnchoredObjectQuery](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquery)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HKAuthorizationStatus [enum]](https://developer.apple.com/documentation/healthkit/hkauthorizationstatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HKBiologicalSex [enum]](https://developer.apple.com/documentation/healthkit/hkbiologicalsex)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HKBiologicalSexObject](https://developer.apple.com/documentation/healthkit/hkbiologicalsexobject)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKBiologicalSexObject : NSObject, NSCopying, NSSecureCoding, NSCoding {     var biologicalSex: HKBiologicalSex { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class HKBiologicalSexObject : NSObject, NSCopying, NSSecureCoding {     var biologicalSex: HKBiologicalSex { get } } ``` | NSCopying, NSSecureCoding |

Modified [HKBloodType [enum]](https://developer.apple.com/documentation/healthkit/hkbloodtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HKBloodTypeObject](https://developer.apple.com/documentation/healthkit/hkbloodtypeobject)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKBloodTypeObject : NSObject, NSCopying, NSSecureCoding, NSCoding {     var bloodType: HKBloodType { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class HKBloodTypeObject : NSObject, NSCopying, NSSecureCoding {     var bloodType: HKBloodType { get } } ``` | NSCopying, NSSecureCoding |

Modified [HKBodyTemperatureSensorLocation [enum]](https://developer.apple.com/documentation/healthkit/hkbodytemperaturesensorlocation)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HKCategorySample](https://developer.apple.com/documentation/healthkit/hkcategorysample)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HKCategoryType](https://developer.apple.com/documentation/healthkit/hkcategorytype)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HKCategoryValue [enum]](https://developer.apple.com/documentation/healthkit/hkcategoryvalue)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HKCategoryValueAppleStandHour [enum]](https://developer.apple.com/documentation/healthkit/hkcategoryvalueapplestandhour)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HKCategoryValueCervicalMucusQuality [enum]](https://developer.apple.com/documentation/healthkit/hkcategoryvaluecervicalmucusquality)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HKCategoryValueMenstrualFlow [enum]](https://developer.apple.com/documentation/healthkit/hkcategoryvaluemenstrualflow)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HKCategoryValueOvulationTestResult [enum]](https://developer.apple.com/documentation/healthkit/hkcategoryvalueovulationtestresult)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HKCategoryValueSleepAnalysis [enum]](https://developer.apple.com/documentation/healthkit/hkcategoryvaluesleepanalysis)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HKCharacteristicType](https://developer.apple.com/documentation/healthkit/hkcharacteristictype)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HKCorrelation](https://developer.apple.com/documentation/healthkit/hkcorrelation)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HKCorrelationQuery](https://developer.apple.com/documentation/healthkit/hkcorrelationquery)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HKCorrelationType](https://developer.apple.com/documentation/healthkit/hkcorrelationtype)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HKDeletedObject](https://developer.apple.com/documentation/healthkit/hkdeletedobject)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKDeletedObject : NSObject, NSSecureCoding, NSCoding {     var UUID: NSUUID { get }     init() } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class HKDeletedObject : NSObject, NSSecureCoding {     var UUID: NSUUID { get }     init() } ``` | NSSecureCoding |

Modified [HKDevice](https://developer.apple.com/documentation/healthkit/hkdevice)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKDevice : NSObject, NSSecureCoding, NSCoding, NSCopying {     var name: String { get }     var manufacturer: String? { get }     var model: String? { get }     var hardwareVersion: String? { get }     var firmwareVersion: String? { get }     var softwareVersion: String? { get }     var localIdentifier: String? { get }     var UDIDeviceIdentifier: String? { get }     init(name name: String?, manufacturer manufacturer: String?, model model: String?, hardwareVersion hardwareVersion: String?, firmwareVersion firmwareVersion: String?, softwareVersion softwareVersion: String?, localIdentifier localIdentifier: String?, UDIDeviceIdentifier UDIDeviceIdentifier: String?)     init()     class func localDevice() -> HKDevice } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class HKDevice : NSObject, NSSecureCoding, NSCopying {     var name: String { get }     var manufacturer: String? { get }     var model: String? { get }     var hardwareVersion: String? { get }     var firmwareVersion: String? { get }     var softwareVersion: String? { get }     var localIdentifier: String? { get }     var UDIDeviceIdentifier: String? { get }     init(name name: String?, manufacturer manufacturer: String?, model model: String?, hardwareVersion hardwareVersion: String?, firmwareVersion firmwareVersion: String?, softwareVersion softwareVersion: String?, localIdentifier localIdentifier: String?, UDIDeviceIdentifier UDIDeviceIdentifier: String?)     init()     class func localDevice() -> HKDevice } ``` | NSCopying, NSSecureCoding |

Modified [HKErrorCode [enum]](https://developer.apple.com/documentation/healthkit/hkerrorcode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HKFitzpatrickSkinType [enum]](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HKFitzpatrickSkinTypeObject](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintypeobject)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKFitzpatrickSkinTypeObject : NSObject, NSCopying, NSSecureCoding, NSCoding {     var skinType: HKFitzpatrickSkinType { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class HKFitzpatrickSkinTypeObject : NSObject, NSCopying, NSSecureCoding {     var skinType: HKFitzpatrickSkinType { get } } ``` | NSCopying, NSSecureCoding |

Modified [HKHealthStore](https://developer.apple.com/documentation/healthkit/hkhealthstore)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HKHeartRateSensorLocation [enum]](https://developer.apple.com/documentation/healthkit/hkheartratesensorlocation)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HKMetricPrefix [enum]](https://developer.apple.com/documentation/healthkit/hkmetricprefix)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HKObject](https://developer.apple.com/documentation/healthkit/hkobject)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKObject : NSObject, NSSecureCoding, NSCoding {     var UUID: NSUUID { get }     var source: HKSource { get }     var sourceRevision: HKSourceRevision { get }     var device: HKDevice? { get }     var metadata: [String : AnyObject]? { get }     init() } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class HKObject : NSObject, NSSecureCoding {     var UUID: NSUUID { get }     var source: HKSource { get }     var sourceRevision: HKSourceRevision { get }     var device: HKDevice? { get }     var metadata: [String : AnyObject]? { get }     init() } ``` | NSSecureCoding |

Modified [HKObjectType](https://developer.apple.com/documentation/healthkit/hkobjecttype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKObjectType : NSObject, NSSecureCoding, NSCoding, NSCopying {     var identifier: String { get }     init()     class func quantityTypeForIdentifier(_ identifier: String) -> HKQuantityType?     class func categoryTypeForIdentifier(_ identifier: String) -> HKCategoryType?     class func characteristicTypeForIdentifier(_ identifier: String) -> HKCharacteristicType?     class func correlationTypeForIdentifier(_ identifier: String) -> HKCorrelationType?     class func workoutType() -> HKWorkoutType } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class HKObjectType : NSObject, NSSecureCoding, NSCopying {     var identifier: String { get }     init()     class func quantityTypeForIdentifier(_ identifier: String) -> HKQuantityType?     class func categoryTypeForIdentifier(_ identifier: String) -> HKCategoryType?     class func characteristicTypeForIdentifier(_ identifier: String) -> HKCharacteristicType?     class func correlationTypeForIdentifier(_ identifier: String) -> HKCorrelationType?     class func workoutType() -> HKWorkoutType } ``` | NSCopying, NSSecureCoding |

Modified [HKObserverQuery](https://developer.apple.com/documentation/healthkit/hkobserverquery)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HKQuantity](https://developer.apple.com/documentation/healthkit/hkquantity)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKQuantity : NSObject, NSSecureCoding, NSCoding, NSCopying {     init()     convenience init(unit unit: HKUnit, doubleValue value: Double)     class func quantityWithUnit(_ unit: HKUnit, doubleValue value: Double) -> Self     func isCompatibleWithUnit(_ unit: HKUnit) -> Bool     func doubleValueForUnit(_ unit: HKUnit) -> Double     func compare(_ quantity: HKQuantity) -> NSComparisonResult } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class HKQuantity : NSObject, NSSecureCoding, NSCopying {     init()     convenience init(unit unit: HKUnit, doubleValue value: Double)     class func quantityWithUnit(_ unit: HKUnit, doubleValue value: Double) -> Self     func isCompatibleWithUnit(_ unit: HKUnit) -> Bool     func doubleValueForUnit(_ unit: HKUnit) -> Double     func compare(_ quantity: HKQuantity) -> NSComparisonResult } ``` | NSCopying, NSSecureCoding |

Modified [HKQuantityAggregationStyle [enum]](https://developer.apple.com/documentation/healthkit/hkquantityaggregationstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HKQuantitySample](https://developer.apple.com/documentation/healthkit/hkquantitysample)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HKQuantityType](https://developer.apple.com/documentation/healthkit/hkquantitytype)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HKQuery](https://developer.apple.com/documentation/healthkit/hkquery)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HKQueryAnchor](https://developer.apple.com/documentation/healthkit/hkqueryanchor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKQueryAnchor : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init(fromValue value: Int)     class func anchorFromValue(_ value: Int) -> Self     init() } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class HKQueryAnchor : NSObject, NSSecureCoding, NSCopying {     convenience init(fromValue value: Int)     class func anchorFromValue(_ value: Int) -> Self     init() } ``` | NSCopying, NSSecureCoding |

Modified [HKSample](https://developer.apple.com/documentation/healthkit/hksample)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HKSampleQuery](https://developer.apple.com/documentation/healthkit/hksamplequery)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HKSampleType](https://developer.apple.com/documentation/healthkit/hksampletype)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HKSource](https://developer.apple.com/documentation/healthkit/hksource)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKSource : NSObject, NSSecureCoding, NSCoding, NSCopying {     var name: String { get }     var bundleIdentifier: String { get }     class func defaultSource() -> HKSource     init() } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class HKSource : NSObject, NSSecureCoding, NSCopying {     var name: String { get }     var bundleIdentifier: String { get }     class func defaultSource() -> HKSource     init() } ``` | NSCopying, NSSecureCoding |

Modified [HKSourceQuery](https://developer.apple.com/documentation/healthkit/hksourcequery)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HKSourceRevision](https://developer.apple.com/documentation/healthkit/hksourcerevision)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKSourceRevision : NSObject, NSSecureCoding, NSCoding, NSCopying {     var source: HKSource { get }     var version: String? { get }     init(source source: HKSource, version version: String)     init() } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class HKSourceRevision : NSObject, NSSecureCoding, NSCopying {     var source: HKSource { get }     var version: String? { get }     init(source source: HKSource, version version: String)     init() } ``` | NSCopying, NSSecureCoding |

Modified [HKStatistics](https://developer.apple.com/documentation/healthkit/hkstatistics)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKStatistics : NSObject, NSSecureCoding, NSCoding, NSCopying {     var quantityType: HKQuantityType { get }     var startDate: NSDate { get }     var endDate: NSDate { get }     var sources: [HKSource]? { get }     init()     func averageQuantityForSource(_ source: HKSource) -> HKQuantity?     func averageQuantity() -> HKQuantity?     func minimumQuantityForSource(_ source: HKSource) -> HKQuantity?     func minimumQuantity() -> HKQuantity?     func maximumQuantityForSource(_ source: HKSource) -> HKQuantity?     func maximumQuantity() -> HKQuantity?     func sumQuantityForSource(_ source: HKSource) -> HKQuantity?     func sumQuantity() -> HKQuantity? } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class HKStatistics : NSObject, NSSecureCoding, NSCopying {     var quantityType: HKQuantityType { get }     var startDate: NSDate { get }     var endDate: NSDate { get }     var sources: [HKSource]? { get }     init()     func averageQuantityForSource(_ source: HKSource) -> HKQuantity?     func averageQuantity() -> HKQuantity?     func minimumQuantityForSource(_ source: HKSource) -> HKQuantity?     func minimumQuantity() -> HKQuantity?     func maximumQuantityForSource(_ source: HKSource) -> HKQuantity?     func maximumQuantity() -> HKQuantity?     func sumQuantityForSource(_ source: HKSource) -> HKQuantity?     func sumQuantity() -> HKQuantity? } ``` | NSCopying, NSSecureCoding |

Modified [HKStatisticsCollection](https://developer.apple.com/documentation/healthkit/hkstatisticscollection)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HKStatisticsCollectionQuery](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquery)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HKStatisticsQuery](https://developer.apple.com/documentation/healthkit/hkstatisticsquery)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HKUnit](https://developer.apple.com/documentation/healthkit/hkunit)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKUnit : NSObject, NSSecureCoding, NSCoding, NSCopying {     var unitString: String { get }     init()     convenience init(fromString string: String)     class func unitFromString(_ string: String) -> Self     convenience init(fromMassFormatterUnit massFormatterUnit: NSMassFormatterUnit)     class func unitFromMassFormatterUnit(_ massFormatterUnit: NSMassFormatterUnit) -> Self     class func massFormatterUnitFromUnit(_ unit: HKUnit) -> NSMassFormatterUnit     convenience init(fromLengthFormatterUnit lengthFormatterUnit: NSLengthFormatterUnit)     class func unitFromLengthFormatterUnit(_ lengthFormatterUnit: NSLengthFormatterUnit) -> Self     class func lengthFormatterUnitFromUnit(_ unit: HKUnit) -> NSLengthFormatterUnit     convenience init(fromEnergyFormatterUnit energyFormatterUnit: NSEnergyFormatterUnit)     class func unitFromEnergyFormatterUnit(_ energyFormatterUnit: NSEnergyFormatterUnit) -> Self     class func energyFormatterUnitFromUnit(_ unit: HKUnit) -> NSEnergyFormatterUnit     func isNull() -> Bool } extension HKUnit {     class func gramUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func gramUnit() -> Self     class func ounceUnit() -> Self     class func poundUnit() -> Self     class func stoneUnit() -> Self     class func moleUnitWithMetricPrefix(_ prefix: HKMetricPrefix, molarMass gramsPerMole: Double) -> Self     class func moleUnitWithMolarMass(_ gramsPerMole: Double) -> Self } extension HKUnit {     class func meterUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func meterUnit() -> Self     class func inchUnit() -> Self     class func footUnit() -> Self     class func yardUnit() -> Self     class func mileUnit() -> Self } extension HKUnit {     class func literUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func literUnit() -> Self     class func fluidOunceUSUnit() -> Self     class func fluidOunceImperialUnit() -> Self     class func pintUSUnit() -> Self     class func pintImperialUnit() -> Self     class func cupUSUnit() -> Self     class func cupImperialUnit() -> Self } extension HKUnit {     class func pascalUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func pascalUnit() -> Self     class func millimeterOfMercuryUnit() -> Self     class func centimeterOfWaterUnit() -> Self     class func atmosphereUnit() -> Self } extension HKUnit {     class func secondUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func secondUnit() -> Self     class func minuteUnit() -> Self     class func hourUnit() -> Self     class func dayUnit() -> Self } extension HKUnit {     class func jouleUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func jouleUnit() -> Self     class func calorieUnit() -> Self     class func kilocalorieUnit() -> Self } extension HKUnit {     class func degreeCelsiusUnit() -> Self     class func degreeFahrenheitUnit() -> Self     class func kelvinUnit() -> Self } extension HKUnit {     class func siemenUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func siemenUnit() -> Self } extension HKUnit {     class func countUnit() -> Self     class func percentUnit() -> Self } extension HKUnit {     func unitMultipliedByUnit(_ unit: HKUnit) -> HKUnit     func unitDividedByUnit(_ unit: HKUnit) -> HKUnit     func unitRaisedToPower(_ power: Int) -> HKUnit     func reciprocalUnit() -> HKUnit } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class HKUnit : NSObject, NSSecureCoding, NSCopying {     var unitString: String { get }     init()     convenience init(fromString string: String)     class func unitFromString(_ string: String) -> Self     convenience init(fromMassFormatterUnit massFormatterUnit: NSMassFormatterUnit)     class func unitFromMassFormatterUnit(_ massFormatterUnit: NSMassFormatterUnit) -> Self     class func massFormatterUnitFromUnit(_ unit: HKUnit) -> NSMassFormatterUnit     convenience init(fromLengthFormatterUnit lengthFormatterUnit: NSLengthFormatterUnit)     class func unitFromLengthFormatterUnit(_ lengthFormatterUnit: NSLengthFormatterUnit) -> Self     class func lengthFormatterUnitFromUnit(_ unit: HKUnit) -> NSLengthFormatterUnit     convenience init(fromEnergyFormatterUnit energyFormatterUnit: NSEnergyFormatterUnit)     class func unitFromEnergyFormatterUnit(_ energyFormatterUnit: NSEnergyFormatterUnit) -> Self     class func energyFormatterUnitFromUnit(_ unit: HKUnit) -> NSEnergyFormatterUnit     func isNull() -> Bool } extension HKUnit {     class func gramUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func gramUnit() -> Self     class func ounceUnit() -> Self     class func poundUnit() -> Self     class func stoneUnit() -> Self     class func moleUnitWithMetricPrefix(_ prefix: HKMetricPrefix, molarMass gramsPerMole: Double) -> Self     class func moleUnitWithMolarMass(_ gramsPerMole: Double) -> Self } extension HKUnit {     class func meterUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func meterUnit() -> Self     class func inchUnit() -> Self     class func footUnit() -> Self     class func yardUnit() -> Self     class func mileUnit() -> Self } extension HKUnit {     class func literUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func literUnit() -> Self     class func fluidOunceUSUnit() -> Self     class func fluidOunceImperialUnit() -> Self     class func pintUSUnit() -> Self     class func pintImperialUnit() -> Self     class func cupUSUnit() -> Self     class func cupImperialUnit() -> Self } extension HKUnit {     class func pascalUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func pascalUnit() -> Self     class func millimeterOfMercuryUnit() -> Self     class func centimeterOfWaterUnit() -> Self     class func atmosphereUnit() -> Self } extension HKUnit {     class func secondUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func secondUnit() -> Self     class func minuteUnit() -> Self     class func hourUnit() -> Self     class func dayUnit() -> Self } extension HKUnit {     class func jouleUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func jouleUnit() -> Self     class func calorieUnit() -> Self     class func kilocalorieUnit() -> Self } extension HKUnit {     class func degreeCelsiusUnit() -> Self     class func degreeFahrenheitUnit() -> Self     class func kelvinUnit() -> Self } extension HKUnit {     class func siemenUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func siemenUnit() -> Self } extension HKUnit {     class func countUnit() -> Self     class func percentUnit() -> Self } extension HKUnit {     func unitMultipliedByUnit(_ unit: HKUnit) -> HKUnit     func unitDividedByUnit(_ unit: HKUnit) -> HKUnit     func unitRaisedToPower(_ power: Int) -> HKUnit     func reciprocalUnit() -> HKUnit } ``` | NSCopying, NSSecureCoding |

Modified [HKUpdateFrequency [enum]](https://developer.apple.com/documentation/healthkit/hkupdatefrequency)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HKWorkout](https://developer.apple.com/documentation/healthkit/hkworkout)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HKWorkoutActivityType [enum]](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HKWorkoutEvent](https://developer.apple.com/documentation/healthkit/hkworkoutevent)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKWorkoutEvent : NSObject, NSSecureCoding, NSCoding {     var type: HKWorkoutEventType { get }     @NSCopying var date: NSDate { get }     convenience init(type type: HKWorkoutEventType, date date: NSDate)     class func workoutEventWithType(_ type: HKWorkoutEventType, date date: NSDate) -> Self     init() } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class HKWorkoutEvent : NSObject, NSSecureCoding {     var type: HKWorkoutEventType { get }     @NSCopying var date: NSDate { get }     convenience init(type type: HKWorkoutEventType, date date: NSDate)     class func workoutEventWithType(_ type: HKWorkoutEventType, date date: NSDate) -> Self     init() } ``` | NSSecureCoding |

Modified [HKWorkoutEventType [enum]](https://developer.apple.com/documentation/healthkit/hkworkouteventtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HKWorkoutSession](https://developer.apple.com/documentation/healthkit/hkworkoutsession)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKWorkoutSession : NSObject, NSSecureCoding, NSCoding {     var activityType: HKWorkoutActivityType { get }     var locationType: HKWorkoutSessionLocationType { get }     weak var delegate: HKWorkoutSessionDelegate?     var state: HKWorkoutSessionState { get }     var startDate: NSDate? { get }     var endDate: NSDate? { get }     init(activityType activityType: HKWorkoutActivityType, locationType locationType: HKWorkoutSessionLocationType)     init() } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class HKWorkoutSession : NSObject, NSSecureCoding {     var activityType: HKWorkoutActivityType { get }     var locationType: HKWorkoutSessionLocationType { get }     weak var delegate: HKWorkoutSessionDelegate?     var state: HKWorkoutSessionState { get }     var startDate: NSDate? { get }     var endDate: NSDate? { get }     init(activityType activityType: HKWorkoutActivityType, locationType locationType: HKWorkoutSessionLocationType)     init() } ``` | NSSecureCoding |

Modified [HKWorkoutSessionLocationType [enum]](https://developer.apple.com/documentation/healthkit/hkworkoutsessionlocationtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HKWorkoutSessionState [enum]](https://developer.apple.com/documentation/healthkit/hkworkoutsessionstate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HKWorkoutType](https://developer.apple.com/documentation/healthkit/hkworkouttype)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

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
