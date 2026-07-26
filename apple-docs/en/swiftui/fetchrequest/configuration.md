---
title: FetchRequest.Configuration
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/fetchrequest/configuration
source_url: 'https://developer.apple.com/documentation/swiftui/fetchrequest/configuration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/fetchrequest/configuration.json'
content_hash: 'sha256:26301da3ed96b65a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FetchRequest](../fetchrequest.md)

# FetchRequest.Configuration

<sub>Structure</sub>

The request’s configurable properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct Configuration
```

## Overview

You initialize a [FetchRequest](../fetchrequest.md) with an optional predicate and sort descriptors, either explicitly or using a configured [NSFetchRequest](../../coredata/nsfetchrequest.md). Later, you can dynamically update the predicate and sort parameters using the request’s configuration structure.

You access or bind to a request’s configuration components through properties on the associated [FetchedResults](../fetchedresults.md) instance.

### Configure using a binding

Get a [Binding](../binding.md) to a fetch request’s configuration structure by accessing the request’s [projectedValue](projectedvalue.md), which you do by using the dollar sign (`$`) prefix on the associated results property. For example, you can create a request for `Quake` entities — a managed object type that the [Loading and Displaying a Large Data Feed](../loading_and_displaying_a_large_data_feed.md) sample code project defines — that initially sorts the results by time:

```swift
@FetchRequest(sortDescriptors: [SortDescriptor(\.time, order: .reverse)])
private var quakes: FetchedResults<Quake>
```

Then you can bind the request’s sort descriptors, which you access through the `quakes` result, to those of a [Table](../table.md) instance:

```swift
Table(quakes, sortOrder: $quakes.sortDescriptors) {
    TableColumn("Place", value: \.place)
    TableColumn("Time", value: \.time) { quake in
        Text(quake.time, style: .time)
    }
}
```

A user who clicks on a table column header initiates the following sequence of events:

1. The table updates the sort descriptors through the binding.
2. The modified sort descriptors reconfigure the request.
3. The reconfigured request fetches new results.
4. SwiftUI redraws the table in response to new results.

### Set configuration directly

If you need to access the fetch request’s configuration elements directly, use the [nsPredicate](../fetchedresults/nspredicate.md) and [sortDescriptors](../fetchedresults/sortdescriptors.md) or [nsSortDescriptors](../fetchedresults/nssortdescriptors.md) properties of the [FetchedResults](../fetchedresults.md) instance. Continuing the example above, to enable the user to dynamically update the predicate, declare a [State](../state.md) property to hold a query string:

```swift
@State private var query = ""
```

Then add an [onChange(of:initial:_:)](<../view/onchange(of_initial___).md>) modifier to the [Table](../table.md) that sets a new predicate any time the query changes:

```swift
.onChange(of: query) { _, value in
    quakes.nsPredicate = query.isEmpty
        ? nil
        : NSPredicate(format: "place CONTAINS %@", value)
}
```

To give the user control over the string, add a [TextField](../textfield.md) in your user interface that’s bound to the `query` state:

```swift
TextField("Filter", text: $query)
```

When the user types into the text field, the predicate updates, the request fetches new results, and SwiftUI redraws the table.

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Setting a predicate

- [nsPredicate](configuration/nspredicate.md) — The request’s predicate.

### Setting sort descriptors

- [sortDescriptors](configuration/sortdescriptors.md) — The request’s sort descriptors, accessed as value types.
- [nsSortDescriptors](configuration/nssortdescriptors.md) — The request’s sort descriptors, accessed as reference types.

## See Also

### Configuring a request dynamically

- [projectedValue](projectedvalue.md) — A binding to the request’s mutable configuration properties.
