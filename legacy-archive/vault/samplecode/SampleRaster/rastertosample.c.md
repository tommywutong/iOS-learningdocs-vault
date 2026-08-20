---
title: SampleRaster
apple_id: DTS40009295
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: null
published: '2011-09-06'
source_url: https://developer.apple.com/library/archive/samplecode/SampleRaster/Listings/rastertosample_c.html
archived_at: '2026-07-18T03:23:04.056064Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SampleRaster](SampleRaster.md)


[Next](sample.h.md)[Previous](English.lproj-SampleRasterHelp.html.md)

# rastertosample.c

```c
/*
     File: rastertosample.c 
 Abstract: Sample CUPS printer driver raster filter for CUPS.

This filter produces a stream of grayscale or RGB pages and demonstrates
how to send device commands to get the current supply levels, control per-
page settings, and so forth. 
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

#include "sample.h"         /* Common sample driver header */
#include <cups/raster.h>        /* CUPS raster header */
#include <signal.h>


/*
 * Local globals...
 */

static int  CancelJob = 0;      /* Set to 1 when we need to cancel the current job */


/*
 * Local functions...
 */

static int  Setup(ppd_file_t *ppd, job_data_t *job);
static int  StartPage(ppd_file_t *ppd, job_data_t *job, cups_page_header2_t *header);
static int  OutputLine(ppd_file_t *ppd, cups_page_header2_t *header, unsigned char *line);
static int  EndPage(ppd_file_t *ppd, job_data_t *job, cups_page_header2_t *header);
static int  Shutdown(ppd_file_t *ppd, job_data_t *job);
static void SignalHandler(int sig);


/*
 * 'main()' - Main entry for filter.
 */

int                 /* O - Exit status */
main(int  argc,             /* I - Number of command-line args */
     char *argv[])          /* I - Command-line arguments */
{
  ppd_file_t        *ppd;       /* PPD file for printer */
  job_data_t        job;        /* Job data */
  int           page = 0;   /* Current page number */
  int           fd;     /* File descriptor for raster data */
  cups_raster_t     *ras;       /* Raster stream */
  cups_page_header2_t   header;     /* Current page header */
  unsigned      y;      /* Current line */
  unsigned char     *line;      /* Line buffer */


 /*
  * Do common driver initialization stuff.
  */

  if ((ppd = Initialize(argc, argv, &job)) == NULL)
    return (1);

 /*
  * Register a signal handler...
  */

  signal(SIGTERM, SignalHandler);

 /*
  * Prepare the print job.
  */

  if (!Setup(ppd, &job))
    return (1);

 /*
  * Open the raster stream.
  */

  if (argc == 7)
  {
    if ((fd = open(argv[6], O_RDONLY)) == -1)
    {
      LogMessage("ERROR", CFCopyLocalizedString(CFSTR("Unable to open raster file - %s"), NULL), strerror(errno));
      return (1);
    }
  }
  else
    fd = 0;

  ras = cupsRasterOpen(fd, CUPS_RASTER_READ);

 /*
  * Process pages as needed...
  */

  while (cupsRasterReadHeader2(ras, &header))
  {
   /*
    * Check for canceled jobs...
    */

    if (CancelJob)
      break;

   /*
    * Allocate memory for the line...
    */

    fprintf(stderr, "DEBUG: cupsBytesPerLine=%u\n", header.cupsBytesPerLine);

    if ((line = malloc(header.cupsBytesPerLine)) == NULL)
    {
      LogMessage("ERROR", CFCopyLocalizedString(CFSTR("Unable to allocate %u bytes!"), NULL), header.cupsBytesPerLine);
      break;
    }

   /*
    * Let the scheduler and user know we are printing a page...
    */

    page ++;

    fprintf(stderr, "PAGE: %d %d\n", page, header.NumCopies);
    LogMessage("INFO", CFCopyLocalizedString(CFSTR("Starting page %d..."), NULL), page);

    if (!StartPage(ppd, &job, &header))
      break;

   /*
    * Print every line on the page...
    */

    for (y = 0; y < header.cupsHeight; y ++)
    {
     /*
      * Check for canceled jobs...
      */

      if (CancelJob)
    break;

     /*
      * Show progress...
      */

      if ((y & 127) == 0)
      {
        LogMessage("INFO", CFCopyLocalizedString(CFSTR("Printing page %d, %.0f%% complete..."), NULL), page, 100.0 * y / header.cupsHeight);

        puts("LEVELS");
    fflush(stdout);
      }

     /*
      * Check for status messages from the device...
      */

      GetStatus(ppd, 0.0);

     /*
      * Read the line and write it out...
      */

      if (cupsRasterReadPixels(ras, line, header.cupsBytesPerLine) > 0)
      {
        if (!OutputLine(ppd, &header, line))
      break;
      }
      else
        break;
    }

   /*
    * Release the line buffer...
    */

    free(line);

   /*
    * Show progress and end the current page...
    */

    LogMessage("INFO", CFCopyLocalizedString(CFSTR("Finished page %d..."), NULL), page);

    if (!EndPage(ppd, &job, &header))
      break;
  }

 /*
  * Check for status messages from the device...
  */

  GetStatus(ppd, 1.0);

 /*
  * End the job on the printer...
  */

  Shutdown(ppd, &job);

 /*
  * Show final status...
  */

  if (page == 0)
  {
    LogMessage("ERROR", CFCopyLocalizedString(CFSTR("No pages found!"), NULL));
    return (1);
  }
  else
  {
    LogMessage("INFO", CFCopyLocalizedString(CFSTR("Ready to print."), NULL));
    return (0);
  }
}


/*
 * 'Setup()' - Setup the printer for the print job.
 */

static int              /* O - 1 on success, 0 on failure */
Setup(ppd_file_t *ppd,          /* I - PPD file for printer */
      job_data_t *job)          /* I - Job data */
{
 /*
  * Send any job setup commands to the printer.
  */

  puts("DOCUMENT");
  printf("AUTHOR %s\n", job->user);
  printf("TITLE %s\n", job->title);

  return (1);
}


/*
 * 'StartPage()' - Start a page on the printer.
 */

static int              /* O - 1 on success, 0 on failure */
StartPage(
    ppd_file_t          *ppd,       /* I - PPD file for printer */
    job_data_t          *job,       /* I - Job data */
    cups_page_header2_t *header)    /* I - Page header */
{
 /*
  * Validate the raster data...
  */

  if (header->cupsBitsPerColor != 8 && header->cupsBitsPerColor != 16)
  {
    LogMessage("ERROR", CFCopyLocalizedString(CFSTR("Bad cupsBitsPerColor=%u!"), NULL), header->cupsBitsPerColor);
    return (0);
  }
  else if (header->cupsColorOrder != CUPS_ORDER_CHUNKED)
  {
    LogMessage("ERROR", CFCopyLocalizedString(CFSTR("Bad cupsColorOrder=%u!"), NULL), header->cupsColorOrder);
    return (0);
  }
  else if (header->cupsColorSpace != CUPS_CSPACE_W &&
           header->cupsColorSpace != CUPS_CSPACE_RGB)
  {
    LogMessage("ERROR", CFCopyLocalizedString(CFSTR("Bad cupsColorSpace=%u!"), NULL), header->cupsColorSpace);
    return (0);
  }

 /*
  * Send any page setup commands to the printer.
  */

  printf("PAGE %u %u %u %u\n", header->Margins[0], header->Margins[1], header->PageSize[0], header->PageSize[1]);
  printf("RASTER %u %u %u\n", header->cupsWidth, header->cupsHeight, header->cupsNumColors);

  return (1);
}


/*
 * 'OutputLine()' - Output a single line of raster data.
 */

static int              /* O - 1 on success, 0 on failure */
OutputLine(
    ppd_file_t          *ppd,       /* I - PPD file for printer */
    cups_page_header2_t *header,    /* I - Page header */
    unsigned char       *line)      /* I - Raster data */
{
 /*
  * Send a line of raster data to the printer.
  */

  if (header->cupsBitsPerColor == 8)
  {
   /*
    * Send 8-bit data to the printer...
    */

    printf("LINE %d\n", header->cupsBytesPerLine);

    return (fwrite(line, 1, header->cupsBytesPerLine, stdout) == header->cupsBytesPerLine);
  }
  else
  {
   /*
    * Send 16-bit data to the printer.  Ordinarily you'd be dithering the
    * print data, but here we just need to convert the 48-bit RGB data to
    * 24-bits.
    *
    * This formula:
    *
    *     (*pixel + 129) / 257
    *
    * rounds the 16-bit pixel to the nearest 8-bit value ("+ 129") and
    * converts from 16-bits to 8-bits (65535 / 255 = 257).
    */

    unsigned short  *pixel;     /* Current pixel */
    int         count;      /* Remaining count */

    printf("LINE %d\n", header->cupsBytesPerLine / 2);

    for (pixel = (unsigned short *)line, count = header->cupsBytesPerLine / 2;
         count > 0;
     count --, pixel ++)
      if (putchar((*pixel + 129) / 257) == EOF)
        return (0);

    return (1);
  }
}


/*
 * 'EndPage()' - End the current page on the printer.
 */

static int
EndPage(
    ppd_file_t          *ppd,       /* I - PPD file for printer */
    job_data_t          *job,       /* I - Job data */
    cups_page_header2_t *header)    /* I - Page header */
{
 /*
  * Send end-of-page commands to the printer.
  */

  puts("ENDPAGE");

  return (1);
}


/*
 * 'Shutdown()' - Finish the current job on the printer.
 */

static int              /* O - 1 on success, 0 on failure */
Shutdown(
    ppd_file_t *ppd,            /* I - PPD file for printer */
    job_data_t *job)            /* I - Job data */
{
 /*
  * Send end-of-job commands to the printer.
  */

  puts("ENDDOCUMENT");

  return (1);
}


/*
 * 'SignalHandler()' - Catch SIGTERM and flag that we need to cancel the job.
 */

static void
SignalHandler(int sig)          /* I - Signal number (unused) */
{
 /*
  * Tell the main loop to cancel the job.
  */

  CancelJob = 1;
}
```

[Next](sample.h.md)[Previous](English.lproj-SampleRasterHelp.html.md)

