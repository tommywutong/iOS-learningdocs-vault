---
title: Packaged Document for OS X
apple_id: DTS40012955
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/PackagedDocument/Listings/PackagedDocument_MyTextPictDocument_m.html
archived_at: '2026-07-18T03:18:44.946636Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Packaged Document for OS X](Packaged%20Document%20for%20OS%20X.md)


[Next](PackagedDocument-WindowController.m.md)[Previous](LICENSE.txt.md)

# PackagedDocument/MyTextPictDocument.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The NSDocument subclass for reading/writing it data and connecting with iCloud.
 */

#import "MyTextPictDocument.h"
#import "MyAppDelegate.h"
#import "WindowController.h"
#import "ViewController.h"

// File names for the package content.
NSString *ImageFileName = @"Image.png";
NSString *TextFileName = @"Text.txt";
NSString *MetaDataFileName = @"MetaData.plist";
    NSString *MetaDataDisclosedKey = @"disclosedKey";   // View disclosed state in MetaData.plist.
    NSString *MetaDataValue2Key = @"value2";            // Special string value in MetaData.plist.

// Encoding used to encode the notes text file.
NSStringEncoding kTextFileEncoding = NSUTF8StringEncoding;


@interface MyTextPictDocument () <ViewControllerDelegate>

// Text content for this document.
@property (copy) NSString *notes;

// Meta data for this document (disclosure state + special string value).
@property (strong) NSMutableDictionary *metaDataDict;

// Document's main file wrapper (to contain subcontent for image, text and metadata).
@property (strong) NSFileWrapper *documentFileWrapper;

@end


#pragma mark -

@implementation MyTextPictDocument

// -------------------------------------------------------------------------------
//  autosavesInPlace
// -------------------------------------------------------------------------------
+ (BOOL)autosavesInPlace
{
    // This gives us autosave and versioning for free in 10.7 and later.
    return YES;
}

// -------------------------------------------------------------------------------
//  canAsynchronouslyWriteToURL:url:typeName:saveOperation
//
//  Turn this on for async saving allowing saving to be asynchronous, making all our
//  save methods (dataOfType, saveToURL) to be called on a background thread.
// -------------------------------------------------------------------------------
- (BOOL)canAsynchronouslyWriteToURL:(NSURL *)url ofType:(NSString *)typeName forSaveOperation:(NSSaveOperationType)saveOperation
{
    return YES;
}

// -------------------------------------------------------------------------------
//  init
// -------------------------------------------------------------------------------
- (instancetype)init
{
    self = [super init];
    if (self != nil)
    {
        // Setup our internal default metaData dictionary,
        // (used to illustrate reading/writing plist data to our file package).
        //
        // Note: these are the default values.
        // If a document was previously saved to disk "readFromFileWrapper" will load the real metadata.
        //
        self.metaDataDict = [NSMutableDictionary dictionaryWithObjectsAndKeys:
                             @YES, MetaDataDisclosedKey,
                             @"someText", MetaDataValue2Key,
                             nil];
    }
    return self;
}

// -------------------------------------------------------------------------------
//  makeWindowControllers
//
//  NSDocumentController invokes this method when creating or opening new documents.
//  We override it to use our own custom subclass of NSWindowController.
// -------------------------------------------------------------------------------
- (void)makeWindowControllers
{
    // Load our hosting NSWindowController add attached it to this document.
    WindowController *windowController =
        [[NSStoryboard storyboardWithName:@"Main" bundle:nil] instantiateControllerWithIdentifier:@"WindowController"];

    [self addWindowController:windowController];

    // As a delegate we want to be notified when the user discloses the attachment view holding/displaying our image.
    [self ourViewController].delegate = self;

    // Notify our view controller to set its disclosure state for the attachmentView,
    // this will make sure the disclosure state in our window matches what's stored in this document.
    //
    BOOL disclosed = [[self.metaDataDict valueForKey:MetaDataDisclosedKey] boolValue];
    [self ourViewController].disclosed = disclosed;
}

// -------------------------------------------------------------------------------
//  setDisplayName
// -------------------------------------------------------------------------------
- (void)setDisplayName:(NSString *)displayNameOrNil
{
    // Trim off the extension when used for displaying in the window title.
    super.displayName = displayNameOrNil.stringByDeletingPathExtension;
}


#pragma mark - Accessors

// -------------------------------------------------------------------------------
//  ourWindowController
//
//  Convenience method, we have only one window controller.
// -------------------------------------------------------------------------------
- (WindowController *)ourWindowController
{
    return self.windowControllers[0];
}

// -------------------------------------------------------------------------------
//  ourViewController
//
//  Convenience method to access our content view controller.
// -------------------------------------------------------------------------------
- (ViewController *)ourViewController
{
    return (ViewController *)[self ourWindowController].contentViewController;
}


