---
title: 'sectionIndexTitle(forSectionName:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsfetchedresultscontroller/sectionindextitle(forsectionname:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/sectionindextitle(forsectionname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchedresultscontroller/sectionindextitle%28forsectionname%3A%29.json'
content_hash: 'sha256:8b1eb0afc3242aa0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchedResultsController](../nsfetchedresultscontroller.md)

# sectionIndexTitle(forSectionName:)

<sub>Instance Method</sub>

Returns the corresponding section index entry for a given section name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sectionIndexTitle(forSectionName sectionName: String) -> String?
```

## Parameters

- `sectionName` — The name of a section.

## Return Value

The section index entry corresponding to the section with name `sectionName`.

## Discussion

The default implementation returns the capitalized first letter of the section name.

You should override this method if you need a different way to convert from a section name to its name in the section index.

### Special Considerations

You only need this method if you use a section index.

## See Also

### Configuring Section Information

- [sectionIndexTitles](sectionindextitles.md) — The array of section index titles.
