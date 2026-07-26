---
title: NSMapTableOptions
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmaptableoptions
source_url: 'https://developer.apple.com/documentation/foundation/nsmaptableoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmaptableoptions.json'
content_hash: 'sha256:3a732753f5e6d29a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMapTableOptions

<sub>Type Alias</sub>

Constants used as components in a bitfield to specify the behavior of elements (keys and values) in an `NSMapTable` object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias NSMapTableOptions = Int
```

## See Also

### Creating and Initializing a Map Table

- [- initWithKeyOptions:valueOptions:capacity:](<nsmaptable/init(keyoptions_valueoptions_capacity_).md>) — Returns a map table, initialized with the given options.
- [+ mapTableWithKeyOptions:valueOptions:](<nsmaptable/init(keyoptions_valueoptions_).md>) — Returns a new map table, initialized with the given options
- [- initWithKeyPointerFunctions:valuePointerFunctions:capacity:](<nsmaptable/init(keypointerfunctions_valuepointerfunctions_capacity_).md>) — Returns a map table, initialized with the given functions.
- [+ strongToStrongObjectsMapTable](<nsmaptable/strongtostrongobjects().md>) — Returns a new map table object which has strong references to the keys and values.
- [+ weakToStrongObjectsMapTable](<nsmaptable/weaktostrongobjects().md>) — Returns a new map table object which has weak references to the keys and strong references to the values.
- [+ strongToWeakObjectsMapTable](<nsmaptable/strongtoweakobjects().md>) — Returns a new map table object which has strong references to the keys and weak references to the values.
- [+ weakToWeakObjectsMapTable](<nsmaptable/weaktoweakobjects().md>) — Returns a new map table object which has weak references to the keys and values.
