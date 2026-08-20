---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOMasterPeerAssociation.html
archived_at: '2026-07-18T01:28:43.561112Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOMasterDetailAssociation.md)
[!](EOMatrixAssociation.md)

---

# EOMasterPeerAssociation

__Inherits From:__
EOMasterDetailAssociation :
EOAssociation :
EODelayedObserver (EOControl) :
NSObject

EOObserving (EODelayedObserver)

__Inherits From:__
com.apple.yellow.eointerface (Yellow Box)

---

## Class Description

An EOMasterPeerAssociation binds two EODisplayGroups together in a master-detail relationship, where the detail EODisplayGroup shows the destination objects for the relationship of the master EODisplayGroup. It is for use in Yellow Box applications only; there isn't an equivalent class for Java Client.

In a master-peer arrangement, the detail display group's data source is independent. Detail objects are fetched independently from the detail's data source, which means that changes to one display group aren't automatically reflected in the other. To update the other display group, it's necessary to save the changes made and then have the other display group fetch its objects anew.

Contrast this with a master-detail setup using an EOMasterDetailAssociation. With an EOMasterDetailAssociation, the display groups' data sources also operate in a master-detail arrangement, meaning changes to one are immediately reflected in the other. The detail objects are taken directly from the selected object in the master display group, so that changes to the objects in one display group are instantly reflected in the other. Master-peer setups display these advantages over master-detail setups:

- You can use them to display the destination objects for relationships that are defined in the model but not declared as class properties. This is typically done for rarely accessed information-or information that's costly to access. By not defining the relationship as a class property, the destination objects aren't stored as instance variables in the source objects, which saves memory and the cost of constructing faults for the relationship.
- Because the detail display group fetches objects with its own data source, you can configure the detail data source with an auxiliary EOQualifier to limit the objects fetched. This further reduces the cost of fetching data.
- You can use an EOMasterPeerAssociation to fetch detail information that may be updated in another editing context or even in another application; thus this association helps you to remain "up to date" with the database.

Generally, master-peer setups are only appropriate when no insertions or deletions will be made in the detail display group. For a master-detail relationship that reflects changes between two display groups, including insertions and deletions, use an EOMasterDetailAssociation.

| __Usable With__ |
| EODisplayGroups whose data sources are not EODetailDataSources |

```
```

| __Aspects__ | __Aspects__ |
| parent | A relationship from the master EODisplayGroup. |

```
```

| __Object Keys Taken__ |
| None |

```
```


---

## Example

Suppose you have a database of salesmen and their associated sales. Each salesman has a city ID. The sales are related to the salesmen by salesman ID, but also have a city ID. You want a list of all the sales in a salesman's city so you could evaluate it against other salesmen. For this, you create a relationshipo between salesman and sales based on city ID (the relationship is not a class property). You can then display that information using an EOMasterPeerAssociation.

---

## Constructors

public `EOMasterPeerAssociation`(java.lang.Object _aDisplayObject_)

Creates a new EOMasterDetailAssociation to monitor and update the value in _aDisplayObject_, an EODisplayGroup.

You normally set up associations with the Interface Builder application, in which case you don't need to create them programmatically. However, if you do create them up programmatically, setting them up is a multi-step process. After creating an association, you must bind its aspects and establish its connections.

__See also:__
[`bindAspect`](EOAssociation.md#apple-gu2tq) (EOAssociation), [`establishConnection`](EOAssociation.md#apple-gu4dq) (EOAssociation)

---

[!](EOMasterDetailAssociation.md)
[!](EOMatrixAssociation.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
