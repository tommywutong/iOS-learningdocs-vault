---
title: Software Delivery Legacy Guide
apple_id: TP40004615
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2010-09-15'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/SoftwareDistribution4/Resource_Forks/Resource_Forks.html
archived_at: '2026-07-15T07:26:59.907150Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Software Delivery Legacy Guide](Introduction.md)


[Next](Glossary.md)[Previous](Prebinding%20Applications.md)

# Preserving Resource Fork Data

In Carbon and pre–Mac OS X applications, application resources were stored in the resource fork of an application executable. In Mac OS X applications resources should be put in the data fork of a separate resource file, not the resource fork of the executable. The primary reason for moving application resources out of resource forks is to enable applications to be seamlessly moved around other file systems without loss of their resources; this would include transfer mechanisms such as BSD commands, FTP, email, and Windows and DOS copy commands. Most other computing environments, including the web, recognize single-fork files only and tend to delete the resource fork of HFS and HFS+ files.

When you package software with PackageMaker, you supply a location from which to gather the files to be packaged. If any of these files (such as a Classic application) has a resource fork, PackageMaker supports splitting the file before packaging. Such split files will be reassembled by the Installer application when the package is installed. Although splitting files with resource forks is optional, if you do not split them, the resource fork data will be lost and the file will be unusable.

Because resource fork splitting changes the files that are split, it is recommended that you operate on copies of these files while creating packages.

[Next](Glossary.md)[Previous](Prebinding%20Applications.md)