#pragma mark - Package Support

// -------------------------------------------------------------------------------
//  fileWrapperOfType:typeName:error
//
//  Called when the user saves this document or when autosave is performed.
//  Create and return a file wrapper that contains the contents of this document,
//  formatted for our specified type.
// -------------------------------------------------------------------------------
- (NSFileWrapper *)fileWrapperOfType:(NSString *)typeName error:(NSError **)outError
{
    // If the document was not read from file or has not previously been saved,
    // it doesn't have a file wrapper, so create one.
    //
    if (self.documentFileWrapper == nil)
    {
        NSFileWrapper *docfileWrapper = [[NSFileWrapper alloc] initDirectoryWithFileWrappers:@{}];
        self.documentFileWrapper = docfileWrapper;
    }

    NSDictionary *fileWrappers = self.documentFileWrapper.fileWrappers;

    // If there isn't a wrapper for the text file, create one too.
    if (fileWrappers[TextFileName] != nil)
    {
        NSFileWrapper *textWrapper = fileWrappers[TextFileName];
        [self.documentFileWrapper removeFileWrapper:textWrapper];
    }

    NSData *textData = [[self ourViewController].textView.string dataUsingEncoding:kTextFileEncoding];
    NSFileWrapper *textFileWrapper = [[NSFileWrapper alloc] initRegularFileWithContents:textData];
    textFileWrapper.preferredFilename = TextFileName;

    [self.documentFileWrapper addFileWrapper:textFileWrapper];

    // If the document file wrapper doesn't contain a file wrapper for an image and the image is not nil,
    // then create a file wrapper for the image and add it to the document file wrapper.
    //
    if ((self.documentFileWrapper.fileWrappers[ImageFileName] == nil) && (self.image != nil))
    {
        NSArray *imageRepresentations = self.image.representations;
        NSData *imageData = [NSBitmapImageRep representationOfImageRepsInArray:imageRepresentations
                                                                     usingType:NSPNGFileType
                                                                    properties:@{}];
        if (imageData == nil)
        {
            NSBitmapImageRep *imageRep = nil;
            @autoreleasepool
            {
                imageData = self.image.TIFFRepresentation;
                imageRep = [[NSBitmapImageRep alloc] initWithData:imageData];
            }
            imageData = [imageRep representationUsingType:NSPNGFileType properties:@{}];
        }

        NSFileWrapper *imageFileWrapper = [[NSFileWrapper alloc] initRegularFileWithContents:imageData];
        imageFileWrapper.preferredFilename = ImageFileName;

        [self.documentFileWrapper addFileWrapper:imageFileWrapper];
    }

    // Check if we already have a meta data file wrapper, first remove the old one if it exists.
    NSFileWrapper *metaDataFileWrapper = self.documentFileWrapper.fileWrappers[MetaDataFileName];
    if (metaDataFileWrapper != nil)
        [self.documentFileWrapper removeFileWrapper:metaDataFileWrapper];

    // Write the new file wrapper for our meta data.
    NSError *plistError = nil;
    NSData *propertyListData = [NSPropertyListSerialization dataWithPropertyList:self.metaDataDict format:NSPropertyListXMLFormat_v1_0 options:0 error:&plistError];
    if (propertyListData == nil || plistError != nil)
    {
        NSLog(@"Could not create metadata plist data: %@", plistError.localizedDescription);
        return nil;
    }

    NSFileWrapper *newMetaDataFileWrapper = [[NSFileWrapper alloc] initRegularFileWithContents:propertyListData];
    newMetaDataFileWrapper.preferredFilename = MetaDataFileName;

    [self.documentFileWrapper addFileWrapper:newMetaDataFileWrapper];

    return self.documentFileWrapper;
}

