---
title: QuickTime for Windows returns bdNamErr (-37) error with long Windows file names
apple_id: DTS10003508
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2008-08-08'
source_url: https://developer.apple.com/library/archive/qa/qa1413/_index.html
archived_at: '2026-07-18T02:30:32.166198Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1413

# QuickTime for Windows returns bdNamErr (-37) error with long Windows file names

## Q:  I'm getting the `bdNamErr` (-37) error when calling `NativePathNameToFSSpec` on my Windows PC with QuickTime 7. The paths I'm using are perfectly valid Windows paths to files on my hard drive. What am I doing wrong? Also, can I use the data reference APIs such as `QTNewDataReferenceFromFullPathCFString`, `QTNewDataReferenceFromCFURL` and so on to avoid these types of errors?

A: There's a limitation in QuickTime prior to version 7.4 which restricts any file name plus extension to 63 characters or less. The full path may still be `MAX_PATH` (see WINDEF.H) characters long, but the file name must be 63 characters or less.

Also, the text encoding of the pathname passed to `NativePathNameToFSSpec` must match the system code page of the Windows system. This means you cannot use Unicode pathnames (either UTF-8 or UTF-16) with this function.

Starting with QuickTime 7.4, the limitation on the length of a file leaf name is now 255 characters, rather than 63 characters as it was in earlier releases. The full path must still be less than or equal to `MAX_PATH` characters.

In addition, the data reference APIs (`QTNewDataReferenceFromFullPathCFString`, `QTNewDataReferenceFromCFURL` and so on) in QuickTime 7.4 now provide more robust support for Unicode pathnames, though these pathnames must also be less than or equal to `MAX_PATH` characters.

The `FSSpec` data structure does not allow Unicode characters. Therefore, it is not possible to represent a file whose pathname contains Unicode characters. With QuickTime 7.4, the Carbon Resource File APIs are not compatible with Unicode pathnames.

You can obtain the long form by calling the `GetLongPathName` Windows API.

- [NativePathNameToFSSpec](https://developer.apple.com/documentation/QuickTime/APIREF/nativepathnametofsspec.htm)
- [QTNewDataReferenceFromFullPathCFString](https://developer.apple.com/documentation/QuickTime/APIREF/qtnewdatareferencefromfullpathcfstring.htm)
- [QTNewDataReferenceFromCFURL](https://developer.apple.com/documentation/QuickTime/APIREF/qtnewdatareferencefromcfurl.htm)
- [Modernizing QuickTime Applications](https://developer.apple.com/technotes/tn2005/tn2140.htm)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-08-08 | Updated to reflect new behavior in QuickTime 7.4. |
| 2005-10-04 | Added information about Data Reference APIs and Unicode pathnames. |
| 2005-02-22 | New document that describes how QuickTime may return bdNamErr (-37) error on Windows if file name is > 63 characters |

