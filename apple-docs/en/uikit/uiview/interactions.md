---
title: interactions
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/interactions
source_url: 'https://developer.apple.com/documentation/uikit/uiview/interactions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/interactions.json'
content_hash: 'sha256:bd2e7b0129f739be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# interactions

<sub>Instance Property</sub>

The array of interactions for the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var interactions: [any UIInteraction] { get set }
```

## See Also

### Adding and removing interactions

- [- addInteraction:](<addinteraction(__).md>) — Adds an interaction to the view.
- [- removeInteraction:](<removeinteraction(__).md>) — Removes an interaction from the view.
- [UIInteraction](../uiinteraction.md) — The protocol that an interaction implements to access the view that owns it.
