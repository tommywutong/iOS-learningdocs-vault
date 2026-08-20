---
title: Distributed Objects Programming Topics
apple_id: 10000102i
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: Foundation
published: '2017-06-07'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/Tasks/errors.html
archived_at: '2026-07-15T07:15:03.248331Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Distributed Objects Programming Topics](Introduction%20to%20Distributed%20Objects.md)


[Next](Authenticating%20Connections.md)[Previous](Configuring%20a%20Connection.md)

For interprocess communication, you should use XPC instead; see _[XPC Services API Reference](https://developer.apple.com/documentation/xpc)_ for more information.

# Handling Connection Errors

`NSConnection` objects make use of network resources that can become unavailable at any time, either temporarily or permanently.

Due to heavy network traffic or a busy process, individual messages over a connection may get delayed or lost, causing a timeout error. A timeout error can happen for an outgoing message, meaning the message was never sent to its recipient, or for a reply to a message successfully sent, meaning either that the message failed to reach its recipient or that the reply could not be delivered back to the original sender. `NSConnection` raises an `NSPortTimeoutException` if after a preset time period either the outgoing message is not sent or the reply message is not received. You set the durations for these timeouts with the `NSConnection` instance methods `setRequestTimeout`: and `setReplyTimeout:`. An application can put an exception handler in place for critical messages, and if an `NSPortTimeoutException` is raised it can send the message again, check that the server (or client) is still running or take whatever other action it needs to recover.

In the extreme case, a connection may become permanently severed. When a process using distributed objects crashes, for example, the objects in that process that have been vended to other applications simply cease to exist. In such a case, the `NSConnection` objects handling those objects invalidate themselves and post an `NSConnectionDidDieNotification` to any observers. This notification allows objects to clean up their state as much as possible in the face of an error.

To register for the `NSConnectionDidDieNotification`, add an observer to the default `NSNotificationCenter`:

```
[[NSNotificationCenter defaultCenter] addObserver:proxyUser
        selector:@selector(connectionDidDie:)
        name:NSConnectionDidDieNotification
        object:serverConnection];
```

The fragment above registers the _proxyUser_ object to receive a `connectionDidDie:` message when the _serverConnection_ object in the application posts an `NSConnectionDidDieNotification`. This allows it to release any proxies it holds and to handle the error as gracefully as possible. See _[Notification Programming Topics](../Notification%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2dg2i)_ for more information on notifications.

One limitation of `NSConnectionDidDieNotification`, however, is that an `NSConnection` object attached to a remote `NSSocketPort` object (the send port) cannot detect when the remote port becomes invalid. This is true even if the remote port is on the same machine. Therefore, an `NSConnection` object cannot post an `NSConnectionDidDieNotification` when the connection is lost. Instead, you must detect the timeout error when the next message is sent and invalidate the `NSSocketPort` object yourself.

In the case of a client-server model wherein the server never messages the client, the server can accumulate `NSConnection` and `NSSocketPort` objects when client applications quit without explicitly logging out from the server. The server, therefore, does not realize that the connection can be closed and released, resulting in memory leaks. One workaround for this situation involves the client vending an object to the server, allowing the server to “ping”, or message, the client if the client has been silent for an excessive period of time. If the client fails to respond, the server can assume the client is no longer alive and it can close the connection.

[Next](Authenticating%20Connections.md)[Previous](Configuring%20a%20Connection.md)

