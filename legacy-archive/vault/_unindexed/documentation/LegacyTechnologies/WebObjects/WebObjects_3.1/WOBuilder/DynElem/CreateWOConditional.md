---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/DynElem/CreateWOConditional.html
archived_at: '2026-07-15T07:50:23.430717Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynElem.book.md)
[!Previous Section](CreateWORepetition.md)

Binding to WOConditionals

# Binding to WOConditionals

Select the WOConditional.

Double-click a variable in the variables browser.

!

A [WOConditional](../../Reference/DynamicElements/WOConditional.md) displays its contents only if a particular condition is true. WOConditional's main attribute is __condition__. If __condition__ is 1 (true), the WOConditional's contents are displayed. If __condition__ is 0, the contents aren't displayed. __condition__ can be bound to a variable or to method that returns the 1 or 0 value. The values __self__ or __nil__ also work in place of 1 or 0.

A WOConditional is like an if-then statement in a structured programming language. It tests to see if its condition is true, and if so, it displays its contents. If the condition is false, it displays nothing.

Many times, you want an "else" clause as well; that is, "if the condition is true, display this text; if not, display this other text." In such cases, you can make use of another WOConditional attribute: __negate__. If __negate__ is 1, it means that the condition is negated after it is evaluated. Thus, if __negate__ is 1 and __condition__ returns 1, the contents are _not_ displayed. To create an if-then-else style of conditional contents, do the following:

1. Drag two WOConditionals onto the page.
2. Select the first conditional and double-click a variable in the object browser.
3. Select the second conditional and double-click the same variable.
4. In the bindings inspector for the second WOConditional, select the __negate__ attribute, type 1 in the text field in the bindings inspector, and click Connect.

The example below is from a component named ReadWriteString. This component lets you set whether a displayed string is editable using the variable __editable__. If __editable__ is 1, the component displays the WOTextField contained in the second conditional. The WOString from the first conditional is not displayed because the first conditional negates the value in __editable__. If __editable__ is 0, the WOString is displayed but not the WOTextField.

!
