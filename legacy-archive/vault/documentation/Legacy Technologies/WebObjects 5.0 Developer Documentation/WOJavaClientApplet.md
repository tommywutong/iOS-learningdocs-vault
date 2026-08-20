---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EODistributionRef/Java/Server/Classes/WOJavaClientApplet.html
archived_at: '2026-07-15T08:13:49.515661Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EODistributionRef/Java/Server/Art/up.gif)](../../EODistributionTOC.md) 

# WOJavaClientApplet

> **__Inherits from:__**
> : com.webobjects.appserver.WOComponent

> **__Package:__**
> : com.webobjects.eodistribution

---

## Class Description

---

WOJavaClientApplet is the web component used by Java Client applications to create and download to the client an applet of class com.apple.client.interface.EOApplet. This component passes several parameters to the applet, including the dimensions, code/codebase, and additional EOApplication-specific parameters-such as the initial EOInterfaceController subclass name and language.

WOJavaClientApplet is able to generate the HTML required by SunSoft's Java Plug-in for Microsoft's Internet Explorer and Netscape's browsers. The plug-in is usually required for Netscape, while Internet Explorer often works without it (whether or not the plug-in is required depends on the applet's contents).

Java Client applications can be started outside of a web browser using the following command-line syntax:

java -classpath path_list com.apple.client.eointerface.EOApplication application_url

When a Java Client application is started outside of a browser, the WOJavaClientApplet is still used on the server side to determine the additional EOApplication-specific parameters. Thus the bindings listed below can still apply even in the absence of a web browser.

The following tables lists those bindings used by WOJavaClientApplet:

|  |  |
| --- | --- |
| __Binding__ | __Description__ |
| width | Width of applet in the HTML page. |
| height | Height of applet in the HTML page. |
| useJavaPlugin | If this flag is true, the WOJavaClientApplet generates HTML that causes Internet Explorer and Netscape's browsers to use SunSoft's Java Plug-in. |
| archive | Standard applet parameter. |
| code | Standard applet parameter. |
| codebase | Standard applet parameter. |
| distributionContext | The EODistributionContext used by the applet to handle requests from the client. If the WOJavaClientApplet does not have a binding for the distribution context, it instantiates one with the session's __defaultEditingContext__, sets the session as the delegate of the distribution context, and itself as the invocation target. |
| interfaceControllerClassName | The class name of the initial EOInterfaceController subclass that becomes visible when an application is launched (in the applet if launched inside a browser). |
| applicationClassName | The name of the EOApplication subclass implementing the application. |
| language | The preferred language for the application. |
| channelClassName | The class name of the distribution channel to be used by the client. |
| temporaryGIDBase | The base from which temporary global ID's are generated. |
| allParameterNames | An NSArray containing the applet's parameters. |
| sessionID | The receiver's session ID. |
| componentURL | The URL for the receiver's action. |

## Constants

---

WOJavaClientApplet defines the following String constants. Each constant corresponds to a WOJavaClientApplet binding and is a key for use in the dictionary returned by [clientSideRequestApplicationParameters](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjjqxmykdnruwk3tuifyha3dfoqxwg3djmvxhiu3jmrsvezlrovsxg5cbobygy2ldmf2gs33okbqxeylnmv2gk4tt).

|  |  |
| --- | --- |
| __Constant__ | __Corresponding Binding__ |
| WidthKey | width |
| HeightKey | height |
| UseJavaPluginKey | useJavaPlugin |
| ArchiveKey | archive |
| CodeKey | code |
| CodebaseKey | codebase |
| DistributionContextKey | distributionContext |
| InterfaceControllerClassNameKey | interfaceControllerClassName |
| ApplicationClassNameKey | applicationClassName |
| LanguageKey | language |
| ChannelClassNameKey | channelClassName |
| TemporaryGIDBaseKey | temporaryGIDBase |
| AllParameterNamesKey | allParameterNames |
| SessionIDKey | sessionID |
| ComponentURLKey | componentURL |

