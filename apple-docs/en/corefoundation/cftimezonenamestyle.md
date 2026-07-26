---
title: CFTimeZoneNameStyle
framework: Core Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cftimezonenamestyle
source_url: 'https://developer.apple.com/documentation/corefoundation/cftimezonenamestyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftimezonenamestyle.json'
content_hash: 'sha256:e2f9ecbd950391e4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTimeZoneNameStyle

<sub>Enumeration</sub>

Index type for constants used to specify styles of time zone names.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CFTimeZoneNameStyle
```

## Overview

For values, see [Time Zone Name Styles](time_zone_name_styles.md)

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [kCFTimeZoneNameStyleDaylightSaving](cftimezonenamestyle/daylightsaving.md) — Specifies the daylight saving name style; for example, “Central Daylight Time” for the Central time zone.
- [kCFTimeZoneNameStyleGeneric](cftimezonenamestyle/generic.md) — Specifies the generic name style, which does not distinguish between daylight saving and standard time; for example, “Central Time” for the Central time zone.
- [kCFTimeZoneNameStyleShortDaylightSaving](cftimezonenamestyle/shortdaylightsaving.md) — Specifies the short daylight saving name style; for example, “CDT” for the Central time zone.
- [kCFTimeZoneNameStyleShortGeneric](cftimezonenamestyle/shortgeneric.md) — Specifies the short generic name style, which does not distinguish between daylight saving and standard time; for example, “CT” for the Central time zone.
- [kCFTimeZoneNameStyleShortStandard](cftimezonenamestyle/shortstandard.md) — Specifies the short standard name style; for example, “CST” for the Central time zone.
- [kCFTimeZoneNameStyleStandard](cftimezonenamestyle/standard.md) — Specifies the standard name style; for example, “Central Standard Time” for the Central time zone.

### Initializers

- [init(rawValue:)](<cftimezonenamestyle/init(rawvalue_).md>)
