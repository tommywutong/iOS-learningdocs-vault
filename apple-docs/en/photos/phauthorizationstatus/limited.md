---
title: PHAuthorizationStatus.limited
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phauthorizationstatus/limited
source_url: 'https://developer.apple.com/documentation/photos/phauthorizationstatus/limited'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phauthorizationstatus/limited.json'
content_hash: 'sha256:4d4e06bab5cabf8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAuthorizationStatus](../phauthorizationstatus.md)

# PHAuthorizationStatus.limited

<sub>Case</sub>

The user authorized this app for limited photo library access.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case limited
```

## Discussion

Use [- presentLimitedLibraryPickerFromViewController:](<../phphotolibrary/presentlimitedlibrarypicker(from_).md>) or [- presentLimitedLibraryPickerFromViewController:completionHandler:](<../phphotolibrary/presentlimitedlibrarypicker(from_completionhandler_).md>) to manually present the limited library picker.

> [!important] Important
> Add the `PHPhotoLibraryPreventAutomaticLimitedAccessAlert` key with a Boolean value of `true` to your app’s `Info.plist` file to prevent the system from automatically presenting the limited library selection prompt.

## See Also

### Status Types

- [PHAuthorizationStatusNotDetermined](notdetermined.md) — The user hasn’t set the app’s authorization status.
- [PHAuthorizationStatusRestricted](restricted.md) — The app isn’t authorized to access the photo library, and the user can’t grant such permission.
- [PHAuthorizationStatusDenied](denied.md) — The user explicitly denied this app access to the photo library.
- [PHAuthorizationStatusAuthorized](authorized.md) — The user explicitly granted this app access to the photo library.
