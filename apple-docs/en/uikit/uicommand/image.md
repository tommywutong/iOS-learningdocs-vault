---
title: image
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicommand/image
source_url: 'https://developer.apple.com/documentation/uikit/uicommand/image'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicommand/image.json'
content_hash: 'sha256:f085f012dc04e81f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICommand](../uicommand.md)

# image

<sub>Instance Property</sub>

The command’s image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var image: UIImage? { get set }
```

## Discussion

Only the [contextSystem](../uimenusystem/context.md) menu system supports the display of an image, and only when the app is running in iOS.

## See Also

### Getting information about the command

- [title](title.md) — The command’s title.
- [action](action.md) — The selector identifying the action method called after the user selects the command.
- [discoverabilityTitle](discoverabilitytitle.md) — An elaborated title that explains the purpose of the command.
- [attributes](attributes.md) — The attributes indicating the style of the command.
- [state](state.md) — The state of the command.
