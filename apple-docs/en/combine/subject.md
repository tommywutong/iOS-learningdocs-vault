---
title: Subject
framework: Combine
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/subject
source_url: 'https://developer.apple.com/documentation/combine/subject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subject.json'
content_hash: 'sha256:bef7ddeda086091d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# Subject

<sub>Protocol</sub>

A publisher that exposes a method for outside callers to publish elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol Subject<Output, Failure> : AnyObject, Publisher
```

## Overview

A subject is a publisher that you can use to ”inject” values into a stream, by calling its [send(_:)](<subject/send(__).md>) method. This can be useful for adapting existing imperative code to the Combine model.

## Relationships

- **Inherits From**: [Publisher](publisher.md)

- **Conforming Types**: [CurrentValueSubject](currentvaluesubject.md), [PassthroughSubject](passthroughsubject.md)

## Topics

### Delivering elements to subscribers

- [send(_:)](<subject/send(__).md>) — Sends a value to the subscriber.
- [send()](<subject/send().md>) — Sends a void value to the subscriber.

### Delivering life cycle events to subscribers

- [send(subscription:)](<subject/send(subscription_).md>) — Sends a subscription to the subscriber.
- [send(completion:)](<subject/send(completion_).md>) — Sends a completion signal to the subscriber.

## See Also

### Subjects

- [CurrentValueSubject](currentvaluesubject.md) — A subject that wraps a single value and publishes a new element whenever the value changes.
- [PassthroughSubject](passthroughsubject.md) — A subject that broadcasts elements to downstream subscribers.
