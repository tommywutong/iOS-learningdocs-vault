---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOHiddenField.html
archived_at: '2026-07-15T08:00:40.083859Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Dynamic Elements](Dynamic%20Element%20Specifications.md)

---

# WOHiddenField

---

# Synopsis

WOHiddenField { value=_defaultValue_; [ name=_fieldName_;] [disabled=YES|NO;] ... };

---

# Description

A WOHiddenField adds hidden text to the HTML page. It corresponds to the HTML element <INPUT TYPE="HIDDEN"...>. Hidden fields are sometimes used to store application state data in the HTML page. In WebObjects, the WOStateStorage element is designed expressly for this purpose.

---

# Bindings

**---

### value

Value for the hidden text field.

**---

### name

Name that uniquely identifies this element within the form. You may specify a name or let WebObjects automatically assign one at runtime.

**---

### disabled

If disabled evaluates to YES, the element appears in the page but is not active.******

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
