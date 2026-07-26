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
doc_path: /documentation/uikit/uiaction/image
source_url: 'https://developer.apple.com/documentation/uikit/uiaction/image'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaction/image.json'
content_hash: 'sha256:69d0722b9cc74f0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAction](../uiaction.md)

# image

<sub>Instance Property</sub>

The action’s image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var image: UIImage? { get set }
```

## Discussion

The image appears next to the action’s [title](title.md). Only the [contextSystem](../uimenusystem/context.md) menu system supports the display of an image, and only when the app is running in iOS.

## See Also

### Getting information about the action

- [title](title.md) — The action’s title.
- [identifier](identifier-swift.property.md) — The unique identifier for the action.
- [discoverabilityTitle](discoverabilitytitle.md) — An elaborated title that explains the purpose of the action.
- [attributes](attributes.md) — The attributes indicating the style of the action.
- [state](state.md) — The state of the action.
- [sender](sender.md) — The object responsible for the action handler.
