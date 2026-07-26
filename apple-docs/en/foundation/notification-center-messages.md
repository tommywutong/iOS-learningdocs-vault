---
title: Notification center messages
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/notification-center-messages
source_url: 'https://developer.apple.com/documentation/foundation/notification-center-messages'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notification-center-messages.json'
content_hash: 'sha256:7122f7dd714cbe81'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Notifications](notifications.md) · [NotificationCenter](notificationcenter.md)

# Notification center messages

<sub>API Collection</sub>

Use Foundation’s notification center with Swift concurrency.

## Overview

In Swift, the [Notification](notification.md) type is `nonisolated`, even in cases where it’s posted on a known isolation. To provide specific isolation information and better support Swift concurrency, `NotificationCenter` defines two message types. A [MainActorMessage](notificationcenter/mainactormessage.md) binds to the main actor, whereas a [AsyncMessage](notificationcenter/asyncmessage.md) uses an arbitrary isolation. Frameworks extend these types to define distinct messages, typically corresponding to an existing [Name](notification/name-swift.typealias.md), that declare instance properties for their values instead of using a `userInfo` dictionary. As a result, messages can conform to [Sendable](../swift/sendable.md) when they either don’t use properties or contain only sendable properties.

If your project only needs to support Swift, you can just use the `Message` types. For projects with both Objective-C and Swift code, define a [Notification](notification.md) as well as a corresponding `Message` type.

### Posting and observing messages

You can post a message with the `post(_:subject:)` method, passing a message instance and optionally providing a subject. To receive messages, add an observer with the `addObserver(of:for:using:)` method. The overloads of this method allow you to observe either messages from a single object or from any object of a given type. Observation ends when you discard the token returned from `addObserver(of:for:using:)` or after an explicit call to [removeObserver(_:)](<notificationcenter/removeobserver(__)-2gmm0.md>).

You can also receive messages as an [AsyncSequence](../swift/asyncsequence.md) with the `messages(of:for:bufferSize:)` methods.

Several flavors of `addObserver(of:for:using:)` and `messages(of:for:bufferSize:)` take a [MessageIdentifier](notificationcenter/messageidentifier.md), which frameworks may implement to provide a typed, ergonomic experience at the call point for convenience, as described in [SE-0299](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0299-extend-generic-static-member-lookup.md).

### Using messages with the SDK

Many system frameworks — including Foundation, UIKit, and AppKit — adopt the [MainActorMessage](notificationcenter/mainactormessage.md) and [AsyncMessage](notificationcenter/asyncmessage.md) types to facilitate using their notifications in concurrency-safe Swift code. The following example shows how to observe Foundation’s [TimeZone](timezone.md) type for the [systemTimeZoneDidChange](notificationcenter/messageidentifier/systemtimezonedidchange.md) message, which contains the property [previousTimeZone](timezone/systemtimezonedidchangemessage/previoustimezone.md).

```
/// Note: Store `token` in a property for as long as you intend to observe.
token = NotificationCenter.default.addObserver(of: TimeZone.self,
                                               for: .systemTimeZoneDidChange)
{ message in
    let identifier = message.previousTimeZone?.identifier ?? "(unknown)"
    print("Time zone changed from \(identifier).")
}
```

For use with existing notification code, [MainActorMessage](notificationcenter/mainactormessage.md) and [AsyncMessage](notificationcenter/asyncmessage.md) define helper methods that conforming types implement to convert a message to a corresponding notification and vice versa.

## Topics

### Declaring a message

- [MainActorMessage](notificationcenter/mainactormessage.md) — A protocol for creating types that you can post to a notification center and bind to the main actor.
- [AsyncMessage](notificationcenter/asyncmessage.md) — A protocol for creating types that you can post to a notification center, which posts them to an arbitrary isolation.

### Using message identifiers

- [MessageIdentifier](notificationcenter/messageidentifier.md) — An optional identifier to associate a given message with a given type.
- [BaseMessageIdentifier](notificationcenter/basemessageidentifier.md) — A type for use when defining optional Message identifiers.

### Observing concurrency-safe notifications

- [addObserver(of:for:using:)](<notificationcenter/addobserver(of_for_using_)-4d19x.md>) — Adds an observer to a center for messages delivered on the main actor with a given subject and identifier.
- [addObserver(of:for:using:)](<notificationcenter/addobserver(of_for_using_)-90os.md>) — Adds an observer to a center for messages delivered on the main actor with a given subject and identifier.
- [addObserver(of:for:using:)](<notificationcenter/addobserver(of_for_using_)-56bn4.md>) — Adds an observer to a center for messages delivered on the main actor with a given subject and message type.
- [addObserver(of:for:using:)](<notificationcenter/addobserver(of_for_using_)-twm3.md>) — Adds an observer to a center for messages delivered asynchronously with a given subject and identifier.
- [addObserver(of:for:using:)](<notificationcenter/addobserver(of_for_using_)-t1wr.md>) — Adds an observer to a center for messages delivered asynchronously with a given subject and message type.
- [addObserver(of:for:using:)](<notificationcenter/addobserver(of_for_using_)-64uw3.md>) — Adds an observer to a center for messages delivered asynchronously with a given subject and message type.
- [removeObserver(_:)](<notificationcenter/removeobserver(__)-2gmm0.md>) — Stops the observation represented by the given observation token.
- [ObservationToken](notificationcenter/observationtoken.md) — A unique token representing a single observer registration in a notification center.

### Receiving notifications as asynchronous sequences

- [messages(of:for:bufferSize:)](<notificationcenter/messages(of_for_buffersize_)-4tof0.md>) — Returns an asynchronous sequence of messages produced by this center for a given subject and identifier.
- [messages(of:for:bufferSize:)](<notificationcenter/messages(of_for_buffersize_)-1ub69.md>) — Returns an asynchronous sequence of messages produced by this center for a given subject type and identifier.
- [messages(of:for:bufferSize:)](<notificationcenter/messages(of_for_buffersize_)-623kg.md>) — Returns an asynchronous sequence of messages produced by this center for a given subject and message type.

### Posting notification messages

- [post(_:subject:)](<notificationcenter/post(__subject_)-87dbk.md>) — Posts a given main actor message to the notification center.
- [post(_:)](<notificationcenter/post(__)-19s7b.md>) — Posts a given main actor message to the notification center.
- [post(_:subject:)](<notificationcenter/post(__subject_)-5271w.md>) — Posts a given asynchronous message to the notification center.
- [post(_:)](<notificationcenter/post(__)-7ia4j.md>) — Posts a given asynchronous message to the notification center.
