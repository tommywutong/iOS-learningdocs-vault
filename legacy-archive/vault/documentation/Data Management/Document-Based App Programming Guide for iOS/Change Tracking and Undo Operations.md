---
title: Document-Based App Programming Guide for iOS
apple_id: TP40011149
resource_type: Guide
platform: tvOS|iOS
topic: Data Management
technology: UIKit
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/DocumentBasedAppPGiOS/ChangeTrackingUndo/ChangeTrackingUndo.html
archived_at: '2026-07-15T07:23:56.524864Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Document-Based App Programming Guide for iOS](About%20Document-Based%20Applications%20in%20iOS.md)


[Next](Resolving%20Document%20Version%20Conflicts.md)[Previous](Managing%20the%20Life%20Cycle%20of%20a%20Document.md)

# Change Tracking and Undo Operations

The saveless-model feature of the [UIDocument](https://developer.apple.com/documentation/uikit/uidocument) class ensures that document data is automatically saved at frequent intervals, relieving users of the need to explicitly save their documents. `UIDocument` implements much of the behavior for the saveless model, but a document-based application must play its own part to make the feature work.

The saveless model implemented by the UIKit framework for documents has two main parts: a mechanism for marking a document as needing to be saved and a variable period for when the framework checks that flag. Periodically, UIKit calls the [hasUnsavedChanges](https://developer.apple.com/documentation/uikit/uidocument/1619965-hasunsavedchanges) method of a `UIDocument` object and evaluates the returned value. If the value is `YES`, it saves the document data to the document file. The period between checks of the `hasUnsavedChanges` value varies according to several factors, including the rate of input by the user.

A document-based application sets the value returned by `hasUnsavedChanges` indirectly, either by implementing undo and redo or by tracking changes to the document. Change tracking requires the application to call the [updateChangeCount:](https://developer.apple.com/documentation/uikit/uidocument/1619961-updatechangecount) method, passing in [UIDocumentChangeDone](https://developer.apple.com/documentation/uikit/uidocument/changekind/done) (a constant of type `UIDocumentChangeKind`). When an application registers an undo action and then sends [undo](https://developer.apple.com/documentation/foundation/nsundomanager/1412189-undo) or [redo](https://developer.apple.com/documentation/foundation/nsundomanager/1417030-redo) messages to the document’s undo manager, `UIDocument` calls [updateChangeCount:](https://developer.apple.com/documentation/uikit/uidocument/1619961-updatechangecount) on its behalf.

Because giving users the ability to undo and redo changes can be a differentiating feature, that approach is recommended for most applications.

You can implement undo and redo operations in your application by following the procedures and recommendations in _[Undo Architecture](../../Cocoa/Undo%20Architecture/Introduction%20to%20Undo%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgayta2i)_. Note that `UIDocument` defines an [undoManager](https://developer.apple.com/documentation/uikit/uidocument/1619953-undomanager) property. You can get the default [NSUndoManager](https://developer.apple.com/documentation/foundation/undomanager) object by accessing this property, or you can assign your own `NSUndoManager` object to it. The undo manager must be associated with the `UIDocument` object through the property in order to enable change tracking and thus automatic saving of document data.

Listing 5-1 illustrates an implementation of undo and redo for a text field.

__Listing 5-1__  Implementing undo and redo for a text field

```objc
- (void)textFieldDidEndEditing:(UITextField *)textField {
    self.undoButton.enabled = YES;
    self.redoButton.enabled = YES;

    if (textField.tag == 1) {
        [self setLocationText:textField.text];
    }
    // code for other text fields here....
}

- (void)setLocationText:(NSString *)newText {
    NSString *currentText = _document.location;
    if (newText != currentText) {
        [_document.undoManager registerUndoWithTarget:self
            selector:@selector(setLocationText:)
            object:currentText];
        _document.location = newText;
        self.locationField.text = newText;
    }
}

- (IBAction)handleUndo:(id)sender {
    [_document.undoManager undo];
    if (![_document.undoManager canUndo]) self.undoButton.enabled = NO;
}

- (IBAction)handleRedo:(id)sender {
    [_document.undoManager redo];
    if (![_document.undoManager canRedo]) self.redoButton.enabled = NO;
}
```


To implement change tracking instead of implementing undo/redo, call the [updateChangeCount:](https://developer.apple.com/documentation/uikit/uidocument/1619961-updatechangecount) method on the `UIDocument` object at the appropriate points in your code. Just as when you register an undo action, it’s typically at the point where you update the document’s model object with data the user has just entered. The parameter passed in should be a [UIDocumentChangeDone](https://developer.apple.com/documentation/uikit/uidocument/changekind/done) constant.

Listing 5-2 shows how you might call [updateChangeCount:](https://developer.apple.com/documentation/uikit/uidocument/1619961-updatechangecount) from within a [UITextViewDelegate](https://developer.apple.com/documentation/uikit/uitextviewdelegate) method that is called when a change is made in a text view.

__Listing 5-2__  Updating the change count of a document

```objc
-(void)textViewDidChange:(UITextView *)textView {
    _document.documentText = textView.text;
    [_document updateChangeCount:UIDocumentChangeDone];
}
```

[Next](Resolving%20Document%20Version%20Conflicts.md)[Previous](Managing%20the%20Life%20Cycle%20of%20a%20Document.md)

