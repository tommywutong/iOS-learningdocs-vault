---
title: 'MTLSizeMake(_:_:_:)'
framework: Metal
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlsizemake(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlsizemake(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsizemake%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:fc3f9ab8da5da3b3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLSizeMake(_:_:_:)

<sub>Function</sub>

Creates a size instance with values for its width, height, and depth properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func MTLSizeMake(_ width: Int, _ height: Int, _ depth: Int) -> MTLSize
```

## Parameters

- `width` — A value for the x-axis dimension.

- `height` — A value for the y-axis dimension. Pass `1` for sizes with one dimension.

- `depth` — A value for the z-axis dimension. Pass `1` for sizes with one or two dimensions.

## See Also

### Creating a size instance

- [init()](<mtlsize/init().md>) — Creates a default size instance by setting the initial values for its width, height, and depth properties to zero.
- [init(width:height:depth:)](<mtlsize/init(width_height_depth_).md>) — Creates a size instance with values for its width, height, and depth properties.
