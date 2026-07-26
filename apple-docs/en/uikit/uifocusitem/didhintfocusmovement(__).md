---
title: 'didHintFocusMovement(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifocusitem/didhintfocusmovement(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifocusitem/didhintfocusmovement(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusitem/didhintfocusmovement%28_%3A%29.json'
content_hash: 'sha256:13ae0e8f28018bc9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusItem](../uifocusitem.md)

# didHintFocusMovement(_:)

<sub>Instance Method</sub>

Indicates to the currently focused item that focus movement might occur.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func didHintFocusMovement(_ hint: UIFocusMovementHint)
```

## Parameters

- `hint` — The movement hint object corresponding to the user’s input.

## Discussion

The focus item is mutated by the focus engine whenever the user’s finger moves on the remote.

## See Also

### Providing movement hints

- [UIFocusMovementHint](../uifocusmovementhint.md) — Provides movement hint information for the focused item.
