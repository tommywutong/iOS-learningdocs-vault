---
title: CFCharacterSetGetTypeID()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfcharactersetgettypeid()
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcharactersetgettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcharactersetgettypeid%28%29.json'
content_hash: 'sha256:039ed5720d544e5a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCharacterSetGetTypeID()

<sub>Function</sub>

Returns the type identifier of the CFCharacterSet opaque type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCharacterSetGetTypeID() -> CFTypeID
```

## Return Value

The type identifier of the CFCharacterSet opaque type.

## Discussion

CFMutableCharacterSet objects have the same type identifier as CFCharacterSet objects.
