---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOFrame.html
archived_at: '2026-07-15T08:00:38.428091Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Dynamic Elements](Dynamic%20Element%20Specifications.md)

---

# WOFrame

---

# Synopsis

WOFrame { value=_aMethod_; | src=_aURL_; | pageName=_aString_; | directActionName=_anActionName_; actionClass=_className_;... };

---

# Description

WOFrame represents itself as a dynamically generated Netscape Frame element.

---

# Bindings

**---

### value

Method that will supply the content for this frame.

**---

### src

External source that will supply the content for this frame.

**---

### pageName

Name of WebObjects page that will supply the content for this frame.

**---

### directActionName

The name of the direct action method (minus the "Action" suffix) that will supply the content for the frame.

**---

### actionClass

The name of the class in which the method designated in directActionName can be found. Defaults to DirectAction.**********

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
