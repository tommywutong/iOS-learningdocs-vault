---
title: 'minusSet:'
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscountedset-minusset
source_url: 'https://developer.apple.com/documentation/foundation/nscountedset-minusset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscountedset-minusset.json'
content_hash: 'sha256:4a2235bb30816b62'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Collections](collections.md) · [NSCountedSet](nscountedset.md)

# minusSet:

<sub>Article</sub>

Removes each object in another given set from the receiving set, if present.

## Overview

For each object in `otherSet` that is present in the set, this method decrements the associated count. If the count for an object is decremented to `0`, the object is removed from the set.

## See Also

### Related Documentation

- [NSCountedSet](nscountedset.md) — A mutable, unordered collection of distinct objects that may appear more than once in the collection.
