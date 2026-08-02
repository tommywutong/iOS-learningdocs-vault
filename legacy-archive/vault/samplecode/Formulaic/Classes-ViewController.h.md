---
title: Formulaic
apple_id: DTS40008932
resource_type: Sample Code
platform: iOS
topic: General
technology: null
published: '2010-07-01'
source_url: https://developer.apple.com/library/archive/samplecode/Formulaic/Listings/Classes_ViewController_h.html
archived_at: '2026-07-18T03:08:49.721961Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Formulaic](Formulaic.md)


[Next](Classes-ViewController.m.md)[Previous](Classes-TabularDataCell.m.md)

# Classes/ViewController.h

```objc
/*
     File: ViewController.h
 Abstract: View controller, the main view controller of the app
  Version: 1.2

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

 Copyright (C) 2010 Apple Inc. All Rights Reserved.

*/

#import "GraphingView.h"

@interface ViewController : UIViewController <UITextFieldDelegate, UITableViewDataSource> 
{
@private
    // Main View
    IBOutlet GraphingView *graphingView;
    IBOutlet UITextField *valueField;
    IBOutlet UISlider *slider;
    IBOutlet UILabel *resultLabel;
    IBOutlet UIButton *stopWatch;

    // Tabular Data slide in view
    IBOutlet UIView *tabularDataView;
    IBOutlet UITableView *tabularDataTableView;

    BOOL stopWatchStateOn;
    BOOL stopWatchDirectionUp;
    BOOL shouldUpdateGraph;
}

- (IBAction)sliderWasChanged:(id)sender;

- (IBAction)stopWatchButtonWasPressed:(id)sender;
- (IBAction)tableButtonWasPressed:(id)sender;

- (IBAction)textFieldChanged:(id)sender;
- (IBAction)touchesEndedForGraphingView:(id)sender event:(UIEvent *)event;

- (IBAction)doneButtonPressed;

@end
```

[Next](Classes-ViewController.m.md)[Previous](Classes-TabularDataCell.m.md)

