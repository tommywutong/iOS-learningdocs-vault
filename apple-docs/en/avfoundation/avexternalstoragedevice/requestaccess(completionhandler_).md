---
title: 'requestAccess(completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avexternalstoragedevice/requestaccess(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalstoragedevice/requestaccess(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalstoragedevice/requestaccess%28completionhandler%3A%29.json'
content_hash: 'sha256:ef9b52769c65889f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVExternalStorageDevice](../avexternalstoragedevice.md)

# requestAccess(completionHandler:)

<sub>Type Method</sub>

Requests access to an external storage device on behalf of your app, which can present a dialog to a person on their device’s display.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class func requestAccess(completionHandler handler: @escaping @Sendable (Bool) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class func requestAccess() async -> Bool
```

## Parameters

- `handler` — A closure you provide the system calls to inform your app whether the person authorizes it to access the storage device. The system can call your closure on any dispatch queue and it’s your app’s responsibility to update its UI on the main thread or queue.

## Discussion

Use this method to request access to save image assets to the external storage device. Your app can’t access the external storage device without generating an error until a person gives it permission.

The system only presents the dialog to a person the first time your app calls the method.

> [!note] Note
> The method doesn’t block while the system presents a dialog to a person.
