---
title: class()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsproxy/class()
source_url: 'https://developer.apple.com/documentation/foundation/nsproxy/class()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsproxy/class%28%29.json'
content_hash: 'sha256:88e8203a252d41b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSProxy](../nsproxy.md)

# class()

<sub>Type Method</sub>

Returns `self` (the class object).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func `class`() -> AnyClass
```

## Return Value

`self`. Because this is a class method, it returns the class object

## See Also

### Describing a Proxy Class or Object

- [description](description.md) — A string containing the real class name and the id of the receiver as a hexadecimal number.
- [debugDescription](debugdescription.md) — A string containing a human-readable description of the receiver suitable for debugging.
