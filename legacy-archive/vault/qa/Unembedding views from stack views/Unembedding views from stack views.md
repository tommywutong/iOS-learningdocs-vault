---
title: Unembedding views from stack views
apple_id: DTS40017118
resource_type: QA
platform: iOS|macOS
topic: Xcode
technology: null
published: '2016-05-16'
source_url: https://developer.apple.com/library/archive/qa/qa1921/_index.html
archived_at: '2026-07-18T02:36:50.346229Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1921

# Unembedding views from stack views

## Q:  How do I unembed my views from a stack view?

A: You can remove views embedded in a stack view by using the Editor menu or the Stack Tool.

1. Select your stack view in the Interface Builder canvas.
2. Choose Editor > Unembed as shown in Figure 1.

__Figure 1__  Select Unembed to remove the stack view. The numbers in this figure correspond to the steps above.

!!

Xcode removes the stack view around your views as shown in Figure 2.

__Figure 2__  Views after removing them from the stack view.

!!

1. Select your stack view in the Interface Builder canvas.
2. Hold down the Option key while selecting the Stack Tool button in the layout bar at the bottom of the canvas.

__Figure 3__  Select the Stack button. The numbers in this figure correspond to the steps above.

!!

1. Select Unembed from the ensuing contextual menu as shown in Figure 4 to unembed your views.

__Figure 4__  Select Unembed to remove your views from a stack view

!!

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-05-16 | New document that how to remove views from a stack view. |

