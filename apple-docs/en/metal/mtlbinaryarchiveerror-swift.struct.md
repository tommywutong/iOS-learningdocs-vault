---
title: MTLBinaryArchiveError
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlbinaryarchiveerror-swift.struct
source_url: 'https://developer.apple.com/documentation/metal/mtlbinaryarchiveerror-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbinaryarchiveerror-swift.struct.json'
content_hash: 'sha256:127d8ac6ce08b38e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLBinaryArchiveError

<sub>Structure</sub>

An error that occurred when creating a binary shader archive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLBinaryArchiveError
```

## Relationships

- **Conforms To**: [CustomNSError](../foundation/customnserror.md), [Equatable](../swift/equatable.md), [Error](../swift/error.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Error codes

- [none](mtlbinaryarchiveerror-swift.struct/none.md) — An error code that represents the absence of any problems.
- [invalidFile](mtlbinaryarchiveerror-swift.struct/invalidfile.md) — An error code that indicates an app is using an invalid reference to an archive file, typically related to a URL.
- [compilationFailure](mtlbinaryarchiveerror-swift.struct/compilationfailure.md) — An error code that indicates the archive’s inability to compile its contents, typically when serializing it to a URL.
- [unexpectedElement](mtlbinaryarchiveerror-swift.struct/unexpectedelement.md) — An error code that indicates a problem with a configuration, typically in a descriptor or an archive’s inability to add linked functions.
- [internalError](mtlbinaryarchiveerror-swift.struct/internalerror.md) — An error code that indicates the Metal framework has an internal problem.
- [Code](mtlbinaryarchiveerror-swift.struct/code.md) — Error codes when creating binary archives of compiled shader code.

### Error domain

- [errorDomain](mtlbinaryarchiveerror-swift.struct/errordomain.md) — The current binary archive error domain.
- [MTLBinaryArchiveDomain](mtlbinaryarchivedomain.md) — The domain for Metal binary archive errors.

## See Also

### Structures

- [MTLTensorError](mtltensorerror-swift.struct.md)
- [MTLCommandBufferError](mtlcommandbuffererror-swift.struct.md) — The command buffer error codes that indicate why the GPU doesn’t finish executing a command buffer.
- [MTLComponentTransform](mtlcomponenttransform.md)
- [MTLCounterSampleBufferError](mtlcountersamplebuffererror-swift.struct.md) — The error codes that indicate why a GPU driver can’t create a counter sample buffer.
- [MTLDynamicLibraryError](mtldynamiclibraryerror-swift.struct.md) — Errors when compiling dynamic libraries.
- [MTLIOError](mtlioerror-swift.struct.md) — The categories of errors for creating an input/output file handle.
- [MTLPackedFloatQuaternion](mtlpackedfloatquaternion.md)
- [MTLStitchedLibraryOptions](mtlstitchedlibraryoptions.md)
- [NSDeviceCertification](nsdevicecertification.md)
- [NSProcessPerformanceProfile](nsprocessperformanceprofile.md) — A value describing the device’s performance profile.
