---
title: Distributed Objects Programming Topics
apple_id: 10000102i
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: Foundation
published: '2017-06-07'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/Concepts/AboutDistributedObjects.html
archived_at: '2026-07-15T07:14:56.724857Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Distributed Objects Programming Topics](Introduction%20to%20Distributed%20Objects.md)


[Next](Distributed%20Objects%20Architecture.md)[Previous](Introduction%20to%20Distributed%20Objects.md)

For interprocess communication, you should use XPC instead; see _[XPC Services API Reference](https://developer.apple.com/documentation/xpc)_ for more information.

# About Distributed Objects

Cocoa’s distributed objects architecture enables objects in different threads or tasks, perhaps on different machines, to transparently send messages to each other. While there are many ways for threads and tasks to communicate with one another, distributed objects hides the mechanism behind the standard Objective-C messaging mechanism. The syntax of local and remote messages are identical.

Remote messages can be sent synchronously or asynchronously. When sending a synchronous message, the sender waits for a reply, blocking its execution, just like a local message. When sending an asynchronous message, the sender continues executing without waiting for a reply; any response from the remote object is ignored.

Distributed objects can be used to divide a complex task into separate code paths that run independently, but can still cooperate as if they were running together. For example, an application can be divided into a graphical front end and a computational back end. The front end can accept all user input and tell the back end to perform various actions. The back end can handle the “heavy lifting” and inform the front end when it can update the user interface with the results. Because the front and back ends run independently, the front end can continue interacting with the user while the back end is busy.

Distributed objects can also be used to implement distributed computing, or parallel processing. If a large job is split into many smaller jobs that are distributed on a multiprocessor machine or on multiple machines, you can harness the combined computational power of all the processors to complete the job. Distributed objects simplifies the application architecture and the communication between its distributed parts.

Cocoa allows distributed objects to communicate over Mach ports, message ports, and sockets. The first two are restricted to communication on a single machine, but sockets can communicate over large networks, including the internet.

Before an object can receive messages from other processes, it must allocate a communication port and make it available to others. Cocoa provides access to name servers for each supported type of communication port. An object can register its port with the appropriate name server to allow other processes to find it. In the case of sockets, you can also publish the object’s socket as a Bonjour network service (see the Cocoa Programming Topic _[Bonjour Overview](../Bonjour%20Overview/About%20Bonjour.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeyts2i)_). Other processes that want to communicate with this object can then look up the object’s communication port, requesting it by name, and attach distributed object connections to it.

For details on how the Objective-C language and runtime enables distributed objects, see the “Remote Messaging” section of The Runtime System in _[The Objective-C Programming Language](../The%20Objective-C%20Programming%20Language/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrt)_.

[Next](Distributed%20Objects%20Architecture.md)[Previous](Introduction%20to%20Distributed%20Objects.md)

