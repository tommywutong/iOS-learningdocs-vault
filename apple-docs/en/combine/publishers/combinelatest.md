---
title: Publishers.CombineLatest
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/combinelatest
source_url: 'https://developer.apple.com/documentation/combine/publishers/combinelatest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/combinelatest.json'
content_hash: 'sha256:343c49acd74eb578'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.CombineLatest

<sub>Structure</sub>

A publisher that receives and combines the latest elements from two publishers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CombineLatest<A, B> where A : Publisher, B : Publisher, A.Failure == B.Failure
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Publisher](../publisher.md)

## Topics

### Creating a combine latest publisher

- [init(_:_:)](<combinelatest/init(____).md>) — Creates a publisher that receives and combines the latest elements from two publishers.

### Declaring supporting types

- [Output](combinelatest/output.md) — The kind of values published by this publisher.
- [Failure](combinelatest/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [a](combinelatest/a.md)
- [b](combinelatest/b.md)

### Comparing publishers

- [==(_:_:)](<combinelatest/==(____).md>) — Returns a Boolean value that indicates whether two publishers are equivalent.

### Default Implementations

- [Equatable Implementations](combinelatest/equatable-implementations.md)

## See Also

### Combining elements from multiple publishers

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
- [Zip4](zip4.md) — A publisher created by applying the zip function to four upstream publishers.
