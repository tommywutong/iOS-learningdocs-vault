---
title: 'init(keyPointerFunctions:valuePointerFunctions:capacity:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmaptable/init(keypointerfunctions:valuepointerfunctions:capacity:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmaptable/init(keypointerfunctions:valuepointerfunctions:capacity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmaptable/init%28keypointerfunctions%3Avaluepointerfunctions%3Acapacity%3A%29.json'
content_hash: 'sha256:a60c7c927c598c3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMapTable](../nsmaptable.md)

# init(keyPointerFunctions:valuePointerFunctions:capacity:)

<sub>Initializer</sub>

Returns a map table, initialized with the given functions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(keyPointerFunctions keyFunctions: NSPointerFunctions, valuePointerFunctions valueFunctions: NSPointerFunctions, capacity initialCapacity: Int)
```

## Parameters

- `keyFunctions` — The functions the map table uses to manage keys.

- `valueFunctions` — The functions the map table uses to manage values.

- `initialCapacity` — The initial capacity of the map table. This is just a hint; the map table may subsequently grow and shrink as required.

## Return Value

A map table, initialized with the given functions.

## See Also

### Creating and Initializing a Map Table

- [- initWithKeyOptions:valueOptions:capacity:](<init(keyoptions_valueoptions_capacity_).md>) — Returns a map table, initialized with the given options.
- [+ mapTableWithKeyOptions:valueOptions:](<init(keyoptions_valueoptions_).md>) — Returns a new map table, initialized with the given options
- [+ strongToStrongObjectsMapTable](<strongtostrongobjects().md>) — Returns a new map table object which has strong references to the keys and values.
- [+ weakToStrongObjectsMapTable](<weaktostrongobjects().md>) — Returns a new map table object which has weak references to the keys and strong references to the values.
- [+ strongToWeakObjectsMapTable](<strongtoweakobjects().md>) — Returns a new map table object which has strong references to the keys and weak references to the values.
- [+ weakToWeakObjectsMapTable](<weaktoweakobjects().md>) — Returns a new map table object which has weak references to the keys and values.
- [NSMapTableOptions](../nsmaptableoptions.md) — Constants used as components in a bitfield to specify the behavior of elements (keys and values) in an `NSMapTable` object.
