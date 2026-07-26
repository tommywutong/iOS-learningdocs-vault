---
title: protectionSpace
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlauthenticationchallenge/protectionspace
source_url: 'https://developer.apple.com/documentation/foundation/urlauthenticationchallenge/protectionspace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlauthenticationchallenge/protectionspace.json'
content_hash: 'sha256:29c0d7ccf1bccdc9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLAuthenticationChallenge](../urlauthenticationchallenge.md)

# protectionSpace

<sub>Instance Property</sub>

The receiver’s protection space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var protectionSpace: URLProtectionSpace { get }
```

## Discussion

A protection space object provides additional information about the authentication request, such as the host, port, authentication realm, and so on. The protection space also tells you whether the authentication challenge is asking you to provide the user’s credentials or to verify the TLS credentials provided by the server.
