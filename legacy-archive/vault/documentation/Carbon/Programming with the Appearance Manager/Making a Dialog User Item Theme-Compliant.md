---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.19.html
archived_at: '2026-07-15T05:23:56.531513Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)



__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.17.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.18.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.1a.md)

---

#    Making a Dialog User Item Theme-Compliant

[Listing 3-4](#apple-gm3dgnzt)
shows another sample function,
MyEditTextFrameUserItemProc
, which, depending upon the presence of the Appearance Manager, branches between two functions, each of which draws a frame for an editable text field. In this example, the editable text frame is defined as a dialog user item. Again, prior to drawing, the
MyEditTextFrameUserItemProc
function calls the
MyIsAppearancePresent
function, described in [Becoming a Client of the Appearance Manager](Becoming%20a%20Client%20of%20the%20Appearance%20Manager.md#apple-gqydmnrt)
, to determine whether the Appearance Manager is present.

If the Appearance Manager is not present,
MyEditTextFrameUserItemProc
calls the function
MyClassicEditTextFrameUserItemProc
.
MyClassicEditTextFrameUserItemProc
first obtains the frame's rectangle from the Dialog Manager, then supplies the rectangle and a color to QuickDraw to draw the frame. However, an editable text frame drawn in this manner maintains the same "fixed" look in any appearance and cannot adapt to theme switches.

If the Appearance Manager is present, however,
MyEditTextFrameUserItemProc
calls
MyAppearanceSavvyEditTextFrameUserItemProc
.
MyAppearanceSavvyEditTextFrameUserItemProc
then passes the appropriate Appearance Manager constant for the drawing state (
kThemeStateActive
or
kThemeStateInactive
) to the function
DrawThemeEditTextFrame
.
DrawThemeEditTextFrame
draws the frame appropriately for the activity state and the current theme. And, when a theme switch occurs, the frame automatically takes on a look consistent with the current theme.

__Listing 3-4__  

Drawing a dialog user item that is theme-compliant

`

static pascal void MyClassicEditTextFrameUserItemProc (
                                                WindowPtr window,
                                                DialogItemIndex itemIndex)
{
    short iType;
    Handle iHandle;
    Rect iRect;

    GetDialogItem (window,itemIndex,&iType,&iHandle,&iRect);
    InsetRect (&iRect,-1,-1);
    // We're pre-Appearance Mgr here, so always draw in black...
    PenNormal ( );
    // unless the editable text field is disabled (inactive); if so, draw in gray
    if (iType & kItemDisableBit) PenPat (&(qd.gray));
    FrameRect (&iRect);
}

static pascal void MyAppearanceSavvyEditTextFrameUserItemProc (
                                                WindowPtr window,
                                                DialogItemIndex itemIndex)
{
    short iType;
    Handle iHandle;
    Rect iRect;

    GetDialogItem (window,itemIndex,&iType,&iHandle,&iRect);
    DrawThemeEditTextFrame (&iRect,
        (iType & kItemDisableBit) ?
            kThemeStateInactive : kThemeStateActive);
}

static pascal void MyEditTextFrameUserItemProc (
                                                WindowPtr window,
                                                DialogItemIndex itemIndex)
{
    OSStatus err = noErr;

    Boolean haveAppearance;

    if (!(err = MyIsAppearancePresent (&haveAppearance)))
    {
        if (haveAppearance)
            MyAppearanceSavvyEditTextFrameUserItemProc (window, itemIndex);
        else
            MyClassicEditTextFrameUserItemProc (window, itemIndex);
    }
}`

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.17.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.18.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.1a.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
