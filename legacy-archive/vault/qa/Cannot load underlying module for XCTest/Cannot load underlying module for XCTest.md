---
title: Cannot load underlying module for XCTest
apple_id: DTS40017688
resource_type: QA
platform: iOS|Xcode Developer Tools|macOS
topic: null
technology: XCTest
published: '2017-10-25'
source_url: https://developer.apple.com/library/archive/qa/qa1954/_index.html
archived_at: '2026-07-18T02:37:53.737197Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1954

# Cannot load underlying module for XCTest

## Q:  My Xcode project fails compiling with a "Cannot load underlying module for XCTest" error message. How do I resolve this issue?

A: You may be getting this error for any of the following reasons:

- Your test class was added to a target, which is not a test target.

  Test classes, which are [XCTestCase](https://developer.apple.com/reference/xctest/xctestcase) subclasses and contain UI testing or unit testing methods, should only be added to [test targets](http://help.apple.com/xcode/mac/current/#/dev264d6a4a4). Remove these classes from any target in your Xcode project that is not a test target in order to resolve your issue as shown in Figure 2.

__Figure 1__  Xcode fails compiling: The CalcUITests class is a member of both the target being tested (Calc) and UI test target (CalcUITests).

!!

__Figure 2__  Xcode successfully builds: The CalcUITests class is a member of the CalcUITests UI test target.

!!

- The [XCTest](https://developer.apple.com/reference/xctest) framework was imported into a source file, which is not a test class.

  Remove `import XCTest` from any source file that is not a [test class](http://help.apple.com/xcode/mac/current/#/devf3ae75689) in your project in order to resolve your issue as shown in Figure 4.

__Figure 3__  Xcode fails compiling: Calculator, a class from the CalculatorKit framework, imports the XCTest framework.

!!

__Figure 4__  Xcode successfully builds: The Calculator no longer imports the XCTest framework.

!!

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-10-25 | New document that describes how to resolve the "Cannot load underlying module for XCTest" error message. |

