---
title: Animations
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/animations
source_url: 'https://developer.apple.com/documentation/swiftui/animations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animations.json'
content_hash: 'sha256:1d07043c266b202c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Animations

<sub>API Collection</sub>

Create smooth visual updates in response to state changes.

## Overview

You tell SwiftUI how to draw your app’s user interface for different states, and then rely on SwiftUI to make interface updates when the state changes.

![](../../../attachments/634da5b7eb74a20fee434a105cebd3c7/animations-hero@2x.png)

To avoid abrupt visual transitions when the state changes, add animation in one of the following ways:

- Animate all of the visual changes for a state change by changing the state inside a call to the [withAnimation(_:_:)](<withanimation(____).md>) global function.
- Add animation to a particular view when a specific value changes by applying the [animation(_:value:)](<view/animation(__value_).md>) view modifier to the view.
- Animate changes to a [Binding](binding.md) by using the binding’s [animation(_:)](<binding/animation(__).md>) method.

SwiftUI animates the effects that many built-in view modifiers produce, like those that set a scale or opacity value. You can animate other values by making your custom views conform to the [Animatable](animatable.md) protocol, and telling SwiftUI about the value you want to animate.

When an animated state change results in adding or removing a view to or from the view hierarchy, you can tell SwiftUI how to transition the view into or out of place using built-in transitions that [AnyTransition](anytransition.md) defines, like [slide](anytransition/slide.md) or [scale](anytransition/scale.md). You can also create custom transitions.

For design guidance, see [Motion](../design/human-interface-guidelines/motion.md) in the Human Interface Guidelines.

## Topics

### Adding state-based animation to an action

- [withAnimation(_:_:)](<withanimation(____).md>) — Returns the result of recomputing the view’s body with the provided animation.
- [withAnimation(_:completionCriteria:_:completion:)](<withanimation(__completioncriteria___completion_).md>) — Returns the result of recomputing the view’s body with the provided animation, and runs the completion when all animations are complete.
- [AnimationCompletionCriteria](animationcompletioncriteria.md) — The criteria that determines when an animation is considered finished.
- [Animation](animation.md) — The way a view changes over time to create a smooth visual transition from one state to another.

### Adding state-based animation to a view

- [animation(_:)](<view/animation(__).md>) — Applies the given animation to this view when this view changes.
- [animation(_:value:)](<view/animation(__value_).md>) — Applies the given animation to this view when the specified value changes.
- [animation(_:body:)](<view/animation(__body_).md>) — Applies the given animation to all animatable values within the `body` closure.

### Creating phase-based animation

- [Controlling the timing and movements of your animations](controlling-the-timing-and-movements-of-your-animations.md) — Build sophisticated animations that you control using phase and keyframe animators.
- [phaseAnimator(_:content:animation:)](<view/phaseanimator(__content_animation_).md>) — Animates effects that you apply to a view over a sequence of phases that change continuously.
- [phaseAnimator(_:trigger:content:animation:)](<view/phaseanimator(__trigger_content_animation_).md>) — Animates effects that you apply to a view over a sequence of phases that change based on a trigger.
- [PhaseAnimator](phaseanimator.md) — A container that animates its content by automatically cycling through a collection of phases that you provide, each defining a discrete step within an animation.

### Creating keyframe-based animation

