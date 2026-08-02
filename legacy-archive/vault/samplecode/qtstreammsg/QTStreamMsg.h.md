---
title: qtstreammsg
apple_id: DTS10001053
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtstreammsg/Listings/QTStreamMsg_h.html
archived_at: '2026-07-26T19:53:07.273844Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtstreammsg](qtstreammsg.md)


[Next](Document%20Revision%20History.md)[Previous](QTStreamMsg.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# QTStreamMsg.h

```c
//////////
//
//  File:       QTStreamMsg.h
//
//  Contains:   Sample code for intercepting and issuing messages to the streaming controller bar.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      06/11/99    rtm     first file
//
//////////

#ifndef __MOVIES__
#include <Movies.h>
#endif

#include <stdlib.h>
#include <string.h>

//////////
//
// constants
//
//////////

#define MESSAGE_ARRAY       {                                   \
                                "Establishing connection",      \
                                "Talking to server",            \
                                "Filling buffer"                \
                            }

#define kConnectingMsgIndex     0
#define kNegotiatingMsgIndex    1
#define kBufferingMsgIndex      2

#define kMaxMessageSize         256         // largest streaming message we expect to receive

//////////
//
// function prototypes
//
//////////

void                            QTStreamMsg_IssueMessage (MovieController theMC, char *theMessage);
PASCAL_RTN Boolean              QTStreamMsg_ActionFilterProc (MovieController theMC, short theAction, void *theParams, long theRefCon);
```

[Next](Document%20Revision%20History.md)[Previous](QTStreamMsg.c.md)

