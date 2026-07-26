---
title: RelevanceKit
framework: RelevanceKit
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/relevancekit
source_url: 'https://developer.apple.com/documentation/relevancekit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/relevancekit.json'
content_hash: 'sha256:644ffa6721350e8d'
translated: false
---

> Navigation: [Technologies](technologies.md)

# RelevanceKit

<sub>Framework</sub>

Provide on-device intelligence with contextual clues that increase your widget’s visibility on Apple Watch.

## Overview

On Apple Watch, widgets appear in the Smart Stack in an order that best fits a person’s context. To order the widgets that appear in the Smart Stack, watchOS attempts to determine a widget’s relevance based on several factors, including contextual clues your app provides to the system.

To give your widget additional visibility in the watchOS Smart Stack and ensure it appears when a person needs it, use RelevanceKit to provide contextual clues that signal the widget’s relevance to the system. For example, your widget might be most useful at a specific location or time, or every time a person starts a workout.

Note that you use RelevanceKit in combination with [WidgetKit](widgetkit.md) and [App Intents](appintents.md) to provide interactive and contextually relevant widgets in the Smart Stack, including iPhone widgets that appear on Apple Watch. When you add an import statement for App Intents to your code, App Intents implicitly adds a dependence to RelevanceKit . You don’t need to explicitly add `import RelevanceKit` to your code.

For more information, refer to [Increasing the visibility of widgets in Smart Stacks](widgetkit/widget-suggestions-in-smart-stacks.md).

> [!note] Note
> Smart Stacks are available in iOS, iPadOS, and watchOS. However, functionality provided by RelevanceKit is only available in watchOS. Calling its API on other platforms doesn’t have any effect.

## Topics

### Providing relevance information

- [Increasing the visibility of widgets in Smart Stacks](widgetkit/widget-suggestions-in-smart-stacks.md) — Provide contextual information and donate intents to the system to make sure your widget appears prominently in Smart Stacks.
- [RelevantContext](relevancekit/relevantcontext.md) — Contextual clues the system uses to show relevant widgets in the Smart Stack on watchOS.

### Fitness clues

- [fitness(_:)](<relevancekit/relevantcontext/fitness(__).md>) — Tells the system a widget is relevant because of a person’s fitness activity.
- [FitnessCondition](relevancekit/relevantcontext/fitnesscondition.md) — Values that represent a person’s fitness activity.

### Hardware clues

- [hardware(headphones:)](<relevancekit/relevantcontext/hardware(headphones_).md>) — Tells the system a widget is relevant when a person’s headphones are connected.
- [HeadphonesCondition](relevancekit/relevantcontext/headphonescondition.md) — A structure that indicates whether a person’s headphones are connected.

### Location clues

- [location(_:)](<relevancekit/relevantcontext/location(__).md>) — Tells the system a widget is relevant at a specific location.
- [location(inferred:)](<relevancekit/relevantcontext/location(inferred_).md>) — Tells the system a widget is relevant at a person’s inferred location.
- [InferredLocation](relevancekit/relevantcontext/inferredlocation.md) — A structure with values for a person’s inferred home, work, school, and commute locations.

### Sleep clues

- [sleep(_:)](<relevancekit/relevantcontext/sleep(__).md>) — Tells the system a widget is relevant because of a person’s sleep schedule.
- [SleepCondition](relevancekit/relevantcontext/sleepcondition.md) — Values that represent a person’s typical bedtime or wakeup time.

### Time clues

- [date(_:)](<relevancekit/relevantcontext/date(__).md>) — Tells the system a widget is relevant at a specific date.
- [date(_:kind:)](<relevancekit/relevantcontext/date(__kind_).md>) — Tells the system a widget is relevant at a specific date and provides an additional contextual hint.
- [date(interval:kind:)](<relevancekit/relevantcontext/date(interval_kind_).md>) — Tells the system a widget is relevant for a time interval and provides an additional contextual hint.
- [date(range:kind:)](<relevancekit/relevantcontext/date(range_kind_).md>) — Tells the system a widget is relevant for a known date range and provides an additional contextual hint.
- [DateKind](relevancekit/relevantcontext/datekind.md) — Values the system uses as additional context for time-based relevance clues.
- [date(from:to:)](<relevancekit/relevantcontext/date(from_to_).md>) — Tells the system a widget is relevant between two dates. _(deprecated)_
