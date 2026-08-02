---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTOC.html
archived_at: '2026-07-15T08:08:44.240997Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Overview%20of%20Java%20Client.md)

---

#  Creating a Java Client WebObjects Application

[[PDF]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClient.pdf)

## Table of Contents

####  [Overview of Java Client](Overview%20of%20Java%20Client.md#apple-obtwmslehuytambqha3tg)

[Advantages of Java](Advantages%20of%20Java.md#apple-obtwm3dehu4tsobxg43a)

[Java Client Architecture](Java%20Client%20Architecture.md#apple-obtwm3dehu4tsobxg44q)

   [Data Synchronization Between Client and Server](Data%20Synchronization%20Between%20Client%20and%20Server.md#apple-obtwm3dehu4tsobzgu3a)

[Java Client as a WebObjects Application](Java%20Client%20as%20a%20WebObjects%20Application.md#apple-obtwm3dehu4tsobxhaza)

[Java Client Layers and Classes](Java%20Client%20Layers%20and%20Classes.md#apple-obtwmslehu4tsobxha2q)

   [Client Interface and Control Layers](Client%20Interface%20and%20Control%20Layers.md#apple-obtwm3dehuytambqgqytc)

   [The Distribution Layer](The%20Distribution%20Layer.md#apple-obtwm3dehu4tsojxgeyq)

      [Client Distribution Classes](Client%20Distribution%20Classes.md#apple-obtwmslehu4tsojqgmzq)

      [Server Distribution Classes](Server%20Distribution%20Classes.md#apple-obtwmslehu4tsojqgm4q)

[Programming With Java Client](Programming%20With%20Java%20Client.md#apple-obtwm3dehu4tsojvgy3q)

####  [Tutorial](Tutorial.md#apple-obtwmslehuytambwga3ts)

[Requirements](Requirements.md#apple-obtwmslehuytambwga4do)

[Enterprise Objects and Relational Databases](Enterprise%20Objects%20and%20Relational%20Databases.md#apple-obtwmslehuytambwgeydc)

[What Goes Into the StudioManager Application](What%20Goes%20Into%20the%20StudioManager%20Application.md#apple-obtwm3dehuytambwgeyto)

[Creating the StudioManager Project](Creating%20the%20StudioManager%20Project.md#apple-obtwmslehuytambwgeztk)
   

[Using the Wizard](Using%20the%20Wizard.md#apple-obtwm3dehuytambwge3tg)
      

[Creating a Model](Creating%20a%20Model.md#apple-obtwmslehuytambwge4tq)
      

[Selecting the Application Template](Selecting%20the%20Application%20Template.md#apple-obtwmslehuytambwgmyto)

[The Ingredients of a Java Client Project](The%20Ingredients%20of%20a%20Java%20Client%20Project.md#apple-obtwmslehuytambwgmztc)

[Client Files](Client%20Files.md#apple-obtwmslehuytambwgmztq)
      

[The Nib File](The%20Nib%20File.md#apple-obtwmslehuytambwgm2da)
      

[The Interface Controller](The%20Interface%20Controller.md#apple-obtwmslehuytambwgm2di)
   

[Server Files](Server%20Files.md#apple-obtwm3dehuytambwgm2tc)
      

[The WOJavaClientApplet Component](The%20WOJavaClientApplet%20Component.md#apple-obtwmslehuytambwgm3dc)
      

[Other Server Files](Other%20Server%20Files.md#apple-obtwmslehuytambwgqydi)

[Verifying and Modifying the Model](Verifying%20and%20Modifying%20the%20Model.md#apple-obtwm3dehuytambwgqyti)
   

[Assigning Primary Keys](Assigning%20Primary%20Keys.md#apple-obtwmslehuytambwgq2da)
   

[Removing Primary and Foreign Keys as Class Properties](Removing%20Primary%20and%20Foreign%20Keys%20as%20Class%20Properties.md#apple-obtwm3dehuytambwgq4ti)

[Creating the User Interface](Creating%20the%20User%20Interface.md#apple-obtwmslehuytambwguyti)
   

[Formatting Currency Values and Dates](Formatting%20Currency%20Values%20and%20Dates.md#apple-obtwm3dehuytambwgyyti)
   

[Adding Action Methods](Adding%20Action%20Methods.md#apple-obtwmslehuytambwgyztc)

[Building and Testing Your Application](Building%20and%20Testing%20Your%20Application.md#apple-obtwmslehuytambwgy2tk)
   

[Testing the Interface](Testing%20the%20Interface.md#apple-obtwm3dehuytambwgy2to)
   

[Building the Application](Building%20the%20Application.md#apple-obtwm3dehuytambwgy3te)
   

[Running a Java Client Application](Running%20a%20Java%20Client%20Application.md#apple-obtwmslehuytambwgy4dk)
   

[What if It Doesn't Work?](What%20if%20It%20Doesn%27t%20Work.md#apple-obtwm3dehuytambwg4zde)

[Adding Relationships](Adding%20Relationships.md#apple-obtwmslehuytambwg42de)
   

[Adding Movies to the Application](Adding%20Movies%20to%20the%20Application.md#apple-obtwm3dehuytambwg43ts)
   

[Creating a Master-Detail Interface](Creating%20a%20Master-Detail%20Interface.md#apple-obtwmslehuytambwg44di)

[Transferring Movies Between Studios](Transferring%20Movies%20Between%20Studios.md#apple-obtwmslehuytambwha3te)

[Putting the Finishing Touches on Your Model](Putting%20the%20Finishing%20Touches%20on%20Your%20Model.md#apple-obtwm3dehuytambwhezde)

[Adding Behavior to Your Enterprise Objects](Adding%20Behavior%20to%20Your%20Enterprise%20Objects-2.md#apple-obtwmslehuytambwhe2tq)
   

[Specifying Custom Enterprise Object Classes](Specifying%20Custom%20Enterprise%20Object%20Classes-2.md#apple-obtwmslehuytambwhe3da)
   

[Generating Source Files](Generating%20Source%20Files.md#apple-obtwm3dehuytambwhe4dg)
   

[Implementing Custom Behavior for Your Classes](Implementing%20Custom%20Behavior%20for%20Your%20Classes.md#apple-obtwmslehuytambxga3ds)
      

[Distributing Business Logic in Java Client Applications](Distributing%20Business%20Logic%20in%20Java%20Client%20Applications.md#apple-obtwmslehuytambxga3tk)
      

[Writing Derived Methods](Writing%20Derived%20Methods.md#apple-obtwmslehuytambxga4dc)
      

[Performing Validation](Performing%20Validation.md#apple-obtwmslehuytambxge2tg)
      

[Providing Default Values for Newly Inserted Objects](Providing%20Default%20Values%20for%20Newly%20Inserted%20Objects.md#apple-obtwmslehuytambxge3te)
      

[Invoking Server Methods Remotely](Invoking%20Server%20Methods%20Remotely.md#apple-obtwmslehuytambxge4di)
      

[Controlling the User Interface](Controlling%20the%20User%20Interface.md#apple-obtwmslehuytambxgi4da)

####  [Advanced Tasks](Advanced%20Tasks.md#apple-obtwmslehuytambwga3tg)

[Debugging Java Client WebObjects Applications](Debugging%20Java%20Client%20WebObjects%20Applications.md#apple-obtwmslehuytambwga3tk)
   

[Debugging Server Code](Debugging%20Server%20Code.md#apple-obtwmslehuytambwga3to)
   

[Debugging Client Code](Debugging%20Client%20Code.md#apple-obtwmslehuytambwga4da)

[Customizing Your Project With Wizards](Customizing%20Your%20Project%20With%20Wizards.md#apple-obtwmslehuytambwga4tk)
   

[Adding Client-side Subprojects](Adding%20Client-side%20Subprojects.md#apple-obtwmslehuytambwga4to)
   

[Adding Interface Controller Subclasses and Nib Files](Adding%20Interface%20Controller%20Subclasses%20and%20Nib%20Files.md#apple-obtwmslehuytambwgeydm)
   

[Adding Web Components (with Interface Controllers)](Adding%20Web%20Components%20%28with%20Interface%20Controllers%29.md#apple-obtwmslehuytambwgezda)
   

[Manual Adjustments to Java Client Projects](Manual%20Adjustments%20to%20Java%20Client%20Projects.md#apple-obtwmslehuytambwgeztq)

####  [Enterprise Objects Framework Concepts](Enterprise%20Objects%20Framework%20Concepts.md#apple-obtwmslehuytambwga3tg)

[Note to Oracle Users](Note%20to%20Oracle%20Users.md#apple-obtwmslehuytambwga4da)

[What is an Enterprise Object?](What%20is%20an%20Enterprise%20Object.md#apple-obtwmslehuytambwga4dm)

[What is a Model?](What%20is%20a%20Model.md#apple-obtwmslehuytambwga4te)

[What are EODisplayGroups and EOEditingContexts?](What%20are%20EODisplayGroups%20and%20EOEditingContexts.md#apple-obtwmslehuytambwgezto)

[What is an Association?](What%20is%20an%20Association.md#apple-obtwmslehuytambwge2dg)

[When Do You Use a Custom Enterprise Object Class?](When%20Do%20You%20Use%20a%20Custom%20Enterprise%20Object%20Class.md#apple-obtwmslehuytambwge2tc)

[Adding Behavior to Enterprise Objects](Adding%20Behavior%20to%20Enterprise%20Objects.md#apple-obtwmslehuytambwge2tm)

####  [Glossary](Glossary.md#apple-obtwmslehu4tsobyge3a)

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Overview%20of%20Java%20Client.md)
