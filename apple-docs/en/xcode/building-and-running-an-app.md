---
title: Building and running an app
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/building-and-running-an-app
source_url: 'https://developer.apple.com/documentation/xcode/building-and-running-an-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/building-and-running-an-app.json'
content_hash: 'sha256:e08bb521cd37613a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Xcode](../xcode.md)

# Building and running an app

<sub>Article</sub>

Compile your source files and assemble an app bundle to run on a device or simulator.

## Overview

During development, you build and run your app many times to test new features and fix bugs. Each time you build, Xcode analyzes your app’s source files to determine which ones it needs to recompile. Xcode also identifies any other tasks that it needs to perform, such as running custom scripts. Depending on the state of your project, Xcode performs either a complete rebuild of your project, or an incremental build of only the changed items.

When you run an app after a successful build, Xcode launches the app on the device you choose. Xcode runs Mac apps on the same device that you launched Xcode on. Xcode runs iOS, iPadOS, tvOS, visionOS, and watchOS apps on Simulator or on a connected device of your choice.

### Configure a target for your app

Xcode determines how to build apps and other products from your project’s target information. A _target_ contains the tasks required to create an executable, and the settings to use to build it. For example, an app target might contain the list of files to compile, the resources to copy into the app’s bundle, and other steps needed to configure the app.

When you create a new project from a template, you choose a default target, which Xcode configures using the information you provide. You can add new targets to your project at any time to create additional products.

For more information, see [Configuring a new target in your project](configuring-a-new-target-in-your-project.md).

### Select a scheme for your target

A _build scheme_ is a collection of settings that specify which targets to build, the build configuration to use, and the executable environment for the running product. Xcode creates schemes for most targets automatically, and you can create additional schemes to customize the build and execution options. For example, you might create a new scheme to pass additional launch arguments to your app.

To build an app, or any other target, choose a scheme that contains the target. Xcode displays the selected scheme in the toolbar of your project window. To change the selected scheme, click the scheme name and choose a new one from the pop-up menu.

![](../../../attachments/f7afef3afd8dd907dae0a062d8309f1b/build-select-scheme@2x.png)

<sub>A screenshot of the project editor showing the scheme pop-up menu displayed in the toolbar with the scheme that builds the app selected.</sub>

For more information on schemes, see [Customizing the build schemes for a project](customizing-the-build-schemes-for-a-project.md).

### Tell Xcode where to run your app

After you choose a scheme to build, click the run destination name next to the scheme name in the toolbar, and choose a simulated or physical device from the pop-up menu.

![](../../../attachments/292a795d5fa6f2f532ab1c4a00ae57c0/build-select-device@2x.png)

<sub>A screenshot of the project editor showing the run destination pop-up menu displayed in the toolbar with My Mac selected.</sub>

Choose a run destination that gives you the capabilities you need. For Mac products, choose My Mac. For other platforms, if the app doesn’t require actual hardware, you can choose a simulator to test features quickly on your Mac. If your app requires actual hardware, or you’re ready to see how your app behaves in real conditions, choose a physical device.

For information on configuring new simulators or connecting to a physical device, see [Running your app on simulated or physical devices](running-your-app-on-simulated-or-physical-devices.md).

> [!important] Important
> Before you ship any code, test and gather metrics on physical devices. Simulators offer quick turnaround times during development, but they don’t simulate the actual performance of target devices.

### Build, run, and debug your app

To build and run your code using the current scheme, choose Product \> Run, or click the Run button in the toolbar above the navigator.

Xcode analyzes your scheme’s targets and builds them in the proper sequence. After a successful build, Xcode launches the associated app. If you selected the Debug executable option in the Info tab of the scheme editor, Xcode attaches the debugger to the app immediately after launch. To build a scheme without running the app, choose Product \> Build instead.

If Xcode encounters an error during a build, Xcode stops building the app and reports the error in the Issue navigator. If you deselect the “Stop build on first error” setting in the General tab of Xcode settings, Xcode continues to build and report errors for the rest of your project’s files. To stop an in-progress build, choose Product \> Stop, or click the Stop button in the toolbar.

A scheme’s build configuration determines how Xcode launches the product. For a scheme that builds an app, Xcode launches the app itself. For other products, you specify the app to launch using the scheme editor. You can also use the scheme editor to specify launch arguments, runtime data, and debugging parameters.

## See Also

### Essentials

- [Creating an Xcode project for an app](creating-an-xcode-project-for-an-app.md) — Start developing your app by creating an Xcode project from a template.
- [Creating your app’s interface with SwiftUI](creating-your-app-s-interface-with-swiftui.md) — Develop apps in SwiftUI with an interactive preview that keeps the code and layout in sync.
- [Previewing your app’s interface in Xcode](previewing-your-apps-interface-in-xcode.md) — Iterate designs quickly and preview your apps’ displays across different Apple devices.
- [Xcode updates](../updates/xcode.md) — Learn about important changes to Xcode.
