---
title: Universal Binary Programming Guidelines, Second Edition
apple_id: TP40002217
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2009-02-04'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/universal_binary/universal_binary_revhx/universal_binary_revhx.html
archived_at: '2026-07-15T08:16:38.176671Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Universal Binary Programming Guidelines, Second Edition](Introduction.md)


[Previous](64-Bit%20Application%20Binary%20Interface.md)

# Document Revision History

This table describes the changes to _Universal Binary Programming Guidelines, Second Edition_.

| __Date__ | __Notes__ |
| 2009-02-04 | Made minor content additions. |
|  | Updated [Programmatically Detecting a Translated Application](Rosetta.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrrgawtemzzgu4ds) with details about the behavior of the `sysctl` call when working with the `proc_native` variable. |
| 2007-02-26 | Updated for Mac OS X v10.5. |
|  | Removed the Appendix “Using PowerPlant” because an Open Source version that supports Intel-based Macintosh computers is available. See [Metrowerks PowerPlant](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteobqgmzdm). |
|  | Replaced the content in [64-Bit Application Binary Interface](64-Bit%20Application%20Binary%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmznknlts) with cross-references to documents that are more thorough at describing the ABI. |
| 2007-01-08 | Added information on 64-bit and made technical corrections. |
|  | Added [64-Bit Application Binary Interface](64-Bit%20Application%20Binary%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmznknlts). |
|  | Added a note to [OpenGL](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteojsgyzda). |
|  | Revised the explanation of the return values for the code in [Listing A-4](Rosetta.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrrgawtemzzgi2ts). |
|  | Removed the code example in [Archived Bit Fields](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteojrha3di) because it was incorrect. |
| 2006-07-24 | Made a few minor technical corrections. |
|  | Revised [Network-Related Data](Swapping%20Bytes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugmwteojrgqztm). |
|  | Clarified how [Listing A-4](Rosetta.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrrgawtemzzgi2ts) works. |
| 2006-06-28 | Fixed link. |
|  | Added [PostScript Printing](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewvgvzs). |
|  | Redirected link from Kernel Extensions Reference to _[Kernel Framework Reference](https://developer.apple.com/documentation/kernel)_. |
| 2006-05-23 | Removed outdated links and made a few other minor changes. |
|  | Revised code regarding flippers to use an explicit `UInt16` pointer and to assign back to `dataptr` the advanced `countPtr`. |
|  | Updated instructions in [Troubleshooting](Rosetta.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrrgawtemzvhezdo). |
|  | Added information about the `CCSResourcesFileMapped` flag to “using PowerPlant”. |
|  | Removed links to documentation that is no longer relevant. |
|  | Added a note to “LStream.h” concerning reading and writing `bool` values. |
| 2006-04-04 | Corrected two function names. |
|  | Revised information in [32-Bit Application Binary Interface](32-Bit%20Application%20Binary%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugywviucykjcummjqge) so that it now only provides a link to the primary ABI reference. |
| 2006-03-08 | Improved wording and added information on Spotlight importers. |
|  | Added information to Objective-C Runtime: Sending Messages and Objective-C: Messages to nil. |
| 2006-02-07 | Improved the wording in several sections. |
|  | Revised wording in [Bit Shifting](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteojuguzdc), [Bit Test, Set, and Clear Functions: Carbon and POSIX](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteobtgaydq), [Troubleshooting](Rosetta.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrrgawtemzvhezdo), and [Guidelines for Swapping Bytes](Swapping%20Bytes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugmwteobugu3tc). |
|  | Revised code in [Listing A-4](Rosetta.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrrgawtemzzgi2ts) by adding a statement to handle versions of Mac OS that pre-date Rosetta. |
| 2006-01-10 | Updated content for Mac OS X v10.4.4. |
|  | Removed the note about preliminary documentation from [Introduction to Universal Binary Programming Guidelines](Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrqgqwviucykjcummjqge). |
|  | Changed Xcode 2.1 to Xcode 2.2 in various places throughout the document because this is the recommended version for building a universal binary. |
|  | Updated screenshots. |
|  | Updated information in [Disk Partitions](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteobthe3ds), [Finder Information and Low-Level File System Operations](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteobqg4yta), [Multithreading](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteojsgi2ta), [Objective-C: Messages to nil](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteojxguzta), [QuickTime Components](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteobqg44tm), [Runtime Code Generation](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteojsgu2da), and [Values in an Array](Swapping%20Bytes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugmwteojxg43tk). |
|  | Added the sections [Code on the Stack: Disabling Execution](Architectural%20Differences.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugawteobuhazde), [Extensible Firmware Interface (EFI)](Architectural%20Differences.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugawteobuha2tk), and [Mach Processes: The Task for PID Function](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteojxhe2te). |
|  | In [Rosetta](Rosetta.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrrgawviucykjcummjqge), updated the sections [What Can Be Translated?](Rosetta.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrrgawtemzwg42do) and [Forcing an Application to Run Translated](Rosetta.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrrgawtemzwhe3tq). |
|  | In [Rosetta](Rosetta.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrrgawviucykjcummjqge), added the section [Programmatically Detecting a Translated Application](Rosetta.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrrgawtemzzgu4ds). |
| 2005-12-06 | Made refinements to existing content. |
|  | Added code that shows how to swap bytes for values in an array. See [Values in an Array](Swapping%20Bytes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugmwteojxg43tk). |
|  | Added [Automator Scripts](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteojxgm2tk), [Dashboard Widgets](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteojxgm4dk), and [QuickTime Metadata Functions](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteojxgiyde). |
| 2005-11-09 | Updated for Xcode 2.2; includes pointers to newly revised tools documentation as well as improved guidelines and tips. |
|  | Revised [Building Your Code](Building%20a%20Universal%20Binary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrqgywtcnjzgq2da). |
|  | Added [Debugging](Building%20a%20Universal%20Binary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrqgywtenbsgy3ti). |
|  | Added information to [Pixel Data](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteobqgm4dk) on how to track down color problems. |
|  | Added the section [Quartz Bitmap Data](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteojwha3ds). |
|  | Added information about IP addresses and other “false” numerical values. |
|  | In several places throughout the book, added cross references to newly revised, relevant documentation. |
|  | Added clarification on the `long double` data type. See [Data Types](Architectural%20Differences.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugawteobsgi2da). |
|  | Added information about using the `PinRect` function. See [QuickDraw Routines](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteobshaztg). |
|  | Added information about the need for Xcode targets to be native. See [Build Assumptions](Building%20a%20Universal%20Binary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrqgywtemzwha3tc) and [Building Your Code](Building%20a%20Universal%20Binary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrqgywtcnjzgq2da). |
|  | Corrected information about how ATS for Fonts handles font resources. See [Font-Related Resources](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteojwgm4dc). |
|  | Changed extended markup language to extensible markup language. |
|  | Improved the grammar in [Objective-C: Messages to nil](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteojxguzta). |
|  | Fixed a link to information on Hyper-Threading Technology. See the [See Also](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteobwgq3ds) section in [Guidelines for Specific Scenarios](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewviucykjcummjqge). |
|  | Made numerous editorial changes throughout. |
| 2005-10-04 | Made technical improvements and minor editorial changes throughout. |
|  | Added a few resources to See Also in [Building a Universal Binary](Building%20a%20Universal%20Binary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrqgywviucykjcummjqge). |
|  | Changed the title of the Appendix Fast Matrix Multiplication to [Architecture-Independent Vector-Based Code](Architecture-Independent%20Vector-Based%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrrgmwviucykjcummjqge). |
|  | Added new sections to the chapter [Guidelines for Specific Scenarios](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewviucykjcummjqge). See [FireWire Device Access](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteojvgezdm) and [USB Device Access](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteojvga4do). |
|  | Added information about a relevant technical note to [QuickTime Components](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteobqg44tm). |
|  | Added an example of a color issue to [Troubleshooting Your Built Application](Building%20a%20Universal%20Binary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrqgywtemzyg4yti). |
|  | Revised the section [Objective-C: Messages to nil](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteojxguzta). |
|  | Revised the code for swapping floating-point values. See [Floating-Point Values](Swapping%20Bytes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugmwteojrgaytm). |
|  | Add a reference to _[SDK Compatibility Guide](../../Developer%20Tools/SDK%20Compatibility%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3dg2i)_ in the chapter [Building a Universal Binary](Building%20a%20Universal%20Binary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrqgywviucykjcummjqge). |
|  | Made corrections to the section [OpenGL](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteojsgyzda). |
| 2005-09-08 | Updated a substantial amount of task and conceptual information. |
|  | Completely replaced information related to PowerPlant. |
|  | Removed most of the content from [Preparing Vector-Based Code](Preparing%20Vector-Based%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrqhawviucykjcummjqge) because the document _[AltiVec/SSE Migration Guide](../../Performance/AltiVec-SSE%20Migration%20Guide/Introduction%20to%20AltiVec-SSE%20Migration%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdomrz)_ provides a more complete discussion of porting AltiVec code to SSE. |
|  | Removed most of the content from the appendix titled _Application Binary Interface_ because the document _[OS X ABI Function Call Guide](../../Developer%20Tools/OS%20X%20ABI%20Function%20Call%20Guide/Introduction%20to%20OS%20X%20ABI%20Function%20Call%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkmrr)_ provides a more complete description of the IA-32 ABI for Intel-based Macintosh computers. |
|  | Added a section—[Java Applications](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteojwgmyte)—that provides information about Java on Intel-based Macintosh computers, including what happens under Rosetta. Added cross-references to a technical note on this topic to [Rosetta](Rosetta.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrrgawviucykjcummjqge). |
| 2005-08-11 | Numerous minor technical and editorial changes throughout. |
|  | Removed the appendix titled _x86 Equivalent Instructions for AltiVec Instructions.”_ |
| 2005-07-07 | Made numerous minor technical refinements and fixed a few typographical errors. |
| 2005-06-17 | Fixed typographical and linking errors. Made several improvements to technical content. |
| 2005-06-07 | New document that describes the architectural differences between PowerPC and Intel and provides tips for writing code that can run on both. |

[Previous](64-Bit%20Application%20Binary%20Interface.md)

