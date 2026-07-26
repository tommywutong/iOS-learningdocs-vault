---
title: 'imageBrowser(_:groupAt:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/imagebrowser(_:groupat:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowser(_:groupat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/imagebrowser%28_%3Agroupat%3A%29.json'
content_hash: 'sha256:7c386df014d42d7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# imageBrowser(_:groupAt:)

<sub>Instance Method</sub>

Returns the group at the specified index.

<sub>macOS</sub>

```swift
func imageBrowser(_ aBrowser: IKImageBrowserView!, groupAt index: Int) -> [AnyHashable : Any]!
```

## Parameters

- `aBrowser` — An image browser view.

- `index` — The index of the group you want to retrieve.

## Return Value

A dictionary that defines the group. The keys in this dictionary can be any of the following constants: [IKImageBrowserGroupStyleKey](../../quartz/ikimagebrowsergroupstylekey.md), [IKImageBrowserGroupBackgroundColorKey](../../quartz/ikimagebrowsergroupbackgroundcolorkey.md), [IKImageBrowserGroupTitleKey](../../quartz/ikimagebrowsergrouptitlekey.md), and [IKImageBrowserGroupRangeKey](../../quartz/ikimagebrowsergrouprangekey.md). For more information on these constants, see [IKImageBrowserView](../../quartz/ikimagebrowserview.md).

## Discussion

This method is optional.
