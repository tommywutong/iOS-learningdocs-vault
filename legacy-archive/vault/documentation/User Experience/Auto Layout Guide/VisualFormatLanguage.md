---
title: Auto Layout Guide
apple_id: TP40010853
resource_type: Guide
platform: tvOS|iOS|macOS
topic: User Experience
technology: AppKit
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/VisualFormatLanguage.html
archived_at: '2026-07-18T02:10:35.214377Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Auto Layout Guide](index.md)



## Visual Format Language

This appendix shows how to use the Auto Layout Visual Format Language to specify common constraints, including standard spacing and dimensions, vertical layout, and constraints with different priorities. In addition, this appendix contains a complete language grammar.

### Visual Format Syntax

The following are examples of constraints you can specify using the visual format. Note how the text visually matches the image.

|  |  |
| --- | --- |
| **Standard Space** | : `[button]-[textField]`   image: ../Art/standardSpace.png |
| **Width Constraint** | : `[button(>=50)]`   image: ../Art/widthConstraint.png |
| **Connection to Superview** | : `|-50-[purpleBox]-50-|`   image: ../Art/connectionToSuperview.png |
| **Vertical Layout** | : `V:[topField]-10-[bottomField]`   image: ../Art/verticalLayout.png |
| **Flush Views** | : `[maroonView][blueView]`   image: ../Art/flushViews.png |
| **Priority** | : `[button(100@20)]`   image: ../Art/priority.png |
| **Equal Widths** | : `[button1(==button2)]`   image: ../Art/equalWidths.png |
| **Multiple Predicates** | : `[flexibleButton(>=70,<=100)]`   image: ../Art/multiplePredicates.png |
| **A Complete Line of Layout** | : `|-[find]-[findNext]-[findField(>=20)]-|`   image: ../Art/completeLayout.png |

The notation prefers good visualization over completeness of expressibility. Most of the constraints that are useful in real user interfaces can be expressed using visual format syntax, but there are a few that cannot. One useful constraint that cannot be expressed is a fixed aspect ratio (for example, `imageView.width = 2 * imageView.height`). To create such a constraint, you must use [constraintWithItem:attribute:relatedBy:toItem:attribute:multiplier:constant:](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1526954-init).

### Visual Format String Grammar

The visual format string grammar is defined as follows (literals are shown in `code font`; __e__ denotes the empty string).

| Symbol | Replacement rule |
| --- | --- |
| <visualFormatString> | (<orientation>:)?  (<superview><connection>)?  <view>(<connection><view>)\*  (<connection><superview>)? |
| <orientation> | `H`|`V` |
| <superview> | `|` |
| <view> | `[`<viewName>(<predicateListWithParens>)?`]` |
| <connection> | __e__|`-`<predicateList>`-`|`-` |
| <predicateList> | <simplePredicate>|<predicateListWithParens> |
| <simplePredicate> | <metricName>|<positiveNumber> |
| <predicateListWithParens> | `(`<predicate>(`,`<predicate>)\*`)` |
| <predicate> | (<relation>)?(<objectOfPredicate>)(`@`<priority>)? |
| <relation> | `==`|`<=`|`>=` |
| <objectOfPredicate> | <constant>|<viewName> _(see note)_ |
| <priority> | <metricName>|<number> |
| <constant> | <metricName>|<number> |
| <viewName> | Parsed as a C identifier. This must be a key mapping to an instance of `NSView` in the passed views dictionary. |
| <metricName> | Parsed as a C identifier. This must be a key mapping to an instance of `NSNumber` in the passed metrics dictionary. |
| <number> | As parsed by `strtod_l`, with the C locale. |

> [!NOTE]
> 

If you make a syntactic mistake, an exception is thrown with a diagnostic message. For example:

1. `Expected ':' after 'V' to specify vertical arrangement`
2. `V|[backgroundBox]|`
3. `^`
5. `A predicate on a view's thickness must end with ')' and the view must end with ']'`
6. `|[whiteBox1][blackBox4(blackWidth][redBox]|`
7. `^`
9. `Unable to find view with name blackBox`
10. `|[whiteBox2][blackBox]`
11. `^`
13. `Unknown relation. Must be ==, >=, or <=`
14. `V:|[blackBox4(>30)]|`
15. `^`

[Changing Constraints](ModifyingConstraints.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmrzfvjvomi)
