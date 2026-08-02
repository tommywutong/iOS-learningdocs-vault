---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/dc/CompositePage.html
archived_at: '2026-07-15T07:23:26.413326Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| dc.h | dc.h | dc.h | dc.h | dc.h |

|  |  |
| --- | --- |
| __Includes:__ | "wx/object.h"  "wx/cursor.h"  "wx/font.h"  "wx/colour.h"  "wx/brush.h"  "wx/pen.h"  "wx/palette.h"  ["wx/list.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/list/index.html#//apple_ref/doc/header/list.h)  "wx/dynarray.h"  ["wx/msw/dc.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/dc/index.html#//apple_ref/doc/header/dc.h)  ["wx/motif/dc.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/dc/index.html#//apple_ref/doc/header/dc.h)  ["wx/gtk/dc.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/dc/index.html#//apple_ref/doc/header/dc.h)  ["wx/x11/dc.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/dc/index.html#//apple_ref/doc/header/dc.h)  ["wx/mgl/dc.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/dc/index.html#//apple_ref/doc/header/dc.h)  ["wx/mac/dc.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/dc/index.html#//apple_ref/doc/header/dc.h)  ["wx/cocoa/dc.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/dc/index.html#//apple_ref/doc/header/dc.h)  ["wx/os2/dc.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/dc/index.html#//apple_ref/doc/header/dc.h)  ["wx/mac/classic/dc.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/dc/index.html#//apple_ref/doc/header/dc.h)  ["wx/mac/carbon/dc.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/dc/index.html#//apple_ref/doc/header/dc.h)  "wx/pen.h"  "wx/brush.h"  "wx/icon.h"  "wx/font.h"  "wx/gdicmn.h" |

## Introduction

---

## Functions

**[DrawEllipticArcRot](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2eojqxorlmnruxa5djmnaxey2sn52a)**
:

**[Rotate](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2sn52gc5df)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DrawEllipticArcRot | DrawEllipticArcRot | DrawEllipticArcRot | DrawEllipticArcRot | DrawEllipticArcRot |

---

```
void DrawEllipticArcRot(
    wxCoord x,
    wxCoord y,
    wxCoord width,
    wxCoord height,
    double sa = 0,
    double ea = 0,
    double angle = 0 )
```

##### Discussion

\param x Upper left corner of bounding box.
\param y Upper left corner of bounding box.
\param w Width of bounding box.
\param h Height of bounding box.
\param sa Starting angle of arc
(counterclockwise, start at 3 o'clock, 360 is full circle).
\param ea Ending angle of arc.
\param angle Rotation angle, the Arc will be rotated after
calculating begin and end.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Rotate | Rotate | Rotate | Rotate | Rotate |

---

```
void Rotate(
    wxList*points,
    double angle,
    wxPoint center = wxPoint() );
```

##### Discussion

This is a quite straight method, it calculates in pixels
and so it produces rounding errors.
\param points The points inside will be rotated.
\param angle Rotating angle (counterclockwise, start at 3 o'clock, 360 is full circle).
\param center Center of rotation.

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Last Updated: 2006-06-20
