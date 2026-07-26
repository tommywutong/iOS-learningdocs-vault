---
title: errorState
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbufferencoderinfo/errorstate
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbufferencoderinfo/errorstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbufferencoderinfo/errorstate.json'
content_hash: 'sha256:e5d71cb1032af219'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBufferEncoderInfo](../mtlcommandbufferencoderinfo.md)

# errorState

<sub>Instance Property</sub>

The execution status of the command encoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var errorState: MTLCommandEncoderErrorState { get }
```

## See Also

### Inspecting execution information

- [label](label.md) — The name of the encoder that generates the error information.
- [debugSignposts](debugsignposts.md) — An array of debug signposts that Metal records as the GPU executes the commands of the encoder’s pass.
- [MTLCommandEncoderErrorState](../mtlcommandencodererrorstate.md) — Possible error conditions for the command encoder’s commands.
