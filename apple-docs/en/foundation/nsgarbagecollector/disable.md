---
title: disable
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+（10.10 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsgarbagecollector/disable
source_url: 'https://developer.apple.com/documentation/foundation/nsgarbagecollector/disable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsgarbagecollector/disable.json'
content_hash: 'sha256:3f83ecf7447bc228'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSGarbageCollector](../nsgarbagecollector.md)

# disable

<sub>Instance Method</sub>

Temporarily disables collections.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) disable;
```

## Discussion

Invocations of this method can be nested. To reenable collection, you must send the collector an [enable](enable.md) message once for each invocation of this method.

## See Also

### Collection State

- [enable](enable.md) — Enables collection after collection has been disabled. _(deprecated)_
- [isEnabled](isenabled.md) — Returns a Boolean value that indicates whether garbage collection is currently enabled for the current process. _(deprecated)_
- [isCollecting](iscollecting.md) — Returns a Boolean value that indicates whether a collection is currently in progress. _(deprecated)_
