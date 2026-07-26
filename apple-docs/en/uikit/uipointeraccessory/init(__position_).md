---
title: 'init(_:position:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipointeraccessory/init(_:position:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipointeraccessory/init(_:position:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointeraccessory/init%28_%3Aposition%3A%29.json'
content_hash: 'sha256:07e1fe5907d78e84'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPointerAccessory](../uipointeraccessory.md)

# init(_:position:)

<sub>Initializer</sub>

Creates a pointer accessory with the specified shape and position.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency convenience init(_ shape: UIPointerShape, position: UIPointerAccessory.Position)
```

## Parameters

- `shape` — One of the available [UIPointerShape](../uipointershape-swift.enum.md) shapes.

- `position` — One of the available [Position](position-swift.struct.md) positions.

## See Also

### Creating a pointer accessory

- [arrow(_:)](<arrow(__).md>) — Creates a pointer accessory with an arrow shape at the specified position.
