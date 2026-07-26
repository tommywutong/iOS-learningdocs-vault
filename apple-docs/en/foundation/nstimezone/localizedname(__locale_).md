---
title: 'localizedName(_:locale:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nstimezone/localizedname(_:locale:)'
source_url: 'https://developer.apple.com/documentation/foundation/nstimezone/localizedname(_:locale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimezone/localizedname%28_%3Alocale%3A%29.json'
content_hash: 'sha256:be215a006ac21a27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTimeZone](../nstimezone.md)

# localizedName(_:locale:)

<sub>Instance Method</sub>

Returns the localized name of the time zone.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func localizedName(_ style: NSTimeZone.NameStyle, locale: Locale?) -> String?
```

## Parameters

- `style` — The format style for the returned string.

- `locale` — The locale for which to format the name.

## Return Value

The name of the receiver localized for `locale` using `style`.

## See Also

### Describing Time Zones

- [description](description.md) — A textual description of the time zone including the name, abbreviation, offset from GMT, and whether or not daylight saving time is currently in effect.
