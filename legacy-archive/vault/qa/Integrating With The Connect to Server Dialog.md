---
title: Integrating With The Connect to Server Dialog
apple_id: DTS10003449
resource_type: QA
platform: macOS
topic: Data Management
technology: null
published: '2006-11-16'
source_url: https://developer.apple.com/library/archive/qa/qa1387/_index.html
archived_at: '2026-07-18T02:30:29.509491Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1387

# Integrating With The Connect to Server Dialog

## Q:  I'm writing a network file system (VFS plug-in) for my custom network file system protocol. How do I integrate with the Finder's Connect to Server dialog? I want to support browsing and allow the user to enter a URL in the Server Address field.

A: I'm writing a network file system (VFS plug-in) for my custom network file system protocol. How do I integrate with the Finder's Connect to Server dialog? I want to support browsing and allow the user to enter a URL in the Server Address field.

It is currently not possible for third party network file systems to fully integrate with the Connect to Server dialog. There are two aspects to this problem.

When you enter a URL in the Server Address field, the Finder calls the File Manager to mount the server volume (`FSMountServerVolumeAsync`). This extracts the URL scheme (the text before the colon) and uses that to load and run the appropriate URLMount plug-in. The structure of a URLMount plug-in is not publicly documented
(r. 3502170)
.

When you click the Browse button, the Finder opens a window that displays the contents of `/Network`. This directory is actually a mount point which automount populates using the NSL map. `automount` generates the NSL map by calling Network Service Location to find all network file system services. NSL does this by calling Open Directory (the Directory Services API), which in turn passes the job off to one or more of its plug-ins (as configured by the Directory Access utility).

The problem here is that, when `automount` searches for services using NSL, it searches for a fixed set of service types (URL schemes)
(r. 2888560)
. This list is currently `afp`, `smb`, `cifs`, `nfs`, `webdav`, and `ftp`. As your URL scheme does not appear in this list, your servers will not appear in `/Network`.

The only workaround currently available is for you to write a custom application that allows the user to mount your file system. Your custom application can support manually entering a URL, browsing, or any other mechanism appropriate for your product.

If you are developing a network file system that's affected by this issue, please contact [DTS](mailto:dts@apple.com) and let us know about your development efforts.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-11-16 | New document that describes problems integrating a third-party network file system with Finder's Connect to Server dialog. |

