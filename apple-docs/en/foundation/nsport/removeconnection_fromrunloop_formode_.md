---
title: 'removeConnection:fromRunLoop:forMode:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsport/removeconnection:fromrunloop:formode:'
source_url: 'https://developer.apple.com/documentation/foundation/nsport/removeconnection:fromrunloop:formode:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsport/removeconnection%3Afromrunloop%3Aformode%3A.json'
content_hash: 'sha256:3eaf222dedb6aa48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Port](../port.md)

# removeConnection:fromRunLoop:forMode:

<sub>Instance Method</sub>

Removes the receiver from the list of ports monitored by `runLoop` in the given input mode, `mode`.

> [!warning] Deprecated
> Use [NSXPCConnection](../nsxpcconnection.md) instead.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) removeConnection:(NSConnection *) conn fromRunLoop:(NSRunLoop *) runLoop forMode:(NSRunLoopMode) mode;
```

## Parameters

- `conn` — The connection object that invoked this method.

- `runLoop` — The run loop to which to add the receiver.

- `mode` — The run loop mode in which to add the receiver.

## Discussion

You should not call this method directly. The method is provided for subclassers who wish to provide their own custom types of `NSPort`. The `NSConnection` object, `conn`, calls this method at the appropriate times.

## See Also

### Creating connections

- [addConnection:toRunLoop:forMode:](addconnection_torunloop_formode_.md) — Adds the receiver to the list of ports monitored by a given run loop for the given input mode. _(deprecated)_
