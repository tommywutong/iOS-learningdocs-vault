---
title: iOS 9.3 API Diffs
apple_id: TP40016662
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-03-01'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS93APIDiffs/Swift/HealthKit.html
archived_at: '2026-07-18T02:57:15.895419Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.3 API Diffs](iOS%209.2%20to%20iOS%209.3%20API%20Differences.md)


# HealthKit Changes for Swift

### HealthKit

Added [HKActivitySummary](https://developer.apple.com/documentation/healthkit/hkactivitysummary)Added [HKActivitySummary.activeEnergyBurned](https://developer.apple.com/documentation/healthkit/hkactivitysummary/1615772-activeenergyburned)Added [HKActivitySummary.activeEnergyBurnedGoal](https://developer.apple.com/documentation/healthkit/hkactivitysummary/1615291-activeenergyburnedgoal)Added [HKActivitySummary.appleExerciseTime](https://developer.apple.com/documentation/healthkit/hkactivitysummary/1615266-appleexercisetime)Added [HKActivitySummary.appleExerciseTimeGoal](https://developer.apple.com/documentation/healthkit/hkactivitysummary/1615409-appleexercisetimegoal)Added [HKActivitySummary.appleStandHours](https://developer.apple.com/documentation/healthkit/hkactivitysummary/1615636-applestandhours)Added [HKActivitySummary.appleStandHoursGoal](https://developer.apple.com/documentation/healthkit/hkactivitysummary/1615113-applestandhoursgoal)Added [HKActivitySummary.dateComponentsForCalendar(_: NSCalendar) -> NSDateComponents](https://developer.apple.com/documentation/healthkit/hkactivitysummary/1615628-datecomponents)Added [HKActivitySummaryQuery](https://developer.apple.com/documentation/healthkit/hkactivitysummaryquery)Added [HKActivitySummaryQuery.init(predicate: NSPredicate?, resultsHandler: (HKActivitySummaryQuery, [HKActivitySummary]?, NSError?) -> Void)](https://developer.apple.com/documentation/healthkit/hkactivitysummaryquery/1615312-init)Added [HKActivitySummaryQuery.updateHandler](https://developer.apple.com/documentation/healthkit/hkactivitysummaryquery/1615203-updatehandler)Added [HKActivitySummaryType](https://developer.apple.com/documentation/healthkit/hkactivitysummarytype)Added [HKObjectType.activitySummaryType() -> HKActivitySummaryType [class]](https://developer.apple.com/documentation/healthkit/hkobjecttype/1615319-activitysummarytype)Added [HKQuery.objectType](https://developer.apple.com/documentation/healthkit/hkquery/1614768-objecttype)Added [HKQuery.predicateForActivitySummariesBetweenStartDateComponents(_: NSDateComponents, endDateComponents: NSDateComponents) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614777-predicate)Added [HKQuery.predicateForActivitySummaryWithDateComponents(_: NSDateComponents) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614790-predicateforactivitysummarywithd)Added [HKPredicateKeyPathDateComponents](https://developer.apple.com/documentation/healthkit/hkpredicatekeypathdatecomponents)Added [HKQuantityTypeIdentifierAppleExerciseTime](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615696-appleexercisetime)Modified [HKObjectType](https://developer.apple.com/documentation/healthkit/hkobjecttype)

|  | Declaration |
| --- | --- |
| From | ``` class HKObjectType : NSObject, NSSecureCoding, NSCopying {     var identifier: String { get }     init()     class func quantityTypeForIdentifier(_ identifier: String) -> HKQuantityType?     class func categoryTypeForIdentifier(_ identifier: String) -> HKCategoryType?     class func characteristicTypeForIdentifier(_ identifier: String) -> HKCharacteristicType?     class func correlationTypeForIdentifier(_ identifier: String) -> HKCorrelationType?     class func workoutType() -> HKWorkoutType } ``` |
| To | ``` class HKObjectType : NSObject, NSSecureCoding, NSCopying {     var identifier: String { get }     init()     class func quantityTypeForIdentifier(_ identifier: String) -> HKQuantityType?     class func categoryTypeForIdentifier(_ identifier: String) -> HKCategoryType?     class func characteristicTypeForIdentifier(_ identifier: String) -> HKCharacteristicType?     class func correlationTypeForIdentifier(_ identifier: String) -> HKCorrelationType?     class func workoutType() -> HKWorkoutType     class func activitySummaryType() -> HKActivitySummaryType } ``` |

Modified [HKQuery](https://developer.apple.com/documentation/healthkit/hkquery)

|  | Declaration |
| --- | --- |
| From | ``` class HKQuery : NSObject {     var sampleType: HKSampleType { get }     var predicate: NSPredicate? { get }     init() } extension HKQuery {     class func predicateForObjectsWithMetadataKey(_ key: String) -> NSPredicate     class func predicateForObjectsWithMetadataKey(_ key: String, allowedValues allowedValues: [AnyObject]) -> NSPredicate     class func predicateForObjectsWithMetadataKey(_ key: String, operatorType operatorType: NSPredicateOperatorType, value value: AnyObject) -> NSPredicate     class func predicateForObjectsFromSource(_ source: HKSource) -> NSPredicate     class func predicateForObjectsFromSources(_ sources: Set<HKSource>) -> NSPredicate     class func predicateForObjectsFromSourceRevisions(_ sourceRevisions: Set<HKSourceRevision>) -> NSPredicate     class func predicateForObjectsFromDevices(_ devices: Set<HKDevice>) -> NSPredicate     class func predicateForObjectsWithDeviceProperty(_ key: String, allowedValues allowedValues: Set<String>) -> NSPredicate     class func predicateForObjectWithUUID(_ UUID: NSUUID) -> NSPredicate     class func predicateForObjectsWithUUIDs(_ UUIDs: Set<NSUUID>) -> NSPredicate     class func predicateForObjectsWithNoCorrelation() -> NSPredicate     class func predicateForObjectsFromWorkout(_ workout: HKWorkout) -> NSPredicate } extension HKQuery {     class func predicateForSamplesWithStartDate(_ startDate: NSDate?, endDate endDate: NSDate?, options options: HKQueryOptions) -> NSPredicate } extension HKQuery {     class func predicateForQuantitySamplesWithOperatorType(_ operatorType: NSPredicateOperatorType, quantity quantity: HKQuantity) -> NSPredicate } extension HKQuery {     class func predicateForCategorySamplesWithOperatorType(_ operatorType: NSPredicateOperatorType, value value: Int) -> NSPredicate } extension HKQuery {     class func predicateForWorkoutsWithWorkoutActivityType(_ workoutActivityType: HKWorkoutActivityType) -> NSPredicate     class func predicateForWorkoutsWithOperatorType(_ operatorType: NSPredicateOperatorType, duration duration: NSTimeInterval) -> NSPredicate     class func predicateForWorkoutsWithOperatorType(_ operatorType: NSPredicateOperatorType, totalEnergyBurned totalEnergyBurned: HKQuantity) -> NSPredicate     class func predicateForWorkoutsWithOperatorType(_ operatorType: NSPredicateOperatorType, totalDistance totalDistance: HKQuantity) -> NSPredicate } ``` |
| To | ``` class HKQuery : NSObject {     var objectType: HKObjectType? { get }     var sampleType: HKSampleType? { get }     var predicate: NSPredicate? { get }     init() } extension HKQuery {     class func predicateForObjectsWithMetadataKey(_ key: String) -> NSPredicate     class func predicateForObjectsWithMetadataKey(_ key: String, allowedValues allowedValues: [AnyObject]) -> NSPredicate     class func predicateForObjectsWithMetadataKey(_ key: String, operatorType operatorType: NSPredicateOperatorType, value value: AnyObject) -> NSPredicate     class func predicateForObjectsFromSource(_ source: HKSource) -> NSPredicate     class func predicateForObjectsFromSources(_ sources: Set<HKSource>) -> NSPredicate     class func predicateForObjectsFromSourceRevisions(_ sourceRevisions: Set<HKSourceRevision>) -> NSPredicate     class func predicateForObjectsFromDevices(_ devices: Set<HKDevice>) -> NSPredicate     class func predicateForObjectsWithDeviceProperty(_ key: String, allowedValues allowedValues: Set<String>) -> NSPredicate     class func predicateForObjectWithUUID(_ UUID: NSUUID) -> NSPredicate     class func predicateForObjectsWithUUIDs(_ UUIDs: Set<NSUUID>) -> NSPredicate     class func predicateForObjectsWithNoCorrelation() -> NSPredicate     class func predicateForObjectsFromWorkout(_ workout: HKWorkout) -> NSPredicate } extension HKQuery {     class func predicateForSamplesWithStartDate(_ startDate: NSDate?, endDate endDate: NSDate?, options options: HKQueryOptions) -> NSPredicate } extension HKQuery {     class func predicateForQuantitySamplesWithOperatorType(_ operatorType: NSPredicateOperatorType, quantity quantity: HKQuantity) -> NSPredicate } extension HKQuery {     class func predicateForCategorySamplesWithOperatorType(_ operatorType: NSPredicateOperatorType, value value: Int) -> NSPredicate } extension HKQuery {     class func predicateForWorkoutsWithWorkoutActivityType(_ workoutActivityType: HKWorkoutActivityType) -> NSPredicate     class func predicateForWorkoutsWithOperatorType(_ operatorType: NSPredicateOperatorType, duration duration: NSTimeInterval) -> NSPredicate     class func predicateForWorkoutsWithOperatorType(_ operatorType: NSPredicateOperatorType, totalEnergyBurned totalEnergyBurned: HKQuantity) -> NSPredicate     class func predicateForWorkoutsWithOperatorType(_ operatorType: NSPredicateOperatorType, totalDistance totalDistance: HKQuantity) -> NSPredicate } extension HKQuery {     class func predicateForActivitySummaryWithDateComponents(_ dateComponents: NSDateComponents) -> NSPredicate     class func predicateForActivitySummariesBetweenStartDateComponents(_ startDateComponents: NSDateComponents, endDateComponents endDateComponents: NSDateComponents) -> NSPredicate } ``` |

Modified [HKQuery.sampleType](https://developer.apple.com/documentation/healthkit/hkquery/1614789-sampletype)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var sampleType: HKSampleType { get } ``` | -- |
| To | ``` var sampleType: HKSampleType? { get } ``` | iOS 9.3 |

Modified [HKObjectQueryNoLimit](https://developer.apple.com/documentation/healthkit/hkobjectquerynolimit)

|  | Declaration |
| --- | --- |
| From | ``` var HKObjectQueryNoLimit: Int32 { get } ``` |
| To | ``` let HKObjectQueryNoLimit: Int ``` |

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
