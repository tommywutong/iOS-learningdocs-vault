---
title: Supporting In-App Purchase in iMessage apps.
apple_id: DTS40017512
resource_type: QA
platform: iOS
topic: User Experience
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/qa/qa1932/_index.html
archived_at: '2026-07-18T02:37:10.721501Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1932

# Supporting In-App Purchase in iMessage apps.

## Q:  My iMessage app uses the compact presentation style and supports in-app purchase. The keyboard comes up when signing in to authenticate my purchase. However, my app loses state once the keyboard is dismissed. How do I resolve this issue?

A: There is an issue that will cause an iMessage app supporting in-app purchase to lose state when dismissing the keyboard in compact style.

To workaround this issue, only perform in-app purchase in expanded style. If in-app purchase was started in compact style, request to transition your extension's user interface to the expanded style by setting `requestPresentationStyle` to `.expanded` before proceeding as shown in Listing 1.

__Listing 1__   Request to transition to the expanded mode (Swift).

```
requestPresentationStyle(.expanded)
```


__Listing 2__  Request to transition to the expanded mode (Objective-C).

```
[self requestPresentationStyle:MSMessagesAppPresentationStyleExpanded];
```

As an example, see the `#images` app displayed in Messages app drawer, which contains a search field as shown in Figure 1. When the search field is tapped, the user interface is transitioned to the expanded style before enabling input as shown in Figure 2.

__Figure 1__  The #images app in Messages app drawer.

!

__Figure 2__  The #images app in expanded presentation style after tapping in its search field.

!

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-08-23 | New document that describes how to support in-app purchase in iMessage apps. |

