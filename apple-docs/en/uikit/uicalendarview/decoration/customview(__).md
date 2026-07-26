---
title: 'customView(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicalendarview/decoration/customview(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarview/decoration/customview(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarview/decoration/customview%28_%3A%29.json'
content_hash: 'sha256:0940de66a579c56e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UICalendarView](../../uicalendarview.md) · [Decoration](../decoration.md)

# customView(_:)

<sub>Type Method</sub>

Creates a new calendar view decoration with a custom view, using your view provider.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class func customView(_ customViewProvider: @escaping () -> UIView) -> Self
```

## Parameters

- `customViewProvider` — A block of code that creates and returns a calendar view decoration.

## Return Value

A calendar view decoration.

## Discussion

Create and return a decoration view for the calendar view in your `customViewProvider` block. The calendar view will clip the decoration view to its parent’s bounds. The decoration view may not have any interactions.
