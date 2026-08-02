---
title: Carbon-Cocoa Integration Guide
apple_id: TP30000893
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CarbonCocoaDoc/Articles/NavigationServices.html
archived_at: '2026-07-15T07:11:57.480967Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Carbon-Cocoa Integration Guide](Introduction%20to%20Carbon-Cocoa%20Integration%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](HICocoaView-%20Using%20Cocoa%20Views%20in%20Carbon%20Windows.md)

# Using Cocoa in a Navigation Services Dialog

Beginning in Mac OS X v10.5, Navigation Services dialogs are implemented using custom subclasses of the Cocoa [NSOpenPanel](https://developer.apple.com/documentation/appkit/nsopenpanel) and [NSSavePanel](https://developer.apple.com/documentation/appkit/nssavepanel) classes. This ensures that Carbon applications using Navigation Services receive the same user interface improvements as Cocoa applications. This change applies to sheet dialogs as well.

As a result of this change, Carbon applications can directly access features in these two Cocoa classes. A Navigation Services `NavDialogRef` object can be cast to a pointer to an instance of either `NSOpenPanel` or `NSSavePanel`, depending on the dialog type. By casting your `NavDialogRef` object to the appropriate Cocoa object, you can use any of the Objective-C accessor methods in the Cocoa object’s class. This is similar to toll-free bridging (see [Interchangeable Data Types](Interchangeable%20Data%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgqydclkukayq)), but it only works in one direction.

There are some limitations to the bridging between Navigation Services and Cocoa. Dialogs created with Navigation Services must be invoked with `NavDialogRun` rather than with `NSOpenPanel` or `NSSavePanel` methods. As implied above, dialogs created with `NSOpenPanel` or `NSSavePanel` constructors cannot be cast to an `NavDialogRef` object. The Carbon and Cocoa models have some overlapping functionality such as file filtering, setting an accessory view, and setting a delegate object. In these cases, to avoid conflicts you should not mix the two models.

Here’s an example that uses Navigation Services to create an Open File dialog and casts it to an `NSOpenPanel` object to set the title and message text displayed in the dialog:

```
// navOptions structure has been created and initialized for text documents
NavDialogRef theDialog = NULL;
NavCreateChooseFileDialog(&navOptions, NULL, NULL, NULL, Handle_NavFilter, NULL, &theDialog);
[(NSOpenPanel*)theDialog setTitle:@"Open Document"];
[(NSOpenPanel*)theDialog setMessage:@"Choose a text document to open:"];
NavDialogRun(theDialog);
```

[Next](Document%20Revision%20History.md)[Previous](HICocoaView-%20Using%20Cocoa%20Views%20in%20Carbon%20Windows.md)

