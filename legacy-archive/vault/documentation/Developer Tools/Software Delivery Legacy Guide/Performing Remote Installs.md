---
title: Software Delivery Legacy Guide
apple_id: TP40004615
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2010-09-15'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/SoftwareDistribution4/Remote_Installs/Remote_Installs.html
archived_at: '2026-07-15T07:26:58.732084Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Software Delivery Legacy Guide](Introduction.md)


[Next](Specifying%20System%20and%20Volume%20Requirements%20in%20Pre-Tiger%20Systems.md)[Previous](Specifying%20Install%20Operations.md)

# Performing Remote Installs

Apple Remote Desktop allows you to install products on multiple client computers from an administrator computer. This type of install is known as a _remote install_. You can perform remote installs immediately or schedule them for later completion.

Remote installs are based on managed installs (described in [Managed Installs](Managed%20Installs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqnrnknltq)). Therefore, the products to be installed on client computers must be packaged as component packages, metapackages, or distribution packages. If the product you want to install remotely is not packaged or if you want to repackage an existing product, you need to create a package for it first. See [Packaging Product Components](Packaging%20Product%20Components.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqnznknltc) and [Defining a Managed Install](Defining%20a%20Managed%20Install.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqojnknltc) to learn how to create packages.

Follow these steps to install a package on multiple clients from an administrator computer (see _[Apple Remote Desktop Administrator's Guide Version 3.3](http://images.apple.com/server/docs/ARD_3_Admin_Guide_v3.3.pdf)_ for more details):

1. In Remote Desktop, select the computers onto which you want to install the package.
2. Choose Manage > Install Packages.
3. In the Install Packages task window, add the packages you want to install to the package list.
4. Select an appropriate postinstallation process action. Figure 8-1 shows the definition of an Install Packages task.

   __Figure 8-1__  Remote Desktop Install Packages task

   !
5. Click Install.

Figure 8-2 shows the result of a successful remote install.

__Figure 8-2__  Successful Install Packages task in Remote Desktop

!!

When an install fails in any of the clients specified in and Install Packages task, you may need to copy the package to the client computer using a Remote Desktop Copy task and perform the installation by opening the package in Installer on the client.

[Next](Specifying%20System%20and%20Volume%20Requirements%20in%20Pre-Tiger%20Systems.md)[Previous](Specifying%20Install%20Operations.md)

