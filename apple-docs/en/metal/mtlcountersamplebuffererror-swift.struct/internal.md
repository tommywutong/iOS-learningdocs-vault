---
title: internal
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcountersamplebuffererror-swift.struct/internal
source_url: 'https://developer.apple.com/documentation/metal/mtlcountersamplebuffererror-swift.struct/internal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcountersamplebuffererror-swift.struct/internal.json'
content_hash: 'sha256:56d4b0bef104b78b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCounterSampleBufferError](../mtlcountersamplebuffererror-swift.struct.md)

# internal

<sub>Type Property</sub>

An error code that indicates the Metal framework has an internal problem.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var `internal`: MTLCounterSampleBufferError.Code { get }
```

## Discussion

The local description contains the underlying error code. You can report the scenario that generated this error code with [Feedback Assistant](https://feedbackassistant.apple.com).

## See Also

### Error code values

- [outOfMemory](outofmemory.md) — An error code that indicates the GPU device doesn’t have sufficient memory to create a counter sample buffer.
- [invalid](invalid.md) — An error code that indicates the descriptor for creating a counter sample buffer descriptor has an invalid property.
- [Code](code.md) — The underlying error code type that indicates why a GPU driver can’t create a counter sample buffer.
