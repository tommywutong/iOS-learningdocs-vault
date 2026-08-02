---
title: PDF Annotation Editor
apple_id: DTS10004035
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2017-10-30'
source_url: https://developer.apple.com/library/archive/samplecode/PDFAnnotationEditor/Listings/MyDocument_m.html
archived_at: '2026-07-18T03:18:24.859191Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PDF Annotation Editor](PDF%20Annotation%20Editor.md)


[Next](Controller.m.md)[Previous](MyWindowController.m.md)

# MyDocument.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The implementation file of MyDocument.
*/ 

// =====================================================================================================================
//  MyDocument.m
// =====================================================================================================================


#import "MyDocument.h"
#import "MyWindowController.h"


@implementation MyDocument
// ========================================================================================================== MyDocument
// ---------------------------------------------------------------------------------------------------------------- init

- (id) init
{
    self = [super init];
    if (self)
    {
        // Add your subclass-specific initialization here.
        // If an error occurs here, send a [self release] message and return nil.

    }

    return self;
}

// ------------------------------------------------------------------------------------------------------- windowNibName

- (NSString *) windowNibName
{
    // Override returning the nib file name of the document
    return @"MyDocument";
}

// ----------------------------------------------------------------------------------------------- makeWindowControllers

- (void) makeWindowControllers
{
    MyWindowController  *controller;

    // Create controller.
    controller = [[MyWindowController alloc] initWithWindowNibName: [self windowNibName]];
    [self addWindowController: controller];

    // Done.
    [controller release];
}

// ------------------------------------------------------------------------------------------ windowControllerDidLoadNib
/*
- (void) windowControllerDidLoadNib: (NSWindowController *) aController
{
    // Super.
    [super windowControllerDidLoadNib: aController];
}
*/
// -------------------------------------------------------------------------------------------- dataRepresentationOfType

- (NSData *) dataRepresentationOfType: (NSString *) aType
{
    // Insert code here to write your document from the given data.  
    // You can also choose to override -fileWrapperRepresentationOfType: or -writeToFile:ofType: instead.

    // For applications targeted for Tiger or later systems, you should use the new Tiger API -dataOfType:error:.  
    // In this case you can also choose to override -writeToURL:ofType:error:, 
    // -fileWrapperOfType:error:, or -writeToURL:ofType:forSaveOperation:originalContentsURL:error: instead.

    return NULL;
}

// ---------------------------------------------------------------------------------------------- loadDataRepresentation

- (BOOL) loadDataRepresentation: (NSData *) data ofType: (NSString *) aType
{
    // Insert code here to read your document from the given data. 
    // You can also choose to override -loadFileWrapperRepresentation:ofType: or -readFromFile:ofType: instead.

    // For apps targeted for Tiger or later systems, you should use the new Tiger API readFromData:ofType:error:.
    // In this case you can also choose to override -readFromURL:ofType:error: or 
    // -readFromFileWrapper:ofType:error: instead.

    return YES;
}

@end
```

[Next](Controller.m.md)[Previous](MyWindowController.m.md)

