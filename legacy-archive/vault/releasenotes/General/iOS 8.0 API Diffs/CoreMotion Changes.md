---
title: iOS 8.0 API Diffs
apple_id: TP40014455
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS80APIDiffs/frameworks/CoreMotion.html
archived_at: '2026-07-18T02:55:56.821753Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.0 API Diffs](iOS%207.1%20to%20iOS%208.0%20API%20Differences.md)


# CoreMotion Changes

## CoreMotion

CMAltimeter.h (Added)Added [CMAltimeter](https://developer.apple.com/documentation/coremotion/cmaltimeter)Added [+[CMAltimeter isRelativeAltitudeAvailable]](https://developer.apple.com/documentation/coremotion/cmaltimeter/1616170-isrelativealtitudeavailable)Added [-[CMAltimeter startRelativeAltitudeUpdatesToQueue:withHandler:]](https://developer.apple.com/documentation/coremotion/cmaltimeter/1616004-startrelativealtitudeupdatestoqu)Added [-[CMAltimeter stopRelativeAltitudeUpdates]](https://developer.apple.com/documentation/coremotion/cmaltimeter/1615947-stoprelativealtitudeupdates)Added [CMAltitudeHandler](https://developer.apple.com/documentation/coremotion/cmaltitudehandler)CMAltitude.h (Added)Added [CMAltitudeData](https://developer.apple.com/documentation/coremotion/cmaltitudedata)Added [CMAltitudeData.pressure](https://developer.apple.com/documentation/coremotion/cmaltitudedata/1616152-pressure)Added [CMAltitudeData.relativeAltitude](https://developer.apple.com/documentation/coremotion/cmaltitudedata/1615907-relativealtitude)CMMotionActivity.hAdded [CMMotionActivity.cycling](https://developer.apple.com/documentation/coremotion/cmmotionactivity/1615451-cycling)CMPedometer.h (Added)Added [CMPedometer](https://developer.apple.com/documentation/coremotion/cmpedometer)Added [+[CMPedometer isDistanceAvailable]](https://developer.apple.com/documentation/coremotion/cmpedometer/1613957-isdistanceavailable)Added [+[CMPedometer isFloorCountingAvailable]](https://developer.apple.com/documentation/coremotion/cmpedometer/1613967-isfloorcountingavailable)Added [+[CMPedometer isStepCountingAvailable]](https://developer.apple.com/documentation/coremotion/cmpedometer/1613963-isstepcountingavailable)Added [-[CMPedometer queryPedometerDataFromDate:toDate:withHandler:]](https://developer.apple.com/documentation/coremotion/cmpedometer/1613946-querypedometerdatafromdate)Added [-[CMPedometer startPedometerUpdatesFromDate:withHandler:]](https://developer.apple.com/documentation/coremotion/cmpedometer/1613950-startpedometerupdatesfromdate)Added [-[CMPedometer stopPedometerUpdates]](https://developer.apple.com/documentation/coremotion/cmpedometer/1613973-stoppedometerupdates)Added [CMPedometerData](https://developer.apple.com/documentation/coremotion/cmpedometerdata)Added [CMPedometerData.distance](https://developer.apple.com/documentation/coremotion/cmpedometerdata/1613944-distance)Added [CMPedometerData.endDate](https://developer.apple.com/documentation/coremotion/cmpedometerdata/1613952-enddate)Added [CMPedometerData.floorsAscended](https://developer.apple.com/documentation/coremotion/cmpedometerdata/1613961-floorsascended)Added [CMPedometerData.floorsDescended](https://developer.apple.com/documentation/coremotion/cmpedometerdata/1613940-floorsdescended)Added [CMPedometerData.numberOfSteps](https://developer.apple.com/documentation/coremotion/cmpedometerdata/1613965-numberofsteps)Added [CMPedometerData.startDate](https://developer.apple.com/documentation/coremotion/cmpedometerdata/1613942-startdate)Added [CMPedometerHandler](https://developer.apple.com/documentation/coremotion/cmpedometerhandler)CMStepCounter.hModified [CMStepCounter](https://developer.apple.com/documentation/coremotion/cmstepcounter)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

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
