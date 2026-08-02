---
title: iOS 9.3 API Diffs
apple_id: TP40016662
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-03-01'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS93APIDiffs/Swift/CoreMotion.html
archived_at: '2026-07-18T02:57:15.417559Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.3 API Diffs](iOS%209.2%20to%20iOS%209.3%20API%20Differences.md)


# CoreMotion Changes for Swift

### CoreMotion

Removed CMSensorRecorder.accelerometerDataFrom(_: NSDate, to: NSDate) -> CMSensorDataList?Removed [CMSensorRecorder.accelerometerDataSince(_: UInt64) -> CMSensorDataList?](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/1804909-accelerometerdatasince)Removed CMSensorRecorder.recordAccelerometerFor(_: NSTimeInterval)Added [CMSensorRecorder.accelerometerDataFromDate(_: NSDate, toDate: NSDate) -> CMSensorDataList?](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/1615937-accelerometerdata)Added [CMSensorRecorder.recordAccelerometerForDuration(_: NSTimeInterval)](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/1615987-recordaccelerometer)Modified [CMSensorRecorder](https://developer.apple.com/documentation/coremotion/cmsensorrecorder)

|  | Declaration |
| --- | --- |
| From | ``` class CMSensorRecorder : NSObject {     class func isAccelerometerRecordingAvailable() -> Bool     class func isAuthorizedForRecording() -> Bool     func accelerometerDataSince(_ identifier: UInt64) -> CMSensorDataList?     func accelerometerDataFrom(_ fromDate: NSDate, to toDate: NSDate) -> CMSensorDataList?     func recordAccelerometerFor(_ duration: NSTimeInterval) } ``` |
| To | ``` class CMSensorRecorder : NSObject {     class func isAccelerometerRecordingAvailable() -> Bool     class func isAuthorizedForRecording() -> Bool     func accelerometerDataFromDate(_ fromDate: NSDate, toDate toDate: NSDate) -> CMSensorDataList?     func recordAccelerometerForDuration(_ duration: NSTimeInterval) } ``` |

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
