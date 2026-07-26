---
title: 'addRunLoop:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsconnection/addrunloop:'
source_url: 'https://developer.apple.com/documentation/foundation/nsconnection/addrunloop:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnection/addrunloop%3A.json'
content_hash: 'sha256:ed55725ca1395117'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnection](../nsconnection.md)

# addRunLoop:

<sub>Instance Method</sub>

Adds the specified run loop to the list of run loops the receiver monitors and from which it responds to requests.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) addRunLoop:(NSRunLoop *) runloop;
```

## Parameters

- `runloop` — The run loop to add to the receiver.

## Discussion

This method is invoked automatically when a request comes in from a new run loop if [enableMultipleThreads](enablemultiplethreads.md) has been set.

## See Also

### Running the Connection in a New Thread

- [runInNewThread](runinnewthread.md) — Creates and starts a new `NSThread` object and then runs the receiving connection in the new thread. _(deprecated)_
- [enableMultipleThreads](enablemultiplethreads.md) — Configures the receiver to allow requests from multiple threads to the remote object, without requiring each thread to each maintain its own connection. _(deprecated)_
- [multipleThreadsEnabled](multiplethreadsenabled.md) — A Boolean value that indicates whether the receiver supports requests from multiple threads. _(deprecated)_
- [removeRunLoop:](removerunloop_.md) — Removes a given `NSRunLoop` object from the list of run loops the receiver monitors and from which it responds to requests. _(deprecated)_
