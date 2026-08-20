---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOApplicationRef/Java/Interfaces/EOAssociationConnector.html
archived_at: '2026-07-15T08:13:43.184736Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# EOAssociationConnector

> __Implemented by:__ : EOAssociationController,: EOEntityController,: EORangeValueController,: EOTableController

> **__Package:__**
> : com.webobjects.eoapplication

---

## Interface Description

---

EOAssociationConnector is an interface that defines an object that can assume the responsibilities for connecting and disconnecting the associations of a transient subcontroller.

## Instance Methods

---

### takeResposibilityForConnectionOfAssociation

`public abstract void takeResposibilityForConnectionOfAssociation(com.webobjects.eointerface.EOAssociation association)`

Invoked when one of the receiver's subcontrollers is disposed as a transient controller. This method instructs the receiver to assume responsibility for managing the subcontroller's EOAssociation, _association_.

---

© 2001 Apple Computer, Inc. (Last Published April 14, 2001)

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
