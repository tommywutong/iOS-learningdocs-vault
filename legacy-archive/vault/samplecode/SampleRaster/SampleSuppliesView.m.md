---
title: SampleRaster
apple_id: DTS40009295
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: null
published: '2011-09-06'
source_url: https://developer.apple.com/library/archive/samplecode/SampleRaster/Listings/SampleSuppliesView_m.html
archived_at: '2026-07-18T03:23:03.624643Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SampleRaster](SampleRaster.md)


[Next](sampletopdf.c.md)[Previous](SampleSuppliesView.h.md)

# SampleSuppliesView.m

```objc
/*
     File: SampleSuppliesView.m 
 Abstract: Supply level view implementation for sample printer utility for Mac OS X.

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

#import <notify.h>
#import "SampleSuppliesView.h"

//
// 'supply_shader()' - A CG shader function that provides a specular highlight...
//

static void
supply_shader(void *info, const CGFloat *in, CGFloat *out)
{
  // This shader adds a specular highlight to the bar.
  CGFloat temp = sin(in[0] * M_PI * 1.25);
  out[0] = out[1] = out[2] = 1.0;
  out[3] = 0.45 * fabs(temp * temp * temp);
}


@implementation SampleSuppliesView
//
// 'dealloc' - Free memory used by the view.
//

- (void)dealloc
{
  ippDelete(data_);
  ppdClose(ppd_);
  httpClose(http_);

  if (shader_)
    CGShadingRelease(shader_);

#if !USE_GCD
  if (thread_)
    [thread_ cancel];
#endif
  [super dealloc];
}

#if !USE_GCD
 //
// 'initWithFrame' - Initialize the view.
//

- (id)initWithFrame:(NSRect)frame
{
  if ((self = [super initWithFrame:frame]) != nil)
  {
    printerURI_[0] = '\0';
    resource_[0] = '\0';
    http_ = NULL;
    data_ = NULL;
    ppd_ = NULL;
    shader_ = NULL;
    thread_ = NULL;
  }

  return (self);
}
#endif

//
// 'drawRect' - Draw the view.
//

- (void)drawRect:(NSRect)rect
{
  // Get the values 
  ipp_attribute_t *colors = ippFindAttribute(data_, "marker-colors", IPP_TAG_NAME);
  ipp_attribute_t *levels = ippFindAttribute(data_, "marker-levels", IPP_TAG_INTEGER);
  ipp_attribute_t *high_levels = ippFindAttribute(data_, "marker-high-levels", IPP_TAG_INTEGER);
  ipp_attribute_t *low_levels = ippFindAttribute(data_, "marker-low-levels", IPP_TAG_INTEGER);
  ipp_attribute_t *message = ippFindAttribute(data_, "marker-message", IPP_TAG_TEXT);
  ipp_attribute_t *names = ippFindAttribute(data_, "marker-names", IPP_TAG_NAME);

  if (!colors || !levels || !names)
    return;

  // Loop through each supply...
  int i;
  float middle = rect.origin.x + 0.25 * rect.size.width;

  for (i = 0; i < levels->num_values; i ++)
  {
    // Get the top of this supply...
    float bottom = rect.origin.y + rect.size.height - (i + 1) * SUPPLY_SPACING;

    // Draw the text label for the supply.
    NSString *label = [NSString stringWithUTF8String:names->values[i].string.text];
    NSSize labelSize = [label sizeWithAttributes:nil];
    NSRect labelRect = NSMakeRect(middle - labelSize.width - 5.0, bottom + 0.5 * (25.0 - labelSize.height), labelSize.width, labelSize.height);

    [[NSColor blackColor] set];
    [label drawInRect:labelRect withAttributes:nil];

    // Draw the supply level...
    int low = 15, high = 100;

    if (low_levels && i < low_levels->num_values)
      low = low_levels->values[i].integer;

    if (high_levels && i < high_levels->num_values)
      high = high_levels->values[i].integer;

    NSRect levelRect = NSMakeRect(middle, bottom + 0.5 * (SUPPLY_SPACING - SUPPLY_HEIGHT), levels->values[i].integer * 0.005 * rect.size.width, SUPPLY_HEIGHT);
    if (colors->values[i].string.text[0] != '#')
      [[NSString stringWithFormat:@"%d%%", levels->values[i].integer] drawInRect:levelRect withAttributes:nil];
    else
    {
      // Get the color for this supply...
      unsigned rgb = strtoul(colors->values[i].string.text + 1, NULL, 16);
      CGFloat red = ((rgb >> 16) & 255) / 255.0;
      CGFloat green = ((rgb >> 8) & 255) / 255.0;
      CGFloat blue = (rgb & 255) / 255.0;

      [NSGraphicsContext saveGraphicsState];

    // Draw the shadow...
    NSRect barRect = NSMakeRect(middle, bottom + 0.5 * (SUPPLY_SPACING - SUPPLY_HEIGHT), 0.5 * rect.size.width, SUPPLY_HEIGHT);
    CGContextRef context = (CGContextRef)[[NSGraphicsContext currentContext] graphicsPort];

    [[NSColor colorWithCalibratedWhite:0.333 alpha:0.5] set];
    CGContextSetShadow(context, CGSizeMake(1.0, -1.0), 1.0);
    [NSBezierPath strokeRect:barRect];

    // Draw the base bar...
    [[NSColor colorWithCalibratedRed:red green:green blue:blue alpha:0.666] setFill];
    [NSBezierPath fillRect:levelRect];

        levelRect.origin.x += levelRect.size.width;
    levelRect.size.width = 0.5 * rect.size.width - levelRect.size.width;
    [[NSColor colorWithCalibratedWhite:0.5 alpha:0.5] setFill];
    [NSBezierPath fillRect:levelRect];

        // Add tick and low/high marks...
    [[NSColor colorWithCalibratedWhite:1.0 alpha:0.25] setStroke];
    NSBezierPath *path = [NSBezierPath bezierPath];
    int j;
    for (j = 0; j <= 10; j ++)
    {
      [path moveToPoint:NSMakePoint(middle + j * barRect.size.width / 10, barRect.origin.y)];
      [path relativeLineToPoint:NSMakePoint(0.0, SUPPLY_HEIGHT)];
        }
    if (low > 0)
    {
      [path moveToPoint:NSMakePoint(middle + low * barRect.size.width / 100, barRect.origin.y)];
      [path relativeLineToPoint:NSMakePoint(0.0, SUPPLY_HEIGHT)];
        }
    if (high < 100)
    {
      [path moveToPoint:NSMakePoint(middle + high * barRect.size.width / 100, barRect.origin.y)];
      [path relativeLineToPoint:NSMakePoint(0.0, SUPPLY_HEIGHT)];
        }
    [path stroke];

    // Finally, overlay the bar with a shaded specular highlight...
    if (!shader_)
    {
      // Create the shader...
      CGFunctionCallbacks callbacks = { 0, supply_shader, NULL };
      CGColorSpaceRef colorSpace = CGColorSpaceCreateDeviceRGB();
      CGFunctionRef function = CGFunctionCreate(NULL, 1, NULL, 4, NULL, &callbacks);

      shader_ = CGShadingCreateAxial(colorSpace, CGPointMake(0, 1), CGPointMake(0, 0), function, false, false);

      CGFunctionRelease(function);
      CGColorSpaceRelease(colorSpace);
    }

    NSRectClip(barRect);

    NSAffineTransform *transform = [NSAffineTransform transform];
    [transform translateXBy:barRect.origin.x yBy:barRect.origin.y];
    [transform scaleXBy:barRect.size.width yBy:barRect.size.height];
    [transform concat];

    CGContextDrawShading(context, shader_);

      [NSGraphicsContext restoreGraphicsState];
    }
  }

  // Then any message...
  if (message && message->values[0].string.text[0])
  {
    NSString *label = [NSString stringWithUTF8String:message->values[0].string.text];
    NSSize labelSize = [label sizeWithAttributes:nil];
    NSRect labelRect = NSMakeRect(rect.origin.x + 0.5 * (rect.size.width - labelSize.width), rect.origin.y + 0.5 * (25.0 - labelSize.height), labelSize.width, labelSize.height);

    [[NSColor blackColor] set];
    [label drawInRect:labelRect withAttributes:nil];
  }
}


//
// 'sendCommand' - Send a printer command in a command file.
//
// Note: This method will eventually use a new PMPrinter API...
//

- (void)sendCommand: (const char *)command withTitle: (NSString *)title
{
  // Check that we have a printer...
  if (!resource_[0])
    return;

  // Create a temporary file containing the CUPS command file...
  char filename[1024];
  cups_file_t *fp = cupsTempFile2(filename, sizeof(filename));
  cupsFilePuts(fp, "#CUPS-COMMAND\n");
  cupsFilePrintf(fp, "%s\n", command);
  cupsFileClose(fp);

  // Print the file using the Print-Job operation...
  ipp_t *request = ippNewRequest(IPP_PRINT_JOB);
  ippAddString(request, IPP_TAG_OPERATION, IPP_TAG_URI, "printer-uri", NULL, printerURI_);
  ippAddString(request, IPP_TAG_OPERATION, IPP_TAG_NAME, "requesting-user-name", NULL, cupsUser());
  ippAddString(request, IPP_TAG_OPERATION, IPP_TAG_MIMETYPE, "document-format", NULL, "application/vnd.cups-command");
  ippAddString(request, IPP_TAG_OPERATION, IPP_TAG_NAME, "job-name", NULL, [title UTF8String]);

  ippDelete(cupsDoFileRequest(http_, request, resource_, filename));

  if (cupsLastError() != IPP_OK)
    NSRunAlertPanel(NSLocalizedString(@"Unable to send printer command!", NULL), @"%s", @"OK", nil, nil, cupsLastErrorString());

  // Remove the temporary file and return...
  unlink(filename);
}


//
// 'setPrinterId' - Set the printer that is associated with the supplies.
//

- (void)setPrinterId:(NSString *)printerId
{
  // Free any existing PPD...
  ppdClose(ppd_);
  ppd_ = NULL;

  // Generate the printer-uri and resource path for this printer...
  httpAssembleURIf(HTTP_URI_CODING_ALL, printerURI_, sizeof(printerURI_), "ipp", NULL, "localhost", 0, "/printers/%s", [printerId UTF8String]);
  snprintf(resource_, sizeof(resource_), "/printers/%s", [printerId UTF8String]);

  // Connect to the server as needed...
  if (!http_)
    http_ = httpConnectEncrypt(cupsServer(), ippPort(), cupsEncryption());

  if (!http_)
  {
    NSRunAlertPanel(NSLocalizedString(@"Unable to contact printing system!", NULL), @"%s", NSLocalizedString(@"OK", NULL), nil, nil, strerror(errno));
    return;
  }

  // Get the PPD for this printer...
  const char *filename = cupsGetPPD2(http_, [printerId UTF8String]);
  if (filename)
  {
    ppd_ = ppdOpenFile(filename);
    unlink(filename);
  }

#ifdef USE_GCD
  // Start a background thread that watches for printer state changes
  [self updateLevelsGCD];
#else
  if (!thread_)
  {
    thread_ = [[NSThread alloc] initWithTarget:self
                                selector:@selector(updateLevelsThread:)
                                object:nil];
    [thread_ start];
  }
#endif
}


//
// 'updateLevels' - Update ink levels for the queue.
//

- (void)updateLevels
{
  static const char * const attrs[] =
  {
    "marker-change-time",
    "marker-colors",
    "marker-high-levels",
    "marker-levels",
    "marker-low-levels",
    "marker-message",
    "marker-names",
    "marker-types",
    "printer-commands",
    "printer-state",
    "printer-state-reasons",
    "printer-type"
  };


  // Check that we have a printer...
  if (!resource_[0])
    return;

  // Create a Get-Printer-Attributes request for the printer
  ipp_t *request = ippNewRequest(IPP_GET_PRINTER_ATTRIBUTES);
  ippAddString(request, IPP_TAG_OPERATION, IPP_TAG_URI, "printer-uri", NULL, printerURI_);
  ippAddStrings(request, IPP_TAG_OPERATION, IPP_TAG_KEYWORD, "requested-attributes", (int)(sizeof(attrs) / sizeof(attrs[0])), NULL, attrs);

  // Send the request and get the printer attributes response...
  ipp_t *response = cupsDoRequest(http_, request, "/");

  // Get the current printer state and the last time the marker-* attributes
  // were updated.
  ipp_attribute_t *changed = ippFindAttribute(response, "marker-change-time", IPP_TAG_INTEGER);
  ipp_attribute_t *commands = ippFindAttribute(response, "printer-commands", IPP_TAG_KEYWORD);
  ipp_attribute_t *levels = ippFindAttribute(response, "marker-levels", IPP_TAG_INTEGER);
  ipp_attribute_t *message = ippFindAttribute(response, "marker-message", IPP_TAG_TEXT);
  ipp_attribute_t *reasons = ippFindAttribute(response, "printer-state-reasons", IPP_TAG_KEYWORD);
  ipp_attribute_t *state = ippFindAttribute(response, "printer-state", IPP_TAG_ENUM);
  ipp_attribute_t *type = ippFindAttribute(response, "printer-type", IPP_TAG_ENUM);

  int i, offline = 0, report_levels = 0;

  if (commands)
  {
    for (i = 0; i < commands->num_values; i ++)
    {
      if (!strcasecmp(commands->values[i].string.text, "ReportLevels"))
      {
        report_levels = 1;
    break;
      }
    }
  }

  if (reasons)
  {
    for (i = 0; i < reasons->num_values; i ++)
    {
      if (!strcmp(reasons->values[i].string.text, "offline-report"))
      {
        offline = 1;
    break;
      }
    }
  }

  // If the printer is idle, not offline, doesn't require authentication, we
  // don't have (recent) marker-levels, and the driver supports ReportLevels
  // commands, send a "ReportLevels" command file to the queue.
  if (state && state->values[0].integer == IPP_PRINTER_IDLE &&
      !offline &&
      type && !(type->values[0].integer & CUPS_PRINTER_AUTHENTICATED) &&
      (!levels ||
       (changed && (time(NULL) - changed->values[0].integer) > 43200)) &&
      report_levels)
  {
    [self sendCommand:"ReportLevels" withTitle:NSLocalizedString(@"Get Supply Levels", NULL)];
  }

  // Update the supplies view...
  if (levels)
  {
    int lines = levels->num_values;

    if (message && message->values[0].string.text[0])
      lines ++;

    ippDelete(data_);
    data_ = response;

    NSRect windowFrame = [[self window] frame];
    NSRect windowContent = [[self window] contentRectForFrameRect:windowFrame];
    NSSize windowSize = NSMakeSize(windowContent.size.width, 90 + SUPPLY_SPACING * lines);
    if (windowContent.size.height != windowSize.height)
      [[self window] setContentSize:windowSize];

    [self setNeedsDisplay:YES];
  }
  else
    ippDelete(response);
}


#if USE_GCD
//
// 'updateLevelsGCD' - Update ink levels for the queue incase there is any changes in the queue
//
- (void)updateLevelsGCD;
{
    int token = 0;
    dispatch_queue_t q = dispatch_queue_create("sample_supply_queue", NULL);

    void (^workBlock)(void) = ^{
        [self performSelectorOnMainThread:@selector(updateLevels) withObject:nil waitUntilDone:NO];
    };

    //  Start the initial work
    dispatch_async(q, workBlock);

    // wait for the printerHistoryChange to update the levels...
    notify_register_dispatch("com.apple.printerHistoryChange", &token, q, ^(int t) {
        workBlock();
    });
}
#else
//
// 'updateLevelsThread' - Update ink levels for the queue.
//

- (void)updateLevelsThread: (id)object
{
    // Watch for printer state changes...
    int fd, token;
    char data;
    ssize_t bytes;

    notify_register_file_descriptor("com.apple.printerHistoryChange", &fd, 0, &token);

    for (;;)
    {
        // Update the ink levels
        [self performSelectorOnMainThread:@selector(updateLevels) withObject:nil waitUntilDone:NO];

        // Read the next notification...
        if ((bytes = read(fd, &data, 1)) == 0)
            break;
        else if (bytes < 0 && errno != EAGAIN && errno != EINTR)
            break;
    }

    notify_cancel(token);

    [NSThread exit];
}
#endif


@end
```

[Next](sampletopdf.c.md)[Previous](SampleSuppliesView.h.md)

