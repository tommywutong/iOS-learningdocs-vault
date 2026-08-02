---
title: SampleRaster
apple_id: DTS40009295
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: null
published: '2011-09-06'
source_url: https://developer.apple.com/library/archive/samplecode/SampleRaster/Listings/SampleRasterPDE_m.html
archived_at: '2026-07-18T03:23:03.468384Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SampleRaster](SampleRaster.md)


[Next](SampleSuppliesView.h.md)[Previous](SampleRasterPDE.h.md)

# SampleRasterPDE.m

```objc
/*
     File: SampleRasterPDE.m 
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

#import "SampleRasterPDE.h"


@implementation SampleRasterPDEPlugIn
//
// 'initWithBundle' - Initialize the plug-in with the bundle info.
//

- (BOOL)initWithBundle:(NSBundle *)theBundle
{
  // We don't need the bundle here but the printing system needs this
  // method defined...
  return (YES);
}


//
// 'PDEPanelsForType:withHostInfo' - Create the views for our PDE.
//

- (NSArray*)PDEPanelsForType:(NSString *)pdeType withHostInfo:(id)host
{
  PDEPluginCallback *callback = (PDEPluginCallback *)host;
  NSMutableArray *pdes = [NSMutableArray array];

  if ([pdeType isEqual:(NSString *)kPrinterModuleTypeIDStr])
  {
    // Here we just add one PDE, but you can add multiple PDEs from this
    // method...
    SampleRasterPDE *pde = [[[SampleRasterPDE alloc] initWithCallback:callback] autorelease];

    if (pde != nil)
      [pdes addObject:pde];
    else
      pdes = nil;
  }

  return (pdes);
}
@end


@implementation SampleRasterPDE
//
// 'changeAdvanced' - Toggle the visibility of the advanced controls.
//

- (IBAction)changeAdvanced:(id)sender
{
  [advancedView setHidden:[advancedButton state] == NSOffState];
  [pdeCallback panelViewDidResize];
}


//
// 'changeMediaType' - Change the media type that is selected.
//

- (IBAction)changeMediaType:(id)sender
{
  ppd_option_t *MediaType = ppdFindOption(ppd, "MediaType");
  ppd_option_t *Resolution = ppdFindOption(ppd, "Resolution");
  ppd_choice_t *MediaType_choice = ppdFindMarkedChoice(ppd, "MediaType");
  int MediaType_index = [mediaType indexOfSelectedItem];
  const char *choice = MediaType->choices[MediaType_index].choice;

  // Set the media type and then, if successful, set the resolution and color mode.
  if ([pdeCallback willChangePPDOptionKeyValue:@"MediaType"
           ppdChoice:[NSString stringWithUTF8String:choice]])
  {
    // When printing on plain paper, print at a lower resolution and in black
    // and white.  Otherwise, print in color with the highest resolution...
    int Resolution_index = strcmp(choice, "Plain") != 0 ? Resolution->num_choices - 1 : 0;

    choice = Resolution->choices[Resolution_index].choice;

    if ([pdeCallback willChangePPDOptionKeyValue:@"Resolution"
                     ppdChoice:[NSString stringWithUTF8String:choice]])
      [printQuality selectItemAtIndex:Resolution_index];

    if ([pdeCallback willChangePPDOptionKeyValue:@"ColorModel"
                     ppdChoice:(MediaType_index > 0 ? @"RGB" : @"Gray")])
      [printInColor setState:MediaType_index > 0 ? NSOnState : NSOffState];
  }
  else
  {
    // We couldn't change the media type, revert to the previous selection...
    [mediaType selectItemAtIndex:(MediaType_choice - MediaType->choices)];
  }
}


//
// 'changePrintInColor' - Change between color and grayscale print modes.
//

- (IBAction)changePrintInColor:(id)sender
{
  // Change the color mode - since this option has no constraints, we do not
  // need to look at the return status...
  [pdeCallback willChangePPDOptionKeyValue:@"ColorModel"
           ppdChoice:([printInColor state] == NSOnState ? @"RGB" : @"Gray")];
}


//
// 'changePrintQuality' - Change the print quality that is selected.
//

- (IBAction)changePrintQuality:(id)sender
{
  ppd_option_t *Resolution = ppdFindOption(ppd, "Resolution");
  ppd_choice_t *Resolution_choice = ppdFindMarkedChoice(ppd, "Resolution");
  int i = [printQuality indexOfSelectedItem];

  // Change the output resolution, reverting as needed...
  if (![pdeCallback willChangePPDOptionKeyValue:@"Resolution"
                    ppdChoice:[NSString stringWithUTF8String:
                                Resolution->choices[i].choice]])
    [printQuality selectItemAtIndex:(Resolution_choice - Resolution->choices)];
}


//
// 'dealloc' - Release memory used by the PDE panel.
//
// The dealloc method is called on object deallocation when garbage
// collection is not in effect.
//

- (void)dealloc
{
  [pdeBundle release];
  [pdeCallback release];
  [pdeName release];

  [super dealloc];
}


//
// 'initWithCallback' - Initialize the PDE panel.
//

- (id)initWithCallback:(PDEPluginCallback *)callback
{
  // Initialize the superclass, return if we can't do so...
  if ((self = [super init]) == nil)
    return (nil);

  // Initialize instance variables...
  pdeBundle   = [[NSBundle bundleForClass:[self class]] retain];
  pdeCallback = [callback retain];
  pdeName     = nil;

  ppd = [pdeCallback ppdFile];

  // Initialize the MediaType and Resolution option menus...
  [self loadMenu:mediaType withOption:"MediaType"];
  [self loadMenu:printQuality withOption:"Resolution"];

  // Return a pointer to the newly initialized instance...  
  return (self);
}


//
// 'loadMenu:withOption' - Load a menu with an option's choices.
//

- (void)loadMenu:(NSPopUpButton *)menu withOption:(const char *)name
{
  int i;
  ppd_option_t *option = ppdFindOption(ppd, name);
  ppd_choice_t *choice;

  if (!option)
    return;

  [menu removeAllItems];
  for (i = 0, choice = option->choices; i < option->num_choices; i ++, choice ++)
  {
    [menu addItemWithTitle:[NSString stringWithUTF8String:choice->text]];
    if (choice->marked)
      [menu selectItemAtIndex:i];
  }
}


//
// 'panelKind' - Return the kind ID for this PDE.
//

- (NSString *)panelKind
{
  return ((NSString *)@"com.apple.examples.print.pde.SampleRasterKind");
}


//
// 'panelName' - Return the localized name for this PDE.
//
// The name is used as its title in the menu of printing panes.
//

- (NSString *)panelName
{
  if (pdeName == NULL)
    pdeName = [[pdeBundle localizedStringForKey:@"Output Mode" value:nil table:nil] retain];

  return (pdeName);
}


//
// 'panelView' - Return the NSView for this PDE.
//
// This method has "get" semantics so we continue to own a reference to
// the NSView it returns.
//
- (NSView *)panelView
{
  if (sampleRasterView == NULL)
    [NSBundle loadNibNamed:@"SampleRasterPDE" owner:self];

  return (sampleRasterView);
}


//
// 'PPDOptionKeyValueDidChange:ppdChoice' - Update the user interface for option changes.
//

- (void)PPDOptionKeyValueDidChange:(NSString *)option ppdChoice:(NSString *)choice
{
  // Here we just call the restore method since we only have 3 options.  If
  // we had more then we might optimize the PDE to compare the option strings
  // and update the appropriate control(s)...
  [self restoreValuesAndReturnError:nil];
}


//
// 'restoreValuesAndReturnError' - Read the new settings values and update our UI accordinly.
//

- (BOOL)restoreValuesAndReturnError:(NSError **)error
{
  int i;
  ppd_choice_t *ColorModel = ppdFindMarkedChoice(ppd, "ColorModel");
  ppd_option_t *MediaType = ppdFindOption(ppd, "MediaType");
  ppd_option_t *Resolution = ppdFindOption(ppd, "Resolution");


  // Update ColorModel
  [printInColor setState:ColorModel && !strcmp(ColorModel->choice, "RGB")];

  // Update MediaType
  for (i = 0; i < MediaType->num_choices; i ++)
    if (MediaType->choices[i].marked)
    {
      [mediaType selectItemAtIndex:i];
      break;
    }

  // Update Resolution
  for (i = 0; i < Resolution->num_choices; i ++)
    if (Resolution->choices[i].marked)
    {
      [printQuality selectItemAtIndex:i];
      break;
    }

  // Return YES to indicate everything is A-OK...
  return (YES);
}


//
// 'saveValuesAndReturnError' - Set UI/stored values to the print settings.
//

- (BOOL)saveValuesAndReturnError:(NSError **)error
{
  // Nothing to do for standard PPD options on 10.5 and higher.
  return (YES);
}


//
// 'shouldHide' - Should we allow the PDE panel to be hidden.
//
// This method allows a PDE to valid the user selections one last time before
// panel is hidden.
//

- (BOOL)shouldHide
{
  return (YES);
}


//
// 'summaryInfo' - Format selections for the summary panel.
//

- (NSDictionary *)summaryInfo
{
  NSMutableDictionary *info = [NSMutableDictionary dictionaryWithCapacity:10];
  [info setObject:@"TBD" forKey:pdeName];

  return (info);
}


//
// 'supportedPPDOptionKeys' - Return an NSArray of PPD option keywords supported by this PDE.
//

- (NSArray *)supportedPPDOptionKeys;
{
  return ([NSArray arrayWithObjects:@"ColorModel", @"MediaType", @"Resolution", nil]);
}


//
// 'willShow' - The PDE panel is about to be shown.
//

- (void)willShow
{
  // Do nothing
}       
@end
```

[Next](SampleSuppliesView.h.md)[Previous](SampleRasterPDE.h.md)

