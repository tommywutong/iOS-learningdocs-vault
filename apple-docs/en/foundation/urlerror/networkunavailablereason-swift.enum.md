---
title: URLError.NetworkUnavailableReason
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlerror/networkunavailablereason-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/urlerror/networkunavailablereason-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlerror/networkunavailablereason-swift.enum.json'
content_hash: 'sha256:58f609ae058f353a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLError](../urlerror.md)

# URLError.NetworkUnavailableReason

<sub>Enumeration</sub>

An enumeration of reasons explaining why a task couldn’t satisfy networking constraints.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NetworkUnavailableReason
```

## Overview

The network may be unavailable due to restrictions placed on the [URLSessionConfiguration](../urlsessionconfiguration.md), such as [allowsConstrainedNetworkAccess](../urlsessionconfiguration/allowsconstrainednetworkaccess.md), [allowsExpensiveNetworkAccess](../urlsessionconfiguration/allowsexpensivenetworkaccess.md) and [allowsCellularAccess](../urlsessionconfiguration/allowscellularaccess.md).

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Unavailability reasons

- [URLError.NetworkUnavailableReason.cellular](networkunavailablereason-swift.enum/cellular.md) — A reason that indicates network is unavailable because the interface is cellular and cellular network is disabled.
- [URLError.NetworkUnavailableReason.constrained](networkunavailablereason-swift.enum/constrained.md) — A reason that indicates network is unavailable because the user enabled “Low Data Mode” in the Settings app.
- [URLError.NetworkUnavailableReason.expensive](networkunavailablereason-swift.enum/expensive.md) — A reason that indicates network is unavailable because the system marked the interface as expensive.

### Enumeration Cases

- [URLError.NetworkUnavailableReason.ultraConstrained](networkunavailablereason-swift.enum/ultraconstrained.md)

## See Also

### Error details

- [failingURL](failingurl.md) — The URL which caused a load to fail.
- [failureURLPeerTrust](failureurlpeertrust.md) — The state of a failed SSL handshake.
- [failureURLString](failureurlstring.md) — The string for the URL which caused a load to fail. _(deprecated)_
- [downloadTaskResumeData](downloadtaskresumedata.md) — An opaque data object used to resume a failed download task.
- [backgroundTaskCancelledReason](backgroundtaskcancelledreason-swift.property.md) — The reason for canceling a background task.
- [BackgroundTaskCancelledReason](backgroundtaskcancelledreason-swift.enum.md) — An enumeration of reasons used to explain the cancellation of a background task.
- [networkUnavailableReason](networkunavailablereason-swift.property.md) — The reason the network was unavailable for a task.
