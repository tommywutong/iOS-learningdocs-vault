---
title: Bundle.DidLoadMessage
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/bundle/didloadmessage
source_url: 'https://developer.apple.com/documentation/foundation/bundle/didloadmessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/didloadmessage.json'
content_hash: 'sha256:f7ab1d801d90de50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# Bundle.DidLoadMessage

<sub>Structure</sub>

A message a bundle sends when it dynamically loads a class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DidLoadMessage
```

## Overview

When a bundle handles a request to load a class with [- classNamed:](<classnamed(__).md>) or  [principalClass](principalclass.md), the bundle dynamically loads the executable code file that contains the class implementation and all other class definitions contained in the file. After module loading completes, the bundle posts this message.

Observe this message with the identifier [didLoad](../notificationcenter/messageidentifier/didload.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [Subject](../notificationcenter/mainactormessage/subject.md) of this message type is [Bundle](../bundle.md).

This message interoperates with the notification [NSBundleDidLoadNotification](didloadnotification.md). The system notifies observers of the message when the [NotificationCenter](../notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Relationships

- **Conforms To**: [AsyncMessage](../notificationcenter/asyncmessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a message

- [init()](<didloadmessage/init().md>) — Creates a message that indicates a bundle dynamically loaded a class.

## See Also

### Getting classes from a bundle

- [- classNamed:](<classnamed(__).md>) — Returns the `Class` object for the specified name.
- [principalClass](principalclass.md) — The bundle’s principal class.
- [NSBundleDidLoadNotification](didloadnotification.md) — A notification that lets observers know when classes are dynamically loaded.
- [NSLoadedClasses](../nsloadedclasses.md) — A constant used as a key for the `userInfo` dictionary of a [NSBundleDidLoadNotification](didloadnotification.md) notification that corresponds to an array of names of each class that was loaded.
