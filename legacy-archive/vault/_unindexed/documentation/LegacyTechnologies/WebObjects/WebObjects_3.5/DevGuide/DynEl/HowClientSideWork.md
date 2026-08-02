---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/DynEl/HowClientSideWork.html
archived_at: '2026-07-15T07:51:31.599010Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynElTOC.md) [!Previous Section](DecidingToUse.md)

## How Client-Side Components Work

A client-side component is really just a special case of a particular server-side dynamic element named WOApplet. You use WOApplet when you want to include any Java applet in a WebObjects application. The difference between a client-side component and other Java applets is that client-side components can communicate with the server.
When you look at client-side component's bindings in the __.wod__ file, it looks like this example:

```
    INPUTFIELD : WOApplet {
        code = "next.wo.client.controls.TextFieldApplet.class";
        codebase = "/WebObjects/Java";
        archive = "woextensions.jar";
        width = "200";
        height = "20";
        associationClass = "next.wo.client.SimpleAssociation";
        stringValue = inputString
    };
```


Like any other server-side dynamic element, the WOApplet's definition contains a list of attributes bound to constants or variables in the component's code.
The __code__ attribute specifies which client-side component this WOApplet should download. The __codebase__ attribute specifies the path of the component relative to your web server's document root. (For the provided client-side components, this path is always __/WebObjects/Java__.)
The __archive__ attribute specifies __.jar__ files that should be preloaded onto the client machine. If you don't use this attribute, the applet downloads Java __.class__ files from the server one by one as it needs them. With the __archive__ attribute, you can package all necessary Java classes into archive files, and they are downloaded once. However, only web browsers that have Java 1.1 support can use __.jar__ files. Because Java 1.1 is fairly new, there's a good chance your users use browsers that don't support __.jar__ files. All of the provided client-side components are packaged in a single archive file named __woextensions.jar__.
The __associationClass__ attribute differentiates the client-side components from any other applet you might include in your application. This attribute specifies an object (a subclass of __next.wo.client.Association__) that the component uses to communicate with the application on the server. The Association object can get and set component state and cause methods to be invoked in the server when actions are triggered in the client. For the WebObjects-provided client-side components, this attribute is always __next.wo.client.SimpleAssociation__. If you create your own client-side components, you provide your own Association subclass.
The final attribute, __stringValue__, is an attribute specific to the TextFieldApplet component. The Association object assigns the value of the __inputString__ variable to be the value of the text field on the client and keeps the two objects in sync so that they always have the same value.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
