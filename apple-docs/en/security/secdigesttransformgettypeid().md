---
title: SecDigestTransformGetTypeID()
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/secdigesttransformgettypeid()
source_url: 'https://developer.apple.com/documentation/security/secdigesttransformgettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secdigesttransformgettypeid%28%29.json'
content_hash: 'sha256:b362d1b8f994d280'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecDigestTransformGetTypeID()

<sub>Function</sub>

Returns the unique identifier of the opaque type to which a digest transform belongs.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecDigestTransformGetTypeID() -> CFTypeID
```

## Return Value

A value that identifies the opaque type of a [SecTransform](sectransform.md) object meant for digests.
