---
title: Component Manager for QuickTime
apple_id: TP40000858
resource_type: Guide
platform: macOS
topic: null
technology: QuickTime
published: '2005-04-08'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/Conceptual/ComponentMgr/2CompMgr4QT/CompMgr4QT.html
archived_at: '2026-07-18T01:52:42.638877Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Component Manager for QuickTime](Introduction%20to%20Component%20Manager%20for%20QuickTime.md)


[Next](Document%20Revision%20History.md)[Previous](Introduction%20to%20Component%20Manager%20for%20QuickTime.md)

# Component Manager for QuickTime

The Component Manager is used to open, communicate with, and close QuickTime components such as image compressors and movie exporters. QuickTime typically opens, configures, and closes components automatically as needed. The Component Manager provides direct access to components for situations where QuickTime's default behavior is not sufficient.

Another way to find a component of a particular type or inspect the capabilities of components, without actually opening components and interrogating them, is to use the component properties API or the component public resources.

The Component Manager creates an interface between components and clients. Clients can be applications, other components, system extensions, and so on. The Component Manager provides a standard interface your application can use to communicate with all components of a given type. Those components, in turn, provide the appropriate services to your client application.

All components of a given type share a common application interface and basic services. For example, all `'imdc'` components provide image decompression services using a common interface.

Individual components may also support additions to the defined application interface, but they must support the defined interface functions. Algorithm-dependent or implementation-dependent variations are implemented by components as extensions to the basic interface. For example, a decompressor component may support a unique compression technique or take advantage of special hardware, but all decompressor components support the `GetCompressedImageSize` function.

The Component Manager defines three kinds of component functions: functions called by client applications, functions component authors need to implement to allow system access, and support functions provided by the system to simplify the process of creating components. This document focuses on functions used by client applications.

The Component Manager allows applications to find components of a particular kind, such as image compressors, and to choose within available components of a kind, such as a JPEG or Cinepak image compressor.

Components are identified primarily by _type_ and _subtype._ Both type and subtype are four-character codes: 32-bit values that are usually best interpreted as a sequence of four ASCII characters.

