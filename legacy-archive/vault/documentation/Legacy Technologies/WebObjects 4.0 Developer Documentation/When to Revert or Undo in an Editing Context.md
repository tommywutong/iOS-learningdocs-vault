---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/Revert.html
archived_at: '2026-07-15T08:01:29.954533Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# When to Revert or Undo in an Editing Context

##  Synopsis

Describes when and how to revert or undo changes made to the Enterprise Objects (EOs) using an Editing Context.

##  Description

EOF provides an object-based undo to allow the greatest flexibility for your user interface. You can redo, undo, or completely revert all changes you have made to your objects.

With EOF 3.0, the undo manager becomes a new class, NSUndoManager, defined in the Foundation framework. NSUndoManager is a general-purpose recorder for undo and redo operations. NSUndoManager automatically groups all operations within a single cycle of the run loop, so that performing an undo will revert all changes that occurred during the loop. Each editing context in an application has its own private NSUndoManager.

Every time an object is about to change, it sends the _willChange_
message to notify its observers. The editing context receiving these notifications will record the undo operations accordingly.

The EOEditingContext class provides the following methods to perform undo operations.

#####  Figure 1. Objective-C Code

```objc
-(void)undo:(id)sender;
```



```objc
-(void)redo:(id)sender;
```



```objc
-(void)revert;
```


or

#####  Figure 2. Objective-C Code

```objc
-(void) revert:(id) sender; // as a target action  method for Interface Builder
```


#####  Figure 3. Java Code

```
public native void undo ();
```



```
public native void redo ();
```



```
public native void revert ();
```


When you send the undo or redo messages to an editing context, they are forwarded to its undo manager. _undo_
closes the last open undo group and then applies all of the undo operations in that group (recording any undo operations as redo operations instead). _redo_
likewise applies all of the redo operations on the top redo group.

Note that _undo_
is intended for undoing top-level groups, and should not be used for nested undo groups. If any unclosed nested undo groups are on the stack when _undo_
is invoked, an exception will be raised. To undo nested groups, you must explicitly close the group with an _endUndoGrouping_
message to the undo manager, then use _undoNestedGroup_
to undo it.

While _undo_
only performs undoing of top-level groups, _revert_
is a more extensive _undo_
. _revert_
removes everything from the undo stack. It throws out all insertions and deletions and restores the updated objects to their last committed values.

Note that _revert_
does not cause a refetch from the database. It also does not replay the entire undo stack. If you add you own operations to the undo stack, they may not be properly reverted. _revert_
also does not undo changes in display groups. Display groups that allow insertion and deletion of objects must be refetched whenever their editing context is reverted so that the user-interface display can be properly synchronized.

Usually, you do not need to write any code, and can simply connect your user-interface widgets to the appropriate undo, redo, or revert operations using InterfaceBuilder.

!Note The EOJavaClient framework released in EOF 3.0 does not support undo.!

####  Gotchas

NSUndoManager does not retain the targets of undo operations. However, it does contain references to the targets of the undo operations, since it needs them to send undo messages when undo is performed.

Therefore, to avoid objects being leaked as your application runs, you should remember to clean the undo stack periodically.

For example, you could clean the stack after a save operation with the following message, or wherever it is appropriate depending on your undo policy. Note that, from a database access perspective, it is not recommended to allow an undo past a prior save point.

```
[[editingContext undoManager] forgetAllObjectsWithTarget: editingContext];
```


##  See Also

· Invalidating Enterprise Objects

· NSUndoManager

##  Questions

· What are the differences between undo and revert?

· How do I use undo, redo, and revert?

##  Keywords

· undo

· redo

· revert

· undoNestedGroup

· forgetAllObjectsWithTarget

##  Revision History

24 July, 1998. Mai Nguyen. First Draft.
19 November, 1998. Clif Liu. Second Draft.

```

```


Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
