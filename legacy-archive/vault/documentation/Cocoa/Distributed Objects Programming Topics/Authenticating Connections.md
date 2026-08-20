---
title: Distributed Objects Programming Topics
apple_id: 10000102i
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: Foundation
published: '2017-06-07'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/Tasks/delegate.html
archived_at: '2026-07-15T07:15:02.742636Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Distributed Objects Programming Topics](Introduction%20to%20Distributed%20Objects.md)


[Next](Making%20Substitutions%20During%20Message%20Encoding.md)[Previous](Handling%20Connection%20Errors.md)

For interprocess communication, you should use XPC instead; see _[XPC Services API Reference](https://developer.apple.com/documentation/xpc)_ for more information.

# Authenticating Connections

An `NSConnection` object can be assigned a delegate, which has two possible responsibilities: approving the formation of new connections, and authenticating messages that pass between `NSConnection` objects.

When a named `NSConnection` object is contacted by a client and forms a child `NSConnection` object to communicate with that client, it sends `connection:shouldMakeNewConnection:` to its delegate first to approve the new connection. If the delegate returns `NO` the connection is refused. This method is useful for limiting the load on a server. It’s also useful for setting the delegate of a child `NSConnection` object (since delegates are not shared automatically between parent and child).

Portable Distributed Objects adds message authentication to `NSConnection`’s API. Delegates in different applications can cooperate to validate the messages passing between them by implementing `authenticationDataForComponents:` and `authenticateComponents:withData:`. The first method requests an authentication stamp for an outgoing message, which is used by the second method to check the validity of the message when it is received.

`authenticationDataForComponents:` provides the packaged components for an outgoing network message in the form of `NSData` and `NSPort` objects. The delegate should use only the `NSData` objects to create the authentication stamp, by hashing the data, calculating a checksum, or some other method. The stamp should be small enough not to adversely affect network performance. The delegate in the receiving application receives an `authenticateComponents:withData:` message to confirm the message, and should recalculate the stamp for the components and compare it with the stamp provided. If it returns `YES` the message is forwarded; if it returns `NO`, an `NSFailedAuthenticationException` is raised and a message is logged to the console.

[Next](Making%20Substitutions%20During%20Message%20Encoding.md)[Previous](Handling%20Connection%20Errors.md)