- [keyframeAnimator(initialValue:repeating:content:keyframes:)](<view/keyframeanimator(initialvalue_repeating_content_keyframes_).md>) — Loops the given keyframes continuously, updating the view using the modifiers you apply in `body`.
- [keyframeAnimator(initialValue:trigger:content:keyframes:)](<view/keyframeanimator(initialvalue_trigger_content_keyframes_).md>) — Plays the given keyframes when the given trigger value changes, updating the view using the modifiers you apply in `body`.
- [KeyframeAnimator](keyframeanimator.md) — A container that animates its content with keyframes.
- [Keyframes](keyframes.md) — A type that defines changes to a value over time.
- [KeyframeTimeline](keyframetimeline.md) — A description of how a value changes over time, modeled using keyframes.
- [KeyframeTrack](keyframetrack.md) — A sequence of keyframes animating a single property of a root type.
- [KeyframeTrackContentBuilder](keyframetrackcontentbuilder.md) — The builder that creates keyframe track content from the keyframes that you define within a closure.
- [KeyframesBuilder](keyframesbuilder.md) — A builder that combines keyframe content values into a single value.
- [KeyframeTrackContent](keyframetrackcontent.md) — A group of keyframes that define an interpolation curve of an animatable value.
- [CubicKeyframe](cubickeyframe.md) — A keyframe that uses a cubic curve to smoothly interpolate between values.
- [LinearKeyframe](linearkeyframe.md) — A keyframe that uses simple linear interpolation.
- [MoveKeyframe](movekeyframe.md) — A keyframe that immediately moves to the given value without interpolating.
- [SpringKeyframe](springkeyframe.md) — A keyframe that uses a spring function to interpolate to the given value.

### Creating custom animations

- [CustomAnimation](customanimation.md) — A type that defines how an animatable value changes over time.
- [AnimationContext](animationcontext.md) — Contextual values that a custom animation can use to manage state and access a view’s environment.
- [AnimationState](animationstate.md) — A container that stores the state for a custom animation.
- [AnimationStateKey](animationstatekey.md) — A key for accessing animation state values.
- [UnitCurve](unitcurve.md) — A  function defined by a two-dimensional curve that maps an input progress in the range [0,1] to an output progress that is also in the range [0,1]. By changing the shape of the curve, the effective speed of an animation or other interpolation can be changed.
- [Spring](spring.md) — A representation of a spring’s motion.

### Making data animatable

- [Animatable](animatable.md) — A type that describes how to animate a property of a view.
- [AnimatableValues](animatablevalues.md)
- [AnimatablePair](animatablepair.md) — A pair of animatable values, which is itself animatable.
- [VectorArithmetic](vectorarithmetic.md) — A type that can serve as the animatable data of an animatable type.
- [EmptyAnimatableData](emptyanimatabledata.md) — An empty type for animatable data.

### Updating a view on a schedule

- [Updating watchOS apps with timelines](../watchos-apps/updating-watchos-apps-with-timelines.md) — Seamlessly schedule updates to your user interface, even while it’s inactive.
- [TimelineView](timelineview.md) — A view that updates according to a schedule that you provide.
- [TimelineSchedule](timelineschedule.md) — A type that provides a sequence of dates for use as a schedule.
- [TimelineViewDefaultContext](timelineviewdefaultcontext.md) — Information passed to a timeline view’s content callback.

### Synchronizing geometries

- [matchedGeometryEffect(id:in:properties:anchor:isSource:)](<view/matchedgeometryeffect(id_in_properties_anchor_issource_).md>) — Defines a group of views with synchronized geometry using an identifier and namespace that you provide.
- [MatchedGeometryProperties](matchedgeometryproperties.md) — A set of view properties that may be synchronized between views using the `View.matchedGeometryEffect()` function.
- [GeometryEffect](geometryeffect.md) — An effect that changes the visual appearance of a view, largely without changing its ancestors or descendants.
- [Namespace](namespace.md) — A dynamic property type that allows access to a namespace defined by the persistent identity of the object containing the property (e.g. a view).
- [geometryGroup()](<view/geometrygroup().md>) — Isolates the geometry (e.g. position and size) of the view from its parent view.

### Defining transitions

