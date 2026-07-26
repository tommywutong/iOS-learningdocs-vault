---
title: 'performAction(for:identifier:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/performaction(for:identifier:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/performaction(for:identifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/performaction%28for%3Aidentifier%3A%29.json'
content_hash: 'sha256:515eddfb3e2c9c3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# performAction(for:identifier:)

<sub>Instance Method</sub>

Sent to the delegate to perform the action.

<sub>macOS</sub>

```swift
func performAction(for person: ABPerson!, identifier: String!)
```

## Parameters

- `person` — The person on which the action will be taken.

- `identifier` — The unique identifier of the selected value.

## Discussion

If the property returned by [- actionProperty](<actionproperty().md>) is a multivalue property, `identifier` contains the unique identifier of the value selected. The person being displayed in the Address Book application’s card view when the rollover menu is accesses is passed as `person`.
