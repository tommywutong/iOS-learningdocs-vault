---
title: sectionIdentifier
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sectionedfetchresults/sectionidentifier
source_url: 'https://developer.apple.com/documentation/swiftui/sectionedfetchresults/sectionidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sectionedfetchresults/sectionidentifier.json'
content_hash: 'sha256:10bc37e82a348f41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SectionedFetchResults](../sectionedfetchresults.md)

# sectionIdentifier

<sub>Instance Property</sub>

The key path that the system uses to group fetched results into sections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency var sectionIdentifier: KeyPath<Result, SectionIdentifier> { get nonmutating set }
```

## Discussion

Set this value to cause the associated [SectionedFetchRequest](../sectionedfetchrequest.md) to execute a fetch with a new section identifier, producing an updated collection of results. Changing this value produces a new set of sections. Use care to coordinate section and sort updates, as described in [Configuration](../sectionedfetchrequest/configuration.md).

## See Also

### Configuring the associated sectioned fetch request

- [nsPredicate](nspredicate.md) — The request’s predicate.
- [sortDescriptors](sortdescriptors.md) — The request’s sort descriptors, accessed as value types.
- [nsSortDescriptors](nssortdescriptors.md) — The request’s sort descriptors, accessed as reference types.
- [Section](section.md) — A collection of fetched results that share a specified identifier.
