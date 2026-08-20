---
title: Where do QuickTime extension files reside on Windows systems?
apple_id: DTS10002079
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2011-07-12'
source_url: https://developer.apple.com/library/archive/qa/qtw100/_index.html
archived_at: '2026-07-18T02:38:53.529490Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QTW100

# Where do QuickTime extension files reside on Windows systems?

## Q:  I'm creating a QuickTime extension (both a .qtx data fork and a .qtr resource fork file) and I'd like to know where to place the files so QuickTime will find them on Windows Systems.

A: There's an easy way to determine where they go -- use the QuickTime 7 `GetQTExtensionDirectory` function. This function returns the path of the QuickTime Extensions directory.

Here's a code snippet showing how to use this function:

__Listing 1__  Calling the `GetQTExtensionDirectory` to located the QuickTime extensions directory.

```
void doGetQTExtDirectory() {     char buffer[MAX_PATH+1];      /* get the QuickTime extensions directory */     UINT strLength = GetQTExtensionDirectory(buffer, MAX_PATH+1);     if (strLength > 0)     {         /*           the buffer now contains the extensions directory string...           */     }     else     {         /* Get the system error message for the last-error code */          DWORD lastErrCode = GetLastError();           /*          handle error here...          */     } }
```

There are also functions for locating the various other directories created by the QuickTime installer, such as the `GetQTApplicationDirectory` function for finding the QuickTime Applications directory, the `GetQTComponentDirectory` function for finding the QuickTime Components directory, and so on.

See the [QuickTime 7 for Windows Update Guide](https://developer.apple.com/documentation/QuickTime/Conceptual/QT7Win_Update_Guide/index.html) for more information.

For versions prior to QuickTime 7, use the string returned by the Win32 `GetSystemDirectory` function concatenated with the string "\QuickTime".

On Windows NT and Windows 2000, that's the

C:\Windows\System32\QuickTime

directory, and on Windows 95 and Windows 98, that's the

C:\Windows\System\QuickTime

directory.

QuickTime will also look in the system directory itself, but we prefer you put them in the folder "QuickTime" inside the system directory.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-07-30 | Revised for QuickTime 7 |
| 2000-09-05 | New document that describes where to locate QuickTime extension files on Windows systems. |

