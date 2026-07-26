---
title: 'modelIdentifierForElement(at:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidatasourcemodelassociation/modelidentifierforelement(at:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidatasourcemodelassociation/modelidentifierforelement(at:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatasourcemodelassociation/modelidentifierforelement%28at%3Ain%3A%29.json'
content_hash: 'sha256:c4d6d87ac7840ef7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDataSourceModelAssociation](../uidatasourcemodelassociation.md)

# modelIdentifierForElement(at:in:)

<sub>Instance Method</sub>

Returns the string that uniquely identifies the data at the specified location in the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func modelIdentifierForElement(at idx: IndexPath, in view: UIView) -> String?
```

## Parameters

- `idx` — The index path to the requested data object.

- `view` — The view that contains the data object.

## Return Value

A string that uniquely identifies the data object.

## Discussion

Use the provided information to locate the requested data object. From that object, extract a string that can be used later to identify the same piece of data again. The string you return must not be based on transient information, such as the pointer to the current object in memory; it must instead be tied to the underlying data. In fact, if two different in-memory objects represent the same piece of data in your app, they must both return the same model identifier string.

## See Also

### Locating the data

- [- indexPathForElementWithModelIdentifier:inView:](<indexpathforelement(withmodelidentifier_in_).md>) — Returns the current index of the data object with the specified identifier.
