---
title: AppearanceSampleUpdated
apple_id: DTS10003689
resource_type: Sample Code
platform: Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2005-06-27'
source_url: https://developer.apple.com/library/archive/samplecode/AppearanceSampleUpdated/Listings/AppearanceSample_1_BevelDialog_cp.html
archived_at: '2026-07-26T19:53:52.791616Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AppearanceSampleUpdated](AppearanceSampleUpdated.md)


[Next](AppearanceSample-1-BevelDialog.h.md)[Previous](AppearanceSample-1-BevelButtonSheet.h.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# AppearanceSample-1/BevelDialog.cp

```c
/*
    File:       BevelDialog.cp

    Contains:   Bevel Button examples dialog.

    Version:    Mac OS X

    Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple Computer, Inc.
                ("Apple") in consideration of your agreement to the following terms, and your
                use, installation, modification or redistribution of this Apple software
                constitutes acceptance of these terms.  If you do not agree with these terms,
                please do not use, install, modify or redistribute this Apple software.

                In consideration of your agreement to abide by the following terms, and subject
                to these terms, Apple grants you a personal, non-exclusive license, under AppleÕs
                copyrights in this original Apple software (the "Apple Software"), to use,
                reproduce, modify and redistribute the Apple Software, with or without
                modifications, in source and/or binary forms; provided that if you redistribute
                the Apple Software in its entirety and without modifications, you must retain
                this notice and the following text and disclaimers in all such redistributions of
                the Apple Software.  Neither the name, trademarks, service marks or logos of
                Apple Computer, Inc. may be used to endorse or promote products derived from the
                Apple Software without specific prior written permission from Apple.  Except as
                expressly stated in this notice, no other rights or licenses, express or implied,
                are granted by Apple herein, including but not limited to any patent rights that
                may be infringed by your derivative works or by other works in which the Apple
                Software may be incorporated.

                The Apple Software is provided by Apple on an "AS IS" basis.  APPLE MAKES NO
                WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION THE IMPLIED
                WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS FOR A PARTICULAR
                PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND OPERATION ALONE OR IN
                COMBINATION WITH YOUR PRODUCTS.

                IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL OR
                CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
                GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
                ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION, MODIFICATION AND/OR DISTRIBUTION
                OF THE APPLE SOFTWARE, HOWEVER CAUSED AND WHETHER UNDER THEORY OF CONTRACT, TORT
                (INCLUDING NEGLIGENCE), STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN
                ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

    Copyright © 1997-2001 Apple Computer, Inc., All Rights Reserved
*/

//
//  This file implements a simple dialog which shows a myriad of bevel
//  button possibilities. Even with all it shows, it does not show all
//  the possible variations.
//

#include "AppearanceSamplePrefix.h"

#if !BUILDING_FOR_CARBON_8
    #include <Carbon/Carbon.h>
#else
    #include <Carbon.h>
#endif

#include "BevelDialog.h"
#include "AppearanceHelpers.h"

enum {
    kDisableButton      = 'DISA',
    kEnableButton       = 'ENAB',
    kOnButton           = 'ON  ',
    kOffButton          = 'OFF ',
    kMixedButton        = 'MIXD',
    kFirstButton        = 6,
    kLastButton         = 32
};

const ControlID     kUserPane   = { 'BBUT', 1000 };

BevelDialog::BevelDialog()
    : TWindow( CFSTR( "AppearanceSample" ), CFSTR( "Bevel Buttons" ) )
{
    ::SetThemeWindowBackground( GetWindowRef(), kThemeActiveDialogBackgroundBrush, true );
    Show();
}

BevelDialog::~BevelDialog()
{
}

Boolean
BevelDialog::HandleCommand( UInt32 commandID )
{
    Boolean     handled = true;

    switch ( commandID )
    {
        case kDisableButton:
            EnableDisableAll( false );
            break;

        case kEnableButton:
            EnableDisableAll( true );
            break;

        case kOnButton:
            SetControlValues( kControlCheckBoxCheckedValue );
            break;

        case kOffButton:
            SetControlValues( kControlCheckBoxUncheckedValue );
            break;

        case kMixedButton:
            SetControlValues( kControlCheckBoxMixedValue );
            break;

        default:
            handled = TWindow::HandleCommand( commandID );
            break;
    }

    return handled;
}

void
BevelDialog::EnableDisableAll( Boolean enable )
{
    if ( enable )
        EnableControlByID( kUserPane );
    else
        DisableControlByID( kUserPane );
}

void
BevelDialog::SetControlValues( short value )
{
    ControlHandle control;
    short       i;

    for ( i = kFirstButton; i <= kLastButton; i++ )
    {
        ControlID       theID = { 'BBUT', i };

        ::GetControlByID( GetWindowRef(), &theID, &control );
        ::SetControlValue( control, value );
    }
}
```

[Next](AppearanceSample-1-BevelDialog.h.md)[Previous](AppearanceSample-1-BevelButtonSheet.h.md)

