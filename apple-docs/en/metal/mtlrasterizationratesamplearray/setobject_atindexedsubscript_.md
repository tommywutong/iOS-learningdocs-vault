---
title: 'setObject:atIndexedSubscript:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrasterizationratesamplearray/setobject:atindexedsubscript:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratesamplearray/setobject:atindexedsubscript:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratesamplearray/setobject%3Aatindexedsubscript%3A.json'
content_hash: 'sha256:018f053629366bb3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateSampleArray](../mtlrasterizationratesamplearray.md)

# setObject:atIndexedSubscript:

<sub>Instance Method</sub>

Stores a sample value at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setObject:(NSNumber *) value atIndexedSubscript:(NSUInteger) index;
```

## Parameters

- `value` — The new value to set.

- `index` — The index of the element you want to set.

## Discussion

The method converts the value to a single precision floating-point value. If the index you specified is out of bounds, this method does nothing.

## See Also

### Accessing the array

- [objectAtIndexedSubscript:](objectatindexedsubscript_.md) — Retrieves the sample value at the specified index.
