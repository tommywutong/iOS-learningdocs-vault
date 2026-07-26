---
title: URLResource
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresource
source_url: 'https://developer.apple.com/documentation/foundation/urlresource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresource.json'
content_hash: 'sha256:90487ef526d72229'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLResource

<sub>Structure</sub>

A resource located at a particular file URL within a bundle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct URLResource
```

## Overview

This type is similar to [LocalizedStringResource](localizedstringresource.md) in its ability to provide access to a resource in a bundle, possibly from another process. Use the [URL](url.md) initializer [init(resource:)](<url/init(resource_).md>) to resolve the resource.

## Relationships

- **Conforms To**: [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a URL resource

- [init(name:subdirectory:locale:bundle:)](<urlresource/init(name_subdirectory_locale_bundle_).md>) — Creates a URL resource from the given bundle, name, and subdirectory, optionally specifying a locale.

### Accessing resource properties

- [bundle](urlresource/bundle.md) — The bundle containing the resource.
- [name](urlresource/name.md) — The name of the resource in the bundle.
- [subdirectory](urlresource/subdirectory.md) — The subdirectory, if any, of the resource.
- [locale](urlresource/locale.md) — The bundle containing the resource.

## See Also

### Localization

- [Locale](locale.md) — Information about linguistic, cultural, and technological conventions for use in formatting data for presentation.
- [NSOrthography](nsorthography.md) — A description of the linguistic content of natural language text, typically used for spelling and grammar checking.
- [NSLocalizedString(_:tableName:bundle:value:comment:)](<nslocalizedstring(__tablename_bundle_value_comment_).md>) — Returns a localized string from a table that Xcode generates for you when exporting localizations.
- [LocalizedStringResource](localizedstringresource.md) — A reference to a localizable string, accessible from another process.
- [CustomLocalizedStringResourceConvertible](customlocalizedstringresourceconvertible.md) — A type that provides an out-of-process localizable description.
