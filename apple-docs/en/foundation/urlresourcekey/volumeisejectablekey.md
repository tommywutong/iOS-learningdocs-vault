---
title: volumeIsEjectableKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresourcekey/volumeisejectablekey
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcekey/volumeisejectablekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcekey/volumeisejectablekey.json'
content_hash: 'sha256:35705d222006e2dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResourceKey](../urlresourcekey.md)

# volumeIsEjectableKey

<sub>Type Property</sub>

A key for determining whether the volume is ejectable from the drive mechanism under software control.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let volumeIsEjectableKey: URLResourceKey
```

## Discussion

The corresponding value is a Boolean `NSNumber` object.

## See Also

### Volume status keys

- [NSURLVolumeIsAutomountedKey](volumeisautomountedkey.md) — A key for determining whether the volume is automounted.
- [NSURLVolumeIsBrowsableKey](volumeisbrowsablekey.md) — A key for determining whether the volume is visible in GUI-based file-browsing environments, such as the Desktop or the Finder app.
- [NSURLVolumeIsEncryptedKey](volumeisencryptedkey.md) — A key for determining whether the volume is encrypted.
- [NSURLVolumeIsInternalKey](volumeisinternalkey.md) — A key for determining whether the volume is connected to an internal bus.
- [NSURLVolumeIsJournalingKey](volumeisjournalingkey.md) — A key for determining whether the volume is currently journaling.
- [NSURLVolumeIsLocalKey](volumeislocalkey.md) — A key for determining whether the volume is on a local device.
- [NSURLVolumeIsReadOnlyKey](volumeisreadonlykey.md) — A key for determining whether the volume is read-only.
- [NSURLVolumeIsRemovableKey](volumeisremovablekey.md) — A key for determining whether the volume is removable from the drive mechanism.
- [NSURLVolumeIsRootFileSystemKey](volumeisrootfilesystemkey.md) — A key for determining whether the volume is the root file system.
- [NSURLVolumeSupportsFileProtectionKey](volumesupportsfileprotectionkey.md) — A Boolean value that indicates the volume supports data protection for files.
- [NSURLVolumeTypeNameKey](volumetypenamekey.md) — The key for the name of the file system type.
- [NSURLVolumeSubtypeKey](volumesubtypekey.md) — The key for the file system subtype value.
- [NSURLVolumeMountFromLocationKey](volumemountfromlocationkey.md) — The key for the volume mounted-from location.
