---
title: SwiftUI updates
framework: Updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/updates/swiftui
source_url: 'https://developer.apple.com/documentation/updates/swiftui'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/updates/swiftui.json'
content_hash: 'sha256:16c41f56b840833e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Updates](../updates.md)

# SwiftUI updates

<sub>Article</sub>

Learn about important changes to SwiftUI.

## Overview

Browse notable changes in [SwiftUI](../swiftui.md).

## June 2026

### General

- Build your project in Xcode 27 or later so that the `@State` attribute uses the [State()](<../swiftui/state().md>) macro to create a state value in an [App](../swiftui/app.md), [Scene](../swiftui/scene.md), or [View](../swiftui/view.md). This change only initializes and stores your property once when it’s a class.
- Build your project in Xcode 27 or later to construct type-agnostic content from closures that you mark with [ContentBuilder](../swiftui/contentbuilder.md), which serves as the unified replacement for type-specific builders like [ToolbarContentBuilder](../swiftui/toolbarcontentbuilder.md) and [CommandsBuilder](../swiftui/commandsbuilder.md).
- Add reordering by drag-and-drop in containers such as lists, stacks, grids, or custom layouts with [reorderable()](<../swiftui/dynamicviewcontent/reorderable().md>) and [reorderContainer(for:isEnabled:move:)](<../swiftui/view/reordercontainer(for_isenabled_move_).md>).
- Add custom swipe actions to views in containers such as scroll views, stacks, grids, or custom layouts using [swipeActions(edge:allowsFullSwipe:content:onPresentationChanged:)](<../swiftui/view/swipeactions(edge_allowsfullswipe_content_onpresentationchanged_).md>) and [swipeActionsContainer()](<../swiftui/view/swipeactionscontainer().md>).

### Transitions

- Specify the  [crossFade](../swiftui/navigationtransition/crossfade.md) transition to have a sheet appear by fading in over content.

### Images

- Cache images locally that you download with [AsyncImage](../swiftui/asyncimage.md), using [asyncImageURLSession(_:)](<../swiftui/view/asyncimageurlsession(__).md>), [init(request:scale:)](<../swiftui/asyncimage/init(request_scale_).md>), [init(request:scale:content:placeholder:)](<../swiftui/asyncimage/init(request_scale_content_placeholder_).md>), and [init(request:scale:transaction:content:)](<../swiftui/asyncimage/init(request_scale_transaction_content_).md>).

### Toolbars

- Use the [visibilityPriority(_:)](<../swiftui/toolbarcontent/visibilitypriority(__).md>) modifier to prioritize important toolbar actions so SwiftUI keeps them visible as space shrinks, moving lower-priority items to the overflow menu first.
- Send secondary toolbar actions, like archive or delete, directly to the overflow menu by wrapping them in a [ToolbarOverflowMenu](../swiftui/toolbaroverflowmenu.md), keeping your primary toolbar focused on key actions.
- Anchor a toolbar item to the trailing edge of the top bar using the [topBarPinnedTrailing](../swiftui/toolbaritemplacement/topbarpinnedtrailing.md) placement so it stays in place even as other items shift or move to the overflow menu.
- Control how toolbars minimize in response to scrolling using the doc://com.apple.documentation/documentation/swiftui/view/toolbarminimizebehavior(_:for:) modifier.

### Documents

- Build document-based apps that read directly from a file URL by conforming your document class to [ReadableDocument](../swiftui/readabledocument.md), enabling access to large files and integration with URL-based frameworks.
- Add write support to a URL-based document by also conforming to [WritableDocument](../swiftui/writabledocument.md).
- Implement custom reading and writing logic with [DocumentReader](../swiftui/documentreader.md) and [DocumentWriter](../swiftui/documentwriter.md), or use [FileWrapperDocumentReader](../swiftui/filewrapperdocumentreader.md) and [FileWrapperDocumentWriter](../swiftui/filewrapperdocumentwriter.md) for simpler file-wrapper-based cases.
- Access the document’s file URL and last modification date, and coordinate additional file access, using [URLDocumentConfiguration](../swiftui/urldocumentconfiguration.md).
- Export a [WritableDocument](../swiftui/writabledocument.md) to disk using the [fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:onCancellation:)](<../swiftui/view/fileexporter(ispresented_document_contenttype_defaultfilename_oncompletion_oncancellation_).md>) modifier.

### Tab bars

- Set the [prominent](../swiftui/tabrole/prominent.md) role on a tab to place the tab in a separate, trailing position of the tab bar.

### Alerts and confirmation dialogs

