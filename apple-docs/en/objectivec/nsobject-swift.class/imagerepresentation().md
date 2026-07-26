---
title: imageRepresentation()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/imagerepresentation()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagerepresentation()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/imagerepresentation%28%29.json'
content_hash: 'sha256:54f2d0acd95339cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# imageRepresentation()

<sub>Instance Method</sub>

Returns the image to display.

<sub>macOS</sub>

```swift
func imageRepresentation() -> Any!
```

## Return Value

The image to display; can return `nil` if the item has no image to display.

## Discussion

Your data source must implement this method. This method  is called frequently, so the receiver should cache the returned instance.
