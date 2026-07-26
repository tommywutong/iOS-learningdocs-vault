---
title: imageVersion()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/imageversion()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imageversion()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/imageversion%28%29.json'
content_hash: 'sha256:e6d73a9fb84f0794'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# imageVersion()

<sub>Instance Method</sub>

Returns the version of the item.

<sub>macOS</sub>

```swift
func imageVersion() -> Int
```

## Return Value

The version of the item.

## Discussion

This method is optional. The receiver can return a new version to let the image browser know that it should not use its cache for the item.
