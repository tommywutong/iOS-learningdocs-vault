---
title: PreferenceKey
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/preferencekey
source_url: 'https://developer.apple.com/documentation/swiftui/preferencekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/preferencekey.json'
content_hash: 'sha256:70b6197e97743d64'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PreferenceKey

<sub>Protocol</sub>

A named value produced by a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol PreferenceKey
```

## Overview

A view with multiple children automatically combines its values for a given preference into a single value visible to its ancestors.

## Relationships

- **Conforming Types**: [PreferredColorSchemeKey](preferredcolorschemekey.md), [LayoutKey](text/layoutkey.md)

## Topics

### Getting the default value

- [defaultValue](preferencekey/defaultvalue.md) — The default value of the preference.
- [Value](preferencekey/value.md) — The type of value produced by this preference.

### Combining preferences

- [reduce(value:nextValue:)](<preferencekey/reduce(value_nextvalue_).md>) — Combines a sequence of values by modifying the previously-accumulated value with the result of a closure that provides the next value.
