---
title: SampleRaster
apple_id: DTS40009295
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: null
published: '2011-09-06'
source_url: https://developer.apple.com/library/archive/samplecode/SampleRaster/Listings/common_c.html
archived_at: '2026-07-18T03:23:03.935557Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SampleRaster](SampleRaster.md)


[Next](English.lproj-changingInk.html.md)[Previous](commandtosample.c.md)

# common.c

```c
/*
     File: common.c 
 Abstract: Common functions for sample CUPS printer driver. 
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

#include <stdarg.h>
#include "sample.h"         /* Common sample driver header */

/*
 * 'GetStatus()' - Read back-channel for status information.
 */

int                 /* O - 1 on success, 0 on failure */
GetStatus(ppd_file_t *ppd,      /* I - PPD file for printer */
          double     timeout)       /* I - Timeout in seconds */
{
  char      buffer[1025],       /* Buffer for back-channel data */
        *start,         /* Start of line */
        *end;           /* End of line */
  ssize_t   bytes;          /* Number of bytes read */
  static int    last_levels[4] = { -1, -1, -1, -1 };
                    /* Previous levels seen */


  if (timeout > 0.0)
  {
   /*
    * Send a "get levels" command to the printer...
    */

    puts("LEVELS");
    fflush(stdout);
  }

 /*
  * Read back-channel data from the backend with no timeout.
  */

  if ((bytes = cupsBackChannelRead(buffer, sizeof(buffer) - 1, timeout)) <= 0)
  {
   /*
    * No data...
    */

    return (timeout == 0.0 ? 1 : 0);
  }

 /*
  * Nul-terminate the buffer.
  */

  buffer[bytes] = '\0';

 /*
  * Parse the back-channel data.  For our imaginary sample device, it will
  * return one of the following strings on a line by itself:
  *
  * ILnnn,nnn,nnn,nnn      (ink levels)
  * OP                     (out of paper)
  * LP                     (low paper)
  * OK                     (no errors)
  *
  * Then we send ATTR: and STATE: messages to the scheduler.  See:
  *
  *     http://localhost:631/help/api-filter.html
  */

  for (start = buffer; *start; start = end)
  {
   /*
    * Find the end of the current line...
    */

    if ((end = strchr(start, '\n')) != NULL)
      *end++ = '\0';
    else
      end = start + strlen(start);

   /*
    * Parse this line...
    */

    if (!strncmp(start, "IL", 2))
    {
     /*
      * Collect ink levels...
      */

      int   levels[4];      /* Ink levels */


      if (sscanf(start, "IL%d,%d,%d,%d", levels + 0, levels + 1, levels + 2,
                 levels + 3) != 4)
        return (0);         /* Bad line */

     /*
      * Only report levels if they have changed...
      */

      if (levels[0] == last_levels[0] &&
          levels[1] == last_levels[1] &&
          levels[2] == last_levels[2] &&
          levels[3] == last_levels[3])
        continue;

     /*
      * Write an ATTR: message to stderr...
      */

      fprintf(stderr,
              "ATTR: marker-colors=#00ffff,#ff00ff,#ffff00,#000000 "
          "marker-levels=%d,%d,%d,%d "
          "marker-names=Cyan,Magenta,Yellow,Black "
          "marker-types=ink,ink,ink,ink\n",
          levels[0], levels[1], levels[2], levels[3]);

      if (levels[0] < 5 && last_levels[0] >= 5)
        fputs("STATE: +com.sample-cyan-error\n", stderr);
      else if (levels[0] >= 5 && last_levels[0] < 5)
        fputs("STATE: -com.sample-cyan-error\n", stderr);

      if (levels[1] < 5 && last_levels[1] >= 5)
        fputs("STATE: +com.sample-magenta-error\n", stderr);
      else if (levels[1] >= 5 && last_levels[1] < 5)
        fputs("STATE: -com.sample-magenta-error\n", stderr);

      if (levels[2] < 5 && last_levels[2] >= 5)
        fputs("STATE: +com.sample-yellow-error\n", stderr);
      else if (levels[2] >= 5 && last_levels[2] < 5)
        fputs("STATE: -com.sample-yellow-error\n", stderr);

      if (levels[3] < 5 && last_levels[3] >= 5)
        fputs("STATE: +com.sample-black-error\n", stderr);
      else if (levels[3] >= 5 && last_levels[3] < 5)
        fputs("STATE: -com.sample-black-error\n", stderr);

      last_levels[0] = levels[0];
      last_levels[1] = levels[1];
      last_levels[2] = levels[2];
      last_levels[3] = levels[3];
    }
    else if (!strcmp(start, "OP"))
    {
     /*
      * Write out-of-paper STATE: messages to stderr...
      */

      fputs("STATE: -media-low-report\n", stderr);
      fputs("STATE: +media-empty-warning\n", stderr);
    }
    else if (!strcmp(start, "LP"))
    {
     /*
      * Write low-paper STATE: messages to stderr...
      */

      fputs("STATE: -media-empty-warning\n", stderr);
      fputs("STATE: +media-low-report\n", stderr);
    }
    else if (!strcmp(start, "OK"))
    {
     /*
      * Write no-error STATE: messages to stderr...
      */

      fputs("STATE: -media-empty-warning\n", stderr);
      fputs("STATE: -media-low-report\n", stderr);
    }
    else
    {
      fprintf(stderr, "DEBUG: Unknown status \"%s\"!\n", start);
      return (0);
    }
  }

 /*
  * Return with no errors.
  */

  return (1);
}


/*
 * 'Initialize()' - Open the PPD file and parse options.
 */

ppd_file_t *                /* O - PPD file for printer */
Initialize(int        argc,     /* I - Number of command-line args */
           char       *argv[],      /* I - Command-line arguments */
           job_data_t *job)     /* O - Job data */
{
  ppd_file_t    *ppd;           /* PPD file for printer */


 /*
  * Validate the command-line arguments...
  */

  if (argc < 6 || argc > 7)
  {
    fprintf(stderr, "Usage: %s job user title copies options [filename]\n",
            argv[0]);
    return (NULL);
  }

 /*
  * Localize...
  */

  SetLocale();

 /*
  * Parse the options on the command-line...
  */

  job->job_id      = atoi(argv[1]);
  job->user        = argv[2];
  job->title       = argv[3];
  job->num_options = cupsParseOptions(argv[5], 0, &(job->options));

 /*
  * Open the PPD file...
  */

  if ((ppd = ppdOpenFile(getenv("PPD"))) != NULL)
  {
   /*
    * Mark the options for the job...
    */

    ppdMarkDefaults(ppd);
    cupsMarkOptions(ppd, job->num_options, job->options);
  }
  else
    LogMessage("ERROR", CFCopyLocalizedString(CFSTR("Unable to open PPD file: %s"), NULL), strerror(errno));

 /*
  * Return the PPD to the caller...
  */

  return (ppd);
}


/*
 * 'LogMessage()' - Write a localized message.
 */

void
LogMessage(const char  *prefix,     /* I - Prefix ("INFO", "ERROR", etc.) */
           CFStringRef format,      /* I - Format string */
       ...)             /* I - Additional arguments as needed */
{
  CFStringRef   formatted;      /* Formatted string */
  va_list   ap;         /* Pointer to additional arguments */
  char      buffer[2048];       /* Output buffer */


 /*
  * Format the message...
  */

  va_start(ap, format);

  if ((formatted = CFStringCreateWithFormatAndArguments(kCFAllocatorDefault, NULL, format, ap)) != NULL)
  {
    if (CFStringGetCString(formatted, buffer, sizeof(buffer), kCFStringEncodingUTF8))
      fprintf(stderr, "%s: %s\n", prefix, buffer);

    CFRelease(formatted);
  }

  va_end(ap);

 /*
  * Since we call this function with a copy of the localized string, release it
  * here so we don't leak memory for every LogMessage call...
  */

  CFRelease(format);
}


/*
 * 'SetLocale()' - Initialize bundle and POSIX localization.
 */

void
SetLocale(void)
{
  const char    *apple_language;    /* APPLE_LANGUAGE environment variable */
  CFStringRef   language;       /* Language string */
  CFArrayRef    languageArray;      /* Language array */


 /*
  * Turn off buffering of stderr...
  */

  setbuf(stderr, NULL);

 /*
  * Setup the Core Foundation language environment for localized messages.
  */

  if ((apple_language = getenv("APPLE_LANGUAGE")) == NULL)
    apple_language = getenv("LANG");

  if (apple_language)
  {
    language      = CFStringCreateWithCString(kCFAllocatorDefault, apple_language, kCFStringEncodingUTF8);
    languageArray = CFArrayCreate(kCFAllocatorDefault, (const void **)&language, 1, &kCFTypeArrayCallBacks);

    CFPreferencesSetValue(CFSTR("AppleLanguages"), languageArray, kCFPreferencesCurrentApplication, kCFPreferencesAnyUser, kCFPreferencesAnyHost);
    setlocale(LC_MESSAGES, "");

    CFRelease(language);
    CFRelease(languageArray);
  }
}
```

[Next](English.lproj-changingInk.html.md)[Previous](commandtosample.c.md)

