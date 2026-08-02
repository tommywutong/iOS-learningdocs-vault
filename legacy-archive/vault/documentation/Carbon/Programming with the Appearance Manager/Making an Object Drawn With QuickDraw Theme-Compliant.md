---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.18.html
archived_at: '2026-07-15T05:23:56.518524Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)



__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.17.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.17.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.19.md)

---

#    Making an Object Drawn With QuickDraw Theme-Compliant

[Listing 3-3](#apple-geztqobw)
shows a sample function called
MyEditTextFrameDraw
, which, depending upon the presence of the Appearance Manager, branches between two functions, each of which draws a frame for an editable text field. Prior to drawing, the
MyEditTextFrameDraw
function calls the
MyIsAppearancePresent
function, described in [Becoming a Client of the Appearance Manager](Becoming%20a%20Client%20of%20the%20Appearance%20Manager.md#apple-gqydmnrt)
, to determine whether the Appearance Manager is present.

If the Appearance Manager is not present,
MyEditTextFrameDraw
calls the non-theme-compliant function
MyClassicEditTextFrameDraw
.
MyClassicEditTextFrameDraw
draws a frame by setting the dimensions of the rectangle and its color with calls to QuickDraw. However, an editable text frame drawn in this manner maintains a "fixed" look in any appearance and cannot adapt to theme switches.

If the Appearance Manager is present, however,
MyEditTextFrameDraw
calls the
MyAppearanceSavvyEditTextFrameDraw
function.
MyAppearanceSavvyEditTextFrameDraw
then passes the appropriate Appearance Manager constant for the drawing state (
kThemeStateActive
or
kThemeStateInactive
) to the function
DrawThemeEditTextFrame
.
DrawThemeEditTextFrame
draws the frame appropriately for the activity state and the current theme. And, when a theme switch occurs, the frame automatically takes on a look consistent with the current theme.

__Listing 3-3__  

Moving from QuickDraw to the Appearance Manager

`

static pascal OSStatus MyClassicEditTextFrameDraw (
                                                const Rect *bounds,
                                                Boolean active)
{
    Rect frame = *bounds;
    InsetRect (&frame,-1,-1);
    // We're pre-Appearance Mgr here, so always draw in black...
    PenNormal ( );
    // unless the editable text field is inactive; in that case, draw in gray
    if (!active) PenPat (&(qd.gray));
    FrameRect (&frame);
    return noErr;
}

static pascal OSStatus MyAppearanceSavvyEditTextFrameDraw (
                                                const Rect *bounds,
                                                Boolean active)
{
    DrawThemeEditTextFrame (bounds,
        active ? kThemeStateActive : kThemeStateInactive);
    return noErr;
}

static pascal OSStatus MyEditTextFrameDraw (const Rect *bounds, Boolean active)
{
    OSStatus err = noErr;

    Boolean haveAppearance;

    if (!(err = MyIsAppearancePresent (&haveAppearance)))
    {
        if (haveAppearance)
            err = MyAppearanceSavvyEditTextFrameDraw (bounds, active);
        else
            err = MyClassicEditTextFrameDraw (bounds, active);
    }

    return err;
}`

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.17.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.17.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.19.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
