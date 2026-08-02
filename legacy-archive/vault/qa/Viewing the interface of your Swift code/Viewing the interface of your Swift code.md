---
title: Viewing the interface of your Swift code
apple_id: DTS40016826
resource_type: QA
platform: tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2016-03-23'
source_url: https://developer.apple.com/library/archive/qa/qa1914/_index.html
archived_at: '2026-07-18T02:36:11.984143Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1914

# Viewing the interface of your Swift code

## Q:  How do I view the interface of my Swift code in Xcode?

A: Xcode generates an interface file that includes all your source code's internal and public declarations when using the Assistant editor button, the Navigate menu, or the Generated Interface feature.

1. Select your Swift file in the project navigator.
2. Click the Assistant editor button in the Xcode toolbar as shown in Figure 1.

__Figure 1__  Viewing the ListItem file in the project navigator. The numbers in this figure correspond to the steps above.

!!

Xcode automatically shows the generated interface for your Swift code in its Assistant editor pane using the Counterparts mode as shown in Figure 2.

__Figure 2__  Viewing the interface of ListItem in the Assistant editor pane

!!

1. Select your Swift file in the project navigator.
2. Choose Navigate > Jump to Generated Interface as shown in Figure 3 to view your code's interface.

__Figure 3__  Select Jump to Generated Interface to view the interface of ListItem. The numbers in this figure correspond to the steps above.

!!

__Figure 4__  Switch back to the Swift file associated with the ListItem interface

!!

1. Select your Swift file in the project navigator.
2. Click the related items button in the editor's jump bar.
3. Xcode displays a contextual menu. Choose Generated Interface as shown in Figure 5 to view your code's interface.

__Figure 5__  Select Generated Interface to view the interface of ListItem. The numbers in this figure correspond to the steps above.

!!

__Figure 6__  Switch back to the Swift file associated with the ListItem interface

!!

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-03-23 | New document that describes how to view the interface of your Swift code. |

