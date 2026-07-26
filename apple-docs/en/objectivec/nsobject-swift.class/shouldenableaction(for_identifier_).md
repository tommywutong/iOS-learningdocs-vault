---
title: 'shouldEnableAction(for:identifier:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/shouldenableaction(for:identifier:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/shouldenableaction(for:identifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/shouldenableaction%28for%3Aidentifier%3A%29.json'
content_hash: 'sha256:6e953bdea527102e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# shouldEnableAction(for:identifier:)

<sub>Instance Method</sub>

Sent to the delegate to determine whether the action should be enabled.

<sub>macOS</sub>

```swift
func shouldEnableAction(for person: ABPerson!, identifier: String!) -> Bool
```

## Parameters

- `person` — The person on which the action will be taken.

- `identifier` — The unique identifier of the selected value.

## Return Value

[YES](../yes.md) if the action is applicable; otherwise, [NO](../no.md).

## Discussion

If the property returned by [- actionProperty](<actionproperty().md>) is a multivalue property, `identifier` contains the unique identifier of the value selected.
