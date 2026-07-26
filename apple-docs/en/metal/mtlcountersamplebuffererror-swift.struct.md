---
title: MTLCounterSampleBufferError
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcountersamplebuffererror-swift.struct
source_url: 'https://developer.apple.com/documentation/metal/mtlcountersamplebuffererror-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcountersamplebuffererror-swift.struct.json'
content_hash: 'sha256:09a4f8091bbc29b4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCounterSampleBufferError

<sub>Structure</sub>

The error codes that indicate why a GPU driver can’t create a counter sample buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLCounterSampleBufferError
```

## Relationships

- **Conforms To**: [CustomNSError](../foundation/customnserror.md), [Equatable](../swift/equatable.md), [Error](../swift/error.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Error code values

- [outOfMemory](mtlcountersamplebuffererror-swift.struct/outofmemory.md) — An error code that indicates the GPU device doesn’t have sufficient memory to create a counter sample buffer.
- [invalid](mtlcountersamplebuffererror-swift.struct/invalid.md) — An error code that indicates the descriptor for creating a counter sample buffer descriptor has an invalid property.
- [internal](mtlcountersamplebuffererror-swift.struct/internal.md) — An error code that indicates the Metal framework has an internal problem.
- [Code](mtlcountersamplebuffererror-swift.struct/code.md) — The underlying error code type that indicates why a GPU driver can’t create a counter sample buffer.

### Error domain

- [errorDomain](mtlcountersamplebuffererror-swift.struct/errordomain.md) — The current counter sample buffer error domain.
- [MTLCounterErrorDomain](mtlcountererrordomain.md) — The domain for Metal counter sample buffer errors.
