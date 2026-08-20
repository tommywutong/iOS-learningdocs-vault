---
title: PackageMaker User Guide
apple_id: TP40005371
resource_type: Guide
platform: Xcode Developer Tools
topic: Languages & Utilities
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/PackageMakerUserGuide/Glossary/Glossary.html
archived_at: '2026-07-15T07:25:20.312972Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [PackageMaker User Guide](Introduction%20to%20PackageMaker%20User%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Packaging%20Workflow.md)

# Glossary

- __choice requirement__

  A test that compares the value of a system property (such as the amount of random-access memory available) with a value. Choice requirements determine the value of a choice’s user-interface properties: selected, actionable, and visible.

- __choice requirement editor__

  Area of a PackageMaker project window that allows packagers to specify a choice requirement (and how it affects the value of the choice’s user-interface properties). See also [choice requirement](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzrfvbuqmjqgays2u2xgy).

- __component package__

  Installer package that contains a single software component as its payload. See also, [product package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzrfvbuqmjqgays2u2xgq).

- __component package editor__

  Area of a PackageMaker project window that specifies packaging and installation information about a product component. This editor is displayed when a component is selected in the Contents pane in the project window.

- __downgradable component__

  A product component, such as an application binary or a plug-in, that can be replaced with an earlier version in an install process.

- __finalization action__

  An action required after a completed installation process. The possible finalization actions are log-out, restart, and shutdown.

- __install choice__

  An option users can select or deselect during the installation process to specify whether a product component is to be installed

- __install customization pane__

  A pane users see while interacting with the Installer application if the package being installed allows the user to customize the install by choosing the product components to be installed. See also, [product package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzrfvbuqmjqgays2u2xgq), [product component](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzrfvbuqmjqgays2u2xgu).

- __install operation__

  An install-time operation performed by an executable file that is invoked at the beginning or at the end of the install. The two install operations supported in OS X v10.5 are preinstall and postinstall.

- __installation action__

  A task to be performed before or after an install. PackageMaker defines several installation actions, including Quit Application and Show File in Finder.

- __installation package__

  A file package with the `pkg` or `mpkg` extension. Installation packages contain a payload and installation information used by the Installer or Remote Desktop applications to identify the payload’s parts and generate an install experience for the user.

- __Installer package database__

  System-level database of all the installation packages installed by the Installer application.

- __managed install__

  An Installer application–driven installation process. Users open an installer package in Installer, which then guides them through the installation process.

- __manual install__

  An user-driven installation process. In this software-installation method, users drag a product’s files to a location of their choosing in their computer’s file system. See also [managed install](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzrfvbuqmjqgays2u2xg4).

- __package identifier__

  Identifies the package within the Installer package database. See also [Installer package database](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzrfvbuqmjqgays2u2xge).

- __package list__

  A pane in a PackageMaker project window that lists the packages the project defines. This list is divided in two parts: the installation-package file (which contains all the product’s files) and the subpackages or package references that contain components of the product.

- __package requirement__

  A test that determines whether a package can be installed on the computer. A package requirement can be optional; such requirements display a warning to the user but allows the install to proceed. Non-optional requirements prevent an install from taking place.

- __package version number__

  Positive integer that identifies an iteration of a single-component product package, or an iteration of a component package within a product package. This version number should be incremented when the contents or installation details of the package are changed. See also [product package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzrfvbuqmjqgays2u2xgq) [component package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzrfvbuqmjqgays2u2xha).

- __payload__

  The product or product components contained in an installation package. See also [installation package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzrfvbuqmjqgays2u2xgm).

- __product component__

  Self-contained part of a product. A product can have one or more components. The OS X file system contains special locations for several types of components. For example, application binaries are placed in `Application` directories, plug-ins are housed in `Plugin` directories, fonts live in `Fonts` directories, and so on.

- __product package__

  Installation package that contains all the components of a product. Product packages with multicomponent products contain or reference component packages. See also [installation package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzrfvbuqmjqgays2u2xgm).

- __product package editor__

  A pane in a PackageMaker project window that specifies packaging and installation information about a product. This pane is displayed when the product package is selected in the [package list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzrfvbuqmjqgays2u2xhe).

- __provider identifier__

  Identifier for the entity responsible for the contents of an installation package; for example, `com.apple`. PackageMaker uses this identifier to generate default package identifiers for a product package’s components. See also [package identifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzrfvbuqmjqgays2u2xgi).

- __relocatable component__

  A product component, such as an application binary or a plug-in, that the user may move after it has been installed.

- __target OS version__

  The earliest release of OS X in which the installation package is to be installed. The package is installable on the specified release and later. For example, a package whose target OS is OS X v10.4 can be installed on computers running OS X v10.4 and later releases.

- __volume requirement__

  A test that compares the value of a volume property (such as free space) with a value. Volume requirements determine whether the user can choose a particular volume as the destination volume of a product package.

[Next](Document%20Revision%20History.md)[Previous](Packaging%20Workflow.md)

