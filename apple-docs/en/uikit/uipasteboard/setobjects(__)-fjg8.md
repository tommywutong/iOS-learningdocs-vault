---
title: 'setObjects(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipasteboard/setobjects(_:)-fjg8'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/setobjects(_:)-fjg8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/setobjects%28_%3A%29-fjg8.json'
content_hash: 'sha256:9b626b836e308f01'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# setObjects(_:)

<sub>Instance Method</sub>

Sets an array of item providers for the pasteboard, based on a specified array of objects.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setObjects<T>(_ objects: [T]) where T : _ObjectiveCBridgeable, T._ObjectiveCType : NSItemProviderWriting
```

## Parameters

- `objects` — An array of item providers for the pasteboard.

## See Also

### Getting and setting item providers

- [itemProviders](itemproviders.md) — An array of item providers for the pasteboard.
- [- setItemProviders:localOnly:expirationDate:](<setitemproviders(__localonly_expirationdate_).md>) — Sets and configures an explicit array of item providers for the pasteboard.
- [- setObjects:](<setobjects(__)-lljo.md>) — Sets an array of item providers for the pasteboard, based on a specified array of objects.
- [- setObjects:localOnly:expirationDate:](<setobjects(__localonly_expirationdate_)-3h3iz.md>) — Sets and configures an array of item providers for the pasteboard, based on a specified array of objects.
- [setObjects(_:localOnly:expirationDate:)](<setobjects(__localonly_expirationdate_)-26u8o.md>) — Sets and configures an array of item providers for the pasteboard, based on a specified array of objects.
