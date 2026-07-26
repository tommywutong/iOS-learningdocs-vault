---
title: 'itemThumbnailData(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicloudsharingcontrollerdelegate/itemthumbnaildata(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicloudsharingcontrollerdelegate/itemthumbnaildata(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicloudsharingcontrollerdelegate/itemthumbnaildata%28for%3A%29.json'
content_hash: 'sha256:a526d6f239f6bcc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICloudSharingControllerDelegate](../uicloudsharingcontrollerdelegate.md)

# itemThumbnailData(for:)

<sub>Instance Method</sub>

Asks the delegate for the thumbnail image data to display on the invitation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func itemThumbnailData(for csc: UICloudSharingController) -> Data?
```

## Discussion

Implement this method to return image data representing the shared recording. Returning `nil` tells the [UICloudSharingController](../uicloudsharingcontroller.md) instance to display the generic image. Not implementing this method is the same as returning `nil`.

[- itemThumbnailDataForCloudSharingController:](<itemthumbnaildata(for_).md>) is called only when creating a new share. For an existing share, the thumbnail image is retrieved from the share using the [CKShareThumbnailImageDataKey](../../cloudkit/cksharethumbnailimagedatakey-1rxdx.md) key.

The following code shows an example of retrieving the image data from a data set stored in an asset catalog found in the main bundle.

```swift
- (nullable NSData *)itemThumbnailDataForCloudSharingController:(UICloudSharingController *)csc
{  
  NSDataAsset *icon = [[NSDataAsset alloc] initWithName:@"thumbnail"];
  return [icon data];
}
```

## See Also

### Configuring the view controller

- [- itemTitleForCloudSharingController:](<itemtitle(for_).md>) — Asks the delegate for the title to display on the invitation screen.
- [- itemTypeForCloudSharingController:](<itemtype(for_).md>) — Asks the delegate for the Uniform Type Identifier (UTI) of the item.
