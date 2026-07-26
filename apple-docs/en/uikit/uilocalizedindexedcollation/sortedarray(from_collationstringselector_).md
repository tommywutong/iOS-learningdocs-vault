---
title: 'sortedArray(from:collationStringSelector:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uilocalizedindexedcollation/sortedarray(from:collationstringselector:)'
source_url: 'https://developer.apple.com/documentation/uikit/uilocalizedindexedcollation/sortedarray(from:collationstringselector:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilocalizedindexedcollation/sortedarray%28from%3Acollationstringselector%3A%29.json'
content_hash: 'sha256:a66f61a3a2327bf2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILocalizedIndexedCollation](../uilocalizedindexedcollation.md)

# sortedArray(from:collationStringSelector:)

<sub>Instance Method</sub>

Sorts the objects within a section by their localized titles.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func sortedArray(from array: [Any], collationStringSelector selector: Selector) -> [Any]
```

## Parameters

- `array` — An array containing the model objects for a section.

- `selector` — The selector of a method implemented by the objects in `array` that returns the string to use for sorting the objects. The method represented by the selector must take no arguments and return an [NSString](../../foundation/nsstring.md) object. For example, you might specify the selector for a name property of the object.

## Return Value

A new array containing the sorted items from the original `array` parameter.

## Discussion

The table-view controller creates the array of objects for a section (`array`) as part of iterating through its model objects with calls to the [- sectionForObject:collationStringSelector:](<section(for_collationstringselector_).md>) method. This method should be called on each local section array.

## See Also

### Preparing the sections and section indexes

- [- sectionForObject:collationStringSelector:](<section(for_collationstringselector_).md>) — Returns an integer identifying the section in which a model object belongs.
