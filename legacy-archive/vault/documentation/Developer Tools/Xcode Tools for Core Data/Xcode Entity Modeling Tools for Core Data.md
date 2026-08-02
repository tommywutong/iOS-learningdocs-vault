---
title: Xcode Tools for Core Data
apple_id: TP40006846
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: CoreData
published: '2010-09-02'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeCoreDataTools/Introduction/Introduction.html
archived_at: '2026-07-15T07:27:49.591484Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Creating%20a%20Data%20Model%20File.md)

# Xcode Entity Modeling Tools for Core Data

The Xcode data modeling tool deals with entities and the relationships between them. You use the tool to define a schema for Core Data. The model ultimately becomes part of your build product and is used by your application at runtime.

The purpose of the Core Data data modeling tool is to create a data model (or schema) for use with the Core Data framework. At runtime, the model is turned into an instance of [NSManagedObjectModel](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel) with a collection of [NSEntityDescription](https://developer.apple.com/documentation/coredata/nsentitydescription), [NSAttributeDescription](https://developer.apple.com/documentation/coredata/nsattributedescription), [NSRelationshipDescription](https://developer.apple.com/documentation/coredata/nsrelationshipdescription), and [NSFetchRequest](https://developer.apple.com/documentation/coredata/nsfetchrequest) objects. In some respects this is analogous to the behavior of Interface Builder. With Interface Builder, you graphically create a collection of objects that are then saved in a file (a nib file) and re-created at runtime. As with user interface elements, you can create a model directly in code at runtime; however, it is typically easier to do so graphically using the appropriate tool. Similarly, just as it is possible to modify the user interface after it has been loaded, it is also possible to customize a model after it has been loaded. (A model does have one constraint not shared with a nib file: a model cannot be modified after you have integrated it into the Core Data stack.)

As your application evolves, to accommodate new features you may need to change the schema. Core Data provides an infrastructure for migrating data from one schema (model version) to another—see _[Core Data Model Versioning and Data Migration Programming Guide](../../Cocoa/Core%20Data%20Model%20Versioning%20and%20Data%20Migration%20Programming%20Guide/Core%20Data%20Model%20Versioning%20and%20Data%20Migration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojz)_. To use this infrastructure, you need to define a versioned model, and mappings between model versions. You create a versioned model using Xcode’s data modeling tool (see [Model Versioning](Model%20Versioning.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dqnbzfvjvomi)) and, if necessary, a mapping model using _[Xcode Mapping Tool for Core Data](../Xcode%20Mapping%20Tool%20for%20Core%20Data/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dqnrr)_.

You should read this document to learn how to use the Xcode entity modeling tool to create a managed object model for a Core Data application. For a task-based example of how to create a data model, see _Creating a Managed Object Model with Xcode_.

This document contains the following sections:

- [Creating a Data Model File](Creating%20a%20Data%20Model%20File.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dqnjvfvjvomi) describes how to create a model file.
- [Workflow](Workflow.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dsmjwfvjvomi) describes the basic features of the data modeling tools and how you use them.
- [The Browser View](The%20Browser%20View.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dqnjxfvjvomi) describes the diagram view of the data modeler.
- [The Diagram View](The%20Diagram%20View.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dqnjwfvjvomi) describes the diagram view of the data modeler.
- [The Predicate Builder](The%20Predicate%20Builder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dqnjtfvjvomi) describes the predicate builder.
- [Code Generation](Code%20Generation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dqnzsfvjvomi) describes how to generate source code for model entities and their properties.
- [Model Versioning](Model%20Versioning.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dqnbzfvjvomi) describes how to create a versioned model and how to specify the current version in a versioned model.
- [Compiling a Data Model](Compiling%20a%20Data%20Model.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dqnzrfvjvomi) describes how to compile a data model and what compiler flags are available.
- [Creating a User Interface From a Data Model](Creating%20a%20User%20Interface%20From%20a%20Data%20Model.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dqnjufvjvomi) describes how to use the data modeler in conjunction with Interface Builder to create a user interface.

[Next](Creating%20a%20Data%20Model%20File.md)

