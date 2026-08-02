---
title: Xcode Profile Guided Optimization
apple_id: TP40014459
resource_type: Guide
platform: watchOS|Xcode Developer Tools
topic: Xcode
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/xcode_profile_guided_optimization/pgo-tasks/pgo-tasks.html
archived_at: '2026-07-15T07:30:56.140487Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Profile Guided Optimization](About%20Profile%20Guided%20Optimization.md)


[Next](Using%20Profile%20Guided%20Optimization.md)[Previous](About%20Profile%20Guided%20Optimization.md)

# Quick Start

Profile Guided Optimization (PGO) is a high-performance optimization tool that is easy to set up and use. In this chapter, you’ll see all the steps needed to use PGO.

To start using PGO, choose Product > Perform Action > Generate Optimization Profile. You are given the choice to run the app, exercising it manually, or to run your tests to exercise it.

![../art/pgo-generate-1_2x.png](attachments/art/pgo-generate-1_2x.png)

When you click the Run button, Xcode confirms that you want to configure the app target.

![../art/pgo-confirm_2x.png](attachments/art/pgo-confirm_2x.png)

After you click the Enable button, Xcode builds and runs the app according to the selection you made for running it.

If you chose to collect the optimization profile by running the app manually, be sure to exercise all the performance-sensitive operations when the app runs. When you are finished, click the Xcode Stop button in the workspace toolbar to write the profile.

![../art/pgo-stop_button.png](attachments/art/pgo-stop_button.png)

If you chose to collect the profile by running your test suite, before you click the Enable button you should first edit the current scheme to select which tests to run. Tests for correctness often focus on checking the unusual conditions and error handling, and those are rarely the things that you want to optimize for best performance. Be sure that your tests, both functional and performance measurement tests, cover the full range of behavior that is important for the performance of your app.

Xcode configures the app target for you when you use the Generate Optimization Profile command. The target configuration settings can be seen in the project editor by selecting your app target and clicking Build Settings.

The PGO defaults are to set Use Optimization Profile to be Yes for Release builds and No for Debug builds.

![../art/pgo-buildsetting-codegen_2x.png](attachments/art/pgo-buildsetting-codegen_2x.png)

The optimization profile is a file with extension `.profdata`. Xcode writes the `.profdata` file in the location specified by the Optimization Profile File build setting in your project, by default in a folder named `OptimizationProfiles` that is added to your project. The folder and file appears in the project navigator as shown in this example:

![../art/pgo-projnav-prodatafile_2x.png](attachments/art/pgo-projnav-prodatafile_2x.png)

As you continue to develop and change code in your app project, the optimization profile becomes out of date. The LLVM compiler recognizes when the profile is no longer a good match to your app’s current state and provides you with a warning. When you receive this warning, you can use the Generate Optimization Profile command again to create an updated profile. Each time you regenerate the optimization profile, Xcode replaces the existing profile data.

[Next](Using%20Profile%20Guided%20Optimization.md)[Previous](About%20Profile%20Guided%20Optimization.md)

