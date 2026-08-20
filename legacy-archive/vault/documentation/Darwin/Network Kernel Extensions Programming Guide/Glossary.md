---
title: Network Kernel Extensions Programming Guide
apple_id: TP40001858
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2012-01-09'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/NKEConceptual/glossary/glossary.html
archived_at: '2026-07-15T07:23:17.222651Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Network Kernel Extensions Programming Guide](Introduction%20to%20Network%20Kernel%20Extensions%20Programming%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Network%20Kernel%20Extensions%20Reference.md)

# Glossary

- __domain__

  A complete protocol family.

- __driver layer__

  I/O Kit Drivers for various networking types.

- __extension__

  A general term for an object module that can be dynamically added to a running system; often used as a synonym for kernel extension.

- __global socket filter__

  A socket filter that is automatically enabled for sockets of the type specified.

- __ifnet structure__

  A data structure containing function pointers and data related to a particular network interface.

- __in-band__

  Communication on a socket or interface that contains actual data destined for the endpoint (for example, `send` and `recv` calls). See also: [out-of-band](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrtgqwuer2cjfeeosse).

- __interface filter__

  A filter that attached to a particular interface. An interface filter alters [in-band](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrtgqwuer2cijbeeqsh) and [out-of-band](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrtgqwuer2cjfeeosse) communication specific to a given interface.

- __interface layer__

  A layer above the driver layer containing interface KEXTs, interface filters, and protocol plumbers.

- __interface KEXT__

  A network kernel extension that provides routines specific to a particular family of interfaces, such as ARP equivalence routines.

- __IP filter__

  A filter that alters IP traffic each time it enters the protocol stack. By its very nature, an IP filter can only filter [in-band](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrtgqwuer2cijbeeqsh) communication.

- __KEXT__

  Short for kernel extension; a plug-in for the OS X kernel (xnu).

- __KPI__

  Short for kernel programming interface; a group of opaque data types and accessor functions designed to maintain binary compatibility across OS releases.

- __mbuf__

  A data structure containing data about a network packet.

- __network kernel extension (NKE)__

  1) The architecture that allows modules to be added to the OS X networking subsystem while the system is running. 2) A module that can be added to a running system.

- __out-of-band__

  Communication on a socket or interface that relates to the operation of the socket or interface rather than data destined for the endpoint (for example, `ioctl` and `getsockopt` calls). See also: [in-band](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrtgqwuer2cijbeeqsh).

- __plug-in__

  A general term for an object module that can be dynamically added to a running system.

- __programmatic socket filter__

  A socket filter that is enabled only under program control by calling `setsockopt` on a specific socket.

- __protocol plumber__

  A network kernel extension that routes data between an interface and a network protocol stack.

- __protocol stack__

  A layer of the kernel network architecture containing the core functionality for a protocol family such as TCP/IP.

- __protosw structure__

  A data structure containing function pointers and data associated with a protocol family.

- __socket structure__

  A data structure containing data associated with a network socket.

- __socket filter__

  A filter that is associated with a particular socket or class of sockets, filtering [in-band](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrtgqwuer2cijbeeqsh) and [out-of-band](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrtgqwuer2cjfeeosse) operations on the socket. A socket filter resides between a socket and the protocol layer.

[Next](Document%20Revision%20History.md)[Previous](Network%20Kernel%20Extensions%20Reference.md)

