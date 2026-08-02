---
title: Xcode Source Management Guide
apple_id: TP40006828
resource_type: Guide
platform: iOS|Xcode Developer Tools
topic: Xcode
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeSourceManagement/10-Introduction/introduction.html
archived_at: '2026-07-15T07:28:32.098782Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Source%20Management%20Overview.md)

# Introduction

A source control system (also known as a source control management system or an SCM system), provides a repository for source files and a high-level interface to the changes made to them over time. In general terms, a source control system stores every change made to a file since it became part of the system. Source control systems can be used by individuals, but they are generally used by teams of developers who work on the same projects. A source control system allows several developers to keep track of the changes the team has made to the files that it stores.

Source control systems provide a command-line interface through which you can perform all the source control operations they support. However, Xcode provides an easy-to-use interface for the most popular source control systems. Through Xcode, you can browse repositories, check out projects, and track changes made to source files.

This document provides an overview of source control and describes how to work on projects managed under source control through the Xcode user interface.

To get the most out of this document, you should be familiar with the Xcode user interface and the structure of Xcode projects.

Consult _[Xcode Workspace Guide](../Xcode%20Workspace%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dsmrq)_ first if you’re not familiar with the Xcode user interface.

This document contains the following chapters:

- [Source Management Overview](Source%20Management%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmobvfvbeeq2cijbuuqy) provides a gentle introduction to source management in Xcode, which includes source control and snapshots.
- [Source Control](Source%20Control.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmobwfvbecssdivdesrq) describes how to connect to source control repositories and work with managed files and projects.
- [Snapshots](Snapshots.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dqmryfvbuqmjqgayc2u2xge) shows how to use locally stored snapshots to manage changes to multiple files.
- [Using Source Control and Snapshots](Using%20Source%20Control%20and%20Snapshots.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dqmryfvbuqmjqgays2u2xge) provides tips and caveats about using source control and snapshots on a project concurrently.

To learn more about source control systems, consult these books:

- _Version Control with Subversion_ (O’Reilly, 2004)
- _Essential CVS, 2nd Edition_ (O’Reilly, 2006)
- _Subversion Version Control: Using The Subversion Version Control System in Development Projects_ (Prentice Hall, 2005)
[Next](Source%20Management%20Overview.md)

