---
title: Technology-specific modifiers
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-technology-modifiers
source_url: 'https://developer.apple.com/documentation/swiftui/view-technology-modifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-technology-modifiers.json'
content_hash: 'sha256:df84a5d5dff3dc6c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md) · [View fundamentals](view-fundamentals.md) · [View](view.md)

# Technology-specific modifiers

<sub>API Collection</sub>

Add modifiers to customize SwiftUI views that other Apple frameworks provide.

## Overview

Configure and customize SwiftUI views that you integrate from other Apple frameworks, such as web views from [WebKit](../webkit.md) or maps from [MapKit](../mapkit.md), with these modifiers.

For more information, see [Technology-specific views](technology-specific-views.md).

## Topics

### Displaying web content

- [WebView](../webkit/webview-swift.struct.md) — A view that displays some web content.
- [WebPage](../webkit/webpage.md) — An object that controls and manages the behavior of interactive web content.
- [onWebViewImmersiveEnvironmentRequest(shouldAllow:present:dismiss:)](<view/onwebviewimmersiveenvironmentrequest(shouldallow_present_dismiss_).md>) — Manages the lifecycle of immersive environments requested by websites. _(beta)_
- [webViewBackForwardNavigationGestures(_:)](<view/webviewbackforwardnavigationgestures(__).md>) — Determines whether horizontal swipe gestures trigger backward and forward page navigation.
- [webViewContentBackground(_:)](<view/webviewcontentbackground(__).md>) — Specifies the visibility of the webpage’s natural background color within this view.
- [webViewContextMenu(menu:)](<view/webviewcontextmenu(menu_).md>) — Adds an item-based context menu to a WebView, replacing the default set of context menu items.
- [webViewElementFullscreenBehavior(_:)](<view/webviewelementfullscreenbehavior(__).md>) — Determines whether a web view can display content full screen.
- [webViewLinkPreviews(_:)](<view/webviewlinkpreviews(__).md>) — Determines whether pressing a link displays a preview of the destination for the link.
- [webViewMagnificationGestures(_:)](<view/webviewmagnificationgestures(__).md>) — Determines whether magnify gestures change the view’s magnification.
- [webViewOnScrollGeometryChange(for:of:action:)](<view/webviewonscrollgeometrychange(for_of_action_).md>) — Adds an action to be performed when a value, created from a scroll geometry, changes.
- [webViewScrollInputBehavior(_:for:)](<view/webviewscrollinputbehavior(__for_).md>) — Enables or disables scrolling in web views when using particular inputs.
- [webViewScrollPosition(_:)](<view/webviewscrollposition(__).md>) — Associates a binding to a scroll position with the web view.
- [webViewTextSelection(_:)](<view/webviewtextselection(__).md>) — Determines whether to allow people to select or otherwise interact with text.

### Accessing Apple Pay and Wallet

