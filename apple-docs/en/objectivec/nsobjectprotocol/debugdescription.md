---
title: debugDescription
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobjectprotocol/debugdescription
source_url: 'https://developer.apple.com/documentation/objectivec/nsobjectprotocol/debugdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobjectprotocol/debugdescription.json'
content_hash: 'sha256:1173fd24ab1e6d0a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# debugDescription

<sub>Instance Property</sub>

A textual representation of the receiver to use with a debugger.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional var debugDescription: String { get }
```

## Return Value

A string that describes the object for debugging purposes.

## Discussion

The debugger’s `po` command uses this property to create a textual representation of the object suitable for display in the debugger. The default implemention returns the same value as [description](description.md). Override either property to provide custom object descriptions.

## See Also

### Describing Objects

- [description](description.md) — A textual representation of the receiver.
