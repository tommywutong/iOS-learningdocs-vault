---
title: ExtensionFoundation
framework: ExtensionFoundation
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 17.4+, visionOS 1.1+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/extensionfoundation
source_url: 'https://developer.apple.com/documentation/extensionfoundation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/extensionfoundation.json'
content_hash: 'sha256:da08168dc873af70'
translated: false
---

> Navigation: [Technologies](technologies.md)

# ExtensionFoundation

<sub>Framework</sub>

Create executable bundles to extend the functionality of other apps.

## Overview

An app extension is an executable code bundle that extends the capabilities of the system, or the capabilities of another app. At the system level, app extensions give you a way to add your custom capabilities to system features. For example, [widgets](widgetkit/creating-a-widget-extension.md) display your app’s content in specific locations like the iOS Home Screen and Lock screen. To build app extensions for system features, you typically use a different framework or a dedicated set of types instead of this framework.

Adopt the `ExtensionFoundation` framework directly when you want to add support for app extensions to your own apps. An app extension model gives you a way to extend your app’s capabilities safely in several ways. If your app needs to run risky code, you might isolate that code in an app extension to prevent it from affecting the rest of your app. Alternatively, a productivity app might give other developers a way to create app extensions that extend the app’s core feature set.

Host apps use the `ExtensionFoundation` framework to find and launch available app extensions. App extensions use this framework to communicate with the host app and support non-UI features. If your app also integrates custom UI from its app extensions, adopt the [ExtensionKit](extensionkit.md) framework in addition to this one.

## Topics

### Essentials

- [Adding support for app extensions to your app](extensionfoundation/adding-support-for-app-extensions-to-your-app.md) — Create an app extension model by defining your code’s extension points and communicating with app extensions at runtime.

### App-extension setup

- [Building an app extension to support a host app](extensionfoundation/building-an-app-extension-to-support-a-host-app.md) — Create an app extension to perform tasks in a separate process from a host app.
- [AppExtension](extensionfoundation/appextension.md) — An interface you use to declare the content, structure, and behavior of an app extension.
- [AppExtensionConfiguration](extensionfoundation/appextensionconfiguration.md) — An interface you use to configure the XPC connection in your app extension.
- [ConnectionHandler](extensionfoundation/connectionhandler.md) — A type that contains a custom closure that handles incoming XPC connections.

### Host-app configuration

- [Discovering app extensions from your app](extensionfoundation/discovering-app-extensions-from-your-app.md) — Find the app extensions that match your host app’s extension points and are available to use.
- [AppExtensionProcess](extensionfoundation/appextensionprocess.md) — A type the host app creates to launch and manage an app extension.
- [AppExtensionIdentity](extensionfoundation/appextensionidentity.md) — A type that uniquely identifies an app extension on the system.

### Extension-point management

- [AppExtensionPoint](extensionfoundation/appextensionpoint.md) — A type you use to declare your host app’s extension points and bind to them from app extensions.
- [ExtensionPointDefining](extensionfoundation/extensionpointdefining.md) — An interface that extension point types adopt.
