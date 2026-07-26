---
title: 'imageBrowserSelectionDidChange(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/imagebrowserselectiondidchange(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowserselectiondidchange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/imagebrowserselectiondidchange%28_%3A%29.json'
content_hash: 'sha256:d5777776daf14110'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# imageBrowserSelectionDidChange(_:)

<sub>Instance Method</sub>

Performs custom tasks when the selection changes.

<sub>macOS</sub>

```swift
func imageBrowserSelectionDidChange(_ aBrowser: IKImageBrowserView!)
```

## Parameters

- `aBrowser` — An image browser view.

## Discussion

This method signals that the user changes the selection in the image browser view. You can implement this method if you want to perform custom tasks at that time.
