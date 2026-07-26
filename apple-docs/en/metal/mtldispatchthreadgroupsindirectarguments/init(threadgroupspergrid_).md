---
title: 'init(threadgroupsPerGrid:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldispatchthreadgroupsindirectarguments/init(threadgroupspergrid:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldispatchthreadgroupsindirectarguments/init(threadgroupspergrid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldispatchthreadgroupsindirectarguments/init%28threadgroupspergrid%3A%29.json'
content_hash: 'sha256:9685f8cf1a2cb747'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDispatchThreadgroupsIndirectArguments](../mtldispatchthreadgroupsindirectarguments.md)

# init(threadgroupsPerGrid:)

<sub>Initializer</sub>

Returns a new data layout for dispatching threadgroups over indirect buffer calls, with specified threadgroups per grid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(threadgroupsPerGrid: (UInt32, UInt32, UInt32))
```

## Parameters

- `threadgroupsPerGrid` — The number of threadgroups for the grid, in each dimension.

## See Also

### Specifying the size of the threadgroup

- [init()](<init().md>) — Returns a new data layout for dispatching threadgroups over indirect buffer calls.
- [threadgroupsPerGrid](threadgroupspergrid.md) — The number of threadgroups for the grid, in each dimension.
