---
title: 'authorizationStatus(for:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phphotolibrary/authorizationstatus(for:)'
source_url: 'https://developer.apple.com/documentation/photos/phphotolibrary/authorizationstatus(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibrary/authorizationstatus%28for%3A%29.json'
content_hash: 'sha256:7d7867c5ba3d9b46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotoLibrary](../phphotolibrary.md)

# authorizationStatus(for:)

<sub>Type Method</sub>

Returns the app’s authorization to access the user’s photo library for the specified access level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func authorizationStatus(for accessLevel: PHAccessLevel) -> PHAuthorizationStatus
```

## Parameters

- `accessLevel` — The access level for which to determine the app’s authorization status.

## Return Value

The app’s authorization status.

## Discussion

For more information about accessing the user’s Photos library, see [Delivering an Enhanced Privacy Experience in Your Photos App](../../photokit/delivering-an-enhanced-privacy-experience-in-your-photos-app.md).

## See Also

### Verifying Authorization

- [+ requestAuthorizationForAccessLevel:handler:](<requestauthorization(for_handler_).md>) — Prompts the user to grant the app permission to access the photo library.
- [PHAccessLevel](../phaccesslevel.md) — The app’s level of access to the user’s photo library.
- [PHAuthorizationStatus](../phauthorizationstatus.md) — Information about your app’s authorization to access the user’s photo library.
- [+ authorizationStatus](<authorizationstatus().md>) — Returns information about your app’s authorization to access the user’s photo library. _(deprecated)_
- [+ requestAuthorization:](<requestauthorization(__).md>) — Requests the user’s permission, if needed, to access the photo library. _(deprecated)_
