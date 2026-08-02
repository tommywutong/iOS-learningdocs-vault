---
title: Auto Layout Guide
apple_id: TP40010853
resource_type: Guide
platform: tvOS|iOS|macOS
topic: User Experience
technology: AppKit
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/LogicalErrors.html
archived_at: '2026-07-18T02:10:20.345342Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Auto Layout Guide](index.md)



## Logical Errors

Logical errors are simply bugs. Somewhere, you have an assumption that is faulty. Perhaps it’s an assumption about how Auto Layout calculates the views’ frames. Perhaps it’s an assumption about the set of constraints that you’ve created, or the view properties you’ve set. Perhaps it’s an assumption about how the constraints interact to create complex behaviors. Regardless, something somewhere does not quite match your mental model.

Logical errors are the hardest to find. After you eliminate all other possibilities, whatever remains, however improbable, must be a logical error. However, even after you’ve determined that you have a bug, you must still discover where, exactly, the faulty assumption lies.

There are no tools or step-by-step instructions here. Fixing logical errors typically involves experiments and iterative tests, both to identify the problem and to figure out how to fix it. There are, however, a few suggestions that may help:

- Review the existing constraints. Make sure you haven’t missed any constraints or accidentally added unwanted constraints. Make sure all the constraints are attached to the correct items and attributes.
- Double-check the view frames. Make sure nothing is getting unexpectedly stretched or shrunk.

  This is particularly important for views with invisible backgrounds, like labels or buttons. It may not be obvious when these items are unexpectedly resized.

  One symptom of resizing is that baseline-aligned views no longer line up properly. This is because the baseline alignment works only when the view is displayed at its intrinsic content height. If you stretch or shrink the view vertically, the text mysteriously appears in the wrong location.
- If a control should always match its intrinsic content size, give it a very high content-hugging and compression-resistance priority (for example, 999).
- Look for any assumptions that you’re making about the layout, and add explicit constraints to make sure those assumptions are true.

  Remember, unsatisfiable layouts are generally the easiest problems to find and fix. Add additional constraints until you have a conflict, then examine and fix the conflict.
- Try to understand why the given constraints are producing the results that you see. If you understand it, you’re well on the way to fixing it.
- Experiment with alternative constraints. Auto Layout typically gives you a number of different solutions for the same problem. Trying an different approach may fix the problem or at least make it easier to spot the mistake.

[Ambiguous Layouts](AmbiguousLayouts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmjyfvjvomi)

[Debugging Tricks and Tips](DebuggingTricksandTips.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmrrfvjvomi)
