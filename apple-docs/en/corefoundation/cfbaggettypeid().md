---
title: CFBagGetTypeID()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfbaggettypeid()
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbaggettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbaggettypeid%28%29.json'
content_hash: 'sha256:1c5a744b7100d851'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBagGetTypeID()

<sub>Function</sub>

Returns the type identifier for the CFBag opaque type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBagGetTypeID() -> CFTypeID
```

## Return Value

The type identifier for the CFBag opaque type.

## Discussion

CFMutableBag objects have the same type identifier as CFBag objects.
