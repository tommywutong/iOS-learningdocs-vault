---
title: Using AirPrint to Print a Banner
apple_id: DTS40013422
resource_type: Sample Code
platform: iOS
topic: General
technology: null
published: '2014-03-12'
source_url: https://developer.apple.com/library/archive/samplecode/PrintBanner/Listings/PrintBanner_ViewController_h.html
archived_at: '2026-07-18T03:19:32.160197Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using AirPrint to Print a Banner](Using%20AirPrint%20to%20Print%20a%20Banner.md)


[Next](PrintBanner-ViewController.m.md)[Previous](PrintBanner-main.m.md)

# PrintBanner/ViewController.h

```objc
/*
     File: ViewController.h
 Abstract: The main view controller containing the app's user interface. Sets up printing using input from the user (text, font, font color). Calculates a font size that optimizes banner text for the width of the available paper. Calculates a cut-size based on the length of the text.

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

 Copyright (C) 2014 Apple Inc. All Rights Reserved.

 */

#import <UIKit/UIKit.h>

@interface ViewController : UIViewController <UIPrintInteractionControllerDelegate> {
    UISimpleTextPrintFormatter *_textFormatter;
}

@property (strong) IBOutlet UITextField *textField;
@property (strong) IBOutlet UISegmentedControl *fontSelection;
@property (strong) IBOutlet UISegmentedControl *colorSelection;
@property (strong) IBOutlet UIButton *printButton;

- (IBAction)print:(id)sender;
- (UIFont *)chosenFontWithSize:(CGFloat)fontSize;
- (UIColor *)chosenColor;

@end
```

[Next](PrintBanner-ViewController.m.md)[Previous](PrintBanner-main.m.md)

