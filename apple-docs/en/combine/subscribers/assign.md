---
title: Subscribers.Assign
framework: Combine
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/subscribers/assign
source_url: 'https://developer.apple.com/documentation/combine/subscribers/assign'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscribers/assign.json'
content_hash: 'sha256:8fee29f83d47c7a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Subscribers](../subscribers.md)

# Subscribers.Assign

<sub>Class</sub>

A simple subscriber that assigns received elements to a property indicated by a key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class Assign<Root, Input>
```

## Relationships

- **Conforms To**: [Cancellable](../cancellable.md), [CustomCombineIdentifierConvertible](../customcombineidentifierconvertible.md), [CustomPlaygroundDisplayConvertible](../../swift/customplaygrounddisplayconvertible.md), [CustomReflectable](../../swift/customreflectable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Subscriber](../subscriber.md)

## Topics

### Creating an assign subscriber

- [init(object:keyPath:)](<assign/init(object_keypath_).md>) — Creates a subscriber to assign the value of a property indicated by a key path.

### Receiving elements

- [receive(_:)](<assign/receive(__).md>) — Tells the subscriber that the publisher has produced an element.

### Receiving life cycle events

- [receive(subscription:)](<assign/receive(subscription_).md>) — Tells the subscriber that it has successfully subscribed to the publisher and may request items.
- [receive(completion:)](<assign/receive(completion_).md>) — Tells the subscriber that the publisher has completed publishing, either normally or with an error.

### Inspecting the assigned property

- [object](assign/object.md) — The object that contains the property to assign.
- [keyPath](assign/keypath.md) — The key path that indicates the property to assign.

### Supporting Debugging

- [customMirror](assign/custommirror.md) — A mirror that reflects the subscriber.
- [description](assign/description.md) — A textual representation of this subscriber.
- [playgroundDescription](assign/playgrounddescription.md) — A custom playground description for this subscriber.

### Instance Methods

- [cancel()](<assign/cancel().md>) — Cancel the activity.

## See Also

### Using convenience subscribers

- [Sink](sink.md) — A simple subscriber that requests an unlimited number of values upon subscription.
