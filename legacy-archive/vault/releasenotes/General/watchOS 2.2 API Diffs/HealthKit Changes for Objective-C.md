---
title: watchOS 2.2 API Diffs
apple_id: TP40016663
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS22APIDiffs/Objective-C/HealthKit.html
archived_at: '2026-07-18T02:58:09.952562Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 2.2 API Diffs](watchOS%202.1%20to%20watchOS%202.2%20API%20Differences.md)


# HealthKit Changes for Objective-C

### HealthKit

#### HKActivitySummary.h (Added)

Added [HKActivitySummary](https://developer.apple.com/documentation/healthkit/hkactivitysummary)Added [HKActivitySummary.activeEnergyBurned](https://developer.apple.com/documentation/healthkit/hkactivitysummary/1615772-activeenergyburned)Added [HKActivitySummary.activeEnergyBurnedGoal](https://developer.apple.com/documentation/healthkit/hkactivitysummary/1615291-activeenergyburnedgoal)Added [HKActivitySummary.appleExerciseTime](https://developer.apple.com/documentation/healthkit/hkactivitysummary/1615266-appleexercisetime)Added [HKActivitySummary.appleExerciseTimeGoal](https://developer.apple.com/documentation/healthkit/hkactivitysummary/1615409-appleexercisetimegoal)Added [HKActivitySummary.appleStandHours](https://developer.apple.com/documentation/healthkit/hkactivitysummary/1615636-applestandhours)Added [HKActivitySummary.appleStandHoursGoal](https://developer.apple.com/documentation/healthkit/hkactivitysummary/1615113-applestandhoursgoal)Added [-[HKActivitySummary dateComponentsForCalendar:]](https://developer.apple.com/documentation/healthkit/hkactivitysummary/1615628-datecomponentsforcalendar)Added [HKPredicateKeyPathDateComponents](https://developer.apple.com/documentation/healthkit/hkpredicatekeypathdatecomponents)

#### HKActivitySummaryQuery.h (Added)

Added [HKActivitySummaryQuery](https://developer.apple.com/documentation/healthkit/hkactivitysummaryquery)Added [-[HKActivitySummaryQuery initWithPredicate:resultsHandler:]](https://developer.apple.com/documentation/healthkit/hkactivitysummaryquery/1615312-init)Added [HKActivitySummaryQuery.updateHandler](https://developer.apple.com/documentation/healthkit/hkactivitysummaryquery/1615203-updatehandler)

#### HKDefines.h

Added #def HK_AVAILABLE_IOS_WATCHOSAdded #def HK_CLASS_AVAILABLE_IOS_WATCHOSAdded #def HK_ENUM_AVAILABLE_IOS_WATCHOS

#### HKObjectType.h

Added [HKActivitySummaryType](https://developer.apple.com/documentation/healthkit/hkactivitysummarytype)Added [+[HKObjectType activitySummaryType]](https://developer.apple.com/documentation/healthkit/hkobjecttype/1615319-activitysummarytype)

#### HKQuery.h

Added [HKQuery.objectType](https://developer.apple.com/documentation/healthkit/hkquery/1614768-objecttype)Added [+[HKQuery predicateForActivitySummariesBetweenStartDateComponents:endDateComponents:]](https://developer.apple.com/documentation/healthkit/hkquery/1614777-predicateforactivitysummariesbet)Added [+[HKQuery predicateForActivitySummaryWithDateComponents:]](https://developer.apple.com/documentation/healthkit/hkquery/1614790-predicateforactivitysummary)Added HKQuery(HKActivitySummaryPredicates)Modified [HKQuery.sampleType](https://developer.apple.com/documentation/healthkit/hkquery/1614789-sampletype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 2.2 |

#### HKSampleQuery.h

Removed #def HKObjectQueryNoLimitAdded [HKObjectQueryNoLimit](https://developer.apple.com/documentation/healthkit/hkobjectquerynolimit)

#### HKTypeIdentifiers.h

Added [HKQuantityTypeIdentifierAppleExerciseTime](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierappleexercisetime)

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
