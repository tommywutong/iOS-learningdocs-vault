---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOMasterDetailAssociation.html
archived_at: '2026-07-18T01:28:46.307172Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOMasterCopyAssociation-2.md)
[!](EOMasterPeerAssociation-2.md)

---

# EOMasterDetailAssociation

__Inherits From:__
EOAssociation : EODelayedObserver (EOControl) : NSObject

__Conforms To:__
NSCoding (EOAssociation)
EOObserving (EODelayedObserver)
NSObject (NSObject)

__Declared in:__
EOInterface/EOMasterDetailAssociation.h

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

[!](EOMasterCopyAssociation-2.md)
[!](EOMasterPeerAssociation-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
