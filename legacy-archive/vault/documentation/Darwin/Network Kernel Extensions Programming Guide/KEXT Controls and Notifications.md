---
title: Network Kernel Extensions Programming Guide
apple_id: TP40001858
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2012-01-09'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/NKEConceptual/control/control.html
archived_at: '2026-07-15T07:23:17.193153Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Network Kernel Extensions Programming Guide](Introduction%20to%20Network%20Kernel%20Extensions%20Programming%20Guide.md)


[Next](Socket%20Filters.md)[Previous](Memory%20Buffers%2C%20Socket%20Manipulation%2C%20and%20Socket%20Input-Output.md)

# KEXT Controls and Notifications

This chapter describes two mechanisms for interacting with a network kernel extension: the kernel control and kernel event APIs. These socket-based APIs allow you to communicate with a KEXT and receive broadcast notifications from the KEXT, respectively.

To support this communication, OS X defines a new socket domain—the `PF_SYSTEM` domain—to provide a way for applications to configure and control KEXTs. The `PF_SYSTEM` domain, in turn, supports two protocols, `SYSPROTO_CONTROL` and `SYSPROTO_EVENT`.

The kernel control (`kern_control`) API, which uses the `SYSPROTO_CONTROL` protocol, allows applications to configure and control a KEXT.

The kernel event (`kern_event`) API, which uses the `SYSPROTO_EVENT` protocol, allows applications and other KEXTs to be notified when certain kernel events occur. It should be used when multiple clients need to know about a given event, and is not intended as a point-to-point communication mechanism. In general, the kernel control API is preferred, as it provides bidirectional communication.

