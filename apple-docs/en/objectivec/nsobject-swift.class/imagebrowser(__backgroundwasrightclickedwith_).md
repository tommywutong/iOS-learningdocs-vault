---
title: 'imageBrowser(_:backgroundWasRightClickedWith:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/imagebrowser(_:backgroundwasrightclickedwith:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowser(_:backgroundwasrightclickedwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/imagebrowser%28_%3Abackgroundwasrightclickedwith%3A%29.json'
content_hash: 'sha256:470c58cf3581ee1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# imageBrowser(_:backgroundWasRightClickedWith:)

<sub>Instance Method</sub>

Performs custom tasks when the user right-clicks the image browser view background.

<sub>macOS</sub>

```swift
func imageBrowser(_ aBrowser: IKImageBrowserView!, backgroundWasRightClickedWith event: NSEvent!)
```

## Parameters

- `aBrowser` — An image browser view.

- `event` — The event that invoked the method.

## Discussion

This method signals  that the user either right-clicked the background or left-clicked it with the Alt key pressed. You can implement this method if you want to perform custom tasks at that time.
