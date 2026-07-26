---
title: mapTableWithStrongToWeakObjects
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.5+（10.8 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsmaptable/maptablewithstrongtoweakobjects
source_url: 'https://developer.apple.com/documentation/foundation/nsmaptable/maptablewithstrongtoweakobjects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmaptable/maptablewithstrongtoweakobjects.json'
content_hash: 'sha256:8e112f6301de8ffb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMapTable](../nsmaptable.md)

# mapTableWithStrongToWeakObjects

<sub>Type Method</sub>

Returns a new map table object which has strong references to the keys and weak references to the values.

> [!warning] Deprecated
> Use [+ strongToWeakObjectsMapTable](<strongtoweakobjects().md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (id) mapTableWithStrongToWeakObjects;
```

## Return Value

A new map table object which has strong references to the keys and weak references to the values.

## Discussion

`NSMapTable` objects created using this method do not support weak references under Automatic Reference Counting (ARC).

## See Also

### Deprecated

- [mapTableWithStrongToStrongObjects](maptablewithstrongtostrongobjects.md) — Returns a new map table object which has strong references to the keys and values. _(deprecated)_
- [mapTableWithWeakToStrongObjects](maptablewithweaktostrongobjects.md) — Returns a new map table object which has weak references to the keys and strong references to the values. _(deprecated)_
- [mapTableWithWeakToWeakObjects](maptablewithweaktoweakobjects.md) — Returns a new map table object which has weak references to the keys and values. _(deprecated)_
- [Legacy Map Table Implementation](../legacy-map-table-implementation.md)
