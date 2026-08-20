---
title: Software Delivery Legacy Guide
apple_id: TP40004615
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2010-09-15'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/SoftwareDistribution4/Manual_Installs/Manual_Installs.html
archived_at: '2026-07-15T07:26:58.716077Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Software Delivery Legacy Guide](Introduction.md)


[Next](Managed%20Installs.md)[Previous](Product%20Containers.md)

# Manual Installs

A manual install is completely controlled by the user. That is, the user gets the product from its container or delivery vehicle and drags it to their file system. This install model works best for simple products, which are made up of one component type. Listing 3-1 shows a typical example of such a product, called Atom. For multicomponent products, a managed install is more appropriate; see[Managed Installs](Managed%20Installs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqnrnknltq) for details.

__Listing 3-1__  A simple product

```
Atom 1.0.0/
   Atom.app
   ReadMe.rtf
```

The main component of the Atom product is the `Atom.app` file package. Users would normally place this file in `/Applications`, but they are free to place it anywhere. Users may or may not copy the `ReadMe.rtf` file to their file system. This file is not essential for the operation of the Atom product but can include installation instructions for novice users in addition to information about the product.

A manual install is the ideal install experience for Mac OS X users. It is also the easiest way for you to deliver your products. All you need to do is place the product in a container (as described in Product Containers) and make it available to your customers on a delivery vehicle.

[Next](Managed%20Installs.md)[Previous](Product%20Containers.md)

