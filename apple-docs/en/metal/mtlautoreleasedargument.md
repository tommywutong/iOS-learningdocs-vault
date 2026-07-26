---
title: MTLAutoreleasedArgument
framework: Metal
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+（16.0 起废弃）, iPadOS 8.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlautoreleasedargument
source_url: 'https://developer.apple.com/documentation/metal/mtlautoreleasedargument'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlautoreleasedargument.json'
content_hash: 'sha256:33e66edfeba0f90c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLAutoreleasedArgument

<sub>Type Alias</sub>

A convenience type alias for an autoreleased argument instance.

> [!warning] Deprecated
> Use [MTLBinding](mtlbinding.md) instead, and cast it to specific binding type, such as [MTLTextureBinding](mtltexturebinding.md), [MTLBufferBinding](mtlbufferbinding.md), and so on.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
typealias MTLAutoreleasedArgument = MTLArgument
```

## See Also

### Function arguments

- [MTLAttribute](mtlattribute.md) — An object that describes an attribute defined in the stage-in argument for a shader.
- [MTLVertexAttribute](mtlvertexattribute.md) — An instance that represents an attribute of a vertex function.
- [MTLArgument](mtlargument.md) — Information about an argument of a graphics or compute function. _(deprecated)_
- [MTLArgumentType](mtlargumenttype.md) — The resource type for an argument of a function. _(deprecated)_
- [MTLArgumentAccess](mtlargumentaccess.md) — Function access restrictions to argument data in the shading language code. _(deprecated)_
