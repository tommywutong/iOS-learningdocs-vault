---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/ObjC_classic/Classes/EOMasterCopyAssociation.html
archived_at: '2026-07-15T08:11:45.506213Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md) 

# EOMasterCopyAssociation

> **__Inherits
> from:__**
> : [EOAssociation](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwyl2fj5axg43pmnuwc5djn5xa) : EODelayedObserver (EOControl) : NSObject

> **__Conforms to:__**
> : NSCoding
> : (EOAssociation)
> : EOObserving (EODelayedObserver)
> : NSObject (NSObject)

> __Declared in:__ : EOInterface/EOMasterCopyAssociation.h

---

## Class Description

---

An EOMasterCopyAssociation object synchronizes two EODisplayGroups
that share the same data source but have different qualifiers.

By binding two display groups with an EOMasterCopyAssociation,
any changes performed in one display group are immediately reflected
in the other. Similarly, changing the selection in one display group
immediately changes it in the other one.

|  |
| --- |
| __Usable With__ |
| EODisplayGroup |

|  |
| --- |
| __Aspects__ |
| parent | An EODisplayGroup with which the association's display group should be synchronized. |

|  |
| --- |
| __Object Keys Taken__ |
| None |  |

## Examples

Suppose you have an EODisplayGroup for displaying Talent objects
(actors and directors) and another display group for displaying
the pictures of the Talents who are actors. When a Talent is selected
in the first display group, you want the "actor" display group
to select that Talent's picture if the selected Talent is an actor.
Since both display groups manage Talent objects, they can share
the same EODataSource. However, the first display group is unqualified-it
fetches all Talent objects; the second display group is qualified
to fetch only the Talents who are actors.

To do this, in Interface Builder, start with an unqualified
display group for displaying all the Talents. Drag a second display
group from the Enterprise Objects palette into your nib. Control-drag
a connection from the new display group to the unqualified Talent
display group. In the Connections inspector, choose EOMasterCopyAssociation,
select the __parent__ aspect, and click Connect.
This action automatically sets the second display group's data
source. Initially, the data source is set to an EODetailDataSource-that's
what you'll see in Interface Builder. However, at runtime, the
association switches the second display group's data source to
that of the __parent__ display group.

Now when you run the application, the display groups will
be synchronized with one another. (You'll programmatically assign
a qualifier to the second display group so that it filters out non-actor
Talents.)

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
