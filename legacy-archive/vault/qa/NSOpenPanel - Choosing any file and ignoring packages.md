---
title: NSOpenPanel - Choosing any file and ignoring packages
apple_id: DTS10004212
resource_type: QA
platform: macOS
topic: Data Management
technology: AppKit
published: '2007-01-25'
source_url: https://developer.apple.com/library/archive/qa/qa1468/_index.html
archived_at: '2026-07-18T02:30:57.008048Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1468

# NSOpenPanel - Choosing any file and ignoring packages

## Q:  How do I setup `NSOpenPanel` to exclude file packages?

A: How do I setup `NSOpenPanel` to exclude file packages?

You need to implement the delegate method:

`- (BOOL)panel:(id)sender shouldShowFilename:(NSString*)filename`

In this method you must filter out file system objects that are packaged directories.

The Finder and `NSOpenPanel` treat packaged directories differently than other directories. Instead of displaying the contents of the packaged directory, they treat it as if it were a single file. Packaged directories usually have the extension: `.app`, `.bundle`, `.framework`, `.plugin`, `.kext`. If your application wishes to deal with only files, excluding these types of packages, you need to alter the behavior of `NSOpenPanel`.

As you setup up your `NSOpenPanel`, make sure you become its delegate by calling:

`[openPanel setDelegate: self];`

Proceed to implement the following delegate method to only allow choosing files and not packages.

__Listing 1__  The delegate method to filter out packaged files.

```objc
- (BOOL)panel:(id)sender shouldShowFilename:(NSString*)filename {     BOOL showObject = YES;      NSDictionary* fileAttribs = [[NSFileManager defaultManager]                                     fileAttributesAtPath:filename traverseLink:YES];     if (fileAttribs)     {         // check for packages         if ([NSFileTypeDirectory isEqualTo:[fileAttribs objectForKey:NSFileType]])         {             if ([[NSWorkspace sharedWorkspace] isFilePackageAtPath:filename] == NO)                 showObject = YES; // it's a folder, OK to show             else                 showObject = NO; // it's a packaged directory, don't show         }         else         {             showObject = YES; // it's a file, OK to show         }     }      return showObject; }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-01-25 | New document that explains how to configure NSOpenPanel to filter only files and ignoring packages. |

