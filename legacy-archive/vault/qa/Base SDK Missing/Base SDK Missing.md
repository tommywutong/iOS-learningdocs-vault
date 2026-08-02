---
title: Base SDK Missing
apple_id: DTS40010191
resource_type: QA
platform: iOS
topic: Xcode
technology: null
published: '2010-11-11'
source_url: https://developer.apple.com/library/archive/qa/qa1701/_index.html
archived_at: '2026-07-18T02:34:12.377277Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1701

# Base SDK Missing

## Q:  I upgraded my SDK to the latest iOS SDK. Xcode displays "Base SDK Missing" in the Overview pop-up menu when I open my project.

A: You are getting the "Base SDK Missing" error message because your "Base SDK" build setting is probably set to an iOS SDK, which is not available in the SDK that you are currently using. For instance, you may be using iOS SDK 4.2 for development while your "Base SDK" is set to iOS SDK 4.0, which is not available in that SDK.

Set your "Base SDK" to `Latest iOS` to resolve this error. Follow these steps to set your "Base SDK":

1. In Xcode, double-click your project in the Project window.
2. Choose the Build pane from the ensuing Info window.
3. Select "All Configurations" from the Configuration popup menu.
4. Navigate to the "Base SDK" build setting and choose `Latest iOS` from the pop-up menu as shown in Figure 1.

__Figure 1__  Base SDK set to Latest iOS for all configurations

!

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-11-11 | Updated for iOS SDK 4.2. |
| 2010-07-21 | New document that describes how to resolve the "Base SDK Missing" error message in Xcode. |

