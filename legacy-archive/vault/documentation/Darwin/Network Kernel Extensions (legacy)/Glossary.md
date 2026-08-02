---
title: Network Kernel Extensions (legacy)
apple_id: TP40001089
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-10-03'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/NetworkKernelExtensions/glossary/glossary.html
archived_at: '2026-07-15T07:23:22.709342Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Network Kernel Extensions (legacy)](About%20Network%20Kernel%20Extensions.md)


[Previous](Document%20Revision%20History.md)

An important change has long been noted in the `<sys/mbuf.h>` header file since the release of Mac OS X 10.2. Note that the header file is bracketed by the `__APPLE_API_UNSTABLE` define. The mbuf structure is a key to the processing of packets in an NKE. As part of the formalizing the NKE APIs, it is expected that the mbuf structure will be changed. Details will be provided in the future. Changes to the existing NKE API are not expected be applied to System Updates to Mac OS X 10.3.x, however, bug fixes or features for future systems may require some interim changes.

For all shipping releases of Mac OS X prior to 10.4, the Network Kernel Extensions (NKE) APIs have not been officially supported. The legacy NKE architecture was implemented as an interim solution. The legacy API was never designed to be officially supported. Other aspects of the OS X networking implementation have received a higher priority, and so the interim solution has remained in effect to OS X 10.3.x.

The NKE mechanism for Mac OS X version 10.4 and later is described in the document _[Network Kernel Extensions Programming Guide](../Network%20Kernel%20Extensions%20Programming%20Guide/Introduction%20to%20Network%20Kernel%20Extensions%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjy)_.

# Glossary

- __domain__

  A complete protocol family.

- __extension__

  A general term for an object module that can be dynamically added to a running system. A synonym for kernel extension.

- __Data Link Interface Layer (DLIL)__

  The fixed part of the network kernel extension architecture that exists between protocol stacks and the network drivers.

- __data link interface module__

  A network kernel extension that handles demultiplexing or packet framing.

- __data link NKE__

  A network kernel extension that exists between the protocol stacks and the device layer.

- __DLIL interface filter__

  A network kernel extension that is installed between the DLIL and one or more network interfaces.

- __DLIL protocol filter__

  A network kernel extension that is installed between the DLIL and a network protocol stack.

- __data link protocol module__

  A network kernel extension that handles the specific interface for the protocol’s attachment to a particular interface family.

- __global NKE__

  An NKE that is automatically enabled for sockets of the type specified for the NKE.

- __network kernel extension (NKE)__

  1) The architecture that allows modules to be added to the Mac OS X networking subsystem while the system is running. 2) A module that can be added to a running system.

- __plug-in__

  A general term for an object module that can be dynamically added to a running system.

- __programmatic filter NKE__

  An NKE that is enabled only under program control, using socket options, for a specific socket.

- __protocol family NKE__

  A network kernel extension that implements a domain.

- __protocol handler__

  A network kernel extension that implements a specific protocol within a domain.

- __socket NKE__

  A network kernel extension that is installed between the socket layer and the protocol stack or network device layers.

[Previous](Document%20Revision%20History.md)

