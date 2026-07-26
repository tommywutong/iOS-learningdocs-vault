---
title: 'init(fetchRequest:transaction:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/fetchrequest/init(fetchrequest:transaction:)'
source_url: 'https://developer.apple.com/documentation/swiftui/fetchrequest/init(fetchrequest:transaction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/fetchrequest/init%28fetchrequest%3Atransaction%3A%29.json'
content_hash: 'sha256:0134784f575bf4e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FetchRequest](../fetchrequest.md)

# init(fetchRequest:transaction:)

<sub>Initializer</sub>

Creates a fully configured fetch request that uses the specified transaction when updating results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(fetchRequest: NSFetchRequest<Result>, transaction: Transaction)
```

## Parameters

- `fetchRequest` — An [NSFetchRequest](../../coredata/nsfetchrequest.md) instance that describes the search criteria for retrieving data from the persistent store.

- `transaction` — A transaction to use for user interface changes that result from changes to the fetched results.

## Discussion

Use this initializer if you need a fetch request with updates that affect the user interface based on a [Transaction](../transaction.md). Otherwise, use [init(fetchRequest:animation:)](<init(fetchrequest_animation_).md>).

## See Also

### Creating a fully configured fetch request

- [init(fetchRequest:animation:)](<init(fetchrequest_animation_).md>) — Creates a fully configured fetch request that uses the specified animation when updating results.
