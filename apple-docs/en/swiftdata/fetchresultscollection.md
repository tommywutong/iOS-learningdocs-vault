---
title: FetchResultsCollection
framework: SwiftData
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/fetchresultscollection
source_url: 'https://developer.apple.com/documentation/swiftdata/fetchresultscollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/fetchresultscollection.json'
content_hash: 'sha256:15971758bd65246b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# FetchResultsCollection

<sub>Structure</sub>

A collection that efficiently provides the results of a completed fetch.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct FetchResultsCollection<Element>
```

## Relationships

- **Conforms To**: [BidirectionalCollection](../swift/bidirectionalcollection.md), [Collection](../swift/collection.md), [RandomAccessCollection](../swift/randomaccesscollection.md), [Sequence](../swift/sequence.md)

## See Also

### Fetching models

- [fetch(_:)](<modelcontext/fetch(__).md>) — Returns an array of typed models that match the criteria of the specified fetch descriptor.
- [fetch(_:batchSize:)](<modelcontext/fetch(__batchsize_).md>) — Returns a collection of typed models, in batches, which match the criteria of the specified fetch descriptor.
- [fetchCount(_:)](<modelcontext/fetchcount(__).md>) — Returns the number of models that match the criteria of the specified fetch descriptor.
- [FetchDescriptor](fetchdescriptor.md) — A type that describes the criteria, sort order, and any additional configuration to use when performing a fetch.
- [enumerate(_:batchSize:allowEscapingMutations:block:)](<modelcontext/enumerate(__batchsize_allowescapingmutations_block_).md>) — Runs a closure for each model that matches the criteria of the specified fetch descriptor.
- [model(for:)](<modelcontext/model(for_).md>) — Returns the persistent model for the specified identifier.
- [registeredModel(for:)](<modelcontext/registeredmodel(for_).md>) — Returns the typed model for the specified identifier.
