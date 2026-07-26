---
title: PHAuthorizationStatus.restricted
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phauthorizationstatus/restricted
source_url: 'https://developer.apple.com/documentation/photos/phauthorizationstatus/restricted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phauthorizationstatus/restricted.json'
content_hash: 'sha256:629a2d3018434fd1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAuthorizationStatus](../phauthorizationstatus.md)

# PHAuthorizationStatus.restricted

<sub>Case</sub>

The app isn’t authorized to access the photo library, and the user can’t grant such permission.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case restricted
```

## Discussion

Parental controls or institutional configuration profiles can restrict the user’s ability to grant photo library access to an app.

## See Also

### Status Types

- [PHAuthorizationStatusNotDetermined](notdetermined.md) — The user hasn’t set the app’s authorization status.
- [PHAuthorizationStatusDenied](denied.md) — The user explicitly denied this app access to the photo library.
- [PHAuthorizationStatusAuthorized](authorized.md) — The user explicitly granted this app access to the photo library.
- [PHAuthorizationStatusLimited](limited.md) — The user authorized this app for limited photo library access.
