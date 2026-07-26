---
title: 'numberOfItems(inImageBrowser:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/numberofitems(inimagebrowser:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/numberofitems(inimagebrowser:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/numberofitems%28inimagebrowser%3A%29.json'
content_hash: 'sha256:f2756fb6f209929e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# numberOfItems(inImageBrowser:)

<sub>Instance Method</sub>

Returns the number of records managed by the data source object.

<sub>macOS</sub>

```swift
func numberOfItems(inImageBrowser aBrowser: IKImageBrowserView!) -> Int
```

## Parameters

- `aBrowser` — An image browser view.

## Return Value

The number of records managed by the image browser view.

## Discussion

Your data source must implement this method. An  [IKImageView](../../quartz/ikimageview.md) object uses this method to determine how many cells it should create and display.
