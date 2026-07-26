---
title: URLError.NetworkUnavailableReason.expensive
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlerror/networkunavailablereason-swift.enum/expensive
source_url: 'https://developer.apple.com/documentation/foundation/urlerror/networkunavailablereason-swift.enum/expensive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlerror/networkunavailablereason-swift.enum/expensive.json'
content_hash: 'sha256:a0b6d4777d3f3851'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URLError](../../urlerror.md) · [NetworkUnavailableReason](../networkunavailablereason-swift.enum.md)

# URLError.NetworkUnavailableReason.expensive

<sub>Case</sub>

A reason that indicates network is unavailable because the system marked the interface as expensive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case expensive
```

## Discussion

The system determines what constitutes “expensive” based on the nature of the network interface and other factors. iOS 13 considers most cellular networks and personal hotspots expensive.

This reason occurs when the following conditions are true:

- The only available network interfaces are expensive.
- The [URLSessionConfiguration](../../urlsessionconfiguration.md) property [allowsExpensiveNetworkAccess](../../urlsessionconfiguration/allowsexpensivenetworkaccess.md) is [false](../../../swift/false.md).

## See Also

### Unavailability reasons

- [URLError.NetworkUnavailableReason.cellular](cellular.md) — A reason that indicates network is unavailable because the interface is cellular and cellular network is disabled.
- [URLError.NetworkUnavailableReason.constrained](constrained.md) — A reason that indicates network is unavailable because the user enabled “Low Data Mode” in the Settings app.
