---
title: Application Architecture Overview
apple_id: 10000005i
resource_type: Guide
platform: macOS
topic: General
technology: AppKit
published: '2011-06-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AppArchitecture/Concepts/Undo.html
archived_at: '2026-07-15T05:25:30.452799Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Application Architecture Overview](Introduction%20to%20Application%20Architecture.md)


[Next](Graceful%20Application%20Termination.md)[Previous](Scripting.md)

# Undo and Redo

The Cocoa frameworks provide support for implementing undo and redo. `NSUndoManager` objects are responsible for tracking of the actions necessary to undo changes that are made to a document. The basic premise of the undo architecture is that when you are about to do something you first tell the `NSUndoManager` object how to undo it. The main API is invocation based, so if you have a `setColor:` method, it sends a message similar to the following before it actually sets the new color:

```
[[undoManager prepareWithInvocationTarget:self] setColor:oldColor]
```

This message causes the creation of an `NSInvocation` instance; if the user chooses Undo, that invocation (of the method `setColor:` with the parameter being the old color) is invoked. Because undone changes are put on a redo stack, if the user chooses the Redo command, the changes are redone.

Because many discrete changes might be involved in a user-level action, all the undo registrations that happen during a single cycle of the event loop are usually grouped together and are undone all at once. `NSUndoManager` has methods that allow you to control the grouping behavior further if you need to.

If you use the document architecture, some aspects of undo handling happen automatically. By default, each `NSDocument` object has an `NSUndoManager` object. (If you don’t want your application supporting Undo, you can use the `NSDocument` method `setHasUndoManager:` to prevent the creation of the undo manager.) You can use the `setUndoManager:` method if you need to use a subclass or if you otherwise need to change the undo manager used by the document.

When an `NSDocument` object has an `NSUndoManager` object, the document automatically keeps its edited state up to date by watching for notifications from the undo manager that tell it when changes are done, undone, or redone. In this case, you should never have to invoke the `NSDocument` method `updateChangeCount:` directly, since it is invoked automatically at the appropriate times.

The important thing to remember about supporting undo in a document-based application is that all changes that affect the persistent state of the document must be undoable. With a multilevel undo architecture, this is very important. If it is possible to make some changes to the document that cannot be undone, then the chain of edits that the `NSUndoManager` keeps for the document can become inconsistent with the document state. For example, imagine that you have a drawing program that is able to undo a resize, but not a delete. If the user selects a graphic and resizes it, the `NSUndoManager` gets an invocation that can undo that resize operation. Now the user deletes that graphic (which is not recorded for undo). If users now try to undo nothing would happen (at the very least) since the graphic that was resized is no longer there and undoing the resize can’t have any visual effect. At worst, the application might crash trying to send a message to a freed object. So when you implement undo, remember that everything that causes a change to the document should be undoable.

The most important code supporting undo should be in your model layer. Each model object in your application should be able to register undo invocations for all primitive methods that change the object.

It is often useful to structure the APIs of your model object to consist of primitive methods and extended methods. Examples of this sort of separation can be found throughout the Foundation framework (including `NSString`, `NSArray`, and `NSDictionary`) as well as in the Sketch example project. If you have such a separation in your model objects, remember that only the primitives should register for undo since, by definition, the extended methods are implemented in terms of the primitives.

Some situations might require you to temporarily suspend undo registration for certain actions. For example, a Sketch application lets the user resize a graphic by grabbing a resize knob and dragging it. During this dragging, hundreds or thousands of changes may be made to the bounds rectangle of the selected graphic. Changing the bounds of a graphic is a primitive operation and would normally result in an undo registration. While the user is actively resizing, though, it would be better if those thousands of undo registrations did not happen. In these cases, your model object might provide API to temporarily suspend and resume some or all of its undo registration. It is up to you to decide how to handle this. Certainly, it would work if those thousands of undo registrations did happen, but it would be a tremendous waste of memory to have to remember all those intermediate rectangles when you will never have to restore one of those intermediate states.

Although the most important part of your undo support should be in the model, there are two situations where you need some undo-related code in either your controller or view objects. The first case is when you want the Undo and Redo menu items to have more specific titles. You can use the `NSUndoManager` method `setActionName:` to give a name to the current undo group. The last invocation of `setActionName:` during an event cycle is the effective one. These names should reflect the intent of the user action, not the primitive operation that the action results in. Therefore, it is in your action methods that you should set action names.

It is not absolutely necessary to name an undo group. The menu items just say “Undo” and “Redo” without being specific about what is to be undone or redone. But when you do register a name it can help the user to know what will be undone or redone. It isn’t too hard to sprinkle a few calls to `setActionName:` in your view or controller action messages, so it is recommended that you try to give meaningful action names.

The second case where you might have some undo code in the controller or view layers is when there are some things that change that do not affect the actual state of the document but that still need to be undoable. Undoing selection changes is often such a case. For example, the Sketch application might not consider the selection to be a part of the document. In fact, if the document can have multiple views open on it, you might be able to have different selections in each one. However, you might want changes in the selection to be able to be undone for the user’s convenience and for visual continuity when the user is actually undoing things. In this case, the view that displays the graphics might keep track of the selection. It should register undo invocations as the selection changes.

Controller and view objects can come and go during the lifetime of a document object, and this is a consideration when controller-layer or view-layer events must be undoable. Your model objects typically live for the lifetime of the document and the document also owns the undo manager, so you don’t generally need to worry about what happens when the model goes away. But you may have to worry about what happens when the controller and view objects go away. If your controller or view object registers any undo invocations, you should make sure that they are cleared from the undo manager when the controller or view is deallocated. You can use the `NSUndoManager` method `removeAllActionsWithTarget:` for this purpose. Once a particular view on your document is closed, there is no point in keeping undo information about things such as selection changes for that view.

It is usually desirable to make scripted changes undoable. This is one more reason to put your primary undo support in your model objects. Since scripting is usually directed at the model, if your undo support is in your model primitives, then scripted changes can be undone. Being able to undo scripted changes is actually most important with macro-like scripts, where the script is used to automate relatively small tasks that are interspersed with direct user manipulation. In these cases especially, you want the scripted changes recorded along with the direct user changes, and for the same reason—it is important to have all changes to a document recorded. If an application doesn’t do this, a document can easily become inconsistent with the undo stack.

[Next](Graceful%20Application%20Termination.md)[Previous](Scripting.md)

