---
title: Xcode debugger does not display the value of my variables.
apple_id: DTS40017605
resource_type: QA
platform: watchOS|tvOS|iOS|Xcode Developer Tools
topic: Xcode
technology: null
published: '2017-02-09'
source_url: https://developer.apple.com/library/archive/qa/qa1947/_index.html
archived_at: '2026-07-18T02:37:25.190985Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1947

# Xcode debugger does not display the value of my variables.

## Q:  The debugger doesn't show my variables' value. How can I view them?

A: The debugger may not show the value of your variables for any of the following reasons:

- The Optimization level is not set to None for the Debug configuration.

  Be sure to set it to `None` for Objective-C apps as shown in Figure 1 and for Swift apps as shown in Figure 2.

__Figure 1__  Optimization level set to None for the Debug configuration.

!!

__Figure 2__  Swift Optimization level set to None for the Debug configuration.

!!

- The Build Configuration pop-up menu is set to Release in the scheme editor's Run action settings pane.

  In Xcode, open the scheme editor by choosing Product > Scheme > Edit Scheme…, select the Run action for your app in the scheme actions pane, then set Build Configuration to `Debug` as seen in Figure 3.

__Figure 3__  Build Configuration set to Debug for the Run action.

!!

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-02-09 | New document that describes causes that can prevent the debugger from showing the value of your variables. |

