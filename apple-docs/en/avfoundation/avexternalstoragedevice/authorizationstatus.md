---
title: authorizationStatus
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avexternalstoragedevice/authorizationstatus
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalstoragedevice/authorizationstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalstoragedevice/authorizationstatus.json'
content_hash: 'sha256:75cb545bac8c720b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVExternalStorageDevice](../avexternalstoragedevice.md)

# authorizationStatus

<sub>Type Property</sub>

Your app’s authorization status for the external storage device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class var authorizationStatus: AVAuthorizationStatus { get }
```

## Discussion

If the value is [AVAuthorizationStatusNotDetermined](../avauthorizationstatus/notdetermined.md), you can request access by calling the [+ requestAccessWithCompletionHandler:](<requestaccess(completionhandler_).md>) method.
