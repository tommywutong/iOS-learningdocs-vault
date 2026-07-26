---
title: SecTransformCreateFP
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/sectransformcreatefp
source_url: 'https://developer.apple.com/documentation/security/sectransformcreatefp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformcreatefp.json'
content_hash: 'sha256:05e86bed50d63828'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTransformCreateFP

<sub>Type Alias</sub>

A pointer to a function that creates a new instance of a custom transform.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
typealias SecTransformCreateFP = (CFString, SecTransform, SecTransformImplementationRef) -> () -> Unmanaged<CFError>?
```

## Parameters

- `name` — The name of the new custom transform. This name must be unique.

- `newTransform` — The newly created transform.

- `ref` — A reference that is bound to an instance of a custom transform.

## Return Value

A [SecTransformInstanceBlock](sectransforminstanceblock.md) that is used to create a new instance of a custom transform.

## Discussion

Provide a function of this type to the [SecTransformCreate](<sectransformcreate(____).md>) function when creating a custom transform. The function defined here returns an object of type [SecTransformInstanceBlock](sectransforminstanceblock.md) that provides the implementation of all of the overrides necessary to create the custom transform. This returned [SecTransformInstanceBlock](sectransforminstanceblock.md) is also where the “instance” variables for the custom transform may be defined.
