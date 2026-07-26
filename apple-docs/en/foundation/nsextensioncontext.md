---
title: NSExtensionContext
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsextensioncontext
source_url: 'https://developer.apple.com/documentation/foundation/nsextensioncontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsextensioncontext.json'
content_hash: 'sha256:ad201f76db0b3502'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSExtensionContext

<sub>Class</sub>

The host app context from which an app extension is invoked.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSExtensionContext
```

## Overview

When a host app sends a request to an app extension, it provides an extension context. For many app extensions, the most important part of the context is the data the user wants to work with, which is contained in the [inputItems](nsextensioncontext/inputitems.md) property.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Handling requests

- [- completeRequestReturningItems:completionHandler:](<nsextensioncontext/completerequest(returningitems_completionhandler_).md>) — Tells the host app to complete the app extension request with an array of result items.
- [- cancelRequestWithError:](<nsextensioncontext/cancelrequest(witherror_).md>) — Tells the host app to cancel the app extension request, with a supplied error.
- [NSExtensionItemsAndErrorsKey](nsextensionitemsanderrorskey.md) — The extension items and errors key.

### Opening URLs

- [- openURL:completionHandler:](<nsextensioncontext/open(__completionhandler_).md>) — Asks the system to open a URL on behalf of the currently running app extension.

### Storing extension items

- [inputItems](nsextensioncontext/inputitems.md) — The list of input [NSExtensionItem](nsextensionitem.md) objects associated with the context.

### Controlling media playback in notification content extensions

- [- mediaPlayingStarted](<nsextensioncontext/mediaplayingstarted().md>) — Tells the system that the Notification Content app extension began playing a media file.
- [- mediaPlayingPaused](<nsextensioncontext/mediaplayingpaused().md>) — Tells the system that the Notification Content app extension stopped playing a media file.

### Populating your share extension with metadata

- [intent](nsextensioncontext/intent.md) — Metadata for populating your share extensions interface.

### Getting Siri-related information

- [hostedViewMinimumAllowedSize](nsextensioncontext/hostedviewminimumallowedsize.md) — The minimum size for a Siri hosted view.
- [hostedViewMaximumAllowedSize](nsextensioncontext/hostedviewmaximumallowedsize.md) — The maximum size for a Siri hosted view.
- [- interfaceParametersDescription](<nsextensioncontext/interfaceparametersdescription().md>) — Returns a human-readable string describing the data that SiriKit displays to the user when you handle an intent.

### Supporting broadcasting

- [- loadBroadcastingApplicationInfoWithCompletion:](<nsextensioncontext/loadbroadcastingapplicationinfo(completion_).md>) _(deprecated)_
- [- completeRequestWithBroadcastURL:setupInfo:](<nsextensioncontext/completerequest(withbroadcast_setupinfo_).md>) _(deprecated)_

### Handling notification actions

- [notificationActions](nsextensioncontext/notificationactions.md)
- [- performNotificationDefaultAction](<nsextensioncontext/performnotificationdefaultaction().md>)
- [- dismissNotificationContentExtension](<nsextensioncontext/dismissnotificationcontentextension().md>)

### Working with notifications

- [NSExtensionHostDidBecomeActiveNotification](nsnotification/name-swift.struct/nsextensionhostdidbecomeactive.md) — Posted when the extension’s host app moves from the inactive to the active state.
- [NSExtensionHostWillResignActiveNotification](nsnotification/name-swift.struct/nsextensionhostwillresignactive.md) — Posted when the extension’s host app moves from the active to the inactive state.
- [NSExtensionHostDidEnterBackgroundNotification](nsnotification/name-swift.struct/nsextensionhostdidenterbackground.md) — Posted when the extension’s host app begins running in the background.
- [NSExtensionHostWillEnterForegroundNotification](nsnotification/name-swift.struct/nsextensionhostwillenterforeground.md) — Posted when the extension’s host app begins running in the foreground.

### Working with notification messages

- [DidBecomeActiveMessage](nsextensioncontext/didbecomeactivemessage.md) — A message the system sends when the extension’s host app moves from the inactive to the active state.
- [WillResignActiveMessage](nsextensioncontext/willresignactivemessage.md) — A message the system sends when the extension’s host app moves from the active to the inactive state.
- [DidEnterBackgroundMessage](nsextensioncontext/didenterbackgroundmessage.md) — A message the system sends when the extension’s host app begins running in the background.
- [WillEnterForegroundMessage](nsextensioncontext/willenterforegroundmessage.md) — A message the system sends when the extension’s host app begins running in the foreground.

### Deprecated

- [- completeRequestWithBroadcastURL:broadcastConfiguration:setupInfo:](<nsextensioncontext/completerequest(withbroadcast_broadcastconfiguration_setupinfo_).md>) — Tells the host app to complete the app extension request with the specified broadcast information. _(deprecated)_
- [widgetActiveDisplayMode](nsextensioncontext/widgetactivedisplaymode.md) — The active display mode of the widget. _(deprecated)_
- [widgetLargestAvailableDisplayMode](nsextensioncontext/widgetlargestavailabledisplaymode.md) — The largest display mode the widget supports. _(deprecated)_
- [- widgetMaximumSizeForDisplayMode:](<nsextensioncontext/widgetmaximumsize(for_).md>) — Returns the maximum size for the specified widget display mode. _(deprecated)_

## See Also

### Extension Support

- [NSExtensionRequestHandling](nsextensionrequesthandling.md) — The interface an app extension uses to respond to a request from a host app.
