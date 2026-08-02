---
title: Software Delivery Legacy Guide
apple_id: TP40004615
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2010-09-15'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/SoftwareDistribution4/Managed_Installs/Managed_Installs.html
archived_at: '2026-07-15T07:26:57.898726Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Software Delivery Legacy Guide](Introduction.md)


[Next](Packaging%20Product%20Components.md)[Previous](Manual%20Installs.md)

# Managed Installs

As described in [Overview of Software Delivery](Overview%20of%20Software%20Delivery.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqmznknltg), _managed installs_ give you more control over the installation process, which, among other things, allows you to fine-tune the user’s install experience. However, when your product is made up of a single component that doesn’t need to be placed at privileged locations in the file system, such as `/Applications` or `/Library`, you should provide users with a manual install for your product. Manual installs are faster and easier to perform for novice and expert users alike. See [Manual Installs](Manual%20Installs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqnjnknlte) for details.

Multicomponent products benefit from managed installs because you can specify how each of a product’s components is installed. Also, remote installs—which allow you to install products remotely on several computers on a network—are based on managed installs. For more information on remote installs, see [Performing Remote Installs](Performing%20Remote%20Installs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqobnknltg).

Managed installs provide these features:

- An automated install experience for multicomponent products
- Support for upgrading your product, which may require replacing only certain components
- Support for custom installs, which allow users to decide what components to install and where to install them

On a more detailed level, managed installs provide fine control over the installation process, including:

- The ability to perform operations before installing, such as:

  - Making sure the target system meets specific criteria
  - Requiring administrative-user authentication before installing components at privileged locations
  - Performing install operations, such as quitting an application to be upgraded or launching daemons (faceless applications)
- Control over details such as whether an install:

  - Allows the user to specify an alternate installation destination
  - Recommends or requires restart, logout, or shutdown after completion
  - Uses the ownership and access permissions of the user installing the product or those specified in the installation package

There are three ways of defining a managed install:

- __Distribution packages__ let you define the complete install experience of your product. They also provide you with a great deal of flexibility for defining the install choices users use to customize an install. Distribution packages offer you and the users of your product the best installation solution for Mac OS X–based products. Distribution packages, however, can be installed only on computers running Mac OS X v10.4 and later.
- __Metapackages__ provide some of the features distribution packages provide but can be installed on computers running Mac OS X v10.2 and later.
- __Component packages__ contain a single product component. They are usually included as part of a distribution package or metapackage but can also be installed individually in computers running Mac OS X v10.2 and later.

The following sections describe the major elements of managed installs and some of their limitations.

The central part of a managed install is the _installation package_, which contains your product and installation information. The following sections describe installation packages and the various types of packages you may need to create when developing a managed install for a product.

An _installation package_ (also known as a package) is a file package (a directory that appears in the Finder as a single file) created using the PackageMaker application (`/Developer/Applications/Utilities`). Packages contain a product or product component—the package’s _payload_—to be installed on a computer, and install configuration information that determines where and how the product is installed.

Packages have the extension `.pkg` or `.mpkg`. When a user double-clicks a package in a Finder window, the Installer application opens the package and walks the user through the installation process.

A package can specify details about four aspects of the package itself and its payload:

- __Product information:__

  - Title
  - Description
  - Welcome file
  - Read Me file
  - License file
  - Conclusion file
- _Package properties:_

  - Package identifier
  - Package version number
  - Resource fork processing
- __Installation properties:__

  - System requirements
  - Volume requirements
  - Authentication requirement
  - Allowance for choosing an installation volume other than the boot volume
  - Installation destination on the installation volume
  - Relocation consent (the ability user may have to change the installation destination)
  - Revert consent
  - Directory-permissions overwrite
  - Postinstallation process action
- __Install operations:__

  - Preflight
  - Preinstall/Preupgrade
  - Postinstall/Postupgrade
  - Postflight

A complex product, such as the Levon product introduced in [Overview of Software Delivery](Overview%20of%20Software%20Delivery.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqmznknltg), is made up of distinct components. Except for single-component products, _component packages_ are used in conjunction with metapackages or distribution packages (described later in this chapter) to create an install experience. Specifically, component packages:

