---
title: CFAttributedStringGetTypeID()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfattributedstringgettypeid()
source_url: 'https://developer.apple.com/documentation/corefoundation/cfattributedstringgettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfattributedstringgettypeid%28%29.json'
content_hash: 'sha256:67f3a88850bc0195'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAttributedStringGetTypeID()

<sub>Function</sub>

Returns the type identifier for the CFAttributedString opaque type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAttributedStringGetTypeID() -> CFTypeID
```

## Return Value

The type identifier for the CFAttributedString opaque type.

## Discussion

CFMutableAttributedString objects have the same type identifier as CFAttributedString objects.
