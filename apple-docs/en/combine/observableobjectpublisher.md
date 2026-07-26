---
title: ObservableObjectPublisher
framework: Combine
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/observableobjectpublisher
source_url: 'https://developer.apple.com/documentation/combine/observableobjectpublisher'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/observableobjectpublisher.json'
content_hash: 'sha256:f01941a00dfc948d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# ObservableObjectPublisher

<sub>Class</sub>

A publisher that publishes changes from observable objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class ObservableObjectPublisher
```

## Relationships

- **Conforms To**: [Publisher](publisher.md)

## Topics

### Creating an observable object publisher

- [init()](<observableobjectpublisher/init().md>) — Creates an observable object publisher instance.

### Delivering elements to subscribers

- [send()](<observableobjectpublisher/send().md>) — Sends the changed value to the downstream subscriber.

## See Also

### Observable Objects

- [ObservableObject](observableobject.md) — A type of object with a publisher that emits before the object has changed.
