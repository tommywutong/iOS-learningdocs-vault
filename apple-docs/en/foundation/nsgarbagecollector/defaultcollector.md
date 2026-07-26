---
title: defaultCollector
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.5+（10.10 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsgarbagecollector/defaultcollector
source_url: 'https://developer.apple.com/documentation/foundation/nsgarbagecollector/defaultcollector'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsgarbagecollector/defaultcollector.json'
content_hash: 'sha256:d2555280ac09c729'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSGarbageCollector](../nsgarbagecollector.md)

# defaultCollector

<sub>Type Method</sub>

Returns the default garbage collector.

<sub>Mac Catalyst, macOS</sub>

```objc
+ (id) defaultCollector;
```

## Return Value

The default garbage collector for the current process. Returns `nil` if the current process is not running with garbage collection.

## Discussion

There is at most one garbage collector for Cocoa within a single process.
