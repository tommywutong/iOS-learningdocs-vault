---
title: 'allocWithZone:'
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsport-allocwithzone
source_url: 'https://developer.apple.com/documentation/foundation/nsport-allocwithzone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsport-allocwithzone.json'
content_hash: 'sha256:3037c411b187bdb2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Streams, Sockets, and Ports](streams-sockets-and-ports.md) · [Port](port.md)

# allocWithZone:

<sub>Article</sub>

Returns an instance of the `NSMachPort` class.

## Overview

For backward compatibility on Mach, [allocWithZone:](nsport-allocwithzone.md) returns an instance of the `NSMachPort` class when sent to the `NSPort` class. Otherwise, it returns an instance of a concrete subclass that can be used for messaging between threads or processes on the local machine, or, in the case of `NSSocketPort`, between processes on separate machines.

## See Also

### Related Documentation

- [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)
- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)
