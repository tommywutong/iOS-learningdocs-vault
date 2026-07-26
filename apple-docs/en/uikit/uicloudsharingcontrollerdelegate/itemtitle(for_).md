---
title: 'itemTitle(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicloudsharingcontrollerdelegate/itemtitle(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicloudsharingcontrollerdelegate/itemtitle(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicloudsharingcontrollerdelegate/itemtitle%28for%3A%29.json'
content_hash: 'sha256:b7de04c69c4c0b43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICloudSharingControllerDelegate](../uicloudsharingcontrollerdelegate.md)

# itemTitle(for:)

<sub>Instance Method</sub>

Asks the delegate for the title to display on the invitation screen.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func itemTitle(for csc: UICloudSharingController) -> String?
```

## Discussion

Implement this method to provide a meaningful title to the [UICloudSharingController](../uicloudsharingcontroller.md) invitation screen.

[- itemTitleForCloudSharingController:](<itemtitle(for_).md>) is called only when creating a new share. For an existing share, the title is retrieved from the share using the [CKShareTitleKey](../../cloudkit/cksharetitlekey-9yavd.md) key, which is set when a new share is saved.

**Swift**

```swift
func itemTitle(for csc: UICloudSharingController) -> String? {
  return "Untitled"
}
```

**Objective-C**

```objc
- (nullable NSString *)itemTitleForCloudSharingController:(UICloudSharingController *)csc
{
  return @"Untitled";
}
```

## See Also

### Configuring the view controller

- [- itemTypeForCloudSharingController:](<itemtype(for_).md>) — Asks the delegate for the Uniform Type Identifier (UTI) of the item.
- [- itemThumbnailDataForCloudSharingController:](<itemthumbnaildata(for_).md>) — Asks the delegate for the thumbnail image data to display on the invitation.
