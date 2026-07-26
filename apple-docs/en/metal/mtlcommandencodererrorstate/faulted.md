---
title: MTLCommandEncoderErrorState.faulted
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandencodererrorstate/faulted
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandencodererrorstate/faulted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandencodererrorstate/faulted.json'
content_hash: 'sha256:e707389b6a72df3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandEncoderErrorState](../mtlcommandencodererrorstate.md)

# MTLCommandEncoderErrorState.faulted

<sub>Case</sub>

An error state that indicates the commands in the command buffer are the cause of an error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case faulted
```

## See Also

### Getting the error state

- [MTLCommandEncoderErrorStateCompleted](completed.md) — A state that indicates the GPU successfully executed the commands without any errors.
- [MTLCommandEncoderErrorStatePending](pending.md) — An error state that indicates the GPU didn’t execute the commands.
- [MTLCommandEncoderErrorStateAffected](affected.md) — An error state that indicates the GPU failed to fully execute the commands because of an error.
- [MTLCommandEncoderErrorStateUnknown](unknown.md) — An error state that indicates the command buffer doesn’t know the state of its commands on the GPU.
