---
title: imageUID()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/imageuid()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imageuid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/imageuid%28%29.json'
content_hash: 'sha256:576914081998a548'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# imageUID()

<sub>Instance Method</sub>

Returns a unique string that identifies the data source item.

<sub>macOS</sub>

```swift
func imageUID() -> String!
```

## Return Value

The string that identifies the data source item

## Discussion

Your data source must implement this method. The image browser view uses this identifier to associate the data source item and  its cache.
