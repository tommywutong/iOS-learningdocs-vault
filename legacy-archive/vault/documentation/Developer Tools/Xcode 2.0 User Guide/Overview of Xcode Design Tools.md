---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/design_overview/01_designToolsIntro.html
archived_at: '2026-07-15T07:29:41.446561Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Common%20Features%20of%20the%20Xcode%20Design%20Tools.md)[Previous](Design%20Tools.md)

# Overview of Xcode Design Tools

Xcode includes two separate design tools, with
similar forms but different functions. Together, the tools allow
you to model both the classes in your application and entities that represent
your data. Although they are in some respects similar, class modeling
and entity-relationship modeling are fundamentally different and
serve different purposes—both are discussed below.

The two tools share some common functionality. They allow
you to create models that form part of your project. They allow
you to browse through the contents of the model using a set of table
views and to visualize the contents in a diagram.

Control over how models are displayed is where Xcode differs
from other design tools. Other IDEs that provide a graphic class
browser typically give you little control over display—you see
what it wants to show you. With Xcode, you have coarse-, medium-,
and fine-grained control over what is displayed and how. You can
edit the diagram in the same way you might in common graphics editors.
For example, you can color, move, and align elements to arrange
them how you wish; zoom in and out of the diagram; and choose whatever
page and grid sizes you want. Moreover, your models never become
stale.

Class modeling allows you to understand and explore the classes
in your project, whether they’re written in Objective-C, C++,
Java, or a mixture of those languages. You can get a bird’s eye
view of your project structure, look at relationships among classes,
or scan quickly through class member and method types, parameters,
and return values. You can use class modeling to augment or replace
the Xcode class browser. The class model is saved with your project
(you can even commit it to your repository), so other team members
can get an overview of your code structure from the class model.

You can use the tool to visualize and browse class hierarchies
not only in terms of the class relationships (subclass and superclass),
but also in terms of what protocols (or interfaces in Java) a class
implements, and what categories are present. You can even add comments to
call out notable things about specific classes.

Unlike most other modeling tools, you control the set of files
(groups, targets, and so forth) that are modeled, the position and
layout of the classes in the diagram, and even what classes are
shown. Moreover the Xcode class information is always up to date.
Class models always represent the actual classes in files, groups,
and targets in your project, and are automatically updated as you
change your source code—even if you add, remove, or refactor classes.

The data modeling tool is like the class modeling tool in
that you can, for example, lay out a diagram to represent your model
visually, but different in that it deals with entities and the relationships
between them, not with classes and hierarchies. There is not necessarily a
1:1 relationship between entities and classes—for example, the
same class may be used to represent more than one entity. For more
about data modeling, see [Modeling Document].

More importantly, however, you use the data modeling
tool to define what is in effect a source file—a schema for Core
Data. The data model ultimately becomes part of your build product
and is used by your application at run time. Instances of entities
are typically stored in a persistent store (typically a file).

There are a number of reasons why modeling tools are useful.
Some reasons apply to both the class and data models, some apply
to one or the other.

A graphical representation of your project gives you a better
conceptual overview of your project than raw XML or a mass of source
files . In particular, with Xcode, it gives you a developer’s
eye view of your project, not a computer-generated representation .
You can customize the view to see the information you need, not
what the computer thinks is important or requires you to see .
This is especially useful for communication between members of
a team, or for homing in on a specific aspect of a project [see
filtering]. In addition, the class modeling tool may also be useful
for learning about functionality provided by existing libraries.

In terms of navigation, the browser view gives you an alternate
means of navigating through your source, following relationships
where appropriate. It provides a compact representation and summary
of the classes or entities in your project, including their properties
and behaviors, and (for the class browser) an easy way to get to
relevant documentation.

Both class and data models are project resources. A class
model is stored with the project as it is an integral part of development
process . A data model is stored as part of the project because
it is essential to Core Data—it is also included in a target
as it is compiled for deployment .

[Next](Common%20Features%20of%20the%20Xcode%20Design%20Tools.md)[Previous](Design%20Tools.md)

