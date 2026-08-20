---
title: Making sense of IOKit error codes
apple_id: DTS10001627
resource_type: QA
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2011-07-18'
source_url: https://developer.apple.com/library/archive/qa/qa1075/_index.html
archived_at: '2026-07-18T02:29:55.545217Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1075

# Making sense of I/O Kit error codes

## Q:  When using I/O Kit, how can I figure out what these huge error codes mean?

A: I/O Kit uses the same error encoding scheme used by the kernel. I/O Kit errors are 32 bits long and their type is either `kern_return_t` or `IOReturn`. Their layout is shown in Listing 1 (from the header `mach/error.h`).

__Listing 1__  I/O Kit error code layout.

```
hi		 		       lo  | system(6) | subsystem(12) | code(14) |
```

The high 6 bits are known as the system value, the next 12 bits are known as the subsystem value, and the low 14 bits make up the error code.

The first place to look for information about error codes is in the header file `IOKit/IOReturn.h`. Here you'll find a list of all the generic I/O Kit errors that aren't specific to a particular family. For example, let's consider the I/O Kit error -536870206, which in hex is 0xE00002C2. By using the information in `IOReturn.h`, we can determine that the system value is 0x38, or `sys_iokit`. The subSystem value is 0x0, so we know it's a `sub_iokit_common` error. The code portion is 0x2C2, which means this is a `kIOReturnBadArgument` error.

There are convenient macros for extracting these three values from an I/O Kit error code. These are shown in Listing 2 (also from `mach/error.h`).

__Listing 2__  Error extraction macros.

```
#define err_get_system(err) (((err)>>26)&0x3f) #define err_get_sub(err) (((err)>>14)&0xfff) #define err_get_code(err) ((err)&0x3fff)
```

It's also possible to get error codes back from I/O Kit with a system value of `sys_mach_ipc`, or 0x4. The most common of these is 268435459 or hex 0x10000003 which is the error `MACH_SEND_INVALID_DEST` defined in the `Kernel.framework` header `mach/message.h`. To understand why you can get a Mach error code, it helps to understand that I/O Kit uses Mach messages to communicate between user space and the kernel. The `io_service_t` type passed to calls such as `IOServiceCreatePlugInInterfaceForService` is defined as `mach_port_t` in the `IOKit.framework` header `IOTypes.h`.

So, a `MACH_SEND_INVALID_DEST` error in this context means that a `io_service_t` is invalid. This can mean either that the `io_service_t` is uninitialized or that it was previously freed.

Remember that each I/O Kit family defines its own family-specific error codes in a different header file. For example, USB error codes are located in `IOKit/usb/USB.h` inside `Kernel.framework`, while most FireWire error codes are located in `IOKit/firewire/IOFireWireFamilyCommon.h`, also inside `Kernel.framework`.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-07-18 | Minor content reformatting and editorial changes. |
| 2002-02-07 | New document that explains how to interpret I/O Kit error codes. |