- Present an alert or confirmation dialog from an optional data item or error object, and use that data to produce the content and title:

    - [alert(_:item:actions:)](<../swiftui/view/alert(__item_actions_).md>)
    - [alert(error:actions:)](<../swiftui/view/alert(error_actions_).md>)
    - [alert(_:item:actions:message:)](<../swiftui/view/alert(__item_actions_message_).md>)
    - [alert(error:actions:message:)](<../swiftui/view/alert(error_actions_message_).md>)
    - [confirmationDialog(_:item:titleVisibility:actions:)](<../swiftui/view/confirmationdialog(__item_titlevisibility_actions_).md>)
    - [confirmationDialog(_:item:titleVisibility:actions:message:)](<../swiftui/view/confirmationdialog(__item_titlevisibility_actions_message_).md>)

### Gestures

- Specify the sources of gesture input to recognize, such as direct or indirect touches, pencil, or pointer. The following gestures have initializers that you can use to specify the sources of gesture input: [DragGesture](../swiftui/draggesture.md), [LongPressGesture](../swiftui/longpressgesture.md), [MagnifyGesture](../swiftui/magnifygesture.md), [RotateGesture](../swiftui/rotategesture.md), [RotateGesture3D](../swiftui/rotategesture3d.md), [SpatialEventGesture](../swiftui/spatialeventgesture.md), [SpatialTapGesture](../swiftui/spatialtapgesture.md), [TapGesture](../swiftui/tapgesture.md), [WindowDragGesture](../swiftui/windowdraggesture.md). For more information see [GestureInputKinds](../swiftui/gestureinputkinds.md).

## June 2025

### General

- Apply Liquid Glass effects to views using [glassEffect(_:in:)](<../swiftui/view/glasseffect(__in_).md>).
- Use [glass](../swiftui/primitivebuttonstyle/glass.md) with the [buttonStyle(_:)](<../swiftui/view/buttonstyle(__)-66fbx.md>) modifier to apply Liquid Glass to instances of `Button`.
- [ToolbarSpacer](../swiftui/toolbarspacer.md) creates a visual break between items in toolbars containing Liquid Glass.
- Use [scrollEdgeEffectStyle(_:for:)](<../swiftui/view/scrolledgeeffectstyle(__for_).md>) to configure the scroll edge effect style for scroll views.
- [backgroundExtensionEffect()](<../swiftui/view/backgroundextensioneffect().md>) duplicates, mirrors, and blurs views placed around edges with available safe areas.
- Set behavior for tab bar minimization with [tabBarMinimizeBehavior(_:)](<../swiftui/view/tabbarminimizebehavior(__).md>).
- Set the [search](../swiftui/tabrole/search.md) role on a tab to take someone to a search tab and have a search field take the place of the tab bar.
- Adjust the content of accessory views based on the placement in a tab view with [TabViewBottomAccessoryPlacement](../swiftui/tabviewbottomaccessoryplacement.md).
- Connect a [WebView](../webkit/webview-swift.struct.md) with a [WebPage](../webkit/webpage.md) to fully control the browsing experience in your app.
- Drag multiple items using the [draggable(containerItemID:containerNamespace:)](<../swiftui/view/draggable(containeritemid_containernamespace_).md>) modifier. Make a view a container for draggable views using the [dragContainer(for:itemID:in:_:)](<../swiftui/view/dragcontainer(for_itemid_in___).md>) modifier.
- Use the [Animatable()](<../swiftui/animatable().md>) macro to have SwiftUI synthesize custom animatable data properties.
- [Slider](../swiftui/slider.md) now supports tick marks. Tick marks appear automatically when initializing a `Slider` with the `step` parameter.
- Use [windowResizeAnchor(_:)](<../swiftui/view/windowresizeanchor(__).md>) to set the window anchor point when a window must resize.

### Text

- [TextEditor](../swiftui/texteditor.md) now supports [AttributedString](../foundation/attributedstring.md).
- Handle text selection with attributed text using [AttributedTextSelection](../swiftui/attributedtextselection.md).
- [AttributedTextFormattingDefinition](../swiftui/attributedtextformattingdefinition.md) defines how text can be styled in specific contexts.
- Use [FindContext](../swiftui/findcontext.md) to create a find navigator in views that support text editing.

### Accessibility

- Support Assistive Access in iOS and iPadOS scenes with [AssistiveAccess](../swiftui/assistiveaccess.md).

### HDR

- [Color.ResolvedHDR](../swiftui/color/resolvedhdr.md) is a set of RGBA values that represent a color that can be shown, including HDR headroom information.

### UIKit and AppKit integration

