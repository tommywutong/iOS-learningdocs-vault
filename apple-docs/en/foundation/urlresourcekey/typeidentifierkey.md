---
title: typeIdentifierKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+（27.0 起废弃）, iPadOS 4.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.6+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/urlresourcekey/typeidentifierkey
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcekey/typeidentifierkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcekey/typeidentifierkey.json'
content_hash: 'sha256:1ec7d27bf16fbc45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResourceKey](../urlresourcekey.md)

# typeIdentifierKey

<sub>Type Property</sub>

The resource’s uniform type identifier (UTI), returned as an `NSString` object (read-only).

> [!warning] Deprecated
> Use NSURLContentTypeKey instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let typeIdentifierKey: URLResourceKey
```

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
- [NSURLIsExcludedFromBackupKey](isexcludedfrombackupkey.md) — A key for indicating whether the system excludes the resource from all backups of app data.
- [NSURLIsExecutableKey](isexecutablekey.md) — Key for determining whether the current process (as determined by the EUID) can execute the resource (if it is a file) or search the resource (if it is a directory), returned as a Boolean `NSNumber` object (read-only).
- [NSURLIsHiddenKey](ishiddenkey.md) — Key for determining whether the resource is normally not displayed to users, returned as a Boolean `NSNumber` object (read-write).
