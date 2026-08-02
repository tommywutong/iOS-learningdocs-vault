---
title: How to add a folder to the contents of a package
apple_id: DTS10004143
resource_type: QA
platform: Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2006-10-31'
source_url: https://developer.apple.com/library/archive/qa/qa1484/_index.html
archived_at: '2026-07-18T02:31:23.152363Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1484

# How to add a folder to the contents of a package

## Q:  How do I place a folder of resource files into the package contents of my executable code, rather than individual references to each file in the folder?

A: How do I place a folder of resource files into the package contents of my executable code, rather than individual references to each file in the folder?

To add a folder of resources to your project, you drag the folder into the `Resources` folder under `Groups & Files`. After the folder is added to the project an alert sheet drops into the window. The sheet has two radio buttons that control the placement and representation of the folder in your package's contents:

`Recursively create groups for any added folders`, and

`Create Folder References for any added folders`

Xcode defaults to the first choice, which creates a file reference for each file in the folder at the root of your package's content directory. You want to select the `Create Folder References for any added folders` button, as shown in figure 1. This selection creates a single reference to the folder that mirrors the layout of the folder from the filesystem - it creates a single folder within the package contents of your executable code. For a more in-depth exploration of this topic, please see the [Xcode User Guide documentation for adding files to your project](https://developer.apple.com/documentation/DeveloperTools/Conceptual/XcodeUserGuide/Contents/Resources/en.lproj/01_04_pr_add_files/chapter_7_section_5.html#//apple_ref/doc/uid/TP40002666-CJBDCEJE).

__Figure 1__  Adding a folder that will remain intact to the resources of a project.

!!

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-10-31 | New document that describes how to add a folder of files to the package contents of executable code |

