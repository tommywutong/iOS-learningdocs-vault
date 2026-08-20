---
title: Xcode Source Management Guide
apple_id: TP40006828
resource_type: Guide
platform: iOS|Xcode Developer Tools
topic: Xcode
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeSourceManagement/20-Technology_Overview/overview.html
archived_at: '2026-07-15T07:28:32.105064Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Source Management Guide](Introduction.md)


[Next](Source%20Control.md)[Previous](Introduction.md)

# Source Management Overview

This chapter provides an introduction to Xcode source management, which includes _Xcode SCM_ and _Xcode snapshots_, a multifile undo/redo mechanism. It describes source control concepts you need to know in order to perform source control operations using Xcode. This chapter also compares SCM with snapshots.

_Source control_, which is also known as source control management (SCM) or version control, is a set of tools and procedures you use to safeguard and manage files and changes made to them over time. By freeing you from these repetitive and error-prone tasks, source control systems allow you to concentrate solely on writing and testing code.

A source control system has three major parts: a repository, a client and a server. The _repository_ is a directory tree or database that contains the files managed by a source control system. The files stored in the repository are called _managed files_. Repositories can reside anywhere but are usually placed in a computer overseen by a system administrator who grants access to the repository and safeguards its contents through regular backups.

The _client_ is the program you use to interact with the repository. The _server_ is the process that actually modifies the repository. When you issue a command to the client, the client talks to the server process to carry it out.

Everyone authorized to access the repository can copy files from the repository into a directory known as the _working copy_. This is where you make changes to the project. Team members normally don’t have access to each other’s working copies. This feature provides privacy and security because one person is unaware of what others are doing until they _commit_ (publish) their changes to the repository.

When you submit changes to a file in the repository, the source control system increments its _revision number_ (also known as version number). Under this scheme, the history of each file is recorded as a set of revisions, which you can retrieve and compare individually.

Source control provides several benefits:

- __Centralized location of files.__ When more than one person works on a project concurrently, source control ensures that the project’s latest manifestation of its source files are kept in a central location. As a result, the project’s products can be built at any time without having to get the latest files from multiple locations.
- __Complete history of every file.__ Because all the changes made to each managed file are maintained in the repository, you can review the evolution of each file or an entire project since its inception. This information can be valuable when investigating the causes of software bugs.
- __Change management infrastructure.__ Source control systems don’t allow you to submit changes to the repository without describing the purpose of the change, which forces you to document your work. This requirement saves time in the long run because it allows everybody to determine the reason for a particular change without having to consult with the person who made the change.

Snapshots provide you with the ability to undo (and redo) change sets across several files. A _snapshot_ is a view of the state of the files in a directory. You can compare snapshots to find out the differences between them, such as which files have changed and the changes made to them. You can also restore your working files to a snapshot, taking their project back to the state it was when the snapshot was taken. Snapshots is not a source control system and does not interface with one. Instead, it’s a facility you can use to safeguard your work. Under standard access policies, your snapshots are not visible to others.

Xcode provides a common interface for various source control systems, including the open-source products Subversion and CVS (Concurrent Versions System), and Perforce. Xcode makes it easy to perform most source control tasks as you work on a project. It also tells you whether the managed files in your copy of the project differ from their representation in the repository.

You should consider using source control when you’re working with other developers on one project. Even when you’re the only one working on a project, you may benefit from the structure that source control adds to the development process, such as revisions and change management. As an alternative to source control, Xcode Snapshots may be more appropriate if you are the sole developer of a project or if you need to complement your repository-backed projects with a local large-scale undo mechanism.

[Next](Source%20Control.md)[Previous](Introduction.md)

