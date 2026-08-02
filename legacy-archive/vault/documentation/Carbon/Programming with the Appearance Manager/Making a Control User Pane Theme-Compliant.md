---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.1a.html
archived_at: '2026-07-15T05:23:56.546187Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)



__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.17.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.19.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.1b.md)

---

#    Making a Control User Pane Theme-Compliant

[Listing 3-5](#apple-gi4dgmzt)
shows a sample function,
MyEditTextFrameControlUserPaneDrawProc
, which, depending upon the presence of the Appearance Manager, branches between two functions, each of which draws a frame for an editable text field. In this example, the frame is defined as a control user pane. Before drawing, the
MyEditTextFrameControlUserPaneDrawProc
function calls the
MyIsAppearancePresent
function, described in [Becoming a Client of the Appearance Manager](Becoming%20a%20Client%20of%20the%20Appearance%20Manager.md#apple-gqydmnrt)
, to determine whether the Appearance Manager is present.

MyEditTextFrameControlUserPaneDrawProc
calls
MyClassicEditTextFrameControlUserPaneDrawProc
if the Appearance Manager is not present.
MyClassicEditTextFrameControlUserPaneDrawProc
first obtains the control rectangle, then supplies the control rectangle and a color to QuickDraw to draw the frame. However, an editable text frame drawn in this manner maintains a "fixed" look in any appearance and cannot adapt to a theme switch.

If the Appearance Manager is present,
MyEditTextFrameControlUserPaneDrawProc
calls the
MyAppearanceSavvyEditTextFrameControlUserPaneDrawProc
function.
MyAppearanceSavvyEditTextFrameControlUserPaneDrawProc
then passes the appropriate Appearance Manager constant for the drawing state (
kThemeStateActive
or
kThemeStateInactive
) to the function
DrawThemeEditTextFrame
.
DrawThemeEditTextFrame
draws the frame appropriately for the activity state and the current theme. And, when a theme switch occurs, the frame automatically takes on a look consistent with the current theme.

__Listing 3-5__  

Drawing a control user pane that is theme-compliant

`

static pascal void MyClassicEditTextFrameControlUserPaneDrawProc (
                                                    ControlHandle control,
                                                    SInt16 /* part */)
{
    Rect contrlRect = (**control).contrlRect;
    InsetRect (&contrlRect,-1,-1);
    // We're pre-Appearance Mgr here, so always draw in black...
    PenNormal ( );
    // unless the control part code value in contrlHilite indicates
    // that the control is inactive (or disabled); if so, draw in gray
    if ((**control).contrlHilite >= 254)
        PenPat (&(qd.gray));
    FrameRect (&contrlRect);
}

static pascal void MyAppearanceSavvyEditTextFrameControlUserPaneDrawProc (
                                                    ControlHandle control,
                                                    SInt16 /* part */)
{
    Rect contrlRect = (**control).contrlRect;
    DrawThemeEditTextFrame (&contrlRect,
        ((**control).contrlHilite < 254) ?
        kThemeStateActive : kThemeStateInactive);
}

static pascal void MyEditTextFrameControlUserPaneDrawProc (
                                                    ControlHandle control,
                                                    SInt16 part)
{
    OSStatus err = noErr;

    Boolean haveAppearance;

    if (!(err = MyIsAppearancePresent (&haveAppearance)))
    {
        if (haveAppearance)
            MyAppearanceSavvyEditTextFrameControlUserPaneDrawProc (control, part);
        else
            MyClassicEditTextFrameControlUserPaneDrawProc (control, part);
    }
}`

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.17.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.19.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.1b.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
