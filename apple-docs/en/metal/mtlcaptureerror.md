---
title: MTLCaptureError
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcaptureerror
source_url: 'https://developer.apple.com/documentation/metal/mtlcaptureerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcaptureerror.json'
content_hash: 'sha256:b594ad2cf1780d3e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCaptureError

<sub>Enumeration</sub>

Errors returned by capture sessions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLCaptureError
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Errors

- [MTLCaptureErrorAlreadyCapturing](mtlcaptureerror/alreadycapturing.md) — A capture error that indicates the session is already in progress.
- [MTLCaptureErrorInvalidDescriptor](mtlcaptureerror/invaliddescriptor.md) — A capture error that indicates your descriptor has invalid properties.
- [MTLCaptureErrorNotSupported](mtlcaptureerror/notsupported.md) — A capture error that indicates the capture options you’re requesting aren’t available.

### Initializers

- [init(rawValue:)](<mtlcaptureerror/init(rawvalue_).md>)

## See Also

### Capture errors

- [MTLCaptureErrorDomain](mtlcaptureerrordomain.md) — The error domain for capture errors.
