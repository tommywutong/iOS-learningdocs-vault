---
title: Runtime Configuration Guidelines
apple_id: 10000170i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: null
published: '2009-10-19'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPRuntimeConfig/Articles/ConfigApplications.html
archived_at: '2026-07-15T08:16:27.209153Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Runtime Configuration Guidelines](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Environment%20Variables.md)

# Additional Configuration Tips

This chapter describes some miscellaneous techniques for configuring your application.

The `PkgInfo` file is an alternate way to specify the type and creator codes of your application or [bundle](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Bundle.html#//apple_ref/doc/uid/TP40008195-CH4). This file is not required, but can improve performance for code that accesses this information. Regardless of whether you provide this file, you should always include type and creator information in your information property list file using the `CFBundlePackageType` and `CFBundleSignature` keys, respectively.

The contents of the `PkgInfo` file are the 4-byte package type followed by the 4-byte signature of your application. Thus, for the TextEdit application, whose type is `'APPL'` and whose signature is `'ttxt'`, the file would contain the ASCII string “APPLttxt”.

If you have a Cocoa application, you can override many user defaults settings by specifying them on the command line. In addition, Cocoa recognizes a few additional arguments for opening and printing files. Table 1 lists some of the more commonly used command-line arguments for Cocoa applications.

__Table 1__  Command-line arguments for Cocoa applications

| Argument | Description |
| `-NSOpen`_fileName_ | Opens the specified file after the application finishes launching. Uses the `application:openFile:` method of the application’s delegate to open the file. |
| `-NSOpenTemp`_fileName_ | Opens the specified file as a temp file after the application finishes launching. Uses the `application:openTempFile:` method of the application’s delegate to open the file. |
| `-NSPrint`_fileName_ | Prints the specified file after the application finishes launching. Uses the `application:printFile:` method of the application’s delegate to print the file. |
| `-NSShowAllDrawing``<YES>` | Shows areas that are about to be drawn in yellow so that you can see which parts of your views are being updated. This is similar to the feature that is available through the Quartz Debug application but operates only on the specified application. |
| `-NSTraceEvents``<YES>` | Displays a running log of events received by the application. |

[Next](Document%20Revision%20History.md)[Previous](Environment%20Variables.md)