- Are the basis for the mechanism that allows you to provide users a way to specify which components to install (for example, a user may not want to install a product’s tutorial files)
- Let you identify required components (which must be installed) and specify the locations of components to be installed at specific locations on the installation volume
- Allow you to specify system and volume requirements for the component using executable files (see [Specifying System and Volume Requirements in Pre-Tiger Systems](Specifying%20System%20and%20Volume%20Requirements%20in%20Pre-Tiger%20Systems.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqmjtfvjvomi))

Component packages have the extension `.pkg`. Each component package contains a single product component and specifies product information, package properties, installation properties, and install operations.

Component packages can be installed on their own or as part of the install of a multicomponent product. After the payload of a component package is installed, Installer places a receipt in the `/Library/Receipts` directory of the installation volume. An _installation receipt_ is a token that Installer uses to determine whether a package has already been installed on a system. As long as the receipt is present, subsequent installs of packages using the same package filename on the same volume are processed as upgrades.

A _metapackage_ is an installation package that contains other installation packages. The enclosed packages can be component packages or metapackages (but not distribution packages).

Metapackages allow you to define a simple install experience for a multicomponent product. When users open a metapackage with the Installer application, they can choose to install only the components they need. Each enclosed package becomes an _install choice_. For example, if a product includes a tutorial-files component that the user performing the install doesn’t need, they can choose not to install that component.

Metapackages have the extension `.mpkg`. Table 4-1 shows what aspects of a metapackage and the packages (component packages and other metapackages) it contains are used in the installation process.

__Table 4-1__  Installation process of a metapackage

|  | Product information | Package properties | Installation properties | Install operations |
| Metapackage | ../art/active_check.jpg | ../art/inactive_check.jpg | ../art/inactive_check.jpg | ../art/inactive_check.jpg |
| Contained packages | ../art/inactive_check.jpg | ../art/active_check.jpg | ../art/active_check.jpg | ../art/active_check.jpg |

Table 4-1 indicates that the containing metapackage specifies package properties, installation properties, and specify install operations. However, the only aspect of the metapackage used in the installation process is its product information. Conversely, for the packages the metapackage contains, all aspects except product information are used in the installation process.

A _distribution package_ is a metapackage that specifies both product and installation information for a product. Distribution packages provide more sophisticated facilities to tailor the installation process. The major features distribution packages provide are:

- Definition of the entire install experience in one place instead of having it spread out through several component packages
- Definition of system and volume requirements using a requirements editor instead of executables
- Install choices can contain more than one component package
- Users can choose an installation destination for each install choice instead of for the entire install
- Installer loads a distribution package for a multicomponent product with many component packages (and presents the user with the install experience it specifies) faster than a metapackage containing the same product

The central part of a distribution package is the _distribution script_. This is a JavaScript-based script file that contains all the information that defines an install experience. When you create a distribution package using PackageMaker, the package’s distribution script is created for you.

Distribution packages differ from metapackages in these areas:

- They can be installed only on computers running Mac OS X v10.4 (Tiger) and later.
- They must contain only component packages, not metapackages or distribution packages.
- Installer ignores installation properties specified in the contained component packages (installation properties are specified by the distribution script).

Table 4-2 shows what aspects of a distribution package and the component packages it contains are used in the installation process.

__Table 4-2__  Installation process of a distribution package

|  | Product information | Package properties | Installation properties | Install operations |
| Distribution package | ../art/active_check.jpg |  | ../art/active_check.jpg |  |
| Contained packages | ../art/inactive_check.jpg | ../art/active_check.jpg | ../art/inactive_check.jpg | ../art/active_check.jpg |

Table 4-2 indicates that a distribution package specifies only product information and installation properties, and both aspects are used in the installation process. The contained packages may specify all package aspects, but only their package properties and install operations contribute to the installation process.

Two of the installation properties you can specify in a package are system requirements and volume requirements. These two properties define criteria the installation host must meet in order for the installation process to proceed.

- __System requirements__ specify criteria the computer or operating system must satisfy. There are two types of system requirements: recommended and required. If the host doesn’t meet a required system requirement, the installation process is canceled.
- __Volume requirements__ specify criteria each of the host’s volumes must meet in order to be considered a valid installation volume.

After the Installer application opens a package, it performs the installation process in several phases:

- __Requirements Check__

  Installer ensures that the installation host meets the system and volume requirements specified by the package.
- __Preinstall__

  Installer runs `preflight` and `preinstall`/`preupgrade` executables. If an executable returns anything other than `0`, the install is cancelled.
- __Install__

  Installer extracts the payload of component packages and copies it to the appropriate destinations.
