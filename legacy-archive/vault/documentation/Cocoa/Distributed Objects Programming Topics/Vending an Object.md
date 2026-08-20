---
title: Distributed Objects Programming Topics
apple_id: 10000102i
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: Foundation
published: '2017-06-07'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/Tasks/vending.html
archived_at: '2026-07-15T07:15:04.757959Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Distributed Objects Programming Topics](Introduction%20to%20Distributed%20Objects.md)


[Next](Getting%20a%20Vended%20Object.md)[Previous](Message%20Encapsulation.md)

For interprocess communication, you should use XPC instead; see _[XPC Services API Reference](https://developer.apple.com/documentation/xpc)_ for more information.

# Vending an Object

To make an object available to other applications, set it up as the root object of an `NSConnection` object and register the connection by name on the network. This code fragment vends `serverObject`, which is assumed to have a valid value of an object to be vended:

```
/* Assume serverObject has a valid value of an object to be vended. */
NSConnection *theConnection;

theConnection = [NSConnection defaultConnection];
[theConnection setRootObject:serverObject];
if ([theConnection registerName:@"server"] == NO) {
    /* Handle error. */
}
```

This fragment takes advantage of the fact that every thread has a default `NSConnection` object, which can be set up as a server. An `NSConnection` object can vend only one object, so the default `NSConnection` object might not be available. In this case, you can create additional `NSConnection` objects to vend objects with the usual `alloc` and `init` methods.

To advertise the connection to other threads and tasks, this fragment registers _theConnection_ under the name “`server`”. This causes the connection’s default receive port to be registered with the system’s default port name server as returned by the `NSPortNameServer` class method `systemDefaultPortNameServer`.

An `NSConnection` object set up this way is called a named connection. A named connection rarely has a channel to any other `NSConnection` object (in [Figure 1](Connections%20and%20Proxies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg43dcljzg4ztcmrnijbegrkkjfdug) and [Figure 2](Connections%20and%20Proxies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg43dcljzg4ztgnbnijbegr2djbdum) the named `NSConnection` objects are the circles labeled `s`). When a client contacts the server, a new pair of `NSConnection` objects is created specifically to handle communication between the two.

An `NSConnection` object adds itself to the current `NSRunLoop` instance when it is initialized. In the main thread of an application based on the Application Kit, the run loop is already running, so there is nothing more to do to vend an object. In a secondary thread or an application that does not use the `NSApplication` object, you have to start the run loop explicitly to capture incoming connection requests and messages. This is usually as simple as getting the current thread’s `NSRunLoop` instance and sending it a `run` message:

```
[[NSRunLoop currentRunLoop] run];
```

See [Configuring a Connection](Configuring%20a%20Connection.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg43dmlkcineuoqkcjbda) for more information on setting `NSConnection` objects up to handle requests.

[Next](Getting%20a%20Vended%20Object.md)[Previous](Message%20Encapsulation.md)

