---
title: 'CFSocketSetSocketFlags(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsocketsetsocketflags(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketsetsocketflags(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketsetsocketflags%28_%3A_%3A%29.json'
content_hash: 'sha256:fa9e00af97c05188'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSocketSetSocketFlags(_:_:)

<sub>Function</sub>

Sets flags that control certain behaviors of a CFSocket object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSocketSetSocketFlags(_ s: CFSocket!, _ flags: CFOptionFlags)
```

## Parameters

- `s` — The CFSocket object to modify.

- `flags` — A bitwise-OR combination of flags controlling the behavior of `s`. See [CFSocket Flags](1560944-cfsocket-flags.md) for the list of available flags.

## Discussion

The `flags` argument controls whether callbacks of a given type are automatically reenabled after they are triggered, and whether the underlying native socket is closed when `s` is invalidated.

To set and clear flags, you must set and mask bits in the flag set, respectively. First, call [CFSocketGetSocketFlags](<cfsocketgetsocketflags(__).md>), then modify the value returned. For example:

```objc
    CFOptionFlags sockopt = CFSocketGetSocketFlags (mysock );
 
    /* Set the read callback to be automatically reenabled. */
    sockopt |= kCFSocketAutomaticallyReenableReadCallBack;
 
    /* Clear the close-on-invalidate flag. */
    sockopt &= ~kCFSocketCloseOnInvalidate;
 
    CFSocketSetSocketFlags(s, sockopt);
```

By default `kCFSocketReadCallBack`, `kCFSocketAcceptCallBack`, and `kCFSocketDataCallBack` callbacks are automatically reenabled after they are triggered, whereas `kCFSocketWriteCallBack` callbacks are not; `kCFSocketConnectCallBack` callbacks can only occur once, so they cannot be reenabled.

If a callback is automatically reenabled, it is called every time the condition becomes true. For example, a read callback is called as long as there is data on the socket waiting to be read. If a callback is not automatically reenabled, then it gets called exactly once, and is not called again until you manually reenable that callback by calling [CFSocketEnableCallBacks](<cfsocketenablecallbacks(____).md>).

Be careful about automatically reenabling read and write callbacks. If you do, the callbacks will be called repeatedly as long as the socket remains readable or writable, respectively.

Be sure to set these flags only for callback types that your CFSocket object actually possesses; the result of setting them for other callback types is undefined.

By default the underlying native socket is closed when `s` is invalidated. To disable that, clear (zero) the `kCFSocketCloseOnInvalidate` flag. This can be useful when you want to destroy a CFSocket object but continue to use the underlying native socket. The CFSocket object must still be invalidated when you no longer need it.

Do not close the underlying native socket without invalidating the CFSocket object first.

## See Also

### Configuring Sockets

- [CFSocketCopyAddress](<cfsocketcopyaddress(__).md>) — Returns the local address of a CFSocket object.
- [CFSocketCopyPeerAddress](<cfsocketcopypeeraddress(__).md>) — Returns the remote address to which a CFSocket object is connected.
- [CFSocketDisableCallBacks](<cfsocketdisablecallbacks(____).md>) — Disables the callback function of a CFSocket object for certain types of socket activity.
- [CFSocketEnableCallBacks](<cfsocketenablecallbacks(____).md>) — Enables the callback function of a CFSocket object for certain types of socket activity.
- [CFSocketGetContext](<cfsocketgetcontext(____).md>) — Returns the context information for a CFSocket object.
- [CFSocketGetNative](<cfsocketgetnative(__).md>) — Returns the native socket associated with a CFSocket object.
- [CFSocketGetSocketFlags](<cfsocketgetsocketflags(__).md>) — Returns flags that control certain behaviors of a CFSocket object.
- [CFSocketSetAddress](<cfsocketsetaddress(____).md>) — Binds a local address to a CFSocket object and configures it for listening.
