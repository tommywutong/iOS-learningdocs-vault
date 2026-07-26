---
title: EnvironmentValues
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues.json'
content_hash: 'sha256:7dc438c1191f3a5f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# EnvironmentValues

<sub>Structure</sub>

A collection of environment values propagated through a view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct EnvironmentValues
```

## Overview

SwiftUI exposes a collection of values to your app’s views in an `EnvironmentValues` structure. To read a value from the structure, declare a property using the [Environment](environment.md) property wrapper and specify the value’s key path. For example, you can read the current locale:

```swift
@Environment(\.locale) var locale: Locale
```

Use the property you declare to dynamically control a view’s layout. SwiftUI automatically sets or updates many environment values, like [pixelLength](environmentvalues/pixellength.md), [scenePhase](environmentvalues/scenephase.md), or [locale](environmentvalues/locale.md), based on device characteristics, system state, or user settings. For others, like [lineLimit](environmentvalues/linelimit.md), SwiftUI provides a reasonable default value.

You can set or override some values using the [environment(_:_:)](<view/environment(____).md>) view modifier:

```swift
MyView()
    .environment(\.lineLimit, 2)
```

The value that you set affects the environment for the view that you modify — including its descendants in the view hierarchy — but only up to the point where you apply a different environment modifier.

SwiftUI provides dedicated view modifiers for setting some values, which typically makes your code easier to read. For example, rather than setting the [lineLimit](environmentvalues/linelimit.md) value directly, as in the previous example, you should instead use the [lineLimit(_:)](<view/linelimit(__).md>) modifier:

```swift
MyView()
    .lineLimit(2)
```

In some cases, using a dedicated view modifier provides additional functionality. For example, you must use the [preferredColorScheme(_:)](<view/preferredcolorscheme(__).md>) modifier rather than setting [colorScheme](environmentvalues/colorscheme.md) directly to ensure that the new value propagates up to the presenting container when presenting a view like a popover:

```swift
MyView()
    .popover(isPresented: $isPopped) {
        PopoverContent()
            .preferredColorScheme(.dark)
    }
```

Create a custom environment value by declaring a new property in an extension to the environment values structure and applying the [Entry()](<entry().md>) macro to the variable declaration:

```swift
extension EnvironmentValues {
    @Entry var myCustomValue: String = "Default value"
}

