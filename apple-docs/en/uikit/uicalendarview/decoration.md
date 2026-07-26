---
title: UICalendarView.Decoration
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicalendarview/decoration
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarview/decoration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarview/decoration.json'
content_hash: 'sha256:a1d40f12f47f99a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICalendarView](../uicalendarview.md)

# UICalendarView.Decoration

<sub>Class</sub>

A view that a calendar view displays for a specific date.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class Decoration
```

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [Sendable](../../swift/sendable.md)

## Topics

### Creating a Default Decoration View

- [- init](<decoration/init().md>) — Creates a default calendar view decoration with a filled circle image, using the system fill color and medium size.
- [default(color:size:)](<decoration/default(color_size_).md>) — Creates a default calendar view decoration with a filled circle image, using the color and size you specify.

### Creating a Custom Decoration View

- [+ decorationWithCustomViewProvider:](<decoration/customview(__).md>) — Creates a new calendar view decoration with a custom view, using your view provider.

### Creating Image Decoration Views

- [image(_:color:size:)](<decoration/image(__color_size_).md>) — Creates a new calendar view decoration with the image, color, and size that you specify.

### Initializers

- [init(customViewProvider:)](<decoration/init(customviewprovider_).md>)

## See Also

### Customizing the calendar display

- [fontDesign](fontdesign.md) — A font design that the calendar view uses for displaying calendar text.
- [delegate](delegate.md) — A delegate object the calendar view calls for decoration views.
- [UICalendarViewDelegate](../uicalendarviewdelegate.md) — An object that a calendar view uses to display decorations for dates.
- [DecorationSize](decorationsize.md) — Constants that indicate the relative size of a decoration in a calendar view.
- [wantsDateDecorations](wantsdatedecorations.md) — A Boolean value that indicates whether the calendar view displays date decorations.
- [- reloadDecorationsForDateComponents:animated:](<reloaddecorations(fordatecomponents_animated_).md>) — Reloads the decorations for the dates you provide, with an option to animate the decoration reload.