- [PayWithApplePayButton](../passkit/paywithapplepaybutton.md) — A type that provides a button to pay with Apple pay.
- [AddPassToWalletButton](../passkit/addpasstowalletbutton.md) — A type that provides a button that enables people to add a new or existing pass to Apple Wallet.
- [VerifyIdentityWithWalletButton](../passkit/verifyidentitywithwalletbutton.md) — A type that displays a button to present the identity verification flow.
- [addOrderToWalletButtonStyle(_:)](<view/addordertowalletbuttonstyle(__).md>) — Sets the button’s style.
- [addPassToWalletButtonStyle(_:)](<view/addpasstowalletbuttonstyle(__).md>) — Sets the style to be used by the button. (see `PKAddPassButtonStyle`).
- [onApplePayCouponCodeChange(perform:)](<view/onapplepaycouponcodechange(perform_).md>) — Called when a user has entered or updated a coupon code. This is required if the user is being asked to provide a coupon code.
- [onApplePayPaymentMethodChange(perform:)](<view/onapplepaypaymentmethodchange(perform_).md>) — Called when a payment method has changed and asks for an update payment request. If this modifier isn’t provided Wallet will assume the payment method is valid.
- [onApplePayShippingContactChange(perform:)](<view/onapplepayshippingcontactchange(perform_).md>) — Called when a user selected a shipping address. This is required if the user is being asked to provide a shipping contact.
- [onApplePayShippingMethodChange(perform:)](<view/onapplepayshippingmethodchange(perform_).md>) — Called when a user selected a shipping method. This is required if the user is being asked to provide a shipping method.
- [payLaterViewAction(_:)](<view/paylaterviewaction(__).md>) — Sets the action on the PayLaterView. See `PKPayLaterAction`.
- [payLaterViewDisplayStyle(_:)](<view/paylaterviewdisplaystyle(__).md>) — Sets the display style on the PayLaterView. See `PKPayLaterDisplayStyle`.
- [payWithApplePayButtonDisableCardArt()](<view/paywithapplepaybuttondisablecardart().md>) — Sets the features that should be allowed to show on the payment buttons.
- [payWithApplePayButtonStyle(_:)](<view/paywithapplepaybuttonstyle(__).md>) — Sets the style to be used by the button. (see `PayWithApplePayButtonStyle`).
- [verifyIdentityWithWalletButtonStyle(_:)](<view/verifyidentitywithwalletbuttonstyle(__).md>) — Sets the style to be used by the button. (see `PKIdentityButtonStyle`).
- [AsyncShareablePassConfiguration](../passkit/asyncshareablepassconfiguration.md)
- [transactionTask(_:action:)](<view/transactiontask(__action_).md>) — Provides a task to perform before this view appears

### Authorizing and authenticating

- [LocalAuthenticationView](../localauthentication/localauthenticationview.md) — A SwiftUI view that displays an authentication interface.
- [SignInWithAppleButton](../authenticationservices/signinwithapplebutton.md) — A SwiftUI view that creates the Sign in with Apple button for display.
- [signInWithAppleButtonStyle(_:)](<view/signinwithapplebuttonstyle(__).md>) — Sets the style used for displaying the control (see `SignInWithAppleButton.Style`).
- [authorizationController](environmentvalues/authorizationcontroller.md) — A value provided in the SwiftUI environment that views can use to perform authorization requests.
- [webAuthenticationSession](environmentvalues/webauthenticationsession.md) — A value provided in the SwiftUI environment that views can use to authenticate a user through a web service.

### Configuring Family Sharing

- [FamilyActivityPicker](../familycontrols/familyactivitypicker.md) — A view in which users specify applications, web domains, and categories without revealing their choices to the app.
- [familyActivityPicker(isPresented:selection:)](<view/familyactivitypicker(ispresented_selection_).md>) — Presents an activity picker view as a sheet.
- [familyActivityPicker(headerText:footerText:isPresented:selection:)](<view/familyactivitypicker(headertext_footertext_ispresented_selection_).md>) — Presents an activity picker view as a sheet.
- [familyActivityPicker(title:headerText:footerText:isPresented:selection:)](<view/familyactivitypicker(title_headertext_footertext_ispresented_selection_).md>) — Present an activity picker sheet for selecting apps and websites to manage.

### Reporting on device activity

- [DeviceActivityReport](../deviceactivity/deviceactivityreport.md) — A view that reports the user’s application, category, and web domain activity in a privacy-preserving way.

### Working with managed devices

- [managedContentStyle(_:)](<view/managedcontentstyle(__).md>) — Applies a managed content style to the view.
- [automatedDeviceEnrollmentAddition(isPresented:)](<view/automateddeviceenrollmentaddition(ispresented_).md>) — Presents a modal view that enables users to add devices to their organization.

### Creating graphics

- [Chart](../charts/chart.md) — A SwiftUI view that displays a chart.
- [SceneView](../scenekit/sceneview.md) — A SwiftUI view for displaying 3D SceneKit content. _(deprecated)_
- [SpriteView](../spritekit/spriteview.md) — A SwiftUI view that renders a SpriteKit scene.

### Getting location information

