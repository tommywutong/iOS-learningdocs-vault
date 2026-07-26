---
title: NSFetchedResultsChangeType
framework: Core Data
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchedresultschangetype
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchedresultschangetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchedresultschangetype.json'
content_hash: 'sha256:efa0f3e60846674e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSFetchedResultsChangeType

<sub>Enumeration</sub>

Constants that specify the possible types of changes that are reported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NSFetchedResultsChangeType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [NSFetchedResultsChangeInsert](nsfetchedresultschangetype/insert.md) — Specifies that an object was inserted.
- [NSFetchedResultsChangeDelete](nsfetchedresultschangetype/delete.md) — Specifies that an object was deleted.
- [NSFetchedResultsChangeMove](nsfetchedresultschangetype/move.md) — Specifies that an object was moved.
- [NSFetchedResultsChangeUpdate](nsfetchedresultschangetype/update.md) — Specifies that an object was changed.

### Initializers

- [init(rawValue:)](<nsfetchedresultschangetype/init(rawvalue_).md>)

## See Also

### Responding to Changes

- [NSFetchedResultsControllerDelegate](nsfetchedresultscontrollerdelegate.md) — A delegate protocol that describes the methods that the associated fetched results controller calls when the fetch results change.
- [NSFetchedResultsSectionInfo](nsfetchedresultssectioninfo.md) — A protocol that defines the interface for section objects vended by a fetched results controller.
- [NSFetchRequestResultType](nsfetchrequestresulttype.md) — Constants that specify the possible result types a fetch request can return.
