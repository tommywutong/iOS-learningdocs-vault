---
title: Xcode Overview
apple_id: TP40010215
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/WorkingonRelatedProjects.html
archived_at: '2026-07-27T06:57:07.920326Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Overview](index.md)


[Next](AlternativeToolchains.md)[Previous](WorkingwithTargets.md)

## Working on Related Projects

A workspace is a collection of projects that helps you reduce the complexity of larger applics. Workspaces have several benefits:

- Any project in the workspace has access to all the content from any other project in that same workspace, including compiled content.
- You can set up dependencies between projects so that a single build command builds all required pieces for the chosen target.
- You can include frameworks, modules, or static libraries, either your own or those of a third party.
- You can break up large projects into smaller pieces, allowing easier maintenance and sharing of functionality.

Create a workspace by choosing File > New > Workspace. After you create a workspace, you can create new projects within it and add existing projects to it. After you create the workspace, open the workspace file instead of the project file.

Convert an existing project into a workspace by choosing File > Save As Workspace. The existing window for the project is converted to a workspace window for the new workspace.

The screenshot shows an example of a workspace with two Xcode project files. The top project in the navigator area is a framework called `MySharedFramework`. The other project file is an app, `UsesSharedFramework`, that includes the shared framework. Using a workspace gives the app project access to everything in the shared framework project and makes tasks like debugging much easier. Adding the framework to the list of linked frameworks for the app creates a dependency between the app and the framework. Xcode checks whether the framework needs to be built before the app.

（原归档配图未能恢复：`XC_O_workspace_2x.png`）

For more information on workspaces, see [Xcode Workspace](https://developer.apple.com/library/archive/featuredarticles/XcodeConcepts/Concept-Workspace.html#//apple_ref/doc/uid/TP40009328-CH7), Creating a Workspace, and Adding an Existing Project to a Workspace.

[Working with Targets](WorkingwithTargets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmzsfvjvomi)

[Using Alternative Toolchains](AlternativeToolchains.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnzwfvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-10-27](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmrsfvjvomi)

[Next](AlternativeToolchains.md)[Previous](WorkingwithTargets.md)
