---
title: 'imageBrowser(_:writeItemsAt:to:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/imagebrowser(_:writeitemsat:to:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowser(_:writeitemsat:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/imagebrowser%28_%3Awriteitemsat%3Ato%3A%29.json'
content_hash: 'sha256:77cbd511d4f11ad0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# imageBrowser(_:writeItemsAt:to:)

<sub>Instance Method</sub>

Signals that a drag should begin.

<sub>macOS</sub>

```swift
func imageBrowser(_ aBrowser: IKImageBrowserView!, writeItemsAt itemIndexes: IndexSet!, to pasteboard: NSPasteboard!) -> Int
```

## Parameters

- `aBrowser` — An image browser view.

- `itemIndexes` — The indexes of the items that should be dragged.

- `pasteboard` — The pasteboard to copy the items to.

## Return Value

The number of items written to the pasteboard.

## Discussion

This method is optional. It is invoked after Image Kit determines that a drag should begin, but before the drag has been started.
