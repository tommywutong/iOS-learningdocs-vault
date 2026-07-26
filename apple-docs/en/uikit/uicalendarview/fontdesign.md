---
title: fontDesign
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicalendarview/fontdesign
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarview/fontdesign'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarview/fontdesign.json'
content_hash: 'sha256:5382a10cc7c3b80f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICalendarView](../uicalendarview.md)

# fontDesign

<sub>Instance Property</sub>

A font design that the calendar view uses for displaying calendar text.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var fontDesign: UIFontDescriptor.SystemDesign { get set }
```

## Discussion

Defaults to [UIFontDescriptorSystemDesignDefault](../uifontdescriptor/systemdesign/default.md).

## See Also

### Customizing the calendar display

- [delegate](delegate.md) — A delegate object the calendar view calls for decoration views.
- [UICalendarViewDelegate](../uicalendarviewdelegate.md) — An object that a calendar view uses to display decorations for dates.
- [Decoration](decoration.md) — A view that a calendar view displays for a specific date.
- [DecorationSize](decorationsize.md) — Constants that indicate the relative size of a decoration in a calendar view.
- [wantsDateDecorations](wantsdatedecorations.md) — A Boolean value that indicates whether the calendar view displays date decorations.
- [- reloadDecorationsForDateComponents:animated:](<reloaddecorations(fordatecomponents_animated_).md>) — Reloads the decorations for the dates you provide, with an option to animate the decoration reload.
