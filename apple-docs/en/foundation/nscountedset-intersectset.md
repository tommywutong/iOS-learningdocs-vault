---
title: 'intersectSet:'
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscountedset-intersectset
source_url: 'https://developer.apple.com/documentation/foundation/nscountedset-intersectset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscountedset-intersectset.json'
content_hash: 'sha256:8907966766b750df'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Collections](collections.md) · [NSCountedSet](nscountedset.md)

# intersectSet:

<sub>Article</sub>

Removes from the receiving set each object that isn’t a member of another given set.

## Overview

For each object in the set that is not present in `otherSet`, this method decrements the associated count. If the count for an object is decremented to `0`, the object is removed from the set.

## See Also

### Related Documentation

- [NSCountedSet](nscountedset.md) — A mutable, unordered collection of distinct objects that may appear more than once in the collection.
