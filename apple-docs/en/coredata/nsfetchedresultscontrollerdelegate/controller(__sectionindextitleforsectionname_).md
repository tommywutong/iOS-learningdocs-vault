---
title: 'controller(_:sectionIndexTitleForSectionName:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsfetchedresultscontrollerdelegate/controller(_:sectionindextitleforsectionname:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchedresultscontrollerdelegate/controller(_:sectionindextitleforsectionname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchedresultscontrollerdelegate/controller%28_%3Asectionindextitleforsectionname%3A%29.json'
content_hash: 'sha256:5263b30b1a694e4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchedResultsControllerDelegate](../nsfetchedresultscontrollerdelegate.md)

# controller(_:sectionIndexTitleForSectionName:)

<sub>Instance Method</sub>

Returns the name for a given section.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func controller(_ controller: NSFetchedResultsController<any NSFetchRequestResult>, sectionIndexTitleForSectionName sectionName: String) -> String?
```

## Parameters

- `controller` — The fetched results controller that sent the message.

- `sectionName` — The default name of the section.

## Return Value

The string to use as the name for the specified section.

## Discussion

This method does not enable change tracking. It is only needed if a section index is used.

If the delegate doesn’t implement this method, the default implementation returns the capitalized first letter of the section name (see [- sectionIndexTitleForSectionName:](<../nsfetchedresultscontroller/sectionindextitle(forsectionname_).md>) in `NSFetchedResultsController`).
