---
title: 'removeInteraction(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/removeinteraction(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/removeinteraction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/removeinteraction%28_%3A%29.json'
content_hash: 'sha256:7a0a57be8dfe53ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# removeInteraction(_:)

<sub>Instance Method</sub>

Removes an interaction from the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func removeInteraction(_ interaction: any UIInteraction)
```

## Parameters

- `interaction` — The interaction object to remove from the view.

## See Also

### Adding and removing interactions

- [- addInteraction:](<addinteraction(__).md>) — Adds an interaction to the view.
- [interactions](interactions.md) — The array of interactions for the view.
- [UIInteraction](../uiinteraction.md) — The protocol that an interaction implements to access the view that owns it.
