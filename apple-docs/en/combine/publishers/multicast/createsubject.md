---
title: createSubject
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/multicast/createsubject
source_url: 'https://developer.apple.com/documentation/combine/publishers/multicast/createsubject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/multicast/createsubject.json'
content_hash: 'sha256:9792e0d8a48e97c6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Multicast](../multicast.md)

# createSubject

<sub>Instance Property</sub>

A closure that returns a subject each time a subscriber attaches to the multicast publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final let createSubject: () -> SubjectType
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives its elements.
