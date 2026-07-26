---
title: init
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsoperation-init
source_url: 'https://developer.apple.com/documentation/foundation/nsoperation-init'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsoperation-init.json'
content_hash: 'sha256:ba7f564f1103efb7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Processes and Threads](processes-and-threads.md) · [Operation](operation.md)

# init

<sub>Article</sub>

Returns an initialized `NSOperation` object.

## Overview

Your custom subclasses must call this method. The default implementation initializes the object’s instance variables and prepares it for use. This method runs on the current thread—that is, the thread you use to allocate the operation object.

## See Also

### Related Documentation

- [Concurrency Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091)
