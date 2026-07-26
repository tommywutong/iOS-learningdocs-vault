---
title: volumeIsRootFileSystem
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresourcevalues/volumeisrootfilesystem
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcevalues/volumeisrootfilesystem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcevalues/volumeisrootfilesystem.json'
content_hash: 'sha256:fd65b7040a82e947'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResourceValues](../urlresourcevalues.md)

# volumeIsRootFileSystem

<sub>Instance Property</sub>

A Boolean value that indicates whether the volume is the root file system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var volumeIsRootFileSystem: Bool? { get }
```

## See Also

### Volume status values

- [volumeIsAutomounted](volumeisautomounted.md) — A Boolean value that indicates whether the volume is automounted.
- [volumeIsBrowsable](volumeisbrowsable.md) — A Boolean value that indicates whether the volume is visible through the user interface.
- [volumeIsEjectable](volumeisejectable.md) — A Boolean value that indicates whether the volume’s media is ejectable from the drive mechanism under software control.
- [volumeIsEncrypted](volumeisencrypted.md) — A Boolean value that indicates whether the volume is encrypted.
- [volumeIsInternal](volumeisinternal.md) — A Boolean value that indicates whether the volume’s device is connected to an internal bus, or nil if not available.
- [volumeIsJournaling](volumeisjournaling.md) — A Boolean value that indicates whether the volume is currently using a journal for speedy recovery after an unplanned restart.
- [volumeIsLocal](volumeislocal.md) — A Boolean value that indicates whether the volume is on a local device.
- [volumeIsReadOnly](volumeisreadonly.md) — A Boolean value that indicates whether the volume is read-only.
- [volumeIsRemovable](volumeisremovable.md) — A Boolean value that indicates whether the volume’s media is removable from the drive mechanism.
- [volumeTypeName](volumetypename.md) — The volume’s type name, as a string.
- [volumeSubtype](volumesubtype.md) — An integer value that indicates the file system subtype.
- [volumeMountFromLocation](volumemountfromlocation.md) — The file system device location, as a string.
