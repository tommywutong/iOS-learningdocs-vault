---
title: PDEProject
apple_id: DTS10000745
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/PDEProject/Listings/PDEPrint_Headers_PDEUtilities_h.html
archived_at: '2026-07-18T03:18:23.523353Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PDEProject](PDEProject.md)


[Next](PDEPrint-Resources-English.lproj-Help-help.html.md)[Previous](PDEPrint-Headers-PDECustom.h.md)

# PDEPrint/Headers/PDEUtilities.h

```c
/*
********************************************************************************

    $Log: PDEUtilities.h,v $


    (c) Copyright 2002 Apple Computer, Inc.  All rights reserved.

    IMPORTANT: This Apple software is supplied to you by Apple Computer,
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
    Neither the name, trademarks, service marks or logos of Apple Computer,
    Inc. may be used to endorse or promote products derived from the Apple
    Software without specific prior written permission from Apple.  Except
    as expressly stated in this notice, no other rights or licenses, express
    or implied, are granted by Apple herein, including but not limited to
    any patent rights that may be infringed by your derivative works or by
    other works in which the Apple Software may be incorporated.

    The Apple Software is provided by Apple on an "AS IS" basis. APPLE MAKES
    NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION THE
    IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS FOR
    A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND
    OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.

    IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL
    OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
    SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
    INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION,
    MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED
    AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE),
    STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE
    POSSIBILITY OF SUCH DAMAGE.

********************************************************************************
*/

#ifndef __PDEUTILITIES__
#define __PDEUTILITIES__

#include <Carbon/Carbon.h>
#include <Print/PMPrintingDialogExtensions.h>

#include "PDECore.h"


/*
--------------------------------------------------------------------------------
    Prototypes
--------------------------------------------------------------------------------
*/

extern void         MyDebugMessage (char *msg, SInt32 err);

extern CFBundleRef  MyGetBundle();
extern void         MyFreeBundle();

extern CFStringRef  MyGetTitle();
extern void         MyFreeTitle();

extern OSStatus     MyEmbedControl (WindowRef, ControlRef, const ControlID*, ControlRef*);
extern OSStatus     MyGetTicket (PMPrintSession, CFStringRef, PMTicketRef*);

extern void         MyReleaseContext (MyContext);
extern OSStatus     MyInstallHelpEventHandler (WindowRef, EventHandlerRef*, EventHandlerUPP *);
extern OSStatus     MyRemoveHelpEventHandler (EventHandlerRef*, EventHandlerUPP *);


#endif
```

[Next](PDEPrint-Resources-English.lproj-Help-help.html.md)[Previous](PDEPrint-Headers-PDECustom.h.md)

