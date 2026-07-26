---
title: PHAuthorizationStatus.notDetermined
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phauthorizationstatus/notdetermined
source_url: 'https://developer.apple.com/documentation/photos/phauthorizationstatus/notdetermined'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phauthorizationstatus/notdetermined.json'
content_hash: 'sha256:4467e405aaca8d70'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAuthorizationStatus](../phauthorizationstatus.md)

# PHAuthorizationStatus.notDetermined

<sub>Case</sub>

The user hasn’t set the app’s authorization status.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case notDetermined
```

## Discussion

The framework automatically prompts for user authorization when you attempt to fetch assets, asset collections, or collection lists. Alternatively, you may call the [+ requestAuthorizationForAccessLevel:handler:](<../phphotolibrary/requestauthorization(for_handler_).md>) method to prompt the user for authorization at a time of your choosing.

## See Also

### Status Types

- [PHAuthorizationStatusRestricted](restricted.md) — The app isn’t authorized to access the photo library, and the user can’t grant such permission.
- [PHAuthorizationStatusDenied](denied.md) — The user explicitly denied this app access to the photo library.
- [PHAuthorizationStatusAuthorized](authorized.md) — The user explicitly granted this app access to the photo library.
- [PHAuthorizationStatusLimited](limited.md) — The user authorized this app for limited photo library access.
