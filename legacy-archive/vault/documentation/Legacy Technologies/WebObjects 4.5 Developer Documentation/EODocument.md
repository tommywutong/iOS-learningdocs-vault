---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOApplication.framework/Java/Interfaces/EODocument.html
archived_at: '2026-07-15T08:11:36.959065Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOApplication Reference

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

# EODocument

> __Implemented by:__ : EODocumentController

> **__Implements:__**
> : EOObjectDisplay

> **__Package:__**
> : com.apple.client.eoapplication

---

## Interface Description

---

EODocument is
an interface that defines the behavior of a controller that displays
and edits enterprise objects.

## Instance Methods

---

### isDocumentForGlobalID

`public abstract boolean isDocumentForGlobalID(
com.apple.client.eocontrol.EOGlobalID globalID,
String entityName)`

Returns `true` if
the receiver is a document for the enterprise object associated
with _globalID_ and _entityName_, `false` otherwise. Typically
implementations return true if the receivers display group is displaying
the specified enteprise object.

---

### isEdited

`public abstract boolean isEdited()`

Returns `true` if
the receiver has unsaved edits, `false` otherwise.

---

### save

`public abstract boolean save()`

Saves the receivers edits,
returning `true` on success
or `false` otherwise.

---

### saveIfUserConfirms

`public abstract boolean saveIfUserConfirms(
String operationTitle,
String message)`

If the receivers enterprise
object has been edited, opens an alert panel that allows the user
to save the edits, discard the edits, or cancel the save operation. The _operationTitle_ argument
is used as the title of the alert panel, and _message_ is
used as the message in the panel. Returns `true` if
the save succeeds, `false` upon
failure or if the user cancels.

---

### setEdited

`public abstract void setEdited(boolean flag)`

Sets the
receivers edited status according to _flag_.

---

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

__DRAFT__
