---
title: 'init(fetchRequest:animation:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/fetchrequest/init(fetchrequest:animation:)'
source_url: 'https://developer.apple.com/documentation/swiftui/fetchrequest/init(fetchrequest:animation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/fetchrequest/init%28fetchrequest%3Aanimation%3A%29.json'
content_hash: 'sha256:aefb70795966ccfa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FetchRequest](../fetchrequest.md)

# init(fetchRequest:animation:)

<sub>Initializer</sub>

Creates a fully configured fetch request that uses the specified animation when updating results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(fetchRequest: NSFetchRequest<Result>, animation: Animation? = nil)
```

## Parameters

- `fetchRequest` — An [NSFetchRequest](../../coredata/nsfetchrequest.md) instance that describes the search criteria for retrieving data from the persistent store.

- `animation` — The animation to use for user interface changes that result from changes to the fetched results.

## Discussion

Use this initializer when you want to configure a fetch request with more than a predicate and sort descriptors. For example, you can vend a request from a `Quake` managed object that the [Loading and Displaying a Large Data Feed](../loading_and_displaying_a_large_data_feed.md) sample code project defines to store earthquake data. Limit the number of results to `1000` by setting a [fetchLimit](../../coredata/nsfetchrequest/fetchlimit.md) for the request:

```swift
extension Quake {
    var request: NSFetchRequest<Quake> {
        let request = NSFetchRequest<Quake>(entityName: "Quake")
        request.sortDescriptors = [
            NSSortDescriptor(
                keyPath: \Quake.time,
                ascending: true)]
        request.fetchLimit = 1000
        return request
    }
}
```

Use the request to define a [FetchedResults](../fetchedresults.md) property:

```swift
@FetchRequest(fetchRequest: Quake.request)
private var quakes: FetchedResults<Quake>
```

If you only need to configure the request’s predicate and sort descriptors, use [init(sortDescriptors:predicate:animation:)](<init(sortdescriptors_predicate_animation_).md>) instead. If you need to specify a [Transaction](../transaction.md) rather than an optional [Animation](../animation.md), use [init(fetchRequest:transaction:)](<init(fetchrequest_transaction_).md>).

## See Also

### Creating a fully configured fetch request

- [init(fetchRequest:transaction:)](<init(fetchrequest_transaction_).md>) — Creates a fully configured fetch request that uses the specified transaction when updating results.
