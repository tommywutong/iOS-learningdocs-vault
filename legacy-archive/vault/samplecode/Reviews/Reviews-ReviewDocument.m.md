---
title: Reviews
apple_id: DTS40010057
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2011-07-21'
source_url: https://developer.apple.com/library/archive/samplecode/Reviews/Listings/Reviews_ReviewDocument_m.html
archived_at: '2026-07-18T03:22:13.018764Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Reviews](Reviews.md)


[Next](Document%20Revision%20History.md)[Previous](Reviews-ReviewDocument.h.md)

# Reviews/ReviewDocument.m

```objc
/*
     File: ReviewDocument.m 
 Abstract: The main document window is read-only, as a demo of accessibility image descriptions.

  Version: 1.1 

 Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple 
 Inc. ("Apple") in consideration of your agreement to the following 
 terms, and your use, installation, modification or redistribution of 
 this Apple software constitutes acceptance of these terms.  If you do 
 not agree with these terms, please do not use, install, modify or 
 redistribute this Apple software. 

 In consideration of your agreement to abide by the following terms, and 
 subject to these terms, Apple grants you a personal, non-exclusive 
 license, under Apple's copyrights in this original Apple software (the 
 "Apple Software"), to use, reproduce, modify and redistribute the Apple 
 Software, with or without modifications, in source and/or binary forms; 
 provided that if you redistribute the Apple Software in its entirety and 
 without modifications, you must retain this notice and the following 
 text and disclaimers in all such redistributions of the Apple Software. 
 Neither the name, trademarks, service marks or logos of Apple Inc. may 
 be used to endorse or promote products derived from the Apple Software 
 without specific prior written permission from Apple.  Except as 
 expressly stated in this notice, no other rights or licenses, express or 
 implied, are granted by Apple herein, including but not limited to any 
 patent rights that may be infringed by your derivative works or by other 
 works in which the Apple Software may be incorporated. 

 The Apple Software is provided by Apple on an "AS IS" basis.  APPLE 
 MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION 
 THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS 
 FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND 
 OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS. 

 IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL 
 OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
 SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
 INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION, 
 MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED 
 AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE), 
 STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE 
 POSSIBILITY OF SUCH DAMAGE. 

 Copyright (C) 2011 Apple Inc. All Rights Reserved. 

 */

#import "ReviewDocument.h"

@implementation ReviewDocument

- (NSString *)windowNibName 
{
    return @"ReviewDocument";
}

/*  The main document window is read-only, as a demo of accessibility image descriptions.
    The editing window allows editing of the contents of the document.
    This illustrates a basic use of multiple windows being used for the same document.
*/
- (IBAction)showEditingWindow:(id)sender {
    if (!editingWindowController) {
    editingWindowController = [[NSWindowController alloc] initWithWindowNibName:@"EditingWindow"];
    [self addWindowController:editingWindowController];
    } 
    [editingWindowController showWindow:nil];
}

- (void)dealloc {
    [editingWindowController release];
    [super dealloc];
}


#pragma mark -
#pragma mark Split View Delegate Method

// Delegate method keeps the section containing the collection view from adjusting when window is resized
- (BOOL)splitView:(NSSplitView *)splitView shouldAdjustSizeOfSubview:(NSView *)view {
    return (view != [collectionView enclosingScrollView]);
}


@end
```

[Next](Document%20Revision%20History.md)[Previous](Reviews-ReviewDocument.h.md)

