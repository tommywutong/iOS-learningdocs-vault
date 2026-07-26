---
title: WebPage
framework: WebKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/webkit/webpage
source_url: 'https://developer.apple.com/documentation/webkit/webpage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/webkit/webpage.json'
content_hash: 'sha256:3e49597161a05dca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WebKit](../webkit.md)

# WebPage

<sub>Class</sub>

An object that controls and manages the behavior of interactive web content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor final class WebPage
```

## Overview

A [WebPage](webpage.md) is an [Observable](../observation/observable.md) type, which you use to access various properties of web content and track changes to them. Use [WebPage](webpage.md) to interact with web content, like evaluating JavaScript or converting the page to PDF data. The following example shows you how you can combine these capabilities to get specific metadata from an ephemeral page with a custom user agent:

```swift
func fetchMetadata(for url: URL) async throws -> (title: String, description: String) {
    let botAgent = """
    Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.4 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.4 facebookexternalhit/1.1 Facebot Twitterbot/1.0
    """

    var configuration = WebPage.Configuration()
    configuration.loadsSubresources = false
    configuration.defaultNavigationPreferences.allowsContentJavaScript = false
    configuration.websiteDataStore = .nonPersistent()

    // Set up the configured page.

    let page = WebPage(configuration: configuration)
    page.customUserAgent = botAgent

    // Load the request and wait for navigation to complete.

    let request = URLRequest(url: url)
    for try await event in page.load(request) {
        // Optionally do something with `event`.
    }

    // At this point, the navigation is complete.
    // Now, use JavaScript to query the appropriate properties of the page.

    let fetchOpenGraphProperty = """
    const propertyValues = document.querySelectorAll(`meta[property="${property}"]`);
    return propertyValues[0];
    """

    let javaScriptResult = try await page.callJavaScript(fetchOpenGraphProperty, arguments: arguments)
    guard let description = javaScriptResult as? String else {
        // Handle failure, like throwing an error.
    }

    guard let title = page.title else {
        // Handle failure, like throwing an error.
    }

    return (title, description)
}
```

Use [WebPage](webpage.md) to programmatically navigate to various types of resources like URL requests, HTML strings, and data. Optionally, you can observe these navigations through the async sequence returned by their associated loading functions, and you can customize them by using a type that conforms to the [NavigationDeciding](webpage/navigationdeciding.md) protocol. You can also use the [backForwardList](webpage/backforwardlist-swift.property.md) property to observe changes to people’s navigation history, and to programmatically navigate to a specific back-forward list item.

[WebPage](webpage.md) also conforms to the `Transferable` protocol. You can use this conformance to export the page to various different types of content, like PDF, web archive data, and other types. For customization of PDF or image exprt, use [exported(as:)](<webpage/exported(as_).md>).

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [Observable](../observation/observable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Transferable](../coretransferable/transferable.md)

## Topics

### Creating a WebPage

- [Configuration](webpage/configuration.md) — A configuration type that specifies the preferences and behaviors of a webpage.
- [init(configuration:)](<webpage/init(configuration_).md>) — Create a new WebPage.
- [init(configuration:dialogPresenter:)](<webpage/init(configuration_dialogpresenter_).md>) — Create a new WebPage.
- [init(configuration:navigationDecider:)](<webpage/init(configuration_navigationdecider_).md>) — Create a new WebPage.
- [init(configuration:navigationDecider:dialogPresenter:)](<webpage/init(configuration_navigationdecider_dialogpresenter_).md>) — Create a new WebPage.

### Managing navigation between webpages

- [NavigationDeciding](webpage/navigationdeciding.md) — Allows providing custom behavior to handle navigation changes and to coordinate these changes for the web page’s main page.
- [NavigationAction](webpage/navigationaction.md) — An object that contains information about an action that causes navigation to occur.
- [NavigationResponse](webpage/navigationresponse.md) — An object that contains the response to a navigation request, and which you use to make navigation-related policy decisions.
- [NavigationPreferences](webpage/navigationpreferences.md) — A type that specifies the behaviors to use when loading and rendering page content.
- [backForwardList](webpage/backforwardlist-swift.property.md) — The webpage’s back-forward list.
- [FrameInfo](webpage/frameinfo.md) — A type that contains information about a frame on a webpage.

### Observing navigation between webpages

- [BackForwardList](webpage/backforwardlist-swift.struct.md) — An observable representation of a webpage’s previously loaded resources.
- [NavigationEvent](webpage/navigationevent.md) — A particular state that occurs during the progression of a navigation.
- [navigations](webpage/navigations.md) — A sequence of all the navigation events that occur throughout the webpage, including both user navigation and programmatic navigation.
- [NavigationError](webpage/navigationerror.md) — A specific error that caused a navigation to fail.

### Configuring a WebPage

- [Configuration](webpage/configuration.md) — A configuration type that specifies the preferences and behaviors of a webpage.
- [DeviceSensorAuthorization](webpage/devicesensorauthorization.md) — A type that describes the authorization permissions policy for the device’s sensors a web resource may access.
- [URLScheme](urlscheme.md) — A type representing a valid URL scheme.
- [URLSchemeHandler](urlschemehandler.md) — A protocol for loading resources with URL schemes that WebKit doesn’t handle.
- [URLSchemeTaskResult](urlschemetaskresult.md) — A value used as part of a sequence of results from a [URLSchemeHandler](urlschemehandler.md), which can either be a `Data` or a `URLResponse`.

### Loading web content

- [load(_:)](<webpage/load(__)-32ngj.md>) — Navigates to an item from the back-forward list and sets it as the current item.
- [load(_:)](<webpage/load(__)-7kw3h.md>) — Loads the web content that the specified URL request object references and navigates to that content.
- [load(_:)](<webpage/load(__)-8wfiq.md>) — Loads the web content that the specified URL references and navigates to that content.
- [load(_:mimeType:characterEncoding:baseURL:)](<webpage/load(__mimetype_characterencoding_baseurl_).md>) — Loads the content of the specified data object and navigates to it.
- [load(html:baseURL:)](<webpage/load(html_baseurl_).md>) — Loads the contents of the specified HTML string and navigates to it.
- [load(simulatedRequest:responseHTML:)](<webpage/load(simulatedrequest_responsehtml_).md>) — Loads the web content from the HTML you provide as if the HTML were the response to the request.
- [load(simulatedRequest:response:responseData:)](<webpage/load(simulatedrequest_response_responsedata_).md>) — Loads the web content from the data you provide as if the data were the response to the request.
- [isLoading](webpage/isloading.md) — Indicates whether the webpage is currently loading content.
- [estimatedProgress](webpage/estimatedprogress.md) — An estimate of completion percentage of the current navigation.

### Managing the loading process

- [reload(fromOrigin:)](<webpage/reload(fromorigin_).md>) — Reloads the current webpage.
- [stopLoading()](<webpage/stoploading().md>) — Stops loading all resources on the current page.

### Inspecting page information

- [CSSMediaType](webpage/cssmediatype.md) — A CSS media type as defined by the [CSS specification](https://www.w3.org/TR/mediaqueries-4/#media-types), or an arbitrary media type value.
- [title](webpage/title.md) — The page title.
- [url](webpage/url.md) — The URL for the current webpage.
- [mediaType](webpage/mediatype.md) — The media type for the contents of the webpage.
- [customUserAgent](webpage/customuseragent.md) — The custom user agent string.
- [serverTrust](webpage/servertrust.md) — The trust management object you use to evaluate trust for the current webpage.
- [hasOnlySecureContent](webpage/hasonlysecurecontent.md) — Indicates whether the webpage loaded all resources on the page through securely encrypted connections.
- [themeColor](webpage/themecolor.md) — The theme color that the system gets from the first valid meta tag in the webpage.
- [isBlockedByScreenTime](webpage/isblockedbyscreentime.md) — Indicates whether Screen Time blocking has occurred.
- [isInspectable](webpage/isinspectable.md) — Indicates whether you can inspect the page with Safari Web Inspector.
- [isWritingToolsActive](webpage/iswritingtoolsactive.md) — Indicates whether Writing Tools is active for the page.

### Executing JavaScript

- [callJavaScript(_:arguments:in:contentWorld:)](<webpage/calljavascript(__arguments_in_contentworld_).md>) — Executes the specified string as an async JavaScript function.

### Customizing JavaScript dialogs

- [DialogPresenting](webpage/dialogpresenting.md) — Allows providing custom behavior to handle JavaScript actions and provide a response.
- [FileInputPromptResult](webpage/fileinputpromptresult.md) — The result of handling a JavaScript open invocation.
- [JavaScriptConfirmResult](webpage/javascriptconfirmresult.md) — The result of handling a JavaScript confirm invocation.
- [JavaScriptPromptResult](webpage/javascriptpromptresult.md) — The result of handling a JavaScript confirm invocation.

### Exporting webpage content

- [ExportedContentConfiguration](webpage/exportedcontentconfiguration.md) — A specialized configuration of a specific exportable type that can have specific properties unique to the content type.
- [exported(as:)](<webpage/exported(as_).md>) — Using the type’s `Transferable` conformance implementation, exports a value as binary data, optionally with a specified configuration for that type of data.

### Interacting with media

- [FullscreenState](webpage/fullscreenstate-swift.enum.md) — The set of possible fullscreen states a webpage may be in.
- [pauseAllMediaPlayback()](<webpage/pauseallmediaplayback().md>) — Pauses playback of all media in the web view.
- [mediaPlaybackState()](<webpage/mediaplaybackstate().md>) — Determine the playback status of media in the page.
- [setAllMediaPlaybackSuspended(_:)](<webpage/setallmediaplaybacksuspended(__).md>) — Changes whether the webpage is suspending playback of all media in the page.
- [closeAllMediaPresentations()](<webpage/closeallmediapresentations().md>) — Closes all media the webpage is presenting, including picture-in-picture video and fullscreen video.
- [fullscreenState](webpage/fullscreenstate-swift.property.md) — The fullscreen state the page is currently in.

### Managing the microphone and camera

- [cameraCaptureState](webpage/cameracapturestate.md) — Indicates whether the webpage is using the camera to capture images or video.
- [microphoneCaptureState](webpage/microphonecapturestate.md) — Indicates whether the webpage is using the microphone to capture audio.
- [setCameraCaptureState(_:)](<webpage/setcameracapturestate(__).md>) — Changes whether the webpage is using the camera to capture images or video.
- [setMicrophoneCaptureState(_:)](<webpage/setmicrophonecapturestate(__).md>) — Changes whether the webpage is using the microphone to capture audio.

### Structures

- [FormInfo](webpage/forminfo.md) — A type that contains information about a form submission from a webpage.
- [ImmersiveEnvironment](webpage/immersiveenvironment.md) — An object representing a website-provided immersive environment that is ready for presentation. _(beta)_

## See Also

### Essentials

- [Building a cross-platform web browser](building-a-cross-platform-web-browser.md) — Implement a browser on multiple platforms that loads content, manages navigation history, and saves favorite websites, using WebKit for SwiftUI.
- [WebView](webview-swift.struct.md) — A view that displays some web content.
