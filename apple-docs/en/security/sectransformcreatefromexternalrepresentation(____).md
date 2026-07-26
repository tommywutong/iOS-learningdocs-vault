---
title: 'SecTransformCreateFromExternalRepresentation(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sectransformcreatefromexternalrepresentation(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectransformcreatefromexternalrepresentation(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformcreatefromexternalrepresentation%28_%3A_%3A%29.json'
content_hash: 'sha256:c6ed3a6cd6a0271a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTransformCreateFromExternalRepresentation(_:_:)

<sub>Function</sub>

Creates a transform instance from a dictionary of parameters.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecTransformCreateFromExternalRepresentation(_ dictionary: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform?
```

## Parameters

- `dictionary` — The dictionary of parameters.

- `error` — An optional pointer to a CFErrorRef. This value is set if an error occurred. If not NULL the caller is responsible for releasing the CFErrorRef.

## Return Value

A pointer to a SecTransformRef object. You must release the object with CFRelease when you are done with it. A NULL will be returned if an error occurred during initialization, and if the error parameter is non-null, it contains the specific error data.
