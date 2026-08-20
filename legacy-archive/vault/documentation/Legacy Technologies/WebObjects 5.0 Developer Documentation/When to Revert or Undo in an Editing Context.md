---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Topics/ProgrammingTopics.37.html
archived_at: '2026-07-15T08:14:53.602467Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.36.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.38.md)

#   When to Revert or Undo in an Editing Context

##  Synopsis

Describes when and how to revert or undo changes made to the Enterprise Objects (EOs) using an EOEditingContext.

##  Description

EOF provides an object-based undo to allow the greatest flexibility for your user interface. You can redo, undo, or completely revert all changes you have made to your objects.

With EOF 3.0, the undo manager becomes a new class, NSUndoManager, defined in the Foundation framework. NSUndoManager is a general-purpose recorder for undo and redo operations. NSUndoManager automatically groups all operations within a single cycle of the run loop, so that performing an undo will revert all changes that occurred during the loop. Each editing context in an application has its own private NSUndoManager.

Every time an object is about to change, it invokes the
willChange
message to notify its observers. The editing context receiving these notifications will record the undo operations accordingly.

The EOEditingContext class provides the following methods to perform undo operations.

####  Objective-C Code

```objc

-(void)undo:(id)sender;
-(void)redo:(id)sender;
-(void)revert;
```

####  Objective-C Code

```objc

-(void) revert:(id) sender; // as a target action  method for Interface Builder
```

####  Java Code

```

public native void undo ();
public native void redo ();
public native void revert ();
```


When you send the undo or redo messages to an editing context, they are forwarded to its undo manager. The
undo
method closes the last open undo group and then applies all of the undo operations in that group (recording any undo operations as redo operations instead). The
redo
method likewise applies all of the redo operations on the top redo group.

Note that
undo
is intended for undoing top-level groups, and should not be used for nested undo groups. If any unclosed nested undo groups are on the stack when
undo
is invoked, an exception will be raised. To undo nested groups, you must explicitly close the group with an
endUndoGrouping
message to the undo manager, then use
undoNestedGroup
to undo it.

While
undo
only performs undoing of top-level groups,
revert
is a more extensive
undo
. The
revert
method removes everything from the undo stack. It throws out all insertions and deletions and restores the updated objects to their last committed values.

Note that
revert
does not cause a refetch from the database. It also does not replay the entire undo stack. If you add your own operations to the undo stack, they may not be properly reverted. The
revert
method also does not undo changes in display groups. Display groups that allow insertion and deletion of objects must be refetched whenever their editing context is reverted so that the user-interface display can be properly synchronized.

Usually, you do not need to write any code, and can simply connect your user-interface widgets to the appropriate undo, redo, or revert operations using Interface Builder.

!Note The EOJavaClient framework released in EOF 3.0 does not support undo.!

###  Caveats

NSUndoManager does not retain the targets of undo operations. However, it does contain references to the targets of the undo operations since it needs them to send undo messages when undo is performed.

Therefore, to avoid objects being leaked as your application runs, you should remember to clean the undo stack periodically.

For example, you could clean the stack after a save operation with the following message, or wherever it is appropriate depending on your undo policy. Note that, from a database access perspective, it is not recommended to allow an undo past a prior save point.

```

[[editingContext undoManager] forgetAllObjectsWithTarget: editingContext];
```

##  See Also

- 

  [Invalidating Objects](Invalidating%20Objects.md#apple-gmztimrx)
- 

  NSUndoManager class specification in the _Foundation Framework Reference_

##  Questions

- 

  What are the differences between undo and revert?
- 

  How do I use undo, redo, and revert?

##  Keywords

- 

  Undo
- 

  Redo
- 

  Revert

##  Revision History

24 July, 1998. Mai Nguyen. First Draft.
19 November, 1998. Clif Liu. Second Draft.

```

```

---

© 1999 Apple Computer, Inc.

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.36.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.38.md)[an error occurred while processing this directive]

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
