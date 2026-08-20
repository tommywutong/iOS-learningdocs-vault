---
title: TickerView
apple_id: DTS10000648
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/TickerView/Listings/main_cp.html
archived_at: '2026-07-18T03:26:54.671130Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TickerView](TickerView.md)


[Next](TTickerView.cp.md)[Previous](TickerView.md)

# main.cp

```c
#include <Carbon/Carbon.h>

#include "TTickerView.h"


int main(int argc, char* argv[])
{
#pragma unused( argc, argv )
    IBNibRef        nibRef;
    WindowRef       window;
    HIViewRef       view;

    OSStatus        err;

    // Workaround: Unfortunately, at the time we call RegisterClass below,
    // the HIView base class isn't registered. It's supposed to be automatically
    // registered, but something is going wrong in HIToolbox. We can force
    // it to register by creating any arbitrary view. Here, we simply create
    // and release a scroll view. That's enough to make sure the HIView base
    // class is registered. Sorry folks.
    HIScrollViewCreate( kHIScrollViewOptionsVertScroll, &view );
    CFRelease( view );

    // Register our ticker view subclass 
    TTickerView::RegisterClass();

    // Create a Nib reference passing the name of the nib file (without the .nib extension)
    // CreateNibReference only searches into the application bundle.
    err = CreateNibReference( CFSTR( "main" ), &nibRef );
    require_noerr( err, CantGetNibRef );

    // Once the nib reference is created, set the menu bar. "MainMenu" is the name of the menu bar
    // object. This name is set in InterfaceBuilder when the nib is created.
    err = SetMenuBarFromNib( nibRef, CFSTR( "MenuBar" ) );
    require_noerr( err, CantSetMenuBar );

    // Then create a window. "MainWindow" is the name of the window object. This name is set in 
    // InterfaceBuilder when the nib is created.
    err = CreateWindowFromNib( nibRef, CFSTR( "MainWindow" ), &window );
    require_noerr( err, CantCreateWindow );

    // We don't need the nib reference anymore.
    DisposeNibReference( nibRef );

    // The window was created hidden so show it.
    ShowWindow( window );

    // Call the event loop
    RunApplicationEventLoop();

CantCreateWindow:
CantSetMenuBar:
CantGetNibRef:

    return err;
}
```

[Next](TTickerView.cp.md)[Previous](TickerView.md)

