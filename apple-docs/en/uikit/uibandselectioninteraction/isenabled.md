---
title: isEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibandselectioninteraction/isenabled
source_url: 'https://developer.apple.com/documentation/uikit/uibandselectioninteraction/isenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibandselectioninteraction/isenabled.json'
content_hash: 'sha256:6c9bf9f24d8ebef8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBandSelectionInteraction](../uibandselectioninteraction.md)

# isEnabled

<sub>Instance Property</sub>

A Boolean value that specifies whether the object is ready to detect interactions.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var isEnabled: Bool { get set }
```

## Discussion

If the value of this property is [true](../../swift/true.md), the [UIBandSelectionInteraction](../uibandselectioninteraction.md) object is ready to detect pointer-based events in its owning view and initiate interactions. If the value is [false](../../swift/false.md), the object ignores events and doesn’t start interactions. The default value of this property is [true](../../swift/true.md).

## See Also

### Getting the interaction state

- [initialModifierFlags](initialmodifierflags.md) — The pressed modifier keys at the start of the interaction.
- [state](state-swift.property.md) — The current state of the interaction object.
- [State](state-swift.enum.md) — Constants that indicate whether a band selection interaction object is inactive or currently tracking an interaction.
