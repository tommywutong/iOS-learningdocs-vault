---
title: 'title(for:identifier:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/title(for:identifier:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/title(for:identifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/title%28for%3Aidentifier%3A%29.json'
content_hash: 'sha256:569d1738de213386'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# title(for:identifier:)

<sub>Instance Method</sub>

Sent to the delegate to request the title of the menu item for the action.

<sub>macOS</sub>

```swift
func title(for person: ABPerson!, identifier: String!) -> String!
```

## Parameters

- `person` — The person on which the action will be taken.

- `identifier` — The unique identifier of the value for which the menu item will be displayed.

## Return Value

The title of the menu item for the action.

## Discussion

If the property returned by [- actionProperty](<actionproperty().md>) is a multivalue property, `identifier` contains the unique identifier of the value selected.
