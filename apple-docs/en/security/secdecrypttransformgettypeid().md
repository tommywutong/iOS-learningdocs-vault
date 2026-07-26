---
title: SecDecryptTransformGetTypeID()
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/secdecrypttransformgettypeid()
source_url: 'https://developer.apple.com/documentation/security/secdecrypttransformgettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secdecrypttransformgettypeid%28%29.json'
content_hash: 'sha256:d9b4e50c77f3617e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecDecryptTransformGetTypeID()

<sub>Function</sub>

Returns the unique identifier of the opaque type to which a decryption transform belongs.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecDecryptTransformGetTypeID() -> CFTypeID
```

## Return Value

A value that identifies the opaque type of a [SecTransform](sectransform.md) object meant for decryption.
