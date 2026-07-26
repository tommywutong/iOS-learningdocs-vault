---
title: initialModifierFlags
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibandselectioninteraction/initialmodifierflags
source_url: 'https://developer.apple.com/documentation/uikit/uibandselectioninteraction/initialmodifierflags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibandselectioninteraction/initialmodifierflags.json'
content_hash: 'sha256:b7fcb9e695d8afd6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBandSelectionInteraction](../uibandselectioninteraction.md)

# initialModifierFlags

<sub>Instance Property</sub>

The pressed modifier keys at the start of the interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var initialModifierFlags: UIKeyModifierFlags { get }
```

## Discussion

When an interaction starts, the [UIBandSelectionInteraction](../uibandselectioninteraction.md) object places the current pressed modifier keys in this property. Use the set of modifier keys to adjust the behavior of your handler. For example, you might extend an existing selection when someone presses the Shift key.

## See Also

### Getting the interaction state

- [enabled](isenabled.md) — A Boolean value that specifies whether the object is ready to detect interactions.
- [state](state-swift.property.md) — The current state of the interaction object.
- [State](state-swift.enum.md) — Constants that indicate whether a band selection interaction object is inactive or currently tracking an interaction.
