---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/ObjC_classic/Classes/EODetailSelectionAssoc.html
archived_at: '2026-07-15T08:11:45.424501Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md) 

# EODetailSelectionAssociation

> **__Inherits
> from:__**
> : [EOAssociation](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwyl2fj5axg43pmnuwc5djn5xa) : EODelayedObserver (EOControl) : NSObject

> **__Conforms to:__**
> : NSCoding
> : (EOAssociation)
> : EOObserving (EODelayedObserver)
> : NSObject (NSObject)

> __Declared in:__ : EOInterface/EODetailSelectionAssociation.h

---

## Class Description

---

An EODetailSelectionAssociation binds two EODisplayGroups
together through a relationship, so that the destination display
group acts as an editor for that relationship.

The destination display group shows all possible values for
the relationship and indicates the actual members of the relationship
by selecting them. The user can change the objects included in the relationship
of the source by selecting and deselecting them in the destination.

EODetailSelectionAssociation is a useful alternative to EOMasterDetailAssociation
and EOMasterPeerAssociation when it's more important to add and
remove objects from a relationship than it is to edit the attributes
of those objects.

|  |
| --- |
| __Usable With__ |
| EODisplayGroup |

|  |
| --- |
| __Aspects__ |
| selectedObjects | A relationship from objects in the source EODisplayGroup. |

|  |
| --- |
| __Object Keys Taken__ |
| None |

## Example

Suppose that an employee can be assigned any number of projects.
Your application displays employees in one table view and projects
in another. When an employee is selected in the first table view,
the employee's assigned projects are selected in the other. To
change the employee's project assignments, a user changes the
selection in the project table view: to add a project to the set,
the user selects it, and to remove a project from the set, the user
deselects it. To do this, in Interface Builder control-drag a connection
from the Projects display group to the Employee display group. Choose EODetailSelectionAssociation
in the Connections inspector, and bind the __selectedObjects__ aspect
to the "projects" key.

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
