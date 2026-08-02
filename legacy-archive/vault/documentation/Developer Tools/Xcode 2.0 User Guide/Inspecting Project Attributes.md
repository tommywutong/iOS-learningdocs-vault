---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/pr_attributes/pr_attributes.html
archived_at: '2026-07-15T07:29:49.478845Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Finding%20Information%20in%20a%20Project.md)[Previous](Organizing%20Xcode%20Projects.md)

# Inspecting Project Attributes

Xcode tracks certain settings at the project-level.
These settings include your choice of version control system, the
version of Mac OS X to develop for, and the build styles available
in the project. You can view and modify project-level settings in
the project inspector.

To open the project inspector, you can either:

- Select the
  project in the Groups & Files list and click the Info or Inspector
  buttons, or choose the Get Info or Show Inspector items from the
  File menu, as described in [Inspector and Info Windows](The%20Project%20Window.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytembufvbegskgi5cesry).
- Choose Project > Edit Project Settings.

The project inspector contains the following panes:

- General.
  This pane, described below, contains options that let you control
  various project-level settings, such as the Source Control Management
  (SCM) system used by the project or the minimum version of Mac OS
  X the project is built to run on.
- Styles. This pane contains all of the build styles defined
  for your project. A build style is a collection of build settings
  that are applied to one or more targets when you build; this allows
  you to vary the way in which a target is built. In the Styles pane,
  you can add, edit, and delete build styles. Build styles are described
  further in [Build Styles](Build%20Styles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrtgawugssbizcesr2g).
- Comments. This pane lets you associate notes and other text
  with the project. The Comments pane is described further in [Adding Comments to Project Items](Organizing%20Xcode%20Projects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmruhawueq2jjfcukq2d).

__Figure 7-1__  The
project inspector

!

The General pane of the project inspector, shown here, contains
the following information:

1. The name
   of the project, set when you first create the project using Xcode’s
   project templates.
2. The location of the project folder in the filesystem.
3. The location at which the build products and intermediate
   files for the project’s targets are placed. The options under
   the heading “Place Build Products In” specify the location where
   Xcode places the products created when building the project’s
   targets. The options listed under “Place Intermediate Build Files
   In” specify where files generated in the course of building the
   product, but not included in the final product, are placed. See [Build Locations](Building%20a%20Product.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqmztfvbecssdjfeugqy) for more information.
4. The cross-development options let you choose the minimum version
   of Mac OS X to build your product for. This lets you target versions
   of the operating system other than the one you are currently developing
   on. Use the Cross-Develop Using Target SDK pop-up menu to specify
   which SDK to use. See [Using Cross-Development in Xcode](Using%20Cross-Development%20in%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrtguwuiqkgizcesq2j) for
   more information.
5. The source control management (SCM) system to use with the
   project. You specify an SCM system at the project level. In the
   General pane of the inspector, you can turn SCM on and off, as well
   as choose the particular SCM system to use with the project. See [Configuring Repository Access](Managing%20Projects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwhewueq2jindeirkf) for
   more information.
6. The Rebuild Code Sense Index button lets you rebuild the symbolic
   index that Code Sense, described in [Code Sense](Finding%20Information%20in%20a%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrvgawueqsdjjeugrsc), uses
   to provides features such as code completion and symbol definition
   searches.

[Next](Finding%20Information%20in%20a%20Project.md)[Previous](Organizing%20Xcode%20Projects.md)

