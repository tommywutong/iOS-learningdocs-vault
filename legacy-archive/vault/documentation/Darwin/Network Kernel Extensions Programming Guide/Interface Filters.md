---
title: Network Kernel Extensions Programming Guide
apple_id: TP40001858
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2012-01-09'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/NKEConceptual/interface_filter_nke/interface_filter_nke.html
archived_at: '2026-07-15T07:23:17.230027Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Network Kernel Extensions Programming Guide](Introduction%20to%20Network%20Kernel%20Extensions%20Programming%20Guide.md)


[Next](Network%20Interfaces%20and%20Protocol%20Plumbers.md)[Previous](IP%20Filters.md)

# Interface Filters

This chapter describes the programming interface for creating interface filters, which are associated with a particular network interface, as shown in [Figure 6-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrtgawueqkcijbeksse).

__Figure 6-1__  Data Link Interface Layer

![Data Link Interface Layer](attachments/art/layers_simple.gif)

An interface filter defines the following callbacks:

- [iff_input_func](https://developer.apple.com/documentation/kernel/iff_input_func), which is used to process packets after they are demuxed.
- [iff_output_func](https://developer.apple.com/documentation/kernel/iff_output_func), which is used to process packets before they are sent out from an interface to a network.
- [iff_event_func](https://developer.apple.com/documentation/kernel/iff_event_func), which is used to filter events specific to an interface.
- [iff_ioctl_func](https://developer.apple.com/documentation/kernel/iff_ioctl_func), which is used to filter ioctls sent to an interface. All undefined ioctls are reserved for future Apple use. You should use `kern_control` if you need to add additional control mechanisms.
- [iff_detached_func](https://developer.apple.com/documentation/kernel/iff_detached_func), which is called when your filter is detached from an interface. When this callback is called, you should perform any cleanup related to the interface. If this is called as a result of the interface itself being detached, it will occur after you receive the interface detach notification.

To attach and detach an interface filter, the following functions are defined by the interface filter KPI:

- [iflt_attach](https://developer.apple.com/documentation/kernel/1589956-iflt_attach), which inserts an interface filter between the protocol plumbers and an attached interface.
- [iflt_detach](https://developer.apple.com/documentation/kernel/1589950-iflt_detach), which removes a previously inserted interface filter.

There are a number of surprises that you may run into when writing an interface filter. Several of these follow:

**Packet injection**
: When your filter injects packets, it should use the [ifnet_input](https://developer.apple.com/documentation/kernel/1525087-ifnet_input) and [ifnet_output_raw](https://developer.apple.com/documentation/kernel/1525049-ifnet_output_raw) functions. If you do this, your filter should be prepared to ignore the packet it just injected, as your filter’s [iff_input_func](https://developer.apple.com/documentation/kernel/iff_input_func) or [iff_output_func](https://developer.apple.com/documentation/kernel/iff_output_func) callback will see this packet again immediately. You should use the `mbuf_tag` APIs ([mbuf_tag_allocate](https://developer.apple.com/documentation/kernel/1535756-mbuf_tag_allocate), for example) to track these packets. If multiple filters are swallowing and reinjecting packets, you may see a given packet multiple times.

__Note:__ When reinjecting packets, the filter must ensure that the packet header field is set in the first mbuf structure. Otherwise, the call to [ifnet_input](https://developer.apple.com/documentation/kernel/1525087-ifnet_input) will result in a kernel panic (`NULL` pointer dereference).

When your [iff_input_func](https://developer.apple.com/documentation/kernel/iff_input_func) callback is called, you may find that the `packet_header` field has been set to `NULL`. The `frame_ptr` parameter to [iff_input_func](https://developer.apple.com/documentation/kernel/iff_input_func) can be used to set the `packet_header` field if the packet must be reinjected. To do this, use the [mbuf_pkthdr_setheader](https://developer.apple.com/documentation/kernel/1535690-mbuf_pkthdr_setheader) function to set the `packet_header` field in the mbuf.

If your [iff_input_func](https://developer.apple.com/documentation/kernel/iff_input_func) callback does not swallow a packet, it is not necessary to set the `packet_header` field.

**Input callbacks: Header pointers and mbufs**
: Your filter’s input callback receives an mbuf pointer to the packet contents and a separate header pointer. The header pointer references the link-layer header, as defined by the relevant interface.

For most interfaces, the length of this header can be determined by inspecting the header length ([ifnet_hdrlen](https://developer.apple.com/documentation/kernel/1524895-ifnet_hdrlen)) defined by the interface. For some interfaces, however, such as PPP, the header length is variable.

**Output callbacks: Header pointers and mbufs**
: Your filter’s output callback receives the entire packet in the mbuf chain. To get the protocol layer information, your filter must know how to parse the link-layer header. For this reason, if you are writing a filter that needs to work with IP packets, you should consider writing an IP filter unless it is absolutely necessary to access link-layer information.

[Next](Network%20Interfaces%20and%20Protocol%20Plumbers.md)[Previous](IP%20Filters.md)

