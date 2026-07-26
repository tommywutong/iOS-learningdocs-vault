---
title: MTLResourceUsage
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresourceusage
source_url: 'https://developer.apple.com/documentation/metal/mtlresourceusage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresourceusage.json'
content_hash: 'sha256:4cf1544a957b81f4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLResourceUsage

<sub>Structure</sub>

Options that describe how a graphics or compute function uses an argument buffer’s resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLResourceUsage
```

## Overview

You can combine multiple [MTLResourceUsage](mtlresourceusage.md) values with a bitwise OR (`|`) if the resource serves multiple purposes over its lifetime. You can enable options for certain resources that indicate whether the Metal driver needs to convert the resource to another format, such as whether it needs to decompress a color render target.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<mtlresourceusage/init(rawvalue_).md>) — Creates a set of resource options from a raw value.

### Type Properties

- [MTLResourceUsageRead](mtlresourceusage/read.md) — An option that enables reading from the resource.
- [MTLResourceUsageSample](mtlresourceusage/sample.md) — An option that enables sampling from the resource. _(deprecated)_
- [MTLResourceUsageWrite](mtlresourceusage/write.md) — An option that enables writing to the resource.

## See Also

### Common resource functionality

- [MTLGPUAddress](mtlgpuaddress.md) — A 64-bit unsigned integer type appropriate for storing GPU addresses.
- [MTLAllocation](mtlallocation.md) — A memory allocation from a Metal GPU device, such as a memory heap, texture, or data buffer.
- [MTLResource](mtlresource.md) — An allocation of memory accessible to a GPU.
- [MTLResourceOptions](mtlresourceoptions.md) — Optional arguments used to set the behavior of a resource.
- [MTLResourceID](mtlresourceid.md)
