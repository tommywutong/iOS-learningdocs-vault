---
title: Java for OS X v10.5 Update 2 Release Notes
apple_id: TP40007988
resource_type: Release Note
platform: Java
topic: Cross Platform
technology: null
published: '2008-09-24'
source_url: https://developer.apple.com/library/archive/releasenotes/Java/JavaLeopardUpdate2RN/Introduction/Introduction.html
archived_at: '2026-07-18T02:58:40.548974Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)


[Next](https://developer.apple.com/library/archive/releasenotes/Java/JavaLeopardUpdate2RN/ResolvedIssues/ResolvedIssues.html)

# Introduction to Java on OS X v10.5 Update 2 Release Notes

These release notes provide information concerning known and resolved issues that may affect developers creating Java applications for OS X with Java for OS X v10.5 Update 2.

Java for OS X v10.5 Update 2 supports all Intel-based and PowerPC-based Macs for J2SE 5.0 and J2SE 1.4.2. Java SE 6 support is available on 64-bit, Intel-based Macs only. This release is only for OS X v10.5.4 and later, and should not be installed on earlier versions of OS X. It updates J2SE 1.4.2 to 1.4.2_18, J2SE 5.0 to version 1.5.0_16, and Java SE 6 to version 1.6.0_07.

Any developer who wants to develop Java applications on OS X v10.5 should read this document as various issues and fixes found in this release may affect your application.

In addition, this document contains details regarding the following updates to J2SE 5.0:

- New API in com.apple.eawt.Application:

- Get and set the Application Dock icon
- Set a badge label on the Dock icon
- Set the Dock menu
- Open the native system help viewer if your application has a help bundle

- New API in com.apple.eio.FileManager:

- getPathToApplicationBundle() obtains the path to the currently running Java application package

- New UI-specific functionality:

- The system focus ring color can now be obtained using: UIManager.getColor(“Focus.color”);
- Aqua-style title-less group borders can now be obtained using: UIManager.getBorder(“InsetBorder.aquaVariant”);
- The apple.awt.UIElement system property can be set to allow Java applications to launch without a Dock icon

This document contains the following chapter:

- [Known and Resolved Issues](https://developer.apple.com/library/archive/releasenotes/Java/JavaLeopardUpdate2RN/ResolvedIssues/ResolvedIssues.html#//apple_ref/doc/uid/TP40007988-CH3-SW1) highlights a selection of high-visibility bugs that have been addressed in this release. This chapter is broken down by the category where the bug occurs and provides a brief description of what the issue was and how it was resolved.

This document also contains a revision history.

[Next](https://developer.apple.com/library/archive/releasenotes/Java/JavaLeopardUpdate2RN/ResolvedIssues/ResolvedIssues.html)