- [LocationButton](../corelocationui/locationbutton.md) — A SwiftUI button that grants one-time location authorization.
- [Map](../mapkit/map.md) — A view that displays an embedded map interface.
- [mapStyle(_:)](<view/mapstyle(__).md>) — Specifies the map style to be used.
- [mapScope(_:)](<view/mapscope(__).md>) — Creates a mapScope that SwiftUI uses to connect map controls to an associated map.
- [mapFeatureSelectionDisabled(_:)](<view/mapfeatureselectiondisabled(__).md>) — Specifies which map features should have selection disabled.
- [mapFeatureSelectionAccessory(_:)](<view/mapfeatureselectionaccessory(__).md>) — Specifies the selection accessory to display for a `MapFeature`
- [mapFeatureSelectionContent(content:)](<view/mapfeatureselectioncontent(content_).md>) — Specifies a custom presentation for the currently selected feature.
- [mapControls(_:)](<view/mapcontrols(__).md>) — Configures all `Map` views in the associated environment to have standard size and position controls
- [mapControlVisibility(_:)](<view/mapcontrolvisibility(__).md>) — Configures all Map controls in the environment to have the specified visibility
- [mapCameraKeyframeAnimator(trigger:keyframes:)](<view/mapcamerakeyframeanimator(trigger_keyframes_).md>) — Uses the given keyframes to animate the camera of a `Map` when the given trigger value changes.
- [lookAroundViewer(isPresented:scene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:)](<view/lookaroundviewer(ispresented_scene_allowsnavigation_showsroadlabels_pointsofinterest_ondismiss_).md>)
- [lookAroundViewer(isPresented:initialScene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:)](<view/lookaroundviewer(ispresented_initialscene_allowsnavigation_showsroadlabels_pointsofinterest_ondismiss_).md>)
- [onMapCameraChange(frequency:_:)](<view/onmapcamerachange(frequency___).md>) — Performs an action when Map camera framing changes
- [mapItemDetailPopover(isPresented:item:displaysMap:attachmentAnchor:)](<view/mapitemdetailpopover(ispresented_item_displaysmap_attachmentanchor_).md>) — Presents a map item detail popover.
- [mapItemDetailPopover(isPresented:item:displaysMap:attachmentAnchor:arrowEdge:)](<view/mapitemdetailpopover(ispresented_item_displaysmap_attachmentanchor_arrowedge_).md>) — Presents a map item detail popover.
- [mapItemDetailPopover(item:displaysMap:attachmentAnchor:)](<view/mapitemdetailpopover(item_displaysmap_attachmentanchor_).md>) — Presents a map item detail popover.
- [mapItemDetailPopover(item:displaysMap:attachmentAnchor:arrowEdge:)](<view/mapitemdetailpopover(item_displaysmap_attachmentanchor_arrowedge_).md>) — Presents a map item detail popover.
- [mapItemDetailSheet(isPresented:item:displaysMap:)](<view/mapitemdetailsheet(ispresented_item_displaysmap_).md>) — Presents a map item detail sheet.
- [mapItemDetailSheet(item:displaysMap:)](<view/mapitemdetailsheet(item_displaysmap_).md>) — Presents a map item detail sheet.

### Displaying media

- [CameraView](../homekit/cameraview.md) — A SwiftUI view into which a video stream or an image snapshot is rendered.
- [NowPlayingView](../watchkit/nowplayingview.md) — A view that displays the system’s Now Playing interface so that the user can control audio.
- [VideoPlayer](../avkit/videoplayer.md) — A view that displays content from a player and a native user interface to control playback.
- [continuityDevicePicker(isPresented:onDidConnect:)](<view/continuitydevicepicker(ispresented_ondidconnect_).md>) — A `continuityDevicePicker` should be used to discover and connect nearby continuity device through a button interface or other form of activation. On tvOS, this presents a fullscreen continuity device picker experience when selected. The modal view covers as much the screen of `self` as possible when a given condition is true.
- [cameraAnchor(isActive:)](<view/cameraanchor(isactive_).md>) — Specifies the view that should act as the virtual camera for Apple Vision Pro 2D Persona stream.
- [foveatedStreamingPauseSheet(session:)](<view/foveatedstreamingpausesheet(session_).md>) — Tells the system to present a sheet with controls for resuming or ending the foveated streaming session when it pauses.

