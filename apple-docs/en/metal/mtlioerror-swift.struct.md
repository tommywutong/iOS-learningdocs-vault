---
title: MTLIOError
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlioerror-swift.struct
source_url: 'https://developer.apple.com/documentation/metal/mtlioerror-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlioerror-swift.struct.json'
content_hash: 'sha256:07d740a013a40b7e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIOError

<sub>Structure</sub>

The categories of errors for creating an input/output file handle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLIOError
```

## Relationships

- **Conforms To**: [CustomNSError](../foundation/customnserror.md), [Equatable](../swift/equatable.md), [Error](../swift/error.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Error codes

- [urlInvalid](mtlioerror-swift.struct/urlinvalid.md) — An error that represents a problem with a file URL.
- [internal](mtlioerror-swift.struct/internal.md) — An error that represents a problem internal to the Metal framework.
- [Code](mtlioerror-swift.struct/code.md) — The error codes for creating an input/output file handle.

### Error domain

- [errorDomain](mtlioerror-swift.struct/errordomain.md) — The current error domain for input/output command queues.
- [MTLIOErrorDomain](mtlioerrordomain.md) — The domain for input/output command queue errors.

## See Also

### Structures

- [MTLTensorError](mtltensorerror-swift.struct.md)
- [MTLBinaryArchiveError](mtlbinaryarchiveerror-swift.struct.md) — An error that occurred when creating a binary shader archive.
- [MTLCommandBufferError](mtlcommandbuffererror-swift.struct.md) — The command buffer error codes that indicate why the GPU doesn’t finish executing a command buffer.
- [MTLComponentTransform](mtlcomponenttransform.md)
- [MTLCounterSampleBufferError](mtlcountersamplebuffererror-swift.struct.md) — The error codes that indicate why a GPU driver can’t create a counter sample buffer.
- [MTLDynamicLibraryError](mtldynamiclibraryerror-swift.struct.md) — Errors when compiling dynamic libraries.
- [MTLPackedFloatQuaternion](mtlpackedfloatquaternion.md)
- [MTLStitchedLibraryOptions](mtlstitchedlibraryoptions.md)
- [NSDeviceCertification](nsdevicecertification.md)
- [NSProcessPerformanceProfile](nsprocessperformanceprofile.md) — A value describing the device’s performance profile.
