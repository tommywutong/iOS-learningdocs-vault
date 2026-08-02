---
title: Network Kernel Extensions Programming Guide
apple_id: TP40001858
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2012-01-09'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/NKEConceptual/interface_nke/interface_nke.html
archived_at: '2026-07-15T07:23:17.687719Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Network Kernel Extensions Programming Guide](Introduction%20to%20Network%20Kernel%20Extensions%20Programming%20Guide.md)


[Next](Network%20Kernel%20Extensions%20Reference.md)[Previous](Interface%20Filters.md)

# Network Interfaces and Protocol Plumbers

This chapter describes the network interface KPI. This programming interface allows a KEXT to attach new network interfaces, communicate with and manipulate network interfaces, and create new virtual interfaces.

The mechanism recommended for supporting new interfaces depends on the nature of the interface. The recommended mechanisms are:

- Ethernet drivers—subclass the [IOEthernetController](https://developer.apple.com/documentation/kernel/ioethernetcontroller) and [IOEthernetInterface](https://developer.apple.com/documentation/kernel/ioethernetinterface) classes from the I/O Kit’s I/O Networking Family.
- Other hardware network controllers—subclass the [IONetworkController](https://developer.apple.com/documentation/kernel/ionetworkcontroller) and [IONetworkInterface](https://developer.apple.com/documentation/kernel/ionetworkinterface) classes.
- Virtual interfaces—the interface KPI described in this section is recommended.

This chapter also describes protocol plumbers. Protocol plumbers are used to attach network protocols to interfaces.

If you are creating support for an interface type that the stack does not already support (such as ATM), regardless of whether your KEXT uses the I/O Kit, you must register protocol plumbers for attaching existing protocols to the new interface type.

The functionality in a network interface is utilized by both the interface driver and the protocol stacks, as shown in [Figure 7-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrtgewueqsbi5eugrcg).

__Figure 7-1__  Network Interfaces in the Networking Stack

![Network Interfaces in the Networking Stack](attachments/art/nke_architecture.gif)

Your network interface should define the following callbacks, which are called by protocols and drivers:

- [ifnet_add_proto_func](https://developer.apple.com/documentation/kernel/ifnet_add_proto_func), which is called whenever a protocol is attached to the interface.
- [ifnet_check_multi](https://developer.apple.com/documentation/kernel/ifnet_check_multi), which is called when a multicast address is added to an interface. This allows the interface to reject invalid multicast addresses before they are added to the interface.
- [ifnet_del_proto_func](https://developer.apple.com/documentation/kernel/ifnet_del_proto_func), which is called when a protocol is detached from the interface.
- [ifnet_demux_func](https://developer.apple.com/documentation/kernel/ifnet_demux_func), which is called with a raw packet from the interface, and returns the protocol family value of the protocol that should process the packet. It can do this using either the demux descriptors registered with [ifnet_add_proto_func](https://developer.apple.com/documentation/kernel/ifnet_add_proto_func) or hard-coded logic. If the packet does not match any protocol, the function should return `ENOENT`.
- [ifnet_detached_func](https://developer.apple.com/documentation/kernel/ifnet_detached_func), which is called when your interface is detached.
- [ifnet_event_func](https://developer.apple.com/documentation/kernel/ifnet_event_func), which is called when an event occurs on a particular interface.
- [ifnet_framer_func](https://developer.apple.com/documentation/kernel/ifnet_framer_func), which is called with outgoing packets before sending them to outgoing interface filters, and is expected to wrap the packet with a stack frame appropriate to the interface type.
- [ifnet_ioctl_func](https://developer.apple.com/documentation/kernel/ifnet_ioctl_func), which is called whenever an ioctl is received for the interface. The network interface is expected to pass these on to the I/O Kit driver if it is necessary and appropriate to do so. All undefined ioctls are reserved for future Apple use. You should use `kern_control` if you need to add additional control mechanisms.
- [ifnet_output_func](https://developer.apple.com/documentation/kernel/ifnet_output_func), which is called with a packet that is ready to be sent out the wire. The network interface is expected to transmit the packet and free the mbuf associated with it. For network interfaces backed by I/O Kit drivers, this callback generally calls a function in the I/O Kit driver that handles both of these tasks.
- [ifnet_set_bpf_tap](https://developer.apple.com/documentation/kernel/ifnet_set_bpf_tap), which is called by the stack to set the BPF tap function that is installed on the interface. This callback is optional, but recommended; if you do not add this function, BPF cannot be used with your interface.

Good examples of many of these functions can be found in `bsd/net/ether_if_module.c` in the `xnu` (kernel) source tree.

The following functions are typically called (in the following order) to support the dynamic insertion and removal of network interfaces:

1. [ifnet_allocate](https://developer.apple.com/documentation/kernel/1525028-ifnet_allocate), which allocates an interface structure.
2. [ifnet_attach](https://developer.apple.com/documentation/kernel/1524922-ifnet_attach), which attaches an interface to the global interface list.
3. [bpfattach](https://developer.apple.com/documentation/kernel/1589467-bpfattach), which enables BPF support on an interface (optional).
4. [ifnet_detach](https://developer.apple.com/documentation/kernel/1524903-ifnet_detach), which removes an interface from the global interface list.
5. [ifnet_release](https://developer.apple.com/documentation/kernel/1525052-ifnet_release), which releases a reference to an interface structure. If the reference count reaches zero (0), the structure will be freed. This release matches the [ifnet_allocate](https://developer.apple.com/documentation/kernel/1525028-ifnet_allocate) call earlier, and should be called _after_ calling [ifnet_detach](https://developer.apple.com/documentation/kernel/1524903-ifnet_detach).

The related function [ifnet_reference](https://developer.apple.com/documentation/kernel/1524857-ifnet_reference) can be used (generally by other KEXTs) to increase the reference count of an interface structure. These calls must be balanced by an equal number of calls to [ifnet_release](https://developer.apple.com/documentation/kernel/1525052-ifnet_release).

Protocol plumbers, as mentioned previously, are responsible for attaching a protocol to a network interface. When a protocol needs to attach to an interface, it calls a function that looks up the plumber designated for that protocol and interface type, then calls that plumber’s plumb handler.

Protocol plumbers define the following callbacks, which are called by protocols:

- [proto_plumb_handler](https://developer.apple.com/documentation/kernel/proto_plumb_handler), which is called to attach a protocol to an interface. This typically consists of a call to the interface’s `ifnet_attach_protocol` callback.
- [proto_unplumb_handler](https://developer.apple.com/documentation/kernel/proto_unplumb_handler), which is called to detach a protocol from an interface. The unplumb handler should call the `ifnet_detach_protocol` function, but may do other cleanup such as freeing any storage allocated in the `proto_plumb_handler` callback.

When attaching a protocol to an interface, the protocol plumber typically fills in the following fields in the [ifnet_attach_proto_param](https://developer.apple.com/documentation/kernel/ifnet_attach_proto_param) structure, many of which may be defined as part of the protocol itself. This mechanism provides the opportunity for the protocol plumber to intercept these calls and take interface-specific actions where needed.

- [proto_media_detached](https://developer.apple.com/documentation/kernel/proto_media_detached) (optional), which is used to notify the protocol that it is being detached.
- [proto_media_event](https://developer.apple.com/documentation/kernel/proto_media_event) (optional), which is called to notify a protocol about interface-specific events.
- [proto_media_input](https://developer.apple.com/documentation/kernel/proto_media_input) (required), which is used to deliver an inbound packet to the protocol for processing.
- [proto_media_ioctl](https://developer.apple.com/documentation/kernel/proto_media_ioctl) (optional), which is typically the protocol’s ioctl handling function.
- [proto_media_preout](https://developer.apple.com/documentation/kernel/proto_media_preout) (required), which is called just before a packet is transmitted. This allows the protocol to specify a media-specific frame type and destination.
- [proto_media_resolve_multi](https://developer.apple.com/documentation/kernel/proto_media_resolve_multi) (optional), which is used to obtain a link layer address for a given protocol layer multicast address. This is only necessary if your interface supports multicast.
- [proto_media_send_arp](https://developer.apple.com/documentation/kernel/proto_media_send_arp) (optional), which is used to obtain the link layer address corresponding to a given protocol layer unicast address. This is necessary for all non-point-to-point interfaces.

Examples of these functions can be found in `bsd/net/ether_inet_pr_module.c` in the `xnu` (kernel) source tree.

The following steps describe the process of sending a packet, using Ethernet as the example medium:

1. The `ip_output` routine in the IP protocol stack calls `ifnet_output`.
2. The [ifnet_output](https://developer.apple.com/documentation/kernel/1525046-ifnet_output) function calls the protocol plumber’s [proto_media_preout](https://developer.apple.com/documentation/kernel/proto_media_preout) function. In the case of IP, this function calls [inet_arp_lookup](https://developer.apple.com/documentation/kernel/1584165-inet_arp_lookup).
3. If the ARP cache does not contain an entry for the IP address, [inet_arp_lookup](https://developer.apple.com/documentation/kernel/1584165-inet_arp_lookup) then calls the protocol plumber’s [proto_media_send_arp](https://developer.apple.com/documentation/kernel/proto_media_send_arp) callback to resolve the target IP address into a media access control (MAC) address.
4. When the [proto_media_preout](https://developer.apple.com/documentation/kernel/proto_media_preout) callback returns, the [ifnet_output](https://developer.apple.com/documentation/kernel/1525046-ifnet_output) function calls the network interface’s [ifnet_framer_func](https://developer.apple.com/documentation/kernel/ifnet_framer_func) function. This framing function prepends interface-specific frame data to the packet.
5. If any interface filters are present, their [iff_output_func](https://developer.apple.com/documentation/kernel/iff_output_func) callbacks are called consecutively.
6. The [ifnet_output](https://developer.apple.com/documentation/kernel/1525046-ifnet_output) function calls the network interface’s [ifnet_output_func](https://developer.apple.com/documentation/kernel/ifnet_output_func) callback, which transmits the packet and frees the mbuf.

The following steps describe the process of receiving a packet:

1. The hardware driver or its support code calls [ifnet_input](https://developer.apple.com/documentation/kernel/1525087-ifnet_input) with pointers to its `ifnet` structure ([ifnet_t](https://developer.apple.com/documentation/kernel/ifnet_t)) and `mbuf` chain ([mbuf_t](https://developer.apple.com/documentation/kernel/mbuf_t)).
2. The packet is queued. Processing resumes on a different thread.
3. The [ifnet_input](https://developer.apple.com/documentation/kernel/1525087-ifnet_input) function calls the network interface’s [ifnet_demux_func](https://developer.apple.com/documentation/kernel/ifnet_demux_func) function for the interface.
4. The demultiplexing function identifies the frame and returns a [protocol_family_t](https://developer.apple.com/documentation/kernel/protocol_family_t) value to indicate which protocol should handle the packet.
5. The [ifnet_input](https://developer.apple.com/documentation/kernel/1525087-ifnet_input) function calls the attached interface filters (if any) sequentially.
6. Any packets not matching an attached protocol are dropped, as are any promiscuous packets.
7. The [ifnet_input](https://developer.apple.com/documentation/kernel/1525087-ifnet_input) function calls the protocol plumber’s [proto_media_input](https://developer.apple.com/documentation/kernel/proto_media_input) function. The plumber is specific to a given protocol/interface combination.

[Next](Network%20Kernel%20Extensions%20Reference.md)[Previous](Interface%20Filters.md)

