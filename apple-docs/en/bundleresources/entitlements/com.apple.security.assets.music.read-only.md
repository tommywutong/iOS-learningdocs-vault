---
title: com.apple.security.assets.music.read-only
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/entitlements/com.apple.security.assets.music.read-only
source_url: 'https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.assets.music.read-only'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/entitlements/com.apple.security.assets.music.read-only.json'
content_hash: 'sha256:224a7f89ef404dd4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Entitlements](../entitlements.md)

# com.apple.security.assets.music.read-only

<sub>Property List Key</sub>

A Boolean value that indicates whether the app may have read-only access to the Music folder.

## Discussion

To add this entitlement to your app, enable the App Sandbox capability in Xcode and set Music Folder to Read Only.

## See Also

### Files and media

- [App Sandbox Entitlement](com.apple.security.app-sandbox.md) — A Boolean value that indicates whether the app may use access control technology to contain damage to the system and user data if an app is compromised.
- [com.apple.security.files.user-selected.read-only](com.apple.security.files.user-selected.read-only.md) — A Boolean value that indicates whether the app may have read-only access to files the user has selected using an Open or Save dialog.
- [com.apple.security.files.user-selected.read-write](com.apple.security.files.user-selected.read-write.md) — A Boolean value that indicates whether the app may have read-write access to files the user has selected using an Open or Save dialog.
- [com.apple.security.files.downloads.read-only](com.apple.security.files.downloads.read-only.md) — A Boolean value that indicates whether the app may have read-only access to the Downloads folder.
- [com.apple.security.files.downloads.read-write](com.apple.security.files.downloads.read-write.md) — A Boolean value that indicates whether the app may have read-write access to the Downloads folder.
- [Privileged File Operations](com.apple.developer.security.privileged-file-operations.md) — An entitlement that permits apps to create symbolic links, replace files, and set file attributes.
- [com.apple.security.assets.pictures.read-only](com.apple.security.assets.pictures.read-only.md) — A Boolean value that indicates whether the app may have read-only access to the Pictures folder.
- [com.apple.security.assets.pictures.read-write](com.apple.security.assets.pictures.read-write.md) — A Boolean value that indicates whether the app may have read-write access to the Pictures folder.
- [com.apple.security.assets.music.read-write](com.apple.security.assets.music.read-write.md) — A Boolean value that indicates whether the app may have read-write access to the Music folder.
- [com.apple.security.assets.movies.read-only](com.apple.security.assets.movies.read-only.md) — A Boolean value that indicates whether the app may have read-only access to the Movies folder.
- [com.apple.security.assets.movies.read-write](com.apple.security.assets.movies.read-write.md) — A Boolean value that indicates whether the app may have read-write access to the Movies folder.
- [All files entitlement](com.apple.security.files.all.md) — A Boolean value that indicates whether the app may have access to all files. _(deprecated)_
- [Data Protection Entitlement](com.apple.developer.default-data-protection.md) — The level of data protection for sensitive user data when an app accesses it on a device.
