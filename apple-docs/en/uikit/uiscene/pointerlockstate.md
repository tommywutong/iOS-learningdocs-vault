---
title: pointerLockState
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/pointerlockstate
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/pointerlockstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/pointerlockstate.json'
content_hash: 'sha256:4475cdb3c4ccadf5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScene](../uiscene.md)

# pointerLockState

<sub>Instance Property</sub>

The pointer lock state for the scene.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var pointerLockState: UIPointerLockState? { get }
```

## Discussion

If a scene can’t lock the pointer, this property is `nil`.

## See Also

### Getting the pointer lock state

- [UIPointerLockState](../uipointerlockstate.md) — An object that contains information about a scene’s pointer lock state.
