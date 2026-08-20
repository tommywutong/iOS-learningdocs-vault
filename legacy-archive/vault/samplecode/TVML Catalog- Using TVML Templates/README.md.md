---
title: 'TVML Catalog: Using TVML Templates'
apple_id: TP40016505
resource_type: Sample Code
platform: tvOS
topic: User Experience
technology: TVMLKit
published: '2017-06-06'
source_url: https://developer.apple.com/library/archive/samplecode/TVMLCatalog/Listings/README_md.html
archived_at: '2026-07-18T03:26:06.144380Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TVML Catalog: Using TVML Templates](TVML%20Catalog-%20Using%20TVML%20Templates.md)


[Next](TVMLCatalog-AppDelegate.swift.md)[Previous](TVML%20Catalog-%20Using%20TVML%20Templates.md)

# README.md

```
# Using TVML Templates

This sample demonstrates how to use the [TVMLKit](https://developer.apple.com/documentation/tvmlkit) framework to display TVML content in a tvOS application, and provides a catalog of the primary TVML templates. For a complete list of templates and available elements, see the [Apple TV Markup Language Reference](https://developer.apple.com/library/content/documentation/LanguagesUtilities/Conceptual/ATV_Template_Guide/).

## Overview

The project is split into two parts:

- TVMLCatalog: this directory contains the Xcode project and related files. The AppDelegate.swift file handles the setup of the TVMLKit framework and launching the JavaScript context to manage the app.
- Server: this directory contains the JavaScript and XML files needed to render the application. The contents of this directory must be hosted on a server accessible from the device.

After the application has been setup and is running you will primarily be working in the client directory. This is where you define the templates you want to present to the user and control the presentation and lifecyle of the application with JavaScript. As you define new templates to present, experiment with the available styles to get a feel for the flexibility provided in TVMLKit and how customizable they are.

To help debug and experiment, you can use the Safari WebInspector to attach to the JavaScript context. WebInspector provides you with a full JavaScript debugging environment. You will need to turn on the Develop menu from Safari > Preferences > Advanced. Select your device from the Develop drop down menu to see a list of running JavaScript contexts.

When you are ready to add more advanced features to your application, open the client files and read through the Apple TV Markup Language Reference. You can add new JavaScript APIs, create new XML templates or elements, and pass additional information into the JavaScript context at launch. You can also expand the capabilities of your application by creating a TopShelfExtenstion for presenting items in the top shelf when your application is moved to the first row of Apple TV main menu.

## Installation instructions:

To start a local server run the following command in a terminal within the "Server" folder to create a simple webserver.

` ``` `
ruby -run -ehttpd . -p9001
` ``` `

- Open the TVMLCatalog.xcodeproj project in Xcode
- If the client code is hosted on a remote server, or you are running this app on the Apple TV change the following property in AppDelegate.swift:
    - Change the [`tvBaseURL`](x-source-tag://tvBaseURL) value to the `URL` hosting the contents of the client directory
    - Note that the Info.plist currently disables App Transport Security via NSAllowsArbitraryLoads. This is only to simplify the process of reviewing the sample. Your own apps should rely on properly secured servers that do not require App Transport Security to be disabled.
- Build and run the application
- When running this application on a device you will need to add a signing profile in the projects Build Settings.

## Requirements

Build Requirements: Xcode 9.0, tvOS 11.0 SDK
Runtime Requirements: tvOS 11.0 or later
```

[Next](TVMLCatalog-AppDelegate.swift.md)[Previous](TVML%20Catalog-%20Using%20TVML%20Templates.md)

