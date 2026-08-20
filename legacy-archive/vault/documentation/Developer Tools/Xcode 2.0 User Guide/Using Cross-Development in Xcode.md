---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/bs_cross_development/bs_cross_development.html
archived_at: '2026-07-15T07:29:03.181590Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Debugging.md)[Previous](Optimizing%20the%20Edit-Build-Debug%20Cycle.md)

# Using Cross-Development in Xcode

Using Xcode, you can develop software that
can be deployed on, and take advantage of features from, different
versions of Mac OS X, including versions different from the one you
are developing on.

When you install the developer tools shipped with Mac OS X
v10.3, you can also install SDKs, or Software Development Kits,
which are complete sets of header files and stub libraries as shipped
in previous versions of Mac OS X. In order to take advantage of
cross-development, you must install the SDKs for the OS versions
you plan on targeting. You then specify which version (or SDK) of
Mac OS X headers and libraries to build with. You can also specify
the earliest Mac OS X system version on which the software will
run.

In some cases, Apple may seed an SDK for an upcoming version
of the operating system, allowing you to prepare your application
to work with future versions of the Mac OS before they have been
released to the general public.

To set up your Xcode project for cross-development, take the
following steps:

1. Choose an
   SDK to develop for. Select your project in the Groups & Files
   list and open an Info window. In the General pane, choose the SDK—for
   example, Mac OS X version 10.2.7—from the “Cross-Develop Using Target
   SDK” pop-up menu. When you choose an SDK, Xcode builds targets
   in your project against the set of headers corresponding to the
   specified version of Mac OS X, and links against the stub libraries
   in that SDK. This allows you to build products on your development
   machine that can be run on the system targeted by the SDK. Your
   software can use features available in system versions up to and
   including the one you select. The default value is to build for
   the current operating system.

   You can also type a path directly
   in the text field or click the Choose button to select an SDK other
   than a Mac OS X SDK, or to choose a Mac OS X SDK that is stored
   in a nonstandard location.
2. Choose a deployment version of the Mac OS. If your software
   must run on a range of operating system versions, choose a Mac OS
   X deployment operating system for each individual target that requires
   one. The deployment operating system identifies the earliest system
   version on which the software can run. By default, this is set
   to the version of Mac OS X corresponding to the SDK version. If
   no SDK is specified and the Mac OS X Deployment Target build setting
   is not set, the compiler targets Mac OS X version 10.1 by default.

   To
   set the deployment version for a target, select the target in the
   Groups & Files list and open an Info window. Click Build to
   open the Build pane.

   Find the Mac OS X Deployment Target
   setting and choose a deployment operating system from the pop-up
   menu in the “Value” column. If this build setting is not visible, select
   Deployment from the Collections menu.
3. For each target, supply a prefix file that takes into account
   the selected SDK. To use an umbrella framework header from an SDK
   as your prefix file, add the appropriate `#include
   <Framework/Framework.h>` directive to
   your target's prefix file, instead of setting a Prefix Header path
   to the umbrella framework header directly.

There is a lot more to successfully developing software for
multiple versions of the Mac OS. For more information see _Cross
Development_ in Tools Documentation.

[Next](Debugging.md)[Previous](Optimizing%20the%20Edit-Build-Debug%20Cycle.md)

