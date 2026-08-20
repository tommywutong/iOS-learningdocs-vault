---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOLoginPanel.html
archived_at: '2026-07-18T01:28:10.073542Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOJoin.md)
[!](EOModel.md)

---

# EOLoginPanel

__Inherits From:__
NSObject

__Inherits From:__
com.apple.yellow.eoaccess

__Declared in:__

---

## Class Description

EOLoginPanel is an abstract class that defines how users of an Enterprise Objects Framework application provide database login information. Concrete subclasses of EOLoginPanel override its one method to run a modal login panel. Unless you are writing a concrete adaptor subclass, you shouldn't need to interact with this class. Generally, the Framework automatically creates and runs an instance of a concrete login panel object when your application needs connection information for the user. If you want to control when or how the login panel is run, use the EOAdaptor methods [`runLoginPanelAndValidateConnectionDictionary`](EOAdaptor.md#apple-he4dcny) and [`runLoginPanel`](EOAdaptor.md#apple-he3tsny). When invoked, these methods create a concrete EOLoginPanel and interact with it for you.

If you are writing a concrete adaptor, you must provide a concrete subclass of EOLoginPanel and a graphical user interface (usually a `.nib` file). Enterprise Objects Framework expects these resources to be provided in a bundle named "LoginPanel" in the adaptor's framework. See the class specification for EOAdaptor for more information.

---

## Constructors

---

### EOLoginPanel

public com.apple.yellow.eoaccess.`EOLoginPanel`()

Creates and returns an instance of EOLoginPanel.

---

## Instance Methods

---

### administrativeConnectionDictionaryForAdaptor

public NSDictionary `administrativeConnectionDictionaryForAdaptor`(EOAdaptor _adaptor_)

Adaptor subclass should implement a subclass that implements this. Returns `null` if the user cancels the panel.

---

### runPanelForAdaptor

public abstract NSDictionary `runPanelForAdaptor`(
EOAdaptor _adaptor_,
boolean _flag,_
boolean _allowsCreation_)

Implemented by subclasses to run the login panel, allowing a user to enter new connection information. Returns the new connection information or `null` if the user cancels the panel. If _flag_ is true, this method runs the login panel until the user enters valid connection information or cancels the panel. If _allowsCreation_ is true, the panel will have an additional button that allows the user to creat a new database, and will prompt them for any necessary administrative information. When valid login information is entered in the panel, it is stored in _adaptor_'s connection dictionary and returned. Login information is validated by sending _adaptor_ an [`assertConnectionDictionaryIsValid`](EOAdaptor.md#apple-gq4dcmq) message.

If _flag_ is false, login information entered in the panel isn't validated and is returned without affecting the adaptor's connection dictionary.

A subclass must override this method without invoking EOAdaptor's implementation.

__See also:__
[`setConnectionDictionary`](EOAdaptor.md#apple-hezdg) (EOAdaptor), [`assertConnectionDictionaryIsValid`](EOAdaptor.md#apple-gq4dcmq) (EOAdaptor),
[`runLoginPanelAndValidateConnectionDictionary`](EOAdaptor.md#apple-he4dcny) (EOAdaptor),
[`runLoginPanel`](EOAdaptor.md#apple-he3tsny) (EOAdaptor)

---

[!](EOJoin.md)
[!](EOModel.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
