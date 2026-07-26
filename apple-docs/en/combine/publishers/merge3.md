---
title: Publishers.Merge3
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/merge3
source_url: 'https://developer.apple.com/documentation/combine/publishers/merge3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/merge3.json'
content_hash: 'sha256:9ca377cdefdc931a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Merge3

<sub>Structure</sub>

A publisher created by applying the merge function to three upstream publishers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Merge3<A, B, C> where A : Publisher, B : Publisher, C : Publisher, A.Failure == B.Failure, A.Output == B.Output, B.Failure == C.Failure, B.Output == C.Output
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Publisher](../publisher.md)

## Topics

### Creating a merge-three publisher

- [init(_:_:_:)](<merge3/init(______).md>) — Creates a publisher created by applying the merge function to three upstream publishers.

### Merging elements

- [merge(with:)](<merge3/merge(with_).md>)
- [merge(with:_:)](<merge3/merge(with___).md>)
- [merge(with:_:_:)](<merge3/merge(with_____).md>)
- [merge(with:_:_:_:)](<merge3/merge(with_______).md>)
- [merge(with:_:_:_:_:)](<merge3/merge(with_________).md>)

### Declaring supporting types

- [Output](merge3/output.md) — The kind of values published by this publisher.
- [Failure](merge3/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [a](merge3/a.md) — A publisher to merge.
- [b](merge3/b.md) — A second publisher to merge.
- [c](merge3/c.md) — A third publisher to merge.

### Comparing publishers

- [==(_:_:)](<merge3/==(____).md>) — Returns a Boolean value that indicates whether two publishers are equivalent.

### Default Implementations

- [Equatable Implementations](merge3/equatable-implementations.md)

## See Also

### Combining elements from multiple publishers

- [CombineLatest](combinelatest.md) — A publisher that receives and combines the latest elements from two publishers.
- [CombineLatest3](combinelatest3.md) — A publisher that receives and combines the latest elements from three publishers.
- [CombineLatest4](combinelatest4.md) — A publisher that receives and combines the latest elements from four publishers.
- [Merge](merge.md) — A publisher created by applying the merge function to two upstream publishers.
- [Merge4](merge4.md) — A publisher created by applying the merge function to four upstream publishers.
- [Merge5](merge5.md) — A publisher created by applying the merge function to five upstream publishers.
- [Merge6](merge6.md) — A publisher created by applying the merge function to six upstream publishers.
- [Merge7](merge7.md) — A publisher created by applying the merge function to seven upstream publishers.
- [Merge8](merge8.md) — A publisher created by applying the merge function to eight upstream publishers.
- [MergeMany](mergemany.md) — A publisher created by applying the merge function to an arbitrary number of upstream publishers.
- [Zip](zip.md) — A publisher created by applying the zip function to two upstream publishers.
- [Zip3](zip3.md) — A publisher created by applying the zip function to three upstream publishers.
- [Zip4](zip4.md) — A publisher created by applying the zip function to four upstream publishers.
