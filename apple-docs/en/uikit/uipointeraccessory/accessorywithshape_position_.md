---
title: 'accessoryWithShape:position:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipointeraccessory/accessorywithshape:position:'
source_url: 'https://developer.apple.com/documentation/uikit/uipointeraccessory/accessorywithshape:position:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointeraccessory/accessorywithshape%3Aposition%3A.json'
content_hash: 'sha256:21ca2193e0f8963f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPointerAccessory](../uipointeraccessory.md)

# accessoryWithShape:position:

<sub>Type Method</sub>

Creates a pointer accessory with the specified shape and position.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) accessoryWithShape:(UIPointerShape *) shape position:(UIPointerAccessoryPosition) position;
```

## Parameters

- `shape` — One of the available [UIPointerShape](../uipointershape-swift.enum.md) shapes.

- `position` — One of the available [Position](position-swift.struct.md) positions.

## See Also

### Creating a pointer accessory

- [arrowAccessoryWithPosition:](arrowaccessorywithposition_.md) — Creates a pointer accessory at the specified position.
