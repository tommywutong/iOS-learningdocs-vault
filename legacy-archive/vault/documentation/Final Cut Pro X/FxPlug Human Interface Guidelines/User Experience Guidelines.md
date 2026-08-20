---
title: FxPlug Human Interface Guidelines
apple_id: TP40013782
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2013-12-18'
source_url: https://developer.apple.com/library/archive/documentation/FinalCutProX/Conceptual/FxPlugHIG/UserExperienceGuidelines/UserExperienceGuidelines.html
archived_at: '2026-07-15T07:32:46.814483Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [FxPlug Human Interface Guidelines](About%20the%20FxPlug%20Human%20Interface%20Guidelines.md)


[Next](FxPlug%20Host%20Built-in%20UI%20Elements.md)[Previous](About%20the%20FxPlug%20Human%20Interface%20Guidelines.md)

# User Experience Guidelines

Final Cut Pro X and Motion use all of the hardware in a modern Mac to deliver a great interactive experience, with minimal rendering time. Your plug-ins should deliver real-time final results, without requiring lower-quality “preview” modes or time-consuming exports.

Not every plug-in idea can deliver in real time in all cases, but by leveraging the full capabilities of FxPlug, you can make sure the user experience is as fluid as possible.

A great plug-in focuses the user experience on the task that the user is attempting to accomplish, not just the parameters used to achieve the result. Getting satisfactory results quickly, with as little to learn as possible, is important. The user will return to your plug-in again and again, and anticipate future plug-ins you create.

For example, if your plug-in creates a magic sparkle particle effect, you may be tempted to design the interface solely as a generalized particle system with dozens of parameters, requiring the user to adjust many values to achieve that look and variations on it. To make the task easier for the user, provide a quick mode or preset to easily generate that magic sparkle particle effect, without requiring numerous steps or having a steep learning curve.

A plug-in works best with an organized workflow of controls. First are the onscreen controls, next the heads-up display (for Motion only), then the Inspector, and finally the keyframe editor. Users jump in at any point along this workflow, so the initial experience should be as fluid as possible.

Place the most relevant and frequently used controls at the top of the Inspector. If a parameter affects the relevance or output of other parameters, place it above the others in the hierarchy. For example, if a slider at the top of the UI has no effect unless a checkbox somewhere below it is selected, reorder the components so that the checkbox appears above the slider. This spares the user frustration and confusion when the slider doesn’t work.

In all of your text-based communication with users, use terminology you’re sure that your users understand. In particular, avoid technical jargon in the user interface. Use what you know about your users to determine whether the words and phrases you plan to use are appropriate. Final Cut Pro X and Motion are professional applications, so industry-specific terminology can be appropriate to some of these users, but also remember that all readers appreciate clear and jargon-free terminology.

For example, the word “key” used to refer to removing a blue or green color from the background of a video clip is perfectly understandable to an audience of video professionals, but it might be confusing to a general user. Therefore, the ideal usage of the word “key” depends on the type of user you are targeting with your plug-in.

All plug-ins operate within the Final Cut Pro X environment, and people expect standard views and controls to look and behave consistently across plug-ins.

__Follow the recommended usages for standard user interface elements.__ In this way, users can depend on their prior experience as they learn to use your plug-in. You also make it easy for your plug-in to look up-to-date and work correctly if FxPlug changes the look or behavior of these standard views or controls.

__For a plug-in that enables a unique task, such as a 3D modeling environment, it’s reasonable to create completely custom controls.__ This is because you’re creating a unique environment, and discovering how to control that environment is an experience that users expect in such plug-ins.

__Avoid radically changing the appearance of a control that performs a standard action.__ Users will spend valuable time discovering how to use unfamiliar controls and will wonder what, if anything, your controls do that the standard ones do not.

FxPlug provides many of the standard controls used by built-in plug-ins.

__To avoid confusing people, never use the standard buttons and icons to mean something else.__ Understand the documented meaning of a standard control; don’t rely on your interpretation of its appearance.

System-provided buttons and icons provide two other substantial advantages:

- Decreased development time, because you don’t have to create custom art to represent standard functions.
- Increased stability of your user interface, even if future FxPlug updates change the appearance of standard controls. In other words, you can rely on the semantic meaning of a standard icon remaining the same, even if its appearance changes.

