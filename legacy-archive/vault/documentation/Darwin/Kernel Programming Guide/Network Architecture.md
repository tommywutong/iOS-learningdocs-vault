---
title: Kernel Programming Guide
apple_id: TP30000905
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/Networking/Networking.html
archived_at: '2026-07-15T07:23:13.692854Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Kernel Programming Guide](About%20This%20Document.md)


[Next](Boundary%20Crossings.md)[Previous](File%20Systems%20Overview.md)

# Network Architecture

OS X kernel extensions (KEXTs) provide
mechanisms to extend and modify the networking infrastructure of
OS X dynamically, without recompiling or relinking the kernel.
The effect is immediate and does not require rebooting the system.

Networking KEXTs can be used to

- monitor network
  traffic
- modify network traffic
- receive notification of asynchronous events from the driver
  layer

In the last case, such events are received by the data link
and network layers. Examples of these events include power management
events and interface status changes.

Specifically, KEXTs allow you to

- create protocol
  stacks that can be loaded and unloaded dynamically and configured automatically
- create modules that can be loaded and unloaded dynamically
  at specific positions in the network hierarchy.

The Kernel Extension Manager dynamically adds KEXTs to the
running OS X kernel inside the kernel’s address space. An
installed and enabled network-related KEXT is invoked automatically,
depending on its position in the sequence of protocol components, to
process an incoming or outgoing packet.

All KEXTs provide initialization and termination routines
that the Kernel Extension Manager invokes when it loads or unloads
the KEXT. The initialization routine handles any operations that
are needed to complete the incorporation of the KEXT into the kernel, such
as updating `protosw` and `domain` structures
(through programmatic interfaces). Similarly, the termination routine
must remove references to the NKE from these structures to unload
itself successfully. NKEs must provide a mechanism, such as a reference
count, to ensure that the NKE can terminate without leaving dangling
pointers.

For additional information on the networking portions of the
OS X kernel, you should read the document _[Network Kernel Extensions Programming Guide](../Network%20Kernel%20Extensions%20Programming%20Guide/Introduction%20to%20Network%20Kernel%20Extensions%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjy)_.

[Next](Boundary%20Crossings.md)[Previous](File%20Systems%20Overview.md)

