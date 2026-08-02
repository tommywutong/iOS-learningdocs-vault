---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/GLUT.html
archived_at: '2026-07-18T02:51:24.297410Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# GLUT Changes for Swift

### GLUT

Removed M_PIModified glutBitmap8By13

|  | Declaration |
| --- | --- |
| From | ``` var glutBitmap8By13: UnsafeMutablePointer<Void> ``` |
| To | ``` var glutBitmap8By13: UnsafeMutableRawPointer! ``` |

Modified glutBitmap9By15

|  | Declaration |
| --- | --- |
| From | ``` var glutBitmap9By15: UnsafeMutablePointer<Void> ``` |
| To | ``` var glutBitmap9By15: UnsafeMutableRawPointer! ``` |

Modified glutBitmapHelvetica10

|  | Declaration |
| --- | --- |
| From | ``` var glutBitmapHelvetica10: UnsafeMutablePointer<Void> ``` |
| To | ``` var glutBitmapHelvetica10: UnsafeMutableRawPointer! ``` |

Modified glutBitmapHelvetica12

|  | Declaration |
| --- | --- |
| From | ``` var glutBitmapHelvetica12: UnsafeMutablePointer<Void> ``` |
| To | ``` var glutBitmapHelvetica12: UnsafeMutableRawPointer! ``` |

Modified glutBitmapHelvetica18

|  | Declaration |
| --- | --- |
| From | ``` var glutBitmapHelvetica18: UnsafeMutablePointer<Void> ``` |
| To | ``` var glutBitmapHelvetica18: UnsafeMutableRawPointer! ``` |

Modified glutBitmapTimesRoman10

|  | Declaration |
| --- | --- |
| From | ``` var glutBitmapTimesRoman10: UnsafeMutablePointer<Void> ``` |
| To | ``` var glutBitmapTimesRoman10: UnsafeMutableRawPointer! ``` |

Modified glutBitmapTimesRoman24

|  | Declaration |
| --- | --- |
| From | ``` var glutBitmapTimesRoman24: UnsafeMutablePointer<Void> ``` |
| To | ``` var glutBitmapTimesRoman24: UnsafeMutableRawPointer! ``` |

Modified glutStrokeMonoRoman

|  | Declaration |
| --- | --- |
| From | ``` var glutStrokeMonoRoman: UnsafeMutablePointer<Void> ``` |
| To | ``` var glutStrokeMonoRoman: UnsafeMutableRawPointer! ``` |

Modified glutStrokeRoman

|  | Declaration |
| --- | --- |
| From | ``` var glutStrokeRoman: UnsafeMutablePointer<Void> ``` |
| To | ``` var glutStrokeRoman: UnsafeMutableRawPointer! ``` |

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
