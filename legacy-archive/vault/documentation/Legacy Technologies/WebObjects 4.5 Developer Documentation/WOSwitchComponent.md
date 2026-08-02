---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOSwitchComponent.html
archived_at: '2026-07-15T08:09:53.555832Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Dynamic Elements

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)

---

# WOSwitchComponent

## Element Description

WOSwitchComponent provides a way to determine at runtime which
nested component should be displayed. This component is useful when
you want to decide how to display information based on the state
of the application.

## Synopsis

WOSwitchComponent { WOComponentName=_aComponentName_;
... };

## Bindings

**WOComponentName**
: Name of the component to display. This attribute
can be a string or a method that returns the name of a component.

If the component specified in __WOComponentName__ takes
attributes, pass these attributes along to WOSwitchComponent following
the __WOComponentName__ attribute. Note that
this means that all components that can be displayed by this WOSwitchComponent
must use the same API.

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)
