---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Objective-C/XCTest.html
archived_at: '2026-07-18T02:57:28.742812Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# XCTest Changes for Objective-C

### XCTest

#### XCAbstractTest.h

Removed -[XCTest run]

#### XCTestCase+AsynchronousTesting.h

Modified [XCTestExpectation](https://developer.apple.com/documentation/xctest/xctestexpectation)

|  | Header |
| --- | --- |
| From | XCTest/XCTestCase+AsynchronousTesting.h |
| To | XCTest/XCTestExpectation.h |

Modified [-[XCTestExpectation fulfill]](https://developer.apple.com/documentation/xctest/xctestexpectation/1501027-fulfill)

|  | Header |
| --- | --- |
| From | XCTest/XCTestCase+AsynchronousTesting.h |
| To | XCTest/XCTestExpectation.h |

#### XCTestDefines.h

Removed #def XCT_GENERICS_AVAILABLERemoved #def XCT_NULLABLE_AVAILABLE

#### XCTestExpectation.h (Added)

Modified [XCTestExpectation](https://developer.apple.com/documentation/xctest/xctestexpectation)

|  | Header |
| --- | --- |
| From | XCTest/XCTestCase+AsynchronousTesting.h |
| To | XCTest/XCTestExpectation.h |

Modified [-[XCTestExpectation fulfill]](https://developer.apple.com/documentation/xctest/xctestexpectation/1501027-fulfill)

|  | Header |
| --- | --- |
| From | XCTest/XCTestCase+AsynchronousTesting.h |
| To | XCTest/XCTestExpectation.h |

#### XCTestSuite.h

Modified [-[XCTestSuite initWithName:]](https://developer.apple.com/documentation/xctest/xctestsuite/1500579-initwithname)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

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
