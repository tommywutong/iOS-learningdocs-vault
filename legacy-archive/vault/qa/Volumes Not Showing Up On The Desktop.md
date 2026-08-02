---
title: Volumes Not Showing Up On The Desktop
apple_id: DTS10004154
resource_type: QA
platform: macOS
topic: Data Management
technology: null
published: '2006-12-20'
source_url: https://developer.apple.com/library/archive/qa/qa1491/_index.html
archived_at: '2026-07-18T02:31:29.671646Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1491

# Volumes Not Showing Up On The Desktop

## Q:  I'm writing a custom file system (VFS plug-in). I can mount my volume just fine at the BSD level, but its icon doesn't show up on the desktop. How can I make my file system's volumes show up on the desktop?

A: I'm writing a custom file system (VFS plug-in). I can mount my volume just fine at the BSD level, but its icon doesn't show up on the desktop. How can I make my file system's volumes show up on the desktop?

If you're developing a __local file system__ (using the terminology from [Technical Q&A QA1242, 'Developing for VFS'](https://developer.apple.com/qa/qa2001/qa1242.html)), you need to create a file system bundle and install it in `/System/Library/Filesystems`. The file system bundle format is not formally documented
(r. 3524590)
, but you can look at [Sample Code 'MFSLives'](https://developer.apple.com/samplecode/MFSLives/index.html) for an example. For a local file system, a valid file system bundle (including the embedded utility and mount tools) is sufficient for the system to probe and mount your file system, and for your volumes to automatically appear on the desktop.

This is, however, not sufficient for a __network file system__. A network file system must have a file system bundle (this allows the Finder to show the correct localized name in the Format field of the Get Info window), but that's not sufficient for your volumes to show up on the desktop automatically. For a network file system, the user typically does some explicit operation to mount a volume. For the built-in network file systems (AppleShare, SMB, and so on), the users mounts a volume using the Connect to Server dialog in the Finder, or by browsing `/Network`. There is currently no way for third party network file systems to integrate into these standard locations. See [Technical Q&A QA1387, 'Integrating With The Connect to Server Dialog'](https://developer.apple.com/qa/qa2004/qa1387.html) for the details.

If you follow the advice from that document and create your own mounting application, your volumes will still not show up on the desktop. You must explicitly notify the sytem when you mount a new volume. The mechanism for doing this is documented below.

In this context a __cluster file system__ works the same way as a network file system.

When you mount a new network volume, you must tell the system about it. You do this by calling the DiskArbitration routine `DiskArbDiskAppearedWithMountpointPing_auto`. This routine isn't part of the standard DiskArbitration framework headers, so you have to declare your own prototype for it. The correct prototype is shown in Listing 1.

__Listing 1__  DiskArbDiskAppearedWithMountpointPing_auto prototype

```
extern kern_return_t DiskArbDiskAppearedWithMountpointPing_auto(     char *   disk,     unsigned flags,     char *   mountpoint ) __attribute__((weak_import));  enum {     kDiskArbDiskAppearedEjectableMask              = 1 << 1,     kDiskArbDiskAppearedNetworkDiskMask            = 1 << 3 };
```

The parameters to this routine are:

- `disk` is the device on which the disk is mounted. In the case of a network volume, you can use any unique string. However, it must match the `f_mntfromname` value returned by statfs for your volume.
- `flags` must be `kDiskArbDiskAppearedEjectableMask | kDiskArbDiskAppearedNetworkDiskMask`.
- `mountpoint` is an absolute path to the directory on which the volume is mounted. Typically this is a unique subdirectory that you create within `/Volumes`.

This routine is part of the old (pre-Mac OS X 10.3), private, DiskArbitration framework interface. When we introduced a new, public DiskArbitration interface in Mac OS X 10.3, we didn't introduce a replacement for this routine because, in the long term, DiskArbitration will automatically learn about new network volumes by way of a kernel notification. So, ultimately, you won't need to call this routine for your volume to appear on the desktop. For that reason, we strongly recommend that you weak link against this symbol and, if it's not present, just don't call it.

For more information about this technique, see [Technical Note TN2064, 'Ensuring Backwards Binary Compatibility - Weak Linking and Availability Macros on Mac OS X'](https://developer.apple.com/technotes/tn2002/tn2064.html).

Finally, because you're calling the old, private DiskArbitration framework interface, you have to explicitly initialize that interface. You do this by calling `DiskArbInit`, the prototype of which is given in Listing 2. If you fail to do this, it's likely that `DiskArbDiskAppearedWithMountpointPing_auto` will fail with an error code of 5 (`KERN_FAILURE`).

__Listing 2__  DiskArbInit prototype

```
extern kern_return_t DiskArbInit(void) __attribute__((weak_import));
```

As with `DiskArbDiskAppearedWithMountpointPing_auto`, you should weak link to this routine and not call it if it's not present.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-12-20 | New document that describes how to make a volume from a third party VFS plug-in show up on the desktop. |

