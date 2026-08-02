---
title: Why is my application crashing in QuickDraw when I'm not using it?
apple_id: DTS10003931
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2006-11-13'
source_url: https://developer.apple.com/library/archive/qa/qa1256/_index.html
archived_at: '2026-07-18T02:30:17.955350Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1256

# Why is my application crashing in QuickDraw when I'm not using it?

## Q:  Why is my application crashing in QuickDraw when I'm not using it?

A: Why is my application crashing in QuickDraw when I'm not using it?

The most likely explanation is that you are experiencing an overwritten closed port problem.

This problem affects both Carbon and Cocoa applications.

System frameworks like the HIToolbox, QuickTime, Print and others still need to make QuickDraw calls for compatibility reasons even when your application does not use QuickDraw directly. Those calls (for instance `PenNormal`) depend on a valid current `GrafPort`. If the application does not set a current port then QuickDraw provides a fallback `GrafPort` to prevent crashes.

To work around this problem, locate in the back trace of the crash log the last call made by your application to any function of a system framework and add a `SetPort( NULL );` statement prior to that call.

Although it may seem counterintuitive to set the current port to `NULL` when past experience and recommendations were exactly the opposite, `SetPort` does not actually set the current port to `NULL` but instead sets the current port to an internal valid fallback port to make sure that QuickDraw doesn't crash when the previous current port gets disposed and a new current port cannot be determined.

If the last system framework call that your application makes before crashing is `RunApplicationEventLoop` or `[NSApplication run]` (and equivalent calls), that probably means that the original problem has been compounded by a long succession of successful QuickDraw calls.

In that case, the workaround would be to add a `SetPort( NULL );` statement after each `DisposeWindow` (and equivalent calls).

It would also be beneficial that you report the problem to Apple with the [BugReporter](https://developer.apple.com/bugreporter/index.html) so that we can investigate and eliminate as much offending code as possible.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-11-13 | New document that provides an explanation and workaround for a rare but serious problem affecting all applications. |

