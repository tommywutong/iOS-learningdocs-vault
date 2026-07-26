---
title: 'init(position:objectSpecifier:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nspositionalspecifier/init(position:objectspecifier:)'
source_url: 'https://developer.apple.com/documentation/foundation/nspositionalspecifier/init(position:objectspecifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspositionalspecifier/init%28position%3Aobjectspecifier%3A%29.json'
content_hash: 'sha256:d08da09d3723dbca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPositionalSpecifier](../nspositionalspecifier.md)

# init(position:objectSpecifier:)

<sub>Initializer</sub>

Initializes a positional specifier with a given position relative to another given specifier.

<sub>Mac Catalyst, macOS</sub>

```swift
init(position: NSPositionalSpecifier.InsertionPosition, objectSpecifier specifier: NSScriptObjectSpecifier)
```

## Parameters

- `position` — The position for the new specifier relative to `specifier`.

- `specifier` — The reference specifier.

## Return Value

An initialized positional specifier with the position specified by `position` relative to the object specified by `specifier`.

## See Also

### Related Documentation

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
