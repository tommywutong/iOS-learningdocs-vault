---
title: volumeSupportsCasePreservedNamesKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresourcekey/volumesupportscasepreservednameskey
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcekey/volumesupportscasepreservednameskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcekey/volumesupportscasepreservednameskey.json'
content_hash: 'sha256:eb639acb60460a2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResourceKey](../urlresourcekey.md)

# volumeSupportsCasePreservedNamesKey

<sub>Type Property</sub>

Key for determining whether the volume supports case-preserved names, returned as a Boolean `NSNumber` object (read-only).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let volumeSupportsCasePreservedNamesKey: URLResourceKey
```

## See Also

### Volume support keys

- [NSURLIsMountTriggerKey](ismounttriggerkey.md) — Key for determining whether the URL is a file system trigger directory, returned as a Boolean `NSNumber` object (read-only). Traversing or opening a file system trigger directory causes an attempt to mount a file system on the directory.
- [NSURLIsVolumeKey](isvolumekey.md) — Key for determining whether the resource is the root directory of a volume, returned as a Boolean `NSNumber` object (read-only).
- [NSURLVolumeCreationDateKey](volumecreationdatekey.md) — Key for the volume’s creation date, returned as an `NSDate` object, or `NULL` if it cannot be determined (read-only).
- [NSURLVolumeIdentifierKey](volumeidentifierkey.md) — The unique identifier of the resource’s volume, returned as an `id` (read-only).
- [NSURLVolumeLocalizedFormatDescriptionKey](volumelocalizedformatdescriptionkey.md) — Key for the volume’s descriptive format name, returned as an `NSString` object (read-only).
- [NSURLVolumeLocalizedNameKey](volumelocalizednamekey.md) — The name of the volume as it should be displayed in the user interface, returned as an `NSString` object (read-only).
- [NSURLVolumeMaximumFileSizeKey](volumemaximumfilesizekey.md) — Key for the largest file size supported by the volume in bytes, returned as a Boolean `NSNumber` object, or `nil` if it cannot be determined (read-only).
- [NSURLVolumeNameKey](volumenamekey.md) — The name of the volume, returned as an string object.
- [NSURLVolumeResourceCountKey](volumeresourcecountkey.md) — Key for the total number of resources on the volume, returned as an `NSNumber` object (read-only).
- [NSURLVolumeSupportsAccessPermissionsKey](volumesupportsaccesspermissionskey.md) — `true` if the volume supports setting POSIX access permissions with the `NSURLFileSecurityKey` property. (Read-only, value type boolean `NSNumber`).
- [NSURLVolumeSupportsAdvisoryFileLockingKey](volumesupportsadvisoryfilelockingkey.md) — Key for determining whether the volume implements whole-file advisory locks in the style of flock, along with the `O_EXLOCK` and `O_SHLOCK` flags of the open function, returned as a Boolean `NSNumber` object (read-only).
- [NSURLVolumeSupportsCaseSensitiveNamesKey](volumesupportscasesensitivenameskey.md) — Key for determining whether the volume supports case-sensitive names, returned as a Boolean `NSNumber` object (read-only).
- [NSURLVolumeSupportsCompressionKey](volumesupportscompressionkey.md) — Whether the volume supports transparent decompression of compressed files using `decmpfs`, returned as `NSNumber` containing a Boolean value (read-only).
- [NSURLVolumeSupportsExclusiveRenamingKey](volumesupportsexclusiverenamingkey.md) — Whether the volume supports exclusive renaming using `renamex_np(2)` with the `RENAME_EXCL` option, returned as `NSNumber` containing a Boolean value (read-only).
- [NSURLVolumeSupportsExtendedSecurityKey](volumesupportsextendedsecuritykey.md) — Key for determining whether the volume supports extended security (access control lists), returned as a Boolean `NSNumber` object (read-only).
