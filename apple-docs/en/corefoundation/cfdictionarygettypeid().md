---
title: CFDictionaryGetTypeID()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfdictionarygettypeid()
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionarygettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionarygettypeid%28%29.json'
content_hash: 'sha256:96445d8ddae49c81'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDictionaryGetTypeID()

<sub>Function</sub>

Returns the type identifier for the CFDictionary opaque type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDictionaryGetTypeID() -> CFTypeID
```

## Return Value

The type identifier for the CFDictionary opaque type.

## Discussion

CFMutableDictionary objects have the same type identifier as CFDictionary objects.
