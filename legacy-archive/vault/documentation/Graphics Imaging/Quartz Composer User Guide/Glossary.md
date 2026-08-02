---
title: Quartz Composer User Guide
apple_id: TP40005381
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: Quartz
published: '2007-07-17'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/QuartzComposerUserGuide/qc_glossary/qc_glossary.html
archived_at: '2026-07-15T07:37:37.867344Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quartz Composer User Guide](Introduction%20to%20Quartz%20Composer%20User%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Tutorial-%20Creating%20a%20Composition.md)

# Glossary

- __clip__

  Prepackaged “mini” compositions that you can drag into a composition and customize for your own use.

- __composition__

  A collection of interconnected patches that describe a data flow.

- __composition repository__

  A central location for storing compositions. Any application can, using the Quartz Composer framework, query the repository for specific types of compositions or browse the repository to see what’s available.

- __consumer__

  A patch that renders a result to a destination.

- __Core Image filter__

  An image processing routine provided by the Core Image framework. Core Image filters are automatically read into Quartz Composer and made available as patches.

- __debug rendering mode__

  A view that displays an animation of the data flow in a composition that can help track down issues. In this mode, patches in the workspace change colors as they move from one state to another. A drawer below the view displays log messages.

- __graph__

  A set of connected patches on the workspace.

- __hierarchical browser__

  The area in the Quartz Composer window used to view and navigate from one level to another in the patch hierarchy.

- __macro patch__

  A patch that contains other patches. A macro is similar to a subroutine in a traditional program. A macro can nest other macros within it. A macro is visually distinguished from a nonmacro patch by its shape—macros have squared-off corners and other patches have rounded corners.

- __OpenGL__

  An open source graphics library. For more information see [http://www.opengl.org/](http://www.opengl.org/).

- __patch__

  The base processing unit in a composition, which executes and produces a result. Patches are similar to routines in traditional programming languages. See also [macro patch](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgobrfvbuqmrrgewueq2jincuiskj).

- __patch hierarchy__

  The levels in a composition created when macro patches are used. See also [macro patch](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgobrfvbuqmrrgewueq2jincuiskj).

- __port__

  The mechanism by which patches communicate. Ports can represent input or output parameters. Connections between input and output ports of different patches establish a data flow in a composition.

- __processor__

  A patch that processes data at specified intervals or in response to changing input values.

- __profile rendering mode__

  A view that displays an analysis of each rendered frame in a composition; the analysis can help you to optimize performance.

- __provider__

  A patch that supplies data from an outside source to a composition.

- __root macro patch__

  The main routine in a composition; the evaluation of a composition begins at the root macro patch. All patches are nested, at one level or another, within the root macro patch. Ports that you publish at the root macro patch are accessible externally.

- __RSS__

  Really Simple Syndication, a lightweight XML format.

- __subpatch__

  A patch that is contained in a macro.

- __template__

  A composition file that contains a basic set of patches for a particular purpose.

- __workspace__

  The area in the Quartz Composer development tool used to assemble patches.

[Next](Document%20Revision%20History.md)[Previous](Tutorial-%20Creating%20a%20Composition.md)

