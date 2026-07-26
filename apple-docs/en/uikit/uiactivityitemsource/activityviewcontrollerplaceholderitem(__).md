---
title: 'activityViewControllerPlaceholderItem(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiactivityitemsource/activityviewcontrollerplaceholderitem(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityitemsource/activityviewcontrollerplaceholderitem(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityitemsource/activityviewcontrollerplaceholderitem%28_%3A%29.json'
content_hash: 'sha256:6c70a1e95e04e8ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityItemSource](../uiactivityitemsource.md)

# activityViewControllerPlaceholderItem(_:)

<sub>Instance Method</sub>

Returns the placeholder object for the data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func activityViewControllerPlaceholderItem(_ activityViewController: UIActivityViewController) -> Any
```

## Parameters

- `activityViewController` — The activity view controller object requesting the placeholder item.

## Return Value

An object to use as a placeholder for the actual data.

## Discussion

This method returns an object that can be used as a placeholder for the real data. Placeholder objects don’t have to contain any real data but should be configured as closely as possible to the actual data object you intend to provide. In general the actual value should match in type but it’s possible to return a different type of data for [- activityViewController:itemForActivityType:](<activityviewcontroller(__itemforactivitytype_).md>). It should be one that the activity can handle otherwise you may get an activity with empty content. For example, the placeholder could be a [UIImage](../uiimage.md) object but the actual value could be an [NSData](../../foundation/nsdata.md) object with PDF information.

## See Also

### Getting the data items

- [- activityViewController:itemForActivityType:](<activityviewcontroller(__itemforactivitytype_).md>) — Returns the data object to be acted upon.
