---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WORepetition.html
archived_at: '2026-07-15T08:00:47.203867Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


![Developer Documentation](attachments/images/wothinban.gif)

__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Dynamic Elements](Dynamic%20Element%20Specifications.md)

---

# WORepetition

---

# Synopsis

WORepetition {list=_anObjectList_; item=_anIteratedObject_; [index=_aNumber_;] [identifier=_aString_;] ... };

WORepetition {count=_aNumber_; [index=_aNumber_;] ... };

---

# Description

A WORepetition is a container element that repeats its contents (that is, everything between the <WEBOBJECT...> and </WEBOBJECT...> tags in the template file) a given number of times. You can use a WORepetition to create dynamically generated ordered and unordered lists or banks of check boxes or radio buttons.

---

# Bindings

**---

### list

Array of objects that the WORepetition will iterate through.

**---

### item

Current item in the list array. (This attribute's value is updated with each iteration.)

**---

### index

Index of the current iteration of the WORepetition. (This attribute's value is updated with each iteration.

**---

### count

Number of times this element will repeat its contents.********

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
