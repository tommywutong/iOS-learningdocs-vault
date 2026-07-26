---
title: UICalendarView.DecorationSize
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicalendarview/decorationsize
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarview/decorationsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarview/decorationsize.json'
content_hash: 'sha256:e1c49972da0426b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICalendarView](../uicalendarview.md)

# UICalendarView.DecorationSize

<sub>Enumeration</sub>

Constants that indicate the relative size of a decoration in a calendar view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum DecorationSize
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Decoration View Sizes

- [UICalendarViewDecorationSizeLarge](decorationsize/large.md) — A large relative decoration size in a calendar view.
- [UICalendarViewDecorationSizeMedium](decorationsize/medium.md) — A medium relative decoration size in a calendar view.
- [UICalendarViewDecorationSizeSmall](decorationsize/small.md) — A small relative decoration size in a calendar view.

### Initializers

- [init(rawValue:)](<decorationsize/init(rawvalue_).md>)

## See Also

### Customizing the calendar display

- [fontDesign](fontdesign.md) — A font design that the calendar view uses for displaying calendar text.
- [delegate](delegate.md) — A delegate object the calendar view calls for decoration views.
- [UICalendarViewDelegate](../uicalendarviewdelegate.md) — An object that a calendar view uses to display decorations for dates.
- [Decoration](decoration.md) — A view that a calendar view displays for a specific date.
- [wantsDateDecorations](wantsdatedecorations.md) — A Boolean value that indicates whether the calendar view displays date decorations.
- [- reloadDecorationsForDateComponents:animated:](<reloaddecorations(fordatecomponents_animated_).md>) — Reloads the decorations for the dates you provide, with an option to animate the decoration reload.
