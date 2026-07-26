---
title: MTLCounterSampleBufferError.Code
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcountersamplebuffererror-swift.struct/code
source_url: 'https://developer.apple.com/documentation/metal/mtlcountersamplebuffererror-swift.struct/code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcountersamplebuffererror-swift.struct/code.json'
content_hash: 'sha256:7e6865fa3b0e1c5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCounterSampleBufferError](../mtlcountersamplebuffererror-swift.struct.md)

# MTLCounterSampleBufferError.Code

<sub>Enumeration</sub>

The underlying error code type that indicates why a GPU driver can’t create a counter sample buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum Code
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Error codes

- [MTLCounterSampleBufferErrorOutOfMemory](code/outofmemory.md) — An error code that indicates the GPU device doesn’t have sufficient memory to create a counter sample buffer.
- [MTLCounterSampleBufferErrorInvalid](code/invalid.md) — An error code that indicates when a counter-sample buffer descriptor has at least one invalid property.
- [MTLCounterSampleBufferErrorInternal](code/internal.md) — An error code that indicates the Metal framework has an internal problem.
- [MTLCounterSampleBufferErrorOutOfMemory](code/outofmemory.md) — An error code that indicates the GPU device doesn’t have sufficient memory to create a counter sample buffer.
- [MTLCounterSampleBufferErrorInvalid](code/invalid.md) — An error code that indicates when a counter-sample buffer descriptor has at least one invalid property.
- [MTLCounterSampleBufferErrorInternal](code/internal.md) — An error code that indicates the Metal framework has an internal problem.

### Initializers

- [init(rawValue:)](<code/init(rawvalue_).md>)
