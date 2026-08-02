---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/NSMutableArrayAdditions.html
archived_at: '2026-07-15T08:11:42.161728Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# NSMutableArray Additions

> __Category
> of:__ NSMutableArray

> __Declared in:__ : EOControl/EOSortOrdering.h

---

## Category Description

---

Enterprise Objects Framework adds one method for sorting its
elements according to a series of EOSortOrderings.

## Instance Methods

---

### sortUsingKeyOrderArray:

`- (void)sortUsingKeyOrderArray:(NSArray
*)orderings`

Sorts the objects of the receiver according
to the EOSortOrderings in _orderings_.
The objects are compared by extracting the sort properties using
the added NSObject method __valueForKey:__ and sending
them __compare:__ messages.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
