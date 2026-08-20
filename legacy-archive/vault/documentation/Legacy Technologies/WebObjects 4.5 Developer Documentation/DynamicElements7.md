---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/DynamicElements7.html
archived_at: '2026-07-15T08:05:30.978190Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Dynamic%20Elements.md) [!Previous Section](DynamicElements6.md)

## How Client-Side Components Work

A client-side component is really just a special case of a particular server-side dynamic element named WOApplet. You use WOApplet when you want to include any Java applet in a WebObjects application. The difference between a client-side component and other Java applets is that client-side components can communicate with the server.
When you look at client-side component's bindings in the __.wod__ file, it looks like this example:

```
INPUTFIELD : WOApplet {
        code = "next.wo.client.controls.TextFieldApplet.class";
        codebase = "/WebObjects/Java";
        archive = "woextensions.jar";
        agcArchive = "woextensions.jar";
        width = "200";
        height = "20";
        associationClass =
"com.apple.client.webobjects.SimpleAssociation";
        stringValue = inputString
};
```


Like any other server-side dynamic element, the WOApplet's definition contains a list of attributes bound to constants or variables in the component's code.
The __code__ attribute specifies which client-side component this WOApplet should download. The __codebase__ attribute specifies the path of the component relative to your web server's document root. (For the provided client-side components, this path is always __/WebObjects/Java__.)
The __archive__ attribute specifies __.jar__ files that should be pre-loaded onto the client machine. If you don't use this attribute, the applet downloads Java __.class__ files from the server one by one as it needs them. With the __archive__ attribute, you can package all necessary Java classes into archive files, and they are downloaded once. However, only web browsers that have Java 1.1 support can use __.jar__ files. Because Java 1.1 is fairly new, there's a good chance your users use browsers that don't support __.jar__ files. All of the provided client-side components are packaged in a single archive file named __woextensions.jar__.
The __agcArchive__ and __associationClass__ attributes differentiate the client-side components from any other applet you might include in your application. The __agcArchive__ attribute specifies the __.jar__ file that contains the AppletGroupController object. AppletGroupController is a hidden Java applet (on the client) that controls the visible applets and handles communication back to the server. AppletGroupController works in conjunction with the object specified by the __association__ attribute. The __association__ attribute specifies a subclass of __com.apple.client.webobjects.Association__ that the component uses to communicate with the application on the server. The Association object can get and set component state and cause methods to be invoked in the server when actions are triggered in the client. The most common association is __com.apple.client.webobjects.SimpleAssociation__. When creating your own client-side components, you can either use it or define your own association. Creating your own association is useful when you don't have the source code for your client-side component.
The final attribute, __stringValue__, is an attribute specific to the TextFieldApplet component. The Association object assigns the value of the __inputString__ variable to be the value of the text field on the client and keeps the two objects in sync so that they always have the same value.
__Note:__  Netscape Navigator 4 supports only a single __.jar__ file per applet, and if there is an interface class to support the applets (that is, if you are using AppletGroupController), that object must be found in the same archive file. Thus if you must support Netscape Navigator 4, you should create one __.jar__ file that contains all of your Java client-side classes, all third-party classes that you are using, and all classes in __com.apple.client.webobjects__. Bind that __.jar__ file to the __archive__ attribute of all of the WOApplets on your page. Bind the same __.jar__ file to the __agcArchive__ attribute of the first WOApplet on the page.

[!Table of Contents](Dynamic%20Elements.md) [!Next Section](DynamicElements8.md)
