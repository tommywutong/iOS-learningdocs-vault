---
title: Safari HTML Reference
apple_id: TP40002049
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: User Experience
technology: WebKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariHTMLRef/Articles/MetaTags.html
archived_at: '2026-07-15T05:19:06.493563Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari HTML Reference](Introduction.md)


[Next](Supported%20Accessibility%20Roles.md)[Previous](Supported%20Input%20Values.md)

# Supported Meta Tags

Apple-specific `meta` tags are described here.

Sets whether a web application runs in full-screen mode.

____Syntax____: |  |
```
<meta name="apple-mobile-web-app-capable" content="yes">
```

____Discussion____: If `content` is set to `yes`, the web application runs in full-screen mode; otherwise, it does not. The default behavior is to use Safari to display web content.

You can determine whether a webpage is displayed in full-screen mode using the `window.navigator.standalone` read-only Boolean JavaScript property.

____Availability____: Available for iOS.

____Support Level____: Apple extension.

Sets the style of the status bar for a web application.

____Syntax____: |  |
```
<meta name="apple-mobile-web-app-status-bar-style" content="black">
```

____Discussion____: This meta tag has no effect unless you first specify full-screen mode as described in apple-`[apple-mobile-web-app-capable](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojtfvjvomy)`.

If `content` is set to `default`, the status bar appears normal. If set to `black`, the status bar has a black background. If set to `black-translucent`, the status bar is black and translucent. If set to `default` or `black`, the web content is displayed below the status bar. If set to `black-translucent`, the web content is displayed on the entire screen, partially obscured by the status bar. The default value is `default`.

____Availability____: Available for iOS.

____Support Level____: Apple extension.

Enables or disables automatic detection of possible phone numbers in a webpage in Safari on iOS.

____Syntax____: |  |
```
<meta name="format-detection" content="telephone=no">
```

____Discussion____: By default, Safari on iOS detects any string formatted like a phone number and makes it a link that calls the number. Specifying `telephone=no` disables this feature.

____Support Level____: Apple extension.

Changes the logical window size used when displaying a page on iOS.

____Syntax____: |  |
```
<meta name = "viewport" content = "width = 320,
       initial-scale = 2.3, user-scalable = no">
```

____Discussion____: Use the viewport meta key to improve the presentation of your web content on iOS. Typically, you use the viewport meta tag to set the width and initial scale of the viewport.

For example, if your webpage is narrower than `980` pixels, then you should set the width of the viewport to fit your web content. If you are designing a Safari on iOS-specific web application, you should set the width to the width of the device.

[Table 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojtfvjvony) describes the properties supported by the viewport meta key and their default values. When providing multiple properties for the viewport meta key, you should use a comma-delimited list of assignment statements. Follow these rules when setting multiple properties:

- Do not use a semicolon as a delimiter.
- A space may work as a delimiter, but a comma is preferred.
- For numeric properties, if the value contains a nonnumeric character but starts with a number, then the number prefix is used as the value. For example, `1.0x` is equivalent to `1.0` and `123x456` is equivalent to `123`. If the parameter doesn’t begin with a number, the value is `0`.

When referring to the dimensions of a device, you should use the constants described in [Table 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojtfvjvooa) instead of hard-coding specific numeric values. For example, use `device-width` instead of `320` for the width, and `device-height` instead of `480` for the height in portrait orientation.

You do not need to set every viewport property. If only a subset of the properties are set, then Safari on iOS infers the other values. For example, if you set the scale to `1.0`, Safari assumes the width is `device-width` in portrait and `device-height` in landscape orientation. Therefore, if you want the width to be `980` pixels and the initial scale to be `1.0`, then set both of these properties.

For example, to set the viewport width to the width of the device, add this to your HTML file:

```
<meta name = "viewport" content = "width = device-width">
```

To set the initial scale to `1.0`, add this to your HTML file:

```
<meta name = "viewport" content = "initial-scale = 1.0">
```

To set the initial scale and to turn off user scaling, add this to your HTML file:

```
<meta name = "viewport" content = "initial-scale = 2.3, user-scalable = no">
```

Use the Safari on iOS console to help debug your webpages as described in the _[Safari Web Inspector Guide](../Safari%20Web%20Inspector%20Guide/About%20Safari%20Web%20Inspector.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzu)_. The console contains tips to help you choose viewport values—for example, it reminds you to use the constants when referring to the device width and height.

____Support Level____: Apple extension.

__Table 1__  Viewport properties

| Property | Description |
| `width` | The width of the viewport in pixels. The default is `980`. The range is from `200` to `10,000`.  You can also set this property to the constants described in [Table 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojtfvjvooa). |
| `height` | The height of the viewport in pixels. The default is calculated based on the value of the width property and the aspect ratio of the device. The range is from `223` to `10,000` pixels.  You can also set this property to the constants described in [Table 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojtfvjvooa). |
| `initial-scale` | The initial scale of the viewport as a multiplier. The default is calculated to fit the webpage in the visible area. The range is determined by the `minimum-scale` and `maximum-scale` properties.  You can set only the initial scale of the viewport—the scale of the viewport the first time the webpage is displayed. Thereafter, the user can zoom in and out unless you set `user-scalable` to `no`. Zooming by the user is also limited by the `minimum-scale` and `maximum-scale` properties. |
| `minimum-scale` | Specifies the minimum scale value of the viewport. The default is `0.25`. The range is from >`0` to `10.0`. |
| `maximum-scale` | Specifies the maximum scale value of the viewport. The default is `5.0`. The range is from >`0` to `10.0`. |
| `user-scalable` | Determines whether or not the user can zoom in and out—whether or not the user can change the scale of the viewport. Set to `yes` to allow scaling and `no` to disallow scaling. The default is `yes`.  Setting `user-scalable` to `no` also prevents a webpage from scrolling when entering text in an input field. |

__Table 2__  Special viewport property values

| Value | Description |
| `device-width` | The width of the device in pixels. |
| `device-height` | The height of the device pixels. |

[Next](Supported%20Accessibility%20Roles.md)[Previous](Supported%20Input%20Values.md)

