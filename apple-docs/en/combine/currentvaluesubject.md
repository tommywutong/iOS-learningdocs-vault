---
title: CurrentValueSubject
framework: Combine
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/currentvaluesubject
source_url: 'https://developer.apple.com/documentation/combine/currentvaluesubject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/currentvaluesubject.json'
content_hash: 'sha256:e5e2c7558c7ae257'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# CurrentValueSubject

<sub>Class</sub>

A subject that wraps a single value and publishes a new element whenever the value changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class CurrentValueSubject<Output, Failure> where Failure : Error
```

## Overview

Unlike [PassthroughSubject](passthroughsubject.md), [CurrentValueSubject](currentvaluesubject.md) maintains a buffer of the most recently published element.

Calling [send(_:)](<subject/send(__).md>) on a [CurrentValueSubject](currentvaluesubject.md) also updates the current value, making it equivalent to updating the [value](currentvaluesubject/value.md) directly.

## Relationships

- **Conforms To**: [Publisher](publisher.md), [Subject](subject.md)

## Topics

### Creating a current value subject

- [init(_:)](<currentvaluesubject/init(__).md>) — Creates a current value subject with the given initial value.

### Accessing the current value

- [value](currentvaluesubject/value.md) — The value wrapped by this subject, published as a new element whenever it changes.

## See Also

### Subjects

- [Subject](subject.md) — A publisher that exposes a method for outside callers to publish elements.
- [PassthroughSubject](passthroughsubject.md) — A subject that broadcasts elements to downstream subscribers.
