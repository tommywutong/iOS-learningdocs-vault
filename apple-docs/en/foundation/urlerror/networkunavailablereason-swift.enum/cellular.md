---
title: URLError.NetworkUnavailableReason.cellular
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlerror/networkunavailablereason-swift.enum/cellular
source_url: 'https://developer.apple.com/documentation/foundation/urlerror/networkunavailablereason-swift.enum/cellular'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlerror/networkunavailablereason-swift.enum/cellular.json'
content_hash: 'sha256:27900ca0c80cdf9f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URLError](../../urlerror.md) · [NetworkUnavailableReason](../networkunavailablereason-swift.enum.md)

# URLError.NetworkUnavailableReason.cellular

<sub>Case</sub>

A reason that indicates network is unavailable because the interface is cellular and cellular network is disabled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case cellular
```

## Discussion

This reason occurs when cellular is the only available network interface, but the [URLSessionConfiguration](../../urlsessionconfiguration.md) property [allowsCellularAccess](../../urlsessionconfiguration/allowscellularaccess.md) is [false](../../../swift/false.md).

## See Also

### Unavailability reasons

- [URLError.NetworkUnavailableReason.constrained](constrained.md) — A reason that indicates network is unavailable because the user enabled “Low Data Mode” in the Settings app.
- [URLError.NetworkUnavailableReason.expensive](expensive.md) — A reason that indicates network is unavailable because the system marked the interface as expensive.
