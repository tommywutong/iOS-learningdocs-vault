---
title: 'addObserver(of:for:using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/notificationcenter/addobserver(of:for:using:)-t1wr'
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/addobserver(of:for:using:)-t1wr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/addobserver%28of%3Afor%3Ausing%3A%29-t1wr.json'
content_hash: 'sha256:bde9649d74e84f91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NotificationCenter](../notificationcenter.md)

# addObserver(of:for:using:)

<sub>Instance Method</sub>

Adds an observer to a center for messages delivered asynchronously with a given subject and message type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addObserver<Identifier, Message>(of subject: Message.Subject.Type, for identifier: Identifier, using observer: @escaping @Sendable (Message) async -> Void) -> NotificationCenter.ObservationToken where Identifier : NotificationCenter.MessageIdentifier, Message : NotificationCenter.AsyncMessage, Message == Identifier.MessageType
```

## Parameters

- `subject` — The metatype to observe all values for a given type.

- `identifier` — An identifier representing a specific message type.

- `observer` — A closure to execute when receving a message.

## Return Value

A token representing the observation registration with the given notification center. Retain this token for as long as you need to receive messages.

## See Also

### Observing concurrency-safe notifications

- [addObserver(of:for:using:)](<addobserver(of_for_using_)-4d19x.md>) — Adds an observer to a center for messages delivered on the main actor with a given subject and identifier.
- [addObserver(of:for:using:)](<addobserver(of_for_using_)-90os.md>) — Adds an observer to a center for messages delivered on the main actor with a given subject and identifier.
- [addObserver(of:for:using:)](<addobserver(of_for_using_)-56bn4.md>) — Adds an observer to a center for messages delivered on the main actor with a given subject and message type.
- [addObserver(of:for:using:)](<addobserver(of_for_using_)-twm3.md>) — Adds an observer to a center for messages delivered asynchronously with a given subject and identifier.
- [addObserver(of:for:using:)](<addobserver(of_for_using_)-64uw3.md>) — Adds an observer to a center for messages delivered asynchronously with a given subject and message type.
- [removeObserver(_:)](<removeobserver(__)-2gmm0.md>) — Stops the observation represented by the given observation token.
- [ObservationToken](observationtoken.md) — A unique token representing a single observer registration in a notification center.
