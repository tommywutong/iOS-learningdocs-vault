---
title: address
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfsocketsignature/address
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketsignature/address'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketsignature/address.json'
content_hash: 'sha256:3ea70752ecbfb5c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFSocketSignature](../cfsocketsignature.md)

# address

<sub>Instance Property</sub>

A CFData object holding the contents of a `struct sockaddr` appropriate for the given protocol family (`struct sockaddr_in` or `struct sockaddr_in6`, for example), identifying the address of the socket.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var address: Unmanaged<CFData>!
```
