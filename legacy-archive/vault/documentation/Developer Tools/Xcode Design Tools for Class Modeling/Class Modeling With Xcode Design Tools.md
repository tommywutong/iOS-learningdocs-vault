---
title: Xcode Design Tools for Class Modeling
apple_id: TP40006845
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: Foundation
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XCodeDesignTools/Articles/xdtDesignTools.html
archived_at: '2026-07-15T07:27:13.027247Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Design Tools for Class Modeling](Introduction%20to%20Xcode%20Design%20Tools%20for%20Class%20Modeling.md)


[Next](Creating%20Models.md)[Previous](Introduction%20to%20Xcode%20Design%20Tools%20for%20Class%20Modeling.md)

# Class Modeling With Xcode Design Tools

The Xcode class modeling tool helps you to explore and understand the classes in your project, whether they’re written in Objective-C, C++, Java, or a mixture of those languages. It allows you to see class relationships (subclass and superclass relationships—including support for multiple inheritance in C++), protocols (or interfaces in Java), and categories. In the diagram view, color and text coding help you to quickly distinguish between classes, categories, and protocols, and between project and framework code. The visibility (public, private, protected) of member functions and variables is shown appropriately. (If you are not familiar with any of these terms, you should consult suitable programming texts.)

Class modeling allows you to understand and explore the classes in your project, whether they’re written in Objective-C, C++, Java, or a mixture of those languages. You can get a bird’s eye view of your project structure, look at relationships among classes, or scan quickly through class member and method types, parameters, and return values. You can use class modeling to augment or replace the Xcode class browser. The class model is saved with your project (you can even commit it to your repository), so other team members can get an overview of your code structure from the class model.

You can use the tool to visualize and browse class hierarchies not only in terms of the class relationships (subclass and superclass), but also in terms of the protocols (or interfaces in Java) a class implements, and the categories that are present. You can even add comments to call out notable things about specific classes.

Unlike most other modeling tools, Xcode lets you control the set of files (groups, targets, and so forth) that are modeled, the position and layout of the classes in the diagram, and even the classes that are shown. Moreover the Xcode class information is always up to date. Class models always represent the actual classes in files, groups, and targets in your project, and are automatically updated as you change your source code—even if you add, remove, or refactor classes.

There are a number of reasons why modeling tools are useful. You can use the tool as an index into your project. From within the tool, you can navigate to the source code of your own classes (both the declaration and implementation), to the declaration in framework classes (those for which you do not have source code), and to corresponding documentation. You can create models that persist as part of your project to communicate design details to other team members, and you can create temporary models (that is, quick models) that serve to illuminate an immediate problem.

A graphical representation of your project gives you a better conceptual overview of your project than raw XML or a mass of source files. In particular, with Xcode, it gives you a developer’s-eye view of your project, not a computer-generated representation. You can customize the view to see the information you need, not what the computer thinks is important or requires you to see. This is especially useful for communicating between members of a team, or for homing in on a specific aspect of a project. In addition, the class modeling tool may also be useful for learning about the functionality provided by existing libraries.

In terms of navigation, the browser view gives you an alternative means of navigating through your source, following relationships where appropriate. It provides a compact representation and summary of the classes in your project, including their properties and behaviors, and an easy way to get to relevant documentation.

[Next](Creating%20Models.md)[Previous](Introduction%20to%20Xcode%20Design%20Tools%20for%20Class%20Modeling.md)

