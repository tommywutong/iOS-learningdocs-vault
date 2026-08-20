---
title: PDF Annotation Editor
apple_id: DTS10004035
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2017-10-30'
source_url: https://developer.apple.com/library/archive/samplecode/PDFAnnotationEditor/Listings/MyWindowController_h.html
archived_at: '2026-07-18T03:18:24.995586Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PDF Annotation Editor](PDF%20Annotation%20Editor.md)


[Next](MyStampAnnotation.m.md)[Previous](PDFViewEdit.h.md)

# MyWindowController.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 PDFAnnotation Editor's custom subclass of NSWindowController. This is used to
         drive multiple open windows within one instance of PDFAnnotation Editor, along
         with assisting saving new PDF files and updating any annotation changes from the
         application. This file also helps drive the toggle between Edit mode and Test mode
         per window. Edit mode allows the user to actively move/edit any annotations in the
         PDF, while Test mode does not as it acts as purely a PDF 'viewer'; users can toggle
         between these modes via the NSSegmentedControl at the bottom of each window.
*/

// =====================================================================================================================
//  MyWindowController.h
// =====================================================================================================================


#import <Cocoa/Cocoa.h>
#import <Quartz/Quartz.h>


@class PDFViewEdit;


@interface MyWindowController : NSWindowController < PDFDocumentDelegate >
{
    IBOutlet PDFViewEdit            *_pdfView;
    IBOutlet NSProgressIndicator    *_saveProgressBar;          // Saving.
    IBOutlet NSPanel                *_saveWindow;
    IBOutlet NSSegmentedControl     *_editTestButton;
}

- (void) setupDocumentNotifications;
- (void) setEditTestMode: (id) sender;

@end
```

[Next](MyStampAnnotation.m.md)[Previous](PDFViewEdit.h.md)