### Supporting Group Activities

- [groupActivityAssociation(_:)](<view/groupactivityassociation(__).md>) — Specifies how a view should be associated with the current SharePlay group activity.

### Selecting photos

- [PhotosPicker](../photosui/photospicker.md) — A view that displays a Photos picker for choosing assets from the photo library.
- [photosPicker(isPresented:selection:matching:preferredItemEncoding:)](<view/photospicker(ispresented_selection_matching_preferreditemencoding_).md>) — Presents a Photos picker that selects a `PhotosPickerItem`.
- [photosPicker(isPresented:selection:matching:preferredItemEncoding:photoLibrary:)](<view/photospicker(ispresented_selection_matching_preferreditemencoding_photolibrary_).md>) — Presents a Photos picker that selects a `PhotosPickerItem` from a given photo library.
- [photosPicker(isPresented:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:)](<view/photospicker(ispresented_selection_maxselectioncount_selectionbehavior_matching_preferreditemencoding_).md>) — Presents a Photos picker that selects a collection of `PhotosPickerItem`.
- [photosPicker(isPresented:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:photoLibrary:)](<view/photospicker(ispresented_selection_maxselectioncount_selectionbehavior_matching_preferreditemencoding_photolibrary_).md>) — Presents a Photos picker that selects a collection of `PhotosPickerItem` from a given photo library.
- [photosPickerAccessoryVisibility(_:edges:)](<view/photospickeraccessoryvisibility(__edges_).md>) — Sets the accessory visibility of the Photos picker. Accessories include anything between the content and the edge, like the navigation bar or the sidebar.
- [photosPickerDisabledCapabilities(_:)](<view/photospickerdisabledcapabilities(__).md>) — Disables capabilities of the Photos picker.
- [photosPickerSearchText(_:)](<view/photospickersearchtext(__).md>) — Sets search text of the Photos picker. _(beta)_
- [photosPickerStyle(_:)](<view/photospickerstyle(__).md>) — Sets the mode of the Photos picker.
- [photosPickerMetadataOptions(_:)](<view/photospickermetadataoptions(__).md>) — Sets metadata options for the Photos picker. _(beta)_
- [photosSharedAlbumCreationSheet(isPresented:defaultTitle:defaultSharingPolicy:photoLibrary:onCompletion:)](<view/photossharedalbumcreationsheet(ispresented_defaulttitle_defaultsharingpolicy_photolibrary_oncompletion_).md>) — Presents a view for allowing the user to create a new shared album. _(beta)_
- [photosSharedAlbumCustomizationSheet(isPresented:albumIdentifier:photoLibrary:onCompletion:)](<view/photossharedalbumcustomizationsheet(ispresented_albumidentifier_photolibrary_oncompletion_).md>) — Presents a view for allowing the user to customize a specified shared album. _(beta)_
- [photosSharedAlbumPostingSheet(isPresented:items:defaultAlbumIdentifier:photoLibrary:completion:)](<view/photossharedalbumpostingsheet(ispresented_items_defaultalbumidentifier_photolibrary_completion_).md>) — Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album. _(beta)_

### Generating images

