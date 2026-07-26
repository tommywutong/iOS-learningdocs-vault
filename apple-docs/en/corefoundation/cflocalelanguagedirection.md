---
title: CFLocaleLanguageDirection
framework: Core Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cflocalelanguagedirection
source_url: 'https://developer.apple.com/documentation/corefoundation/cflocalelanguagedirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cflocalelanguagedirection.json'
content_hash: 'sha256:9d11daaf2da6b9bf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFLocaleLanguageDirection

<sub>Enumeration</sub>

These constants describe the text direction for a language. They are returned by the functions [CFLocaleGetLanguageCharacterDirection](<cflocalegetlanguagecharacterdirection(__).md>) and [CFLocaleGetLanguageLineDirection](<cflocalegetlanguagelinedirection(__).md>).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CFLocaleLanguageDirection
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCFLocaleLanguageDirectionUnknown](cflocalelanguagedirection/unknown.md)
- [kCFLocaleLanguageDirectionLeftToRight](cflocalelanguagedirection/lefttoright.md)
- [kCFLocaleLanguageDirectionRightToLeft](cflocalelanguagedirection/righttoleft.md)
- [kCFLocaleLanguageDirectionTopToBottom](cflocalelanguagedirection/toptobottom.md)
- [kCFLocaleLanguageDirectionBottomToTop](cflocalelanguagedirection/bottomtotop.md)

### Initializers

- [init(rawValue:)](<cflocalelanguagedirection/init(rawvalue_).md>)

## See Also

### Constants

- [Locale Property Keys](locale-property-keys.md) — Predefined locale keys used to get property values.
- [Locale Calendar Identifiers](locale-calendar-identifiers.md) — Predefined locale keys used to get calendar values—values for `kCFLocaleCalendarIdentifier`.
- [Locale Change Notification](locale-change-notification.md) — Identifier for notification sent if the current locale changes.
