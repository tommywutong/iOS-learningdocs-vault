---
title: Unarchiving Interface Objects With Interface Builder Services
apple_id: TP30001005
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2004-02-17'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/UnarchivingIOwithIBS/ibs_tasks/IBSTasks.html
archived_at: '2026-07-15T05:24:42.244874Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Unarchiving Interface Objects With Interface Builder Services](Introduction%20to%20Unarchiving%20Interface%20Objects%20With%20Interface%20Builder%20Services.md)


[Next](Document%20Revision%20History.md)[Previous](Interface%20Builder%20Services%20Concepts.md)

# Interface Builder Services Tasks

The primary tasks for which you’ll need to
use Interface Builder Services are:

- Unarchiving
  the menu bar and main window from your application’s main nib
  file
- Unarchiving an object from an auxiliary nib file
- Unarchiving an object from a framework or other bundle

Each of these tasks are described in the following sections.

When your application starts up, you need to call Interface
Builder Services functions to open the main nib file and unarchive
the interface objects that should be open after start-up. As the [Strategies for Storing Interface Objects](Interface%20Builder%20Services%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambvfvbuqmrqgiwugscei5auorkc) listed
in [Interface Builder Services Concepts](Interface%20Builder%20Services%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambvfvbuqmrqgiwugscejjcemrse) suggest,
the main nib file should contain only those items that are essential
when your application starts up. In most cases, the main nib file
should only contain the menu bar and perhaps a main window.

The steps below outline how to open a main nib file and unarchive
the objects in it. Listing 3-1 shows
how to implement the steps for a nib file that contains a menu bar
and a main window. If your application needs only one of these objects
at startup, you can easily modify the sample code.

1. Call the
   function `CreateNibReference` to create
   a reference to the main nib file.
2. Unarchive the menu bar from the main nib file by calling the
   function `SetMenuBarFromNib`. This function
   also sets the menu bar so users can use the menu bar when your application
   has started up.
3. If your application has a main window, you call the function `CreateWindowFromNib` to unarchive
   the main window.
4. After you have unarchived the objects from the main nib file,
   you must dispose of the nib reference by calling the function `DisposeNibReference`.
5. The function `CreateWindowFromNib` unarchives
   the window so it’s hidden. If you want the window to be visible,
   you must call the Window Manager function `ShowWindow`.

It is good practice to check for errors each step of the way,
as shown in [<xRefNoLink>Listing 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambvfvbuqmrqgmwugskiinaucrkk). If the interface can’t be created, you should
halt the start up process. Without an interface, your application
is likely to be useless.

__Listing 2-1__  Unarchiving the menu bar and main window
from the main nib file

```
int main (int argc, char* argv[])
{
    IBNibRef        nibRef;
    WindowRef       window;
    OSStatus        err;

    // Create a nib reference to a nib file.
    err = CreateNibReference (CFSTR ("main"), &nibRef);
    // Call the macro require_noerr to make sure no errors occurred
    require_noerr (err, CantGetNibRef);

    // Unarchive the menu bar and make it ready to use.
    err = SetMenuBarFromNib (nibRef, CFSTR("MainMenu"));
    require_noerr (err, CantSetMenuBar);

    // Unarchive the main window.
    err = CreateWindowFromNib (nibRef, CFSTR("MainWindow"), &window);
    require_noerr (err, CantCreateWindow);

    // Dispose of the nib reference as soon as you don’t need it any more.
    DisposeNibReference (nibRef);
    // Make the unarchived window visible.
    ShowWindow (window);

    // Start the event loop. RunApplicationEventLoop is a
     // Carbon Event Manager function.
    RunApplicationEventLoop ();

    // You’ll jump to one of the "Cant" statements only if there’s
    // an error.
    CantCreateWindow:
    CantSetMenuBar:
    CantGetNibRef:
    return err;
}
```


The [Strategies for Storing Interface Objects](Interface%20Builder%20Services%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambvfvbuqmrqgiwugscei5auorkc) suggest
that you create several nib files to store your application’s
interface objects. The main nib file should contain at the most,
the menu bar and the window that opens (if any) when your application
starts up. Document windows, palettes, toolbars, contextual menus,
and other interface objects should be stored in separate, auxiliary
nib files.

The steps for opening an auxiliary nib file and unarchiving
an object from it are similar to those used to open a main nib file:

1. Call the
   function `CreateNibReference` to create
   a reference to the auxiliary nib file that contains the object you
   want to unarchive.
2. Call the appropriate function to unarchive the object from
   the nib file. To unarchive a window, call the function `CreateWindowFromNib`,
   to unarchive a menu, call the function `CreateMenuFromNib`.
3. After you have unarchived the object from the auxiliary nib
   file, you must dispose of the nib reference by calling the function `DisposeNibReference`.

One common use of an auxiliary nib file is to store an object
that’s used repeatedly in an application, such as a document window.
Another use is to store objects that are rarely needed, such as
an About window. Listing
3-2 shows how to implement a `MyCreateNewDocument` function
that your application would call each time the user creates a new
document. Note that similar to [Listing 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambvfvbuqmrqgmwugskiinaucrkk), the code shown in Listing 3-2 implements error
checking.

