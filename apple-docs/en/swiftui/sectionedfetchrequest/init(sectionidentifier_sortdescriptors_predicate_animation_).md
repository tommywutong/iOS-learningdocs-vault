---
title: 'init(sectionIdentifier:sortDescriptors:predicate:animation:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/sectionedfetchrequest/init(sectionidentifier:sortdescriptors:predicate:animation:)'
source_url: 'https://developer.apple.com/documentation/swiftui/sectionedfetchrequest/init(sectionidentifier:sortdescriptors:predicate:animation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sectionedfetchrequest/init%28sectionidentifier%3Asortdescriptors%3Apredicate%3Aanimation%3A%29.json'
content_hash: 'sha256:45021e5ad8d3c7dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SectionedFetchRequest](../sectionedfetchrequest.md)

# init(sectionIdentifier:sortDescriptors:predicate:animation:)

<sub>Initializer</sub>

Creates a sectioned fetch request based on a section identifier, a predicate, and reference type sort parameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(sectionIdentifier: KeyPath<Result, SectionIdentifier>, sortDescriptors: [NSSortDescriptor], predicate: NSPredicate? = nil, animation: Animation? = nil)
```

## Parameters

- `sectionIdentifier` — A key path that SwiftUI applies to the `Result` type to get an object’s section identifier.

- `sortDescriptors` — An array of sort descriptors that define the sort order of the fetched results.

- `predicate` — An [NSPredicate](../../foundation/nspredicate.md) instance that defines logical conditions used to filter the fetched results.

- `animation` — The animation to use for user interface changes that result from changes to the fetched results.

## Discussion

The request gets the entity type from the `Result` instance by calling that managed object’s [entity()](<../../coredata/nsmanagedobject/entity().md>) type method. If you need to specify the entity type explicitly, use the [init(entity:sectionIdentifier:sortDescriptors:predicate:animation:)](<init(entity_sectionidentifier_sortdescriptors_predicate_animation_).md>) initializer instead. If you need more control over the fetch request configuration, use [init(fetchRequest:sectionIdentifier:animation:)](<init(fetchrequest_sectionidentifier_animation_).md>). For value type sort descriptors, use [init(sectionIdentifier:sortDescriptors:predicate:animation:)](<init(sectionidentifier_sortdescriptors_predicate_animation_).md>).

## See Also

### Creating a fetch request

- [init(entity:sectionIdentifier:sortDescriptors:predicate:animation:)](<init(entity_sectionidentifier_sortdescriptors_predicate_animation_).md>) — Creates a sectioned fetch request for a specified entity description, based on a section identifier, a predicate, and sort parameters.
