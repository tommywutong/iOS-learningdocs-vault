---
title: imageRepresentationType()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/imagerepresentationtype()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagerepresentationtype()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/imagerepresentationtype%28%29.json'
content_hash: 'sha256:941a597ff4422c2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# imageRepresentationType()

<sub>Instance Method</sub>

Returns the representation type of the image to display.

<sub>macOS</sub>

```swift
func imageRepresentationType() -> String!
```

## Return Value

A string that specifies the image representation type. The string can be any of the constants defined in [Image Representation Types](../../quartz/image-representation-types.md).

## Discussion

Your data source must implement this method.
