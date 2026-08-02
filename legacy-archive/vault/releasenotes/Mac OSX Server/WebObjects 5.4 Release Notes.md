---
title: WebObjects 5.4 Release Notes
apple_id: TP40006091
resource_type: Release Note
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSXServer/WO54_ReleaseNotes/Introduction/Introduction.html
archived_at: '2026-07-18T02:58:56.128378Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)


[Next](https://developer.apple.com/library/archive/releasenotes/MacOSXServer/WO54_ReleaseNotes/ResolvedIssues/ResolvedIssues.html)

# Introduction to WebObjects 5.4 Release Notes

WebObjects 5.4 for Mac OS X v10.5 is an application server with tools, technologies, and capabilities to create Internet and intranet applications. It has an object-oriented architecture that promotes quick development of reusable web components. WebObjects is extremely scalable and supports high transaction volumes. These release notes describe the improvements and changes made to both the developer and deployment versions of WebObjects 5.4.

With this release of WebObjects are the following improvements, changes, additions, and deprecated tools and technologies.

WebObjects Runtime Improvements

- Combined Component Template Parser that reduces .wo components to single .html files
- Generation of XHTML compliant pages
- AJAX request handler for enhanced page caching
- Added support for secure URL generation
- JMX monitoring support
- Entity index management in the model
- Improved the synchronization with the database
- Added support for index generation
- Support for enum in attribute conversion
- Improved support for vendor specific prototypes (EOJDBCOraclePrototype, EOJDBCFrontBasePrototype, etc.)
- Derby support (Embedded database)
- Support for Generics
- WebServices update (Axis 1.4)
- Full support for Apple XML plist (Read and Write)
- Ant build support

Open Specifications

- EOModels
- WO Components (classic and single file)

Sample code

- JavaMonitor
- EOF utilities

WebObjects Deployment

- WebObjects Apache 2.2 module 32/64 bit
- Apache 1.3 deployment compatibility
- Leopard migration assistant from Apache 1.3 to Apache 2.2

JDK support

- JDK 1.5 minimum requirement

Build System

- Jam build systems still in place for legacy Xcode projects
- Ant build system support

Deprecations

- Jam based project creation templates
- Java Client Nib based applications
- Direct to JavaClient based applications
- EOCocoaClient based applications
- OpenBase no longer example database
- Tools (EOModeler, WebObjects Builder, Rule editor)

Any developer who wants to develop and deploy WebObjects applications should read this document as various issues and fixes found in this release may affect your application. Anyone interested in new WebObjects development should also read this document for the most current information on new features and outstanding issues with WebObjects 5.4.

This document contains the following chapter:

- [Known and Resolved Issues](https://developer.apple.com/library/archive/releasenotes/MacOSXServer/WO54_ReleaseNotes/ResolvedIssues/ResolvedIssues.html#//apple_ref/doc/uid/TP40006091-CH3-SW1) highlights a selection of high-visibility bugs that have been addressed in this release. This chapter is broken down by the category where the bug occurs and provides a brief description of what the issue was and how it was resolved.

This document also contains a revision history.

The Following WebObjects documents may be helpful:

- _[WebObjects Overview](../../documentation/Web%20Objects/WebObjects%20Overview/Introduction%20to%20WebObjects%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamby)_
- _[WebObjects Deployment Guide Using JavaMonitor](../../documentation/Web%20Objects/WebObjects%20Deployment%20Guide%20Using%20JavaMonitor/Introduction%20to%20WebObjects%20Deployment%20Guide%20Using%20JavaMonitor.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambz)_
- _WebObjects 5.4 Reference_
- _WebObjects File Format Reference_
- _[WebObjects Application Properties Reference](../../documentation/Web%20Objects/WebObjects%20Application%20Properties%20Reference/Introduction%20to%20WebObjects%20Application%20Properties%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamrq)_
[Next](https://developer.apple.com/library/archive/releasenotes/MacOSXServer/WO54_ReleaseNotes/ResolvedIssues/ResolvedIssues.html)

