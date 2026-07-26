---
title: watchOS updates
framework: Updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/updates/watchos
source_url: 'https://developer.apple.com/documentation/updates/watchos'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/updates/watchos.json'
content_hash: 'sha256:4259b86398b60f40'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Updates](../updates.md)

# watchOS updates

<sub>Article</sub>

Learn about important changes to watchOS.

## Overview

Browse notable changes in [watchOS apps](../watchos-apps.md).

## September 2024

### Watch sizes

- Apple Watch Series 10 are larger and have a different aspect ratio than previous watches. The watch is 1mm larger than the Series 9 (42mm and 46mm), but the screen gains more width than height. Use [scenePadding(_:)](<../swiftui/view/scenepadding(__).md>) to align text with the text margins, and [ignoresSafeArea(_:edges:)](<../swiftui/view/ignoressafearea(__edges_).md>) to extend content beyond the watch’s safe area.

### Shallow dives

- Apple Watch Series 10 supports the Shallow Depth and Pressure capability. Use [CMWaterSubmersionManager](../coremotion/cmwatersubmersionmanager.md) to start a shallow dive session, and [underwaterDepth](../healthkit/hkquantitytypeidentifier/underwaterdepth.md) and [waterTemperature](../healthkit/hkquantitytypeidentifier/watertemperature.md) to read depth and temperature samples from HealthKit.

## June 2024

### Water temperature

- Access water temperature data from swimming workouts. Apple Watch Ultra records [waterTemperature](../healthkit/hkquantitytypeidentifier/watertemperature.md) samples during swimming workouts.

### Double tap

- Specify which control responds to the double tap gesture using the [handGestureShortcut(_:isEnabled:)](<../swiftui/view/handgestureshortcut(__isenabled_).md>) view modifier, passing [primaryAction](../swiftui/handgestureshortcut/primaryaction.md) as the parameter. Double tap can interact with any buttonlike controls, such as buttons or toggles.

### Creating workouts

- Create custom pool swimming workouts with the [HKWorkoutActivityType.swimming](../healthkit/hkworkoutactivitytype/swimming.md) activity.
- Set a distance-with-time goal for custom swimming workouts with the [WorkoutGoal.poolSwimDistanceWithTime(_:_:)](<../workoutkit/workoutgoal/poolswimdistancewithtime(____).md>) goal.
- Provide a custom name to a workout step using the [WorkoutStep](../workoutkit/workoutstep.md) structure’s [displayName](../workoutkit/workoutstep/displayname.md).
- Preview workouts on Apple Watch using the [workoutPreview(_:isPresented:)](<../swiftui/view/workoutpreview(__ispresented_).md>) view modifier.
- Set average power goals for cycling and running with [PowerThresholdAlert](../workoutkit/powerthresholdalert.md) and [PowerRangeAlert](../workoutkit/powerrangealert.md).
- Set pace goals for indoor running with the [SpeedThresholdAlert](../workoutkit/speedthresholdalert.md) and [SpeedRangeAlert](../workoutkit/speedrangealert.md) targets.

## September 2023

- When someone performs a Double Tap gesture while viewing a notification on Apple Watch Series 9 or Apple Watch Ultra 2, the system invokes the first nondestructive action. A nondestructive action doesn’t include the [destructive](../usernotifications/unnotificationactionoptions/destructive.md) option, and won’t delete user data or change the app irrevocably.

## June 2023

- Use the new watchOS user interface design to simplify navigation, better use the Digital Crown, and enrich the app experience. For more information, see [Designing for watchOS](../design/human-interface-guidelines/designing-for-watchos.md) and [Creating an intuitive and effective UI in watchOS 10](../watchos-apps/creating-an-intuitive-and-effective-ui-in-watchos-10.md).
- Update your WidgetKit-based complications to take advantage of the Smart Stack on Apple Watch. People can scroll down to see relevant widgets directly on the watch face using the Digital Crown. For more information, see [Increasing the visibility of widgets in Smart Stacks](../widgetkit/widget-suggestions-in-smart-stacks.md).
- Use curved text along the bevel or around the corners in WidgetKit-based complications.
- Add state preservation and restoration to watchOS apps. For more information, see [Preserving your app’s UI across launches](../uikit/preserving-your-app-s-ui-across-launches.md).
- Use WorkoutKit to create goal, pacer, multisport, and fully custom interval workouts. Display a preview of the workout that shows the workout details, and sync workouts with a paired Apple Watch. For more information, see   [WorkoutKit](../workoutkit.md).
- Access batches of high-frequency accelerometer and device motion data during workouts. Use this data to analyze motion — such as a golf or baseball swing — after the action occurs. For more information, see [Core Motion](../coremotion.md).
- Use Core Motion’s water submersion manager to monitor shallow dives on Apple Watch Ultra. For more information, see [Core Motion](../coremotion.md).
- Support Bluetooth cycling sensors. People can pair power, cadence, and speed sensors to Apple Watch to enhance their cycling workouts. You can access this data using HealthKit for live and historical workouts.

## See Also

### Technology and frameworks

- [Accelerate updates](accelerate.md) — Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md) — Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md) — Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md) — Learn about important changes to AdAttributionKit.
- [App Clips updates](appclips.md) — Learn about important changes in App Clips.
- [App Intents updates](appintents.md) — Learn about important changes in App Intents.
- [AppKit updates](appkit.md) — Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md) — Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](applemapsserverapi.md) — Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](applepencil.md) — Learn about important changes to Apple Pencil.
- [ARKit updates](arkit.md) — Learn about important changes to ARKit.
- [Audio Toolbox updates](audiotoolbox.md) — Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](authenticationservices.md) — Learn about important changes to AuthenticationServices.
- [AVFAudio updates](avfaudio.md) — Learn about important changes to AVFAudio.
- [AVFoundation updates](avfoundation.md) — Learn about important changes to AVFoundation.
