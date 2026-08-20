---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/QTKit.html
archived_at: '2026-07-18T02:52:37.020110Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# QTKit Changes

## QTKit

Removed QTCaptureDevice.init(uniqueID: String!)Added QTTime.init()Added QTTime.init(timeValue: Int64, timeScale: Int, flags: Int)Added QTTimeRange.init()Added QTTimeRange.init(time: QTTime, duration: QTTime)Added MAC_OS_X_VERSION_10_4Added MAC_OS_X_VERSION_10_5Added MAC_OS_X_VERSION_10_6Added MAC_OS_X_VERSION_10_7Modified QTMovieModernizer.destinationURL

|  | Declaration |
| --- | --- |
| From | ``` var destinationURL: NSURL! { get } ``` |
| To | ``` @NSCopying var destinationURL: NSURL! { get } ``` |

Modified QTMovieModernizer.sourceURL

|  | Declaration |
| --- | --- |
| From | ``` var sourceURL: NSURL! { get } ``` |
| To | ``` @NSCopying var sourceURL: NSURL! { get } ``` |

Modified QTMovieModernizer.init(sourceURL: NSURL!, destinationURL: NSURL!)

|  | Declaration |
| --- | --- |
| From | ``` init(sourceURL source: NSURL!, destinationURL destination: NSURL!) ``` |
| To | ``` init!(sourceURL source: NSURL!, destinationURL destination: NSURL!) ``` |

Modified QTTime [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct QTTime {     var timeValue: Int64     var timeScale: Int     var flags: Int } ``` |
| To | ``` struct QTTime {     var timeValue: Int64     var timeScale: Int     var flags: Int     init()     init(timeValue timeValue: Int64, timeScale timeScale: Int, flags flags: Int) } ``` |

Modified QTTimeRange [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct QTTimeRange {     var time: QTTime     var duration: QTTime } ``` |
| To | ``` struct QTTimeRange {     var time: QTTime     var duration: QTTime     init()     init(time time: QTTime, duration duration: QTTime) } ``` |

Modified QTMovieModernizerOutputFormat_AppleProRes422

|  | Declaration |
| --- | --- |
| From | ``` let QTMovieModernizerOutputFormat_AppleProRes422: NSString! ``` |
| To | ``` let QTMovieModernizerOutputFormat_AppleProRes422: String ``` |

Modified QTMovieModernizerOutputFormat_AppleProRes4444

|  | Declaration |
| --- | --- |
| From | ``` let QTMovieModernizerOutputFormat_AppleProRes4444: NSString! ``` |
| To | ``` let QTMovieModernizerOutputFormat_AppleProRes4444: String ``` |

Modified QTMovieModernizerOutputFormat_H264

|  | Declaration |
| --- | --- |
| From | ``` let QTMovieModernizerOutputFormat_H264: NSString! ``` |
| To | ``` let QTMovieModernizerOutputFormat_H264: String ``` |

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
