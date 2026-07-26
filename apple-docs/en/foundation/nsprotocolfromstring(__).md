---
title: 'NSProtocolFromString(_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsprotocolfromstring(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsprotocolfromstring(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsprotocolfromstring%28_%3A%29.json'
content_hash: 'sha256:6bb4f994430ef5aa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSProtocolFromString(_:)

<sub>Function</sub>

Returns a the protocol with a given name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSProtocolFromString(_ namestr: String) -> Protocol?
```

## Parameters

- `namestr` — The name of a protocol.

## Return Value

The protocol object named by `namestr`, or `nil` if no protocol by that name is currently loaded. If `namestr` is `nil`, returns `nil`.

## See Also

### Type Lookup

- [NSClassFromString](<nsclassfromstring(__).md>) — Obtains a class by name.
- [NSStringFromClass](<nsstringfromclass(__).md>) — Returns the name of a class as a string.
- [NSSelectorFromString](<nsselectorfromstring(__).md>) — Returns the selector with a given name.
- [NSStringFromSelector](<nsstringfromselector(__).md>) — Returns a string representation of a given selector.
- [NSStringFromProtocol](<nsstringfromprotocol(__).md>) — Returns the name of a protocol as a string.
