---
title: error
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlauthenticationchallenge/error
source_url: 'https://developer.apple.com/documentation/foundation/urlauthenticationchallenge/error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlauthenticationchallenge/error.json'
content_hash: 'sha256:a53826f76124114b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLAuthenticationChallenge](../urlauthenticationchallenge.md)

# error

<sub>Instance Property</sub>

The error object representing the last authentication failure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var error: (any Error)? { get }
```

## Discussion

This value is `nil` if the protocol doesn’t use errors to indicate an authentication failure.

## See Also

### Related Documentation

- [failureResponse](failureresponse.md) — The URL response object representing the last authentication failure.
