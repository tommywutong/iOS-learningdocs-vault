---
title: CustomLocalizedStringResourceConvertible
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/customlocalizedstringresourceconvertible
source_url: 'https://developer.apple.com/documentation/foundation/customlocalizedstringresourceconvertible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/customlocalizedstringresourceconvertible.json'
content_hash: 'sha256:03e950a14a72106d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# CustomLocalizedStringResourceConvertible

<sub>Protocol</sub>

A type that provides an out-of-process localizable description.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol CustomLocalizedStringResourceConvertible
```

## Overview

Similar to [CustomStringConvertible](../swift/customstringconvertible.md), types that conform to [CustomLocalizedStringResourceConvertible](customlocalizedstringresourceconvertible.md) provide their own representation when converting to a string instance. Whereas [CustomStringConvertible](../swift/customstringconvertible.md) provides a [description](../swift/customstringconvertible/description.md) string, this type offers a [LocalizedStringResource](localizedstringresource.md). This allows out-of-process callers to create a localized description from the resource, possibly in a different locale than the current process uses.

## Relationships

- **Conforming Types**: [LocalizedStringResource](localizedstringresource.md), [PersonNameComponents](personnamecomponents.md)

## Topics

### Describing a resource

- [localizedStringResource](customlocalizedstringresourceconvertible/localizedstringresource.md) — A resource that helps provide a description of this instance.

## See Also

### Localization

- [Locale](locale.md) — Information about linguistic, cultural, and technological conventions for use in formatting data for presentation.
- [NSOrthography](nsorthography.md) — A description of the linguistic content of natural language text, typically used for spelling and grammar checking.
- [NSLocalizedString(_:tableName:bundle:value:comment:)](<nslocalizedstring(__tablename_bundle_value_comment_).md>) — Returns a localized string from a table that Xcode generates for you when exporting localizations.
- [LocalizedStringResource](localizedstringresource.md) — A reference to a localizable string, accessible from another process.
- [URLResource](urlresource.md) — A resource located at a particular file URL within a bundle.