- [imagePlaygroundGenerationStyle(_:in:)](<view/imageplaygroundgenerationstyle(__in_).md>) — Sets the selected and allowed styles to use when displaying the image generation sheet.
- [imagePlaygroundOptions(_:)](<view/imageplaygroundoptions(__).md>) — Sets the options to use when generating an image.
- [imagePlaygroundSheet(isPresented:concept:sourceImage:onCompletion:onCancellation:)](<view/imageplaygroundsheet(ispresented_concept_sourceimage_oncompletion_oncancellation_).md>) — Presents the system sheet to create an image using the specified string and optional starting image.
- [imagePlaygroundSheet(isPresented:concept:sourceImage:onCompletion:onAdaptiveImageGlyphCreation:onCancellation:)](<view/imageplaygroundsheet(ispresented_concept_sourceimage_oncompletion_onadaptiveimageglyphcreation_oncancellation_).md>) — Presents the system sheet to create images from the specified input.
- [imagePlaygroundSheet(isPresented:concept:sourceImageURL:onCompletion:onCancellation:)](<view/imageplaygroundsheet(ispresented_concept_sourceimageurl_oncompletion_oncancellation_).md>) — Presents the system sheet to create an image using the specified string and image URL.
- [imagePlaygroundSheet(isPresented:concept:sourceImageURL:onCompletion:onAdaptiveImageGlyphCreation:onCancellation:)](<view/imageplaygroundsheet(ispresented_concept_sourceimageurl_oncompletion_onadaptiveimageglyphcreation_oncancellation_).md>) — Presents the system sheet to create an image or Genmoji using the specified string and image URL.
- [imagePlaygroundSheet(isPresented:concepts:sourceImage:onCompletion:onCancellation:)](<view/imageplaygroundsheet(ispresented_concepts_sourceimage_oncompletion_oncancellation_).md>) — Presents the system sheet to create an image using one or more concepts and an optional starting image.
- [imagePlaygroundSheet(isPresented:concepts:sourceImage:onCompletion:onAdaptiveImageGlyphCreation:onCancellation:)](<view/imageplaygroundsheet(ispresented_concepts_sourceimage_oncompletion_onadaptiveimageglyphcreation_oncancellation_).md>) — Presents the system sheet to create an image or Genmoji using one or more concepts and an optional starting image.
- [imagePlaygroundSheet(isPresented:concepts:sourceImageURL:onCompletion:onCancellation:)](<view/imageplaygroundsheet(ispresented_concepts_sourceimageurl_oncompletion_oncancellation_).md>) — Presents the system sheet to create an image using one or more concepts and an image URL.
- [imagePlaygroundSheet(isPresented:concepts:sourceImageURL:onCompletion:onAdaptiveImageGlyphCreation:onCancellation:)](<view/imageplaygroundsheet(ispresented_concepts_sourceimageurl_oncompletion_onadaptiveimageglyphcreation_oncancellation_).md>) — Presents the system sheet to create an image or Genmoji using one or more concepts and an image URL.

### Previewing content

- [quickLookPreview(_:)](<view/quicklookpreview(__).md>) — Presents a Quick Look preview of the contents of a single URL.
- [quickLookPreview(_:in:)](<view/quicklookpreview(__in_).md>) — Presents a Quick Look preview of the URLs you provide.

### Interacting with networked devices

- [DevicePicker](../devicediscoveryui/devicepicker.md) — A SwiftUI view that displays other devices on the network, and creates an encrypted connection to a copy of your app running on that device.
- [devicePickerSupports](environmentvalues/devicepickersupports.md) — Checks for support to present a DevicePicker.

### Configuring a Live Activity

- [activitySystemActionForegroundColor(_:)](<view/activitysystemactionforegroundcolor(__).md>) — The text color for the auxiliary action button that the system shows next to a Live Activity on the Lock Screen.
- [activityBackgroundTint(_:)](<view/activitybackgroundtint(__).md>) — Sets the tint color for the background of a Live Activity that appears on the Lock Screen.
- [isActivityFullscreen](environmentvalues/isactivityfullscreen.md) — A Boolean value that indicates whether the Live Activity appears in a full-screen presentation.
- [activityFamily](environmentvalues/activityfamily.md) — The size family of the current Live Activity.

### Interacting with the App Store and Apple Music

