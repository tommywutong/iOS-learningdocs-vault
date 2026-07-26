---
title: type
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（16.0 起废弃）, iPadOS 8.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlargument/type
source_url: 'https://developer.apple.com/documentation/metal/mtlargument/type'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargument/type.json'
content_hash: 'sha256:9f97f0880d5a5a58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgument](../mtlargument.md)

# type

<sub>Instance Property</sub>

The argument’s resource type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var type: MTLArgumentType { get }
```

## Discussion

This property indicates which type of resource is used (buffer, texture, sampler, or threadgroup memory) in the shading language code. For information on possible values, see [MTLArgumentType](../mtlargumenttype.md).

## See Also

### Describing the argument

- [name](name.md) — The name of the argument. _(deprecated)_
- [active](isactive.md) — A Boolean that indicates whether the compiled function uses the argument. _(deprecated)_
- [index](index.md) — The index in the argument table that corresponds to the function argument. _(deprecated)_
- [access](access.md) — The argument’s read and/or write access. _(deprecated)_
