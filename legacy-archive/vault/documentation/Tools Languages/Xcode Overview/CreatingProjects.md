---
title: Xcode Overview
apple_id: TP40010215
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/CreatingProjects.html
archived_at: '2026-07-27T06:57:07.902258Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Overview](index.md)


[Next](WorkingwithTargets.md)[Previous](UsingMultipleWorkspaces.md)

## Working with Projects

Apps you create in Xcode require a __project__, which keeps the necessary files and resources organized. You start a project by choosing File > New > New Project. Xcode opens a new workspace window and displays a dialog in which you choose a project template. Xcode provides built-in templates for developing common styles of iOS, watchOS, and OS X apps. These templates include essential project configuration and files that help you start your development effort quickly.

（原归档配图未能恢复：`ProjectTemplate_2x.png`）

View the names of project files in the project navigator. When you select a file in the project navigator, the file’s contents appear in the appropriate editor or viewer. The screenshot below shows the Adventure project. An implementation file (`APAViewController.m`) is selected in the project navigator, and the file’s contents appear in the source editor.

（原归档配图获取待重试：`Projects_2x.png`）

### A Project Is a Repository of Files and Resources for Building Apps

A project contains the elements needed to build one or more apps (or other software products, such as command-line tools and plug-ins). The project also maintains the relationships among these elements. These elements include:

- References to source code files (including implementation files and header files where appropriate), libraries and frameworks, image files, and user interface files
- Groups, for organizing files in the project navigator
- Project-level build configurations
- Targets, each of which produces a single app

By selecting the project name in the project navigator, you open the project editor. You can use the project editor to specify every aspect of how your apps should be built, from the version of the software development kit (SDK) to specific compiler options. In this screenshot, the Adventure project is selected in the project navigator _and_ in the project editor. The project editor displays the Info pane for the Adventure project.

（原归档配图获取待重试：`Targets_2x.png`）

When you create a project, Xcode provides two standard project-level build configurations: debug and release. These configurations differ mostly in whether they include debug information and in the degree to which each build is optimized. These two build configurations are probably sufficient for your product development needs. Most developers never need to change the values of the vast majority of build settings.

To add more build configurations, open the project editor, duplicate one of the project’s existing configurations, and then modify its settings. For example, you might configure a build that’s fully optimized but that also includes debug information in order to debug your optimized code.

（原归档配图未能恢复：`project_editor-build_configurations_2x.png`）

### Closing and Opening a Project or a Workspace

To close a project or workspace, choose File > Close Project or File > Close Workspace. Xcode remembers which windows you had open and how they were configured, and it restores them when you reopen the project or workspace.

[Using Multiple Workspace Windows](UsingMultipleWorkspaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmzqfvjvomi)

[Working with Targets](WorkingwithTargets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmzsfvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-10-27](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmrsfvjvomi)

[Next](WorkingwithTargets.md)[Previous](UsingMultipleWorkspaces.md)