- Host and present SwiftUI scenes in UIKit with [UIHostingSceneDelegate](../swiftui/uihostingscenedelegate.md) and in AppKit with [NSHostingSceneRepresentation](../swiftui/nshostingscenerepresentation.md).
- Incorporate gesture recognizers in SwiftUI views from AppKit with [NSGestureRecognizerRepresentable](../swiftui/nsgesturerecognizerrepresentable.md).

### Immersive spaces

- Manipulate views using common hand gestures with [manipulable(coordinateSpace:operations:inertia:isEnabled:onChanged:)](<../swiftui/view/manipulable(coordinatespace_operations_inertia_isenabled_onchanged_).md>).
- Snap volumes to horizontal surfaces and windows to vertical surfaces using [SurfaceSnappingInfo](../swiftui/surfacesnappinginfo.md).
- Use [RemoteImmersiveSpace](../swiftui/remoteimmersivespace.md) to render stereo content from your Mac app on Apple Vision Pro.
- Use [SpatialContainer](../swiftui/spatialcontainer.md) to create a layout container that aligns overlapping content in 3D space.
- Depth-based variants of modifiers allow easier volumetric layouts in SwiftUI. For example, [aspectRatio3D(_:contentMode:)](<../swiftui/view/aspectratio3d(__contentmode_).md>), [rotation3DLayout(_:)](<../swiftui/view/rotation3dlayout(__).md>), and [depthAlignment(_:)](<../swiftui/layout/depthalignment(__).md>).

## June 2024

### Volumes

- Specify the alignment of a volume when moved in the world using the [volumeWorldAlignment(_:)](<../swiftui/scene/volumeworldalignment(__).md>) scene modifier.
- Specify the default world scaling behavior of your scene using the [defaultWorldScaling(_:)](<../swiftui/scene/defaultworldscaling(__).md>) scene modifier.
- Adjust the visibilty of a volume’s baseplate using the [volumeBaseplateVisibility(_:)](<../swiftui/view/volumebaseplatevisibility(__).md>) view modifier.
- Define a custom action to execute when the viewpoint of a volume changes using the [onVolumeViewpointChange(updateStrategy:initial:_:)](<../swiftui/view/onvolumeviewpointchange(updatestrategy_initial___).md>) view modifier.

### Windows

- Change the default initial size and position of a window using the [defaultWindowPlacement(_:)](<../swiftui/scene/defaultwindowplacement(__).md>) modifier.
- Change the default behavior for how windows behave when performing a zoom using [WindowIdealSize](../swiftui/windowidealsize.md) and provide the placement for the zoomed window with the [windowIdealPlacement(_:)](<../swiftui/scene/windowidealplacement(__).md>) modifier.
- Create utility windows in SwiftUI using the new [UtilityWindow](../swiftui/utilitywindow.md) scene type and toggle the window’s visibility using the [WindowVisibilityToggle](../swiftui/windowvisibilitytoggle.md).
- Customize the style of a window using the new [window](../swiftui/containerbackgroundplacement/window.md) container background placement, the [toolbar(removing:)](<../swiftui/view/toolbar(removing_).md>) view modifier, and the [plain](../swiftui/windowstyle/plain.md) window style.
- Set the default launch behavior for a scene using the [defaultLaunchBehavior(_:)](<../swiftui/scene/defaultlaunchbehavior(__).md>) modifier.
- Replace one scene with another using the [pushWindow](../swiftui/environmentvalues/pushwindow.md) method.

### Immersive spaces

- Add an action to perform when the state of the immersion changes using the [onImmersionChange(_:)](<../swiftui/view/onimmersionchange(__).md>) modifier.
- Apply a custom color or dim a passthrough video in an immersive space using the [colorMultiply(_:)](<../swiftui/surroundingseffect/colormultiply(__).md>) and [dim(intensity:)](<../swiftui/surroundingseffect/dim(intensity_).md>) initializers.

### Documents

- Customize the launch experience of document-based applications using [DocumentGroupLaunchScene](../swiftui/documentgrouplaunchscene.md) and [NewDocumentButton](../swiftui/newdocumentbutton.md).

### Navigation

- Specify the appearance and interaction of [TabView](../swiftui/tabview.md) with the [tabViewStyle(_:)](<../swiftui/view/tabviewstyle(__).md>)  modifier using values like [sidebarAdaptable](../swiftui/tabviewstyle/sidebaradaptable.md), [tabBarOnly](../swiftui/tabviewstyle/tabbaronly.md), and [grouped](../swiftui/tabviewstyle/grouped.md).
- Build hierarchy by nesting tabs as a tab item within [TabSection](../swiftui/tabsection.md).
- Enable people to customize a [TabView](../swiftui/tabview.md) using the [tabViewCustomization(_:)](<../swiftui/view/tabviewcustomization(__).md>) modifier and persist customization state in [AppStorage](../swiftui/appstorage.md) with [TabViewCustomization](../swiftui/tabviewcustomization.md).

