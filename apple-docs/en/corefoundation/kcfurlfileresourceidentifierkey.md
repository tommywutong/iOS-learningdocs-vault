---
title: kCFURLFileResourceIdentifierKey
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfurlfileresourceidentifierkey
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfurlfileresourceidentifierkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfurlfileresourceidentifierkey.json'
content_hash: 'sha256:efc4dc6cc6bf7a67'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFURLFileResourceIdentifierKey

<sub>Global Variable</sub>

Key for the resource’s unique identifier, returned as a `CFType` object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCFURLFileResourceIdentifierKey: CFString!
```

## Discussion

This identifier can be used to determine equality between file system resources with the [CFEqual](<cfequal(____).md>) function. Two resources are equal if they have the same file-system path or if their paths link to the same inode on the same file system.

The value of this identifier is not persistent across system restarts.

## See Also

### Constants

- [kCFURLNameKey](kcfurlnamekey.md) — Key for the resource’s name in the file system, returned as a `CFString` object.
- [kCFURLLocalizedNameKey](kcfurllocalizednamekey.md) — Key for the resource’s localized or extension-hidden name, retuned as a `CFString` object.
- [kCFURLPathKey](kcfurlpathkey.md) — A `CFString` value containing the URL’s path as a file system path. (read-only)
- [kCFURLIsRegularFileKey](kcfurlisregularfilekey.md) — Key for determining whether the resource is a regular file, as opposed to a directory or a symbolic link. Returned as a `CFBoolean` object.
- [kCFURLIsDirectoryKey](kcfurlisdirectorykey.md) — Key for determining whether the resource is a directory, returned as a `CFBoolean` object.
- [kCFURLIsSymbolicLinkKey](kcfurlissymboliclinkkey.md) — Key for determining whether the resource is a symbolic link, returned as a `CFBoolean` object.
- [kCFURLIsVolumeKey](kcfurlisvolumekey.md) — Key for determining whether the resource is the root directory of a volume, returned as a `CFBoolean` object.
- [kCFURLIsPackageKey](kcfurlispackagekey.md) — Key for determining whether the resource is a packaged directory, returned as a `CFBoolean` object.
- [kCFURLIsSystemImmutableKey](kcfurlissystemimmutablekey.md) — Key for determining whether the resource’s system immutable bit is set, returned as a `CFBoolean` object.
- [kCFURLIsUserImmutableKey](kcfurlisuserimmutablekey.md) — Key for determining whether the resource’s user immutable bit is set, returned as a `CFBoolean` object.
- [kCFURLIsHiddenKey](kcfurlishiddenkey.md) — Key for determining whether the resource is normally not displayed to users, returned as a `CFBoolean` object.
- [kCFURLHasHiddenExtensionKey](kcfurlhashiddenextensionkey.md) — Key for determining whether the resource’s extension is normally removed from its localized name, returned as a `CFBoolean` object.
- [kCFURLCreationDateKey](kcfurlcreationdatekey.md) — Key for the resource’s creation date, returned as a `CFDate` object if the volume supports creation dates, or `nil` if creation dates are unsupported.
- [kCFURLContentAccessDateKey](kcfurlcontentaccessdatekey.md) — Key for the last time the resource was accessed, returned as a `CFDate` object if the volume supports access dates, or `nil` if access dates are unsupported.
- [kCFURLContentModificationDateKey](kcfurlcontentmodificationdatekey.md) — Key for the last time the resource was modified, returned as a `CFDate` object if the volume supports modification dates, or `nil` if modification dates are unsupported.
