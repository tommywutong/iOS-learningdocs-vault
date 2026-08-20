---
title: How do I programmatically quit my iOS application?
apple_id: DTS40007952
resource_type: QA
platform: iOS
topic: User Experience
technology: null
published: '2012-04-09'
source_url: https://developer.apple.com/library/archive/qa/qa1561/_index.html
archived_at: '2026-07-18T02:32:18.365488Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1561

# How do I programmatically quit my iOS application?

## Q:  How do I programmatically quit my iOS application?

A: There is no API provided for gracefully terminating an iOS application.

In iOS, the user presses the Home button to close applications. Should your application have conditions in which it cannot provide its intended function, the recommended approach is to display an alert for the user that indicates the nature of the problem and possible actions the user could take — turning on WiFi, enabling Location Services, etc. Allow the user to terminate the application at their own discretion.

Additionally, data may not be saved, because `-applicationWillTerminate:` and similar `UIApplicationDelegate` methods will not be invoked if you call `exit`.

If during development or testing it is necessary to terminate your application, the `abort` function, or `assert` macro is recommended.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2012-04-09 | Updated to more strongly discourage the exit function, and include best practices for debugging. |
| 2008-08-27 | New document that discusses best practices for terminating an iOS application in code. |

