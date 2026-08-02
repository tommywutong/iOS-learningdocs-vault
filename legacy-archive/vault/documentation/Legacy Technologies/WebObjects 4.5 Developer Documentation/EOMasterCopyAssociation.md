---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOMasterCopyAssociation.html
archived_at: '2026-07-15T08:11:44.860909Z'
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
> : [EOAssociation](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuc43tn5rwsylunfxw4) : EODelayedObserver (EOControl)
> : NSObject

> **__Implements:__**
> : EOObserving (EODelayedObserver)

> **__Package:__**
> : com.apple.yellow.eointerface

---

## Class Description

---

An EOMasterCopyAssociation object synchronizes two EODisplayGroups
that share the same data source but have different qualifiers.

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.client.eointerface package. |

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
select the `parent` aspect, and click Connect.
This action automatically sets the second display group's data
source. Initially, the data source is set to an EODetailDataSource-that's
what you'll see in Interface Builder. However, at runtime, the
association switches the second display group's data source to
that of the `parent` display group.

Now when you run the application, the display groups will
be synchronized with one another. (You'll programmatically assign
a qualifier to the second display group so that it filters out non-actor
Talents.)

## Constructors

---

### EOMasterCopyAssociation

`public EOMasterCopyAssociation(Object  aDisplayObject)`

Creates a new EOMasterCopyAssociation to monitor
and update the value in  _aDisplayObject,_
an EODisplayGroup.

You normally set up associations with the
Interface Builder application, in which case you don't need to
create them programmatically. However, if you do create them up
programmatically, setting them up is a multi-step process. After
creating an association, you must bind its aspects and establish
its connections.

__See Also:__  [bindAspect](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwe2lomraxg4dfmn2a) (EOAssociation), [establishConnection](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk43umfrgy2ltnbbw63tomvrxi2lpny) (EOAssociation)

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
