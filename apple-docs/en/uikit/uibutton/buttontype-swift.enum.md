---
title: UIButton.ButtonType
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/buttontype-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/buttontype-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/buttontype-swift.enum.json'
content_hash: 'sha256:76732bbf6de680f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# UIButton.ButtonType

<sub>Enumeration</sub>

Specifies the style of a button.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum ButtonType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIButtonTypeCustom](buttontype-swift.enum/custom.md) — No button style.
- [UIButtonTypeSystem](buttontype-swift.enum/system.md) — A system style button, such as those shown in navigation bars and toolbars.
- [UIButtonTypeDetailDisclosure](buttontype-swift.enum/detaildisclosure.md) — A detail disclosure button.
- [UIButtonTypeInfoLight](buttontype-swift.enum/infolight.md) — An information button that has a light background.
- [UIButtonTypeInfoDark](buttontype-swift.enum/infodark.md) — An information button that has a dark background.
- [UIButtonTypeContactAdd](buttontype-swift.enum/contactadd.md) — A contact add button.
- [UIButtonTypePlain](buttontype-swift.enum/plain.md) — A standard system button without a blurred background view.
- [UIButtonTypeClose](buttontype-swift.enum/close.md) — A close button to dismiss panels and views.
- [UIButtonTypeRoundedRect](buttontype-swift.enum/roundedrect.md) — A rounded-rectangle style button. _(deprecated)_

### Initializers

- [init(rawValue:)](<buttontype-swift.enum/init(rawvalue_).md>)

## See Also

### Creating buttons of a specific type

- [+ buttonWithType:](<init(type_).md>) — Creates and returns a new button of the specified type.
- [init(type:primaryAction:)](<init(type_primaryaction_).md>) — Creates a new button with the specified type, registers the primary action event, and sets the title and image to the action’s title and image.
