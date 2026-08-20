---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOApplicationRef/Java/Interfaces/EOObjectDisplay.html
archived_at: '2026-07-15T08:13:43.316711Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# EOObjectDisplay

> __Implemented by:__ : [EOEntityController](EOEntityController.md#apple-ijbesskgjjeug):

> **__Package:__**
> : com.webobjects.eoapplication

---

## Interface Description

---

EOObjectDisplay is an interface that defines the behavior of a controller that displays enterprise objects using an EODisplayGroup.

## Instance Methods

---

### controllerDisplayGroup

`public abstract com.webobjects.eointerface.EODisplayGroup controllerDisplayGroup()`

Returns a display group containing the receiver-an EOController or subclass. This display group can be used to connect controller methods to the user interface.

---

### displayGroup

`public abstract com.webobjects.eointerface.EODisplayGroup displayGroup()`

Returns the display group the receiver uses to display and edit the properties of its enterprise objects.

---

### editingContext

`public abstract com.webobjects.eocontrol.EOEditingContext editingContext()`

Returns the editing context the receiver uses to manage the graph of its enterprise objects.

---

### entityName

`public abstract String entityName()`

Returns the name of the entity that describes the enterprise objects the receiver displays with its display group.

---

© 2001 Apple Computer, Inc. (Last Published April 14, 2001)

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
