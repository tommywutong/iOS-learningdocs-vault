---
title: callStackSymbols
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsexception/callstacksymbols
source_url: 'https://developer.apple.com/documentation/foundation/nsexception/callstacksymbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexception/callstacksymbols.json'
content_hash: 'sha256:ea2374fb96099f13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSException](../nsexception.md)

# callStackSymbols

<sub>Instance Property</sub>

An array containing the current call stack symbols.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var callStackSymbols: [String] { get }
```

## Discussion

An array of strings describing the call stack backtrace at the moment the exception was first raised. The format of each string is determined by the `backtrace_symbols()` API

## See Also

### Getting Exception Stack Frames

- [callStackReturnAddresses](callstackreturnaddresses.md) — The call return addresses related to a raised exception.
