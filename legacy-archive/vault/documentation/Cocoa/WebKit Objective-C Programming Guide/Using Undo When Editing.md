---
title: WebKit Objective-C Programming Guide
apple_id: 10000164i
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2012-11-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/Tasks/UsingUndo.html
archived_at: '2026-07-15T07:14:55.751052Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebKit Objective-C Programming Guide](Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md)


[Next](Using%20the%20Document%20Object%20Model%20from%20Objective-C.md)[Previous](Changing%20Editing%20Behavior.md)

# Using Undo When Editing

You can undo high-level web content editing operations—edits made programmatically and by the user—without writing any additional code. However, if you programmatically modify the Document Object Model (DOM), you need to write additional code to make those operations undoable.

For example, you can undo high-level operations programmatically as follows:

```
    // Delete content
    [webView deleteSelection];

    // Restore it
    [[webView undoManager] undo];
```

However, it’s not as simple to undo a DOM operation. It’s not good enough to return the DOM to an equivalent state—it must be exactly as it was originally. For example, you can’t just undo deleted text by creating a new node and inserting it in the old location. The links between the nodes need to be exactly as they were before deleting the text.

One approach is to store the deleted objects so that you still have a copy. For example, you might store a deleted DOM node before removing it from the tree as follows:

```
 DOMNode *containerNode = [self containerNode];

    // Must keep a copy before removing from the document
    deletedNode = [containerNode lastChild];

    // Now remove
    [containerNode removeChild:deletedNode];

    // Make undoable
    [[webView undoManager] registerUndoWithTarget:self selector:@selector(undoAction) object:self];
```

You can then implement `undoAction` to return the DOM to its original state:

```objc
- (void)undoAction
{
    DOMNode *containerNode = [self containerNode];

    // Put the node back
    [containerNode appendChild:deletedNode];

    // Make redoable
    [[webView undoManager] registerUndoWithTarget:self selector:@selector(redoAction) object:self];
}
```

The `redoAction` simply deletes the stored node again as follows:

```objc


- (void)redoAction
{
    DOMNode *containerNode = [self containerNode];

    // Take node out again
    [containerNode removeChild:deletedNode];

    // Make undoable
    [[webView undoManager] registerUndoWithTarget:self selector:@selector(undoAction) object:self];
}
```

[Next](Using%20the%20Document%20Object%20Model%20from%20Objective-C.md)[Previous](Changing%20Editing%20Behavior.md)

