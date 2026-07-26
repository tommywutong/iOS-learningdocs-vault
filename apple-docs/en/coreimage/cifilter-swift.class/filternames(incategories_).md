---
title: 'filterNames(inCategories:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifilter-swift.class/filternames(incategories:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/filternames(incategories:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/filternames%28incategories%3A%29.json'
content_hash: 'sha256:84734dafb39f788a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# filterNames(inCategories:)

<sub>Type Method</sub>

Returns an array of all published filter names that match all the specified categories.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func filterNames(inCategories categories: [String]?) -> [String]
```

## Parameters

- `categories` — One or more of the filter category keys defined in [Filter Category Keys](../filter-category-keys.md). Pass `nil` to get all filters in all categories.

## Return Value

An array that contains all published filter names that match all the categories specified by the `categories` argument.

## Discussion

When you pass more than one filter category, this method returns the intersection of the filters in the categories. For example, if you pass the categories [kCICategoryBuiltIn](../kcicategorybuiltin.md)  and [kCICategoryColorAdjustment](../kcicategorycoloradjustment.md), you obtain all the filters that are members of both the built-in and color adjustment categories. But if you pass in `kCICategoryGenerator` and [kCICategoryStylize](../kcicategorystylize.md), you will not get any filters returned to you because there are no filters that are members of both the generator and stylize categories. If you want to obtain all stylize and generator filters, you must call the `filterNamesInCategories:` method for each category separately and then merge the results.

## See Also

### Accessing registered filters

- [+ filterNamesInCategory:](<filternames(incategory_).md>) — Returns an array of all published filter names in the specified category.
