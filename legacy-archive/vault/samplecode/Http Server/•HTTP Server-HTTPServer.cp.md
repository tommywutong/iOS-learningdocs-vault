---
title: Http Server
apple_id: DTS10000238
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Http_Server/Listings/_HTTP_Server_HTTPServer_cp.html
archived_at: '2026-07-18T03:11:57.797043Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Http Server](Http%20Server.md)


[Next](%E2%80%A2HTTP%20Server-HttpServer.r.md)[Previous](Http%20Server.md)

# •HTTP Server/HTTPServer.cp

```c
//  ServerShell.cp - Macintosh OpenTransport Network Server shell 
//
// Apple Macintosh Developer Technical Support
// Written by:  Vinne Moscaritolo
//
//  Copyright (work in progress)  Apple Computer, Inc All rights reserved.
//
// You may incorporate this sample code into your applications without
// restriction, though the sample code has been provided "AS IS" and the
// responsibility for its operation is 100% yours.  However, what you are
// not permitted to do is to redistribute the source as "DSC Sample Code"
// after having made changes. If you're going to re-distribute the source,
// we require that you make it clear in the source that the code was
// descended from Apple Sample Code, but that you've made changes.
//

#include "THTTPServer.h"

// ---------------------------------------------------------------------------
//   main
// ---------------------------------------------------------------------------
//  xxx

#include <strstream.h>


void main()
{
char errorBuf[256];
ostrstream err( errorBuf,256);

    try
    {
        THTTPServerApp      theApp; 
        theApp.Start();
    }

// Error handler
    catch (TNetworkException &ex)
    {
        err << "NETWORK EXCEPTION: " << ex.GetExceptionMessage() << ", OSStatus: " << ex.GetOSStatus() <<
                ", File: " << ex.GetExceptionFile() << ", Line: " << ex.GetExceptionLine() << endl;
    }

    catch(TMacException &ex)
    {
        err << "EXCEPTION: " << ex.GetExceptionMessage() << ",  OSErr: " << ex.GetExceptionOSErr() <<
                ", File: " << ex.GetExceptionFile() << ", Line: " << ex.GetExceptionLine() << endl;
    }

    catch(...)      // catch everything
    {
        err <<"Undefined exception.\n";
    } 


}
```

[Next](%E2%80%A2HTTP%20Server-HttpServer.r.md)[Previous](Http%20Server.md)