- [appStoreOverlay(isPresented:configuration:)](<view/appstoreoverlay(ispresented_configuration_).md>) — Presents a StoreKit overlay when a given condition is true.
- [manageSubscriptionsSheet(isPresented:)](<view/managesubscriptionssheet(ispresented_).md>)
- [refundRequestSheet(for:isPresented:onDismiss:)](<view/refundrequestsheet(for_ispresented_ondismiss_).md>) — Display the refund request sheet for the given transaction.
- [offerCodeRedemption(options:isPresented:onCompletion:)](<view/offercoderedemption(options_ispresented_oncompletion_).md>) — Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect. _(beta)_
- [musicPicker(isPresented:title:selection:)](<view/musicpicker(ispresented_title_selection_).md>) — Presents a music picker to select items from the Apple Music catalog and the user’s music library. _(beta)_
- [musicSubscriptionOffer(isPresented:options:onLoadCompletion:)](<view/musicsubscriptionoffer(ispresented_options_onloadcompletion_).md>) — Initiates the process of presenting a sheet with subscription offers for Apple Music when the `isPresented` binding is `true`.
- [currentEntitlementTask(for:priority:action:)](<view/currententitlementtask(for_priority_action_).md>) — Declares the view as dependent on the entitlement of an In-App Purchase product, and returns a modified view.
- [inAppPurchaseOptions(_:)](<view/inapppurchaseoptions(__).md>) — Add a function to call before initiating a purchase from StoreKit view within this view, providing a set of options for the purchase.
- [manageSubscriptionsSheet(isPresented:subscriptionGroupID:)](<view/managesubscriptionssheet(ispresented_subscriptiongroupid_).md>)
- [onInAppPurchaseCompletion(perform:)](<view/oninapppurchasecompletion(perform_).md>) — Add an action to perform when a purchase initiated from a StoreKit view within this view completes.
- [onInAppPurchaseStart(perform:)](<view/oninapppurchasestart(perform_).md>) — Add an action to perform when a user triggers the purchase button on a StoreKit view within this view.
- [productIconBorder()](<view/producticonborder().md>) — Adds a standard border to an in-app purchase product’s icon .
- [productViewStyle(_:)](<view/productviewstyle(__).md>) — Sets the style for In-App Purchase product views within a view.
- [productDescription(_:)](<view/productdescription(__).md>) — Configure the visibility of labels displaying an in-app purchase product description within the view.
- [storeButton(_:for:)](<view/storebutton(__for_).md>) — Specifies the visibility of auxiliary buttons that store view and subscription store view instances may use.
- [storeProductTask(for:priority:action:)](<view/storeproducttask(for_priority_action_).md>) — Declares the view as dependent on an In-App Purchase product and returns a modified view.
- [storeProductsTask(for:priority:action:)](<view/storeproductstask(for_priority_action_).md>) — Declares the view as dependent on a collection of In-App Purchase products and returns a modified view.
- [subscriptionStatusTask(for:priority:action:)](<view/subscriptionstatustask(for_priority_action_).md>) — Declares the view as dependent on the status of an auto-renewable subscription group, and returns a modified view.
- [subscriptionStoreButtonLabel(_:)](<view/subscriptionstorebuttonlabel(__).md>) — Configures subscription store view instances within a view to use the provided button label.
- [subscriptionStoreControlIcon(icon:)](<view/subscriptionstorecontrolicon(icon_).md>) — Sets a view to use to decorate individual subscription options within a subscription store view.
- [subscriptionStoreControlStyle(_:)](<view/subscriptionstorecontrolstyle(__).md>) — Sets the control style for subscription store views within a view.
- [subscriptionStoreControlStyle(_:placement:)](<view/subscriptionstorecontrolstyle(__placement_).md>) — Sets the control style and control placement for subscription store views within a view.
- [subscriptionStoreOptionGroupStyle(_:)](<view/subscriptionstoreoptiongroupstyle(__).md>) — Sets the style subscription store views within this view use to display groups of subscription options.
- [subscriptionStorePickerItemBackground(_:)](<view/subscriptionstorepickeritembackground(__).md>) — Sets the background style for picker items of the subscription store view instances within a view.
- [subscriptionStorePickerItemBackground(_:in:)](<view/subscriptionstorepickeritembackground(__in_).md>) — Sets the background shape and style for subscription store view picker items within a view.
- [subscriptionStorePolicyDestination(for:destination:)](<view/subscriptionstorepolicydestination(for_destination_).md>) — Configures a view as the destination for a policy button action in subscription store views.
- [subscriptionStorePolicyDestination(url:for:)](<view/subscriptionstorepolicydestination(url_for_).md>) — Configures a URL as the destination for a policy button action in subscription store views.
- [subscriptionStorePolicyForegroundStyle(_:)](<view/subscriptionstorepolicyforegroundstyle(__).md>) — Sets the style for the terms of service and privacy policy buttons within a subscription store view.
- [subscriptionStorePolicyForegroundStyle(_:_:)](<view/subscriptionstorepolicyforegroundstyle(____).md>) — Sets the primary and secondary style for the terms of service and privacy policy buttons within a subscription store view.
- [subscriptionStoreSignInAction(_:)](<view/subscriptionstoresigninaction(__).md>) — Adds an action to perform when a person uses the sign-in button on a subscription store view within a view.
- [subscriptionStoreControlBackground(_:)](<view/subscriptionstorecontrolbackground(__).md>) — Set a standard effect to use for the background of subscription store view controls within the view.
- [subscriptionPromotionalOffer(offer:compactJWS:)](<view/subscriptionpromotionaloffer(offer_compactjws_).md>) — Selects a promotional offer to apply to a purchase a customer makes from a subscription store view.
- [subscriptionIntroductoryOffer(applyOffer:compactJWS:)](<view/subscriptionintroductoryoffer(applyoffer_compactjws_).md>) — Selects the introductory offer eligibility preference to apply to a purchase a customer makes from a subscription store view.
- [subscriptionOfferViewButtonVisibility(_:for:)](<view/subscriptionofferviewbuttonvisibility(__for_).md>)
- [subscriptionOfferViewDetailAction(_:)](<view/subscriptionofferviewdetailaction(__).md>)
- [subscriptionOfferViewStyle(_:)](<view/subscriptionofferviewstyle(__).md>)
- [preferredSubscriptionOffer(_:)](<view/preferredsubscriptionoffer(__).md>) — Selects a subscription offer to apply to a purchase that a customer makes from a subscription store view, a store view, or a product view.
- [preferredSubscriptionPricingTerms(_:)](<view/preferredsubscriptionpricingterms(__).md>)

