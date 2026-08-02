---
title: iOS 8.2 API Diffs
apple_id: TP40015021
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS82APIDiffs/modules/HealthKit.html
archived_at: '2026-07-18T02:56:19.361558Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.2 API Diffs](iOS%208.1%20to%20iOS%208.2%20API%20Differences.md)


# HealthKit Changes

## HealthKit

Added HKBiologicalSex.OtherAdded HKHealthStore.preferredUnitsForQuantityTypes(NSSet!, completion:(([NSObject: AnyObject]!, NSError!) -> Void)!)Added HKWorkoutActivityType.OtherAdded HKUserPreferencesDidChangeNotificationModified HKBiologicalSex [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum HKBiologicalSex : Int {     case NotSet     case Female     case Male } ``` |
| To | ``` enum HKBiologicalSex : Int {     case NotSet     case Female     case Male     case Other } ``` |

Modified HKUnit

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSSecureCoding |
| To | AnyObject, NSCoding, NSCopying, NSSecureCoding |

Modified HKWorkoutActivityType [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum HKWorkoutActivityType : UInt {     case AmericanFootball     case Archery     case AustralianFootball     case Badminton     case Baseball     case Basketball     case Bowling     case Boxing     case Climbing     case Cricket     case CrossTraining     case Curling     case Cycling     case Dance     case DanceInspiredTraining     case Elliptical     case EquestrianSports     case Fencing     case Fishing     case FunctionalStrengthTraining     case Golf     case Gymnastics     case Handball     case Hiking     case Hockey     case Hunting     case Lacrosse     case MartialArts     case MindAndBody     case MixedMetabolicCardioTraining     case PaddleSports     case Play     case PreparationAndRecovery     case Racquetball     case Rowing     case Rugby     case Running     case Sailing     case SkatingSports     case SnowSports     case Soccer     case Softball     case Squash     case StairClimbing     case SurfingSports     case Swimming     case TableTennis     case Tennis     case TrackAndField     case TraditionalStrengthTraining     case Volleyball     case Walking     case WaterFitness     case WaterPolo     case WaterSports     case Wrestling     case Yoga } ``` |
| To | ``` enum HKWorkoutActivityType : UInt {     case AmericanFootball     case Archery     case AustralianFootball     case Badminton     case Baseball     case Basketball     case Bowling     case Boxing     case Climbing     case Cricket     case CrossTraining     case Curling     case Cycling     case Dance     case DanceInspiredTraining     case Elliptical     case EquestrianSports     case Fencing     case Fishing     case FunctionalStrengthTraining     case Golf     case Gymnastics     case Handball     case Hiking     case Hockey     case Hunting     case Lacrosse     case MartialArts     case MindAndBody     case MixedMetabolicCardioTraining     case PaddleSports     case Play     case PreparationAndRecovery     case Racquetball     case Rowing     case Rugby     case Running     case Sailing     case SkatingSports     case SnowSports     case Soccer     case Softball     case Squash     case StairClimbing     case SurfingSports     case Swimming     case TableTennis     case Tennis     case TrackAndField     case TraditionalStrengthTraining     case Volleyball     case Walking     case WaterFitness     case WaterPolo     case WaterSports     case Wrestling     case Yoga     case Other } ``` |

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
