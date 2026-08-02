---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOMasterDetailAssociation.html
archived_at: '2026-07-18T01:28:43.488421Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOMasterCopyAssociation.md)
[!](EOMasterPeerAssociation.md)

---

# EOMasterDetailAssociation

__Inherits From:__
EOAssociation : .EODelayedObserver (EOControl) : Object (Java Client)
EOAssociation : .EODelayedObserver (EOControl) : NSObject (Yellow Box)

EOObserving (EODelayedObserver)

__Inherits From:__
com.apple.client.eointerface (Java Client)
com.apple.yellow.eointerface (Yellow Box)

---

## Class Description

An EOMasterDetailAssociation object binds one EODisplayGroup (the detail) to a relationship in another (the master), so that the detail display group contains the destination objects for the object selected in the master. The display groups' data sources also operate in a master-detail arrangement, meaning changes to one are immediately reflected in the other. In this arrangement, the detail EODisplayGroup's data source must be an EODetailDataSource. The detail objects are taken directly from the selected object in the master EODisplayGroup, so that changes to the objects in one EODisplayGroup are instantly reflected in the other.

In Yellow Box, by contrast, with an EOMasterPeerAssociation, the two EODisplayGroups are independent of each other (EOMasterPeerAssociation is not a Java Client class). In a master-peer setup, insertions and deletions in the detail EODisplayGroup don't affect the corresponding relationship property of the selected object in the master EODisplayGroup. Master-peer setups are more appropriate when no insertions or deletions will be made in the detail EODisplayGroup. See the EOMasterPeerAssociation class specification for more information.

| __Usable With__ |
| EODisplayGroups whose data sources are EODetailDataSources |

```
```

| __Aspects__ | __Aspects__ |
| parent (Yellow Box)  ParentAspect (Java Client) | A relationship from the master EODisplayGroup. |

```
```


---

## Example

Suppose you have a master EODisplayGroup displaying Movie objects and a detail display group displaying Talent objects. The two display groups are bound to one another through Movie's `directors` relationship-a to-many relationship from Movie to Talent. When a Movie is selected, you want the Talent display group to display the Talents who directed the Movie. Inserting a new director into the Talent display group should add the director to the selected Movie's `directors` relationship; and similarly, deleting a director from the Talent display group should remove the director from the selected Movie's `directors` relationship.

To do this, in Interface Builder, control-drag a connection from the Talent display group to the Movie display group. In the Connections inspector, choose EOMasterDetailAssociation, and bind `parent` aspect to the "directors" key.

---

## Constructors

public `EOMasterDetailAssociation`(java.lang.Object _aDisplayObject_)

Creates a new EOMasterDetailAssociation to monitor and update the value in _aDisplayObject_, an EODisplayGroup.

You normally set up associations with the Interface Builder application, in which case you don't need to create them programmatically. However, if you do create them up programmatically, setting them up is a multi-step process. After creating an association, you must bind its aspects and establish its connections.

__See also:__
[`bindAspect`](EOAssociation.md#apple-gu2tq) (EOAssociation), [`establishConnection`](EOAssociation.md#apple-gu4dq) (EOAssociation)

---

## Instance Methods

---

### priority

- (EOObserverPriority)`priority`

(Yellow Box only) Returns EOObserverPrioritySecond (one notch above the default priority). This guarantees that changes in the master are propagated to the detail before any other updates are made.

---

[!](EOMasterCopyAssociation.md)
[!](EOMasterPeerAssociation.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
