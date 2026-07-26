---
title: 'activityViewController(_:thumbnailImageForActivityType:suggestedSize:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiactivityitemsource/activityviewcontroller(_:thumbnailimageforactivitytype:suggestedsize:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityitemsource/activityviewcontroller(_:thumbnailimageforactivitytype:suggestedsize:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityitemsource/activityviewcontroller%28_%3Athumbnailimageforactivitytype%3Asuggestedsize%3A%29.json'
content_hash: 'sha256:b821b87af7bb1ec1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityItemSource](../uiactivityitemsource.md)

# activityViewController(_:thumbnailImageForActivityType:suggestedSize:)

<sub>Instance Method</sub>

For activities that support a preview image, returns a thumbnail preview image for the item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func activityViewController(_ activityViewController: UIActivityViewController, thumbnailImageForActivityType activityType: UIActivity.ActivityType?, suggestedSize size: CGSize) -> UIImage?
```

## Parameters

- `activityViewController` — The activity view controller object requesting information about the data item.

- `activityType` — The selected activity type.

- `size` — The suggested size for the thumbnail image, in points. You should provide an image using the appropriate [scale](../uiscreen/scale.md) for the screen. Images provided at the suggested size will result in the best experience.

## Return Value

The image to use as a preview for the item.

## See Also

### Providing information about the data items

- [- activityViewController:subjectForActivityType:](<activityviewcontroller(__subjectforactivitytype_).md>) — For activities that support a subject field, returns the subject for the item.
- [- activityViewController:dataTypeIdentifierForActivityType:](<activityviewcontroller(__datatypeidentifierforactivitytype_).md>) — For items that are provided as data, returns the UTI for the item.