### Modal presentations

- Use built-in presentation sizes for sheets like [form](../swiftui/presentationsizing/form.md) or [page](../swiftui/presentationsizing/page.md) with the [presentationSizing(_:)](<../swiftui/view/presentationsizing(__).md>) modifier or create custom sized sheets using the [PresentationSizing](../swiftui/presentationsizing.md) protocol.

### Toolbars

- Specify the display mode of toolbars in macOS using the [ToolbarLabelStyle](../swiftui/toolbarlabelstyle.md) type.
- Configure the foreground style in the toolbar environment in watchOS using the [toolbarForegroundStyle(_:for:)](<../swiftui/view/toolbarforegroundstyle(__for_).md>) view modifier.
- Anchor ornaments relative to the depth of your volume — in addition to the height and width — using the [scene(_:)](<../swiftui/ornamentattachmentanchor/scene(__)-1l8wf.md>) method that takes a [UnitPoint3D](../swiftui/unitpoint3d.md).

### Views

- Create custom container views like [Picker](../swiftui/picker.md), [List](../swiftui/list.md), and [TabView](../swiftui/tabview.md) using new [Group](../swiftui/group.md) and [ForEach](../swiftui/foreach.md) initializers, like [init(subviews:transform:)](<../swiftui/group/init(subviews_transform_).md>) and [init(subviews:content:)](<../swiftui/foreach/init(subviews_content_).md>), respectively.
- Declare a custom container value by defining a key that conforms to the [ContainerValueKey](../swiftui/containervaluekey.md) protocol, and set the container value for a view using the [containerValue(_:_:)](<../swiftui/view/containervalue(____).md>) modifier.
- Create [EnvironmentValues](../swiftui/environmentvalues.md), [Transaction](../swiftui/transaction.md), [ContainerValues](../swiftui/containervalues.md), and [FocusedValues](../swiftui/focusedvalues.md) entries by using the [Entry()](<../swiftui/entry().md>) macro to the variable declaration.

### Animation

- Customize the transition when pushing a view onto a navigation stack or presenting a view with the [navigationTransition(_:)](<../swiftui/view/navigationtransition(__).md>) view modifier.
- Add new symbols effects and configurations like [wiggle](../symbols/symboleffect/wiggle.md), [rotate](../symbols/symboleffect/rotate.md), and [breathe](../symbols/symboleffect/breathe.md) using the [symbolEffect(_:options:value:)](<../swiftui/view/symboleffect(__options_value_).md>) modifier.

### Text input and output

- Add text suggestions support to any text field using [textInputSuggestions(_:)](<../swiftui/view/textinputsuggestions(__).md>) and [textInputCompletion(_:)](<../swiftui/view/textinputcompletion(__).md>) view modifiers.
- Access and modify selected text using a new [TextSelection](../swiftui/textselection.md) binding for [TextField](../swiftui/textfield.md) and [TextEditor](../swiftui/texteditor.md).
- Bind to the focus state of an app’s search field using the [searchFocused(_:equals:)](<../swiftui/view/searchfocused(__equals_).md>) view modifier.

### Drawing and graphics

- Precompile shaders at build time using the [compile(as:)](<../swiftui/shader/compile(as_).md>) method.
- Create mesh gradients with a grid of points and colors using the new [MeshGradient](../swiftui/meshgradient.md) type.
- Extend SwiftUI Text views with custom rendering effects and interaction behaviors using [TextAttribute](../swiftui/textattribute.md), [Text.Layout](../swiftui/text/layout.md), and [TextRenderer](../swiftui/textrenderer.md).
- Create a new [Color](../swiftui/color.md) by mixing two colors using the [mix(with:by:in:)](<../swiftui/color/mix(with_by_in_).md>) method.

### Layout

- Enable custom spacing between views in a [ZStack](../swiftui/zstack.md) along the depth axis with the [init(alignment:spacing:content:)](<../swiftui/zstack/init(alignment_spacing_content_).md>) initializer.

### Scrolling

