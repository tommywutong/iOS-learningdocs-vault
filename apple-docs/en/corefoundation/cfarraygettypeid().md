---
title: CFArrayGetTypeID()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfarraygettypeid()
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarraygettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarraygettypeid%28%29.json'
content_hash: 'sha256:f15bcd482d23c611'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArrayGetTypeID()

<sub>Function</sub>

Returns the type identifier for the CFArray opaque type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFArrayGetTypeID() -> CFTypeID
```

## Return Value

The type identifier for the CFArray opaque type.

## Discussion

CFMutableArray objects have the same type identifier as CFArray objects.
