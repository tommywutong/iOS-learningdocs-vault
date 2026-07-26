---
title: MTLDynamicLibraryError
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldynamiclibraryerror-swift.struct
source_url: 'https://developer.apple.com/documentation/metal/mtldynamiclibraryerror-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldynamiclibraryerror-swift.struct.json'
content_hash: 'sha256:d47ec9054721d5c0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLDynamicLibraryError

<sub>Structure</sub>

Errors when compiling dynamic libraries.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLDynamicLibraryError
```

## Relationships

- **Conforms To**: [CustomNSError](../foundation/customnserror.md), [Equatable](../swift/equatable.md), [Error](../swift/error.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Error codes

- [none](mtldynamiclibraryerror-swift.struct/none.md) — An error code that represents the absence of any problems.
- [invalidFile](mtldynamiclibraryerror-swift.struct/invalidfile.md) — An error code that indicates an app is using an invalid reference to a library file, typically related to a URL.
- [compilationFailure](mtldynamiclibraryerror-swift.struct/compilationfailure.md) — An error code that indicates Metal couldn’t compile a dynamic library.
- [unresolvedInstallName](mtldynamiclibraryerror-swift.struct/unresolvedinstallname.md) — An error code that indicates Metal couldn’t resolve the installation name for a new dynamic library.
- [dependencyLoadFailure](mtldynamiclibraryerror-swift.struct/dependencyloadfailure.md) — An error code that indicates a dynamic library couldn’t link to other dynamic libraries.
- [unsupported](mtldynamiclibraryerror-swift.struct/unsupported.md) — An error code that indicates the GPU device doesn’t support dynamic libraries.
- [Code](mtldynamiclibraryerror-swift.struct/code.md) — Error codes that Metal can generate when creating dynamic libraries.

### Error domain

- [errorDomain](mtldynamiclibraryerror-swift.struct/errordomain.md) — The current dynamic library error domain.
- [MTLDynamicLibraryDomain](mtldynamiclibrarydomain.md) — The domain for Metal dynamic library errors.

## See Also

### Structures

- [MTLTensorError](mtltensorerror-swift.struct.md)
- [MTLBinaryArchiveError](mtlbinaryarchiveerror-swift.struct.md) — An error that occurred when creating a binary shader archive.
- [MTLCommandBufferError](mtlcommandbuffererror-swift.struct.md) — The command buffer error codes that indicate why the GPU doesn’t finish executing a command buffer.
- [MTLComponentTransform](mtlcomponenttransform.md)
- [MTLCounterSampleBufferError](mtlcountersamplebuffererror-swift.struct.md) — The error codes that indicate why a GPU driver can’t create a counter sample buffer.
- [MTLIOError](mtlioerror-swift.struct.md) — The categories of errors for creating an input/output file handle.
- [MTLPackedFloatQuaternion](mtlpackedfloatquaternion.md)
- [MTLStitchedLibraryOptions](mtlstitchedlibraryoptions.md)
- [NSDeviceCertification](nsdevicecertification.md)
- [NSProcessPerformanceProfile](nsprocessperformanceprofile.md) — A value describing the device’s performance profile.
