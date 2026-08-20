---
title: Text Encodings in VFS
apple_id: DTS10001705
resource_type: QA
platform: macOS
topic: Data Management
technology: System
published: '2011-09-30'
source_url: https://developer.apple.com/library/archive/qa/qa1173/_index.html
archived_at: '2026-07-18T02:30:12.039057Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1173

# Text Encodings in VFS

## Q:  I'm writing a file system (VFS) plug-in for Mac OS X. How do I handle text encodings correctly?

A: The lowest levels of Mac OS X—which includes both the POSIX-level API and the VFS plug-in KPI—treat file names as UTF-8 encoded Unicode strings. This raises a number of interesting issues.

This Q&A assumes that you're familiar with the terms __precomposed__ and __decomposed__ Unicode. If that's not the case, there's a short explanation in [Technical Q&A QA1235, 'Converting to Precomposed Unicode'](https://developer.apple.com/qa/qa2001/qa1235.html).

Your target volume format should define whether it uses precomposed or decomposed Unicode. For example, HFS Plus uses decomposed Unicode whereas UDF and SMB use precomposed Unicode.

Unfortunately, some volume formats (for example, NFS) have no accepted standard. This presents additional challenges, which are covered below.

When returning names to higher layers (for example, from your `readdir` vnode operation), you should return decomposed names. If your underlying volume format uses precomposed names, you should convert any precomposed characters to their decomposed equivalents before returning them to the system.

In most cases, high-level software will pass decomposed names to your file system. However, this is not guaranteed. There are a variety of circumstances (some discussed below) where your file system is passed precomposed names. Regardless of their incoming state, you should always convert names to the encoding scheme required by your underlying volume format. Thus, if your underlying volume format requires precomposed names, you should convert names to their precomposed variant before writing them to disk. Similarly, if your volume format requires decomposed names, you should decompose any precomposed characters.

This raises the question of what to do if your underlying volume format does not define a standard. There is no good solution here. You can choose to pass through names unchanged, which is what Apple's NFS implementation does, or provide some user interface for the user to choose (similar to the Encoding popup in the Finder's Get Info window for an original HFS (Mac OS Standard) volume). Either way the user experience will not be ideal.

In user space it is easy to convert between precomposed and decomposed Unicode; see [Technical Q&A QA1235, 'Converting to Precomposed Unicode'](https://developer.apple.com/qa/qa2001/qa1235.html) for more details on doing this. However, these APIs are not callable from inside the kernel, where your VFS plug-in resides. Fortunately, starting with Mac OS X 10.5 the kernel provides a KPI for manipulating Unicode. For details, see the various routines defined in `<sys/utfconv.h>`, including `utf8_normalizestr`.

In theory the techniques described above can cause compatibility problems for applications. For example, if an application creates a file using a precomposed name and then iterates through the directory looking for that file using a simple binary string comparison, it won't find the file. In practice this is rarely a problem. Don't forget that the primary file system, HFS Plus, works this way, so any program that's incompatible with your file system will also be incompatible with HFS Plus.

Most of Apple's built-in file systems use the techniques described above. Two notable exceptions are NFS and UFS. Of these, NFS is the most troublesome because NFS volumes can be shared with non-Mac clients that create files with precomposed characters in their names, and the Mac OS X NFS client does not decompose them before returning them to applications. If the user copies files from an NFS volume to your volume using a naive copy program (like the `cp` command line tool), the copy program will copy the files without decomposing the names. Thus your file system will by asked to create files with precomposed names. Your file system must be prepared to handle this, as described above.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-09-30 | Updated to describe the latest techniques and, specifically, to recommend the use of the <sys/utfconv.h> KPIs. |
| 2003-02-10 | New document that explains how to handle text encodings correctly when writing a file system (VFS) plug-in for Mac OS X. |

