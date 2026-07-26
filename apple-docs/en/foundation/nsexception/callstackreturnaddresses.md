---
title: callStackReturnAddresses
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsexception/callstackreturnaddresses
source_url: 'https://developer.apple.com/documentation/foundation/nsexception/callstackreturnaddresses'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexception/callstackreturnaddresses.json'
content_hash: 'sha256:81d095e2ec5b990e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSException](../nsexception.md)

# callStackReturnAddresses

<sub>Instance Property</sub>

The call return addresses related to a raised exception.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var callStackReturnAddresses: [NSNumber] { get }
```

## Discussion

An array of [NSNumber](../nsnumber.md) objects encapsulating [NSUInteger](../../objectivec/nsuinteger.md) values. Each value is a call frame return address. The array of stack frames starts at the point at which the exception was first raised, with the first items being the most recent stack frames.

`NSException` subclasses posing as the `NSException` class or subclasses or other API elements that interfere with the exception-raising mechanism may not get this information.

## See Also

### Getting Exception Stack Frames

- [callStackSymbols](callstacksymbols.md) — An array containing the current call stack symbols.
