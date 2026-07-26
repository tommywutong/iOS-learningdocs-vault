---
title: URLError.NetworkUnavailableReason.constrained
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlerror/networkunavailablereason-swift.enum/constrained
source_url: 'https://developer.apple.com/documentation/foundation/urlerror/networkunavailablereason-swift.enum/constrained'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlerror/networkunavailablereason-swift.enum/constrained.json'
content_hash: 'sha256:ede41be9c6a8621e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URLError](../../urlerror.md) · [NetworkUnavailableReason](../networkunavailablereason-swift.enum.md)

# URLError.NetworkUnavailableReason.constrained

<sub>Case</sub>

A reason that indicates network is unavailable because the user enabled “Low Data Mode” in the Settings app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case constrained
```

## Discussion

This reason occurs when the following conditions are true:

- The only available network is cellular.
- The user has enabled “Low Data Mode” option in the Cellular Data Options section of the Settings app.
- The [URLSessionConfiguration](../../urlsessionconfiguration.md) property [allowsConstrainedNetworkAccess](../../urlsessionconfiguration/allowsconstrainednetworkaccess.md) is [false](../../../swift/false.md).

## See Also

### Unavailability reasons

- [URLError.NetworkUnavailableReason.cellular](cellular.md) — A reason that indicates network is unavailable because the interface is cellular and cellular network is disabled.
- [URLError.NetworkUnavailableReason.expensive](expensive.md) — A reason that indicates network is unavailable because the system marked the interface as expensive.
