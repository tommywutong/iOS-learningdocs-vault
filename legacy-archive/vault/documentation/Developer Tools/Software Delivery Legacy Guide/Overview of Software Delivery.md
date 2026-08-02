---
title: Software Delivery Legacy Guide
apple_id: TP40004615
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2010-09-15'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/SoftwareDistribution4/Overview/Overview.html
archived_at: '2026-07-15T07:26:58.721598Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Software Delivery Legacy Guide](Introduction.md)


[Next](Product%20Containers.md)[Previous](Introduction.md)

# Overview of Software Delivery

Mac OS X provides several mechanisms you can use to deliver a software product to your customers. These mechanisms are both flexible and easy to develop. They support the delivery of simple or complex products to novice or expert users. In addition, Mac OS X and Apple Remote Desktop provide facilities for delivering products to several computers on an intranet.

Whether you are a product developer or a network administrator, Mac OS X allows you to create a product delivery solution to satisfy the product-installation needs of your customers.

The nature and structure of your product determine the install experience you can provide to its users. If your product is a self-contained application (one that doesn’t need to install components at different locations in the file system), you can distribute it as a single file or folder. Users then can drag the product from its container or delivery vehicle to a location of their choice in their file systems. This type of installation process is called _manual install_. This is the preferred method of delivering applications to Mac OS X users.

However, there are situations that require more complex products. For example, some applications require the presence of shared resources such as frameworks or fonts, which, in general, reside at `/Library/Frameworks` and `/Library/Fonts`, respectively. Each item that resides at a distinct location on the file system is known as a _component_. To make it easy for users to install a multicomponent product, instead of making users place each component in the appropriate location you develop an appealing install that frees users from that tedious and error-prone task. To that end, the Installer application (`/Applications/Utilities`) uses a simple interface to guide users through the process of installing multicomponent products. This type of installation process is known as a _managed install_.

Managed installs provide users with a GUI (graphical user interface) through which they specify a few details to customize an install. The Installer application handles the file-management tasks on the users’ behalf.

You use PackageMaker (`/Developer/Applications/Utilities`) to develop a managed install. You can tailor the install experience with Read Me and license agreement files and by specifying installation requirements to ensure the product is installed only on systems that meet specific criteria, such as available memory and disk space.

Listing 1-1 shows an example of a single-component product, called Atom. This is the kind of product users should be able to install manually.

__Listing 1-1__  Atom—A single-component product

```
Atom_product/
   Atom.app
```

Listing 1-2, on the other hand, showcases a multicomponent product, called Levon, comprised of an application package, a documentation file, and a framework. The application package should be placed in `/Applications`, the documentation file in `/Library/Documentation`, and the framework in `/Library/Frameworks`. (See _[File System Overview](../../Mac%20OSX/File%20System%20Overview/Introduction%20to%20the%20File%20System%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4dk2i)_ for a more complete list file system locations and component types.) For users, having to drag three files to three locations is not an appealing install experience. A managed install is more appropriate for a product of this kind.

__Listing 1-2__  Levon—A multicomponent product

```
Levon_product/
   Levon.app
   Levon_User_Guide.pdf
   SharedServices.framework
```


If you’re a network administrator, you probably are often faced with the task of distributing the same software to a set of computers. A _remote install_ is an installation process that network administrators can use to remotely place products on several networked computers. Remote installs use the same underlying engine that managed installs are based on. But although the Installer application is used to perform the install tasks on the target clients, the users of these computers do not participate in the installation process; that is, they don’t interact with Installer. In fact, administrators can install products on computers while users are logged in and actively using their systems. Also, administrators can schedule a Remote Desktop task that performs a remote install, ensuring that unavailable computers receive the product when they become available. (See _[Apple Remote Desktop Administrator's Guide Version 3.3](http://images.apple.com/server/docs/ARD_3_Admin_Guide_v3.3.pdf)_ for more information.

The following chapters describe in detail how to develop a delivery solution for your product.

[Next](Product%20Containers.md)[Previous](Introduction.md)

