---
title: FileManager.SearchPathDirectory
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/searchpathdirectory
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/searchpathdirectory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/searchpathdirectory.json'
content_hash: 'sha256:b076e5295fcd36a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# FileManager.SearchPathDirectory

<sub>Enumeration</sub>

The location of significant directories.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum SearchPathDirectory
```

## Overview

Use these constants with the [init(for:in:appropriateFor:create:)](<../url/init(for_in_appropriatefor_create_).md>) initializer and the [- URLsForDirectory:inDomains:](<urls(for_in_).md>) and [- URLForDirectory:inDomain:appropriateForURL:create:error:](<url(for_in_appropriatefor_create_).md>) methods of FileManager.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Directory Locations

- [NSApplicationDirectory](searchpathdirectory/applicationdirectory.md) — Supported applications (`/Applications`).
- [NSDemoApplicationDirectory](searchpathdirectory/demoapplicationdirectory.md) — Unsupported applications and demonstration versions.
- [NSDeveloperApplicationDirectory](searchpathdirectory/developerapplicationdirectory.md) — Developer applications (`/Developer/Applications`).
- [NSAdminApplicationDirectory](searchpathdirectory/adminapplicationdirectory.md) — System and network administration applications.
- [NSLibraryDirectory](searchpathdirectory/librarydirectory.md) — Various user-visible documentation, support, and configuration files (`/Library`).
- [NSDeveloperDirectory](searchpathdirectory/developerdirectory.md) — Developer resources (`/Developer`).
- [NSUserDirectory](searchpathdirectory/userdirectory.md) — User home directories (`/Users`).
- [NSDocumentationDirectory](searchpathdirectory/documentationdirectory.md) — Documentation.
- [NSDocumentDirectory](searchpathdirectory/documentdirectory.md) — Document directory.
- [NSCoreServiceDirectory](searchpathdirectory/coreservicedirectory.md) — Core services (`System/Library/CoreServices`).
- [NSAutosavedInformationDirectory](searchpathdirectory/autosavedinformationdirectory.md) — The user’s autosaved documents (`Library/Autosave Information`).
- [NSDesktopDirectory](searchpathdirectory/desktopdirectory.md) — The user’s desktop directory.
- [NSCachesDirectory](searchpathdirectory/cachesdirectory.md) — Discardable cache files (`Library/Caches`).
- [NSApplicationSupportDirectory](searchpathdirectory/applicationsupportdirectory.md) — Application support files (`Library/Application Support`).
- [NSDownloadsDirectory](searchpathdirectory/downloadsdirectory.md) — The user’s downloads directory.
- [NSInputMethodsDirectory](searchpathdirectory/inputmethodsdirectory.md) — Input Methods `(Library/Input Methods)`.
- [NSMoviesDirectory](searchpathdirectory/moviesdirectory.md) — The user’s Movies directory `(~/Movies`).
- [NSMusicDirectory](searchpathdirectory/musicdirectory.md) — The user’s Music directory (`~/Music`).
- [NSPicturesDirectory](searchpathdirectory/picturesdirectory.md) — The user’s Pictures directory (`~/Pictures`).
- [NSPrinterDescriptionDirectory](searchpathdirectory/printerdescriptiondirectory.md) — The system’s PPDs directory (`Library/Printers/PPDs`).
- [NSSharedPublicDirectory](searchpathdirectory/sharedpublicdirectory.md) — The user’s Public sharing directory (`~/Public`).
- [NSPreferencePanesDirectory](searchpathdirectory/preferencepanesdirectory.md) — The PreferencePanes directory for use with System Preferences (`Library/PreferencePanes`).
- [NSApplicationScriptsDirectory](searchpathdirectory/applicationscriptsdirectory.md) — The user scripts folder for the calling application (`~/Library/Application Scripts/<code-signing-id>`.
- [NSItemReplacementDirectory](searchpathdirectory/itemreplacementdirectory.md) — The constant used to create a temporary directory.
- [NSAllApplicationsDirectory](searchpathdirectory/allapplicationsdirectory.md) — All directories where applications can be stored.
- [NSAllLibrariesDirectory](searchpathdirectory/alllibrariesdirectory.md) — All directories where resources can be stored.
- [NSTrashDirectory](searchpathdirectory/trashdirectory.md) — The trash directory.

### Initializers

- [init(rawValue:)](<searchpathdirectory/init(rawvalue_).md>)

## See Also

### Supporting Types

- [DirectoryEnumerationOptions](directoryenumerationoptions.md) — Options for enumerating the contents of directories.
- [SearchPathDomainMask](searchpathdomainmask.md) — Domain constants specifying base locations to use when you search for significant directories.
- [FileAttributeKey](../fileattributekey.md) — Keys in dictionaries used to get and set file attributes.
- [FileAttributeType](../fileattributetype.md) — Values representing a file’s type attribute.
- [FileProtectionType](../fileprotectiontype.md) — Protection level values that can be associated with a file attribute key.
- [URLFileProtection](../urlfileprotection.md) — Protection-level values for a URL resource key.
