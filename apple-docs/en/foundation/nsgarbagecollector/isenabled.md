---
title: isEnabled
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+（10.10 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsgarbagecollector/isenabled
source_url: 'https://developer.apple.com/documentation/foundation/nsgarbagecollector/isenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsgarbagecollector/isenabled.json'
content_hash: 'sha256:d4982e66bccde6f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSGarbageCollector](../nsgarbagecollector.md)

# isEnabled

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether garbage collection is currently enabled for the current process.

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) isEnabled;
```

## Return Value

[true](../../swift/true.md) if garbage collection is enabled for the current process, otherwise [false](../../swift/false.md).

## Discussion

This method returns [false](../../swift/false.md) if garbage collection is on, but has been temporarily suspended (using [disable](disable.md)).

To check whether the current process is using garbage collection check the result of `[NSGarbageCollector defaultCollector]`. If [defaultCollector](defaultcollector.md) is `nil`, then garbage collection is permanently off. If [defaultCollector](defaultcollector.md) is not `nil`, then the current process is using garbage collection—you can then use `isEnabled` to determine whether or not the collector is actually allowed to run right now.

## See Also

### Collection State

- [disable](disable.md) — Temporarily disables collections. _(deprecated)_
- [enable](enable.md) — Enables collection after collection has been disabled. _(deprecated)_
- [isCollecting](iscollecting.md) — Returns a Boolean value that indicates whether a collection is currently in progress. _(deprecated)_
