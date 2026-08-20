---
title: Using PPD constraints with Paper Sizes
apple_id: DTS40007920
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: null
published: '2008-08-08'
source_url: https://developer.apple.com/library/archive/qa/qa1603/_index.html
archived_at: '2026-07-18T02:32:24.302573Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1603

# Using PPD constraints with Paper Sizes

## Q:  When I create a UIConstraint against PageSize it only works some of the time. Why?

A: When I create a UIConstraint against PageSize it only works some of the time. Why?

When a UIConstraint is checked by the printing system, there are two keywords that are checked, PageSize and PageRegion. If you only constrain against PageSize, then it will appear as if it is possible to get an invalid pair of constraints if you set the options in certain orders. If you constrain to both then you will always get a consistent experience. An example of correctly constraining the print tray with the paper size, is shown below.

__Listing 1__  Constraining the print tray and the paper size

```
*% Tray2 cannot hold Legal paper *UIConstraints: *InputSlot Tray2          *PageSize Legal *UIConstraints: *PageSize Legal           *InputSlot Tray2 *% Additionally constrain the PageRegion. *UIConstraints: *InputSlot Tray2          *PageRegion Legal *UIConstraints: *PageRegion Legal         *InputSlot Tray2
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-08-08 | New document that describes the requirements for using PPD Constraints to constrain options against paper size. |

