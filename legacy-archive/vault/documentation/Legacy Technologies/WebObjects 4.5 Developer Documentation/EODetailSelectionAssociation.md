---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EODetailSelectionAssoc.html
archived_at: '2026-07-15T08:11:44.665550Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

# EODetailSelectionAssociation

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

An EODetailSelectionAssociation binds two EODisplayGroups
together through a relationship, so that the destination display
group acts as an editor for that relationship.

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.client.eointerface package. |

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
in the Connections inspector, and bind the `selectedObjects` aspect
to the "projects" key.

## Constructors

---

### EODetailSelectionAssociation

`public EODetailSelectionAssociation(Object  aDisplayObject)`

Creates a new EODetailSelectionAssociation to
monitor and update the value in  _aDisplayObject,_
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
