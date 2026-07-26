---
title: MTLCommandEncoderErrorState
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandencodererrorstate
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandencodererrorstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandencodererrorstate.json'
content_hash: 'sha256:0aeaab415b3ec312'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCommandEncoderErrorState

<sub>Enumeration</sub>

Possible error conditions for the command encoder’s commands.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLCommandEncoderErrorState
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the error state

- [MTLCommandEncoderErrorStateCompleted](mtlcommandencodererrorstate/completed.md) — A state that indicates the GPU successfully executed the commands without any errors.
- [MTLCommandEncoderErrorStatePending](mtlcommandencodererrorstate/pending.md) — An error state that indicates the GPU didn’t execute the commands.
- [MTLCommandEncoderErrorStateAffected](mtlcommandencodererrorstate/affected.md) — An error state that indicates the GPU failed to fully execute the commands because of an error.
- [MTLCommandEncoderErrorStateFaulted](mtlcommandencodererrorstate/faulted.md) — An error state that indicates the commands in the command buffer are the cause of an error.
- [MTLCommandEncoderErrorStateUnknown](mtlcommandencodererrorstate/unknown.md) — An error state that indicates the command buffer doesn’t know the state of its commands on the GPU.

### Initializers

- [init(rawValue:)](<mtlcommandencodererrorstate/init(rawvalue_).md>)

## See Also

### Inspecting execution information

- [label](mtlcommandbufferencoderinfo/label.md) — The name of the encoder that generates the error information.
- [debugSignposts](mtlcommandbufferencoderinfo/debugsignposts.md) — An array of debug signposts that Metal records as the GPU executes the commands of the encoder’s pass.
- [errorState](mtlcommandbufferencoderinfo/errorstate.md) — The execution status of the command encoder.
