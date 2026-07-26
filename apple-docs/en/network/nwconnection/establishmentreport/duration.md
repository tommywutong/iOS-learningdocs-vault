---
title: duration
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/establishmentreport/duration
source_url: 'https://developer.apple.com/documentation/network/nwconnection/establishmentreport/duration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/establishmentreport/duration.json'
content_hash: 'sha256:591109ddb113a832'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWConnection](../../nwconnection.md) · [EstablishmentReport](../establishmentreport.md)

# duration

<sub>Instance Property</sub>

The total duration of the successful connection establishment attempt, from the preparing state to the ready state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let duration: TimeInterval
```

## See Also

### Inspecting Connection Attempts

- [previousAttemptCount](previousattemptcount.md) — The number of attempts made before the successful attempt, when the connection moved from the preparing state back to the waiting state.
- [attemptStartedAfterInterval](attemptstartedafterinterval.md) — The time between the call to start and the beginning of the successful connection attempt.
