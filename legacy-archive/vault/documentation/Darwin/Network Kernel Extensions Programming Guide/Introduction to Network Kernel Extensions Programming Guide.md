---
title: Network Kernel Extensions Programming Guide
apple_id: TP40001858
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2012-01-09'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/NKEConceptual/intro/intro.html
archived_at: '2026-07-15T07:23:18.043269Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Network%20Kernel%20Extensions%20Overview.md)

# Introduction to Network Kernel Extensions Programming Guide

Network kernel extensions (NKEs) provide a way to extend and modify the networking infrastructure of OS X while the kernel is running, without requiring the kernel to be recompiled, relinked, or rebooted.

NKEs allow you to create modules that can be loaded and unloaded dynamically at specific positions in the network hierarchy. These modules can monitor and modify network traffic, and can receive notification of asynchronous events from the driver layer, such as interface status changes.

This document is primarily of interest to developers who need to extend or modify the OS X networking infrastructure. This includes:

- Adding support for new, non-ethernet interface types.
- Designing custom routing technologies.
- Creating link-layer encryption technologies.

This document assumes a significant understanding of networking concepts, including a basic familiarity with sockets, packet filtering, and so on. It also assumes that you are already familiar with the basics of kernel-level operating systems programming.

Because even minor bugs in kernel-level code can cause serious consequences, including application instability, data corruption, and even kernel panics, the techniques described in this document should be used only if no other mechanism already exists. For example, where possible, IP filtering should generally be done using `ipfw`. Similarly, packet logging should generally be done using `bpf`.

This document is intended to provide supplementary conceptual material specific to network kernel extensions. It is not intended as a reference document, and assumes prior knowledge of OS X kernel extensions (KEXTs). For reference material specific to networking KEXTs, see the document _KPI Reference_. For additional information on OS X KEXTs in general, see the document _[Kernel Extension Programming Topics](../Kernel%20Extension%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrt)_.

The following sources provide additional information that may be of interest to developers of network kernel extensions:

- _[Kernel Extension Programming Topics](../Kernel%20Extension%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrt)_—conceptual information about kernel extensions in OS X.
- _KPI Reference_—reference documentation specific to network kernel extensions and other non-I/O Kit (device driver) KEXTs.
- _[Kernel Framework Reference](https://developer.apple.com/documentation/kernel)_—reference documentation for I/O Kit device drivers, including network device drivers.
- _The Design and Implementation of the 4.4 BSD Operating System_. M. K. McKusick et al., Addison-Wesley, Reading, 1996.
- _Unix Network Programming,_ Second Edition, volume 1. Richard W. Stevens, Prentice Hall, New York, 1998.
- _TCP/IP Illustrated,_ volume 1: The Protocols. Richard W. Stevens, Addison-Wesley, Reading, 1994.
- _TCP/IP Illustrated,_ volume 2: The Implementation. Richard W. Stevens and Gary R. Wright, Addison-Wesley, Reading, 1995.
- _TCP/IP Illustrated,_ volume 3: Other Protocols. Richard W. Stevens, Addison-Wesley, Reading, 1996.

The following websites provide information about the Berkeley Software Distribution (BSD):

- [http://www.FreeBSD.org](http://www.freebsd.org/)
- [http://www.NetBSD.org](http://www.netbsd.org/)
- [http://www.OpenBSD.org/](http://www.openbsd.org/)
[Next](Network%20Kernel%20Extensions%20Overview.md)

