---
title: LocalizedStringResource.BundleDescription
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/localizedstringresource/bundledescription
source_url: 'https://developer.apple.com/documentation/foundation/localizedstringresource/bundledescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/localizedstringresource/bundledescription.json'
content_hash: 'sha256:3da4560d13a5ac40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [LocalizedStringResource](../localizedstringresource.md)

# LocalizedStringResource.BundleDescription

<sub>Enumeration</sub>

The location of a bundle to use for looking up localized strings, such as the main bundle, or a bundle at a specific file URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum BundleDescription
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Bundle descriptions

- [LocalizedStringResource.BundleDescription.main](bundledescription/main.md) — The app’s main bundle.
- [LocalizedStringResource.BundleDescription.atURL(_:)](<bundledescription/aturl(__).md>) — A bundle located at a specific file URL.
- [LocalizedStringResource.BundleDescription.forClass(_:)](<bundledescription/forclass(__).md>) — The bundle for a specific class.

## See Also

### Accessing resource properties

- [key](key.md) — The key to use to look up a localized string.
- [defaultValue](defaultvalue.md) — The resource’s default value.
- [table](table.md) — The name of the table containing the key-value pairs.
- [bundle](bundle.md) — The bundle containing the table’s strings file.
- [locale](locale.md) — The locale to use to look up the localized string from the string resource.
