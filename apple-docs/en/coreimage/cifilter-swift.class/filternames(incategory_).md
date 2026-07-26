---
title: 'filterNames(inCategory:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifilter-swift.class/filternames(incategory:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/filternames(incategory:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/filternames%28incategory%3A%29.json'
content_hash: 'sha256:6a942d27692b9103'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# filterNames(inCategory:)

<sub>Type Method</sub>

Returns an array of all published filter names in the specified category.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func filterNames(inCategory category: String?) -> [String]
```

## Parameters

- `category` — A string object that specifies one of the filter categories defined in [Filter Category Keys](../filter-category-keys.md).

## Return Value

An array that contains all published names of the filter in a category.

## See Also

### Accessing registered filters

- [+ filterNamesInCategories:](<filternames(incategories_).md>) — Returns an array of all published filter names that match all the specified categories.
