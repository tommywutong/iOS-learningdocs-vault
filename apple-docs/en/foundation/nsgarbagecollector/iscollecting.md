---
title: isCollecting
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+（10.6 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsgarbagecollector/iscollecting
source_url: 'https://developer.apple.com/documentation/foundation/nsgarbagecollector/iscollecting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsgarbagecollector/iscollecting.json'
content_hash: 'sha256:bc99ff8bfade184b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSGarbageCollector](../nsgarbagecollector.md)

# isCollecting

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether a collection is currently in progress.

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) isCollecting;
```

## Return Value

[true](../../swift/true.md) if a collection is currently in progress, otherwise [false](../../swift/false.md).

## See Also

### Collection State

- [disable](disable.md) — Temporarily disables collections. _(deprecated)_
- [enable](enable.md) — Enables collection after collection has been disabled. _(deprecated)_
- [isEnabled](isenabled.md) — Returns a Boolean value that indicates whether garbage collection is currently enabled for the current process. _(deprecated)_
