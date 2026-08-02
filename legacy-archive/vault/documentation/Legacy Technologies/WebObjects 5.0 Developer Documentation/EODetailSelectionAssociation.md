---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface/Classes/EODetailSelectionAssociat.html
archived_at: '2026-07-15T08:13:55.188262Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface/Art/up.gif)](../../EOInterfaceTOC.md)

# EODetailSelectionAssociation

> **__Inherits from:__**
> : [EOAssociation](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuc43tn5rwsylunfxw4) : EODelayedObserver (EOControl) : Object

> **__Implements:__**
> : NSDisposable: EOObserving (EOControl)

> **__Package:__**
> : com.webobjects.eointerface

---

## Class Description

---

An EODetailSelectionAssociation binds two EODisplayGroups together through a relationship, so that the destination display group acts as an editor for that relationship.

The destination display group shows all possible values for the relationship and indicates the actual members of the relationship by selecting them. The user can change the objects included in the relationship of the source by selecting and deselecting them in the destination.

EODetailSelectionAssociation is a useful alternative to EOMasterDetailAssociation and EOMasterPeerAssociation when it's more important to add and remove objects from a relationship than it is to edit the attributes of those objects.

|  |
| --- |
| __Usable With__ |
| EODisplayGroup |

|  |
| --- |
| __Aspects__ |
| `selectedObjects` | A relationship from objects in the source EODisplayGroup. |

|  |
| --- |
| __Object Keys Taken__ |
| None |

## Example

Suppose that an employee can be assigned any number of projects. Your application displays employees in one table view and projects in another. When an employee is selected in the first table view, the employee's assigned projects are selected in the other. To change the employee's project assignments, a user changes the selection in the project table view: to add a project to the set, the user selects it, and to remove a project from the set, the user deselects it. To do this, in Interface Builder control-drag a connection from the Projects display group to the Employee display group. Choose EODetailSelectionAssociation in the Connections inspector, and bind the __selectedObjects__ aspect to the "projects" key.

## Interfaces Implemented

---

> : NSDisposable:
>
> : EOObserving:

## Method Types

---

> **All methods**
>
> : [EODetailSelectionAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrjwk3dfmn2gs33oifzxg33dnfqxi2lpnyxukt2emv2gc2lmknswyzldoruw63sbonzw6y3jmf2gs33o): [isUsableWithObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrjwk3dfmn2gs33oifzxg33dnfqxi2lpnyxws42vonqwe3dfk5uxi2cpmjvgky3u): [primaryAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrjwk3dfmn2gs33oifzxg33dnfqxi2lpnyxxa4tjnvqxe6kbonygky3u): [subjectChanged](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrjwk3dfmn2gs33oifzxg33dnfqxi2lpnyxxg5lcnjswg5cdnbqw4z3fmq)

## Constructors

---

### EODetailSelectionAssociation

`public EODetailSelectionAssociation(Object aDisplayObject)`

Creates a new EODetailSelectionAssociation to monitor and update the value in _aDisplayObject_, an EODisplayGroup.

You normally set up associations in Interface Builder, in which case you don't need to create them programmatically. However, if you do create them up programmatically, setting them up is a multi-step process. After creating an association, you must bind its aspects and establish its connections.

__See Also:__ bindAspect (EOAssociation), establishConnection (EOAssociation)

---

## Instance Methods

---

### isUsableWithObject

`public boolean isUsableWithObject(Object anObject)`

Description forthcoming.

---

### primaryAspect

`public String primaryAspect()`

Returns EOAssociation.SourceAspect.

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
