---
title: OTSimpleDownloadHTTP
apple_id: DTS10000710
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/OTSimpleDownloadHTTP/Listings/OTSimpleDownloadHTTP_h.html
archived_at: '2026-07-18T03:17:20.122020Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OTSimpleDownloadHTTP](OTSimpleDownloadHTTP.md)


[Next](OTSimpleDownloadHTTPTest.c.md)[Previous](OTSimpleDownloadHTTP.c.md)

# OTSimpleDownloadHTTP.h

```
/*
    File:       OTSimpleDownloadHTTP.h

    Contains:   Interface to the simple HTTP download sample.

    Written by: Quinn "The Eskimo!" 

    Copyright:  Copyright © 1997-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                7/23/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/
#if defined(__MWERKS__)
#   include <carbon.h>
#   include <Types.h>
#   include <SIOUX.h>
#else
#   include <CoreServices/CoreServices.h>
#endif


/////////////////////////////////////////////////////////////////////
// More Assert replaces OTAssert in carbonized code because OTAssert 
// does not exist
    //
    //  We usually want asserions and other debugging code
    //  turned on, but you can turn it all off if you like
    //  by setting MORE_DEBUG to 0.
    //

#ifndef MORE_DEBUG
#   define MORE_DEBUG 1
#endif

    //
    //  Our assertion macros compile down to nothing if
    //  MORE_DEBUG is not true. MoreAssert produces a
    //  value indicating whether the assertion succeeded
    //  or failed. MoreAssertQ is Quinn's flavor of
    //  MoreAssert which does not produce a value.
    //

#if MORE_DEBUG
#   define MoreAssert(x) \
        ((x) ? true : (DebugStr ("\pMoreAssert failure: " #x), false))
#   define MoreAssertQ(x) \
        do { if (!(x)) DebugStr ("\pMoreAssertQ failure: " #x); } while (false)
#else
#   define MoreAssert(x) (true)
#   define MoreAssertQ(x)
#endif
/////////////////////////////////////////////////////////////////////



OSStatus DownloadHTTPSimple(const char *hostName,
                            const char *httpCommand,
                            const short destFileRefNum);

// Download a URL from the a web server.  hostName is a pointer
// to a string that contains the DNS address of the web server.
// The DNS address must be suffixed by ":<port>", where <port>
// is the port number the web server is operating on.
// httpCommand contains the HTTP command to send.  Typically this
// is of the form:
//
//      GET <x> HTTP/1.0\0x13\0x10\0x13\0x10
//
// where <x> is the URL path.  destFileRefNum is the file
// reference number to which the results of the HTTP command
// are written.  This routine does not parse the returned HTTP
// header in any way.  The entire incoming stream goes into
// the file verbatim.
//
// For example, if you were asked to download a URL like:
//
//      http://devworld.apple.com/dev/technotes.shtml
//
// you would set:
//
//      o hostName to "devworld.apple.com:80" (80 is the
//        default port for HTTP.
//      o httpCommand to "GET /dev/technotes.shtml HTTP/1.0\0x13\0x10\0x13\0x10"
```

[Next](OTSimpleDownloadHTTPTest.c.md)[Previous](OTSimpleDownloadHTTP.c.md)

