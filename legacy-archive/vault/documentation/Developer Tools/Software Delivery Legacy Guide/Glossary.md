---
title: Software Delivery Legacy Guide
apple_id: TP40004615
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2010-09-15'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/SoftwareDistribution4/Glossary/Glossary.html
archived_at: '2026-07-15T07:26:54.703687Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Software Delivery Legacy Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Preserving%20Resource%20Fork%20Data.md)

# Glossary

- __application package__

  A file package containing the code and other resources that make up a Mac OS X application. Application packages make it easy for users to move applications around their file systems.

- __bundle__

  A structured directory hierarchy that stores files in a way that facilitates their retrieval. Bundles are used extensively in Mac OS X; in particular most application executables are enclosed in bundles together with the resources the application needs to operate.

- __container__

  A file-based enclosure for a product that facilitates delivery to its users. Disk images installation packages, and ZIP archives are the most popular product containers.

- __component__

  A part of a software product that resides at a distinct location on the file system. See also [component package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqmjvfvjvomy).

- __component package__

  An installation package whose payload is one of the components of a product.

- __custom install__

  A metapackage or distribution package install that a user performs after modifying the default option selection.

- __delivery vehicle__

  Transport used by users of a product to obtain the product’s files. These include optical media and the Internet.

- __disk image__

  A file-based enclosure that facilitates the transport of a directory structure on the Internet. Disk images can also be compressed to allow a product’s files to be placed on optical media.

- __distribution package__

  A metapackage that contains a distribution script that specifies the install experience for a product. Distribution packages provide a streamlined packaging experience for developers and an enhanced install experience for users. See also [distribution script](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqmjvfvjvony);[metapackage](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqmjvfvjvomi).

- __distribution script__

  An XML file with the extension `.dist` that contains all the information that defines an install experience in a distribution package. See also [distribution package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqmjvfvjvomq).

- __easy install__

  A metapackage or distribution package install that a user performs using the default option selection.

- __file package__

  A directory (often a bundle) that appears as a single file in Finder windows. See also [bundle](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqmjvfvjvona); [file package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqmjvfvjvoni).

- __hybrid metapackage__

  A metapackage that contains a distribution script. This type of installer package behaves as a distribution package when installed on computers running Mac OS X v10.4 and later. On computers running earlier versions of the operating system, a hybrid metapackage behaves as a regular metapackage. See also [metapackage](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqmjvfvjvomi); [distribution package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqmjvfvjvomq).

- __install choice__

  An option users can select or deselect as part of the installation process to specify whether a product component is to be installed.

- __install experience__

  The tasks a user needs to perform in order to install a product on their computer.

- __installation host__

  The computer onto which a package is to be installed.

- __install operation__

  Installation activity performed by an executable file that is invoked at a specific point during the installation process.

- __install operation executable__

  An executable file that is invoked by Installer during an install, before or after copying a package’s payload to the installation destination.

- __installation destination__

  The directory in which Installer places a package’s payload.

- __installation package__

  A file package with the `.pkg` or `.mpkg` extension. Installation packages (also known as packages) contain products or product components (known as the package’s payload) and installation information used by the Installer application and Remote Desktop to place product files on a file system.

- __installation property__

  Information in an installation package that specifies an installation requirement or an installation process detail, such as whether relocation is allowed.

- __installation receipt__

  A token that Installer uses to determine whether a component has already been installed on an installation volume.

- __installation requirement__

  A condition that the target computer or volume of an installation must meet in order for the install to take place. The two types of installation requirements are system requirements and volume requirements.

- __installation volume__

  The volume (or mountpoint) onto which an installation package is to be installed.

- __managed install__

  An Installer-driven installation process. Users open an installer package in the Installer application, which performs all install tasks.

- __manual install__

  A user-driven installation process. Users drag a product’s files to a location of their choosing in their file system.

- __metapackage__

  Installation package that contains other installation packages, usually component packages. Metapackages are used to deliver multicomponent products to users and to provide them with install choices that allow them to choose which components to install. See also [component package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqmjvfvjvomy).

- __package properties__

  Installer package data that provides Installer details about the package itself, such as its identifier, version number, and resource fork processing.

- __payload__

  The product or product components contained in an installation package. See also [installation package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqmjvfvjvonq).

- __product container__

  A file that contains a packaged or unpackaged product. The two container types are disk image and ZIP archive.

- __relocation__

  The ability of users to change the installation location of a package before an install.

- __remote install__

  A network administrator–driven installation process. An administrator uses Apple Remote Desktop to install a package onto a set of client computers.

- __system requirement__

  A condition that must be met by the computer (and associated operating system) in order for the install to proceed.

- __volume requirement__

  A condition that must be met by a volume in order qualify as a possible installation volume.

[Next](Document%20Revision%20History.md)[Previous](Preserving%20Resource%20Fork%20Data.md)

