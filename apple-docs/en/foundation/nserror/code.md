---
title: code
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nserror/code
source_url: 'https://developer.apple.com/documentation/foundation/nserror/code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nserror/code.json'
content_hash: 'sha256:bcb7a6134e2e6abf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSError](../nserror.md)

# code

<sub>Instance Property</sub>

The error code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var code: Int { get }
```

## Discussion

Note that errors are domain-specific.

## See Also

### Related Documentation

- [localizedDescription](localizeddescription.md) — A string containing the localized description of the error.

### Getting Error Properties

- [domain](domain.md) — A string containing the error domain.
- [userInfo](userinfo.md) — The user info dictionary.
