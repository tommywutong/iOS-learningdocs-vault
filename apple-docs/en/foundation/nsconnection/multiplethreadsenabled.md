---
title: multipleThreadsEnabled
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsconnection/multiplethreadsenabled
source_url: 'https://developer.apple.com/documentation/foundation/nsconnection/multiplethreadsenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnection/multiplethreadsenabled.json'
content_hash: 'sha256:e3a9a1d9f91e1833'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnection](../nsconnection.md)

# multipleThreadsEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver supports requests from multiple threads.

<sub>Mac Catalyst, macOS</sub>

```objc
@property (readonly) BOOL multipleThreadsEnabled;
```

## Return Value

[true](../../swift/true.md) if the receiver supports requests from multiple threads.

## Discussion

[true](../../swift/true.md) if the receiver supports requests from multiple threads, otherwise [false](../../swift/false.md).

The default is [true](../../swift/true.md).

## See Also

### Running the Connection in a New Thread

- [runInNewThread](runinnewthread.md) — Creates and starts a new `NSThread` object and then runs the receiving connection in the new thread. _(deprecated)_
- [enableMultipleThreads](enablemultiplethreads.md) — Configures the receiver to allow requests from multiple threads to the remote object, without requiring each thread to each maintain its own connection. _(deprecated)_
- [addRunLoop:](addrunloop_.md) — Adds the specified run loop to the list of run loops the receiver monitors and from which it responds to requests. _(deprecated)_
- [removeRunLoop:](removerunloop_.md) — Removes a given `NSRunLoop` object from the list of run loops the receiver monitors and from which it responds to requests. _(deprecated)_
