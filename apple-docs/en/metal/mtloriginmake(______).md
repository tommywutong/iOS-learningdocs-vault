---
title: 'MTLOriginMake(_:_:_:)'
framework: Metal
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtloriginmake(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtloriginmake(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtloriginmake%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:bce68af04fde8f85'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLOriginMake(_:_:_:)

<sub>Function</sub>

Returns a new origin with the specified coordinates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func MTLOriginMake(_ x: Int, _ y: Int, _ z: Int) -> MTLOrigin
```

## Parameters

- `x` — The x coordinate.

- `y` — The y coordinate.

- `z` — The z coordinate.

## Return Value

The specified origin point.

## See Also

### Creating origin points

- [init()](<mtlorigin/init().md>) — Initializes a new origin.
- [init(x:y:z:)](<mtlorigin/init(x_y_z_).md>) — Initializes a new origin with the specified coordinates.