Avoid branding and graphical logos in your plug-in. Adding logos or other elements that aren’t part of the plug-in functionality takes space from other controls such as sliders, checkboxes, and pop-up menus. Users are likely to use your plug-in alongside others, so you want simple interfaces in order to offer users a cleaner window space and better user experience.

If you must add branding elements, place them into the application associated with your plug-in, or place the branding elements into a separate, optional floating window that is opened from within your plug-in.

When you are designing the plug-in, provide enough controls to give users a variety of options, but limit the number of parameters. Limiting the number of parameters makes it easier for users to accomplish a task.

If your plug-in contains more than 10 or 15 parameters, consider finding creative ways to consolidate them and to provide a quicker way for the user to achieve the same result.

In your plug-in, hide settings that enable or disable certain parameters, rather than displaying them as disabled. This keeps the UI compact and clear of parameters that currently have no effect on the image.

The exception to this rule is if the disabled parameters’ values remain relevant even when disabled. For example, if a checkbox specifies that the user can set a custom color, displaying a disabled color well filled with the default white implies that (a) the current color is white and (b) this color cannot be adjusted until the custom color checkbox is selected.

Direct manipulation in the Viewer is often the fastest, most intuitive means for a user to adjust the settings of a plug-in. Many of Apple’s standard plug-ins have onscreen controls that let users edit the most important aspects of an effect without having to open the Inspector and adjust sliders or other numeric parameters. Consider adding onscreen controls to your plug-in so that users can quickly and interactively adjust an effect.

Custom controls can be powerful if those controls are suited to your plugin’s task.

FxPlug provides many standard UI elements that enable a wide range of actions in your plug-in. Users are comfortable with these elements in new plug-ins because they already know how to use them. In rare cases, however, you might need to enable an action for your plug-in for which there is no FxPlug element. If you need to design a custom UI element, follow these general guidelines:

- __Don’t assign new behaviors to standard UI elements.__ It’s better to create a custom element than to change the behavior of a familiar FxPlug element. If UI elements behave differently in different situations, the interface becomes unpredictable.
- __Don’t create a custom UI element that looks or behaves like an FxPlug UI element.__ If your custom element looks too much like an FxPlug element, users might not notice the difference and can become confused when it does not behave as they expect. Similarly, if your custom element behaves the same way as an FxPlug element, users may wonder why there are two different controls that do the same thing, and assume that there is some difference they can’t see.
- __Make sure your custom UI element enhances the usability of your plug-in__. A custom UI element should provide users with a unique benefit, one that is difficult to achieve in any other way. If a new UI element doesn’t help users, they’re likely to feel that they wasted time learning about it.
- __Avoid replicating a UI element from another platform.__ Not all users are familiar with other platforms, so don’t assume that they will recognize non-FxPlug UI elements. If you need the functionality of an element that is not in the FxPlug interface, use the interface to design a new UI element that coordinates with the design of your plug-in and that supplies the behavior you need.

When first applied to footage, the plug-in should have an immediate effect. Users should see a result and then be able to adjust the effect to their liking. Doing nothing by default forces the user to first learn about your plug-in’s parameters in order to explore the features.

For example, if your plug-in is called the “Super Blur” filter, the user expects the plug-in to blur the image, so it’s best to use something other than zero as the default amount of the blur.

If you’re redesigning an existing plug-in from another platform for FxPlug, make sure you give people an FxPlug experience.

Here are some strategies that can help developers convert an existing plug-in to FxPlug.

__Focus on real-time interactivity.__ Final Cut Pro X and Motion users expect plug-ins to behave in real time or near real time, with highly interactive performance. One way to enhance the performance of an existing plug-in is to take advantage of the latest GPU-based technologies.

__Focus on tasks, not features.__ Successful plug-ins tend to focus on tasks, not on having large numbers of adjustable parameters. If your plug-in requires a very large set of parameters, consider consolidating them, or breaking up the functionality into separate plug-ins.

__Design for onscreen controls.__ Great plug-ins can operate effectively without requiring the Inspector to be visible. Leverage the onscreen controls to make your plug-in do remarkable things while working directly on the image.

[Next](FxPlug%20Host%20Built-in%20UI%20Elements.md)[Previous](About%20the%20FxPlug%20Human%20Interface%20Guidelines.md)

