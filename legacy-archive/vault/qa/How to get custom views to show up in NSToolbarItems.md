---
title: How to get custom views to show up in NSToolbarItems
apple_id: DTS10001581
resource_type: QA
platform: macOS
topic: User Experience
technology: AppKit
published: '2011-09-07'
source_url: https://developer.apple.com/library/archive/qa/qa1029/_index.html
archived_at: '2026-07-18T02:29:54.799050Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1029

# How to get custom views to show up in NSToolbarItems

## Q:  Why do custom views not show up in an NSToolBarItem?

A: I have created an NSToolbarItem and added a custom view using `-setView:`. My custom view never shows up in my NSToolbar, however, even after adding the NSToolbarItem and installing the NSToolbar in my window. My standard NSToolbarItems (that contain images) show up just fine. What am I doing wrong here?

NSToolbarItems have a default minimum/maximum width/height of 0,0. Calling `-setImage:` on an NSToolbarItem to give it an image changes the size to be the size of the image, but calling `-setView:` to instead give it a custom view does not. Thus, your custom view never is visible on the screen, because it has a minimum/maximum width and height of 0. Call `-setMinSize:` and `-setMaxSize:` on your NSToolbarItem to set the proper sizes when creating it, and your custom view will become visible.

__Listing 1__  An example of setting the NSToolbarItem size:

```
[newNSToolbarItem setMinSize:[customView bounds].size]; [newNSToolbarItem setMaxSize:[customView bounds].size];
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-09-07 | Reformatted content and made minor editorial changes. |
| 2001-05-03 | New document that why custom views may not show up in an NSToolBarItem and how to make it visible. |

