---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/customizing/customizing.html
archived_at: '2026-07-15T07:29:18.385145Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Customizing%20Key%20Equivalents.md)[Previous](Remote%20Debugging%20in%20Xcode.md)

# Customizing Xcode

The Xcode development environment does its
best to provide an easy, intuitive interface for the most common
development tasks that you face. However, there are many different factors
that affect your requirements for your development environment.
Luckily, Xcode is also a very flexible tool, providing many different
ways to customize the development process.

The following chapters describe many of the ways in which
you can customize Xcode to make it a more productive and custom-tailored
environment for your development. Some features are of particular
use to developers who are familiar with BBEdit, CodeWarrior, or MPW,
but most should be useful to any developer.

In particular, these chapters show you how to customize Xcode’s
user interface, change user settings with Xcode Preferences, and
add functionality to the Xcode application using the User Scripts
menu. In addition, many of the chapters that appear in previous
sections of this document also describe ways in which you can use
Xcode to customize your development environment. It does not describe
how to extend the Xcode application.

Xcode offers many opportunities for customization, including:

- Customizing
  the build process. Xcode provides many different ways for you to customize
  the behavior of the build system. The Copy Files and Run Script
  build phases, described in [Build Phases](Build%20Phases.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshawugssbi5ceiscj), let you add
  your own operations to the build process for a target; [Build Rules](Build%20Phases.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshawueqsdindekrck) let you customize
  the way in which files in a target’s build phases are processed.
  You can use Shell Script targets to add reusable custom operations
  to the build process; external targets let you build using an external build
  tool of your own choice. See [Special Types of Targets](Targets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsg4wugskiirceiskc).
  You can also invoke `xcodebuild` from
  shell scripts to automatically build one or more products.
- [Setting Command-Line Arguments and Environment Variables](Executable%20Environments.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrtg4wugsscizceeq2f) shows how to set environment variables that
  are available to your executable when running in the Xcode development
  environment.
- [Using Smart Groups to Organize Files](Organizing%20Xcode%20Projects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmruhawugsscjfceuske) describes
  how to use smart groups to organize the files of a large project.
- [Project Window Layouts](The%20Project%20Window.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytembufvbegskgi5aucsa) describes
  how to customize the configuration of the project window and other
  Xcode windows.
- [Customizing Key Equivalents](Customizing%20Key%20Equivalents.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgawueqkcjjdegsch) shows
  you how to set Command-key equivalents for menu items and keyboard
  equivalents for common editing tasks.
- [Using Scripts To Customize Xcode](Using%20Scripts%20To%20Customize%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgiwugskijfauuqkc) describes how to use shell commands and scripts
  to customize your programming environment.

[Next](Customizing%20Key%20Equivalents.md)[Previous](Remote%20Debugging%20in%20Xcode.md)