- __Save Receipt__

  Installer copies the component package file (with its payload stripped) to the `Library/Receipts` directory in the installation volume.
- __Postinstall__

  Installer runs `postinstall`/`postupgrade` and `postflight` executables.

The following sections detail the operations that the Installer application performs in the Requirements Check, Preinstall, and Postinstall phases of the installation process for the three types of installation package files. For details on the purpose of the executable files used to define installation requirements and install operations (`InstallationCheck`, `VolumeCheck`, `preflight`, `preinstall`, `preupgrade`, `postinstall`, `postupgrade`, and `postflight`), see [Specifying Install Operations](Specifying%20Install%20Operations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqmjufvjvomi) and [Specifying System and Volume Requirements in Pre-Tiger Systems](Specifying%20System%20and%20Volume%20Requirements%20in%20Pre-Tiger%20Systems.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqmjtfvjvomi).

This is how Installer performs the Requirements Check, Preinstall, and Postinstall phases of a component package’s installation process:

- __Requirements Check__

  `InstallationCheck`

  `VolumeCheck` on each available volume
- __Preinstall__

  `preflight`

  `preinstall` or `preupgrade`
- __Postinstall__

  `postinstall` or `postupgrade`

  `postflight`

This is how the Installer application performs the Requirements Check, Preinstall, and Postinstall phases of a metapackage’s installation process:

- __Requirements Check__

  `InstallationCheck` for each package but not the top metapackage

  `VolumeCheck` on each available volume for each package but not the top metapackage
- __Preinstall__

  `preflight` for top metapackage

  `preflight` for each package

  `preinstall` or `preupgrade` for top metapackage

  `preinstall` or `preupgrade` for each package
- __Postinstall__

  `postinstall` or `postupgrade` for each package

  `postinstall` or `postupgrade` for top metapackage

  `postflight` for top metapackage

  `postflight` for each package

This is how the Installer application performs the Requirements Check, Preinstall, and Postinstall phases of a distribution package’s installation process:

- __Requirements Check__

  Installation Check script

  Volume Check script on each available volume
- __Preinstall__

  `preflight` for each package

  `preinstall` or `preupgrade` for each package
- __Postinstall__

  `postinstall` or `postupgrade` for each package

  `postflight` for each package

The install experience that the Installer application shows users after they open an installation package has the following phases:

- __System Requirements__

  The first task Installer performs after opening a package is to ensure that the installation host meets the package’s installation requirements. Unsatisfied nonfatal system requirements produce a warning in user-driven installs.
- __Authentication__

  When a package requires admin or `root` user authentication, Installer displays the Authentication dialog. Users must enter the user name and password of an administrative user on the system to perform the install.
- __Welcome__

  Installer always displays the Welcome page. To tailor the Welcome page, include a welcome file in the package.
- __Read Me__

  If the package includes a Read Me file, Installer displays it in the Read Me page. The user can save or print this file.
- __License__

  If the package includes a license agreement file, Installer displays it in the License page. The user must accept the license in order to continue the installation process.
- __Volume Requirements__

  Installer checks each available volume to determine whether it meets the package’s volume requirements. It uses the information gathered in this phase in the Volume Selection phase.
- __Volume Selection__

  Installer displays the Select Destination page if the package contains at least one package.
- __Customization__

  If the package allows both an easy install and a custom install, Installer displays the Installation Type page, which defaults to the easy install. The user can choose to perform the easy install or the custom install.
- __Install__

  When the user clicks Install (and after admin or `root` user authentication, if needed), Installer shows the Install page and performs the install.
- __Conclusion__

  Installer shows the Conclusion page when the installation process ends. In distribution packages, you can include a conclusion file that Installer shows instead of the default conclusion message.

After an installation process is complete, the Installer application can recommend or mandate that the user log out of the system or restart or shut down the computer, depending on the most drastic postinstallation process action specified in the installation package. When specifying a package’s postinstallation process action, you must take into account the nature of your product and the way it interacts with Mac OS X and other executables in the system.

There are some issues and limitations of managed installs:

- The Installer application does not support uninstalling products.
- Installer runs only on Mac OS X.
- Without proper care when specifying the ownership and access permissions of component files, it is possible to render a system unusable. Make sure you test all installer packages before shipping them to customers.
- Relocation does not work in installation hosts running Mac OS X v10.3.3 or earlier.

[Next](Packaging%20Product%20Components.md)[Previous](Manual%20Installs.md)

