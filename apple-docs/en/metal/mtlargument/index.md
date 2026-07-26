---
title: index
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（16.0 起废弃）, iPadOS 8.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlargument/index
source_url: 'https://developer.apple.com/documentation/metal/mtlargument/index'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargument/index.json'
content_hash: 'sha256:9194eeeac56c8f46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgument](../mtlargument.md)

# index

<sub>Instance Property</sub>

The index in the argument table that corresponds to the function argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var index: Int { get }
```

## Discussion

A command encoder ([MTLComputeCommandEncoder](../mtlcomputecommandencoder.md) or [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)) specifies the index in the corresponding argument table. For example, an app can call the [- setTexture:atIndex:](<../mtlcomputecommandencoder/settexture(__index_).md>) method of [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md) to specify an index in the texture argument table for an [MTLTexture](../mtltexture.md) instance that is used as an argument of a compute function.

## See Also

### Describing the argument

- [name](name.md) — The name of the argument. _(deprecated)_
- [active](isactive.md) — A Boolean that indicates whether the compiled function uses the argument. _(deprecated)_
- [type](type.md) — The argument’s resource type. _(deprecated)_
- [access](access.md) — The argument’s read and/or write access. _(deprecated)_
