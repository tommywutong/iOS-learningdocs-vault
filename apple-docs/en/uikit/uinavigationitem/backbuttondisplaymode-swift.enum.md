---
title: UINavigationItem.BackButtonDisplayMode
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/backbuttondisplaymode-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/backbuttondisplaymode-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/backbuttondisplaymode-swift.enum.json'
content_hash: 'sha256:f7110d0ec5005a90'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# UINavigationItem.BackButtonDisplayMode

<sub>Enumeration</sub>

Constants that describe the display modes of the Back button.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum BackButtonDisplayMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UINavigationItemBackButtonDisplayModeDefault](backbuttondisplaymode-swift.enum/default.md) — The navigation item attempts to display a specific title, a generic title, or no title for the Back button, depending on the space available.
- [UINavigationItemBackButtonDisplayModeGeneric](backbuttondisplaymode-swift.enum/generic.md) — The navigation item attempts to display a generic title or no title for the Back button, depending on the space available.
- [UINavigationItemBackButtonDisplayModeMinimal](backbuttondisplaymode-swift.enum/minimal.md) — The navigation item displays the Back button indicator instead of a title.

### Initializers

- [init(rawValue:)](<backbuttondisplaymode-swift.enum/init(rawvalue_).md>)

## See Also

### Configuring the Back button

- [backBarButtonItem](backbarbuttonitem.md) — The bar button item for adding a Back button to the navigation bar.
- [backButtonTitle](backbuttontitle.md) — The custom title of the Back button.
- [backButtonDisplayMode](backbuttondisplaymode-swift.property.md) — The display mode of the Back button.
- [hidesBackButton](hidesbackbutton.md) — A Boolean value that determines whether the navigation item hides the Back button.
- [- setHidesBackButton:animated:](<sethidesbackbutton(__animated_).md>) — Hides or shows the Back button, optionally animating the transition.
- [backAction](backaction.md) — The back action for the navigation bar.
