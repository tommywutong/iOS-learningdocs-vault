---
title: Network Kernel Extensions (legacy)
apple_id: TP40001089
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-10-03'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/NetworkKernelExtensions/using/using.html
archived_at: '2026-07-15T07:23:22.774170Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Network Kernel Extensions (legacy)](About%20Network%20Kernel%20Extensions.md)


[Next](Network%20Kernel%20Extensions%20Reference.md)[Previous](About%20Network%20Kernel%20Extensions.md)

An important change has long been noted in the `<sys/mbuf.h>` header file since the release of Mac OS X 10.2. Note that the header file is bracketed by the `__APPLE_API_UNSTABLE` define. The mbuf structure is a key to the processing of packets in an NKE. As part of the formalizing the NKE APIs, it is expected that the mbuf structure will be changed. Details will be provided in the future. Changes to the existing NKE API are not expected be applied to System Updates to Mac OS X 10.3.x, however, bug fixes or features for future systems may require some interim changes.

For all shipping releases of Mac OS X prior to 10.4, the Network Kernel Extensions (NKE) APIs have not been officially supported. The legacy NKE architecture was implemented as an interim solution. The legacy API was never designed to be officially supported. Other aspects of the OS X networking implementation have received a higher priority, and so the interim solution has remained in effect to OS X 10.3.x.

The NKE mechanism for Mac OS X version 10.4 and later is described in the document _[Network Kernel Extensions Programming Guide](../Network%20Kernel%20Extensions%20Programming%20Guide/Introduction%20to%20Network%20Kernel%20Extensions%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjy)_.

# Using Network Kernel Extensions

This chapter provides an overview for the TCPLogger sample which is included in the NKE documentation package.

tcplognke is a socket NKE which is invoked for each TCP connection. It records detailed information about each connection, including the number of bytes sent to and from the system, the time the connection was up, and the remote IP address. The tcplog command line utility demonstrates control of the tcplognke NKE to enable/disable logging, dump log information, and specify different logging criteria.

When tcplognke is loaded and initialized, it installs itself in the TCP protocol structure ready for use and it registers a Kernel Controller structure. The tcplog utility demonstrates the use of the PF_SYSTEM socket to enable/disable logging in the tcplognke, to have the NKE send saved log information to the tool, for the tool to display in the terminal window. Other command options are implemented in the tool to control the operations of the NKE.

The tcplognke NKE keeps a buffer of connection records. If no control program attaches to it, the buffer is continually overwritten as connections are established and terminated. To retain or view the information that the tcplognke NKE gathers, use the enclosed tcplog command line utility. The tool configures the tcplognke NKE to send log records to the tcplog program. The tcplog tool then loops, displaying and writing log records as the tcplognke NKE creates them.

The source code for the tcplognke NKE and for the tcplog command line utility are available for the _current_ (10.4 and later) version of the NKE architecture as the _[tcplognke](https://developer.apple.com/library/archive/samplecode/tcplognke/Introduction/Intro.html#//apple_ref/doc/uid/DTS10003669)_ sample code project. See the Read Me file with the TCPLogger sample code for more instructions on the design and use of the sample NKE.

The _legacy_ tcplognke NKE (for 10.3 and earlier) is not published and is not supported. You must contact Apple developer technical support to obtain this sample code.

[Next](Network%20Kernel%20Extensions%20Reference.md)[Previous](About%20Network%20Kernel%20Extensions.md)

