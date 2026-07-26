---
title: mapTableWithStrongToStrongObjects
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.5+（10.8 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsmaptable/maptablewithstrongtostrongobjects
source_url: 'https://developer.apple.com/documentation/foundation/nsmaptable/maptablewithstrongtostrongobjects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmaptable/maptablewithstrongtostrongobjects.json'
content_hash: 'sha256:a143416b813c908f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMapTable](../nsmaptable.md)

# mapTableWithStrongToStrongObjects

<sub>Type Method</sub>

Returns a new map table object which has strong references to the keys and values.

> [!warning] Deprecated
> Use [+ strongToStrongObjectsMapTable](<strongtostrongobjects().md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (id) mapTableWithStrongToStrongObjects;
```

## Return Value

A new map table object which has strong references to the keys and values.

## See Also

### Deprecated

- [mapTableWithWeakToStrongObjects](maptablewithweaktostrongobjects.md) — Returns a new map table object which has weak references to the keys and strong references to the values. _(deprecated)_
- [mapTableWithStrongToWeakObjects](maptablewithstrongtoweakobjects.md) — Returns a new map table object which has strong references to the keys and weak references to the values. _(deprecated)_
- [mapTableWithWeakToWeakObjects](maptablewithweaktoweakobjects.md) — Returns a new map table object which has weak references to the keys and values. _(deprecated)_
- [Legacy Map Table Implementation](../legacy-map-table-implementation.md)
