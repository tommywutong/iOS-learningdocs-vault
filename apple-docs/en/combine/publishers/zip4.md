---
title: Publishers.Zip4
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/zip4
source_url: 'https://developer.apple.com/documentation/combine/publishers/zip4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/zip4.json'
content_hash: 'sha256:a7b764a1ebab0e8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Zip4

<sub>Structure</sub>

A publisher created by applying the zip function to four upstream publishers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Zip4<A, B, C, D> where A : Publisher, B : Publisher, C : Publisher, D : Publisher, A.Failure == B.Failure, B.Failure == C.Failure, C.Failure == D.Failure
```

## Overview

Use a `Publishers.Zip4` to combine the latest elements from four publishers and emit a tuple to the downstream. The returned publisher waits until all four publishers have emitted an event, then delivers the oldest unconsumed event from each publisher as a tuple to the subscriber.

If any upstream publisher finishes successfully or fails with an error, so too does the zipped publisher.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Publisher](../publisher.md)

## Topics

### Creating a zip-four Publisher

- [init(_:_:_:_:)](<zip4/init(________).md>) — Creates a publisher created by applying the zip function to four upstream publishers.

### Declaring supporting types

- [Output](zip4/output.md) — The kind of values published by this publisher.
- [Failure](zip4/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [a](zip4/a.md) — A publisher to zip.
- [b](zip4/b.md) — A second publisher to zip.
- [c](zip4/c.md) — A third publisher to zip.
- [d](zip4/d.md) — A fourth publisher to zip.

### Comparing publishers

- [==(_:_:)](<zip4/==(____).md>) — Returns a Boolean value that indicates whether two publishers are equivalent.

### Default Implementations

- [Equatable Implementations](zip4/equatable-implementations.md)

## See Also

### Combining elements from multiple publishers

- [CombineLatest](combinelatest.md) — A publisher that receives and combines the latest elements from two publishers.
- [CombineLatest3](combinelatest3.md) — A publisher that receives and combines the latest elements from three publishers.
- [CombineLatest4](combinelatest4.md) — A publisher that receives and combines the latest elements from four publishers.
- [Merge](merge.md) — A publisher created by applying the merge function to two upstream publishers.
- [Merge3](merge3.md) — A publisher created by applying the merge function to three upstream publishers.
- [Merge4](merge4.md) — A publisher created by applying the merge function to four upstream publishers.
- [Merge5](merge5.md) — A publisher created by applying the merge function to five upstream publishers.
- [Merge6](merge6.md) — A publisher created by applying the merge function to six upstream publishers.
- [Merge7](merge7.md) — A publisher created by applying the merge function to seven upstream publishers.
- [Merge8](merge8.md) — A publisher created by applying the merge function to eight upstream publishers.
- [MergeMany](mergemany.md) — A publisher created by applying the merge function to an arbitrary number of upstream publishers.
- [Zip](zip.md) — A publisher created by applying the zip function to two upstream publishers.
- [Zip3](zip3.md) — A publisher created by applying the zip function to three upstream publishers.
