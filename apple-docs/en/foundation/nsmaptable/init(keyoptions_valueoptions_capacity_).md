---
title: 'init(keyOptions:valueOptions:capacity:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmaptable/init(keyoptions:valueoptions:capacity:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmaptable/init(keyoptions:valueoptions:capacity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmaptable/init%28keyoptions%3Avalueoptions%3Acapacity%3A%29.json'
content_hash: 'sha256:fbaf1295a092e399'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMapTable](../nsmaptable.md)

# init(keyOptions:valueOptions:capacity:)

<sub>Initializer</sub>

Returns a map table, initialized with the given options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(keyOptions: NSPointerFunctions.Options = [], valueOptions: NSPointerFunctions.Options = [], capacity initialCapacity: Int)
```

## Parameters

- `keyOptions` — A bit field that specifies the options for the keys in the map table. For possible values, see [NSMapTableOptions](../nsmaptableoptions.md).

- `valueOptions` — A bit field that specifies the options for the values in the map table. For possible values, see [NSMapTableOptions](../nsmaptableoptions.md).

- `initialCapacity` — The initial capacity of the map table. This is just a hint; the map table may subsequently grow and shrink as required.

## Return Value

A map table initialized using the given options.

## Discussion

`values` must contain entries at all the indexes specified in `keys`.

## See Also

### Related Documentation

- [Collections Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Collections.html#//apple_ref/doc/uid/10000034i)

### Creating and Initializing a Map Table

- [+ mapTableWithKeyOptions:valueOptions:](<init(keyoptions_valueoptions_).md>) — Returns a new map table, initialized with the given options
- [- initWithKeyPointerFunctions:valuePointerFunctions:capacity:](<init(keypointerfunctions_valuepointerfunctions_capacity_).md>) — Returns a map table, initialized with the given functions.
- [+ strongToStrongObjectsMapTable](<strongtostrongobjects().md>) — Returns a new map table object which has strong references to the keys and values.
- [+ weakToStrongObjectsMapTable](<weaktostrongobjects().md>) — Returns a new map table object which has weak references to the keys and strong references to the values.
- [+ strongToWeakObjectsMapTable](<strongtoweakobjects().md>) — Returns a new map table object which has strong references to the keys and weak references to the values.
- [+ weakToWeakObjectsMapTable](<weaktoweakobjects().md>) — Returns a new map table object which has weak references to the keys and values.
- [NSMapTableOptions](../nsmaptableoptions.md) — Constants used as components in a bitfield to specify the behavior of elements (keys and values) in an `NSMapTable` object.
