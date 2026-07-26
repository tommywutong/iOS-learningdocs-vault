---
title: 'init(_:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibandselectioninteraction/init(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibandselectioninteraction/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibandselectioninteraction/init%28_%3A%29.json'
content_hash: 'sha256:a9e369c54885af27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBandSelectionInteraction](../uibandselectioninteraction.md)

# init(_:)

<sub>Initializer</sub>

Creates a new band selection interaction object with the provided handler code.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(_ selectionHandler: @escaping (UIBandSelectionInteraction) -> Void)
```

## Parameters

- `selectionHandler` — The handler block you use to process interaction-related events. The handler block has no return value and takes the following parameter: - **interaction** — The band selection interaction object that reported the event. Use the [state](state-swift.property.md) property of this object to determine what actions to take. For example, when the value of the property is [UIBandSelectionInteractionStateSelecting](state-swift.enum/selecting.md), get the current selection rectangle and intersect it with the items in your view.

## Return Value

An initialized band selection interaction object. Add the returned object to a view to begin detecting interactions.
