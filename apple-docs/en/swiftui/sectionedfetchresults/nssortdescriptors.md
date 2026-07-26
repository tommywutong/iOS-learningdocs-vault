---
title: nsSortDescriptors
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sectionedfetchresults/nssortdescriptors
source_url: 'https://developer.apple.com/documentation/swiftui/sectionedfetchresults/nssortdescriptors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sectionedfetchresults/nssortdescriptors.json'
content_hash: 'sha256:1fb9587f2e01d1b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SectionedFetchResults](../sectionedfetchresults.md)

# nsSortDescriptors

<sub>Instance Property</sub>

The request’s sort descriptors, accessed as reference types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency var nsSortDescriptors: [NSSortDescriptor] { get nonmutating set }
```

## Discussion

Set this value to cause the associated [SectionedFetchRequest](../sectionedfetchrequest.md) to execute a fetch with a new collection of [NSSortDescriptor](../../foundation/nssortdescriptor.md) instances. The order of managed objects stored in the results collection may change as a result. Use care to coordinate section and sort updates, as described in [Configuration](../sectionedfetchrequest/configuration.md).

If you want to use [SortDescriptor](../../foundation/sortdescriptor.md) instances, set [sortDescriptors](sortdescriptors.md) instead.

## See Also

### Configuring the associated sectioned fetch request

- [nsPredicate](nspredicate.md) — The request’s predicate.
- [sortDescriptors](sortdescriptors.md) — The request’s sort descriptors, accessed as value types.
- [sectionIdentifier](sectionidentifier.md) — The key path that the system uses to group fetched results into sections.
- [Section](section.md) — A collection of fetched results that share a specified identifier.
