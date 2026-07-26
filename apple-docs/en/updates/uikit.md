---
title: UIKit updates
framework: Updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/updates/uikit
source_url: 'https://developer.apple.com/documentation/updates/uikit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/updates/uikit.json'
content_hash: 'sha256:d7a727203b33e88d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Updates](../updates.md)

# UIKit updates

<sub>Article</sub>

Learn about important changes to UIKit.

## Overview

Browse notable changes in [UIKit](../uikit.md).

## June 2026

### General

- Align sensor data from Core Location and Core Motion with your app’s UI orientation by setting a [UIView](../uikit/uiview.md) as the body of a [CLLocationManager](../corelocation/cllocationmanager.md) or [CMMotionManager](../coremotion/cmmotionmanager.md) instance.
- Use [UICollectionViewCompositionalLayoutSectionProvider](../uikit/uicollectionviewcompositionallayoutsectionprovider.md) closures as part of automatic observation tracking to automatically invalidate and update compositional layouts when observable objects change.
- Use [UIRefreshControl](../uikit/uirefreshcontrol.md) and [UIStepper](../uikit/uistepper.md) in Mac apps built with Mac Catalyst. These controls are now fully supported in the Mac idiom.

### App life cycle

- Adopt the UIKit scene-based life cycle using the guidance in [Transitioning to the UIKit scene-based life cycle](../uikit/transitioning-to-the-uikit-scene-based-life-cycle.md). Starting in iOS 27, apps built with the latest SDK must use the scene-based life cycle or they fail to launch.

### Drag and drop

- Control drag initiation timing in gesture-rich views by configuring [UIDragInteraction](../uikit/uidraginteraction.md). Use [allowsPointerDragBeforeLiftDelay](../uikit/uidraginteraction/allowspointerdragbeforeliftdelay.md) to independently control when pointer-initiated drags begin.

### Text views

- Override viewport layout methods directly in a [UITextView](../uikit/uitextview.md) subclass by conforming to [NSTextViewportLayoutControllerDelegate](../uikit/nstextviewportlayoutcontrollerdelegate.md).
- Register a [UITextAttachmentViewProviderReusePolicy](../uikit/uitextattachmentviewproviderreusepolicy.md) on `UITextView` to retain attachment views during scrolling and editing, preventing flicker and preserving view state.
- Use [NSTextTable](../uikit/nstexttable.md), [NSTextBlock](../uikit/nstextblock.md), and [NSTextTableBlock](../uikit/nstexttableblock.md) to represent table structures in attributed strings.
- Access paragraph text blocks using [textBlocks](../uikit/nsparagraphstyle/textblocks.md).
- Use [NSTextViewportRenderingSurface](../uikit/nstextviewportrenderingsurface.md) to render text in custom views and layers, and [NSTextViewportRenderingSurfaceKey](../uikit/nstextviewportrenderingsurfacekey.md) to identify them for caching.

## June 2025

### General

- Provide seamless immersive visuals by using [UIBackgroundExtensionView](../uikit/uibackgroundextensionview.md) to extend a view’s content under sidebars and inspectors.
- Apply Liquid Glass effects to views using [UIGlassEffect](../uikit/uiglasseffect.md).
- Organize views together for morph animations in [UIGlassContainerEffect](../uikit/uiglasscontainereffect.md).
- Add or adjust effects at the edge of a scroll view with [UIScrollEdgeEffect](../uikit/uiscrolledgeeffect.md).
- Apply Liquid Glass effects to buttons with [glass()](<../uikit/uibutton/configuration-swift.struct/glass().md>) and [prominentGlass()](<../uikit/uibutton/configuration-swift.struct/prominentglass().md>).
- UIKit now supports Swift Observable objects. Use observable objects in [layoutSubviews()](<../uikit/uiview/layoutsubviews().md>); then UIKit automatically invalidates and updates the UI when those objects change.
- Add a badge to a [UIBarButtonItem](../uikit/uibarbuttonitem.md) with [badge](../uikit/uibarbuttonitem/badge-4sz3f.md).
- Notification payloads are now strongly typed: [NotificationCenter.MessageIdentifier](../foundation/notificationcenter/messageidentifier.md).

### Menu bar in iPadOS

- Swipe from the top to reveal an iPad app’s full menu. Menus on iPad support images, submenus, inline sections, checkmarks, and more.
- Configure main menus with [UIMainMenuSystem](../uikit/uimainmenusystem.md).

### High dynamic range (HDR)

