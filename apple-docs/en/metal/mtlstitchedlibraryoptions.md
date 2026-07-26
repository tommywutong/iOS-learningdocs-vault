---
title: MTLStitchedLibraryOptions
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstitchedlibraryoptions
source_url: 'https://developer.apple.com/documentation/metal/mtlstitchedlibraryoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstitchedlibraryoptions.json'
content_hash: 'sha256:af797c0dd0d43784'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLStitchedLibraryOptions

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLStitchedLibraryOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<mtlstitchedlibraryoptions/init(rawvalue_).md>)

### Type Properties

- [MTLStitchedLibraryOptionFailOnBinaryArchiveMiss](mtlstitchedlibraryoptions/failonbinaryarchivemiss.md) — An option that instructs the compiler to return an error when a GPU function for a stitched library isn’t in a binary archive.
- [MTLStitchedLibraryOptionStoreLibraryInMetalPipelinesScript](mtlstitchedlibraryoptions/storelibraryinmetalpipelinesscript.md)

## See Also

### Structures

- [MTLTensorError](mtltensorerror-swift.struct.md)
- [MTLBinaryArchiveError](mtlbinaryarchiveerror-swift.struct.md) — An error that occurred when creating a binary shader archive.
- [MTLCommandBufferError](mtlcommandbuffererror-swift.struct.md) — The command buffer error codes that indicate why the GPU doesn’t finish executing a command buffer.
- [MTLComponentTransform](mtlcomponenttransform.md)
- [MTLCounterSampleBufferError](mtlcountersamplebuffererror-swift.struct.md) — The error codes that indicate why a GPU driver can’t create a counter sample buffer.
- [MTLDynamicLibraryError](mtldynamiclibraryerror-swift.struct.md) — Errors when compiling dynamic libraries.
- [MTLIOError](mtlioerror-swift.struct.md) — The categories of errors for creating an input/output file handle.
- [MTLPackedFloatQuaternion](mtlpackedfloatquaternion.md)
- [NSDeviceCertification](nsdevicecertification.md)
- [NSProcessPerformanceProfile](nsprocessperformanceprofile.md) — A value describing the device’s performance profile.
