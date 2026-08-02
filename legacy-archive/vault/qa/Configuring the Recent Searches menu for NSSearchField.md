---
title: Configuring the Recent Searches menu for NSSearchField
apple_id: DTS10004132
resource_type: QA
platform: macOS
topic: User Experience
technology: AppKit
published: '2006-11-27'
source_url: https://developer.apple.com/library/archive/qa/qa1496/_index.html
archived_at: '2026-07-18T02:31:37.880598Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1496

# Configuring the Recent Searches menu for NSSearchField

## Q:  Why are my menu items disabled in the Recent Searches menu of `NSSearchField`?

A: Why are my menu items disabled in the Recent Searches menu of `NSSearchField`?

You are probably not providing an action selector to your menu items. When you add Search Categories to the Recent Searches menu, you are responsible for providing the "action" selector.

Here is how you would programatically build a menu item to be added:

__Listing 1__  Example menu item

```
NSMenuItem *item = [[NSMenuItem alloc] initWithTitle:@"Client Search"                                          action:@selector(clientSearchAction:)                                          keyEquivalent:@""];
```

If you are using Interface Builder to configure your Recent Searches menu, you must connect the menu item to the appropriate action selector in your controller object.

For a complete code example, refer to:

[Introduction to Search Fields: Configuring a Search Menu](https://developer.apple.com/documentation/Cocoa/Conceptual/SearchFields/index.html#//apple_ref/doc/uid/10000168i)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-11-27 | New document that discusses the common problem when adding menu items to the Recent Searches menu. |

