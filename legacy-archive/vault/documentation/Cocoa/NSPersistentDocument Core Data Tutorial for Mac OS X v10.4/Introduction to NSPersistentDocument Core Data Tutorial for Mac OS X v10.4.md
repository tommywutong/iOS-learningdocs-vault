---
title: NSPersistentDocument Core Data Tutorial for Mac OS X v10.4.
apple_id: TP40008168
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2009-02-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSPersistentDocumentTutorial104/00_Introduction/introduction.html
archived_at: '2026-07-15T07:16:47.641503Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Overview%20of%20the%20Tutorial.md)

This document will not be modified in the future.

# Introduction to NSPersistentDocument Core Data Tutorial for Mac OS X v10.4

The task goal of this tutorial is to create a document-based application that allows a user to display and modify information about a department, employees in the department, and managerial relationships between the employees.

This tutorial takes you through the steps of building a simple Core Data–based application using `NSPersistentDocument` and Cocoa bindings. `NSPersistentDocument` is a subclass of `NSDocument` that integrates with the Core Data framework. You will find this tutorial useful if you’re using the Core Data framework to create a document-based application.

You should read this document to gain an understanding of how to create a Core Data document-based application using `NSPersistentDocument` and Cocoa bindings. Among other concepts, you will learn how to create the project, how to customize the creation of a document, and how to localize error messages.

[Overview of the Tutorial](Overview%20of%20the%20Tutorial.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnryfvbuqmrygmwvgvzr) describes the application you will create, and the task constraints.

[Creating the Project, Model, and Interface](Creating%20the%20Project%2C%20Model%2C%20and%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnryfvbuqmrqgmwvgvzr) describes how you create a Core Data document-based project in Xcode, and how you create the data model and how you can use it to automatically create a default user interface.

[Creating a Custom Class](Creating%20a%20Custom%20Class.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnryfvbuqmrrhewvgvzr) describes how to implement a custom class for an entity.

[Adding a Department Object](Adding%20a%20Department%20Object.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnryfvbuqmrsgmwvgvzr) describes how you add a Department object to the document, and configure the user interface appropriately.

[Copy and Paste](Copy%20and%20Paste.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnryfvbuqmrugmwvgvzr) describes one way you can support copy and paste in a Core Data application.

[Localizing and Customizing Model Property Names and Error Messages](Localizing%20and%20Customizing%20Model%20Property%20Names%20and%20Error%20Messages.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnryfvbuqmrshawvgvzr) describes how you can localize property names and customize alert panels.

[Document Metadata](Document%20Metadata.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnryfvbuqmrtgywvgvzr) describes how you can add metadata to your document that Spotlight can extract—it also describes how you write the Spotlight importer.

[A Sheet for Creating a New Employee](A%20Sheet%20for%20Creating%20a%20New%20Employee.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnryfvbuqmrygqwvgvzs) describes how you can use a sheet for data entry.

_[Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)_ describes functionality provided by the Core Data framework from a high-level overview to in-depth descriptions.

_[Core Data Utility Tutorial](../Core%20Data%20Utility%20Tutorial/Introduction%20to%20Core%20Data%20Utility%20Tutorial.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbq)_ takes you through the steps of building a command-line utility that uses Core Data. _You are strongly encouraged to complete the low-level tutorial before following this tutorial._

[Next](Overview%20of%20the%20Tutorial.md)

