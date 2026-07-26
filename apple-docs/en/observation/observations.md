---
title: Observations
framework: Observation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/observation/observations
source_url: 'https://developer.apple.com/documentation/observation/observations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/observation/observations.json'
content_hash: 'sha256:da50410f77117741'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Observation](../observation.md)

# Observations

<sub>Structure</sub>

An asynchronous sequence generated from a closure that tracks the transactional changes of `@Observable` types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Observations<Element, Failure> where Element : Sendable, Failure : Error
```

## Overview

`Observations` conforms to `AsyncSequence`, providing an intuitive and safe mechanism to track changes to types that are marked as `@Observable` by using Swift Concurrency to indicate transactional boundaries starting from the willSet of the first mutation to the next suspension point of the safe access.

## Relationships

- **Conforms To**: [AsyncSequence](../swift/asyncsequence.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Structures

- [Iterator](observations/iterator.md)

### Initializers

- [init(_:)](<observations/init(__).md>) — Constructs an asynchronous sequence for a given closure by tracking changes of `@Observable` types.

### Type Methods

- [untilFinished(_:)](<observations/untilfinished(__).md>) — Constructs an asynchronous sequence for a given closure by tracking changes of `@Observable` types.

### Enumerations

- [Iteration](observations/iteration.md)
