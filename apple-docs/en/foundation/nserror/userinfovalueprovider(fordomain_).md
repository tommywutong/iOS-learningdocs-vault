---
title: 'userInfoValueProvider(forDomain:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nserror/userinfovalueprovider(fordomain:)'
source_url: 'https://developer.apple.com/documentation/foundation/nserror/userinfovalueprovider(fordomain:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nserror/userinfovalueprovider%28fordomain%3A%29.json'
content_hash: 'sha256:6432838ce487854f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSError](../nserror.md)

# userInfoValueProvider(forDomain:)

<sub>Type Method</sub>

Returns any user info provider specified for a given error domain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func userInfoValueProvider(forDomain errorDomain: String) -> (@Sendable (any Error, String) -> Any?)?
```

## Parameters

- `errorDomain` — The error domain of the user info provider.

## Return Value

The user info provider of the error domain, or `nil` if none is specified.

## See Also

### Providing Error User Info

- [+ setUserInfoValueProviderForDomain:provider:](<setuserinfovalueprovider(fordomain_provider_).md>) — Specifies a block to call when the corresponding property is not present in the user info dictionary.
- [ErrorUserInfoKey](../erroruserinfokey.md) — These keys may exist in the user info dictionary.
- [UserInfoKey](userinfokey.md) — These keys may exist in the user info dictionary.