extension View {
    func myCustomValue(_ myCustomValue: String) -> some View {
        environment(\.myCustomValue, myCustomValue)
    }
}
```

Clients of your value then access the value in the usual way, reading it with the [Environment](environment.md) property wrapper, and setting it with the `myCustomValue` view modifier.

## Relationships

- **Conforms To**: [CustomStringConvertible](../swift/customstringconvertible.md)

## Topics

### Creating and accessing values

- [init()](<environmentvalues/init().md>) — Creates an environment values instance.
- [subscript(_:)](<environmentvalues/subscript(__).md>) — Accesses the environment value associated with a custom key.
- [description](environmentvalues/description.md) — A string that represents the contents of the environment values instance.

### Accessibility

- [accessibilityAssistiveAccessEnabled](environmentvalues/accessibilityassistiveaccessenabled.md) — A Boolean value that indicates whether Assistive Access is in use.
- [accessibilityDimFlashingLights](environmentvalues/accessibilitydimflashinglights.md) — Whether the setting to reduce flashing or strobing lights in video content is on. This setting can also be used to determine if UI in playback controls should be shown to indicate upcoming content that includes flashing or strobing lights.
- [accessibilityDifferentiateWithoutColor](environmentvalues/accessibilitydifferentiatewithoutcolor.md) — Whether the system preference for Differentiate without Color is enabled.
- [accessibilityEnabled](environmentvalues/accessibilityenabled.md) — A Boolean value that indicates whether the user has enabled an assistive technology.
- [accessibilityInvertColors](environmentvalues/accessibilityinvertcolors.md) — Whether the system preference for Invert Colors is enabled.
- [accessibilityLargeContentViewerEnabled](environmentvalues/accessibilitylargecontentviewerenabled.md) — Whether the Large Content Viewer is enabled.
- [accessibilityPlayAnimatedImages](environmentvalues/accessibilityplayanimatedimages.md) — Whether the setting for playing animations in an animated image is on. When this value is false, any presented image that contains animation should not play automatically.
- [accessibilityPrefersHeadAnchorAlternative](environmentvalues/accessibilityprefersheadanchoralternative.md) — Whether the system setting to prefer alternatives to head-anchored content is on.
- [accessibilityPrefersCrossFadeTransitions](environmentvalues/accessibilitypreferscrossfadetransitions.md) — A Boolean value that indicates whether the Reduce Motion and the Prefer Cross-Fade Transitions settings are in an enabled state.
- [accessibilityQuickActionsEnabled](environmentvalues/accessibilityquickactionsenabled.md) — A Boolean that indicates whether the quick actions feature is enabled.
- [accessibilityReduceMotion](environmentvalues/accessibilityreducemotion.md) — Whether the system preference for Reduce Motion is enabled.
- [accessibilityReduceTransparency](environmentvalues/accessibilityreducetransparency.md) — Whether the system preference for Reduce Transparency is enabled.
- [accessibilityShowButtonShapes](environmentvalues/accessibilityshowbuttonshapes.md) — Whether the system preference for Show Button Shapes is enabled. _(deprecated)_
- [accessibilitySwitchControlEnabled](environmentvalues/accessibilityswitchcontrolenabled.md) — A Boolean value that indicates whether the Switch Control motor accessibility feature is in use.
- [accessibilityVoiceOverEnabled](environmentvalues/accessibilityvoiceoverenabled.md) — A Boolean value that indicates whether the VoiceOver screen reader is in use.
- [legibilityWeight](environmentvalues/legibilityweight.md) — The font weight to apply to text.

### Actions

- [dismiss](environmentvalues/dismiss.md) — An action that dismisses the current presentation.
- [dismissSearch](environmentvalues/dismisssearch.md) — An action that ends the current search interaction.
- [dismissWindow](environmentvalues/dismisswindow.md) — A window dismissal action stored in a view’s environment.
- [openImmersiveSpace](environmentvalues/openimmersivespace.md) — An action that presents an immersive space.
- [dismissImmersiveSpace](environmentvalues/dismissimmersivespace.md) — An immersive space dismissal action stored in a view’s environment.
- [newDocument](environmentvalues/newdocument.md) — An action in the environment that presents a new document.
- [openDocument](environmentvalues/opendocument.md) — An action in the environment that presents an existing document.
- [openURL](environmentvalues/openurl.md) — An action that opens a URL.
- [openWindow](environmentvalues/openwindow.md) — A window presentation action stored in a view’s environment.
- [pushWindow](environmentvalues/pushwindow.md) — A window presentation action stored in a view’s environment.
- [purchase](environmentvalues/purchase.md) — An action that starts an in-app purchase.
- [refresh](environmentvalues/refresh.md) — A refresh action stored in a view’s environment.
- [rename](environmentvalues/rename.md) — An action that activates the standard rename interaction.
- [resetFocus](environmentvalues/resetfocus.md) — An action that requests the focus system to reevaluate default focus.
- [openSettings](environmentvalues/opensettings.md) — A Settings presentation action stored in a view’s environment.

### Authentication

- [authorizationController](environmentvalues/authorizationcontroller.md) — A value provided in the SwiftUI environment that views can use to perform authorization requests.
- [webAuthenticationSession](environmentvalues/webauthenticationsession.md) — A value provided in the SwiftUI environment that views can use to authenticate a user through a web service.

### Controls and input

- [buttonRepeatBehavior](environmentvalues/buttonrepeatbehavior.md) — Whether buttons with this associated environment should repeatedly trigger their actions on prolonged interactions.
- [controlSize](environmentvalues/controlsize.md) — The size to apply to controls within a view.
- [defaultWheelPickerItemHeight](environmentvalues/defaultwheelpickeritemheight.md) — The default height of an item in a wheel-style picker, such as a date picker.
- [keyboardShortcut](environmentvalues/keyboardshortcut.md) — The keyboard shortcut that buttons in this environment will be triggered with.
- [menuIndicatorVisibility](environmentvalues/menuindicatorvisibility.md) — The menu indicator visibility to apply to controls within a view.
- [menuOrder](environmentvalues/menuorder.md) — The preferred order of items for menus presented from this view.
- [searchSuggestionsPlacement](environmentvalues/searchsuggestionsplacement.md) — The current placement of search suggestions.
- [preferredPencilDoubleTapAction](environmentvalues/preferredpencildoubletapaction.md) — The action that the user prefers to perform after double-tapping their Apple Pencil, as selected in the Settings app.
- [preferredPencilSqueezeAction](environmentvalues/preferredpencilsqueezeaction.md) — The action that the user prefers to perform when squeezing their Apple Pencil, as selected in the Settings app.

### Display characteristics

- [appearsActive](environmentvalues/appearsactive.md) — Whether views and styles in this environment should prefer an active appearance over an inactive appearance.
- [colorScheme](environmentvalues/colorscheme.md) — The color scheme of this environment.
- [colorSchemeContrast](environmentvalues/colorschemecontrast.md) — The contrast associated with the color scheme of this environment.
- [displayScale](environmentvalues/displayscale.md) — The display scale of this environment.
- [horizontalSizeClass](environmentvalues/horizontalsizeclass.md) — The horizontal size class of this environment.
- [imageScale](environmentvalues/imagescale.md) — The image scale for this environment.
- [pixelLength](environmentvalues/pixellength.md) — The size of a pixel on the screen.
- [sidebarRowSize](environmentvalues/sidebarrowsize.md) — The current size of sidebar rows.
- [verticalSizeClass](environmentvalues/verticalsizeclass.md) — The vertical size class of this environment.
- [immersiveSpaceDisplacement](environmentvalues/immersivespacedisplacement.md) — The displacement that the system applies to the immersive space when moving the space away from its default position, in meters.
- [labelsVisibility](environmentvalues/labelsvisibility.md) — The labels visibility set by [labelsVisibility(_:)](<view/labelsvisibility(__).md>).
- [materialActiveAppearance](environmentvalues/materialactiveappearance.md) — The behavior materials should use for their active state, defaulting to `automatic`.
- [TabBarPlacement](tabbarplacement.md) — A placement for tabs in a tab view.
- [toolbarLabelStyle](environmentvalues/toolbarlabelstyle.md) — The label style to apply to controls within a toolbar.

### Global objects

- [calendar](environmentvalues/calendar.md) — The current calendar that views should use when handling dates.
- [documentConfiguration](environmentvalues/documentconfiguration.md) — The configuration of a document in a [DocumentGroup](documentgroup.md).
- [locale](environmentvalues/locale.md) — The current locale that views should use.
- [managedObjectContext](environmentvalues/managedobjectcontext.md)
- [modelContext](environmentvalues/modelcontext.md) — The SwiftData model context that will be used for queries and other model operations within this environment.
- [timeZone](environmentvalues/timezone.md) — The current time zone that views should use when handling dates.
- [undoManager](environmentvalues/undomanager.md) — The undo manager used to register a view’s undo operations.

### Scrolling

- [isScrollEnabled](environmentvalues/isscrollenabled.md) — A Boolean value that indicates whether any scroll views associated with this environment allow scrolling to occur.
- [horizontalScrollIndicatorVisibility](environmentvalues/horizontalscrollindicatorvisibility.md) — The visibility to apply to scroll indicators of any horizontally scrollable content.
- [verticalScrollIndicatorVisibility](environmentvalues/verticalscrollindicatorvisibility.md) — The visiblity to apply to scroll indicators of any vertically scrollable content.
- [scrollDismissesKeyboardMode](environmentvalues/scrolldismisseskeyboardmode.md) — The way that scrollable content interacts with the software keyboard.
- [horizontalScrollBounceBehavior](environmentvalues/horizontalscrollbouncebehavior.md) — The scroll bounce mode for the horizontal axis of scrollable views.
- [verticalScrollBounceBehavior](environmentvalues/verticalscrollbouncebehavior.md) — The scroll bounce mode for the vertical axis of scrollable views.

### State

- [editMode](environmentvalues/editmode.md) — An indication of whether the user can edit the contents of a view associated with this environment.
- [isActivityFullscreen](environmentvalues/isactivityfullscreen.md) — A Boolean value that indicates whether the Live Activity appears in a full-screen presentation.
- [isEnabled](environmentvalues/isenabled.md) — A Boolean value that indicates whether the view associated with this environment allows user interaction.
- [isFocused](environmentvalues/isfocused.md) — Returns whether the nearest focusable ancestor has focus.
- [isFocusEffectEnabled](environmentvalues/isfocuseffectenabled.md) — A Boolean value that indicates whether the view associated with this environment allows focus effects to be displayed.
- [isHoverEffectEnabled](environmentvalues/ishovereffectenabled.md) — A Boolean value that indicates whether the view associated with this environment allows hover effects to be displayed.
- [isLuminanceReduced](environmentvalues/isluminancereduced.md) — A Boolean value that indicates whether the display or environment currently requires reduced luminance.
- [isPresented](environmentvalues/ispresented.md) — A Boolean value that indicates whether the view associated with this environment is currently presented.
- [isSceneCaptured](environmentvalues/isscenecaptured.md) — The current capture state.
- [isSearching](environmentvalues/issearching.md) — A Boolean value that indicates when the user is searching.
- [isTabBarShowingSections](environmentvalues/istabbarshowingsections.md) — A Boolean value that determines whether a tab view shows the expanded contents of a tab section.
- [scenePhase](environmentvalues/scenephase.md) — The current phase of the scene.
- [supportsMultipleWindows](environmentvalues/supportsmultiplewindows.md) — A Boolean value that indicates whether the current platform supports opening multiple windows.

### StoreKit configuration

- [displayStoreKitMessage](environmentvalues/displaystorekitmessage.md)
- [requestReview](environmentvalues/requestreview.md)

### Text styles

- [allowsTightening](environmentvalues/allowstightening.md) — A Boolean value that indicates whether inter-character spacing should tighten to fit the text into the available space.
- [autocorrectionDisabled](environmentvalues/autocorrectiondisabled.md) — A Boolean value that determines whether the view hierarchy has auto-correction enabled.
- [dynamicTypeSize](environmentvalues/dynamictypesize.md) — The current Dynamic Type size.
- [font](environmentvalues/font.md) — The default font of this environment.
- [layoutDirection](environmentvalues/layoutdirection.md) — The layout direction associated with the current environment.
- [lineLimit](environmentvalues/linelimit.md) — The maximum number of lines that text can occupy in a view.
- [lineSpacing](environmentvalues/linespacing.md) — The distance in points between the bottom of one line fragment and the top of the next.
- [minimumScaleFactor](environmentvalues/minimumscalefactor.md) — The minimum permissible proportion to shrink the font size to fit the text into the available space.
- [multilineTextAlignment](environmentvalues/multilinetextalignment.md) — An environment value that indicates how a text view aligns its lines when the content wraps or contains newlines.
- [textCase](environmentvalues/textcase.md) — A stylistic override to transform the case of `Text` when displayed, using the environment’s locale.
- [textSelectionAffinity](environmentvalues/textselectionaffinity.md) — A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).
- [truncationMode](environmentvalues/truncationmode.md) — A value that indicates how the layout truncates the last line of text to fit into the available space.

### View attributes

- [allowedDynamicRange](environmentvalues/alloweddynamicrange.md) — The allowed dynamic range for the view, or nil.
- [backgroundMaterial](environmentvalues/backgroundmaterial.md) — The material underneath the current view.
- [backgroundProminence](environmentvalues/backgroundprominence.md) — The prominence of the background underneath views associated with this environment.
- [backgroundStyle](environmentvalues/backgroundstyle.md) — An optional style that overrides the default system background style when set.
- [badgeProminence](environmentvalues/badgeprominence.md) — The prominence to apply to badges associated with this environment.
- [contentTransition](environmentvalues/contenttransition.md) — The current method of animating the contents of views.
- [contentTransitionAddsDrawingGroup](environmentvalues/contenttransitionaddsdrawinggroup.md) — A Boolean value that controls whether views that render content transitions use GPU-accelerated rendering.
- [defaultMinListHeaderHeight](environmentvalues/defaultminlistheaderheight.md) — The default minimum height of a header in a list.
- [defaultMinListRowHeight](environmentvalues/defaultminlistrowheight.md) — The default minimum height of rows in a list.
- [headerProminence](environmentvalues/headerprominence.md) — The prominence to apply to section headers within a view.
- [physicalMetrics](environmentvalues/physicalmetrics.md) — The physical metrics associated with a scene.
- [realityKitScene](environmentvalues/realitykitscene.md)
- [realityViewCameraControls](environmentvalues/realityviewcameracontrols.md) — The camera controls for the reality view.
- [redactionReasons](environmentvalues/redactionreasons.md) — The current redaction reasons applied to the view hierarchy.
- [springLoadingBehavior](environmentvalues/springloadingbehavior.md) — The behavior of spring loaded interactions for the views associated with this environment.
- [symbolRenderingMode](environmentvalues/symbolrenderingmode.md) — The current symbol rendering mode, or `nil` denoting that the mode is picked automatically using the current image and foreground style as parameters.
- [symbolVariants](environmentvalues/symbolvariants.md) — The symbol variant to use in this environment.
- [worldTrackingLimitations](environmentvalues/worldtrackinglimitations.md) — The current limitations of the device tracking the user’s surroundings.

### Widgets

- [showsWidgetContainerBackground](environmentvalues/showswidgetcontainerbackground.md) — An environment variable that indicates whether the background of a widget appears.
- [showsWidgetLabel](environmentvalues/showswidgetlabel.md) — A Boolean value that indicates whether an accessory family widget can display an accessory label.
- [widgetFamily](environmentvalues/widgetfamily.md) — The template of the widget — small, medium, or large.
- [widgetRenderingMode](environmentvalues/widgetrenderingmode.md) — The widget’s rendering mode, based on where the system is displaying it.
- [widgetContentMargins](environmentvalues/widgetcontentmargins.md) — A property that identifies the content margins of a widget.

### Deprecated environment values

- [disableAutocorrection](environmentvalues/disableautocorrection.md) — A Boolean value that determines whether the view hierarchy has auto-correction enabled. _(deprecated)_
- [sizeCategory](environmentvalues/sizecategory.md) — The size of content. _(deprecated)_
- [presentationMode](environmentvalues/presentationmode.md) — A binding to the current presentation mode of the view associated with this environment. _(deprecated)_
- [PresentationMode](presentationmode.md) — An indication whether a view is currently presented by another view. _(deprecated)_
- [complicationRenderingMode](environmentvalues/complicationrenderingmode.md) — The complication rendering mode for the current environment. _(deprecated)_
- [controlActiveState](environmentvalues/controlactivestate.md) — The active appearance expected of controls in a window. _(deprecated)_

### Instance Properties

- [accessibilityReduceHighlightingEffects](environmentvalues/accessibilityreducehighlightingeffects.md) — Whether the system preference for Reduce Bright Effects is enabled.
- [accessibilityShowBorders](environmentvalues/accessibilityshowborders.md) — Whether the system preference for Show Borders is enabled.
- [activityFamily](environmentvalues/activityfamily.md) — The size family of the current Live Activity.
- [askPermission](environmentvalues/askpermission.md) — An action that sends a permission question to a parent or guardian.
- [buttonSizing](environmentvalues/buttonsizing.md) — The preferred sizing behavior of buttons in the view hierarchy.
- [credentialDataManager](environmentvalues/credentialdatamanager.md) — This environment variable is for SwiftUI clients of the ASCredentialDataManager API. An example usage might look like:
- [credentialExportManager](environmentvalues/credentialexportmanager.md) — This environment variable is for SwiftUI clients of the credential exchange API. An example usage might look like:
- [credentialImportManager](environmentvalues/credentialimportmanager.md) — This environment variable is for SwiftUI clients of the credential exchange API. An example usage might look like:
- [deliveredVerificationCodesManager](environmentvalues/deliveredverificationcodesmanager.md) — This environment variable is for SwiftUI clients of the ASDeliveredVerificationCodesManager API. An example usage might look like: _(beta)_
- [devicePickerSupports](environmentvalues/devicepickersupports.md) — Checks for support to present a DevicePicker.
- [findContext](environmentvalues/findcontext.md)
- [fontResolutionContext](environmentvalues/fontresolutioncontext.md) — Information used to resolve a font.
- [imagePlaygroundAllowedGenerationStyles](environmentvalues/imageplaygroundallowedgenerationstyles.md)
- [imagePlaygroundOptions](environmentvalues/imageplaygroundoptions.md)
- [imagePlaygroundPersonalizationPolicy](environmentvalues/imageplaygroundpersonalizationpolicy.md) _(deprecated)_
- [imagePlaygroundSelectedGenerationStyle](environmentvalues/imageplaygroundselectedgenerationstyle.md)
- [isActivityUpdateReduced](environmentvalues/isactivityupdatereduced.md) — A Boolean value that indicates whether the Live Activity update synchronization rate is reduced.
- [isDynamicIslandLimitedInWidth](environmentvalues/isdynamicislandlimitedinwidth.md) — A Boolean value that indicates whether the Dynamic Island view displays with a limited width. _(beta)_
- [isTabViewSidebarAvailable](environmentvalues/istabviewsidebaravailable.md) — A Boolean value that indicates whether a tab sidebar is available within the content of a surrounding [TabView](tabview.md). _(beta)_
- [isUserAuthenticationEnabled](environmentvalues/isuserauthenticationenabled.md) — The current system user authentication enablement status.
- [labelIconToTitleSpacing](environmentvalues/labelicontotitlespacing.md) — The spacing between the icon and title of a label.
- [labelReservedIconWidth](environmentvalues/labelreservediconwidth.md) — The width reserved for icons in labels.
- [levelOfDetail](environmentvalues/levelofdetail.md) — The level of detail the view is recommended to have.
- [lineHeight](environmentvalues/lineheight.md) — The default line height for text influenced by this environment.
- [navigationLinkIndicatorVisibility](environmentvalues/navigationlinkindicatorvisibility.md) — A value that says whether a built-in navigation link would show a disclosure indicator in the current context.
- [remoteDeviceIdentifier](environmentvalues/remotedeviceidentifier.md) — An opaque object that identifies the device on which the scene (from which this value is accessed from) is being presented on.
- [requestAgeRange](environmentvalues/requestagerange.md) — An action that presents a system interface to request a person’s age range.
- [requestAppDeletion](environmentvalues/requestappdeletion.md)
- [showSignificantUpdateAcknowledgment](environmentvalues/showsignificantupdateacknowledgment.md) — Presents a system interface to inform people about significant app changes and request their acknowledgment.
- [supportedActivityFamilies](environmentvalues/supportedactivityfamilies.md) — An environment value that that indicates potential rendered family for a Live Activity.
- [supportsImagePlayground](environmentvalues/supportsimageplayground.md) — A Boolean value that indicates whether image generation is available on the current device.
- [supportsRemoteScenes](environmentvalues/supportsremotescenes.md) — Indicates if the current device supports presenting a [RemoteImmersiveSpace](remoteimmersivespace.md) on a remote device.
- [surfaceSnappingInfo](environmentvalues/surfacesnappinginfo.md) — Provides information about the current snap state of the scene.
- [symbolColorRenderingMode](environmentvalues/symbolcolorrenderingmode.md) — The property specifying how symbol images fill their layers, or nil to use the default fill style.
- [symbolVariableValueMode](environmentvalues/symbolvariablevaluemode.md) — The current symbol variable value mode, or `nil` denoting that the mode is picked automatically.
- [systemPrefersReducedResourceUsage](environmentvalues/systemprefersreducedresourceusage.md) — A boolean value indicating whether the system would prefer the app to reduce its overall resource usage. _(beta)_
- [tabBarPlacement](environmentvalues/tabbarplacement.md) — The current placement of the tab bar.
- [tabViewBottomAccessoryPlacement](environmentvalues/tabviewbottomaccessoryplacement.md) — The current placement of the tab view bottom accessory.
- [windowClippingMargins](environmentvalues/windowclippingmargins.md)
- [writingToolsBehavior](environmentvalues/writingtoolsbehavior.md) — The current Writing Tools behavior for text and text input.

## See Also

### Accessing environment values

- [Environment](environment.md) — A property wrapper that reads a value from a view’s environment.
