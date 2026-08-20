---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/ObjC_classic/Classes/EOMasterPeerAssociation.html
archived_at: '2026-07-15T08:11:45.536902Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md) 

# EOMasterPeerAssociation

> **__Inherits
> from:__**
> : [EOMasterDetailAssociation](EOMasterDetailAssociation.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwyl2fj5gwc43umvzeizlumfuwyqltonxwg2lboruw63q) : [EOAssociation](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwyl2fj5axg43pmnuwc5djn5xa) : EODelayedObserver (EOControl) : NSObject

> **__Conforms to:__**
> : NSCoding
> : (EOAssociation)
> : EOObserving (EODelayedObserver)
> : NSObject (NSObject)

> __Declared in:__ : EOInterface/EOMasterDetailAssociation.h

---

## Class Description

---

An EOMasterPeerAssociation binds two EODisplayGroups together
in a master-detail relationship, where the detail EODisplayGroup
shows the destination objects for the relationship of the master EODisplayGroup.

In a master-peer arrangement, the detail display group's
data source is independent. Detail objects are fetched independently
from the detail's data source, which means that changes to one
display group aren't automatically reflected in the other. To
update the other display group, it's necessary to save the changes
made and then have the other display group fetch its objects anew.

Contrast this with a master-detail setup using an EOMasterDetailAssociation.
With an EOMasterDetailAssociation, the display groups' data sources
also operate in a master-detail arrangement, meaning changes to
one are immediately reflected in the other. The detail objects are taken
directly from the selected object in the master display group, so
that changes to the objects in one display group are instantly reflected
in the other. Master-peer setups display these advantages over master-detail
setups:

- You can use them to display the destination objects
  for relationships that are defined in the model but not declared
  as class properties. This is typically done for rarely accessed
  information-or information that's costly to access. By not defining
  the relationship as a class property, the destination objects aren't
  stored as instance variables in the source objects, which saves
  memory and the cost of constructing faults for the relationship.
- Because the detail display group fetches objects with its
  own data source, you can configure the detail data source with an
  auxiliary EOQualifier to limit the objects fetched. This further
  reduces the cost of fetching data.
- You can use an EOMasterPeerAssociation to fetch detail information
  that may be updated in another editing context or even in another
  application; thus this association helps you to remain "up to
  date" with the database.

Generally, master-peer setups are only appropriate when no
insertions or deletions will be made in the detail display group.
For a master-detail relationship that reflects changes between two
display groups, including insertions and deletions, use an EOMasterDetailAssociation.

|  |
| --- |
| __Usable With__ |
| EODisplayGroups whose data sources are not EODetailDataSources |

|  |
| --- |
| __Aspects__ |
| parent | A relationship from the master EODisplayGroup. |

|  |
| --- |
| __Object Keys Taken__ |
| None |

## Example

Suppose you have a database of salesmen and their associated
sales. Each salesman has a city ID. The sales are related to the
salesmen by salesman ID, but also have a city ID. You want a list
of all the sales in a salesman's city so you could evaluate it
against other salesmen. For this, you create a relationship between
salesman and sales based on city ID (the relationship is not a class
property). You can then display that information using an EOMasterPeerAssociation.

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