For detailed reference documentation on these APIs, see _[Kernel Framework Reference](https://developer.apple.com/documentation/kernel)_.

The kernel control API is a bidirectional communication mechanism between a user space application and a KEXT. This section describes this API at the kernel level and the user space level.

Supporting kernel controls in a KEXT is relatively straightforward.

In the KEXT’s start function, you must register a kernel control structure using the [ctl_register](https://developer.apple.com/documentation/kernel/1809176-ctl_register) function. The `ctl_register` function is defined in `<sys/kern_control.h>` as follows:

```
int ctl_register(struct kern_ctl_reg *userctl,
            kern_ctl_ref *ctlref);
```

The `kern_ctl_reg` structure contains three fields that are used to identify the control. The fields `ctl_id` and `ctl_name` can be shared across multiple controls.

The final field, `ctl_unit`, contains a value that is specific to a given control. A control can be registered multiple times with the same `ctl_id`, but for each instance a different unit number must be used. For dynamically-allocated control IDs, this value is filled in automatically.

Other fields of the `kern_ctl_reg` structure contain handler functions that you must create to handle various control requests.

The structure’s fields are defined as follows:

**`ctl_name`**
: a bundle ID string for your control of up to `MAX_KCTL_NAME` bytes (including the terminating null). This may be used to generate `ctl_id`.

**`ctl_id`**
: a unique 4 byte ID for the control. (See note below.)

**`ctl_unit`**
: the unit number for the control. The value is automatically assigned for dynamically-allocated `ctl_id` values.

**`ctl_flags`**
: flags that affect the behavior of a control. You can set the `CTL_FLAG_PRIVILEGED` flag to require that the user have admin privileges to contact the control.

For more TCP-like behavior, the flag `CTL_FLAG_REG_SOCK_STREAM` may be specified to indicate that the control should be registered for stream connections rather than datagrams. Note, however, that if you set `CTL_FLAG_REG_SOCK_STREAM`, you _must_ connect to the control using `SOCK_STREAM` instead of `SOCK_DGRAM`.

**`ctl_sendsize`**
: size of buffer reserved for sending messages. A value of 0 indicates that the default size should be used.

**`ctl_recvsize`**
: size of buffer reserved for receiving messages. A value of 0 indicates that the default size should be used.

**`ctl_connect`**
: called when the client process calls connect on the socket with the ID/unit number of the registered control.

**`ctl_disconnect`**
: called when the user client process closes the control socket.

**`ctl_send`**
: called when the user client process writes data to the socket.

**`ctl_setopt`**
: called when the user client process calls `setsockopt` to set the control configuration.

**`ctl_getopt`**
: called when the user client process calls `getsockopt` on the socket.

On successful return, the second parameter, `ctlref`, will contain a reference to the registered kernel control. This reference must be used to unregister the control, and is also passed as an argument to any callbacks when they are called.

It is possible to take advantage of kernel control naming to allow processes to interact with a KEXT in different ways. A KEXT may, for example, register a root-only control for configuring the KEXT. It might register a second control, available to any process, for gathering statistics. Each instance of the control will have a different `ctlref`, and this value can then be used to determine which behavior to use.

When the kernel control receives a connection from a user-space process, the control’s [ctl_connect_func](https://developer.apple.com/documentation/kernel/ctl_connect_func) callback is called. In this function, you should determine the unit number associated with the connection so that you can later send data back to the connecting process. You should then create a data structure (of your choosing) to store connection-specific data, and should return this structure by assignment through the `void **` handle passed in as the third parameter. This value will be passed to the other callbacks when they are called.

At this point, the user process can communicate with the control using [getsockopt](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/getsockopt.2.html#//apple_ref/doc/man/2/getsockopt), [setsockopt](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/setsockopt.2.html#//apple_ref/doc/man/2/setsockopt), [read](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/read.2.html#//apple_ref/doc/man/2/read)/[recv](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/recv.2.html#//apple_ref/doc/man/2/recv), and [write](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/write.2.html#//apple_ref/doc/man/2/write)/[send](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/send.2.html#//apple_ref/doc/man/2/send) on the socket. With the exception of [recv](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/recv.2.html#//apple_ref/doc/man/2/recv) (which reads data from a queue), calls in user space to these functions result in a kernel-space call to the equivalent callbacks in the control, [ctl_getopt_func](https://developer.apple.com/documentation/kernel/ctl_getopt_func), [ctl_setopt_func](https://developer.apple.com/documentation/kernel/ctl_setopt_func), and `ctl_send`, respectively.

The kernel process can, in turn, call a number of functions to send data back to the user space process. This data can be read by the user process using the [read](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/read.2.html#//apple_ref/doc/man/2/read) or [recv](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/recv.2.html#//apple_ref/doc/man/2/recv) system calls. In particular, you can use [ctl_enqueuedata](https://developer.apple.com/documentation/kernel/1809168-ctl_enqueuedata) and [ctl_enqueuembuf](https://developer.apple.com/documentation/kernel/1809171-ctl_enqueuembuf) to queue up data to send to the user space process, and [ctl_getenqueuespace](https://developer.apple.com/documentation/kernel/1809173-ctl_getenqueuespace) to find out how much free space is available in the queue.

When the user process closes the communication socket to the control, the [ctl_disconnect_func](https://developer.apple.com/documentation/kernel/ctl_disconnect_func) callback is called. At this point, the control should free any connection-specific resources that it has allocated.

[Listing 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrsg4wugscejfbuqr2j) shows some basic example functions to use as a starting point:

__Listing 3-1__  A basic `kern_control` example

```
errno_t error;
struct kern_ctl_reg     ep_ctl; // Initialize control
kern_ctl_ref     kctlref;
bzero(&ep_ctl, sizeof(ep_ctl));  // sets ctl_unit to 0
ep_ctl.ctl_id = 0; /* OLD STYLE: ep_ctl.ctl_id = kEPCommID; */
ep_ctl.ctl_unit = 0;
strcpy(ep_ctl.ctl_name, "org.mklinux.nke.foo");
ep_ctl.ctl_flags = CTL_FLAG_PRIVILEGED & CTL_FLAG_REG_ID_UNIT;
ep_ctl.ctl_send = EPHandleWrite;
ep_ctl.ctl_getopt = EPHandleGet;
ep_ctl.ctl_setopt = EPHandleSet;
ep_ctl.ctl_connect = EPHandleConnect;
ep_ctl.ctl_disconnect = EPHandleDisconnect;
error = ctl_register(&ep_ctl, &kctlref);

/* A simple setsockopt handler */
errno_t EPHandleSet( kern_ctl_ref ctlref, unsigned int unit, void *userdata, int opt, void *data, size_t len )
{
    int    error = EINVAL;
#if DO_LOG
    log(LOG_ERR, "EPHandleSet opt is %d\n", opt);
#endif

    switch ( opt )
    {
        case kEPCommand1:               // program defined symbol
            error = Do_First_Thing();
            break;

        case kEPCommand2:               // program defined symbol
            error = Do_Command2();
            break;
    }
    return error;
}

/* A simple A simple getsockopt handler */
errno_t EPHandleGet(kern_ctl_ref ctlref, unsigned int unit, void *userdata, int opt, void *data, size_t *len)
{
    int    error = EINVAL;
#if DO_LOG
    log(LOG_ERR, "EPHandleGet opt is %d *****************\n", opt);
#endif
    return error;
}

/* A minimalist connect handler */
errno_t
EPHandleConnect(kern_ctl_ref ctlref, struct sockaddr_ctl *sac, void **unitinfo)
{
#if DO_LOG
    log(LOG_ERR, "EPHandleConnect called\n");
#endif
    return (0);
}

/* A minimalist disconnect handler */
errno_t
EPHandleDisconnect(kern_ctl_ref ctlref, unsigned int unit, void *unitinfo)
{
#if DO_LOG
    log(LOG_ERR, "EPHandleDisconnect called\n");
#endif
    return;
}

/* A minimalist write handler */
errno_t EPHandleWrite(kern_ctl_ref ctlref, unsigned int unit, void *userdata, mbuf_t m, int flags)
{
#if DO_LOG
    log(LOG_ERR, "EPHandleWrite called\n");
#endif
    return (0);
}
```


Adding `kern_control` support in your NKE is only half of the story. The other half is actually using this support from a client application.

To communicate with an NKE, you must first open a `PF_SYSTEM` socket using the `socket` call as follows:

```
fd = socket(PF_SYSTEM, SOCK_DGRAM, SYSPROTO_CONTROL);
```

Next, your application must associate the socket with a particular kernel control. To do this, the client process should call [connect](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/connect.2.html#//apple_ref/doc/man/2/connect) with the file descriptor returned from the [socket](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/socket.2.html#//apple_ref/doc/man/2/socket) call, along with a filled in `[sockaddr_ctl](../../../Reference/usr_APIs/kern_control/CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3umfts643pmnvwczdeojpwg5dm)` structure containing the ID and unit number of the NKE's kernel control.

For example:

```
sockaddr_ctl addr;

/* (initialize addr here) */

result = connect(fd, (struct sockaddr *)&addr, sizeof(addr));
```

The second parameter, of type `[sockaddr_ctl](../../../Reference/usr_APIs/kern_control/CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3umfts643pmnvwczdeojpwg5dm)`, should be filled in as follows:

```
addr.sc_len = sizeof(struct sockaddr_ctl);
addr.sc_family = AF_SYSTEM;
addr.ss_sysaddr = AF_SYS_CONTROL;
addr.sc_id = MY_ID;     // set to value of ctl_id registered by the NKE in
                        // the ctl_register call described above.
addr.sc_unit = MY_UNIT; // set to the unit number registered by the NKE
                        // in the ctl_register call described above.
```

Of course, in the case of a dynamically-generated control ID, you must obtain the value for `sc_id` using the `CTLIOCGINFO` ioctl, as shown in [Listing 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrsg4wugscejfbuqr2j). When using a dynamically-generated control ID, the unit number is ignored. The stack will automatically pick an unused unit number and fill in the `sc_unit` field before passing the [connect](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/connect.2.html#//apple_ref/doc/man/2/connect) call to the kernel control’s connect callback. While the kernel side must keep track of the unit number for sending data back to the client, from the client’s perspective, the unit number is unused.

Now that a communication channel is in place, the client process may use the `setsockopt` call to send commands to the NKE, or the `getsockopt` call to obtain status information from the NKE. The NKE defines which socket option names it will handle. The client process should pass only supported option names to the NKE in the `setsockopt` call. However, for safety, it is the responsibility of the NKE to ignore options that it does not understand, returning `EOPNOTSUPP`.

[Listing 3-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrsg4wugscejbdemqsb) shows a code example for opening a `PF_SYSTEM` socket to communicate with an NKE.

__Listing 3-2__  Opening a `PF_SYSTEM` socket to use with `kern_control`

```
    struct sockaddr_ctl       addr;
    int                       ret = 1;

    fd = socket(PF_SYSTEM, SOCK_DGRAM, SYSPROTO_CONTROL);
    if (fd != -1) {
        bzero(&addr, sizeof(addr)); // sets the sc_unit field to 0
        addr.sc_len = sizeof(addr);
        addr.sc_family = AF_SYSTEM;
        addr.ss_sysaddr = AF_SYS_CONTROL;
#ifdef STATIC_ID
        addr.sc_id = kEPCommID;  // should be unique - use a registered Creator ID here
        addr.sc_unit = kEPCommUnit;  // should be unique.
#else
        {
            struct ctl_info info;
            memset(&info, 0, sizeof(info));
            strncpy(info.ctl_name, MYCONTROLNAME, sizeof(info.ctl_name));
            if (ioctl(fd, CTLIOCGINFO, &info)) {
                perror(“Could not get ID for kernel control.\n”);
                exit(-1);
            }
            addr.sc_id = info.ctl_id;
            addr.sc_unit = 0;
        }
#endif

        result = connect(fd, (struct sockaddr *)&addr, sizeof(addr));
        if (result) {
           fprintf(stderr, "connect failed %d\n", result);
        }
    } else { /* no fd */
            fprintf(stderr, "failed to open socket\n");
    }

    if (!result) {
        result = setsockopt( fd, SYSPROTO_CONTROL, kEPCommand1, NULL, 0);
        if (result){
            fprintf(stderr, "setsockopt failed on kEPCommand1 call - result was %d\n", result);
        }
    }
```


The kernel event notification mechanism, or `kern_event`, is a lightweight mechanism that allows applications to be notified when certain kernel events occur. It is a one-shot event from kernel space to user space that is broadcast to all processes that are listening. For bidirectional communication, you must use the `kern_control` API, described in [Using the Kernel Control API for KEXT Control](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrsg4wugsceineeksch).

This API is relatively straightforward. At initialization time, your NKE should call `kev_vendor_code_find` with the bundle name of your NKE (up to 200 characters in length). It will return a unique identifier that your KEXT should use to identify any notifications that it posts. This identifier value is not persistent across reboots.

Once you have a vendor code, your NKE can post notifications. To post a notification, your NKE calls `kev_message_post` with a `kev_msg` structure containing the vendor code obtained previously, along with the event’s class, subclass, event code, and up to five pieces of data of arbitrary length associated with the event.

You can define your own class and subclass values as appropriate for your NKE. The Apple-defined class values used by kernel events built into OS X can be found in the header file `kern_event.h`.

To receive kernel notifications in a client application, you must first create a kernel event socket as follows:

```
fd = socket(PF_SYSTEM, SOCK_RAW, SYSPROTO_EVENT);
```

Once you have created this socket, you can use this to receive event notifications. There are several ioctls available to help you filter notifications:

- `SIOCGKEVFILT`—get the kernel event filter for this socket.
- `SIOCGKEVID`—get the current event ID pending on the socket. Each event will have a different ID.
- `SIOCGKEVVENDOR`—look up a vendor code.
- `SIOCSKEVFILT`—set the kernel event filter for this socket.

For example, to set the event filter to filter only for Apple-generated events from AppleTalk, you might do the following:

```
struct kev_request req;
req.vendor_code=KEV_VENDOR_APPLE;
req.kev_class=KEV_APPLESHARE_CLASS;
req.kev_subclass=KEV_ANY_SUBCLASS;

if (ioctl(fd, SIOCSKEVFILT, &req)) {
    perror(“SIOCSKEVFILT”);
    exit(-1);
}
```

Using the `SIOCGKEVFILT` ioctl is similar:

```
struct kev_request req;

if (ioctl(fd, SIOCGKEVFILT, &req)) {
    perror(“SIOCSKEVFILT”);
    exit(-1);
}
printf(“The current filter is vendor code %d, class %d, subclass %d\n”,
    req.vendor_code, req.class, req.subclass);
```

To look up a vendor code for another vendor, you might do the following:

```
struct kev_vendor_code vc;
strcpy(vc.vendor_string, “org.mklinux.driver.swim3”);
if (ioctl(fd, SIOCGKEVVENDOR, &vc)) exit(-1);
printf(“Vendor code returned was %d\n”, vc.vendor_code);
```

Finally, to obtain the next event ID from the socket, you might do something like this:

```
uint32_t id;
if (ioctl(fd, SIOCGKEVID, &id)) exit(-1);
printf(“ID returned was %d\n”, id);
```


Developers often ask how an NKE can open a “preference file” in an NKE’s start function. Under the existing architecture, the NKE cannot reliably access a preference file. When the system starts the NKE, there are no APIs that the NKE can use to open a file and read preference information.

The proper way to dynamically configure an NKE is with a startup daemon or other application-level process. The daemon finds the NKE using the kernel control (`kern_control`) mechanism described in [Using the Kernel Control API for KEXT Control](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrsg4wugsceineeksch), and passes in configuration information that the NKE may require.

To avoid crashes, unexplained behavior, and other pitfalls, there are a few simple rules you should follow when using `kern_control` and `kern_event` in your NKE.

**Unregister your control.**
: When someone tries to talk to you after your KEXT is unloaded, a kernel panic ensues. You must use `ctl_deregister` to unregister your control before your NKE is unloaded. This call will fail if there are clients still connected to your kernel control.

**The maximum data size for events is 2KB.**
: Data passed with the `kern_event` APIs must be sent in chunks no larger than the `mbuf` cluster size, or 2KB. Otherwise, truncation will occur.

[Next](Socket%20Filters.md)[Previous](Memory%20Buffers%2C%20Socket%20Manipulation%2C%20and%20Socket%20Input-Output.md)

