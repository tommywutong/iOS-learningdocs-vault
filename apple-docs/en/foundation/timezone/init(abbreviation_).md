---
title: 'init(abbreviation:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/timezone/init(abbreviation:)'
source_url: 'https://developer.apple.com/documentation/foundation/timezone/init(abbreviation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timezone/init%28abbreviation%3A%29.json'
content_hash: 'sha256:dd57c4bc5a671e69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [TimeZone](../timezone.md)

# init(abbreviation:)

<sub>Initializer</sub>

Returns a time zone identified by a given abbreviation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(abbreviation: String)
```

## Parameters

- `abbreviation` — The abbreviation for the time zone.

## Return Value

A time zone identified by abbreviation determined by resolving the abbreviation to an identifier using the abbreviation dictionary and then returning the time zone for that identifier. Returns `nil` if there is no match for abbreviation.

## Discussion

In general, you are discouraged from using abbreviations except for unique instances such as “GMT”. Time Zone abbreviations are not standardized and so a given abbreviation may have multiple meanings–for example, “EST” refers to Eastern Time in both the United States and Australia
