---
title: ObjectWillChangePublisher
framework: Combine
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/observableobject/objectwillchangepublisher
source_url: 'https://developer.apple.com/documentation/combine/observableobject/objectwillchangepublisher'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/observableobject/objectwillchangepublisher.json'
content_hash: 'sha256:3e43fcac62b95bb7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [ObservableObject](../observableobject.md)

# ObjectWillChangePublisher

<sub>Associated Type</sub>

The type of publisher that emits before the object has changed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype ObjectWillChangePublisher : Publisher = ObservableObjectPublisher where Self.ObjectWillChangePublisher.Failure == Never
```

## See Also

### Publishing changes

- [objectWillChange](objectwillchange.md) — A publisher that emits before the object has changed.
