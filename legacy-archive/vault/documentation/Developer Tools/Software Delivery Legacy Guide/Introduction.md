---
title: Software Delivery Legacy Guide
apple_id: TP40004615
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2010-09-15'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/SoftwareDistribution4/Introduction/Introduction.html
archived_at: '2026-07-15T07:26:54.719332Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Overview%20of%20Software%20Delivery.md)

# Introduction

This document describes the process of packaging and delivering a software product so that it can be installed on a user’s computer. The two major methods of delivering software are manual installs and managed installs.

A manual install is the preferred delivery solution because it offers the simplest install experience for small or compact products, such as a single application package. For example, to install an application, a user may drag the application package from a CD onto a folder of their choosing.

For more complex products, managed installs let you define every aspect of the install experience, including making sure the target computer meets specific requirements. Managed installs are generally used with products comprising several components to tailor the installation of each component depending on its kind. A managed install uses installer packages that define an install experience. When users open such packages, the Installer application guides them through the installation process and copies the product files to the appropriate locations on their file system.

Network administrators can use a type of managed install, a remote install, to install a product on several networked computers using Remote Desktop. No user interaction occurs in this type of install.

This document is meant to provide software delivery guidelines to product developers, product packagers, and network administrators.

- __Product developers__ create products or product components (such as applications, frameworks, plug-ins, and so on) using development tools such as Xcode.
- __Product packagers__ devise a delivery solution for an entire product.
- __Network administrators__ manage a group of networked computers and may need to install the same software on several computers remotely.

This document contains the following chapters and appendixes:

- [Overview of Software Delivery](Overview%20of%20Software%20Delivery.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqmznknltg) introduces the major software delivery mechanisms used in Mac OS X: manual installs and managed installs. It also explains remote installs, which network administrators use to install products on several computers on a network.
- [Product Containers](Product%20Containers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqnbnknlti) introduces general product delivery mechanisms that can be used in manual installs and managed installs. This chapter shows how to create a disk image for a standalone product. This chapter also shows how to create Internet-enabled disk images, which streamline manual installs. This chapter is especially useful to product packagers.
- [Manual Installs](Manual%20Installs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqnjnknlte) describes manual installs and provides an example of a simple product that should be installed manually. Product developers and packagers should read this chapter.
- [Managed Installs](Managed%20Installs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqnrnknltq) lists the major features managed installs provide, and explains when managed installs are appropriate. This chapter describes the three types of installation package and how they are processed by the Installer application. This chapter also describes the managed installation process and user experience. This information is useful to product packagers and network administrators.
- [Packaging Product Components](Packaging%20Product%20Components.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqnznknltc) explains how to create an installation package for a product component or a single-component product for a remote install.
- [Defining a Managed Install](Defining%20a%20Managed%20Install.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqojnknltc) explains how to create an install experience using a distribution package or a metapackage. Also shows how to create a hybrid metapackage. This information is useful to product packagers and network administrators.
- [Specifying Install Operations](Specifying%20Install%20Operations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqmjufvjvomi) explains how to define install operations for a managed install. This information is useful to product packagers and network administrators.
- [Performing Remote Installs](Performing%20Remote%20Installs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqobnknltg) provides an overview of remote installs and an example of one. This chapter is targeted to network administrators.
- [Specifying System and Volume Requirements in Pre-Tiger Systems](Specifying%20System%20and%20Volume%20Requirements%20in%20Pre-Tiger%20Systems.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqmjtfvjvomi) explains how to define installation requirements using executable files. This information is useful to product packagers and network administrators.
- [Prebinding Applications](Prebinding%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqmjrfvjvomi) explains when an application may benefit from having its prebinding information updated after a manual install. Product developers and packagers may find this information useful.
- [Preserving Resource Fork Data](Preserving%20Resource%20Fork%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqmjsfvjvomi) provides an overview of resource forks and explains how the PackageMaker and Installer applications handle payloads that include files with embedded resource forks instead of separate resource files. Product developers and packagers may find this information useful.

- _[File System Overview](../../Mac%20OSX/File%20System%20Overview/Introduction%20to%20the%20File%20System%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4dk2i)_ describes the Mac OS X file system and its domains. Knowledge of the Mac OS X directory hierarchy is paramount when packaging multicomponent products.
- _[Runtime Configuration Guidelines](../../Mac%20OSX/Runtime%20Configuration%20Guidelines/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3ta2i)_ explains the keys used in `Info.plist` files to specify some product properties, such as version and identifier. These properties are required when packaging products to create a managed install.
- _[Bundle Programming Guide](../../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_ describes Mac OS X bundles and file packages, which are used extensively in Mac OS X.
- _[Apple Remote Desktop Administrator's Guide Version 3.3](http://images.apple.com/server/docs/ARD_3_Admin_Guide_v3.3.pdf)_ explains how to use Remote Desktop to manage a set of networked computers.
[Next](Overview%20of%20Software%20Delivery.md)

