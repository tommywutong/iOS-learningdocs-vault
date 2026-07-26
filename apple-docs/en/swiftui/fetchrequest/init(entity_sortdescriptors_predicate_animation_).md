---
title: 'init(entity:sortDescriptors:predicate:animation:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/fetchrequest/init(entity:sortdescriptors:predicate:animation:)'
source_url: 'https://developer.apple.com/documentation/swiftui/fetchrequest/init(entity:sortdescriptors:predicate:animation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/fetchrequest/init%28entity%3Asortdescriptors%3Apredicate%3Aanimation%3A%29.json'
content_hash: 'sha256:0c46b94a73d7f3a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FetchRequest](../fetchrequest.md)

# init(entity:sortDescriptors:predicate:animation:)

<sub>Initializer</sub>

Creates a fetch request for a specified entity description, based on a predicate and sort parameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(entity: NSEntityDescription, sortDescriptors: [NSSortDescriptor], predicate: NSPredicate? = nil, animation: Animation? = nil)
```

## Parameters

- `entity` — The description of the Core Data entity to fetch.

- `sortDescriptors` — An array of sort descriptors that define the sort order of the fetched results.

- `predicate` — An [NSPredicate](../../foundation/nspredicate.md) instance that defines logical conditions used to filter the fetched results.

- `animation` — The animation to use for user interface changes that result from changes to the fetched results.

## Discussion

Use this initializer if you need to explicitly specify the entity type for the request. If you specify a placeholder `Result` type in the request declaration, use the [init(sortDescriptors:predicate:animation:)](<init(sortdescriptors_predicate_animation_).md>) initializer to let the request infer the entity type. If you need more control over the fetch request configuration, use [init(fetchRequest:animation:)](<init(fetchrequest_animation_).md>).

## See Also

### Creating a fetch request

- [init(sortDescriptors:predicate:animation:)](<init(sortdescriptors_predicate_animation_).md>) — Creates a fetch request based on a predicate and reference type sort parameters.
