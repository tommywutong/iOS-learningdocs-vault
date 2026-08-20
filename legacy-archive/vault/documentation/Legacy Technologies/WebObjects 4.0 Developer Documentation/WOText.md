---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOText.html
archived_at: '2026-07-15T08:00:50.262248Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Dynamic Elements](Dynamic%20Element%20Specifications.md)

---

# WOText

---

# Synopsis

WOText { value=_defaultValue_; [name=_fieldName_;] [disabled=YES|NO;] ... };

---

# Description

WOText generates a multi-line field for text input and display. It corresponds to the HTML element <TEXTAREA>.

---

# Bindings

**---

### value

During page generation, value specifies the text that is displayed in the text field. During request handling, value contains the text as the user left it.

**---

### name

Name that uniquely identifies this element within the form. You may specify a name or let WebObjects automatically assign one at runtime.

**---

### disabled

If disabled evaluates to YES, the text area appears in the page but is not active. That is, value does not contain the user's input when the page is submitted.******

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
