---
title: CFDataGetTypeID()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfdatagettypeid()
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdatagettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdatagettypeid%28%29.json'
content_hash: 'sha256:0c6262e7f2dcf3c6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDataGetTypeID()

<sub>Function</sub>

Returns the type identifier for the CFData opaque type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDataGetTypeID() -> CFTypeID
```

## Return Value

The type identifier for the CFData opaque type.

## Discussion

CFMutableData objects have the same type identifier as CFData objects.
