---
title: Unified window title and toolbar appearance in Carbon
apple_id: DTS10003737
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2005-06-17'
source_url: https://developer.apple.com/library/archive/qa/qa1423/_index.html
archived_at: '2026-07-18T02:30:39.800573Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1423

# Unified window title and toolbar appearance in Carbon

## Q:  In Mac OS X v10.4, there is a new window appearance that draws the window titlebar and toolbar as one unified gradient, with no separation between the two areas. Does Carbon support this unified window appearance?

A: In Mac OS X v10.4, there is a new window appearance that draws the window titlebar and toolbar as one unified gradient, with no separation between the two areas. Does Carbon support this unified window appearance?

Yes, via a new window attribute. This attribute was not included in the final 10.4 headers, but is implemented in 10.4 and later.

To access this style using Carbon, set the kWindowUnifiedTitleAndToolbarAttribute bit in the window's attributes using ChangeWindowAttributes. This constant has the following value:

__Listing 1__  kWindowUnifiedTitleAndToolbarAttribute constant

```
#define kWindowUnifiedTitleAndToolbarAttribute (1 << 7)
```

This attribute may be set either at window creation time or after the window is created. The window will redraw when the attribute is changed.

A window may not have both kWindowMetalAttribute and kWindowUnifiedTitleAndToolbarAttribute. If a window already has the Metal attribute, attempting to set the Unified attribute will cause ChangeWindowAttributes to return an error, and vice versa.

There are some known issues with the Carbon implementation of this window style as of Mac OS X v10.4.2:

- When a window using this style is deactivated, Carbon does not change the window title or toolbar appearance. Cocoa draws an inactive window's title and toolbar using a striped background, identical to the appearance of an inactive non-unified window.
- When a window using this style has its toolbar hidden, Carbon draws a very light gray line at the bottom of the title, which is much less visible when adjacent to a white background for the window content. Cocoa draws a dark gray line at the bottom of the title to separate the title from the window content.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-06-17 | New document that how to use the unified window title and toolbar appearance for a Carbon window. |

