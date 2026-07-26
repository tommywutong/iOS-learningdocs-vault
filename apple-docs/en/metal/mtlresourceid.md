---
title: MTLResourceID
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresourceid
source_url: 'https://developer.apple.com/documentation/metal/mtlresourceid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresourceid.json'
content_hash: 'sha256:b38ee1008d1173c4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLResourceID

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLResourceID
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<mtlresourceid/init().md>)

## See Also

### Common resource functionality

- [MTLGPUAddress](mtlgpuaddress.md) — A 64-bit unsigned integer type appropriate for storing GPU addresses.
- [MTLAllocation](mtlallocation.md) — A memory allocation from a Metal GPU device, such as a memory heap, texture, or data buffer.
- [MTLResource](mtlresource.md) — An allocation of memory accessible to a GPU.
- [MTLResourceOptions](mtlresourceoptions.md) — Optional arguments used to set the behavior of a resource.
- [MTLResourceUsage](mtlresourceusage.md) — Options that describe how a graphics or compute function uses an argument buffer’s resource.
