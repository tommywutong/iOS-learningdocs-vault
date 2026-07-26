---
title: 'init(coder:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nslocale/init(coder:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/init(coder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/init%28coder%3A%29.json'
content_hash: 'sha256:cec84dc435e1a245'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocale](../nslocale.md)

# init(coder:)

<sub>Initializer</sub>

Returns a locale initialized from data in the given unarchiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(coder: NSCoder)
```

## Parameters

- `coder` — The decoder to use during initialization.

## Return Value

The initialized locale.

## See Also

### Related Documentation

- [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i)

### Initializing a Locale

- [- initWithLocaleIdentifier:](<init(localeidentifier_).md>) — Initializes a locale using a given locale identifier.