### Accessing health data

- [healthDataAccessRequest(store:objectType:predicate:trigger:completion:)](<view/healthdataaccessrequest(store_objecttype_predicate_trigger_completion_).md>) — Asynchronously requests permission to read a data type that requires per-object authorization (such as vision prescriptions).
- [healthDataAccessRequest(store:readTypes:trigger:completion:)](<view/healthdataaccessrequest(store_readtypes_trigger_completion_).md>) — Requests permission to read the specified HealthKit data types.
- [healthDataAccessRequest(store:shareTypes:readTypes:trigger:completion:)](<view/healthdataaccessrequest(store_sharetypes_readtypes_trigger_completion_).md>) — Requests permission to save and read the specified HealthKit data types.
- [workoutPreview(_:isPresented:)](<view/workoutpreview(__ispresented_).md>) — Presents a preview of the workout contents as a modal sheet

### Providing tips

- [popoverTip(_:arrowEdge:action:)](<view/popovertip(__arrowedge_action_).md>) — Presents a popover tip on the modified view.
- [popoverTip(_:isPresented:attachmentAnchor:arrowEdge:action:)](<view/popovertip(__ispresented_attachmentanchor_arrowedge_action_).md>) — Presents a popover tip on the modified view.
- [popoverTip(_:isPresented:attachmentAnchor:arrowEdges:action:)](<view/popovertip(__ispresented_attachmentanchor_arrowedges_action_).md>) — Presents a popover tip on the modified view.
- [tipAnchor(_:)](<view/tipanchor(__).md>) — Sets a value for the specified tip anchor to be used to anchor a tip view to the `.bounds` of the view.
- [tipBackground(_:)](<view/tipbackground(__).md>) — Sets the tip’s view background to a style.
- [tipBackgroundInteraction(_:)](<view/tipbackgroundinteraction(__).md>) — Controls whether people can interact with the view behind a presented tip.
- [tipCornerRadius(_:antialiased:)](<view/tipcornerradius(__antialiased_).md>) — Sets the corner radius for an inline tip view.
- [tipImageSize(_:)](<view/tipimagesize(__).md>) — Sets the size for a tip’s image.
- [tipViewStyle(_:)](<view/tipviewstyle(__).md>) — Sets the given style for TipView within the view hierarchy.
- [tipImageStyle(_:)](<view/tipimagestyle(__).md>) — Sets the style for a tip’s image.
- [tipImageStyle(_:_:)](<view/tipimagestyle(____).md>) — Sets the style for a tip’s image.
- [tipImageStyle(_:_:_:)](<view/tipimagestyle(______).md>) — Sets the style for a tip’s image.

