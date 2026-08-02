---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOCheckBox.html
archived_at: '2026-07-15T08:00:34.566290Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Dynamic Elements](Dynamic%20Element%20Specifications.md)

---

# WOCheckBox

---

# Synopsis

WOCheckBox {value=_defaultValue_; [selection=_selectedValue_;] [name=_fieldName_;] [disabled=YES|NO;] ... };

WOCheckBox {checked=YES|NO; [name=_fieldName_;] [disabled=YES|NO;] ... };

---

# Description

A WOCheckBox object displays itself in the HTML page as its namesake, a check box user interface control. It corresponds to the HTML element <INPUT TYPE="CHECKBOX"...>.

If you want to create a list of check boxes, use WOCheckBoxList instead of this element.

---

# Bindings

**---

### value

Value of this input element. If not specified, WebObjects provides a default value.

**---

### selection

If selection and value are equal when the page is generated, the check box is checked. When the page is submitted, selection is assigned the value of the check box.

**---

### checked

During page generation, if checked evaluates to YES, the check box appears in the checked state. During request handling, checked reflects the state the user left the check box in: YES if checked; NO if not.

**---

### name

Name that uniquely identifies this element within the form. You may specify a name or let WebObjects automatically assign one at runtime.

**---

### disabled

If disabled evaluates to YES, this element appears in the page but is not active. That is, selection won't contain the user's selection when the page is submitted.**********

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
