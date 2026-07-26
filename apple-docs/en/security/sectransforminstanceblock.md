---
title: SecTransformInstanceBlock
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sectransforminstanceblock
source_url: 'https://developer.apple.com/documentation/security/sectransforminstanceblock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransforminstanceblock.json'
content_hash: 'sha256:88f7a81b53e07390'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTransformInstanceBlock

<sub>Type Alias</sub>

A block that you return from a transform creation function.

<sub>Mac Catalyst, macOS</sub>

```swift
typealias SecTransformInstanceBlock = () -> Unmanaged<CFError>?
```

## Return Value

A an error object if an error occurred.

## Discussion

You return a block of this type from the custom transform creation function of type [SecTransformCreateFP](sectransformcreatefp.md) that you register with the [SecTransformRegister](<sectransformregister(______).md>) function.