### Showing a translation

- [translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:)](<view/translationpresentation(ispresented_text_attachmentanchor_arrowedge_replacementaction_).md>) — Presents a translation popover when a given condition is true.
- [translationTask(_:action:)](<view/translationtask(__action_).md>) — Adds a task to perform before this view appears or when the translation configuration changes.
- [translationTask(source:target:action:)](<view/translationtask(source_target_action_).md>) — Adds a task to perform before this view appears or when the specified source or target languages change.
- [translationTask(source:target:preferredStrategy:action:)](<view/translationtask(source_target_preferredstrategy_action_).md>) — Adds a task to perform before this view appears or when the specified source or target languages change.

### Presenting journaling suggestions

- [journalingSuggestionsPicker(isPresented:onCompletion:)](<view/journalingsuggestionspicker(ispresented_oncompletion_).md>) — Presents a visual picker interface that contains events and images that a person can select to retrieve more information.
- [journalingSuggestionsPicker(isPresented:journalingSuggestionToken:onCompletion:)](<view/journalingsuggestionspicker(ispresented_journalingsuggestiontoken_oncompletion_).md>) — Presents a visual picker interface that contains events and images that a person can select to retrieve more information.

### Managing contact access

- [contactAccessButtonCaption(_:)](<view/contactaccessbuttoncaption(__).md>)
- [contactAccessButtonStyle(_:)](<view/contactaccessbuttonstyle(__).md>)
- [contactAccessPicker(isPresented:completionHandler:)](<view/contactaccesspicker(ispresented_completionhandler_).md>) — Modally present UI which allows the user to select which contacts your app has access to.

### Syncing game saves

- [gameSaveSyncingAlert(directory:finishedLoading:)](<view/gamesavesyncingalert(directory_finishedloading_).md>) — Presents a modal view while the game synced directory loads.

### Handling game controller events

- [handlesGameControllerEvents(matching:)](<view/handlesgamecontrollerevents(matching_).md>) — Specifies the game controllers events which should be delivered through the GameController framework when the view, or one of its descendants has focus.

### Creating a tabletop game

- [tabletopGame(_:parent:automaticUpdate:)](<view/tabletopgame(__parent_automaticupdate_).md>) — Adds a tabletop game to a view.
- [tabletopGame(_:parent:automaticUpdate:interaction:)](<view/tabletopgame(__parent_automaticupdate_interaction_).md>) — Supplies a closure which returns a new interaction whenever needed.

### Configuring camera controls

- [realityViewCameraControls](environmentvalues/realityviewcameracontrols.md) — The camera controls for the reality view.
- [realityViewCameraControls(_:)](<view/realityviewcameracontrols(__).md>) — Adds gestures that control the position and direction of a virtual camera.
- [realityViewLayoutBehavior(_:)](<view/realityviewlayoutbehavior(__).md>) — A view modifier that controls the frame sizing and content alignment behavior for `RealityView`

### Interacting with transactions

- [transactionPicker(isPresented:selection:)](<view/transactionpicker(ispresented_selection_).md>) — Presents a picker that selects a collection of transactions.
