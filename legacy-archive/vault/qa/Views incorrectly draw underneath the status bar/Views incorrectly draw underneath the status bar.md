---
title: Views incorrectly draw underneath the status bar
apple_id: DTS40011743
resource_type: QA
platform: iOS
topic: User Experience
technology: null
published: '2012-02-07'
source_url: https://developer.apple.com/library/archive/qa/qa1723/_index.html
archived_at: '2026-07-18T02:34:28.242749Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1723

# Views incorrectly draw underneath the status bar

## Q:  Why does my view controller draw under the status bar?

A: If your view controller is the primary content to your `UIWindow`, this can occur when either not setting `UIWindow`'s `rootViewController` property, or the view controller's "Layout" setting "Resize view From NIB" is NOT checked in Interface Builder.

__Figure 1__  Example of a view placed under the status bar.

!

__Listing 1__  Setting `UIWindow`'s `rootViewController` property

```
if ([self.window respondsToSelector:@selector(setRootViewController:)])
        self.window.rootViewController = viewController;
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2012-02-07 | New document that describes the conditions that can cause views to draw underneath the status bar. |

