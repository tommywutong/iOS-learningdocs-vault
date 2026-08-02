---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTOC.html
archived_at: '2026-07-15T08:00:18.860692Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
JavaClient Tutorial

_Creating a Java Client WebObjects Application_

[Next](CSJ_Tutorial.g.md)

# Creating a Java Client WebObjects Application

#### Apple Developer's Library

[PDF](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/JavaClient.pdf)

###  Contents

###  [Overview of Java Client](CSJ_Tutorial.g.md#apple-obtwmslehuytambqha3tg)

[Advantages of Java](CSJ_Tutorial.1.md#apple-obtwmslehu4tsobxg43a)

[Java Client Architecture](CSJ_Tutorial.2.md#apple-obtwmslehu4tsobxg44q)

- [Data Synchronization Between Client and Server](CSJ_Tutorial.3.md#apple-obtwmslehu4tsobzgu3a)

[Java Client as a WebObjects Application](CSJ_Tutorial.4.md#apple-obtwmslehu4tsobxhaza)

[Java Client Layers and Classes](CSJ_Tutorial.5.md#apple-obtwmslehu4tsobxha2q)

- [Client Interface and Control Layers](CSJ_Tutorial.6.md#apple-obtwmslehuytambqgqytc)

- [The Distribution Layer](CSJ_Tutorial.7.md#apple-obtwmslehu4tsojxgeyq)

  - [Client Distribution Classes](CSJ_Tutorial.7.md#apple-obtwmslehu4tsojqgmzq)

  - [Server Distribution Classes](CSJ_Tutorial.7.md#apple-obtwmslehu4tsojqgm4q)

[Programming With Java Client](CSJ_Tutorial.8.md#apple-obtwmslehu4tsojvgy3q)

### [Tutorial](CSJ_Tutorial.8a.md#apple-obtwmslehu2tgojw)

- [Requirements](CSJ_Tutorial.8a.md#apple-obtwmslehuytsmbqgi)

[Enterprise Objects and Relational Databases](CSJ_Tutorial.9.md#apple-obtwmslehu2timbv)

[What Goes Into the StudioManager Application](CSJ_Tutorial.a.md#apple-obtwmslehuytkmbqgq)

[Creating the StudioManager Project](CSJ_Tutorial.b.md#apple-obtwmslehuytknzxga)

- [Using the Wizard](CSJ_Tutorial.c.md#apple-obtwmslehuytmmzwgq)

  - [Creating a Model](CSJ_Tutorial.c.md#apple-obtwmslehuytombtgy)

    [- Selecting the Application Template](CSJ_Tutorial.c.md#apple-obtwmslehuytmobygy)

[The Ingredients of a Java Client Project](CSJ_Tutorial.d.md#apple-obtwmslehuytsmjugi)

- [Client Files](CSJ_Tutorial.e.md#apple-obtwmslehu4dsmzq)

  - [The Nib File](CSJ_Tutorial.e.md#apple-obtwmslehuzdcobwgy)

  - [The Interface Controller](CSJ_Tutorial.e.md#apple-obtwmslehuzdeojrg4)

- [Server Files](CSJ_Tutorial.f.md#apple-obtwmslehuzdcobxge)

  - [The WOJavaClientApplet Component](CSJ_Tutorial.f.md#apple-obtwmslehuzdcobyga)

  - [Other Server Files](CSJ_Tutorial.f.md#apple-obtwmslehuzdanjzha)

[Verifying and Modifying the Model](CSJ_Tutorial.10.md#apple-obtwmslehuytcnzwgy)

- [Assigning Primary Keys](CSJ_Tutorial.11.md#apple-obtwmslehu2tinzz)

- [Removing Primary and Foreign Keys as Class Properties](CSJ_Tutorial.12.md#apple-obtwmslehuytemzxge)

[Creating the User Interface](CSJ_Tutorial.13.md#apple-obtwmslehu2tknby)

- [Formatting Currency Values and Dates](CSJ_Tutorial.14.md#apple-obtwmslehuyteojwgi)

- [Adding Action Methods](CSJ_Tutorial.15.md#apple-obtwmslehuzdgmjvhe)

[Building and Testing Your Application](CSJ_Tutorial.16.md#apple-obtwmslehuzdgmjwg4)

- [Testing the Interface](CSJ_Tutorial.17.md#apple-obtwmslehuytgmbsgq)

- [Building the Application](CSJ_Tutorial.18.md#apple-obtwmslehuzdgmjxgy)

- [Running a Java Client Application](CSJ_Tutorial.19.md#apple-obtwmslehuzdgmjzgy)

- [What if It Doesn't Work?](CSJ_Tutorial.1a.md#apple-obtwmslehuzdgmruge)

[Adding Relationships](CSJ_Tutorial.1b.md#apple-obtwmslehu2tomjx)

- [Adding Movies to the Application](CSJ_Tutorial.1c.md#apple-obtwmslehu3tknjz)

- [Creating a Master-Detail Interface](CSJ_Tutorial.1d.md#apple-obtwmslehuytenbuge)

[Transferring Movies Between Studios](CSJ_Tutorial.1e.md#apple-obtwmslehu2tqmrz)

[Putting the Finishing Touches on Your Model](CSJ_Tutorial.1f.md#apple-obtwmslehu2tqnjv)

[Adding Behavior to Your Enterprise Objects](CSJ_Tutorial.20.md#apple-obtwmslehu4tkmbw)

- [Specifying Custom Enterprise Object Classes](CSJ_Tutorial.21.md#apple-obtwmslehu2tqnrr)

- [Generating Source Files](CSJ_Tutorial.22.md#apple-obtwmslehu2tqobq)

- [Implementing Custom Behavior for Your Classes](CSJ_Tutorial.23.md#apple-obtwmslehuytenrxgm)

  - [Distributing Business Logic in Java Client Applications](CSJ_Tutorial.23.md#apple-obtwmslehuzdambsha)

  - [Writing Derived Methods](CSJ_Tutorial.23.md#apple-obtwmslehu2tsojz)

  - [Providing Default Values for Newly Inserted Objects](CSJ_Tutorial.23.md#apple-obtwmslehu3danzz)

  - [Invoking Server Methods Remotely](CSJ_Tutorial.23.md#apple-obtwmslehuzdambtgm)

  - [Controlling the User Interface](CSJ_Tutorial.23.md#apple-obtwmslehuzdcnjzgq)

###  [Advanced Tasks](CSJ_Tutorial.24.md#apple-obtwmslehu4tsobygm4q)

[Debugging Java Client WebObjects Applications](CSJ_Tutorial.24.md#apple-obtwmslehu4tsojqgi4q)

- [Debugging Server Code](CSJ_Tutorial.24.md#apple-obtwmslehu4tsojqgmyq)

- [Debugging Client Code](CSJ_Tutorial.25.md#apple-obtwmslehu4tsojqgm2a)

[Customizing Your Project With Wizards](CSJ_Tutorial.26.md#apple-obtwmslehu4tsojqgyza)

- [Adding Client-side Subprojects](CSJ_Tutorial.27.md#apple-obtwmslehu4tsojqgy3a)

- [Adding Interface Controller Subclasses and Nib Files](CSJ_Tutorial.28.md#apple-obtwmslehu4tsojqgy4q)

- [Adding Web Components (with Interface Controllers)](CSJ_Tutorial.29.md#apple-obtwmslehu4tsojqg42a)

- [Manual Adjustments to Java Client Projects](CSJ_Tutorial.2a.md#apple-obtwmslehu4tsojqhazq)

###  [Enterprise Objects Framework Concepts](CSJ_Tutorial.2b.md#apple-obtwmslehuytambrga2ti)

[Note to Oracle Users](CSJ_Tutorial.2b.md#apple-obtwmslehu4tsobxha3a)

[What is an Enterprise Object?](CSJ_Tutorial.2b.md#apple-obtwmslehu4tsobxgy4a)

[What is a Model?](CSJ_Tutorial.2c.md#apple-obtwmslehu4tsobyg42q)

[What are EODisplayGroups and EOEditingContexts?](CSJ_Tutorial.2d.md#apple-obtwmslehu4tsobxgy4q)

[What is an Association?](CSJ_Tutorial.2e.md#apple-obtwmslehu4tsobxg4ya)

[When Do You Use a Custom Enterprise Object Class?](CSJ_Tutorial.2f.md#apple-obtwmslehu4tsobxg4yq)

[Adding Behavior to Enterprise Objects](CSJ_Tutorial.30.md#apple-obtwmslehu4tsobzg42q)

###  [Glossary](CSJ_Tutorial.31.md#apple-obtwmslehu4tsobyge3a)

---

\xA9 1999 Apple Computer, Inc.

[Next](CSJ_Tutorial.g.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
