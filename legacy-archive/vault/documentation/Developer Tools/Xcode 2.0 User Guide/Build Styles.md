---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/bs_build_styles/bs_build_styles.html
archived_at: '2026-07-15T07:29:00.301964Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Building%20a%20Product.md)[Previous](Build%20Settings.md)

# Build Styles

A build style is a variation on a target that
allows you to override some of the build settings in a target without
creating a whole new target. While a target contains a list of files,
build rules, build phases, and build settings, a build style contains
only build settings. You can apply the same build style to all targets
in your project. Build styles are a flexible tool for quickly “tweaking”
your product or for saving different groups of build settings to
apply to a target depending on the current circumstances.

This article provides a general explanation of build styles,
describes the predefined build styles you get when you create an
Xcode project, and explains how to define your own build styles.

Build styles allow you to build two or more “flavors”
or styles of a product without having to change build settings in
the target or create separate targets for each product flavor. When
you perform a build, the build settings defined in a build style
modify or add to the group of build settings defined in the targets
being built.

A common use of build styles is to build a given target differently
to create development and deployment versions of a product. There
are a handful of build settings—for example, optimization settings
for the compiler—whose values are different, depending upon whether
you are building a product for development purposes or to deploy
to customers. In each situation, the target you build is identical
in every other way—files, build phases, and build rules—because
the product you want to generate for each is essentially the same. The
only difference is in how the source files of the target are processed
to build that product, the “style,” if you will, in which the
target is built.

If you were to create two targets—one for debugging and
one for the final build—you would have to remember to keep both
targets in sync. When you added a file to one target, you would
have to remember to add it to the other, and so forth. With a build
style, only the build settings defined in the build style are overridden.
A build style does not override a target’s build phases or build
rules. It is much simpler to create build styles containing the
build settings whose values you wish to change and then build with
the appropriate build style.

Build styles are defined and used on a per-project basis.
When you initiate a build, Xcode builds the active target, and any
targets it depends on, with the active build style. Whatever build
settings the active build style contains override any values assigned
to those build settings in the target. See [Build Settings](Build%20Settings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshewueqkdjfdecrch) for
details.

New Xcode projects contain two predefined build styles, Development
and Deployment. You can edit those build styles or define new build
styles of your own.

In addition to the Development and Deployment build styles
present in all project types in Xcode, you may need to add a special
build style to satisfy particular needs, such as configuring an
environment to measure the performance of your application. In such
a build style you may add build settings that include the addition
of a library or framework that gathers and logs performance-related
information. You may also need to target your application to specific
Mac OS X versions. In that case, you may need to build your application
slightly differently for each version. For example, you can have
build styles named Mac OS X 10.2 and a Mac OS X 10.3 that build
a product tailored for Mac OS X version 10.2 and Mac OS X version
10.3, respectively, by setting Mac OS X Deployment target (MACOSX_DEPLOYMENT_TARGET),
and any other build settings necessary, to the appropriate values.

A development build of a product may include debugging information
to assist you in fixing bugs. However, this extra information can
consume valuable space in a user’s system. A deployment build
should contain only the code necessary to run the application.

Some build settings tell Xcode to add debugging information
to an executable or specify whether to optimize its execution speed.
Other build settings turn on features such as ZeroLink and Fix and
Continue, which are useful only during development.

All Xcode project templates include two build styles, the
Development build style and the Deployment build style. By default,
the Development build style turns on ZeroLink, Fix and Continue,
and debug-symbol generation, among others, while turning off code optimization.
The Deployment build style turns off ZeroLink and Fix and Continue.
The code-optimization level is set to its highest by default, through
the Optimization Level (GCC_OPTIMIZATION_LEVEL) build setting. Note
that the Deployment build style doesn’t turn on Deployment Location
(DEPLOYMENT_LOCATION); therefore, the product is not copied to the
location where it would be installed on a user’s system. It also doesn’t
turn on Deployment Postprocessing (DEPLOYMENT_POSTPROCESSING), which
specifies whether to strip binaries and whether to set their permissions
to standard values.

For more information on building products for deployment,
see [Building From the Command Line](Building%20a%20Product.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqmztfvbecssejbcukry).

Generally, the two default build styles are enough for most
people. You can use them as they are or add additional build settings
to them. For example, you can specify that the Development build
style display more compiler warnings.

If you’re thinking of creating a new target, consider whether
it might be best to create a new build style instead. In general,
create a new target to create a new product, and create a new build
style to modify how a target is built. If you’re creating targets
that differ only in their build settings, consider creating one
target and several build styles. If you need to create targets that
differ in other ways—such as build phases or information property
list entries—you need to create separate targets for each.

To view the build styles in your project, select your project,
open an Info window. and click Styles to open the Styles pane, shown in Figure 26-1.
You can also choose Project > Edit Active Build Style to open
the Styles pane of the project inspector and select the active build
style.

__Figure 26-1__  The Styles pane

!

The build styles defined in your project are listed in the Build
Style pop-up menu at the top of the Styles pane. To view the contents
of a build style, select it from this menu. You can see the build
settings defined in the build style and their specifications in
the table below the Build Style menu.

The _active build style_ is the build style
applied to the active target, and to any targets it depends upon,
when you build a project. Choose Project > Set Active Build Style
or use the Active Build Style toolbar item in the Build Results
window to change the active build style. You can also customize
the project window toolbar to include the Active Build Style item; this
allows you to change the active build style directly from the project
window. To customize the toolbar, choose View > Customize Toolbar
and drag the Active Build Style item to the toolbar.

Although the Development and Deployment build styles are sufficient
in most cases, you may find that you wish to create your own build
style. You can add and remove build styles from your project in
the Styles pane of the inspector window. To create a new build style
choose New Build Style from the Build Style pop-up menu. You can
duplicate existing build styles as well.

To remove a build style from your project:

- Choose Edit
  Build Styles from the Build Style pop-up menu.
- Select the build style you want to remove in the resulting
  dialog and click the Delete button.

You can modify the value of a build setting in a build style
in the same way that you change the value of a build setting in
a target, described in [Editing Build Setting Specifications](Build%20Settings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrshewugsscijcemr2e).

To add a new build setting to the build style, click the plus
(+) symbol in the lower left corner of the build settings table.
Double-click in the Setting column and type the name of the build
setting, then double-click in the Value column and type the value.

To delete a build setting from a build style, select that build setting
in the build settings table and click the minus sign (-) in the
lower-left corner.

[Next](Building%20a%20Product.md)[Previous](Build%20Settings.md)

