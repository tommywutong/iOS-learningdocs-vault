---
title: 'init(red:green:blue:alpha:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtltextureswizzlechannels/init(red:green:blue:alpha:)'
source_url: 'https://developer.apple.com/documentation/metal/mtltextureswizzlechannels/init(red:green:blue:alpha:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltextureswizzlechannels/init%28red%3Agreen%3Ablue%3Aalpha%3A%29.json'
content_hash: 'sha256:495560383b1eeada'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTextureSwizzleChannels](../mtltextureswizzlechannels.md)

# init(red:green:blue:alpha:)

<sub>Initializer</sub>

Creates a swizzle pattern.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(red: MTLTextureSwizzle, green: MTLTextureSwizzle, blue: MTLTextureSwizzle, alpha: MTLTextureSwizzle)
```

## Parameters

- `red` — The data you want to copy to the first output channel

- `green` — The data you want to copy to the second output channel

- `blue` — The data you want to copy to the third output channel

- `alpha` — The data you want to copy to the fourth output channel

## See Also

### Creating a swizzle pattern

- [init()](<init().md>) — Creates a default swizzle pattern.
