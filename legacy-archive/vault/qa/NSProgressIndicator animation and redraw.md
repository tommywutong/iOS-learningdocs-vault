---
title: NSProgressIndicator animation and redraw
apple_id: DTS10004130
resource_type: QA
platform: macOS
topic: User Experience
technology: AppKit
published: '2006-11-15'
source_url: https://developer.apple.com/library/archive/qa/qa1473/_index.html
archived_at: '2026-07-18T02:30:57.295145Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1473

# NSProgressIndicator animation and redraw

## Q:  Why doesn't my `NSProgressIndicator` redraw every time I update it's value?

A: Why doesn't my `NSProgressIndicator` redraw every time I update it's value?

When an update to `NSProgressIndicator` is needed, when its value changes, or you call `animate:`, an event to redraw the view is added to the event queue and will be processed the next time events for that view are dispatched.

To ensure the progress bar redraws at once, you need to call:

`[progressIndicator displayIfNeeded];`

This will force pending events out of the standard queue and have them reflected on-screen immediately.

__Listing 1__  Example of using `NSProgressIndicator` control in a loop.

```
[progressIndicator setMaxValue: (double)count]; //... for (loopIndex = 0; loopIndex < count; loopIndex++) {      // do some work...      [progressIndicator setDoubleValue: (double)loopIndex];      [progressIndicator displayIfNeeded]; }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-11-15 | New document that discusses why NSProgressIndicator does not redraw during progress loops. |

