---
title: MTLCounterSampleBufferError.Code.invalid
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcountersamplebuffererror-swift.struct/code/invalid
source_url: 'https://developer.apple.com/documentation/metal/mtlcountersamplebuffererror-swift.struct/code/invalid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcountersamplebuffererror-swift.struct/code/invalid.json'
content_hash: 'sha256:5a36736f137e10d0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Metal](../../../metal.md) · [MTLCounterSampleBufferError](../../mtlcountersamplebuffererror-swift.struct.md) · [Code](../code.md)

# MTLCounterSampleBufferError.Code.invalid

<sub>Case</sub>

An error code that indicates when a counter-sample buffer descriptor has at least one invalid property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case invalid
```

## Discussion

This error applies to the [MTLDevice](../../mtldevice.md) protocol’s [- newCounterSampleBufferWithDescriptor:error:](<../../mtldevice/makecountersamplebuffer(descriptor_).md>) method and its [MTLCounterSampleBufferDescriptor](../../mtlcountersamplebufferdescriptor.md) parameter.

## See Also

### Error codes

- [MTLCounterSampleBufferErrorOutOfMemory](outofmemory.md) — An error code that indicates the GPU device doesn’t have sufficient memory to create a counter sample buffer.
- [MTLCounterSampleBufferErrorInternal](internal.md) — An error code that indicates the Metal framework has an internal problem.
- [MTLCounterSampleBufferErrorOutOfMemory](outofmemory.md) — An error code that indicates the GPU device doesn’t have sufficient memory to create a counter sample buffer.
- [MTLCounterSampleBufferErrorInternal](internal.md) — An error code that indicates the Metal framework has an internal problem.
