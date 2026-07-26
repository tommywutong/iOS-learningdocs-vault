---
title: 'itemType(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicloudsharingcontrollerdelegate/itemtype(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicloudsharingcontrollerdelegate/itemtype(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicloudsharingcontrollerdelegate/itemtype%28for%3A%29.json'
content_hash: 'sha256:fd80d9ffb2a19da2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICloudSharingControllerDelegate](../uicloudsharingcontrollerdelegate.md)

# itemType(for:)

<sub>Instance Method</sub>

Asks the delegate for the Uniform Type Identifier (UTI) of the item.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func itemType(for csc: UICloudSharingController) -> String?
```

## Discussion

[UICloudSharingController](../uicloudsharingcontroller.md) uses the UTI to determine if the shared item is a special type. This allows text presented by the controller to refer to the item using descriptive wording. For example, if the shared item is a presentation and `kUTTypePresentation` is returned, the screens refer to the shared item as a _presentation_. Likewise, if the shared item is a document and `kUTTypeContent` is returned, the screens refer to the item as a _document_. And when `kUTTypeSpreadsheet` is returned, the screens refer to the item as a _spreadsheet_.

For types unique to your app, return `nil` or do not implement this method.

**Swift**

```swift
func itemType(for csc: UICloudSharingController) -> String? {
  return kUTTypePNG as String // Add "import MobileCoreServices" to use UTI constants.
}
```

**Objective-C**

```objc
- (nullable NSString *)itemTypeForCloudSharingController:(UICloudSharingController *)csc
{
  return (NSString*)kUTTypePNG; // Add #import <MobileCoreServices/MobileCoreServices.h> to use UTI constants.
}
```

## See Also

### Configuring the view controller

- [- itemTitleForCloudSharingController:](<itemtitle(for_).md>) — Asks the delegate for the title to display on the invitation screen.
- [- itemThumbnailDataForCloudSharingController:](<itemthumbnaildata(for_).md>) — Asks the delegate for the thumbnail image data to display on the invitation.
