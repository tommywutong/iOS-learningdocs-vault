---
title: 'objectAtIndexedSubscript:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrasterizationratesamplearray/objectatindexedsubscript:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratesamplearray/objectatindexedsubscript:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratesamplearray/objectatindexedsubscript%3A.json'
content_hash: 'sha256:1cd2354a6f0a8289'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateSampleArray](../mtlrasterizationratesamplearray.md)

# objectAtIndexedSubscript:

<sub>Instance Method</sub>

Retrieves the sample value at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (NSNumber *) objectAtIndexedSubscript:(NSUInteger) index;
```

## Parameters

- `index` — The index of the element to retrieve.

## Return Value

An [NSNumber](../../foundation/nsnumber.md) object. It contains the value of the sample at the specified index or `0` if the index you specified is out of bounds.

## See Also

### Accessing the array

- [setObject:atIndexedSubscript:](setobject_atindexedsubscript_.md) — Stores a sample value at the specified index.
