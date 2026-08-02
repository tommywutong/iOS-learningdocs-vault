---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/HealthKit.html
archived_at: '2026-07-18T02:56:13.675930Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# HealthKit Changes

## HealthKit

Removed HKQueryOptions.valueRemoved HKStatisticsOptions.valueAdded HKQueryOptions.init(rawValue: UInt)Added HKStatisticsOptions.init(rawValue: UInt)Modified HKAnchoredObjectQuery.init(type: HKSampleType!, predicate: NSPredicate!, anchor: Int, limit: Int, completionHandler:((HKAnchoredObjectQuery!,[AnyObject]!, Int, NSError!) -> Void)!)

|  | Declaration |
| --- | --- |
| From | ``` init(type type: HKSampleType!, predicate predicate: NSPredicate!, anchor anchor: Int, limit limit: Int, completionHandler handler: ((HKAnchoredObjectQuery!, [AnyObject]!, Int, NSError!) -> Void)!) ``` |
| To | ``` init!(type type: HKSampleType!, predicate predicate: NSPredicate!, anchor anchor: Int, limit limit: Int, completionHandler handler: ((HKAnchoredObjectQuery!, [AnyObject]!, Int, NSError!) -> Void)!) ``` |

Modified HKCategorySample.init(type: HKCategoryType!, value: Int, startDate: NSDate!, endDate: NSDate!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(type type: HKCategoryType!, value value: Int, startDate startDate: NSDate!, endDate endDate: NSDate!) ``` |
| To | ``` convenience init!(type type: HKCategoryType!, value value: Int, startDate startDate: NSDate!, endDate endDate: NSDate!) ``` |

Modified HKCategorySample.init(type: HKCategoryType!, value: Int, startDate: NSDate!, endDate: NSDate!, metadata:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(type type: HKCategoryType!, value value: Int, startDate startDate: NSDate!, endDate endDate: NSDate!, metadata metadata: [NSObject : AnyObject]!) ``` |
| To | ``` convenience init!(type type: HKCategoryType!, value value: Int, startDate startDate: NSDate!, endDate endDate: NSDate!, metadata metadata: [NSObject : AnyObject]!) ``` |

Modified HKCorrelation.init(type: HKCorrelationType!, startDate: NSDate!, endDate: NSDate!, objects: NSSet!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(type correlationType: HKCorrelationType!, startDate startDate: NSDate!, endDate endDate: NSDate!, objects objects: NSSet!) ``` |
| To | ``` convenience init!(type correlationType: HKCorrelationType!, startDate startDate: NSDate!, endDate endDate: NSDate!, objects objects: NSSet!) ``` |

Modified HKCorrelation.init(type: HKCorrelationType!, startDate: NSDate!, endDate: NSDate!, objects: NSSet!, metadata:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(type correlationType: HKCorrelationType!, startDate startDate: NSDate!, endDate endDate: NSDate!, objects objects: NSSet!, metadata metadata: [NSObject : AnyObject]!) ``` |
| To | ``` convenience init!(type correlationType: HKCorrelationType!, startDate startDate: NSDate!, endDate endDate: NSDate!, objects objects: NSSet!, metadata metadata: [NSObject : AnyObject]!) ``` |

Modified HKCorrelationQuery.init(type: HKCorrelationType!, predicate: NSPredicate!, samplePredicates:[NSObject: AnyObject]!, completion:((HKCorrelationQuery!,[AnyObject]!, NSError!) -> Void)!)

|  | Declaration |
| --- | --- |
| From | ``` init(type correlationType: HKCorrelationType!, predicate predicate: NSPredicate!, samplePredicates samplePredicates: [NSObject : AnyObject]!, completion completion: ((HKCorrelationQuery!, [AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` init!(type correlationType: HKCorrelationType!, predicate predicate: NSPredicate!, samplePredicates samplePredicates: [NSObject : AnyObject]!, completion completion: ((HKCorrelationQuery!, [AnyObject]!, NSError!) -> Void)!) ``` |

Modified HKObserverQuery.init(sampleType: HKSampleType!, predicate: NSPredicate!, updateHandler:((HKObserverQuery!, HKObserverQueryCompletionHandler!, NSError!) -> Void)!)

|  | Declaration |
| --- | --- |
| From | ``` init(sampleType sampleType: HKSampleType!, predicate predicate: NSPredicate!, updateHandler updateHandler: ((HKObserverQuery!, HKObserverQueryCompletionHandler!, NSError!) -> Void)!) ``` |
| To | ``` init!(sampleType sampleType: HKSampleType!, predicate predicate: NSPredicate!, updateHandler updateHandler: ((HKObserverQuery!, HKObserverQueryCompletionHandler!, NSError!) -> Void)!) ``` |

Modified HKQuantity.init(unit: HKUnit!, doubleValue: Double)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(unit unit: HKUnit!, doubleValue value: Double) ``` |
| To | ``` convenience init!(unit unit: HKUnit!, doubleValue value: Double) ``` |

Modified HKQuantitySample.init(type: HKQuantityType!, quantity: HKQuantity!, startDate: NSDate!, endDate: NSDate!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(type quantityType: HKQuantityType!, quantity quantity: HKQuantity!, startDate startDate: NSDate!, endDate endDate: NSDate!) ``` |
| To | ``` convenience init!(type quantityType: HKQuantityType!, quantity quantity: HKQuantity!, startDate startDate: NSDate!, endDate endDate: NSDate!) ``` |

Modified HKQuantitySample.init(type: HKQuantityType!, quantity: HKQuantity!, startDate: NSDate!, endDate: NSDate!, metadata:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(type quantityType: HKQuantityType!, quantity quantity: HKQuantity!, startDate startDate: NSDate!, endDate endDate: NSDate!, metadata metadata: [NSObject : AnyObject]!) ``` |
| To | ``` convenience init!(type quantityType: HKQuantityType!, quantity quantity: HKQuantity!, startDate startDate: NSDate!, endDate endDate: NSDate!, metadata metadata: [NSObject : AnyObject]!) ``` |

Modified HKQueryOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HKQueryOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var None: HKQueryOptions { get }     static var StrictStartDate: HKQueryOptions { get }     static var StrictEndDate: HKQueryOptions { get } } ``` |
| To | ``` struct HKQueryOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: HKQueryOptions { get }     static var StrictStartDate: HKQueryOptions { get }     static var StrictEndDate: HKQueryOptions { get } } ``` |

Modified HKQueryOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified HKSampleQuery.init(sampleType: HKSampleType!, predicate: NSPredicate!, limit: Int, sortDescriptors:[AnyObject]!, resultsHandler:((HKSampleQuery!,[AnyObject]!, NSError!) -> Void)!)

|  | Declaration |
| --- | --- |
| From | ``` init(sampleType sampleType: HKSampleType!, predicate predicate: NSPredicate!, limit limit: Int, sortDescriptors sortDescriptors: [AnyObject]!, resultsHandler resultsHandler: ((HKSampleQuery!, [AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` init!(sampleType sampleType: HKSampleType!, predicate predicate: NSPredicate!, limit limit: Int, sortDescriptors sortDescriptors: [AnyObject]!, resultsHandler resultsHandler: ((HKSampleQuery!, [AnyObject]!, NSError!) -> Void)!) ``` |

Modified HKSourceQuery.init(sampleType: HKSampleType!, samplePredicate: NSPredicate!, completionHandler:((HKSourceQuery!, NSSet!, NSError!) -> Void)!)

|  | Declaration |
| --- | --- |
| From | ``` init(sampleType sampleType: HKSampleType!, samplePredicate objectPredicate: NSPredicate!, completionHandler completionHandler: ((HKSourceQuery!, NSSet!, NSError!) -> Void)!) ``` |
| To | ``` init!(sampleType sampleType: HKSampleType!, samplePredicate objectPredicate: NSPredicate!, completionHandler completionHandler: ((HKSourceQuery!, NSSet!, NSError!) -> Void)!) ``` |

Modified HKStatisticsCollectionQuery.init(quantityType: HKQuantityType!, quantitySamplePredicate: NSPredicate!, options: HKStatisticsOptions, anchorDate: NSDate!, intervalComponents: NSDateComponents!)

|  | Declaration |
| --- | --- |
| From | ``` init(quantityType quantityType: HKQuantityType!, quantitySamplePredicate quantitySamplePredicate: NSPredicate!, options options: HKStatisticsOptions, anchorDate anchorDate: NSDate!, intervalComponents intervalComponents: NSDateComponents!) ``` |
| To | ``` init!(quantityType quantityType: HKQuantityType!, quantitySamplePredicate quantitySamplePredicate: NSPredicate!, options options: HKStatisticsOptions, anchorDate anchorDate: NSDate!, intervalComponents intervalComponents: NSDateComponents!) ``` |

Modified HKStatisticsOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HKStatisticsOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var None: HKStatisticsOptions { get }     static var SeparateBySource: HKStatisticsOptions { get }     static var DiscreteAverage: HKStatisticsOptions { get }     static var DiscreteMin: HKStatisticsOptions { get }     static var DiscreteMax: HKStatisticsOptions { get }     static var CumulativeSum: HKStatisticsOptions { get } } ``` |
| To | ``` struct HKStatisticsOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: HKStatisticsOptions { get }     static var SeparateBySource: HKStatisticsOptions { get }     static var DiscreteAverage: HKStatisticsOptions { get }     static var DiscreteMin: HKStatisticsOptions { get }     static var DiscreteMax: HKStatisticsOptions { get }     static var CumulativeSum: HKStatisticsOptions { get } } ``` |

Modified HKStatisticsOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified HKStatisticsQuery.init(quantityType: HKQuantityType!, quantitySamplePredicate: NSPredicate!, options: HKStatisticsOptions, completionHandler:((HKStatisticsQuery!, HKStatistics!, NSError!) -> Void)!)

|  | Declaration |
| --- | --- |
| From | ``` init(quantityType quantityType: HKQuantityType!, quantitySamplePredicate quantitySamplePredicate: NSPredicate!, options options: HKStatisticsOptions, completionHandler handler: ((HKStatisticsQuery!, HKStatistics!, NSError!) -> Void)!) ``` |
| To | ``` init!(quantityType quantityType: HKQuantityType!, quantitySamplePredicate quantitySamplePredicate: NSPredicate!, options options: HKStatisticsOptions, completionHandler handler: ((HKStatisticsQuery!, HKStatistics!, NSError!) -> Void)!) ``` |

Modified HKUnit.init(fromEnergyFormatterUnit: NSEnergyFormatterUnit)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(fromEnergyFormatterUnit energyFormatterUnit: NSEnergyFormatterUnit) ``` |
| To | ``` convenience init!(fromEnergyFormatterUnit energyFormatterUnit: NSEnergyFormatterUnit) ``` |

Modified HKUnit.init(fromLengthFormatterUnit: NSLengthFormatterUnit)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(fromLengthFormatterUnit lengthFormatterUnit: NSLengthFormatterUnit) ``` |
| To | ``` convenience init!(fromLengthFormatterUnit lengthFormatterUnit: NSLengthFormatterUnit) ``` |

Modified HKUnit.init(fromMassFormatterUnit: NSMassFormatterUnit)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(fromMassFormatterUnit massFormatterUnit: NSMassFormatterUnit) ``` |
| To | ``` convenience init!(fromMassFormatterUnit massFormatterUnit: NSMassFormatterUnit) ``` |

Modified HKUnit.init(fromString: String!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(fromString string: String!) ``` |
| To | ``` convenience init!(fromString string: String!) ``` |

Modified HKWorkout.init(activityType: HKWorkoutActivityType, startDate: NSDate!, endDate: NSDate!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate!, endDate endDate: NSDate!) ``` |
| To | ``` convenience init!(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate!, endDate endDate: NSDate!) ``` |

Modified HKWorkout.init(activityType: HKWorkoutActivityType, startDate: NSDate!, endDate: NSDate!, duration: NSTimeInterval, totalEnergyBurned: HKQuantity!, totalDistance: HKQuantity!, metadata:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate!, endDate endDate: NSDate!, duration duration: NSTimeInterval, totalEnergyBurned totalEnergyBurned: HKQuantity!, totalDistance totalDistance: HKQuantity!, metadata metadata: [NSObject : AnyObject]!) ``` |
| To | ``` convenience init!(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate!, endDate endDate: NSDate!, duration duration: NSTimeInterval, totalEnergyBurned totalEnergyBurned: HKQuantity!, totalDistance totalDistance: HKQuantity!, metadata metadata: [NSObject : AnyObject]!) ``` |

Modified HKWorkout.init(activityType: HKWorkoutActivityType, startDate: NSDate!, endDate: NSDate!, workoutEvents:[AnyObject]!, totalEnergyBurned: HKQuantity!, totalDistance: HKQuantity!, metadata:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate!, endDate endDate: NSDate!, workoutEvents workoutEvents: [AnyObject]!, totalEnergyBurned totalEnergyBurned: HKQuantity!, totalDistance totalDistance: HKQuantity!, metadata metadata: [NSObject : AnyObject]!) ``` |
| To | ``` convenience init!(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate!, endDate endDate: NSDate!, workoutEvents workoutEvents: [AnyObject]!, totalEnergyBurned totalEnergyBurned: HKQuantity!, totalDistance totalDistance: HKQuantity!, metadata metadata: [NSObject : AnyObject]!) ``` |

Modified HKWorkoutEvent.init(type: HKWorkoutEventType, date: NSDate!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(type type: HKWorkoutEventType, date date: NSDate!) ``` |
| To | ``` convenience init!(type type: HKWorkoutEventType, date date: NSDate!) ``` |

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
