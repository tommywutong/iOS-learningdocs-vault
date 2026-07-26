---
title: 'init(width:height:depth:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlsize/init(width:height:depth:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlsize/init(width:height:depth:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsize/init%28width%3Aheight%3Adepth%3A%29.json'
content_hash: 'sha256:d74e619a4cddcb87'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLSize](../mtlsize.md)

# init(width:height:depth:)

<sub>Initializer</sub>

Creates a size instance with values for its width, height, and depth properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(width: Int, height: Int, depth: Int)
```

## Parameters

- `width` — A value for the x-axis dimension.

- `height` — A value for the y-axis dimension. Pass `1` for sizes with one dimension.

- `depth` — A value for the z-axis dimension. Pass `1` for sizes with one or two dimensions.

## See Also

### Creating a size instance

- [init()](<init().md>) — Creates a default size instance by setting the initial values for its width, height, and depth properties to zero.
- [MTLSizeMake](<../mtlsizemake(______).md>) — Creates a size instance with values for its width, height, and depth properties.