WOJavaClientApplet also defines String constants for the names of the notifications it posts. For more information, see ["Notifications" (page 40)](#apple-ijfesssgiffeg).

## Constructors

---

### WOJavaClientApplet

`public WOJavaClientApplet(WOContext context)`

Standard one-argument WOComponent constructor.

---

## Instance Methods

---

### allParameterNamesString

`public String allParameterNamesString()`

Returns a string containing all of the receiver's parameters separated by spaces.

---

### applicationClassName

`public String applicationClassName()`

Returns a string containing the name of the EOApplication subclass the applet contains.

---

### archive

`public String archive()`

If the applet has a binding for __archive__, the value of that binding is returned. Otherwise, the default __archive__ binding-"eojavaclient.jar"-is returned.

---

### channelClassName

`public String channelClassName()`

Returns the string value bound to the __channelClassName__ binding. The __channelClassName__ identifies the class of the object that the client uses for a distribution channel.

__See Also:__ [interfaceControllerClassName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjjqxmykdnruwk3tuifyha3dfoqxws3tumvzgmyldmvbw63tuojxwy3dfojbwyyltonhgc3lf)

---

### clientSideRequestApplicationParameters

`public NSDictionary clientSideRequestApplicationParameters()`

Returns a dictionary with the values of all the bindings that have been set. This method is used by EOApplication on the client to warm up a Java application started outside of a browser.

__See Also:__ [interfaceControllerClassName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjjqxmykdnruwk3tuifyha3dfoqxws3tumvzgmyldmvbw63tuojxwy3dfojbwyyltonhgc3lf)

---

### code

`public String code()`

If the applet has a binding for __code__, the value of that binding is returned. Otherwise, the default __code__ binding-"com.apple.client.eointerface.EOApplet"-is returned.

---

### codebase

`public String codebase()`

If the applet has a binding for __codebase__, the value of that binding is returned. Otherwise, this method checks to see if the request came through a web server and, if so, returns a URL relative to __cgi-bin/WebObjects__ for the resource request handler. If the request didn't come through a web server, this method returns "/WebObjects/Java".

---

### componentURL

`public String componentURL()`

Returns a string containing the receiver's action URL.

---

### distributionContext

`public EODistributionContext distributionContext()`

Returns the EODistributionContext used by this component to handle client requests.

---

### handleClientRequest

`public Object handleClientRequest()`

Using the component's EODistributionContext, generates a response for a client request.

__See Also:__ responseToClientMessage (EODistributionContext class)

---

### interfaceControllerClassName

`public String interfaceControllerClassName()`

Returns the value bound to __interfaceControllerClassName__.

__See Also:__ [channelClassName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjjqxmykdnruwk3tuifyha3dfoqxwg2dbnzxgk3cdnrqxg42omfwwk), [clientSideRequestApplicationParameters](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjjqxmykdnruwk3tuifyha3dfoqxwg3djmvxhiu3jmrsvezlrovsxg5cbobygy2ldmf2gs33okbqxeylnmv2gk4tt)

---

### otherParameterNames

`public NSArray otherParameterNames()`

Returns an array containing the names of the nonstandard WOJavaClientApplet parameters.

---

### otherParametersString

`public String otherParametersString()`

Returns a string containing the parameter names and values of the nonstandard WOJavaClientApplet parameters. The string is in the form 'name`="`value`"` name`="`value`" ...`

---

### otherParameterValue

`public String otherParameterValue()`

Returns the value of the parameter corresponding to the `otherParameterName` instance variable.

---

### sessionID

`public String sessionID()`

Returns a string containing the receiver's session ID.

---

### shouldOmitApplicationClassName

`public boolean shouldOmitApplicationClassName()`

Description forthcoming.

---

### shouldOmitChannelClassName

`public boolean shouldOmitChannelClassName()`

Description forthcoming.

---

### shouldOmitInterfaceControllerClassName

`public boolean shouldOmitInterfaceControllerClassName()`

Description forthcoming.

---

### synchronizesVariablesWithBindings

`public boolean synchronizesVariablesWithBindings()`

Overridden from com.webobjects.appserver.WOComponent.

---

### temporaryGIDBase

`public String temporaryGIDBase()`

Returns a string containing the base from which temporary global ID's are generated.

---

## Notifications

---

### DidVendComponentURLNotification

Posted after the WOJavaClientApplet vends a component URL. The notification contains:

|  |  |
| --- | --- |
| Notification Object | The WOJavaClientApplet that vended a component URL. |
| Userinfo | None |

### WillDeallocNotification

Posted whenever the WOJavaClientApplet is about to be deallocated. The notification contains:

|  |  |
| --- | --- |
| Notification Object | The WOJavaClientApplet that's about to be deallocated. |
| Userinfo | None |

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/EODistributionRef/Java/Server/Art/up.gif)](../../EODistributionTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
