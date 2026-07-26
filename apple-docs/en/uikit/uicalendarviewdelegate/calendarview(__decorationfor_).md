---
title: 'calendarView(_:decorationFor:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicalendarviewdelegate/calendarview(_:decorationfor:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarviewdelegate/calendarview(_:decorationfor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarviewdelegate/calendarview%28_%3Adecorationfor%3A%29.json'
content_hash: 'sha256:1c0e50a3dc17e91b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICalendarViewDelegate](../uicalendarviewdelegate.md)

# calendarView(_:decorationFor:)

<sub>Instance Method</sub>

Creates a calendar view decoration for the date represented by the date components you provide.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func calendarView(_ calendarView: UICalendarView, decorationFor dateComponents: DateComponents) -> UICalendarView.Decoration?
```

## Parameters

- `calendarView` — The calendar view object requesting the decoration.

- `dateComponents` — Date components that represent the date for the calendar view to display a decoration.

## Return Value

A calendar view decoration.
