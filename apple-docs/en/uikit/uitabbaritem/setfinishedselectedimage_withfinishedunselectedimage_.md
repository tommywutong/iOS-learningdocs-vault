---
title: 'setFinishedSelectedImage:withFinishedUnselectedImage:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+（7.0 起废弃）, iPadOS 5.0+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uitabbaritem/setfinishedselectedimage:withfinishedunselectedimage:'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbaritem/setfinishedselectedimage:withfinishedunselectedimage:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbaritem/setfinishedselectedimage%3Awithfinishedunselectedimage%3A.json'
content_hash: 'sha256:6d8f94a3c2708cf2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarItem](../uitabbaritem.md)

# setFinishedSelectedImage:withFinishedUnselectedImage:

<sub>Instance Method</sub>

Sets the finished selected and unselected images.

> [!warning] Deprecated
> Use [image](../uibaritem/image.md) and [selectedImage](selectedimage.md) with [UIImageRenderingModeAlwaysOriginal](../uiimage/renderingmode-swift.enum/alwaysoriginal.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) setFinishedSelectedImage:(UIImage *) selectedImage withFinishedUnselectedImage:(UIImage *) unselectedImage;
```

## Parameters

- `selectedImage` — The finished selected image.

- `unselectedImage` — The finished unselected image.

## See Also

### Deprecated

- [finishedSelectedImage](finishedselectedimage.md) — Returns the finished selected image. _(deprecated)_
- [finishedUnselectedImage](finishedunselectedimage.md) — Returns the finished unselected image. _(deprecated)_
