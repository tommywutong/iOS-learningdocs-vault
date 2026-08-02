---
title: Settings Application Schema Reference
apple_id: TP40007071
resource_type: Guide
platform: watchOS|tvOS|iOS
topic: Data Management
technology: null
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/PreferenceSettings/Conceptual/SettingsApplicationSchemaReference/Introduction/Introduction.html
archived_at: '2026-07-18T01:51:37.197512Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](Schema%20File%20Root%20Content.md)

# Introduction

Preferences for iOS and tvOS apps are displayed by the system-provided Settings app. Preferences for WatchKit extensions are displayed by the system-provided Apple Watch app. A settings bundle contains the information needed by these system apps to display your preferences and make it possible for the user to modify them. The system apps save the corresponding values to the defaults database so that your app can retrieve them at runtime.

This document describes the elements that comprise the schema files you include in a settings bundle. All bundles must have the root content. The inclusion of other elements is based on your needs and the preferences you plan to display.

For information about creating a settings bundle for an iOS app, see Application Preferences in _[App Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072)_.

For information about creating a settings bundle for a WatchKit extension, see _[App Programming Guide for watchOS](https://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969)_.

Each article in this document describes the keys associated with a particular element of a preferences schema file:

- [Schema File Root Content](Schema%20File%20Root%20Content.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tamjyfvjvomi) describes the keys found at the root level of the schema file.
- [Group Element](Group%20Element.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tambzfvjvomi) describes the keys found in a `PSGroupSpecifier` element.
- [Child Pane Element](Child%20Pane%20Element.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tamjxfvjvomi) describes the keys found in a `PSChildPaneSpecifier` element.
- [Toggle Switch Element](Toggle%20Switch%20Element.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tamjsfvjvomi) describes the keys found in a `PSToggleSwitchSpecifier` element.
- [Slider Element](Slider%20Element.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tamjtfvjvomi) describes the keys found in a `PSSliderSpecifier` element.
- [Title Element](Title%20Element.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tamjvfvjvomi) describes the keys found in a `PSTitleValueSpecifier` element.
- [Text Field Element](Text%20Field%20Element.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tamjrfvjvomi) describes the keys found in a `PSTextFieldSpecifier` element.
- [Multi Value Element](Multi%20Value%20Element.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tamjwfvjvomi) describes the keys found in a `PSMultiValueSpecifier` element.
- [Radio Group Element](Radio%20Group%20Element.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbzge2tcojwfvjvomq) describes the keys found in a `PSRadioGroupSpecifier` element.

[Next](Schema%20File%20Root%20Content.md)

