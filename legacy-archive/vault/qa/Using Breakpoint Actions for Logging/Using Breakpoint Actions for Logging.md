---
title: Using Breakpoint Actions for Logging
apple_id: DTS40009412
resource_type: QA
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/qa/qa1675/_index.html
archived_at: '2026-07-18T02:33:42.805455Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1675

# Using Breakpoint Actions for Logging

## Q:  How do I use Breakpoint Actions for logging debug messages?

A: Traditionally, many programmers have used printf, NSLog, and similar facilities for tracing execution through in code. Similar functionality can be achieved using Breakpoint Actions, which allow you to attach a set of log expressions to a standard debugging breakpoint.

The steps for logging via a Breakpoint Action are:

- Set a breakpoint by clicking once in the editor window's "gutter".
- Control-click (or right-click) to display the breakpoint context menu, and choose "Edit Breakpoint". This will open the breakpoints window.

__Figure 1__  Breakpoint Menu:

!

__Figure 2__  Breakpoints Window:

!

- Click the "+" button to open the breakpoint actions.
- Enter your log text.
- Click the top right checkbox to ensure that execution continues when the breakpoint is hit.

__Figure 3__  Breakpoint Action logging example:

!

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-03-09 | Moved to Retired Documents Library. |
| 2009-12-09 | First Version |

