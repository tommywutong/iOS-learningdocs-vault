---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface/Classes/EOMasterCopyAssociation.html
archived_at: '2026-07-15T08:13:55.267229Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface/Art/up.gif)](../../EOInterfaceTOC.md)

# EOMasterCopyAssociation

> **__Inherits from:__**
> : [EOMasterAssociation](EOMasterAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhu2yltorsxeqltonxwg2lboruw63q) : [EOAssociation](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuc43tn5rwsylunfxw4) : EODelayedObserver (EOControl) : Object

> **__Implements:__**
> : NSDisposable: EOObserving (EOControl)

> **__Package:__**
> : com.webobjects.eointerface

---

## Class Description

---

An EOMasterCopyAssociation object synchronizes two EODisplayGroups that share the same data source but have different qualifiers.

By binding two display groups with an EOMasterCopyAssociation, any changes performed in one display group are immediately reflected in the other. Similarly, changing the selection in one display group immediately changes it in the other one.

|  |
| --- |
| __Usable With__ |
| EODisplayGroup |

|  |
| --- |
| __Aspects__ |
| `parent` | An EODisplayGroup with which the association's display group should be synchronized. |

|  |
| --- |
| __Object Keys Taken__ |
| None |  |

## Examples

Suppose you have an EODisplayGroup for displaying Talent objects (actors and directors) and another display group for displaying the pictures of the Talents who are actors. When a Talent is selected in the first display group, you want the "actor" display group to select that Talent's picture if the selected Talent is an actor. Since both display groups manage Talent objects, they can share the same EODataSource. However, the first display group is unqualified-it fetches all Talent objects; the second display group is qualified to fetch only the Talents who are actors.

To do this, in Interface Builder, start with an unqualified display group for displaying all the Talents. Drag a second display group from the Enterprise Objects palette into your nib. Control-drag a connection from the new display group to the unqualified Talent display group. In the Connections inspector, choose EOMasterCopyAssociation, select the __parent__ aspect, and click Connect. This action automatically sets the second display group's data source. Initially, the data source is set to an EODetailDataSource-that's what you'll see in Interface Builder. However, at runtime, the association switches the second display group's data source to that of the __parent__ display group.

Now when you run the application, the display groups will be synchronized with one another. (You'll programmatically assign a qualifier to the second display group so that it filters out non-actor Talents.)

## Interfaces Implemented

---

> : NSDisposable:
>
> : EOObserving:

## Method Types

---

> **All methods**
>
> : [EOMasterCopyAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvqxg5dfojbw64dzifzxg33dnfqxi2lpnyxukt2nmfzxizlsinxxa6kbonzw6y3jmf2gs33o): [subjectChanged](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvqxg5dfojbw64dzifzxg33dnfqxi2lpnyxxg5lcnjswg5cdnbqw4z3fmq)

## Constructors

---

### EOMasterCopyAssociation

`public EOMasterCopyAssociation(Object aDisplayObject)`

Creates a new EOMasterCopyAssociation to monitor and update the value in _aDisplayObject_, an EODisplayGroup.

You normally set up associations with the Interface Builder application, in which case you don't need to create them programmatically. However, if you do create them up programmatically, setting them up is a multi-step process. After creating an association, you must bind its aspects and establish its connections.

__See Also:__ bindAspect (EOAssociation), establishConnection (EOAssociation)

---

## Instance Methods

---

### subjectChanged

`public void subjectChanged()`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 21, 2001)

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface/Art/up.gif)](../../EOInterfaceTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
