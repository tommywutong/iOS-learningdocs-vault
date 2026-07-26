---
title: 'init(fetchRequest:sectionIdentifier:transaction:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/sectionedfetchrequest/init(fetchrequest:sectionidentifier:transaction:)'
source_url: 'https://developer.apple.com/documentation/swiftui/sectionedfetchrequest/init(fetchrequest:sectionidentifier:transaction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sectionedfetchrequest/init%28fetchrequest%3Asectionidentifier%3Atransaction%3A%29.json'
content_hash: 'sha256:3f069e3a20f38bc6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SectionedFetchRequest](../sectionedfetchrequest.md)

# init(fetchRequest:sectionIdentifier:transaction:)

<sub>Initializer</sub>

Creates a fully configured sectioned fetch request that uses the specified transaction when updating results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(fetchRequest: NSFetchRequest<Result>, sectionIdentifier: KeyPath<Result, SectionIdentifier>, transaction: Transaction)
```

## Parameters

- `fetchRequest` — An [NSFetchRequest](../../coredata/nsfetchrequest.md) instance that describes the search criteria for retrieving data from the persistent store.

- `sectionIdentifier` — A key path that SwiftUI applies to the `Result` type to get an object’s section identifier.

- `transaction` — A transaction to use for user interface changes that result from changes to the fetched results.

## Discussion

Use this initializer if you need a fetch request with updates that affect the user interface based on a [Transaction](../transaction.md). Otherwise, use [init(fetchRequest:sectionIdentifier:animation:)](<init(fetchrequest_sectionidentifier_animation_).md>).

## See Also

### Creating a fully configured fetch request

- [init(fetchRequest:sectionIdentifier:animation:)](<init(fetchrequest_sectionidentifier_animation_).md>) — Creates a fully configured sectioned fetch request that uses the specified animation when updating results.
