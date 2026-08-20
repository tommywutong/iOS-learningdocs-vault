---
title: Xcode 4 Transition Guide
apple_id: TP40009984
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2011-08-10'
source_url: https://developer.apple.com/library/archive/documentation/IDEs/Conceptual/Xcode4TransitionGuide/NewProject/NewProject.html
archived_at: '2026-07-15T07:41:49.774932Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 4 Transition Guide](About%20the%20Transition%20to%20Xcode%204.md)


[Next](Orientation%20to%20Xcode%204.md)[Previous](Using%20an%20Existing%20Xcode%203%20Project.md)

# Creating a New Xcode 4 Project

If you want to start a new software development undertaking using Xcode 4, you need to first decide whether you need a single [Xcode project](https://developer.apple.com/library/archive/featuredarticles/XcodeConcepts/Concept-Projects.html#//apple_ref/doc/uid/TP40009328-CH5) or multiple related projects. For a simple application or utility, a single project should suffice. However, if you have several related executables that need to link against a custom library, you probably want at least a separate project for the library and another for the executables, and possibly a separate project for each executable. In that case, see [Create a New Workspace](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsobufvbuqnbnknltg).

If you decide that you don’t need a workspace, open Xcode 4 and click “Create a new Xcode project” in the startup screen. If Xcode 4 is already open, choose File > New > New Project. In the dialog that appears, be careful to select the type of project you want to create for the correct platform.

If you decide later that you want to create a workspace and add your project to it after all, see the instructions in [Using an Existing Xcode 3 Project](Using%20an%20Existing%20Xcode%203%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsobufvbuqmrnknltemi).

If you decide you want to work with two or more related projects, create an [Xcode workspace](https://developer.apple.com/library/archive/featuredarticles/XcodeConcepts/Concept-Workspace.html#//apple_ref/doc/uid/TP40009328-CH7). To do so, use the following procedure:

1. When Xcode 4 opens, ignore the startup screen and choose File > New > New Workspace.
2. In the New Workspace dialog, specify the location for the workspace file and the name of the workspace. If your projects are in the same directory, it might be convenient to create a new folder and put the workspace file in there as well. To avoid possible confusion with your projects, give the workspace a unique name. Click Save.
3. Choose File > New > New Project and follow the directions for each project you want to add. Be careful to select the correct platform and project type for your purposes.

[Next](Orientation%20to%20Xcode%204.md)[Previous](Using%20an%20Existing%20Xcode%203%20Project.md)

