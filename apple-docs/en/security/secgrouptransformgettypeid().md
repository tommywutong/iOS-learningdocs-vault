---
title: SecGroupTransformGetTypeID()
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/secgrouptransformgettypeid()
source_url: 'https://developer.apple.com/documentation/security/secgrouptransformgettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secgrouptransformgettypeid%28%29.json'
content_hash: 'sha256:0de701d9fd8e0c39'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecGroupTransformGetTypeID()

<sub>Function</sub>

Returns the Core Foundation type ID for a transform group container.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecGroupTransformGetTypeID() -> CFTypeID
```

## Return Value

A value that identifies the opaque type of a [SecGroupTransform](secgrouptransform.md) object.
