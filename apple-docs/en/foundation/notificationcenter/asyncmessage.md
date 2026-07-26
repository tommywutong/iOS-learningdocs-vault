---
title: NotificationCenter.AsyncMessage
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationcenter/asyncmessage
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/asyncmessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/asyncmessage.json'
content_hash: 'sha256:e001145544e9b363'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NotificationCenter](../notificationcenter.md)

# NotificationCenter.AsyncMessage

<sub>Protocol</sub>

A protocol for creating types that you can post to a notification center, which posts them to an arbitrary isolation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol AsyncMessage : Sendable
```

## Overview

You post types conforming to `AsyncMessage` to a notification center using `post(_:subject:)` and observe them with `addObserver(of:for:using:)`.

The notification center delivers `AsyncMessage` types asynchronously when posted. Asynchronous delivery isn’t suitable for messages with time-critical deliveries, such as a message that must have its observers called before a certain action takes place.

For types that post on the main actor, use [MainActorMessage](mainactormessage.md).

Each `AsyncMessage` is associated with a specific `Subject` type.

For example, an `AsyncMessage` associated with the type `Event` could use the following declaration:

```swift
struct EventDidStart: NotificationCenter.AsyncMessage {
    typealias Subject = Event
}
```

`AsyncMessage` can use an optional [MessageIdentifier](messageidentifier.md) type for context-aware observer registration:

```swift
extension NotificationCenter.MessageIdentifier where Self == NotificationCenter.BaseMessageIdentifier<EventDidStart> {
    static var didStart: Self { .init() }
}
```

With this identifier, observers can receive information about a specific instance by registering for this message with a [NotificationCenter](../notificationcenter.md):

```swift
let observerToken = NotificationCenter.default.addObserver(of: importantEvent, for: .didStart)
```

Or an observer can receive information about any instance with:

```swift
let observerToken = NotificationCenter.default.addObserver(of: Event.self, for: .didStart)
```

The notification center ties observation the lifetime of the returned [ObservationToken](observationtoken.md) and automatically de-registers the observer if the token goes out of scope. You can also remove observation explicitly:

```swift
NotificationCenter.default.removeObserver(observerToken)
```

### Notification Interoperability

`AsyncMessage` includes optional interoperability with [Notification](../notification.md), enabling posters and observers of both types to pass information.

It does this by offering a [makeMessage(_:)](<asyncmessage/makemessage(__).md>) method that collects values from a [Notification](../notification.md)‘s [userInfo](../notification/userinfo.md) and populates properties on a new message. In the other direction, a [makeNotification(_:)](<asyncmessage/makenotification(__).md>) method collects the message’s defined properties and loads them into a new notification’s [userInfo](../notification/userinfo.md) dictionary.

For example, if there exists a [Notification](../notification.md) posted on an arbitrary isolation identified by the [Name](../notification/name-swift.typealias.md) `"eventDidFinish"` with a [userInfo](../notification/userinfo.md) dictionary containing the key `"duration"` as an [NSNumber](../nsnumber.md), an app could post and observe the notification with the following [AsyncMessage](asyncmessage.md):

```swift
struct EventDidFinish: NotificationCenter.AsyncMessage {
    typealias Subject = Event
    static var name: Notification.Name { Notification.Name("eventDidFinish") }

    var duration: Int

    static func makeNotification(_ message: Self) -> Notification {
        return Notification(name: Self.name, userInfo: ["duration": NSNumber(message.duration)])
    }

    static func makeMessage(_ notification: Notification) -> Self? {
        guard let userInfo = notification.userInfo,
              let duration = userInfo["duration"] as? Int
        else {
            return nil
        }

        return Self(duration: duration)
    }
}
```

With this definition, an observer for this `AsyncMessage` type receives information even if the poster used the [Notification](../notification.md) equivalent, and vice versa.

## Relationships

- **Inherits From**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

- **Conforming Types**: [DidLoadMessage](../bundle/didloadmessage.md), [CalendarDayChangedMessage](../calendar/calendardaychangedmessage.md), [ConnectionAcceptedMessage](../filehandle/connectionacceptedmessage.md), [DataAvailableMessage](../filehandle/dataavailablemessage.md), [ReadCompletionMessage](../filehandle/readcompletionmessage.md), [ReadToEndOfFileCompletionMessage](../filehandle/readtoendoffilecompletionmessage.md), [CookiesChangedMessage](../httpcookiestorage/cookieschangedmessage.md), [LowDiskSpaceMessage](../nsbundleresourcerequest/lowdiskspacemessage.md), [DidFinishGatheringMessage](../nsmetadataquery/didfinishgatheringmessage.md), [DidStartGatheringMessage](../nsmetadataquery/didstartgatheringmessage.md), [DidBecomeInvalidMessage](../port/didbecomeinvalidmessage.md), [DidTerminateMessage](../process/didterminatemessage.md), [PowerStateDidChangeMessage](../processinfo/powerstatedidchangemessage.md), [ThermalStateDidChangeMessage](../processinfo/thermalstatedidchangemessage.md), [DidChangeMessage](../userdefaults/didchangemessage.md)

## Topics

### Declaring the message name and subject

- [name](asyncmessage/name.md) — A optional name corresponding to this type, used to interoperate with notification posters and observers.
- [Subject](asyncmessage/subject.md) — A type which you can optionally post and observe along with this `AsyncMessage`.

### Converting between messages and notifications

- [makeMessage(_:)](<asyncmessage/makemessage(__).md>) — Converts a posted notification into this asynchronous message type for any observers.
- [makeNotification(_:)](<asyncmessage/makenotification(__).md>) — Converts a posted asynchronous message into a notification for any observers.

## See Also

### Declaring a message

- [MainActorMessage](mainactormessage.md) — A protocol for creating types that you can post to a notification center and bind to the main actor.
