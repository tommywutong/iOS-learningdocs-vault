---
title: 'activityViewController(_:subjectForActivityType:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiactivityitemsource/activityviewcontroller(_:subjectforactivitytype:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityitemsource/activityviewcontroller(_:subjectforactivitytype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityitemsource/activityviewcontroller%28_%3Asubjectforactivitytype%3A%29.json'
content_hash: 'sha256:d10081bd32fc93f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityItemSource](../uiactivityitemsource.md)

# activityViewController(_:subjectForActivityType:)

<sub>Instance Method</sub>

For activities that support a subject field, returns the subject for the item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func activityViewController(_ activityViewController: UIActivityViewController, subjectForActivityType activityType: UIActivity.ActivityType?) -> String
```

## Parameters

- `activityViewController` — The activity view controller object requesting information about the data item.

- `activityType` — The selected activity type; may be `nil`.

## Return Value

A string to use as the contents of the subject field.

## Discussion

When posting an item the service may provide for a separate subject field and data field, such as an email message. Implement this method if you wish to provide a subject field for services that support one.

## See Also

### Providing information about the data items

- [- activityViewController:dataTypeIdentifierForActivityType:](<activityviewcontroller(__datatypeidentifierforactivitytype_).md>) — For items that are provided as data, returns the UTI for the item.
- [- activityViewController:thumbnailImageForActivityType:suggestedSize:](<activityviewcontroller(__thumbnailimageforactivitytype_suggestedsize_).md>) — For activities that support a preview image, returns a thumbnail preview image for the item.
