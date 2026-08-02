---
title: Accessibility Programming Guide for OS X
apple_id: TP40001078
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/documentation/Accessibility/Conceptual/AccessibilityMacOSX/OSXAXDeveloping.html
archived_at: '2026-07-15T03:49:09.619192Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Accessibility Programming Guide for OS X](index.md)



## Designing an Accessible OS X App

Designing your app with accessibility in mind not only allows you to reach a larger group of users, it results in a better experience for all your users. You’ve already made the design decision to develop an app that runs in OS X. Now, make sure you can deliver the Macintosh experience to all your users.

### Basic Design Guidelines

You should incorporate accessibility into your most fundamental design decisions. Building accessibility into your design results in a cleaner app and a better experience for all users. The following design guidelines are particularly important when developing an accessible app.

- __Familiarize yourself with the HIG.___OS X Human Interface Guidelines_ presents the best practices of app design that help you create a first-rate app for OS X. It also provides detailed specifications for designing and implementing an intuitive, consistent, and aesthetically pleasing user interface that delivers the superlative experience Macintosh users have come to expect. Furthermore, the Accessibility API assumes that your app follows these guidelines. Creating a fully-functional, accessible app is much easier when your app sticks closely to the HIG.
- __Support full keyboard navigation__. For many users, a mouse is difficult, if not impossible, to use. Consequently, a user should be able to perform all your app’s functions using the keyboard alone. As a secondary benefit, this also helps support power users, who often prefer keyboard shortcuts over mouse-based interfaces.
- __Don’t override built-in keyboard shortcuts__. As a general rule, never override reserved keyboard shortcuts. In particular, if you override accessibility-related keyboard shortcuts, users who have enabled full keyboard access cannot work with your app in the way they expect to. This caveat applies both to the keyboard shortcuts OS X reserves (listed in the _OS X Human Interface Guidelines_ appendix “Keyboard Shortcuts Quick Reference”) and to the accessibility-related keyboard shortcuts (listed in [Accessibility Keyboard Shortcuts](OSXAXKeyboardShortcuts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzyfvbuqmrvgmwugscejfdumqsi)).

  A corollary to this principle is to avoid creating too many new keyboard shortcuts that are specific to your app. Users should not have to memorize a new set of keyboard commands for each app they use.
- __Provide alternatives for drag-and-drop operations__. If your app relies on drag-and-drop operations in its workflow, provide alternative ways to accomplish the same tasks. This task may not be easy; in fact, for apps that are heavily dependent on drag and drop, you may have to design a different interface.

  For example, the original OS X Finder app was designed to provide a simple drag-and-drop interface to the file system. In keeping with its accessibility goals, however, the Finder adds keyboard support that allows users to copy and move files using keyboard commands instead of the mouse.
- __Make sure there’s always a way out of your app’s workflow__. Having a way out of your app’s workflow is important for all users, of course, but it’s essential for users of assistive technologies. A user relying on an accessibility client to use your app may have a somewhat narrower view of your app’s user interface. For this reason, it’s especially important to make canceling operations and retracing steps easy.

### Considering Specific Disabilities

Following the guidelines in [Basic Design Guidelines](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzyfvbuqmrqg4wugrkhirauercg) will help you design an easy-to-use app that is easy to access-enable. Still, there may be specific information about particular disabilities you don’t know. This information is useful to keep in mind during the design process.

The following sections describe some broad categories of disabilities and offer suggestions for specific design solutions and adaptations you can make. The main theme of these suggestions is to provide as many alternative modes of content display as possible. The more ways your app presents information, the easier it is for your users to find an approach that fits their needs.

### Visual Disabilities

Visual disabilities include blindness, color blindness, and low vision. In addition to making your app accessible to accessibility clients, such as screen readers, also consider the following:

- Although color can greatly enhance a user interface, make sure it is not the only source of information. A color blind user may not be able to distinguish between two objects that differ only in color.
- Provide an audio option to all visual cues and feedback. Your app should make it easy to replace visual communication with audio communication.
- Provide an option to present images and animated content in an alternative manner. If your app displays an image or animation, consider providing your own succinct descriptions of these elements so that blind or low-vision users can benefit from the information they convey.

### Hearing Disabilities

People with hearing disabilities may have difficulty distinguishing your app’s sound effects from ambient noise, or they may not be able to hear them at all. Users without hearing disabilities may find themselves in circumstances in which audio output from an app is inappropriate (in a library, for example). It is a good idea to consider these points as you design the audio output of your app.

Your app should not override the audio-output settings the user selects in System Preferences. It should also provide a visual option to all audio cues and feedback. For example, a “beep” can be replaced or accompanied by a flash of the display screen.

### Motor and Cognitive Disabilities

People with motor disabilities may need to use alternatives to the standard mouse and keyboard input devices. Other users may have difficulty with the fine motor control required to double-click a mouse or to press key combinations on the keyboard. Users with cognitive or learning disabilities may need extra time to complete tasks or respond to alerts.

For the most part, support for motor disabilities is provided at the hardware or operating-system level. OS X provides many such solutions in the Accessibility preferences. The Sticky Keys feature, for example, allows a user to type the keys in a key combination sequentially instead of simultaneously. As an app developer, therefore, the most important thing you can do is to access-enable your app so your users can deploy the assistive technologies of their choice.

A feature such as Sticky Keys can also be helpful to a user with a cognitive or learning disability that makes it difficult to perform simultaneous tasks. An app that provides its output in both visual and auditory modes (especially simultaneously) can enhance comprehension. Users with such disabilities also benefit from the redundancy provided by an app that employs both audio and visual output.

In addition to making your app accessible, consider incorporating the following features:

- __Provide options to adjust the length of expected response times.__ Users who have difficulty quickly responding to app events benefit from having extra time to respond. When a timed response is required—such as notification that a regularly scheduled action is about to take place—provide at least one response method that does not require users to respond within the timed interval. Alternatively, provide at least one method that allows users to increase the response time to at least five times the default setting.
- __Avoid using regularly blinking cursors or other objects onscreen.__ The frequency of a blinking object must not be in the range of 2 to 55 Hz, inclusive. Objects that blink in this frequency range can cause medical complications, such as seizures, in some people.

[Why Make Your App Accessible?](OSXAXwhy.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzyfvbuqmrqgywviucykjcummjqge)

[The OS X Accessibility Model](OSXAXmodel.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzyfvbuqmrqhawviucykjcummjqge)
