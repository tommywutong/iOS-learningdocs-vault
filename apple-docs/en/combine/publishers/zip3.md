---
title: Publishers.Zip3
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/zip3
source_url: 'https://developer.apple.com/documentation/combine/publishers/zip3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/zip3.json'
content_hash: 'sha256:95042ce590a4ab80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Zip3

<sub>Structure</sub>

A publisher created by applying the zip function to three upstream publishers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Zip3<A, B, C> where A : Publisher, B : Publisher, C : Publisher, A.Failure == B.Failure, B.Failure == C.Failure
```

## Overview

Use a `Publishers.Zip3` to combine the latest elements from three publishers and emit a tuple to the downstream. The returned publisher waits until all three publishers have emitted an event, then delivers the oldest unconsumed event from each publisher as a tuple to the subscriber.

If any upstream publisher finishes successfully or fails with an error, so too does the zipped publisher.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Publisher](../publisher.md)

## Topics

### Creating a zip-three Publisher

- [init(_:_:_:)](<zip3/init(______).md>) — Creates a publisher that applies the zip function to three upstream publishers.

### Declaring supporting types

- [Output](zip3/output.md) — The kind of values published by this publisher.
- [Failure](zip3/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [a](zip3/a.md) — A publisher to zip.
- [b](zip3/b.md) — A second publisher to zip.
- [c](zip3/c.md) — A third publisher to zip.

### Comparing publishers

- [==(_:_:)](<zip3/==(____).md>) — Returns a Boolean value that indicates whether two publishers are equivalent.

### Default Implementations

- [Equatable Implementations](zip3/equatable-implementations.md)

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
- [Zip4](zip4.md) — A publisher created by applying the zip function to four upstream publishers.
