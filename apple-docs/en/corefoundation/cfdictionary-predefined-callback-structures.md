---
title: Predefined Callback Structures
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfdictionary-predefined-callback-structures
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionary-predefined-callback-structures'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionary-predefined-callback-structures.json'
content_hash: 'sha256:9d59ccf9f3f9ae3f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFDictionary](cfdictionary.md)

# Predefined Callback Structures

<sub>API Collection</sub>

CFDictionary provides some predefined callbacks for your convenience.

## Topics

### Constants

- [kCFCopyStringDictionaryKeyCallBacks](kcfcopystringdictionarykeycallbacks.md) — Predefined [CFDictionaryKeyCallBacks](cfdictionarykeycallbacks.md) structure containing a set of callbacks appropriate for use when the keys of a CFDictionary are all CFString objects, which may be mutable and need to be copied in order to serve as constant keys for the values in the dictionary.
- [kCFTypeDictionaryKeyCallBacks](kcftypedictionarykeycallbacks.md) — Predefined [CFDictionaryKeyCallBacks](cfdictionarykeycallbacks.md) structure containing a set of callbacks appropriate for use when the keys of a CFDictionary are all CFType-derived objects.
- [kCFTypeDictionaryValueCallBacks](kcftypedictionaryvaluecallbacks.md) — Predefined [CFDictionaryValueCallBacks](cfdictionaryvaluecallbacks.md) structure containing a set of callbacks appropriate for use when the values in a CFDictionary are all CFType-derived objects.
