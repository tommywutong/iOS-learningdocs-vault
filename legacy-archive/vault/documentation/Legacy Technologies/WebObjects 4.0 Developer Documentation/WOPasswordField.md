---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOPasswordField.html
archived_at: '2026-07-15T08:00:44.899850Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Dynamic Elements](Dynamic%20Element%20Specifications.md)

---

# WOPasswordField

---

# Synopsis

WOPasswordField { value=_defaultValue_; [name=_fieldName_;] [disabled =YES|NO;] ... };

---

# Description

A WOPasswordField represents itself as a text field that doesn't echo the characters that a user enters. It corresponds to the HTML element <INPUT TYPE="PASSWORD"...>.

---

# Bindings

**---

### value

During page generation, value sets the default value of the text field. This value is not displayed to the user. During request handling, value holds the value the user entered into the field, or the default value if the user left the field untouched.

**---

### name

Name that uniquely identifies this element within the form. You may specify a name or let WebObjects automatically assign one at runtime.

**---

### disabled

If disabled evaluates to YES, the element appears in the page but is not active. That is, value does not contain the user's input when the page is submitted.******

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
