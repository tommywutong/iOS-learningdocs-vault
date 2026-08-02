---
title: Code Loading Programming Topics
apple_id: 10000052i
resource_type: Guide
platform: macOS
topic: General
technology: Foundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingCode/Concepts/MultiBundleApps.html
archived_at: '2026-07-15T07:16:27.348601Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Code Loading Programming Topics](Introduction%20to%20Dynamically%20Loading%20Code.md)


[Next](Plug-in%20Architectures.md)[Previous](CFBundle%20and%20NSBundle.md)

# Multi-Bundle Applications

This concept describes how to design an application that uses multiple loadable components. This material is relevant both to developers organizing their application into large loadable components and to developers designing an extensible plug-in architecture.

Components are at the heart of the object-oriented programming model. Rather than a monolithic, intertwined mess of code, well-designed applications are built up from components, each of which handles some well-defined unit of functionality. This structuring occurs on many levels, from simple data objects to large self-contained components such as integrated HTML viewers. Even most applications written in “non-object-oriented” languages like C exhibit this sort of structure.

You can use loadable bundles to separate components into discrete executable packages that can be loaded dynamically at runtime. When designing an application, you may want to use multiple loadable bundles to partition the application into well-defined components that work together but can be developed, compiled, and loaded independently of one another. While you are unlikely to need multiple bundles for simple data objects, they may be appropriate for larger pieces of functionality.

Take as an example an integrated application that produces cards, banners, and newsletters. Although the three components may link against some shared code, in any particular runtime session it is unlikely that more than one of the components will be used. Additionally, each component is independent of the other, and functions essentially as a separate application.

Because of the independent nature of the components and the likelihood that only one of them will be used at any time, such an application is a good candidate for using a bundle-based design. Figure 1 shows how the example application might be organized with bundles.

__Figure 1__  Structuring an app with loadable bundles

!

By building each component as its own loadable bundle, you gain several advantages:

- You can develop and test each component independently, and build one without rebuilding the others.
- You can mix and match different versions of the components just by moving file packages around.
- At runtime, your application can load only the bundles that are actually used, instead of loading code that is never used. In non-Cocoa applications, the application can even unload bundles once they’re done being used.

Most applications can benefit from this approach, but you may not need dynamic loading. For shared code used by multiple applications or multiple components of an application, you should use a framework instead.

Additionally, Cocoa applications cannot unload bundles. If you want to be able to load and unload large separately built application components, you can build your application as a number of smaller executable components, and the main application can fork child processes. You can enable communication between the processes with the Cocoa distributed objects architecture. For more information, see _[Distributed Objects Programming Topics](../Distributed%20Objects%20Programming%20Topics/Introduction%20to%20Distributed%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeyde2i)_.

Another common kind of structuring that applications can benefit from is a plug-in model. Many applications have a number of features that perform similar tasks, like graphics filters in an image processing application or modules in a screen saver. These are best developed as part of a plug-in architecture, so that new modules can be added later with relative ease. Additionally, by publishing the plug-in architecture, you can allow extensibility of your application by third parties. Even if you don’t want to publish your plug-in architecture to third parties, using a plug-in model can greatly ease your own internal development. For more information about plug-ins, see [Plug-in Architectures](Plug-in%20Architectures.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3telkcineuiqsbivfa).

To effectively organize an application into multiple bundles, you should keep a few things in mind:

- It’s hard to manage complex interdependencies between loadable bundles, so organize your application into largely self-contained, independent units. The easiest way to do this is for each bundle to contain a reference to a single object in another bundle—in Cocoa, typically the principal class—and use it to access any other functionality and data.
- Separate out components that may never be used during a runtime session to prevent code from being loaded and never used.
- If your application contains a number of components that perform variations on the same type of operation, such as graphics filters or export formats, or any component that you want to be replaceable or extensible, consider using a plug-in architecture.

For example, return to the banner/card/newsletter application described in [When to Use Multiple Bundles](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tcljzgy4dcoi). According to these guidelines, it makes sense to organize the application into four loadable bundles: one for the main application controller, and one each for the three subapplications. Additionally, perhaps the application has a number of different ways of drawing text: in a circle, in the shape of a zebra, etc. Providing a plug-in architecture for text-drawing methods would make the application developer’s job easier and allow third parties to add features like drawing text with three-dimensional effects.

[Next](Plug-in%20Architectures.md)[Previous](CFBundle%20and%20NSBundle.md)