- Scroll to a view, offset, or edge in a scroll view using the [scrollPosition(_:anchor:)](<../swiftui/view/scrollposition(__anchor_).md>) view modifier and specifying one of the [ScrollPosition](../swiftui/scrollposition.md) values.
- Limit the number of views that can be scrolled by a single interaction using the limit behavior value [alwaysByFew](../swiftui/viewalignedscrolltargetbehavior/limitbehavior/alwaysbyfew.md) or [alwaysByOne](../swiftui/viewalignedscrolltargetbehavior/limitbehavior/alwaysbyone.md).
- Add an action to be called when a view crosses a provided threshold using the [onScrollVisibilityChange(threshold:_:)](<../swiftui/view/onscrollvisibilitychange(threshold___).md>) modifier.
- Access both the old and new values when a scroll view’s phase changes by using the [onScrollPhaseChange(_:)](<../swiftui/view/onscrollphasechange(__)-7mica.md>) modifier.

### Gestures

- Conditionally disable a gesture using the `isEnabled` parameter in a modifier like [gesture(_:isEnabled:)](<../swiftui/view/gesture(__isenabled_).md>).
- Create extra drag areas of a window in macOS when you add a [WindowDragGesture](../swiftui/windowdraggesture.md) gesture.
- Create a hand gesture shortcut for Double Tap in watchOS using the [HandGestureShortcut](../swiftui/handgestureshortcut.md) structure.
- Enable whether gestures can handle events that activate the containing window using the [allowsWindowActivationEvents(_:)](<../swiftui/view/allowswindowactivationevents(__).md>) view modifier.

### Input events

- Create a group of hover effects that activate together using [HoverEffectGroup](../swiftui/hovereffectgroup.md) and apply them to a view using the [hoverEffect(in:isEnabled:body:)](<../swiftui/view/hovereffect(in_isenabled_body_).md>) view modifier.
- Customize the appearance of the system pointer in macOS, iPadOS, and visionOS with new pointer styles using [pointerStyle(_:)](<../swiftui/view/pointerstyle(__).md>) or the visibility with the [pointerVisibility(_:)](<../swiftui/view/pointervisibility(__).md>) modifier.
- Access keyboard modifier flags using the [onModifierKeysChanged(mask:initial:_:)](<../swiftui/view/onmodifierkeyschanged(mask_initial___).md>).
- Replace the primary view with one or more alternative views when pressing a specified set of modifier keys using the [modifierKeyAlternate(_:_:)](<../swiftui/view/modifierkeyalternate(____).md>) view modifier.
- Enable the hand pointer for custom drawing and markup applications using the [handPointerBehavior(_:)](<../swiftui/view/handpointerbehavior(__).md>) modifier.

### Previews in Xcode

- Write dynamic properties inline in previews using the new [Previewable()](<../swiftui/previewable().md>) macro.
- Inject shared environment objects, model containers, or other dependencies into previews using the [PreviewModifier](../swiftui/previewmodifier.md) protocol.

### Accessibility

- Specify that your accessibility element behaves as a tab bar using the [isTabBar](../swiftui/accessibilitytraits/istabbar.md) accessibility trait with the [accessibilityAddTraits(_:)](<../swiftui/view/accessibilityaddtraits(__).md>) modifier. In UIKit, use [tabBar](../uikit/uiaccessibilitytraits/tabbar.md).
- Generate a localized description of a color in a string interpolation by adding `accessibilityName:`, such as `"\(accessibilityName: myColor)"`. Pass that string to any accessibility modifier.

### Framework interoperability

- Reuse existing UIKit gesture recognizer code in SwiftUI. In SwiftUI, create UIKit gesture recognizers using [UIGestureRecognizerRepresentable](../swiftui/uigesturerecognizerrepresentable.md). In UIKit, refer to SwiftUI gestures by name using [name](../uikit/uigesturerecognizer/name.md).
- Share menu content definitions between SwiftUI and AppKit by using the [NSHostingMenu](../swiftui/nshostingmenu.md) in your AppKit view hierarchy.

## June 2023, visionOS

### Scenes

- Create a volume that can display 3D models by applying the [volumetric](../swiftui/windowstyle/volumetric.md) window style to an app’s window.
- Make use of a Full Space by opening an [ImmersiveSpace](../swiftui/immersivespace.md) scene. You can use the [mixed](../swiftui/immersionstyle/mixed.md) immersion style to place objects in a person’s surroundings, or the [full](../swiftui/immersionstyle/full.md) style to completely control the visual experience.
- Display 3D models in a volume or a Full Space using RealityKit entities that you load with that framework’s [Model3D](../realitykit/model3d.md) or [RealityView](../realitykit/realityview.md) structure.

### Toolbars and ornaments

