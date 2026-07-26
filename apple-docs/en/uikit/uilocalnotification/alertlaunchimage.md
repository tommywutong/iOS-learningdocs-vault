---
title: alertLaunchImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（10.0 起废弃）, iPadOS 4.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, watchOS 2.0+（3.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilocalnotification/alertlaunchimage
source_url: 'https://developer.apple.com/documentation/uikit/uilocalnotification/alertlaunchimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilocalnotification/alertlaunchimage.json'
content_hash: 'sha256:51055ac796d18808'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILocalNotification](../uilocalnotification.md)

# alertLaunchImage

<sub>Instance Property</sub>

Identifies the image used as the launch image when the user taps (or slides) the action button (or slider).

> [!warning] Deprecated
> For more information, see [UILocalNotification](../uilocalnotification.md).

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
var alertLaunchImage: String? { get set }
```

## Discussion

The string is a filename of an image file in the app bundle. This image is a launching image specified for a given notification; when the user taps the action button (for example, “View”) or moves the action slider, the image is used in place of the default launching image. If the value of this property is `nil` (the default), the system either uses the previous snapshot, uses the image identified by the `UILaunchImageFile` key in the app’s `Info.plist` file, or falls back to `Default.png`.

The value of this key has the exact same semantics as `UILaunchImageFile`. For more about this key, see the [Information Property List Key Reference](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009247).

## See Also

### Composing the alert

- [alertBody](alertbody.md) — The message displayed in the notification alert. _(deprecated)_
- [alertAction](alertaction.md) — The title of the action button or slider. _(deprecated)_
- [alertTitle](alerttitle.md) — A short description of the reason for the alert. _(deprecated)_
- [hasAction](hasaction.md) — A Boolean value that controls whether the notification shows or hides the alert action. _(deprecated)_
- [category](category.md) — The name of a group of actions to display in the alert. _(deprecated)_
