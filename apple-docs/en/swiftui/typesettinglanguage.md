---
title: TypesettingLanguage
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/typesettinglanguage
source_url: 'https://developer.apple.com/documentation/swiftui/typesettinglanguage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/typesettinglanguage.json'
content_hash: 'sha256:78791a95ab901a9a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TypesettingLanguage

<sub>Structure</sub>

Defines how typesetting language is determined for text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TypesettingLanguage
```

## Overview

Use a modifier like [typesettingLanguage(_:isEnabled:)](<view/typesettinglanguage(__isenabled_).md>) to specify the typesetting language.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting language behavior

- [automatic](typesettinglanguage/automatic.md) — Automatic language behavior.
- [explicit(_:)](<typesettinglanguage/explicit(__).md>) — Use explicit language.

## See Also

### Localizing text

- [Preparing views for localization](preparing-views-for-localization.md) — Specify hints and add strings to localize your SwiftUI views.
- [LocalizedStringKey](localizedstringkey.md) — The key used to look up an entry in a strings file or strings dictionary file.
- [locale](environmentvalues/locale.md) — The current locale that views should use.
- [typesettingLanguage(_:isEnabled:)](<view/typesettinglanguage(__isenabled_).md>) — Specifies the language for typesetting.
