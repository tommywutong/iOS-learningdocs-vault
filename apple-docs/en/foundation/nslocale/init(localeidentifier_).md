---
title: 'init(localeIdentifier:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nslocale/init(localeidentifier:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/init(localeidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/init%28localeidentifier%3A%29.json'
content_hash: 'sha256:4c3649b51640461f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocale](../nslocale.md)

# init(localeIdentifier:)

<sub>Initializer</sub>

Initializes a locale using a given locale identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(localeIdentifier string: String)
```

## Parameters

- `string` — The identifier for the new locale.

## Return Value

The initialized locale.

## Discussion

This method is the designated initializer for this class.

## See Also

### Related Documentation

- [Internationalization and Localization Guide](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i)
- [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i)

### Initializing a Locale

- [- initWithCoder:](<init(coder_).md>) — Returns a locale initialized from data in the given unarchiver.
