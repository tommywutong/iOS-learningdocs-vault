---
title: enable
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+（10.10 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsgarbagecollector/enable
source_url: 'https://developer.apple.com/documentation/foundation/nsgarbagecollector/enable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsgarbagecollector/enable.json'
content_hash: 'sha256:79faccaf914a9a02'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSGarbageCollector](../nsgarbagecollector.md)

# enable

<sub>Instance Method</sub>

Enables collection after collection has been disabled.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) enable;
```

## Discussion

This method balances a single invocation of [disable](disable.md). To reenable collection, this method must be invoked as many times as was [disable](disable.md).

## See Also

### Collection State

- [disable](disable.md) — Temporarily disables collections. _(deprecated)_
- [isEnabled](isenabled.md) — Returns a Boolean value that indicates whether garbage collection is currently enabled for the current process. _(deprecated)_
- [isCollecting](iscollecting.md) — Returns a Boolean value that indicates whether a collection is currently in progress. _(deprecated)_
