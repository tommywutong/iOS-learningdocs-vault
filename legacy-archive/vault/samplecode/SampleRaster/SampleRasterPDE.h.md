---
title: SampleRaster
apple_id: DTS40009295
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: null
published: '2011-09-06'
source_url: https://developer.apple.com/library/archive/samplecode/SampleRaster/Listings/SampleRasterPDE_h.html
archived_at: '2026-07-18T03:23:03.426838Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SampleRaster](SampleRaster.md)


[Next](SampleRasterPDE.m.md)[Previous](SampleController.m.md)

# SampleRasterPDE.h

```objc
/*
     File: SampleRasterPDE.h 
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

#import <Cocoa/Cocoa.h>

#if MAC_OS_X_VERSION_MAX_ALLOWED <= MAC_OS_X_VERSION_10_5
#  import <Print/PDEPluginInterface.h>
#  import <Print/PMPrintingDialogExtensions.h>
#else
#  import <PrintCore/PDEPluginInterface.h>
#  import <PrintCore/PMPrintingDialogExtensions.h>
#endif


@interface SampleRasterPDEPlugIn : NSObject
{
}
@end

@interface PDEPluginCallback : NSObject
{
}
@end

@interface SampleRasterPDE : NSObject
{
  IBOutlet id advancedButton;
  IBOutlet id advancedView;
  IBOutlet id mediaType;
  IBOutlet id printInColor;
  IBOutlet id printQuality;
  IBOutlet id sampleRasterView;

  NSBundle *pdeBundle;
  PDEPluginCallback *pdeCallback;
  NSString *pdeName;

  ppd_file_t *ppd;
}

- (IBAction)changeAdvanced:(id)sender;
- (IBAction)changeMediaType:(id)sender;
- (IBAction)changePrintInColor:(id)sender;
- (IBAction)changePrintQuality:(id)sender;
- (id)initWithCallback:(PDEPluginCallback *)callback;
- (void)loadMenu:(NSPopUpButton *)menu withOption:(const char *)name;
@end
```

[Next](SampleRasterPDE.m.md)[Previous](SampleController.m.md)

