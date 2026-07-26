---
title: NSCreateZone
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nscreatezone
source_url: 'https://developer.apple.com/documentation/foundation/nscreatezone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscreatezone.json'
content_hash: 'sha256:6a82e1625a72f0f0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSCreateZone

<sub>Function</sub>

Creates a new zone.

> [!warning] Deprecated
> Zones are ignored on iOS and 64-bit runtime in macOS. You should not use zones in current development.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern NSZone *NSCreateZone(NSUInteger startSize, NSUInteger granularity, BOOL canFree);
```

## Return Value

A pointer to a new zone of `startSize` bytes, which will grow and shrink by `granularity` bytes. If `canFree` is 0, the allocator will never free memory, and `malloc` will be fast. Returns `NULL` if a new zone could not be created.

## See Also

### Managing Zones

- [NSRecycleZone](nsrecyclezone.md) — Frees memory in a zone. _(deprecated)_
- [NSSetZoneName](nssetzonename.md) — Sets the name of the specified zone. _(deprecated)_
- [NSZoneCalloc](nszonecalloc.md) — Allocates memory in a zone. _(deprecated)_
- [NSZoneFree](nszonefree.md) — Deallocates a block of memory in the specified zone. _(deprecated)_
- [NSZoneFromPointer](nszonefrompointer.md) — Gets the zone for a given block of memory. _(deprecated)_
- [NSZoneMalloc](nszonemalloc.md) — Allocates memory in a zone. _(deprecated)_
- [NSZoneName](nszonename.md) — Returns the name of the specified zone. _(deprecated)_
- [NSZoneRealloc](nszonerealloc.md) — Allocates memory in a zone. _(deprecated)_
- [NSDefaultMallocZone](nsdefaultmalloczone.md) — Returns the default zone. _(deprecated)_
