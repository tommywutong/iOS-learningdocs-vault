---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.1b.html
archived_at: '2026-07-15T05:23:56.560146Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)



__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.17.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.1a.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.1c.md)

---

#    Making a Custom Definition Function Theme-Compliant

The
MyEditTextFrameControlDefProc
function, shown in [Listing 3-6](#apple-gmytqmrq)
, draws a frame for an editable text field that is defined as a custom control definition function. The
MyEditTextFrameControlDefProc
function calls the
MyIsAppearancePresent
function, described in [Becoming a Client of the Appearance Manager](Becoming%20a%20Client%20of%20the%20Appearance%20Manager.md#apple-gqydmnrt)
, to determine whether the Appearance Manager is present. Depending upon the presence of the Appearance Manager,
MyEditTextFrameControlDefProc
branches between two functions to draw the frame.

If the Appearance Manager is not present,
MyEditTextFrameControlDefProc
calls the non-theme-compliant function,
MyClassicEditTextFrameControlDefProc
.
MyClassicEditTextFrameControlDefProc
first obtains the control rectangle, then supplies the control rectangle and a color to QuickDraw to draw the frame. However, an editable text frame drawn in this manner maintains the same "fixed" look in any appearance, and it cannot adapt to theme switches.

If the Appearance Manager is present, however,
MyEditTextFrameControlDefProc
calls the
MyAppearanceSavvyEditTextFrameControlDefProc
function.
MyAppearanceSavvyEditTextFrameControlDefProc
then passes the appropriate Appearance Manager constant for the drawing state (
kThemeStateActive
or
kThemeStateInactive
) to the function
DrawThemeEditTextFrame
.
DrawThemeEditTextFrame
draws the frame appropriately for the activity state and the current theme. And, when a theme switch occurs, the frame automatically takes on a look consistent with the current theme.

__Listing 3-6__  

Drawing a custom definition function that is theme-compliant

`

static pascal SInt32 MyClassicEditTextFrameControlDefProc (
                                                        SInt16 /* varCode */,
                                                        ControlHandle control,
                                                        ControlDefProcMessage message,
                                                        SInt32 /* param */)
{
    Rect contrlRect;

    switch (message)
    {
        case drawCntl :

            contrlRect = (**control).contrlRect;
            InsetRect (&contrlRect,-1,-1);
            // We're pre-Appearance Mgr here, so always draw in black...
            PenNormal ( );
            // unless the control part code value in contrlHilite indicates
            // that the control is inactive (or disabled); if so, draw in gray
            if ((**control).contrlHilite >= 254)
                PenPat (&(qd.gray));
            FrameRect (&contrlRect);
            break;

        default :

            // other cases omitted for simplicity
            break;
    }

    return 0;
}

static pascal SInt32 MyAppearanceSavvyEditTextFrameControlDefProc (
                                                        SInt16 /* varCode */,
                                                        ControlHandle control,
                                                        ControlDefProcMessage message,
                                                        SInt32 /* param */)
{
    Rect contrlRect;

    switch (message)
    {
        case drawCntl :

            contrlRect = (**control).contrlRect;
            DrawThemeEditTextFrame (&contrlRect,
                ((**control).contrlHilite < 254) ?
                    kThemeStateActive : kThemeStateInactive);
            break;

        default :

            // other cases omitted for simplicity
            break;
    }

    return 0;
}

static pascal SInt32 MyEditTextFrameControlDefProc (
                                                    SInt16 varCode,
                                                    ControlHandle control,
                                                    ControlDefProcMessage message,
                                                    SInt32 param)
{
    OSStatus err = noErr;

    Boolean haveAppearance;

    if (!(err = MyIsAppearancePresent (&haveAppearance)))
    {
        if (haveAppearance)
            err = MyAppearanceSavvyEditTextFrameControlDefProc (
                                                    varCode,
                                                    control,
                                                    message,
                                                    param);
        else
            err = MyClassicEditTextFrameControlDefProc (
                                                    varCode,
                                                    control,
                                                    message,
                                                    param);
    }

    return err;
}`

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.17.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.1a.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.1c.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
