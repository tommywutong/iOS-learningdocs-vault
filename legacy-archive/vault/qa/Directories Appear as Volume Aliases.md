---
title: Directories Appear as Volume Aliases
apple_id: DTS10003324
resource_type: QA
platform: macOS
topic: Data Management
technology: CoreServices
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/qa/qa1351/_index.html
archived_at: '2026-07-18T02:30:25.762371Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1351

# Directories Appear as Volume Aliases

## Q:  I'm writing a network file system (VFS plug-in KEXT) for Mac OS X. Everything seems to work fine at the BSD layer, but the Finder is very confused, showing every directory on my file system as a volume alias. How can I fix this?

A: I'm writing a network file system (VFS plug-in KEXT) for Mac OS X. Everything seems to work fine at the BSD layer, but the Finder is very confused, showing every directory on my file system as a volume alias. How can I fix this?

To fix this problem you must ensure that every object on your volume returns the same value in the `st_dev` field returned by `stat`. In addition, this value must match the device number for the volume itself. The system gets the device number for a volume by calling `statfs` and extracting the device number from the first word of the `f_fsid` array in the `statfs` structure. You must make sure that this number matches the value you're returning from `stat`.

The typical data flow for this value is as follows.

- For a local file system, your mount entry point (`examplefs_mount`) is called with arguments that contain a path to a device node. Your file system should look up this path (using `namei`) to find the vnode for the device (let's call this `devvp`). It should then initialize the volume's `f_fsid` as follows.


```swift
mp->mnt_stat.f_fsid.val[0] = (long) devvp->v_rdev; mp->mnt_stat.f_fsid.val[1] = mp->mnt_vfc->vfc_typenum;
```
- For a network file system, your mount entry point (`examplefs_mount`) should initialize the volume's `f_fsid` by calling `vfs_getnewfsid`. This sets up the `f_fsid` to a synthetic value that uniquely identifies the volume.
- In your `statfs` entry point (`examplefs_statfs`), make sure that you return sensible results in the `f_fsid` field of the `statfs` structure. In most cases you don't need to do anything here because the system gets the initial value of this structure from your volume's `mnt_stat` structure.
- In your getattr entry point (`examplefs_getattr`), return the device number (`mp->mnt_stat.f_fsid.val[0]`) in the `vap->va_fsid` so that the kernel can copy that value into the `st_dev` field of the `stat` structure that it returns to the caller.
- If your volume supports the `ATTR_CMN_DEVID` attribute, its value must match the `st_dev` value returned via `stat`.
- If your volume supports the `ATTR_CMN_FSID` attribute, its value must match the `f_fsid` value returned via `statfs`.

The rest of this document explains how mixing up your device numbers leads to the observed symptoms. If all you want to do is fix this problem and move on to the next bug, you can safely skip it. On the other hand, if you want to learn a little about the interaction between Carbon File Manager and the BSD layer of Mac OS X, by all means read on.

To understand what's going you need to understand the difference between how BSD and Carbon represent the file system as a whole. Under BSD the file system is a single tree. Each volume is mounted as a directory in the tree (a mount point) and moving through that directory can take you from one volume to another. BSD programs are aware of this and can cope with it just fine.

On the other hand, Carbon represents the file system as a forest of trees. Each volume has its own root directory, with a tree of directories spread out underneath it. Because each volume is a separate entity, Carbon programs do not expect that moving within a volume's directory structure will take them to a different volume.

Mac OS X must provide BSD semantics for BSD programs and Carbon semantics for Carbon programs. The BSD semantics are the native file system semantics on Mac OS X, so that part is easy. Providing Carbon semantics is trickier. Carbon File Manager is responsible for emulating Carbon semantics on top of the native BSD API. This involves a number of subtle tricks, some of which can trip up file system implementers. Thus, this is just one example of a general problem: you must carefully code your VFS plug-in in order for Carbon programs to work properly.

This particular case revolves around mount points. When Carbon File Manager encounters a mount point within a directory, it can't pass the mount point directly back to the program because Carbon programs don't expect to cross volumes when navigating the directory tree. Instead, Carbon File Manager returns what's known as a synthetic alias. To a Carbon program this synthetic alias looks like an alias file (the `kIsAlias` bit is set in the file's Finder flags). If the Carbon program wants to traverse this 'alias', it calls the Alias Manager to resolve it. The Alias Manager recognizes the synthetic alias and resolves it by returning a reference to the root directory of the destination volume. Thus, to a Carbon program, a mount point looks like an alias to the root directory of the destination volume.

In this case, Carbon File Manager is interpreting every directory on your file system as a mount point, and thus Carbon programs (including the Finder) see every directory as an alias to a volume. The key question is why. It turns out that Carbon File Manager uses the device number associated with a file system object (the `st_dev` field of the `stat` structure returned by `stat`) to determine mount point changes. When examining a directory, Carbon File Manager compares the `st_dev` of the directory with the device number associated with the volume on which the directory resides. If they're different, as is the case with your file system, it assumes that the directory represents a mount point. At that point it returns a synthetic alias for the volume, which the Finder displays as a volume alias. If you make all of the device numbers match (as described above), Carbon File Manager will recognise your directories as directories, and the problem goes away.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2018-06-04 | Moved to Retired Documents Library. |
| 2004-05-25 | Discusses how VFS plug-ins should handle device numbers to ensure compatibility with Carbon applications. |
|  | Discusses how VFS plug-ins should handle device numbers to ensure compatibility with Carbon applications. |
|  | New document that discusses how VFS plug-ins should handle device numbers to ensure compatibility with Carbon applications. |

