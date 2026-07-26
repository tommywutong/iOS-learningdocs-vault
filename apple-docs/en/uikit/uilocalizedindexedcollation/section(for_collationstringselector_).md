---
title: 'section(for:collationStringSelector:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uilocalizedindexedcollation/section(for:collationstringselector:)'
source_url: 'https://developer.apple.com/documentation/uikit/uilocalizedindexedcollation/section(for:collationstringselector:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilocalizedindexedcollation/section%28for%3Acollationstringselector%3A%29.json'
content_hash: 'sha256:d421df6655e46d5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILocalizedIndexedCollation](../uilocalizedindexedcollation.md)

# section(for:collationStringSelector:)

<sub>Instance Method</sub>

Returns an integer identifying the section in which a model object belongs.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func section(for object: Any, collationStringSelector selector: Selector) -> Int
```

## Parameters

- `object` — A model object of the application that is part of the data model for the table view.

- `selector` — The selector of a method of `object` that returns the string to use for sorting. The method represented by the selection must take no arguments and return an [NSString](../../foundation/nsstring.md) object. For example, you might specify the selector for a `name` property of the object.

## Return Value

An integer that identifies the section in which the model object belongs. The numbers returned indicate a sequential ordering.

## Discussion

The table-view controller should iterate through all model objects for the table view and call this method for each object. If the application provides a `Localizable.strings` file for the current language preference, the indexed-collation object localizes each string returned by the method identified by `selector`. It uses this localized name when collating titles. The controller should use the returned integer to identify a local “section” array in which it should insert `object`.

## See Also

### Preparing the sections and section indexes

- [- sortedArrayFromArray:collationStringSelector:](<sortedarray(from_collationstringselector_).md>) — Sorts the objects within a section by their localized titles.