- [transition(_:)](<view/transition(__).md>) — Associates a transition with the view.
- [Transition](transition.md) — A description of view changes to apply when a view is added to and removed from the view hierarchy.
- [TransitionProperties](transitionproperties.md) — The properties a `Transition` can have.
- [TransitionPhase](transitionphase.md) — An indication of which the current stage of a transition.
- [AsymmetricTransition](asymmetrictransition.md) — A composite `Transition` that uses a different transition for insertion versus removal.
- [AnyTransition](anytransition.md) — A type-erased transition.
- [contentTransition(_:)](<view/contenttransition(__).md>) — Modifies the view to use a given transition as its method of animating changes to the contents of its views.
- [contentTransition](environmentvalues/contenttransition.md) — The current method of animating the contents of views.
- [contentTransitionAddsDrawingGroup](environmentvalues/contenttransitionaddsdrawinggroup.md) — A Boolean value that controls whether views that render content transitions use GPU-accelerated rendering.
- [ContentTransition](contenttransition.md) — A kind of transition that applies to the content within a single view, rather than to the insertion or removal of a view.
- [PlaceholderContentView](placeholdercontentview.md) — A placeholder used to construct an inline modifier, transition, or other helper type.

### Defining matched transitions

- [matchedTransitionSource(id:in:)](<view/matchedtransitionsource(id_in_).md>) — Identifies this view as the source of a navigation transition, such as a zoom transition.
- [matchedTransitionSource(id:in:configuration:)](<view/matchedtransitionsource(id_in_configuration_).md>) — Identifies this view as the source of a navigation transition, such as a zoom transition.
- [MatchedTransitionSourceConfiguration](matchedtransitionsourceconfiguration.md) — A configuration that defines the appearance of a matched transition source.
- [EmptyMatchedTransitionSourceConfiguration](emptymatchedtransitionsourceconfiguration.md) — An unstyled matched transition source configuration.

### Defining navigation transitions

- [navigationTransition(_:)](<view/navigationtransition(__).md>) — Sets the navigation transition style for this view.
- [NavigationTransition](navigationtransition.md) — A type that defines the transition to use when navigating to a view.
- [AnyNavigationTransition](anynavigationtransition.md) — A type-erasing navigation transition that allows for providing any navigation transition value dynamically. _(beta)_
- [CrossFadeNavigationTransition](crossfadenavigationtransition.md) — A navigation transition that cross-fades between the appearing view and the disappearing view. _(beta)_

### Moving an animation to another view

- [withTransaction(_:_:)](<withtransaction(____).md>) — Executes a closure with the specified transaction and returns the result.
- [withTransaction(_:_:_:)](<withtransaction(______).md>) — Executes a closure with the specified transaction key path and value and returns the result.
- [transaction(_:)](<view/transaction(__).md>) — Applies the given transaction mutation function to all animations used within the view.
- [transaction(value:_:)](<view/transaction(value___).md>) — Applies the given transaction mutation function to all animations used within the view.
- [transaction(_:body:)](<view/transaction(__body_).md>) — Applies the given transaction mutation function to all animations used within the `body` closure.
- [Transaction](transaction.md) — The context of the current state-processing update.
- [Entry()](<entry().md>) — Creates an environment values, transaction, container values, or focused values entry.
- [TransactionKey](transactionkey.md) — A key for accessing values in a transaction.

### Deprecated types

- [AnimatableModifier](animatablemodifier.md) — A modifier that can create another modifier with animation. _(deprecated)_

## See Also

### Views

- [View fundamentals](view-fundamentals.md) — Define the visual elements of your app using a hierarchy of views.
- [View configuration](view-configuration.md) — Adjust the characteristics of views in a hierarchy.
- [View styles](view-styles.md) — Apply built-in and custom appearances and behaviors to different types of views.
- [Text input and output](text-input-and-output.md) — Display formatted text and get text input from the user.
- [Images](images.md) — Add images and symbols to your app’s user interface.
- [Controls and indicators](controls-and-indicators.md) — Display values and get user selections.
- [Menus and commands](menus-and-commands.md) — Provide space-efficient, context-dependent access to commands and controls.
- [Shapes](shapes.md) — Trace and fill built-in and custom shapes with a color, gradient, or other pattern.
- [Drawing and graphics](drawing-and-graphics.md) — Enhance your views with graphical effects and customized drawings.
