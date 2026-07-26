---
title: ALAssetsLibraryChangedNotification
framework: Assets Library
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/assetslibrary/alassetslibrarychangednotification
source_url: 'https://developer.apple.com/documentation/assetslibrary/alassetslibrarychangednotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/assetslibrary/alassetslibrarychangednotification.json'
content_hash: 'sha256:41e22f8d35b8e6e5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Assets Library](../assetslibrary.md)

# ALAssetsLibraryChangedNotification

<sub>Global Variable</sub>

Sent when the contents of the assets library have changed from under the app that is using the data.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```objc
extern NSString * const ALAssetsLibraryChangedNotification;
```

## Discussion

In iOS 4.0, the notification’s [object](../foundation/nsnotification/object.md) is `nil`. In iOS 4.1 and later, the notification object is the library object that posted the notification.

In iOS 6.0 and later, the user information dictionary describes what changed:

- If the user information dictionary is `nil`, reload all assets and asset groups.
- If the user information dictionary an empty dictionary, there is no need to reload assets and asset groups.
- If the user information dictionary is not empty, reload the effected assets and asset groups. For the keys used, see [Notification Keys](notification-keys.md).

This notification is sent on an arbitrary thread.
