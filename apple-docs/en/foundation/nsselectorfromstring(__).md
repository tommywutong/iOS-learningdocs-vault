---
title: 'NSSelectorFromString(_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsselectorfromstring(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsselectorfromstring(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsselectorfromstring%28_%3A%29.json'
content_hash: 'sha256:e9c7717e0008fff2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSSelectorFromString(_:)

<sub>Function</sub>

Returns the selector with a given name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSSelectorFromString(_ aSelectorName: String) -> Selector
```

## Parameters

- `aSelectorName` — A string of any length, with any characters, that represents the name of a selector.

## Return Value

The selector named by `aSelectorName`. If `aSelectorName` is `nil`, or cannot be converted to UTF-8 (this should be only due to insufficient memory), returns `(SEL)0`.

## Discussion

To make a selector, [NSSelectorFromString](<nsselectorfromstring(__).md>) passes a UTF-8 encoded character representation of `aSelectorName` to [sel_registerName(_:)](<../objectivec/sel_registername(__).md>) and returns the value returned by that function. Note, therefore, that if the selector does not exist it is registered and the newly-registered selector is returned.

Recall that a colon (”:”) is part of a method name; `setHeight` is not the same as `setHeight:`.

## See Also

### Type Lookup

- [NSClassFromString](<nsclassfromstring(__).md>) — Obtains a class by name.
- [NSStringFromClass](<nsstringfromclass(__).md>) — Returns the name of a class as a string.
- [NSStringFromSelector](<nsstringfromselector(__).md>) — Returns a string representation of a given selector.
- [NSStringFromProtocol](<nsstringfromprotocol(__).md>) — Returns the name of a protocol as a string.
- [NSProtocolFromString](<nsprotocolfromstring(__).md>) — Returns a the protocol with a given name.
