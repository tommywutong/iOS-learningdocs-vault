---
title: Auto Layout Guide
apple_id: TP40010853
resource_type: Guide
platform: tvOS|iOS|macOS
topic: User Experience
technology: AppKit
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/TypesofErrors.html
archived_at: '2026-07-18T02:10:25.620864Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Auto Layout Guide](index.md)



## Types of Errors

Errors in Auto Layout can be divided into three main categories:

- __Unsatisfiable Layouts__. Your layout has no valid solution. For more information, see [Unsatisfiable Layouts](ConflictingLayouts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmjzfvjvomi).
- __Ambiguous Layouts__. Your layout has two or more possible solutions. For more information, see [Ambiguous Layouts](AmbiguousLayouts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmjyfvjvomi).
- __Logical Errors__. There is a bug in your layout logic. For more information, see [Logical Errors](LogicalErrors.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmrqfvjvomi).

Most of the time, the real problem is just determining what went wrong. You added the constraints you thought you needed, but when you ran the app, things did not turn out as you had hoped.

Usually, as soon as you understand the problem, the solution is obvious. Remove conflicting constraints, add missing constraints, and adjust tied priorities so that there is a clear winner. Of course, getting to the point where you can easily understand the problem may take some trial and error. Like any skill, it gets easier with practice.

Sometimes, however, things get more complicated. That’s where the [Debugging Tricks and Tips](DebuggingTricksandTips.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmrrfvjvomi) chapter comes in.

[Views with Intrinsic Content Size](ViewswithIntrinsicContentSize.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmjtfvjvomi)

[Unsatisfiable Layouts](ConflictingLayouts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmjzfvjvomi)
