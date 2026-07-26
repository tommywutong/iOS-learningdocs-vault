---
title: commandTypes
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectcommandbufferdescriptor/commandtypes
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcommandbufferdescriptor/commandtypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcommandbufferdescriptor/commandtypes.json'
content_hash: 'sha256:55d72703519b9a79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectCommandBufferDescriptor](../mtlindirectcommandbufferdescriptor.md)

# commandTypes

<sub>Instance Property</sub>

The set of command types that you can encode into the indirect command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var commandTypes: MTLIndirectCommandType { get set }
```

## Discussion

When you create the indirect command buffer, Metal allocates memory for each command it can hold. It needs to allocate enough memory to hold any command that you might later encode. To save space, specify only the command types you are going to encode in the indirect command buffer.

You can’t combine rendering and compute commands in the same indirect command buffer.
