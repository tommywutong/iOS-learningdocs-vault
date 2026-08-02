---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/Movies/MoviesTOC.html
archived_at: '2026-07-15T07:55:06.047977Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Top](../GettingStartedTOC.md)

# Creating a WebObjects Database Application

---

One of the most powerful features of WebObjects is its ability to provide access to databases. To do so, it uses a framework called the Enterprise Objects Framework. This chapter introduces you to the Enterprise Objects Framework by showing you how to create a simple database application. The steps you take in creating this application demonstrate the principles you'll use in every other application you develop with the WebObjects and Enterprise Objects Framework.
The application you'll create in this tutorial is called Movies. It makes use of a sample database, the Movies database, that contains information about movies. Before you do this tutorial, you need to set up the Movies database as described in the _[Post-Installation Instructions](../../PostInstall/PostInstallTOC.md)_. In addition, if you aren't familiar with Project Builder and WebObjects Builder, read the first tutorials in this book, ["Creating a Simple WebObjects Application"](../GuestBook/GuestBookTOC.md) and ["Enhancing Your Application"](../GuestBookPlus/GuestBookPlusTOC.md), which introduce basic concepts and procedures you should know before you go on.

In this tutorial, you will:

- Use the WebObjects Application Wizard to create a fully functional Main component that reads and writes from the Movies database.
- Create and configure _display groups_ for interacting with a database in terms of objects.
- Create bindings between display groups and a user interface.
- Write code to manipulate display groups' selected objects.
- Set up display groups in a master-detail configuration.
- Use EOModeler to maintain a model file.
- Create custom enterprise object classes.

Along the way, you'll learn basic Enterprise Objects Framework concepts you can use to design your own database applications.

[****
: __The Movies Application__](0_Intro.md#apple-ge4tiobz)

[****
: __Enterprise Objects and the Movies Database__](0_Intro.md#apple-geytanjw)

[****
: Enterprise Objects and Relationships](0_Intro.md#apple-gm2dk)

[****
: __Designing the Main Page__](Movies1.md#apple-ge2tknzz)

[****
: Starting the WebObjects Application Wizard](Movies1.md#apple-he2doma)[****
: Specifying a Model File](Movies2.md#apple-geytgnjz)[****
: Choosing an Adaptor](Movies3.md#apple-geytgnzv)[****
: Choosing What to Include in Your Model](Movies4.md#apple-he2tkoi)[****
: Choosing the Tables to Include](Movies5.md#apple-gi4ta)[****
: Specifying Primary Keys](Movies6.md#apple-he3domy)[****
: Specifying Referential Integrity Rules](Movies7.md#apple-geytqmrq)[****
: Choosing an Entity](Movies8.md#apple-he3dmny)[****
: Choosing a Layout](Movies10.md#apple-gmyte)[****
: Choosing Attributes to Display](Movies11.md#apple-he3tonq)[****
: Choosing an Attribute to Display as a Hyperlink](Movies11.md#apple-he3tkni)[****
: Choosing Attributes to Query On](Movies11.md#apple-he3tmna)[****
: Running Movies](Movies12.md#apple-gezdcnzu)

[****
: __Examining Your Project__](Movies13.md#apple-gmydg)

[****
: Examining the Variables](Movies14.md#apple-gezdimbs)[****
: Examining the Bindings](Movies15.md#apple-ge2dkojq)

[****
: Bindings in the Query Part](Movies16.md#apple-ge2dkojx)[****
: Bindings in the Repetition Part](Movies17.md#apple-ge3timjs)[****
: Bindings in the Editing Part](Movies18.md#apple-ge2dmnbv)

[****
: __Refining Main.wo__](Movies19.md#apple-geztknbx)

[****
: Specifying a Sort Order](Movies20.md#apple-ge2deoju)[****
: Specifying Default Values for New Enterprise Objects](Movies21.md#apple-ge3tknbx)[****
: Setting a Date Format](Movies22.md#apple-geztknbz)[****
: Setting a Number Format](Movies23.md#apple-giztaoby)[****
: Optional Exercise](Movies24.md#apple-ge2dsnby)

[****
: __Adding the MovieDetails Page__](Movies25.md#apple-ge4damrr)

[****
: Creating the MovieDetails Component](Movies25.md#apple-gm4ts)[****
: Storing the Selected Movie](Movies26.md#apple-gqydc)[****
: Navigating from Main to MovieDetails](Movies27.md#apple-gqzta)[****
: Designing MovieDetails' User Interface](Movies28.md#apple-geydgmru)[****
: Adding Date and Number Formats](Movies29.md#apple-gqzdk)[****
: Navigating from MovieDetails to Main](Movies29.md#apple-ge2tenrq)[****
: Running Movies](Movies29.md#apple-g44ta)

[****
: __Refining Your Model__](Movies30.md#apple-gq2di)

[****
: Opening Your Model](Movies30.md#apple-geztoojv)[****
: Removing Primary and Foreign Keys as Class Properties](Movies31.md#apple-geztsmrs)[****
: Adding Relationships to Your Model](Movies32.md#apple-geztsmbv)[****
: Using the Advanced Relationship Inspector](Movies33.md#apple-geztsmzt)[****
: Where Do Primary Keys Come From?](Movies34.md#apple-ge2tmobx)

[****
: __Setting Up a Master-Detail Configuration__](Movies35.md#apple-geztonrx)

[****
: Creating a Detail Display Group](Movies36.md#apple-ge2dinjs)[****
: Adding a Repetition](Movies37.md#apple-ge3daojs)[****
: Configuring a Repetition](Movies38.md#apple-geztkojq)[****
: Running Movies](Movies38.md#apple-ge3dgmjy)

[****
: __Updating Objects in the Detail Display Group__](Movies39.md#apple-gu3te)

[****
: Managing a DisplayGroup's Selection](Movies40.md#apple-gu3tg)[****
: Adding a Form](Movies41.md#apple-gu3to)[****
: Adding a Talent Display Group](Movies42.md#apple-geydknzu)[****
: Configuring the Browser](Movies43.md#apple-ge2danrv)[****
: Adding Insert, Save, and Delete Buttons](Movies44.md#apple-gyydq)

[****
: __Adding Behavior to Your Enterprise Objects__](Movies45.md#apple-ge4tcmjq)

[****
: Specifying Custom Enterprise Object Classes](Movies46.md#apple-ge4timzr)[****
: Generating Custom Enterprise Object Classes](Movies47.md#apple-ge4timru)[****
: Adding Custom Behavior to Talent](Movies48.md#apple-ge4tenrx)[****
: Providing Default Values in MovieRole](Movies49.md#apple-ge4tgmjz)[****
: Running Movies](Movies49.md#apple-giydmmbr)

[!First Section](0_Intro.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
