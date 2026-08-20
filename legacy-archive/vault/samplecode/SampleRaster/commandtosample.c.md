---
title: SampleRaster
apple_id: DTS40009295
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: null
published: '2011-09-06'
source_url: https://developer.apple.com/library/archive/samplecode/SampleRaster/Listings/commandtosample_c.html
archived_at: '2026-07-18T03:23:03.850154Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SampleRaster](SampleRaster.md)


[Next](common.c.md)[Previous](README.txt.md)

# commandtosample.c

```c
/*
     File: commandtosample.c 
 Abstract: Sample CUPS printer driver command filter. 
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
#include <cups/cups.h>          /* CUPS API headers */

/*
 * Local functions...
 */

static void print_self_test_page(const char *user);


/*
 * 'main()' - Main entry for filter.
 */

int                 /* O - Exit status */
main(int  argc,             /* I - Number of command-line args */
     char *argv[])          /* I - Command-line arguments */
{
  ppd_file_t    *ppd;           /* PPD file for printer */
  job_data_t    job;            /* Job data */
  cups_file_t   *fp;            /* Command file */
  char      line[1024],     /* Line from file */
        *value;         /* Pointer to value on line */
  int       linenum;        /* Current line number */


 /*
  * Do common driver initialization stuff.
  */

  if ((ppd = Initialize(argc, argv, &job)) == NULL)
    return (1);

 /*
  * Open the command file as needed...
  */

  if (argc == 7)
  {
    if ((fp = cupsFileOpen(argv[6], "r")) == NULL)
    {
      LogMessage("ERROR", CFCopyLocalizedString(CFSTR("Unable to open command file: %s"), NULL), strerror(errno));
      return (1);
    }
  }
  else
    fp = cupsFileStdin();

 /*
  * Read the commands from the file and send the appropriate printer commands...
  *
  * The CUPS command file format is documented here:
  *
  *     http://localhost:631/help/spec-command.html
  */

  linenum = 0;

  while (cupsFileGetConf(fp, line, sizeof(line), &value, &linenum))
  {
   /*
    * Parse the command...
    */

    if (!strcasecmp(line, "ChangeInk"))
    {
     /*
      * Change ink...
      */

      printf("CHANGEINK %s\n", value);
      puts("LEVELS");
      fflush(stdout);

      GetStatus(ppd, 5.0);
    }
    else if (!strcasecmp(line, "Clean"))
    {
     /*
      * Clean heads...
      */

      printf("CLEAN %s\n", value);
    }
    else if (!strcasecmp(line, "PrintSelfTestPage"))
    {
     /*
      * Print a self-test page.
      */

      print_self_test_page(argv[2]);
    }
    else if (!strcasecmp(line, "ReportLevels"))
    {
     /*
      * Report the supply/ink levels...
      */

      puts("LEVELS");
      fflush(stdout);

      GetStatus(ppd, 5.0);
    }
    else
      LogMessage("ERROR", CFCopyLocalizedString(CFSTR("Unknown printer command \"%s\"!"), NULL), line);
  }

  return (0);
}


/*
 * 'print_self_test_page()' - Print a self-test page.
 */

static void
print_self_test_page(const char *user)  /* I - User that requested page */
{
  int       y,          /* Current line */
        color,          /* Current color */
        pass;           /* Current pass */
  unsigned char data[360 * 3],      /* Data for line */
        *dataptr;       /* Pointer into line */
  unsigned char colors[4][3] =      /* Colors for each "ink" */
        {
          { 0, 0, 0 },      /* Black */
          { 0, 255, 255 },  /* Cyan */
          { 255, 0, 255 },  /* Magenta */
          { 255, 255, 0 }   /* Yellow */
        };


 /*
  * The self-test page prints a common head test pattern for each color like
  * this:
  *
  * |----            |
  * |    ----        |
  * |        ----    |
  * |            ----|
  * |----            |
  * |    ----        |
  * |        ----    |
  * |            ----|
  */

  puts("DOCUMENT");
  printf("AUTHOR %s\n", user);
  puts("TITLE Self-Test Page");

  puts("PAGE 0 0 360 72");      /* 5x1" test page */
  puts("RASTER 360 72 3");      /* 72dpi color image */

  for (y = 0; y < 72; y ++)
  {
   /*
    * Clear the line...
    */

    memset(data, 255, sizeof(data));

   /*
    * Add each color...
    */

    for (color = 0, pass = y & 7; color < 4; color ++)
    {
      dataptr = data + color * 96 * 3;

      memcpy(dataptr + 0 * 3, colors[color], 3);
      memcpy(dataptr + 71 * 3, colors[color], 3);

      dataptr += pass * 9 * 3;
      memcpy(dataptr + 0 * 3, colors[color], 3);
      memcpy(dataptr + 1 * 3, colors[color], 3);
      memcpy(dataptr + 2 * 3, colors[color], 3);
      memcpy(dataptr + 3 * 3, colors[color], 3);
      memcpy(dataptr + 4 * 3, colors[color], 3);
      memcpy(dataptr + 5 * 3, colors[color], 3);
      memcpy(dataptr + 6 * 3, colors[color], 3);
      memcpy(dataptr + 7 * 3, colors[color], 3);
      memcpy(dataptr + 8 * 3, colors[color], 3);
    }

   /*
    * Write the line...
    */

    printf("LINE %d\n", (int)sizeof(data));
    fwrite(data, 1, sizeof(data), stdout);
  }

  puts("ENDPAGE");
  puts("ENDDOCUMENT");

 /*
  * Log that we printed a page!
  */

  fputs("PAGE: 1 1\n", stderr);
}
```

[Next](common.c.md)[Previous](README.txt.md)

