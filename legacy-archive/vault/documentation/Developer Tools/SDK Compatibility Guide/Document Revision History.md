---
title: SDK Compatibility Guide
apple_id: 10000163i
resource_type: Guide
platform: Xcode Developer Tools
topic: General
technology: null
published: '2010-11-15'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/cross_development/RevisionHistory.html
archived_at: '2026-07-15T07:30:33.220360Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [SDK Compatibility Guide](Introduction.md)


[Previous](Using%20SDK-Based%20Development.md)

# Document Revision History

This table describes the changes to _SDK Compatibility Guide_.

| __Date__ | __Notes__ |
| 2010-11-15 | Added an explanation of how to use the `NS_CLASS_AVAILABLE` macro in [Using Weakly Linked Classes in iOS](Using%20SDK-Based%20Development.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgaydalktk4zq). |
|  | Updated and improved the [Configuring a Project for SDK-Based Development](Configuring%20a%20Project%20for%20SDK-Based%20Development.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3dg2jninedclktk4za) and [Using SDK-Based Development](Using%20SDK-Based%20Development.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgaydalktk43a) chapters. |
|  | Improved the [Using Weakly Linked Methods, Functions, and Symbols](Using%20SDK-Based%20Development.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgaydaljrgeytinjtg4) section by adding information on checking the availability of external symbols. |
| 2010-02-16 | Corrected an example that shows how to use conditional compilation macros. |
| 2009-09-09 | Clarified build setting information. |
| 2009-05-12 | Changed the title from Cross-Development Programming Guide. Added information about iOS SDK-based development. Revised text significantly and removed obsolete information. |
| 2006-11-07 | Added details on cross-development and universal binaries. |
|  | Added chapter “Determining the Version of a Framework”. Noted requirement to build with GCC 3.3 when targeting OS X versions prior to OS X v10.3.0. Corrected OS X version requirements for code compiled with GCC 4.0. Added links to further information on building universal binaries from the command line. Changed deployment target in example. |
| 2006-05-23 | Corrected a build-setting specification and added per-architecture-build-setting availability details. |
|  | Corrected specification for `LDFLAGS` build setting in “Configuring a Makefile-Based Project”. Added availability details for the per-architecture build settings feature. |
| 2006-03-08 | Added a link to Technical Note TN2163, which describes how to develop a universal I/O Kit driver. |
| 2006-02-07 | Made minor corrections. |
|  | Added information on building universal binary versions of kernel extensions. |
|  | Clarified use of `LDFLAGS`. |
| 2005-11-09 | Added a section on using cross-development to create universal binaries. Added information on identifying deprecated API. Corrected errors. |
|  | Added “Cross-Development and Universal Binaries” chapter. Added [Finding Instances of Deprecated API Usage](Using%20SDK-Based%20Development.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgaydalktk42q). Reorganized content to create separate sections for configuring cross-development settings in Xcode and in makefile-based projects. Corrected sample code listing in [Conditionally Compiling for Different SDKs](Using%20SDK-Based%20Development.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgaydaljrgeytinzuge). |
| 2005-08-11 | Fixed a bug in code that checks for the existence of a symbol. Updated steps for setting a deployment target to reflect Xcode 2.1. |
| 2005-06-04 | Updated information about checking for undefined functions. Added information about how to support SDKs from command-line programs. |
| 2003-09-16 | Made a number of changes throughout this document to reflect the final status of cross-development support as it shipped in OS X version 10.3. |
| 2003-08-21 | First general release of document. |

[Previous](Using%20SDK-Based%20Development.md)

