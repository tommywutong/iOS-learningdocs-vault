---
title: volume
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresourcevalues/volume
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcevalues/volume'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcevalues/volume.json'
content_hash: 'sha256:260ac53d9cfd9995'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResourceValues](../urlresourcevalues.md)

# volume

<sub>Instance Property</sub>

URL of the volume on which the resource is stored.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var volume: URL? { get }
```

## See Also

### Volume support values

- [isMountTrigger](ismounttrigger.md) — A Boolean value that indicates whether this URL is a file system trigger directory.
- [isVolume](isvolume.md) — A Boolean value that indicates whether the root directory is a volume.
- [volumeCreationDate](volumecreationdate.md) — The volume’s creation date, or `nil` if this cannot be determined.
- [volumeIdentifier](volumeidentifier.md) — An identifier that identifies the volume the file system object is on.
- [volumeLocalizedFormatDescription](volumelocalizedformatdescription.md) — The volume format that’s visible to the user.
- [volumeLocalizedName](volumelocalizedname.md) — The name of the volume that’s visible to the user.
- [volumeMaximumFileSize](volumemaximumfilesize.md) — The largest file size supported by this file system, in bytes, or `nil` if this cannot be determined.
- [volumeName](volumename.md) — The name of the volume.
- [volumeResourceCount](volumeresourcecount.md) — The total number of resources on the volume.
- [volumeSupportsAccessPermissions](volumesupportsaccesspermissions.md) — A Boolean value that indicates whether the volume supports setting standard access permissions.
- [volumeSupportsAdvisoryFileLocking](volumesupportsadvisoryfilelocking.md) — A Boolean value that indicates whether the volume implements whole-file flock(2) style advisory locks, and the O_EXLOCK and O_SHLOCK flags of the open(2) call.
- [volumeSupportsCasePreservedNames](volumesupportscasepreservednames.md) — A Boolean value that indicates whether the volume format preserves the case of file and directory names.
- [volumeSupportsCaseSensitiveNames](volumesupportscasesensitivenames.md) — A Boolean value that indicates whether the volume format treats upper and lower case characters in file and directory names as different.
- [volumeSupportsCompression](volumesupportscompression.md) — A Boolean value that indicates whether the volume supports transparent decompression of compressed files using decmpfs.
- [volumeSupportsExclusiveRenaming](volumesupportsexclusiverenaming.md) — A Boolean value that indicates whether the volume warns of a pre-existing destination when renaming a file.
