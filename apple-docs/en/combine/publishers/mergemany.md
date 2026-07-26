---
title: Publishers.MergeMany
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/mergemany
source_url: 'https://developer.apple.com/documentation/combine/publishers/mergemany'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/mergemany.json'
content_hash: 'sha256:cd3a775a989d79e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.MergeMany

<sub>Structure</sub>

A publisher created by applying the merge function to an arbitrary number of upstream publishers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MergeMany<Upstream> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Publisher](../publisher.md)

## Topics

### Creating a merge many publisher

- [init(_:)](<mergemany/init(__)-1hsqd.md>) — Creates a publisher created by applying the merge function to an arbitrary number of upstream publishers.
- [init(_:)](<mergemany/init(__)-3hrmo.md>) — Creates a publisher created by applying the merge function to a sequence of upstream publishers.

### Merging elements

- [merge(with:)](<mergemany/merge(with_).md>) — Combines elements from this publisher with those from another publisher of the same type, delivering an interleaved sequence of elements.

### Declaring supporting types

- [Output](mergemany/output.md) — The kind of values published by this publisher.
- [Failure](mergemany/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [publishers](mergemany/publishers.md) — The array of upstream publishers that this publisher merges together.

### Comparing publishers

- [==(_:_:)](<mergemany/==(____).md>) — Returns a Boolean value that indicates whether two publishers are equivalent.

### Default Implementations

- [Equatable Implementations](mergemany/equatable-implementations.md)

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
- [Zip](zip.md) — A publisher created by applying the zip function to two upstream publishers.
- [Zip3](zip3.md) — A publisher created by applying the zip function to three upstream publishers.
- [Zip4](zip4.md) — A publisher created by applying the zip function to four upstream publishers.