// -------------------------------------------------------------------------------
//  readFromFileWrapper:fileWrapper:typeName:outError
//
//  Set the contents of this document by reading from a file wrapper of a specified type,
//  and return YES if successful.
// -------------------------------------------------------------------------------
- (BOOL)readFromFileWrapper:(NSFileWrapper *)fileWrapper ofType:(NSString *)typeName error:(NSError **)outError
{
    /*
     When opening a document, look for the image and text file wrappers. For each wrapper,
     extract the data from it and keep the file wrapper itself. The file wrappers are kept
     so that, if the corresponding data hasn't been changed, they can be resused during a
     save and thus the source file itself can be reused rather than rewritten. This avoids
     the overhead of syncing data unnecessarily. If the data related to a file wrapper changes
     (a new image is added or the text is edited), the corresponding file wrapper object is
     disposed of and a new file wrapper created on save (see fileWrapperOfType:error:).
     */
    NSDictionary *fileWrappers = fileWrapper.fileWrappers;

    // Load the text file from it's wrapper.
    NSFileWrapper *imageFileWrapper = fileWrappers[ImageFileName];
    if (imageFileWrapper != nil)
    {
        NSData *imageData = imageFileWrapper.regularFileContents;
        NSImage *targetImage = [[NSImage alloc] initWithData:imageData];
        self.image = targetImage;
    }

    // Load the image file from it's wrapper.
    NSFileWrapper *textFileWrapper = fileWrappers[TextFileName];
    if (textFileWrapper != nil)
    {
        NSData *textData = textFileWrapper.regularFileContents;
        NSString *targetNotes = [[NSString alloc] initWithData:textData encoding:kTextFileEncoding];
        self.notes = targetNotes;
    }

    // Load the metaData file from it's wrapper.
    NSFileWrapper *metaDataFileWrapper = fileWrappers[MetaDataFileName];
    if (metaDataFileWrapper != nil)
    {
        // We have meta data in this document.
        NSData *metaData = metaDataFileWrapper.regularFileContents;
        NSMutableDictionary *finalMetadata = [NSPropertyListSerialization propertyListWithData:metaData options:NSPropertyListImmutable format:NULL error:outError];
        self.metaDataDict = finalMetadata;
    }

    self.documentFileWrapper = fileWrapper;

    return YES;
}


#pragma mark - Model Support

// -------------------------------------------------------------------------------
// entireRange
// -------------------------------------------------------------------------------
- (NSRange)entireRange
{
    NSTextView *targetTextView = [self ourViewController].textView;
    return NSMakeRange(0, targetTextView.string.length);
}

// -------------------------------------------------------------------------------
//  updateTextView:textView
//
//  Called by our window controller to update our text view after a read operation.
// -------------------------------------------------------------------------------
- (void)updateTextView:(NSTextView *)inTextView
{
    // Take our model data and apply it to the textView.
    if (_notes != nil)
    {
        [inTextView replaceCharactersInRange:[self entireRange] withString:_notes];
    }
}

// -------------------------------------------------------------------------------
//  updateImage:image
//
//  Called by our window controller to update our image view after a read operation.
// -------------------------------------------------------------------------------
- (void)updateImageView:(NSImageView *)inImageView
{
    // Take our model data and apply it to the textView.
    inImageView.image = self.image;
}

// -------------------------------------------------------------------------------
//  updateImageModel:image
//
//  This is called from our NSWindowController when an new image is dragged in.
// -------------------------------------------------------------------------------
- (void)updateImageModel:(NSImage *)inImage
{
    self.image = inImage;

    // Remove the image file wrapper, if it exists.
    NSFileWrapper *imageFileWrapper = self.documentFileWrapper.fileWrappers[ImageFileName];
    if (imageFileWrapper != nil)
    {
        [self.documentFileWrapper removeFileWrapper:imageFileWrapper];
    }

    // Auto save this change.
    [self updateChangeCount:NSChangeDone];
}

// -------------------------------------------------------------------------------
//  updateTextModel:text
//
//  This is called from our NSWindowController when the text has changed.
// -------------------------------------------------------------------------------
- (void)updateTextModel:(NSString *)text
{
    // Remove the text file wrapper, if it exists.
    NSFileWrapper *textFileWrapper = self.documentFileWrapper.fileWrappers[TextFileName];
    if (textFileWrapper != nil)
    {
        [self.documentFileWrapper removeFileWrapper:textFileWrapper];
    }

    // Auto save this change.
    [self updateChangeCount:NSChangeDone];
}

// -------------------------------------------------------------------------------
// updateChangeCount:change
// -------------------------------------------------------------------------------
- (void)updateChangeCount:(NSDocumentChangeType)change
{
    // Keep track of changes are handled automatically by NSDocument,
    // but in case we want to track these changes independently of the built in NSUndoManager, we do it here.
    //
    [super updateChangeCount:change];

    if (change == NSChangeDone)
    {
        // We are up to date.
    }
}


#pragma mark - ViewControllerDelegate

- (void)viewController:(ViewController *)viewController didDiscloseImage:(BOOL)disclosedImage
{
    // As a delegate we are notified by our content view controller subclass that the user disclosed
    // the attachmentView (holding/displaying the image).
    //
    [self.metaDataDict setValue:@(disclosedImage) forKey:MetaDataDisclosedKey];

    // Disclosure state is also saved as part of the docyment, so auto save this change.
    [self updateChangeCount:NSChangeDone];
}

@end
```

[Next](PackagedDocument-WindowController.m.md)[Previous](LICENSE.txt.md)

