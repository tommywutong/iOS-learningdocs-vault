---
title: wrappedValue
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sectionedfetchrequest/wrappedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/sectionedfetchrequest/wrappedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sectionedfetchrequest/wrappedvalue.json'
content_hash: 'sha256:228aa75d36ab049e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SectionedFetchRequest](../sectionedfetchrequest.md)

# wrappedValue

<sub>Instance Property</sub>

The fetched results of the fetch request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency var wrappedValue: SectionedFetchResults<SectionIdentifier, Result> { get }
```

## Discussion

This property behaves like the [wrappedValue](../fetchrequest/wrappedvalue.md) of a [FetchRequest](../fetchrequest.md). In particular, SwiftUI returns the value associated with this property when you use [SectionedFetchRequest](../sectionedfetchrequest.md) as a property wrapper and then access the wrapped property by name. For example, consider the following `quakes` property declaration that fetches a `Quake` type that the [Loading and Displaying a Large Data Feed](../loading_and_displaying_a_large_data_feed.md) sample code project defines:

```swift
@SectionedFetchRequest<String, Quake>(
    sectionIdentifier: \.day,
    sortDescriptors: [SortDescriptor(\.time, order: .reverse)]
)
private var quakes: SectionedFetchResults<String, Quake>
```

You access the request’s `wrappedValue`, which contains a [SectionedFetchResults](../sectionedfetchresults.md) instance, by referring to the `quakes` property by name. That value is a collection of sections, each of which contains a group of managed objects:

```swift
Text("Found \(quakes.count) days of earthquakes")
```

If you need to separate the request and the result entities, you can declare `quakes` in two steps by using the request’s `wrappedValue` to obtain the results:

```swift
var fetchRequest = SectionedFetchRequest<String, Quake>(
    fetchRequest: request,
    sectionIdentifier: \.day)
var quakes: SectionedFetchedResults<String, Quake> { fetchRequest.wrappedValue }
```

The `wrappedValue` property returns an empty array when there are no fetched results; for example, because no entities satisfy the predicate, or because the data store is empty.

## See Also

### Getting the fetched results

- [update()](<update().md>) — Updates the fetched results.
