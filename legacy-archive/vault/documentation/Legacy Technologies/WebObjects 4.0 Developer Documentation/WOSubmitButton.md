---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOSubmitButton.html
archived_at: '2026-07-15T08:00:49.236774Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Dynamic Elements](Dynamic%20Element%20Specifications.md)

---

# WOSubmitButton

---

# Synopsis

WOSubmitButton { action=_submitForm_; value=_aString_; [disabled=YES|NO;] [name=_aName_;] ... };

---

# Description

A WOSubmitButton element generates a submit button in an HTML page. This element is used within HTML forms.

---

# Bindings

**---

### action

Action method to invoke when the form is submitted.

**---

### value

Title of the button.

**---

### disabled

If disabled evaluates to YES, the element appears in the page but is not active. That is, clicking the button does not actually submit the form.

**---

### name

Name that uniquely identifies this element within the form. You may specify a name or let WebObjects automatically assign one at runtime.********

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
