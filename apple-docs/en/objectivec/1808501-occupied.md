---
title: occupied
framework: Objective-C Runtime
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/1808501-occupied
source_url: 'https://developer.apple.com/documentation/objectivec/1808501-occupied'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/1808501-occupied.json'
content_hash: 'sha256:93d653657c4b0908'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [Objective-C Runtime](objective-c-runtime.md) · [objc_cache](objc_cache.md)

# occupied

<sub>Article</sub>

An integer specifying the total number of occupied cache buckets.

## See Also

### Fields

- [mask](1808499-mask.md) — An integer specifying the total number of allocated cache buckets (minus one). During method lookup, the Objective-C runtime uses this field to determine the index at which to begin a linear search of the `buckets` array. A pointer to a method’s selector is masked against this field using a logical AND operation (`index = (mask & selector))`. This serves as a simple hashing algorithm.
- [buckets](1808503-buckets.md) — An array of pointers to [Method](method.md) data structures. This array may contain no more than `mask + 1` items. Note that pointers may be `NULL`, indicating that the cache bucket is unoccupied, and occupied buckets may not be contiguous. This array may grow over time.
