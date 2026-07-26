---
title: threadgroupMemoryDataSize
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（16.0 起废弃）, iPadOS 8.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlargument/threadgroupmemorydatasize
source_url: 'https://developer.apple.com/documentation/metal/mtlargument/threadgroupmemorydatasize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargument/threadgroupmemorydatasize.json'
content_hash: 'sha256:63b3dcaa0e7c8745'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgument](../mtlargument.md)

# threadgroupMemoryDataSize

<sub>Instance Property</sub>

The size, in bytes, of the threadgroup data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var threadgroupMemoryDataSize: Int { get }
```

## Discussion

If the argument is not a threadgroup, querying this property is a fatal error. The Metal device determines this value.

## See Also

### Describing a threadgroup memory argument

- [threadgroupMemoryAlignment](threadgroupmemoryalignment.md) — The required byte alignment in memory for the threadgroup data. _(deprecated)_
