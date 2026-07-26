---
title: PassthroughSubject
framework: Combine
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/passthroughsubject
source_url: 'https://developer.apple.com/documentation/combine/passthroughsubject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/passthroughsubject.json'
content_hash: 'sha256:09eb30899e91b4d5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# PassthroughSubject

<sub>Class</sub>

A subject that broadcasts elements to downstream subscribers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class PassthroughSubject<Output, Failure> where Failure : Error
```

## Overview

As a concrete implementation of [Subject](subject.md), the [PassthroughSubject](passthroughsubject.md) provides a convenient way to adapt existing imperative code to the Combine model.

Unlike [CurrentValueSubject](currentvaluesubject.md), a [PassthroughSubject](passthroughsubject.md) doesn’t have an initial value or a buffer of the most recently-published element. A [PassthroughSubject](passthroughsubject.md) drops values if there are no subscribers, or its current demand is zero.

## Relationships

- **Conforms To**: [Publisher](publisher.md), [Subject](subject.md)

## Topics

### Creating a passthrough subject

- [init()](<passthroughsubject/init().md>)

## See Also

### Subjects

- [Subject](subject.md) — A publisher that exposes a method for outside callers to publish elements.
- [CurrentValueSubject](currentvaluesubject.md) — A subject that wraps a single value and publishes a new element whenever the value changes.
