---
title: 'indexPathForElement(withModelIdentifier:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidatasourcemodelassociation/indexpathforelement(withmodelidentifier:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidatasourcemodelassociation/indexpathforelement(withmodelidentifier:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatasourcemodelassociation/indexpathforelement%28withmodelidentifier%3Ain%3A%29.json'
content_hash: 'sha256:390dd3185114ec28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDataSourceModelAssociation](../uidatasourcemodelassociation.md)

# indexPathForElement(withModelIdentifier:in:)

<sub>Instance Method</sub>

Returns the current index of the data object with the specified identifier.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func indexPathForElement(withModelIdentifier identifier: String, in view: UIView) -> IndexPath?
```

## Parameters

- `identifier` — The identifier for the requested data object. Use this identifier to locate the matching object in your data source object. This is the same string that your app’s [- modelIdentifierForElementAtIndexPath:inView:](<modelidentifierforelement(at_in_).md>) method returned when encoding the data originally.

- `view` — The view into which the object is being inserted.

## Return Value

The current index of the object whose data matches the value in `identifier`, or `nil` if the object was not found.

## Discussion

During state restoration, `view` can call this method to locate objects that aren’t where they were expected to be. This can happen if the number of objects in the table isn’t the same as during the previous launch cycle. The view uses the information to ensure that the rows with the same data are once again selected or scrolled into view, even if those rows are in a different location now.

## See Also

### Locating the data

- [- modelIdentifierForElementAtIndexPath:inView:](<modelidentifierforelement(at_in_).md>) — Returns the string that uniquely identifies the data at the specified location in the view.
