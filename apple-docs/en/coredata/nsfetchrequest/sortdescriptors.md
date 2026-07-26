---
title: sortDescriptors
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchrequest/sortdescriptors
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchrequest/sortdescriptors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchrequest/sortdescriptors.json'
content_hash: 'sha256:a930f8eb382ad813'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchRequest](../nsfetchrequest.md)

# sortDescriptors

<sub>Instance Property</sub>

The sort descriptors of the fetch request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sortDescriptors: [NSSortDescriptor]? { get set }
```

## Discussion

The sort descriptors specify how the objects returned when the [NSFetchRequest](../nsfetchrequest.md) is issued should be ordered—for example, by last name and then by first name. The sort descriptors are applied in the order in which they appear in the `sortDescriptors` array (serially in lowest-array-index-first order).

A value of `nil` is treated as no sort descriptors.
