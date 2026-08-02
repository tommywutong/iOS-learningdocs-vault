---
title: SampleRaster
apple_id: DTS40009295
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: null
published: '2011-09-06'
source_url: https://developer.apple.com/library/archive/samplecode/SampleRaster/Listings/sampletopdf_c.html
archived_at: '2026-07-18T03:23:04.254131Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SampleRaster](SampleRaster.md)


[Next](SampleUtility.m.md)[Previous](SampleSuppliesView.m.md)

# sampletopdf.c

```c
/*
     File: sampletopdf.c 
 Abstract: Sample driver to PDF test backend for CUPS.

MOST PRINTER DRIVERS DO NOT REQUIRE A BACKEND.  DO NOT USE THIS CODE IN A
PRODUCTION PRINTER DRIVER.  This backend is provided for testing/
experimentation with the "Sample Raster Printer" example raster printer
driver for CUPS. 
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

#include <ApplicationServices/ApplicationServices.h>
#include <CoreFoundation/CoreFoundation.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include "sample.h"
#include <cups/backend.h>


/*
 * Local functions...
 */

static void free_data(void *info, const void *data, size_t size);
static void load_levels(int cmyk[4]);
static void save_levels(int cmyk[4]);
static void update_ink_levels(int cmyk[4], unsigned char *line, int bytes,
                          int depth, int resolution);


/*
 * 'main()' - Read sample raster data and write a PDF file.
 */

int                 /* O - Exit status */
main(int  argc,             /* I - Number of command-line arguments */
     char *argv[])          /* I - Command-line arguments */
{
  int       document;       /* Looping var */
  CGContextRef  context;        /* PDF context */
  char      basename[1024],     /* Base filename */
        *baseptr,       /* Pointer into base filename */
        filename[1024],     /* Actual filename */
        line[1024],     /* Line from file */
        *value;         /* Value from line */
  int       linenum;        /* Current line number */
  CGRect    page_box;       /* Box for page size */
  unsigned  raster_width,       /* Width of page image */
        raster_height,      /* Height of page image */
        raster_depth,       /* Depth of page image - 1 (grayscale) or 3 (RGB) */
        raster_size;        /* Total size of page image */
  int       resolution;     /* Computed resolution */
  unsigned char *raster_data,       /* Page buffer */
        *raster_ptr,        /* Pointer into page buffer */
        *raster_end;        /* Pointer to end of page buffer */
  int       cmyk[4];        /* CMYK "ink" levels */
  CFStringRef   cf_filename;        /* CoreFoundation filename */
  CFURLRef  cf_fileurl;     /* CoreFoundation file URL */
  cups_file_t   *fp;            /* Input file */


 /*
  * Localize...
  */

  SetLocale();

 /*
  * Validate command-line...
  */

  if (argc == 1)
  {
   /*
    * List devices...
    */

    puts("direct sampletopdf://Acme/Sample%20Raster \"Acme Sample Raster\" \"Sample Raster Driver\" \"MFG:Acme;MODEL:Sample Raster;\"");

    return (CUPS_BACKEND_OK);
  }
  else if (argc < 6 || argc > 7)
  {
   /*
    * Bad invocation...
    */

    fputs("Usage: sampletopdf job user title copies options [filename]\n",
          stderr);
    return (CUPS_BACKEND_STOP);
  }
  else if (argc == 6)
    fp = cupsFileStdin();
  else if ((fp = cupsFileOpen(argv[6], "r")) == NULL)
  {
    LogMessage("ERROR", CFCopyLocalizedString(CFSTR("Unable to open print file - %s"), NULL), strerror(errno));
    return (CUPS_BACKEND_STOP);
  }

 /*
  * Prepare base output filename using job ID (argv[1]) and title (argv[3])...
  */

  snprintf(basename, sizeof(basename), "%s - %s", argv[1], argv[3]);
  for (baseptr = basename; *baseptr; baseptr ++)
    if ((!(*baseptr & 0x80) && *baseptr < ' ') || *baseptr == '/' ||
        *baseptr == 0x7f)
      *baseptr = '_';

 /*
  * Prepare a directory to hold the files...
  */

  snprintf(filename, sizeof(filename), "/Library/Caches/%s", getenv("PRINTER"));
  mkdir(filename, 0755);
  chmod(filename, 0755);

 /*
  * Read lines from file until we see end-of-file...
  */

  context     = NULL;
  linenum     = 0;
  document    = 0;
  raster_data = NULL;
  resolution  = 100;

  page_box.origin.x = page_box.origin.y = page_box.size.width = page_box.size.height = 0.0;

  load_levels(cmyk);

  while (cupsFileGetConf(fp, line, sizeof(line), &value, &linenum))
  {
    if (!strcmp(line, "DOCUMENT"))
    {
      if (context)
      {
    CGContextRelease(context);
    context = NULL;
      }

      document ++;
      snprintf(filename, sizeof(filename), "/Library/Caches/%s/%s%d.pdf", getenv("PRINTER"), basename, document);
      cf_filename = CFStringCreateWithCString(kCFAllocatorDefault, filename, kCFStringEncodingUTF8);

      if (cf_filename)
      {
        cf_fileurl = CFURLCreateWithFileSystemPath(kCFAllocatorDefault, cf_filename, kCFURLPOSIXPathStyle, false);

        if (cf_fileurl)
    {
      context = CGPDFContextCreateWithURL(cf_fileurl, NULL, NULL);
          CFRelease(cf_fileurl);
    }

        CFRelease(cf_filename);

        chmod(filename, 0644);
    fprintf(stderr, "DEBUG: Writing \"%s\"...\n", filename);
      }
    }
    else if (!strcmp(line, "ENDDOCUMENT"))
    {
      if (context)
      {
    CGContextRelease(context);
    context = NULL;
      }
    }
    else if (!strcmp(line, "PAGE") && value && context)
    {
      unsigned  rect[4];        /* Rectangle for page */


     /*
      * Since CGFloat is double for 64-bit builds and float for 32-bit builds,
      * we can't use a simple sscanf to read the page rectangle.  Instead, we'll
      * read the rectangle into unsigned integers (that's the form sent by our
      * rastertosample filter) and then copy to the CGRect...
      */

      if (sscanf(value, "%u%u%u%u", rect + 0, rect + 1, rect + 2, rect + 3) == 4)
      {
        page_box.origin.x    = rect[0];
    page_box.origin.y    = rect[1];
    page_box.size.width  = rect[2];
    page_box.size.height = rect[3];

        fprintf(stderr, "DEBUG: Starting page - [%g %g %g %g]...\n",
            page_box.origin.x, page_box.origin.y,
        page_box.size.width, page_box.size.height);
    CGContextBeginPage(context, &page_box);
      }
    }
    else if (!strcmp(line, "ENDPAGE") && context)
    {
      if (raster_data)
      {
    CFStringRef colorSpaceName = NULL;
    if (raster_depth == 1)
    {
          // kCGColorSpaceGenericGrayGamma2_2 doesn't exist in all versions of Mac OS X
          if (&kCGColorSpaceGenericGrayGamma2_2 != NULL)
            colorSpaceName = kCGColorSpaceGenericGrayGamma2_2;
          else
            colorSpaceName = kCGColorSpaceGenericGray;
        }
    else
    {
          // kCGColorSpaceSRGB doesn't exist in all versions of Mac OS X
          if (&kCGColorSpaceSRGB != NULL)
            colorSpaceName = kCGColorSpaceSRGB;
          else
            colorSpaceName = kCGColorSpaceGenericRGB;
        }

    CGColorSpaceRef colorspace = CGColorSpaceCreateWithName(colorSpaceName);
    CGDataProviderRef provider = CGDataProviderCreateWithData(NULL, raster_data, raster_size, free_data);
    CGImageRef image = CGImageCreate(raster_width, raster_height, 8, raster_depth * 8, raster_width * raster_depth, colorspace, kCGImageAlphaNone, provider, NULL, false, kCGRenderingIntentDefault);

    CGContextDrawImage(context, page_box, image);

        fputs("DEBUG: Drawing image on page...\n", stderr);

    CGImageRelease(image);
    CGDataProviderRelease(provider);
    CGColorSpaceRelease(colorspace);
      }

      fputs("DEBUG: Ending page...\n", stderr);

      CGPDFContextEndPage(context);
    }
    else if (!strcmp(line, "RASTER") && value && !raster_data && page_box.size.width > 0.0 && page_box.size.height > 0.0)
    {
     /*
      * Get raster dimensions and depth...
      */

      if (sscanf(value, "%u%u%u", &raster_width, &raster_height,
                 &raster_depth) == 3)
      {
        if ((raster_depth == 1 || raster_depth == 3) &&
        raster_width > 0 && raster_width <= 3600 &&
        raster_height > 0 && raster_height <= 5400)
    {
     /*
      * Allocate memory for up to 12x18" page at 300 DPI.
      */

          raster_size = raster_width * raster_height * raster_depth;
          raster_data = malloc(raster_size);
      raster_ptr  = raster_data;
      raster_end  = raster_data + raster_size;
      resolution  = (int)(raster_width * 72.0 / page_box.size.width);

         /*
      * Clear the page to white...
      */

      memset(raster_data, 255, raster_size);
    }
      }
    }
    else if (!strcmp(line, "LINE") && value && raster_data)
    {
      size_t bytes = strtol(value, NULL, 10);

      if ((raster_ptr + bytes) > raster_end)
      {
       /*
        * Raster data too long!
    */

        cupsFileRead(fp, (char *)raster_ptr, raster_end - raster_ptr);

        for (bytes -= raster_end - raster_ptr; bytes > 0; bytes --)
      cupsFileGetChar(fp);

    bytes = raster_end - raster_ptr;
      }
      else
        cupsFileRead(fp, (char *)raster_ptr, bytes);

     /*
      * Update ink usage counters.  Normally you'd get this information
      * from the printer itself, but since we are simulating the printer
      * we also have to simulate the ink usage counters and the affect on
      * the printed output.
      */

      update_ink_levels(cmyk, raster_ptr, bytes, raster_depth, resolution);

     /*
      * Advance to the next line...
      */

      raster_ptr += bytes;
    }
    else if (!strcmp(line, "LEVELS"))
    {
     /*
      * Report levels...
      */

      char  levels[255];        /* Ink levels */

      snprintf(levels, sizeof(levels), "IL%d,%d,%d,%d\n", cmyk[0] / 10000, cmyk[1] / 10000, cmyk[2] / 10000, cmyk[3] / 10000);
      cupsBackChannelWrite(levels, strlen(levels), 1.0);
    }
    else if (!strcmp(line, "CHANGEINK"))
    {
     /*
      * "Change" ink...
      */

      cmyk[0] = cmyk[1] = cmyk[2] = cmyk[3] = 1000000;
    }
  }

  if (context)
  {
    CGPDFContextClose(context);
    CGContextRelease(context);
    context = NULL;
  }

  save_levels(cmyk);

  return (CUPS_BACKEND_OK);
}


/*
 * 'free_data()' - Free bitmap data when CG is done using it.
 */

static void
free_data(void       *info,     /* I - Context pointer (unused) */
          const void *data,     /* I - Pointer to data */
      size_t     size)      /* I - Size of data buffer (unused) */
{
  (void)info;
  (void)size;

  free((void *)data);
}


/*
 * 'load_levels()' - Load the CMYK ink levels from the cache file.
 */

static void
load_levels(int cmyk[4])        /* O - CMYK levels */
{
  cups_file_t   *fp;            /* File to read from */
  char      filename[1024],     /* Cache filename */
        line[1024];     /* Line from file */


  cmyk[0] = cmyk[1] = cmyk[2] = cmyk[3] = 1000000;

  snprintf(filename, sizeof(filename), "/Library/Caches/%s.cmyk", getenv("PRINTER"));

  if ((fp = cupsFileOpen(filename, "r")) != NULL)
  {
    if (cupsFileGets(fp, line, sizeof(line)))
      sscanf(line, "%d%d%d%d", cmyk + 0, cmyk + 1, cmyk + 2, cmyk + 3);

    cupsFileClose(fp);
  }
}


/*
 * 'save_levels()' - Save the CMYK ink levels to the cache file.
 */

static void
save_levels(int cmyk[4])        /* I - CMYK levels */
{
  cups_file_t   *fp;            /* File to write to */
  char      filename[1024];     /* Cache filename */


  snprintf(filename, sizeof(filename), "/Library/Caches/%s.cmyk", getenv("PRINTER"));

  if ((fp = cupsFileOpen(filename, "w")) != NULL)
  {
    cupsFilePrintf(fp, "%d %d %d %d\n", cmyk[0], cmyk[1], cmyk[2], cmyk[3]);
    cupsFileClose(fp);
    chmod(filename, 0644);
  }
}


/*
 * 'update_ink_levels()' - Update the virtual CMYK ink levels based on a line
 *                         from the page.
 */

static void
update_ink_levels(
    int           cmyk[4],      /* IO - CMYK levels */
    unsigned char *line,        /* I  - Pixels on the current line */
    int           bytes,        /* I  - Number of bytes */
    int           depth,        /* I  - Bytes per pixel */
    int           resolution)       /* I  - Output resolution */
{
  int c = 0, m = 0, y = 0, k = 0;   /* Total CMYK on the line */


  if (depth == 1)
  {
   /*
    * Update black ink usage for grayscale output...
    */

    if (cmyk[3] <= 0)
    {
     /*
      * Simulate out-of-ink condition by removing black...
      */

      memset(line, 255, bytes);
    }
    else
    {
     /*
      * Otherwise count the amount of black ink used...
      */

      while (bytes > 0)
      {
    k += 255 - *line;

    bytes --;
    line ++;
      }
    }
  }
  else if (cmyk[0] <= 0 && cmyk[1] <= 0 && cmyk[2] <= 0 && cmyk[3] <= 0)
  {
   /*
    * Completely out of ink, blank the line to simulate that...
    */

    memset(line, 255, bytes);
  }
  else
  {
   /*
    * Update CMYK ink usage for color output...
    */

    int kmin, kmax;

    while (bytes > 0)
    {
     /*
      * NOTE: Real printers need more complex code than this!
      *
      * The classic RGB to CMYK formula calculates K using the maximum
      * RGB value, and then subtracts it from the C, M, and Y values:
      *
      *    K = 1 - max(R,G,B)
      *    C = 1 - R - K
      *    M = 1 - G - K
      *    Y = 1 - B - K
      *
      * Colors tend to look "flat" with this simple formula, so instead we
      * use a formula that calculates black based on both the minimum and
      * maximum RGB values so that the amount of black depends not only on
      * the darkness of the color but how colorful it is.  Less colorful
      * colors use more black:
      *
      *         (1 - max(R,G,B))^3
      *     K = ------------------
      *         (1 - min(R,G,B))^2
      *
      *     C = 1 - R - K
      *     M = 1 - G - K
      *     Y = 1 - B - K
      */

      kmin = line[0] > line[1] ?
         (line[0] > line[2] ? line[0] : line[2]) :
         (line[1] > line[2] ? line[1] : line[2]);
      kmax = line[0] < line[1] ?
         (line[0] < line[2] ? line[0] : line[2]) :
         (line[1] < line[2] ? line[1] : line[2]);
      if (kmax > kmin)
      {
    kmin = 255 - kmin;
    kmax = 255 - kmax;
    kmin = 255 - kmin * kmin * kmin / (kmax * kmax);
      }

     /*
      * Add the current CMYK values to our color counters for the line.
      */

      c += kmin - line[0];
      m += kmin - line[1];
      y += kmin - line[2];
      k += 255 - kmin;

      if (cmyk[0] <= 0)
      {
       /*
    * Simulate out-of-cyan-ink condition by removing cyan...
    */

    line[0] = kmin;
      }

      if (cmyk[1] <= 0)
      {
       /*
    * Simulate out-of-magenta-ink condition by removing magenta...
    */

    line[1] = kmin;
      }

      if (cmyk[2] <= 0)
      {
       /*
    * Simulate out-of-yellow-ink condition by removing yellow...
    */

    line[2] = kmin;
      }

      if (cmyk[3] <= 0)
      {
       /*
    * Simulate out-of-black-ink condition by removing black...
    */

    kmin = 255 - kmin;
    line[0] += kmin;
    line[1] += kmin;
    line[2] += kmin;
      }

      bytes -= 3;
      line += 3;
    }
  }

 /*
  * Subtract a portion of the CMYK colors used on this line from the
  * ink counters, then limit to a minimum of 0 ink left.
  */

  cmyk[0] -= 50 * c / resolution / resolution;
  cmyk[1] -= 50 * m / resolution / resolution;
  cmyk[2] -= 50 * y / resolution / resolution;
  cmyk[3] -= 50 * k / resolution / resolution;

  if (cmyk[0] < 0)
    cmyk[0] = 0;
  if (cmyk[1] < 0)
    cmyk[1] = 0;
  if (cmyk[2] < 0)
    cmyk[2] = 0;
  if (cmyk[3] < 0)
    cmyk[3] = 0;
}
```

[Next](SampleUtility.m.md)[Previous](SampleSuppliesView.m.md)

