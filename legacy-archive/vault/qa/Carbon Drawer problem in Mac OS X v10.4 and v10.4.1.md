---
title: Carbon Drawer problem in Mac OS X v10.4 and v10.4.1
apple_id: DTS10003735
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2005-06-21'
source_url: https://developer.apple.com/library/archive/qa/qa1435/_index.html
archived_at: '2026-07-18T02:30:43.132376Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1435

# Carbon Drawer problem in Mac OS X v10.4 and v10.4.1

## Q:  Why did my drawer separate from its parent window? Why did all my windows stick together?

A: Why did my drawer separate from its parent window? Why did all my windows stick together?

On Mac OS X v10.4 and v10.4.1, there is a drawer problem which has two sets of symptoms:

- Collapsing a window with a visible drawer and expanding this window from the Dock separates the drawer from its parent window.
- Closing a drawer with the mouse makes all document windows stick together.

This problem has been fixed in Mac OS X v10.4.2 but if you need a workaround for users who wouldn't or couldn't upgrade their system, you can use the following code.

In a typical window with a drawer creation code, you would have:

__Listing 1__  Creating a window with a drawer.

```
void CreateANewWindow() {     IBNibRef  nibRef;     WindowRef window;     WindowRef drawer;     OSStatus  status;      // Create a Nib reference passing the name of the nib file (without the .nib extension)     // CreateNibReference only searches into the application bundle.     status = CreateNibReference(CFSTR("main"), &nibRef);     require_noerr( status, CantGetNibRef );      // Then create a window. "MainWindow" is the name of the window object. This name is set in      // InterfaceBuilder when the nib is created.     status = CreateWindowFromNib(nibRef, CFSTR("MainWindow"), &window);     require_noerr(status, MainWindow);      // Then create a drawer window. "Drawer" is the name of the window object. This name is set in      // InterfaceBuilder when the nib is created.     status = CreateWindowFromNib(nibRef, CFSTR("Drawer"), &drawer);     require_noerr(status, Drawer);      // We don't need the nib reference anymore.     DisposeNibReference(nibRef);      // The window was created hidden so show it.     ShowWindow( window );      // Associating the windows     status = SetDrawerParent( drawer, window );     require_noerr(status, SetDrawerParent);      // And showing the drawer     status = ToggleDrawer( drawer );     require_noerr(status, ToggleDrawer);  ToggleDrawer: SetDrawerParent: InstallWindowEventHandler: MainWindow: Drawer: CantGetNibRef:      return; }
```

The first step for working around the bug is to add an event handler on the drawer window to intercept the two events kEventWindowConstrain and kEventWindowDrawerClosed. But you need to install this workaround only on Mac OS X v10.4 and v10.4.1 (if the workaround is applied on other versions of Mac OS X, it is unnecessary but harmless since the code checks for the presence of the problem (see the second comment in the FixDrawerBugTimer function)), thus:

__Listing 2__  Creating a window with a drawer with the workaround.

