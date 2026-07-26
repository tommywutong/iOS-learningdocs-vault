---
title: access
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（16.0 起废弃）, iPadOS 8.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlargument/access
source_url: 'https://developer.apple.com/documentation/metal/mtlargument/access'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargument/access.json'
content_hash: 'sha256:5e16413d218c7851'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgument](../mtlargument.md)

# access

<sub>Instance Property</sub>

The argument’s read and/or write access.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var access: MTLBindingAccess { get }
```

## Discussion

This property indicates the type of access qualifiers (read-only, write-only, or read-write) used in the Metal shading language code. For information on possible values, see [MTLArgumentAccess](../mtlargumentaccess.md).

## See Also

### Describing the argument

- [name](name.md) — The name of the argument. _(deprecated)_
- [active](isactive.md) — A Boolean that indicates whether the compiled function uses the argument. _(deprecated)_
- [index](index.md) — The index in the argument table that corresponds to the function argument. _(deprecated)_
- [type](type.md) — The argument’s resource type. _(deprecated)_
