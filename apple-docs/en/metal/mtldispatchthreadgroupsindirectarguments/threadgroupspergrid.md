---
title: threadgroupsPerGrid
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldispatchthreadgroupsindirectarguments/threadgroupspergrid
source_url: 'https://developer.apple.com/documentation/metal/mtldispatchthreadgroupsindirectarguments/threadgroupspergrid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldispatchthreadgroupsindirectarguments/threadgroupspergrid.json'
content_hash: 'sha256:6d56e3959179c159'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDispatchThreadgroupsIndirectArguments](../mtldispatchthreadgroupsindirectarguments.md)

# threadgroupsPerGrid

<sub>Instance Property</sub>

The number of threadgroups for the grid, in each dimension.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var threadgroupsPerGrid: (UInt32, UInt32, UInt32)
```

## See Also

### Specifying the size of the threadgroup

- [init()](<init().md>) — Returns a new data layout for dispatching threadgroups over indirect buffer calls.
- [init(threadgroupsPerGrid:)](<init(threadgroupspergrid_).md>) — Returns a new data layout for dispatching threadgroups over indirect buffer calls, with specified threadgroups per grid.
