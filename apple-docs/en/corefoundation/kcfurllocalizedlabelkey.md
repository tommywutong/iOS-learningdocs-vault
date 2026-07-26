---
title: kCFURLLocalizedLabelKey
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfurllocalizedlabelkey
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfurllocalizedlabelkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfurllocalizedlabelkey.json'
content_hash: 'sha256:f7c43d939615012a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFURLLocalizedLabelKey

<sub>Global Variable</sub>

Key for the resource’s localized label text, returned as a `CFString` object, or `NULL` if the resource has no localized label text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCFURLLocalizedLabelKey: CFString!
```

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
