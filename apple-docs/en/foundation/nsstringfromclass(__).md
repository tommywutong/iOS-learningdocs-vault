---
title: 'NSStringFromClass(_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstringfromclass(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstringfromclass(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstringfromclass%28_%3A%29.json'
content_hash: 'sha256:567d4a1156d14cbe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSStringFromClass(_:)

<sub>Function</sub>

Returns the name of a class as a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSStringFromClass(_ aClass: AnyClass) -> String
```

## Parameters

- `aClass` — A class.

## Return Value

A string containing the name of `aClass`. If `aClass` is `nil`, returns `nil`.

## See Also

### Type Lookup

- [NSClassFromString](<nsclassfromstring(__).md>) — Obtains a class by name.
- [NSSelectorFromString](<nsselectorfromstring(__).md>) — Returns the selector with a given name.
- [NSStringFromSelector](<nsstringfromselector(__).md>) — Returns a string representation of a given selector.
- [NSStringFromProtocol](<nsstringfromprotocol(__).md>) — Returns the name of a protocol as a string.
- [NSProtocolFromString](<nsprotocolfromstring(__).md>) — Returns a the protocol with a given name.
