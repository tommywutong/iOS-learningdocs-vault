---
title: mapTableWithWeakToWeakObjects
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.5+（10.8 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsmaptable/maptablewithweaktoweakobjects
source_url: 'https://developer.apple.com/documentation/foundation/nsmaptable/maptablewithweaktoweakobjects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmaptable/maptablewithweaktoweakobjects.json'
content_hash: 'sha256:1ccde0a27cb584c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMapTable](../nsmaptable.md)

# mapTableWithWeakToWeakObjects

<sub>Type Method</sub>

Returns a new map table object which has weak references to the keys and values.

> [!warning] Deprecated
> Use [+ weakToWeakObjectsMapTable](<weaktoweakobjects().md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (id) mapTableWithWeakToWeakObjects;
```

## Return Value

A new map table object which has weak references to the keys and values.

## Discussion

`NSMapTable` objects created using this method do not support weak references under Automatic Reference Counting (ARC).

## See Also

### Deprecated

- [mapTableWithStrongToStrongObjects](maptablewithstrongtostrongobjects.md) — Returns a new map table object which has strong references to the keys and values. _(deprecated)_
- [mapTableWithWeakToStrongObjects](maptablewithweaktostrongobjects.md) — Returns a new map table object which has weak references to the keys and strong references to the values. _(deprecated)_
- [mapTableWithStrongToWeakObjects](maptablewithstrongtoweakobjects.md) — Returns a new map table object which has strong references to the keys and weak references to the values. _(deprecated)_
- [Legacy Map Table Implementation](../legacy-map-table-implementation.md)
