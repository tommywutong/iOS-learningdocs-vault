---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface/Classes/EOMasterPeerAssociation.html
archived_at: '2026-07-15T08:13:55.297004Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface/Art/up.gif)](../../EOInterfaceTOC.md)

# EOMasterPeerAssociation

> **__Inherits from:__**
> : [EOMasterDetailAssociation](EOMasterDetailAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhu2yltorsxerdforqws3cbonzw6y3jmf2gs33o) : [EOMasterAssociation](EOMasterAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhu2yltorsxeqltonxwg2lboruw63q) : [EOAssociation](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuc43tn5rwsylunfxw4) : EODelayedObserver (EOControl) : Object

> **__Implements:__**
> : NSDisposable: EOObserving (EOControl)

> **__Package:__**
> : com.webobjects.eointerface

---

## Class Description

---

An EOMasterPeerAssociation binds two EODisplayGroups together in a master-detail relationship, where the detail EODisplayGroup shows the destination objects for the relationship of the master EODisplayGroup.

In a master-peer arrangement, the detail display group's data source is independent. Detail objects are fetched independently from the detail's data source, which means that changes to one display group aren't automatically reflected in the other. To update the other display group, it's necessary to save the changes made and then have the other display group fetch its objects anew.

Contrast this with a master-detail setup using an EOMasterDetailAssociation. With an EOMasterDetailAssociation, the display groups' data sources also operate in a master-detail arrangement, meaning changes to one are immediately reflected in the other. The detail objects are taken directly from the selected object in the master display group, so that changes to the objects in one display group are instantly reflected in the other. Master-peer setups display these advantages over master-detail setups:

- You can use them to display the destination objects for relationships that are defined in the model but not declared as class properties. This is typically done for rarely accessed information-or information that's costly to access. By not defining the relationship as a class property, the destination objects aren't stored as instance variables in the source objects, which saves memory and the cost of constructing faults for the relationship.
- Because the detail display group fetches objects with its own data source, you can configure the detail data source with an auxiliary EOQualifier to limit the objects fetched. This further reduces the cost of fetching data.
- You can use an EOMasterPeerAssociation to fetch detail information that may be updated in another editing context or even in another application; thus this association helps you to remain "up to date" with the database.

Generally, master-peer setups are only appropriate when no insertions or deletions will be made in the detail display group. For a master-detail relationship that reflects changes between two display groups, including insertions and deletions, use an EOMasterDetailAssociation.

|  |
| --- |
| __Usable With__ |
| EODisplayGroups whose data sources are not EODetailDataSources |

|  |
| --- |
| __Aspects__ |
| `parent` | A relationship from the master EODisplayGroup. |

|  |
| --- |
| __Object Keys Taken__ |
| None |

## Example

Suppose you have a database of salesmen and their associated sales. Each salesman has a city ID. The sales are related to the salesmen by salesman ID, but also have a city ID. You want a list of all the sales in a salesman's city so you could evaluate it against other salesmen. For this, you create a relationship between salesman and sales based on city ID (the relationship is not a class property). You can then display that information using an EOMasterPeerAssociation.

## Interfaces Implemented

---

> : NSDisposable:
>
> : EOObserving:

## Method Types

---

> **All methods**
>
> : [EOMasterPeerAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvqxg5dfojigkzlsifzxg33dnfqxi2lpnyxukt2nmfzxizlskbswk4sbonzw6y3jmf2gs33o): [isUsableWithObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvqxg5dfojigkzlsifzxg33dnfqxi2lpnyxws42vonqwe3dfk5uxi2cpmjvgky3u)

## Constructors

---

### EOMasterPeerAssociation

`public EOMasterPeerAssociation(Object anObject)`

Description forthcoming.

---

## Instance Methods

---

### isUsableWithObject

`public boolean isUsableWithObject(Object anObject)`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 21, 2001)

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface/Art/up.gif)](../../EOInterfaceTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
