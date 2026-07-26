---
title: TimelineProviderContext
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/timelineprovidercontext
source_url: 'https://developer.apple.com/documentation/widgetkit/timelineprovidercontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/timelineprovidercontext.json'
content_hash: 'sha256:9181ac43113d9234'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# TimelineProviderContext

<sub>Structure</sub>

An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
struct TimelineProviderContext
```

## Overview

When requesting timelines for a widget, WidgetKit passes the [TimelineProvider](timelineprovider.md) a context object that includes details about how the widget appears. These details include:

- The [WidgetFamily](widgetfamily.md); for example, [WidgetFamily.systemSmall](widgetfamily/systemsmall.md) and  [WidgetFamily.systemMedium](widgetfamily/systemmedium.md).
- The size, in points, of the widget.
- Variants of the environments where the widget might appear.
- Whether the widget appears as a preview in the widget gallery.

If your widget uses assets that take time to generate or depend on the specific environment they’re rendered in, you can use the environment variants to generate those assets in advance. Some of the common environment properties to consider include:

- [colorScheme](../swiftui/environmentvalues/colorscheme.md), where you use different assets for light and dark schemes.
- [displayScale](../swiftui/environmentvalues/displayscale.md), where your widget might appear in both @1x and @2x displays on macOS devices.

To be responsive when the environment changes, WidgetKit may render the widget’s view in advance. For example, WidgetKit renders both light and dark versions of the widget so that if the color scheme changes, the correct version is immediately available.

## Topics

### Preparing Preview Content

- [isPreview](timelineprovidercontext/ispreview.md) — A Boolean value that indicates when the widget appears in the widget gallery.

### Accessing Size Attributes

- [family](timelineprovidercontext/family.md) — The user-configured family of the widget: small, medium, or large.
- [displaySize](timelineprovidercontext/displaysize.md) — The size, in points, of the widget.

### Accessing Environment Variations

- [environmentVariants](timelineprovidercontext/environmentvariants-swift.property.md) — All environment values that might be set when a widget appears.
- [EnvironmentVariants](timelineprovidercontext/environmentvariants-swift.struct.md) — A structure containing all varieties of environments where a widget could appear.

## See Also

### Timeline updates

- [Keeping a widget up to date](keeping-a-widget-up-to-date.md) — Plan your widget’s timeline to show timely, relevant information using dynamic views, and update the timeline when things change.
- [TimelineProvider](timelineprovider.md) — A type that advises WidgetKit when to update a widget’s display.
- [AppIntentTimelineProvider](appintenttimelineprovider.md) — A type that advises WidgetKit when to update a user-configurable widget’s display.
- [IntentTimelineProvider](intenttimelineprovider.md) — A type that advises WidgetKit when to update a user-configurable widget’s display.
- [TimelineEntry](timelineentry.md) — A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [Timeline](timeline.md) — An object that specifies a date for WidgetKit to update a widget’s view.
- [WidgetCenter](widgetcenter.md) — An object that contains a list of user-configured widgets and is used for reloading widget timelines.
