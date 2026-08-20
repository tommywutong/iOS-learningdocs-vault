---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WORadioButton.html
archived_at: '2026-07-15T08:00:46.294862Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Dynamic Elements](Dynamic%20Element%20Specifications.md)

---

# WORadioButton

---

# Synopsis

WORadioButton {value=_defaultValue_; [selection=_selectedValue_;] [name=_fieldName_;] [disabled=YES|NO;] ... };

WORadioButton {checked=YES|NO; [name=_fieldName_;] [disabled=YES|NO;] ... };

---

# Description

WORadioButton represents itself as an on-off switch. Radio buttons are normally grouped, since the most important aspect of their behavior is that they allow the user to select no more than one of several choices. If the user selects one button, the previously selected button (if any) becomes deselected.

Since radio buttons normally appear as a group, WORadioButton is commonly found within a WORepetition. Alternatively, you can use the WORadioButtonList element.

---

# Bindings

**---

### value

Value of this input element. If not specified, WebObjects provides a default value.

**---

### selection

If selection and value are equal when the page is generated, the radio button is selected. When the page is submitted, selection is assigned the value of the radio button.

**---

### checked

During page generation, if checked evaluates to YES, the radio button appears in the selected state. During request handling, checked reflects the state the user left the radio button in: YES if checked; NO if not.

**---

### name

Name that identifies the radio button's group. Only one radio button at a time can be selected within a group.

**---

### disabled

If disabled evaluates to YES, this element appears in the page but is not active. That is, selection does not contain the user's selection when the page is submitted.**********

Note that either checked or value is required in a WORadioButton declaration, but that they are mutually exclusive.

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
