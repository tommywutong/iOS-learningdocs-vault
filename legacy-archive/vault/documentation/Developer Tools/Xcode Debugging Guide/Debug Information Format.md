---
title: Xcode Debugging Guide
apple_id: TP40007057
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeDebugging/900-Debug_Information_Format/debug_information_format.html
archived_at: '2026-07-15T07:28:00.991757Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Debugging Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Mac%20OS%20X%20Low-Level%20Debugging.md)

# Debug Information Format

Xcode uses the DWARF debug information format to store your product’s debug data. In general, binaries created for debugging have debug information embedded in them. The debug information for release binaries, on the other hand, is normally stored in a separate file, the dSYM file. This practice reduces the size of the binaries delivered to users of your product, which results in faster downloads and less space used in media, such as DVDs.

In the unlikely event you need provide users with your product’s debug information (for example, to allow users of a framework to troubleshoot a problem in its operation and give you file and line number information about their call stacks), you send them the dSYM file that was generated alongside the release binary. You can also rely on dSYM files to symbolize crash logs sent by your customers.

The [DEBUG_INFORMATION_FORMAT (Debug Information Format)](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/XcodeBuildSettingRef/1-Build_Setting_Reference/build_setting_ref.html#//apple_ref/doc/uid/TP40003931-CH3-SW52) build setting lets you specify whether Xcode generates DWARF debug information and where to place it: In the binary or in a dSYM file along the binary, as shown in Figure 12-1.

__Figure 12-1__  A binary file and its dSYM file

!

Xcode uses the `dsymutil` tool to generate dSYM files. See the tool’s man page for more information about generating dSYM files.

[Next](Document%20Revision%20History.md)[Previous](Mac%20OS%20X%20Low-Level%20Debugging.md)

