---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOSwitchComponent.html
archived_at: '2026-07-15T08:00:49.729917Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Dynamic Elements](Dynamic%20Element%20Specifications.md)

---

# WOSwitchComponent

---

# Synopsis

WOSwitchComponent { WOComponentName=_aComponentName_; ... };

---

# Description

WOSwitchComponent provides a way to determine at runtime which nested component should be displayed. This component is useful when you want to decide how to display information based on the state of the application.

---

# Bindings

**---

### WOComponentName

Name of the component to display. This attribute can be a string or a method that returns the name of a component.

If the component specified in WOComponentName takes attributes, pass these attributes along to WOSwitchComponent following the WOComponentName attribute. Note that this means that all components that can be displayed by this WOSwitchComponent must use the same API.**

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
