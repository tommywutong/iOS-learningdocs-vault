---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/ObjC_classic/Classes/EOMasterDetailAssociation.html
archived_at: '2026-07-15T08:11:45.522104Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md) 

# EOMasterDetailAssociation

> **__Inherits
> from:__**
> : [EOAssociation](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwyl2fj5axg43pmnuwc5djn5xa) : EODelayedObserver (EOControl) : NSObject

> **__Conforms to:__**
> : NSCoding
> : (EOAssociation)
> : EOObserving (EODelayedObserver)
> : NSObject (NSObject)

> __Declared in:__ : EOInterface/EOMasterDetailAssociation.h

---

## Class Description

---

An EOMasterDetailAssociation object binds one EODisplayGroup
(the detail) to a relationship in another (the master), so that
the detail display group contains the destination objects for the
object selected in the master. The display groups' data sources
also operate in a master-detail arrangement, meaning changes to
one are immediately reflected in the other. In this arrangement,
the detail EODisplayGroup's data source must be an EODetailDataSource.
The detail objects are taken directly from the selected object in
the master EODisplayGroup, so that changes to the objects in one EODisplayGroup
are instantly reflected in the other.

In Yellow Box, by contrast, with an EOMasterPeerAssociation,
the two EODisplayGroups are independent of each other (EOMasterPeerAssociation
is not a Java Client class). In a master-peer setup, insertions
and deletions in the detail EODisplayGroup don't affect the corresponding
relationship property of the selected object in the master EODisplayGroup.
Master-peer setups are more appropriate when no insertions or deletions
will be made in the detail EODisplayGroup. See the EOMasterPeerAssociation
class specification for more information.

|  |
| --- |
| __Usable With__ |
| EODisplayGroups whose data sources are EODetailDataSources |

|  |
| --- |
| __Aspects__ |
| parent | A relationship from the master EODisplayGroup. |

## Example

Suppose you have a master EODisplayGroup displaying Movie
objects and a detail display group displaying Talent objects. The
two display groups are bound to one another through Movie's __directors__ relationship-a
to-many relationship from Movie to Talent. When a Movie is selected,
you want the Talent display group to display the Talents who directed
the Movie. Inserting a new director into the Talent display group
should add the director to the selected Movie's __directors__ relationship;
and similarly, deleting a director from the Talent display group
should remove the director from the selected Movie's __directors__ relationship.

To do this, in Interface Builder, control-drag a connection
from the Talent display group to the Movie display group. In the
Connections inspector, choose EOMasterDetailAssociation, and bind __parent__ aspect
to the "directors" key.

## Instance Methods

---

### priority

`- (EOObserverPriority)priority`

Returns EOObserverPrioritySecond (one notch
above the default priority). This guarantees that changes in the
master are propagated to the detail before any other updates are
made.

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
