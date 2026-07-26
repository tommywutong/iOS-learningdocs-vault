---
title: NSFetchedResultsSectionInfo
framework: Core Data
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchedresultssectioninfo
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchedresultssectioninfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchedresultssectioninfo.json'
content_hash: 'sha256:d94595b48f0b98c3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSFetchedResultsSectionInfo

<sub>Protocol</sub>

A protocol that defines the interface for section objects vended by a fetched results controller.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NSFetchedResultsSectionInfo
```

## Topics

### Accessing Objects

- [numberOfObjects](nsfetchedresultssectioninfo/numberofobjects.md) — The number of objects (rows) in the section.
- [objects](nsfetchedresultssectioninfo/objects.md) — The array of objects in the section.

### Accessing the Name and Title

- [name](nsfetchedresultssectioninfo/name.md) — The name of the section.
- [indexTitle](nsfetchedresultssectioninfo/indextitle.md) — The index title of the section.

## See Also

### Responding to Changes

- [NSFetchedResultsControllerDelegate](nsfetchedresultscontrollerdelegate.md) — A delegate protocol that describes the methods that the associated fetched results controller calls when the fetch results change.
- [NSFetchRequestResultType](nsfetchrequestresulttype.md) — Constants that specify the possible result types a fetch request can return.
- [NSFetchedResultsChangeType](nsfetchedresultschangetype.md) — Constants that specify the possible types of changes that are reported.
