---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/Movies/Movies1.html
archived_at: '2026-07-15T07:54:08.177906Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](MoviesTOC.md) [!Previous Section](0_Intro.md)

# Designing the Main Page

Every WebObjects application has at least one component-usually named Main-that represents the first page the application displays. In Movies, the Main component represents the MovieSearch page.
To design the Main component, you'll use the WebObjects Application Wizard. The wizard performs all the setup that's necessary to fetch database records and display them in a web page. Specifying different wizard options yields different pages: The MovieSearch page is an example of one of the many different layouts you can generate with the wizard.

## Starting the WebObjects Application Wizard

- In Project Builder, choose Project!New.
- In the New Project panel, select WebObjects Application from the Project Type pop-up list.
- Click Browse.
- In the Open panel, navigate to a directory under _DocumentRoot___/WebObjects__, where you want to create your new project.
- Type Movies in the "File name" field.
- Click Save.
- In the New Project panel, click OK.

This starts the WebObjects Application Wizard.

- Choose Wizard under Available Assistance.

With this option, the wizard guides you through the creation of a Main component for your application. When you finish, you can immediately build and run your application without performing any additional steps and without adding any code.

- Choose Java as the primary language.
- Click Next.

[!Table of Contents](MoviesTOC.md) [!Next Section](Movies2.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
