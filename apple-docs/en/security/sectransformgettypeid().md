---
title: SecTransformGetTypeID()
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/sectransformgettypeid()
source_url: 'https://developer.apple.com/documentation/security/sectransformgettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformgettypeid%28%29.json'
content_hash: 'sha256:92de2eef48088bda'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTransformGetTypeID()

<sub>Function</sub>

Returns the unique identifier of the opaque type to which a security transform object belongs.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecTransformGetTypeID() -> CFTypeID
```

## Return Value

A value that identifies the opaque type of a [SecTransform](sectransform.md) object.
