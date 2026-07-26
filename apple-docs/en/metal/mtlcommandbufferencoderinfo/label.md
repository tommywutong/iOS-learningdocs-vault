---
title: label
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbufferencoderinfo/label
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbufferencoderinfo/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbufferencoderinfo/label.json'
content_hash: 'sha256:a8fba809c58ffca1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBufferEncoderInfo](../mtlcommandbufferencoderinfo.md)

# label

<sub>Instance Property</sub>

The name of the encoder that generates the error information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var label: String { get }
```

## Discussion

Metal assigns the value of the property to the encoder’s [label](../mtlcommandencoder/label.md) property.

## See Also

### Inspecting execution information

- [debugSignposts](debugsignposts.md) — An array of debug signposts that Metal records as the GPU executes the commands of the encoder’s pass.
- [errorState](errorstate.md) — The execution status of the command encoder.
- [MTLCommandEncoderErrorState](../mtlcommandencodererrorstate.md) — Possible error conditions for the command encoder’s commands.
