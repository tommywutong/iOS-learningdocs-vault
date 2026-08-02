---
title: QuickTime Video Effects and Transitions Guide
apple_id: TP40000868
resource_type: Guide
platform: macOS
topic: null
technology: QuickTime
published: '2009-06-01'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/RM/EffectsTransitions/Effects/A-Intro/1Introduction.html
archived_at: '2026-07-18T02:05:03.952756Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](https://developer.apple.com/library/archive/documentation/QuickTime/RM/EffectsTransitions/Effects/B-Chapter/2HowToAddQuickTimeVi.html)

# Introduction to QuickTime Video Effects and Transitions Guide

This book introduces you to QuickTime video effects and transitions. You can use effects and transitions to control the visual transition between two sources. Sources can be tracks in a QuickTime movie or they can be graphics worlds. You can use filter effects to visually alter a single source, such as applying a blur or ripple. You can also use free-standing effects, such as a cloud or fire effect, that do not require a source (though they can be composited with other video).

Because visual effects are calculated and executed at runtime, they typically result in a much smaller file than a pre-rendered version of the same effect.

Effects tracks can be created, edited, and used in essentially the same manner as other video tracks. You can “stack” effects by using one effects track as the source for another effect. You can also use an effect as the source for a sprite track, making the fire effect into a sprite, for example.

QuickTime includes over 145 effects, and its extensible architecture allows you to create additional effects of your own if you need them in your application development.

You need to read this document if you are writing an application that creates QuickTime movies and you want to add video effects to those movies, or if you want to use video effects on graphics worlds without creating a QuickTime movie, or if you want to create new video effects of your own.

This document discusses the high-level functions available to you that provide your application with pre-packaged access to the video effects architecture, and are designed to be easy to use and give you access to the most common uses of the QuickTime Video Effects architecture.

The low-level functions provide more complex and comprehensive interfaces to the effects dialog functionality. Using the low-level functions, you can gain more control over the standard parameters dialog box, such as the ability to incorporate user interface elements from the dialog box into your own application-defined dialog box.

This document is divided into five chapters:

- [How To Add QuickTime Video Effects](https://developer.apple.com/library/archive/documentation/QuickTime/RM/EffectsTransitions/Effects/B-Chapter/2HowToAddQuickTimeVi.html#//apple_ref/doc/uid/TP40000868-HowToAddQuickTimeVideoEffects-SW1) discusses how QuickTime video effects are implemented and how you can add effects to QuickTime movies.
- [Constructing a Video Effects User Interface](https://developer.apple.com/library/archive/documentation/QuickTime/RM/EffectsTransitions/Effects/C-Chapter/3ConstructingaVideoE.html#//apple_ref/doc/uid/TP40000868-ConstructingaVideoEffectsUserInterface-SW1) discusses how to construct a user interface that enables users to select an effect, change its parameters, and preview the results.
- [Built-in QuickTime Video Effects](https://developer.apple.com/library/archive/documentation/QuickTime/RM/EffectsTransitions/Effects/D-Chapter/4Built-inQuickTimeVi.html#//apple_ref/doc/uid/TP40000868-BuiltinQuickTimeVideoEffects-SW1) discusses SMTPE effects, which are implementations of over 100 standard effects defined by the Society of Motion Picture and Television Engineers, plus the set of effects implemented by Apple Computer, which you can use for a variety of purposes.
- [Creating New Video Effects](https://developer.apple.com/library/archive/documentation/QuickTime/RM/EffectsTransitions/Effects/E-Chapter/5CreatingNewVideoEff.html#//apple_ref/doc/uid/TP40000868-CreatingNewVideoEffects-SW1) describes how you can create your own video effects. The chapter walks you through the implementation of a sample effect component. The sample effect is built on a framework of code that you can reuse when you implement your own effect component.
- [Video Effects API](https://developer.apple.com/library/archive/documentation/QuickTime/RM/EffectsTransitions/Effects/F-Chapter/6VideoEffectsAPI.html#//apple_ref/doc/uid/TP40000868-VideoEffectsAPI-SW1) describes the constants, data types, and functions defined in QuickTime that support video effects.

The following Apple books cover related aspects of QuickTime programming:

- _[QuickTime Overview](QuickTime%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojs)_ gives you the starting information you need to do QuickTime programming.
- _[QuickTime Movie Basics](QuickTime%20Movie%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmby)_ introduces you to some of the basic concepts you need to understand when working with QuickTime movies.
- _QuickTime Guide for Windows_ provides information specific to programming for QuickTime on the Windows platform.
[Next](https://developer.apple.com/library/archive/documentation/QuickTime/RM/EffectsTransitions/Effects/B-Chapter/2HowToAddQuickTimeVi.html)

