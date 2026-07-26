---
title: SecEncryptTransformGetTypeID()
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/secencrypttransformgettypeid()
source_url: 'https://developer.apple.com/documentation/security/secencrypttransformgettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secencrypttransformgettypeid%28%29.json'
content_hash: 'sha256:e34269ab3817291e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecEncryptTransformGetTypeID()

<sub>Function</sub>

Returns the unique identifier of the opaque type to which an encryption transform belongs.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecEncryptTransformGetTypeID() -> CFTypeID
```

## Return Value

A value that identifies the opaque type of a [SecTransform](sectransform.md) object meant for encryption.
