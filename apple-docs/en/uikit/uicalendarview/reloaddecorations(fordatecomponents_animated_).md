---
title: 'reloadDecorations(forDateComponents:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicalendarview/reloaddecorations(fordatecomponents:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarview/reloaddecorations(fordatecomponents:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarview/reloaddecorations%28fordatecomponents%3Aanimated%3A%29.json'
content_hash: 'sha256:532335b0894034a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICalendarView](../uicalendarview.md)

# reloadDecorations(forDateComponents:animated:)

<sub>Instance Method</sub>

Reloads the decorations for the dates you provide, with an option to animate the decoration reload.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func reloadDecorations(forDateComponents dates: [DateComponents], animated: Bool)
```

## Parameters

- `dates` — An array of dates to reload that you provide as date components.

- `animated` — A Boolean value that indicates whether the calendar view should animate the decoration reload.

## See Also

### Customizing the calendar display

- [fontDesign](fontdesign.md) — A font design that the calendar view uses for displaying calendar text.
- [delegate](delegate.md) — A delegate object the calendar view calls for decoration views.
- [UICalendarViewDelegate](../uicalendarviewdelegate.md) — An object that a calendar view uses to display decorations for dates.
- [Decoration](decoration.md) — A view that a calendar view displays for a specific date.
- [DecorationSize](decorationsize.md) — Constants that indicate the relative size of a decoration in a calendar view.
- [wantsDateDecorations](wantsdatedecorations.md) — A Boolean value that indicates whether the calendar view displays date decorations.
