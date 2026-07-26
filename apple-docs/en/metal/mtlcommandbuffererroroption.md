---
title: MTLCommandBufferErrorOption
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffererroroption
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffererroroption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffererroroption.json'
content_hash: 'sha256:c3c71f807c9d7274'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCommandBufferErrorOption

<sub>Structure</sub>

Options for reporting errors from a command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLCommandBufferErrorOption
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Buffer error options

- [MTLCommandBufferErrorOptionEncoderExecutionStatus](mtlcommandbuffererroroption/encoderexecutionstatus.md) — An option that instructs a command buffer to save additional details about a GPU runtime error.

### Protocol support

- [init(rawValue:)](<mtlcommandbuffererroroption/init(rawvalue_).md>) — Creates a set of error options from a raw integer value.

## See Also

### Configuring the command buffer

- [logState](mtlcommandbufferdescriptor/logstate.md) — The shader logging configuration that the command buffer uses.
- [retainedReferences](mtlcommandbufferdescriptor/retainedreferences.md) — A Boolean value that indicates whether the command buffer the descriptor creates maintains strong references to the resources it uses.
- [errorOptions](mtlcommandbufferdescriptor/erroroptions.md) — The reporting configuration that indicates which information the GPU driver stores in a command buffer’s error property.
