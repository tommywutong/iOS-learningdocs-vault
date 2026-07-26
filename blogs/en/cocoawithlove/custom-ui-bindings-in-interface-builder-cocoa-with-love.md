---
title: 'Custom UI Bindings in Interface Builder | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/03/custom-ui-bindings-in-interface-builder.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:f44dcea8d61842a8'
translated: false
---

> 原文：[Custom UI Bindings in Interface Builder | Cocoa with Love](https://www.cocoawithlove.com/2010/03/custom-ui-bindings-in-interface-builder.html)　·　Cocoa with Love (Matt Gallagher)

In my [last post](https://www.cocoawithlove.com/2010/03/designing-view-with-bindings.html), I showed how you might redesign the interface to the iPhone's `UITableView` if you wanted to reimplement it on the Mac using Cocoa Bindings. This time, I'll show you how to make those bindings editable in Interface Builder so you can use the entire class with no code at all.

## Introduction

I'm going to use integration with Interface Builder to construct a simple browser for the Address Book using the `ColumnView` class to select entries:

![](https://www.cocoawithlove.com/assets/objc-era/abbrowser.png)

The column on the left is handled by the `ColumnView` class, a class which supports layout of rows in sections, with variable row heights, variable row classes and selection.

In fact, if the `ABAddressBook` and its children were KVO compliant, there would be no project-specific code in this program at all (just the generic `ColumnView` class, its children and default application template code).

> ColumnViewSample.zip
> 
> (70kb)

## Interface Builder integration

Last time, I focussed on [designing a view for use with bindings](https://www.cocoawithlove.com/2010/03/designing-view-with-bindings.html) in code and didn't look at integrating that effort with Interface Builder.

The redesign eliminated all 7 controller methods that would ordinarily be required to configure a `UITableView`.

However, the code still required a great big binding instruction:

```objc
[columnView
    bind:ColumnViewSectionArrayBinding
    toObject:[[AddressBookDataController sharedController] groupsController]
    withKeyPath:@"arrangedObjects"
    options:
        [NSDictionary dictionaryWithObjectsAndKeys:
            @"members", ColumnViewSectionContentKeyOption,
            kABGroupNameProperty, ColumnViewSectionHeaderDataKeyOption,
            @"Last", ColumnSectionRowDisplayKeyOption,
        nil]];
```

to hook everything together.

The purpose of Interface Builder integration is to eliminate even this statement; instead, the entire program can be set up using data alone.

## Setting up an IBPlugin

The first required step is to setup an Interface Builder plugin for the `ColumnView` class.

I've previously written a post showing [all the steps required to create an IBPlugin for a view class](https://www.cocoawithlove.com/2009/07/custom-views-in-interface-builder-using.html). These are the steps I followed.

The _ColumnPlugin_ project is in a subfolder of the _ColumnViewSample_ project folder. You must build and run _ColumnPlugin_ in the Release configuration to install it in your `~/Library/Frameworks` directory. After that, you will be able to use the `ColumnView`'s bindings in Interface Builder.

> You will get an error — Unable to resolve plug-in dependency for "ColumnViewSampleWindow.xib" — unless you build the "Release" build of ColumnPlugin.xcodeproj before you build the ColumnViewSample project.

## Exposing bindings

Of course, the only reason why building the _ColumnPlugin_ project will allow you to use the `ColumnView`'s bindings is because the `ColumnView` class implements methods which enable Interface Builder integration. Let's look at how that works.

The first required step is to expose the binding. This is very simple, just invoke the `exposeBinding:` method in the `+intialize` method for the class.

```objc
+ (void)initialize
{
    if (self == [ColumnView class])
    {
        [self exposeBinding:ColumnViewSectionsArrayBinding];
    }
}
```

The string `ColumnViewSectionsArrayBinding` is initialized as `sectionsArray`, so this binding affects the `sectionsArray` property on `ColumnView`.

If you select an object with a binding like this, it will appear in Interface Builder's bindings panel (select the object and press Command-4) at the bottom under the "Parameters" section.

## Custom binding options

If you add no other support, this will be sufficient to support basic binding of an arbitrary object to this property.

However, I designed my class to expect a number of keys to be set at the same time as the binding. These include:

- —A key path (relative to each section object) where the rows array can be found (if not present, it is assumed that the section

  the rows array).
- — A key path (relative to each section object) where the default class to use for all rows in the section can be found (if not present the default

  class is used). This property is overridden by the

  .
- — A key path (relative to each row object) where the class for the row can be found (if not present, it is assumed the section

  the rows array).
- — A key path (relative to each row object) where a separate object used for display is found (if not present, the row object is used directly for display).
- — A key path (relative to each section object) where the object for the header is found (if not present, no header is shown for the section).
- — A key path (relative to each section object) where the class for the header row is found (if not present, the default

  class is used).
- — A key path (relative to each row object) by which every section should be sorted.
- — A key path (relative to each section object) where the key by which that section should be sorted can be found (this will override the allSectionsSortKey).

So we need to set up these properties as editable fields in the bindings editor.

The primary way to set up the options for a binding is through the `optionDescriptionForBinding:` method:

```objc
- (NSArray *)optionDescriptionsForBinding:(NSString *)binding
{
    if ([binding isEqualToString:ColumnViewSectionsArrayBinding])
    {
        NSArray *options =
            [NSArray arrayWithObjects:
                AttributeDescription(ColumnViewSectionContentKeyOption, sectionContentKey ? sectionContentKey : @"self"),
                AttributeDescription(ColumnSectionRowDisplayKeyOption, rowDisplayKey),
                AttributeDescription(ColumnSectionClassKeyOption, sectionClassKey),
                AttributeDescription(ColumnSectionRowClassKeyOption, rowClassKey),
                AttributeDescription(ColumnViewSectionHeaderDataKeyOption, sectionHeaderDataKey),
                AttributeDescription(ColumnViewSectionHeaderClassKeyOption, sectionHeaderClassKey),
                AttributeDescription(ColumnViewAllSectionsSortKeyOption, allSectionsSortKey),
                AttributeDescription(ColumnViewSectionRowSortKeyOption, sectionRowSortKey),
            nil];
        return options;
    }
    
    return [super optionDescriptionsForBinding:binding];
}
```

Here `AttributeDescription` is just a helper method to create an `NSAttributeDescription` object.

## Fixing custom bindings so they work

Having made it this far with my design and Interface Builder integration I discovered that Interface Builder doesn't support custom bindings options.

If you try to use a bindings option that isn't on [Apple's official list of Bindings Options](http://developer.apple.com/Mac/library/documentation/Cocoa/Reference/CocoaBindingsRef/Concepts/BindingsOptions.html#//apple_ref/doc/uid/20002304-BAJEAIEE), the option will get set on your class briefly and then immediately cleared.

There is a fix for this unfortunate behavior: get the values when they are initially set, save them to persistent attributes (which you need to inform Interface Builder about) and then ignore any attempt in Interface Builder to set your options to `nil`.

Informing Interface Builder you have persistent attributes is done in the _CustomViewIntegration.m_ file of the ColumnPlugin:

```objc
- (void)ibPopulateKeyPaths:(NSMutableDictionary *)keyPaths {
    [super ibPopulateKeyPaths:keyPaths];
    
    [[keyPaths objectForKey:IBAttributeKeyPaths]
        addObjectsFromArray:
            [NSArray arrayWithObjects:
                ColumnViewSectionContentKeyOption,
                ColumnSectionRowDisplayKeyOption,
                ColumnSectionClassKeyOption,
                ColumnSectionRowClassKeyOption,
                ColumnViewSectionHeaderDataKeyOption,
                ColumnViewSectionHeaderClassKeyOption,
                ColumnViewAllSectionsSortKeyOption,
                ColumnViewSectionRowSortKeyOption,
            nil]];
}
```

This will make sure that Interface Builder tracks these values in Undo/Redo.

After this is done, you need to ensure the attributes are saved when the Interface Builder file is saved by implementing `encodeWithCoder` on the `ColumnView` itself:

```objc
- (void)encodeWithCoder:(NSCoder *)encoder
{
    [super encodeWithCoder:encoder];
    [encoder encodeObject:sectionContentKey forKey:ColumnViewSectionContentKeyOption];
    [encoder encodeObject:rowDisplayKey forKey:ColumnSectionRowDisplayKeyOption];
    // And so on the for the other 6 properties...
```

and load them correctly when the NIB file is loaded:

```objc
- (id)initWithCoder:(NSCoder *)decoder
{
    self = [super initWithCoder:decoder];
    if (self != nil)
    {
        sectionContentKey = [[decoder decodeObjectForKey:ColumnViewSectionContentKeyOption] retain];
        rowDisplayKey = [[decoder decodeObjectForKey:ColumnSectionRowDisplayKeyOption] retain];
        // And so on the for the other 6 properties...
```

and finally, ensure that any attempt by Interface Builder to set them to `nil` is ignored:

```objc
- (void)bind:(NSString *)bindingName toObject:(id)observedObject
    withKeyPath:(NSString *)observedKeyPath options:(NSDictionary *)options
{
    if ([bindingName isEqualToString:ColumnViewSectionsArrayBinding])
    {
        // ...Other work associated with setting the binding goes here...
        
        if ([options objectForKey:ColumnViewSectionContentKeyOption])
        {
            self.sectionContentKey = [options objectForKey:ColumnViewSectionContentKeyOption];
            self.rowDisplayKey = [options objectForKey:ColumnSectionRowDisplayKeyOption];
            // ...and so on..
        }

        // ... and so on for the other bindings
```

What I have done is considered the `ColumnViewSectionContentKeyOption` option a mandatory inclusion — this will allow me to detect if Interface Builder is improperly setting my bindings options to nil or if the setting is valid. If there is no value for the `ColumnViewSectionContentKeyOption` key in the dictionary then the options are considered invalid and will be skipped — leaving them at their previous values and allowing us to save them in `initWithCoder:` when the file is saved.

## Setting it all up in Interface Builder

Now that we have Interface Builder integration, hooking up the components in Interface Builder for our program is easy.

### Provide the ColumnView with data

An `NSArrayController` with the Address Book Data Controller's `groups` array as its content is bound to the `sectionArray` of our `ColumnView`. `ColumnView` prefers that you use an `NSArrayController` for the top-level content (instead of directly binding an `NSArray`), since it can use the selection and sorting from the `NSArrayController` for the sections in the view.

The `sectionArray` binding has the "section Content Key", "row Display Key", "section Header Data Key" and "section Row Sort Key" values filled in, so the ColumnView will know where to find the rows for each section, the object used to display the row, the name for each section and the sort order for each section respectively.

### Update the detail view when the selection changes

The `ColumnView` has a KVO-compliant `selectedSectionArrayController` property which returns the `NSArrayController` for the content in the selected section. Using the `selection` property of this `NSArrayController`, we can get the selected row's data.

To bind this `selectedSectionArrayController` property, we need to add an `NSObjectController` at the top level which will have our `ColumnView` connected to its `content` outlet.

By binding all of the text fields in the detail view through this controller, their values will all update based on the current selection. i.e. the "First Name" text field is bound to the `NSObjectController`, with the controller key `selection` and the model key `selectedSectionArrayController.selection.First`.

Fields will automatically show "No selection" and "(None)" when there is no selection or a given selection does not contain a value for the field.

## Conclusion

> ColumnViewSample.zip
> 
> (70kb)

The final ColumnViewSample project shows a Master-Detail-style interface, constructed with almost no code. This is due to classes which are designed to work with bindings. A code-less implementation only works when when your classes are fully KVC and KVO compliant as bindings cannot operate without these design patterns.

Implementing custom bindings options in Interface Builder for the various key-path options wasn't totally necessary — you can set basic string keys like these in a normal Interface Builder Attributes panel — but I wanted to keep these keys closely associated with the binding. As an added benefit, this approach allowed me to use Interface Builder's built-in interface for editing these fields, rather than requiring that I implement my own.

`ColumnView` remains a fairly basic replication of `UITableView`-like functionality for the Mac. There is no `UINavigationController` for drill-down hierarchies. It lacks the animation and edit modes of `UITableView`. It does not attempt to reuse `RowView`s for efficiency like `UITableView` does. Nor have I really tested it thoroughly — it was just an experiment on my part.

Despite these shortcomings, if you want section-based layout of views though and you're prepared to add other features as you need them, `ColumnView` may be useful as an alternative to `NSCollectionView` or `NSTableView`.
