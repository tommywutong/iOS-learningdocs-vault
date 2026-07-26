---
title: nsPredicate
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sectionedfetchresults/nspredicate
source_url: 'https://developer.apple.com/documentation/swiftui/sectionedfetchresults/nspredicate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sectionedfetchresults/nspredicate.json'
content_hash: 'sha256:f621806688386b55'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SectionedFetchResults](../sectionedfetchresults.md)

# nsPredicate

<sub>Instance Property</sub>

The request’s predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency var nsPredicate: NSPredicate? { get nonmutating set }
```

## Discussion

Set this value to cause the associated [SectionedFetchRequest](../sectionedfetchrequest.md) to execute a fetch with a new predicate, producing an updated collection of results.

## See Also

### Configuring the associated sectioned fetch request

- [sortDescriptors](sortdescriptors.md) — The request’s sort descriptors, accessed as value types.
- [nsSortDescriptors](nssortdescriptors.md) — The request’s sort descriptors, accessed as reference types.
- [sectionIdentifier](sectionidentifier.md) — The key path that the system uses to group fetched results into sections.
- [Section](section.md) — A collection of fetched results that share a specified identifier.
