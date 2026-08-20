---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WhatIsWebObjects10.html
archived_at: '2026-07-15T08:06:39.681458Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](What%20Is%20a%20WebObjects%20Application.md) [!Previous Section](WhatIsWebObjects9.md)

## Web Components

A _component_ is a web page, or a portion of one, that has both content and behavior. Usually a component represents an entire page, so the word "page" is used interchangeably with the word "component." Components don't always represent an entire page, however. For example, a component might represent only a header or footer of a page; you can nest it inside of a component that represents the rest of the page.
Components are made up of:

- A template that specifies how the component looks
- Code that specifies how the component acts
- Bindings that associate the component's template with its code

Typically, components consist of some form of these three files, but any given component might contain more or fewer parts. For example, a component may not need a code file at all; it may need only a template file and a set of bindings. Another component might have a code file but no template file or bindings. Plus, if you create a component using Project Builder or WebObjects Builder, you'll get a fourth file, _Component___.api__, which contains API that should be made public to other components.
Note that the various parts of a component are actually located in various Project Builder suitcases: the template and bindings files are located under WebComponents, the code files are located under Classes, and API files (if you have any) wind up under a suitcase named Resources.

[!Table of Contents](What%20Is%20a%20WebObjects%20Application.md) [!Next Section](WhatIsWebObjects11.md)
