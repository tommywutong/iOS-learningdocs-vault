---
title: Distributed Objects Programming Topics
apple_id: 10000102i
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: Foundation
published: '2017-06-07'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/Concepts/ports.html
archived_at: '2026-07-15T07:15:00.766960Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Distributed Objects Programming Topics](Introduction%20to%20Distributed%20Objects.md)


[Next](Message%20Encapsulation.md)[Previous](Connections%20and%20Proxies.md)

For interprocess communication, you should use XPC instead; see _[XPC Services API Reference](https://developer.apple.com/documentation/xpc)_ for more information.

# Ports and Name Servers

Ports are the low-level communication channels that transmit and receive the raw data between threads and processes. Ports can be assigned names and advertised to other processes through port name servers. Each type of port has its own port name server.

An `NSPort` object represents a communication channel to or from another `NSPort` object, which typically resides in a different thread or task. The distributed objects system uses `NSPort` objects to send `NSPortMessage` objects back and forth. You should implement interapplication communication using distributed objects whenever possible, and use `NSPort` objects directly only when necessary.

To receive incoming messages, `NSPort` objects must be added to an NSRunLoop as an input source. NSConnection objects automatically add their receive port when initialized. See _[Run Loops](../Run%20Loops/Introduction%20to%20Run%20Loops.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3de2i)_ for more information.

Subclasses of `NSPort` represent particular flavors of data transport from one process to another. The available subclasses are `NSMachPort`, `NSMessagePort`, and `NSSocketPort` and each is described below.

Note that instances of port subclasses cannot be mixed on a particular communication channel. For example, a client cannot connect to a server using `NSMessagePort` if the server only supports connections made with `NSSocketPort`. Also, you cannot transfer instances of `NSMessagePort` in a message to another process over a channel which is using `NSSocketPort` objects as its endpoints; you can only pass `NSSocketPort` objects on such a channel. These restrictions apply to any subclasses of `NSPort`, not just `NSMessagePort` and `NSSocketPort`. However, you are free to create other connections to a server using other subclasses of `NSPort` (assuming the server supports multiple transports) and send instances of that other subclass on that channel.

`NSMachPort` is an object wrapper for a Mach port, the fundamental communication port in OS X. `NSMachPort` allows for local (on the same machine) communication only.

To use `NSMachPort` effectively you should be familiar with Mach ports, port access rights, and Mach messages. See the Mach OS documentation for more information.

`NSMessagePort` is a system-independent implementation of `NSPort` for sending messages. `NSMessagePort` allows for local (on the same machine) communication only.

`NSSocketPort` is a system-independent implementation of `NSPort` for sending messages over a BSD socket port. `NSSocketPort` allows for both local and remote communication, but may be more expensive than the other ports for the local case.

`NSPortNameServer` provides an object-oriented interface to the port registration service used by the distributed objects system. `NSConnection` objects use it to contact each other and to distribute objects over the network; you should rarely need to interact directly with an `NSPortNameServer` object .

You get an `NSPortNameServer` object by using the `systemDefaultPortNameServer` class method—never allocate and initialize an instance directly. With the default server object you can register an `NSPort` object under a given name, making it available on the network, and also unregister it so that it cannot be looked up (although other applications that have already looked up the `NSPort` object can still use it until it becomes invalid).

Each type of `NSPort` has its own `NSPortNameServer` subclass as described below.

This port name server takes and returns instances of NSMachPort.

Port removal functionality is not supported in `NSMachBootstrapServer`; if you want to cancel a service, you have to destroy the port (invalidate the `NSMachPort` object given to `registerPort:name:`).

This port name server takes and returns instances of `NSMessagePort`.

Port removal functionality is not supported in `NSMessagePortNameServer`; if you want to cancel a service, you have to destroy the port (invalidate the `NSMessagePort` object given to `registerPort:name:`).

This port name server takes and returns instances of `NSSocketPort`.

Port removal functionality is supported by the `removePortForName:` method and should be used to remove invalid socket ports.

Unlike the other port name servers, `NSSocketPortNameServer` can operate over a network. By registering your socket ports, you make them available to other computers on the network without hard-coding the TCP port numbers. Clients just need to know the name of the host running the port name server (and the name of the port).

[Next](Message%20Encapsulation.md)[Previous](Connections%20and%20Proxies.md)

