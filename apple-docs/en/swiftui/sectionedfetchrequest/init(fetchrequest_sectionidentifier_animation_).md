---
title: 'init(fetchRequest:sectionIdentifier:animation:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/sectionedfetchrequest/init(fetchrequest:sectionidentifier:animation:)'
source_url: 'https://developer.apple.com/documentation/swiftui/sectionedfetchrequest/init(fetchrequest:sectionidentifier:animation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sectionedfetchrequest/init%28fetchrequest%3Asectionidentifier%3Aanimation%3A%29.json'
content_hash: 'sha256:3b072e7404bf87d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SectionedFetchRequest](../sectionedfetchrequest.md)

# init(fetchRequest:sectionIdentifier:animation:)

<sub>Initializer</sub>

Creates a fully configured sectioned fetch request that uses the specified animation when updating results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(fetchRequest: NSFetchRequest<Result>, sectionIdentifier: KeyPath<Result, SectionIdentifier>, animation: Animation? = nil)
```

## Parameters

- `fetchRequest` — An [NSFetchRequest](../../coredata/nsfetchrequest.md) instance that describes the search criteria for retrieving data from the persistent store.

- `sectionIdentifier` — A key path that SwiftUI applies to the `Result` type to get an object’s section identifier.

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

Use the request to define a `SectionedFetchedResults` property:

```swift
@SectionedFetchRequest<String, Quake>(
    fetchRequest: Quake.request,
    sectionIdentifier: \.day)
private var quakes: FetchedResults<String, Quake>
```

If you only need to configure the request’s section identifier, predicate, and sort descriptors, use [init(sectionIdentifier:sortDescriptors:predicate:animation:)](<init(sectionidentifier_sortdescriptors_predicate_animation_).md>) instead. If you need to specify a [Transaction](../transaction.md) rather than an optional [Animation](../animation.md), use [init(fetchRequest:sectionIdentifier:transaction:)](<init(fetchrequest_sectionidentifier_transaction_).md>).

## See Also

### Creating a fully configured fetch request

- [init(fetchRequest:sectionIdentifier:transaction:)](<init(fetchrequest_sectionidentifier_transaction_).md>) — Creates a fully configured sectioned fetch request that uses the specified transaction when updating results.
