---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/DynamicElements/Cndnls.htm
archived_at: '2026-07-15T07:56:15.111621Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!](DynElTOC.md)[Table
of Contents](DynElTOC.md) [!](Reps.md)[Previous
Section](Reps.md) 

## Conditionals

A conditional (WOConditional) is a dynamic container
element that displays its contents only if a particular condition is true.
WOConditional's main attribute is __condition__, which takes a Boolean
value. If __condition__ is true (1), the WOConditional's contents are
displayed. If __condition__ is false (0), the contents aren't displayed.

__condition__ can be bound to a variable or to
method that returns a Boolean value. (WebScript and Objective-C use the
constants __YES__ and __NO__; Java uses __true__ and __false__.)
To bind __condition__ (or any other attribute that takes a Boolean)
to a constant value, enter YES or NO in the bindings Inspector.

To create a conditional, click !
in the toolbar.

__Note:__ Any selected elements will be contained
within the conditional.

!

To bind to a conditional, click a variable or method
and drag to one of the conditional's outer icons. The Inspector appears,
displaying the bindings for the WOConditional, with the __condition__
attribute selected by default. Complete the binding by clicking Connect
Variable, or choose a different attribute to bind.

There is a shortcut for binding the condition
attribute. Drag from a key in the object browser to the binding box in
the conditional.

Sometimes, you want the equivalent of an "if-then-else"
structure; that is, "if the condition is true, display this text; if not,
display this other text." To accomplish this, you can use the __negate__
attribute. If __negate__ is true, then the contents of the conditional
are displayed only if __condition__ is false. To create an if-then-else
structure, do the following:

1. Create two WOConditionals. 
2. Bind the __condition__ attribute of both of them to the same variable
   or method. 
3. Bind the __negate__ attribute of the second one to YES (true). 

By default, __negate__ is false, so you do not explicitly need to
bind the first conditional's negate attribute.

As with repetitions, you can "wrap" a conditional around
a table row (see ["Repetitions"](Reps.md#apple-geydknjq)). When you
do this, the conditional symbol doesn't appear but the row appears with
a blue background.

[!](DynElTOC.md)[Table
of Contents](DynElTOC.md) [!](CustomWO.md)[Next
Section](CustomWO.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
