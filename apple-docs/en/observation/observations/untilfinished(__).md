---
title: 'untilFinished(_:)'
framework: Observation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/observation/observations/untilfinished(_:)'
source_url: 'https://developer.apple.com/documentation/observation/observations/untilfinished(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/observation/observations/untilfinished%28_%3A%29.json'
content_hash: 'sha256:aefb2833f5170907'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Observation](../../observation.md) · [Observations](../observations.md)

# untilFinished(_:)

<sub>Type Method</sub>

Constructs an asynchronous sequence for a given closure by tracking changes of `@Observable` types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func untilFinished(_ emit: @escaping @isolated(any) @Sendable () throws(Failure) -> Observations<Element, Failure>.Iteration) -> Observations<Element, Failure>
```

## Parameters

- `emit` — A closure to generate an element for the sequence.

## Discussion

The emit closure is responsible for extracting a value out of a single or many `@Observable` types. This method continues to be invoked until the .finished option is returned or an error is thrown.
