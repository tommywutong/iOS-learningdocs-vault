---
title: isActive
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（16.0 起废弃）, iPadOS 8.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlargument/isactive
source_url: 'https://developer.apple.com/documentation/metal/mtlargument/isactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargument/isactive.json'
content_hash: 'sha256:7a660cdf8444a918'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgument](../mtlargument.md)

# isActive

<sub>Instance Property</sub>

A Boolean that indicates whether the compiled function uses the argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isActive: Bool { get }
```

## Discussion

When you create the [MTLFunction](../mtlfunction.md) object, Metal statically determines whether the function uses the argument. If [true](../../swift/true.md), you need to provide a value for this argument when you encode a command that calls this function. If [false](../../swift/false.md), the function doesn’t use the argument, and you can ignore it.

## See Also

### Describing the argument

- [name](name.md) — The name of the argument. _(deprecated)_
- [index](index.md) — The index in the argument table that corresponds to the function argument. _(deprecated)_
- [type](type.md) — The argument’s resource type. _(deprecated)_
- [access](access.md) — The argument’s read and/or write access. _(deprecated)_
