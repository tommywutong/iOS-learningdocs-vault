---
title: currentUser
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nstermofaddress/currentuser
source_url: 'https://developer.apple.com/documentation/foundation/nstermofaddress/currentuser'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstermofaddress/currentuser.json'
content_hash: 'sha256:7ecaaa6fec77241d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTermOfAddress](../nstermofaddress.md)

# currentUser

<sub>Type Method</sub>

The term of address that should be used for addressing the user

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) currentUser;
```

## Discussion

This term of address will only compare equal to another `+[NSTermOfAddress currentUser]`
