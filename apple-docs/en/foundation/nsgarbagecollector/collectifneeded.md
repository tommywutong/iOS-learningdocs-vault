---
title: collectIfNeeded
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+（10.10 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsgarbagecollector/collectifneeded
source_url: 'https://developer.apple.com/documentation/foundation/nsgarbagecollector/collectifneeded'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsgarbagecollector/collectifneeded.json'
content_hash: 'sha256:3b9e4981788b7ec5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSGarbageCollector](../nsgarbagecollector.md)

# collectIfNeeded

<sub>Instance Method</sub>

Tells the receiver to collect if memory consumption thresholds have been exceeded.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) collectIfNeeded;
```

## Discussion

You use this method to indicate to the collector that there is an opportunity to perform a collection. Collection is subject to interruption on user input.

## See Also

### Triggering Collection

- [collectExhaustively](collectexhaustively.md) — Tells the receiver to collect iteratively. _(deprecated)_
