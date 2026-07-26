---
title: FetchRequest
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/fetchrequest
source_url: 'https://developer.apple.com/documentation/swiftui/fetchrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/fetchrequest.json'
content_hash: 'sha256:958418a6edf73d97'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# FetchRequest

<sub>Structure</sub>

A property wrapper type that retrieves entities from a Core Data persistent store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @propertyWrapper @preconcurrency struct FetchRequest<Result> where Result : NSFetchRequestResult
```

## Overview

Use a `FetchRequest` property wrapper to declare a [FetchedResults](fetchedresults.md) property that provides a collection of Core Data managed objects to a SwiftUI view. The request infers the entity type from the `Result` placeholder type that you specify. Condition the request with an optional predicate and sort descriptors. For example, you can create a request to list all `Quake` managed objects that the [Loading and Displaying a Large Data Feed](loading_and_displaying_a_large_data_feed.md) sample code project defines to store earthquake data, sorted by their `time` property:

```swift
@FetchRequest(sortDescriptors: [SortDescriptor(\.time, order: .reverse)])
private var quakes: FetchedResults<Quake> // Define Quake in your model.
```

Alternatively, when you need more flexibility, you can initialize the request with a configured [NSFetchRequest](../coredata/nsfetchrequest.md) instance:

```swift
@FetchRequest(fetchRequest: request)
private var quakes: FetchedResults<Quake>
```

Always declare properties that have a fetch request wrapper as private. This lets the compiler help you avoid accidentally setting the property from the memberwise initializer of the enclosing view.

The fetch request and its results use the managed object context stored in the environment, which you can access using the [managedObjectContext](environmentvalues/managedobjectcontext.md) environment value. To support user interface activity, you typically rely on the [viewContext](../coredata/nspersistentcontainer/viewcontext.md) property of a shared [NSPersistentContainer](../coredata/nspersistentcontainer.md) instance. For example, you can set a context on your top level content view using a shared container that you define as part of your model:

```swift
ContentView()
    .environment(
        \.managedObjectContext,
        QuakesProvider.shared.container.viewContext)
```

When you need to dynamically change the predicate or sort descriptors, access the request’s [Configuration](fetchrequest/configuration.md) structure. To create a request that groups the fetched results according to a characteristic that they share, use [SectionedFetchRequest](sectionedfetchrequest.md) instead.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [DynamicProperty](dynamicproperty.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a fetch request

- [init(sortDescriptors:predicate:animation:)](<fetchrequest/init(sortdescriptors_predicate_animation_).md>) — Creates a fetch request based on a predicate and reference type sort parameters.
- [init(entity:sortDescriptors:predicate:animation:)](<fetchrequest/init(entity_sortdescriptors_predicate_animation_).md>) — Creates a fetch request for a specified entity description, based on a predicate and sort parameters.

### Creating a fully configured fetch request

- [init(fetchRequest:animation:)](<fetchrequest/init(fetchrequest_animation_).md>) — Creates a fully configured fetch request that uses the specified animation when updating results.
- [init(fetchRequest:transaction:)](<fetchrequest/init(fetchrequest_transaction_).md>) — Creates a fully configured fetch request that uses the specified transaction when updating results.

### Configuring a request dynamically

- [Configuration](fetchrequest/configuration.md) — The request’s configurable properties.
- [projectedValue](fetchrequest/projectedvalue.md) — A binding to the request’s mutable configuration properties.

### Getting the fetched results

- [update()](<fetchrequest/update().md>) — Updates the fetched results.
- [wrappedValue](fetchrequest/wrappedvalue.md) — The fetched results of the fetch request.

### Default Implementations

- [DynamicProperty Implementations](fetchrequest/dynamicproperty-implementations.md)

## See Also

### Accessing Core Data

- [Loading and displaying a large data feed](loading-and-displaying-a-large-data-feed.md) — Consume data in the background, and lower memory use by batching imports and preventing duplicate records.
- [managedObjectContext](environmentvalues/managedobjectcontext.md)
- [FetchedResults](fetchedresults.md) — A collection of results retrieved from a Core Data store.
- [SectionedFetchRequest](sectionedfetchrequest.md) — A property wrapper type that retrieves entities, grouped into sections, from a Core Data persistent store.
- [SectionedFetchResults](sectionedfetchresults.md) — A collection of results retrieved from a Core Data persistent store, grouped into sections.
