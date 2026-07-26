---
title: weakToStrongObjects()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmaptable/weaktostrongobjects()
source_url: 'https://developer.apple.com/documentation/foundation/nsmaptable/weaktostrongobjects()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmaptable/weaktostrongobjects%28%29.json'
content_hash: 'sha256:2e1ea72f0422e498'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMapTable](../nsmaptable.md)

# weakToStrongObjects()

<sub>Type Method</sub>

Returns a new map table object which has weak references to the keys and strong references to the values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func weakToStrongObjects() -> NSMapTable<KeyType, ObjectType>
```

## Return Value

A new map table object which has weak references to the keys and strong references to the values.

## Discussion

Use of weak-to-strong map tables is not recommended. The strong values for weak keys which get zeroed out continue to be maintained until the map table resizes itself.

## See Also

### Creating and Initializing a Map Table

- [- initWithKeyOptions:valueOptions:capacity:](<init(keyoptions_valueoptions_capacity_).md>) — Returns a map table, initialized with the given options.
- [+ mapTableWithKeyOptions:valueOptions:](<init(keyoptions_valueoptions_).md>) — Returns a new map table, initialized with the given options
- [- initWithKeyPointerFunctions:valuePointerFunctions:capacity:](<init(keypointerfunctions_valuepointerfunctions_capacity_).md>) — Returns a map table, initialized with the given functions.
- [+ strongToStrongObjectsMapTable](<strongtostrongobjects().md>) — Returns a new map table object which has strong references to the keys and values.
- [+ strongToWeakObjectsMapTable](<strongtoweakobjects().md>) — Returns a new map table object which has strong references to the keys and weak references to the values.
- [+ weakToWeakObjectsMapTable](<weaktoweakobjects().md>) — Returns a new map table object which has weak references to the keys and values.
- [NSMapTableOptions](../nsmaptableoptions.md) — Constants used as components in a bitfield to specify the behavior of elements (keys and values) in an `NSMapTable` object.
