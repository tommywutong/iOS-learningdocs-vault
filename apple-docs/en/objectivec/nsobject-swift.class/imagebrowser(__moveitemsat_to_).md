---
title: 'imageBrowser(_:moveItemsAt:to:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/imagebrowser(_:moveitemsat:to:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowser(_:moveitemsat:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/imagebrowser%28_%3Amoveitemsat%3Ato%3A%29.json'
content_hash: 'sha256:cb0cc25beb07110a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# imageBrowser(_:moveItemsAt:to:)

<sub>Instance Method</sub>

Signals that the specified items should be moved to the specified destination.

<sub>macOS</sub>

```swift
func imageBrowser(_ aBrowser: IKImageBrowserView!, moveItemsAt indexes: IndexSet!, to destinationIndex: Int) -> Bool
```

## Parameters

- `aBrowser` — An image browser view.

- `indexes` — The indexes of the items that should be reordered.

- `destinationIndex` — The starting index of the destination the items should be moved to.

## Return Value

[YES](../yes.md) if successful; [NO](../no.md) otherwise.

## Discussion

This method is optional. It is invoked by the image browser view after  Image Kit determines  that a reordering operation should be applied. The data source should update itself by reordering its elements.

## See Also

### Related Documentation

- [setAllowsReordering(_:)](<../../quartz/ikimagebrowserview/setallowsreordering(__).md>) — Controls whether the user can reorder items.
