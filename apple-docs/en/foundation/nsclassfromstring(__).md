---
title: 'NSClassFromString(_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsclassfromstring(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsclassfromstring(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsclassfromstring%28_%3A%29.json'
content_hash: 'sha256:cfd2fac242343029'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSClassFromString(_:)

<sub>Function</sub>

Obtains a class by name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSClassFromString(_ aClassName: String) -> AnyClass?
```

## Parameters

- `aClassName` — The name of a class.

## Return Value

The class object named by `aClassName`, or `nil` if no class by that name is currently loaded. If `aClassName` is `nil`, returns `nil`.

## See Also

### Type Lookup

- [NSStringFromClass](<nsstringfromclass(__).md>) — Returns the name of a class as a string.
- [NSSelectorFromString](<nsselectorfromstring(__).md>) — Returns the selector with a given name.
- [NSStringFromSelector](<nsstringfromselector(__).md>) — Returns a string representation of a given selector.
- [NSStringFromProtocol](<nsstringfromprotocol(__).md>) — Returns the name of a protocol as a string.
- [NSProtocolFromString](<nsprotocolfromstring(__).md>) — Returns a the protocol with a given name.
