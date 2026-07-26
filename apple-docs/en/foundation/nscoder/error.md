---
title: error
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscoder/error
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/error.json'
content_hash: 'sha256:3f07530f27962458'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# error

<sub>Instance Property</sub>

An error in the top-level encode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var error: (any Error)? { get }
```

## Discussion

The meaning of this property depends on the setting of the [decodingFailurePolicy](decodingfailurepolicy-swift.property.md) property. For [NSDecodingFailurePolicyRaiseException](decodingfailurepolicy-swift.enum/raiseexception.md), this property is always `nil`. For [NSDecodingFailurePolicySetErrorAndReturn](decodingfailurepolicy-swift.enum/seterrorandreturn.md), a non-`nil` value represents the first error encountered while decoding the archive.

## See Also

### Managing Decode Errors

- [- failWithError:](<failwitherror(__).md>) — Signals to this coder that the decode operation has failed.
