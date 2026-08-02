---
title: FxPlug SDK Overview
apple_id: TP40002180
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/FXPlug_overview/FxPlugsFCPx/FxPlugsFCPx.html
archived_at: '2026-07-15T05:17:57.085276Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [FxPlug SDK Overview](About%20the%20FxPlug%20SDK.md)


[Next](Creating%20Onscreen%20Controls.md)[Previous](Working%20with%20Entitlements.md)

# Creating FxPlug Plug-ins for Final Cut Pro

To make FxPlug plug-ins work in Final Cut Pro, you need to create a Final Cut Effect within Motion that rigs and/or publishes your FxPlug parameters. The best place to learn how to do that is in the Motion documentation (see the _Using Rigs_ section for complete details).

Most users of Final Cut Pro want to solve specific tasks rather than to apply particular effects. In general, you want to avoid publishing long lists of parameters that are likely to confuse users and make completing their tasks harder rather than easier.

Advanced users who need more control will be able to either open your Final Cut Effect in Motion and edit it themselves, or create their own Final Cut Pro Effects within Motion for their specific task. Remember, less advanced users will be overwhelmed by filters that are too complex and won’t generally need to control every parameter in a given filter.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To create a basic Final Cut Pro Effect

1. Open Motion.
2. Create a new Final Cut Pro Effect document from the Project Browser.

   This should create a new Motion document with a drop zone named Effect Source in the timeline.
3. Apply the Glow filter to the Effect Source Drop Zone.

   Note that a Final Cut Pro Effect, Generator, Transition or Title is really just a Motion document. They can contain any of the visual effects that are normally possible, such as multiple filters, behaviors, shapes, or text to name a few.
4. Select the newly applied FxPlug plug-in and open the Motion Inspector to reveal its parameters.
5. When you mouse over the Radius parameter, you’ll notice a popup-menu indicator appear to the right of the Radius slider.
6. Click it to reveal the parameter’s option menu.
7. Choose Add To Rig > Create New Rig > Add To New Slider.

   You’ll notice a new Rig group created in the layer list, with a new layer named Slider which is now selected.
8. Double-click the name Slider in the layer list, and change the name to Glowiness.

   When this effect is applied in Final Cut Pro, it now shows a single parameter named Glowiness. Next, connect it to two different parameters so that the user can control them at the same time.
9. Select the Glow filter again in the layer list to display its parameters in the Inspector.

   The Radius parameter should now have an icon of a joystick to the right.
10. Click the pop-up menu for the Opacity slider, and choose Add To Rig > Rig > Add To Glowiness.
11. Show the Glowiness slider in the Inspector by selecting it in the layer list.
12. The slider is displayed with two circles below it, one at the left end of the slider and one at the right end. Select the one on the left by clicking it.
13. Set the Effect Source.Opacity slider to 0 and the Effect Source.Aura.Inner Radius slider to 0.

    This sets the Opacity and Radius parameters to 0 when the rigged slider is set to 0.
14. Select the circle under the right end of the Glowiness slider by clicking it.
15. Set the Effect Source.Opacity slider to its maximum value, and do the same for the Effect Source.Aura.Inner Radius slider.

    Now when the user moves the Glowiness slider in the Final Cut Pro Inspector, both the Opacity and Radius parameters increase.

Publishing a parameter, such as the Threshold parameter, so the user can control it directly, is different from rigging. With rigging, you can tie one user-visible parameter to a host of parameters in your Final Cut Pro Effect. With Publishing, a parameter is directly accessible to users.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To create the Threshold parameter for direct manipulation

1. In the layer list, select the Glow effect so that its parameters are displayed in the Inspector.
2. In the Inspector, click the Threshold parameter’s pop-up menu, and choose Publish.
3. Save the effect.

   When you attempt to save a Final Cut Pro Effect, Transition, Generator, or Title, you’re presented with some options. In addition to a name, you can assign the effect to a category, which is where it appears in the Final Cut Pro Effect Browser. You can also choose a Theme.
4. After you have a name and category, click the Publish button.

Your effect should be immediately available in Final Cut Pro. You don’t need to quit Motion, or quit and restart Final Cut Pro, to see it.

Occasionally, an FxPlug may need to know from which app it has been invoked. Checking the hostID is the preferred way of doing this. Please note that if an FxPlug is invoked as part of a Motion Effect, it will return Motion as the host app. If you require further differentiation, it is possible to check the bundle identifier of the mainBundle.

When updating a plug-in, it may be necessary to deprecate older versions of the Motion Template wrapper. You use the second bit of the `<flags>` value in the Motion XML document to indicate whether the template is deprecated (1) or not (0). To deprecate a template, in the Motion XML document perform a bitwise OR operation on the `<flags>` child element of the `<template>` element with the value 0x2. For example, if the `<flags>` value was previously `1`, it should now be `3`, like this:

```
<template>
    <flags>3</flags>
</template>
```

This action marks the associated Motion template as obsolete, and it will no longer appear in the effects browser.

This is the only way to deprecate a Motion template, and it only works with the Motion XML document; there is no UI for doing this.

[Next](Creating%20Onscreen%20Controls.md)[Previous](Working%20with%20Entitlements.md)

