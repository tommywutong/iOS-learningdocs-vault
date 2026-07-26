---
title: state
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibandselectioninteraction/state-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uibandselectioninteraction/state-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibandselectioninteraction/state-swift.property.json'
content_hash: 'sha256:227283b32d1a41a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBandSelectionInteraction](../uibandselectioninteraction.md)

# state

<sub>Instance Property</sub>

The current state of the interaction object.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var state: UIBandSelectionInteraction.State { get }
```

## Discussion

Use the current state to determine what actions to take in your handler. For example, when an interaction object is in the selecting state, you might highlight items in your view that are inside the current selection rectangle.

## See Also

### Getting the interaction state

- [enabled](isenabled.md) — A Boolean value that specifies whether the object is ready to detect interactions.
- [initialModifierFlags](initialmodifierflags.md) — The pressed modifier keys at the start of the interaction.
- [State](state-swift.enum.md) — Constants that indicate whether a band selection interaction object is inactive or currently tracking an interaction.
