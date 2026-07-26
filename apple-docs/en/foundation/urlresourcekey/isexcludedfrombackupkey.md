---
title: isExcludedFromBackupKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.1+, iPadOS 5.1+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresourcekey/isexcludedfrombackupkey
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcekey/isexcludedfrombackupkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcekey/isexcludedfrombackupkey.json'
content_hash: 'sha256:87329746b73c02f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResourceKey](../urlresourcekey.md)

# isExcludedFromBackupKey

<sub>Type Property</sub>

A key for indicating whether the system excludes the resource from all backups of app data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let isExcludedFromBackupKey: URLResourceKey
```

## Discussion

The value of this key is a read-write Boolean [NSNumber](../nsnumber.md) object.

Use this property to exclude cache and other app support files that aren’t necessary in a backup. Set this property each time you save a file because some common file operations cause this property to reset to `false`.

## See Also

### Other resource keys

- [NSURLKeysOfUnsetValuesKey](keysofunsetvalueskey.md) — Key for the resource properties that have not been set after the [- setResourceValues:error:](<../nsurl/setresourcevalues(__).md>) method returns an error, returned as an array of `NSString` objects.
- [NSURLQuarantinePropertiesKey](quarantinepropertieskey.md)
- [NSURLAddedToDirectoryDateKey](addedtodirectorydatekey.md) — The time at which the resource’s was created or renamed into or within its parent directory, returned as an `NSDate`. Inconsistent behavior may be observed when this attribute is requested on hard-linked items. This property is not supported by all volumes. (read-only)
- [NSURLAttributeModificationDateKey](attributemodificationdatekey.md) — The time at which the resource’s attributes were most recently modified, returned as an `NSDate` object if the volume supports attribute modification dates, or `nil` if attribute modification dates are unsupported (read-only).
- [NSURLContentAccessDateKey](contentaccessdatekey.md) — The time at which the resource was most recently accessed.
- [NSURLContentModificationDateKey](contentmodificationdatekey.md) — The time at which the resource was most recently modified.
- [NSURLCreationDateKey](creationdatekey.md) — The time at which the resource was created.
- [NSURLCustomIconKey](customiconkey.md) — The icon stored with the resource, returned as an `NSImage` object, or `nil` if the resource has no custom icon.
- [NSURLDocumentIdentifierKey](documentidentifierkey.md) — The document identifier returned as an `NSNumber` (read-only).
- [NSURLEffectiveIconKey](effectiveiconkey.md) — The resource’s normal icon, returned as an `NSImage` object (read-only).
- [NSURLGenerationIdentifierKey](generationidentifierkey.md) — An opaque generation identifier, returned as an `id <NSCopying, NSCoding, NSObject>` (read-only)
- [NSURLHasHiddenExtensionKey](hashiddenextensionkey.md) — Key for determining whether the resource’s extension is normally removed from its localized name, returned as a Boolean `NSNumber` object (read-write).
- [NSURLIsExecutableKey](isexecutablekey.md) — Key for determining whether the current process (as determined by the EUID) can execute the resource (if it is a file) or search the resource (if it is a directory), returned as a Boolean `NSNumber` object (read-only).
- [NSURLIsHiddenKey](ishiddenkey.md) — Key for determining whether the resource is normally not displayed to users, returned as a Boolean `NSNumber` object (read-write).
- [NSURLIsReadableKey](isreadablekey.md) — Key for determining whether the current process (as determined by the EUID) can read the resource, returned as a Boolean `NSNumber` object (read-only).
