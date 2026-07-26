---
title: dsohandle()
framework: Swift
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/dsohandle()
source_url: 'https://developer.apple.com/documentation/swift/dsohandle()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dsohandle%28%29.json'
content_hash: 'sha256:90e9188fe760ff43'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# dsohandle()

<sub>Macro</sub>

Produces the dynamic shared object (DSO) handle in use where the macro appears.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@freestanding(expression) macro dsohandle() -> UnsafeRawPointer
```

## Return Value

The DSO handle.
