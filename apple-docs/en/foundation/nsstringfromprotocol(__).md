---
title: 'NSStringFromProtocol(_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstringfromprotocol(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstringfromprotocol(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstringfromprotocol%28_%3A%29.json'
content_hash: 'sha256:4bb060b0f8748b04'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSStringFromProtocol(_:)

<sub>Function</sub>

Returns the name of a protocol as a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSStringFromProtocol(_ proto: Protocol) -> String
```

## Parameters

- `proto` — A protocol.

## Return Value

A string containing the name of `proto`.

## See Also

### Type Lookup

- [NSClassFromString](<nsclassfromstring(__).md>) — Obtains a class by name.
- [NSStringFromClass](<nsstringfromclass(__).md>) — Returns the name of a class as a string.
- [NSSelectorFromString](<nsselectorfromstring(__).md>) — Returns the selector with a given name.
- [NSStringFromSelector](<nsstringfromselector(__).md>) — Returns a string representation of a given selector.
- [NSProtocolFromString](<nsprotocolfromstring(__).md>) — Returns a the protocol with a given name.
