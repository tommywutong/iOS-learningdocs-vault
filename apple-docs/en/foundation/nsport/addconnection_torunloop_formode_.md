---
title: 'addConnection:toRunLoop:forMode:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsport/addconnection:torunloop:formode:'
source_url: 'https://developer.apple.com/documentation/foundation/nsport/addconnection:torunloop:formode:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsport/addconnection%3Atorunloop%3Aformode%3A.json'
content_hash: 'sha256:2f77c544a8d8fc23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Port](../port.md)

# addConnection:toRunLoop:forMode:

<sub>Instance Method</sub>

Adds the receiver to the list of ports monitored by a given run loop for the given input mode.

> [!warning] Deprecated
> Use [NSXPCConnection](../nsxpcconnection.md) instead.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) addConnection:(NSConnection *) conn toRunLoop:(NSRunLoop *) runLoop forMode:(NSRunLoopMode) mode;
```

## Parameters

- `conn` — The connection object that invoked this method.

- `runLoop` — The run loop to which to add the receiver.

- `mode` — The run loop mode in which to add the receiver.

## Discussion

You should not call this method directly. The method is provided for subclassers who wish to provide their own custom types of `NSPort`. The `NSConnection` object, `conn`, calls this method at the appropriate times.

## See Also

### Related Documentation

- [- addPort:forMode:](<../runloop/add(__formode_)-6z982.md>) — Adds a port as an input source to the specified mode of the run loop.

### Creating connections

- [removeConnection:fromRunLoop:forMode:](removeconnection_fromrunloop_formode_.md) — Removes the receiver from the list of ports monitored by `runLoop` in the given input mode, `mode`. _(deprecated)_
