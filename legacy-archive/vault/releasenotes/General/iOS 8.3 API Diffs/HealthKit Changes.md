---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/HealthKit.html
archived_at: '2026-07-18T02:56:25.747282Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# HealthKit Changes

## HealthKit

Modified HKCorrelation.objects

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var objects: NSSet! { get } ``` |
| To | ``` var objects: Set<NSObject>! { get } ``` |

Modified HKCorrelation.objectsForType(HKObjectType!) -> Set<NSObject>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objectsForType(_ objectType: HKObjectType!) -> NSSet! ``` | iOS 8.0 |
| To | ``` func objectsForType(_ objectType: HKObjectType!) -> Set<NSObject>! ``` | iOS 8.3 |

Modified HKCorrelation.init(type: HKCorrelationType!, startDate: NSDate!, endDate: NSDate!, objects: Set<NSObject>!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` convenience init!(type correlationType: HKCorrelationType!, startDate startDate: NSDate!, endDate endDate: NSDate!, objects objects: NSSet!) ``` | iOS 8.0 |
| To | ``` convenience init!(type correlationType: HKCorrelationType!, startDate startDate: NSDate!, endDate endDate: NSDate!, objects objects: Set<NSObject>!) ``` | iOS 8.3 |

Modified HKCorrelation.init(type: HKCorrelationType!, startDate: NSDate!, endDate: NSDate!, objects: Set<NSObject>!, metadata:[NSObject: AnyObject]!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` convenience init!(type correlationType: HKCorrelationType!, startDate startDate: NSDate!, endDate endDate: NSDate!, objects objects: NSSet!, metadata metadata: [NSObject : AnyObject]!) ``` | iOS 8.0 |
| To | ``` convenience init!(type correlationType: HKCorrelationType!, startDate startDate: NSDate!, endDate endDate: NSDate!, objects objects: Set<NSObject>!, metadata metadata: [NSObject : AnyObject]!) ``` | iOS 8.3 |

Modified HKHealthStore.biologicalSexWithError(NSErrorPointer) -> HKBiologicalSexObject?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func biologicalSexWithError(_ error: NSErrorPointer) -> HKBiologicalSexObject! ``` | iOS 8.0 |
| To | ``` func biologicalSexWithError(_ error: NSErrorPointer) -> HKBiologicalSexObject? ``` | iOS 8.3 |

Modified HKHealthStore.bloodTypeWithError(NSErrorPointer) -> HKBloodTypeObject?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func bloodTypeWithError(_ error: NSErrorPointer) -> HKBloodTypeObject! ``` | iOS 8.0 |
| To | ``` func bloodTypeWithError(_ error: NSErrorPointer) -> HKBloodTypeObject? ``` | iOS 8.3 |

Modified HKHealthStore.dateOfBirthWithError(NSErrorPointer) -> NSDate?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func dateOfBirthWithError(_ error: NSErrorPointer) -> NSDate! ``` | iOS 8.0 |
| To | ``` func dateOfBirthWithError(_ error: NSErrorPointer) -> NSDate? ``` | iOS 8.3 |

Modified HKHealthStore.preferredUnitsForQuantityTypes(Set<NSObject>!, completion:(([NSObject: AnyObject]!, NSError!) -> Void)!)

|  | Declaration |
| --- | --- |
| From | ``` func preferredUnitsForQuantityTypes(_ quantityTypes: NSSet!, completion completion: (([NSObject : AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` func preferredUnitsForQuantityTypes(_ quantityTypes: Set<NSObject>!, completion completion: (([NSObject : AnyObject]!, NSError!) -> Void)!) ``` |

Modified HKHealthStore.requestAuthorizationToShareTypes(Set<NSObject>!, readTypes: Set<NSObject>!, completion:((Bool, NSError!) -> Void)!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func requestAuthorizationToShareTypes(_ typesToShare: NSSet!, readTypes typesToRead: NSSet!, completion completion: ((Bool, NSError!) -> Void)!) ``` | iOS 8.0 |
| To | ``` func requestAuthorizationToShareTypes(_ typesToShare: Set<NSObject>!, readTypes typesToRead: Set<NSObject>!, completion completion: ((Bool, NSError!) -> Void)!) ``` | iOS 8.3 |

Modified HKQuantity.compare(HKQuantity) -> NSComparisonResult

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func compare(_ quantity: HKQuantity!) -> NSComparisonResult ``` | iOS 8.0 |
| To | ``` func compare(_ quantity: HKQuantity) -> NSComparisonResult ``` | iOS 8.3 |

Modified HKQuery.predicateForObjectsFromSources(Set<NSObject>!) -> NSPredicate! [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func predicateForObjectsFromSources(_ sources: NSSet!) -> NSPredicate! ``` | iOS 8.0 |
| To | ``` class func predicateForObjectsFromSources(_ sources: Set<NSObject>!) -> NSPredicate! ``` | iOS 8.3 |

Modified HKQuery.predicateForObjectsWithUUIDs(Set<NSObject>!) -> NSPredicate! [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func predicateForObjectsWithUUIDs(_ UUIDs: NSSet!) -> NSPredicate! ``` | iOS 8.0 |
| To | ``` class func predicateForObjectsWithUUIDs(_ UUIDs: Set<NSObject>!) -> NSPredicate! ``` | iOS 8.3 |

Modified HKSourceQuery.init(sampleType: HKSampleType!, samplePredicate: NSPredicate!, completionHandler:((HKSourceQuery!, Set<NSObject>!, NSError!) -> Void)!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init!(sampleType sampleType: HKSampleType!, samplePredicate objectPredicate: NSPredicate!, completionHandler completionHandler: ((HKSourceQuery!, NSSet!, NSError!) -> Void)!) ``` | iOS 8.0 |
| To | ``` init!(sampleType sampleType: HKSampleType!, samplePredicate objectPredicate: NSPredicate!, completionHandler completionHandler: ((HKSourceQuery!, Set<NSObject>!, NSError!) -> Void)!) ``` | iOS 8.3 |

Modified HKStatisticsCollection.sources() -> Set<NSObject>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func sources() -> NSSet! ``` | iOS 8.0 |
| To | ``` func sources() -> Set<NSObject>! ``` | iOS 8.3 |

Modified HKCategoryTypeIdentifierSleepAnalysis

|  | Declaration |
| --- | --- |
| From | ``` let HKCategoryTypeIdentifierSleepAnalysis: NSString! ``` |
| To | ``` let HKCategoryTypeIdentifierSleepAnalysis: String ``` |

Modified HKCharacteristicTypeIdentifierBiologicalSex

|  | Declaration |
| --- | --- |
| From | ``` let HKCharacteristicTypeIdentifierBiologicalSex: NSString! ``` |
| To | ``` let HKCharacteristicTypeIdentifierBiologicalSex: String ``` |

Modified HKCharacteristicTypeIdentifierBloodType

|  | Declaration |
| --- | --- |
| From | ``` let HKCharacteristicTypeIdentifierBloodType: NSString! ``` |
| To | ``` let HKCharacteristicTypeIdentifierBloodType: String ``` |

Modified HKCharacteristicTypeIdentifierDateOfBirth

|  | Declaration |
| --- | --- |
| From | ``` let HKCharacteristicTypeIdentifierDateOfBirth: NSString! ``` |
| To | ``` let HKCharacteristicTypeIdentifierDateOfBirth: String ``` |

Modified HKCorrelationTypeIdentifierBloodPressure

|  | Declaration |
| --- | --- |
| From | ``` let HKCorrelationTypeIdentifierBloodPressure: NSString! ``` |
| To | ``` let HKCorrelationTypeIdentifierBloodPressure: String ``` |

Modified HKCorrelationTypeIdentifierFood

|  | Declaration |
| --- | --- |
| From | ``` let HKCorrelationTypeIdentifierFood: NSString! ``` |
| To | ``` let HKCorrelationTypeIdentifierFood: String ``` |

Modified HKErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let HKErrorDomain: NSString! ``` |
| To | ``` let HKErrorDomain: String ``` |

Modified HKMetadataKeyBodyTemperatureSensorLocation

|  | Declaration |
| --- | --- |
| From | ``` let HKMetadataKeyBodyTemperatureSensorLocation: NSString! ``` |
| To | ``` let HKMetadataKeyBodyTemperatureSensorLocation: String ``` |

Modified HKMetadataKeyCoachedWorkout

|  | Declaration |
| --- | --- |
| From | ``` let HKMetadataKeyCoachedWorkout: NSString! ``` |
| To | ``` let HKMetadataKeyCoachedWorkout: String ``` |

Modified HKMetadataKeyDeviceManufacturerName

|  | Declaration |
| --- | --- |
| From | ``` let HKMetadataKeyDeviceManufacturerName: NSString! ``` |
| To | ``` let HKMetadataKeyDeviceManufacturerName: String ``` |

Modified HKMetadataKeyDeviceName

|  | Declaration |
| --- | --- |
| From | ``` let HKMetadataKeyDeviceName: NSString! ``` |
| To | ``` let HKMetadataKeyDeviceName: String ``` |

Modified HKMetadataKeyDeviceSerialNumber

|  | Declaration |
| --- | --- |
| From | ``` let HKMetadataKeyDeviceSerialNumber: NSString! ``` |
| To | ``` let HKMetadataKeyDeviceSerialNumber: String ``` |

Modified HKMetadataKeyDigitalSignature

|  | Declaration |
| --- | --- |
| From | ``` let HKMetadataKeyDigitalSignature: NSString! ``` |
| To | ``` let HKMetadataKeyDigitalSignature: String ``` |

Modified HKMetadataKeyExternalUUID

|  | Declaration |
| --- | --- |
| From | ``` let HKMetadataKeyExternalUUID: NSString! ``` |
| To | ``` let HKMetadataKeyExternalUUID: String ``` |

Modified HKMetadataKeyFoodType

|  | Declaration |
| --- | --- |
| From | ``` let HKMetadataKeyFoodType: NSString! ``` |
| To | ``` let HKMetadataKeyFoodType: String ``` |

Modified HKMetadataKeyGroupFitness

|  | Declaration |
| --- | --- |
| From | ``` let HKMetadataKeyGroupFitness: NSString! ``` |
| To | ``` let HKMetadataKeyGroupFitness: String ``` |

Modified HKMetadataKeyHeartRateSensorLocation

|  | Declaration |
| --- | --- |
| From | ``` let HKMetadataKeyHeartRateSensorLocation: NSString! ``` |
| To | ``` let HKMetadataKeyHeartRateSensorLocation: String ``` |

Modified HKMetadataKeyIndoorWorkout

|  | Declaration |
| --- | --- |
| From | ``` let HKMetadataKeyIndoorWorkout: NSString! ``` |
| To | ``` let HKMetadataKeyIndoorWorkout: String ``` |

Modified HKMetadataKeyReferenceRangeLowerLimit

|  | Declaration |
| --- | --- |
| From | ``` let HKMetadataKeyReferenceRangeLowerLimit: NSString! ``` |
| To | ``` let HKMetadataKeyReferenceRangeLowerLimit: String ``` |

Modified HKMetadataKeyReferenceRangeUpperLimit

|  | Declaration |
| --- | --- |
| From | ``` let HKMetadataKeyReferenceRangeUpperLimit: NSString! ``` |
| To | ``` let HKMetadataKeyReferenceRangeUpperLimit: String ``` |

Modified HKMetadataKeyTimeZone

|  | Declaration |
| --- | --- |
| From | ``` let HKMetadataKeyTimeZone: NSString! ``` |
| To | ``` let HKMetadataKeyTimeZone: String ``` |

Modified HKMetadataKeyUDIDeviceIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let HKMetadataKeyUDIDeviceIdentifier: NSString! ``` |
| To | ``` let HKMetadataKeyUDIDeviceIdentifier: String ``` |

Modified HKMetadataKeyUDIProductionIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let HKMetadataKeyUDIProductionIdentifier: NSString! ``` |
| To | ``` let HKMetadataKeyUDIProductionIdentifier: String ``` |

Modified HKMetadataKeyWasTakenInLab

|  | Declaration |
| --- | --- |
| From | ``` let HKMetadataKeyWasTakenInLab: NSString! ``` |
| To | ``` let HKMetadataKeyWasTakenInLab: String ``` |

Modified HKMetadataKeyWasUserEntered

|  | Declaration |
| --- | --- |
| From | ``` let HKMetadataKeyWasUserEntered: NSString! ``` |
| To | ``` let HKMetadataKeyWasUserEntered: String ``` |

Modified HKMetadataKeyWorkoutBrandName

|  | Declaration |
| --- | --- |
| From | ``` let HKMetadataKeyWorkoutBrandName: NSString! ``` |
| To | ``` let HKMetadataKeyWorkoutBrandName: String ``` |

Modified HKPredicateKeyPathCategoryValue

|  | Declaration |
| --- | --- |
| From | ``` let HKPredicateKeyPathCategoryValue: NSString! ``` |
| To | ``` let HKPredicateKeyPathCategoryValue: String ``` |

Modified HKPredicateKeyPathCorrelation

|  | Declaration |
| --- | --- |
| From | ``` let HKPredicateKeyPathCorrelation: NSString! ``` |
| To | ``` let HKPredicateKeyPathCorrelation: String ``` |

Modified HKPredicateKeyPathEndDate

|  | Declaration |
| --- | --- |
| From | ``` let HKPredicateKeyPathEndDate: NSString! ``` |
| To | ``` let HKPredicateKeyPathEndDate: String ``` |

Modified HKPredicateKeyPathMetadata

|  | Declaration |
| --- | --- |
| From | ``` let HKPredicateKeyPathMetadata: NSString! ``` |
| To | ``` let HKPredicateKeyPathMetadata: String ``` |

Modified HKPredicateKeyPathQuantity

|  | Declaration |
| --- | --- |
| From | ``` let HKPredicateKeyPathQuantity: NSString! ``` |
| To | ``` let HKPredicateKeyPathQuantity: String ``` |

Modified HKPredicateKeyPathSource

|  | Declaration |
| --- | --- |
| From | ``` let HKPredicateKeyPathSource: NSString! ``` |
| To | ``` let HKPredicateKeyPathSource: String ``` |

Modified HKPredicateKeyPathStartDate

|  | Declaration |
| --- | --- |
| From | ``` let HKPredicateKeyPathStartDate: NSString! ``` |
| To | ``` let HKPredicateKeyPathStartDate: String ``` |

Modified HKPredicateKeyPathUUID

|  | Declaration |
| --- | --- |
| From | ``` let HKPredicateKeyPathUUID: NSString! ``` |
| To | ``` let HKPredicateKeyPathUUID: String ``` |

Modified HKPredicateKeyPathWorkout

|  | Declaration |
| --- | --- |
| From | ``` let HKPredicateKeyPathWorkout: NSString! ``` |
| To | ``` let HKPredicateKeyPathWorkout: String ``` |

Modified HKPredicateKeyPathWorkoutDuration

|  | Declaration |
| --- | --- |
| From | ``` let HKPredicateKeyPathWorkoutDuration: NSString! ``` |
| To | ``` let HKPredicateKeyPathWorkoutDuration: String ``` |

Modified HKPredicateKeyPathWorkoutTotalDistance

|  | Declaration |
| --- | --- |
| From | ``` let HKPredicateKeyPathWorkoutTotalDistance: NSString! ``` |
| To | ``` let HKPredicateKeyPathWorkoutTotalDistance: String ``` |

Modified HKPredicateKeyPathWorkoutTotalEnergyBurned

|  | Declaration |
| --- | --- |
| From | ``` let HKPredicateKeyPathWorkoutTotalEnergyBurned: NSString! ``` |
| To | ``` let HKPredicateKeyPathWorkoutTotalEnergyBurned: String ``` |

Modified HKPredicateKeyPathWorkoutType

|  | Declaration |
| --- | --- |
| From | ``` let HKPredicateKeyPathWorkoutType: NSString! ``` |
| To | ``` let HKPredicateKeyPathWorkoutType: String ``` |

Modified HKQuantityTypeIdentifierActiveEnergyBurned

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierActiveEnergyBurned: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierActiveEnergyBurned: String ``` |

Modified HKQuantityTypeIdentifierBasalEnergyBurned

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierBasalEnergyBurned: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierBasalEnergyBurned: String ``` |

Modified HKQuantityTypeIdentifierBloodAlcoholContent

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierBloodAlcoholContent: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierBloodAlcoholContent: String ``` |

Modified HKQuantityTypeIdentifierBloodGlucose

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierBloodGlucose: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierBloodGlucose: String ``` |

Modified HKQuantityTypeIdentifierBloodPressureDiastolic

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierBloodPressureDiastolic: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierBloodPressureDiastolic: String ``` |

Modified HKQuantityTypeIdentifierBloodPressureSystolic

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierBloodPressureSystolic: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierBloodPressureSystolic: String ``` |

Modified HKQuantityTypeIdentifierBodyFatPercentage

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierBodyFatPercentage: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierBodyFatPercentage: String ``` |

Modified HKQuantityTypeIdentifierBodyMass

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierBodyMass: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierBodyMass: String ``` |

Modified HKQuantityTypeIdentifierBodyMassIndex

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierBodyMassIndex: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierBodyMassIndex: String ``` |

Modified HKQuantityTypeIdentifierBodyTemperature

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierBodyTemperature: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierBodyTemperature: String ``` |

Modified HKQuantityTypeIdentifierDietaryBiotin

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryBiotin: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryBiotin: String ``` |

Modified HKQuantityTypeIdentifierDietaryCaffeine

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryCaffeine: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryCaffeine: String ``` |

Modified HKQuantityTypeIdentifierDietaryCalcium

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryCalcium: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryCalcium: String ``` |

Modified HKQuantityTypeIdentifierDietaryCarbohydrates

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryCarbohydrates: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryCarbohydrates: String ``` |

Modified HKQuantityTypeIdentifierDietaryChloride

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryChloride: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryChloride: String ``` |

Modified HKQuantityTypeIdentifierDietaryCholesterol

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryCholesterol: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryCholesterol: String ``` |

Modified HKQuantityTypeIdentifierDietaryChromium

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryChromium: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryChromium: String ``` |

Modified HKQuantityTypeIdentifierDietaryCopper

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryCopper: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryCopper: String ``` |

Modified HKQuantityTypeIdentifierDietaryEnergyConsumed

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryEnergyConsumed: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryEnergyConsumed: String ``` |

Modified HKQuantityTypeIdentifierDietaryFatMonounsaturated

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryFatMonounsaturated: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryFatMonounsaturated: String ``` |

Modified HKQuantityTypeIdentifierDietaryFatPolyunsaturated

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryFatPolyunsaturated: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryFatPolyunsaturated: String ``` |

Modified HKQuantityTypeIdentifierDietaryFatSaturated

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryFatSaturated: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryFatSaturated: String ``` |

Modified HKQuantityTypeIdentifierDietaryFatTotal

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryFatTotal: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryFatTotal: String ``` |

Modified HKQuantityTypeIdentifierDietaryFiber

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryFiber: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryFiber: String ``` |

Modified HKQuantityTypeIdentifierDietaryFolate

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryFolate: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryFolate: String ``` |

Modified HKQuantityTypeIdentifierDietaryIodine

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryIodine: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryIodine: String ``` |

Modified HKQuantityTypeIdentifierDietaryIron

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryIron: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryIron: String ``` |

Modified HKQuantityTypeIdentifierDietaryMagnesium

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryMagnesium: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryMagnesium: String ``` |

Modified HKQuantityTypeIdentifierDietaryManganese

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryManganese: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryManganese: String ``` |

Modified HKQuantityTypeIdentifierDietaryMolybdenum

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryMolybdenum: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryMolybdenum: String ``` |

Modified HKQuantityTypeIdentifierDietaryNiacin

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryNiacin: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryNiacin: String ``` |

Modified HKQuantityTypeIdentifierDietaryPantothenicAcid

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryPantothenicAcid: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryPantothenicAcid: String ``` |

Modified HKQuantityTypeIdentifierDietaryPhosphorus

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryPhosphorus: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryPhosphorus: String ``` |

Modified HKQuantityTypeIdentifierDietaryPotassium

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryPotassium: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryPotassium: String ``` |

Modified HKQuantityTypeIdentifierDietaryProtein

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryProtein: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryProtein: String ``` |

Modified HKQuantityTypeIdentifierDietaryRiboflavin

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryRiboflavin: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryRiboflavin: String ``` |

Modified HKQuantityTypeIdentifierDietarySelenium

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietarySelenium: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietarySelenium: String ``` |

Modified HKQuantityTypeIdentifierDietarySodium

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietarySodium: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietarySodium: String ``` |

Modified HKQuantityTypeIdentifierDietarySugar

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietarySugar: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietarySugar: String ``` |

Modified HKQuantityTypeIdentifierDietaryThiamin

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryThiamin: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryThiamin: String ``` |

Modified HKQuantityTypeIdentifierDietaryVitaminA

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryVitaminA: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryVitaminA: String ``` |

Modified HKQuantityTypeIdentifierDietaryVitaminB12

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryVitaminB12: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryVitaminB12: String ``` |

Modified HKQuantityTypeIdentifierDietaryVitaminB6

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryVitaminB6: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryVitaminB6: String ``` |

Modified HKQuantityTypeIdentifierDietaryVitaminC

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryVitaminC: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryVitaminC: String ``` |

Modified HKQuantityTypeIdentifierDietaryVitaminD

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryVitaminD: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryVitaminD: String ``` |

Modified HKQuantityTypeIdentifierDietaryVitaminE

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryVitaminE: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryVitaminE: String ``` |

Modified HKQuantityTypeIdentifierDietaryVitaminK

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryVitaminK: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryVitaminK: String ``` |

Modified HKQuantityTypeIdentifierDietaryZinc

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDietaryZinc: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDietaryZinc: String ``` |

Modified HKQuantityTypeIdentifierDistanceCycling

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDistanceCycling: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDistanceCycling: String ``` |

Modified HKQuantityTypeIdentifierDistanceWalkingRunning

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierDistanceWalkingRunning: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierDistanceWalkingRunning: String ``` |

Modified HKQuantityTypeIdentifierElectrodermalActivity

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierElectrodermalActivity: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierElectrodermalActivity: String ``` |

Modified HKQuantityTypeIdentifierFlightsClimbed

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierFlightsClimbed: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierFlightsClimbed: String ``` |

Modified HKQuantityTypeIdentifierForcedExpiratoryVolume1

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierForcedExpiratoryVolume1: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierForcedExpiratoryVolume1: String ``` |

Modified HKQuantityTypeIdentifierForcedVitalCapacity

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierForcedVitalCapacity: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierForcedVitalCapacity: String ``` |

Modified HKQuantityTypeIdentifierHeartRate

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierHeartRate: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierHeartRate: String ``` |

Modified HKQuantityTypeIdentifierHeight

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierHeight: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierHeight: String ``` |

Modified HKQuantityTypeIdentifierInhalerUsage

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierInhalerUsage: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierInhalerUsage: String ``` |

Modified HKQuantityTypeIdentifierLeanBodyMass

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierLeanBodyMass: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierLeanBodyMass: String ``` |

Modified HKQuantityTypeIdentifierNikeFuel

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierNikeFuel: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierNikeFuel: String ``` |

Modified HKQuantityTypeIdentifierNumberOfTimesFallen

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierNumberOfTimesFallen: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierNumberOfTimesFallen: String ``` |

Modified HKQuantityTypeIdentifierOxygenSaturation

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierOxygenSaturation: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierOxygenSaturation: String ``` |

Modified HKQuantityTypeIdentifierPeakExpiratoryFlowRate

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierPeakExpiratoryFlowRate: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierPeakExpiratoryFlowRate: String ``` |

Modified HKQuantityTypeIdentifierPeripheralPerfusionIndex

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierPeripheralPerfusionIndex: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierPeripheralPerfusionIndex: String ``` |

Modified HKQuantityTypeIdentifierRespiratoryRate

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierRespiratoryRate: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierRespiratoryRate: String ``` |

Modified HKQuantityTypeIdentifierStepCount

|  | Declaration |
| --- | --- |
| From | ``` let HKQuantityTypeIdentifierStepCount: NSString! ``` |
| To | ``` let HKQuantityTypeIdentifierStepCount: String ``` |

Modified HKSampleSortIdentifierEndDate

|  | Declaration |
| --- | --- |
| From | ``` let HKSampleSortIdentifierEndDate: NSString! ``` |
| To | ``` let HKSampleSortIdentifierEndDate: String ``` |

Modified HKSampleSortIdentifierStartDate

|  | Declaration |
| --- | --- |
| From | ``` let HKSampleSortIdentifierStartDate: NSString! ``` |
| To | ``` let HKSampleSortIdentifierStartDate: String ``` |

Modified HKUserPreferencesDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let HKUserPreferencesDidChangeNotification: NSString! ``` |
| To | ``` let HKUserPreferencesDidChangeNotification: String ``` |

Modified HKWorkoutSortIdentifierDuration

|  | Declaration |
| --- | --- |
| From | ``` let HKWorkoutSortIdentifierDuration: NSString! ``` |
| To | ``` let HKWorkoutSortIdentifierDuration: String ``` |

Modified HKWorkoutSortIdentifierTotalDistance

|  | Declaration |
| --- | --- |
| From | ``` let HKWorkoutSortIdentifierTotalDistance: NSString! ``` |
| To | ``` let HKWorkoutSortIdentifierTotalDistance: String ``` |

Modified HKWorkoutSortIdentifierTotalEnergyBurned

|  | Declaration |
| --- | --- |
| From | ``` let HKWorkoutSortIdentifierTotalEnergyBurned: NSString! ``` |
| To | ``` let HKWorkoutSortIdentifierTotalEnergyBurned: String ``` |

Modified HKWorkoutTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let HKWorkoutTypeIdentifier: NSString! ``` |
| To | ``` let HKWorkoutTypeIdentifier: String ``` |

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
