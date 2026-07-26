---
title: sectionIndexTitles
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchedresultscontroller/sectionindextitles
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/sectionindextitles'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchedresultscontroller/sectionindextitles.json'
content_hash: 'sha256:b661b87974fa56e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchedResultsController](../nsfetchedresultscontroller.md)

# sectionIndexTitles

<sub>Instance Property</sub>

The array of section index titles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sectionIndexTitles: [String] { get }
```

## Discussion

The default implementation returns the array created by calling [- sectionIndexTitleForSectionName:](<sectionindextitle(forsectionname_).md>) on all the known sections. You should override this method if you want to return a different array for the section index.

### Special Considerations

You only need this method if you use a section index.

## See Also

### Configuring Section Information

- [- sectionIndexTitleForSectionName:](<sectionindextitle(forsectionname_).md>) — Returns the corresponding section index entry for a given section name.