- Display a toolbar item in an ornament using the [bottomOrnament](../swiftui/toolbaritemplacement/bottomornament.md) toolbar item placement.
- Add an ornament to a window directly using the [ornament(visibility:attachmentAnchor:contentAlignment:ornament:)](<../swiftui/view/ornament(visibility_attachmentanchor_contentalignment_ornament_).md>) view modifier.

### Drawing and graphics

- Detect view geometry in three dimensions using a [GeometryReader3D](../swiftui/geometryreader3d.md).
- Add a 3D visual effect using the [visualEffect3D(_:)](<../swiftui/view/visualeffect3d(__).md>) view modifier.
- Rotate or scale in three dimensions with view modifiers like [rotation3DEffect(_:anchor:)](<../swiftui/view/rotation3deffect(__anchor_).md>) and [scaleEffect(x:y:z:anchor:)](<../swiftui/view/scaleeffect(x_y_z_anchor_).md>), respectively.
- Convert between display points and physical distances using a [PhysicalMetricsConverter](../swiftui/physicalmetricsconverter.md).

### View configuration

- Add a glass background effect to a view using the [glassBackgroundEffect(displayMode:)](<../swiftui/view/glassbackgroundeffect(displaymode_).md>) view modifier.
- Dim passthrough when appropriate by applying a [preferredSurroundingsEffect(_:)](<../swiftui/view/preferredsurroundingseffect(__).md>) modifier.

### View layout

- Make 3D adjustments to layout with view modifiers like [offset(z:)](<../swiftui/view/offset(z_).md>), [padding3D(_:)](<../swiftui/view/padding3d(__)-6bex4.md>), and [frame(depth:alignment:)](<../swiftui/view/frame(depth_alignment_).md>).

### Gestures

- Enable people to rotate objects in three dimensions when you add a [RotateGesture3D](../swiftui/rotategesture3d.md) gesture.

## June 2023

### Scenes

- Close windows by their identifier using the [dismissWindow](../swiftui/environmentvalues/dismisswindow.md) action stored in the environment.
- Enable people to open a settings window by presenting a [SettingsLink](../swiftui/settingslink.md) button.

### Navigation

- Control views of a navigation split view or stack using a new overload of the [navigationDestination(item:destination:)](<../swiftui/view/navigationdestination(item_destination_).md>) view modifier.
- Manage column visibility of a navigation split view using new overloads of the view’s initializer, like [init(columnVisibility:preferredCompactColumn:sidebar:content:detail:)](<../swiftui/navigationsplitview/init(columnvisibility_preferredcompactcolumn_sidebar_content_detail_).md>).

### Modal presentations

- Use new overloads of the file export, import, and move modifiers, like [fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)](<../swiftui/view/fileexporter(ispresented_document_contenttypes_defaultfilename_oncompletion_oncancellation_)-34bd6.md>), to access new file management features. For example, you can:

    - Configure a file import or export dialog to open on a default directory, enable only certain file types, display hidden files, and so on.
    - Retain file interface configuration that a person chooses from one presentation to the next.
    - Export types that conform to the [Transferable](../coretransferable/transferable.md) protocol.
- Specify a dialog severity using the [dialogSeverity(_:)](<../swiftui/view/dialogseverity(__).md>) view modifier.
- Provide a custom icon for a dialog using the [dialogIcon(_:)](<../swiftui/view/dialogicon(__).md>) modifier.
- Enable people to suppress dialogs using one of the dialog suppression modifiers, like [dialogSuppressionToggle(isSuppressed:)](<../swiftui/view/dialogsuppressiontoggle(issuppressed_).md>).

### Toolbars

- Configure the toolbar title display size using the [toolbarTitleDisplayMode(_:)](<../swiftui/view/toolbartitledisplaymode(__).md>) modifier.

### Search

- Present search programmatically using a binding to a new `isPresented` parameter available in some searchable view modifiers, like [searchable(text:isPresented:placement:prompt:)](<../swiftui/view/searchable(text_ispresented_placement_prompt_)-1hn4y.md>).
- Create mutable search tokens by providing a binding to the input of the `token` closure in the applicable searchable view modifiers, like [searchable(text:editableTokens:isPresented:placement:prompt:token:)](<../swiftui/view/searchable(text_editabletokens_ispresented_placement_prompt_token_)-2ilmg.md>).

### Data and storage

- Bridge between SwiftUI environment keys and UIKit traits more easily using the [UITraitBridgedEnvironmentKey](../swiftui/uitraitbridgedenvironmentkey.md) protocol.
- Get better performance when you share data throughout your app by using the new [Observable()](<../observation/observable().md>) macro.
- Access both the old and new values of a value that changes when processing the completion closure of the [onChange(of:initial:_:)](<../swiftui/view/onchange(of_initial___)-4psgg.md>) view modifier.

