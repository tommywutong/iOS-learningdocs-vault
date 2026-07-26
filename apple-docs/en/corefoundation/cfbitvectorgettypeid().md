---
title: CFBitVectorGetTypeID()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfbitvectorgettypeid()
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbitvectorgettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbitvectorgettypeid%28%29.json'
content_hash: 'sha256:d19d388e659605ba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBitVectorGetTypeID()

<sub>Function</sub>

Returns the type identifier for the CFBitVector opaque type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBitVectorGetTypeID() -> CFTypeID
```

## Return Value

The type identifier for the CFBitVector opaque type.

## Discussion

CFMutableBitVector objects have the same type identifier as CFBitVector objects.
