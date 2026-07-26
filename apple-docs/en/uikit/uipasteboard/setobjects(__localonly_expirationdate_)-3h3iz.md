---
title: 'setObjects(_:localOnly:expirationDate:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipasteboard/setobjects(_:localonly:expirationdate:)-3h3iz'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/setobjects(_:localonly:expirationdate:)-3h3iz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/setobjects%28_%3Alocalonly%3Aexpirationdate%3A%29-3h3iz.json'
content_hash: 'sha256:3d7c8d5ce14d283c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# setObjects(_:localOnly:expirationDate:)

<sub>Instance Method</sub>

Sets and configures an array of item providers for the pasteboard, based on a specified array of objects.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setObjects(_ objects: [any NSItemProviderWriting], localOnly: Bool, expirationDate: Date?)
```

## Parameters

- `objects` — An array of item providers for the pasteboard.

- `localOnly` — If [false](../../swift/false.md), the pasteboard items are available to other devices through the Handoff feature; if [true](../../swift/true.md), the pasteboard items are only available to the local device.

- `expirationDate` — An [NSDate](../../foundation/nsdate.md) value that specifies the time and date that you want the system to remove the pasteboard items from the pasteboard.

## See Also

### Getting and setting item providers

- [itemProviders](itemproviders.md) — An array of item providers for the pasteboard.
- [- setItemProviders:localOnly:expirationDate:](<setitemproviders(__localonly_expirationdate_).md>) — Sets and configures an explicit array of item providers for the pasteboard.
- [- setObjects:](<setobjects(__)-lljo.md>) — Sets an array of item providers for the pasteboard, based on a specified array of objects.
- [setObjects(_:)](<setobjects(__)-fjg8.md>) — Sets an array of item providers for the pasteboard, based on a specified array of objects.
- [setObjects(_:localOnly:expirationDate:)](<setobjects(__localonly_expirationdate_)-26u8o.md>) — Sets and configures an array of item providers for the pasteboard, based on a specified array of objects.
