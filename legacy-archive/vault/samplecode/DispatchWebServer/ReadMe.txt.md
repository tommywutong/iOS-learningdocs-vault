---
title: DispatchWebServer
apple_id: DTS40007762
resource_type: Sample Code
platform: macOS
topic: Performance
technology: null
published: '2009-05-29'
source_url: https://developer.apple.com/library/archive/samplecode/DispatchWebServer/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:07:02.002502Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DispatchWebServer](DispatchWebServer.md)


[Next](DispatchWebServer.c.md)[Previous](DispatchWebServer.md)

# ReadMe.txt

```
### DispatchWebServer ###

===========================================================================
DESCRIPTION:

Sample code showing how to: Use dispatch in a real world setting,
schedule file and network I/O, use vnode sources, create and manage
timers.

===========================================================================
BUILD REQUIREMENTS:

Mac OS X version 10.6 Snow Leopard

===========================================================================
RUNTIME REQUIREMENTS:

Mac OS X version 10.6 Snow Leopard

===========================================================================
PACKAGING LIST:

DispatchWebServer.c       - the web server

===========================================================================
RUNNING:

Running the program will start a web server on port 8080. It will read
content from ~/Sites and write ~/Library/Logs/DispatchWebServer-transfer.log
each time it completes a request.

It will write some status to stdout when it makes new connections, receives
requests, completes requests, and when it closes connections.   It also
shows the state of each active request once every five seconds and any
time you send a SIGINFO signal to it.

===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

Version 1.0
- First version

===========================================================================
Copyright (C) 2009 Apple Inc. All rights reserved.
```

[Next](DispatchWebServer.c.md)[Previous](DispatchWebServer.md)

