---
title: wrappedValue
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/fetchrequest/wrappedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/fetchrequest/wrappedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/fetchrequest/wrappedvalue.json'
content_hash: 'sha256:d6c5670201a282c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FetchRequest](../fetchrequest.md)

# wrappedValue

<sub>Instance Property</sub>

The fetched results of the fetch request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency var wrappedValue: FetchedResults<Result> { get }
```

## Discussion

SwiftUI returns the value associated with this property when you use [FetchRequest](../fetchrequest.md) as a property wrapper, and then access the wrapped property by name. For example, consider the following `quakes` property declaration that fetches a `Quake` type that the [Loading and Displaying a Large Data Feed](../loading_and_displaying_a_large_data_feed.md) sample code project defines:

```swift
@FetchRequest(fetchRequest: request)
private var quakes: FetchedResults<Quake>
```

You access the request’s `wrappedValue`, which contains a [FetchedResults](../fetchedresults.md) instance, by referring to the `quakes` property by name:

```swift
Text("Found \(quakes.count) earthquakes")
```

If you need to separate the request and the result entities, you can declare `quakes` in two steps by using the request’s `wrappedValue` to obtain the results:

```swift
var fetchRequest = FetchRequest<Quake>(fetchRequest: request)
var quakes: FetchedResults<Quake> { fetchRequest.wrappedValue }
```

The `wrappedValue` property returns an empty array when there are no fetched results — for example, because no entities satisfy the predicate, or because the data store is empty.

## See Also

### Getting the fetched results

- [update()](<update().md>) — Updates the fetched results.