For example, an image decompressor for JPEG images has type `'imdc'` and subtype `'jpeg'.` A component’s capabilities and characteristics can be further identified using the manufacturer’s code (also a four-character code, such as `'aapl'),` or by getting the component’s properties, or by interrogating the component directly.

Using the Component Manager, you can find out how many components of a specific type are available and get further details about a component’s capabilities, without having to open the components. The Component Manager keeps track of many component characteristics, such as a component’s name, icon, and information string.

The Component Manager allows a single component to serve multiple client applications at the same time. Each client application has a unique access path to the component. These access paths are called _component_ _connections._ You identify a component connection by specifying a _component_ _instance._ The Component Manager provides this component instance to your application when you open a connection to a component. The component maintains separate status information for each open connection.

For example, multiple applications might each open a connection to an image decompression component. The Component Manager routes each application request to the component instance for that connection. Because a component can maintain separate storage for each connection, application requests do not interfere with each other and each application has full access to the services provided by the component.

A function that finds a component typically returns a component identifier, referred to simply as a component. A function that opens a connection to a component returns a connection identifier, also known as a component instance.

Most QuickTime functions that take a component instance as a parameter can accept a component, as a convenience to the programmer, because the instance can typically be inferred.

This situation becomes ambiguous in threaded programming models, however. If you are calling QuickTime from more than one thread, be careful to always distinguish the component from the component instance.

This section describes how you can use the Component Manager to:

- Gain access to components
- Locate components and take advantage of their services
- Get information about a component
- Close a connection to a component

You can allow the Component Manager to locate a suitable component for you. If you are interested in using a component of a particular type and subtype, and you do not need to specify any other characteristics of the component, use the [OpenADefaultComponent](https://developer.apple.com/documentation/coreservices/1516360-openadefaultcomponent) function. This technique is the easiest way to open a component connection.

The [OpenADefaultComponent](https://developer.apple.com/documentation/coreservices/1516360-openadefaultcomponent) function searches for available components and attempts to open a connection to a component with the specified type and subtype. If more than one component of the specified type and subtype is available, [OpenADefaultComponent](https://developer.apple.com/documentation/coreservices/1516360-openadefaultcomponent) selects the first one in the list. If successful, it passes back a component instance that identifies your connection to the component.

To open a connection to a component based on information more specific than the component type and subtype, you can set up a component description structure ( [ComponentDescription](https://developer.apple.com/documentation/coreservices/componentdescription)) and call [FindNextComponent](https://developer.apple.com/documentation/coreservices/1516552-findnextcomponent), passing in `0` as the component identifier. `FindNextComponent` returns the first component it finds that matches the component description structure. Open the component using OpenAComponent.

If you need to choose among several components that match the component description structure, you can use [GetComponentInfo](https://developer.apple.com/documentation/coreservices/1516438-getcomponentinfo) to retrieve more information on each component. Follow these steps:

1. Set up a component description structure that describes the component.
2. Use the [CountComponents](https://developer.apple.com/documentation/coreservices/1516515-countcomponents) function to determine how many components, if any, match your description.
3. Use the [FindNextComponent](https://developer.apple.com/documentation/coreservices/1516552-findnextcomponent) function to iterate through the list, passing in `0` for the first component and the component ID of the previous component for each subsequent component, as shown in Listing 1.
4. Call [GetComponentInfo](https://developer.apple.com/documentation/coreservices/1516438-getcomponentinfo) to obtain further details on each component.
5. Open the component you want using the OpenAComponent function.

__Listing 1-1__  Iterating through a list of components

```
/*
   An application-defined function, myImportFinder, fills out a
   component description record to specify the search criteria for the
   desired component, then calls FindNextComponent to find a component
   with the specified characteristics--in this example, a movie
   importer component (any component with the type MovieImportType)
   that can open a particular file type  (subtype = someFileType).

   Begin by setting componentID to 0 and calling this function,
   passing in the desired file type to import. The function returns 0
   if a component is found, and componentID is set to the
   component ID. Call this function again without modifying
   omponentID to search for another matching component. The function
   returns 0 if another matching component is found. Repeat until you
   find the particular component that you want or until the function
   return is nonzero (no more matching components).

*/

long componentID

pascal Boolean myImportFinder(OSType someFileType)

{
  ComponentDescription cd;
  Boolean result = true;      // true means no matching importer

  cd.componentType = MovieImportType;
  cd.componentSubType = someFileType;
  cd.componentManufacturer = 0; //any manufacturer
  cd.componentFlags = canMovieImportFiles;
  cd.componentFlagsMask = canMovieImportFiles;
  componentID = (FindNextComponent(componentID, &cd))  // search for component to do the work
  if componentID
    result = false;

  return result;
}
```

Alternatively, you can use the component property functions to get the properties of components, though not all components support this. For more information, see [Component Property Functions and Selectors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnjyfvbuqmlhfvbw63lqn5xgk3tukbzg64dfoj2hsrtvnzrxi2lpnzzwc3teknswyzldorxxe4y).

Some components also provide information about themselves in public resources. For details, see [Component Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnjyfvbuqmlhfvbw63lqn5xgk3tukjsxg33vojrwk4y).

The specific component functions available to applications vary considerably with the component type. See the documentation for a given type of component to see what functions it provides that are unique.

The Component Manager defines a number of functions that all components should support, however, regardless of component type. For example, all components should support [GetComponentInfo](https://developer.apple.com/documentation/coreservices/1516438-getcomponentinfo) and `GetComponentVersion`. In addition, you can ask any component if it supports a given function by calling ComponentFunctionImplemented .

For more information, see [Component Manager Functions and Data Structures for Applications](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnjyfvbuqmlhfvbw63lqn5xgk3tujvqw4ylhmvzem5lomn2gs33oonqw4zcemf2gcu3uoj2wg5dvojsxgztpojaxa4dmnfrwc5djn5xhg).

When your application is done with a component, close the connection by calling [CloseComponent](https://developer.apple.com/documentation/coreservices/1516436-closecomponent). When all component instances are closed, the component is released.

These are the Component Manager functions and data types commonly used by applications to work with components.

Additional functions that may be available to applications vary with the component type. See the documentation for a specific component to see what it does.

The functions listed here should be supported by all components, regardless of type. In addition, you can ask any component if it supports a given function by calling `ComponentFunctionImplemented`.

For a complete list of Component Manager functions and data types, see _[Component Manager Reference](https://developer.apple.com/documentation/coreservices/carbon_core/component_manager)_.

Finding components:

- [FindNextComponent](https://developer.apple.com/documentation/coreservices/1516552-findnextcomponent)
- [CountComponents](https://developer.apple.com/documentation/coreservices/1516515-countcomponents)
- [GetComponentListModSeed](https://developer.apple.com/documentation/coreservices/1516399-getcomponentlistmodseed)
- [GetComponentTypeModSeed](https://developer.apple.com/documentation/coreservices/1516653-getcomponenttypemodseed)

Opening and closing components:

- [OpenADefaultComponent](https://developer.apple.com/documentation/coreservices/1516360-openadefaultcomponent)
- [OpenAComponent](https://developer.apple.com/documentation/coreservices/1516558-openacomponent)
- [CloseComponent](https://developer.apple.com/documentation/coreservices/1516436-closecomponent)

Getting information about components:

- [GetComponentInfo](https://developer.apple.com/documentation/coreservices/1516438-getcomponentinfo)
- `GetComponentIconSuite`
- `GetComponentVersion`
- `ComponentFunctionImplemented`

Retrieving component errors:

- [GetComponentInstanceError](https://developer.apple.com/documentation/coreservices/1516618-getcomponentinstanceerror)

Data types used by applications:

- [ComponentDescription](https://developer.apple.com/documentation/coreservices/componentdescription)
- [ComponentInstanceRecord](https://developer.apple.com/documentation/coreservices/componentinstancerecord)
- [ComponentRecord](https://developer.apple.com/documentation/coreservices/componentrecord)

Component property functions, which are available in QuickTime 6.4 and later, provide another way to get information about components. They can also be used to configure components without a user dialog, to configure a component programmatically, and to set up callbacks that are called when something changes in a component.

The configuration interface to many components, such as those used for capture, export, and compression, involves a standard user dialog. QuickTime-based applications sometimes need to configure these operations from custom user interfaces or to configure them programmatically, with no user interaction at all.

The following functions are available to work with component properties:

- `[QTGetComponentPropertyInfo](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrdwk5cdn5wxa33omvxhiudsn5ygk4tupfew4ztp)` gets information about a specified property of a component, such as the size and data format.
- `[QTGetComponentProperty](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrdwk5cdn5wxa33omvxhiudsn5ygk4tupe)` gets the value of a specific component property.
- `[QTSetComponentProperty](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjwk5cdn5wxa33omvxhiudsn5ygk4tupe)` sets the value of a specific component property programmatically.
- `[QTAddComponentPropertyListener](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrawizcdn5wxa33omvxhiudsn5ygk4tupfggs43umvxgk4q)` installs a callback to monitor a component property. Your callback function is called when the property value changes.
- `[QTRemoveComponentPropertyListener](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjgk3lpozsug33nobxw4zloorihe33qmvzhi6kmnfzxizlomvza)` removes a component property monitoring callback.
- `QTComponentPropertyListenerCollectionCreate` creates a collection of component property monitors, allowing you to manage groups of callback functions.
- `[QTComponentPropertyListenerCollectionAddListener](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrbw63lqn5xgk3tukbzg64dfoj2hstdjon2gk3tfojbw63dmmvrxi2lpnzbxezlborsq)` adds a listener callback for a specified property class and ID to a property listener collection.
- `[QTComponentPropertyListenerCollectionRemoveListener](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrbw63lqn5xgk3tukbzg64dfoj2hstdjon2gk3tfojbw63dmmvrxi2lpnzjgk3lpozsuy2ltorsw4zls)` removes a listener callback with a specified property class and ID from a property listener collection.
- `[QTComponentPropertyListenerCollectionNotifyListeners](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrbw63lqn5xgk3tukbzg64dfoj2hstdjon2gk3tfojbw63dmmvrxi2lpnzhg65djmz4uy2ltorsw4zlsom)` calls all listener callbacks in a component property listener collection registered for a specified property class and ID.
- `[QTComponentPropertyListenerCollectionHasListenersForProperty](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrbw63lqn5xgk3tukbzg64dfoj2hstdjon2gk3tfojbw63dmmvrxi2lpnzegc42mnfzxizlomvzhgrtpojihe33qmvzhi6i)` determines if there are any listeners in a component property listener collection registered for a specified property class and ID.
- `[QTComponentPropertyListenerCollectionIsEmpty](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrbw63lqn5xgk3tukbzg64dfoj2hstdjon2gk3tfojbw63dmmvrxi2lpnzexgrlnob2hs)` determines if a listener collection is empty.

Beginning with Quicktime 6.4, the Component Manager defines optional standard selectors for component properties. These selectors can be implemented by all components, regardless of type, that are written to work with the component properties mechanism. Components can adopt these functions on their own schedule. The Component Manager allows callers to discover safely whether components implement the property selectors and perform operations according to older mechanisms if support for the properties mechanism is unavailable.

As developers adopt the component property functions, it will be possible to configure most or all exporters, for example, by means of the same set of properties. Use of the component property functions allows support for richer scripting and simpler custom user interfaces.

Component resources provide an alternate method of gathering detailed information about components, without opening them and interrogating them. This can be a great time saver when you need to get specific information about a lot of components.

Macintosh programmers should be familiar with the idea of resources, commonly a collection of static data bundled with an application, such as the text strings used in menus and the icon that represents the file. This bundling provides a convenient way to separate data that may be localized to a language, for example, from program code that can be modified only with extreme care.

Resources can be stored inside the file they belong to or in a parallel file, typically a file in the same directory and having the same name, but with a different filename extension. QuickTime provides support for both kinds of resource storage on Windows operating systems. In Mac OS X, resource files are not normally visible; they are bundled inside a folder represented by the parent file’s icon.

QuickTime components can contain resources, which are simply pieces of data. Component resources are typically used as a way for components to store data that is accessed directly only by the component itself. QuickTime 4 and later also supports public resources, which can be accessed by the system and by application programs. Of course, a component can access its own public resources as well.

A component’s resources are identified by an `OSType` value and an ID. A private resource’s `OSType` value and ID are the same as the Mac OS resource type and ID that the resource is identified with in the component’s resource file.

A component’s public resources are also identified by an `OSType` value and an ID, but they do not have to be the same as the Mac OS resource type and ID that the resource is stored in.

A component that provides public component resources must provide a component resource map, which indicates the mapping between the public resource `OSType` and ID and the private `OSType` and ID. Listing 2 shows an example of a component resource map.

__Listing 1-2__  Example of a component resource map

```

resource 'thnr' (512) {
        {
                'PICT', 1, 0,
                'pict', 128, 0,

                'PICT', 2, 0,
                'pict', 129, 0,
        }
}
```

This component resource map makes available two public resources, `'PICT'` `1` and `'PICT'` `2.` The map shows that these two public resources are stored in the component as Mac OS resources `'pict'` `128` and 'pict' `129.`

An application can obtain a public resource from a component by using the [GetComponentPublicResource](https://developer.apple.com/documentation/coreservices/1516336-getcomponentpublicresource) function, as shown in the following code snippet:

```swift
err = GetComponentPublicResource (
   (Component)store->self, 'PICT' , 1, &resource);
```

For each call to [GetComponentPublicResource](https://developer.apple.com/documentation/coreservices/1516336-getcomponentpublicresource), the Component Manager may have to open the component’s resource file and load a resource. Resource caching makes this fast for repeated calls to the same resource, but if many components are to be accessed in turn, the first pass may be quite slow.

Often, however, multiple components of the same type are stored in a single file. QuickTime itself contains nearly a dozen movie exporters, for example. Storing components of the same type in one file makes significant optimization possible; to support this, QuickTime provides the function [GetComponentPublicResourceList](https://developer.apple.com/documentation/coreservices/1516460-getcomponentpublicresourcelist).

[GetComponentPublicResourceList](https://developer.apple.com/documentation/coreservices/1516460-getcomponentpublicresourcelist) is a single optimized call to obtain a specified public resource from each component that matches a component description. Listing 3 is an example that shows how to get all the `'PICT'` `1` public resources from all installed movie exporters. The resources are passed back as an atom container, with each resource in its own atom.

__Listing 1-3__  Getting a resource from all components of a type

```

QTAtomContainer resources;
ComponentDescription cd;

cd.componentType = MovieExportType;
cd.componentSubType = 0;
cd.componentManufacturer = 0;
cd.componentFlags = 0;
cd.componentFlagsMask = 0;

err = GetComponentPublicResourceList ('PICT', 1, 0, &cd, nil, nil, &resources)
```

Once the call to [GetComponentPublicResourceList](https://developer.apple.com/documentation/coreservices/1516460-getcomponentpublicresourcelist) has completed, the QT atom container returned contains all the `'PICT'` `1` public resources for all movie exporters installed. Listing 4 shows how to access these resources.

__Listing 1-4__  Accessing resources from a component resource list

```

long i, count;

count = QTCountChildrenOfType(resources,
kParentAtomIsContainer, OSTypeConst('comp'));
for (i=1; i<=count; i++) {
        QTAtom compAtom, resourceAtom;
        Component c;

        compAtom = QTFindChildByIndex(
   					resources, kParentAtomIsContainer,
   					OSTypeConst('comp'), i, (long *)&c);
        resourceAtom = QTFindChildByID(
   						resources, compAtom, 'PICT', 1, nil);
        if (resourceAtom) {
                Handle resource = NewHandle(0);

                QTCopyAtomDataToHandle(
   					resources, resourceAtom, resource);

                // do something with the resource for Component c

                DisposeHandle(resource);
        }
}

QTDisposeAtomContainer(resources);
```

Notice that the resource atom’s ID is returned as the component atom’s `compAtom` reference.

Although using [GetComponentPublicResourceList](https://developer.apple.com/documentation/coreservices/1516460-getcomponentpublicresourcelist) can take more code, it is often substantially faster than repeated calls to [GetComponentPublicResource](https://developer.apple.com/documentation/coreservices/1516336-getcomponentpublicresource). You can use either approach, but using [GetComponentPublicResourceList](https://developer.apple.com/documentation/coreservices/1516460-getcomponentpublicresourcelist) is recommended as its performance is likely to remain high, especially as more components are added to QuickTime.

[Next](Document%20Revision%20History.md)[Previous](Introduction%20to%20Component%20Manager%20for%20QuickTime.md)

