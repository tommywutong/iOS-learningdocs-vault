---
title: 'requestAuthorization(for:handler:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phphotolibrary/requestauthorization(for:handler:)'
source_url: 'https://developer.apple.com/documentation/photos/phphotolibrary/requestauthorization(for:handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibrary/requestauthorization%28for%3Ahandler%3A%29.json'
content_hash: 'sha256:5ac39f42287045ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotoLibrary](../phphotolibrary.md)

# requestAuthorization(for:handler:)

<sub>Type Method</sub>

Prompts the user to grant the app permission to access the photo library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func requestAuthorization(for accessLevel: PHAccessLevel, handler: @escaping @Sendable (PHAuthorizationStatus) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func requestAuthorization(for accessLevel: PHAccessLevel) async -> PHAuthorizationStatus
```

## Parameters

- `accessLevel` — The access level to request.

- `handler` — The callback the system invokes when it’s made a determination of the app’s status.

## Discussion

For more information about accessing the user’s Photos library, see [Delivering an Enhanced Privacy Experience in Your Photos App](../../photokit/delivering-an-enhanced-privacy-experience-in-your-photos-app.md).

## See Also

### Verifying Authorization

- [+ authorizationStatusForAccessLevel:](<authorizationstatus(for_).md>) — Returns the app’s authorization to access the user’s photo library for the specified access level.
- [PHAccessLevel](../phaccesslevel.md) — The app’s level of access to the user’s photo library.
- [PHAuthorizationStatus](../phauthorizationstatus.md) — Information about your app’s authorization to access the user’s photo library.
- [+ authorizationStatus](<authorizationstatus().md>) — Returns information about your app’s authorization to access the user’s photo library. _(deprecated)_
- [+ requestAuthorization:](<requestauthorization(__).md>) — Requests the user’s permission, if needed, to access the photo library. _(deprecated)_
