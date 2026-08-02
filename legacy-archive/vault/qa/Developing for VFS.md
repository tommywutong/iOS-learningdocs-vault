---
title: Developing for VFS
apple_id: DTS10002278
resource_type: QA
platform: macOS
topic: Data Management
technology: null
published: '2006-12-22'
source_url: https://developer.apple.com/library/archive/qa/qa1242/_index.html
archived_at: '2026-07-18T02:30:17.716241Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1242

# Developing for VFS

## Q:  Does Apple support the development of external file systems (VFS plug-ins) on Mac OS X? Where can I find information about developing such a file system?

A: Does Apple support the development of external file systems (VFS plug-ins) on Mac OS X? Where can I find information about developing such a file system?

The answer depends on what type of file system you're developing.

A __leaf file system__ works independently of other file systems. Leaf file systems include:

- __local file systems__ — These talk straight to a block storage device, which is typically attached to the computer directly (for example, an ATA hard disk). HFS Plus is an example of a local file system.
- __network file systems__ — A network file system translates each file system operation into the corresponding network commands and transmits those to a file server. Mac OS X supports a number of network file systems, including AFP, NFS, and SMB/CIFS.
- __cluster file systems__ — A cluster file system combines the previous two approaches, using network commands for metadata operations and block storage commands for data transfer (typically via a Storage Area Network, or SAN). Xsan is Apple's cluster file system.

Apple supports the development of leaf file systems for all versions of Mac OS X. However, the rules have changed substantially, and for the better, in Mac OS X 10.4 Tiger.

Prior to the introduction of Mac OS X 10.4 Tiger, the BSD portions of the Mac OS X kernel were not architected for binary compatibility. Implementing a VFS plug-in required intimate knowledge of the kernel's internals, and the resulting product embedded that knowledge, making it very brittle. The slightest change to the kernel (reordering the fields within a structure, for example) would break all VFS plug-ins.

With Mac OS X 10.4 Tiger, Apple has solved this problem by introducing a VFS Kernel Programming Interface (KPI). This KPI isolates your VFS plug-in from kernel changes. For example, you no longer access fields in kernel structures directly; rather you call accessor functions that are supplied by the KPI. By using this KPI you can develop a VFS plug-in with the expectation that it will be compatible with future systems.

This sounds like file system nirvana, right? Alas, there are still a few things to worry about.

- There is no binary compatibility for VFS plug-ins between pre-10.4 systems and 10.4. If your product has to support pre-10.4 systems, you have to develop and ship two VFS plug-ins: one for pre-10.4, and one for 10.4 and beyond. There are ways to minimize the pain (for example, you can create an internal abstraction layer that isolates the bulk of your code from these differences), but no way to eliminate it entirely.
- If you're porting a VFS plug-in to the Mac OS X 10.4 KPI from another UNIX platform, you will notice that certain well known UNIX kernel structures (such as `struct uio`) are now opaque. That is, you can't directly access the fields of `struct uio`; you must call the appropriate accessor functions instead.

  This change is a direct consequence of our binary compatibility requirement, but it can cause problems if you have a cross platform code base. The only good solution is to change all of your code to use some form of macros to access these fields, and then define the macros appropriately for the platform.
- Documentation for the VFS KPI is still rather rudimentary. Apple will rectify this in the future
  (r. 3524590)
  ; in the meantime, this Q&A includes a list of references to documentation and other resources.

If you're developing a VFS plug-in, you may find the following resources useful.

