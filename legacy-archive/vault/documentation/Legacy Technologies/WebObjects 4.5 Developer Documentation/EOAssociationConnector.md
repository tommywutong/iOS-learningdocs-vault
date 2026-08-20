---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOApplication.framework/Java/Interfaces/EOAssociationConnector.html
archived_at: '2026-07-15T08:11:36.879767Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOApplication Reference

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

# EOAssociationConnector

> __Implemented by:__ : EOAssociationController,
> : EOEntityController,
> : EORangeValueController,
> : EOTableController

> **__Package:__**
> : com.apple.client.eoapplication

---

## Interface Description

---

EOAssociationConnector is
an interface that defines an object that can assume the responsibilities
for connecting and disconnecting the associations of a transient
subcontroller.

## Instance Methods

---

### takeResposibilityForConnectionOfAssociation

`public abstract void takeResposibilityForConnectionOfAssociation(com.apple.client.eointerface.EOAssociation association)`

Invoked when one of the receiver's
subcontrollers is disposed as a transient controller. This
method instructs the receiver to assume responsibility for managing
the subcontroller's EOAssociation, _association_.

---

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

__DRAFT__
