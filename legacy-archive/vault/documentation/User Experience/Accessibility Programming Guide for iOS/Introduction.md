---
title: Accessibility Programming Guide for iOS
apple_id: TP40008785
resource_type: Guide
platform: tvOS|iOS
topic: User Experience
technology: UIKit
published: '2012-02-16'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/iPhoneAccessibility/Introduction/Introduction.html
archived_at: '2026-07-18T02:14:06.034643Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Understanding%20Accessibility%20on%20iOS.md)

# Introduction

Using iOS 3.0 and later, VoiceOver is available to help users with visual impairments use their iOS-based devices. The UI Accessibility programming interface, introduced in iOS 3.0, helps developers make their applications accessible to VoiceOver users. Briefly, VoiceOver describes an application’s user interface and helps users navigate through the application’s views and controls, using speech and sound. Users familiar with VoiceOver in Mac OS X can leverage their experience to help them quickly come up to speed using VoiceOver on their devices.

iPhone applications that run in iOS 3.0 and later should be accessible to VoiceOver users. iOS and the iOS SDK support this goal by:

- Making standard UIKit controls and views accessible by default
- Supplying the UI Accessibility programming interface, which defines a streamlined process for making an iPhone application accessible
- Providing tools that help you implement accessibility in your code and test the accessibility of your application

If you’re developing or updating an iPhone application, you should read this document to learn how to make your application accessible to VoiceOver users.

This document contains the following chapters:

- [Understanding Accessibility on iOS](Understanding%20Accessibility%20on%20iOS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doobvfvbuqmjqgawvgvzr) briefly describes how VoiceOver works on the device and introduces the programming interface and tools you can use to make your application accessible.
- [Making Your iOS App Accessible](Making%20Your%20iOS%20App%20Accessible.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doobvfvbuqmjqgiwvgvzv) provides in-depth guidance for making your application accessible to VoiceOver users.

This document used to contain information related to testing your app’s accessibility experience with VoiceOver and Accessibility Inspector. That content has moved to a dedicated document titled _[Verifying App Accessibility on iOS](https://developer.apple.com/library/archive/technotes/TestingAccessibilityOfiOSApps/TestingtheAccessibilityofiOSApps/TestingtheAccessibilityofiOSApps.html#//apple_ref/doc/uid/TP40012619)_.

[Next](Understanding%20Accessibility%20on%20iOS.md)

