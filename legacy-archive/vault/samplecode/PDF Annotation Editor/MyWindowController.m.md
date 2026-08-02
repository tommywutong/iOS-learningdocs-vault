---
title: PDF Annotation Editor
apple_id: DTS10004035
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2017-10-30'
source_url: https://developer.apple.com/library/archive/samplecode/PDFAnnotationEditor/Listings/MyWindowController_m.html
archived_at: '2026-07-18T03:18:25.043462Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PDF Annotation Editor](PDF%20Annotation%20Editor.md)


[Next](MyDocument.m.md)[Previous](LICENSE.txt.md)

# MyWindowController.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The implementation file for MyWindowController.
*/ 

// =====================================================================================================================
//  MyWindowController.m
// =====================================================================================================================


#import "AnnotationPanel.h"
#import "MyWindowController.h"
#import "PDFViewEdit.h"


@implementation MyWindowController
// ================================================================================================== MyWindowController
// ------------------------------------------------------------------------------------------------------- windowDidLoad

- (void) windowDidLoad
{
    PDFDocument     *pdfDoc;
    AnnotationPanel *annotPanel;

    // Create PDFDocument.
    pdfDoc = [[PDFDocument alloc] initWithURL:[[self document] fileURL]];

    // Set document.
    [_pdfView setDocument: pdfDoc];
    [pdfDoc release];

    // Default display mode.
    [_pdfView setAutoScales: YES];

    // Indicate edit mode.
    [_pdfView setEditMode: ([_editTestButton selectedSegment] == 0)];

    // Enable drag & drop of PDF files.
    [_pdfView setAcceptsDraggedFiles:YES];

    // Establish notifications for this document.
    [self setupDocumentNotifications];

    // Bring up annotation panel.
    annotPanel = [AnnotationPanel sharedAnnotationPanel];
    [[NSNotificationCenter defaultCenter] addObserver: self selector: @selector(annotationChanged:) 
            name: AnnotationPanelAnnotationDidChangeNotification object: annotPanel];
}

// ------------------------------------------------------------------------------------------ setupDocumentNotifications

- (void) setupDocumentNotifications
{
    // Document saving progress notifications.
    [[NSNotificationCenter defaultCenter] addObserver: self selector: @selector(documentBeginWrite:) 
            name: @"PDFDidBeginDocumentWrite" object: [_pdfView document]];
    [[NSNotificationCenter defaultCenter] addObserver: self selector: @selector(documentEndWrite:) 
            name: @"PDFDidEndDocumentWrite" object: [_pdfView document]];
    [[NSNotificationCenter defaultCenter] addObserver: self selector: @selector(documentEndPageWrite:) 
            name: @"PDFDidEndPageWrite" object: [_pdfView document]];

    // Delegate.
    [[_pdfView document] setDelegate: self];
}

// ------------------------------------------------------------------------------------------------------------- dealloc

- (void) dealloc
{
    // No more notifications.
    [[NSNotificationCenter defaultCenter] removeObserver: self];

    // Call super.
    [super dealloc];
}

#pragma mark -------- actions
// ----------------------------------------------------------------------------------------------------- setEditTestMode

- (void) setEditTestMode: (id) sender;
{
    // Tell our PDFView sublclass what mode it is in.
    [_pdfView setEditMode: ([(NSSegmentedControl *)sender selectedSegment] == 0)];
}

#pragma mark -------- annotation panel notification
// --------------------------------------------------------------------------------------------------- annotationChanged

- (void) annotationChanged: (NSNotification *) notification
{
    // Lazy.
    [_pdfView setNeedsDisplay: YES];

    // Tell our subclass about the annotation change.
    [_pdfView annotationChanged];
}

#pragma mark -------- save progress
// -------------------------------------------------------------------------------------------------- documentBeginWrite

- (void) documentBeginWrite: (NSNotification *) notification
{
    // Establish maximum and current value for progress bar.
    [_saveProgressBar setMaxValue: (double)[[_pdfView document] pageCount]];
    [_saveProgressBar setDoubleValue: 0.0];

    // Bring up the save panel as a sheet.
    [[self window] beginSheet: _saveWindow completionHandler: ^(NSModalResponse returnCode) {
        [[[self window] sheetParent] endSheet:[self window] returnCode:returnCode];
    }];
}

// ---------------------------------------------------------------------------------------------------- documentEndWrite

- (void) documentEndWrite: (NSNotification *) notification
{
    [NSApp endSheet: _saveWindow];
}

// ------------------------------------------------------------------------------------------------ documentEndPageWrite

- (void) documentEndPageWrite: (NSNotification *) notification
{
    [_saveProgressBar setDoubleValue: [[[notification userInfo] objectForKey: @"PDFDocumentPageIndex"] floatValue]];
    [_saveProgressBar displayIfNeeded];
}

// --------------------------------------------------------------------------------------------- saveProgressSheetDidEnd

- (void) saveProgressSheetDidEnd: (NSWindow *) sheet returnCode: (int) returnCode contextInfo: (void *) contextInfo
{
    [_saveWindow close];
}

@end
```

[Next](MyDocument.m.md)[Previous](LICENSE.txt.md)

