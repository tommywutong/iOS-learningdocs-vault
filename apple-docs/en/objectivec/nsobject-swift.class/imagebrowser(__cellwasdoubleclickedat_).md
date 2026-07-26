---
title: 'imageBrowser(_:cellWasDoubleClickedAt:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/imagebrowser(_:cellwasdoubleclickedat:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowser(_:cellwasdoubleclickedat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/imagebrowser%28_%3Acellwasdoubleclickedat%3A%29.json'
content_hash: 'sha256:60b1217244980184'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# imageBrowser(_:cellWasDoubleClickedAt:)

<sub>Instance Method</sub>

Performs custom tasks when the user double-clicks an item in the image browser view.

<sub>macOS</sub>

```swift
func imageBrowser(_ aBrowser: IKImageBrowserView!, cellWasDoubleClickedAt index: Int)
```

## Parameters

- `aBrowser` — An image browser view.

- `index` — The index of the cell.

## Discussion

This method signals that the user double-clicked an item in the image browser view. You can implement this method if you want to perform custom tasks at that time.
