---
title: Timeline
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/timeline
source_url: 'https://developer.apple.com/documentation/widgetkit/timeline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/timeline.json'
content_hash: 'sha256:b4d83b04253fbf00'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# Timeline

<sub>Structure</sub>

An object that specifies a date for WidgetKit to update a widget’s view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
struct Timeline<EntryType> where EntryType : TimelineEntry
```

## Overview

To tell WidgetKit when to update a widget’s view, [TimelineProvider](timelineprovider.md) generates a timeline. The timeline contains an array of timeline entry objects and a refresh policy.

To create timeline entries, declare a custom type that conforms to `TimelineEntry`. Each entry specifies the date you would like WidgetKit to update the widget’s view, and any additional information that your widget needs to render the view. Timeline entries may also include information about their relevance compared to other entries in timelines for the same widget kind. WidgetKit uses this relevance information when considering whether a widget should be promoted in a stack. For more about supplying relevance information, see [TimelineEntryRelevance](timelineentryrelevance.md).

The timeline’s refresh policy specifies the earliest date for WidgetKit to request a new timeline from the provider. The default refresh policy, [atEnd](timelinereloadpolicy/atend.md), tells WidgetKit to request a new timeline after the last date in the array of timeline entries you provide. However, you can use [after(_:)](<timelinereloadpolicy/after(__).md>) to indicate a different date either earlier or later than the default date. Specify an earlier date if you know there’s a point in time before the end of your timeline entries that may alter the timeline. Conversely, specify a later date if you know that after the last date, your timeline won’t change for some period of time. Alternatively, use [never](timelinereloadpolicy/never.md) to tell WidgetKit not to request a new timeline at all. In that case, your app uses [WidgetCenter](widgetcenter.md) to prompt WidgetKit to request a new timeline.

> [!note] Note
> WidgetKit may not update the widget’s view exactly at a timeline entry’s date. The update may occur at a later date.

For more information about generating timelines, see [TimelineProvider](timelineprovider.md).

## Topics

### Creating a Timeline

- [init(entries:policy:)](<timeline/init(entries_policy_).md>) — Creates a timeline for when you want WidgetKit to update a widget’s view.

### Getting Timeline Properties

- [entries](timeline/entries.md) — An array of timeline entries.
- [policy](timeline/policy.md) — The policy that determines the earliest date and time WidgetKit requests a new timeline from a timeline provider.
- [TimelineReloadPolicy](timelinereloadpolicy.md) — A type that indicates the earliest date WidgetKit requests a new timeline from the widget’s provider.

## See Also

### Timeline updates

- [Keeping a widget up to date](keeping-a-widget-up-to-date.md) — Plan your widget’s timeline to show timely, relevant information using dynamic views, and update the timeline when things change.
- [TimelineProvider](timelineprovider.md) — A type that advises WidgetKit when to update a widget’s display.
- [AppIntentTimelineProvider](appintenttimelineprovider.md) — A type that advises WidgetKit when to update a user-configurable widget’s display.
- [IntentTimelineProvider](intenttimelineprovider.md) — A type that advises WidgetKit when to update a user-configurable widget’s display.
- [TimelineProviderContext](timelineprovidercontext.md) — An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.
- [TimelineEntry](timelineentry.md) — A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [WidgetCenter](widgetcenter.md) — An object that contains a list of user-configured widgets and is used for reloading widget timelines.
