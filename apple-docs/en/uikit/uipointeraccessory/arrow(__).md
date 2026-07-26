---
title: 'arrow(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipointeraccessory/arrow(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipointeraccessory/arrow(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointeraccessory/arrow%28_%3A%29.json'
content_hash: 'sha256:c346e0f73330bf7f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPointerAccessory](../uipointeraccessory.md)

# arrow(_:)

<sub>Type Method</sub>

Creates a pointer accessory with an arrow shape at the specified position.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency class func arrow(_ position: UIPointerAccessory.Position) -> Self
```

## Parameters

- `position` — One of the available [Position](position-swift.struct.md) positions.

## See Also

### Creating a pointer accessory

- [init(_:position:)](<init(__position_).md>) — Creates a pointer accessory with the specified shape and position.