### Views

- Display a standard interface when a resource, like search results or a network connection, isn’t available using the [ContentUnavailableView](../swiftui/contentunavailableview.md) view type.
- Display a standard inspector interface with a platform-appropriate appearance by applying the [inspector(isPresented:content:)](<../swiftui/view/inspector(ispresented_content_).md>) modifier.

### Animation

- Perform an action when an animation completes by specifying a completion closure to the [withAnimation(_:completionCriteria:_:completion:)](<../swiftui/withanimation(__completioncriteria___completion_).md>) view modifier.
- Define custom animation behaviors by creating a type that conforms to the [CustomAnimation](../swiftui/customanimation.md) protocol.
- Perform animations that progress through predefined phases using the [PhaseAnimator](../swiftui/phaseanimator.md) structure, or according to a set of time-based keyframes by using the [Keyframes](../swiftui/keyframes.md) protocol.
- Specify information about a change in state — for example, to request a particular animation — using custom [TransactionKey](../swiftui/transactionkey.md) instances.
- Design custom animation curves using [UnitCurve](../swiftui/unitcurve.md).
- Apply streamlined spring parameters, now standardized across all Apple frameworks, using the new [spring(duration:bounce:blendDuration:)](<../swiftui/animation/spring(duration_bounce_blendduration_).md>) animation. You can also use the [Spring](../swiftui/spring.md) structure as a convenience to represent a spring’s motion.

### Text input and output

- Indicate the language that appears in a specific [Text](../swiftui/text.md) view so that SwiftUI can help to avoid clipping and collision of text, and perform proper line breaking and hyphenation using the [typesettingLanguage(_:isEnabled:)](<../swiftui/view/typesettinglanguage(__isenabled_)-4ldzm.md>) view modifier.
- Scale text semantically, for example by labeling it as having a secondary text scale, using the [textScale(_:isEnabled:)](<../swiftui/view/textscale(__isenabled_).md>) modifier.

### Shapes

- Apply more than one [fill(_:style:)](<../swiftui/shape/fill(__style_)-3y2ud.md>) or [stroke(_:style:antialiased:)](<../swiftui/shape/stroke(__style_antialiased_).md>) modifier to a single [Shape](../swiftui/shape.md).
- Apply Boolean operations to both shapes and paths, like [intersection(_:eoFill:)](<../swiftui/shape/intersection(__eofill_).md>) and [union(_:eoFill:)](<../swiftui/shape/union(__eofill_).md>).
- Use predefined shape styles, like [rect](../swiftui/shape/rect.md), to simplify your code.
- Create rounded rectangles with uneven corners using [rect(topLeadingRadius:bottomLeadingRadius:bottomTrailingRadius:topTrailingRadius:style:)](<../swiftui/shape/rect(topleadingradius_bottomleadingradius_bottomtrailingradius_toptrailingradius_style_).md>).

### Drawing and graphics

- Create fully customizable, high-performance graphics by drawing with Metal shaders inside a SwiftUI app using a [Shader](../swiftui/shader.md) structure.
- Configure an image with a specific dynamic range by applying the [allowedDynamicRange(_:)](<../swiftui/view/alloweddynamicrange(__).md>) view modifier.
- Compose effects that you apply to a view based on some aspect of the geometry of the view using the [visualEffect(_:)](<../swiftui/view/visualeffect(__).md>) modifier. For example, you can apply a blur that varies depending on the view’s position in the display.

### Layout

- Define custom coordinate spaces using the [CoordinateSpaceProtocol](../swiftui/coordinatespaceprotocol.md) with new [GeometryProxy](../swiftui/geometryproxy.md) methods, like [bounds(of:)](<../swiftui/geometryproxy/bounds(of_).md>) and [frame(in:)](<../swiftui/geometryproxy/frame(in_)-68tks.md>), to get the dimensions of containers.
- Create a frame for a view that lays out its content based on characteristics of the container view using [containerRelativeFrame(_:alignment:)](<../swiftui/view/containerrelativeframe(__alignment_).md>).
- Set the background of a container view using the [containerBackground(_:for:)](<../swiftui/view/containerbackground(__for_).md>) view modifier.

### Lists and tables

