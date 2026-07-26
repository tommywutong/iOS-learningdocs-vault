---
title: projectedValue
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/fetchrequest/projectedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/fetchrequest/projectedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/fetchrequest/projectedvalue.json'
content_hash: 'sha256:4a00cac0e7ee8b79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FetchRequest](../fetchrequest.md)

# projectedValue

<sub>Instance Property</sub>

A binding to the request’s mutable configuration properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency var projectedValue: Binding<FetchRequest<Result>.Configuration> { get }
```

## Discussion

SwiftUI returns the value associated with this property when you use [FetchRequest](../fetchrequest.md) as a property wrapper on a [FetchedResults](../fetchedresults.md) instance, and then access the results with a dollar sign (`$`) prefix. The value that SwiftUI returns is a [Binding](../binding.md) to the request’s [Configuration](configuration.md) structure, which dynamically configures the request.

For example, consider the following fetch request for a type that the [Loading and Displaying a Large Data Feed](../loading_and_displaying_a_large_data_feed.md) sample code project defines to store earthquake data, sorted based on the `time` property:

```swift
@FetchRequest(sortDescriptors: [SortDescriptor(\.time, order: .reverse)])
private var quakes: FetchedResults<Quake>
```

You can use the projected value to enable a [Table](../table.md) instance to make updates:

```swift
Table(quakes, sortOrder: $quakes.sortDescriptors) {
    TableColumn("Place", value: \.place)
    TableColumn("Time", value: \.time) { quake in
        Text(quake.time, style: .time)
    }
}
```

Because you initialize the table using a binding to the descriptors, the table can modify the sort in response to actions that the user takes, like clicking a column header.

## See Also

### Configuring a request dynamically

- [Configuration](configuration.md) — The request’s configurable properties.
