---
title: Distributed Objects Programming Topics
apple_id: 10000102i
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: Foundation
published: '2017-06-07'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/Concepts/messaging.html
archived_at: '2026-07-15T07:15:00.253082Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Distributed Objects Programming Topics](Introduction%20to%20Distributed%20Objects.md)


[Next](Vending%20an%20Object.md)[Previous](Ports%20and%20Name%20Servers.md)

For interprocess communication, you should use XPC instead; see _[XPC Services API Reference](https://developer.apple.com/documentation/xpc)_ for more information.

# Message Encapsulation

This section describes the classes used by the distributed objects system to encapsulate messages passed over a connection. Unless you are getting involved with the low-level details of distributed objects, you should never need to use these classes directly. `NSInvocation` and `NSMethodSignature`, however, have uses outside of distributed objects, so you may encounter them in other situations.

An `NSInvocation` object is an Objective-C message rendered static, an action turned into an object. `NSInvocation` objects are used to store and forward messages between objects and between applications, primarily by `NSTimer` and the distributed objects system. An `NSInvocation` object contains all the elements of an Objective-C message: a target, a selector, arguments, and the return value. Each of these elements can be set directly, and the return value is set automatically when the invocation is dispatched.

An `NSInvocation` object can be repeatedly dispatched to different targets; its arguments can be modified between dispatch for varying results; even its selector can be changed to another with the same method signature (argument and return types). This makes it useful for repeating messages with many arguments and variations; rather than retyping a slightly different expression for each message, you modify the `NSInvocation` object as needed each time before dispatching it to a new target.

For examples of how `NSInvocation` is used, see [Using NSInvocation](Using%20NSInvocation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg42dilkdjjbeeqkdjjea).

An `NSMethodSignature` object records type information for the arguments and return value of a method. It is used to forward messages that the receiving object does not respond to—most notably in the case of distributed objects. An `NSMethodSignature` object is typically created using `NSObject`'s `methodSignatureForSelector:` instance method. It is then used to create an `NSInvocation` object, which is passed as the argument to a `forwardInvocation:` message to send the invocation on to whatever other object can handle the message. In the default case, `NSObject` invokes `doesNotRecognizeSelector:`, which raises an exception. For distributed objects, the `NSInvocation` object is encoded using the information in the `NSMethodSignature` object and sent to the real object represented by the receiver of the message.

`NSPortCoder` is a concrete subclass of `NSCoder` used in the distributed objects system to transmit object proxies (and sometimes objects themselves) between `NSConnection` objects. An `NSPortCoder` object is always created and used by an `NSConnection` object; your code should never need to explicitly create or use one.

An `NSPortMessage` object defines a low level, operating-system independent type for interapplication (and interthread) messages. `NSPortMessage` objects are used primarily by the distributed objects system. You should implement interapplication communication using distributed objects whenever possible, and use `NSPortMessage` objects only when necessary.

An `NSPortMessage` object has three major parts: the send and receive ports, which are NSPorts that link the sender of the message to the receiver, and the components, which form the body of the message. The components are held as an `NSArray` object containing `NSData` and `NSPort` objects. `NSPortMessage`’s `sendBeforeDate:` message sends the components out through the send port; any replies to the message arrive on the receive port. See the NSPort class specification for information on handling incoming messages.

An `NSPortMessage` object can be initialized with a pair of `NSPort` objects and an `NSArray` instance containing components. An `NSPortMessage` object’s body can contain only `NSPort` objects or `NSData` objects. In the distributed objects system the byte/character arrays are usually encoded `NSInvocation` objects that are being forwarded from a proxy to the corresponding real object.

An `NSPortMessage` object also maintains a message identifier, which can be used to indicate the class of a message, such as an Objective-C method invocation, a connection request, an error, and so on. Use the `setMsgid:` and `msgid` methods to access the identifier.

`NSDistantObjectRequest` objects are used by the Distributed Objects system to help handle invocations between different processes. You should never create `NSDistantObjectRequest` objects directly. Unless you are getting involved with the low-level details of Distributed Objects, there should never be a need to access an `NSDistantObjectRequest` object. The distant object request for an incoming message is sent to the connection’s delegate if it implements `connection:handleRequest:`.

[Next](Vending%20an%20Object.md)[Previous](Ports%20and%20Name%20Servers.md)

