---
title: PHAuthorizationStatus
framework: Photos
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phauthorizationstatus
source_url: 'https://developer.apple.com/documentation/photos/phauthorizationstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phauthorizationstatus.json'
content_hash: 'sha256:4a87dc499bf138bc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHAuthorizationStatus

<sub>Enumeration</sub>

Information about your app’s authorization to access the user’s photo library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum PHAuthorizationStatus
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Status Types

- [PHAuthorizationStatusNotDetermined](phauthorizationstatus/notdetermined.md) — The user hasn’t set the app’s authorization status.
- [PHAuthorizationStatusRestricted](phauthorizationstatus/restricted.md) — The app isn’t authorized to access the photo library, and the user can’t grant such permission.
- [PHAuthorizationStatusDenied](phauthorizationstatus/denied.md) — The user explicitly denied this app access to the photo library.
- [PHAuthorizationStatusAuthorized](phauthorizationstatus/authorized.md) — The user explicitly granted this app access to the photo library.
- [PHAuthorizationStatusLimited](phauthorizationstatus/limited.md) — The user authorized this app for limited photo library access.

### Initializers

- [init(rawValue:)](<phauthorizationstatus/init(rawvalue_).md>)

## See Also

### Verifying Authorization

- [+ authorizationStatusForAccessLevel:](<phphotolibrary/authorizationstatus(for_).md>) — Returns the app’s authorization to access the user’s photo library for the specified access level.
- [+ requestAuthorizationForAccessLevel:handler:](<phphotolibrary/requestauthorization(for_handler_).md>) — Prompts the user to grant the app permission to access the photo library.
- [PHAccessLevel](phaccesslevel.md) — The app’s level of access to the user’s photo library.
- [+ authorizationStatus](<phphotolibrary/authorizationstatus().md>) — Returns information about your app’s authorization to access the user’s photo library. _(deprecated)_
- [+ requestAuthorization:](<phphotolibrary/requestauthorization(__).md>) — Requests the user’s permission, if needed, to access the photo library. _(deprecated)_
