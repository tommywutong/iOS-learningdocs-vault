---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/SCMOverview/SCMOverview.html
archived_at: '2026-07-15T07:28:50.806863Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Managing%20Projects.md)[Previous](Version%20Control.md)

# Overview of Version Control

_Version control_ (also known
as Source Control Management or SCM) is a set of tools and procedures
to safeguard and manage files and changes made to them over time.
A version control system frees you from having to manually manage
access to the files that comprise a software project and track changes.
Version control systems take care of these details, allowing you
to concentrate on writing and testing code.

You should read this chapter if you’re new to version control
and are interested in adopting version control practices in your
projects. After reading this overview, you’ll understand how version
control provides an infrastructure that improves the development
experience for single developers and multiple developers working
in the same project.

This chapter describes the essential aspects of version control
systems. If you’re familiar with version control, you can skip
this chapter.

Have you ever wondered which files you modified to correct
a problem in one of your projects? Or, how about undoing changes
you made the previous day because you came up with a better solution
to the problem? A version control system can give you answer to the
first question quickly; you don’t need to check modification dates
or comments inside source files. It would also let you discard multifile
changes so you can reimplement the solution to a problem without
manually identifying and removing each change in every file you
touched.

A version control system has three major parts: a repository,
a client, and a server. The _repository_ is a directory
tree or database that contains the files managed by a version control
system. The files stored in the repository are called _managed
files_. Repositories can reside anywhere but are usually
placed in a computer managed by a system administrator who sets
access to the repository and ensures the persistence of its contents
through regular backups.

The _client_ is the program developers use
to interact with a repository. The _server_ is
the process that actually modifies the repository. When a developer
issues a command to the client, the client talks to the server process
to carry it out.

Every developer authorized to access the repository can copy
files from the repository into a local directory, also known as
a _working copy_. This is where developers make
changes to the project; they never work with the files in the repository.
Developers normally don’t have access to each other’s working
copies. This feature provides privacy and security because developers
are unaware of what their peers are doing until they publish or _submit_ their
changes to the repository.

When a developer submits changes to a file in the repository,
its _version number_ (also known as the _revision
number_) is incremented. The history of each file is recorded
as a set of revisions, which you can retrieve and compare individually.

Version control provides several benefits, including:

- Centralized
  location of files

  When multiple developers work on a project
  concurrently, version control ensures that the project’s official
  files are kept in a central location. As a result, the project’s
  products can be built at any time without having to get the latest
  files from multiple locations.
- Complete history of every file

  Because all the changes
  made to each file in the repository are maintained in the repository,
  you can review the evolution of each file or an entire project since
  its inception. This information can be valuable when investigating
  the causes of software bugs.
- Change management infrastructure

  Version control systems
  don’t allow developers to submit changes to the repository without
  describing the purpose of the change, which forces developers to
  document their work. This requirement saves time in the long run
  because it allows everybody to determine the reason for a particular
  change without having to find the person who performed the change.
  Version control also lets developers group changes in the way that
  best fits the them and their team. For example, developers can submit
  changes on a daily basis, whether the items they’re working on
  are finished. This feature reduces the amount of data loss that
  can occur in case a developer’s computer fails unexpectedly; however,
  it also reduces the stability of the project. Submitting changes to
  the repository only after a feature is completely implemented and
  tested is a better approach, especially for sensitive features that
  should be kept secret for some time.

Consider using version control when several developers work
on one project at the same time. Single developers can also benefit
from the structure that version control adds to the development
process, such as revisions and change management.

Xcode provides a common interface to various version control
systems, which include the open-source CVS (Concurrent Versions
System) and Subversion, and Perforce. Xcode makes it easy to perform
most version control tasks as you develop. It also tells you whether
you’ve modified managed files in your local copy of the project. [Managing Projects](Managing%20Projects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwhewueqkkincumskg) and [Managing Files](Managing%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrxgawueqkkivbeeq2i) describe
Xcode’s version control interface in detail.

[Next](Managing%20Projects.md)[Previous](Version%20Control.md)

