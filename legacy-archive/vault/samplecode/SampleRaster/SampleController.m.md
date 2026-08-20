---
title: SampleRaster
apple_id: DTS40009295
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: null
published: '2011-09-06'
source_url: https://developer.apple.com/library/archive/samplecode/SampleRaster/Listings/SampleController_m.html
archived_at: '2026-07-18T03:23:03.369164Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SampleRaster](SampleRaster.md)


[Next](SampleRasterPDE.h.md)[Previous](SampleController.h.md)

# SampleController.m

```objc
/*
     File: SampleController.m 
 Abstract: Window controller definitions for sample printer utility for Mac OS X.

MOST PRINTER DRIVERS DO NOT REQUIRE A PRINTER UTILITY.  This utility is
provided for testing/experimentation with the "Sample Printer" example
raster printer driver for CUPS. 
  Version: 4.0 

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

#import "SampleController.h"
#import "SampleSuppliesView.h"


@implementation SampleController
//
// 'applicationDidFinishLaunching' - Get the printer ID.
//

- (void)applicationDidFinishLaunching:(NSNotification *)notification
{
  // Get the printer ID...
  NSAppleEventDescriptor *event = [[NSAppleEventManager sharedAppleEventManager] currentAppleEvent];

  if (event)
    [suppliesView setPrinterId:[[event paramDescriptorForKeyword:keyAEPropData] stringValue]];
}


//
// 'applicationShouldTerminateAfterLastWindowClosed' - Quit the utility when the window is closed.
//

- (BOOL)applicationShouldTerminateAfterLastWindowClosed:(NSApplication *)sender;
{
  (void)sender;

  return (YES);
}


//
// 'cleanPrintHeads' - Send a "Clean all" command to the queue.
//

- (IBAction)cleanPrintHeads: (id)sender
{
  [suppliesView sendCommand:"Clean all" withTitle:NSLocalizedString(@"Clean Print Heads", NULL)];
}


//
// 'changeInks' - Send a "ChangeInk all" command to the queue.
//

- (IBAction)changeInks: (id)sender
{
  [suppliesView sendCommand:"ChangeInk all" withTitle:NSLocalizedString(@"Change Inks", NULL)];
}


//
// 'printSelfTestPage' - Print a self-text page.
//

- (IBAction)printSelfTestPage: (id)sender
{
  [suppliesView sendCommand:"PrintSelfTestPage" withTitle:NSLocalizedString(@"Self-Test Page", NULL)];
}
@end
```

[Next](SampleRasterPDE.h.md)[Previous](SampleController.h.md)

