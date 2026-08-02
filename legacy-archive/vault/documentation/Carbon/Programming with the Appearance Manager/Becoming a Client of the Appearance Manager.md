---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.11.html
archived_at: '2026-07-15T05:23:56.424738Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)



__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.f.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.10.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.12.md)

---

#   Becoming a  Client of the Appearance Manager

Before calling any Appearance Manager functions, you should check that the Appearance Manager is present. [Listing 3-1](#apple-ge4dimby)
shows an example of a function that simply checks to see whether the Appearance Manager is present. You may wish to perform a more extended check to determine, for example, the version of the Appearance Manager that is installed.

__Listing 3-1__  

Determining whether the Appearance Manager is present

`

static pascal OSStatus MyIsAppearancePresent (Boolean *haveAppearance)
{
    OSStatus err = noErr;

    long response;

    // Attempt to call Gestalt; if we succeed, test for presence of Appearance Mgr
    if (!(err = Gestalt (gestaltAppearanceAttr,&response)))
        *haveAppearance = response & (1 << gestaltAppearanceExists) ? true : false;
    // If the Appearance Mgr selector is undefined, the Appearance Mgr is not present
    else if (err == gestaltUndefSelectorErr)
    {
        *haveAppearance = false;
        err = noErr;
    }

    return err;
}`

After determining that the Appearance Manager is present, but prior to initializing or drawing any onscreen elements or invoking any definition functions, you should 

register your program as client of the Appearance Manager by calling the function
RegisterAppearanceClient
, which is all many programs need to do to be theme-compliant.

You should call
RegisterAppearanceClient
in order to receive Appearance Manager Apple events. With Appearance Manager 1.1 and later, when the user changes the current appearance (that is, when a theme switch occurs), the Appearance Manager sends Apple events to all running applications that are registered as clients of the Appearance Manager and which are high-level event aware. Because typical results of a theme switch might include a change in menu bar height or window structure dimensions, as well as changes to the system fonts, colors, and patterns currently in use, you should listen for and, under most circumstances, respond to the Appearance Manager Apple events. See
Appearance Manager Apple Event Constants
for more details on the Appearance Manager Apple events.

> ####  Note
>
> 
>
> The Appearance Manager Apple events are notifications your program receives after the theme switch has occurred, so you should not depend on receiving an Apple event before being asked to redraw in the new theme.

When your program calls
RegisterAppearanceClient
, the Appearance Manager also automatically maps standard pre-Appearance Manager definition functions to their theme-compliant equivalents for your program, whether or not systemwide appearance is active; see [Definition Function Mapping and Program Registration](Definition%20Function%20Mapping%20and%20Program%20Registration.md#apple-giytemrq)
for more details on this process.

You are also encouraged to register plug-ins with the Appearance Manager in order to receive definition function mapping when systemwide appearance is off. You can use the function
IsAppearanceClient
to determine if the process containing your plug-in is registered as a client of the Appearance Manager. If it is not, you can register your plug-in on entry by calling
RegisterAppearanceClient
, and you can unregister it on exit by calling the function
UnregisterAppearanceClient
.

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.f.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.10.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.12.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