- Disable selectability of an item in a [List](../swiftui/list.md) or [Table](../swiftui/table.md) by applying the [selectionDisabled(_:)](<../swiftui/view/selectiondisabled(__).md>) modifier.
- Collapse or expand a [Section](../swiftui/section.md) of a list or table using the `isExpanded` binding in the section’s initializer.
- Configure row or section spacing using the [listRowSpacing(_:)](<../swiftui/view/listrowspacing(__).md>) and [listSectionSpacing(_:)](<../swiftui/view/listsectionspacing(__)-5t518.md>) modifiers, respectively.
- Set the prominence of a badge using the [badgeProminence(_:)](<../swiftui/view/badgeprominence(__).md>) view modifier.
- Configure alternating row backgrounds using the [alternatingRowBackgrounds(_:)](<../swiftui/view/alternatingrowbackgrounds(__).md>) modifier.
- Customize table column visibility and reordering using the [TableColumnCustomization](../swiftui/tablecolumncustomization.md) structure.
- Add hierarchical rows to a table using the [DisclosureTableRow](../swiftui/disclosuretablerow.md) structure, or recursively hierarchical rows using the [OutlineGroup](../swiftui/outlinegroup.md) structure.
- Hide table column headers using the [tableColumnHeaders(_:)](<../swiftui/view/tablecolumnheaders(__).md>) modifier.

### Scrolling

- Read the position of a scroll view using one of the scroll position modifiers, like [scrollPosition(id:anchor:)](<../swiftui/view/scrollposition(id_anchor_).md>).
- Flash scroll indicators programmatically using a view modifier, like [scrollIndicatorsFlash(onAppear:)](<../swiftui/view/scrollindicatorsflash(onappear_).md>).
- Clip scroll views in custom ways after disabling default clipping using the [scrollClipDisabled(_:)](<../swiftui/view/scrollclipdisabled(__).md>) modifier.
- Create paged scroll views, aligned to either page or view boundaries, using the [scrollTargetBehavior(_:)](<../swiftui/view/scrolltargetbehavior(__).md>) view modifier.
- Create custom scroll behaviors using the [ScrollTargetBehavior](../swiftui/scrolltargetbehavior.md) protocol.
- Control the insets of scrollable views using the [safeAreaPadding(_:)](<../swiftui/view/safeareapadding(__)-5lh9p.md>) and [contentMargins(_:_:for:)](<../swiftui/view/contentmargins(____for_)-1lt8b.md>) view modifiers.
- Add effects to views as they scroll on- and offscreen using one of the [scrollTransition(_:axis:transition:)](<../swiftui/view/scrolltransition(__axis_transition_).md>) modifiers.
- Create a [TabView](../swiftui/tabview.md) that supports vertical paging in watchOS by applying the [verticalPage](../swiftui/tabviewstyle/verticalpage.md) tab view style.

### Gestures

- Make smoother transitions between gestures and animations by using a new [velocity](../swiftui/draggesture/value/velocity.md) property on the values associated with certain gestures and a [tracksVelocity](../swiftui/transaction/tracksvelocity.md) property on [Transaction](../swiftui/transaction.md).
- Gain access to more information, including both velocity and position, by migrating to the new [MagnifyGesture](../swiftui/magnifygesture.md) and [RotateGesture](../swiftui/rotategesture.md), which replace the now deprecated `MagnificationGesture` and `RotationGesture`.

### Input events

- Enable a view that’s in focus to react directly to keyboard input by applying one of the [onKeyPress(_:action:)](<../swiftui/view/onkeypress(__action_).md>) view modifiers.
- Enable people to choose from a compact collection of items in a [Menu](../swiftui/menu.md) by styling a [Picker](../swiftui/picker.md) with the [palette](../swiftui/pickerstyle/palette.md) style.
- Provide haptic or audio feedback in response to an event using one of the sensory feedback modifiers, like [sensoryFeedback(_:trigger:)](<../swiftui/view/sensoryfeedback(__trigger_).md>).
- Create buttons and toggles that perform an [AppIntent](../appintents/appintent.md) in a widget, Live Activity, and other places using new initializers like [init(_:intent:)](<../swiftui/button/init(__intent_)-7urde.md>) and [init(_:isOn:intent:)](<../swiftui/toggle/init(__ison_intent_)-4lsrf.md>).

### Focus

- Distinguish between views for which focus serves different purposes, such as those that have a primary action like a button and those that take input like a text field, using the new [focusable(_:interactions:)](<../swiftui/view/focusable(__interactions_).md>) view modifier.
- Manage the effect that receiving focus has on a view using the [focusEffectDisabled(_:)](<../swiftui/view/focuseffectdisabled(__).md>) modifier.

### Previews in Xcode

- Reduce the amount of boilerplate that you need to create Xcode previews by using the new [Preview(_:traits:_:body:)](<../swiftui/preview(__traits___body_).md>) macro.

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
