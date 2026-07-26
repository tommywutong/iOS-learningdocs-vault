---
title: PHAccessLevel
framework: Photos
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phaccesslevel
source_url: 'https://developer.apple.com/documentation/photos/phaccesslevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phaccesslevel.json'
content_hash: 'sha256:ed738a7afb8ca741'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHAccessLevel

<sub>Enumeration</sub>

The app’s level of access to the user’s photo library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum PHAccessLevel
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Access Levels

- [PHAccessLevelAddOnly](phaccesslevel/addonly.md) — A value that indicates the app may only add to the user’s photo library.
- [PHAccessLevelReadWrite](phaccesslevel/readwrite.md) — A value that indicates the app can read from and write to the user’s photo library.

### Initializers

- [init(rawValue:)](<phaccesslevel/init(rawvalue_).md>)

## See Also

### Verifying Authorization

- [+ authorizationStatusForAccessLevel:](<phphotolibrary/authorizationstatus(for_).md>) — Returns the app’s authorization to access the user’s photo library for the specified access level.
- [+ requestAuthorizationForAccessLevel:handler:](<phphotolibrary/requestauthorization(for_handler_).md>) — Prompts the user to grant the app permission to access the photo library.
- [PHAuthorizationStatus](phauthorizationstatus.md) — Information about your app’s authorization to access the user’s photo library.
- [+ authorizationStatus](<phphotolibrary/authorizationstatus().md>) — Returns information about your app’s authorization to access the user’s photo library. _(deprecated)_
- [+ requestAuthorization:](<phphotolibrary/requestauthorization(__).md>) — Requests the user’s permission, if needed, to access the photo library. _(deprecated)_
