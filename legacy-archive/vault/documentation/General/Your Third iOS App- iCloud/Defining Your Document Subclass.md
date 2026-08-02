---
title: 'Your Third iOS App: iCloud'
apple_id: TP40011317
resource_type: Guide
platform: iOS
topic: General
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/iCloud101/DefiningYourDocumentSubclass/DefiningYourDocumentSubclass.html
archived_at: '2026-07-15T07:34:29.696873Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Your Third iOS App: iCloud](About%20Your%20Third%20iOS%20App.md)


[Next](Implementing%20the%20Master%20View%20Controller.md)[Previous](Getting%20Started.md)

# Defining Your Document Subclass

The best way to manage a file in iCloud is to use a custom document object based on the [UIDocument](https://developer.apple.com/documentation/uikit/uidocument) class. This class provides the basic behavior required for managing files both locally and in iCloud. To use the class, you must subclass it and override the methods responsible for reading and writing your app data.

In the [Model-View-Controller](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MVC.html#//apple_ref/doc/uid/TP40008195-CH32) architecture, document objects are model controllers—that is, their job is to act as a controller object for portions of your app’s data model. A document object typically facilitates interactions between your app’s data structures and the view controllers that present the associated data.

The Simple Text Editor app uses a custom [UIDocument](https://developer.apple.com/documentation/uikit/uidocument) subclass to manage the contents of individual text files. Because this class does not exist in the template project, you must create it explicitly.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To create your document subclass

1. In Xcode, select File > New > New File.
2. In the iOS section, select the Cocoa Touch group.
3. Select Objective-C class for the file type and click Next.
4. Specify the following information for your subclass:

   - Class: `STESimpleTextDocument`
   - Subclass of: `UIDocument` (You might have to type the class name in the provided field.)
5. Click Next.

   Xcode prompts you to save the source files.
6. Navigate to your project directory and make sure the SimpleTextEditor target is selected in the list of targets.
7. Click Create.

The data managed by the `STESimpleTextDocument` class consists of an [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString) object, which stores the text associated with the document. You declare this string using a [property](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13).

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To add the property declaration for the string data

1. In the project navigator, select `STESimpleTextDocument.h`.
2. Add a declared property called `documentText` for storing the document contents.

   The property declaration looks like this:

```objc
@property (copy, nonatomic) NSString* documentText;
```

To complete the implementation of the `documentText` property, you also need to tell the compiler to synthesize the [accessor](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/AccessorMethod.html#//apple_ref/doc/uid/TP40008195-CH2) methods. You provide code to do this in your document’s implementation file.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To synthesize the accessor methods for the document text property

1. In the project navigator, select `STESimpleTextDocument.m`.
2. After the `@implementation STESimpleTextDocument` line, add the following line of code:

```objc
@synthesize documentText = _documentText;
```

   Only the synthesized getter method is actually created. The app provides a custom setter method to perform some extra tasks when a new string is assigned to the document.

The `STESimpleTextDocument` class uses a custom setter method for its `documentText` property. The custom setter method adds undo support when setting the document text. Not only does this give the app support for undoing changes on the document’s text, it also provides some benefits related to iCloud. Specifically, it triggers the document’s autosave mechanism, which causes those changes to be sent to iCloud.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To implement the setDocumentText: method

1. In the project navigator, select `STESimpleTextDocument.m`.
2. Add the following code to the class implementation:

```objc
- (void)setDocumentText:(NSString *)newText {
   NSString* oldText = _documentText;
   _documentText = [newText copy];

   // Register the undo operation.
   [self.undoManager setActionName:@"Text Change"];
   [self.undoManager registerUndoWithTarget:self
          selector:@selector(setDocumentText:)
          object:oldText];
}
```

In the `setDocumentText:` method, you must save the string containing the old text and pass it to the undo manager as part of the operation. The undo manager maintains the reference to the old string until it is no longer needed.

A document object writes a document’s contents to disk and reads those contents back in. Nearly all of the work needed to initiate read and write operations is handled automatically by the [UIDocument](https://developer.apple.com/documentation/uikit/uidocument) class. But because the actual reading and writing of data is specific to your document class, you must write some custom code.

In the Simple Text Editor app, the document object’s data is an `NSString` object, but `UIDocument` does not allow you to write strings directly to disk. So instead, you must package the string in a form that the document object can handle, namely an [NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData) object. You do this in the [contentsForType:error:](https://developer.apple.com/documentation/uikit/uidocument/1619978-contentsfortype) method of your document subclass.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To implement the contentsForType:error: method

1. In the project navigator, select `STESimpleTextDocument.m`.
2. Implement the `contentsForType:error:` method.

   This method is a declared method of the `UIDocument` class. Overriding it is your way to provide your app’s data to the document object. Your implementation of the `contentsForType:error:` method must make sure there is a valid string to write to disk, package that string in an `NSData` object, and return it.

```objc
- (id)contentsForType:(NSString *)typeName error:(NSError **)outError {
    if (!self.documentText)
        self.documentText = @"";

    NSData *docData = [self.documentText
                           dataUsingEncoding:NSUTF8StringEncoding];
    return docData;
}
```

Using the built-in document infrastructure allows you to focus on your data instead of worrying about how to write that data to disk. When you return your data object, the document object creates a file coordinator object and uses it to write the data to disk. The use of a file coordinator ensures that your app has exclusive access to the file and is required when saving files to an iCloud container directory. If you did not use the `UIDocument` class, you would be responsible for creating the file coordinator object yourself.

The process for reading your document data is similar to the process for writing it. All you have to do is retrieve your document data from the data object passed to the [loadFromContents:ofType:error:](https://developer.apple.com/documentation/uikit/uidocument/1619971-loadfromcontents) method. As with writing, you do not have to create a file coordinator or do anything other than read your data from the provided object.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To implement the loadFromContents:ofType:error: method

1. In the project navigator, select `STESimpleTextDocument.m`.
2. Implement the `loadFromContents:ofType:error:` method.

   The implementation of the `loadFromContents:ofType:error:` method checks to see whether the data object contains valid information and, if so, uses it to create a new string object. If it does not contain any bytes, it initializes the document contents to an empty string.

```objc
- (BOOL)loadFromContents:(id)contents
             ofType:(NSString *)typeName
             error:(NSError **)outError {
    if ([contents length] > 0)
        self.documentText = [[NSString alloc]
                    initWithData:contents
                    encoding:NSUTF8StringEncoding];
    else
        self.documentText = @"";

    return YES;
}
```


When the contents of the document change, the document object must communicate those changes to other interested objects. One way to do so is using a [delegate](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) object.

The first step in supporting a delegate object is to define a protocol with the methods that object must implement. For the `STESimpleTextDocument` class, you need to let the delegate know when the document initiates changes to its content. In this app, the delegate is always a view controller, so the delegate method gives that view controller a chance to update its views.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To declare the document’s delegate protocol

1. In the project navigator, select `STESimpleTextDocument.h`.
2. Declare a new protocol and call it `STESimpleTextDocumentDelegate`.

   Place the protocol declaration after the declaration of the `STESimpleTextDocument` class.
3. Add a `documentContentsDidChange:` method to your protocol.

   This method takes your document object as a parameter and has no return value. Your protocol definition should now look similar to the following:

```objc
@protocol STESimpleTextDocumentDelegate <NSObject>
@optional
- (void)documentContentsDidChange:(STESimpleTextDocument*)document;
@end
```

For the `STESimpleTextDocument` class, a document changes its own content only when it loads content from disk. Thus, the only method that must be modified to call the delegate method is the `loadFromContents:ofType:error:` method. All other document-related changes come from outside of the document and do not result in calling the delegate method.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To add delegate support to the document class

1. In the project navigator, select `STESimpleTextDocument.h`.
2. Add a forward declaration of the `STESimpleTextDocumentDelegate` protocol to the header file.

   Place the forward declaration before the declaration of the `STESimpleTextDocument` class. You need the forward declaration to prevent compiler errors.

```objc
@protocol STESimpleTextDocumentDelegate;
```
3. Add a `delegate` property to the `STESimpleTextDocument` class.

   Your delegate object should be a weak reference to an object of type `id` that conforms to the `STESimpleTextDocumentDelegate` protocol. Thus, your property declaration should look similar to the following:

```objc
@property (weak, nonatomic) id<STESimpleTextDocumentDelegate> delegate;
```
4. In the project navigator, select `STESimpleTextDocument.m`.
5. Synthesize the delegate property.

```objc
@synthesize delegate = _delegate;
```
6. At the end of your [loadFromContents:ofType:error:](https://developer.apple.com/documentation/uikit/uidocument/1619971-loadfromcontents) method, add code to call the `documentContentsDidChange:` delegate method.

   When calling a delegate method, always check for the existence of the delegate object and make sure that the object responds to the given selector. The implementation of your `loadFromContents:ofType:error:` method should now look similar to the following:

```objc
- (BOOL)loadFromContents:(id)contents
               ofType:(NSString *)typeName
               error:(NSError *__autoreleasing *)outError {
    if ([contents length] > 0)
        self.documentText = [[NSString alloc] initWithData:contents
                                              encoding:NSUTF8StringEncoding];
    else
        self.documentText = @"";

    // Tell the delegate that the document contents changed.
    if (self.delegate && [self.delegate respondsToSelector:
                          @selector(documentContentsDidChange:)])
        [self.delegate documentContentsDidChange:self];

    return YES;
}
```

After entering the code for your document object, build your project to make sure everything compiles. At this point, you see only the default master-detail interface, because the document object has not yet been used.

In this chapter, you learned how to define a document class and use it to read and write the contents of a file. You also learned how an undo manager object can trigger autosave operations and how to use a delegate to report changes. Finally, you learned how to use a delegate protocol to communicate changes to other interested objects. In the next chapter, you will start building the interface of your app so that you can display the documents you create.

[Next](Implementing%20the%20Master%20View%20Controller.md)[Previous](Getting%20Started.md)

