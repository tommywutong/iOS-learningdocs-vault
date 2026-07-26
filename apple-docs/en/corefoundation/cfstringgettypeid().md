---
title: CFStringGetTypeID()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstringgettypeid()
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringgettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringgettypeid%28%29.json'
content_hash: 'sha256:f861a90dd7205ec3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringGetTypeID()

<sub>Function</sub>

Returns the type identifier for the CFString opaque type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringGetTypeID() -> CFTypeID
```

## Return Value

The type identifier for the CFString opaque type.

## Discussion

CFMutableString objects have the same type identifier as CFString objects.

## See Also

### Getting String Properties

- [CFShowStr](<cfshowstr(__).md>) — Prints the attributes of a string during debugging.
