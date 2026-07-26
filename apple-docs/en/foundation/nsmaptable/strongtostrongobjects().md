---
title: strongToStrongObjects()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmaptable/strongtostrongobjects()
source_url: 'https://developer.apple.com/documentation/foundation/nsmaptable/strongtostrongobjects()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmaptable/strongtostrongobjects%28%29.json'
content_hash: 'sha256:9ed26020bde2ca29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMapTable](../nsmaptable.md)

# strongToStrongObjects()

<sub>Type Method</sub>

Returns a new map table object which has strong references to the keys and values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func strongToStrongObjects() -> NSMapTable<KeyType, ObjectType>
```

## Return Value

A new map table object which has strong references to the keys and values.

## See Also

### Creating and Initializing a Map Table

- [- initWithKeyOptions:valueOptions:capacity:](<init(keyoptions_valueoptions_capacity_).md>) — Returns a map table, initialized with the given options.
- [+ mapTableWithKeyOptions:valueOptions:](<init(keyoptions_valueoptions_).md>) — Returns a new map table, initialized with the given options
- [- initWithKeyPointerFunctions:valuePointerFunctions:capacity:](<init(keypointerfunctions_valuepointerfunctions_capacity_).md>) — Returns a map table, initialized with the given functions.
- [+ weakToStrongObjectsMapTable](<weaktostrongobjects().md>) — Returns a new map table object which has weak references to the keys and strong references to the values.
- [+ strongToWeakObjectsMapTable](<strongtoweakobjects().md>) — Returns a new map table object which has strong references to the keys and weak references to the values.
- [+ weakToWeakObjectsMapTable](<weaktoweakobjects().md>) — Returns a new map table object which has weak references to the keys and values.
- [NSMapTableOptions](../nsmaptableoptions.md) — Constants used as components in a bitfield to specify the behavior of elements (keys and values) in an `NSMapTable` object.
