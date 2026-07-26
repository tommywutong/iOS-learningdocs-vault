---
title: generationIdentifierKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresourcekey/generationidentifierkey
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcekey/generationidentifierkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcekey/generationidentifierkey.json'
content_hash: 'sha256:a3fb2ada096f618d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResourceKey](../urlresourcekey.md)

# generationIdentifierKey

<sub>Type Property</sub>

An opaque generation identifier, returned as an `id <NSCopying, NSCoding, NSObject>` (read-only)

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let generationIdentifierKey: URLResourceKey
```

## Discussion

The generation identifier can be compared using isEqual: to determine if the data in a document has been modified. For URLs which refer to the same file inode, the generation identifier changes when the data in the file’s data fork is changed. Changes to extended attributes or other file system metadata do not change the identifier. For URLs which refer to the same directory inode, the generation identifier changes when direct children of that directory are added, removed or renamed. Changes to the data of the direct children of that directory does not change the generation identifier. The  identifier persists across system restarts. It is tied to a specific document on a specific volume and is not transferred when the document is copied to another volume. This property is not supported by all volumes.

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
- [NSURLHasHiddenExtensionKey](hashiddenextensionkey.md) — Key for determining whether the resource’s extension is normally removed from its localized name, returned as a Boolean `NSNumber` object (read-write).
- [NSURLIsExcludedFromBackupKey](isexcludedfrombackupkey.md) — A key for indicating whether the system excludes the resource from all backups of app data.
- [NSURLIsExecutableKey](isexecutablekey.md) — Key for determining whether the current process (as determined by the EUID) can execute the resource (if it is a file) or search the resource (if it is a directory), returned as a Boolean `NSNumber` object (read-only).
- [NSURLIsHiddenKey](ishiddenkey.md) — Key for determining whether the resource is normally not displayed to users, returned as a Boolean `NSNumber` object (read-write).
- [NSURLIsReadableKey](isreadablekey.md) — Key for determining whether the current process (as determined by the EUID) can read the resource, returned as a Boolean `NSNumber` object (read-only).
