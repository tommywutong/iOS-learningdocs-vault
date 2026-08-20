---
title: Dashboard Programming Topics
apple_id: TP40002837
resource_type: Guide
platform: Safari|macOS
topic: Networking, Internet, & Web
technology: null
published: '2010-02-01'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashboard_ProgTopics/Articles/AppleClasses.html
archived_at: '2026-07-15T05:17:18.535399Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dashboard Programming Topics](Introduction%20to%20Dashboard%20Programming%20Topics.md)


[Next](Using%20Scroll%20Areas.md)[Previous](Designing%20Widgets.md)

# Introduction to the Apple Classes

Starting with OS X v10.4.3, Apple provides you with a set of JavaScript classes that make it easy to incorporate common controls and utilities into your widget. These classes, called _Apple Classes_, include:

- A scroll area and scroll bars
- Sliders
- Animation timers
- Buttons, including the standard glass-style button
- The Info button

The Apple Classes are found in `/System/Library/WidgetResources/AppleClasses/` and can be used from there or from within your widget, depending on whether backward compatibility is a concern.

There are two ways to use any Apple Class in your widget: so that your widget is backward compatible with OS X versions 10.4 to 10.4.2, or so your widget runs on OS X v10.4.3 and later.

Since the Apple Classes are included with OS X starting with version 10.4.3, you may want to use a class yet deploy the widget on OS X versions 10.4 to 10.4.2. To do this, follow these steps:

1. Copy the needed Apple Classes out of `/System/Library/WidgetResources/` into a folder, named `AppleClasses`, at the top level of your widget's bundle.
2. In your main HTML file, include the needed classes using a local file path, like this:

```
<script type='text/javascript' src='AppleClasses/AppleInfoButton.js' charset='utf-8'/>
```
3. In your `Info.plist` information property list file, include the key `BackwardsCompatibleClassLookup` and set its value to the boolean value `YES`.

By copying the needed Apple Classes inside in your widget and including the local copy in your main HTML file, your widget uses the local copies, ensuring that the classes are available to your widget no matter what version of OS X v.10.4 the widget is running on.

Note that the Info.plist key `BackwardsCompatibleClassLookup` has special meaning on OS X v.10.4.3 and later. When Dashboard sees this key and any `<script>` tag that includes a file with `AppleClasses/` as the first part of its path, it automatically provides your widget with the corresponding version located in `/System/Library/WidgetResources/` instead of the local copy. This allows you to use the most up-to-date version of an Apple Class in future versions of OS X while retaining backward compatibility with earlier versions of OS X v.10.4.

If you intend for your widget to only work on OS X version 10.4.3 and later, you can omit any backward compatibility steps and just include the JavaScript files for the needed classes at the their location in `/System/Library/WidgetResources/`, like this:

```
<script type='text/javascript' src='/System/Library/WidgetResources/AppleClasses/AppleInfoButton.js' charset='utf-8'/>
```


Read these articles to learn more about the Apple Classes and how to use them:

| Apple Class | Correlating Articles |
| --- | --- |
| `AppleScrollArea` and `AppleScrollbar`, used to create a region with scrollable content. | [Using Scroll Areas](Using%20Scroll%20Areas.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztenbrfvjvomq) |
| `AppleSlider`, used to add a slider control to your widget. | [Using an Apple Slider](Using%20an%20Apple%20Slider.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztenbsfvjvomq) |
| `AppleAnimator`, an automatic timer that generate values based on a predefined curve. | [Using Animation](Using%20Animation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcobxfvjvomi) |
| `AppleButton`, used primarily to add a standard glass-styled button to your widget. | [Using an Apple Button](Using%20an%20Apple%20Button.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcobvfvjvoni), [Widget Backs and Preferences](Widget%20Backs%20and%20Preferences.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztanbtfvjvomy) (specifically the [In Your HTML File](Widget%20Backs%20and%20Preferences.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztanbtfvjvony) and [In Your JavaScript File](Widget%20Backs%20and%20Preferences.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztanbtfvjvoni) sections) |
| `AppleInfoButton`, used on a widget's front to signify that a widget has a back. When clicked, it flips the widget over. | [Widget Backs and Preferences](Widget%20Backs%20and%20Preferences.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztanbtfvjvomy) (specifically the [In Your HTML File](Widget%20Backs%20and%20Preferences.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztanbtfvjvony) and [In Your JavaScript File](Widget%20Backs%20and%20Preferences.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztanbtfvjvoni) sections) |

[Next](Using%20Scroll%20Areas.md)[Previous](Designing%20Widgets.md)

