---
title: Java for OS X v10.5 Update 1 Release Notes
apple_id: TP40007619
resource_type: Release Note
platform: Java
topic: Cross Platform
technology: null
published: '2008-05-02'
source_url: https://developer.apple.com/library/archive/releasenotes/Java/JavaLeopardUpdate1RN/Introduction/Introduction.html
archived_at: '2026-07-18T02:58:40.517343Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)


[Next](https://developer.apple.com/library/archive/releasenotes/Java/JavaLeopardUpdate1RN/ResolvedIssues/ResolvedIssues.html)

# Introduction to Java on OS X v10.5 Update 1 Release Notes

These release notes explain Java on OS X v10.5 Update 1 and some known and resolved issues that may affect developers creating Java applications for OS X v10.5 Update 1.

Java for OS X v10.5 Update 1 provides Java SE 6 version 1.6.0_05 to all 64-bit capable Intel Macs. This release is only for OS X v10.5.2 and later, and should not be installed on earlier versions of OS X. This release provides several additional features including support for AppleScript as a javax.script language, new API for altering the application Dock icon, and native support for document modal sheets.

Any developer who wants to develop Java applications on OS X v10.5 should read this document as various issues and fixes found in this release may affect your application. Java developers should also read this document for the most current information on Java SE 6 and 64-bit support in OS X v10.5.

In addition, this document contains new details regarding:

- AppleScript as a supported language to the javax.script API.
- New API in com.apple.eawt.Application:

  - Get and set the Application Dock icon
  - Set a badge label on the Dock icon
  - Set the Dock menu
  - Open the native system help viewer if your application has a help bundle
- New API in com.apple.eio.FileManager:

  - getPathToApplicationBundle() obtains the path to the currently running Java application package
- Document Modal Sheets can be created by setting the the "apple.awt.documentModalSheet" client property to Boolean.TRUE on the JRootPane of JDialogs.
- GraphicsConfiguration.getNormalizingTransform() now returns a transform value that represents the physical size of the attached monitor.
- The system focus ring color can now be obtained using: UIManager.getColor("Focus.color");
- Aqua-style title-less group borders can now be obtained using: UIManager.getBorder("InsetBorder.aquaVariant");
- Java DTrace probes are supported.
- Java SE 6 can be used as a supported Java VM for Applets in 64-bit capable browsers. Java SE 5 will continue to be used in 32-bit-only capable browsers, such as Safari.

This document contains the following chapter:

- [Known and Resolved Issues](https://developer.apple.com/library/archive/releasenotes/Java/JavaLeopardUpdate1RN/ResolvedIssues/ResolvedIssues.html#//apple_ref/doc/uid/TP40007619-CH3-SW1) highlights a selection of high-visibility bugs that have been addressed in this release. This chapter is broken down by the category where the bug occurs and provides a brief description of what the issue was and how it was resolved.

This document also contains a revision history.

[Next](https://developer.apple.com/library/archive/releasenotes/Java/JavaLeopardUpdate1RN/ResolvedIssues/ResolvedIssues.html)

