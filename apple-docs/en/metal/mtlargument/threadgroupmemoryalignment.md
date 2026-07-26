---
title: threadgroupMemoryAlignment
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（16.0 起废弃）, iPadOS 8.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlargument/threadgroupmemoryalignment
source_url: 'https://developer.apple.com/documentation/metal/mtlargument/threadgroupmemoryalignment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargument/threadgroupmemoryalignment.json'
content_hash: 'sha256:b65d545df0b7afc3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgument](../mtlargument.md)

# threadgroupMemoryAlignment

<sub>Instance Property</sub>

The required byte alignment in memory for the threadgroup data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var threadgroupMemoryAlignment: Int { get }
```

## Discussion

If the argument is not a threadgroup, querying this property is a fatal error. The Metal device determines this value.

## See Also

### Describing a threadgroup memory argument

- [threadgroupMemoryDataSize](threadgroupmemorydatasize.md) — The size, in bytes, of the threadgroup data. _(deprecated)_
