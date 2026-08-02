---
title: Distributed Objects Programming Topics
apple_id: 10000102i
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: Foundation
published: '2017-06-07'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/Tasks/accessing.html
archived_at: '2026-07-15T07:15:01.761825Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Distributed Objects Programming Topics](Introduction%20to%20Distributed%20Objects.md)


[Next](Configuring%20a%20Connection.md)[Previous](Vending%20an%20Object.md)

For interprocess communication, you should use XPC instead; see _[XPC Services API Reference](https://developer.apple.com/documentation/xpc)_ for more information.

# Getting a Vended Object

An application gets a vended object by creating a proxy, or a stand-in, for that object in its own address space. The proxy forwards messages sent to it through its `NSConnection` object back to the vended object. An application can get a proxy for a vended object in two ways. First, the `rootProxyForConnectionWithRegisteredName:host:` class method returns the proxy directly:

```
id theProxy;
theProxy = [[NSConnection
    rootProxyForConnectionWithRegisteredName:@"server"
    host:nil] retain];
[theProxy setProtocolForProxy:@protocol(ServerProtocol)];
```

This message returns a proxy to the root object of the `NSConnection` object named “server”. The `nil` host name indicates that only the local host is searched for a registered `NSConnection` object; you can specify a specific host name to restrict the server to an identified host.

The invocation of `setProtocolForProxy:` informs the distributed objects system of the set of messages that _theProxy_ responds to. Normally, the first time a particular selector is forwarded by a proxy the `NSConnection` object must confirm the argument and return types with the real object. This can add significant overhead to distributed messages. Setting a protocol records this information so that no confirmation is needed for the messages in the protocol, and only the message forwarding costs are incurred.

Another way to get a proxy is to get an `NSConnection` object to the server and then ask for the proxy of its root object:

```
NSConnection *theConnection;
id theProxy;

theConnection = [NSConnection connectionWithRegisteredName:@"server"
                    host:nil];
theProxy = [[theConnection rootProxy] retain];
[theProxy setProtocolForProxy:@protocol(ServerProtocol)];
```

This is useful if you need to interact with the `NSConnection` object as well as the proxy. (However, note that _theConnection_ is not retained in this example.)

A named `NSConnection` object spawns a child `NSConnection` object to handle communication between two applications (`s` spawning `s/b` and `s/a` in [Figure 1](Connections%20and%20Proxies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg43dcljzg4ztcmrnijbegrkkjfdug)). Though the child `NSConnection` object does not have a name, it shares the root object and other configuration attributes of its parent, but not the delegate. You should not register a child `NSConnection` object with a name or change its root object, but you can change its other attributes, as described in [Configuring a Connection](Configuring%20a%20Connection.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg43dmlkcineuoqkcjbda).

By default, messages sent to a proxy object are forwarded over the connection synchronously; that is, the sender waits for the message to be processed and a reply received from the remote object. This occurs even for a method with a `void` return type, since the remote object can raise an exception that is passed back to the sender. The local thread or application thus blocks until the message completes execution. To avoid this, you can declare the method type as `oneway void` to cause asynchronous messaging. For more details, see the “Remote Messaging” section of The Runtime System in _[The Objective-C Programming Language](../The%20Objective-C%20Programming%20Language/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrt)_.

[Next](Configuring%20a%20Connection.md)[Previous](Vending%20an%20Object.md)

