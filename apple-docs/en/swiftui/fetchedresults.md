---
title: FetchedResults
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/fetchedresults
source_url: 'https://developer.apple.com/documentation/swiftui/fetchedresults'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/fetchedresults.json'
content_hash: 'sha256:5b92eb1da44ce87d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# FetchedResults

<sub>Structure</sub>

A collection of results retrieved from a Core Data store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct FetchedResults<Result> where Result : NSFetchRequestResult
```

## Overview

Use a `FetchedResults` instance to show or edit Core Data managed objects in your app’s user interface. You request a particular set of results by specifying a `Result` type as the entity type, and annotating the fetched results property declaration with a [FetchRequest](fetchrequest.md) property wrapper. For example, you can create a request to list all `Quake` managed objects that the [Loading and Displaying a Large Data Feed](loading_and_displaying_a_large_data_feed.md) sample code project defines to store earthquake data, sorted by their `time` property:

```swift
@FetchRequest(sortDescriptors: [SortDescriptor(\.time, order: .reverse)])
private var quakes: FetchedResults<Quake>
```

The results instance conforms to [RandomAccessCollection](../swift/randomaccesscollection.md), so you access it like any other collection. For example, you can create a [List](list.md) that iterates over all the results:

```swift
List(quakes) { quake in
    NavigationLink(destination: QuakeDetail(quake: quake)) {
        QuakeRow(quake: quake)
    }
}
```

When you need to dynamically change the request’s predicate or sort descriptors, set the result instance’s [nsPredicate](fetchedresults/nspredicate.md) and [sortDescriptors](fetchedresults/sortdescriptors.md) or [nsSortDescriptors](fetchedresults/nssortdescriptors.md) properties, respectively.

The fetch request and its results use the managed object context stored in the environment, which you can access using the [managedObjectContext](environmentvalues/managedobjectcontext.md) environment value. To support user interface activity, you typically rely on the [viewContext](../coredata/nspersistentcontainer/viewcontext.md) property of a shared [NSPersistentContainer](../coredata/nspersistentcontainer.md) instance. For example, you can set a context on your top level content view using a container that you define as part of your model:

```swift
ContentView()
    .environment(
        \.managedObjectContext,
        QuakesProvider.shared.container.viewContext)
```

## Relationships

- **Conforms To**: [BidirectionalCollection](../swift/bidirectionalcollection.md), [Collection](../swift/collection.md), [RandomAccessCollection](../swift/randomaccesscollection.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Sequence](../swift/sequence.md)

## Topics

### Configuring the associated fetch request

- [nsPredicate](fetchedresults/nspredicate.md) — The request’s predicate.
- [sortDescriptors](fetchedresults/sortdescriptors.md) — The request’s sort descriptors, accessed as value types.
- [nsSortDescriptors](fetchedresults/nssortdescriptors.md) — The request’s sort descriptors, accessed as reference types.

### Getting indices

- [startIndex](fetchedresults/startindex.md) — The index of the first entity in the results collection.
- [endIndex](fetchedresults/endindex.md) — The index that’s one greater than the last valid subscript argument.

### Getting results

- [subscript(_:)](<fetchedresults/subscript(__).md>) — Gets the entity at the specified index.

## See Also

### Accessing Core Data

- [Loading and displaying a large data feed](loading-and-displaying-a-large-data-feed.md) — Consume data in the background, and lower memory use by batching imports and preventing duplicate records.
- [managedObjectContext](environmentvalues/managedobjectcontext.md)
- [FetchRequest](fetchrequest.md) — A property wrapper type that retrieves entities from a Core Data persistent store.
- [SectionedFetchRequest](sectionedfetchrequest.md) — A property wrapper type that retrieves entities, grouped into sections, from a Core Data persistent store.
- [SectionedFetchResults](sectionedfetchresults.md) — A collection of results retrieved from a Core Data persistent store, grouped into sections.
