---
title: 'initWithReceivePort:sendPort:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsconnection/initwithreceiveport:sendport:'
source_url: 'https://developer.apple.com/documentation/foundation/nsconnection/initwithreceiveport:sendport:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnection/initwithreceiveport%3Asendport%3A.json'
content_hash: 'sha256:79111cfb8ee69443'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnection](../nsconnection.md)

# initWithReceivePort:sendPort:

<sub>Instance Method</sub>

Returns an `NSConnection` object initialized with given send and receive ports.

<sub>Mac Catalyst, macOS</sub>

```objc
- (instancetype) initWithReceivePort:(NSPort *) receivePort sendPort:(NSPort *) sendPort;
```

## Parameters

- `receivePort` — The receive port for the new connection.

- `sendPort` — The send port for the new connection.

## Return Value

An `NSConnection` object initialized with `receivePort` and `sendPort`. The returned object might be different than the original receiver.

## Discussion

The new `NSConnection` object adds `receivePort` to the current `NSRunLoop` object with `NSDefaultRunLoopMode` as the mode. If the application doesn’t use an `NSApplication` object to handle events, it needs to run the `NSRunLoop` object with one of its various `run...` messages.

This method posts an [NSConnectionDidInitializeNotification](../nsconnectiondidinitializenotification.md) once the connection is initialized.

The `receivePort` and `sendPort` parameters affect initialization as follows:

- If an `NSConnection` object with the same ports already exists, returns it and discards the original receiver.
- If an `NSConnection` object exists that uses the same ports, but switched in role, then the new `NSConnection` object communicates with it. Messages sent to a proxy held by either connection are forwarded through the other `NSConnection` object. This rule applies both within and across address spaces.

This behavior is useful for setting up distributed object connections between threads within an application. See [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i) for more information.

- If `receivePort` and `sendPort` are `nil`, deallocates the receiver and returns `nil`.
- If `receivePort` is `nil`, the `NSConnection` object allocates and uses a new port of the same class as `sendPort`.
- If `sendPort` is `nil` or if both ports are the same, the `NSConnection` object uses `receivePort` for both sending and receiving and is useful only for vending an object. Use [registerName:](registername_.md) and [rootObject](rootobject-c.property.md) to vend an object.
- If an `NSConnection` object exists that uses `receivePort` as both of its ports, it’s treated as the parent of the new `NSConnection` object, and its root object and all its configuration settings are applied to the new `NSConnection` object. You should neither register a name for nor set the root object of the new `NSConnection` object. See [Configuring a Connection](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/Tasks/configuring.html#//apple_ref/doc/uid/20000766) for more information.
- If `receivePort` and `sendPort` are different and neither is shared with another `NSConnection` object, the receiver can be used to vend an object as well as to communicate with other `NSConnection` objects. However, it has no other `NSConnection` object to communicate with until one is set up.
- The `receivePort` parameter can’t be shared by `NSConnection` objects in different threads.

This method is the designated initializer for the `NSConnection` class.

## See Also

### Related Documentation

- [defaultConnection](defaultconnection.md) — Returns the default `NSConnection` object for the current thread. _(deprecated)_

### Creating Instances

- [connectionWithReceivePort:sendPort:](connectionwithreceiveport_sendport_.md) — Returns an `NSConnection` object that communicates using given send and receive ports. _(deprecated)_
