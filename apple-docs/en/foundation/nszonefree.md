---
title: NSZoneFree
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nszonefree
source_url: 'https://developer.apple.com/documentation/foundation/nszonefree'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nszonefree.json'
content_hash: 'sha256:3f846a3df4100e3e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSZoneFree

<sub>Function</sub>

Deallocates a block of memory in the specified zone.

> [!warning] Deprecated
> Zones are ignored on iOS and 64-bit runtime in macOS. You should not use zones in current development.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void NSZoneFree(NSZone *zone, void *ptr);
```

## Discussion

Returns memory to the `zone` from which it was allocated. The standard C function `free` does the same, but spends time finding which zone the memory belongs to.

## See Also

### Managing Zones

- [NSCreateZone](nscreatezone.md) — Creates a new zone. _(deprecated)_
- [NSRecycleZone](nsrecyclezone.md) — Frees memory in a zone. _(deprecated)_
- [NSSetZoneName](nssetzonename.md) — Sets the name of the specified zone. _(deprecated)_
- [NSZoneCalloc](nszonecalloc.md) — Allocates memory in a zone. _(deprecated)_
- [NSZoneFromPointer](nszonefrompointer.md) — Gets the zone for a given block of memory. _(deprecated)_
- [NSZoneMalloc](nszonemalloc.md) — Allocates memory in a zone. _(deprecated)_
- [NSZoneName](nszonename.md) — Returns the name of the specified zone. _(deprecated)_
- [NSZoneRealloc](nszonerealloc.md) — Allocates memory in a zone. _(deprecated)_
- [NSDefaultMallocZone](nsdefaultmalloczone.md) — Returns the default zone. _(deprecated)_
