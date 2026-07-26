---
title: runInNewThread
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsconnection/runinnewthread
source_url: 'https://developer.apple.com/documentation/foundation/nsconnection/runinnewthread'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnection/runinnewthread.json'
content_hash: 'sha256:4c0c3721effb7502'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnection](../nsconnection.md)

# runInNewThread

<sub>Instance Method</sub>

Creates and starts a new `NSThread` object and then runs the receiving connection in the new thread.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) runInNewThread;
```

## Discussion

If the newly created thread is the first to be detached from the current thread, this method posts an [NSWillBecomeMultiThreadedNotification](../nsnotification/name-swift.struct/nswillbecomemultithreaded.md) with `nil` to the default notification center.

## See Also

### Running the Connection in a New Thread

- [enableMultipleThreads](enablemultiplethreads.md) — Configures the receiver to allow requests from multiple threads to the remote object, without requiring each thread to each maintain its own connection. _(deprecated)_
- [multipleThreadsEnabled](multiplethreadsenabled.md) — A Boolean value that indicates whether the receiver supports requests from multiple threads. _(deprecated)_
- [addRunLoop:](addrunloop_.md) — Adds the specified run loop to the list of run loops the receiver monitors and from which it responds to requests. _(deprecated)_
- [removeRunLoop:](removerunloop_.md) — Removes a given `NSRunLoop` object from the list of run loops the receiver monitors and from which it responds to requests. _(deprecated)_
