---
title: UICalendarViewDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicalendarviewdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarviewdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarviewdelegate.json'
content_hash: 'sha256:64fad3ccc2ee65ee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICalendarViewDelegate

<sub>Protocol</sub>

An object that a calendar view uses to display decorations for dates.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UICalendarViewDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Providing calendar view decorations

- [- calendarView:decorationForDateComponents:](<uicalendarviewdelegate/calendarview(__decorationfor_).md>) — Creates a calendar view decoration for the date represented by the date components you provide.

### Instance Methods

- [- calendarView:didChangeVisibleDateComponentsFrom:](<uicalendarviewdelegate/calendarview(__didchangevisibledatecomponentsfrom_).md>)

## See Also

### Customizing the calendar display

- [fontDesign](uicalendarview/fontdesign.md) — A font design that the calendar view uses for displaying calendar text.
- [delegate](uicalendarview/delegate.md) — A delegate object the calendar view calls for decoration views.
- [Decoration](uicalendarview/decoration.md) — A view that a calendar view displays for a specific date.
- [DecorationSize](uicalendarview/decorationsize.md) — Constants that indicate the relative size of a decoration in a calendar view.
- [wantsDateDecorations](uicalendarview/wantsdatedecorations.md) — A Boolean value that indicates whether the calendar view displays date decorations.
- [- reloadDecorationsForDateComponents:animated:](<uicalendarview/reloaddecorations(fordatecomponents_animated_).md>) — Reloads the decorations for the dates you provide, with an option to animate the decoration reload.
