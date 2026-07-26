---
title: collectExhaustively
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+（10.10 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsgarbagecollector/collectexhaustively
source_url: 'https://developer.apple.com/documentation/foundation/nsgarbagecollector/collectexhaustively'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsgarbagecollector/collectexhaustively.json'
content_hash: 'sha256:23ed80b6718b19f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSGarbageCollector](../nsgarbagecollector.md)

# collectExhaustively

<sub>Instance Method</sub>

Tells the receiver to collect iteratively.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) collectExhaustively;
```

## Discussion

You use this method to indicate to the collector that it should perform an exhaustive collection. Collection is subject to interruption on user input.

## See Also

### Triggering Collection

- [collectIfNeeded](collectifneeded.md) — Tells the receiver to collect if memory consumption thresholds have been exceeded. _(deprecated)_
