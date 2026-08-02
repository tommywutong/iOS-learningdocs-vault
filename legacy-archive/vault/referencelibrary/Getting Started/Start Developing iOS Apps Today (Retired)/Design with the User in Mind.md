---
title: Start Developing iOS Apps Today (Retired)
apple_id: TP40013837
resource_type: Guide
platform: iOS
topic: null
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/RoadMapiOS-Legacy/chapters/RM_iHIG_Station/Fundamentals/Fundamentals.html
archived_at: '2026-07-18T02:47:15.302980Z'
---
> 导航：[总目录](../../../README.md) · [referencelibrary](../../../_indexes/referencelibrary.md) · [Start Developing iOS Apps Today (Retired)](Document%20Revision%20History.md)



[Back to Human Interface Design](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/RoadMapiOS-Legacy/chapters/HumanInterfaceDesign.html)
!
!
!

# Retired Document

__Important:__ This version of _Start Developing iOS Apps Today_ has been retired. The replacement version provides a new, more streamlined walkthrough of the basics. For information covering the same subject area as this page, please see _[iOS Human Interface Guidelines](https://developer.apple.com/library/ios/documentation/UserExperience/Conceptual/MobileHIG/index.html#//apple_ref/doc/uid/TP40006556)_.

# Design with the User in Mind

The success of an iOS app depends largely on the quality of its user interface. If users don’t find an app attractive and easy to use, even the fastest, most powerful, most full-featured app can languish in the App Store.

There are many ways to get from initial inspiration to popular app, and there is no single path that guarantees success. But there is one directive on which all successful app development depends: Design with the user in mind. The strategies and best practices summarized below are all based on this directive, and they represent a few of the many principles and guidelines you need to follow as you design an app. When you’re ready to get to work, be sure to read _iOS Human Interface Guidelines_ for the complete story.

If you're new to iOS, your first step is to become an iOS user yourself. Then, as much as possible, explore the characteristics of the iOS platform as a user, not as a developer. Whether you've used iOS-based devices from the beginning or you've never held one before, take the time to articulate your expectations and analyze your actions as you use the device.

![image: ../Art/IntroUserInterface_2x.png](attachments/chapters/RM_iHIG_Station/Art/IntroUserInterface_2x.png)

For example, consider how the following device and software features affect the user experience:

- iPhone, iPad, and iPod touch are handheld devices that enable and encourage people to use them on the go. People expect apps to start quickly and be easy to use in a wide variety of environments.
- On all iOS-based devices, the display is paramount, regardless of its size. The comparatively small device margin around the display becomes almost invisible while people are engaged in using apps.
- The Multi-Touch interface allows people to manipulate content without the intervention of another device, such as a mouse. People tend to feel more in control of the app experience because they can use touch to manipulate onscreen elements.
- Only one app at a time is frontmost. Users can use the multitasking bar to switch between apps quickly and easily, but the experience differs from seeing multiple apps open simultaneously on a computer display.
- In general, apps don’t open separate windows at the same time. Instead, users transition between screens of content, each of which can contain multiple views.
- The built-in Settings app contains user preferences for both the device and some of the apps that run on it. To open Settings, users must switch away from the app they’re currently using, so these preferences are of the “set once and rarely change” variety. Most apps can avoid adding preferences to Settings and can instead allow people to make choices within the app’s main user interface.

Remember that a great iOS app embraces the platform it runs on and provides an experience that seamlessly integrates device and platform features.

As a user, you notice when an app makes it hard to tell whether it received your input, or when a popover seems to emerge from different areas on the screen without apparent reason. In cases like these, what you notice is the app’s failure to follow the fundamental principles of human interface design.

In this context, the term human interface refers to the interaction between people and devices, including the software that runs on them. An app (or a device) is easy and enjoyable for people to use when its human interface builds on the ways in which people actually think and behave.

Apple’s human interface design principles codify several high-level aspects of human-device interaction that have a perceptible effect on the user experience. As you design your app, keep in mind the following principles of HI design:

- __Aesthetic integrity__. Aesthetic integrity is not a measure of how beautiful an app is; rather, it’s a measure of how well the appearance of the app integrates with its function.
- __Consistency__. Consistency in the interface allows people to transfer their knowledge and skills from one app to another. Ideally, an app is consistent with the iOS standards, within itself, and with earlier versions of itself.
- __Direct manipulation__. When people directly manipulate onscreen objects instead of using separate controls to manipulate them, they're more engaged with the task and they more readily understand the results of their actions.
- __Feedback__. Feedback acknowledges people’s actions and assures them that processing is occurring. For example, people expect immediate feedback when they operate a control, and they appreciate status updates during lengthy operations.
- __Metaphors__. When virtual objects and actions in an app are metaphors for objects and actions in the real world, users quickly grasp how to use the app. The most appropriate metaphors suggest a usage or experience without enforcing the limitations of the real-world object or action on which they’re based.
- __User control__. Although an app can suggest a course of action or warn about dangerous consequences, it’s usually a mistake for the app to take decision-making away from the user. The best apps find the correct balance between giving people the capabilities they need and helping them avoid dangerous outcomes.

_iOS Human Interface Guidelines_ guidelines that range from user experience recommendations to specific rules that govern the usage of iOS technologies and onscreen elements. This section does not function as a summary of _iOS Human Interface Guidelines_; rather, it gives you a taste of the types of guidelines that help you design a successful app.

Great iOS apps give people streamlined access to the content they care about. To do this, these apps incorporate user experience guidelines such as these:

- Focus on the primary task.
- Make usage easy and obvious.
- Use user-centric terminology.
- Make targets fingertip-size.
- De-emphasize settings.
- Use user interface (UI) elements consistently.
- Use subtle animation to communicate.
- Ask people to save only when necessary.

Users expect apps to incorporate platform features such as multitasking, iCloud, VoiceOver, and printing. Even though users might think of these features as automatically available, app developers know that they must do work to integrate them. To make sure that an app provides the expected user experience for these features, developers follow iOS technology guidelines such as these:

- Support iCloud storage simply and transparently.
- Be prepared for multitasking-related interruptions and be ready to resume.
- Comply with the user’s Notification Center settings when handling local and push notifications.
- Supply descriptive information so that the app is accessible to VoiceOver users.
- Rely on the system-provided printing UI to enable a printing experience users appreciate.
- Ensure that sounds meet users’ expectations in all situations.

When an app correctly uses UI elements, such as buttons and tab bars, users are likely to notice only that the app behaves as they expect. But when an app uses UI elements incorrectly, users are often quick to voice their dissatisfaction. Great iOS apps take care to follow UI element usage guidelines. For example:

- Ensure that the back button in a navigation bar displays the title of the previous screen.
- Don’t remove a tab from a tab bar when its function is unavailable.
- Avoid providing a “dismiss popover” button.
- Always provide feedback when users select an item listed in a table view.
- On iPad, present a picker only within a popover.
- Use system-provided buttons and icons according to their documented meaning.
- When designing custom icons and images, use universal imagery that all users understand and avoid replicating Apple UI elements or products.

Again, the guidelines listed in this section represent a fraction of the guidelines contained in _iOS Human Interface Guidelines_. Reading that document in its entirety is an essential step in the app development process.

The most successful iOS apps are often the result of thoughtful design iteration. When developers focus on the main task and continue to refine their list of features, they can create a superior user experience. The strategies summarized in this section can help you refine your idea, review design options, and converge on an app that people will appreciate.

__Distill the feature list__. As early as possible in the design process, define precisely what your app does and who your target audience is. Use this definition (called an application definition statement) to filter out unnecessary features and to guide the style of the app. Although it’s tempting to think that more features make a better app, the opposite is more often true. The best apps tend to focus on enabling a main task and providing only those features that users need to accomplish the task.

__Design for the device__. In addition to integrating the patterns of the iOS user interface and user experience, make sure that your app feels at home on the device. If you plan to develop a universal app (that is, an app that runs on both iPhone and iPad), this means that you must design a different UI for each device, even though much of the underlying code can be the same. Similarly, if you plan to start with web-based content, it’s essential that you redesign the content to look and feel like a native app.

__Customize appropriately__. Every app includes some UI customization, if only in its App Store icon. The iOS SDK gives you the ability to customize every aspect of the UI, so it’s up to you to decide how much customization is appropriate. The best apps balance customization with clarity of purpose and ease of use. Ideally, you want users to recognize the distinctiveness of your app, while at the same time appreciating the consistency that makes an app intuitive and easy to use.

__Prototype and iterate__. Soon after you’ve decided what features to include, begin creating testable prototypes. Early prototypes don’t need to display real UI or art and they don’t need to handle real content, but they do need to give testers an accurate idea of how the app works. During testing, pay particular attention to what testers try and fail to do, because those attempts can reveal places where the app appears to promise a behavior that it doesn’t deliver. Continue testing until you’re satisfied that users can easily grasp how the app works and operate all its features.

[Back to Human Interface Design](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/RoadMapiOS-Legacy/chapters/HumanInterfaceDesign.html)
!
!
!
