---
title: authorizationStatus()
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+（14.0 起废弃）, iPadOS 8.0+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, macOS 10.13+（11.0 起废弃）, tvOS 10.0+（14.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/photos/phphotolibrary/authorizationstatus()
source_url: 'https://developer.apple.com/documentation/photos/phphotolibrary/authorizationstatus()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibrary/authorizationstatus%28%29.json'
content_hash: 'sha256:711cb566fbb1ed83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotoLibrary](../phphotolibrary.md)

# authorizationStatus()

<sub>Type Method</sub>

Returns information about your app’s authorization to access the user’s photo library.

> [!warning] Deprecated
> Use [+ authorizationStatusForAccessLevel:](<authorizationstatus(for_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func authorizationStatus() -> PHAuthorizationStatus
```

## Return Value

The current authorization status.

## See Also

### Verifying Authorization

- [+ authorizationStatusForAccessLevel:](<authorizationstatus(for_).md>) — Returns the app’s authorization to access the user’s photo library for the specified access level.
- [+ requestAuthorizationForAccessLevel:handler:](<requestauthorization(for_handler_).md>) — Prompts the user to grant the app permission to access the photo library.
- [PHAccessLevel](../phaccesslevel.md) — The app’s level of access to the user’s photo library.
- [PHAuthorizationStatus](../phauthorizationstatus.md) — Information about your app’s authorization to access the user’s photo library.
- [+ requestAuthorization:](<requestauthorization(__).md>) — Requests the user’s permission, if needed, to access the photo library. _(deprecated)_
