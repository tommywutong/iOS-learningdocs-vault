---
title: debugSignposts
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbufferencoderinfo/debugsignposts
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbufferencoderinfo/debugsignposts'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbufferencoderinfo/debugsignposts.json'
content_hash: 'sha256:2d299c5bc6c3227a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBufferEncoderInfo](../mtlcommandbufferencoderinfo.md)

# debugSignposts

<sub>Instance Property</sub>

An array of debug signposts that Metal records as the GPU executes the commands of the encoder’s pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var debugSignposts: [String] { get }
```

## See Also

### Inspecting execution information

- [label](label.md) — The name of the encoder that generates the error information.
- [errorState](errorstate.md) — The execution status of the command encoder.
- [MTLCommandEncoderErrorState](../mtlcommandencodererrorstate.md) — Possible error conditions for the command encoder’s commands.
