---
title: volumeIsRemovable
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresourcevalues/volumeisremovable
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcevalues/volumeisremovable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcevalues/volumeisremovable.json'
content_hash: 'sha256:eba06c50302980b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResourceValues](../urlresourcevalues.md)

# volumeIsRemovable

<sub>Instance Property</sub>

A Boolean value that indicates whether the volume’s media is removable from the drive mechanism.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var volumeIsRemovable: Bool? { get }
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
- [volumeIsRootFileSystem](volumeisrootfilesystem.md) — A Boolean value that indicates whether the volume is the root file system.
- [volumeTypeName](volumetypename.md) — The volume’s type name, as a string.
- [volumeSubtype](volumesubtype.md) — An integer value that indicates the file system subtype.
- [volumeMountFromLocation](volumemountfromlocation.md) — The file system device location, as a string.
