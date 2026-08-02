---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface/Classes/EOMasterDetailAssociation.html
archived_at: '2026-07-15T08:13:55.283219Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface/Art/up.gif)](../../EOInterfaceTOC.md)

# EOMasterDetailAssociation

> **__Inherits from:__**
> : [EOMasterAssociation](EOMasterAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhu2yltorsxeqltonxwg2lboruw63q) : [EOAssociation](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuc43tn5rwsylunfxw4) : EODelayedObserver (EOControl) : Object

> **__Implements:__**
> : NSDisposable: EOObserving (EOControl)

> **__Package:__**
> : com.webobjects.eointerface

---

## Class Description

---

An EOMasterDetailAssociation object binds one EODisplayGroup (the detail) to a relationship in another (the master), so that the detail display group contains the destination objects for the object selected in the master. The display groups' data sources also operate in a master-detail arrangement, meaning changes to one are immediately reflected in the other. In this arrangement, the detail EODisplayGroup's data source must be an EODetailDataSource. The detail objects are taken directly from the selected object in the master EODisplayGroup, so that changes to the objects in one EODisplayGroup are instantly reflected in the other.

In com.webobjects.eointerface.cocoa, by contrast, with an EOMasterPeerAssociation, the two EODisplayGroups are independent of each other. In a master-peer setup, insertions and deletions in the detail EODisplayGroup don't affect the corresponding relationship property of the selected object in the master EODisplayGroup. Master-peer setups are more appropriate when no insertions or deletions will be made in the detail EODisplayGroup. See the EOMasterPeerAssociation class specification for more information.

## Example

Suppose you have a master EODisplayGroup displaying Movie objects and a detail display group displaying Talent objects. The two display groups are bound to one another through Movie's __directors__ relationship-a to-many relationship from Movie to Talent. When a Movie is selected, you want the Talent display group to display the Talents who directed the Movie. Inserting a new director into the Talent display group should add the director to the selected Movie's __directors__ relationship; and similarly, deleting a director from the Talent display group should remove the director from the selected Movie's __directors__ relationship.

To do this, in Interface Builder, control-drag a connection from the Talent display group to the Movie display group. In the Connections inspector, choose EOMasterDetailAssociation, and bind __parent__ aspect to the "directors" key.

## Interfaces Implemented

---

> : NSDisposable
>
> : [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvqxg5dfojcgk5dbnfwec43tn5rwsylunfxw4l3enfzxa33tmu)
>
> :
>
> : EOObserving:

## Method Types

---

> **All methods**
>
> : [EOMasterDetailAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvqxg5dfojcgk5dbnfwec43tn5rwsylunfxw4l2fj5gwc43umvzeizlumfuwyqltonxwg2lboruw63q): [isUsableWithObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvqxg5dfojcgk5dbnfwec43tn5rwsylunfxw4l3jonkxgylcnrsvo2lunbhwe2tfmn2a): [subjectChanged](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvqxg5dfojcgk5dbnfwec43tn5rwsylunfxw4l3tovrguzldorbwqylom5swi)

## Constructors

---

### EOMasterDetailAssociation

`public EOMasterDetailAssociation(Object aDisplayObject)`

Creates a new EOMasterDetailAssociation to monitor and update the value in _aDisplayObject_, an EODisplayGroup.

You normally set up associations with the Interface Builder application, in which case you don't need to create them programmatically. However, if you do create them up programmatically, setting them up is a multi-step process. After creating an association, you must bind its aspects and establish its connections.

__See Also:__ bindAspect (EOAssociation), establishConnection (EOAssociation)

---

## Instance Methods

---

### dispose

`public void dispose()`

See the description in the documentation for NSDisposable.

---

### isUsableWithObject

`public boolean isUsableWithObject(Object aDisplayObject)`

Returns `true` if _aDisplayObject_ is an instance of EODisplayGroup and its dataSource is either `null` or an EODetailDataSource (EOControl).

__See Also:__ isUsableWithObject (EOAssociation)

---

### subjectChanged

`public void subjectChanged()`

See the subjectChanged method description in the superclass EOAssociation.

---

© 2001 Apple Computer, Inc. (Last Published April 21, 2001)

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface/Art/up.gif)](../../EOInterfaceTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
