---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOApplication.framework/Java/Interfaces/EOObjectDisplay.html
archived_at: '2026-07-15T08:11:37.001426Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOApplication Reference

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

# EOObjectDisplay

> __Implemented by:__ : [EOEntityController](EOEntityController.md#apple-ijbesskgjjeug)
> :

> **__Package:__**
> : com.apple.client.eoapplication

---

## Interface Description

---

EOObjectDisplay is
an interface that defines the behavior of a controller that displays
enterprise objects using an EODisplayGroup.

## Instance Methods

---

### controllerDisplayGroup

`public abstract com.apple.client.eointerface.EODisplayGroup controllerDisplayGroup()`

Returns a display group containing
the receiver-an EOController or subclass. This
display group can be used to connect controller methods to the user
interface.

---

### displayGroup

`public abstract com.apple.client.eointerface.EODisplayGroup displayGroup()`

Returns the display group the
receiver uses to display and edit the properties of its enterprise
objects.

---

### editingContext

`public abstract com.apple.client.eocontrol.EOEditingContext editingContext()`

Returns the editing context
the receiver uses to manage the graph of its enterprise objects.

---

### entityName

`public abstract String entityName()`

Returns the name of the entity
that describes the enterprise objects the receiver displays with
its display group.

---

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

__DRAFT__
