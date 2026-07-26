---
title: 'activityViewController(_:itemForActivityType:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiactivityitemsource/activityviewcontroller(_:itemforactivitytype:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityitemsource/activityviewcontroller(_:itemforactivitytype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityitemsource/activityviewcontroller%28_%3Aitemforactivitytype%3A%29.json'
content_hash: 'sha256:be4a43b0bd33b9cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityItemSource](../uiactivityitemsource.md)

# activityViewController(_:itemForActivityType:)

<sub>Instance Method</sub>

Returns the data object to be acted upon.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func activityViewController(_ activityViewController: UIActivityViewController, itemForActivityType activityType: UIActivity.ActivityType?) -> Any?
```

## Parameters

- `activityViewController` — The activity view controller object requesting the data item.

- `activityType` — The type of activity to be performed with the data object. You can use this string to decide how best to prepare the data object.

## Return Value

The final data object to be acted on. May be `nil` if multiple items were registered for a single activity type, so long as one of the items returns an actual value.

## Discussion

This method returns the actual data object to be acted on by an activity object. Your implementation of this method should create or generate the data object and return it as quickly as possible.

## See Also

### Getting the data items

- [- activityViewControllerPlaceholderItem:](<activityviewcontrollerplaceholderitem(__).md>) — Returns the placeholder object for the data.
