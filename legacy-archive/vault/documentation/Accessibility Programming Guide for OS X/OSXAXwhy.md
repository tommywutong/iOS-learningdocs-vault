---
title: Accessibility Programming Guide for OS X
apple_id: TP40001078
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/documentation/Accessibility/Conceptual/AccessibilityMacOSX/OSXAXwhy.html
archived_at: '2026-07-15T03:49:19.611846Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Accessibility Programming Guide for OS X](index.md)



## Why Make Your App Accessible?

Accessibility encompasses more than just providing an alternative to a mouse-driven user interface. At its core, accessibility is about enabling individuals and supporting their viewpoints and working styles. This chapter presents several compelling reasons why you should access-enable every app you develop.

### Increase Your User Base

Millions of people have a disability or special needs, from visual and hearing impairments, to physical disabilities, to cognitive and learning challenges. For these people, access to computers is vitally important, because computers can provide a level of independence that is difficult to attain any other way.

As populations around the world age, an increasing number of people experience age-related disabilities, such as vision or hearing loss. Unlike earlier generations, members of the currently aging population are more accustomed to using computers in their daily lives. They are more likely to store a large portion of their meaningful data in digital form and to embrace digital communication. Current and future generations of the elderly expect to be able to continue using their computers and accessing their data, regardless of the state of their vision and hearing. Therefore, apps that support customizable text displays, access by a screen reader, or the replacement of visual cues by audible ones can serve this population well.

Even people who don’t necessarily identify themselves as disabled can benefit from alternative ways of interacting with apps. Consider a person suffering from carpal tunnel syndrome (a painful condition caused by the compression of a nerve in the wrist) who prefers an app that provides keyboard alternatives to its mouse-driven user interface. By providing alternative ways to use your app, you allow users to choose their own ways to work and express themselves, which ultimately broadens your user base.

### Enter New Markets

Federal regulations such as section 508 of the Rehabilitation Act of 1973 in the United States stipulate that computers used in government or educational settings must provide reasonable access for people with disabilities. As this regulation and others like it take effect, entrance into these markets is dependent upon your ability to supply accessible apps.

Like the localization issue a few years ago, accessibility has evolved from a good idea to an essential component of competitive apps. Apple is committed to providing the best platform from which to enter these markets. By access-enabling your app and deploying it on OS X, you make your app more attractive to these markets.

### Take Advantage of OS X Assistive Features

OS X is designed to accommodate assistive technologies and has many built-in features to help people with disabilities. Users access most of this functionality through the Accessibility pane of System Preferences. Some of these built-in technologies take advantage of the same accessibility architecture that allows external assistive technologies to access your app.

For example, VoiceOver, the built-in spoken interface introduced in OS X version 10.4, relies on the accessibility architecture to make the navigation and use of the system accessible to users with visual disabilities. As soon as you access-enable your app, VoiceOver helps a visually impaired user interact with it.

### It’s Not Difficult

AppKit integrates accessibility into its API. When you are using standard views and controls, most of accessibility comes for free. This integration lets you focus on providing your app-specific information to assistive technologies, which enhances the user’s experience and highlights your app’s unique features.

If you have an established app, you’ll find that the OS X accessibility architecture is designed to allow you to access-enable your app in a selective way, letting you enjoy the benefits of accessibility without having to redesign your app.

[About OS X Accessibility](index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzyfvbuqmrvgqwvgvzr)

[Designing an Accessible OS X App](OSXAXDeveloping.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzyfvbuqmrqg4wueqkci5fegr2h)
