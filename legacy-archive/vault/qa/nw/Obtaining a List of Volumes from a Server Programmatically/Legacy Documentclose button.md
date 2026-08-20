---
title: Obtaining a List of Volumes from a Server Programmatically
apple_id: DTS10001423
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/nw/nw11.html
archived_at: '2026-07-18T02:29:44.433178Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Networking](https://developer.apple.com/referencelibrary/Networking/index.html)

|  |
| --- |
| Technical Q&A NW11Obtaining a List of Volumes from a Server Programmatically |

|  |  |  |
| --- | --- | --- |
| ---   Q: How do I obtain a list of volumes from a server programmatically, given that I have the atalk-internet address of that server?  A: To obtain a list of volumes from a server programatically, you use an `AFPCommand` called `afpGetSParms`. This command requires you to log in (as either a guest or a user) and create a session, and then issue the `afpGetSParms`. The string returned by `afpGetSParms`, which is described on __page 13-98 of _Inside AppleTalk_,__looks like this:   |  | | --- | | ``` [0-3]   long    Current Date-time on Server's clock [4] byte    Number of Volumes that follow ---->     byte    NumVol Structure...         Msb = HasPassword (bit)         Lsb = HasConfigInfo (appleII stuff, ignore it)     P-String    Volume Name <---- ``` |   The string is repeated for each volume.  There is also an example in the __February 1995 Developer CD:__  __Dev.CD Feb 95:Sample Code:Snippets:Networking:AppleTalk Libraries__  The string from this example looks like this:   |  | | --- | | ``` short LogOnAsGuest(AddrBlock *serverAddress,Ptr SCBBlock)   {     AFPLoginPrm *XPPBlock;  /* to build parameter blocks for AFP */     short       cbsize;     char        XPPReply[quantumSize*8];          /* used to get AFP replies (max. size 8 ATP packet) */     char        XPPCmd[quantumSize]; /* used to send AFP commands */     OSErr       error;     short       result; -   /* information used by Login function */     char        AFPVersion[30];     char        AuthentMethod[30];      strcpy(AFPVersion, "AFPVersion 2.0");     strcpy(AuthentMethod, "No User Authent");      if (!(XPPBlock = (AFPLoginPrm *)NewPtrClear(sizeof(AFPLoginPrm))))         return MemError();      XPPBlock->ioRefNum = xppRefNum;     XPPBlock->ioCompletion = nil;     XPPBlock->aspTimeout = 1;    /* Timeout for ATP */     XPPBlock->aspRetry = 2;      /* Retry count for ATP */     XPPBlock->afpAddrBlock = *serverAddress;            /* AppleTalk address of the server */     XPPBlock->afpAttnRoutine = nil ;     XPPBlock->rbPtr = (Ptr)XPPReply; /* Reply buffer pointer */     XPPBlock->rbSize = quantumSize;  /* Reply buffer size */      /* prepare command information :        1st byte : command (login)        2nd Pascal string : AFP version        3rd Pascal string : Authentication                            Method - see Inside AppleTalk 13-104 */     XPPCmd[0] = afpLogin;     XPPCmd[1] = strlen(AFPVersion);     strcpy(XPPCmd+2,AFPVersion);     cbsize = strlen(XPPCmd);     XPPCmd[cbsize] = strlen(AuthentMethod);     strcpy(XPPCmd+cbsize+1,AuthentMethod);     cbsize = strlen(XPPCmd);      XPPBlock->cbPtr = (Ptr)XPPCmd; /* Command block pointer */     XPPBlock->cbSize = cbsize;     XPPBlock->afpSCBPtr = (Ptr) SCBBlock; /* SCB pointer in AFP login */     if ((error = AFPCommand((XPPParmBlkPtr)XPPBlock,sync)) != noErr)         result = error;     else         if (XPPBlock->cmdResult != noErr)            result =  XPPBlock->cmdResult ;         else result =  XPPBlock->sessRefnum;                 /* return session number */      DisposPtr((Ptr)XPPBlock);     return result; }   /* LogOnAsGuest */ OSErr GetServerParams(short sessNum,Ptr replyBuffer,short buffLength) {     XPPPrmBlk   *XPPBlock; /* to build parameter blocks for AFP */     char        XPPCmd[quantumSize];/* used to send AFP commands */     OSErr       error;      if (!(XPPBlock = (XPPPrmBlk *)NewPtrClear(sizeof(XPPPrmBlk))))         return MemError();     XPPBlock->ioRefNum = xppRefNum; /* driver reference number */     /* prepare command information :         no input provided except command - see IA 13-98 */     XPPCmd[0]  = afpGetSParms;      XPPBlock->sessRefnum = sessNum;     XPPBlock->aspTimeout = 2; /* Timeout for ATP */     XPPBlock->aspRetry = 2;     XPPBlock->cbPtr = (Ptr)XPPCmd;     XPPBlock->cbSize = 1;            /* Command block size */     XPPBlock->rbPtr = replyBuffer;   /* Reply buffer pointer */     XPPBlock->rbSize = buffLength;     XPPBlock->wdSize = 0;    /* Write Data size */     XPPBlock->wdPtr = nil;      /* Write Data pointer */      error = AFPCommand((XPPParmBlkPtr)XPPBlock,sync);     DisposPtr((Ptr)XPPBlock);     return error;  } main() { Str32 theServer; Ptr buffer; AddrBlock serverAddress; char SCBBlock[scbMemSize]; /* used by AFP to manage a session */ short sessionNum; OSErr ErrNo; short refNum; /* allocate a buffer to retrieve info */     if (!(buffer = NewPtr(buffSize))) return;  /* open .XPP driver */     ErrNo = OpenXPP(&refNum); // hard coded address cause I'm lazy     serverAddress.aNet = 41107;     serverAddress.aNode = 87;     serverAddress.aSocket = 250;  // simple login as guest     if ((sessionNum = LogOnAsGuest(              &serverAddress,&SCBBlock)) <= 0) {         DisposePtr(buffer);         return;         } // get server params     if ((ErrNo = GetServerParams(sessionNum,                 buffer,buffSize)) != noErr) {         DisposePtr(buffer);         return;         } // buffer has server string  // be a good citizen     LogOut(sessionNum,&SCBBlock);     DisposePtr(buffer); } ``` | |

#### [June 01 1995]

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
