---
title: NotificationCenter.ObservationToken
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationcenter/observationtoken
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/observationtoken'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/observationtoken.json'
content_hash: 'sha256:5816a150694318cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NotificationCenter](../notificationcenter.md)

# NotificationCenter.ObservationToken

<sub>Structure</sub>

A unique token representing a single observer registration in a notification center.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ObservationToken
```

## Overview

You receive the `ObservationToken` type as a return value from `addObserver(of:for:using:)` and related methods.

Retain the `ObservationToken` for as long as you need to continue observation, since observation ends when the token goes out of scope. You can also explicitly stop observing by passing the token to `removeObserver(_:)-(ObservationToken)`.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## See Also

### Observing concurrency-safe notifications

- [addObserver(of:for:using:)](<addobserver(of_for_using_)-4d19x.md>) — Adds an observer to a center for messages delivered on the main actor with a given subject and identifier.
- [addObserver(of:for:using:)](<addobserver(of_for_using_)-90os.md>) — Adds an observer to a center for messages delivered on the main actor with a given subject and identifier.
- [addObserver(of:for:using:)](<addobserver(of_for_using_)-56bn4.md>) — Adds an observer to a center for messages delivered on the main actor with a given subject and message type.
- [addObserver(of:for:using:)](<addobserver(of_for_using_)-twm3.md>) — Adds an observer to a center for messages delivered asynchronously with a given subject and identifier.
- [addObserver(of:for:using:)](<addobserver(of_for_using_)-t1wr.md>) — Adds an observer to a center for messages delivered asynchronously with a given subject and message type.
- [addObserver(of:for:using:)](<addobserver(of_for_using_)-64uw3.md>) — Adds an observer to a center for messages delivered asynchronously with a given subject and message type.
- [removeObserver(_:)](<removeobserver(__)-2gmm0.md>) — Stops the observation represented by the given observation token.
