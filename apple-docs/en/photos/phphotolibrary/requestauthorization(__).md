---
title: 'requestAuthorization(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+（27.0 起废弃）, iPadOS 8.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 10.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/photos/phphotolibrary/requestauthorization(_:)'
source_url: 'https://developer.apple.com/documentation/photos/phphotolibrary/requestauthorization(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibrary/requestauthorization%28_%3A%29.json'
content_hash: 'sha256:56f9de6eadfe0eee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotoLibrary](../phphotolibrary.md)

# requestAuthorization(_:)

<sub>Type Method</sub>

Requests the user’s permission, if needed, to access the photo library.

> [!warning] Deprecated
> Use [+ requestAuthorizationForAccessLevel:handler:](<requestauthorization(for_handler_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func requestAuthorization(_ handler: @escaping (PHAuthorizationStatus) -> Void)
```

## Parameters

- `handler` — A block Photos calls upon determining your app’s authorization to access the photo library. The block takes a single parameter: - **status** — The current authorization status.

## See Also

### Verifying Authorization

- [+ authorizationStatusForAccessLevel:](<authorizationstatus(for_).md>) — Returns the app’s authorization to access the user’s photo library for the specified access level.
- [+ requestAuthorizationForAccessLevel:handler:](<requestauthorization(for_handler_).md>) — Prompts the user to grant the app permission to access the photo library.
- [PHAccessLevel](../phaccesslevel.md) — The app’s level of access to the user’s photo library.
- [PHAuthorizationStatus](../phauthorizationstatus.md) — Information about your app’s authorization to access the user’s photo library.
- [+ authorizationStatus](<authorizationstatus().md>) — Returns information about your app’s authorization to access the user’s photo library. _(deprecated)_
