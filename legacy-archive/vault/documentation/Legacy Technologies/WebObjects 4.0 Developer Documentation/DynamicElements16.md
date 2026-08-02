---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DynamicElements16.html
archived_at: '2026-07-18T01:25:43.321230Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](DynamicElements15.md)

## Conditionals

A conditional (WOConditional) is a dynamic container element that displays its contents only if a particular condition is true. WOConditional's main attribute is __condition__, which takes a Boolean value. If __condition__ is true (1), the WOConditional's contents are displayed. If __condition__ is false (0), the contents aren't displayed.
__condition__ must be bound to a variable or a method that returns a boolean value. (WebScript and Objective-C use the constants __YES__ and __NO__; Java uses __true__ and __false__.) To bind __condition__ (or any other attribute that takes a boolean) to a constant value, enter __YES__ or __NO__ in the bindings Inspector.
To create a conditional, click ! in the toolbar.
__Note:__ Any selected elements will be contained within the conditional.

!

To bind to a conditional, click a variable or method and drag to one of the conditional's outer icons. The Inspector appears, displaying the bindings for the WOConditional, with the __condition__ attribute selected by default. Complete the binding by clicking Connect, or choose a different attribute to bind.
There is a shortcut for binding the condition attribute similar to the WOString shortcut. Drag from a key in the object browser to the binding box in the conditional.
Sometimes, you want the equivalent of an "if-then-else" structure; that is, "if the condition is true, display this text; if not, display this other text." To accomplish this, you can use the __negate__ attribute. If __negate__ is true, then the contents of the conditional are displayed only if __condition__ is false. To create an if-then-else structure, do the following:

- Create two WOConditionals.
- Bind the __condition__ attribute of both of them to the same variable or method.
- Bind the __negate__ attribute of the second one to YES (true).

By default, __negate__ is false, so you do not explicitly need to bind the first conditional's negate attribute.

As with repetitions, you can "wrap" a conditional around a table row (see ["Repetitions"](DynamicElements15.md#apple-geydknjq)). When you do this, the conditional symbol doesn't appear but the row appears with a blue background.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](DynamicElements17.md)
