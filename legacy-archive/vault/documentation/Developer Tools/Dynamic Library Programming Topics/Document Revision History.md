---
title: Dynamic Library Programming Topics
apple_id: TP40001869
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/DynamicLibraries/990-Revision-1.9/history.html
archived_at: '2026-07-15T07:24:28.228480Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dynamic Library Programming Topics](Introduction.md)


[Previous](Logging%20Dynamic%20Loader%20Events.md)

# Document Revision History

This table describes the changes to _Dynamic Library Programming Topics_.

| __Date__ | __Notes__ |
| 2012-07-23 | Updated to use automatic reference counting. |
|  | Updated reference software to OS 10.7 and the Xcode 4.3.3 Command Line Tools component. |
|  | Adopted automatic reference counting (ARC) in Objective-C–based code listings. |
|  | Replaced use of GCC (`gcc`) with LLVM compiler (`clang`). |
| 2012-06-11 | Update example code to new initializer pattern. |
| 2009-02-26 | Added information about run-path dependent libraries. |
|  | Added [Run-Path Dependent Libraries](Run-Path%20Dependent%20Libraries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmbwfvjvomi). |
| 2009-02-04 | Made minor corrections. |
|  | Fixed small errors in content and example code. Switched to using `~/include` and `~/lib` instead of `/usr/local/include` and `/usr/local/lib` as working locations for headers and libraries. |
| 2006-11-07 | Added information on using libtool to create libraries and on locating external resources using file-path macros. |
|  | Added details about `@executable_path` and `@loader_path` in [Locating External Resources](Dynamic%20Library%20Design%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdamjtfvjvomrr). |
|  | Added tip on using libtool to build dynamic libraries in [Setting the Library’s Version Information](Creating%20Dynamic%20Libraries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanztfvjvomrq). |
| 2006-09-05 | Added information about the creation and usage of private embedded frameworks. |
|  | Added information to [Using Dynamic Libraries](Using%20Dynamic%20Libraries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcobsfvjvomjq) > [Installing Dependent Libraries](Using%20Dynamic%20Libraries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcobsfvjvomjs). |
| 2006-02-07 | Made minor correctness changes. |
|  | Removed extraneous code lines from [Listing 3](Dynamic%20Library%20Usage%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsmryfvjvoni). |
| 2005-08-11 | Corrected errors and typos. |
|  | Changed `LS_LIBRARY_PATH` to `LD_LIBRARY_PATH` in [Using Dynamic Libraries](Using%20Dynamic%20Libraries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcobsfvjvomjq). |
|  | Changed `DYLD_PRIINT_STATISTICS` to `DYLD_PRINT_INITIALIZERS` and corrected description for `DYLD_PRINT_SEGMENTS` in [Logging Dynamic Loader Events](Logging%20Dynamic%20Loader%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanzxfvjvomi). |
| 2005-06-04 | New document that shows how to correctly design, implement, and use dynamic libraries. |

[Previous](Logging%20Dynamic%20Loader%20Events.md)