__Listing 2-2__  Unarchiving a document window from an
auxiliary nib file

```
WindowRef MyCreateNewDocument (CFStringRef inName)
{
    IBNibRef documentNib;
    OSStatus err;
    WindowRef theWindow;

    // Create a nib reference to an auxiliary nib file with
    // the name document.nib.
    err = CreateNibReference (CFSTR ("document"), &documentNib);
    // Call the macro require_noerr to make sure no errors occurred
    require_noerr (err, CantGetNibRef);

    // Unarchive the document window. Use the name you gave to the
    // window object in the Instances pane in Interface Builder.
    err = CreateWindowFromNib (documentNib, CFSTR("MyDocument"),
                                                 &theWindow);
    require_noerr (err, CantCreateWindow);

    // Dispose of the nib reference as soon as you don’t need it anymore.
    DisposeNibReference (documentNib);

    // Call the Window Manager function to set the title shown in the
    // window’s title bar to the name passed to MyCreateNewDocument.
    err =  SetWindowTitleWithCFString (theWindow, inName);
    // In this example, the window gets returned. Remember, it’s been
    // unarchived, but it is still not visible. It won’t be visible
    // until you call the Window Manager function ShowWindow.
    return theWindow;

    // You’ll jump to one of the "Cant" statements only if there’s
    // an error.
    CantCreateWindow:
    CantGetNibRef:
     return NULL;
}
```


Your application is not limited to using interface objects
contained within its own bundle. You can unarchive interface objects
from another bundle or framework to which your application has access.
For example, you could unarchive a tools palette or other object provided
by a plug-in bundle.

The steps for unarchiving an object from a nib file in a framework
or other bundle are similar to those used to open an auxiliary nib
file. They are listed below. The main difference is that you need
to get a reference to the bundle. Then you must call the function `CreateNibReferenceWithCFBundle` instead
of `CreateNibReference`.

1. Call the
   Core Foundation URL Services function `CFURLCreateWithFileSystemPath` and the
   Core Foundation Bundle Services function `CFBundleCreate` to
   create a reference to the bundle that contains nib file you want
   to open. See the Core Foundation reference documentation for more
   information.
2. Call the function `CreateNibReferenceWithCFBundle` to
   create a reference to the nib file that contains the object you
   want to unarchive.
3. Call the appropriate function to unarchive the object from
   the nib file. To unarchive a window, call the function `CreateWindowFromNib`,
   to unarchive a menu, call the function `CreateMenuFromNib`.
4. After you have unarchived the object from the nib file, you
   must dispose of the nib reference by calling the function `DisposeNibReference`.

The function `MyCreateWidgetFromFramework`,
shown in [Listing 3-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambvfvbuqmrqgmwugskii5euuske), shows how to unarchive a “widget window” from
a bundle whose path you pass to the function.

__Listing 2-3__  Unarchiving a widget window from a nib
file in a bundle

```
WindowRef MyCreateWidgetFromBundle (CFStringRef widgetBundlePath
                                    CFStringRef widgetFileName,
                                    CFStringRef  widgetWindowName)
{
    IBNibRef widgetNib;
    OSStatus err;
    WindowRef theWindow;
    CFBundleRef mainBundle;
    CFURLRef    bundleURL;
    CFBundleRef widgetBundle;

    // Look for a resource in the bundle passed to
    // the function MyCreateWidgetFromBundle
    bundleURL = CFURLCreateWithFileSystemPath(
                            kCFAllocatorDefault,
                            widgetBundlePath,
                            kCFURLPOSIXPathStyle,
                            TRUE);
    // Make a bundle instance using the URL Reference
    widgetBundle = CFBundleCreate (kCFAllocatorDefault, bundleURL);

    // Create a nib reference to the nib file.
    err = CreateNibReferenceWithCFBundle (widgetBundle,
                            widgetFileName, &widgetNib);
    // Call the macro require_noerr to make sure no errors occurred
    require_noerr (err, CantGetNibRef);

    // Unarchive the widget window.
    err = CreateWindowFromNib (widgetNib, widgetWindowName, &theWindow);
    require_noerr (err, CantCreateWindow );

    // Dispose of the nib reference as soon as you don’t need it anymore.
    DisposeNibReference (widgetNib);
    // Release the Core Foundation objects
    CFRelease (bundleURL);
    CFRelease (widgetBundle);

    // In this example, the window gets returned. Remember, it’s been
    // unarchived, but it is still not visible. It won’t be visible
    // until you call the Window Manager function ShowWindow.
    return theWindow;

    // You’ll jump to one of the "Cant" statements only if there’s
    // an error.
    CantCreateWindow:
    CantGetNibRef:
     return NULL;
}
```

[Next](Document%20Revision%20History.md)[Previous](Interface%20Builder%20Services%20Concepts.md)

