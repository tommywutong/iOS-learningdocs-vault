---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOApplicationRef/Java/Interfaces/EODocument.html
archived_at: '2026-07-15T08:13:43.271725Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# EODocument

> __Implemented by:__ : EODocumentController

> **__Implements:__**
> : EOObjectDisplay

> **__Package:__**
> : com.webobjects.eoapplication

---

## Interface Description

---

EODocument is an interface that defines the behavior of a controller that displays and edits enterprise objects.

## Instance Methods

---

### isDocumentForGlobalID

`public abstract boolean isDocumentForGlobalID( com.webobjects.eocontrol.EOGlobalID globalID, String entityName)`

Returns `true` if the receiver is a document for the enterprise object associated with _globalID_ and _entityName_, `false` otherwise. Typically implementations return true if the receiver's display group is displaying the specified enteprise object.

---

### isEdited

`public abstract boolean isEdited()`

Returns `true` if the receiver has unsaved edits, `false` otherwise.

---

### save

`public abstract boolean save()`

Saves the receiver's edits, returning `true` on success or `false` otherwise.

---

### saveIfUserConfirms

`public abstract boolean saveIfUserConfirms( String operationTitle, String message)`

If the receiver's enterprise object has been edited, opens an alert panel that allows the user to save the edits, discard the edits, or cancel the save operation. The _operationTitle_ argument is used as the title of the alert panel, and _message_ is used as the message in the panel. Returns `true` if the save succeeds, `false` upon failure or if the user cancels.

---

### setEdited

`public abstract void setEdited(boolean flag)`

Sets the receiver's edited status according to _flag_.

---

© 2001 Apple Computer, Inc. (Last Published April 14, 2001)

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
