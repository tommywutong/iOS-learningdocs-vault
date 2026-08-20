---
title: AppearanceSampleUpdated
apple_id: DTS10003689
resource_type: Sample Code
platform: Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2005-06-27'
source_url: https://developer.apple.com/library/archive/samplecode/AppearanceSampleUpdated/Listings/AppearanceSample_final_RadioGroup_cp.html
archived_at: '2026-07-26T19:54:08.010126Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AppearanceSampleUpdated](AppearanceSampleUpdated.md)


[Next](AppearanceSample-final-RadioGroup.h.md)[Previous](AppearanceSample-final-PushButtonSheet.h.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# AppearanceSample-final/RadioGroup.cp

```c
/*
    File:       RadioGroup.cp

    Contains:   Class to implement a radio group.

    Version:    Appearance 1.0 SDK

    Copyright:  © 1997 by Apple Computer, Inc., all rights reserved.

    File Ownership:

        DRI:                Edward Voas

        Other Contact:      7 of 9, Borg Collective

        Technology:         OS Technologies Group

    Writers:

        (edv)   Ed Voas

    Change History (most recent first):

         <1>     9/11/97    edv     First checked in.
*/

#include "AppearanceSamplePrefix.h"

#if !BUILDING_FOR_CARBON_8
    #include <HIToolbox/ControlDefinitions.h>
#else
    #include <ControlDefinitions.h>
#endif

#include "RadioGroup.h"

typedef struct
{
    ControlRef      control;
    SInt16          value;
} RadioEntry;

RadioGroup::RadioGroup()
{
    fInfo = NewHandle( 0 );
    fValue = 0;
    fMixed = false;
}

RadioGroup::~RadioGroup()
{
    DisposeHandle( fInfo );
}

void
RadioGroup::AddControl( ControlRef control, SInt16 value )
{
    Size        size;
    SInt16      numItems;

    size = GetHandleSize( fInfo );
    numItems = size / sizeof( RadioEntry );

    SetHandleSize( fInfo, size + sizeof( RadioEntry ) );

    ((RadioEntry*)*fInfo)[ numItems ].value = value;
    ((RadioEntry*)*fInfo)[ numItems ].control = control;

    SetValue( value );
}

SInt16
RadioGroup::GetValue()
{
    return fValue;
}

void
RadioGroup::SetValue( SInt16 value )
{
    SInt16      numItems;
    SInt16      i;
    ControlRef  oldControl = nil, newControl = nil;

    if ( fMixed )
    {
        numItems = GetHandleSize( fInfo ) / sizeof( RadioEntry );

        for ( i = 0; i < numItems; i++ )
        {
            if ( GetControlValue( ((RadioEntry*)*fInfo)[ i ].control ) )
            {
                SetControlValue( ((RadioEntry*)*fInfo)[ i ].control, 0 );
            }
        }
    }

    if ( (value != fValue) || fMixed )
    {
        numItems = GetHandleSize( fInfo ) / sizeof( RadioEntry );

        for ( i = 0; i < numItems; i++ )
        {
            if ( ((RadioEntry*)*fInfo)[ i ].value == value )
                newControl = ((RadioEntry*)*fInfo)[ i ].control;

            if ( ((RadioEntry*)*fInfo)[ i ].value == fValue )
                oldControl = ((RadioEntry*)*fInfo)[ i ].control;
        }
        if ( newControl )
        {
            if ( oldControl )
                SetControlValue( oldControl, 0 );

            SetControlValue( newControl, 1 );
        }
        fValue = value;
    }
    fMixed = false;
}

void
RadioGroup::SetMixed( SInt16 value )
{
    SInt16      numItems;
    SInt16      i;
    ControlRef  newControl = nil;

    numItems = GetHandleSize( fInfo ) / sizeof( RadioEntry );

    for ( i = 0; i < numItems; i++ )
    {
        if ( ((RadioEntry*)*fInfo)[ i ].value == value )
        {
            newControl = ((RadioEntry*)*fInfo)[ i ].control;
            break;
        }
    }
    if ( newControl )
    {
        SetControlValue( newControl, kControlCheckBoxMixedValue );
    }
    fValue = value;

    fMixed = true;
}

void
RadioGroup::SetValueByControl( ControlRef control )
{
    SInt16      numItems;
    SInt16      i;
    ControlRef  oldControl = nil;
    SInt16      value = 0;
    Boolean     valueFound = false;

    if ( fMixed )
    {
        numItems = GetHandleSize( fInfo ) / sizeof( RadioEntry );

        for ( i = 0; i < numItems; i++ )
        {
            if ( GetControlValue( ((RadioEntry*)*fInfo)[ i ].control ) )
            {
                SetControlValue( ((RadioEntry*)*fInfo)[ i ].control, 0 );
            }
        }
    }

    numItems = GetHandleSize( fInfo ) / sizeof( RadioEntry );

    for ( i = 0; i < numItems; i++ )
    {
        if ( ((RadioEntry*)*fInfo)[ i ].control == control )
        {
            value = ((RadioEntry*)*fInfo)[ i ].value;
            valueFound = true;
        }

        if ( ((RadioEntry*)*fInfo)[ i ].value == fValue )
            oldControl = ((RadioEntry*)*fInfo)[ i ].control;
    }
    if ( valueFound )
    {
        if ( oldControl )
            SetControlValue( oldControl, 0 );

        SetControlValue( control, 1 );

        fValue = value;
    }
    fMixed = false;
}
```

[Next](AppearanceSample-final-RadioGroup.h.md)[Previous](AppearanceSample-final-PushButtonSheet.h.md)

