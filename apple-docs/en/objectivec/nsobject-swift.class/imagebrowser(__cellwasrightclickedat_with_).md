---
title: 'imageBrowser(_:cellWasRightClickedAt:with:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/imagebrowser(_:cellwasrightclickedat:with:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowser(_:cellwasrightclickedat:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/imagebrowser%28_%3Acellwasrightclickedat%3Awith%3A%29.json'
content_hash: 'sha256:047123083607d77e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# imageBrowser(_:cellWasRightClickedAt:with:)

<sub>Instance Method</sub>

Performs custom tasks when the user right-clicks an item in the image browser view.

<sub>macOS</sub>

```swift
func imageBrowser(_ aBrowser: IKImageBrowserView!, cellWasRightClickedAt index: Int, with event: NSEvent!)
```

## Parameters

- `aBrowser` — An image browser view.

- `index` — The index of the cell.

- `event` — The event that invoked the method.

## Discussion

This method signals that the user either right-clicked an item in the browser or left-clicked the item with the Alt key pressed. You can implement this method if you want to perform custom tasks at that time.
