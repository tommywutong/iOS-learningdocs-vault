---
title: 'imageBrowser(_:removeItemsAt:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/imagebrowser(_:removeitemsat:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowser(_:removeitemsat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/imagebrowser%28_%3Aremoveitemsat%3A%29.json'
content_hash: 'sha256:7a2608d5a132073a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# imageBrowser(_:removeItemsAt:)

<sub>Instance Method</sub>

Signals that a remove operation should be applied to the specified items.

<sub>macOS</sub>

```swift
func imageBrowser(_ aBrowser: IKImageBrowserView!, removeItemsAt indexes: IndexSet!)
```

## Parameters

- `aBrowser` — An image browser view.

- `indexes` — The indexes of the items that should be removed.

## Discussion

This method is optional. It is invoked by the image browser after  Image Kit determines  that a remove operation should be applied. In response, the data source should update itself by removing the specified items.
