---
title: errorDomain
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/netservice/errordomain
source_url: 'https://developer.apple.com/documentation/foundation/netservice/errordomain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservice/errordomain.json'
content_hash: 'sha256:dc21a7d7984302e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetService](../netservice.md)

# errorDomain

<sub>Type Property</sub>

This key identifies the originator of the error, which is either the `NSNetService` object or the mach network layer. For most errors, you should not need the value provided by this key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class let errorDomain: String
```

## See Also

### Constants

- [NSNetServicesErrorCode](errorcode-swift.type.property.md) — This key identifies the error that occurred during the most recent operation.
