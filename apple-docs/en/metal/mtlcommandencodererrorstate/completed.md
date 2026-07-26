---
title: MTLCommandEncoderErrorState.completed
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandencodererrorstate/completed
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandencodererrorstate/completed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandencodererrorstate/completed.json'
content_hash: 'sha256:4d4a916964c72284'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandEncoderErrorState](../mtlcommandencodererrorstate.md)

# MTLCommandEncoderErrorState.completed

<sub>Case</sub>

A state that indicates the GPU successfully executed the commands without any errors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case completed
```

## See Also

### Getting the error state

- [MTLCommandEncoderErrorStatePending](pending.md) — An error state that indicates the GPU didn’t execute the commands.
- [MTLCommandEncoderErrorStateAffected](affected.md) — An error state that indicates the GPU failed to fully execute the commands because of an error.
- [MTLCommandEncoderErrorStateFaulted](faulted.md) — An error state that indicates the commands in the command buffer are the cause of an error.
- [MTLCommandEncoderErrorStateUnknown](unknown.md) — An error state that indicates the command buffer doesn’t know the state of its commands on the GPU.
