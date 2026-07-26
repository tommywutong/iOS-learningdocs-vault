---
title: userInfo
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nserror/userinfo
source_url: 'https://developer.apple.com/documentation/foundation/nserror/userinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nserror/userinfo.json'
content_hash: 'sha256:4ff68af4eec60c7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSError](../nserror.md)

# userInfo

<sub>Instance Property</sub>

The user info dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var userInfo: [String : Any] { get }
```

## Discussion

If the user info dictionary has not been set, this property is `nil`.

On macOS 10.8 or later, if the user info dictionary has not been set, this property returns an empty dictionary.

## See Also

### Related Documentation

- [localizedDescription](localizeddescription.md) — A string containing the localized description of the error.

### Getting Error Properties

- [code](code.md) — The error code.
- [domain](domain.md) — A string containing the error domain.
