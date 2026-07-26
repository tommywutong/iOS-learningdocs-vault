---
title: 'calendarView(_:didChangeVisibleDateComponentsFrom:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.2+, iPadOS 16.2+, Mac Catalyst 16.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicalendarviewdelegate/calendarview(_:didchangevisibledatecomponentsfrom:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarviewdelegate/calendarview(_:didchangevisibledatecomponentsfrom:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarviewdelegate/calendarview%28_%3Adidchangevisibledatecomponentsfrom%3A%29.json'
content_hash: 'sha256:2f4b17aef4ab43f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICalendarViewDelegate](../uicalendarviewdelegate.md)

# calendarView(_:didChangeVisibleDateComponentsFrom:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func calendarView(_ calendarView: UICalendarView, didChangeVisibleDateComponentsFrom previousDateComponents: DateComponents)
```

## Parameters

- `calendarView` — The @c UICalendarView

- `previousDateComponents` — The previous date components before the visible date components changed.

## Discussion

Called when the visible date has changed from @c previousDateComponents from user interaction.