```
void CreateANewWindow() {     IBNibRef  nibRef;     WindowRef window;     WindowRef drawer;     OSStatus  status;      // Create a Nib reference passing the name of the nib file (without the .nib extension)     // CreateNibReference only searches into the application bundle.     status = CreateNibReference(CFSTR("main"), &nibRef);     require_noerr( status, CantGetNibRef );      // Then create a window. "MainWindow" is the name of the window object. This name is set in      // InterfaceBuilder when the nib is created.     status = CreateWindowFromNib(nibRef, CFSTR("MainWindow"), &window);     require_noerr(status, MainWindow);      // Then create a drawer window. "Drawer" is the name of the window object. This name is set in      // InterfaceBuilder when the nib is created.     status = CreateWindowFromNib(nibRef, CFSTR("Drawer"), &drawer);     require_noerr(status, Drawer);      // We don't need the nib reference anymore.     DisposeNibReference(nibRef);      // We don't have predefined constants for version numbers yet so...     if ((kHIToolboxVersionNumber >= 219) && ((kHIToolboxVersionNumber < 220))     {         const EventTypeSpec eventFixDrawerBugs[] =         {              { kEventClassWindow, kEventWindowConstrain },              { kEventClassWindow, kEventWindowDrawerClosed }         };         status = InstallWindowEventHandler( drawer, FixDrawerBugHandler,             GetEventTypeCount( eventFixDrawerBugs ), eventFixDrawerBugs, 0, NULL );         require_noerr(status, InstallWindowEventHandler);     }      // The window was created hidden so show it.     ShowWindow( window );      // Associating the windows     status = SetDrawerParent( drawer, window );     require_noerr(status, SetDrawerParent);      // And showing the drawer     status = ToggleDrawer( drawer );     require_noerr(status, ToggleDrawer);  ToggleDrawer: SetDrawerParent: InstallWindowEventHandler: MainWindow: Drawer: CantGetNibRef:      return; }
```

And the second step is to provide the event handler function and the actual workaround code function. This function is called by a one-time Carbon Event Timer function to ensure that the workaround code will be called after the HIToolbox has finished closing the drawer.

__Listing 3__  Workaround functions.

```
void FixDrawerBugTimer( EventLoopTimerRef inTimer, void* inRefcon ) {     WindowGroupRef        documentGroup = GetWindowGroupOfClass( kDocumentWindowClass );     ItemCount             childCount;     WindowGroupAttributes attr;      // Now that the timer has fired, we don't need it any more     RemoveEventLoopTimer( inTimer );      //     // If the document group does not have the MoveTogether attribute, then we're running     // on an OS release that has fixed this bug, and we don't need to do anything else.     //     verify_noerr( GetWindowGroupAttributes( documentGroup, &attr ) );     if ( ( attr & kWindowGroupAttrMoveTogether ) == 0 )         return;      // Clear the MoveTogether attribute from the document group     verify_noerr( ChangeWindowGroupAttributes( documentGroup, 0, kWindowGroupAttrMoveTogether ) );      // Count the groups that are immediate children of the document group     childCount = CountWindowGroupContents( documentGroup, kNilOptions );     if ( childCount > 0 )     {         WindowGroupRef* groups = (WindowGroupRef*) calloc( sizeof( WindowGroupRef ), childCount );         if ( groups != NULL )         {             ItemCount i;             verify_noerr( GetWindowGroupContents( documentGroup, kNilOptions, childCount, NULL, (void**) groups ) );              //             // For each child of the document group, if that child group has the MoveTogether attribute itself,             // then clear and then reset the attribute. This will fix the binding between windows in the group.             //             for ( i = 0; i < childCount; i++ )             {                 WindowGroupRef group = groups[i];                  verify_noerr( GetWindowGroupAttributes( group, &attr ) );                 if ( ( attr & kWindowGroupAttrMoveTogether ) != 0 )                 {                     ChangeWindowGroupAttributes( group, 0, kWindowGroupAttrMoveTogether );                     ChangeWindowGroupAttributes( group, kWindowGroupAttrMoveTogether, 0 );                 }             }              free( groups );         }     } }  pascal OSStatus FixDrawerBugHandler(EventHandlerCallRef inHandlerCallRef, EventRef inEvent, void *inUserData) {     check( GetEventClass( inEvent ) == kEventClassWindow );      switch ( GetEventKind( inEvent ) )     {         case kEventWindowConstrain:             return noErr;          case kEventWindowDrawerClosed:             // Use a one-shot timer to postpone our fixup code             // until after the toolbox has finished closing the drawer             return InstallEventLoopTimer( GetCurrentEventLoop(), 0, 0, FixDrawerBugTimer, 0, NULL );     }      return eventNotHandledErr; }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-06-21 | New document that workaround for a drawer problem present in Mac OS X v10.4 but fixed in v10.4.2 |

