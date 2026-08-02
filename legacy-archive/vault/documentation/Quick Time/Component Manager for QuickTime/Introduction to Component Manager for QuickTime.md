---
title: Component Manager for QuickTime
apple_id: TP40000858
resource_type: Guide
platform: macOS
topic: null
technology: QuickTime
published: '2005-04-08'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/Conceptual/ComponentMgr/1CompMgr4QTIntroduction/Introduction.html
archived_at: '2026-07-18T01:52:42.603867Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Component%20Manager%20for%20QuickTime.md)

# Introduction to Component Manager for QuickTime

Many QuickTime services, such as image compression and decompression, are provided by components. Components are a type of shared code resource that you can manipulate using the Component Manager.

For the most part, QuickTime components are opened, configured, and closed as needed by QuickTime, without you as an application programmer having to work with them explicitly.

You will probably need to use the Component Manager from time to time, however, in order to open a specific component, to determine whether a component has specific properties, to modify the default configuration of a component, or to configure a component programmatically instead of invoking a user dialog.

_Organization_ _of_ _this_ _Document_

This document describes the parts of the Component Manager you are likely to use in a QuickTime application. It includes a discussion of [Component Resources](Component%20Manager%20for%20QuickTime.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnjyfvbuqmlhfvbw63lqn5xgk3tukjsxg33vojrwk4y), including component public resources, that can often be used to obtain information about components quickly, without actually opening the components.

This document also describes [Component Property Functions and Selectors](Component%20Manager%20for%20QuickTime.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnjyfvbuqmlhfvbw63lqn5xgk3tukbzg64dfoj2hsrtvnzrxi2lpnzzwc3teknswyzldorxxe4y), introduced in QuickTime 6.4, that can be used to get and set component properties, and to install callbacks that are activated when component properties change, without using the Component Manager directly.

_See_ _Also_

In addition to this document, you may find the following documents useful:

- For a high-level introduction to QuickTime components, see _[QuickTime Overview](../QuickTime%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojs)_ and the [QuickTime QuickStart Guide](https://developer.apple.com/quicktime/qttutorial/).
- In addition to the conceptual information in this document, you should refer to the _[Component Manager Reference](https://developer.apple.com/documentation/coreservices/carbon_core/component_manager)_.
- If you intend to create new components, you also need to read [Creating QuickTime Components](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000433-TP30000595).

[Next](Component%20Manager%20for%20QuickTime.md)

