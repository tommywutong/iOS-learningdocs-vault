---
title: attemptStartedAfterInterval
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/establishmentreport/attemptstartedafterinterval
source_url: 'https://developer.apple.com/documentation/network/nwconnection/establishmentreport/attemptstartedafterinterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/establishmentreport/attemptstartedafterinterval.json'
content_hash: 'sha256:8c562092761608e8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWConnection](../../nwconnection.md) · [EstablishmentReport](../establishmentreport.md)

# attemptStartedAfterInterval

<sub>Instance Property</sub>

The time between the call to start and the beginning of the successful connection attempt.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let attemptStartedAfterInterval: TimeInterval
```

## See Also

### Inspecting Connection Attempts

- [duration](duration.md) — The total duration of the successful connection establishment attempt, from the preparing state to the ready state.
- [previousAttemptCount](previousattemptcount.md) — The number of attempts made before the successful attempt, when the connection moved from the preparing state back to the waiting state.
