---
title: 'init(_:)'
framework: Observation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/observation/observations/init(_:)'
source_url: 'https://developer.apple.com/documentation/observation/observations/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/observation/observations/init%28_%3A%29.json'
content_hash: 'sha256:67f20c0e858cf7fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Observation](../../observation.md) · [Observations](../observations.md)

# init(_:)

<sub>Initializer</sub>

Constructs an asynchronous sequence for a given closure by tracking changes of `@Observable` types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ emit: @escaping @isolated(any) @Sendable () throws(Failure) -> Element)
```

## Parameters

- `emit` — A closure to generate an element for the sequence.

## Discussion

The emit closure is responsible for extracting a value out of a single or many `@Observable` types.
