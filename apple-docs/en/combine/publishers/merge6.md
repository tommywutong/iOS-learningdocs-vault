---
title: Publishers.Merge6
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/merge6
source_url: 'https://developer.apple.com/documentation/combine/publishers/merge6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/merge6.json'
content_hash: 'sha256:e9b2317373ecfa51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Merge6

<sub>Structure</sub>

A publisher created by applying the merge function to six upstream publishers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Merge6<A, B, C, D, E, F> where A : Publisher, B : Publisher, C : Publisher, D : Publisher, E : Publisher, F : Publisher, A.Failure == B.Failure, A.Output == B.Output, B.Failure == C.Failure, B.Output == C.Output, C.Failure == D.Failure, C.Output == D.Output, D.Failure == E.Failure, D.Output == E.Output, E.Failure == F.Failure, E.Output == F.Output
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Publisher](../publisher.md)

## Topics

### Creating a merge-six publisher

- [init(_:_:_:_:_:_:)](<merge6/init(____________).md>) — publisher created by applying the merge function to six upstream publishers.

### Merging elements

- [merge(with:)](<merge6/merge(with_).md>)
- [merge(with:_:)](<merge6/merge(with___).md>)

### Declaring supporting types

- [Output](merge6/output.md) — The kind of values published by this publisher.
- [Failure](merge6/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [a](merge6/a.md) — A publisher to merge.
- [b](merge6/b.md) — A second publisher to merge.
- [c](merge6/c.md) — A third publisher to merge.
- [d](merge6/d.md) — A fourth publisher to merge.
- [e](merge6/e.md) — A fifth publisher to merge.
- [f](merge6/f.md) — A sixth publisher to merge.

### Comparing publishers

- [==(_:_:)](<merge6/==(____).md>) — Returns a Boolean value that indicates whether two publishers are equivalent.

### Default Implementations

- [Equatable Implementations](merge6/equatable-implementations.md)

## See Also

### Combining elements from multiple publishers

- [CombineLatest](combinelatest.md) — A publisher that receives and combines the latest elements from two publishers.
- [CombineLatest3](combinelatest3.md) — A publisher that receives and combines the latest elements from three publishers.
- [CombineLatest4](combinelatest4.md) — A publisher that receives and combines the latest elements from four publishers.
- [Merge](merge.md) — A publisher created by applying the merge function to two upstream publishers.
- [Merge3](merge3.md) — A publisher created by applying the merge function to three upstream publishers.
- [Merge4](merge4.md) — A publisher created by applying the merge function to four upstream publishers.
- [Merge5](merge5.md) — A publisher created by applying the merge function to five upstream publishers.
- [Merge7](merge7.md) — A publisher created by applying the merge function to seven upstream publishers.
- [Merge8](merge8.md) — A publisher created by applying the merge function to eight upstream publishers.
- [MergeMany](mergemany.md) — A publisher created by applying the merge function to an arbitrary number of upstream publishers.
- [Zip](zip.md) — A publisher created by applying the zip function to two upstream publishers.
- [Zip3](zip3.md) — A publisher created by applying the zip function to three upstream publishers.
- [Zip4](zip4.md) — A publisher created by applying the zip function to four upstream publishers.
