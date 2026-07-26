---
title: Publishers.Merge4
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/merge4
source_url: 'https://developer.apple.com/documentation/combine/publishers/merge4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/merge4.json'
content_hash: 'sha256:154e7a58c57812f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Merge4

<sub>Structure</sub>

A publisher created by applying the merge function to four upstream publishers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Merge4<A, B, C, D> where A : Publisher, B : Publisher, C : Publisher, D : Publisher, A.Failure == B.Failure, A.Output == B.Output, B.Failure == C.Failure, B.Output == C.Output, C.Failure == D.Failure, C.Output == D.Output
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Publisher](../publisher.md)

## Topics

### Creating a merge-four publisher

- [init(_:_:_:_:)](<merge4/init(________).md>) — Creates a publisher created by applying the merge function to four upstream publishers.

### Merging elements

- [merge(with:)](<merge4/merge(with_).md>)
- [merge(with:_:)](<merge4/merge(with___).md>)
- [merge(with:_:_:)](<merge4/merge(with_____).md>)
- [merge(with:_:_:_:)](<merge4/merge(with_______).md>)

### Declaring supporting types

- [Output](merge4/output.md) — The kind of values published by this publisher.
- [Failure](merge4/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [a](merge4/a.md) — A publisher to merge.
- [b](merge4/b.md) — A second publisher to merge.
- [c](merge4/c.md) — A third publisher to merge.
- [d](merge4/d.md) — A fourth publisher to merge.

### Comparing publishers

- [==(_:_:)](<merge4/==(____).md>) — Returns a Boolean value that indicates whether two publishers are equivalent.

### Default Implementations

- [Equatable Implementations](merge4/equatable-implementations.md)

## See Also

### Combining elements from multiple publishers

- [CombineLatest](combinelatest.md) — A publisher that receives and combines the latest elements from two publishers.
- [CombineLatest3](combinelatest3.md) — A publisher that receives and combines the latest elements from three publishers.
- [CombineLatest4](combinelatest4.md) — A publisher that receives and combines the latest elements from four publishers.
- [Merge](merge.md) — A publisher created by applying the merge function to two upstream publishers.
- [Merge3](merge3.md) — A publisher created by applying the merge function to three upstream publishers.
- [Merge5](merge5.md) — A publisher created by applying the merge function to five upstream publishers.
- [Merge6](merge6.md) — A publisher created by applying the merge function to six upstream publishers.
- [Merge7](merge7.md) — A publisher created by applying the merge function to seven upstream publishers.
- [Merge8](merge8.md) — A publisher created by applying the merge function to eight upstream publishers.
- [MergeMany](mergemany.md) — A publisher created by applying the merge function to an arbitrary number of upstream publishers.
- [Zip](zip.md) — A publisher created by applying the zip function to two upstream publishers.
- [Zip3](zip3.md) — A publisher created by applying the zip function to three upstream publishers.
- [Zip4](zip4.md) — A publisher created by applying the zip function to four upstream publishers.
