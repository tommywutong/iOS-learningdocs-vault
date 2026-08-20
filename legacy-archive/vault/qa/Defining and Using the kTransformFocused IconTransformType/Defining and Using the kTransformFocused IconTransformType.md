---
title: Defining and Using the kTransformFocused IconTransformType
apple_id: DTS10003511
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2005-03-29'
source_url: https://developer.apple.com/library/archive/qa/qa1414/_index.html
archived_at: '2026-07-18T02:30:32.202740Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1414

# Defining and Using the kTransformFocused IconTransformType

## Q:  How can I draw a selected icon with a focus ring like the HIToolbox does in a HIToolbar?

A: How can I draw a selected icon with a focus ring like the HIToolbox does in a HIToolbar?

There is a special IconTransformType value which can be used with PlotIconRefInContext, and only PlotIconRefInContext, in order to get the desired result. This IconTransformType is available in Mac OS X since version 10.3 but is not exported in the headers.

It will be documented in Icons.h in a later release of the Development Tools but you can start using it right now by defining it yourself:

__Listing 1__  Defining the kTransformFocused IconTransformType.

```
enum     {     kTransformFocused = 0x8000     };
```

Then you just use this IconTransformType like any other as in the sample code extract below:

__Listing 2__  Using the kTransformFocused IconTransformType.

```
IconRef iconRef; status = GetIconRef(kOnSystemDisk, kSystemIconsCreator, kGenericApplicationIcon, &iconRef); require_noerr(status, bail);  status = PlotIconRefInContext(                 context, &iconRect, kAlignNone, kTransformNone,                 &color, kPlotIconRefNormalFlags, iconRef); require_noerr(status, bail);  iconRect = CGRectOffset(iconRect, 160, 0); status = PlotIconRefInContext(                 context, &iconRect, kAlignNone, kTransformFocused,                 &color, kPlotIconRefNormalFlags, iconRef); require_noerr(status, bail);
```

And this code should draw the following icons:

__Figure 1__  Generic Application Icon Non-Selected and Selected.

!

However, if the icon is clipped, for example by its parent view (see Figure 2 and Figure 3), then the focus ring will be partly drawn outside the clip area, leaving an undesired graphic artifact (in this example, at the bottom of the icon). This is a purely cosmetic bug and is a known problem.

__Figure 2__  Icons clipped by the parent view.

!

__Figure 3__  Magnified icon with its artifacts.

!

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-03-29 | New document that documents a new IconTransformType, available in Panther and later, which draws a focus ring around an icon. |

