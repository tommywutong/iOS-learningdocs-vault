---
title: CFSetGetTypeID()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfsetgettypeid()
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsetgettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsetgettypeid%28%29.json'
content_hash: 'sha256:284c8634a57b3f01'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSetGetTypeID()

<sub>Function</sub>

Returns the type identifier for the CFSet type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSetGetTypeID() -> CFTypeID
```

## Return Value

The type identifier for the CFSet type.

## Discussion

CFMutableSet has the same type identifier as CFSet.
