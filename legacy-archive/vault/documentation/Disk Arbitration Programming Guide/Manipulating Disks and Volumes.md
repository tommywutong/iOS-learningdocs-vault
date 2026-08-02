---
title: Disk Arbitration Programming Guide
apple_id: TP40009310
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: DiskArbitration
published: '2013-09-17'
source_url: https://developer.apple.com/library/archive/documentation/DriversKernelHardware/Conceptual/DiskArbitrationProgGuide/ManipulatingDisks/ManipulatingDisks.html
archived_at: '2026-07-15T07:31:54.605884Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Disk Arbitration Programming Guide](About%20Disk%20Arbitration.md)


[Next](Document%20Revision%20History.md)[Previous](Using%20Disk%20Arbitration%20Notification%20and%20Approval%20Callbacks.md)

# Manipulating Disks and Volumes

In addition to watching for changes in volumes and refusing mount, unmount, and eject calls, the Disk Arbitration framework provides the ability to get various pieces of information about a volume, mount and unmount volumes, and so on. This chapter describes how to do this.

Before you can manipulate a disk or volume, you must obtain a [DADiskRef](https://developer.apple.com/documentation/diskarbitration/dadisk) object for that disk or volume. You can obtain a `DADiskRef` object in four ways:

- As a parameter passed to your event callback (described in [Using Disk Arbitration Notification and Approval Callbacks](Using%20Disk%20Arbitration%20Notification%20and%20Approval%20Callbacks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tgmjqfvbuqmrnknlte))
- From an `io_service_t` user-space reference to an `IOMedia` object for a valid device slice by calling [DADiskCreateFromIOMedia](https://developer.apple.com/documentation/diskarbitration/1401862-dadiskcreatefromiomedia)

  You can obtain an `io_service_t` user-space reference to an [IOMedia](https://developer.apple.com/documentation/kernel/iomedia) object by calling [IOServiceGetMatchingService](https://developer.apple.com/documentation/iokit/1514535-ioservicegetmatchingservice) or [IOServiceGetMatchingServices](https://developer.apple.com/documentation/iokit/1514494-ioservicegetmatchingservices). To learn about working with the I/O Registry, read _[IOKit Fundamentals](../Device%20Drivers/IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_.
- From a BSD device name (`disk1s1`, for example) using [DADiskCreateFromBSDName](https://developer.apple.com/documentation/diskarbitration/1401870-dadiskcreatefrombsdname)
- From a mount point by calling [DADiskCreateFromVolumePath](https://developer.apple.com/documentation/diskarbitration/1401858-dadiskcreatefromvolumepath)

If you have either an `io_service_t` object or a BSD device name, your app can create a `DADiskRef` object as follows:

1. Create a `DASessionRef` object as described in [Creating a Session](Using%20Disk%20Arbitration%20Notification%20and%20Approval%20Callbacks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tgmjqfvbuqmrnknltg).
2. Schedule it as described in [Scheduling the Session with the Run Loop or Dispatch Queue](Using%20Disk%20Arbitration%20Notification%20and%20Approval%20Callbacks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tgmjqfvbuqmrnknltcma). Be sure your dispatch queue or run loop is running.
3. Create the disk objects.
4. Manipulate them as desired.

Disk arbitration provides three functions to get additional information about disks and partitions: [DADiskCopyDescription](https://developer.apple.com/documentation/diskarbitration/1401854-dadiskcopydescription), [DADiskGetBSDName](https://developer.apple.com/documentation/diskarbitration/1401880-dadiskgetbsdname), and [DADiskCopyIOMedia](https://developer.apple.com/documentation/diskarbitration/1401888-dadiskcopyiomedia). As a rule, you can obtain almost any information about a particular disk by calling [DADiskCopyDescription](https://developer.apple.com/documentation/diskarbitration/1401854-dadiskcopydescription). For some fairly esoteric pieces of information, however, you may have to obtain an `IOMedia` object for the disk and query that object.

- If you need the BSD device name of the disk or partition (`disk1s1`, for example) as a C string (commonly used when working with POSIX-level APIs), call [DADiskGetBSDName](https://developer.apple.com/documentation/diskarbitration/1401880-dadiskgetbsdname).
- For most other information, call [DADiskCopyDescription](https://developer.apple.com/documentation/diskarbitration/1401854-dadiskcopydescription), as described in [Obtaining a Description Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tgmjqfvbuqmznknlto).
- If the information you need is not available through [DADiskCopyDescription](https://developer.apple.com/documentation/diskarbitration/1401854-dadiskcopydescription), call [DADiskCopyIOMedia](https://developer.apple.com/documentation/diskarbitration/1401888-dadiskcopyiomedia).

The [DADiskCopyDescription](https://developer.apple.com/documentation/diskarbitration/1401854-dadiskcopydescription) method returns a [CFDictionaryRef](https://developer.apple.com/documentation/corefoundation/cfdictionaryref) object containing several dozen pieces of information about a disk or partition. Some commonly used data includes:

- Mount point and volume name
- BSD device node name and major and minor numbers
- Information about the hardware (device ID, vendor ID, GUID, and so on)
- Connection info (bus name and path)

You can find a complete list of properties in the `DADisk.h` header in the Disk Arbitration Framework, along with a description of the expected data types for the values of each key.

For example, to print the mount point path for a volume:

```
DADiskRef disk;
CFDictionaryRef *diskinfo;

...

diskinfo = DADiskCopyDescription(disk);
CFURLRef fspath = CFDictionaryGetValue(dict,
                kDADiskDescriptionVolumePathKey);

char buf[MAXPATHLEN];
if (CFURLGetFileSystemRepresentation(fspath, false, (UInt8 *)buf, sizeof(buf))) {
    printf("Disk %s mounted at %s\n",
        DADiskGetBSDName(disk),
        buf);

    /* Print the complete dictionary for debugging. */
    CFShow(diskinfo);
} else {
    /* Something is *really* wrong. */
}
```

For a complete list of dictionary keys, see the Constants section in _[DADisk.h Reference](https://developer.apple.com/documentation/diskarbitration/dadisk.h)_.

In some rare situations, you may need to obtain additional information about a disk beyond what is available from Disk Arbitration. If you do, you can call [DADiskCopyIOMedia](https://developer.apple.com/documentation/diskarbitration/1401888-dadiskcopyiomedia) to obtain an `io_service_t` object, which is the user-space representation of an [IOMedia](https://developer.apple.com/documentation/kernel/iomedia) object. You can manipulate this object just as you would any I/O Registry object.

For example, you can obtain a Core Foundation dictionary with the media’s I/O Registry properties by calling [IORegistryEntryCreateCFProperties](https://developer.apple.com/documentation/iokit/1514310-ioregistryentrycreatecfpropertie) on the resulting object.

The properties in an I/O Registry dictionary are defined in the I/O Kit Framework. For more information, see _[I/O Kit Framework Reference](https://developer.apple.com/documentation/iokit)_.

To mount or unmount a volume, call [DADiskMount](https://developer.apple.com/documentation/diskarbitration/1492772-dadiskmount) or [DADiskUnmount](https://developer.apple.com/documentation/diskarbitration/1492758-dadiskunmount). If you care whether the mount or unmount was successful, you must also provide a callback to handle the result.

Alternatively, you can call [DADiskMountWithArguments](https://developer.apple.com/documentation/diskarbitration/1492714-dadiskmountwitharguments) if you need to pass additional options to the `mount` command. This command takes a null-terminated array of [CFStringRef](https://developer.apple.com/documentation/corefoundation/cfstringref) values, each of which becomes an argument to the `mount` command. You can find the most common options in the manual page for `mount`. For additional volume-format-specific options, see the manual page for specific mount commands, such as `mount_hfs`.

For each of these functions, the callback function takes three parameters: a [DADiskRef](https://developer.apple.com/documentation/diskarbitration/dadisk) object, a [DADissenterRef](https://developer.apple.com/documentation/diskarbitration/dadissenter) object, and a context pointer (passed as a parameter when you register the callback). If the operation was successful, the dissenter object is `NULL`. Otherwise, it provides information about why the operation failed.

For example, the following snippet unmounts a volume:

```
void unmount_done(DADiskRef disk,
    DADissenterRef dissenter,
    void *context);

...

DADiskUnmount(disk, kDADiskUnmountOptionDefault,
    unmount_done, NULL);

...

void unmount_done(DADiskRef disk,
    DADissenterRef dissenter,
    void *context)
{
    if (dissenter) {
        /* Unmount failed. */
        char buf[MAXPATHLEN];
        if (CFURLGetFileSystemRepresentation(fspath, false, (UInt8 *)buf, sizeof(buf))) {
            fprintf(stderr, "Unmount failed (Error: 0x%x Reason: %s).  Retrying.\n",
                DADissenterGetStatus(dissenter),
                buf);
        } else {
            /* Something is *really* wrong. */
        }
    } else {
        /* Do something. */
    }
}
```

The most common error code values (errors specific to disk arbitration) are described in the `DAReturn` enumeration. However, this function can also potentially return any other error code in the `mach_error_t` space (UNIX errors, and so on).

Mounting a volume is similar except that you can specify a [CFURLRef](https://developer.apple.com/documentation/corefoundation/cfurl) object with the mount point path (or pass `NULL` to mount the volume at the standard location). For example:

```
unsigned char *mppath = "/mnt/mydisk";

path = CFURLCreateFromFileSystemRepresentation(
    kCFAllocatorDefault,
    mppath,
    strlen(mppath),
    true);

DADiskMountWithArguments(disk, path, kDADiskMountOptionDefault,
    mount_complete_callback, NULL,
    NULL);
```


Ejecting a disk is similar to unmounting a volume. There are two key differences:

- You can eject only a whole-disk partition (`/dev/disk0`, for example), not a leaf partition (`/dev/disk0s3`, for example). If you are starting from a leaf partition, you must first obtain the whole disk partition that contains it.
- You must unmount all volumes on a disk before ejecting it. To ensure that all volumes are unmounted (if possible), first call [DADiskUnmount](https://developer.apple.com/documentation/diskarbitration/1492758-dadiskunmount), passing the whole disk partition as the disk argument, and setting the `kDADiskUnmountOptionWhole` flag in the unmount options.

To get the whole disk partition that contains a given leaf partition, use [DADiskCopyWholeDisk](https://developer.apple.com/documentation/diskarbitration/1401828-dadiskcopywholedisk). For example:

```
DADiskRef wholedisk = DADiskCopyWholeDisk(disk);
```

The following snippet, given a [DADiskRef](https://developer.apple.com/documentation/diskarbitration/dadisk) object associated with a single partition (called `partition`), unmounts all volumes on the underlying disk, then ejects the disk:

```
void unmount_done(DADiskRef disk,
    DADissenterRef dissenter,
    void *context);
void eject_done(DADiskRef disk,
    DADissenterRef dissenter,
    void *context);

...

/* Unmount all volumes */
DADiskRef wholedisk = DADiskCopyWholeDisk(partition);
DADiskUnmount(wholedisk, kDADiskUnmountOptionWhole,
    unmount_done, NULL);
CFRelease(wholedisk);

...

/* In the unmount callback, eject the volume. */
void unmount_done(DADiskRef disk,
    DADissenterRef dissenter,
    void *context)
{
    if (dissenter) {
        ...
    } else {
        DADiskEject(disk, kDADiskEjectOptionDefault,
            eject_done, NULL);
    }
}

/* Eject callback. */
void eject_done(DADiskRef disk,
    DADissenterRef dissenter,
    void *context)
{
    if (dissenter) {
        ...
    } else {
        ...
    }
}
```

[Next](Document%20Revision%20History.md)[Previous](Using%20Disk%20Arbitration%20Notification%20and%20Approval%20Callbacks.md)

