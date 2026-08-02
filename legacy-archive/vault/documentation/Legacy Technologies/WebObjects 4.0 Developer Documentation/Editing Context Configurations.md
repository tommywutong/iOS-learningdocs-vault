---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/Guide/AppConfs3.html
archived_at: '2026-07-18T01:19:16.469990Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Developer's Guide](Enterprise%20Objects%20Framework%20Developer%27s%20Guide.md)

[!Table of Contents](Application%20Configurations.md) [!Previous Section](Non-Graphical%20User%20Interface%20Applications.md)

# Editing Context Configurations

Recall that by default, each nib has its own EOEditingContext and that nibs share an EOObjectStoreCoordinator (see["Sharing Editing Contexts and Coordinators"](Graphical%20User%20Interface%20Applications.md#apple-gm4demy)). In this default configuration, each _peer_ editing context has its own object graph. So for example, a single database row can be represented by separate enterprise object instances in different editing contexts. Changes to an object in one editing context don't affect the corresponding object in another editing context until all changes are successfully saved through their shared EOObjectStoreCoordinator. At that time the objects in all editing contexts are synchronized with the committed changes.

This arrangement is useful when an application allows the user to edit multiple independent _documents_. For example, imagine an Application Kit application that creates and modifies video rental records. Each rental is represented by a window that is loaded from the same nib.
You can implement variations on the default configuration to:

- Use one EOEditingContext for multiple nibs.

In this scenario, multiple nibs have the same object graph and therefore see each other's changes to objects immediately.

- Use nested EOEditingContexts.

This configuration is useful in a "drill down" user interface where, for example, changes in a nested dialog box can be okayed or canceled.

## Using One Editing Context for Multiple Nibs

Ordinarily, changes to objects in one EOEditingContext aren't immediately reflected in the objects of another editing context. [Figure 40](#apple-gm4tima) shows how this plays out in an application.

!

Figure 40. Different Nibs Use Different EOEditingContexts

In an application where changes in Window 1 should be immediately reflected in Window 2, both nibs should use the same editing context.
To use one editing context for multiple nibs, use the EOEditingContext static method __setSubstitutionEditingContext__ (the __setSubstitutionEditingContext:__ class method in Objective-C). You use this method to substitute the specified editing context for the one associated with a nib file you're about to load. This method causes all of the connections in your nib file to be redirected to the specified editing context.
For example, if Nib 1 in the figure above is loaded before Nib 2, you could invoke the following code before loading Nib 2 to set its EOEditingContext to the same one in Nib 1.
In Java:

```
EODisplayGroup displayGroup;
    // Assume that displayGroup is the display group
    // from Nib 1 and that Nib 1 has already been loaded.
EOEditingContext editingContext;

editingContext =
displayGroup.dataSource().editingContext();
EOEditingContext.setSubstitutionEditingContext(editingCo
ntext);
NSApplication.loadNibNamed("Nib2", this);

// Restore the default behavior
EOEditingContext.setSubstitutionEditingContext(null);
```


In Objective-C:

```
EODisplayGroup *displayGroup;
    // Assume that displayGroup is the display group
    // from Nib 1 and that Nib 1 has already been loaded.
EOEditingContext *editingContext;

editingContext = [[displayGroup dataSource]
editingContext];
[EOEditingContext
setSubstitutionEditingContext:editingContext];
[NSApplication loadNibNamed:@"Nib2" owner:self];

// Restore the default behavior
[EOEditingContext setSubstitutionEditingContext:nil];
```


After loading a nib with a substitution editing context, you should restore the default behavior by setting the substitution editing context to __null__ (__nil__ in Objective-C). Then when nibs are loaded in the future, their editing contexts are simply unarchived and aren't replaced.

## Using Nested Editing Contexts

EOEditingContexts can be nested, allowing a user to make edits to an object graph in one editing context and then discard or commit those changes to another object graph (which, in turn, may commit them to an external store). For example, [Figure 41](#apple-gm4tomy) shows a drill-down user interface that can be implemented with nested editing contexts. Before users save rental information, they can supply optional comments about the rental. Canceling the Comments panel reverts the rental to its pre-comments state. Okaying the Comments panel incorporates the comments into the rental.

!

Figure 41. A Drill-Down User Interface

To implement the drill-down behavior of this interface, the editing context for the Comments window sits on top of the Rental window's editing context as shown in [Figure 42](#apple-gm4tqnq). In this configuration, the Rental window's editing context is the parent object store of the Comment's editing context.

!

Figure 42. Nested Editing Context Configuration

To set up a nested editing context configuration, use the EOEditingContext static method __setDefaultParentObjectStore__ (__setDefaultParentObjectStore:__ in Objective-C). For example, [Figure 43](#apple-gm4tsny) shows the nibs for the Rental and Comments windows.

!

Figure 43. Nibs for the Rental and Comments Windows

Before loading Nib 2, the Rental application should invoke the following code to assign the Rental editing context as the parent object store of the Comments editing context.
In Java:

```
EODisplayGroup rentalsDisplayGroup;
    // Assume that rentalsDisplayGroup is the display group
    // from Nib 1 and that Nib 1 has already been loaded.
EOEditingContext editingContext;

editingContext =
displayGroup.dataSource().editingContext();
EOEditingContext.setDefaultParentObjectStore(editingCont
ext);
NSApplication.loadNibNamed("Nib2", this);

// Restore the default behavior
EOEditingContext.setDefaultParentObjectStore(null);
```


In Objective-C:

```
EODisplayGroup *rentalsDisplayGroup;
    // Assume that rentalsDisplayGroup is the display group
    // from Nib 1 and that Nib 1 has already been loaded.
EOEditingContext *editingContext;

editingContext = [[displayGroup dataSource]
editingContext];
[EOEditingContext
setDefaultParentObjectStore:editingContext];
[NSApplication loadNibNamed:@"Nib2" owner:self];

// Restore the default behavior
[EOEditingContext setDefaultParentObjectStore:nil];
```


After loading a nib with an editing context substituted as the default parent object store, you should restore the default behavior by setting the default parent EOObjectStore to __null__ (__nil__ in Objective-C). Then when nibs are loaded in the future, their editing contexts are simply connected to the default EOObjectStoreCoordinator.

[!Table of Contents](Application%20Configurations.md) [!Next Section](Object%20Store%20Coordinator%20Configurations.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
