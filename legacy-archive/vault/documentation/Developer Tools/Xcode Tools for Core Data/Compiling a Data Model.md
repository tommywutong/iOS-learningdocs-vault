---
title: Xcode Tools for Core Data
apple_id: TP40006846
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: CoreData
published: '2010-09-02'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeCoreDataTools/Articles/xcdCompilerFlags.html
archived_at: '2026-07-15T07:27:39.404210Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Tools for Core Data](Xcode%20Entity%20Modeling%20Tools%20for%20Core%20Data.md)


[Next](Creating%20a%20User%20Interface%20From%20a%20Data%20Model.md)[Previous](Model%20Versioning.md)

# Compiling a Data Model

A data model is a deployment resource. A data model must not only be a project file, it must be associated with the target that uses it. In addition to details of the entities and properties in the model, the model contains information about the diagram—its layout, colors of elements, and so on. This latter information is not needed at runtime. The model file is compiled to remove the extraneous information and make runtime loading of the resource as efficient as possible.

The model compiler, `momc`, is located in `Library/Xcode/Plug-ins/XDCoreDataModel.xdplugin/Contents/Resources/` in the Developer directory. If you want to use it in your own build scripts, its usage is `momc source destination`, where _source_ is the path of the Core Data model to compile and _destination_ is the path of the output mom file.

The compiler can generate warnings for various model configuration problems (such as unidirectional relationships). You can toggle these warnings by checking the appropriate boxes in the Warnings section of the project Build panel, as shown in Figure 1.

__Figure 1__  Project build panel showing `momc` warning flags

!
[Next](Creating%20a%20User%20Interface%20From%20a%20Data%20Model.md)[Previous](Model%20Versioning.md)

