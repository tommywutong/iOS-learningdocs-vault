---
title: 'imageBrowser(_:itemAt:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/imagebrowser(_:itemat:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowser(_:itemat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/imagebrowser%28_%3Aitemat%3A%29.json'
content_hash: 'sha256:aedc196d5eba5e40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# imageBrowser(_:itemAt:)

<sub>Instance Method</sub>

Returns an object for the item in an image browser view that corresponds to the specified index.

<sub>macOS</sub>

```swift
func imageBrowser(_ aBrowser: IKImageBrowserView!, itemAt index: Int) -> Any!
```

## Parameters

- `aBrowser` — An image browser view.

- `index` — The index of the item you want to retrieve.

## Return Value

An `IKImageBrowserItem` object.

## Discussion

Your data source must implement this method. The returned object must implement the required methods of the IKImageBrowserItem protocol.
