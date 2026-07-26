---
title: 'init(upstream:createSubject:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/multicast/init(upstream:createsubject:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/multicast/init(upstream:createsubject:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/multicast/init%28upstream%3Acreatesubject%3A%29.json'
content_hash: 'sha256:4dafbf8e53fec0df'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Multicast](../multicast.md)

# init(upstream:createSubject:)

<sub>Initializer</sub>

Creates a multicast publisher that applies a closure to create a subject that delivers elements to subscribers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, createSubject: @escaping () -> SubjectType)
```

## Parameters

- `createSubject` — A closure that returns a [Subject](../../subject.md) each time a subscriber attaches to the multicast publisher.