- Mac OS X's VFS architecture is derived from 4.4BSD. "The Design and Implementation of the 4.4BSD Operating System" (ISBN: 0-201-54979-4) includes a good overview of VFS on that system. As there are key differences between 4.4BSD and Mac OS X (KPIs, the Unified Buffer Cache, changes to support HFS semantics, and more), you should not consider this book authoritative.
- For general information about Mac OS X kernel programming, see the [documentation](https://developer.apple.com/documentation/Darwin/Kernel-date.html) on the Apple developer web site.
- There are a number of [DTS Q&As](https://developer.apple.com/technicalqas/Darwin/idxFileManagement-date.html) that cover VFS. These Q&As cover the most frequently encountered gotchas with VFS development on Mac OS X, and they're well worth a look.
- The following VFS plug-ins were written specifically as sample code:

  - [Sample Code 'EmptyFS'](https://developer.apple.com/samplecode/EmptyFS/index.html) is a very simple VFS plug-in; its volumes are completely empty (except for the root directory). The purpose of this sample is to create the minimal VFS plug-in that builds and runs. You can use EmptyFS to explore VFS behaviour, or as a template for your own VFS plug-in.
  - [Sample Code 'MFSLives'](https://developer.apple.com/samplecode/MFSLives/index.html) is a sample VFS plug-in that implements read-only access to the Macintosh File System (MFS) volume format. MFS is an excellent volume format for sample code because it's very simple but it allows you to exercise the code paths associated with Macintosh-specific metadata (specifically, Finder info, multi-fork files, and volfs).
- The source for a number of existing file systems is available in [Darwin](https://developer.apple.com/darwin/) (the open source underpinnings of Mac OS X). I recommend the DOS/FAT file system (the "msdosfs" project) and the WebDAV file system (the "webdavfs" project).

If you have technical questions, there are a variety of mailing lists for free community-based support (I recommend the [darwin-kernel](http://www.lists.apple.com/darwin-kernel) mailing list) and Apple [Developer Technical Support](https://developer.apple.com/technicalsupport/index.html) for paid support.

A __stacking file system__ (sometimes called a __filter file system__) sits on top of another file system and modifies its behavior in some way. The canonical example of a stacking file system is an encryption file system. You could stack this file system on top of any existing file system to provide encryption support.

Apple does not support the development of stacking VFS plug-ins on Mac OS X
(r. 4383626)
. We've taken this position because, in our opinion, it's not possible to create a stacking VFS plug-in that:

- works reliably
- does not severely impinge on system performance
- has any hope of binary (or even source-level) compatibility with future systems

If you have a problem that can only be solved via a stacking file system, please let us know by mailing [Developer Technical Support](mailto:dts@apple.com). While we can't support your development, we are interested in gathering information about what developers need and why. This feedback will guide our long-term approach to this question. We may also be able to suggest an alternative design that does not require stacking.

Finally, there are a number of third party developers who are working in this realm. If you are absolutely determined to develop an unsupported stacking VFS plug-in, you will find some help on the Internet.

Developing a VFS plug-in for Mac OS X is hard. There are a number of factors that contribute to the difficulty:

- File systems are inherently complex.
- File systems must be very reliable.
- Your code is executed within the kernel, which is a more difficult programming environment than user space.
- Your file system can be accessed by all applications, which make compatibility engineering and testing difficult.

All-in-all, it's much better if you can avoid developing a file system. Moreover, if you must develop a file system, it's better if you can push as much of that development into user space as possible.

There are two well known techniques for minimising the amount of kernel code that you have to write.

- __NFS server__ — You can avoid writing any kernel code by writing a local NFS server, running it on the user's computer, and then using Apple's built-in NFS client to mount that server in the file system hierarchy. While it might seem convoluted, this approach is relatively simple and effective: Apple uses it to implement the automount and FTP file systems.

  Because of the multiple round trips in and out of the kernel, this approach is not appropriate for a data- or metadata-intensive file system.
- __kernel/user hybrid__ — This approach places the bulk of the code in a user space daemon, with an in-kernel stub file system that redirects requests to the daemon. This is how Apple's WebDAV file system works. It has the advantage that you get total control over how your file system appears to the user, while keeping most of the code in user space.

  A hybrid approach is also more suited to performance sensitive applications because you choose which data (or metadata) is generated (or cached) by the kernel, and which is left up to the daemon. The WebDAV file system has a particularly interesting take on this: in WebDAV the daemon caches data in files on the local hard disk, and the kernel stub can service read and write requests directly from those files.

Finally, Mac OS X provides specific APIs to solve problems that might otherwise require a stacking file system.

- I/O Media filter scheme drivers can be used to implement block-level encryption. While this isn't an exact replacement for a stacked encryption file system (each has its own advantages and disadvantages), it goes a long way towards meeting the user-level goal.

  See [Sample Code 'SampleFilterScheme'](https://developer.apple.com/samplecode/SampleFilterScheme/index.html) for an example of how to do this.
- Mac OS X 10.4 introduces a new KPI, Kernel Authorization (or Kauth), which can be used to implement an anti-virus file scanner. Kauth is documented in [Technical Note TN2127, 'Kernel Authorization'](https://developer.apple.com/technotes/tn2005/tn2127.html), with its associated [Sample Code 'KauthORama'](https://developer.apple.com/samplecode/KauthORama/index.html).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-12-22 | Added links to EmptyFS and MFSLives, and the Kauth documentation and sample code. Added a bug number for VFS documentation. |
| 2006-03-16 | Added bug number to track stacking VFS requirement. |
| 2005-05-24 | Update for Mac OS X 10.4 Tiger. |
| 2003-03-26 | New document that describes Apple's position on developing external file systems (VFS plug-ins) for Mac OS X. |