- [UIColorPickerViewController](../uikit/uicolorpickerviewcontroller.md) supports picking HDR colors, with a maximum supported exposure value.
- Observe [UITraitHDRHeadroomUsageLimit](../uikit/uitraithdrheadroomusagelimit-swift.struct.md) to automatically adjust HDR usage when a view with HDR content is not in focus.

## June 2024

### General

- Leverage automatic trait usage tracking inside key update methods such as [layoutSubviews()](<../uikit/uiview/layoutsubviews().md>), eliminating the need for manual trait change registration and invalidation.
- Add repeat, wiggle, breathe, and rotate effects to [SF Symbols](https://developer.apple.com/sf-symbols/).
- Take advantage of enhancements to [UIListContentConfiguration](../uikit/uilistcontentconfiguration-swift.struct.md), which now automatically updates to match the style of the containing list by using the new [UIListEnvironment](../uikit/uilistenvironment.md) trait from the trait collection, removing the need to instantiate a configuration for a specific list style yourself.
- Opt out or restrict collaboration on certain types of data through the share sheet using [UIActivityCollaborationMode](../uikit/uiactivitycollaborationmode.md).
- Select a specific week of the year in [UICalendarView](../uikit/uicalendarview.md) using the new [UICalendarSelectionWeekOfYear](../uikit/uicalendarselectionweekofyear.md) selection option.
- Observe, participate in, and affect the UI update process using [UIUpdateLink](../uikit/uiupdatelink.md).

### Navigation

- Showcase your app and its unique identity with a new, customizable launch design for document-based apps. In UIKit, define [launchOptions](../uikit/uidocumentviewcontroller/launchoptions-swift.property.md) on your [UIDocumentViewController](../uikit/uidocumentviewcontroller.md).
- Make your app’s navigation more immersive by adopting the new tab bar on iPad. If your app presents a rich hierarchy of tab items, set the  [mode](../uikit/uitabbarcontroller/mode-swift.property.md) to [UITabBarController.Mode.tabSidebar](../uikit/uitabbarcontroller/mode-swift.enum/tabsidebar.md) to automatically switch between the tab bar and sidebar representations. In SwiftUI, use [sidebarAdaptable](../swiftui/tabviewstyle/sidebaradaptable.md).
- Transition between views in a way that feels fluid and consistent using a systemwide zoom transition. In UIKit, configure your view controller’s [preferredTransition](../uikit/uiviewcontroller/preferredtransition.md) to [zoom(options:sourceViewProvider:)](<../uikit/uiviewcontroller/transition/zoom(options_sourceviewprovider_).md>). In SwiftUI, use [zoom(sourceID:in:)](<../swiftui/navigationtransition/zoom(sourceid_in_).md>).

### Framework interoperability

- Reuse existing UIKit gesture recognizer code in SwiftUI. In SwiftUI, create UIKit gesture recognizers using [UIGestureRecognizerRepresentable](../swiftui/uigesturerecognizerrepresentable.md). In UIKit, refer to SwiftUI gestures by name using [name](../uikit/uigesturerecognizer/name.md).

### visionOS

- Support more varieties of list layouts by configuring whether section headers stretch to fill the entire width of the list or shrink to tightly hug their content. For collection views, use [contentHuggingElements](../uikit/uicollectionlayoutlistconfiguration-swift.struct/contenthuggingelements-swift.property.md) on [UICollectionLayoutListConfiguration](../uikit/uicollectionlayoutlistconfiguration-swift.struct.md). For table views, use [contentHuggingElements](../uikit/uitableview/contenthuggingelements.md) on [UITableView](../uikit/uitableview.md).
- Animate SF Symbols on visionOS using the symbol effects API and [UIImageView](../uikit/uiimageview.md).
- Apply hierarchical vibrant text color to labels using [UIColor.Prominence](../uikit/uicolor/prominence-swift.enum.md).
- Specify an action to perform without shifting the focus away from the keyboard using [keyboardAction](../uikit/uitextinputassistantitem/keyboardaction.md).
- Push a new scene in place of an existing scene using [UIWindowScenePushPlacement](../uikit/uiwindowscenepushplacement-swift.struct.md). The new scene appears in the same position as the original scene, hiding it. Closing the new scene makes the original scene reappear.

### tvOS

- Create a unifying color theme in your app by specifying an accent color in your app’s asset catalog, which is now supported in tvOS.

## June 2023

### General

- Preview your views and view controllers alongside your code using the new `#Preview` Swift macro.
- Take advantage of a new view controller appearance callback, [viewIsAppearing(_:)](<../uikit/uiviewcontroller/viewisappearing(__).md>), to run code that depends on the view’s initial geometry. The system calls this method when both the view and view controller have an up-to-date trait collection, and after the superview adds the view to the hierarchy and lays it out. This method deploys back to iOS 13.
- Learn about enhancements to the trait system, which let you define custom traits for your own data, quickly change trait values throughout the view hierarchy, and register for trait changes in more flexible ways. For more information, see WWDC23 session 10057: [Unleash the UIKit trait system](https://developer.apple.com/videos/play/wwdc2023/10057/).
- Display and manage empty state consistently in your app with [UIContentUnavailableConfiguration](../uikit/uicontentunavailableconfiguration-swift.struct.md), which provides new system standard styles and layouts for common empty states. Help people understand why no content is present, and when possible, provide guidance on how to add content.
- Create a powerful text experience in your app. Define richer interactions by changing the default tap or menu behavior when interacting with a text item. If you implement a custom UI for displaying text, support the redesigned text cursor by adopting the new text selection UI. Mark up text fields with additional text content types to help people fill out forms even faster. For more information, see WWDC23 session 10058: [What’s new with text and text interactions](https://developer.apple.com/videos/play/wwdc2023/10058/).
- Let people drop supported files and content onto your app icon on the Home Screen to open them in your app. To make sure your app is properly configured, verify that your `Info.plist` file specifies the file types your app supports using [CFBundleDocumentTypes](../bundleresources/information-property-list/cfbundledocumenttypes.md).

### Accessibility and internationalization

- Simplify how you maintain your accessibility code with block-based setters for accessibility attributes. Make sure people receive the most important information first by specifying a default, low, or high priority for announcements. Enhance custom accessibility elements with the new toggle and zoom accessibility traits.
- Create a great text experience for international users by testing your UI in all languages. Adopt text styles to take advantage of enhancements to the font system, like improved wrapping and hyphenation for Chinese, German, Japanese, and Korean, as well as enhancements for variable line heights that improve legibility in several languages, including Arabic, Hindi, Thai, and Vietnamese. Access localized variants of symbol images by specifying a locale.

### iPadOS

- Help people customize their Stage Manager configuration by including a larger target area for dragging windows. Leverage new resizing behavior for split view controllers to get the most out of your UI in Stage Manager.
- Support scrolling of your scroll view content with hardware keyboard shortcuts. This behavior is enabled by default, which you can override using [allowsKeyboardScrolling](../uikit/uiscrollview/allowskeyboardscrolling.md).
- Simplify document management in your document-centric apps. Set your `UIDocument` subclass as the rename delegate of a navigation item to handle file renaming automatically. Build your content view controller from `UIDocumentViewController`, which provides a system default experience for managing documents: automatically configuring the title menu, sharing, drag and drop, key commands, and more. For more information, see WWDC23 session 10056: [Build better document-centric apps](https://developer.apple.com/videos/play/wwdc2023/10056/).
- Enhance the Apple Pencil experience in your iPadOS app. Give your app a sense of depth by using [UIHoverGestureRecognizer](../uikit/uihovergesturerecognizer.md) to draw a preview of the stroke. Support the beautiful new inks in PencilKit, including monoline, fountain pen, watercolor, and crayon.

### Views and controls

- Animate symbol images with new symbol effects, including bounce, pulse, variable color, scale, appear, disappear, and replace.
- Build even more performant apps with flexible layouts using collection views. Apply diffable data source snapshots and perform batch updates with even better performance. Use the [uniformAcrossSiblings(estimate:)](<../uikit/nscollectionlayoutdimension/uniformacrosssiblings(estimate_).md>) dimension for compositional layouts to specify uniform size across sibling items, with smaller items increasing in size to match their largest sibling.
- Simplify spring animations by providing duration and bounce parameters for the new view animation method, [animate(springDuration:bounce:initialSpringVelocity:delay:options:animations:completion:)](<../uikit/uiview/animate(springduration_bounce_initialspringvelocity_delay_options_animations_completion_).md>).
- Represent fractional progress through a page of content with page controls.
- Display and manipulate high dynamic range (HDR) images.
- Display your menu as a palette with [displayAsPalette](../uikit/uimenu/options-swift.struct/displayaspalette.md) for it to appear as a row of menu elements for choosing from a collection of items.
- Take advantage of the [UIStatusBarStyle.default](../uikit/uistatusbarstyle/default.md) status bar style, which now automatically chooses a light or dark appearance that maintains contrast with the content underneath it.

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
