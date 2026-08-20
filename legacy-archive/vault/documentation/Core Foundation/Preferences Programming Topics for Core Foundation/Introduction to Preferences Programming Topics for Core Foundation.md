---
title: Preferences Programming Topics for Core Foundation
apple_id: 10000129i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2006-10-03'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPreferences/CFPreferences.html
archived_at: '2026-07-15T07:22:42.166496Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Preferences%20Best%20Practices.md)

# Introduction to Preferences Programming Topics for Core Foundation

Most applications need to store and retrieve preferences to allow for user customization of application behavior and provide a way to keep track of configuration settings across multiple launches. Frameworks and libraries can also use preferences to store configuration information. Core Foundation preferences provide a simple and standard way to maintain preferences for both types of use.

Preferences allow you to store values that are associated with a key that can later be used to “look up” the preference value when you need it. Key/value pairs are assigned a scope using a combination of username, application ID, and host (computer) name. This mechanism allows you to create preferences which apply to different classes of users. For example, using preferences you can save a preference value that applies to:

- The current user of your application on the current host
- All users of your application on a specific host connected to the local network
- The current user of your application on any host connected to the local network
- Any user of any application on any host connected to the local network

Preferences has a high-level API which makes it very simple to store and retrieve application preferences using the default scope (current user, any host) which is appropriate for the majority of situations. There is also a low-level API which allows you to specify the exact scope of a preference value when necessary.

Preferences uses the Core Foundation property list types to store and retrieve preference values. Readers unfamiliar with property lists should consult the Core Foundation Topic _[Property List Programming Topics for Core Foundation](../Property%20List%20Programming%20Topics%20for%20Core%20Foundation/Introduction%20to%20Property%20List%20Programming%20Topics%20for%20Core%20Foundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezta2i)_ for more information.

This topic contains conceptual information you need to understand in order to use the preferences API, and examples that demonstrate how to save and retrieve preference values. The concepts covered in this topic are:

- [Preferences Best Practices](Preferences%20Best%20Practices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytemjzfvbuuqsfjjbeqsa)
- [Application IDs](Application%20IDs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dolkdjjbeksscjbea)
- [Preference Domains](Preference%20Domains.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dqlkdjjbeksscjbea)

The tasks covered in this topic are:

- [Using the High-Level Preferences API](Using%20the%20High-Level%20Preferences%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dslkdjjbekscbifdq)
- [Using the Low-Level Preferences API](Using%20the%20Low-Level%20Preferences%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3talkdjjbekscbifdq)

[Next](Preferences%20Best%20Practices.md)

