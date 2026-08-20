---
title: Document-Based App Programming Guide for iOS
apple_id: TP40011149
resource_type: Guide
platform: tvOS|iOS
topic: Data Management
technology: UIKit
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/DocumentBasedAppPGiOS/CreateCustomDocument/CreateCustomDocument.html
archived_at: '2026-07-15T07:23:56.533134Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Document-Based App Programming Guide for iOS](About%20Document-Based%20Applications%20in%20iOS.md)


[Next](Managing%20the%20Life%20Cycle%20of%20a%20Document.md)[Previous](Document-Based%20Application%20Preflight.md)

# Creating a Custom Document Object

A document-based application must have an instance of a subclass of [UIDocument](https://developer.apple.com/documentation/uikit/uidocument) that represents and manages document data. This chapter discusses the [method overrides](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MethodOverriding.html#//apple_ref/doc/uid/TP40008195-CH57) most applications need to make and offers suggestions for overriding other methods. For the core override points—the [loadFromContents:ofType:error:](https://developer.apple.com/documentation/uikit/uidocument/1619971-loadfromcontents) and [contentsForType:error:](https://developer.apple.com/documentation/uikit/uidocument/1619978-contentsfortype) methods—examples are given for both [NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData) and [NSFileWrapper](https://developer.apple.com/documentation/foundation/filewrapper) as types of document data read from and written to a file. [Storing Document Data in a File Package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqobnknlte) further explains how to use file-wrapper objects for document data.

You can override methods of `UIDocument` other than the ones discussed in this chapter to read and write document data for particular purposes—for example, to write and read document data incrementally. However, these more advanced overrides have more complex requirements and should be avoided if possible. See _[UIDocument Class Reference](https://developer.apple.com/documentation/uikit/uidocument)_ for discussions of these overrides.

In Xcode, add new Objective-C source and header files to your project, naming them appropriately (suggestion: work “Document” into the name). In the header file, change the superclass to `UIDocument` and add [properties](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13) to hold the document data. In Listing 3-1, the document data is plain text, so an [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString) property is all that is needed to hold it. (The text will be converted to an `NSData` object that is written to the document file.)

__Listing 3-1__  Document subclass declarations (`NSData`)

```objc
@interface MyDocument : UIDocument {
}
@property(nonatomic, strong) NSString *documentText;
@end
```

Listing 3-2 illustrates set of declarations for another application that uses an `NSFileWrapper` object as the data-representation type. (The code examples in the chapter alternate between the two applications.) Not only is there a property to hold the file-wrapper object, there are properties to hold the text and image components of the represented file package.

__Listing 3-2__  Document subclass declarations (`NSFileWrapper`)

```objc
@interface ImageNotesDocument : UIDocument

@property (nonatomic, strong) NSString* text;
@property (nonatomic, strong) UIImage* image;
@property (nonatomic, strong) NSFileWrapper *fileWrapper;

@property (nonatomic, weak) id <ImageNotesDocumentDelegate> delegate;
@end

@protocol ImageNotesDocumentDelegate <NSObject>
-(void)noteDocumentContentsUpdated:(ImageNotesDocument*)noteDocument;
@end
```

This code shows additional declarations for a [delegate](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) and the [protocol](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45) that it adopts. The document object’s view [controller](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11) makes itself the delegate of the document object (and adopts the protocol) so that it can be notified (via `noteDocumentContentsUpdated:` messages) of modifications to the document file. [Listing 3-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqobnknltm) shows when and how the `noteDocumentContentsUpdated:` message is sent.

When an application opens a document (at the user’s request), [UIDocument](https://developer.apple.com/documentation/uikit/uidocument) reads the contents of the document file and calls the [loadFromContents:ofType:error:](https://developer.apple.com/documentation/uikit/uidocument/1619971-loadfromcontents) method, passing in an object encapsulating the document data. That object can be an [NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData) object or an [NSFileWrapper](https://developer.apple.com/documentation/foundation/filewrapper) object. In your override of the method, initialize the document’s internal data structures (that is, its model objects) from the contents of the passed-in object.

The example in Listing 3-3 creates a string from the passed-in `NSData` object and assigns it to the `documentText` property. It also informs its delegate (in this case, the document’s view controller) of the updated document contents by invoking a protocol method. The motivation behind this delegation message is that the `loadFromContents:ofType:error:` method is called not only as the result of opening a document, but also because of iCloud updates and reversion operations ([revertToContentsOfURL:completionHandler:](https://developer.apple.com/documentation/uikit/uidocument/1619974-reverttocontentsofurl)).

__Listing 3-3__  Loading a document’s data (`NSData`)

```objc
- (BOOL)loadFromContents:(id)contents ofType:(NSString *)typeName error:(NSError **)outError {
    if ([contents length] > 0) {
        self.documentText = [[NSString alloc] initWithData:(NSData *)contents encoding:NSUTF8StringEncoding];
    } else {
        self.documentText = @"";
    }
    if ([_delegate respondsToSelector:@selector(noteDocumentContentsUpdated:)]) {
        [_delegate noteDocumentContentsUpdated:self];
    }
    return YES;
}
```

If you have more than one document type, check the `typeName` parameter; a different document type might affect how your code handles the document-data object. If your code experiences an error that prevents it from loading document data, return `NO`; optionally, you can return by reference an [NSError](https://developer.apple.com/documentation/foundation/nserror) object that describes the error.

The example in Listing 3-4 handles document data in the form of an `NSFileWrapper` object. It simply assigns this object to its property.

__Listing 3-4__  Loading a document’s data (`NSFileWrapper`)

```objc
-(BOOL)loadFromContents:(id)contents ofType:(NSString *)typeName error:(NSError **)outError {
    self.fileWrapper = (NSFileWrapper *)contents;
    if ([_delegate respondsToSelector:@selector(noteDocumentContentsUpdated:)]) {
        [_delegate noteDocumentContentsUpdated:self];
    }
    return YES;
}
```

In this code, the method implementation does not extract the text and image components of the file wrapper and assign them to their properties. That is done lazily in the getter methods for the `text` and `image` properties.

When a document is closed or when it is automatically saved, `UIDocument` sends the document object a [contentsForType:error:](https://developer.apple.com/documentation/uikit/uidocument/1619978-contentsfortype) message. You must override this method to return a snapshot of the document’s data to `UIDocument`, which then writes it to the document file. Listing 3-5 gives an example of returning a snapshot of document data in the form of an `NSData` object.

__Listing 3-5__  Returning a snapshot of document data (`NSData`)

```objc
- (id)contentsForType:(NSString *)typeName error:(NSError **)outError {
    if (!self.documentText) {
        self.documentText = @"";
    }
    NSData *docData = [self.documentText dataUsingEncoding:NSUTF8StringEncoding allowLossyConversion:NO];
    return docData;
}
```

If the `documentText` property has not yet been assigned any string value yet, it is assigned an empty string before it’s used to create an `NSData` object.

Listing 3-6 shows an implementation of the same method that returns an `NSFileWrapper` object. Basically, if a top-level (directory) file-wrapper object doesn’t exist, the code creates it; and if the two contained (regular file) file-wrapper objects do not exist, the code creates them from the values of the `text` and `image` properties. Then, it returns the top-level file wrapper to `UIDocument`, which creates a file package in the file system. See [Storing Document Data in a File Package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqobnknlte) for a more detailed explanation of file packages and documents.

__Listing 3-6__  Returning a snapshot of document data (`NSFileWrapper`)

```objc
-(id)contentsForType:(NSString *)typeName error:(NSError **)outError {

    if (self.fileWrapper == nil) {
        self.fileWrapper = [[NSFileWrapper alloc] initDirectoryWithFileWrappers:nil];
    }
    NSDictionary *fileWrappers = [self.fileWrapper fileWrappers];
    if (([fileWrappers objectForKey:TextFileName] == nil) && (self.text != nil)) {
        NSData *textData = [self.text dataUsingEncoding:TextFileEncoding];
        NSFileWrapper *textFileWrapper = [[NSFileWrapper alloc] initRegularFileWithContents:textData];
        [textFileWrapper setPreferredFilename:TextFileName];
        [self.fileWrapper addFileWrapper:textFileWrapper];
    }
    if (([fileWrappers objectForKey:ImageFileName] == nil) && (self.image != nil)) {
        @autoreleasepool {
            NSData *imageData = UIImagePNGRepresentation(self.image);
            NSFileWrapper *imageFileWrapper = [[NSFileWrapper alloc] initRegularFileWithContents:imageData];
            [imageFileWrapper setPreferredFilename:ImageFileName];
            [self.fileWrapper addFileWrapper:imageFileWrapper];
        }
    }
    return  self.fileWrapper;
}
```


A file package has an internal structure that is reflected in the methods of the [NSFileWrapper](https://developer.apple.com/documentation/foundation/filewrapper) class. A file wrapper is a runtime representation of a file-system node, which is either a directory, a regular file, or a symbolic link. As shown in Figure 3-1, a file package is a file-system node, typically a directory and its contents, that the operating system treats as a single, opaque entity. It is similar in concept to a bundle.

__Figure 3-1__  Structure of a file package

!

You programmatically compose a file package by creating a top-level directory file wrapper and then adding to that container regular files and subdirectories, each represented by other `NSFileWrapper` objects. File wrappers inside the top-level directory should have preferred names associated with them.

With this brief overview in mind, look again at the following lines of code from the [contentsForType:error:](https://developer.apple.com/documentation/uikit/uidocument/1619978-contentsfortype) method in [Listing 3-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqobnknltq). The file package created in this method has two components, a text file and an image file. (The creation of the image file wrapper is not shown in the snippet.)

```
    if (self.fileWrapper == nil) {
        self.fileWrapper = [[NSFileWrapper alloc] initDirectoryWithFileWrappers:nil];
    }
    NSDictionary *fileWrappers = [self.fileWrapper fileWrappers];
    if (([fileWrappers objectForKey:TextFileName] == nil) && (self.text != nil)) {
        NSData *textData = [self.text dataUsingEncoding:TextFileEncoding];
        NSFileWrapper *textFileWrapper = [[NSFileWrapper alloc] initRegularFileWithContents:textData];
        [textFileWrapper setPreferredFilename:TextFileName];
        [self.fileWrapper addFileWrapper:textFileWrapper];
    }
```

The code creates a top-level directory if it doesn’t exist. If a file wrapper doesn’t exist for the text file, it creates one from the string contents of the text property. It gives this file wrapper a preferred filename and then adds it to the top-level directory file wrapper.

For more on `NSFileWrapper`, see _[NSFileWrapper Class Reference](https://developer.apple.com/documentation/foundation/nsfilewrapper)_; also see [Exporting the Document UTI](Document-Based%20Application%20Preflight.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqmznknltg) for the required `Info.plist` property for document file packages.

There are a few other `UIDocument` overrides that many document-based applications might want to make:

- [disableEditing](https://developer.apple.com/documentation/uikit/uidocument/1619958-disableediting)...[enableEditing](https://developer.apple.com/documentation/uikit/uidocument/1619987-enableediting)—`UIDocument` calls the first method when it is unsafe for the user to make changes to document content, such as when there are updates from iCloud or a revert operation is underway. You can implement this method to prevent editing during this period. When editing becomes safe again, `UIDocument` calls the second method.
- [savingFileType](https://developer.apple.com/documentation/uikit/uidocument/1619991-savingfiletype)—This method by default returns the value of the [fileType](https://developer.apple.com/documentation/uikit/uidocument/1619992-filetype) property. If the current document should be saved under a different file type for any reason, you can override this method to return the replacement file-type UTI. An example (from Mac OS X) is that when an image is added to an RTF file, it should be saved as an RTFD file package.

[Next](Managing%20the%20Life%20Cycle%20of%20a%20Document.md)[Previous](Document-Based%20Application%20Preflight.md)

