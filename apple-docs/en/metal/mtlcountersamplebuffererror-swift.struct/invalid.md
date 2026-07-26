---
title: invalid
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcountersamplebuffererror-swift.struct/invalid
source_url: 'https://developer.apple.com/documentation/metal/mtlcountersamplebuffererror-swift.struct/invalid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcountersamplebuffererror-swift.struct/invalid.json'
content_hash: 'sha256:57b67203eb04bcd0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCounterSampleBufferError](../mtlcountersamplebuffererror-swift.struct.md)

# invalid

<sub>Type Property</sub>

An error code that indicates the descriptor for creating a counter sample buffer descriptor has an invalid property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var invalid: MTLCounterSampleBufferError.Code { get }
```

## Discussion

This error applies to the [MTLDevice](../mtldevice.md) protocol’s [- newCounterSampleBufferWithDescriptor:error:](<../mtldevice/makecountersamplebuffer(descriptor_).md>) method and its [MTLCounterSampleBufferDescriptor](../mtlcountersamplebufferdescriptor.md) parameter.

## See Also

### Error code values

- [outOfMemory](outofmemory.md) — An error code that indicates the GPU device doesn’t have sufficient memory to create a counter sample buffer.
- [internal](internal.md) — An error code that indicates the Metal framework has an internal problem.
- [Code](code.md) — The underlying error code type that indicates why a GPU driver can’t create a counter sample buffer.
