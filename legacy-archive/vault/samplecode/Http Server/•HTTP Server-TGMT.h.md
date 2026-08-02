---
title: Http Server
apple_id: DTS10000238
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Http_Server/Listings/_HTTP_Server_TGMT_h.html
archived_at: '2026-07-18T03:11:58.029429Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Http Server](Http%20Server.md)


[Next](%E2%80%A2HTTP%20Server-THTTPServer.cp.md)[Previous](%E2%80%A2HTTP%20Server-TGMT.cp.md)

# •HTTP Server/TGMT.h

```c
//  TGmt.h - G M Time class object
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

#ifndef _H_TGMT
#define _H_TGMT

#include <iostream.h>

class TGmt
 {
    friend ostream &operator<< (ostream&, const TGmt&);
    enum {kUndefined = 0};  

public:
    TGmt() : fTime(kUndefined) {};

    void Now();
    unsigned long Elapsed();

private:
    unsigned long   fTime;
};

#endif
```

[Next](%E2%80%A2HTTP%20Server-THTTPServer.cp.md)[Previous](%E2%80%A2HTTP%20Server-TGMT.cp.md)

